# -*- coding: ascii -*-
"""PLATEAU DU LECTEUR AUX ETATS DE BP -- machine 2, 2026-11-16. EXTRA DESCRIPTIF, hors verdict, ne rejuge rien (le gel ne se rejoue pas sous d'autres seuils apres lecture).
Repond a la question M-2 de machine 1 ('cette lecture est-elle trop favorable ou trop severe ?') par ce que le lecteur dit LUI-MEME de l'incertitude de la reference a BP : pour chaque etat juge de BP,
la marge a la tolerance (T - |ln q3|), l'etalement du plateau A que le lecteur publie, et l'ecart de la largeur de plateau B a A. Lit verdict_ordre3.json et verdict_ter.json du run, rien d'autre.
Usage : py -3.11 -P plateau_bp_machine2_v1.py <run_gel_loi_ordre3>"""
import json
import math
import os
import statistics
import sys

R = sys.argv[1]
V3 = json.load(open(os.path.join(R, 'verdict_ordre3.json')))
VT = json.load(open(os.path.join(R, 'verdict_ter.json')))
C = {c['id']: c for c in V3['cellules']}
print('PLATEAU DU LECTEUR AUX ETATS JUGES DE BP (domaine d\'abord) : marge a la tolerance, etalement du plateau A, ecart ln de la largeur du plateau B a la largeur A')
tout = []
for cid in ('BP', 'BN'):
    lect = {e['rang']: e for e in VT['points'][cid]['etats']}
    for e in sorted((x for x in C[cid]['etats'] if x['exclu'] is None), key=lambda x: (not x['dans_le_domaine'], x['rang'])):
        p = lect[e['rang']]['plateaux']
        A, B = p['A'], p.get('B', {})
        ecart = math.log(B['Gamma_pl'] / A['Gamma_pl']) if 'Gamma_pl' in B else float('nan')
        print('  %s rang %2d %-7s |ln q3| %.6f  marge %+.6f  etalement A %.6f  ecart ln B/A %+.2e' % (cid, e['rang'], 'DOMAINE' if e['dans_le_domaine'] else 'hors', abs(e['ln_q3']), e['tolerance'] - abs(e['ln_q3']), A['etalement'], ecart))
        tout.append((cid, e['rang'], e['dans_le_domaine'], e['tolerance'] - abs(e['ln_q3']), A['etalement']))
bp = sorted(((m, r, et) for c, r, d, m, et in tout if c == 'BP' and d))
print('BP, etats du domaine, marges croissantes : %s' % ', '.join('rang %d %+.4f' % (r, m) for m, r, _ in bp))
rang3 = [x for x in tout if x[0] == 'BP' and x[1] == 3][0]
print('BP rang 3 : marge %+.6f ; etalement du plateau A %.6f, soit %.1f fois la marge' % (rang3[3], rang3[4], rang3[4] / rang3[3]))
et_all = [A['etalement'] for pid, p in VT['points'].items() for e in p['etats'] for A in [e['plateaux']['A']] if 'etalement' in A]
print('pour l\'echelle, etalement du plateau A sur les %d etats lus : mediane %.6f, plus grand %.6f' % (len(et_all), statistics.median(et_all), max(et_all)))
