#!/usr/bin/env python3
# -*- coding: ascii -*-
"""CONSTRUCTION DU GEL constante A v7 = v6 EMIS (847bb3bb2dd19f87, machine 1, NON CERTIFIE, REMPLACE,
non edite) + les hunks qui levent les defauts de la certification machine 2 du v6. machine 2, v1,
13/09/2026. Plume du gel : machine 1, conservee -- ce script n'ecrit que ce qui se DERIVE ou se
MESURE, a ancre unique, et machine 1 contresigne le v7 par diff (ou le refuse : le pin du v10
est alors a refaire).

  H6  4.8 RE-DERIVEE (D-v6-3, FOND) : les intervalles de la jumelle etaient ceux du v5 (2 x 620) ;
      l'instrument v9 derive 2 x 400 ; gel et instrument se contredisaient.
  H7  9 RE-DERIVEE (D-v6-4, FOND) : la colonne bruit/signal et ses deux derivees rapportaient
      bruit_R a l'ancien signal 1/1024 (18.0x, 21.4x, 51.8x) alors que la ligne signal_R dit 1/441.
  H8  3.2 : la ligne n = 23, "non jouee" au v6, est MESUREE sur BOCAL4 (D-v6-2) : branche 5,
      min e/seuil 1.113 < 1.15 -> exclue par la clause (T) de la regle, mesuree et non derivee ;
      3.5 le dit.
  H9  11 : "v9" designait le temoin v9, remplace ; le volet T se compte sous la v11 (D-v6-5).
  H10 en-tete : provenance du v7, et le fait que la table 3.2 du v6 etait un hunk manuel hors
      script (D-v6-1). Titre et ligne FIN passent en v7.
Usage : construction_gel_v7_machine2_v1.py <v6 emis> <sortie v7> <log pre-vol n23 BOCAL4>
"""
import hashlib, json, math, os, re, sys, unicodedata
from fractions import Fraction as F

SRC, OUT, L23 = sys.argv[1], sys.argv[2], sys.argv[3]
raw = open(SRC, 'rb').read()
assert hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()).hexdigest()[:16] == '847bb3bb2dd19f87'
s = raw.decode('utf-8')
RAC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- H6 : 4.8, derivee
d0, M, r, k, dt1 = F(1, 100), 20, F(1, 10), 2, 0.006
dp = d0 / 21 ** 2
W2 = ('1.73', '2.27', '2.80')
td = {w: math.sqrt(float(dp / (1 + F(w) ** 2))) for w in W2}
e = {w: math.ceil(dt1 / (k * td[w] / M)) for w in W2}
n2a_j = ' / '.join('[%d, %d]' % (2 * (400 - e[w]), 2 * 401) for w in W2)
n2s_j = ' / '.join('[%d, %d]' % (2 * 400, 2 * (400 + e[w])) for w in W2)
assert n2a_j == '[748, 802] / [736, 802] / [724, 802]', n2a_j
assert n2s_j == '[800, 852] / [800, 864] / [800, 876]', n2s_j

# ---------------------------------------------------------------- H7 : 9, derivee du run 85
JA = json.load(open(os.path.join(RAC, 'registre', 'runs', 'run_alpha_delta85', 'resultats_alpha.json'), encoding='utf-8'))
al = {4: F(2), 5: F(4, 3), 7: F(4, 5)}
disp = {p: JA['degres'][str(p)]['dispersion_lnA'] for p in (4, 5, 7)}
sig = 1.0 / 441
lignes9 = {}
for p in (4, 5, 7):
    b = disp[p] * (p - 2) / (sum(math.log(v) for v in JA['degres'][str(p)]['gA_sur_K'].values()) / 6)
    lignes9[p] = (b, b / sig, b / sig / math.sqrt(6), b / sig / math.sqrt(18))
ANC9 = ("    4    1.7624e-02        18.0x             7.4x               4.3x\n"
        "    5    2.0866e-02        21.4x             8.7x               5.0x\n"
        "    7    5.0582e-02        51.8x            21.1x              12.2x\n")
NEW9 = ''.join("    %d    %.4e   %10.1fx   %14.1fx   %16.1fx\n" % (p, lignes9[p][0], lignes9[p][1], lignes9[p][2], lignes9[p][3]) for p in (4, 5, 7))
assert all('%.4e' % lignes9[p][0] in ANC9 for p in (4, 5, 7)), 'bruit_R ne se retrouve pas au v6'
lo, hi = min(x[1] for x in lignes9.values()), max(x[1] for x in lignes9.values())

# ---------------------------------------------------------------- H8 : n = 23, mesure
lg = open(L23, 'rb').read().decode('utf-8', 'replace')
v23 = re.search(r'VERDICT\s+(.+)', lg).group(1).strip()
assert v23.startswith('REGLAGE QUALIFIE'), v23
rat = [float(x) for x in re.findall(r'e/seuil=([0-9.]+)', lg)]
pobs = [(float(a), float(t)) for a, t in re.findall(r'p_obs=([0-9.]+) tol_ordre=([0-9.]+)', lg)]
assert len(rat) == 9 and len(pobs) == 9
mn, mx = min(rat), max(abs(a - 4) / t for a, t in pobs)
assert mn < 1.15
INF = 1.659260768e-05
kT23, m23 = (1 / 52900) / INF, 3.457292925e-05 * 52900

REMPL = [
    # titre et provenance
    ("# PRE-ENREGISTREMENT constante A v6 -- LA FENETRE DESCEND",
     "# PRE-ENREGISTREMENT constante A v7 -- LA FENETRE DESCEND"),
    ("# BROUILLON MACHINE 1 -- DEVIENT GEL A LA CERTIFICATION MACHINE 2\n# v6 = v5 (2c0d2dc86054838c, 31722 o, CERTIFIEE 104/104 par machine 2, REMPLACEE, non\n# editee) + les hunks enumeres par construction_gel_v6_et_banc_v9_machine1_v1.py :\n",
     "# BROUILLON MACHINE 1 -- DEVIENT GEL A LA CERTIFICATION MACHINE 2\n"
     "# v7 = v6 (847bb3bb2dd19f87, 40158 o, NON CERTIFIEE par machine 2 -- D-v6-3 : 4.8 non re-derivee,\n"
     "# D-v6-4 : section 9 non re-derivee -- REMPLACEE, non editee) + cinq hunks derives ou mesures,\n"
     "# appliques par construction_gel_v7_machine2_v1.py (machine 2 ; plume machine 1 conservee, a\n"
     "# contresigner par diff) : H6 4.8 re-derivee au reglage v6 (2 x 400) ; H7 section 9, colonnes\n"
     "# bruit/signal re-derivees au signal 1/441 ; H8 3.2, la ligne n = 23 MESUREE sur BOCAL4 (branche 5,\n"
     "# min e/seuil 1.113 < 1.15 : exclue par la clause (T), mesuree) et 3.5 le dit ; H9 11, le volet T\n"
     "# se compte sous la v11 ; H10 cette provenance. Fait de forme du v6 (D-v6-1) : sa table 3.2 etait\n"
     "# un hunk MANUEL, hors du script de construction qu'il declarait comme provenance.\n"
     "# v6 = v5 (2c0d2dc86054838c, 31722 o, CERTIFIEE 104/104 par machine 2, REMPLACEE, non\n# editee) + les hunks enumeres par construction_gel_v6_et_banc_v9_machine1_v1.py :\n"),
    # H8 : la ligne n = 23 de la table 3.2
    ("    23  1/52900    1.139  1.829  (pre-vol non joue a ce n)\n",
     "    23  1/52900    %.3f  %.3f  %-46s %.3f         %.2f   (BOCAL4)\n" % (kT23, m23, v23[:46], mn, mx)),
    ("        ne passe la porte sur cette echelle (n = 22 et n = 24 mordent) :",
     "        ne passe la porte sur cette echelle (n = 22 et n = 24 mordent ; n = 23\n        ouvre mais a e/seuil = %.3f < 1.15, clause (T) mesuree) :" % mn),
    # H6 : 4.8
    ("    n_2a jumelle : [1162, 1242] / [1144, 1242] / [1124, 1242]\n", "    n_2a jumelle : %s\n" % n2a_j),
    ("    n_2s jumelle : [1240, 1318] / [1240, 1336] / [1240, 1356]\n", "    n_2s jumelle : %s\n" % n2s_j),
    # H7 : 9
    (ANC9, NEW9),
    ("**L-desc REFUTE R ~ 1 (structure persistante) a 18 a 52 fois le bruit ;",
     "**L-desc REFUTE R ~ 1 (structure persistante) a %d a %d fois le bruit ;" % (round(lo), round(hi))),
    # H9 : 11
    ("Volet A : identiques au v5 4.5 -- plan 18, G_dt 18, G_k 18, G_seuil 9,\nG_lignee 27 ; `comptes + sautes == 90`. Volet T : les comptes de la\n**v9** -- ATTENDUS = 41 (voie A), en forme derivee.",
     "Volet A : identiques au v5 4.5 -- plan 18, G_dt 18, G_k 18, G_seuil 9,\nG_lignee 27 ; `comptes + sautes == 90`. Volet T : les comptes de la\n**v11** (et son erratum 7 (i)) -- ATTENDUS = 41 (voie A), en forme derivee."),
    ("-- FIN constante_A_pre_enregistrement_v6 --", "-- FIN constante_A_pre_enregistrement_v7 --"),
]
for a, b in REMPL:
    assert s.count(a) == 1, 'ancre non unique ou absente : %r' % a[:70]
    s = s.replace(a, b)
assert all(ord(c) < 128 for c in s), 'non ASCII'
open(OUT, 'w', encoding='ascii', newline='\n').write(s)
c = hashlib.sha256(unicodedata.normalize('NFC', s).encode()).hexdigest()[:16]
print('v7 ecrit : %s canon %s %d o ; %d remplacements ; 4.8 %s | %s ; 9 bruit/signal %s ; n=23 %s min e/seuil %.3f'
      % (os.path.basename(OUT), c, len(s.encode()), len(REMPL), n2a_j, n2s_j,
         ', '.join('%.1fx' % lignes9[p][1] for p in (4, 5, 7)), v23[:30], mn))
