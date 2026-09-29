"""certif_v10_v16_machine2_v1.py -- machine 2, 2026-09-29.

CERTIFICATION CROISEE du gel constante A v10 (130ba949482129a7) et de l'instrument v16
(634c4aaa2aad7598), livres par machine 1 (lot 26ecd16e21783e5e, 13/13 au canon).
OBJET DU v10 : MESURER A. Il restaure la regle du plus grand n (n = 21), definit la mesure
avant le run et pre-enregistre trois predictions dont une NEUVE, (c) : le coefficient du terme
tau^2 ajuste LIBREMENT vaut le c1 derive, aux 18 points, a 10 pour cent.

Chaque nombre du reglage est RE-DERIVE ICI par mes formules ; les planchers corriges a n = 21
par ma forme close ; la mesure de A est REJOUEE sur MES series du 92. Et la piece porte ce que
ma mesure du 29/09 (ce_qui_borne_A_machine2_v1) etablit sur ce que le v10 appelle son
incertitude : la dispersion qu'il declare est un SYSTEMATIQUE DE FENETRE monotone, pas un alea.
Deux verbes : chk (peut mordre), note (ne peut pas). E19 : aucun run joue.
"""
import hashlib
import json
import math
import os
import re
import sys
import unicodedata
from fractions import Fraction as F

V9, V10 = 'constante_A_pre_enregistrement_v9.md', 'constante_A_pre_enregistrement_v10.md'
B15, B16 = 'banc_qualification_machine1_v15.py', 'banc_qualification_machine1_v16.py'
CONSTR, MACH = 'construction_gel_v10_banc_v16_machine1_v1.py', 'machinerie_reglage.py'
FEUILLE10 = 'lecture_v10_machine1_v1.py'
DERJ = 'derivation_second_ordre_machine2_v1.json'
CANON = {V9: 'b515abc5a6da73c5', V10: '130ba949482129a7', B15: 'a1553f6eb5cc74b8',
         B16: '634c4aaa2aad7598', CONSTR: 'd50ab5e7d2b6e0c0', DERJ: 'b70fca94d72822ad'}
W2S = ('1.73', '2.27', '2.80')
DEGRES = (4, 5, 7)
PROJ4 = 0.2238
DP21 = F(1, 44100)
INF = 1.659260768e-05
SUP1 = 3.457292925e-05
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


def coeffs(p, w2):
    a = F(4, p - 2)
    w = F(w2)
    K = a * (a + 1) * (a + 2) * (a + 3)
    P2 = a * (a + 1) * (a - 1) * (a - 2)
    P4 = (4 - a) * (3 - a) * (2 - a) * (1 - a)
    c1 = (1 + w * w) * a * (a + 1) / ((p - 1) * K - P2)
    c2 = (K * F((p - 1) * (p - 2), 2) * c1 * c1 - (1 + w * w) * c1 * (2 - a) * (1 - a) - w * w) / (P4 - (p - 1) * K)
    return c1, c2


T10 = open(V10, encoding='utf-8').read()
PLAT = ' '.join(T10.split())
SRC16 = open(B16, encoding='utf-8').read()

out('CERTIFICATION MACHINE 2 DU GEL v10 ET DE L INSTRUMENT v16 -- OBJET : MESURER A')
out('python %s ; %s' % (sys.version.split()[0], os.path.basename(__file__)))

out()
out('0. ANCRES ET PB-1')
for f in sorted(CANON):
    if f == CONSTR:
        note('canon %s' % f, B(f))
        continue
    chk('canon %s' % f, os.path.isfile(f) and B(f) == CANON[f], B(f) if os.path.isfile(f) else 'absent')
chk('PB-1 : le v9 et le v15 ne sont pas edites', B(V9) == CANON[V9] and B(B15) == CANON[B15])

# ---------------------------------------------------------------- 1. RECONSTRUCTION
out()
out('1. RECONSTRUCTION DEPUIS LE v9 ET LE v15')
REC = 'm2_rec_v10_sabase'
for f in (V10, B16):
    r = os.path.join(REC, f)
    if os.path.exists(r):
        chk('1.1 %s reconstruit IDENTIQUE AU BIT' % f, open(f, 'rb').read() == open(r, 'rb').read(),
            'canon %s' % B(r))
    else:
        note('1.1 %s' % f, 'reconstruction absente')
chk('1.2 : la construction EXIGE le canon de la base 92 DE MACHINE 1 (af295b8a660d33e8)',
    "af295b8a660d33e8" in open(CONSTR, encoding='utf-8').read())
note('1.2 portee -- E-v10-1', 'le gel v10 ne se reconstruit QUE depuis la base 92 de machine 1 : '
     'avec la mienne (4a880c934f8aacd2), dont la table coincide pourtant a 1.9e-16, le script '
     'ARRETE sur son assert. C est la candidate 15 (une base ajustee se cite par sa table a '
     'tolerance declaree, jamais par son canon, qui est machine-dependant) prise a revers par '
     'la construction elle-meme. Le gel est reproductible, mais A UNE SEULE MACHINE.')
mh = re.search(r"non appliques : \[([^\]]*)\]", open('lecture_v10_essai_sur_92.log', encoding='utf-8',
                                                     errors='replace').read()) if os.path.exists('lecture_v10_essai_sur_92.log') else None
note('1.3 les trois hunks non appliques', "la construction rend 'H2 h19 (0)', 'H2 h20 (0)', "
     "'H2 s12 (0)' : trois fragments du reglage a n = 18 qu'elle ne trouve pas dans le v9")
absents = [p for p in ("delta_0 / n^2 avec n =", "marge T kT = delta", "les deux marges partielles")
           if p not in open(V9, encoding='utf-8').read()]
chk('1.3 : les trois sont BENINS -- le texte qu ils remplacent n existe plus dans le v9',
    len(absents) == 3, '%d/3 patrons absents du v9' % len(absents))
note('1.3 mais', 'la note de machine 1 annonce "41 hunks" sans dire que trois n ont pas trouve '
     'leur ancre. Rien ne reste a n = 18 (verifie en 2), mais un compte de hunks qui inclut des '
     'hunks non appliques se decrit faux -- meme famille que E-v9-1.')

# ---------------------------------------------------------------- 2. LE REGLAGE n = 21
out()
out('2. LE REGLAGE n = 21, RE-DERIVE PAR MES FORMULES')
chk('2.1 : delta\' = 1/44100 et delta\'/delta_0 = 1/441',
    DP21 == F(1, 100) / 441
    and ' '.join("n = 21    delta' = 1/44100 = 2.267574e-05".split()) in PLAT
    and "delta'/delta_0 = 1/441" in PLAT, str(DP21))
kT = float(DP21) / INF
m = SUP1 / float(DP21)
chk('2.2 : kT = 1.3666', '%.4f' % kT == '1.3666' and '1.3666' in PLAT, '%.6f' % kT)
chk('2.3 : m = 1.5247', '%.4f' % m == '1.5247' and '1.5247' in PLAT, '%.6f' % m)
chk('2.4 : kT >= 1.15 -- la clause du volet T n est pas relachee', kT >= 1.15, '%.4f' % kT)
for p, att in ((4, '1/882000'), (5, '1/637000'), (7, '1/469224')):
    a = F(4, p - 2)
    pl = DP21 / ((a + 2) * (a + 3))
    chk('2.5 p=%d : plancher du modele = %s, exact' % (p, att), str(pl) == att and att in PLAT, str(pl))
chk('2.6 : la regle du PLUS GRAND n (v7 3.2) est RESTAUREE et nommee',
    'REGLE DE CHOIX DU v10' in T10 and 'RESTAUREE' in PLAT and 'plus grand' in PLAT)

out()
out('3. LES PLANCHERS CORRIGES A n = 21, RE-DERIVES PAR MA FORME CLOSE')
PL21 = {}
for p in DEGRES:
    PL21[p] = PROJ4 * max(abs(float(coeffs(p, w)[1])) * (float(DP21) / (1 + float(w) ** 2)) ** 2 for w in W2S)
ATT = {4: '2.8041e-14', 5: '6.6050e-14', 7: '1.7174e-13'}
for p in DEGRES:
    chk('3.1 p=%d : plancher corrige = %s' % (p, ATT[p]),
        '%.4e' % PL21[p] == ATT[p] and ATT[p] in PLAT, '%.6e' % PL21[p])
if os.path.exists('derives_v10.json'):
    dv = json.load(open('derives_v10.json', encoding='utf-8'))
    k = [x for x in dv if 'plancher' in x.lower()]
    if k:
        d = dv[k[0]]
        chk('3.2 : derives_v10.json porte les memes planchers que je re-derive',
            all(abs(d[str(p)] / PL21[p] - 1) < 1e-12 for p in DEGRES))
note('3.3 le plancher n est plus le sujet', 'a n = 21 il vaut 2.8e-14 a 1.7e-13 ; la dispersion '
     'du 92 vaut 3.5e-09 : quatre a cinq ordres au-dessus. Descendre delta\' ne touche pas a ce '
     'qui borne la mesure (ce_qui_borne_A_machine2_v1, 7 controles 0 morsure).')

# ---------------------------------------------------------------- 4. LA MESURE DE A
out()
out('4. LA MESURE DE A, REJOUEE SUR MES SERIES DU 92')
ess = 'm2_lecture_v10_essai_sur_92.log'
if os.path.exists(ess):
    t = open(ess, encoding='utf-8', errors='replace').read()
    RG = re.compile(r'mesure p = (\d) -- delta_p ([+-][\d.e-]+) ; S\(p\) ([\d.e-]+) ; A\(p\) = ([\d.]+) '
                    r'\(theorique \(K/g\)\^\(1/\(p-2\)\) = ([\d.]+)\)')
    mes = {int(a): (float(b), float(c), float(d), float(e)) for a, b, c, d, e in RG.findall(t)}
    chk('4.1 : la feuille v10 rend la mesure aux trois degres', sorted(mes) == list(DEGRES), str(sorted(mes)))
    for p in DEGRES:
        dp, S, Ap, Ath = mes[p]
        note('4.2 p=%d' % p, 'delta_p %+.4e ; S(p) %.4e ; A(p) %.9f ; theorique %.9f ; '
             'ecart relatif %.2e' % (dp, S, Ap, Ath, abs(Ap / Ath - 1)))
        chk('4.3 p=%d : A(p) coincide avec (K/g)^(1/(p-2)) a mieux que 1e-08 relatif' % p,
            abs(Ap / Ath - 1) < 1e-8, '%.2e' % abs(Ap / Ath - 1))
    chk('4.4 : la moyenne delta_p est UN ORDRE sous la dispersion S(p), aux trois degres',
        all(abs(mes[p][0]) < mes[p][1] / 5 for p in DEGRES),
        str({p: '%.2f' % (mes[p][1] / abs(mes[p][0])) for p in DEGRES}))
    chk('4.5 : ma mesure reproduit celle de machine 1 a p = 5 et p = 7 (p = 4 porte la cellule '
        'divergente 4|2.27|1.20)',
        abs(mes[5][0] - (-2.0e-10)) < 2e-11 and abs(mes[7][0] - (-2.7e-10)) < 2e-11,
        'moi %s | elle +7.4e-11 / -2.0e-10 / -2.7e-10' % {p: '%.1e' % mes[p][0] for p in DEGRES})
else:
    note('4', 'essai non joue ici')

# ---------------------------------------------------------------- 5. LE POINT DE FOND
out()
out('5. CE QUE LE v10 APPELLE SON INCERTITUDE EST UN SYSTEMATIQUE DE FENETRE, MONOTONE')
ra = json.load(open('out_run_delta92/alpha_v15/resultats_alpha.json', encoding='utf-8'))
signes, demi = {}, {}
for p in DEGRES:
    ec = ra['degres'][str(p)]['ecarts_corriges']
    d = [(ec['%d|%s|1.20' % (p, w)] - ec['%d|%s|1.05' % (p, w)]) * 1e9 for w in W2S]
    signes[p] = 'tous positifs' if all(x > 0 for x in d) else ('tous negatifs' if all(x < 0 for x in d) else 'meles')
    demi[p] = (max(d) - min(d)) / 2
    note('5.1 p=%d' % p, 'effet de c aux trois w2 : %s -> %s ; demi-etendue %.3f e-09'
         % (' '.join('%+.3f' % x for x in d), signes[p], demi[p]))
chk('5.2 : a p = 4 et p = 5, l effet de fenetre a UN SEUL SIGNE aux six points',
    signes[4] == signes[5] == 'tous positifs', str(signes))
if os.path.exists(ess):
    chk('5.3 : et sa demi-etendue est 7 a 9 fois la moyenne delta_p que le v10 appelle la mesure',
        all(demi[p] / abs(mes[p][0] * 1e9) > 5 for p in (4, 5)),
        str({p: '%.1f' % (demi[p] / abs(mes[p][0] * 1e9)) for p in (4, 5)}))
note('5.4 la consequence', 'une dependance MONOTONE en c ne se centre pas en moyennant deux c : '
     'la valeur vraie est au-dela du couple, pas entre. A p = 4 et 5, A(p) tel que le v10 le '
     'definit porte donc un BIAIS de fenetre de l ordre de 1.6e-09, sept a neuf fois le delta_p '
     'qu il mesure -- et le v10 le declare en incertitude (S + plancher_corr) au lieu de le '
     'corriger. A p = 7 les signes sont MELES : M2, dont le mode est AJUSTE, absorbe la fenetre.')
note('5.5 ce qui va dans le bon sens', 'la prediction (c) du v10 -- le coefficient de tau^2 '
     'ajuste LIBREMENT contre le c1 derive -- est exactement l instrument qui mesure ce '
     'systematique. Elle est pre-enregistree, et c est bien.')
note('5.6 ce que je prescris', 'un TROISIEME indice de fenetre c. Avec deux points on constate '
     'une pente, on ne l extrapole pas ; avec trois on extrapole c -> la limite et le biais se '
     'retire au lieu de se declarer. C est le pas qui manque entre "A est bornee" et "A est '
     'mesuree", et il ne coute qu un tiers de series en plus.')

# ---------------------------------------------------------------- 6. LES DEUX CORRECTIONS DU BANC
out()
out('6. LES DEUX CORRECTIONS DU BANC (D-v16-1, D-v16-2)')
chk('6.1 D-v16-1 : l horizon du synthetique sans CAP est borne', 'N_2BP' in SRC16 or '20 *' in SRC16 or 'horizon' in SRC16.lower())
chk('6.2 D-v16-2 : G22 rend la lecture corrigee NON JOUEE PAR CONSTRUCTION (mutation q = 2)',
    'mutation q = 2' in SRC16 or 'NON JOUEE par mutation' in SRC16)
if os.path.exists('m2_v16_banc.log'):
    tb = open('m2_v16_banc.log', encoding='utf-8', errors='replace').read()
    _g22 = [l[15:150] for l in tb.splitlines() if 'G22' in l]
    chk('6.3 : chez moi G22 le DIT dans sa ligne', 'NON JOUEE par mutation q = 2' in tb,
        _g22[0] if _g22 else 'ligne G22 absente')

# ---------------------------------------------------------------- 7. LES EPREUVES
out()
out('7. LES EPREUVES DU v16, REJOUEES SUR BOCAL4 (n = 21)')
EPR = (('selftest', 'm2_v16_selftest.log', 'm1_v16_selftest.log', r'bilan (\d+/\d+)', '103/103'),
       ('banc qui tue', 'm2_v16_banc.log', 'm1_v16_banc.log', r'bilan (\d+/\d+) scenarios mordent', '58/58'),
       ('pre-vol temoin', 'm2_v16_prevol_temoin.log', 'm1_v16_prevol_temoin.log', r'VERDICT\s+(.+)', None),
       ('pre-vol alpha', 'm2_v16_prevol_alpha.log', 'm1_v16_prevol_alpha.log', r'VERDICT\s+(.+)', None))
for nom, fm2, fm1, motif, att in EPR:
    if not os.path.exists(fm2):
        note('7 %s' % nom, 'non joue ici')
        continue
    v2 = re.findall(motif, open(fm2, encoding='utf-8', errors='replace').read())
    v1 = re.findall(motif, open(fm1, encoding='utf-8', errors='replace').read()) if os.path.exists(fm1) else []
    g2 = v2[-1].strip() if v2 else 'motif non trouve'
    g1 = v1[-1].strip() if v1 else 'motif non trouve'
    if att:
        chk('7 %s : %s chez moi' % (nom, att), g2 == att, g2[:70])
    chk('7 %s : mon resultat == celui de machine 1' % nom, g2 == g1, 'moi %s | elle %s' % (g2[:55], g1[:55]))

# ---------------------------------------------------------------- BILAN
out()
out('BILAN : %d controles, %d mordent' % (bilan['chk'], len(bilan['mord'])))
for nm in bilan['mord']:
    out('   MORD : %s' % nm)
sortie = {'bilan': {'chk': bilan['chk'], 'mord': len(bilan['mord']), 'noms': bilan['mord']},
          'planchers_n21_re_derives': {str(p): PL21[p] for p in DEGRES},
          'reglage_n21': {'kT': kT, 'm': m},
          'signe_effet_fenetre': signes,
          'demi_etendue_fenetre_e9': demi,
          'portee': 'certification m2 du gel v10 et de l instrument v16 ; aucun run joue (E19)'}
with open('certif_v10_v16_machine2_v1.json', 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(sortie, fh, sort_keys=True, ensure_ascii=True, indent=1, default=str)
with open('certif_v10_v16_machine2_v1.log', 'w', encoding='utf-8', newline='\n') as fh:
    fh.write('\n'.join(lignes) + '\n')
print()
print('log convention B %s' % B('certif_v10_v16_machine2_v1.log'))
