"""certif_v8_v14_machine2_v2.py -- machine 2, 2026-09-18.

v2 = v1 (127c766817486e0d, NON EMISE) + deux FAUX ECHECS retires avant emission : le pin de
l instrument se nomme GEL_ALPHA (et porte aussi la taille), et la table des modes libres se
compare a une TOLERANCE ABSOLUE, pas au chiffre imprime (son ulp atteint le 7e chiffre).

CERTIFICATION CROISEE du gel constante A v8 (800fc6a9a8e56e49) et de l'instrument v14
(dc91676c640d4323), livres par machine 1 (lot b87f7a97f6477449, 11/11 au canon).
Chaque chiffre du gel est RE-DERIVE ICI par mes propres formules (gel alpha v5 sections 6
et 10.3 ; gel v7 sections 3 et 4), jamais repris du script de construction de machine 1 ;
les tables du gel sont extraites par STRUCTURE et comparees valeur par valeur.
Deux verbes : chk (peut mordre), note (ne peut pas). Sorties ecrites avant le bilan.
E19 : aucun run avant le verdict de cette piece.
"""
import hashlib
import json
import math
import os
import re
import sys
import unicodedata
from fractions import Fraction as F

V7, V8 = 'constante_A_pre_enregistrement_v7.md', 'constante_A_pre_enregistrement_v8.md'
B13, B14 = 'banc_qualification_machine1_v13.py', 'banc_qualification_machine1_v14.py'
FEUILLE = 'lecture_v8_machine1_v1.py'
CANON = {V7: 'a2b8463372e1f906', V8: '800fc6a9a8e56e49', B13: '1ac295648490a86c', B14: 'dc91676c640d4323'}
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


T8 = open(V8, encoding='utf-8').read()
PLAT = ' '.join(T8.split())               # blancs normalises : les gels sont replies a 72 colonnes
SRC14 = open(B14, encoding='utf-8').read()

out('CERTIFICATION MACHINE 2 DU GEL v8 ET DE L INSTRUMENT v14')
out('python %s ; %s' % (sys.version.split()[0], os.path.basename(__file__)))
out()
out('0. ANCRES ET PROVENANCE')
for f, c in CANON.items():
    chk('canon %s' % f, B(f) == c, B(f))

# ------------------------------------------------------------------ 1. LE REGLAGE
out()
out('1. LE REGLAGE n = 18, RE-DERIVE PAR MES PROPRES FORMULES')
n, D0, r, M, k, g = 18, F(1, 100), F(1, 10), 20, 2, 0.05
INF, W2 = 1.659260768e-05, (1.73, 2.27, 2.80)
AL = {4: F(2), 5: F(4, 3), 7: F(4, 5)}
A_P = {4: 48.98979, 5: 9.65048, 7: 3.14244}
DISP85 = {4: 1.97714978966701e-06, 5: 2.393510486697892e-06, 7: 7.43220491195018e-06}
DP = D0 / n ** 2
chk("delta' = 1/32400 exact", DP == F(1, 32400), str(DP))
chk("levier delta'/delta_0 = 1/324", DP / D0 == F(1, 324), str(DP / D0))
chk('3.3 : decimale 3.086420e-05', '%.6e' % float(DP) == '3.086420e-05', '%.6e' % float(DP))
kT = float(DP) / INF
SUP1 = min(DISP85[p] * float((AL[p] + 2) * (AL[p] + 3)) for p in AL)
m_marge = SUP1 / float(DP)
chk('3.3 : kT = 1.8601', '%.4f' % kT == '1.8601', '%.6f' % kT)
chk('3.3 : m = 1.1202', '%.4f' % m_marge == '1.1202', '%.6f' % m_marge)
chk('3.1 (T) : kT >= 1.15, la clause du v7 n est PAS relachee', kT >= 1.15, '%.4f' % kT)
chk('3.3 : SUP(1) = 3.457292925e-05', '%.9e' % SUP1 == '3.457292925e-05', '%.9e' % SUP1)
for p in AL:
    pl = DP / ((AL[p] + 2) * (AL[p] + 3))
    att = re.search(r'\n    %d    (1/\d+)\s+([\d.e+-]+)\s+([\d.]+)' % p, T8)
    mine = (str(pl), '%e' % float(pl), '%.4f' % (float(pl) / DISP85[p]))
    chk('3.3 p=%d : plancher exact, decimal, rapport a disp_85' % p, att is not None and mine == att.groups(),
        '%s | gel %s' % (mine, att.groups() if att else 'table absente'))

tau_dom = {w: math.sqrt(float(DP) / (1 + w * w)) for w in W2}
tau_cap = {w: float(r) * tau_dom[w] for w in W2}
for w in W2:
    att = re.search(r'\n    %.2f    ([\d.e+-]+)   ([\d.e+-]+)   ([\d.e+-]+)   ([\d.e+-]+)' % w, T8)
    mine = ('%e' % tau_dom[w], '%e' % tau_cap[w], '%e' % (k * tau_dom[w] / M), '%e' % (tau_cap[w] / M))
    chk('4.3 w2=%.2f : tau_dom, tau_CAP, dt_2a, dt_2b' % w, att is not None and mine == att.groups(),
        '%s | gel %s' % (mine, att.groups() if att else 'table absente'))

sec44 = T8[T8.index('4.4 BASCULE 2b'):T8.index('4.5 CAP')]
sec45 = T8[T8.index('4.5 CAP'):T8.index('4.6 LE COUT')]
for sec, nom, fn in ((sec44, '4.4 bascule 2b', lambda p, w: A_P[p] * (k * tau_dom[w]) ** (-float(AL[p]))),
                     (sec45, '4.5 CAP', lambda p, w: A_P[p] * tau_cap[w] ** (-float(AL[p])))):
    for p in AL:
        att = re.search(r'p = %d\s+([\d.e+-]+)\s+([\d.e+-]+)\s+([\d.e+-]+)' % p, sec)
        mine = tuple('%.4e' % fn(p, w) for w in W2)
        chk('%s p=%d' % (nom, p), att is not None and mine == att.groups(),
            '%s | gel %s' % (mine, att.groups() if att else 'table absente'))
deb = max(g * (A_P[p] * tau_cap[w] ** (-float(AL[p]))) ** (p - 1) for p in AL for w in W2)
chk('4.5 : controle de debordement 1.381e+26', '%.3e' % deb == '1.381e+26', '%.4e' % deb)
chk('4.6 : n_2a nominal = 20 x 17 = 340', '20 x %d = %d' % (n - 1, M * (n - 1)) in PLAT, 'M (n-1) = %d' % (M * (n - 1)))
chk('9 : le signal L-desc vaut le levier 1/324 = 3.0864e-03', '3.0864e-03' in PLAT, '%.4e' % (1 / 324))

# ------------------------------------------------------------------ 2. SECTION 5bis
out()
out('2. SECTION 5bis -- COEFFICIENTS DERIVES ET DEUX PREDICTIONS')
der = json.load(open('derivation_second_ordre_machine2_v1.json', encoding='utf-8'))
chk('la derivation citee est la mienne', B('derivation_second_ordre_machine2_v1.json') == 'b70fca94d72822ad')
for p, att in ((4, '1/3'), (5, '65/261'), (7, '133/795')):
    a = AL[p]
    K = a * (a + 1) * (a + 2) * (a + 3)
    P2 = a * (a + 1) * (a - 1) * (a - 2)
    rap = (a * (a + 1) / ((p - 1) * K - P2)) * ((a + 2) * (a + 3))
    chk('5bis (a) p=%d : c1 tau_dom^2 / plancher = %s' % (p, att), str(rap) == att, str(rap))
for p, att in ((4, '7/2'), (5, '17/6'), (7, '23/10')):
    chk('5bis (b) p=%d : Re beta = alpha + 3/2 = %s' % (p, att), str(AL[p] + F(3, 2)) == att, str(AL[p] + F(3, 2)))
    chk('5bis (b) p=%d : la frequence du gel est celle de ma derivation' % p,
        '%.6f' % der['C3'][str(p)]['im_complexe'] in PLAT, '%.6f' % der['C3'][str(p)]['im_complexe'])
lev = F(1, 32400) / F(1, 44100)
chk('5bis : levier = 441/324 exact', lev == F(441, 324), str(lev))
for p, att in ((4, '3.4606e-07'), (5, '3.5800e-07'), (7, '3.2648e-07')):
    vrai = der['C4']['%d|1.73' % p]['0.0']['biais_lnA'] * float(lev)
    mt = re.search(r'([\d.]+e-07) \(p = %d' % p, PLAT)
    tape = float(mt.group(1)) if mt else float('nan')
    chk('5bis (a) p=%d : la prediction du gel = biais(91) x levier a 1e-4 pres' % p,
        mt is not None and abs(tape / vrai - 1) <= 1e-4,
        'gel %s | re-derive %.6e | ecart relatif %.2e' % (att, vrai, abs(tape / vrai - 1)))
    chk('5bis (a) p=%d : et elle est RE-DERIVEE, non arrondie a la main' % p, '%.4e' % vrai == att,
        'gel %s | %.4e depuis le biais non arrondi %.6e' % (att, vrai, der['C4']['%d|1.73' % p]['0.0']['biais_lnA']))
b7, w7 = float(AL[7] + F(3, 2)), der['C3']['7']['im_complexe']
chk('5bis (b) : amplitude transportee x 1.4255', '%.4f' % (float(lev) ** (b7 / 2)) == '1.4255', '%.6f' % (float(lev) ** (b7 / 2)))
chk('5bis (b) : phase transportee -0.4465 rad', '%.4f' % (-w7 * math.log(math.sqrt(float(lev)))) == '-0.4465',
    '%.6f' % (-w7 * math.log(math.sqrt(float(lev)))))
base_m1 = json.load(open('base_modes_libres_n21_machine1_v1.json', encoding='utf-8'))
base_m2 = json.load(open('m2_base_modes_libres_n21_v1.json', encoding='utf-8'))
ec = max(abs(base_m2['modes_p7'][c][f] - base_m1['modes_p7'][c][f]) for c in base_m1['modes_p7'] for f in ('a', 'c'))
chk('5bis (b) : base rejouee chez moi, ecart ABSOLU <= 1e-15 sur (a, c)', ec <= 1e-15, '%.3e' % ec)
tab = re.findall(r'(7\|[\d.]+\|[\d.]+)\s+([+-][\d.e+-]+)\s+([+-][\d.e+-]+)\s+([\d.e+-]+)\s+([+-][\d.]+)', T8)
chk('5bis (b) : la table du gel porte les SIX points', len(tab) == 6, str(len(tab)))
FMT = {'a': '%+.6e', 'c': '%+.6e', 'amplitude': '%.6e', 'phase': '%+.4f'}
ecarts = [(c, f, v, FMT[f] % base_m2['modes_p7'][c][f], abs(float(v) - float(FMT[f] % base_m2['modes_p7'][c][f])))
          for c, a, cc, am, ph in tab
          for f, v in (('a', a), ('c', cc), ('amplitude', am), ('phase', ph))]
chiffre = [e for e in ecarts if e[2] != e[3]]           # ne coincident pas au chiffre IMPRIME
pire = max(ecarts, key=lambda e: e[4])
chk('5bis (b) : la table du gel se reproduit chez moi a 1e-15 ABSOLU (tolerance, pas le chiffre)',
    pire[4] <= 1e-15, 'pire ecart %.3e sur %s/%s ; %d des 24 ne coincident pas au chiffre imprime'
    % (pire[4], pire[0], pire[1], len(chiffre)))
note('5bis (b) portee de la table', 'elle est imprimee a 7 chiffres sur des coefficients dont l ulp atteint '
     'le 7e ; %d des 24 differe entre machines (%s) : une table ajustee se cite AVEC SA TOLERANCE'
     % (len(chiffre), ', '.join('%s/%s gel %s moi %s' % (c, f, v, w) for c, f, v, w, _ in chiffre) or 'aucun'))
note('5bis (b) canon de la base', 'le gel cite 79099ef4ea51adf6 (machine 1) ; ma base rejouee rend %s : '
     'le canon d une base AJUSTEE est machine-dependant, seule la table imprimee se reproduit'
     % B('m2_base_modes_libres_n21_v1.json'))
srcF = open(FEUILLE, encoding='utf-8').read()
chk('5bis (a) : la feuille RE-DERIVE le biais du 91 au lieu de le taper', '2.5425e-07' not in srcF,
    'BIAIS_91 est tape en dur (%s), arrondi a %%.4e du dossier C4' % re.search(r'BIAIS_91 = \{[^}]*\}', srcF).group(0)[:60])

# ------------------------------------------------------------------ 3. LES COMPTES
out()
out('3. LES COMPTES -- LE GEL CONTRE CE QUE L INSTRUMENT DERIVE')
sec11 = ' '.join(T8[T8.index('11. LES COMPTES'):T8.index('12. CE QUE CE GEL')].split())
att14 = re.search(r'"plan": n_plan, "G_dt": n_plan, "G_k": n_plan, "G_dt4": n_plan', SRC14)
chk('v14 : le quatrieme etage G_dt4 entre dans les attendus de l instrument', att14 is not None)
n_att14 = 18 * 4 + 9 + 27
mgel = re.search(r'comptes \+ sautes == (\d+)', sec11)
chk('gel 11 : le compte ECRIT au gel egale celui que l instrument derive',
    mgel is not None and int(mgel.group(1)) == n_att14,
    'gel %s | instrument plan+G_dt+G_k+G_dt4+G_seuil+G_lignee = %d' % (mgel.group(1) if mgel else '?', n_att14))
chk('gel 11 : le quatrieme etage est NOMME dans les comptes du gel', 'G_dt4' in sec11 or 'dt_2b/4' in sec11,
    'enumeration du gel : %s' % (re.search(r'plan \d+, G_dt \d+, G_k \d+, G_seuil \d+, G_lignee \d+', sec11) or '?'))

# ------------------------------------------------------------------ 4. LA PORTE DU PLANCHER
out()
out('4. G-PLANCHER CONTRE LE DISPOSITIF DU v8 -- LE POINT DE FOND')
run91 = json.load(open('out_run_delta91/alpha_v13/resultats_alpha.json', encoding='utf-8'))
d91 = {int(p): run91['degres'][p]['dispersion_lnA'] for p in ('4', '5', '7')}
note('dispersion LD-12 MESUREE au 91 (n = 21)', str({p: '%.3e' % d91[p] for p in sorted(d91)}))
note('dispersion du 85 dont le gel se sert en 3.3 et 7', str({p: '%.3e' % DISP85[p] for p in sorted(DISP85)}))
pentes = {4: 0.114, 5: 0.327, 7: 0.726}
mord = {}
for loi, fn in (('pente mesuree 85 -> 91', lambda p: float(lev) ** pentes[p]),
                ("troncature en dt^4 (delta'^2)", lambda p: float(lev) ** 2)):
    qui = []
    for p in AL:
        disp18 = d91[p] * fn(p)
        pl = float(DP / ((AL[p] + 2) * (AL[p] + 3)))
        tol = max(disp18, pl)
        if tol <= pl:
            qui.append(p)
        note('transport par %s, p=%d' % (loi, p), 'disp(18) %.3e | plancher %.3e | disp/plancher %.3f | '
             'tol/plancher %.3f%s' % (disp18, pl, disp18 / pl, tol / pl,
                                      '   -> G-PLANCHER MORD' if tol <= pl else ''))
    mord[loi] = qui
chk('4.1 : sous au moins une loi de transport il reste TROIS degres non mordus',
    any(len(q) == 0 for q in mord.values()), 'degres mordus : %s' % mord)
note('4.2 attendu de conception', 'le gel annonce en 7 les rapports 1.28 / 1.12 / 2.56, calcules sur les '
     'dispersions du 85, soit 2.0 / 7.3 / 83.4 fois celles que le run 91 a MESUREES')
srcPA = re.search(r'D\["P_A"\] = ([^\n]+)', SRC14).group(1).strip()
chk('4.3 : la P-A de l instrument lit la tolerance de 5bis (S + residu de Richardson)',
    'S_' in srcPA or 'lnA_R' in srcPA, 'v14 calcule P_A ainsi : %s' % srcPA)
chk('4.4 : la P-A de l instrument lit le lnA CORRIGE (M1/M2)', 'lnA_M1' in SRC14 or 'lnA_R' in SRC14,
    'v14 lit gA_II_sur_K, c est-a-dire l ajustement II NON corrige')
chk('4.5 : la cascade de l instrument connait les modeles de 5bis',
    'M2' in SRC14 and 'modes_libres' in SRC14,
    'les modeles vivent dans la feuille de lecture, hors cascade ; la branche 3b est lue avant eux')

# ------------------------------------------------------------------ 5. FORME
out()
out('5. FORME, STRUCTURE, PB-1')
colles = [l for l in T8.splitlines() if re.match(r'^={10,}[^=\s]', l)]
chk('5.1 : aucun separateur de section colle a son titre', not colles, '%d ligne(s), dont : %s' % (len(colles), (colles[:1] or [''])[0][:90]))
chk('5.2 : la ligne FIN figure une seule fois', T8.count('-- FIN constante_A_pre_enregistrement_v8 --') == 1)
pin = re.search(r'GEL_ALPHA = \("([^"]+)", "([0-9a-f]{16})", (\d+)\)', SRC14)
chk('5.3 : le pin GEL_ALPHA du v14 porte chemin, canon ET taille du gel v8',
    pin is not None and pin.group(2) == CANON[V8] and int(pin.group(3)) == os.path.getsize(V8)
    and pin.group(1).endswith(V8), pin.group(0) if pin else 'GEL_ALPHA absente')
chk('5.4 : PB-1, le v7 et le v13 ne sont pas edites', B(V7) == CANON[V7] and B(B13) == CANON[B13])

# ------------------------------------------------------------------ 6. EPREUVES DE L INSTRUMENT
out()
out('6. LES EPREUVES DE L INSTRUMENT v14, JOUEES SUR BOCAL4')
EPR = (('selftest', 'm2_v14_selftest.log', r'bilan (\d+/\d+)', '103/103'),
       ('banc qui tue', 'm2_v14_banc.log', r'bilan (\d+/\d+) scenarios mordent', '56/56'),
       ('pre-vol temoin', 'm2_v14_prevol_temoin.log', r'VERDICT\s+(.+)', None),
       ('pre-vol alpha', 'm2_v14_prevol_alpha.log', r'VERDICT\s+(.+)', None))
for nom, f, motif, att in EPR:
    if not os.path.exists(f):
        note(nom, 'NON JOUE ici : journal absent')
        continue
    t = open(f, encoding='utf-8', errors='replace').read()
    mm = re.findall(motif, t)
    val = mm[-1].strip()[:90] if mm else 'motif non trouve'
    if att:
        chk('6 %s : %s' % (nom, att), mm and mm[-1].strip() == att, '%s (journal %s)' % (val, B(f)))
    else:
        note('6 %s' % nom, '%s (journal %s)' % (val, B(f)))

# ------------------------------------------------------------------ BILAN
out()
sortie = {'bilan': {'chk': bilan['chk'], 'mord': len(bilan['mord']), 'noms': bilan['mord']},
          'canons': {f: B(f) for f in CANON}, 'plancher_transport': mord,
          'portee': 'certification m2 du gel v8 et de l instrument v14 ; aucun run joue'}
with open('certif_v8_v14_machine2_v2.json', 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(sortie, fh, sort_keys=True, ensure_ascii=True, indent=1)
out('BILAN : %d controles, %d mordent' % (bilan['chk'], len(bilan['mord'])))
for nm in bilan['mord']:
    out('   MORD : %s' % nm)
with open('certif_v8_v14_machine2_v2.log', 'w', encoding='utf-8', newline='\n') as fh:
    fh.write('\n'.join(lignes) + '\n')
print('log convention B %s ; JSON %s' % (B('certif_v8_v14_machine2_v2.log'), B('certif_v8_v14_machine2_v2.json')))
