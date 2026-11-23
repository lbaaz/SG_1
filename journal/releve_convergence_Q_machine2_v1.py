# -*- coding: ascii -*-
"""RELEVE (lecture seule, aucun calcul) de la qualite de convergence des 480 lectures de la qualification Q : cinq points x fantome et jumeau x quatre absorbeurs x douze barreaux.
Pour chaque fichier lect2D_Q*_{fantome,jumeau}.json : nombre de lectures suivies, iterations maximales, residu maximal, nombre de "decalage_repris", poids du site (0, 0) minimal et maximal sur les lectures suivies du fantome ;
puis l'etendue plate de Gamma sous A (barreaux consecutifs ou |Gamma / Gamma_pl - 1| <= 0.005, Gamma_pl = plateau de A rendu par la feuille deposee, recalcule ici par la meme routine importee).
Usage : py -3.11 -P releve_convergence_Q_machine2_v1.py <dossier des lect2D_Q*.json> <feuille deposee lecture_lecteur_gel_loi_machine1_v1.py>"""
import importlib.util
import json
import os
import sys

DOS, FEUILLE = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location('feuille', FEUILLE)
FE = importlib.util.module_from_spec(spec)
spec.loader.exec_module(FE)
KS = list(range(-3, 9))
tot_suivi = tot = 0
print('%-4s %-7s %-12s %-8s %-12s %-10s %-22s' % ('pt', 'qui', 'suivies/48', 'iter max', 'residu max', 'decalages', 'poids du site min..max'))
for ident in ('Qa', 'Qc', 'Qd', 'Qe', 'Qf'):
    for qui in ('fantome', 'jumeau'):
        t = json.load(open(os.path.join(DOS, 'lect2D_%s_%s.json' % (ident, qui))))['lecture']['traj']
        L = [t[x][str(k)] for x in 'ABCD' for k in KS]
        S = [r for r in L if r['suivi']]
        tot_suivi += len(S)
        tot += len(L)
        pw = [r['poids_site'] for r in S if r['poids_site'] is not None]
        print('%-4s %-7s %-12s %-8d %-12.1e %-10d %.4f .. %.4f' % (ident, qui, '%d/48' % len(S), max(r['iterations'] for r in S), max(r['residu'] for r in S), sum(1 for r in S if r['decalage_repris']), min(pw), max(pw)))
print('lectures suivies : %d sur %d' % (tot_suivi, tot))
print('\netendue plate sous A (fantome) : barreaux k consecutifs ou |Gamma(k) / Gamma_pl - 1| <= 0.005')
for ident in ('Qa', 'Qc', 'Qd', 'Qe', 'Qf'):
    t = json.load(open(os.path.join(DOS, 'lect2D_%s_fantome.json' % ident)))['lecture']['traj']
    J = FE.juger_etat({x: t[x] for x in 'ABCD'}, None)
    gp = J['plateaux']['A']['Gamma_pl']
    plat = [k for k in KS if t['A'][str(k)]['suivi'] and t['A'][str(k)]['gamma'] and abs(t['A'][str(k)]['gamma'] / gp - 1) <= 0.005]
    print('%-3s A : k = %s (%d barreaux consecutifs : %s)' % (ident, plat, len(plat), 'oui' if plat == list(range(plat[0], plat[-1] + 1)) else 'NON'))
