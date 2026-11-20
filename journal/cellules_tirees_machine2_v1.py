# -*- coding: ascii -*-
"""Les six cellules tirees (gel "pont", graine 456823) : leurs nombres, lus dans MES details d'eligibilite (eligibilite_pont_machine2_v1.py), avec la place de chacune parmi les 48 cellules (rang de |pas|
et de l'etendue du lisse, marge au seuil). Faits, aucun jugement. Machine 2, 2026-11-17.
Usage : py -3.11 -I cellules_tirees_machine2_v1.py <details.json> <w2 de MG, fraction> <w2 de PG, fraction>"""
import json
import sys
from fractions import Fraction as F

D = json.load(open(sys.argv[1])); W = {'MG': F(sys.argv[2]), 'PG': F(sys.argv[3])}
print('cellule  w2       |delta|  g            m_bord  e_bord  etendue_vide  etendue_lisse_max  pas_max  | rang de pas_max parmi les 48 (1 = le plus grand)  marge a 0.10 | rang de etendue_lisse_max  marge a 0.03')
rp = sorted(D, key=lambda d: -d['pas_max']); rl = sorted(D, key=lambda d: -d['etendue_lisse_max'])
for s in ('MG', 'PG'):
    for m in (3, 4, 5):
        d = [x for x in D if F(x['w2']) == W[s] and x['m'] == m][0]
        print('%s%d      %.3f    %.3f    %s  %d       %.4f  %.4f        %.4f             %.4f   | %-2d                                                 %+.4f       | %-2d                         %+.4f' % (
            s, m, float(W[s]), abs(float(W[s]) - 2.0), d['g'], d['m_bord'], d['e_bord'], d['etendue_vide'], d['etendue_lisse_max'], d['pas_max'], rp.index(d) + 1, 0.10 - d['pas_max'], rl.index(d) + 1, 0.03 - d['etendue_lisse_max']))
# un w2 est ELIGIBLE si ses TROIS cellules le sont (4.7) : on regroupe par w2 (mon premier passage lisait l'eligibilite de la cellule a 3 barreaux seule, ce qui est faux)
par_w2 = {}
for x in D:
    par_w2.setdefault(F(x['w2']), []).append(x['eligible'])
el = {s: sorted((abs(float(w) - 2.0) for w, e in par_w2.items() if all(e) and (w < 2) == (s == 'MG')), reverse=True) for s in ('MG', 'PG')}
print('|delta| des w2 ELIGIBLES (trois cellules eligibles) : MG %s ; PG %s' % (' '.join('%.3f' % v for v in el['MG']), ' '.join('%.3f' % v for v in el['PG'])))
print('le w2 tire de MG a le plus grand |delta| parmi les w2 eligibles de MG : %s ; celui de PG a le plus grand |delta| parmi les w2 eligibles de PG : %s' % (
    abs(float(W['MG']) - 2.0) == max(el['MG']), abs(float(W['PG']) - 2.0) == max(el['PG'])))
