#!/usr/bin/env python3
# -*- coding: ascii -*-
"""CONSTRUCTION DU GEL constante A v11 (depuis le v10 130ba949482129a7, CERTIFIE 996dc8be7d245387) ET DU
BANC v17 (depuis le v16 634c4aaa2aad7598, CERTIFIE ; pin et version seuls). machine 1, v1, 29/09/2026.
Reprises de la certification m2 du v10/v16 : E-v10-1 (la base du 92 se verifie par sa TABLE, a 1e-15,
depuis n'importe quel poste, a 1e-12 (l'arrondi de la table) -- plus par le canon d'un JSON ajuste) ; E-v10-2 (les
hunks se comptent appliques ET sans ancre, declares) ; et le FAIT DE FOND : ce que le v10 appelait
incertitude est un SYSTEMATIQUE DE FENETRE, borne et non retire -- ecrit tel quel, avec une prediction
(d) sur son signe. Rien n'est edite.
Usage : <v10.md> <v16.py> <base_92.json (n'importe quel poste)> <sortie>
"""
import hashlib, json, math, os, re, sys, unicodedata

V10, V16, BASE, OUT = sys.argv[1:5]
os.makedirs(OUT, exist_ok=True)


def canon(p):
    raw = open(p, 'rb').read()
    return hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()).hexdigest()[:16]


assert canon(V10) == '130ba949482129a7', canon(V10)
assert canon(V16) == '634c4aaa2aad7598', canon(V16)
s = open(V10, encoding='utf-8').read()
# E-v10-1 : la base par sa TABLE -- la table typee au v10 (6 lignes) contre le JSON fourni, a 1e-15 absolu
base = json.load(open(BASE, encoding='utf-8'))['modes_p7']
rows = re.findall(r'\n    (7\|\d\.\d\d\|\d\.\d\d)\s+([+-]\d\.\d{6}e[+-]\d\d)\s+([+-]\d\.\d{6}e[+-]\d\d)\s+(\d\.\d{6}e[+-]\d\d)\s+([+-]\d\.\d{4})', s)
assert len(rows) == 6, len(rows)
for cle, a_, c_, amp, ph in rows:
    assert abs(float(a_) - base[cle]['a']) <= 1e-12 and abs(float(c_) - base[cle]['c']) <= 1e-12, (cle, a_, c_, base[cle])   # 1e-12 : arrondi de la table (7 chiffres) ; les deux machines sont a 1.9e-16
H, manques = [], []


def rep(old, new, nom, count=1, must=True):
    global s
    c = s.count(old)
    if c != count:
        if must:
            raise AssertionError('GEL %s : %d occurrence(s) de %r' % (nom, c, old[:70]))
        manques.append('%s (%d)' % (nom, c)); return
    s = s.replace(old, new); H.append(nom)


rep("  20 pour cent et 0.3 rad. Base du 92, (a, c) apres Richardson a ordre mesure (machine 1,\n  lecture v9 af295b8a660d33e8 ; les memes a 1e-16 chez machine 2) :",
    "  20 pour cent et 0.3 rad. Base du 92, (a, c) apres Richardson a ordre mesure -- la TABLE\n  fait foi (E-v10-1) : elle se reproduit a 1.9e-16 entre les deux machines, les canons des JSON\n  ajustes (af295b8a660d33e8 chez machine 1) sont machine-dependants et ne sont pas des ancres :", 'E-v10-1 base par table')
i0 = s.index("LA MESURE DE A (ce que ce gel appelle mesurer)")
i1 = s.index("CE QUE LA P-A EST, TELLE QUE L'INSTRUMENT v16 LA CALCULE")
mesure = """LA MESURE DE A (ce que ce gel appelle mesurer) : par point, lnA_R (Richardson a ordre
  mesure sur M1/M2) ; par degre, delta_p = moyenne des six (lnA_R - ln(K/g)/(p-2)) et
  S(p) = max - min des six lnA_R ; A(p) = (K/g)^(1/(p-2)) exp(delta_p). CE QUE S(p) EST
  (certification machine 2 du v10, ce_qui_borne_A fb4163b7893c5070, 7 controles ; rejoue
  par machine 1 sur ses propres series du 92) : ni le plancher analytique (quatre a cinq
  ordres plus bas), ni du bruit (l'effet de c se reproduit AU BIT entre les deux machines,
  8 cas sur 9, l'exception etant la cellule exposee 4|2.27) : un SYSTEMATIQUE DE FENETRE,
  deterministe. Au 92, sous M1 a p = 4 et 5, l'ecart lnA_R(c = 1.20) - lnA_R(c = 1.05) est
  POSITIF aux six (p, w2) (+2.3e-09, +2.8e-09, +6.1e-10 ; +3.6e-09, +2.1e-09, +1.8e-10 chez
  machine 1) : une dependance monotone en c ne se centre pas en moyennant deux c, la valeur
  vraie est au-dela du couple, et A(p) porte un biais de fenetre de l'ordre de 1.6e-09, sept
  a neuf fois le delta_p mesure. A p = 7 sous M2 les signes sont meles. Et SOUS M2 A p = 4
  ET 5 L'EFFET NE DISPARAIT PAS (machine 1, a posteriori : +5.3e-09, +4.8e-09, +1.2e-09 ;
  +6.4e-09, +8.5e-10, -1.2e-10, S double) : ce n'est pas le mode libre qui le porte a ces
  degres, c'est la composition de la fenetre, et l'ajuster n'y change rien.
  DONC : A(p) est rendu avec une BORNE DE SYSTEMATIQUE S(p) + plancher_corr(p) en lnA, pas
  une incertitude statistique ; le biais est BORNE, non retire. Ce gel ne le retire pas :
  le retirer est un chantier (extrapolation en c par un troisieme indice, prescription
  machine 2 ; ou moyenne sur le decalage de grille, comme C4 l'a mesure a 1.3 pour cent)
  qui se decide APRES ce run, sur ses trois niveaux.
  PREDICTION EN AVEUGLE (d) -- LE SIGNE DU SYSTEMATIQUE : a n = 21, sous M1 a p = 4 et 5,
  les six ecarts lnA_R(1.20) - lnA_R(1.05) sont de MEME SIGNE, positif ; a p = 7 sous M2
  ils ne le sont pas. TIENT / NON par degre. (Un signe unique sur six a 1/32 de chance
  d'etre fortuit ; c'est la reproductibilite d'un systematique qui est testee, pas sa
  cause.) P-A corrigee reste le test de la relation : vraie au degre si
  |lnA_R - ln(K/g)/(p-2)| <= tol_lnA(p) aux points lus. Au 92 (n = 18, a posteriori pour ce
  gel) : S(p) = 4.47e-09 / 3.72e-09 / 3.52e-09 (BOCAL4), P-A vraie aux trois, A(p) a 2e-10
  a 3e-10 du theorique -- SOUS le systematique.

"""
s = s[:i0] + mesure + s[i1:]; H.append('FOND mesure de A : systematique de fenetre, prediction (d)')
old_head = s[:s.index('# Banc de verification (N-69')]
new_head = """# PRE-ENREGISTREMENT constante A v11 -- MESURER A AU BARREAU DU 91 (n = 21), AVEC CE QUE
# LA MESURE PORTE : UN SYSTEMATIQUE DE FENETRE BORNE, NON RETIRE, ET SON SIGNE PREDIT ;
# QUATRE PREDICTIONS EN AVEUGLE (a, b, c, d)
# BROUILLON MACHINE 1 -- DEVIENT GEL A LA CERTIFICATION MACHINE 2
# v11 = v10 (130ba949482129a7, CERTIFIE des deux cotes -- 996dc8be7d245387 --, REMPLACE,
# non edite) + les hunks de construction_gel_v11_banc_v17_machine1_v1.py :
#   E-v10-1  la base du 92 se verifie par sa TABLE (six lignes, 1e-12) depuis n'importe
#            quel poste, a 1e-12 ; le canon d'un JSON ajuste n'est plus une ancre.
#   E-v10-2  le compte des hunks du v10 etait "41" : 38 appliques et 3 fragments sans ancre
#            (h19, h20, s12 : leur texte n'existait plus dans le v9), benins, ici declares.
#   FOND     5bis, la mesure de A : S(p) est un systematique de fenetre (fait de machine 2,
#            rejoue par machine 1, y compris sous M2 a p = 4, 5 ou il ne disparait pas) ;
#            A(p) est rendu avec une BORNE, pas une incertitude ; prediction (d) neuve sur
#            le signe du systematique ; le retrait du biais est un chantier d'apres-run.
# Le v10 et le v16 ne portaient rien de faux (certification : 39 controles, 0 morsure) ;
# le v11 dit ce que le v10 ignorait. Reglage, modeles, Richardson, (a), (b), (c) :
# inchanges. Instrument v17 = v16 certifie + pin et version, aucun code.
"""
s = s.replace(old_head, new_head); H.append('H0 en-tete')
rep("10. L'INSTRUMENT v16 -- DU AVANT TOUT RUN", "10. L'INSTRUMENT v17 -- DU AVANT TOUT RUN", 'H titre 10')
rep("Le v16 se re-certifie EN ENTIER par machine 2", "Le v17 (= v16 certifie + pin v11 et version, aucun code) se re-certifie EN ENTIER par machine 2", 'H certif v17')
s = s.replace("lecture_v10_machine1_v1.py", "lecture_v10_machine1_v1.py (inchangee : elle joue (d) par ses lnA_R)"); H.append('H feuille')
s = s.replace("-- FIN constante_A_pre_enregistrement_v10 --", """    constante_A_pre_enregistrement_v10.md              130ba949482129a7  REMPLACE (certifie)
    POUR_MACHINE1_certification_v10_v16_machine2_v1.md 4f856a34d6e887a8  (lot 996dc8be7d245387)
    ce_qui_borne_A_machine2_v1.py / .log / .json       ed5bbce867f0a41d / fb4163b7893c5070 / 55532af50289e38a
    banc_qualification_machine1_v16.py                 634c4aaa2aad7598  CERTIFIE, REMPLACE PAR LE v17
    registre : delta 92 depose, HEAD 09baf5c (268 pieces, releve machine 1 : 73/73 citations au registre)

-- FIN constante_A_pre_enregistrement_v11 --"""); H.append('H section 13 et FIN')
assert all(c < 128 for c in s.encode())
GEL = os.path.join(OUT, 'constante_A_pre_enregistrement_v11.md')
open(GEL, 'w', encoding='utf-8', newline='\n').write(s)
print('GEL v11 : %d hunks appliques ; sans ancre : %s ; canon %s ; %d octets' % (len(H), manques or 'aucun', canon(GEL), os.path.getsize(GEL)))
b = open(V16, encoding='utf-8').read()
old_pin = 'GEL_ALPHA = ("gels/constante_A_pre_enregistrement_v10.md", "130ba949482129a7", %d)' % os.path.getsize(V10)
assert b.count(old_pin) == 1, old_pin
b = b.replace(old_pin, 'GEL_ALPHA = ("gels/constante_A_pre_enregistrement_v11.md", "%s", %d)' % (canon(GEL), os.path.getsize(GEL)))
assert b.count('VERSION = "banc_qualification_machine1_v16"') == 1
b = b.replace('VERSION = "banc_qualification_machine1_v16"', 'VERSION = "banc_qualification_machine1_v17"')
old_h = "DE LA CONSTANTE A (delta' = 1/44100 ; v16 = v15 certifie + M1c/M2c a c1 libre (gel v10 5bis (c)), reglage n = 21, pin gel v10,"
assert b.count(old_h) == 1
b = b.replace(old_h, "DE LA CONSTANTE A (delta' = 1/44100 ; v17 = v16 certifie + pin gel v11 et version, aucun code ; v16 = v15 certifie + M1c/M2c a c1 libre (gel v10 5bis (c)), reglage n = 21,")
assert all(c < 128 for c in b.encode())
BANC = os.path.join(OUT, 'banc_qualification_machine1_v17.py')
open(BANC, 'w', encoding='utf-8', newline='\n').write(b)
print('BANC v17 : 3 remplacements (pin, version, en-tete) ; canon %s' % canon(BANC))
