# -*- coding: ascii -*-
"""Confrontation etat par etat : ma feuille (retro_machine2_v1.json) contre la feuille retrospective de machine 1 (feuille_ordre3_retrospective_v1.json), memes entrees."""
import json, math, sys
mine = json.load(open(sys.argv[1])); his = json.load(open(sys.argv[2]))
M = {c['id']: c for c in mine['cellules']}; H = {c['id']: c for c in his['cellules']}
assert sorted(M) == sorted(H), (sorted(M), sorted(H))
pire = {k: 0.0 for k in ('G2', 'G3', 'e_bord', 'stab3', 'ln_q2', 'ln_q3')}
dif_cell, dif_etat, n, n_dom, marge_stab, marge_e = [], [], 0, 0, 9.9, 9.9
for i in sorted(M):
    m, h = M[i], H[i]
    for k in ('n_lus', 'n_juges', 'n_domaine', 'n_hors', 'exploitable', 'E1', 'E2', 'E3'):
        if m[k] != h[k]:
            dif_cell.append((i, k, m[k], h[k]))
    if m['n_pres'] != h['n_ordre3_plus_pres'] or m['seuil_E2'] != h['seuil_E2']:
        dif_cell.append((i, 'n_pres/seuil', (m['n_pres'], m['seuil_E2']), (h['n_ordre3_plus_pres'], h['seuil_E2'])))
    hh = {e['rang']: e for e in h['etats']}
    for e in m['etats']:
        x = hh[e['rang']]
        if e['exclu'] != x['exclu']:
            dif_etat.append((i, e['rang'], 'exclu', e['exclu'], x['exclu']))
            continue
        if e['exclu'] is not None:
            continue
        n += 1
        if bool(e['domaine']) != bool(x['dans_le_domaine']):
            dif_etat.append((i, e['rang'], 'domaine', e['domaine'], x['dans_le_domaine']))
        n_dom += bool(e['domaine'])
        for k, kk in (('G2', 'G2'), ('G3', 'G3'), ('e_bord', 'e_bord')):
            pire[k] = max(pire[k], abs(e[k] / x[kk] - 1.0))
        if e['stab3'] is not None and x['stab3'] is not None:
            pire['stab3'] = max(pire['stab3'], abs(e['stab3'] - x['stab3']))
        pire['ln_q2'] = max(pire['ln_q2'], abs(e['ln_q2'] - x['ln_q2']))
        if e['ln_q3'] is not None and x['ln_q3'] is not None:
            pire['ln_q3'] = max(pire['ln_q3'], abs(e['ln_q3'] - x['ln_q3']))
        if e['stab3'] is not None:
            marge_stab = min(marge_stab, abs(e['stab3'] - 0.05))
        marge_e = min(marge_e, abs(e['e_bord'] - 0.7), abs(e['e_bord'] - 0.3))
for k in ('E1', 'E2', 'E1B', 'E3'):
    a = mine[k][0]; b = his[k]['issue']
    if a != b:
        dif_cell.append(('global', k, a, b))
print('cellules : %d ; etats juges compares : %d (dont %d dans le domaine)' % (len(M), n, n_dom))
print('differences de cellule ou d\'issue : %d %s' % (len(dif_cell), dif_cell[:6]))
print('differences d\'etat (exclusion, domaine) : %d %s' % (len(dif_etat), dif_etat[:6]))
print('ecarts relatifs maximaux : G2 %.2e, G3 %.2e, e_bord %.2e ; ecarts absolus maximaux : stab3 %.2e, ln q2 %.2e, ln q3 %.2e' % (pire['G2'], pire['G3'], pire['e_bord'], pire['stab3'], pire['ln_q2'], pire['ln_q3']))
print('plus petite marge d\'un etat juge a une garde : |stab3 - 0.05| %.2e ; |e_bord - 0.3 ou 0.7| %.2e' % (marge_stab, marge_e))
sys.exit(0 if not dif_cell and not dif_etat else 1)
