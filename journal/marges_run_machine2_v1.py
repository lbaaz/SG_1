# -*- coding: ascii -*-
"""MARGES AUX SEUILS du run du gel loi de la largeur, ordre 3 -- machine 2, 2026-11-16. EXTRA, hors verdict : le verdict du run est celui de la feuille d'ordre 3 jouee dans le run.
Lit la sortie de MA feuille independante sur les vrais fichiers (concordance_run_machine2_v1.json) et la table gelee ; ne calcule rien en 2D, ne rejoue aucun appel.
Pour chaque cellule : E1 = plus petite marge T - |ln q3| sur les etats du domaine ; E2 = nombre d'etats ou l'ordre 3 est plus pres, contre le seuil ; E3 = plus petite marge ln B - |ln q2| sur les etats juges.
Usage : py -3.11 -P marges_run_machine2_v1.py <concordance_run_machine2_v1.json> <table_points_gel_loi_ordre3_v1.json>"""
import json
import math
import sys
from fractions import Fraction as F

o = json.load(open(sys.argv[1]))
t = json.load(open(sys.argv[2]))
W = {p['id']: p for p in t['points']}


def bande(w2):
    d = abs(F(str(w2)) - 2)
    return 1.25 if d <= F(6, 100) else 1.6


print('MARGES AUX SEUILS, lues sur la sortie de ma feuille independante (extra, hors verdict du run)')
pire = None
for c in o['cellules']:
    dom = [e for e in c['etats'] if e['exclu'] is None and e['domaine']]
    jug = [e for e in c['etats'] if e['exclu'] is None]
    m1 = min(dom, key=lambda e: e['T'] - abs(e['ln_q3']))
    B = bande(W[c['id']]['w2'])
    m3 = min(jug, key=lambda e: math.log(B) - abs(e['ln_q2']))
    ex = [(e['rang'], e['exclu']) for e in c['etats'] if e['exclu']]
    marge = m1['T'] - abs(m1['ln_q3'])
    if pire is None or marge < pire[0]:
        pire = (marge, c['id'], m1)
    print('%-3s %-3s domaine %2d  E1 marge %+.6f (rang %2d, T %.2f, |ln q3| %.6f, e_bord %.4f)  E2 %s  E3 marge %+.4f (rang %2d, bande %.2f)  exclus %s' % (
        c['id'], c['creneau'], len(dom), marge, m1['rang'], m1['T'], abs(m1['ln_q3']), m1['e_bord'], ('%d/%d' % (c['n_pres'], c['seuil_E2'])) if c['E2'] else '-',
        math.log(B) - abs(m3['ln_q2']), m3['rang'], B, ex))
print('plus petite marge E1 de tout le run : %+.6f a la cellule %s, etat de rang %d (|ln q3| %.6f pour T %.2f, e_bord %.4f, stab3 %.4f)' % (
    pire[0], pire[1], pire[2]['rang'], abs(pire[2]['ln_q3']), pire[2]['T'], pire[2]['e_bord'], pire[2]['stab3']))
