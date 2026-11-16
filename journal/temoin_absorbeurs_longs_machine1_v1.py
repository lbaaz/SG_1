# -*- coding: ascii -*-
"""Le temoin positif (jumeau H+, largeur connue par rotation complexe) sous le lecteur creux : (i) validation contre
l'etage 1 de la nuit bis (F1, G20 et G30) ; (ii) absorbeurs longs F1 et F2 (L = 60, 80). Hors chaine, classe 3.
Usage : python3 -I temoin_absorbeurs_longs_machine1_v1.py <moteur.py> <sonde_etage1.json> <dossier du lecteur>"""
import sys, json, time, math
from fractions import Fraction as F
import numpy as np
sys.path.insert(0, sys.argv[3])
import lecteur_2D_creux_machine1_v2 as L2
M = L2.charger_moteur(sys.argv[1]); D = json.load(open(sys.argv[2]))
REF = {"j06": 5.3688e-10, "j08": 6.4279e-09}
w2 = F(39, 20); r_c = 40; eta0 = 0.05; t0 = time.time()
for j in ("j06", "j08"):
    tp = D["TP"][j]; g = tp["g"]; ref = REF[j]
    P = L2.Point(M, w2, g, 120, signe=+1)
    print("=== %s g = %.5f Gamma_ref = %.4e ; cles traj : %s" % (j, g, ref, list(tp["traj"].keys())))
    # validation contre la nuit
    for geo, tr in tp["traj"].items():
        N = 60 if "20" in geo else 70
        H0, dg = P.bloc(N); W = L2.W_table(N, "F1", r_c)
        ecs = []
        for ks in sorted(tr.keys(), key=int):
            e = tr[ks]; e0 = e["etats"][0] if "etats" in e else e
            if e0.get("gamma") is None: continue
            r = L2.lire_etat(H0, dg, W, eta0 * 2.0 ** (-int(ks)), N, (0, 0), e0["E_re"], n_voisins=6)
            ecs.append((int(ks), r["gamma"] / e0["gamma"] - 1.0, r["gamma"] / ref, e0["gamma"] / ref))
        print("  %s : lecteur creux / reference, k=-5.. : %s" % (geo, " ".join("%.4f" % x[2] for x in ecs)))
        print("  %s : sonde BOCAL4 / reference,  k=-5.. : %s" % (geo, " ".join("%.4f" % x[3] for x in ecs)))
        print("  %s : ecart relatif creux / BOCAL4, max sur k <= 3 : %.2e" % (geo, max(abs(x[1]) for x in ecs if x[0] <= 3)), flush=True)
    E0 = tp["traj"][list(tp["traj"].keys())[0]]["3"]
    E0 = (E0["etats"][0] if "etats" in E0 else E0)["E_re"]
    for (forme, L) in (("F1", 60), ("F2", 60), ("F1", 80), ("F2", 80)):
        N = r_c + L; H0, dg = P.bloc(N); W = L2.W_table(N, forme, r_c)
        vals = []
        for k in range(-5, 13):
            r = L2.lire_etat(H0, dg, W, eta0 * 2.0 ** (-k), N, (0, 0), E0, n_voisins=6); vals.append(r["gamma"] / ref)
        print("  %s L%d (N %d) / reference, k=-5..12 : %s  (%.0f s)" % (forme, L, N, " ".join("%.4f" % v for v in vals), time.time() - t0), flush=True)
