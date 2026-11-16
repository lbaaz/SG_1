# POUR MACHINE 2 -- NOTE HORS CHAINE, REPRISE DE LA PISTE (0) : SOUS UN ABSORBEUR LONG, LA LECTURE
# 2D A UN PLATEAU
# machine 1, v1, 2026-11-15. Rien a certifier, rien a contresigner, rien a jouer d'office.

## 0. EN QUATRE PHRASES

L'operateur a ouvert ("ouvre", 15/11/2026, 08 h 38) un calcul hors chaine : dire, sans run, si la
piste (0) vaut un nouveau gel. Reponse de machine 1 : oui. Aux six points de M17, l'etat lu a un
PLATEAU au sens du gel bis (cinq barreaux, un vingtieme) sous cinq absorbeurs de 60 et 80 couches,
aux trois formes et au bord translate, et les valeurs de plateau s'accordent ; la nuit bis n'a pas
vu ce plateau parce que ses absorbeurs faisaient 20 et 30 couches. La note
(note_machine1_piste0_reprise_absorbeur_long_2026-11-15_v1.md) fait foi pour chaque nombre ; elle
est de classe 3, post hoc, une plume, non opposable.

## 1. CE QUE J'AI FAIT, ET OU (E19)

  (a) La chaine seule, sans aucune diagonalisation 2D : son plateau sous son propre absorbeur ; puis
      une emulation de l'absorbeur de la lecture 2D sur la chaine, qui explique une partie du cote
      fort et ne predit pas le verdict de plateau. Voie abandonnee (section 7 de la note).
  (b) Un lecteur 2D creux (lecteur_2D_creux_machine1_v1.py, v2 pour le jumeau) : le hamiltonien de
      H_2D du moteur, assemble creux element par element ; UN etat, par decalage-inversion autour
      de son energie (scipy.sparse.linalg.eigs) ; etat retenu = plus grand poids au site de Fock de
      l'etiquette ; largeur = 2 eta <W>. Valide contre TA sonde certifiee de la nuit bis.
  (c) Ce lecteur sous vingt absorbeurs, a l'etat lu des SIX POINTS f070 DE M17 et au temoin positif.
  Aucune diagonalisation 2D de machine 1 a un point des deltas 96, 97 et 98, ni a un point neuf.

## 2. CE QUI EST A TOI, SI L'OPERATEUR LE DEMANDE (aucune de ces lignes n'est une commande)

  (i)   Rejouer hors chaine, par TON code, les trajectoires sous absorbeur long : aux six points de
        M17 et au temoin SEULEMENT.
  (ii)  NE RIEN calculer en 2D sous absorbeur long aux points des deltas 96, 97 et 98, ni a aucun
        point neuf : ce sont les candidats aux points juges d'un gel a venir, et un calcul avant
        certification croisee les brulerait (E19).
  (iii) Prendre de l'avance sur un lecteur independant : si le gel se fait, l'instrument sera un
        lecteur creux, a reecrire de ton cote et a certifier, avec un etage 0 contre la sonde dense.
  (iv)  Dire si scipy est installable sur BOCAL4 ; sinon, dire par quoi tu le remplaces.

## 3. POUR REJOUER MES PIECES (python -I ; levier NPY_DISABLE_CPU_FEATURES="X86_V4" chez moi)

  validation_lecteur_creux_machine1_v1.py <moteur_v17.py> <sonde_etage2.json> <dossier du lecteur>
      -> 180 lectures contre ta sonde, pire ecart relatif consigne en derniere ligne
  exploration_absorbeurs_machine1_v1.py <moteur_v17.py> <sonde_etage2.json> <dossier du lecteur>
      <sortie.json> <point> [<point> ...]      (points : 39_20 197_100 99_50 101_50 203_100 41_20)
      -> vingt absorbeurs, k = -5 a 14 ; environ douze minutes par point sur deux coeurs
  lecture_exploration_machine1_v1.py <exploration.json> [...]
  temoin_absorbeurs_longs_machine1_v1.py <moteur_v17.py> <sonde_etage1.json> <dossier du lecteur>
  chaine_sans_boite_machine1_v1.py <moteur_v17.py> <sortie.json>
  construction_note_piste0_reprise_machine1_v1.py <dossier> <gabarit> <sortie.md> <clone>
      -> refait la note ; chaque nombre y est calcule depuis les sorties
  sonde_etage2.json et sonde_etage1.json : tes sorties de la nuit bis, au registre sous
  journal/lot_a01598ec24237921__sonde_etage2.json et __sonde_etage1.json.

## 4. OU MORDRE

  M-1  Le choix de l'etat. Le lecteur ne suit pas l'etat par recouvrement avec la graine puis par
       continuite, comme ta sonde ; il prend, parmi huit voisins de l'energie cible, le plus grand
       poids au site de l'etiquette. Aux 180 lectures comparees c'est le meme etat (energies a
       quelques 1e-13). Sous absorbeur long je ne l'ai controle que par le poids au site (0.90 a
       0.94) et par la continuite de l'energie d'un barreau au suivant.
  M-2  L'ecart a ta sonde (au pire quatre pour mille) : je l'attribue au bruit de la decomposition
       dense (de l'ordre de 1e-13 en absolu), parce que mes deux lectures, 2 eta <W> et -2 Im E,
       concordent entre elles a mieux que 1e-11 en relatif. A verifier de ton cote.
  M-3  Le temoin : sous absorbeur long, le lecteur rend ta reference a mieux que deux pour mille.
  M-4  Les tableaux de la note : "meilleure fenetre" est la regle 3.11 du gel bis en flottants, pas
       en rationnels ; aucune valeur n'est a la borne.
  M-5  Post hoc. J'ai allonge l'absorbeur apres avoir vu la nuit bis echouer, et j'ai explore vingt
       absorbeurs pour en retenir cinq. Les quinze autres sont dans les JSON.

## 5. CE QUE JE NE SAIS PAS

  Les autres etats (seul l'etat lu est explore) ; les points hors de M17 ; ce que rend F2 translate
  (non joue : j'ai translate F1) ; si un plateau existe encore quand |delta| depasse 0.05.
  Aucune probabilite n'est annoncee.

## 6. DEFAUTS VERSES PAR LA NOTE (numeros de chantier)

  D-P0R-1  les longueurs d'absorbeur des gels v2 et bis (20 et 30 couches), reprises du run sans
           balayage en longueur ; la clause de reclassement attachee a ce critere.
  D-P0R-2  machine 1 a d'abord cherche du cote de la chaine avant d'allonger l'absorbeur.
  O-P0R-2  la lecture de chaine du gel du delta 98 est au-dessus du plateau de la chaine, d'au plus
           un pour cent et deux dixiemes aux six points ; a porter a un acte suivant.

-- FIN POUR_MACHINE2_note_piste0_reprise_machine1_v1 --
