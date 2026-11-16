# -*- coding: ascii -*-
"""La chaine d'ordre 2 sans boite, etat lu des six points de M17 : valeur de plateau et etalement sous son absorbeur.
Plateau : debut de l'absorbeur a m_bord + 8, + 16, + 24 ; chaine de 400 sites ; ef = 1/8, 1/16, 1/32, 1/64 (eta_c = |d| ef).
Valeur retenue : debut m_bord + 16, ef 1/32. Reference du gel 41153158190cf7f1 : debut m_bord + b_M // 2, Mh = 4 (m_bord + b_M), ef 1/16.
Usage : python3 -I chaine_sans_boite_machine1_v1.py <moteur.py> <sortie.json>"""
import sys, json, math, importlib.util
from fractions import Fraction as F
import numpy as np
spec = importlib.util.spec_from_file_location("moteur", sys.argv[1])
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
P = M.P; C0, C1 = M.CANAL; W1 = float(M.W1)
PTS = [("39_20", F(39, 20), (7, 2)), ("197_100", F(197, 100), (7, 2)), ("99_50", F(99, 50), (7, 2)),
       ("101_50", F(101, 50), (7, 2)), ("203_100", F(203, 100), (7, 2)), ("41_20", F(41, 20), (8, 2))]
SAUTS = [(k, l) for k in range(-P, P + 1) for l in range(-P, P + 1)
         if 0 < abs(k) + abs(l) <= P and (k + l) % 2 == P % 2 and (k, l) != (C0, C1) and (k, l) != (-C0, -C1)]
def tables(n1, n2, w2, g, Mh):
    w = float(w2); d = C1 * w - C0 * W1; m_min = -min(n1 // C0, n2 // C1)
    def V(k, l, a, b):
        if a < 0 or b < 0 or a + k < 0 or b + l < 0: return 0.0
        return (g / P) * M.X_saut_reel(P, k, l, float(a), float(b), w2)
    t, S, U = {}, {}, {}
    for m in range(m_min, Mh + 1):
        a, b = n1 + C0 * m, n2 + C1 * m
        t[m] = V(C0, C1, a, b); S[m] = 0.0; U[m] = 0.0
        for (k, l) in SAUTS:
            v = V(k, l, a, b)
            if v == 0.0: continue
            ej = -W1 * k + w * l; S[m] += v * v / (-ej)
            k2, l2 = 2 * C0 - k, 2 * C1 - l
            if abs(k2) + abs(l2) <= P and (k2, l2) != (C0, C1):
                U[m] += 0.5 * v * V(k2, l2, a + k, b + l) * (1.0 / (-ej) + 1.0 / (2.0 * d - ej))
    return d, m_min, t, S, U
def largeur(d, m_min, t, S, U, Mh, debut, eta_c):
    n = Mh - m_min + 1; H = np.zeros((n, n), dtype=complex); Wd = np.zeros(n)
    for m in range(m_min, Mh + 1):
        i = m - m_min; H[i, i] = m * d + (S[m] - S[0])
        if m > debut:
            Wd[i] = eta_c * (m - debut) ** 2; H[i, i] += -1j * Wd[i]
        if m < Mh: H[i, i + 1] = t[m]; H[i + 1, i] = t[m]
        if m + 2 <= Mh: H[i, i + 2] = U[m]; H[i + 2, i] = U[m]
    val, vec = np.linalg.eig(H)
    poids = np.abs(vec[-m_min, :]) ** 2 / np.sum(np.abs(vec) ** 2, axis=0)
    nu = np.lexsort((val.real, -poids))[0]; psi2 = np.abs(vec[:, nu]) ** 2
    return float(2.0 * (Wd @ psi2) / psi2.sum())
out = {}
for nom, w2, (n1, n2) in PTS:
    g = float(M.g_du_point(w2)); sites = M.barriere(float(n1), float(n2), w2, g, True); mb = sites[-1][0]; bM = max(8, mb)
    d, m_min, t, S, U = tables(n1, n2, w2, g, 400)
    grille = {}
    for dd in (8, 16, 24):
        for j in (3, 4, 5, 6):
            grille["%d_%d" % (dd, j)] = largeur(d, m_min, t, S, U, 400, mb + dd, abs(d) * 2.0 ** (-j))
    v = list(grille.values())
    gel = largeur(d, m_min, t, S, U, (mb + bM) * 4, mb + bM // 2, abs(d) / 16.0)
    out[nom] = {"w2": "%d/%d" % (w2.numerator, w2.denominator), "g": g, "etat": [n1, n2], "m_bord": mb, "plateau": grille["16_5"],
                "etalement": max(v) / min(v) - 1.0, "grille": grille, "lecture_du_gel_98": gel}
    print("%-8s m_bord %d plateau %.6e etalement sur 12 reglages %.1e ; lecture du gel 98 / plateau : %.4f" % (out[nom]["w2"], mb, grille["16_5"], out[nom]["etalement"], gel / grille["16_5"]))
json.dump(out, open(sys.argv[2], "w"), indent=1, sort_keys=True)
