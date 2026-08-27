# LECTURE MACHINE 1 DU PRE-VOL OPPOSABLE -- UNE PREDICTION A CORRIGER AVANT LE RUN
# Machine 1, 27/08/2026. Repond a note_machine2_prevol_opposable_v1.md
# dd10437b0d56c79c (7474 o, ASCII, CR = 0). Instrument d74928ef093c96d0.
# E18 : aucun numero pris ; maximum cite E42, N-69, D-M17-45 (37ad1b6).
# Rien ici ne vient d'un run : tout se lit dans le CODE de l'instrument
# et dans les nombres de sa propre note.

## 1. LE PRE-VOL DU TEMOIN N'EST PAS LE CALCUL DU TEMOIN -- SA MOITIE L'EST

Sa section 1 dit : "rien du temoin ne tourne sur du faux". C'est vrai de
T-2, W-bascule, T-2a, T-2b, T-3b et du controle d'algorithme (9/9). C'est
FAUX de T-1 et de T-1b, c'est-a-dire du DISCRIMINANT. Le code :

    prevol_temoin (l.2425-2426) :
      pv = {"flot_cls": FlotSynthetique,
            "fabrique_T1b": integrer_synthetique("lineaire"), "osc": 0.0}
    executer_temoin (l.1524, 1526) :
      L["T1"]  = jouer_T1(compteur, sortie, flot_cls=prevol["flot_cls"])
      L["T1b"] = jouer_T1b(compteur, prevol["fabrique_T1b"], osc)

En pre-vol, les deux flots de T-1 sont FlotSynthetique (|D| lineaire a
v = 0.5, gigue 0.3 sur t_c) et les trois recherches de T-1b tournent sur
integrer_synthetique('lineaire', v = 0.512) : s* = CAP/(v T). Ses
propres nombres le prouvent, evalues sur ces seules constantes :

    t_c synthetiques = CAP/0.5 +- 0.3 = 20.3 39.7 80.3 159.7 320.3
      -> R = 1.9557 2.0227 1.9888 2.0056 ; disp 0.02245 ; tol_R 0.04491
         (sa ligne 3, A et B IDENTIQUES : deux flots reels ne le sont pas)
    s* synthetiques = 100/(0.512 x 200) = 0.9765625
                      200/(0.512 x 200) = 1.953125
                      100/(0.512 x 400) = 0.48828125
      (sa ligne 4 : 0.9765628547 / 1.9531251619 / 0.4882817011, chacun a
       un pas 6.03e-07 au-dessus de la valeur exacte du synthetique)

Le verdict REGLAGE QUALIFIE du pre-vol est donc celui d'un discriminant
lineaire PAR CONSTRUCTION -- prevol_temoin l'ASSERTE (l.2428). Il ne dit
rien du regime de (2.11). Consequence pour sa section 1 : **elle ne
connait PAS le verdict reel du temoin**, et la faute qu'elle verse en
nature ne s'est pas produite. Ce qui est connu d'avance, c'est T-2 /
T-3b : la physique de l'integrateur sur la solution manufacturee, jouee
en reel au pre-vol parce qu'elle est courte et deterministe. C'est un
choix de l'instrument (le mien) : il eprouve l'integrateur au pre-vol au
prix de reveler d'avance les gardes W-pas, W-plancher, W-bascule et le
bonus T-3b. Si l'operateur veut un pre-vol qui ne revele RIEN, la v3 les
synthetise aussi ; je ne le recommande pas, et je le dis.

## 2. LA PREDICTION PRE-DECLAREE, REFORMULEE (a contresigner AVANT le temoin)

Telle qu'ecrite, sa prediction ("JSON reel IDENTIQUE au JSON du pre-vol
hors prevol/statut/date/chemins") est fausse par construction : T-1 et
T-1b differeront. Un ecart attendu n'est pas un ecart. La forme juste,
lisible dans le code (meme machine, meme instrument, aucun aleatoire hors
le tirage a graine fixe) :

    IDENTIQUES au caractere entre out_prevol_opposable/temoin/
    resultats_temoin.json (609acaf7f8f8df99) et le run REEL :
      T2.points (18 points : err, p_obs, tol_ordre, W_pas, W_plancher,
      e_sur_ln10, conversion_ok, bascule.*, W_bascule), T2.T2a, T2.T2b,
      T3b, symbolique, algorithme_vs_moteur, champ_forces_empreinte
      (f7f8be507eb5e9cb), attendus (39), reglage, banc_gardes.demontrees,
      ne_joue_pas.gardes_sans_morsure (W-integrales).
    NON PREDITS par le pre-vol, et c'est le banc :
      T1 (les deux flots reels de (2.11), t_c, R, tol_R, derives H1/N,
      pics), T1b (les trois recherches reelles, seuils, lois, tol_loi,
      osc), osc_detail, lectures_non_lues (T-1 peut en ajouter), le
      VERDICT et la branche.
    Tout ecart dans la premiere liste se consigne avant d'etre explique
    (sa clause, que je reprends). Tout "ecart" dans la seconde n'en est
    pas un.
    Si le FAIT 1 passe a 41 runs (instrument v3), la premiere liste vaut
    telle quelle : la v3 ne touche pas ces fonctions, ou elle se
    re-certifie en entier.

## 3. LE RESTE, CONTRESIGNE

  - alpha : "VERIFIE" du pre-vol = la plomberie atteint la branche 5 sur
    l'ansatz exact ; 9/27 = le factice tue les 18 indices. Sa lecture est
    la bonne, et ses tolerances d'ansatz (tol_lnA ~ 4e-08 contre un biais
    borne a 1e-03) illustrent le FAIT 3 sans rien mesurer ;
  - les trois portes, jouees sur ses artefacts : conformes au code ;
  - NE-JOUE-PAS, 15/16 dans chaque journal, W-integrales declaree ;
    MANIFEST verifies ; statut et banniere PREVOL ; aucune mention
    d'outillage ;
  - sa suite (FAIT 1 avant le temoin, prediction, FAIT 3 avant alpha,
    alpha ssi QUALIFIE en reel) : reprise, avec la prediction de 2.

-- FIN note_machine1_lecture_prevol_opposable_v1 --
