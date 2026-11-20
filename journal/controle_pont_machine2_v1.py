# -*- coding: ascii -*-
"""CONTROLE du pont de machine 1 (note du 16/11 soir) -- machine 2, v1. Hors chaine. Aucune 2D. Aucun gel.
Refait par mon code : chaine fermee du premier ordre, croisement evite de l'etat du site 0, V ; temps classique T par QUATRE
interpolations de t(m) ; classement des niveaux voisins (famille 'dehors' ou echelle sous la barriere).
Usage : py -3.11 -P controle_pont_machine2_v1.py <clone du registre> <json de m1 : pont_semiclassique_v1.json> [cellule]"""
import sys, os, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp
from scipy.interpolate import CubicSpline, PchipInterpolator
from scipy.integrate import quad
from scipy.optimize import brentq

executer = exec   # charge les blocs du registre dans l'espace de noms (meme usage que le script de m1)
REG, JM1 = sys.argv[1], sys.argv[2]
ONLY = sys.argv[3] if len(sys.argv) > 3 else None
S = REG.rstrip('/\\')
spec = importlib.util.spec_from_file_location("moteur", S + "/scripts/m17_chaine_v17.py"); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
for bloc in ("chaine_ordre2_bloc_machine1_v1.py", "ordre3_bloc_machine1_v1.py", "chaine_adaptee_bloc_machine1_v1.py"):
    p = S + "/scripts/" + bloc; executer(compile(open(p, encoding="ascii").read(), p, "exec"))
TAB = json.load(open(S + "/journal/table_cellules_gel_vide_v1.json"))
CEL = [c for c in TAB["cellules"] if c["ligne"] == "lisible" and (ONLY is None or c["id"] == ONLY)]
M1 = {c["id"]: c for c in json.load(open(JM1))["cellules"]}


def chaine_fermee(tb, N):
    n = N + 1; H = np.zeros((n, n))
    for m in range(N + 1):
        H[m, m] = m * tb["d"]
        if m < N:
            H[m, m + 1] = tb["t"][m]; H[m + 1, m] = tb["t"][m]
    return H


def croisements(H0, ech):
    """Tous les croisements evites de l'etat du site 0 sur theta in (-1.5, 1.5) : retourne (theta, val, vec) au croisement."""
    def lire(th):
        H = H0.copy(); H[-1, -1] += ech * math.tan(th); val, vec = np.linalg.eigh(H); return val, vec
    grille = np.linspace(-1.5, 1.5, 481)
    rg = [int(np.argmax(lire(th)[1][0, :] ** 2)) for th in grille]
    out = []
    for k in range(len(grille) - 1):
        if rg[k] == rg[k + 1]:
            continue
        lo, hi, rlo = float(grille[k]), float(grille[k + 1]), rg[k]
        for _ in range(200):
            mi = 0.5 * (lo + hi)
            if mi == lo or mi == hi:
                break
            val, vec = lire(mi)
            if int(np.argmax(vec[0, :] ** 2)) == rlo:
                lo = mi
            else:
                hi = mi
        val, vec = lire(0.5 * (lo + hi)); out.append((0.5 * (lo + hi), val, vec))
    return out


def temps(tb, E, N, mode):
    """T(E) = 2 Int dm / sqrt(4 t^2 - (E - m d)^2), de la sortie de la barriere (dernier changement de signe) au bout m = N.
    mode 'spline_ln' : spline cubique de ln t en ln(m+1/2) (convention de m1) ; 'pchip_lin' : PCHIP de ln t en m+1/2 ;
    'lin_ln' : interpolation lineaire de ln t en m+1/2 ; 'spline_m' : spline cubique de ln t en m + 1/2 (abscisse lineaire)."""
    d = tb["d"]; ms = sorted(m for m in tb["t"] if 0 <= m < N); xs = np.array(ms) + 0.5; ys = np.log(np.abs([tb["t"][m] for m in ms]))
    if mode == "spline_ln":
        sp = CubicSpline(np.log(xs), ys); t = lambda m: math.exp(float(sp(math.log(m))))
    elif mode == "pchip_lin":
        sp = PchipInterpolator(xs, ys); t = lambda m: math.exp(float(sp(m)))
    elif mode == "lin_ln":
        t = lambda m: math.exp(float(np.interp(m, xs, ys)))
    elif mode == "spline_m":
        sp = CubicSpline(xs, ys); t = lambda m: math.exp(float(sp(m)))
    f = lambda m: 4.0 * t(m) ** 2 - (E - m * d) ** 2
    grille = np.linspace(0.6, float(N - 0.5), 4000); s = [f(m) for m in grille]
    k = max(i for i in range(len(grille) - 1) if s[i] < 0 <= s[i + 1])
    m0 = brentq(f, grille[k], grille[k + 1], xtol=1e-14)
    g = lambda u: 2.0 * u / math.sqrt(max(f(m0 + u * u), 1e-300))
    I, err = quad(g, 0.0, math.sqrt(N - 0.5 - m0), limit=400, epsabs=0, epsrel=1e-10)
    return 2.0 * I, m0


MODES = ("spline_ln", "pchip_lin", "lin_ln", "spline_m")
print("cellule m   N  ncr  V            2pi/T/|d|   ln(V^2T/G): spline_ln  pchip_lin  lin_ln  spline_m   | poids dehors des voisins bas/haut   ecart bas/haut en |d|")
bilan = {md: [] for md in MODES}; tous = 0; distincts = set()
for c in CEL:
    w2 = F(c["w2"]); g = float(c["g"]); sites = M.barriere(0, 0, w2, g, True); tb = tables_ordre2(0, 0, w2, g, sites)
    lnG = c["ln_G1"]; ad = abs(c["delta"]); mb = tb["m2_bord"]
    Ns = sorted({mb + cc + L for cc in (6, 8, 10) for L in (16, 20, 24)})
    for N in Ns:
        H0 = chaine_fermee(tb, N); ech = abs(tb["t"][N - 1]); cr = croisements(H0, ech)
        for th, val, vec in cr:
            p = vec[0, :] ** 2; o = np.argsort(-p)[:2]; i, j = sorted(int(x) for x in o)
            if j != i + 1 or i - 1 < 0 or j + 1 >= len(val):
                continue
            V = 0.5 * (val[j] - val[i]); E = 0.5 * (val[i] + val[j]); tous += 1; distincts.add((c["id"], N))
            row = []
            for md in MODES:
                T, m0 = temps(tb, E, N, md); row.append(math.log(V * V * T) - lnG); bilan[md].append(row[-1])
                if md == "spline_ln":
                    Tref, m0ref = T, m0
            ext = np.arange(len(val)) > m0ref + 1.0
            wb = float((vec[ext, i - 1] ** 2).sum()); wh = float((vec[ext, j + 1] ** 2).sum())
            print("%-5s %d  %-3d  %d  %.4e  %.3f       %+.4f  %+.4f  %+.4f  %+.4f  | %.3f %.3f   %.2f %.2f" % (
                c["id"], mb, N, len(cr), V, 2 * math.pi / Tref / ad, row[0], row[1], row[2], row[3], wb, wh, (val[i] - val[i - 1]) / ad, (val[j + 1] - val[j]) / ad), flush=True)
print("croisements", tous, "paires (cellule,N) distinctes", len(distincts))
for md in MODES:
    a = np.array(bilan[md]); print("%-10s ln(V^2T/G) : min %+.4f  max %+.4f  moyenne %+.4f" % (md, a.min(), a.max(), a.mean()))
