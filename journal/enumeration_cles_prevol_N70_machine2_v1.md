ENUMERATION DES CLES DU PRE-VOL -- N-70 -- MACHINE 2 -- v1
==========================================================
Plume : machine 2. Se DEPOSE AVANT le run du volet T.
Ancree sur le JSON du pre-vol temoin, instrument v8
4d8882a2223a5c74, gel temoin v11 a2e7ef3e237c5acf.

TOUT CE QUI SUIT EST DERIVE, RIEN N EST TAPE : le perimetre est
LU du depot 9bis (ses cles de reference), les exemptions sont
LUES de son champ "exemptes", et les trois classes sortent de la
MESURE decrite en 2. Garde de partition verifiee a l ecriture :
exemptes + mordantes + identiques == perimetre, et
perimetre + hors == total.
E18 : aucun numero pris, aucun propose.

=========================================================
1. LE PERIMETRE, ET D OU IL VIENT
=========================================================

  depot 9bis          c4310e33da6b9759
  reference du depot  runs/run_temoin_delta85/resultats_temoin.json
  cles de reference   T1 T1b T3a T3b
  exemptions declarees ['duree_s']

  feuilles du JSON de pre-vol ............ 856
  DANS le perimetre 9bis ................. 247
  HORS perimetre, par construction ....... 609
    (dont /T2 : le reglage prime le re-exerce ; hors perimetre
     declare, gel v11 9bis)

=========================================================
2. LA REPRODUCTIBILITE, MESUREE AVANT QUE LA PREDICTION VAILLE
=========================================================

N-70 exige la mesure avant la prediction. Deux mesures :

  (a) DEUX PRE-VOLS, MEME MACHINE, meme commande :
      4 feuilles instables sur 856 --
        /T1b/recherches/a/duree_s
        /T1b/recherches/b/duree_s
        /T1b/recherches/c/duree_s
        /meta/date_utc
      -> ce sont EXACTEMENT les feuilles non deterministes, et
         elles sont toutes couvertes par les exemptions declarees.

  (b) DEUX MACHINES (Linux / Windows), meme instrument, meme
      commande : 96 feuilles divergent sur 856.
      Dans le perimetre : 7, dont 3 exemptes.

=========================================================
3. LES TROIS CLASSES
=========================================================

  PREDITES IDENTIQUES .... 240
  EXEMPTES ............... 3
  **NON PREDITES** ....... 4
  ---------------------------
  perimetre .............. 247

EXEMPTES (enumerees, et couvertes par le depot) :
    /T1b/recherches/a/duree_s
    /T1b/recherches/b/duree_s
    /T1b/recherches/c/duree_s

**NON PREDITES -- ET C EST LA TROUVAILLE DE CETTE ENUMERATION** :
    /T1/A/W_integrales/tol_int
       moi   0.008578984888782988
       elle  0.008578984888782986   (1 pas representable(s))
    /T1/A/W_integrales/tol_int_sur_1
       moi   0.008578984888782988
       elle  0.008578984888782986   (1 pas representable(s))
    /T3a/A/tol_int
       moi   0.008578984888782988
       elle  0.008578984888782986   (1 pas representable(s))
    /T3a/A/tol_int_sur_1
       moi   0.008578984888782988
       elle  0.008578984888782986   (1 pas representable(s))

PREDITES IDENTIQUES : les 240 autres cles du perimetre. Elles se
comparent AU BIT a la reference deposee ; tout ecart sur l une
d elles -> NON CONCLUANT D INSTRUMENT avant toute lecture.
Enumeration complete en annexe A.

=========================================================
4. CE QUE LA MESURE OBLIGE A DIRE -- LE RUN N EST PAS
   OPPOSABLE SUR N IMPORTE QUELLE MACHINE
=========================================================

Les 4 cles non predites portent toutes la MEME grandeur :

    tol_int = log2( (1+b) / (1+b/2) ),   b = sqrt(omega2) * dt

b vaut 0.012 et il est IDENTIQUE AU BIT des deux cotes. L ecart
nait de log2 et sqrt -- la bibliotheque mathematique, non
normalisee au bit. **Meme famille que le x**3 du champ de forces**,
a l interieur du perimetre cette fois.

ET LA REFERENCE DEPOSEE TRANCHE DEJA, SANS QUE PERSONNE
NE L AIT CHOISI :

    registre/runs/run_temoin_delta85  ->  0.008578984888782988
    machine 2 (Windows) .................  0.008578984888782988  ==
    machine 1 (Linux) ...................  0.008578984888782986  !=

**Le depot 9bis porte la valeur de machine 2.** Un run du volet T
execute sur machine 1 ferait donc mordre le controle de custody
sur 4 cles du perimetre -- NON CONCLUANT D INSTRUMENT avant
toute lecture, et pour une raison qui n a rien de physique.

TROIS ISSUES, ET LE CHOIX N EST PAS A MA PLUME :

  (a) LE RUN SE JOUE SUR MACHINE 2. Aucun texte ne bouge. Mais
      c est une contrainte SILENCIEUSE aujourd hui : elle n est
      ecrite nulle part, et le present document la rend visible.
  (b) LES 4 CLES ENTRENT AUX EXEMPTIONS. Elles ne sont pas des
      durees : ce sont des tolerances mesurees. Les exempter
      affaiblit le controle -- a peser, pas a faire par confort.
  (c) LE CONTROLE 9bis ACQUIERT UNE TOLERANCE pour les cles
      portant un appel libm -- meme remede que la clause 7 (i),
      autre patient. C est la seule issue qui ne cache rien,
      et la plus couteuse.

Je NE tranche PAS : arbitrage operateur. Mais **aucune des trois
ne peut rester implicite** : sans decision ecrite, le run est
opposable ou non selon la machine ou il tourne, et personne ne
l aura decide.

=========================================================
5. CE QUE CETTE ENUMERATION NE FAIT PAS
=========================================================

Elle ne prend aucun numero (E18) et ne depose rien -- elle est LA
PIECE A DEPOSER, pas le depot. Elle ne predit RIEN sur /T2 :
hors perimetre par construction, et le pre-vol y joue un moteur
factice (N-62). Elle ne prononce aucun verdict du volet T. Elle
ne tranche pas 4.

=========================================================
ANNEXE A -- LES 240 CLES PREDITES IDENTIQUES
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
  /T1/A/W_integrales/integrales/N/ecart_a_4
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
  /T3a/A/integrales/N/ecart_a_4
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

-- FIN enumeration_cles_prevol_N70_machine2_v1 --
