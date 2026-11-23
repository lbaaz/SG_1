# -*- coding: ascii -*-
"""MON tirage du gel "SOMMET" (partie 1), certification (c), ecrit depuis les sections 3 et 6 de la piece SEULES, sans lire tirage_sommet_machine1_v1.py.
Le w2 du creneau s au rang r est l'element de numero int(sha256("<graine>|<s>|<r>") en hexadecimal, 16) modulo n_s de la liste CROISSANTE des n_s w2 candidats du creneau (numerotee a partir de 0) ; chaine hachee en ASCII ; s = MP, PP, MG ou PG ; r en decimal sans zero devant.
Regle des rangs (section 6) : pour chaque creneau, dans l'ordre MP, PP, MG, PG et independamment, on parcourt les rangs 0, 1, 2, ... ; le w2 tire a un rang est RETENU s'il est eligible dans la TABLE COMMUNE et s'il n'est pas deja retenu ; sinon rang suivant (creneau ENTIER) ;
on s'arrete a DEUX w2 retenus ("a" puis "b") ; au plus dix rangs (0 a 9) ; sinon PAS DE GEL. Sortie : les huit w2, leurs cinquante-six cellules (g, eta0, r_c ecrits dans la table commune).
LA GRAINE : une suite de chiffres (0 a 9), d'au moins six chiffres, donnee par l'operateur. Ce script REFUSE toute autre graine, sauf l'option --demonstration (la graine "DEMONSTRATION", qui n'est pas un tirage).
Usage : py -3.11 -I tirage_sommet_machine2_v1.py <table commune JSON> <graine ou DEMONSTRATION> [--demonstration]"""
import hashlib
import json
import re
import sys
from fractions import Fraction as F

TABLE, GRAINE = sys.argv[1], sys.argv[2]
DEMO = '--demonstration' in sys.argv[3:]
if DEMO:
    if GRAINE != 'DEMONSTRATION':
        raise SystemExit("REFUS : --demonstration ne prend que la graine DEMONSTRATION")
elif not re.fullmatch(r'[0-9]{6,}', GRAINE):
    raise SystemExit("REFUS : une graine est une suite de chiffres, d'au moins six chiffres, donnee par l'operateur")
commune = json.load(open(TABLE))['creneaux']
ORDRE = ('MP', 'PP', 'MG', 'PG')


def candidats(nom):
    return sorted(F(c['w2']) for c in commune[nom]['candidats'])


def element(graine, s, r):
    h = hashlib.sha256(('%s|%s|%d' % (graine, s, r)).encode('ascii')).hexdigest()
    return h, int(h, 16)


def cellules(nom, w2):
    c = [x for x in commune[nom]['candidats'] if F(x['w2']) == w2][0]
    return c['cellules']


def tire(graine, nom):
    liste = candidats(nom)
    elig = {F(c['w2']): c['eligible'] for c in commune[nom]['candidats']}
    suite, retenus = [], []
    for r in range(10):
        h, n = element(graine, nom, r)
        w2 = liste[n % len(liste)]
        ok = elig[w2] and w2 not in retenus
        suite.append((r, h, n % len(liste), w2, elig[w2], w2 in retenus))
        if ok:
            retenus.append(w2)
            if len(retenus) == 2:
                return suite, retenus
    return suite, None


print('graine : %s%s ; table commune : %s' % (GRAINE, ' (DEMONSTRATION : PAS un tirage)' if DEMO else '', TABLE if False else 'lue'))
print('\nles huit lignes de controle de la section 3 (rangs 0 et 1 bruts, avant la regle des rangs) :')
for nom in ORDRE:
    for r in (0, 1):
        h, n = element(GRAINE, nom, r)
        ns = len(candidats(nom))
        print('    sha256("%s|%s|%d") = %s... ; modulo %d = %d -> w2 = %.5f' % (GRAINE, nom, r, h[:16], ns, n % ns, float(candidats(nom)[n % ns])))
print('\ntirage (regle des rangs, section 6) :')
tout, nb = [], 0
for nom in ORDRE:
    suite, res = tire(GRAINE, nom)
    for (r, h, i, w2, el, deja) in suite:
        print('  %s rang %d : indice %d sur %d -> w2 = %.5f ; eligible dans la table commune : %s ; deja retenu : %s' % (nom, r, i, len(candidats(nom)), float(w2), el, deja))
    if res is None:
        print('  %s : PAS DE GEL (pas deux w2 eligibles distincts en dix rangs)' % nom)
        raise SystemExit(2)
    for lettre, w2 in zip('ab', res):
        print('  => %s%s : w2 = %s = %.5f' % (nom, lettre, w2, float(w2)))
        for j, c in enumerate(cellules(nom, w2), 1):
            print('       %s%s%d  kappa %s  g = %s  eta0 = %s  r_c = %d' % (nom, lettre, j, c['kappa'], c['g'], c['eta0'], c['r_c']))
            nb += 1
        tout.append((nom + lettre, str(w2)))
print('\n%d w2, %d cellules : %s' % (len(tout), nb, ' '.join('%s=%s' % x for x in tout)))
