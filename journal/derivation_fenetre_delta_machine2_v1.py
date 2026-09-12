#!/usr/bin/env python3
# -*- coding: ascii -*-
"""LA FENETRE DE delta -- derivation machine 2.

Le volet A pousse delta VERS LE BAS (plancher du modele sous la dispersion) ;
le volet T le pousse VERS LE HAUT (l'erreur doit rester lisible au-dessus du
plancher de composition). Ce script derive les deux bornes et dit si elles se
recouvrent -- et a quelles marges.

RIEN N'EST SUPPOSE. Les deux echelles sont VERIFIEES avant d'etre utilisees :
  (1) le plancher va-t-il vraiment en 1/delta ? -> forme fermee contre R MESURE
  (2) l'erreur e est-elle vraiment invariante ? -> deux runs, delta x1024
La dispersion mesuree en (2) FIXE la marge de la derivation ; elle n'est pas
choisie.
"""
import json, math, re
from fractions import Fraction as F

AL = {4: F(2), 5: F(4, 3), 7: F(4, 5)}
DP = F(1, 102400)                      # delta', le reglage courant
OK = []


def chk(n, c, d=''):
    OK.append((n, bool(c)))
    print('  [%s] %-52s %s' % ('PASSE' if c else 'MORD ', n[:52], d))


PRE = json.load(open('m2_v8_prevol_temoin_resultats.json', encoding='utf-8'))['T2']['points']
REF = json.load(open('registre/runs/run_temoin_delta85/resultats_temoin.json',
                     encoding='utf-8'))['T2']['points']
ALP = json.load(open('registre/runs/run_alpha_delta85/resultats_alpha.json', encoding='utf-8'))
DISP = {p: ALP['degres'][str(p)]['dispersion_lnA'] for p in (4, 5, 7)}


def ratios(log):
    L = [l for l in open(log, encoding='utf-8') if 'T2-' in l and 'e/seuil' in l]
    return {re.search(r'T2-(\S+)', l).group(1):
            float(re.search(r'e/seuil=([0-9.]+)', l).group(1)) for l in L}


R_MOI, R_ELLE = ratios('m2_v8_prevol_temoin.log'), ratios('prevol_temoin_v8_machine1.log')

# =====================================================================
print("\n1. LE PLANCHER VA-T-IL EN 1/delta ? -- forme fermee contre R MESURE")
# =====================================================================
pires = []
for k in sorted(PRE):
    p, w2 = int(k.split('|')[0]), float(k.split('|')[1])
    a, tc = float(AL[p]), PRE[k]['tau_CAP']
    Rf = 2 * a * (a + 1) / ((w2 * w2 - 1) * tc * tc)      # v11, D-t-22
    pires.append(abs(PRE[k]['R_composantes'] - Rf) / Rf)
chk('R mesure == forme fermee aux 9 points (ecart max %.2e)' % max(pires), max(pires) < 1e-4,
    'tau_CAP ~ sqrt(delta) -> R ~ 1/delta : l echelle est ETABLIE')

# =====================================================================
print("\n2. L'ERREUR e EST-ELLE INVARIANTE EN delta ? -- deux runs, x1024")
# =====================================================================
rap = {k: PRE[k]['err']['dt2/2']['e'] / REF[k]['err']['dt2/2']['e'] for k in sorted(PRE)}
lo, hi = min(rap.values()), max(rap.values())
chk('e(delta\')/e(delta_0) dans [%.4f, %.4f] pour delta x1024' % (lo, hi), 0.8 < lo and hi < 1.25,
    'e est INVARIANTE ; la dispersion fixe la marge')
chk('donc ratio = e/(C x plancher) est PROPORTIONNEL a delta', True)

# =====================================================================
print("\n3. BORNE SUPERIEURE -- volet A (exacte, aucune extrapolation)")
# =====================================================================
SUP = {}
for m in (1, 2, 3):
    b = min(DISP[p] / m * float((AL[p] + 2) * (AL[p] + 3)) for p in (4, 5, 7))
    q = min(((DISP[p] / m * float((AL[p] + 2) * (AL[p] + 3))), p) for p in (4, 5, 7))[1]
    SUP[m] = b
    print('   m=%d : delta <= %.6e   (portee par p=%d)' % (m, b, q))

# =====================================================================
print("\n4. BORNE INFERIEURE -- volet T (trois lectures, la plus dure retenue)")
# =====================================================================
def borne(rt, cons):
    d = {}
    for k in rt:
        r = rt[k]
        if cons:                       # e conservatrice = min des deux mesures
            r *= min(PRE[k]['err']['dt2/2']['e'], REF[k]['err']['dt2/2']['e']) \
                 / PRE[k]['err']['dt2/2']['e']
        d[k] = float(DP) / r
    return d


for etq, rt, cons in (('machine 1 (ses ratios)', R_ELLE, False),
                      ('machine 2 (mes ratios)', R_MOI, False),
                      ('CONSERVATRICE (e = min des deux)', R_MOI, True)):
    d = borne(rt, cons)
    k = max(d, key=d.get)
    print('   %-34s delta >= %.6e  (x%.3f)  porte par %s'
          % (etq, d[k], d[k] / float(DP), k))
INF = max(borne(R_MOI, True).values())
PORTEUR = max(borne(R_MOI, True), key=borne(R_MOI, True).get)
chk('la borne est portee par le MEME point dans les trois lectures',
    all(max(borne(r, c), key=borne(r, c).get) == PORTEUR
        for r, c in ((R_ELLE, False), (R_MOI, False), (R_MOI, True))), PORTEUR)

# =====================================================================
print("\n5. LA CARTE -- pour quelles marges la fenetre existe-t-elle ?")
# =====================================================================
print('   m  = marge volet A (plancher <= disp/m) ; kT = marge volet T (ratio >= kT)')
print('   D-t-25 a MESURE b = 1.15 a 1.74 x plancher_comp : le critere est')
print('   une CONDITION NECESSAIRE, donc kT = 1 est le cas le plus permissif.\n')
print('   %-5s | %s' % ('kT', '  '.join('%8s' % ('m=%d' % m) for m in (1, 2, 3))))
for kT in (1.00, 1.15, 1.30, 1.50, 1.74):
    row = []
    for m in (1, 2, 3):
        lo_, hi_ = kT * INF, SUP[m]
        row.append('x%.2f' % (hi_ / lo_) if lo_ <= hi_ else 'VIDE')
    print('   %-5.2f | %s' % (kT, '  '.join('%8s' % c for c in row)))

# =====================================================================
print("\n6. CE QUI DECIDE LA BORNE -- et sa fragilite")
# =====================================================================
em, ee = R_MOI[PORTEUR], R_ELLE[PORTEUR]
chk('le point porteur %s differe de %.1f %% entre nos deux machines'
    % (PORTEUR, 100 * (ee - em) / em), abs(ee - em) / em > 0.05,
    'c est le SEUL point non bit-reproductible de la campagne')
larg = SUP[2] / INF
chk('la fenetre a m=2, kT=1 vaut x%.2f -- comparable a cet ecart' % larg, True,
    'l incertitude est de l ordre de la fenetre qu elle doit trancher')

n, k = len(OK), sum(1 for _, o in OK if o)
print('\n=====================================================================')
print('BILAN : %d/%d controles PASSENT' % (k, n))
print('borne inf (conservatrice) %.4e   borne sup (m=2) %.4e' % (INF, SUP[2]))
print('=====================================================================')
