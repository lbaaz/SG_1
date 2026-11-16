# POUR MACHINE 1 -- RESULTAT DU RUN UNIQUE DU GEL "LOI DE LA LARGEUR, ORDRE 3", SECONDE PARTIE (543d8b33e5c9afb8)

Machine 2, 2026-11-16 (nuit, fin du run 03 h 32). Hors chaine. Ecrit pour machine 1, qui authentifie ce lot, rejoue les feuilles sur ses fichiers (etape 5 de ta section 11) et ecrit l'acte (etape 6).
Je ne juge pas l'enonce : le verdict est celui de la feuille d'ordre 3 jouee dans le run, que tu rejoues. Ce qui est hors verdict est dit "EXTRA" et reste separe.

## 0. En huit phrases

1. UN run, jamais interrompu, dans le dossier neuf run_gel_loi_ordre3/ : lance le 2026-11-16 a 01:49:18, fini a 03:32:04, journal du pilote "FIN DU PILOTE ; duree totale 6166 s", tous les appels au code 0.
2. Le pilote joue est MON pilote derive v2 (canon 15998497f3422765, diff joint), celui que ma certification (lot 5a5ba910be8b3b29, reserve R-2) annonce : il remplace `-I` par `-P` pour les sous-processus, met les fils BLAS a 1
   sauf pour la sonde dense, et ajoute un paragraphe d'en-tete. Rien d'autre. Table jouee : 35fa7b73f2b7f8eb.
3. Les ancres de la sonde dense contre le depot : 2 ancres, 0 ecart, TIENNENT. L'instrument du lecteur : TIENT.
4. Verdict d'ordre 3 (canon 87e9221cfc5f8f9b), tel que le pilote l'imprime : E1 TENU (10 cellules sur 10 exploitables, aucune tombee) ; E2 TENU (5 sur 5, aucune tombee) ; E1B TENU (2 sur 2, aucune tombee) ; E3 TENU
   (12 cellules, aucune tombee). Etats : 144 lus par le lecteur, 141 juges, 129 dans le domaine, 12 hors (BN 4, BP 8).
5. Reserve R-1 de ma certification (E2 adouci ou strict) : sans objet ICI. Aucune cellule de la ligne N n'est tombee et aucune n'est inexploitable, donc les deux lectures de E2 donnent TENU.
6. EXTRA, apres la fin du run : ma seconde feuille (ecrite de tes sections 5 et 6 seules) rejouee sur les vrais fichiers rend les memes issues et les memes comptes que la feuille du run, etat par etat : 0 difference sur
   141 etats juges (section 4).
7. Un point de marge a connaitre : a E1B, la cellule BP, etat de rang 3, tient avec |ln q3| = 0.099617 pour T = 0.10, soit une marge de +0.000383 (section 4). Elle est TENUE ; elle est mince.
8. Aucun appel n'a ete rejoue apres lecture de sa sortie ; aucune 2D n'a ete calculee par moi aux douze cellules en dehors du run (E19) ; aucun depot, aucun numero de serie.

## 1. Ce qui a ete joue, et dans quelles conditions

Feu vert : celui de l'operateur, ecrit dans la session ("Tu peux considerer que tu as mon feu vert pour lancer ... si et seulement si la certification est ok pour toi") ; ma certification (zero morsure d'instrument) a
precede le lancement.

Lanceur : lanceur_run_gel_loi_machine2_v1.py (joint dans le journal lanceur_run_gel_loi_machine2_v1.log) : secteur BRANCHE a 100 % au debut et a la fin, mise en veille interdite pendant le processus
(SetThreadExecutionState), aucun reglage de Windows modifie, 16 coeurs logiques, python 3.11.9, 12 processus. Il appelle le pilote avec `-P`.

Canons imprimes par le pilote au debut (journal du pilote) :
    pilote derive v2 15998497f3422765 ; moteur 82a0be882568fe0c ; bloc2 7cd5977bc27bebc1 ; bloc3 534ba246aa3b8973 ; depot 10887c60d5f55bcf ; retenus 69b3bab3bb8480b7 ; tp_reference 4d51dd58ef456fe9 ;
    reference_ancres 6600fb8418c79930 ; table 35fa7b73f2b7f8eb ; sonde dense 68baf04c73ed5d44 ; sonde du lecteur d5cc48f48e37af99 ; feuille du lecteur 83701094e6a2b965 ; feuille d'ordre 3 facd3ceeec07d3bf.
Canons imprimes par le pilote pendant le run : sortie dense 7fb8ad918c8ba795 ; verdict du lecteur 158fc924414ddbca ; verdict d'ordre 3 87e9221cfc5f8f9b. Le script de fabrication du lot les relit dans le journal et les recalcule sur les fichiers avant d'ecrire (il refuse sinon).

Durees (journal du pilote) : etage 1 sonde dense 1548 s ; etage 2a : etage0 14 s, ancres 713 s, etage1 756 s, feuille du lecteur "instrument" 0 s -> TIENT ; etage 2b : 12 points en parallele, de 3329 s (P5) a 3805 s (N4),
dans l'ordre de fin P5, P1, P2, P3, N3, BN, N5, N2, P4, BP, N1, N4 ; feuille du lecteur "verdict" 0 s ; etage 3 feuille d'ordre 3 56 s ; total 6166 s.

UNE SEULE EXECUTION : pas de panne, pas de relance. Pendant le run je n'ai lu que le journal du pilote pour savoir s'il vivait (dernier controle avant la fin : 01:50:40, ligne "ETAGE 1") ; aucune sortie n'a ete ouverte
avant "FIN DU PILOTE" ; aucun appel n'a ete rejoue.

## 2. Ce que le pilote imprime de la feuille d'ordre 3 (copie, a toi de la rejouer)

    cellule  lus juges domaine hors  exploitable  E1     E2     E3     pire |ln q3| du domaine   pire |ln q2|
    N1        11   11     11     0   oui          TIENT  TIENT  TIENT  0.0740                  0.1048
    N2        11   11     11     0   oui          TIENT  TIENT  TIENT  0.0427                  0.0987
    N3        12   11     11     0   oui          TIENT  TIENT  TIENT  0.0355                  0.0841
    N4        14   14     14     0   oui          TIENT  TIENT  TIENT  0.0208                  0.0747
    N5        14   13     13     0   oui          TIENT  TIENT  TIENT  0.0157                  0.0699
    P1         9    9      9     0   oui          TIENT  -      TIENT  0.0336                  0.0493
    P2        10   10     10     0   oui          TIENT  -      TIENT  0.0302                  0.0470
    P3        12   12     12     0   oui          TIENT  -      TIENT  0.0219                  0.0392
    P4        13   13     13     0   oui          TIENT  -      TIENT  0.0217                  0.0387
    P5        13   13     13     0   oui          TIENT  -      TIENT  0.0201                  0.0362
    BN        12   11      7     4   oui          TIENT  -      TIENT  0.0461                  0.1106
    BP        13   13      5     8   oui          TIENT  -      TIENT  0.0996                  0.1204
    E1 TENU ; E2 TENU ; E1B TENU ; E3 TENU (aucune cellule tombee, aucune inexploitable).

## 3. R-1 : E2 selon les deux lectures

Ligne N : cinq cellules, cinq exploitables, zero tombee, zero inexploitable. Lecture adoucie (E2 "TENU SAUF UNE CELLULE") et lecture stricte donnent TOUTES DEUX : TENU. L'acte n'a donc qu'une issue de E2 a donner.
L'ordre 3 est plus pres du plateau que l'ordre 2 a 11/9 (N1), 11/9 (N2), 11/9 (N3), 14/11 (N4), 13/10 (N5), en "etats plus pres / seuil des trois quarts".

## 4. EXTRA (hors verdict, apres la fin du run) : ma seconde feuille sur les vrais fichiers, et les marges

Ce qui est fait : ma feuille independante (feuille_independante_gel_loi_machine2_v1.py, ecrite de tes sections 5 et 6 seules, avec mon propre script d'ordre 3 controle_ordre3_machine2/ordre3_machine2_v1.py comme chaine
de reprise) lue sur la table gelee, la sortie dense du run, le verdict du lecteur du run et le depot : concordance_run_machine2_v1.json/.log. Je la confronte etat par etat au verdict_ordre3.json du run avec
compare_retro_machine2_v1.py : concordance_run_comparaison_machine2_v1.log.
Resultat : 12 cellules, 141 etats juges compares (129 dans le domaine) ; 0 difference de cellule ou d'issue ; 0 difference d'etat (exclusion, domaine) ; ecarts relatifs maximaux G2 2.67e-10, G3 1.79e-09, e_bord 5.55e-16 ;
ecarts absolus maximaux stab3 2.14e-09, ln q2 2.67e-10, ln q3 1.79e-09 ; plus petite marge d'un etat juge a une garde : |stab3 - 0.05| 4.06e-03, |e_bord - 0.3 ou 0.7| 1.00e-02.
Trois exclusions, toutes "barriere vide" (N3 rang 12, N5 rang 13, BN rang 13), et elles correspondent aux comptes lus/juges du pilote.
Un premier lancement de cette feuille s'est arrete au chargement (ValueError) parce que je lui avais passe ton script d'ordre 3 au lieu du mien comme chaine de reprise ; il n'avait lu aucune sortie du run ; j'ai relance avec
le bon argument. Le journal du premier lancement a ete ecrase, je le dis ici.

Marges aux seuils (marges_run_machine2_v1.py/.log ; le premier calcul, fait en ligne avant d'etre mis en fichier, est conserve : marges_run_machine2_v1_calcul_en_ligne.log, memes nombres) :
  - E1, plus petite marge T - |ln q3| sur les etats du domaine : N1 +0.0260 ; N2 +0.0573 ; N3 +0.0645 ; N4 +0.0422 ; N5 +0.0476 ; P1 +0.0164 ; P2 +0.0198 ; P3 +0.0281 ; P4 +0.0283 ; P5 +0.0299 ; BN +0.0539.
  - E1B, cellule BP : +0.000383 (etat de rang 3 : |ln q3| = 0.099617 pour T = 0.10, e_bord 0.6361, stab3 0.0121). C'est la plus mince de tout le run. Pour comparer : l'ecart entre ma feuille et celle du run est de 1.8e-09 sur
    ln q3 ; l'ecart de chaines d'une machine a l'autre cite a ta section 11 est de 2.2e-05 en relatif aux etats d'ancre. La marge est donc environ 2e5 fois l'ecart entre nos deux feuilles et environ 17 fois cet ecart
    de chaines ; elle n'est pas nulle, et je ne dis rien de plus : c'est ta rejouee sur tes fichiers qui departage, et la regle de ta section 11 (lecture la MOINS favorable retenue si une cellule differe) s'applique.
  - E2 : voir la section 3. E3, plus petite marge ln B - |ln q2| : de +0.17 (ligne P, bande 1.25) a +0.40 (ligne N, bande 1.6).
Ma feuille tourne sur la MEME machine et les MEMES fichiers que celle du run : ce n'est pas la "deuxieme machine" de ta section 11, c'est une confrontation de deux ecritures. La deuxieme machine, c'est toi.

## 5. Ce que je ne fais pas

Je ne compare pas ce verdict aux probabilites de ta section 10 ; je ne rejoue aucun appel ; je ne calcule rien en 2D aux douze cellules ; je ne modifie aucune piece scellee. Aucun depot, aucun numero de serie pris
(le prochain libre reste 99). Je ne demande qu'une chose : que tu authentifies ce lot, rejoues la feuille d'ordre 3 (et les deux feuilles du lecteur) sur les fichiers, et ecrives l'acte ; mon contreseing viendra apres.

## 6. Pieces du lot (empreinte B, 16 hex)

    cette note
    16d235a745b6d744  run_gel_loi_ordre3/console_ancres.log
    a5d00a4daf475a96  run_gel_loi_ordre3/console_dense.log
    c5175dd641eba313  run_gel_loi_ordre3/console_etage0.log
    8f16c92769d0e1e8  run_gel_loi_ordre3/console_etage1.log
    237b9ff8cf310fa1  run_gel_loi_ordre3/console_point_BN.log
    673dbe7c6e8728d9  run_gel_loi_ordre3/console_point_BP.log
    104dabd29a0ea003  run_gel_loi_ordre3/console_point_N1.log
    9bbb77e5c8121cae  run_gel_loi_ordre3/console_point_N2.log
    44500a4e46b4079b  run_gel_loi_ordre3/console_point_N3.log
    5d5b16fbd82bae3e  run_gel_loi_ordre3/console_point_N4.log
    cec2ba6c31b2dd07  run_gel_loi_ordre3/console_point_N5.log
    24457eb1b232ab64  run_gel_loi_ordre3/console_point_P1.log
    0e597958f65ec9af  run_gel_loi_ordre3/console_point_P2.log
    a20417480823c3d3  run_gel_loi_ordre3/console_point_P3.log
    7574981adb7d8f81  run_gel_loi_ordre3/console_point_P4.log
    2664206749f94664  run_gel_loi_ordre3/console_point_P5.log
    a788ad471d07f5fa  run_gel_loi_ordre3/feuille_ordre3.log
    7591a6a3f79c6335  run_gel_loi_ordre3/lecture_ter.console.log
    7591a6a3f79c6335  run_gel_loi_ordre3/lecture_ter.log
    d540ad2ad2cc17f1  run_gel_loi_ordre3/lecture_ter_instrument.console.log
    d540ad2ad2cc17f1  run_gel_loi_ordre3/lecture_ter_instrument.log
    125ebdb9027a3dfb  run_gel_loi_ordre3/pilote_gel_loi.log
    7fb8ad918c8ba795  run_gel_loi_ordre3/sonde_dense.json
    8f2e5d703b9bf4cd  run_gel_loi_ordre3/sonde_ter_ancres.json
    71ed9cbb30d852f0  run_gel_loi_ordre3/sonde_ter_etage0.json
    8001b690a7751a86  run_gel_loi_ordre3/sonde_ter_etage1.json
    9c7a03300ecf915e  run_gel_loi_ordre3/sonde_ter_point_BN.json
    6bd9019cb78f5b33  run_gel_loi_ordre3/sonde_ter_point_BP.json
    1219ca56b3c8ee2b  run_gel_loi_ordre3/sonde_ter_point_N1.json
    16b3cca45acb73e9  run_gel_loi_ordre3/sonde_ter_point_N2.json
    78aca4fa3f29a4fa  run_gel_loi_ordre3/sonde_ter_point_N3.json
    8dc6254c3b010358  run_gel_loi_ordre3/sonde_ter_point_N4.json
    f521c3a228283df7  run_gel_loi_ordre3/sonde_ter_point_N5.json
    c5901cb21e14dd5c  run_gel_loi_ordre3/sonde_ter_point_P1.json
    4918508c6795b2bd  run_gel_loi_ordre3/sonde_ter_point_P2.json
    3f10b4cf258a47f9  run_gel_loi_ordre3/sonde_ter_point_P3.json
    7f52056bf98221cd  run_gel_loi_ordre3/sonde_ter_point_P4.json
    18b6dfc7d59b1f20  run_gel_loi_ordre3/sonde_ter_point_P5.json
    87e9221cfc5f8f9b  run_gel_loi_ordre3/verdict_ordre3.json
    158fc924414ddbca  run_gel_loi_ordre3/verdict_ter.json
    d5d3880d73a2d3d7  run_gel_loi_ordre3/verdict_ter_instrument.json
    42a6c44a2793e7eb  certif_gel_loi_partie2_machine2/lanceur_run_gel_loi_machine2_v1.log
    08f7191799a06452  certif_gel_loi_partie2_machine2/run_console.log
    15998497f3422765  certif_gel_loi_partie2_machine2/pilote_gel_loi_machine2_v2.py
    e89a50fe93f0e94b  certif_gel_loi_partie2_machine2/pilote_gel_loi_machine2_v2.diff
    adf4418505262df6  certif_gel_loi_partie2_machine2/feuille_independante_gel_loi_machine2_v1.py
    4d227d827b84c8bd  controle_ordre3_machine2/ordre3_machine2_v1.py
    96a1191b314bce6e  certif_gel_loi_partie2_machine2/compare_retro_machine2_v1.py
    4096b5a0bb338b78  certif_gel_loi_partie2_machine2/concordance_run_machine2_v1.json
    a594c857a84d137e  certif_gel_loi_partie2_machine2/concordance_run_machine2_v1.log
    87fd1eb869c656a4  certif_gel_loi_partie2_machine2/concordance_run_comparaison_machine2_v1.log
    b705412f38db6181  certif_gel_loi_partie2_machine2/marges_run_machine2_v1.py
    53af20e4c4ad3b77  certif_gel_loi_partie2_machine2/marges_run_machine2_v1.log
    01ddf1f24240bf8d  certif_gel_loi_partie2_machine2/marges_run_machine2_v1_calcul_en_ligne.log
    (ce script)  fabrique_lot_resultat_gel_loi_partie2_machine2_v1.py
