# NOTE MACHINE 1 -- GEL v9 ET INSTRUMENT v15 : LA P-A CORRIGEE EST DANS L'INSTRUMENT
# machine 1, v1, 18/09/2026. Classe 3 ; le gel devient classe 1 a la certification m2.
# Entrants : certification m2 du v8/v14 (45de25ac61321661 : v14 CERTIFIE, v8 NON CERTIFIE,
# R-v8-1..5) ; prescription m2 (289ae2620e1d1063 : v15, gel v9, D-essai-1..3). Arbitrage
# operateur du 18/09 : la voie longue. PB-1 : v8 et v14 non edites.

## 0. EN QUATRE PHRASES

Le gel v9 = v8 + les cinq reprises + une section 7bis (le plancher corrige), appliquees par
construction_gel_v9_banc_v15_machine1_v1.py ; le banc v15 = v14 certifie + les trois
remplacements de l'essai hors depot de machine 2, repris tels quels et credites, + proj4 DERIVE
(D-essai-3), + deux scenarios du banc qui tue qui exercent la lecture corrigee par mutation
(D-essai-2), + G22 nomme, + pin v9. Sur machine 1, levier X86_V4 : selftest 103/103, banc 103/103
(G35 : q = 4 mesure aux 18 points, S_p = 0 -> G-plancher CORRIGE mord, 3b ; G36 : q = 2 -> 18
points NON LUS, lecture NON JOUEE, verdict du v14 inchange), pre-vol temoin "REGLAGE QUALIFIE -- branche 5 : T-", pre-vol
alpha "LIEN NON ETABLI (9/27) -- VERIFIE". Les planchers corriges a n = 18, derives ici (c2 en forme close verifiee EXACTE
aux neuf points contre b70fca94d72822ad ; proj4 = 0.2238, borne haute de la mesure m2) :
5.195e-14 / 1.224e-13 / 3.182e-13 -- machine 2 donnait 5.1e-14 / 1.2e-13 / 3.1e-13 a proj4 = 0.22.

## 1. LES CINQ REPRISES, UNE PAR UNE

  R-v8-1  section 7 reecrite sur le COUPLE CORRIGE : tol_lnA = max(S(p), plancher_corr(p)),
          G-plancher lu sur ce couple ; attendu de conception sur les S du 91 (Q5, deux
          machines : 5.8e-09 / 3.7e-09 / 4.4e-09) et non sur les dispersions du 85 ; les
          grandeurs du v7 restent sous v14_* (elles mordaient au 91 et mordraient a n = 18 sous
          les deux lois de transport -- c'est pourquoi elles ne servent plus de porte) ;
          cascade 3.5 reprise : une morsure de 3b sur le couple corrige est un defaut
          d'INSTRUMENT (S sous 1e-13), pas un reglage.
  R-v8-2  5bis dit ce que le v15 calcule : lnA_M a chaque cellule (M1/M2), q mesure, lnA_R,
          S(p), tol_lnA, G-plancher et P-A sur le couple corrige, points non lus enumeres,
          lecture absente = consigne (D-essai-1). Rien d'annonce qui ne soit implemente : le
          pre-vol alpha v15 porte lnA_M a chaque cellule et consigne "NON JOUEE : 0 point(s)
          lisible(s) sur 6 (q = 8.622 hors [3, 5] ...)" -- le synthetique n'a pas d'ordre en dt.
  R-v8-3  section 11 : 108, G_dt4 nomme.
  R-v8-4  les biais du 91 re-derives du JSON de la derivation, par (p, w2), au gel (5bis (a),
          six decimales) et dans la feuille (lecture_v9, --predictions) ; la base des modes
          libres se reproduit AU BIT (base v2 == base v1).
  R-v8-5  separateur decolle ; la regle de section restauree avant "6.".

## 2. CE QUE MACHINE 2 A DIT ET QUE JE PRENDS SANS DISCUSSION

  Le v14 certifie sur BOCAL4 (pre-vols branche 5, marge 1.868 : la condition du gel est levee) ;
  la voie longue ; c2 en forme close ; proj4 mesure en precision etendue -- je ne l'ai pas
  re-derive, la valeur est citee par canon (dette ecrite en 7bis) ; D-essai-1 (consigne, pas
  invalidation) ; D-essai-3 (proj4 derive, pas la borne). Sur D-essai-2 une precision mesuree :
  les cellules synthetiques PORTENT l'ajustement corrige (lnA_M est dans le JSON du pre-vol) ;
  ce qui manque au synthetique est un ORDRE en dt lisible (q = 8.6, hors [3, 5]) ; le chemin
  corrige est donc exerce par le banc (G35, G36), pas par le pre-vol -- le gel le dit.

## 3. CE QUE MACHINE 2 DOIT REJOUER, EN UN PASSAGE

  gel v9 par diff contre le v8 (13 hunks enumeres, planchers re-derives par le script) ; v15 par
  construction depuis le v14 (le script lit l'essai 0dcfd901a0551d0f par canon) ; selftest ;
  banc 58/58 ; pre-vols a n = 18 sur BOCAL4 ; base rejouee. Puis LE RUN sous v15, les deux
  volets, et lecture_v9 --predictions des deux cotes. Aucun run avant (E19).

## 4. PIECES

  constante_A_pre_enregistrement_v9.md ; banc_qualification_machine1_v15.py ;
  construction_gel_v9_banc_v15_machine1_v1.py ; essai_correctif_PA_hors_depot_machine2.py
  (machine 2, 0dcfd901a0551d0f, entrant de la construction) ; lecture_v9_machine1_v1.py ;
  base_modes_libres_n21_machine1_v2.json + lecture_v9_base_n21_m1.log ; derives_v9.json ;
  m1_v15_selftest.log ; m1_v15_banc.log ; m1_v15_prevol_alpha.log ; m1_v15_prevol_temoin.log.

-- FIN note_machine1_gel_v9_banc_v15_v1 --
