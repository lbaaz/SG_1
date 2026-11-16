# -*- coding: ascii -*-
"""Essai de la feuille en etape "verdict" sur des sorties SYNTHETIQUES : aucune largeur n'y est calculee. Les etats
sont ceux que la regle du gel tire du depot ; les trajectoires sont fabriquees (constantes a G_dep, ou alterees).
Sert a eprouver le chemin de lecture (completude, refus, cascade, issue du depot) sans toucher aux douze points.
Usage : python3 -I essai_feuille_verdict_synthetique_machine1_v1.py <feuille.py> <sonde_ordre2.json>
        <verdict_ter_instrument.json d'un essai> <dossier de travail>"""
import sys, os, json, shutil, subprocess, copy
FEUILLE, DEPOT, VINST, TRAVAIL = sys.argv[1:5]
src = open(FEUILLE).read()
import re
CANON_SONDE = re.search(r'CANON_SONDE = "([0-9a-f]{16})"', src).group(1)
REGLAGE = {"ks": list(range(-3, 9)), "ks_etage0": [2, 3, 4],
           "absorbeurs": [["A", "F2", 0, 80], ["B", "F2", 0, 100], ["C", "F1", 0, 100], ["D", "F2", 10, 80]],
           "plancher10": 1.33e-12, "iter_min": 2, "iter_max": 12, "tol_residu": 1e-11, "poids_min": 0.5}
D = json.load(open(DEPOT)); P = {p["id"]: p for p in D["points"]}
JUGES = ["C1", "C2", "C3", "C4", "M1", "M2", "M3", "M4", "L1", "L2", "L3", "L4"]
def traj(val, lin=False, suivi=True):
    return {str(k): {"gamma": (val * 2.0 ** (-k) if lin else val), "suivi": suivi} for k in range(-3, 9)}
def point(pid, alter=None):
    p = P[pid]; etats = []
    for e in p["etats"]:
        g3 = (e.get("Gamma_2D") or {}).get("3")
        if g3 is None or g3 <= 1.33e-12:
            continue
        t = {x: traj(g3) for x in "ABCD"}
        if alter:
            alter(e, t)
        etats.append({"rang": e["rang"], "n1": int(e["n1"]), "n2": int(e["n2"]), "traj": t})
    return {"id": pid, "etats": etats}
def fichier(pids, alter=None, canon=CANON_SONDE):
    return {"sonde_canon": canon, "moteur_canon": "82a0be882568fe0c", "depot_canon": "10887c60d5f55bcf", "retenus_canon": "69b3bab3bb8480b7",
            "mode": "point", "reglage": REGLAGE, "points": [point(i, alter) for i in pids]}
def jouer(nom, fichiers, attendu_code, attendu_texte):
    d = os.path.join(TRAVAIL, nom); shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    shutil.copy(VINST, os.path.join(d, "verdict_ter_instrument.json"))
    for n, f in fichiers.items():
        json.dump(f, open(os.path.join(d, n), "w"))
    r = subprocess.run([sys.executable, "-I", FEUILLE, "verdict", d, DEPOT], capture_output=True, text=True)
    ok = r.returncode == attendu_code and all(a in r.stdout for a in attendu_texte)
    print("  %-52s %s  (code %d ; %s)" % (nom, "TIENT" if ok else "MORD ", r.returncode, [l for l in r.stdout.splitlines() if l.startswith(("VERDICT", "ISSUE", "LECTURE REFUSEE"))]))
    if not ok:
        print(r.stdout[-600:], r.stderr[-600:])
    return ok
T = []
tous = {"sonde_ter_point_%s.json" % i: fichier([i]) for i in JUGES}
T.append(jouer("S01_tout_plat", tous, 0, ["VERDICT : ESTIMATEUR QUALIFIE", "ISSUE DE LA LECTURE DEPOSEE (consigne e) : LA LECTURE DEPOSEE EST SUR LE PLATEAU (137 sur 137)", "ETATS : 137 juges, 137 QUALIFIES"]))
groupes = {"sonde_ter_point_C1_C2_C3_C4.json": fichier(["C1", "C2", "C3", "C4"]), "sonde_ter_point_M.json": fichier(["M1", "M2", "M3", "M4"]), "sonde_ter_point_L.json": fichier(["L1", "L2", "L3", "L4"])}
T.append(jouer("S02_trois_groupes", groupes, 0, ["VERDICT : ESTIMATEUR QUALIFIE"]))
def lin_C_rang0(e, t):
    if e["rang"] == 0: t["C"] = traj(e["Gamma_2D"]["3"], lin=True)
f = dict(tous); f["sonde_ter_point_L3.json"] = fichier(["L3"], lin_C_rang0)
T.append(jouer("S03_etat_lu_de_L3_sans_plateau_sous_C", f, 0, ["VERDICT : QUALIFIE PAR POINT", "point L3  etat lu NON QUALIFIE", "ETATS : 137 juges, 136 QUALIFIES"]))
def lin_C_tous_sauf_0(e, t):
    if e["rang"] != 0: t["C"] = traj(e["Gamma_2D"]["3"], lin=True)
f = dict(tous)
for i in ("L1", "L3"):
    f["sonde_ter_point_%s.json" % i] = fichier([i], lin_C_tous_sauf_0)
T.append(jouer("S04_etats_lus_tenus_26_autres_non", f, 0, ["VERDICT : QUALIFIE A L'ETAT LU", "ETATS : 137 juges, 111 QUALIFIES"]))
def decale_A(e, t):
    for x in "ABCD": t[x] = traj(e["Gamma_2D"]["3"] * 1.08)
f = dict(tous); f["sonde_ter_point_M2.json"] = fichier(["M2"], decale_A)
T.append(jouer("S05_plateau_a_8_centiemes_du_depot_a_M2", f, 0, ["VERDICT : ESTIMATEUR QUALIFIE", "LA LECTURE DEPOSEE N'EST PAS PARTOUT SUR LE PLATEAU (123 sur 137)"]))
f = dict(tous); f["sonde_ter_point_C1.json"] = fichier(["C1"], decale_A)
T.append(jouer("S05b_plateau_a_8_centiemes_du_depot_a_C1", f, 0, ["VERDICT : ESTIMATEUR QUALIFIE", "A NEUF ETATS SUR DIX AU MOINS (129 sur 137)"]))
def non_suivi_D(e, t):
    t["D"] = traj(e["Gamma_2D"]["3"], suivi=False)
f = {"sonde_ter_point_%s.json" % i: fichier([i], non_suivi_D) for i in JUGES}
T.append(jouer("S06_rien_de_suivi_sous_D", f, 0, ["VERDICT : NON LISIBLE"]))
f = dict(tous); del f["sonde_ter_point_M4.json"]
T.append(jouer("S07_un_point_manque", f, 0, ["VERDICT : RUN INCOMPLET"]))
f = dict(tous); f["sonde_ter_point_bis_C1.json"] = fichier(["C1"])
T.append(jouer("S08_un_point_lu_deux_fois", f, 2, ["LECTURE REFUSEE"]))
f = dict(tous); f["sonde_ter_point_C2.json"] = fichier(["C2"], canon="0000000000000000")
T.append(jouer("S09_sortie_d_une_autre_sonde", f, 2, ["LECTURE REFUSEE"]))
f = dict(tous); x = fichier(["C3"]); x["points"][0]["etats"].pop(); f["sonde_ter_point_C3.json"] = x
T.append(jouer("S10_un_etat_manque", f, 2, ["LECTURE REFUSEE"]))
f = dict(tous); x = fichier(["C4"]); del x["points"][0]["etats"][0]["traj"]["B"]["8"]; f["sonde_ter_point_C4.json"] = x
T.append(jouer("S11_un_barreau_manque", f, 2, ["LECTURE REFUSEE"]))
f = dict(tous); x = fichier(["M1"]); x["reglage"] = dict(REGLAGE, ks=list(range(-3, 8))); f["sonde_ter_point_M1.json"] = x
T.append(jouer("S12_autre_reglage", f, 2, ["LECTURE REFUSEE"]))
d = os.path.join(TRAVAIL, "S13_instrument_ne_tient_pas"); shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
vi = json.load(open(VINST)); vi["instrument"] = "NE TIENT PAS"; json.dump(vi, open(os.path.join(d, "verdict_ter_instrument.json"), "w"))
for n, f_ in tous.items(): json.dump(f_, open(os.path.join(d, n), "w"))
r = subprocess.run([sys.executable, "-I", FEUILLE, "verdict", d, DEPOT], capture_output=True, text=True)
ok = r.returncode == 0 and "VERDICT : NON CONCLUANT D'INSTRUMENT" in r.stdout; T.append(ok)
print("  %-52s %s" % ("S13_instrument_ne_tient_pas", "TIENT" if ok else "MORD "))
print("ESSAI SYNTHETIQUE DE LA FEUILLE : %d cas, %d tenus" % (len(T), sum(T)))
sys.exit(0 if all(T) else 1)
