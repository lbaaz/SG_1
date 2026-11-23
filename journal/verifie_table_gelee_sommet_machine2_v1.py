# -*- coding: ascii -*-
"""CERTIFICATION (a), (b) et (e) du gel "SOMMET", seconde partie (piece 81a2febcfce49007, lot a2dc5cb2b9c3da0d) : sa TABLE GELEE (table_cellules_gel_sommet_v1.json, 4238e2b262119f83) contre MES calculs, a pleine precision.
 (a) SON tirage (graine 114565) = LE MIEN : les 8 w2 et les 56 cellules (w2, kappa, profondeur, g, eta0, r_c) contre le journal de MON tirage (tirage_graine_114565_sommet_machine2_v1.log, fait AVANT de lire sa table gelee) ;
 (b) les PREDICTIONS (etendue, ln G3*, poids) contre MA table (detail_machine2_sommet_v1.json) aux 56 cellules ; et le tableau imprime de la section 3 de la piece (g, eta0, r_c, G3* a quatre chiffres, etendue a quatre decimales) contre sa table JSON ;
 (e) les NEUF TEMOINS POSITIFS : leurs g, eta0, r_c, m contre mes fichiers de travail de Q et de Q2 (jobs_Q_machine2_v1.txt, jobs_Q2_machine2_v1.txt) ; leur plateau de reference contre le plateau que la feuille deposee rend sur MES sorties (Q_sorties, Q2_sorties) ; le canon de mon pilote et le canon du bloc dans mes JSON.
Usage : py -3.11 -I verifie_table_gelee_sommet_machine2_v1.py <dossier du lot de machine 1> <ma table detail JSON> <mon journal de tirage> <ma piece de travail : dossier certif_relecteur_machine2> <feuille deposee> <la piece .md de la seconde partie>"""
import hashlib
import importlib.util
import json
import math
import os
import re
import sys
import unicodedata
from fractions import Fraction as F

LOT, DETAIL, TIRAGE, RELECT, FEUILLE, PIECE = sys.argv[1:7]
t = json.load(open(os.path.join(LOT, 'table_cellules_gel_sommet_v1.json')))
det = json.load(open(DETAIL))
txt = open(TIRAGE, encoding='ascii').read()
spec = importlib.util.spec_from_file_location('feuille', FEUILLE)
FE = importlib.util.module_from_spec(spec)
spec.loader.exec_module(FE)


def canon_B(chemin):
    s = unicodedata.normalize('NFC', open(chemin, 'rb').read().decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n')
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


print('(a) SON TIRAGE CONTRE LE MIEN')
mes_w2 = {m[0] + m[1]: m[2] for m in re.findall(r'=> (MP|PP|MG|PG)([ab]) : w2 = (\S+) =', txt)}
sien = {c + 'ab'[i]: w for c, ws in t['w2_tires'].items() for i, w in enumerate(ws)}
print('    huit w2 : miens %s' % mes_w2)
print('    huit w2 : siens %s' % sien)
print('    identiques : %s' % ('OUI' if mes_w2 == sien and len(sien) == 8 else 'NON'))
mes_c = {m[0] + m[1] + m[2]: (m[3], m[4], m[5], m[6]) for m in re.findall(r'(MP|PP|MG|PG)([ab])(\d)\s+kappa ([0-9.]+)\s+g = ([0-9.e+-]+)\s+eta0 = ([0-9.e+-]+)\s+r_c = (\d+)', txt)}
dif = []
pire_delta = 0.0
for c in t['cellules']:
    cle = c['id']
    mine = mes_c.get(cle)
    w2 = F(c['w2'])
    if mine != (c['kappa'], c['g'], c['eta0'], str(c['r_c'])) or mes_w2.get(cle[:3]) != c['w2']:
        dif.append(cle)
    pire_delta = max(pire_delta, abs(c['delta'] - float(w2 - 2)))
    if c['tolerance'] != 0.01 or c['boite'] != c['r_c'] + 100:
        dif.append(cle + ' (tolerance ou boite)')
print('    56 cellules : %d dans sa table, %d dans mon journal ; differences (w2, kappa, g, eta0, r_c, tolerance 0.01, boite = r_c + 100) : %s ; plus grand ecart de delta : %.1e' % (len(t['cellules']), len(mes_c), dif or 'AUCUNE', pire_delta))
ok_a = mes_w2 == sien and not dif and len(t['cellules']) == 56 == len(mes_c)
print('(a) %s\n' % ('TIENT' if ok_a else 'NE TIENT PAS'))

print('(b) SES PREDICTIONS CONTRE MA TABLE (calculee de sa piece de gel, partie 1, avant la graine)')
cle_creneau = {'MP': 'MP', 'PP': 'PP', 'MG': 'MG', 'PG': 'PG'}
pe = pl = pw = 0.0
mb_ko = []
for c in t['cellules']:
    nom = c['id'][:2]
    k = round(abs(float(F(c['w2'])) - 2.0) * 100000)
    r = det['%s|%d' % (nom, k)]
    assert F(r['w2']) == F(c['w2'])
    mc = [x for x in r['cellules'] if x['kappa'] == c['kappa']][0]
    pe = max(pe, abs(mc['etendue'] - c['etendue']))
    pl = max(pl, abs(mc['ln_plateau'] - c['ln_G3']))
    pw = max(pw, abs(mc['poids_site0_min'] - c['poids_min_chaine']))
    if mc['m_bord'] != c['m'] or mc['r_c'] != c['r_c'] or mc['g'] != c['g'] or mc['eta0'] != c['eta0']:
        mb_ko.append(c['id'])
print('    56 cellules : plus grand ecart etendue %.2e ; ln G3* %.2e ; poids du site 0 %.2e ; m, r_c, g, eta0 differents : %s' % (pe, pl, pw, mb_ko or 'AUCUN'))
ok_b = pe < 1e-9 and pl < 1e-9 and not mb_ko
# tableau imprime de la section 3 de la piece
piece = open(PIECE, encoding='ascii').read()
lig = re.findall(r'^\s+((?:MP|PP|MG|PG)[ab]\d)\s+(\S+)\s+([+-][0-9.]+)\s+([0-9.]+)\s+(\d)\s+([0-9.e+-]+)\s+([0-9.e+-]+)\s+(\d+)\s+([0-9.e+-]+)\s+([0-9.]+)\s*$', piece, re.M)
imp_ko = []
for (cid, w2, dl, kp, m, g, e, rc, g3, et) in lig:
    c = [x for x in t['cellules'] if x['id'] == cid][0]
    if not (w2 == c['w2'] and kp == c['kappa'] and int(m) == c['m'] and g == c['g'] and e == c['eta0'] and int(rc) == c['r_c'] and g3 == ('%.3e' % math.exp(c['ln_G3'])) and et == ('%.4f' % c['etendue']) and dl == ('%+.5f' % c['delta'])):
        imp_ko.append(cid)
print('    tableau imprime de la section 3 de la piece : %d lignes lues ; differentes de sa table JSON (w2, delta, kappa, m, g, eta0, r_c, G3* a quatre chiffres, etendue) : %s' % (len(lig), imp_ko or 'AUCUNE'))
ok_b = ok_b and len(lig) == 56 and not imp_ko
print('(b) %s\n' % ('TIENT' if ok_b else 'NE TIENT PAS'))

print('(e) LES NEUF TEMOINS POSITIFS ET LE PILOTE DE LECTURE')
jobs = {}
for f in ('jobs_Q_machine2_v1.txt', 'jobs_Q2_machine2_v1.txt'):
    for l in open(os.path.join(RELECT, f), encoding='ascii'):
        p = l.split()
        if p and p[5] == '-1':
            jobs[p[0]] = (p[1], p[2], p[3], p[4], p[6])
ko = []
pr = 0.0
for w in t['temoins_positifs']:
    j = jobs[w['id']]
    if (j[0], j[1], int(j[2]), j[3], int(j[4])) != (w['w2'], w['g'], w['m'], w['eta0'], w['r_c']):
        ko.append((w['id'], j, w))
    dos = os.path.join(RELECT, 'Q2_sorties' if w['id'].startswith('Q2') else 'Q_sorties')
    traj = json.load(open(os.path.join(dos, 'lect2D_%s_fantome.json' % w['id'])))['lecture']['traj']
    gp = FE.juger_etat({x: traj[x] for x in 'ABCD'}, None)['plateaux']['A']['Gamma_pl']
    pr = max(pr, abs(math.log(gp) - w['ln_Gamma_pl_reference']))
print('    9 temoins : g, eta0, r_c, m, w2 contre mes fichiers de travail : differences %s ; plus grand ecart du ln du plateau de reference a celui que la feuille deposee rend sur mes sorties : %.2e' % (ko or 'AUCUNE', pr))
can_p = canon_B(os.path.join(RELECT, 'lecteur_2D_pilote_machine2_v1.py'))
blocs = set()
for d in ('Q_sorties', 'Q2_sorties'):
    for f in os.listdir(os.path.join(RELECT, d)):
        if f.endswith('_fantome.json') or f.endswith('_jumeau.json'):
            j = json.load(open(os.path.join(RELECT, d, f)))
            blocs.add((j['pilote_canon'], j['bloc_sha256_16'], j['source_bloc_canon'], j['moteur_canon']))
print('    canon de MON pilote : %s ; ses canons dans la table : pilote %s, bloc %s, source %s, moteur %s' % (can_p, t['regle']['pilote_machine2_canon'], t['regle']['bloc_sha256_16'], t['regle']['source_bloc_canon'], t['regle']['moteur_canon']))
print('    ce que mes dix-huit fichiers de Q et de Q2 portent (pilote, bloc, source, moteur) : %s' % sorted(blocs))
ok_e = (not ko and pr < 1e-9 and can_p == t['regle']['pilote_machine2_canon'] == '47a84eae6052f006'
        and blocs == {('47a84eae6052f006', t['regle']['bloc_sha256_16'], t['regle']['source_bloc_canon'], t['regle']['moteur_canon'])})
print('(e) %s' % ('TIENT' if ok_e else 'NE TIENT PAS'))
print('\nRESUME : (a) %s ; (b) %s ; (e) %s' % ('TIENT' if ok_a else 'NON', 'TIENT' if ok_b else 'NON', 'TIENT' if ok_e else 'NON'))
