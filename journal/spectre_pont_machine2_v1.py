# -*- coding: ascii -*-
"""Spectre de la chaine fermee autour du croisement (machine 2, hors chaine). Pour une cellule et une coupure N :
liste des niveaux dans +-W |delta|, avec leur poids sur le site 0, sur la barriere (m <= m0) et sur le dehors (m > m0).
Usage : py -3.11 -P spectre_pont_machine2_v1.py <registre> <cellule> <N> [W]"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp

executer = exec
REG, CID, N = sys.argv[1].rstrip('/\\'), sys.argv[2], int(sys.argv[3]); W = float(sys.argv[4]) if len(sys.argv) > 4 else 12.0
spec = importlib.util.spec_from_file_location("moteur", REG + "/scripts/m17_chaine_v17.py"); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
for bloc in ("chaine_ordre2_bloc_machine1_v1.py", "ordre3_bloc_machine1_v1.py", "chaine_adaptee_bloc_machine1_v1.py"):
    p = REG + "/scripts/" + bloc; executer(compile(open(p, encoding="ascii").read(), p, "exec"))
TAB = json.load(open(REG + "/journal/table_cellules_gel_vide_v1.json"))
c = [x for x in TAB["cellules"] if x["id"] == CID][0]
w2 = F(c["w2"]); g = float(c["g"]); sites = M.barriere(0, 0, w2, g, True); tb = tables_ordre2(0, 0, w2, g, sites); ad = abs(c["delta"]); mb = tb["m2_bord"]
print("cellule", CID, "m_bord", mb, "delta", c["delta"], "d", tb["d"])
print("t(m), m=0..%d :" % (mb + 8), ["%.3e" % tb["t"][m] for m in range(0, mb + 9)])
print("sites m*d/|d| :", ["%.2f" % (m * tb["d"] / ad) for m in range(0, mb + 9)])
n = N + 1; H0 = np.zeros((n, n))
for m in range(n):
    H0[m, m] = m * tb["d"]
    if m < N:
        H0[m, m + 1] = tb["t"][m]; H0[m + 1, m] = tb["t"][m]
ech = abs(tb["t"][N - 1])


def lire(th):
    H = H0.copy(); H[-1, -1] += ech * math.tan(th); return np.linalg.eigh(H)


# croisement : premier changement de rang du poids maximal sur le site 0
grille = np.linspace(-1.5, 1.5, 481); rg = [int(np.argmax(lire(th)[1][0, :] ** 2)) for th in grille]
k = [i for i in range(len(grille) - 1) if rg[i] != rg[i + 1]][0]
lo, hi, rlo = float(grille[k]), float(grille[k + 1]), rg[k]
for _ in range(200):
    mi = 0.5 * (lo + hi)
    if mi == lo or mi == hi:
        break
    if int(np.argmax(lire(mi)[1][0, :] ** 2)) == rlo:
        lo = mi
    else:
        hi = mi
th = 0.5 * (lo + hi); val, vec = lire(th)
p0 = vec[0, :] ** 2; E0 = val[np.argsort(-p0)[:2]].mean()
m0 = {"MG3": 4.41, "MG4": 5.39, "MG5": 6.37}.get(CID, mb + 1.4)
print("theta du croisement %.12f  E du croisement/|d| %+.4e   m0 (sortie de barriere, valeur de m1) %.2f" % (th, E0 / ad, m0))
print("  k    (E - E0)/|d|    poids site0   poids barriere(1..m0)   poids dehors (m>m0)   ecart au precedent / |d|")
prev = None
for q in range(len(val)):
    e = (val[q] - E0) / ad
    if abs(e) <= W:
        pb = float((vec[1:int(m0) + 1, q] ** 2).sum()); pd = float((vec[int(m0) + 1:, q] ** 2).sum())
        print("%3d  %+10.4f   %.4f   %.4f   %.4f    %s" % (q, e, vec[0, q] ** 2, pb, pd, "" if prev is None else "%.4f" % (e - prev)))
        prev = e
