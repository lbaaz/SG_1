# -*- coding: ascii -*-
"""Le residu ln(V^2 T_cl / Gamma) du pont de machine 1 s'explique-t-il par l'ecart T_cl / T lu sur le spectre ? Machine 2, hors chaine.
Pour chaque cellule lisible, une coupure N : V et E du croisement ; T_cl(E) ; Gamma = exp(ln_G1) de la table gelee ;
rapport r = (ecart observe entre deux niveaux de fuite PROPRES) / (2 pi / T_cl au milieu), moyenne sur les paires propres ;
correction = -ln r (si T_vrai = T_cl / r). On imprime residu, correction, residu corrige.
Usage : py -3.11 -P residu_vs_spectre_pont_machine2_v1.py <registre> [N_decalage = 28]  (N = m_bord + N_decalage)"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp
from scipy.interpolate import CubicSpline
from scipy.integrate import quad
from scipy.optimize import brentq

executer = exec
REG = sys.argv[1].rstrip('/\\'); DEC = int(sys.argv[2]) if len(sys.argv) > 2 else 28
spec = importlib.util.spec_from_file_location("moteur", REG + "/scripts/m17_chaine_v17.py"); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
for bloc in ("chaine_ordre2_bloc_machine1_v1.py", "ordre3_bloc_machine1_v1.py", "chaine_adaptee_bloc_machine1_v1.py"):
    p = REG + "/scripts/" + bloc; executer(compile(open(p, encoding="ascii").read(), p, "exec"))
TAB = json.load(open(REG + "/journal/table_cellules_gel_vide_v1.json"))


def temps_fn(tb, N):
    d = tb["d"]; ms = sorted(m for m in tb["t"] if 0 <= m < N); xs = np.array(ms) + 0.5; ys = np.log(np.abs([tb["t"][m] for m in ms]))
    sp = CubicSpline(np.log(xs), ys); t = lambda m: math.exp(float(sp(math.log(m))))
    def T(E):
        f = lambda m: 4.0 * t(m) ** 2 - (E - m * d) ** 2
        grille = np.linspace(0.6, N - 0.5, 4000); s = [f(m) for m in grille]
        k = max(i for i in range(len(grille) - 1) if s[i] < 0 <= s[i + 1]); m0 = brentq(f, grille[k], grille[k + 1], xtol=1e-14)
        I, err = quad(lambda u: 2.0 * u / math.sqrt(max(f(m0 + u * u), 1e-300)), 0.0, math.sqrt(N - 0.5 - m0), limit=400, epsabs=0, epsrel=1e-10)
        return 2.0 * I, m0
    return T


print("cellule m  N   V            residu ln(V^2T_cl/G)   r (paires propres)  nb   correction -ln r   residu corrige")
for c in [x for x in TAB["cellules"] if x["ligne"] == "lisible"]:
    w2 = F(c["w2"]); g = float(c["g"]); sites = M.barriere(0, 0, w2, g, True); tb = tables_ordre2(0, 0, w2, g, sites); ad = abs(c["delta"]); d = tb["d"]; mb = tb["m2_bord"]
    N = mb + DEC; n = N + 1; H0 = np.zeros((n, n))
    for m in range(n):
        H0[m, m] = m * d
        if m < N:
            H0[m, m + 1] = tb["t"][m]; H0[m + 1, m] = tb["t"][m]
    ech = abs(tb["t"][N - 1])
    def lire(th):
        H = H0.copy(); H[-1, -1] += ech * math.tan(th); return np.linalg.eigh(H)
    grille = np.linspace(-1.5, 1.5, 481); rg = [int(np.argmax(lire(th)[1][0, :] ** 2)) for th in grille]
    ks = [i for i in range(len(grille) - 1) if rg[i] != rg[i + 1]]
    if not ks:
        print(c["id"], "pas de croisement"); continue
    k = ks[0]; lo, hi, rlo = float(grille[k]), float(grille[k + 1]), rg[k]
    for _ in range(200):
        mi = 0.5 * (lo + hi)
        if mi == lo or mi == hi:
            break
        if int(np.argmax(lire(mi)[1][0, :] ** 2)) == rlo:
            lo = mi
        else:
            hi = mi
    val, vec = lire(0.5 * (lo + hi)); o = sorted(int(x) for x in np.argsort(-vec[0, :] ** 2)[:2]); i, j = o
    V = 0.5 * (val[j] - val[i]); Ea = 0.5 * (val[i] + val[j])
    T = temps_fn(tb, N); Tcl, m0a = T(Ea); res = math.log(V * V * Tcl) - c["ln_G1"]
    skip = int(math.ceil(m0a)) + 3
    pout = (vec[skip:, :] ** 2).sum(axis=0)
    idx = [q for q in range(n) if pout[q] > 0.99 and abs(val[q] - Ea) < 60 * ad]
    rs = []
    for a, b in zip(idx[:-1], idx[1:]):
        if b == a + 1:
            mid = 0.5 * (val[a] + val[b]); Tm, _ = T(mid); rs.append(((val[b] - val[a]) / (2 * math.pi / Tm)))
    if rs:
        r = float(np.mean(rs)); corr = -math.log(r)
        print("%-5s %d  %-3d %.4e   %+.4f              %.4f  (%.4f..%.4f)  %d   %+.4f           %+.4f" % (c["id"], mb, N, V, res, r, min(rs), max(rs), len(rs), corr, res + corr), flush=True)
    else:
        print("%-5s %d  %-3d %.4e   %+.4f              (aucune paire propre)" % (c["id"], mb, N, V, res), flush=True)
