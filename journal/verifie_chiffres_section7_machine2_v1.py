# -*- coding: ascii -*-
"""Je recalcule, depuis MA table (detail_machine2_sommet_v1.json), les chiffres de la section 7 de la piece qui ne sont pas des nombres ecrits :
 - par kappa, sur les 80 w2 : l'intervalle de Phi = G3* / |w2 - 2| et l'etalement de ln Phi (a comparer a sa table : 6.68321e-06 a 6.68373e-06, 0.0001 ; ... ; 5.17263e-01 a 5.17455e-01, 0.0004) ;
 - le SIGNE de delta, a kappa et |w2 - 2| egaux (k = 5 a 20 sauf 10 : MP contre PP ; k = 25 a 49 : MG contre PG ; 40 paires x 7 kappa = 280) : ln[Phi(delta < 0) / Phi(delta > 0)], intervalle (sa piece : de -0.00007 a +0.00051) ;
 - le nombre de cellules a barriere vide (sa piece : 400), la plus grande boite N = r_c + 100 (122), l'intervalle de eta0 / g (3.8883 a 3.9027) et de eta0 / |w2 - 2| (1.385 a 38.17), le plus petit poids du site 0 (0.9013), les largeurs predites au-dessus du plus grand plateau qualifie (1.08861e-04) et au-dessous du plus petit au sommet (2.05518e-09).
Usage : py -3.11 -I verifie_chiffres_section7_machine2_v1.py <detail_machine2_sommet_v1.json>"""
import json
import math
import sys
from fractions import Fraction as F

det = json.load(open(sys.argv[1]))
KN = ['0.0363', '0.0530', '0.0800', '0.1300', '0.2000', '0.4000', '1.0000']
print('Phi = G3* / |w2 - 2| par kappa (80 w2) :')
for kn in KN:
    phis = []
    for cle, r in det.items():
        d = float(abs(F(r['w2']) - 2))
        c = [x for x in r['cellules'] if x['kappa'] == kn][0]
        phis.append(c['G3_plateau'] / d)
    print('  kappa %s  Phi %.5e a %.5e  etalement de ln Phi %.4f' % (kn, min(phis), max(phis), math.log(max(phis) / min(phis))))
paires = []
for k in list(range(5, 21)):
    if k != 10:
        paires.append(('MP|%d' % k, 'PP|%d' % k))
for k in range(25, 50):
    paires.append(('MG|%d' % k, 'PG|%d' % k))
v = []
for a, b in paires:
    for kn in KN:
        pa = [x for x in det[a]['cellules'] if x['kappa'] == kn][0]['G3_plateau']
        pb = [x for x in det[b]['cellules'] if x['kappa'] == kn][0]['G3_plateau']
        da, db = float(abs(F(det[a]['w2']) - 2)), float(abs(F(det[b]['w2']) - 2))
        assert da == db
        v.append(math.log((pa / da) / (pb / db)))
print('\nsigne de delta, a kappa et |w2 - 2| egaux : %d paires ; ln[Phi(delta < 0) / Phi(delta > 0)] de %+.5f a %+.5f' % (len(v), min(v), max(v)))
cs = [c for r in det.values() for c in r['cellules']]
print('\ncellules a barriere vide : %d ; plus grande boite N = r_c + 100 : %d ; eta0 / g de %.4f a %.4f ; eta0 / |w2 - 2| de %.3f a %.2f ; plus petit poids du site 0 : %.4f' % (
    sum(1 for c in cs if c['barriere_vide']), max(c['r_c'] for c in cs) + 100, min(c['eta0_sur_g'] for c in cs), max(c['eta0_sur_g'] for c in cs), min(c['eta0_sur_delta'] for c in cs), max(c['eta0_sur_delta'] for c in cs), min(c['poids_site0_min'] for c in cs)))
QD, Q2B = 1.08861e-04, 2.05518e-09
hauts = [c['G3_plateau'] for c in cs if c['G3_plateau'] > QD]
bas = [c['G3_plateau'] for c in cs if c['G3_plateau'] < Q2B]
print('largeur predite au-dessus du plus grand plateau qualifie (Q-d, 1.08861e-04) : %d cellules, jusqu a %.2f fois ; au-dessous du plus petit au sommet (Q2-b, 2.05518e-09) : %d cellules, jusqu a %.3f fois' % (len(hauts), max(hauts) / QD, len(bas), min(bas) / Q2B))
print('couplages ecrits : de %.5e a %.5e' % (min(float(c['g']) for c in cs), max(float(c['g']) for c in cs)))
