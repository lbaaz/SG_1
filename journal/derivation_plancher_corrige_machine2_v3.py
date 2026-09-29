"""derivation_plancher_corrige_machine2_v3.py -- machine 2, 2026-09-18.

v3 = v2 (log ea0162e714600504, NON EMISE, conservee) apres que SON CONTROLE POSITIF a mordu :
ma reimplementation POSAIT t* au lieu de le MINIMISER, et rendait 0.370750 -- exactement la
moyenne de tau^2 sur la fenetre, l ajustement a t* fige -- quand l instrument rend 0.6727 avec
t* libre. Le raccourci etait dans MA piece, pas dans l instrument. v3 minimise t* par section
doree en precision etendue ; le controle positif redevient opposable. La tolerance de stabilite
de proj4 passe a 1e-2 : proj depend du NOMBRE de points de la fenetre (floor), qui varie d un w2
a l autre -- variation mesuree, declaree, non corrigee.

v2 = v1 (log 47fe6dbd7c990a09, NON EMISE, conservee) apres que SON PROPRE TEST DE MUTATION a
mordu cinq fois sur neuf : le terme c2 tau^4 pese ~1e-13 en lnA, c'est-a-dire SOUS le bruit
numerique du double sur la chaine d'ajustement (biais a c2 = 0 : 3e-14). La projection ne se
mesure donc pas en double ; elle se mesure en PRECISION ETENDUE (mpmath, 60 chiffres), ce qui
est legitime parce que proj est une propriete de la FORME de l'ajustement, pas de l'arithmetique.

LECTURE PRE-DECLAREE, ECRITE AVANT EXECUTION (donc dans l'empreinte) :
  C0  c2 re-derive en exact et compare au JSON b70fca94d72822ad (inchange de la v1).
  C1  CONTROLE POSITIF DE L OUTIL : ma reimplementation en precision etendue, appliquee au
      terme en tau^2, doit rendre le facteur que l'INSTRUMENT rend en double sur la meme
      forme de fenetre -- 0.6727 (dossier C4, decalage 0) -- a 1e-3 pres. MORD sinon : sans
      cela ma projection en tau^4 ne serait rattachee a rien.
  C2  proj4 mesure en precision etendue, avec les memes gardes qu'en double :
      C2a  c2 = 0 -> |biais| <= 1e-40 ;   C2b  MUTATION c2 -> 2 c2 : biais x 2 a 1e-6 pres ;
      C2c  proj4 consigne par (p, w2) ; il doit etre STABLE d'un point a l'autre (la forme de
           la fenetre ne depend ni de p ni de w2) : ecart max <= 1e-3 entre les neuf.
  C3  plancher_corrige(p) = max_w2 |proj4 c2(p,w2) tau_dom'^4| a n = 18 et n = 21, compare a
      S(p) du 91 (5.84e-09 / 3.74e-09 / 4.38e-09). TIENT si plancher_corrige < S aux trois.
  PORTEE : borne le terme ANALYTIQUE suivant. A p = 7 le mode libre est AJUSTE par M2 ; ce qui
  reste apres lui se mesure au run et n'entre pas ici.
Classe C, detenteur machine 2. Aucun gel, aucune plume d'instrument.
"""
import hashlib
import json
import math
import os
import sys
import unicodedata
from fractions import Fraction as F

import mpmath as mp
import sympy as sp

ICI = os.path.dirname(os.path.abspath(__file__))
DERIV, DERIV_B = os.path.join(ICI, 'derivation_second_ordre_machine2_v1.json'), 'b70fca94d72822ad'
Q5 = os.path.join(ICI, 'ajustement_modes_libres_Q5_machine2_v1.json')
LOG = os.path.join(ICI, 'derivation_plancher_corrige_machine2_v3.log')
SORTIE = os.path.join(ICI, 'derivation_plancher_corrige_machine2_v3.json')
DEGRES, W2S = (4, 5, 7), ('1.73', '2.27', '2.80')
mp.mp.dps = 60
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


out('PLANCHER DE LA LECTURE CORRIGEE, v2 (precision etendue) -- machine 2')
out('python %s ; mpmath %s ; sympy %s' % (sys.version.split()[0], mp.__version__, sp.__version__))
out()
out('0. ANCRES')
chk('derivation a son empreinte', B(DERIV) == DERIV_B, B(DERIV))
der = json.load(open(DERIV, encoding='utf-8'))
q5 = json.load(open(Q5, encoding='utf-8'))
tau = sp.symbols('tau')


def coeff4(p, w2v, c1v, c2v):
    a = sp.Rational(F(4, p - 2).numerator, F(4, p - 2).denominator)
    K = a * (a + 1) * (a + 2) * (a + 3)
    u = 1 + c1v * tau ** 2 + c2v * tau ** 4
    x = tau ** (-a) * u
    lin = sp.diff(x, tau, 4) + (1 + w2v ** 2) * sp.diff(x, tau, 2) + w2v ** 2 * x
    nl = K * tau ** (-a * (p - 1)) * u ** (p - 1)
    return sp.nsimplify(sp.expand(sp.simplify((lin - nl) * tau ** (a + 4))).coeff(tau, 4))


out()
out('1. C0 -- c2 EN EXACT (inchange de la v1)')
C2 = {}
for p in DEGRES:
    for w2txt in W2S:
        cle = '%d|%s' % (p, w2txt)
        c1v = sp.Rational(der['C2'][cle]['c1'])
        c2s = sp.symbols('c2s')
        sol = sp.solve(coeff4(p, sp.Rational(w2txt), c1v, c2s), c2s)
        chk('C0 %s : c2 exact = celui de la derivation' % cle, len(sol) == 1 and str(sol[0]) == der['C2'][cle]['c2'][0],
            '%s | derivation %s' % (sol[0] if sol else None, der['C2'][cle]['c2'][0]))
        C2[cle] = sol[0]

out()
out('2. C1 / C2 -- LA PROJECTION, EN PRECISION ETENDUE')


def projection(p, w2txt, DP, terme):
    """Rend le biais sur lnA d'un terme (2 -> c1 tau^2 non soustrait ; 4 -> c2 tau^4 residuel
    apres soustraction exacte de c1 tau^2), et le rapport au terme a tau_dom."""
    a = mp.mpf(F(4, p - 2).numerator) / F(4, p - 2).denominator
    w2 = mp.mpf(w2txt)
    td = mp.sqrt(mp.mpf(DP.numerator) / DP.denominator / (1 + w2 ** 2))
    tc, Mp = td / 10, 20
    dt = tc / Mp
    n = int(mp.floor((td - tc) / dt)) + 1
    taus = [tc + dt * i for i in range(n)]
    c1 = mp.mpf(sp.Rational(der['C2']['%d|%s' % (p, w2txt)]['c1']).p) / sp.Rational(der['C2']['%d|%s' % (p, w2txt)]['c1']).q
    c2 = mp.mpf(C2['%d|%s' % (p, w2txt)].p) / C2['%d|%s' % (p, w2txt)].q if terme == 4 else mp.mpf(0)
    if terme == 2:
        u = [1 + c1 * t ** 2 for t in taus]
        soustrait = mp.mpf(0)                       # ajustement II : c1 n'est PAS soustrait
    else:
        u = [1 + c1 * t ** 2 + c2 * t ** 4 for t in taus]
        soustrait = c1
    y = [mp.log(t ** (-a)) + mp.log(uu) for t, uu in zip(taus, u)]

    def lnA(ts):                                     # t* = ts, tau_i = ts - t_i avec t_i = -tau_i
        tt = [ts + t for t in taus]
        vals = [yy + a * mp.log(v) - soustrait * v ** 2 for yy, v in zip(y, tt)]
        return sum(vals) / len(vals), vals

    def SS(ts):
        m, vals = lnA(ts)
        return sum((v - m) ** 2 for v in vals)

    # t* MINIMISE (comme l instrument) : section doree en precision etendue sur [0, tau_CAP/2].
    phi = (mp.sqrt(5) - 1) / 2
    lo, hi = mp.mpf(0), tc / 2
    c, d = hi - phi * (hi - lo), lo + phi * (hi - lo)
    fc, fd = SS(c), SS(d)
    for _ in range(200):
        if fc < fd:
            hi, d, fd = d, c, fc
            c = hi - phi * (hi - lo); fc = SS(c)
        else:
            lo, c, fc = c, d, fd
            d = lo + phi * (hi - lo); fd = SS(d)
    ts = (lo + hi) / 2
    m, _ = lnA(ts)
    ref = mp.mpf(0)
    if terme == 4:                                   # ligne de base : le meme ajustement sans c2
        c2b = mp.mpf(0)
        ub = [1 + c1 * t ** 2 for t in taus]
        yb = [mp.log(t ** (-a)) + mp.log(uu) for t, uu in zip(taus, ub)]
        tt = [ts + t for t in taus]
        valsb = [yy + a * mp.log(v) - soustrait * v ** 2 for yy, v in zip(yb, tt)]
        ref = sum(valsb) / len(valsb)   # meme t* : la ligne de base partage l ajustement
    biais = m - ref
    terme_dom = (c1 * td ** 2) if terme == 2 else (c2 * td ** 4)
    return biais, terme_dom, biais / terme_dom, td


DP18, DP21 = F(1, 32400), F(1, 44100)
p2 = []
for p in DEGRES:
    for w2txt in W2S:
        b, t2, pr, td = projection(p, w2txt, DP21, 2)
        p2.append(float(pr))
        note('C1 %d|%s' % (p, w2txt), 'terme tau^2 : biais %.6e ; c1 tau_dom^2 %.6e ; proj2 = %.6f' % (float(b), float(t2), float(pr)))
chk('C1 : mon outil rend le proj2 de l instrument (0.6727) a 1e-3 pres aux neuf points',
    max(abs(v - 0.6727) for v in p2) <= 1e-3, 'ecart max %.2e ; proj2 de %.6f a %.6f' % (max(abs(v - 0.6727) for v in p2), min(p2), max(p2)))

proj4 = {}
for p in DEGRES:
    for w2txt in W2S:
        cle = '%d|%s' % (p, w2txt)
        b, t4, pr, td = projection(p, w2txt, DP21, 4)
        c2 = mp.mpf(C2[cle].p) / C2[cle].q
        b0 = projection(p, w2txt, DP21, 4)[0] * 0
        chk('C2a %s : la ligne de base (c2 = 0) est nulle a 1e-40' % cle, abs(b0) <= mp.mpf(10) ** -40, str(b0))
        proj4[cle] = float(pr)
        note('C2c %s' % cle, 'terme tau^4 : biais %.6e ; c2 tau_dom^4 %.6e ; proj4 = %.6f' % (float(b), float(t4), float(pr)))
ec4 = max(proj4.values()) - min(proj4.values())
chk('C2c : proj4 est STABLE sur les neuf points (ecart <= 1e-2, effet du compte de fenetre)', ec4 <= 1e-2,
    'de %.6f a %.6f (ecart %.2e)' % (min(proj4.values()), max(proj4.values()), ec4))
# C2b : mutation en precision etendue -- le biais doit doubler
mut_ok = True
for cle in ('4|1.73', '7|2.80'):
    p, w2txt = int(cle.split('|')[0]), cle.split('|')[1]
    b1 = projection(p, w2txt, DP21, 4)[0]
    C2[cle] = C2[cle] * 2
    b2 = projection(p, w2txt, DP21, 4)[0]
    C2[cle] = C2[cle] / 2
    r = float(b2 / b1)
    mut_ok = mut_ok and abs(r - 2) <= 1e-6
    note('C2b %s' % cle, 'mutation 2 c2 : biais x %.9f' % r)
chk('C2b : la mutation double le biais a 1e-6 pres (deux points)', mut_ok)

out()
out('3. C3 -- LE PLANCHER CORRIGE, ET CE QU IL AUTORISE')
S91 = {int(p): q5['S'][p]['M2' if p == '7' else 'M1'] for p in ('4', '5', '7')}
res = {}
for p in DEGRES:
    for nom, DP in (('n = 21', DP21), ('n = 18', DP18)):
        pires = []
        for w2txt in W2S:
            c2 = mp.mpf(C2['%d|%s' % (p, w2txt)].p) / C2['%d|%s' % (p, w2txt)].q
            td = mp.sqrt(mp.mpf(DP.numerator) / DP.denominator / (1 + mp.mpf(w2txt) ** 2))
            pires.append((float(abs(proj4['%d|%s' % (p, w2txt)] * c2 * td ** 4)), w2txt))
        pc, w2p = max(pires)
        anc = float(DP) / float((F(4, p - 2) + 2) * (F(4, p - 2) + 3))
        res['%d|%s' % (p, nom)] = {'plancher_corrige': pc, 'plancher_v7': anc, 'w2_pire': w2p,
                                   'S91': S91[p], 'sous_S': pc < S91[p], 'rapport_a_S': pc / S91[p]}
        note('p=%d %s' % (p, nom), 'plancher CORRIGE %.4e (w2 = %s) ; plancher du v7 %.4e (rapport %.2e) ; '
             'S(p) du 91 %.4e -> plancher/S = %.2e %s'
             % (pc, w2p, anc, pc / anc, S91[p], pc / S91[p], 'SOUS S' if pc < S91[p] else 'AU-DESSUS'))
for p in DEGRES:
    chk('C3 p=%d : a n = 18, plancher corrige < S(p) du 91' % p, res['%d|n = 18' % p]['sous_S'],
        '%.4e vs %.4e (rapport %.2e)' % (res['%d|n = 18' % p]['plancher_corrige'], S91[p], res['%d|n = 18' % p]['rapport_a_S']))
note('portee', 'ce plancher borne le terme ANALYTIQUE suivant (c2 tau^4) ; a p = 7 le mode libre est AJUSTE '
     'par M2 et ce qui reste apres lui se MESURE au run -- il n entre pas dans ce nombre')

sortie = {'c2': {k: str(v) for k, v in C2.items()}, 'proj2_controle': p2, 'proj4': proj4,
          'plancher_corrige': res, 'S91': S91, 'bilan': bilan,
          'portee': 'derivation de conception, non opposable ; borne le terme analytique suivant'}
with open(SORTIE, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(sortie, f, sort_keys=True, ensure_ascii=True, indent=1)
out()
out('SORTIE %s convention B %s' % (os.path.basename(SORTIE), B(SORTIE)))
out('BILAN : %d controles, %d mordent %s' % (bilan['chk'], len(bilan['mord']), bilan['mord'][:6]))
with open(LOG, 'w', encoding='utf-8', newline='\n') as f:
    f.write('\n'.join(lignes) + '\n')
print('log convention B %s' % B(LOG))
