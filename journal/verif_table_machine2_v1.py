# -*- coding: ascii -*-
"""(a) La table gelee porte-t-elle les douze cellules de MON tirage (graine 200482, rang 0) et les deux ancres ? Lit mon journal de tirage et le sien, la table, la table de pre-vol, le depot."""
import json, re, sys, hashlib, unicodedata
from fractions import Fraction as F
LOT = 'livraison_16a_gel_loi_partie2/ext/lot_m1/'
def canon(p):
    t = unicodedata.normalize('NFC', open(p, 'rb').read().decode('utf-8')).replace('\r\n', '\n')
    return hashlib.sha256(t.encode()).hexdigest()[:16]
res = []
def ctl(n, ok, d):
    res.append(ok); print('%-4s %-6s %s' % (n, 'TIENT' if ok else 'MORD', d))
T = json.load(open(LOT + 'table_points_gel_loi_ordre3_v1.json'))
P = json.load(open(LOT + 'table_points_prevol_gel_loi_ordre3_v1.json'))
mine = {}
for l in open('controle_carte_machine2/tirage_graine_200482_machine2_v1.log'):
    m = re.match(r'\s*(N[1-5]|P[1-5]|BN|BP)\s+w2 = (\S+) \(([\d.]+)\) facteur (\S+)\s*$', l)
    if m: mine[m.group(1)] = (F(m.group(2)), F(m.group(4)))
his = {}
for l in open(LOT + 'tirage_machine1_v1_graine_200482.log'):
    m = re.match(r'\s+(N[1-5]|P[1-5]|BN|BP)\s+w2 = (\S+)\s+facteur (\S+)\s*$', l)
    if m: his[m.group(1)] = (F(m.group(2)), F(m.group(3)))
tab = {p['id']: (F(p['w2']), F(p['facteur'])) for p in T['points'] if p['role'] == 'juge'}
ctl('T01', len(mine) == 12 and mine == tab, 'les douze cellules de la table gelee = celles de MON journal de tirage (graine 200482) : %d / %d' % (sum(mine.get(k) == v for k, v in tab.items()), len(tab)))
ctl('T02', his == tab == mine, 'et = celles du journal de tirage de machine 1 (son script lance par lui) : %d / %d' % (sum(his.get(k) == v for k, v in tab.items()), len(tab)))
ctl('T03', T['graine'] == '200482' and T['rang'] == 0 and T['prevol'] is False, 'graine %r, rang %r, prevol %r' % (T['graine'], T['rang'], T['prevol']))
anc = {p['id']: (F(p['w2']), F(p['facteur']), p['role']) for p in T['points'] if p['role'] == 'ancre'}
D = {p['id']: p for p in json.load(open('C:/Users/bazil/AppData/Local/Temp/claude/75adcc7f3c1d08bf/7d33635e-8345-4a2c-a69e-f6a51f9d8fa7/scratchpad/reg_neuf98/journal/sonde_ordre2.json'))['points']}
ctl('T04', sorted(anc) == ['A1', 'A2'] and all(anc[i][0] == F(D[i]['w2']) and anc[i][1] == F(D[i]['facteur']) for i in anc), 'les deux ancres A1, A2 de la table = celles du depot du delta 98 (w2, facteur) : %s' % {i: (str(anc[i][0]), str(anc[i][1])) for i in anc})
ids = [p['id'] for p in T['points']]
ctl('T05', ids == ['N1','N2','N3','N4','N5','P1','P2','P3','P4','P5','BN','BP','A1','A2'] and [p['creneau'] for p in T['points'][:12]] == ['N']*5+['P']*5+['BN','BP'], 'quatorze points, creneaux N x5, P x5, BN, BP ; ordre : %s' % ids)
pj = [p for p in P['points'] if p['role'] == 'juge']
ctl('T06', len(pj) == 1 and pj[0]['id'] == 'C3' and F(pj[0]['w2']) == F(D['C3']['w2']) and F(pj[0]['facteur']) == F(D['C3']['facteur']) and [p['id'] for p in P['points'] if p['role'] == 'ancre'] == ['A1', 'A2'] and P['prevol'] is True,
    'table de pre-vol : un seul point juge, C3 (w2 %s, facteur %s = le depot), et A1, A2 ; prevol vrai' % (pj[0]['w2'], pj[0]['facteur']))
ctl('T07', canon(LOT + 'table_points_gel_loi_ordre3_v1.json') == '35fa7b73f2b7f8eb' and canon(LOT + 'table_points_prevol_gel_loi_ordre3_v1.json') == 'a29225df977dfe41', 'canons des deux tables : 35fa7b73f2b7f8eb et a29225df977dfe41')
print('BILAN : %d controles, %d tiennent' % (len(res), sum(res)))
sys.exit(0 if all(res) else 1)
