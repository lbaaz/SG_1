# -*- coding: ascii -*-
"""TIRAGE DU GEL "PONT", PREMIERE PARTIE -- ma version, ECRITE DEPUIS LE TEXTE DU GEL SEUL (sections 3 et 6). Machine 2, 2026-11-17. Je n'ai pas lu tirage_pont_machine1_v1.py avant de l'ecrire.
Regle : pour chaque creneau s (MG puis PG, independamment) et chaque rang r = 0..4, le w2 est l'element de numero int(sha256("<graine>|<s>|<r>") en hexadecimal, 16) modulo n_s de la liste CROISSANTE
des n_s w2 candidats du creneau ; le premier rang dont le w2 est eligible DANS LA TABLE COMMUNE donne le w2 du creneau (creneau entier, jamais cellule par cellule) ; cinq rangs sans w2 eligible : PAS DE GEL.
La graine est une suite de chiffres (0 a 9), d'au moins six chiffres ; la graine de demonstration ("DEMONSTRATION") n'est PAS une graine valide.
Usage : py -3.11 -I tirage_pont_machine2_v1.py <table commune.json> <graine | --demonstration>
        py -3.11 -I tirage_pont_machine2_v1.py <table commune.json> --simulation <N> <graine de depart>   (statistique sur N graines : repartition, frequence de PAS DE GEL)"""
import hashlib
import json
import re
import sys
from fractions import Fraction as F

MUT = None
if '--mutation' in sys.argv:
    i = sys.argv.index('--mutation'); MUT = sys.argv[i + 1]; del sys.argv[i:i + 2]
TABLE = json.load(open(sys.argv[1], encoding='ascii'))
RANGS = 5 if MUT != 'quatre_rangs' else 4


def tirer(graine, table=TABLE, verifier_graine=True):
    """Rend (cellules, journal) ; cellules = None si PAS DE GEL."""
    if verifier_graine and not re.fullmatch(r'[0-9]{6,}', graine):
        raise SystemExit('graine invalide : suite de chiffres (0 a 9), au moins six')
    res, journal = {}, []
    for s in ('MG', 'PG'):
        cand = sorted(table['creneaux'][s]['candidats'], key=lambda c: F(c['w2']))
        if MUT == 'liste_decroissante':
            cand = cand[::-1]
        n = len(cand); choisi = None
        for r in range(RANGS):
            h = hashlib.sha256(('%s|%s|%d' % (graine, s, r)).encode('ascii')).hexdigest()
            k = int(h, 16) % n
            if MUT == 'modulo_octets':
                k = int(h[:2], 16) % n
            c = cand[k]
            journal.append('%s rang %d : sha256 = %s... ; modulo %d = %d -> w2 = %s %s' % (s, r, h[:16], n, k, ('%.3f' % float(F(c['w2']))), 'ELIGIBLE' if c['eligible'] else 'ineligible'))
            if c['eligible']:
                choisi = c; break
            if MUT == 'cellule_par_cellule':
                break
        if choisi is None:
            return None, journal + ['creneau %s : PAS DE GEL (aucun w2 eligible en %d rangs)' % (s, RANGS)]
        for ce in choisi['cellules']:
            res['%s%d' % (s, ce['m'])] = (('%.3f' % float(F(choisi['w2']))), ce['g'])
    return res, journal


if sys.argv[2] == '--demonstration':
    print('DEMONSTRATION (n est pas une graine valide) ; table : %s' % sys.argv[1])
    res, jr = tirer('DEMONSTRATION', verifier_graine=False)
    print('\n'.join(jr))
    if res:
        print('cellules : ' + ' ; '.join('%s : w2 = %s, g = %s' % (k, v[0], v[1]) for k, v in sorted(res.items())))
elif sys.argv[2] == '--simulation':
    N = int(sys.argv[3]); depart = int(sys.argv[4]); comptes = {'MG': {}, 'PG': {}}; pas_de_gel = {'MG': 0, 'PG': 0, 'au_moins_un': 0}
    for i in range(N):
        g = str(depart + i)
        res, jr = tirer(g.zfill(6))
        if res is None:
            pas_de_gel['au_moins_un'] += 1
            for s in ('MG', 'PG'):
                if any(('creneau %s : PAS DE GEL' % s) in l for l in jr):
                    pas_de_gel[s] += 1
            continue
        for s in ('MG', 'PG'):
            w = res['%s3' % s][0]; comptes[s][w] = comptes[s].get(w, 0) + 1
    print('SIMULATION : %d graines de %d a %d ; PAS DE GEL (au moins un creneau) : %d (%.4f) ; MG : %d (%.4f) ; PG : %d' % (
        N, depart, depart + N - 1, pas_de_gel['au_moins_un'], pas_de_gel['au_moins_un'] / N, pas_de_gel['MG'], pas_de_gel['MG'] / N, pas_de_gel['PG']))
    for s in ('MG', 'PG'):
        print('  %s : %s' % (s, ' '.join('%s:%d' % (w, comptes[s][w]) for w in sorted(comptes[s]))))
else:
    graine = sys.argv[2]
    res, jr = tirer(graine)
    print('\n'.join(jr))
    print('RESULTAT : ' + ('PAS DE GEL' if res is None else ' ; '.join('%s : w2 = %s, g = %s' % (k, v[0], v[1]) for k, v in sorted(res.items()))))
