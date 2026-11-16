# -*- coding: ascii -*-
"""Certification (d) : les nombres des sections 1, 3, 7.3, 7.4 et 9 (G-8) du gel partie 2, recalcules depuis MES predictions (predictions_machine2_vide_v1.json), pas depuis la table de m1.
Usage : py -3.11 -I controle_nombres_gel_machine2_v1.py"""
import json
import math

D = r'd:\devs\bocal\BOCAL4\certif_gel_vide_partie2_machine2'
P = json.load(open(D + r'\predictions_machine2_vide_v1.json'))['cellules']
M = json.load(open(r'd:\devs\bocal\BOCAL4\livraison_16h_gel_vide_partie2\ext\x_gel_vide_partie2\lot_machine1_2026-11-16_gel_vide_partie2_instrument_enonces_v1\table_cellules_gel_vide_v1.json'))
tol = {c['id']: c['tolerance'] for c in M['cellules']}
FM, FMAX = M['joues']['part_manquee_mediane'], M['joues']['part_manquee_par_cellule_max']
lis = [p for p in P if p['m'] <= 6]
pro = [p for p in P if p['m'] > 6]
print('SECTION 1 (16 cellules lisibles) :')
print('  |ln G3/G2| max : %.4f (gel 0.0026)  a %s' % (max(abs(p['ln_G3'] - p['ln_G2']) for p in lis), max(lis, key=lambda p: abs(p['ln_G3'] - p['ln_G2']))['id']))
print('  |ln G3/G1| max : %.4f (gel 0.0206)  a %s' % (max(abs(p['ln_G3'] - p['ln_G1']) for p in lis), max(lis, key=lambda p: abs(p['ln_G3'] - p['ln_G1']))['id']))
print('  |r3| max       : %.4f (gel 0.0291)  a %s' % (max(abs(p['r3']) for p in lis), max(lis, key=lambda p: abs(p['r3']))['id']))
for i in ('MG12', 'MG16'):
    p = [x for x in P if x['id'] == i][0]
    print('  %s : ln G3/G1 = %+.4f (gel -0.055 / -0.077)' % (i, p['ln_G3'] - p['ln_G1']))
print('SECTION 3 : N_max = r_c + 100 : ', all(p['N_max'] == p['r_c'] + 100 for p in P), '; e_bord des 12 profondes de %.3f a %.3f (gel 0.024 a 0.283)' % (min(p['e_bord'] for p in pro), max(p['e_bord'] for p in pro)))
print('SECTION 7.4 : T / etendue des 16 lisibles : de %.1f a %.1f (gel 2.9 a 15.1)' % (min(0.02 / p['etendue'] for p in lis), max(0.02 / p['etendue'] for p in lis)))
res_b = []
for p in lis:
    res_b.append((-FMAX / (1 - FMAX) * p['r3'], p['id']))
pire = max(res_b, key=lambda x: abs(x[0]))
print('  residu attendu (b), part manquee max : plus grand |.| aux lisibles = %.4f a %s (gel 0.0090 a MG6) ; 0.02 / ce nombre = %.2f (gel 2.2)' % (abs(pire[0]), pire[1], 0.02 / abs(pire[0])))
med = max((-FM / (1 - FM) * p['r3'] for p in lis), key=abs)
print('  residu attendu (b), part manquee mediane : plus grand |.| aux lisibles = %.4f (gel 0.0022)' % abs(med))
pro_pire = max(abs(-FMAX / (1 - FMAX) * p['r3']) for p in pro)
print('  residu attendu (b), pire, aux profondes : %.4f (gel 0.0312)' % pro_pire)
print('  T - etendue aux lisibles : de %.4f a %.4f (gel 0.0130 a 0.0187)' % (min(0.02 - p['etendue'] for p in lis), max(0.02 - p['etendue'] for p in lis)))
print('SECTION 9 G-8 : cellules LISIBLES dont le plateau predit G3* est sous 1.33e-12 :')
sous = [p for p in lis if math.exp(p['ln_G3']) < 1.33e-12]
print('  ', [p['id'] for p in sous], '; G3* de %.2e a %.2e (gel : MG6 MP5 MP6 PP5 PP6 PG5 PG6 ; 4.4e-15 a 1.3e-12)' % (min(math.exp(p['ln_G3']) for p in sous), max(math.exp(p['ln_G3']) for p in sous)))
print('  MG5 : G3* = %.4e (juste au-dessus du plancher, rapport %.4f)' % (math.exp([p for p in P if p['id'] == 'MG5'][0]['ln_G3']), math.exp([p for p in P if p['id'] == 'MG5'][0]['ln_G3']) / 1.33e-12))
print('SECTION 7.3 : signe de r3 par creneau, aux lisibles :')
for s in ('MG', 'MP', 'PP', 'PG'):
    print('   %s : %s' % (s, ' '.join('%s %+.4f' % (p['id'], p['r3']) for p in lis if p['id'].startswith(s))))
print('SECTION 5 : s de m1 contre l\'etendue : T - etendue = %.4f ... ; une cellule ne tient que si s <= (T - etendue) - |ln q|' % min(0.02 - p['etendue'] for p in lis))
print('  etalement du lecteur au plus tolere pour que PG6 puisse tenir avec |ln q| = 0.005 : s <= %.4f' % (0.02 - [p for p in P if p['id'] == 'PG6'][0]['etendue'] - 0.005))
