#!/usr/bin/env python3
# -*- coding: ascii -*-
"""LES VERIFICATIONS DE SA LECTURE -- machine 2, v2, 12/09/2026 (soir).

D-ACA-7, VERSE PAR MACHINE 1 ET ACCORDE : la v1 portait TROIS chk a condition litterale
`True` -- LA MEME FAUTE QUE D-ACA-1, DANS LA FEUILLE QUI CLOT D-ACA-1. Sa garde
(be6bb447da1f4363) les a trouves par l'arbre syntaxique ; je l'ai rejouee ici et elle rend
son compte au chiffre. La v2 adopte SA PROPOSITION : DEUX VERBES -- `chk` MESURE et compte,
`note` porte la PROSE et ne compte pas. La v1 n'est pas editee (PB-1).
Compte honnete de la v1 : 23 lignes au log, 21 appels statiques, dont 3 de prose
-> 20 controles capables de mordre.

Sa note a37c86b0e9b80833 verse trois corrections et pose une question. Cette feuille les
tranche AU POSTE, aux sources, jamais sur citation :

  (a) SA CORRECTION SUR tau_CAP -- la plus lourde, et elle est CONTRE MOI. Elle ecrit que
      `tau_CAP` est une FORME FERMEE et non un temps lu sur la trajectoire, donc que mon
      "ratio ~ delta est MESURE" surestime. Verifie ICI au banc DEPOSE (v3, sa citation)
      ET au banc CERTIFIE (v8, celui qui jouera) -- c'est le v8 qui tranche pour l'acte.

  (b) SA QUESTION, POSEE A MA PLUME : les feuilles `plancher_composantes` et `seuil_5_4`
      descendent-elles de `R_composantes` -- une racine ou trois ? Decidable au bit.
      Et le compte HONNETE de racines d'ETAT independantes par cellule en decoule.

  (c) `D-ACA-3`, CONTRE MOI : ma docstring de v3 dit 21, mon log dit 22.

  (d) `D-ACA-4`, DE SA MAIN : son controle nommait `dt2/4` et des etats finaux que le
      pre-vol ne porte pas. Elle dit que le `dt2/4` vient d'une AUTRE piece,
      `c8d86e5e5b4fd745`. Verifie -- y compris que sa citation RESOUT au poste.

PB-1 : rien n'est edite. La v3 n'est pas corrigee ici ; ce qu'elle doit dire va a l'acte.
"""
import ast, hashlib, json, os, re, struct, unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(ICI)
P = lambda *a: os.path.join(RAC, *a)
B = lambda x: struct.pack('>d', x).hex()
OK = []


def chk(n, c, d=''):
    """MESURE. Compte au bilan. Sa condition n'est JAMAIS une constante -- D-ACA-7."""
    OK.append((n, bool(c)))
    print('  [%s] %-54s %s' % ('PASSE' if c else 'MORD ', n[:54], d))


def note(n, d=''):
    """PROSE. Ne compte pas. Deuxieme verbe propose par machine 1 au lot 990a8fe5cec6ef87,
    adopte ici : ce qui ne peut pas mordre ne s'ecrit pas comme un controle."""
    print('  [ note] %-54s %s' % (n[:54], d))


def canon(p):
    raw = open(p, 'rb').read()
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8'))
        t = t.replace('\r\n', '\n').replace('\r', '\n').encode('utf-8')
        return hashlib.sha256(t).hexdigest()[:16]
    except UnicodeDecodeError:
        return hashlib.sha256(raw).hexdigest()[:16]


def pts(*a):
    return json.load(open(P(*a), encoding='utf-8'))['T2']['points']


# =====================================================================
print("\n(a) SA CORRECTION SUR tau_CAP -- AU BANC DEPOSE ET AU BANC CERTIFIE")
# =====================================================================
# Mordrait si tau_cap lisait un temps sur la trajectoire : la source le dirait.
SRC = re.compile(r'def tau_cap\(w2\):\s*\n\s*return ([^\n]+)')
DOM = re.compile(r'def tau_dom\(w2\):\s*\n\s*return ([^\n]+)')
for etq, f in (('banc DEPOSE (v3, sa citation)', 'banc_qualification_machine1_v3.py'),
               ('banc CERTIFIE (v8, celui qui joue)', 'banc_qualification_machine1_v8.py')):
    src = open(P(f), encoding='utf-8').read()
    mc, md = SRC.search(src), DOM.search(src)
    print('   %-36s tau_cap = %s' % (etq, mc.group(1).strip()))
    print('   %-36s tau_dom = %s' % ('', md.group(1).strip()))
    chk('%-30s tau_cap est une FORME FERMEE' % etq[:30],
        'R_CAP' in mc.group(1) and 'tau_dom' in mc.group(1), 'aucune lecture de trajectoire')
    chk('%-30s et sqrt(DELTA) y est explicite' % etq[:30],
        'sqrt' in md.group(1) and 'DELTA' in md.group(1), md.group(1).strip())
note('SA CORRECTION EST JUSTE : sqrt(delta) est PAR CONSTRUCTION',
     'le rapport 32 exact en est la signature, pas une mesure')
# Ce qui reste MESURE, et il faut le dire aussi : R contre la forme fermee.
PRE = pts('m2_v8_prevol_temoin_resultats.json')
from fractions import Fraction as F
AL = {4: F(2), 5: F(4, 3), 7: F(4, 5)}
pires = []
for k in sorted(PRE):
    p, w2 = int(k.split('|')[0]), float(k.split('|')[1])
    a, tc = float(AL[p]), PRE[k]['tau_CAP']
    pires.append(abs(PRE[k]['R_composantes'] - 2 * a * (a + 1) / ((w2 * w2 - 1) * tc * tc))
                 / (2 * a * (a + 1) / ((w2 * w2 - 1) * tc * tc)))
chk('CE QUI RESTE MESURE : R suit la forme fermee D-t-22', max(pires) < 1e-4,
    'ecart max %.2e -- c est une mesure, elle' % max(pires))

# =====================================================================
print("\n(b) SA QUESTION -- UNE RACINE OU TROIS ? DECIDE AU BIT")
# =====================================================================
EPS = 2.0 ** -52
d1 = [k for k in PRE if B(PRE[k]['plancher_composantes']) != B(EPS * PRE[k]['R_composantes'])]
d2 = [k for k in PRE if B(PRE[k]['seuil_5_4'])
      != B(PRE[k]['C_effectif'] * PRE[k]['plancher_composantes'])]
chk('plancher_composantes == eps x R_composantes AU BIT (9/9)', not d1,
    ','.join(sorted(d1)) or '0 ecart')
chk('seuil_5_4 == C_effectif x plancher_composantes AU BIT (9/9)', not d2,
    ','.join(sorted(d2)) or '0 ecart')
chk('REPONSE : UNE racine (R_composantes), TROIS feuilles', not d1 and not d2,
    'l acte inscrit des FEUILLES, elle a raison de le demander')

LOT = ('entrant_machine1_2026-09-12_reponse_globale', 'lot')
N = pts(*(LOT + ('resultats_temoin_prevol_noyau_machine1.json',)))
L = pts(*(LOT + ('resultats_temoin_prevol_libm_machine1.json',)))
print('\n   LE COMPTE HONNETE -- racines d ETAT INDEPENDANTES par cellule :')
racines = {}
for k in sorted(N):
    r = []
    if N[k]['R_composantes'] != L[k]['R_composantes']:
        r.append('R_composantes')
    if N[k]['bascule']['x_b_num'] != L[k]['bascule']['x_b_num']:
        r.append('x_b_num')
    racines[k] = r
    print('      %-8s %d racine(s) : %s' % (k, len(r), ','.join(r) or 'aucune'))
chk('CHAQUE cellule garde au moins UNE racine d ETAT',
    all(racines.values()), '9/9 -- le verdict de D-ACA-2 tient au compte honnete')
chk('4|2.27 et 4|2.80 se reduisent a la SEULE racine R_composantes',
    racines['4|2.27'] == ['R_composantes'] and racines['4|2.80'] == ['R_composantes'],
    'leurs "ETAT 3" etaient 3 feuilles, 1 racine')

# =====================================================================
print("\n(c) D-ACA-3 -- MA DOCSTRING CONTRE MON LOG")
# =====================================================================
doc = open(os.path.join(ICI, 'derivation_fenetre_delta_machine2_v3.py'),
           encoding='utf-8').read()[:3000]
log = open(os.path.join(ICI, 'derivation_fenetre_delta_machine2_v3.log'),
           encoding='utf-8', errors='replace').read()
chk('ma docstring de v3 annonce 21', 'v3 en porte 21' in doc, 'ligne 22 de la docstring')
chk('mon log rend 22', 'BILAN : 22/22' in log, 'les deux ne peuvent pas etre vrais')
note('D-ACA-3 EST JUSTE, ET C EST UN COMPTE NON NOMME',
     '22 lignes, toutes capables de mordre, dont UNE conjonction')

# =====================================================================
print("\n(d) D-ACA-4 -- SA PIECE, ET SA CITATION")
# =====================================================================
CV = P('entrant_machine1_2026-09-12_convergence_dt', 'lot',
       'convergence_dt_7_1p73_machine1_v1.json')
chk('sa citation c8d86e5e5b4fd745 RESOUT au poste', canon(CV) == 'c8d86e5e5b4fd745',
    canon(CV))
cv = json.load(open(CV, encoding='utf-8'))
chk('cette piece porte bien QUATRE flots (dt2 .. dt2/8)', len(cv['flots']) == 4,
    'k = ' + ','.join(str(f['k']) for f in cv['flots']))
chk('et elle ne porte AUCUN etat final x1, x2', not any(
    x in cv['flots'][0] for x in ('x1', 'x2')),
    ','.join(sorted(cv['flots'][0])[:6]))
chk('le PRE-VOL, lui, ne porte que dt2 et dt2/2', sorted(PRE['5|1.73']['err']) ==
    ['dt2', 'dt2/2'], 'sa lecture de sa propre faute est exacte')
# Trouve en verifiant : un piege de NOM a mon poste, et il est de ma main.
JUM = P('G2_convergence_dt', 'convergence_dt_7_1p73_machine1_v1.json')
REJ = P('G2_convergence_dt', 'rejeu1_convergence_dt_machine2_v1.json')
chk('PIEGE A MON POSTE : un fichier sous SON nom ne porte PAS son contenu',
    os.path.exists(JUM) and canon(JUM) != 'c8d86e5e5b4fd745', canon(JUM))
chk('il porte en fait MON rejeu1, au bit', os.path.exists(REJ)
    and canon(JUM) == canon(REJ), '%s == %s' % (canon(JUM), canon(REJ)))

# =====================================================================
print("\n(e) R-G2-5 -- SA FEUILLE, REJOUEE SUR LE v8 CERTIFIE (absent du registre)")
# =====================================================================
def compte_exposables(f):
    """Sa classification, appliquee au seul fichier qui decidera du run."""
    src = open(P(f), encoding='utf-8').read()
    arbre = ast.parse(src)
    numpy = any(isinstance(n, (ast.Import, ast.ImportFrom))
                and 'numpy' in ast.dump(n) for n in ast.walk(arbre))
    e = c = k = 0
    for n in ast.walk(arbre):
        if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Pow):
            if isinstance(n.left, ast.Constant):
                k += 1
            elif isinstance(n.right, ast.Constant) and n.right.value == 2:
                c += 1
            elif numpy:
                e += 1
    return e, c, k


e8, c8, k8 = compte_exposables('banc_qualification_machine1_v8.py')
e3, c3, k3 = compte_exposables('banc_qualification_machine1_v3.py')
print('   v3 (au registre, perime de cinq) EXPOSABLES %d | CARRE %d | CONST %d' % (e3, c3, k3))
print('   v8 (CERTIFIE, celui qui joue)    EXPOSABLES %d | CARRE %d | CONST %d' % (e8, c8, k8))
chk('le v8 certifie porte PLUS d exposables que le v3 depose', e8 > e3,
    '%d contre %d' % (e8, e3))
chk('son compte de 36 pour le v3 est reproduit ici', e3 == 36, '%d' % e3)
note('CE QUE R-G2-5 NE DIT PAS : le TYPE de la base a l execution',
     'une EXPOSABLE est une ligne A TYPER, pas une ligne exposee')

n, k = len(OK), sum(1 for _, o in OK if o)
print('\n=====================================================================')
print('BILAN : %d/%d controles PASSENT' % (k, n))
print('=====================================================================')
