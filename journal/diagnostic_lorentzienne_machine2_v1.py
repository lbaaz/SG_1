# -*- coding: ascii -*-
"""Diagnostic (machine 2, hors chaine) : la fonction de force du vide du laboratoire 1D est-elle une lorentzienne de largeur Gamma exacte ?
Compare le poids cumule |E - E_r.real| <= x Gamma aux predictions d'une lorentzienne de poids Z, pour L = 4096 (Gamma/D ~ 11).
Usage : py -3.11 -P diagnostic_lorentzienne_machine2_v1.py [L]"""
import math
import sys
import numpy as np
sys.argv = [sys.argv[0], 'calib'] + sys.argv[1:1]
SRC = open('lab1d_vide_couloir_machine2_v1.py', encoding='ascii').read().split("if MODE == 'calib'")[0]
executer = exec
executer(SRC)
L = int(sys.argv[2]) if len(sys.argv) > 2 else 4096
Er, G = gamma_exact()
d, o = chaine(L); E, w = force(d, o)
print('L = %d  Gamma = %.6e  E_r.real = %.6f  poids total = %.12f' % (L, G, Er.real, w.sum()))
c0 = Er.real
for x in (0.25, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0):
    m = np.abs(E - c0) <= x * G
    print('poids dans |E - E_r| <= %5.2f Gamma : %.5f   (lorentzienne pure de largeur Gamma : %.5f)' % (x, w[m].sum(), 2 / math.pi * math.atan(2 * x)))
Q = quartiles(E, w)
print('quartiles - E_r : %+.5f %+.5f %+.5f  (en Gamma : %+.4f %+.4f %+.4f)' % (Q[0] - c0, Q[1] - c0, Q[2] - c0, (Q[0] - c0) / G, (Q[1] - c0) / G, (Q[2] - c0) / G))
# fraction du poids a plus de 0.2 de E_r (hors resonance) : l'ailleurs
for r in (0.05, 0.2, 1.0):
    far = np.abs(E - c0) > r
    print('poids a |E - E_r| > %.2f : %.5f  | cote bas %.5f  cote haut %.5f' % (r, w[far].sum(), w[E < c0 - r].sum(), w[E > c0 + r].sum()))
