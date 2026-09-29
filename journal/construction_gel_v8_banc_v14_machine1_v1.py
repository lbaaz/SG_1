#!/usr/bin/env python3
# -*- coding: ascii -*-
"""CONSTRUCTION DU GEL constante A v8 (depuis le v7 certifie a2b8463372e1f906) ET DU BANC v14
(depuis le v13 certifie 1ac295648490a86c). machine 1, v1, 13/09/2026. Rien n'est edite : les
deux sources sont lues, les deux sorties sont neuves. Tout remplacement a une ancre UNIQUE,
asseree ; les fragments dependant du reglage sont REGENERES aux deux reglages (n = 21 : ancre ;
n = 18 : remplacement) par les memes formules que la construction du v6, jamais tapes.
Usage : <v7.md> <v13.py> <repertoire de sortie> [<JSON Q5 : base des modes libres a n = 21>]
"""
import hashlib, json, math, os, re, sys, unicodedata
from fractions import Fraction as F

V7, V13, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
Q5 = sys.argv[4] if len(sys.argv) > 4 else None
os.makedirs(OUT, exist_ok=True)


def canon(p):
    raw = open(p, 'rb').read()
    return hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()).hexdigest()[:16]


assert canon(V7) == 'a2b8463372e1f906', canon(V7)
assert canon(V13) == '1ac295648490a86c', canon(V13)

# ---------------------------------------------------------------- LE REGLAGE, PARAMETRE PAR n
INF = 1.659260768e-05
DISP = {4: 1.97714978966701e-06, 5: 2.393510486697892e-06, 7: 7.43220491195018e-06}
AL = {4: F(2), 5: F(4, 3), 7: F(4, 5)}
A = {4: 48.98979, 5: 9.65048, 7: 3.14244}
D0, r, M, k, dt1, g, T_MAX = F(1, 100), F(1, 10), 20, 2, 0.006, 0.05, 400.0
W2 = (1.73, 2.27, 2.80)
SUP1 = min(DISP[p] * float((AL[p] + 2) * (AL[p] + 3)) for p in (4, 5, 7))


def R(n):
    """Toutes les grandeurs du reglage delta' = delta_0 / n^2, comme au v6."""
    d = {}
    DP = D0 / n ** 2
    d['n'], d['DP'], d['kT'], d['m'] = n, DP, float(DP) / INF, SUP1 / float(DP)
    d['plancher'] = {p: DP / ((AL[p] + 2) * (AL[p] + 3)) for p in (4, 5, 7)}
    d['ratio'] = {p: float(d['plancher'][p]) / DISP[p] for p in (4, 5, 7)}
    tau_dom = {w: math.sqrt(float(DP) / (1 + w * w)) for w in W2}
    tau_cap = {w: float(r) * tau_dom[w] for w in W2}
    d['tau_dom'], d['tau_cap'] = tau_dom, tau_cap
    d['dt2a'] = {w: k * tau_dom[w] / M for w in W2}
    d['dt2b'] = {w: tau_cap[w] / M for w in W2}
    d['basc'] = {(p, w): A[p] * (k * tau_dom[w]) ** (-float(AL[p])) for p in (4, 5, 7) for w in W2}
    d['cap'] = {(p, w): A[p] * tau_cap[w] ** (-float(AL[p])) for p in (4, 5, 7) for w in W2}
    d['deb'] = max((g * d['cap'][(p, w)] ** (p - 1), p, w) for p in (4, 5, 7) for w in W2)
    d['n2a'] = M * (n - 1)
    d['ret'] = {w: math.ceil(dt1 / d['dt2a'][w]) for w in W2}
    d['bornes'] = {w: (d['n2a'] - d['ret'][w], d['n2a'] + 1) for w in W2}
    tau_dom_0 = {w: math.sqrt(float(D0) / (1 + w * w)) for w in W2}
    n2s = {}
    for w in W2:
        depart_2s = T_MAX - k * tau_dom_0[w]
        t_start = math.floor(depart_2s / dt1) * dt1
        n2s[w] = math.ceil((T_MAX - k * tau_dom[w] - t_start) / (k * tau_dom[w] / M))
    d['n2s'] = n2s
    d['i2s'] = {w: (d['n2a'], d['n2a'] + d['ret'][w]) for w in W2}
    d['n2a_k'] = M * (4 * n // 2 - 1)
    return d


def frags(d):
    """Les fragments de TEXTE du gel qui dependent du reglage, dans le format de la construction v6."""
    n, DP, kT, m, pl, ra = d['n'], d['DP'], d['kT'], d['m'], d['plancher'], d['ratio']
    f = {}
    f['h19'] = "#       delta' = delta_0 / n^2 avec n = %d : delta' = %s = %.6e, DANS la fenetre --" % (n, DP, float(DP))
    f['h20'] = "#       marge T kT = delta'/INF = %.4f, marge A m = %.4f (delta 90, nn.4 : les deux" % (kT, m)
    f['s0'] = "descend la fenetre (delta' = %s, soit 1/%d de la fenetre du 85 ; le v5" % (DP, n * n)
    f['s33a'] = "    **n = %d    delta' = %s = %.6e    delta'/delta_0 = 1/%d**" % (n, DP, float(DP), n * n)
    f['s33b'] = "    kT = delta'/INF = %.4f  (D-t-25 a mesure le besoin du volet T entre" % kT
    f['s33c'] = "                            1.15 et 1.74) ; m = SUP(1)/delta' = %.4f" % m
    f['s33t'] = "\n".join("    %d    %-22s  %.6e     %.4f" % (p, str(pl[p]), float(pl[p]), ra[p]) for p in (4, 5, 7))
    f['s41'] = "fenetre tombe a tau = k tau_dom' = %.3e / %.3e / %.3e" % tuple(k * d['tau_dom'][w] for w in W2)
    f['s43'] = "\n".join("    %.2f    %.6e   %.6e   %.6e   %.6e" % (w, d['tau_dom'][w], d['tau_cap'][w], d['dt2a'][w], d['dt2b'][w]) for w in W2)
    f['s44'] = "\n".join("    p = %d        %s" % (p, "    ".join("%.4e" % d['basc'][(p, w)] for w in W2)) for p in (4, 5, 7))
    f['s45'] = "\n".join("    p = %d        %s" % (p, "    ".join("%.4e" % d['cap'][(p, w)] for w in W2)) for p in (4, 5, 7))
    f['deb'] = "max g |x|^(p-1) au CAP' = %.3e\n    (p = %d, w2 = %.2f)" % d['deb']
    f['n2a'] = "n_2a nominal = M (sqrt(delta_0/delta') - 1) = 20 x %d = %d" % (n - 1, d['n2a'])
    f['bornes'] = "    n_2a dans [ %d - ceil(dt_1/dt_2a(w2)) , %d ]\n         soit %s   (w2 = 1.73/2.27/2.80)" % (
        d['n2a'], d['n2a'] + 1, " / ".join("[%d, %d]" % d['bornes'][w] for w in W2))
    f['cout'] = "Cout nominal de la descente : ~%d pas par serie sur-seuil" % (d['n2a'] + 380)
    f['pas'] = "-- son compte n'est PAS %d :" % d['n2a']
    f['i47'] = "    %d <= n_2s <= %d + ceil(dt_1/dt_2a(w2))\n    soit %s    (w2 = 1.73/2.27/2.80)" % (
        d['n2a'], d['n2a'], " / ".join("[%d, %d]" % (d['n2a'], d['n2a'] + d['ret'][w]) for w in W2))
    f['n2s'] = "n_2s = %d / %d / %d" % tuple(d['n2s'][w] for w in W2)
    f['j2a'] = "    n_2a jumelle : %s" % " / ".join("[%d, %d]" % (2 * d['bornes'][w][0], 2 * d['bornes'][w][1]) for w in W2)
    f['j2s'] = "    n_2s jumelle : %s" % " / ".join("[%d, %d]" % (2 * d['i2s'][w][0], 2 * d['i2s'][w][1]) for w in W2)
    f['s471'] = "MEME reglage (delta' = %s, r, M, k, la regle du pas par etage) et sur" % DP
    f['s6'] = ("    delta' = %s    DERIVE en 3 (le pre-vol est le nombre, regle 3.2)\n"
               "    n = %d              choisi par le balayage, jamais tape (3.2)\n"
               "    kT = %.4f, m = %.4f DERIVES en 3.3 (les marges se mesurent, ne se tapent pas)" % (DP, n, kT, m))
    f['s7'] = "attendu de conception : %.2f / %.2f / %.2f\naux p = 4 / 5 / 7 (3.3, m = %.2f au plus contraint)" % (
        1 / ra[4], 1 / ra[5], 1 / ra[7], m)
    f['s10'] = "le reglage (DELTA = %s ; B_DESC, M_MARGE, J_DESC = %d, 1, 2 -- la racine\nde descente vaut %d, PURE ;" % (DP, n, n)
    f['s12'] = "n = %d, les deux marges partielles, a la plume de machine 1" % n
    f['r2'] = "1/%d" % (n * n)
    f['r2v4'] = "%.4e" % float(DP / D0)
    f['r2v3'] = "%.3e" % float(DP / D0)
    return f


d21, d18 = R(21), R(18)
f21, f18 = frags(d21), frags(d18)

# ---------------------------------------------------------------- LE GEL v8
s = open(V7, encoding='utf-8').read()
H = []


def rep(old, new, nom, count=1):
    global s
    c = s.count(old)
    assert c == count, 'GEL %s : %d occurrence(s) de %r' % (nom, c, old[:60])
    s = s.replace(old, new)
    H.append(nom)


# fragments du reglage, n = 21 -> n = 18
for cle in ('h19', 'h20', 's0', 's33a', 's33b', 's33c', 's33t', 's41', 's43', 's44', 's45', 'deb', 'n2a', 'bornes', 'cout',
            'pas', 'i47', 'n2s', 'j2a', 'j2s', 's471', 's6', 's7', 's10', 's12'):
    rep(f21[cle], f18[cle], 'H2 ' + cle)
rep("(formule ci-dessous, au reglage v6 ; le v5 donnait", "(formule ci-dessous, au reglage v8 ; le v5 donnait", 'H2 n2s texte')
n441 = len(re.findall(r'1/441(?!\d)', s))
s = re.sub(r'1/441(?!\d)', f18['r2'], s); H.append('H2 1/441 -> 1/324 (%d)' % n441)
rep(f21['r2v4'], f18['r2v4'], 'H2 signal 4 dec'); rep(f21['r2v3'], f18['r2v3'], 'H2 signal 3 dec')
# section 9 : les rapports bruit/signal, re-derives au signal 1/324 depuis les bruits de la table
lignes9 = re.findall(r'\n    (\d)    (\d\.\d{4}e-0\d) +(\d+\.\d)x +(\d+\.\d)x +(\d+\.\d)x', s)
assert len(lignes9) == 3, lignes9
for p, bruit, r1, r2, r3 in lignes9:
    b = float(bruit); sig = 1.0 / 324
    old = re.search(r'\n(    %s    %s +%sx +%sx +%sx)' % (p, re.escape(bruit), re.escape(r1), re.escape(r2), re.escape(r3)), s).group(1)
    assert s.count(old) == 1, old
    new = "    %s    %s   %8s   %14s   %17s" % (p, bruit, '%.1fx' % (b / sig), '%.1fx' % (b / sig / math.sqrt(6)), '%.1fx' % (b / sig / math.sqrt(18)))
    s = s.replace(old, new)
# la phrase de synthese de L-desc, re-derivee : "a 8 a 22 fois le bruit" -> bornes des rapports par degre
lo9, hi9 = min(float(x[1]) * 324 for x in lignes9), max(float(x[1]) * 324 for x in lignes9)
old_syn = "**L-desc REFUTE R ~ 1 (structure persistante) a 8 a 22 fois le bruit ;"
assert s.count(old_syn) == 1, 'synthese L-desc'
s = s.replace(old_syn, "**L-desc REFUTE R ~ 1 (structure persistante) a %d a %d fois le bruit ;" % (round(lo9), round(hi9)))
H.append('H2 section 9 : trois lignes de rapports au signal 1/324')

# la regle de choix de n : test d'echelle (3.2)
i0 = s.index("(le compte nominal 4.6 reste entier : M(n - 1)). REGLE DE CHOIX, declaree")
i1 = s.index("3.3 Resultat (Fraction, regle 15) :")
regle = """(le compte nominal 4.6 reste entier : M(n - 1)). REGLE DE CHOIX DU v8 (regle
d'ECHELLE) : ce gel ne mesure pas A, il TESTE le terme du premier ordre par sa
proportionnalite a delta' (5bis) ; n est donc le barreau de LEVIER MAXIMAL -- le
plus petit n -- tel que le pre-vol du temoin rende branche 5 avec e/seuil >= 1.15
aux neuf points SUR LES DEUX MACHINES : n = 18 (balayage machine 1 : e/seuil >=
1.868 ; BOCAL4 : a jouer AVANT tout run). Le levier contre le run 91 (n = 21) est
441/324 = %.4f. La regle du v7 (le plus grand n qui ouvre la porte) valait pour
mesurer A ; elle est suspendue, non abrogee. Aucune valeur de A n'entre dans ce
choix : le balayage (machine 1, levier X86_V4) :

""" % (441 / 324)
tab0 = s.index("    n   delta'", i0)
s = s[:i0] + regle + s[tab0:]; H.append('H1 regle d echelle (3.2)')

# 5bis : les modeles, Richardson a ordre mesure, les deux predictions en aveugle
base = ""
if Q5 and os.path.exists(Q5):
    J = json.load(open(Q5, encoding='utf-8'))
    rows = ["    point          a               c               amplitude       phase (rad)   [base %s, q = 4 suppose]" % canon(Q5)]
    for cle in sorted(J['modes_p7']):
        v = J['modes_p7'][cle]
        rows.append("    %-14s %+.6e   %+.6e   %.6e   %+.4f" % (cle, v['a'], v['c'], v['amplitude'], v['phase']))
    base = "\n".join(rows)
b7, w7 = 2.3, 2.896549671592048
fac = 441 / 324
pred = {p: b * fac for p, b in ((4, 2.5425e-07), (5, 2.6302e-07), (7, 2.3986e-07))}
s5bis = """5bis. LES MODELES D'AJUSTEMENT, RICHARDSON A ORDRE MESURE, ET LES DEUX
      PREDICTIONS EN AVEUGLE (chantier du second ordre, delta 91 nn.5)
=======================================================================

Ce que le second ordre a derive (dossier machine 2 du 13/09, derivation
b70fca94d72822ad rejouee au bit par machine 1 ; Q5 4634a795a008a562, rejoue
sur les deux arithmetiques) et que ce gel PRE-ENREGISTRE :

  (a) le terme du premier ordre : x = A tau^(-alpha) (1 + c1 tau^2 + ...),
      c1 = (1 + w2^2) alpha (alpha+1) / ((p-1) K - P2), P2 = alpha (alpha+1)
      (alpha-1)(alpha-2) ; c1 tau_dom'^2 = delta' x alpha(alpha+1)/((p-1)K - P2)
      ne depend pas de w2 : 1/3, 65/261, 133/795 du plancher 10.3 aux p = 4, 5, 7.
  (b) les modes libres : x = x0 (1 + e tau^beta), (beta-alpha)(beta-alpha-1)
      (beta-alpha-2)(beta-alpha-3) = (p-1) K ; le polynome en m = beta - alpha
      est symetrique par m -> 3 - m, donc la paire complexe a Re beta = alpha +
      3/2 EXACTEMENT : 7/2, 17/6, 23/10 ; frequence en ln tau 4.213075,
      3.492054, 2.896550 (derivation C3). Amplitude et phase LIBRES par point.
  (c) la "dispersion" LD-12 de l'instrument est l'ecart de lnA_II entre les
      grilles (dt_2b, k=2), (dt_2b/2, k=2), (dt_2b, k=4) : de l'erreur
      d'integrateur, que Richardson retire.

MODELES PAR DEGRE, ECRITS AVANT LE RUN, JAMAIS CHOISIS SUR LA SOMME DES CARRES
(F3 de Q5 : a p = 7 une frequence fausse rend un SS plus bas que la vraie) :
  y = ln|x1 + x2| sur la fenetre de point fixe de l'instrument, tau = t* - t,
  s = tau / tau_dom'(w2), t* minimise par l'instrument ;
    M1   y + alpha ln tau - c1 tau^2 = lnA                      (c1 fixe, derive)
    M2   ... = lnA + s^b [a cos(w ln s) + c sin(w ln s)]         (b, w derives)
  p = 4 et p = 5 : M1. p = 7 : M2, avec M2- (w/2) et M2+ (2w) joues comme tests
  negatifs -- M2 doit gagner sur M1 d'un facteur >= 3 sur S(7) et les frequences
  fausses ne doivent pas (Q5 : 57 contre 2.1, sur les deux machines).
  L'ajustement II de l'instrument (sans c1) est CONSERVE : la prediction (a)
  ci-dessous se lit sur lui (R1).

RICHARDSON A ORDRE MESURE : l'instrument v14 joue chaque point a dt_2b, dt_2b/2
et dt_2b/4 (cle G_dt4, series _dt2s4_k2 ; un etage 2b de plus, ~%d pas). Par
point, q = log2((lnA(dt) - lnA(dt/2)) / (lnA(dt/2) - lnA(dt/4))) est MESURE ;
lnA_R = lnA(dt/4) + (lnA(dt/4) - lnA(dt/2)) / (2^q - 1). Un q hors [3, 5] rend
le point NON LU ; q = 4 n'est plus suppose. S(p) = max - min des six lnA_R d'un
degre est la tolerance d'instrument, mesuree AU RUN, jamais tapee (R2).

PREDICTION EN AVEUGLE (a) -- LE BIAIS DU PREMIER ORDRE EST PROPORTIONNEL A delta' :
  lu sur l'ajustement II sans c1, apres Richardson a ordre mesure, contre
  ln(K/g)/(p-2) : pred(p) = biais(91) x 441/324 = %.4e (p = 4), %.4e (p = 5),
  %.4e (p = 7, lisible sous M2 seulement). TIENT au degre si obs_R/pred est dans
  [0.8, 1.2] aux six points ET |obs_R - pred| <= 3 S(p) ; NON sinon. Contre
  "biais constant" l'ecart est 36 pour cent ; contre une loi de modes libres
  delta'^((alpha+3/2)/2), 26 / 15 / 5 pour cent aux p = 4 / 5 / 7 (R3).

PREDICTION EN AVEUGLE (b) -- LE TRANSPORT DES MODES LIBRES A p = 7 : la trajectoire
  est la meme jusqu'a la bascule, donc l'amplitude e du mode libre aussi ; dans la
  fenetre normalisee s les coefficients de M2 se transportent par amplitude x
  (441/324)^(b/2) = %.4f (b = 23/10) et phase - w ln sqrt(441/324) = %.4f rad
  (w = %.6f), point par point, lus sur M2 apres Richardson. Base a n = 21 (lecture_v8 en mode --base
  sur les series BOCAL4 du 91, JSON base_modes_libres_n21, tapee par construction) :
%s
  TIENT au point si l'amplitude transportee est a 20 pour cent et la phase a 0.3
  rad de l'ajustement a n = 18 (l'ecart de grille de Q5, F4, borne les deux) ;
  la lecture rend le compte des six.

CE QUE CES PREDICTIONS NE SONT PAS : une mesure de A (la lecture P-A reste celle
de 10.3, a deux regimes : instrument-limite a p = 4 et 5 -- tolerance S(p) + residu
de Richardson --, et a p = 7 sous M2 ; le second ordre c2 et la puissance de M2
sur d'autres degres restent hors de ce gel). La feuille de lecture qui joue tout
cela est deposee avec ce gel (lecture_v8_machine1_v1.py) et se joue sur les series
que l'instrument depose, par les deux machines.

""" % (4 * 380, pred[4], pred[5], pred[7], fac ** (b7 / 2), -w7 * math.log(math.sqrt(fac)), w7, base or "    (base : cle points du JSON de Q5, a taper par construction)")
i6 = s.index("6. LES NOMBRES")
i6 = s.rindex("====", 0, i6)
s = s[:i6] + s5bis + s[i6:]; H.append('H3 section 5bis')

# section 10 : instrument v14
rep("Part du v8 CERTIFIE (banc_qualification_machine1_v8.py 4d8882a2223a5c74,\nnote machine 2 2a618ffb180ea568, selftest 103/103), construit par\nconstruction_gel_v6_et_banc_v9_machine1_v1.py :",
    "Part du v13 CERTIFIE (banc_qualification_machine1_v13.py 1ac295648490a86c,\ncertification machine 2 24/24 ; v10-v13 : D-v9-1, D-v10-1, D-v11-1, D-v12-1\nlevees), construit par construction_gel_v8_banc_v14_machine1_v1.py -- le meme\nscript que ce gel -- qui ajoute UN etage : la jumelle a dt_2b/4 (cle G_dt4,\nseries _dt2s4_k2, intervalles x4), sans toucher aux verdicts (G-dt lit toujours\ndt contre dt/2) ; et :", 'H4 section 10')
rep("10. L'INSTRUMENT v9 -- DU AVANT TOUT RUN", "10. L'INSTRUMENT v14 -- DU AVANT TOUT RUN", 'H4 titre 10')
rep("Le v9 se re-certifie EN ENTIER par machine 2 (selftest, banc qui tue,\nNE-JOUE-PAS) et son pre-vol se joue des deux cotes au reglage v6 avant tout\nrun.",
    "Le v14 se re-certifie EN ENTIER par machine 2 (selftest, banc qui tue,\nNE-JOUE-PAS) et son pre-vol se joue des deux cotes au reglage v8 avant tout\nrun.", 'H4 v14 certif')
# header du gel
old_head = s[:s.index('# Banc de verification (N-69')]
new_head = """# PRE-ENREGISTREMENT constante A v8 -- LE TERME DU PREMIER ORDRE EST DERIVE ; CE
# GEL LE TESTE EN AVEUGLE PAR SA PROPORTIONNALITE A delta' (n = 18, levier 441/324)
# ET PRE-ENREGISTRE LES MODES LIBRES A p = 7 ; RICHARDSON A ORDRE MESURE
# BROUILLON MACHINE 1 -- DEVIENT GEL A LA CERTIFICATION MACHINE 2
# v8 = v7 (a2b8463372e1f906, CERTIFIEE 114/114 par machine 2 et contresignee par
# machine 1, REMPLACEE, non editee) + les hunks enumeres par
# construction_gel_v8_banc_v14_machine1_v1.py :
#   H1  3.2 : regle d'ECHELLE -- n = 18 (delta' = 1/32400), le barreau de levier
#       maximal qui ouvre la porte (balayage machine 1 ; BOCAL4 a jouer avant tout run) ;
#       la regle du v7 (le plus grand n) est suspendue, ce gel ne mesure pas A.
#   H2  tous les nombres du reglage re-derives a n = 18 (3.3, 4.1, 4.3-4.8, 6, 7, 9,
#       10, 12 ; 1/441 -> 1/324) par les formules de la construction du v6.
#   H3  section 5bis : modeles M1 (p = 4, 5) et M2 (p = 7) a coefficients DERIVES,
#       tests negatifs, Richardson a ordre MESURE (troisieme niveau), et les deux
#       predictions en aveugle (biais x 441/324 ; transport des modes libres).
#   H4  section 10 : instrument v14 = v13 certifie + etage dt_2b/4, meme script.
#   H5  sections 12 et 13 : ce que ce gel ne dit pas ; les pieces du second ordre.
# Aucun nombre de fond du v7 ne change hors le reglage ; la phrase de 9 aux bornes
# non tracees (D-v7-1) est REMPLACEE par une phrase sourcee (H5).
"""
s = s.replace(old_head, new_head); H.append('H0 en-tete')
# D-v7-1 : la phrase de 9 aux bornes non tracees, remplacee par une phrase sourcee
old9 = s[s.index("R ~ 1 sortait, P-A l'aurait deja dit (un biais persistant de 2.2e-04 a"):]
old9 = old9[:old9.index(")") + 1]
new9 = ("R ~ 1 sortait, P-A l'aurait deja dit (un biais persistant de l'ordre des\nplanchers du 85, 5.0e-04 a 9.4e-04 -- cle /degres/p/plancher_lnA du run\n6d7d23130e9322f8 --, creverait une tolerance a ~2e-06)")
rep(old9, new9, 'H5 D-v7-1 phrase de 9 sourcee')
# section 12 : ajout
rep("          n = %d, les deux marges partielles, a la plume de machine 1" % 18,
    "          n = %d, puis suspendu au v8 au profit de la regle d'echelle (3.2)" % 21, 'H5 section 12 (v)')
s = s.replace("-- FIN constante_A_pre_enregistrement_v7 --",
              """Pieces ajoutees par la v8 :
    constante_A_pre_enregistrement_v7.md               a2b8463372e1f906  REMPLACEE
    journal_delta_91_constante_A_run_v2.md             035e19806db14910  (registre 729f9a9)
    banc_qualification_machine1_v13.py                 1ac295648490a86c  CERTIFIE, REMPLACE PAR LE v14
    dossier_conception_second_ordre_machine2_v1.md     (lot machine 2 du 13/09)
    lecture_predeclaree_second_ordre_machine2_v1.md    99080e4822bf0108
    derivation_second_ordre_machine2_v1.py / .json     f0333c0afcf86583 / b70fca94d72822ad
    exploration_richardson_second_ordre_machine2_v1.py 9562f34b1b5d6d4a
    lecture_predeclaree_Q5_modes_libres_machine2_v1.md fc6ca127f8eabc8b
    ajustement_modes_libres_Q5_machine2_v1.py / .json  e7ff0b5664efe1c2 / 4634a795a008a562
    note_machine1_lecture_second_ordre_v1.md           c8390c986806649b
    note_machine1_lecture_Q5_v1.md                     8640542955081128
    banc_qualification_machine1_v14.py, lecture_v8_machine1_v1.py, construction : empreintes au manifeste du lot v8

-- FIN constante_A_pre_enregistrement_v8 --"""); H.append('H5 section 13 et FIN')
assert all(c < 128 for c in s.encode())
GEL = os.path.join(OUT, 'constante_A_pre_enregistrement_v8.md')
open(GEL, 'w', encoding='utf-8', newline='\n').write(s)
print('GEL v8 : %d hunks ; canon %s ; %d octets' % (len(H), canon(GEL), os.path.getsize(GEL)))

# ---------------------------------------------------------------- LE BANC v14
b = open(V13, encoding='utf-8').read()
HB = []


def repb(old, new, nom, count=1):
    global b
    c = b.count(old)
    assert c == count, 'BANC %s : %d occurrence(s) de %r' % (nom, c, old[:60])
    b = b.replace(old, new)
    HB.append(nom)


def attentes(d):
    """Les attentes du selftest, typees au v9 (n = 21) et re-derivees a n = 18."""
    n, DP = d['n'], d['DP']
    a = {}
    a['DELTA'] = "DELTA = Fraction(%d, %d)" % (DP.numerator, DP.denominator)
    a['BJ'] = "B_DESC, M_MARGE, J_DESC = %d, 1, 2              # gel v6 3.2 : delta' = delta_0 / %d^2 ; m derive = %.2f > M_MARGE" % (n, n, d['m'])
    a['pl'] = "for p, att in ((4, Fraction(%s)), (5, Fraction(%s)), (7, Fraction(%s))):" % tuple(str(d['plancher'][p]).replace('/', ', ') for p in (4, 5, 7))
    a['nom'] = '    test("n_2b\' = M k / r = 400 ; fenetre = 180 ; nominaux %d / 380 (derives, v6 4.6-4.7)",\n         N_2BP == 400 and N_FENETRE == 180 and n_2a_nominal() == %d and n_2b_nominal() == 380)' % (d['n2a'], d['n2a'])
    a['l46'] = 'test("intervalles 4.6 : n_2a %s ; n_2b [360,381] (derives, entiers)",' % '/'.join('[%d,%d]' % d['bornes'][w] for w in W2)
    a['i46'] = '         == [%s]' % ', '.join('(%d, %d)' % d['bornes'][w] for w in W2)
    a['n2ak'] = '         and n_2a_nominal_k(K_GARDE) == %d)' % d['n2a_k']
    a['l47'] = 'test("intervalles 4.7 : n_2s %s ; jumelle 4.8 : bornes x2",' % '/'.join('[%d,%d]' % d['i2s'][w] for w in W2)
    a['i47'] = '         [intervalle_2s(w) for w in W2S] == [%s]' % ', '.join('(%d, %d)' % d['i2s'][w] for w in W2)
    a['j47'] = '         and [intervalle_2s(w, 2) for w in W2S] == [%s]' % ', '.join('(%d, %d)' % (2 * d['i2s'][w][0], 2 * d['i2s'][w][1]) for w in W2)
    a['j2a'] = '         and intervalle_evenement(n_2a_nominal(), retard_2a(1.73), 2) == (%d, %d)' % (2 * d['bornes'][W2[0]][0], 2 * d['bornes'][W2[0]][1])
    a['g24'] = '"un %d asserte ne l\'aurait pas vu"' % d['n2a']
    w0 = W2[0]
    a['g25'] = ('scenario("G25 n_2s > %d SANS morsure : %d dans [%d, %d] a w2=1.73 (un %d asserte = banc mort)",\n             intervalle_2s(1.73) == (%d, %d) and %d < %d <= %d and not (%d == %d),\n             "n_2s derive = %d", gardes=())'
                % (d['n2a'], d['n2s'][w0], d['i2s'][w0][0], d['i2s'][w0][1], d['n2a'], d['i2s'][w0][0], d['i2s'][w0][1], d['n2a'], d['n2s'][w0], d['i2s'][w0][1], d['n2s'][w0], d['n2a'], d['n2s'][w0]))
    a['json'] = '"reglage": {"delta": "%s"}' % DP
    a['st'] = '    test("delta\' = %s et delta_0 = b^J delta\' = 1/100 (EXACT, v6 3)",\n         DELTA == Fraction(%d, %d)' % (DP, DP.numerator, DP.denominator)
    a['ldesc'] = 'refute R~1, ne confirme pas 1/%d' % (n * n)
    tab = 'TABLES_GEL_ALPHA = {   # gel constante A v6, 4.3 (tau_dom\', dt_2b), 4.4 (bascule 2b), 4.5 (CAP\') -- re-derivees au reglage v6\n'
    tab += '    "tau_dom": {%s},\n' % ', '.join('%.2f: "%.4e"' % (w, d['tau_dom'][w]) for w in W2)
    tab += '    "dt2": {%s},\n' % ', '.join('%.2f: "%.4e"' % (w, d['dt2b'][w]) for w in W2)
    tab += '    "dt2a": {%s},\n' % ', '.join('%.2f: "%.4e"' % (w, d['dt2a'][w]) for w in W2)
    tab += '    "CAP": {%s},\n' % ',\n            '.join(', '.join('(%d, %.2f): "%.4e"' % (p, w, d['cap'][(p, w)]) for w in W2) for p in (4, 5, 7))
    tab += '    "bascule": {%s},\n' % ',\n                '.join(', '.join('(%d, %.2f): "%.4e"' % (p, w, d['basc'][(p, w)]) for w in W2) for p in (4, 5, 7))
    tab += '    "A": {4: "48.98979", 5: "9.65048", 7: "3.14244"},\n}\n'
    a['tab'] = tab
    return a


a21, a18 = attentes(d21), attentes(d18)
repb(a21['pl'], a18['pl'], 'B1 planchers du selftest (2)', count=2)
for cle in ('DELTA', 'BJ', 'st', 'nom', 'l46', 'i46', 'n2ak', 'l47', 'i47', 'j47', 'j2a', 'g24', 'g25', 'json', 'ldesc', 'tab'):
    repb(a21[cle], a18[cle], 'B1 ' + cle)
repb("DE LA CONSTANTE A (delta' = 1/44100 ;", "DE LA CONSTANTE A (delta' = 1/32400 ; v14 = v13 certifie + etage dt_2b/4 (cle G_dt4), reglage n = 18, pin gel v8,\nconstruction_gel_v8_banc_v14_machine1_v1.py ;", 'B2 en-tete')
repb("  - delta := delta' = 1/44100 (gel v6, 3 : DERIVE de la tenaille) ; delta_0 = 1/100",
     "  - delta := delta' = 1/32400 (gel v8, 3 : regle d'echelle, n = 18) ; delta_0 = 1/100", 'B2 l.17')
repb('GEL_ALPHA = ("gels/constante_A_pre_enregistrement_v7.md", "a2b8463372e1f906", 41061)',
     'GEL_ALPHA = ("gels/constante_A_pre_enregistrement_v8.md", "%s", %d)' % (canon(GEL), os.path.getsize(GEL)), 'B3 pin v8')
repb('VERSION = "banc_qualification_machine1_v13"', 'VERSION = "banc_qualification_machine1_v14"', 'B4 VERSION')
# l'etage dt_2b/4
repb('        JRN("A-%s" % etiquette, "phase 1 sans bascule (%s a t=%.3f) -> G-fen, COMPTE" % (ph1["evenement"], ph1["t"]))\n        return rec\n    fac = 2 if jumelle else 1\n',
     '        JRN("A-%s" % etiquette, "phase 1 sans bascule (%s a t=%.3f) -> G-fen, COMPTE" % (ph1["evenement"], ph1["t"]))\n        return rec\n    fac = jumelle if (isinstance(jumelle, int) and not isinstance(jumelle, bool) and jumelle > 1) else (2 if jumelle else 1)   # v14 : jumelle=4 -> dt/4\n', 'B5 facteur de jumelle')
repb('    plan, gdt, gk, seuil, lignee = {}, {}, {}, {}, {}\n', '    plan, gdt, gk, seuil, lignee, gdt4 = {}, {}, {}, {}, {}, {}   # v14 : troisieme niveau\n', 'B6 dict gdt4 (3 occurrences : run, pre-vol, banc)', count=3)
repb('                gk[cle] = trajectoire_plan(w2, p, s, dt2, K_GARDE, compteur, sortie, "p%d_w%.2f_c%.2f_dt2_k4" % (p, w2, c), synth, sgn=sg)\n',
     '                gk[cle] = trajectoire_plan(w2, p, s, dt2, K_GARDE, compteur, sortie, "p%d_w%.2f_c%.2f_dt2_k4" % (p, w2, c), synth, sgn=sg)\n'
     '                # v14 (gel v8, 5bis) : troisieme niveau dt_2b/4, intervalles x4 ; ne porte aucun verdict de cascade.\n'
     '                gdt4[cle] = trajectoire_plan(w2, p, s, dt2 / 4, K_BASC, compteur, sortie, "p%d_w%.2f_c%.2f_dt2s4_k2" % (p, w2, c), synth, sgn=sg, jumelle=4)\n', 'B7 trajectoire dt/4')
repb('    L = {"plan": plan, "G_dt": gdt, "G_k": gk, "seuil": {},', '    L = {"plan": plan, "G_dt": gdt, "G_k": gk, "G_dt4": gdt4 or {}, "seuil": {},', 'B8 cle G_dt4')
repb('def lire_alpha(plan, gdt, gk, seuil, lignee, e_ln10_max, ref_desc=None):', 'def lire_alpha(plan, gdt, gk, seuil, lignee, e_ln10_max, ref_desc=None, gdt4=None):   # v14', 'B10 signature lire_alpha')
repb('    L.update(lire_alpha(plan, gdt, gk, seuil, lignee, porte["e_sur_ln10_max"], ref_desc=ref_desc))', '    L.update(lire_alpha(plan, gdt, gk, seuil, lignee, porte["e_sur_ln10_max"], ref_desc=ref_desc, gdt4=gdt4))', 'B11 appel du run reel')
# les deux boucles du banc qui tue jouent aussi le troisieme niveau, pour que les comptes attendus restent ceux du run
repb('                    gk[cle] = trajectoire_plan(w2, p, s, dt2, K_GARDE, compteur, None, "s", sy)\n',
     '                    gk[cle] = trajectoire_plan(w2, p, s, dt2, K_GARDE, compteur, None, "s", sy)\n'
     '                    gdt4[cle] = trajectoire_plan(w2, p, s, dt2 / 4, K_BASC, compteur, None, "s", sy, jumelle=4)   # v14\n', 'B12 banc synthetique : dt/4')
repb('                    gk[cle] = trajectoire_plan(w2, p, s, dt2, K_GARDE, compteur, sortie_s, "b_p%d_w%.2f_c%.2f_c" % (p, w2, c), sy)\n',
     '                    gk[cle] = trajectoire_plan(w2, p, s, dt2, K_GARDE, compteur, sortie_s, "b_p%d_w%.2f_c%.2f_c" % (p, w2, c), sy)\n'
     '                    gdt4[cle] = trajectoire_plan(w2, p, s, dt2 / 4, K_BASC, compteur, sortie_s, "b_p%d_w%.2f_c%.2f_d" % (p, w2, c), sy, jumelle=4)   # v14\n', 'B13 banc de series : dt/4')
repb('        return lire_alpha(plan, gdt, gk, seuil, lignee, e_req), compteur\n', '        return lire_alpha(plan, gdt, gk, seuil, lignee, e_req, gdt4=gdt4), compteur\n', 'B14')
repb('        return lire_alpha(plan, gdt, gk, seuil, lignee, e_req)\n', '        return lire_alpha(plan, gdt, gk, seuil, lignee, e_req, gdt4=gdt4)\n', 'B15')
repb('    return {"plan": n_plan, "G_dt": n_plan, "G_k": n_plan, "G_seuil": len(DEGRES) * len(W2S),',
     '    return {"plan": n_plan, "G_dt": n_plan, "G_k": n_plan, "G_dt4": n_plan, "G_seuil": len(DEGRES) * len(W2S),', 'B9 comptes attendus')
assert all(c < 128 for c in b.encode())
BANC = os.path.join(OUT, 'banc_qualification_machine1_v14.py')
open(BANC, 'w', encoding='utf-8', newline='\n').write(b)
print('BANC v14 : %d remplacements ; canon %s' % (len(HB), canon(BANC)))
print('reglage v8 : n = 18, delta = %s ; kT %.4f m %.4f ; n_2a %d ; pred (a) %s ; transport x%.4f, %.4f rad' % (
    d18['DP'], d18['kT'], d18['m'], d18['n2a'], {p: '%.4e' % v for p, v in pred.items()}, fac ** (b7 / 2), -w7 * math.log(math.sqrt(fac))))
