# -*- coding: ascii -*-
"""Essai d'un temoin negatif : le jumeau H+ a la geometrie de l'ancre A1 (meme w2, meme g, meme etiquette (7,2)),
sous les quatre absorbeurs. Sa largeur intrinseque est nulle a cette precision : ce que le lecteur rend est fait
par l'absorbeur et doit etre proportionnel a eta (pas de plateau). Et le temoin positif sous D (non vu jusqu'ici).
Usage : python3 -I essai_temoin_negatif_machine1_v1.py <moteur.py> <bloc.py> <sonde_ordre2.json> <tp_reference.json>"""
import sys, json, math, time, importlib.util
from fractions import Fraction as F
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sl
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
exec(compile(open(sys.argv[2]).read(), sys.argv[2], "exec"))
S = json.load(open(sys.argv[3])); REF = {b["j"]: b for b in json.load(open(sys.argv[4]))["balayage"]}
KS = list(range(-3, 9)); ABS = [("A", "F2", 0, 60), ("B", "F2", 0, 80), ("C", "F1", 0, 80), ("D", "F2", 10, 60)]
def best(v):
    return min(max(v[i:i + 5]) / min(v[i:i + 5]) - 1.0 for i in range(len(v) - 4))
p = [q for q in S["points"] if q["id"] == "A1"][0]; w2 = F(39, 20); g = p["g"]; r_c = p["r_c"]; eta0 = p["eta0"]
H0m, dm = assembler(w2, g, r_c + 80, signe=+1)
for site in ((7, 2), (0, 0)):
    for nom, forme, dr, L in ABS:
        N = r_c + dr + L; H0, dg = restreindre(H0m, dm, r_c + 80, N)
        tr = trajectoire(H0, dg, table_W(N, forme, r_c + dr, L), eta0, N, site, float(site[0]) + float(w2) * site[1], KS)
        v = [tr[str(k)]["gamma"] for k in KS]
        print("jumeau H+ a la geometrie de A1, site %s, %s : gamma k=-3..8 : %s | suivis %d | rapports successifs : %s" % (
            site, nom, " ".join("%.2e" % x for x in v), sum(tr[str(k)]["suivi"] for k in KS),
            " ".join("%.2f" % (v[i + 1] / v[i]) if v[i] > 0 else "nan" for i in range(len(v) - 1))), flush=True)
for j, g in ((6, 0.08408964152537146), (8, 0.1)):
    H0m, dm = assembler(w2, g, 120, signe=+1)
    for nom, forme, dr, L in ABS:
        N = 40 + dr + L; H0, dg = restreindre(H0m, dm, 120, N)
        tr = trajectoire(H0, dg, table_W(N, forme, 40 + dr, L), 0.05, N, (0, 0), 0.0, KS)
        v = [tr[str(k)]["gamma"] / REF[j]["Gamma_ref"] for k in KS]
        print("temoin positif j = %d, %s : gamma / reference, k=-3..8 : %s | meilleur etalement %.4f | suivis %d | iterations max %d" % (
            j, nom, " ".join("%.4f" % x for x in v), best(v), sum(tr[str(k)]["suivi"] for k in KS), max(tr[str(k)]["iterations"] for k in KS)), flush=True)
