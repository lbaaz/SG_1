# -*- coding: ascii -*-
"""ETIQUETTES PREDITES aux douze cellules (1D seulement : AUCUNE 2D) -- machine 2, 2026-11-16. Pour chaque cellule de la table gelee, mon evaluateur de cellule (controle_carte_machine2/cellule_machine2_v1.py) rend les quatorze
premieres etiquettes (n1, n2) de plus grand poids de Poisson de la graine : ce sont les 'quatorze etiquettes predites de leur cellule' dont l'acte compte celles que les etats lus portent.
Usage : py -3.11 -P etiquettes_predites_machine2_v1.py <moteur_v17.py> <bloc ordre 2> <ordre3_machine2_v1.py> <table.json> <sortie.json>"""
import importlib.util
import json
import sys
from fractions import Fraction as F

spec = importlib.util.spec_from_file_location('cellule', '../controle_carte_machine2/cellule_machine2_v1.py')
CEL = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CEL)
table = json.load(open(sys.argv[4]))
out = {}
for p in table['points']:
    if p['role'] != 'juge':
        continue
    c = CEL.evalue(F(p['w2']), F(p['facteur']))
    out[p['id']] = [[e['n1'], e['n2']] for e in c['etats'][:14]]
    print(p['id'], 'N', c['N'], len(out[p['id']]), 'etiquettes', flush=True)
json.dump(out, open(sys.argv[5], 'w'), indent=1)
