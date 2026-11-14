# -*- coding: ascii -*-
"""LECTURE DES RESULTATS DE LA NUIT E-B BIS -- machine 2, 2026-11-13. NE MESURE RIEN, NE JUGE RIEN : relit les JSON ecrits
par la sonde v3 et la feuille v2 (dossier nuit_EB_bis/sortie) et ecrit (1) les trajectoires Gamma_k / G_run de l'etat 0
a chaque (point, configuration), (2) le comptage des annonces A-1 a A-8 DU GEL a partir des champs du verdict (A-6 a A-8
sont des comptes de l'acte : ils sont ici lus dans les JSON, jamais tapes), (3) le controle que l'etat 0 est suivi a
chaque barreau de l'etage 2 (recouvrement ov). La regle de plateau est celle de la feuille (importee, jamais recopiee).
Usage depuis BOCAL4 : python -P lecture_resultat_nuit_EB_bis_machine2_v1.py > nuit_EB_bis/lecture_resultat_machine2_v1.log"""
import importlib.util
import json
import math
import os
import sys

sys.dont_write_bytecode = True
ICI = os.path.dirname(os.path.abspath(__file__))
S = os.path.join(ICI, 'nuit_EB_bis', 'sortie')
FEUILLE = os.path.join(ICI, 'nuit_EB_bis', 'scripts', 'lecture_qualification_EB_machine1_v2.py')
sys.argv = [FEUILLE]
spec = importlib.util.spec_from_file_location('feuille', FEUILLE)
F = importlib.util.module_from_spec(spec)
spec.loader.exec_module(F)

s2 = json.load(open(os.path.join(S, 'sonde_etage2.json'), encoding='ascii'))
v1 = json.load(open(os.path.join(S, 'verdict_etage1.json'), encoding='ascii'))
vq = json.load(open(os.path.join(S, 'verdict_qualification_EB.json'), encoding='ascii'))
det = vq['detail']
ORDRE = ['39_20', '197_100', '99_50', '101_50', '203_100', '41_20']
CFG = ['F1G20', 'F1G30', 'F1GT', 'F2G20', 'F3G20']
f1 = [(n, det['points'][n]['plateaux']['F1G20']) for n in ORDRE if det['points'][n]['plateaux']['F1G20']['statut'] == 'PLATEAU']

print('LECTURE DES RESULTATS -- nuit E-B bis -- gel %s, sonde v3 (etage 2) moteur %s' % (s2['gel'], s2['moteur']))
print('plateforme : %s' % json.dumps(s2['plateforme'], sort_keys=True))
print('verdict de la qualification (feuille v2) : %s ; E_run %.4f' % (vq['verdict'], det['E_run']))
print('')
print('1. Gamma(k) / G_run de l\'etat 0, k = %d .. %d (-- : non lisible) ; G_run = valeur lue par M17 (barreau k = 3)'
      % (F.K_MIN, F.K_MAX))
for n in ORDRE:
    p = s2['points'][n]
    G = p['G_run']
    print('== point %s  G_run %.4e' % (n, G))
    for c in CFG:
        se = F.serie(p['cfg'][c]['traj'])
        row = ' '.join(('%d:%.3f' % (k, se[k] / G)) if se.get(k) else ('%d:--' % k) for k in sorted(se))
        pl = det['points'][n]['plateaux'][c]
        print('  %-6s N=%d identite %.4f | %s' % (c, p['cfg'][c]['N'], p['cfg'][c]['identite'], row))
        print('         feuille : %-15s k0 %2d etalement %.4f Gamma_pl %.4e' % (pl['statut'], pl['k0'], pl['etalement'], pl['Gamma_pl']))
print('')
print('1b. Verifications des phrases de la note')
for n in ORDRE:
    p = s2['points'][n]
    s20, s30 = F.serie(p['cfg']['F1G20']['traj']), F.serie(p['cfg']['F1G30']['traj'])
    ec = max(abs(s30[k] / s20[k] - 1.0) for k in range(-5, 3))
    r3 = s20[3] / p['G_run']
    r04 = [s20[k] / p['G_run'] for k in range(0, 5)]
    r58 = [s20[k] / p['G_run'] for k in range(-5, 0)]
    print('   %-8s F1G30/F1G20 - 1, k=-5..2 : plus grand ecart %.4f ; F1G20 k=3 : %.6f x G_run ; k=0..4 : %.3f a %.3f ; '
          'k=-5..-1 : %.3f a %.3f' % (n, ec, r3, min(r04), max(r04), min(r58), max(r58)))
for n, p in f1:
    for c in ('F1G30', 'F1GT'):
        e = det['points'][n]['plateaux'][c].get('ecart_ln_F1G20')
        print('   accord %s / F1G20 au point %s : |ln| = %s (seuil %.2f)' % (c, n, ('%.4f' % e) if e is not None else 'non joue', F.TAU_F))
print('')
print('2. Etat 0 SUIVI a chaque barreau de l\'etage 2, et plus petit recouvrement lu')
nbad, nov, ovmin = 0, 0, 1.0
for n in ORDRE:
    for c in CFG:
        for k, r in s2['points'][n]['cfg'][c]['traj'].items():
            e = r['etats'][0]
            nov += 1
            if not e.get('suivi'):
                nbad += 1
            if e.get('ov') is not None:
                ovmin = min(ovmin, e['ov'])
print('   %d trajectoires (point, configuration, k) ; non suivies : %d ; plus petit recouvrement lu : %.9f' % (nov, nbad, ovmin))
print('')
print('3. Les annonces du gel (section 11), lues dans les JSON')
print('   A-1 verdict : %s (annonce a 0.27 pour NON QUALIFIE)' % vq['verdict'])
print('   statuts des six points : %s' % ' ; '.join('%s %s' % (n, det['points'][n]['statut']) for n in ORDRE))
nq = [n for n in ORDRE if det['points'][n]['statut'] == 'QUALIFIE']
print('   points QUALIFIES : %d %s' % (len(nq), nq))
print('   feuille : %s' % json.dumps(det['annonces'], sort_keys=True))
print('   A-6 : etage 1 = %s ; TP aux quatre configurations : %s' % (v1['etage1'], ' '.join(
    '%s/%s:%s' % (j, c, 'TIENT' if v1['detail']['TP'][j][c]['tient'] else 'NE TIENT PAS')
    for j in ('j06', 'j08') for c in ('F1G20', 'F1G30'))))
print('   A-7 : points avec PLATEAU a (F1, G20) : %d %s' % (len(f1), ['%s k0=%d' % (n, p['k0']) for n, p in f1]))
if f1:
    print('         k0 >= -1 a chacun : %s' % all(p['k0'] >= -1 for _, p in f1))
print('   A-8 : consigne 6 (e) aux points a PLATEAU (F1, G20) : %s' % [(n, det['points'][n]['M17_sur_plateau']) for n, _ in f1])
for n, p in f1:
    G = s2['points'][n]['G_run']
    print('         %s : |ln(G_run / Gamma_pl)| = %.4f (seuil %.2f)' % (n, abs(math.log(G / p['Gamma_pl'])), F.TAU_F))
print('   T-etats : S_w lus %d sur 6 ; nombre de plateaux par point : %s ; mediane %s' % (
    sum(1 for n in ORDRE if det['T_etats'][n]['S_w'] is not None), {n: det['T_etats'][n]['n_plateaux'] for n in ORDRE},
    det['mediane_S_w']))
print('')
print('4. Plateaux par configuration (feuille) : nombre de PLATEAU sur six points')
for c in CFG:
    print('   %-6s %d sur 6' % (c, sum(1 for n in ORDRE if det['points'][n]['plateaux'][c]['statut'] == 'PLATEAU')))
print('')
print('CE QUE CE LOG NE JOUE PAS : aucune decomposition, aucune mesure, aucun jugement : il relit.')
