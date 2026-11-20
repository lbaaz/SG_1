# -*- coding: ascii -*-
"""Les ecarts entre niveaux de fuite (poids dehors > 0.99) de la chaine fermee, compares a 2 pi / T_classique(E) au milieu de chaque
paire de niveaux. Machine 2, hors chaine. Usage : py -3.11 -P ecarts_vs_T_pont_machine2_v1.py <registre> <cellule> <N>"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp
from scipy.interpolate import CubicSpline
from scipy.integrate import quad
from scipy.optimize import brentq

executer = exec
REG, CID, N = sys.argv[1].rstrip('/\\'), sys.argv[2], int(sys.argv[3])
spec = importlib.util.spec_from_file_location("moteur", REG + "/scripts/m17_chaine_v17.py"); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
for bloc in ("chaine_ordre2_bloc_machine1_v1.py", "ordre3_bloc_machine1_v1.py", "chaine_adaptee_bloc_machine1_v1.py"):
    p = REG + "/scripts/" + bloc; executer(compile(open(p, encoding="ascii").read(), p, "exec"))
TAB = json.load(open(REG + "/journal/table_cellules_gel_vide_v1.json"))
c = [x for x in TAB["cellules"] if x["id"] == CID][0]
w2 = F(c["w2"]); g = float(c["g"]); sites = M.barriere(0, 0, w2, g, True); tb = tables_ordre2(0, 0, w2, g, sites); ad = abs(c["delta"]); d = tb["d"]
ms = sorted(m for m in tb["t"] if 0 <= m < N); xs = np.array(ms) + 0.5; ys = np.log(np.abs([tb["t"][m] for m in ms]))
sp = CubicSpline(np.log(xs), ys); t = lambda m: math.exp(float(sp(math.log(m))))


def T(E, borne):
    f = lambda m: 4.0 * t(m) ** 2 - (E - m * d) ** 2
    grille = np.linspace(0.6, float(borne), 4000); s = [f(m) for m in grille]
    k = max(i for i in range(len(grille) - 1) if s[i] < 0 <= s[i + 1]); m0 = brentq(f, grille[k], grille[k + 1], xtol=1e-14)
    I, err = quad(lambda u: 2.0 * u / math.sqrt(max(f(m0 + u * u), 1e-300)), 0.0, math.sqrt(borne - m0), limit=400, epsabs=0, epsrel=1e-10)
    return 2.0 * I, m0


n = N + 1; H = np.zeros((n, n))
for m in range(n):
    H[m, m] = m * d
    if m < N:
        H[m, m + 1] = tb["t"][m]; H[m + 1, m] = tb["t"][m]
val, vec = np.linalg.eigh(H)
ext = vec[6:, :] ** 2   # poids au-dela du site 5 (apres la barriere de cette cellule : ajuster si m_bord est plus grand)
pout = ext.sum(axis=0)
idx = [q for q in range(n) if pout[q] > 0.99 and abs(val[q]) < 40 * ad]
print("cellule", CID, "N", N, "m_bord", tb["m2_bord"], " niveaux de fuite (poids dehors > 0.99, |E| < 40 |d|) :", len(idx))
print("   E_k/|d|    ecart au suivant / |d|   milieu/|d|   2pi/T(milieu)/|d|   rapport (ecart observe / (2pi/T))   sortie m0")
for a, b in zip(idx[:-1], idx[1:]):
    if b != a + 1:
        continue
    mid = 0.5 * (val[a] + val[b]); Tm, m0 = T(mid, N - 0.5); gap = (val[b] - val[a]) / ad; ref = 2 * math.pi / Tm / ad
    print("  %+9.3f   %8.3f             %+9.3f    %8.3f           %.3f                           %.2f" % (val[a] / ad, gap, mid / ad, ref, gap / ref, m0))
