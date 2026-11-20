# -*- coding: ascii -*-
"""ENTREES de la boite 2D nue au point sacrifie w2 = 101/50 (machine 2, hors chaine, classe 3). Verifie, pour les trois g de la note de m1 (v2/v3, section 2), que la chaine
a bien 3, 4, 5 barreaux et que le plateau sous absorbeur adapte (ordre 3) retombe sur les Gamma de la note ; mesure le cout de X_saut_reel (construction de la boite).
Usage : py -3.11 -P entrees_boite2d_machine2_v1.py <registre clone>"""
import importlib.util
import math
import sys
import time
from fractions import Fraction as F
import numpy as np
import mpmath as mp

executer = exec
REG = sys.argv[1].rstrip('/\\')
spec = importlib.util.spec_from_file_location("moteur", REG + "/scripts/m17_chaine_v17.py"); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
for bloc in ("chaine_ordre2_bloc_machine1_v1.py", "ordre3_bloc_machine1_v1.py", "chaine_adaptee_bloc_machine1_v1.py"):
    p = REG + "/scripts/" + bloc; executer(compile(open(p, encoding="ascii").read(), p, "exec"))
W2 = F(101, 50)
CELLULES = [(3, 5.53067e-03, 3.2661e-09), (4, 4.22189e-03, 7.2530e-11), (5, 3.35640e-03, 1.5154e-12)]   # (barreaux, g, Gamma) : NOTE de m1 (texte)
print("w2 = %s  delta = w2 - 2 = %+.4f   (energie libre : -W1 n1 + w2 n2 ; echelle du vide (2m, m) : energie m * delta)" % (W2, float(W2) - 2.0))
for nb, g, Gn in CELLULES:
    sites = M.barriere(0, 0, W2, g, True); tb = tables_ordre2(0, 0, W2, g, sites); t3 = tables_ordre3(0, 0, W2, g, tb); p3 = plateau_adapte(tb, t3)
    G = math.exp(p3["ln_G"])
    print("barreaux (len(sites)) = %d (note : %d) | m2_bord = %d | Gamma = %.4e (note : %.4e) | rapport %.5f | etendue de l'absorbeur %s" % (
        len(sites), nb, tb["m2_bord"], G, Gn, G / Gn, p3.get("etendue", "?")), flush=True)
# cout de X_saut_reel
t0 = time.time(); n = 0
for a in range(0, 40):
    for b in range(0, 40):
        for (k, l) in ((1, 0), (0, 1), (2, 1), (1, 2), (3, 0), (0, 3), (4, 1), (2, 3), (5, 0), (1, 4), (3, 2)):
            M.X_saut_reel(5, k, l, float(a), float(b), W2); n += 1
print("X_saut_reel : %d appels en %.2f s (%.2f ms par appel)" % (n, time.time() - t0, 1000 * (time.time() - t0) / n))
