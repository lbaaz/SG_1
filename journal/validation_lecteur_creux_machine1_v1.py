# -*- coding: ascii -*-
"""Validation du lecteur 2D creux contre les sorties de la nuit bis (sonde certifiee, BOCAL4) : etat 0, six points.
Usage : python3 -I validation_lecteur_creux_machine1_v1.py <moteur.py> <sonde_etage2.json> <dossier du lecteur> [tout]"""
import sys, json, time, math
from fractions import Fraction as F
import numpy as np
sys.path.insert(0, sys.argv[3])
import lecteur_2D_creux_machine1_v1 as L2
M = L2.charger_moteur(sys.argv[1]); D = json.load(open(sys.argv[2])); TOUT = len(sys.argv) > 4
ETAT = {"39_20": (7, 2), "197_100": (7, 2), "99_50": (7, 2), "101_50": (7, 2), "203_100": (7, 2), "41_20": (8, 2)}
pire = 0.0; n = 0; t0 = time.time()
for nom in ["99_50", "39_20", "197_100", "101_50", "203_100", "41_20"]:
    p = D["points"][nom]; num, den = p["w2"].split("/"); w2 = F(int(num), int(den)); g = float(M.g_du_point(w2))
    P = L2.Point(M, w2, g, 71)
    if nom == "99_50":      # controle d'assemblage : bloc N = 60 contre H_2D dense du moteur
        H0, dg = P.bloc(60); Hd, _ = M.H_2D(60, w2, g, -1, "x5", 0.0, None)
        ec = np.max(np.abs((H0.toarray() + np.diag(dg)) - Hd.real)); print("assemblage : ecart max a H_2D du moteur (N = 60) : %.3e ; partie imaginaire du moteur : %.1e" % (ec, np.max(np.abs(Hd.imag))))
        del Hd
    for cfg, c in p["cfg"].items():
        if not TOUT and not (cfg == "F1G20" or nom == "99_50"):
            continue
        N, r_c, forme = c["N"], c["r_c"], c["forme"]
        H0, dg = P.bloc(N); W = L2.W_table(N, forme, r_c)
        ecs = []
        for ks, tr in c["traj"].items():
            e0 = tr["etats"][0]
            r = L2.lire_etat(H0, dg, W, tr["eta"], N, ETAT[nom], e0["E_re"])
            ec = r["gamma"] / e0["gamma"] - 1.0; ecs.append((int(ks), ec, r["gamma_im"] / e0["gamma"] - 1.0, r["E_re"] - e0["E_re"], r["poids_site"]))
            n += 1; pire = max(pire, abs(ec))
        ecs.sort()
        print("%-8s %-6s ecart relatif a BOCAL4, k=-5..12 : %s | max |flux| %.2e, max |-2ImE| %.2e, max |dE_re| %.1e, poids site min %.3f  (%.0f s)" % (
            p["w2"], cfg, " ".join("%+.0e" % x[1] for x in ecs), max(abs(x[1]) for x in ecs), max(abs(x[2]) for x in ecs), max(abs(x[3]) for x in ecs), min(x[4] for x in ecs), time.time() - t0), flush=True)
print("VALIDATION : %d lectures, pire ecart relatif %.3e" % (n, pire))
