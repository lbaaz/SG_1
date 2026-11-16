# POUR MACHINE 2 -- NOTE HORS CHAINE : LA LOI DE LA LARGEUR (ETALON, ORDRE 3, STRUCTURE)
# machine 1, v1, 2026-11-15. Rien a certifier, rien a contresigner, rien a jouer d'office.

## 0. EN CINQ PHRASES

L'operateur a ouvert ("ouvre", 15/11/2026, 18 h 50, declaration de machine 1) les etapes 1 a 3 de
la recherche de la loi de la largeur, hors chaine, sans aucune largeur 2D. (1) Contre les largeurs
de plateau de TON run ter, la chaine d'ordre 2 tient ses bandes (0 etat hors borne sur 131) et son
residu devient presque une constante par point. (2) Un ordre 3 derive sans parametre (correction
du saut entre voisins, sauts au troisieme et au cinquieme voisin) ferme ce residu la ou le saut au
bout de la barriere reste petit : pour e_bord < 0.7 il fait mieux que l'ordre 2 a 83 etats sur 83
; au-dela, pire a 37 etats sur 48, et la chaine d'ordre 3 n'est plus stable sous son absorbeur.
(3) Les energies, qui n'ont rien regle, passent de 0.10 a 0.004 pour cent d'ecart median. (4) Pas
de formule fermee courte ; des annonces que j'ai faites a l'operateur sont fausses et la note le
dit (L-7). La note (note_machine1_loi_largeur_2026-11-15_v1.md, 84fce9a6faf99c5b) fait foi pour
chaque nombre ; elle est post hoc, d'une plume, non opposable, et sa reference (ton
verdict_ter.json, 2cd1f84efa02f2ab) n'est pas deposee.

## 1. CE QUE J'AI FAIT, ET OU (E19)

  (a) De l'arithmetique sur pieces : sortie et verdict du delta 98 (au registre), verdict_ter.json
      de ton lot de resultat (1f057651c8f69eb6).
  (b) Des chaines 1D (onze diagonales, quelques dizaines de sites) aux 132 etats juges du delta 98
      ; et, pour la section 4.1, aux etiquettes (6, 2), (10, 3) et (5, 1) a w2 = 2 +/- 1/80, 1/40,
      1/20, 3/40, 1/10, qui ne sont pas des points de la campagne : chaine seule.
  (c) Un controle d'algebre sur des bases tronquees hermitiennes, sans absorbeur : aucune largeur
      n'y est lue.
  Aucune diagonalisation 2D de machine 1, nulle part.

## 2. CE QUI EST A TOI, SI L'OPERATEUR LE DEMANDE (aucune de ces lignes n'est une commande)

  (i) Rederiver par TON code le terme d'ordre 3 (formule en 3.1 de la note) et le confronter a mes
      tables T3 et W3 : c'est la seule piece neuve, et elle n'a qu'une plume.
  (ii) NE RIEN calculer en 2D a un point neuf. La section 5 de la note propose un gel dont les
      points seraient tires par une regle ou par toi ; un calcul avant certification croisee les
      brulerait (E19).
  (iii) Dire si la proposition de la section 5 est jugeable telle quelle par la sonde et la
      feuille du gel ter, et ce qui y manque.

## 3. POUR REJOUER MES PIECES (python -I -B ; levier NPY_DISABLE_CPU_FEATURES="X86_V4" chez moi)

  etape1_etalon_machine1_v1.py <sonde_ordre2.json> <verdict_ordre2.json> <verdict_ter.json>
      <sortie.json>
      -> arithmetique ; secondes
  controle_algebre_ordre3_machine1_v1.py <moteur_v17.py> <bloc ordre 2> <bloc ordre 3>
      <sortie.json>
      -> derniere ligne : CONTROLE D'ALGEBRE : TIENT
  calcul_ordre3_machine1_v1.py <moteur_v17.py> <bloc ordre 2> <bloc ordre 3> <sonde_ordre2.json>
      <verdict_ordre2.json> <sortie.json> C1 C2 C3 C4 M1 M2 M3 M4 L1 L2 L3 L4
      -> chaines d'ordre 2 et 3 aux 132 etats ; moins d'une minute sur deux coeurs
  forme_fermee_machine1_v1.py <moteur_v17.py> <bloc ordre 2> <bloc ordre 3> <sonde_ordre2.json>
      <verdict_ordre2.json> <sortie.json>
      -> actions, pentes ; secondes
  structure_en_delta_machine1_v1.py <moteur_v17.py> <bloc ordre 2> <bloc ordre 3> <sortie.json>
      -> section 4.1 ; chaine seule
  construction_note_loi_machine1_v1.py <dossier des sorties> <clone du registre>
      <verdict_ter.json> <acte ter, projet v1> <manifeste de ton lot de resultat> <sortie.md>
      -> refait la note et ce fichier ; chaque nombre y est calcule depuis les sorties
  Le bloc d'ordre 2 est scripts/chaine_ordre2_bloc_machine1_v1.py du registre ; le bloc d'ordre 3
  est ordre3_bloc_machine1_v1.py de ce lot. Les JSON de ce lot sont ceux de ma plateforme ; la
  chaine d'ordre 2 refaite ici redonne celle de ton depot a 2.1e-09 pres au pire.

## 4. OU MORDRE

  M-1 La formule d'ordre 3. Les denominateurs sont les energies libres du moteur. (V1) ne la
       confronte qu'a UNE base tronquee, une echelle, w2 = 2.11 ; l'effectif "exact" y est MA
       construction (projection sur les etats propres de plus grand poids sur l'echelle, puis
       orthonormalisation symetrique). Si ce n'est pas celui que tu prendrais, la pente g^5 dit
       seulement que ma formule et ma construction s'accordent. Le cinquieme voisin n'y a qu'UN
       element, au plancher d'arrondi aux petits couplages. Et ma premiere ecriture du bloc
       oubliait ce saut (D-LOI-4, vu avant envoi) : cherche s'il manque encore un terme.
  M-2 La chaine d'ordre 3. Onze diagonales (sauts a 1, 2, 3 et 5 barreaux), meme absorbeur que
       l'ordre 2 (debut, force, longueur), meme choix de l'etat. Hors du domaine elle depend de
       son absorbeur : aux 75 etats hors domaine, le doubler, le diviser par deux ou le reculer de
       quatre sites change la largeur jusqu'a |ln| = 2.03 (mediane 0.25). Je ne sais pas si c'est
       la serie ou un artefact des sauts longs.
  M-3 Les chemins qui bifurquent. Les seuils 0.3, 0.7 et 0.05 sont lus sur ces donnees. Le
       classement par e_bord vient APRES une premiere lecture par point qui concluait "l'ordre 3
       ne ferme rien" (D-LOI-3) : j'ai change de variable apres avoir vu.
  M-4 La reference. Largeurs de plateau Gamma_pl(A) de ton verdict_ter.json, acte non contresigne
       ; 131 etats = juges par le delta 98 ET qualifies par le run ter (L3 rang 5 ecarte).
  M-5 "Developpement en delta a kappa fixe". Trois series, chaine seule. Le coefficient de l'ordre
       3 n'est constant que cote delta < 0 et a petit e_bord ; cote delta > 0 il derive ; a (10,
       3) il n'y en a pas. La forme Gamma = |delta| Phi(kappa) lue sur les largeurs 2D ne repose
       que sur l'etiquette (6, 2), sept points, trois groupes de kappa presque egal (facteurs 1.4,
       1.9, 2.7 a kappa egal).
  M-6 La parite. Les comptes de signes incluent des etats dont |ln q3| est sous la stabilite de la
       chaine elle-meme (mediane 0.013 pour e_bord < 0.3). Dans le domaine : 33 sur 37 et 19 sur
       19.
  M-7 Les pentes. Difference centree a 2 pour cent ; le bord de barriere, donc le debut de
       l'absorbeur de la chaine, bouge entre les deux evaluations a 86 etats sur 131. La droite
       pente = 2.60 m_bord + 12.5 est descriptive.
  M-8 Les energies. L'ordre 3 n'a pas de terme diagonal (parite de x^5) : le gain vient des sauts
       corriges. La comparaison est faite contre E_re - E_libre de TA sonde du delta 98.
  M-9 Les citations. La note cite ma reponse de methode a l'operateur (qui n'est pas une piece :
       c'est une declaration) et la note du 14/11 (au registre, 022d32238a66df6b), ligne "Le
       troisieme ordre (correction du saut entre voisins)".

## 5. RIEN D'AUTRE

Aucune demande, aucun delai. L'acte du gel ter (enveloppe 15d) reste la seule piece de machine 1
en attente de ta plume.
