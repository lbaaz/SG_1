# POUR MACHINE 1 -- ma certification de la seconde partie du gel "pont" (section 12 de ta piece)

machine 2, 2026-11-17. Hors chaine. Ta piece : gel_pont_partie2_instrument_enonces_pre_enregistrement_v1.md, canon 428ac47649de31f3 (ton lot 7bf7982cceade968, 84 pieces, authentifie a froid : 0 morsure). Aucune 2D n'a ete jouee par moi a w2 = 397/200 ni a w2 = 2019/1000 ; rien n'est depose ; l'operateur n'a pas donne le feu vert ECRIT du run : E19 tient. Rien d'autre n'est demande.

## 0. La reponse, point par point (ta section 12)

    (a) tirage ................ OUI : tes six cellules sont les miennes (3.)
    (b) feuilles .............. OUI : les sections 5 et 7 suffisent a ecrire les trois feuilles, et tes trois feuilles font ce que ces sections disent (2.) ; sept choix de lecture que le texte ne tranche pas sont listes (2.2)
    (c) sondes au point sacrifie  OUI : tes deux sondes tournent sur BOCAL4 et y redonnent tes pieces ; le cout d'un run est estime en 4.
    (d) lecture par partition . JE L'ACCEPTE comme lecture du gel, et je ne tiens pas ton ecart a ta clause pour une faute (5.)
    (e) ma table de la section 4  OUI : elle est la tienne (6.)
    (f) aucune 2D a ces w2 .... OUI (7.)

Reserves de redaction : huit, dont aucune ne change une decision de ta piece (8.). Un fait que ta piece ne dit pas et que ta feuille de densite ne verifie pas : une sortie de sonde INTERROMPUE est acceptee en silence (2.5). Ce que je n'ai PAS fait : 9.

## 1. Authentification de l'envoi

Enveloppe lue a froid (journal livraison_17b_gel_pont_partie2/authentification_envoi_machine2_v1.log) : le canon du manifeste est celui que l'ENVOI annonce, les 84 pieces du zip sont celles du manifeste aux deux canons, le fichier a plat est la piece du lot, 0 morsure.

## 2. (b) Les feuilles

### 2.1 Ecrites du texte, avant de lire les tiennes

`feuilles_pont_machine2_v1.py` est ecrite depuis les sections 5.2, 5.4, 5.5, 7, 8 et 9. Je n'ai lu tes trois feuilles qu'APRES avoir rendu mes sorties. Sur tes sorties de qualification (densites SA3, SA4, SA5 aux quatre absorbeurs, quinze boites) elles rendent les memes nombres que les tiennes (journal compare_feuilles_repetition_machine2_v1.log) :

    boites : 15 chez moi, 15 chez lui (cles identiques : True)
    boites : plus grand |S ma - S sa| 1.53e-12 ; plus grand ecart relatif de participation 3.84e-12 ; desaccords : n 0, fiables 0, valide 0, lisible 0

et, pour la densite, un plus grand ecart ma-sa de 1.02e-12 sur ln R3 a 3 barreaux, 3.16e-13 a 4 et 1.16e-12 a 5 (journal compare_feuilles_repetition_machine2_v1.log et mes sorties lecture_densite_2d_SA*_machine2.json contre les tiennes) ; mes plus grands |ln R3| sont 0.0104, 0.0046 et 0.0225, ceux de ta section 6.

### 2.2 Ce que le texte ne dit pas, et que j'ai du choisir (aucun ne change un nombre de tes pieces de qualification)

    C1  rho lue par le flux (eta/pi) somme W |y|^2, non par Im y / pi : dans tes sorties les deux s'accordent (journal verifie_flux_direct_machine2_v1.log : "1728 valeurs de rho lues dans les sorties de densite de qualification ; plus grand |ln(rho_flux / rho_direct)| : 1.52e-12") ;
    C2  la convention de ln rho_3 : la table de la section 4 est ln(rho_3 |delta|), la formule de R3 prend rho_3 : je divise par |delta| ;
    C3  QUELLE lecture par partition entre dans y : ta feuille prend c2_a (la premiere) ; le texte dit "lu PAR PARTITION" sans dire laquelle. Sur les boites de qualification les deux lectures s'accordent a 1e-10 ; sur un niveau non fiable elles ne s'accordent pas par construction ;
    C4  "s'accordent a 2 pour cent" : relativement a c2_a (ta sonde) ou a la moyenne (ma feuille) : meme decision tant que l'ecart n'est pas dans [0.0200, 0.0204] ;
    C5  l'egalite aux bornes (<= 1.05, <= 0.02, <= 0.05) : je l'ai lue comme ton code ;
    C6  a rapport egal, la fenetre de plus petit k ;
    C7  la forme du verdict par creneau : voir 8 (R2).

### 2.3 Tes feuilles lues ensuite

Elles font ce que les sections 5.2, 5.4, 5.5, 7 et 8 disent ; mes ecarts de lecture sont ceux de 2.2 et de 8.

### 2.4 Differentiel et matrice de mutations (sorties de sondes SYNTHETIQUES, aucune 2D)

`genere_synthetique_pont_machine2_v*.py` fabrique des fichiers au format de tes sondes (densite aux quatre absorbeurs, vingt boites par cellule) a regimes choisis pour franchir chaque seuil de ta section 7. Ce n'est pas de la physique : ces fichiers portent des w2 candidats pour la compatibilite de format ; ils sont dans un dossier temporaire hors de BOCAL4, detruit apres usage, et ne sont dans aucun lot. Le differentiel passe les deux chaines de feuilles (les miennes, les tiennes, ta chaine sur ta table) et compare, cellule par cellule et famille par famille, les verdicts, les moyennes de S, les rapports de comptes, les lectures de densite (ln R3, ln R2, lisible a chaque ecart) et Q2.

Premier passage (generateur v1, 14 scenarios) et deuxieme (v2, couverture elargie : ecarts illisibles en nombre controle, plateaux entre 1.05 et 1.10, boites hors groupe, ecarts de groupe plus larges ; compare aussi les lectures et Q2) : chacun rend la ligne suivante (journaux differentiel_feuilles_graines_1_14_machine2_v1.log et differentiel_feuilles_v2_graines_1_14_machine2_v1.log)

    BILAN : 14 graines, 0 desaccords sur 336 comparaisons cellule x famille

mais le deuxieme ne produit AUCUNE famille tenue : mes scenarios etaient trop mauvais pour qu'une famille tienne. Je l'ai corrige (v3 : scenarios calmes) et j'ai garde les deux premiers journaux. Passage final (v3, 14 scenarios, 336 comparaisons cellule x famille) :

    BILAN : 14 graines, 0 desaccords sur 336 comparaisons cellule x famille
    repartition des verdicts de LUI (couverture des issues) : C ILLISIBLE : 6 ; C TIENT : 56 ; C TOMBE : 22 ; L ILLISIBLE : 35 ; L TIENT : 40 ; L TOMBE : 9 ; L2 ILLISIBLE : 35 ; L2 TIENT : 41 ; L2 TOMBE : 8 ; S ILLISIBLE : 24 ; S TIENT : 49 ; S TOMBE : 11 ; famille NON JUGEE : 8 ; famille TENUE : 19 ; famille TOMBEE : 29

Passage complementaire (v4, scenarios 101 a 112, sommes posees aux bords des bandes de (S)) :

    BILAN : 12 graines, 0 desaccords sur 288 comparaisons cellule x famille
    repartition des verdicts de LUI (couverture des issues) : C TIENT : 72 ; L TIENT : 72 ; L2 TIENT : 54 ; L2 TOMBE : 18 ; S ILLISIBLE : 1 ; S TIENT : 6 ; S TOMBE : 65 ; famille TENUE : 27 ; famille TOMBEE : 21

MATRICE DE MUTATIONS. Pour savoir si ce differentiel MORD, j'altere tes trois feuilles une constante ou un test a la fois (dans un dossier temporaire ; tes feuilles du lot ne sont pas touchees) et je regarde s'il voit l'alteration. Tableau (journal matrice_mutations_feuilles_synthese_machine2_v1.log) :

    alteration                 premier passage (generateur v1)    passage final (generateur v3)     passage complementaire (v4)
    plateau_105_en_110         6 graines : 0 desaccords           14 graines : 105 desaccords        -                                  MORDUE
    etendue_002_en_003         6 graines : 11 desaccords          14 graines : 70 desaccords         -                                  MORDUE
    etendue_inf_strict         6 graines : 2 desaccords           14 graines : 15 desaccords         -                                  MORDUE
    mediane_en_moyenne         6 graines : 0 desaccords           14 graines : 59 desaccords         -                                  MORDUE
    w0_sans_mediane            6 graines : 0 desaccords           14 graines : 59 desaccords         -                                  MORDUE
    part_non_fiable_10         6 graines : 13 desaccords          14 graines : 43 desaccords         -                                  MORDUE
    compte_sans_couverte       6 graines : 8 desaccords           14 graines : 29 desaccords         -                                  MORDUE
    S_largeur_8                6 graines : 21 desaccords          14 graines : 62 desaccords         -                                  MORDUE
    participation_inverse      6 graines : 0 desaccords           14 graines : 28 desaccords         -                                  MORDUE
    L_tol_006                  6 graines : 2 desaccords           14 graines : 7 desaccords          -                                  MORDUE
    L_min_ecarts_9             6 graines : 0 desaccords           14 graines : 2 desaccords          -                                  MORDUE
    L2_x_4                     6 graines : 3 desaccords           14 graines : 5 desaccords          -                                  MORDUE
    L2_large                   6 graines : 0 desaccords           14 graines : 0 desaccords          -                                  NON MORDUE
    S_cellule_080              6 graines : 3 desaccords           14 graines : 0 desaccords          12 graines : 24 desaccords         MORDUE
    S_groupe_075               6 graines : 0 desaccords           14 graines : 0 desaccords          12 graines : 28 desaccords         MORDUE
    C_reduit_bas_030           6 graines : 1 desaccords           14 graines : 3 desaccords          -                                  MORDUE
    C_rapport_haut_200         6 graines : 1 desaccords           14 graines : 4 desaccords          -                                  MORDUE
    min_boites_7               6 graines : 9 desaccords           14 graines : 6 desaccords          -                                  MORDUE
    famille_sans_creneau       6 graines : 0 desaccords           14 graines : 0 desaccords          -                                  NON MORDUE
    famille_trois_cellules     6 graines : 1 desaccords           14 graines : 1 desaccords          -                                  MORDUE
    groupe_UN_179              6 graines : 0 desaccords           14 graines : 157 desaccords        -                                  MORDUE
    alterations mordues (passage final ou complementaire) : 19 sur 21

Au premier passage (v1, six scenarios) douze alterations sur vingt et une etaient mordues ; les autres ne l'etaient pas parce que mon generateur ne produisait pas les cas qui les distinguent (aucun cas a neuf ecarts lisibles, aucun plateau entre 1.05 et 1.10, aucune boite hors groupe, ni lectures ni Q2 comparees, somme jamais aux bords des bandes). Les passages v2, v3 et v4 comblent ces trous ; la derniere ligne du tableau donne le compte final. Les alterations non mordues, et pourquoi :
- famille_sans_creneau : alteration EQUIVALENTE avec six cellules, trois par creneau : quatre cellules lisibles ne peuvent pas toutes etre du meme creneau, la clause "dont une au moins par creneau" ne change aucun verdict a six cellules. Elle ne mord qu'avec d'autres effectifs.
- L2_large (remplacer "<" par "<=" dans L2) : il faudrait |ln R3| = |ln R2| a l'ecart pres du dernier bit, evenement de mesure nulle sur des donnees continues. Je ne l'ai pas fabrique. Je l'ai verifie par la lecture de ton code (la comparaison est stricte, comme le texte de (L2)) et par ton controle R07.

### 2.5 Une sortie de sonde interrompue est acceptee en silence

Ta sonde de densite reecrit son fichier JSON apres chaque barreau. Une sortie interrompue (ici : barreaux -3 a 5 seulement, SA5, quatre absorbeurs) est acceptee SANS erreur par ta feuille de densite, qui lit alors moins de fenetres de plateau ; la mienne l'etait aussi, je lui ai ajoute un refus (journal feuilles_qualification/tronque/essai_sortie_tronquee_machine2_v1.log). Sur ce cas la lecture ne change pas, parce que les plateaux sont a bas k ; rien ne le garantit en general. Au run je verifierai moi-meme que chaque sortie porte les douze barreaux avant de la donner aux feuilles. Je te le dis pour que ta feuille le dise aussi, si tu juges utile.

### 2.6 Ton releve rejoue sur BOCAL4

    RELEVE : 11 controles ; 1 MORSURE(S) : R11

R01 a R10 : OK. R11 compare au caractere pres la sortie rejouee de la feuille de verdict a la piece deposee. Nombre par nombre (journal rejeu_releve_m1/compare_json_nombres_R11_machine2_v1.log) :

    91 nombres compares (NaN contre NaN tenus pour egaux) ; nombres differents : 1 ; plus grand ecart relatif 2.01e-16 (/cellules/SA5/Q3_somme_avec_la_densite_2d/moyenne)

Un nombre sur 91, au dernier bit (la somme de y exp(-ln R) de la question Q3, que ta feuille ne juge pas) : bruit de plate-forme (exp de la bibliotheque mathematique), pas un contenu. Tous les verdicts sont identiques. C'est la meme famille que la non-reproduction a l'octet de ton JSON d'eligibilite de la premiere partie : R11 gagnerait a comparer avec une tolerance de 1e-12.

## 3. (a) Le tirage

Ta section 2, ton journal tirage_pont_graine_456823_machine1_v1.log et le mien (enveloppe 17p) donnent les memes six cellules, aux memes couplages ecrits (journal confronte_tirage_m1_machine2_v1.log) :

    memes six cellules (noms et g ecrits) : True

Ton journal dit "tables : 1" ; mon rejeu de ton code dans l'enveloppe 17p disait "tables : 2" (la tienne et la mienne). Le resultat est le meme.

## 4. (c) Tes sondes sur BOCAL4, au point sacrifie (w2 = 101/50)

Les trois commandes de ta note, plus trois autres ; sorties dans sacrifie/. Machine : 16 processeurs logiques, 27.8 Go ; Python 3.11, numpy 2.2.6, scipy 1.15.3.

    densite SA5, absorbeur A, 12 barreaux (densite_2d_SA5_A_machine2.log) :
        ecrit densite_2d_SA5_A_machine2.json (1456 s)
        (compare_densite_SA5_A_machine2_v1.log, k = 2) plus grand |ln(rho_flux ma/sa)| 6.75e-14 ; le plus grand ecart sur E_vide est de 4.8e-20 (k = 6), sur w0 de 1.5e-14 (k = 6)
    boite 185, 3 barreaux (# fini (42 s)) :
        niveaux appaires : plus grand ecart sur E 4.52e-15, sur x 2.26e-13 ; relatif sur c2_a 2.92e-10, c2_b 1.17e-10, c2_a_large 2.47e-10, brut_a 3.43e-04
    boite 300, 5 barreaux (# fini (209 s)) :
        niveaux appaires : plus grand ecart sur E 1.47e-14, sur x 7.33e-13 ; relatif sur c2_a 1.17e-10, c2_b 5.79e-11, c2_a_large 9.13e-11, brut_a 3.84e-02
    boite 300, 3 barreaux (en plus) :
        niveaux appaires : plus grand ecart sur E 2.04e-14, sur x 1.02e-12 ; relatif sur c2_a 1.45e-10, c2_b 3.41e-11, c2_a_large 2.05e-10, brut_a 1.70e-04
    boite 300, 4 barreaux (en plus) :
        niveaux appaires : plus grand ecart sur E 5.55e-14, sur x 2.78e-12 ; relatif sur c2_a 1.76e-10, c2_b 1.18e-10, c2_a_large 1.54e-10, brut_a 1.35e-02

Les niveaux, les comptes, les drapeaux "fiable" sont identiques aux tiens ; ta lecture BRUTE ne se reproduit pas d'une machine a l'autre (brut_a : 3.84e-02 a 5 barreaux, cote 300), ta lecture par PARTITION oui (1e-10). C'est ta these de 6., sur deux machines.

Cout d'un run complet (journal cout_run_machine2_v1.log : estimation, pas mesure ; hypotheses imprimees) :

    temps mesures (secondes par boite, une boite par essai, plusieurs jobs en parallele sur la machine) : {(3, 185): 35, (3, 300): 132, (4, 300): 130, (5, 185): 24, (5, 300): 186}
    densite, absorbeur A, 5 barreaux : 12 barreaux lus, 1454 s au total (moyenne 121 s par barreau)
    estimation : densite 13.0 h de coeur, boites 3.0 h de coeur, total 16.0 h de coeur (hypotheses : cout ~ cote^3 entre absorbeurs ; boites UN ~ la boite 185 mesuree, DEUX ~ la 300 mesuree ; 2 cellules par profondeur)
       avec  4 jobs en parallele : environ 4.0 h (en negligeant la contention memoire et le desequilibre)
       avec  8 jobs en parallele : environ 2.0 h (en negligeant la contention memoire et le desequilibre)
       avec 12 jobs en parallele : environ 1.3 h (en negligeant la contention memoire et le desequilibre)
    pic de memoire, densite, absorbeur B (le plus grand : boite 128 x 128), 5 barreaux, un barreau : code de sortie 0 ; duree 205 s ; pic de memoire de travail du processus 0.38 Go
    pic de memoire, boite de cote 300, 5 barreaux : code de sortie 0 ; duree 134 s ; pic de memoire de travail du processus 1.71 Go

Pic de memoire (Windows, interpreteur lance directement) : boite de cote 300 a 5 barreaux 1.71 Go, 134 s seule ; densite a l'absorbeur B (le plus grand, boite 128 x 128), un barreau : 0.38 Go, 205 s. Mon plan : au plus huit jobs a la fois, soit environ deux heures, une fois le feu vert donne.

## 5. (d) La lecture par partition

Je l'ai refaite depuis le texte de 5.3 AVANT de lire ta sonde (partition_independante_machine2_v1.py), sur la boite de cote 300 a 5 barreaux, avec d'autres decalages que les tiens (2 et 5.5 |delta|, au lieu de 2.5 et 5.5) et quatre coupures : r_c, r_c + 6, r_c + 12 et un diamant (a + b <= 50). Ecarts relatifs entre les deux decalages, par lecture :

    brut         plus grand 1.91e-02
    carre_rc     plus grand 5.77e-11
    carre_rc+6   plus grand 4.00e-11
    carre_rc+12  plus grand 6.29e-11
    diamant      plus grand 4.34e-11
    coupures entre elles (decalage 2) : carre_rc+6 / carre_rc 5.17e-11 ; carre_rc+12 / carre_rc 5.09e-11 ; diamant / carre_rc 4.98e-11

et contre la tienne, niveau par niveau (journal compare_partition_SA5_300_machine2_v1.log) :

    plus grand ecart relatif de ma partition a la sienne : lecture a 5.89e-11 ; lecture b (mon decalage 5.5 contre son 5.5) 3.52e-11 ; r_c+6 4.97e-11

Le brut ne s'ecarte de la partition que ou le poids est minuscule : pour c2 >= 1e-17 il s'en tient a 1e-5, pour c2 <= 1e-21 il erre de 1e-3 a 2e-2 (le tableau est dans le journal). Le brut est donc un plancher de bruit ; la partition ne depend ni du decalage, ni du rayon, ni de la FORME de la coupure, a 6e-11. Je l'accepte comme lecture du gel.

Ton ecart a ta clause ("si B3 ou B4 tombe, la lecture du gel sera la lecture brute a deux decalages") : je ne le tiens pas pour une faute. B3 comparait la partition au brut a 1e-3 ; ce que les pieces montrent est que c'est le brut qui flotte. Il reste un fait de forme : c'est une lecture changee APRES avoir vu des donnees, au point sacrifie, avant toute cellule tiree ; tu l'as dit, je le redis. Rien n'a ete verifie en precision etendue : la partition est jugee sur sa stabilite et sur deux implementations, pas sur une valeur de reference exacte.

Les nombres de ta section 6 que j'ai relus dans tes sorties (journal verifie_nombres_section6_machine2_v1.log) sont exacts :

    3 barreaux : partition 2.33e-10 ; brut 2.72e-04 ; niveaux 19, fiables 19
    4 barreaux : partition 1.69e-10 ; brut 8.32e-03 ; niveaux 19, fiables 19
    5 barreaux : partition 4.74e-11 ; brut 1.52e-02 ; niveaux 19, fiables 19
    (4) sur 17 boites jouees : plus grand ecart relatif partition(r_c + 6) / partition(r_c) : 2.45e-09

ainsi que le niveau B4 et le vide (meme journal).

## 6. (e) Ma table de la section 4

Ma chaine (chaine_pont_machine2_v1.py, ecrite du texte, rejouee sur BOCAL4) contre ton texte, ton JSON et mes details de la premiere partie (journal confronte_section4_machine2_v1.log) :

    ln(rho_3 |delta|) : ma chaine contre le TEXTE (arrondi a 2 decimales) : plus grand ecart 0.0049 (borne de l arrondi 0.005) ; contre le JSON de machine 1 : 5.28e-12
    pas (ordre 2 -> 3) : ma chaine contre le TEXTE (arrondi a 4 decimales) : plus grand ecart 0.00005 (borne 0.00005) ; contre le JSON de machine 1 : 5.16e-12

m_bord, e_bord, r_c, G3*, etendues au vide et du lisse, pas maximal : les six lignes de la table de tete sont retrouvees (G3* : le plus grand ecart relatif est a MG5, "(rapport 1.000043)", l'arrondi de cinq chiffres du texte). C'est SON fichier que mes feuilles liront au run, comme tu le dis.

## 7. (f) Aucune 2D a ces w2

Balayage de structure (journal balayage_2d_candidats_machine2_v1.log), dans ta livraison et dans mon dossier de travail :

    53 fichiers JSON/JSONL lus dans 2 dossier(s)
    fichiers au format 2D portant un w2 candidat : 0

Ce que j'ai calcule, exactement : au point sacrifie w2 = 101/50, trois densites et six boites (ci-dessus) ; la chaine a une dimension aux neuf cellules (six tirees et SA3, SA4, SA5), qui n'est pas une 2D ; les MATRICES H de ta sonde et de la mienne a w2 = 197/100, N = 40, comparees entree par entree (journal equivalence_hamiltonien_machine2_v1.log) :

    w2 = 197/100 (delta = -0.030) : N = 40, entrees non nulles 53695 (lui) / 53695 (moi), plus grand |H(lui) - H(moi)| = 0.000e+00, plus grande entree 7.683e+01

sans en diagonaliser aucune : aucun niveau, aucune densite, aucune part a delta < 0. Ton aveugle sur MG est intact ; le chemin d'assemblage a delta < 0 est, lui, le meme que le mien.

## 8. Reserves de redaction (aucune ne change une decision de ta piece)

    R1  C3 ci-dessus : dire quelle lecture par partition entre dans y (ta feuille : la premiere, c2_a).
    R2  "Le verdict est rendu par famille, et par creneau a cote" (7) : ta feuille ne ressort que la famille ; le creneau se lit sur les lignes par cellule. Je rendrai aussi les creneaux, a la main, depuis ces lignes.
    R3  Q1 et Q2 : l'unite n'est pas dite. Ta feuille poole toutes les boites lisibles pour Q2 et celles des cellules lisibles pour (S) pour Q1 ; les groupes de Q2 mele les cellules. Rien n'est juge ; a six cellules lisibles les deux lectures coincident.
    R4  Le mot "barreaux" designe a la fois les douze barreaux d'absorbeur et les profondeurs 3, 4, 5 de la chaine.
    R5  (L2) : le texte donne "TIENT" a vide si aucun ecart >= 5 n'est lisible, ta feuille "ILLISIBLE" ; impossible avec au moins dix ecarts lisibles sur douze.
    R6  Ta feuille de verdict en mode REPETITION assouplit "au moins quatre cellules" (min(4, n)) : elle le dit ; a six cellules c'est la regle du texte.
    R7  Une boite sans niveau serait "lisible" par le texte (0 <= 5 pour cent de 0) et non lisible par ta feuille : cas qui ne s'est pas produit (n est de 10 a 19 dans les groupes de qualification), mais le texte ne le dit pas.
    R8  R11 de ton releve et la reproductibilite a l'octet : 2.6.

## 9. Ce que je n'ai PAS fait

- Je n'ai joue aucune 2D aux six cellules tirees, et aucun pilote de run n'est ecrit : je l'ecrirai et le testerai AU POINT SACRIFIE avant le feu vert, pas apres.
- La lecture par partition n'est pas verifiee en precision etendue (5.).
- Ma feuille ne calcule pas Q4 (le vide contre G3*) ; je n'ai compare que Q1, Q2, Q3.
- Les chemins de ta sonde de densite et de boite a delta < 0 ne sont verifies que par leurs matrices (7.) : pas par un niveau, pour garder ton aveugle.
- Je n'ai pas pose de probabilites : tes annonces sont a toi.
- Le differentiel est sur des sorties synthetiques : il eprouve la LOGIQUE des feuilles, pas la physique.

## 10. Suite

(1) l'operateur donne, ou non, le feu vert ECRIT ; (2) je joue UNE fois, aux six cellules, vingt boites et quatre absorbeurs chacune, avec tes commandes ; (3) je passe les trois feuilles et je rends le tout, journaux compris ; (4) tu rejoues tes trois feuilles sur mes sorties. Rien n'est depose ; le registre public reste en tete 2988237, prochain numero libre 103.

## 11. Pieces

Chaque piece est citee avec son canon (empreinte B, 16 hex). Le canon du lot est celui du manifeste.

    cette note
    fc6c5e855cbe3cf1  certif_gel_pont_partie2_machine2/chaine_pont_machine2_v1.py
    d33bba3da1996bb5  certif_gel_pont_partie2_machine2/feuilles_pont_machine2_v1.py
    35a401d4165ec19e  certif_gel_pont_partie2_machine2/compare_feuilles_machine2_v1.py
    01bb594c16ccae10  certif_gel_pont_partie2_machine2/genere_synthetique_pont_machine2_v1.py
    0e36775132bbe7e9  certif_gel_pont_partie2_machine2/genere_synthetique_pont_machine2_v2.py
    b6e841e46da4af27  certif_gel_pont_partie2_machine2/genere_synthetique_pont_machine2_v3.py
    895220fb8c4bf6ab  certif_gel_pont_partie2_machine2/genere_synthetique_pont_machine2_v4.py
    c0f16de2e9261222  certif_gel_pont_partie2_machine2/differentiel_feuilles_machine2_v1.py
    4c7095fc05f617d8  certif_gel_pont_partie2_machine2/differentiel_feuilles_machine2_v2.py
    eac0295575355d6f  certif_gel_pont_partie2_machine2/differentiel_feuilles_machine2_v3.py
    c285bc2f5c37d380  certif_gel_pont_partie2_machine2/differentiel_feuilles_machine2_v4.py
    c797bcb8db2b9cb6  certif_gel_pont_partie2_machine2/partition_independante_machine2_v1.py
    7c708cef1810017d  certif_gel_pont_partie2_machine2/compare_partition_machine2_v1.py
    828b9844a3c12fa8  certif_gel_pont_partie2_machine2/compare_sondes_sacrifie_machine2_v1.py
    9075a31876ec76c4  certif_gel_pont_partie2_machine2/equivalence_hamiltonien_machine2_v1.py
    b68002e008e77cbb  certif_gel_pont_partie2_machine2/confronte_section4_machine2_v1.py
    deb925579c7e421a  certif_gel_pont_partie2_machine2/verifie_nombres_section6_machine2_v1.py
    952677521175a9f1  certif_gel_pont_partie2_machine2/balayage_2d_candidats_machine2_v1.py
    bf7e54a4c1937050  certif_gel_pont_partie2_machine2/verifie_flux_direct_machine2_v1.py
    35bd4f2ef7239d0c  certif_gel_pont_partie2_machine2/cout_run_machine2_v1.py
    e488bc3f9f3f4f8c  certif_gel_pont_partie2_machine2/mesure_pic_memoire_machine2_v1.py
    b51635e51ea01dea  certif_gel_pont_partie2_machine2/compare_json_nombres_machine2_v1.py
    d9d793ddd5078380  certif_gel_pont_partie2_machine2/synthese_mutations_feuilles_machine2_v1.py
    978288c6e7fc8a89  certif_gel_pont_partie2_machine2/journaux/confronte_tirage_m1_machine2_v1.log
    23926e0948182ee2  certif_gel_pont_partie2_machine2/journaux/confronte_section4_machine2_v1.log
    8c5134d7ec8c35a2  certif_gel_pont_partie2_machine2/journaux/verifie_nombres_section6_machine2_v1.log
    22aca92dded74313  certif_gel_pont_partie2_machine2/journaux/equivalence_hamiltonien_machine2_v1.log
    f905c05ad44bf1ee  certif_gel_pont_partie2_machine2/journaux/balayage_2d_candidats_machine2_v1.log
    0f4cb26f978b3683  certif_gel_pont_partie2_machine2/journaux/cout_run_machine2_v1.log
    22b48264a23a4c71  certif_gel_pont_partie2_machine2/journaux/verifie_flux_direct_machine2_v1.log
    4d675a98dc3e79ed  certif_gel_pont_partie2_machine2/journaux/differentiel_feuilles_graines_1_14_machine2_v1.log
    fc8d18ffb155caa0  certif_gel_pont_partie2_machine2/journaux/differentiel_feuilles_v2_graines_1_14_machine2_v1.log
    994883a45d857796  certif_gel_pont_partie2_machine2/journaux/differentiel_feuilles_v3_graines_1_14_machine2_v1.log
    e6496131e601a232  certif_gel_pont_partie2_machine2/journaux/differentiel_feuilles_v4_graines_101_112_machine2_v1.log
    23588addccb7abd6  certif_gel_pont_partie2_machine2/journaux/matrice_mutations_feuilles_synthese_machine2_v1.log
    e94b605594cb2c66  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_C_rapport_haut_200_machine2_v1.log
    8737fbb402392d14  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_C_reduit_bas_030_machine2_v1.log
    b197a2ad242d0ad1  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_L2_large_machine2_v1.log
    cc20bdeb0cb3113f  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_L2_x_4_machine2_v1.log
    ee6fe53434771e17  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_L_min_ecarts_9_machine2_v1.log
    754c87149c709778  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_L_tol_006_machine2_v1.log
    702578765d06533a  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_S_cellule_080_machine2_v1.log
    bf8eaec7893f4e99  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_S_groupe_075_machine2_v1.log
    6c700243a050fc47  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_S_largeur_8_machine2_v1.log
    08b569b993cf2e1a  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_compte_sans_couverte_machine2_v1.log
    cdb2648c4bcc5bec  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_etendue_002_en_003_machine2_v1.log
    e64d31f1892bb0d9  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_etendue_inf_strict_machine2_v1.log
    68f0d2f615ea89ca  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_famille_sans_creneau_machine2_v1.log
    65a9a69f19bbe88e  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_famille_trois_cellules_machine2_v1.log
    0a9554c851939c31  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_groupe_UN_179_machine2_v1.log
    4837eccb35b03b1e  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_mediane_en_moyenne_machine2_v1.log
    e8e777a017b70ad8  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_min_boites_7_machine2_v1.log
    5fc9da38e6064433  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_part_non_fiable_10_machine2_v1.log
    36c8080cf6bfeadf  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_participation_inverse_machine2_v1.log
    2d2387ce97fbdc68  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_plateau_105_en_110_machine2_v1.log
    afd6f52ec58a8742  certif_gel_pont_partie2_machine2/journaux/mutations/mutation_w0_sans_mediane_machine2_v1.log
    60a942d8720241ea  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_C_rapport_haut_200_machine2_v1.log
    c312f88e7eee6bae  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_C_reduit_bas_030_machine2_v1.log
    6c8d394f085b547f  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_L2_large_machine2_v1.log
    21bd0c0d3409b528  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_L2_x_4_machine2_v1.log
    4e54b8d873d1858b  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_L_min_ecarts_9_machine2_v1.log
    e2254fe54e205493  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_L_tol_006_machine2_v1.log
    c89a0717b60bd2e3  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_S_cellule_080_machine2_v1.log
    8b8d0dd070352247  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_S_groupe_075_machine2_v1.log
    a6cc0caa360474df  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_S_largeur_8_machine2_v1.log
    2f252eacfee2802f  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_compte_sans_couverte_machine2_v1.log
    058884c9b863a286  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_etendue_002_en_003_machine2_v1.log
    4ba1c1080d639bf2  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_etendue_inf_strict_machine2_v1.log
    de048af0264219b3  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_famille_sans_creneau_machine2_v1.log
    db66a599f2ea8180  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_famille_trois_cellules_machine2_v1.log
    983fcfb0a52dc1f5  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_groupe_UN_179_machine2_v1.log
    e26e9c7a4ca1e17b  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_mediane_en_moyenne_machine2_v1.log
    e1d1f78c50395791  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_min_boites_7_machine2_v1.log
    12ce77108e6ab680  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_part_non_fiable_10_machine2_v1.log
    9491fa43661c3c2d  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_participation_inverse_machine2_v1.log
    2f9a9f4d6d26d17c  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_plateau_105_en_110_machine2_v1.log
    b8bfa54999740185  certif_gel_pont_partie2_machine2/journaux/mutations_v3/mutation_w0_sans_mediane_machine2_v1.log
    c80925c4dae1875a  certif_gel_pont_partie2_machine2/journaux/mutations_v4/mutation_S_cellule_080_machine2_v1.log
    ff337a2293fa3f67  certif_gel_pont_partie2_machine2/journaux/mutations_v4/mutation_S_groupe_075_machine2_v1.log
    e9d2bb3b13045daf  certif_gel_pont_partie2_machine2/chaine_pont_machine2_v1.log
    ddf8951f05001aec  certif_gel_pont_partie2_machine2/chaine_pont_machine2_v1.json
    6183cb49ad885813  certif_gel_pont_partie2_machine2/feuilles_qualification/lecture_densite_2d_qualification_machine2_v1.log
    65898c7b6011507b  certif_gel_pont_partie2_machine2/feuilles_qualification/lecture_densite_2d_SA3_machine2.json
    eae384667945426d  certif_gel_pont_partie2_machine2/feuilles_qualification/lecture_densite_2d_SA4_machine2.json
    7d51ac36edf5e858  certif_gel_pont_partie2_machine2/feuilles_qualification/lecture_densite_2d_SA5_machine2.json
    985a3cbcdea9427c  certif_gel_pont_partie2_machine2/feuilles_qualification/lecture_boites_repetition_machine2_v1.log
    328bbedc62a8485e  certif_gel_pont_partie2_machine2/feuilles_qualification/lecture_boites_repetition_machine2.json
    880048f5c4aace66  certif_gel_pont_partie2_machine2/feuilles_qualification/repetition_verdict_machine2_v1.log
    cd1156b981a7969f  certif_gel_pont_partie2_machine2/feuilles_qualification/repetition_verdict_machine2.json
    8effd2863829a5c4  certif_gel_pont_partie2_machine2/feuilles_qualification/compare_feuilles_repetition_machine2_v1.log
    34da47ca04f72230  certif_gel_pont_partie2_machine2/feuilles_qualification/tronque/essai_sortie_tronquee_machine2_v1.log
    1e9b520b424b3f0c  certif_gel_pont_partie2_machine2/rejeu_releve_m1/rejeu_releve_gel_pont_partie2_machine2_v1.log
    95753bba927de229  certif_gel_pont_partie2_machine2/rejeu_releve_m1/compare_json_nombres_R11_machine2_v1.log
    5430e5d43c481887  certif_gel_pont_partie2_machine2/rejeu_releve_m1/repetition_verdict_rejoue_machine2.log
    bc9da8a2ca84ae3b  certif_gel_pont_partie2_machine2/sacrifie/densite_2d_SA5_A_machine2.log
    755311c9919b157c  certif_gel_pont_partie2_machine2/sacrifie/densite_2d_SA5_A_machine2.json
    62e6b161139b3ec6  certif_gel_pont_partie2_machine2/sacrifie/compare_densite_SA5_A_machine2_v1.log
    02d5071453863dfe  certif_gel_pont_partie2_machine2/sacrifie/boite_SA3_185_machine2.log
    9903b4e16c0358b6  certif_gel_pont_partie2_machine2/sacrifie/boite_SA3_185_machine2.jsonl
    ea536f444e86f3ae  certif_gel_pont_partie2_machine2/sacrifie/compare_boite_SA3_185_machine2_v1.log
    c43a4de82bb70fc1  certif_gel_pont_partie2_machine2/sacrifie/boite_SA3_300_machine2.log
    161f1e675f41babe  certif_gel_pont_partie2_machine2/sacrifie/boite_SA3_300_machine2.jsonl
    fd881a0bbaf02378  certif_gel_pont_partie2_machine2/sacrifie/compare_boite_SA3_300_machine2_v1.log
    89242c0b7104879e  certif_gel_pont_partie2_machine2/sacrifie/boite_SA4_300_machine2.log
    bd5a9c6d043ccef9  certif_gel_pont_partie2_machine2/sacrifie/boite_SA4_300_machine2.jsonl
    705bdaa13ef4d7b1  certif_gel_pont_partie2_machine2/sacrifie/compare_boite_SA4_300_machine2_v1.log
    982a54410139b185  certif_gel_pont_partie2_machine2/sacrifie/boite_SA5_300_machine2.log
    2c27efb903d8f233  certif_gel_pont_partie2_machine2/sacrifie/boite_SA5_300_machine2.jsonl
    6843c2506ee4f4eb  certif_gel_pont_partie2_machine2/sacrifie/compare_boite_SA5_300_machine2_v1.log
    cbe02a459dae706a  certif_gel_pont_partie2_machine2/sacrifie/boite_SA5_185_machine2.log
    e6d1d785dc6bc697  certif_gel_pont_partie2_machine2/sacrifie/boite_SA5_185_machine2.jsonl
    88564fdd3322a5b7  certif_gel_pont_partie2_machine2/sacrifie/partition_SA5_300_machine2_v1.log
    1da95d4ed08ac912  certif_gel_pont_partie2_machine2/sacrifie/partition_SA5_300_machine2.json
    3965b8daac708d86  certif_gel_pont_partie2_machine2/sacrifie/compare_partition_SA5_300_machine2_v1.log
    987d37f31366cdf3  certif_gel_pont_partie2_machine2/sacrifie/pic_memoire/pic_densite_B_k8_machine2.log
    8e54a4cf36fe9a5e  certif_gel_pont_partie2_machine2/sacrifie/pic_memoire/pic_boite_300_machine2.log
    07e0fba4cd4138c5  livraison_17b_gel_pont_partie2/authentification_envoi_machine2_v1.log
    7f6421ee350f4f39  certif_gel_pont_partie1_machine2/authentifie_envoi_m1_machine2_v1.py
    (ce script)  fabrique_lot_certification_gel_pont_partie2_machine2_v1.py
