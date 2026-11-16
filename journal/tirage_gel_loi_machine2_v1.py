# -*- coding: ascii -*-
"""REGLE DE TIRAGE du gel de la loi -- machine 2, v1, 2026-11-15 (section 4 de POUR_MACHINE1_carte_reponse_machine2_v1.md). stdlib seule ; aucun calcul physique ; ne lit aucun resultat.
Quatre creneaux, au millieme de w2, centiemes exclus ; le w2 du creneau s au rang r (r = 0, 1, 2, ...) est la valeur de numero (int(sha256("<graine>|<s>|<r>"), 16) modulo n_s) de la liste croissante du
creneau. La GRAINE est une suite de chiffres donnee par l'operateur APRES la certification de la regle ; ce script ne la contient pas et refuse de tourner sans elle. L'eligibilite des cellules du tirage (calculee
en 1D par les deux machines) n'est PAS dans ce script : si une cellule d'un creneau est ineligible, on rappelle ce script avec r + 1 pour le creneau ENTIER, au plus cinq rangs.
Usage : py -3.11 -I tirage_gel_loi_machine2_v1.py <graine : chiffres> <rang r : 0 a 4>
        py -3.11 -I tirage_gel_loi_machine2_v1.py --listes        (affiche les quatre listes de candidats, sans tirer)
        py -3.11 -I tirage_gel_loi_machine2_v1.py --essai         (selftest sur une graine d'ESSAI ; ses valeurs ne servent a rien)"""
import hashlib
import re
import sys
from fractions import Fraction as F

# creneau : (fenetre ouverte sur delta, facteurs)
CRENEAUX = {'N': (F(-70, 1000), F(-60, 1000), ('3/4', '5/6', '1', '6/5', '4/3')),
            'P': (F(30, 1000), F(50, 1000), ('3/4', '5/6', '1', '6/5', '4/3')),
            'BN': (F(-85, 1000), F(-75, 1000), ('1',)),
            'BP': (F(60, 1000), F(70, 1000), ('1',))}
ORDRE = ('N', 'P', 'BN', 'BP')
RANGS_MAX = 5


def liste(s):
    """w2 = 2 + delta au millieme, delta strictement dans la fenetre, centiemes exclus (ils sont joues a d'autres facteurs)."""
    lo, hi, _ = CRENEAUX[s]
    out = []
    for m in range(1800, 2200):                       # w2 = m / 1000
        w2 = F(m, 1000)
        d = w2 - 2
        if lo < d < hi and (w2 * 100).denominator != 1:
            out.append(w2)
    return out


def tire(graine, s, r):
    L = liste(s)
    h = hashlib.sha256(('%s|%s|%d' % (graine, s, r)).encode('ascii')).hexdigest()
    return L[int(h, 16) % len(L)]


def main():
    a = sys.argv[1:]
    if a == ['--listes']:
        att = {'N': 9, 'P': 18, 'BN': 8, 'BP': 9}
        for s in ORDRE:
            L = liste(s)
            print('%-2s : %2d valeurs (attendu %d) : %s' % (s, len(L), att[s], ' '.join('%.3f' % float(x) for x in L)))
            assert len(L) == att[s], 'la liste du creneau %s n a pas le compte annonce' % s
        return
    if a == ['--essai']:
        g = '0000000000'
        print('ESSAI SUR UNE GRAINE QUI N EST PAS CELLE DE L OPERATEUR (%s) : ne retenir aucune de ces valeurs' % g)
        deja = set()
        for r in range(RANGS_MAX):
            ligne = []
            for s in ORDRE:
                w = tire(g, s, r)
                assert w in liste(s) and (w * 100).denominator != 1
                ligne.append('%s %.3f' % (s, float(w)))
            print('  rang %d : %s' % (r, ' ; '.join(ligne)))
        assert tire(g, 'N', 0) == tire(g, 'N', 0), 'tirage non deterministe'
        print('ESSAI : deterministe, valeurs dans les listes, aucun centieme')
        return
    if len(a) != 2 or not re.fullmatch(r'\d{6,}', a[0]) or not re.fullmatch(r'[0-4]', a[1]):
        raise SystemExit('REFUS : il faut la graine de l operateur (au moins six chiffres) et un rang 0 a 4')
    graine, r = a[0], int(a[1])
    print('graine %s, rang %d (sha256 de "<graine>|<creneau>|<rang>", modulo la taille de la liste)' % (graine, r))
    for s in ORDRE:
        w = tire(graine, s, r)
        lo, hi, fac = CRENEAUX[s]
        print('  %-2s : w2 = %.3f (delta %+.3f), facteurs %s' % (s, float(w), float(w - 2), ' '.join(fac)))


if __name__ == '__main__':
    main()
