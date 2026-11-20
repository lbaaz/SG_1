# -*- coding: ascii -*-
"""Confronte MA lecture par partition (partition_independante_machine2_v1.py, ecrite du texte) a celle de la sonde de machine 1, niveau par niveau (appariement par energie), et dit ou le brut s'ecarte.
Usage : py -3.11 -P compare_partition_machine2_v1.py <ma sortie.json> <sa sortie.jsonl> <cote>"""
import json
import math
import sys

mine = json.load(open(sys.argv[1])); cote = int(sys.argv[3])
his = [json.loads(l) for l in open(sys.argv[2]) if l.strip()]
his = [b for b in his if b['cote'] == cote][0]
A = mine['lectures']['2']; B = mine['lectures']['5.5']
print('cote %d, %d niveaux chez moi (deux decalages : %d et %d), %d chez lui' % (cote, len(A), len(A), len(B), his['n']))
assert len(A) == len(B) == his['n']
d = dict(a=0.0, b=0.0, large=0.0)
print('  x        c2 (lui, lecture a)   ma partition (decalage 2)  rapport     son brut_a / partition   mon brut(2) / partition   mon brut(5.5) / partition')
for u, v, w in zip(A, B, his['niveaux']):
    assert abs(u['E'] - w['E']) < 1e-9 and abs(v['E'] - w['E']) < 1e-9
    d['a'] = max(d['a'], abs(u['carre_rc'] / w['c2_a'] - 1)); d['b'] = max(d['b'], abs(v['carre_rc'] / w['c2_b'] - 1)); d['large'] = max(d['large'], abs(u['carre_rc+6'] / w['c2_a_large'] - 1))
    print('  %.4f   %.3e            %.3e                  %.2e    %+.2e                %+.2e                  %+.2e' % (w['x'], w['c2_a'], u['carre_rc'], u['carre_rc'] / w['c2_a'] - 1, w['brut_a'] / w['c2_a'] - 1, u['brut'] / u['carre_rc'] - 1, v['brut'] / v['carre_rc'] - 1))
print('plus grand ecart relatif de ma partition a la sienne : lecture a %.2e ; lecture b (mon decalage 5.5 contre son 5.5) %.2e ; r_c+6 %.2e' % (d['a'], d['b'], d['large']))
