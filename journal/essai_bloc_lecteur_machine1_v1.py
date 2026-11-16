# -*- coding: ascii -*-
"""Essai du bloc du lecteur : (i) contre le lecteur d'exploration (ARPACK) a l'etat lu de 1.98, F2 a 60 couches ;
(ii) contre la sonde dense deposee (delta 98) aux ancres A1 et A2, k = 2, 3, 4, F1 a 20 couches, tous les etats.
Usage : python3 -I essai_bloc_lecteur_machine1_v1.py <moteur.py> <bloc.py> <exploration_v1.json> <sonde_ordre2.json>"""
import sys, json, math, time, importlib.util
from fractions import Fraction as F
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sl
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
exec(compile(open(sys.argv[2]).read(), sys.argv[2], "exec"))
EX = json.load(open(sys.argv[3]))["points"]["99_50"]; S = json.load(open(sys.argv[4]))
t0 = time.time()
w2 = F(99, 50); g = float(M.g_du_point(w2)); H0m, dm = assembler(w2, g, 100)
H0, dg = restreindre(H0m, dm, 100, 100); W = table_W(100, "F2", 40, 60)
E3 = EX["cfg"]["F2_r+0_L60"]["traj"]["3"]["E_re"]
tr = trajectoire(H0, dg, W, EX["eta0"], 100, (7, 2), E3, list(range(-5, 15)))
ec = max(abs(tr[str(k)]["gamma"] / EX["cfg"]["F2_r+0_L60"]["traj"][str(k)]["gamma"] - 1.0) for k in range(-5, 15))
print("(i) 1.98, F2 a 60 couches, k = -5 a 14 : pire ecart relatif au lecteur d'exploration %.1e ; iterations max %d ; suivis %d sur 20 ; %.0f s" % (
    ec, max(tr[str(k)]["iterations"] for k in range(-5, 15)), sum(tr[str(k)]["suivi"] for k in range(-5, 15)), time.time() - t0))
for pid in ("A1", "A2"):
    p = [q for q in S["points"] if q["id"] == pid][0]
    num, den = p["w2"].split("/"); w2 = F(int(num), int(den)); g = p["g"]; N = p["N"]; r_c = p["r_c"]
    H0, dg = assembler(w2, g, N); H0 = H0.tocsc(); W = table_W(N, "F1", r_c, N - r_c)
    pire_rel = 0.0; pire_abs = 0.0; n = 0; hors = []
    for e in p["etats"]:
        tr = trajectoire(H0, dg, W, p["eta0"], N, (int(e["n1"]), int(e["n2"])), e["E_re"], [2, 3, 4])
        for k in ("2", "3", "4"):
            gd = e["Gamma_2D"][k]; gl = tr[k]["gamma"]; n += 1
            da = abs(gl - gd); pire_abs = max(pire_abs, da)
            if gd > 1.33e-10: pire_rel = max(pire_rel, da / gd)
            if da > 1e-3 * gd + 6e-13 or not tr[k]["suivi"]: hors.append((e["rang"], k, gd, gl, tr[k]["suivi"], tr[k]["poids_site"]))
    print("(ii) %s (N %d, r_c %d) : %d lectures ; pire ecart absolu %.2e ; pire ecart relatif au-dessus de mille planchers %.1e ; hors (1e-3 relatif + 6e-13) : %s ; %.0f s" % (
        pid, N, r_c, n, pire_abs, pire_rel, hors, time.time() - t0))
