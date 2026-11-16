# -*- coding: ascii -*-
"""MON TIRAGE REEL du gel 'largeur du vide' (partie 1, b57c9ccdd3946261), par MON code. Derive de tirage_demonstration_machine2_v1.py (non edite : il est dans mon lot d4f95772710d545c).
Sections 3 et 6 du gel : w2 du creneau s au rang r = element de numero int(sha256("<graine>|<s>|<r>") hex, 16) modulo n_s de la liste croissante des w2 candidats ; si le w2 tire n'est pas
eligible dans la table commune : rang suivant, pour le creneau entier ; au plus cinq rangs ; sinon PAS DE GEL. La graine est une suite de chiffres (au moins six), donnee par l'operateur, reportee telle quelle.
La table commune est la MIENNE (table_commune_vide_machine2_v1.json) ; celle de m1 (table_commune_vide_machine1_v1.json) doit lui etre egale en contenu.
Aucune 2D, aucun calcul de largeur. Usage : py -3.11 -I tirage_graine_machine2_v1.py <graine>"""
import hashlib
import json
import re
import sys
from fractions import Fraction as F

D = r'd:\devs\bocal\BOCAL4\certif_gel_vide_partie1_machine2'
M1 = r'd:\devs\bocal\BOCAL4\livraison_16g_reception_certification_vide\ext\lot_machine1_2026-11-16_reception_certification_gel_vide_partie1_v1\table_commune_vide_machine1_v1.json'
if len(sys.argv) != 2 or not re.fullmatch(r'[0-9]{6,}', sys.argv[1]):
    raise SystemExit('REFUS : la graine doit etre une suite d au moins six chiffres (0 a 9)')
GRAINE = sys.argv[1]
commune = json.load(open(D + r'\table_commune_vide_machine2_v1.json'))['creneaux']
autre = json.load(open(M1))['creneaux']
print('table commune de m2 == table commune de m1 (contenu JSON) :', commune == autre)
if commune != autre:
    raise SystemExit('REFUS : les deux tables communes different')
PROF = (3, 4, 5, 6, 8, 12, 16)


def candidats(nom):
    return sorted(F(c['w2']) for c in commune[nom]['candidats'])


def element(s, r):
    h = hashlib.sha256(('%s|%s|%d' % (GRAINE, s, r)).encode('ascii')).hexdigest()
    return h, int(h, 16)


resultat = {}
print('graine :', GRAINE)
for nom in ('MG', 'MP', 'PP', 'PG'):
    liste = candidats(nom)
    elig = {F(c['w2']): c for c in commune[nom]['candidats']}
    choix = None
    for r in range(5):
        h, n = element(nom, r)
        w2 = liste[n % len(liste)]
        print('  %s rang %d : sha256("%s|%s|%d") = %s... ; modulo %d = %d -> w2 = %s (%.3f) : %s' % (
            nom, r, GRAINE, nom, r, h[:16], len(liste), n % len(liste), w2, float(w2), 'ELIGIBLE, retenu' if elig[w2]['eligible'] else 'inelligible, rang suivant'))
        if elig[w2]['eligible']:
            choix = (r, w2, elig[w2])
            break
    if choix is None:
        raise SystemExit('PAS DE GEL : le creneau %s n a pas de w2 eligible en cinq rangs' % nom)
    resultat[nom] = choix
print()
cellules = []
for nom in ('MG', 'MP', 'PP', 'PG'):
    r, w2, c = resultat[nom]
    for x in c['cellules']:
        cellules.append({'id': '%s%d' % (nom, x['m']), 'creneau': nom, 'rang': r, 'w2': str(w2), 'w2_decimal': '%.3f' % float(w2), 'm': x['m'], 'g': x['g'],
                         'ligne': 'lisible' if x['m'] in (3, 4, 5, 6) else 'profonde', 'retenue': bool(x['eligible'])})
for c in cellules:
    print('  %-5s w2 = %-9s (%s)  m = %-2d  g = %s  %s%s' % (c['id'], c['w2'], c['w2_decimal'], c['m'], c['g'], c['ligne'], '' if c['retenue'] else '  NON RETENUE'))
print()
print('cellules : %d (lisibles %d, profondes retenues %d)' % (len(cellules), sum(1 for c in cellules if c['ligne'] == 'lisible'), sum(1 for c in cellules if c['ligne'] == 'profonde' and c['retenue'])))
json.dump({'graine': GRAINE, 'creneaux': {k: {'rang': v[0], 'w2': str(v[1])} for k, v in resultat.items()}, 'cellules': cellules},
          open(D + r'\tirage_graine_%s_machine2_v1.json' % GRAINE, 'w', newline='\n'), indent=1, sort_keys=True)
