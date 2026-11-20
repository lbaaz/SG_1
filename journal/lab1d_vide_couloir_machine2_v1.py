# -*- coding: ascii -*-
"""LABORATOIRE 1D (machine 2, 2026-11-16, hors chaine, classe 3) : un vide, une barriere, puis un COULOIR UNIFORME de longueur L. Sert a valider, dans un cas ou la
reponse est connue, les outils que machine 1 applique a la 2D fermee : (1) Gamma exact SANS absorbeur (pole de resonance avec un couloir semi-infini) ; (2) la fonction de
force du vide dans la boite fermee : nombre effectif de niveaux, ecart interquartile (= largeur d'une lorentzienne), survie P(t) et son retour ; (3) le croisement evite
(demi-ecart V) quand on fait defiler la condition de bord ; (4) le passage Gamma < D (regime de Rabi : le vide bat) -> Gamma > D (le vide se desintegre).
Energie en unites du saut du couloir (t_L = 1). Aucune dependance au registre, aucun chemin en dur.
Usage : py -3.11 -P lab1d_vide_couloir_machine2_v1.py calib [B U t0 tb]        -> Gamma exact et E_r pour les parametres
        py -3.11 -P lab1d_vide_couloir_machine2_v1.py A [B U t0 tb]            -> experience A : un couloir, L variable
        py -3.11 -P lab1d_vide_couloir_machine2_v1.py C [B U t0 tb]            -> experience C : K couloirs de longueurs differentes, memes DOS totale"""
import math
import sys
import numpy as np
from scipy.linalg import eigh, eigh_tridiagonal

MODE = sys.argv[1] if len(sys.argv) > 1 else 'calib'
PAR = [float(x) for x in sys.argv[2:6]] if len(sys.argv) > 5 else [2, 3.0, 1.0, 1.0]
B, U, T0, TB = int(PAR[0]), PAR[1], PAR[2], PAR[3]
TC = 1.0


def gamma_exact(B=B, U=U, t0=T0, tb=TB, tc=TC):
    """Pole de resonance : x_0(E) = 0 avec la self-energie exacte du couloir semi-infini (retardee, continuee sous l'axe). Rend (E_r, Gamma = -2 Im E_r)."""
    e = [0.0] + [U] * B; h = [t0] + [tb] * (B - 1)

    def f(E):
        S = tc ** 2 * (E - 1j * np.sqrt(4.0 - E * E + 0j)) / 2.0
        x = E - e[B] - S
        for i in range(B - 1, -1, -1):
            x = E - e[i] - h[i] ** 2 / x
        return x
    E = 0.0 - 1e-4j
    for _ in range(100):
        d = 1e-7; fp = (f(E + d) - f(E - d)) / (2 * d); En = E - f(E) / fp
        if abs(En - E) < 1e-15:
            E = En; break
        E = En
    return E, -2.0 * E.imag


def chaine(L, u=0.0, B=B, U=U, t0=T0, tb=TB, tc=TC):
    d = np.array([0.0] + [U] * B + [0.0] * L); o = np.array([t0] + [tb] * (B - 1) + [tc] + [1.0] * (L - 1))
    d = d.copy(); d[-1] += u
    return d, o


def force(d, o):
    """Niveaux E_k et poids du vide w_k = psi_k(site 0)^2 de la chaine fermee."""
    w, v = eigh_tridiagonal(d, o)
    return w, v[0, :] ** 2


def quartiles(E, w):
    c = np.cumsum(w) - 0.5 * w; c = c / (np.sum(w))
    return [float(np.interp(q, c, E)) for q in (0.25, 0.5, 0.75)]


def survie(E, w, ts):
    A = np.array([np.sum(w * np.exp(-1j * E * t)) for t in ts]); return np.abs(A) ** 2


def croisement(L, Dnom, Ec=0.0, B=B, U=U, t0=T0, tb=TB):
    """Premier croisement evite du vide quand u = tb2 * tan(theta) defile sur le dernier site (comme dans la chaine de machine 1). Rend (V, poids des deux niveaux, ecart voisins)."""
    def lire(th):
        d, o = chaine(L, 1.0 * math.tan(th), B, U, t0, tb)
        w, v = eigh_tridiagonal(d, o, select='v', select_range=(Ec - 6 * Dnom, Ec + 6 * Dnom))
        return w, v[0, :] ** 2
    from scipy.optimize import minimize_scalar
    # a un croisement evite l'ENERGIE du niveau-vide est continue (ce sont les indices qui s'echangent) : on repere le CREUX du poids maximal du vide, puis on
    # minimise l'ecart entre les deux niveaux de plus grand poids.
    def deux(th):
        w, p = lire(th); o2 = np.argsort(-p)[:2]; i, j = sorted(int(x) for x in o2); return w, p, i, j

    def ecart(th):
        w, p, i, j = deux(th); return float(w[j] - w[i])
    gr = np.linspace(-1.5, 1.5, 241); pm = [float(np.max(lire(th)[1])) for th in gr]
    k = int(np.argmin(pm))
    if k in (0, len(gr) - 1):
        return 'creux au bord de la grille'
    r = minimize_scalar(ecart, bounds=(float(gr[k - 1]), float(gr[k + 1])), method='bounded', options={'xatol': 1e-13})
    w, p, i, j = deux(r.x)
    if j != i + 1:
        return 'les deux niveaux de plus grand poids ne sont pas adjacents'
    if i < 1 or j + 1 >= len(w):
        return 'voisins hors fenetre'
    return 0.5 * (w[j] - w[i]), (float(p[i]), float(p[j])), 0.5 * (w[j + 1] - w[i - 1]), float(0.5 * (w[i] + w[j]))


if MODE == 'calib':
    E, G = gamma_exact()
    print('B=%d U=%.3f t0=%.3f tb=%.3f : E_r = %.8f %+.8fi  Gamma = %.6e   L(Gamma = D) = 2 pi / Gamma = %.1f' % (B, U, T0, TB, E.real, E.imag, G, 2 * math.pi / G))
    raise SystemExit(0)

Er, G = gamma_exact()
print('PARAMETRES B=%d U=%.3f t0=%.3f tb=%.3f tc=%.3f | resonance exacte : E_r = %.8f %+.8fi ; Gamma = %.6e ; 1/Gamma = %.1f ; L(Gamma=D) = 2pi/Gamma = %.1f' % (B, U, T0, TB, TC, Er.real, Er.imag, G, 1 / G, 2 * math.pi / G))
if MODE == 'A':
    print('L      N     D=2pi/(L+1)  Gamma/D   n_eff   Gamma_Q(interquartile)/Gamma   mediane-E_r    P(t_f)   taux de survie ajuste/Gamma   (t_f)     | croisement : V    2piV^2/(D_nn Gamma)   V/sqrt(Gamma D/2pi)   poids(i,j)')
    for L in (8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096):
        d, o = chaine(L); E, w = force(d, o); N = len(d); D = 2 * math.pi / (L + 1)
        neff = 1.0 / float(np.sum(w ** 2)); q1, q2, q3 = quartiles(E, w)
        tf = min(0.4 * (L + 1), 1.5 / G); ts = np.linspace(0.0, tf, 400); P = survie(E, w, ts)
        sel = P > 1e-3; pente = np.polyfit(ts[sel], np.log(P[sel]), 1)[0] if sel.sum() > 5 else float('nan')
        cr = croisement(L, D, Er.real)
        if isinstance(cr, tuple):
            V, pw, Dnn, Ec = cr; crs = '%.4e   %.4f   %.4f   (%.3f, %.3f)' % (V, 2 * math.pi * V * V / (Dnn * G), V / math.sqrt(G * D / (2 * math.pi)), pw[0], pw[1])
        else:
            crs = 'pas de croisement a deux niveaux : %s' % cr
        print('%-5d %-5d %.4e   %8.4f  %7.3f  %8.4f                      %+.3e     %.4f   %8.4f                      (%.1f)  | %s' % (L, N, D, G / D, neff, (q3 - q1) / G, q2 - Er.real, float(P[-1]), -pente / G, tf, crs), flush=True)
if MODE == 'C':
    print('K couloirs de longueurs differentes (somme des L_c = %d), saut vide-couloir tc/sqrt(K) ; meme self-energie, donc MEME Gamma exact ; seule la DOS totale compte.' % 1024)
    print('K    N     somme L_c  Gamma/D_tot   n_eff   Gamma_Q/Gamma   P(t_f)   taux ajuste/Gamma  (t_f)')
    for K in (1, 2, 4, 8, 16, 32, 64):
        rng = np.random.default_rng(12345 + K)
        base = 1024 // K; Ls = [max(4, int(base * (0.6 + 0.8 * rng.random()))) for _ in range(K)]; s = sum(Ls); Ls = [max(4, int(round(l * 1024.0 / s))) for l in Ls]
        n = 1 + B + sum(Ls); H = np.zeros((n, n)); H[0, 0] = 0.0
        for i in range(1, B + 1):
            H[i, i] = U
        H[0, 1] = H[1, 0] = T0
        for i in range(1, B):
            H[i, i + 1] = H[i + 1, i] = TB
        pos = 1 + B
        for L in Ls:
            H[B, pos] = H[pos, B] = TC / math.sqrt(K)
            for j in range(L - 1):
                H[pos + j, pos + j + 1] = H[pos + j + 1, pos + j] = 1.0
            pos += L
        E, v = eigh(H); w = v[0, :] ** 2; Dtot = 2 * math.pi / (sum(Ls) / 1.0)
        neff = 1.0 / float(np.sum(w ** 2)); q1, q2, q3 = quartiles(E, w)
        tf = min(0.4 * 1025, 1.5 / G); ts = np.linspace(0.0, tf, 400); P = survie(E, w, ts); sel = P > 1e-3
        pente = np.polyfit(ts[sel], np.log(P[sel]), 1)[0] if sel.sum() > 5 else float('nan')
        print('%-4d %-5d %-9d  %8.4f   %7.3f  %8.4f        %.4f   %8.4f          (%.1f)' % (K, n, sum(Ls), G / Dtot, neff, (q3 - q1) / G, float(P[-1]), -pente / G, tf), flush=True)


def ldos_ouverte(E, B=B, U=U, t0=T0, tb=TB, tc=TC):
    """Densite locale exacte du site 0 pour le couloir SEMI-INFINI : rho(E) = -Im(1/x_0(E))/pi (self-energie retardee)."""
    e = [0.0] + [U] * B; h = [t0] + [tb] * (B - 1)
    S = tc ** 2 * (E - 1j * np.sqrt(4.0 - E * E + 0j)) / 2.0
    x = E - e[B] - S
    for i in range(B - 1, -1, -1):
        x = E - e[i] - h[i] ** 2 / x
    return float(-(1.0 / x).imag / math.pi)


if MODE == 'D':
    # Dispersion de la statistique REPONDEREE de machine 1 : Y = somme sur les niveaux k de la fenetre de y_k = w_k / rho_ouverte(E_k), divisee par la largeur de la fenetre.
    # Attendu : moyenne 1 (la regle de somme). On mesure l'ECART-TYPE selon le nombre n de niveaux dans la fenetre, pour trois spectres :
    #  (R) regulier : un couloir, condition de bord aleatoire ;  (P) aleatoire a poids reguliers : K couloirs de longueurs differentes, couplages egaux ;
    #  (PT) aleatoire a poids de Porter-Thomas : K couloirs de longueurs differentes, couplage de chaque couloir tire gaussien (carre moyen conserve).
    OM, DE = 0.40, 0.05; lo, hi = Er.real + DE, Er.real + DE + OM
    print('fenetre [E_r + %.2f, E_r + %.2f], largeur %.2f' % (DE, DE + OM, OM))
    print('spectre      K   n vise  realisations  niveaux/fenetre   Y moyen   Y ecart-type   S brut moyen   S brut ecart-type')
    rng = np.random.default_rng(777)
    from scipy.integrate import quad
    I_open = quad(ldos_ouverte, lo, hi, epsabs=0, epsrel=1e-10, limit=200)[0]

    def stat(E, w):
        m = (E > lo) & (E < hi); y = sum(float(wk) / ldos_ouverte(float(Ek)) for Ek, wk in zip(E[m], w[m])) / OM
        return y, float(w[m].sum() / I_open), int(m.sum())

    def multi(K, Ltot, gauss):
        base = max(3, Ltot // K); Ls = [max(3, int(base * (0.6 + 0.8 * rng.random()))) for _ in range(K)]; s = sum(Ls); Ls = [max(3, int(round(l * Ltot / s))) for l in Ls]
        n = 1 + B + sum(Ls); H = np.zeros((n, n)); H[0, 1] = H[1, 0] = T0
        for i in range(1, B + 1):
            H[i, i] = U
        for i in range(1, B):
            H[i, i + 1] = H[i + 1, i] = TB
        g = rng.standard_normal(K) if gauss else np.ones(K); pos = 1 + B
        for c, Lc in enumerate(Ls):
            H[B, pos] = H[pos, B] = TC * g[c] / math.sqrt(K)
            for j in range(Lc - 1):
                H[pos + j, pos + j + 1] = H[pos + j + 1, pos + j] = 1.0
            pos += Lc
        return eigh(H)

    for nbar in (2, 4, 8, 16):
        L = int(round(math.pi * 1.98 * nbar / OM)) - 1; Y, S, ns = [], [], []
        for r in range(300):
            d, o = chaine(L, u=float(rng.uniform(-4, 4))); E, w = force(d, o); y, s_, n_ = stat(E, w); Y.append(y); S.append(s_); ns.append(n_)
        print('regulier     1   %-6d  %-12d  %-15.2f   %.4f    %.4f        %.4f         %.4f' % (nbar, len(Y), np.mean(ns), np.mean(Y), np.std(Y), np.mean(S), np.std(S)), flush=True)
    for (K, nbar) in ((4, 4), (4, 8), (8, 8), (8, 16), (16, 16), (16, 32)):
        Ltot = int(round(math.pi * 1.98 * nbar / OM)) - 1
        for nom, gauss in (('alea poids reg', False), ('alea Porter-Th', True)):
            Y, S, ns = [], [], []
            for r in range(150):
                E, v = multi(K, Ltot, gauss); y, s_, n_ = stat(E, v[0, :] ** 2); Y.append(y); S.append(s_); ns.append(n_)
            print('%-13s %-3d %-6d  %-12d  %-15.2f   %.4f    %.4f        %.4f         %.4f' % (nom, K, nbar, len(Y), np.mean(ns), np.mean(Y), np.std(Y), np.mean(S), np.std(S)), flush=True)
