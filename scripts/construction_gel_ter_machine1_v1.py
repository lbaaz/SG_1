# -*- coding: ascii -*-
"""Construit le gel ter : chaque nombre du texte est calcule ici, depuis les pieces, et pose dans le gabarit.
Usage : python3 -I construction_gel_ter_machine1_v1.py <dossier du gel> <dossier de la note> <clone du registre>
        <manifeste du lot de la note> <gabarit> <annonces.txt> <sortie.md>"""
import sys, os, re, json, math, hashlib, unicodedata, subprocess, tempfile, importlib.util
from fractions import Fraction as F
D, DN, CLONE, MAN_NOTE, GABARIT, ANNONCES, SORTIE = sys.argv[1:8]

def canon(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]

def essai(nom):
    """Sorties de la sonde sur le conteneur de machine 1 : sous essai_m1/ au chantier, prefixees essai_m1_ dans le lot a plat."""
    a_ = os.path.join(D, "essai_m1", nom)
    return a_ if os.path.exists(a_) else os.path.join(D, "essai_m1_" + nom)

def med(x):
    x = sorted(x); n = len(x); return x[n // 2] if n % 2 else 0.5 * (x[n // 2 - 1] + x[n // 2])

V = {}
# --- canons ---
V["c_moteur"] = canon(os.path.join(CLONE, "scripts/m17_chaine_v17.py")); assert V["c_moteur"] == "82a0be882568fe0c"
V["c_depot"] = canon(os.path.join(CLONE, "journal/sonde_ordre2.json")); assert V["c_depot"] == "10887c60d5f55bcf"
V["c_retenus"] = canon(os.path.join(CLONE, "journal/tp_retenus_machine2_v1.json")); assert V["c_retenus"] == "69b3bab3bb8480b7"
V["c_ref_tp"] = canon(os.path.join(CLONE, "journal/tp_reference_machine2_v1.json")); assert V["c_ref_tp"] == "4d51dd58ef456fe9"
V["c_gel_bis"] = canon(os.path.join(CLONE, "gels/qualification_EB_bis_pre_enregistrement_v1.md")); assert V["c_gel_bis"] == "dcda1611adf5f8fd"
V["c_note"] = canon(os.path.join(DN, "note/note_machine1_piste0_reprise_absorbeur_long_2026-11-15_v1.md"))
V["c_lot_note"] = canon(MAN_NOTE)
assert V["c_note"] in open(MAN_NOTE).read()
V["c_bloc"] = canon(os.path.join(D, "lecteur_plateau_bloc_machine1_v1.py"))
V["c_sonde"] = canon(os.path.join(D, "sonde_qualification_EB_ter_machine1_v1.py"))
V["c_feuille"] = canon(os.path.join(D, "lecture_qualification_EB_ter_machine1_v1.py"))
V["c_banc"] = canon(os.path.join(D, "banc_feuille_ter_machine1_v1.py"))
V["c_ref_ancres"] = canon(os.path.join(D, "reference_ancres_ter_machine1_v1.json"))
sonde_src = open(os.path.join(D, "sonde_qualification_EB_ter_machine1_v1.py")).read()
assert open(os.path.join(D, "lecteur_plateau_bloc_machine1_v1.py")).read().rstrip("\n") in sonde_src
feuille_src = open(os.path.join(D, "lecture_qualification_EB_ter_machine1_v1.py")).read()
assert 'CANON_SONDE = "%s"' % V["c_sonde"] in feuille_src and V["c_ref_ancres"] in feuille_src
SOURCES = [("gels/qualification_EB_bis_pre_enregistrement_v1.md", "le gel bis, JOUE (delta 95)"),
           ("journal/journal_delta_95_qualification_EB_bis_v2.md", "l'acte 95 : NON QUALIFIE"),
           ("scripts/m17_chaine_v17.py", "le moteur"),
           ("journal/sonde_ordre2.json", "la sortie deposee de la sonde du delta 98 : points, etats, G_dep"),
           ("journal/journal_delta_98_ordre2_chaine_EA_v1.md", "l'acte 98"),
           ("journal/tp_retenus_machine2_v1.json", "les couplages retenus du temoin, j = 6 et j = 8"),
           ("journal/tp_reference_machine2_v1.json", "la table de reference du temoin (machine 2)"),
           ("journal/lot_a01598ec24237921__sonde_etage2.json", "la sortie de la sonde dense, nuit bis"),
           ("journal/sonde_chaine_par_etat.json", "la sortie deposee du delta 96 (points de reglage J1, J2, J3, J5)"),
           ("journal/sonde_domaine_G1.json", "la sortie deposee du delta 97 (points de reglage E4, H1)")]
V["sources"] = "\n".join("    %s  %s\n        %s" % (canon(os.path.join(CLONE, p)), p, q) for p, q in SOURCES)
# --- la feuille, chargee pour juger le reglage par ses propres fonctions ---
spec = importlib.util.spec_from_file_location("feuille", os.path.join(D, "lecture_qualification_EB_ter_machine1_v1.py"))
Fe = importlib.util.module_from_spec(spec); spec.loader.exec_module(Fe)
ok, T = Fe.selftest(); assert ok; V["n_selftest"] = len(T)
r = subprocess.run([sys.executable, "-I", os.path.join(D, "banc_feuille_ter_machine1_v1.py"), os.path.join(D, "lecture_qualification_EB_ter_machine1_v1.py"),
                    tempfile.mkdtemp()], capture_output=True, text=True)
m = re.search(r"BANC : (\d+) alterations, (\d+) mordues, 0 survivantes \[\], 0 cibles refusees \[\] ; base saine : True", r.stdout)
assert r.returncode == 0 and m and m.group(1) == m.group(2), r.stdout[-400:]
V["n_banc"] = int(m.group(1))
open(os.path.join(D, "banc_feuille_ter_machine1_v1.log"), "w", newline="\n").write(r.stdout)
# --- les douze points et leurs etats juges ---
DEP = json.load(open(os.path.join(CLONE, "journal/sonde_ordre2.json"))); P = {p["id"]: p for p in DEP["points"]}
lignes = []; nj = 0; etal = []
for i in Fe.JUGES:
    p = P[i]; e = Fe.etats_attendus(p, "juges"); nj += len(e); rc = p["r_c"]
    assert any(x[0] == 0 for x in e)
    lignes.append("  %-5s  %-8s  %-7s  %3d  %2d            %d, %d, %d, %d" % (i, p["w2"], p["facteur"], rc, len(e), rc + 80, rc + 100, rc + 100, rc + 90))
    for x in p["etats"]:
        g = x.get("Gamma_2D") or {}
        if g.get("3") is not None and g["3"] > Fe.PLANCHER10:
            v = [g[k] for k in ("2", "3", "4")]; etal.append(max(v) / min(v) - 1.0)
V["table_points"] = "\n".join(lignes); V["n_juges"] = nj; V["n_lectures"] = nj * 4 * 12
V["seuil_etats"] = int(math.ceil(F(9, 10) * nj)); assert F(V["seuil_etats"]) >= F(9, 10) * nj > F(V["seuil_etats"] - 1)
V["dep_med"] = "%.3f" % med(etal); V["dep_max"] = "%.3f" % max(etal)
# --- (i) la note : six points de M17 ---
EX = {}
for f in ("exploration_v1.json", "exploration_v1b.json"):
    EX.update(json.load(open(os.path.join(DN, f)))["points"])
assert len(EX) == 6
KSN = list(range(-5, 15))
def fen(vals, ks):
    best = None
    for i in range(len(ks) - 4):
        f = [vals[k] for k in ks[i:i + 5]]; e = max(f) / min(f)
        if best is None or e < best[0]: best = (e, math.exp(sum(math.log(x) for x in f) / 5.0))
    return best[0] - 1.0, best[1]
pire, acc, f3 = 0.0, 0.0, 0.0
for nom, p in EX.items():
    vals = {}
    for c in ("F2_r+0_L60", "F2_r+0_L80", "F1_r+0_L80", "F3_r+0_L60", "F1_r+10_L60"):
        e, v = fen({k: p["cfg"][c]["traj"][str(k)]["gamma"] for k in KSN}, KSN); pire = max(pire, e); vals[c] = v
    acc = max(acc, max(vals.values()) / min(vals.values()) - 1.0)
    f3 = max(f3, abs(math.log(vals["F3_r+0_L60"] / vals["F1_r+0_L80"])))
assert pire <= 0.05
V["note_pire_etal"] = "%.4f" % pire; V["note_accord"] = "%.4f" % acc; V["f3_ecart"] = "%.4f" % f3
# --- (ii) le reglage : huit points, juges par la feuille ---
R = {}
for f in ("reglage_p1.json", "reglage_p2.json"):
    R.update(json.load(open(os.path.join(D, f)))["points"])
couv = []
for pid in ("E4", "J2", "H1", "A2", "A1", "J1", "J3", "J5"):
    q_ = [x for f_ in ("journal/sonde_ordre2.json", "journal/sonde_chaine_par_etat.json", "journal/sonde_domaine_G1.json")
          for x in json.load(open(os.path.join(CLONE, f_)))["points"] if x["id"] == pid][0]
    tous_juges = Fe.etats_attendus(q_, "juges"); rmax = max(e["rang"] for e in R[pid]["etats"].values())
    att = [x for x in tous_juges if x[0] <= rmax]
    assert sorted((e["rang"], e["n1"], e["n2"]) for e in R[pid]["etats"].values()) == att, pid      # couverture complete jusqu'au rang dit
    couv.append("%s tous (%d)" % (pid, len(att)) if len(att) == len(tous_juges) else "%s rangs 0 a %d (%d sur %d)" % (pid, rmax, len(att), len(tous_juges)))
V["regl_couverture"] = ", ".join(couv[:3]) + ",\n        " + ", ".join(couv[3:6]) + ",\n        " + ", ".join(couv[6:])
assert sorted(R) == sorted(["A1", "A2", "J1", "J2", "J3", "J5", "E4", "H1"]), sorted(R)
tous = []; fl = 0.0; nlect = 0; par_point = []
for pid in ("A1", "A2", "J1", "J2", "J3", "J5", "E4", "H1"):
    q = 0
    for cle, e in R[pid]["etats"].items():
        j = Fe.juger_etat(e["cfg"], e["G2D"]["3"]); tous.append((pid, e["rang"], j)); q += j["statut"] == "QUALIFIE"
        for x in Fe.ABS:
            for k in Fe.KS:
                r_ = e["cfg"][x][str(k)]; nlect += 1
                if r_["suivi"]: fl = max(fl, abs(r_["gamma_im"] / r_["gamma"] - 1.0))
    par_point.append("%s %d/%d" % (pid, q, len(R[pid]["etats"])))
V["regl_n"] = len(tous); V["regl_lectures"] = nlect; V["flux_im"] = "%.0e" % fl
m = re.search(r"pire ecart relatif au lecteur d'exploration ([0-9.e+-]+) ; iterations max (\d+) ; suivis 20 sur 20", open(os.path.join(D, "essai_bloc_lecteur_v1.log")).read())
V["bloc_arpack"] = m.group(1); assert float(m.group(1)) < 1e-9
nq = sum(1 for t in tous if t[2]["statut"] == "QUALIFIE"); nn = sum(1 for t in tous if t[2]["statut"] == "NON QUALIFIE"); nl = len(tous) - nq - nn
r0 = [t for t in tous if t[1] == 0]; assert len(r0) == 8
b = ["        %d QUALIFIES, %d NON QUALIFIES, %d NON LISIBLES ; etat lu QUALIFIE a %d points sur 8 ;" % (nq, nn, nl, sum(1 for t in r0 if t[2]["statut"] == "QUALIFIE")),
     "        par point (QUALIFIES / juges) : %s," % ", ".join(par_point[:4]),
     "        %s ;" % ", ".join(par_point[4:])]
STAT = {}
for x in Fe.ABS:
    es = [t[2]["plateaux"][x]["etalement"] for t in tous if "k0" in t[2]["plateaux"][x]]
    STAT["etal_" + x] = (med(es), max(es), sum(e > 0.05 for e in es), len(es))
    b.append("        etalement de la meilleure fenetre sous %s : mediane %.4f, plus grand %.4f ;" % (x, med(es), max(es)))
for x in ("B", "C", "D"):
    ec = [t[2]["plateaux"][x]["ecart_ln_A"] for t in tous if "ecart_ln_A" in t[2]["plateaux"][x]]
    STAT["acc_" + x] = (med(ec), max(ec))
    b.append("        accord %s / A, |ln| : mediane %.4f, plus grand %.4f ;" % (x, med(ec), max(ec)))
dp = [t[2]["ecart_ln_depot"] for t in tous if t[2]["ecart_ln_depot"] is not None]
STAT["depot"] = (med(dp), max(dp), sum(e > 0.05 for e in dp), len(dp))
b.append("        consigne (e), |ln(G_dep / Gamma_pl(A))| : mediane %.4f, plus grand %.4f ; au-dessus de" % (med(dp), max(dp)))
b.append("        tau a %d etats sur %d." % (sum(e > 0.05 for e in dp), len(dp)))
V["regl_bilan"] = "\n".join(b)
json.dump({"n": len(tous), "QUALIFIES": nq, "NON_QUALIFIES": nn, "NON_LISIBLES": nl, "stat": STAT, "par_point": par_point,
           "non_qualifies": [(t[0], t[1], t[2]["echecs"]) for t in tous if t[2]["statut"] != "QUALIFIE"]},
          open(os.path.join(D, "bilan_reglage_machine1_v1.json"), "w"), indent=1, sort_keys=True)
# --- (ii bis) le premier jeu d'absorbeurs ---
R1 = {}
for f in ("exploration_etats_p1.json", "exploration_etats_p2.json"):
    R1.update(json.load(open(os.path.join(D, f)))["points"])
KS1 = list(range(-3, 9)); n1 = 0; pire1 = {x: (0.0, None) for x in "ABCD"}
for pid, p_ in R1.items():
    for cle, e in p_["etats"].items():
        n1 += 1
        for x in "ABCD":
            v = {k: e["cfg"][x][str(k)]["gamma"] for k in KS1}; ee = fen(v, KS1)[0]
            if ee > pire1[x][0]: pire1[x] = (ee, "%s rang %d" % (pid, e["rang"]))
t_e4 = open(os.path.join(D, "essai_configs_E4.log")).read()
m = re.search(r"rang  0 \(6,1\) F2:\+0: 60 : .*?k<=8 : ([0-9.]+) a k0=\S+ val ([0-9.]+)", t_e4); e4_a = float(m.group(1)); e4_va = float(m.group(2))
m = re.search(r"rang  0 \(6,1\) F2:\+10: 60 : .*?k<=8 : ([0-9.]+) a k0=\S+ val ([0-9.]+)", t_e4); e4_vd = float(m.group(2))
assert e4_a > 0.05
V["prem_n"] = n1
ordre1 = [p_ for p_ in ("A1", "A2", "J1", "J2", "J3", "J5") if p_ in R1]; assert sorted(ordre1) == sorted(R1)
V["prem_points"] = ", ".join("%s %d" % (p_, len(R1[p_]["etats"])) for p_ in ordre1)
fausses = []
for pid, p_ in R1.items():
    for cle, e in p_["etats"].items():
        j = Fe.juger_etat(e["cfg"], e["G2D"]["3"])
        if j["statut"] != "QUALIFIE":
            fausses.append((pid, e["rang"], j["echecs"], j["plateaux"]["C"]))
assert len(fausses) == 1 and fausses[0][:2] == ("J2", 5) and len(fausses[0][2]) == 1 and fausses[0][2][0].startswith("(c) accord C / A")
V["prem_fausse"] = ("J2, rang 5, sous F1 a 80\n       couches, une fenetre du cote fort (k0 = %d, etalement %.4f) retenue a %.4f de A en\n       logarithme" % (
    fausses[0][3]["k0"], fausses[0][3]["etalement"], fausses[0][3]["ecart_ln_A"]))
V["prem_bilan"] = ("plus grand etalement\n        de la meilleure fenetre %.4f sous F2 a 60 couches, %.4f sous F2 a 80,\n"
                   "        %.4f sous F1 a 80 (%s), %.4f sous F2 translate. Et, par un essai a part\n"
                   "        au point E4 : l'etat lu n'a pas de plateau sous F2 a 60 couches (meilleur etalement\n"
                   "        %.4f), et sa valeur sous F2 translate s'en ecarte de %.4f en logarithme." % (
                       pire1["A"][0], pire1["B"][0], pire1["C"][0], pire1["C"][1], pire1["D"][0], e4_a, abs(math.log(e4_vd / e4_va))))
# --- (iii), (iv) : la sonde de ce gel sur le conteneur de machine 1 ---
s1 = json.load(open(essai("sonde_ter_etage1.json"))); assert s1["sonde_canon"] == V["c_sonde"]
e1 = Fe.juger_etage1(s1, json.load(open(os.path.join(CLONE, "journal/tp_reference_machine2_v1.json")))); assert e1["tient"], e1["motifs"]
V["tp_pire"] = "%.4f" % max(e1["detail"]["TP"][j][x]["ecart_ln"] for j in e1["detail"]["TP"] for x in Fe.ABS)
tn3 = [t["traj"][x]["3"]["gamma"] for t in s1["temoin_negatif"] for x in Fe.ABS]
for t in s1["temoin_negatif"]:
    for x in Fe.ABS:
        v = [t["traj"][x][str(k)]["gamma"] for k in Fe.KS]
        assert all(abs(v[i + 1] / v[i] - 0.5) < 2e-3 for i in range(len(v) - 1))      # se divise par deux a chaque barreau, a 0.002 pres
V["tn_min"] = "%.0e" % min(tn3); V["tn_max"] = "%.0e" % max(tn3)
s0 = json.load(open(essai("sonde_ter_etage0.json"))); assert s0["sonde_canon"] == V["c_sonde"]
e0 = Fe.juger_etage0(s0, DEP); assert e0["tient"] and e0["lectures"] == 84, e0["hors"]
V["e0_abs"] = "%.1e" % e0["pire_ecart_absolu"]; V["e0_rel"] = "%.1e" % e0["pire_ecart_relatif_au_dessus_de_mille_planchers"]
sa = json.load(open(os.path.join(D, "reference_ancres_ter_machine1_v1.json"))); assert sa["sonde_canon"] == V["c_sonde"]
an = Fe.juger_ancres(sa, sa, DEP); assert an["tient"] and an["lectures"] == 192
# --- couts ---
def durees(log):
    """Duree de chaque etat : ecart au repere de temps precedent du meme journal (assemblage ou etat precedent)."""
    out = {}; dernier = 0.0
    for l in open(os.path.join(D, log)).read().splitlines():
        m = re.match(r"(\w+) : assemblage Nmax = \d+, (\d+) s", l)
        if m:
            dernier = float(m.group(2)); continue
        m = re.match(r"  (\w+) rang .*\((\d+) s\)$", l)
        if m:
            t = float(m.group(2)); out.setdefault(m.group(1), []).append(t - dernier); dernier = t
    return out
dur = {}
for log in ("reglage_p1.log", "reglage_p2.log"):
    for pid, v in durees(log).items():
        dur.setdefault(pid, []).extend(v)
assert sorted(dur) == sorted(R) and all(x > 0 for v in dur.values() for x in v), dur
classe = {"petit": med(dur["J3"] + dur["E4"]), "moyen": med(dur["A1"] + dur["A2"] + dur["J1"] + dur["J2"]), "grand": med(dur["J5"] + dur["H1"])}
cumul = 0.0
for i in Fe.JUGES:
    rc = P[i]["r_c"]; n = len(Fe.etats_attendus(P[i], "juges"))
    cumul += n * (classe["petit"] if rc <= 37 else classe["moyen"] if rc <= 44 else classe["grand"])
toutes = [x for v in dur.values() for x in v]
V["cout_etat_min"] = "%d s" % round(min(toutes)); V["cout_etat_max"] = "%d s" % round(max(toutes))
V["cout_e2"] = "%.1f h" % (cumul / 3600.0)
V["cout_e0"] = "%d s" % round(s0["duree_s"]); V["cout_e1"] = "%d s" % round(s1["duree_s"]); V["cout_ancres"] = "%d s" % round(sa["duree_s"])
m = re.search(r"pic de memoire : (\d+) Mo", open(os.path.join(D, "mesure_memoire_machine1_v1.log")).read())
V["cout_mem"] = "%s Mo" % m.group(1)
# --- annonces : texte de la plume, les valeurs vues y sont posees par les memes cles ---
ann = open(ANNONCES).read().rstrip("\n")
V["annonces"] = re.sub(r"\{\{(\w+)\}\}", lambda m: str(V[m.group(1)]), ann)
g = open(GABARIT).read()
manquants = set(re.findall(r"\{\{(\w+)\}\}", g)) - set(V)
assert not manquants, manquants
out = re.sub(r"\{\{(\w+)\}\}", lambda m: str(V[m.group(1)]), g)
out.encode("ascii"); assert "%" not in out
longues = [(i + 1, len(l)) for i, l in enumerate(out.splitlines()) if len(l) > 100]
if longues:
    for i_, n_ in longues: print("LONGUE", i_, n_, out.splitlines()[i_ - 1])
assert not longues, longues
open(SORTIE, "w", newline="\n").write(out)
json.dump({k: v for k, v in V.items() if k not in ("annonces", "sources", "table_points", "regl_bilan")}, open(os.path.join(D, "valeurs_gel_ter_machine1_v1.json"), "w"), indent=1, sort_keys=True)
print("ecrit", SORTIE, canon(SORTIE), len(out.splitlines()), "lignes")
for k in sorted(V):
    if k not in ("annonces", "sources", "table_points", "regl_bilan"): print("  %-18s %s" % (k, V[k]))
print(V["regl_bilan"])
