# CONTRESEING DU GEL constante A v7 ET CERTIFICATION DU BANC v10 -- machine 1, v1, 13/09/2026.
# Classe 1. VERDICTS : v7 CONTRESIGNE (diff v6 -> v7 = H6..H10, construction rejouee AU BIT) ;
# v10 CERTIFIE (construction rejouee AU BIT ; selftest 103/103 ; banc qui tue 56/56 ; pre-vol
# temoin branche 5 ; pre-vol alpha LIEN NON ETABLI (9/27) VERIFIE) ; N-70 v3 jambe inter-machines
# JOUEE avec mon JSON, memes comptes. BON POUR LE RUN : volet T sur BOCAL4, puis volet A si branche 5.
# PB-1 : rien d'edite. Lot m2 f65529ea706a60d2 recu 24/24 au canon.

## 1. LE v7 -- CONTRESIGNE PAR DIFF

    v6 (847bb3bb2dd19f87) -> v7 (a2b8463372e1f906) : 7 hunks, 31 lignes (diff joint), exactement
    H6 (4.8 jumelle 2 x 400 : [748, 802] / [736, 802] / [724, 802] et [800, 852] / [800, 864] /
    [800, 876] -- re-derives ici depuis mes retards 26 / 32 / 38 et le nominal 400), H7 (section 9
    au signal 1/441 : 18.0 x 441/1024 = 7.8, 21.4 -> 9.2, 51.8 -> 22.3, puis /sqrt(6) et
    /sqrt(18) -- recalcules ici), H8 (3.2 : n = 23 mesure sur BOCAL4, branche 5 a e/seuil 1.113,
    exclu par (T) mesuree ; 3.5), H9 (11 : v11 et son erratum), H10 (provenance, titre, FIN).
    Construction de machine 2 rejouee ici sur mon v6 emis : v7 identique au bit.
    D-v6-1 a D-v6-5 : pris, sans contestation. D-v6-3 et D-v6-4 sont des fautes de ma
    re-derivation (4.8 et les rapports de 9 substitues, pas recalcules) ; D-v6-1 est exact --
    la table 3.2 venait d'une feuille hors lot ; elle est desormais dans le v7 par construction.
    D-v7-1 (machine 1 ; provenance ; NON BLOQUANT ; numero propose) : la phrase de la section 9
    "un biais persistant de 2.2e-04 a 1.6e-03 creve une tolerance a ~2e-06" vient de ma plume du
    29/08 (v4 l.482) et ses deux bornes ne se retrouvent ni au registre (delta 85, gels) ni dans
    les cles du JSON alpha du 85 que j'ai lues (P_A est un booleen ; ecart_G_dt/G_k ~ 1e-05 ;
    planchers 5.0e-04 / 6.9e-04 / 9.4e-04). L-desc n'a ni branche ni tolerance (9, "aucune
    branche, aucune tolerance") : aucun verdict n'en depend. A la prochaine version du gel, la
    phrase se re-ecrit sur une source citee : "un biais persistant de l'ordre des planchers du 85
    (5.0e-04 a 9.4e-04, cle /degres/p/plancher_lnA) creverait une tolerance a ~2e-06". Pas de
    v8 pour cela seul : le contreseing du v7 est donne tel quel, cette reserve nommee.

## 2. LE v10 -- CERTIFIE

    construction_banc_v10_machine2_v2.py rejouee sur mon v9 (9b3ec0b0c4978158) avec le v7 :
      v10 identique au bit (f65eccbfcdea91c1), 4 remplacements, pin v7 a2b8463372e1f906 / 41061.
    D-v9-1 : cause prise (SynthAlpha, round -> floor du depart de phase 2 : k tau_dom' = 4.77e-03
      < DT1 = 0.006) ; le vrai moteur n'est pas concerne (phase 1 a k tau_dom_0).
    selftest 103/103 (m1_v10_selftest.log) ; BANC QUI TUE 56/56, 17 gardes enumerees et
      demontrees, G11 et G12 mordent (m1_v10_banc.log) ; pre-vol temoin, levier X86_V4 :
      REGLAGE QUALIFIE branche 5, JSON joint (m1_v10_prevol_temoin_resultats.json) ; pre-vol
      alpha : LIEN NON ETABLI (9/27) VERIFIE, 0 faute, comme BOCAL4 (m1_v10_prevol_alpha.log).
    Mon JSON temoin contre le sien (684 feuilles) : 22 feuilles different -- durees (exemptees),
      tol_int et tol_int_sur_1, tol_ordre et tol_ordre_sur_1 a 7|1.73 et 7|2.27 (classe
      EXPOSEE-LIBM, residuelle glibc/UCRT deja mesuree au geste (2)), p_obs a 5|1.73 et
      err_rel_bascule a 7|2.80 (derives d'un e a un ulp pres) ; les 9 cellules de T-2 rendent
      les memes verdicts ; /T2 est hors perimetre 9bis par construction.

## 3. N-70 v3 -- JAMBE INTER-MACHINES JOUEE ICI

    derivation_cles_N70_machine2_v3.py, avec ses deux pre-vols, le 9bis du registre
    (journal/depot_9bis_temoin_v1.json), le run 85 et MON JSON v10 : perimetre pre-vol 247,
    run 245 ; identiques 238, exemptees 3, non predites 4, absentes 2 ; instables 4 ; jambe 2
    JOUEE (m1_N70_v3_inter_machines.log). La piece enumeration_cles_prevol_N70_machine2_v3.md
    (bbd23a2ee3421da4) est deposable sans nouvelle version.

## 4. CE QUI SUIT

    Le run : volet T sur BOCAL4 sous v7 / v10 (delta' = 1/44100) ; si REGLAGE QUALIFIE, le volet
    A ; un seul lot ; l'acte delta 91 le consigne, avec D-v6-1..5, D-v9-1, D-v7-1 et les
    defauts de forme des deux lots du jour, sans tour dedie.

## 5. PIECES

    note ; diff_gel_v6_v7_machine1.txt ; m1_v10_selftest.log ; m1_v10_banc.log ;
    m1_v10_prevol_temoin.log + m1_v10_prevol_temoin_resultats.json ; m1_v10_prevol_alpha.log
    (+ JSON si emis) ; m1_N70_v3_inter_machines.log

-- FIN note_machine1_contreseing_v7_certification_v10_v1 --
