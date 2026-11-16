# -*- coding: ascii -*-
"""MARGES D'ANCRAGE (gel bis 3.7) sous les absorbeurs longs du rejeu (i) de machine 2, point par point. HORS CHAINE. Lit
rejeu_absorbeurs_longs_machine2_v1.json ; rien n'est recalcule. Pour chaque point : la marge de la nuit bis (F1, G20 : recouvrement du premier
etat / recouvrement du second), puis, sur les onze configurations longues, la plus petite et la plus grande marge, la plus petite
identite (3.9) avec l'etat de M17, et l'ecart d'energie de l'etat d'ancrage a celui de M17 (en valeur absolue).
Usage : py -3.11 -P lecteur_creux_m2/marges_ancrage_rejeu_machine2_v1.py <rejeu.json>"""
import json
import sys

d = json.load(open(sys.argv[1]))
ordre = ['39_20', '197_100', '99_50', '101_50', '203_100', '41_20']
print('point     marge nuit bis | marges sous absorbeurs longs : min  max (config du min) | identite min | ecart E_re max a M17 | distance au sigma max')
for p in ordre:
    rs = [r for r in d['resultats'] if r['nature'] == 'pt' and r['nom'] == p]
    ref = rs[0]['ref_ancre']
    marges, ident, dE, dsig = [], [], 0.0, 0.0
    for r in rs:
        for c, x in r['configs'].items():
            a = x['ancre']
            marges.append((a['recouvrement_graine'] / a['recouvrement_second'], c))
            ident.append(x['identite_M17'])
            dE = max(dE, abs(a['E_re'] - ref['E_re']))
            dsig = max(dsig, a['dist_sigma'])
    marges.sort()
    print('%-8s  %.3f          | %.3f  %.3f (%s) | %.6f | %.2e | %.3f'
          % (p, ref['rec'] / ref['rec2'], marges[0][0], marges[-1][0], marges[0][1], min(ident), dE, dsig))
print('')
print('temoin H+ : marge d ancrage (vide), par trajectoire')
for r in d['resultats']:
    if r['nature'] == 'tp':
        for c, x in sorted(r['configs'].items()):
            a = x['ancre']
            print('  %s %-6s rec %.4f second %.4f rapport %.3f' % (r['nom'], c, a['recouvrement_graine'], a['recouvrement_second'],
                                                                  a['recouvrement_graine'] / a['recouvrement_second']))
