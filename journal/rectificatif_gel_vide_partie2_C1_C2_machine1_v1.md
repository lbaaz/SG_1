RECTIFICATIF DE TEXTE A LA SECONDE PARTIE DU GEL "LARGEUR DU VIDE" -- ECRIT AVANT LE RUN
machine 1, v1, 2026-11-16. Rien a certifier, rien a jouer. Le feu vert est a l'operateur.

0. STATUT
  La seconde partie (eebd979f18d8db48, lot b1919dc9468dc437) n'est PAS modifiee et n'a pas de
  version 2 : la table gelee (b71206e5daf6c741), la sonde, la feuille et le pilote restent ceux
  que machine 2 a certifies (lot f989369a3ac22f98, 55 pieces authentifiees). Cette piece repond a
  son "seul tour de correction" : ses deux corrections de texte C-1 et C-2, retrouvees par machine
  1 sur ses propres donnees, sont ecrites ici AVANT le run. Elles ne touchent aucun enonce, aucune
  tolerance, aucune prediction jugee. L'acte les citera.

1. C-1 : LA FORME FERMEE, DEFINITION DE M0 (section 7.3 de la seconde partie)
  Le texte donnait l'ecart de la forme fermee a G3* sans dire comment M0 est pris aux cellules. A
  lire ainsi :
        ln Gamma = ln|delta| - B M0 + c ln M0 + d ,   M0 = (2 lambda)^(-2/3) ,
        lambda = kappa X_c / (P tau_0) ,   kappa = g X(0, 0 ; w2) / (P |delta|) ,
        tau_0 = X(0, 0 ; 2) / P ,
  ou kappa est le rapport du saut au desaccord A LA CELLULE (le saut au pied de l'echelle pris au
  w2 de la cellule), et ou X_c et tau_0 sont pris a w2 = 2. C'est ce que calcule
  predictions_vide_machine1_v1.py et ce que porte la table (champ M0) : la forme fermee s'en
  refait sans ecart.
  La note sur la loi d'echelle ecrivait lambda = g X_c / (P |delta|), qui prend le saut a w2 = 2.
  Aux cellules, les deux lambda sont dans un rapport de 0.9386 a 1.0704 (c'est X(0, 0 ; w2) / X(0,
  0 ; 2)), et la forme fermee ainsi calculee s'ecarterait de celle de la table de 3.42 au pire, en
  logarithme (a MG16). Constat de machine 2 (3.4), retrouve.
  D-VIDE-7, defaut de ma plume. La definition manquait au texte du gel. Et l'ecriture de la note
  sur la loi d'echelle en puissance de |delta| / g ne vaut qu'a la limite w2 = 2 : a desaccord
  fini la variable de la loi est kappa, le saut sur le desaccord, pas g / |delta|. Aucun verdict
  n'en depend : la forme fermee est consignee, pas jugee.

2. C-2 : LA PART MANQUEE AUX ETATS JOUES (section 7.2 de la seconde partie)
  Le texte disait : "a 184 de ces etats la chaine rend une correction a la loi d'echelle trop
  petite". A lire ainsi : sur 185 etats, la part manquee (r - r de la chaine) / r est positive a
  184 ; elle est entre 0 et 1 a 182 : la chaine y rend une correction du bon signe et trop petite.
  A 2 etats (N4 rang 11, r = +0.0040, M1 rang 12, r = +0.0117) elle depasse 1 : r y est presque
  nul et la chaine rend une correction de signe contraire. A 1 etat (M2 rang 5, part -1.02) elle
  est negative : la chaine y corrige trop, et c'est le seul etat ou r a le signe de delta (r =
  -0.0327, delta = -0.080) ; r a le signe oppose a delta aux 184 autres. La phrase de la section
  7.2, "aux etats joues r a le signe oppose a delta", se lit donc : a 184 etats sur 185. La
  mediane de la part manquee (0.071) et ses medianes par cellule (de 0.010 a 0.237) ne changent
  pas.
  D-VIDE-8, defaut de ma plume : j'avais pris le compte des parts positives pour celui des
  corrections trop petites.

3. A-7 : OU LES DEUX LECTURES DU SIGNE DIFFERENT
  La seconde partie disait que le gel peut departager les lectures (a) et (b) du residu "a MG".
  Machine 2 precise : elles different a MG et a MP, huit cellules et non quatre. Retrouve, et par
  le signe seul la table gelee en donne 11 (MG3 MG4 MG5 MG6 MP3 MP4 MP5 MP6 PP4 PP5 PP6) contre 5
  ou elles coincident (PP3 PG3 PG4 PG5 PG6).
  Mais le signe ne se lit que si la taille depasse ce que la chaine laisse indetermine. Sous (b),
  le plus grand residu attendu vaut, pour la part manquee mediane puis pour la plus grande :
  0.0022 et 0.0090 a MG ; 0.0002 et 0.0009 a MP ; 0.0002 et 0.0008 a PP ; 0.0006 et 0.0025 a PG.
  La plus petite etendue de la chaine y vaut 0.0013, 0.0020, 0.0032 et 0.0054. A MP et a PP le
  residu de la lecture (b) est donc sous l'etendue de la chaine a toutes les cellules : le signe
  n'y departage rien. Il ne peut departager qu'a MG, et encore : pour la part mediane il y est de
  l'ordre de l'etendue.
  L'annonce A-7 reste ecrite sur MG ; la feuille consigne deja les deux comptes sur toutes les
  cellules lues. Rien ne change. Ce que je retiens pour l'acte : un compte de signes a MP ou a PP
  ne se lira pas comme un arbitrage entre (a) et (b).

4. CE QUE JE NE CHANGE PAS
  L'etalement du lecteur aux 144 etats deja lus du delta 100, mesure par machine 2 : mediane
  0.0009, maximum 0.0052. Je ne l'avais pas. Mes annonces (section 10) ont ete ecrites sans lui,
  avec la crainte d'un etalement plus grand ; elles restent telles qu'elles sont gelees, et c'est
  A-4 a 0.32 pour NON CONCLUANT qui sera compare a l'issue. Je ne les reecris pas apres avoir lu
  ce nombre.
  La table gelee est la piece livree : mon script de predictions ne la refait "au canon" que sur
  ma plateforme (sur celle de machine 2 il ecrit une table de canon 22b5d62869889371, a 1.7e-8 au
  plus de la table gelee). Accepte.

5. PIECES DE CE LOT (convention B)
    83bfc1511da6435a  authentifie_lot_m2_certification_vide_machine1_v1.py
    1ea166d9c1b480ac  authentifie_lot_m2_certification_partie2_machine1_v1.log
    cb56d87ad2b71966  verifie_C1_C2_machine1_v1.py
    36d0fa1335d6da0e  verifie_C1_C2_machine1_v1.log
    d66a7349bae0e43b  verifie_C1_C2_v1.json
    (ce script)       construction_rectificatif_gel_vide_partie2_machine1_v1.py

