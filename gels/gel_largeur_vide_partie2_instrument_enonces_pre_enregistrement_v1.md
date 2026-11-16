GEL "LARGEUR DU VIDE" -- SECONDE PARTIE : L'INSTRUMENT, LES ENONCES, LES TOLERANCES
PRE-ENREGISTREMENT v1 -- machine 1, 2026-11-16.
A CERTIFIER PAR MACHINE 2 AVANT TOUTE LECTURE 2D DU FANTOME A L'UNE DES CELLULES.

0. STATUT
  Cette piece complete la premiere partie (b57c9ccdd3946261, lot 879ea2e51c7d7f4f), que machine 2
  a certifiee telle quelle, sans morsure (lot d4f95772710d545c). Elle fixe les cellules tirees,
  l'instrument du run, les enonces juges, leurs tolerances, ce que chaque issue engage, et les
  annonces de la plume. Rien n'est joue : l'etat que porte le site (0, 0) du systeme a fantome n'a
  ete lu en 2D a aucune cellule, par machine 1.
  Ouverture. L'operateur a ecrit "on gele et on avance !" (16/11/2026, 12 h 19) : declaration de
  machine 1, que machine 2 dit ne pas pouvoir attester (lot d4f95772710d545c).
  Graine. L'operateur a ecrit a machine 1 "la graine 479579" (16/11/2026, 13 h 34), apres avoir
  porte la certification de machine 2 et apres que machine 1 a authentifie cette certification et
  ecrit la table commune (lot 53c604647e78afa4, remis a l'operateur avant la graine ; machine 1 ne
  sait pas s'il a ete porte a machine 2). Machine 1 n'avait calcule aucun tirage sur une graine
  faite de chiffres avant de la recevoir. Elle avait rappele a l'operateur que la graine lui
  revenait ; elle n'en a propose ni commente aucune.
  Tirage. Par le script de machine 1 (cc1b2df637a9f3cd), sur les deux tables d'eligibilite
  (7b278d2b5a34d0a3 et 84bffbbd2f675181) : les quatre creneaux sortent au rang 0, 28 cellules.
  Machine 2 dit son tirage a la certification ; si ses cellules ou leurs couplages ecrits
  different, PAS DE GEL (premiere partie, section 6).
  E19. Aucune des deux machines ne lit en 2D le systeme a fantome a l'une des cellules, ni l'etat
  (0, 0) du systeme a fantome a aucun w2, avant la certification croisee de cette piece et le feu
  vert ecrit de l'operateur. Tout ce que cette piece calcule aux cellules est une chaine a une
  dimension. Les calculs 2D qu'elle rapporte (pre-vol, section 4.5) sont l'instrument du lecteur a
  ses points deja joues, et le JUMEAU SANS FANTOME a w2 = 101/50, qui n'est pas un candidat.

1. QUESTION ET PERIMETRE
  La largeur de l'etat que porte le site (0, 0), "le vide", n'a jamais ete lue en 2D. La note sur
  le vide (15641e09a351d56d) dit qu'une chaine a une dimension la predit, sous un absorbeur de
  chaine adapte au saut. Ce gel demande si c'est vrai, a des cellules que personne n'a choisies.
  Perimetre : quatre w2 (delta = -0.018, -0.003, +0.005, +0.017), sept profondeurs de barriere.
  L'objet juge est la chaine d'ordre 3 des blocs deposes sous l'absorbeur adapte (bloc
  49a40d9098b55361), telle quelle : son plateau G3* sur dix-huit variantes. La reference est la
  largeur de plateau sous l'absorbeur A, lue par le lecteur creux du delta 99.
  Ce que le gel SEPARE et ne separe pas. Aux seize cellules lisibles, l'ordre 3 differe de l'ordre
  2 de 0.0026 au plus, du premier ordre de 0.0206 au plus, et de la loi d'echelle |delta|
  Phi*(kappa) de 0.0291 au plus : sous une tolerance de 0.02, V1 n'oppose donc pas les ordres
  entre eux. Il eprouve ceci : "le mecanisme de l'echelle et la chaine rendent la largeur du vide
  a 0.02 pres". Les corrections a la loi d'echelle ne sont eprouvees que sur la ligne profonde du
  creneau MG, si elle est lue : a MG12 et MG16 l'ordre 3 est a -0.055 et -0.077 du premier ordre.

2. SOURCES (convention B)
    82a0be882568fe0c scripts/m17_chaine_v17.py (registre dee73bd), le moteur
    7cd5977bc27bebc1 scripts/chaine_ordre2_bloc_machine1_v1.py (registre), le bloc d'ordre 2
    534ba246aa3b8973 scripts/ordre3_bloc_machine1_v1.py (registre), le bloc d'ordre 3
    d5cc48f48e37af99 scripts/sonde_lecteur_gel_loi_machine1_v1.py (registre) : la sonde du
                      lecteur, jouee telle quelle a l'etage A, et dont le bloc LECTEUR CREUX est
                      execute par la sonde de ce gel
    83701094e6a2b965 scripts/lecture_lecteur_gel_loi_machine1_v1.py (registre) : la feuille du
                      lecteur, jouee telle quelle a l'etage A, et dont juger_etat est appele par
                      la feuille de ce gel
    10887c60d5f55bcf journal/sonde_ordre2.json (registre), le depot du delta 98 : les ancres
    69b3bab3bb8480b7 journal/tp_retenus_machine2_v1.json (registre) : couplages du temoin positif
    4d51dd58ef456fe9 journal/tp_reference_machine2_v1.json (registre) : reference du temoin
                      positif
    6600fb8418c79930 journal/reference_ancres_ter_machine1_v1.json (registre) : reference des
                      ancres
    35fa7b73f2b7f8eb journal/table_points_gel_loi_ordre3_v1.json (registre) : la table que la
                      sonde deposee exige a l'etage A
    b57c9ccdd3946261 gel_largeur_vide_partie1_regle_tirage_pre_enregistrement_v1.md (lot
                      879ea2e51c7d7f4f)
    49a40d9098b55361 chaine_adaptee_bloc_machine1_v1.py (meme lot) : le predicteur
    cc1b2df637a9f3cd tirage_vide_machine1_v1.py (meme lot)
    d4f95772710d545c lot de machine 2 : certification de la premiere partie, sa table
                      (84bffbbd2f675181), ses cinq demandes R-1 a R-5
    53c604647e78afa4 lot de machine 1 : reception, table commune, les dix-huit variantes aux etats
                      joues (e9a0a3812de6ad16)
    15641e09a351d56d note sur le vide (lot c5d8fd0313217569) ; la loi d'echelle : lot
                      408b8a595cad0040
  Les lots de machine 1 et de machine 2 de ce jour ne sont pas au registre (dee73bd) : les deux
  machines les detiennent.

3. LES CELLULES
  Table gelee : table_cellules_gel_vide_v1.json, canon b71206e5daf6c741. Elle porte la graine, les
  rangs, les 28 cellules, leurs predictions et leur tolerance. La sonde, la feuille et le pilote
  portent son canon en dur. Par cellule : w2, delta, profondeur m, couplage ecrit, r_c, plus
  grande boite du lecteur (r_c + 100), plateau predit G3* et etendue de la chaine sous ses
  dix-huit variantes, tolerance T.
    cellule  w2          delta    m   g            r_c  boite  G3*       etendue  T
    MG3      991/500     -0.018   3   4.31696e-03  24   124    2.94e-09  0.0013   0.02
    MG4      991/500     -0.018   4   3.29539e-03  26   126    6.48e-11  0.0014   0.02
    MG5      991/500     -0.018   5   2.61984e-03  28   128    1.34e-12  0.0026   0.02
    MG6      991/500     -0.018   6   2.14200e-03  30   130    2.55e-14  0.0022   0.02
    MG8      991/500     -0.018   8   1.52906e-03  34   134    8.35e-18  0.0054   0.05
    MG12     991/500     -0.018   12  9.19414e-04  50   150    7.05e-25  0.0092   0.05
    MG16     991/500     -0.018   16  6.29420e-04  66   166    5.21e-32  0.0086   0.05
    MP3      1997/1000   -0.003   3   7.61494e-04  24   124    4.95e-10  0.0027   0.02
    MP4      1997/1000   -0.003   4   5.81293e-04  26   126    1.10e-11  0.0029   0.02
    MP5      1997/1000   -0.003   5   4.62128e-04  28   128    2.29e-13  0.0020   0.02
    MP6      1997/1000   -0.003   6   3.77840e-04  30   130    4.37e-15  0.0058   0.02
    MP8      1997/1000   -0.003   8   2.69720e-04  34   134    1.45e-18  0.0064   0.05
    MP12     1997/1000   -0.003   12  1.62181e-04  50   150    1.25e-25  0.0091   0.05
    MP16     1997/1000   -0.003   16  1.11027e-04  66   166    9.50e-33  0.0074   0.05
    PP3      401/200     +0.005   3   1.30778e-03  24   124    8.25e-10  0.0032   0.02
    PP4      401/200     +0.005   4   9.98303e-04  26   126    1.83e-11  0.0042   0.02
    PP5      401/200     +0.005   5   7.93651e-04  28   128    3.82e-13  0.0041   0.02
    PP6      401/200     +0.005   6   6.48897e-04  30   130    7.32e-15  0.0052   0.02
    PP8      401/200     +0.005   8   4.63212e-04  34   134    2.43e-18  0.0068   0.05
    PP12     401/200     +0.005   12  2.78526e-04  50   150    2.13e-25  0.0083   0.05
    PP16     401/200     +0.005   16  1.90676e-04  66   166    1.62e-32  0.0054   0.05
    PG3      2017/1000   +0.017   3   4.64925e-03  24   124    2.79e-09  0.0054   0.02
    PG4      2017/1000   +0.017   4   3.54905e-03  26   126    6.19e-11  0.0063   0.02
    PG5      2017/1000   +0.017   5   2.82149e-03  28   128    1.29e-12  0.0069   0.02
    PG6      2017/1000   +0.017   6   2.30688e-03  30   130    2.48e-14  0.0070   0.02
    PG8      2017/1000   +0.017   8   1.64676e-03  34   134    8.26e-18  0.0084   0.05
    PG12     2017/1000   +0.017   12  9.90184e-04  50   150    7.26e-25  0.0077   0.05
    PG16     2017/1000   +0.017   16  6.77868e-04  66   166    5.59e-32  0.0068   0.05
  Aux 28 cellules la barriere du moteur finit au site m, et G3* et l'etendue sont ceux de la table
  de la premiere partie, que machine 2 a retrouvee par sa methode (ecart de 1.3e-08 sur le
  logarithme du plateau, lot d4f95772710d545c).

4. L'INSTRUMENT : UN RUN, TROIS ETAGES
  4.1 Les pieces (convention B)
    b71206e5daf6c741 table_cellules_gel_vide_v1.json : la table gelee ; ecrite par
                      predictions_vide_machine1_v1.py (d7f37c7e2f08a2ea)
    0f82986cca133330 sonde_vide_machine1_v1.py : NOUVELLE ; elle execute le bloc LECTEUR CREUX de
                      la sonde deposee, lu dans son fichier
    ac39a24def6c7420 feuille_vide_machine1_v1.py : NOUVELLE ; elle appelle juger_etat de la
                      feuille deposee et juge les enonces
    a38b1550f8f5e3cf pilote_gel_vide_machine1_v1.py : NOUVEAU ; il enchaine et tient le journal
    916eec7c3b6f6a47 table_cellules_prevol_vide_v1.json : deux cellules a w2 = 101/50, non
                      candidat : le pre-vol
  Aucune piece deposee n'est editee ni derivee : la sonde et la feuille du lecteur sont jouees
  telles quelles a l'etage A, et leurs routines sont executees depuis leurs fichiers, au canon
  controle, aux etages B et C.
  4.2 Le deroulement du run (le pilote)
    Etage A. L'instrument du lecteur, tel qu'au gel "ordre 3" : la sonde deposee en modes etage0,
    ancres et etage1 (les deux ancres du depot, le temoin positif, le temoin negatif des ancres),
    puis la feuille deposee, etape "instrument". Si elle ne rend pas TIENT, le run s'arrete :
    aucune cellule n'est lue.
    Etage B. La sonde de ce gel, un appel par cellule : le jumeau sans fantome (signe +1) puis le
    fantome (signe -1), au site (0, 0), depuis l'energie 0, sous les quatre absorbeurs du depot (A
    : F2, 80 couches ; B : F2, 100 ; C : F1, 100 ; D : F2, bord r_c + 10, 80), a douze barreaux (k
    = -3 a 8, eta_k = eta0 2^(-k)), avec r_c = 2 (m + max(8, m)) + 2 et eta0 = |w2 - 2|. Aucun
    etage dense.
    Etage C. La feuille de ce gel : section 5.
  4.3 Le banc de la feuille
    Le banc fabrique des dossiers de run SYNTHETIQUES pour la table gelee (des plateaux poses a la
    main autour de la prediction : ils ne disent rien des cellules), change une chose a la fois,
    avec l'effet attendu ecrit avant : 26 cas, 26 tenus. Ils couvrent : une cellule qui tombe,
    deux, le signe, la cellule non jugeable, trop de non jugeables, un creneau sans deux cellules
    tenues, le desaccord d'un absorbeur, l'absence de plateau, les lectures non suivies, le temoin
    trop large, le temoin non suivi, l'instrument, le fichier absent, le canon de la sonde, le
    couplage, le fichier de pre-vol, la geometrie, la ligne profonde (qui tombe, non lue, peu
    lue), la tolerance par ligne, les trois termes de la bande, une autre table.
    Defaut de ma plume, garde a cote : au premier passage 25 cas sur 26 tenaient. Le cas rate
    (b24) portait une attente fausse de ma main (0.0105 pour un seuil de 0.0110) ; la feuille
    avait raison. L'attente est corrigee, le diff et le premier journal sont joints ; la feuille
    n'a pas ete retouchee.
  4.4 Les refus, sans aucune mesure
    Le chemin sans --prevol sur la table du gel ne peut pas etre joue avant le feu vert : il
    lirait le fantome. Seuls ses refus le sont (essai_refus_machine1_v1.py) : 9 essais, 9 tenus,
    aucun fichier ecrit. La sonde refuse la table du gel avec --prevol, toute autre table sans
    --prevol, une cellule inconnue, un w2 candidat en pre-vol, un moteur qui n'est pas au canon ;
    la feuille et le pilote refusent de meme. La lecture du fantome ne differe de celle du jumeau
    que par l'argument signe du bloc depose : elle n'a jamais ete executee par la sonde de ce gel.
  4.5 Le pre-vol de machine 1
    Le pilote, avec --prevol, sur la table de pre-vol (deux cellules a w2 = 101/50, m = 3 et 8) :
    l'etage A entier, puis le jumeau seul aux deux cellules, puis la feuille. Quatre controles
    (comparaison_prevol_vide_machine1_v1.py), tous tenus :
      P1 l'instrument du lecteur, joue par le pilote avec les pieces deposees : TIENT.
      P2 a m = 8, le jumeau lu par la sonde de ce gel rend les largeurs de la piece de faisabilite
         de la premiere partie (meme w2, meme couplage, meme geometrie) : 6 lectures comparees,
         pire ecart relatif 4.4e-16.
      P3 lectures du jumeau suivies : 48 sur 48 a m = 3 (largeurs de 2.4e-51 a 1.8e-35), 48 sur 48
         a m = 8 (de 3.5e-70 a 1.2e-52) ; le fantome n'est lu a aucune ; les fichiers sont marques
         pre-vol.
      P4 la feuille, en pre-vol : "PRE-VOL, RIEN N'EST JUGE", aucune issue rendue.
    Durees sur le conteneur de machine 1 (deux processus, un fil chacun) : feuille du lecteur,
    instrument 0 s ; feuille_vide 0 s ; lecteur ancres 643 s ; lecteur etage0 21 s ; lecteur
    etage1 701 s ; sonde_vide PV3 114 s ; sonde_vide PV8 148 s ; total 870 s. Ce que le pre-vol ne
    dit pas : rien du fantome, et rien de BOCAL4.

5. CELLULE LUE, BANDE, JUGEMENT (ce que fait la feuille)
  LECTEUR. La feuille appelle juger_etat de la feuille deposee sur les quatre trajectoires du
  fantome : un plateau sous chacun des quatre absorbeurs (cinq barreaux consecutifs, plus grande
  valeur <= 1.05 fois la plus petite), et les plateaux sous B, C et D a 0.05 pres du plateau sous
  A, en logarithme. Statut : QUALIFIE, NON QUALIFIE ou NON LISIBLE, comme au gel ter. Gamma_pl est
  le plateau sous A.
  ETALEMENT DU LECTEUR, s : le plus grand de ln(1 + etalement du plateau sous A) et des trois
  |ln(plateau X / plateau A)|, X = B, C, D. Ce sont des nombres que la feuille deposee calcule
  deja.
  TEMOIN. Le jumeau sans fantome a la meme cellule (demande R-4 de machine 2). Il TIENT si ses 48
  lectures sont suivies et si sa plus grande largeur vaut au plus 1e-6 Gamma_pl.
  CELLULE LUE : QUALIFIE et temoin tenu. Sinon NON LUE, avec son motif.
  JUGEMENT d'une cellule lue. ln q = ln(G3* / Gamma_pl). BANDE b = etendue de la chaine a la
  cellule (table) + s. La cellule TIENT si |ln q| <= T - b ; elle TOMBE si |ln q| > T + b ; elle
  est NON JUGEABLE sinon (demande R-2 de machine 2, a laquelle la plume ajoute s). Une cellule
  dont la bande atteint la tolerance ne peut donc pas tenir : elle tombe ou n'est pas jugeable.

6. LES ENONCES ET LEURS ISSUES (la cellule est l'unite)
  V1, ligne lisible, seize cellules, T = 0.02. TOMBE si deux cellules ou plus tombent ; sinon NON
  CONCLUANT si moins de douze cellules sont jugees (tenues ou tombees), ou si un creneau a moins
  de deux cellules tenues ; sinon TENU SAUF UNE CELLULE si une tombe ; sinon TENU.
  VP, ligne profonde, douze cellules, T = 0.05. Hors de V1 : quelle que soit son issue, celle de
  V1 ne change pas. TOMBE si deux cellules ou plus tombent ; sinon NON LUE si aucune n'est jugee ;
  sinon NON CONCLUANT si moins de six sont jugees ; sinon TENU SAUF UNE CELLULE ou TENU.
  Ce qui est consigne sans etre juge, par cellule lue : le signe de ln q et celui de delta ; ln q
  pour l'ordre 2, pour le premier ordre, pour la loi d'echelle |delta| Phi*(kappa) et pour la
  forme fermee a trois termes ; ln(Gamma_pl / |delta|), pour lire la superposition des creneaux a
  profondeur egale. Aucun enonce ne porte sur le signe du residu (demande R-5).
  La note sur le vide proposait un enonce V2 sur la forme fermee. Il n'est PAS pose : aux cellules
  lisibles la forme fermee est a 0.026 a 0.060 du plateau predit, hors de toute tolerance utile ;
  elle est consignee (section 14, E-3).

7. LES TOLERANCES, ET CE QUE LA PLUME A VU AVANT DE LES ECRIRE
  Aucune largeur 2D du vide n'existe. Les tolerances viennent de trois sources, toutes regardees
  avant d'ecrire.
  7.1 Ce que la chaine peut
    L'etendue de la chaine sous ses dix-huit variantes vaut de 0.0013 a 0.0070 aux cellules
    lisibles et 0.0092 au plus aux profondes. Ce n'est pas l'erreur de la chaine : c'est ce que
    son absorbeur laisse indetermine.
  7.2 Ce que la chaine a manque aux etats deja joues (apres coup ; lot 53c604647e78afa4)
    Aux 185 etats du domaine des deltas 98 et 100, sous l'absorbeur adapte, le residu ln(G3* /
    Gamma_pl) a le signe de delta partout (constat de machine 2, retrouve par machine 1) ; a 184
    de ces etats la chaine rend une correction a la loi d'echelle trop petite. La part manquee, (r
    - r de la chaine) / r, vaut 0.071 en mediane, et de 0.010 a 0.237 selon la cellule (mediane
    par cellule).
    DEUX LECTURES de ce constat, qui coincident aux etats joues et PAS au vide. (a) "Le residu a
    le signe de delta." (b) "La chaine manque une part f de sa correction" : le residu vaut alors
    - f / (1 - f) r3, r3 etant ce que la chaine ajoute a la loi d'echelle. Aux etats joues r a le
    signe oppose a delta et les deux lectures donnent le meme signe. Au vide, r3 est NEGATIF aux
    quatre cellules lisibles de MG (delta < 0) : la lecture (a) y annonce un residu negatif, la
    lecture (b) un residu positif. La plume ne sait pas laquelle vaut pour le vide ; le gel peut
    les departager a MG, si la bande le permet.
  7.3 Les chaines aux cellules, et ce qui tiendrait
    Par cellule : ln(G3* / G2*) ; ln(G3* / G1*) ; r3 ; ecart de la forme fermee a G3* ; residu
    attendu sous la lecture (b), pour la part manquee mediane puis pour la plus grande ; et T -
    etendue, le plus grand |ln q| qui tiendrait si le lecteur etait sans etalement.
    cellule  ln(G3*/G2*)  ln(G3*/G1*)  r3       ferme - G3*  residu (b) : median, pire   T - etendue
    MG3      -0.0012      -0.0060      -0.0103  +0.0600      +0.0008, +0.0032            0.0187
    MG4      -0.0015      -0.0106      -0.0163  +0.0557      +0.0013, +0.0051            0.0186
    MG5      -0.0015      -0.0152      -0.0223  +0.0554      +0.0017, +0.0069            0.0174
    MG6      -0.0015      -0.0206      -0.0291  +0.0573      +0.0022, +0.0090            0.0178
    MG8      -0.0018      -0.0312      -0.0426  +0.0652      +0.0033, +0.0132            0.0446
    MG12     -0.0019      -0.0549      -0.0721  +0.0872      +0.0056, +0.0224            0.0408
    MG16     -0.0021      -0.0771      -0.1002  +0.1123      +0.0077, +0.0312            0.0414
    MP3      -0.0000      -0.0001      -0.0008  +0.0504      +0.0001, +0.0003            0.0173
    MP4      -0.0001      -0.0002      -0.0011  +0.0405      +0.0001, +0.0003            0.0171
    MP5      -0.0001      -0.0004      -0.0016  +0.0347      +0.0001, +0.0005            0.0180
    MP6      -0.0001      -0.0014      -0.0028  +0.0311      +0.0002, +0.0009            0.0142
    MP8      -0.0001      -0.0023      -0.0042  +0.0268      +0.0003, +0.0013            0.0436
    MP12     -0.0001      -0.0053      -0.0081  +0.0232      +0.0006, +0.0025            0.0409
    MP16     -0.0001      -0.0073      -0.0112  +0.0233      +0.0009, +0.0035            0.0426
    PP3      -0.0002      -0.0019      -0.0007  +0.0503      +0.0001, +0.0002            0.0168
    PP4      -0.0002      -0.0013      +0.0003  +0.0391      -0.0000, -0.0001            0.0158
    PP5      -0.0002      -0.0002      +0.0017  +0.0314      -0.0001, -0.0005            0.0159
    PP6      -0.0002      +0.0002      +0.0025  +0.0258      -0.0002, -0.0008            0.0148
    PP8      -0.0002      +0.0016      +0.0047  +0.0179      -0.0004, -0.0015            0.0432
    PP12     -0.0003      +0.0048      +0.0095  +0.0056      -0.0007, -0.0030            0.0417
    PP16     -0.0003      +0.0079      +0.0142  -0.0021      -0.0011, -0.0044            0.0446
    PG3      -0.0018      -0.0120      -0.0079  +0.0575      +0.0006, +0.0025            0.0146
    PG4      -0.0020      -0.0114      -0.0061  +0.0455      +0.0005, +0.0019            0.0137
    PG5      -0.0023      -0.0107      -0.0041  +0.0372      +0.0003, +0.0013            0.0131
    PG6      -0.0026      -0.0106      -0.0027  +0.0310      +0.0002, +0.0008            0.0130
    PG8      -0.0029      -0.0076      +0.0030  +0.0196      -0.0002, -0.0009            0.0416
    PG12     -0.0032      -0.0024      +0.0136  +0.0015      -0.0010, -0.0042            0.0423
    PG16     -0.0031      +0.0045      +0.0261  -0.0140      -0.0020, -0.0081            0.0432
    Lecture. Aux cellules lisibles le residu attendu sous (b) vaut 0.0022 au plus pour la part
    mediane et 0.0090 au plus pour la plus grande (a MG6) ; machine 2 extrapolait "de l'ordre de
    0.005, au plus 0.01". T - etendue y vaut de 0.0130 a 0.0187 : une cellule ne tient que si le
    residu ET l'etalement du lecteur logent ensemble sous ce nombre. L'etalement du lecteur au
    vide n'est pas connu ; au mandataire a une dimension de la note sur le vide (sa section 2.3)
    l'absorbeur du lecteur restait a moins d'un centieme de la chaine. Dans l'hypothese d'un
    etalement de 0.01, les cellules du creneau PG ne tiendraient que sous 0.0030 a 0.0046.
  7.4 Les deux tolerances
    T = 0.02 sur la ligne lisible : c'est la demande R-1 de machine 2 ("au plus 0.02"), que la
    plume prend telle quelle. Elle vaut de 2.9 a 15.1 fois l'etendue de la chaine et 2.2 fois le
    plus grand residu attendu sous (b) ; la tolerance de E1 (0.05) en aurait valu 5.5 fois. T =
    0.05 sur la ligne profonde : la valeur de E1 pour e_bord < 0.3 ; les douze cellules profondes
    ont e_bord de 0.024 a 0.283, et le residu attendu sous (b) y monte a 0.0312 pour la plus
    grande part manquee.
    Ces deux valeurs, le facteur 1e-6 du temoin et les comptes des issues (douze, deux, six) ont
    ete ecrits dans la feuille AVANT le banc et n'ont pas ete retouches ensuite. Declaration de la
    plume : machine 2 ne peut pas la verifier. Aucun ne sera regle apres lecture.

8. CE QUE CHAQUE ISSUE ENGAGE
  L'INSTRUMENT NE TIENT PAS (etage A) : aucune cellule n'est lue, rien n'est juge ; l'acte le dit
    ; une suite demande un autre gel.
  V1 TENU. L'acte peut ecrire : "a seize cellules tirees au sort, de 3 a 6 barreaux et pour
    |delta| de 0.003 a 0.018, la chaine d'ordre 3 sous absorbeur adapte rend la largeur de l'etat
    porte par (0, 0) a 0.02 pres en logarithme, au-dela de sa propre etendue et de l'etalement du
    lecteur". Il NE peut PAS ecrire que la chaine est exacte : son defaut connu (7.2) est
    seulement plus petit que la tolerance (demande R-5). Il ne peut pas ecrire que l'ordre 3 fait
    mieux que le premier ordre : V1 ne les separe pas (section 1). Il ne peut rien ecrire de la
    duree de vie du systeme ferme : la largeur est celle d'un etat sous absorbeur, stable sous les
    variations jouees, et rien d'autre. Le bloc de l'absorbeur adapte peut alors etre propose au
    depot.
  V1 TENU SAUF UNE CELLULE. La meme phrase, la cellule nommee, avec son ln q, sa bande et son
    creneau.
  V1 TOMBE. L'acte ecrit que la chaine ne rend pas la largeur du vide a cette tolerance, cellules
    nommees. La prediction de la note sur le vide est alors declaree non confirmee. Aucune autre
    chaine, aucun autre absorbeur de chaine, aucune autre tolerance n'est essayee sur ces cellules
    ; la loi d'echelle ne peut pas etre enoncee pour le vide.
  V1 NON CONCLUANT. L'acte donne les comptes et dit lequel des deux a manque : le lecteur
    (cellules non lues) ou la resolution (cellules non jugeables : la bande atteint la tolerance).
    Ce n'est pas une refutation, et ce n'est pas une confirmation. Pas de rejeu, pas de nouveau
    seuil.
  VP, quelle que soit son issue, ne change pas celle de V1. TENU : la chaine tient aussi a 8
    barreaux et plus, la ou le lecteur qualifie ; l'acte dit jusqu'a quelle profondeur des
    cellules ont ete jugees. TOMBE : la chaine ou le lecteur echoue en profondeur, et l'acte ne
    dit pas lequel : sous 1.33e-12 la qualification en cours de run est la SEULE garde (demande
    R-3), aucune seconde mesure 2D independante n'existe. NON LUE ou NON CONCLUANT : le lecteur ne
    lit pas la ligne profonde ; rien n'est dit de la chaine.
  Dans tous les cas : la table par cellule est publiee (statut du lecteur, plateaux et ecarts des
    quatre absorbeurs, temoin, Gamma_pl, s, bande, ln q, jugement, et les grandeurs consignees),
    les cellules non lues avec leur motif.

9. GARDES (chaque journal dit ce qu'il ne joue pas)
  G-1 canons en dur : moteur, sonde et feuille deposees du lecteur, depot, couplages et references
      du temoin et des ancres, table deposee du gel "ordre 3", table gelee, sonde, feuille ; un
      ecart arrete.
  G-2 la sonde lit le bloc du lecteur dans le fichier depose, au canon controle ; elle ne le
      recopie pas.
  G-3 forme de chaque fichier de cellule, controlee par la feuille avant tout jugement : canons,
      mode, cellule egale a celle de la table (w2, m, couplage ecrit, r_c, eta0), absorbeurs et
      boites, quatre trajectoires de douze barreaux pour le jumeau et pour le fantome, signe,
      site, energie de depart. Un fichier manquant ou non conforme : RUN INCOMPLET, rien n'est
      juge.
  G-4 instrument du lecteur : etage 0, ancres, etage 1, par les pieces deposees, tolerances
      inchangees.
  G-5 temoin : le jumeau a la geometrie de chaque cellule (section 5).
  G-6 pre-vol : avec --prevol la table du gel est refusee, un w2 candidat est refuse et le fantome
      n'est pas lu ; sans --prevol toute autre table est refusee.
  G-7 une seule execution : le pilote exige un dossier neuf et joue chaque appel une fois ; un
      code de sortie non nul l'arrete.
  G-8 ce que l'accord des quatre absorbeurs eprouve : l'independance de la largeur a la boite (80
      ou 100 couches, bord deplace de dix) et a la forme de l'absorbeur (F1 ou F2). Il n'eprouve
      PAS l'exactitude de la largeur : une erreur commune aux quatre lui echappe. Sous 1.33e-12
      (dix planchers de la decomposition dense : aucun etat n'a ete lu en dessous), c'est pourtant
      la seule garde (demande R-3) ; cela vaut pour 7 cellules de la ligne lisible, dont le
      plateau predit est sous ce seuil (MG6, MP5, MP6, PP5, PP6, PG5, PG6 ; G3* de 4.4e-15 a
      1.3e-12), et pour toute la ligne profonde.

10. ANNONCES DE LA PLUME (ecrites apres les calculs de la section 7 ; aucune 2D du fantome)
  Ce sont des jugements, pas des calculs. Probabilites :
  A-1 (0.95) l'instrument du lecteur tient (etage A).
  A-2 (0.95) le temoin tient aux 28 cellules.
  A-3 (0.60) le lecteur qualifie les seize cellules lisibles ; (0.80) au moins douze.
  A-4 V1 : TENU 0.50 ; TENU SAUF UNE CELLULE 0.05 ; TOMBE 0.08 ; NON CONCLUANT 0.32 ; le reste
      (0.05) est l'instrument.
  A-5 VP : TENU 0.35 ; TENU SAUF UNE CELLULE 0.05 ; TOMBE 0.10 ; NON LUE ou NON CONCLUANT 0.45 ;
      le reste (0.05) est l'instrument.
  A-6 (0.55) aux cellules lisibles lues, le plus grand |ln q| est sous 0.01.
  A-7 le signe du residu a MG, aux cellules lisibles lues, d'apres le constat de machine 2
      (section 7.2) : negatif, comme delta, a trois cellules au moins : 0.40 ; positif, comme la
      lecture (b), a trois au moins : 0.40. La plume ne tranche pas.
  La plume annonce donc que V1 a une chance sur deux de tenir, et que l'issue qu'elle craint le
  plus n'est pas la chute mais le NON CONCLUANT : une tolerance de 0.02 contre une bande que le
  lecteur peut elargir. Elle le gele ainsi.

11. DEROULEMENT, E19, ET CE QUI EST PERMIS
  ORDRE. (1) Machine 2 dit son tirage et certifie cette piece, la table, la sonde, la feuille et
  son banc, le pilote ; un seul tour de correction. (2) Feu vert ecrit de l'operateur. (3) Machine
  2 joue le pilote UNE fois, dans un dossier neuf. (4) Lot de resultat : les fichiers de l'etage
  A, les 28 fichiers de cellule, le verdict, les journaux, le journal du pilote. (5) Machine 1
  authentifie et rejoue la feuille. (6) Acte.
  PRE-VOL. Avant le feu vert, machine 2 peut jouer le pilote avec --prevol sur la table de pre-vol
  : l'etage A est a des points deja joues, et le jumeau a un w2 non candidat. Son pilote peut
  deriver du mien s'il le faut ; --drapeau -P et un fil BLAS par appel y sont deja.
  UNE SEULE EXECUTION. Un pilote arrete par une panne se relance ENTIER dans un dossier neuf, et
  l'acte le dit ; aucun appel n'est rejoue apres lecture de sa sortie.
  DEUX MACHINES. Le verdict est celui de la feuille jouee par machine 2 dans le run. Machine 1 la
  rejoue sur les fichiers du lot : la feuille ne calcule aucune chaine, les predictions sont dans
  la table ; les deux verdicts doivent etre les memes. S'ils different, l'acte donne les deux et
  retient la lecture la MOINS favorable a l'enonce.
  E19. Aucune des deux machines ne lit le fantome a une cellule avant le feu vert ; machine 1 n'y
  lit rien en 2D avant d'avoir recu et authentifie le lot de resultat. Ce gel ne se rejoue pas
  sous d'autres seuils, d'autres gardes, une autre chaine ou d'autres cellules apres lecture.

12. COUTS (a mesurer au pre-vol de machine 2, pas a promettre)
  Etage A : 1365 s de calcul en trois appels sur le conteneur de machine 1 ; le run du gel "ordre
  3" l'a joue sur BOCAL4. Etage B : par cellule, 48 lectures du jumeau et 48 du fantome ; a m =
  16, machine 2 a mesure sur BOCAL4 de 2.9 s a 4.4 s par lecture du jumeau (lot d4f95772710d545c)
  ; sur machine 1, 48 lectures du jumeau ont pris 113 s a m = 3 et 147 s a m = 8. Etage C :
  quelques secondes.

13. LIMITES DECLAREES
  L-1 L'objet juge est UNE chaine : les blocs deposes, forme symetrique, sous UN absorbeur de
      chaine, celui du bloc 49a40d9098b55361. Aucune autre definition n'est essayee.
  L-2 V1 ne separe pas l'ordre 3 des ordres inferieurs ni de la loi d'echelle (section 1).
  L-3 La reference est une largeur sous absorbeur, qualifiee par sa stabilite sous quatre
      absorbeurs (G-8). Sous 1.33e-12 aucune seconde mesure 2D n'existe. Le jumeau prouve un
      plancher, pas une exactitude.
  L-4 Aux etats juges des deltas 98 et 100 le lecteur n'a jamais lu le systeme a fantome a |delta|
      < 0.030, ni un etat de largeur inferieure a 1.33e-12 : ce gel l'y envoie, en desaccord a
      toutes les cellules, en largeur a celles que nomme G-8. Qu'il y lise juste n'est appuye que
      par des faits indirects (note sur le vide, section 2 ; faisabilite au jumeau par machine 2,
      a w2 = 3999/2000 et 4001/2000).
  L-5 Seules des cellules QUALIFIEES sont jugees. Une cellule que le lecteur ne qualifie pas peut
      etre une cellule ou la chaine echoue : les comptes de V1 (douze, deux par creneau) bornent
      cet effet sans l'annuler.
  L-6 La tolerance ne sort pas d'une theorie de l'erreur : elle vient de l'etendue de la chaine et
      d'une extrapolation depuis des etats excites a |delta| >= 0.03, dont le sens meme est ambigu
      au vide (7.2).
  L-7 Quatre w2, un seul par creneau : rien n'est dit de la dependance en delta a l'interieur d'un
      creneau.
  L-8 Le creneau PP est sorti a w2 = 2.005, un des quatre w2 candidats que les notes de ce jour
      avaient deja calcules en chaine seule (premiere partie, 4.8 et 9) ; et le creneau PG a w2 =
      2.017, celui de la graine de demonstration. Aucune 2D n'y existe.
  L-9 Un seul modele (x^5, W1 = 1, canal 2:1), un seul etat. Rien n'est dit de la dynamique du
      systeme ferme.

14. ECARTS DECLARES, ET REPONSES AUX DEMANDES DE MACHINE 2
  E-1 La premiere partie annoncait (section 11) "la sonde du lecteur derivee du depot" et "sa
      feuille". Il n'y a pas de derivation : la sonde et la feuille de ce gel sont nouvelles et
      executent les routines deposees depuis leurs fichiers ; l'etage A joue les pieces deposees
      telles quelles.
  E-2 Les ancres et le temoin positif que la premiere partie annoncait sont ceux de l'etage A,
      inchanges ; le temoin de chaque cellule est le jumeau sans fantome, lu par la sonde de ce
      gel.
  E-3 L'enonce V2 de la note sur le vide (forme fermee) n'est pas pose (section 6).
  E-4 R-1 : T = 0.02, prise telle quelle. R-2 : la regle NON JUGEABLE est posee, et la bande porte
      en plus l'etalement du lecteur, ajout de la plume. R-3 : G-8 et section 8. R-4 : le jumeau a
      chaque cellule, dans le run. R-5 : aucun enonce sur le signe ; il est consigne, dit en
      section 8, et l'annonce A-7 en parle sans trancher. Machine 2 peut refuser A-7.
  E-5 Le lot de reception de machine 1 (53c604647e78afa4) disait que l'annonce donnerait "le signe
      attendu du residu et sa taille". Les chaines aux cellules montrent que le signe attendu
      depend de la lecture (7.2) : l'annonce donne les deux.
  E-6 Un cas du banc portait une attente fausse au premier passage (4.3).
  E-7 Le pilote passe -B a python (aucun fichier de cache ecrit a cote des scripts deposes) : un
      premier pre-vol, lance sans ce drapeau, a ete arrete au bout de moins d'une minute et
      relance ; rien n'en est garde.

15. CE QUE MACHINE 2 CERTIFIE
  (a) que la table gelee porte les 28 cellules de SON tirage, avec les memes couplages ecrits ;
  (b) que les predictions de la table (G3*, etendue) sont celles de sa table de la premiere
      partie, et que G2*, G1*, Phi* et la forme fermee se recalculent ;
  (c) que la sonde ne fait qu'executer le bloc depose a la geometrie de la section 4.2, et que la
      feuille applique les sections 5 et 6 ; que le banc mord ;
  (d) que les nombres des sections 3 et 7 sortent des pieces ;
  (e) le pre-vol sur BOCAL4 ;
  (f) qu'elle accepte, ou refuse, les ecarts de la section 14, la bande (etendue + s), le facteur
      1e-6 du temoin, les comptes des issues, et l'annonce A-7.

16. PIECES DE CE LOT (convention B)
    b71206e5daf6c741  table_cellules_gel_vide_v1.json
    d7f37c7e2f08a2ea  predictions_vide_machine1_v1.py
    ae577eea6a605b4e  predictions_vide_machine1_v1.log
    034c201f5125b0af  tirage_vide_graine_479579_machine1_v1.log
    0f82986cca133330  sonde_vide_machine1_v1.py
    ac39a24def6c7420  feuille_vide_machine1_v1.py
    a38b1550f8f5e3cf  pilote_gel_vide_machine1_v1.py
    0892944809929123  banc_feuille_vide_machine1_v1.py
    6e9f47735c18ab98  banc_feuille_vide_machine1_v1.log
    9e57ea5b59e529f8  banc_feuille_vide_machine1_v1_premier_passage_attente_fausse.log
    45ad4e103788d05f  banc_feuille_vide_machine1_v1_retouche_b24.diff
    7d18a4b4cb13316f  essai_refus_machine1_v1.py
    441b92e462af8165  essai_refus_machine1_v1.log
    a5a654a84750effd  table_prevol_vide_machine1_v1.py
    916eec7c3b6f6a47  table_cellules_prevol_vide_v1.json
    d977ce1f01d3b429  comparaison_prevol_vide_machine1_v1.py
    cf079d1220d95056  comparaison_prevol_vide_machine1_v1.log
    8a95ccb23b0585c6  comparaison_prevol_vide_v1.json
    f6a0167c19b222bd  prevol_pilote_gel_vide.log
    cdb18cee663eb537  prevol_verdict_ter_instrument.json
    2f6173956ec242c2  prevol_sonde_vide_PV3.json
    009d6f33a8c4d1a0  prevol_sonde_vide_PV8.json
    40ee64e5ab86843b  prevol_verdict_vide.json
    (ce script)       construction_gel_vide_partie2_machine1_v1.py

-- FIN gel_largeur_vide_partie2_instrument_enonces_pre_enregistrement_v1 --
