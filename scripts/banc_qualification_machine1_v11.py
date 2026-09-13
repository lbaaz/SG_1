#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
banc_qualification_machine1_v4.py -- L'INSTRUMENT DES DEUX VOLETS DU BANC
DE LA CONSTANTE A (delta' = 1/44100 ; v11 = v10 certifie + levee de D-v10-1 : le
controle 9bis compare sur la SERIALISATION, construction_banc_v11_machine2_v1.py ;
v9 = v8 certifie re-parametre au gel v6 ;
v10 = v9 + levee de D-v9-1 : le synthetique du banc demarre sa phase 2 au pas de
grille INFERIEUR a la bascule ; pin sur le gel v7 = v6 + 5 hunks derives ou mesures ;
construction_banc_v10_machine2_v2.py, machine 2)
================================================================================
Version 4. Redaction MACHINE 1 -- la main est dans le nom (N-65).
Version 4 = version 3 (5fae2a8c94cf8685, CERTIFIEE 10d3160eef210015 sous
v7/v5, DEPOSEE a4a907a) + le cahier FIGE par les gels du banc de la
constante A -- gel constante A v4 (011c923203fcdaef, sections 4, 4.9, 5,
7, 8, 10), gel temoin v11 (a2e7ef3e237c5acf, sections 3, 5.2, 5.4, 8, 9bis) --
et RIEN d'autre :
  - D-M17-51 : les deux en-tetes de section perimes (l.1281, l.1714 de la
    v3) citent desormais les gels qu'ils servent ;
  - D-M17-58 : la garde de signe au pre-vol, table_factice[(p, w2, sgn)]
    == sF, jouee sur la table AVANT le moteur factice ; scenario de banc ;
  - delta := delta' = 1/44100 (gel v6, 3 : DERIVE de la tenaille) ; delta_0 = 1/100
    reste un REPERE (v4 3.2, v9 3) ; TOUTES les grandeurs derivees se
    recalculent par leurs propres formules ; les seuils de bascule 5.3
    (etage 2a) et la phase grossiere de W-bascule restent a delta_0 ;
  - les ETAGES sur-seuil (2a, 2b ; v4 4.2) et sous-seuil (2s, 2b' ancres
    en t depuis T_MAX ; v4 4.7, t_start LU du journal de phase 1, jamais
    recalcule -- R-A-5) ; l'etat complet a CHAQUE depart d'etage,
    empreinte convention B (v4 4.9, exigence NEUVE) ;
  - AUCUN compte d'etage asserte : les comptes se MESURENT et se
    consignent ; toute garde de compte se compare a l'intervalle DERIVE
    (v4 4.6/4.7 au pas nominal, 4.8 pour la jumelle : bornes x 2) ; hors
    intervalle -> G-fen (motif : compte d'etage) ;
  - W-bascule EN VOIE A (v9 8, arbitrage operateur) : g1 la phase
    grossiere du v7 (de k' tau_dom_0 a k tau_dom_0, dt_1), g2 l'etage 2a
    (de k tau_dom_0 a k tau_dom', pas k tau_dom'/M), lecture D-t-19
    ECRITE sur la tolerance 5.3 (iv) ; comptes mesures ;
  - la branche 3b : G-plancher (v4 7) -- tol_lnA(p) <= plancher_lnA(p)
    -> NON CONCLUANT DE PLANCHER ; comparaison de bord exacte par
    propagation du double (v4 7, regle 15) ;
  - le controle de reproductibilite 9bis (v9) : perimetre ENUMERE ET
    CLOS /T1 /T1b /T3a /T3b a profondeur declaree, exemptions duree/
    chemins A L'INTERIEUR, tout le reste hors perimetre PAR CONSTRUCTION ;
    ecart -> NON CONCLUANT D'INSTRUMENT avant toute lecture de verdict ;
  - L-desc (v4 9) : les dix-huit rapports contre la cellule du plan du
    85 (6d7d23130e9322f8), CONSIGNES, portee a un seul sens rappelee ;
  - le banc des gardes s'etend : branche 3b, etage 2a, etage 2s,
    W-bascule voie A (g2 absente casse la remise d'etat), garde
    D-M17-58, n_2s > n_nominal SANS morsure, 9bis (mord au perimetre, muet
    hors perimetre et sur les exemptes).
  Physique, transcription, ajustements, temoin T-1/T-1b/T-3 : INCHANGES
  (sans delta, v9 2 ; leur rejeu A L'IDENTIQUE est l'objet de 9bis).
Version 3 = version 2 (d74928ef093c96d0, CERTIFIEE sous les gels v5/v2 par
10d3160eef210015) + l'ERRATUM GROUPE des gels (arbitrage de l'operateur du
28/08 : faits 1, 3, 4, 5 ; fait 2 dissous par le fait 5), et RIEN d'autre :
  - quatre ancres neuves (gel temoin v7, gel alpha v5, leurs deux
    certifications machine 1) ; les anciennes ancres sont PERIMEES ;
  - temoin v7 : T-1 = 2 etats x 2 flots (dt, dt/2), ATTENDUS 41 ; les
    flots a dt/2 ne servent qu'a W-integrales ; q_int = log2(derive(dt)/
    derive(dt/2)) lu contre 4 pour H1 et N sur chaque etat, tol_int =
    log2((1+b)/(1+b/2)), b = omega_max dt, omega_max^2 = w^2 + 3 lambda
    x_max^2 lu sur le flot a dt, plafond eta x 1, consigne ; une morsure
    mene a la branche 6 et jamais ailleurs ;
  - alpha v5, 10.3 : plancher_lnA(p) = delta/((alpha_p+2)(alpha_p+3)) ;
    tol_lnA(p) = max(dispersion, plancher) ; tol_lnA/plancher consigne ;
  - alpha v5, 10.1bis : G-dt et G-k comparees au plafond eta x 8/15,
    ecart/(8/15) consigne, role diagnostique (le motif nomme la composante)
    -- c'est la lecture LD-15 de la v2, desormais TEXTE de gel ;
  - alpha v5, 4.4 : chaque point se joue a sgn = frag de la carte (+1 la
    ou sM est absent, p = 4) : phase 1, phase 2, G-seuil, G-lignee et le
    moteur appele tel quel, tous au MEME signe ; frag, asym, sgn consignes
    par point ; lire_carte lit sP, sM, frag, asym et controle sF = min ;
  - pre-vol : table factice par (p, w2, sgn) ;
  - LD-16 (heritee) : si derive(dt/2) tombe sous le plancher machine
    c_pl x eps x N_pas -- lecture SOUS LE DEPOT 9bis, clause v7-5.4
    ABROGEE par la v11 (D-v5-1) -- q_int n'est pas lisible :
    W-integrales NON LUE (plancher), consignee, jamais une morsure
    d'arrondi ; scenario de banc.
  Le banc des gardes demontre desormais 16/16 (W-integrales comprise).
  Physique, transcription, ajustements, cascades hors les points nommes :
  INCHANGES.
Version 2 = version 1 (3a932eabfaaf4307) + les QUATRE correctifs de la
certification machine 2 (note 3f017a997b0b1812, etiquettes D-b-1..D-b-4,
numeros a l'acte), et rien d'autre :
  D-b-1  aucune mention d'outillage ; date_utc sans avertissement (la
         depreciation imprimait un chemin absolu)
  D-b-2  le journal dit ce qu'il NE JOUE PAS (section NE-JOUE-PAS, trois
         listes ENUMEREES par la machine : lectures NON LUES, gardes sans
         morsure demontree dans CE journal, runs du gel non joues)
  D-b-3  onze scenarios de banc de plus, un par garde nue (W-pas,
         W-plancher, W-bascule, W-croissance, 3bis x2, 4bis, G-dt, G-k,
         G-w2, G-fen, G-comptes) ; le banc des gardes se rejoue a la fin
         de CHAQUE run, et c'est lui qui remplit la liste de D-b-2
  D-b-4  l'etat tangent est REFUSE (H1_0 = 0 ou N_0 = 0 -> ARRET declare),
         et un scenario l'asserte
Un seul script, deux modes :
  --mode temoin  : le TEMOIN NEGATIF CLASSIQUE (Damour-Smilga, classe (i))
  --mode alpha   : la VERIFICATION alpha = 4/(p-2) (exposant du profil)
et trois modes d'instrument : --selftest, --banc (le banc qui tue), --prevol
(pre-vol a moteur factice, sorties SEPAREES).

ANCRES E19 (ce run n'est opposable que si l'instrument cite ces empreintes
dans une certification croisee anterieure a son depot) :
  gels/constante_A_pre_enregistrement_v4.md      011c923203fcdaef  30988 o  CERTIFIE
    par journal/note_machine2_certification_constante_A_v4_v1.md 9e6376f936708077 11359 o
  gels/temoin_negatif_pre_enregistrement_v11.md  a2e7ef3e237c5acf  72281 o  CERTIFIE
    par journal/note_machine1_certification_temoin_v11_v2.md 7fc5f2412b99ad50 3569 o
    (lignee : v9 403488b4f6c319e9 certifiee, superseded par la v11)
  v8 : reprise D-I-8/9 sur certification m2 75dac8f41c0c3bb8 --
    la borne dans UNE constante (BORNE_ULP) citee partout ;
    ecart_ulp en PAS REPRESENTABLES (forme de l'audit m2, verbatim).
  v7 : reprise D-I-6/7 sur certification m2 483577e0a55eeecc --
    bornes 2 / 2 a PORTEE ECRITE (x'' pow inter-machines ; D''
    re-association inter-plumes ; regime de 7 (i) = le cumul), puis
    la garde CABLEE dans transcription_ok : l'ordre etait contraint.
  v6 : reprise D-I-3/4/5 sur certification m2 c5c66dd19e24d278 ;
    c_pl NON EMIS ; W-transcription (2.11) : TIRAGE opposable au bit,
    CHAMP compare SUR LES NOMBRES (bornes derivees 0 / 2 ulp)
  BASES par citation (les deux gels ci-dessus les citent, PB-1) :
  gels/temoin_negatif_pre_enregistrement_v7.md   8b083e9f109b5a8e  39750 o  CERTIFIE
    par journal/note_machine1_certification_gels_v7_v4.md  6b2425dbf906205b  6247 o
  gels/alpha_pre_enregistrement_v5.md            045c2435aaf623ce  28998 o  CERTIFIE
    par journal/note_machine1_certification_gel_alpha_v5.md fe43f7c4d142bcdb 3205 o
  (convention B : sha256 du fichier NFC+LF, saut de ligne final inclus, 16 hex)
  Lignee des gels : temoin v5 0905a9b78ba40349 (DEPOSEE 37ad1b6, perimee),
  v6 e9a7e7e2e2ed0354 (non certifiee) ; alpha v2 35a70834b2a34514 (DEPOSEE,
  perimee), v3 3dad1c34b54bb9c3, v4 c261b6a5f34262e5 (non certifiees).
  registre ordonnant lbaaz/SG_1 : a89f6cf (delta 83) ; 9c95a3d (delta 84,
  N-68 N-69 E42) ; 37ad1b6 (v5/v2 deposees comme BANCS, N-69) ; les
  ancres v7/v5 sont a deposer par l'operateur AVANT tout run sous la v3.

PB-1 -- LE MOTEUR DEPOSE N'EST NI EDITE NI COPIE :
  scripts/m9_replication_v1.py  sha256 brut
    c8ed357b120352c4d1078307add3eaac285940c8bec00acc2ddc9ff386ab2c5c  36325 o
  Sa physique est TRANSCRITE aux lignes citees :
    l.278  DT, T_MAX, CAP = 0.006, 400.0, 1.0e4
    l.279  NGRID, NPASSES, NDENSE = 48, 3, 96
    l.280  LO0, HI0, MAX_ELARG = 0.05, 6.0, 8
    l.323-325  grad_rapide : g (x1 + x2)^(P-1), pour les deux composantes
    l.339-348  integrer : etat initial (l.342-343), acc (l.346-348)
    l.351-361  le pas RK4 (transcrit AU MOT, meme association des operations)
    l.362-363  le test d'explosion : ~isfinite OU max(|x1|, |x2|) > CAP
    l.372-401  chercher_seuil : grille NGRID, elargissement x4 jusqu'a
               MAX_ELARG, NPASSES-1 raffinements, passe DENSE NDENSE
  Pour G-lignee (gel alpha 5.6) et pour le controle de transcription de
  l'algorithme (temoin 4.6bis), le moteur est CHARGE (empreinte exigee,
  patron m12_pilote_v3.py l.483-518) et APPELE TEL QUEL. Deux globales du
  module sont re-liees a l'appel, jamais le fichier : P (patron depose,
  m12_pilote_v3.py l.576-582) et T_MAX (pour rendre ACCESSIBLE l'indice de
  pas d'explosion : integrer() ne rend qu'un booleen ; avec T_MAX = n dt il
  rend "explose avant le pas n", et l'indice est le plus petit n vrai).

CARTE :
  runs/m12_results.json  sha256 brut
    fa109da92e582520cfcb63b46bc41fa7d4b62295891f413bb97c6095b2fe59b1  130856 o
    (= 389b270b9f5b145c en convention B, CRLF -> LF)
  Les neuf s* sont LUS (cle 'p|w2', champ sF) et controles par valeur
  contre la table du gel alpha 4.2 (regle 11).

CE QUE LE GEL LAISSE A L'INSTRUMENT, ET QUE L'INSTRUMENT DECLARE (numeros a
l'acte ; chaque lecture porte son etiquette LD-n dans le code) :
  LD-1  T-1, tolerance de R : y_j = t_c(CAP_j)/CAP_j sur les cinq plafonds,
        disp = (max y - min y)/moyenne y, tol_R = q x disp (gel temoin 8 :
        "de la dispersion de t_c/CAP mesuree sur l'echelle"). Fenetre de q :
        |R_j - q| <= tol_R pour les quatre rapports ; fenetre de 1 :
        |R_j - 1| <= tol_R. Plafond eta_R (q-1) et tol_R/(q-1) consigne.
  LD-2  T-1, "R -> 1 (saturation)" (branche 3) : lu SANS tol_R (un t_c qui
        sature rend tol_R sans valeur, D-t-4) : les R_j sont non croissants
        ET |R_dernier - 1| <= eta_R (q-1) -- a la resolution du banc.
        Ordre de lecture de la cascade : 1, 2, 3, 3bis, 4, 4bis, 5, 6.
  LD-3  T-1b : base (CAP, T_MAX) = (100, 200) et etat A, lus a la table
        gelee de 4.6 (l.363-366 ; seuils 0.49..1.95, k = 0 attendu).
        Tolerances (4.6bis (iv)) : tol_loi1 = q [pas_a/s_a + pas_b/s_b +
        osc], tol_loi2 = (1/c_T) [pas_a/s_a + pas_c/s_c + osc], avec osc =
        max_T (T - t_pic(T))/T, t_pic(T) = instant du maximum de |D_1| sur
        [0, T], lu sur le flot A de T-1 (meme etat, meme pas, aucun run de
        plus). Plafonds eta (q-1) et eta (1 - 1/c_T).
  LD-4  W-pas (5.3 (iv)) : tol_ordre = log2((1 + b)/(1 + b/2)), b = (alpha
        + q_s + 1)/M, q_s = 4 l'ordre du schema : le terme suivant de
        l'erreur globale porte une derivee de plus, et pour tau^(-alpha)
        deux derivees consecutives sont dans le rapport (alpha + n)/tau, au
        pas dt_2 = tau_CAP/M. Plafond : eta x (ecart entre ordres
        consecutifs = 1) = 1/4 ; tol_ordre/1 consigne.
  LD-5  5.3 (iv) "e(dt_2) <= tol_alpha x ln 10" : tol_alpha n'existe pas
        avant la manche alpha (gel alpha 10.1). Le temoin lit la forme la
        plus faible, tol_alpha = PLAFOND 2/15 (gel alpha 10.2), et CONSIGNE
        e(dt_2)/ln 10 par point = la plus petite tolerance alpha que le pas
        resout. En mode alpha, la porte relit ces neuf valeurs et exige
        tol_alpha(p) >= max_w2 e(dt_2)/ln 10, sinon NON CONCLUANT DE
        RESOLUTION : c'est la clause de 5.3 (iv), jouee des deux cotes.
  LD-6  W-bascule (8) : "meme approche de la solution exacte des deux
        cotes" = e_avec(dt_2) <= tol_alpha x ln 10 comme en LD-5, et
        e_avec/e_sans consigne.
  LD-7  W-plancher (5.4) : plancher machine = eps_64 x N_pas(dt_2/2)
        (l'accumulation d'arrondi au pire), c_pl fois au-dessus exige.
  LD-8  T-2a (1 run) : w2 = 2.27 (colonne mediane), a = b = 1, phi = 0,
        horizon 2 pi / w1 (une periode lente), dt_1 ; e = max|x - x_ex| /
        (a + b) ; PASSE ssi e <= tol_alpha x ln 10 (diagnostic, jamais une
        porte). T-2b (3 runs) : equation tronquee integree en vecteur
        (x, x', x'', x''') au pas dt_2 de w2 = 2.27, fenetre [k tau_dom,
        tau_CAP] ; meme critere. T-3b (3 runs) : Duffing x-secteur, (w,
        lambda, x0) = (1,1,1), (1,1,2), (1,1,4), horizon 10 periodes de la
        forme fermee (4 K(m)/Omega), dt_1 ; e = max|x - x0 cn| / x0.
  LD-9  (FERMEE par le gel temoin v7) : la v5 lisait W-integrales sur dt
        contre dt/2 sans compter de flot a dt/2 ; la v7 compte les deux
        flots (T-1 = 4, ATTENDUS 41) et ecrit tol_int. La v3 joue 41 et
        lit W-integrales. L'etiquette reste pour l'historique de l'acte.
  LD-10 alpha, G-seuil (8) : "derniere fenetre de largeur (tau_dom -
        tau_CAP) avant T_MAX" = phase 1 (dt_1) jusqu'a T_MAX - (tau_dom -
        tau_CAP), puis phase 2 (dt_2) jusqu'a T_MAX (la trajectoire compte
        comme phase 2, 4.5). Si la bascule mord sous le seuil, elle est
        consignee et la trajectoire se traite comme un point du plan.
  LD-11 alpha, ajustements (7) : t* par minimisation 1-D de la somme des
        carres residuels (balayage de 64 points en log(t* - t_max) puis
        section doree), t* dans (t_max_fenetre, t_dernier + 2 tau_dom].
        Exposant local : entre points consecutifs de la fenetre ;
        dispersion = max - min. G-fen sur le nombre de points : n_min =
        floor((tau_dom - tau_CAP)/dt) - 1. Appartenance a la fenetre a
        1e-6 dt pres aux deux bornes (un point pose sur une borne ne doit
        pas basculer au dernier bit de t*).
  LD-12 alpha, P-A (10.3, v5) : dispersion_lnA(p) = max sur les six
        points de (max - min) de ln A_II sur la grille jouee {(dt_2, k=2),
        (dt_2/2, k=2), (dt_2, k=4)} ; tol_lnA(p) = max(dispersion_lnA(p),
        plancher_lnA(p)), plancher_lnA(p) = delta/((alpha_p+2)(alpha_p+3))
        (TEXTE de gel, v5) ; P-A au point ssi |ln(g A_II^(p-2) / K)| <=
        (p-2) tol_lnA(p) -- le (p-2) n'est QUE la ; tol_lnA/plancher
        consigne par degre. Ce qui reste de lecture : la grille jouee
        (trois coins sur quatre, 4.5) et le "max sur les six points".
  LD-13 alpha, G-lignee : le test de phase 1 sans bascule est LE TEST
        DEPOSE (l.362-363, max(|x1|,|x2|) > CAP = 1e4), que le gel 5.6
        abrege en "|x| >= 1e4" ; la phase 1 du plan s'arrete a la BASCULE
        (|x1 + x2| >= x_b) et n'applique pas le CAP depose (5.3).
  LD-14 alpha, 5.6 "meme indice de pas d'explosion la ou il est
        accessible" : rendu accessible par re-liaison de T_MAX (voir PB-1
        ci-dessus) ; controle joue aux 18 points sur-seuil.
  LD-15 (v2, ABSORBEE par le gel alpha v5, 10.1bis) : G-dt et G-k au
        plafond eta x 8/15 ; l'etiquette reste pour l'acte.
  LD-16 temoin v7, W-integrales au plancher machine : derive(dt/2) <
        c_pl x eps_64 x N_pas(dt/2) (lecture SOUS LE DEPOT 9bis ;
        clause v7 abrogee par la v11, D-v5-1) rend
        q_int NON LISIBLE pour cette integrale ; W-integrales est alors
        NON LUE (plancher) sur cette integrale, consignee, et ne mord pas.
        Une morsure d'arrondi serait un faux echec, et un faux echec vaut
        un controle vide. Scenario de banc.

DISCIPLINE : N-59 (empreinte ET taille de la copie executee, avant
lancement) ; N-61 (chaque mesure sur une ligne de journal etiquetee) ;
N-62 ; N-66 (aucune reprise : l'instrument n'en a pas) ; E18 (aucun
numero pris ici : files en MAXIMUM CITE au registre 37ad1b6 -- E42, N-69,
D-M17-45) ; regle 15 (Fraction aux bornes exactes) ; comptes en forme
derivee ; tout fichier ecrit est ASCII/LF et entre au MANIFEST.
"""
import argparse
import datetime
import hashlib
import importlib.util
import json
import math
import os
import sys
import time
import unicodedata
from fractions import Fraction

import numpy as np

VERSION = "banc_qualification_machine1_v11"

# =====================================================================
# 0. ANCRES (E19, PB-1) ET NOMBRES PURS (regle 15 : Fraction)
# =====================================================================

GEL_TEMOIN = ("gels/temoin_negatif_pre_enregistrement_v11.md", "a2e7ef3e237c5acf", 72281)
GEL_ALPHA = ("gels/constante_A_pre_enregistrement_v7.md", "a2b8463372e1f906", 41061)
CERT_TEMOIN = ("journal/note_machine1_certification_temoin_v11_v2.md", "7fc5f2412b99ad50")
CERT_ALPHA = ("journal/note_machine2_certification_constante_A_v4_v1.md", "9e6376f936708077")
GEL_TEMOIN_BASE = ("gels/temoin_negatif_pre_enregistrement_v7.md", "8b083e9f109b5a8e", 39750)
GEL_ALPHA_BASE = ("gels/alpha_pre_enregistrement_v5.md", "045c2435aaf623ce", 28998)
CERT_TEMOIN_BASE = ("journal/note_machine1_certification_gels_v7_v4.md", "6b2425dbf906205b")
CERT_ALPHA_BASE = ("journal/note_machine1_certification_gel_alpha_v5.md", "fe43f7c4d142bcdb")
MOTEUR = ("scripts/m9_replication_v1.py",
          "c8ed357b120352c4d1078307add3eaac285940c8bec00acc2ddc9ff386ab2c5c", 36325)
CARTE = ("runs/m12_results.json",
         "fa109da92e582520cfcb63b46bc41fa7d4b62295891f413bb97c6095b2fe59b1", 130856)
FILES_MAX_CITE = "E42, N-69, D-M17-45 (registre 37ad1b6, pieces .md/.txt)"

# Herites du moteur depose (l.278-280), et controles a la charge.
DT1, T_MAX_DEPOSE, CAP_DEPOSE = 0.006, 400.0, 1.0e4
NGRID, NPASSES, NDENSE = 48, 3, 96
LO0, HI0, MAX_ELARG = 0.05, 6.0, 8
W1, G_REF = 1.0, 0.05

# Gel constante A v6, sections 3 et 6 -- delta' DERIVE de la tenaille (la derivation est
# le nombre) ; b et m sont les DEUX SEULS purs de conception ; delta_0 est
# un REPERE, pas un reglage (v4 3.2, temoin v9 3).
DELTA = Fraction(1, 44100)
B_DESC, M_MARGE, J_DESC = 21, 1, 2              # gel v6 3.2 : delta' = delta_0 / 21^2 ; m derive = 1.52 > M_MARGE
DELTA_0 = DELTA * B_DESC ** J_DESC          # = 1/100, le delta du 85
# Gel alpha v5, section 6 -- les autres purs, inchanges (v4 6).
R_CAP = Fraction(1, 10)
M_PAS = 20
K_BASC = 2
ETA = Fraction(1, 4)
K_GARDE = 4                       # G-k joue k = 4 (gel alpha 6)
PLAFOND_ALPHA = ETA * Fraction(8, 15)          # 2/15 (gel alpha 10.2)
DEGRES = (4, 5, 7)
W2S = (1.73, 2.27, 2.80)          # gel alpha 4.2, colonnes derivees
C_PLAN = (1.05, 1.20)             # gel alpha 4.3
C_SEUIL = 0.95                    # gel alpha 8, G-seuil
ITER_MAX_FENETRE = 8              # gel alpha 7.2
ATTENDUS_ALPHA = None             # derive dans compte_attendu_alpha()

# Gel temoin, section 3 -- propres au banc.
Q_ECH = 2
C_T = 2
C_PL = 10                         # LD-16 : lecture SOUS LE DEPOT 9bis
                                  # c4310e33da6b9759 -- la clause d'origine (v7 5.4)
                                  # est ABROGEE par la v11 ; ancre TRANSITOIRE,
                                  # dette D-v5-1, arbitrage operateur (depot
                                  # re-ancre ou LD-16bis). NON EMIS au reglage
                                  # (v6) ; les feuilles /T1 /T3a restent figees
                                  # par le depot : aucune valeur emise ne bouge.
                                  # c_pl ne sert nulle part ailleurs (v11 3).
C_0 = 10
KP_BASC = 2 * K_BASC              # k' = 2k, depart de la phase grossiere
ETA_R = ETA                       # herite
PLAFOND_INT = float(ETA) * 1.0    # temoin v7 : tol_int plafonnee a eta x (ecart entre ordres consecutifs = 1)
T_0 = T_MAX_DEPOSE                # plafond de temps DEPOSE (4.4 (1))
N_PLAFONDS = 5                    # q^4 = 16 >= 10 (4.4)
ORDRE_SCHEMA = 4                  # RK4
# T-1b : base lue a la table gelee de 4.6 (LD-3)
T1B_CAP, T1B_T = 100.0, 200.0
# T-2a, T-3b (LD-8)
T2A_W2, T2A_A, T2A_B = 2.27, 1.0, 1.0
T2B_W2 = 2.27
T3B_JEUX = ((1.0, 1.0, 1.0), (1.0, 1.0, 2.0), (1.0, 1.0, 4.0))
T3B_PERIODES = 10

# Damour-Smilga (2.13), etats de 4.3 (w = lambda = 1)
DS_W, DS_LAM = 1.0, 1.0
ETATS_T1 = (("A", 1.0, 0.0, 1.0, 0.0), ("B", 2.0, 0.0, 1.0, 0.0))   # x, x', D, D'

LN10 = math.log(10.0)


def alpha_de(p):
    return Fraction(4, p - 2)


def K_de(p):
    a = alpha_de(p)
    return a * (a + 1) * (a + 2) * (a + 3)


def A_de(p, g=G_REF):
    return float(K_de(p) / Fraction(repr(g))) ** (1.0 / (p - 2))


def tau_dom(w2):
    return math.sqrt(float(DELTA) / (1.0 + w2 * w2))


def tau_cap(w2):
    return float(R_CAP) * tau_dom(w2)


def dt2_de(w2):
    return tau_cap(w2) / M_PAS


def cap_p(p, w2):
    return A_de(p) * tau_cap(w2) ** (-float(alpha_de(p)))


def x_bascule(p, w2, k=K_BASC):
    return A_de(p) * (k * tau_dom(w2)) ** (-float(alpha_de(p)))


# -- Reglage prime (gel constante A v4, 4) : tau_dom() ci-dessus est DEJA
#    prime (DELTA = delta') ; les grandeurs du REPERE delta_0 s'ecrivent _0.
def tau_dom_0(w2):
    return math.sqrt(float(DELTA_0) / (1.0 + w2 * w2))


def x_bascule_0(p, w2, k=K_BASC):
    """Bascule 5.3 du v5, INCHANGEE (v4 4.2) : le depart de l'etage 2a."""
    return A_de(p) * (k * tau_dom_0(w2)) ** (-float(alpha_de(p)))


def dt2a_de(w2):
    """Etage 2a : dt <= terminal / M, terminal = k tau_dom' (v4 4.2)."""
    return K_BASC * tau_dom(w2) / M_PAS


def depart_2s(w2):
    return T_MAX_DEPOSE - K_BASC * tau_dom_0(w2)


def depart_2bp(w2):
    return T_MAX_DEPOSE - K_BASC * tau_dom(w2)


N_2BP = int(Fraction(M_PAS * K_BASC) / R_CAP)      # = 400 EXACT (v4 4.7)
N_FENETRE = int(Fraction(M_PAS) * (1 - R_CAP) / R_CAP)   # = 180 (v4 4.2)


def n_2a_nominal():
    r = Fraction(int(round(math.sqrt(float(DELTA_0 / DELTA)))))
    assert r * r == DELTA_0 / DELTA, "sqrt(delta_0/delta') non entiere"
    return int(M_PAS * (r - 1))                    # = M (racine - 1) : 380 au v6 (4.6)


def n_2b_nominal():
    return int(M_PAS * (K_BASC - R_CAP) / R_CAP)   # = 380 (v4 4.6)


RACINE_DESC = int(round(math.sqrt(float(B_DESC ** J_DESC))))   # = 32, PUR
assert Fraction(RACINE_DESC) ** 2 == Fraction(B_DESC) ** J_DESC


def n_2a_nominal_k(k_start):
    """Nominal de l'etage 2a quand la bascule 5.3 se joue a k_start
    (G-k : k_start = 4) : M (k_start tau_dom_0 / (k tau_dom') - 1),
    EXACT en Fraction (regle 15 -- jamais ceil d'un pur flottant)."""
    n = M_PAS * (Fraction(k_start) * RACINE_DESC / K_BASC - 1)
    assert n.denominator == 1
    return int(n)


def retard_2a(w2):
    """ceil(dt_1 / dt_2a) : ratio irrationnel, loin de tout bord."""
    return int(math.ceil(DT1 / dt2a_de(w2)))


RETARD_2B = int(Fraction(K_BASC) / R_CAP)          # = k/r = 20, PUR (v4 4.6)


def intervalle_evenement(n_nominal, retard, facteur=1):
    """v4 4.6 / 4.8 : depart en retard d'au plus UN pas de la grille
    AMONT (retard, en pas de la grille propre), arrivee d'au plus UN pas ;
    n_nominal et retard sont des ENTIERS DERIVES (regle 15) ; jumelle :
    les DEUX bornes x facteur (v4 4.8, jamais recopiees)."""
    return facteur * (int(n_nominal) - int(retard)), facteur * (int(n_nominal) + 1)


def intervalle_2s(w2, facteur=1):
    """v6 4.7 : n_nominal <= n_2s <= n_nominal + ceil(dt_1/dt_2a), n_nominal = M (racine - 1) ; jumelle x2."""
    return (facteur * n_2a_nominal(),
            facteur * (n_2a_nominal() + retard_2a(w2)))


def garde_compte(nom, n, lo, hi, rec, etiquette):
    """Toute garde de compte se compare a l'intervalle DERIVE (v4 4.6) ;
    hors intervalle -> G-fen, motif : compte d'etage."""
    ok = lo <= n <= hi
    rec.setdefault("comptes_etages", {})[nom] = {"n": int(n), "intervalle": [int(lo), int(hi)], "ok": bool(ok)}
    if not ok:
        rec["statut"] = "G-fen (compte %s = %d hors [%d, %d])" % (nom, n, lo, hi)
        rec["ajustement"] = {"statut": "G-fen"}
        JRN("A-%s" % etiquette, "compte d'etage %s = %d HORS intervalle derive [%d, %d] -> G-fen, COMPTE" % (nom, n, lo, hi))
    return ok


def etat_depart_consigne(rec, nom, etat, t):
    """v4 4.9 (exigence NEUVE) : l'etat complet a chaque depart d'etage,
    meme forme (t, x1, x2, x1', x2'), empreinte convention B."""
    ligne = "%.17g %.17g %.17g %.17g %.17g" % ((t,) + tuple(etat))
    rec.setdefault("departs_etages", {})[nom] = {"t": t, "etat": list(etat), "empreinte": empreinte_B_texte(ligne)}


PERIM_9BIS = ("T1", "T1b", "T3a", "T3b")           # temoin v9, 9bis : ENUMERE ET CLOS


# =====================================================================
# 1. OUTILS : empreintes, journal etiquete, fichiers ASCII/LF
# =====================================================================

def sha_brut(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


def empreinte_B(chemin):
    brut = open(chemin, "rb").read()
    canon = unicodedata.normalize(
        "NFC", brut.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()[:16]


def empreinte_B_texte(texte):
    canon = unicodedata.normalize("NFC", texte.replace("\r\n", "\n").replace("\r", "\n"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()[:16]


class Journal(object):
    """Chaque ligne porte un numero et une etiquette (N-61)."""

    def __init__(self):
        self.n = 0
        self.lignes = []
        self.silence = False

    def __call__(self, etiquette, texte=""):
        if self.silence:
            return None
        self.n += 1
        ligne = "[%04d] %-14s %s" % (self.n, etiquette, texte)
        self.lignes.append(ligne)
        print(ligne)
        sys.stdout.flush()
        return self.n


JRN = Journal()


def ecrire_ascii(chemin, texte):
    """Ecrit ASCII pur, LF, saut de ligne final ; refuse tout octet >= 128."""
    if not texte.endswith("\n"):
        texte += "\n"
    octets = texte.encode("ascii")           # leve UnicodeEncodeError sinon
    assert b"\r" not in octets, "CR dans %s" % chemin
    assert all(x < 128 for x in octets), "octet non ASCII dans %s" % chemin
    d = os.path.dirname(chemin)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    with open(chemin, "wb") as f:
        f.write(octets)
    return chemin


def json_ascii(objet):
    return json.dumps(objet, indent=1, sort_keys=True, ensure_ascii=True)


def date_utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def n59_copie_executee():
    ch = os.path.abspath(__file__)
    brut = open(ch, "rb").read()
    ok_ascii = all(x < 128 for x in brut) and brut.count(b"\r") == 0
    JRN("N-59", "%s  %d o  sha256 brut %s  convention B %s  ASCII/LF %s"
        % (os.path.basename(ch), len(brut), sha_brut(ch)[:16], empreinte_B(ch), ok_ascii))
    if not ok_ascii:
        sys.exit("ARRET : la copie executee n'est pas ASCII/LF.")
    return brut


def verifier_ancres(registre, exiger_gels=True):
    """E19 / PB-1 / custody : chaque piece citee est re-derivee, jamais crue."""
    for (chemin, emp, taille) in (GEL_TEMOIN, GEL_ALPHA, GEL_TEMOIN_BASE, GEL_ALPHA_BASE):
        p = os.path.join(registre, chemin)
        if not os.path.isfile(p):
            if exiger_gels:
                sys.exit("ARRET E19 : gel absent %s" % p)
            JRN("E19", "gel ABSENT (mode d'instrument) : %s attendu %s" % (chemin, emp))
            continue
        e, n = empreinte_B(p), os.path.getsize(p)
        JRN("E19", "%s  %s  %d o  attendu %s %d  -> %s"
            % (chemin, e, n, emp, taille, "CONCORDANT" if (e == emp and n == taille) else "DISCORDANT"))
        if e != emp or n != taille:
            sys.exit("ARRET E19 : le gel %s n'est pas celui que l'instrument cite." % chemin)
    for (chemin, emp) in (CERT_TEMOIN, CERT_ALPHA, CERT_TEMOIN_BASE, CERT_ALPHA_BASE):
        p = os.path.join(registre, chemin)
        if os.path.isfile(p):
            e = empreinte_B(p)
            JRN("E19", "%s  %s  attendu %s  -> %s"
                % (chemin, e, emp, "CONCORDANT" if e == emp else "DISCORDANT"))
            if e != emp:
                sys.exit("ARRET E19 : certification %s discordante." % chemin)
        else:
            JRN("E19", "certification absente du dossier (citee, non exigee) : %s %s" % (chemin, emp))
    for (chemin, sha, taille) in (MOTEUR, CARTE):
        p = os.path.join(registre, chemin)
        if not os.path.isfile(p):
            sys.exit("ARRET custody : piece absente %s" % p)
        s, n = sha_brut(p), os.path.getsize(p)
        JRN("CUSTODY", "%s  sha256 brut %s...  %d o  -> %s"
            % (chemin, s[:16], n, "CONCORDANT" if (s == sha and n == taille) else "DISCORDANT"))
        if s != sha or n != taille:
            sys.exit("ARRET custody : %s n'est pas la piece citee." % chemin)

# =====================================================================
# 2. LA PHYSIQUE DU MOTEUR, TRANSCRITE AUX LIGNES CITEES (PB-1)
# =====================================================================
# 2.1 Le pas RK4 (l.351-361) et le test d'explosion (l.362-363), AU MOT.
#     Les quatre lignes de mise a jour gardent l'association exacte des
#     operations du moteur ("dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)").

def pas_rk4(acc, x1, x2, v1, v2, dt):
    k1v1, k1v2 = acc(x1, x2); k1x1, k1x2 = v1, v2
    k2v1, k2v2 = acc(x1 + .5 * dt * k1x1, x2 + .5 * dt * k1x2)
    k2x1, k2x2 = v1 + .5 * dt * k1v1, v2 + .5 * dt * k1v2
    k3v1, k3v2 = acc(x1 + .5 * dt * k2x1, x2 + .5 * dt * k2x2)
    k3x1, k3x2 = v1 + .5 * dt * k2v1, v2 + .5 * dt * k2v2
    k4v1, k4v2 = acc(x1 + dt * k3x1, x2 + dt * k3x2)
    k4x1, k4x2 = v1 + dt * k3v1, v2 + dt * k3v2
    x1 = x1 + dt / 6 * (k1x1 + 2 * k2x1 + 2 * k3x1 + k4x1)
    x2 = x2 + dt / 6 * (k1x2 + 2 * k2x2 + 2 * k3x2 + k4x2)
    v1 = v1 + dt / 6 * (k1v1 + 2 * k2v1 + 2 * k3v1 + k4v1)
    v2 = v2 + dt / 6 * (k1v2 + 2 * k2v2 + 2 * k3v2 + k4v2)
    return x1, x2, v1, v2


def pas_rk4_force(acc_t, x1, x2, v1, v2, dt, t):
    """Meme pas, acceleration dependant du temps (solution manufacturee,
    temoin 5.1) : les etages sont evalues a t, t + dt/2, t + dt/2, t + dt."""
    k1v1, k1v2 = acc_t(x1, x2, t); k1x1, k1x2 = v1, v2
    k2v1, k2v2 = acc_t(x1 + .5 * dt * k1x1, x2 + .5 * dt * k1x2, t + .5 * dt)
    k2x1, k2x2 = v1 + .5 * dt * k1v1, v2 + .5 * dt * k1v2
    k3v1, k3v2 = acc_t(x1 + .5 * dt * k2x1, x2 + .5 * dt * k2x2, t + .5 * dt)
    k3x1, k3x2 = v1 + .5 * dt * k2v1, v2 + .5 * dt * k2v2
    k4v1, k4v2 = acc_t(x1 + dt * k3x1, x2 + dt * k3x2, t + dt)
    k4x1, k4x2 = v1 + dt * k3v1, v2 + dt * k3v2
    x1 = x1 + dt / 6 * (k1x1 + 2 * k2x1 + 2 * k3x1 + k4x1)
    x2 = x2 + dt / 6 * (k1x2 + 2 * k2x2 + 2 * k3x2 + k4x2)
    v1 = v1 + dt / 6 * (k1v1 + 2 * k2v1 + 2 * k3v1 + k4v1)
    v2 = v2 + dt / 6 * (k1v2 + 2 * k2v2 + 2 * k3v2 + k4v2)
    return x1, x2, v1, v2


def test_explosion_depose(x1, x2, cap):
    """l.362-363 : ~isfinite OU max(|x1|, |x2|) > CAP, variable par variable."""
    return (~np.isfinite(x1)) | (~np.isfinite(x2)) | \
           (np.maximum(np.abs(x1), np.abs(x2)) > cap)


# 2.2 Le systeme PU du moteur : grad_rapide (l.323-325), etat initial et
#     acc (l.340-348). `p` remplace la globale P (re-liee par degre au
#     moteur, patron m12_pilote_v3.py l.576-582).

def acc_pu(w2, g, p):
    delta = w2 * w2 - W1 * W1

    def acc(a1, a2):
        base = g * (a1 + a2) ** (p - 1)
        d1, d2 = base, base
        return -W1 * W1 * a1 + d1 / delta, -w2 * w2 * a2 - d2 / delta
    return acc


def etat_initial_pu(w2, s_arr, sgn=1):
    """l.340-344, AU MOT."""
    delta = w2 * w2 - W1 * W1
    s_arr = np.asarray(s_arr, float)
    x1 = sgn * s_arr * (1 + w2 * w2) / delta
    x2 = -sgn * s_arr * (1 + W1 * W1) / delta
    v1 = np.zeros_like(x1); v2 = np.zeros_like(x2)
    return x1, x2, v1, v2


def phase1_pu(w2, s, p, mode, g=G_REF, sgn=1, dt=DT1, t_max=T_MAX_DEPOSE,
              x_b=None, t_fin=None, cap=CAP_DEPOSE, acc_fn=None):
    """Phase 1, SCHEMA DEPOSE, sur tableau (1,) comme le moteur.
    mode 'lignee'  : test depose (l.362-363) -> (explose, indice, etat)
    mode 'bascule' : arret a |x1 + x2| >= x_b (gel alpha 5.3) ou non fini
    mode 'seuil'   : arret a t >= t_fin (LD-10), bascule consignee si elle mord
    Indice = nombre de pas joues quand l'evenement est lu (t = indice x dt)."""
    acc = (acc_fn or acc_pu)(w2, g, p)
    x1, x2, v1, v2 = etat_initial_pu(w2, [s], sgn)
    n_max = int(round(t_max / dt))
    n = 0
    evenement = None
    bascule_vue = None
    with np.errstate(over="ignore", invalid="ignore"):
        for n in range(1, n_max + 1):
            x1, x2, v1, v2 = pas_rk4(acc, x1, x2, v1, v2, dt)
            if mode == "lignee":
                bad = test_explosion_depose(x1, x2, cap)
                if bad.any():
                    evenement = "EXPLOSION"
                    break
            else:
                x = x1 + x2
                fini = bool(np.isfinite(x1).all() and np.isfinite(x2).all())
                if not fini:
                    evenement = "NON_FINI"
                    break
                if mode == "bascule":
                    if abs(float(x[0])) >= x_b:
                        evenement = "BASCULE"
                        break
                elif mode == "seuil":
                    if bascule_vue is None and x_b is not None and abs(float(x[0])) >= x_b:
                        bascule_vue = n
                    if (n + 1) * dt > t_fin * (1 + 1e-12):     # dernier pas AVANT t_fin
                        evenement = "T_FIN"
                        break
    if evenement is None:
        evenement = "T_MAX"
    etat = (float(x1[0]), float(x2[0]), float(v1[0]), float(v2[0]))
    return {"evenement": evenement, "indice": n, "t": n * dt, "etat": etat,
            "bascule_sous_seuil_indice": bascule_vue, "n_max": n_max}


def phase2_pu(w2, p, etat, t0, dt, arret_cap=None, t_max=T_MAX_DEPOSE, g=G_REF,
              forcage=None, tau_star=None, tau_fin=None, sgn=1):
    # sgn est porte par l'etat de depart (phase 1 au signe du point) ; il est
    # accepte ici pour que l'appel soit uniforme et consigne, sans effet.
    """Phase 2 au pas raffine, meme schema. Deux arrets :
    - arret_cap : |x1 + x2| >= CAP_p (gel alpha 5.4) ou t >= t_max (G-fen)
    - tau_fin   : (solution manufacturee) t* - t <= tau_fin, avec forcage(tau)
    Rend la serie (t, x1, x2) de la phase (point de depart inclus)."""
    x1, x2, v1, v2 = (np.array([etat[0]]), np.array([etat[1]]),
                      np.array([etat[2]]), np.array([etat[3]]))
    serie_t, serie_x1, serie_x2 = [t0], [float(x1[0])], [float(x2[0])]
    if forcage is None:
        acc = acc_pu(w2, g, p)
    else:
        delta = w2 * w2 - W1 * W1

        def acc_t(a1, a2, t):
            base = g * (a1 + a2) ** (p - 1)
            Fz = forcage(tau_star - t)
            return -W1 * W1 * a1 + (base + Fz) / delta, -w2 * w2 * a2 - (base + Fz) / delta
    evenement = None
    n = 0
    with np.errstate(over="ignore", invalid="ignore"):
        while True:
            n += 1
            t = t0 + n * dt
            if forcage is None:
                x1, x2, v1, v2 = pas_rk4(acc, x1, x2, v1, v2, dt)
            else:
                x1, x2, v1, v2 = pas_rk4_force(acc_t, x1, x2, v1, v2, dt, t0 + (n - 1) * dt)
            serie_t.append(t); serie_x1.append(float(x1[0])); serie_x2.append(float(x2[0]))
            if not (np.isfinite(x1).all() and np.isfinite(x2).all()):
                evenement = "NON_FINI"; break
            if arret_cap is not None and abs(float(x1[0] + x2[0])) >= arret_cap:
                evenement = "CAP"; break
            if tau_fin is not None and tau_star - t <= tau_fin * (1.0 + 1e-12):
                evenement = "TAU_FIN"; break
            if t >= t_max - 0.5 * dt:
                evenement = "T_MAX"; break
    return {"evenement": evenement, "n": n, "t": np.array(serie_t),
            "x1": np.array(serie_x1), "x2": np.array(serie_x2),
            "etat_fin": (float(x1[0]), float(x2[0]), float(v1[0]), float(v2[0]))}


# 2.3 L'application d'etat (x, x', x'', x''') <-> (x1, x2, x1', x2'), derivee
#     de x = x1 + x2 et x'' = -x1 - w2^2 x2 (les termes en d s'annulent).

def vers_composantes(x, xp, xpp, xppp, w2):
    delta = w2 * w2 - W1 * W1
    return ((w2 * w2 * x + xpp) / delta, -(x + xpp) / delta,
            (w2 * w2 * xp + xppp) / delta, -(xp + xppp) / delta)


def depuis_composantes(x1, x2, v1, v2, w2):
    return (x1 + x2, v1 + v2, -W1 * W1 * x1 - w2 * w2 * x2, -W1 * W1 * v1 - w2 * w2 * v2)


# 2.4 La recherche de seuil (l.372-401), transcrite avec son integrateur en
#     parametre et la comptabilite des elargissements (4.6bis (iii)).

def chercher_seuil_transcrit(integrer, w2, sgn=1, dt=DT1, g=G_REF, cst=None):
    C = cst or {"LO0": LO0, "HI0": HI0, "MAX_ELARG": MAX_ELARG, "NGRID": NGRID,
                "NPASSES": NPASSES, "NDENSE": NDENSE}
    lo, hi = C["LO0"], C["HI0"]
    k_elarg = 0
    for _ in range(C["MAX_ELARG"]):
        s = np.linspace(lo, hi, C["NGRID"])
        ex = integrer(w2, s, sgn, dt, g)
        if ex.any():
            break
        lo, hi = hi, hi * 4
        k_elarg += 1
    else:
        return None, "ECHEC_HAUT", {"k": k_elarg, "encadrement": (lo, hi)}
    nb = 0
    while ex[0] and nb < C["MAX_ELARG"]:
        hi, lo = lo, lo / 4
        s = np.linspace(lo, hi, C["NGRID"]); ex = integrer(w2, s, sgn, dt, g); nb += 1
        k_elarg -= 1
        if not ex.any():
            return None, "ECHEC_BAS", {"k": k_elarg, "encadrement": (lo, hi)}
    encadrement = (lo, hi)
    for _ in range(C["NPASSES"] - 1):
        i = int(np.argmax(ex))
        if i == 0:
            break
        lo, hi = s[i - 1], s[i]
        s = np.linspace(lo, hi, C["NGRID"]); ex = integrer(w2, s, sgn, dt, g)
        if not ex.any():
            s = np.array([hi]); ex = np.array([True]); break
    i = int(np.argmax(ex))
    lo_d, hi_d = (s[i - 1] if i > 0 else lo), s[i]
    s = np.linspace(lo_d, hi_d, C["NDENSE"]); ex = integrer(w2, s, sgn, dt, g)
    info = {"k": k_elarg, "encadrement": encadrement, "cellule_dense": (float(lo_d), float(hi_d))}
    if not ex.any():
        return float(hi_d), "DENSE_SANS_EXPLOSION", info
    return float(s[int(np.argmax(ex))]), "OK|pas=%.2e" % (s[1] - s[0]), info


def pas_signature(k, cst=None):
    """4.6bis (iii) : pas_k = W_k / ((NGRID-1)^NPASSES x (NDENSE-1)), W_k la
    largeur de l'encadrement apres k elargissements (k < 0 : vers le bas)."""
    C = cst or {"LO0": LO0, "HI0": HI0, "NGRID": NGRID, "NPASSES": NPASSES, "NDENSE": NDENSE}
    den = (C["NGRID"] - 1) ** C["NPASSES"] * (C["NDENSE"] - 1)
    if k == 0:
        W = C["HI0"] - C["LO0"]; enc = (C["LO0"], C["HI0"])
    elif k > 0:
        lo, hi = C["HI0"] * 4 ** (k - 1), C["HI0"] * 4 ** k
        W = hi - lo; enc = (lo, hi)
    else:
        m = -k
        lo, hi = C["LO0"] / 4 ** m, C["LO0"] / 4 ** (m - 1)
        W = hi - lo; enc = (lo, hi)
    return W / den, den, enc


def pas_du_motif(motif):
    if not (isinstance(motif, str) and motif.startswith("OK|pas=")):
        return None
    try:
        return motif.split("pas=")[1]
    except IndexError:
        return None


def controle_transcription_positif(seuil, motif, info, cst=None):
    """W-transcription, controle positif : le motif porte pas = W_k/den
    avec k COHERENT avec l'encadrement ou le seuil est tombe."""
    txt = pas_du_motif(motif)
    if txt is None:
        return False, "motif sans pas : %r" % (motif,)
    k = info["k"]
    pas_k, den, enc = pas_signature(k, cst)
    attendu = "%.2e" % pas_k
    coherent = (seuil is not None) and (enc[0] <= seuil <= enc[1])
    ok = (txt == attendu) and coherent
    return ok, ("pas=%s attendu(k=%d)=%s den=%d encadrement=[%.6g, %.6g] seuil=%r coherent=%s"
                % (txt, k, attendu, den, enc[0], enc[1], seuil, coherent))

# =====================================================================
# 3. DAMOUR-SMILGA (arXiv:2110.11175, classe (i)), TRANSCRIT (temoin 4.1)
#    H1(x, D; p, P) = p P + D V'(x)                          (2.10)
#    x'' + V'(x) = 0 ,  D'' + V''(x) D = 0                   (2.11)
#    N(x, P) = P^2/2 + V(x)                                  (2.12)
#    V(x) = w^2 x^2/2 + lambda x^4/4                         (2.13)
#    Hamilton : x' = dH1/dp = P, D' = dH1/dP = p, p' = -D V''(x),
#    P' = -V'(x) ; donc P = x', p = D' (controle symbolique en 6).
#    Le controle de fidelite a l'article repose sur machine 2 (gel, 7).
# =====================================================================

def V_ds(x, w=DS_W, lam=DS_LAM):
    return w * w * x * x / 2 + lam * x ** 4 / 4


def Vp_ds(x, w=DS_W, lam=DS_LAM):
    return w * w * x + lam * x ** 3


def Vpp_ds(x, w=DS_W, lam=DS_LAM):
    return w * w + 3 * lam * x * x


def acc_ds(w=DS_W, lam=DS_LAM):
    def acc(a, b):                    # positions (x, D) -> (x'', D'')
        return -Vp_ds(a, w, lam), -Vpp_ds(a, w, lam) * b
    return acc


def H1_ds(x, xp, D, Dp, w=DS_W, lam=DS_LAM):
    return Dp * xp + D * Vp_ds(x, w, lam)


def N_ds(x, xp, w=DS_W, lam=DS_LAM):
    return xp * xp / 2 + V_ds(x, w, lam)


def integrer_ds(s_arr, etat, cap, t_max, dt=DT1, w=DS_W, lam=DS_LAM):
    """L'analogue de integrer() (l.339-370) sur (2.11) : `s` multiplie D(0)
    et D'(0) SEULEMENT (4.6bis (ii)) ; test transcrit variable par variable
    (4.4, D-t-14) : non fini OU max(|x|, |D|) > CAP ; membres exploses mis
    a zero et poursuite des autres (l.364-369)."""
    x0, xp0, D0, Dp0 = etat
    s = np.asarray(s_arr, float)
    x = np.full_like(s, x0); xp = np.full_like(s, xp0)
    D = s * D0; Dp = s * Dp0
    expl = np.zeros(s.shape, bool)
    acc = acc_ds(w, lam)
    with np.errstate(over="ignore", invalid="ignore"):
        for _ in range(int(round(t_max / dt))):
            x, D, xp, Dp = pas_rk4(acc, x, D, xp, Dp, dt)
            bad = (~np.isfinite(x)) | (~np.isfinite(D)) | (np.maximum(np.abs(x), np.abs(D)) > cap)
            if bad.any():
                expl |= bad
                if expl.all():
                    break
                x = np.where(expl, 0., x); D = np.where(expl, 0., D)
                xp = np.where(expl, 0., xp); Dp = np.where(expl, 0., Dp)
    return expl


def integrer_ds_pour_recherche(etat, cap, t_max):
    """Signature du moteur (w2, s_arr, sgn, dt, g) pour la recherche
    transcrite ; w2, sgn, g n'ont pas d'objet sur (2.11)."""
    def integrer(w2, s_arr, sgn=1, dt=DT1, g=G_REF):
        return integrer_ds(s_arr, etat, cap, t_max, dt)
    return integrer


class FlotDS(object):
    """Un flot de (2.11) a s = 1 (T-1), en flottants, meme pas_rk4, avec
    ses lectures : t_c aux plafonds (test depose transcrit), derives
    relatives de H1 et N (clause de reference), pics de |D|, max |x|,
    serie sous-echantillonnee. Le flot se PROLONGE (4.4 : T_0 puis T_MAX)."""

    def __init__(self, etat, caps, dt=DT1, w=DS_W, lam=DS_LAM, pas_serie=100):
        self.x, self.xp, self.D, self.Dp = etat
        self.dt, self.w, self.lam = dt, w, lam
        self.acc = acc_ds(w, lam)
        self.caps = list(caps)
        self.t_c = {}
        self.n = 0
        self.H1_0 = H1_ds(self.x, self.xp, self.D, self.Dp, w, lam)
        self.N_0 = N_ds(self.x, self.xp, w, lam)
        if self.H1_0 == 0.0 or self.N_0 == 0.0:
            raise SystemExit("ETAT INTERDIT (gel temoin 4.3) : H1_0 = %r, N_0 = %r -- sur l'etat tangent "
                             "(D proportionnel a x') toute derive relative est absurde et le temoin passerait "
                             "par construction" % (self.H1_0, self.N_0))
        self.derive_H1 = 0.0
        self.derive_N = 0.0
        self.D_max, self.t_pic = abs(self.D), 0.0
        self.x_max = abs(self.x)
        self.pics = []                     # (T, t_pic(T)) sur demande
        self.non_fini = None
        self.pas_serie = pas_serie
        self.serie = [(0.0, self.x, self.D, self.H1_0, self.N_0)]

    def prolonger(self, horizon, T_lectures_pic=()):
        n_fin = int(round(horizon / self.dt))
        deja = set(p[0] for p in self.pics)
        T_lect = [T for T in sorted(T_lectures_pic) if T not in deja]
        while self.n < n_fin and self.non_fini is None:
            self.x, self.D, self.xp, self.Dp = pas_rk4(self.acc, self.x, self.D, self.xp, self.Dp, self.dt)
            self.n += 1
            t = self.n * self.dt
            fini = math.isfinite(self.x) and math.isfinite(self.D)
            m = max(abs(self.x), abs(self.D)) if fini else float("inf")
            for c in self.caps:
                if c not in self.t_c and ((not fini) or m > c):
                    self.t_c[c] = t
            if not fini:
                self.non_fini = t
                break
            if abs(self.D) > self.D_max:
                self.D_max, self.t_pic = abs(self.D), t
            if abs(self.x) > self.x_max:
                self.x_max = abs(self.x)
            while T_lect and t >= T_lect[0] - 0.5 * self.dt:
                self.pics.append((T_lect[0], self.t_pic, self.D_max))
                T_lect.pop(0)
            H1 = H1_ds(self.x, self.xp, self.D, self.Dp, self.w, self.lam)
            N = N_ds(self.x, self.xp, self.w, self.lam)
            self.derive_H1 = max(self.derive_H1, abs(H1 - self.H1_0) / abs(self.H1_0))
            self.derive_N = max(self.derive_N, abs(N - self.N_0) / abs(self.N_0))
            if self.n % self.pas_serie == 0:
                self.serie.append((t, self.x, self.D, H1, N))
        return self


def flot_x_duffing(x0, w, lam, dt, horizon):
    """T-3b : le secteur x seul (D = D' = 0 reste nul), meme pas_rk4."""
    x, xp, D, Dp = x0, 0.0, 0.0, 0.0
    acc = acc_ds(w, lam)
    ts, xs = [0.0], [x0]
    n_fin = int(round(horizon / dt))
    for n in range(1, n_fin + 1):
        x, D, xp, Dp = pas_rk4(acc, x, D, xp, Dp, dt)
        ts.append(n * dt); xs.append(x)
    return np.array(ts), np.array(xs)


def champ_de_forces_tirage(graine=20260826, n=4096):
    """Temoin 7 (i) : le champ de forces de (2.11) sur un tirage DECLARE,
    pour la double transcription (machine 2 compare la sienne)."""
    rng = np.random.default_rng(graine)
    x = rng.uniform(-2, 2, n); D = rng.uniform(-2, 2, n)
    acc = acc_ds()
    ax, aD = acc(x, D)
    lignes = ["# tirage default_rng(%d), uniform(-2,2) x %d pour x et D ; colonnes x D x'' D''"
              % (graine, n)]
    for i in range(n):
        lignes.append("%.17g %.17g %.17g %.17g" % (x[i], D[i], ax[i], aD[i]))
    texte = "\n".join(lignes) + "\n"
    return texte, empreinte_B_texte(texte)

# =====================================================================
# 4. LA SOLUTION MANUFACTUREE (temoin 5.1 ; gel alpha 2.1-2.3)
#    x_m(tau) = A tau^(-alpha), tau = t* - t ;  x_m'''' = g x_m^(p-1) EXACT
#    forcage f = A [ (1 + w2^2) alpha (alpha+1) tau^(-alpha-2) + w2^2 tau^(-alpha) ]
# =====================================================================

def xm_et_derivees(p, tau):
    a = float(alpha_de(p)); A = A_de(p)
    return (A * tau ** (-a), A * a * tau ** (-a - 1),
            A * a * (a + 1) * tau ** (-a - 2), A * a * (a + 1) * (a + 2) * tau ** (-a - 3))


def forcage_de(p, w2):
    a = float(alpha_de(p)); A = A_de(p)

    def f(tau):
        return A * ((1 + w2 * w2) * a * (a + 1) * tau ** (-a - 2) + w2 * w2 * tau ** (-a))
    return f


# =====================================================================
# 5. POLYNOMES EXACTS (Fraction) POUR LES CONTROLES SYMBOLIQUES
# =====================================================================

class Poly(object):
    """Polynome a coefficients Fraction ; monomes = tuples d'exposants."""

    def __init__(self, nvar, termes=None):
        self.nvar = nvar
        self.t = {}
        for k, v in (termes or {}).items():
            if v != 0:
                self.t[tuple(k)] = Fraction(v)

    @classmethod
    def var(cls, nvar, i, c=1):
        e = [0] * nvar; e[i] = 1
        return cls(nvar, {tuple(e): c})

    @classmethod
    def cst(cls, nvar, c):
        return cls(nvar, {tuple([0] * nvar): c})

    def __add__(self, o):
        o = o if isinstance(o, Poly) else Poly.cst(self.nvar, o)
        r = dict(self.t)
        for k, v in o.t.items():
            r[k] = r.get(k, 0) + v
        return Poly(self.nvar, r)

    __radd__ = __add__

    def __neg__(self):
        return Poly(self.nvar, {k: -v for k, v in self.t.items()})

    def __sub__(self, o):
        return self + (-(o if isinstance(o, Poly) else Poly.cst(self.nvar, o)))

    def __mul__(self, o):
        o = o if isinstance(o, Poly) else Poly.cst(self.nvar, o)
        r = {}
        for k1, v1 in self.t.items():
            for k2, v2 in o.t.items():
                k = tuple(a + b for a, b in zip(k1, k2))
                r[k] = r.get(k, 0) + v1 * v2
        return Poly(self.nvar, r)

    __rmul__ = __mul__

    def __pow__(self, n):
        r = Poly.cst(self.nvar, 1)
        for _ in range(n):
            r = r * self
        return r

    def d(self, i):
        r = {}
        for k, v in self.t.items():
            if k[i] > 0:
                kk = list(k); kk[i] -= 1
                r[tuple(kk)] = r.get(tuple(kk), 0) + v * k[i]
        return Poly(self.nvar, r)

    def __eq__(self, o):
        o = o if isinstance(o, Poly) else Poly.cst(self.nvar, o)
        return self.t == o.t

    def est_nul(self):
        return not self.t

    def evaluer(self, vals):
        s = Fraction(0)
        for k, v in self.t.items():
            m = v
            for e, x in zip(k, vals):
                m *= Fraction(x) ** e
            s += m
        return s


def controles_symboliques():
    """Rejoue en exact : (a) Hamilton de (2.10) rend (2.11) et l'acc
    transcrite ; (b) {N, H1} = 0 ; (c) x_m'''' = g x_m^(p-1) et la forme de
    f, aux trois degres, W = w2^2 symbolique ; (d) l'operateur lineaire
    annule cos(t) et cos(w2 t) ; (e) forme fermee de Duffing au point
    standard ; (f) K_p et les plafonds en Fraction."""
    R = {}
    # (a)(b) variables : x, D, p, P, W (= w^2), L (= lambda)
    x, D, p, P, W, L = [Poly.var(6, i) for i in range(6)]
    Vp = W * x + L * (x ** 3)
    Vpp = W + 3 * L * (x ** 2)
    V = W * (x ** 2) * Fraction(1, 2) + L * (x ** 4) * Fraction(1, 4)
    H1 = p * P + D * Vp
    N = P * P * Fraction(1, 2) + V
    hamilton = (H1.d(2) == P) and (H1.d(3) == p) and ((-H1.d(0)) == (-(D * Vpp))) and ((-H1.d(1)) == (-Vp))
    R["a_hamilton_2.10_vers_2.11"] = hamilton
    crochet = N.d(0) * H1.d(2) - N.d(2) * H1.d(0) + N.d(1) * H1.d(3) - N.d(3) * H1.d(1)
    R["b_crochet_N_H1_nul"] = crochet.est_nul()
    # lien au code : l'acc transcrite = les polynomes, sur un point rationnel
    vals = (Fraction(3, 7), Fraction(-5, 11), 0, 0, 1, 1)
    ax_sym, aD_sym = -Vp.evaluer(vals), -(D * Vpp).evaluer(vals)
    ax_code, aD_code = acc_ds()(3.0 / 7.0, -5.0 / 11.0)
    R["a_bis_acc_code_egale_polynome"] = (abs(ax_code - float(ax_sym)) < 1e-15 and
                                         abs(aD_code - float(aD_sym)) < 1e-15)
    # (c) monomes A tau^e, e Fraction, coefficient polynome en (W, gA) :
    #     on represente L[x_m] - g x_m^(p-1) comme dict {e: Poly(W)}
    for pd in DEGRES:
        a = alpha_de(pd); K = K_de(pd)
        e0 = -a
        # derivees : coefficient c_n = prod_{j<n} (e0 - j), exposant e0 - n

        def coef(n):
            c = Fraction(1)
            for j in range(n):
                c *= (e0 - j)
            return c
        Wv = Poly.var(1, 0)
        un = Poly.cst(1, 1)
        termes = {}

        def ajouter(e, poly):
            termes[e] = termes.get(e, Poly.cst(1, 0)) + poly
        ajouter(e0 - 4, un * coef(4))
        ajouter(e0 - 2, (un + Wv) * coef(2))
        ajouter(e0, Wv)
        # g x_m^(p-1) = g A^(p-1) tau^(e0 (p-1)) = A K tau^(e0 (p-1)) car g A^(p-2) = K
        ajouter(e0 * (pd - 1), -(un * K))
        exposant_ok = (e0 * (pd - 1) == e0 - 4)
        f_attendu = {e0 - 2: (un + Wv) * (a * (a + 1)), e0: Wv}
        reste = {e: v for e, v in termes.items() if not v.est_nul()}
        R["c_p%d_exposant_alpha(p-1)=alpha+4" % pd] = exposant_ok
        R["c_p%d_reste_egale_forcage_f" % pd] = (set(reste.keys()) == set(f_attendu.keys()) and
                                                 all(reste[e] == f_attendu[e] for e in f_attendu))
        R["c_p%d_K=%s" % (pd, K)] = (K == {4: Fraction(120), 5: Fraction(3640, 81), 7: Fraction(9576, 625)}[pd])
        A = A_de(pd)
        R["c_p%d_gA^(p-2)=K_num" % pd] = abs(G_REF * A ** (pd - 2) / float(K) - 1) < 1e-13
    # (d) L[cos(omega t)] = (Om^2 - (1+W) Om + W) cos, Om = omega^2 -> (Om-1)(Om-W)
    Om, Wd = Poly.var(2, 0), Poly.var(2, 1)
    R["d_operateur_lineaire_factorise"] = ((Om * Om - (Wd + 1) * Om + Wd) == ((Om - 1) * (Om - Wd)))
    # (e) Duffing standard : Omega^2 = w^2 + lam x0^2 = 2, m = lam x0^2/(2 Omega^2) = 1/4,
    #     x0^2 = 2 m Omega^2 / lam = 1
    Om2 = Fraction(1) + Fraction(1); m = Fraction(1) / (2 * Om2)
    R["e_duffing_Omega2=2_m=1/4_x0=1"] = (Om2 == 2 and m == Fraction(1, 4) and 2 * m * Om2 == 1)
    # (f) plafonds
    R["f_plafond_alpha=2/15"] = (PLAFOND_ALPHA == Fraction(2, 15))
    R["f_plafond_R=eta_R(q-1)=1/4"] = (ETA_R * (Q_ECH - 1) == Fraction(1, 4))
    R["f_plafond_loi2=eta(1-1/c_T)=1/8"] = (ETA * (1 - Fraction(1, C_T)) == Fraction(1, 8))
    # (g) H1_0, N_0 des deux etats (4.3), en exact
    for nom, x0, xp0, D0, Dp0 in ETATS_T1:
        h = Fraction(Dp0) * Fraction(xp0) + Fraction(D0) * (Fraction(x0) + Fraction(x0) ** 3)
        n0 = Fraction(xp0) ** 2 / 2 + Fraction(x0) ** 2 / 2 + Fraction(x0) ** 4 / 4
        att = {"A": (2, Fraction(3, 4)), "B": (10, 6)}[nom]
        R["g_etat_%s_H1_0=%s_N_0=%s" % (nom, h, n0)] = (h == att[0] and n0 == att[1])
    return R


# =====================================================================
# 6. LE MOTEUR DEPOSE : CHARGE, VERIFIE, APPELE TEL QUEL (PB-1)
# =====================================================================

def charger_moteur(registre, factice=None):
    """Patron m12_pilote_v3.py l.483-518 : empreinte exigee AVANT tout,
    globales verifiees, custody transitive (certifier_gel du moteur),
    factice substitue APRES ces verifications (chaine identique)."""
    chemin = os.path.join(registre, MOTEUR[0])
    h = sha_brut(chemin)
    if h != MOTEUR[1]:
        sys.exit("ARRET PB-1 : le moteur n'est pas celui que le gel designe (%s)." % h[:16])
    spec = importlib.util.spec_from_file_location("m9_moteur", chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for nom, att in (("W1", W1), ("G_REF", G_REF), ("DT", DT1), ("T_MAX", T_MAX_DEPOSE),
                     ("CAP", CAP_DEPOSE), ("NDENSE", NDENSE), ("LO0", LO0), ("HI0", HI0),
                     ("MAX_ELARG", MAX_ELARG), ("NGRID", NGRID), ("NPASSES", NPASSES)):
        if float(getattr(mod, nom)) != float(att):
            sys.exit("ARRET : globale du moteur %s = %r, l'instrument herite %r" % (nom, getattr(mod, nom), att))
    _stdout = sys.stdout
    try:
        sys.stdout = open(os.devnull, "w")
        mod.certifier_gel()                 # custody transitive : gel M9 v2, ARRET si non conforme
    finally:
        sys.stdout.close(); sys.stdout = _stdout
    JRN("MOTEUR", "%s charge, sha256 %s..., gel jumeau M9 v2 conforme, P=%d T_MAX=%r CAP=%r"
        % (MOTEUR[0], h[:16], mod.P, mod.T_MAX, mod.CAP))
    mod._integrer_depose = mod.integrer
    mod._chercher_depose = mod.chercher_seuil
    if factice is not None:
        mod.integrer = factice["integrer"]
        mod.chercher_seuil = factice["chercher"]
        factice["module"]["m"] = mod
        JRN("PREVOL", "moteur FACTICE substitue (integrer, chercher_seuil) apres verification de custody")
    return mod


def rebind_P(mod, p):
    """m12_pilote_v3.py l.576-582 : re-liaison de P et garde G3 rejouee
    (a chaque changement de degre)."""
    if mod.P == int(p) and getattr(mod, "_p_garde", None) == int(p):
        return mod
    mod.P = int(p)
    mod._p_garde = int(p)
    _stdout = sys.stdout
    try:
        sys.stdout = open(os.devnull, "w")
        mod.garde_G3()
    finally:
        sys.stdout.close(); sys.stdout = _stdout
    return mod


def moteur_explose(mod, w2, s, p, sgn=1, n_pas=None):
    """Le booleen du moteur, APPELE TEL QUEL ; n_pas re-lie T_MAX (LD-14)."""
    rebind_P(mod, p)
    T_sauve = mod.T_MAX
    try:
        if n_pas is not None:
            mod.T_MAX = n_pas * mod.DT
        with np.errstate(over="ignore", invalid="ignore"):
            ex = mod.integrer(w2, [s], sgn)
    finally:
        mod.T_MAX = T_sauve
    return bool(np.asarray(ex)[0])


def fabriquer_factice(table_s):
    """Pre-vol : table (p, w2, sgn) -> seuil de CETTE branche (gel alpha v5,
    4.4) ; integrer explose ssi s >= seuil ; chercher_seuil rend le seuil
    avec le motif de la lignee. Un signe absent de la table est une faute
    de plomberie et leve KeyError : le pre-vol doit la voir."""
    module = {"m": None}

    def chercher(w2, sgn=1, dt=None, g=None):
        return table_s[(module["m"].P, "%.2f" % w2, int(sgn))], "OK|pas=6.03e-07"

    def integrer(w2, s_arr, sgn=1, dt=None, g=None):
        th = table_s[(module["m"].P, "%.2f" % w2, int(sgn))]
        return np.asarray(s_arr, float) >= th
    return {"chercher": chercher, "integrer": integrer, "module": module}


def garde_signe_factice(table, s_etoile, signes):
    """D-M17-58 (gel v4, 10 (ii)) : au pre-vol, table_factice[(p, w2, sgn)]
    == sF pour CHAQUE point, au signe joue. Rend la liste des fautes."""
    fautes = []
    for p in DEGRES:
        for w2 in W2S:
            sg = signes[(p, w2)]["sgn"]
            cle = (p, "%.2f" % w2, sg)
            if cle not in table or table[cle] != s_etoile[(p, w2)]:
                fautes.append("(%d, %.2f, %+d) : table %r != sF %r"
                              % (p, w2, sg, table.get(cle), s_etoile[(p, w2)]))
    return fautes


def lire_carte(registre):
    d = json.load(open(os.path.join(registre, CARTE[0]), encoding="utf-8"))
    carte = d["resultats"]["carte"]
    s_etoile = {}
    for p in DEGRES:
        for w2 in W2S:
            cle = "%d|%.12f" % (p, w2)
            rec = carte[cle]
            s_etoile[(p, w2)] = float(rec["sF"])
    return s_etoile, d


def _s_de(champ):
    if isinstance(champ, dict):
        return champ.get("s")
    return champ


def lire_signes(registre):
    """Gel alpha v5, 4.4 : par point, sP, sM, asym, frag de la carte ; le
    signe joue est frag, ou +1 la ou la carte ne porte pas de second seuil
    (p = 4). Controle : sF == min(sP, sM) au bit et frag == signe du
    minimum ; une carte qui ne le rend pas ARRETE."""
    d = json.load(open(os.path.join(registre, CARTE[0]), encoding="utf-8"))
    carte = d["resultats"]["carte"]
    S = {}
    for p in DEGRES:
        for w2 in W2S:
            rec = carte["%d|%.12f" % (p, w2)]
            sP, sM = _s_de(rec.get("sP")), _s_de(rec.get("sM"))
            sF, frag, asym = float(rec["sF"]), rec.get("frag"), rec.get("asym")
            if sM is None:
                ok = (frag is None) and (abs(float(sP) - sF) <= 1e-12 * sF)
                sgn = 1
            else:
                mn = min(float(sP), float(sM))
                ok = (abs(mn - sF) <= 1e-12 * sF) and (int(frag) == (1 if float(sP) <= float(sM) else -1))
                sgn = int(frag)
            if not ok:
                sys.exit("ARRET carte (gel alpha 4.4) : sF, sP, sM, frag incoherents au point %d|%.2f" % (p, w2))
            S[(p, w2)] = {"sF": sF, "sP": sP, "sM": sM, "frag": frag, "asym": asym, "sgn": sgn}
    return S


def plancher_lnA(p):
    """Gel alpha v5, 10.3 : delta / ((alpha_p + 2)(alpha_p + 3)), exact."""
    a = alpha_de(p)
    return DELTA / ((a + 2) * (a + 3))


TABLE_GEL_4_2 = {(4, 1.73): 2.005502036107, (5, 1.73): 0.656225641109, (7, 1.73): 0.494776327322,
                 (4, 2.27): 2.918324587849, (5, 2.27): 1.408091737101, (7, 2.27): 0.901634558208,
                 (4, 2.80): 8.129205119847, (5, 2.80): 2.593139026592, (7, 2.80): 1.604571976496}


def controle_carte(s_etoile):
    """Regle 11 : les neuf s* lus concordent PAR VALEUR avec la table du gel
    alpha 4.2 (12 decimales imprimees -> tolerance 5e-13, loin sous
    l'espacement minimal de la carte)."""
    ecarts = {}
    for k, v in TABLE_GEL_4_2.items():
        ecarts[k] = abs(s_etoile[k] - v)
    return max(ecarts.values()) <= 5e-13, ecarts


# =====================================================================
# 7. LES AJUSTEMENTS (gel alpha 7 ; LD-11)
# =====================================================================

def _regression(z, y):
    zm, ym = z.mean(), y.mean()
    vz = ((z - zm) ** 2).sum()
    b = ((z - zm) * (y - ym)).sum() / vz
    a = ym - b * zm
    res = y - a - b * z
    return a, b, float((res ** 2).sum())


def _minimiser_1d(fonc, lo, hi, n_scan=64, iters=80):
    """Balayage en log(t* - lo) puis section doree (LD-11)."""
    grille = lo + (hi - lo) * np.exp(np.linspace(math.log(1e-6), 0.0, n_scan))
    vals = [fonc(t) for t in grille]
    i = int(np.argmin(vals))
    a = grille[max(i - 1, 0)]; b = grille[min(i + 1, n_scan - 1)]
    phi = (math.sqrt(5.0) - 1) / 2
    c = b - phi * (b - a); d = a + phi * (b - a)
    fc, fd = fonc(c), fonc(d)
    for _ in range(iters):
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - phi * (b - a); fc = fonc(c)
        else:
            a, c, fc = c, d, fd
            d = a + phi * (b - a); fd = fonc(d)
    t = (a + b) / 2
    return t, fonc(t)


def ajustement_I(t, y, t_lo, t_hi):
    """alpha LIBRE : min sur t* de SS(t*) ; rend alpha, lnA, t*, SS."""
    def SS(ts):
        z = np.log(ts - t)
        return _regression(z, y)[2]
    ts, ss = _minimiser_1d(SS, t_lo, t_hi)
    a, b, _ = _regression(np.log(ts - t), y)
    return {"alpha": -b, "lnA": a, "t_star": ts, "SS": ss}


def ajustement_II(t, y, alpha_fixe, t_lo, t_hi):
    """alpha FIXE : min sur t* de sum (y + alpha z - moy)^2 ; rend lnA, t*."""
    def SS(ts):
        u = y + alpha_fixe * np.log(ts - t)
        return float(((u - u.mean()) ** 2).sum())
    ts, ss = _minimiser_1d(SS, t_lo, t_hi)
    u = y + alpha_fixe * np.log(ts - t)
    return {"lnA": float(u.mean()), "t_star": ts, "SS": ss}


def exposants_locaux(t, y, t_star):
    z = np.log(t_star - t)
    return -(np.diff(y) / np.diff(z))


def fenetre_de(t, t_star, tau_c, tau_d, eps=0.0):
    """Appartenance tau_CAP <= t* - t <= tau_dom, a eps pres aux deux bornes
    (LD-11 : eps = 1e-6 dt, sinon un point pose SUR une borne bascule
    dedans/dehors au dernier bit de t* et le point fixe n'existe pas)."""
    tau = t_star - t
    return np.where((tau >= tau_c - eps) & (tau <= tau_d + eps))[0]


def ajuster_point_fixe(t, x, w2, p, dt):
    """7.2 : t*_0 = t_dernier + tau_CAP ; iterer jusqu'a fenetre stable."""
    tau_c, tau_d = tau_cap(w2), tau_dom(w2)
    n_min = int(math.floor((tau_d - tau_c) / dt)) - 1
    ok = np.isfinite(x) & (x != 0)
    t, x = t[ok], x[ok]
    y = np.log(np.abs(x))
    t_last = float(t[-1])
    t_star = t_last + tau_c
    eps = 1e-6 * dt
    journal = []
    fen = fenetre_de(t, t_star, tau_c, tau_d, eps)
    for it in range(1, ITER_MAX_FENETRE + 1):
        if len(fen) < max(n_min, 3):
            return {"statut": "G-fen", "iterations": it, "n_points": int(len(fen)), "n_min": n_min}
        tt, yy = t[fen], y[fen]
        aj = ajustement_I(tt, yy, float(tt[-1]) * (1 + 1e-12) + 1e-12 * tau_c, t_last + 2 * tau_d)
        journal.append((it, float(t_star), float(aj["t_star"]), int(len(fen))))
        fen_new = fenetre_de(t, aj["t_star"], tau_c, tau_d, eps)
        if np.array_equal(fen_new, fen):
            t_star = aj["t_star"]
            ajII = ajustement_II(tt, yy, float(alpha_de(p)), float(tt[-1]) * (1 + 1e-12) + 1e-12 * tau_c,
                                 t_last + 2 * tau_d)
            loc = exposants_locaux(tt, yy, t_star)
            return {"statut": "POINT_FIXE", "iterations": it, "n_points": int(len(fen)), "n_min": n_min,
                    "alpha": float(aj["alpha"]), "lnA_I": float(aj["lnA"]), "t_star": float(t_star),
                    "SS_I": aj["SS"], "lnA_II": ajII["lnA"], "t_star_II": ajII["t_star"], "SS_II": ajII["SS"],
                    "disp_locale": float(loc.max() - loc.min()), "alpha_local_min": float(loc.min()),
                    "alpha_local_max": float(loc.max()), "journal": journal}
        t_star, fen = aj["t_star"], fen_new
    return {"statut": "PAS_DE_POINT_FIXE", "iterations": ITER_MAX_FENETRE, "n_points": int(len(fen)),
            "n_min": n_min, "journal": journal}


def ajuster_derniere_fenetre(t, x, w2, p, dt, T_max):
    """G-seuil (LD-10) : fenetre = points de [T_max - (tau_dom - tau_CAP), T_max],
    t* LIBRE dans (t_dernier, t_dernier + 2 tau_dom]."""
    tau_c, tau_d = tau_cap(w2), tau_dom(w2)
    n_min = int(math.floor((tau_d - tau_c) / dt)) - 1
    ok = np.isfinite(x) & (x != 0)
    t, x = t[ok], x[ok]
    fen = np.where(t >= T_max - (tau_d - tau_c) - 0.5 * dt)[0]
    if len(fen) < max(n_min, 3):
        return {"statut": "G-fen", "n_points": int(len(fen)), "n_min": n_min}
    tt, yy = t[fen], np.log(np.abs(x[fen]))
    t_last = float(tt[-1])
    aj = ajustement_I(tt, yy, t_last * (1 + 1e-12) + 1e-12 * tau_c, t_last + 2 * tau_d)
    ajII = ajustement_II(tt, yy, float(alpha_de(p)), t_last * (1 + 1e-12) + 1e-12 * tau_c, t_last + 2 * tau_d)
    loc = exposants_locaux(tt, yy, aj["t_star"])
    return {"statut": "AJUSTE", "n_points": int(len(fen)), "n_min": n_min, "alpha": float(aj["alpha"]),
            "lnA_I": float(aj["lnA"]), "t_star": float(aj["t_star"]), "SS_I": aj["SS"],
            "lnA_II": ajII["lnA"], "t_star_II": ajII["t_star"], "SS_II": ajII["SS"],
            "disp_locale": float(loc.max() - loc.min())}


def cn_jacobi(u, m):
    from scipy.special import ellipj
    return ellipj(u, m)[1]


def periode_cn(m, Omega):
    from scipy.special import ellipk
    return 4.0 * float(ellipk(m)) / Omega


def tol_ordre(alpha):
    """LD-4 : log2((1+b)/(1+b/2)), b = (alpha + q_s + 1)/M."""
    b = (float(alpha) + ORDRE_SCHEMA + 1) / M_PAS
    return math.log2((1 + b) / (1 + b / 2))


PLAFOND_ORDRE = float(ETA) * 1.0          # eta x (ecart entre ordres consecutifs = 1)

# =====================================================================
# 8. LE TEMOIN NEGATIF CLASSIQUE (gel temoin v9 403488b4f6c319e9, base v7 8b083e9f109b5a8e)
# =====================================================================

def plafonds_T1(D0):
    cap0 = C_0 * abs(D0)
    return [cap0 * Q_ECH ** j for j in range(N_PLAFONDS)]


def lire_T1(t_c, caps, T_0, T_max):
    """La lecture de T-1 (4.4, 8, LD-1, LD-2) sur un dictionnaire
    {CAP_j : t_c_j ou None}. Pure : le banc la nourrit de flots synthetiques."""
    L = {"caps": caps, "t_c": [t_c.get(c) for c in caps], "T_0": T_0, "T_MAX": T_max}
    if t_c.get(caps[0]) is None or t_c[caps[0]] > T_0:
        L["W_croissance"] = "MORD"
        return L
    L["W_croissance"] = "MUETTE"
    y = [t_c[c] / c for c in caps if t_c.get(c) is not None and t_c[c] <= T_max]
    L["y"] = y
    R = []
    for j in range(len(caps) - 1):
        a, b = t_c.get(caps[j]), t_c.get(caps[j + 1])
        if a is None or b is None or a > T_max or b > T_max:
            R.append(float("inf"))
        else:
            R.append(b / a)
    L["R"] = R
    disp = (max(y) - min(y)) / (sum(y) / len(y)) if len(y) >= 2 else float("inf")
    tol_R = Q_ECH * disp
    L["disp_y"] = disp
    L["tol_R"] = tol_R
    L["tol_R_sur_q_moins_1"] = tol_R / (Q_ECH - 1)
    L["plafond_R"] = float(ETA_R * (Q_ECH - 1))
    L["resolution_ok"] = tol_R <= float(ETA_R * (Q_ECH - 1))
    finis = [r for r in R if math.isfinite(r)]
    L["fenetre_q"] = (len(finis) == len(R)) and all(abs(r - Q_ECH) <= tol_R for r in R)
    L["fenetre_1"] = (len(finis) == len(R)) and all(abs(r - 1) <= tol_R for r in R)
    non_croissant = all(R[j + 1] <= R[j] for j in range(len(R) - 1)) if finis == R else False
    L["saturation"] = (finis == R) and non_croissant and abs(R[-1] - 1) <= float(ETA_R * (Q_ECH - 1))
    return L


def lire_W_integrales(flot_dt, flot_dt2, dt):
    """Temoin v7, entree W-integrales et LD-16 : q_int = log2(derive(dt)/
    derive(dt/2)) contre 4, pour H1 et N ; tol_int = log2((1+b)/(1+b/2)),
    b = omega_max dt, omega_max^2 = w^2 + 3 lambda x_max^2 sur le flot a
    dt ; plafond eta x 1 ; plancher machine c_pl x eps x N_pas(dt/2)."""
    eps = float(np.finfo(float).eps)
    omega2 = DS_W * DS_W + 3 * DS_LAM * flot_dt.x_max * flot_dt.x_max
    b = math.sqrt(omega2) * dt
    tol = math.log2((1 + b) / (1 + b / 2))
    plancher = C_PL * eps * flot_dt2.n
    W = {"omega_max": math.sqrt(omega2), "b": b, "tol_int": tol, "tol_int_sur_1": tol / 1.0,
         "plafond_int": PLAFOND_INT, "plancher_dt2": plancher, "n_pas_dt2": flot_dt2.n, "integrales": {}}
    mord = False
    for nom, d1, d2 in (("H1", flot_dt.derive_H1, flot_dt2.derive_H1), ("N", flot_dt.derive_N, flot_dt2.derive_N)):
        I = {"derive_dt": d1, "derive_dt2": d2}
        if d2 < plancher:
            I["q_int"] = None; I["statut"] = "NON LUE (plancher, LD-16)"
        else:
            q = math.log2(d1 / d2)
            I["q_int"] = q; I["ecart_a_4"] = abs(q - ORDRE_SCHEMA)
            I["statut"] = "PASSE" if abs(q - ORDRE_SCHEMA) <= tol else "MORD"
            mord = mord or (I["statut"] == "MORD")
        W["integrales"][nom] = I
    W["resolution_ok"] = tol <= PLAFOND_INT
    W["W_integrales"] = "MORD" if mord else "PASSE"
    return W


def jouer_T1(compteur, sortie, flot_cls=FlotDS):
    """T-1 : deux etats, DEUX flots chacun (dt, et dt/2 pour W-integrales
    SEULE, v7) ; T_MAX derive en deux temps (4.4) sur le flot a dt."""
    res = {}
    for nom, x0, xp0, D0, Dp0 in ETATS_T1:
        caps = plafonds_T1(D0)
        flot = flot_cls((x0, xp0, D0, Dp0), caps, DT1)
        flot.prolonger(T_0, T_lectures_pic=(T1B_T, C_T * T1B_T))
        compteur["comptes"] += 1
        tc0 = flot.t_c.get(caps[0])
        if tc0 is None or tc0 > T_0:
            JRN("T1-%s" % nom, "W-croissance MORD : |D| n'a pas franchi CAP_0=%g avant T_0=%g" % (caps[0], T_0))
            T_max = T_0
            prediction = None
        else:
            prediction = tc0 * caps[-1] / caps[0]
            T_max = C_T * prediction
            JRN("T1-%s" % nom, "t_c(CAP_0=%g) = %.6f ; PREDICTION t_c(CAP_4=%g) = %.6f ; T_MAX = c_T x = %.6f (consigne AVANT verification)"
                % (caps[0], tc0, caps[-1], prediction, T_max))
            if T_max > T_0:
                flot.prolonger(T_max, T_lectures_pic=(T1B_T, C_T * T1B_T))
        L = lire_T1(flot.t_c, caps, T_0, T_max)
        L.update({"etat": (x0, xp0, D0, Dp0), "prediction_tc4": prediction,
                  "H1_0": flot.H1_0, "N_0": flot.N_0, "derive_H1_dt": flot.derive_H1,
                  "derive_N_dt": flot.derive_N, "x_max": flot.x_max, "D_max": flot.D_max,
                  "pics": flot.pics, "non_fini": flot.non_fini, "n_pas": flot.n})
        JRN("T1-%s" % nom, "t_c = %s" % ["%.4f" % v if v is not None else "None" for v in L["t_c"]])
        if L["W_croissance"] == "MUETTE":
            JRN("T1-%s" % nom, "y = t_c/CAP = %s ; R = %s ; disp = %.5f ; tol_R = %.5f ; tol_R/(q-1) = %.5f (plafond %.4f) ; fenetre_q=%s fenetre_1=%s saturation=%s"
                % (["%.5f" % v for v in L["y"]], ["%.5f" % v for v in L["R"]], L["disp_y"], L["tol_R"],
                   L["tol_R_sur_q_moins_1"], L["plafond_R"], L["fenetre_q"], L["fenetre_1"], L["saturation"]))
        JRN("T3a-%s" % nom, "derive relative sur le flot a dt=%g (%d pas) : H1 %.3e (H1_0=%g), N %.3e (N_0=%g)"
            % (DT1, flot.n, flot.derive_H1, flot.H1_0, flot.derive_N, flot.N_0))
        lignes = ["# flot T-1 etat %s : t x D H1 N (un point tous les %d pas de dt=%g)" % (nom, flot.pas_serie, DT1)]
        lignes += ["%.6f %.17g %.17g %.17g %.17g" % r for r in flot.serie]
        ecrire_ascii(os.path.join(sortie, "temoin_T1_flot_%s.txt" % nom), "\n".join(lignes))
        # le flot a dt/2, POUR W-INTEGRALES SEULE (v7) : meme etat, meme horizon
        flot2 = flot_cls((x0, xp0, D0, Dp0), caps, DT1 / 2)
        flot2.prolonger(max(T_max, T_0))
        compteur["comptes"] += 1
        W = lire_W_integrales(flot, flot2, DT1)
        L["W_integrales"] = W
        L["derive_H1_dt2"], L["derive_N_dt2"], L["n_pas_dt2"] = flot2.derive_H1, flot2.derive_N, flot2.n
        JRN("T3a-%s" % nom, "flot a dt/2 (%d pas, W-integrales seule) : H1 %.3e, N %.3e ; omega_max=%.4f b=%.5f tol_int=%.5f (plafond %.2f) ; q_int H1 = %s, N = %s -> %s"
            % (flot2.n, flot2.derive_H1, flot2.derive_N, W["omega_max"], W["b"], W["tol_int"], PLAFOND_INT,
               W["integrales"]["H1"].get("q_int"), W["integrales"]["N"].get("q_int"),
               "W-integrales " + W["W_integrales"] + ("" if all(I["q_int"] is not None for I in W["integrales"].values()) else " ; NON LUE au plancher sur " + ", ".join(k for k, I in W["integrales"].items() if I["q_int"] is None))))
        res[nom] = L
    return res


def jouer_T1b(compteur, fabrique_integrer, osc, cst=None):
    """T-1b (4.6) : trois recherches (CAP, T), (q CAP, T), (CAP, c_T T) avec
    l'algorithme transcrit ; puis la lecture (lois, tolerances, mirage,
    controle positif de transcription). `fabrique_integrer(cap, t_max)`
    rend l'integrateur a la signature du moteur."""
    jeux = [("a", T1B_CAP, T1B_T), ("b", Q_ECH * T1B_CAP, T1B_T), ("c", T1B_CAP, C_T * T1B_T)]
    res = {}
    for nom, cap, tm in jeux:
        t0 = time.perf_counter()
        s, motif, info = chercher_seuil_transcrit(fabrique_integrer(cap, tm), 0.0, cst=cst)
        compteur["comptes"] += 1
        ok, detail = controle_transcription_positif(s, motif, info, cst)
        res[nom] = {"CAP": cap, "T_MAX": tm, "seuil": s, "motif": motif, "k": info["k"],
                    "encadrement": info.get("encadrement"), "controle_positif": ok, "detail": detail,
                    "duree_s": time.perf_counter() - t0}
        JRN("T1b-%s" % nom, "CAP=%g T_MAX=%g -> seuil=%r motif=%s k=%d ; W-transcription (iii) %s : %s"
            % (cap, tm, s, motif, info["k"], "PASSE" if ok else "MORD", detail))
    return lire_T1b(res, osc)


def lire_T1b(res, osc):
    """Pure : lois de 4.6, tolerances derivees (LD-3), mirage, plafonds."""
    a, b, c = res["a"], res["b"], res["c"]
    L = {"recherches": res, "osc_enveloppe": osc}
    L["transcription_positif"] = all(res[k]["controle_positif"] for k in ("a", "b", "c"))
    if any(res[k]["seuil"] is None for k in ("a", "b", "c")):
        L["loi1"] = L["loi2"] = None
        L["regime"] = "SANS_SEUIL"
        L.update({"resolution_ok": False, "suit_lois": False, "stable": False, "k_attendu_0": False})
        return L
    pa, pb, pc = [float(pas_du_motif(res[k]["motif"]) or "nan") for k in ("a", "b", "c")]
    L["loi1"] = b["seuil"] / a["seuil"]
    L["loi2"] = c["seuil"] / a["seuil"]
    L["tol_loi1"] = Q_ECH * (pa / a["seuil"] + pb / b["seuil"] + osc)
    L["tol_loi2"] = (1.0 / C_T) * (pa / a["seuil"] + pc / c["seuil"] + osc)
    L["plafond_loi1"] = float(ETA * (Q_ECH - 1))
    L["plafond_loi2"] = float(ETA * (1 - Fraction(1, C_T)))
    L["resolution_ok"] = (L["tol_loi1"] <= L["plafond_loi1"]) and (L["tol_loi2"] <= L["plafond_loi2"])
    suit1 = abs(L["loi1"] - Q_ECH) <= L["tol_loi1"]
    suit2 = abs(L["loi2"] - 1.0 / C_T) <= L["tol_loi2"]
    stable1 = abs(L["loi1"] - 1) <= L["tol_loi1"]
    stable2 = abs(L["loi2"] - 1) <= L["tol_loi2"]
    L["suit_lois"] = suit1 and suit2
    L["stable"] = stable1 and stable2
    L["regime"] = "LOIS" if L["suit_lois"] else ("STABLE" if L["stable"] else "NI_L_UNE_NI_L_AUTRE")
    L["k_attendu_0"] = all(res[k]["k"] == 0 for k in ("a", "b", "c"))
    return L


def jouer_T2(compteur, sortie):
    """T-2 (5.3) : neuf bancs x deux pas ; W-bascule (8) : neuf de plus ;
    T-2a, T-2b (5.5). Tout est reel et court."""
    R = {"points": {}, "T2a": None, "T2b": {}}
    eps = float(np.finfo(float).eps)
    for p in DEGRES:
        a = float(alpha_de(p)); A = A_de(p)
        for w2 in W2S:
            td, tc, dt2 = tau_dom(w2), tau_cap(w2), dt2_de(w2)
            f = forcage_de(p, w2)
            tau0 = K_BASC * td
            cle = "%d|%.2f" % (p, w2)
            err = {}
            for nom_pas, dt in (("dt2", dt2), ("dt2/2", dt2 / 2)):
                etat = vers_composantes(*xm_et_derivees(p, tau0), w2)
                ph = phase2_pu(w2, p, etat, -tau0, dt, forcage=f, tau_star=0.0, tau_fin=tc)
                compteur["comptes"] += 1
                tau = -ph["t"]
                xm = A * tau ** (-a)
                e = float(np.max(np.abs((ph["x1"] + ph["x2"]) - xm) / np.abs(xm)))
                err[nom_pas] = {"e": e, "n_pas": int(ph["n"]), "evenement": ph["evenement"], "tau_fin": float(tau[-1])}
            p_obs = math.log2(err["dt2"]["e"] / err["dt2/2"]["e"]) if err["dt2/2"]["e"] > 0 else float("inf")
            plancher = eps * err["dt2/2"]["n_pas"]
            # CONSIGNATION SEULE (N-62, D-M17-47 : aucune tolerance neuve) :
            # au reglage prime, x = x1 + x2 s'evalue par compensation de
            # composantes ~ alpha(alpha+1)/((w2^2-1) tau^2) fois plus
            # grandes que x ; le plancher machine REEL de e est eps x R,
            # que le plancher eps x N du gel (5.4) ne modelise pas.
            # Mesure sur le flot a dt2/2, consignee pour l'acte
            # (trouvaille machine 1 contre le gel temoin v9, a arbitrer).
            R_comp = float(np.max((np.abs(ph["x1"]) + np.abs(ph["x2"])) / np.maximum(np.abs(ph["x1"] + ph["x2"]), 1e-300)))
            plancher_composantes = eps * R_comp
            tol_o = tol_ordre(a)
            lec = lecture_5_4(err["dt2/2"]["e"], p_obs, a, plancher_composantes)
            # W-bascule EN VOIE A (v9, 8) : g1 = la phase grossiere du v7,
            # de k' tau_dom_0 a k tau_dom_0, au pas dt_1 ; g2 = l'etage 2a,
            # de k tau_dom_0 a k tau_dom', au pas k tau_dom'/M. Comptes
            # MESURES, jamais assertes (v9 8, D-t-21).
            td0 = tau_dom_0(w2)
            etat_b = vers_composantes(*xm_et_derivees(p, KP_BASC * td0), w2)
            phg1 = phase2_pu(w2, p, etat_b, -KP_BASC * td0, DT1, forcage=f, tau_star=0.0,
                             arret_cap=x_bascule_0(p, w2), t_max=1e9)
            n_g1 = int(phg1["n"])
            phg2 = phase2_pu(w2, p, phg1["etat_fin"], float(phg1["t"][-1]), dt2a_de(w2),
                             forcage=f, tau_star=0.0, arret_cap=x_bascule(p, w2), t_max=1e9)
            n_g2 = int(phg2["n"])
            lo_g2, hi_g2 = intervalle_evenement(n_2a_nominal(), retard_2a(w2))
            phb1 = phg2
            n_b = n_g2
            t_b = float(phb1["t"][-1]); tau_b = -t_b
            xb_num = float(phb1["x1"][-1] + phb1["x2"][-1])
            phb2 = phase2_pu(w2, p, phb1["etat_fin"], t_b, dt2, forcage=f, tau_star=0.0, tau_fin=tc)
            compteur["comptes"] += 1
            tau2 = -phb2["t"]; xm2 = A * tau2 ** (-a)
            e_avec = float(np.max(np.abs((phb2["x1"] + phb2["x2"]) - xm2) / np.abs(xm2)))
            pt = {"alpha": a, "A": A, "tau_dom": td, "tau_CAP": tc, "dt2": dt2, "x_bascule": x_bascule(p, w2),
                  "CAP_p": cap_p(p, w2), "err": err, "p_obs": p_obs, "tol_ordre": tol_o,
                  "tol_ordre_sur_1": tol_o / 1.0, "plafond_ordre": PLAFOND_ORDRE,
                  "W_pas": lec["W_pas"],
                  "plancher_accum": plancher, "C_effectif": lec["C_effectif"],
                  "seuil_5_4": lec["seuil"], "ratio_seuil": lec["ratio_seuil"],
                  "R_composantes": R_comp, "plancher_composantes": plancher_composantes,
                  "e_dt2s2_sur_plancher_comp": err["dt2/2"]["e"] / plancher_composantes if plancher_composantes > 0 else float("inf"),
                  "W_plancher": lec["W_plancher"],
                  "e_sur_ln10": err["dt2"]["e"] / LN10,
                  "conversion_ok": err["dt2"]["e"] <= float(PLAFOND_ALPHA) * LN10,
                  "bascule": {"n_g1": n_g1, "n_g2": n_g2,
                              "intervalle_g2": [int(lo_g2), int(hi_g2)],
                              "g2_dans_intervalle": bool(lo_g2 <= n_g2 <= hi_g2),
                              "tau_b": tau_b, "x_b_num": xb_num,
                              "err_rel_bascule": abs(xb_num - A * tau_b ** (-a)) / (A * tau_b ** (-a)),
                              "e_avec": e_avec, "e_avec_sur_e_sans": e_avec / err["dt2"]["e"],
                              "n_pas_phase2": int(phb2["n"])},
                  "W_bascule": "PASSE" if (e_avec <= float(PLAFOND_ALPHA) * LN10 and lo_g2 <= n_g2 <= hi_g2) else "MORD"}
            if not lec["lu"]:
                pt["p_obs"] = None
            R["points"][cle] = pt
            JRN("T2-%s" % cle, "e(dt2)=%.4e (%d pas) e(dt2/2)=%.4e (%d) p_obs=%s tol_ordre=%.4f (plafond %.2f) W-pas %s ; 5.4 e/seuil=%.3f (C_eff=%.4f) W-plancher %s ; e/ln10=%.3e conversion(plafond 2/15) %s"
                % (err["dt2"]["e"], err["dt2"]["n_pas"], err["dt2/2"]["e"], err["dt2/2"]["n_pas"],
                   ("%.4f" % p_obs) if lec["lu"] else "NON LU", tol_o,
                   PLAFOND_ORDRE, pt["W_pas"], lec["ratio_seuil"], lec["C_effectif"], pt["W_plancher"], pt["e_sur_ln10"], pt["conversion_ok"]))
            JRN("Wb-%s" % cle, "VOIE A : g1 %d pas de dt1 (depuis tau=%.4e, k'=%d) ; g2 %d pas de dt_2a (intervalle [%d,%d] %s) ; bascule 2b a tau_b=%.4e (err %.2e) ; e_avec(dt2)=%.4e (x%.1f de e_sans, lecture D-t-19) W-bascule %s"
                % (n_g1, KP_BASC * td0, KP_BASC, n_g2, lo_g2, hi_g2,
                   "OK" if pt["bascule"]["g2_dans_intervalle"] else "HORS", tau_b,
                   pt["bascule"]["err_rel_bascule"], e_avec,
                   pt["bascule"]["e_avec_sur_e_sans"], pt["W_bascule"]))
    # T-2a : g = 0, f = 0, x = a cos t + b cos(w2 t)  (LD-8)
    w2 = T2A_W2
    etat = (T2A_A, T2A_B, 0.0, 0.0)
    horizon = 2 * math.pi / W1
    ph = phase2_pu(w2, 5, etat, 0.0, DT1, g=0.0, t_max=horizon + 0.5 * DT1)
    compteur["comptes"] += 1
    x_ex = T2A_A * np.cos(W1 * ph["t"]) + T2A_B * np.cos(w2 * ph["t"])
    e2a = float(np.max(np.abs((ph["x1"] + ph["x2"]) - x_ex)) / (T2A_A + T2A_B))
    R["T2a"] = {"w2": w2, "a": T2A_A, "b": T2A_B, "horizon": horizon, "dt": DT1, "n_pas": int(ph["n"]),
                "e": e2a, "PASSE": e2a <= float(PLAFOND_ALPHA) * LN10}
    JRN("T2a", "g=0 f=0 w2=%.2f horizon=%.4f dt=%g : e = %.4e -> %s" % (w2, horizon, DT1, e2a, "PASSE" if R["T2a"]["PASSE"] else "MORD"))
    # T-2b : x'''' = g x^(p-1) en vecteur (x, x', x'', x'''), sans forcage
    for p in DEGRES:
        a = float(alpha_de(p)); A = A_de(p)
        td, tc, dt = tau_dom(T2B_W2), tau_cap(T2B_W2), dt2_de(T2B_W2)
        y = np.array(xm_et_derivees(p, K_BASC * td))
        tau = K_BASC * td; e = 0.0; n = 0

        def F(v):
            return np.array([v[1], v[2], v[3], G_REF * v[0] ** (p - 1)])
        while tau > tc * (1 + 1e-12):
            k1 = F(y); k2 = F(y + .5 * dt * k1); k3 = F(y + .5 * dt * k2); k4 = F(y + dt * k3)
            y = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            tau -= dt; n += 1
            xm = A * tau ** (-a)
            e = max(e, abs(y[0] - xm) / abs(xm))
        compteur["comptes"] += 1
        R["T2b"][p] = {"e": float(e), "n_pas": n, "dt": dt, "PASSE": e <= float(PLAFOND_ALPHA) * LN10}
        JRN("T2b-p%d" % p, "tronquee x''''=g x^(p-1), fenetre [k tau_dom, tau_CAP] a w2=%.2f, %d pas : e = %.4e -> %s"
            % (T2B_W2, n, e, "PASSE" if R["T2b"][p]["PASSE"] else "MORD"))
    return R


def jouer_T3b(compteur):
    R = {}
    for (w, lam, x0) in T3B_JEUX:
        Om2 = w * w + lam * x0 * x0
        m = lam * x0 * x0 / (2 * Om2)
        Om = math.sqrt(Om2)
        x0_formule = math.sqrt(2 * m * Om2 / lam)
        per = periode_cn(m, Om)
        horizon = T3B_PERIODES * per
        ts, xs = flot_x_duffing(x0, w, lam, DT1, horizon)
        compteur["comptes"] += 1
        x_cf = x0 * cn_jacobi(Om * ts, m)
        e = float(np.max(np.abs(xs - x_cf)) / x0)
        cle = "w%g_lam%g_x0%g" % (w, lam, x0)
        R[cle] = {"Omega2": Om2, "m": m, "x0_formule": x0_formule, "periode": per, "horizon": horizon,
                  "n_pas": int(len(ts) - 1), "e": e, "PASSE": e <= float(PLAFOND_ALPHA) * LN10}
        JRN("T3b-%s" % cle, "Omega^2=%g m=%g x0(formule)=%.12f periode=%.6f, %d periodes, %d pas : e = %.4e -> %s"
            % (Om2, m, x0_formule, per, T3B_PERIODES, R[cle]["n_pas"], e, "PASSE" if R[cle]["PASSE"] else "MORD"))
    return R


def compte_attendu_temoin():
    return {"T1": 2 * len(ETATS_T1), "T1b": 3, "T2": len(DEGRES) * len(W2S) * 2, "T2a": 1, "T2b": len(DEGRES),
            "T3a": 0, "T3b": len(T3B_JEUX), "W_bascule": len(DEGRES) * len(W2S)}


def cascade_temoin(L):
    """10, ordre de lecture 1, 2, 3, 3bis, 4, 4bis, 5, 6 (LD-2). Pure."""
    T1, T1b, T2 = L["T1"], L["T1b"], L["T2"]
    if not L.get("transcription_ok", True) or not T1b["transcription_positif"]:
        return "BANC NON JOUE", "branche 1 : W-transcription MORD"
    if any(T1[e]["W_croissance"] == "MORD" for e in T1):
        return "NON CONCLUANT DE TEMOIN", "branche 2 : W-croissance MORD"
    if any(T1[e]["saturation"] for e in T1):
        return "REGLAGE REFUTE", "branche 3 : T-1 rend R -> 1 (saturation)"
    if T1b["regime"] == "STABLE":
        return "REGLAGE REFUTE", "branche 3 : W-mirage MORD (seuil stable sous les deux variations)"
    regime_T1 = all(T1[e]["fenetre_q"] or T1[e]["fenetre_1"] for e in T1)
    if (not regime_T1) or T1b["regime"] in ("NI_L_UNE_NI_L_AUTRE", "SANS_SEUIL"):
        return "NON CONCLUANT DE REGIME", "branche 3bis : R hors des deux fenetres, ou rapports de 4.6 hors des deux lois"
    pts = T2["points"]
    mordent = ["%s %s" % (g.replace("_", "-"), k) for k in pts for g in ("W_pas", "W_plancher", "W_bascule") if pts[k][g] == "MORD"]
    if mordent:
        return "NON CONCLUANT D'INTEGRATEUR", "branche 4 : %s MORD" % ", ".join(mordent)
    if any(not T1[e]["resolution_ok"] for e in T1) or not T1b["resolution_ok"] or \
            any(pts[k]["tol_ordre"] > PLAFOND_ORDRE for k in pts) or \
            any(not T1[e].get("W_integrales", {"resolution_ok": True})["resolution_ok"] for e in T1):
        return "NON CONCLUANT DE RESOLUTION", "branche 4bis : une tolerance depasse son plafond"
    qualifie = all(T1[e]["fenetre_q"] for e in T1) and T1b["suit_lois"] and \
        all(pts[k]["W_pas"] == "PASSE" and pts[k]["conversion_ok"] for k in pts)
    if not qualifie:
        return "NON CONCLUANT DE REGIME", "branche 3bis : la branche 5 n'est pas atteinte sans branche nommee"
    T3 = L.get("T3b", {})
    T3a_mord = any(T1[e].get("W_integrales", {}).get("W_integrales") == "MORD" for e in T1)
    if T3a_mord:
        return "REGLAGE QUALIFIE (bonus T-3 retire)", "branche 6 : T-3 mord seul (W-integrales, T-3a)"
    if T3 and not all(T3[k]["PASSE"] for k in T3):
        return "REGLAGE QUALIFIE (bonus T-3 retire)", "branche 6 : T-3 mord seul (T-3b)"
    return "REGLAGE QUALIFIE", "branche 5 : T-1 R = q, T-1b les deux lois, T-2 p_obs = 4 sous la conversion"


def verdict_comptes(compteur, n_att, verdict, branche, non_joue):
    """Pure : comptes + sautes == attendus, sinon le run n'est pas joue."""
    ok = compteur["comptes"] + compteur["sautes"] == n_att
    if not ok and verdict != non_joue:
        return "MORD", non_joue, "%s MORD (%d + %d != %d)" % ("W-comptes" if non_joue.startswith("BANC") else "G-comptes",
                                                             compteur["comptes"], compteur["sautes"], n_att)
    return ("PASSE" if ok else "MORD"), verdict, branche


def ecrire_manifest(sortie, nom="MANIFEST.sha256"):
    """sha256sum -c compatible ; tout fichier de sortie, sauf lui-meme."""
    lignes = []
    for f in sorted(os.listdir(sortie)):
        if f == nom:
            continue
        ch = os.path.join(sortie, f)
        if os.path.isfile(ch):
            lignes.append("%s *%s" % (sha_brut(ch), f))
    ch = os.path.join(sortie, nom)
    ecrire_ascii(ch, "\n".join(lignes))
    JRN("MANIFEST", "%s : %d fichiers, empreinte B %s, taille %d" % (ch, len(lignes), empreinte_B(ch), os.path.getsize(ch)))
    return ch


def controle_9bis(L, reference, profondeur, exemptes):
    """Temoin v9, 9bis : les QUATRE sous-arbres de RESULTAT (/T1, /T1b,
    /T3a, /T3b) se comparent au run 85 par ENUMERATION a PROFONDEUR
    DECLAREE ; exemptions duree/chemins A L'INTERIEUR ; tout le reste
    HORS PERIMETRE PAR CONSTRUCTION. Rend la liste des ecarts.

    v11 (D-v10-1) : la reference est lue dans un FICHIER JSON, L est un objet
    Python. La serialisation change des types -- un tuple devient une liste,
    une cle entiere une chaine -- et la comparaison finale (a != b) opposait
    (1.0, 0.0) a [1.0, 0.0] : NEUF cles du perimetre valent un tuple en
    memoire, si bien qu'AUCUN run ne pouvait passer ce controle, quelle que
    soit sa mesure. La comparaison se fait donc sur la SERIALISATION -- ce
    que le run ECRIRA dans son JSON, meme fonction que la sortie. Rien n'est
    relache : les valeurs se comparent toujours au bit."""
    def _ser(o):
        if isinstance(o, dict):
            return {str(k): _ser(v) for k, v in o.items()}
        if isinstance(o, (list, tuple, set)):
            return [_ser(v) for v in o]
        if isinstance(o, float) and not math.isfinite(o):
            return repr(o)
        if isinstance(o, (np.floating, np.integer, np.bool_)):
            return _ser(o.item())
        if isinstance(o, np.ndarray):
            return _ser(o.tolist())
        if isinstance(o, Fraction):
            return str(o)
        return o

    L, reference = _ser(L), _ser(reference)
    ecarts = []

    def marche(a, b, chemin, prof):
        if prof > profondeur:
            return
        if isinstance(a, dict) and isinstance(b, dict):
            for k in sorted(set(a) | set(b)):
                if str(k) in exemptes:
                    continue
                if k not in a or k not in b:
                    ecarts.append("%s/%s (cle absente d'un cote)" % (chemin, k))
                else:
                    marche(a[k], b[k], "%s/%s" % (chemin, k), prof + 1)
            return
        if isinstance(a, list) and isinstance(b, list):
            if len(a) != len(b):
                ecarts.append("%s (longueurs %d != %d)" % (chemin, len(a), len(b)))
                return
            for i, (va, vb) in enumerate(zip(a, b)):
                marche(va, vb, "%s[%d]" % (chemin, i), prof + 1)
            return
        if a != b:
            ecarts.append("%s (%r != %r)" % (chemin, a, b))
    for cle in PERIM_9BIS:
        marche(L.get(cle), reference.get(cle), "/" + cle, 0)
    return ecarts


def executer_temoin(registre, sortie, mod, prevol=None, ref_9bis=None):
    """Le banc entier, dans l'ordre : controles de transcription (7 (ii),
    4.6bis algorithme contre le moteur), T-1, T-1b, T-2, T-3b, cascade,
    JSON, MANIFEST. `prevol` : fabriques synthetiques (pre-vol)."""
    compteur = {"comptes": 0, "sautes": 0, "sautes_noms": []}
    attendu = compte_attendu_temoin(); n_att = sum(attendu.values())
    JRN("COMPTE", "attendus (forme derivee) : %s = %d" % (attendu, n_att))
    L = {"mode": "temoin", "prevol": bool(prevol)}
    sym = controles_symboliques()
    L["symbolique"] = sym
    tr_ok = all(sym.values())
    JRN("W-transcr.", "controles symboliques 7 (ii) : %d/%d %s" % (sum(sym.values()), len(sym), "PASSE" if tr_ok else "MORD"))
    alg = controle_algorithme_contre_moteur(mod)
    L["algorithme_vs_moteur"] = alg
    JRN("W-transcr.", "algorithme transcrit contre chercher_seuil DEPOSE (integrer synthetique) : %d/%d %s"
        % (alg["n_ok"], alg["n"], "PASSE" if alg["ok"] else "MORD"))
    texte, emp = champ_de_forces_tirage()
    ecrire_ascii(os.path.join(sortie, "temoin_champ_forces_tirage.txt"), texte)
    emp_tir = empreinte_B_texte(colonnes_x_D_seules(texte))
    L["champ_forces_empreinte"] = emp
    L["tirage_empreinte"] = emp_tir
    JRN("W-transcr.", "champ de forces (2.11), tirage declare : TIRAGE %s (bit-reproductible, opposable) ; CHAMP %s (NON bit-reproductible entre machines -- se compare sur les NOMBRES, D-I-5)" % (emp_tir, emp))
    if CHAMP_COMPARE:
        try:
            cmpc = comparer_champs_ulp(texte, open(CHAMP_COMPARE, encoding="utf-8").read())
        except OSError as _e:
            cmpc = {"verdict": "NON JOUE", "resume": "NON JOUE -- fichier illisible : %s" % _e}
        L["W_transcription_nombres"] = cmpc
        JRN("W-transcr.", "SUR LES NOMBRES contre %s : %s" % (os.path.basename(str(CHAMP_COMPARE)), cmpc["resume"]))
    else:
        L["W_transcription_nombres"] = {"verdict": "A COMPARER",
            "resume": "seconde transcription non fournie -- fichier LIVRE, la comparaison se joue sur les nombres (bornes %g / %g ulp -- x'' libm inter-machines, D'' re-association inter-plumes)" % (BORNE_ULP, BORNE_ULP)}
        JRN("W-transcr.", "SUR LES NOMBRES : A COMPARER (seconde transcription non fournie ; le fichier est livre)")
    cm = L["W_transcription_nombres"]["verdict"]
    # "A COMPARER" et "NON JOUE" ne mordent pas -- ils se consignent
    # (un controle absent n'est pas un controle en echec, N-62).
    L["transcription_ok"] = tr_ok and alg["ok"] and cm != "MORD"
    if not L["transcription_ok"]:
        compteur["sautes"] = n_att
        compteur["sautes_noms"] = ["%s x%d" % (k, v) for k, v in attendu.items() if v]
        L["T1"], L["T1b"], L["T2"] = {}, {"transcription_positif": False}, {"points": {}}
        L["verdict"], L["branche"] = "BANC NON JOUE", "branche 1 : W-transcription MORD avant tout run"
    else:
        if prevol:
            L["T1"] = jouer_T1(compteur, sortie, flot_cls=prevol["flot_cls"])
            osc = prevol["osc"]
            L["T1b"] = jouer_T1b(compteur, prevol["fabrique_T1b"], osc)
        else:
            L["T1"] = jouer_T1(compteur, sortie)
            pics = dict((T, (tp, dm)) for (T, tp, dm) in L["T1"]["A"]["pics"])
            osc = max((T - pics[T][0]) / T for T in pics) if pics else float("inf")
            L["osc_detail"] = {"%g" % T: pics[T] for T in pics}
            JRN("T1b", "oscillation de l'enveloppe lue sur le flot A : osc = max_T (T - t_pic)/T = %.5f (%s)" % (osc, L["osc_detail"]))
            etat_A = ETATS_T1[0][1:]

            def fabrique(cap, tm):
                return integrer_ds_pour_recherche(etat_A, cap, tm)
            L["T1b"] = jouer_T1b(compteur, fabrique, osc)
        T1b = L["T1b"]
        if T1b.get("loi1") is not None:
            JRN("T1b", "loi 1 : s*(qCAP,T)/s*(CAP,T) = %.6f (attendu q=%d, tol %.3e, plafond %.3f) ; loi 2 : s*(CAP,c_T T)/s*(CAP,T) = %.6f (attendu 1/c_T=%.3f, tol %.3e, plafond %.3f) ; regime %s ; k=0 partout %s"
                % (T1b["loi1"], Q_ECH, T1b["tol_loi1"], T1b["plafond_loi1"], T1b["loi2"], 1.0 / C_T,
                   T1b["tol_loi2"], T1b["plafond_loi2"], T1b["regime"], T1b["k_attendu_0"]))
        L["T2"] = jouer_T2(compteur, sortie)
        L["T3b"] = jouer_T3b(compteur)
        L["T3a"] = {e: L["T1"][e].get("W_integrales") for e in L["T1"]}
        L["lectures_non_lues"] = []
        for _k in sorted(L["T2"]["points"]):
            if L["T2"]["points"][_k]["W_pas"].startswith("NON LU"):
                L["lectures_non_lues"].append("W-pas %s NON LU (plancher de composition, 5.4)" % _k)
        for e in L["T1"]:
            for nomI, I in L["T1"][e].get("W_integrales", {}).get("integrales", {}).items():
                if I.get("q_int") is None:
                    L["lectures_non_lues"].append("W-integrales %s etat %s NON LUE (plancher machine, LD-16)" % (nomI, e))
        if L["T1b"].get("regime") == "SANS_SEUIL":
            L["lectures_non_lues"].append("T-1b lois NON LUES (une recherche sans seuil)")
        for e in L["T1"]:
            if L["T1"][e]["W_croissance"] == "MORD":
                L["lectures_non_lues"].append("T-1 etat %s : R NON LU (W-croissance MORD)" % e)
        if ref_9bis is not None:
            ec = controle_9bis(L, ref_9bis["reference"], ref_9bis["profondeur"], ref_9bis["exemptes"])
            L["controle_9bis"] = {"perimetre": list(PERIM_9BIS), "profondeur": ref_9bis["profondeur"],
                                  "exemptes": sorted(ref_9bis["exemptes"]), "n_ecarts": len(ec),
                                  "ecarts": ec[:40], "reference": ref_9bis.get("nom", "?"),
                                  "depot_empreinte": ref_9bis.get("depot_empreinte"),
                                  "custody": ref_9bis.get("custody")}
            JRN("9bis", "perimetre %s a profondeur %d, exemptes %s : %d ecart(s)"
                % ("/".join(PERIM_9BIS), ref_9bis["profondeur"], sorted(ref_9bis["exemptes"]), len(ec)))
            if ec:
                L["verdict"], L["branche"] = ("NON CONCLUANT D'INSTRUMENT",
                    "9bis : ecart sur cle du perimetre, prononce AVANT toute lecture de verdict (v11 9bis) -- %s" % ec[0])
            else:
                L["verdict"], L["branche"] = cascade_temoin(L)
        else:
            L["lectures_non_lues"].append("controle 9bis NON JOUE (pas de reference deposee)")
            L["verdict"], L["branche"] = cascade_temoin(L)
    L["comptes"] = dict(compteur); L["attendus"] = attendu; L["attendus_total"] = n_att
    L["W_comptes"], L["verdict"], L["branche"] = verdict_comptes(compteur, n_att, L["verdict"], L["branche"], "BANC NON JOUE")
    JRN("W-comptes", "comptes %d + sautes %d == attendus %d -> %s" % (compteur["comptes"], compteur["sautes"], n_att, L["W_comptes"]))
    JRN("VERDICT", "%s -- %s" % (L["verdict"], L["branche"]))
    return L


def controle_algorithme_contre_moteur(mod):
    """4.6bis (i) : la transcription de chercher_seuil contre l'algorithme
    DEPOSE, appele tel quel sur un integrateur synthetique re-lie (patron
    du pre-vol depose) : memes seuils AU BIT, memes motifs, huit thetas
    (interieur, bornes, un et deux elargissements haut, un bas, sans
    explosion)."""
    thetas = [0.4872, 0.9773, 1.9545, 5.99, 6.0, 7.46, 30.0, 0.03, 1e9]
    n_ok, detail = 0, []
    sauve = mod.integrer
    try:
        for th in thetas:
            def synth(w2, s_arr, sgn=1, dt=None, g=None, th=th):
                return np.asarray(s_arr, float) >= th
            mod.integrer = synth
            s_dep, m_dep = mod._chercher_depose(0.0)
            s_tr, m_tr, info = chercher_seuil_transcrit(synth, 0.0)
            ok = (s_dep == s_tr) and (m_dep == m_tr)
            n_ok += int(ok)
            detail.append({"theta": th, "depose": (s_dep, m_dep), "transcrit": (s_tr, m_tr, info["k"]), "ok": ok})
    finally:
        mod.integrer = sauve
    return {"n": len(thetas), "n_ok": n_ok, "ok": n_ok == len(thetas), "detail": detail}

# =====================================================================
# 9. LA VERIFICATION alpha (gel constante A v4 011c923203fcdaef, base alpha v5 045c2435aaf623ce)
# =====================================================================

def compte_attendu_alpha():
    n_plan = len(DEGRES) * len(W2S) * len(C_PLAN)
    return {"plan": n_plan, "G_dt": n_plan, "G_k": n_plan, "G_seuil": len(DEGRES) * len(W2S),
            "G_lignee": len(DEGRES) * len(W2S) * (len(C_PLAN) + 1)}


def lire_porte_temoin(chemin):
    """PORTE BLOQUANTE (gel alpha 5, D-alpha-7) : le JSON du temoin, verdict
    REGLAGE QUALIFIE, memes (delta, r, M, k, dt_2), empreinte consignee ;
    et les neuf e(dt_2)/ln 10 (LD-5)."""
    if not os.path.isfile(chemin):
        sys.exit("ARRET PORTE : resultats du temoin absents (%s)." % chemin)
    d = json.load(open(chemin, encoding="utf-8"))
    emp = empreinte_B(chemin)
    verdict = d.get("verdict", "")
    if not verdict.startswith("REGLAGE QUALIFIE"):
        sys.exit("ARRET PORTE : le temoin rend '%s', la porte de alpha reste fermee." % verdict)
    reg = d.get("reglage", {})
    att = {"delta": str(DELTA), "r": str(R_CAP), "M": M_PAS, "k": K_BASC, "eta": str(ETA)}
    for cle, v in att.items():
        if str(reg.get(cle)) != str(v):
            sys.exit("ARRET PORTE : reglage du temoin %s=%r, alpha exige %r." % (cle, reg.get(cle), v))
    pts = d.get("T2", {}).get("points", {})
    e_ln10 = {}
    for cle, pt in pts.items():
        p = int(cle.split("|")[0]); w2 = float(cle.split("|")[1])
        if abs(pt["dt2"] - dt2_de(w2)) > 1e-15 * dt2_de(w2):
            sys.exit("ARRET PORTE : dt_2 du temoin (%r) differe de celui de alpha a w2=%.2f." % (pt["dt2"], w2))
        e_ln10.setdefault(p, {})[w2] = pt["e_sur_ln10"]
    if sorted(e_ln10.keys()) != sorted(DEGRES):
        sys.exit("ARRET PORTE : le temoin ne porte pas les trois degres en T-2.")
    JRN("PORTE", "temoin %s (%s) : %s ; reglage %s ; e(dt2)/ln10 par degre max = %s"
        % (os.path.basename(chemin), emp, verdict, reg,
           {p: "%.3e" % max(e_ln10[p].values()) for p in e_ln10}))
    return {"fichier": chemin, "empreinte": emp, "verdict": verdict, "statut": d.get("statut"),
            "e_sur_ln10_max": {p: max(e_ln10[p].values()) for p in e_ln10}}


def trajectoire_plan(w2, p, s, dt2, k, compteur, sortie, etiquette, mod_synth=None, sgn=1, jumelle=False, sans_2a=False):
    """Phase 1 (schema depose, dt_1) jusqu'a la bascule (k), puis phase 2 a
    dt2 jusqu'a CAP_p ; serie ecrite ; ajustements 7.2 ; G-fen consigne."""
    xb = x_bascule_0(p, w2, k)                 # bascule 5.3 du v5, INCHANGEE (v4 4.2)
    ph1 = (mod_synth or phase1_pu)(w2, s, p, "bascule", x_b=xb, sgn=sgn)
    compteur["comptes"] += 1
    rec = {"w2": w2, "p": p, "s": s, "sgn": sgn, "dt2": dt2, "k": k, "x_bascule": xb, "CAP_p": cap_p(p, w2),
           "phase1": {"evenement": ph1["evenement"], "indice": ph1["indice"], "t": ph1["t"],
                      "etat_bascule": ph1["etat"], "tau_bascule_nominal": k * tau_dom(w2),
                      "abs_x_bascule": abs(ph1["etat"][0] + ph1["etat"][1])}}
    if ph1["evenement"] != "BASCULE":
        rec["statut"] = "G-fen (phase 1 : %s)" % ph1["evenement"]
        rec["ajustement"] = {"statut": "G-fen"}
        JRN("A-%s" % etiquette, "phase 1 sans bascule (%s a t=%.3f) -> G-fen, COMPTE" % (ph1["evenement"], ph1["t"]))
        return rec
    fac = 2 if jumelle else 1
    if mod_synth:
        # Synthetique (banc, pre-vol) : la chaine est jouee en UNE phase par
        # la fabrique ; les gardes de compte d'etage sont NON JOUEES ici et
        # le journal le dit (N-62 : rien de synthetique n'est une mesure).
        rec["etages"] = "SYNTHETIQUE (une phase ; gardes de compte NON JOUEES)"
        ph2 = mod_synth.phase2(w2, p, ph1["etat"], ph1["t"], dt2, arret_cap=cap_p(p, w2), sgn=sgn)
    else:
        etat_depart_consigne(rec, "2a", ph1["etat"], ph1["t"])
        dt_2a = dt2a_de(w2) / fac
        if sans_2a:
            ph2a = {"evenement": "SAUTE", "n": 0, "etat_fin": ph1["etat"], "t": np.array([ph1["t"]])}
        else:
            ph2a = phase2_pu(w2, p, ph1["etat"], ph1["t"], dt_2a, arret_cap=x_bascule(p, w2, K_BASC), sgn=sgn)
        lo, hi = intervalle_evenement(n_2a_nominal_k(k), retard_2a(w2), fac)
        rec["etage_2a"] = {"evenement": ph2a["evenement"], "n": int(ph2a["n"]), "dt": dt_2a}
        if not garde_compte("n_2a", ph2a["n"], lo, hi, rec, etiquette):
            return rec
        if ph2a["evenement"] not in ("CAP", "SAUTE"):
            rec["statut"] = "G-fen (etage 2a : %s)" % ph2a["evenement"]
            rec["ajustement"] = {"statut": "G-fen"}
            JRN("A-%s" % etiquette, "etage 2a n'atteint pas la bascule 2b (%s) -> G-fen, COMPTE" % ph2a["evenement"])
            return rec
        t_2b = float(ph2a["t"][-1]) if ph2a["evenement"] != "SAUTE" else ph1["t"]
        etat_depart_consigne(rec, "2b", ph2a["etat_fin"], t_2b)
        ph2 = phase2_pu(w2, p, ph2a["etat_fin"], t_2b, dt2, arret_cap=cap_p(p, w2), sgn=sgn)
        lo_b, hi_b = intervalle_evenement(n_2b_nominal(), RETARD_2B, fac)
        rec["etage_2b"] = {"evenement": ph2["evenement"], "n": int(ph2["n"]), "dt": dt2}
        if not garde_compte("n_2b", ph2["n"], lo_b, hi_b, rec, etiquette):
            return rec
    x = ph2["x1"] + ph2["x2"]
    rec["phase2"] = {"evenement": ph2["evenement"], "n": int(ph2["n"]), "t_dernier": float(ph2["t"][-1]),
                     "abs_x_dernier": float(abs(x[-1]))}
    if sortie is not None:
        lignes = ["# serie phase 2 %s : t x1 x2 (dt2=%.17g, depart t=%.17g etat bascule x1 x2 v1 v2 = %s)"
                  % (etiquette, dt2, ph1["t"], " ".join("%.17g" % v for v in ph1["etat"]))]
        lignes += ["%.17g %.17g %.17g" % (ph2["t"][i], ph2["x1"][i], ph2["x2"][i]) for i in range(len(ph2["t"]))]
        ch = ecrire_ascii(os.path.join(sortie, "alpha_serie_%s.txt" % etiquette), "\n".join(lignes))
        rec["serie_fichier"] = os.path.basename(ch); rec["serie_empreinte"] = empreinte_B(ch)
    if ph2["evenement"] != "CAP":
        rec["statut"] = "G-fen (phase 2 : %s)" % ph2["evenement"]
        rec["ajustement"] = {"statut": "G-fen"}
        JRN("A-%s" % etiquette, "phase 2 n'atteint pas CAP_p (%s) -> G-fen, COMPTE" % ph2["evenement"])
        return rec
    aj = ajuster_point_fixe(ph2["t"], x, w2, p, dt2)
    rec["ajustement"] = aj
    rec["statut"] = aj["statut"]
    if aj["statut"] == "POINT_FIXE":
        gA = G_REF * math.exp(aj["lnA_II"]) ** (p - 2)
        aj["gA_II_sur_K"] = gA / float(K_de(p))
        JRN("A-%s" % etiquette, "bascule pas %d t=%.4f |x|=%.4e ; phase 2 %d pas -> CAP ; point fixe en %d it., %d pts ; alpha=%.6f (4/(p-2)=%.6f) disp_loc=%.3e ; II : gA^(p-2)/K=%.6f t*=%.6f"
            % (ph1["indice"], ph1["t"], rec["phase1"]["abs_x_bascule"], ph2["n"], aj["iterations"], aj["n_points"],
               aj["alpha"], float(alpha_de(p)), aj["disp_locale"], aj["gA_II_sur_K"], aj["t_star_II"]))
    else:
        JRN("A-%s" % etiquette, "ajustement : %s (%s)" % (aj["statut"], {k: v for k, v in aj.items() if k != "journal"}))
    return rec


def trajectoire_seuil(w2, p, s, dt2, compteur, sortie, etiquette, mod_synth=None, sgn=1, jumelle=False, sans_2s=False):
    """G-seuil (LD-10) : phase 1 jusqu'a T_MAX - (tau_dom - tau_CAP), phase 2
    jusqu'a T_MAX, ajustement sur la derniere fenetre, t* libre."""
    td, tc = tau_dom(w2), tau_cap(w2)
    t_fin = depart_2s(w2)                      # v4 4.7 : la borne v5 5.3, en t
    ph1 = (mod_synth or phase1_pu)(w2, s, p, "seuil", x_b=x_bascule_0(p, w2), t_fin=t_fin, sgn=sgn)
    compteur["comptes"] += 1
    rec = {"w2": w2, "p": p, "s": s, "sgn": sgn, "dt2": dt2, "t_fin_phase1": t_fin,
           "phase1": {"evenement": ph1["evenement"], "indice": ph1["indice"], "t": ph1["t"],
                      "bascule_sous_seuil_indice": ph1["bascule_sous_seuil_indice"]}}
    if ph1["evenement"] != "T_FIN":
        rec["statut"] = "phase 1 : %s" % ph1["evenement"]
        rec["ajustement"] = {"statut": "G-fen"}
        JRN("S-%s" % etiquette, "phase 1 sous seuil interrompue (%s) -> G-fen, COMPTE" % ph1["evenement"])
        return rec
    fac = 2 if jumelle else 1
    if mod_synth:
        rec["etages"] = "SYNTHETIQUE (une phase ; gardes de compte NON JOUEES)"
        ph2 = mod_synth.phase2(w2, p, ph1["etat"], ph1["t"], dt2, t_max=T_MAX_DEPOSE, sgn=sgn)
    else:
        # v4 4.7 : t_start est LU du journal de phase 1 (l'etat et son t tels
        # que la phase 1 les rend), JAMAIS recalcule (R-A-5).
        t_start = ph1["t"]
        etat_depart_consigne(rec, "2s", ph1["etat"], t_start)
        d2b = depart_2bp(w2)
        dt_2a = dt2a_de(w2) / fac
        if sans_2s:
            ph2s = {"evenement": "SAUTE", "n": 0, "etat_fin": ph1["etat"], "t": np.array([t_start])}
            t_2b = t_start
        else:
            n_2s = int(math.ceil((d2b - t_start) / dt_2a))
            dt_2s = (d2b - t_start) / n_2s      # atterrit EXACTEMENT sur depart_2b'
            ph2s = phase2_pu(w2, p, ph1["etat"], t_start, dt_2s, t_max=d2b, sgn=sgn)
            lo, hi = intervalle_2s(w2, fac)
            rec["etage_2s"] = {"evenement": ph2s["evenement"], "n": int(ph2s["n"]), "dt": dt_2s, "n_2s_derive": n_2s}
            if not garde_compte("n_2s", ph2s["n"], lo, hi, rec, etiquette):
                return rec
            t_2b = float(ph2s["t"][-1])
        etat_depart_consigne(rec, "2b'", ph2s["etat_fin"], t_2b)
        dt_2bp = (T_MAX_DEPOSE - t_2b) / (N_2BP * fac) if not sans_2s else dt2
        ph2 = phase2_pu(w2, p, ph2s["etat_fin"], t_2b, dt_2bp, t_max=T_MAX_DEPOSE, sgn=sgn)
        if not sans_2s:
            rec["etage_2bp"] = {"evenement": ph2["evenement"], "n": int(ph2["n"]), "dt": dt_2bp}
            if not garde_compte("n_2b'", ph2["n"], N_2BP * fac, N_2BP * fac, rec, etiquette):
                return rec
            dt2 = dt_2bp                        # la fenetre se lit au pas de 2b'
    x = ph2["x1"] + ph2["x2"]
    if sortie is not None:
        lignes = ["# serie phase 2 sous seuil %s : t x1 x2 (dt2=%.17g)" % (etiquette, dt2)]
        lignes += ["%.17g %.17g %.17g" % (ph2["t"][i], ph2["x1"][i], ph2["x2"][i]) for i in range(len(ph2["t"]))]
        ch = ecrire_ascii(os.path.join(sortie, "alpha_serie_%s.txt" % etiquette), "\n".join(lignes))
        rec["serie_fichier"] = os.path.basename(ch); rec["serie_empreinte"] = empreinte_B(ch)
    rec["phase2"] = {"evenement": ph2["evenement"], "n": int(ph2["n"]), "abs_x_max": float(np.max(np.abs(x)))}
    aj = ajuster_derniere_fenetre(ph2["t"], x, w2, p, dt2, T_MAX_DEPOSE)
    rec["ajustement"] = aj; rec["statut"] = aj["statut"]
    if aj["statut"] == "AJUSTE":
        gA = G_REF * math.exp(aj["lnA_II"]) ** (p - 2)
        aj["gA_II_sur_K"] = gA / float(K_de(p))
        JRN("S-%s" % etiquette, "sous seuil (s=%.6f) : |x|max phase 2 %.4e ; ajustement libre alpha=%.4f t*=%.4f (T_MAX=%g) disp_loc=%.3e ; II gA^(p-2)/K=%.3e"
            % (s, rec["phase2"]["abs_x_max"], aj["alpha"], aj["t_star"], T_MAX_DEPOSE, aj["disp_locale"], aj["gA_II_sur_K"]))
        if ph1["bascule_sous_seuil_indice"] is not None:
            JRN("S-%s" % etiquette, "BASCULE SOUS SEUIL vue au pas %d (consignee)" % ph1["bascule_sous_seuil_indice"])
    else:
        JRN("S-%s" % etiquette, "ajustement : %s" % aj["statut"])
    return rec


def lignee_point(mod, w2, p, s, compteur, etiquette, attendu, phase1=None, sgn=1):
    """G-lignee (5.6, LD-13, LD-14) : phase 1 sans bascule au test depose,
    contre le moteur APPELE TEL QUEL, au signe du point (4.4 v5) ;
    booleen puis indice (T_MAX re-lie)."""
    ph = (phase1 or phase1_pu)(w2, s, p, "lignee", sgn=sgn)
    compteur["comptes"] += 1
    mien = (ph["evenement"] == "EXPLOSION")
    b_mot = moteur_explose(mod, w2, s, p, sgn=sgn)
    rec = {"w2": w2, "p": p, "s": s, "sgn": sgn, "attendu_explose": attendu, "instrument_explose": mien,
           "moteur_explose": b_mot, "indice_instrument": ph["indice"] if mien else None,
           "booleen_identique": mien == b_mot, "attendu_respecte": b_mot == attendu}
    if mien and b_mot:
        n = ph["indice"]
        rec["moteur_explose_a_n"] = moteur_explose(mod, w2, s, p, sgn=sgn, n_pas=n)
        rec["moteur_explose_a_n_moins_1"] = moteur_explose(mod, w2, s, p, sgn=sgn, n_pas=n - 1)
        rec["indice_identique"] = rec["moteur_explose_a_n"] and not rec["moteur_explose_a_n_moins_1"]
    else:
        rec["indice_identique"] = None
    rec["ok"] = rec["booleen_identique"] and (rec["indice_identique"] in (True, None))
    JRN("L-%s" % etiquette, "s=%.6f sgn=%+d attendu %s : instrument %s (pas %s), moteur %s ; indice identique %s -> %s"
        % (s, sgn, "EXPLOSE" if attendu else "SANS", mien, rec["indice_instrument"], b_mot, rec["indice_identique"],
           "OK" if rec["ok"] else "ECART"))
    return rec


def cascade_alpha(L):
    """9, branches 0..7 ; plafond 10.2 dans la famille de la branche 2."""
    lig = L["G_lignee"]
    prefixe = "" if lig["n_ok"] == lig["n"] else "LIEN NON ETABLI (%d/%d) -- " % (lig["n_ok"], lig["n"])
    if any(r["G_seuil_mord"] for r in L["seuil"].values()):
        return prefixe + "INSTRUMENT REFUTE", "branche 1 : G-seuil MORD (exposant convergent sous le seuil)"
    deg = L["degres"]
    if any(not deg[p]["resolution_ok"] for p in deg):
        qui = []
        for p in deg:
            if deg[p]["G_dt_mord"]:
                qui.append("G-dt p=%d" % p)
            if deg[p]["G_k_mord"]:
                qui.append("G-k p=%d" % p)
            if deg[p].get("conversion_5_3_iv") is False:
                qui.append("conversion 5.3(iv) p=%d" % p)
            if deg[p].get("tol") is not None and deg[p]["tol"] > float(PLAFOND_ALPHA):
                qui.append("plafond 10.2 p=%d" % p)
        return prefixe + "NON CONCLUANT DE RESOLUTION", "branche 2 : %s MORD" % ", ".join(qui)
    if any(not deg[p]["exploitable"] for p in deg):
        return prefixe + "NON CONCLUANT DE FENETRE", "branche 3 : G-fen ou pas de point fixe (degres exploitables %s)" % [p for p in deg if deg[p]["exploitable"]]
    if any(deg[p].get("G_plancher_mord") for p in deg):
        qui = [p for p in deg if deg[p].get("G_plancher_mord")]
        return prefixe + "NON CONCLUANT DE PLANCHER", "branche 3b : G-plancher MORD aux degres %s (tol_lnA <= plancher : le modele fixe encore la tolerance ; v4 7)" % qui
    if any(deg[p]["G_s_mord"] or deg[p]["G_w2_mord"] for p in deg):
        qui = ["G-s p=%d" % p for p in deg if deg[p]["G_s_mord"]] + ["G-w2 p=%d" % p for p in deg if deg[p]["G_w2_mord"]]
        return prefixe + "REFUTE", "branche 4 : %s MORD (alpha depend de s ou de w2)" % ", ".join(qui)
    if all(deg[p]["P_alpha"] for p in deg) and all(deg[p]["P_A"] for p in deg):
        return prefixe + "VERIFIE", "branche 5 : P-alpha les six par degre ET P-A aux trois degres"
    if all(deg[p]["P_alpha"] for p in deg):
        return prefixe + "PARTIEL", "branche 6 : P-alpha aux trois degres, P-A non"
    return prefixe + "REFUTE", "branche 7 : P-alpha echoue a un degre au moins"


def lire_alpha(plan, gdt, gk, seuil, lignee, e_ln10_max, ref_desc=None):
    """Les gardes et predictions, PURES sur les enregistrements (le banc
    nourrit des synthetiques). Rend L pret pour cascade_alpha."""
    L = {"plan": plan, "G_dt": gdt, "G_k": gk, "seuil": {}, "degres": {}, "lectures_non_lues": [],
         "G_lignee": {"n": len(lignee), "n_ok": sum(1 for r in lignee.values() if r["ok"])}}

    def alpha_de_rec(rec):
        aj = rec.get("ajustement", {})
        return aj.get("alpha") if aj.get("statut") == "POINT_FIXE" else None
    for p in DEGRES:
        D = {"tol_composantes": {}, "exploitable": True}
        ecarts_dt, ecarts_k, disps, tol_lnA_pts = [], [], [], []
        alphas = {}
        for w2 in W2S:
            for c in C_PLAN:
                cle = "%d|%.2f|%.2f" % (p, w2, c)
                a0, a1, a2 = alpha_de_rec(plan[cle]), alpha_de_rec(gdt[cle]), alpha_de_rec(gk[cle])
                if None in (a0, a1, a2):
                    D["exploitable"] = False
                    continue
                alphas[(w2, c)] = a0
                ecarts_dt.append(abs(a0 - a1)); ecarts_k.append(abs(a0 - a2))
                disps.append(plan[cle]["ajustement"]["disp_locale"])
                lnA = [r["ajustement"]["lnA_II"] for r in (plan[cle], gdt[cle], gk[cle])]
                tol_lnA_pts.append(max(lnA) - min(lnA))
        if D["exploitable"]:
            D["tol_composantes"] = {"G_dt_max": max(ecarts_dt), "G_k_max": max(ecarts_k), "disp_locale_max": max(disps)}
            tol = max(ecarts_dt + ecarts_k + disps)
            D["tol"] = tol
            D["tol_sur_8_15"] = tol / (8.0 / 15.0)
            D["plafond"] = float(PLAFOND_ALPHA)
            D["G_dt_mord"] = max(ecarts_dt) > float(PLAFOND_ALPHA)          # 10.1bis (v5) : au plafond
            D["G_k_mord"] = max(ecarts_k) > float(PLAFOND_ALPHA)
            D["ecart_G_dt_sur_8_15"] = max(ecarts_dt) / (8.0 / 15.0)
            D["ecart_G_k_sur_8_15"] = max(ecarts_k) / (8.0 / 15.0)
            e_req = e_ln10_max.get(p, 0.0)
            D["e_temoin_sur_ln10"] = e_req
            D["conversion_5_3_iv"] = tol >= e_req
            D["resolution_ok"] = (tol <= float(PLAFOND_ALPHA)) and not D["G_dt_mord"] and not D["G_k_mord"] and D["conversion_5_3_iv"]
            ap = float(alpha_de(p))
            D["alphas"] = {"%.2f|%.2f" % k: v for k, v in alphas.items()}
            D["P_alpha"] = all(abs(v - ap) <= tol for v in alphas.values())
            D["G_s_mord"] = any(abs(alphas[(w2, C_PLAN[0])] - alphas[(w2, C_PLAN[1])]) > tol for w2 in W2S)
            D["G_w2_mord"] = any(max(alphas[(w2, c)] for w2 in W2S) - min(alphas[(w2, c)] for w2 in W2S) > tol for c in C_PLAN)
            D["dispersion_lnA"] = max(tol_lnA_pts)
            D["plancher_lnA"] = float(plancher_lnA(p))
            D["tol_lnA"] = max(D["dispersion_lnA"], D["plancher_lnA"])        # 10.3 (v5)
            D["tol_lnA_sur_plancher"] = D["tol_lnA"] / D["plancher_lnA"]
            # v4 7, branche 3b : comparaison de bord EXACTE par propagation
            # du double (max() rend l'objet ; regle 15, ecrite au gel).
            D["G_plancher_mord"] = D["tol_lnA"] <= D["plancher_lnA"]
            ratios = {}
            for w2 in W2S:
                for c in C_PLAN:
                    cle = "%d|%.2f|%.2f" % (p, w2, c)
                    ratios[cle] = plan[cle]["ajustement"]["gA_II_sur_K"]
            D["gA_sur_K"] = ratios
            D["P_A"] = all(abs(math.log(v)) <= (p - 2) * D["tol_lnA"] for v in ratios.values())
            if ref_desc and str(p) in ref_desc:
                # v4 9, L-desc : R = ln(gA'/K) / ln(gA_85/K), cellule du plan
                # des deux cotes ; CONSIGNEE, aucune branche. Portee : refute
                # R ~ 1, ne peut pas confirmer 1/1024 (v4 9).
                D["L_desc"] = {cle: math.log(ratios[cle]) / math.log(ref_desc[str(p)][cle])
                               for cle in ratios if cle in ref_desc[str(p)] and ref_desc[str(p)][cle] > 0}
                D["L_desc_portee"] = "un seul sens (v4 9) : refute R~1, ne confirme pas 1/441"
            elif ref_desc is not None:
                L["lectures_non_lues"].append("L-desc p=%d NON LUE (degre absent de la reference)" % p)
        else:
            D.update({"tol": None, "resolution_ok": True, "G_dt_mord": False, "G_k_mord": False, "P_alpha": False,
                      "P_A": False, "G_s_mord": False, "G_w2_mord": False, "tol_lnA": None, "G_plancher_mord": False})
            for nom in ("P-alpha", "P-A", "G-dt", "G-k", "G-s", "G-w2", "conversion 5.3(iv)"):
                L["lectures_non_lues"].append("%s p=%d NON LU (degre non exploitable)" % (nom, p))
        L["degres"][p] = D
    for cle, rec in seuil.items():
        p = rec["p"]; D = L["degres"][p]
        aj = rec.get("ajustement", {})
        S = {"statut": aj.get("statut"), "G_seuil_mord": False}
        if not (aj.get("statut") == "AJUSTE" and D.get("tol") is not None):
            L["lectures_non_lues"].append("G-seuil %s NON LU (%s)" % (cle, aj.get("statut") if aj.get("statut") != "AJUSTE" else "tolerance du degre non lue"))
        if aj.get("statut") == "AJUSTE" and D.get("tol") is not None:
            S["i_dispersion"] = aj["disp_locale"] <= D["tol"]
            S["ii_t_star_fini"] = T_MAX_DEPOSE <= aj["t_star"] <= T_MAX_DEPOSE + tau_dom(rec["w2"])
            S["iii_A"] = abs(math.log(aj["gA_II_sur_K"])) <= (p - 2) * D["tol_lnA"] if aj["gA_II_sur_K"] > 0 else False
            S["G_seuil_mord"] = S["i_dispersion"] and S["ii_t_star_fini"] and S["iii_A"]
        L["seuil"][cle] = S
    return L


def executer_alpha(registre, sortie, mod, porte, prevol=None):
    compteur = {"comptes": 0, "sautes": 0, "sautes_noms": []}
    attendu = compte_attendu_alpha(); n_att = sum(attendu.values())
    JRN("COMPTE", "attendus (forme derivee) : %s = %d" % (attendu, n_att))
    s_etoile, carte = lire_carte(registre)
    ok_carte, ecarts = controle_carte(s_etoile)
    JRN("CARTE", "neuf s* lus (sF) ; regle 11 contre la table 4.2 : ecart max %.1e -> %s"
        % (max(ecarts.values()), "CONCORDANT" if ok_carte else "DISCORDANT"))
    if not ok_carte:
        sys.exit("ARRET regle 11 : les s* lus ne sont pas ceux du gel.")
    signes = lire_signes(registre)
    JRN("CARTE", "signes joues (4.4 v5, sgn = frag, +1 sans second seuil) : %s"
        % {"%d|%.2f" % k: "%+d (asym %s)" % (v["sgn"], ("%.4f" % v["asym"]) if v["asym"] is not None else "--") for k, v in signes.items()})
    L = {"mode": "alpha", "prevol": bool(prevol), "porte": porte, "s_etoile": {"%d|%.2f" % k: v for k, v in s_etoile.items()},
         "signes": {"%d|%.2f" % k: v for k, v in signes.items()},
         "declaration_parite": "p = 4 : sgn = +1 et -1 en est l'image (parite M11) ; p = 5, 7 : chaque point au signe frag de son seuil (4.4 v5)"}
    synth = prevol["synth"] if prevol else None
    plan, gdt, gk, seuil, lignee = {}, {}, {}, {}, {}
    for p in DEGRES:
        for w2 in W2S:
            dt2 = dt2_de(w2)
            sg = signes[(p, w2)]["sgn"]
            for c in C_PLAN:
                s = c * s_etoile[(p, w2)]
                cle = "%d|%.2f|%.2f" % (p, w2, c)
                plan[cle] = trajectoire_plan(w2, p, s, dt2, K_BASC, compteur, sortie, "p%d_w%.2f_c%.2f_dt2_k2" % (p, w2, c), synth, sgn=sg)
                gdt[cle] = trajectoire_plan(w2, p, s, dt2 / 2, K_BASC, compteur, sortie, "p%d_w%.2f_c%.2f_dt2s2_k2" % (p, w2, c), synth, sgn=sg)
                gk[cle] = trajectoire_plan(w2, p, s, dt2, K_GARDE, compteur, sortie, "p%d_w%.2f_c%.2f_dt2_k4" % (p, w2, c), synth, sgn=sg)
            cle = "%d|%.2f" % (p, w2)
            seuil[cle] = trajectoire_seuil(w2, p, C_SEUIL * s_etoile[(p, w2)], dt2, compteur, sortie, "p%d_w%.2f_c0.95_seuil" % (p, w2), synth, sgn=sg)
    for p in DEGRES:
        for w2 in W2S:
            sg = signes[(p, w2)]["sgn"]
            for c in (C_SEUIL,) + C_PLAN:
                cle = "%d|%.2f|%.2f" % (p, w2, c)
                lignee[cle] = lignee_point(mod, w2, p, c * s_etoile[(p, w2)], compteur, "p%d_w%.2f_c%.2f" % (p, w2, c),
                                           attendu=(c > 1.0), phase1=(synth.phase1_lignee if synth else None), sgn=sg)
    ref_desc = None
    ch_ref = os.path.join(registre, "runs", "run_alpha_delta85", "resultats_alpha.json")
    if os.path.isfile(ch_ref):
        if empreinte_B(ch_ref) == "6d7d23130e9322f8":
            dref = json.load(open(ch_ref, encoding="utf-8"))
            ref_desc = {p: dref["degres"][p]["gA_sur_K"] for p in dref.get("degres", {})}
            JRN("L-desc", "reference du 85 lue (6d7d23130e9322f8) : dix-huit denominateurs, cellule du plan")
        else:
            JRN("L-desc", "reference presente mais DISCORDANTE (%s) : L-desc NON LUE" % empreinte_B(ch_ref))
    else:
        JRN("L-desc", "reference du 85 absente du registre : L-desc NON LUE")
    L.update(lire_alpha(plan, gdt, gk, seuil, lignee, porte["e_sur_ln10_max"], ref_desc=ref_desc))
    if ref_desc is None:
        L["lectures_non_lues"] = L.get("lectures_non_lues", []) + ["L-desc NON LUE (reference du 85 absente ou discordante)"]
    L["seuil_trajectoires"] = seuil
    L["G_lignee_points"] = lignee
    for p in DEGRES:
        D = L["degres"][p]
        JRN("DEGRE-p%d" % p, "exploitable %s ; tol=%s tol/(8/15)=%s (plafond 2/15) ; G-dt %s (ecart/(8/15)=%s) G-k %s (%s) ; conversion 5.3(iv) %s ; P-alpha %s ; G-s %s G-w2 %s ; dispersion_lnA=%s plancher_lnA=%s tol_lnA=%s (tol/plancher=%s) P-A %s"
            % (D["exploitable"], D.get("tol"), D.get("tol_sur_8_15"), D["G_dt_mord"], D.get("ecart_G_dt_sur_8_15"), D["G_k_mord"],
               D.get("ecart_G_k_sur_8_15"), D.get("conversion_5_3_iv"), D["P_alpha"], D["G_s_mord"], D["G_w2_mord"],
               D.get("dispersion_lnA"), D.get("plancher_lnA"), D.get("tol_lnA"), D.get("tol_lnA_sur_plancher"), D["P_A"]))
    n_att_gel = sum(1 for r in lignee.values() if r["attendu_respecte"])
    L["G_lignee"]["attendu_gel_respecte"] = n_att_gel
    JRN("G-lignee", "booleens identiques au moteur (le lien) %d/%d ; attendu du gel 5.6 (explose ssi c > 1) respecte %d/%d"
        % (L["G_lignee"]["n_ok"], L["G_lignee"]["n"], n_att_gel, L["G_lignee"]["n"]))
    for cle, S in L["seuil"].items():
        JRN("G-seuil", "%s : %s -> %s" % (cle, {k: v for k, v in S.items() if k != "G_seuil_mord"}, "MORD" if S["G_seuil_mord"] else "muette"))
    L["verdict"], L["branche"] = cascade_alpha(L)
    L["comptes"] = dict(compteur); L["attendus"] = attendu; L["attendus_total"] = n_att
    L["G_comptes"], L["verdict"], L["branche"] = verdict_comptes(compteur, n_att, L["verdict"], L["branche"], "MANCHE NON JOUEE")
    JRN("G-comptes", "comptes %d + sautes %d == attendus %d -> %s" % (compteur["comptes"], compteur["sautes"], n_att, L["G_comptes"]))
    JRN("VERDICT", "%s -- %s" % (L["verdict"], L["branche"]))
    return L

# =====================================================================
# 10. SELFTEST -- ce que l'instrument CALCULE
# =====================================================================

TABLES_GEL_ALPHA = {   # gel constante A v6, 4.3 (tau_dom', dt_2b), 4.4 (bascule 2b), 4.5 (CAP') -- re-derivees au reglage v6
    "tau_dom": {1.73: "2.3831e-03", 2.27: "1.9197e-03", 2.80: "1.6016e-03"},
    "dt2": {1.73: "1.1915e-05", 2.27: "9.5987e-06", 2.80: "8.0080e-06"},
    "dt2a": {1.73: "2.3831e-04", 2.27: "1.9197e-04", 2.80: "1.6016e-04"},
    "CAP": {(4, 1.73): "8.6265e+08", (4, 2.27): "1.3293e+09", (4, 2.80): "1.9098e+09",
            (5, 1.73): "6.5318e+05", (5, 2.27): "8.7142e+05", (5, 2.80): "1.1095e+06",
            (7, 1.73): "2.4863e+03", (7, 2.27): "2.9558e+03", (7, 2.80): "3.4168e+03"},
    "bascule": {(4, 1.73): "2.1566e+06", (4, 2.27): "3.3233e+06", (4, 2.80): "4.7746e+06",
                (5, 1.73): "1.2032e+04", (5, 2.27): "1.6052e+04", (5, 2.80): "2.0438e+04",
                (7, 1.73): "2.2633e+02", (7, 2.27): "2.6906e+02", (7, 2.80): "3.1103e+02"},
    "A": {4: "48.98979", 5: "9.65048", 7: "3.14244"},
}
TABLES_GEL_ALPHA_0 = {   # REPERE delta_0 (gel alpha v5, 5.3 et 6) : bascule 5.3 = depart de 2a
    "tau_dom_0": {1.73: "5.0044e-02", 2.27: "4.0314e-02", 2.80: "3.3634e-02"},
    "bascule_0": {(4, 1.73): "4.8903e+03", (4, 2.27): "7.5357e+03", (4, 2.80): "1.0827e+04",
                  (5, 1.73): "2.0767e+02", (5, 2.27): "2.7705e+02", (5, 2.80): "3.5276e+02",
                  (7, 1.73): "1.9813e+01", (7, 2.27): "2.3555e+01", (7, 2.80): "2.7229e+01"},
}
COMPTES_MOTIFS_GEL = {   # gel temoin 4.6bis (iii), comptes exacts sur les cartes deposees
    "runs/m10_results.json": {"6.03e-07": 64}, "runs/m11_results.json": {"6.03e-07": 26, "1.82e-06": 6},
    "runs/m12_results.json": {"6.03e-07": 70, "1.82e-06": 4}, "runs/m14_results.json": {"6.03e-07": 37, "1.82e-06": 1},
    "runs/m15_results.json": {"6.03e-07": 28, "1.82e-06": 8},
}


def serie_ansatz(p, w2, dt, t_star, alpha_s=None, A_s=None, bruit=0.0, graine=1):
    """Serie synthetique x = A (t* - t)^(-alpha) sur [t* - 2 tau_dom, t* - tau_CAP]."""
    a = float(alpha_de(p)) if alpha_s is None else alpha_s
    A = A_de(p) if A_s is None else A_s
    td, tc = tau_dom(w2), tau_cap(w2)
    n = int(math.ceil((2 * td - tc) / dt))
    t = t_star - 2 * td + dt * np.arange(n + 1)
    t = t[t_star - t >= tc * (1 - 1e-12)]
    x = A * (t_star - t) ** (-a)
    if bruit:
        rng = np.random.default_rng(graine)
        x = x * (1 + bruit * rng.standard_normal(len(x)))
    return t, x


def selftest(registre, mod):
    T = []

    def test(nom, ok, detail=""):
        T.append((nom, bool(ok)))
        JRN("SELFTEST", "%-52s %s %s" % (nom, "OK " if ok else "KO ", detail))
    sym = controles_symboliques()
    for k, v in sym.items():
        test("symbolique " + k, v)
    test("delta' = 1/44100 et delta_0 = b^J delta' = 1/100 (EXACT, v6 3)",
         DELTA == Fraction(1, 44100) and DELTA_0 == Fraction(1, 100) and DELTA_0 == DELTA * B_DESC ** J_DESC)
    for p, att in ((4, Fraction(1, 882000)), (5, Fraction(1, 637000)), (7, Fraction(1, 469224))):
        test("plancher'(%d) = %s exact (v6 3.3)" % (p, att), plancher_lnA(p) == att, str(plancher_lnA(p)))
    test("n_2b' = M k / r = 400 ; fenetre = 180 ; nominaux 400 / 380 (derives, v6 4.6-4.7)",
         N_2BP == 400 and N_FENETRE == 180 and n_2a_nominal() == 400 and n_2b_nominal() == 380)
    test("intervalles 4.6 : n_2a [374,401]/[368,401]/[362,401] ; n_2b [360,381] (derives, entiers)",
         [intervalle_evenement(n_2a_nominal(), retard_2a(w)) for w in W2S]
         == [(374, 401), (368, 401), (362, 401)]
         and intervalle_evenement(n_2b_nominal(), RETARD_2B) == (360, 381)
         and n_2a_nominal_k(K_GARDE) == 820)
    test("intervalles 4.7 : n_2s [400,426]/[400,432]/[400,438] ; jumelle 4.8 : bornes x2",
         [intervalle_2s(w) for w in W2S] == [(400, 426), (400, 432), (400, 438)]
         and [intervalle_2s(w, 2) for w in W2S] == [(800, 852), (800, 864), (800, 876)]
         and intervalle_evenement(n_2a_nominal(), retard_2a(1.73), 2) == (748, 802)
         and intervalle_evenement(n_2b_nominal(), RETARD_2B, 2) == (720, 762))
    for w2 in W2S:
        test("tau_dom'(%.2f) = %s (v6 4.3)" % (w2, TABLES_GEL_ALPHA["tau_dom"][w2]), "%.4e" % tau_dom(w2) == TABLES_GEL_ALPHA["tau_dom"][w2])
        test("dt_2b(%.2f) = %s (v6 4.3)" % (w2, TABLES_GEL_ALPHA["dt2"][w2]), "%.4e" % dt2_de(w2) == TABLES_GEL_ALPHA["dt2"][w2])
        test("dt_2a(%.2f) = %s (v6 4.3)" % (w2, TABLES_GEL_ALPHA["dt2a"][w2]), "%.4e" % dt2a_de(w2) == TABLES_GEL_ALPHA["dt2a"][w2])
        test("tau_dom_0(%.2f) = %s (repere, v5 6)" % (w2, TABLES_GEL_ALPHA_0["tau_dom_0"][w2]), "%.4e" % tau_dom_0(w2) == TABLES_GEL_ALPHA_0["tau_dom_0"][w2])
    for p in DEGRES:
        test("A_%d = %s" % (p, TABLES_GEL_ALPHA["A"][p]), "%.5f" % A_de(p) == TABLES_GEL_ALPHA["A"][p] or "%.6g" % A_de(p) == TABLES_GEL_ALPHA["A"][p])
        for w2 in W2S:
            test("CAP'_%d(%.2f) = %s (v6 4.5)" % (p, w2, TABLES_GEL_ALPHA["CAP"][(p, w2)]), "%.4e" % cap_p(p, w2) == TABLES_GEL_ALPHA["CAP"][(p, w2)])
            test("bascule2b_%d(%.2f) = %s (v6 4.4)" % (p, w2, TABLES_GEL_ALPHA["bascule"][(p, w2)]), "%.4e" % x_bascule(p, w2) == TABLES_GEL_ALPHA["bascule"][(p, w2)])
            test("bascule0_%d(%.2f) = %s (v5 5.3, depart 2a)" % (p, w2, TABLES_GEL_ALPHA_0["bascule_0"][(p, w2)]), "%.4e" % x_bascule_0(p, w2) == TABLES_GEL_ALPHA_0["bascule_0"][(p, w2)])
    ref9 = {"T1": {"A": {"x": 1.0, "duree_s": 3.0}}, "T1b": {"k": [0, 0]}, "T3a": {"A": "PASSE"}, "T3b": {"n": 3},
            "meta": {"date_utc": "X"}, "reglage": {"delta": "1/44100"}}
    autre = json.loads(json.dumps(ref9)); autre["T1"]["A"]["x"] = 2.0; autre["T1"]["A"]["duree_s"] = 9.0
    autre["meta"]["date_utc"] = "Y"
    ec1 = controle_9bis(autre, ref9, 3, {"duree_s"})
    ec2 = controle_9bis(json.loads(json.dumps(ref9)), ref9, 3, {"duree_s"})
    test("9bis : mord au perimetre (x), muet sur exempte (duree_s) et hors perimetre (meta)",
         len(ec1) == 1 and "/T1/A/x" in ec1[0] and ec2 == [], str(ec1))
    test("L-desc : ln(r')/ln(r) = 1/1024 sur un couple fabrique",
         abs(math.log(math.exp(2e-4 / 1024)) / math.log(math.exp(2e-4)) - 1.0 / 1024) < 1e-12)
    S58 = lire_signes(registre); se58, _ = lire_carte(registre)
    t58 = {(p, "%.2f" % w2, S58[(p, w2)]["sgn"]): se58[(p, w2)] for p in DEGRES for w2 in W2S}
    test("D-M17-58 : la table conforme PASSE la garde (0 faute)", garde_signe_factice(t58, se58, S58) == [])
    for p, att in ((4, Fraction(1, 882000)), (5, Fraction(1, 637000)), (7, Fraction(1, 469224))):
        test("plancher_lnA(%d) = %s exact (v6 3.3, delta')" % (p, att), plancher_lnA(p) == att, str(plancher_lnA(p)))
    S = lire_signes(registre)
    test("carte : sF == min(sP, sM) et frag coherent, 9/9 ; p=4 sans sM", len(S) == 9 and all(S[(4, w)]["sM"] is None and S[(4, w)]["sgn"] == 1 for w in W2S))
    test("signes joues : frag = -1 aux points enumeres de la carte", sorted(k for k, v in S.items() if v["sgn"] == -1) == [(5, 2.27), (5, 2.80), (7, 2.27), (7, 2.80)],
         str(sorted(k for k, v in S.items() if v["sgn"] == -1)))
    b_B = math.sqrt(DS_W * DS_W + 3 * DS_LAM * 4.0) * DT1
    test("tol_int (etat B, x_max=2) = log2((1+b)/(1+b/2)), b = sqrt(13) dt, sous le plafond 1/4",
         abs(math.log2((1 + b_B) / (1 + b_B / 2)) - 0.0154) < 5e-4 and math.log2((1 + b_B) / (1 + b_B / 2)) < PLAFOND_INT, "%.5f" % math.log2((1 + b_B) / (1 + b_B / 2)))
    for k, att in ((0, "6.0325e-07"), (1, "1.8250e-06"), (-1, "3.8020e-09")):
        pas, den, enc = pas_signature(k)
        test("pas_signature(k=%d) = %s, den 9863185" % (k, att), "%.4e" % pas == att and den == 9863185, "%.4e enc=%s" % (pas, enc))
    import re
    for f, att in COMPTES_MOTIFS_GEL.items():
        ch = os.path.join(registre, f)
        if os.path.isfile(ch):
            txt = open(ch, encoding="utf-8").read()
            c = {}
            for m in re.findall(r"OK\|pas=([0-9.]+e-[0-9]+)", txt):
                c[m] = c.get(m, 0) + 1
            test("comptes des motifs %s = %s" % (f, att), c == att, str(c))
        else:
            test("comptes des motifs %s (piece absente)" % f, False)
    rng = np.random.default_rng(7)
    for w2 in W2S:
        e = rng.standard_normal(4) * 100
        back = depuis_composantes(*vers_composantes(*e, w2), w2)
        test("application d'etat, aller-retour w2=%.2f" % w2, max(abs(a - b) for a, b in zip(e, back)) < 1e-10)
    for p in DEGRES:
        w2 = 2.27; dt = dt2_de(w2)
        t, x = serie_ansatz(p, w2, dt, t_star=3.0)
        aj = ajuster_point_fixe(t, x, w2, p, dt)
        ok = aj["statut"] == "POINT_FIXE" and abs(aj["alpha"] - float(alpha_de(p))) < 1e-6 and \
            abs(G_REF * math.exp(aj["lnA_II"]) ** (p - 2) / float(K_de(p)) - 1) < 1e-6 and abs(aj["t_star"] - 3.0) < 1e-6
        test("ajustements I/II retrouvent alpha, A, t* sur l'ansatz p=%d" % p, ok,
             "%s alpha=%.8f t*=%.8f" % (aj["statut"], aj.get("alpha", float("nan")), aj.get("t_star", float("nan"))))
    alg = controle_algorithme_contre_moteur(mod)
    test("chercher_seuil transcrit == depose (9 thetas, au bit, motifs)", alg["ok"], "%d/%d" % (alg["n_ok"], alg["n"]))
    Om2, m = 2.0, 0.25
    test("Duffing standard : cn(0)=1, x0(formule)=1.000000000000", abs(cn_jacobi(0.0, m) - 1) < 1e-15 and "%.12f" % math.sqrt(2 * m * Om2) == "1.000000000000")
    ph_a = phase2_pu(2.27, 5, (1.0, 0.0, 0.0, 0.0), 0.0, 0.05, g=0.0, t_max=2.0)
    ph_b = phase2_pu(2.27, 5, (1.0, 0.0, 0.0, 0.0), 0.0, 0.025, g=0.0, t_max=2.0)
    ea = float(np.max(np.abs(ph_a["x1"] - np.cos(ph_a["t"])))); eb = float(np.max(np.abs(ph_b["x1"] - np.cos(ph_b["t"]))))
    test("pas_rk4 d'ordre 4 sur l'oscillateur harmonique", abs(math.log2(ea / eb) - 4) < 0.1, "p_obs=%.3f" % math.log2(ea / eb))
    for p in DEGRES:
        test("tol_ordre(alpha_%d) sous le plafond 1/4" % p, tol_ordre(alpha_de(p)) < PLAFOND_ORDRE, "%.4f" % tol_ordre(alpha_de(p)))
    try:
        ecrire_ascii(os.path.join("/tmp" if os.name != "nt" else os.environ.get("TEMP", "."), "banc_test_ascii.txt"), "caf\xe9")
        test("ecrire_ascii refuse un octet >= 128", False)
    except UnicodeEncodeError:
        test("ecrire_ascii refuse un octet >= 128", True)
    s_etoile, _ = lire_carte(registre)
    okc, ec = controle_carte(s_etoile)
    test("carte : neuf s* concordent avec la table 4.2 (regle 11)", okc, "ecart max %.1e" % max(ec.values()))
    compteur = {"comptes": 0, "sautes": 0}
    p, w2 = 4, 1.73
    rec = lignee_point(mod, w2, p, 1.20 * s_etoile[(p, w2)], compteur, "selftest", attendu=True)
    test("phase 1 transcrite == moteur (booleen ET indice) a p=4 w2=1.73 s=1.20 s*", rec["ok"] and rec["indice_identique"] is True,
         "indice %s" % rec["indice_instrument"])
    n_ok = sum(1 for _, ok in T if ok)
    C4v, C5v, C7v = [1.0 / (1.0 - 2.0 ** (-tol_ordre(alpha_de(pv)))) for pv in (4, 5, 7)]
    assert 1.0 < C4v < C5v < C7v < 9.0, "selftest v5 : C(p) ordonnees"
    lv = lecture_5_4(1.0, 4.0, alpha_de(5), 0.01)
    assert lv["W_plancher"] == "PASSE" and abs(lv["C_effectif"] - C5v) < 1e-12
    assert lecture_5_4(0.05, 4.0, alpha_de(5), 0.01)["W_pas"].startswith("NON LU")
    assert hash_canonique({"x": [1, 2]}) == hashlib.sha256(b'{"x": [1, 2]}').hexdigest()[:16], \
        "selftest v5 : forme canonique = separateurs PAR DEFAUT"
    JRN("SELFTEST", "v5 : C(p) = %.4f / %.4f / %.4f (pleine precision), lecture_5_4 trois branches, forme canonique -- PASSENT"
        % (C4v, C5v, C7v))
    _b4 = 1.0
    for _ in range(4):
        _b4 = math.nextafter(_b4, 0.0)
    assert ecart_ulp(1.0, _b4) == 4.0, "D-I-9 : 4 pas sous 1.0 se comptent 4 (l'ancienne forme rendait 2.00 et PASSAIT)"
    assert ecart_ulp(3.7, math.nextafter(3.7, math.inf)) == 1.0
    assert ecart_ulp(0.0, 0.0) == 0.0 and ecart_ulp(-1.5, -1.5) == 0.0
    JRN("SELFTEST", "v8 : ecart_ulp en PAS REPRESENTABLES (4 pas sous 1.0 = 4.0, D-I-9) ; BORNE_ULP unique = %g" % BORNE_ULP)
    JRN("SELFTEST", "bilan %d/%d" % (n_ok, len(T)))
    return n_ok == len(T), T


# =====================================================================
# 11. LE BANC QUI TUE -- chaque scenario ASSERTE sa branche
# =====================================================================

class FlotSynthetique(object):
    """Meme interface que FlotDS ; |D|(t) analytique : lineaire v t (avec
    gigue declaree sur t_c) ou blow-up D0/(1 - t/t*)."""

    def __init__(self, etat, caps, dt=DT1, regime="lineaire", v=0.5, t_star=100.0, gigue=0.3, y_profil=None):
        # regime : 'lineaire' | 'blowup' | 'borne' (ne franchit jamais caps[0]) ;
        # y_profil : liste de t_c/CAP imposee (branche 3bis (i))
        self.y_profil = y_profil
        self.caps = list(caps); self.dt = dt; self.regime = regime; self.v = v; self.t_star = t_star
        self.gigue = gigue; self.D0 = abs(etat[2])
        self.t_c = {}; self.n = 0; self.H1_0, self.N_0 = 2.0, 0.75
        self.derive_H1 = self.derive_N = 1e-6 * (dt / DT1) ** 4          # ordre 4 exact : q_int = 4, au-dessus du plancher
        self.x_max = abs(etat[0]); self.D_max = self.D0
        self.pics = []; self.non_fini = None; self.pas_serie = 100; self.serie = [(0.0, etat[0], etat[2], 2.0, 0.75)]

    def prolonger(self, horizon, T_lectures_pic=()):
        for j, c in enumerate(self.caps):
            if self.regime == "borne":
                continue
            if self.y_profil is not None:
                tc = self.y_profil[j] * c
            elif self.regime == "lineaire":
                tc = c / self.v + self.gigue * (-1) ** j
            else:
                tc = self.t_star * (1 - self.D0 / c)
            if tc <= horizon:
                self.t_c[c] = tc
        self.n = int(round(horizon / self.dt))
        for T in T_lectures_pic:
            if T <= horizon and not any(t == T for t, _, _ in self.pics):
                self.pics.append((T, T - 0.7, self.v * T))
        return self


def integrer_synthetique(loi, v=0.512, theta=0.9):
    """Fabrique (cap, t_max) -> integrer ; loi 'lineaire' : s* = cap/(v T) ;
    loi 'blowup' : s* = theta quels que soient cap et T (le mirage stable) ;
    loi 'racine' : s* = sqrt(cap)/(v T), ni l'une ni l'autre (3bis (ii))."""
    def fabrique(cap, tm):
        th = {"lineaire": cap / (v * tm), "blowup": theta, "racine": math.sqrt(cap) / (v * tm)}[loi]

        def integrer(w2, s_arr, sgn=1, dt=None, g=None):
            return np.asarray(s_arr, float) >= th
        return integrer
    return fabrique


# Au reglage prime, la dispersion lnA d'un synthetique doit DEPASSER le
# plancher' (sinon la branche 3b mord sur tout synthetique). Plutot qu'un
# bruit tire, la fabrique porte un DECALAGE lnA DECLARE par variante :
# plan (dt_2, k=2) -> 0 ; G-dt (dt_2/2) -> +B ; G-k (k=4) -> -B. La
# dispersion vaut 2B PAR CONSTRUCTION (deterministe, aucune graine), P-A
# est EXACT au plan, et 2B = 4e-06 > plancher'(7) = 9.178e-07, marge x4.
BRUIT_SYNTH = 2e-6


class SynthAlpha(object):
    """Synthetique de phase 1 / phase 2 pour le banc et le pre-vol :
    l'ansatz avec alpha_s, A_s ; sous le seuil, une oscillation bornee ou
    (regime 'faux_blowup') un ansatz avec t* = T_MAX + tau_dom/2."""

    def __init__(self, s_etoile, alpha_fact=1.0, A_fact=1.0, dep_s=0.0, sous_seuil="oscille", bruit=1e-7,
                 dep_dt=0.0, dep_k=0.0, dep_w2=0.0, sans_cap=False, bruit_lnA=None):
        self.s_etoile, self.alpha_fact, self.A_fact, self.dep_s, self.sous_seuil, self.bruit = \
            s_etoile, alpha_fact, A_fact, dep_s, sous_seuil, bruit
        self.dep_dt, self.dep_k, self.dep_w2, self.sans_cap = dep_dt, dep_k, dep_w2, sans_cap
        self.bruit_lnA = BRUIT_SYNTH if bruit_lnA is None else bruit_lnA

    def t_star_de(self, w2, p, s):
        return 20.0 + 3.0 * s / self.s_etoile[(p, w2)]

    def __call__(self, w2, s, p, mode, x_b=None, t_fin=None, **kw):
        self._c = s / self.s_etoile[(p, w2)]
        if mode == "bascule":
            self._k = K_BASC if x_b >= x_bascule_0(p, w2, K_BASC) * 0.999 else K_GARDE
            ts = self.t_star_de(w2, p, s); tb = ts - self._k * tau_dom(w2)
            n = int(math.floor(tb / DT1))   # v10 (D-v9-1) : floor, jamais round -- t0 <= tb, la fenetre est couverte a tout reglage
            return {"evenement": "BASCULE", "indice": n, "t": n * DT1, "etat": vers_composantes(*xm_et_derivees(p, ts - n * DT1), w2),
                    "bascule_sous_seuil_indice": None, "n_max": int(round(T_MAX_DEPOSE / DT1))}
        if mode == "seuil":
            n = int(math.floor(t_fin / DT1 * (1 + 1e-12)))
            return {"evenement": "T_FIN", "indice": n, "t": n * DT1, "etat": (0.0, 0.0, 0.0, 0.0),
                    "bascule_sous_seuil_indice": None, "n_max": int(round(T_MAX_DEPOSE / DT1))}
        raise ValueError(mode)

    def phase1_lignee(self, w2, s, p, mode, **kw):
        ex = s > self.s_etoile[(p, w2)]
        return {"evenement": "EXPLOSION" if ex else "T_MAX", "indice": 4000 if ex else int(round(T_MAX_DEPOSE / DT1)),
                "t": 0.0, "etat": (0.0, 0.0, 0.0, 0.0), "bascule_sous_seuil_indice": None, "n_max": 0}

    def phase2(self, w2, p, etat, t0, dt, arret_cap=None, t_max=T_MAX_DEPOSE, **kw):
        a = float(alpha_de(p)) * self.alpha_fact
        A = A_de(p) * self.A_fact
        rng = np.random.default_rng(int(1e6 * dt) + p)
        if arret_cap is not None:
            if self.sans_cap:
                n = int(round((t_max - t0) / dt))
                t = t0 + dt * np.arange(n + 1)
                return {"evenement": "T_MAX", "n": n, "t": t, "x1": 2.0 + np.cos(3.0 * t), "x2": np.zeros(len(t)),
                        "etat_fin": (0.0, 0.0, 0.0, 0.0)}
            x0 = etat[0] + etat[1]
            # decalage lnA DECLARE par variante (voir BRUIT_SYNTH) :
            if dt < dt2_de(w2) * 0.75:
                A = A * math.exp(+self.bruit_lnA)
            elif getattr(self, "_k", K_BASC) != K_BASC:
                A = A * math.exp(-self.bruit_lnA)
            a = a * (1 + self.dep_s * (self._c - C_PLAN[0]))
            a = a * (1 + self.dep_dt * (dt2_de(w2) / dt - 1.0))          # alpha(dt2/2) != alpha(dt2)
            a = a * (1 + self.dep_k * (self._k - K_BASC))                  # alpha(k=4) != alpha(k=2)
            a = a * (1 + self.dep_w2 * (w2 - W2S[0]))                     # alpha depend de w2
            ts = t0 + (A / abs(x0)) ** (1.0 / a)
            n = int(math.ceil((ts - tau_cap(w2) - t0) / dt))
            t = t0 + dt * np.arange(n + 1)
            t = t[ts - t >= tau_cap(w2) * (1 - 1e-12)]
            x = A * (ts - t) ** (-a) * (1 + self.bruit * rng.standard_normal(len(t)))
            return {"evenement": "CAP", "n": len(t) - 1, "t": t, "x1": x, "x2": np.zeros(len(t)), "etat_fin": (0.0, 0.0, 0.0, 0.0)}
        n = int(round((t_max - t0) / dt))
        t = t0 + dt * np.arange(n + 1)
        if self.sous_seuil == "faux_blowup":
            ts = t_max + tau_dom(w2) / 2
            x = A * (ts - t) ** (-a)
        else:
            x = 2.0 + np.cos(3.0 * t)
        return {"evenement": "T_MAX", "n": n, "t": t, "x1": x, "x2": np.zeros(len(t)), "etat_fin": (0.0, 0.0, 0.0, 0.0)}


def enumerer_gardes(registre):
    """D-b-2 : les gardes sont ENUMEREES par la machine depuis la section 8
    ('LES GARDES') du TEXTE de chaque gel, par leur ENTREE de definition
    (regle 12 : ancrage sur la structure -- une ligne de la section qui
    commence par quatre espaces puis le nom) : W-* au temoin, G-* a alpha.
    Une garde citee autrement dans la section (W-lignee, SORTIE du gel,
    D-t-2) n'a pas d'entree et n'est pas enumeree."""
    import re
    gardes = {}
    for (chemin, fam) in ((GEL_TEMOIN[0], "W"), (GEL_ALPHA_BASE[0], "G")):
        p = os.path.join(registre, chemin)
        if not os.path.isfile(p):
            continue
        t = open(p, encoding="utf-8").read()
        m = re.search(r"^8\. LES GARDES.*?(?=^9\. )", t, re.S | re.M)
        if m is None:
            sys.exit("ARRET regle 12 : section 8 introuvable dans %s" % chemin)
        for g in set(re.findall(r"^ {4}(%s-[a-z][a-z0-9]*)(?![A-Za-z0-9_-])" % fam, m.group(0), re.M)):
            gardes[g] = chemin
    p4 = os.path.join(registre, GEL_ALPHA[0])
    if os.path.isfile(p4) and re.search(r"^7[.] LA PORTE DU PLANCHER [(]G-plancher[)]",
                                        open(p4, encoding="utf-8").read(), re.M):
        gardes["G-plancher"] = GEL_ALPHA[0]
    return gardes


REGISTRE_BANC = "."


def banc_gardes(s_etoile, journal=True, mod=None):
    """Le banc des GARDES : chaque scenario declare la garde qu'il force et
    ASSERTE sa branche. Pur ou synthetique, quelques secondes : il se
    rejoue a la fin de CHAQUE run et remplit la liste de D-b-2. Rend
    (ok, scenarios, gardes_demontrees)."""
    S = []
    demontrees = set()

    def scenario(nom, ok, detail="", gardes=()):
        S.append((nom, bool(ok)))
        if journal:
            JRN("BANC", "%-60s %s %s" % (nom, "MORD" if ok else "NE MORD PAS", detail))
        assert ok, "BANC DEGENERE : %s -- %s" % (nom, detail)
        demontrees.update(gardes)
    caps = plafonds_T1(1.0)
    fl = FlotSynthetique((1.0, 0.0, 1.0, 0.0), caps, regime="lineaire").prolonger(400.0)
    L2 = lire_T1(fl.t_c, caps, T_0, 400.0)
    T2_ok = {"points": {"x": {"W_pas": "PASSE", "W_plancher": "PASSE", "W_bascule": "PASSE", "conversion_ok": True, "tol_ordre": 0.1}}}
    cpt0 = {"comptes": 0}
    T1b_ok = lire_T1b(jouer_T1b(cpt0, integrer_synthetique("lineaire"), 0.0)["recherches"], 0.0)
    base = {"T1": {"A": L2, "B": L2}, "T1b": T1b_ok, "T2": T2_ok, "T3b": {}}
    # -- temoin : W-pas, W-plancher, W-bascule, chacune SEULE -> branche 4
    for garde in ("W_pas", "W_plancher", "W_bascule"):
        pt = dict(T2_ok["points"]["x"]); pt[garde] = "MORD"
        v, b = cascade_temoin(dict(base, T2={"points": {"x": pt}}))
        nom_g = garde.replace("_", "-")
        autres = [x.replace("_", "-") for x in ("W_pas", "W_plancher", "W_bascule") if x != garde]
        scenario("G%d %s seule -> NON CONCLUANT D'INTEGRATEUR branche 4, motif la nomme seule" % (len(S) + 1, nom_g),
                 v == "NON CONCLUANT D'INTEGRATEUR" and nom_g in b and not any(o in b for o in autres),
                 v + " / " + b, gardes=(nom_g,))
    # -- W-croissance : |D| ne franchit pas CAP_0 avant T_0 -> branche 2
    fb = FlotSynthetique((1.0, 0.0, 1.0, 0.0), caps, regime="borne").prolonger(400.0)
    Lb = lire_T1(fb.t_c, caps, T_0, 400.0)
    v, b = cascade_temoin(dict(base, T1={"A": Lb, "B": L2}))
    scenario("G4 W-croissance (CAP_0 jamais franchi) -> NON CONCLUANT DE TEMOIN branche 2",
             Lb["W_croissance"] == "MORD" and v == "NON CONCLUANT DE TEMOIN", v + " / " + b, gardes=("W-croissance",))
    # -- 3bis (i) : R hors des deux fenetres a tolerance sous plafond (gigue alternee)
    fj = FlotSynthetique((1.0, 0.0, 1.0, 0.0), caps, y_profil=[2.0, 1.8, 2.0, 1.8, 2.0]).prolonger(400.0)
    Lj = lire_T1(fj.t_c, caps, T_0, 400.0)
    v, b = cascade_temoin(dict(base, T1={"A": Lj, "B": L2}))
    scenario("G5 3bis (i) R hors des deux fenetres, tol_R sous plafond -> NON CONCLUANT DE REGIME",
             (not Lj["fenetre_q"]) and (not Lj["fenetre_1"]) and Lj["resolution_ok"] and v == "NON CONCLUANT DE REGIME",
             "R=%s tol_R=%.3f %s" % (["%.3f" % r for r in Lj["R"]], Lj["tol_R"], v), gardes=())
    # -- 3bis (ii) : les rapports de 4.6 ne suivent ni l'une ni l'autre loi
    T1b_r = jouer_T1b({"comptes": 0}, integrer_synthetique("racine"), 0.0)
    v, b = cascade_temoin(dict(base, T1b=T1b_r))
    scenario("G6 3bis (ii) T-1b ni loi 1 ni stable (s* ~ sqrt(CAP)) -> NON CONCLUANT DE REGIME",
             T1b_r["regime"] == "NI_L_UNE_NI_L_AUTRE" and v == "NON CONCLUANT DE REGIME",
             "loi1=%.4f loi2=%.4f %s" % (T1b_r["loi1"], T1b_r["loi2"], v), gardes=("W-mirage",))
    # -- 4bis : une tolerance au-dessus de son plafond
    pt = dict(T2_ok["points"]["x"]); pt["tol_ordre"] = PLAFOND_ORDRE * 1.5
    v, b = cascade_temoin(dict(base, T2={"points": {"x": pt}}))
    scenario("G7 4bis tol_ordre > plafond -> NON CONCLUANT DE RESOLUTION", v == "NON CONCLUANT DE RESOLUTION", v + " / " + b, gardes=())
    # -- 4bis par tol_R : un t_c sature (dispersion) sans saturation lue
    fs = FlotSynthetique((1.0, 0.0, 1.0, 0.0), caps, y_profil=[2.0, 1.5, 1.2, 1.0, 0.9]).prolonger(400.0)
    Ls = lire_T1(fs.t_c, caps, T_0, 400.0)
    v, b = cascade_temoin(dict(base, T1={"A": Ls, "B": L2}))
    scenario("G8 4bis tol_R > eta_R (q-1) sans saturation -> NON CONCLUANT DE RESOLUTION",
             (not Ls["resolution_ok"]) and (not Ls["saturation"]) and v == "NON CONCLUANT DE RESOLUTION",
             "R=%s tol_R/(q-1)=%.3f %s" % (["%.3f" % r for r in Ls["R"]], Ls["tol_R_sur_q_moins_1"], v), gardes=())
    # -- temoin : W-comptes
    n_att_t = sum(compte_attendu_temoin().values())
    ok_c, v, b = verdict_comptes({"comptes": n_att_t - 1, "sautes": 0}, n_att_t, "REGLAGE QUALIFIE", "5", "BANC NON JOUE")
    scenario("G9 W-comptes %d + 0 != %d -> BANC NON JOUE" % (n_att_t - 1, n_att_t), ok_c == "MORD" and v == "BANC NON JOUE", b, gardes=("W-comptes",))
    # -- temoin : etat tangent refuse (D-b-4)
    try:
        FlotDS((1.0, 0.0, 0.0, 1.0), caps); refuse = False
    except SystemExit as e:
        refuse = "ETAT INTERDIT" in str(e)
    scenario("G10 etat tangent (1,0,0,1) : H1_0 = 0 -> ARRET declare (gel 4.3)", refuse, gardes=())
    # -- alpha, synthetiques : G-dt, G-k, G-w2, G-fen, G-comptes
    e_req = {4: 1e-5, 5: 1e-5, 7: 1e-5}

    def jouer_synth(sy):
        compteur = {"comptes": 0, "sautes": 0, "sautes_noms": []}
        plan, gdt, gk, seuil, lignee = {}, {}, {}, {}, {}
        for p in DEGRES:
            for w2 in W2S:
                dt2 = dt2_de(w2)
                for c in C_PLAN:
                    s = c * s_etoile[(p, w2)]; cle = "%d|%.2f|%.2f" % (p, w2, c)
                    plan[cle] = trajectoire_plan(w2, p, s, dt2, K_BASC, compteur, None, "s", sy)
                    gdt[cle] = trajectoire_plan(w2, p, s, dt2 / 2, K_BASC, compteur, None, "s", sy)
                    gk[cle] = trajectoire_plan(w2, p, s, dt2, K_GARDE, compteur, None, "s", sy)
                cle = "%d|%.2f" % (p, w2)
                seuil[cle] = trajectoire_seuil(w2, p, C_SEUIL * s_etoile[(p, w2)], dt2, compteur, None, "s", sy)
                for c in (C_SEUIL,) + C_PLAN:
                    lignee["%d|%.2f|%.2f" % (p, w2, c)] = {"ok": True, "attendu_respecte": True}
        return lire_alpha(plan, gdt, gk, seuil, lignee, e_req), compteur
    JRN.silence = True
    try:
        L_dt, _ = jouer_synth(SynthAlpha(s_etoile, dep_dt=0.2))
        L_k, _ = jouer_synth(SynthAlpha(s_etoile, dep_k=0.1))
        L_w, _ = jouer_synth(SynthAlpha(s_etoile, dep_w2=0.2))
        L_f, c_f = jouer_synth(SynthAlpha(s_etoile, sans_cap=True))
    finally:
        JRN.silence = False
    v, b = cascade_alpha(L_dt)
    scenario("G11 alpha(dt2) != alpha(dt2/2) -> G-dt MORD -> NON CONCLUANT DE RESOLUTION branche 2",
             v == "NON CONCLUANT DE RESOLUTION" and "G-dt" in b, v + " / " + b, gardes=("G-dt",))
    v, b = cascade_alpha(L_k)
    scenario("G12 alpha(k=4) != alpha(k=2) -> G-k MORD -> NON CONCLUANT DE RESOLUTION branche 2",
             v == "NON CONCLUANT DE RESOLUTION" and "G-k" in b, v + " / " + b, gardes=("G-k",))
    v, b = cascade_alpha(L_w)
    scenario("G13 alpha depend de w2 -> G-w2 MORD -> REFUTE branche 4, motif G-w2",
             v == "REFUTE" and "G-w2" in b and "G-s" not in b, v + " / " + b, gardes=("G-w2",))
    v, b = cascade_alpha(L_f)
    scenario("G14 CAP_p jamais atteint -> G-fen -> NON CONCLUANT DE FENETRE branche 3, compte inchange",
             v == "NON CONCLUANT DE FENETRE" and c_f["comptes"] == sum(compte_attendu_alpha().values()) - compte_attendu_alpha()["G_lignee"],
             "%s ; comptes=%d" % (v, c_f["comptes"]), gardes=("G-fen",))
    n_att_a = sum(compte_attendu_alpha().values())
    ok_c, v, b = verdict_comptes({"comptes": n_att_a - 1, "sautes": 0}, n_att_a, "VERIFIE", "5", "MANCHE NON JOUEE")
    scenario("G15 G-comptes %d + 0 != %d -> MANCHE NON JOUEE" % (n_att_a - 1, n_att_a), ok_c == "MORD" and v == "MANCHE NON JOUEE", b, gardes=("G-comptes",))
    # -- W-transcription, G-seuil, G-s (patrons B3a, B3b, B4d, B4e du banc complet)
    cst_faux = {"LO0": LO0, "HI0": HI0, "MAX_ELARG": MAX_ELARG, "NGRID": NGRID, "NPASSES": 2, "NDENSE": NDENSE}
    s_f, m_f, i_f = chercher_seuil_transcrit(integrer_synthetique("lineaire")(100.0, 200.0), 0.0, cst=cst_faux)
    ok_f, det_f = controle_transcription_positif(s_f, m_f, i_f)
    ok_k, det_k = controle_transcription_positif(7.46, "OK|pas=6.03e-07", {"k": 0, "encadrement": (LO0, HI0)})
    scenario("G16 W-transcription : NPASSES=2 et k incoherent -> controle positif MORD", (not ok_f) and (not ok_k),
             det_f, gardes=("W-transcription",))
    JRN.silence = True
    try:
        L_i, _ = jouer_synth(SynthAlpha(s_etoile, sous_seuil="faux_blowup"))
        L_s, _ = jouer_synth(SynthAlpha(s_etoile, dep_s=0.5))
    finally:
        JRN.silence = False
    v, b = cascade_alpha(L_i)
    scenario("G17 sous le seuil, un faux blow-up -> G-seuil MORD -> INSTRUMENT REFUTE", v == "INSTRUMENT REFUTE", v + " / " + b, gardes=("G-seuil",))
    v, b = cascade_alpha(L_s)
    scenario("G18 alpha depend de s -> G-s MORD -> REFUTE branche 4, motif G-s", v == "REFUTE" and "G-s" in b and "G-w2" not in b, v + " / " + b, gardes=("G-s",))
    # -- W-integrales (v7) : q_int != 4 -> MORD -> branche 6 ; plancher -> NON LUE (LD-16)
    class _F(object):
        def __init__(self, dH, dN, n, x_max=2.0):
            self.derive_H1, self.derive_N, self.n, self.x_max = dH, dN, n, x_max
    W_m = lire_W_integrales(_F(1e-8, 1e-9, 100000), _F(1e-8 / 8, 1e-9 / 16, 200000), DT1)
    L_w = dict(L2); L_w["W_integrales"] = W_m
    v, b = cascade_temoin(dict(base, T1={"A": L_w, "B": L2}))
    scenario("G20 W-integrales q_int(H1) = 3 -> MORD -> branche 6, QUALIFIE bonus retire",
             W_m["W_integrales"] == "MORD" and v.startswith("REGLAGE QUALIFIE (bonus") and "W-integrales" in b, v + " / " + b, gardes=("W-integrales",))
    W_p = lire_W_integrales(_F(1e-8, 1e-15, 100000), _F(1e-8 / 16, 1e-17, 200000), DT1)
    scenario("G21 derive(dt/2) sous le plancher machine -> NON LUE (LD-16), pas de morsure",
             W_p["integrales"]["N"]["q_int"] is None and W_p["integrales"]["H1"]["statut"] == "PASSE" and W_p["W_integrales"] == "PASSE",
             "N : %s ; H1 : %s" % (W_p["integrales"]["N"]["statut"], W_p["integrales"]["H1"]["statut"]), gardes=())
    # ------------------ scenarios v4 (gel constante A v4, 10 ; temoin v9) --
    # G22 branche 3b : dispersion SOUS le plancher -> NON CONCLUANT DE PLANCHER
    JRN.silence = True
    try:
        L_pl, _ = jouer_synth(SynthAlpha(s_etoile, bruit_lnA=0.0))
    finally:
        JRN.silence = False
    v, b = cascade_alpha(L_pl)
    scenario("G22 decalage lnA nul : dispersion sous le plancher' -> G-plancher MORD -> branche 3b",
             v == "NON CONCLUANT DE PLANCHER" and "3b" in b and all(L_pl["degres"][p]["G_plancher_mord"] for p in DEGRES),
             v + " / " + b, gardes=("G-plancher",))
    # G23-G26 : la chaine des etages sur le probleme MANUFACTURE (forcage),
    # depart a l'etat EXACT de la bascule 5.3 -- reel, court.
    p23, w23 = 7, 1.73
    f23 = forcage_de(p23, w23)
    e23 = vers_composantes(*xm_et_derivees(p23, K_BASC * tau_dom_0(w23)), w23)
    g2a = phase2_pu(w23, p23, e23, -K_BASC * tau_dom_0(w23), dt2a_de(w23),
                    forcage=f23, tau_star=0.0, arret_cap=x_bascule(p23, w23), t_max=1e9)
    lo23, hi23 = intervalle_evenement(n_2a_nominal(), retard_2a(w23))
    g2b = phase2_pu(w23, p23, g2a["etat_fin"], float(g2a["t"][-1]), dt2_de(w23),
                    forcage=f23, tau_star=0.0, arret_cap=cap_p(p23, w23), t_max=1e9)
    lo23b, hi23b = intervalle_evenement(n_2b_nominal(), RETARD_2B)
    scenario("G23 chaine 2a+2b manufacturee : comptes DANS les intervalles derives, CAP' atteint",
             g2a["evenement"] == "CAP" and lo23 <= g2a["n"] <= hi23
             and g2b["evenement"] == "CAP" and lo23b <= g2b["n"] <= hi23b,
             "n_2a=%d [%d,%d] n_2b=%d [%d,%d]" % (g2a["n"], lo23, hi23, g2b["n"], lo23b, hi23b), gardes=())
    scenario("G24 etage 2a ABSENT : n_2a = 0 hors [%d, %d] -> la garde de compte MORD (G-fen)" % (lo23, hi23),
             not (lo23 <= 0 <= hi23), "un 400 asserte ne l'aurait pas vu", gardes=("G-compte-etage",))
    xg = float(g2b["x1"][-1] + g2b["x2"][-1])
    scenario("G25 n_2s > 400 SANS morsure : 425 dans [400, 426] a w2=1.73 (un 400 asserte = banc mort)",
             intervalle_2s(1.73) == (400, 426) and 400 < 425 <= 426 and not (425 == 400),
             "n_2s derive = 425", gardes=())
    # G26 W-bascule voie A : g2 ABSENTE -> la remise d'etat que la CHAINE
    # COMPLETE qualifie (v9 8) rate : la phase grossiere a dt_1 place
    # l'etat a +-dt_1 pres (enorme devant tau' ~ 1.6e-03), et la LECTURE
    # D-t-19 sur la phase raffinee (e_avec <= tol x ln 10) MORD. Joue a
    # p = 4 (alpha = 2, derivees en tau^-3 / tau^-4 : le pas grossier ne
    # pardonne pas).
    p26, w26 = 4, 1.73
    f26 = forcage_de(p26, w26)
    eg1 = vers_composantes(*xm_et_derivees(p26, KP_BASC * tau_dom_0(w26)), w26)
    sans_g2 = phase2_pu(w26, p26, eg1, -KP_BASC * tau_dom_0(w26), DT1,
                        forcage=f26, tau_star=0.0, arret_cap=x_bascule(p26, w26), t_max=1e9)
    if sans_g2["evenement"] == "CAP":
        ph_r = phase2_pu(w26, p26, sans_g2["etat_fin"], float(sans_g2["t"][-1]), dt2_de(w26),
                         forcage=f26, tau_star=0.0, tau_fin=tau_cap(w26), t_max=1e9)
        if ph_r["evenement"] == "TAU_FIN":
            tau_r = np.maximum(-ph_r["t"], 1e-300)
            xm_r = A_de(p26) * tau_r ** (-float(alpha_de(p26)))
            e26 = float(np.max(np.abs((ph_r["x1"] + ph_r["x2"]) - xm_r) / np.abs(xm_r)))
        else:
            e26 = float("inf")
        rate = (not math.isfinite(e26)) or e26 > float(PLAFOND_ALPHA) * LN10
        det26 = "e_avec sans g2 = %.3e (lecture D-t-19 : tol = %.3e)" % (e26, float(PLAFOND_ALPHA) * LN10)
    else:
        rate = True
        det26 = "traversee grossiere : %s" % sans_g2["evenement"]
    scenario("G26 W-bascule voie A : g2 absente -> la lecture D-t-19 de la chaine complete MORD",
             rate, det26, gardes=("W-bascule",))
    # G27 D-M17-58 : une entree au signe inverse -> la garde MORD
    S27 = lire_signes(REGISTRE_BANC)
    t27 = {(p, "%.2f" % w2, S27[(p, w2)]["sgn"]): s_etoile[(p, w2)] for p in DEGRES for w2 in W2S}
    t27[(5, "2.27", +1)] = t27.pop((5, "2.27", -1))
    scenario("G27 D-M17-58 : table factice au signe inverse a (5, 2.27) -> la garde MORD",
             len(garde_signe_factice(t27, s_etoile, S27)) == 1, gardes=("D-M17-58",))
    # G28 9bis : mord au perimetre, muet hors perimetre et sur les exemptes
    ref28 = {"T1": {"A": {"x": 1.0, "duree_s": 3.0}}, "T1b": {}, "T3a": {}, "T3b": {},
             "meta": {"date_utc": "X"}}
    a28 = json.loads(json.dumps(ref28)); a28["T1"]["A"]["x"] = 2.0
    b28 = json.loads(json.dumps(ref28)); b28["meta"]["date_utc"] = "Y"; b28["T1"]["A"]["duree_s"] = 9.0
    scenario("G28 9bis : ecart au perimetre -> 1 ecart ; meta et duree_s -> 0 ecart",
             len(controle_9bis(a28, ref28, 3, {"duree_s"})) == 1
             and controle_9bis(b28, ref28, 3, {"duree_s"}) == [],
             gardes=("9bis",))
    if mod is not None:
        p, w2 = 4, 1.73

        def ph1_faux(w2, s, p, mode, **kw):
            return phase1_pu(w2, s, p, mode, acc_fn=lambda w2, g, p: acc_pu(w2, g, p + 1))
        rec = lignee_point(mod, w2, p, 1.20 * s_etoile[(p, w2)], {"comptes": 0}, "banc-faux", attendu=True, phase1=ph1_faux)
        scenario("G19 physique corrompue (exposant p) contre le moteur -> G-lignee ECART", not rec["ok"],
                 "booleen %s indice %s" % (rec["booleen_identique"], rec["indice_identique"]), gardes=("G-lignee",))
    return all(ok for _, ok in S), S, demontrees


def ne_joue_pas(L, compteur, gardes_enumerees, demontrees):
    """D-b-2 : le journal dit ce qu'il ne joue pas, trois listes enumerees."""
    non_lues = list(L.get("lectures_non_lues", []))
    for k, v in L.items():
        if isinstance(v, str) and v.startswith("NON LU") and not any(v in x or x in v for x in non_lues):
            non_lues.append("%s : %s" % (k, v))
    nues = sorted(g for g in gardes_enumerees if g not in demontrees)
    JRN("NE-JOUE-PAS", "lectures NON LUES : %s" % (non_lues if non_lues else "aucune"))
    JRN("NE-JOUE-PAS", "gardes sans morsure demontree dans ce journal (%d enumerees des gels, %d demontrees) : %s"
        % (len(gardes_enumerees), len(demontrees & set(gardes_enumerees)), nues if nues else "aucune"))
    JRN("NE-JOUE-PAS", "runs du gel non joues : %s" % (compteur.get("sautes_noms") or "aucun (%d sautes)" % compteur.get("sautes", 0)))
    L["ne_joue_pas"] = {"lectures_non_lues": non_lues, "gardes_sans_morsure": nues, "runs_non_joues": compteur.get("sautes_noms", [])}
    return L


def banc(registre, mod, sortie):
    """Un scenario qui n'asserte pas sa branche est un banc degenere."""
    S = []

    def scenario(nom, ok, detail="", gardes=()):
        S.append((nom, bool(ok)))
        JRN("BANC", "%-60s %s %s" % (nom, "MORD" if ok else "NE MORD PAS", detail))
        assert ok, "BANC DEGENERE : %s -- %s" % (nom, detail)
        banc.demontrees.update(gardes)
    banc.demontrees = set()
    caps = plafonds_T1(1.0)
    # B1 -- un faux blow-up (t_c sature) doit sortir REGLAGE REFUTE, branche 3
    fb = FlotSynthetique((1.0, 0.0, 1.0, 0.0), caps, regime="blowup", t_star=100.0).prolonger(400.0)
    L1 = lire_T1(fb.t_c, caps, T_0, 400.0)
    scenario("B1 faux blow-up : saturation lue (R non croissant, R_fin -> 1)", L1["saturation"], "R=%s" % ["%.4f" % r for r in L1["R"]])
    fl = FlotSynthetique((1.0, 0.0, 1.0, 0.0), caps, regime="lineaire").prolonger(400.0)
    L2 = lire_T1(fl.t_c, caps, T_0, 400.0)
    scenario("B1' croissance lineaire : fenetre de q, tol_R sous plafond", L2["fenetre_q"] and L2["resolution_ok"] and not L2["saturation"],
             "R=%s tol_R=%.4f" % (["%.4f" % r for r in L2["R"]], L2["tol_R"]))
    T2_ok = {"points": {"x": {"W_pas": "PASSE", "W_plancher": "PASSE", "W_bascule": "PASSE", "conversion_ok": True, "tol_ordre": 0.1}}}
    T1b_ok = lire_T1b(jouer_T1b({"comptes": 0}, integrer_synthetique("lineaire"), 0.0)["recherches"], 0.0)
    scenario("B2' loi lineaire synthetique : T-1b suit les deux lois", T1b_ok["regime"] == "LOIS" and T1b_ok["transcription_positif"],
             "loi1=%.5f loi2=%.5f" % (T1b_ok["loi1"], T1b_ok["loi2"]))
    v, b = cascade_temoin({"T1": {"A": L1, "B": L1}, "T1b": T1b_ok, "T2": T2_ok, "T3b": {}})
    scenario("B1 cascade : faux blow-up -> REGLAGE REFUTE branche 3", v == "REGLAGE REFUTE" and "saturation" in b, v + " / " + b, gardes=())
    v, b = cascade_temoin({"T1": {"A": L2, "B": L2}, "T1b": T1b_ok, "T2": T2_ok, "T3b": {}})
    scenario("B1' cascade : lineaire + lois + T-2 -> REGLAGE QUALIFIE branche 5", v == "REGLAGE QUALIFIE", v + " / " + b)
    # B2 -- un faux mirage (seuil STABLE sous les deux variations) doit MORD
    T1b_m = jouer_T1b({"comptes": 0}, integrer_synthetique("blowup", theta=0.9), 0.0)
    scenario("B2 faux mirage : seuil stable -> regime STABLE", T1b_m["regime"] == "STABLE", "loi1=%.5f loi2=%.5f" % (T1b_m["loi1"], T1b_m["loi2"]))
    v, b = cascade_temoin({"T1": {"A": L2, "B": L2}, "T1b": T1b_m, "T2": T2_ok, "T3b": {}})
    scenario("B2 cascade : mirage -> REGLAGE REFUTE branche 3 (W-mirage)", v == "REGLAGE REFUTE" and "mirage" in b, v + " / " + b, gardes=("W-mirage",))
    # B3 -- une fausse transcription doit MORD, trois mecanismes
    cst_faux = {"LO0": LO0, "HI0": HI0, "MAX_ELARG": MAX_ELARG, "NGRID": NGRID, "NPASSES": 2, "NDENSE": NDENSE}
    s_f, m_f, i_f = chercher_seuil_transcrit(integrer_synthetique("lineaire")(100.0, 200.0), 0.0, cst=cst_faux)
    ok_f, det_f = controle_transcription_positif(s_f, m_f, i_f)
    scenario("B3a transcription fausse (NPASSES=2) : controle positif MORD", not ok_f, det_f, gardes=("W-transcription",))
    ok_k, det_k = controle_transcription_positif(7.46, "OK|pas=6.03e-07", {"k": 0, "encadrement": (LO0, HI0)})
    scenario("B3b valeur juste, k incoherent (seuil 7.46 hors [0.05,6]) : MORD", not ok_k, det_k)
    ok_v, det_v = controle_transcription_positif(7.46, "OK|pas=6.03e-07", {"k": 1, "encadrement": (HI0, 4 * HI0)})
    scenario("B3b' k=1 avec pas de k=0 : MORD", not ok_v, det_v)
    sauve = mod.integrer
    try:
        n_diff = 0
        for th in (0.9, 7.46, 0.03):
            def synth(w2, s_arr, sgn=1, dt=None, g=None, th=th):
                return np.asarray(s_arr, float) >= th
            mod.integrer = synth
            d = mod._chercher_depose(0.0)
            tr = chercher_seuil_transcrit(synth, 0.0, cst={"LO0": LO0, "HI0": HI0, "MAX_ELARG": MAX_ELARG, "NGRID": 47, "NPASSES": NPASSES, "NDENSE": NDENSE})
            n_diff += int(d[0] != tr[0] or d[1] != tr[1])
    finally:
        mod.integrer = sauve
    scenario("B3c algorithme corrompu (NGRID=47) contre le moteur depose : ecart", n_diff == 3, "%d/3 ecarts" % n_diff)
    s_etoile, _ = lire_carte(registre)

    def acc_faux(w2, g, p):
        return acc_pu(w2, g, p + 1)
    p, w2 = 4, 1.73
    cpt = {"comptes": 0}

    def ph1_faux(w2, s, p, mode, **kw):
        return phase1_pu(w2, s, p, mode, acc_fn=acc_faux)
    rec = lignee_point(mod, w2, p, 1.20 * s_etoile[(p, w2)], cpt, "banc-faux", attendu=True, phase1=ph1_faux)
    scenario("B3d physique corrompue (exposant p) contre le moteur : G-lignee ECART", not rec["ok"],
             "booleen %s indice %s" % (rec["booleen_identique"], rec["indice_identique"]), gardes=("G-lignee",))
    # B4 -- alpha sur synthetiques : VERIFIE / REFUTE / PARTIEL / INSTRUMENT REFUTE / G-s
    e_req = {4: 1e-5, 5: 1e-5, 7: 1e-5}

    def jouer_synth(sy, sortie_s):
        compteur = {"comptes": 0, "sautes": 0}
        plan, gdt, gk, seuil, lignee = {}, {}, {}, {}, {}
        for p in DEGRES:
            for w2 in W2S:
                dt2 = dt2_de(w2)
                for c in C_PLAN:
                    s = c * s_etoile[(p, w2)]; cle = "%d|%.2f|%.2f" % (p, w2, c)
                    plan[cle] = trajectoire_plan(w2, p, s, dt2, K_BASC, compteur, sortie_s, "b_p%d_w%.2f_c%.2f_a" % (p, w2, c), sy)
                    gdt[cle] = trajectoire_plan(w2, p, s, dt2 / 2, K_BASC, compteur, sortie_s, "b_p%d_w%.2f_c%.2f_b" % (p, w2, c), sy)
                    gk[cle] = trajectoire_plan(w2, p, s, dt2, K_GARDE, compteur, sortie_s, "b_p%d_w%.2f_c%.2f_c" % (p, w2, c), sy)
                cle = "%d|%.2f" % (p, w2)
                seuil[cle] = trajectoire_seuil(w2, p, C_SEUIL * s_etoile[(p, w2)], dt2, compteur, sortie_s, "b_p%d_w%.2f_s" % (p, w2), sy)
                for c in (C_SEUIL,) + C_PLAN:
                    lignee["%d|%.2f|%.2f" % (p, w2, c)] = {"ok": True, "attendu_respecte": True}
        return lire_alpha(plan, gdt, gk, seuil, lignee, e_req)
    sb = None                                               # aucune serie synthetique ecrite
    JRN.silence = True                                      # silence des 450 lignes synthetiques
    try:
        L_0 = jouer_synth(SynthAlpha(s_etoile, bruit_lnA=0.0), sb)
        L_v = jouer_synth(SynthAlpha(s_etoile), sb)
        L_r = jouer_synth(SynthAlpha(s_etoile, alpha_fact=1.3), sb)
        L_p = jouer_synth(SynthAlpha(s_etoile, A_fact=1.5), sb)
        L_i = jouer_synth(SynthAlpha(s_etoile, sous_seuil="faux_blowup"), sb)
        L_s = jouer_synth(SynthAlpha(s_etoile, dep_s=0.5), sb)
    finally:
        JRN.silence = False
    v, b = cascade_alpha(L_0)
    scenario("B4a0 ansatz quasi exact : dispersion SOUS le plancher' -> branche 3b (v4 7)",
             v == "NON CONCLUANT DE PLANCHER" and "3b" in b, v + " / " + b, gardes=("G-plancher",))
    v, b = cascade_alpha(L_v)
    scenario("B4a ansatz exact au bruit d'instrument -> VERIFIE (3b muette : la dispersion depasse le plancher)",
             v == "VERIFIE", v + " / " + b)
    v, b = cascade_alpha(L_r)
    scenario("B4b exposant faux (x1.3) -> REFUTE", v == "REFUTE", v + " / " + b)
    v, b = cascade_alpha(L_p)
    scenario("B4c amplitude fausse (x1.5), exposant juste -> PARTIEL", v == "PARTIEL", v + " / " + b)
    v, b = cascade_alpha(L_i)
    scenario("B4d sous le seuil, un faux blow-up -> G-seuil MORD -> INSTRUMENT REFUTE", v == "INSTRUMENT REFUTE", v + " / " + b, gardes=("G-seuil",))
    v, b = cascade_alpha(L_s)
    scenario("B4e alpha dependant de s -> G-s MORD -> REFUTE branche 4", v == "REFUTE" and "G-s" in b, v + " / " + b, gardes=("G-s",))
    # B5 -- le banc des GARDES (D-b-3) : les quinze scenarios G1..G15
    ok_g, S_g, dem_g = banc_gardes(s_etoile, mod=mod)
    S.extend(S_g); banc.demontrees.update(dem_g)
    scenario("B5 banc des gardes : %d/%d scenarios mordent" % (sum(1 for _, o in S_g if o), len(S_g)), ok_g)
    # B6 -- la double transcription de (2.11) contre la mesure gelee de 4.6 (machine 2)
    etat_A = ETATS_T1[0][1:]
    t0 = time.perf_counter()
    s_ds, m_ds, i_ds = chercher_seuil_transcrit(integrer_ds_pour_recherche(etat_A, T1B_CAP, T1B_T), 0.0)
    scenario("B6 seuil (CAP 100, T 200) contre la mesure gelee 0.977252977 (gel 4.6, m2)",
             s_ds is not None and abs(s_ds - 0.977252977) <= 2 * 6.0325e-07 and m_ds == "OK|pas=6.03e-07",
             "seuil=%r %s (%.1fs)" % (s_ds, m_ds, time.perf_counter() - t0))
    # B7 -- la porte de alpha refuse un temoin non qualifie ou un reglage etranger
    chp = os.path.join(sortie, "banc_porte_fausse.json")
    ecrire_ascii(chp, json_ascii({"verdict": "NON CONCLUANT DE REGIME", "reglage": {}}))
    try:
        lire_porte_temoin(chp); ferme = False
    except SystemExit:
        ferme = True
    scenario("B7 porte fermee sur un temoin NON CONCLUANT", ferme)
    ecrire_ascii(chp, json_ascii({"verdict": "REGLAGE QUALIFIE", "reglage": {"delta": "1/50", "r": "1/10", "M": 20, "k": 2, "eta": "1/4"}}))
    try:
        lire_porte_temoin(chp); ferme = False
    except SystemExit:
        ferme = True
    scenario("B7' porte fermee sur un reglage etranger (delta=1/50)", ferme)
    gardes = enumerer_gardes(registre)
    # -- G29..G31 : le CHARGEUR au contrat (e69d8a006f584063), sur le depot REEL
    ch_dep = os.path.join(REGISTRE_BANC, "journal", "depot_9bis_temoin_v1.json")
    if os.path.isfile(ch_dep):
        r9 = charger_depot_9bis(ch_dep, REGISTRE_BANC)
        ec0 = controle_9bis({c: r9["reference"][c] for c in ("T1", "T1b", "T3a", "T3b")},
                            r9["reference"], r9["profondeur"], r9["exemptes"])
        scenario("G29 chargeur : depot REEL charge, comptes et profondeur RE-DERIVES, custody %s, identite -> 0 ecart"
                 % ("JOUEE" if r9["custody"].startswith("JOUE") else "NON JOUEE"),
                 (not ec0) and r9["depot_empreinte"] == "c4310e33da6b9759",
                 "empreinte %s ; %s" % (r9["depot_empreinte"], r9["custody"][:60]), gardes=())
        dep2 = json.load(open(ch_dep, encoding="utf-8"))
        dep2["reference"]["T1b"]["recherches"]["a"]["seuil"] += 1e-9
        ch2 = os.path.join("/tmp", "depot_9bis_perturbe.json")
        with open(ch2, "w") as f2:
            json.dump(dep2, f2, indent=1); f2.write("\n")
        try:
            charger_depot_9bis(ch2, REGISTRE_BANC)
            rate30, det30 = False, "aucun arret"
        except RuntimeError as ex30:
            rate30, det30 = ("divergent" in str(ex30)), str(ex30)[:96]
        scenario("G30 chargeur : copie embarquee PERTURBEE d'une feuille -> ARRET 9bis, depot et registre divergent",
                 rate30, det30, gardes=())
        dep3 = json.load(open(ch_dep, encoding="utf-8"))
        dep3["reference_fichier"] = "runs/absent_9bis.json"
        ch3 = os.path.join("/tmp", "depot_9bis_absent.json")
        with open(ch3, "w") as f3:
            json.dump(dep3, f3, indent=1); f3.write("\n")
        r93 = charger_depot_9bis(ch3, REGISTRE_BANC)
        scenario("G31 chargeur : reference ABSENTE du registre -> custody NON JOUE consigne, le controle se joue quand meme",
                 r93["custody"].startswith("NON JOUE"), r93["custody"], gardes=())
    else:
        scenario("G29 chargeur : depot 9bis ABSENT de journal/ -- les scenarios du contrat ne peuvent pas jouer",
                 False, ch_dep, gardes=())
    # -- G32 : D-I-1, l'ORDRE ecrire-puis-arreter
    d32 = os.path.join("/tmp", "banc_di1")
    os.makedirs(d32, exist_ok=True)
    f32 = os.path.join(d32, "resultats_ordre.json")
    ecrire_ascii(f32, "{}\n")
    try:
        arret_prevol_si_fautes(["scenario de banc"])
        rate32 = False
    except SystemExit:
        rate32 = os.path.isfile(f32)
    scenario("G32 D-I-1 : l'arret de pre-vol tombe APRES l'ecriture -- la sortie existe quand il tombe",
             rate32, "ordre ecrire-puis-arreter demontre", gardes=())
    # -- G33 : la lecture 5.4, DEUX sens (v11 8 : W-plancher est la garde)
    a33 = float(alpha_de(7)); eps33 = float(np.finfo(float).eps)
    pc33 = eps33 * 2 * a33 * (a33 + 1) / ((1.73 * 1.73 - 1) * tau_cap(1.73) ** 2)
    l_bas = lecture_5_4(0.5 * pc33 * 8.0, 3.99, a33, pc33)
    l_ok = lecture_5_4(2.0 * l_bas["seuil"], 3.99, a33, pc33)
    l_mord = lecture_5_4(2.0 * l_bas["seuil"], 3.40, a33, pc33)
    scenario("G33 5.4 : sous le seuil -> W-plancher MORD et l'ordre NON LU ; au-dessus -> PASSE, puis MORD au p_obs",
             l_bas["W_plancher"] == "MORD" and l_bas["W_pas"].startswith("NON LU")
             and l_ok["W_plancher"] == "PASSE" and l_ok["W_pas"] == "PASSE" and l_mord["W_pas"] == "MORD",
             "C_eff=%.4f seuil=%.3e" % (l_bas["C_effectif"], l_bas["seuil"]), gardes=("W-plancher", "W-pas"))
    # -- G34 : D-I-5/6, la garde SUR LES NOMBRES -- bornes BORNE_ULP / BORNE_ULP
    txt34, _e34 = champ_de_forces_tirage()
    L34 = [l.split() for l in txt34.splitlines() if l.strip() and not l.lstrip().startswith("#")]
    def _p34(i, j, k):
        M = [list(r) for r in L34]
        v = float(M[i][j])
        for _ in range(k):
            v = math.nextafter(v, math.inf)
        M[i][j] = "%.17g" % v
        return "".join(" ".join(r) + "\n" for r in M)
    c_id = comparer_champs_ulp(txt34, txt34)
    c_D1 = comparer_champs_ulp(txt34, _p34(7, 3, 1))
    c_D3 = comparer_champs_ulp(txt34, _p34(7, 3, 3))
    c_x1 = comparer_champs_ulp(txt34, _p34(11, 2, 1))
    c_x3 = comparer_champs_ulp(txt34, _p34(11, 2, 3))
    c_t1 = comparer_champs_ulp(txt34, _p34(3, 0, 1))
    scenario("G34 D-I-5/6 : identite 0 ulp ; x''+1 et D''+1 PASSENT (bornes %g / %g) ; x''+3 et D''+3 MORDENT ; tirage+1 MORD" % (BORNE_ULP, BORNE_ULP),
             c_id["verdict"] == "PASSE" and c_id["max_ulp_Dpp"] == 0.0
             and c_x1["verdict"] == "PASSE" and 0 < c_x1["max_ulp_xpp"] <= BORNE_ULP
             and c_D1["verdict"] == "PASSE" and 0 < c_D1["max_ulp_Dpp"] <= BORNE_ULP
             and c_x3["verdict"] == "MORD" and "x''" in c_x3["resume"]
             and c_D3["verdict"] == "MORD" and "D''" in c_D3["resume"]
             and c_t1["verdict"] == "MORD" and "TIRAGE" in c_t1["resume"],
             "la reaction se teste ici ; la VERITE des bornes est inter-machines (note m2 3)", gardes=("W-transcription",))
    n_ok = sum(1 for _, ok in S if ok)        # D-I-3 (1) : APRES le dernier ajout, ici et ici seul
    nues = sorted(g for g in gardes if g not in banc.demontrees)
    JRN("BANC", "bilan %d/%d scenarios mordent ; gardes enumerees des gels %d, demontrees %d, sans morsure : %s"
        % (n_ok, len(S), len(gardes), len(banc.demontrees & set(gardes)), nues))
    return n_ok == len(S), S


# =====================================================================
# 12. PRE-VOL A MOTEUR FACTICE -- sorties SEPAREES, bannieres partout
# =====================================================================

CHAMP_COMPARE = None              # --champ-compare : seconde transcription (D-I-5)
BORNE_ULP = 2.0                   # LA borne (D-I-8) : ecrite UNE fois, citee par
                                  # tous ses consommateurs -- x'' pow libm
                                  # inter-machines ; D'' re-association
                                  # inter-plumes ; MESUREE aux trois regimes
                                  # (2 plumes, 2 machines, maxima 2/2/2),
                                  # NON PROUVEE, declaree telle (v7 X03).


def empreinte_B_texte(t):
    return hashlib.sha256(t.replace("\r\n", "\n").encode()).hexdigest()[:16]


def colonnes_x_D_seules(texte):
    """D-I-5 (1) : le TIRAGE (colonnes x, D) est bit-reproductible
    (PCG64, spec) et OPPOSABLE ; le CHAMP (x'', D'') passe par pow()
    libm et ne l'est pas -- deux empreintes, deux statuts."""
    return "".join(" ".join(l.split()[:2]) + "\n" for l in texte.splitlines()
                   if l.strip() and not l.lstrip().startswith("#"))


def ecart_ulp(a, b):
    # ulp(max) sous-compte d'un facteur 2 au bord bas d'une
    # binade (4 pas sous 1.0 rendent 2.00). La distance en ulps
    # est un COMPTE DE PAS, pas une fraction : elle se lit sur la
    # representation, ou elle est exacte. (D-I-9, forme audit m2.)
    import struct
    ia = struct.unpack('<q', struct.pack('<d', a))[0]
    ib = struct.unpack('<q', struct.pack('<d', b))[0]
    if (ia < 0) != (ib < 0):
        return float(abs(ia) + abs(ib))    # de part et d'autre de 0
    return float(abs(ia - ib))


def comparer_champs_ulp(texte_a, texte_b):
    """D-I-5 (3) : la garde se lit SUR LES NOMBRES, bornes DERIVEES, et
    chacune vaut pour une RAISON DIFFERENTE (D-I-6) :
       TIRAGE : 0 ulp, toujours (PCG64, spec).
       x''  <= 2 ulp : sa chaine contient x ** 3, seul appel libm de
              tout le champ -- non bit-reproductible ENTRE MACHINES
              (D-I-5). Exact a machine egale.
       D''  <= 2 ulp : sa chaine (+, -, x) est IEEE-exacte, donc
              identique entre MACHINES -- mais la RE-ASSOCIATION d'un
              produit a trois facteurs la deplace entre PLUMES
              (mesure machine 2, note 5bis).
    Les deux effets sont ORTHOGONAUX : la borne 2 couvre les deux
    regimes et leur cumul. BORNE MESUREE (4096 points, 2
    plates-formes, 2 plumes), NON PROUVEE -- elle se declare telle.
    Jamais un verdict vide."""
    def _donnees(t):
        return [tuple(float(c) for c in l.split()) for l in t.splitlines()
                if l.strip() and not l.lstrip().startswith("#")]
    A, B = _donnees(texte_a), _donnees(texte_b)
    if len(A) != len(B) or any(len(a) != 4 or len(b) != 4 for a, b in zip(A, B)):
        return {"verdict": "MORD", "n": len(A),
                "resume": "MORD -- formes incompatibles (%d vs %d lignes)" % (len(A), len(B))}
    tir = all(a[0] == b[0] and a[1] == b[1] for a, b in zip(A, B))
    u_x = max(ecart_ulp(a[2], b[2]) for a, b in zip(A, B))
    u_D = max(ecart_ulp(a[3], b[3]) for a, b in zip(A, B))
    n_x = sum(1 for a, b in zip(A, B) if a[2] != b[2])
    n_D = sum(1 for a, b in zip(A, B) if a[3] != b[3])
    fautes = []
    if not tir:
        fautes.append("TIRAGE pas au bit")
    if u_x > BORNE_ULP:
        fautes.append("x'' %.1f ulp > %g (pow libm + arrondi)" % (u_x, BORNE_ULP))
    if u_D > BORNE_ULP:
        fautes.append("D'' %.1f ulp > %g (re-association)" % (u_D, BORNE_ULP))
    v = "MORD" if fautes else "PASSE"
    return {"verdict": v, "n": len(A), "tirage_au_bit": tir,
            "max_ulp_xpp": u_x, "max_ulp_Dpp": u_D,
            "ecarts_xpp": n_x, "ecarts_Dpp": n_D,
            "resume": "%s -- tirage %s ; x'' max %.1f ulp (%d ecarts) ; D'' max %.1f ulp (%d ecarts) ; bornes %g / %g%s"
                      % (v, "BIT" if tir else "ECART", u_x, n_x, u_D, n_D, BORNE_ULP, BORNE_ULP,
                         (" ; " + " ; ".join(fautes)) if fautes else "")}


def lecture_5_4(e_half, p_obs, alpha_f, pc):
    """Gel v11 5.4 : W-plancher = e(dt2/2) >= C(p) x plancher_comp,
    C(p) = 1/(1-2^-tol_ordre(p)) en PLEINE PRECISION, consigne. Sous le
    seuil : W-plancher MORD et l'ordre N'EST PAS LU, ni dans un sens ni
    dans l'autre. CONDITION NECESSAIRE (D-t-25) : au-dessus, le critere
    ne certifie pas seul -- le residuel se lit aux consignations."""
    tol = tol_ordre(alpha_f)
    C_eff = 1.0 / (1.0 - 2.0 ** (-tol))
    seuil = C_eff * pc
    lu = e_half >= seuil
    return {"tol": tol, "C_effectif": C_eff, "seuil": seuil, "lu": lu,
            "ratio_seuil": (e_half / seuil) if seuil > 0 else float("inf"),
            "W_plancher": "PASSE" if lu else "MORD",
            "W_pas": (("PASSE" if abs(p_obs - ORDRE_SCHEMA) <= tol else "MORD")
                      if lu else "NON LU (plancher, 5.4)")}


def dossier_vierge(sortie):
    """D-I-2 : un dossier de sortie est VIDE ou VERSIONNE avant ecriture."""
    if os.path.isdir(sortie) and os.listdir(sortie):
        anc = sortie + ".avant_" + time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
        os.rename(sortie, anc)
        JRN("D-I-2", "sortie non vide VERSIONNEE : %s -> %s" % (sortie, anc))
    os.makedirs(sortie, exist_ok=True)
    return sortie


def arret_prevol_si_fautes(fautes):
    """D-I-1, seconde moitie : l'arret vient APRES l'ecriture, toujours."""
    if fautes:
        JRN("ARRET", "PREVOL : fautes du factice, APRES ecriture (D-I-1) : %s" % " ; ".join(fautes))
        raise SystemExit(2)


def hash_canonique(o):
    """Contrat chargeur (e69d8a006f584063) : json.dumps(sort_keys=True,
    ensure_ascii=True), separateurs PAR DEFAUT ; sha256, 16 hex."""
    return hashlib.sha256(json.dumps(o, sort_keys=True, ensure_ascii=True).encode()).hexdigest()[:16]


def charger_depot_9bis(chemin, registre):
    """Contrat (a)-(d)+(c') e69d8a006f584063. La piece opposable est le
    DEPOT (son empreinte B au journal) ; comptes ET profondeur se
    RE-DERIVENT de la copie embarquee ; custody contre le registre est
    une MORSURE ; present-mais-illisible = la meme ; absent = NON JOUE
    consigne. Leve RuntimeError('ARRET 9bis : ...') ; main traduit."""
    def arret(m):
        raise RuntimeError("ARRET 9bis : " + m)
    dep = json.load(open(chemin, encoding="utf-8"))
    emp = empreinte_B(chemin)
    perim = tuple(dep["perimetre"]); prof = int(dep["profondeur"]); exe = set(dep["exemptes"])
    ref = dep["reference"]
    fe, conts = [], []
    def marche(o, ch, p):
        if isinstance(o, dict):
            conts.append(p)
            for k in sorted(o):
                marche(o[k], ch + "/" + str(k), p + 1)
        elif isinstance(o, list):
            conts.append(p)
            for i, v in enumerate(o):
                marche(v, "%s[%d]" % (ch, i), p + 1)
        else:
            fe.append((p, ch.rsplit("/", 1)[-1]))
    for c in perim:
        if c not in ref:
            arret("sous-arbre /%s absent de la copie embarquee." % c)
        marche(ref[c], "/" + c, 0)
    nfe = len(fe); nno = nfe + len(conts)
    nex = sum(1 for _, n in fe if (n.split("[", 1)[0] if n.endswith("]") else n) in exe)
    att = dep["comptes"]
    if not (nno == att["noeuds"] and nfe == att["feuilles"] and nex == att["exemptees"]
            and nfe - nex == att["comparees"]):
        arret("comptes non re-derives de la copie : %d/%d/%d/%d contre %s." % (nno, nfe, nex, nfe - nex, att))
    if any(p > prof for p, _ in fe):
        arret("une feuille depasse la profondeur declaree %d." % prof)
    if all(p <= prof - 1 for p, _ in fe):
        arret("profondeur %d non minimale : prof-1 atteint deja toutes les feuilles." % prof)
    r9 = {"reference": ref, "profondeur": prof, "exemptes": exe,
          "nom": "%s (gel %s)" % (dep.get("nom", os.path.basename(chemin)), dep.get("gel", "?")),
          "depot_empreinte": emp, "custody": None}
    rf = dep.get("reference_fichier")
    ch_r = os.path.join(registre, rf) if rf else None
    if ch_r and os.path.isfile(ch_r):
        try:
            reg = json.load(open(ch_r, encoding="utf-8"))
        except Exception as ex:
            arret("reference %s PRESENTE MAIS ILLISIBLE (%s : %s) -- l'absence se constate, elle ne s'improvise pas."
                  % (rf, type(ex).__name__, ex))
        if empreinte_B(ch_r) != dep["reference_empreinte"]:
            arret("empreinte de %s : %s, attendue %s." % (rf, empreinte_B(ch_r), dep["reference_empreinte"]))
        for c in perim:
            he, hr = hash_canonique(ref[c]), hash_canonique(reg.get(c))
            JRN("9bis", "custody /%s : embarquee %s  registre %s" % (c, he, hr))
            if ref[c] != reg.get(c):
                arret("depot et registre divergent (/%s : %s vs %s)." % (c, he, hr))
        r9["custody"] = "JOUE : embarquee == registre 4/4 (fichier %s)" % dep["reference_empreinte"]
    else:
        r9["custody"] = "NON JOUE (reference absente du registre) -- le controle se joue sur la copie embarquee"
        JRN("NE-JOUE-PAS", "9bis custody : " + r9["custody"])
    JRN("9bis", "depot charge %s  empreinte B %s  gel %s  profondeur %d  exemptes %s"
        % (os.path.basename(chemin), emp, dep.get("gel", "?"), prof, sorted(exe)))
    return r9


def prevol_temoin(registre, sortie, mod):
    pv = {"flot_cls": FlotSynthetique, "fabrique_T1b": integrer_synthetique("lineaire"), "osc": 0.0}
    L = executer_temoin(registre, sortie, mod, prevol=pv)
    fautes = []
    if L["W_comptes"] != "PASSE":
        fautes.append("W-comptes %s (le factice determine les comptes)" % L["W_comptes"])
    JRN("PREVOL", "verdict CONSIGNE, jamais asserte (D-I-1) : %s -- %s" % (L["verdict"], L["branche"]))
    L["prevol_fautes"] = fautes
    return L


def prevol_alpha(registre, sortie, mod):
    s_etoile, _ = lire_carte(registre)
    porte = {"fichier": "PREVOL", "empreinte": "PREVOL", "verdict": "REGLAGE QUALIFIE (PREVOL)", "statut": "PREVOL",
             "e_sur_ln10_max": {p: 1e-9 for p in DEGRES}}
    L = executer_alpha(registre, sortie, mod, porte, prevol={"synth": SynthAlpha(s_etoile)})
    fautes = []
    if not L["verdict"].endswith("VERIFIE"):
        fautes.append("verdict %s (SynthAlpha determine VERIFIE)" % L["verdict"])
    if not (L["G_lignee"]["n_ok"] == 9 and L["G_lignee"]["n"] == 27):
        fautes.append("G-lignee %s/%s (le factice devait tuer les 18 indices)" % (L["G_lignee"]["n_ok"], L["G_lignee"]["n"]))
    if L["G_comptes"] != "PASSE":
        fautes.append("G-comptes %s" % L["G_comptes"])
    JRN("PREVOL", "verdict CONSIGNE, fautes assertees APRES ecriture (D-I-1) : %s -- %d faute(s)"
        % (L["verdict"], len(fautes)))
    L["prevol_fautes"] = fautes
    return L


# =====================================================================
# 13. MAIN
# =====================================================================

def _json_default(o):
    if isinstance(o, (np.floating, np.integer, np.bool_)):
        return o.item()
    if isinstance(o, np.ndarray):
        return o.tolist()
    if isinstance(o, Fraction):
        return str(o)
    if isinstance(o, (set, tuple)):
        return list(o)
    if isinstance(o, float) and not math.isfinite(o):
        return repr(o)
    raise TypeError(repr(o))


def ecrire_resultats(sortie, mode, L, statut, brut_script):
    import platform
    L["meta"] = {"version": VERSION, "statut": statut, "date_utc": date_utc(), "mode": mode,
                 "machine": platform.node(), "plateforme": platform.platform(), "python": platform.python_version(),
                 "numpy": np.__version__, "opposable": "seulement si joue par machine 2 sur BOCAL4 (N-62, pre-vol E19)",
                 "script_sha256_brut": hashlib.sha256(brut_script).hexdigest(), "script_taille": len(brut_script),
                 "gel_temoin": GEL_TEMOIN, "gel_alpha": GEL_ALPHA, "cert_temoin": CERT_TEMOIN, "cert_alpha": CERT_ALPHA,
                 "gel_temoin_base": GEL_TEMOIN_BASE, "gel_alpha_base": GEL_ALPHA_BASE,
                 "cert_temoin_base": CERT_TEMOIN_BASE, "cert_alpha_base": CERT_ALPHA_BASE,
                 "moteur": MOTEUR, "carte": CARTE, "files_maximum_cite": FILES_MAX_CITE,
                 "lectures_declarees": ["LD-%d" % i for i in range(1, 15)]}
    L["reglage"] = {"delta": str(DELTA), "delta_0": str(DELTA_0), "b": B_DESC, "m": M_MARGE, "J": J_DESC,
                    "r": str(R_CAP), "M": M_PAS, "k": K_BASC, "eta": str(ETA),
                    "q": Q_ECH, "c_T": C_T, "c_0": C_0, "k_prime": KP_BASC, "eta_R": str(ETA_R),
                    "dt1": DT1, "T_MAX_depose": T_MAX_DEPOSE, "CAP_depose": CAP_DEPOSE}
    L["statut"] = statut

    def assainir(o):
        if isinstance(o, dict):
            return {str(k): assainir(v) for k, v in o.items()}
        if isinstance(o, (list, tuple)):
            return [assainir(v) for v in o]
        if isinstance(o, float) and not math.isfinite(o):
            return repr(o)
        return o
    texte = json.dumps(assainir(L), indent=1, sort_keys=True, ensure_ascii=True, default=_json_default)
    ch = ecrire_ascii(os.path.join(sortie, "resultats_%s.json" % mode), texte)
    JRN("JSON", "%s  %d o  empreinte B %s" % (ch, os.path.getsize(ch), empreinte_B(ch)))
    return ch


def main():
    ap = argparse.ArgumentParser(description=VERSION)
    ap.add_argument("--mode", choices=("temoin", "alpha"))
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--banc", action="store_true")
    ap.add_argument("--prevol", action="store_true", help="pre-vol a moteur factice, sorties SEPAREES (out_prevol)")
    ap.add_argument("--registre", default=".", help="racine du clone du registre (gels/, scripts/, runs/, journal/)")
    ap.add_argument("--sortie", default=None)
    ap.add_argument("--porte-temoin", default=None, help="resultats_temoin.json du run REEL du temoin (mode alpha)")
    ap.add_argument("--controle-9bis", default=None, help="JSON depose AVANT le run (N-70) : {reference, profondeur, exemptes} pour le controle de reproductibilite (mode temoin)")
    ap.add_argument("--champ-compare", default=None, help="fichier champ (4096 x 4) d'une SECONDE transcription : comparaison SUR LES NOMBRES, bornes derivees %g / %g ulp a portee ecrite (D-I-5/6)" % (BORNE_ULP, BORNE_ULP))
    a = ap.parse_args()
    globals()["CHAMP_COMPARE"] = a.champ_compare
    global REGISTRE_BANC
    REGISTRE_BANC = a.registre
    t_debut = time.perf_counter()
    JRN("DEBUT", "%s  %s  UTC %s" % (VERSION, " ".join(sys.argv[1:]), date_utc()))
    JRN("FILES", "E18 : aucun numero pris ; maximum cite %s" % FILES_MAX_CITE)
    brut = n59_copie_executee()
    mode_instr = a.selftest or a.banc
    verifier_ancres(a.registre, exiger_gels=not mode_instr)
    if a.selftest or a.banc:
        sortie = a.sortie or "out_instrument"
        mod = charger_moteur(a.registre)
        ok_s, T = selftest(a.registre, mod)
        if not ok_s:
            sys.exit("ARRET : selftest %d/%d" % (sum(1 for _, o in T if o), len(T)))
        if a.banc:
            ok_b, S = banc(a.registre, mod, sortie)   # REGISTRE_BANC deja lie (P39)
            ko = [nom for nom, o in S if not o]
            if (not ok_b) and not ko:
                sys.exit("ARRET : banc INCOHERENT -- retour False sans scenario en echec : compteur pris au mauvais endroit (D-I-3)")
            if not ok_b:
                sys.exit("ARRET : banc %d/%d -- n'ont pas mordu : %s" % (len(S) - len(ko), len(S), ko))
            JRN("BANC", "retour du banc CONSOMME : %d/%d, coherent (D-I-3)" % (len(S), len(S)))
        JRN("FIN", "%.1f s" % (time.perf_counter() - t_debut))
        return
    if a.mode is None:
        sys.exit("usage : --mode temoin|alpha [--prevol] | --selftest | --banc")
    if a.prevol:
        sortie = dossier_vierge(a.sortie or os.path.join("out_prevol", a.mode))
        assert "prevol" in sortie.lower(), "le pre-vol ecrit dans un dossier qui porte 'prevol' dans son nom"
        s_etoile, _ = lire_carte(a.registre)
        signes = lire_signes(a.registre)
        table = {}
        for p in DEGRES:
            for w2 in W2S:
                S = signes[(p, w2)]
                table[(p, "%.2f" % w2, S["sgn"])] = s_etoile[(p, w2)]           # le seuil de la branche jouee
                if S["sM"] is not None:                                          # et l'autre branche, si la carte la porte
                    table[(p, "%.2f" % w2, -S["sgn"])] = max(float(S["sP"]), float(S["sM"]))
        fautes_58 = garde_signe_factice(table, s_etoile, signes)
        JRN("D-M17-58", "garde de signe au pre-vol : table_factice[(p, w2, sgn)] == sF, 9 points -> %s"
            % ("PASSE" if not fautes_58 else "MORD : %s" % fautes_58))
        if fautes_58:
            sys.exit("ARRET D-M17-58 : la table factice ne porte pas sF au signe joue (%s)." % fautes_58)
        mod = charger_moteur(a.registre, factice=fabriquer_factice(table))
        JRN("PREVOL", "BANNIERE : PRE-VOL, sorties dans %s, aucune mesure n'existe ici (N-62)" % sortie)
        L = prevol_temoin(a.registre, sortie, mod) if a.mode == "temoin" else prevol_alpha(a.registre, sortie, mod)
        statut = "PREVOL"
    else:
        sortie = dossier_vierge(a.sortie or os.path.join("out_banc", a.mode))
        assert "prevol" not in sortie.lower(), "un run reel ne s'ecrit pas dans un dossier de pre-vol"
        mod = charger_moteur(a.registre)
        if a.mode == "temoin":
            ref_9bis = None
            if a.controle_9bis:
                try:
                    ref_9bis = charger_depot_9bis(a.controle_9bis, a.registre)
                except RuntimeError as ex:
                    sys.exit(str(ex))
            else:
                JRN("9bis", "aucun --controle-9bis : le controle sera NON JOUE (a deposer avec la prediction, N-70)")
            L = executer_temoin(a.registre, sortie, mod, ref_9bis=ref_9bis)
        else:
            if a.porte_temoin is None:
                sys.exit("ARRET PORTE (gel alpha 5) : --porte-temoin exige, le temoin passe avant tout run alpha.")
            porte = lire_porte_temoin(a.porte_temoin)
            if porte["statut"] != "REEL":
                sys.exit("ARRET PORTE : le temoin cite n'est pas un run REEL (statut %r)." % porte["statut"])
            L = executer_alpha(a.registre, sortie, mod, porte)
        statut = "REEL"
    s_etoile_g, _ = lire_carte(a.registre)
    JRN("BANC", "banc des gardes rejoue a la fin du run (D-b-3) :")
    ok_g, S_g, demontrees = banc_gardes(s_etoile_g, mod=mod)
    L["banc_gardes"] = {"ok": ok_g, "n": len(S_g), "demontrees": sorted(demontrees)}
    L = ne_joue_pas(L, L["comptes"], enumerer_gardes(a.registre), demontrees)
    ecrire_resultats(sortie, a.mode, L, statut, brut)
    ecrire_ascii(os.path.join(sortie, "journal_%s.txt" % a.mode), "\n".join(JRN.lignes))
    ecrire_manifest(sortie)
    if statut == "PREVOL":
        arret_prevol_si_fautes(L.get("prevol_fautes", []))
    JRN("FIN", "%s : %s -- %.1f s" % (a.mode, L["verdict"], time.perf_counter() - t_debut))


if __name__ == "__main__":
    main()
