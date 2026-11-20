# -*- coding: ascii -*-
"""Confronte le TABLEAU DE SYNTHESE de la section 7 du gel "pont" (par creneau et par profondeur, sur les huit w2 : e_bord max, etendue au vide max, etendue du lisse max, pas max, plateau predit G3* de ...
a ..., rho_3 lisse a huit |delta| de ... a ...) a mes details. Il porte des nombres que la confrontation cellule par cellule ne contient pas (e_bord, G3*, rho_3). Machine 2, 2026-11-17.
Usage : py -3.11 -I confronte_synthese_section7_machine2_v1.py <gel.md> <mes details.json>"""
import json
import re
import sys
from fractions import Fraction as F

texte = open(sys.argv[1], encoding='utf-8').read(); D = json.load(open(sys.argv[2]))
lignes = re.findall(r'^\s{4}(MG|PG)\s+(\d)\s+(\d\.\d{3})\s+(\d\.\d{4})\s+(\d\.\d{4})\s+(\d\.\d{4})\s+(\d\.\d)e([-+]\d+) a (\d\.\d)e([-+]\d+)\s+(\d)e([-+]\d+) a (\d)e([-+]\d+)', texte, re.M)
print('lignes de synthese lues dans la section 7 : %d (attendu 6)' % len(lignes))
tot = ok = 0
for (s, m, eb, ev, el, pas, p0, e0, p1, e1, r0, f0, r1, f1) in lignes:
    m = int(m); cel = [d for d in D if d['m'] == m and float(F(d['w2'])) * (1 if s == 'PG' else 1) and ((float(F(d['w2'])) < 2) == (s == 'MG'))]
    moi = (max(d['e_bord'] for d in cel), max(d['etendue_vide'] for d in cel), max(d['etendue_lisse_max'] for d in cel), max(d['pas_max'] for d in cel),
           min(d['plateau'] for d in cel), max(d['plateau'] for d in cel), min(d['rho3_8'] * abs(float(F(d['w2'])) - 2.0) for d in cel), max(d['rho3_8'] * abs(float(F(d['w2'])) - 2.0) for d in cel))
    # la derniere colonne du gel est rho_3 |delta| a huit |delta| (en-tete "rho_3 |delta|") : la densite MULTIPLIEE par |delta| = |w2 - 2| de la cellule ; mon premier passage l'avait lue sans |delta|
    lui = (float(eb), float(ev), float(el), float(pas), float(p0 + 'e' + e0), float(p1 + 'e' + e1), float(r0 + 'e' + f0), float(r1 + 'e' + f1))
    nom = ('e_bord max', 'etendue au vide max', 'etendue du lisse max', 'pas max', 'G3* min', 'G3* max', 'rho_3(8) min', 'rho_3(8) max')
    for k, (a, b) in enumerate(zip(moi, lui)):
        tot += 1
        if k < 4:
            digits = 3 if k == 0 else 4; bon = abs(round(a, digits) - b) < 0.6 * 10 ** (-digits)
        elif k < 6:
            bon = abs(float('%.1e' % a) - b) < 1e-12 * max(abs(b), 1e-300) * 1e3 or float('%.1e' % a) == b
        else:
            bon = float('%.0e' % a) == b
        ok += bon
        if not bon:
            print('   ECART %s m=%d %s : moi %.6g ; lui %.6g' % (s, m, nom[k], a, b))
    print('   %s m=%d : e_bord %.4f ; etendue vide %.4f ; etendue lisse %.4f ; pas %.4f ; G3* de %.2e a %.2e ; rho_3 |delta| a 8 |delta| de %.1e a %.1e' % ((s, m) + moi))
print('%d nombres de synthese sur %d identiques a la precision imprimee par le gel' % (ok, tot))
