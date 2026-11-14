# -*- coding: ascii -*-
"""Les statuts des points du run tiennent-ils sous le bruit des fils mesure a la certification ? Pour chaque etat juge, le bruit relatif de la
cible est 7.32e-14 / Gamma_2D(3) (ecart absolu maximal vu entre 16 et 4 fils, compare_16fils_4fils) et celui de la chaine est nul (identique
a tous les fils, meme comparaison) ; on regarde si q x (1 +- bruit) franchit une borne du gel (1/2, 2, 0.3162, 3.1623) et, pour chaque point,
si son statut (le pire des etats juges) change, dans le pire et dans le meilleur sens. Ne juge rien, ne relit rien : un controle de robustesse de la lecture de la feuille.
Usage : python -P stabilite_sous_bruit_machine2_v1.py <verdict.json> <sonde.json>"""
import json, sys
V = json.load(open(sys.argv[1], encoding='ascii')); S = json.load(open(sys.argv[2], encoding='ascii'))
BRUIT = 7.32e-14
BORNES = (0.5, 2.0, 10 ** -0.5, 10 ** 0.5)
def palier(q):
    return 0 if 0.5 <= q <= 2.0 else (1 if q * q >= 0.1 and q * q <= 10.0 else 2)
NOMS = ['FACTEUR 2', 'DECADE', 'HORS DECADE']
tot_juges, plus_proche = 0, (9.9, None)
pire_bruit = (0.0, None)
for x in V['points']:
    if x['statut'] == 'NON LISIBLE':
        continue
    pire0 = max(palier(e['q']) for e in x['etats'] if not e['exclu'])
    pire_bas = pire_haut = 0
    for e in x['etats']:
        if e['exclu']:
            continue
        tot_juges += 1
        rb = BRUIT / e['Gamma_2D']
        if rb > pire_bruit[0]:
            pire_bruit = (rb, (x['id'], e['rang'], e['Gamma_2D']))
        qb, qh = e['q'] / (1 + rb), e['q'] / (1 - rb)          # Gamma_2D au denominateur
        pire_bas = max(pire_bas, palier(min(qb, qh)))
        pire_haut = max(pire_haut, palier(max(qb, qh)))
        for b in BORNES:
            d = abs(e['q'] / b - 1)
            if d < plus_proche[0]:
                plus_proche = (d, (x['id'], e['rang'], e['q'], b))
    # le statut du point sous la pire configuration des deux sens, etat par etat
    pire_conf = max(max(palier(e['q'] / (1 + BRUIT / e['Gamma_2D'])), palier(e['q'] / (1 - BRUIT / e['Gamma_2D']))) for e in x['etats'] if not e['exclu'])
    meilleure = max(min(palier(e['q'] / (1 + BRUIT / e['Gamma_2D'])), palier(e['q'] / (1 - BRUIT / e['Gamma_2D']))) for e in x['etats'] if not e['exclu'])
    print('%s %-6s statut %-11s ; sous le bruit : pire configuration %-11s, meilleure %-11s -> %s' % (x['id'], x['role'], x['statut'], NOMS[pire_conf],
          NOMS[meilleure], 'INCHANGE' if NOMS[pire_conf] == x['statut'] == NOMS[meilleure] else 'POURRAIT CHANGER'))
print('%d etats juges ; bruit relatif maximal de la cible %.2e (%s, Gamma_2D(3) = %.3e) ; q le plus proche d une borne : ecart relatif %.3f (%s)' % (
    tot_juges, pire_bruit[0], pire_bruit[1][:2], pire_bruit[1][2], plus_proche[0], plus_proche[1]))
