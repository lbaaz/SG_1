# -*- coding: ascii -*-
"""Compare mon PREMIER PASSAGE (Gamma = -2 Im(E) en double precision) et mon passage de REFERENCE (Gamma en precision etendue) : cellules ou l'etendue au vide change de plus de 5e-5, et si une
eligibilite change. Machine 2, 2026-11-17.
Usage : py -3.11 -I compare_passages_gamma_machine2_v1.py <log premier passage> <log reference> <table premier passage> <table reference>"""
import json
import re
import sys


def lire(f):
    d = {}
    for l in open(f, encoding='ascii'):
        m = re.match(r'^(MG|PG)\s+(\d\.\d{3})\s+(\d)\s+(\S+)\s+(\d+)\s+(\d\.\d+)\s+(\d\.\d+)\s+(\d\.\d+)\s+(\d\.\d+)', l)
        if m:
            d[(m.group(2), int(m.group(3)))] = float(m.group(7))
    return d


a, b = lire(sys.argv[1]), lire(sys.argv[2])
ta, tb = json.load(open(sys.argv[3])), json.load(open(sys.argv[4]))
chg = sorted(k for k in a if abs(a[k] - b[k]) > 5e-5)
print('premier passage : %d cellules lues ; reference : %d' % (len(a), len(b)))
print('cellules dont l etendue au vide change de plus de 5e-5 entre double precision et precision etendue : %d sur %d, toutes a %s barreaux' % (len(chg), len(a), '/'.join(sorted(set(str(k[1]) for k in chg)))))
for k in chg:
    print('   %s m%d : double %.4f -> precision etendue %.4f' % (k[0], k[1], a[k], b[k]))
print('plus grand ecart de l etendue au vide : %.4f' % max(abs(a[k] - b[k]) for k in a))
print('tables d eligibilite (section 5) identiques entre les deux passages : %s' % (ta == tb))
