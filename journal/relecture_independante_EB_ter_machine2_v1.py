# -*- coding: ascii -*-
"""RELECTURE INDEPENDANTE du run juge du gel E-B ter (432319b9feb34b82) par MA feuille (feuille_independante_ter_machine2_v1.py, 0 desaccord a la certification) :
elle lit les douze sonde_ter_point_*.json du dossier du run et le depot, rejuge chaque etat, chaque point, la cascade et la consigne (e), et COMPARE a verdict_ter.json de la feuille
de machine 1 (statut par etat, par point, comptes, verdict, issue). Elle calcule aussi ce que l'acte de machine 1 devra lire : les annonces A-1 a A-10 (gel, section 11), par MA lecture,
non opposable ; l'acte est celui de machine 1. Aucun calcul 2D. Seuils de la comparaison, declares avant : zero ecart de statut, de comptes, de verdict, d'issue ; Gamma_pl a 1e-12 relatif.
Usage : py -3.11 -I relecture_independante_EB_ter_machine2_v1.py <dossier du run> <sonde_ordre2.json> <sortie.json>"""
import glob
import json
import math
import os
import statistics
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import feuille_independante_ter_machine2_v1 as MA

RUN, DEPOT, SORTIE = [os.path.abspath(a) for a in sys.argv[1:4]]
dep = {p['id']: p for p in json.load(open(DEPOT))['points']}
v1 = json.load(open(os.path.join(RUN, 'verdict_ter.json')))
vi = json.load(open(os.path.join(RUN, 'verdict_ter_instrument.json')))
pts = {}
for f in sorted(glob.glob(os.path.join(RUN, 'sonde_ter_point_*.json'))):
    s = json.load(open(f))
    for p in s['points']:
        pts[p['id']] = p
ecarts = []
etats = []
for i in MA.JUGES:
    for e in sorted(pts[i]['etats'], key=lambda x: x['rang']):
        g = dep[i]['etats'][[x['rang'] for x in dep[i]['etats']].index(e['rang'])]['Gamma_2D']['3']
        j = MA.juger_etat(e['traj'], g)
        etats.append((i, e['rang'], g, j))
        theirs = [x for x in v1['points'][i]['etats'] if x['rang'] == e['rang']][0]
        if theirs['statut'] != j['statut'] or theirs['lu_sur_le_plateau'] != j['lu']:
            ecarts.append((i, e['rang'], theirs['statut'], j['statut']))
        for x in 'ABCD':
            tp = theirs['plateaux'][x]
            mp = j['plateaux'][x]
            if tp['statut'] != mp['statut'] or ('k0' in tp and (tp['k0'] != mp['k0'] or abs(tp['Gamma_pl'] / mp['Gamma_pl'] - 1.0) > 1e-12)):
                ecarts.append((i, e['rang'], x, tp['statut'], mp['statut']))
lus = {i: [j for (ii, r, g, j) in etats if ii == i and r == 0][0]['statut'] for i in MA.JUGES}
nj = len(etats)
nq = sum(1 for t in etats if t[3]['statut'] == 'QUALIFIE')
npl = sum(1 for t in etats if t[3]['lu'] is not None)
nlu = sum(1 for t in etats if t[3]['lu'] is True)
verdict = MA.cascade(vi['instrument'] == 'TIENT', lus, nj, nq)
issue = MA.issue_consigne(npl, nlu)
print('MA RELECTURE : %d etats, %d QUALIFIES ; etats lus QUALIFIES : %d sur 12 ; consigne (e) : %d sur %d' % (nj, nq, sum(1 for s in lus.values() if s == 'QUALIFIE'), nlu, npl))
print('MA RELECTURE : VERDICT %s ; ISSUE %s' % (verdict, issue))
print('FEUILLE DE MACHINE 1 : VERDICT %s ; ISSUE %s ; %d etats juges, %d qualifies, %d a plateau sous A, %d lus sur le plateau' % (
    v1['verdict'], v1['issue_depot'], v1['n_juges'], v1['n_qualifies'], v1['n_plateau_A'], v1['n_lus_sur_le_plateau']))
ok = (verdict == v1['verdict'] and issue == v1['issue_depot'] and (nj, nq, npl, nlu) == (v1['n_juges'], v1['n_qualifies'], v1['n_plateau_A'], v1['n_lus_sur_le_plateau']) and not ecarts)
print('ECARTS DE STATUT OU DE PLATEAU ENTRE LES DEUX FEUILLES : %d ; ACCORD COMPLET : %s' % (len(ecarts), ok))
for e in ecarts[:10]:
    print('   ', e)
# ---- comptes par point, par absorbeur ; ce que l'acte lira
print('')
print('PAR POINT : etat lu, juges, QUALIFIES, NON QUALIFIES, NON LISIBLES, lecture deposee sur le plateau')
nq_par = {}
for i in MA.JUGES:
    es = [t for t in etats if t[0] == i]
    c = {s: sum(1 for t in es if t[3]['statut'] == s) for s in ('QUALIFIE', 'NON QUALIFIE', 'NON LISIBLE')}
    nq_par[i] = c['NON QUALIFIE']
    print('  %-3s %-13s %2d %2d %2d %2d   %2d sur %2d' % (i, lus[i], len(es), c['QUALIFIE'], c['NON QUALIFIE'], c['NON LISIBLE'],
                                                         sum(1 for t in es if t[3]['lu'] is True), sum(1 for t in es if t[3]['lu'] is not None)))
for t in etats:
    if t[3]['statut'] != 'QUALIFIE':
        print('  %s rang %2d %s G_dep %.3e : %s %s' % (t[0], t[1], t[3]['statut'], t[2], t[3]['echecs'], t[3]['sans_fenetre']))
sans_pl = {x: sum(1 for t in etats if t[3]['plateaux'][x]['statut'] != 'PLATEAU') for x in 'ABCD'}
print('etats sans PLATEAU par absorbeur (pas de plateau ou aucune fenetre) :', sans_pl)
et = {x: [t[3]['plateaux'][x]['etalement'] for t in etats if 'k0' in t[3]['plateaux'][x]] for x in 'ABCD'}
for x in 'ABCD':
    print('  etalement de la meilleure fenetre sous %s : mediane %.4f, plus grand %.4f' % (x, statistics.median(et[x]), max(et[x])))
acc = {}
for x in 'BCD':
    acc[x] = [abs(math.log(t[3]['plateaux'][x]['Gamma_pl'] / t[3]['plateaux']['A']['Gamma_pl'])) for t in etats
              if t[3]['plateaux']['A']['statut'] == 'PLATEAU' and t[3]['plateaux'][x]['statut'] == 'PLATEAU']
    print('  accord %s / A : |ln| mediane %.4f, plus grand %.4f (%d etats)' % (x, statistics.median(acc[x]), max(acc[x]), len(acc[x])))
dp = [abs(math.log(t[2] / t[3]['plateaux']['A']['Gamma_pl'])) for t in etats if t[3]['plateaux']['A']['statut'] == 'PLATEAU']
print('  consigne (e) : |ln(G_dep / Gamma_pl(A))| mediane %.4f, plus grand %.4f, au-dessus de tau : %d sur %d' % (statistics.median(dp), max(dp), sum(1 for e in dp if e > 0.05), len(dp)))
# ---- les annonces
print('')
print('LES ANNONCES (gel, section 11), par MA lecture ; non opposable')
neg = ('C1', 'C2', 'M1', 'M2', 'L1', 'L2')
A = {}
A['A-1'] = (verdict, 'ESTIMATEUR QUALIFIE 0.46, QUALIFIE A L ETAT LU 0.08, QUALIFIE PAR POINT 0.40, NON QUALIFIE 0.01, NON LISIBLE 0.01, NON CONCLUANT 0.04')
A['A-2'] = (issue, 'SUR LE PLATEAU 0.02 ; NEUF SUR DIX 0.23 ; PAS PARTOUT 0.75')
A['A-3'] = (all(lus[i] == 'QUALIFIE' for i in MA.JUGES if i != 'L3'), 'l etat lu est QUALIFIE aux onze points autres que L3 : 0.80')
mx = max(nq_par.values())
A['A-4'] = (nq_par['L3'] == mx, 'L3 compte le plus d etats non QUALIFIES, ex aequo admis : 0.55 ; non qualifies par point %s' % nq_par)
A['A-5'] = (all(t[3]['plateaux'][x]['etalement'] <= 0.02 for t in etats if t[0] in neg for x in 'AB' if 'k0' in t[3]['plateaux'][x]), 'aux six points de delta negatif, aucun etat n a, sous A ni B, de meilleure fenetre d etalement > 0.02 : 0.80')
ab = [abs(math.log(t[3]['plateaux']['B']['Gamma_pl'] / t[3]['plateaux']['A']['Gamma_pl'])) for t in etats if t[3]['plateaux']['A']['statut'] == 'PLATEAU' and t[3]['plateaux']['B']['statut'] == 'PLATEAU']
A['A-6'] = (all(e <= 0.02 for e in ab), 'a tout etat ou A et B ont un PLATEAU, |ln(Gamma_pl(B) / Gamma_pl(A))| <= 0.02 : 0.60 ; plus grand %.4f sur %d etats' % (max(ab), len(ab)))
A['A-7'] = (vi['instrument'] == 'TIENT', 'l instrument tient : 0.96')
mC = max(sans_pl.values())
A['A-8'] = ((sans_pl['C'] == mC) or mC == 0, 'C est l absorbeur sous lequel le plus d etats n ont pas de PLATEAU, ex aequo admis, zero partout vrai : 0.70 ; %s' % sans_pl)
med = statistics.median(dp)
A['A-9'] = (0.01 <= med <= 0.04, 'la mediane de |ln(G_dep / Gamma_pl(A))| est entre 0.01 et 0.04 : 0.75 ; elle vaut %.4f' % med)
nl_ = sum(1 for t in etats if t[3]['statut'] == 'NON LISIBLE')
A['A-10'] = (nl_ <= 3, 'trois etats au plus NON LISIBLES : 0.80 ; il y en a %d' % nl_)
for k, (v, txt) in A.items():
    print('  %-5s %-40s %s' % (k, str(v), txt))
json.dump({'verdict_ma': verdict, 'issue_ma': issue, 'verdict_m1': v1['verdict'], 'issue_m1': v1['issue_depot'], 'accord_complet': bool(ok), 'ecarts': ecarts, 'comptes': [nj, nq, npl, nlu],
           'annonces': {k: [str(v), t] for k, (v, t) in A.items()}}, open(SORTIE, 'w'), indent=1, default=str)
sys.exit(0 if ok else 1)
