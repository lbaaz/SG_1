ENUMERATION DES CLES DU PRE-VOL -- N-70 -- MACHINE 2 -- **v2**
===============================================================
Plume : machine 2. Se DEPOSE AVANT le run du volet T.
Ancree sur le JSON du pre-vol temoin, instrument v8
4d8882a2223a5c74, gel temoin v11 a2e7ef3e237c5acf + son erratum
7 (i). SUPERSEDE la v1 (4ef8235b16f26210), qui n est PAS editee
(PB-1) : la v1 reste citable, elle porte une classe de moins.

CE QUI CHANGE, ET POURQUOI. La contre-derivation machine 1
(aa98fa8b4ba921d8) a leve une classe que ma v1 ignorait : DEUX
cles du perimetre de pre-vol N EXISTERONT PAS au run. Ma v1 les
classait PREDITES IDENTIQUES -- **une prediction d identite sur
des cles qui n existeront pas**. Verifie chez moi, et la regle
qui les gouverne est DERIVEE ci-dessous, pas recopiee.

MA FAUTE, NOMMEE. J avais mesure DEUX choses -- la stabilite sur
ma machine, l accord entre machines -- et omis la troisieme :
**la PRESENCE dans la reference contre laquelle la prediction se
fait**. Une prediction d identite presuppose l existence, et je
n avais jamais compare le pre-vol a la REFERENCE. La lecon est
celle de D-v5-1, deplacee d un cran : *une cle se predit AVEC son
regime, comme une mesure se fige avec sa lecture.*

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

Le mecanisme, en clair : au PRE-VOL le moteur est factice et ses
derives sont larges -- N-A PASSE, donc ecart_a_4 est emise. Au RUN
REEL, N-A tombe sous le plancher machine (LD-16) : NON LUE, et la
cle n existe pas. Le pre-vol emet donc DEUX cles que le run
n emettra pas, et ce n est pas un defaut : c est le regime.

=========================================================
2. LE PERIMETRE, ET LES DEUX COMPTES QU IL FAUT DISTINGUER
=========================================================

  depot 9bis, cles de reference ... T1 T1b T3a T3b
  exemptions declarees ............ ['duree_s']

  feuilles du JSON de PRE-VOL ..................... 856
  perimetre au PRE-VOL ............................ 247
  **perimetre au RUN** ............................ **245**
  perimetre de la REFERENCE deposee ............... 245
    -> run == reference : **le DEPOT est sain, la custody ne
       verra rien**. C est l ENUMERATION qui etait fausse, pas
       le depot. (Constat machine 1, verifie ici.)

=========================================================
3. LES QUATRE CLASSES
=========================================================

  PREDITES IDENTIQUES ....... 238
  EXEMPTES .................. 3
  NON PREDITES .............. 4
  **PREDITES ABSENTES** ..... 2   (classe NEUVE, v2)
  ------------------------------
  perimetre au pre-vol ...... 247
  moins les absentes ........ 245 = perimetre au RUN

**PREDITES ABSENTES** -- emises au pre-vol, ABSENTES au run :
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

NON PREDITES (inchangees depuis la v1, et contre-derivees par
machine 1 a 1.0 pas chacune avec son compteur v8) :
    /T1/A/W_integrales/tol_int                      1 pas
    /T1/A/W_integrales/tol_int_sur_1                1 pas
    /T3a/A/tol_int                                  1 pas
    /T3a/A/tol_int_sur_1                            1 pas

PREDITES IDENTIQUES : les 238 autres. Elles se comparent AU BIT a
la reference deposee ; tout ecart -> NON CONCLUANT D INSTRUMENT
avant toute lecture. Enumeration complete en annexe A.

=========================================================
4. CE QUI NE CHANGE PAS -- LA TROUVAILLE DE LA v1 TIENT
=========================================================

Les 4 cles NON PREDITES sont inchangees, et machine 1 les a
CONTRE-DERIVEES independamment : meme quatre cles, 1.0 pas
chacune, meme sens -- le depot porte la valeur machine 2.
`tol_int = log2((1+b)/(1+b/2))`, `b` identique au bit des deux
cotes : **la libm, a l interieur du perimetre**.

**Les trois issues restent entieres, et le choix reste a
l OPERATEUR** : (a) le run se joue sur machine 2 ; (b) les quatre
cles entrent aux exemptions ; (c) le controle 9bis acquiert une
tolerance pour les cles portant un appel libm. Sans decision
ecrite, le run est opposable ou non selon la machine ou il
tourne, et personne ne l aura decide.

=========================================================
5. CE QUE CETTE ENUMERATION NE FAIT PAS
=========================================================

Elle ne prend aucun numero (E18) et ne depose rien -- elle est LA
PIECE A DEPOSER. Elle ne predit aucune VALEUR : le pre-vol est un
factice (N-62), il fournit la LISTE des cles et leur regime, les
valeurs viennent de la reference. Elle ne predit rien hors
perimetre (/T2 compris, hors perimetre par construction). Elle ne
tranche pas les trois issues de 4. Elle n edite pas la v1.

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

-- FIN enumeration_cles_prevol_N70_machine2_v2 --
