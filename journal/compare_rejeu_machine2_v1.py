# -*- coding: ascii -*-
"""Compare les sorties JSON de MON rejeu (sortie/) a celles du lot de m1 : structure identique (cles, longueurs, types, booleens,
chaines) et nombres egaux a une tolerance relative. Les durees sont ecartees. Rend, par fichier : nombres compares, plus grand
ecart relatif, chemin du pire, desaccords de structure.
Usage : py -3.11 -I compare_rejeu_machine2_v1.py [tol_rel]"""
import json
import math
import sys

BASE = r'd:\devs\bocal\BOCAL4'
LOT = BASE + r'\livraison_16e_vide_etape_sans_run\ext\lot_machine1_2026-11-16_vide_etape_sans_run_v1'
MIEN = BASE + r'\rejeu_vide_machine2\sortie'
FICHIERS = ['temoin_lecteur_vide_v1.json', 'procede_lecteur_profond_v1.json', 'mandataire_absorbeur_2D_v1.json',
            'absorbeur_adapte_v1.json', 'controle_joues_absorbeur_v1.json', 'carte_adaptee_v1.json', 'apres_barriere_v1.json']
IGNORE = ('duree_s', 'assemblage_s', 'duree_totale_s')
TOL = float(sys.argv[1]) if len(sys.argv) > 1 else 1e-9


def cmp(a, b, chemin, st):
    if isinstance(a, dict):
        if not isinstance(b, dict) or set(a) != set(b):
            st['struct'].append(chemin + ' (cles)')
            return
        for k in a:
            if k in IGNORE:
                continue
            cmp(a[k], b[k], chemin + '/' + str(k), st)
    elif isinstance(a, list):
        if not isinstance(b, list) or len(a) != len(b):
            st['struct'].append(chemin + ' (longueur)')
            return
        for i, (x, y) in enumerate(zip(a, b)):
            cmp(x, y, chemin + '[%d]' % i, st)
    elif isinstance(a, bool) or a is None or isinstance(a, str):
        if a != b:
            st['struct'].append('%s : %r vs %r' % (chemin, a, b))
    elif isinstance(a, (int, float)):
        if not isinstance(b, (int, float)) or isinstance(b, bool):
            st['struct'].append(chemin + ' (type)')
            return
        st['n'] += 1
        if a == b:
            return
        if math.isnan(a) and math.isnan(b):
            return
        r = abs(a - b) / max(abs(a), abs(b), 1e-300)
        if abs(a - b) > st['pire_abs'] and max(abs(a), abs(b)) > 1e-3:
            st['pire_abs'], st['chemin_abs'] = abs(a - b), chemin
        if r > st['pire']:
            st['pire'], st['chemin'] = r, chemin
        if r > TOL:
            st['hors'] += 1
    else:
        st['struct'].append(chemin + ' (type inconnu)')


tot_struct = 0
for f in FICHIERS:
    st = {'n': 0, 'pire': 0.0, 'chemin': '', 'pire_abs': 0.0, 'chemin_abs': '', 'hors': 0, 'struct': []}
    try:
        a = json.load(open(LOT + '\\' + f))
        b = json.load(open(MIEN + '\\' + f))
    except Exception as e:
        print('%-36s ABSENT/ILLISIBLE : %s' % (f, e))
        tot_struct += 1
        continue
    cmp(a, b, '', st)
    tot_struct += len(st['struct'])
    print('%-36s nombres %6d  pire ecart relatif %.2e  hors tol(%.0e) : %4d  desaccords de structure : %d' % (
        f, st['n'], st['pire'], TOL, st['hors'], len(st['struct'])))
    if st['pire'] > 0:
        print('      pire relatif a', st['chemin'])
        print('      pire ABSOLU (valeurs > 1e-3) : %.2e a %s' % (st['pire_abs'], st['chemin_abs']))
    for s in st['struct'][:6]:
        print('      STRUCT', s)
print('DESACCORDS DE STRUCTURE TOTAL :', tot_struct)
