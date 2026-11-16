# -*- coding: ascii -*-
"""TIRAGE COMPLET des douze points du gel 'loi de la largeur, ordre 3' (premiere partie, b56ca5cb2dd25da1, sections 3 et 6) -- machine 2, v1, 2026-11-15. stdlib seule ; aucun calcul physique.
Derive de tirage_gel_loi_machine2_v1.py (non edite : charge par chemin) : ajoute la regle des rangs. Pour chaque creneau, dans l'ordre N, P, BN, BP et independamment : rang 0 ; si le w2 tire n'est pas
eligible dans la table commune (TOUTES les tables donnees : un w2 y est eligible s'il l'est dans chacune), rang suivant, pour le CRENEAU ENTIER ; au plus cinq rangs (0 a 4) ; un creneau sans w2 eligible en
cinq rangs : PAS DE GEL, et on le dit. Un meme w2 peut sortir a deux rangs ; il n'est pas retire de la liste. La graine est lue COMME UNE CHAINE (zeros de tete compris), au moins six chiffres, donnee par
l'operateur ; ce script ne la contient pas.
Usage : py -3.11 -I tirage_complet_machine2_v1.py <tirage_gel_loi_machine2_v1.py> <graine : chiffres> <table.json> [<autre table.json> ...]
        py -3.11 -I tirage_complet_machine2_v1.py <tirage_gel_loi_machine2_v1.py> --demonstration <table.json> [...]   (graine "DEMONSTRATION" : non numerique, ne peut pas etre la graine)
        py -3.11 -I tirage_complet_machine2_v1.py <tirage_gel_loi_machine2_v1.py> --essai                              (selftest : determinisme, rang suivant, arret sans candidat)"""
import importlib.util
import json
import re
import sys
from fractions import Fraction as F

TIRAGE = sys.argv[1]
spec = importlib.util.spec_from_file_location('tirage', TIRAGE)
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)


def tirer(graine, eligible):
    """eligible : fonction (creneau, w2) -> bool. Rend (cellules, journal) ou (None, journal) : PAS DE GEL."""
    cellules, journal = [], []
    for s in T.ORDRE:
        pris = None
        for r in range(T.RANGS_MAX):
            w = T.tire(graine, s, r)
            ok = eligible(s, w)
            journal.append('creneau %-2s rang %d : w2 = %s (%.3f) : %s' % (s, r, w, float(w), 'ELIGIBLE, retenu' if ok else 'INELIGIBLE'))
            if ok:
                pris = w
                break
        if pris is None:
            journal.append('creneau %s : aucun w2 eligible en %d rangs : PAS DE GEL' % (s, T.RANGS_MAX))
            return None, journal
        fac = T.CRENEAUX[s][2]
        for i, f in enumerate(fac):
            cellules.append({'id': s + (str(i + 1) if len(fac) > 1 else ''), 'creneau': s, 'w2': str(pris), 'facteur': f})
    return cellules, journal


def table(chemins):
    tabs = [json.load(open(c)) for c in chemins]
    ok = {}
    for s in T.ORDRE:
        for w in T.liste(s):
            ok[(s, w)] = all(any(F(c['w2']) == w and c['eligible'] for c in t['creneaux'][s]['candidats']) for t in tabs)
    return lambda s, w: ok[(s, w)]


def main():
    a = sys.argv[2:]
    if a == ['--essai']:
        tout = lambda s, w: True
        c1, j1 = tirer('DEMONSTRATION', tout)
        c2, j2 = tirer('DEMONSTRATION', tout)
        assert c1 == c2 and len(c1) == 12 and [c['id'] for c in c1] == ['N1', 'N2', 'N3', 'N4', 'N5', 'P1', 'P2', 'P3', 'P4', 'P5', 'BN', 'BP'], 'tirage non deterministe ou ids faux'
        w_bn0 = T.tire('DEMONSTRATION', 'BN', 0)
        sauf = lambda s, w: not (s == 'BN' and w == w_bn0)
        c3, j3 = tirer('DEMONSTRATION', sauf)
        assert [c for c in c3 if c['creneau'] == 'BN'][0]['w2'] == str(T.tire('DEMONSTRATION', 'BN', 1)) and 'INELIGIBLE' in ' '.join(j3), 'rang suivant faux'
        rien = lambda s, w: not (s == 'P')
        c4, j4 = tirer('DEMONSTRATION', rien)
        assert c4 is None and 'PAS DE GEL' in j4[-1], 'arret sans candidat faux'
        print('\n'.join(j1))
        print('ids : %s' % ' '.join(c['id'] for c in c1))
        print('rang suivant : BN %s ineligible -> %s' % (w_bn0, [c for c in c3 if c['creneau'] == 'BN'][0]['w2']))
        print('ESSAI : TIENT (determinisme, douze cellules, rang suivant, arret sans candidat)')
        return
    if a and a[0] == '--demonstration':
        graine, tabs = 'DEMONSTRATION', a[1:]
        print('GRAINE DE DEMONSTRATION (pas celle de l operateur) : ne retenir aucune de ces valeurs')
    else:
        graine, tabs = a[0], a[1:]
        if not re.fullmatch(r'\d{6,}', graine):
            raise SystemExit('REFUS : la graine est une suite d au moins six chiffres, donnee par l operateur')
    if not tabs:
        raise SystemExit('REFUS : il faut au moins une table d eligibilite (la table commune est le ET de toutes les tables donnees)')
    cellules, journal = tirer(graine, table(tabs))
    print('\n'.join(journal))
    if cellules is None:
        print('PAS DE GEL')
        raise SystemExit(3)
    for c in cellules:
        print('  %-3s w2 = %s (%s) facteur %s' % (c['id'], c['w2'], '%.3f' % float(F(c['w2'])), c['facteur']))


if __name__ == '__main__':
    main()
