# -*- coding: ascii -*-
"""VERIFICATION, par moi, de la section 3 de la note de machine 1 (22g, lot 423ec0fd24240977), "d'apres coup" : 2D moins chaine du PREMIER ordre (C1) et moins sa table d'ordre 2 (C2), par force d'absorbeur et couplage.
C1 : son fichier chaine_premier_ordre_pole_court.json, lu comme DONNEES (cles "a|m_c|m0", Gamma / g, independant de g). 2D : MES 8 JSON pole_court_sorties/. C2 : la constante TABLE de mon analyse_pole_court_machine2_v1.py (recopie verifiee identique a sa note, 96 sur 96).
Je recalcule : max |2D - C1|, max |2D - C2|, nombre de cas ou C1 est plus pres que C2, signes a a = 0.5 par parite de coupe, croissance de 2D - C1 quand g double. Je ne reprends aucun de ses scripts.
Usage : py -3.11 -I verifie_apres_coup_m1_machine2_v1.py <chaine_premier_ordre_pole_court.json> <pole_court_sorties>"""
import ast
import glob
import json
import os
import sys

C1 = {tuple(k.split('|')): v for k, v in json.load(open(sys.argv[1], encoding='ascii')).items()}
ICI = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(ICI, 'analyse_pole_court_machine2_v1.py'), encoding='ascii').read()
TABLE = ast.literal_eval(src[src.index('TABLE = {'):src.index('fs = sorted(')].split('=', 1)[1].strip())
D2 = {}
for f in glob.glob(os.path.join(sys.argv[2], 'pole_court_b*_g*.json')):
    d = json.load(open(f, encoding='ascii'))
    for c in d['cas']:
        D2[(float(d['g']), c['a'], 10 + d['boite'], c['m0'])] = c['gamma_sur_g']
print('cas 2D : %d ; cles C1 : %d' % (len(D2), len(C1)))
print('%-4s %-6s %-13s %-13s %s' % ('a', 'g', 'max|2D-C1|', 'max|2D-C2|', 'cas ou C1 plus pres que C2'))
ecart = {}
for a in (0.5, 1.0, 2.0, 4.0):
    for g in (5e-4, 1e-3):
        e1, e2, n = 0.0, 0.0, 0
        for mc in (10, 11, 12, 13):
            for m0 in (2, 3, 4):
                v = D2[(g, a, mc, m0)]
                c1 = C1[('%.1f' % a, str(mc), str(m0))]
                c2 = TABLE[(g, a)][mc][m0 - 2]
                ecart[(g, a, mc, m0)] = v - c1
                e1, e2 = max(e1, abs(v - c1)), max(e2, abs(v - c2))
                n += abs(v - c1) < abs(v - c2)
        print('%-4.1f %-6.0e %-13.2e %-13.2e %d sur 12' % (a, g, e1, e2, n))
for a in (0.5, 1.0):
    r = [ecart[(1e-3, a, mc, m0)] / ecart[(5e-4, a, mc, m0)] for mc in (10, 11, 12, 13) for m0 in (2, 3, 4)]
    print('a = %.1f : (2D - C1)(g = 1e-3) / (2D - C1)(g = 5e-4) de %.2f a %.2f' % (a, min(r), max(r)))
for par, mcs in (('paires', (10, 12)), ('impaires', (11, 13))):
    v = [ecart[(g, 0.5, mc, m0)] for g in (5e-4, 1e-3) for mc in mcs for m0 in (2, 3, 4)]
    print('a = 0.5, coupes %s : 2D - C1 : %d negatifs, %d positifs' % (par, sum(x < 0 for x in v), sum(x > 0 for x in v)))
