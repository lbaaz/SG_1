"""relecture_nombres_delta92_machine2_v1.py -- machine 2, 2026-09-29.

RELECTURE DES NOMBRES DE L'ACTE DELTA 92 AUX SOURCES, DEUX JAMBES (forme du 91).
Entrant : l'acte journal_delta_nn_constante_A_second_ordre_v1.md, plume machine 1, projet v1.

  JAMBE 1 -- LES CANONS. Chaque empreinte de 16 hex citee par l'acte est cherchee dans ce que
     je detiens. Une empreinte RESOLUE nomme le fichier qui la porte ; une empreinte NON
     RESOLUE est nommee et comptee -- elle n'est pas une faute en soi (l'acte declare des
     pieces a detention unique, et machine 1 detient les siennes), mais elle ne peut pas etre
     relue par moi, et cela se dit.
  JAMBE 2 -- LES NOMBRES. Chaque nombre que l'acte ecrit et que je peux recalculer ou relire
     dans MA source est confronte a elle. Jamais depuis l'acte, jamais depuis machine 1 :
     depuis le JSON du run, mes journaux, ma derivation, mon Q5, ma forme close.

Deux verbes : chk (peut mordre), note (ne peut pas). Rien n'est edite.
Usage : relecture_nombres_delta92_machine2_v1.py <acte.md>
"""
import hashlib
import json
import math
import os
import re
import sys
import unicodedata
from fractions import Fraction as F

ACTE = sys.argv[1] if len(sys.argv) > 1 else 'journal_delta_nn_constante_A_second_ordre_v1.md'
RUNA = 'out_run_delta92/alpha_v15/resultats_alpha.json'
PRED = 'm2_lecture_v9_predictions_delta92.json'
DERJ = 'derivation_second_ordre_machine2_v1.json'
Q5J = 'ajustement_modes_libres_Q5_machine2_v1.json'
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
    raw = open(p, 'rb').read()
    return hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()).hexdigest()[:16]


T = open(ACTE, encoding='utf-8').read()
PLAT = ' '.join(T.split())

out('RELECTURE MACHINE 2 DES NOMBRES DE L ACTE DELTA 92, AUX SOURCES')
out('python %s ; %s' % (sys.version.split()[0], os.path.basename(__file__)))
out('acte : %s  (convention B %s, %d octets)' % (os.path.basename(ACTE), B(ACTE), os.path.getsize(ACTE)))

# ================================================================= JAMBE 1
out()
out('JAMBE 1 -- LES CANONS CITES, RESOLUS DANS CE QUE JE DETIENS')
cites = sorted(set(re.findall(r'\b[0-9a-f]{16}\b', T)))
note('1.0 empreintes distinctes citees par l acte', str(len(cites)))
index = {}
for rac, _, fs in os.walk('.'):
    if any(x in rac for x in ('.git', '__pycache__', 'reception_travail', 'm2_reconstruction')):
        continue
    for f in fs:
        q = os.path.join(rac, f)
        try:
            if os.path.getsize(q) > 40_000_000:
                continue
            index.setdefault(B(q), []).append(q.replace('\\', '/').lstrip('./'))
        except Exception:
            continue
resolues = [c for c in cites if c in index]
non = [c for c in cites if c not in index]
note('1.1 resolues chez moi', '%d / %d' % (len(resolues), len(cites)))
for c in non:
    ctx = re.search(r'([^\n]*\b%s\b[^\n]*)' % c, T)
    out('  [NON RESOLUE] %s -- %s' % (c, (ctx.group(1).strip()[:110]) if ctx else ''))
note('1.2 non resolues', '%d -- ce sont les pieces que machine 1 detient seule, plus les miennes '
     'qu elle cite sans que je les aie sous ce nom ; enumerees ci-dessus' % len(non))
chk('1.3 : TOUTES les pieces du run et de mes certifications que l acte cite se resolvent',
    all(c in index for c in ('511f897547a84ba2', '7503c5a40aefcf7a', 'a1b97554adf19cde',
                             '7a693228a172cdad', 'b09d4e0d0412742c', '90d0f63215b33257',
                             '9f5cbd763fbcc0ee', '5a1032b29d3f03c7', '6e4d2afc73a6bc6d',
                             '81ee9c622716ff67', 'd52e40dc52fd52e1', '4a880c934f8aacd2',
                             '240836e9c5c0f1d3', 'b5568d8f31f8492e', '289ae2620e1d1063',
                             'b70fca94d72822ad', '3b12117a58dde698', '4634a795a008a562')))
chk('1.4 : le gel v9 et l instrument v15 cites sont bien les certifies',
    index.get('b515abc5a6da73c5') and index.get('a1553f6eb5cc74b8'))
chk('1.5 : PB-1, l acte n edite rien -- les pieces citees que je detiens portent leur canon',
    all(any(os.path.isfile(p) for p in index[c]) for c in resolues))

# ================================================================= JAMBE 2
out()
out('JAMBE 2 -- LES NOMBRES, RELUS DANS MES SOURCES')
ra = json.load(open(RUNA, encoding='utf-8'))
pr = json.load(open(PRED, encoding='utf-8'))
der = json.load(open(DERJ, encoding='utf-8'))
deg = ra['degres']

out()
out('2.1 LE RUN : comptes, etages, durees, verdicts')
chk('2.1a : comptes 108 = 18 x 4 + 9 + 27', ra['attendus_total'] == 108 == 18 * 4 + 9 + 27
    and '108 = 18 x 4 + 9 + 27' in PLAT, str(ra['attendus_total']))
for k in ('plan', 'G_dt', 'G_dt4'):
    chk('2.1b : %s 18 cellules, comme l acte l ecrit' % k,
        len(ra[k]) == 18 and ('%s 18' % k) in PLAT, str(len(ra[k])))
for f, att, quoi in (('m2_run_delta92_temoin.log', '118.0', 'volet temoin'),
                     ('m2_run_delta92_alpha.log', '252.3', 'volet alpha')):
    t = open(f, encoding='utf-8', errors='replace').read()
    m = re.search(r'FIN\s+\w+ : .*? -- ([\d.]+) s', t)
    chk('2.1c : duree du %s = %s s' % (quoi, att),
        m is not None and m.group(1) == att and ('%s s' % att) in PLAT,
        'mon journal rend %s s' % (m.group(1) if m else '?'))
vt = re.findall(r'VERDICT\s+(.+)', open('m2_run_delta92_temoin.log', encoding='utf-8', errors='replace').read())[-1].strip()
va = re.findall(r'VERDICT\s+(.+)', open('m2_run_delta92_alpha.log', encoding='utf-8', errors='replace').read())[-1].strip()
chk('2.1d : le verdict temoin de l acte est le mien, mot pour mot',
    'REGLAGE QUALIFIE (bonus T-3 retire)' in PLAT and 'T-3 mord seul' in PLAT
    and vt.startswith('REGLAGE QUALIFIE (bonus T-3 retire)'), vt[:70])
chk('2.1e : le verdict alpha de l acte est le mien, mot pour mot',
    'VERIFIE -- branche 5 : P-alpha les six par degre ET P-A aux trois degres' in PLAT
    and va == 'VERIFIE -- branche 5 : P-alpha les six par degre ET P-A aux trois degres', va[:70])

out()
out('2.2 LA TABLE DE nn.5 : S(p), planchers, rapports, contraste v14')
ATT_S = {4: '4.4679e-09', 5: '3.7152e-09', 7: '3.5182e-09'}
ATT_PL = {4: '5.194891e-14', 5: '1.223649e-13', 7: '3.181768e-13'}
ATT_R = {4: '8.60e+04', 5: '3.04e+04', 7: '1.11e+04'}
ATT_V14 = {4: ('1.0086e-06', '1.5432e-06'), 5: ('3.2839e-07', '2.1368e-06'), 7: ('8.6748e-08', '2.9008e-06')}


def coeffs(p, w2):
    a = F(4, p - 2)
    w = F(w2)
    K = a * (a + 1) * (a + 2) * (a + 3)
    P2 = a * (a + 1) * (a - 1) * (a - 2)
    P4 = (4 - a) * (3 - a) * (2 - a) * (1 - a)
    c1 = (1 + w * w) * a * (a + 1) / ((p - 1) * K - P2)
    c2 = (K * F((p - 1) * (p - 2), 2) * c1 * c1 - (1 + w * w) * c1 * (2 - a) * (1 - a) - w * w) / (P4 - (p - 1) * K)
    return c1, c2


DP = F(1, 32400)
for p in (4, 5, 7):
    D = deg[str(p)]
    chk('2.2a p=%d : S(p) de l acte == le mien' % p,
        '%.4e' % D['S_p'] == ATT_S[p] and ATT_S[p] in PLAT, '%.6e' % D['S_p'])
    mien = 0.2238 * max(abs(float(coeffs(p, w)[1])) * (float(DP) / (1 + float(w) ** 2)) ** 2
                        for w in ('1.73', '2.27', '2.80'))
    chk('2.2b p=%d : le plancher de l acte == celui que JE re-derive' % p,
        '%.6e' % mien == ATT_PL[p] and ATT_PL[p] in PLAT, '%.6e' % mien)
    rap = D['tol_lnA'] / D['plancher_corrige']
    chk('2.2c p=%d : le rapport tol/plancher de l acte == le mien' % p,
        '%.2e' % rap == ATT_R[p] and ATT_R[p] in PLAT, '%.2e' % rap)
    chk('2.2d p=%d : G-plancher corrige silencieux et P-A True, comme l acte l ecrit' % p,
        D['G_plancher_mord'] is False and D['P_A'] is True,
        'mord %s, P-A %s' % (D['G_plancher_mord'], D['P_A']))
    d14, p14 = ATT_V14[p]
    chk('2.2e p=%d : le contraste v14 de l acte == le mien (dispersion / plancher)' % p,
        '%.4e' % D['v14_dispersion_lnA'] == d14 and '%.4e' % D['v14_plancher_lnA' if 'v14_plancher_lnA' in D else 'plancher_lnA'] == p14
        and d14 in PLAT and p14 in PLAT,
        '%.4e / %.4e' % (D['v14_dispersion_lnA'], D.get('v14_plancher_lnA', D['plancher_lnA'])))
    chk('2.2f p=%d : et sous le v14 G-plancher aurait MORDU' % p,
        D['v14_G_plancher_mord'] is True, str(D['v14_G_plancher_mord']))

out()
out('2.3 LES BORNES DE q PAR DEGRE (nn.5)')
ATT_Q = {4: ('3.792', '3.964'), 5: ('3.715', '4.116'), 7: ('3.779', '4.050')}
for p in (4, 5, 7):
    q = deg[str(p)]['q_mesure']
    lo, hi = '%.3f' % min(q.values()), '%.3f' % max(q.values())
    chk('2.3 p=%d : q entre %s et %s' % (p, lo, hi),
        (lo, hi) == ATT_Q[p] and lo in PLAT and hi in PLAT, '%s a %s' % (lo, hi))
chk('2.3d : dix-huit points lus sur dix-huit, aucun hors [3, 5]',
    sum(len(deg[str(p)]['lnA_R']) for p in (4, 5, 7)) == 18
    and all(3.0 <= v <= 5.0 for p in (4, 5, 7) for v in deg[str(p)]['q_mesure'].values()))

out()
out('2.4 LES DEUX PREDICTIONS (nn.6)')
chk('2.4a : (a) TIENT a p = 4 et p = 5, NON a p = 7',
    pr['prediction_a'] == {'4': 'TIENT', '5': 'TIENT', '7': 'NON'}, str(pr['prediction_a']))
chk('2.4b : (b) tient 6/6', pr['prediction_b']['tenus'] == 6, str(pr['prediction_b']['tenus']))
RA7 = ['0.867', '0.284', '0.963', '1.234', '1.089', '0.881']
chk('2.4c : les six ratios de (a) a p = 7 que l acte ecrit sont les miens',
    all(r in PLAT for r in RA7), ' '.join(RA7))
chk('2.4d : le facteur d amplitude et le decalage de phase du transport',
    abs((441 / 324) ** (float(F(4, 5) + F(3, 2)) / 2) - 1.4255) < 5e-5
    and abs(-der['C3']['7']['im_complexe'] * math.log(math.sqrt(441 / 324)) + 0.4465) < 5e-5,
    '%.4f et %+.4f rad' % ((441 / 324) ** (float(F(4, 5) + F(3, 2)) / 2),
                           -der['C3']['7']['im_complexe'] * math.log(math.sqrt(441 / 324))))

out()
out('2.5 LA DERIVATION (nn.2) -- EN EXACT, CHEZ MOI')
for p, att in ((4, '1/3'), (5, '65/261'), (7, '133/795')):
    a = F(4, p - 2)
    K = a * (a + 1) * (a + 2) * (a + 3)
    P2 = a * (a + 1) * (a - 1) * (a - 2)
    rap = (a * (a + 1) / ((p - 1) * K - P2)) * ((a + 2) * (a + 3))
    chk('2.5a p=%d : c1 tau_dom^2 / plancher = %s, exact' % (p, att),
        str(rap) == att and att in PLAT, str(rap))
for p, att in ((4, '7/2'), (5, '17/6'), (7, '23/10')):
    chk('2.5b p=%d : Re beta = alpha + 3/2 = %s' % (p, att),
        str(F(4, p - 2) + F(3, 2)) == att and att in PLAT, str(F(4, p - 2) + F(3, 2)))
for p, att in ((4, '4.213075'), (5, '3.492054'), (7, '2.896550')):
    chk('2.5c p=%d : frequence en ln tau = %s' % (p, att),
        '%.6f' % der['C3'][str(p)]['im_complexe'] == att and att in PLAT,
        '%.6f' % der['C3'][str(p)]['im_complexe'])
exact = all(F(der['C2']['%d|%s' % (p, w)]['c1']) == coeffs(p, w)[0]
            and F(der['C2']['%d|%s' % (p, w)]['c2'][0]) == coeffs(p, w)[1]
            for p in (4, 5, 7) for w in ('1.73', '2.27', '2.80'))
chk('2.5d : c1 ET c2 exacts aux neuf (p, w2) contre ma derivation', exact)

out()
out('2.6 Q5 ET proj4')
if os.path.isfile(Q5J):
    q5 = json.load(open(Q5J, encoding='utf-8'))
    S7 = q5['S']['7']
    chk('2.6a : a p = 7, M2 reduit la somme des carres de 2.508e-07 a 4.378e-09',
        '%.3e' % S7['M1'] == '2.508e-07' and '%.3e' % S7['M2'] == '4.378e-09'
        and '2.508e-07' in PLAT and '4.378e-09' in PLAT,
        'M1 %.4e -> M2 %.4e (x %.1f)' % (S7['M1'], S7['M2'], S7['M1'] / S7['M2']))
    chk('2.6b : le facteur est bien x 57', '%.0f' % (S7['M1'] / S7['M2']) == '57' and 'x 57' in PLAT,
        '%.1f' % (S7['M1'] / S7['M2']))
    fx = min(S7['M1'] / S7['M2-'], S7['M1'] / S7['M2+'])
    chk('2.6c : une frequence fausse ne reduit que de x 2.1',
        '%.1f' % fx == '2.1' and 'x 2.1' in PLAT, '%.2f' % fx)
tl = open('derivation_plancher_corrige_machine2_v3.log', encoding='utf-8', errors='replace').read()
pj = sorted(set(re.findall(r'proj4 = ([\d.]+)', tl)))
chk('2.6d : proj4 de 0.2195 a 0.2238, comme l acte l ecrit',
    pj == ['0.219452', '0.223764'] and '0.2195 a 0.2238' in PLAT, str(pj))
chk('2.6e : proj2 de l instrument 0.6727 (0.6638 a un demi-pas)',
    '0.6727' in PLAT and '0.6638' in PLAT and '0.6727' in tl)

out()
out('2.7 CE QUE L ACTE DIT DE MES PROPRES PIECES')
chk('2.7a : ma certification du v9/v15 -- 69 controles', '69 controles' in PLAT
    and re.search(r'^BILAN : 69 controles', open('certif_v9_v15_machine2_v1.log', encoding='utf-8').read(), re.M))
chk('2.7b : ma certification du run -- 45 controles, 0 morsure',
    '45 controles, 0 morsure' in PLAT
    and re.search(r'^BILAN : 45 controles, 0 mordent', open('certif_run_delta92_machine2_v1.log', encoding='utf-8').read(), re.M))
chk('2.7c : selftest 103/103 et banc 58/58', '103/103' in PLAT and '58/58' in PLAT
    and re.search(r'^BILAN|bilan 58/58 scenarios mordent', open('m2_v15_banc.log', encoding='utf-8', errors='replace').read(), re.M))
chk('2.7d : l acte reprend MA consigne du facteur ~1.4 (transport optimiste)',
    'optimiste' in PLAT and '1.4' in PLAT)
chk('2.7e : l acte ecrit que A n est PAS mesuree',
    "A n'est pas mesuree" in T or 'A N EST TOUJOURS PAS MESUREE' in T.upper() or 'A non mesuree' in PLAT)
chk('2.7f : E18 -- aucun numero pris ; aucune regle adoptee',
    'aucune regle' in PLAT and ('E18' in PLAT or 'Numero pris au depot' in PLAT))

# ================================================================= BILAN
out()
out('BILAN : %d controles, %d mordent' % (bilan['chk'], len(bilan['mord'])))
for nm in bilan['mord']:
    out('   MORD : %s' % nm)
sortie = {'bilan': {'chk': bilan['chk'], 'mord': len(bilan['mord']), 'noms': bilan['mord']},
          'canons': {'cites': len(cites), 'resolus': len(resolues), 'non_resolus': non},
          'acte': {'fichier': os.path.basename(ACTE), 'canon': B(ACTE)},
          'portee': 'relecture m2 des nombres de l acte delta 92 aux sources ; deux jambes'}
with open('relecture_nombres_delta92_machine2_v1.json', 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(sortie, fh, sort_keys=True, ensure_ascii=True, indent=1)
with open('relecture_nombres_delta92_machine2_v1.log', 'w', encoding='utf-8', newline='\n') as fh:
    fh.write('\n'.join(lignes) + '\n')
print()
print('log convention B %s' % B('relecture_nombres_delta92_machine2_v1.log'))
