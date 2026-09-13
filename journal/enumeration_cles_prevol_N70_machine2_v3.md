ENUMERATION DES CLES DU PRE-VOL -- N-70 -- MACHINE 2 -- **v3**
===============================================================
Plume : machine 2. Se DEPOSE AVANT le run du volet T.
Ancree sur le JSON du pre-vol temoin, instrument v10 (script brut
f65eccbfcdea91c1..., meta), gel constante A v7 a2b8463372e1f906, gel temoin v11
a2e7ef3e237c5acf + son erratum 7 (i), reglage delta' = 1/44100.
SUPERSEDE la v2 (4867dffe3392dea6, ancree sur le v8 a 1/102400),
qui n est PAS editee (PB-1). Meme regle, memes classes, meme
feuille de derivation (v3 : entrees en arguments, jambe absente
declaree NON JOUEE).

Entrees, authentifiees par canon avant lecture :
  pre-vol 1 (BOCAL4)   dcdd26486e971d1f  m2_v10_prevol_temoin_1_resultats.json
  pre-vol 2 (BOCAL4)   e02477c67d02b4dc  m2_v10_prevol_temoin_2_resultats.json
  depot 9bis           c4310e33da6b9759  depot_9bis_temoin_v1.json
  reference run 85     644240dc894c2733  resultats_temoin.json
  pre-vol machine 1    ABSENT -> jambe (2) NON JOUEE : les cles NON PREDITES
                       sont celles de la v2 (4 tol_int a appel libm), HERITEES,
                       a confirmer sur son JSON de pre-vol v10.

E18 : aucun numero pris, aucun propose.

=========================================================
1. LA REGLE D EMISSION CONDITIONNELLE -- DERIVEE
=========================================================

Sur les 16 groupes `integrales/*` des DEUX fichiers :

    **ecart_a_4 est EMISE si et seulement si l integrale est LUE**
    (statut PASSE ou MORD) ; elle est ABSENTE si le statut est
    "NON LUE (plancher, LD-16)".

  verifie 16/16 groupes, 0 contre-exemple.
    pre-vol   /T1/A/W_integrales/integrales/H1           PASSE                      EMISE
    pre-vol   /T1/A/W_integrales/integrales/N            PASSE                      EMISE
    pre-vol   /T1/B/W_integrales/integrales/H1           PASSE                      EMISE
    pre-vol   /T1/B/W_integrales/integrales/N            PASSE                      EMISE
    pre-vol   /T3a/A/integrales/H1                       PASSE                      EMISE
    pre-vol   /T3a/A/integrales/N                        PASSE                      EMISE
    pre-vol   /T3a/B/integrales/H1                       PASSE                      EMISE
    pre-vol   /T3a/B/integrales/N                        PASSE                      EMISE
    reference /T1/A/W_integrales/integrales/H1           MORD                       EMISE
    reference /T1/A/W_integrales/integrales/N            NON LUE (plancher, LD-16)  ABSENTE
    reference /T1/B/W_integrales/integrales/H1           MORD                       EMISE
    reference /T1/B/W_integrales/integrales/N            MORD                       EMISE
    reference /T3a/A/integrales/H1                       MORD                       EMISE
    reference /T3a/A/integrales/N                        NON LUE (plancher, LD-16)  ABSENTE
    reference /T3a/B/integrales/H1                       MORD                       EMISE
    reference /T3a/B/integrales/N                        MORD                       EMISE

=========================================================
2. LE PERIMETRE, ET LES DEUX COMPTES QU IL FAUT DISTINGUER
=========================================================

  depot 9bis, cles de reference ... T1 T1b T3a T3b
  exemptions declarees ............ ['duree_s']

  feuilles du JSON de PRE-VOL ..................... 848
  perimetre au PRE-VOL ............................ 247
  **perimetre au RUN** ............................ **245**
  perimetre de la REFERENCE deposee ............... 245

=========================================================
3. LES QUATRE CLASSES
=========================================================

  PREDITES IDENTIQUES ....... 238
  EXEMPTES .................. 3
  NON PREDITES .............. 4   (HERITEES de la v2 ; jambe (2) NON JOUEE)
  PREDITES ABSENTES ......... 2
  ------------------------------
  perimetre au pre-vol ...... 247
  moins les absentes ........ 245 = perimetre au RUN

STABILITE SUR MA MACHINE (jambe 1) : 4 feuilles different entre les deux
pre-vols, toutes exemptees (durees) :
    /T1b/recherches/a/duree_s
    /T1b/recherches/b/duree_s
    /T1b/recherches/c/duree_s
    /meta/date_utc

PREDITES ABSENTES -- emises au pre-vol, ABSENTES au run :
    /T1/A/W_integrales/integrales/N/ecart_a_4
       pre-vol : statut 'PASSE' -> emise
       run     : statut 'NON LUE (plancher, LD-16)' -> ABSENTE
    /T3a/A/integrales/N/ecart_a_4
       pre-vol : statut 'PASSE' -> emise
       run     : statut 'NON LUE (plancher, LD-16)' -> ABSENTE

EXEMPTES :
    /T1b/recherches/a/duree_s
    /T1b/recherches/b/duree_s
    /T1b/recherches/c/duree_s

NON PREDITES :
    /T1/A/W_integrales/tol_int                      heritee v2 (libm), a confirmer
    /T1/A/W_integrales/tol_int_sur_1                heritee v2 (libm), a confirmer
    /T3a/A/tol_int                                  heritee v2 (libm), a confirmer
    /T3a/A/tol_int_sur_1                            heritee v2 (libm), a confirmer

PREDITES IDENTIQUES : les 238 autres. Elles se comparent AU BIT a
la reference deposee ; tout ecart -> NON CONCLUANT D INSTRUMENT
avant toute lecture. Enumeration complete en annexe A.

=========================================================
4. CE QUE CETTE ENUMERATION NE FAIT PAS
=========================================================

Elle ne prend aucun numero (E18) et ne depose rien -- elle est LA
PIECE A DEPOSER. Elle ne predit aucune VALEUR : le pre-vol est un
factice (N-62), il fournit la LISTE des cles et leur regime, les
valeurs viennent de la reference. Elle ne predit rien hors
perimetre. L issue N-70 (a)(b)(c) est tranchee par le gel v7 ((c),
tolerance en ulp pour les cles EXPOSEE-LIBM) : sous ce regime les
4 cles NON PREDITES se comparent a tolerance, pas au bit.

=========================================================
ANNEXE A -- LES 238 CLES PREDITES IDENTIQUES
=========================================================

  /T1/A/D_max
  /T1/A/H1_0
  /T1/A/N_0
  /T1/A/R/0
  /T1/A/R/1
  /T1/A/R/2
  /T1/A/R/3
  /T1/A/T_0
  /T1/A/T_MAX
  /T1/A/W_croissance
  /T1/A/W_integrales/W_integrales
  /T1/A/W_integrales/b
  /T1/A/W_integrales/integrales/H1/derive_dt
  /T1/A/W_integrales/integrales/H1/derive_dt2
  /T1/A/W_integrales/integrales/H1/ecart_a_4
  /T1/A/W_integrales/integrales/H1/q_int
  /T1/A/W_integrales/integrales/H1/statut
  /T1/A/W_integrales/integrales/N/derive_dt
  /T1/A/W_integrales/integrales/N/derive_dt2
  /T1/A/W_integrales/integrales/N/q_int
  /T1/A/W_integrales/integrales/N/statut
  /T1/A/W_integrales/n_pas_dt2
  /T1/A/W_integrales/omega_max
  /T1/A/W_integrales/plafond_int
  /T1/A/W_integrales/plancher_dt2
  /T1/A/W_integrales/resolution_ok
  /T1/A/caps/0
  /T1/A/caps/1
  /T1/A/caps/2
  /T1/A/caps/3
  /T1/A/caps/4
  /T1/A/derive_H1_dt
  /T1/A/derive_H1_dt2
  /T1/A/derive_N_dt
  /T1/A/derive_N_dt2
  /T1/A/disp_y
  /T1/A/etat/0
  /T1/A/etat/1
  /T1/A/etat/2
  /T1/A/etat/3
  /T1/A/fenetre_1
  /T1/A/fenetre_q
  /T1/A/n_pas
  /T1/A/n_pas_dt2
  /T1/A/non_fini
  /T1/A/pics/0/0
  /T1/A/pics/0/1
  /T1/A/pics/0/2
  /T1/A/pics/1/0
  /T1/A/pics/1/1
  /T1/A/pics/1/2
  /T1/A/plafond_R
  /T1/A/prediction_tc4
  /T1/A/resolution_ok
  /T1/A/saturation
  /T1/A/t_c/0
  /T1/A/t_c/1
  /T1/A/t_c/2
  /T1/A/t_c/3
  /T1/A/t_c/4
  /T1/A/tol_R
  /T1/A/tol_R_sur_q_moins_1
  /T1/A/x_max
  /T1/A/y/0
  /T1/A/y/1
  /T1/A/y/2
  /T1/A/y/3
  /T1/A/y/4
  /T1/B/D_max
  /T1/B/H1_0
  /T1/B/N_0
  /T1/B/R/0
  /T1/B/R/1
  /T1/B/R/2
  /T1/B/R/3
  /T1/B/T_0
  /T1/B/T_MAX
  /T1/B/W_croissance
  /T1/B/W_integrales/W_integrales
  /T1/B/W_integrales/b
  /T1/B/W_integrales/integrales/H1/derive_dt
  /T1/B/W_integrales/integrales/H1/derive_dt2
  /T1/B/W_integrales/integrales/H1/ecart_a_4
  /T1/B/W_integrales/integrales/H1/q_int
  /T1/B/W_integrales/integrales/H1/statut
  /T1/B/W_integrales/integrales/N/derive_dt
  /T1/B/W_integrales/integrales/N/derive_dt2
  /T1/B/W_integrales/integrales/N/ecart_a_4
  /T1/B/W_integrales/integrales/N/q_int
  /T1/B/W_integrales/integrales/N/statut
  /T1/B/W_integrales/n_pas_dt2
  /T1/B/W_integrales/omega_max
  /T1/B/W_integrales/plafond_int
  /T1/B/W_integrales/plancher_dt2
  /T1/B/W_integrales/resolution_ok
  /T1/B/W_integrales/tol_int
  /T1/B/W_integrales/tol_int_sur_1
  /T1/B/caps/0
  /T1/B/caps/1
  /T1/B/caps/2
  /T1/B/caps/3
  /T1/B/caps/4
  /T1/B/derive_H1_dt
  /T1/B/derive_H1_dt2
  /T1/B/derive_N_dt
  /T1/B/derive_N_dt2
  /T1/B/disp_y
  /T1/B/etat/0
  /T1/B/etat/1
  /T1/B/etat/2
  /T1/B/etat/3
  /T1/B/fenetre_1
  /T1/B/fenetre_q
  /T1/B/n_pas
  /T1/B/n_pas_dt2
  /T1/B/non_fini
  /T1/B/pics/0/0
  /T1/B/pics/0/1
  /T1/B/pics/0/2
  /T1/B/pics/1/0
  /T1/B/pics/1/1
  /T1/B/pics/1/2
  /T1/B/plafond_R
  /T1/B/prediction_tc4
  /T1/B/resolution_ok
  /T1/B/saturation
  /T1/B/t_c/0
  /T1/B/t_c/1
  /T1/B/t_c/2
  /T1/B/t_c/3
  /T1/B/t_c/4
  /T1/B/tol_R
  /T1/B/tol_R_sur_q_moins_1
  /T1/B/x_max
  /T1/B/y/0
  /T1/B/y/1
  /T1/B/y/2
  /T1/B/y/3
  /T1/B/y/4
  /T1b/k_attendu_0
  /T1b/loi1
  /T1b/loi2
  /T1b/osc_enveloppe
  /T1b/plafond_loi1
  /T1b/plafond_loi2
  /T1b/recherches/a/CAP
  /T1b/recherches/a/T_MAX
  /T1b/recherches/a/controle_positif
  /T1b/recherches/a/detail
  /T1b/recherches/a/encadrement/0
  /T1b/recherches/a/encadrement/1
  /T1b/recherches/a/k
  /T1b/recherches/a/motif
  /T1b/recherches/a/seuil
  /T1b/recherches/b/CAP
  /T1b/recherches/b/T_MAX
  /T1b/recherches/b/controle_positif
  /T1b/recherches/b/detail
  /T1b/recherches/b/encadrement/0
  /T1b/recherches/b/encadrement/1
  /T1b/recherches/b/k
  /T1b/recherches/b/motif
  /T1b/recherches/b/seuil
  /T1b/recherches/c/CAP
  /T1b/recherches/c/T_MAX
  /T1b/recherches/c/controle_positif
  /T1b/recherches/c/detail
  /T1b/recherches/c/encadrement/0
  /T1b/recherches/c/encadrement/1
  /T1b/recherches/c/k
  /T1b/recherches/c/motif
  /T1b/recherches/c/seuil
  /T1b/regime
  /T1b/resolution_ok
  /T1b/stable
  /T1b/suit_lois
  /T1b/tol_loi1
  /T1b/tol_loi2
  /T1b/transcription_positif
  /T3a/A/W_integrales
  /T3a/A/b
  /T3a/A/integrales/H1/derive_dt
  /T3a/A/integrales/H1/derive_dt2
  /T3a/A/integrales/H1/ecart_a_4
  /T3a/A/integrales/H1/q_int
  /T3a/A/integrales/H1/statut
  /T3a/A/integrales/N/derive_dt
  /T3a/A/integrales/N/derive_dt2
  /T3a/A/integrales/N/q_int
  /T3a/A/integrales/N/statut
  /T3a/A/n_pas_dt2
  /T3a/A/omega_max
  /T3a/A/plafond_int
  /T3a/A/plancher_dt2
  /T3a/A/resolution_ok
  /T3a/B/W_integrales
  /T3a/B/b
  /T3a/B/integrales/H1/derive_dt
  /T3a/B/integrales/H1/derive_dt2
  /T3a/B/integrales/H1/ecart_a_4
  /T3a/B/integrales/H1/q_int
  /T3a/B/integrales/H1/statut
  /T3a/B/integrales/N/derive_dt
  /T3a/B/integrales/N/derive_dt2
  /T3a/B/integrales/N/ecart_a_4
  /T3a/B/integrales/N/q_int
  /T3a/B/integrales/N/statut
  /T3a/B/n_pas_dt2
  /T3a/B/omega_max
  /T3a/B/plafond_int
  /T3a/B/plancher_dt2
  /T3a/B/resolution_ok
  /T3a/B/tol_int
  /T3a/B/tol_int_sur_1
  /T3b/w1_lam1_x01/Omega2
  /T3b/w1_lam1_x01/PASSE
  /T3b/w1_lam1_x01/e
  /T3b/w1_lam1_x01/horizon
  /T3b/w1_lam1_x01/m
  /T3b/w1_lam1_x01/n_pas
  /T3b/w1_lam1_x01/periode
  /T3b/w1_lam1_x01/x0_formule
  /T3b/w1_lam1_x02/Omega2
  /T3b/w1_lam1_x02/PASSE
  /T3b/w1_lam1_x02/e
  /T3b/w1_lam1_x02/horizon
  /T3b/w1_lam1_x02/m
  /T3b/w1_lam1_x02/n_pas
  /T3b/w1_lam1_x02/periode
  /T3b/w1_lam1_x02/x0_formule
  /T3b/w1_lam1_x04/Omega2
  /T3b/w1_lam1_x04/PASSE
  /T3b/w1_lam1_x04/e
  /T3b/w1_lam1_x04/horizon
  /T3b/w1_lam1_x04/m
  /T3b/w1_lam1_x04/n_pas
  /T3b/w1_lam1_x04/periode
  /T3b/w1_lam1_x04/x0_formule

-- FIN enumeration_cles_prevol_N70_machine2_v3 --
