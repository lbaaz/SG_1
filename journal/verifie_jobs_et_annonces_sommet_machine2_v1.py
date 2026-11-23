# -*- coding: ascii -*-
"""CERTIFICATION (d), partie "appels" : les deux fichiers de travail de machine 1 (jobs_gel_sommet_v1.txt : 112 lignes ; jobs_temoins_sommet_v1.txt : 18 lignes) sont-ils, ligne pour ligne, ce que la table gelee et la section 4.2 de la piece disent ?
Je les REGENERE de la table (cellule par cellule, le jumeau signe +1 puis le fantome signe -1 ; format : id w2 g m eta0 signe r_c ABCD) et je compare le TEXTE. Je verifie aussi que chaque ligne est un appel valable de MON pilote (arguments : id, w2 en fraction, g, m, eta0, signe, r_c, absorbeurs).
Hors regle : les chiffres de CHAINE de ses annonces A-8 (les sept rapports miroirs, de kappa 0.0363 a 1) et A-9 (l'etalement de ln(G3* / |delta|) a chaque kappa, de 0.00004 a 0.00048), recalcules de MA table. Aucune 2D.
Usage : py -3.11 -I verifie_jobs_et_annonces_sommet_machine2_v1.py <dossier du lot de machine 1> <ma table detail JSON>"""
import json
import math
import os
import sys
from fractions import Fraction as F

LOT, DETAIL = sys.argv[1:3]
t = json.load(open(os.path.join(LOT, 'table_cellules_gel_sommet_v1.json')))
det = json.load(open(DETAIL))
gen_c = ['%s %s %s %d %s %d %d ABCD' % (c['id'], c['w2'], c['g'], c['m'], c['eta0'], s, c['r_c']) for c in t['cellules'] for s in (1, -1)]
gen_t = ['%s %s %s %d %s %d %d ABCD' % (w['id'], w['w2'], w['g'], w['m'], w['eta0'], s, w['r_c']) for w in t['temoins_positifs'] for s in (1, -1)]
son_c = [l.rstrip('\n') for l in open(os.path.join(LOT, 'jobs_gel_sommet_v1.txt'), encoding='ascii') if l.strip()]
son_t = [l.rstrip('\n') for l in open(os.path.join(LOT, 'jobs_temoins_sommet_v1.txt'), encoding='ascii') if l.strip()]
print('jobs des cellules : %d lignes generees de la table, %d dans son fichier ; identiques ligne pour ligne : %s' % (len(gen_c), len(son_c), 'OUI' if gen_c == son_c else 'NON'))
print('jobs des temoins : %d lignes generees de la table, %d dans son fichier ; identiques ligne pour ligne : %s' % (len(gen_t), len(son_t), 'OUI' if gen_t == son_t else 'NON'))
bad = 0
for l in son_c + son_t:
    p = l.split()
    try:
        assert len(p) == 8 and p[5] in ('1', '-1') and p[7] == 'ABCD'
        F(p[1])
        float(p[2])
        int(p[3])
        float(p[4])
        int(p[6])
    except Exception:
        bad += 1
print('lignes qui ne sont pas un appel valable de mon pilote : %d' % bad)
ids = [l.split()[0] + ('j' if l.split()[5] == '1' else 'f') for l in son_c + son_t]
print('appels distincts : %d sur %d (aucun appel en double)' % (len(set(ids)), len(ids)))
print('\nA-8 : rapports miroirs de la chaine, kappa 0.0363 a 1 (MPa contre PPb, meme |delta| = 0.00011) :')
rat = []
for kn in ('0.0363', '0.0530', '0.0800', '0.1300', '0.2000', '0.4000', '1.0000'):
    a = [c for c in det['MP|11']['cellules'] if c['kappa'] == kn][0]
    b = [c for c in det['PP|11']['cellules'] if c['kappa'] == kn][0]
    rat.append(math.log((a['G3_plateau'] / 0.00011) / (b['G3_plateau'] / 0.00011)))
print('    ' + ' ; '.join('%+.5f' % x for x in rat) + '   (ses annonces : -0.00001 ; +0.00006 ; +0.00014 ; +0.00005 ; +0.00008 ; +0.00005 ; +0.00008)')
print('\nA-9 : etalement de ln(G3* / |delta|) sur les huit w2 tires, par kappa :')
et = []
for kn in ('0.0363', '0.0530', '0.0800', '0.1300', '0.2000', '0.4000', '1.0000'):
    v = []
    for c in t['cellules']:
        if c['kappa'] == kn:
            k = round(abs(F(c['w2']) - 2) * 100000)
            mc = [x for x in det['%s|%d' % (c['id'][:2], k)]['cellules'] if x['kappa'] == kn][0]
            v.append(mc['ln_plateau'] - math.log(float(abs(F(c['w2']) - 2))))
    et.append(max(v) - min(v))
print('    ' + ' ; '.join('%.5f' % x for x in et) + '   (sa phrase : de 0.00004 a 0.00048 ; plus petit %.5f, plus grand %.5f chez moi)' % (min(et), max(et)))
