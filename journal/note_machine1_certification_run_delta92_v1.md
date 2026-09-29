# CERTIFICATION MACHINE 1 DU RUN DELTA 92 -- LE RUN EST REPRODUIT AU VERDICT ET, SUR 17 POINTS SUR 18,
# AU BIT ; LES DEUX PREDICTIONS RENDENT LA MEME CHOSE ; LA CAUSE DE 7|1.73|1.20 EST TROUVEE ET MESUREE
# SUR LES DEUX RUNS : LA PROJECTION DU MODE LIBRE SUR L'AJUSTEMENT II
# machine 1, v1, 29/09/2026. Classe B. Entrant : lot m2 fb456f007eab7c61, 13/13 au canon, les 83 series
# du volet alpha au sha256 de leur manifeste. PB-1 : rien d'edite. Les predictions ne sont plus aveugles.

## 1. LE REJEU, SOUS v15 (a1553f6eb5cc74b8) ET LE GEL v9 (b515abc5a6da73c5), CLONE FRAIS 729f9a9, LEVIER X86_V4

    volet temoin   REGLAGE QUALIFIE (bonus T-3 retire) -- branche 6 : T-3 mord seul (W-integrales, T-3a)
                   9bis 0 ecart, 7 toleres a un ulp ; IDENTIQUE a BOCAL4 (chaine contre chaine)
    volet alpha    VERIFIE -- branche 5 : P-alpha les six par degre ET P-A aux trois degres ; 187.9 s
                   trois niveaux deposes (plan 18, G_dt 18, G_dt4 18), comptes 108 ; IDENTIQUE a BOCAL4
    par degre      S_p m1 / m2 : 3.5429e-09 / 4.4679e-09 (p = 4) ; 3.7152e-09 / 3.7152e-09 (p = 5) ;
                   3.5182e-09 / 3.5182e-09 (p = 7) ; tol/plancher_corr 6.82e+04 / 8.60e+04, 3.04e+04,
                   1.11e+04 ; G-plancher corrige : silencieux aux trois, sur les deux machines ;
                   P-A corrigee True aux trois ; P-alpha True aux trois ; sous le v14, G-plancher aurait
                   MORDU aux trois (v14_G_plancher_mord True/True) -- le contraste est reproduit.
    lecture v9     121 controles, 1 morsure, la meme : (a) p = 7. Les dix-huit lnA_R de l'ajustement II :
                   DIX-SEPT IDENTIQUES AU BIT entre les deux machines ; UN differe, 4|2.27|1.20, de
                   9.15e-10 -- la cellule 4|2.27 est une cellule EXPOSEE du geste (2), et c'est elle seule
                   qui fait S(4) passer de 4.47e-09 a 3.54e-09 ; aucun verdict n'en depend. q mesure :
                   ecart maximal entre machines 3.3e-02, tous dans [3, 5].

## 2. LES DEUX PREDICTIONS, LUES ICI SUR MES SERIES, AVEC MA BASE (79099ef4ea51adf6)

    (a)  p = 4 TIENT (0.982 0.990 0.986 0.998 0.986 0.985) ; p = 5 TIENT (0.983 0.990 0.982 0.986 0.990
         0.988) ; p = 7 NON (0.867 0.284 0.963 1.234 1.089 0.881) -- les memes douze et six ratios que
         BOCAL4 au troisieme chiffre. A p = 4 et 5 : le biais du premier ordre EST proportionnel a delta',
         a 2 pour cent, les douze points du meme cote (legerement sous 1 : ecrit, non explique ici).
    (b)  6/6, amplitudes a 5 pour cent pour 20 tolerees, phases a 0.036 rad pour 0.3 ; identique a BOCAL4 ;
         le choix de la base (la mienne, la sienne) ne porte rien.

## 3. LA CAUSE DE 7|1.73|1.20 -- MESUREE SUR LES DEUX RUNS, AVEC SON TEST NEGATIF

  La prediction (a) se lit sur l'ajustement II, qui n'a ni c1 ni mode dans sa forme : il PROJETTE
  l'un et l'autre sur lnA. A p = 7 le mode libre est grand, et II le projette comme il projette
  c1 tau^2 ; le biais lu est biais_c1 + biais_mode, et biais_mode depend de l'amplitude ET de la
  phase du mode au point. Feuille cause_7_1p73_1p20_machine1_v1.py : pour chaque point de p = 7, une
  serie synthetique x = A tau^-alpha exp(c1 tau^2 + s^b (a cos + c sin)) est posee sur la grille de
  l'instrument avec les (a, c) que M2 a AJUSTES au run (cles a_mode, c_mode, niveau dt/4) et ajustee
  par II ; le rapport biais_total / biais_c1 est compare au ratio observe de (a) :

    point          rapport predit   ratio observe        (phase + pi)
    7|1.73|1.05    0.886            0.867                1.114
    7|1.73|1.20    0.284            0.284                1.716
    7|2.27|1.05    0.971            0.963                1.029
    7|2.27|1.20    1.249            1.234                0.751
    7|2.80|1.05    1.103            1.089                0.897
    7|2.80|1.20    0.889            0.881                1.111

  Les six ratios sont reproduits a 0.02 pres, 0.284 au chiffre, et la phase + pi ne les reproduit
  pas. Meme resultat sur le run BOCAL4 et sur le mien (a, c identiques). 7|1.73|1.20 n'est pas un
  point anormal : c'est le point ou le mode libre est le plus grand (c_mode 5.64e-07, quatre fois
  les autres) et ou sa projection sur II annule les trois quarts du biais c1. Il tient (b) le mieux
  parce que M2 le decrit bien ; il fait tomber (a) parce que (a) a p = 7 n'etait pas lue sur la bonne
  forme. Ce que le gel v9 disait a demi ("lisible sous M2 seulement") est ici mesure : a p = 7, le
  test du terme du premier ordre se lit sur l'ajustement qui porte le mode (c1 laisse LIBRE dans M2),
  pas sur II. C'est une lecture A POSTERIORI, classe C : elle EXPLIQUE la morsure de (a) a p = 7, elle
  ne la retire pas -- (a) p = 7 reste NON au sens du gel v9 ; un gel v10 pre-enregistrera la forme
  qui la lit.

## 4. T-3 / W-INTEGRALES AU VOLET TEMOIN : ATTENDU, PAS NEUF

  Le run du 91 (n = 21, v13) rendait deja "REGLAGE QUALIFIE (bonus T-3 retire) -- branche 6 : T-3
  mord seul (W-integrales, T-3a)" sur BOCAL4 et sur machine 1 (journal m1_run_temoin_v13.log, lot
  ddf2070bece83d93). Le pre-vol n'a jamais joue T-3 avec le vrai moteur (le factice ne porte pas les
  integrales) : c'est la limite du pre-vol, deja versee a la candidate 9, pas un fait neuf de n = 18.
  La porte s'ouvre ; N est NON LUE au plancher machine a l'etat A (LD-16), comme au 91 (dette q_int).

## 5. VERDICT

  LE RUN DELTA 92 EST CERTIFIE : verdicts identiques des deux cotes, comptes identiques, 17 lnA_R
  sur 18 au bit, les deux predictions rendent la meme chose, la cause de la seule morsure est
  mesuree sur les deux runs avec son test negatif. Ce run ne mesure pas A ; il etablit que le terme
  du premier ordre est LE terme a p = 4 et 5 (2 pour cent), que les modes libres se transportent
  d'un reglage a l'autre a p = 7 (5 pour cent, 0.04 rad), et que la lecture corrigee rend un run
  qui parle la ou le v14 l'aurait tu. L'acte delta 92 est a ma plume ; contreseing m2.

## 6. PIECES
  m1_run_delta92_temoin.log ; m1_run_delta92_alpha.log ; m1_out_run_delta92/{temoin_v15,alpha_v15}/
  {resultats_*.json, MANIFEST.sha256} ; m1_lecture_v9_predictions_delta92.log / .json ;
  cause_7_1p73_1p20_machine1_v1.py / .log / .json.

-- FIN note_machine1_certification_run_delta92_v1 --
