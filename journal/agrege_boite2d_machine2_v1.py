# -*- coding: ascii -*-
"""Agrege les journaux de la boite 2D nue (machine 2) comme les tableaux de la note de machine 1 : par echantillon et par tranche de cotes.
Usage : py -3.11 -P agrege_boite2d_machine2_v1.py <journal 3 barreaux> <journal 4> <journal 5>"""
import re
import sys
import numpy as np

def lire(chemin):
    R = []
    for l in open(chemin, encoding='ascii', errors='replace'):
        m = re.match(r'^(\d+)\s+(\d+)\s+(\d\.\d+)\s+([-+]\d\.\d+)\s+(\d+)\s+(\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\S+)', l)
        if m:
            R.append(dict(N=int(m.group(1)), w0=float(m.group(3)), n=int(m.group(5)), ny=int(m.group(6)), S1=float(m.group(7)), S0=float(m.group(8)), part=float(m.group(9)), rapp=float(m.group(10))))
        elif re.match(r'^\d+\s+\d+\s+\d\.\d+\s+[-+]\d\.\d+\s+0 niveau', l):
            m2 = re.match(r'^(\d+)', l); R.append(dict(N=int(m2.group(1)), w0=float('nan'), n=0, ny=0, S1=0.0, S0=0.0, part=0.0, rapp=float('nan')))
    return R

def ligne(nom, S):
    if not S:
        print('%-34s (rien)' % nom); return
    n = len(S); a = np.array([x['S1'] for x in S]); a0 = np.array([x['S0'] for x in S])
    print('%-34s %3d boites | Somme/largeur (avec 1/w0) %.3f +- %.3f  (sans %.3f) | niveaux/boite %.2f | participation %.2f | participation/niveaux %.2f' % (
        nom, n, a.mean(), a.std(ddof=1) / np.sqrt(n) if n > 1 else float('nan'), a0.mean(), np.mean([x['n'] for x in S]), np.mean([x['part'] for x in S]),
        np.mean([x['part'] for x in S]) / max(np.mean([x['n'] for x in S]), 1e-9)))

J = {3: lire(sys.argv[1]), 4: lire(sys.argv[2]), 5: lire(sys.argv[3])}
print('--- echantillons de la note de m1 (sa valeur entre parentheses : somme ; niveaux ; participation)')
ligne('3 barr., cotes 21-45  (1.017;2.20;1.80)', [x for x in J[3] if 21 <= x['N'] <= 45])
ligne('3 barr., cotes 46-64  (1.048;4.00;2.78)', [x for x in J[3] if 46 <= x['N'] <= 64])
ligne('4 barr., cotes 21-45  (1.020;1.96;1.58)', [x for x in J[4] if 21 <= x['N'] <= 45])
ligne('5 barr., cotes 21-45  (1.021;1.84;1.55)', [x for x in J[5] if 21 <= x['N'] <= 45])
print('--- 3 barreaux par tranche (sa note : somme ; niveaux ; participation)')
for (lo, hi, ref) in ((21, 27, '0.98;1.29;1.21'), (28, 34, '1.06;2.29;1.96'), (35, 41, '1.01;2.57;2.04'), (42, 48, '1.04;2.86;2.15'), (49, 56, '1.10;3.88;2.63'), (57, 64, '0.99;4.62;3.15')):
    ligne('  cotes %d-%d  (%s)' % (lo, hi, ref), [x for x in J[3] if lo <= x['N'] <= hi])
for nb in (3, 4, 5):
    S = [x for x in J[nb] if x['N'] <= 64]
    if len(S) > 3:
        sl = np.polyfit([x['N'] for x in S], [x['n'] for x in S], 1)[0]
        print('pente du nombre de niveaux selon le cote, %d barreaux, cotes %d-%d : %+.4f par quantum  (sa note, 3 barreaux 21-64 : +0.084)' % (nb, S[0]['N'], S[-1]['N'], sl))
S = J[3]
print('--- 3 barreaux, par boite : y_min / mediane la plus petite : %.2e ; boites sans niveau : %d' % (min(x['rapp'] for x in S if x['rapp'] == x['rapp']), sum(1 for x in S if x['n'] == 0)))
