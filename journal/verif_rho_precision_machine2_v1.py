# -*- coding: ascii -*-
"""PRECISION DE LA DENSITE rho (gel "pont", 4.5) : sur quelques cellules a 5 barreaux (les plus faibles Gamma et rho), aux ecarts les plus defavorables (x = 0.05 et x = 8), pour les 18 variantes
de l'ordre 3, compare trois lectures de rho = -(1/pi) Im[(E - H)^-1]_00 : (D) resolution directe en double precision (celle de ma chaine) ; (F) le flux (1/pi) somme_m W_m |y_m|^2, y = (E - H)^-1 e_0
(celle de machine 1) ; (P) resolution en precision etendue (40 chiffres) de la MEME matrice a la MEME energie. Machine 2, hors chaine, 1D seule.
Usage : py -3.11 -P verif_rho_precision_machine2_v1.py <registre clone>"""
import importlib.util
import math
import sys
from fractions import Fraction as F
import numpy as np
import mpmath as mp

executer = exec
REG = sys.argv[1].rstrip('/\\')
spec = importlib.util.spec_from_file_location("moteur", REG + "/scripts/m17_chaine_v17.py"); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
for bloc in ("chaine_ordre2_bloc_machine1_v1.py", "ordre3_bloc_machine1_v1.py", "chaine_adaptee_bloc_machine1_v1.py"):
    p = REG + "/scripts/" + bloc; executer(compile(open(p, encoding="ascii").read(), p, "exec"))
KAPPA = {3: 0.0262, 4: 0.0200, 5: 0.0159}; VARIANTES = [(a, c, L) for a in (1.0, 2.0, 4.0) for c in (6, 8, 10) for L in (16, 24)]


def matrice(tb, t3, a, c, L):
    d, m_min, m_bord = tb["d"], tb["m_min"], tb["m2_bord"]; debut = m_bord + c; Mh = debut + L; n = Mh - m_min + 1
    H = np.zeros((n, n), dtype=complex); W = np.zeros(n)
    for m in range(m_min, Mh + 1):
        i = m - m_min; H[i, i] = m * d + (tb["S"][m] - tb["S"][0])
        if m > debut:
            W[i] = a * abs(tb["t"][m]) * ((m - debut) / float(L)) ** 2; H[i, i] += -1j * W[i]
        if m + 1 <= Mh:
            x = tb["t"][m] + t3["T3"][m]; H[i, i + 1] = x; H[i + 1, i] = x
        if m + 2 <= Mh:
            H[i, i + 2] = tb["U"][m]; H[i + 2, i] = tb["U"][m]
        if m + 3 <= Mh:
            H[i, i + 3] = t3["W3"][m]; H[i + 3, i] = t3["W3"][m]
        if m + 5 <= Mh:
            H[i, i + 5] = t3["W5"][m]; H[i + 5, i] = t3["W5"][m]
    return H, W, -m_min


mp.mp.dps = 40
pire = {'F': 0.0, 'D': 0.0}; n = 0
print('cellule          x     variante      rho (precision etendue)   erreur relative : directe double (D)   flux (F)')
for w2 in (F(1981, 1000), F(1989, 1000), F(2011, 1000), F(2019, 1000)):
    m = 5; X = M.X_saut_reel(5, 2, 1, 0, 0, w2); g = float('%.5e' % (KAPPA[m] * abs(float(w2) - 2.0) * 5 / X)); delta = float(w2) - 2.0
    sites = M.barriere(0, 0, w2, g, True); tb = tables_ordre2(0, 0, w2, g, sites); t3 = tables_ordre3(0, 0, w2, g, tb)
    for (a, c, L) in VARIANTES:
        H, W, i0 = matrice(tb, t3, a, c, L); val, vec = np.linalg.eig(H); poids = np.abs(vec[i0, :]) ** 2 / np.sum(np.abs(vec) ** 2, axis=0); k = int(np.lexsort((val.real, -poids))[0]); Ev = val[k].real
        for x in (0.05, 8.0):
            E = Ev - x * delta
            y = np.linalg.solve(E * np.eye(len(H)) - H, np.eye(len(H))[:, i0]); rD = -(1.0 / math.pi) * y[i0].imag; rF = (1.0 / math.pi) * float(np.sum(W * np.abs(y) ** 2))
            A = mp.matrix(len(H), len(H))
            for i in range(len(H)):
                for j in range(len(H)):
                    if H[i, j] != 0:
                        A[i, j] = -mp.mpc(float(H[i, j].real), float(H[i, j].imag))
                A[i, i] += mp.mpf(float(E))
            b = mp.matrix(len(H), 1); b[i0] = 1
            z = mp.lu_solve(A, b); rP = -(z[i0].imag) / mp.pi
            eD = abs((mp.mpf(rD) - rP) / rP); eF = abs((mp.mpf(rF) - rP) / rP); pire['D'] = max(pire['D'], float(eD)); pire['F'] = max(pire['F'], float(eF)); n += 1
            if (a, c, L) in ((1.0, 6, 16), (4.0, 10, 24)):
                print('%-9s m=%d   %-5s %-12s %.6e                  %.2e                         %.2e' % ('%.3f' % float(w2), m, x, str((a, c, L)), float(rP), float(eD), float(eF)))
print('%d lectures comparees ; plus grande erreur relative : directe en double precision %.2e ; flux %.2e' % (n, pire['D'], pire['F']))
