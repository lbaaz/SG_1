# -*- coding: ascii -*-
"""LECTURE DE LA CARTE -- machine 1, v1, 2026-11-15. Hors chaine. Arithmetique sur les sorties de carte_chaine_machine1_v1.py
et sur le depot du delta 98 ; aucun calcul de chaine ni de 2D ici.
(A) Ce que vaut la carte comme prediction, aux seize points deja joues : boite, etiquettes lues, passage du plancher.
(B) La grille : par cellule (delta, facteur), boite, etats predits jugeables, dans le domaine de l'ordre 3, discriminants.
(C) Les balayages en couplage : a w2 fixe, les etiquettes dans le domaine a plusieurs facteurs, et ce que la chaine y predit.
Usage : python3 -I lecture_carte_machine1_v1.py <carte_depot.json> <carte_neg.json> <carte_pos.json> <sonde_ordre2.json>
        <verdict_ordre2.json> <sortie.json>"""
import sys, json, math, statistics
from fractions import Fraction as F
CDEP, CNEG, CPOS, DEP, V98, SORTIE = sys.argv[1:7]
PLANCHER10 = 1.33e-12; E_MAX = 0.7; STAB_MAX = 0.05; DISC_MIN = 0.05; DISC_FIN = 0.02; N_ETATS = 14
N_COUT = 74; JUG_MIN = 8; DOM_MIN = 5       # regle d'eligibilite PROPOSEE (rien n'est gele) ; 74 : la plus grande boite deja jouee (M3, L4)
# couples (w2, facteur) deja joues : gel du delta 98, section 4 (M17, gel "hors plage", gel "garde G-1"), et ses seize points
JOUES = set()
for w, f in ([(x, "1") for x in ("195/100", "197/100", "198/100", "202/100", "203/100", "205/100", "185/100", "190/100", "196/100", "204/100", "210/100", "215/100",
                                  "208/100", "209/100", "191/100", "212/100", "189/100")]
             + [(x, f) for x in ("195/100", "205/100") for f in ("3/2", "2/3")] + [(x, "3/2") for x in ("210/100", "212/100", "190/100")]
             + [(x, "2/3") for x in ("208/100", "210/100", "191/100", "190/100")]):
    JOUES.add((F(w), F(f)))
D = {p["id"]: p for p in json.load(open(DEP))["points"]}; V = {p["id"]: p for p in json.load(open(V98))["points"]}
for p in D.values():
    JOUES.add((F(p["w2"]), F(p["facteur"])))
med = statistics.median

def lire(e):
    """Classement d'une etiquette par la chaine seule."""
    if e["vide"]:
        return {"jug": False, "dom": False, "disc": False, "disc2": False, "G": None}
    dans = e["e_bord"] < E_MAX and e["stab3"] is not None and e["stab3"] <= STAB_MAX
    G = e["G3"] if dans else e["G2"][2]
    jug = bool(e["stable1"] and e["stable2"] and G > PLANCHER10)
    ec = abs(math.log(e["G2"][2] / e["G3"])) if (jug and dans) else 0.0
    return {"jug": jug, "dom": bool(jug and dans), "disc": bool(jug and dans and ec >= DISC_MIN), "disc2": bool(jug and dans and ec >= DISC_FIN), "G": G, "ecart_23": ec}

out = {"reglage": {"plancher10": PLANCHER10, "e_max": E_MAX, "stab_max": STAB_MAX, "disc_min": DISC_MIN, "disc_fin": DISC_FIN, "n_etats": N_ETATS, "N_cout": N_COUT, "jug_min": JUG_MIN, "dom_min": DOM_MIN}}
# ---------------- (A)
print("(A) LA CARTE COMME PREDICTION, AUX SEIZE POINTS DEJA JOUES (depot du delta 98)")
print("    id   boite, graine, g   etiquettes lues dans les 14 predites (dans les 16)   juges   plancher : bien predit / lus a etiquette unique")
A = {"points": {}, "boite": 0, "lues": 0, "dans14": 0, "dans16": 0, "plancher_ok": 0, "plancher_n": 0, "VP": 0, "FP": 0, "FN": 0, "VN": 0}
for c in json.load(open(CDEP))["cellules"]:
    p = D[c["id"]]; v = {e["rang"]: e for e in V[c["id"]]["etats"]}
    ok = bool(c["r_c"] == p["r_c"] and c["N"] == p["N"] and abs(c["g"] / p["g"] - 1) < 1e-12 and max(abs(a - b) for a, b in zip(c["graine"], p["graine"])) < 1e-10)
    lus = [(e["n1"], e["n2"]) for e in p["etats"]]; dist = sorted(set(lus)); pred = {(e["n1"], e["n2"]): e for e in c["etats"]}
    p14 = [k for k, e in pred.items() if e["rang_predit"] is not None and e["rang_predit"] < N_ETATS]; p16 = [k for k, e in pred.items() if e["rang_predit"] is not None]
    n14 = sum(l in p14 for l in dist); n16 = sum(l in p16 for l in dist); vp = fp = fn = vn = 0
    for e in p["etats"]:
        lab = (e["n1"], e["n2"])
        if lus.count(lab) > 1:
            continue
        m = pred[lab]; reel = e["Gamma_2D"]["3"] > PLANCHER10; pr = (not m["vide"]) and m["G2"][2] > PLANCHER10
        if not m["vide"] and e["chaine2"]["definie"]:
            assert abs(m["G2"][2] / e["chaine2"]["gammas_flux"][2] - 1) < 1e-6, (c["id"], lab)
        vp += reel and pr; fp += (not reel) and pr; fn += reel and (not pr); vn += (not reel) and (not pr)
    A["points"][c["id"]] = {"boite": ok, "lues": len(dist), "dans14": n14, "dans16": n16, "juges": V[c["id"]]["n_juges"], "VP": vp, "FP": fp, "FN": fn, "VN": vn}
    A["boite"] += ok; A["lues"] += len(dist); A["dans14"] += n14; A["dans16"] += n16
    for k, x in (("VP", vp), ("FP", fp), ("FN", fn), ("VN", vn)):
        A[k] += x
    print("    %-3s  %-17s  %2d sur %2d (%2d)                                       %2d      %2d / %2d" % (c["id"], "identiques" if ok else "DIFFERENTS", n14, len(dist), n16,
          V[c["id"]]["n_juges"], vp + vn, vp + fp + fn + vn))
A["plancher_ok"] = A["VP"] + A["VN"]; A["plancher_n"] = A["VP"] + A["FP"] + A["FN"] + A["VN"]
print("    total : boite, graine et couplage identiques a %d points sur %d ; etiquettes lues : %d sur %d dans les 14 predites, %d dans les 16 ;" % (A["boite"], len(A["points"]), A["dans14"], A["lues"], A["dans16"]))
print("            passage du plancher bien predit pour %d etats sur %d (au-dessus a tort %d, au-dessous a tort %d)" % (A["plancher_ok"], A["plancher_n"], A["FP"], A["FN"]))
out["A"] = A
# ---------------- (B)
cells = json.load(open(CNEG))["cellules"] + json.load(open(CPOS))["cellules"]
facteurs = sorted(set(F(c["facteur"]) for c in cells)); deltas = sorted(set(round(c["delta"], 2) for c in cells))
G = {}
for c in cells:
    es = [e for e in c["etats"] if e["rang_predit"] is not None and e["rang_predit"] < N_ETATS]; ls = [lire(e) for e in es]
    jug = [(e, l) for e, l in zip(es, ls) if l["jug"]]; dom = [(e, l) for e, l in jug if l["dom"]]
    joue = (F(c["w2"]), F(c["facteur"])) in JOUES
    r = {"w2": c["w2"], "delta": round(c["delta"], 2), "facteur": c["facteur"], "g": c["g"], "graine": c["graine"], "N": c["N"], "faisable": c["faisable"], "joue": joue,
         "cout": (c["N"] / 60.0) ** 6, "n_jug": len(jug), "n_dom": len(dom), "n_disc": sum(l["disc"] for e, l in dom), "n_disc2": sum(l["disc2"] for e, l in dom),
         "ecart_23_med": med([l["ecart_23"] for e, l in dom]) if dom else None, "signe_23": (sum(e["G2"][2] > e["G3"] for e, l in dom), len(dom)), "n_vide": sum(e["vide"] for e in es),
         "e_bord_med": med([e["e_bord"] for e, l in jug]) if jug else None, "lgG_min": math.log10(min(l["G"] for e, l in jug)) if jug else None,
         "lgG_max": math.log10(max(l["G"] for e, l in jug)) if jug else None,
         "dom": {"%d,%d" % (e["n1"], e["n2"]): {"G3": e["G3"], "G2": e["G2"][2], "e_bord": e["e_bord"], "m_bord": e["m_bord"], "disc": l["disc"]} for e, l in dom}}
    r["eligible"] = bool(r["faisable"] and r["N"] <= N_COUT and r["n_jug"] >= JUG_MIN and r["n_dom"] >= DOM_MIN and not joue)
    G[(r["delta"], F(c["facteur"]))] = r
def table(titre, f):
    print(titre)
    print("    delta  " + "".join("%9s" % str(x) for x in facteurs))
    for d in deltas:
        print("    %+.2f  " % d + "".join("%9s" % f(G[(d, x)]) for x in facteurs))
print("(B) LA GRILLE : %d cellules, |delta| de 0.02 a 0.12, facteur sur g_du_point de %s a %s ; etats = les %d etiquettes de plus grand poids de la graine" % (len(G), facteurs[0], facteurs[-1], N_ETATS))
table("  (B1) boite N de la sonde dense (j : couple deja joue ; ! : infaisable, N > 120)", lambda r: "%d%s" % (r["N"], "!" if not r["faisable"] else ("j" if r["joue"] else "")))
table("  (B2) etats predits jugeables / dans le domaine de l'ordre 3 / discriminants (ordre 2 et ordre 3 a plus de 5 pour cent l'un de l'autre)",
      lambda r: "%d/%d/%d" % (r["n_jug"], r["n_dom"], r["n_disc"]))
table("  (B2 bis) dans le domaine : etats ou les deux ordres different de plus de 2 pour cent / ecart median |ln(ordre 2 / ordre 3)|",
      lambda r: ("%d/%.3f" % (r["n_disc2"], r["ecart_23_med"])) if r["ecart_23_med"] is not None else "-")
table("  (B3) desaccord au bout de la barriere, mediane des etats jugeables", lambda r: ("%.2f" % r["e_bord_med"]) if r["e_bord_med"] is not None else "-")
table("  (B4) log10 de la largeur predite, du plus petit au plus grand etat jugeable", lambda r: ("%.0f:%.0f" % (r["lgG_min"], r["lgG_max"])) if r["lgG_min"] is not None else "-")
table("  (B5) cellule eligible a la regle proposee (faisable, N <= %d, au moins %d jugeables dont %d dans le domaine, couple jamais joue)" % (N_COUT, JUG_MIN, DOM_MIN),
      lambda r: "oui" if r["eligible"] else ".")
el = [k for k, r in G.items() if r["eligible"]]
print("    cellules eligibles : %d sur %d ; delta < 0 : %d ; delta > 0 : %d ; par |delta| : %s" % (len(el), len(G), sum(k[0] < 0 for k in el), sum(k[0] > 0 for k in el),
      ", ".join("%.2f : %d-/%d+" % (a, sum(k[0] == -a for k in el), sum(k[0] == a for k in el)) for a in sorted(set(abs(d) for d in deltas)))))
# resumes
R = {"eligibles": len(el), "eligibles_neg": sum(k[0] < 0 for k in el), "eligibles_pos": sum(k[0] > 0 for k in el), "cellules": len(G)}
for nom, sg in (("neg", -1), ("pos", 1)):
    R["delta_max_dom_" + nom] = max([abs(k[0]) for k, r in G.items() if k[0] * sg > 0 and r["n_dom"] >= DOM_MIN] or [0.0])
    R["delta_max_dom_plein_" + nom] = max([a for a in sorted(set(abs(d) for d in deltas)) if all(G[(sg * b, x)]["n_dom"] == G[(sg * b, x)]["n_jug"] for b in sorted(set(abs(d) for d in deltas)) if b <= a
                                           for x in facteurs if F(3, 4) <= x <= F(1))] or [0.0])
    R["cellules_disc5_" + nom] = sorted(["%+.2f x %s" % (k[0], k[1]) for k, r in G.items() if k[0] * sg > 0 and r["n_disc"] >= DOM_MIN])
    R["cellules_disc2_" + nom] = len([1 for k, r in G.items() if k[0] * sg > 0 and r["n_disc2"] >= DOM_MIN])
    R["cellules_dom_" + nom] = len([1 for k, r in G.items() if k[0] * sg > 0 and r["n_dom"] >= DOM_MIN])
    R["ordre2_au_dessus_" + nom] = [sum(r["signe_23"][0] for k, r in G.items() if k[0] * sg > 0), sum(r["signe_23"][1] for k, r in G.items() if k[0] * sg > 0)]
R["e_bord_sur_delta"] = {str(x): [min(G[(d, x)]["e_bord_med"] / abs(d) for d in deltas if G[(d, x)]["e_bord_med"] is not None), max(G[(d, x)]["e_bord_med"] / abs(d) for d in deltas if G[(d, x)]["e_bord_med"] is not None)]
                         for x in facteurs}
R["N_eligibles"] = [min(G[k]["N"] for k in el), max(G[k]["N"] for k in el)]; R["lgG_eligibles"] = [min(G[k]["lgG_min"] for k in el), max(G[k]["lgG_max"] for k in el)]
print("    domaine (au moins %d etats) : jusqu'a |delta| = %.2f cote negatif, %.2f cote positif ; cellules : %d et %d" % (DOM_MIN, R["delta_max_dom_neg"], R["delta_max_dom_pos"], R["cellules_dom_neg"], R["cellules_dom_pos"]))
print("    discriminantes a 5 pour cent (au moins %d etats) : %d cellules cote negatif (%s), %d cote positif" % (DOM_MIN, len(R["cellules_disc5_neg"]),
      "delta de %s a %s" % (min(c.split(" x ")[0] for c in R["cellules_disc5_neg"]), max(c.split(" x ")[0] for c in R["cellules_disc5_neg"])) if R["cellules_disc5_neg"] else "aucune", len(R["cellules_disc5_pos"])))
print("    discriminantes a 2 pour cent : %d cellules cote negatif, %d cote positif" % (R["cellules_disc2_neg"], R["cellules_disc2_pos"]))
print("    dans le domaine, l'ordre 2 est au-dessus de l'ordre 3 : %d etats sur %d cote negatif, %d sur %d cote positif" % (*R["ordre2_au_dessus_neg"], *R["ordre2_au_dessus_pos"]))
print("    e_bord median / |delta|, du plus petit au plus grand sur les 22 desaccords : " + " ; ".join("%s : %.1f a %.1f" % (x, *R["e_bord_sur_delta"][str(x)]) for x in facteurs))
print("    cellules eligibles : boites de %d a %d ; largeurs predites de 1e%.0f a 1e%.0f" % (*R["N_eligibles"], *R["lgG_eligibles"]))
out["resume"] = R
out["B"] = {"%+.2f|%s" % (k[0], k[1]): r for k, r in G.items()}
# ---------------- (C)
print("(C) BALAYAGES EN COUPLAGE A w2 FIXE : etiquettes dans le domaine a plusieurs facteurs (cellules faisables, N <= %d)" % N_COUT)
print("    delta   etiquettes a 2 facteurs ou plus, a 3 ou plus   meilleure : etiquette, facteurs, rapport des couplages, decades de largeur predites, pente moyenne")
C = {}
for d in deltas:
    par = {}
    for x in facteurs:
        r = G[(d, x)]
        if not (r["faisable"] and r["N"] <= N_COUT):
            continue
        for lab, e in r["dom"].items():
            par.setdefault(lab, []).append((x, r["g"], e["G3"], e["e_bord"], e["disc"]))
    multi = {lab: v for lab, v in par.items() if len(v) >= 2}
    best = None
    for lab, v in multi.items():
        v.sort(); dec = math.log10(v[-1][2] / v[0][2]); rg = v[-1][1] / v[0][1]
        cand = {"etiquette": lab, "facteurs": [str(a[0]) for a in v], "rapport_g": rg, "decades": dec, "pente": math.log(v[-1][2] / v[0][2]) / math.log(rg),
                "G3": [a[2] for a in v], "e_bord": [a[3] for a in v], "consecutifs": all(facteurs.index(v[i + 1][0]) - facteurs.index(v[i][0]) == 1 for i in range(len(v) - 1))}
        if best is None or cand["decades"] > best["decades"]:
            best = cand
    C["%+.2f" % d] = {"n2": len(multi), "n3": sum(len(v) >= 3 for v in multi.values()), "meilleure": best,
                      "toutes": {lab: [[str(a[0]), a[1], a[2], a[3], a[4]] for a in v] for lab, v in multi.items()}}
    if best:
        print("    %+.2f   %2d, %2d    (%s) aux facteurs %s : couplage x %.2f, %.1f decades, pente %.1f" % (d, len(multi), C["%+.2f" % d]["n3"], best["etiquette"], " ".join(best["facteurs"]),
              best["rapport_g"], best["decades"], best["pente"]))
    else:
        print("    %+.2f    0,  0    aucune" % d)
out["C"] = C
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
