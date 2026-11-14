# -*- coding: ascii -*-
"""compare_rejeu_chaine_EA_machine2_v1 : hors chaine, classe 3, machine 2. Compare MON rejeu de comparaison_par_etat_machine1_v1.py
(chaine_EA_rejeu/point_<num>_<den>.log, six points) aux journaux A et B de machine 1 (comparaison_par_etat_machine1_v1_{A,B}.log),
et applique les trois regles de morsure de la note 9322566db2546adb, 3.2 : (1) un etat lu different ; (2) un rapport chaine/2D hors de
[0.50, 1.64] sur un etat au-dessus de dix planchers (1.33e-12 x 10) ; (3) un ecart-type de J au-dessus de 0.2. Ne mesure rien.
Usage depuis BOCAL4 : python -P chaine_EA_rejeu/compare_rejeu_chaine_EA_machine2_v1.py"""
import glob
import os
import re
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = 'chaine_EA_rejeu/'
PLANCHER10 = 1.33e-12 * 10      # "dix planchers" du script de machine 1 : g2 > 1.33e-12 (le texte dit dix planchers = 1.33e-12 : seuil du script)
SEUIL = 1.33e-12                # le seuil que le script de machine 1 applique (g2 > 1.33e-12)


def lire(txt):
    pts, cur = {}, None
    for ln in txt.splitlines():
        m = re.match(r'^POINT w2=(\S+)', ln)
        if m:
            cur = m.group(1)
            pts[cur] = {'rows': []}
            continue
        m = re.match(r'^\s*(\d+)\s+(0\.\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+([0-9.]+)\s+([0-9.e+-]+)\s+([0-9.e+-]+)\s+([0-9.]+|nan)\s+([0-9.]+|nan)(.*)$', ln)
        if m and cur:
            pts[cur]['rows'].append(dict(rang=int(m.group(1)), n1=int(m.group(3)), n2=int(m.group(4)), sj=float(m.group(6)), g2=float(m.group(7)),
                                         gc=float(m.group(8)), q=float(m.group(10)), sous='sous 10 planchers' in m.group(11)))
        m = re.match(r'^BILAN w2=(\S+) .*marge du rang 0 sur le rang 1 : ([0-9.]+)', ln)
        if m:
            pts[m.group(1)]['marge'] = float(m.group(2))
    return pts


M1 = {}
for n in 'AB':
    M1.update(lire(open(D + 'comparaison_par_etat_machine1_v1_%s.log' % n, encoding='utf-8').read()))
M2 = {}
for f in sorted(glob.glob(D + 'point_*_*.log')):
    M2.update(lire(open(f, encoding='utf-8').read()))
ORDRE = ['39/20', '197/100', '99/50', '101/50', '203/100', '41/20']
print('REJEU machine 2 de comparaison_par_etat_machine1_v1.py (4eaef82543e4f76f) contre les journaux A et B de machine 1')
tous, mem_etat, mem_marge = [], True, True
for p in ORDRE:
    a, b = M1[p], M2[p]
    id_ = [(x['rang'], x['n1'], x['n2']) for x in a['rows']] == [(x['rang'], x['n1'], x['n2']) for x in b['rows']]
    mem_etat = mem_etat and id_ and (a['rows'][0]['n1'], a['rows'][0]['n2']) == (b['rows'][0]['n1'], b['rows'][0]['n2'])
    mem_marge = mem_marge and a['marge'] == b['marge']
    g = [(x, y) for x, y in zip(a['rows'], b['rows']) if y['g2'] > SEUIL]
    tous += [(p, y) for _, y in g]
    print('  %-8s rangs et etiquettes identiques : %s ; etat lu (%d,%d) ; marge rang 0 / rang 1 : m1 %.4f, m2 %.4f ; %d etats au-dessus du seuil' % (
        p, id_, b['rows'][0]['n1'], b['rows'][0]['n2'], a['marge'], b['marge'], len(g)))
print('(1) etat lu different : %s' % ('AUCUN : memes rangs, memes etiquettes, memes marges aux six points' if mem_etat and mem_marge else 'OUI'))
q = [y['q'] for _, y in tous]
bas = [(p, y['n1'], y['n2'], y['q']) for p, y in tous if y['q'] < 0.50 or y['q'] > 1.64]
q1 = [y['q'] for p in ORDRE for y in M1[p]['rows'] if y['g2'] > SEUIL]
print('(2) %d etats-points au-dessus du seuil ; chaine/2D de %.3f a %.3f chez moi, de %.3f a %.3f chez machine 1 ; hors [0.50, 1.64] : %s' % (
    len(q), min(q), max(q), min(q1), max(q1), [(p, '(%d,%d)' % (n1, n2), x) for p, n1, n2, x in bas]))
sj = max(y['sj'] for p in ORDRE for y in M2[p]['rows'] if y['g2'] > SEUIL)
print('(3) plus grand ecart-type de J sur ces etats : %.3f (regle : 0.2)' % sj)
for s in (1e-11, 1e-10, 1e-9):
    d = [abs(x['g2'] / y['g2'] - 1) for p in ORDRE for x, y in zip(M1[p]['rows'], M2[p]['rows']) if y['g2'] > s]
    print('Gamma_2D machine 1 / machine 2 : %d etats au-dessus de %.0e, ecart relatif max %.2e' % (len(d), s, max(d)))
print('plus grand ecart absolu Gamma_2D, tous les etats : %.2e' % max(abs(x['g2'] - y['g2']) for p in ORDRE for x, y in zip(M1[p]['rows'], M2[p]['rows'])))
print('')
print('BISSECTION (resonant seul), mon rejeu de bissection_chaine_2D_machine1_v2.py contre le journal de machine 1 :')
for w, f in (('39/20', '39_20'), ('101/50', '101_50'), ('41/20', '41_20')):
    v = {}
    for ln in open(D + 'bissection_%s.log' % f, encoding='utf-8'):
        m = re.match(r'^(complet|resonant)\s+Gamma=([0-9.e+-]+)', ln)
        if m:
            v[m.group(1)] = float(m.group(2))
    t1, cur, v1 = open(D + 'bissection_chaine_2D_machine1_v2.log', encoding='utf-8').read(), None, {}
    for ln in t1.splitlines():
        m = re.match(r'^w2=(\S+)', ln)
        if m:
            cur = m.group(1)
        m = re.match(r'^(complet|resonant)\s+Gamma=([0-9.e+-]+)', ln)
        if m and cur == w:
            v1[m.group(1)] = float(m.group(2))
    if 'complet' not in v1:       # le journal de bissection de machine 1 n'a pas de ligne 'complet' a 1.95 : son Gamma_2D lu du journal A (rang 0)
        v1['complet'] = M1[w]['rows'][0]['g2']
        print('  (%s : pas de ligne "complet" dans le journal de bissection de machine 1 ; je prends le Gamma_2D lu, rang 0, du journal A)' % w)
    print('  %-7s complet m2 %.4e (m1 %.4e) ; resonant m2 %.4e (m1 %.4e) ; complet / resonant : m2 %.3f, m1 %.3f' % (
        w, v['complet'], v1['complet'], v['resonant'], v1['resonant'], v['complet'] / v['resonant'], v1['complet'] / v1['resonant']))
print('')
print('CE QUE CE LOG NE JOUE PAS : aucune decomposition, aucune mesure ; il relit des journaux.')
