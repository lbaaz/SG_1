#!/usr/bin/env python3
# -*- coding: ascii -*-
"""CONSTRUCTION DU GEL constante A v9 (depuis le v8 800fc6a9a8e56e49, NON CERTIFIE, remplace) ET
DU BANC v15 (depuis le v14 dc91676c640d4323, CERTIFIE par machine 2 45de25ac61321661).
machine 1, v1, 18/09/2026. Arbitrage operateur du 18/09 : la P-A corrigee est PORTEE DANS
L'INSTRUMENT. Rien n'est edite ; ancres uniques asserees ; les nombres se derivent ici.
Le v15 applique les trois remplacements de l'essai hors depot de machine 2
(essai_correctif_PA_hors_depot_machine2.py 0dcfd901a0551d0f, texte repris tel quel, credite),
plus : proj4 DERIVE (D-essai-3), deux scenarios du banc qui tue qui exercent la lecture corrigee
par MUTATION (D-essai-2), G22 nomme, pin gel v9, version.
Usage : <v8.md> <v14.py> <derivation_second_ordre.json> <repertoire de sortie>
"""
import hashlib, json, math, os, re, sys, unicodedata
from fractions import Fraction as F

V8, V14, DER, OUT = sys.argv[1:5]
os.makedirs(OUT, exist_ok=True)


def canon(p):
    raw = open(p, 'rb').read()
    return hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()).hexdigest()[:16]


assert canon(V8) == '800fc6a9a8e56e49', canon(V8)
assert canon(V14) == 'dc91676c640d4323', canon(V14)
der = json.load(open(DER, encoding='utf-8'))
assert canon(DER) == 'b70fca94d72822ad', canon(DER)

# ---------------------------------------------------------------- LE PLANCHER CORRIGE, DERIVE
N, DP = 18, F(1, 32400)
W2 = ('1.73', '2.27', '2.80')
PROJ4 = 0.2238          # machine 2, derivation_plancher_corrige v3 (mpmath 60 chiffres) : 0.2195 a 0.2238 ; borne haute prise


def coeffs(p, w2):
    a = F(4, p - 2); w = F(w2)
    K = a * (a + 1) * (a + 2) * (a + 3)
    P2 = a * (a + 1) * (a - 1) * (a - 2)
    P4 = (4 - a) * (3 - a) * (2 - a) * (1 - a)
    c1 = (1 + w * w) * a * (a + 1) / ((p - 1) * K - P2)
    c2 = (K * F((p - 1) * (p - 2), 2) * c1 * c1 - (1 + w * w) * c1 * (2 - a) * (1 - a) - w * w) / (P4 - (p - 1) * K)
    return c1, c2


PL = {}
for p in (4, 5, 7):
    vals = []
    for w2 in W2:
        c1, c2 = coeffs(p, w2)
        ref = der['C2']['%d|%s' % (p, w2)]
        assert F(ref['c1']) == c1 and F(ref['c2'][0]) == c2, (p, w2, c1, c2, ref)   # forme close == derivation, EXACT
        td4 = (float(DP) / (1 + float(w2) ** 2)) ** 2
        vals.append(abs(float(c2)) * td4)
    PL[p] = PROJ4 * max(vals)
LEV = 441 / 324
BIA = {p: {w2: der['C4']['%d|%s' % (p, w2)]['0.0']['biais_lnA'] for w2 in W2} for p in (4, 5, 7)}
PRED = {p: {w2: BIA[p][w2] * LEV for w2 in W2} for p in (4, 5, 7)}

# ---------------------------------------------------------------- LE GEL v9
s = open(V8, encoding='utf-8').read()
H = []


def rep(old, new, nom, count=1):
    global s
    c = s.count(old)
    assert c == count, 'GEL %s : %d occurrence(s) de %r' % (nom, c, old[:70])
    s = s.replace(old, new)
    H.append(nom)


# R-v8-5 : le separateur colle
rep('=' * 67 + "5bis. LES MODELES D'AJUSTEMENT", '=' * 71 + "\n\n5bis. LES MODELES D'AJUSTEMENT", 'R-v8-5 separateur')
rep("par les deux machines.\n\n====\n6. LES NOMBRES", "par les deux machines.\n\n" + '=' * 71 + "\n6. LES NOMBRES", 'R-v8-5 rule avant 6')
# R-v8-3 : les comptes
rep("Volet A : identiques au v5 4.5 -- plan 18, G_dt 18, G_k 18, G_seuil 9,\nG_lignee 27 ; `comptes + sautes == 90`.",
    "Volet A : v5 4.5 plus le quatrieme etage -- plan 18, G_dt 18, G_k 18,\nG_dt4 18 (jumelle a dt_2b/4, v14), G_seuil 9, G_lignee 27 ; `comptes +\nsautes == 108`.", 'R-v8-3 section 11')
rep("           comptes + sautes == 90", "           comptes + sautes == 108", 'R-v8-3 en-tete des comptes')
# R-v8-4 : les biais re-derives du JSON de la derivation
old_a = s[s.index("PREDICTION EN AVEUGLE (a) -- LE BIAIS DU PREMIER ORDRE EST PROPORTIONNEL A delta' :"):]
old_a = old_a[:old_a.index("PREDICTION EN AVEUGLE (b)")]
new_a = """PREDICTION EN AVEUGLE (a) -- LE BIAIS DU PREMIER ORDRE EST PROPORTIONNEL A delta' :
  lu sur l'ajustement II sans c1, apres Richardson a ordre mesure, contre
  ln(K/g)/(p-2) : pred(p, w2) = biais_91(p, w2) x 441/324, biais_91 RE-DERIVE du JSON
  de la derivation (C4, decalage 0.0, b70fca94d72822ad), jamais tape :
    p = 4 : %s
    p = 5 : %s
    p = 7 : %s   (lisible sous M2 seulement)
  TIENT au degre si obs_R/pred est dans [0.8, 1.2] aux six points ET |obs_R - pred|
  <= 3 S(p) ; NON sinon. Contre "biais constant" l'ecart est 36 pour cent ; contre
  une loi de modes libres delta'^((alpha+3/2)/2), 26 / 15 / 5 pour cent aux
  p = 4 / 5 / 7 (R3).

""" % tuple(" / ".join("%.6e (w2 %s)" % (PRED[p][w2], w2) for w2 in W2) for p in (4, 5, 7))
rep(old_a, new_a, 'R-v8-4 predictions (a) re-derivees')
# R-v8-2 : la P-A que l instrument calcule
old_pa = s[s.index("CE QUE CES PREDICTIONS NE SONT PAS : une mesure de A (la lecture P-A reste celle"):]
old_pa = old_pa[:old_pa.index("que l'instrument depose, par les deux machines.") + len("que l'instrument depose, par les deux machines.")]
new_pa = """CE QUE LA P-A DEVIENT, TELLE QUE L'INSTRUMENT v15 LA CALCULE (R-v8-2) : a chaque
cellule, a cote de l'ajustement II conserve (lnA_II), l'ajustement CORRIGE
(lnA_M : M1 a p = 4, 5 ; M2 a p = 7, coefficients derives) ; au depouillement,
par point, q MESURE sur les trois niveaux et lnA_R par Richardson (q hors [3, 5]
-> point NON LU, enumere avec son motif) ; par degre, S(p) = max - min des lnA_R,
tol_lnA = max(S(p), plancher_corr(p)) (7bis), G-plancher et P-A lus sur le
COUPLE CORRIGE : P-A vraie au degre si |lnA_R - ln(K/g)/(p-2)| <= tol_lnA aux
points lus. Les grandeurs du v7 (LD-12 : dispersion, tol, G-plancher, P-A) sont
CONSERVEES sous v14_*. Une lecture corrigee absente (moins de deux points lus)
est une CONSIGNE : les grandeurs du v7 restent, le verdict est celui du v7
(D-essai-1). Ce que ces predictions ne sont pas : une mesure de A au sens d'une
valeur -- la P-A est un test ; le second ordre c2 n'entre que par le plancher
7bis. La feuille de lecture deposee avec ce gel (lecture_v9_machine1_v1.py)
joue les deux predictions sur les series que l'instrument depose, par les deux
machines, et RE-DERIVE le biais du 91 du JSON de la derivation."""
rep(old_pa, new_pa, 'R-v8-2 5bis P-A telle que construite')
# R-v8-1 : section 7 sur le couple corrige ; 7bis ; cascade 3.5
i7 = s.index("7. LA PORTE DU PLANCHER (G-plancher) -- la question meme du banc")
i8 = s.index("8. LA CASCADE -- v5 section 9, une branche s'insere")
i8 = s.rindex('=' * 20, 0, i8) if s[i8 - 73:i8].count('=') > 60 else i8
sec7 = """7. LA PORTE DU PLANCHER (G-plancher) -- la question meme du banc, sur le
   COUPLE CORRIGE (R-v8-1)
=======================================================================

Au depouillement du volet A, par degre : tol_lnA(p) = max(S(p), plancher_corr(p)),
S(p) = max - min des six lnA_R (Richardson a ordre mesure sur l'ajustement
corrige), plancher_corr(p) le plancher du terme suivant, derive en 7bis.
G-plancher MORD au degre p si tol_lnA(p) <= plancher_corr(p) -- comparaison de
bord exacte (regle 15). La branche 3b (NON CONCLUANT DE PLANCHER) est lue AVANT
P-A, comme au v5 ; mais elle est lue sur le couple corrige.

Attendu de conception, sur ce que le run 91 a MESURE (jamais sur le 85) : S_M1(4)
= 5.8e-09, S_M1(5) = 3.7e-09, S_M2(7) = 4.4e-09 a n = 21 (Q5, deux machines) ;
transportes a n = 18 par les deux lois (pente mesuree 85 -> 91 ; troncature en
dt^4) ils restent entre 4e-09 et 1e-08. Contre des planchers corriges de
%.1e / %.1e / %.1e, tol_lnA/plancher_corr vaut 1e+04 a 1e+05 : la porte ne
peut mordre que si S(p) s'effondre sous 1e-13, ce qu'un double ne rend pas --
elle redevient un CONTROLE (une morsure y serait un defaut d'instrument, pas
un fait). Les grandeurs du v7 restent lisibles sous v14_* : au 91 elles
mordaient aux trois degres (0.869, 0.208, 0.042), et elles mordraient encore
a n = 18 sous les deux lois de transport (machine 2, certification du v8) --
c'est pourquoi le plancher du v7 ne sert plus de porte.

Cascade 3.5 (v8 3.5 reprise) : si 3b mord sur le couple corrige, le run est
NON CONCLUANT DE PLANCHER et le defaut est d'INSTRUMENT (S sous le plancher
corrige) : pas de v10 de reglage, une lecture du depouillement ; si le pre-vol
BOCAL4 rend branche 4 a n = 18 (il a rendu branche 5, marge 1.868), la cascade
du v7 3.5 s'applique. Un seul pas par run.

7bis. LE PLANCHER CORRIGE -- forme, derivation, portee (machine 2, 18/09 ;
      re-derive par construction ici)
=======================================================================

  Forme close du terme suivant (exacte, Fraction ; verifiee EXACTE aux neuf
  (p, w2) contre la derivation b70fca94d72822ad par ce script) :
    a = 4/(p-2) ; K = a(a+1)(a+2)(a+3) ; P2 = a(a+1)(a-1)(a-2) ;
    P4 = (4-a)(3-a)(2-a)(1-a)
    c1 = (1 + w2^2) a (a+1) / ((p-1) K - P2)
    c2 = [ K (p-1)(p-2)/2 c1^2 - (1 + w2^2) c1 (2-a)(1-a) - w2^2 ] / [ P4 - (p-1) K ]
  Plancher : plancher_corr(p) = proj4 x max_w2 |c2(p, w2)| tau_dom'(w2)^4,
  proj4 le facteur de projection du terme tau^4 sur la fenetre d'ajustement,
  MESURE en precision etendue par machine 2 (derivation_plancher_corrige v3,
  3b12117a58dde698 : 0.2195 a 0.2238 selon le compte de points ; en double le
  terme n'est pas mesurable, il pese 1e-13 contre un bruit de chaine 3e-14).
  Valeur prise : proj4 = %.4f, borne HAUTE de l'intervalle mesure ; machine 1
  ne l'a pas re-derivee (dette declaree : la valeur est celle de machine 2,
  citee par canon, et quatre ordres sous S rendent l'ecart sans portee).
  A n = 18 (delta' = 1/32400) :
    p = 4 : %.4e     p = 5 : %.4e     p = 7 : %.4e
  soit 1e-07 fois le plancher du v7 et 1e-05 fois S(p) du 91. Portee : ce
  plancher borne le terme ANALYTIQUE suivant ; a p = 7 le mode libre est
  AJUSTE par M2, non borne, et ce qui reste apres lui se MESURE au run (S(p)
  le porte). Rien ici ne promet davantage.

""" % (PL[4], PL[5], PL[7], PROJ4, PL[4], PL[5], PL[7])
s = s[:i7] + sec7 + s[i8:]; H.append('R-v8-1 section 7 et 7bis')
# section 10 : instrument v15
rep("10. L'INSTRUMENT v14 -- DU AVANT TOUT RUN", "10. L'INSTRUMENT v15 -- DU AVANT TOUT RUN", 'H section 10 titre')
rep("Part du v13 CERTIFIE (banc_qualification_machine1_v13.py 1ac295648490a86c,\ncertification machine 2 24/24 ; v10-v13 : D-v9-1, D-v10-1, D-v11-1, D-v12-1\nlevees), construit par construction_gel_v8_banc_v14_machine1_v1.py -- le meme\nscript que ce gel -- qui ajoute UN etage : la jumelle a dt_2b/4 (cle G_dt4,\nseries _dt2s4_k2, intervalles x4), sans toucher aux verdicts (G-dt lit toujours\ndt contre dt/2) ; et :",
    "Part du v14 CERTIFIE (banc_qualification_machine1_v14.py dc91676c640d4323,\ncertification machine 2 45de25ac61321661 : selftest 103/103, banc 56/56, pre-vols\nbranche 5 sur BOCAL4), construit par construction_gel_v9_banc_v15_machine1_v1.py\n-- le meme script que ce gel -- qui porte la lecture CORRIGEE dans l'instrument\n(prescription machine 2 du 18/09, essai hors depot 0dcfd901a0551d0f, ses trois\nremplacements repris tels quels) : c1 et c2 en forme close, ajuster_corrige\n(M1/M2, meme fenetre, meme t*), richardson_q a ordre MESURE, plancher_corrige a\nproj4 DERIVE (D-essai-3), lnA_M a chaque cellule, G-plancher et P-A sur le couple\ncorrige, v14_* conserves, lecture absente consignee NON JOUEE (D-essai-1) ; et\nDEUX scenarios neufs du banc qui tue qui exercent ce chemin par MUTATION des lnA_M\n(D-essai-2 : les series synthetiques sont exactes en dt, q y est indefini, la\nlecture corrigee y est NON JOUEE et consignee -- le pre-vol ne l'exerce pas, le\nbanc si) ; G22 nomme le plancher qu'il exerce (v14). Le v14 avait ajoute l'etage\ndt_2b/4 (G_dt4) ; et :", 'H section 10 v15')
rep("Le v14 se re-certifie EN ENTIER par machine 2 (selftest, banc qui tue,\nNE-JOUE-PAS) et son pre-vol se joue des deux cotes au reglage v8 avant tout\nrun.",
    "Le v15 se re-certifie EN ENTIER par machine 2 (selftest, banc qui tue -- 58\nscenarios --, NE-JOUE-PAS) et son pre-vol se joue des deux cotes au reglage v9\n(= v8 : n = 18) avant tout run.", 'H section 10 certif v15')
# en-tete
old_head = s[:s.index('# Banc de verification (N-69')]
new_head = """# PRE-ENREGISTREMENT constante A v9 -- LE TERME DU PREMIER ORDRE EST DERIVE ; CE
# GEL LE TESTE EN AVEUGLE PAR SA PROPORTIONNALITE A delta' (n = 18, levier 441/324),
# PRE-ENREGISTRE LES MODES LIBRES A p = 7, ET PORTE LA P-A CORRIGEE DANS L'INSTRUMENT
# BROUILLON MACHINE 1 -- DEVIENT GEL A LA CERTIFICATION MACHINE 2
# v9 = v8 (800fc6a9a8e56e49, NON CERTIFIE par machine 2 -- 45de25ac61321661, cinq
# reprises --, REMPLACE, non edite) + les reprises, appliquees par
# construction_gel_v9_banc_v15_machine1_v1.py :
#   R-v8-1  section 7 sur le COUPLE CORRIGE ; attendu sur les dispersions du 91 ;
#           cascade 3.5 reprise ; section 7bis neuve : le plancher corrige (forme
#           close de c2, proj4 mesure par machine 2, valeurs a n = 18).
#   R-v8-2  5bis : la P-A est ce que l'instrument v15 calcule (arbitrage operateur du
#           18/09 : la voie longue) ; v14_* conserves ; lecture absente = consigne.
#   R-v8-3  section 11 : 108, le quatrieme etage nomme.
#   R-v8-4  les biais du 91 RE-DERIVES du JSON de la derivation, par (p, w2).
#   R-v8-5  le separateur de 5bis decolle de son titre.
#   H       section 10 : instrument v15 ; section 13 : les pieces du 18/09.
# Le reglage (n = 18), les modeles, Richardson a ordre mesure, les deux predictions
# en aveugle et Q5 sont INCHANGES : rien de ce qui mordait ne les touchait.
"""
s = s.replace(old_head, new_head); H.append('H0 en-tete')
s = s.replace("lecture_v8_machine1_v1.py", "lecture_v9_machine1_v1.py"); H.append('H feuille v9')
s = s.replace("-- FIN constante_A_pre_enregistrement_v8 --", """    constante_A_pre_enregistrement_v8.md               800fc6a9a8e56e49  REMPLACE (non certifie)
    note_machine2_certification_v8_v14_v1.md           0e3aa516ad021159  (lot 45de25ac61321661)
    POUR_MACHINE1_prescription_PA_dans_instrument_machine2_v1.md  b86f25c573fd5b05  (lot 289ae2620e1d1063)
    derivation_plancher_corrige_machine2_v3.py / .json b0e107f45e0bc17b / 3b12117a58dde698
    essai_correctif_PA_hors_depot_machine2.py          0dcfd901a0551d0f  (les trois remplacements)
    banc_qualification_machine1_v14.py                 dc91676c640d4323  CERTIFIE, REMPLACE PAR LE v15

-- FIN constante_A_pre_enregistrement_v9 --"""); H.append('H section 13 et FIN')
assert all(c < 128 for c in s.encode())
GEL = os.path.join(OUT, 'constante_A_pre_enregistrement_v9.md')
open(GEL, 'w', encoding='utf-8', newline='\n').write(s)
print('GEL v9 : %d hunks ; canon %s ; %d octets ; planchers corriges %s' % (len(H), canon(GEL), os.path.getsize(GEL), {p: '%.3e' % v for p, v in PL.items()}))

# ---------------------------------------------------------------- LE BANC v15
b = open(V14, encoding='utf-8').read()
HB = []


def repb(old, new, nom, count=1):
    global b
    c = b.count(old)
    assert c == count, 'BANC %s : %d occurrence(s) de %r' % (nom, c, old[:70])
    b = b.replace(old, new)
    HB.append(nom)


ESSAI = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'essai_correctif_PA_hors_depot_machine2.py')
assert canon(ESSAI) == '0dcfd901a0551d0f', 'essai machine 2 absent ou modifie'
ns = {}
src_essai = open(ESSAI, encoding='utf-8').read()
i_a = src_essai.index("AIDES = '''"); i_r = src_essai.index("REMPLACEMENTS = [")
exec(src_essai[i_a:i_r], ns)          # ne definit que AIDES et BLOC_C (des chaines), sans rien executer d'autre
AIDES, BLOC_C = ns['AIDES'], ns['BLOC_C']
AIDES = AIDES.replace("# CORRECTIF D ESSAI (machine 2, hors depot) : la lecture CORRIGEE portee dans l instrument.",
                      "# v15 (machine 1, sur prescription machine 2 du 18/09, essai 0dcfd901a0551d0f repris tel quel) :\n# la lecture CORRIGEE portee dans l instrument.")
AIDES = AIDES.replace('    """Borne DERIVEE du terme suivant : max_w2 |c2(p,w2)| tau_dom\'(w2)^4, proj4 <= 1."""\n    return max(abs(float(coeffs_c1_c2(p, w2)[1])) * tau_dom(w2) ** 4 for w2 in W2S)',
                      '    """Plancher DERIVE du terme suivant : PROJ4 x max_w2 |c2(p,w2)| tau_dom\'(w2)^4 (gel v9, 7bis ; D-essai-3)."""\n    return PROJ4 * max(abs(float(coeffs_c1_c2(p, w2)[1])) * tau_dom(w2) ** 4 for w2 in W2S)')
assert 'PROJ4 *' in AIDES
AIDES = AIDES.replace("FREQ_MODE_LIBRE = {", "PROJ4 = %.4f   # machine 2, precision etendue : 0.2195 a 0.2238 ; borne haute (gel v9, 7bis)\nFREQ_MODE_LIBRE = {" % PROJ4)
BLOC_C = BLOC_C.replace("# --- CORRECTIF D ESSAI : la lecture CORRIGEE (machine 2, hors depot) ---", "# --- v15 : la lecture CORRIGEE (gel v9, 5bis et 7 ; essai machine 2 0dcfd901a0551d0f) ---")
BLOC_C = BLOC_C.replace("# --- fin du correctif d essai ---", "# --- fin v15 ---")
repb('def ajuster_point_fixe(t, x, w2, p, dt):', AIDES + '\ndef ajuster_point_fixe(t, x, w2, p, dt):', 'H-a aides (machine 2)')
repb('    aj = ajuster_point_fixe(ph2["t"], x, w2, p, dt2)\n    rec["ajustement"] = aj',
     '    aj = ajuster_point_fixe(ph2["t"], x, w2, p, dt2)\n    rec["ajustement"] = aj\n    rec["ajustement_corrige"] = ajuster_corrige(ph2["t"], x, w2, p, dt2)', 'H-b lnA_M a chaque cellule (machine 2)')
repb('            D["P_A"] = all(abs(math.log(v)) <= (p - 2) * D["tol_lnA"] for v in ratios.values())',
     '            D["P_A"] = all(abs(math.log(v)) <= (p - 2) * D["tol_lnA"] for v in ratios.values())\n' + BLOC_C, 'H-c couple corrige (machine 2)')
# D-essai-2 : le banc exerce la lecture corrigee par mutation
repb('    def jouer_synth(sy):\n        compteur = {"comptes": 0, "sautes": 0, "sautes_noms": []}',
     '    def jouer_synth(sy, mut=None):\n        compteur = {"comptes": 0, "sautes": 0, "sautes_noms": []}', 'B-D2a jouer_synth(mut)')
repb('        return lire_alpha(plan, gdt, gk, seuil, lignee, e_req, gdt4=gdt4), compteur\n',
     '        if mut:\n            mut(plan, gdt, gdt4)          # v15 : mutation des lnA_M AVANT le depouillement\n        return lire_alpha(plan, gdt, gk, seuil, lignee, e_req, gdt4=gdt4), compteur\n', 'B-D2b mutation')
repb('    n_att_a = sum(compte_attendu_alpha().values())\n',
     '''    # -- v15 : la lecture CORRIGEE, exercee par MUTATION des lnA_M (les series synthetiques sont
    #    exactes en dt : q y est indefini, la lecture corrigee y est NON JOUEE et consignee)
    def _mut_lnA_M(plan, gdt, gdt4, f0, f1, f2, eps=1e-6):   # eps grand devant l'ulp de 1.0 : q se mesure a 1e-9 pres
        for cle in plan:
            for cell, f in ((plan, f0), (gdt, f1), (gdt4, f2)):
                if cle in cell and isinstance(cell[cle].get("ajustement_corrige"), dict):
                    cell[cle]["ajustement_corrige"]["lnA_M"] = 1.0 + f * eps
    L_q4, _ = jouer_synth(SynthAlpha(s_etoile), mut=lambda pl, g1, g4: _mut_lnA_M(pl, g1, g4, 16.0, 1.0, 1.0 / 16.0))
    v, bq = cascade_alpha(L_q4)
    q_ok = all(abs(qq - 4.0) < 1e-6 for p in DEGRES for qq in L_q4["degres"][p].get("q_mesure", {}).values()) and \\
        all(len(L_q4["degres"][p].get("lnA_R", {})) == 6 for p in DEGRES)
    scenario("G35 lecture corrigee : q = 4 MESURE aux 18 points et S_p = 0 -> G-plancher CORRIGE MORD -> branche 3b",
             q_ok and v == "NON CONCLUANT DE PLANCHER" and all(L_q4["degres"][p]["G_plancher_mord"] for p in DEGRES),
             "%s ; q %s ; S_p %s" % (v, ["%.3f" % qq for p in DEGRES for qq in list(L_q4["degres"][p].get("q_mesure", {}).values())[:1]],
                                    ["%.1e" % (L_q4["degres"][p].get("S_p") or -1) for p in DEGRES]), gardes=("G-plancher",))
    L_q2, _ = jouer_synth(SynthAlpha(s_etoile), mut=lambda pl, g1, g4: _mut_lnA_M(pl, g1, g4, 4.0, 1.0, 1.0 / 4.0))
    v2_, b2_ = cascade_alpha(L_q2)
    L_ref, _ = jouer_synth(SynthAlpha(s_etoile))
    v0_, b0_ = cascade_alpha(L_ref)
    scenario("G36 lecture corrigee : q = 2 mesure -> 18 points NON LUS, lecture NON JOUEE, verdict du v14 inchange",
             v2_ == v0_ and all(len(L_q2["degres"][p].get("points_non_lus", [])) == 6 and
                                str(L_q2["degres"][p].get("lecture_corrigee", "")).startswith("NON JOUEE") for p in DEGRES),
             "%s == %s ; non lus %s" % (v2_, v0_, [len(L_q2["degres"][p].get("points_non_lus", [])) for p in DEGRES]), gardes=())
    n_att_a = sum(compte_attendu_alpha().values())
''', 'B-D2c scenarios G35 et G36')
repb('scenario("G22 decalage lnA nul : dispersion sous le plancher\' -> G-plancher MORD -> branche 3b",',
     'scenario("G22 decalage lnA nul : dispersion sous le plancher\' du v14 (LD-12 ; la lecture corrigee y est NON JOUEE) -> G-plancher MORD -> branche 3b",', 'B-G22 nomme')
repb('GEL_ALPHA = ("gels/constante_A_pre_enregistrement_v8.md", "800fc6a9a8e56e49", 46050)',
     'GEL_ALPHA = ("gels/constante_A_pre_enregistrement_v9.md", "%s", %d)' % (canon(GEL), os.path.getsize(GEL)), 'B pin v9')
repb('VERSION = "banc_qualification_machine1_v14"', 'VERSION = "banc_qualification_machine1_v15"', 'B VERSION')
repb("DE LA CONSTANTE A (delta' = 1/32400 ; v14 = v13 certifie + etage dt_2b/4 (cle G_dt4), reglage n = 18, pin gel v8,",
     "DE LA CONSTANTE A (delta' = 1/32400 ; v15 = v14 certifie + la lecture CORRIGEE dans l'instrument (gel v9 5bis, 7, 7bis ;\nessai machine 2 0dcfd901a0551d0f), deux scenarios G35/G36, pin gel v9, construction_gel_v9_banc_v15_machine1_v1.py ;\nv14 = v13 certifie + etage dt_2b/4 (cle G_dt4), reglage n = 18,", 'B en-tete')
assert all(c < 128 for c in b.encode())
BANC = os.path.join(OUT, 'banc_qualification_machine1_v15.py')
open(BANC, 'w', encoding='utf-8', newline='\n').write(b)
print('BANC v15 : %d remplacements ; canon %s' % (len(HB), canon(BANC)))
json.dump({"planchers_corriges_n18": {str(p): PL[p] for p in PL}, "proj4": PROJ4, "predictions_a": {str(p): PRED[p] for p in PRED}},
          open(os.path.join(OUT, 'derives_v9.json'), 'w'), indent=1)
