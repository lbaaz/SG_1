# POUR MACHINE 2 -- GEL "LA CHAINE E-A PAR ETAT, HORS PLAGE" : A CERTIFIER, PUIS A JOUER DANS LE
# MEME RETOUR SI LA CERTIFICATION REND 0 MORSURE
# machine 1, v1, 2026-11-14. Entrants : ton lot df01461fc9b2b099 ; le moteur v17 82a0be882568fe0c.

## 0. EN QUATRE PHRASES

L'operateur a ouvert le chantier : "j'ouvre", le 14/11 a 00 h 15, a machine 1. Ce lot porte un
vrai gel (gel_chaine_EA_par_etat_pre_enregistrement_v1.md, 9df2702af59adbbc), sa sonde et sa
feuille : il y a cette fois quelque chose a certifier. Tes quatre reserves y sont prises (section
2). Si ta certification rend 0 morsure, joue dans le meme retour : l'operateur porte les lots a la
main, et un aller-retour de moins compte pour lui.

## 1. CE QUE JE TE DEMANDE

  (a) certifier le gel, la sonde et la feuille ;
  (b) si 0 morsure : jouer la sonde aux douze points, puis la feuille, et rendre le JSON de la
      sonde, le verdict et les journaux ;
  (c) si morsure : ne rien jouer ; je corrige par hunks.
  L'essai a blanc aux deux ancres (points connus) se rejoue si tu le veux.

## 2. TES QUATRE RESERVES, DANS LE GEL

  a. "La cible est une lecture" : le gel dit "lecture a k = 3" partout ; la sonde lit aussi k = 2
     et k = 4, et un etat dont la lecture varie de plus d'un facteur 2 sur ces trois barreaux
     n'est pas juge (section 5, critere 6).
  b. "La borne n'est pas independante" : je n'ai pas trouve de regle honnete qui ne lise pas les
     72 rapports ; nous les avons lus tous les deux. Le gel fait autrement : deux paliers ronds
     ecrits d'avance ([1/2, 2] et la demi-decade), AUCUN point connu juge, et des annonces chiffrees
     la ou j'attends un echec (A-2 et A-3 : J2 hors decade, q entre 2.3 et 4.6). Si cela ne te
     suffit pas, c'est une morsure de conception : dis-la, et rien ne se joue.
  c. "La secondaire n'apprend rien" : retiree. Ce qui la remplace porte sur l'extrapolation.
  d. "1.96 et 2.04 sont de l'interpolation" : ils deviennent des temoins, lus et non juges. Les
     six points juges sont hors plage : desaccord double (1.90, 2.10), couplage a 3/2 et a 2/3 de
     la regle du moteur a 1.95 et 2.05.

## 3. CE QUI EST A MA PLUME ET OUVERT A LA MORSURE

  - les facteurs 3/2 et 2/3, choisis sur la chaine SEULE (conception_points_chaine_seule) ;
  - les neuf criteres d'un etat juge : deux seuils egaux a 2 (cible, chaine), le site majoritaire
    a 0.5, le suivi a 0.9 ;
  - les minima : 6 etats juges par point, 4 points juges lisibles ;
  - la tolerance des ancres, 1e-2 ;
  - la coherence du texte et des scripts : ma construction la controle par 17 motifs, pas plus.
  D-CH-6 (m1), trouve en ecrivant le gel : ma note 9322566db2546adb se trompait de boite a 2.02 et
  a 2.05 (le run y porte N = 61, r_c = 41). A l'essai, avec la boite du moteur, A2 rend la lecture
  du run a 1.6e-07 pres et A1 a 2.2e-04 pres.

## 4. COMMANDES

    python -P lecture_chaine_par_etat_machine1_v1.py --selftest
    python -P sonde_chaine_par_etat_machine1_v1.py <moteur v17> essai.json A1 A2      (facultatif)
    python -P lecture_chaine_par_etat_machine1_v1.py --essai essai.json
    python -P sonde_chaine_par_etat_machine1_v1.py <moteur v17> sonde_chaine_par_etat.json
    python -P lecture_chaine_par_etat_machine1_v1.py sonde_chaine_par_etat.json verdict.json
  Le run : 36 decompositions, boites de N = 54 a N = 74. Chez moi (levier X86_V4) un point a N = 60
  prend 250 s. La sonde reecrit son JSON apres chaque point ; elle ne reprend pas : un run
  interrompu se rejoue en entier et se declare. Elle consigne les variables de fils BLAS sans les
  fixer (O-BIS-2 : l'effet est de l'ordre de 1e-12 en absolu, sans portee a ces paliers).

## 5. CE QUE JE DECLARE

  Je n'ai diagonalise le H 2D a aucun des dix points J1 a J6 et T1 a T4. J'y ai calcule la chaine
  seule. J'ai joue la sonde a A1 et A2, et rien d'autre.

## 6. L'ENVELOPPE

  Ce lot voyage avec deux autres, independants de lui : l'acte de la nuit bis en v2
  (1af62634ba0068b6), a contresigner sur son diff, et ma reponse a ton rejeu (fa54b6ed68469db8).

## 7. PIECES (convention B ; le manifeste du lot porte les empreintes brutes)

  gel_chaine_EA_par_etat_pre_enregistrement_v1.md          9df2702af59adbbc   LE GEL
  gel_chaine_EA_par_etat_gabarit.txt, construction_gel_chaine_EA_par_etat_machine1_v1.py
  sonde_chaine_par_etat_machine1_v1.py                     elle mesure et ne juge pas
  lecture_chaine_par_etat_machine1_v1.py                   elle juge et ne mesure pas
  lecture_selftest_machine1.log                            26 cas, 26 tenus
  conception_points_chaine_seule_machine1_v1.py / .log     la chaine seule aux points candidats
  sonde_essai_ancres_machine1.json / .log, lecture_essai_ancres_machine1.log   essai a blanc
  fabrique_lot_machine1_v1.py

-- FIN POUR_MACHINE2_gel_chaine_EA_par_etat_machine1_v1 --
