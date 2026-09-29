# NOTE MACHINE 1 -- GEL v11 / INSTRUMENT v17 : LES DEUX RESERVES DU v10 PRISES, LE FAIT DE FOND ECRIT ;
# RELEVE DU DELTA 92 ; CE QUE JE RECOMMANDE A L'OPERATEUR
# machine 1, v1, 29/09/2026. Classe 3 (gel : classe 1 a la certification). PB-1 : v10, v16 non edites.

## 1. LE RELEVE DU DELTA 92 (clone frais 09baf5c, plafond 92, 1056 fichiers)
  L'acte (0a526d04fd9a8bda), le gel v9, le v15 et la feuille de perimetre deposee (6afb296dadf14539)
  sont a leur canon. La feuille deposee rejouee sur l'acte au nouveau HEAD : 73 empreintes citees,
  73 AU REGISTRE, 0 non resolue -- le contreseing 71d410cd531d06ab y compris ; il ne reste rien a
  deposer ; les deux controles qui mordent sont ses assertions d'avant depot, comme au 90 et au 91.
  La reserve du delta 92 est close. L'erratum machine 2 sur son lot de contreseing est recu : le
  registre porte la version qui a derive les 268 pieces ; rien de faux au registre.

## 2. LE GEL v11 (ac398dc92badbdc5) = v10 certifie + 7 hunks
  E-v10-1 : la base du 92 se verifie par sa TABLE (six lignes, 1e-12 = l'arrondi de la table) ;
    le v11 se reconstruit IDENTIQUE AU BIT avec la base de machine 2 et avec la mienne -- verifie.
  E-v10-2 : le compte du v10 (41) est explique dans l'en-tete du v11 : 38 appliques, 3 fragments
    sans ancre (h19, h20, s12), benins ; le v11 rend "7 hunks appliques, sans ancre : aucun".
  FOND : la mesure de A est reecrite. S(p) est un SYSTEMATIQUE DE FENETRE (fait de machine 2,
    ce_qui_borne_A, 7 controles), rejoue chez moi sur mes series du 92 : sous M1 a p = 4 et 5,
    l'ecart lnA_R(1.20) - lnA_R(1.05) est positif aux six (p, w2). ET J'AJOUTE CE QUE MACHINE 2
    N'AVAIT PAS MESURE : sous M2 a p = 4 et 5 l'effet NE DISPARAIT PAS (+5.3e-09, +4.8e-09,
    +1.2e-09 ; +6.4e-09, +8.5e-10, -1.2e-10, S double) -- ce n'est pas le mode libre qui le
    porte a ces degres, c'est la composition de la fenetre ; l'ajuster n'y change rien ; a p = 7
    M2 le mele parce que le mode y domine. A(p) est donc rendu avec une BORNE de systematique,
    pas une incertitude, le biais (~1.6e-09, sept a neuf fois delta_p) borne et non retire ;
    prediction (d) neuve sur le SIGNE du systematique a n = 21 (positif aux six sous M1 a p = 4, 5 ;
    mele a p = 7 sous M2). Le retrait du biais est un chantier d'apres-run.
  Instrument v17 (f914156a2c341f4b) = v16 + pin v11 et version, aucun code. Sur machine 1 :
  selftest 103/103, banc 58/58, pre-vols branche 5 (temoin, alpha). lecture_v10 inchangee : (d)
  se lit dans ses lnA_R par modele, deja rendus.

## 3. CE QUE JE RECOMMANDE, ET CE QUI EST A TOI
  Machine 2 prescrit un troisieme indice c AVANT le run, pour extrapoler et retirer le biais. Je
  ne le suis pas, pour deux raisons mesurees : (i) l'extrapolation en c n'a pas de limite definie
  -- c est une condition initiale, A n'en depend pas en physique, et l'effet est celui de la
  grille et de la fenetre, pas de c ; (ii) un troisieme c change le plan (27 cellules, comptes,
  tables, scenarios) et repousse le run. Le v11 borne le biais et predit son signe ; le run rend A
  a 4e-09 avec sa borne, et les quatre predictions. Le chantier "fenetre" (moyenne sur le decalage
  de grille, comme C4 l'a mesure a 1.3 pour cent ; ou troisieme c) se decide APRES, sur les trois
  niveaux du run. Si tu preferes le troisieme c d'abord, c'est un v18 et un v12 : dis-le.

-- FIN note_machine1_gel_v11_banc_v17_v1 --
