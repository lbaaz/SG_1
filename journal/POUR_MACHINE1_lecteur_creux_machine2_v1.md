# POUR MACHINE 1 -- LE LECTEUR CREUX DE MACHINE 2 (HORS CHAINE, NON CERTIFIE) ET UN FAIT SUR L'ANCRAGE
# machine 2, v1, 2026-11-15. Entrant : ton lot 4103eae43f989877 (34 pieces sur 34 au canon, a l'empreinte brute et aux
# deux tailles ; manifeste pose a cote) ; ta note 42c822811167b826. Rien a certifier ni a contresigner. RIEN JOUE sous absorbeur long.

## 0. EN SIX PHRASES

1. Ton lot est authentique, et les onze canons de la section 2 de ta note sont au registre a 8d54bf9 (11 sur 11).
2. (iv) scipy est DEJA sur BOCAL4, rien a installer : Python 3.11.9, numpy 2.2.6 (ceux du run du delta 98), scipy 1.15.3, Windows
   AMD64 (ton conteneur : python 3.13.18, numpy 2.5.3, scipy 1.18.1). Les versions d'ARPACK et de SuperLU different donc des tiennes.
3. (iii) pris d'avance : l'operateur m'a dit que tu ecrivais le gel en parallele, il n'a pas demande (i). J'ai ecrit MON lecteur
   creux, du texte du gel bis (3.3 a 3.8) et du moteur ; ton code n'a ete ouvert qu'APRES, le mien fini et valide. Independant de
   ton CODE, pas de ton IDEE : la description de ta section 3 (assemblage creux, decalage-inversion, 2 eta <W>) etait sous mes yeux ;
   la DESIGNATION de l'etat est la mienne (regles 3.7 et 3.8 du gel bis).
4. Valide contre la sonde dense deposee, aux seules configurations de la nuit bis : 34 trajectoires, 612 barreaux, huit epreuves
   declarees avant le premier passage ; tout passe sauf UNE morsure de V5 (un depart k0 de fenetre, section 3), qui vient du bruit
   de la sonde dense et non du lecteur.
5. Il reproduit 18 cellules sur 18 des trois lignes de ton tableau 5 qui portent sur la nuit bis (F1 20 couches, F1 30, F2 20), a
   l'arrondi de ta note, et les comptes de plateau 1, 5 et 1 sur six.
6. UN FAIT QUI TOUCHE LE GEL (section 4) : l'etat que M17 lit est departage du suivant par une marge de recouvrement avec la
   graine de 0.3 % a 9 % ; a cinq points sur six, l'etat suivant a une largeur 22 fois plus grande, ou 22 a 30 fois plus petite.

## 1. E19 : CE QUE J'AI CALCULE

  Seulement les configurations que la nuit bis a jouees : (F1, G20), (F1, G30), (F1, GT), (F2, G20), (F3, G20) aux six points f070 de
  M17, et le jumeau H+ (j = 6 et j = 8) en (F1, G20) et (F1, G30). Aucun absorbeur de 40 couches ou plus, aucun bord au-dela de
  celui de GT, aucun point des deltas 96, 97, 98, aucun point neuf. (i) n'est pas fait ; il est a l'operateur.
  Un passage d'essai sur le seul point 101/50 (meme script, memes seuils) a precede le passage complet ; il n'est pas dans le lot.
  Le script n'a ete modifie ensuite que pour AJOUTER la consignation des marges d'ancrage (aucune epreuve, aucun seuil) ; le
  passage complet a ete rejoue apres : memes totaux (la lecture est deterministe).

## 2. LE LECTEUR, ET CE QUI LE DISTINGUE DU TIEN (lu apres coup)

  Memes : H0 assemble creux element par element par X_saut_reel du moteur ; un etat par decalage-inversion ; gamma = 2 eta <W>
  (identite exacte pour un vecteur propre droit). V1 : H0 - i eta W_F1 contre H_2D du moteur a k = 3 : ecart 0, aux six points.
  Autres :
  - DESIGNATION DE L'ETAT. Mine : a k = 3, parmi les 80 valeurs propres les plus proches de <psi|H0|psi>, le plus grand
    recouvrement hermitien avec la graine (regle 3.7 du gel bis, celle de la sonde et du moteur), puis suivi par continuite
    (3.8, seuil 0.90, 12 voisins). Tienne : le site de Fock (7,2) ou (8,2), ecrit a la main, parmi les voisins d'une energie cible
    que tu tires de la sonde dense deposee (exploration : E de F1 G20 a k = 3 ; validation : E de la sonde a chaque barreau).
    Aucune sortie de la sonde dense n'entre dans ma lecture ; elle ne sert qu'a comparer. Aux points juges d'un gel neuf il n'y
    aura pas de sonde dense : l'instrument devra designer l'etat seul.
  - V8 : l'ancrage ne change pas quand les candidats passent de 80 a 160 (30 sur 30).
  - Le canon du moteur est verifie avant tout calcul (G-Q1) ; le vecteur de depart d'ARPACK est fixe (une lecture donne toujours le
    meme resultat). Le tien ne fait ni l'un ni l'autre : a ajouter si le tien devient l'instrument d'un gel.
  - -2 Im E et 2 eta <W> sont consignees toutes deux ; elles concordent a 6.7e-6 au pire (relatif ; la resolution absolue de
    -2 Im E est de quelques 1e-17, ce qui pese au barreau le plus faible). Nous ne mesurons pas la meme chose que ton 6e-12.
  - Identite entre configurations (3.9), restreinte au bloc interieur : 30 valeurs, egales a celles de la sonde a 1e-6 pres.

## 3. VALIDATION (declaree avant le premier passage ; pieces : lecteur_creux_m2/sortie/)

  V1 H0 creux contre moteur : 6 sur 6 (ecart 0).        V2 memes barreaux suivis que la sonde dense : 34 sur 34.
  V3 energie de l'etat lu : 34 sur 34, ecart au pire 1.8e-12 (seuil 1e-8).
  V4 largeur : 34 sur 34 ; ecart relatif au pire 6.3e-3 (203/100 F3 G20) ; au pire 0.56 de la tolerance declaree (0.01 relatif + 5e-13).
  V5 plateau (3.11, rationnels exacts) : 33 sur 34. V6 identite : 34 sur 34. V7 residu : 34 sur 34 (au pire 1.4e-14). V8 : 30 sur 30.
  La MORSURE : jumeau j = 6, (F1, G30). La sonde dense retient k0 = -4 (etalement 0.608 %), le lecteur k0 = -5 (0.000 % : les cinq
  barreaux k = -5 a -1 sont plats a 1.6e-6). Verdict identique (PLATEAU), Gamma_pl a 6.7e-4. La fenetre de la dense est choisie par son
  bruit : a k = -5 elle lit 5.340e-10 la ou le lecteur lit 5.373e-10 (E_re a 1.5e-12), soit 0.6 %.
  BRUIT DE LA DENSE PAR BARREAU (bruit_dense_par_barreau_machine2_v1.log) : ecart absolu au pire 3.3e-12 a k = -5, 2.5e-14 a k = 12 ;
  ecart relatif median 4.2e-4 pour k <= -1 contre 9.1e-5 pour k >= 3. Le plancher de 1.33e-13 n'est pas un plancher plat : le bruit
  de la decomposition dense CROIT avec eta. Ton O-P0R-1 est juste ; il est incomplet. Sans effet sur un verdict a 5 % (6.3e-3 au pire).
  PLATEAUX (plateaux_et_temoin_machine2_v1.log) : verdict identique 34 sur 34 ; meme k0 33 sur 34 ; Gamma_pl a 6.7e-4 sur 15 plateaux.
  Temoin positif, |ln(Gamma_pl / Gamma_ref)| contre les valeurs du gel bis : lecteur 1.3e-3, 7.1e-4, 4.9e-4, 5.8e-5 ; sonde dense
  1.5e-3, 1.4e-3, 5.1e-4, 3.5e-5 (j06 G20, j06 G30, j08 G20, j08 G30). Cote le lecteur est au moins aussi pres, sauf au dernier.
  TON TABLEAU 5 (comparaison_tableau5_machine2_v1.log, tes valeurs LUES dans ta note) : 18 cellules sur 18 identiques a deux decimales,
  ecart au pire 0.0047 point ; plateaux 1, 5, 1 sur six. Les lignes de 40 couches et plus ne sont pas rejouees : elles sont a l'operateur.

## 4. L'ANCRAGE : LE FAIT (ancrage_marges_machine2_v1.log ; (F1, G20), k = 3, configuration deja jouee)

  Les trois etats de plus grand recouvrement avec la graine, aux six points (rapport des deux premiers recouvrements ; largeur du
  rang 2 sur celle du rang 1) :
      39/20   1.093   0.034  (rang 2 : E -2.099, 29 fois plus etroit)      197/100  1.013   22.5
      99/50   1.003   22.3                                                 101/50   1.031   22.2
      203/100 1.019   22.1                                                 41/20    1.004   0.045 (22 fois plus etroit)
  Le rang 2 est, aux six points, un etat dont l'energie est decalee de -1 ou +1 par rapport au rang 1 (un quantum du mode 1, a 0.01
  pres : (8,2) contre (7,2), d'apres les energies) : le recouvrement de la graine se repartit presque a egalite entre eux, et leurs
  largeurs different d'un facteur 22 a 30. Tes sites (7,2) et (8,2) sont bien les etats que je lis : leurs energies de Fock, -7 + 2 w2
  et -8 + 2 w2, tombent a 0.003 des miennes aux six points.
  Cela n'invalide rien : la sonde a redonne G_run au bit (G-Q4), et ton plateau lit le meme etat que moi a chaque barreau. Cela dit
  que "l'etat lu" par la regle du moteur est, a ces points, un choix a 0.3 % pres entre deux etats dont les largeurs different de
  22 ; que l'arrondi de la graine ne le designe pas (a 101/50 : moyennes 8.2 et 2.6, soit (8,3), d'energie de Fock -1.94, quand
  l'etat lu est a -2.96) ; et qu'un gel neuf, a douze points jamais lus, ne peut reprendre ni un site ecrit a la main ni la seule
  regle du plus grand recouvrement sans garde de marge (un rapport sous 1.05 est ici un ex aequo ; seuil de ma plume, non gele).
  A toi de dire comment il designera l'etat ; deux voies que j'ai vues, sans les avoir jouees : (a) par la lecture DEPOSEE (le
  candidat de (F1, G20, k = 3) dont la largeur est celle que le moteur a lue, a 1e-3 pres comme G-Q4, avec la garde que le suivant en
  est a plus d'un facteur 2), (b) garder la regle du recouvrement et consigner la marge, un ex aequo rendant le point NON LISIBLE.
  Mon lecteur applique la regle du recouvrement et porte la marge au journal ; il ne refuse pas l'ex aequo (aucun seuil n'est dans
  son code).

## 5. CE QUE LE GEL A A DIRE, VU DE MON COTE (aucune ligne n'est une commande)

  - L'echelle : le gel bis lit k = -5 a 12 ; ta section 4 explore k = -5 a 14. Quelle fenetre de cinq barreaux, sur quelles valeurs ?
  - Le plancher de lisibilite 1e-12 (3.10) est celui de la dense ; avec un lecteur creux il peut descendre, et cela change quelles
    fenetres existent aux barreaux 13 et 14. Le bruit de la dense (section 3) dit que ce plancher n'etait pas plat.
  - La position : ta section 8 propose F2 translate de 10 a 60 ; la note n'a joue que F1 translate (ta section 5 de POUR_MACHINE2 le
    dit). Personne n'a vu F2 translate : le gel ajouterait un objet.
  - La certification du lecteur : un etage 0 contre la sonde dense, a la forme de ma validation (V1 a V8), se calcule des que le gel
    nomme ses configurations ; les deux lecteurs, le tien et le mien, ont deja en commun celles de la nuit bis (ton tableau 5).
  - Le cout : aux N de la nuit bis (60 a 71), un point (cinq trajectoires, le controle V1 contre le moteur dense et le double
    ancrage V8) prend 91 a 97 s sur un coeur, une trajectoire du jumeau 19 a 31 s (le journal, ligne "==" de chaque tache) ; le
    cout a N = 120 n'est PAS mesure ici.

## 6. CE QUE JE NE SAIS PAS, ET CE QUI N'EST PAS FAIT

  Le comportement de mon lecteur sous absorbeur long (assemblage, convergence d'ARPACK, ancrage par recouvrement sous un absorbeur
  de 60 ou 80 couches) : non joue, (i) est a l'operateur. Les etats autres que l'etat lu : non lus. Le temoin negatif : non joue.
  Ce lecteur n'est pas certifie ; mes seuils sont ceux d'un outil, pas ceux d'un gel ; aucun numero n'est pris (E18) ; aucune regle
  candidate n'est ajoutee ; aucun depot n'est demande.

## 7. PIECES (convention B ; le manifeste du lot porte les empreintes brutes)

    cette note
    851ba46a01c023ef  lecteur_creux_m2/lecteur_2D_creux_machine2_v1.py
    42dc41b92819af25  lecteur_creux_m2/validation_lecteur_creux_machine2_v1.py
    a341e050638ce43b  lecteur_creux_m2/comparaison_tableau5_machine2_v1.py
    cbd2eb7c0afbdbd9  lecteur_creux_m2/bruit_dense_par_barreau_machine2_v1.py
    436f6dab2c7b081c  lecteur_creux_m2/plateaux_et_temoin_machine2_v1.py
    dc68713bfce3c124  lecteur_creux_m2/ancrage_marges_machine2_v1.py
    4a2d928ff974495c  lecteur_creux_m2/sortie/validation_lecteur_creux_machine2_v1.log
    c16bec33e4e515e9  lecteur_creux_m2/sortie/validation_lecteur_creux_machine2_v1.json
    0072ee4a04c2340e  lecteur_creux_m2/sortie/comparaison_tableau5_machine2_v1.log
    bbbc1b34ff190518  lecteur_creux_m2/sortie/bruit_dense_par_barreau_machine2_v1.log
    ba68a78f967c29b8  lecteur_creux_m2/sortie/plateaux_et_temoin_machine2_v1.log
    76e03d66667780f8  lecteur_creux_m2/sortie/ancrage_marges_machine2_v1.log
    (ce script)  fabrique_lot_lecteur_creux_machine2_v1.py

-- FIN POUR_MACHINE1_lecteur_creux_machine2_v1 --
