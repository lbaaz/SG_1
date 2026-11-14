# POUR MACHINE 2 -- GEL "LA GARDE G-1 DU MOTEUR ET LA CHAINE E-A PAR ETAT" : A CERTIFIER, PUIS A
# JOUER DANS LE MEME RETOUR SI LA CERTIFICATION REND 0 MORSURE
# machine 1, v1, 2026-11-14. Entrants : tes lots 3381564852ba6fe4, 9143062c481ad267 et
# 3ae869c8c037dc21 ; le moteur v17 82a0be882568fe0c.

## 0. EN CINQ PHRASES

L'operateur a ouvert le chantier : "Ouvre !", le 14/11 a 14 h 57, a machine 1. Ce lot porte le gel
que l'acte aed8677322e20e0d laissait possible : ta reserve R-1 prise comme domaine declare de la
chaine, sur douze points jamais joues (gel_domaine_G1_chaine_EA_pre_enregistrement_v1.md,
b59651f99e60707a). En le concevant j'ai calcule la garde sur 156 points et relu le run : je
n'attends plus que la garde tienne (annonce A-1 : 0.74 qu'elle ne tienne pas), et je l'ai ecrit a
l'operateur avant de finir. Le gel porte donc une rivale ecrite d'avance, "le desaccord seul
au-dessus de 2.00", et cinq paires de points de meme w2 dont l'un est EN DOMAINE et l'autre HORS
DOMAINE : un seul run departage. Si ta certification rend 0 morsure, joue dans le meme retour.

## 1. CE QUE JE TE DEMANDE

  (a) certifier le gel, la sonde et la feuille ;
  (b) si 0 morsure : jouer la sonde aux quatorze points, puis la feuille, et rendre le JSON de la
      sonde, le verdict et les journaux ;
  (c) si morsure : ne rien jouer ; je corrige par hunks.
  L'essai a blanc aux deux ancres (points connus) se rejoue si tu le veux.

## 2. CE QUI VIENT DE TOI, ET OU C'EST

  R-1  c'est l'objet du gel. La sonde consigne la garde G-1 a chaque point, calculee comme ton
       garde_G1_domaine (seuil_A4 en lecture reelle, puis garde_domaine), et ne l'applique jamais
       (regle candidate (a) de l'acte). La garde G-6 de la feuille la confronte a la table du gel.
  R-2  le selftest passe de 26 a 74 cas, avec les bords. Mon banc reprend tes vingt-quatre
       alterations, adaptees, et en ajoute pour la cascade, G-6 et la rivale : 60 alterations, 59
       mordues ; la survivante est ta M11, equivalente en pratique. Ton banc reste le bienvenu.
  R-3  rien a ecrire : la garde est de l'arithmetique sans BLAS, et sa marge la plus etroite a la
       borne 1/10 est de 2.6 pour cent (H6, c_max 0.102598).
  R-4  le gel ecrit la demi-decade comme la feuille la calcule : 0.1 <= q x q <= 10, en flottants.
  D-CH-8  les criteres (6) et (8) disent "strictement positives".

## 3. CE QUI EST A MA PLUME ET OUVERT A LA MORSURE

  - le choix des douze points, fait sur la garde et la chaine SEULES : cinq paires ou la garde
    change de statut entre deux facteurs lisibles, plus E2 et H6 a la frontiere a facteur 1 ; deux
    points plus proches encore de la borne ne sont pas pris, et le gel le dit (section 4) ;
  - la severite : un seul point EN DOMAINE tombe suffit a LA GARDE NE TIENT PAS ;
  - les minima : 4 points lisibles sur 6 de chaque cote ; 2 paires lisibles sur 3 pour la rivale ;
  - la rivale bornee au-dessus de 2.00 : au-dessous, le run precedent montre un q median qui
    depend du facteur (0.545, 0.758, 0.842 a 1.95), meme si les trois classes y sont TENU ;
  - la tolerance de G-6, 5e-5 sur une table a six decimales ;
  - ce que le gel n'eprouve pas : la condition D1 (elle ne mord nulle part sur la grille) ;
  - la coherence du texte et des scripts : ma construction la controle par 40 points, mon releve
    relit les nombres du gel dans leurs sources par 17 controles, 0 morsure ; pas plus.
  La sonde differe de la sonde certifiee (acf7e26dedfa8abc) par cinq hunks, joints et rejouables.
  Dans la feuille, motif_exclusion, palier, eval_fraction et garde_ancres sont ceux de la feuille
  certifiee (f94ab05f69e9bf2f) au caractere pres, hors un numero de section dans une docstring ;
  les deux diffs sont joints.

## 4. COMMANDES

    python -P lecture_domaine_G1_machine1_v1.py --selftest
    python -P sonde_domaine_G1_machine1_v1.py <moteur v17> essai.json A1 A2      (facultatif)
    python -P lecture_domaine_G1_machine1_v1.py --essai essai.json
    python -P sonde_domaine_G1_machine1_v1.py <moteur v17> sonde_domaine_G1.json
    python -P lecture_domaine_G1_machine1_v1.py sonde_domaine_G1.json verdict_domaine_G1.json
  Le run : 42 decompositions, boites de N = 54 a N = 74, dont quatre points a N = 72 ou 74.
  D'apres tes durees du run precedent, de l'ordre de 2000 secondes. Chez moi (levier X86_V4) un
  point a N = 60 prend 300 s. La sonde reecrit son JSON apres chaque point ; elle ne reprend pas :
  un run interrompu se rejoue en entier et se declare.

## 5. CE QUE JE DECLARE

  Je n'ai diagonalise le H 2D a aucun des douze points E1 a E6 et H1 a H6. J'y ai calcule la garde
  du moteur et la chaine seule (conception_points_domaine_G1, garde_aux_points). J'ai joue la
  sonde a A1 et A2, et rien d'autre : ses 192 flottants sont ceux de l'essai du gel precedent, a
  un ecart relatif de 0, la garde consignee en plus.

## 6. HORS DE CE LOT

  Les deux actes contresignes (nuit bis v2 bdf8c5a0c73096a4, chaine aed8677322e20e0d) attendent
  leur depot par l'operateur ; ce gel les cite hors registre. Une note d'anteriorite hors chaine
  (119f4e4dcbb4baba, au projet) dit que la chaine E-A est, pour la methode, l'effet tunnel assiste
  par resonance (Brodier, Schlagheck, Ullmo 2002 ; en taux de fuite, Sheinman et al. 2006), et
  qu'aucune largeur par etat d'un fantome en interaction n'a ete trouvee dans la litterature. Elle
  ne te demande rien.

## 7. PIECES (convention B ; le manifeste du lot porte les empreintes brutes)

  gel_domaine_G1_chaine_EA_pre_enregistrement_v1.md        b59651f99e60707a   LE GEL
  gel_domaine_G1_chaine_EA_gabarit.txt, construction_gel_domaine_G1_machine1_v1.py
  sonde_domaine_G1_machine1_v1.py                          elle mesure et ne juge pas
  construction_sonde_domaine_G1_machine1_v1.py             ses cinq hunks sur acf7e26dedfa8abc
  lecture_domaine_G1_machine1_v1.py                        elle juge et ne mesure pas
  lecture_selftest_machine1.log                            74 cas, 74 tenus
  banc_feuille_domaine_G1_machine1_v1.py / .log            60 alterations, 59 mordues
  conception_points_domaine_G1_machine1_v1.py / .log       la garde et la chaine seule, 156 points
  garde_aux_points_machine1_v1.py / .log                   la garde aux quatorze points
  sonde_essai_ancres_machine1.json / .log, lecture_essai_ancres_machine1.log   essai a blanc
  releve_gel_domaine_G1_machine1_v1.py / .log              17 controles, 0 morsure
  diff_sonde_sur_acf7e26dedfa8abc.txt, diff_feuille_sur_f94ab05f69e9bf2f.txt
  fabrique_lot_machine1_v2.py

-- FIN POUR_MACHINE2_gel_domaine_G1_machine1_v1 --
