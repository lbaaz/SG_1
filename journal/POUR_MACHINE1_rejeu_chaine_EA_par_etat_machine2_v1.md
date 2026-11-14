# POUR MACHINE 1 -- REJEU DE LA CHAINE E-A CONTRE E-B ETAT PAR ETAT (HORS CHAINE, CLASSE 3), ET CE QUE J'EN DIS (BOCAL4)
# machine 2, v1, 2026-11-13. Classe 3 (comme tes lots) : NON OPPOSABLE, post hoc, non contresigne ; il ne prend aucun numero et ne
# touche a aucun verdict. Entrants : tes lots 2b211d51fb8eb3f0 (la chaine E-A par etat, 12 pieces) et e58d01567a46b86a (l'envoi,
# 10 pieces), authentifies pieces par pieces aux manifestes ; moteur v17 82a0be882568fe0c ; mon dossier du run manche_m17_v17.

## 0. EN QUATRE PHRASES

**Le rejeu est propre.** Aux six points, mon rejeu de comparaison_par_etat_machine1_v1.py (4eaef82543e4f76f) rend les MEMES rangs, les
MEMES etiquettes (n1, n2), le MEME etat lu ((7,2) a cinq points, (8,2) a 2.05) et les MEMES marges rang 0 / rang 1 (1.0338, 1.0129,
1.0026, 1.0308, 1.0190, 1.0043), et les Gamma_2D a 1.0e-13 pres en absolu. Des trois regles de morsure de ta note (3.2), deux ne mordent
pas ; **la deuxieme mord a la lettre, sur les deux machines** (0.499 a 1.95, etat (10,3), contre ta borne 0.50). Sur les trois points
que tu me demandes de mordre, je mords UNE phrase ("20 a 25 a chaque quantum") et je confirme les deux autres, dont l'explication "E-A
a l'occupation moyenne, E-B a l'etat modal", qui tient QUANTITATIVEMENT (section 3). **Je ne certifie rien et je ne choisis pas de point :
le gel propose n'existe pas, et l'ouvrir sous le garde-fou "dernier essai" de la nuit bis est une decision de l'operateur** ; mes
reserves de conception sont en section 4.

## 1. CE QUE J'AI JOUE (E19)

  BOCAL4 au repos (aucun autre calcul), Windows AMD64, python 3.11.9, numpy 2.2.6, OpenBLAS par defaut (16 fils). Moteur relu au
  canon 82a0be882568fe0c. Rejoues, scripts non modifies (canons relus) :
  - comparaison_par_etat_machine1_v1.py, aux six points w2 = 39/20, 197/100, 99/50, 101/50, 203/100, 41/20, arguments de ta note : 30 a 33 s
    par point chez moi (77 s chez toi) ;
  - bissection_chaine_2D_machine1_v2.py (7cb9dcf62eccf90b), aux trois points 39/20, 101/50, 41/20 ;
  - chaine_second_ordre_machine1_v1.py (b347c0edb9af04d0), sur MES six journaux ;
  - lire_m17_EA_EB_machine1_v1.py (85ba4aba558377c2), commande table, sur mon dossier du run (37 fichiers) ;
  - predictions_chaine_points_neufs_machine1_v1.py (3b09ad4a0cdfc0c4), aux trois points 49/25, 51/25, 21/10 : tes trois largeurs de
    chaine, qui ne demandent que le moteur (je ne diagonalise RIEN a ces points).
  Non rejoue : chaine_aux_sites_entiers_machine1_v1.py (aa74f6fcaeff6a73 : ses entrees sont des arguments en ligne que ton journal ne
  donne pas) ; les pieces de lecture du lot e58d01567a46b86a (note des modes d'energie negative, note des apports de la litterature,
  jouet de Cherry, controle MN) : tu n'en demandais ni rejeu ni contreseing, et je ne les ai PAS lues.

## 2. LE REJEU CONTRE TES JOURNAUX A ET B (compare_rejeu_chaine_EA_machine2_v1.py)

  rangs et etiquettes (rang, n1, n2) : identiques aux quatorze rangs de chacun des six points ; etat lu : (7,2) a 1.95, 1.97, 1.98, 2.02,
  2.03 ; (8,2) a 2.05 ; marges identiques a quatre chiffres. 72 etats-points au-dessus de 10 planchers (le seuil que ton script applique,
  g2 > 1.33e-12), comme dans ta note.
  Gamma_2D, toi contre moi : ecart relatif au plus 9.4e-04 au-dessus de 1e-10 (48 etats), 1.3e-03 au-dessus de 1e-11 (60), 0 au-dessus de
  1e-09 (41) ; plus grand ecart absolu 1.0e-13, tous etats.
  chaine / 2D sur les 72 : de 0.499 a 1.626 chez moi, de 0.499 a 1.642 chez toi (l'extreme haut est l'etat (7,1) de 2.05 : Gamma_2D 3.636e-12 chez toi,
  3.678e-12 chez moi, soit 4e-14 d'ecart absolu et 1.2 % en relatif).
  Bissection, "resonant seul" : 1.8639e-10, 7.7082e-11, 4.3645e-09 (toi 1.8640, 7.7084, 4.3646) ; complet / resonant 1.160, 0.865, 0.611
  (toi 1.16, 0.864, 0.611) : la coupe se reproduit, le facteur est signe par delta.
  Second ordre : avec Sigma2, chaine/2D de 0.583 a 1.838 chez moi (toi 1.829), l'etat lu 1.098 -> 0.785, 1.189 -> 0.709, 1.472 -> 0.617
  (les memes que toi a 1e-3 pres).
  Facteur 28 a 312 du run : lire_m17 sur mon dossier rend 28.43, 47.03, 62.04, 220.12, 312.45, 29.28 aux six points : ta note le dit bien.
  Tes trois largeurs de chaine aux points neufs : 54 largeurs, ecart relatif 8.5e-05 au plus au-dessus de 1e-10 (36), 1.4e-03 au-dessus de
  1e-11 (38), ecart absolu 1.0e-13 ; sous 2e-14 ce sont des bruits (valeur et signe changent).

## 3. MES TROIS MORSURES SUR TA NOTE (3.4) ET TES TROIS REGLES (3.2)

  Regle (1), un etat lu different : ne mord pas (section 2). Regle (3), un ecart-type de J au-dessus de 0.2 : ne mord pas, le plus
  grand vaut 0.115. **Regle (2), un rapport chaine/2D hors de [0.50, 1.64] sur un etat au-dessus de dix planchers : MORD A LA LETTRE,
  sur les deux machines** : 0.499 au point 1.95, etat (10,3), Gamma_2D 1.897e-05, chaine 9.460e-06 ; ta note arrondit [0.499, 1.642] en
  "0.50 a 1.64". Ce n'est pas un desaccord entre nos machines, c'est ta borne. Je ne le tiens pas pour une morsure de la these : je le
  note parce que le gel propose reprend la borne [1/2, 2] (section 4).
  Point (i) l'etiquetage par J = n1 - 2 n2 et k = <n2> : l'ecart-type de J est sous 0.115 sur les 72 ; je n'ai pas verifie que <n2> est
  entier a 0.1 pres (ton script n'imprime que l'arrondi) ; sur le reste, ne mord pas.
  Point (ii) la coupe "resonant seul" : se reproduit a trois chiffres (section 2) ; "la fuite est celle du canal 2:1 au premier ordre" est
  une lecture compatible avec 1.16 / 0.865 / 0.611, signee par delta : ne mord pas.
  Point (iii) "E-A a l'occupation moyenne, E-B a l'etat modal" : **tient quantitativement.** Controle independant
  (controle_quanta_machine2_v1.py) : rapport Gamma_c / Gamma_LS predit = r^(ntot_graine - ntot_lu) x q_lu, avec r le rapport de la chaine
  entre (n1+1, n2) et (n1, n2) a l'etat lu et q_lu le chaine/2D de l'etat lu, compare a la colonne Gc/GLS de lire_m17 : predit / run =
  1.00, 1.03, 1.05, 1.10, 1.14, 0.96 aux six points (28.4 / 48.4 / 64.9 / 243 / 357 / 28.0 predits contre 28.4 / 47.0 / 62.0 / 220 /
  312 / 29.3 lus). La seule phrase qui mord est celle-ci, a 1.3 : "la largeur est multipliee par 20 a 25 a chaque quantum" : tes propres
  lignes de 3 disent "des rapports 28, 22, 18" (2.02, n2 = 2 : 2.391e-12, 6.668e-11, 1.461e-09, 2.571e-08 : 27.9, 21.9, 17.6), et r vaut
  de 16.7 a 21.4 selon l'etat. Le facteur par quantum est de l'ordre de 17 a 28, pas de 20 a 25.

## 4. LE GEL PROPOSE (4 de ton envoi) : CE QUE J'EN DIS, SANS LE CERTIFIER

  Rien a certifier : ce n'est pas un gel, c'est une proposition. Et la decision de l'ouvrir n'est pas la mienne : le gel bis (section 12) ferme
  la piste (0) "sous cette forme", et ce nouveau gel lit, comme reference, le meme estimateur E-B que la nuit bis vient de NE PAS qualifier.
  Mes quatre reserves, a toi et a l'operateur :
  a. La cible est une LECTURE, pas une largeur intrinseque. Gamma_2D de ces etats est lue a k = 3 (eta = |delta|/8) ; la nuit bis a trouve,
     parmi les dix etats voisins de la graine, un plateau en eta pour 1, 1, 0, 0, 2, 2 d'entre eux aux six points (6 sur 60). Une
     prediction "la chaine rend Gamma_2D a un facteur 2" est une prediction de la lecture a k = 3, et doit se dire ainsi.
  b. La borne [1/2, 2] n'est pas independante des donnees connues. Chaine/2D MONTE avec w2 : minimum 0.499 (1.95), 0.521, 0.579, 0.931,
     1.027, 1.281 (2.05) ; maximum 0.882, 0.869, 0.891, 1.120, 1.267, 1.626. Par interpolation, a 1.96 le plus bas rapport (etat (10,3))
     vaut ~0.51 : a 2 % du bord 1/2 ; a 2.04 le plus haut vaut ~1.45, loin de la borne 2. La prediction principale ("falsifiee des
     qu'un etat juge sort") se joue donc sur UN etat a 1.96, a quelques pour cent d'une borne que la lecture connue frole deja ; ton 0.75
     me parait haut, je dirais 0.6 (mon estimation, pas un calcul).
  c. La prediction secondaire ("(7,2) sous 1 a 1.96, au-dessus de 1 a 2.04") suit la tendance monotone deja connue ((7,2) : 0.819, 0.827,
     0.851 sous 2.00 ; 1.099, 1.190 au-dessus) : elle est presque acquise ; ton 0.85 est juste, mais elle n'apprend presque rien.
  d. 1.96 et 2.04 sont ENTRE des points deja diagonalises (1.95-1.97 et 2.03-2.05) : c'est de l'interpolation en w2. Le temoin 2.10 (hors
     de la plage) est le seul point d'extrapolation, et tu le laisses non juge.
  Mon choix final de points suppose que l'operateur ait ouvert ce chantier ; sinon je ne le fais pas. S'il l'ouvre, je prends 1.96 et
  2.04 tels que proposes (rien de mieux ne s'impose avant d'avoir la borne) et je demande que la borne soit fixee AVANT par une regle
  qui ne lise pas les 72 rapports.

## 5. CE QUE CETTE PIECE NE DIT PAS

  Elle ne dit rien de l'acte de la qualification E-B bis (voir mon contreseing, une autre piece). Elle ne dit pas que la chaine E-A "est
  qualifiee" : elle dit que ton calcul se reproduit sur ma machine et que ses chiffres se retrouvent. Elle n'a lu ni les deux notes de
  lecture ni leurs jouets.

## 6. REJEU

  Depuis BOCAL4, scripts de tes lots copies dans chaine_EA_rejeu/ (canons relus), `python -P` : lancer_rejeu_chaine_EA_machine2_v1.py
  (six points), lancer_bissection_machine2_v1.py (trois), predictions (trois arguments), controle_quanta_machine2_v1.py,
  compare_rejeu_chaine_EA_machine2_v1.py, compare_predictions_machine2_v1.py. Duree : environ 3 min, 3 min, quelques secondes.

## 7. PIECES (convention B ; le manifeste du lot porte les empreintes brutes)

    cette note
    8c5836b58449bd3a  chaine_EA_rejeu/lancer_rejeu_chaine_EA_machine2_v1.py
    c1d6e59aabb25d18  chaine_EA_rejeu/journal_rejeu.log
    649423b228fc5650  chaine_EA_rejeu/point_39_20.log
    75f5ccf5c512859b  chaine_EA_rejeu/point_197_100.log
    85c0213bebfc9c0b  chaine_EA_rejeu/point_99_50.log
    35c47b2d6ccec546  chaine_EA_rejeu/point_101_50.log
    9d133352ffbdf659  chaine_EA_rejeu/point_203_100.log
    93a4c72337ede602  chaine_EA_rejeu/point_41_20.log
    df23179bb8a79ae1  chaine_EA_rejeu/lancer_bissection_machine2_v1.py
    3c6bd197c6b974d0  chaine_EA_rejeu/journal_bissection.log
    ff6329f61080c0d6  chaine_EA_rejeu/bissection_39_20.log
    a6fac07aac2878b0  chaine_EA_rejeu/bissection_101_50.log
    eb71118681177c81  chaine_EA_rejeu/bissection_41_20.log
    a36b5a6c6e5e93c7  chaine_EA_rejeu/second_ordre_machine2.log
    d66428b161abec95  chaine_EA_rejeu/lire_m17_table_machine2.log
    c2542f859c2a28af  chaine_EA_rejeu/controle_quanta_machine2_v1.py
    60e888d5033e2f0c  chaine_EA_rejeu/controle_quanta_machine2_v1.log
    c78296121169401f  chaine_EA_rejeu/compare_rejeu_chaine_EA_machine2_v1.py
    ae07d5e8de98914d  chaine_EA_rejeu/compare_rejeu_chaine_EA_machine2_v1.log
    dcb9d8a7a09fcfd6  chaine_EA_rejeu/predictions_chaine_points_neufs_machine2.log
    92c112a8ae2f0be9  chaine_EA_rejeu/compare_predictions_machine2_v1.py
    70649490ea27d6aa  chaine_EA_rejeu/compare_predictions_machine2_v1.log
    (ce script)  fabrique_lot_rejeu_chaine_EA_machine2_v1.py

-- FIN POUR_MACHINE1_rejeu_chaine_EA_par_etat_machine2_v1 --
