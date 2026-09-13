#!/usr/bin/env python3
# -*- coding: ascii -*-
"""CONSTRUCTION DU GEL constante A v6 ET DU BANC v9 -- machine 1, v1, 12/09/2026 (nuit).

v6 = v5 (2c0d2dc86054838c, REMPLACEE, non editee) + hunks ENUMERES ci-dessous, appliques par
remplacement a ancre UNIQUE (src.count(ancre) == 1, sinon arret : aucune substitution muette,
candidate 5 de nn.8 du delta 90). Le banc v9 = v8 (4d8882a2223a5c74, CERTIFIE, non edite) +
les remplacements qui portent le nouveau reglage. Les tables 4.3-4.6 sont DERIVEES ici
(regle 13), depuis delta' et les constantes pures du v5 (r = 1/10, M = 20, k = 2, dt_1 = 0.006),
A_p repris de TABLES_GEL_ALPHA du banc v8 (source : run 85), g = 0.05 repris du controle
de debordement du v5. Chemins en arguments : <v5.md> <banc_v8.py> <repertoire de sortie>.
"""
import hashlib, math, os, sys, unicodedata
from fractions import Fraction as F

V5, V8, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(OUT, exist_ok=True)


def canon(p):
    raw = open(p, 'rb').read()
    t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
    return hashlib.sha256(t).hexdigest()[:16]


assert canon(V5) == '2c0d2dc86054838c', canon(V5)
assert canon(V8) == '4d8882a2223a5c74', canon(V8)

# ---------------------------------------------------------------- LE REGLAGE v6, DERIVE
INF = 1.659260768e-05                     # tenaille v3 4353c80e60cef87c, borne inferieure (volet T)
DISP = {4: 1.97714978966701e-06, 5: 2.393510486697892e-06, 7: 7.43220491195018e-06}   # run 85, /degres/p/dispersion_lnA
AL = {4: F(2), 5: F(4, 3), 7: F(4, 5)}
N_DESC = int(sys.argv[4]) if len(sys.argv) > 4 else 21   # nombre pur de conception : delta' = delta_0 / N_DESC^2 (argument optionnel, scan du pre-vol)
D0 = F(1, 100)
DP = D0 / N_DESC ** 2                     # 1/40000
SUP1 = min(DISP[p] * float((AL[p] + 2) * (AL[p] + 3)) for p in (4, 5, 7))   # volet A a m = 1
kT = float(DP) / INF
m = SUP1 / float(DP)
plancher = {p: DP / ((AL[p] + 2) * (AL[p] + 3)) for p in (4, 5, 7)}
ratio = {p: float(plancher[p]) / DISP[p] for p in (4, 5, 7)}
r, M, k, dt1 = F(1, 10), 20, 2, 0.006
W2 = (1.73, 2.27, 2.80)
tau_dom = {w: math.sqrt(float(DP) / (1 + w * w)) for w in W2}
tau_cap = {w: float(r) * tau_dom[w] for w in W2}
dt2a = {w: k * tau_dom[w] / M for w in W2}
dt2b = {w: tau_cap[w] / M for w in W2}
# A_p par inversion de la table 4.4 du v5 (bascule 2b a w2 = 1.73, k tau_dom'(v5) = 3.127778e-03)
A = {4: 48.98979, 5: 9.65048, 7: 3.14244}   # A_p du gel (TABLES_GEL_ALPHA["A"] du banc v8, source run 85), tels que le v8 les tape
basc = {(p, w): A[p] * (k * tau_dom[w]) ** (-float(AL[p])) for p in (4, 5, 7) for w in W2}
cap = {(p, w): A[p] * tau_cap[w] ** (-float(AL[p])) for p in (4, 5, 7) for w in W2}
g = 0.05
deb = max((g * cap[(p, w)] ** (p - 1), p, w) for p in (4, 5, 7) for w in W2)
n2a = M * (N_DESC - 1)
bornes = {w: (n2a - math.ceil(dt1 / dt2a[w]), n2a + 1) for w in W2}
DELTA_FALLBACK_T = D0 / 18 ** 2           # porte T en branche 4 -> n = 18
DELTA_FALLBACK_A = D0 / 22 ** 2           # G-plancher mord (3b) -> n = 22

# ---------------------------------------------------------------- LES HUNKS DU GEL
H = []


def rep(s, old, new, nom):
    n = s.count(old)
    assert n == 1, 'ancre %s : %d occurrence(s)' % (nom, n)
    H.append(nom)
    return s.replace(old, new)


import re as _re
s = open(V5, encoding='utf-8').read()
n1024 = len(_re.findall(r'1/1024(?!\d)', s))
s = _re.sub(r'1/1024(?!\d)', '1/%d' % (N_DESC * N_DESC), s)
n9766 = s.count('9.766e-04') + s.count('9.7656e-04')
s = s.replace('9.766e-04', '%.3e' % float(DP / D0)).replace('9.7656e-04', '%.4e' % float(DP / D0))
H.append('H5f 1/1024 -> 1/%d (%d occurrences, frontiere de mot) et 9.766e-04 -> %.3e (%d)' % (N_DESC * N_DESC, n1024, float(DP / D0), n9766))
old_head = s[:s.index('# Banc de verification (N-69')]
new_head = """# PRE-ENREGISTREMENT constante A v6 -- LA FENETRE DESCEND JUSQU'A CE QUE
# L'INSTRUMENT, ET NON LE MODELE, FIXE LA TOLERANCE DE P-A ; LE REGLAGE EST
# PRIS DANS LA FENETRE DE LA TENAILLE, LA OU LE VOLET T LIT ET OU LE VOLET A MESURE
# BROUILLON MACHINE 1 -- DEVIENT GEL A LA CERTIFICATION MACHINE 2
# v6 = v5 (2c0d2dc86054838c, 31722 o, CERTIFIEE 104/104 par machine 2, REMPLACEE, non
# editee) + les hunks enumeres par construction_gel_v6_et_banc_v9_machine1_v1.py :
#   H1  section 3 : delta' n'est plus delta_0 / 4^5 = 1/102400 -- ce reglage est SOUS la
#       borne inferieure de la tenaille (INF = 1.659260768e-05, derivation v3
#       4353c80e60cef87c, reproduite au bit par les deux machines) et le pre-vol du v8 y
#       rend branche 4 des deux cotes (4 des 9 points de T-2 non lus). Descente declaree
#       delta' = delta_0 / n^2 avec n = %d : delta' = %s = %.6e, DANS la fenetre --
#       marge T kT = delta'/INF = %.4f, marge A m = %.4f (delta 90, nn.4 : les deux
#       marges pleines sont impossibles ; ni l'une ni l'autre n'est pleine ici, les deux
#       sont > 1) ; n est CHOISI PAR LE PRE-VOL (balayage de l'echelle, 3.2), pas a la
#       main : trois machoires, W-plancher, W-pas et le plancher du volet A.
#       Cascade de reglage PRE-ENREGISTREE en 3.5.
#   H2  tables 4.1, 4.3, 4.4, 4.5, 4.6 re-derivees au reglage v6 ; 4.7 : n_2s se re-derive
#       au pre-vol v9 par la formule inchangee.
#   H3  section 5 : la porte porte le temoin v11 (a2e7ef3e237c5acf, certifie
#       7fc5f2412b99ad50) et son erratum 7 (i) (13601ef21efdc024) ; l'instrument est le v9,
#       re-parametre depuis le v8 CERTIFIE (4d8882a2223a5c74, 2a618ffb180ea568) ; la
#       tolerance du 9bis entre machines est dite EN ULP pour les cles de classe
#       EXPOSEE-LIBM ; la ligne de plateforme de tout journal de run porte le temoin
#       d'arrondi executable.
#   H4  LD-16 re-ancree : c_pl = 10 est un parametre du reglage depose (run 85,
#       /reglage/c_pl), pas une clause de 5.4.
#   H5  sections 6, 7, 10, 12, 13 mises au reglage v6 et aux pieces du delta 90.
# Aucun autre nombre de fond ne change ; delta'/delta_0 passe de 1/1024 a 1/%d partout (section 9 comprise).
""" % (N_DESC, DP, float(DP), kT, m, N_DESC * N_DESC)
s = rep(s, old_head, new_head, 'H0 en-tete')
s = rep(s, "descend la fenetre (delta' = 1/102400, soit 1/%d de la fenetre du 85)" % (N_DESC * N_DESC),
        "descend la fenetre (delta' = %s, soit 1/%d de la fenetre du 85 ; le v5\ndescendait a 1/102400, SOUS la porte du volet T, section 3)" % (DP, N_DESC * N_DESC), 'H1a section 0')

i0 = s.index("3. LA DERIVATION DE delta' (regle 13 : en forme derivee)")
i1 = s.index("= les planchers de 3.3. Aucun autre nombre.\n") + len("= les planchers de 3.3. Aucun autre nombre.\n")
BAL = open(os.path.join(OUT, 'balayage_resume.txt')).read().rstrip('\n') if os.path.exists(os.path.join(OUT, 'balayage_resume.txt')) else '    (balayage : feuille jointe au lot)'
sec3 = """3. LA DERIVATION DE delta' (regle 13 : en forme derivee) -- TROIS MACHOIRES
=======================================================================

3.1 Trois conditions de conception. Le v5 n'en ecrivait qu'une :

    (A) plancher'(p) = delta' / ((alpha_p + 2)(alpha_p + 3))
                    <= dispersion_lnA_85(p) / m,  m >= 1, pour CHAQUE p   (volet A)
    (T) W-plancher lit aux neuf points de T-2 : e/seuil >= 1 partout, et
        e/seuil >= 1.15 (besoin mesure D-t-25) ; en forme derivee, delta' >=
        kT x INF, INF = 1.659260768e-05 (tenaille, delta 90 nn.4)      (volet T)
    (O) W-pas lit aux neuf points : |p_obs - 4| <= tol_ordre(p) (v11, 7 (i))

(T) et (O) tirent en sens contraires de (A) : le ratio e/seuil est
proportionnel a delta (le plancher de compensation va en 1/delta, e est
invariante a la dispersion pres) ; l'ordre observe se degrade quand dt_2b
grossit, et dt_2b va en sqrt(delta). Au reglage du v5 (1/102400) le
pre-vol du v8 rend branche 4 des deux cotes (W-plancher MORD a 5|1.73,
7|1.73, 7|2.27, 7|2.80). Aucune des trois machoires ne se derive sur le
papier au dixieme pres : (O) FLUCTUE avec la grille d'un n a l'autre. Le
reglage se prend donc AU PRE-VOL, sur l'echelle entiere.

3.2 Descente declaree : delta' = delta_0 / n^2, delta_0 = 1/100, n entier
(le compte nominal 4.6 reste entier : M(n - 1)). REGLE DE CHOIX, declaree
avant le balayage : n est le PLUS GRAND entier de l'echelle (le plus petit
delta', donc la plus grande marge du volet A) tel que le pre-vol du temoin
rende branche 5 avec e/seuil >= 1.15 aux neuf points. Aucune valeur de A
n'entre dans ce choix : le pre-vol est une mesure d'instrument. Balayage
sur machine 1 (levier X86_V4, arithmetique de BOCAL4 au bit) :

%s

3.3 Resultat (Fraction, regle 15) :

    **n = %d    delta' = %s = %.6e    delta'/delta_0 = 1/%d**
    kT = delta'/INF = %.4f  (D-t-25 a mesure le besoin du volet T entre
                            1.15 et 1.74) ; m = SUP(1)/delta' = %.4f
    SUP(1) = min_p disp_85(p)(alpha_p+2)(alpha_p+3) = %.9e (p = 5)

    p    plancher'(p) exact      plancher'(p)      plancher'/disp_85
    4    %-22s  %.6e     %.4f
    5    %-22s  %.6e     %.4f
    7    %-22s  %.6e     %.4f

Les trois planchers tiennent SOUS les dispersions du 85 (m > 1 aux trois
degres) : si la dispersion du present run reste a son niveau, c'est
l'instrument qui fixe tol_lnA -- la porte de la section 7 en decide, sur
les grandeurs du run. Le v5 (n = 32) donnait kT = 0.59 : hors fenetre.

3.4 PRECISION (D-alpha-9 transposee) : a tau_dom', le terme neglige
vaut AU PLUS delta' fois le terme dominant ; le rapport exact est
delta'/((alpha+2)(alpha+3)) = les planchers de 3.3. Aucun autre nombre.

3.5 CASCADE DE REGLAGE, PRE-ENREGISTREE (aucun reglage ne se choisit
apres avoir vu une valeur ; les branches se declenchent sur un VERDICT DE
PORTE, jamais sur A) :
    porte T en branche 4 sur BOCAL4 au reglage v6  ->  v7 au plus grand n
        du balayage inferieur a %d qui rende branche 5 sur BOCAL4 (le
        balayage est alors rejoue sur BOCAL4, meme feuille, meme regle) ;
    G-plancher MORD (branche 3b) au reglage v6  ->  aucun delta' plus petit
        ne passe la porte sur cette echelle (n = %d et n = 24 mordent) :
        la mesure de A exige un instrument plus fin a p = 7 (v10 : dt_2b
        plus petit ou compensation du plancher), arbitrage de l'operateur.
    Un seul pas de cascade par run ; au-dela, arbitrage de l'operateur.
""" % (BAL, N_DESC, DP, float(DP), N_DESC * N_DESC, kT, m, SUP1,
       str(plancher[4]), float(plancher[4]), ratio[4], str(plancher[5]), float(plancher[5]), ratio[5],
       str(plancher[7]), float(plancher[7]), ratio[7], N_DESC, N_DESC + 1)
s = s[:i0] + sec3 + s[i1:]; H.append('H1 section 3')

s = rep(s, "fenetre tombe a tau = k tau_dom' = 3.128e-03 / 2.520e-03 / 2.102e-03",
        "fenetre tombe a tau = k tau_dom' = %.3e / %.3e / %.3e" % tuple(k * tau_dom[w] for w in W2), 'H2a 4.1')
s = rep(s, """    1.73    1.563889e-03   1.563889e-04   1.563889e-04   7.819443e-06
    2.27    1.259825e-03   1.259825e-04   1.259825e-04   6.299123e-06
    2.80    1.051051e-03   1.051051e-04   1.051051e-04   5.255256e-06""",
        '\n'.join('    %.2f    %.6e   %.6e   %.6e   %.6e' % (w, tau_dom[w], tau_cap[w], dt2a[w], dt2b[w]) for w in W2), 'H2b 4.3')
s = rep(s, """    p = 4        5.0077e+06    7.7166e+06    1.1087e+07
    p = 5        2.1098e+04    2.8147e+04    3.5838e+04
    p = 7        3.1701e+02    3.7687e+02    4.3566e+02""",
        '\n'.join('    p = %d        %s' % (p, '    '.join('%.4e' % basc[(p, w)] for w in W2)) for p in (4, 5, 7)), 'H2c 4.4')
s = rep(s, """    p = 4        2.0031e+09    3.0866e+09    4.4346e+09
    p = 5        1.1454e+06    1.5280e+06    1.9456e+06
    p = 7        3.4826e+03    4.1402e+03    4.7859e+03""",
        '\n'.join('    p = %d        %s' % (p, '    '.join('%.4e' % cap[(p, w)] for w in W2)) for p in (4, 5, 7)), 'H2d 4.5')
s = rep(s, "max g |x|^(p-1) au CAP' = 4.361e+27\n    (p = 4, w2 = 2.80)", "max g |x|^(p-1) au CAP' = %.3e\n    (p = %d, w2 = %.2f)" % deb, 'H2e debordement')
s = rep(s, "n_2a nominal = M (sqrt(delta_0/delta') - 1) = 20 x 31 = 620", "n_2a nominal = M (sqrt(delta_0/delta') - 1) = 20 x %d = %d" % (N_DESC - 1, n2a), 'H2f n_2a')
s = rep(s, """    n_2a dans [ 620 - ceil(dt_1/dt_2a(w2)) , 621 ]
         soit [581, 621] / [572, 621] / [562, 621]   (w2 = 1.73/2.27/2.80)""",
        "    n_2a dans [ %d - ceil(dt_1/dt_2a(w2)) , %d ]\n         soit %s   (w2 = 1.73/2.27/2.80)" % (n2a, n2a + 1, ' / '.join('[%d, %d]' % bornes[w] for w in W2)), 'H2g bornes')
s = rep(s, "Cout nominal de la descente : ~1000 pas par serie sur-seuil", "Cout nominal de la descente : ~%d pas par serie sur-seuil" % (n2a + 380), 'H2h cout')
T_MAX = 400.0
tau_dom_0 = {w: math.sqrt(float(D0) / (1 + w * w)) for w in W2}
n2s = {}
for w in W2:
    depart_2s = T_MAX - k * tau_dom_0[w]
    t_start = math.floor(depart_2s / dt1) * dt1
    n2s[w] = math.ceil((T_MAX - k * tau_dom[w] - t_start) / (k * tau_dom[w] / M))
ret = {w: math.ceil(dt1 / dt2a[w]) for w in W2}
s = rep(s, "n_2s = 658 / 631 / 646 -- elles se VERIFIENT au run",
        "n_2s = %d / %d / %d (formule ci-dessous, au reglage v6 ; le v5 donnait\n658 / 631 / 646 a 1/102400) -- elles se VERIFIENT au run" % tuple(n2s[w] for w in W2), 'H2i n_2s')
s = rep(s, "    620 <= n_2s <= 620 + ceil(dt_1/dt_2a(w2))\n    soit [620, 659] / [620, 668] / [620, 678]    (w2 = 1.73/2.27/2.80)",
        "    %d <= n_2s <= %d + ceil(dt_1/dt_2a(w2))\n    soit %s    (w2 = 1.73/2.27/2.80)" % (n2a, n2a, ' / '.join('[%d, %d]' % (n2a, n2a + ret[w]) for w in W2)), 'H2j intervalles 4.7')
s = rep(s, "-- son compte n'est PAS 620 :", "-- son compte n'est PAS %d :" % n2a, 'H2k')

s = rep(s, "5. LA PORTE DE QUALIFICATION (D-alpha-7 transposee) -- SUR LE TEMOIN\n   v9, CERTIFIE",
        "5. LA PORTE DE QUALIFICATION (D-alpha-7 transposee) -- SUR LE TEMOIN\n   v11, CERTIFIE, AVEC SON ERRATUM 7 (i) ; INSTRUMENT v9", 'H3a titre 5')
i0 = s.index("L'histoire, en une ligne, empreintes a l'appui :")
i1 = s.index("CE QUE LA PORTE EXIGEAIT, LA v9 LE PORTE")
s = s[:i0] + """L'histoire, empreintes a l'appui : la v9 du temoin (403488b4f6c319e9,
certifiee b5da74783e5f97c6) a ete SUPERSEDEE par la v11 (a2e7ef3e237c5acf,
certifiee par machine 1 7fc5f2412b99ad50), completee sans edition par
l'erratum de tolerance a sa clause 7 (i) (13601ef21efdc024) ; le depot 9bis
(c4310e33da6b9759) vaut CLOS avec elle ; l'enumeration N-70 v2 des cles du
pre-vol (4867dffe3392dea6) est contresignee au bit sur machine adverse.
L'instrument est passe du v4 au v8 CERTIFIE (4d8882a2223a5c74, selftest
103/103, note 2a618ffb180ea568) ; le v9 de la section 10 le re-parametre.
Tout cela est au registre depuis le delta 90 (11f86226cf4aa612, e68341f).
LE FAIT QUI COMMANDE CE GEL : le pre-vol du v8 en mode temoin, au reglage
1/102400, rend NON CONCLUANT D'INTEGRATEUR, branche 4, DES DEUX COTES
(0a24121e441cc0c3 BOCAL4 ; c45ac9f59907fbf4 machine 1) -- W-plancher MORD
a 5|1.73, 7|1.73, 7|2.27, 7|2.80. Le reglage v6 (section 3) le remonte
dans la fenetre ; le pre-vol se rejoue au v9, des deux cotes, AVANT tout
run : attendu branche 5, sinon 3.5.

""" + s[i1:]; H.append('H3b histoire de la porte')
s = rep(s, "CE QUE LA PORTE EXIGEAIT, LA v9 LE PORTE", "CE QUE LA PORTE EXIGEAIT, LA v11 LE PORTE (comme la v9 avant elle)", 'H3c')
s = rep(s, "(v9, section 8) : g1 la phase grossiere", "(v11, section 8) : g1 la phase grossiere", 'H3d')
s = rep(s, "LE CONTROLE DE REPRODUCTIBILITE (v9, section 9bis)", "LE CONTROLE DE REPRODUCTIBILITE (v11, section 9bis)", 'H3e')
s = rep(s, "pas comme telle.\n\nAucun run du volet A n'est opposable avant le verdict REGLAGE QUALIFIE\n(ou PASSE) du volet T sous la **v9**, jouee sous LE MEME reglage\n(delta', r, M, k, la regle du pas par etage) et sur le meme instrument\n(v4, du) ;",
        """pas comme telle.

TOLERANCE DU 9bis ENTRE MACHINES, MESUREE AU GESTE (2) (delta 90 nn.5) :
les cles de classe EXPOSEE-LIBM -- les quatre tol_int a appel libm,
tol_ordre et tol_ordre_sur_1 -- se comparent entre machines A 2 ULP
(residuelle glibc/UCRT mesuree a 1 ulp, degre-selective, p = 7) ; toute
autre cle du perimetre au bit, exemptions N-70 comprises ; c'est l'issue
(c) de N-70, prise ici pour ce gel. LA LIGNE DE PLATEFORME de tout journal
de run (pre-vol, temoin, alpha) porte le temoin d'arrondi EXECUTABLE
(1765.6704444885254) ** 6 en tableau numpy, en hexadecimal, plus la version
de numpy et le niveau de dispatch : ...9c6 correctement arrondi (BOCAL4,
libm UCRT ; machine 1 avec NPY_DISABLE_CPU_FEATURES=X86_V4), ...9c5 sous le
noyau SIMD (machine 1 sans levier). Un run joue sous ...9c5 est NON
CONCLUANT D'INSTRUMENT avant toute lecture.

LD-16, RE-ANCREE (decision (i) du delta 90, prise ici pour ce gel) : le
plancher c_pl x eps x N de LD-16 lit c_pl = 10 comme PARAMETRE DU REGLAGE
DEPOSE (run 85, 6d7d23130e9322f8, cle /reglage/c_pl = 10), repris tel quel
au reglage v6 ; la clause 5.4 abrogee par la v11 n'en est plus la source.
Le v9 emet la cle c_pl_ld16_herite comme le v8, sa provenance est celle-ci.

Aucun run du volet A n'est opposable avant le verdict REGLAGE QUALIFIE
(ou PASSE) du volet T sous la **v11 et son erratum 7 (i)**, jouee sous LE
MEME reglage (delta' = %s, r, M, k, la regle du pas par etage) et sur
le meme instrument (v9, du) ;""" % DP, 'H3f 9bis ulp, temoin, LD-16, porte')

i0 = s.index("    delta' = 1/102400   DERIVE en 3 (la derivation est le nombre)")
i1 = s.index("7. LA PORTE DU PLANCHER (G-plancher)")
i1 = s.rindex("====", 0, i1)
s = s[:i0] + """    delta' = %s    DERIVE en 3 (le pre-vol est le nombre, regle 3.2)
    n = %d              choisi par le balayage, jamais tape (3.2)
    kT = %.4f, m = %.4f DERIVES en 3.3 (les marges se mesurent, ne se tapent pas)
    cascade 3.5         pre-enregistree, sur verdict de porte seulement
    r = 1/10, M = 20, k = 2, k' = 4, eta = 1/4, dt_1 = 0.006,
    T_MAX = 400, c_pl = 10   INCHANGES, cites du v5 section 6 et du reglage
                        du run 85 (cle /reglage, 6d7d23130e9322f8)

""" % (DP, N_DESC, kT, m) + s[i1:]; H.append('H5a section 6')
s = rep(s, "degre, passe ou non (v5 10.3) -- attendu de conception : > 3 partout\n(3.3), mais c'est le run qui parle, pas la conception.",
        "degre, passe ou non (v5 10.3) -- attendu de conception : %.2f / %.2f / %.2f\naux p = 4 / 5 / 7 (3.3, m = %.2f au plus contraint), mais c'est le run qui\nparle, pas la conception." % (1 / ratio[4], 1 / ratio[5], 1 / ratio[7], m), 'H5b section 7')
s = rep(s, "10. L'INSTRUMENT v4 -- DU AVANT TOUT RUN\n=======================================================================\n\nPart de banc_qualification_machine1_v3.py (5fae2a8c94cf8685). Prend :",
        """10. L'INSTRUMENT v9 -- DU AVANT TOUT RUN
=======================================================================

Part du v8 CERTIFIE (banc_qualification_machine1_v8.py 4d8882a2223a5c74,
note machine 2 2a618ffb180ea568, selftest 103/103), construit par
construction_gel_v6_et_banc_v9_machine1_v1.py : les seuls remplacements sont
le reglage (DELTA = %s ; B_DESC, M_MARGE, J_DESC = %d, 1, 2 -- la racine
de descente vaut %d, PURE ; le selftest du reglage et ses attentes 3.3, 4.6,
4.7 re-derivees ; les tables du gel ; la cle /reglage/delta du JSON) et les
mentions de 1/102400, 620 et 1/1024 des commentaires ; RIEN d'autre. Toutes les tables se re-derivent de DELTA au chargement, comme au
v8. Le v9 se re-certifie EN ENTIER par machine 2 (selftest, banc qui tue,
NE-JOUE-PAS) et son pre-vol se joue des deux cotes au reglage v6 avant tout
run. Les exigences du v4 ci-dessous restent celles du v9 (elles sont
portees par le v8 depuis le 29/08, neuf defauts D-I leves) :""" % (DP, N_DESC, N_DESC), 'H5c section 10')
s = rep(s, "    (iv)  rien ici ne parle du temps jusqu'a l'explosion (etape 3 de\n          l'horizon) : s'il se derive, il se derive AVANT de se jouer.",
        """    (iv)  rien ici ne parle du temps jusqu'a l'explosion (etape 3 de
          l'horizon) : s'il se derive, il se derive AVANT de se jouer ;
    (v)   delta' est pris dans la fenetre de la tenaille, une grandeur
          d'INSTRUMENT (ratios du pre-vol et dispersion du 85) : aucune
          valeur de A n'entre dans ce choix, et la cascade 3.5 ne se
          declenche que sur un verdict de porte ; l'arbitrage du 29/08
          (une marge, pas les deux) est tranche ici par le balayage,
          n = %d, les deux marges partielles, a la plume de machine 1
          sous veto de l'operateur.""" % N_DESC, 'H5d section 12')
s = rep(s, "-- FIN constante_A_pre_enregistrement_v5 --", """Pieces ajoutees par la v6 (toutes au registre a e68341f, delta 90) :
    constante_A_pre_enregistrement_v5.md              2c0d2dc86054838c  REMPLACEE
    derivation_fenetre_delta_machine2_v3.py / .log    4353c80e60cef87c / f60104c0c3ba7ec4
    temoin_negatif_pre_enregistrement_v11.md          a2e7ef3e237c5acf  GEL DU VOLET T
    erratum_temoin_v11_clause_7i_tolerance_v1.md      13601ef21efdc024
    enumeration_cles_prevol_N70_machine2_v2.md        4867dffe3392dea6
    banc_qualification_machine1_v8.py                 4d8882a2223a5c74  CERTIFIE, REMPLACE PAR LE v9
    m2_v8_prevol_temoin_resultats.json                0a24121e441cc0c3  (pre-vol branche 4, BOCAL4)
    prevol_temoin_v8_machine1.log                     c45ac9f59907fbf4  (pre-vol branche 4, machine 1)
    journal_delta_90_constante_A_v2.md                11f86226cf4aa612  (l'acte qui consigne tout cela)
    banc_qualification_machine1_v9.py et son script de construction : empreintes au manifeste du lot v6

-- FIN constante_A_pre_enregistrement_v6 --""", 'H5e section 13 et FIN')
assert '1/40000' not in s.replace('1/40000    1.507', '') and '9.766e-04' not in s, 'residu de reglage tape'
assert all(c < 128 for c in s.encode()), 'non ASCII'
open(os.path.join(OUT, 'constante_A_pre_enregistrement_v6.md'), 'w', encoding='utf-8', newline='\n').write(s)

# ---------------------------------------------------------------- LE BANC v9
b = open(V8, encoding='utf-8').read()
HB = []


def repb(old, new, nom):
    global b
    n = b.count(old)
    assert n == 1, 'banc, ancre %s : %d' % (nom, n)
    HB.append(nom)
    b = b.replace(old, new)


repb("DE LA CONSTANTE A (delta' = 1/102400)", "DE LA CONSTANTE A (delta' = %s ; v9 = v8 certifie re-parametre au gel v6)" % DP, 'B1 en-tete l.5')
repb("  - delta := delta' = 1/102400 (gel v4, 3 : DERIVE) ; delta_0 = 1/100", "  - delta := delta' = %s (gel v6, 3 : DERIVE de la tenaille) ; delta_0 = 1/100" % DP, 'B2 l.17')
repb("DELTA = Fraction(1, 102400)", "DELTA = Fraction(%d, %d)" % (DP.numerator, DP.denominator), 'B3 DELTA')
repb("B_DESC, M_MARGE, J_DESC = 4, 2, 5", "B_DESC, M_MARGE, J_DESC = %d, 1, 2              # gel v6 3.2 : delta' = delta_0 / %d^2 ; m derive = %.2f > M_MARGE" % (N_DESC, N_DESC, m), 'B4 descente')
repb("    return int(M_PAS * (r - 1))                    # = 620 (v4 4.6)", "    return int(M_PAS * (r - 1))                    # = M (racine - 1) : 380 au v6 (4.6)", 'B5 commentaire 620')
repb('    """v4 4.7 : 620 <= n_2s <= 620 + ceil(dt_1/dt_2a) ; jumelle x2."""', '    """v6 4.7 : n_nominal <= n_2s <= n_nominal + ceil(dt_1/dt_2a), n_nominal = M (racine - 1) ; jumelle x2."""', 'B6 docstring 4.7')
repb('    test("delta\' = 1/102400 et delta_0 = b^J delta\' = 1/100 (EXACT, v4 3)",\n         DELTA == Fraction(1, 102400)', '    test("delta\' = %s et delta_0 = b^J delta\' = 1/100 (EXACT, v6 3)",\n         DELTA == Fraction(%d, %d)' % (DP, DP.numerator, DP.denominator), 'B7 selftest')
repb('"reglage": {"delta": "1/102400"}', '"reglage": {"delta": "%s"}' % DP, 'B8 JSON reglage')
repb('refute R~1, ne confirme pas 1/1024', 'refute R~1, ne confirme pas 1/%d' % (N_DESC * N_DESC), 'B9 L-desc')
repb("D-M17-58, n_2s > 620 SANS morsure", "D-M17-58, n_2s > n_nominal SANS morsure", 'B10 en-tete banc qui tue')
GEL6 = os.path.join(OUT, 'constante_A_pre_enregistrement_v6.md')
repb('GEL_ALPHA = ("gels/constante_A_pre_enregistrement_v4.md", "011c923203fcdaef", 30988)',
     'GEL_ALPHA = ("gels/constante_A_pre_enregistrement_v6.md", "%s", %d)' % (canon(GEL6), os.path.getsize(GEL6)), 'B11 pin du gel v6')
repb("# Gel constante A v4, sections 3 et 6 -- delta' DERIVE", "# Gel constante A v6, sections 3 et 6 -- delta' DERIVE de la tenaille", 'B12 commentaire gel')
i0 = b.index('TABLES_GEL_ALPHA = {'); i1 = b.index('TABLES_GEL_ALPHA_0 = {')
tab = 'TABLES_GEL_ALPHA = {   # gel constante A v6, 4.3 (tau_dom\', dt_2b), 4.4 (bascule 2b), 4.5 (CAP\') -- re-derivees au reglage v6\n'
tab += '    "tau_dom": {%s},\n' % ', '.join('%.2f: "%.4e"' % (w, tau_dom[w]) for w in W2)
tab += '    "dt2": {%s},\n' % ', '.join('%.2f: "%.4e"' % (w, dt2b[w]) for w in W2)
tab += '    "dt2a": {%s},\n' % ', '.join('%.2f: "%.4e"' % (w, dt2a[w]) for w in W2)
tab += '    "CAP": {%s},\n' % ',\n            '.join(', '.join('(%d, %.2f): "%.4e"' % (p, w, cap[(p, w)]) for w in W2) for p in (4, 5, 7))
tab += '    "bascule": {%s},\n' % ',\n                '.join(', '.join('(%d, %.2f): "%.4e"' % (p, w, basc[(p, w)]) for w in W2) for p in (4, 5, 7))
tab += '    "A": {4: "48.98979", 5: "9.65048", 7: "3.14244"},\n}\n'
b = b[:i0] + tab + b[i1:]; HB.append('B13 TABLES_GEL_ALPHA re-derivees (v6)')
# --- les attentes du selftest, typees au v4 dans le v8, re-derivees ici au reglage v6 (gel v6 3.3, 4.6, 4.7)
T_MAX = 400.0
tau_dom_0 = {w: math.sqrt(float(D0) / (1 + w * w)) for w in W2}
n2s = {}
for w in W2:
    depart_2s = T_MAX - k * tau_dom_0[w]
    t_start = math.floor(depart_2s / dt1) * dt1
    depart_2bp = T_MAX - k * tau_dom[w]
    n2s[w] = math.ceil((depart_2bp - t_start) / (k * tau_dom[w] / M))
ret = {w: math.ceil(dt1 / dt2a[w]) for w in W2}
i2s = {w: (n2a, n2a + ret[w]) for w in W2}
n2a_k = M * (4 * N_DESC // 2 - 1)                      # n_2a_nominal_k(K_GARDE = 4) = M (4 racine / k - 1)
pl = {p: str(plancher[p]) for p in (4, 5, 7)}
old_pl = "for p, att in ((4, Fraction(1, 2048000)), (5, Fraction(9, 13312000)), (7, Fraction(1, 1089536))):"
new_pl = "for p, att in ((4, Fraction(%s)), (5, Fraction(%s)), (7, Fraction(%s))):" % tuple(pl[p].replace('/', ', ') for p in (4, 5, 7))
assert b.count(old_pl) == 2; b = b.replace(old_pl, new_pl); HB.append('B14 planchers du selftest (2 boucles)')
b = b.replace("exact (v4 3.3)", "exact (v6 3.3)").replace("exact (v4 3.3, delta')", "exact (v6 3.3, delta')")
repb('test("n_2b\' = M k / r = 400 ; fenetre = 180 ; nominaux 620 / 380 (derives, v4 4.6-4.7)",\n         N_2BP == 400 and N_FENETRE == 180 and n_2a_nominal() == 620 and n_2b_nominal() == 380)',
     'test("n_2b\' = M k / r = 400 ; fenetre = 180 ; nominaux %d / 380 (derives, v6 4.6-4.7)",\n         N_2BP == 400 and N_FENETRE == 180 and n_2a_nominal() == %d and n_2b_nominal() == 380)' % (n2a, n2a), 'B15 nominaux')
repb('test("intervalles 4.6 : n_2a [581,621]/[572,621]/[562,621] ; n_2b [360,381] (derives, entiers)",',
     'test("intervalles 4.6 : n_2a %s ; n_2b [360,381] (derives, entiers)",' % '/'.join('[%d,%d]' % bornes[w] for w in W2), 'B16 label 4.6')
repb('         == [(581, 621), (572, 621), (562, 621)]', '         == [%s]' % ', '.join('(%d, %d)' % bornes[w] for w in W2), 'B17 intervalles 4.6')
repb('         and n_2a_nominal_k(K_GARDE) == 1260)', '         and n_2a_nominal_k(K_GARDE) == %d)' % n2a_k, 'B18 n_2a_k')
repb('test("intervalles 4.7 : n_2s [620,659]/[620,668]/[620,678] ; jumelle 4.8 : bornes x2",',
     'test("intervalles 4.7 : n_2s %s ; jumelle 4.8 : bornes x2",' % '/'.join('[%d,%d]' % i2s[w] for w in W2), 'B19 label 4.7')
repb('         [intervalle_2s(w) for w in W2S] == [(620, 659), (620, 668), (620, 678)]',
     '         [intervalle_2s(w) for w in W2S] == [%s]' % ', '.join('(%d, %d)' % i2s[w] for w in W2), 'B20 intervalles 4.7')
repb('         and [intervalle_2s(w, 2) for w in W2S] == [(1240, 1318), (1240, 1336), (1240, 1356)]',
     '         and [intervalle_2s(w, 2) for w in W2S] == [%s]' % ', '.join('(%d, %d)' % (2 * i2s[w][0], 2 * i2s[w][1]) for w in W2), 'B21 jumelle')
repb('"un 620 asserte ne l\'aurait pas vu"', '"un %d asserte ne l\'aurait pas vu"' % n2a, 'B22 G24')
w0 = W2[0]
repb('scenario("G25 n_2s > 620 SANS morsure : 658 dans [620, 659] a w2=1.73 (un 620 asserte = banc mort)",\n             intervalle_2s(1.73) == (620, 659) and 620 < 658 <= 659 and not (658 == 620),\n             "n_2s derive = 658", gardes=())',
     'scenario("G25 n_2s > %d SANS morsure : %d dans [%d, %d] a w2=1.73 (un %d asserte = banc mort)",\n             intervalle_2s(1.73) == (%d, %d) and %d < %d <= %d and not (%d == %d),\n             "n_2s derive = %d", gardes=())'
     % (n2a, n2s[w0], i2s[w0][0], i2s[w0][1], n2a, i2s[w0][0], i2s[w0][1], n2a, n2s[w0], i2s[w0][1], n2s[w0], n2a, n2s[w0]), 'B23 G25')
repb('VERSION = "banc_qualification_machine1_v8"', 'VERSION = "banc_qualification_machine1_v9"', 'B24 VERSION')
repb('         and intervalle_evenement(n_2a_nominal(), retard_2a(1.73), 2) == (1162, 1242)',
     '         and intervalle_evenement(n_2a_nominal(), retard_2a(1.73), 2) == (%d, %d)' % (2 * bornes[W2[0]][0], 2 * bornes[W2[0]][1]), 'B25 jumelle 2a')
b = b.replace('(v4 4.3)', '(v6 4.3)').replace('(v4 4.4)', '(v6 4.4)').replace('(v4 4.5)', '(v6 4.5)'); HB.append('B26 etiquettes v4 -> v6 des tables')
print('n_2s derives v6 : %s ; intervalles 4.7 : %s ; n_2a_k %d' % (n2s, i2s, n2a_k))
assert all(c < 128 for c in b.encode()), 'banc non ASCII'
open(os.path.join(OUT, 'banc_qualification_machine1_v9.py'), 'w', encoding='utf-8', newline='\n').write(b)
print('GEL v6 : %d hunks : %s' % (len(H), ' ; '.join(H)))
print('BANC v9 : %d remplacements : %s' % (len(HB), ' ; '.join(HB)))
print("reglage v6 : delta' = %s = %.6e ; kT = %.4f ; m = %.4f ; SUP(1) = %.9e ; planchers/disp %s" % (DP, float(DP), kT, m, SUP1, {p: round(ratio[p], 4) for p in ratio}))
print('tables : tau_dom %s ; n_2a %d ; bornes %s ; debordement %.3e' % ({w: '%.6e' % tau_dom[w] for w in W2}, n2a, bornes, deb[0]))
print('canons : v6 %s ; banc v9 %s' % (canon(os.path.join(OUT, 'constante_A_pre_enregistrement_v6.md')), canon(os.path.join(OUT, 'banc_qualification_machine1_v9.py'))))
