# -*- coding: ascii -*-
"""LA TABLE GELEE DES CELLULES DU GEL "SOMMET" -- machine 1, v1, 2026-11-22. Aucun calcul de chaine ni de 2D : un assemblage.
Entrees : la graine ; la table commune d'eligibilite (au canon) ; la table complete de machine 1 (ses predictions a une
dimension, calculees AVANT la graine) ; le script de tirage de la premiere partie (charge au canon, sa fonction tirer
appelee telle quelle) ; la feuille DEPOSEE du lecteur (au canon) et les dix-huit sorties de machine 2 aux neuf points
sacrifies (Q et Q2), lues comme des donnees, pour ecrire la reference des TEMOINS POSITIFS DU SOMMET.
Sorties : table_cellules_gel_sommet_v1.json (graine, rangs, 56 cellules avec leurs trois nombres ecrits, leurs predictions,
leur tolerance, et les neuf temoins positifs avec leur plateau de reference) ; jobs_gel_sommet_v1.txt (112 lignes, une par
lecture d'une cellule) et jobs_temoins_sommet_v1.txt (18 lignes), au format du pilote de machine 2 :
ID W2 G M ETA0 SIGNE RC ABS.
Usage : python3 -I -B predictions_sommet_machine1_v1.py <graine> <table commune.json> <table complete m1.json> <tirage_sommet.py>
        <feuille deposee du lecteur.py> <dossier Q_sorties> <dossier Q2_sorties> <dossier de sortie>"""
import sys, os, json, math, hashlib, unicodedata, importlib.util, io, contextlib
from fractions import Fraction as F
GRAINE, COMMUNE, COMPLETE, TIRAGE, FEUILLE, DQ, DQ2, OUT = sys.argv[1:9]
CANONS = {"commune": "77ce2a6c7e867011", "complete": "882f55d07d03dfff", "tirage": "816ac4d298e82f16", "feuille": "83701094e6a2b965"}
PILOTE_M2, MOTEUR, SOURCE_BLOC, BLOC16 = "47a84eae6052f006", "82a0be882568fe0c", "d5cc48f48e37af99", "5b835ce079ce2cf4"
ABSORBEURS = [["A", "F2", 0, 80], ["B", "F2", 0, 100], ["C", "F1", 0, 100], ["D", "F2", 10, 80]]; KS = list(range(-3, 9))
TOLERANCE, TEMOIN_MAX, TOL_TEMOIN_POSITIF = 0.01, 1e-6, 1e-3
S1_JUGEES_MIN, S1_TENUES_PAR_W2_MIN, PORTEE_TENUES_PAR_KAPPA_MIN = 42, 4, 4
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
for nom, chemin in (("commune", COMMUNE), ("complete", COMPLETE), ("tirage", TIRAGE), ("feuille", FEUILLE)):
    if canon_B(chemin) != CANONS[nom]:
        raise SystemExit("REFUS : %s n'est pas au canon %s" % (nom, CANONS[nom]))
if not (GRAINE.isdigit() and GRAINE.isascii() and len(GRAINE) >= 6):
    raise SystemExit("REFUS : la graine doit etre une suite d'au moins six chiffres")
# --- le tirage, par la fonction du script de la premiere partie (son autotest est joue a l'import, sortie retenue)
src = open(TIRAGE, encoding="ascii").read(); coupe = src.index('if sys.argv[1] == "--autotest":')
T = {}; exec(compile(src[:coupe], TIRAGE, "exec"), T)                      # definitions seules : ORDRE, LISTES, numero, tirer
C = json.load(open(COMMUNE)); el = {}; cel = {}
for s in T["ORDRE"]:
    for c in C["creneaux"][s]["candidats"]:
        k = (s, F(c["w2"])); el[k] = bool(c["eligible"]); cel[k] = {x["kappa"]: (x["g"], x["eta0"], int(x["r_c"])) for x in c["cellules"]}
tirees, journal = T["tirer"](GRAINE, lambda s, w: el[(s, w)], lambda s, w: [(kap,) + cel[(s, w)][kap] for kap in T["KAPPAS"]])
assert tirees is not None and len(tirees) == 56, "PAS DE GEL"
# --- les predictions : la table complete de machine 1
D = json.load(open(COMPLETE)); pred = {}
for s in T["ORDRE"]:
    for c in D["creneaux"][s]["candidats"]:
        for x in c["cellules"]:
            pred[(F(c["w2"]), x["kappa"])] = x
cellules = []; jobs = []
for i, t in enumerate(tirees):
    w = F(t["w2"]); p = pred[(w, t["kappa"])]; d = float(w) - 2.0
    assert (p["g"], p["eta0"], p["r_c"]) == (t["g"], t["eta0"], t["r_c"]) and p["eligible"] and p["m_bord"] == p["cible"]
    job = [t["id"], t["w2"], t["g"], str(p["m_bord"]), t["eta0"], None, str(t["r_c"]), "ABCD"]
    cellules.append({"id": t["id"], "creneau": t["creneau"], "rang": t["id"][2], "numero_kappa": int(t["id"][3]), "w2": t["w2"], "delta": d, "kappa": t["kappa"],
                     "m": p["m_bord"], "g": t["g"], "eta0": t["eta0"], "r_c": t["r_c"], "boite": t["r_c"] + 100, "ln_G3": p["ln_G3"], "etendue": p["etendue"],
                     "ln_G2": p["ln_G2"], "ln_G1": p["ln_G1"], "ln_Phi": p["ln_Phi"], "poids_min_chaine": p["poids_min"], "tolerance": TOLERANCE})
    for signe in ("1", "-1"):
        jobs.append(" ".join(job[:5] + [signe] + job[6:]))
# --- les temoins positifs du sommet : les neuf points sacrifies, leur plateau de reference relu par la feuille deposee
spec = importlib.util.spec_from_file_location("feuille_lecteur", FEUILLE); L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
POINTS = (("Qa", DQ, "2", 0, "9.73875e-04", 18, 1.36076e-05, 0.0030), ("Qc", DQ, "2", 0, "3.89550e-03", 18, 5.44311e-05, 0.0016), ("Qd", DQ, "2", 0, "7.79100e-03", 18, 1.08861e-04, 0.0028),
          ("Qe", DQ, "20001/10000", 0, "1.16821e-03", 18, 1.20924e-05, 0.0026), ("Qf", DQ, "20001/10000", 0, "5.84106e-04", 18, 2.91470e-06, 0.0032),
          ("Q2a", DQ2, "20001/10000", 1, "2.33642e-04", 20, 4.94622e-08, 0.0026), ("Q2b", DQ2, "20001/10000", 2, "1.55762e-04", 22, 2.05449e-09, 0.0024),
          ("Q2c", DQ2, "19999/10000", 0, "1.16909e-03", 18, 1.21071e-05, 0.0030), ("Q2d", DQ2, "19999/10000", 0, "5.84544e-04", 18, 2.92086e-06, 0.0033))
temoins = []; jobs_t = []
for (pid, dossier, w2, m, eta0, r_c, G3, etendue) in POINTS:
    f = json.load(open(os.path.join(dossier, "lect2D_%s_fantome.json" % pid))); x = f["cellule"]
    assert f["pilote_canon"] == PILOTE_M2 and f["moteur_canon"] == MOTEUR and f["source_bloc_canon"] == SOURCE_BLOC and f["bloc_sha256_16"] == BLOC16, pid
    assert (x["id"], x["w2"], x["m"], x["r_c"]) == (pid, w2, m, r_c) and x["eta0"] == float(eta0) and f["reglage"]["absorbeurs"] == ABSORBEURS and f["reglage"]["ks"] == KS, pid
    J = L.juger_etat(f["lecture"]["traj"], None); assert J["statut"] == "QUALIFIE", pid
    temoins.append({"id": pid, "w2": w2, "delta": float(F(w2)) - 2.0, "m": m, "g": x["g"], "eta0": eta0, "r_c": r_c, "boite": r_c + 100,
                    "ln_Gamma_pl_reference": math.log(J["plateaux"]["A"]["Gamma_pl"]), "ln_G3": math.log(G3), "etendue": etendue, "tolerance_reference": TOL_TEMOIN_POSITIF})
    for signe in ("1", "-1"):
        jobs_t.append(" ".join([pid, w2, x["g"], str(m), eta0, signe, str(r_c), "ABCD"]))
table = {"gel": "sommet", "version": 1, "graine": GRAINE, "journal_du_tirage": journal,
         "w2_tires": {s: [next(c["w2"] for c in cellules if c["id"].startswith(s + r)) for r in "ab"] for s in T["ORDRE"]},
         "regle": {"absorbeurs_du_lecteur": ABSORBEURS, "barreaux": KS, "tolerance": TOLERANCE, "temoin_max": TEMOIN_MAX, "tolerance_temoin_positif": TOL_TEMOIN_POSITIF,
                   "s1_jugees_min": S1_JUGEES_MIN, "s1_tenues_par_w2_min": S1_TENUES_PAR_W2_MIN, "portee_tenues_par_kappa_min": PORTEE_TENUES_PAR_KAPPA_MIN,
                   "pilote_machine2_canon": PILOTE_M2, "moteur_canon": MOTEUR, "source_bloc_canon": SOURCE_BLOC, "bloc_sha256_16": BLOC16,
                   "table_commune_canon": CANONS["commune"], "table_complete_machine1_canon": CANONS["complete"]},
         "cellules": cellules, "temoins_positifs": temoins}
os.makedirs(OUT, exist_ok=True)
json.dump(table, open(os.path.join(OUT, "table_cellules_gel_sommet_v1.json"), "w"), indent=1, sort_keys=True)
open(os.path.join(OUT, "jobs_gel_sommet_v1.txt"), "w", newline="\n").write("\n".join(jobs) + "\n")
open(os.path.join(OUT, "jobs_temoins_sommet_v1.txt"), "w", newline="\n").write("\n".join(jobs_t) + "\n")
print("graine %s ; w2 tires : %s" % (GRAINE, " ; ".join("%s %s" % (s, " et ".join(table["w2_tires"][s])) for s in T["ORDRE"])))
for l in journal: print("  " + l)
print("cellule  w2              delta      kappa   m  g            eta0         r_c  boite  G3*          etendue  ln(G3/G1)  T")
for c in cellules:
    print("%-7s  %-14s  %+.5f  %s  %d  %s  %s  %-3d  %-5d  %.5e  %.4f   %+.5f   %.2f" % (c["id"], c["w2"], c["delta"], c["kappa"], c["m"], c["g"], c["eta0"], c["r_c"], c["boite"],
          math.exp(c["ln_G3"]), c["etendue"], c["ln_G3"] - c["ln_G1"], c["tolerance"]))
print("temoin   w2           m  g        eta0         r_c  plateau de reference (lu a Q ou Q2)  ln(reference / G3*)")
for t in temoins:
    print("%-7s  %-11s  %d  %-7s  %s  %-3d  %.5e                          %+.5f" % (t["id"], t["w2"], t["m"], t["g"], t["eta0"], t["r_c"], math.exp(t["ln_Gamma_pl_reference"]), t["ln_Gamma_pl_reference"] - t["ln_G3"]))
G = [math.exp(c["ln_G3"]) for c in cellules]
print("56 cellules : couplages de %s a %s ; G3* de %.5e a %.5e ; etendue de %.4f a %.4f ; plus grand |ln(G3/G1)| %.5f ; |ln(G3/G2)| %.5f" % (
    min((c["g"] for c in cellules), key=float), max((c["g"] for c in cellules), key=float), min(G), max(G), min(c["etendue"] for c in cellules), max(c["etendue"] for c in cellules),
    max(abs(c["ln_G3"] - c["ln_G1"]) for c in cellules), max(abs(c["ln_G3"] - c["ln_G2"]) for c in cellules)))
print("lectures : %d pour les cellules, %d pour les temoins positifs ; plus grande boite %d" % (len(jobs), len(jobs_t), max(c["boite"] for c in cellules + temoins)))
print("ecrit : table_cellules_gel_sommet_v1.json (canon %s) ; jobs_gel_sommet_v1.txt (%s) ; jobs_temoins_sommet_v1.txt (%s)" % (
    canon_B(os.path.join(OUT, "table_cellules_gel_sommet_v1.json")), canon_B(os.path.join(OUT, "jobs_gel_sommet_v1.txt")), canon_B(os.path.join(OUT, "jobs_temoins_sommet_v1.txt"))))
