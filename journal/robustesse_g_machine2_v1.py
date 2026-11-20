# -*- coding: ascii -*-
"""Robustesse du couplage ECRIT (section 2 du gel "pont") aux lectures possibles de la formule g = kappa_m |w2 - 2| P / X(w2), "%.5e" : (A) |float(w2) - 2.0| en double precision (ma chaine) ; (B) float(|w2 - 2|)
calcule en fraction exacte ; (C) X(w2) lu avec w2 = Fraction ou avec w2 = float. Compte les cellules ou le texte du couplage ecrit (6 chiffres) change. Machine 2, 2026-11-17.
Usage : py -3.11 -P robustesse_g_machine2_v1.py <registre clone>"""
import importlib.util
import sys
from fractions import Fraction as F

REG = sys.argv[1].rstrip('/\\')
spec = importlib.util.spec_from_file_location("moteur", REG + "/scripts/m17_chaine_v17.py"); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
KAPPA = {3: 0.0262, 4: 0.0200, 5: 0.0159}
W2 = [F(k, 1000) for k in (1981, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 2011, 2012, 2013, 2014, 2015, 2016, 2018, 2019)]
diff_B = diff_C = n = 0; maxrel = 0.0
for w in W2:
    X = M.X_saut_reel(5, 2, 1, 0, 0, w); Xf = M.X_saut_reel(5, 2, 1, 0, 0, float(w))
    for m in (3, 4, 5):
        a = KAPPA[m] * abs(float(w) - 2.0) * 5 / X; b = KAPPA[m] * float(abs(w - 2)) * 5 / X; c = KAPPA[m] * abs(float(w) - 2.0) * 5 / Xf
        n += 1; diff_B += ('%.5e' % a) != ('%.5e' % b); diff_C += ('%.5e' % a) != ('%.5e' % c); maxrel = max(maxrel, abs(a / b - 1), abs(a / c - 1))
print('%d cellules ; couplage ecrit different entre |float(w2) - 2.0| et float(|w2 - 2|) : %d ; entre X(w2) en Fraction et en float : %d ; plus grand ecart relatif avant arrondi : %.2e' % (n, diff_B, diff_C, maxrel))
