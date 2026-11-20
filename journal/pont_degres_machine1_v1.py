# -*- coding: ascii -*-
"""LE PONT, EPREUVE HORS ECHANTILLON : D'AUTRES DEGRES -- machine 1, v1, 2026-11-16. HORS CHAINE, classe 3, premier ordre seul.
Le choix du temps classique T dans Gamma = V^2 T est venu APRES avoir vu les nombres du degre 5 (seconde passe). Ici il est
eprouve la ou il n'a rien vu : aux degres p = 3, 7 et 9 du meme canal (2, 1), ou le saut croit comme m^(p/2) et ou T n'a pas
la meme valeur (2 pi / (T |delta|) tend vers p - 2 dans la limite continue : 1, 5, 7 au lieu de 3).
ATTENDU, ECRIT AVANT LE CALCUL : a chaque degre, pour des barrieres de 3 a 6 barreaux, |ln(V^2 T / Gamma)| <= 0.03, T etant
calcule sur les sauts seuls. Rien n'est attendu de la valeur de 2 pi / (T |delta|) a coupure finie (au degre 3 l'integrale
converge lentement). Le degre 5 est rejoue comme controle.
Cellule : w2 = 991/500 ; le couplage est fixe par la profondeur voulue m : racine(r_m r_(m+1)) = 1, r_m = 2 |t_m| / (m |delta|).
Usage : python3 -I -B pont_degres_machine1_v1.py <moteur> <sortie.json>"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import quad
from scipy.optimize import brentq
MOTEUR, SORTIE = sys.argv[1:3]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
W2 = F(991, 500); D = float(W2) - 2.0; AD = abs(D)
VARIANTES = [(a, c, L) for a in (1.0, 2.0, 4.0) for c in (6, 8, 10) for L in (16, 24)]; COUPURES = [(c, L) for c in (6, 8, 10) for L in (16, 20, 24)]

def sauts(p, g, Mmax):
    return [(g / p) * M.X_saut_reel(p, 2, 1, float(2 * m), float(m), W2) for m in range(Mmax + 1)]

def absorbeur(t, mb):
    v = []
    for (a, c, L) in VARIANTES:
        debut = mb + c; N = debut + L; H = np.zeros((N + 1, N + 1), dtype=complex); Wd = np.zeros(N + 1)
        for m in range(N + 1):
            H[m, m] = m * D
            if m > debut:
                Wd[m] = a * abs(t[m]) * ((m - debut) / float(L)) ** 2; H[m, m] += -1j * Wd[m]
            if m < N:
                H[m, m + 1] = t[m]; H[m + 1, m] = t[m]
        val, vec = np.linalg.eig(H); poids = np.abs(vec[0, :]) ** 2; nu = np.lexsort((val.real, -poids))[0]
        psi2 = np.abs(vec[:, nu]) ** 2; v.append(math.log(float(2.0 * (Wd @ psi2) / psi2.sum())))
    s = sorted(v); return 0.5 * (s[len(s) // 2 - 1] + s[len(s) // 2]), s[-1] - s[0]

def croisement(t, N):
    H0 = np.zeros((N + 1, N + 1))
    for m in range(N + 1):
        H0[m, m] = m * D
        if m < N:
            H0[m, m + 1] = t[m]; H0[m + 1, m] = t[m]
    ech = abs(t[N - 1])
    def lire(theta):
        H = H0.copy(); H[-1, -1] += ech * math.tan(theta); val, vec = np.linalg.eigh(H); return val, vec[0, :] ** 2
    rang = lambda th: int(np.argmax(lire(th)[1]))
    grille = np.linspace(-1.5, 1.5, 241); rangs = [rang(th) for th in grille]
    for k in range(len(grille) - 1):
        if rangs[k] == rangs[k + 1]:
            continue
        lo, hi, rlo = float(grille[k]), float(grille[k + 1]), rangs[k]
        for _ in range(200):
            mi = 0.5 * (lo + hi)
            if mi == lo or mi == hi:
                break
            lo, hi = (mi, hi) if rang(mi) == rlo else (lo, mi)
        val, p = lire(0.5 * (lo + hi)); i, j = sorted(int(x) for x in np.argsort(-p)[:2])
        if j != i + 1:
            continue
        return {"V": float(0.5 * (val[j] - val[i])), "E": float(0.5 * (val[i] + val[j])), "poids": [float(p[i]), float(p[j])], "norme": float(max(abs(val[0]), abs(val[-1])))}
    return None

def temps_classique(t, E, N):
    ms = list(range(len(t))); sp = CubicSpline(np.log(np.array(ms) + 0.5), np.log(np.abs(t))); tt = lambda m: math.exp(float(sp(math.log(m))))
    f = lambda m: 4.0 * tt(m) ** 2 - (E - m * D) ** 2
    grille = np.linspace(0.6, float(N), 4000); s = [f(m) for m in grille]; k = max(i for i in range(len(grille) - 1) if s[i] < 0 <= s[i + 1])
    m0 = brentq(f, grille[k], grille[k + 1], xtol=1e-14)
    I, err = quad(lambda u: 2.0 * u / math.sqrt(max(f(m0 + u * u), 1e-300)), 0.0, math.sqrt(N - m0), limit=400, epsabs=0, epsrel=1e-10)
    return 2.0 * I, m0

out = {"piece": "pont_degres_machine1_v1", "w2": "991/500", "attendu": "|ln(V^2 T / Gamma)| <= 0.03", "cas": []}
print("p  m  g            Gamma abs    etendue  N   V           ecart/bruit  2pi/(T|delta|)  ln(V^2 T/Gamma)  sortie")
for p in (3, 5, 7, 9):
    for m in (3, 4, 5, 6):
        t1 = sauts(p, 1.0, m + 2); r = lambda k: 2 * abs(t1[k]) / (k * AD); g = 1.0 / math.sqrt(r(m) * r(m + 1))
        t = sauts(p, g, m + 12 + 26); barr = [k for k in range(1, len(t)) if k * AD > 2 * abs(t[k])]; mb = max(k for k in barr if all(q in barr for q in range(1, k + 1)))
        lnG, et = absorbeur(t, mb); G = math.exp(lnG)
        for (c, L) in COUPURES:
            N = mb + c + L; x = croisement(t, N)
            if x is None:
                print("%d  %d  %.5e  %.3e    %.4f   %-3d aucun croisement trouve" % (p, mb, g, G, et, N)); continue
            Tc, m0 = temps_classique(t, x["E"], N); lr = math.log(x["V"] ** 2 * Tc / G); bruit = 2 * x["V"] / (2.2e-16 * x["norme"])
            out["cas"].append({"p": p, "m_voulu": m, "m_bord": mb, "g": g, "ln_G": lnG, "etendue": et, "N": N, "V": x["V"], "T": Tc, "D_T_sur_delta": 2 * math.pi / (Tc * AD),
                               "ln_V2T_sur_G": lr, "ecart_sur_bruit": bruit, "sortie": m0, "poids": x["poids"]})
            print("%d  %d  %.5e  %.3e    %.4f   %-3d %.4e  %.1e      %.3f           %+.4f          %.2f" % (p, mb, g, G, et, N, x["V"], bruit, 2 * math.pi / (Tc * AD), lr, m0), flush=True)
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
ok = [c for c in out["cas"] if c["ecart_sur_bruit"] > 1e3]
for p in (3, 5, 7, 9):
    X = [c["ln_V2T_sur_G"] for c in ok if c["p"] == p]
    if X:
        print("degre %d : %d croisements lisibles ; ln(V^2 T / Gamma) de %+.4f a %+.4f ; attendu tenu : %s" % (p, len(X), min(X), max(X), all(abs(x) <= 0.03 for x in X)))
