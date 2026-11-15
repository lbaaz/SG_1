DELTA nn -- LA CHAINE E-A AU SECOND ORDRE : RUN DES 14 ET 15/11/2026 SOUS LE GEL 41153158190cf7f1.
VERDICT : L'ORDRE 2 TIENT. COMPARAISON : L'ORDRE 2 FAIT MIEUX PARTOUT. ENERGIES : L'ENERGIE TIENT.
-- PROJET, VERSION 1
(plume machine 1 ; run et certification machine 2 ; a contresigner par machine 2)
=======================================================================

nn.0 POSITION
  Ce delta rend le run du gel "la chaine E-A au second ordre". Sa question : completee par son
  second ordre (le deplacement Sigma2 de chaque site, un saut au second voisin) et par ses sites
  bas, la chaine E-A rend-elle la LECTURE de E-B a k = 3, sur douze points jamais joues, dans des
  bornes ecrites d'avance : 1.25 jusqu'a |delta| = 0.06, 1.6 jusqu'a 0.10, 2 jusqu'a 0.12 ? Reponse
  de la feuille : L'ORDRE 2 TIENT. Les trois bandes sont TENUES ; aucun des douze points ne tombe ;
  132 etats juges. Les deux issues propres du gel sont L'ORDRE 2 FAIT MIEUX PARTOUT et L'ENERGIE
  TIENT.
  Ce chantier n'est pas la piste (0) : il ne requalifie pas E-B, et aucune phrase d'ici ne dit
  "largeur" sans "lue a k = 3". Il a ete ouvert par l'operateur ("ok go", le 14/11/2026 a 22 h 04, a
  machine 1) ; machine 2 ne peut pas le verifier sur piece (nn.11).
  Registre a l'ecriture : origin/main 79e77d2, plafond 97 (releve du 15/11 au matin). Aucun numero
  n'est pris ici (E18).

nn.1 PIECES (convention B)
  Au registre (79e77d2)
    scripts/m17_chaine_v17.py  82a0be882568fe0c
        le moteur ; il n'est pas modifie
    gels/gel_domaine_G1_chaine_EA_pre_enregistrement_v1.md  b59651f99e60707a
        le gel precedent
    journal/journal_delta_97_domaine_G1_chaine_EA_v1.md  e718d2db619af9b1
        son acte : la suite "deriver le residuel de la chaine" et les trois regles candidates (a),
        (b), (c)
  Hors registre, de machine 1 (lot 3bc363266957de56)
    gel_ordre2_chaine_EA_pre_enregistrement_v1.md  41153158190cf7f1
        le gel
    sonde_ordre2_machine1_v1.py  24315c52b234319c
        la sonde : elle mesure et ne juge pas
    chaine_ordre2_bloc_machine1_v1.py  7cd5977bc27bebc1
        le bloc de la chaine d'ordre 2, insere tel quel dans la sonde
    lecture_ordre2_machine1_v1.py  0dc8241c680eb1ff
        la feuille : elle juge et ne mesure pas
    note_machine1_residuel_chaine_EA_second_ordre_2026-11-14_v1.md  022d32238a66df6b
        la note hors chaine, apres coup, que ce gel met a l'epreuve ; non certifiee
  Hors registre, de machine 2
    lot de certification  59a583a640112891
        certification du gel, de la sonde, de la feuille et du bloc, AVANT le run
      POUR_MACHINE1_certification_gel_ordre2_machine2_v1.md  e25286235e5474f5
          la note : 0 morsure, six reserves
      ordre2/controles_gel_ordre2_machine2_v1.log  830b16e74f339795
          ses 22 controles de lecture
      ordre2/bloc_independant_machine2_v1.log  2adf855b5aba5f50
          le bloc recalcule a part, 17 controles
      ordre2/garde_et_boites_machine2_v1.log  9dd0fc58e38936e9
          la garde et la boite recalculees aux seize points
      ordre2/banc_feuille_ordre2_machine2_v1.log  04e47095995210c4
          le banc de la feuille et son lecteur independant
      ordre2/compare_essais_16fils_machine1.log  33585399bf8c0d9b
          son essai aux ancres contre celui de machine 1
    lot de resultat  6dfdfe8fd0b8eaad
        le run, sa lecture, les controles de machine 2
      ordre2/sortie/sonde_ordre2.json  10887c60d5f55bcf
          les mesures : seize points, 224 etats
      ordre2/sortie/verdict_ordre2.json  4195583a970eaf70
          le verdict rendu par la feuille sur BOCAL4
      ordre2/sortie/lecture_ordre2.log  c8a03a393d95cebf
          son journal
      ordre2/sortie/console_ordre2.log  3e0fceb4dec89ba7
          le journal du pilote : heures et codes de retour
      ordre2/sortie/sonde_ordre2.log  a68ab28afb75e54e
          le journal de la sonde : boites et durees
      POUR_MACHINE1_resultat_ordre2_machine2_v1.md  e10c02883d9b20a9
          la note de machine 2
      ordre2/sortie/relecture_independante_machine2.log  81d9151e2595f712
          son lecteur independant, 0 ecart
      ordre2/sortie/compare_run_essai_ancres_machine2.log  64c3a19b08afb862
          les ancres du run contre son essai
      ordre2/sortie/stabilite_cascade_machine2.log  172c031d05d5f56a
          le verdict sous le bruit des fils
      ordre2/sortie/sensibilite_bruit_machine2.log  a48503026fecbb7d
          le meme, a des multiples de ce bruit
      ordre2/sortie/stabilite_cascade_machine2_v1_defaut.log  0db441d7922f03b2
          le defaut de bord de son premier outil
      ordre2/sortie/etat_machine_machine2.log  4d6ca2940b76beff
          la batterie et l'horloge du processeur a la fin du run
  De ce lot
    verdict_rejoue_machine1.json  4195583a970eaf70
        la feuille rejouee par machine 1 sur le JSON de machine 2 : le meme canon
    lecture_rejouee_machine1.log  616799ab3deb89c2
        son journal

nn.2 CE QUI A ETE JOUE, ET PAR QUI (E19)
  Machine 1, avant le lot de resultat : aucune decomposition 2D aux quatorze points neufs ; la garde
  du moteur et les deux chaines, seules ; la sonde aux deux ancres, points connus. Apres : la
  feuille, rejouee sur le JSON de machine 2, et rien d'autre. Machine 1 n'a joue la sonde a aucun
  point juge ni temoin.
  Machine 2 : la certification d'abord (22 controles, 0 morsure ; le bloc recalcule a part, 17
  controles, 0 morsure), puis UN run, par un pilote qui verifie les quatre canons : sonde lancee le
  14/11 a 23 h 26, finie le 15/11 a 0 h 41, 4524 secondes, code 0 ; les seize points dans l'ordre du
  gel, W2 en dernier, 14 etats chacun ; aucun arret, aucune reprise, aucun point rejoue ; puis la
  feuille (selftest 160 sur 160, code 0). BOCAL4, Windows AMD64, python 3.11.9, numpy 2.2.6, 16
  coeurs, variables de fils non fixees.
  Le run a ete joue SUR BATTERIE, et cette fois c'est sur une piece : batterie a 100 pour cent au
  lancement, a 62 a la fin, processeur a 2516 MHz pour un maximum de 3801 (journal de l'etat de la
  machine). Le gel annoncait de l'ordre de 3100 secondes pour quinze points et 1500 pour W2 ; le run
  en a pris 3177 et 1346. Durees par point, en secondes : C1 377, C2 283, C3 91, C4 107, M1 153, M2
  100, M3 460, M4 316, L1 86, L2 155, L3 102, L4 464, A1 144, A2 157, W1 183, W2 1346.
  Rejeu de machine 1 : le verdict rejoue est, objet JSON pour objet JSON, celui que machine 2 a
  rendu ; les deux fichiers ont le meme canon 4195583a970eaf70. Le lecteur independant de machine 2,
  ecrit du texte du gel, lit la meme chose a chaque point (0 ecart). Aux deux ancres, le run rend au
  bit les valeurs de l'essai de sa certification (28 etats, chaines comprises).

nn.3 LES GARDES
  Aucune ne mord. G-1 et G-7 : le moteur et la sonde lus au JSON sont aux canons 82a0be882568fe0c et
  24315c52b234319c. G-2, G-3 : les seize points sont presents, chacun avec son role, son w2, son
  facteur, g = facteur x regle, et 14 etats. G-4 : les etats (7,2) de A1 et (8,2) de A2 rendent la
  lecture du run de M17 au bit (ecart relatif 0, tolerance 1e-2). G-5 : selftest 160 sur 160, sur
  BOCAL4 et chez machine 1. G-6 : la garde du moteur consignee porte aux seize points le statut de
  la table, et ses D1 et c_max en different de moins de 1e-6 (tolerance 5e-5) ; elle dit HORS
  DOMAINE a M4, L1, L2, L4, W1, W2. G-8 : aux deux memes etats, la chaine d'ordre 2 de BOCAL4 rend
  les references de machine 1 a 8e-11 pres pour Gamma_flux (tolerance 1e-3) et a 3e-12 pres pour dE
  (tolerance 1e-6).

nn.4 LES SEIZE POINTS (q = Gamma de chaine / Gamma_2D lue a k = 3, sur les etats juges)
  L'ordre 2 : q2 lu a Gamma_flux. Le palier est la plus petite des bornes 1.25, 1.6, 2 qui contient
  tous les etats juges.
    id  w2       fact  delta  bande      borne  juges   q2 min    med    max   palier  statut
    C1  197/100  2/3   -0.03  proche     1.25     8     1.002  1.042  1.055   1.25    TENU
    C2  97/50    3/4   -0.06  proche     1.25    11     1.044  1.099  1.136   1.25    TENU
    C3  203/100  3/2   +0.03  proche     1.25    14     1.015  1.021  1.032   1.25    TENU
    C4  103/50   4/3   +0.06  proche     1.25    13     1.067  1.076  1.091   1.25    TENU
    M1  193/100  1     -0.07  moyenne    1.6     11     1.075  1.120  1.140   1.25    TENU
    M2  48/25    4/3   -0.08  moyenne    1.6     13     1.041  1.108  1.144   1.25    TENU
    M3  207/100  2/3   +0.07  moyenne    1.6      8     1.114  1.128  1.153   1.25    TENU
    M4  21/10    3/4   +0.10  moyenne    1.6      9     1.356  1.388  1.447   1.6     TENU
    L1  189/100  4/3   -0.11  lointaine  2       14     1.093  1.181  1.226   1.25    TENU
    L2  47/25    1     -0.12  lointaine  2       10     1.171  1.229  1.314   1.6     TENU
    L3  211/100  3/2   +0.11  lointaine  2       12     1.273  1.306  1.350   1.6     TENU
    L4  53/25    2/3   +0.12  lointaine  2        9     1.508  1.579  1.679   2       TENU
    A1  39/20    1     -0.05  ancre      -       11     1.038  1.062  1.080   1.25    LU
    A2  41/20    1     +0.05  ancre      -       12     1.035  1.053  1.064   1.25    LU
    W1  107/50   1     +0.14  temoin     -       11     1.513  1.689  2.047   aucun   LU
    W2  209/100  1/2   +0.09  temoin     -        3     NON LISIBLE (moins de 6 etats juges)
  La chaine du moteur (q1, lu a -2 Im E), les deux pires ecarts (le plus grand |ln q| d'un etat
  juge) et le plus grand ecart d'energie :
    id   q1 min     med     max   pire o2  pire o1  comparaison   ecart d'energie  energie
    C1    0.444   0.600   0.676    0.053    0.811   MIEUX         2.69e-04         TENUE
    C2    0.415   0.622   0.773    0.128    0.880   MIEUX         1.18e-03         TENUE
    C3    1.063   1.178   1.250    0.032    0.223   MIEUX         3.28e-04         TENUE
    C4    1.377   1.620   1.678    0.087    0.518   MIEUX         1.36e-03         TENUE
    M1    0.573   0.813   0.970    0.131    0.557   MIEUX         1.59e-03         TENUE
    M2    0.653   0.846   1.064    0.135    0.425   MIEUX         2.53e-03         TENUE
    M3    1.838   2.160   2.501    0.142    0.917   MIEUX         1.12e-03         TENUE
    M4    3.840   4.638   5.620    0.370    1.726   MIEUX         2.41e-03         TENUE
    L1    0.712   1.030   1.394    0.203    0.339   MIEUX         4.60e-03         TENUE
    L2    0.810   1.052   1.350    0.273    0.300   MIEUX         3.40e-03         TENUE
    L3    2.923   3.385   4.027    0.300    1.393   MIEUX         4.27e-03         TENUE
    L4    7.416   8.804  10.551    0.518    2.356   MIEUX         3.21e-03         TENUE
    A1    0.587   0.758   0.882    0.077    0.533   MIEUX         8.12e-04         TENUE
    A2    1.292   1.505   1.629    0.062    0.488   MIEUX         7.77e-04         TENUE
    W1    8.058  10.796  15.533    0.716    2.743   MIEUX         5.59e-03         TENUE
  Aux douze points juges : 168 etats, 132 juges, 36 exclus (31 sous dix planchers, 4 a J flou, 1 a
  barriere vide). A W2 : 3 etats juges, 11 exclus sous dix planchers.

nn.5 LE VERDICT
  Chaque bande a ses quatre points lisibles et aucun ne tombe : PROCHE, MOYENNE et LOINTAINE sont
  TENUES, et la cascade rend L'ORDRE 2 TIENT. Plus grand q2 par bande : 1.136 pour une borne de
  1.25, 1.447 pour 1.6, 1.679 pour 2 ; ils sont a C2, M4 et L4. L'ecart est d'un seul cote : le plus
  petit q2 des 132 etats juges est 1.002 (a C1), le plus grand 1.679 (a L4).
  La lecture SANS MARGE (gel, section 11) rend le meme verdict : aucun etat n'est garde par la marge
  d'un plancher, la borne nue les contient tous.
  Ce que le gel autorise a ecrire (section 13), et rien de plus : sur douze points neufs, aux
  facteurs de 2/3 a 3/2, la chaine completee par son second ordre et ses sites bas a rendu la
  lecture de E-B a k = 3 a un facteur 1.25 pres pour |delta| <= 0.06, 1.6 pres jusqu'a 0.10, 2 pres
  jusqu'a 0.12. C'est un domaine, borne par bande, de cette chaine-la contre cette lecture-la.

nn.6 LA COMPARAISON ET LES ENERGIES
  Comparaison au pire etat : les douze points sont MIEUX. La chaine du moteur va, sur les memes 132
  etats, de q1 = 0.415 a q1 = 10.551 ; l'ordre 2 de 1.002 a 1.679. Les trois points ou l'ecart entre
  les deux pires est le plus mince : L2 (0.273 pour l'ordre 2 contre 0.300), L1 (0.203 contre
  0.339), C3 (0.032 contre 0.223). q1 reste lu a -2 Im E, le moteur n'etant pas modifie ; machine 2
  mesure que cette valeur differe de 0.2 a 0.3 pour cent d'une machine a l'autre aux etats juges (sa
  reserve R-2) : l'ecart de L2, 0.027 en logarithme, est une dizaine de fois plus large.
  Ce que le gel autorise a ecrire : le second ordre est ce qui manquait a la chaine du moteur, aux
  points lus.
  Energies : les douze points sont tenus. Plus grand ecart relatif entre le decalage d'energie de la
  chaine d'ordre 2 et celui de l'etat 2D : 0.0014 a la bande proche, 0.0025 a la moyenne, 0.0046 a
  la lointaine (a L1), pour une tolerance de 0.01. Ce que le gel autorise a ecrire : la chaine
  d'ordre 2 rend aussi le decalage d'energie des etats, a un pour cent pres, ce que les largeurs ne
  controlent pas.
  Ce que ce controle tient, et ce qu'il ne tient pas (certification de machine 2, bloc recalcule a
  part) : contre l'energie exacte du H_2D sans absorbeur, a g, g/2 et g/4, l'erreur relative de la
  chaine d'ordre 2 est divisee par quatre a chaque moitie de g (7.50e-05, 1.84e-05, 4.59e-06 a
  l'etat d'ancre de A1) ; a g, l'ordre 1 est a 4.37e-02, "u seul" a 4.40e-02, "Sigma2 seul" a
  4.40e-04. L'energie tient donc Sigma2 ; elle ne tient pas le saut au second voisin, qui n'y entre
  qu'a l'ordre suivant. Ce saut est tenu autrement : machine 2 le retrouve a 5e-13 pres par une
  somme sur les 36 sauts de x^5, et a 5e-15 pres en le lisant sur la matrice H_2D du moteur, sans
  enumerer aucun saut.

nn.7 LECTURES SANS VERDICT (gel, section 11)
  Le palier atteint est en nn.4 : 1.25 a huit points juges, les quatre de la bande proche, M1, M2,
  M3 et L1 ; 1.6 a M4, L2 et L3 ; 2 a L4.
  La loi apres coup de la note, ln(q2) = 2.87 delta^2 m_bord : la mediane de q2 / loi va de 0.889
  (L2) a 1.037 (M4 et L3). Elle surestime au point le plus bas, 1.88.
  L'arithmetique : le plus grand ecart relatif entre -2 Im E et Gamma_flux de la chaine d'ordre 2, a
  un point juge, est 0.013 (L4).
  Les ancres, points connus : q2 de 1.038 a 1.080 a A1, de 1.035 a 1.064 a A2.
  Le temoin W1 (2.14, facteur 1, hors enonce) : 11 etats juges, q2 de 1.513 a 2.047 ; sept sont
  au-dela de 1.6, deux au-dela de 2 ; aucun palier. Il est MIEUX (0.716 contre 2.743) et tenu en
  energie (0.0056).
  Le temoin W2 (2.09, facteur 1/2, hors enonce) a ete joue, boite de 89, 1346 secondes sur batterie,
  et il est NON LISIBLE : 3 etats juges sur 14, les 11 autres sous dix planchers. L'acte n'en lit
  rien ; rien n'est appris au facteur 1/2.
  Le bruit des fils (machine 2, sa reserve R-3 ; bruit de la cible 7.32e-14 en absolu sur
  Gamma_2D(3)) : au bruit mesure, aucun statut de point ne change et un seul verdict est possible.
  Un etat de L4 peut entrer ou sortir des etats juges ; le point est TENU dans les deux cas. Le
  verdict est inchange jusqu'a sept fois ce bruit (5.12e-13) ; a partir de huit fois (5.86e-13), NE
  TIENT PAS, TIENT JUSQU'A 0.10 et TIENT sont tous possibles. Ce bruit a ete mesure aux boites de 60
  et 61 ; il ne l'a pas ete a celles de 73 et 74 (C1, M3, L4), le gel interdisant de rejouer un
  point.

nn.8 LES ANNONCES DE LA PLUME, COMPTEES (gel, section 12)
  A-1 : la plume donnait 0.45 a L'ORDRE 2 TIENT, 0.27 a TIENT JUSQU'A 0.10, 0.10 a TIENT JUSQU'A
  0.06, 0.08 a NE TIENT PAS, 0.04 a NON LISIBLE, 0.06 a NON CONCLUANT D'INSTRUMENT. L'issue qu'elle
  disait la plus probable est sortie.
    A-2  (0.85) la bande PROCHE est TENUE                      VRAIE
    A-3  (0.80) la bande MOYENNE est TENUE                     VRAIE
    A-4  (0.60) la bande LOINTAINE est TENUE                   VRAIE
    A-5  (0.70) L2 est TENU                                    VRAIE  (plus petit q2 1.171)
    A-6  (0.80) L4 est TENU                                    VRAIE
    A-6  (0.65) son plus grand q2 est entre 1.5 et 1.9         VRAIE  (1.679)
    A-7  (0.80) M4 est TENU                                    VRAIE
    A-7  (0.65) son plus grand q2 est entre 1.35 et 1.55       VRAIE  (1.447)
    A-8  (0.85) L'ORDRE 2 FAIT MIEUX PARTOUT                   VRAIE
    A-9  (0.90) L'ENERGIE TIENT                                VRAIE
    A-9  (0.70) le plus grand ecart d'energie est < 0.006      VRAIE  (0.0046, a L1)
    A-10 (0.70) a chaque point le plus petit q2 est >= 0.95    VRAIE  (le plus petit : 1.002, a C1)
    A-11 (0.60) la mediane de q2 / loi est entre 0.93 et 1.15  FAUSSE (L2 : 0.889)
    A-12 (0.75) W1 a un etat juge hors de 1.6                  VRAIE  (sept sur onze)
    A-12 (0.70) tous ses etats juges sont sous 2.5             VRAIE  (le plus grand : 2.047)
    A-13 (0.65) W2 est joue et lisible                         FAUSSE (joue, 3 etats juges)
    A-14 (0.65) -2 Im E et Gamma_flux a moins de 0.05          VRAIE  (le plus grand : 0.013, a L4)
    A-15 (0.95) la garde G-4 tient                             VRAIE
    A-15 (0.93) la garde G-8 tient                             VRAIE
    A-15 (0.97) la garde G-6 tient                             VRAIE
  18 annonces jugees sur 20 sont vraies ; les deux fausses sont A-11 (la loi apres coup, a L2) et
  A-13 (W2 n'est pas lisible). La condition de A-5 et les deux sous-annonces de A-13 ne sont pas
  jugees. La somme des probabilites annoncees est 15.2 pour 18 vraies : ces annonces ne sont pas
  independantes, presque toutes tiennent a la meme question, et la plume n'en tire aucune phrase de
  calibrage.

nn.9 DEFAUTS ET RESERVES
  D-O2-1 (m1) : la plume a ecrit a l'operateur, avant de calculer la grille, 0.85 pour "un facteur
    1.6 jusqu'a |delta| = 0.12". Le gel le dit (section 2 (iii)). Le run le dement : le palier de L4
    est 2, son plus grand q2, 1.679, est au-dela de 1.6. C'est le defaut D-G1-3 du delta 97, refait
    le meme jour.
  D-O2-2 (m1 ; reserve R-1 de machine 2) : le selftest de la feuille laisse passer 22 des 115
    alterations d'une ligne que machine 2 lui oppose ; son banc en mord 20, les deux dernieres etant
    equivalentes. La table est tenue (131 alterations sur 131), ce que la regle candidate (a)
    demandait ; le reste ne l'est qu'en partie : les tolerances de G-8, des bords d'inegalite, des
    lectures declarees. Ce sont des trous du selftest, pas des defauts de la feuille : le lecteur
    independant de machine 2 et la feuille s'accordent sur 4000 sondes synthetiques, et sur le run.
  D-O2-3 (m1) : W2 a coute 1346 secondes sur batterie pour 3 etats juges. La plume avait estime sa
    lisibilite sur les 32 sites voisins de la graine, pas sur les 14 etats que la sonde retient ;
    elle annoncait 0.65 (A-13).
  D-O2-4 (m1 ; reserve R-4 de machine 2) : deux chiffres de la note different de ceux que machine 2
    recalcule : 7.00 pour 6.987 (repris par le gel, section 2 (i)), et 241 etats sur 243 dans un
    facteur 1.5 pour 242. Ils viennent de l'arrondi de -2 Im E aux plus petites largeurs ; rien ne
    s'y appuie.
  D-O2-5 (m1) : la note ecrit que les energies "preferent la somme des deux termes a chacun pris
    seul". Le controle de machine 2 (nn.6) montre que l'energie tient Sigma2 et non le saut au
    second voisin. La phrase de la note est trop forte.
  R-2 (m2) : -2 Im E de la chaine du moteur s'arrondit d'une machine a l'autre, Gamma_flux non
    (1e-9). Le choix de Gamma_flux pour q2 tient ; q1 reste a -2 Im E (nn.6).
  R-3 (m2) : la marge d'un plancher vaut 1.7 fois le bruit qu'elle mesure sur Gamma_2D(3) ; le
    verdict, lui, tient jusqu'a sept fois ce bruit (nn.7).
  R-5 (m2) : l'ouverture n'est pas verifiable sur piece par machine 2 (nn.11).
  R-6 (m2) : elle ne verifie ni le rattachement des deux termes a la litterature, ni la note
    d'anteriorite, ni les choix de la plume (bandes, bornes, points, comparaison au pire etat,
    tolerance d'energie) : ils sont ecrits d'avance, pas valides.
  De machine 2, declares par elle : six de ses controles ont mordu a ses premiers jets, par sa
    faute, sans toucher au gel ; son premier outil de lecture sous le bruit avait un defaut de bord,
    qu'elle a corrige par une version derivee, la premiere restant jointe.

nn.10 CE QUE LE RESULTAT CHANGE A CE QUI ETAIT ECRIT
  Note 022d32238a66df6b : elle etait une lecture apres coup de 22 points connus. Sur douze points
  neufs, dans des bornes ecrites avant le run, sa lecture tient ; l'acte en ecrit ce que nn.5 et
  nn.6 autorisent. Sa loi apres coup reste une description : elle manque a L2. Deux de ses chiffres
  et une de ses phrases sont corriges (D-O2-4, D-O2-5).
  Delta 97, nn.11 (iv) : la suite "deriver le residuel de la chaine" est faite, et mise a l'epreuve.
  Ce que cet acte decrivait sans l'expliquer, un rapport qui change de sens a 2.00, croit avec le
  desaccord et depend du facteur, est, aux points lus, le second ordre de la chaine. Son verdict, LA
  GARDE NE TIENT PAS, n'est pas touche.
  Gel 41153158190cf7f1, section 2 (ii) : la plume supposait un second canal vers 1.85. A L2, le
  point le plus bas (1.88), aucun etat n'est trop bas : le plus petit q2 y est 1.171. Rien n'est dit
  de 1.85.
  La lecture de E-B garde son statut : elle n'est pas qualifiee. Deux calculs aux absorbeurs
  differents s'accordent dans les bornes du gel a douze points ; cet acte n'en tire rien sur la
  lecture elle-meme. Les verdicts PAS DE SIGNAL de M17, NON QUALIFIE de la nuit bis, TENU EN PARTIE
  et LA GARDE NE TIENT PAS ne sont pas touches.

nn.11 A ARBITRER PAR L'OPERATEUR
  (i) Le numero (E18) et le depot.
  (ii) L'ouverture. Seul l'operateur peut attester qu'il a ouvert ce chantier le 14/11 a 22 h 04 ;
      son message de depot le dit ou non. Machine 2 a joue parce que l'envoi le demandait et que
      l'operateur l'a porte.
  (iii) La suite. Cet acte n'en propose aucune comme decidee. Il en existe : porter l'ordre 2 dans
      le moteur, ce qui demande une nouvelle version ; calculer l'ordre suivant, le residu etant
      d'un seul cote, croissant avec le desaccord, et non explique ; eprouver le facteur 1/2, que W2
      n'a pas rendu lisible, ou le desaccord au-dela de 0.12, ou W1 va jusqu'a 2.047 ; reprendre la
      piste (0) avec cette chaine pour second calcul ; ou rien, ce verdict se deposant tel quel.
  (iv) Les regles. Cet acte n'en propose aucune (nn.12).

nn.12 REGLES CANDIDATES SOUS (X)
  Aucune regle nouvelle ; trente-quatre attendent la revue. Pour cette revue, ce que les trois
  regles candidates du delta 97, appliquees ici sans etre adoptees, ont donne :
  (a) le selftest porte sa propre copie de la table : la table est tenue (131 sur 131), le reste du
      selftest ne l'est pas (D-O2-2) ; ce qui tient la feuille, c'est le banc de la machine qui
      certifie.
  (b) la borne porte une marge d'un plancher et la lecture sans marge est rendue : ici la marge n'a
      garde aucun etat, et machine 2 mesure que le verdict tient jusqu'a sept fois le bruit.
  (c) la tete du registre a ete relevee, et le gel n'a rien cite a tort hors registre ; mais la
      plume a encore conseille un gel avec un chiffre avant de calculer (D-O2-1).

nn.13 LE CANAL
  Lots echanges pour ce chantier (canons) : machine 1 -- le gel et ses instruments
  3bc363266957de56 ; machine 2 -- la certification 59a583a640112891, le resultat 6dfdfe8fd0b8eaad.
  Les enveloppes qui les ont portes ne sont pas des lots et ne se citent pas.

nn.14 CE QUE CE DELTA NE FAIT PAS
  Il n'affirme aucune largeur intrinseque et ne dit pas que la chaine est "qualifiee" : elle rend,
  dans des bornes dites, une lecture qui ne l'est pas. Il ne dit rien hors des facteurs de 2/3 a
  3/2, de la fraction 0.70, du canal 2:1 de x^5 et de |delta| de 0.03 a 0.12. Il ne dit pas d'ou
  vient le residu. Il ne rejoue aucun point, ne relit sous aucune autre borne, aucune autre bande,
  aucun autre critere, aucune autre population (gel, section 14). Il ne modifie pas le moteur. Il ne
  rouvre pas la piste (0). Il ne prend aucun numero, n'adopte aucune regle, n'edite aucune piece
  citee (PB-1).

nn.15 PIECES DU LOT
  journal_delta_nn_ordre2_chaine_EA_v1.md               cet acte
  ecrire_acte_ordre2_machine1_v1.py                     le script qui pose nombres et canons
  verdict_rejoue_machine1.json, lecture_rejouee_machine1.log   la feuille rejouee par machine 1
  releve_acte_ordre2_machine1_v1.py / .log              le releve de sortie de machine 1
  contre_epreuve_releve_acte_ordre2_machine1_v1.py / .log   ce releve, sur des copies alterees
  POUR_MACHINE2_acte_ordre2_machine1_v1.md              la note d'accompagnement
  fabrique_lot_machine1_v2.py
  Perimetre : la feuille du contresignataire, sur ce texte ; les entrants sont ceux de nn.1.

-- FIN journal_delta_nn_ordre2_chaine_EA_v1 --
