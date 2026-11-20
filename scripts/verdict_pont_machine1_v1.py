# -*- coding: ascii -*-
"""FEUILLE DE VERDICT, gel "pont" -- machine 1, v1, 2026-11-17.
Applique aux lectures (lecture_densite_2d_pont et lecture_boites_pont) les enonces de la seconde partie du gel, la
CELLULE pour unite. Les constantes ci-dessous sont celles du gel ; cette feuille ne recalcule aucune lecture.
(L)  cellule LISIBLE si au moins 10 des 12 ecarts le sont ; elle TIENT si, a chaque ecart lisible, |ln R3(x)| <= 0.05.
(L2) cellule lisible pour (L) ; elle TIENT si, a chaque ecart lisible x >= 5, |ln R3| < |ln R2|.
(S)  cellule LISIBLE si chaque groupe de cotes compte au moins 8 boites lisibles ; elle TIENT si la moyenne de S sur
       toutes ses boites lisibles est dans [0.85, 1.15] ET si la moyenne de chaque groupe est dans [0.80, 1.20].
(C)  cellule LISIBLE si chaque groupe compte au moins 8 boites de compte valide ; elle TIENT si, dans chaque groupe,
       le COMPTE REDUIT (moyenne de n) / (moyenne des cotes x 7.95 x |delta|) est dans [0.33, 0.55] ET si le rapport de
       la moyenne de n du groupe DEUX a celle du groupe UN est dans [1.25, 1.85].
Groupes : UN = cotes 180 a 189 ; DEUX = cotes 291 a 300.
Une famille est TENUE si aucune cellule lisible ne tombe et si au moins quatre cellules sont lisibles, dont une au
moins par creneau ; TOMBEE si une cellule lisible tombe ; NON JUGEE sinon.
Sans jugement : (Q1) la moyenne de S toutes boites lisibles confondues ; (Q2) les parts sont-elles egales (rapport de
la moyenne de 1 / participation a celle de 3 / (n + 2)) ; (Q3) la somme relue avec la densite 2D (y divise par R3 a
l'ecart du niveau, ln R3 interpole lineairement en x entre les ecarts lisibles) ; (Q4) le vide.
Usage : python3 -I -B verdict_pont_machine1_v1.py <chaine_cellules.json> <lecture_boites.json> <sortie.json>
                      <lecture_densite MG3> <MG4> <MG5> <PG3> <PG4> <PG5>
        REPETITION, hors gel : ... <sortie.json> --repetition <un-debut> <un-fin> <deux-debut> <deux-fin> <min boites>
                      <nom=lecture_densite> [...]"""
import sys, json, math
CHAINE, BOITES, SORTIE = sys.argv[1:4]; reste = sys.argv[4:]
CELLULES = ("MG3", "MG4", "MG5", "PG3", "PG4", "PG5"); UN = (180, 189); DEUX = (291, 300); MIN_BOITES = 8
TOL_L, MIN_ECARTS, X_L2 = 0.05, 10, 5.0
S_CELLULE, S_GROUPE = (0.85, 1.15), (0.80, 1.20); C_REDUIT, C_RAPPORT = (0.33, 0.55), (1.25, 1.85)
REPETITION = bool(reste and reste[0] == "--repetition")
if REPETITION:
    UN = (int(reste[1]), int(reste[2])); DEUX = (int(reste[3]), int(reste[4])); MIN_BOITES = int(reste[5])
    paires = [a.split("=") for a in reste[6:]]; CELLULES = tuple(n for n, _ in paires); DENS = {n: f for n, f in paires}
    print("REPETITION, CE N'EST PAS UN VERDICT : cellules %s, groupes %s et %s, au moins %d boites" % (" ".join(CELLULES), UN, DEUX, MIN_BOITES))
else:
    assert len(reste) == 6; DENS = dict(zip(CELLULES, reste))
CH = json.load(open(CHAINE)); X = CH["ecarts"]; LB = json.load(open(BOITES))
def moyenne(v): return sum(v) / len(v)
def ecart_type(v):
    m = moyenne(v); return math.sqrt(sum((x - m) ** 2 for x in v) / (len(v) - 1)) if len(v) > 1 else float("nan")
def dans(v, b): return b[0] <= v <= b[1]
out = {"repetition": REPETITION, "cellules": {}, "familles": {}, "questions": {}}
toutes_S = []; par_groupe = {"UN": [], "DEUX": []}
for nom in CELLULES:
    c = CH["cellules"][nom]; d = json.load(open(DENS[nom])); r = {"w2": c["w2"], "m": c["m"], "g": c["g"]}
    assert (d["w2"], d["m"], d["g"]) == (c["w2"], c["m"], c["g"]) and d["X"] == X
    # (L) et (L2)
    lis = [(i, p) for i, p in enumerate(d["par_x"]) if p["lisible"]]
    tol = [TOL_L for i in range(len(X))]
    r["L"] = {"ecarts_lisibles": len(lis), "tolerance": TOL_L}
    if len(lis) < MIN_ECARTS:
        r["L"]["verdict"] = "ILLISIBLE"; r["L2"] = {"verdict": "ILLISIBLE"}
    else:
        hors = [X[i] for i, p in lis if not abs(p["ln_R3"]) <= tol[i]]
        pire = max(lis, key=lambda t: abs(t[1]["ln_R3"]) / tol[t[0]])
        r["L"].update({"verdict": "TIENT" if not hors else "TOMBE", "ecarts_hors_tolerance": hors, "ln_R3": [p.get("ln_R3") for p in d["par_x"]],
                       "pire_ecart": X[pire[0]], "pire_ln_R3": pire[1]["ln_R3"], "pire_part_de_tolerance": abs(pire[1]["ln_R3"]) / tol[pire[0]]})
        gr = [(X[i], p) for i, p in lis if X[i] >= X_L2]
        pas_mieux = [x for x, p in gr if not abs(p["ln_R3"]) < abs(p["ln_R2"])]
        r["L2"] = {"verdict": ("TIENT" if not pas_mieux else "TOMBE") if gr else "ILLISIBLE", "ecarts_juges": [x for x, p in gr],
                   "ecarts_ou_l_ordre_2_est_plus_pres": pas_mieux}
    # (S) et (C)
    bs = [b for cel in LB["cellules"] if (cel["w2"], cel["m"], cel["g"]) == (c["w2"], c["m"], c["g"]) for b in cel["boites"]]
    g = {"UN": [b for b in bs if UN[0] <= b["cote"] <= UN[1]], "DEUX": [b for b in bs if DEUX[0] <= b["cote"] <= DEUX[1]]}
    assert all(len(set(b["cote"] for b in v)) == len(v) for v in g.values()), "un cote en double"
    Sg = {k: [b["S"] for b in v if b["lisible"]] for k, v in g.items()}; ng = {k: [b["n"] for b in v if b["compte_valide"]] for k, v in g.items()}
    cg = {k: [b["cote"] for b in v if b["compte_valide"]] for k, v in g.items()}
    r["S"] = {"boites_lisibles": {k: len(v) for k, v in Sg.items()}}
    if min(len(v) for v in Sg.values()) < MIN_BOITES:
        r["S"]["verdict"] = "ILLISIBLE"
    else:
        tous = Sg["UN"] + Sg["DEUX"]; mo = moyenne(tous); mg = {k: moyenne(v) for k, v in Sg.items()}
        ok = dans(mo, S_CELLULE) and all(dans(v, S_GROUPE) for v in mg.values())
        r["S"].update({"verdict": "TIENT" if ok else "TOMBE", "moyenne": mo, "erreur": ecart_type(tous) / math.sqrt(len(tous)),
                       "moyenne_par_groupe": mg, "ecart_type_par_groupe": {k: ecart_type(v) for k, v in Sg.items()}})
        toutes_S += [(nom, s) for s in tous]
    r["C"] = {"boites_de_compte_valide": {k: len(v) for k, v in ng.items()}}
    if min(len(v) for v in ng.values()) < MIN_BOITES:
        r["C"]["verdict"] = "ILLISIBLE"
    else:
        mn = {k: moyenne(v) for k, v in ng.items()}; rap = mn["DEUX"] / mn["UN"]
        red = {k: mn[k] / (moyenne(cg[k]) * LB["largeur"] * abs(c["delta"])) for k in mn}
        ok = all(dans(v, C_REDUIT) for v in red.values()) and dans(rap, C_RAPPORT)
        r["C"].update({"verdict": "TIENT" if ok else "TOMBE", "moyenne_par_groupe": mn, "compte_reduit": red, "rapport": rap})
    # (Q2), (Q3), (Q4)
    for k, v in g.items():
        par_groupe[k] += [(1.0 / b["participation"], 3.0 / (b["n"] + 2)) for b in v if b["lisible"] and b["n"]]
    if lis:
        xi = [X[i] for i, p in lis]; li = [p["ln_R3"] for i, p in lis]
        def lnR(x):
            if x <= xi[0]: return li[0]
            if x >= xi[-1]: return li[-1]
            j = max(k for k in range(len(xi)) if xi[k] <= x); t = (x - xi[j]) / (xi[j + 1] - xi[j]); return li[j] + t * (li[j + 1] - li[j])
        Sd = [sum(y * math.exp(-lnR(x)) for x, y in zip(b["x"], b["y"])) / LB["largeur"] for v in g.values() for b in v if b["lisible"]]
        r["Q3_somme_avec_la_densite_2d"] = {"boites": len(Sd), "moyenne": moyenne(Sd) if Sd else None}
    r["Q4_vide_ln_chaine3_sur_2d"] = {a: v["ln_chaine3_sur_2d"] for a, v in d["vide"].items()}
    out["cellules"][nom] = r
    print("%-4s (L) %-9s %s | (L2) %-9s | (S) %-9s %s | (C) %-9s %s" % (nom, r["L"]["verdict"],
          "" if r["L"]["verdict"] == "ILLISIBLE" else "pire %+.4f a x = %g (%.2f de la tolerance)" % (r["L"]["pire_ln_R3"], r["L"]["pire_ecart"], r["L"]["pire_part_de_tolerance"]),
          r["L2"]["verdict"], r["S"]["verdict"],
          "" if r["S"]["verdict"] == "ILLISIBLE" else "%.4f +- %.4f (UN %.4f, DEUX %.4f)" % (r["S"]["moyenne"], r["S"]["erreur"], r["S"]["moyenne_par_groupe"]["UN"], r["S"]["moyenne_par_groupe"]["DEUX"]),
          r["C"]["verdict"],
          "" if r["C"]["verdict"] == "ILLISIBLE" else "n %.2f et %.2f (reduits %.3f et %.3f), rapport %.3f" % (r["C"]["moyenne_par_groupe"]["UN"], r["C"]["moyenne_par_groupe"]["DEUX"],
          r["C"]["compte_reduit"]["UN"], r["C"]["compte_reduit"]["DEUX"], r["C"]["rapport"])))
for fam in ("L", "L2", "S", "C"):
    v = {n: out["cellules"][n][fam]["verdict"] for n in CELLULES}
    lisibles = [n for n in CELLULES if v[n] != "ILLISIBLE"]; tombees = [n for n in CELLULES if v[n] == "TOMBE"]
    creneaux = set(n[:2] for n in lisibles); tous_creneaux = set(n[:2] for n in CELLULES)
    if tombees: verdict = "TOMBEE"
    elif len(lisibles) >= min(4, len(CELLULES)) and creneaux == tous_creneaux: verdict = "TENUE"
    else: verdict = "NON JUGEE"
    out["familles"][fam] = {"verdict": verdict, "lisibles": lisibles, "tombees": tombees}
    print("FAMILLE (%s) : %s ; cellules lisibles %d sur %d%s" % (fam, verdict, len(lisibles), len(CELLULES), "" if not tombees else " ; tombees : " + " ".join(tombees)))
if toutes_S:
    s = [x for _, x in toutes_S]; mo = moyenne(s); er = ecart_type(s) / math.sqrt(len(s))
    out["questions"]["Q1"] = {"boites": len(s), "moyenne": mo, "erreur": er, "exces_en_erreurs": (mo - 1.0) / er if er == er and er > 0 else None}
    print("(Q1) somme, %d boites lisibles confondues : %.4f +- %.4f" % (len(s), mo, er))
for k, v in par_groupe.items():
    if v:
        out["questions"]["Q2_" + k] = {"boites": len(v), "rapport": moyenne([a for a, _ in v]) / moyenne([b for _, b in v])}
        print("(Q2) groupe %s, %d boites : rapport %.3f (parts tirees d'une loi de Porter-Thomas : 1)" % (k, len(v), out["questions"]["Q2_" + k]["rapport"]))
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
print("ecrit : %s%s" % (SORTIE, " (REPETITION)" if REPETITION else ""))
