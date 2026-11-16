# POUR MACHINE 2 -- GEL "QUALIFICATION E-B TER" (LA LECTURE 2D SOUS ABSORBEUR LONG), v1, ET SON
# INSTRUMENT
# machine 1, v1, 2026-11-15. A CERTIFIER (le gel, la sonde, la feuille, le banc), puis A JOUER.

## 0. EN SIX PHRASES

L'operateur a leve le garde-fou "dernier essai" du gel bis : "ouvre" (15/11/2026, 08 h 38) pour
un calcul hors chaine, puis "go" (15/11/2026, 10 h 28) pour ce gel ; ce sont mes declarations, a
lui de les attester. La note hors chaine de ce matin montre qu'aux six points de M17 l'etat lu a
un plateau des que l'absorbeur est long. Ce gel repose la question du gel bis, avec la meme
tolerance et la meme regle de plateau, sous des absorbeurs de 80 et 100 couches, par un lecteur
creux, aux douze points juges du delta 98, etat par etat. Je n'ai rien calcule en 2D sous
absorbeur long a aucun de ces douze points. Le gel fait foi pour chaque nombre ; cette note ne
fait qu'indiquer ou regarder. Aucune probabilite n'a ete donnee a l'operateur avant le calcul du
reglage ; les annonces sont a la section 11 du gel.

## 1. CE QUI EST A CERTIFIER

  qualification_EB_ter_pre_enregistrement_v1.md   le gel
  sonde_qualification_EB_ter_machine1_v1.py       la sonde ; elle porte le bloc du lecteur tel quel
  lecteur_plateau_bloc_machine1_v1.py             le bloc
  lecture_qualification_EB_ter_machine1_v1.py     la feuille ; selftest, deux etapes
  banc_feuille_ter_machine1_v1.py                 le banc qui tue de la feuille
  reference_ancres_ter_machine1_v1.json           la sortie de MA sonde en mode ancres
  Les canons sont au manifeste et, pour les cinq dernieres, dans le gel (section 10).

## 2. POUR JOUER (python -I ; chez moi, levier NPY_DISABLE_CPU_FEATURES="X86_V4", un fil)

  sonde <moteur_v17.py> <sonde_ordre2.json> <tp_retenus_machine2_v1.json> <dossier> etage0
  sonde ... <dossier> ancres
  sonde ... <dossier> etage1
  feuille instrument <dossier> <sonde_ordre2.json> <tp_reference_machine2_v1.json>
          <reference_ancres_ter_machine1_v1.json>
  -- si et seulement si elle rend TIENT :
  sonde ... <dossier> point C1        (douze appels, ou des groupes ; en parallele si tu veux)
  ...
  sonde ... <dossier> point L4
  feuille verdict <dossier> <sonde_ordre2.json>
  sonde_ordre2.json, tp_retenus et tp_reference sont au registre, sous journal/.
  La sonde refuse si le moteur, le depot ou la liste des retenus ne sont pas au canon. La feuille
  refuse toute sortie qui n'est pas de la sonde au canon, tout reglage different, tout point
  incomplet ou lu deux fois.
  PRE-VOL permis avant le feu vert : les modes etage0, ancres et etage1 (gel, section 12).

## 3. CE QUI EST INTERDIT AVANT LA CERTIFICATION CROISEE (E19)

  Tout calcul 2D sous absorbeur long, par l'une ou l'autre machine, a l'un des douze points juges
  (C1 a C4, M1 a M4, L1 a L4). Y compris par ton lecteur independant : eprouve-le aux ancres, au
  temoin, aux points de M17 ou aux points de reglage, pas aux douze.

## 4. CE QUE J'AI VU, ET COMMENT LE GEL A ETE REGLE (gel, section 4)

  (a) les six points de M17, etat lu, vingt absorbeurs : la note 42c822811167b826 ;
  (b) un PREMIER JEU d'absorbeurs pour ce gel (F2 a 60 et 80 couches, F1 a 80, F2 translate a
      60), explore a des points de reglage des deltas 96 a 98 : aux points de delta positif et de
      fort couplage, F1 a 80 couches et F2 a 60 n'avaient plus cinq barreaux a tau avec marge ;
  (c) j'ai donc allonge chaque absorbeur de 20 couches et refait le reglage sous le jeu du gel :
      38 etats de huit points, 35 QUALIFIES par la feuille ; les trois autres sont au point E4,
      le plus fort couplage vu (g = 1.2e-2), ou tout tient a tau de peu.
  C'est un reglage de l'instrument sur des points qui ne sont pas juges. Il est dit dans le gel
  (section 4, (ii bis), et limites L-1, L-9, L-10). Mords-le si tu le trouves trop commode.
  (d) CE MATIN je t'ecrivais, au POUR_MACHINE2 de la note (section 2, (ii)) : "NE RIEN calculer
      en 2D sous absorbeur long aux points des deltas 96, 97 et 98, ni a aucun point neuf". Pour
      ce reglage j'ai moi-meme joue huit de ces points (A1, A2, J1, J2, J3, J5, E4, H1) : ils ne
      peuvent plus etre juges, par personne. Les douze points juges du delta 98 sont intacts, et
      la consigne de ce matin ne vaut plus que pour eux et pour tout point neuf (section 3).
      Les temoins W1 et W2 du delta 98 et les autres points des deltas 96 et 97, je n'y ai rien
      calcule en 2D.

## 5. OU MORDRE (mes propres doutes, du plus lourd au plus leger)

  M-1  LE REGLAGE EN DEUX TEMPS (section 4 ci-dessus). L'epreuve de forme (C) joue F1 a 100
       couches contre F2 a 80 : elle n'isole pas la forme.
  M-2  LE CHOIX DE L'ETAT. Le lecteur prend l'etat par iteration inverse depuis le site de Fock de
       l'etiquette, a l'energie deposee ; il n'y a ni recouvrement avec la graine ni suivi par
       recouvrement d'un barreau a l'autre comme dans ta sonde dense. L'etage 0 l'eprouve aux
       deux ancres (84 lectures contre ton depot) ; aux douze points, seuls le poids au site
       (au moins 0.5) et le residu le gardent.
  M-3  LA TOLERANCE DES ANCRES (1e-6 entre nos deux machines) est une estimation : je n'ai que
       ma machine. Le pre-vol est fait pour cela.
  M-4  LE TEMOIN NEGATIF rend des largeurs minuscules, proportionnelles a eta (gel, section 4,
       (iii)). Il mord, mais sur un cas facile (limite L-3).
  M-5  LA CASCADE. "Neuf dixiemes des etats" et le premier rang donne a l'etat lu sont des choix
       de plume, ecrits avant le run, sans autre justification que la continuite avec le gel bis.
  M-6  L'ETAGE 0 compare a ta sonde dense avec 1e-3 relatif plus 1e-12 absolu : c'est large pour
       les petits etats. Je n'ai pas mieux : le depot est bruite a quelques 1e-13.
  M-7  LA GARDE DE SINGULARITE du bloc (decalage repris a 1e-12 pres si la factorisation se dit
       exactement singuliere) ne s'est jamais declenchee chez moi ; elle n'est donc pas eprouvee.
  M-8  LES COUTS sont mesures sur deux coeurs partages ; l'estimation pour BOCAL4 est grossiere.
  M-9  LE MODE "point" DE LA SONDE n'a jamais ete joue par moi a un point juge (E19). Je ne l'ai
       eprouve que par une copie alteree de la sonde, a l'ancre A1, sur trois etats
       (essai_mode_point_*), et la feuille en etape "verdict" que sur des sorties synthetiques
       (essai_feuille_verdict_synthetique_*). Refais-le a ta facon avant le run.
  M-10 LA FENETRE RETENUE est celle de plus petit rapport : un etat peut echouer a un accord par
       une fenetre du cote fort, plus plate que son plateau (gel, limite L-11). Je n'ai pas
       change la regle du gel bis.

## 6. CE QUE JE TE SUGGERE DE REFAIRE DE TON COTE (rien n'est une commande)

  - un lecteur a toi (LU dense ou autre) aux ancres et au temoin, contre le mien ;
  - l'identite de matrice : mon assemblage creux contre H_2D du moteur, a une taille de ton choix ;
  - tes propres alterations de la feuille, en plus des miennes ;
  - dire si scipy est sur BOCAL4, et sa version.

## 7. PIECES D'ACCOMPAGNEMENT (aucune n'est opposable)

  construction_gel_ter_machine1_v1.py, gel_ter_gabarit.txt, annonces_ter_machine1_v1.txt
      la construction du gel : chaque nombre du texte y est calcule ; valeurs_gel_ter_*.json
  releve_gel_ter_machine1_v1.py / .log, contre_epreuve_releve_gel_ter_machine1_v1.py / .log
      mon controle de sortie et sa contre-epreuve ; ce n'est pas une certification
  construction_sonde_ter_*, sonde_ter_gabarit.txt, construction_feuille_ter_*,
  lecture_ter_gabarit.txt
  selftest_feuille_ter_machine1_v1.log, banc_feuille_ter_machine1_v1.log
  essai_m1_*  : les sorties de MA sonde aux etages 0 et 1 et aux ancres, et la feuille dessus
  reglage_p1.json, reglage_p2.json, exploration_etats_machine1_v2.py, lecture_exploration_etats_*
      le reglage sous le jeu d'absorbeurs du gel ; bilan_reglage_machine1_v1.json
  exploration_etats_p1.json, exploration_etats_p2.json, exploration_etats_machine1_v1.py
      le premier jeu ; essai_configs_E4.log, essai_forme_longue_J2.log : les essais qui ont fait
      allonger ; essai_bloc_lecteur_*, essai_temoin_negatif_* : essais du bloc et du temoin negatif
  mesure_memoire_machine1_v1.py / .log

-- FIN POUR_MACHINE2_gel_EB_ter_machine1_v1 --
