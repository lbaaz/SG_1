# -*- coding: ascii -*-
"""Compare, cellule par cellule, le verdict de la feuille de m1 (celle du pilote, verdict_vide.json) et celui de MA feuille (feuille_vide_machine2_v1.py, canon a6754241629160a7,
ecrite depuis le texte du gel) sur les MEMES sorties brutes du run unique (run_gel_vide_machine2/run_1). Aucune donnee n'est modifiee.
Usage : py -3.11 -I compare_feuilles_run_1_machine2_v1.py"""
import json
import math

A = json.load(open(r'd:\devs\bocal\BOCAL4\run_gel_vide_machine2\run_1\verdict_vide.json'))
B = json.load(open(r'd:\devs\bocal\BOCAL4\resultats_run_vide_machine2\verdict_vide_feuille_machine2.json'))
print('verdict m1 :', A['verdict'], '| verdict m2 :', B['verdict'], '| identiques :', A['verdict'] == B['verdict'])
for k in ('V1', 'VP'):
    print('  %s : issue m1 %s / m2 %s ; comptes m1 %s / m2 %s ; identiques : %s' % (k, A[k]['issue'], B[k]['issue'], A[k]['comptes'], B[k]['comptes'], A[k]['issue'] == B[k]['issue'] and A[k]['comptes'] == B[k]['comptes']))
print('  instrument m1 %s / m2 %s ; incomplet m1 %s / m2 %s ; prevol m1 %s / m2 %s' % (A['instrument'], B['instrument'], A['incomplet'], B['incomplet'], A['prevol'], B['prevol']))
ca = {c['id']: c for c in A['cellules']}
cb = {c['id']: c for c in B['cellules']}
assert sorted(ca) == sorted(cb) and len(ca) == 28, 'cellules differentes'
mauv = []
pire = {'ln_q': 0.0, 'bande': 0.0, 'etalement': 0.0, 'ln_Gamma_pl': 0.0}
for i in sorted(ca, key=lambda s: (['MG', 'MP', 'PP', 'PG'].index(s[:2]), int(s[2:]))):
    a, b = ca[i], cb[i]
    # ln q de m1 : repris du jugement ; chercher le champ
    lq_a = a.get('ln_q')
    lg_a = a.get('ln_Gamma_pl')
    if lq_a is None or lg_a is None:
        # m1 range ces nombres sous un autre nom : on cherche les cles numeriques de premier niveau
        raise SystemExit('champs ln_q / ln_Gamma_pl absents chez m1 : cles = %s' % sorted(a.keys()))
    d = {'ln_q': abs(lq_a - b['ln_q']), 'bande': abs(a['bande'] - b['bande']), 'etalement': abs(a['etalement_du_lecteur'] - b['etalement_du_lecteur']), 'ln_Gamma_pl': abs(lg_a - b['ln_Gamma_pl'])}
    for k in d:
        pire[k] = max(pire[k], d[k])
    ok = a['jugement'] == b['jugement'] and a['lecteur']['statut'] == b['lecteur']['statut'] == 'QUALIFIE' and a['temoin']['tient'] == b['temoin']['tient'] is True
    if not ok:
        mauv.append((i, a['jugement'], b['jugement']))
print('cellules comparees :', len(ca), '; jugements, statuts du lecteur et temoins identiques :', 28 - len(mauv), 'sur 28')
print('ecart max entre les deux feuilles : ln q %.2e ; bande %.2e ; etalement %.2e ; ln Gamma_pl %.2e' % (pire['ln_q'], pire['bande'], pire['etalement'], pire['ln_Gamma_pl']))
print('DESACCORDS :', mauv)
