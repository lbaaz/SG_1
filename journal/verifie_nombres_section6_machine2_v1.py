# -*- coding: ascii -*-
"""Section 6 du gel (seconde partie) : des nombres que le texte AFFIRME sur ses pieces, relus par machine 2 dans les sorties de machine 1 (aucun calcul de sonde, aucune 2D rejouee ici).
(1) au vide, ln(chaine d'ordre 3 / 2D) par absorbeur ; (2) accord des deux lectures par partition et des deux lectures brutes aux cotes 300 (3, 4, 5 barreaux) ; (3) le niveau B4 (5 barreaux, cote 300, x = 6.699) ;
(4) l'ecart maximal entre la partition a r_c et a r_c + 6 sur toutes les boites jouees. Machine 2, 2026-11-17.
Usage : py -3.11 -P verifie_nombres_section6_machine2_v1.py <dossier du lot de machine 1>"""
import glob
import json
import os
import sys

D = sys.argv[1]
print('(1) au vide, ln(chaine d ordre 3 / 2D) :')
for a in 'ABCD':
    v = []
    for p in (3, 4, 5):
        f = os.path.join(D, 'lecture_densite_2d_SA%d_v1.json' % p)
        v.append(json.load(open(f))['vide'][a]['ln_chaine3_sur_2d'])
    print('   absorbeur %s : de %+.5f a %+.5f (trois profondeurs : %s)' % (a, min(v), max(v), ' '.join('%+.5f' % t for t in v)))
print('(2) cote 300 : plus grand ecart relatif entre les deux lectures')
for p in (3, 4, 5):
    b = [json.loads(l) for l in open(os.path.join(D, 'boite_SA%d_300_v1.jsonl' % p)) if l.strip()]
    b = [x for x in b if x['cote'] == 300][0]
    par = max(abs(n['c2_a'] - n['c2_b']) / n['c2_a'] for n in b['niveaux'])
    brut = max(abs(n['brut_a'] - n['brut_b']) / n['brut_a'] for n in b['niveaux'])
    print('   %d barreaux : partition %.2e ; brut %.2e ; niveaux %d, fiables %d' % (p, par, brut, b['n'], b['fiables']))
    if p == 5:
        for n in b['niveaux']:
            if abs(n['x'] - 6.699) < 0.001:
                print('(3) B4 : niveau x = %.4f : partition a/b %.3e / %.3e (ecart relatif %.2e) ; brut a/b %.3e / %.3e (ecart relatif %.4f) ; fiable %s' % (
                    n['x'], n['c2_a'], n['c2_b'], abs(n['c2_a'] - n['c2_b']) / n['c2_a'], n['brut_a'], n['brut_b'], abs(n['brut_a'] - n['brut_b']) / n['brut_a'], n['fiable']))
pire = 0.0
nb = 0
for f in sorted(glob.glob(os.path.join(D, 'boite*_v1.jsonl'))):
    for l in open(f):
        if l.strip():
            b = json.loads(l)
            nb += 1
            pire = max(pire, max(abs(n['c2_a_large'] / n['c2_a'] - 1.0) for n in b['niveaux']) if b['niveaux'] else 0.0)
print('(4) sur %d boites jouees : plus grand ecart relatif partition(r_c + 6) / partition(r_c) : %.2e' % (nb, pire))
