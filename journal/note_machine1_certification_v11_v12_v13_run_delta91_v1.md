# CERTIFICATION DES INSTRUMENTS v11, v12 ET DU RUN DELTA 91 -- LE RUN EST REPRODUIT SUR MACHINE 1,
# MAIS SEULEMENT SOUS UN v13 : LE 9bis DU v12 MORD D'UN ULP ENTRE LES DEUX LIBM (D-v12-1)
# machine 1, v1, 13/09/2026. Classe 1. PB-1 : rien d'edite ; v11 et v12 conserves, gel v7 non touche.
# Lot m2 41208ad7ac1293cc recu 23/23 au canon. Fait verse contre moi : mon premier rejeu du v12 a
# ete lance avec la sortie DANS l'arbre recu ; l'instrument l'a versionne (D-I-2), rien n'est
# perdu, les deux repertoires de m2 ont ete remis a leur nom et resolvent a leurs canons
# (8d4c76d38726baf1, edec88c7a9f3faf2) ; mes sorties vivent ailleurs (out13_m1/).

## 1. v11 ET v12 -- CERTIFIES COMME INSTRUMENTS

    constructions rejouees au bit : v10 -> v11 a9f3fa1d639107d2, v11 -> v12 2c4345515bb02325.
    v12 sur machine 1 (levier X86_V4) : selftest 103/103 ; banc qui tue 56/56.
    D-v10-1 (tuple contre liste dans le 9bis) et D-v11-1 (jumelle non armee) : pris ; leurs
    feuilles de mesure (11/11, 20/20) et la lecture du run (35/35) sont LUES, non rejouees ici
    (chemins de son poste : out_run_delta91/temoin/, alpha/) -- a rejouer au releve du depot.

## 2. LE RUN SOUS v12 SUR MACHINE 1 : NON CONCLUANT D'INSTRUMENT -- D-v12-1

    Volet T, meme reglage, meme 9bis (depot c4310e33da6b9759, reference BOCAL4) :
    NON CONCLUANT D'INSTRUMENT -- 9bis : 7 ecart(s) sur cle du perimetre, prononce AVANT toute
    lecture ; porte de alpha fermee. Les sept, tous a UN ulp : /T1/A et /T3a/A tol_int et
    tol_int_sur_1 (0.008578984888782986 contre ...988), /T1/B disp_y, tol_R, tol_R_sur_q_moins_1.
    D-v12-1 (instrument ; plume des deux machines ; numero propose) : le gel v7, section 5,
    decision (ii) issue (c), dit que les cles de classe EXPOSEE-LIBM se comparent entre machines
    A 2 ULP ; le 9bis du v12 compare AU BIT toute feuille. Et la classe est plus large que son
    enumeration au gel (tol_int, tol_ordre) : une dispersion (disp_y) et une tolerance (tol_R)
    passent aussi par la libm. Sur BOCAL4, machine de la reference, 0 ecart PAR CONSTRUCTION :
    c'est l'issue (a) de N-70 -- la contrainte muette -- que le run a rendue visible. Aucun run
    d'une autre machine ne pouvait passer ce 9bis.

## 3. v13 = v12 + LEVEE DE D-v12-1 -- ET LE RUN EST REPRODUIT

    construction_banc_v13_machine1_v1.py <v12> <v13> : 6 remplacements a ancre unique ; pin v7
    inchange ; canon 1ac295648490a86c. Toute feuille FLOTTANTE finie du perimetre 9bis se
    compare a 2 ulp (2^-52 relatif) ; les ecarts toleres sont ENUMERES dans le JSON
    (toleres_ulp) et au journal ; entiers, chaines, booleens, longueurs, cles : au bit.
    selftest 103/103 ; banc qui tue 56/56 (G28 "ecart au perimetre" mord toujours).
    RUN TEMOIN v13, machine 1, levier X86_V4 : REGLAGE QUALIFIE (bonus T-3 retire) -- branche 6,
      T-3 mord seul ; 9bis 0 ecart, 7 toleres a 1.0 ulp ; custody 4/4 ; W-comptes 41.
      JSON out13_m1/temoin_v13/resultats_temoin.json. Contre le JSON BOCAL4 : 17 feuilles
      different hors durees/meta/9bis, toutes de la classe EXPOSEE-LIBM (tol_int, tol_int_sur_1,
      disp_y, tol_R, tol_R_sur_q_moins_1, tol_ordre, tol_ordre_sur_1, p_obs).
    RUN ALPHA v13, porte lue sur mon fichier temoin : NON CONCLUANT DE PLANCHER -- branche 3b,
      G-plancher MORD aux degres [4, 5, 7] ; 198 s. Contre le JSON BOCAL4, par degre : 60 cles
      numeriques, UNE differe -- dispersion_lnA a p = 5, 3.2503e-07 contre 3.2607e-07 (0.3 pour
      cent, 1.0e-09 absolu : la dispersion de lnA amplifie l'ulp des flots) ; P_alpha vraie aux
      trois degres des deux cotes ; G_plancher_mord aux trois des deux cotes ; rapports
      dispersion/plancher 0.869 / 0.208 / 0.042 identiques a trois chiffres.
    LES DEUX VERDICTS DU DELTA 91 SONT DESORMAIS CEUX DES DEUX MACHINES, le run de reference
    restant celui de BOCAL4 sous v12 (le v13 ne change que le 9bis). Le v13 est a certifier par
    machine 2 dans le meme passage que l'acte.

## 4. MA PLUME SUR LE FAIT (a) : LA CLAUSE (T) A 1.15 NE SE RELACHE PAS

    (i)  1.15 est le bas du besoin MESURE (D-t-25, 1.15 a 1.74) ; l'abaisser a 1.10 pour ouvrir
         p = 4 serait regler une porte sur le resultat qu'on veut voir -- ce que la campagne
         s'interdit, meme quand le resultat est un rapport d'instrument.
    (ii) la fenetre a p = 4 est calculee a dispersion FIXE. Or la dispersion BAISSE avec delta :
         entre le 85 (delta_0) et le 91 (delta_0/441), disp_85/disp_91 = 2.0 / 7.3 / 83 aux
         p = 4 / 5 / 7, soit des exposants 0.12 / 0.33 / 0.73 (deux points, a prendre comme tels).
         A n = 23 la dispersion a p = 4 vaudrait ~9.6e-07 contre un plancher 9.45e-07 : m = 1.02.
         Une fenetre a deux pour cent, a un seul degre, ne mesure pas A ; p = 5 et p = 7 restent
         limites par le modele de 3.5 et 17.5 fois, et davantage sous cette pente.
    (iii) le plancher est un terme de MODELE (le terme neglige de la fenetre, 3.4 : delta'
         fois le dominant). Le chemin qui ouvre les trois degres n'est pas un delta' plus petit
         -- la porte T l'interdit et le run le chiffre -- c'est de DERIVER ce terme au premier
         ordre et de le soustraire : le plancher residuel devient O(delta'^2) ~ 5e-06 x
         plancher, sous la dispersion d'un facteur 1e+04 a 1e+05 au reglage courant. C'est le
         chantier "second ordre" deja a l'horizon ; il precede tout gel v8. Le rapport 1.13 de
         P-A a p = 4 y deviendra un test, il n'en est pas un aujourd'hui.
    Le run ne contredit pas la cascade 3.5 : il la chiffre, et la reponse est un instrument
    (un modele) plus fin, pas un reglage.

## 5. POUR L'ACTE DELTA 91

    A consigner : les deux verdicts (BOCAL4 v12 ; machine 1 v13) ; P-alpha aux trois degres ;
    P-A sous tolerance de modele ; la tenaille chiffree (17.5 a dispersion fixe, plus sous la
    pente mesuree) ; D-v10-1, D-v11-1, D-v12-1 ; D-v6-1..5, D-v9-1, D-v7-1 ; la dette q_int(N)
    = 4.96 (etat B, reproduite) ; la classe EXPOSEE-LIBM etendue par mesure (erratum du gel v7,
    forme de 7 (i), sans editer le v7 ni bouger le pin) ; la plume de machine 1 sur (T).
    Aucun numero pris ; aucun delta recommande ; rien de tranche pour l'operateur.

## 6. PIECES

    construction_banc_v13_machine1_v1.py ; banc_qualification_machine1_v13.py (1ac295648490a86c)
    m1_v12_selftest.log, m1_v12_banc.log, m1_run_temoin_v12.log (D-v12-1, mesure)
    m1_v13_selftest.log, m1_v13_banc.log, m1_run_temoin_v13.log, m1_run_alpha_v13.log
    out13_m1/temoin_v13/{resultats_temoin.json, journal_temoin.txt}
    out13_m1/alpha_v13/{resultats_alpha.json, journal_alpha.txt}

-- FIN note_machine1_certification_v11_v12_v13_run_delta91_v1 --
