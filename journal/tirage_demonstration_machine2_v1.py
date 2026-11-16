# -*- coding: ascii -*-
"""Point (d) de la certification du gel 'loi, ordre 3', premiere partie : MON tirage (tirage_gel_loi_machine2_v1.py) sur la graine de demonstration "DEMONSTRATION" (qui n'est pas une suite de chiffres et ne
peut donc pas etre la graine) rend-il les memes empreintes, numeros et w2 que la section 3 du gel et que le journal d'autotest de machine 1 ? stdlib seule ; aucune graine de l'operateur.
Usage : py -3.11 -I tirage_demonstration_machine2_v1.py <tirage_gel_loi_machine2_v1.py> <tirage_machine1_v1_autotest.log>"""
import hashlib
import importlib.util
import re
import sys
from fractions import Fraction as F

TIRAGE, LOG1 = sys.argv[1:3]
spec = importlib.util.spec_from_file_location('tirage', TIRAGE)
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)
att = {}
for l in open(LOG1, encoding='utf-8').read().split('\n'):
    m = re.match(r'sha256\("DEMONSTRATION\|(\w+)\|(\d)"\) = ([0-9a-f]{16})\.\.\. ; modulo\s+(\d+) =\s+(\d+) -> w2 = (\d\.\d{3})$', l)
    if m:
        att[(m.group(1), int(m.group(2)))] = (m.group(3), int(m.group(4)), int(m.group(5)), m.group(6))
print('lignes lues dans le journal d autotest de machine 1 : %d (attendu 8)' % len(att))
ok = len(att) == 8
for (s, r), (h16, n, num, w) in sorted(att.items(), key=lambda x: (T.ORDRE.index(x[0][0]), x[0][1])):
    hh = hashlib.sha256(('%s|%s|%d' % ('DEMONSTRATION', s, r)).encode('ascii')).hexdigest()
    L = T.liste(s)
    mon_num = int(hh, 16) % len(L)
    mon_w = T.tire('DEMONSTRATION', s, r)
    bon = hh[:16] == h16 and len(L) == n and mon_num == num and '%.3f' % float(mon_w) == w and mon_w == F(w)
    ok = ok and bon
    print('  %-2s rang %d : mon sha256 %s... ; modulo %2d = %2d -> w2 = %.3f ; machine 1 : %s... ; modulo %2d = %2d -> %s : %s' % (s, r, hh[:16], len(L), mon_num, float(mon_w), h16, n, num, w, 'IDENTIQUE' if bon else 'DIFFERENT'))
print('exemple de la section 3 du gel : sha256("DEMONSTRATION|N|0") = 4b2a1d038c89c813... ; modulo 9 = 4 -> w2 = 1.935 : %s' % (
    'RETROUVE' if hashlib.sha256(b'DEMONSTRATION|N|0').hexdigest().startswith('4b2a1d038c89c813') and T.tire('DEMONSTRATION', 'N', 0) == F(1935, 1000) else 'NON RETROUVE'))
print('TIRAGE SUR LA GRAINE DE DEMONSTRATION : %s' % ('TIENT, les huit lignes sont identiques' if ok else 'NE TIENT PAS'))
