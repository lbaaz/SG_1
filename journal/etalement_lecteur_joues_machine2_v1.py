# -*- coding: ascii -*-
"""ETALEMENT DU LECTEUR s AUX ETATS DEJA JOUES (run 'loi de la largeur, ordre 3', delta 100) : la grandeur dont depend que V1 puisse conclure (section 5 du gel : bande b = etendue + s, TIENT si |ln q| <= T - b).
m1 ecrit (7.3) 'L'etalement du lecteur au vide n'est pas connu'. Je le mesure la ou le lecteur creux a deja lu le fantome : les 12 fichiers sonde_ter_point_*.json de MON run du delta 100 (donnees EXISTANTES, aucune lecture neuve).
Pour chaque etat lu : j'applique juger_etat de la feuille DEPOSEE du lecteur (canon 83701094e6a2b965) aux quatre trajectoires ; s = max(ln(1 + etalement du plateau sous A), |ln(plateau B/A)|, |ln(plateau C/A)|, |ln(plateau D/A)|),
exactement comme la feuille du gel du vide. Sont comptes : les etats QUALIFIES (statut du lecteur) et, parmi eux, la repartition de s.
Usage : py -3.11 -I etalement_lecteur_joues_machine2_v1.py"""
import glob
import importlib.util
import json
import math
import os
import statistics as st

R = r'd:\devs\bocal\BOCAL4\run_gel_loi_ordre3'
FL = r'd:\devs\bocal\BOCAL4\livraison_16a_gel_loi_partie2\ext\lot_m1\lecture_lecteur_gel_loi_machine1_v1.py'    # canon 83701094e6a2b965
spec = importlib.util.spec_from_file_location('feuille_lecteur', FL)
L = importlib.util.module_from_spec(spec)
spec.loader.exec_module(L)
lignes = []
n_etats = n_q = 0
statuts = {}
for p in sorted(glob.glob(os.path.join(R, 'sonde_ter_point_*.json'))):
    S = json.load(open(p))
    cell = os.path.basename(p)[len('sonde_ter_point_'):-5]
    for pt in S['points'] if isinstance(S['points'], list) else S['points'].values():
        etats = pt.get('etats') or []
        for e in etats:
            tr = e.get('traj')
            if not tr or sorted(tr) != ['A', 'B', 'C', 'D']:
                continue
            n_etats += 1
            j = L.juger_etat(tr, None)
            statuts[j['statut']] = statuts.get(j['statut'], 0) + 1
            if j['statut'] != 'QUALIFIE':
                continue
            n_q += 1
            P = j['plateaux']
            s = max([math.log(1.0 + P['A']['etalement'])] + [P[x]['ecart_ln_A'] for x in 'BCD'])
            lignes.append({'cellule': cell, 'rang': e.get('rang'), 'etat': (e.get('n1'), e.get('n2')), 's': s, 'etal_A': P['A']['etalement'], 'ecart_max': max(P[x]['ecart_ln_A'] for x in 'BCD'), 'Gamma_pl': P['A']['Gamma_pl']})
print('etats lus (quatre trajectoires) :', n_etats, '; statuts du lecteur :', statuts, '; QUALIFIES :', n_q)
v = sorted(x['s'] for x in lignes)
q = lambda f: v[min(len(v) - 1, int(f * len(v)))]
print('s (etalement du lecteur) : min %.4f ; mediane %.4f ; q25 %.4f ; q75 %.4f ; q90 %.4f ; max %.4f' % (v[0], st.median(v), q(0.25), q(0.75), q(0.90), v[-1]))
for seuil, quoi in ((0.005, 'tres petit'), (0.008, 'PG6 pourrait tenir a |ln q| = 0.005'), (0.0100, 'dix-millieme'), (0.0130, 'T - etendue min : une cellule ne peut tenir qu en dessous'), (0.0187, 'T - etendue max'), (0.02, 'T')):
    print('  part des etats QUALIFIES avec s <= %.4f (%s) : %.1f %% (%d sur %d)' % (seuil, quoi, 100.0 * sum(1 for x in v if x <= seuil) / len(v), sum(1 for x in v if x <= seuil), len(v)))
print('composantes : etalement du plateau sous A (ln(1+etal)) : mediane %.4f ; max %.4f ; ecart max a B, C, D : mediane %.4f ; max %.4f' % (
    st.median(math.log(1 + x['etal_A']) for x in lignes), max(math.log(1 + x['etal_A']) for x in lignes), st.median(x['ecart_max'] for x in lignes), max(x['ecart_max'] for x in lignes)))
print('par cellule : nombre d etats QUALIFIES, s median')
par = {}
for x in lignes:
    par.setdefault(x['cellule'], []).append(x['s'])
for k in sorted(par):
    print('   %-3s %3d etats ; s median %.4f ; min %.4f ; max %.4f' % (k, len(par[k]), st.median(par[k]), min(par[k]), max(par[k])))
json.dump({'etats': lignes}, open(r'd:\devs\bocal\BOCAL4\certif_gel_vide_partie2_machine2\etalement_lecteur_joues_machine2_v1.json', 'w', newline='\n'), indent=1, sort_keys=True)
