# -*- coding: ascii -*-
"""La chaine d'ordre 2 SANS boite : sa largeur est-elle independante de SON absorbeur ?
Balayage : force eta_c = |d| * ef, debut de l'absorbeur, longueur de la chaine. Etat lu des six points de M17.
Usage : python3 -I chaine_longue_plateau_machine1_v1.py <moteur_v17.py>"""
import sys, math, importlib.util
from fractions import Fraction as F
import numpy as np
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
P = M.P; C0, C1 = M.CANAL; W1 = float(M.W1)
PTS = [("39/20", F(39, 20), (7, 2), 2.1623273017950654e-10), ("197/100", F(197, 100), (7, 2), 1.2976139867476588e-10),
       ("99/50", F(99, 50), (7, 2), 8.442078568634348e-11), ("101/50", F(101, 50), (7, 2), 6.562453137549285e-11),
       ("203/100", F(203, 100), (7, 2), 9.007654704606157e-11), ("41/20", F(41, 20), (8, 2), 2.6613925716641374e-09)]
SAUTS = [(k, l) for k in range(-P, P + 1) for l in range(-P, P + 1)
         if 0 < abs(k) + abs(l) <= P and (k + l) % 2 == P % 2 and (k, l) != (C0, C1) and (k, l) != (-C0, -C1)]

def tables(n1, n2, w2, g, Mh):
    w = float(w2); d = C1 * w - C0 * W1; m_min = -min(n1 // C0, n2 // C1)
    def V(k, l, a, b):
        if a < 0 or b < 0 or a + k < 0 or b + l < 0:
            return 0.0
        return (g / P) * M.X_saut_reel(P, k, l, float(a), float(b), w2)
    t, S, U = {}, {}, {}
    for m in range(m_min, Mh + 1):
        a, b = n1 + C0 * m, n2 + C1 * m
        t[m] = V(C0, C1, a, b); S[m] = 0.0; U[m] = 0.0
        for (k, l) in SAUTS:
            v = V(k, l, a, b)
            if v == 0.0:
                continue
            ej = -W1 * k + w * l
            S[m] += v * v / (-ej)
            k2, l2 = 2 * C0 - k, 2 * C1 - l
            if abs(k2) + abs(l2) <= P and (k2, l2) != (C0, C1):
                U[m] += 0.5 * v * V(k2, l2, a + k, b + l) * (1.0 / (-ej) + 1.0 / (2.0 * d - ej))
    return d, m_min, t, S, U

def largeur(d, m_min, t, S, U, Mh, debut, eta_c, puissance=2):
    n = Mh - m_min + 1
    H = np.zeros((n, n), dtype=complex); Wd = np.zeros(n)
    for m in range(m_min, Mh + 1):
        i = m - m_min
        H[i, i] = m * d + (S[m] - S[0])
        if m > debut:
            Wd[i] = eta_c * (m - debut) ** puissance; H[i, i] += -1j * Wd[i]
        if m < Mh:
            H[i, i + 1] = t[m]; H[i + 1, i] = t[m]
        if m + 2 <= Mh:
            H[i, i + 2] = U[m]; H[i + 2, i] = U[m]
    val, vec = np.linalg.eig(H)
    poids = np.abs(vec[-m_min, :]) ** 2 / np.sum(np.abs(vec) ** 2, axis=0)
    nu = np.lexsort((val.real, -poids))[0]
    psi2 = np.abs(vec[:, nu]) ** 2
    return float(2.0 * (Wd @ psi2) / psi2.sum()), float(poids[nu])

for nom, w2, (n1, n2), G in PTS:
    g = float(M.g_du_point(w2))
    sites = M.barriere(float(n1), float(n2), w2, g, True)
    mb = sites[-1][0]
    Mmax = 400
    d, m_min, t, S, U = tables(n1, n2, w2, g, Mmax)
    print("=== %s etat %s g %.4e d %+.3f m_bord %d ; t_m : m=%d %.3f, m=%d %.3f, m=20 %.3f, m=40 %.3f, m=100 %.2f ; S(m)-S(0) : m=20 %.4f, m=40 %.3f" % (
        nom, (n1, n2), g, d, mb, mb, t[mb], mb + 4, t[mb + 4], t[20], t[40], t[100], S[20] - S[0], S[40] - S[0]))
    efs = [2.0 ** (-j) for j in range(0, 13)]
    print("   ef = 2^-j, j : " + " ".join("%7d" % j for j in range(0, 13)))
    for debut, Mh in ((mb + 4, 64), (mb + 4, 128), (mb + 4, 256), (mb + 4, 400), (mb + 1, 256), (mb + 8, 256), (mb + 16, 400)):
        vals = [largeur(d, m_min, t, S, U, Mh, debut, abs(d) * ef)[0] / G for ef in efs]
        print("   debut %2d Mh %3d : " % (debut, Mh) + " ".join("%7.4f" % v for v in vals))
