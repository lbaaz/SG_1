#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
m17_chaine_v17.py -- manche M17, estimateur quantique de chaine (p=5, site 2:1)
==============================================================================
Version 17. Repond a : note_machine2_RETRAIT_certification_v16_m17_v1
(copie recue 85537791102f3ae1) -- LA CERTIFICATION v16 EST RETIREE dans
l'heure : mon balayage de temoins_P7 ("premier w2 qui matche") etait
ecrit pour un dossier ideal, pas pour celui qu'un RUN PRODUIT -- quatre
fichiers au w2 nominal, le tri ASCII place P8 avant f070, le P8 a
g = 3e-4 est E-B INFAISABLE sans L_retenu : NON EVALUABLE, P7_sain
False, LA MANCHE ENTIERE en ARRET DE REGLE apres cinq heures. Famille
M14 / D-M17-31 ; le pre-vol machine 2 a mordu AVANT le pilote, zero
temps moteur perdu. CORRECTIF (prescription machine 2, jouee 7/7,
appliquee AU MOT) : on ne BALAYE pas, on NOMME -- _chemin_point, la
fonction meme que mesurer_manche emploie pour ECRIRE le point ;
l'ordre des noms d'un dossier ne decide plus de rien ; fail-closed
conserve. PLUS LES DEUX PROSES consignees a la certification retiree :
la ligne 4 (le jumeau se nommait v15 -- D-M17-35 defait par ma propre
main une version plus tard) et la RESOLUTION DU DENOMINATEUR, ECRITE
au docstring de temoins_P7 (E29 : le denominateur est PAR CELLULE, le
signal re-mesure a la geometrie de chaque cellule -- cout une
diagonalisation de plus par cellule, ecart mesure 3.69 pour cent,
meme verdict, homogeneite retenue en attendant l'acte). RIEN D'AUTRE.
Version 16. Repond a : note_machine2_certification_gel_v12b2_m17_v1.md
(GEL v12-b2 CERTIFIE 20950e52e7d63225, copie recue de6f702f0d4b052e) --
LES QUATRE consequences d'instrument, section 4 :
[RA] RE-ANCRAGE vers 20950e52e7d63225, code ET fragment (troisieme
re-ancrage du jour : la lecon ne s'oublie plus, elle s'execute).
[TRAD] la porte de POSITION : v_rc = gamma_LS(N + p, ..., r_c + p) --
la TRANSLATION du gel v11, L conserve ; correctif deja joue machine 2
(le nominal devient EN DOMAINE).
[NOM] la cle 'rc_plus_p' devient 'translation_p' (proposition
machine 2, retenue : une cle dit ce que le code fait). Rien ne la
lisait par son nom ; l'assembleur est inchange.
[P7] temoins_P7 REECRIT a la clause du gel v12-b2 -- code neuf :
MODULE, seuil RELATIF 1e-2 x Gamma_LS(H) du MEME point et de la MEME
geometrie, DEUX cellules lues PAR TRANSLATION, monotonie RETIREE ;
le L est LU de l'artefact du point (jamais re-derive de la formule
remplacee) ; sans artefact ou sans L retenu : NON EVALUABLE et
P7_sain = False (fail-closed, D-S2). Le fondement de marge vit au
gel : pire cellule jouee L = 30, 10.7 x (certification v12-b2,
section 2 -- le 11.7 de la prose du gel se corrige a l'acte).
Version 15. Repond a : note_machine2_contrecert_v14_m17_v1.md (NON
CERTIFIE, copie recue 5292c217db83449d) -- QUATRE gestes, rien d'autre :
[D-M17-31] mesurer_point : l'indexation nue de G9_mordue (la SOEUR que
la parade de la v12 avait a moitie couverte -- .get sur stationnarites,
pas sur G9) passe en .get : un point rejete a L = 30 sort par la
CASCADE au lieu de tuer la boucle de manche. Correctif machine 2, JOUE
par elle, applique au mot.
[D-M17-32] SORTIE (a) RETENUE : l'extrapolation de 4.6 est PAR LE
RATIO MESURE (rich = G + (G - G_prec) * r / (1 - r)), celle que
l'instrument de la sonde de direction rend et que le gel v10 cite
(2.157522e-10 au nominal, reproduit a 2.7e-08 -- N-63) ; le couple
(Richardson, residu_declare) devient coherent. DECLARE : la campagne
porte DEUX extrapolations sous le meme mot -- 4.7/E-A dit 2b - a,
4.6/E-B dit par-le-ratio -- la difference est ECRITE ici et va a
l'acte.
[D-M17-35] deux residus de prose herites corriges : le nom du jumeau
(l.4, v8 depuis l'origine) et le bloc E19 du docstring qui disait
encore "ne cite PAS l'empreinte du gel" -- faux depuis la v11.
Version 14. Repond a : note_machine2_certification_gel_v10_m17_v1.md,
section 9 -- TROIS ordres de script decoulant de l'erratum 4.6 (gel v10
CERTIFIE 96076b26be766304), dans l'ordre de contrainte :
[RA] RE-ANCRAGE : GEL_EMPREINTE -> 96076b26be766304, code ET fragment
(le sixieme site, troisieme passage) -- sans lui rien n'est opposable
sous la v10 (E19).
[GEO] GEOMETRIE PAR POINT (4.6) dans executer_EB : L fixe par le
critere d'absorbeur -- descente en eta a trois pas (eta/2, /4, /8),
les DEUX DERNIERS < tau_LS -- essai a L = 20 (nominal) puis L = 30 ;
rejet a 30 = descente_rejetee_L30, motif par la CASCADE (E36).
Operatif 4.6 consigne : eta final, Gamma, r (paire E34 :
dernier/precedent, pas joues), RICHARDSON meme paire, RESIDU declare.
Stationnarites-PORTES restantes : rc_plus_p, N_plus_p (a eta final).
La MONTANTE eta -> 2 eta : TEMOIN NOMME consigne, jamais un arret.
[POND] TAUX (directive) : gamma_LS rend Gamma_pondere =
somme(|c_nu|^2 Gamma_nu) sur les resonances retenues a poids cumule
>= SEUIL_POIDS_TAU (G-5, 0.99), avec poids_cumule et n_resonances ;
les trois sorties historiques sont INCHANGEES AU BIT (l'etat de plus
grand recouvrement devient temoin par le gel, sa valeur reste rendue).
Version 13. Repond a : POUR_MACHINE1_ordre_Q3_v13.md -- ORDRE DE
L'OPERATEUR : inscrire E35 (Q3). E35 est OPPOSABLE depuis le depot du
delta 81 (main 2c09fff) et son texte dit "occupations REELLES" ;
occupations_graine ne porte que deux lectures, E35 en nomme une. DEUX
lignes, pas une : le code (l.180) ET le fragment de docstring (l.28),
que la garde D-S1 matche par son mot `reste` -- piege paye par machine 2
AVANT l'ordre (N-53), deuxieme fois que le script enumere lui-meme un
site qu'un ordre avait manque. Forme CANONIQUE au fragment, sans
guillemets (convention du sixieme site des ancres). RESIDU COSMETIQUE
DECLARE, non touche : les trois lignes de commentaire de continuation
sous la constante (l.181-183) deviennent orphelines de leur phrase --
aucune ne mord aucune garde, et les corriger excederait l'ordre.
RIEN D'AUTRE : aucun nombre ne bouge (bit-verifie), la manche MESURE.
Version 12. Repond a : note_machine2_prevol_v11_m17_v1.md, section 4 --
UN ARRET QUI SORT PAR EXCEPTION (KeyError('w2') a l'assemblage sur tout
point en arret legitime, ex. ARRET Q3). Regle D-P3/E36 : un chemin
d'arret sort par la CASCADE, jamais par exception -- la faute de l'ex
aequo (v8) se representait sous une autre peau. Prescription machine 2
appliquee : un point SANS w2 ne s'INDEXE pas, il se CONSIGNE
(arrets_sans_index : fichier, statut, motif) et la cascade prononce ;
terme ajoute EN FIN de l'arret. ETENDU A LA FAMILLE, declare : la
branche P8 mourait de meme (sort key d['g'] evaluee avant tout filtre) ;
la garde d'ingestion, posee APRES la branche site, couvre les deux.
Q3 (LECTURE_OCCUPATIONS) N'EST PAS TOUCHEE : decision de gel, E35
opposable, l'inscription attend l'ordre -- l'etendre ici serait E29.
Version 11. Repond a : certification v10 section 5 (ea93c063c6d69bf1) et
bon pour depot 81 v1. LE DELTA 81 EST DEPOSE (operateur) : les numeros
E33..E36 sont opposables, le verrou E18 tombe. UN SEUL GESTE, aux valeurs
fixees AU CARACTERE par la certification : les CINQ ancres consignees --
GEL_EMPREINTE (E19) et les quatre cles Q1..Q4 -- PLUS UN SITE que le
perimetre fixe ne listait pas et que la garde D-S1 (fragments
perimes) a ENUMERE MECANIQUEMENT en refusant de tourner : le
fragment l.95 du docstring, qui declarait encore None, suit la
constante qu'il cite. RIEN D'AUTRE : aucune
constante, aucun chemin de calcul, aucune garde ne bouge (bit-verifie).
LECTURE_OCCUPATIONS reste reelle : hors des cinq valeurs fixees, toute
mesure l'exige explicite -- l'etendre serait E29.
Version 10. Repond a : note_machine2_contrecert_v9_m17_v1.md (verdict
NON CERTIFIE, un defaut : D-M17-30, racine dans l'ordre -- temoins_P7,
SIXIEME site de la couche E-B, portait P en dur ; unique appelant de la
branche abs_x5, la parametrisation v9 y etait correcte et INATTEIGNABLE).
Leve ici, prescription machine 2 appliquee AU MOT (p=P en fin, N et les
deux appels gamma_LS suivent p). Reserve 2 TRANCHEE EN LA DECLARANT :
le site d'appel du mode --run reste au defaut p=P -- la manche EST
p = 5 ; p s'expose au banc par la fonction. Reserve 1 (B_N suit-il p ?)
NON tranchee : question de gel, a la file de l'acte. Test v10 : aux
jambes de la v9 s'ajoute la jambe de MUTATION (regle proposee par la
contre-cert) -- les six fonctions E-B enumerees MECANIQUEMENT par l'AST
(zero P en corps hors defaut), et chaque primitive BOUGE a p = 4.
AUCUNE ancre inscrite (81.6).
Version 9. Repond a : POUR_MACHINE1_ordre_v9_script_m17.md (ordre emis
sur l'acte 80 DEPOSE, 80.7). D-B2 : p devient PARAMETRE nomme en fin de
signature, defaut p=P -- H_2D, gamma_LS, borne_L8_derivee, executer_EB ;
le releve de l'ordre citait trois fonctions, la source en portait DEUX de
plus hors releve (la branche abs_x5 de H_2D, l.665-666, et le M_e de
borne_L8_derivee, l.1244) : parametrees et DECLAREES. A p = P chaque
sortie est bit-identique a la v8 (test joint, condition de la
contre-certification). D-B1 : garde_G4 calculee -- <B(t)> <= E sur le
jumeau FERME (eta=0, sans CAP : la borne L9 est une conservation, le CAP
la briserait par construction) ; a p IMPAIR elle se declare NON
APPLICABLE et jamais "passee" ; si elle mord, l'arret sort PAR LA
CASCADE (etat consigne, artefact ecrit, E36). TROUVAILLE de la
parametrisation, mordue par G-4 a sa premiere execution : le
demi-espace de H_2D excluait (0,0), nul a p impair, PORTEUR de la
positivite de V a p pair -- terme diagonal restitue sous garde de
parite (chemin p=5 inchange au bit). Ordre section 4 : le
temoin de la clause litterale 4.7 se mesure a M_facteur = 2 (amendement
E34 signe : la valeur par defaut M = 15 n'est pas convergee et ne se
publie pas seule). AUCUNE ancre inscrite : la v9 part encore en ARRET
ANCRES NON CONSIGNEES, et c'est correct (81.6).
Version 8. Repond a : note_machine2_prevol_m17_v2.md 834004d608171caa
(D-P0/P1/P2 leves et verifies -- reprise M16 fermee, 34 fichiers, zero
recalcul, bit-identique ; recoupement PR-7 (ii) : rho = 5/7 et p = 49/720
par deux chemins independants. D-P3 NEUF : l'ex aequo exact tuait
l'assemblage par exception -- un chemin d'arret non nomme est un chemin
non gouverne. v8 : l'arret est route PAR la cascade, statut ARRET EX
AEQUO consigne, JSON ecrit ; l'erratum de gel correspondant -- "ex aequo
exact dans un rang" ajoute a la branche 1 -- rejoint les ancres, Q4.)
Version 7. Repond a : note_machine2_prevol_m17_v1.md 76c88195d4e0a728
(PRE-VOL N-58 : D-P0 BLOQUANT, le chemin d'apres-mesure n'existait pas --
la v7 l'ecrit : boucle de grille avec reprise, P1 au site, bloc P8 en s
absolu exempte de G-1, stationnarites E-B tau_LS, temoins P7, borne L8
G-9, assemblage P2..P8 et cascade, modes --pilote/--run/--assemblage ;
D-P1 : canonicalisation des signes moins par codepoint + PLANCHER == 5
points ; D-P2 : barriere vide DECLAREE, defaut m2 nomme. D-F1 et D-F2
sont des faits d'acte, pas des defauts de script.)
Version 6 (rappel). Repond a : note_machine2_relecture_script_m17_v5.md 5c72d568db03d7fb
(D-S6 leve la ou il mordait ; D-S7 : la FAMILLE restait -- deux instances
de la recherche par registre dans le selftest lui-meme, le garde pose a
l'interieur de la chose qu'il ne peut pas proteger. Patron de campagne :
une renumerotation est un renommage, elle se propage MECANIQUEMENT ou ne
se fait pas -- ici, une deregistration).
Lignee : v1 d3291b34d0692c5b -> v2 34179f717412a606 -> v3 0aa03a2ca9ee70a9
-> v4 8806bab5b8b94766 -> v5 5345e40e5d27d084 -> v6 646b2be5a3198b1e
-> v7 0ce5c730ef53eac7 -> v8 a25619c412c93fd9 -> v9 a639c6e5f40ce853
-> v10 74e99e8ca4e91408 -> v11 223076efdd49dc60 -> v12 d84df28b4f4d8785
-> v13 6ca5edc8d72a05cb -> v14 01242ffdb8259ea3 -> v15 cedd270109b469c4
-> v16 a2081c7ee9b75683 -> v17. PB-1 : versions anterieures intactes.
La relecture passee ne certifie pas : la certification du script est la
contre-certification, apres le pre-vol N-58 et le banc lourd (machine 2).
ASYMETRIE Q2/Q3, DECLAREE (D-S2) : Q3 est fail-closed (deux lectures
vivantes -> ARRET Q3, aucune mesure) ; Q2 est fail-open en calcul (la
lettre de 4.7 est insatisfiable, un fail-closed y serait indiscernable
d'un vrai arret) -- MAIS rien n'est opposable tant que les erratums ne
sont pas consignes : le terme `erratums non consignes` alimente `arret`
en chaque point (D-S2), etendu a l'ancre E19 elle-meme (D-S4) : les
QUATRE pieces -- GEL_EMPREINTE et les trois numeros d'erratum -- se
consignent dans le MEME acte, la contre-certification, et `arret` les
nomme toutes tant qu'elles manquent. ARRET DE REGLE par la branche 1
jusque-la.
BROUILLON MACHINE 1 -- E19 : l'empreinte du gel EST inscrite (ancre
GEL_EMPREINTE ci-dessous, consignee a la v11 sur ordre, re-ancree sur
le gel v10 a la v14) ; le present docstring en est le jumeau (D-S1).

SOURCES CITEES (convention B, sha256 NFC+LF, 16 hex) :
  spec_estimateur_quantique_v3.md        48ac3e06ae5e89ff   (normative)
  pr6_carte_classique_etendue_v1.json    d32761567d24024f   (reference P3)
  m9_replication_v1.py (moteur)          c8ed357b120352c4   (custody G-8,
                                          re-verifie a l'import si fourni)
  note_outreach_EN_2026-07-25q.md        265e64de538e7cec   (table S-H, 4.12b)
GEL_EMPREINTE = 20950e52e7d63225   # E19 : gel v12-b2 certifie (P7).

QUESTIONS AU GEL -- etat apres la note m2 202bc80e147040d6 :
  [Q1, fraction P6 -- ARBITREE] FRACTION_P6 = 0.70 ; le gel nomme deja 0.70 trois
  fois (temoin S-G, bloc P8 4.11, chemin (b) du pilote). A 0.70 la
  barriere nominale a 7 sites (Lambda_c a de la dynamique) ; pres de
  1.00 elle s'effondre et les rangs de P6 sont du bruit. Numero
  d'erratum a l'acte (E18) : tant qu'il n'est pas consigne, P6 =
  NON_CONCLUANT motive (jamais SIGNAL).
  [Q2, stationnarite eta -- ARBITREE : erratum fonde, et plus fort]
  Le doublement de 4.7 DIVERGE (7.24 -> 26.50 -> 33.99 %), a tout M
  (9-10 chiffres identiques M=30..120) : clause insatisfiable en tout
  point, ARRET DE REGLE de la manche entiere sur Gamma_c -- qui ne
  porte AUCUN verdict (P3 juge K_s, P6 juge Gamma_LS et Lambda_c ;
  seul P8, non-verdictoire, emploie Gamma_c). Regle M15 au fondement :
  verifier la DIRECTION d'une perturbation, pas seulement sa presence.
  Procedure operative v2 : descente eta -> eta/2 jusqu'a pas <= tau_M
  (budget 8) ; la regle d'arret borne le PAS, pas le residu -- ratio
  mesure r ~ 0.42-0.46, residu estime pas*r/(1-r) ~ 1.2 % < tau_M a
  eta/16, DECLARE et consigne. Consignes : eta final, Gamma_c la,
  Richardson (2G(eta/2) - G(eta)), et l'ecart de la clause litterale.
  Numero d'erratum a l'acte (E18).
  [Q3, lecture des occupations de la graine (phi) -- OUVERTE, posee
  par machine 2] Trois objets distincts : chaine de Fock entiere
  (L4/L5), forme fermee sur le rayon (L6), continuation analytique
  exacte aux occupations moyennes reelles (la graine nominale est HORS
  RAYON de 48 % : n1/n2 = 2.957 contre 2.000). L'ancrage entier
  quantifie s*_Q par pas ~20 % contre une resolution gelee de 0.4 %
  (S-B : 1.102, ECHEC) ; la continuation reelle donne S-B = 0.9736
  (PASSE, 53 % de la tolerance). Resoudre une definition en silence
  est une faute meme quand la resolution est la bonne (E29) : le
  script PORTE LES DEUX lectures (LECTURE_OCCUPATIONS, obligatoire en
  mesure), la decision se prend au gel, en 4.4 ou 4.7, a l'acte.
  Convention attenante DECLAREE : la taille de boite E-B est entiere
  par exces (ceil), independante de la lecture.

Conventions de nommage (G-7, PR-4) : invariants K_nu* / K_s* uniquement ;
identifiant `delta` nu interdit (Delta_norm, delta_des). Aucun horodatage
dans les sorties (4.10). Sommation : ordre croissant declare.
"""

import sys, os, re, json, math, hashlib, unicodedata
from fractions import Fraction

import numpy as np

# ---------------------------------------------------------------------------
# Constantes gelees (gel section 4 et 5) -- citees par section, jamais inventees
# ---------------------------------------------------------------------------
GEL_EMPREINTE = "20950e52e7d63225"  # E19 : gel v12-b2 (P7), certif m2
P = 5
W1 = Fraction(1)
CANAL = (2, 1)                                   # 4.1
KAPPA = 12                                       # 4.3
GRILLE_W2 = [Fraction(195, 100), Fraction(197, 100), Fraction(198, 100),
             Fraction(2), Fraction(202, 100), Fraction(203, 100),
             Fraction(205, 100)]                 # 4.2 (site exact inclus)
FRACTIONS_S = [0.50, 0.70, 0.85, 1.00, 1.20]     # 4.4
RES_BISSECTION = 0.004                            # 4.5 (x s*_ff)
BORNES_BISSECTION = (0.3, 1.5)                    # 4.5 (x s*_ff)
N_MAX_EB = 120                                    # 4.6
B_N = P                                           # 4.6 : N = r_c + P + B_N
P8_W2 = Fraction(195, 100)                        # 4.11
P8_G = [3e-3, 1e-3, 3e-4]                         # 4.11 (g decroissant)
P8_FRACTION = 0.70                                # 4.11
FRACTION_P6 = 0.70                                # Q1 arbitree (note m2
                                                  # 202bc80e) ; numero E18
                                                  # a l'acte
LECTURE_OCCUPATIONS = "reelle"                    # Q3 ARBITREE : E35 (delta 81
                                                  # "entiere", fixee par
                                                  # erratum a l'acte ; toute
                                                  # mesure l'exige explicite
BUDGET_DESCENTE = 8                               # Q2 : pas de descente max
ERRATUMS_CONSIGNES = {"Q1_fraction_P6": "E33",    # numeros E18, remplis a
                      "Q2_eta_descente": "E34",   # la contre-certification
                      "Q3_lecture_graine": "E35",
                      "Q4_ex_aequo_cascade": "E36"}  # D-P3 : branche 1 du gel

def _module_courant():
    """Reference au module courant SANS le registre des modules (D-S6,
    D-S7, forme machine 2 note 5c72d568db03d7fb, adoptee verbatim) : sous
    un chargement importlib non enregistre -- celui du pre-vol -- la
    recherche par registre echoue ; les globales, elles, sont la."""
    mod = sys.modules.get(__name__)
    if mod is not None:
        return mod
    import types as _t
    ns = _t.SimpleNamespace(**globals())
    ns.__doc__ = __doc__
    return ns

def ancres_manquantes(mod=None):
    """D-S4 (note 1136082ac2fea470) corrige D-S6 (note ac485de22076a0f3),
    formes machine 2 adoptees verbatim. E19 : l'ancre primaire est gardee
    comme les errata, motif nommant les quatre pieces. mod=None : le module
    courant, SANS sys.modules -- un chargement importlib non enregistre
    (celui du pre-vol) y echouerait (D-S6)."""
    errata = ERRATUMS_CONSIGNES if mod is None else mod.ERRATUMS_CONSIGNES
    ancre = GEL_EMPREINTE if mod is None else mod.GEL_EMPREINTE
    manque = [k for k, v in errata.items() if v is None]
    if ancre is None:
        manque.append("GEL_EMPREINTE (ancre E19)")
    return manque

TAU_RAC = 1e-9                                    # 5
TAU_P2 = 0.05                                     # 5 (absolu, K_s)
BANDE_P4 = 0.6                                    # 5
BANDE_P8 = 3.0                                    # 5
TAU_M = 0.02                                      # 5
TAU_LS = 0.05                                     # 5
TOL_DEN = 1e-6                                    # 5 / 4.8
BORNE_D1 = Fraction(1, 5)                         # 6, G-1
BORNE_D2A = Fraction(1, 10)                       # 6, G-1 (contamination)
ALPHA = Fraction(5, 100)                          # 5
N_MIN = 5                                         # 5
SEUIL_POIDS_TAU = 0.99                            # G-5 : chaines tau retenues
EMPREINTE_MOTEUR = "c8ed357b120352c4"             # custody G-8
EMPREINTE_CARTE = "d32761567d24024f"
EMPREINTE_NOTE25Q = "265e64de538e7cec"

# ---------------------------------------------------------------------------
# G-7 -- forme executable du gel (section 10), adoptee verbatim
# ---------------------------------------------------------------------------
SENS_ADMIS = ("nu", "s")
IDENTIFIANTS_BANNIS = ("delta",)      # 4.1 / PR-4 : Delta_norm ou delta_des

def controle_G7(module):
    noms = [n for n in vars(module) if not n.startswith("_")]
    vus  = [n for n in noms if n == "K" or n.startswith("K_")]
    fautifs = [n for n in vus
               if len(n.split("_")) < 2 or n.split("_")[1] not in SENS_ADMIS]
    bannis = [n for n in noms if n in IDENTIFIANTS_BANNIS]
    assert vus, "G-7 : aucun invariant vu -- controle inerte"
    assert not fautifs, "G-7 : invariant sans sens _nu/_s : %s" % fautifs
    assert not bannis, "G-7 : identifiant banni (4.1, PR-4) : %s" % bannis
    return len(vus)

# ---------------------------------------------------------------------------
# Fragments perimes (D-S1, forme machine 2 note cb4697134c8a070d, adoptee) :
# le docstring declare ce que le script fait ; toute constante qu'il cite
# doit valoir ce que le module porte. Canonicaliser AVANT de comparer
# (lecon : str(0.70) == "0.7", famille float("1.414214") != sqrt(2)).
# ---------------------------------------------------------------------------
def _valeur(txt):
    t = txt.strip(" .;,()")
    if t == "None":
        return None
    for conv in (int, float):
        try:
            return conv(t)
        except ValueError:
            pass
    return t

def fragments_perimes(mod):
    ecarts = []
    for nom, val in re.findall(r"([A-Z][A-Z0-9_]{3,})\s+(?:=|reste)\s+(\S+)",
                               mod.__doc__ or ""):
        if not hasattr(mod, nom):
            continue
        dit, reel = _valeur(val), getattr(mod, nom)
        if isinstance(dit, float) and isinstance(reel, (int, float)):
            egal = abs(float(reel) - dit) <= 1e-12 * max(1.0, abs(dit))
        else:
            egal = (dit == reel)
        if not egal:
            ecarts.append((nom, val, reel))
    return ecarts

# ---------------------------------------------------------------------------
# Convention B (gel section 0, forme executable)
# ---------------------------------------------------------------------------
def empreinte_convention_B(chemin):
    brut = open(chemin, "rb").read()
    canon = unicodedata.normalize(
        "NFC", brut.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()[:16]

# ---------------------------------------------------------------------------
# Elements de matrice exacts (spec L1) -- DOUBLE implementation de I_j
# I_j(m, n) entier ; <m| xt^j |n> = I_j(m, n) * sqrt(m! / n!)
# Sommation : ordre croissant des indices, declare.
# ---------------------------------------------------------------------------
def I_j_implA(j, m, n):
    """Implementation A : recursion sur dict {indice: coeff entier}."""
    etat = {n: 1}
    for _ in range(j):
        suivant = {}
        for idx in sorted(etat):                      # ordre croissant declare
            c = etat[idx]
            suivant[idx + 1] = suivant.get(idx + 1, 0) + c
            if idx >= 1:
                suivant[idx - 1] = suivant.get(idx - 1, 0) + c * idx
        etat = suivant
    return etat.get(m, 0)

def I_j_implB(j, m, n, n_haut):
    """Implementation B : puissance de matrice entiere (objets Python)."""
    taille = n_haut + j + 2
    M = [[0] * taille for _ in range(taille)]
    for a in range(taille):
        if a + 1 < taille:
            M[a + 1][a] += 1
        if a - 1 >= 0:
            M[a - 1][a] += a
    v = [0] * taille
    v[n] = 1
    for _ in range(j):
        w = [0] * taille
        for a in range(taille):                       # ordre croissant declare
            if v[a]:
                for b in range(taille):
                    if M[b][a]:
                        w[b] += M[b][a] * v[a]
        v = w
    return v[m] if 0 <= m < taille else 0

_RAC_FACT = {}
def _sqrt_ratio_fact(m, n):
    """sqrt(m!/n!) en flottant, ratio calcule en entier exact d'abord."""
    if m >= n:
        r = 1
        for t in range(n + 1, m + 1):
            r *= t
        return math.sqrt(r)
    r = 1
    for t in range(m + 1, n + 1):
        r *= t
    return 1.0 / math.sqrt(r)

def element_xt(j, m, n):
    if m < 0 or n < 0:
        return 0.0
    I = I_j_implA(j, m, n)
    if I == 0:
        return 0.0
    return I * _sqrt_ratio_fact(m, n)

def lambdas(w2):
    Delta_norm = float(w2) ** 2 - float(W1) ** 2
    l1 = (2.0 * Delta_norm * float(W1)) ** -0.5
    l2 = (2.0 * Delta_norm * float(w2)) ** -0.5
    return Delta_norm, l1, l2

def X_saut(p, k, l, n1, n2, w2):
    """<n1+k, n2+l| x^p |n1, n2> ; selection L1 (parite, portee) implicite."""
    if n1 + k < 0 or n2 + l < 0:
        return 0.0
    _, l1, l2 = lambdas(w2)
    total = 0.0
    for j in range(0, p + 1):                         # ordre croissant declare
        jj = p - j
        if j < abs(k) or jj < abs(l):
            continue
        if (j - k) % 2 or (jj - l) % 2:
            continue
        e1 = element_xt(j, n1 + k, n1)
        e2 = element_xt(jj, n2 + l, n2)
        if e1 and e2:
            total += math.comb(p, j) * (l1 ** j) * (l2 ** jj) * e1 * e2
    return total

def coeff_homogene_X_s(w2):
    """X_c du canal (2,1) a p=5 : coefficient dominant, forme derivee
    (spec L4 iii ; derivation : termes j=2 et j=4 sur le rayon (2 nu, nu)).
    Regle 13, DECLARE : les litteraux 60/80 sont gages par la convergence
    COMPTEE du selftest (mutations 61, 81, 80.8 mordues, note m2 202bc80e),
    non par l'arithmetique exacte."""
    _, l1, l2 = lambdas(w2)
    return 60.0 * l1 ** 2 * l2 ** 3 + 80.0 * l1 ** 4 * l2


# ---------------------------------------------------------------------------
# Elements continues en occupation REELLE (graine phi : spec 3.0 et L6,
# "graine sur le rayon, n_j^0 = nu0 k_j"). <n+k|xt^j|n> = Q_{j,k}(n) *
# sqrt(prod_{t=1..k}(n+t)), Q extrait EXACTEMENT (interpolation Fraction
# sur les points entiers de I_j) ; identique aux entiers sur les entiers
# (verifie au selftest). L'arrondi 4.4 reste la regle de la graine (F).
# ---------------------------------------------------------------------------
_POLY_Q = {}

def _poly_Q(j, k):
    """Coefficients Fraction de Q_{j,k}(n) = I_j(n+k, n), degre (j-k)/2."""
    cle = (j, k)
    if cle in _POLY_Q:
        return _POLY_Q[cle]
    assert k >= 0 and (j - k) % 2 == 0 and j >= k
    d = (j - k) // 2
    xs = list(range(d + 1))
    ys = [Fraction(I_j_implA(j, n + k, n)) for n in xs]
    coeffs = [Fraction(0)] * (d + 1)
    for i, xi in enumerate(xs):                       # Lagrange exact
        base = [Fraction(1)]
        den = Fraction(1)
        for t, xt_ in enumerate(xs):
            if t == i:
                continue
            nouveau = [Fraction(0)] * (len(base) + 1)
            for a, c in enumerate(base):
                nouveau[a] -= c * xt_
                nouveau[a + 1] += c
            base = nouveau
            den *= (xi - xt_)
        for a, c in enumerate(base):
            coeffs[a] += ys[i] * c / den
    _POLY_Q[cle] = coeffs
    return coeffs

def element_xt_reel(j, decal, n):
    """<n+decal| xt^j |n> pour n reel >= 0 (symetrie pour decal < 0)."""
    if decal < 0:
        return element_xt_reel(j, -decal, n + decal) if n + decal >= 0 else 0.0
    if j < decal or (j - decal) % 2:
        return 0.0
    if n < 0:
        return 0.0
    coeffs = _poly_Q(j, decal)
    q = 0.0
    for a in range(len(coeffs) - 1, -1, -1):          # Horner, ordre declare
        q = q * n + float(coeffs[a])
    prod = 1.0
    for t in range(1, decal + 1):
        prod *= (n + t)
    return q * math.sqrt(prod) if prod > 0 else 0.0

def X_saut_reel(p, k, l, n1, n2, w2):
    """X_{k,l} aux occupations reelles (graine phi)."""
    if n1 + k < 0 or n2 + l < 0:
        return 0.0
    _, l1, l2 = lambdas(w2)
    total = 0.0
    for j in range(0, p + 1):                         # ordre croissant declare
        jj = p - j
        e1 = element_xt_reel(j, k, n1)
        e2 = element_xt_reel(jj, l, n2)
        if e1 and e2:
            total += math.comb(p, j) * (l1 ** j) * (l2 ** jj) * e1 * e2
    return total

# ---------------------------------------------------------------------------
# Invariants (gel 4.0) -- seuls noms K_*, sens au premier segment
# ---------------------------------------------------------------------------
def K_nu_ff(w2):
    """Invariant de L6 (sens occupation), forme fermee."""
    d_abs = abs(float(w2) - 2.0 * float(W1))
    return d_abs * ((P - 2) / P) ** ((P - 2) / 2) / coeff_homogene_X_s(w2)

def K_s_ff(w2, g):
    """Invariant du registre (sens amplitude) de la forme fermee."""
    return g * s_ff(w2, g) ** (P - 2)

def g_du_point(w2):
    return K_nu_ff(w2) / KAPPA                        # 4.3, lecture K_nu

def nu0_etoile(w2, g):
    d_abs = abs(float(w2) - 2.0 * float(W1))
    return ((P - 2) / P) * (d_abs / (g * coeff_homogene_X_s(w2))) ** (2.0 / (P - 2))

def s_ff(w2, g):
    Delta_norm, _, _ = lambdas(w2)
    return math.sqrt(nu0_etoile(w2, g) * Delta_norm / (2.0 * float(w2)))

def appariement(s, w2):
    """spec 3.0 : n1, n2 de la graine (PR-4 : confronte au moteur, accord)."""
    Delta_norm, _, _ = lambdas(w2)
    n1 = s * s * (Delta_norm + 2.0) ** 2 / (2.0 * Delta_norm)
    n2 = 2.0 * s * s * float(w2) / Delta_norm
    return n1, n2

def arrondi_graine(x):
    """Regle declaree (4.4) : au plus proche, .5 vers le haut."""
    return int(math.floor(x + 0.5))

def occupations_graine(s, w2, lecture):
    """Q3 : les DEUX lectures portees ; le gel tranchera (erratum, acte).
    'reelle' : moyennes de la graine coherente (spec 3.0), continuation
    exacte. 'entiere' : site de Fock le plus proche (arrondi 4.4)."""
    n1, n2 = appariement(s, w2)
    if lecture == "reelle":
        return n1, n2
    if lecture == "entiere":
        return float(arrondi_graine(n1)), float(arrondi_graine(n2))
    raise RuntimeError("Q3 non arbitree : lecture des occupations requise"
                       " ('reelle' ou 'entiere'), refus de mesurer")

# ---------------------------------------------------------------------------
# Enumeration des sauts admis, Omega_c (gel 4.1 : parite L1 incluse)
# ---------------------------------------------------------------------------
def sauts_admis():
    admis, ecartes = [], []
    for k in range(0, P + 1):                         # ordre croissant declare
        for l in range(0, P + 1):
            if (k, l) == (0, 0):
                continue
            if k + l > P:
                ecartes.append(((k, l), "portee"))
            elif (k + l) % 2 != P % 2:
                ecartes.append(((k, l), "parite L1"))
            elif l != 0 and Fraction(k, l) == Fraction(*CANAL):
                ecartes.append(((k, l), "multiple du canal"))
            else:
                admis.append((k, l))
    return admis, ecartes

def Omega_du_canal(w2):
    """Omega_c en Fraction sur la grille (G-2)."""
    admis, ecartes = sauts_admis()
    valeurs = []
    for (k, l) in admis:
        e = abs(l * w2 - k * W1)
        if e != 0:
            valeurs.append((e, (k, l)))
    om, arg = min(valeurs)
    comptes = {"admis": len(admis), "ecartes": len(ecartes),
               "enumeres": (P + 1) * (P + 1) - 1}
    assert comptes["admis"] + comptes["ecartes"] == comptes["enumeres"], \
        "G-5 : admis + ecartes != enumeres"
    return om, arg, comptes

# ---------------------------------------------------------------------------
# Sauts hors chaine depuis un site (signes), pour Sigma2 -- spec L5 / gel 4.8
# ---------------------------------------------------------------------------
def sauts_hors_chaine_signes():
    hors = []
    for k in range(-P, P + 1):
        for l in range(-P, P + 1):
            if (k, l) == (0, 0) or abs(k) + abs(l) > P:
                continue
            if (k + l) % 2 != P % 2:
                continue
            if l != 0 and k * CANAL[1] == l * CANAL[0]:
                continue                              # direction du canal
            hors.append((k, l))
    return sorted(hors)                               # ordre declare

def energie_libre(n1, n2, w2):
    return -float(W1) * n1 + float(w2) * n2

def Sigma2_site(n1, n2, w2, g):
    """Somme SIGNEE sur les sauts admis hors chaine ; denominateurs au
    premier ordre ; arret si |denominateur| < TOL_DEN (4.8)."""
    e0 = energie_libre(n1, n2, w2)
    total, min_den, comptes = 0.0, float("inf"), {"pris": 0, "ecartes_bord": 0}
    for (k, l) in sauts_hors_chaine_signes():
        m1n, m2n = n1 + k, n2 + l
        if m1n < 0 or m2n < 0:
            comptes["ecartes_bord"] += 1
            continue
        V = (g / P) * X_saut_reel(P, k, l, n1, n2, w2)
        if V == 0.0:
            comptes["ecartes_bord"] += 1
            continue
        den = e0 - energie_libre(m1n, m2n, w2)
        if abs(den) < TOL_DEN:
            raise RuntimeError("ARRET tol_den : denominateur %.3e au saut %s"
                               % (den, (k, l)))
        min_den = min(min_den, abs(den))
        total += V * V / den
        comptes["pris"] += 1
    return total, min_den, comptes

# ---------------------------------------------------------------------------
# Chaine E-A : barriere, garde de domaine, action, seuil (spec L5-L7, gel G-1)
# ---------------------------------------------------------------------------
def t_site(m, n1_0, n2_0, w2, g):
    return (g / P) * X_saut_reel(P, CANAL[0], CANAL[1],
                                 n1_0 + CANAL[0] * m, n2_0 + CANAL[1] * m, w2)

def barriere(n1_0, n2_0, w2, g, avec_Sigma2, m_plafond=4000,
             signe_delta=+1, facteur_t=None):
    """B_c comptee : sites m>=1 avec |e_m| > 2|t_m| ; e_m signe (4.8).
    signe_delta : bascule delta_des -> -delta_des a w2 FIXE (banc S-C).
    facteur_t : {site: facteur} de mutation d'un t_m (banc S-C, mord)."""
    d_des = signe_delta * (float(w2) - 2.0 * float(W1))
    S0 = Sigma2_site(n1_0, n2_0, w2, g)[0] if avec_Sigma2 else 0.0
    sites, negatifs_consec = [], 0
    for m in range(1, m_plafond + 1):
        Sm = (Sigma2_site(n1_0 + CANAL[0] * m, n2_0 + CANAL[1] * m, w2, g)[0]
              if avec_Sigma2 else 0.0)
        e_m = m * d_des + (Sm - S0)
        t_m = t_site(m, n1_0, n2_0, w2, g)
        if facteur_t and m in facteur_t:
            t_m *= facteur_t[m]
        if abs(e_m) > 2.0 * abs(t_m):
            sites.append((m, abs(e_m), abs(t_m)))
            negatifs_consec = 0
        else:
            if sites:
                negatifs_consec += 1
                if negatifs_consec >= 3:              # f decroit ensuite (L5)
                    break
            elif m > 8 and 2.0 * abs(t_m) > 4.0 * abs(m * d_des) + 1.0:
                break                                  # ouverte des la graine
    return sites

def garde_domaine(w2, g, sites_det, Omega_c):
    """G-1 : (D1) et (D2a contamination) sur les sites de la determination."""
    d_abs = abs(float(w2) - 2.0 * float(W1))
    D1 = d_abs / float(Omega_c)
    if sites_det:
        c_max = max(t / (2.0 * float(Omega_c)) for _, _, t in sites_det)
        site_max = max(sites_det, key=lambda x: x[2])[0]
    else:
        c_max, site_max = 0.0, None
    ok = (D1 <= float(BORNE_D1)) and (c_max <= float(BORNE_D2A))
    return {"D1": D1, "borne_D1": float(BORNE_D1), "c_max": c_max,
            "site_c_max": site_max, "borne_D2a": float(BORNE_D2A),
            "statut": "EN DOMAINE" if ok else "HORS DOMAINE"}

def Lambda_action(sites):
    return sum(math.log(e / (2.0 * t)) for _, e, t in sites)

def q_np_action(sites, Omega_c):
    """Part de Lambda accumulee aux sites ou 2|t| > Omega_c/5 (G-1)."""
    tot = Lambda_action(sites)
    if tot == 0.0:
        return 0.0
    part = sum(math.log(e / (2.0 * t)) for _, e, t in sites
               if 2.0 * t > float(Omega_c) / 5.0)
    return part / tot

def seuil_A4(w2, g, avec_Sigma2=True, lecture=None):
    """Bissection sur s (4.5). Rend s*_Q, les sites du dernier encadrement
    sous le seuil (S_det, garde D2a), et la resolution."""
    sff = s_ff(w2, g)
    lo, hi = BORNES_BISSECTION[0] * sff, BORNES_BISSECTION[1] * sff
    res = RES_BISSECTION * sff

    def barriere_de(s):
        n1, n2 = occupations_graine(s, w2, lecture)   # Q3 : lecture requise
        return barriere(n1, n2, w2, g, avec_Sigma2)

    b_lo, b_hi = barriere_de(lo), barriere_de(hi)
    assert b_lo, "A4 : borne basse sans barriere -- fenetre a revoir"
    assert not b_hi, "A4 : borne haute avec barriere -- fenetre a revoir"
    sites_lo = b_lo
    while hi - lo > res:
        mid = 0.5 * (lo + hi)
        b = barriere_de(mid)
        if b:
            lo, sites_lo = mid, b
        else:
            hi = mid
    assert sites_lo, "G-1 : encadrement final sous le seuil a barriere vide"
    return {"s_star_Q": 0.5 * (lo + hi), "resolution": res,
            "S_det": sites_lo, "s_lo_final": lo}

# ---------------------------------------------------------------------------
# Gamma_c : chaine tridiagonale a bord absorbant (4.7) ; taux = etat de plus
# grand recouvrement (definition unique avec E-B, 4.6)
# ---------------------------------------------------------------------------
def gamma_chaine(n1_0, n2_0, w2, g, sites, eta_facteur=1.0, M_facteur=1):
    d_des = float(w2) - 2.0 * float(W1)
    m2_bord = sites[-1][0] if sites else 8
    b_M = max(8, m2_bord)
    M = (m2_bord + b_M) * M_facteur
    eta_c = abs(d_des) * eta_facteur
    debut_cap = m2_bord + b_M // 2
    H = np.zeros((M + 1, M + 1), dtype=complex)
    for m in range(M + 1):
        H[m, m] = m * d_des
        if m > debut_cap:
            H[m, m] += -1j * eta_c * (m - debut_cap) ** 2
        if m < M:
            t = t_site(m, n1_0, n2_0, w2, g)
            H[m, m + 1] = t
            H[m + 1, m] = t
    valeurs, vecteurs = np.linalg.eig(H)
    recs = np.abs(vecteurs[0, :]) ** 2                # graine au site m=0
    ordre = np.lexsort((valeurs.real, -recs))         # deterministe (4.10)
    nu = ordre[0]
    return {"Gamma_c": float(-2.0 * valeurs[nu].imag),
            "M": M, "eta_c": eta_c, "recouvrement": float(recs[nu])}

# ---------------------------------------------------------------------------
# E-B : H 2D tronque + CAP ; jumeaux ; plancher (4.6, 4.9, P7)
# ---------------------------------------------------------------------------
def indexation(N):
    return {(a, b): a * N + b for a in range(N) for b in range(N)}

def H_2D(N, w2, g, signe_fantome=-1, potentiel="x5", eta=0.0, r_c=None,
         p=P):
    idx = indexation(N)
    dim = N * N
    H = np.zeros((dim, dim), dtype=complex)
    for (a, b), i in idx.items():
        H[i, i] = signe_fantome * float(W1) * a + float(w2) * b
    if potentiel == "x5":
        moitie = [(k, l) for k in range(-p, p + 1) for l in range(-p, p + 1)
                  if abs(k) + abs(l) <= p and (k + l) % 2 == p % 2
                  and ((k, l) > (0, 0))]
        for (a, b), i in idx.items():
            for (k, l) in sorted(moitie):             # ordre declare
                a2, b2 = a + k, b + l
                if 0 <= a2 < N and 0 <= b2 < N:
                    V = (g / p) * X_saut_reel(p, k, l, float(a), float(b), w2)
                    if V:
                        j = idx[(a2, b2)]
                        H[j, i] += V
                        H[i, j] += V                  # x^p reel symetrique
        if p % 2 == 0:
            # terme diagonal (k, l) = (0, 0) : exclu du demi-espace
            # ((k, l) > (0, 0)), concu pour p IMPAIR ou il est nul par
            # parite. A p PAIR il existe et porte la positivite de V
            # (L9) ; sans lui V = x^p prive de sa diagonale n'est pas
            # >= 0 et G-4 mord sur le pipeline sain -- elle l'a fait a
            # sa premiere execution. Correctif sous D-B2 : un p
            # parametre doit produire le H correct a p pair. Le chemin
            # impair n'execute pas ce bloc : bit-identite v8 preservee.
            for (a, b), i in idx.items():
                V0 = (g / p) * X_saut_reel(p, 0, 0, float(a), float(b), w2)
                if V0:
                    H[i, i] += V0
    elif potentiel == "abs_x5":
        X = np.zeros((dim, dim))
        _, l1, l2 = lambdas(w2)
        for (a, b), i in idx.items():
            if a + 1 < N:
                X[idx[(a + 1, b)], i] += l1 * math.sqrt(a + 1)
            if a - 1 >= 0:
                X[idx[(a - 1, b)], i] += l1 * math.sqrt(a)
            if b + 1 < N:
                X[idx[(a, b + 1)], i] += l2 * math.sqrt(b + 1)
            if b - 1 >= 0:
                X[idx[(a, b - 1)], i] += l2 * math.sqrt(b)
        vals, vecs = np.linalg.eigh(0.5 * (X + X.T))
        H = H + (g / p) * ((vecs * (np.abs(vals) ** p)) @ vecs.T).astype(complex)
    if eta and r_c is not None:
        for (a, b), i in idx.items():
            if max(a, b) > r_c:
                H[i, i] += -1j * eta * (max(a, b) - r_c) ** 2
    return H, idx

def graine_coherente(N, s, w2, signe=+1):
    n1m, n2m = appariement(s, w2)
    a1 = signe * math.sqrt(n1m)
    a2 = -signe * math.sqrt(n2m)                      # phase de la note 25q
    v1 = np.array([math.exp(-n1m / 2) * a1 ** n / math.sqrt(math.factorial(n))
                   for n in range(N)])
    v2 = np.array([math.exp(-n2m / 2) * a2 ** n / math.sqrt(math.factorial(n))
                   for n in range(N)])
    psi = np.kron(v1, v2)
    return psi / np.linalg.norm(psi)

def gamma_LS(N, w2, g, s, signe_fantome, potentiel, eta, r_c, p=P):
    H, _ = H_2D(N, w2, g, signe_fantome, potentiel, eta, r_c, p)
    psi = graine_coherente(N, s, w2)
    valeurs, vecteurs = np.linalg.eig(H)
    recs = np.abs(vecteurs.conj().T @ psi) ** 2
    ordre = np.lexsort((valeurs.real, -recs))
    nu = ordre[0]
    poids_queue = float(np.sum(np.abs(psi) ** 2 *
                    np.array([1.0 if max(divmod(i, N)) > r_c else 0.0
                              for i in range(N * N)])))
    # [POND] ERRATUM 4.6 (gel v10) -- TAUX : largeur ponderee, retention
    # G-5 (SEUIL_POIDS_TAU). Les trois sorties historiques ci-dessous
    # sont INCHANGEES ; l'etat de plus grand recouvrement est TEMOIN.
    tri = np.argsort(-recs)
    cumul = np.cumsum(recs[tri])
    # RESOLUTION DECLAREE (precision de gel due a l'acte) : les |c_nu|^2
    # d'une base propre NON ORTHOGONALE (H non normal, CAP) ne somment
    # pas a 1 -- une retention ABSOLUE a 0.99 peut etre inatteignable
    # (mesure : poids_total < 0.99 a la geometrie G1 reelle). La seule
    # lecture executable de "poids cumule >= 0.99 (G-5)" est RELATIVE
    # au poids total, qui est CONSIGNE comme diagnostic.
    poids_total = float(cumul[-1])
    seuil_abs = SEUIL_POIDS_TAU * max(poids_total, 1e-300)
    n_ret = int(min(np.searchsorted(cumul, seuil_abs) + 1, len(cumul)))
    retenus = tri[:n_ret]
    gam_pond = float(np.sum(recs[retenus] * (-2.0 * valeurs[retenus].imag)))
    return {"Gamma_LS": float(-2.0 * valeurs[nu].imag),
            "recouvrement": float(recs[nu]),
            "plancher": eta * poids_queue,
            "Gamma_pondere": gam_pond,
            "poids_cumule": float(cumul[n_ret - 1]),
            "poids_total": poids_total,
            "n_resonances": n_ret}

# ---------------------------------------------------------------------------
# Spearman exact (regle 16) -- distribution par enumeration complete
# ---------------------------------------------------------------------------
def rho_spearman(rangs_a, rangs_b):
    n = len(rangs_a)
    d2 = sum((ra - rb) ** 2 for ra, rb in zip(rangs_a, rangs_b))
    return Fraction(1) - Fraction(6 * d2, n * (n * n - 1))

def rho_crit_exact(n, alpha):
    from itertools import permutations
    base = list(range(1, n + 1))
    rhos = sorted((rho_spearman(base, p) for p in permutations(base)),
                  reverse=True)
    total = math.factorial(n)
    seuil = None
    valeurs = sorted(set(rhos), reverse=True)
    for v in valeurs:
        p_val = Fraction(sum(1 for r in rhos if r >= v), total)
        if p_val <= alpha:
            seuil = v
        else:
            break
    return seuil

def p_exact_de_rho(n, rho_obs):
    from itertools import permutations
    base = list(range(1, n + 1))
    total = math.factorial(n)
    c = sum(1 for p in permutations(base)
            if rho_spearman(base, p) >= rho_obs)
    return Fraction(c, total)

# ---------------------------------------------------------------------------
# References : carte PR-6 (schema 4.12 a) et table Gamma_st 25q (4.12 b)
# ---------------------------------------------------------------------------
def lire_carte(chemin):
    e = empreinte_convention_B(chemin)
    assert e == EMPREINTE_CARTE, "custody carte : %s != %s" % (e, EMPREINTE_CARTE)
    donnees = json.load(open(chemin, encoding="utf-8"))
    lignes = donnees["carte"]
    sel, ec = [], []
    for lg in lignes:
        if (lg.get("p") == 5 and lg.get("var") == "full"
                and lg.get("g") == 0.05 and lg.get("sgn") == "+1"
                and lg.get("dans_grille_P3") is True):
            sel.append(lg)
        else:
            ec.append(lg)
    assert len(sel) + len(ec) == len(lignes), "G-5 carte"
    for lg in sel:
        assert lg.get("sgn") == "+1", "PR-6 : sgn != +1 sur ligne selectionnee"
    return sel, {"selectionnees": len(sel), "ecartees": len(ec),
                 "lignes": len(lignes)}

_MOINS = (chr(0x2212), chr(0x2013), chr(0x2014))   # MINUS, EN DASH, EM DASH

def _canon_moins(x):
    """D-P1 (note 76c88195d4e0a728) : parser sans canonicaliser est
    float("1.414214") != sqrt(2) sous une troisieme peau."""
    for c in _MOINS:
        x = x.replace(c, "-")
    return x

def lire_table_gamma_st(chemin):
    """4.12 b : table Markdown TRANSPOSEE de la section 4(a) de la note 25q ;
    assertion d'orientation sur la ligne d'en-tete ; seconde table exclue."""
    e = empreinte_convention_B(chemin)
    assert e == EMPREINTE_NOTE25Q, "custody note 25q : %s" % e
    texte = open(chemin, encoding="utf-8").read()
    lignes = texte.split("\n")
    tetes = [i for i, l in enumerate(lignes)
             if l.strip().startswith("|") and "| s |" in l.replace("  ", " ")]
    assert tetes, "4.12 b : ligne d'en-tete '| s |' introuvable (orientation)"
    i0 = tetes[0]
    en_tete = [c.strip() for c in lignes[i0].strip().strip("|").split("|")]
    corps = None
    for l in lignes[i0 + 1:i0 + 4]:
        cs = [c.strip() for c in l.strip().strip("|").split("|")]
        if cs and ("Gamma" in cs[0] or "\\Gamma" in cs[0] or "st" in cs[0]):
            corps = cs
            break
    assert corps is not None, "4.12 b : ligne Gamma_st introuvable sous l'en-tete"
    colonnes = list(zip(en_tete[1:], corps[1:]))
    sel = [(float(_canon_moins(sv)), float(_canon_moins(gv)))
           for sv, gv in colonnes
           if _flottant(_canon_moins(sv)) and _flottant(_canon_moins(gv))
           and float(_canon_moins(sv)) >= 1.2]
    ec = len(colonnes) - len(sel)
    assert len(sel) + ec == len(colonnes), "G-5 table"
    assert len(sel) == 5, \
        "4.12(b) : %d points au lieu des 5 declares" % len(sel)
    return sel, {"selectionnees": len(sel), "ecartees": ec,
                 "colonnes": len(colonnes)}

def _flottant(x):
    try:
        float(x); return True
    except ValueError:
        return False

# ---------------------------------------------------------------------------
# Cascade de verdict (gel section 8) -- seule source ; mutation au selftest
# ---------------------------------------------------------------------------
BRANCHES = [
    ("ARRET DE REGLE",     lambda p3, p6, p7s, arret: arret or not p7s),
    ("SIGNAL",             lambda p3, p6, p7s, arret: p3 == "PASSE" and p6 == "PASSE"),
    ("PARTIEL",            lambda p3, p6, p7s, arret: ("PASSE" in (p3, p6)) and
        ((p6 if p3 == "PASSE" else p3) == "NON_CONCLUANT")),
    ("PARTIEL CONTRARIE",  lambda p3, p6, p7s, arret: ("PASSE" in (p3, p6)) and
        ((p6 if p3 == "PASSE" else p3) == "ECHOUE")),
    ("NON CONCLUANT",      lambda p3, p6, p7s, arret: p3 == "NON_CONCLUANT"
        and p6 == "NON_CONCLUANT"),
    ("PAS DE SIGNAL",      lambda p3, p6, p7s, arret: True),
]

def verdict(p3, p6, p7_sain, arret, branches=BRANCHES):
    for nom, cond in branches:
        if cond(p3, p6, p7_sain, arret):
            return nom
    return None

# ---------------------------------------------------------------------------
# Sorties deterministes (4.10) : ecriture atomique, cles triees, sans date
# ---------------------------------------------------------------------------
def ecrire_json_point(chemin, contenu):
    brut = json.dumps(contenu, sort_keys=True, ensure_ascii=True,
                      separators=(",", ": "), indent=1) + "\n"
    tmp = chemin + ".tmp"
    with open(tmp, "w", encoding="ascii", newline="\n") as f:
        f.write(brut)
    os.replace(tmp, chemin)
    return hashlib.sha256(brut.encode()).hexdigest()[:16]

# ---------------------------------------------------------------------------
# SELFTEST (gel section 10) -- sans moteur, comptes en forme derivee
# ---------------------------------------------------------------------------
def selftest():
    rapports = []

    # 1. L1 exact contre matrices flottantes, j = 1..5 ; interdits == 0 exact
    xt = np.diag(np.sqrt(np.arange(1, 24)), 1)
    xt = xt + xt.T
    pires = []
    for j in range(1, 6):
        Mf = np.linalg.matrix_power(xt, j)
        for m in range(0, 12):
            for n in range(0, 12):
                attendu = element_xt(j, m, n)
                pires.append(abs(attendu - Mf[m, n]) /
                             max(1.0, abs(Mf[m, n])))
    assert max(pires) <= TAU_RAC, "L1 : ecart %e" % max(pires)
    interdits = [X_saut(5, 1, 1, 6, 4, Fraction(2)),
                 X_saut(5, 3, 3, 6, 4, Fraction(2)),
                 X_saut(5, 2, 0, 6, 4, Fraction(2))]
    assert all(v == 0.0 for v in interdits), "L1 : interdit non nul"
    rapports.append("L1 exact : %d elements a %.1e ; interdits == 0" %
                    (len(pires), max(pires)))

    # 2. I_j en double implementation, egalite ENTIERE
    paires = comptees = 0
    for j in range(1, 6):
        for n in range(0, 10):
            for m in range(0, 12):
                a = I_j_implA(j, m, n)
                b = I_j_implB(j, m, n, 10)
                assert a == b, "I_j : A != B en (%d,%d,%d)" % (j, m, n)
                paires += 1
                comptees += 1
    assert paires == comptees == 5 * 10 * 12, "G-5 selftest I_j"
    rapports.append("I_j double implementation : %d paires, bit-identiques" % paires)

    # 2b. Continuation reelle == entiers sur les entiers (graine phi, L6)
    pires_r, nb_r = 0.0, 0
    for j in range(1, 6):
        for k in range(-j, j + 1):
            if (j - k) % 2:
                continue
            for n in range(0, 9):
                if n + k < 0:
                    continue
                a = element_xt(j, n + k, n)
                b = element_xt_reel(j, k, float(n))
                nb_r += 1
                pires_r = max(pires_r, abs(a - b) / max(1.0, abs(a)))
    assert pires_r <= TAU_RAC, "continuation : ecart %e" % pires_r
    rapports.append("continuation reelle : %d elements == entiers a %.1e" %
                    (nb_r, pires_r))

    # 3. Temoin de lecture K_nu (4.3) : nu0* independant de w2, relation a kappa
    va = nu0_etoile(GRILLE_W2[0], g_du_point(GRILLE_W2[0]))
    vb = nu0_etoile(GRILLE_W2[-1], g_du_point(GRILLE_W2[-1]))
    assert va == vb, "temoin K_nu : nu0* depend de w2 (lecture s ?)"
    assert abs(va ** ((P - 2) / 2) - KAPPA) <= KAPPA * TAU_RAC, "temoin kappa"
    rapports.append("temoin lecture K_nu : nu0* = %.6f uniforme, kappa retrouve" % va)

    # 3b. X_c : convergence comptee du rapport X(2 nu, nu)/nu^{5/2}
    w2t = GRILLE_W2[0]
    xc = coeff_homogene_X_s(w2t)
    ecarts = [abs(X_saut(5, 2, 1, 2 * nu, nu, w2t) / nu ** 2.5 - xc) / xc
              for nu in (400, 800)]
    assert ecarts[1] < ecarts[0] and ecarts[1] < 5e-3, "X_c : pas de convergence"
    rapports.append("X_c converge : %.1e -> %.1e" % (ecarts[0], ecarts[1]))

    # 4. G-7 : cinq montages (note m2 v8, executes)
    import types
    vus_script = controle_G7(_module_courant())
    gel = types.ModuleType("gel_canonique")
    for nom in ("K_nu", "K_s", "K_nu_ff", "K_s_ff", "K_s_Q", "K_s_cl"):
        setattr(gel, nom, 0)
    gel.Delta_norm = 0
    gel.delta_des = 0
    assert controle_G7(gel) == 6
    mutations, mordus = 0, 0
    for nom_mute in ("K_" + "star", "K_" + "ff"):
        m = types.ModuleType("mute")
        setattr(m, "K_nu", 0)
        setattr(m, nom_mute, 0)
        mutations += 1
        try:
            controle_G7(m); raise SystemExit("G-7 : mutation non mordue")
        except AssertionError:
            mordus += 1
    m = types.ModuleType("mute_banni")
    m.K_nu = 0
    setattr(m, "del" + "ta", 0)
    mutations += 1
    try:
        controle_G7(m); raise SystemExit("G-7 : banni non mordu")
    except AssertionError:
        mordus += 1
    m = types.ModuleType("vide")
    mutations += 1
    try:
        controle_G7(m); raise SystemExit("G-7 : vide non mordu")
    except AssertionError:
        mordus += 1
    assert mordus == mutations == 4
    rapports.append("G-7 : sain script (%d vus), sain gel (6 vus), 4 montages"
                    " mutes/vide mordus -- 5/5" % vus_script)

    # 5. Cascade : 36/36 uniques, puis mutation -> 3 orphelines
    etats = ("PASSE", "ECHOUE", "NON_CONCLUANT")
    cellules = [(a, b, c, d) for a in etats for b in etats
                for c in (True, False) for d in (True, False)]
    assert len(cellules) == 36
    uniques = sum(1 for cel in cellules if verdict(*cel) is not None)
    assert uniques == 36, "cascade : %d/36" % uniques
    orphelines = sum(1 for cel in cellules
                     if verdict(*cel, branches=BRANCHES[:-1]) is None)
    assert orphelines == 3, "mutation cascade : %d orphelines" % orphelines
    rapports.append("cascade : 36/36 uniques ; mutation -> 3 orphelines, mord")

    # 6. rho_crit exact (regle 16) : contre les valeurs connues n = 4, 5, 6
    attendus = {4: Fraction(1), 5: Fraction(9, 10), 6: Fraction(29, 35)}
    for n, att in sorted(attendus.items()):
        rc = rho_crit_exact(n, ALPHA)
        assert rc == att, "rho_crit(%d) = %s != %s" % (n, rc, att)
    rapports.append("rho_crit exact : n=4,5,6 conformes (1, 9/10, 29/35)")

    # 7. Sauts admis / Omega_c : comptes et attendus de l'acte
    attendus_Om = {Fraction(195, 100): Fraction(9, 10),
                   Fraction(205, 100): Fraction(1)}
    for w2, att in sorted(attendus_Om.items()):
        om, arg, comptes = Omega_du_canal(w2)
        assert om == att, "Omega_c(%s) = %s != %s" % (w2, om, att)
    rapports.append("Omega_c : bords conformes aux attendus consignes"
                    " (9/10 gauche, w1 droite)")

    # 7b. Fragments perimes (D-S1) : quatre montages, dont la lecon float
    import types as _types
    assert fragments_perimes(_module_courant()) == [], \
        "fragments perimes : le docstring contredit le code"
    m_ok = _types.ModuleType("coherent"); m_ok.__doc__ = "TEST_CONST = 3"
    m_ok.TEST_CONST = 3
    assert fragments_perimes(m_ok) == []
    m_fl = _types.ModuleType("float_ok"); m_fl.__doc__ = "F_CONST = 0.70"
    m_fl.F_CONST = 0.7
    assert fragments_perimes(m_fl) == [], "lecon str(0.70) non tenue"
    m_ko = _types.ModuleType("perime"); m_ko.__doc__ = "TEST_CONST reste None"
    m_ko.TEST_CONST = 3
    assert len(fragments_perimes(m_ko)) == 1
    rapports.append("fragments perimes : module reel 0 ecart ; montages"
                    " coherent/float/perime 3/3 (lecon 0.70 tenue)")

    # 7c. Ancres manquantes (D-S4) : quatre montages machine 2, 4/4
    m_an = _types.ModuleType("ancres")
    m_an.ERRATUMS_CONSIGNES = {"Q1": None, "Q2": None, "Q3": None}
    m_an.GEL_EMPREINTE = None
    assert len(ancres_manquantes(m_an)) == 4
    m_an.ERRATUMS_CONSIGNES = {"Q1": 30, "Q2": 31, "Q3": 32}
    assert ancres_manquantes(m_an) == ["GEL_EMPREINTE (ancre E19)"]
    m_an.GEL_EMPREINTE = "posee"
    m_an.ERRATUMS_CONSIGNES = {"Q1": None, "Q2": None, "Q3": None}
    assert len(ancres_manquantes(m_an)) == 3
    m_an.ERRATUMS_CONSIGNES = {"Q1": 30, "Q2": 31, "Q3": 32}
    assert ancres_manquantes(m_an) == []
    rapports.append("ancres manquantes (D-S4) : montages 4/4 (4, 1, 3, 0) ;"
                    " module reel : %d manquantes tant que l'acte n'a pas"
                    " signe" % len(ancres_manquantes()))

    # 7c-bis. Assemblage P3 fabrique (D-P0) : parfait -> PASSE ; mutation
    # a DISTANCE 2 (D-F2 : une adjacente donne 33/35 et PASSE -- inerte)
    rc6 = rho_crit_exact(6, ALPHA)
    rq0 = [1, 2, 3, 4, 5, 6]
    assert rho_spearman(rq0, rq0) >= rc6
    rq_adj = [2, 1, 3, 4, 5, 6]
    assert rho_spearman(rq0, rq_adj) >= rc6      # inerte, D-F2 constate
    rq_d2 = [3, 2, 1, 4, 5, 6]
    assert rho_spearman(rq0, rq_d2) < rc6, "mutation distance 2 : doit tuer"
    assert verdict("PASSE", "NON_CONCLUANT", True, False) == "PARTIEL"
    assert _rangs([1.0, 1.0, 2.0]) is None, \
        "D-P3 : l'ex aequo doit rendre None (route), pas une exception"
    assert verdict("ARRET EX AEQUO", "NON_CONCLUANT", True, True) \
        == "ARRET DE REGLE"
    rapports.append("assemblage fabrique : parfait PASSE ; adjacente 33/35"
                    " inerte (D-F2) ; distance 2 -> 27/35 MORD ; ex aequo"
                    " -> None route en ARRET DE REGLE (D-P3) ; cascade"
                    " cablee -> PARTIEL")

    # 7d. Fragment de pre-vol (prescription D-S6) : chargement importlib
    # NON enregistre -- celui du pre-vol -- puis mesurer_point de bout en
    # bout, deux poles d'etat, coherence avec le chargement interne.
    import importlib.util as _ilu
    spec_ext = _ilu.spec_from_file_location("m17_frag_prevol",
                                            os.path.abspath(__file__))
    m_ext = _ilu.module_from_spec(spec_ext)
    spec_ext.loader.exec_module(m_ext)        # PAS d'inscription sys.modules
    w2_n = Fraction(195, 100)
    r_ext = m_ext.mesurer_point(w2_n, m_ext.g_du_point(w2_n), 0.70,
                                avec_EB=False, lecture="reelle")
    r_int = mesurer_point(w2_n, g_du_point(w2_n), 0.70,
                          avec_EB=False, lecture="reelle")
    assert r_ext["statut"] == r_int["statut"], \
        "D-S6 : statuts divergents selon le chargement"
    # D-S7, prescription 2 : sur le module externe SAIN, avant mutation
    assert controle_G7(m_ext) >= 1, "D-S7 : G-7 inerte sur module externe"
    assert fragments_perimes(m_ext) == [], \
        "D-S7 : fragments perimes sur module externe"
    m_ext.GEL_EMPREINTE = "ancre-posee-au-montage"
    m_ext.ERRATUMS_CONSIGNES = {k: 99 for k in m_ext.ERRATUMS_CONSIGNES}
    r_tout = m_ext.mesurer_point(w2_n, m_ext.g_du_point(w2_n), 0.70,
                                 avec_EB=False, lecture="reelle")
    assert r_tout["statut"] == "EN DOMAINE", \
        "D-S6 : tout consigne devrait rendre EN DOMAINE (rendu %s)" \
        % r_tout["statut"]
    rapports.append("fragment pre-vol (D-S6/D-S7) : chargement non"
                    " enregistre, statut '%s' coherent interne/externe ;"
                    " G-7 et fragments perimes joues sur le module externe"
                    " ; tout consigne au montage -> EN DOMAINE"
                    % r_ext["statut"])

    # 7e. Garde de source (D-S7, prescription 3) : aucune recherche par
    # registre en forme crochet ; seule la forme .get( est admise.
    # Aiguille par concatenation (G-7 : bannir l'appel, pas le mot).
    src = open(os.path.abspath(__file__), encoding="ascii").read()
    aiguille_reg = "sys." + "modules" + "["
    admise = "sys." + "modules" + ".get("
    nb_crochet = src.count(aiguille_reg)
    nb_get = src.count(admise)
    assert nb_crochet == 0, \
        "D-S7 : %d recherche(s) par registre en forme crochet" % nb_crochet
    assert nb_get >= 1, "D-S7 : garde inerte (aucune forme .get non plus)"
    rapports.append("garde de source (D-S7) : 0 forme crochet, %d forme(s)"
                    " .get admise(s) -- comptes sur la source elle-meme"
                    % nb_get)

    # 8. Determinisme JSON : deux ecritures, memes octets (S-I, jambe locale)
    import tempfile
    contenu = {"b": 1.0 / 3.0, "a": [1, 2], "w2": "195/100"}
    with tempfile.TemporaryDirectory() as d:
        c1 = ecrire_json_point(os.path.join(d, "x.json"), contenu)
        os.remove(os.path.join(d, "x.json"))
        c2 = ecrire_json_point(os.path.join(d, "x.json"), contenu)
    assert c1 == c2, "S-I local : octets differents"
    rapports.append("ecriture deterministe : re-ecriture bit-identique")

    print("SELFTEST : %d controles PASSES" % len(rapports))
    for r in rapports:
        print("  - " + r)
    print("comptes selftest : %d + 0 sautes == %d attendus" %
          (len(rapports), len(rapports)))
    return True

# ---------------------------------------------------------------------------
# Point de mesure (assemblage) -- utilise par pilote et run
# ---------------------------------------------------------------------------
def mesurer_point(w2, g, fraction_s, avec_EB=True, lecture=None,
                  s_absolu=None, exempt_G1=False):
    d_des_fr = w2 - 2 * W1
    if d_des_fr == 0:
        return {"statut": "SITE EXACT", "w2": str(w2),
                "note": "P1 seulement : delta_des = 0 en Fraction,"
                        " aucune sortie Gamma_c ni s_star_Q (4.7)"}
    if g == 0:
        return {"statut": "CHAINE DECONNECTEE", "w2": str(w2), "Gamma": 0.0}
    Omega_c, arg_Om, comptes_Om = Omega_du_canal(w2)
    d_abs = abs(float(w2) - 2.0 * float(W1))
    if d_abs / float(Omega_c) > float(BORNE_D1) and not exempt_G1:
        return {"p": P, "w2": str(w2), "g": g, "statut": "HORS DOMAINE",
                "domaine": {"D1": d_abs / float(Omega_c),
                            "borne_D1": float(BORNE_D1),
                            "Omega_c": str(Omega_c),
                            "minimiseur": list(arg_Om), "comptes": comptes_Om,
                            "note": "(D1) echoue avant A4 ; (D2a) non evaluee"}}
    # Q3 : garde de lecture APRES les routages occupation-free (site exact,
    # g = 0, D1), AVANT toute quantite qui depend des occupations
    if lecture is None:
        lecture = LECTURE_OCCUPATIONS
    if lecture is None:
        return {"statut": "ARRET Q3",
                "motif": "lecture des occupations non arbitree (erratum"
                         " requis a l'acte) ; aucune mesure"}
    sortie_lecture = {"lecture_occupations": lecture,
                      "erratums": dict(ERRATUMS_CONSIGNES)}
    seuil = seuil_A4(w2, g, lecture=lecture)
    garde = garde_domaine(w2, g, seuil["S_det"], Omega_c)
    sortie = {"p": P, "w2": str(w2), "g": g, "canal": list(CANAL),
              "conventions": {"graine": "phi/F, arrondi .5 vers le haut",
                              "r": "max(n1,n2)", "sommation": "croissante",
                              "hbar": 1},
              "domaine": dict(garde, Omega_c=str(Omega_c),
                              minimiseur=list(arg_Om), comptes=comptes_Om),
              }
    if garde["statut"] != "EN DOMAINE":
        if not exempt_G1:
            sortie["statut"] = "HORS DOMAINE"
            return sortie
        sortie["lecture_P8"] = "instrumentale ((D2a) echouee, 4.11)"
    s = (s_absolu if s_absolu is not None
         else fraction_s * s_ff(w2, g))                # 4.11 : P8 en absolu
    n1_0, n2_0 = occupations_graine(s, w2, lecture)   # Q3
    sites = barriere(n1_0, n2_0, w2, g, avec_Sigma2=True)
    sites_po = barriere(n1_0, n2_0, w2, g, avec_Sigma2=False)
    S0v, min_den, _ = Sigma2_site(n1_0, n2_0, w2, g)
    S1v = Sigma2_site(n1_0 + CANAL[0], n2_0 + CANAL[1], w2, g)[0]
    sortie["statut"] = "EN DOMAINE"
    sortie["graine"] = {"fraction": fraction_s, "s": s,
                        "s_absolu": s_absolu is not None,
                        "n1_0": n1_0, "n2_0": n2_0, "nu0": n2_0,
                        "convention": "lecture '%s' (Q3) ; arrondi 4.4 ="
                                      " graine (F)" % lecture}
    sortie["EA"] = {"m1": sites[0][0] if sites else None,
                    "m2": sites[-1][0] if sites else None,
                    "card_Bc": len(sites),
                    "barriere_vide": not sites,
                    "Lambda_c": Lambda_action(sites),
                    "Lambda_c_premier_ordre": Lambda_action(sites_po),
                    "q_np": q_np_action(sites, Omega_c),
                    "Sigma2": {"S0": S0v, "pente_S1_moins_S0": S1v - S0v,
                               "min_denominateur": min_den},
                    "s_star_Q": {"val": seuil["s_star_Q"],
                                 "resolution": seuil["resolution"]},
                    "K_nu_ff": K_nu_ff(w2), "K_s_ff": K_s_ff(w2, g),
                    "K_s_compte": g * seuil["s_star_Q"] ** (P - 2)}
    motifs_arret = []
    if not sites:
        # D-P2 : le cas se DECLARE -- defaut nomme, aucune chaine jouee
        sortie["EA"]["defaut_barriere_vide"] = (
            "graine au-dessus du seuil compte : Lambda_c = 0 par"
            " construction, Gamma_c et E-B non joues, m2 sans valeur"
            " (le defaut 8 de la v6 est retire)")
    else:
        # Amendement E34 (ordre section 4) : le temoin de la clause
        # litterale se mesure a M_facteur = 2 -- la valeur par defaut
        # (M = 15) n'est pas convergee et ne se publie pas seule. Sa
        # stationnarite en M devient x2 contre x4 ; l'ancien gc2 (x2)
        # fusionne avec le temoin lui-meme.
        gc4 = gamma_chaine(n1_0, n2_0, w2, g, sites, M_facteur=4)
        gc = gamma_chaine(n1_0, n2_0, w2, g, sites, M_facteur=2)
        gce = gamma_chaine(n1_0, n2_0, w2, g, sites, eta_facteur=2.0,
                           M_facteur=2)
        stat_M = abs(gc4["Gamma_c"] - gc["Gamma_c"]) / max(gc["Gamma_c"], 1e-300)
        stat_e = abs(gce["Gamma_c"] - gc["Gamma_c"]) / max(gc["Gamma_c"], 1e-300)
        pas_desc, prev, stationnaire = [], gc4["Gamma_c"], False
        f = 1.0
        for _ in range(BUDGET_DESCENTE):
            f *= 0.5
            gd = gamma_chaine(n1_0, n2_0, w2, g, sites, eta_facteur=f,
                              M_facteur=4)
            ec = abs(gd["Gamma_c"] - prev) / max(prev, 1e-300)
            pas_desc.append({"eta_facteur": f, "Gamma_c": gd["Gamma_c"],
                             "ecart_pas": ec})
            prev = gd["Gamma_c"]
            if ec <= TAU_M:
                stationnaire = True
                break
        gd8 = gamma_chaine(n1_0, n2_0, w2, g, sites,
                           eta_facteur=pas_desc[-1]["eta_facteur"], M_facteur=8)
        stat_M_desc = abs(gd8["Gamma_c"] - pas_desc[-1]["Gamma_c"]) / \
            max(pas_desc[-1]["Gamma_c"], 1e-300)
        operatif = {"val": pas_desc[-1]["Gamma_c"],
                    "eta_final_facteur": pas_desc[-1]["eta_facteur"],
                    "stationnaire": stationnaire,
                    "stationnarite_pas": pas_desc[-1]["ecart_pas"],
                    "stationnarite_M_descente": stat_M_desc,
                    "M": gd8["M"] // 2, "recouvrement": gc4["recouvrement"],
                    "procedure": "Q2 : eta initial |delta_des|, moitie a"
                                 " chaque pas jusqu'a pas <= tau_M (budget"
                                 " %d), M x4 ; erratum a l'acte"
                                 % BUDGET_DESCENTE,
                    "pas": pas_desc}
        if len(pas_desc) >= 2:
            a, b = pas_desc[-2], pas_desc[-1]
            operatif["Gamma_Richardson"] = 2 * b["Gamma_c"] - a["Gamma_c"]
            if a["ecart_pas"] > 0:
                r = b["ecart_pas"] / a["ecart_pas"]
                operatif["ratio_pas"] = r
                if 0 < r < 1:
                    operatif["residu_estime"] = b["ecart_pas"] * r / (1 - r)
        sortie["EA"]["Gamma_c"] = operatif
        sortie["EA"]["Gamma_c_temoin_clause_4_7"] = {
            "val": gc["Gamma_c"], "eta_c": gc["eta_c"], "M": gc["M"],
            "recouvrement": gc["recouvrement"], "stationnarite_M": stat_M,
            "ecart_doublement": stat_e, "insatisfiable": stat_e > TAU_M,
            "note": "temoin de la clause 4.7 litterale ; NON operatif"
                    " (D-S3) ; M_facteur = 2 (amendement E34)"}
        if stat_M_desc > TAU_M:
            motifs_arret.append("stationnarite M operative %.3e" % stat_M_desc)
        if not stationnaire:
            motifs_arret.append("descente non stationnaire (budget %d)"
                                % BUDGET_DESCENTE)
        if avec_EB:
            sortie["EB"] = executer_EB(w2, g, s, n1_0, sites)
            if sortie["EB"].get("descente_rejetee_L30"):
                motifs_arret.append("erratum 4.6 : descente rejetee a"
                                    " L = 30 (bord de fenetre)")
            if sortie["EB"].get("faisable"):
                for nomst, v in sortie["EB"].get("stationnarites",
                                                 {}).items():
                    if v > TAU_LS:
                        motifs_arret.append("G-3 : stationnarite E-B %s ="
                                            " %.3e > tau_LS" % (nomst, v))
                if sortie["EB"].get("G9_mordue"):
                    motifs_arret.append("G-9 : Gamma_LS(H+) au-dela de la"
                                        " borne L8 derivee")
    manquantes = ancres_manquantes()          # D-S4 ; sans sys.modules (D-S6)
    if manquantes:
        motifs_arret.append("ancres non consignees : %s"
                            % ", ".join(manquantes))
    sortie["motifs_arret"] = motifs_arret
    sortie.update(sortie_lecture)
    if motifs_arret:
        seul_ancres = (len(motifs_arret) == 1 and manquantes)
        sortie["statut"] = ("ARRET ANCRES NON CONSIGNEES" if seul_ancres
                            else "ARRET DE REGLE")
    return sortie


# ---------------------------------------------------------------------------
# E-B execute (erratum 4.6) : geometrie par point (critere d'absorbeur),
# operatif descente/Richardson/residu, montante TEMOIN, portes r_c + p
# et N + p, jumeau H+,
# borne L8 derivee (G-9) -- formes declarees, citations spec 3.8
# ---------------------------------------------------------------------------
def borne_L8_derivee(Omega_c, t_maxv, r_c, r_graine, plancher, p=P):
    """Spec 3.8 : amplitude de fuite <= (2 t_max / Omega_c)^M_e ; largeur
    <= Omega_c x (amplitude)^2. M_e = nombre de sauts de la graine au bord
    (portee p par saut), forme DERIVEE DECLAREE, plancher numerique 10x
    plancher_EB en garde basse (sinon G-9 mord sur du bruit). A ratifier."""
    M_e = max(1, math.ceil((r_c - r_graine) / p))
    fac = 2.0 * t_maxv / float(Omega_c)
    if fac >= 1.0:
        return float("inf")                    # borne inoperante, declaree
    return max(10.0 * plancher, float(Omega_c) * fac ** (2 * M_e))

def garde_G4(N, w2, g, s, p=P, n_t=8):
    """G-4 (gel section 6) : <B(t)> <= E sur le JUMEAU, violation = arret.
    Fondement L9 : a p PAIR, g > 0, H+ = B + V avec V >= 0 donc
    <B(t)> = E - <V(t)> <= E. A p IMPAIR, V n'a pas de minimum : la garde
    se declare NON APPLICABLE (jamais "passee" la ou elle ne peut pas
    s'exercer). Evaluation sur le jumeau FERME (eta = 0, sans CAP) : la
    borne est une propriete de conservation, le CAP la briserait par
    construction et la garde mesurerait l'absorbeur, pas le pipeline.
    Grille de temps DECLAREE : n_t + 1 instants sur une periode 2*pi de
    l'oscillateur w1. Tolerance DERIVEE (regle 13, patron G3) :
    1e-9 * (|E| + max_t |<V(t)>| + 1e-300). Un arret G-4 sort PAR LA
    CASCADE de l'assembleur, jamais par exception (E36)."""
    if p % 2 == 1:
        return {"garde": "G-4", "p": p, "statut": "NON APPLICABLE",
                "motif": "p impair : V sans minimum, aucune borne de ce"
                         " type (L9)", "mordu": False}
    Hg, _ = H_2D(N, w2, g, +1, "x5", 0.0, None, p)
    H0, _ = H_2D(N, w2, 0.0, +1, "x5", 0.0, None, p)
    V = (Hg - H0).real
    psi0 = graine_coherente(N, s, w2)
    E = float(psi0 @ (Hg.real @ psi0))
    vals, vecs = np.linalg.eigh(Hg.real)
    c0 = vecs.T @ psi0
    depassement = -float("inf")
    vmax = 0.0
    for j in range(n_t + 1):
        t = 2.0 * math.pi * j / n_t
        psi_t = vecs @ (np.exp(-1j * vals * t) * c0)
        v_moy = float((psi_t.conj() @ (V @ psi_t)).real)
        vmax = max(vmax, abs(v_moy))
        depassement = max(depassement, -v_moy)      # <B(t)> - E = -<V(t)>
    tol = 1e-9 * (abs(E) + vmax + 1e-300)
    mordu = depassement > tol
    return {"garde": "G-4", "p": p,
            "statut": "MORDUE" if mordu else "PASSEE",
            "E": E, "depassement_max": depassement,
            "tolerance": tol, "n_t": n_t, "mordu": bool(mordu)}

def executer_EB(w2, g, s, n1_0, sites, p=P):
    m2b = sites[-1][0]
    b_M = max(8, m2b)
    r_c = math.ceil(n1_0) + 2 * (m2b + b_M) + 2
    # [GEO] ERRATUM 4.6 (gel v10) : la geometrie se fixe PAR POINT par le
    # critere d'absorbeur ; N = r_c + p + B_N est REMPLACE. Essai a
    # L = 20 (nominal) puis L = 30 ; rejet aux deux = arret PAR LA
    # CASCADE. Pas de descente : |Gamma_k - Gamma_{k-1}| / denominateur
    # (convention declaree ci-dessous), critere : les DEUX DERNIERS
    # (eta/4 et eta/8) < tau_LS. Operatif : paire E34.
    d_abs = abs(float(w2) - 2.0 * float(W1))
    eta = d_abs
    essais = []
    L_retenu, valeurs_desc, pas_desc = None, None, None
    for L in (20, 30):
        N = r_c + L
        if N > N_MAX_EB:
            return {"faisable": False, "N_derive": N, "N_max": N_MAX_EB,
                    "L_essaye": L,
                    "G4": {"garde": "G-4", "p": p, "statut": "NON EVALUEE",
                           "motif": "EB infaisable (N > N_max)",
                           "mordu": False}}
        vd = [gamma_LS(N, w2, g, s, -1, "x5", eta * f, r_c, p)
              for f in (1.0, 0.5, 0.25, 0.125)]
        pd = []
        for k in (1, 2, 3):
            dk = max(vd[k - 1]["Gamma_LS"], 10.0 * vd[k - 1]["plancher"],
                     1e-300)
            pd.append(abs(vd[k]["Gamma_LS"] - vd[k - 1]["Gamma_LS"]) / dk)
        acc = pd[1] < TAU_LS and pd[2] < TAU_LS
        essais.append({"L": L, "N": N, "pas": pd, "accepte": acc})
        if acc:
            L_retenu, valeurs_desc, pas_desc = L, vd, pd
            break
    critere = {"fenetre": "[10, 30]", "nominal": 20, "essais": essais,
               "L_retenu": L_retenu}
    if L_retenu is None:
        return {"faisable": True, "r_c": r_c, "eta": eta,
                "descente_rejetee_L30": True,
                "critere_absorbeur": critere,
                "G4": {"garde": "G-4", "p": p, "statut": "NON EVALUEE",
                       "motif": "descente rejetee a L = 30 (4.6)",
                       "mordu": False}}
    N = r_c + L_retenu
    b8, b4 = valeurs_desc[3], valeurs_desc[2]
    plancher = b8["plancher"]
    denom8 = max(b8["Gamma_LS"], 10.0 * plancher, 1e-300)
    r_e34 = pas_desc[2] / pas_desc[1] if pas_desc[1] > 0 else float("nan")
    richardson = (b8["Gamma_LS"] + (b8["Gamma_LS"] - b4["Gamma_LS"])
                  * r_e34 / (1.0 - r_e34)
                  if 0.0 < r_e34 < 1.0 else float("nan"))
    residu = (pas_desc[2] * r_e34 / (1.0 - r_e34)
              if 0.0 < r_e34 < 1.0 else float("nan"))
    operatif = {"eta_final_facteur": 0.125, "Gamma": b8["Gamma_LS"],
                "r": r_e34, "Richardson": richardson,
                "residu_declare": residu,
                "clause": "paire E34 : dernier pas / precedent, tous"
                          " deux dans les pas joues ; Richardson meme"
                          " paire ; le residu se DECLARE"}
    eta_f = eta * 0.125
    v_rc = gamma_LS(N + p, w2, g, s, -1, "x5", eta_f, r_c + p, p)
    #        ^ TRANSLATION (gel v11) : r_c + p ET N + p conjoints, L conserve
    v_N = gamma_LS(N + p, w2, g, s, -1, "x5", eta_f, r_c, p)
    stats = {"translation_p": abs(v_rc["Gamma_LS"] - b8["Gamma_LS"]) / denom8,
             "N_plus_p": abs(v_N["Gamma_LS"] - b8["Gamma_LS"]) / denom8}
    v_2eta = gamma_LS(N, w2, g, s, -1, "x5", 2.0 * eta, r_c, p)
    d0 = max(valeurs_desc[0]["Gamma_LS"],
             10.0 * valeurs_desc[0]["plancher"], 1e-300)
    temoin_montante = {"ecart": abs(v_2eta["Gamma_LS"]
                                    - valeurs_desc[0]["Gamma_LS"]) / d0,
                       "note": "TEMOIN NOMME (erratum 4.6, patron 4.7 /"
                               " E34) : consigne, JAMAIS un arret"}
    hplus = gamma_LS(N, w2, g, s, +1, "x5", eta, r_c, p)
    t_maxv = max(abs(t) for _, _, t in sites)
    Om = Omega_du_canal(w2)[0]
    borne = borne_L8_derivee(Om, t_maxv, r_c, math.ceil(n1_0), plancher, p)
    g4 = garde_G4(N, w2, g, s, p=p)
    return {"faisable": True, "N": N, "r_c": r_c, "eta": eta,
            "convention_denominateur": "ecarts tau_LS au denominateur"
                                       " max(Gamma, 10 x plancher), declare"
                                       " ; pas de descente : denominateur"
                                       " au pas PRECEDENT",
            "critere_absorbeur": critere,
            "operatif_4_6": operatif,
            "Gamma_LS": {"H": b8, "Hplus": hplus},
            "temoin_montante": temoin_montante,
            "stationnarites": stats, "plancher": plancher,
            "borne_L8": borne,
            "G9_mordue": hplus["Gamma_LS"] > borne,
            "G4": g4}


# ---------------------------------------------------------------------------
# ORCHESTRATION (D-P0) : P1 au site, grille + reprise, bloc P8, temoins P7,
# assemblage P2..P8 + cascade -- le chemin d'apres-mesure du gel 4.10 / 11
# ---------------------------------------------------------------------------
def point_site_exact(m_scan=50):
    """P1 : delta_des = 0 en Fraction ; f_c(m) <= 0 pour tout m scanne,
    B_c vide AU SENS STRICT. Ancre (0,0), g_ref = g(1.95) DECLARE (le gel
    ne fixe pas le g du site : convention a ratifier)."""
    w2 = Fraction(2)
    g_ref = g_du_point(GRILLE_W2[0])
    S0v = Sigma2_site(0.0, 0.0, w2, g_ref)[0]
    max_f, sites_positifs = -float("inf"), 0
    for mm in range(1, m_scan + 1):
        Sm = Sigma2_site(0.0 + CANAL[0] * mm, 0.0 + CANAL[1] * mm, w2, g_ref)[0]
        e_m = Sm - S0v                        # delta_des = 0 exact
        t_m = t_site(mm, 0.0, 0.0, w2, g_ref)
        f = abs(e_m) - 2.0 * abs(t_m)
        max_f = max(max_f, f)
        if f > 0:
            sites_positifs += 1
    return {"statut": "SITE EXACT", "w2": "2", "P1": {
        "delta_des_exact_nul": True, "g_ref_declare": g_ref,
        "m_scannes": m_scan, "sites_f_positifs": sites_positifs,
        "max_f": max_f, "B_c_vide_strict": sites_positifs == 0}}

def _chemin_point(dossier, w2, etiquette):
    return os.path.join(dossier, "pt_%s_%s.json"
                        % (str(w2).replace("/", "_"), etiquette))

def _point_valide(chemin):
    if not os.path.exists(chemin):
        return False
    try:
        return "statut" in json.load(open(chemin, encoding="ascii"))
    except Exception:
        return False

def mesurer_manche(dossier):
    """Boucle du gel 4.10 : w2 croissant (ordre 4.2), fractions croissantes,
    bloc P8 en dernier (g decroissant). Reprise : JSON valide saute et
    compte 'repris'. Comptes G-5 en forme derivee."""
    os.makedirs(dossier, exist_ok=True)
    comptes = {"attendus": 0, "calcules": 0, "repris": 0, "site_exact": 0,
               "hors_domaine": 0, "en_domaine": 0, "arrets": 0,
               "barrieres_vides": 0, "eb_infaisables": 0}
    def consigner(chemin, contenu):
        ecrire_json_point(chemin, contenu)
        st = contenu.get("statut", "?")
        if st == "SITE EXACT":
            comptes["site_exact"] += 1
        elif st == "HORS DOMAINE":
            comptes["hors_domaine"] += 1
        elif st.startswith("ARRET"):
            comptes["arrets"] += 1
        else:
            comptes["en_domaine"] += 1
        if contenu.get("EA", {}).get("barriere_vide"):
            comptes["barrieres_vides"] += 1
        if contenu.get("EB", {}).get("faisable") is False:
            comptes["eb_infaisables"] += 1
    for w2 in GRILLE_W2:
        if w2 - 2 * W1 == 0:
            comptes["attendus"] += 1
            ch = _chemin_point(dossier, w2, "site")
            if _point_valide(ch):
                comptes["repris"] += 1
                continue
            consigner(ch, point_site_exact())
            comptes["calcules"] += 1
            continue
        for fr in FRACTIONS_S:                # croissantes (4.10)
            comptes["attendus"] += 1
            ch = _chemin_point(dossier, w2, "f%03d" % round(fr * 100))
            if _point_valide(ch):
                comptes["repris"] += 1
                continue
            r = mesurer_point(w2, g_du_point(w2), fr,
                              avec_EB=(fr == FRACTION_P6))
            consigner(ch, r)
            comptes["calcules"] += 1
    s8 = P8_FRACTION * s_ff(P8_W2, g_du_point(P8_W2))   # 4.11 : absolu fixe
    for g8 in P8_G:                            # g decroissant (4.10)
        comptes["attendus"] += 1
        ch = _chemin_point(dossier, P8_W2, "P8_g%s" % repr(g8))
        if _point_valide(ch):
            comptes["repris"] += 1
            continue
        r = mesurer_point(P8_W2, g8, P8_FRACTION, avec_EB=True,
                          s_absolu=s8, exempt_G1=True)
        r["bloc"] = "P8 (4.11, exempte du renvoi G-1, lecture instrumentale"
        r["bloc"] += " ou (D2a) echoue)"
        consigner(ch, r)
        comptes["calcules"] += 1
    ok = comptes["repris"] + comptes["calcules"] == comptes["attendus"]
    comptes["G5"] = "%d repris + %d calcules == %d attendus : %s" % (
        comptes["repris"], comptes["calcules"], comptes["attendus"],
        "OK" if ok else "FAUX")
    assert ok, "G-5 grille : " + comptes["G5"]
    return comptes

def temoins_P7(dossier, w2=None, g=None, p=P):
    """P7 au nominal (gel v12-b2) : FREE exact (H diagonale, Gamma = 0.0
    par construction) ; jumeau |x|^5 borne en MODULE et RELATIF --
    |Gamma_jumeau| <= 1e-2 x Gamma_LS(H) du MEME point, MEME geometrie
    (le L du critere 4.6, LU de l'artefact), DEUX cellules PAR
    TRANSLATION ; monotonie RETIREE (bruit signe). Fail-closed sans
    artefact (D-S2). L'artefact est NOMME par _chemin_point (jamais
    balaye : l'ordre ASCII des noms d'un dossier de run a mordu --
    retrait v16). DENOMINATEUR PAR CELLULE, resolution DECLAREE (E29,
    certification v16 retiree, section 3) : le signal est re-mesure a
    la geometrie de CHAQUE cellule -- cout : une diagonalisation de
    plus par cellule (dim 4225 au nominal) ; ecart mesure contre la
    lecture par-la-mesure : 3.69 pour cent, meme verdict ;
    l'homogeneite jumeau/son-signal est RETENUE, revocable a l'acte."""
    w2 = w2 or Fraction(195, 100)
    g = g if g is not None else g_du_point(w2)
    s = FRACTION_P6 * s_ff(w2, g)
    n1_0, n2_0 = occupations_graine(s, w2, LECTURE_OCCUPATIONS or "reelle")
    sites = barriere(n1_0, n2_0, w2, g, True)
    m2b = sites[-1][0] if sites else 8
    b_M = max(8, m2b)
    r_c = math.ceil(n1_0) + 2 * (m2b + b_M) + 2
    free = {"Gamma_LS": 0.0, "declaration": "chaine deconnectee (g = 0) :"
            " H diagonale exacte, etat de recouvrement max sous r_c,"
            " largeur nulle par construction"}
    # geometrie du critere 4.6 : L RETENU, lu de l'artefact NOMME --
    # jamais re-derive de la formule remplacee (fait c, contre-cert
    # v11), jamais BALAYE (l'ordre ASCII des noms placait P8 avant
    # f070 dans un dossier de run : retrait de la certification v16).
    # Le nom vient de _chemin_point, la fonction qui a ECRIT le point.
    L_ret = None
    ch_pt = _chemin_point(dossier, w2,
                          "f%03d" % round(FRACTION_P6 * 100))
    try:
        d = json.load(open(ch_pt, encoding="ascii"))
        L_ret = (d.get("EB", {}).get("critere_absorbeur", {})
                 .get("L_retenu"))
    except (ValueError, OSError):
        L_ret = None
    if not L_ret:
        contenu = {"FREE": free, "statut": "NON EVALUABLE",
                   "motif": "aucun artefact de point ne porte un L"
                            " retenu (fail-closed, D-S2)",
                   "P7_sain": False}
        ecrire_json_point(os.path.join(dossier, "temoins_P7.json"),
                          contenu)
        return contenu
    eta = abs(float(w2) - 2.0)
    cellules, sain = {}, True
    for nom, rcx in (("r_c", r_c), ("translate", r_c + p)):
        Nx = rcx + L_ret                       # translation : L conserve
        sig = gamma_LS(Nx, w2, g, s, -1, "x5", eta, rcx, p)
        jum = gamma_LS(Nx, w2, g, s, +1, "abs_x5", eta, rcx, p)
        seuil = 1e-2 * sig["Gamma_LS"]
        ok = abs(jum["Gamma_LS"]) <= seuil
        sain = sain and ok
        cellules[nom] = {"signal_H": sig["Gamma_LS"],
                         "jumeau": jum["Gamma_LS"], "seuil": seuil,
                         "marge": (seuil / abs(jum["Gamma_LS"])
                                   if jum["Gamma_LS"] else float("inf")),
                         "passe": ok}
    contenu = {"FREE": free, "L_retenu": L_ret, "jumeau_x5": cellules,
               "seuil_temoin": "1e-2 x Gamma_LS(H) du MEME point, MEME"
                               " geometrie, deux cellules translatees"
                               " (gel v12-b2, sections 5 et 7)",
               "P7_sain": sain}
    ecrire_json_point(os.path.join(dossier, "temoins_P7.json"), contenu)
    return contenu

def _rangs(valeurs):
    """Rangs stricts. Rend None sur ex aequo exact (D-P3) : l'arret est
    route PAR la cascade -- statut consigne, JSON ecrit -- jamais par
    exception. La nulle exacte de Spearman exige des rangs stricts."""
    if len(set(valeurs)) != len(valeurs):
        return None
    tri = sorted(valeurs)
    return [tri.index(v) + 1 for v in valeurs]

def assembler(dossier, carte_chemin, table_chemin=None):
    """Assemblage du gel : P2 consigne, P3 et P6 primaires, P4/P5/P8
    consignes, P7 depuis les temoins, comptes G-5, cascade section 8."""
    fichiers = sorted(fn for fn in os.listdir(dossier)
                      if fn.startswith("pt_") and fn.endswith(".json"))
    pts, p8_pts, site, arrets_sans_index = {}, [], None, []
    for fn in fichiers:
        d = json.load(open(os.path.join(dossier, fn), encoding="ascii"))
        if d.get("statut") == "SITE EXACT":
            site = d
        elif "w2" not in d:
            # D-P3 (E36, la famille) : un point en arret legitime (ex.
            # ARRET Q3) ne porte ni w2 ni g. Il ne s'INDEXE pas -- ni en
            # pts (KeyError w2, site du pre-vol) ni en p8_pts (la cle de
            # tri d['g'] mourait de meme) -- il se CONSIGNE, et l'arret
            # sort par la cascade, jamais par exception.
            arrets_sans_index.append({"fichier": fn,
                                      "statut": d.get("statut", "?"),
                                      "motif": d.get("motif", "")})
        elif "P8" in fn:
            p8_pts.append(d)
        elif fn.endswith("f%03d.json" % round(FRACTION_P6 * 100)):
            pts[float(Fraction(d["w2"]))] = d
    lignes_carte, comptes_carte = lire_carte(carte_chemin)
    carte = {float(Fraction(str(lg["w2"])).limit_denominator(10000)):
             lg["sstar"] for lg in lignes_carte}
    resultat = {"comptes_carte": comptes_carte}
    en_dom = {w: d for w, d in pts.items()
              if d.get("domaine", {}).get("statut") == "EN DOMAINE"
              and not d.get("statut", "").startswith("ARRET")}
    arrets = [w for w, d in pts.items()
              if d.get("statut", "").startswith("ARRET")
              or d.get("statut") == "EXCEPTION"]
    # ---- P2 (consigne) ----
    def _ks(w, cle):
        return pts[w]["EA"][cle] if w in pts and "EA" in pts[w] else None
    p2 = {}
    for nom, (wi, we) in (("gauche", (1.98, 1.95)), ("droite", (2.02, 2.05))):
        if _ks(wi, "K_s_compte") and _ks(we, "K_s_compte"):
            rr = (_ks(wi, "K_s_compte") / _ks(we, "K_s_compte")) / \
                 (_ks(wi, "K_s_ff") / _ks(we, "K_s_ff"))
            p2[nom] = {"rapport_de_rapports": rr,
                       "dans_bande": abs(rr - 1.0) <= TAU_P2}
    p2["lecture"] = ("les deux cotes" if all(v.get("dans_bande")
                     for k, v in p2.items() if k != "lecture")
                     and len(p2) == 2 else "PARTIEL de P2, consigne")
    resultat["P2"] = p2
    # ---- P3 (primaire) ----
    w_p3 = sorted(w for w in en_dom if w in carte)
    n_eff = len(w_p3)
    if n_eff < N_MIN:
        p3 = {"etat": "NON_CONCLUANT", "n_eff": n_eff, "n_min": N_MIN}
    else:
        rq = _rangs([en_dom[w]["EA"]["K_s_compte"] for w in w_p3])
        rc_ = _rangs([carte[w] for w in w_p3])   # sstar en RANG (E27/G-6)
        if rq is None or rc_ is None:
            p3 = {"etat": "ARRET EX AEQUO", "n_eff": n_eff,
                  "motif": "ex aequo exact dans un rang (D-P3, branche 1"
                           " du gel par erratum Q4)"}
        else:
            rho = rho_spearman(rc_, rq)
            rcrit = rho_crit_exact(n_eff, ALPHA)
            p3 = {"etat": "PASSE" if rho >= rcrit else "ECHOUE",
                  "n_eff": n_eff, "rho": str(rho), "rho_crit": str(rcrit),
                  "p_exact": str(p_exact_de_rho(n_eff, rho)),
                  "rangs_quantiques": rq, "rangs_classiques": rc_}
    resultat["P3"] = p3
    # ---- P4 (consigne) ----
    if en_dom:
        residus = {w: math.log(en_dom[w]["EA"]["K_s_compte"]
                               / en_dom[w]["EA"]["K_s_ff"]) for w in en_dom}
        vals = list(residus.values())
        moy = sum(vals) / len(vals)
        std = math.sqrt(sum((v - moy) ** 2 for v in vals) / len(vals))
        resultat["P4"] = {"ecart_type_residu": std, "bande": BANDE_P4,
                          "residu_moyen_consigne": moy,
                          "lecture": ("dans la bande" if std <= BANDE_P4
                                      else "forme fermee = echelle seulement"),
                          "convention": "ecart-type population (ddof = 0),"
                                        " declare"}
        # ---- P5 (secondaire, x/3) ----
        paires = [(1.98, 2.02), (1.97, 2.03), (1.95, 2.05)]
        p5 = {"convention": "signe predit = signe(pente Sigma2 gauche -"
                            " pente Sigma2 droite), DECLARE, a ratifier",
              "paires": []}
        accords = total = 0
        for wg, wd in paires:
            if wg in residus and wd in residus:
                ecart = residus[wg] - residus[wd]
                pg = en_dom[wg]["EA"]["Sigma2"]["pente_S1_moins_S0"]
                pd_ = en_dom[wd]["EA"]["Sigma2"]["pente_S1_moins_S0"]
                pred = 1 if pg > pd_ else -1
                acc = (ecart > 0) == (pred > 0)
                total += 1
                accords += int(acc)
                p5["paires"].append({"paire": [wg, wd], "ecart": ecart,
                                     "signe_predit": pred, "accord": acc})
        p5["resultat"] = "%d/%d" % (accords, total)
        resultat["P5"] = p5
    # ---- P6 (primaire) ----
    w_p6 = sorted(w for w, d in en_dom.items()
                  if d.get("EB", {}).get("faisable"))
    if any(v is None for v in ERRATUMS_CONSIGNES.values()):
        p6 = {"etat": "NON_CONCLUANT",
              "motif": "erratums non consignes (Q1 fraction P6)"}
    elif len(w_p6) < N_MIN:
        p6 = {"etat": "NON_CONCLUANT", "n_eff": len(w_p6), "n_min": N_MIN}
    else:
        rg = _rangs([en_dom[w]["EB"]["Gamma_LS"]["H"]["Gamma_LS"]
                     for w in w_p6])
        rl = _rangs([-en_dom[w]["EA"]["Lambda_c"] for w in w_p6])
        if rg is None or rl is None:
            rg = rl = None
            p6 = {"etat": "ARRET EX AEQUO",
                  "motif": "ex aequo exact dans un rang (D-P3, Q4)"}
            resultat["P6"] = p6
            rho6 = None
        else:
            rho6 = rho_spearman(rl, rg)
        if rho6 is None:
            rc6 = viol = None
        else:
            rc6 = rho_crit_exact(len(w_p6), ALPHA)
            viol = sum(1 for w in w_p6
                   if en_dom[w]["EB"]["Gamma_LS"]["H"]["Gamma_LS"]
                       - en_dom[w]["EB"]["Gamma_LS"]["Hplus"]["Gamma_LS"]
                       <= 0)
        if rho6 is not None:
            etat6 = "PASSE" if (rho6 >= rc6 and viol == 0) else "ECHOUE"
            p6 = {"etat": etat6, "n_eff": len(w_p6), "rho": str(rho6),
                  "rho_crit": str(rc6), "violations_ii": viol,
                  "p_exact": str(p_exact_de_rho(len(w_p6), rho6))}
    resultat["P6"] = p6
    # ---- P7 ----
    ch_t = os.path.join(dossier, "temoins_P7.json")
    p7_sain = False
    if os.path.exists(ch_t):
        tem = json.load(open(ch_t, encoding="ascii"))
        p7_sain = bool(tem.get("P7_sain"))
        resultat["P7"] = {"sain": p7_sain}
    else:
        resultat["P7"] = {"sain": False, "motif": "temoins non exerces"}
    # ---- P8 (consigne) ----
    p8v = [(d["g"], d["EA"]["Gamma_c"]["val"], d["EA"]["card_Bc"])
           for d in sorted(p8_pts, key=lambda x: -x["g"])
           if "EA" in d and "Gamma_c" in d.get("EA", {})]
    if len(p8v) == 3:
        xs = [math.log(gv) for gv, _, _ in p8v]
        ys = [math.log(max(vv, 1e-300)) for _, vv, _ in p8v]
        xm, ym = sum(xs) / 3, sum(ys) / 3
        pente = sum((x - xm) * (y - ym) for x, y in zip(xs, ys)) / \
            sum((x - xm) ** 2 for x in xs)
        bc_med = p8v[1][2]
        resultat["P8"] = {"pente_loglog": pente, "card_Bc_g_median": bc_med,
                          "ecart": abs(pente - 2 * bc_med),
                          "bande": BANDE_P8, "verdict": "aucun (secondaire)"}
    # ---- G-9 et arret ----
    g9 = [w for w, d in en_dom.items() if d.get("EB", {}).get("G9_mordue")]
    ex_aequo = [nom for nom, bloc in (("P3", p3), ("P6", p6))
                if bloc.get("etat") == "ARRET EX AEQUO"]
    resultat["arret_ex_aequo"] = ex_aequo
    g4_etats = sorted([str(w), d.get("EB", {}).get("G4", {})
                       .get("statut", "ABSENTE")]
                      for w, d in en_dom.items())
    g4_mordus = [w for w, d in en_dom.items()
                 if d.get("EB", {}).get("G4", {}).get("mordu")]
    arret = (bool(arrets) or bool(g9) or not p7_sain or bool(ex_aequo)
             or bool(g4_mordus) or bool(arrets_sans_index))
    resultat["arrets_points"] = arrets
    resultat["arrets_sans_index"] = arrets_sans_index
    resultat["G9_points"] = g9
    resultat["G4_points"] = g4_etats
    resultat["G4_mordues"] = g4_mordus
    resultat["verdict"] = verdict(p3.get("etat", "NON_CONCLUANT"),
                                  p6.get("etat", "NON_CONCLUANT"),
                                  p7_sain, arret)
    ecrire_json_point(os.path.join(dossier, "assemblage.json"), resultat)
    return resultat

def piloter(dossier):
    """Gel 11.4 : quatre points, quatre chemins."""
    os.makedirs(dossier, exist_ok=True)
    w2n = Fraction(195, 100)
    s8 = P8_FRACTION * s_ff(P8_W2, g_du_point(P8_W2))
    chemins = [
        ("a_site", lambda: point_site_exact()),
        ("b_nominal", lambda: mesurer_point(w2n, g_du_point(w2n),
                                            FRACTION_P6, avec_EB=True)),
        ("c_hors_domaine", lambda: mesurer_point(
            Fraction(1414214, 1000000), 0.05, FRACTION_P6, avec_EB=False)),
        ("d_EB_infaisable_P8", lambda: mesurer_point(
            P8_W2, P8_G[-1], P8_FRACTION, avec_EB=True,
            s_absolu=s8, exempt_G1=True)),
    ]
    sorties = {}
    for nom, f in chemins:
        r = f()
        ecrire_json_point(os.path.join(dossier, "pilote_%s.json" % nom), r)
        sorties[nom] = r.get("statut", "?")
        eb = r.get("EB", {})
        print("pilote %-22s -> %-28s%s" % (nom, sorties[nom],
              (" ; EB faisable=%s" % eb.get("faisable")) if eb else ""))
    return sorties


# ---------------------------------------------------------------------------
# BANC (section 9) -- scenarios legers executables sans moteur ; les lourds
# (S-D, S-H, matrice complete) au pre-vol machine 2, ce script les PORTE.
# ---------------------------------------------------------------------------
def banc_leger():
    resultats = {}
    # S-A : chaine deconnectee
    r = mesurer_point(Fraction(195, 100), 0.0, 0.70, avec_EB=False)
    assert r["statut"] == "CHAINE DECONNECTEE" and r["Gamma"] == 0.0
    resultats["S-A"] = "deconnectee detectee avant toute barriere"
    # site exact (P1)
    r = mesurer_point(Fraction(2), 1e-3, 0.70, avec_EB=False)
    assert r["statut"] == "SITE EXACT"
    resultats["P1"] = "site exact route avant tout calcul"
    # S-B : rapport compte / rapport ff, paire gauche -- LES DEUX lectures
    # (Q3) : la paire de nombres est la piece de la question, pas un choix
    rapports_B = {}
    for lec in ("reelle", "entiere"):
        kq, kf = {}, {}
        for w2 in (Fraction(198, 100), Fraction(195, 100)):
            g = g_du_point(w2)
            sQ = seuil_A4(w2, g, lecture=lec)["s_star_Q"]
            kq[w2] = g * sQ ** (P - 2)
            kf[w2] = K_s_ff(w2, g)
        rapports_B[lec] = (kq[Fraction(198, 100)] / kq[Fraction(195, 100)]) / \
                          (kf[Fraction(198, 100)] / kf[Fraction(195, 100)])
    assert abs(rapports_B["reelle"] - 1.0) <= 0.05, \
        "S-B reelle : %.4f" % rapports_B["reelle"]
    assert abs(rapports_B["entiere"] - 1.0) > 0.05, \
        "S-B entiere : %.4f -- devrait echouer (Q3)" % rapports_B["entiere"]
    resultats["S-B"] = ("paire gauche, deux lectures (Q3) : reelle %.4f"
                        " (PASSE), entiere %.4f (ECHOUE, attendu)") % (
        rapports_B["reelle"], rapports_B["entiere"])
    # S-C, forme machine 2 (note 202bc80e, executee) : signe de delta_des
    # en parametre a w2 FIXE, trois assertions, trois branches atteintes.
    w2 = Fraction(195, 100); g = g_du_point(w2)
    n1_0, n2_0 = occupations_graine(0.70 * s_ff(w2, g), w2, "reelle")
    # (i) premier ordre seul : invariance AU BIT sous delta -> -delta
    bp = barriere(n1_0, n2_0, w2, g, False, signe_delta=+1)
    bm = barriere(n1_0, n2_0, w2, g, False, signe_delta=-1)
    assert len(bp) == len(bm), "S-C(i) : cardinaux premier ordre"
    Lp, Lm = Lambda_action(bp), Lambda_action(bm)
    assert Lp == Lm, "S-C(i) : Lambda premier ordre non bit-identique"
    # (ii) Sigma2 actif : la difference EXISTE (P5 en a besoin)
    bps = barriere(n1_0, n2_0, w2, g, True, signe_delta=+1)
    bms = barriere(n1_0, n2_0, w2, g, True, signe_delta=-1)
    Lps, Lms = Lambda_action(bps), Lambda_action(bms)
    assert (len(bps) != len(bms)) or (Lps != Lms), \
        "S-C(ii) : Sigma2 actif sans effet de signe"
    # (iii) mutation d'un t_m -> Lambda change (MORD)
    bmu = barriere(n1_0, n2_0, w2, g, True, signe_delta=+1,
                   facteur_t={bps[0][0]: 1.07})
    Lmu = Lambda_action(bmu)
    assert Lmu != Lps, "S-C(iii) : mutation t_m non detectee"
    resultats["S-C"] = ("signe en parametre : premier ordre bit-identique"
                        " (%.6f) ; Sigma2 actif %d vs %d sites, Lambda %.4f"
                        " vs %.4f ; mutation t -> %.4f MORD") % (
        Lp, len(bps), len(bms), Lps, Lms, Lmu)
    # S-G : hors domaine (point M7-M9) et en domaine (nominal)
    r = mesurer_point(Fraction(1414214, 1000000), 0.05, 0.70, avec_EB=False)
    assert r["statut"] == "HORS DOMAINE", "S-G : M7-M9 non renvoye"
    r2 = mesurer_point(w2, g, 0.70, avec_EB=False, lecture="reelle")
    assert r2["domaine"]["statut"] == "EN DOMAINE", "S-G : garde renvoie le nominal"
    resultats["S-G"] = "M7-M9 renvoye ; garde du nominal EN DOMAINE (D1 %.3f,"         " c_max %.3f)" % (r2["domaine"]["D1"], r2["domaine"]["c_max"])
    # CONSTAT : EA.Gamma_c = operatif (D-S3), temoin nomme, arret D-S2
    op = r2["EA"]["Gamma_c"]; tem = r2["EA"]["Gamma_c_temoin_clause_4_7"]
    resultats["S-E constat"] = ("statut nominal = %s (motifs : %s) ;"
        " EA.Gamma_c operatif %.4e (eta |d|x%g, %d pas, stat M desc %.1e,"
        " residu %.4f, Richardson %.4e) ; temoin 4.7 : %.4e, ecart"
        " doublement %.3f") % (
        r2["statut"], "; ".join(r2.get("motifs_arret", [])) or "aucun",
        op["val"], op["eta_final_facteur"], len(op["pas"]),
        op["stationnarite_M_descente"], op.get("residu_estime", float("nan")),
        op.get("Gamma_Richardson", float("nan")),
        tem["val"], tem["ecart_doublement"])
    # S-F, forme machine 2 (note 202bc80e, executee) : hors-diagonale
    # bit-identique H/H+, diagonale differente, mutation d'un V -> MORD.
    N_sf = 6
    HH, _ = H_2D(N_sf, w2, g, signe_fantome=-1)
    HP, _ = H_2D(N_sf, w2, g, signe_fantome=+1)
    hors_H = HH - np.diag(np.diag(HH))
    hors_P = HP - np.diag(np.diag(HP))
    assert np.array_equal(hors_H, hors_P), "S-F : hors-diagonale differe"
    nb_hd = int(np.count_nonzero(hors_H))
    nb_diag = int(np.count_nonzero(np.diag(HH) != np.diag(HP)))
    assert nb_diag > 0, "S-F : le signe fantome n'agit pas sur la diagonale"
    HHm = hors_H.copy()
    i_m, j_m = np.argwhere(HHm != 0)[0]
    HHm[i_m, j_m] *= (1.0 + 1e-9)
    assert not np.array_equal(HHm, hors_P), "S-F : mutation V non mordue"
    resultats["S-F"] = ("hors-diagonale bit-identique (%d elements non"
                        " nuls) ; diagonale differente sur %d/%d ;"
                        " mutation V MORD") % (nb_hd, nb_diag, N_sf * N_sf)
    print("BANC LEGER : %d scenarios PASSES" % len(resultats))
    for k in sorted(resultats):
        print("  - %s : %s" % (k, resultats[k]))
    print("comptes banc : %d + 0 sabotes survivants == %d" %
          (len(resultats), len(resultats)))
    return True

# ---------------------------------------------------------------------------
# Entree
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "--selftest"
    if mode == "--selftest":
        selftest()
    elif mode == "--banc-leger":
        selftest()
        banc_leger()
    elif mode == "--point":
        w2 = Fraction(sys.argv[2]); g = float(sys.argv[3]); fr = float(sys.argv[4])
        lec = None
        if "--lecture" in sys.argv:
            lec = sys.argv[sys.argv.index("--lecture") + 1]
        r = mesurer_point(w2, g, fr, avec_EB=("--sans-eb" not in sys.argv),
                          lecture=lec)
        print(json.dumps(r, sort_keys=True, indent=1, default=str))
    elif mode == "--pilote":
        piloter(sys.argv[2])
    elif mode == "--run":
        d = sys.argv[2]
        comptes = mesurer_manche(d)
        print("comptes grille :", comptes["G5"])
        temoins_P7(d)   # p = P par defaut : la manche est p = 5 ;
        #   p s'expose au banc par la fonction (contre-cert v9, res. 2)
        print("temoins P7 ecrits")
    elif mode == "--assemblage":
        d = sys.argv[2]
        carte = sys.argv[sys.argv.index("--carte") + 1]
        r = assembler(d, carte)
        print("P3 =", r["P3"].get("etat"), "; P6 =", r["P6"].get("etat"),
              "; verdict =", r["verdict"])
    else:
        raise SystemExit("modes : --selftest | --banc-leger | --point w2 g"
                         " fraction | --pilote D | --run D | --assemblage D"
                         " --carte C")
