#!/usr/bin/env python3
# -*- coding: ascii -*-
"""BROUILLON DU v9 -- v8 avec delta = 1/(100 n^2) et la descente n, DEUX REMPLACEMENTS ASSERES.
machine 2, v1, 12/09/2026. Exploration (classe 3) : le brouillon n'est ancre sur aucun gel et n'est
pas un instrument ; il sert a jouer le selftest (qui liste les grandeurs a re-deriver) et le pre-vol
temoin (T-2 reel) a un delta candidat. Usage : construction_brouillon_v9_machine2_v1.py <n>.
"""
import hashlib, os, sys, unicodedata

n = int(sys.argv[1])
ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(ICI)
src = os.path.join(RAC, 'banc_qualification_machine1_v8.py')
raw = open(src, 'rb').read()
t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
assert hashlib.sha256(t).hexdigest()[:16] == '4d8882a2223a5c74', 'le v8 au poste n est pas le v8 certifie'
t = raw.decode('utf-8')
for a, b in (('DELTA = Fraction(1, 102400)', 'DELTA = Fraction(1, %d)' % (100 * n * n)),
             ('B_DESC, M_MARGE, J_DESC = 4, 2, 5', 'B_DESC, M_MARGE, J_DESC = %d, 1, 1' % (n * n))):
    assert t.count(a) == 1, a
    t = t.replace(a, b)
out = os.path.join(RAC, 'banc_v9brouillon_n%d.py' % n)
open(out, 'w', encoding='utf-8', newline='\n').write(t)
print('%s : delta = 1/%d, racine %d' % (os.path.basename(out), 100 * n * n, n))
