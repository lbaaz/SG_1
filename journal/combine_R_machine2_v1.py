# -*- coding: ascii -*-
"""Combine les R des trois tranches (cotes ~200, ~300, ~400) lus dans les journaux de agrege_attendus_machine2_v1.py : moyenne ponderee par l'inverse du carre de l'ecart-type
d'un tirage Porter-Thomas aux memes n (c'est une incertitude APPROCHEE : elle suppose des parts Porter-Thomas). Machine 2, hors chaine.
Usage : py -3.11 -I combine_R_machine2_v1.py <journal tranche 200> <journal tranche 300> <journal tranche 400>"""
import math
import re
import sys

W = []
for f in sys.argv[1:4]:
    t = open(f, encoding='ascii').read()
    m = re.search(r'R observe = (\d+\.\d+)\s+\| Porter-Thomas aux memes n : R = (\d+\.\d+) \+- (\d+\.\d+)', t)
    e = re.search(r'exponentielle : R = (\d+\.\d+) \+- (\d+\.\d+)', t)
    c = re.search(r'cotes (\d+) a (\d+) : (\d+) boites', t)
    R, Rpt, s, Rex, sex = float(m.group(1)), float(m.group(2)), float(m.group(3)), float(e.group(1)), float(e.group(2))
    W.append((R, s, Rpt, Rex, sex)); print('tranche cotes %s-%s (%s boites) : R = %.3f ; Porter-Thomas %.3f +- %.3f -> ecart %+.2f sigma ; exponentielle %.3f +- %.3f -> ecart %+.2f sigma' % (
        c.group(1), c.group(2), c.group(3), R, Rpt, s, (R - Rpt) / s, Rex, sex, (R - Rex) / sex))
w = [1.0 / s ** 2 for (R, s, a, b, c) in W]; Rm = sum(wi * x[0] for wi, x in zip(w, W)) / sum(w); sm = 1.0 / math.sqrt(sum(w))
print('R combine (trois tranches, ponderation 1 / sigma_PT^2) = %.3f +- %.3f ; ecart a Porter-Thomas (1) : %+.2f sigma ; a l exponentielle (~0.70) : %+.2f sigma' % (Rm, sm, (Rm - 1.0) / sm, (Rm - 0.70) / sm))
