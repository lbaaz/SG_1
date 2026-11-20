# -*- coding: ascii -*-
"""Confronte mes feuilles de DENSITE et mon VERDICT a ceux de machine 1 sur les sorties du run (six cellules). Complete compare_run_machine2_v1.py (boites). Machine 2, 2026-11-18.
Je ne compare que les nombres que les deux feuilles portent sous le meme sens (ln R3, ln R2, ln rho 2D, lisible, w0) et les verdicts par cellule et par famille (L, L2, S, C).
Usage : py -3.11 -P compare_densite_verdict_run_machine2_v1.py <dossier du run>"""
import json
import os
import sys

run = sys.argv[1]
CELLULES = ['MG3', 'MG4', 'MG5', 'PG3', 'PG4', 'PG5']
pire = {'ln_R3': 0.0, 'ln_R2': 0.0, 'ln_rho_2D': 0.0, 'w0': 0.0, 'ln_R3_max_abs': 0.0}
desacc = 0
nb = 0
for c in CELLULES:
    sa = json.load(open(os.path.join(run, 'lecture_densite_2d_%s.json' % c)))
    ma = json.load(open(os.path.join(run, 'feuilles_machine2', 'lecture_densite_%s.json' % c)))
    assert sa['X'] == ma['X'], c
    assert len(sa['par_x']) == len(ma['par_x']) == len(sa['X']), c
    for a, b in zip(sa['par_x'], ma['par_x']):
        nb += 1
        pire['ln_R3'] = max(pire['ln_R3'], abs(a['ln_R3'] - b['ln_R3']))
        pire['ln_R2'] = max(pire['ln_R2'], abs(a['ln_R2'] - b['ln_R2']))
        pire['ln_rho_2D'] = max(pire['ln_rho_2D'], abs(a['ln_rho_2d'] - b['ln_rho_2D']))
        desacc += (a['lisible'] != b['lisible'])
    pire['w0'] = max(pire['w0'], abs(sa['w0'] - ma['w0']))
    pire['ln_R3_max_abs'] = max(pire['ln_R3_max_abs'], abs(sa['ln_R3_max_abs'] - ma['ln_R3_max_abs']))
    print('%s : ecarts lisibles %d (lui) %d (moi) ; plus grand |ln R3| %.6f (lui) %.6f (moi)' % (c, sa['ecarts_lisibles'], ma['ecarts_lisibles'], sa['ln_R3_max_abs'], ma['ln_R3_max_abs']))
print('densite : %d ecarts compares ; pire |d ln R3| %.2e ; pire |d ln R2| %.2e ; pire |d ln rho 2D| %.2e ; pire |d w0| %.2e ; pire |d plus grand ln R3| %.2e ; desaccords sur lisible : %d'
      % (nb, pire['ln_R3'], pire['ln_R2'], pire['ln_rho_2D'], pire['w0'], pire['ln_R3_max_abs'], desacc))

sv = json.load(open(os.path.join(run, 'verdict.json')))
mv = json.load(open(os.path.join(run, 'feuilles_machine2', 'verdict.json')))
dis = 0
pire_S = 0.0
pire_c = 0.0
for c in CELLULES:
    for f in ('L', 'L2', 'S', 'C'):
        a = sv['cellules'][c][f]['verdict'] == 'TIENT'
        b = mv['cellules'][c][f]['tient'] is True
        dis += (a != b)
        if not a:
            pass
    pire_S = max(pire_S, abs(sv['cellules'][c]['S']['moyenne'] - mv['cellules'][c]['S']['moyenne']))
print('verdict par cellule : %d jugements (6 cellules x 4 familles) compares, desaccords %d ; pire |d S moyenne| %.2e' % (24, dis, pire_S))
for f in ('L', 'L2', 'S', 'C'):
    a, b = sv['familles'][f], mv['familles'][f]
    print('famille (%s) : lui %s %s ; moi %s %s' % (f, a['verdict'], a['tombees'], b['etat'], b['tombees']))
print('Q1 : lui %.4f +- %.4f (%d boites) ; Q2 UN : lui %.3f, moi %.3f ; Q2 DEUX : lui %.3f, moi %.3f' % (sv['questions']['Q1']['moyenne'], sv['questions']['Q1']['erreur'], sv['questions']['Q1']['boites'],
      sv['questions']['Q2_UN']['rapport'], mv['questions']['Q2_groupe_UN']['rapport'], sv['questions']['Q2_DEUX']['rapport'], mv['questions']['Q2_groupe_DEUX']['rapport']))
print('repetition (son verdict) : %s' % sv['repetition'])
