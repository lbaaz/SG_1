"""certif_v9_v15_machine2_v1.py -- machine 2, 2026-09-21.

CERTIFICATION CROISEE du gel constante A v9 (b515abc5a6da73c5) et de l'instrument v15
(a1553f6eb5cc74b8), livres par machine 1 (lot MANIFEST 13/13 au canon).
Entrants : ma certification du v8/v14 (45de25ac61321661, v8 NON CERTIFIE, R-v8-1..5) et ma
prescription (289ae2620e1d1063, D-essai-1..3). Arbitrage operateur du 18/09 : la voie longue.

Chaque nombre du gel est RE-DERIVE ICI par mes propres formules -- la forme close de c1 et c2
est retapee depuis ma derivation b70fca94d72822ad, le plancher corrige est recalcule, les
predictions sont refaites depuis le JSON -- jamais repris du script de construction de machine 1.
Les cinq reprises R-v8-1..5 sont verifiees UNE PAR UNE dans le texte du v9, et les trois defauts
D-essai-1..3 dans le source du v15.
Deux verbes : chk (peut mordre), note (ne peut pas). Sorties ecrites avant le bilan.
E19 : aucun run avant le verdict de cette piece.
"""
import hashlib
import json
import os
import re
import sys
import unicodedata
from fractions import Fraction as F

V8, V9 = 'constante_A_pre_enregistrement_v8.md', 'constante_A_pre_enregistrement_v9.md'
B14, B15 = 'banc_qualification_machine1_v14.py', 'banc_qualification_machine1_v15.py'
FEUILLE9 = 'lecture_v9_machine1_v1.py'
CONSTR = 'construction_gel_v9_banc_v15_machine1_v1.py'
DERJ = 'derivation_second_ordre_machine2_v1.json'
CANON = {V8: '800fc6a9a8e56e49', V9: 'b515abc5a6da73c5', B14: 'dc91676c640d4323',
         B15: 'a1553f6eb5cc74b8', FEUILLE9: '4144c0086a3a99e7', CONSTR: 'd6d7ac766b8f5ac6',
         DERJ: 'b70fca94d72822ad'}
lignes, bilan = [], {'chk': 0, 'mord': []}


def out(s=''):
    print(s)
    lignes.append(s)


def chk(nom, cond, detail=''):
    bilan['chk'] += 1
    if not cond:
        bilan['mord'].append(nom)
    out('  [chk %s] %s%s' % ('PASSE' if cond else 'MORD ', nom, (' -- ' + detail) if detail else ''))
    return cond


def note(nom, detail):
    out('  [note] %s -- %s' % (nom, detail))


def B(p):
    b = open(p, 'rb').read()
    return hashlib.sha256(unicodedata.normalize('NFC', b.decode('utf-8')).replace('\r\n', '\n').encode()).hexdigest()[:16]


T9 = open(V9, encoding='utf-8').read()
PLAT = ' '.join(T9.split())
SRC15 = open(B15, encoding='utf-8').read()
der = json.load(open(DERJ, encoding='utf-8'))

out('CERTIFICATION MACHINE 2 DU GEL v9 ET DE L INSTRUMENT v15')
out('python %s ; %s' % (sys.version.split()[0], os.path.basename(__file__)))
out()
out('0. ANCRES ET PROVENANCE')
for f in sorted(CANON):
    chk('canon %s' % f, B(f) == CANON[f], B(f))
chk('PB-1 : le v8 et le v14 ne sont pas edites', B(V8) == CANON[V8] and B(B14) == CANON[B14])

# ---------------------------------------------------------------- 1. RECONSTRUCTION
out()
out('1. RECONSTRUCTION : LE GEL v9 ET LE BANC v15 DEPUIS LE v8 ET LE v14')
REC = 'm2_reconstruction_v9_v15'
for f in (V9, B15):
    r = os.path.join(REC, f)
    if not os.path.exists(r):
        note('reconstruction %s' % f, 'ABSENTE : rejouer %s' % CONSTR)
        continue
    ident = open(f, 'rb').read() == open(r, 'rb').read()
    chk('1 %s reconstruit IDENTIQUE AU BIT depuis le depose' % f, ident,
        'canon reconstruit %s' % B(r))
rj = os.path.join(REC, 'derives_v9.json')
if os.path.exists(rj):
    chk('1 derives_v9.json : meme convention B malgre les fins de ligne',
        B(rj) == B('derives_v9.json') == '156f9a455f52313e', '%s / %s' % (B(rj), B('derives_v9.json')))
    note('1 derives_v9.json portee', 'le brut differe (CRLF ici, LF chez machine 1) ; la convention B '
         'normalise et le manifeste porte bien l empreinte B -- aucun ecart de fond')

# ---------------------------------------------------------------- 2. LE PLANCHER CORRIGE
out()
out('2. LE PLANCHER CORRIGE, RE-DERIVE PAR MES PROPRES FORMULES')
DP = F(1, 32400)
W2 = ('1.73', '2.27', '2.80')
PROJ4 = 0.2238


def coeffs(p, w2):
    """forme close de c1 et c2 -- retapee depuis MA derivation, pas depuis machine 1"""
    a = F(4, p - 2)
    w = F(w2)
    K = a * (a + 1) * (a + 2) * (a + 3)
    P2 = a * (a + 1) * (a - 1) * (a - 2)
    P4 = (4 - a) * (3 - a) * (2 - a) * (1 - a)
    c1 = (1 + w * w) * a * (a + 1) / ((p - 1) * K - P2)
    c2 = (K * F((p - 1) * (p - 2), 2) * c1 * c1 - (1 + w * w) * c1 * (2 - a) * (1 - a) - w * w) / (P4 - (p - 1) * K)
    return c1, c2


exact = True
for p in (4, 5, 7):
    for w2 in W2:
        c1, c2 = coeffs(p, w2)
        ref = der['C2']['%d|%s' % (p, w2)]
        exact = exact and F(ref['c1']) == c1 and F(ref['c2'][0]) == c2
chk('2.1 : la forme close de c1 ET c2 est EXACTE aux neuf (p, w2) contre ma derivation', exact)
c2_7 = coeffs(7, '1.73')[1]
chk('2.1 temoin : c2(7, 1.73) = 603151178891/25348416000000',
    str(c2_7) == '603151178891/25348416000000', str(c2_7))

PL = {}
for p in (4, 5, 7):
    vals = []
    for w2 in W2:
        c2 = coeffs(p, w2)[1]
        td4 = (float(DP) / (1 + float(w2) ** 2)) ** 2
        vals.append(abs(float(c2)) * td4)
    PL[p] = PROJ4 * max(vals)
ATT = {4: '5.1949e-14', 5: '1.2236e-13', 7: '3.1818e-13'}
for p in (4, 5, 7):
    chk('2.2 p=%d : plancher_corr re-derive == celui ECRIT au gel 7bis (%s)' % (p, ATT[p]),
        '%.4e' % PL[p] == ATT[p] and ATT[p] in PLAT, '%.6e' % PL[p])
dv = json.load(open('derives_v9.json', encoding='utf-8'))
chk('2.3 : derives_v9.json porte les memes planchers que je re-derive',
    all(abs(dv['planchers_corriges_n18'][str(p)] / PL[p] - 1) < 1e-12 for p in (4, 5, 7)))
chk('2.4 : proj4 = 0.2238 est la BORNE HAUTE de MA mesure (0.2195 a 0.2238)',
    dv['proj4'] == PROJ4 and '0.2195 a 0.2238' in PLAT, str(dv['proj4']))
chk('2.5 : le gel cite MA derivation du plancher par son canon (3b12117a58dde698)',
    '3b12117a58dde698' in PLAT and B('derivation_plancher_corrige_machine2_v3.json') == '3b12117a58dde698')
chk('2.6 : la DETTE est declaree au gel -- machine 1 n a pas re-derive proj4',
    're-derivee' in PLAT and 'dette declaree' in PLAT)
note('2.6 portee de la dette', 'ma prescription demandait "le v15 re-derive proj4 chez lui" ; machine 1 '
     'cite par canon et l ECRIT au gel 7bis. La piece reste a une seule machine : je le consigne, '
     'je ne le fais pas mordre (quatre ordres sous S rendent l ecart sans portee)')
v7pl = {p: float(DP / ((F(4, p - 2) + 2) * (F(4, p - 2) + 3))) for p in (4, 5, 7)}
chk('2.7 : le plancher corrige vaut de l ordre de 1e-07 fois celui du v7',
    all(1e-8 < PL[p] / v7pl[p] < 1e-6 for p in (4, 5, 7)),
    str({p: '%.1e' % (PL[p] / v7pl[p]) for p in (4, 5, 7)}))

# ---------------------------------------------------------------- 3. R-v8-1, LE FOND
out()
out('3. R-v8-1 -- G-PLANCHER SUR LE COUPLE CORRIGE : LA PORTE PEUT-ELLE ENCORE MORDRE ?')
q5 = json.load(open('ajustement_modes_libres_Q5_machine2_v1.json', encoding='utf-8'))
S91 = {4: q5['S']['4']['M1'], 5: q5['S']['5']['M1'], 7: q5['S']['7']['M2']}
note('S(p) MESURE au 91 (n = 21, Q5, deux machines)', str({p: '%.4e' % S91[p] for p in sorted(S91)}))
for p, att in ((4, '5.8e-09'), (5, '3.7e-09'), (7, '4.4e-09')):
    chk('3.1 p=%d : le S du gel 7 est bien celui de MON Q5 (%s)' % (p, att),
        '%.1e' % S91[p] == att and att in PLAT, '%.4e' % S91[p])
LEV = 441 / 324
pentes = {4: 0.114, 5: 0.327, 7: 0.726}
mord = {}
for loi, fn in (('pente mesuree 85 -> 91', lambda p: LEV ** pentes[p]),
                ('troncature en dt^4', lambda p: LEV ** 2)):
    qui, rap = [], {}
    for p in (4, 5, 7):
        S18 = S91[p] * fn(p)
        tol = max(S18, PL[p])
        rap[p] = tol / PL[p]
        if tol <= PL[p]:
            qui.append(p)
    mord[loi] = qui
    note('3.2 transport par %s' % loi, 'tol/plancher_corr = %s ; degres mordus %s'
         % ({p: '%.1e' % rap[p] for p in sorted(rap)}, qui or 'aucun'))
    chk('3.2 %s : AUCUN degre mordu sur le couple corrige' % loi, not qui)
    chk('3.2 %s : rapport tol/plancher de 1e+04 a 1e+05 comme le gel l annonce' % loi,
        all(1e3 <= rap[p] <= 1e6 for p in rap), str({p: '%.1e' % rap[p] for p in sorted(rap)}))
note('3.3 contraste avec le v7', 'au 91 les grandeurs du v7 mordaient aux trois degres '
     '(0.869 / 0.208 / 0.042) : c est ce que ma certification du v8 avait etabli et qui fondait R-v8-1')
chk('3.4 : le gel 7 conserve les grandeurs du v7 sous v14_* au lieu de les effacer',
    'v14_*' in PLAT and 'v14_tol_lnA' in SRC15 and 'v14_P_A' in SRC15)
chk('3.5 : le gel dit qu une morsure de 3b est un defaut d INSTRUMENT, pas un reglage',
    'defaut' in PLAT and 'INSTRUMENT' in PLAT and 'pas de v10 de reglage' in PLAT)
chk('3.6 : l attendu de conception ne se calcule PLUS sur le 85',
    'jamais sur le 85' in PLAT and '1.28 / 1.12 / 2.56' not in PLAT)

# ---------------------------------------------------------------- 4. LES CINQ REPRISES
out()
out('4. LES CINQ REPRISES, UNE PAR UNE')
sec7 = T9[T9.index('7. LA PORTE DU PLANCHER'):T9.index('8. LA CASCADE')]
chk('R-v8-1 : la section 7 lit G-plancher sur le COUPLE CORRIGE',
    'COUPLE CORRIGE' in sec7 and 'plancher_corr' in sec7
    and 'max(S(p), plancher_corr(p))' in ' '.join(sec7.split()))
chk('R-v8-1 : une section 7bis derive le plancher corrige', '7bis. LE PLANCHER CORRIGE' in T9)
annonces = (('lnA_M a chaque cellule', 'lnA_M' in SRC15),
            ('q mesure (Richardson)', 'richardson_q' in SRC15),
            ('lnA_R', 'D["lnA_R"]' in SRC15),
            ('S(p)', 'D["S_p"]' in SRC15),
            ('tol_lnA sur le couple corrige', 'D["tol_lnA"] = max(D["S_p"]' in SRC15),
            ('points non lus enumeres', 'D["points_non_lus"]' in SRC15),
            ('plancher corrige', 'plancher_corrige(p)' in SRC15))
for nom, ok in annonces:
    chk('R-v8-2 : ce que 5bis annonce est IMPLEMENTE au v15 -- %s' % nom, ok)
chk('R-v8-2 : la P-A a deux regimes est CALCULEE (v14_* et couple corrige)',
    'D["v14_P_A"]' in SRC15 and 'D["P_A"] = all(abs(v - lnAK)' in SRC15)
sec11 = ' '.join(T9[T9.index('11. LES COMPTES'):T9.index('12. CE QUE CE GEL')].split())
n_att = 18 * 4 + 9 + 27
m11 = re.search(r'comptes \+ sautes == (\d+)', sec11)
chk('R-v8-3 : le compte du gel vaut 108 et egale celui que l instrument derive',
    m11 is not None and int(m11.group(1)) == n_att == 108,
    'gel %s | instrument %d' % (m11.group(1) if m11 else '?', n_att))
chk('R-v8-3 : le quatrieme etage G_dt4 est NOMME dans les comptes', 'G_dt4' in sec11)
srcF9 = open(FEUILLE9, encoding='utf-8').read()
chk('R-v8-4 : la feuille ne tape plus le biais arrondi (2.5425e-07 absent)', '2.5425e-07' not in srcF9)
chk('R-v8-4 : la feuille RE-DERIVE le biais du JSON de la derivation', 'biais_lnA' in srcF9)
for p in (4, 5, 7):
    vrai = {w2: der['C4']['%d|%s' % (p, w2)]['0.0']['biais_lnA'] * LEV for w2 in W2}
    ok = all(abs(dv['predictions_a'][str(p)][w2] / vrai[w2] - 1) < 1e-12 for w2 in W2)
    chk('R-v8-4 p=%d : la prediction (a) est re-derivee par (p, w2), pas tapee' % p, ok,
        str({w2: '%.6e' % vrai[w2] for w2 in W2}))
colles = [l for l in T9.splitlines() if re.match(r'^={10,}[^=\s]', l)]
chk('R-v8-5 : aucun separateur colle a son titre', not colles, '%d ligne(s)' % len(colles))

# ---------------------------------------------------------------- 5. LES TROIS DEFAUTS
out()
out('5. LES TROIS DEFAUTS DE MA PRESCRIPTION, DANS LE SOURCE DU v15')
chk('D-essai-1 : une lecture corrigee absente est une CONSIGNE, jamais une invalidation',
    'NON JOUEE : %d point(s) lisible(s)' in SRC15 and 'exploitable = False' not in SRC15)
chk('D-essai-1 : le v15 CITE le log du premier essai qui l a revele (623bc17a04259d7d)',
    '623bc17a04259d7d' in SRC15)
chk('D-essai-2 : le banc porte un scenario ou le G-plancher CORRIGE mord (G35)', 'G35' in SRC15)
chk('D-essai-2 : et un scenario ou q sort de [3, 5] et les points sont NON LUS (G36)', 'G36' in SRC15)
chk('D-essai-3 : le v15 prend proj4 DERIVE, pas la borne <= 1', '0.2238' in SRC15 and 'PROJ4' in SRC15)
chk('5.4 : le v15 credite l essai de machine 2 par son canon', '0dcfd901a0551d0f' in SRC15)
pin = re.search(r'GEL_ALPHA = \("([^"]+)", "([0-9a-f]{16})", (\d+)\)', SRC15)
chk('5.5 : le pin GEL_ALPHA du v15 porte le chemin, le canon ET la taille du gel v9',
    pin is not None and pin.group(2) == CANON[V9] and int(pin.group(3)) == os.path.getsize(V9)
    and pin.group(1).endswith(V9), pin.group(0) if pin else 'GEL_ALPHA absente')
chk('5.6 : la ligne FIN du gel figure une seule fois',
    T9.count('-- FIN constante_A_pre_enregistrement_v9 --') == 1)

# ---------------------------------------------------------------- 6. LES EPREUVES
out()
out('6. LES EPREUVES DE L INSTRUMENT v15, REJOUEES SUR BOCAL4')
EPR = (('selftest', 'm2_v15_selftest.log', 'm1_v15_selftest.log', r'bilan (\d+/\d+)', '103/103'),
       ('banc qui tue', 'm2_v15_banc.log', 'm1_v15_banc.log', r'bilan (\d+/\d+) scenarios mordent', '58/58'),
       ('pre-vol temoin', 'm2_v15_prevol_temoin.log', 'm1_v15_prevol_temoin.log', r'VERDICT\s+(.+)', None),
       ('pre-vol alpha', 'm2_v15_prevol_alpha.log', 'm1_v15_prevol_alpha.log', r'VERDICT\s+(.+)', None))
for nom, fm2, fm1, motif, att in EPR:
    if not os.path.exists(fm2):
        note(nom, 'NON JOUE ici : journal absent')
        continue
    v2 = re.findall(motif, open(fm2, encoding='utf-8', errors='replace').read())
    v1 = re.findall(motif, open(fm1, encoding='utf-8', errors='replace').read()) if os.path.exists(fm1) else []
    g2 = v2[-1].strip() if v2 else 'motif non trouve'
    g1 = v1[-1].strip() if v1 else 'motif non trouve'
    if att:
        chk('6 %s : %s chez moi' % (nom, att), g2 == att, '%s (journal %s)' % (g2[:70], B(fm2)))
    chk('6 %s : mon resultat == celui de machine 1' % nom, g2 == g1,
        'moi %s | machine 1 %s' % (g2[:60], g1[:60]))
tb1 = open('m1_v15_banc.log', encoding='utf-8', errors='replace').read()
mb = re.search(r'bilan (\d+/\d+) scenarios mordent', tb1)
man = open('MANIFEST_lot_machine1_gel_v9_banc_v15_v1.txt', encoding='utf-8').read()
chk('6.5 : le MANIFESTE du lot decrit correctement le compte du banc',
    (mb is not None) and ('banc %s' % mb.group(1)) in man,
    'le banc rend %s ; le manifeste et la note 0 annoncent "banc 103/103", qui est le compte du '
    'SELFTEST ; la note 3 annonce bien 58/58' % (mb.group(1) if mb else '?'))
tb2 = open('m2_v15_banc.log', encoding='utf-8', errors='replace').read()
for g in ('G35', 'G36'):
    l2 = [l for l in tb2.splitlines() if g + ' lecture corrigee' in l]
    l1 = [l for l in tb1.splitlines() if g + ' lecture corrigee' in l]
    chk('6.6 %s : exerce la lecture corrigee et rend la meme chose sur les deux machines' % g,
        bool(l2) and bool(l1) and l2[0].split(g, 1)[1] == l1[0].split(g, 1)[1],
        (l2[0][15:130] if l2 else 'absent'))

# ---------------------------------------------------------------- 7. LA BASE
out()
out('7. LA BASE DES MODES LIBRES, REJOUEE CHEZ MOI')
FB = 'm2_lecture_v9_base_n21.log'
bl = open(FB, encoding='utf-8', errors='replace').read() if os.path.exists(FB) else ''
mbil = re.search(r'BILAN : (\d+) controles, (\d+) mordent', bl)
chk('7.1 : ma lecture v9 en mode --base rend 0 morsure sur 75 controles',
    mbil is not None and mbil.group(2) == '0', mbil.group(0) if mbil else 'log absent')
note('7.1 portee', 'le controle C0 exige l instrument QUI A PRODUIT le run : le 91 est un run du v13. '
     'Joue avec le v15 il rend 36 morsures a 1e-07 -- ce n est pas un ecart de machine, c est le '
     'mauvais instrument ; joue avec le v13 il rend 0/75')
if os.path.exists('m2_base_modes_libres_n21_v2.json'):
    b2 = json.load(open('m2_base_modes_libres_n21_v2.json', encoding='utf-8'))
    b1 = json.load(open('base_modes_libres_n21_machine1_v2.json', encoding='utf-8'))
    ec = max(abs(b2['modes_p7'][c][f] - b1['modes_p7'][c][f]) for c in b1['modes_p7'] for f in ('a', 'c'))
    chk('7.2 : ma base rejouee == celle de machine 1 a 1e-15 ABSOLU sur (a, c)', ec <= 1e-15, '%.3e' % ec)
    chk('7.3 : ma base v2 reproduit ma base v1 AU BIT (0a7d411197d0603d)',
        B('m2_base_modes_libres_n21_v2.json') == '0a7d411197d0603d',
        B('m2_base_modes_libres_n21_v2.json'))
    note('7.4 canons croises', 'machine 1 rend %s, moi %s : le canon d une base AJUSTEE reste '
         'machine-dependant (etabli a la certification du v8) ; seule la table imprimee se reproduit'
         % (B('base_modes_libres_n21_machine1_v2.json'), B('m2_base_modes_libres_n21_v2.json')))

# ---------------------------------------------------------------- BILAN
out()
sortie = {'bilan': {'chk': bilan['chk'], 'mord': len(bilan['mord']), 'noms': bilan['mord']},
          'canons': {f: B(f) for f in sorted(CANON)},
          'planchers_corriges_re_derives': {str(p): PL[p] for p in PL},
          'S_91_Q5': {str(p): S91[p] for p in S91},
          'plancher_transport': mord,
          'portee': 'certification m2 du gel v9 et de l instrument v15 ; aucun run joue (E19)'}
with open('certif_v9_v15_machine2_v1.json', 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(sortie, fh, sort_keys=True, ensure_ascii=True, indent=1)
out('BILAN : %d controles, %d mordent' % (bilan['chk'], len(bilan['mord'])))
for nm in bilan['mord']:
    out('   MORD : %s' % nm)
with open('certif_v9_v15_machine2_v1.log', 'w', encoding='utf-8', newline='\n') as fh:
    fh.write('\n'.join(lignes) + '\n')
print('log convention B %s ; JSON %s' % (B('certif_v9_v15_machine2_v1.log'), B('certif_v9_v15_machine2_v1.json')))
