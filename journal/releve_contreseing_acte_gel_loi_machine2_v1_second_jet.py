# -*- coding: ascii -*-
"""RELEVE DU CONTRESEING de machine 2 -- acte du run du gel "loi de la largeur, ordre 3" (projet v1 de machine 1, canon a3f7d5d6809dcfe5). 2026-11-16.
Chaque nombre de l'acte est LU dans l'acte (expression reguliere) puis REFAIT depuis les fichiers du run (verdict d'ordre 3, verdict du lecteur, sortie dense, journal du pilote, gel, table) par mon propre code ;
rien n'est repris des scripts de machine 1. Un controle MORD si un nombre de l'acte ne se retrouve pas. Les controles sont fins (un id par famille de nombres) pour que la contre-epreuve sache lequel doit mordre.
Usage : py -3.11 -P releve_contreseing_acte_gel_loi_machine2_v1.py <acte.md> <sortie.json> [--sans-fichiers-m1]"""
import difflib
import hashlib
import json
import math
import os
import re
import statistics
import sys
import unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
B4 = os.path.dirname(ICI)
RUN = os.path.join(B4, 'run_gel_loi_ordre3')
L2 = os.path.join(B4, 'livraison_16a_gel_loi_partie2', 'ext', 'lot_m1')
L1 = os.path.join(B4, 'livraison_15g_gel_loi_partie1', 'lot_m1')
M1 = os.path.join(B4, 'livraison_16b_acte_gel_loi_ordre3', 'ext', 'lot_m1')
CERT = os.path.join(B4, 'certif_gel_loi_partie2_machine2')
GEL2 = os.path.join(L2, 'gel_loi_ordre3_partie2_instrument_enonces_pre_enregistrement_v1.md')
ACTE, SORTIE = sys.argv[1], sys.argv[2]
RES = []


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
    except UnicodeDecodeError:
        t = raw
    return hashlib.sha256(t).hexdigest()[:16]


def canon(p):
    return emp(open(p, 'rb').read())


def ctl(cid, ok, msg):
    RES.append((cid, bool(ok), msg))
    print('%-5s %-5s %s' % (cid, 'TIENT' if ok else 'MORD', msg), flush=True)


def norm(s):
    return ' '.join(s.split())


def grab(motif, texte, cid, nom, flags=0):
    m = re.search(motif, texte, flags)
    if not m:
        ctl(cid, False, '%s : phrase introuvable dans l\'acte (motif %r)' % (nom, motif[:70]))
        return None
    return m


act_brut = open(ACTE, encoding='ascii', newline='').read()
act = act_brut.replace('\r\n', '\n')
T = norm(act)
gel = norm(open(GEL2, encoding='ascii').read())
V3 = json.load(open(os.path.join(RUN, 'verdict_ordre3.json')))
VT = json.load(open(os.path.join(RUN, 'verdict_ter.json')))
DENSE = json.load(open(os.path.join(RUN, 'sonde_dense.json')))
LOGP = open(os.path.join(RUN, 'pilote_gel_loi.log'), encoding='utf-8').read()
CELL = {c['id']: c for c in V3['cellules']}
ORDRE = ['N1', 'N2', 'N3', 'N4', 'N5', 'P1', 'P2', 'P3', 'P4', 'P5', 'BN', 'BP']


def iss(x):
    return x['issue'] if isinstance(x, dict) else (x[0] if isinstance(x, list) else x)


assert sorted(CELL) == sorted(ORDRE)


def jug(c):
    return [e for e in c['etats'] if e['exclu'] is None]


def dom(c):
    return [e for e in jug(c) if e['dans_le_domaine']]


def hors(c):
    return [e for e in jug(c) if not e['dans_le_domaine']]


def f4(x):
    return '%.4f' % x


def sg4(x):
    return '%+.4f' % x


# ---------------------------------------------------------------- R01 forme
ok = all(ord(ch) < 128 for ch in act) and '%' not in act
long = max(len(l) for l in act.split('\n'))
ctl('R01a', ok and act.rstrip('\n').endswith('-- FIN journal_delta_nn_loi_largeur_ordre3_v1 --'), 'ASCII, sans pour cent, plus longue ligne %d, ligne de FIN' % long)
man = open(os.path.join(os.path.dirname(M1), 'MANIFEST_lot_machine1_acte_gel_loi_ordre3_v1.txt'), encoding='utf-8').read()
cm = re.search(r'^([0-9a-f]{16})\s+\S+\s+\d+\s+\d+\s+journal_delta_nn_loi_largeur_ordre3_v1\.md', man, re.M)
ctl('R01b', cm and cm.group(1) == 'a3f7d5d6809dcfe5' and (canon(os.path.join(M1, 'journal_delta_nn_loi_largeur_ordre3_v1.md')) == 'a3f7d5d6809dcfe5' or '--sans-fichiers-m1' in sys.argv),
    'canon de l\'acte lu (fichier du lot) = manifeste = a3f7d5d6809dcfe5')

# ---------------------------------------------------------------- R02 empreintes
FICH = {
    'gel1': os.path.join(L1, 'gel_loi_ordre3_partie1_regle_tirage_pre_enregistrement_v1.md'), 'gel2': GEL2,
    'lot_cert': os.path.join(B4, 'MANIFEST_lot_machine2_certification_gel_loi_partie2_v1.txt'), 'lot_res': os.path.join(B4, 'MANIFEST_lot_machine2_resultat_gel_loi_partie2_v1.txt'),
    'note_cert': os.path.join(B4, 'POUR_MACHINE1_certification_gel_loi_partie2_machine2_v1.md'), 'note_res': os.path.join(B4, 'POUR_MACHINE1_resultat_gel_loi_partie2_machine2_v1.md'),
    'journal': os.path.join(RUN, 'pilote_gel_loi.log'), 'pilote2': os.path.join(CERT, 'pilote_gel_loi_machine2_v2.py'), 'dense': os.path.join(RUN, 'sonde_dense.json'),
    'instr': os.path.join(RUN, 'verdict_ter_instrument.json'), 'lecteur': os.path.join(RUN, 'verdict_ter.json'), 'ordre3': os.path.join(RUN, 'verdict_ordre3.json'),
    'ordre3_m1': os.path.join(M1, 'verdict_ordre3_rejoue_machine1.json'), 'lecteur_m1': os.path.join(M1, 'rejeu_machine1_verdict_ter.json'),
    'lot_m1_1': os.path.join(B4, 'livraison_15g_gel_loi_partie1', 'MANIFEST_lot_machine1_gel_loi_partie1_regle_tirage_v1.txt'),
    'lot_m1_2': os.path.join(B4, 'livraison_16a_gel_loi_partie2', 'ext', 'MANIFEST_lot_machine1_gel_loi_partie2_instrument_enonces_v1.txt'),
    'lot_cert1': os.path.join(B4, 'MANIFEST_lot_machine2_certification_gel_loi_partie1_v1.txt'), 'lot_tirage': os.path.join(B4, 'MANIFEST_lot_machine2_tirage_graine_200482_v1.txt'),
    'pilote1': os.path.join(L2, 'pilote_gel_loi_machine1_v1.py'), 'bloc3': os.path.join(L2, 'ordre3_bloc_machine1_v1.py'), 'table': os.path.join(L2, 'table_points_gel_loi_ordre3_v1.json'),
    'feuille_m2': os.path.join(CERT, 'feuille_independante_gel_loi_machine2_v1.py')}
CAN = {k: canon(p) for k, p in FICH.items()}
LIGNES = [  # (motif du libelle dans nn.12, cle)
    (r'gel, premiere partie', 'gel1'), (r'gel, seconde partie', 'gel2'), (r'certification de la seconde partie', 'lot_cert'), (r'resultat du run', 'lot_res'), (r'sa note de certification', 'note_cert'),
    (r'sa note de resultat', 'note_res'), (r'journal du pilote', 'journal'), (r'pilote joue', 'pilote2'), (r'sortie dense', 'dense'), (r'verdict de l\'instrument', 'instr'),
    (r'verdict du lecteur rejoue', 'lecteur_m1'), (r'verdict du lecteur$', 'lecteur'), (r'verdict d\'ordre 3 rejoue', 'ordre3_m1'), (r'verdict d\'ordre 3 du run', 'ordre3')]
bloc12 = act.split('nn.12 PIECES')[1] if 'nn.12 PIECES' in act else ''
mal, vus = [], 0
for l in bloc12.split('\n'):
    m = re.match(r'\s+([0-9a-f]{16}) (.+)$', l)
    if not m:
        continue
    vus += 1
    cle = next((k for p, k in LIGNES if re.search(p, m.group(2).strip())), None)
    if cle is None:
        mal.append('libelle inconnu : ' + m.group(2))
    elif CAN[cle] != m.group(1):
        mal.append('%s : acte %s, recalcule %s' % (m.group(2), m.group(1), CAN[cle]))
ctl('R02a', vus == 14 and not mal, 'nn.12 : %d empreintes lues, toutes recalculees depuis mes fichiers ; en defaut : %s' % (vus, mal))
connus = dict((CAN[k], k) for k in CAN)
connus.update({'35fa7b73f2b7f8eb': 'table', '2882de31bc49ce2f': 'pilote1', '534ba246aa3b8973': 'bloc3', 'adf4418505262df6': 'feuille_m2', '15998497f3422765': 'pilote2'})
att = {'35fa7b73f2b7f8eb': 'table', '2882de31bc49ce2f': 'pilote1', '534ba246aa3b8973': 'bloc3', 'adf4418505262df6': 'feuille_m2'}
jetons = sorted(set(re.findall(r'\b[0-9a-f]{16}\b', act)))
inconnus = [j for j in jetons if j not in connus]
ctl('R02b', not inconnus and all(CAN[att[j]] == j for j in att if j in jetons),
    '%d empreintes distinctes citees dans l\'acte, toutes retrouvees sur un de mes fichiers (table, pilote de m1, bloc 3, ma 2e feuille comprises) ; inconnues : %s' % (len(jetons), inconnus))
for lot, cle in (('4fb1dc66f96f57f6', 'lot_cert1'), ('220a0970134335e1', 'lot_tirage'), ('596a45bf6d4f97d7', 'lot_m1_1'), ('76ed746ef4db3b0c', 'lot_m1_2')):
    if lot in act:
        ctl('R02c', CAN[cle] == lot, 'lot %s cite dans nn.1 = manifeste retrouve chez moi (%s)' % (lot, CAN[cle]))

# ---------------------------------------------------------------- R03 chronologie
m = grab(r'lance le (\d{4}-\d\d-\d\d) a (\d\d:\d\d:\d\d) et fini a (\d\d:\d\d:\d\d) ; duree totale (\d+) s ; (\d+) appels, tous au code 0', T, 'R03a', 'nn.1 chronologie')
if m:
    deb = re.search(r'(\d{4}-\d\d-\d\d) (\d\d:\d\d:\d\d) PILOTE DU GEL', LOGP)
    fin = re.search(r'(\d{4}-\d\d-\d\d) (\d\d:\d\d:\d\d) FIN DU PILOTE ; duree totale (\d+) s', LOGP)
    codes = re.findall(r'code=(\d+)', LOGP)
    ctl('R03a', (m.group(1), m.group(2), m.group(3), m.group(4)) == (deb.group(1), deb.group(2), fin.group(2), fin.group(3)) and int(m.group(5)) == len(codes) and set(codes) == {'0'},
        'lance %s %s, fini %s, %s s, %d appels tous au code 0 (journal du pilote)' % (deb.group(1), deb.group(2), fin.group(2), fin.group(3), len(codes)))
m = grab(r'sonde dense (\d+) s ; les douze points du lecteur de (\d+) a (\d+) s, en parallele ; feuille d\'ordre 3 (\d+) s', T, 'R03b', 'nn.1 durees')
if m:
    dd = int(re.search(r'sonde dense\s+code=0 duree=(\d+) s', LOGP).group(1))
    pts = [int(x) for x in re.findall(r'lecteur point \w+\s+code=0 duree=(\d+) s', LOGP)]
    fo = int(re.search(r'feuille d\'ordre 3\s+code=0 duree=(\d+) s', LOGP).group(1))
    ctl('R03b', (int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))) == (dd, min(pts), max(pts), fo) and len(pts) == 12, 'durees : dense %d s ; 12 points de %d a %d s ; feuille d\'ordre 3 %d s' % (dd, min(pts), max(pts), fo))
ctl('R03c', 'table jouee : 35fa7b73f2b7f8eb, sans --prevol' in T.replace('Table jouee', 'table jouee') and 'canon table             35fa7b73f2b7f8eb' in LOGP and 'PRE-VOL' not in LOGP and '--prevol' not in LOGP.replace('sans --prevol', ''),
    'table jouee 35fa7b73f2b7f8eb dans le journal, aucun pre-vol dans le journal')
imprimes = re.findall(r'canon (\w+)\s+([0-9a-f]{16})', LOGP.split('ETAGE 1')[0])
p1 = open(FICH['pilote1'], encoding='ascii').read()
ctl('R03d', len(imprimes) == 12 and all(c in p1 or c in gel for _, c in imprimes if _ not in ('table',)),
    'les %d canons imprimes au depart sont ceux du pilote de m1 (valeurs en dur) ou du gel' % len(imprimes))
a_ = open(FICH['pilote1'], encoding='ascii').read().split('\n')
b_ = open(FICH['pilote2'], encoding='ascii').read().split('\n')
blocs = [op for op in difflib.SequenceMatcher(None, a_, b_, autojunk=False).get_opcodes() if op[0] != 'equal']
ctl('R03e', len(blocs) == 3 and 'trois blocs different' in T, 'pilote joue contre pilote de m1 : %d blocs different (l\'acte dit trois)' % len(blocs))
mt_cert = os.path.getmtime(FICH['lot_cert'])
import datetime
dt0 = datetime.datetime.strptime(deb.group(1) + ' ' + deb.group(2), '%Y-%m-%d %H:%M:%S').timestamp()
ctl('R03f', mt_cert < dt0 < mt_cert + 600, 'mon manifeste de certification (%s) precede le lancement (%s) de moins de dix minutes' % (datetime.datetime.fromtimestamp(mt_cert).strftime('%H:%M:%S'), deb.group(2)))

# ---------------------------------------------------------------- R04 instrument et lecteur
m = grab(r'2 ancres, (\d+) ecart\. Instrument du lecteur \(etage 0, ancres, etage 1\) : (\w+)\. Le lecteur a lu (\d+) etats aux douze cellules ; les (\d+) sont QUALIFIES ; son verdict de cascade, que ce gel ne juge pas, est "([A-Z ]+)"\. La lecture deposee a k = 3 est sur le plateau a (\d+) etats sur (\d+)', T, 'R04a', 'nn.2')
if m:
    nq = sum(1 for p in VT['points'].values() for e in p['etats'] if e['statut'] == 'QUALIFIE')
    nl = sum(len(p['etats']) for p in VT['points'].values())
    ctl('R04a', 'ANCRES de la sonde dense contre le depot : 2 ancres, 0 ecarts : TIENNENT' in LOGP and m.group(1) == '0' and m.group(2) == VT['instrument'] and int(m.group(3)) == nl == int(m.group(4)) == nq
        and m.group(5) == VT['verdict'] and (int(m.group(6)), int(m.group(7))) == (VT['n_lus_sur_le_plateau'], VT['n_plateau_A']), 'ancres 2/0 ; instrument %s ; %d etats lus, %d QUALIFIES ; cascade "%s" ; plateau %d sur %d' % (VT['instrument'], nl, nq, VT['verdict'], VT['n_lus_sur_le_plateau'], VT['n_plateau_A']))
m = grab(r'sortie dense (\w{16}) ; verdict de l\'instrument du lecteur (\w{16}) ; verdict du lecteur (\w{16}) ; verdict d\'ordre 3 (\w{16})\.', T, 'R04b', 'nn.2 canons')
if m:
    ctl('R04b', (m.group(1), m.group(2), m.group(3), m.group(4)) == (CAN['dense'], CAN['instr'], CAN['lecteur'], CAN['ordre3']), 'canons nn.2 recalcules')

# ---------------------------------------------------------------- R05 le tableau nn.3, cellule par cellule
for cid in ORDRE:
    c = CELL[cid]
    m = re.search(r'^\s+%s\s+(\d+) / +(\d+) / +(\d+) / +(\d+)\s+(\w+) +(\w+|-) +(\w+)\s+\|ln q3\| ([0-9.]+)\s+marge ([+-][0-9.]+)\s+\|ln q2\| ([0-9.]+)\s*$' % cid, act, re.M)
    if not m:
        ctl('R05' + cid, False, 'ligne de %s introuvable dans nn.3' % cid)
        continue
    d, j = dom(c), jug(c)
    mine = (str(len(c['etats'])), str(len(j)), str(len(d)), str(len(hors(c))), c['E1'], c['E2'] or '-', c['E3'], f4(max(abs(e['ln_q3']) for e in d)), sg4(min(e['tolerance'] - abs(e['ln_q3']) for e in d)), f4(max(abs(e['ln_q2']) for e in j)))
    ctl('R05' + cid, m.groups() == mine, '%s : acte %s ; refait %s' % (cid, ' '.join(m.groups()), ' '.join(mine)))
cs = [CELL[i] for i in ORDRE]
lig = [c for c in cs if c['creneau'] in ('N', 'P')]
brd = [c for c in cs if c['creneau'] not in ('N', 'P')]
nlus, njug, ndom, nhor = (sum(len(c['etats']) for c in cs), sum(len(jug(c)) for c in cs), sum(len(dom(c)) for c in cs), sum(len(hors(c)) for c in cs))
m = grab(r'Etats : (\d+) lus, (\d+) juges, (\d+) dans le domaine, (\d+) hors\. Trois etats lus ne sont pas juges, tous pour "barriere vide" : (.+?)\.', T, 'R06a', 'nn.3 comptes')
exc = [(c['id'], e['rang'], e['exclu']) for c in cs for e in c['etats'] if e['exclu'] is not None]   # dans l'ordre des cellules du gel
if m:
    attendu = ', '.join('%s rang %d' % (i, r) for i, r, _ in exc)
    ctl('R06a', tuple(map(int, m.groups()[:4])) == (nlus, njug, ndom, nhor) and m.group(5) == attendu and {x[2] for x in exc} == {'barriere vide'} and len(exc) == 3,
        'comptes %d/%d/%d/%d ; exclus : %s' % (nlus, njug, ndom, nhor, attendu))
m = grab(r'E1 : (\w+) \((\d+) cellules, (\d+) exploitables, aucune tombee\)\. E2 : (\w+) \((\d+) cellules, (\d+) exploitables, aucune tombee\)\. E1B : (\w+) \((\d+) cellules, (\d+) exploitables, aucune tombee\)\. E3 : (\w+) \((\d+) cellules, aucune tombee\)', T, 'R06b', 'nn.3 issues')
if m:
    ln_ = [c for c in cs if c['creneau'] == 'N']
    ex = lambda g: sum(1 for c in g if c['E1'] in ('TIENT', 'TOMBE'))
    ok = (m.group(1), int(m.group(2)), int(m.group(3))) == (iss(V3['E1']), len(lig), ex(lig))
    ok = ok and (m.group(4), int(m.group(5)), int(m.group(6))) == ('TENU', len(ln_), sum(1 for c in ln_ if c['E2'] in ('TIENT', 'TOMBE')))
    ok = ok and (m.group(7), int(m.group(8)), int(m.group(9))) == ('TENU', len(brd), ex(brd)) and (m.group(10), int(m.group(11))) == ('TENU', len(cs))
    ok = ok and not any(c['E1'] == 'TOMBE' or c['E2'] == 'TOMBE' or c['E3'] == 'TOMBE' for c in cs) and (iss(V3['E2']), iss(V3['E1B']), iss(V3['E3'])) == ('TENU', 'TENU', 'TENU')
    ctl('R06b', ok, 'issues : E1 %d/%d, E2 %d/%d, E1B %d/%d, E3 %d, aucune tombee, aucune inexploitable' % (ex(lig), len(lig), sum(1 for c in ln_ if c['E2'] in ('TIENT', 'TOMBE')), len(ln_), ex(brd), len(brd), len(cs)))

# ---------------------------------------------------------------- R07 E1 et E1B (nn.5)
dl = [e for c in lig for e in dom(c)]
m = grab(r'Aux dix cellules de ligne, (\d+) etats juges du domaine ; \|ln q3\| vaut ([0-9.]+) en mediane et ([0-9.]+) au plus \((\w+)\)', T, 'R07a', 'nn.5 E1 lignes')
if m:
    cm_ = max(((abs(e['ln_q3']), c['id']) for c in lig for e in dom(c)))
    ctl('R07a', (m.group(1), m.group(2), m.group(3), m.group(4)) == (str(len(dl)), f4(statistics.median(abs(e['ln_q3']) for e in dl)), f4(cm_[0]), cm_[1]), 'lignes : %d etats, mediane %s, plus grand %s (%s)' % (len(dl), f4(statistics.median(abs(e['ln_q3']) for e in dl)), f4(cm_[0]), cm_[1]))
da = [e for c in cs for e in dom(c)]
cls = [[e for e in da if e['e_bord'] < 0.3], [e for e in da if 0.3 <= e['e_bord'] < 0.5], [e for e in da if 0.5 <= e['e_bord'] < 0.7]]
for i, motif in enumerate((r'\[0, 0\.3\[ : (\d+) etats, mediane ([0-9.]+), plus grand ([0-9.]+)', r'\[0\.3, 0\.5\[ : (\d+), ([0-9.]+), ([0-9.]+)', r'\[0\.5, 0\.7\[ : (\d+), ([0-9.]+), ([0-9.]+)')):
    m = grab(motif, T, 'R07b%d' % i, 'classe %d' % i)
    if m:
        v = [abs(e['ln_q3']) for e in cls[i]]
        ctl('R07b%d' % i, m.groups() == (str(len(v)), f4(statistics.median(v)), f4(max(v))), 'classe e_bord %d : %d etats, mediane %s, plus grand %s' % (i, len(v), f4(statistics.median(v)), f4(max(v))))
ctl('R07b3', len(da) == sum(len(x) for x in cls) == 129 and '(129 etats)' in T, 'les trois classes couvrent les %d etats du domaine' % len(da))
m = grab(r'plus petite marge d\'une cellule de ligne est ([+-][0-9.]+), a (\w+) : un etat de e_bord < 0\.3 a \|ln q3\| = ([0-9.]+) pour T = ([0-9.]+)\. (\w+), que la plume annoncait comme le point dur, tient avec ([+-][0-9.]+) de marge', T, 'R07c', 'nn.5 marges de ligne')
if m:
    mm = min(((e['tolerance'] - abs(e['ln_q3']), c['id'], e) for c in lig for e in dom(c)), key=lambda x: x[0])
    mn1 = min(e['tolerance'] - abs(e['ln_q3']) for e in dom(CELL['N1']))
    ctl('R07c', (m.group(1), m.group(2), m.group(3), m.group(4), m.group(5), m.group(6)) == (sg4(mm[0]), mm[1], f4(abs(mm[2]['ln_q3'])), '%.2f' % mm[2]['tolerance'], 'N1', sg4(mn1)) and mm[2]['e_bord'] < 0.3,
        'plus petite marge de ligne %s a %s (|ln q3| %s, T %.2f, e_bord %.3f) ; N1 %s' % (sg4(mm[0]), mm[1], f4(abs(mm[2]['ln_q3'])), mm[2]['tolerance'], mm[2]['e_bord'], sg4(mn1)))
bn, bp = CELL['BN'], CELL['BP']
m = grab(r'BN \(delta = ([+-][0-9.]+)\) : (\d+) etats du domaine, \|ln q3\| au plus ([0-9.]+), marge ([+-][0-9.]+)\. BP \(delta = ([+-][0-9.]+)\) : (\d+) etats du domaine, ln q3 de ([+-][0-9.]+) a ([+-][0-9.]+) ; le plus grand, a l\'etat de rang (\d+), vaut ([0-9.]+) pour T = ([0-9.]+) : marge ([+-][0-9.]+)', T, 'R07d', 'nn.5 E1B')
if m:
    bpd = dom(bp)
    pbp = max(bpd, key=lambda e: abs(e['ln_q3']))
    mine = ('%+.3f' % bn['delta'], str(len(dom(bn))), f4(max(abs(e['ln_q3']) for e in dom(bn))), sg4(min(e['tolerance'] - abs(e['ln_q3']) for e in dom(bn))), '%+.3f' % bp['delta'], str(len(bpd)),
            sg4(min(e['ln_q3'] for e in bpd)), sg4(max(e['ln_q3'] for e in bpd)), str(pbp['rang']), '%.6f' % abs(pbp['ln_q3']), '%.2f' % pbp['tolerance'], '%+.6f' % (pbp['tolerance'] - abs(pbp['ln_q3'])))
    ctl('R07d', m.groups() == mine, 'E1B : acte %s ; refait %s' % (' '.join(m.groups()), ' '.join(mine)))
m = grab(r'Plus petites distances d\'un etat juge a une garde, dans tout le run : ([0-9.]+) a e_bord = 0\.7 \((\w+) rang (\d+)\), ([0-9.]+) a la stabilite 0\.05 \((\w+) rang (\d+)\)', T, 'R07e', 'nn.5 gardes')
if m:
    tous = [(c['id'], e) for c in cs for e in jug(c)]
    de = min(tous, key=lambda x: abs(x[1]['e_bord'] - 0.7))
    ds = min(((i, e) for i, e in tous if e['stab3'] is not None), key=lambda x: abs(x[1]['stab3'] - 0.05))
    ctl('R07e', m.groups() == (f4(abs(de[1]['e_bord'] - 0.7)), de[0], str(de[1]['rang']), f4(abs(ds[1]['stab3'] - 0.05)), ds[0], str(ds[1]['rang'])),
        'garde e_bord 0.7 : %s a %s rang %d ; stabilite 0.05 : %s a %s rang %d' % (f4(abs(de[1]['e_bord'] - 0.7)), de[0], de[1]['rang'], f4(abs(ds[1]['stab3'] - 0.05)), ds[0], ds[1]['rang']))

# ---------------------------------------------------------------- R08 E2 et E3 (nn.5)
ligN = [CELL[i] for i in ('N1', 'N2', 'N3', 'N4', 'N5')]
npres = {c['id']: sum(1 for e in dom(c) if abs(e['ln_q3']) < abs(e['ln_q2'])) for c in ligN}
m = grab(r'plus pres du plateau que l\'ordre 2 a (\d+) etats juges du domaine sur (\d+) : N1 (\d+) sur (\d+), N2 (\d+) sur (\d+), N3 (\d+) sur (\d+), N4 (\d+) sur (\d+), N5 (\d+) sur (\d+)\. L\'ordre 2 y est trop grand \(ln q2 median de ([+-][0-9.]+) a ([+-][0-9.]+) selon la cellule\), l\'ordre 3 trop petit \(ln q3 median de ([+-][0-9.]+) a ([+-][0-9.]+)\)', T, 'R08a', 'nn.5 E2')
if m:
    g = m.groups()
    attendu = [str(sum(npres.values())), str(sum(len(dom(c)) for c in ligN))]
    for c in ligN:
        attendu += [str(npres[c['id']]), str(len(dom(c)))]
    q2m = [statistics.median(e['ln_q2'] for e in dom(c)) for c in ligN]
    q3m = [statistics.median(e['ln_q3'] for e in dom(c)) for c in ligN]
    attendu += [sg4(min(q2m)), sg4(max(q2m)), sg4(min(q3m)), sg4(max(q3m))]
    ctl('R08a', list(g) == attendu, 'E2 : %s sur %s ; ln q2 median %s a %s ; ln q3 median %s a %s' % (attendu[0], attendu[1], attendu[-4], attendu[-3], attendu[-2], attendu[-1]))
m = grab(r'ligne N \(borne ([0-9.]+)\), \|ln q2\| au plus ([0-9.]+) ; ligne P \(borne ([0-9.]+)\), au plus ([0-9.]+) ; BN ([0-9.]+) ; BP ([0-9.]+)\. La plus petite marge en logarithme est ([0-9.]+), sur la ligne (\w)', T, 'R08b', 'nn.5 E3')
if m:
    def mx(g_):
        return max(abs(e['ln_q2']) for c in g_ for e in jug(c))
    mN, mP, mBN, mBP = mx(ligN), mx([CELL[i] for i in ('P1', 'P2', 'P3', 'P4', 'P5')]), mx([bn]), mx([bp])
    ctl('R08b', m.groups()[:6] == ('1.6', f4(mN), '1.25', f4(mP), f4(mBN), f4(mBP)) and CELL['N1']['bande'] == 1.6 and CELL['P1']['bande'] == 1.25, 'E3 : bornes 1.6 / 1.25 ; |ln q2| au plus N %s, P %s, BN %s, BP %s' % (f4(mN), f4(mP), f4(mBN), f4(mBP)))
    marges = {'N': math.log(1.6) - mN, 'P': math.log(1.25) - mP, 'BN': math.log(1.6) - mBN, 'BP': math.log(1.6) - mBP}
    pm = min(marges, key=marges.get)
    ctl('R08c', (m.group(7), m.group(8)) == ('%.3f' % marges[pm], pm), 'E3 : plus petite marge en logarithme refaite : %.4f sur %s ; l\'acte ecrit %s sur %s' % (marges[pm], pm, m.group(7), m.group(8)))

# ---------------------------------------------------------------- R09 consigne (nn.6)
m = grab(r'ligne N, negatif a (\d+) etats sur (\d+) ; ligne P, positif a (\d+) sur (\d+) ; BN negatif a ses (\d+) etats ; BP positif a ses (\d+) etats', T, 'R09a', 'nn.6 signes')
if m:
    P5 = [CELL[i] for i in ('P1', 'P2', 'P3', 'P4', 'P5')]
    neg = lambda g_: sum(1 for c in g_ for e in dom(c) if e['ln_q3'] < 0)
    pos = lambda g_: sum(1 for c in g_ for e in dom(c) if e['ln_q3'] > 0)
    nd = lambda g_: sum(len(dom(c)) for c in g_)
    ctl('R09a', m.groups() == (str(neg(ligN)), str(nd(ligN)), str(pos(P5)), str(nd(P5)), str(neg([bn])), str(pos([bp]))) and neg([bn]) == nd([bn]) and pos([bp]) == nd([bp]), 'signes : N %d/%d negatifs ; P %d/%d positifs ; BN %d ; BP %d' % (neg(ligN), nd(ligN), pos(P5), nd(P5), neg([bn]), pos([bp])))
H = [(c['id'], e) for c in (bn, bp) for e in hors(c)]
m = grab(r'12 etats juges \(BN (\d+), BP (\d+)\), de e_bord ([0-9.]+) a ([0-9.]+) ; (\d+) ne sortent du domaine que par la garde de stabilite\. L\'ordre 3 n\'y est plus loin que l\'ordre 2 a AUCUN : \|ln q3\| au plus ([0-9.]+), \|ln q2\| au plus ([0-9.]+)', T, 'R09b', 'nn.6 hors domaine')
if m:
    stab_seule = sum(1 for _, e in H if e['e_bord'] < 0.7)
    loin = sum(1 for _, e in H if abs(e['ln_q3']) > abs(e['ln_q2']))
    ctl('R09b', m.groups() == (str(len(hors(bn))), str(len(hors(bp))), '%.3f' % min(e['e_bord'] for _, e in H), '%.3f' % max(e['e_bord'] for _, e in H), str(stab_seule), f4(max(abs(e['ln_q3']) for _, e in H)), f4(max(abs(e['ln_q2']) for _, e in H))) and loin == 0 and len(H) == 12,
        'hors domaine : %d etats (BN %d, BP %d), e_bord %.3f a %.3f, %d par la stabilite seule, ordre 3 plus loin a %d, |ln q3| %s, |ln q2| %s' % (len(H), len(hors(bn)), len(hors(bp)), min(e['e_bord'] for _, e in H), max(e['e_bord'] for _, e in H), stab_seule, loin, f4(max(abs(e['ln_q3']) for _, e in H)), f4(max(abs(e['ln_q2']) for _, e in H))))
m = grab(r'A la ligne P, l\'ordre 3 est plus pres que l\'ordre 2 aux (\d+) etats du domaine', T, 'R09c', 'nn.6 ligne P')
if m:
    ctl('R09c', m.group(1) == str(sum(1 for c in P5 for e in dom(c) if abs(e['ln_q3']) < abs(e['ln_q2']))), 'ligne P : ordre 3 plus pres que l\'ordre 2 a %s etats du domaine' % m.group(1))
m = grab(r'Etiquettes : (\d+) des (\d+) etats lus portent une etiquette parmi les quatorze predites de leur cellule', T, 'R09d', 'nn.6 etiquettes')
if m:
    pred = {p['id']: {(x['n1'], x['n2']) for x in p['etats']} for p in DENSE['points']}
    n_et = sum(1 for p in VT['points'].values() for e in p['etats'] if (e['n1'], e['n2']) in pred[p['id']])
    ctl('R09d', m.groups() == (str(n_et), str(nlus)), 'etiquettes : %d des %d etats lus portent une etiquette parmi les predites' % (n_et, nlus))

# ---------------------------------------------------------------- R10 regularites et attentes (nn.7)
ATT = {}
for mm in re.finditer(r'\b(N\d|P\d|BN|BP) +domaine +(\d+) +\( *(\d+) a 0\.05\) +e_bord ([0-9.]+) a ([0-9.]+) +ln\(G3/G2\) ([+-][0-9.]+) +attente ([0-9.]+) +marge ([0-9.]+)', open(GEL2, encoding='ascii').read()):
    ATT[mm.group(1)] = (int(mm.group(2)), float(mm.group(7)))
neg_dom = [(c, e) for c in (ligN + [bn]) for e in dom(c)]
ks = [-e['ln_q3'] / math.log(e['G3'] / e['G2']) ** 2 for c, e in neg_dom if abs(math.log(e['G3'] / e['G2'])) >= 0.05]
m = grab(r'Avant le run : mediane ([0-9.]+), au plus ([0-9.]+)\. Aux (\d+) etats du domaine du run a delta < 0 : mediane ([0-9.]+), au plus ([0-9.]+) ; aucun etat au-dessus de ([0-9.]+)', T, 'R10a', 'nn.7 k')
if m:
    gm = re.search(r'k = -ln q3 / \(ln\(G3 / G2\)\)\^2 vaut de ([0-9.]+) a ([0-9.]+), mediane ([0-9.]+)', gel)
    ctl('R10a', m.groups() == (gm.group(3), gm.group(2), str(len(neg_dom)), '%.2f' % statistics.median(ks), '%.2f' % max(ks), gm.group(2)) and len(ks) == len(neg_dom) and sum(1 for k in ks if k > float(gm.group(2))) == 0,
        'k a delta < 0 : %d etats (%d ou la correction se lit), mediane %.2f, plus grand %.2f ; avant le run (gel) mediane %s, plus grand %s' % (len(neg_dom), len(ks), statistics.median(ks), max(ks), gm.group(3), gm.group(2)))
pos_dom = [(c, e) for c in (P5 + [bp]) for e in dom(c)]
r3 = [e['ln_q3'] / c['delta'] ** 3 for c, e in pos_dom]
r2 = [e['ln_q3'] / c['delta'] ** 2 for c, e in pos_dom]
m = grab(r'ln q3 / delta\^3 atteint (\d+) \(avant le run : au plus (\d+)\) et depasse l\'ancien maximum a (\d+) etats sur (\d+) ; ln q3 / delta\^2 atteint ([0-9.]+) \(avant : au plus ([0-9.]+)\) et le depasse a (\d+) etats', T, 'R10b', 'nn.7 delta > 0')
if m:
    gm = re.search(r'ln q3 / delta\^2 vaut au plus ([0-9.]+) \(mediane [0-9.]+\), ln q3 / delta\^3 au plus (\d+)', gel)
    ctl('R10b', m.groups() == ('%.0f' % max(r3), gm.group(2), str(sum(1 for x in r3 if x > float(gm.group(2)))), str(len(pos_dom)), '%.1f' % max(r2), gm.group(1), str(sum(1 for x in r2 if x > float(gm.group(1))))),
        'delta > 0 : %d etats ; delta^3 plus grand %.0f (avant %s), depasse a %d ; delta^2 plus grand %.1f (avant %s), depasse a %d' % (len(pos_dom), max(r3), gm.group(2), sum(1 for x in r3 if x > float(gm.group(2))), max(r2), gm.group(1), sum(1 for x in r2 if x > float(gm.group(1)))))
pire = {c['id']: max(abs(e['ln_q3']) for e in dom(c)) for c in cs}
m = grab(r'sont tenues aux six cellules de ce cote : le realise est sous l\'attente a N1 \(([0-9.]+) pour ([0-9.]+)\), N2, N3, N4, N5 et BN', T, 'R10c', 'nn.7 attentes delta < 0')
if m:
    sous = [i for i in ('N1', 'N2', 'N3', 'N4', 'N5', 'BN') if pire[i] < ATT[i][1]]
    ctl('R10c', len(ATT) == 12 and len(sous) == 6 and m.groups() == (f4(pire['N1']), '%.4f' % ATT['N1'][1]), 'attentes (lues dans la table 7.3 du gel) : realise sous l\'attente a %s ; N1 %s pour %.4f' % (sous, f4(pire['N1']), ATT['N1'][1]))
m = grab(r'au-dessus de l\'attente de 7\.3 a (\d+) cellules de la ligne P sur cinq \((P1, P2, P3, P4)\) : ([0-9.]+) a P1 pour une attente de ([0-9.]+)', T, 'R10d', 'nn.7 attentes delta > 0')
if m:
    dessus = [i for i in ('P1', 'P2', 'P3', 'P4', 'P5') if pire[i] > ATT[i][1]]
    ctl('R10d', (m.group(1), m.group(2), m.group(3), m.group(4)) == (str(len(dessus)), ', '.join(dessus), f4(pire['P1']), '%.4f' % ATT['P1'][1]), "au-dessus de l'attente : %s ; P1 %s pour %.4f" % (dessus, f4(pire['P1']), ATT['P1'][1]))
m = grab(r'le plus grand \|ln q3\| d\'une cellule croit quand le couplage baisse \(de ([0-9.]+) au facteur (\S+) a ([0-9.]+) au facteur (\S+)\) ; la mediane, elle, bouge peu \(de ([0-9.]+) a ([0-9.]+)\)', T, 'R10e', 'nn.7 ligne P')
if m:
    med = [statistics.median(abs(e['ln_q3']) for e in dom(c)) for c in P5]
    ctl('R10e', m.groups() == (f4(pire['P5']), CELL['P5']['facteur'], f4(pire['P1']), CELL['P1']['facteur'], f4(min(med)), f4(max(med))) and all(pire[a] > pire[b] for a, b in (('P1', 'P2'), ('P2', 'P3'), ('P3', 'P4'), ('P4', 'P5'))),
        'ligne P : plus grand |ln q3| %s (facteur %s) a %s (facteur %s), decroissant avec le facteur ; medianes %s a %s' % (f4(pire['P5']), CELL['P5']['facteur'], f4(pire['P1']), CELL['P1']['facteur'], f4(min(med)), f4(max(med))))
m = grab(r'A BP, le realise \(([0-9.]+)\) est entre les deux attentes \(([0-9.]+) et ([0-9.]+)\)', T, 'R10f', 'nn.7 BP')
if m:
    g_ = re.search(r'sous la tolerance par une regularite \(([0-9.]+), puissance 2\) et au-dessus par l\'autre \(([0-9.]+), puissance 3\)', gel)
    ctl('R10f', m.groups() == (f4(pire['BP']), g_.group(1), g_.group(2)) and float(g_.group(1)) < pire['BP'] < float(g_.group(2)) and abs(float(g_.group(2)) - ATT['BP'][1]) < 1e-9, 'BP : realise %s entre %s (puissance 2) et %s (puissance 3, la table 7.3)' % (f4(pire['BP']), g_.group(1), g_.group(2)))
m = grab(r'Etats au-dela du plus grand e_bord vu avant le run \(([0-9.]+)\) : (\d+) etats du domaine \((.+?)\) ; \|ln q3\| de ([0-9.]+) a ([0-9.]+)\.', T, 'R10g', 'nn.7 garde 0.7')
if m:
    au = sorted(((c['id'], e['rang'], abs(e['ln_q3'])) for c in cs for e in dom(c) if e['e_bord'] > float(m.group(1))))
    ctl('R10g', (m.group(2), m.group(3), m.group(4), m.group(5)) == (str(len(au)), ', '.join('%s rang %d' % (i, r) for i, r, _ in au), f4(min(x[2] for x in au)), f4(max(x[2] for x in au))) and 'aucun etat du domaine a e_bord au-dessus de 0.603' in gel,
        'au-dela de e_bord 0.603 : %d etats du domaine : %s' % (len(au), ', '.join('%s r%d' % (i, r) for i, r, _ in au)))

# ---------------------------------------------------------------- R11 annonces (nn.7) contre le gel, section 10
def prob(motif):
    mm = re.search(motif, gel)
    return mm.groups() if mm else None


g1 = prob(r'A-1 \(([0-9.]+)\)')
g2 = prob(r'A-2 E1 : TENU ([0-9.]+) ; TENU SAUF UNE CELLULE ([0-9.]+)')
g3 = prob(r'A-3 .*? : ([0-9.]+) qu\'elle tombe')
g4 = prob(r'A-4 E2 : TENU ([0-9.]+)')
g5 = prob(r'A-5 E3 TENU : ([0-9.]+)')
g6 = prob(r'A-6 E1B : BN tient ([0-9.]+) ; BP tient ([0-9.]+)')
g7 = prob(r'A-7 \(([0-9.]+)\)')
m = grab(r'A-1 \(([0-9.]+), l\'instrument tient\).*?A-2 : la plume donnait ([0-9.]+) a "E1 TENU" et ([0-9.]+) a "TENU SAUF UNE CELLULE".*?A-3 : elle donnait ([0-9.]+) a la chute de N1.*?A-4 : ([0-9.]+) a "E2 TENU".*?A-5 \(([0-9.]+), E3 TENU\).*?BN tient \(annonce ([0-9.]+)\) ; BP tient \(annonce ([0-9.]+)\).*?A-7 \(([0-9.]+), les signes\)', T, 'R11a', 'nn.7 annonces')
if m:
    ctl('R11a', None not in (g1, g2, g3, g4, g5, g6, g7) and m.groups() == (g1[0], g2[0], g2[1], g3[0], g4[0], g5[0], g6[0], g6[1], g7[0]), 'annonces de la section 10 du gel retrouvees : %s' % (m.groups(),))
ctl('R11b', 'elle annoncait que l\'issue la plus probable n\'etait PAS un E1 tenu partout' in T and 'La plume annonce donc que l\'issue la plus probable n\'est PAS un E1 tenu partout' in gel, 'phrase de la plume (section 10) correctement rapportee')

# ---------------------------------------------------------------- R12 la phrase autorisee (nn.8), le bloc
mg = re.search(r'L\'acte peut ecrire : "(.+?)"\. Il ne peut pas ecrire une loi en delta', gel)
ma = re.search(r'l\'acte ecrit donc la phrase que le gel autorisait : (.+?)\. Le bloc d\'ordre 3 \((\w{16})\) peut etre propose au depot', T)
ctl('R12a', mg and ma and ma.group(1) == mg.group(1) and ma.group(2) == CAN['bloc3'], 'phrase de nn.8 = phrase autorisee par la section 8 du gel (a la lettre) ; bloc d\'ordre 3 %s' % (ma.group(2) if ma else None))
ctl('R12b', all(x in T for x in ('Il n\'ecrit PAS', 'une loi en delta', 'BP est a la limite', 'Aucun seuil, aucune garde, aucune tolerance n\'a ete regle apres lecture')) and 'Le bloc d\'ordre 3 peut alors etre propose au depot' in gel,
    'nn.8 : limites ecrites (pas de loi en delta, BP a la limite, rien de regle apres lecture)')

# ---------------------------------------------------------------- R13 reserves (nn.9) et ecart d'ecarts
m = grab(r'va "de ([0-9.]+) a ([0-9.]+)" aux etiquettes predites de la ligne N\. Le plus grand est ([0-9.]+)', T, 'R13a', 'nn.9 O-1')
if m:
    ver = open(os.path.join(CERT, 'verification_nombres_gel_machine2_v1.log'), encoding='ascii').read()
    mv = re.search(r'de ([0-9.]+) a ([0-9.]+) \(texte', ver)
    ctl('R13a', (m.group(1), m.group(2)) == ('0.066', '0.164') and 'de 0.066 a 0.164' in gel and mv is not None and '%.4f' % float(m.group(3)) == mv.group(2) and float(m.group(3)) < 0.164,
        'O-1 : gel "0.066 a 0.164" ; mon calcul (verification des nombres, passage mordu) %s ; dans l acte : plus grand %s, soit %.4f' % (mv.group(2) if mv else None, m.group(3), float(m.group(3))))
ctl('R13b', 'Lecture du gel (une cellule tombee donnerait TENU SAUF UNE CELLULE) : TENU. Lecture stricte (une cellule tombee donnerait TOMBE) : TENU' in T and not any(c['E2'] in ('TOMBE', 'INEXPLOITABLE') for c in ligN),
    'R-1 : E2 TENU aux deux lectures (aucune cellule N tombee ou inexploitable)')

# ---------------------------------------------------------------- R14 le rejeu de machine 1 (nn.4)
if '--sans-fichiers-m1' not in sys.argv:
    V3m = json.load(open(FICH['ordre3_m1']))
    VTm = json.load(open(FICH['lecteur_m1']))
    gaps = {'ln_q3': 0.0, 'ln_q2': 0.0, 'stab3': 0.0, 'e_bord': 0.0}
    diffs = []
    for cm_ in V3m['cellules']:
        c = CELL[cm_['id']]
        if (cm_['n_domaine'], cm_['n_hors'], cm_['n_juges'], cm_['E1'], cm_['E2'], cm_['E3']) != (c['n_domaine'], c['n_hors'], c['n_juges'], c['E1'], c['E2'], c['E3']):
            diffs.append(cm_['id'])
        for e, f in zip(c['etats'], cm_['etats']):
            if (e['rang'], e['exclu'], e.get('dans_le_domaine')) != (f['rang'], f['exclu'], f.get('dans_le_domaine')):
                diffs.append((c['id'], e['rang']))
                continue
            if e['exclu'] is None:
                for k in gaps:
                    if e[k] is not None and f[k] is not None:
                        gaps[k] = max(gaps[k], abs(e[k] - f[k]))
    issues_m = {k: iss(V3m[k]) for k in ('E1', 'E1B', 'E2', 'E3')}
    issues_r = {k: iss(V3[k]) for k in ('E1', 'E1B', 'E2', 'E3')}
    m = grab(r'plus grands ecarts entre les deux machines sur les 141 etats juges : ([0-9.e-]+) sur ln q3, ([0-9.e-]+) sur ln q2, ([0-9.e-]+) sur la stabilite ; e_bord identique', T, 'R14a', 'nn.4 ecarts')
    if m:
        f2 = lambda x: ('%.1e' % x).replace('e-0', 'e-0') if x else '0'
        ctl('R14a', not diffs and issues_m == issues_r and m.groups() == ('%.1e' % gaps['ln_q3'], '%.1e' % gaps['ln_q2'], '%.1e' % gaps['stab3']) and gaps['e_bord'] == 0.0,
            'rejeu de m1 contre le run : memes issues %s, differences d\'etat %s ; ecarts ln q3 %.1e, ln q2 %.1e, stab %.1e, e_bord %.1e' % (issues_m == issues_r, diffs[:3], gaps['ln_q3'], gaps['ln_q2'], gaps['stab3'], gaps['e_bord']))
    rel, memes = 0.0, True
    for pid, p in VT['points'].items():
        q = VTm['points'][pid]
        for e, f in zip(p['etats'], q['etats']):
            memes = memes and (e['rang'], e['statut'], e['n1'], e['n2']) == (f['rang'], f['statut'], f['n1'], f['n2'])
            for k, pl in e['plateaux'].items():
                if 'Gamma_pl' in pl:
                    rel = max(rel, abs(pl['Gamma_pl'] / f['plateaux'][k]['Gamma_pl'] - 1.0))
    m = grab(r'plus grand ecart relatif : ([0-9.e-]+)\)', T, 'R14b', 'nn.4 lecteur')
    if m:
        ctl('R14b', memes and m.group(1) == '%.1e' % rel, 'lecteur rejoue : memes etats et statuts : %s ; plus grand ecart relatif d\'une largeur de plateau %.1e' % (memes, rel))
    def lignes(p):
        return open(p, encoding='utf-8', errors='replace').read().replace('\r\n', '\n').split('\n')
    idn = lignes(os.path.join(RUN, 'lecture_ter.log')) == lignes(os.path.join(M1, 'rejeu_machine1_lecture_ter.log')) and lignes(os.path.join(RUN, 'lecture_ter_instrument.log')) == lignes(os.path.join(M1, 'rejeu_machine1_lecture_ter_instrument.log'))
    ctl('R14c', idn and 'les deux journaux de lecture sont identiques ligne a ligne' in T, 'journaux de lecture du run et du rejeu identiques ligne a ligne (CRLF mis a part) : %s' % idn)
    mine = json.load(open(os.path.join(ICI, 'ma_feuille_sur_verdict_lecteur_machine1_v1.json')))
    his = json.load(open(os.path.join(M1, 'verdict_ordre3_rejoue_sur_mon_verdict.json')))
    his_i = {k: iss(his[k]) for k in ('E1', 'E1B', 'E2', 'E3')}
    mi = {k: mine[k][0] for k in ('E1', 'E1B', 'E2', 'E3')}
    cmp_ = all((c['n_juges'], c['n_domaine'], c['n_hors']) == (his_c['n_juges'], his_c['n_domaine'], his_c['n_hors']) for c, his_c in zip(mine['cellules'], sorted(his['cellules'], key=lambda x: [k['id'] for k in mine['cellules']].index(x['id']))))
    ctl('R14d', mi == his_i and cmp_ and 'Rejouee aussi sur le verdict du lecteur de machine 1 : memes issues' in T, 'MA feuille rejouee sur le verdict du lecteur de m1 : issues %s ; les siennes %s ; memes comptes : %s' % (mi, his_i, cmp_))
    m = grab(r'sa seconde feuille \((\w{16}), ecrite des sections 5 et 6 du gel seules, avec ses propres chaines\) sur les fichiers du run : aucune difference sur les (\d+) etats juges', T, 'R14e', 'nn.4 ma seconde feuille')
    if m:
        mrun = json.load(open(os.path.join(CERT, 'concordance_run_machine2_v1.json')))
        ctl('R14e', m.group(1) == CAN['feuille_m2'] and int(m.group(2)) == njug and sum(c['n_juges'] for c in mrun['cellules']) == njug, 'ma 2e feuille %s ; %d etats juges (concordance deja faite hier, 0 difference)' % (CAN['feuille_m2'], njug))
    ctl('R14f', 'plus de cent mille fois cet ecart' in T and (pbp['tolerance'] - abs(pbp['ln_q3'])) / gaps['ln_q3'] > 1e5, 'marge de BP %.3g = %.2g fois l\'ecart ln q3 entre machines (l\'acte : plus de cent mille)' % (pbp['tolerance'] - abs(pbp['ln_q3']), (pbp['tolerance'] - abs(pbp['ln_q3'])) / gaps['ln_q3']))

# ---------------------------------------------------------------- R15 nn.0 et nn.10
mm = re.search(r'graine de l\'operateur \((\d+)\) : cinq couplages a delta = ([+-][0-9.]+), cinq a delta = ([+-][0-9.]+), et deux cellules de bord a delta = ([+-][0-9.]+) et ([+-][0-9.]+)', T)
ctl('R15a', mm and (mm.group(2), mm.group(3), mm.group(4), mm.group(5)) == ('%+.3f' % CELL['N1']['delta'], '%+.3f' % CELL['P1']['delta'], '%+.3f' % bn['delta'], '%+.3f' % bp['delta']) and all(abs(CELL[i]['delta'] - CELL['N1']['delta']) < 1e-12 for i in ('N2', 'N3', 'N4', 'N5'))
    and all(abs(CELL[i]['delta'] - CELL['P1']['delta']) < 1e-12 for i in ('P2', 'P3', 'P4', 'P5')) and mm.group(1) == '200482', 'deltas des douze cellules et graine 200482 : %s' % (mm.groups() if mm else None))
m = grab(r'P1 et P2 n\'ont que (\d+) et (\d+) etats lus \((\d+) et (\d+) predits dans le domaine\)', T, 'R15b', 'nn.10 P1 P2')
if m:
    ctl('R15b', m.groups() == (str(len(CELL['P1']['etats'])), str(len(CELL['P2']['etats'])), str(ATT['P1'][0]), str(ATT['P2'][0])), 'P1 et P2 : etats lus %d et %d ; predits dans le domaine %d et %d (table 7.3)' % (len(CELL['P1']['etats']), len(CELL['P2']['etats']), ATT['P1'][0], ATT['P2'][0]))
ctl('R15c', 'BP tient a 0.000383 pres' in T and '%.6f' % (pbp['tolerance'] - abs(pbp['ln_q3'])) == '0.000383', 'nn.10 : BP tient a 0.000383 pres')

# ---------------------------------------------------------------- bilan
mord = [r for r in RES if not r[1]]
print('RELEVE DU CONTRESEING : %d controles, %d mordent : %s' % (len(RES), len(mord), [r[0] for r in mord]))
json.dump([{'id': a, 'tient': b, 'texte': c} for a, b, c in RES], open(SORTIE, 'w'), indent=1)
sys.exit(0 if not mord else 1)
