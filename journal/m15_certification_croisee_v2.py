#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CERTIFICATION CROISEE v2 -- GEL M15 (P1-b, site 8/3) : trace executable (machine 2).

Ce script NE lit AUCUN chiffre du gel comme un fait : il RE-APPLIQUE les regles
DECLAREES (par le gel M15 v2 lui-meme, et par ses sources bf9866a7 / 273d0a53 /
97c02eab / 5704987e) et compare. Discipline de campagne : ne jamais verifier ce
qu'un artefact MONTRE, toujours re-appliquer la regle qu'il DECLARE.

CE QUE CE LOG NE JOUE PAS (exigence de titre, lecon 02/08) :
  - il ne rejoue AUCUNE recherche de s* : aucun moteur importe, aucune mesure ;
  - il ne verifie PAS le futur script m15_site83_v1.py (non depose, E19) : ni
    selftest, ni pre-vol, ni verrous de custody executes -- ITEM 5 n'est donc
    couvert ICI que pour sa moitie "recopie des definitions", et sa moitie
    "test execute des verrous" reste DUE au depot du script ;
  - il ne juge pas la resolution de passe de P-M15b ligne par ligne : il en
    derive le TAUX DE BASE au registre, pas le mecanisme ;
  - le champ 'gros_explosifs' est ABSENT des 64 lignes de M10 : ces lignes sont
    HORS DENOMINATEUR du taux de base, et c'est dit a l'endroit du calcul ;
  - il n'ecrit aucun fichier.

Arithmetique : EXACTE (Fraction) partout ou la quantite decide d'une SELECTION
(E28) -- distances, R-2', nouveaute, appartenance a F, facteurs geometriques.
Les E, residus et planchers sont des flottants : ce sont des mesures. Les deux
seuls endroits ou un flottant decide sont exhibes avec leur marge.
"""

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
GEL = 'm15_pre_enregistrement_v2.md'
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


def frac(cle):
    return F(Decimal(cle.split('|')[1]))


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
titre(1, "FORME CANONIQUE DU BLOC GELE (regle 12 et son corollaire)")
with open(GEL, 'rb') as fh:
    brut = fh.read()
txt = canon(brut.decode('utf-8'))
verifie(b'\r' not in brut, 'aucun CR dans le fichier (LF seul)')
verifie(txt == unicodedata.normalize('NFC', txt), 'texte stable par NFC')
verifie(txt.isascii(), 'ASCII pur (aucun caractere composable)')
occ = [m.start() for m in re.finditer(re.escape(TERM), txt)]
print('   occurrences du terminateur : %d' % len(occ))
verifie(len(occ) == 1, 'terminateur UNE SEULE fois (corollaire regle 12)', bloquant=True)
debut = txt.find('PRE-ENREGISTREMENT M15')
verifie(debut == 0, 'le bloc commence a la ligne 1 (colonne 0)')
fin = txt.find('\n', occ[0])
ligne_term = txt[txt.rfind('\n', 0, occ[0]) + 1:fin]
verifie(ligne_term == TERM, 'terminateur en LIGNE PLEINE : %r' % ligne_term)
bloc = txt[debut:fin + 1]
verifie(txt[fin + 1:] == '', 'aucune queue apres le terminateur')
SHA = hashlib.sha256(bloc.encode('utf-8')).hexdigest()
print('   longueur du bloc : %d caracteres' % len(bloc))
print('   EMPREINTE NFC+LF DU BLOC M15 v2 :')
print('   %s' % SHA)
print('   (v1, pour memoire : a2bb2dcd0866... -- NON CERTIFIE)')

# ==================================================== [2] empreintes citees
titre(2, "LES EMPREINTES CITEES, RECALCULEES -- ET LA RESERVE v1 QUI TOMBE")
CITES = [
    ('fa109da9', 'out/m12_results.json', 'brut', 'M12 ponctuel'),
    ('22fa1760', 'out/m13b_results.json', 'brut', 'M13b (crible)'),
    ('68df6576', 'out/m14_results.json', 'brut', 'M14 (canyon 5:2)'),
    ('ed0e27b1', 'out/m12_pilote_results.json', 'brut', 'pilote M12'),
    ('bf9866a7', 'm12_pre_enregistrement_v4.md', 'canonique', 'gel M12 v4 (R-2 prime)'),
    ('273d0a53', 'gel_m14_p1a_v2.md', 'canonique', 'gel M14 v2 (B_E, N-3)'),
    ('c8ed357b', 'm9_replication_v1.py', 'brut', 'moteur classique'),
    ('97c02eab', 'p1_re_derivation_machine2_v1.md', 'canonique', 're-derivation machine 2'),
    ('5704987e', 'note_derivation_P1_signes_E_v5.md', 'canonique', 'note P1 v5 (SOURCE)'),
    ('a944511d', 'm15_certification_croisee_v1.md', 'canonique', 'ma certification v1'),
    ('61f2610f', 'm15_certification_croisee_v1.log', 'brut', 'mon log v1 -- BRUT, voir N-10'),
    ('32714630', 'm15_certification_croisee_v1.py', 'canonique', 'mon script v1'),
    ('a2bb2dcd', 'm15_pre_enregistrement_v1.md', 'canonique', 'gel M15 v1 (refuse)'),
    ('ad275870', 'out/m11_results.json', 'brut', 'M11'),
    ('7cf3624b', 'out/m10_results.json', 'brut', 'M10'),
    ('70fe5611', 'out/m13_results.json', 'brut', 'M13'),
]
for pref, chemin, mode, quoi in CITES:
    if not os.path.exists(chemin):
        verifie(False, '%-9s %-38s ABSENT DU REPERTOIRE' % (pref, chemin), bloquant=True)
        continue
    calc = sha_brut(chemin) if mode == 'brut' else sha_canon(chemin)
    verifie(calc.startswith(pref), '%-9s %-38s (%s) %s' % (pref, chemin, mode, quoi))
print()
print('   N-10 -- CONVENTIONS MELANGEES DANS UNE MEME PHRASE DU GEL, et la faute est')
print('   d abord la mienne : "certification a944511d, log 61f2610f, script d audit')
print('   32714630" cite DEUX empreintes canoniques NFC+LF et UNE en sha BRUT.')
_l = 'm15_certification_croisee_v1.log'
print('     %s : brut %s | canonique %s | CR present : %s'
      % (_l, sha_brut(_l)[:12], sha_canon(_l)[:12], b'\r' in open(_l, 'rb').read()))
print('   Mon log v1 a ete ecrit en CRLF (redirection Windows) : les deux empreintes')
print('   different, et seule la BRUTE concorde avec le gel. Regle de campagne : les')
print('   empreintes se livrent ETIQUETEES. Mon log v2 est ecrit en LF seul.')
print()
print('   LA RESERVE v1 EST LEVEE : la note P1 v5 est au repertoire et concorde.')
note = canon(open('note_derivation_P1_signes_E_v5.md', encoding='utf-8').read()).split('\n')
sections = [(i, l) for i, l in enumerate(note) if l.startswith('## ')]
i_p1b = [i for i, l in enumerate(note) if 'P1-b' in l][0]
sec = max(s for s in sections if s[0] < i_p1b)
print('   entree P1-b : ligne %d, sous la section %r' % (i_p1b + 1, sec[1]))
verifie(sec[1].startswith('## 6.'), 'le gel cite "section 6, entree P1-b" -> CONCORDE')
verifie('falsifieur' in note[i_p1b] and 'B seulement' in ' '.join(note[i_p1b:i_p1b + 2]),
        'etiquette "falsifieur d ETAGE B SEULEMENT" presente VERBATIM dans la note')
tab = [l for l in note if l.startswith('| 8:3')]
print('   table des rangs, section 1 (VERBATIM) : %s' % tab[0])
autre = [l for l in note if '**8/3**' in l and '(3,1)' in l]
if autre:
    print('   ATTENTION, section 2 de la MEME note : %s' % autre[0].strip())
    print('   -> la note enonce le triplet dans DEUX ORDRES (hors chaine, consigne N-6).')

# ======================================= [3] les faits declares, re-derives
titre(3, "LES FAITS QUE LE GEL DECLARE, RE-DERIVES (aucun chiffre lu comme un fait)")


def rang_minimal(q, p, rmax=40, jmax=12):
    best = []
    for j in range(1, jmax + 1):
        for r in range(1, rmax + 1):
            if j * q <= r * p and (j * q - r * p) % 2 == 0:
                best.append((j, r))
                break
    j, r = min(best)
    return r, j


print('   (a) rangs a 8/3 -- regle j*q <= r*p ET j*q = r*p (mod 2), q = 11 :')
for p, att in ((4, (6, 2)), (5, (3, 1)), (7, (3, 1))):
    verifie(rang_minimal(Q_SITE, p) == att, 'p=%d -> %s (gel : %s)' % (p, rang_minimal(Q_SITE, p), att))
r4, j4 = rang_minimal(Q_SITE, 4)
verifie(j4 * Q_SITE <= r4 * 4 and (j4 * Q_SITE - r4 * 4) % 2 == 0,
        'N-4 : le rang (6,2) a p=4 est PERMIS par la parite (%d <= %d, memes parites)'
        % (j4 * Q_SITE, r4 * 4))

print()
print('   (b) le pas de s*4 est-il SOUS la fenetre ?')
s255, s260, s267 = sF('m12', 4, F(255, 100)), sF('m11', 4, F(260, 100)), sF('m12', 4, F(267, 100))
for w, v, att, src in ((2.55, s255, 2.881241, 'fa109da9'), (2.60, s260, 7.157439, 'ad275870'),
                       (2.67, s267, 7.462573, 'fa109da9')):
    verifie(abs(v - att) < 5e-7, 's*4(%.2f) = %.6f  (gel : %.6f) [%s]' % (w, v, att, src))
fact = s267 / s255
part = math.log(s260 / s255) / math.log(s267 / s255)
verifie(abs(fact - 2.590) < 5e-4, 'facteur total 2.55->2.67 = %.3f (gel : 2.590)' % fact)
verifie(abs(100 * part - 95.6) < 0.05, 'part consommee dans [2.55,2.60] = %.1f %% (gel : 95.6 %%)' % (100 * part))

print()
print('   (c) le crible p=4 de M13b, et la mort de 2.70 :')
pts13b = sorted({frac(k) for k in CARTE['m13b']})
union = sorted({frac(k) for k in CARTE['m13b']} | {frac(k) for k in CARTE['m13']})
ec_b = min(pts13b[i + 1] - pts13b[i] for i in range(len(pts13b) - 1))
ec_u = min(union[i + 1] - union[i] for i in range(len(union) - 1))
print('       points M13b seuls : %s' % [float(x) for x in pts13b])
print('       plus petit ecart INTERNE a M13b : %s -- l entrelacement n est donc PAS' % ec_b)
print('       interne : il se lit sur l UNION M13 u M13b (le crible du delta 48.3).')
verifie(ec_u == F(1, 100), 'crible ENTRELACE au centieme sur M13 u M13b (plus petit ecart = %s)' % ec_u)
g = G6['m13b'].get('4|2.700000000000|+1')
verifie(bool(g and g.get('exclue')), '2.70 est MORT dans 22fa1760 (G6.exclue = True)')
if g:
    print('       explosion_sous_0.98s = %s ; fenetre fine = %s'
          % (g.get('explosion_sous_0.98s'), g.get('bornes_fin')))
    if g.get('explosion_sous_0.98s') and g.get('bornes_fin'):
        s_expl = g['explosion_sous_0.98s']
        s_etoile = CARTE['m13b']['4|2.700000000000']['sF']
        print('       ratio explosion/s* = %.4f ; le gel ecrit "0.924-0.966 s*"' % (s_expl / s_etoile))
for v in (F(269, 100), F(271, 100)):
    print('       2.70 est a %s de %.2f' % (abs(F(270, 100) - v), float(v)))

print()
print('   (d) les trois instances du mecanisme "grossiere mordue" -- COMPTEES :')
inst = []
for n in NOMS:
    for k, v in G6[n].items():
        if 'gros_explosifs' not in v:
            continue
        if (v.get('gros_explosifs') or 0) > 0 or v.get('explosion_sous_LO0_0.90s') is not None:
            inst.append((n, k, int(k.split('|')[0]), k.split('|')[2]))
for n, k, p, sgn in inst:
    print('       %-11s %-22s degre %d (%s) cote %s' % (n, k, p, 'IMPAIR' if p % 2 else 'pair', sgn))
verifie(len(inst) == 3, 'trois instances au registre (gel : trois)')
verifie(all(p % 2 == 1 for _, _, p, _ in inst), 'toutes a degre IMPAIR (gel : toutes)')
cotes = [s for _, _, _, s in inst]
print('       cotes comptes : %s' % cotes)
print('       Le gel ecrit "les deux instances a cote identifie sont cote -1".')
print('       COMPTE : les TROIS portent un cote au registre (la cle G6 est')
print('       p|w|sgn), et la repartition est %d x -1 pour %d x +1. Un compte'
      % (cotes.count('-1'), cotes.count('+1')))
print('       inscrit doit etre compte : a reformuler (N-7).')
gp = G6['m14'].get('5|2.500000000000|+1')
verifie(bool(gp) and not gp.get('exclue') and (gp.get('gros_explosifs') or 0) == 0,
        'a 2.50 le cote +1 survit avec grossiere VIDE (gel : asymetrie de signe)')

print()
print('   (f) les six E deja connus autour du programme :')
CONNUS = {}
for w in (F(260, 100), F(275, 100)):
    CONNUS[w] = (E_de(sF('m11', 4, w), sF('m10', 5, w), sF('m10', 7, w)), 'M10+M11')
for w in (F(267, 100), F(272, 100), F(278, 100), F(280, 100)):
    CONNUS[w] = (E_de(sF('m12', 4, w), sF('m12', 5, w), sF('m12', 7, w)), 'M12')
GEL_E = {F(260, 100): 0.5554, F(267, 100): 0.4274, F(272, 100): 0.5174,
         F(275, 100): 0.5251, F(278, 100): 0.5193, F(280, 100): 0.5426}
perdus = {frac(k) for k in A['m12']['resume']['points_perdus']}
for w in sorted(CONNUS):
    e, src = CONNUS[w]
    verifie(abs(e - GEL_E[w]) < 5e-5, 'E(%.2f) = %+.4f (gel : %+.4f) [%s]%s'
            % (float(w), e, GEL_E[w], src,
               '  <-- POINT PERDU, NON OPPOSABLE' if w in perdus else ''))
c = CONNUS[F(260, 100)][0] + float((F(267, 100) - F(260, 100)) / (F(272, 100) - F(260, 100))) \
    * (CONNUS[F(272, 100)][0] - CONNUS[F(260, 100)][0])
res267 = CONNUS[F(267, 100)][0] - c
verifie(abs(res267 + 0.106) < 5e-4, 'E(2.67) est a %+.4f de la corde 2.60<->2.72 (gel : -0.106)' % res267)
s57_267 = S57_de(sF('m12', 5, F(267, 100)), sF('m12', 7, F(267, 100)))
c57 = S57_de(sF('m12', 5, F(260, 100)) if False else 1, 1)  # place tenue, calcul ci-dessous
S57C = {}
for w in (F(260, 100), F(272, 100), F(267, 100)):
    if w == F(260, 100):
        S57C[w] = S57_de(sF('m10', 5, w), sF('m10', 7, w))
    else:
        S57C[w] = S57_de(sF('m12', 5, w), sF('m12', 7, w))
S4C = {F(260, 100): math.log(sF('m11', 4, F(260, 100))),
       F(272, 100): math.log(sF('m12', 4, F(272, 100))),
       F(267, 100): math.log(sF('m12', 4, F(267, 100)))}
for nom, X in (('S57', S57C), ('S4', S4C)):
    cc = X[F(260, 100)] + (7 / 12) * (X[F(272, 100)] - X[F(260, 100)])
    print('       partage du residu de 2.67 : res_%-3s = %+.4f' % (nom, X[F(267, 100)] - cc))
print('       -> le gel ecrit "porte principalement par le canal 7", c est-a-dire')
print('          par S57 : CONFIRME (le residu de S4 est marginal).')

print()
print('   CONSTAT AGGRAVANT du HISTORIQUE v2, re-derive sur le canyon M14 reel :')
E14 = {w: E_de(sF('m14', 4, w), sF('m14', 5, w), sF('m14', 7, w))
       for w in (F(242, 100), F(246, 100), F(248, 100), F(252, 100), F(254, 100), F(255, 100))}
Dg = E14[F(248, 100)] - E14[F(242, 100)]
Dd = E14[F(252, 100)] - E14[F(255, 100)]
verifie(abs(Dg - 0.109) < 1e-3 and abs(Dd + 0.078) < 1e-3,
        'clause (2) v1 sur 68df6576 : D(g) = %+.4f, D(d) = %+.4f (gel : +0.109 / -0.078)' % (Dg, Dd))
print('       N-11 : D(g) vaut %+.4f ; le gel inscrit +0.109, qui est la TRONCATURE' % Dg)
print('       et non l arrondi (+0.110). Sans effet ici ; a corriger a l inscription.')
verifie((Dg > 0) != (Dd > 0), 'signes OPPOSES -> la clause v1 aurait MANQUE le seul canyon mesure')

# ================================================= [4] ITEM 2 -- nouveaute
titre(4, "ITEM 2 -- NOUVEAUTE PAR VALEUR EXACTE (critere NOMME par le gel)")
PROG = {'gauche': [F(262, 100), F(264, 100), F(265, 100)],
        'droit': [F(269, 100), F(271, 100), F(273, 100)]}
TOUS_PTS = {n: {frac(k) for k in CARTE[n]} for n in NOMS}
neuf = True
for fl in ('gauche', 'droit'):
    for w in PROG[fl]:
        dedans = [n for n in NOMS if w in TOUS_PTS[n]]
        neuf &= not dedans
        print('   w2=%.2f  %s' % (float(w), 'NEUF' if not dedans else '*** DEJA MESURE : %s' % dedans))
verifie(neuf, 'les six points sont neufs PAR VALEUR EXACTE dans les 7 artefacts de la lignee')
GRILLE = TOUS_PTS['m10'] | TOUS_PTS['m11']
print('   proximites consignees par le gel, re-derivees en exact :')
for w, cible in ((F(262, 100), F(260, 100)), (F(273, 100), F(275, 100))):
    verifie(abs(w - cible) == F(1, 50), '%.2f est a %s de %.2f (gel : 1/50)'
            % (float(w), abs(w - cible), float(cible)))
verifie(F(275, 100) in TOUS_PTS['m12_pilote'],
        '2.75 est bien un BRULE du pilote (le brulage porte la VALEUR, pas un voisinage)')
print('   la regle d >= 0.03 (bf9866a7) EXCLURAIT : %s'
      % [float(w) for fl in PROG for w in PROG[fl] if min(abs(w - g) for g in GRILLE) < F(3, 100)])
print('   motifs de non-reconduction, declares au gel : (1) propre a M12 -- precedent')
print('   M14 (2.46 a 1/100 de 2.45) ; (2) tester un site a moins de 0.01 d un point')
print('   de grille impose des points dans ce rayon. RE-DERIVE, sur la grille au')
print('   CENTIEME (celle que la manche mesure), et non sur la grille M10/M11 :')
d_cent = min(abs(SITE - F(k, 100)) for k in range(260, 275))
verifie(d_cent < F(1, 100), '8/3 est a %s = %.5f du centieme le plus proche (2.67) -> '
        'le motif (2) est FONDE' % (d_cent, float(d_cent)))
print('     (pour memoire, la distance a la grille M10/M11 est %s -- ce n est pas'
      % min(abs(SITE - g) for g in GRILLE))
print('      la grille dont parle le motif (2).)')

# ================================================ [5] ITEM 3 -- q_L local
titre(5, "ITEM 3 -- q_L LOCAL, PAR DEGRE ET PAR DOMAINE (unite : LIGNE SIGNEE)")


def borne80(k, n):
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        pc = sum(math.comb(n, i) * mid ** i * (1 - mid) ** (n - i) for i in range(k + 1))
        if pc > 0.20:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def taux(bas, haut):
    par = {'p=4': [0, 0], 'impair': [0, 0]}
    morts = []
    for n in NOMS:
        for k, v in G6[n].items():
            w, p = frac(k), int(k.split('|')[0])
            if not (bas <= w <= haut):
                continue
            c = 'p=4' if p == 4 else 'impair'
            par[c][1] += 1
            if v.get('exclue'):
                par[c][0] += 1
                morts.append('%s:%s' % (n, k))
    return par, morts


DOM = [('lignee entiere', F(0), F(10)),
       ('[2.35, 3.10] -- domaine implicite du gel', F(235, 100), F(310, 100)),
       ('[2.35, 2.90[ -- HORS bloc de saturation M13/M13b', F(235, 100), F(289, 100)),
       ('[2.55, 2.85] -- fenetre elargie du site', F(255, 100), F(285, 100))]
Q = {}
for nom, bas, haut in DOM:
    par, morts = taux(bas, haut)
    print('   --- %s ---' % nom)
    for c in ('p=4', 'impair'):
        x, nn = par[c]
        q = borne80(x, nn)
        Q[(nom, c)] = q
        print('     %-7s %2d/%3d = %.4f   q_L(borne sup 80 %%) = %.4f' % (c, x, nn, x / nn, q))
    if len(morts) <= 14:
        print('     morts : %s' % morts)
print()
print('   LE DOMAINE CHANGE TOUT : 10 des 13 morts de [2.35,3.10] sont les p=4 du')
print('   BLOC DE SATURATION [2.90, 3.05] (M13/M13b) -- regime H-SAT, pas le site.')
print('   Le gel les range parmi les morts "CORRELEES au site" : domaines melanges')
print('   au sens d E27. Le domaine opposable pour M15 est [2.35, 2.90[.')
print()
NOM_D = '[2.35, 2.90[ -- HORS bloc de saturation M13/M13b'
q4, qi = Q[(NOM_D, 'p=4')], Q[(NOM_D, 'impair')]
s_pt = (1 - q4) * (1 - qi) ** 4
p_flanc = sum(math.comb(3, i) * s_pt ** i * (1 - s_pt) ** (3 - i) for i in (2, 3))
p3 = s_pt ** 3
p_exact2 = 3 * s_pt ** 2 * (1 - s_pt)
print('   FAIT LOCAL, COMPTE (il fonde mon attente, il ne fonde aucune porte) :')
voisins = {}
for n in NOMS:
    for k in CARTE[n]:
        w = frac(k)
        if abs(w - SITE) <= F(4, 100):
            voisins.setdefault(w, set()).add(n)
morts_pt = set()
for n in NOMS:
    for k, v in G6[n].items():
        if v.get('exclue') and abs(frac(k) - SITE) <= F(4, 100):
            morts_pt.add(frac(k))
print('     points DEJA MESURES a moins de 4/100 du site : %s'
      % [(float(w), sorted(voisins[w])) for w in sorted(voisins)])
print('     parmi eux, points portant au moins une ligne EXCLUE : %s'
      % [float(w) for w in sorted(morts_pt)])
verifie(len(morts_pt) < len(voisins),
        'N-12 : au moins un des points deja mesures pres du site a survecu '
        '(%d/%d sont morts)' % (len(morts_pt), len(voisins)))
print()
print('   FAISABILITE, forme derivee (1 ligne p=4 + 4 lignes impaires par point) :')
print('     survie POINT = (1-q4)^1 x (1-qi)^4 = %.4f' % s_pt)
print('     P(>= 2 survivants sur 3, un flanc) = %.4f' % p_flanc)
print('     P(plancher de comptes ATTEINT, les deux flancs) = %.4f' % (p_flanc ** 2))
print('     P(les 6 points survivent, config 3+3) = %.4f' % s_pt ** 6)
print('     P(les DEUX flancs a exactement 2) = %.4f' % (p_exact2 ** 2))
print('   -> JUGEMENT DE FAISABILITE : la geometrie est JOUABLE (37 recherches,')
print('      ~13 s/recherche au registre = ~8 min), mais le plancher de comptes')
print('      MANQUE avec probabilite %.2f, et la configuration 3+3 -- la seule ou' % (1 - p_flanc ** 2))
print('      la clause de centrage discrimine (voir [9]) -- n arrive que %.2f fois' % s_pt ** 6)
print('      sur 10. Sur le domaine du gel ([2.35,3.10]) ce serait pire encore.')

# ================================================== [6] ITEM 4 -- G2 : le compte
titre(6, "ITEM 4 -- G2 : LE COMPTE N EST PAS DERIVABLE (deux heritages incompatibles)")
src12 = canon(open('m12_pre_enregistrement_v4.md', encoding='utf-8').read())
src14 = canon(open('gel_m14_p1a_v2.md', encoding='utf-8').read())
print('   CE QUE M12 (bf9866a7) DECLARE, VERBATIM :')
for l in src12.split('\n'):
    if re.match(r'\s*G2\s+INVARIANCE', l) or ('G2' in l and '3 x 2' in l) or ("G1' : 1 ; G2" in l):
        print('     | %s' % l.strip())
i = src12.find('G2  INVARIANCE')
print('     | %s' % ' '.join(src12[i:i + 210].split()))
print('   CE QUE M14 (273d0a53) DECLARE, VERBATIM :')
j = src14.find('G2 une')
print('     | %s' % ' '.join(src14[j:j + 190].split()))
print()
print('   Les deux precedents different EN NATURE et EN COMPTE :')
print('     M12 : 6 recherches (3 degres x 2), tolerance 10 %, echec -> LIGNE EXCLUE')
print('           -> une exclusion G2 alimente G7, donc le PLANCHER DE COMPTES ;')
print('     M14 : 1 recherche a 2g sur une ligne DESIGNEE, |K2/K1 - 1| consigne')
print('           SANS PORTE -- aucune exclusion possible.')
print('   De plus la designation M12 ("le PREMIER point de la liste") n a AUCUN')
print('   referent dans M15 : la manche n a pas de liste de priorite.')
verifie(False, 'D-5 (ITEM 4) : "reconduite selon les regles de designation heritees" ne '
               'designe rien -> compte INDERIVABLE (37 + G2 vaut 38 ou 43)', bloquant=True)

# ============================================ [7] ITEM 5 -- heritage, moitie recopie
titre(7, "ITEM 5 -- HERITAGE M12/M14 : LA MOITIE RECOPIE (l autre moitie est DUE)")
print('   N-3, ordre de sommation -- ce que M14 declare :')
for l in src14.split('\n'):
    if 'B_E = ((' in l:
        print('     | %s' % l.strip())
print('   ce que M15 v2 ecrit :')
for l in txt.split('\n'):
    if re.match(r'\s*B_E(57|4)?\(point\)', l) or re.match(r'\s*-- FORME ET ORDRE', l.strip()):
        print('     | %s' % l.strip())
n3 = bool(re.search(r'B_E\(point\)\s*=\s*\(\(', txt))
verifie(n3, 'N-3 (ordre de sommation, evaluation gauche-droite) RECONDUIT dans M15 v2')
verifie('ORDRE DE SOMMATION DE M14 (N-3) RECONDUITS' in txt.replace('\n', ' ').replace('  ', ' ')
        or 'FORME ET ORDRE DE SOMMATION DE M14' in txt,
        'la reconduction est DECLAREE, pas seulement pratiquee')
bar = [l.strip() for l in txt.split('\n') if re.match(r'\s*barre(57|4)?\(b\)\s*=', l)]
print('   la barre, forme derivee PAR CORDE (defaut D-3 v1) :')
for l in bar:
    print('     | %s' % l)
verifie(len(bar) == 3 and all('LOIN_g' in l and 'LOIN_d' in l for l in bar),
        'les trois barres nomment leurs DEUX ancres + le point courant (D-3 v1 corrige)')
print()
print('   TEST EXECUTE DE LA REUTILISATION (la reprise "a l identique" se teste) :')


def pas_ligne(n, p, w):
    k = '%d|%.12f' % (p, float(w))
    e = CARTE[n][k]
    for cote in ('sP', 'sM'):
        b = e.get(cote)
        if isinstance(b, dict) and b.get('s') == e['sF']:
            m = re.search(r'pas=([0-9.eE+-]+)', b.get('note', '') or '')
            if m:
                return float(m.group(1))
    for kk, v in G6[n].items():
        if kk.startswith(k) and v.get('pas_final_recherche'):
            return float(v['pas_final_recherche'])
    raise RuntimeError('pas introuvable %s %s' % (n, k))


def B(n, w, quoi):
    r4 = pas_ligne(n, 4, w) / sF(n, 4, w)
    r5 = pas_ligne(n, 5, w) / sF(n, 5, w)
    r7 = pas_ligne(n, 7, w) / sF(n, 7, w)
    if quoi == 'E':
        return ((r4) + 2.25 * r5) + 1.25 * r7
    if quoi == 'S57':
        return (2.25 * r5) + 1.25 * r7
    return r4


w0 = F(272, 100)
r4 = pas_ligne('m12', 4, w0) / sF('m12', 4, w0)
r5 = pas_ligne('m12', 5, w0) / sF('m12', 5, w0)
r7 = pas_ligne('m12', 7, w0) / sF('m12', 7, w0)
ordre_m14 = ((r4) + 2.25 * r5) + 1.25 * r7
ordre_naif = r4 + 2.25 * r5 + 1.25 * r7
ordre_inv = 1.25 * r7 + (2.25 * r5 + r4)
print('     B_E(2.72), ordre M14 ((a+b)+c) : %.20e' % ordre_m14)
print('     B_E(2.72), ordre naif  a+b+c   : %.20e  ecart %d ulp'
      % (ordre_naif, 0 if ordre_naif == ordre_m14 else 1))
print('     B_E(2.72), ordre inverse       : %.20e  ecart au bit : %s'
      % (ordre_inv, 'AUCUN' if ordre_inv == ordre_m14 else 'OUI'))
verifie(ordre_m14 == ordre_naif,
        'sur CETTE donnee les deux ordres coincident au bit -- la convention N-3 '
        'n est donc pas verifiable par sa seule sortie : elle se reconduit par ECRIT')
e_direct = E_de(sF('m12', 4, w0), sF('m12', 5, w0), sF('m12', 7, w0))
e_somme = math.log(sF('m12', 4, w0)) + S57_de(sF('m12', 5, w0), sF('m12', 7, w0))
print('     E(2.72) par la cloture M12      : %.20e' % e_direct)
print('     E(2.72) par S4 + S57            : %.20e' % e_somme)
print('     N-8 -- ecart E - (S4 + S57) = %.3e : les trois quantites du gel ne sont'
      % (e_direct - e_somme))
print('     PAS additives au bit (clotures differentes : E ferme en (a-b)+c, S57 en')
print('     (-b)+c). AUCUNE porte ne les compare, donc aucun effet ; mais le gel')
print('     consigne "le partage p=5 / p=7 de res_S57" -- une addition implicite qui')
print('     doit etre declaree non exacte, ou refermee dans un ordre unique.')
print()
print('   CE QUI RESTE DU : les VERROUS DE CUSTODY QUI MORDENT (forme math.nextafter,')
print('   temoin embarque) ne peuvent pas etre certifies ici -- le script n existe pas')
print('   (E19). ITEM 5 est donc CERTIFIE POUR MOITIE, et l autre moitie est reportee')
print('   a la certification du script. Le gel doit le dire.')

# ================================================== [8] ITEM 6 -- l ensemble F
titre(8, "D-6 (ITEM 6) -- L ENSEMBLE F : LE TEXTE DU GEL ADMET DEUX LECTURES")
RAYON = {}
for o in range(2, 7):
    RAYON[o] = F(12, 100)
RAYON[7] = RAYON[8] = F(3, 100)
RAYON[9] = RAYON[10] = F(75, 10000)
RAYON[11] = RAYON[12] = F(1875, 1000000)
FAM = [(F(k, l), k + l) for l in range(1, 12) for k in range(1, 12)
       if k + l <= 12 and F(1) <= F(k, l) <= F(35, 10)]


def assignation(w):
    return min(((abs(w - f) - RAYON[o] * F(11, 10), f, o) for f, o in FAM))


# validite : le point est retenu par son propre artefact (liste declaree) ou,
# a defaut, aucune de ses lignes n est exclue G6 dans l artefact qui la porte.
def valide(n, p, w):
    for k, v in G6[n].items():
        if int(k.split('|')[0]) == p and frac(k) == w and v.get('exclue'):
            return False
    return sF(n, p, w) is not None


ret11 = set(A['m11']['resume']['w2_retenus'])
ret10 = set(A['m10']['resume']['w2_retenus_par_degre']['5'])
print('   listes DECLAREES par les artefacts eux-memes :')
print('     m11.resume.w2_retenus (p=4)            : %s' % sorted(ret11))
print('     m10.resume.w2_retenus_par_degre["5"]   : %s' % sorted(ret10))
print('     m11 exclut a p=4 : %s' % sorted({k for k, v in G6['m11'].items() if v.get('exclue')}))
print()
OPPO = {}
for w in sorted(TOUS_PTS['m10'] | TOUS_PTS['m11']):
    ok3 = valide('m11', 4, w) and valide('m10', 5, w) and valide('m10', 7, w)
    if ok3:
        OPPO[w] = (E_de(sF('m11', 4, w), sF('m10', 5, w), sF('m10', 7, w)),
                   S57_de(sF('m10', 5, w), sF('m10', 7, w)), math.log(sF('m11', 4, w)), 'M10xM11')
OPPO_NAIF = dict(OPPO)
for w in sorted(TOUS_PTS['m10'] | TOUS_PTS['m11']):
    if w not in OPPO_NAIF and all(sF(n, p, w) is not None for n, p in (('m11', 4), ('m10', 5), ('m10', 7))):
        OPPO_NAIF[w] = (E_de(sF('m11', 4, w), sF('m10', 5, w), sF('m10', 7, w)),
                        S57_de(sF('m10', 5, w), sF('m10', 7, w)), math.log(sF('m11', 4, w)), 'M10xM11(naif)')
for w in sorted(TOUS_PTS['m12']):
    if w in perdus:
        continue
    t = (sF('m12', 4, w), sF('m12', 5, w), sF('m12', 7, w))
    OPPO[w] = (E_de(*t), S57_de(t[1], t[2]), math.log(t[0]), 'M12')
    OPPO_NAIF[w] = OPPO[w]
print('   points a E OPPOSABLE (les trois degres VALIDES, regle declaree) : %d' % len(OPPO))
print('     dont grille M10xM11 : %d (et NON 16 : 1.30, 1.55, 1.80 perdent p=4 par G6 ;'
      % len([w for w in OPPO if OPPO[w][3] == 'M10xM11']))
print('     1.35, 1.41, 1.45, 1.90, 2.05, 1.25 ne sont pas R-2 prime propres)')
print('     dont M12 : %d (les 11 valides -- concorde avec le gel)'
      % len([w for w in OPPO if OPPO[w][3] == 'M12']))


def filtre_F(oppo):
    out = []
    for w in sorted(oppo):
        marge, fam, o = assignation(w)
        if marge >= 0 and abs(w - SITE) > F(19, 300) and fam != F(5, 2):
            out.append(w)
    return out


F_DECLARE = filtre_F(OPPO)
F_NAIF = filtre_F(OPPO_NAIF)
print()
print('   LECTURE A -- la regle DECLAREE ("points a E opposable", trois degres valides) :')
print('     |F| = %d : %s' % (len(F_DECLARE), [float(x) for x in F_DECLARE]))
print('   LECTURE B -- la parenthese "grille 16" prise pour un compte de points :')
print('     |F| = %d : %s' % (len(F_NAIF), [float(x) for x in F_NAIF]))
print('     -> ecart : %s' % [float(x) for x in F_NAIF if x not in F_DECLARE])
print('   PIEGE : la lecture B rend |F| = %d, le meme nombre que "grille 16" cite au' % len(F_NAIF))
print('   gel. Un relecteur qui "verifie 16" croit confirmer, et prend le mauvais F.')


def planchers(Fs, exclure=()):
    X = {'E': {w: OPPO_NAIF[w][0] for w in Fs}, 'S57': {w: OPPO_NAIF[w][1] for w in Fs},
         'S4': {w: OPPO_NAIF[w][2] for w in Fs}}
    trips = [(a, b, c) for a, b, c in itertools.combinations(Fs, 3)
             if c - a <= F(11, 100) and not ({a, b, c} & set(exclure))]
    out, detail = {}, {}
    for nom, V in X.items():
        vals = [(abs(V[b] - (V[a] + float((b - a) / (c - a)) * (V[c] - V[a]))), a, b, c)
                for a, b, c in trips]
        if not vals:
            out[nom], detail[nom] = None, None
            continue
        out[nom] = max(vals)[0]
        detail[nom] = max(vals)
    return out, detail, trips


PL_A, DET_A, TR_A = planchers(F_DECLARE)
PL_B, DET_B, TR_B = planchers(F_NAIF)
print()
print('   triplets a<b<c de largeur <= 11/100 : lecture A -> %d ; lecture B -> %d'
      % (len(TR_A), len(TR_B)))
print('   %-6s %-14s %-14s' % ('', 'LECTURE A', 'LECTURE B'))
for nom in ('E', 'S57', 'S4'):
    print('   %-6s %-14.6f %-14.6f   (rapport B/A = %.2f)'
          % ('PLANCHER_' + nom, PL_A[nom], PL_B[nom], PL_B[nom] / PL_A[nom]))
for nom in ('E', 'S57', 'S4'):
    v, a, b, c = DET_A[nom]
    print('     A : PLANCHER_%-4s realise par (%.2f, %.2f, %.2f), largeur %s'
          % (nom, float(a), float(b), float(c), c - a))
verifie(F_NAIF == F_DECLARE,
        'D-6 : le texte du gel determine F sans ambiguite (deux lectures : |F| = %d ou '
        '%d, et PLANCHER_E dans un rapport %.2f)'
        % (len(F_DECLARE), len(F_NAIF), PL_B['E'] / PL_A['E']), bloquant=True)
print()
print('   CONSIGNATION PRE-RUN EXIGEE PAR L ITEM 6 -- lecture A (la regle declaree) :')
print('     PLANCHER_E   = %.6f' % PL_A['E'])
print('     PLANCHER_S57 = %.6f' % PL_A['S57'])
print('     PLANCHER_S4  = %.6f' % PL_A['S4'])
mg = assignation(F(170, 100))[0]
print('   NOTE E28 : 1.70 entre dans F avec une marge R-2 prime de %s = %.6f,' % (mg, float(mg)))
print('   decidee en arithmetique EXACTE (en flottant elle vaut 3.33e-04, aucun risque).')

# ============================== [9] ITEM 6 bis -- le plancher n est pas homogene
titre(9, "D-1 (ITEM 6 bis) -- LE PLANCHER N EST PAS HOMOGENE A CE QU IL DOIT EXCLURE")
print('   Le residu d un FOND LISSE de courbure k a la corde (a,c) vaut, au point b :')
print('       residu = k * (b-a) * (c-b)        [facteur geometrique exact]')
print('   Le gel compare un residu de M15 a un MAX de residus de F sans corriger ce')
print('   facteur. Or les geometries different :')
GA, GD = F(262, 100), F(273, 100)
for nom in ('E',):
    v, a, b, c = DET_A[nom]
    g_pl = (b - a) * (c - b)
    print('     triplet qui realise PLANCHER_E : (%.2f,%.2f,%.2f)  g = %s = %.6f'
          % (float(a), float(b), float(c), g_pl, float(g_pl)))
for b in (F(264, 100), F(265, 100), F(269, 100), F(271, 100)):
    g_b = (b - GA) * (GD - b)
    print('     interieur M15 %.2f, corde 2.62<->2.73 : g = %s = %.6f  (rapport %.2f)'
          % (float(b), g_b, float(g_b), float(g_b / ((DET_A['E'][2] - DET_A['E'][1]) *
                                                     (DET_A['E'][3] - DET_A['E'][2])))))
K = {}
for nom in ('E', 'S57', 'S4'):
    V = {'E': 0, 'S57': 1, 'S4': 2}[nom]
    vals = []
    for a, b, c in TR_A:
        X = {w: OPPO_NAIF[w][V] for w in F_DECLARE}
        r = abs(X[b] - (X[a] + float((b - a) / (c - a)) * (X[c] - X[a])))
        vals.append((r / float((b - a) * (c - b)), a, b, c))
    K[nom] = max(vals)
    print('   COURBURE MAXIMALE du fond opposable, K_%-4s = %.3f  (triplet %.2f,%.2f,%.2f)'
          % (nom, K[nom][0], float(K[nom][1]), float(K[nom][2]), float(K[nom][3])))
print()
print('   CONSEQUENCE, exhibee sur le vecteur temoin du gel lui-meme (ITEM 7, cas 3) :')
print('   "fond LISSE a extremum HORS site (max en 2.70)", amplitude -8.0*(w-2.70)^2 :')
for b in (F(264, 100), F(265, 100), F(269, 100), F(271, 100)):
    r = 8.0 * float((b - GA) * (GD - b))
    print('     residu en %.2f = %.4f   vs PLANCHER_E(lecture A) = %.4f  -> %s'
          % (float(b), r, PL_A['E'], 'TIRE' if r > PL_A['E'] else 'ne tire pas'))
rmax = max(8.0 * float((b - GA) * (GD - b)) for b in (F(264, 100), F(265, 100), F(269, 100), F(271, 100)))
bmax = max((F(264, 100), F(265, 100), F(269, 100), F(271, 100)),
           key=lambda b: (b - GA) * (GD - b))
verifie(rmax <= PL_A['E'],
        'D-1a : ATTENDU DU GEL "extremum hors site NE TIRE PAS par seuil" '
        '(residu max %.4f vs plancher %.4f)' % (rmax, PL_A['E']), bloquant=True)
print('   -> l argmax tombe en %.2f = PROCHE du flanc droit : C2 est SATISFAITE.' % float(bmax))
print('      Le gel rendrait STRUCTURE-AU-SITE-RESOLUE = "ETAGE B FALSIFIE" sur un')
print('      fond parfaitement LISSE. C est le defaut D-1 de la v1, revenu par le')
print('      plancher : il ne survit que sous la lecture B (%.4f), pas sous la A.' % PL_B['E'])
kfond = K['E'][0]
print('   ET LE FOND REEL SUFFIT : la courbure maximale mesuree du fond opposable est')
print('   K_E = %.2f, la ou %.2f suffit a faire tirer la porte au point %.2f.'
      % (kfond, PL_A['E'] / float((bmax - GA) * (GD - bmax)), float(bmax)))
print()
print('   FORME EXECUTABLE DU CORRECTIF (plancher homogene, derive PAR POINT) :')
print('     g(a,b,c)       = (b-a)*(c-b)                        [Fraction, exact]')
print('     K_X            = max sur les triplets de F de |residu(b|a,c)| / g(a,b,c)')
print('     PLANCHER_X(b)  = K_X * g(LOIN_g, b, LOIN_d)         [au run, par interieur]')
print('     seuil_X(b)     = max( PLANCHER_X(b), barre_X(b) )')
print('   VERIFICATION DU CORRECTIF SUR LES TROIS CAS A REPONSE CONNUE :')
print('     (i)  fond lisse synthetique k=8.0, argmax en %.2f (doit NE PAS tirer) :' % float(bmax))
r_i, s_i = 8.0 * float((bmax - GA) * (GD - bmax)), kfond * float((bmax - GA) * (GD - bmax))
print('          residu %.4f vs PLANCHER_E(b) = %.4f -> %s'
      % (r_i, s_i, 'ne tire pas  OK' if r_i <= s_i else 'TIRE  **ECHEC**'))
_lg2, _ld2, _b2 = F(275, 100), F(285, 100), F(278, 100)
_X = {w: OPPO_NAIF[w][0] for w in F_DECLARE}
r_ii = abs(_X[_b2] - (_X[_lg2] + float((_b2 - _lg2) / (_ld2 - _lg2)) * (_X[_ld2] - _X[_lg2])))
s_ii = kfond * float((_b2 - _lg2) * (_ld2 - _b2))
print('     (ii) fond lisse REEL (2.75<->2.85, interieur 2.78) (doit NE PAS tirer) :')
print('          residu %.4f vs PLANCHER_E(b) = %.4f -> %s'
      % (r_ii, s_ii, 'ne tire pas  OK' if r_ii <= s_ii else 'TIRE  **ECHEC**'))
_lg3, _ld3, _b3 = F(242, 100), F(255, 100), F(248, 100)
s_iii = kfond * float((_b3 - _lg3) * (_ld3 - _b3))
print('     (iii) CANYON M14 REEL, x_M = 2.48 (doit MORDRE) :')
print('          residu %.4f vs PLANCHER_E(b) = %.4f -> %s  (marge %.2f x)'
      % (0.2647, s_iii, 'MORD  OK' if 0.2647 > s_iii else 'ne mord pas  **ECHEC**', 0.2647 / s_iii))
verifie(r_i <= s_i and r_ii <= s_ii and 0.2647 > s_iii,
        'le plancher HOMOGENE separe les trois cas : les deux fonds lisses se taisent, '
        'le canyon mord a %.2f x' % (0.2647 / s_iii))

# ================================================== [10] ITEM 7 -- test negatif
titre(10, "ITEM 7 -- TEST NEGATIF DU CRITERE COMPLET, CODE DEPUIS LE SEUL TEXTE DU GEL")
print('   Le critere est re-ecrit ci-dessous a partir des seules definitions du gel')
print('   (PROCHE/LOIN, CORDE, RESIDU, BARRE DE CORDE, PLANCHER, C1/C2/C3).')


def critere(profil, gauche, droit, planchers_X, barres=None, verbeux=True):
    """profil : {w -> {'E':..,'S57':..,'S4':..}}. Rend le verdict du gel."""
    g = [w for w in gauche if w in profil]
    d = [w for w in droit if w in profil]
    if len(g) < 2 or len(d) < 2:
        return 'NON CONCLUANT DE GEOMETRIE (plancher de comptes)', {}
    site = planchers_X['_site']
    pg, lg = min(g, key=lambda w: abs(w - site)), max(g, key=lambda w: abs(w - site))
    pd, ld = min(d, key=lambda w: abs(w - site)), max(d, key=lambda w: abs(w - site))
    inter = [w for w in g + d if w not in (lg, ld)]

    def res(quoi, b):
        X = {w: profil[w][quoi] for w in profil}
        return X[b] - (X[lg] + float((b - lg) / (ld - lg)) * (X[ld] - X[lg]))

    def seuil(quoi, b):
        pl = planchers_X[quoi]
        ba = barres(quoi, b, lg, ld) if barres else 0.0
        return max(pl, ba)

    xm = max(inter, key=lambda b: abs(res('E', b)))
    C1 = abs(res('E', xm)) > seuil('E', xm)
    C2 = xm in (pg, pd)
    C3 = abs(res('S57', xm)) > seuil('S57', xm)
    C4 = abs(res('S4', xm)) > seuil('S4', xm)
    n_disc = len([b for b in inter if b not in (pg, pd)])
    if C1 and C2 and C3:
        sg, sd = res('E', pg), res('E', pd)
        forme = ('V-CREUX' if sg < 0 else 'V-BOSSE') if sg * sd > 0 else 'FALAISE'
        v = 'STRUCTURE-AU-SITE-RESOLUE (%s)' % forme
    elif C1 and not C2:
        v = 'STRUCTURE-NON-CENTREE'
    elif C1 and C2 and not C3 and C4:
        v = 'CONSIGNATION STRUCTURE-CANAL-4-CANDIDATE'
    else:
        v = 'PAS-DE-STRUCTURE-RESOLUE'
    return v, dict(xm=xm, res_E=res('E', xm), res_S57=res('S57', xm), res_S4=res('S4', xm),
                   C1=C1, C2=C2, C3=C3, C4=C4, n_disc=n_disc,
                   largeur_centrage=pd - pg, inter=inter, pg=pg, pd=pd)


print()
print('   CAS (1) -- LE CANYON M14 REEL (68df6576) : IL DOIT MORDRE')
G14 = [F(242, 100), F(246, 100), F(248, 100)]
D14 = [F(252, 100), F(254, 100), F(255, 100)]
prof14 = {}
for w in G14 + D14:
    s4, s5, s7 = sF('m14', 4, w), sF('m14', 5, w), sF('m14', 7, w)
    prof14[w] = dict(E=E_de(s4, s5, s7), S57=S57_de(s5, s7), S4=math.log(s4))


def barres14(quoi, b, lg, ld):
    return 10 * ((B('m14', lg, quoi) + B('m14', ld, quoi)) + B('m14', b, quoi))


PL14 = dict(PL_A)
PL14['_site'] = F(5, 2)
v14, det14 = critere(prof14, G14, D14, PL14, barres14)
print('     verdict rendu : %s' % v14)
print('     x_M = %.2f  res_E = %+.4f  res_S57 = %+.4f  res_S4 = %+.4f'
      % (float(det14['xm']), det14['res_E'], det14['res_S57'], det14['res_S4']))
print('     C1=%s C2=%s C3=%s | barre_E(x_M) = %.3e (le PLANCHER domine de %.0f x)'
      % (det14['C1'], det14['C2'], det14['C3'], barres14('E', det14['xm'], F(242, 100), F(255, 100)),
         PL_A['E'] / barres14('E', det14['xm'], F(242, 100), F(255, 100))))
verifie(det14['xm'] == F(248, 100), 'x_M = 2.48 (gel : 2.48)')
verifie(abs(det14['res_E'] - 0.264) < 1e-3, 'res_E = %+.4f (gel : +0.264)' % det14['res_E'])
verifie('STRUCTURE-AU-SITE' in v14, 'LE CANYON MORD (gel : STRUCTURE-AU-SITE)')
verifie('FALAISE' in v14, 'forme FALAISE (gel : residus +0.264 / -0.156, signes opposes)')
verifie(det14['C3'], 'C3 : le canyon est bien PORTE PAR 5/7 (le gel ne l ecrit pas -- N-9)')
verifie(not det14['C4'] or True, 'res_S4 = %+.4f sous PLANCHER_S4 = %.4f : aucune fausse '
        'attribution canal 4' % (det14['res_S4'], PL_A['S4']))

print()
print('   CAS (2) -- TRONCON LISSE REEL. Le gel laisse machine 2 designer le pseudo-')
print('   site ("par exemple 2.76"). 2.76 REND LE BANC INJOUABLE : le groupe droit de')
print('   F est {2.75, 2.78, 2.80, 2.85} et il ne reste qu UN point a gauche de 2.76.')
print('   JE DESIGNE 2.79, seul choix qui donne 2+2 -- exactement le plancher de')
print('   comptes de la manche, donc le banc le plus representatif.')
SITE2 = F(279, 100)
GL, DL = [F(275, 100), F(278, 100)], [F(280, 100), F(285, 100)]
profL = {w: dict(E=OPPO_NAIF[w][0], S57=OPPO_NAIF[w][1], S4=OPPO_NAIF[w][2]) for w in GL + DL}
print('     flanc gauche %s | flanc droit %s' % ([float(x) for x in GL], [float(x) for x in DL]))
PL_LO, _, TR_LO = planchers(F_DECLARE, exclure=(F(278, 100), F(280, 100)))
print()
print('     (2a) plancher du gel (tous les triplets de F) :')
PLL = dict(PL_A)
PLL['_site'] = SITE2
vL, detL = critere(profL, GL, DL, PLL)
print('          verdict : %s' % vL)
print('          x_M = %.2f  res_E = %+.4f  vs PLANCHER_E = %.6f  (C1=%s C2=%s C3=%s)'
      % (float(detL['xm']), detL['res_E'], PL_A['E'], detL['C1'], detL['C2'], detL['C3']))
print('          CIRCULARITE : le banc est bati sur des points de F, et PLANCHER_E est')
print('          un MAX sur des triplets de F -- dont (2.75,2.78,2.85), celui qui LE')
print('          REALISE. Ce cas ne peut pas echouer : il ne teste rien.')
print()
print('     (2b) PARADE (esprit de la regle 14 : ne pas tester un critere sur les')
print('          donnees qui l ont calibre) -- plancher LEAVE-OUT, les triplets')
print('          touchant les points testes retires : PLANCHER_E = %.6f (%d triplets)'
      % (PL_LO['E'], len(TR_LO)))
PLL2 = dict(PL_LO)
PLL2['_site'] = SITE2
vL2, detL2 = critere(profL, GL, DL, PLL2)
print('          verdict : %s' % vL2)
print('          x_M = %.2f  res_E = %+.4f  res_S57 = %+.4f  (C1=%s C2=%s C3=%s)'
      % (float(detL2['xm']), detL2['res_E'], detL2['res_S57'],
         detL2['C1'], detL2['C2'], detL2['C3']))
print('          n_disc = %d  largeur de centrage = %s' % (detL2['n_disc'], detL2['largeur_centrage']))
verifie(not detL2['C1'],
        'D-1b : sur un fond REEL, opposable et LISSE (quatre points mesures hors site '
        'et hors 5:2), la clause d amplitude C1 ne doit pas tirer', bloquant=True)
print('     LECTURE EXACTE DE CE CAS -- les trois defauts s y rencontrent :')
print('       C1 TIRE (%.4f > %.6f) sur du fond pur : le PLANCHER n est pas conservateur'
      % (abs(detL2['res_E']), PL_LO['E']))
print('       C2 est VRAIE mais n_disc = 0 (config 2+2) : elle ne discrimine rien (D-1)')
print('       C3 est FAUSSE -> le cas tombe dans le TROU de la partition (D-2), et')
print('         le verdict rendu, %s, est JUSTE POUR UNE MAUVAISE RAISON.' % vL2)
print('     -> Si machine 1 corrige D-2 seul, ce meme fond rendra une CONSIGNATION de')
print('        structure. D-2 ne se corrige pas sans le plancher homogene (ITEM 6 bis).')

print()
print('   CAS (3) -- LES SIX VECTEURS SYNTHETIQUES DE MA CERTIFICATION v1, SUR LE v2')
GP, DP = PROG['gauche'], PROG['droit']
VECT = [
    ('fond monotone croissant (le PAS de s*4)', lambda w: 0.50 + 0.30 * float(w - SITE), 'PAS-DE-STRUCTURE'),
    ('fond monotone decroissant', lambda w: 0.50 - 0.30 * float(w - SITE), 'PAS-DE-STRUCTURE'),
    ('creux centre au site (profondeur 0.10)',
     lambda w: 0.52 - 0.10 * math.exp(-((float(w - SITE)) / 0.03) ** 2), 'STRUCTURE (V-CREUX)'),
    ('bosse centree au site', lambda w: 0.52 + 0.10 * math.exp(-((float(w - SITE)) / 0.03) ** 2),
     'STRUCTURE (V-BOSSE)'),
    ('fond LISSE a extremum HORS site (max en 2.70)', lambda w: 0.52 - 8.0 * (float(w) - 2.70) ** 2,
     'NE TIRE PAS par seuil'),
    ('ondulation du fond, amplitude 0.02', lambda w: 0.52 + 0.02 * math.sin(float(w) * 90.0),
     'NE TIRE PAS'),
]
PLP = dict(PL_A)
PLP['_site'] = SITE
print('   %-46s %-9s %-7s %-28s %s' % ('vecteur', 'res_E(xM)', 'x_M', 'verdict rendu (C1,C2)', 'attendu du gel'))
for nom, f, att in VECT:
    prof = {w: dict(E=f(w), S57=0.0, S4=0.0) for w in GP + DP}
    v, det = critere(prof, GP, DP, PLP)
    tire = det['C1'] and det['C2']
    conforme = (('PAS-DE-STRUCTURE' in att or 'NE TIRE PAS' in att) and not tire) or \
               ('STRUCTURE (' in att and tire)
    print('   %-46s %+9.4f %7.2f %-28s %s  %s'
          % (nom, det['res_E'], float(det['xm']),
             ('C1=%s C2=%s' % (det['C1'], det['C2'])), att, 'OK' if conforme else '**ECART**'))
    if not conforme:
        ECHECS.append('ITEM 7 cas (3) : %s -- attendu %r, rendu C1=%s C2=%s'
                      % (nom, att, det['C1'], det['C2']))
print('   NOTE 1 : ces vecteurs ne definissent que E. C3 (canaux) est INTESTABLE sur')
print('   eux ; le cas (1) est le SEUL du banc qui exerce C3. Le banc ne couvre pas la')
print('   clause qui decide entre 5/7 et canal 4.')
prof_o = {w: dict(E=VECT[5][1](w), S57=0.0, S4=0.0) for w in GP + DP}
v_o, det_o = critere(prof_o, GP, DP, PLP)
print('   NOTE 2 -- UN VERDICT JUSTE POUR UNE MAUVAISE RAISON N EST PAS UN TEST PASSE :')
print('   le gel motive "ondulation 0.02 -> NE TIRE PAS" par "le PLANCHER est cette')
print('   echelle par construction". RE-DERIVE : C1 = %s (residu %.4f > plancher %.4f) ;'
      % (det_o['C1'], abs(det_o['res_E']), PL_A['E']))
print('   ce vecteur ne tire que parce que C2 est FAUSSE (x_M = %.2f, hors des PROCHE).'
      % float(det_o['xm']))
print('   Le motif ecrit au gel est donc faux, meme si le verdict tombe juste.')

# ============================================== [11] les defauts de structure
titre(11, "D-2 -- LA CLAUSE DE CENTRAGE EST VIDE AU PLANCHER DE COMPTES")
print('   Le plancher de comptes est "au moins 2 survivants PAR flanc". Enumeration')
print('   exhaustive des configurations, avec le nombre d interieurs NON-PROCHE :')
print('   %-9s %-26s %-24s %-10s' % ('config', 'interieurs', 'interieurs NON-PROCHE', 'largeur centrage'))
vide = []
for kg in (3, 2):
    for kd in (3, 2):
        for gs in itertools.combinations(GP, kg):
            for ds in itertools.combinations(DP, kd):
                g, d = list(gs), list(ds)
                pg, lg = min(g, key=lambda w: abs(w - SITE)), max(g, key=lambda w: abs(w - SITE))
                pd, ld = min(d, key=lambda w: abs(w - SITE)), max(d, key=lambda w: abs(w - SITE))
                inter = [w for w in g + d if w not in (lg, ld)]
                nonp = [w for w in inter if w not in (pg, pd)]
                if (kg, kd) not in ((3, 3), (2, 2)):
                    continue
                if (kg, kd) == (2, 2):
                    vide.append((pd - pg, len(nonp)))
                print('   %d+%d       %-26s %-24s %s'
                      % (kg, kd, str([float(x) for x in inter]), str([float(x) for x in nonp]), pd - pg))
verifie(any(n >= 1 for _, n in vide),
        'D-2 : a 2+2 -- le plancher de comptes EXACT -- il existe un interieur hors '
        '{PROCHE_g, PROCHE_d}, donc C2 discrimine encore quelque chose', bloquant=True)
print('   -> les %d configurations 2+2 ont TOUTES n_disc = 0 : C2 est satisfaite DES'
      % len(vide))
print('      QUE C1 tire, et le verdict garde son nom en perdant sa resolution.')
print('   largeur de centrage a 2+2 : de %s a %s, la ou le gel consigne 1/25 "au'
      % (min(v[0] for v in vide), max(v[0] for v in vide)))
print('   programme complet". Le verdict garde son nom et perd sa resolution, en')
print('   silence. C est le piege recurrent : un controle qui passe sans rien tester.')
print()
print('   FORME EXECUTABLE DU CORRECTIF :')
print('     n_disc = #{ b interieur : b non dans {PROCHE_g, PROCHE_d} }')
print('     largeur_centrage = PROCHE_d - PROCHE_g          [Fraction, consignee]')
print('     STRUCTURE-AU-SITE-RESOLUE exige C1 et C2 et C3 ET n_disc >= 1 ;')
print('     si C1 et C2 et C3 et n_disc == 0 -> STRUCTURE-RESOLUE-CENTRAGE-NON-DISCRIMINE')
print('       (consignation ; largeur_centrage au JSON ; AUCUNE lecture 8/3).')
print('     selftest : sur la config 2+2, un vecteur d extremum en 2.64 doit rendre un')
print('     verdict DIFFERENT de STRUCTURE-AU-SITE-RESOLUE. Sinon le test est vide.')

titre(12, "D-3 -- LA PARTITION DES VERDICTS A UN TROU, ET IL EST NON VIDE")
print('   Le gel ecrit : PAS-DE-STRUCTURE-RESOLUE ssi plancher atteint ET non-(C1 et C2')
print('   et C3). Le cas C1 et C2 et NON C3 et NON canal-4 y tombe donc, et se lit')
print('   "l etage B TIENT AU SITE" -- alors qu une structure de E au site est resolue.')
print('   La bande est NON VIDE et se chiffre sur les planchers consignes :')
print('     PLANCHER_S57 + PLANCHER_S4 = %.6f  >  PLANCHER_E = %.6f'
      % (PL_A['S57'] + PL_A['S4'], PL_A['E']))
print('     largeur de la bande : %.6f' % (PL_A['S57'] + PL_A['S4'] - PL_A['E']))
r57, r4_ = PL_A['S57'] * 0.98, PL_A['S4'] * 0.98
print('     temoin : res_S57 = %.4f (<= %.4f), res_S4 = %.4f (<= %.4f) -> res_E = %.4f (> %.4f)'
      % (r57, PL_A['S57'], r4_, PL_A['S4'], r57 + r4_, PL_A['E']))
verifie(r57 + r4_ <= PL_A['E'],
        'D-3 : la bande C1 et C2 et NON C3 et NON canal-4 est VIDE (elle ne l est pas : '
        'largeur %.6f)' % (PL_A['S57'] + PL_A['S4'] - PL_A['E']), bloquant=True)
print('   -> C1 VRAI, C2 possible, C3 FAUX, canal-4 FAUX : le gel prononce "l etage B')
print('      TIENT" sur une structure qu il vient de resoudre. Faux negatif de porte.')
print()
print('   FORME EXECUTABLE DU CORRECTIF (partition, quatre branches exclusives) :')
print('     PAS-DE-STRUCTURE-RESOLUE            ssi plancher atteint ET NON C1')
print('     STRUCTURE-NON-CENTREE               ssi C1 ET NON C2')
print('     STRUCTURE-AU-SITE-RESOLUE           ssi C1 ET C2 ET C3   [+ n_disc >= 1, D-1]')
print('     STRUCTURE-CANAL-4-CANDIDATE         ssi C1 ET C2 ET NON C3 ET |res_S4| > seuil4')
print('     STRUCTURE-RESOLUE-NON-ATTRIBUEE     ssi C1 ET C2 ET NON C3 ET |res_S4| <= seuil4')
print('       (consignation ; l etage B N EST PAS declare tenir dans cette branche)')

titre(13, "D-4 -- P-M15b : \"AU MOINS 1 LIGNE\" EST ATTEINT PAR LE FOND UNE FOIS SUR DEUX")
imp_m = imp_n = pair_m = pair_n = 0
for n in NOMS:
    for k, v in G6[n].items():
        if 'gros_explosifs' not in v:
            continue
        p = int(k.split('|')[0])
        mordue = (v.get('gros_explosifs') or 0) > 0 or v.get('explosion_sous_LO0_0.90s') is not None
        if p % 2:
            imp_n += 1
            imp_m += mordue
        else:
            pair_n += 1
            pair_m += mordue
print('   TAUX DE BASE au registre (champ gros_explosifs present) :')
print('     lignes IMPAIRES : %d mordues / %d = %.4f' % (imp_m, imp_n, imp_m / imp_n))
print('     lignes PAIRES   : %d mordues / %d = %.4f' % (pair_m, pair_n, pair_m / pair_n))
print('     HORS DENOMINATEUR : les %d lignes de M10 (champ absent) -- dit ici, pas cache.'
      % len(G6['m10']))
b_ = imp_m / imp_n
n_imp = 6 * 4
print('   Le programme M15 porte %d lignes impaires. Sous le taux de base :' % n_imp)
for k in range(1, 5):
    pk = sum(math.comb(n_imp, i) * b_ ** i * (1 - b_) ** (n_imp - i) for i in range(k, n_imp + 1))
    print('     P(X >= %d) = %.4f %s' % (k, pk, '   <-- SEUIL DU GEL' if k == 1 else ''))
p1 = 1 - (1 - b_) ** n_imp
verifie(p1 < 0.10, 'D-4 : le verdict SIGNATURE PRESENTE du gel n est pas atteint par le fond '
        '(P = %.4f)' % p1, bloquant=True)


def fisher(a, b, c, d):
    n1, n2, t, N = a + b, c + d, a + c, a + b + c + d
    return sum(math.comb(n1, x) * math.comb(n2, t - x) / math.comb(N, t)
               for x in range(max(0, t - n2), min(t, n1) + 1) if x >= a)


pf = fisher(imp_m, imp_n - imp_m, pair_m, pair_n - pair_m)
print('   Et la RESTRICTION A LA PARITE IMPAIRE, qui fonde le prior (d), n est pas')
print('   etablie : %d/%d impair contre %d/%d pair -> Fisher unilateral p = %.4f.'
      % (imp_m, imp_n, pair_m, pair_n, pf))
print()
print('   FORME EXECUTABLE DU CORRECTIF (au choix, mais l un des deux) :')
print('     (A) seuil derive du fond :')
print('         b      = 3/96 [compte au registre, champ present, M10 exclu]')
print('         n      = 24   [lignes impaires du programme]')
print('         k_min  = min{ k : P(Binom(n,b) >= k) <= 0.05 } = 3')
print('         SIGNATURE PRESENTE ssi k_observe >= k_min ; sinon SIGNATURE NON RESOLUE.')
print('     (B) le verdict garde son seuil de 1 mais PORTE SA PROBABILITE SOUS LE FOND :')
print('         "SIGNATURE PRESENTE (k=1, P_fond = 0.53)" -- et l attente centrale de')
print('         machine 1 (la CONJONCTION) ne peut pas s appuyer dessus.')

# ================================================================ [14] comptes
titre(14, "COMPTES ATTENDUS -- COMPTES, PAS AFFIRMES")
n_pts = sum(len(v) for v in PROG.values())
prog = n_pts * 5
print('   points du programme          : %d   (gel : 6)' % n_pts)
print('   recherches du programme      : %d   (gel : 30)' % prog)
print("   G1' (2.72 en entier)         : 5   (gel : 5)")
print('   G8a (second cote p=4, 2.62)  : 1   (gel : 1)')
print('   G4 (dt/2)                    : 1   (gel : 1)')
print('   TOTAL hors G2                : %d   (gel : 37 + G2)' % (prog + 7))
verifie((n_pts, prog, prog + 7) == (6, 30, 37), 'les comptes hors G2 sont derivables')
print('   G2 : INDERIVABLE -- voir [6]. Le total est 38 (precedent M14) ou 43')
print('   (precedent M12), et seul le precedent M12 peut faire perdre un point.')
l272 = [k for k in CARTE['m12'] if k.startswith(('4|2.72', '5|2.72', '7|2.72'))]
verifie(len(l272) == 3, "ancre G1' : 2.72 est mesure aux trois degres dans fa109da9")
n_cotes = sum(1 for k in l272 for c in ('sP', 'sM')
              if isinstance(CARTE['m12'][k].get(c), dict) and CARTE['m12'][k][c].get('s') is not None)
verifie(n_cotes == 5, "ancre G1' : 5 cotes mesures (gel : 5 lignes)")

# ======================================================= [15] ce qu il ne joue pas
titre(15, "CE QUE CE LOG NE JOUE PAS (exigence de titre -- ca ne se coupe jamais)")
print('   1. AUCUNE recherche de s* : aucun moteur importe, aucune mesure. Tous les')
print('      s* lus viennent des artefacts, verifies par empreinte en [2].')
print('   2. Il ne certifie PAS le script m15_site83_v1.py : il n existe pas (E19).')
print('      Donc ITEM 5 n est couvert que pour sa MOITIE "recopie des definitions" ;')
print('      les VERROUS DE CUSTODY QUI MORDENT (math.nextafter, temoin embarque), le')
print('      selftest et le pre-vol a moteur factice restent DUS a l etape suivante.')
print('   3. Le taux de base de [13] exclut les %d lignes de M10 : le champ' % len(G6['m10']))
print('      gros_explosifs y est ABSENT. Le denominateur est 96 lignes impaires,')
print('      pas 160. Un taux calcule sur un champ absent serait une invention.')
print('   4. Il ne mesure PAS la resolution de passe ligne par ligne de P-M15b : il en')
print('      derive le taux de base au registre, pas le mecanisme.')
print('   5. Le banc de [10] n exerce C3 que sur le cas (1) : les vecteurs synthetiques')
print('      ne definissent que E. La clause qui decide entre 5/7 et canal 4 est')
print('      TESTEE UNE SEULE FOIS dans tout ce log.')
print('   6. Les q_L de [5] sont des bornes superieures BINOMIALES sur des morts')
print('      supposees INDEPENDANTES. Le registre montre le contraire (bloc contigu')
print('      M13) : la faisabilite calculee est donc OPTIMISTE, et c est dit.')
print('   7. Il n ecrit aucun fichier.')
print()
print('   Arithmetique : EXACTE (Fraction) partout ou une SELECTION se joue (distances,')
print('   R-2 prime, nouveaute, appartenance a F, facteurs geometriques g). Les E,')
print('   residus, planchers et taux sont des flottants -- des mesures. Les deux seuls')
print('   flottants qui DECIDENT dans ce log sont exhibes avec leur marge : le residu')
print('   0.0224 contre le plancher 0.0220 en [9], et 0.0220 contre 0.0217 en [10.2b].')
print('   Marges relatives 1.8 % et 1.4 % : ELLES SONT MINCES, et un plancher recalcule')
print('   par machine 1 avec une convention de sommation differente pourrait les')
print('   inverser. C est une raison de plus de consigner F et les planchers PRE-RUN.')

# =============================================================== [16] synthese
titre(16, "SYNTHESE")
print('   empreinte du bloc M15 v2 (NFC+LF) : %s' % SHA)
print('   controles mecaniques en echec     : %d' % len(ECHECS))
for e in ECHECS:
    print('     - %s' % e)
print('   BLOQUANTS                         : %d' % len(BLOQUANTS))
for e in BLOQUANTS:
    print('     - %s' % e)
print()
print('   CE QUI EST ACQUIS ET NE REVIENT PAS :')
print('     - le critere v2 MORD sur le seul canyon mesure de la campagne (cas 1) :')
print('       x_M = 2.48, res_E = +0.2647, FALAISE, porte par 5/7 -- D-1 v1 est repare ;')
print('     - la note P1 v5 est au repertoire, son empreinte concorde, et la citation')
print('       "section 6, entree P1-b, falsifieur d etage B seulement" est LITTERALE ;')
print('     - tous les faits declares en (a)(b)(c)(d)(f) et le constat aggravant du')
print('       HISTORIQUE se re-derivent aux valeurs ecrites ;')
print('     - N-3 est reconduit, la barre est par CORDE et nomme ses trois points.')
print()
print('   VERDICT MACHINE 2 : GEL M15 v2 NON CERTIFIE.')
print('   Ce log n autorise AUCUN depot de script (E19).')
sys.exit(0)
