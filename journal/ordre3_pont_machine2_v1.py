# -*- coding: ascii -*-
"""Le pont a l'ORDRE 3 (machine 2, hors chaine, 1D seule). Chaine fermee d'ordre 3 (diagonale m d + S(m) - S(0), sauts t+T3 au 1er voisin,
U au 2e, W3 au 3e, W5 au 5e : ceux de m1, relus dans son script). Temps T = -2 dPhi/dE, Phi(E) = Int k(x,E) dx, k racine de la relation de
dispersion a portee longue (valable tant que la dispersion est monotone sur (0, pi) ; verifie et signale). Memes etapes qu'a l'ordre 1 :
V et E_a du croisement ; residu ln(V^2 T / Gamma) avec Gamma = exp(ln_G3) de la table gelee ; calibration r = ecart observe / (2 pi / T)
sur les paires de niveaux de fuite PROPRES ; residu corrige = residu - ln r.
Usage : py -3.11 -P ordre3_pont_machine2_v1.py <registre> <json de m1 pont_v1.json> [cellule]"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp
from scipy.interpolate import PchipInterpolator
from scipy.integrate import quad
from scipy.optimize import brentq

executer = exec
REG, JM1 = sys.argv[1].rstrip('/\\'), sys.argv[2]
ONLY = sys.argv[3] if len(sys.argv) > 3 else None
spec = importlib.util.spec_from_file_location("moteur", REG + "/scripts/m17_chaine_v17.py"); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
for bloc in ("chaine_ordre2_bloc_machine1_v1.py", "ordre3_bloc_machine1_v1.py", "chaine_adaptee_bloc_machine1_v1.py"):
    p = REG + "/scripts/" + bloc; executer(compile(open(p, encoding="ascii").read(), p, "exec"))
TAB = json.load(open(REG + "/journal/table_cellules_gel_vide_v1.json"))
PV1 = {}
for c in json.load(open(JM1))["cellules"]:
    for x in c["croisements"]:
        PV1[(c["id"], x["ordre"], x["N"])] = x


def interp(tab, dec, ln=False):
    ks = sorted(tab.keys()); xs = np.array(ks, dtype=float) + dec; ys = np.array([tab[k] for k in ks], dtype=float)
    if ln:
        sp = PchipInterpolator(xs, np.log(np.abs(ys)), extrapolate=True); sg = 1.0 if ys[0] > 0 else -1.0
        return lambda x: sg * math.exp(float(sp(x)))
    sp = PchipInterpolator(xs, ys, extrapolate=True); return lambda x: float(sp(x))


def modele(tb, t3, ordre):
    d = tb["d"]
    if ordre == 1:
        tau = interp(tb["t"], 0.5, ln=True); z = lambda x: 0.0
        return d, tau, z, z, z, z
    t1 = {m: tb["t"][m] + t3["T3"][m] for m in tb["t"]}
    tau = interp(t1, 0.5, ln=True)
    dS = interp({m: tb["S"][m] - tb["S"][0] for m in tb["S"]}, 0.0)
    return d, tau, interp(tb["U"], 1.0), interp(t3["W3"], 1.5), interp(t3["W5"], 2.5), dS


def temps_fn(tb, t3, ordre, xb):
    d, tau, U, W3, W5, dS = modele(tb, t3, ordre)
    eps = lambda k, x: x * d + dS(x) + 2 * tau(x) * math.cos(k) + 2 * U(x) * math.cos(2 * k) + 2 * W3(x) * math.cos(3 * k) + 2 * W5(x) * math.cos(5 * k)
    veloc = lambda k, x: -2 * tau(x) * math.sin(k) - 4 * U(x) * math.sin(2 * k) - 6 * W3(x) * math.sin(3 * k) - 10 * W5(x) * math.sin(5 * k)
    nonmono = [False]

    def kfun(x, E):
        if E >= eps(0.0, x):
            return 0.0
        if E <= eps(math.pi, x):
            return math.pi
        return brentq(lambda k: eps(k, x) - E, 0.0, math.pi, xtol=1e-13)

    def Phi(E):
        # marge : > 0 si E est dans la bande (entre le bas eps(pi) et le haut eps(0)) ; x0 = derniere entree dans la bande
        f = lambda x: min(eps(0.0, x) - E, E - eps(math.pi, x))
        gr = np.linspace(0.6, xb, 1500); s = [f(x) for x in gr]
        idx = [i for i in range(len(gr) - 1) if s[i] < 0 <= s[i + 1]]
        x0 = brentq(f, gr[idx[-1]], gr[idx[-1] + 1], xtol=1e-14)
        haut = (eps(0.0, x0) - E) < (E - eps(math.pi, x0))    # le point de retournement est sur le bord HAUT (k = 0) ou BAS (k = pi)
        kap = (lambda x: kfun(x, E)) if haut else (lambda x: math.pi - kfun(x, E))
        I, err = quad(lambda u: 2.0 * u * kap(x0 + u * u), 0.0, math.sqrt(xb - x0), limit=400, epsabs=0, epsrel=1e-10)
        return I, x0

    def T(E, h):
        (Pp, x0p), (Pm, x0m) = Phi(E + h), Phi(E - h); (P0, x0) = Phi(E)
        return 2.0 * abs(Pp - Pm) / (2.0 * h), x0
    def chk(x0):
        """Premier x >= x0 ou la dispersion cesse d'etre monotone sur (0, pi) (vitesse >= 0 pour un k) ; -1 si elle l'est partout jusqu'a xb."""
        for x in np.linspace(x0, xb, 120):
            if max(veloc(k, x) for k in np.linspace(0.02, math.pi - 0.02, 80)) >= 0.0:
                return float(x)
        return -1.0
    return T, chk


def T_ancien_ordre1(tb, E, N):
    """T de l'ordre 1 par l'integrale de 1/vitesse (interpolation PCHIP de ln t en x = m + 1/2), comme dans mon premier controle."""
    d = tb["d"]; tau = interp(tb["t"], 0.5, ln=True)
    f = lambda m: 4.0 * tau(m) ** 2 - (E - m * d) ** 2
    gr = np.linspace(0.6, N - 0.5, 4000); s = [f(m) for m in gr]; k = max(i for i in range(len(gr) - 1) if s[i] < 0 <= s[i + 1]); m0 = brentq(f, gr[k], gr[k + 1], xtol=1e-14)
    I, err = quad(lambda u: 2.0 * u / math.sqrt(max(f(m0 + u * u), 1e-300)), 0.0, math.sqrt(N - 0.5 - m0), limit=400, epsabs=0, epsrel=1e-10)
    return 2.0 * I


def chaine(tb, t3, N, ordre):
    H = np.zeros((N + 1, N + 1))
    for m in range(N + 1):
        H[m, m] = m * tb["d"] + ((tb["S"][m] - tb["S"][0]) if ordre == 3 else 0.0)
        if m < N:
            x = tb["t"][m] + (t3["T3"][m] if ordre == 3 else 0.0); H[m, m + 1] = x; H[m + 1, m] = x
        if ordre == 3:
            for pas, tab in ((2, tb["U"]), (3, t3["W3"]), (5, t3["W5"])):
                if m + pas <= N:
                    H[m, m + pas] = tab[m]; H[m + pas, m] = tab[m]
    return H


def premier_croisement(H0, ech):
    lire = lambda th: np.linalg.eigh(H0 + np.diag([0.0] * (len(H0) - 1) + [ech * math.tan(th)]))
    gr = np.linspace(-1.5, 1.5, 481); rg = [int(np.argmax(lire(th)[1][0, :] ** 2)) for th in gr]
    ks = [i for i in range(len(gr) - 1) if rg[i] != rg[i + 1]]
    if not ks:
        return None
    k = ks[0]; lo, hi, rlo = float(gr[k]), float(gr[k + 1]), rg[k]
    for _ in range(200):
        mi = 0.5 * (lo + hi)
        if mi == lo or mi == hi:
            break
        if int(np.argmax(lire(mi)[1][0, :] ** 2)) == rlo:
            lo = mi
        else:
            hi = mi
    return lire(0.5 * (lo + hi))


print("ordre cellule m  N   V (le mien)   V de m1 (ou -)   T/T_ancien(ordre1)   residu ln(V^2T/G)   r propres (min..max) nb   residu corrige")
for c in [x for x in TAB["cellules"] if x["ligne"] == "lisible" and (ONLY is None or x["id"] == ONLY)]:
    w2 = F(c["w2"]); g = float(c["g"]); sites = M.barriere(0, 0, w2, g, True); tb = tables_ordre2(0, 0, w2, g, sites); t3 = tables_ordre3(0, 0, w2, g, tb)
    ad = abs(c["delta"]); mb = tb["m2_bord"]; d = tb["d"]
    Ns = sorted({mb + cc + L for cc in (6, 8, 10) for L in (16, 20, 24)})
    for ordre, lnG in ((1, c["ln_G1"]), (3, c["ln_G3"])):
        for N in (Ns[0], Ns[len(Ns) // 2], Ns[-1]):
            H0 = chaine(tb, t3, N, ordre); res = premier_croisement(H0, abs(tb["t"][N - 1]))
            if res is None:
                print(ordre, c["id"], mb, N, "pas de croisement"); continue
            val, vec = res; i, j = sorted(int(x) for x in np.argsort(-vec[0, :] ** 2)[:2]); V = 0.5 * (val[j] - val[i]); Ea = 0.5 * (val[i] + val[j])
            T, chk = temps_fn(tb, t3, ordre, N - 0.5); h = 0.05 * ad
            Tc, x0 = T(Ea, h); resid = math.log(V * V * Tc) - lnG
            rap = (Tc / T_ancien_ordre1(tb, Ea, N)) if ordre == 1 else float("nan")
            pout = (vec[int(math.ceil(x0)) + 3:, :] ** 2).sum(axis=0)
            idx = [q for q in range(len(val)) if pout[q] > 0.99 and abs(val[q] - Ea) < 60 * ad]; rs = []
            for a, b in zip(idx[:-1], idx[1:]):
                if b == a + 1:
                    mid = 0.5 * (val[a] + val[b]); Tm, _ = T(mid, h); rs.append((val[b] - val[a]) / (2 * math.pi / Tm))
            v1 = PV1.get((c["id"], ordre, N)); v1s = ("%.4e" % v1["V"]) if v1 else "-"
            xnm = chk(x0); nm = ("monotone" if xnm < 0 else "NON MONOTONE des x=%.1f" % xnm)
            if rs:
                r = float(np.mean(rs)); print("%d     %-5s %d  %-3d %.4e   %s   %.4f   %+.4f   %.4f (%.4f..%.4f) %d   %+.4f   %s" % (ordre, c["id"], mb, N, V, v1s, rap, resid, r, min(rs), max(rs), len(rs), resid - math.log(r), nm), flush=True)
            else:
                print("%d     %-5s %d  %-3d %.4e   %s   %.4f   %+.4f   (aucune paire propre)   %s" % (ordre, c["id"], mb, N, V, v1s, rap, resid, nm), flush=True)
