# -*- coding: ascii -*-
"""Exploration hors chaine (classe 3, post hoc) : la lecture 2D de l'etat 0 aux points DEJA JOUES de M17,
sous des absorbeurs que la nuit bis n'a pas joues (plus longs, autres bords). Lecteur creux valide (3.9e-3 au pire).
Usage : python3 -I exploration_absorbeurs_machine1_v1.py <moteur.py> <sonde_etage2.json> <dossier du lecteur> <sortie.json> <point> [<point> ...]"""
import sys, json, time, math
from fractions import Fraction as F
import numpy as np
sys.path.insert(0, sys.argv[3])
import lecteur_2D_creux_machine1_v1 as L2
M = L2.charger_moteur(sys.argv[1]); D = json.load(open(sys.argv[2])); SORTIE = sys.argv[4]; NOMS = sys.argv[5:]
ETAT = {"39_20": (7, 2), "197_100": (7, 2), "99_50": (7, 2), "101_50": (7, 2), "203_100": (7, 2), "41_20": (8, 2)}
KS = list(range(-5, 15))
CONFIGS = [("F1", 0, 20), ("F1", 0, 30), ("F1", 0, 40), ("F1", 0, 60), ("F1", 0, 80),
           ("F2", 0, 20), ("F2", 0, 30), ("F2", 0, 40), ("F2", 0, 60), ("F2", 0, 80),
           ("F3", 0, 30), ("F3", 0, 40), ("F3", 0, 60),
           ("F1", 10, 30), ("F1", 10, 40), ("F1", 10, 60), ("F1", -10, 30), ("F1", -10, 50), ("F1", -20, 40), ("F1", -20, 60)]
try:
    sortie = json.load(open(SORTIE))
except Exception:
    sortie = {"points": {}}
t0 = time.time()
for nom in NOMS:
    p = D["points"][nom]; num, den = p["w2"].split("/"); w2 = F(int(num), int(den)); g = float(M.g_du_point(w2)); r0 = p["r0"]; eta0 = p["eta0"]
    Nmax = max(r0 + dr + L for (_, dr, L) in CONFIGS)
    P = L2.Point(M, w2, g, Nmax)
    print("%s : assemblage Nmax = %d, %.0f s" % (nom, Nmax, time.time() - t0), flush=True)
    E3 = p["cfg"]["F1G20"]["traj"]["3"]["etats"][0]["E_re"]
    pt = sortie["points"].setdefault(nom, {"w2": p["w2"], "g": g, "r0": r0, "eta0": eta0, "G_run": p["G_run"], "cfg": {}})
    for (forme, dr, L) in CONFIGS:
        cle = "%s_r%+d_L%d" % (forme, dr, L)
        if cle in pt["cfg"]:
            continue
        r_c = r0 + dr; N = r_c + L
        H0, dg = P.bloc(N); W = L2.W_table(N, forme, r_c)
        traj = {}; Ec = E3
        for k in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
            r = L2.lire_etat(H0, dg, W, eta0 * 2.0 ** (-k), N, ETAT[nom], Ec, n_voisins=8); traj[str(k)] = r
            if r["poids_site"] > 0.5: Ec = r["E_re"]
        Ec = traj["3"]["E_re"]
        for k in [2, 1, 0, -1, -2, -3, -4, -5]:
            r = L2.lire_etat(H0, dg, W, eta0 * 2.0 ** (-k), N, ETAT[nom], Ec, n_voisins=8); traj[str(k)] = r
            if r["poids_site"] > 0.5: Ec = r["E_re"]
        pt["cfg"][cle] = {"forme": forme, "r_c": r_c, "L": L, "N": N, "traj": traj}
        G = p["G_run"]
        print("  %-12s N %3d : " % (cle, N) + " ".join("%.3f" % (traj[str(k)]["gamma"] / G) for k in KS) + "  | poids min %.2f  (%.0f s)" % (min(traj[str(k)]["poids_site"] for k in KS), time.time() - t0), flush=True)
        json.dump(sortie, open(SORTIE, "w"), indent=1, sort_keys=True)
print("fini", time.time() - t0)
