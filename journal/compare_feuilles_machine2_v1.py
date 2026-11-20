# -*- coding: ascii -*-
"""Confronte mes feuilles (feuilles_pont_machine2_v1.py) a celles de machine 1, sur ses pieces de qualification : boites (S, n, participation, fiables, valide, lisible, par cote) et verdict
(L, L2, S, C, familles, Q2, Q3). Machine 2, 2026-11-17. Je n'ai lu les feuilles de machine 1 qu'APRES avoir rendu mes sorties ; ici je ne lis que leurs SORTIES.
Usage : py -3.11 -P compare_feuilles_machine2_v1.py <ma_lecture_boites.json> <sa_lecture_boites.json> <mon_verdict.json> <son_verdict.json>"""
import json
import sys

mb, sb, mv, sv = [json.load(open(p)) for p in sys.argv[1:5]]
# boites : les siennes sont rangees par cellule (m)
ses = {}
for c in sb['cellules']:
    for b in c['boites']:
        ses[(c['m'], b['cote'])] = b
mes = {(tuple(b['cellule_cle'])[1], b['cote']): b for b in mb['boites']}
print('boites : %d chez moi, %d chez lui (cles identiques : %s)' % (len(mes), len(ses), sorted(mes) == sorted(ses)))
pire = {'S': 0.0, 'participation': 0.0, 'n': 0, 'fiables': 0, 'valide': 0, 'lisible': 0}
for k in sorted(set(mes) & set(ses)):
    a, b = mes[k], ses[k]
    pire['S'] = max(pire['S'], abs(a['S'] - b['S'])); pire['participation'] = max(pire['participation'], abs(a['participation'] / b['participation'] - 1))
    pire['n'] += (a['n'] != b['n']); pire['fiables'] += (a['fiables'] != b['fiables']); pire['valide'] += (a['valide'] != b['compte_valide']); pire['lisible'] += (a['lisible'] != b['lisible'])
print('boites : plus grand |S ma - S sa| %.2e ; plus grand ecart relatif de participation %.2e ; desaccords : n %d, fiables %d, valide %d, lisible %d' % (
    pire['S'], pire['participation'], pire['n'], pire['fiables'], pire['valide'], pire['lisible']))
# verdict
for nom in sorted(sv['cellules']):
    a, b = mv['cellules'][nom], sv['cellules'][nom]
    L = (a['L']['tient'], b['L']['verdict']); L2 = (a['L2']['tient'], b['L2']['verdict'])
    S = (a['S']['tient'], b['S']['verdict']); C = (a['C']['tient'], b['C']['verdict'])
    print('%s : (L) moi %s / lui %s ; (L2) %s / %s ; (S) %s / %s ; (C) %s / %s' % (nom, L[0], L[1], L2[0], L2[1], S[0], S[1], C[0], C[1]))
    if b.get('S', {}).get('moyenne') is not None and a['S']['moyenne'] == a['S']['moyenne']:
        print('     S moyenne : moi %.12f lui %.12f ; erreur moi %s lui %s' % (a['S']['moyenne'], b['S']['moyenne'], a['S']['erreur'], b['S'].get('erreur')))
    q3 = b.get('Q3_somme_avec_la_densite_2d', {})
    if 'Q3_somme_densite_2D' in a['questions'] and q3:
        print('     Q3 : moi %.12f (%s boites) lui %.12f (%s boites)' % (a['questions']['Q3_somme_densite_2D'], 'S-lisibles', q3['moyenne'], q3['boites']))
for fam in ('L', 'L2', 'S', 'C'):
    print('famille (%s) : moi %s / lui %s' % (fam, mv['familles'][fam]['etat'], sv['familles'][fam]['verdict'] if 'verdict' in sv['familles'][fam] else sv['familles'][fam]))
print('Q2 groupes : moi', {k: (v['boites'], round(v['rapport'], 6)) for k, v in mv['questions'].items()}, '| lui', {k: v for k, v in sv.get('questions', {}).items()} if 'questions' in sv else [k for k in sv])
