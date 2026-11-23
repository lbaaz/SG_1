GEL "SOMMET" -- SECONDE PARTIE : L'INSTRUMENT, L'ENONCE, LES TOLERANCES
PRE-ENREGISTREMENT v1 -- machine 1, 2026-11-22.
A CERTIFIER PAR MACHINE 2 AVANT TOUTE LECTURE 2D A L'UNE DES CELLULES.

0. STATUT
  Cette piece complete la premiere partie (1e5039cade55d13f, lot 3ba4618d7976c6ea), que machine 2 a
  certifiee telle quelle, sans refus (lot 21e9bddfe5db83b2) : sa table des 560 cellules candidates,
  ecrite du texte, est celle de machine 1, et la table commune est ce meme fichier
  (77ce2a6c7e867011). Cette piece fixe les cellules tirees, l'instrument du run, l'enonce juge, ses
  tolerances, ce que chaque issue engage, et les annonces de la plume. Rien n'est joue.
  Graine. L'operateur a ecrit a machine 1 "graine 114565" (22/11/2026, 23 h 21), apres lui avoir
  remis la certification de machine 2 (22 h 55) et apres que machine 1 l'a authentifiee et a recoupe
  la table commune par son code. Machine 1 n'avait calcule aucun tirage sur une graine faite de
  chiffres avant de la recevoir ; elle avait rappele a l'operateur que la graine lui revenait ; elle
  n'en a propose ni commente aucune. Elle ne sait pas si machine 2 l'a recue : machine 2 le dit a la
  certification.
  Tirage. Par le script de machine 1 (816ac4d298e82f16), sur la table commune : chaque creneau rend
  ses deux w2 aux rangs 0 et 1, aucun rang n'est saute ; huit w2, cinquante-six cellules. Machine 2
  dit son tirage a la certification ; si ses cellules ou leurs trois nombres ecrits different, PAS
  DE GEL (premiere partie, section 6).
  E19. Aucune des deux machines ne fait de calcul 2D, du systeme a fantome ou du jumeau, a l'un des
  huit w2 tires, avant la certification croisee de cette piece et le feu vert ecrit de l'operateur.
  Tout ce que cette piece calcule aux cellules est une chaine a une dimension, faite avant la
  graine. Machine 1 n'a fait AUCUN calcul 2D pour cette piece : sa feuille a ete essayee sur des
  dossiers synthetiques et sur les sorties que machine 2 a deja produites aux neuf points sacrifies,
  lues comme des donnees ; son pilote n'a joue que des scripts factices (sections 4.3 a 4.5).

1. QUESTION ET PERIMETRE
  Le gel "largeur du vide" (delta 102) a montre que la chaine a une dimension rend la largeur de
  l'etat que porte le site (0, 0) aux ailes, a trois barreaux de barriere et plus. Ce gel demande si
  elle la rend encore au SOMMET, de deux barreaux jusqu'a la fenetre sans barriere, la ou le saut au
  pied de l'echelle vaut jusqu'au desaccord lui-meme, a des cellules que personne n'a choisies.
  Perimetre : huit w2 (1.99989, 1.99993, 2.00008, 2.00011, 1.99968, 1.99956, 2.00039, 2.00048) et
  sept kappa (0.0363, 0.0530, 0.0800, 0.1300, 0.2000, 0.4000, 1.0000). L'objet juge est la chaine
  d'ordre 3 des blocs deposes sous l'absorbeur adapte (bloc 49a40d9098b55361), telle quelle : son
  plateau G3* sur dix-huit variantes, calcule avant la graine. La reference est la largeur de
  plateau sous l'absorbeur A, lue par le lecteur creux du depot avec le eta0 et le r_c ecrits de la
  cellule.
  Ce que le gel SEPARE et ne separe pas. Aux cinquante-six cellules l'ordre 3 differe du premier
  ordre de 0.00034 au plus en logarithme, et de l'ordre 2 de 0.00005 au plus : sous une tolerance de
  0.01, l'enonce n'oppose pas les ordres. Il eprouve ceci : "le mecanisme de l'echelle et la chaine
  rendent la largeur du vide a 0.01 pres, de kappa = 0.0363 a kappa = 1". La loi d'echelle et le
  signe de delta ne sont pas juges : ils sont consignes (section 6).

2. SOURCES (convention B)
    82a0be882568fe0c scripts/m17_chaine_v17.py (registre 055be58), le moteur
    d5cc48f48e37af99 scripts/sonde_lecteur_gel_loi_machine1_v1.py (registre) : la sonde du lecteur,
                     jouee telle quelle a l'etage A, et dont le bloc LECTEUR CREUX est execute par
                     le pilote de lecture
    83701094e6a2b965 scripts/lecture_lecteur_gel_loi_machine1_v1.py (registre) : la feuille du
                     lecteur, jouee telle quelle a l'etage A, et dont juger_etat est appele par la
                     feuille de ce gel
    10887c60d5f55bcf journal/sonde_ordre2.json (registre), le depot du delta 98 : les ancres
    69b3bab3bb8480b7 journal/tp_retenus_machine2_v1.json (registre) : couplages du temoin positif du
                     depot
    4d51dd58ef456fe9 journal/tp_reference_machine2_v1.json (registre) : sa reference
    6600fb8418c79930 journal/reference_ancres_ter_machine1_v1.json (registre) : reference des ancres
    35fa7b73f2b7f8eb journal/table_points_gel_loi_ordre3_v1.json (registre) : la table que la sonde
                     deposee exige a l'etage A
    a38b1550f8f5e3cf scripts/pilote_gel_vide_machine1_v1.py (registre) : le pilote dont celui de ce
                     lot derive
    ac39a24def6c7420 scripts/feuille_vide_machine1_v1.py (registre) : la feuille dont celle de ce
                     lot derive
    eebd979f18d8db48 gels/gel_largeur_vide_partie2_instrument_enonces_pre_enregistrement_v1.md
                     (registre) : la piece dont celle-ci reprend la forme
    1e5039cade55d13f gel_sommet_partie1_regle_tirage_pre_enregistrement_v1.md (lot
                     3ba4618d7976c6ea) : la premiere partie
    816ac4d298e82f16 tirage_sommet_machine1_v1.py (meme lot) : le tirage
    882f55d07d03dfff eligibilite_sommet_v1.json (meme lot) : la table complete de machine 1, d'ou
                     viennent les predictions
    77ce2a6c7e867011 la table commune (lots 3ba4618d7976c6ea et 21e9bddfe5db83b2)
    47a84eae6052f006 lecteur_2D_pilote_machine2_v1.py (lots c58c2b3f533c516b et 295b2b1549b076c2 de
                     machine 2) : le pilote de lecture qui a lu Q et Q2 ; ECRIT PAR MACHINE 2, joue
                     ici tel quel
  Les lots de machine 1 et de machine 2 du 22/11 ne sont pas au registre (055be58) : les deux
  machines les detiennent. Le pilote de lecture de machine 2 n'est pas dans ce lot : machine 1 ne
  l'a jamais execute, elle l'a lu.

3. LES CELLULES
  Table gelee : table_cellules_gel_sommet_v1.json, canon 4238e2b262119f83. Elle porte la graine, le
  journal du tirage, les 56 cellules, leurs trois nombres ecrits, leurs predictions et leur
  tolerance, et les neuf temoins positifs avec leur plateau de reference. La feuille et le pilote
  portent son canon en dur. Par cellule : w2, delta = w2 - 2, kappa, profondeur m de la barriere,
  couplage ecrit g, echelle ecrite eta0, rayon r_c, plateau predit G3* et etendue de la chaine sous
  ses dix-huit variantes. La tolerance est T = 0.01 a toutes ; la plus grande boite du lecteur est
  r_c + 100.
    cellule  w2              delta      kappa   m  g            eta0         r_c  G3*        etendue
    MPa1     199989/100000   -0.00011  0.0363  2  3.91071e-05  1.52405e-04  22   7.352e-10  0.0034
    MPa2     199989/100000   -0.00011  0.0530  1  5.70985e-05  2.22519e-04  20   1.975e-08  0.0021
    MPa3     199989/100000   -0.00011  0.0800  0  8.61865e-05  3.35878e-04  18   2.636e-07  0.0018
    MPa4     199989/100000   -0.00011  0.1300  0  1.40053e-04  5.45801e-04  18   1.974e-06  0.0024
    MPa5     199989/100000   -0.00011  0.2000  0  2.15466e-04  8.39694e-04  18   6.135e-06  0.0003
    MPa6     199989/100000   -0.00011  0.4000  0  4.30932e-04  1.67939e-03  18   1.958e-05  0.0015
    MPa7     199989/100000   -0.00011  1.0000  0  1.07733e-03  4.19847e-03  18   5.691e-05  0.0030
    MPb1     199993/100000   -0.00007  0.0363  2  2.48901e-05  9.69848e-05  22   4.679e-10  0.0034
    MPb2     199993/100000   -0.00007  0.0530  1  3.63409e-05  1.41603e-04  20   1.257e-08  0.0021
    MPb3     199993/100000   -0.00007  0.0800  0  5.48542e-05  2.13741e-04  18   1.677e-07  0.0017
    MPb4     199993/100000   -0.00007  0.1300  0  8.91380e-05  3.47328e-04  18   1.256e-06  0.0022
    MPb5     199993/100000   -0.00007  0.2000  0  1.37135e-04  5.34350e-04  18   3.904e-06  0.0003
    MPb6     199993/100000   -0.00007  0.4000  0  2.74271e-04  1.06870e-03  18   1.246e-05  0.0019
    MPb7     199993/100000   -0.00007  1.0000  0  6.85677e-04  2.67176e-03  18   3.622e-05  0.0032
    PPa1     25001/12500     +0.00008  0.0363  2  2.84618e-05  1.10840e-04  22   5.347e-10  0.0033
    PPa2     25001/12500     +0.00008  0.0530  1  4.15558e-05  1.61832e-04  20   1.436e-08  0.0024
    PPa3     25001/12500     +0.00008  0.0800  0  6.27258e-05  2.44275e-04  18   1.917e-07  0.0014
    PPa4     25001/12500     +0.00008  0.1300  0  1.01929e-04  3.96945e-04  18   1.435e-06  0.0018
    PPa5     25001/12500     +0.00008  0.2000  0  1.56814e-04  6.10686e-04  18   4.462e-06  0.0017
    PPa6     25001/12500     +0.00008  0.4000  0  3.13629e-04  1.22137e-03  18   1.424e-05  0.0033
    PPa7     25001/12500     +0.00008  1.0000  0  7.84072e-04  3.05344e-03  18   4.139e-05  0.0024
    PPb1     200011/100000   +0.00011  0.0363  2  3.91394e-05  1.52405e-04  22   7.352e-10  0.0033
    PPb2     200011/100000   +0.00011  0.0530  1  5.71457e-05  2.22519e-04  20   1.975e-08  0.0024
    PPb3     200011/100000   +0.00011  0.0800  0  8.62576e-05  3.35878e-04  18   2.635e-07  0.0013
    PPb4     200011/100000   +0.00011  0.1300  0  1.40169e-04  5.45803e-04  18   1.974e-06  0.0017
    PPb5     200011/100000   +0.00011  0.2000  0  2.15644e-04  8.39695e-04  18   6.135e-06  0.0019
    PPb6     200011/100000   +0.00011  0.4000  0  4.31288e-04  1.67939e-03  18   1.957e-05  0.0032
    PPb7     200011/100000   +0.00011  1.0000  0  1.07822e-03  4.19847e-03  18   5.691e-05  0.0031
    MGa1     6249/3125       -0.00032  0.0363  2  1.13677e-04  4.43360e-04  22   2.139e-09  0.0034
    MGa2     6249/3125       -0.00032  0.0530  1  1.65974e-04  6.47328e-04  20   5.747e-08  0.0016
    MGa3     6249/3125       -0.00032  0.0800  0  2.50527e-04  9.77100e-04  18   7.668e-07  0.0023
    MGa4     6249/3125       -0.00032  0.1300  0  4.07106e-04  1.58779e-03  18   5.742e-06  0.0030
    MGa5     6249/3125       -0.00032  0.2000  0  6.26317e-04  2.44275e-03  18   1.785e-05  0.0021
    MGa6     6249/3125       -0.00032  0.4000  0  1.25263e-03  4.88548e-03  18   5.695e-05  0.0026
    MGa7     6249/3125       -0.00032  1.0000  0  3.13159e-03  1.22138e-02  18   1.656e-04  0.0023
    MGb1     49989/25000     -0.00044  0.0363  2  1.56235e-04  6.09618e-04  22   2.941e-09  0.0035
    MGb2     49989/25000     -0.00044  0.0530  1  2.28112e-04  8.90078e-04  20   7.902e-08  0.0013
    MGb3     49989/25000     -0.00044  0.0800  0  3.44319e-04  1.34351e-03  18   1.054e-06  0.0026
    MGb4     49989/25000     -0.00044  0.1300  0  5.59519e-04  2.18321e-03  18   7.896e-06  0.0031
    MGb5     49989/25000     -0.00044  0.2000  0  8.60799e-04  3.35878e-03  18   2.454e-05  0.0027
    MGb6     49989/25000     -0.00044  0.4000  0  1.72160e-03  6.71757e-03  18   7.831e-05  0.0029
    MGb7     49989/25000     -0.00044  1.0000  0  4.30399e-03  1.67939e-02  18   2.277e-04  0.0024
    PGa1     200039/100000   +0.00039  0.0363  2  1.38913e-04  5.40345e-04  22   2.607e-09  0.0031
    PGa2     200039/100000   +0.00039  0.0530  1  2.02820e-04  7.88931e-04  20   7.002e-08  0.0028
    PGa3     200039/100000   +0.00039  0.0800  0  3.06144e-04  1.19084e-03  18   9.342e-07  0.0012
    PGa4     200039/100000   +0.00039  0.1300  0  4.97483e-04  1.93511e-03  18   6.997e-06  0.0010
    PGa5     200039/100000   +0.00039  0.2000  0  7.65359e-04  2.97710e-03  18   2.175e-05  0.0031
    PGa6     200039/100000   +0.00039  0.4000  0  1.53072e-03  5.95421e-03  18   6.939e-05  0.0024
    PGa7     200039/100000   +0.00039  1.0000  0  3.82680e-03  1.48855e-02  18   2.017e-04  0.0021
    PGb1     12503/6250      +0.00048  0.0363  2  1.71027e-04  6.65038e-04  22   3.208e-09  0.0030
    PGb2     12503/6250      +0.00048  0.0530  1  2.49709e-04  9.70992e-04  20   8.618e-08  0.0028
    PGb3     12503/6250      +0.00048  0.0800  0  3.76919e-04  1.46565e-03  18   1.150e-06  0.0014
    PGb4     12503/6250      +0.00048  0.1300  0  6.12494e-04  2.38168e-03  18   8.612e-06  0.0012
    PGb5     12503/6250      +0.00048  0.2000  0  9.42298e-04  3.66412e-03  18   2.677e-05  0.0030
    PGb6     12503/6250      +0.00048  0.4000  0  1.88460e-03  7.32826e-03  18   8.540e-05  0.0026
    PGb7     12503/6250      +0.00048  1.0000  0  4.71149e-03  1.83206e-02  18   2.483e-04  0.0030
  Aux 56 cellules la barriere du moteur finit a la profondeur cible, et G3* et l'etendue sont ceux
  de la table de machine 1 calculee avant la graine, que machine 2 a retrouves par sa methode (ecart
  de 2.3e-11 au plus sur le logarithme du plateau, lot 21e9bddfe5db83b2). Couplages de 2.48901e-05 a
  4.71149e-03 ; plateaux predits de 4.679e-10 a 2.483e-04 ; etendue de 0.0003 a 0.0035.
  Le tirage a sorti une paire de w2 MIROIRS, 1.99989 et 2.00011 (meme |delta|, signes opposes) :
  sept paires de cellules a kappa egal y lisent le signe de delta seul. C'est le hasard de la
  graine ; rien n'en est juge.
  Les neuf TEMOINS POSITIFS DU SOMMET : les points sacrifies de Q et de Q2, a w2 = 2, 20001/10000 et
  19999/10000, qui ne sont pas candidats. Leur reference est le plateau que le lecteur y a rendu,
  relu par juger_etat de la feuille deposee dans les sorties de machine 2 :
    temoin  w2           m  g        eta0         r_c  plateau de reference
    Qa      2            0  2.5e-4   9.73875e-04  18   1.36078e-05
    Qc      2            0  1e-3     3.89550e-03  18   5.44311e-05
    Qd      2            0  2e-3     7.79100e-03  18   1.08861e-04
    Qe      20001/10000  0  3e-4     1.16821e-03  18   1.20926e-05
    Qf      20001/10000  0  1.5e-4   5.84106e-04  18   2.91446e-06
    Q2a     20001/10000  1  6e-5     2.33642e-04  20   4.94717e-08
    Q2b     20001/10000  2  4e-5     1.55762e-04  22   2.05518e-09
    Q2c     19999/10000  0  3e-4     1.16909e-03  18   1.21073e-05
    Q2d     19999/10000  0  1.5e-4   5.84544e-04  18   2.92063e-06

4. L'INSTRUMENT : UN RUN, QUATRE ETAGES ET UNE GARDE
  4.1 Les pieces (convention B)
    4238e2b262119f83 table_cellules_gel_sommet_v1.json : la table gelee ; ecrite par
                     predictions_sommet_machine1_v1.py (b5d424a72d088ec1)
    ed4c3886b17fcdc3 pilote_gel_sommet_machine1_v1.py : NOUVEAU ; il enchaine et tient le journal ;
                     derive du pilote depose du gel "largeur du vide"
    ac934e0caaa59c08 feuille_gel_sommet_machine1_v1.py : NOUVELLE ; elle appelle juger_etat de la
                     feuille deposee, garde et juge ; derivee de la feuille deposee du gel "largeur
                     du vide"
    7b68e47a2a735e3b jobs_gel_sommet_v1.txt : les 112 lectures des cellules, au format du pilote de
                     lecture de machine 2
    e1b636ad123bfc83 jobs_temoins_sommet_v1.txt : les 18 lectures des temoins positifs, meme format
    47a84eae6052f006 lecteur_2D_pilote_machine2_v1.py : le pilote de lecture, de machine 2, hors de
                     ce lot (section 2)
    Aucune piece deposee n'est editee : la sonde et la feuille du lecteur sont jouees telles quelles
    a l'etage A, et leurs routines sont executees depuis leurs fichiers, au canon controle, aux
    autres etages. Les deux fichiers de travail ne commandent rien : le pilote tire ses appels de la
    table ; le banc verifie qu'ils sont ces lignes (4.5).
  4.2 Le deroulement du run (le pilote)
    Etage A. L'instrument du lecteur, tel qu'aux gels "ordre 3" et "largeur du vide" : la sonde
    deposee en modes etage0, ancres et etage1 (les deux ancres du depot, le temoin positif, le
    temoin negatif des ancres), puis la feuille deposee, etape "instrument". Si elle ne rend pas
    TIENT, le run s'arrete : rien d'autre n'est lu.
    Etage A'. Les neuf temoins positifs du sommet, par le pilote de lecture de machine 2 : le jumeau
    sans fantome (signe +1) puis le fantome (signe -1), au site (0, 0), depuis l'energie 0, sous les
    quatre absorbeurs du depot (A : F2, 80 couches ; B : F2, 100 ; C : F1, 100 ; D : F2, bord r_c +
    10, 80), a douze barreaux (k = -3 a 8, eta_k = eta0 2^(-k)), avec le eta0 et le r_c de la table.
    Garde. La feuille de ce gel, etape --temoins : instrument et temoins positifs (section 5). Si
    elle ne rend pas TIENT, le run s'arrete : AUCUNE cellule n'est lue. Elle refuse un dossier ou
    une cellule a deja un fichier.
    Etage B. Les 56 cellules, par le meme pilote de lecture, de la meme facon : 112 lectures.
    Etage C. La feuille de ce gel : sections 5 et 6.
  4.3 Le banc de la feuille
    Le banc fabrique des dossiers de run SYNTHETIQUES pour la table gelee (des plateaux poses a la
    main autour de la prediction : ils ne disent rien des cellules), change une chose a la fois,
    avec l'effet attendu ecrit avant : 30 cas, 30 tenus au premier passage. Ils couvrent : une
    cellule qui tombe, d'un cote et de l'autre ; deux ; la cellule non jugeable ; trop de non
    jugeables ; un w2 sans quatre cellules tenues ; le desaccord d'un absorbeur ; l'absence de
    plateau ; un absorbeur sans cinq barreaux lisibles ; une lecture non suivie sans consequence ;
    le jumeau trop large ; le jumeau non suivi ; l'instrument qui ne tient pas ou qui manque ; un
    temoin positif hors de sa reference, non qualifie, ou juste sous le seuil ; le fichier absent ;
    le canon du pilote de lecture ; le couplage ; eta0 ; la geometrie ; une autre table ; la bande
    qui depasse la tolerance ; la portee qui perd un kappa ; l'etape de garde dans ses quatre
    issues.
  4.4 La feuille sur des sorties reelles, sans aucune mesure nouvelle
    L'etape de garde a ete jouee sur les dix-huit fichiers que machine 2 a produits a Q et a Q2, lus
    comme des donnees : les 9 temoins positifs y sont QUALIFIES, leur jumeau tient, et ils rendent
    leur reference a 0 pres (ce sont les memes fichiers : cela eprouve la lecture de la feuille, pas
    le lecteur). L'instrument de l'etage A y manque, et la garde rend "L'INSTRUMENT NE TIENT PAS",
    comme elle le doit.
  4.5 Le banc du pilote
    Le pilote n'a JAMAIS joue une lecture reelle chez machine 1 : les calculs 2D sont chez machine
    2. Son banc le joue sur des scripts FACTICES qui notent leurs arguments ; le pilote eprouve est
    une copie dont seules les lignes des canons en dur sont remplacees. 12 cas, 12 tenus : le run
    entier dans l'ordre des etages ; les 18 puis les 112 appels de lecture egaux, argument pour
    argument, aux lignes des deux fichiers de travail ; l'arret si l'instrument ne tient pas ;
    l'arret si la garde ne tient pas, sans une cellule lue ; le pre-vol ; le refus d'un dossier deja
    la ; l'arret sur un code de sortie non nul ; l'arret du pilote non modifie devant une piece qui
    n'est pas au canon. Ce que ce banc ne dit pas : rien de ce que font les vrais scripts.
  4.6 Le pre-vol, chez machine 2
    Avec --prevol le pilote joue l'etage A, l'etage A' et la garde, puis s'arrete : AUCUNE cellule
    n'est lue. Les neuf points relus sont des points sacrifies, deja lus sur le mot de l'operateur.
    Ce sera la premiere execution reelle du pilote. Machine 2 demande a l'operateur ce qu'elle
    estime devoir lui demander.

5. POINT LU, BANDE, JUGEMENT (ce que fait la feuille)
  LECTEUR. La feuille appelle juger_etat de la feuille deposee sur les quatre trajectoires du
  fantome. Il exige un plateau sous CHACUN des quatre absorbeurs (cinq barreaux lisibles
  consecutifs, plus grande valeur <= 1.05 fois la plus petite ; lisible = suivie, finie, strictement
  positive), et les plateaux sous B, C et D a 0.05 pres du plateau sous A, en logarithme. Statut :
  QUALIFIE ; NON QUALIFIE si un absorbeur a une fenetre de cinq barreaux lisibles mais pas de
  plateau, ou si un accord manque ; NON LISIBLE si, sans autre echec, un absorbeur n'a pas cinq
  barreaux lisibles consecutifs. Une lecture non suivie hors de la fenetre retenue ne change rien.
  Gamma_pl est le plateau sous A.
  ETALEMENT DU LECTEUR, s : le plus grand de ln(1 + etalement du plateau sous A) et des trois
  |ln(plateau X / plateau A)|, X = B, C, D.
  TEMOIN. Le jumeau sans fantome au meme point. Il TIENT si ses 48 lectures sont suivies et si sa
  plus grande largeur vaut au plus 1e-6 Gamma_pl.
  POINT LU : QUALIFIE et temoin tenu. Sinon NON LU, avec son motif. Une cellule dont B, C ou D n'a
  pas de plateau, ou s'ecarte de A de plus de 0.05, est donc NON LUE : elle n'est pas "lue sans
  accord".
  TEMOIN POSITIF. Un point sacrifie TIENT s'il est lu et si |ln(Gamma_pl / plateau de reference)| <=
  0.001. Les temoins positifs TIENNENT si les neuf tiennent.
  JUGEMENT d'une cellule lue. ln q = ln(G3* / Gamma_pl). BANDE b = etendue de la chaine a la cellule
  (table) + s. La cellule TIENT si |ln q| <= T - b ; elle TOMBE si |ln q| > T + b ; elle est NON
  JUGEABLE sinon. La tolerance pour tenir est donc plus serree que T ; une cellule dont la bande
  atteint T ne peut pas tenir : elle tombe ou n'est pas jugeable.

6. L'ENONCE ET SES ISSUES (la cellule est l'unite)
  S1, cinquante-six cellules, huit w2, T = 0.01. TOMBE si deux cellules ou plus tombent ; sinon NON
  CONCLUANT si moins de 42 cellules sont jugees (tenues ou tombees), ou si un w2 a moins de 4
  cellules tenues sur sept ; sinon TENU SAUF UNE CELLULE si une tombe ; sinon TENU. C'est l'enonce
  V1 du gel "largeur du vide", porte de seize cellules a cinquante-six (trois quarts jugees) et de
  quatre creneaux a huit w2 (plus de la moitie tenues).
  PORTEE. La feuille donne les kappa ou 4 cellules au moins sur huit tiennent. Si S1 tient, l'acte
  n'ecrit sa phrase que pour ces kappa.
  Ce qui est consigne sans etre juge, par cellule lue : le signe de ln q et celui de delta ; ln q
  pour l'ordre 2 et pour le premier ordre ; ln(Gamma_pl / |delta|), et son etalement a kappa egal
  d'un w2 a l'autre (la loi d'echelle) ; aux sept paires de cellules miroirs, ln[Phi(delta < 0) /
  Phi(delta > 0)] lu et celui de la chaine ; la largeur rapportee au saut au pied de l'echelle ; les
  barreaux plats a 0.005 pres sous A. Aucun enonce ne porte sur le signe du residu, sur le signe de
  delta ni sur la loi d'echelle.

7. LES TOLERANCES, ET CE QUE LA PLUME A VU AVANT DE LES ECRIRE
  7.1 T = 0.01. Elle vient de la demolition de l'esquisse par machine 2 (0.02 valait 250 fois le
      pire ecart lu), prise par machine 1 avant Q2. Ce que la plume avait vu : aux neuf points
      sacrifies le lecteur est a 0.00034 au plus de G3* en logarithme, son etalement s vaut 0.0018
      au plus, et la chaine a une etendue de 0.0035 au plus aux 56 cellules. Si le lecteur s'etale
      aux cellules comme a ces points, la bande est de 0.0053 au plus et une cellule tient jusqu'a
      |ln q| = 0.0047 : 13 fois le pire ecart lu. Aucune largeur 2D n'existe a une cellule.
  7.2 La tolerance des temoins positifs, 0.001, est posee a la main. Le meme code sur la meme
      machine doit rendre le meme plateau a bien mieux ; 0.001 laisse passer un changement de
      bibliotheque, pas un changement d'instrument.
  7.3 Les seuils de S1 (42 cellules jugees sur 56, 4 tenues sur sept par w2) et de la portee (4 sur
      huit par kappa) sont poses ici, apres le tirage et avant toute lecture. Ils ne dependent
      d'aucune prediction.
  7.4 Ce que la plume sait du defaut de sa chaine. Aux deux points de barriere lus (Q2-a, Q2-b) le
      lecteur est a 0.00019 et 0.00034 AU-DESSUS de G3*. Refait a une dimension, variante par
      variante : cet ecart vient de la mediane de l'absorbeur adapte, pas des ordres de la chaine.
      Il est sous l'etendue. La tolerance vaut 29 fois le plus grand ; l'acte ne pourra pas ecrire
      que la chaine est exacte.
  7.5 Ce que le lecteur n'a jamais lu. Quatre cellules (MGa7, MGb7, PGa7, PGb7) ont un plateau
      predit au-dessus du plus grand plateau qualifie (1.08861e-04, Q-d), jusqu'a 2.28 fois, a des
      couplages de plus de 2e-03 ; quatre (MPa1, MPb1, PPa1, PPb1) sont sous le plus petit plateau
      qualifie au sommet (2.05518e-09, Q2-b), jusqu'a 0.228 fois. Aucune borne n'est posee : si le
      lecteur n'y qualifie pas, la cellule est non lue et se compte comme telle.

8. CE QUE CHAQUE ISSUE ENGAGE
  L'INSTRUMENT NE TIENT PAS (etage A), ou LES TEMOINS POSITIFS NE TIENNENT PAS (garde) : aucune
    cellule n'est lue, rien n'est juge ; l'acte le dit ; une suite demande un autre gel, ou les
    cellules, restees vierges, peuvent etre reprises telles quelles.
  S1 TENU. L'acte peut ecrire : "a cinquante-six cellules tirees au sort, en huit tirages, pour
    |delta| de 0.00007 a 0.00048 et kappa de 0.0363 a 1 [les kappa de la portee], la chaine d'ordre
    3 sous absorbeur adapte rend la largeur de l'etat porte par (0, 0) a 0.01 pres en logarithme,
    au-dela de sa propre etendue et de l'etalement du lecteur". Avec le delta 102, la loi d'echelle
    de la largeur du vide est alors eprouvee des ailes au sommet. Il NE peut PAS ecrire : que la
    chaine est exacte (7.4) ; que l'ordre 3 fait mieux que le premier ordre (section 1) ; quoi que
    ce soit de la duree de vie du systeme ferme ; quoi que ce soit de w2 = 2 exactement ni au-dela
    de kappa = 1 ; "cinquante-six cellules" sans dire "huit tirages", ni sans dire que ce que la
    graine a fait varier est le couplage, le signe et l'echelle du desaccord.
  S1 TENU SAUF UNE CELLULE. La meme phrase, la cellule nommee, avec son ln q, sa bande, son w2 et
    son kappa.
  S1 TOMBE. L'acte ecrit que la chaine ne rend pas la largeur du vide au sommet a cette tolerance,
    cellules nommees. Aucune autre chaine, aucun autre absorbeur de chaine, aucune autre tolerance,
    aucun autre eta0 n'est essaye sur ces cellules.
  S1 NON CONCLUANT. L'acte donne les comptes et dit lequel des deux a manque : le lecteur (cellules
    non lues) ou la resolution (cellules non jugeables). Ce n'est ni une refutation ni une
    confirmation. Pas de rejeu, pas de nouveau seuil.
  Dans tous les cas : la table par cellule est publiee (statut du lecteur, plateaux et ecarts des
    quatre absorbeurs, temoin, Gamma_pl, s, bande, ln q, jugement, et les grandeurs consignees), les
    cellules non lues avec leur motif, et les neuf temoins positifs.

9. GARDES (chaque journal dit ce qu'il ne joue pas)
  G-1 canons en dur : moteur, sonde et feuille deposees du lecteur, depot, couplages et references
      du temoin et des ancres, table deposee du gel "ordre 3", table gelee, pilote de lecture de
      machine 2, feuille ; un ecart arrete.
  G-2 le pilote de lecture lit le bloc du lecteur dans le fichier depose, au canon controle ; chaque
      fichier de lecture porte l'empreinte du texte du bloc (5b835ce079ce2cf4), que la feuille
      exige.
  G-3 forme de chaque fichier, controlee par la feuille avant tout jugement : canons, point egal a
      celui de la table (w2, m, couplage ecrit, r_c, eta0), absorbeurs et boites, quatre
      trajectoires de douze barreaux, signe, site, energie de depart. Un fichier de cellule manquant
      ou non conforme : RUN INCOMPLET, rien n'est juge.
  G-4 instrument du lecteur : etage 0, ancres, etage 1, par les pieces deposees, tolerances
      inchangees.
  G-5 temoin : le jumeau a la geometrie de chaque point.
  G-6 temoins positifs du sommet : ils disent que l'instrument, le jour du run, rend au sommet ce
      qu'il y a rendu a Q et a Q2. Ils ne disent pas qu'il y lit juste : c'est le meme code.
  G-7 la garde est jouee AVANT toute lecture de cellule, et refuse un dossier ou une cellule a deja
      un fichier ; le pre-vol s'arrete apres elle.
  G-8 une seule execution : le pilote exige un dossier neuf et joue chaque appel une fois ; un code
      de sortie non nul l'arrete.
  G-9 ce que l'accord des quatre absorbeurs eprouve : l'independance de la largeur a la boite et a
      la forme de l'absorbeur. Il n'eprouve PAS l'exactitude de la largeur : une erreur commune aux
      quatre lui echappe, et une erreur commune au lecteur et a la chaine echapperait au gel entier.

10. ANNONCES DE LA PLUME (ecrites apres le tirage ; aucune 2D a une cellule)
  Ce sont des jugements, pas des calculs. Probabilites :
  A-1 (0.95) l'instrument du lecteur tient (etage A).
  A-2 (0.97) les neuf temoins positifs tiennent.
  A-3 (0.95) le temoin tient aux 56 cellules.
  A-4 (0.70) le lecteur qualifie les 56 cellules ; (0.90) au moins cinquante.
  A-5 S1 : TENU 0.80 ; TENU SAUF UNE CELLULE 0.02 ; TOMBE 0.02 ; NON CONCLUANT 0.08 ; le reste
      (0.08) est l'instrument ou les temoins positifs.
  A-6 (0.75) aux cellules lues, le plus grand |ln q| est sous 0.001.
  A-7 (0.70) aux seize cellules de barriere (kappa = 0.0363 et 0.0530), ln q est negatif, le lecteur
      au-dessus de la chaine comme a Q2-a et Q2-b, a douze cellules au moins.
  A-8 (0.65) aux sept paires miroirs, le rapport lu est a 0.0001 pres de celui de la chaine a cinq
      paires au moins. La chaine donne, de kappa = 0.0363 a 1 : -0.00001 ; +0.00006 ; +0.00014 ;
      +0.00005 ; +0.00008 ; +0.00005 ; +0.00008.
  A-9 (0.75) a chaque kappa, l'etalement de ln(Gamma_pl / |delta|) sur les w2 lus est sous 0.001 ;
      la chaine donne de 0.00004 a 0.00048.
  La plume annonce donc que S1 tient a quatre chances sur cinq. Ce qu'elle craint n'est pas un
  desaccord : c'est une cellule non lue au bord de ce que le lecteur a deja qualifie, ou un
  instrument qui ne se rejoue pas. Elle le gele ainsi.

11. DEROULEMENT, E19, ET CE QUI EST PERMIS
  ORDRE. (1) Machine 2 dit son tirage et certifie cette piece, la table, la feuille et son banc, le
  pilote et son banc ; un seul tour de correction. (2) Feu vert ecrit de l'operateur. (3) Machine 2
  joue le pilote UNE fois, dans un dossier neuf. (4) Lot de resultat : les fichiers de l'etage A,
  les 130 fichiers de lecture, la garde, le verdict, les journaux, le journal du pilote. (5) Machine
  1 authentifie et rejoue la feuille. (6) Acte.
  PRE-VOL. Avant le feu vert, machine 2 peut jouer le pilote avec --prevol : section 4.6. Son pilote
  peut deriver du mien s'il le faut, et elle le dit ; --drapeau -P et un fil BLAS par appel y sont
  deja.
  UNE SEULE EXECUTION. Un pilote arrete par une panne se relance ENTIER dans un dossier neuf, et
  l'acte le dit ; aucun appel n'est rejoue apres lecture de sa sortie.
  DEUX MACHINES. Le verdict est celui de la feuille jouee par machine 2 dans le run. Machine 1 la
  rejoue sur les fichiers du lot : la feuille ne calcule aucune chaine, les predictions sont dans la
  table ; les deux verdicts doivent etre les memes. S'ils different, l'acte donne les deux et
  retient la lecture la MOINS favorable a l'enonce.
  E19. Aucune des deux machines ne lit une cellule avant le feu vert ; machine 1 n'y lit rien en 2D,
  ni avant ni apres : elle relit le lot de resultat. Ce gel ne se rejoue pas sous d'autres seuils,
  d'autres gardes, une autre chaine ou d'autres cellules apres lecture.

12. COUTS (a mesurer au pre-vol de machine 2, pas a promettre)
  Etage A : 1365 s de calcul en trois appels sur le conteneur de machine 1 au gel "largeur du
  vide" ; BOCAL4 l'a joue aux deltas 100 et 102. Etages A' et B : 130 lectures dans des boites de
  122 au plus ; d'apres machine 2, les dix lectures de Q ont pris 2 min 35 s et les huit de Q2 2 min
  28 s sur seize coeurs logiques. Etage C : quelques secondes.

13. LIMITES DECLAREES
  L-1 S1 ne separe pas l'ordre 3 des ordres inferieurs (section 1).
  L-2 Huit tirages, pas cinquante-six epreuves : a kappa egal la chaine ne varie que de 0.00048 au
      plus d'un w2 tire a l'autre. Ce que la graine fait varier est le couplage, le signe et
      l'echelle du desaccord (reserve de machine 2).
  L-3 Aucun des sept kappa n'a ete lu en 2D avant le run ; ils sont encadres par les neuf points
      sacrifies et, pour 0.0363, par les cellules de trois barreaux du delta 102.
  L-4 La regle de eta0 est une convention dans une zone que Q et Q2 ont trouvee plate ; le gel ne
      l'eprouve pas : il consigne, par cellule, les barreaux plats sous A.
  L-5 La chaine et la 2D partagent le moteur ; une erreur commune au lecteur et a la chaine ne se
      verrait pas (G-9).
  L-6 La largeur est celle d'un etat sous absorbeur, stable sous les variations jouees. Rien n'est
      dit de la duree de vie du systeme ferme.
  L-7 Le pilote de ce gel n'a jamais joue une lecture reelle avant le pre-vol de machine 2 (4.5).
  L-8 Les seuils de S1, la tolerance des temoins positifs et les probabilites de la section 10 sont
      de la plume de machine 1, posees a la main.
  L-9 Une definition du hamiltonien effectif : celle des blocs deposes (forme symetrique).

14. ECARTS DECLARES, ET REPONSES AUX REMARQUES DE MACHINE 2 (lot 21e9bddfe5db83b2)
  E-1 La premiere partie annoncait, pour temoins, "le jumeau a chaque cellule, les ancres et le
      temoin positif du depot". S'y AJOUTENT les neuf temoins positifs du sommet et la garde qui les
      lit avant toute cellule : l'etage A eprouve l'instrument aux ailes, sous la regle du depot ;
      rien n'y eprouvait la regle de eta0 du sommet le jour du run.
  E-2 Le pilote de lecture est celui de machine 2, celui qui a lu Q et Q2, et non une sonde neuve de
      machine 1 : c'est l'instrument qualifie, et machine 1 ne joue aucune 2D. La premiere partie
      disait "le lecteur creux du depot" : c'est son bloc qui est execute, depuis son fichier.
  E-3 La portee par kappa (section 6) n'etait pas annoncee. Elle ne change pas l'issue de S1 : elle
      borne la phrase de l'acte.
  E-4 Le pre-vol se joue sur la table du gel et s'arrete avant les cellules, au lieu d'une table de
      pre-vol a part : les temoins positifs sont dans la table gelee.
  R-1 (T et la bande) : la formule est en section 5 ; c'est celle du gel "largeur du vide". "Tient
      jusqu'a 0.005 environ" voulait dire T moins la bande : la tolerance pour tenir est plus serree
      que T.
  R-2 (ce qu'on exige de B, C et D) : section 5. Une cellule sans plateau sous B, C ou D, ou en
      desaccord avec A, est NON LUE. Une lecture non suivie hors de la fenetre retenue ne change
      rien : le banc le montre (cas b11).
  R-4 (le signe de delta) : consigne, non juge ; les sept paires miroirs le liront a kappa et
      |delta| egaux.
  R-5 (le cout) : section 12.
  Sa reserve sur les huit tirages est en L-2 et dans ce que l'acte ne peut pas ecrire (section 8).

15. CE QUE MACHINE 2 CERTIFIE
  (a) SON tirage sur la graine 114565, par son code : les memes 56 cellules, avec les memes trois
      nombres ecrits ; sinon PAS DE GEL ;
  (b) que les predictions de la table gelee sont celles de sa propre table aux 56 cellules ;
  (c) la feuille : qu'elle fait ce que disent les sections 5 et 6 ; son banc rejoue ;
  (d) le pilote : qu'il enchaine ce que dit la section 4.2 ; son banc rejoue ; son pre-vol si elle
      le joue ;
  (e) que le pilote de lecture au canon 47a84eae6052f006 est bien le sien, inchange depuis Q et Q2,
      et que les plateaux de reference des neuf temoins sont ceux de ses sorties ;
  (f) qu'elle accepte, ou refuse, ce qui est pose ici : les temoins positifs du sommet et leur
      tolerance, les seuils de S1, la portee, les ecarts E-1 a E-4.

16. PIECES DE CE LOT (convention B)
    4238e2b262119f83  table_cellules_gel_sommet_v1.json
    b5d424a72d088ec1  predictions_sommet_machine1_v1.py
    e34c47d1a31196d3  predictions_sommet_machine1_v1.log
    0b5f7500eb3b586d  tirage_sommet_graine_114565_machine1_v1.log
    7b68e47a2a735e3b  jobs_gel_sommet_v1.txt
    e1b636ad123bfc83  jobs_temoins_sommet_v1.txt
    ac934e0caaa59c08  feuille_gel_sommet_machine1_v1.py
    7e0a00c361042f9a  banc_feuille_gel_sommet_machine1_v1.py
    b575cdfe8ba2417f  banc_feuille_gel_sommet_machine1_v1.log
    4fe14e3bf1327d37  garde_sur_les_sorties_de_Q_et_Q2_machine1_v1.log
    ed4c3886b17fcdc3  pilote_gel_sommet_machine1_v1.py
    d3843810ea649454  banc_pilote_gel_sommet_machine1_v1.py
    0fe167b0c443c3cb  banc_pilote_gel_sommet_machine1_v1.log
    (ce script)       construction_gel_sommet_partie2_machine1_v1.py
  Le lot porte aussi le controle de cette piece contre ces sorties et son journal, ecrits apres
  elle : le manifeste du lot fait foi.
