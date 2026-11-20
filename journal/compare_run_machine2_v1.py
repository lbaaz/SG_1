# -*- coding: ascii -*-
"""Confronte mes feuilles a celles de machine 1 sur les SORTIES DU RUN (six cellules). Remplace pour le run reel compare_feuilles_machine2_v1.py, dont la cle de boite (m, cote) confondait MG3 et PG3
(ecrit pour une seule cellule de qualification) : ici la cle est (w2, m, g, cote). Machine 2, 2026-11-18. Les deux premieres sorties de ce defaut (60 boites sur 120) restent dans le journal du run.
Usage : py -3.11 -P compare_run_machine2_v1.py <dossier du run>"""
import json
import os
import sys

run = sys.argv[1]
sb = json.load(open(os.path.join(run, 'lecture_boites.json')))
mb = json.load(open(os.path.join(run, 'feuilles_machine2', 'lecture_boites.json')))
ses = {}
for c in sb['cellules']:
    for b in c['boites']:
        ses[(c['w2'], c['m'], c['g'], b['cote'])] = b
mes = {(b['cellule_cle'][0], b['cellule_cle'][1], b['cellule_cle'][2], b['cote']): b for b in mb['boites']}
print('boites : %d chez moi, %d chez lui, cles identiques : %s' % (len(mes), len(ses), sorted(mes) == sorted(ses)))
pire = {'S': 0.0, 'participation': 0.0, 'x': 0.0, 'y': 0.0}
cnt = {'n': 0, 'fiables': 0, 'valide': 0, 'lisible': 0, 'len_xy': 0}
ou = {}
for k in sorted(set(mes) & set(ses)):
    a, b = mes[k], ses[k]
    for nom, va, vb in (('S', a['S'], b['S']), ('participation', a['participation'], b['participation'])):
        d = abs(va - vb) if nom == 'S' else abs(va / vb - 1)
        if d > pire[nom]:
            pire[nom] = d
            ou[nom] = k
    cnt['n'] += (a['n'] != b['n'])
    cnt['fiables'] += (a['fiables'] != b['fiables'])
    cnt['valide'] += (a['valide'] != b['compte_valide'])
    cnt['lisible'] += (a['lisible'] != b['lisible'])
    if len(a['x']) != len(b['x']) or len(a['y']) != len(b['y']):
        cnt['len_xy'] += 1
    else:
        for u, v in zip(a['x'], b['x']):
            pire['x'] = max(pire['x'], abs(u - v))
        for u, v in zip(a['y'], b['y']):
            pire['y'] = max(pire['y'], abs(u - v))
print('boites : pire |S ma - S sa| %.3e (boite %s) ; pire ecart relatif de participation %.3e (boite %s) ; pire |x| %.3e ; pire |y| %.3e' % (pire['S'], ou.get('S'), pire['participation'], ou.get('participation'), pire['x'], pire['y']))
print('boites : desaccords n %d, fiables %d, valide %d, lisible %d, longueurs x/y %d' % (cnt['n'], cnt['fiables'], cnt['valide'], cnt['lisible'], cnt['len_xy']))

mv = json.load(open(os.path.join(run, 'feuilles_machine2', 'verdict.json')))
sv = json.load(open(os.path.join(run, 'verdict.json')))
print('--- verdict : ma structure ---', sorted(mv.keys()))
print(json.dumps({k: mv[k] for k in mv if k != 'cellules'}, ensure_ascii=False)[:1500])
