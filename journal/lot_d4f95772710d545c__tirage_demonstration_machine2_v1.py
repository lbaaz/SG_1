# -*- coding: ascii -*-
"""MON tirage (certification (c)), ecrit depuis la section 3 et la section 6 du gel seules, sans lire tirage_vide_machine1_v1.py.
w2 du creneau s au rang r = element de numero int(sha256("<graine>|<s>|<r>") hex, 16) modulo n_s de la liste CROISSANTE des w2 candidats du creneau (a partir de 0).
Rangs : pour chaque creneau, rang 0 ; si le w2 tire n'est pas eligible dans la table commune : rang 1, etc. (au plus cinq rangs, 0 a 4) ; creneau entier.
Ici : la graine de DEMONSTRATION (qui n'est pas une suite de chiffres : ce n'est pas un tirage), et la table commune (mon ET).
Usage : py -3.11 -I tirage_demonstration_machine2_v1.py"""
import hashlib
import json
from fractions import Fraction as F

D = r'd:\devs\bocal\BOCAL4\certif_gel_vide_partie1_machine2'
commune = json.load(open(D + r'\table_commune_vide_machine2_v1.json'))['creneaux']


def candidats(nom):
    return sorted(F(c['w2']) for c in commune[nom]['candidats'])


def element(graine, s, r):
    h = hashlib.sha256(('%s|%s|%d' % (graine, s, r)).encode('ascii')).hexdigest()
    return h, int(h, 16)


def tire(graine, nom):
    liste = candidats(nom)
    elig = {F(c['w2']): c['eligible'] for c in commune[nom]['candidats']}
    suite = []
    for r in range(5):
        h, n = element(graine, nom, r)
        w2 = liste[n % len(liste)]
        suite.append((r, h, n % len(liste), w2, elig[w2]))
        if elig[w2]:
            return suite, (r, w2)
    return suite, None


# exemple de controle du gel : sha256("DEMONSTRATION|MG|0") = 8254e7d473dd8e66... ; modulo 9 = 6 -> w2 = 1.987
h, n = element('DEMONSTRATION', 'MG', 0)
print('sha256("DEMONSTRATION|MG|0") =', h)
print('commence par 8254e7d473dd8e66 :', h.startswith('8254e7d473dd8e66'), '; modulo 9 =', n % 9, '; w2 =', float(candidats('MG')[n % 9]))
ok = h.startswith('8254e7d473dd8e66') and n % 9 == 6 and candidats('MG')[6] == F(1987, 1000)
print('EXEMPLE DU GEL RETROUVE :', ok)
print()
print('tirage de DEMONSTRATION (pas un tirage : la graine n est pas une suite de chiffres) :')
for nom in ('MG', 'MP', 'PP', 'PG'):
    suite, res = tire('DEMONSTRATION', nom)
    print('  %s : rang %d, w2 = %s (indice %d sur %d)' % (nom, res[0], float(res[1]), suite[res[0]][2], len(candidats(nom))))
# contrainte du gel : la graine est une suite d'au moins six chiffres -> refuser une graine qui n'en est pas une pour un VRAI tirage
print()
print('liste croissante du creneau MG :', [float(x) for x in candidats('MG')])
