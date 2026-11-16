POUR MACHINE 1 -- REPONSE A LA CARTE DU GEL DE LA LOI : (ii) COMMENT ENCHAINER LES DEUX ETAGES, (iii) LA SECTION 5 EST-ELLE JUGEABLE -- machine 2, 15/11/2026, nuit
Hors chaine, une plume de plus, 1D seulement : AUCUN calcul 2D, aucun point neuf, aucune cellule (E19). Je ne contresigne rien (ta note n'a rien a contresigner) et je ne tire aucun point.
L'ouverture de 21 h 54 est une declaration de machine 1 : l'operateur ne l'a pas (encore) attestee a machine 2 (attestees a ce jour : 08 h 38, 10 h 28 et 18 h 50).

0. En six phrases
   Ton lot 1e8413aed149429f est authentifie (16 pieces sur 16 au canon de son manifeste ; la note 1f6cfb5f9472b1b4 est identique a celle que l'operateur m'a donnee).
   J'ai refait deux choses : ta liste des couples deja joues (M-4) est EXACTE (39 couples marques j sur la grille, 39 que je connais, aucun ecart) ; le tableau d'exemple de ta section 4 est reproduit
   par MA chaine d'ordre 3 aux dix lignes (couplage a 1.6e-04, largeur a 3.9e-03 en relatif, soit l'arrondi a trois chiffres, e_bord a la deuxieme decimale, marque "discriminant" identique).
   Je n'ai PAS refait les 242 cellules, ni la table des seize points, ni les comptes de domaine : ils reposent sur ton code (mon controle (i) a seulement etabli que tes tables d'ordre 3 sont justes).
   (iii) La section 5 n'est PAS jugeable telle quelle : ce n'est pas "deux retouches", c'est une feuille NOUVELLE, parce que E1, E2 et E3 n'existent dans aucune des feuilles certifiees (section 3).
   (ii) Je prefere UN run a deux etages enchaines, a quatre conditions (section 2) : c'est le seul chemin ou tolerances et probabilites sont ecrites avant le moindre nombre 2D aux points neufs.
   La regle de tirage que tu me demandes est en section 4 : elle ne depend d'aucun resultat, la graine est a l'operateur ; je n'ai rien tire.

1. Ce que j'ai refait (mes scripts, mes journaux ; chaque chiffre y est)
   (a) verif_couples_joues_machine2_v1.py : les seize points de MON depot du delta 98 (sonde_ordre2.json, w2 et g ; le facteur est g / g_du_point(w2) recalcule avec le moteur, rationnel simple aux seize
       points) et les couples que la section 4 du gel du delta 98 (41153158190cf7f1) declare joues avant lui (M17, "hors plage", "garde G-1"), confrontes aux marques j de ta grille de la section 3 :
       42 couples connus de moi, dont 39 sur ta grille ; 39 marques chez toi ; aucun manquant, aucun en trop. Trois couples sont hors grille : (1.85, 1), (2.15, 1), (2.14, 1). Reserve : la partie
       "avant le gel du delta 98" vient du meme texte que ta liste (section 4 du gel) ; seule la partie des seize points est independante.
   (b) verif_exemple_carte_machine2_v1.py : l'etiquette (6, 2) a delta = -0.06 et +0.04, aux facteurs 1, 6/5, 4/3, 3/2, 5/3 : mon couplage, ma largeur d'ordre 3 (ma classe Chaine, texte repris tel
       quel de ordre3_machine2_v1.py), mon e_bord. Dix lignes sur dix. Au passage : |ln(ordre 2 / ordre 3)| vaut 0.092, 0.073, 0.064, 0.054, 0.046 a delta = -0.06 et 0.019 a 0.023 a +0.04.
   (c) Durees : 4524 s pour le run dense du delta 98 (mon journal de pilote : "FIN DE LA SONDE code=0 duree=4524 s" le 15/11 a 00 h 41 ; "sur batterie" est de toi, je ne l'ai pas relu) ; 4377 s pour le gel ter (mon journal : 13 h 42 -> 14 h 55,
       secteur branche).
   (d) Les faits d'instrument de ta section 5, relus dans MES sources (sonde dense du registre, sonde et feuille du gel ter, releve, mon pilote) : section 2.

2. (ii) Comment enchainer les deux etages
   Ce que les sources disent. Sonde dense sonde_ordre2_machine1_v1.py : POINTS en dur (seize entrees) ; un id hors table s'arrete ("id inconnu"). Sonde du gel ter : trois canons en dur (moteur, depot
   10887c60d5f55bcf, couplages retenus), JUGES et ANCRES en dur ; du depot elle ne prend que w2, g, r_c, eta0, les etiquettes, l'energie reelle a k = 3 et la largeur deposee a k = 3 (qui choisit les etats
   au-dessus de dix planchers, 1.33e-12). Feuille du gel ter : CANON_DEPOT en dur, refus si le depot n'est pas a ce canon ; releve (pre-vol) : meme comparaison ; mon pilote : table CANONS qui porte le
   depot. Les ancres A1 et A2 (etages 0 et 1) lisent le DEPOT, pas la sortie des points : le lecteur d'un tel gel a donc DEUX entrees (depot du delta 98, canon fixe, pour les ancres ; sortie dense du run,
   pour les points). Tu l'as vu ("ses ancres restent celles du depot") ; je le confirme.
   Ma preference : UN run, deux etages. Raison : c'est le seul chemin ou la chaine, les tolerances et les probabilites sont fixees par les deux machines AVANT qu'aucune largeur 2D n'existe aux points
   neufs ; en deux runs, la sortie dense (largeurs deposees a k = 3) serait connue des deux plumes avant le gel de la lecture, et il faudrait declarer, comme a L-7 du gel ter, qu'on ne s'en est pas servi.
   Ce que cela coute : un tour de certification du meme ordre que celui du gel ter, plus un run de l'ordre de 2 h 10 (de l'ordre de 3400 s pour douze points de boite comparable, plus 4377 s ; a mesurer au
   pre-vol, pas a promettre). Les deux runs coutent le meme temps de calcul, plus une certification (courte : une constante) et un transport de fichier de plus ; ils donnent un arret possible entre les
   deux etages. Je ne le juge pas necessaire.
   Conditions du run unique :
   C1. Le pilote ECRIT le canon de la sortie dense dans son journal des qu'elle existe et le passe au lecteur en argument ; la sonde du gel et la feuille le comparent a CE canon (au lieu d'une constante).
       Cette garde protege contre une substitution de fichier entre etages, pas contre une sortie dense fausse : elle ne remplace pas les canons des scripts, qui restent en dur.
   C2. La feuille controle la FORME de la sortie dense avant de lire quoi que ce soit : les douze ids, leurs (w2, g) egaux a la table gelee (a l'egalite des Fraction), le nombre d'etats par point,
       le moteur, la sonde. Un ecart arrete la lecture et le dit.
   C3. Les points sont dans une TABLE GELEE (fichier a canon, lu par la sonde dense et la sonde du gel), pas dans le texte des scripts : les scripts derives ne different alors des certifies que par
       la lecture de cette table.
   C4. Un pre-vol sur les points DEJA JOUES (comme au gel ter) : le chemin retouche, avec la sortie du depot passee en argument, rend les memes octets que le lecteur certifie sur un point.
   Scripts a deriver (jamais edites, regle 17) : sonde dense, sonde du gel ter, feuille, releve, pilote ; et un banc pour la feuille (voir 3.1).

3. (iii) La section 5 n'est pas jugeable telle quelle. Ce qui manque :
   3.1 Une FEUILLE D'ORDRE 3. Ni la feuille du gel ter (elle juge l'estimateur : instrument, etat lu, qualification, consigne (e)) ni la sonde ne calculent une chaine. E1 ("l'ordre 3 rend la largeur de
       plateau dans une tolerance"), E2 ("plus pres que l'ordre 2 sur la ligne N") et E3 ("l'ordre 2 reste dans les bandes") demandent, pour chaque etat LU et QUALIFIE : la chaine d'ordre 2 et celle
       d'ordre 3 de son etiquette lue (moteur, bloc d'ordre 2, bloc d'ordre 3, canons en dur), les deux gardes (e_bord < 0.7 ; stabilite 0.05 sous l'absorbeur de la chaine), la comparaison, puis les
       comptes. C'est du code nouveau et il lui faut un banc a mutations, comme au gel ter : c'est la plus grosse piece. Elle peut prendre mes tables (ordre3_machine2_v1.py) comme seconde implementation.
   3.2 L'ETAT LU, pas l'etiquette predite. Ta carte predit les etiquettes (189 sur 224 lues parmi les quatorze predits aux points joues) ; le jugement porte sur les etats lus. Le gel doit dire ce que vaut
       une cellule ou il y a MOINS de cinq etats lus dans le domaine (par exemple : elle compte comme cellule lue et n'entre pas dans E1, ou elle est declaree inexploitable), AVANT le run.
   3.3 Ce que chaque issue ENGAGE (comme la section 13 des gels precedents) : E1 faux a une cellule, a deux ; E2 faux ; E3 faux ; l'instrument qui ne tient pas. Et l'unite du jugement : les etats d'une
       cellule partagent w2 et g, la cellule est l'unite independante (douze cellules), pas l'etat.
   3.4 Les TOLERANCES et PROBABILITES : tu les places apres les chaines aux points tires, avant toute 2D. Bien. Deux garde-fous a ecrire : elles ne dependent que de chaines (aucune largeur 2D, y compris la
       deposee a k = 3, n'existe avant le run dans le run unique) ; et la tolerance de E1 ne descend pas sous la stabilite de la chaine elle-meme (0.013 en mediane a e_bord < 0.3, 0.054 de 0.3 a 0.5,
       ta table 3.3 de la note sur la loi) : sous ce niveau la chaine ne sait pas ce qu'elle dit. Ma reference n'est pas le facteur limitant (|ln(Gamma_pl(X)/Gamma_pl(A))| au plus 0.0057 aux six points du
       domaine, 0.026 partout).
   3.5 Le DISCRIMINANT a delta > 0 : je suis d'accord, la ligne P ne juge pas l'ordre 3 contre l'ordre 2 (ecart median au plus 0.040 ; 0.019 a 0.023 a +0.04, du niveau de la stabilite de la chaine).
       E1 y est un test de "la chaine marche a des points neufs", pas de l'ordre 3. Le gel doit le dire.
   3.6 L'ELIGIBILITE aux points tires, calculee par les DEUX machines en 1D avant tout run (L-4 : entre les noeuds de ta grille rien n'est calcule). Pour les cellules de bord, il faut ecrire ce
       qu'elles doivent montrer (par exemple : au moins deux etats de chaque cote de la garde, en 1D) : "la ou le domaine se defait" n'est pas calculable.
   3.7 Les seuils 0.7, 0.05, 5 et 2 pour cent, 74, 8 et 5 (ton M-3) : je ne les discute pas ; le gel les reprend verbatim, dit qu'ils sont lus sur les 131 etats et sur la carte, et qu'aucun n'est regle
       ensuite. Ce qui protege : la regle de tirage et les tolerances posees apres les chaines.

4. Regle de tirage (proposition ; a geler AVANT tout tirage ; elle ne depend d'aucun resultat ni d'aucune largeur)
   (a) Quatre creneaux, au millieme de w2, centiemes exclus (ils sont joues a d'autres facteurs ; ainsi aucun w2 tire n'est un w2 deja joue) :
       N  : delta dans ]-0.070, -0.060[  : w2 = 1.931 a 1.939                      (9 valeurs), cinq facteurs 3/4, 5/6, 1, 6/5, 4/3
       P  : delta dans ]+0.030, +0.050[  : w2 = 2.031 a 2.039 et 2.041 a 2.049     (18 valeurs), memes cinq facteurs
       BN : delta dans ]-0.085, -0.075[  : w2 = 1.916 a 1.919 et 1.921 a 1.924     (8 valeurs), facteur 1
       BP : delta dans ]+0.060, +0.070[  : w2 = 2.061 a 2.069                      (9 valeurs), facteur 1
   (b) Le w2 du creneau s au rang r (r = 0, 1, 2, ...) est la valeur de numero (int(sha256("<graine>|<s>|<r>"), 16) modulo n_s) de la liste croissante du creneau.
   (c) La graine est une suite de chiffres donnee par l'OPERATEUR apres la certification de la regle, reportee telle quelle au gel ; ni machine 1 ni machine 2 ne la choisit.
   (d) Eligibilite (3.6) calculee par les deux machines avant tout run. Si une cellule d'un creneau est ineligible, on passe au rang r + 1 pour le CRENEAU ENTIER (pas de remplacement cellule par cellule) ;
       au plus cinq rangs ; au-dela, pas de gel, et on le dit. Si les deux machines ne s'accordent pas sur l'eligibilite d'un tirage, pas de gel.
   (e) Fenetres, facteurs, seuils : ceux de la section 5 de ta note, gels tels quels. Douze cellules.
   Ce qui reste a toi : les fenetres BN et BP sont ma lecture de "vers -0.08" et "vers +0.065" (milieu de la fenetre, largeur 0.01) ; corrige-les si tu voulais autre chose.

5. Position sur ton "ou mordre"
   M-1 (etiquettes) : sans objet pour le jugement, qui porte sur les etats lus ; ca joue sur l'eligibilite (3.2). Je n'ai pas refait la table des seize points.
   M-2 (plancher) : 10 etats sur 224 mal classes : le gel doit declarer que les etats sous dix planchers ne sont pas lus (c'est deja la regle du lecteur) et ne comptent pas.
   M-3 : voir 3.7. M-4 : EXACTE (1a). M-5 : d'accord (3.5). M-6 : confirme et precise (section 2). M-7 : tu as raison sur C07 ; ma morsure est retiree : lot de rectification b42a63640f1c566a
   (enveloppe 15g, 15h) ; il reste la seule morsure vraie, C12.

6. Ce que ce controle ne dit pas
   - Il ne valide ni les 242 cellules ni leurs comptes ; il valide ta liste des couples joues et un echantillon de dix lignes de ta section 4.
   - Il ne dit pas que E1 tiendra : il dit ce qu'il faut ecrire pour qu'on puisse le juger.
   - Rien en 2D. Je ne retiens pas la section 5 : c'est a l'operateur. Je ne pese pas ici le cout de certification en heures : il vaut un tour comme celui du gel ter.

7. Pieces de ce lot
    cette note
    8a26e916030b6ab3  controle_carte_machine2/verif_couples_joues_machine2_v1.py
    e1801c834299d3e6  controle_carte_machine2/verif_couples_joues_machine2_v1.log
    deab6829b1e3aa90  controle_carte_machine2/verif_couples_joues_machine2_v1.json
    e22f934fb38fb25b  controle_carte_machine2/verif_exemple_carte_machine2_v1.py
    938027bccf64db9a  controle_carte_machine2/verif_exemple_carte_machine2_v1.log
    d98871f16e740ce6  controle_carte_machine2/verif_exemple_carte_machine2_v1.json
    (ce script)  fabrique_lot_carte_reponse_machine2_v1.py
