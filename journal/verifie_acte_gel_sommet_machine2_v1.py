# -*- coding: ascii -*-
"""CONTRESEING de l'acte du gel "SOMMET" (journal_delta_nn_sommet_v1.md, 417cf051cc04671b, lot fcfeb710fc3910cc de machine 1) : chaque nombre qui peut etre refait l'est, depuis MES fichiers (le dossier du run, le verdict de la feuille jouee dans le run, la table gelee, mes sorties de Q et Q2, mes journaux, mes notes),
et non depuis son rejeu ni son controle. Je ne lis pas ses scripts ; je lis son acte comme un texte.
Parties : A. nn.3, les 56 lignes (w2, kappa, g, plateau lu, s, etendue, bande, ln q, jugement) ; B. nn.2, les neuf temoins ; C. nn.6, le tableau par kappa (ln q, negatifs, Phi, etalements) et la largeur rapportee au saut ; D. nn.1 et nn.3, les durees, les 136 appels, les heures, les lectures non suivies, la largeur du jumeau, la platitude sous A ;
E. nn.5, la bande, la marge, "sous l'etendue", "sous l'etalement" ; F. nn.7, les annonces (comptes) ; G. nn.9, le champ poids_min de la feuille ; H. nn.12, les canons des pieces de machine 2 ; I. nn.8, ce que le delta 102 depose dit.
Usage : py -3.11 -I verifie_acte_gel_sommet_machine2_v1.py <acte .md> <dossier du run> <table gelee JSON> <mes notes : dossier racine BOCAL4> <delta 102 depose .md>"""
import hashlib
import json
import math
import os
import re
import sys
import unicodedata
from fractions import Fraction as F

ACTE, RUN, TABLE, RACINE, D102 = sys.argv[1:6]
act = open(ACTE, encoding='ascii').read()
V = json.load(open(os.path.join(RUN, 'verdict_sommet.json')))
T = json.load(open(TABLE))
C = {c['id']: c for c in V['cellules']}
TC = {c['id']: c for c in T['cellules']}
n_ok = n_ko = 0
bites = []


def check(nom, ok, detail=''):
    global n_ok, n_ko
    if ok:
        n_ok += 1
    else:
        n_ko += 1
        bites.append('%s %s' % (nom, detail))
    print('%s : %s %s' % ('TIENT ' if ok else 'MORD  ', nom, detail))


def canon_B(chemin):
    s = unicodedata.normalize('NFC', open(chemin, 'rb').read().decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n')
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


# ---- A. nn.3
print('A. nn.3 : les 56 lignes contre le verdict de ma feuille-run')
rows = re.findall(r'^\s{4}((?:MP|PP|MG|PG)[ab]\d)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s*$', act, re.M)
bad = []
for (cid, w2d, kp, g, plat, s, et, b, lq, jug) in rows:
    c = C[cid]
    mien = ('%.5f' % float(F(c['w2'])), c['kappa'], c['g'], '%.5e' % math.exp(c['ln_Gamma_pl']), '%.4f' % c['etalement_du_lecteur'], '%.4f' % c['etendue'], '%.4f' % c['bande'], '%+.5f' % c['ln_q'], c['jugement'])
    if (w2d, kp, g, plat, s, et, b, lq, jug) != mien:
        bad.append((cid, (w2d, kp, g, plat, s, et, b, lq, jug), mien))
check('A. les 56 lignes de nn.3 (w2, kappa, g, plateau lu a six chiffres, s, etendue, bande, ln q, jugement) = verdict de la feuille jouee dans le run', len(rows) == 56 and not bad, '(%d lignes lues ; differences : %s)' % (len(rows), bad[:3] or 'aucune'))

# ---- B. nn.2
print('\nB. nn.2 : les neuf temoins')
tm = re.findall(r'^\s{4}(Q2?[a-f])\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s*$', act, re.M)
pts = {p['id']: p for p in V['temoins_positifs']['points']}
bad = []
for (i, w2, g, lu, ref, ec) in tm:
    p = pts[i]
    w = [x for x in T['temoins_positifs'] if x['id'] == i][0]
    if (w2, g, lu, ref) != (w['w2'], w['g'], '%.5e' % p['lecteur']['plateaux']['A']['Gamma_pl'], '%.5e' % math.exp(w['ln_Gamma_pl_reference'])) or abs(p['ecart_reference']) > 1e-12 or ec != '+0.0e+00':
        bad.append(i)
check('B. les neuf temoins de nn.2 (w2, g, plateau lu, reference, ecart nul) = ma garde jouee dans le run', len(tm) == 9 and not bad, '(%d lignes ; differences : %s)' % (len(tm), bad or 'aucune'))

# ---- C. nn.6
print('\nC. nn.6 : le tableau par kappa')
KN = ['0.0363', '0.0530', '0.0800', '0.1300', '0.2000', '0.4000', '1.0000']
lg = re.findall(r'^\s{4}(0\.\d{4}|1\.0000)\s+([+-]\d\.\d{5})\s+([+-]\d\.\d{5})\s+([+-]\d\.\d{5})\s+(\d)\s+(\S+)\s+(\S+)\s+(\d\.\d{5})\s+(\d\.\d{5})\s*$', act, re.M)
bad = []
for (kp, mn, mx, moy, neg, pmin, pmax, el, ech) in lg:
    cs = [c for c in V['cellules'] if c['kappa'] == kp]
    lq = [c['ln_q'] for c in cs]
    phi = [math.exp(c['ln_Gamma_pl']) / abs(c['delta']) for c in cs]
    lphi = [math.log(x) for x in phi]
    lch = [TC[c['id']]['ln_Phi'] for c in cs]
    mien = ('%+.5f' % min(lq), '%+.5f' % max(lq), '%+.5f' % (sum(lq) / len(lq)), str(sum(1 for x in lq if x < 0)), '%.5e' % min(phi), '%.5e' % max(phi), '%.5f' % (max(lphi) - min(lphi)), '%.5f' % (max(lch) - min(lch)))
    if (mn, mx, moy, neg, pmin, pmax, el, ech) != mien:
        bad.append((kp, (mn, mx, moy, neg, pmin, pmax, el, ech), mien))
check('C1. le tableau par kappa de nn.6 (min, max, moyenne de ln q ; nombre de negatifs ; Phi lu min et max ; etalement lu et de la chaine)', len(lg) == 7 and not bad, '(%d lignes ; differences : %s)' % (len(lg), bad[:2] or 'aucune'))
mem = [sum(1 for c in V['cellules'] if c['kappa'] == k and c['ln_q'] < 0) for k in KN]
check('C2. "meme signe aux huit w2 a 5 kappa sur sept"', sum(1 for n in mem if n in (0, 8)) == 5, '(negatifs par kappa : %s)' % mem)
ratio = {}
for c in V['cellules']:
    ratio.setdefault(c['kappa'], []).append(math.exp(c['consigne']['ln_Gamma_pl_sur_t0']))
moy = ['%s %.4f' % (k, sum(ratio[k]) / len(ratio[k])) for k in KN]
txt = re.search(r'moyenne par kappa : (.*?)\. A la\s+resonance', act, re.S).group(1)
check('C3. "la largeur rapportee au saut au pied de l echelle, moyenne par kappa"', re.sub(r'\s*;\s*', ';', re.sub(r'\s+', ' ', txt)) == ';'.join(moy), '(acte : %s ; moi : %s)' % (re.sub(r'\s+', ' ', txt), '; '.join(moy)))
la = max(max(math.log(max(x)) - math.log(min(x)) for x in [[math.exp(c['ln_Gamma_pl']) / abs(c['delta']) for c in V['cellules'] if c['kappa'] == k]]) for k in KN)
check('C4. "la largeur lue rapportee au desaccord varie de 0.00032 au plus entre les huit w2"', abs(la - 0.00032) < 5e-6, '(moi : %.5f)' % la)
d = sorted(set(round(abs(c['delta']) * 1e5) for c in V['cellules']))
check('C5. "desaccords de 0.00007 a 0.00048 et les deux signes"', d[0] == 7 and d[-1] == 48, '(|delta| en 1e-5 : %s ; %d valeurs distinctes pour huit w2)' % (d, len(d)))

# ---- D. nn.1 / nn.3
print('\nD. nn.1 et nn.3 : durees, appels, heures, lectures')
pl = open(os.path.join(RUN, 'pilote_gel_sommet.log'), encoding='ascii').read().split('\n')
app = []
for l in pl:
    m = re.match(r'^(\S+ \S+)\s+(lecture (\S+) (jumeau|fantome)|lecteur (\S+)|feuille du lecteur, instrument|feuille du gel, etape de garde|feuille du gel)\s+code=(\d+) duree=(\d+) s', l)
    if m:
        app.append((m.group(1), m.group(2), m.group(3), m.group(5), int(m.group(6)), int(m.group(7))))
check('D1. "136 appels, tous au code 0 ; aucun arret, aucune relance"', len(app) == 136 and all(a[4] == 0 for a in app) and not any('ARRET' in l for l in pl), '(appels comptes dans le journal du pilote : %d)' % len(app))
dA = {a[3]: a[5] for a in app if a[3]}
check('D2. "etage A : 20 s, 846 s et 897 s (etage 0, ancres, etage 1, en parallele)"', (dA.get('etage0'), dA.get('ancres'), dA.get('etage1')) == (20, 846, 897), '(journal : etage0 %s s, ancres %s s, etage1 %s s)' % (dA.get('etage0'), dA.get('ancres'), dA.get('etage1')))
tem = [a[5] for a in app if a[2] and a[2][0] == 'Q']
cel = [a[5] for a in app if a[2] and a[2][0] != 'Q']
check('D3. "les dix-huit lectures des temoins de 129 a 180 s ; les 112 lectures des cellules de 115 a 206 s"', (len(tem), min(tem), max(tem), len(cel), min(cel), max(cel)) == (18, 129, 180, 112, 115, 206), '(journal : %d de %d a %d s ; %d de %d a %d s)' % (len(tem), min(tem), max(tem), len(cel), min(cel), max(cel)))
check('D4. "lance le 2026-11-23 00:16:01 et fini a 01:05:05 ; duree totale 2944 s"', pl[1].startswith('2026-11-23 00:16:01') and any(l.startswith('2026-11-23 01:05:05 FIN DU PILOTE ; duree totale 2944 s') for l in pl), '')
check('D5. "garde : jouee a 00:36:05, avant la premiere lecture de cellule"', any(l.startswith('2026-11-23 00:36:05 GARDE : TIENT') for l in pl) and min(a[0] for a in app if a[2] and a[2][0] != 'Q') >= '2026-11-23 00:36:05', '')
nsf = 0
nsj = 0
nsf_l = []
pl_max = 0.0
flat = 0.0
KS = list(range(-3, 9))
for c in V['cellules']:
    gp = math.exp(c['ln_Gamma_pl'])
    fa = json.load(open(os.path.join(RUN, 'lect2D_%s_fantome.json' % c['id'])))['lecture']['traj']
    ju = json.load(open(os.path.join(RUN, 'lect2D_%s_jumeau.json' % c['id'])))['lecture']['traj']
    for x in 'ABCD':
        for k in KS:
            if not fa[x][str(k)]['suivi']:
                nsf += 1
                nsf_l.append('%s %s k=%+d' % (c['id'], x, k))
            if not ju[x][str(k)]['suivi']:
                nsj += 1
            elif ju[x][str(k)]['gamma'] is not None:
                pl_max = max(pl_max, abs(ju[x][str(k)]['gamma']) / gp)
    for k in range(-3, 5):
        flat = max(flat, abs(fa['A'][str(k)]['gamma'] / gp - 1))
check('D6. "fantome : 2679 suivies sur 2688 ; les 9 non suivies ; jumeau : 0 non suivie sur 2688"', (2688 - nsf, nsf, nsj) == (2679, 9, 0) and sorted(nsf_l) == sorted(['MPa7 A k=+8', 'MPb7 D k=+8', 'PPa7 A k=+8', 'PPa7 D k=+7', 'PPa7 D k=+8', 'MGa6 A k=+8', 'MGa7 C k=-3', 'MGb7 C k=-3', 'PGa7 B k=+8']), '(moi : %d suivies, %d non suivies, %d au jumeau)' % (2688 - nsf, nsf, nsj))
check('D7. "plus grande largeur du jumeau : 4.8e-26 du plateau au plus"', abs(pl_max - 4.8e-26) / 4.8e-26 < 0.05, '(moi : %.2e)' % pl_max)
check('D8. "sous A la largeur est plate a 0.005 pres aux barreaux k = -3 a 4 a toutes les cellules"', flat <= 0.005, '(plus grand ecart relatif sous A, k = -3 a 4, aux 56 cellules : %.5f)' % flat)

# ---- E. nn.5
print('\nE. nn.5')
cs = V['cellules']
bmax = max(c['bande'] for c in cs)
marge = min((c['tolerance'] - c['bande'] - abs(c['ln_q']), c['id']) for c in cs)
check('E1. "la plus grande bande est 0.0056 ; la cellule la plus pres de sa limite (MGb1) garde 0.0044"', '%.4f' % bmax == '0.0056' and marge[1] == 'MGb1' and '%.4f' % marge[0] == '0.0044', '(moi : bande max %.5f ; cellule %s, marge %.5f)' % (bmax, marge[1], marge[0]))
sous_et = sum(1 for c in cs if abs(c['ln_q']) < c['etendue'])
sous_s = sum(1 for c in cs if abs(c['ln_q']) < c['etalement_du_lecteur'])
check('E2. "|ln q| est sous l etendue de la chaine a 56 cellules sur 56, et sous l etalement du lecteur a 56"', sous_et == 56 and sous_s == 56, '(moi : sous l etendue %d, sous l etalement s %d)' % (sous_et, sous_s))
et_max = max(c['etendue'] for c in cs)
check('E3. nn.0 "plateaux de 4.68e-10 a 2.48e-04 ; couplages de 2.48901e-05 a 4.71149e-03 ; |ln q| au plus 0.00025 (PPb2)"',
      ('%.2e' % min(math.exp(c['ln_Gamma_pl']) for c in cs), '%.2e' % max(math.exp(c['ln_Gamma_pl']) for c in cs), min(cs, key=lambda c: float(c['g']))['g'], max(cs, key=lambda c: float(c['g']))['g']) == ('4.68e-10', '2.48e-04', '2.48901e-05', '4.71149e-03')
      and max(cs, key=lambda c: abs(c['ln_q']))['id'] == 'PPb2' and '%.5f' % max(abs(c['ln_q']) for c in cs) == '0.00025', '(plus grand |ln q| : %s)' % max(cs, key=lambda c: abs(c['ln_q']))['id'])

# ---- F. nn.7  (comptes)
print('\nF. nn.7 : les annonces')
bar = [c for c in cs if c['numero_kappa'] in (1, 2)]
neg = [c for c in bar if c['ln_q'] < 0]
pm = V['consigne']['paires_miroirs']
check('F1. "A-7 : dix cellules de barriere negatives : huit de kappa = 0.0530 et 2 des huit de kappa = 0.0363"', (len(neg), sum(1 for c in neg if c['numero_kappa'] == 2), sum(1 for c in neg if c['numero_kappa'] == 1)) == (10, 8, 2), '')
check('F2. "A-8 : 7 sur 7 a 0.0001" et "A-9 : 0.00032 au plus"', sum(1 for p in pm if abs(p['ln_rapport_lu'] - p['ln_rapport_chaine']) <= 1e-4) == 7 and '%.5f' % max(v['etalement_lu'] for v in V['consigne']['loi_d_echelle'].values()) == '0.00032', '')
check('F3. "ln q est negatif a 32 cellules, du signe de delta a 28 ; l ordre 3 plus pres a 35 sur 56"', (V['consigne']['ln_q_negatif'], V['consigne']['ln_q_du_signe_de_delta'], V['consigne']['ordre3_plus_pres_que_ordre1']) == (32, 28, 35), '')

# ---- G. nn.9
print('\nG. nn.9 : le champ poids_min de sa feuille')
pmin_f = min(c['lecteur']['poids_min'] for c in cs)
pw = 1.0
for c in cs:
    fa = json.load(open(os.path.join(RUN, 'lect2D_%s_fantome.json' % c['id'])))['lecture']['traj']
    for x in 'ABCD':
        for k in KS:
            if fa[x][str(k)]['suivi']:
                pw = min(pw, fa[x][str(k)]['poids_site'])
check('G1. "poids_min de la feuille (toutes lectures) = 0.5348 ; poids des lectures suivies = 0.7181"', '%.4f' % pmin_f == '0.5348' and '%.4f' % pw == '0.7181', '(moi : champ poids_min %.4f ; lectures suivies %.4f)' % (pmin_f, pw))

# ---- H. nn.12 : canons de mes pieces
print('\nH. nn.12 : les canons de mes pieces citees')
att = {'c46c3aa3977366f4': 'POUR_MACHINE1_certification_gel_sommet_partie2_machine2_v1.md', 'c462991d2484064c': 'POUR_MACHINE1_resultat_run_gel_sommet_machine2_v1.md'}
for cn, f in att.items():
    p = os.path.join(RACINE, f)
    check('H. %s = canon de ma note %s' % (cn, f), canon_B(p) == cn, '(moi : %s)' % canon_B(p))
for cn, f in (('f6382d96633043ff', 'pilote_gel_sommet.log'), ('c11edf7b49007d05', 'verdict_ter_instrument.json'), ('707b6d999a2b9100', 'garde_sommet.json'), ('2c39171a593d95df', 'verdict_sommet.json')):
    p = os.path.join(RUN, f)
    check('H. %s = canon de %s du run' % (cn, f), canon_B(p) == cn, '(moi : %s)' % canon_B(p))
for cn, f in (('c58c2b3f533c516b', 'MANIFEST_lot_machine2_Q_sommet_v1.txt'), ('295b2b1549b076c2', 'MANIFEST_lot_machine2_Q2_signe_v1.txt'), ('21e9bddfe5db83b2', 'MANIFEST_lot_machine2_certification_gel_sommet_partie1_v1.txt'), ('3db782eea5023b31', 'MANIFEST_lot_machine2_tirage_graine_114565_gel_sommet_v1.txt'),
              ('b7f328b916ba720d', 'MANIFEST_lot_machine2_certification_gel_sommet_partie2_v1.txt'), ('735b9394013b02db', 'MANIFEST_lot_machine2_resultat_run_gel_sommet_v1.txt')):
    p = os.path.join(RACINE, f)
    check('H. %s = canon du manifeste de mon lot (%s)' % (cn, f), canon_B(p) == cn, '(moi : %s)' % canon_B(p))

# ---- I. nn.8 : delta 102
print('\nI. nn.8 : ce que le delta 102 depose dit')
d102 = open(D102, encoding='ascii').read()
check('I1. delta 102 : "|delta| de 0.003 a 0.018" et "0.0098 a trois barreaux jusqu a 0.1262 a seize"', '|delta| de 0.003 a 0.018' in d102 and '0.0098 a 3 barreaux' in d102 and '0.1262 a 16' in d102, '')
g_k1 = 1.0 * 0.01 * 5 / 0.510310363
check('I2. "kappa = 1 a |delta| = 0.01 demande g voisin de 0.1"', 0.09 < g_k1 < 0.11, '(moi : g = kappa |delta| P / X = %.4f)' % g_k1)
print('\nBILAN : %d controles tenus, %d morsures' % (n_ok, n_ko))
for b in bites:
    print('  MORSURE : %s' % b)
