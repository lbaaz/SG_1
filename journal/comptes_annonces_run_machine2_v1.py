# -*- coding: ascii -*-
"""COMPTES, SANS JUGEMENT, du run du gel "sommet" contre les ANNONCES de machine 1 (section 10 de sa piece 81a2febcfce49007) : je recompte, depuis verdict_sommet.json (sa feuille, jouee dans le run) et les fichiers de lecture, ce que chaque annonce comptait. Les annonces sont les siennes (L-8) ; je ne dis ni qu'elles tiennent ni qu'elles ne tiennent pas :
je donne le nombre lu, a cote de ce que l'annonce disait. Aucun nouveau calcul 2D. Les ecritures de la comparaison a la chaine (A-8, A-9) viennent du verdict de la feuille.
Usage : py -3.11 -I comptes_annonces_run_machine2_v1.py <dossier du run>"""
import json
import math
import os
import sys

RUN = sys.argv[1]
V = json.load(open(os.path.join(RUN, 'verdict_sommet.json')))
C = V['cellules']
print('A-1 instrument de l etage A : %s ; A-2 temoins positifs : %s (%d sur %d)' % (V['instrument'], V['temoins_positifs']['issue'], V['temoins_positifs']['tenus'], V['temoins_positifs']['sur']))
lues = [c for c in C if c['lu']]
print('A-3 temoin (jumeau) tenu : %d cellules sur 56' % sum(1 for c in C if c['temoin'] and c['temoin']['tient']))
print('A-4 cellules lues (qualifiees et temoin tenu) : %d sur 56 (annonce : 56 a 0.70, au moins 50 a 0.90)' % len(lues))
print('A-5 S1 : %s ; tenues %d, tombees %d, non jugeables %d, non lues %d' % (V['S1']['issue'], V['S1']['comptes']['TIENT'], V['S1']['comptes']['TOMBE'], V['S1']['comptes']['NON JUGEABLE'], V['S1']['comptes']['NON LUE']))
mx = max(abs(c['ln_q']) for c in lues)
print('A-6 plus grand |ln q| aux cellules lues : %.5f (annonce : sous 0.001) ; marge minimale T - b - |ln q| : %.5f' % (mx, min(c['tolerance'] - c['bande'] - abs(c['ln_q']) for c in lues)))
bar = [c for c in lues if c['numero_kappa'] in (1, 2)]
neg = [c for c in bar if c['ln_q'] < 0]
print('A-7 cellules de barriere (kappa 0.0363 et 0.0530) : %d ; ln q negatif a %d (annonce : au moins 12 sur 16) ; par kappa : 0.0363 -> %d sur 8, 0.0530 -> %d sur 8' % (
    len(bar), len(neg), sum(1 for c in bar if c['numero_kappa'] == 1 and c['ln_q'] < 0), sum(1 for c in bar if c['numero_kappa'] == 2 and c['ln_q'] < 0)))
print('    ln q aux barrieres : kappa 0.0363 : %s' % ' '.join('%+.5f' % c['ln_q'] for c in bar if c['numero_kappa'] == 1))
print('                         kappa 0.0530 : %s' % ' '.join('%+.5f' % c['ln_q'] for c in bar if c['numero_kappa'] == 2))
pm = V['consigne']['paires_miroirs']
ecarts = [abs(p['ln_rapport_lu'] - p['ln_rapport_chaine']) for p in pm]
print('A-8 sept paires miroirs : ecart du rapport lu au rapport de la chaine : %s ; a 0.0001 pres a %d paires sur %d (annonce : cinq au moins)' % (' '.join('%.5f' % e for e in ecarts), sum(1 for e in ecarts if e <= 1e-4), len(pm)))
la = V['consigne']['loi_d_echelle']
print('A-9 etalement de ln(Gamma_pl / |delta|) lu, par kappa : %s (annonce : sous 0.001 a chaque kappa) ; ceux de la chaine : %s' % (
    ' '.join('%.5f' % la[k]['etalement_lu'] for k in sorted(la)), ' '.join('%.5f' % la[k]['etalement_chaine'] for k in sorted(la))))
print('\nconsigne (sans jugement) : ln q negatif (lecteur au-dessus de la chaine) a %d cellules ; ln q du signe de delta a %d ; ordre 3 plus pres de la largeur lue que l ordre 1 a %d cellules sur 56' % (
    V['consigne']['ln_q_negatif'], V['consigne']['ln_q_du_signe_de_delta'], V['consigne']['ordre3_plus_pres_que_ordre1']))
par = {}
for c in lues:
    par.setdefault(c['kappa'], []).append(c['ln_q'])
print('ln q par kappa (min, max sur les 8 cellules) : ' + ' ; '.join('%s [%+.5f, %+.5f]' % (k, min(v), max(v)) for k, v in sorted(par.items())))
