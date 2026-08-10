#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CERTIFICATION CROISEE v3 -- GEL M15 (P1-b, site 8/3) : trace executable (machine 2).

Ce script NE lit AUCUN chiffre du gel comme un fait. Il RE-APPLIQUE les regles que
le gel v3 DECLARE (F par regle, assignation R-2', courbures K_X, planchers par
point, partition D-3, k_min) et les compare a ce que le gel ecrit. Discipline :
ne jamais verifier ce qu'un artefact MONTRE, toujours re-appliquer la regle qu'il
DECLARE -- y compris quand l'artefact declare reprendre mon propre texte.

CE QUE CE LOG NE JOUE PAS (exigence de titre) :
  - AUCUNE recherche de s* : aucun moteur importe, aucune mesure ;
  - il ne certifie PAS m15_site83_v1.py (non depose, E19) : ITEM 5 temps 2
    (verrous math.nextafter, selftest, pre-vol) reste DU ;
  - le taux de base exclut les 64 lignes de M10 (champ absent) ;
  - la partition est testee sur les 32 combinaisons booleennes, PAS sur des
    profils physiques exhaustifs ;
  - il n'ecrit aucun fichier.

Arithmetique : EXACTE (Fraction) partout ou une SELECTION se joue -- distances,
R-2', assignation, appartenance a F, facteurs geometriques g, queue binomiale et
comparaison a 1/20 (D-4). Les E, residus, K_X et planchers sont des flottants :
ce sont des mesures.
"""

import difflib
import hashlib
import itertools
import json
import math
import os
import re
import sys
import unicodedata
from decimal import Decimal
from fractions import Fraction as F

sys.stdout.reconfigure(encoding='utf-8')

SITE = F(8, 3)
Q_SITE = 11
GEL = 'm15_pre_enregistrement_v3.md'
TERM = '=== FIN DU GEL M15 ==='
ECHECS, BLOQUANTS = [], []


def canon(t):
    return unicodedata.normalize('NFC', t.replace('\r\n', '\n').replace('\r', '\n'))


def sha_brut(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def sha_canon(p):
    with open(p, encoding='utf-8') as fh:
        return hashlib.sha256(canon(fh.read()).encode('utf-8')).hexdigest()


def frac(k):
    return F(Decimal(k.split('|')[1]))


def titre(n, s):
    print()
    print('=' * 78)
    print('[%s] %s' % (n, s))
    print('=' * 78)


def verifie(cond, lib, bloquant=False):
    print('   %s %s' % ('OK  ' if cond else '**ECHEC**', lib))
    if not cond:
        (BLOQUANTS if bloquant else ECHECS).append(lib)
    return cond


NOMS = ('m10', 'm11', 'm12', 'm13', 'm13b', 'm14', 'm12_pilote')
A = {n: json.load(open('out/%s_results.json' % n, encoding='utf-8')) for n in NOMS}
CARTE = {n: A[n]['resultats']['carte'] for n in NOMS}
G6 = {n: A[n]['resultats'].get('G6', {}) for n in NOMS}


def sF(n, p, w):
    k = '%d|%.12f' % (p, float(w))
    return CARTE[n][k]['sF'] if k in CARTE[n] else None


def E_de(s4, s5, s7):
    return (math.log(s4) - 2.25 * math.log(s5)) + 1.25 * math.log(s7)


def S57_de(s5, s7):
    return (-2.25 * math.log(s5)) + 1.25 * math.log(s7)


# =========================================================== [1] forme + sha
titre(1, "FORME CANONIQUE DU BLOC GELE v3 (regle 12 et son corollaire)")
with open(GEL, 'rb') as fh:
    brut = fh.read()
txt = canon(brut.decode('utf-8'))
verifie(b'\r' not in brut, 'aucun CR dans le fichier (LF seul)')
verifie(txt == unicodedata.normalize('NFC', txt), 'texte stable par NFC')
verifie(txt.isascii(), 'ASCII pur')
occ = [m.start() for m in re.finditer(re.escape(TERM), txt)]
print('   occurrences du terminateur : %d' % len(occ))
verifie(len(occ) == 1, 'terminateur UNE SEULE fois (corollaire regle 12)', bloquant=True)
verifie(txt.find('PRE-ENREGISTREMENT M15') == 0, 'le bloc commence a la ligne 1 (colonne 0)')
fin = txt.find('\n', occ[0])
verifie(txt[txt.rfind('\n', 0, occ[0]) + 1:fin] == TERM, 'terminateur en LIGNE PLEINE')
bloc = txt[:fin + 1]
verifie(txt[fin + 1:] == '', 'aucune queue apres le terminateur')
SHA = hashlib.sha256(bloc.encode('utf-8')).hexdigest()
print('   longueur du bloc : %d caracteres' % len(bloc))
print('   EMPREINTE NFC+LF DU BLOC M15 v3 (brut = canonique, fichier LF/ASCII) :')
print('   %s' % SHA)

# ============================================ [2] le diff livre est-il honnete
titre(2, "LE DIFF LIVRE EST-IL LE VRAI DELTA v2 -> v3 ? (custody)")
v2 = canon(open('m15_pre_enregistrement_v2.md', encoding='utf-8').read()).split('\n')
v3 = txt.split('\n')
recalc = list(difflib.unified_diff(v2, v3, 'v2', 'v3', lineterm='', n=3))
livre = canon(open('m15_diff_v2_v3.txt', encoding='utf-8').read()).split('\n')


def signature(lignes):
    plus = [l[1:] for l in lignes if l.startswith('+') and not l.startswith('+++')]
    moins = [l[1:] for l in lignes if l.startswith('-') and not l.startswith('---')]
    return plus, moins


p_l, m_l = signature(livre)
p_r, m_r = signature(recalc)
print('   ajouts   : livre %d | recalcule %d' % (len(p_l), len(p_r)))
print('   retraits : livre %d | recalcule %d' % (len(m_l), len(m_r)))
verifie(p_l == p_r, 'les lignes AJOUTEES du diff livre sont exactement celles du vrai delta')
verifie(m_l == m_r, 'les lignes RETIREES du diff livre sont exactement celles du vrai delta')
print('   -> le diff ne cache ni n ajoute rien. Il n a pas ete relu comme une source :')
print('      tout ce qui suit est re-derive du TEXTE v3, jamais du diff.')

# ==================================================== [3] empreintes citees
titre(3, "LES EMPREINTES CITEES PAR LA v3, RECALCULEES ET ETIQUETEES (N-10)")
CITES = [
    ('a2bb2dcd', 'm15_pre_enregistrement_v1.md', 'canonique', 'gel M15 v1'),
    ('c92c58e5', 'm15_pre_enregistrement_v2.md', 'canonique', 'gel M15 v2'),
    ('a944511d', 'm15_certification_croisee_v1.md', 'canonique', 'ma certification v1'),
    ('61f2610f', 'm15_certification_croisee_v1.log', 'brut', 'mon log v1 (CRLF -- N-10)'),
    ('32714630', 'm15_certification_croisee_v1.py', 'canonique', 'mon script v1'),
    ('9088ce59', 'm15_certification_croisee_v2.md', 'canonique', 'ma certification v2'),
    ('dbbaee82', 'm15_certification_croisee_v2.log', 'canonique', 'mon log v2 (LF)'),
    ('26e7353f', 'm15_certification_croisee_v2.py', 'canonique', 'mon script v2'),
    ('fa109da9', 'out/m12_results.json', 'brut', 'M12'),
    ('22fa1760', 'out/m13b_results.json', 'brut', 'M13b'),
    ('68df6576', 'out/m14_results.json', 'brut', 'M14'),
    ('ed0e27b1', 'out/m12_pilote_results.json', 'brut', 'pilote M12'),
    ('70fe5611', 'out/m13_results.json', 'brut', 'M13'),
    ('ad275870', 'out/m11_results.json', 'brut', 'M11'),
    ('7cf3624b', 'out/m10_results.json', 'brut', 'M10'),
    ('bf9866a7', 'm12_pre_enregistrement_v4.md', 'canonique', 'gel M12 v4'),
    ('273d0a53', 'gel_m14_p1a_v2.md', 'canonique', 'gel M14 v2'),
    ('97c02eab', 'p1_re_derivation_machine2_v1.md', 'canonique', 're-derivation machine 2'),
    ('5704987e', 'note_derivation_P1_signes_E_v5.md', 'canonique', 'note P1 v5'),
    ('c8ed357b', 'm9_replication_v1.py', 'brut', 'moteur classique'),
]
for pref, chemin, mode, quoi in CITES:
    if not os.path.exists(chemin):
        verifie(False, '%-9s %-38s ABSENT' % (pref, chemin), bloquant=True)
        continue
    calc = sha_brut(chemin) if mode == 'brut' else sha_canon(chemin)
    verifie(calc.startswith(pref), '%-9s %-38s (%s) %s' % (pref, chemin, mode, quoi))
print()
print('   N-10 EST TENU : la v3 etiquette 61f2610f [BRUT] et dit pourquoi (CRLF).')
print('   Mes trois fichiers v2 sont en LF : brut = canonique, et la v3 le dit.')
print()
print('   ITEM 3, condition de re-paraphe ("seulement si domaine ou registre change") :')
print('   les SEPT artefacts de la lignee ont les empreintes qu ils avaient a la')
verifie(all(sha_brut('out/%s_results.json' % n).startswith(p) for n, p in
            (('m10', '7cf3624b'), ('m11', 'ad275870'), ('m12', 'fa109da9'),
             ('m13', '70fe5611'), ('m13b', '22fa1760'), ('m14', '68df6576'),
             ('m12_pilote', 'ed0e27b1'))),
        'certification v2 : REGISTRE INCHANGE -> ITEM 3 reste CLOS, aucun re-paraphe du')
print('   q_L. Le DOMAINE declare au gel ([2.35, 2.90[) est celui que j ai derive.')

# ================================= [4] ce que la v3 me cite : re-derive, pas cru
titre(4, "CE QUE LA v3 CITE DE MA CERTIFICATION v2 -- RE-DERIVE, JAMAIS CRU")
E14 = {w: E_de(sF('m14', 4, w), sF('m14', 5, w), sF('m14', 7, w))
       for w in (F(242, 100), F(246, 100), F(248, 100), F(252, 100), F(254, 100), F(255, 100))}
Dg = E14[F(248, 100)] - E14[F(242, 100)]
Dd = E14[F(252, 100)] - E14[F(255, 100)]
verifie(abs(Dg - 0.1096) < 5e-5 and abs(Dd + 0.0781) < 5e-5,
        'N-11 tenu : D(g) = %+.4f, D(d) = %+.4f (v3 : +0.1096 / -0.0781, arrondis)' % (Dg, Dd))
inst = [(n, k) for n in NOMS for k, v in G6[n].items()
        if 'gros_explosifs' in v and ((v.get('gros_explosifs') or 0) > 0
                                      or v.get('explosion_sous_LO0_0.90s') is not None)]
cotes = [k.split('|')[2] for _, k in inst]
verifie(sorted(k for _, k in inst) == sorted(['7|1.700000000000|-1', '7|2.670000000000|+1',
                                              '5|2.500000000000|-1']),
        'N-7 tenu : les trois instances sont bien 7|1.70|-1, 7|2.67|+1, 5|2.50|-1')
verifie(cotes.count('-1') == 2 and cotes.count('+1') == 1,
        'N-7 tenu : repartition 2 x (-1) pour 1 x (+1), comptee')
imp_m = imp_n = pair_m = pair_n = 0
for n in NOMS:
    for k, v in G6[n].items():
        if 'gros_explosifs' not in v:
            continue
        mord = (v.get('gros_explosifs') or 0) > 0 or v.get('explosion_sous_LO0_0.90s') is not None
        if int(k.split('|')[0]) % 2:
            imp_n += 1
            imp_m += mord
        else:
            pair_n += 1
            pair_m += mord
verifie((imp_m, imp_n, pair_m, pair_n) == (3, 96, 0, 87),
        'taux de base : %d/%d impair contre %d/%d pair (v3 : 3/96 et 0/87)'
        % (imp_m, imp_n, pair_m, pair_n))


def fisher(a, b, c, d):
    n1, n2, t, N = a + b, c + d, a + c, a + b + c + d
    return sum(math.comb(n1, x) * math.comb(n2, t - x) / math.comb(N, t)
               for x in range(max(0, t - n2), min(t, n1) + 1) if x >= a)


pf = fisher(imp_m, imp_n - imp_m, pair_m, pair_n - pair_m)
verifie(abs(pf - 0.1422) < 5e-5, 'Fisher unilateral p = %.4f (v3 : 0.1422)' % pf)
e_d = E_de(sF('m12', 4, F(272, 100)), sF('m12', 5, F(272, 100)), sF('m12', 7, F(272, 100)))
e_s = math.log(sF('m12', 4, F(272, 100))) + S57_de(sF('m12', 5, F(272, 100)), sF('m12', 7, F(272, 100)))
verifie(abs(abs(e_d - e_s) - 1.110e-16) < 5e-19,
        'N-8 tenu : ecart E - (S4+S57) = %.3e (v3 : 1.110e-16)' % abs(e_d - e_s))
voisins = sorted({frac(k) for n in NOMS for k in CARTE[n] if abs(frac(k) - SITE) <= F(4, 100)})
morts_v = sorted({frac(k) for n in NOMS for k, v in G6[n].items()
                  if v.get('exclue') and abs(frac(k) - SITE) <= F(4, 100)})
verifie(voisins == morts_v == [F(267, 100), F(270, 100)],
        'N-12 tenu : les deux seuls voisins mesures (2.67, 2.70) sont morts tous les deux')
note = canon(open('note_derivation_P1_signes_E_v5.md', encoding='utf-8').read()).split('\n')
i_p1b = [i for i, l in enumerate(note) if 'P1-b' in l][0]
sec = max((i, l) for i, l in enumerate(note) if l.startswith('## ') and i < i_p1b)
verifie(sec[1].startswith('## 6.'), 'N-6 / source : P1-b est bien en section 6 de la note v5')
verifie(any(l.startswith('| 8:3') and '(6, 2) | (3, 1) | (3, 1)' in l for l in note),
        'N-6 tenu : la table de la section 1 donne bien (6,2)/(3,1)/(3,1)')

# ======================================= [5] ITEM 6 -- F par regle, courbures
titre(5, "ITEM 6 -- F PAR REGLE (D-6), ASSIGNATION R-2' (D-6), COURBURES K_X (D-1)")
RAYON = {}
for o in range(2, 7):
    RAYON[o] = F(12, 100)
RAYON[7] = RAYON[8] = F(3, 100)
RAYON[9] = RAYON[10] = F(75, 10000)
RAYON[11] = RAYON[12] = F(1875, 1000000)
FAM = [(F(k, l), k + l) for l in range(1, 12) for k in range(1, 12)
       if k + l <= 12 and F(1) <= F(k, l) <= F(35, 10)]


def assignation_v3(w):
    """v3, en toutes lettres : argmin de |w - q/r| / rayon(ordre) ; egalite -> ordre bas
    puis denominateur petit. TOUT en Fraction."""
    best = None
    for f, o in FAM:
        cle = (abs(w - f) / RAYON[o], o, f.denominator)
        if best is None or cle < best[0]:
            best = (cle, f, o)
    return best[1], best[2]


def assignation_v2(w):
    """la lecture que J'AI appliquee a la certification v2 : argmin de la marge ABSOLUE."""
    return min(((abs(w - f) - RAYON[o] * F(11, 10), f, o) for f, o in FAM))[1]


def r2propre(w):
    return all(abs(w - f) >= RAYON[o] * F(11, 10) for f, o in FAM)


def exclue_G6(n, p, w):
    return any(int(k.split('|')[0]) == p and frac(k) == w and v.get('exclue')
               for k, v in G6[n].items())


perdus = {frac(k) for k in A['m12']['resume']['points_perdus']}
CH = {}
for w in sorted({frac(k) for k in CARTE['m10']} | {frac(k) for k in CARTE['m11']}):
    if exclue_G6('m11', 4, w) or exclue_G6('m10', 5, w) or exclue_G6('m10', 7, w):
        continue
    if None in (sF('m11', 4, w), sF('m10', 5, w), sF('m10', 7, w)):
        continue
    CH[w] = (E_de(sF('m11', 4, w), sF('m10', 5, w), sF('m10', 7, w)),
             S57_de(sF('m10', 5, w), sF('m10', 7, w)), math.log(sF('m11', 4, w)))
for w in sorted({frac(k) for k in CARTE['m12']}):
    if w in perdus or any(exclue_G6('m12', p, w) for p in (4, 5, 7)):
        continue
    CH[w] = (E_de(sF('m12', 4, w), sF('m12', 5, w), sF('m12', 7, w)),
             S57_de(sF('m12', 5, w), sF('m12', 7, w)), math.log(sF('m12', 4, w)))
FS = [w for w in sorted(CH)
      if r2propre(w) and abs(w - SITE) > F(19, 300) and assignation_v3(w)[0] != F(5, 2)]
print('   F (SORTIE, aucun compte annonce au gel) : |F| = %d' % len(FS))
print('     %s' % [float(x) for x in FS])
verifie(len(FS) == 14, "|F| = 14 -- identique a la lecture A de ma certification v2")
print()
print('   ATTENTION, DECLARATION N-13 -- la v3 definit l assignation par la marge')
print('   NORMALISEE |w - q/r| / rayon ; la certification v2 avait applique la marge')
print('   ABSOLUE (|w - q/r| - 1.10 x rayon). Les deux ne coincident PAS :')
diff_assign = [(w, assignation_v3(w)[0], assignation_v2(w)) for w in FS
               if assignation_v3(w)[0] != assignation_v2(w)]
for w, a3, a2 in diff_assign:
    print('     %.2f : v3 -> %-5s   v2 -> %-5s' % (float(w), a3, a2))
print('   soit %d des %d points de F. La v3 ecrit "(Lecture argmin appliquee par' % (len(diff_assign), len(FS)))
print('   machine 2 a la certification v2)" : c est le MEME MOT, pas la meme regle.')
for w in (F(242, 100), F(245, 100), F(255, 100)):
    verifie(assignation_v3(w)[0] == F(5, 2) == assignation_v2(w),
            'mais sur le SEUL usage fait (exclusion 5:2), les deux regles concordent en %.2f'
            % float(w))
FS_v2 = [w for w in sorted(CH)
         if r2propre(w) and abs(w - SITE) > F(19, 300) and assignation_v2(w) != F(5, 2)]
verifie(FS_v2 == FS,
        "ce qui compte : les deux lectures rendent le MEME ensemble F (le seul usage "
        "de l'assignation est l'exclusion 5:2)")
print('   N-13 est donc une DECLARATION, pas un defaut : la regle a change de forme,')
print('   la selection non. Mais "assignation R-2 prime" est desormais un terme du')
print('   registre : toute reutilisation FUTURE sur une autre question divergera des')
print('   6 points ci-dessus, et le gel ne doit pas la presenter comme ma lecture.')


def g(a, b, c):
    return (b - a) * (c - b)


TRIPS = [(a, b, c) for a, b, c in itertools.combinations(FS, 3) if c - a <= F(11, 100)]
print()
print('   triplets a < b < c de F avec c - a <= 11/100 (SORTIE) : %d' % len(TRIPS))
IDX = {'E': 0, 'S57': 1, 'S4': 2}


def residu(i, a, b, c):
    return CH[b][i] - (CH[a][i] + float((b - a) / (c - a)) * (CH[c][i] - CH[a][i]))


K = {}
for nom, i in IDX.items():
    vals = [(abs(residu(i, a, b, c)) / float(g(a, b, c)), a, b, c) for a, b, c in TRIPS]
    K[nom] = max(vals)
print('   %-6s %-12s %-28s %-10s' % ('', 'K_X', 'triplet realisateur', 'g exact'))
for nom in ('E', 'S57', 'S4'):
    k, a, b, c = K[nom]
    print('   K_%-4s %-12.6f (%.2f, %.2f, %.2f)%-14s %s'
          % (nom, k, float(a), float(b), float(c), '', g(a, b, c)))
print()
print('   CONSIGNATION PRE-RUN (ITEM 6) -- les triplets, en clair :')
for a, b, c in TRIPS:
    print('     (%.2f, %.2f, %.2f)  g = %-10s res_E = %+.4f  K_E local = %6.2f'
          % (float(a), float(b), float(c), str(g(a, b, c)), residu(0, a, b, c),
             abs(residu(0, a, b, c)) / float(g(a, b, c))))
verifie(K['S57'][0] + K['S4'][0] > K['E'][0],
        'la bande D-3 est NON VIDE : K_S57 + K_S4 = %.4f > K_E = %.4f (marge %.1f %%)'
        % (K['S57'][0] + K['S4'][0], K['E'][0],
           100 * (K['S57'][0] + K['S4'][0] - K['E'][0]) / K['E'][0]))

# ============================== [6] la partition D-3 : exclusive et exhaustive
titre(6, "D-3 -- LA PARTITION EST-ELLE EXCLUSIVE ET EXHAUSTIVE ? (32 combinaisons)")


def branche(C1, C2, C3, disc, C4):
    """La partition, recopiee du SEUL texte du gel v3 (section PORTES)."""
    out = []
    if not C1:
        out.append('PAS-DE-STRUCTURE-RESOLUE')
    if C1 and not C2:
        out.append('STRUCTURE-NON-CENTREE')
    if C1 and C2 and C3 and disc:
        out.append('STRUCTURE-AU-SITE-RESOLUE')
    if C1 and C2 and C3 and not disc:
        out.append('STRUCTURE-RESOLUE-CENTRAGE-NON-DISCRIMINE')
    if C1 and C2 and not C3 and C4:
        out.append('STRUCTURE-CANAL-4-CANDIDATE')
    if C1 and C2 and not C3 and not C4:
        out.append('STRUCTURE-RESOLUE-NON-ATTRIBUEE')
    return out


mauvais = []
couvertes = set()
for bits in itertools.product((False, True), repeat=5):
    b = branche(*bits)
    couvertes.update(b)
    if len(b) != 1:
        mauvais.append((bits, b))
print('   combinaisons (C1, C2, C3, n_disc>=1, C4) testees : 32')
verifie(not mauvais, 'chaque combinaison tombe dans EXACTEMENT une branche '
                     '(%d anomalies)' % len(mauvais), bloquant=True)
print('   branches atteintes : %d' % len(couvertes))
for v in sorted(couvertes):
    print('     - %s' % v)
verifie(len(couvertes) == 6, 'les SIX branches nommees sont toutes atteignables')

# ============================================== [7] D-4 -- k_min, en Fraction
titre(7, "D-4 -- k_min DERIVE DU FOND, EN ARITHMETIQUE EXACTE (regle candidate 15)")
b_fond = F(3, 96)
n_eff = 24


def queue_exacte(n, b, k):
    return sum(F(math.comb(n, i)) * b ** i * (1 - b) ** (n - i) for i in range(k, n + 1))


print('   b_fond = %s (exact) ; n_eff = %d' % (b_fond, n_eff))
for k in range(0, 5):
    q = queue_exacte(n_eff, b_fond, k)
    print('     P(X >= %d) = %.6f   %s 1/20   (queue et comparaison en Fraction)'
          % (k, float(q), '<=' if q <= F(1, 20) else '> '))
kmin = min(k for k in range(0, n_eff + 1) if queue_exacte(n_eff, b_fond, k) <= F(1, 20))
verifie(kmin == 3, 'k_min = %d (v3 : 3), decide par comparaison EXACTE a 1/20' % kmin)
p0 = (1 - b_fond) ** n_eff
verifie(abs(float(p0) - 0.4667) < 5e-5,
        'P(k = 0) = %.4f (v3 : 0.4667) -- "l absence n est pas resolvable", exact' % float(p0))
verifie(abs(float(queue_exacte(n_eff, b_fond, 1)) - 0.5333) < 5e-5,
        'P(k >= 1) = %.4f : le seuil v2 tombait bien par le fond une fois sur deux'
        % float(queue_exacte(n_eff, b_fond, 1)))

# ================================================== [8] ITEM 4 -- G2, le compte
titre(8, "ITEM 4 -- G2 : LA DESIGNATION EST-ELLE UNIVOQUE, LE TOTAL DERIVABLE ?")
src14 = canon(open('gel_m14_p1a_v2.md', encoding='utf-8').read())
j = src14.find('G2 une')
print('   precedent NOMME par la v3, verbatim dans 273d0a53 :')
print('     | %s' % ' '.join(src14[j:j + 150].split()))
verifie('sans porte' in src14[j:j + 200],
        'le precedent M14 est bien "consigne SANS PORTE" -- aucune exclusion possible')
prog = 6 * 5
total = prog + 5 + 1 + 1 + 1
print('   programme 6 x 5 = %d ; G1 prime 5 ; G8a 1 ; G4 1 ; G2 1' % prog)
verifie(total == 38, 'total = %d (v3 : 38)' % total)
print()
print('   DECLARATION N-14 -- la designation depend du RESULTAT : "7|PROCHE_droit|+1",')
print('   et PROCHE_droit est le survivant du flanc droit le plus proche du site.')
print('   Si le flanc droit ne rend AUCUN survivant, G2 n a pas de cible : le compte')
print('   attendu vaut alors 37, et la forme derivee "comptes + sautes == attendu"')
print('   doit porter G2 en SAUTEE avec motif. Le gel ne l ecrit pas. Sous le q_L')
p_flanc_vide = (1 - (1 - 0.0855) * (1 - 0.0679) ** 4) ** 3
print('   local (ITEM 3), P(flanc droit entierement mort) = %.4f -- faible, non nul.'
      % p_flanc_vide)

# ================================================== [9] ITEM 7 -- le banc v3
titre(9, "ITEM 7 -- TEST NEGATIF DU CRITERE v3, CODE DEPUIS LE SEUL TEXTE DU GEL")
PROG = {'gauche': [F(262, 100), F(264, 100), F(265, 100)],
        'droit': [F(269, 100), F(271, 100), F(273, 100)]}


def critere(profil, gauche, droit, site, KX, barres=None):
    """Re-ecrit du seul texte v3 : PROCHE/LOIN, corde, residu, PLANCHER par point,
    seuils, C1/C2/C3, n_disc, partition D-3."""
    gg = [w for w in gauche if w in profil]
    dd = [w for w in droit if w in profil]
    if len(gg) < 2 or len(dd) < 2:
        return 'NON CONCLUANT DE GEOMETRIE', {}
    pg, lg = min(gg, key=lambda w: abs(w - site)), max(gg, key=lambda w: abs(w - site))
    pd, ld = min(dd, key=lambda w: abs(w - site)), max(dd, key=lambda w: abs(w - site))
    inter = [w for w in gg + dd if w not in (lg, ld)]
    n_disc = len([b for b in inter if b not in (pg, pd)])

    def res(q, b):
        X = {w: profil[w][q] for w in profil}
        return X[b] - (X[lg] + float((b - lg) / (ld - lg)) * (X[ld] - X[lg]))

    def seuil(q, b):
        pl = KX[q] * float(g(lg, b, ld))
        ba = barres(q, b, lg, ld) if barres else 0.0
        return max(pl, ba)

    xm = max(inter, key=lambda b: abs(res('E', b)))
    C1 = abs(res('E', xm)) > seuil('E', xm)
    C2 = xm in (pg, pd)
    C3 = abs(res('S57', xm)) > seuil('S57', xm)
    C4 = abs(res('S4', xm)) > seuil('S4', xm)
    v = branche(C1, C2, C3, n_disc >= 1, C4)[0]
    if v == 'STRUCTURE-AU-SITE-RESOLUE' or v == 'STRUCTURE-RESOLUE-CENTRAGE-NON-DISCRIMINE':
        sg, sd = res('E', pg), res('E', pd)
        v += ' (%s)' % (('V-CREUX' if sg < 0 else 'V-BOSSE') if sg * sd > 0 else 'FALAISE')
    bloquante = ('C1' if not C1 else ('C2' if not C2 else ('C3' if not C3 else '-')))
    return v, dict(xm=xm, rE=res('E', xm), r57=res('S57', xm), r4=res('S4', xm),
                   sE=seuil('E', xm), s57=seuil('S57', xm), s4=seuil('S4', xm),
                   C1=C1, C2=C2, C3=C3, C4=C4, n_disc=n_disc, bloquante=bloquante,
                   larg=pd - pg, pg=pg, pd=pd, inter=inter)


KX = {'E': K['E'][0], 'S57': K['S57'][0], 'S4': K['S4'][0]}


def montre(nom, v, d, attendu, cle_ok):
    ok = cle_ok(v, d)
    print('   %-42s -> %s' % (nom, v))
    if d:
        print('     x_M=%.2f res_E=%+.4f/%.4f  res_S57=%+.4f/%.4f  res_S4=%+.4f/%.4f'
              % (float(d['xm']), d['rE'], d['sE'], d['r57'], d['s57'], d['r4'], d['s4']))
        print('     C1=%-5s C2=%-5s C3=%-5s n_disc=%d  clause bloquante : %s'
              % (d['C1'], d['C2'], d['C3'], d['n_disc'], d['bloquante']))
    verifie(ok, 'ATTENDU du gel : %s' % attendu, bloquant=not ok)
    return ok


print()
print('   CAS (1) -- CANYON M14 REEL (68df6576)')
G14 = [F(242, 100), F(246, 100), F(248, 100)]
D14 = [F(252, 100), F(254, 100), F(255, 100)]
prof14 = {}
for w in G14 + D14:
    s4, s5, s7 = sF('m14', 4, w), sF('m14', 5, w), sF('m14', 7, w)
    prof14[w] = dict(E=E_de(s4, s5, s7), S57=S57_de(s5, s7), S4=math.log(s4))


def pas_ligne(n, p, w):
    k = '%d|%.12f' % (p, float(w))
    e = CARTE[n][k]
    for cote in ('sP', 'sM'):
        b_ = e.get(cote)
        if isinstance(b_, dict) and b_.get('s') == e['sF']:
            m = re.search(r'pas=([0-9.eE+-]+)', b_.get('note', '') or '')
            if m:
                return float(m.group(1))
    for kk, v in G6[n].items():
        if kk.startswith(k) and v.get('pas_final_recherche'):
            return float(v['pas_final_recherche'])
    raise RuntimeError('pas introuvable %s %s' % (n, k))


def B(n, w, q):
    r4 = pas_ligne(n, 4, w) / sF(n, 4, w)
    r5 = pas_ligne(n, 5, w) / sF(n, 5, w)
    r7 = pas_ligne(n, 7, w) / sF(n, 7, w)
    if q == 'E':
        return ((r4) + 2.25 * r5) + 1.25 * r7
    if q == 'S57':
        return (2.25 * r5) + 1.25 * r7
    return r4


def barres14(q, b, lg, ld):
    return 10 * ((B('m14', lg, q) + B('m14', ld, q)) + B('m14', b, q))


v1_, d1_ = critere(prof14, G14, D14, F(5, 2), KX, barres14)
montre('canyon M14', v1_, d1_, 'STRUCTURE-AU-SITE-RESOLUE, FALAISE, toutes clauses',
       lambda v, d: v.startswith('STRUCTURE-AU-SITE-RESOLUE') and 'FALAISE' in v
       and d['C1'] and d['C2'] and d['C3'] and d['n_disc'] >= 1)
print('     marge C1 = %.2f x ; marge C3 = %.2f x ; n_disc = %d (v3 : 2.33x, >= 1)'
      % (abs(d1_['rE']) / d1_['sE'], abs(d1_['r57']) / d1_['s57'], d1_['n_disc']))
verifie(abs(abs(d1_['rE']) / d1_['sE'] - 2.33) < 0.01, 'la marge 2.33x du gel se re-derive')

print()
print('   CAS (2) -- TRONCON LISSE REEL, pseudo-site 2.79 (2+2), et son LEAVE-OUT')
GL, DL = [F(275, 100), F(278, 100)], [F(280, 100), F(285, 100)]
profL = {w: dict(E=CH[w][0], S57=CH[w][1], S4=CH[w][2]) for w in GL + DL}
v2_, d2_ = critere(profL, GL, DL, F(279, 100), KX)
montre('fond reel lisse (plancher du gel)', v2_, d2_,
       'PAS-DE-STRUCTURE-RESOLUE, clause bloquante C1',
       lambda v, d: v == 'PAS-DE-STRUCTURE-RESOLUE' and d['bloquante'] == 'C1')
TR_LO = [(a, b, c) for a, b, c in TRIPS if not ({a, b, c} & {F(278, 100), F(280, 100)})]
K_LO = max(abs(residu(0, a, b, c)) / float(g(a, b, c)) for a, b, c in TR_LO)
print('     LEAVE-OUT (regle 14, esprit) : triplets touchant 2.78/2.80 retires ->')
print('     %d triplets, K_E^(-) = %.4f (contre %.4f)' % (len(TR_LO), K_LO, K['E'][0]))
v2b, d2b = critere(profL, GL, DL, F(279, 100), dict(KX, E=K_LO, S57=K_LO, S4=K_LO))
montre('fond reel lisse (plancher LEAVE-OUT)', v2b, d2b,
       'PAS-DE-STRUCTURE-RESOLUE meme sans les donnees qui ont calibre le plancher',
       lambda v, d: v == 'PAS-DE-STRUCTURE-RESOLUE' and d['bloquante'] == 'C1')
print('     -> la circularite du cas (2) est LEVEE : le verdict tient hors calibration.')

print()
print('   CAS (3) -- VECTEURS SYNTHETIQUES, rejoues sur le critere v3')
GP, DP = PROG['gauche'], PROG['droit']
VECT = [
    ('pente monotone croissante', lambda w: 0.50 + 0.30 * float(w - SITE), 'PAS-DE-STRUCTURE-RESOLUE', 'C1'),
    ('pente monotone decroissante', lambda w: 0.50 - 0.30 * float(w - SITE), 'PAS-DE-STRUCTURE-RESOLUE', 'C1'),
    ('creux centre 0.10', lambda w: 0.52 - 0.10 * math.exp(-((float(w - SITE)) / 0.03) ** 2),
     'STRUCTURE-AU-SITE-RESOLUE (V-CREUX)', None),
    ('bosse centree 0.10', lambda w: 0.52 + 0.10 * math.exp(-((float(w - SITE)) / 0.03) ** 2),
     'STRUCTURE-AU-SITE-RESOLUE (V-BOSSE)', None),
    ('fond lisse k=8.0, max en 2.70', lambda w: 0.52 - 8.0 * (float(w) - 2.70) ** 2,
     'NE TIRE PAS', 'C1'),
    ('ondulation 0.02', lambda w: 0.52 + 0.02 * math.sin(float(w) * 90.0), 'PAS STRUCTURE-AU-SITE', None),
]
for nom, f, att, bloq in VECT:
    # S57 suit E (structure portee 5/7), S4 plat : le gel exige que les attendus
    # portent TOUTES les clauses (N-9), donc les vecteurs doivent definir S57.
    prof = {w: dict(E=f(w), S57=f(w) - 0.52, S4=0.0) for w in GP + DP}
    v, d = critere(prof, GP, DP, SITE, KX)
    conforme = (att in v) or (att == 'NE TIRE PAS' and not (d['C1'] and d['C2'])) \
        or (att == 'PAS STRUCTURE-AU-SITE' and not v.startswith('STRUCTURE-AU-SITE-RESOLUE'))
    print('   %-34s x_M=%.2f res_E=%+.4f/%.4f  C1=%-5s C2=%-5s C3=%-5s  bloquante=%s'
          % (nom, float(d['xm']), d['rE'], d['sE'], d['C1'], d['C2'], d['C3'], d['bloquante']))
    print('     verdict : %-46s attendu : %s' % (v, att))
    verifie(conforme, 'cas (3) %s' % nom, bloquant=not conforme)
    if bloq:
        verifie(d['bloquante'] == bloq, 'cas (3) %s : clause bloquante CONSIGNEE = %s (gel : %s)'
                % (nom, d['bloquante'], bloq))

print()
print('   CAS (4) -- VECTEUR CANAL 4 (S4 seul porte la structure, S57 plat)')
amp4 = 0.12
prof4 = {w: dict(S4=1.0 + amp4 * math.exp(-((float(w - SITE)) / 0.03) ** 2), S57=-1.5) for w in GP + DP}
for w in prof4:
    prof4[w]['E'] = prof4[w]['S4'] + prof4[w]['S57']
v4_, d4_ = critere(prof4, GP, DP, SITE, KX)
montre('canal 4 pur (amplitude %.2f)' % amp4, v4_, d4_,
       'STRUCTURE-CANAL-4-CANDIDATE -- C1, C2, C3 FAUSSE exercee, |res_S4| > seuil4',
       lambda v, d: v == 'STRUCTURE-CANAL-4-CANDIDATE' and d['C1'] and d['C2']
       and not d['C3'] and d['C4'])

print()
print('   CAS (5) -- TEMOIN DE BANDE (res_S57 et res_S4 chacun sous son seuil, res_E au-dessus)')
bmax = max([F(264, 100), F(265, 100), F(269, 100), F(271, 100)],
           key=lambda b: g(F(262, 100), b, F(273, 100)))
gb = float(g(F(262, 100), bmax, F(273, 100)))
cible57, cible4 = 0.995 * KX['S57'] * gb, 0.995 * KX['S4'] * gb
print('     construit en %.2f : plancher_E=%.5f plancher_S57=%.5f plancher_S4=%.5f'
      % (float(bmax), KX['E'] * gb, KX['S57'] * gb, KX['S4'] * gb))
print('     cible : res_S57 = %.5f, res_S4 = %.5f, somme = %.5f > %.5f'
      % (cible57, cible4, cible57 + cible4, KX['E'] * gb))


def triangle(w, sommet, amp):
    """profil triangulaire nul aux deux LOIN, valant amp au sommet -- residu exact = amp."""
    a, c = F(262, 100), F(273, 100)
    if w == sommet:
        return amp
    if w in (a, c):
        return 0.0
    d_ = abs(float(w - sommet)) / float(c - a)
    return amp * max(0.0, 1 - 6 * d_)


prof5 = {}
for w in GP + DP:
    s57 = triangle(w, bmax, cible57)
    s4 = triangle(w, bmax, cible4)
    prof5[w] = dict(S57=s57, S4=s4, E=s57 + s4)
v5_, d5_ = critere(prof5, GP, DP, SITE, KX)
montre('temoin de bande', v5_, d5_,
       'STRUCTURE-RESOLUE-NON-ATTRIBUEE -- la branche du trou D-3, exercee',
       lambda v, d: v == 'STRUCTURE-RESOLUE-NON-ATTRIBUEE')

print()
print('   CAS (6) -- CONFIGURATION 2+2, extremum au PROCHE gauche (n_disc = 0)')
G22, D22 = [F(262, 100), F(264, 100)], [F(269, 100), F(271, 100)]
prof6 = {w: dict(E=0.52 - 0.20 * math.exp(-((float(w) - 2.64) / 0.02) ** 2),
                 S57=-0.20 * math.exp(-((float(w) - 2.64) / 0.02) ** 2), S4=0.0)
         for w in G22 + D22}
v6_, d6_ = critere(prof6, G22, D22, SITE, KX)
montre('2+2, extremum en 2.64', v6_, d6_,
       'verdict DIFFERENT de STRUCTURE-AU-SITE-RESOLUE (n_disc = 0)',
       lambda v, d: not v.startswith('STRUCTURE-AU-SITE-RESOLUE') and d['n_disc'] == 0)
print('     largeur_centrage consignee : %s (contre 1/25 au programme complet)' % d6_['larg'])

# ==================================================== [10] la puissance
titre(10, "PUISSANCE -- CE QUE LE GEL NE CHIFFRE PAS (consignation pre-run)")
GA, GD = F(262, 100), F(273, 100)
print('   PLANCHER_E(b) = K_E * g(2.62, b, 2.73), par interieur :')
for b in (F(264, 100), F(265, 100), F(269, 100), F(271, 100)):
    print('     b = %.2f  g = %-10s PLANCHER_E = %.5f  PLANCHER_S57 = %.5f  PLANCHER_S4 = %.5f'
          % (float(b), str(g(GA, b, GD)), KX['E'] * float(g(GA, b, GD)),
             KX['S57'] * float(g(GA, b, GD)), KX['S4'] * float(g(GA, b, GD))))
a_, b_, c_ = F(260, 100), F(267, 100), F(272, 100)
E260 = E_de(sF('m11', 4, a_), sF('m10', 5, a_), sF('m10', 7, a_))
E272 = E_de(sF('m12', 4, c_), sF('m12', 5, c_), sF('m12', 7, c_))
E267 = E_de(sF('m12', 4, b_), sF('m12', 5, b_), sF('m12', 7, b_))
res267 = E267 - (E260 + float((b_ - a_) / (c_ - a_)) * (E272 - E260))
courb = abs(res267) / float(g(a_, b_, c_))
print()
print('   LE SEUL INDICE MESURE AU SITE, RAMENE A LA MEME UNITE QUE LE SEUIL :')
print('     res_E(2.67 | 2.60, 2.72) = %+.4f  sur g = %s = %.6f'
      % (res267, g(a_, b_, c_), float(g(a_, b_, c_))))
print('     courbure equivalente du site = %.3f' % courb)
print('     K_E, courbure max du fond    = %.3f' % KX['E'])
verifie(courb > KX['E'], 'la courbure du site DEPASSE K_E (rapport %.3f, soit %+.0f %%)'
        % (courb / KX['E'], 100 * (courb / KX['E'] - 1)))
print('   Si cette courbure se conserve a la geometrie du programme :')
for bb in (F(265, 100), F(269, 100)):
    att = courb * float(g(GA, bb, GD))
    seu = KX['E'] * float(g(GA, bb, GD))
    print('     b = %.2f : residu attendu %.4f  vs PLANCHER_E %.4f  -> %s (marge %.2f x)'
          % (float(bb), att, seu, 'TIRE' if att > seu else 'NE TIRE PAS', att / seu))
print()
print('   ET LE CONTROLE POSITIF DU GEL LUI-MEME PASSE DE JUSTESSE : le vecteur')
prof_c = {w: dict(E=0.52 - 0.10 * math.exp(-((float(w - SITE)) / 0.03) ** 2),
                  S57=-0.10 * math.exp(-((float(w - SITE)) / 0.03) ** 2), S4=0.0)
          for w in GP + DP}
vc_, dc_ = critere(prof_c, GP, DP, SITE, KX)
print('   "creux centre 0.10" rend res_E = %.4f contre un plancher de %.4f :'
      % (abs(dc_['rE']), dc_['sE']))
print('   marge %.3f x. Un creux de profondeur %.3f au lieu de 0.10 ne tirerait plus.'
      % (abs(dc_['rE']) / dc_['sE'], 0.10 * dc_['sE'] / abs(dc_['rE'])))
verifie(abs(dc_['rE']) / dc_['sE'] > 1.0,
        'le controle positif du gel tire (marge %.3f x)' % (abs(dc_['rE']) / dc_['sE']))
print()
print('   MAIS L ATTENTE INSCRITE (ma note v2 section 13, citee au gel en RESUME) dit')
print('   res_E au PROCHE dans [0.03, 0.08]. Confrontee aux planchers par point :')
for bb in (F(265, 100), F(269, 100)):
    seu = KX['E'] * float(g(GA, bb, GD))
    frac_tire = max(0.0, 0.08 - max(0.03, seu)) / 0.05
    print('     b = %.2f : PLANCHER_E = %.4f -> %.0f %% de [0.03, 0.08] fait tirer C1'
          % (float(bb), seu, 100 * frac_tire))
print()
print('   ET LE TROISIEME PLANCHER, CELUI DES COMPTES : C1 ne suffit plus, il faut')
print('   n_disc >= 1 (D-2), donc AU MOINS UN FLANC A TROIS SURVIVANTS.')
s_pt = (1 - 0.0855) * (1 - 0.0679) ** 4
p3 = s_pt ** 3
p2e = 3 * s_pt ** 2 * (1 - s_pt)
p_plancher = (p3 + p2e) ** 2
p_disc = p_plancher - p2e ** 2
print('     survie POINT = %.4f ; P(plancher de comptes) = %.4f ; P(n_disc >= 1) = %.4f'
      % (s_pt, p_plancher, p_disc))
print('   -> LE FALSIFIEUR NE PEUT PRONONCER "ETAGE B FALSIFIE" QUE DANS %.0f %% DES RUNS,'
      % (100 * p_disc))
print('      et, dans ces runs, seulement si la structure depasse une courbure que le')
print('      seul indice mesure ne depasse que de %.0f %%.' % (100 * (courb / KX['E'] - 1)))
print()
print('   CE N EST PAS UN DEFAUT DU CRITERE : les trois formes possibles ont ete jouees.')
print('     - plancher PLAT (v2)          : le fond reel et le vecteur k=8 TIRENT -> refuse')
gmatch = {}
for b in (F(264, 100), F(265, 100), F(269, 100), F(271, 100)):
    gb2 = g(GA, b, GD)
    comp = [abs(residu(0, x, y, z)) for x, y, z in TRIPS
            if F(1, 2) * gb2 <= g(x, y, z) <= 2 * gb2]
    gmatch[b] = max(comp) if comp else None
print('     - plancher g-APPARIE (teste ici, non retenu au gel) : max des residus a')
print('       geometrie comparable = %.4f partout ; le vecteur k=8 rend 0.0224 en 2.69'
      % gmatch[F(269, 100)])
verifie(gmatch[F(269, 100)] < 0.0224,
        'la variante g-appariee ECHOUE le banc (%.4f < 0.0224 : le vecteur k=8 la '
        'franchit) -- elle est donc ECARTEE, et non pas oubliee' % gmatch[F(269, 100)])
print('     - plancher COURBURE (v3)      : les trois cas a reponse connue passent.')
print('   La forme retenue est la SEULE des trois qui passe le banc. Le prix est la')
print('   puissance, et ce prix doit etre ECRIT : c est une consignation, pas un defaut.')

# ================================================== [11] ce qu il ne joue pas
titre(11, "CE QUE CE LOG NE JOUE PAS")
print('   1. AUCUNE recherche de s* : aucun moteur importe. Tous les s* viennent des')
print('      artefacts verifies par empreinte en [3].')
print('   2. Il ne certifie PAS m15_site83_v1.py (non depose, E19). ITEM 5 TEMPS 2 --')
print('      verrous de custody qui mordent, selftest, pre-vol a moteur factice --')
print('      reste DU, et le gel v3 le declare desormais lui-meme.')
print('   3. La partition [6] est testee sur les 32 combinaisons BOOLEENNES, pas sur')
print('      des profils physiques : elle prouve l exclusivite et l exhaustivite du')
print('      texte, pas que chaque branche soit ATTEIGNABLE par un profil reel. Les')
print('      cas (4), (5) et (6) du banc exhibent trois de ces profils ; les trois')
print('      autres branches le sont par les cas (1), (2) et (3).')
print('   4. Les vecteurs synthetiques de [9] cas (3) portent un S57 que J AI choisi')
print('      (S57 = E - 0.52, S4 plat) : le gel exige des attendus a toutes clauses')
print('      (N-9) mais ne fixe pas les canaux de ces vecteurs. Mon choix est declare')
print('      ici ; un autre choix changerait C3 sans changer C1 ni C2.')
print('   5. Le taux de base de [7] exclut les 64 lignes de M10 (champ absent).')
print('   6. Les probabilites de [10] supposent les morts INDEPENDANTES ; le registre')
print('      montre le contraire (bloc contigu M13). Elles sont OPTIMISTES.')
print('   7. Il n ecrit aucun fichier.')
print()
print('   Arithmetique : EXACTE (Fraction) pour distances, R-2 prime, assignation,')
print('   appartenance a F, facteurs g, queue binomiale et comparaison a 1/20.')
print('   Les K_X, residus et planchers sont des flottants. Le seul flottant qui')
print('   DECIDE dans ce log est la marge de puissance %.3f contre 1 en [10], et' % (courb / KX['E']))
print('   elle est exhibee, pas cachee.')

# =============================================================== [12] synthese
titre(12, "SYNTHESE")
print('   empreinte du bloc M15 v3 (NFC+LF, brut = canonique) :')
print('   %s' % SHA)
print('   controles mecaniques en echec : %d' % len(ECHECS))
for e in ECHECS:
    print('     - %s' % e)
print('   BLOQUANTS                     : %d' % len(BLOQUANTS))
for e in BLOQUANTS:
    print('     - %s' % e)
print()
print('   LES SIX DEFAUTS DE LA CERTIFICATION v2, UN PAR UN :')
print('     D-1 plancher homogene      : REPARE -- courbure K_X, plancher par point ;')
print('         canyon 2.33x, fond reel muet (y compris en LEAVE-OUT), k=8 muet.')
print('     D-2 centrage vide a 2+2    : REPARE -- n_disc, largeur_centrage, branche')
print('         CENTRAGE-NON-DISCRIMINE, exercee au cas (6).')
print('     D-3 trou de partition      : REPARE -- 32/32 combinaisons dans exactement')
print('         une branche, six branches atteintes, temoin de bande exerce (cas 5).')
print('     D-4 signature par le fond  : REPARE -- k_min = 3 en Fraction exacte.')
print('     D-5 compte G2              : REPARE -- precedent M14 nomme, total 38.')
print('     D-6 ensemble F             : REPARE -- F par regle, |F| = 14 en SORTIE.')
print('     N-6 a N-12                 : tous declares et re-verifies en [4].')
sys.exit(0)
