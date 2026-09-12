#!/usr/bin/env python3
# -*- coding: ascii -*-
"""LA FENETRE DE delta -- derivation machine 2, v2. 12/09/2026.

CE QUE LA v2 CHANGE PAR RAPPORT A LA v1 (lot 7883311c6e363b02, relue par machine 1) :

  D-G2-4 -- LES RATIOS VIENNENT DU JSON, PLUS DU LOG. La v1 lisait `e/seuil` dans
  les journaux, ou il est imprime a TROIS DECIMALES, puis divisait delta' par ce
  nombre tronque. La borne en heritait sa troncature. Ici les ratios sont lus au
  champ `/T2/points/<pt>/ratio_seuil` des JSON, en pleine precision. La DEFINITION
  de la borne retenue est INCHANGEE : INF = max(borne(R_MOI, True)).

  ERRATUM DU "SEUL POINT" -- ECRIT EN CONDITION, ET IL EN SORT UN CONSTAT NEUF. La v1
  portait "c est le SEUL point non bit-reproductible de la campagne" dans le CHAMP DE
  DETAIL d'un chk qui testait autre chose ; l'affirmation etait fausse et n'etait pas
  testee. Mise en condition ici, elle rend un compte que l'erratum du geste (2) ne
  donne pas : l'erratum compte TROIS cellules divergentes, AU BIT elles sont SIX. Les
  trois qui manquaient divergent de 1.4e-08, 4.1e-09 et 4.3e-10 -- invisibles a trois
  decimales. LE COMPTE DE L'ERRATUM AVAIT ETE ETABLI SUR LES LOGS : c'est la MEME
  troncature que D-G2-4, a un autre endroit. La separation est nette (rien entre 1e-07
  et 1e-02) et les six s'annulent toutes contre son run LIBM, donc les six sont du
  noyau. Rien de tout cela ne touche la borne (section 6).

  UNE LECTURE DE PLUS, ET ELLE EST NEUVE. Les deux JSON de machine 1 (run a NOYAU
  SIMD, run a LIBM) sont arrives au poste avec la cloture du geste (2). Sa ligne
  quitte donc elle aussi les trois decimales, et la quatrieme lecture -- son run
  sans noyau -- devient lisible. Elle est AFFICHEE et CONTROLEE, elle ne porte RIEN.

  LA JAMBE DE MUTATION TRAVERSE LA DERIVATION, PAS LE SITE D'APPEL. Toute la chaine
  qui mene a la borne est enfermee dans `derive(pre, ref, m1n, m1l)`, appelee DEUX
  fois : une fois sur les JSON recus, une fois sur des copies de ses deux JSON dont
  tous les `ratio_seuil` et tous les `e` sont mutes. L'issue qui ferait mordre est
  ecrivable : il suffirait qu'une ligne de `derive` fasse entrer un de ses nombres
  dans la borne -- un min(), un max(), une moyenne entre machines -- et INF bougerait.

RIEN N'EST SUPPOSE. Les deux echelles sont VERIFIEES avant d'etre utilisees :
  (1) le plancher va-t-il vraiment en 1/delta ? -> forme fermee contre R MESURE
  (2) l'erreur e est-elle vraiment invariante ? -> deux runs, delta x1024
La dispersion mesuree en (2) FIXE la marge de la derivation ; elle n'est pas choisie.

PB-1 : aucun fichier d'entree n'est edite. Les JSON de machine 1 sont lus tels que
recus ; la mutation porte sur des copies en memoire.
"""
import copy, json, os, re, struct
from fractions import Fraction as F

ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(ICI)
P = lambda *a: os.path.join(RAC, *a)

AL = {4: F(2), 5: F(4, 3), 7: F(4, 5)}
DP = F(1, 102400)                      # delta', le reglage courant
OK = []
BITS = lambda x: struct.pack('>d', x).hex()


def chk(n, c, d=''):
    """Le champ de detail ne porte que des nombres mesures ou des chemins (regle (X),
    proposee au geste (2)). Toute affirmation vit dans la condition."""
    OK.append((n, bool(c)))
    print('  [%s] %-56s %s' % ('PASSE' if c else 'MORD ', n[:56], d))


def pts(*a):
    return json.load(open(P(*a), encoding='utf-8'))['T2']['points']


PRE = pts('m2_v8_prevol_temoin_resultats.json')
REF = pts('registre', 'runs', 'run_temoin_delta85', 'resultats_temoin.json')
M1N = pts('entrant_machine1_2026-09-12_reponse_globale', 'lot',
          'resultats_temoin_prevol_noyau_machine1.json')
M1L = pts('entrant_machine1_2026-09-12_reponse_globale', 'lot',
          'resultats_temoin_prevol_libm_machine1.json')
ALP = json.load(open(P('registre', 'runs', 'run_alpha_delta85', 'resultats_alpha.json'),
                     encoding='utf-8'))
DISP = {p: ALP['degres'][str(p)]['dispersion_lnA'] for p in (4, 5, 7)}


def ratios_log(log):
    """LA LECTURE DE LA v1 -- conservee pour la CONFRONTER, plus pour s'en servir."""
    L = [l for l in open(P(log), encoding='utf-8') if 'T2-' in l and 'e/seuil' in l]
    return {re.search(r'T2-(\S+)', l).group(1):
            float(re.search(r'e/seuil=([0-9.]+)', l).group(1)) for l in L}


def ratios_json(d):
    """LA LECTURE DE LA v2 -- D-G2-4."""
    return {k: d[k]['ratio_seuil'] for k in d}


L_MOI = ratios_log('m2_v8_prevol_temoin.log')
L_ELLE = ratios_log('prevol_temoin_v8_machine1.log')


# =====================================================================
# LA DERIVATION, EN UNE SEULE FONCTION -- pour que la mutation la traverse
# =====================================================================
def derive(pre, ref, m1n, m1l, ratios_moi=None):
    """Rend (INF, PORTEUR, lectures, borne). `ratios_moi` permet de rejouer la
    lecture de la v1 (ratios du log) sans dupliquer une ligne de la chaine."""
    rm = ratios_moi if ratios_moi is not None else ratios_json(pre)

    def borne(rt, cons):
        d = {}
        for k in rt:
            r = rt[k]
            if cons:                   # e conservatrice = min des deux mesures
                r *= min(pre[k]['err']['dt2/2']['e'], ref[k]['err']['dt2/2']['e']) \
                     / pre[k]['err']['dt2/2']['e']
            d[k] = float(DP) / r
        return d

    lect = (('machine 1 -- son run a NOYAU', ratios_json(m1n), False),
            ('machine 1 -- son run a LIBM', ratios_json(m1l), False),
            ('machine 2 -- mes ratios', rm, False),
            ('CONSERVATRICE (e = min des deux)', rm, True))
    cons = borne(rm, True)
    return max(cons.values()), max(cons, key=cons.get), lect, borne


R_MOI, R_NOYAU, R_LIBM = ratios_json(PRE), ratios_json(M1N), ratios_json(M1L)

# =====================================================================
print("\n0. D-G2-4 -- LE JSON PORTE-T-IL LA GRANDEUR QUE LE LOG TRONQUE ?")
# =====================================================================
# Mordrait si /ratio_seuil designait une autre grandeur (e/plancher, par exemple) :
# l'identite au bit tomberait, et l'arrondi ne retrouverait pas le journal.
ide = [k for k in PRE
       if BITS(PRE[k]['ratio_seuil'])
       != BITS(PRE[k]['err']['dt2/2']['e'] / PRE[k]['seuil_5_4'])]
chk('ratio_seuil == e(dt2/2) / seuil_5_4 AU BIT (%d/%d)'
    % (len(PRE) - len(ide), len(PRE)), not ide, ','.join(sorted(ide)) or '0 ecart')
arr = [k for k in R_MOI if '%.3f' % R_MOI[k] != '%.3f' % L_MOI[k]]
chk('mon JSON arrondi a 3 dec == mon log (%d/%d)' % (len(R_MOI) - len(arr), len(R_MOI)),
    not arr, ','.join(sorted(arr)) or '0 ecart')
arn = [k for k in R_NOYAU if '%.3f' % R_NOYAU[k] != '%.3f' % L_ELLE[k]]
chk('son JSON NOYAU arrondi a 3 dec == son log du 28/08 (%d/%d)'
    % (len(R_NOYAU) - len(arn), len(R_NOYAU)), not arn, ','.join(sorted(arn)) or '0 ecart')
print('   porteur 7|1.73 :  log %.3f  ->  JSON %.17g' % (L_MOI['7|1.73'], R_MOI['7|1.73']))

# =====================================================================
print("\n1. LE PLANCHER VA-T-IL EN 1/delta ? -- forme fermee contre R MESURE")
# =====================================================================
pires = []
for k in sorted(PRE):
    p, w2 = int(k.split('|')[0]), float(k.split('|')[1])
    a, tc = float(AL[p]), PRE[k]['tau_CAP']
    Rf = 2 * a * (a + 1) / ((w2 * w2 - 1) * tc * tc)      # v11, D-t-22
    pires.append(abs(PRE[k]['R_composantes'] - Rf) / Rf)
chk('R mesure == forme fermee aux 9 points', max(pires) < 1e-4,
    'ecart max %.2e ; tau_CAP ~ sqrt(delta) -> R ~ 1/delta' % max(pires))

# =====================================================================
print("\n2. L'ERREUR e EST-ELLE INVARIANTE EN delta ? -- deux runs, x1024")
# =====================================================================
rap = {k: PRE[k]['err']['dt2/2']['e'] / REF[k]['err']['dt2/2']['e'] for k in sorted(PRE)}
lo, hi = min(rap.values()), max(rap.values())
chk('e(delta-prime)/e(delta_0) dans [0.8, 1.25] pour delta x1024',
    0.8 < lo and hi < 1.25,
    'mesure [%.4f, %.4f] ; la dispersion fixe la marge' % (lo, hi))
chk('donc ratio = e/(C x plancher) est PROPORTIONNEL a delta', True,
    'consequence des sections 1 et 2')

# =====================================================================
print("\n3. BORNE SUPERIEURE -- volet A (exacte, aucune extrapolation)")
# =====================================================================
SUP = {}
for m in (1, 2, 3):
    b = min(DISP[p] / m * float((AL[p] + 2) * (AL[p] + 3)) for p in (4, 5, 7))
    q = min(((DISP[p] / m * float((AL[p] + 2) * (AL[p] + 3))), p) for p in (4, 5, 7))[1]
    SUP[m] = b
    print('   m=%d : delta <= %.9e   (portee par p=%d)' % (m, b, q))

# =====================================================================
print("\n4. BORNE INFERIEURE -- volet T (quatre lectures, la plus dure retenue)")
# =====================================================================
INF, PORTEUR, LECT, borne = derive(PRE, REF, M1N, M1L)
INF_V1 = derive(PRE, REF, M1N, M1L, ratios_moi=L_MOI)[0]   # ce que la v1 rendait

for etq, rt, cons in LECT:
    d = borne(rt, cons)
    k = max(d, key=d.get)
    print('   %-34s delta >= %.9e  (x%.4f)  porte par %s'
          % (etq, d[k], d[k] / float(DP), k))
chk('la borne est portee par le MEME point dans les 4 lectures',
    all(max(borne(r, c), key=borne(r, c).get) == PORTEUR for _, r, c in LECT), PORTEUR)
print('   RETENUE : INF = %.9e   (v1, depuis le log : %.9e)' % (INF, INF_V1))

# =====================================================================
print("\n5. D-G2-4 -- CE QUE LA CORRECTION DEPLACE, ET CE QU'ELLE NE DEPLACE PAS")
# =====================================================================
ecart = abs(INF - INF_V1) / INF
marge = SUP[2] / INF - 1.0
chk('l ecart JSON/log est DEUX ORDRES sous la marge de la fenetre', ecart < marge / 100,
    'ecart %.4e  marge %.4e  rapport %.1f' % (ecart, marge, marge / ecart))


def carte(inf):
    return {(kT, m): ('VIDE' if kT * inf > SUP[m] else 'x%.4f' % (SUP[m] / (kT * inf)))
            for kT in (1.00, 1.15, 1.30, 1.50, 1.74) for m in (1, 2, 3)}


c1, c2 = carte(INF_V1), carte(INF)
chg = sorted('kT=%.2f,m=%d' % c for c in c1 if (c1[c] == 'VIDE') != (c2[c] == 'VIDE'))
chk('aucune des 15 cellules de la carte ne change de statut', not chg,
    ','.join(chg) or '0 changement')
print('\n   m  = marge volet A (plancher <= disp/m) ; kT = marge volet T (ratio >= kT)')
print('   D-t-25 a MESURE b = 1.15 a 1.74 x plancher_comp : le critere est')
print('   une CONDITION NECESSAIRE, donc kT = 1 est le cas le plus permissif.\n')
print('   %-5s | %s' % ('kT', '  '.join('%8s' % ('m=%d' % m) for m in (1, 2, 3))))
for kT in (1.00, 1.15, 1.30, 1.50, 1.74):
    print('   %-5.2f | %s' % (kT, '  '.join('%8s' % c2[(kT, m)] for m in (1, 2, 3))))

# =====================================================================
print("\n6. LA BORNE RETENUE LIT-ELLE UN NOMBRE DE MACHINE 1 ? -- jambe de MUTATION")
# =====================================================================
# On ne mute pas la variable au site d'appel (ce serait un controle vide) : on mute
# les DEUX JSON qui entrent dans `derive`, et on relit la borne a la sortie.
def mute(d, f):
    """Copie mutee et COHERENTE : e x f, ratio_seuil x f, seuil inchange."""
    m = copy.deepcopy(d)
    for k in m:
        m[k]['ratio_seuil'] *= f
        for s in m[k]['err']:
            m[k]['err'][s]['e'] *= f
    return m


MN3, ML5 = mute(M1N, 3.0), mute(M1L, 0.5)
INF_MUT, PORT_MUT, LECT_MUT, borne_mut = derive(PRE, REF, MN3, ML5)
chk('INF INCHANGE AU BIT quand ses DEUX JSON entrent mutes (x3, x0.5)',
    BITS(INF_MUT) == BITS(INF), '%s / %s' % (BITS(INF), BITS(INF_MUT)))
chk('le PORTEUR est inchange sous la meme mutation', PORT_MUT == PORTEUR,
    '%s / %s' % (PORTEUR, PORT_MUT))
# Sans ce troisieme controle la jambe ne prouverait rien : une mutation qui ne
# deplace aucune lecture de machine 1 rendrait les deux premiers vrais pour rien.
recu = max(borne(R_NOYAU, False).values())
mute_ = max(borne_mut(ratios_json(MN3), False).values())
chk('la mutation DEPLACE bien la lecture affichee de machine 1',
    BITS(recu) != BITS(mute_), 'recu %.9e -> mute %.9e' % (recu, mute_))

# =====================================================================
print('\n7. L\'ERRATUM DU "SEUL POINT" -- EN CONDITION, PLUS EN DETAIL')
# =====================================================================
# CONSTAT NEUF DE LA v2, ET C'EST UNE DEUXIEME INSTANCE DE D-G2-4. L'erratum du
# geste (2) compte TROIS cellules divergentes. Ce compte est juste A LA RESOLUTION
# DU LOG, ou il a ete etabli. AU BIT elles sont SIX : trois grossieres (> 1e-2, les
# basculements visibles du noyau) et trois fines (< 1e-7), invisibles a 3 decimales.
# Le compte de l'erratum heritait donc de la meme troncature que la borne.
dif_n = sorted(k for k in R_MOI if BITS(R_MOI[k]) != BITS(R_NOYAU[k]))
dif_l = sorted(k for k in R_MOI if BITS(R_MOI[k]) != BITS(R_LIBM[k]))
dif_3 = sorted(k for k in R_MOI if '%.3f' % R_MOI[k] != '%.3f' % R_NOYAU[k])
rel = lambda k: abs(R_NOYAU[k] - R_MOI[k]) / R_MOI[k]

chk('AU BIT, mes ratios different de son NOYAU sur 6 cellules', len(dif_n) == 6,
    ','.join(dif_n))
chk('A 3 DECIMALES ils different sur 3 -- le compte de l erratum', len(dif_3) == 3,
    ','.join(dif_3))
chk('mes ratios == son LIBM AU BIT (%d/%d)' % (len(R_MOI) - len(dif_l), len(R_MOI)),
    not dif_l, ','.join(dif_l) or '0 ecart')
for k in dif_n:
    print('   %-8s moi %.17g   noyau %.17g   (%.1e)  %s'
          % (k, R_MOI[k], R_NOYAU[k], rel(k), PRE[k]['W_plancher']))

gros = sorted(k for k in dif_n if rel(k) > 1e-2)
fins = sorted(k for k in dif_n if rel(k) < 1e-7)
chk('la separation gros/fin est NETTE : aucune cellule entre 1e-7 et 1e-2',
    sorted(gros + fins) == dif_n, 'gros %d  fin %d  total %d'
    % (len(gros), len(fins), len(dif_n)))
chk('les 3 GROSSIERES sont celles que le log rendait visibles', gros == dif_3,
    ','.join(gros))
lues_g = sorted(k for k in gros if PRE[k]['W_plancher'] != 'MORD')
lues_b = sorted(k for k in dif_n if PRE[k]['W_plancher'] != 'MORD')
chk('parmi les 3 GROSSIERES, 2 sont LUES au pre-vol', len(lues_g) == 2, ','.join(lues_g))
chk('parmi les 6 AU BIT, 4 sont LUES au pre-vol', len(lues_b) == 4, ','.join(lues_b))
chk('le PORTEUR est la seule GROSSIERE qui ne soit PAS lue',
    PORTEUR in gros and PORTEUR not in lues_g, PORTEUR)

# =====================================================================
print("\n8. LA PORTE -- le reglage courant est-il dans la fenetre ?")
# =====================================================================
chk('delta-prime = %.9e est SOUS la borne inferieure' % float(DP), float(DP) < INF,
    'delta-prime / INF = %.4f' % (float(DP) / INF))

n, k = len(OK), sum(1 for _, o in OK if o)
print('\n=====================================================================')
print('BILAN : %d/%d controles PASSENT' % (k, n))
print('borne inf (conservatrice, JSON) %.9e   borne sup (m=2) %.9e' % (INF, SUP[2]))
print('fenetre a m=2, kT=1 : %s     porteur : %s' % (c2[(1.00, 2)], PORTEUR))
print('=====================================================================')
