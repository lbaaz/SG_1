GEL "LOI DE LA LARGEUR, ORDRE 3" -- SECONDE PARTIE : L'INSTRUMENT, LES ENONCES, LES TOLERANCES
PRE-ENREGISTREMENT v1 -- machine 1, 2026-11-16 (nuit du 15 au 16).
A CERTIFIER PAR MACHINE 2 AVANT TOUT CALCUL 2D A L'UNE DES DOUZE CELLULES.

0. STATUT
  Cette piece complete la premiere partie (b56ca5cb2dd25da1, lot 596a45bf6d4f97d7), que machine 2
  a certifiee telle quelle, a zero morsure (lot 4fb1dc66f96f57f6). Elle fixe les douze cellules
  tirees, l'instrument du run, les enonces juges, leurs tolerances, ce que chaque issue engage, et
  les annonces de la plume. Rien n'est joue : aucune des douze cellules n'a ete calculee en 2D,
  par aucune des deux machines.
  Ouverture. L'operateur a atteste a machine 1 (15/11/2026, 22 h 54) que son "Reprends" de 22 h 42
  etait bien le "go" du gel. Machine 2 dit avoir recu de lui "OK go on gel", sans pouvoir le dater
  (lot 4fb1dc66f96f57f6, section 2).
  Graine. L'operateur a donne la graine 200482 a machine 1 par ecrit (15/11/2026, 23 h 19), apres
  la certification de la premiere partie ; il l'a ecrite sous forme de question, machine 1 a
  repondu que sa valeur n'appelait pas d'avis de sa part et l'a prise comme donnee. Machine 1
  n'avait calcule aucun tirage avant de la recevoir. Machine 2 rapporte l'avoir recue de
  l'operateur (lot 220a0970134335e1). Les mots exacts sont dans la note d'accompagnement.
  Tirage. Par le script de machine 1 (0f608f8ade6ff378) et par ceux de machine 2 (c3128f277ef97d26
  et d6eb47056ec5b534), sur le ET des deux tables d'eligibilite (f11ac4458a336650 et
  e7a530fde7efd9cf, identiques) : les quatre creneaux sortent au rang 0 et les douze cellules des
  deux machines sont les memes, une a une (lot 220a0970134335e1 ; journal de machine 1 joint).
  E19. Aucun calcul 2D, dense ou creux, a aucune des douze cellules, par aucune des deux machines,
  avant la certification croisee de cette piece et le feu vert ecrit de l'operateur. Tout ce que
  cette piece calcule aux cellules est une chaine a une dimension. Les calculs 2D qu'elle rapporte
  (pre-vol, section 4.6) sont a des points DEJA JOUES.

1. QUESTION ET PERIMETRE
  La note sur la loi de la largeur (lot e93f1898dcd78a8f) a lu, sur 131 etats de douze points deja
  joues, qu'une chaine a une dimension poussee a l'ordre 3 rend la largeur de plateau a quelques
  centiemes pres DANS UN DOMAINE (e_bord < 0.7 et chaine d'ordre 3 stable), et qu'elle s'egare
  au-dela. C'etait lu apres coup, sur des points choisis pour autre chose. Ce gel demande si cela
  tient a des points que personne n'a choisis : douze cellules tirees au sort par une graine de
  l'operateur.
  Perimetre : un w2 par ligne (delta = -0.065 et +0.035), cinq couplages par ligne, et deux
  cellules de bord (delta = -0.076 et +0.067). L'objet juge est la chaine du bloc d'ordre 3 de
  machine 1 (534ba246aa3b8973), telle quelle. La reference est la largeur de plateau sous
  l'absorbeur A, lue par le lecteur creux du gel ter (432319b9feb34b82).

2. SOURCES (convention B)
    82a0be882568fe0c scripts/m17_chaine_v17.py (registre 8d54bf9), le moteur
    7cd5977bc27bebc1 scripts/chaine_ordre2_bloc_machine1_v1.py (registre), le bloc d'ordre 2
    534ba246aa3b8973 ordre3_bloc_machine1_v1.py (lot e93f1898dcd78a8f ; joint ici), le bloc
                      d'ordre 3, rederive par machine 2 (lot 889fe9b4c1c1c60a)
    10887c60d5f55bcf journal/sonde_ordre2.json (registre), le depot du delta 98 : ancres, et
                      sortie dense du pre-vol
    41153158190cf7f1 gels/gel_ordre2_chaine_EA_pre_enregistrement_v1.md (registre) : regle du
                      point, bandes de l'ordre 2
    24315c52b234319c scripts/sonde_ordre2_machine1_v1.py (registre) : la sonde dense certifiee
    432319b9feb34b82 qualification_EB_ter_pre_enregistrement_v1.md (lot 42110a3d1eabdaa0) : le
                      lecteur, ses epreuves, ses statuts
    b5616dcf858e8801 sonde_qualification_EB_ter_machine1_v1.py (meme lot) : la sonde du lecteur
                      certifiee
    b2d6d7cfaf30f1cf lecture_qualification_EB_ter_machine1_v1.py (meme lot) : la feuille du
                      lecteur certifiee
    69b3bab3bb8480b7 journal/tp_retenus_machine2_v1.json (registre) : couplages du temoin
    4d51dd58ef456fe9 journal/tp_reference_machine2_v1.json (registre) : reference du temoin
    6600fb8418c79930 reference_ancres_ter_machine1_v1.json (lot 42110a3d1eabdaa0) : reference des
                      ancres
    b56ca5cb2dd25da1 gel_loi_ordre3_partie1_regle_tirage_pre_enregistrement_v1.md (lot
                      596a45bf6d4f97d7)
    4fb1dc66f96f57f6 lot de machine 2 : certification de la premiere partie, sa table, la table
                      commune
    220a0970134335e1 lot de machine 2 : son tirage sur la graine 200482
    2cd1f84efa02f2ab verdict_ter.json du run du gel ter (lot 1f057651c8f69eb6 de machine 2) : les
                      largeurs de plateau des points deja joues.
  L'acte du gel ter (751165a3eee613d9, lot 26b3912297b31713) est contresigne par machine 2 (lots
  e8ff4d600edf89ef et b42a63640f1c566a) et N'EST PAS ENCORE DEPOSE : le clone de machine 1 est a
  8d54bf9, et les enveloppes de machine 2 du 15/11 disent le registre a ce numero. La reference de
  ce gel s'appuie donc sur un acte contresigne, pas sur un acte depose (section 13, L-2).

3. LES DOUZE CELLULES
  Table gelee : table_points_gel_loi_ordre3_v1.json, canon 35fa7b73f2b7f8eb. Elle porte la graine,
  le rang, les douze cellules (role "juge") et les deux ancres du depot, A1 (w2 = 39/20) et A2
  (41/20), au facteur 1 (role "ancre"). Les scripts de l'instrument lisent les points dans cette
  table et portent son canon en dur.
  Par cellule : w2, delta, facteur, couplage g = facteur x g_du_point(w2), boite N de la sonde
  dense ; puis, pour les quatorze etiquettes PREDITES par la chaine (premiere partie, section 4) :
  etats jugeables / dans le domaine / hors du domaine.
    N1  w2 = 387/200   delta -0.065  x3/4  g = 1.6697e-03  N = 68   predits 11 / 11 /  0
    N2  w2 = 387/200   delta -0.065  x5/6  g = 1.8552e-03  N = 63   predits 10 / 10 /  0
    N3  w2 = 387/200   delta -0.065  x1/1  g = 2.2262e-03  N = 60   predits 12 / 12 /  0
    N4  w2 = 387/200   delta -0.065  x6/5  g = 2.6715e-03  N = 57   predits 13 / 13 /  0
    N5  w2 = 387/200   delta -0.065  x4/3  g = 2.9683e-03  N = 55   predits 14 / 14 /  0
    P1  w2 = 407/200   delta +0.035  x3/4  g = 1.3105e-03  N = 69   predits 12 / 12 /  0
    P2  w2 = 407/200   delta +0.035  x5/6  g = 1.4561e-03  N = 64   predits 13 / 13 /  0
    P3  w2 = 407/200   delta +0.035  x1/1  g = 1.7473e-03  N = 61   predits 13 / 13 /  0
    P4  w2 = 407/200   delta +0.035  x6/5  g = 2.0968e-03  N = 58   predits 13 / 13 /  0
    P5  w2 = 407/200   delta +0.035  x4/3  g = 2.3297e-03  N = 55   predits 13 / 13 /  0
    BN  w2 = 481/250   delta -0.076  x1/1  g = 2.4924e-03  N = 60   predits 11 /  7 /  4
    BP  w2 = 2067/1000 delta +0.067  x1/1  g = 3.7499e-03  N = 61   predits 14 /  6 /  8
  Ces comptes sont ceux des deux tables (machine 1 et machine 2, identiques). Ils portent sur des
  etiquettes predites : le jugement portera sur les etats LUS (sections 5 et 6).

4. L'INSTRUMENT : UN RUN, DEUX ETAGES
  4.1 Les pieces (convention B)
    35fa7b73f2b7f8eb table_points_gel_loi_ordre3_v1.json : la table gelee
    68baf04c73ed5d44 sonde_dense_gel_loi_machine1_v1.py : derivee de la sonde dense certifiee
                      (24315c52b234319c)
    d5cc48f48e37af99 sonde_lecteur_gel_loi_machine1_v1.py : derivee de la sonde du gel ter
                      (b5616dcf858e8801)
    83701094e6a2b965 lecture_lecteur_gel_loi_machine1_v1.py : derivee de la feuille du gel ter
                      (b2d6d7cfaf30f1cf)
    facd3ceeec07d3bf feuille_ordre3_machine1_v1.py : NOUVELLE ; elle juge les enonces
    2882de31bc49ce2f pilote_gel_loi_machine1_v1.py : NOUVEAU ; il enchaine et tient le journal
    a29225df977dfe41 table_points_prevol_gel_loi_ordre3_v1.json : un point deja joue (C3) et les
                      ancres
  Les trois scripts derives le sont par remplacements de texte, chacun trouve une seule fois dans
  sa source ; aucun script certifie n'est edite. Le script de construction et un diff unifie par
  script sont joints : la sonde dense differe de sa source par la lecture de la table et l'en-tete
  de sa sortie ; la sonde du lecteur par l'origine des points du mode "point" (la sortie dense du
  run, au canon passe) et l'en-tete ; la feuille du lecteur par la meme origine, le controle de
  forme, trois canons de plus dans le verdict, et un refus retire (section 14, E-4).
  4.2 Le deroulement du run (le pilote)
    Etage 1. La sonde dense, aux quatorze points de la table : boite, trois decompositions denses
    (k = 2, 3, 4), les 14 etats de plus grand recouvrement avec la graine coherente, leurs
    etiquettes, leur largeur deposee a k = 3. Meme code que la sonde du delta 98.
    Etage 2a. La sonde du lecteur en modes etage0, ancres, etage1 (points regles du depot :
    inchanges) ; la feuille du lecteur, etape "instrument". Si elle ne rend pas TIENT, le run
    s'arrete : rien n'est juge.
    Etage 2b. La sonde du lecteur en mode point, un appel par cellule : chaque etat dont la
    largeur deposee a k = 3 depasse dix planchers (1.33e-12) est lu sous les quatre absorbeurs, a
    douze barreaux. La feuille du lecteur, etape "verdict" : plateau sous A, accords B, C, D,
    statut de chaque etat (gel ter, section 7).
    Etage 3. La feuille d'ordre 3 : chaines a une dimension (moteur, ordre 2, ordre 3) a
    l'etiquette LUE de chaque etat ; jugement des enonces de la section 6.
  4.3 Les quatre conditions de machine 2 (lot 548fb2ba8793ecfe, section 2)
    C1. Le pilote ecrit le canon de la sortie dense dans son journal des qu'elle existe et le
    passe en argument a la sonde du lecteur, a la feuille du lecteur et a la feuille d'ordre 3,
    qui le comparent au fichier qu'elles lisent. Il fait de meme du canon du verdict du lecteur
    pour la feuille d'ordre 3. Les canons des scripts, du moteur, des blocs, du depot et de la
    table restent en dur.
    C2. Forme de la sortie dense, controlee avant toute lecture : par la sonde du lecteur (canon
    du moteur et de la sonde dense, canon de la table ; par point : w2 et facteur egaux a ceux de
    la table a l'egalite des fractions, couplage egal a facteur x g_du_point(w2) a 1e-12 pres en
    relatif, 14 etats, point faisable) ; par la feuille du lecteur (les memes, sauf le couplage :
    elle n'a pas de moteur ; et les quatorze points de la table, eux seuls) ; par la feuille
    d'ordre 3 (tout cela, et les ancres : 4.4).
    C3. Les points sont dans la table gelee, pas dans le texte des scripts.
    C4. Pre-vol sur des points deja joues : section 4.6.
  4.4 Les ancres de la sonde dense
    Ajout de machine 1. La sonde dense rejoue les deux ancres du depot. La feuille d'ordre 3 exige
    que leurs 14 etats portent les memes etiquettes que dans le depot, que leur largeur deposee a
    k = 3 s'en ecarte d'au plus 1e-3 en relatif plus 1e-12, et leur energie d'au plus 1e-9. Sinon
    l'instrument ne tient pas et rien n'est juge. C'est un controle de reproduction de la sonde
    dense sur la machine du run, pas un controle de justesse (L-10).
  4.5 Les deux feuilles et leurs bancs
    Feuille du lecteur derivee : son selftest tient (68 cas sur 68) ; le banc certifie de la
    feuille du gel ter (6b63a9de25107ae4), joue sur la feuille derivee, mord a 43 alterations sur
    43.
    Feuille d'ordre 3 : jouee sur les douze points juges du delta 98 (depot, et verdict du run du
    gel ter), elle retrouve les 131 etats de la note sur la loi, les memes, dont 56 dans le
    domaine. Son banc (ea750a31036b0058) part de trois points deja joues et change UNE chose a la
    fois, avec l'effet attendu ecrit avant : 17 mutations, 17 mordent comme attendu. Elles
    couvrent : une largeur de plateau, toutes les largeurs d'un point, un statut, l'instrument,
    une etiquette, le couplage, le nombre d'etats, le facteur de la table, la bande de l'ordre 2,
    le J, un canon, la cellule inexploitable, l'etiquette double, une ancre, la part des etats
    juges, une ancre retiree, la table hors pre-vol.
  4.6 Le pre-vol de machine 1 (condition C4)
    Sur la machine de machine 1, le pilote a joue le chemin derive en mode --prevol sur la table
    de pre-vol (le point C3 du delta 98, deja joue, et les ancres), la sortie du depot tenant lieu
    de sortie dense. Cinq controles (comparaison_prevol_machine1_v1.py), tous tenus :
      P1 mesures des etages 0, ancres et 1 contre la sonde certifiee sur la meme machine (en-tete
          et durees mis a part) : etage0 identique, ancres identique, etage1 identique
      P2 point C3 : 14 etats, memes etiquettes : oui, memes suivis : oui ; 672 lectures suivies,
          pire ecart relatif 4.4e-16 (tolerance 1e-6)
      P3 verdict du lecteur a C3 : 14 etats, memes statuts : oui (QUALIFIES : 14) ; pire |ln|
          entre largeurs de plateau A : 3.6e-15
      P4 feuille d'ordre 3 a C3 : lus 14, juges 14, domaine 14, hors 0, E1 TIENT, E3 TIENT ;
          identiques a la feuille retrospective : oui ; pire ecart sur ln q3 : 3.7e-15
      P5 sonde dense derivee a C3 : boite 55 (depot 55), ecart relatif de couplage 0e+00, 14
          etiquettes identiques : oui ; pire ecart relatif de Gamma_2D(3) au-dessus de dix
          planchers 7.3e-04 ; pire ecart d'energie 3.0e-13 ; hors tolerance : 0 ; duree 138.8 s
    Durees sur le conteneur de machine 1 (deux coeurs) : etage0 19 s, ancres 675 s, etage1 724 s,
    point C3 1639 s, feuille d'ordre 3 3 s ; total 2386 s. La sonde dense derivee a C3 : 139 s.
    Ecart declare (E-7) : ce pre-vol a ete LANCE avant la derniere retouche de la feuille d'ordre
    3 (le niveau TENU SAUF UNE CELLULE de E2 et quatre lignes d'en-tete). Le journal du pilote
    porte donc les canons d'avant, de la feuille (582d17c67f460ff6) et du pilote
    (06094b61135f56fb) ; l'etage 3 du pre-vol, lui, a joue la feuille finale (facd3ceeec07d3bf),
    deja en place quand il a ete atteint. Les deux pieces telles qu'au lancement sont jointes,
    reconstruites : elles rendent les deux canons du journal ; le diff de la retouche est joint.
    Le pilote final ne differe de celui du pre-vol que par le canon de la feuille qu'il porte.
    Machine 2 refait le pre-vol avec les pieces finales (section 11).
    Ce que le pre-vol de machine 1 ne dit pas : "les memes octets que le lecteur certifie" au
    point (C4, a la lettre) ne se verifie que sur la machine du run certifie ; machine 1 ne peut
    comparer qu'a 1e-6 pres. C'est a machine 2 de le faire sur BOCAL4, avec le meme script de
    comparaison.
  4.7 Le chemin sans --prevol, essaye a blanc hors des cellules
    Le run se joue SANS --prevol. Ses branches propres (table du gel, controles de provenance,
    creneaux N, P, BN, BP) ne peuvent pas etre jouees pour de vrai avant le feu vert : ce serait
    calculer en 2D aux cellules. Machine 1 les a fait tourner sans aucune mesure 2D a une cellule
    (essai_a_blanc_hors_cellules_machine1_v1.py), sur les pieces aux canons de 4.1. Six essais,
    tous tenus :
      S1 sonde dense, table du gel, sans --prevol, ancre A1 seule : code 0 ; prevol False ; canon
          de la table du gel porte ; 14 etats ; hors tolerance des ancres contre le depot : 0 ;
          duree 240.5 s
      S2 sonde dense : table du gel avec --prevol refusee (code 1) ; table de pre-vol sans
          --prevol refusee (code 1) ; rien n'est ecrit
      S3 sonde du lecteur, table du gel, sans --prevol, mode etage0 (ancres) : code 0 ; mesures
          identiques a celles du pre-vol : oui
      S4 sonde du lecteur, mode point N1, sans --prevol : arret au controle de forme (point
          infaisable) apres les controles de provenance ; sortie dense sans canon de table refusee
          ; canon passe faux refuse ; aucune mesure, aucun fichier
      S5 feuille du lecteur, etape verdict, sans --prevol, fichiers fabriques : code 0 ; les douze
          points lus ; le verdict porte les canons de la table, de la sortie dense et de la
          feuille : oui
      S6 feuille d'ordre 3, sans --prevol, fichiers fabriques : code 0 ; douze cellules ; ancres
          tenues ; une issue rendue pour E1 (10 cellules), E2 (5), E1B (2), E3 (12) : oui (issues
          non affichees : elles n'ont aucun sens)
    Les fichiers dits fabriques recopient des mesures de points DEJA JOUES (depot du delta 98, run
    du gel ter) sous les identifiants, w2, facteurs et couplages des cellules, avec les en-tetes
    que les scripts attendent. Ils ne disent rien des cellules ; les issues que la feuille en tire
    n'ont aucun sens, ne sont pas affichees, et les fichiers sont effaces. Les seules chaines
    calculees aux cellules y sont a une dimension. Le pilote, lui, n'a ete joue qu'avec --prevol.

5. ETATS JUGES, DOMAINE, CELLULE EXPLOITABLE
  ETAT LU : un des 14 etats de la sonde dense que le lecteur a lus (largeur deposee a k = 3
  au-dessus de dix planchers).
  ETAT JUGE : un etat lu qui est, dans cet ordre, QUALIFIE par la feuille du lecteur ; d'etiquette
  nette (ecart-type de J < 0.2) ; d'etiquette unique parmi les 14 etats du point ; de barriere non
  vide ; de chaine du moteur stable et de chaine d'ordre 2 stable (quatre eta de chaine, toutes
  les largeurs positives, plus grande / plus petite <= 2). Un etat exclu l'est avec son premier
  motif, publie.
  DANS LE DOMAINE : un etat juge tel que e_bord < 0.7 et que la stabilite de sa chaine d'ordre 3
  soit definie et <= 0.05 (premiere partie, 4.3 et 4.4). HORS DU DOMAINE : un etat juge qui n'est
  pas dans le domaine.
  Grandeurs : G2 et G3 sont les largeurs des chaines d'ordre 2 et d'ordre 3 au facteur d'eta 1/16
  ; Gamma_pl est la largeur de plateau sous l'absorbeur A ; q2 = G2 / Gamma_pl, q3 = G3 /
  Gamma_pl.
  CELLULE EXPLOITABLE. Il faut d'abord qu'au moins les deux tiers de ses etats lus soient juges.
  Puis : pour une cellule de ligne (N1 a N5, P1 a P5), au moins 5 etats juges dans le domaine ;
  pour une cellule de bord (BN, BP), au moins 2 dans le domaine et au moins 2 hors du domaine. Une
  cellule INEXPLOITABLE n'entre ni dans E1, ni dans E2, ni dans E1B ; elle reste jugee par E3 ;
  ses nombres sont publies.

6. LES ENONCES ET LEURS ISSUES (la cellule est l'unite)
  E1, cellules de ligne. Une cellule exploitable TIENT si chacun de ses etats juges du domaine a
  |ln q3| <= T, avec T = 0.05 si e_bord < 0.3 et T = 0.10 sinon ; elle TOMBE sinon. Un seul etat
  hors tolerance fait tomber la cellule.
  E2, cellules de la ligne N. Une cellule exploitable TIENT si |ln q3| < |ln q2| pour au moins les
  trois quarts (arrondis par exces) de ses etats juges du domaine ; elle TOMBE sinon.
  E1B, cellules de bord. Comme E1, sur les etats juges du domaine de BN et de BP.
  E3, les douze cellules. Une cellule TIENT si chacun de ses etats juges, dans le domaine ou non,
  a 1/B <= q2 <= B, B etant la borne du delta 98 : 1.25 pour |delta| <= 0.06, 1.6 jusqu'a 0.10.
  Les lignes N et les deux bords sont a B = 1.6 ; la ligne P a B = 1.25. Une cellule sans etat
  juge est VIDE et ne tombe pas.
  ISSUES. Les chutes d'abord, ce sont des faits ; les cellules inexploitables ensuite.
    E1 (dix cellules) : TOMBE si deux cellules exploitables ou plus tombent ; sinon NON CONCLUANT
    si plus de deux cellules sont inexploitables ; sinon TENU si aucune ne tombe, TENU SAUF UNE
    CELLULE si une seule tombe.
    E2 (cinq cellules) : de meme, NON CONCLUANT si plus d'une cellule est inexploitable.
    E1B (deux cellules) : TOMBE si une cellule exploitable tombe ; sinon NON CONCLUANT si l'une
    est inexploitable ; sinon TENU.
    E3 (douze cellules) : TOMBE si une cellule tombe ; sinon TENU.
  La ligne P ne juge pas l'ordre 3 contre l'ordre 2 : aux etiquettes predites de ses cinq
  cellules, |ln(G3 / G2)| vaut de 0.014 a 0.019, du niveau de la stabilite de la chaine. E1 y
  eprouve "la chaine marche a des points neufs", pas l'ordre 3. Seule la ligne N, par E2, oppose
  les deux ordres (|ln(G3 / G2)| de 0.066 a 0.164 a ses etiquettes predites).
  Ce qui est consigne sans etre juge : pour les etats hors du domaine, si l'ordre 3 est plus loin
  que l'ordre 2 ; le signe de ln q3 ; le statut que la feuille du lecteur donne a chaque point.

7. LES TOLERANCES, ET CE QUE LA PLUME A VU AVANT DE LES ECRIRE
  Aucune largeur 2D n'existe aux douze cellules, pas meme la largeur deposee a k = 3 : dans le run
  unique elle nait a l'etage 1. Les tolerances ne peuvent donc venir que de deux sources, et la
  plume a regarde les deux.
  7.1 Les points deja joues
    Les 56 etats du domaine des douze points du delta 98 (feuille d'ordre 3 retrospective), par
    classe de e_bord : nombre, mediane et plus grand |ln q3| :
      e_bord dans [0.0, 0.3[   27 etats   mediane 0.0083   plus grand 0.0374
      e_bord dans [0.3, 0.5[   16 etats   mediane 0.0277   plus grand 0.0415
      e_bord dans [0.5, 0.7[   13 etats   mediane 0.0385   plus grand 0.0604
    D'ou T = 0.05 sous e_bord = 0.3 (plus grand vu : 0.0374) et T = 0.10 au-dela (plus grand vu :
    0.0604). L'ordre 3 est plus pres que l'ordre 2 a 56 de ces 56 etats. La tolerance ne descend
    nulle part sous la stabilite de la chaine, qui vaut au plus 0.05 dans le domaine par
    definition.
    Ces deux valeurs ont ete ecrites dans la feuille AVANT que la plume calcule les marges de 7.3
    ; elles n'ont pas ete retouchees ensuite. C'est une declaration de la plume : machine 2 ne
    peut pas la verifier.
    Les deux ancres, deja jouees et absentes des 131 etats (leurs deux etats lus, plateau de la
    reference de machine 1) : a A1 (delta = -0.05), ln q3 = -0.0122 et -0.0065 ; a A2 (delta =
    +0.05), ln q3 = +0.0374 et +0.0373.
  7.2 Deux regularites lues aux points deja joues (etats du domaine)
    A delta < 0 (39 etats : A1, C1, C2, M1, M2), ln q3 est negatif a 35 etats sur 39 : l'ordre 3
    corrige trop. Aux 31 etats ou la correction d'ordre 3 se lit (|ln(G3 / G2)| >= 0.05), k = -ln
    q3 / (ln(G3 / G2))^2 vaut de 0.55 a 3.24, mediane 1.99.
    A delta > 0 (21 etats : A2, C3, C4), ln q3 est positif partout ; ln q3 / delta^2 vaut au plus
    15.0 (mediane 10.2), ln q3 / delta^3 au plus 493 (mediane 192). Trois points ne separent pas
    ces deux puissances.
  7.3 Les chaines aux douze cellules (etiquettes predites), et les marges
    Par cellule : nombre d'etats predits du domaine ; ceux a T = 0.05 ; e_bord extremes ; ln(G3 /
    G2) median ; puis l'attente du pire |ln q3| par les regularites de 7.2 prises a leur valeur la
    plus defavorable (k = 3.24 a delta < 0 ; la puissance 3 et son plus grand coefficient a delta
    > 0), et la marge, T / attente.
    N1  domaine 11 ( 0 a 0.05)  e_bord 0.442 a 0.626  ln(G3/G2) -0.1524  attente 0.0866  marge 1.15
    N2  domaine 10 ( 0 a 0.05)  e_bord 0.441 a 0.565  ln(G3/G2) -0.1311  attente 0.0620  marge 1.61
    N3  domaine 12 ( 0 a 0.05)  e_bord 0.317 a 0.562  ln(G3/G2) -0.1056  attente 0.0406  marge 2.46
    N4  domaine 13 ( 1 a 0.05)  e_bord 0.191 a 0.501  ln(G3/G2) -0.0840  attente 0.0254  marge 2.78
    N5  domaine 14 ( 2 a 0.05)  e_bord 0.191 a 0.500  ln(G3/G2) -0.0731  attente 0.0194  marge 3.46
    P1  domaine 12 ( 5 a 0.05)  e_bord 0.250 a 0.396  ln(G3/G2) -0.0155  attente 0.0211  marge 2.37
    P2  domaine 13 ( 6 a 0.05)  e_bord 0.214 a 0.359  ln(G3/G2) -0.0165  attente 0.0211  marge 2.37
    P3  domaine 13 ( 8 a 0.05)  e_bord 0.142 a 0.324  ln(G3/G2) -0.0175  attente 0.0211  marge 2.37
    P4  domaine 13 (13 a 0.05)  e_bord 0.142 a 0.287  ln(G3/G2) -0.0178  attente 0.0211  marge 2.37
    P5  domaine 13 (13 a 0.05)  e_bord 0.142 a 0.288  ln(G3/G2) -0.0174  attente 0.0211  marge 2.37
    BN  domaine  7 ( 0 a 0.05)  e_bord 0.369 a 0.583  ln(G3/G2) -0.1411  attente 0.0734  marge 1.36
    BP  domaine  6 ( 0 a 0.05)  e_bord 0.347 a 0.636  ln(G3/G2) -0.0355  attente 0.1481  marge 0.68
    Lecture. La cellule N1 est le point dur : sa correction d'ordre 3 est la plus grande que la
    chaine ait faite dans le domaine (0.152 en mediane, contre 0.127 au plus aux points joues), et
    sa marge est de 1.15. Sous la valeur la plus defavorable de k, l'ordre 2 y serait plus pres
    que l'ordre 3 a 4 etats sur 11 : E2 y tomberait. La cellule BP est sous la tolerance par une
    regularite (0.0672, puissance 2) et au-dessus par l'autre (0.1481, puissance 3). Les neuf
    autres cellules de ligne ont une marge d'au moins 1.61.
    Ce que la plume n'a pas vu : aux points joues, aucun etat du domaine n'a e_bord au-dessus de
    0.603. Aux douze cellules, 5 etats predits du domaine sont au-dela (3 a N1, 2 a BP) : la garde
    e_bord < 0.7 y est eprouvee pour la premiere fois.
    La plume n'a PAS desserre la tolerance au vu de ces marges. Elle a en revanche donne a E2 le
    niveau TENU SAUF UNE CELLULE apres les avoir vues (section 14, E-2).

8. CE QUE CHAQUE ISSUE ENGAGE
  L'INSTRUMENT NE TIENT PAS (feuille du lecteur, ou ancres de la sonde dense) : rien n'est juge ;
  l'acte le dit ; aucun rejeu sous d'autres reglages ; une suite demande un autre gel.
  E1 TENU et E2 TENU. L'acte peut ecrire : "a douze cellules tirees au sort, la chaine d'ordre 3
  rend la largeur de plateau des etats juges du domaine a 0.05 pres en logarithme (e_bord < 0.3)
  et a 0.10 pres au-dela, et elle est plus pres que l'ordre 2 sur la ligne negative". Il ne peut
  pas ecrire une loi en delta : un seul w2 par ligne. Le bloc d'ordre 3 peut alors etre propose au
  depot.
  E1 TENU SAUF UNE CELLULE, ou E2 TENU SAUF UNE CELLULE. La meme phrase, la cellule nommee. L'acte
  dit que la garde du domaine ne suffit pas a cette cellule. Il ne redessine pas le domaine :
  aucune garde, aucun seuil n'est regle apres lecture ; un domaine plus etroit demande un autre
  gel et d'autres points.
  E1 TOMBE. L'acte ecrit que la chaine d'ordre 3 ne rend pas la largeur a cette tolerance dans le
  domaine declare. La lecture de la note sur la loi (56 etats du domaine, plus grand |ln q3| :
  0.0604) est alors declaree lue en echantillon, non confirmee hors echantillon. Le bloc d'ordre 3
  n'est pas propose au depot.
  E2 TOMBE. L'acte ecrit qu'a des points neufs l'ordre 3 n'est pas plus pres que l'ordre 2 sur la
  ligne negative. L'ordre 3 n'est pas propose comme correction de l'ordre 2.
  E3 TOMBE. Les bornes du delta 98 ne tiennent pas a des points neufs : l'acte le dit, cellule et
  etat nommes, et dit que l'acte du delta 98 est borne a ses douze points.
  E1B. TENU : les deux fenetres de bord sont dans le domaine au facteur 1, a ces deux w2. TOMBE :
  le bord du domaine est plus pres que la garde ne le dit, du cote nomme. Dans les deux cas c'est
  une observation du bord ; elle ne change pas l'issue de E1.
  NON CONCLUANT : l'acte le dit et donne les comptes ; pas de rejeu, pas de nouveau seuil.
  Dans tous les cas : la table par etat est publiee (etiquette, e_bord, stabilite, G2, G3,
  Gamma_pl, q2, q3, statut), les etats exclus avec leur motif. Aucune autre definition du
  hamiltonien effectif, aucun autre absorbeur de chaine, aucune autre tolerance n'est essayee
  apres lecture.

9. GARDES (chaque journal dit ce qu'il ne joue pas)
  G-1 canons en dur : moteur, blocs d'ordre 2 et 3, depot, couplages et references du temoin et
      des ancres, table, les quatre scripts ; un ecart arrete.
  G-2 la sortie dense et le verdict du lecteur sont lus au canon que le pilote vient d'ecrire dans
      son journal (C1).
  G-3 forme de la sortie dense (C2) ; provenance : sortie dense et verdict portent le canon de la
      table et des scripts qui les ont ecrits.
  G-4 ancres de la sonde dense contre le depot (4.4).
  G-5 instrument du lecteur : etage 0, ancres, etage 1, tels qu'au gel ter (sections 5 et 6 de ce
      gel-la), tolerances inchangees.
  G-6 pre-vol : un script lance avec --prevol refuse la table du gel ; sans --prevol il refuse
      toute autre table ; une sortie de pre-vol ne juge rien.
  G-7 une seule execution : le pilote exige un dossier neuf et joue chaque appel une fois ; un
      code de sortie non nul l'arrete.

10. ANNONCES DE LA PLUME (ecrites apres les calculs de la section 7 ; aucune 2D aux cellules)
  Ce sont des jugements, pas des calculs : huit points deja joues ne font pas une loi d'erreur.
  Probabilites :
  A-1 (0.90) l'instrument tient (feuille du lecteur et ancres de la sonde dense).
  A-2 E1 : TENU 0.35 ; TENU SAUF UNE CELLULE 0.40 ; TOMBE 0.10 ; NON CONCLUANT 0.05 ; le reste
      (0.10) est l'instrument.
  A-3 la cellule qui tombe le plus probablement sous E1 est N1 : 0.45 qu'elle tombe, si elle est
      exploitable.
  A-4 E2 : TENU 0.50 ; TENU SAUF UNE CELLULE 0.30 (N1) ; TOMBE 0.05 ; NON CONCLUANT 0.05 ; le
      reste (0.10) est l'instrument.
  A-5 E3 TENU : 0.85.
  A-6 E1B : BN tient 0.65 ; BP tient 0.40.
  A-7 (0.80) a la ligne N, ln q3 est negatif pour au moins trois quarts des etats juges du domaine
      ; a la ligne P, positif pour au moins trois quarts.
  La plume annonce donc que l'issue la plus probable n'est PAS un E1 tenu partout. Elle le gele
  ainsi.

11. DEROULEMENT, E19, ET CE QUI EST PERMIS
  ORDRE. (1) Machine 2 certifie cette piece, la table, les scripts derives et leurs diffs, la
  feuille d'ordre 3 et son banc, le pilote ; un seul tour de correction. (2) Feu vert ecrit de
  l'operateur. (3) Machine 2 joue le pilote UNE fois, dans un dossier neuf. (4) Lot de resultat :
  la sortie dense, les fichiers du lecteur, les deux verdicts du lecteur, le verdict d'ordre 3,
  les journaux, le journal du pilote. (5) Machine 1 authentifie et rejoue les feuilles. (6) Acte.
  PRE-VOL. Avant le feu vert, machine 2 peut jouer le pilote avec --prevol sur la table de
  pre-vol, avec ou sans --dense : ce sont des points deja joues. Avec --dense et le depot, le mode
  point doit lui rendre les mesures du fichier de C3 de son run du gel ter.
  UNE SEULE EXECUTION. Un pilote arrete par une panne se relance ENTIER dans un dossier neuf, et
  l'acte le dit ; aucun appel n'est rejoue apres lecture de sa sortie.
  DEUX MACHINES. Le verdict est celui de la feuille d'ordre 3 jouee par machine 2 dans le run.
  Machine 1 la rejoue sur les fichiers du lot. Les chaines different d'une machine a l'autre :
  2.2e-05 en relatif au plus aux deux etats d'ancre (mesure de machine 1 au gel du delta 98). Un
  etat au ras d'une garde peut donc changer de cote. Si le verdict d'une cellule differe entre les
  deux machines, la lecture la MOINS favorable a l'enonce est retenue, et l'acte donne les deux.
  E19. Aucune des deux machines ne calcule en 2D a l'une des douze cellules avant le feu vert ;
  machine 1 n'y calcule rien en 2D avant d'avoir recu et authentifie le lot de resultat.
  Ce gel ne se rejoue pas sous d'autres seuils, d'autres gardes, une autre chaine ou d'autres
  points apres lecture.

12. COUTS (a mesurer au pre-vol de machine 2, pas a promettre)
  Etage 1 : de l'ordre de 2400 s sur BOCAL4, par interpolation des durees du depot selon la boite
  (boites de 55 a 69, plus les deux ancres). Etages 2a et 2b : le run du gel ter a coute 4377 s
  pour 137 etats ; les tables predisent 149 etats au-dessus de dix planchers aux douze cellules.
  Etage 3 : de l'ordre de la minute.

13. LIMITES DECLAREES
  L-1 L'objet juge est UNE chaine : le bloc 534ba246aa3b8973, forme symetrique (hermitienne).
      Essai fait, sur les chaines seules (definition_bloch_machine1_v1.py) : la forme de Bloch,
      tronquee au meme ordre et mise sous le meme absorbeur. Les deux formes s'accordent comme il
      se doit a petit couplage (l'ecart d'energie varie en g^4.01, attendu 4), mais aux couplages
      du gel la forme de Bloch n'est pas une chaine utilisable : a l'etat eprouve, ses deux
      moities du saut valent 9.1 et 11.1 fois la correction symetrique au dernier site de la
      barriere et depassent le saut lui-meme a partir du site 22 ; sa largeur varie d'un facteur
      5.0 avec la force de l'absorbeur (la forme symetrique : 1.027). Aux 56 etats du domaine des
      points joues, |ln(G_Bloch / G_sym)| vaut 0.33 en mediane et jusqu'a 3.8 ; la forme de Bloch
      n'est plus pres du plateau qu'a 7 etats. Cet essai ne chiffre donc PAS une dependance a la
      definition : il dit que la troncature n'a de largeur stable que sous sa forme hermitienne.
      Aucune autre forme hermitienne n'a ete essayee.
  L-2 La reference est le lecteur du gel ter, dont l'acte est contresigne et non depose.
  L-3 Seuls des etats QUALIFIES et d'etiquette nette sont juges. Un etat que le lecteur ne
      qualifie pas ou dont l'etiquette est floue peut etre un etat ou la chaine echoue : la garde
      des deux tiers borne cet effet sans l'annuler.
  L-4 L'eligibilite portait sur des etiquettes predites, justes a 189 sur 224 aux points joues
      (note de la carte) : une cellule peut sortir inexploitable.
  L-5 Etats au-dela du plus grand e_bord vu : 7.3.
  L-6 La ligne P ne discrimine pas les deux ordres : section 6.
  L-7 Les tolerances ne sortent pas d'une theorie de l'erreur : elles sont lues sur 60 etats de
      huit points deja joues, et ne dependent de la chaine que par e_bord.
  L-8 Un w2 par ligne : rien n'est dit de la dependance en delta entre les lignes et les bords.
  L-9 Etats au ras d'une garde : section 11, DEUX MACHINES.
  L-10 Les ancres de la sonde dense eprouvent sa reproduction, pas sa justesse.
  L-11 E3 applique la borne du delta 98 a la largeur de plateau, sans la marge d'un plancher que
      ce gel-la donnait a la lecture dense.
  L-12 La stabilite est une convention : celle de l'absorbeur de la chaine et du bloc d'ordre 2
      depose (premiere partie).

14. ECARTS DECLARES
  E-1 La note de la carte donnait a E3 deux volets : hors du domaine, l'ordre 2 reste dans les
      bandes du delta 98, et l'ordre 3 est declare non applicable. Ici E3 porte sur tous les etats
      juges, dans le domaine ou non, et le second volet n'est pas un enonce : il est consigne. La
      superposition des deux lignes en Gamma / |delta| a facteur egal, que la note voulait
      observer, n'est pas calculee par la feuille : elle se lira dans la table par etat. Aux
      points joues l'ordre 3 est plus pres que l'ordre 2 aux 83 etats juges de e_bord < 0.7, dont
      les 27 que la stabilite exclut du domaine.
  E-2 Machine 2 demandait ce qu'engage "E2 faux". La plume a donne a E2 les memes niveaux qu'a E1,
      dont TENU SAUF UNE CELLULE, APRES avoir vu sur les chaines que N1 est a la limite. C'est un
      adoucissement fait en connaissance des marges ; machine 2 peut le refuser : c'est une
      constante de la feuille.
  E-3 C2 demandait l'egalite de (w2, g) a la table. La table porte w2 et le facteur ; le couplage
      est compare a facteur x g_du_point(w2) a 1e-12 pres, par les scripts qui chargent le moteur.
  E-4 La feuille du gel ter refusait de lire un point dont l'etat de rang 0 n'etait pas lu. La
      feuille derivee ne refuse plus : un seul tel point aurait arrete toute la lecture, et ce gel
      ne se sert pas du statut du point.
  E-5 La garde des deux tiers (section 5) et les ancres de la sonde dense (4.4) sont des ajouts de
      machine 1.
  E-6 La premiere partie annoncait des tolerances "calculees sur les chaines aux douze cellules".
      Elles sont lues aux points deja joues ; ce qui est calcule aux douze cellules, ce sont les
      classes de e_bord, les attentes et les marges.
  E-7 Le journal du pre-vol porte un canon anterieur de la feuille d'ordre 3 : 4.6.
  E-8 La plume avait dit a l'operateur qu'elle chiffrerait la dependance a la definition du
      hamiltonien effectif en ecrivant ce gel. Elle a essaye une autre definition ; l'essai ne
      rend pas un chiffre de dependance (L-1).

15. CE QUE MACHINE 2 CERTIFIE
  (a) que la table gelee porte les douze cellules de SON tirage et les deux ancres ;
  (b) que chaque script derive ne differe de sa source certifiee que par les remplacements du
      script de construction ;
  (c) que la feuille d'ordre 3 applique les sections 5 et 6, et que son banc mord ;
  (d) que les nombres des sections 3 et 7 sortent des pieces ;
  (e) le pre-vol sur BOCAL4, avec les pieces finales ;
  (f) qu'elle accepte, ou refuse, les ecarts de la section 14.

-- FIN gel_loi_ordre3_partie2_instrument_enonces_pre_enregistrement_v1 --
