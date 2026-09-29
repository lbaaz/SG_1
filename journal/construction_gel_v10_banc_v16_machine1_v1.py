#!/usr/bin/env python3
# -*- coding: ascii -*-
"""CONSTRUCTION DU GEL constante A v10 (depuis le v9 b515abc5a6da73c5, CERTIFIE) ET DU BANC v16 (depuis
le v15 a1553f6eb5cc74b8, CERTIFIE). machine 1, v1, 29/09/2026. Go operateur du 29/09 : "gel v10".
OBJET DU v10 : MESURER A. Le v9 testait le terme du premier ordre a un reglage deplace ; le v10 revient
au barreau du 91 (n = 21, regle du plus grand n qui ouvre la porte, v7 3.2 restauree), lit la P-A
corrigee comme une MESURE (valeur et incertitude par degre), et pre-enregistre trois predictions :
(a) le biais du premier ordre au levier 1 (les biais C4 eux-memes), (b) le transport des modes libres
du 92 vers le 91 (levier 324/441), (c) NEUVE : le coefficient du terme tau^2 AJUSTE LIBREMENT egale c1
derive, aux 18 points, a 10 pour cent -- c'est la forme qui lit le premier ordre a p = 7 sans projeter
le mode (cause de 7|1.73|1.20 au 92). Rien n'est edite ; ancres uniques asserees ; fragments du reglage
regeneres a n = 18 (ancre) et n = 21 (remplacement) par la machinerie de la construction du v6/v8.
Usage : <v9.md> <v15.py> <derivation.json> <lecture_v9_predictions_delta92.json (base 92)> <sortie>
"""
import hashlib, importlib.util, json, math, os, re, sys, unicodedata
from fractions import Fraction as F

V9, V15, DER, BASE92, OUT = sys.argv[1:6]
os.makedirs(OUT, exist_ok=True)
spec = importlib.util.spec_from_file_location('mach', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'machinerie_reglage.py'))
mach = importlib.util.module_from_spec(spec); spec.loader.exec_module(mach)


def canon(p):
    raw = open(p, 'rb').read()
    return hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()).hexdigest()[:16]


assert canon(V9) == 'b515abc5a6da73c5', canon(V9)
assert canon(V15) == 'a1553f6eb5cc74b8', canon(V15)
assert canon(DER) == 'b70fca94d72822ad', canon(DER)
assert canon(BASE92) == 'af295b8a660d33e8', canon(BASE92)
der, base92 = json.load(open(DER)), json.load(open(BASE92))
d18, d21 = mach.R(18), mach.R(21)
f18, f21, a18, a21 = mach.frags(d18), mach.frags(d21), mach.attentes(d18), mach.attentes(d21)
W2 = ('1.73', '2.27', '2.80')
PROJ4 = 0.2238


def coeffs(p, w2):
    a = F(4, p - 2); w = F(w2)
    K = a * (a + 1) * (a + 2) * (a + 3); P2 = a * (a + 1) * (a - 1) * (a - 2); P4 = (4 - a) * (3 - a) * (2 - a) * (1 - a)
    c1 = (1 + w * w) * a * (a + 1) / ((p - 1) * K - P2)
    c2 = (K * F((p - 1) * (p - 2), 2) * c1 * c1 - (1 + w * w) * c1 * (2 - a) * (1 - a) - w * w) / (P4 - (p - 1) * K)
    return c1, c2


PL = {}
for p in (4, 5, 7):
    vals = []
    for w2 in W2:
        c1, c2 = coeffs(p, w2)
        assert F(der['C2']['%d|%s' % (p, w2)]['c2'][0]) == c2
        vals.append(abs(float(c2)) * (float(d21['DP']) / (1 + float(w2) ** 2)) ** 2)
    PL[p] = PROJ4 * max(vals)
LEV_B = 324 / 441                      # du 92 (n = 18) vers le 91 (n = 21)
b7, w7 = 2.3, der['C3']['7']['im_complexe']
FA, DPH = LEV_B ** (b7 / 2), -w7 * math.log(math.sqrt(LEV_B))

# ---------------------------------------------------------------- LE GEL v10
s = open(V9, encoding='utf-8').read()
H, manques = [], []


def rep(old, new, nom, count=1, must=True):
    global s
    c = s.count(old)
    if c != count:
        if must:
            raise AssertionError('GEL %s : %d occurrence(s) de %r' % (nom, c, old[:70]))
        manques.append('%s (%d)' % (nom, c)); return
    s = s.replace(old, new); H.append(nom)


for cle in ('h19', 'h20', 's0', 's33a', 's33b', 's33c', 's33t', 's41', 's43', 's44', 's45', 'deb', 'n2a', 'bornes', 'cout', 'pas',
            'i47', 'n2s', 'j2a', 'j2s', 's471', 's6', 's10', 's12'):
    rep(f18[cle], f21[cle], 'H2 ' + cle, must=False)
n324 = len(re.findall(r'1/324(?!\d)', s)); s = re.sub(r'1/324(?!\d)', '1/441', s); H.append('H2 1/324 -> 1/441 (%d)' % n324)
rep(f18['r2v4'], f21['r2v4'], 'H2 signal 4 dec', must=False); rep(f18['r2v3'], f21['r2v3'], 'H2 signal 3 dec', must=False)
lignes9 = re.findall(r'\n    (\d)    (\d\.\d{4}e-0\d) +(\d+\.\d)x +(\d+\.\d)x +(\d+\.\d)x', s)
assert len(lignes9) == 3
for p, bruit, r1, r2, r3 in lignes9:
    b = float(bruit); sig = 1.0 / 441
    old = re.search(r'\n(    %s    %s +%sx +%sx +%sx)' % (p, re.escape(bruit), re.escape(r1), re.escape(r2), re.escape(r3)), s).group(1)
    s = s.replace(old, "    %s    %s   %8s   %14s   %17s" % (p, bruit, '%.1fx' % (b / sig), '%.1fx' % (b / sig / math.sqrt(6)), '%.1fx' % (b / sig / math.sqrt(18))))
lo9, hi9 = min(float(x[1]) * 441 for x in lignes9), max(float(x[1]) * 441 for x in lignes9)
old_syn = re.search(r"\*\*L-desc REFUTE R ~ 1 \(structure persistante\) a \d+ a \d+ fois le bruit ;", s).group(0)
s = s.replace(old_syn, "**L-desc REFUTE R ~ 1 (structure persistante) a %d a %d fois le bruit ;" % (round(lo9), round(hi9))); H.append('H2 section 9')
# 3.2 : la regle du plus grand n, restauree
i0 = s.index("(le compte nominal 4.6 reste entier : M(n - 1)). REGLE DE CHOIX DU v8")
tab0 = s.index("    n   delta'", i0)
s = s[:i0] + """(le compte nominal 4.6 reste entier : M(n - 1)). REGLE DE CHOIX DU v10 : ce gel
MESURE A ; la regle du v7 3.2 est RESTAUREE -- n est le plus grand entier de l'echelle
tel que le pre-vol du temoin rende branche 5 avec e/seuil >= 1.15 aux neuf points sur
les deux machines : n = 21 (e/seuil >= 1.433 ; branche 5 des deux cotes au 91 ; run
reel 91 REGLAGE QUALIFIE). C'est le barreau du 91 : ce que le 91 n'a pas pu lire (deux
niveaux, plancher du modele), le v10 le lit sous la lecture corrigee, et le compare.
La regle d'echelle du v8/v9 (n = 18) a rempli son office au delta 92 et est levee.
Aucune valeur de A n'entre dans ce choix. Balayage (machine 1, levier X86_V4) :

""" + s[tab0:]; H.append('H1 regle 3.2 restauree')
# 5bis : (a) au levier 1, (b) depuis la base du 92, (c) neuve
i_a = s.index("PREDICTION EN AVEUGLE (a) -- LE BIAIS DU PREMIER ORDRE EST PROPORTIONNEL A delta' :")
i_fin = s.index("CE QUE LA P-A DEVIENT, TELLE QUE L'INSTRUMENT v15 LA CALCULE (R-v8-2)")
rows = []
for cle in sorted(base92['modes_p7']):
    v = base92['modes_p7'][cle]
    rows.append("    %-14s %+.6e   %+.6e   %.6e   %+.4f" % (cle, v['a'], v['c'], v['amplitude'], v['phase']))
BIA = {p: {w2: der['C4']['%d|%s' % (p, w2)]['0.0']['biais_lnA'] for w2 in W2} for p in (4, 5, 7)}
s5 = """PREDICTION EN AVEUGLE (a) -- LE BIAIS DU PREMIER ORDRE AU BARREAU DU 91 (levier 1) :
  lu sur l'ajustement II sans c1, apres Richardson a ordre mesure, contre ln(K/g)/(p-2) :
  pred(p, w2) = biais_91(p, w2), le biais C4 lui-meme (b70fca94d72822ad, decalage 0.0) :
    p = 4 : %s
    p = 5 : %s
    p = 7 : lisible sous (c) seulement -- le mode libre se projette sur II (delta 92, nn.6)
  TIENT au degre (p = 4, 5) si obs_R/pred est dans [0.8, 1.2] aux six points ET
  |obs_R - pred| <= 3 S(p). Au 92 la meme lecture tenait a 2 pour cent au levier 441/324 ;
  ici le levier vaut 1 et la lecture n'est plus a posteriori (le 91 ne l'a jamais jouee
  a trois niveaux).

PREDICTION EN AVEUGLE (b) -- LE TRANSPORT DES MODES LIBRES DU 92 (n = 18) VERS LE 91
  (n = 21) : levier 324/441 ; amplitude x (324/441)^(b/2) = %.4f, phase - w ln sqrt(324/441)
  = %+.4f rad (w = %.6f), point par point, lus sur M2 apres Richardson ; TIENT au point a
  20 pour cent et 0.3 rad. Base du 92, (a, c) apres Richardson a ordre mesure (machine 1,
  lecture v9 %s ; les memes a 1e-16 chez machine 2) :
    point          a               c               amplitude       phase (rad)
%s
  Au 92 le transport 21 -> 18 tenait 6/6 a 5 pour cent et 0.036 rad.

PREDICTION EN AVEUGLE (c) -- LE TERME tau^2, AJUSTE LIBREMENT, VAUT c1 DERIVE :
  l'instrument v16 ajuste a chaque cellule, a cote de M1/M2, la forme M1c (p = 4, 5 :
  y + alpha ln tau = lnA + c1_fit tau^2) et M2c (p = 7 : plus le mode libre a (b, w)
  derives), c1_fit LIBRE ; par point, c1_R = Richardson a ordre mesure sur les trois
  niveaux (q hors [3, 5] -> NON LU). Prediction : c1_R / c1_derive(p, w2) dans
  [0.9, 1.1] aux 18 points, c1_derive = (1 + w2^2) alpha (alpha+1)/((p-1) K - P2) :
    p = 4 : %s ; p = 5 : %s ; p = 7 : %s   (w2 = 1.73 / 2.27 / 2.80)
  C'est la lecture du premier ordre qui ne projette pas le mode (cause de 7|1.73|1.20,
  delta 92 nn.6) : elle vaut aux trois degres, p = 7 compris. La feuille rend aussi
  l'erreur-type de c1_fit ; elle ne fait pas verdict, la tolerance de 10 pour cent le fait.

LA MESURE DE A (ce que ce gel appelle mesurer) : par point, lnA_R (Richardson a ordre
  mesure sur M1/M2) ; par degre, delta_p = moyenne des six (lnA_R - ln(K/g)/(p-2)) et
  S(p) = max - min des six lnA_R ; A(p) = (K/g)^(1/(p-2)) exp(delta_p), incertitude
  S(p) + plancher_corr(p) en lnA. P-A corrigee, telle que l'instrument la calcule, est
  le test : vraie au degre si |lnA_R - ln(K/g)/(p-2)| <= tol_lnA(p) aux points lus.
  Au 92 (n = 18, a posteriori pour ce gel) : S(p) = 4.47e-09 / 3.72e-09 / 3.52e-09
  (BOCAL4), P-A vraie aux trois. Ce gel pre-enregistre la meme lecture a n = 21.

""" % (" / ".join("%.6e (w2 %s)" % (BIA[4][w2], w2) for w2 in W2), " / ".join("%.6e (w2 %s)" % (BIA[5][w2], w2) for w2 in W2),
       FA, DPH, w7, canon(BASE92), "\n".join(rows),
       " / ".join("%.6f" % float(coeffs(4, w2)[0]) for w2 in W2), " / ".join("%.6f" % float(coeffs(5, w2)[0]) for w2 in W2), " / ".join("%.6f" % float(coeffs(7, w2)[0]) for w2 in W2))
s = s[:i_a] + s5 + s[i_fin:]; H.append('H3 5bis predictions (a) (b) (c) et la mesure')
rep("CE QUE LA P-A DEVIENT, TELLE QUE L'INSTRUMENT v15 LA CALCULE (R-v8-2)", "CE QUE LA P-A EST, TELLE QUE L'INSTRUMENT v16 LA CALCULE (v15 inchange sur ce point)", 'H3 titre P-A')
# 7 et 7bis : attendu sur les S du 92 ; planchers a n = 21 ; dette proj4 levee
rep("Attendu de conception, sur ce que le run 91 a MESURE (jamais sur le 85) : S_M1(4)\n= 5.8e-09, S_M1(5) = 3.7e-09, S_M2(7) = 4.4e-09 a n = 21 (Q5, deux machines) ;\ntransportes a n = 18 par les deux lois (pente mesuree 85 -> 91 ; troncature en\ndt^4) ils restent entre 4e-09 et 1e-08.",
    "Attendu de conception, sur ce que le run 92 a MESURE (jamais sur le 85) : S(p) =\n4.47e-09 / 3.72e-09 / 3.52e-09 a n = 18 sous la lecture corrigee (BOCAL4 ; machine 1 :\n3.54e-09 a p = 4, un point expose, les deux autres identiques), et au 91 sous Q5\n5.8e-09 / 3.7e-09 / 4.4e-09 a n = 21 : entre 3e-09 et 6e-09 au barreau du v10.", 'H4 attendu 92')
rep("Contre des planchers corriges de\n%.1e / %.1e / %.1e" % (5.194891026474795e-14, 1.2236486277104784e-13, 3.181768292545168e-13),
    "Contre des planchers corriges de\n%.1e / %.1e / %.1e" % (PL[4], PL[5], PL[7]), 'H4 planchers section 7')
rep("  Valeur prise : proj4 = %.4f, borne HAUTE de l'intervalle mesure ; machine 1\n  ne l'a pas re-derivee (dette declaree : la valeur est celle de machine 2,\n  citee par canon, et quatre ordres sous S rendent l'ecart sans portee).\n  A n = 18 (delta' = 1/32400) :\n    p = 4 : %.4e     p = 5 : %.4e     p = 7 : %.4e" % (PROJ4, 5.194891026474795e-14, 1.2236486277104784e-13, 3.181768292545168e-13),
    "  Valeur prise : proj4 = %.4f, borne HAUTE de l'intervalle mesure, RE-DERIVEE par\n  machine 1 le 29/09 (JSON identique au bit, 3b12117a58dde698 ; log 6194df14ffd3d12e) :\n  la dette du v9 est levee, le nombre est a deux machines.\n  A n = 21 (delta' = 1/44100) :\n    p = 4 : %.4e     p = 5 : %.4e     p = 7 : %.4e" % (PROJ4, PL[4], PL[5], PL[7]), 'H4 7bis n = 21, dette levee')
rep("  soit 1e-07 fois le plancher du v7 et 1e-05 fois S(p) du 91.", "  soit 1e-07 fois le plancher du v7 et 1e-05 fois S(p) du 91 et du 92.", 'H4 7bis portee')
rep("BOCAL4 rend branche 4 a n = 18 (il a rendu branche 5, marge 1.868), la cascade", "BOCAL4 rend branche 4 a n = 21 (il a rendu branche 5 au 91, marge 1.433), la cascade", 'H4 cascade')
rep("a n = 18 sous les deux lois de transport (machine 2, certification du v8) --", "a n = 18 sous les deux lois de transport (machine 2, certification du v8) et au 92 --", 'H4 contraste')
# 10 : instrument v16
rep("10. L'INSTRUMENT v15 -- DU AVANT TOUT RUN", "10. L'INSTRUMENT v16 -- DU AVANT TOUT RUN", 'H5 titre 10')
rep("Part du v14 CERTIFIE (banc_qualification_machine1_v14.py dc91676c640d4323,\ncertification machine 2 45de25ac61321661 : selftest 103/103, banc 56/56, pre-vols\nbranche 5 sur BOCAL4), construit par construction_gel_v9_banc_v15_machine1_v1.py\n-- le meme script que ce gel -- qui porte la lecture CORRIGEE dans l'instrument",
    "Part du v15 CERTIFIE (banc_qualification_machine1_v15.py a1553f6eb5cc74b8,\ncertification machine 2 b5568d8f31f8492e ; run delta 92 sur les deux machines),\nconstruit par construction_gel_v10_banc_v16_machine1_v1.py -- le meme script que ce\ngel -- qui re-parametre le reglage a n = 21 (les attentes du selftest et les tables\ndu gel re-derivees) et ajoute UNE forme d'ajustement : M1c/M2c a c1 LIBRE\n(ajuster_c1_libre, cle ajustement_c1_libre a chaque cellule : c1_fit, son erreur-type,\nlnA), sans aucun verdict de cascade -- la prediction (c) se lit dessus. Le v15 avait\nporte la lecture CORRIGEE dans l'instrument", 'H5 section 10')
rep("Le v15 se re-certifie EN ENTIER par machine 2 (selftest, banc qui tue -- 58\nscenarios --, NE-JOUE-PAS) et son pre-vol se joue des deux cotes au reglage v9\n(= v8 : n = 18) avant tout run.",
    "Le v16 se re-certifie EN ENTIER par machine 2 (selftest, banc qui tue -- 58\nscenarios --, NE-JOUE-PAS) et son pre-vol se joue des deux cotes au reglage v10\n(n = 21) avant tout run.", 'H5 certif v16')
old_head = s[:s.index('# Banc de verification (N-69')]
new_head = """# PRE-ENREGISTREMENT constante A v10 -- MESURER A : LA P-A CORRIGEE LUE COMME UNE MESURE
# (VALEUR ET INCERTITUDE PAR DEGRE) AU BARREAU DU 91 (n = 21, REGLE DU PLUS GRAND n
# RESTAUREE), TROIS PREDICTIONS EN AVEUGLE DONT UNE NEUVE : LE TERME tau^2 AJUSTE
# LIBREMENT VAUT c1 DERIVE AUX 18 POINTS
# BROUILLON MACHINE 1 -- DEVIENT GEL A LA CERTIFICATION MACHINE 2
# v10 = v9 (b515abc5a6da73c5, CERTIFIE des deux cotes, REMPLACE, non edite) + les hunks
# de construction_gel_v10_banc_v16_machine1_v1.py :
#   H1  3.2 : regle du plus grand n restauree (v7) -> n = 21, le barreau du 91 ; la regle
#       d'echelle du v8/v9 est levee, son office rempli au delta 92.
#   H2  tous les nombres du reglage re-derives a n = 21 (3.3, 4.1, 4.3-4.8, 6, 9, 10,
#       12 ; 1/324 -> 1/441) par la machinerie de la construction du v6/v8.
#   H3  5bis : (a) au levier 1 (les biais C4 eux-memes, p = 4 et 5) ; (b) le transport
#       des modes libres du 92 vers le 91 (levier 324/441, base du 92) ; (c) NEUVE, c1
#       libre aux 18 points a 10 pour cent ; et la MESURE de A, definie avant le run.
#   H4  7 : attendu sur les S du 92 ; 7bis : planchers a n = 21, dette proj4 LEVEE
#       (re-derivee par machine 1 le 29/09) ; cascade et contraste mis au 92.
#   H5  10 : instrument v16 = v15 certifie + M1c/M2c a c1 libre ; 13 : pieces du 92.
# Rien d'autre ne change : modeles, Richardson a ordre mesure, lecture corrigee, N-70,
# LD-16, temoin, tous inchanges du v9.
"""
s = s.replace(old_head, new_head); H.append('H0 en-tete')
rep("puis suspendu au v8 au profit de la regle d'echelle (3.2)", "suspendu au v8/v9 au profit de la regle d'echelle, RESTAURE au v10 (3.2)", 'H5 section 12 (v)', must=False)
s = s.replace("lecture_v9_machine1_v1.py", "lecture_v10_machine1_v1.py"); H.append('H feuille v10')
s = s.replace("-- FIN constante_A_pre_enregistrement_v9 --", """    constante_A_pre_enregistrement_v9.md               b515abc5a6da73c5  REMPLACE (certifie)
    journal_delta_nn_constante_A_second_ordre_v1.md    0a526d04fd9a8bda  (delta 92, contresigne
                                                       1c4660dd54c463d8 ; depot a venir)
    lot m2 run_delta92 fb456f007eab7c61 ; lot m1 certification du run af86e5b281d037e9
    m1_lecture_v9_predictions_delta92.json             af295b8a660d33e8  (base du 92 pour (b))
    banc_qualification_machine1_v15.py                 a1553f6eb5cc74b8  CERTIFIE, REMPLACE PAR LE v16

-- FIN constante_A_pre_enregistrement_v10 --"""); H.append('H section 13 et FIN')
assert all(c < 128 for c in s.encode())
GEL = os.path.join(OUT, 'constante_A_pre_enregistrement_v10.md')
open(GEL, 'w', encoding='utf-8', newline='\n').write(s)
print('GEL v10 : %d hunks ; non appliques : %s ; canon %s ; planchers n=21 %s' % (len(H), manques or 'aucun', canon(GEL), {p: '%.4e' % PL[p] for p in PL}))

# ---------------------------------------------------------------- LE BANC v16
b = open(V15, encoding='utf-8').read()
HB = []


def repb(old, new, nom, count=1):
    global b
    c = b.count(old)
    assert c == count, 'BANC %s : %d occurrence(s) de %r' % (nom, c, old[:70])
    b = b.replace(old, new); HB.append(nom)


repb(a18['pl'], a21['pl'], 'B1 planchers du selftest (2)', count=2)
for cle in ('DELTA', 'BJ', 'st', 'nom', 'l46', 'i46', 'n2ak', 'l47', 'i47', 'j47', 'j2a', 'g24', 'g25', 'json', 'ldesc', 'tab'):
    repb(a18[cle], a21[cle], 'B1 ' + cle)
repb("DE LA CONSTANTE A (delta' = 1/32400 ; v15 = v14 certifie + la lecture CORRIGEE dans l'instrument (gel v9 5bis, 7, 7bis ;",
     "DE LA CONSTANTE A (delta' = 1/44100 ; v16 = v15 certifie + M1c/M2c a c1 libre (gel v10 5bis (c)), reglage n = 21, pin gel v10,\nconstruction_gel_v10_banc_v16_machine1_v1.py ; v15 = v14 certifie + la lecture CORRIGEE dans l'instrument (gel v9 5bis, 7, 7bis ;", 'B2 en-tete')
repb("  - delta := delta' = 1/32400 (gel v8, 3 : regle d'echelle, n = 18) ; delta_0 = 1/100",
     "  - delta := delta' = 1/44100 (gel v10, 3 : plus grand n qui ouvre la porte, n = 21) ; delta_0 = 1/100", 'B2 l.17')
repb('GEL_ALPHA = ("gels/constante_A_pre_enregistrement_v9.md", "b515abc5a6da73c5", 50206)',
     'GEL_ALPHA = ("gels/constante_A_pre_enregistrement_v10.md", "%s", %d)' % (canon(GEL), os.path.getsize(GEL)), 'B3 pin v10')
repb('VERSION = "banc_qualification_machine1_v15"', 'VERSION = "banc_qualification_machine1_v16"', 'B4 VERSION')
repb('def plancher_corrige(p):', '''def ajuster_c1_libre(t, x, w2, p, dt):
    """v16 (gel v10, 5bis (c)) : la forme M1c (p = 4, 5) / M2c (p = 7) a c1 LIBRE -- y + alpha ln tau =
    lnA + c1_fit tau^2 [+ s^b (a cos(w ln s) + c sin(w ln s))]. Meme fenetre, meme minimisation de
    t* ; rend c1_fit, son erreur-type (moindres carres), lnA. Aucun verdict de cascade."""
    a = float(alpha_de(p))
    b, wlib = float(a + Fraction(3, 2)), FREQ_MODE_LIBRE[p]
    tc, td = tau_cap(w2), tau_dom(w2)
    ok = np.isfinite(x) & (x != 0)
    t, x = t[ok], x[ok]
    y = np.log(np.abs(x))
    ref = ajuster_point_fixe(t, x, w2, p, dt)
    if ref["statut"] != "POINT_FIXE":
        return {"statut": ref["statut"]}
    fen = fenetre_de(t, ref["t_star"], tc, td, 1e-6 * dt)
    tt, yy = t[fen], y[fen]

    def systeme(ts):
        tau = ts - tt
        u = yy + a * np.log(tau)
        cols = [np.ones_like(tau), tau ** 2]
        if p == 7:
            s = tau / td
            cols += [s ** b * np.cos(wlib * np.log(s)), s ** b * np.sin(wlib * np.log(s))]
        return u, np.column_stack(cols)

    def SS(ts):
        u, X = systeme(ts)
        return float(((u - X @ np.linalg.lstsq(X, u, rcond=None)[0]) ** 2).sum())

    lo, hi = float(tt[-1]) * (1 + 1e-12) + 1e-12 * tc, float(t[-1]) + 2 * td
    ts, ss = _minimiser_1d(SS, lo, hi)
    u, X = systeme(ts)
    coef, _, rang, _ = np.linalg.lstsq(X, u, rcond=None)
    n, k = X.shape
    sig2 = ss / max(n - k, 1)
    cov = sig2 * np.linalg.inv(X.T @ X)
    return {"statut": "AJUSTE", "modele": "M2c" if p == 7 else "M1c", "lnA": float(coef[0]), "c1_fit": float(coef[1]),
            "c1_err": float(math.sqrt(max(cov[1, 1], 0.0))), "t_star": ts, "SS": ss, "rang": int(rang), "n_points": int(n)}


def plancher_corrige(p):''', 'B5 ajuster_c1_libre')
repb('    rec["ajustement_corrige"] = ajuster_corrige(ph2["t"], x, w2, p, dt2)',
     '    rec["ajustement_corrige"] = ajuster_corrige(ph2["t"], x, w2, p, dt2)\n    rec["ajustement_c1_libre"] = ajuster_c1_libre(ph2["t"], x, w2, p, dt2)   # v16 (gel v10, 5bis (c))', 'B6 appel')
repb("""            if self.sans_cap:
                n = int(round((t_max - t0) / dt))
                t = t0 + dt * np.arange(n + 1)""", """            if self.sans_cap:
                # v16 : horizon du synthetique SANS CAP borne a 20 N_2BP pas -- le verdict (T_MAX -> G-fen) ne
                # depend pas de la longueur, la memoire si : a n = 21, la jumelle dt/4 demandait 63 M pas.
                n = min(int(round((t_max - t0) / dt)), 20 * N_2BP)
                t = t0 + dt * np.arange(n + 1)""", 'B7 horizon du synthetique sans CAP')
repb("""        L_pl, _ = jouer_synth(SynthAlpha(s_etoile, bruit_lnA=0.0))
    finally:
        JRN.silence = False
    v, b = cascade_alpha(L_pl)
    scenario("G22 decalage lnA nul""", """        # v16 : la lecture corrigee est rendue NON JOUEE PAR CONSTRUCTION (q = 2 par mutation) -- au v15 elle
        # l'etait par accident (q du synthetique hors [3, 5] a n = 18, dans [3, 5] a p = 5 a n = 21).
        L_pl, _ = jouer_synth(SynthAlpha(s_etoile, bruit_lnA=0.0), mut=lambda pl, g1, g4: _mut_lnA_M_module(pl, g1, g4, 4.0, 1.0, 0.25))
    finally:
        JRN.silence = False
    v, b = cascade_alpha(L_pl)
    scenario("G22 decalage lnA nul""", 'B8 G22 deterministe')
repb("(LD-12 ; la lecture corrigee y est NON JOUEE) -> G-plancher MORD -> branche 3b\",", "(LD-12 ; la lecture corrigee y est NON JOUEE par mutation q = 2) -> G-plancher MORD -> branche 3b\",", 'B8 G22 nom')
repb("def plancher_corrige(p):", """def _mut_lnA_M_module(plan, gdt, gdt4, f0, f1, f2, eps=1e-6):
    \"\"\"v16 : mutation des lnA_M des trois niveaux (banc qui tue) ; (16, 1, 1/16) -> q = 4 ; (4, 1, 1/4) -> q = 2.\"\"\"
    for cle in plan:
        for cell, f in ((plan, f0), (gdt, f1), (gdt4, f2)):
            if cle in cell and isinstance(cell[cle].get("ajustement_corrige"), dict):
                cell[cle]["ajustement_corrige"]["lnA_M"] = 1.0 + f * eps


def plancher_corrige(p):""", 'B9 mutation au niveau module')
assert all(c < 128 for c in b.encode())
BANC = os.path.join(OUT, 'banc_qualification_machine1_v16.py')
open(BANC, 'w', encoding='utf-8', newline='\n').write(b)
print('BANC v16 : %d remplacements ; canon %s' % (len(HB), canon(BANC)))
json.dump({"planchers_corriges_n21": {str(p): PL[p] for p in PL}, "proj4": PROJ4, "levier_b": LEV_B, "facteur_amplitude": FA, "decalage_phase": DPH,
           "c1_derive": {"%d|%s" % (p, w2): float(coeffs(p, w2)[0]) for p in (4, 5, 7) for w2 in W2}}, open(os.path.join(OUT, 'derives_v10.json'), 'w'), indent=1)
