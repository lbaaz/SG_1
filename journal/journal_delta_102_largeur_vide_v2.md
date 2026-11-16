DELTA nn -- LARGEUR DU VIDE, CHAINE D'ORDRE 3 SOUS ABSORBEUR ADAPTE : RUN DU 16/11/2026 SOUS LE GEL
EN DEUX PARTIES b57c9ccdd3946261 (REGLE DE TIRAGE) ET eebd979f18d8db48 (INSTRUMENT, ENONCES).
VERDICT : V1 TENU, VP TENU.
-- VERSION 2 (cinq precisions proposees par machine 2 a son contreseing de la version 1, toutes
retenues : nn.9 ; aucun nombre juge, aucun tableau ne change)
(plume machine 1 ; certification, run, seconde feuille et contreseing de la version 1 machine 2)
=======================================================================

nn.0 POSITION
  Ce delta rend le run unique du gel "largeur du vide". Sa question : la largeur de l'etat que
  porte le site (0, 0), jamais lue en 2D avant ce run, est-elle celle que predit une chaine a une
  dimension, l'ordre 3 des blocs deposes sous un absorbeur de chaine adapte au saut, a des
  cellules que personne n'a choisies ? Vingt-huit cellules ont ete tirees par une graine de
  l'operateur (479579) : quatre w2 (delta = -0.018, -0.003, +0.005, +0.017), sept profondeurs de
  barriere chacun (3, 4, 5, 6 barreaux : ligne lisible ; 8, 12, 16 : ligne profonde). Les
  predictions etaient gelees dans une table (b71206e5daf6c741) avant toute lecture.
  Reponse de la feuille du run : V1 TENU (16 cellules lisibles sur 16 tiennent), VP TENU (12
  profondes sur 12). Aucune cellule n'est tombee, aucune n'est non jugeable, aucune n'est non lue
  : les 28 cellules sont QUALIFIEES par le lecteur et leur temoin tient. Machine 1 a rejoue la
  feuille sur les fichiers du run : meme verdict, champ par champ.
  A savoir avant tout le reste. (1) L'ecart de la chaine au plateau lu, |ln q|, vaut 0.00068 au
  plus aux cellules lisibles (MG6) et 0.00134 au plus aux profondes (PG16), pour des tolerances de
  0.02 et 0.05, sur 23.5 decades de largeur (de 2.9e-09 a 9.5e-33). (2) Cet ecart est sous
  l'etendue de la chaine a 28 cellules sur 28 : le gel est tenu a ses tolerances, et il ne MESURE
  pas l'erreur de la chaine en dessous de ce que son absorbeur laisse indetermine. (3) La largeur
  jugee est celle d'un etat sous absorbeur ; cet acte ne dit rien de la duree de vie du systeme
  ferme.

nn.1 CE QUI A ETE JOUE, ET DANS QUEL ORDRE
  Ouverture. L'operateur a ecrit a machine 1 "on gele et on avance !" (16/11/2026, 12 h 19) :
  declaration de machine 1, que machine 2 dit ne pas pouvoir attester. A l'operateur de
  l'attester.
  Premiere partie du gel (b57c9ccdd3946261, regle de tirage et d'eligibilite, lot
  879ea2e51c7d7f4f) : certifiee par machine 2 sans morsure (lot d4f95772710d545c, 69 pieces).
  Graine donnee par l'operateur a machine 1 ("la graine 479579", 13 h 34) ; tirage identique sur
  les deux machines (lot 5921fcd984d6de5b). Seconde partie (eebd979f18d8db48, lot
  b1919dc9468dc437) : certifiee par machine 2 AVANT le run (lot f989369a3ac22f98, 55 pieces) aux
  cinq points demandes ; aucune correction d'un nombre ou d'une regle ; deux corrections de TEXTE
  (C-1, C-2 : nn.9). Sa feuille, ecrite du texte seul, rend les memes verdicts que celle du gel
  sur 5 100 dossiers synthetiques ; son pre-vol sur BOCAL4 tient (1 001 s).
  Rectificatif. Machine 1 a ecrit les deux corrections de texte AVANT le run (336913aecc732cdf,
  lot 71ec801a5f86e068) ; la seconde partie n'a pas de version 2, la table et l'instrument n'ont
  pas change. Machine 2 dit l'avoir authentifie avant de lancer (canon du manifeste recalcule par
  elle : 71ec801a5f86e068 ; son rejeu du script de verification rend la console de machine 1).
  Feu vert. Machine 2 rapporte que l'operateur lui a ecrit, le 16/11 a 19 h 10 (heure de BOCAL4) :
  "M1 a livre, tu peux jouer ensuite si tout te semble propre". Elle le lit comme le feu vert
  ecrit, conditionnel, et dit avoir d'abord authentifie le rectificatif et verifie sa machine.
  Machine 1 n'a pas vu ce message ; l'operateur lui a ecrit a 19 h 18 : "M2 vient de lancer le
  run." C'est a l'operateur de l'attester.
  Run. UN run, dans un dossier neuf, lance le 2026-11-16 a 19:13:54 et fini a 19:57:11 (heure de
  BOCAL4) ; duree totale 2597 s ; 33 appels, tous au code 0 ; aucun arret, aucune relance (journal
  du pilote, 2d8e6692d862fa37). Pilote joue : celui du gel, tel quel (a38b1550f8f5e3cf), 8
  processus, drapeau -P, lance par un lanceur de machine 2 (5a73b5a492d5d4a2) qui recalcule 12
  canons et ne modifie aucune piece. Table jouee : b71206e5daf6c741, sans --prevol. Les canons que
  le pilote imprime au depart sont ceux du gel. Durees : etage A 20 s, 659 s et 700 s (etage 0,
  ancres, etage 1, en parallele) ; les 28 cellules de 309 a 866 s chacune, 8 a la fois.
  E19. Machine 1 n'a lu en 2D le systeme a fantome a aucune cellule, ni l'etat (0, 0) a aucun w2,
  ni avant ni apres le run : son rejeu ne joue que la feuille. Machine 2 declare n'avoir lu, avant
  la fin du pilote, que le journal de demarrage de son lanceur, et n'avoir rejoue aucun appel.

nn.2 L'INSTRUMENT
  Instrument du lecteur (etage 0, ancres, etage 1, pieces deposees, tolerances inchangees) : TIENT
  ; canon de son verdict cc54f4bc4e175143. Machine 2 le dit egal, champ pour champ, a celui de son
  pre-vol, aux durees pres.
  Lecteur. 28 cellules sur 28 QUALIFIEES ; les quatre absorbeurs en PLATEAU partout (112 plateaux
  sur 112) ; 1344 lectures du fantome sur 1344 suivies ; poids du site (0, 0) au moins 0.999 ;
  residu au plus 6.9e-12 ; aucun decalage repris. L'etalement du plateau sous A vaut 0.0002 au
  plus ; le plus grand ecart entre absorbeurs 0.0031 (PP8). L'etalement du lecteur s, le plus
  grand des deux, va de 0.0001 a 0.0031, mediane 0.0011. Machine 2 l'avait mesure aux 144 etats
  deja lus du delta 100 : mediane 0.0009, au plus 0.0052.
  Temoin. Le jumeau sans fantome, a la geometrie de chaque cellule : 1344 lectures sur 1344
  suivies ; il tient aux 28 cellules ; sa plus grande largeur vaut au plus 1.3e-27 du plateau,
  pour un seuil de 1e-06.
  Sous le plancher. 19 cellules sur 28 ont un plateau sous 1.33e-12 (les 12 profondes, et MG6 MP5
  MP6 PP5 PP6 PG5 PG6) : la qualification en cours de run y est la seule garde (gel, G-8).
  Sorties du run (convention B) : verdict de l'instrument cc54f4bc4e175143 ; verdict de la feuille
  8472dba8919a9b6e ; les 28 fichiers de cellule portent les canons que le journal du pilote
  imprime.

nn.3 LE VERDICT DE LA FEUILLE DU RUN
  ln q = ln G3* (table gelee) - ln Gamma_pl : positif quand la chaine depasse la lecture. Bande b
  = etendue de la chaine sur ses dix-huit variantes + etalement s du lecteur. TIENT si |ln q| <= T
  - b ; marge = T - b - |ln q|.
    cellule  w2         m   ln Gamma_pl  s       etendue  bande b  ln q      T     marge   jugement
    MG3      991/500    3   -19.6443     0.0016  0.0013   0.0030   +0.00024  0.02  0.0168  TIENT
    MG4      991/500    4   -23.4596     0.0015  0.0014   0.0029   +0.00042  0.02  0.0167  TIENT
    MG5      991/500    5   -27.3358     0.0004  0.0026   0.0029   +0.00055  0.02  0.0165  TIENT
    MG6      991/500    6   -31.2989     0.0002  0.0022   0.0024   +0.00068  0.02  0.0169  TIENT
    MG8      991/500    8   -39.3244     0.0018  0.0054   0.0072   +0.00050  0.05  0.0423  TIENT
    MG12     991/500    12  -55.6116     0.0005  0.0092   0.0097   +0.00050  0.05  0.0398  TIENT
    MG16     991/500    16  -72.0324     0.0001  0.0086   0.0087   +0.00122  0.05  0.0401  TIENT
    MP3      1997/1000  3   -21.4263     0.0022  0.0027   0.0048   -0.00005  0.02  0.0151  TIENT
    MP4      1997/1000  4   -25.2361     0.0005  0.0029   0.0034   +0.00035  0.02  0.0163  TIENT
    MP5      1997/1000  5   -29.1067     0.0005  0.0020   0.0025   +0.00036  0.02  0.0172  TIENT
    MP6      1997/1000  6   -33.0638     0.0010  0.0058   0.0068   +0.00007  0.02  0.0131  TIENT
    MP8      1997/1000  8   -41.0771     0.0029  0.0064   0.0093   -0.00006  0.05  0.0407  TIENT
    MP12     1997/1000  12  -57.3391     0.0003  0.0091   0.0094   +0.00041  0.05  0.0402  TIENT
    MP16     1997/1000  16  -73.7344     0.0003  0.0074   0.0077   +0.00047  0.05  0.0418  TIENT
    PP3      401/200    3   -20.9155     0.0020  0.0032   0.0052   +0.00019  0.02  0.0146  TIENT
    PP4      401/200    4   -24.7237     0.0002  0.0042   0.0045   +0.00020  0.02  0.0153  TIENT
    PP5      401/200    5   -28.5925     0.0011  0.0041   0.0052   +0.00031  0.02  0.0145  TIENT
    PP6      401/200    6   -32.5478     0.0018  0.0052   0.0070   +0.00024  0.02  0.0128  TIENT
    PP8      401/200    8   -40.5572     0.0031  0.0068   0.0099   -0.00031  0.05  0.0398  TIENT
    PP12     401/200    12  -56.8109     0.0014  0.0083   0.0096   +0.00053  0.05  0.0398  TIENT
    PP16     401/200    16  -73.1973     0.0001  0.0054   0.0055   -0.00030  0.05  0.0442  TIENT
    PG3      2017/1000  3   -19.6990     0.0006  0.0054   0.0060   +0.00017  0.02  0.0138  TIENT
    PG4      2017/1000  4   -23.5064     0.0019  0.0063   0.0082   +0.00032  0.02  0.0115  TIENT
    PG5      2017/1000  5   -27.3743     0.0021  0.0069   0.0090   +0.00006  0.02  0.0110  TIENT
    PG6      2017/1000  6   -31.3284     0.0023  0.0070   0.0093   -0.00058  0.02  0.0101  TIENT
    PG8      2017/1000  8   -39.3352     0.0016  0.0084   0.0100   -0.00022  0.05  0.0398  TIENT
    PG12     2017/1000  12  -55.5832     0.0007  0.0077   0.0085   +0.00073  0.05  0.0408  TIENT
    PG16     2017/1000  16  -71.9634     0.0004  0.0068   0.0073   +0.00134  0.05  0.0414  TIENT
  V1 (16 cellules lisibles) : TENU ; 16 TIENT, 0 TOMBE, 0 NON JUGEABLE, 0 NON LUE ; quatre tenues
  a chaque creneau. VP (12 cellules profondes, hors de V1) : TENU ; 12 TIENT, 0 TOMBE, 0 NON
  JUGEABLE, 0 NON LUE. Le run est complet.
  Le lecteur, par cellule : barreau de depart du plateau sous A, B, C, D ; etalement du plateau
  sous A ; ecarts |ln| de B, C, D a A ; rapport de la plus grande largeur du jumeau au plateau.
  Statut QUALIFIE et quatre PLATEAUX partout.
    cellule  k0 (A B C D)   etalement A  ecart B   ecart C   ecart D   jumeau / plateau
    MG3      -2 -1  1 -2    2.1e-05      6.9e-06   1.6e-03   4.6e-06   1.3e-27
    MG4      -2 -1  2 -2    2.9e-05      7.1e-06   1.5e-03   1.8e-05   1.4e-29
    MG5      -2 -1  2 -2    1.8e-05      4.6e-06   3.8e-04   3.8e-06   2.0e-31
    MG6      -1 -1  2 -2    1.2e-05      2.3e-06   2.1e-04   5.1e-06   4.1e-33
    MG8      -1  0  2 -2    4.9e-05      1.1e-05   1.8e-03   1.8e-05   1.9e-36
    MG12     -1 -1  2  0    6.3e-07      1.6e-08   5.1e-04   7.3e-07   4.5e-52
    MG16     -1 -1  2 -1    3.0e-06      5.4e-07   8.3e-05   8.7e-07   1.3e-67
    MP3      -1 -1  1 -2    2.2e-05      6.0e-06   2.2e-03   9.5e-06   3.2e-36
    MP4      -1 -1  2 -2    2.0e-05      1.5e-06   5.1e-04   1.0e-06   3.2e-39
    MP5      -1 -1  1 -2    6.2e-06      1.0e-06   4.9e-04   8.1e-06   1.5e-41
    MP6       0  0  2 -1    3.6e-05      9.9e-07   1.0e-03   2.4e-06   3.6e-44
    MP8       0  0  2 -1    3.8e-05      6.5e-06   2.9e-03   8.7e-06   3.1e-48
    MP12      0  0  3  0    1.0e-05      1.8e-06   2.7e-04   3.3e-06   9.7e-70
    MP16      0  0  3  0    1.2e-05      1.5e-06   3.5e-04   3.4e-06   8.0e-91
    PP3      -2 -1  2 -2    4.1e-05      1.4e-05   2.0e-03   1.0e-05   6.7e-34
    PP4      -1 -1  2 -2    3.1e-06      1.1e-07   2.2e-04   3.9e-06   1.6e-36
    PP5      -1 -1  0 -2    2.7e-05      4.2e-06   1.1e-03   7.8e-06   8.5e-39
    PP6       0  0  3 -1    3.2e-05      1.3e-05   1.8e-03   1.1e-05   4.8e-41
    PP8       0  0  2 -1    5.4e-05      3.1e-06   3.1e-03   8.5e-06   5.2e-45
    PP12      0  0  2  0    2.5e-05      3.1e-06   1.4e-03   5.6e-06   8.5e-65
    PP16      0  0  2 -1    2.0e-06      1.2e-07   9.6e-05   3.6e-06   2.2e-84
    PG3      -2 -1  1 -2    1.9e-04      2.0e-05   6.4e-04   5.3e-05   7.4e-28
    PG4      -2 -1  2 -2    1.3e-04      4.2e-07   1.9e-03   5.9e-06   7.4e-30
    PG5      -1 -1  2 -2    7.8e-05      1.4e-05   2.1e-03   2.0e-05   1.0e-31
    PG6      -1 -1  2 -2    7.5e-05      1.4e-05   2.3e-03   2.3e-05   2.0e-33
    PG8      -1 -1  2 -1    7.0e-06      2.4e-06   1.6e-03   8.7e-06   8.6e-37
    PG12     -1  0  3 -1    2.6e-05      5.9e-06   7.5e-04   1.4e-05   1.4e-52
    PG16     -1  0  3 -1    1.4e-05      3.4e-06   4.4e-04   8.1e-06   2.7e-68

nn.4 LE REJEU DE MACHINE 1 (etape 5 du gel)
  Lot de resultat authentifie : 9a14bf95fa8c6d20, 82 pieces sur 82. La piece de reception
  (c815876f0ff7d66b) et son essai (4adc285659120eb8, 20 cas tenus sur 20) ont ete ecrits PENDANT
  le run, avant tout resultat ; machine 1 en a donne les canons a l'operateur avant de recevoir le
  lot : declaration de machine 1, a l'operateur de l'attester. Elle fixait d'avance comment
  compter les annonces (nn.9).
  Feuille du gel (ac39a24def6c7420), rejouee par machine 1 sur les fichiers du run : VERDICTS
  IDENTIQUES. 1576 champs compares (les 1517 feuilles de l'arbre du verdict, et 59 listes sans
  identifiant, toutes vides, comptees chacune pour un champ), dont 816 nombres ; aucun champ
  d'issue, de jugement ou de statut ne differe, ni aucun autre champ discret ; plus grand ecart
  d'un nombre : 1.4e-14. La regle "deux machines" du gel (lecture la moins favorable) n'a pas a
  jouer.
  Hors verdict, machine 2 a joue sa propre feuille (a6754241629160a7) sur les memes fichiers :
  meme verdict, memes jugements a 28 cellules sur 28. Elle note que ce zero est moins fort qu'il
  n'en a l'air, les deux feuilles appelant la meme routine deposee du lecteur. Et elle a recalcule
  ln q avec SES predictions de chaine : ecart de 4.26e-09 au plus a celui de la feuille. Le chemin
  du fantome de la sonde n'avait jamais tourne avant le run (le pre-vol ne le lit pas, G-6). Ce
  qui le garde est que ses 28 largeurs retrouvent des chaines calculees de deux cotes, A MOTEUR
  COMMUN (nn.10) : cet accord garde la reduction a une dimension, les absorbeurs, le lecteur et
  l'orchestration de la sonde ; il ne garde pas les elements de matrice.

nn.5 LECTURE, ENONCE PAR ENONCE
  V1. Aux 16 cellules lisibles (3 a 6 barreaux, |delta| de 0.003 a 0.018, plateaux de 4.4e-15 a
  2.9e-09) : |ln q| vaut 0.00028 en mediane et 0.00068 au plus (MG6) pour T = 0.02 ; la plus
  petite marge est 0.0101 (PG6). La bande va de 0.0024 a 0.0093 : l'etendue de la chaine y entre
  pour 0.0013 a 0.0070, le lecteur pour 0.0002 a 0.0023.
  VP. Aux 12 cellules profondes (8, 12 et 16 barreaux, plateaux de 9.5e-33 a 8.3e-18) : |ln q|
  vaut 0.00048 en mediane et 0.00134 au plus (PG16) pour T = 0.05 ; la plus petite marge est
  0.0398 (PP8). Des cellules ont ete jugees jusqu'a 16 barreaux, aux quatre creneaux. Toute cette
  ligne est sous 1.33e-12 : ce que VP dit, il le dit d'une reference que rien d'autre que sa
  stabilite sous quatre absorbeurs ne garde.
  Ce que ces nombres ne permettent pas. |ln q| est sous l'etendue de la chaine a 28 cellules sur
  28, sous la bande a 28, et sous l'etalement du lecteur a 21. Le gel tient donc avec une marge
  large, mais la taille de l'ecart (quelques dix-milliemes) est en dessous de ce que la chaine et
  le lecteur determinent chacun : elle n'est pas une mesure de l'erreur de la chaine.

nn.6 CE QUI ETAIT CONSIGNE SANS ETRE JUGE
  Les autres predictions de la table, a la meme lecture : ln q de l'ordre 2, du premier ordre, de
  la loi d'echelle |delta| Phi*(kappa), de la forme fermee (avec la definition de M0 du
  rectificatif) ; et ln(Gamma_pl / |delta|).
    cellule  ordre 3    ordre 2   ordre 1   loi d'echelle  forme fermee  ln(Gamma_pl/|delta|)
    MG3      +0.00024   +0.0014   +0.0062   +0.0106        +0.0602       -15.6269
    MG4      +0.00042   +0.0019   +0.0110   +0.0167        +0.0561       -19.4422
    MG5      +0.00055   +0.0020   +0.0158   +0.0228        +0.0560       -23.3184
    MG6      +0.00068   +0.0022   +0.0213   +0.0297        +0.0580       -27.2815
    MG8      +0.00050   +0.0022   +0.0317   +0.0431        +0.0657       -35.3070
    MG12     +0.00050   +0.0024   +0.0554   +0.0726        +0.0877       -51.5942
    MG16     +0.00122   +0.0033   +0.0783   +0.1015        +0.1136       -68.0151
    MP3      -0.00005   -0.0000   +0.0000   +0.0008        +0.0504       -15.6171
    MP4      +0.00035   +0.0004   +0.0005   +0.0015        +0.0409       -19.4269
    MP5      +0.00036   +0.0004   +0.0007   +0.0019        +0.0350       -23.2975
    MP6      +0.00007   +0.0001   +0.0015   +0.0029        +0.0312       -27.2547
    MP8      -0.00006   +0.0000   +0.0022   +0.0041        +0.0267       -35.2680
    MP12     +0.00041   +0.0005   +0.0057   +0.0085        +0.0236       -51.5300
    MP16     +0.00047   +0.0006   +0.0078   +0.0116        +0.0237       -67.9252
    PP3      +0.00019   +0.0004   +0.0020   +0.0008        +0.0505       -15.6172
    PP4      +0.00020   +0.0004   +0.0015   -0.0001        +0.0393       -19.4254
    PP5      +0.00031   +0.0005   +0.0006   -0.0014        +0.0317       -23.2942
    PP6      +0.00024   +0.0004   +0.0001   -0.0023        +0.0260       -27.2495
    PP8      -0.00031   -0.0001   -0.0019   -0.0050        +0.0176       -35.2589
    PP12     +0.00053   +0.0008   -0.0042   -0.0090        +0.0061       -51.5126
    PP16     -0.00030   -0.0000   -0.0082   -0.0145        -0.0024       -67.8990
    PG3      +0.00017   +0.0020   +0.0122   +0.0081        +0.0577       -15.6245
    PG4      +0.00032   +0.0024   +0.0117   +0.0064        +0.0458       -19.4319
    PG5      +0.00006   +0.0024   +0.0107   +0.0041        +0.0372       -23.2998
    PG6      -0.00058   +0.0020   +0.0100   +0.0021        +0.0304       -27.2539
    PG8      -0.00022   +0.0027   +0.0074   -0.0032        +0.0194       -35.2607
    PG12     +0.00073   +0.0039   +0.0031   -0.0129        +0.0022       -51.5087
    PG16     +0.00134   +0.0045   -0.0031   -0.0247        -0.0126       -67.8889
  Ordres. Ligne lisible : l'ordre 2 est a 0.0024 au plus du plateau (PG4), le premier ordre a
  0.0213 (MG6), la loi d'echelle a 0.0297 (MG6), la forme fermee a 0.0602 (MG3) ; l'ordre 3 est
  plus pres que l'ordre 2 a 15 cellules sur 16, que le premier ordre a 14, que la loi d'echelle a
  15. Ligne profonde : 0.0045 (PG16), 0.0783 (MG16), 0.1015 (MG16), 0.1136 (MG16) ; plus pres a 9,
  12 et 12 cellules sur 12. Le gel disait (section 1) que V1 ne separe pas les ordres, et que les
  corrections a la loi d'echelle ne seraient eprouvees que sur la ligne profonde du creneau MG si
  elle etait lue. Elle l'a ete : a MG12 et MG16 l'ordre 3 est a +0.0005 et +0.0012 du plateau, le
  premier ordre a +0.0554 et +0.0783, la loi d'echelle a +0.0726 et +0.1015, pour des bandes de
  0.0097 et 0.0087. Ce sont des nombres consignes : aucun enonce du gel ne portait sur eux.
  Superposition. A profondeur egale les quatre creneaux ont le meme kappa (a 3e-06 pres) : la loi
  d'echelle les superposerait en ln(Gamma_pl / |delta|). Ils s'ecartent de 0.0098 a 3 barreaux,
  0.0321 a 6, 0.0481 a 8, 0.0855 a 12 et 0.1262 a 16. La chaine predit ces ecarts (0.0097, 0.0316,
  0.0473, 0.0858, 0.1263) : une fois sa correction retiree il reste 0.0003, 0.0013, 0.0008, 0.0003
  et 0.0016.
  Ce reste est sous la plus petite etendue de chaine de chacune de ces profondeurs (0.0013,
  0.0022, 0.0054, 0.0077 et 0.0054) : lui non plus ne mesure pas l'erreur de la chaine (nn.5).
  Signe de ln q. Positif a 22 cellules sur 28, negatif a 6 ; mediane +0.00032. Par creneau : MG 7
  sur 7, MP 5 sur 7, PP 5 sur 7, PG 5 sur 7. A delta < 0 il est positif a 12 cellules sur 14, a
  delta > 0 a 10 sur 14 : il ne suit pas le signe de delta (il en a le signe a 12 cellules sur
  28). Il a le signe de la lecture (b) a 19. Aux 11 cellules lisibles ou les lectures (a) et (b)
  different, il a le signe de (b) a 7 (MG3 MG4 MG5 MG6 MP4 MP5 MP6) et celui de (a) a 4 (MP3 PP4
  PP5 PP6) ; aux 5 ou elles coincident, le signe commun a 4.
  Ces signes ne departagent rien : la taille est sous l'etendue de la chaine a toutes les
  cellules. Aux quatre cellules lisibles de MG, les seules ou le rectificatif attendait que le
  signe puisse se lire, ln q vaut +0.00024, +0.00042, +0.00055 et +0.00068 pour des etendues de
  0.0013, 0.0014, 0.0026 et 0.0022 ; la lecture (b) y attendait de 0.0008 a 0.0022 pour la part
  manquee mediane des etats joues. Machine 2 note qu'un petit decalage positif commun aux deux
  signes de delta decrirait aussi ces 28 nombres, et que personne ne l'avait ecrit avant le run.
  L'acte ne retient ni l'un ni l'autre : le gel ne departage pas (a) de (b).

nn.7 LES ANNONCES DE LA PLUME, CONFRONTEES AU RUN (gel, section 10)
  A-1 (0.95, l'instrument tient) : il tient. A-2 (0.95, le temoin tient aux 28 cellules) : il
  tient aux 28. A-3 (0.60 pour seize cellules lisibles qualifiees, 0.80 pour douze au moins) : 16
  sur 16. A-4 : la plume donnait 0.50 a "V1 TENU", 0.32 a "NON CONCLUANT", 0.08 a "TOMBE" : c'est
  V1 TENU. A-5 : 0.35 a "VP TENU", 0.45 a "NON LUE ou NON CONCLUANT", 0.10 a "TOMBE" : c'est VP
  TENU. A-6 (0.55, plus grand |ln q| lisible sous 0.01) : 0.00068, a MG6. A-7 : la plume donnait
  0.40 a "negatif a trois cellules lisibles de MG au moins" et 0.40 a "positif a trois au moins" :
  il est positif aux 4 ; aucune ne sort de sa bande, et l'annonce, vraie dans sa lettre, ne
  tranche rien (nn.6).
  Pour la seconde fois de suite l'issue la plus favorable a eu lieu : E1 TENU, annonce a 0.35, au
  gel "ordre 3" ; VP TENU, annonce a 0.35 contre 0.45 pour NON LUE ou NON CONCLUANT, ici. V1 TENU
  etait deja l'issue la plus probable du tableau de la plume (0.50). Deux issues ne mesurent pas
  un biais.
  La plume ecrivait que l'issue qu'elle craignait le plus etait le NON CONCLUANT, "une tolerance
  de 0.02 contre une bande que le lecteur peut elargir" : aucune cellule n'est non jugeable ; la
  plus grande bande lisible vaut 0.0093 et le lecteur n'y met que 0.0023 au plus. Elle n'avait pas
  la mesure de l'etalement du lecteur aux etats deja lus quand elle a gele ses annonces
  (rectificatif, section 4) ; ce n'est pas une excuse : la mesure etait a sa portee.

nn.8 CE QUE CET ACTE ECRIT, ET CE QU'IL N'ECRIT PAS (gel, section 8)
  V1 TENU. L'acte ecrit la phrase que le gel autorisait : a seize cellules tirees au sort, de 3 a
  6 barreaux et pour |delta| de 0.003 a 0.018, la chaine d'ordre 3 sous absorbeur adapte rend la
  largeur de l'etat porte par (0, 0) a 0.02 pres en logarithme, au-dela de sa propre etendue et de
  l'etalement du lecteur.
  VP TENU. La chaine tient aussi a 8, 12 et 16 barreaux, a 0.05 pres, aux douze cellules
  profondes, toutes qualifiees par le lecteur ; des cellules ont ete jugees jusqu'a 16 barreaux.
  Le bloc de l'absorbeur adapte (49a40d9098b55361) peut etre propose au depot ; la decision est a
  l'operateur.
  Il n'ecrit PAS : que la chaine est exacte, ni qu'elle l'est a un millieme (l'ecart lu est sous
  son etendue : nn.5) ; que l'ordre 3 est JUGE meilleur que le premier ordre ou que la loi
  d'echelle (c'est consigne aux cellules profondes de MG, nn.6 ; ce n'etait pas un enonce) ; la
  loi d'echelle comme resultat juge pour le vide (sa superposition est consignee, avec ses ecarts)
  ; laquelle des lectures (a) et (b) vaut au vide ; rien des cellules non tirees, des |delta| hors
  de 0.003 a 0.018, des centiemes exclus ; rien de la duree de vie du systeme ferme : la largeur
  est celle d'un etat sous absorbeur, stable sous les variations jouees, et rien d'autre. Aucun
  seuil, aucune garde, aucune tolerance n'a ete regle apres lecture ; ce gel ne se rejoue pas.

nn.9 CORRECTIONS DE MACHINE 2, DEFAUTS DE LA PLUME, ECARTS
  C-1 (correction de texte de machine 2 ; D-VIDE-7). La seconde partie ne disait pas comment M0
    est pris dans la forme fermee. Il l'est avec kappa a la cellule (rectificatif, section 1) ;
    avec la definition de la note sur la loi d'echelle la forme fermee differerait de 3.42 au pire
    (a MG16). La loi s'ecrit en kappa, le saut sur le desaccord, pas en g / |delta|. Sans effet
    sur un verdict : la forme fermee est consignee.
  C-2 (correction de texte de machine 2 ; D-VIDE-8). La seconde partie disait qu'a 184 des 185
    etats joues la chaine rend une correction trop petite ; c'est a 182 (rectificatif, section 2).
    Sans effet.
  A-7. Machine 2 precisait que les lectures (a) et (b) different a MG et a MP ; le rectificatif
    ajoutait que seule MG pouvait les departager par la taille. Le run ne les departage a aucune
    (nn.6).
  D-VIDE-1 a D-VIDE-5 sont declares dans la note sur le vide ; D-VIDE-6 dans le lot de reception
    53c604647e78afa4.
  Les ecarts E-1 a E-7 de la seconde partie restent tels qu'ecrits (section 14).
  Conventions de comptage des annonces, fixees par machine 1 seule pendant le run (piece de
    reception) : A-2 comptee indeterminee si une cellule n'est pas qualifiee et qu'aucun temoin
    juge n'echoue ; un run incomplet compte dans la case "instrument" de A-4 et A-5 ; A-7 "ni l'un
    ni l'autre" au reste des probabilites. Aucune n'a joue.
  Reserves de machine 2 a sa certification, sans correction : le script de predictions de machine
    1 ne refait la table gelee "au canon" que sur la plateforme de machine 1 (sur BOCAL4 : canon
    22b5d62869889371, a 1.7e-8 au plus) ; son test par mutations attrape 18 fautes greffees sur
    20, les deux manquees etant des egalites de bord (strict contre large).
  Ce que machine 2 dit ne pas avoir fait : verifier que deux executions de l'etage B rendent les
    memes octets (par regle il n'y a qu'un run) ; relire la sonde ligne a ligne apres le run.
  RETOUCHES DE LA VERSION 2. La version 1 de cet acte (464ba00a6905e3a5, lot 29058152bbba7a7a) a
    ete relevee par machine 2 (lot e1dfb7ba7b18196e, 15 pieces authentifiees) : 28 controles, 28
    tenus ; contre-epreuve de son releve : 46 corruptions de l'acte sur 46 mordues. Elle en
    contresigne le contenu SANS CONDITION et propose cinq precisions, qui ne sont pas des
    conditions. Toutes sont retenues : P-1 (nn.4 et nn.10 : "a moteur commun", et la routine qui
    assemble la 2D) ; P-2 (nn.2 : "aux durees pres") ; P-3 (nn.4 : ce que comptent les 1576
    champs) ; P-4 (nn.6 : le reste de la superposition est sous l'etendue de la chaine) ; P-5
    (nn.7 : la phrase sur les annonces, celle de machine 2, avec une phrase de la plume sur V1).
    Machine 2 dit que la limite du moteur commun corrige sa propre note de resultat. S'y ajoutent,
    et rien d'autre : ce paragraphe, la mention de version en tete, nn.11, trois lignes de nn.12
    et la ligne de fin. Aucun nombre juge, aucun tableau n'a change.

nn.10 LIMITES
  Celles du gel, section 13, restent (L-1 a L-9) : l'objet juge est UNE chaine sous UN absorbeur
    de chaine ; la reference est une largeur sous absorbeur, qualifiee par sa stabilite sous
    quatre absorbeurs ; quatre w2, un seul par creneau ; un seul modele, un seul etat ; la
    tolerance ne sort pas d'une theorie de l'erreur.
  Sous 1.33e-12 (19 cellules sur 28) aucune seconde mesure 2D n'existe : une erreur commune aux
    quatre absorbeurs echapperait au lecteur. Ce qui appuie ces lectures est indirect : le jumeau,
    et le fait que la chaine, calculee avant et par deux machines, les retrouve.
  La 2D des cellules a ete calculee sur une seule machine (BOCAL4), une seule fois. Machine 1 n'en
    a rejoue aucune.
  Le chemin du fantome de la sonde a tourne pour la premiere fois dans ce run (nn.4).
  La chaine et la 2D partagent le moteur (82a0be882568fe0c). Les sauts de la chaine, et le
    hamiltonien de la boite, assemble par la routine "assembler" du bloc du lecteur, lu dans sa
    sonde deposee (d5cc48f48e37af99) et execute tel quel, appellent la meme fonction X_saut_reel ;
    les predictions des deux machines aussi. L'accord eprouve la reduction a une dimension et les
    absorbeurs, pas le moteur.
  L'accord a quelques dix-milliemes n'est pas resolu : il est sous l'etendue de la chaine partout
    (nn.5).
  Le feu vert de l'operateur est rapporte par machine 2 ; machine 1 ne l'a pas vu. L'ouverture, la
    graine et l'anteriorite de la piece de reception sont des declarations de machine 1.

nn.11 SUITE
  La version 1 est contresignee ; machine 2 peut rejouer son releve sur cette version 2. Depot : a
  la decision de l'operateur, numero pris au depot. Ce run s'appuie sur des pieces qui ne sont pas
  au registre : les deux parties du gel et leurs lots (table gelee, sonde, feuille, pilote, bloc
  de l'absorbeur adapte), le rectificatif, les notes sur la loi d'echelle et sur le vide. Ce gel
  ne se rejoue pas.

nn.12 PIECES (convention B)
    b57c9ccdd3946261 gel, premiere partie (lot 879ea2e51c7d7f4f)
    eebd979f18d8db48 gel, seconde partie (lot b1919dc9468dc437)
    b71206e5daf6c741 table gelee des 28 cellules
    49a40d9098b55361 bloc de l'absorbeur adapte
    336913aecc732cdf rectificatif C-1, C-2 (lot 71ec801a5f86e068)
    464ba00a6905e3a5 version 1 de cet acte (lot 29058152bbba7a7a)
    d4f95772710d545c lot de machine 2 : certification de la premiere partie
    5921fcd984d6de5b lot de machine 2 : son tirage
    f989369a3ac22f98 lot de machine 2 : certification de la seconde partie
    9a14bf95fa8c6d20 lot de machine 2 : resultat du run
    e1dfb7ba7b18196e lot de machine 2 : contreseing de la version 1
    2913b7aa82184ef1 sa note de certification de la seconde partie
    bcaf377489a0e1ff sa note de resultat
    700a39a9a7223fd0 sa note de contreseing
    a38b1550f8f5e3cf pilote joue (celui du gel)
    5a73b5a492d5d4a2 lanceur de machine 2
    2d8e6692d862fa37 journal du pilote du run
    cc54f4bc4e175143 verdict de l'instrument du lecteur
    8472dba8919a9b6e verdict de la feuille du run
    47bb39ef530a967c verdict rejoue par machine 1
    c95df19ff2f16ff7 verdict de la seconde feuille de machine 2
    c815876f0ff7d66b piece de reception de machine 1 (ecrite pendant le run)
    4adc285659120eb8 son essai
    957ce0b198a5f31b reception : comparaison des verdicts et annonces
    f1d08f97d5301157 lecture du resultat pour l'acte (script)
    af0b3d8cdd0b4fa5 lecture du resultat pour l'acte (nombres)

-- FIN journal_delta_nn_largeur_vide_v2 --
