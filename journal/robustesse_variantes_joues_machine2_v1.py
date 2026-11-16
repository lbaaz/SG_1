# -*- coding: ascii -*-
"""NOUVEAU CALCUL DE MA MAIN (pas un rejeu) : pour chaque etat joue du domaine des deltas 98 et 100, parmi les 18 variantes
d'absorbeur adapte de m1 (famille de la note, section 3.2), combien feraient sortir la chaine d'ordre 3 de la tolerance E1 ?
Meme chaine d'ordre 3 (blocs deposes), memes tables, memes variantes : seule la LECTURE est differente (je garde les 18 valeurs
au lieu de la mediane). Apres coup ; ce n'est pas un rejeu du gel du delta 100, aucun verdict n'est modifie. Aucun calcul 2D.
Les largeurs 2D de plateau et les tolerances sont LUES dans la sortie de mon rejeu (controle_joues_absorbeur_v1.json) et dans
superposition_v1.json de m1. Derive de controle_joues_absorbeur_machine1_v1.py (non edite : je ne fais qu'importer ses fonctions).
Usage : py -3.11 -P robustesse_variantes_joues_machine2_v1.py"""
import json
import math
import importlib.util
import statistics
import sys
from fractions import Fraction as F

BASE = r'd:\devs\bocal\BOCAL4'
LOT = BASE + r'\livraison_16e_vide_etape_sans_run\ext\lot_machine1_2026-11-16_vide_etape_sans_run_v1'
MOTEUR = BASE + r'\m17_chaine_v17.py'
BLOC2 = BASE + r'\ordre2\chaine_ordre2_bloc_machine1_v1.py'
BLOC3 = BASE + r'\livraison_16a_gel_loi_partie2\ext\lot_m1\ordre3_bloc_machine1_v1.py'
PHI, CARTE, ADAPTE = LOT + r'\phi_echelle_machine1_v1.py', LOT + r'\carte_machine1_v1.py', LOT + r'\absorbeur_adapte_machine1_v1.py'
SUPER = LOT + r'\superposition_v1.json'
JOUES = BASE + r'\rejeu_vide_machine2\sortie\controle_joues_absorbeur_v1.json'
SORTIE = BASE + r'\rejeu_vide_machine2\sortie\robustesse_variantes_joues_machine2_v1.json'

spec = importlib.util.spec_from_file_location('adapte', ADAPTE)
A = importlib.util.module_from_spec(spec)
spec.loader.exec_module(A)
C = A.charger(MOTEUR, BLOC2, BLOC3, PHI, CARTE)
E = [e for e in json.load(open(SUPER))['etats'] if e['domaine']]
tol = {(e['source'], e['id'], e['rang']): e['tolerance_E1'] for e in json.load(open(JOUES))['etats']}
sortie = []
for i, e in enumerate(E):
    C._cache.clear()
    w2 = F(e['w2'])
    tb, t3 = A.tables(e['n1'], e['n2'], w2, e['g'])
    p = A.plateau(tb, t3, 3, e['ln_Phi'])
    d = abs(e['delta'])
    ln_gpl = math.log(e['Gamma_pl'] / d)
    q = [v - ln_gpl for v in p['valeurs']]
    t = tol[(e['source'], e['id'], e['rang'])]
    ln_dep = math.log(e['G3'] / d) - ln_gpl
    sortie.append({'source': e['source'], 'id': e['id'], 'rang': e['rang'], 'delta': e['delta'], 'tolerance': t,
                   'q_depose': ln_dep, 'q_variantes': q, 'hors': sum(1 for x in q if abs(x) > t),
                   'q_min': min(q), 'q_max': max(q), 'q_med': statistics.median(q)})
    if (i + 1) % 20 == 0:
        print('  %d/%d' % (i + 1, len(E)), flush=True)
json.dump({'etats': sortie}, open(SORTIE, 'w'), indent=1, sort_keys=True)
print('ETATS', len(sortie))
n_ge1 = sum(1 for s in sortie if s['hors'] > 0)
print('etats ou AU MOINS UNE des 18 variantes sort de la tolerance E1 :', n_ge1)
print('etats ou la MEDIANE des variantes sort de la tolerance :', sum(1 for s in sortie if abs(s['q_med']) > s['tolerance']))
print('etats ou la regle deposee sort de la tolerance :', sum(1 for s in sortie if abs(s['q_depose']) > s['tolerance']))
print('plus petite marge |q| / tolerance, regle deposee : %.4f ; mediane des variantes : %.4f' % (
    max(abs(s['q_depose']) / s['tolerance'] for s in sortie), max(abs(s['q_med']) / s['tolerance'] for s in sortie)))
print()
print('par cellule : n etats, sur 18 variantes : nombre total hors tolerance / (18 n) ; plus grand |q| de toutes les variantes / tolerance')
cel = {}
for s in sortie:
    cel.setdefault((s['source'], s['id']), []).append(s)
for key, S in sorted(cel.items(), key=lambda kv: kv[1][0]['delta']):
    tot = sum(s['hors'] for s in S)
    mx = max(max(abs(s['q_min']), abs(s['q_max'])) / s['tolerance'] for s in S)
    print('  %-8s %-3s delta %+.4f n=%2d  hors %3d/%3d  (%.1f %%)  pire variante / tolerance = %.2f' % (key[0], key[1], S[0]['delta'], len(S), tot, 18 * len(S), 100.0 * tot / (18 * len(S)), mx))
print()
for s in cel[('delta100', 'BP')]:
    print('  BP rang %2d : deposee %+.4f ; variantes de %+.4f a %+.4f (mediane %+.4f) ; %d/18 hors tolerance %.2f' % (
        s['rang'], s['q_depose'], s['q_min'], s['q_max'], s['q_med'], s['hors'], s['tolerance']))
