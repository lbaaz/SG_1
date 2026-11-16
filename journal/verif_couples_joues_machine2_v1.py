# -*- coding: ascii -*-
"""M-4 de la note de machine 1 'la carte du gel de la loi' : la liste des couples (w2, facteur) DEJA JOUES, recopiee a la main (marque 'j' dans la grille de la section 3), est comparee a ce que je sais :
(1) les seize points du depot du delta 98 (sonde_ordre2.json : w2, g, et le facteur g / g_du_point(w2) recalcule avec le moteur) ; (2) les couples que la section 4 du gel du delta 98 (41153158190cf7f1)
declare joues avant lui (M17, 'hors plage', 'garde G-1'). Hors chaine, lecture seule, AUCUN calcul 2D : g_du_point est une fonction du moteur.
Usage : py -3.11 -P verif_couples_joues_machine2_v1.py <moteur_v17.py> <sonde_ordre2.json> <note carte de machine 1 (.md)> <sortie.json>"""
import importlib.util
import json
import re
import sys
from fractions import Fraction as F

MOTEUR, DEP, NOTE, SORTIE = sys.argv[1:5]
spec = importlib.util.spec_from_file_location('moteur', MOTEUR)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)

COLS = [F(1, 2), F(3, 5), F(2, 3), F(3, 4), F(5, 6), F(1), F(6, 5), F(4, 3), F(3, 2), F(5, 3), F(2)]
# (1) les points du depot
joues = {}
for p in json.load(open(DEP))['points']:
    w2 = F(p['w2'])
    r = p['g'] / M.g_du_point(w2)
    fr = F(r).limit_denominator(12)
    assert abs(float(fr) - r) < 1e-9, ('facteur non rationnel simple', p['id'], r)
    joues[(w2, fr)] = 'delta98 ' + p['id']
n_depot = len(joues)
# (2) couples declares joues avant le gel du delta 98 (section 4 du gel)
avant = []
for w in ('1.95', '1.97', '1.98', '2.02', '2.03', '2.05', '1.85', '1.90', '1.96', '2.04', '2.10', '2.15', '2.08', '2.09', '1.91', '2.12', '1.89'):
    avant.append((F(w), F(1)))
for w in ('1.95', '2.05', '2.10', '2.12', '1.90'):
    avant.append((F(w), F(3, 2)))
for w in ('1.95', '2.05', '2.08', '2.10', '1.91', '1.90'):
    avant.append((F(w), F(2, 3)))
for c in avant:
    joues.setdefault(c, 'avant le gel du delta 98')
# (3) la grille de machine 1
txt = open(NOTE, encoding='utf-8').read()
marques = set()
lignes = 0
for l in txt.split('\n'):
    m = re.match(r'\| ([+-]0,\d\d) \| (.*) \|$', l)
    if not m or '/' not in m.group(2) or l.count('|') != 13:
        continue
    cel = [x.strip() for x in m.group(2).split('|')]
    if len(cel) != 11 or not all(re.match(r'^\d+/\d+/\d+', c) for c in cel):
        continue
    lignes += 1
    d = F(m.group(1).replace(',', '.'))
    for c, f in zip(cel, COLS):
        if c.endswith(' j'):
            marques.add((F(2) + d, f))
print('lignes de la grille lues : %d (attendu 22)' % lignes)
sur_grille = {c: o for c, o in joues.items() if c[1] in COLS and (c[0] * 100).denominator == 1 and 2 <= abs((c[0] - 2) * 100) <= 12}
print('couples joues connus de moi : %d (dont %d points du depot) ; sur la grille de machine 1 : %d ; marques j de machine 1 : %d' % (len(joues), n_depot, len(sur_grille), len(marques)))
manque_chez_lui = sorted(set(sur_grille) - marques)
en_trop_chez_lui = sorted(marques - set(sur_grille))
print('joues par moi sur la grille mais SANS marque j chez machine 1 : %d' % len(manque_chez_lui))
for c in manque_chez_lui:
    print('   w2 = %s facteur %s  (%s)' % (c[0], c[1], sur_grille[c]))
print('marques j chez machine 1 que je ne connais pas comme joues : %d' % len(en_trop_chez_lui))
for c in en_trop_chez_lui:
    print('   w2 = %s facteur %s' % (c[0], c[1]))
hors = sorted(c for c in joues if c not in sur_grille)
print('couples joues connus de moi hors de la grille (|delta| > 0.12 ou facteur hors des onze) : %d' % len(hors))
print('   ', ', '.join('(%s, %s)' % (c[0], c[1]) for c in hors))
json.dump({'joues': ['%s %s %s' % (c[0], c[1], o) for c, o in sorted(joues.items())], 'marques_machine1': ['%s %s' % c for c in sorted(marques)],
           'manque_chez_machine1': ['%s %s' % c for c in manque_chez_lui], 'en_trop_chez_machine1': ['%s %s' % c for c in en_trop_chez_lui]}, open(SORTIE, 'w'), indent=1)
print('M-4 : %s' % ('LA LISTE DE MACHINE 1 EST EXACTE' if not manque_chez_lui and not en_trop_chez_lui else 'ECARTS (voir ci-dessus)'))
