# -*- coding: ascii -*-
"""VERIFICATION DES NOMBRES du gel (section 15 (d)) -- machine 2, 2026-11-16. Chaque nombre de la section 3 (cellules), 4.5 (131 / 56), 6 (|ln(G3/G2)| predits), 7.1 (classes de e_bord),
7.2 (regularites), 7.3 (marges) est LU dans le texte du gel par expression reguliere (jamais recopie) et RECALCULE de mon cote : mes chaines (feuille_independante_gel_loi_machine2_v1.py),
mon evaluateur de cellule (controle_carte_machine2/cellule_machine2_v1.py, 1D seulement : AUCUNE 2D aux cellules), ma feuille sur les points deja joues (retro_machine2_v1.json),
la feuille du gel ter pour relire le plateau des ancres. Les REGLES de calcul des marges sont celles du texte du gel (7.3) ; ou le texte est muet, celle du script de machine 1 est suivie
et consignee comme telle ('regle de m1').
Usage : py -3.11 -P verification_nombres_gel_machine2_v1.py <moteur> <bloc2> <ordre3_machine2_v1.py> <gel.md> <table du gel.json> <retro_machine2.json> <table_retrospective.json> <depot.json> <feuille ter.py> <reference ancres.json> <sortie.json>"""
import importlib.util
import json
import math
import re
import sys
from fractions import Fraction as F

MOTEUR, BLOC2, SCRIPT3, GEL, TABLE, RETRO, TRETRO, DEPOT, FTER, REFANC, SORTIE = sys.argv[1:12]
sys.argv = [sys.argv[0], MOTEUR, BLOC2, SCRIPT3]
spec = importlib.util.spec_from_file_location('feuille_independante', 'feuille_independante_gel_loi_machine2_v1.py')
MINE = importlib.util.module_from_spec(spec)
spec.loader.exec_module(MINE)
MINE.charger(MOTEUR, BLOC2, SCRIPT3)
spec = importlib.util.spec_from_file_location('cellule', '../controle_carte_machine2/cellule_machine2_v1.py')
CEL = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CEL)
spec = importlib.util.spec_from_file_location('feuille_ter', FTER)
FT = importlib.util.module_from_spec(spec)
spec.loader.exec_module(FT)

gel = open(GEL, encoding='ascii').read()
res = []


def ctl(nom, ok, detail):
    res.append({'controle': nom, 'tient': bool(ok), 'detail': detail})
    print('%-5s %-6s %s' % (nom, 'TIENT' if ok else 'MORD', detail), flush=True)


def med(x):
    x = sorted(x)
    n = len(x)
    return x[n // 2] if n % 2 else 0.5 * (x[n // 2 - 1] + x[n // 2])


T = {p['id']: p for p in json.load(open(TABLE))['points']}
CELLS = [i for i in ('N1', 'N2', 'N3', 'N4', 'N5', 'P1', 'P2', 'P3', 'P4', 'P5', 'BN', 'BP')]

# ---------- mes chaines aux douze cellules (1D, etiquettes PREDITES) ----------
mine = {}
for i in CELLS:
    w2, fac = F(T[i]['w2']), F(T[i]['facteur'])
    mine[i] = CEL.evalue(w2, fac)
    print('  cellule %s evaluee (1D) : N %d, g %.4e' % (i, mine[i]['N'], mine[i]['g']), flush=True)

# ---------- N01 : section 3 ----------
motif3 = re.compile(r'^\s+(N[1-5]|P[1-5]|BN|BP)\s+w2 = (\S+)\s+delta ([+-]\d\.\d+)\s+x(\S+)\s+g = (\S+)\s+N = (\d+)\s+predits\s+(\d+) /\s*(\d+) /\s*(\d+)\s*$', re.M)
l3 = {m.group(1): m for m in motif3.finditer(gel)}
bad = []
for i in CELLS:
    m = l3.get(i)
    if m is None:
        bad.append('%s absente du texte' % i)
        continue
    c = mine[i]
    jug, dom = c['compte'][0], c['compte'][1]
    att = (F(m.group(2)), F(m.group(4)), float(m.group(3)), float(m.group(5)), int(m.group(6)), int(m.group(7)), int(m.group(8)), int(m.group(9)))
    mon = (F(T[i]['w2']), F(T[i]['facteur']), round(c['delta'], 3), c['g'], c['N'], jug, dom, jug - dom)
    if att[0] != mon[0] or att[1] != mon[1] or abs(att[2] - mon[2]) > 5e-4 or abs(att[3] / mon[3] - 1) > 1e-3 or att[4:] != mon[4:]:
        bad.append('%s : texte %s, moi %s' % (i, att, mon))
ctl('N01', not bad and len(l3) == 12, 'section 3 : douze cellules (w2, delta, facteur, g a 4 chiffres, boite N, jugeables / domaine / hors) = mon evaluateur 1D : %s' % (bad or 'toutes'))

# ---------- feuille retrospective (mes sorties) ----------
R = json.load(open(RETRO))
TR = {p['id']: p for p in json.load(open(TRETRO))['points']}
dom_etats = []          # (point, delta, ln_q3, ln(G3/G2), e_bord)
n_jug = n_dom = n_pres = n_stab_excl = n_e07 = 0
for c in R['cellules']:
    d = float(F(TR[c['id']]['w2'])) - 2.0
    for e in c['etats']:
        if e['exclu'] is not None:
            continue
        n_jug += 1
        if e['e_bord'] < 0.7:
            n_e07 += 1
        if e['domaine']:
            n_dom += 1
            n_pres += e['pres']
            dom_etats.append((c['id'], d, e['ln_q3'], math.log(e['G3'] / e['G2']), e['e_bord']))
        elif e['e_bord'] < 0.7:
            n_stab_excl += 1
ctl('N02', n_jug == 131 and n_dom == 56 and sum(c['n_lus'] for c in R['cellules']) == 137,
    'section 4.5 : 137 etats lus, 131 juges, 56 dans le domaine sur les douze points du delta 98 (ma feuille : %d lus, %d juges, %d domaine)' % (sum(c['n_lus'] for c in R['cellules']), n_jug, n_dom))
ctl('N03', n_pres == 56 and n_e07 == 83 and n_stab_excl == 27,
    "sections 7.1 et E-1 : ordre 3 plus pres que l'ordre 2 a %d des %d etats du domaine ; %d etats juges de e_bord < 0.7 dont %d exclus par la stabilite (texte : 56/56, 83, 27)" % (n_pres, n_dom, n_e07, n_stab_excl))

# ---------- N04 : 7.1 classes ----------
cl = {}
for nom, lo, hi in (('0', 0.0, 0.3), ('1', 0.3, 0.5), ('2', 0.5, 0.7)):
    v = [abs(x[2]) for x in dom_etats if lo <= x[4] < hi]
    cl[nom] = (len(v), med(v), max(v))
txt = {}
for m in re.finditer(r'e_bord dans \[([\d.]+), ([\d.]+)\[\s+(\d+) etats\s+mediane ([\d.]+)\s+plus grand ([\d.]+)', gel):
    txt[m.group(1)] = (int(m.group(3)), float(m.group(4)), float(m.group(5)))
att = {'0': txt.get('0.0'), '1': txt.get('0.3'), '2': txt.get('0.5')}
okc = all(att[k] and att[k][0] == cl[k][0] and abs(att[k][1] - cl[k][1]) < 5.1e-5 and abs(att[k][2] - cl[k][2]) < 5.1e-5 for k in cl)
ctl('N04', okc, '7.1 : classes de e_bord (nombre, mediane, plus grand |ln q3|) : moi %s ; texte %s' % (
    {k: (v[0], round(v[1], 4), round(v[2], 4)) for k, v in cl.items()}, att))

# ---------- ancres (plateau de la reference de machine 1) ----------
DEP = {p['id']: p for p in json.load(open(DEPOT))['points']}
REF = {p['id']: p for p in json.load(open(REFANC))['points']}
anc = []
for pid in ('A1', 'A2'):
    p = DEP[pid]
    w2 = F(p['w2'])
    lus = {e['rang']: e for e in REF[pid]['etats']}
    for e in p['etats']:
        G3d = e['Gamma_2D']['3']
        if G3d <= 1.33e-12:
            continue
        c = MINE.chaines(w2, p['g'], e['n1'], e['n2'])
        if c['vide'] or not (c['stable1'] and c['stable2']):
            continue
        dans = bool(c['e_bord'] < 0.7 and c['stab3'] is not None and c['stab3'] <= 0.05)
        pl = None
        if e['rang'] in lus:
            j = FT.juger_etat(lus[e['rang']]['traj'], G3d)
            if j['statut'] == 'QUALIFIE' and 'Gamma_pl' in j['plateaux']['A']:
                pl = float(j['plateaux']['A']['Gamma_pl'])
        anc.append({'id': pid, 'delta': float(w2) - 2.0, 'rang': e['rang'], 'dans': dans, 'e_bord': c['e_bord'], 'ln_q3': math.log(c['G3'] / pl) if pl else None, 'd32': math.log(c['G3'] / c['G2'])})
a1 = sorted([x['ln_q3'] for x in anc if x['id'] == 'A1' and x['ln_q3'] is not None and x['dans']])
a2 = sorted([x['ln_q3'] for x in anc if x['id'] == 'A2' and x['ln_q3'] is not None and x['dans']])
m71 = re.search(r'a A1 \(delta = -0\.05\), ln q3 = ([+-][\d.]+) et ([+-][\d.]+) ; a A2 \(delta =\s+\+0\.05\), ln q3 = ([+-][\d.]+) et ([+-][\d.]+)', gel)
ta1 = sorted([float(m71.group(1)), float(m71.group(2))])
ta2 = sorted([float(m71.group(3)), float(m71.group(4))])
ctl('N05', len(a1) == 2 and len(a2) == 2 and all(abs(x - y) < 5.1e-5 for x, y in zip(a1, ta1)) and all(abs(x - y) < 5.1e-5 for x, y in zip(a2, ta2)),
    '7.1 : ln q3 aux deux etats lus des ancres : moi A1 %s A2 %s ; texte A1 %s A2 %s' % ([round(x, 4) for x in a1], [round(x, 4) for x in a2], ta1, ta2))

# ---------- N06 : 7.2 ----------
neg = [(x[0], x[1], x[2], x[3], x[4]) for x in dom_etats if x[1] < 0] + [(x['id'], x['delta'], x['ln_q3'], x['d32'], x['e_bord']) for x in anc if x['ln_q3'] is not None and x['dans'] and x['delta'] < 0]
pos = [(x[0], x[1], x[2], x[3], x[4]) for x in dom_etats if x[1] > 0] + [(x['id'], x['delta'], x['ln_q3'], x['d32'], x['e_bord']) for x in anc if x['ln_q3'] is not None and x['dans'] and x['delta'] > 0]
neg_k = [x for x in neg if abs(x[3]) >= 0.05]
ks = [-x[2] / x[3] ** 2 for x in neg_k]
K_MED, K_MAX, K_MIN = med(ks), max(ks), min(ks)
c2 = [x[2] / x[1] ** 2 for x in pos]
c3 = [x[2] / x[1] ** 3 for x in pos]
mon72 = (len(neg), sum(x[2] < 0 for x in neg), len(neg_k), round(K_MIN, 2), round(K_MED, 2), round(K_MAX, 2), len(pos), round(med(c2), 1), round(max(c2), 1), round(med(c3)), round(max(c3)))
m1 = re.search(r'A delta < 0 \((\d+) etats[^)]*\), ln q3 est negatif a (\d+) etats sur (\d+)', gel)
m2 = re.search(r'Aux (\d+) etats ou la correction d\'ordre 3 se lit[^,]*, k = [^v]*vaut de ([\d.]+) a ([\d.]+), mediane ([\d.]+)', gel, re.S)
m3 = re.search(r'A delta > 0 \((\d+) etats[^)]*\), ln q3 est positif partout ; ln q3 / delta\^2 vaut au plus\s+([\d.]+) \(mediane ([\d.]+)\), ln q3 / delta\^3 au plus (\d+) \(mediane (\d+)\)', gel, re.S)
txt72 = (int(m1.group(1)), int(m1.group(2)), int(m2.group(1)), float(m2.group(2)), float(m2.group(4)), float(m2.group(3)), int(m3.group(1)), float(m3.group(3)), float(m3.group(2)), int(m3.group(5)), int(m3.group(4)))
ctl('N06', mon72 == txt72 and all(x[2] > 0 for x in pos),
    '7.2 : delta<0 : etats / negatifs / lus pour k / k min, mediane, max ; delta>0 : etats, c2 mediane et max, c3 mediane et max : moi %s ; texte %s ; ln q3 positif partout a delta>0 : %s' % (mon72, txt72, all(x[2] > 0 for x in pos)))
E_VU = max(x[4] for x in neg + pos)
ctl('N07', abs(E_VU - 0.603) < 5.1e-4, '7.3 : plus grand e_bord d un etat du domaine aux points joues : moi %.4f, texte 0.603' % E_VU)

# ---------- N08 : 7.3 les marges (regles du texte ; regle de m1 la ou le texte est muet) ----------
C2_MED, C2_MAX, C3_MED, C3_MAX = med(c2), max(c2), med(c3), max(c3)
motif73 = re.compile(r'^\s+(N[1-5]|P[1-5]|BN|BP)\s+domaine\s+(\d+) \(\s*(\d+) a 0\.05\)\s+e_bord ([\d.]+) a ([\d.]+)\s+ln\(G3/G2\) ([+-][\d.]+)\s+attente ([\d.]+)\s+marge ([\d.]+)\s*$', re.M)
l73 = {m.group(1): m for m in motif73.finditer(gel)}
bad, sortie73 = [], {}
n_au_dela = {}
for i in CELLS:
    c = mine[i]
    d = c['delta']
    dom = [e for e in c['etats'][:14] if e.get('domaine')]
    for e in dom:
        e['_T'] = 0.05 if e['e_bord'] < 0.3 else 0.10
        e['_d32'] = math.log(e['G3'] / e['G2'][2])
    if d < 0:                                               # regle de m1 : k le plus defavorable x (ln(G3/G2))^2 etat par etat ; marge = min des T / attente
        att_etats = [K_MAX * e['_d32'] ** 2 for e in dom]
        attente = max(att_etats)
        marge = min(e['_T'] / a for e, a in zip(dom, att_etats))
    else:                                                   # regle de m1 : puissance 3, plus grand coefficient ; marge = plus petit T du domaine / attente
        attente = C3_MAX * d ** 3
        marge = min(e['_T'] for e in dom) / attente
    n_au_dela[i] = sum(e['e_bord'] > E_VU for e in dom)
    mm = l73.get(i)
    sortie73[i] = {'domaine': len(dom), 'T_bas': sum(e['_T'] == 0.05 for e in dom), 'e_bord': (min(e['e_bord'] for e in dom), max(e['e_bord'] for e in dom)), 'd32_med': med([e['_d32'] for e in dom]), 'attente': attente, 'marge': marge}
    if mm is None:
        bad.append('%s absente du texte' % i)
        continue
    if (len(dom) != int(mm.group(2)) or sortie73[i]['T_bas'] != int(mm.group(3)) or abs(min(e['e_bord'] for e in dom) - float(mm.group(4))) > 5.1e-4
            or abs(max(e['e_bord'] for e in dom) - float(mm.group(5))) > 5.1e-4 or abs(sortie73[i]['d32_med'] - float(mm.group(6))) > 5.1e-5
            or abs(attente - float(mm.group(7))) > 5.1e-5 or abs(marge - float(mm.group(8))) > 5.1e-3):
        bad.append('%s : texte %s ; moi %s' % (i, mm.groups()[1:], (len(dom), sortie73[i]['T_bas'], round(sortie73[i]['e_bord'][0], 3), round(sortie73[i]['e_bord'][1], 3), round(sortie73[i]['d32_med'], 4), round(attente, 4), round(marge, 2))))
ctl('N08', not bad and len(l73) == 12, '7.3 : douze lignes (etats du domaine, a T = 0.05, e_bord extremes, ln(G3/G2) median, attente, marge) recalculees de mes chaines : %s' % (bad or 'toutes'))
ctl('N09', n_au_dela['N1'] == 3 and n_au_dela['BP'] == 2 and sum(n_au_dela.values()) == 5,
    '7.3 : etats predits du domaine au-dela du plus grand e_bord vu (%.3f) : N1 %d, BP %d, total %d (texte : 3 a N1, 2 a BP, 5)' % (E_VU, n_au_dela['N1'], n_au_dela['BP'], sum(n_au_dela.values())))
# E2 a N1 : "sous la valeur la plus defavorable de k, l'ordre 2 serait plus pres que l'ordre 3 a 4 etats sur 11"
c = mine['N1']
dom = [e for e in c['etats'][:14] if e.get('domaine')]
n2 = 0
for e in dom:
    a = K_MAX * math.log(e['G3'] / e['G2'][2]) ** 2
    d32 = math.log(e['G3'] / e['G2'][2])
    n2 += a > abs(-a - d32)
ctl('N10', n2 == 4 and len(dom) == 11, "7.3 : N1, sous k = %.2f, l'ordre 2 est plus pres que l'ordre 3 a %d etats sur %d (texte : 4 sur 11)" % (K_MAX, n2, len(dom)))
# P : |ln(G3/G2)| aux etiquettes predites : 0.014 a 0.019 ; N : 0.066 a 0.164
pp = [abs(math.log(e['G3'] / e['G2'][2])) for i in ('P1', 'P2', 'P3', 'P4', 'P5') for e in mine[i]['etats'][:14] if e.get('domaine')]
nn = [abs(math.log(e['G3'] / e['G2'][2])) for i in ('N1', 'N2', 'N3', 'N4', 'N5') for e in mine[i]['etats'][:14] if e.get('domaine')]
ctl('N11', abs(min(pp) - 0.014) < 6e-4 and abs(max(pp) - 0.019) < 6e-4 and abs(min(nn) - 0.066) < 6e-4 and abs(max(nn) - 0.164) < 6e-4,
    "section 6 : |ln(G3/G2)| aux etiquettes predites : ligne P de %.3f a %.3f (texte 0.014 a 0.019), ligne N de %.3f a %.3f (texte 0.066 a 0.164)" % (min(pp), max(pp), min(nn), max(nn)))
n_tot = sum(mine[i]['compte'][0] for i in CELLS)
ctl('N12', n_tot == 149, "section 12 : etats predits jugeables aux douze cellules : %d (texte : 149 au-dessus de dix planchers)" % n_tot)
print('BILAN : %d controles, %d tiennent' % (len(res), sum(r['tient'] for r in res)))
json.dump({'controles': res, 'marges': sortie73, 'k_max': K_MAX, 'c3_max': C3_MAX, 'e_vu': E_VU}, open(SORTIE, 'w'), indent=1, sort_keys=True, default=str)
sys.exit(0 if all(r['tient'] for r in res) else 1)
