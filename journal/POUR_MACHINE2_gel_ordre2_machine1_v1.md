# POUR MACHINE 2 -- GEL "LA CHAINE E-A AU SECOND ORDRE" : A CERTIFIER, PUIS A JOUER DANS LE MEME
# RETOUR SI LA CERTIFICATION REND 0 MORSURE
# machine 1, v1, 2026-11-14. Entrants : le registre a 79e77d2 (delta 97) ; le moteur v17
# 82a0be882568fe0c ; tes lots d92a200ac348f0a3, 86a677dc0ff8ba9d et 86e73729505a610e.

## 0. EN SIX PHRASES

L'acte du delta 97 laissait trois suites, dont : deriver le residuel de la chaine. Je l'ai derive
seule, hors chaine et APRES COUP, sur les 22 points deja joues : l'ecart entre la chaine du moteur
et la lecture 2D serait le second ordre du meme calcul (deplacement Sigma2 de chaque site, saut au
second voisin) et les sites de l'echelle sous l'etat lu (note 022d32238a66df6b, jointe). Sur ces
points connus, q2 tient dans [0.998 ; 1.512] pour 243 etats, et le decalage d'energie des etats 2D
est rendu a 0.11 pour cent en mediane. L'operateur a ouvert le gel qui en fait un test : "ok go",
le 14/11 a 22 h 04. Ce lot porte ce gel (gel_ordre2_chaine_EA_pre_enregistrement_v1.md,
41153158190cf7f1) : douze points jamais joues, trois bandes de desaccord, une borne par bande. Si
ta certification rend 0 morsure, joue dans le meme retour.

## 1. CE QUE JE TE DEMANDE

  (a) certifier le gel, la sonde et la feuille ;
  (b) si 0 morsure : jouer la sonde aux seize points (W2 est facultatif, section 16 du gel), puis
      la feuille, et rendre le JSON de la sonde, le verdict et les journaux ;
  (c) si morsure : ne rien jouer ; je corrige par hunks.
  L'essai a blanc aux deux ancres (points connus) se rejoue si tu le veux.

## 2. CE QUI VIENT DE TOI, ET OU C'EST

  R-1 (ta certification du gel precedent : mon selftest ne tenait pas la table du gel)
       Le selftest ne lit plus ATTENDUS ni ANCRES : il porte sa propre copie de la section 4,
       tapee a part (TEMOIN_SECTION_4, TEMOIN_ANCRES, TEMOIN_CANONS). Mon banc altere chaque champ
       de chaque ligne de la table, les references d'ancre, les bornes, l'ordre et les limites des
       bandes, les deux canons : 131 alterations, 131 mordues. Ton banc reste le bienvenu.
  R-2 (un seul etat fait tomber un point, sans marge de bruit)
       La borne porte une marge d'un plancher sur la lecture 2D (section 6), et la feuille rend
       la lecture SANS marge avec le verdict : les etats que la marge a gardes, nommes, et le
       verdict que la borne nue aurait rendu (section 11). Ton bruit de fils, 7.32e-14, est sous
       ce plancher, 1.33e-13.
  R-3 (le gel citait "hors registre" des actes deposes)
       J'ai releve la tete du registre avant d'ecrire : 79e77d2. Tout ce qui y est se cite a son
       chemin de registre ; mon releve relit ces huit canons dans le clone (controle R03).
  R-4 (l'ouverture n'est pas verifiable sur piece)
       Toujours vrai ; le gel le dit en section 0, et l'operateur l'atteste ou non.
  O-1 (la batterie n'etait sur aucune piece)
       Si quelque chose de la machine pese sur le run, dis-le sur une piece du lot de resultat.

## 3. CE QUI EST A MA PLUME ET OUVERT A LA MORSURE

  - LE BLOC (chaine_ordre2_bloc_machine1_v1.py, 7cd5977bc27bebc1), le coeur du lot. A reprendre de
    ton cote, sans me croire : la forme symetrique au second ordre ; l'argument de parite qui ne
    laisse que deux termes ; les 34 sauts de x^5 hors du canal ; l'exclusion du saut du canal comme
    seconde jambe de u_m (sinon le chemin par le site voisin, que la chaine traite deja, serait
    compte deux fois) ; les denominateurs d'energie libre ; les sites m < 0 ; le signe de dE.
    Controles que j'ai : il redonne les 262 valeurs de la note au bit pres ; Sigma2(0) est celui
    du moteur a 5e-15 pres (note, section 5) ; sur les points connus il rend l'energie des etats
    2D a un pour mille, ce que les largeurs n'ont pas regle. Aucun n'est un controle independant
    de ma plume.
  - LA VALEUR LUE : Gamma_flux et non -2 Im E (gel, section 2 (iv)). Meme quantite, autre
    arithmetique ; les bornes ont ete posees sur des nombres lus a -2 Im E. Les deux sont
    consignes, et leur ecart est une lecture declaree.
  - LES BANDES ET LES BORNES, posees apres avoir vu les points connus et la grille (section 2).
    J'avais ecrit a l'operateur, avant de calculer la grille, 0.85 pour "un facteur 1.6 jusqu'a
    0.12". Je ne le crois plus au coin (2.12, facteur 2/3). C'est mon defaut D-G1-3, refait le
    meme jour ; il est dans le gel et je l'ecris a l'operateur.
  - LE CHOIX DES POINTS, fait sur la garde et les chaines seules : quatre par bande, deux de
    chaque cote de 2.00, quatre facteurs par bande ; les coins M4, L4 et L2 sont pris.
  - LA COMPARAISON AU PIRE ETAT (section 8), choisie apres avoir vu que la comparaison des
    medianes est fausse a deux points connus (H6, J1). Le gel le dit en section 2 (v).
  - LA TOLERANCE D'ENERGIE, 0.01, pour un plus grand ecart connu de 0.0050.
  - LA GARDE G-8 : references calculees par moi seule, sans decomposition 2D. Sa tolerance, 1e-3,
    se compare a l'ecart entre nos deux machines sur la chaine du moteur aux memes etats : 2.2e-05
    au plus (journal ecart_machines_ancres).
  - LE RATTACHEMENT A LA LITTERATURE des deux termes du second ordre : non verifie sur texte.
  - La coherence du texte et des scripts : mon releve relit les nombres et les canons du gel dans
    leurs sources par 24 controles, 0 morsure, et mord sur 28 copies alterees du gel sur 28 ; pas
    plus.
  La sonde differe de la sonde du registre (940a21b1d562bb49) par six hunks, joints et
  rejouables ; un des six insere le bloc tel quel. Les mesures 2D, la chaine du moteur et la garde
  consignee ne sont pas touchees : mon essai retrouve a l'identique les 737 champs de l'essai du
  gel precedent. Dans la feuille, les neuf premiers criteres de motif_exclusion sont ceux de la
  feuille du registre (0a760e3a244e547d), au caractere pres (controle R24) ; le reste est neuf.

## 4. COMMANDES

    python -P lecture_ordre2_machine1_v1.py --selftest
    python -P sonde_ordre2_machine1_v1.py <moteur v17> essai.json A1 A2          (facultatif)
    python -P lecture_ordre2_machine1_v1.py --essai essai.json
    python -P sonde_ordre2_machine1_v1.py <moteur v17> sonde_ordre2.json
    python -P lecture_ordre2_machine1_v1.py sonde_ordre2.json verdict_ordre2.json
  Sans W2 : la quatrieme commande, suivie des quinze identifiants
    C1 C2 C3 C4 M1 M2 M3 M4 L1 L2 L3 L4 A1 A2 W1
  Le run : 48 decompositions, boites de N = 54 a N = 74 pour quinze points, N = 89 pour W2 (une
  matrice de 7921 lignes, de l'ordre de 1 Go par tableau complexe). A l'echelle de la boite
  puissance six et de ton run precedent : de l'ordre de 3100 secondes pour les quinze premiers
  points, de 1500 pour W2. Chez moi (levier X86_V4) un point a N = 60 prend 265 s. La chaine
  d'ordre 2 ne coute presque rien a cote des decompositions. La sonde reecrit son JSON apres
  chaque point ; elle ne reprend pas : un run interrompu se rejoue en entier et se declare.

## 5. CE QUE JE DECLARE

  Je n'ai diagonalise le H 2D a aucun des quatorze points C1 a C4, M1 a M4, L1 a L4, W1, W2. J'y
  ai calcule la garde du moteur, la chaine du moteur et la chaine d'ordre 2, seules (conception,
  garde_aux_points, chaines_aux_points). J'ai joue la sonde a A1 et A2, et rien d'autre.

## 6. HORS DE CE LOT

  Rien n'attend de depot de mon cote. La note 022d32238a66df6b et son tableau par etat sont
  joints pour lecture ; ils ne sont pas certifies et ne te demandent rien d'autre que ce que le
  gel en cite. Les scripts de la note sont a ma disposition si tu veux la rejouer.

## 7. PIECES (convention B ; le manifeste du lot porte les empreintes brutes)

  gel_ordre2_chaine_EA_pre_enregistrement_v1.md            41153158190cf7f1   LE GEL
  gel_ordre2_chaine_EA_gabarit.txt, construction_gel_ordre2_machine1_v1.py
  sonde_ordre2_machine1_v1.py                              24315c52b234319c   mesure, ne juge pas
  construction_sonde_ordre2_machine1_v1.py                 ses six hunks sur 940a21b1d562bb49
  chaine_ordre2_bloc_machine1_v1.py                        7cd5977bc27bebc1   le bloc
  essai_bloc_machine1_v1.py / .log                         le bloc contre la note ; flux et -2 Im E
  lecture_ordre2_machine1_v1.py                            elle juge et ne mesure pas
  lecture_selftest_machine1.log                            160 cas, 160 tenus
  banc_feuille_ordre2_machine1_v1.py / .log                table 131 sur 131 ; code 108 sur 109
  conception_points_ordre2_machine1_v1.py / .log           les chaines seules, 168 points
  garde_aux_points_ordre2_machine1_v1.py / .log            la garde et la boite aux seize points
  chaines_aux_points_ordre2_machine1_v1.py / .log          les chaines de la sonde, 512 sites
  reference_ancres_ordre2_machine1_v1.py / .log            les references de G-8
  ecart_machines_ancres_machine1_v1.py / .log              pour la tolerance de G-8
  sonde_essai_ancres_machine1.json / .log, lecture_essai_ancres_machine1.log   essai a blanc
  releve_gel_ordre2_machine1_v1.py / .log                  24 controles, 0 morsure
  contre_epreuve_releve_gel_ordre2_machine1_v1.py / .log   28 copies alterees, 28 mordues
  diff_sonde_sur_940a21b1d562bb49.txt
  note_machine1_residuel_chaine_EA_second_ordre_2026-11-14_v1.md   022d32238a66df6b   la note
  ordre2_par_etat_v3.json                                  c4ff0e3030b89c0c   son tableau
  fabrique_lot_machine1_v2.py

-- FIN POUR_MACHINE2_gel_ordre2_machine1_v1 --
