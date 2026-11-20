# -*- coding: ascii -*-
"""MARGES des conditions d'eligibilite (gel "pont", 4.6) sur les 48 cellules, d'apres MES details (eligibilite_pont_machine2_v1.py) : pour chaque condition, la valeur la plus defavorable, le seuil,
la cellule la plus proche du seuil, et si la condition ecarte au moins une cellule ("lie"). Machine 2, 2026-11-17.
Usage : py -3.11 -I marges_pont_machine2_v1.py <details.json>"""
import json
import sys
from fractions import Fraction as F

D = json.load(open(sys.argv[1]))
nom = lambda d: '%.3f m%d' % (float(F(d['w2'])), d['m'])
print('%d cellules ; eligibles : %d' % (len(D), sum(1 for d in D if d['eligible'])))
CONDS = [('(i) m_bord = m', None, None), ('(ii) e_bord < 0.7', 'e_bord', 0.7), ('(iii) etendue au vide <= 0.02', 'etendue_vide', 0.02), ('(iv) etendue du lisse <= 0.03', 'etendue_lisse_max', 0.03), ('(v) |pas| <= 0.10', 'pas_max', 0.10)]
for lab, cle, seuil in CONDS:
    if cle is None:
        ko = [d for d in D if d['m_bord'] != d['m']]
        print('%-34s ecarte %d cellule(s) ; m_bord = m partout : %s' % (lab, len(ko), len(ko) == 0)); continue
    v = sorted(D, key=lambda d: -d[cle]); pire = v[0]
    ko = [d for d in D if d[cle] >= seuil] if cle == 'e_bord' else [d for d in D if d[cle] > seuil]
    dedans = [d for d in D if d[cle] <= seuil]; plus_proche_dedans = max(dedans, key=lambda d: d[cle]); dehors = [d for d in D if d[cle] > seuil]
    plus_proche_dehors = min(dehors, key=lambda d: d[cle]) if dehors else None
    print('%-34s valeur max %.4f (%s) pour un seuil de %.2f : rapport seuil/max = %.2f ; ecarte %d cellule(s)%s' % (
        lab, pire[cle], nom(pire), seuil, seuil / pire[cle], len(ko),
        ('' if not dehors else ' ; la plus proche du seuil : dedans %s %.4f, dehors %s %.4f (marge %.4f et %.4f)' % (nom(plus_proche_dedans), plus_proche_dedans[cle], nom(plus_proche_dehors), plus_proche_dehors[cle], seuil - plus_proche_dedans[cle], plus_proche_dehors[cle] - seuil))))
v = [d for d in D if d['pas_max'] > 0.10]
print('cellules ecartees par (v), avec l\'ecart x qui porte le pas maximal :')
for d in sorted(v, key=lambda d: (float(F(d['w2'])), d['m'])):
    e = max(d['ecarts'], key=lambda e: abs(e['pas']))
    print('   %s : |pas| max %.4f a x = %g' % (nom(d), abs(e['pas']), e['x']))
w = {}
for d in D:
    w.setdefault(d['w2'], []).append(d['eligible'])
print('w2 ecartes : %s' % ' '.join('%.3f' % float(F(k)) for k, e in sorted(w.items(), key=lambda kv: float(F(kv[0]))) if not all(e)))
print('G3* (plateau au vide) : de %.2e a %.2e ; rho_3 lisse a 8 |delta| : de %.1e a %.1e' % (min(d['plateau'] for d in D), max(d['plateau'] for d in D), min(d['rho3_8'] for d in D), max(d['rho3_8'] for d in D)))
print('ecart relatif maximal de Gamma lu en double precision (-2 Im E) a la precision etendue : %.2e' % max(d['gamma_double_vs_hp_rel'] for d in D))
