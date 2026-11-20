GEL "PONT" -- SECONDE PARTIE : L'INSTRUMENT, LES ENONCES, LES TOLERANCES
pre-enregistrement, machine 1, 2026-11-17, version 1. Classe A. ASCII, lignes de 100 colonnes.

0. STATUT
  Cette piece est la seconde partie du gel "pont". La premiere (canon 735ce41be200c5cd) a fixe le
  tirage et l'eligibilite ; machine 2 l'a certifiee (lot acfecb6da73f20ae) ; l'operateur a donne la
  graine. Cette piece fixe, AVANT toute 2D aux cellules tirees : les six cellules, ce que la chaine
  seule y predit, les deux sondes et les trois feuilles, les enonces et leurs tolerances, ce que
  vaut une cellule illisible, ce que chaque issue engage, et les annonces de la plume.
  RIEN N'EST JOUE. Aucune 2D du systeme a fantome, de quelque sorte, n'a ete calculee par machine 1
  a w2 = 397/200 ni a w2 = 2019/1000. Tout ce qui est calcule et lu ici en 2D l'est au point
  sacrifie w2 = 101/50, qui n'est pas candidat ; un essai du code, a l'aveugle, a un autre w2 non
  candidat, est dit en section 6. Le run n'a lieu qu'apres la certification de cette piece par
  machine 2 et le feu vert ECRIT de l'operateur (E19). Machine 2 joue, une fois.
  Cette piece ne juge rien et ne depose rien.

1. SOURCES (convention B)
    735ce41be200c5cd  gel_pont_partie1_regle_tirage_pre_enregistrement_v1.md (lot de machine 1
                      55612644fc4ca279)
    acfecb6da73f20ae  lot de machine 2 : certification de la premiere partie ; sa note :
    0e7cdc94fc64f8fe  POUR_MACHINE1_certification_gel_pont_partie1_machine2_v1.md
    0c10ddbf2813d809  table_commune_pont_v1.json : la table commune, la meme des deux cotes
    dce7431e7a8b4a8c  lot de machine 2 : 32 boites fermees au point sacrifie, 3 barreaux
  Registre public lbaaz/SG_1, tete 2988237 (delta 102). Blocs deposes, executes tels quels :
    82a0be882568fe0c  scripts/m17_chaine_v17.py (le moteur)
    7cd5977bc27bebc1  scripts/chaine_ordre2_bloc_machine1_v1.py (tables d'ordre 2)
    534ba246aa3b8973  scripts/ordre3_bloc_machine1_v1.py (tables d'ordre 3)
    49a40d9098b55361  scripts/chaine_adaptee_bloc_machine1_v1.py (absorbeur adapte de la chaine)
    d5cc48f48e37af99  scripts/sonde_lecteur_gel_loi_machine1_v1.py (le bloc "LECTEUR CREUX")

2. LA GRAINE ET LE TIRAGE
  L'operateur a donne la graine a machine 1 le 17/11/2026 a 09 h 56, apres lui avoir remis la
  certification de machine 2 : 456823. Elle ne se change plus ; aucune machine ne la choisit ni ne
  la commente.
  Tirage de machine 1 sur la table commune (0c10ddbf2813d809), par tirage_pont_machine1_v1.py
  (69b8e585f57e0c1e), regle de la section 3 de la premiere partie :
    creneau MG, rang 0 : sha256("456823|MG|0") = bab2ed478849ce6c... ; modulo 8 = 3
                        -> w2 = 397/200 (1.985), ELIGIBLE, retenu
    creneau PG, rang 0 : sha256("456823|PG|0") = 7ba5f5c18c4df1e2... ; modulo 8 = 7
                        -> w2 = 2019/1000 (2.019), ELIGIBLE, retenu
  LES SIX CELLULES :
    MG3  w2 = 397/200    m = 3  g = 3.63872e-03
    MG4  w2 = 397/200    m = 4  g = 2.77765e-03
    MG5  w2 = 397/200    m = 5  g = 2.20823e-03
    PG3  w2 = 2019/1000  m = 3  g = 5.23478e-03
    PG4  w2 = 2019/1000  m = 4  g = 3.99601e-03
    PG5  w2 = 2019/1000  m = 5  g = 3.17683e-03
  Machine 2 tire de son cote, par son script. Si ses six cellules ne sont pas celles-ci : PAS DE
  GEL.

3. RECTIFICATION DE LA PREMIERE PARTIE (reserve R1 de machine 2)
  Machine 2 a certifie la premiere partie avec une reserve de redaction, R1 : le 4.4 dit "Gamma = -2
  Im(E)" sans dire que la valeur propre lue en double precision ne suffit pas a 4 et 5 barreaux. La
  reserve est fondee, et la faute est de la plume : le gel du vide portait la phrase, la premiere
  partie de ce gel l'a laissee tomber. Le 4.4 se lit AINSI : la largeur d'une variante est lue sans
  perte, par le flux 2 somme_m W_m |psi_m|^2 / somme_m |psi_m|^2 tant que Gamma / |delta| > 1e-15,
  en precision arbitraire en dessous ; c'est ce que fait le bloc depose, et ce qu'a fait le script
  de la premiere partie.
  Controle de machine 1 sur ses 48 matrices : -2 Im(E) en double precision s'ecarte de la lecture du
  bloc de 3.4e-06 au plus a 3 barreaux, 1.4e-04 a 4, 4.6e-03 a 5 ; l'etendue au vide change de plus
  de 5e-5 dans 18 cellules (2 a 4 barreaux, 16 a 5) ; aucune decision de la condition (iii) ne
  change (plus grande etendue ainsi lue : 0.0075, pour un seuil de 0.02). La piece de la premiere
  partie n'est pas retouchee.
  Pris aussi de sa note, sans changement de la regle. Sur les 48 cellules, seule la condition (v), a
  l'ecart x = 8, ecarte des cellules ; les seuils (i) a (iv) n'en lient aucune et ne sont pas
  eprouves par cette table. La table commune est citee par son canon 0c10ddbf2813d809 (format de la
  section 5), non par le JSON complet de machine 1 (d03c9ca093ea5bfc), que machine 2 dit ne pas
  reproduire a l'octet sur BOCAL4 (decisions identiques, flottants a 9e-7 pres). Controle de machine
  1 : la chaine de machine 2, ecrite depuis le texte, rend les 48 cellules avec 0 desaccord de
  couplage ecrit, 0 d'eligibilite, et un plus grand ecart de 1.8e-09 sur les grandeurs comparees
  (e_bord, etendues, logarithmes des largeurs et des densites, pas).

4. LA TABLE GELEE DES SIX CELLULES (chaine seule, aucune 2D)
  Par chaine_cellules_pont_machine1_v1.py et le bloc chaine_pont_bloc_machine1_v1.py, qui redonnent
  la table de la premiere partie aux six cellules avec un ecart de 0. G3* : plateau de la largeur au
  vide (ordre 3). Les deux etendues sont celles des dix-huit variantes de l'absorbeur adapte. Le pas
  est ln rho_2 - ln rho_3.
    cellule  m_bord  e_bord   r_c   G3*          etendue   etendue du    |pas| au
                                                 au vide   lisse, au     plus
                                                           plus
    MG3      3       0.0447   24    2.4590e-09   0.0014    0.0046        0.0690
    MG4      4       0.0595   26    5.4260e-11   0.0015    0.0074        0.0774
    MG5      5       0.0743   28    1.1262e-12   0.0026    0.0110        0.0869
    PG3      3       0.0575   24    3.1064e-09   0.0050    0.0105        0.0421
    PG4      4       0.0768   26    6.8986e-11   0.0060    0.0167        0.0418
    PG5      5       0.0961   28    1.4415e-12   0.0063    0.0219        0.0384
  ln (rho_3 |delta|), le lisse d'ordre 3 du site 0 aux douze ecarts x (en |delta|, du cote oppose au
  desaccord) :
    x      MG3      MG4      MG5      PG3      PG4      PG5
    0.05    -11.73   -15.56   -19.45   -11.73   -15.55   -19.44
    0.25    -15.91   -19.82   -23.77   -15.90   -19.80   -23.74
    0.5     -18.39   -22.39   -26.42   -18.35   -22.34   -26.36
    1       -21.68   -25.85   -30.03   -21.61   -25.76   -29.92
    1.5     -24.15   -28.48   -32.79   -24.03   -28.34   -32.64
    2       -26.21   -30.68   -35.13   -26.05   -30.50   -34.93
    3       -29.62   -34.37   -39.05   -29.38   -34.10   -38.75
    4       -32.47   -37.46   -42.36   -32.15   -37.10   -41.96
    5       -34.96   -40.17   -45.26   -34.54   -39.71   -44.77
    6       -37.19   -42.60   -47.88   -36.68   -42.04   -47.28
    7       -39.22   -44.82   -50.27   -38.62   -44.17   -49.58
    8       -41.10   -46.88   -52.49   -40.41   -46.13   -51.70
  Le pas de l'ordre 2 a l'ordre 3, aux memes ecarts :
    x      MG3      MG4      MG5      PG3      PG4      PG5
    0.05   +0.0010  +0.0009  +0.0011  +0.0023  +0.0025  +0.0029
    0.25   +0.0008  +0.0006  +0.0006  +0.0021  +0.0024  +0.0027
    0.5    +0.0003  +0.0001  -0.0001  +0.0016  +0.0020  +0.0021
    1      -0.0008  -0.0011  -0.0015  +0.0010  +0.0010  +0.0008
    1.5    -0.0025  -0.0029  -0.0036  -0.0007  -0.0007  -0.0008
    2      -0.0044  -0.0051  -0.0060  -0.0021  -0.0024  -0.0027
    3      -0.0097  -0.0113  -0.0126  -0.0064  -0.0073  -0.0076
    4      -0.0169  -0.0192  -0.0213  -0.0114  -0.0126  -0.0128
    5      -0.0262  -0.0296  -0.0329  -0.0181  -0.0192  -0.0192
    6      -0.0377  -0.0424  -0.0474  -0.0256  -0.0264  -0.0256
    7      -0.0521  -0.0584  -0.0652  -0.0337  -0.0341  -0.0325
    8      -0.0690  -0.0774  -0.0869  -0.0421  -0.0418  -0.0384
  Ces nombres sont ceux du poste de machine 1. Machine 2 les recalcule sur BOCAL4 par le meme script
  ; c'est SON fichier que ses feuilles lisent au run. A la premiere partie, nos deux chaines
  s'accordaient a 5.3e-12 pres sur les logarithmes des densites.

5. L'INSTRUMENT
  Deux sondes, qui calculent en 2D et ne lisent pas la chaine ; trois feuilles, qui ne calculent
  aucune 2D. Aucun tirage aleatoire.
  5.1 SONDE DE DENSITE (sonde_densite_2d_pont_machine1_v1.py, 38ad6aa883b6e4fa). Pour une cellule et
      un absorbeur : hamiltonien, absorbeurs et lecture du vide du bloc "LECTEUR CREUX" depose ;
      geometrie du lecteur, r_c = 2 (m + max(8, m)) + 2 ; absorbeurs A (F2, bord r_c, 80 couches), B
      (F2, r_c, 100), C (F1, r_c, 100), D (F2, r_c + 10, 80) ; boite = bord + couches. Douze
      barreaux, eta_k = |delta| 2^(-k), k = -3 a 8. A chaque barreau : l'etat-vide est lu (E_v,
      largeur, poids w0 du site (0, 0)) ; puis, a chacun des douze ecarts x, (A - E) y = e_(0,0)
      avec A = H0 + diag - i eta W et E = E_v - x delta, et rho = (eta / pi) somme_j W_j |y_j|^2.
      Derivee de la sonde de l'exploration du 17/11 (95a91f49bb5db12e) ; elle la redonne avec un
      ecart de 0 au point sacrifie (absorbeur A, k = 3).
  5.2 FEUILLE DE DENSITE (lecture_densite_2d_pont_machine1_v1.py, c5c70a9b08c3bee3). Par absorbeur
      et par ecart, la routine de PLATEAU deposee du lecteur : parmi les fenetres de cinq barreaux
      consecutifs, celle de plus petit rapport max / min ; PLATEAU si ce rapport est <= 1.05 ;
      valeur = moyenne geometrique des cinq. rho_2D(x) = exponentielle de la mediane des quatre ln
      rho. L'ecart est LISIBLE si les quatre absorbeurs ont un plateau et si l'etendue de leurs
      quatre ln rho est <= 0.02. w0 : mediane sur les absorbeurs de la mediane sur les barreaux.
      Elle rend ln R3(x) = ln rho_2D(x) - ln w0 - ln rho_3(x), et ln R2 de meme avec le lisse
      d'ordre 2.
  5.3 SONDE DE BOITE FERMEE (sonde_boite_fermee_pont_machine1_v1.py, 443940bd265c495d). Ecrite par
      machine 1 sans recopier celle de machine 2. Boite N x N sans absorbeur, H = H0 + diag du meme
      bloc. Niveau-vide : iteration inverse a decalage 0 depuis le site (0, 0) ; E_v et w0 = poids
      du site (0, 0). Fenetre : 0.05 < x < 8, x = (E_v - E) / delta. DEUX lectures par
      decalage-inversion (eigsh de scipy, factorisation creuse d'ordre COLAMD, vecteur de depart
      fixe), decalages E_v - 2.5 delta et E_v - 5.5 delta ; le nombre de niveaux demandes double, de
      24 a 768, tant que les niveaux trouves ne debordent pas la fenetre des deux cotes. Poids c^2
      du site (0, 0) d'un niveau, lu PAR PARTITION : le vecteur est coupe en dedans I (sites max(a,
      b) <= r_c) et dehors O ; le dedans est recalcule depuis le dehors, (H_II - E) psi_I = - H_IO
      psi_O, resolution dense dans l'ordre naturel des sites ; c^2 = psi_I(0,0)^2 / (|psi_I|^2 +
      |psi_O|^2). Le composant BRUT du vecteur d'ARPACK est consigne a cote. Un niveau est FIABLE si
      ses deux lectures par partition s'accordent a 2 pour cent.
  5.4 FEUILLE DES BOITES (lecture_boites_pont_machine1_v1.py, a18770415291a726). PART d'un niveau,
      en |delta| : y = c^2 / (w0 rho_3(x) |delta|), rho_3(x) etant le lisse d'ordre 3 calcule
      directement a l'ecart du niveau (bloc chaine_pont_bloc_machine1_v1.py, cda5906f9be4b5bf).
      SOMME d'une boite : S = (somme des y) / 7.95, 7.95 etant la largeur de la fenetre en |delta|.
      COMPTE : n, le nombre de niveaux de la fenetre. Le compte d'une boite est VALIDE si son
      niveau-vide est suivi (poids du site (0, 0) >= 0.5, residu <= 1e-9) et si ses deux lectures
      debordent la fenetre et trouvent les memes niveaux (energies a 1e-9 pres). Une boite est
      LISIBLE si son compte est valide et si ses niveaux non fiables portent au plus 5 pour cent de
      la somme des y.
  5.5 FEUILLE DE VERDICT (verdict_pont_machine1_v1.py, f36f7dd5dd684643). Applique la section 7 aux
      sorties des deux feuilles. Ses constantes sont celles de la section 7 ; en cas de desaccord
      entre ce texte et la feuille, c'est ce TEXTE qui fait foi.
  5.6 CE QUI EST JOUE, par cellule : la sonde de densite aux quatre absorbeurs, douze barreaux
      chacun ; la sonde de boite fermee a VINGT cotes, groupe UN = 180 a 189, groupe DEUX = 291 a
      300, chaque cote une fois. Puis les feuilles. Les cotes peuvent etre repartis entre plusieurs
      processus ; une boite interrompue se rejoue telle quelle ; rien d'autre ne se rejoue.

6. QUALIFICATION DE L'INSTRUMENT AU POINT SACRIFIE (w2 = 101/50, hors chaine)
  Attendus ecrits avant les sorties : attendu_qualification_instruments_pont_machine1_v1.txt
  (7ed5e7b6d2b65623 ; son heure ecrite est fausse, rectificatif 7654c900f4725c5d : le fichier est
  date de 10 h 05, la premiere sortie de 10 h 11) et
  attendu_groupe_UN_point_sacrifie_machine1_v1.txt (728a6f0e3bf36425). Juges par
  bilan_qualification_pont_machine1_v1.py.
  DENSITE. ln R3 et ln R2 aux douze ecarts, aux trois profondeurs (3 barreaux : sorties de
  l'exploration du 17/11, remises au format) :
    x      3 barreaux         4 barreaux         5 barreaux
           ln R3    ln R2     ln R3    ln R2     ln R3    ln R2
    0.05   +0.0006  -0.0019   +0.0003  -0.0025   +0.0006  -0.0027
    0.25   +0.0003  -0.0018   +0.0005  -0.0022   +0.0009  -0.0021
    0.5    +0.0005  -0.0016   +0.0007  -0.0016   +0.0009  -0.0016
    1      +0.0006  -0.0003   +0.0005  -0.0006   -0.0000  -0.0010
    1.5    -0.0004  +0.0002   -0.0008  +0.0000   -0.0003  +0.0004
    2      -0.0015  +0.0006   -0.0010  +0.0015   -0.0006  +0.0022
    3      -0.0031  +0.0036   -0.0031  +0.0045   -0.0024  +0.0057
    4      -0.0059  +0.0066   -0.0041  +0.0093   -0.0013  +0.0124
    5      -0.0074  +0.0120   -0.0043  +0.0162   -0.0006  +0.0200
    6      -0.0092  +0.0184   -0.0046  +0.0237   +0.0033  +0.0306
    7      -0.0104  +0.0255   -0.0016  +0.0353   +0.0105  +0.0451
    8      -0.0086  +0.0364   +0.0045  +0.0491   +0.0225  +0.0631
  Lisibles : 12, 12 et 12 ecarts sur 12. Plus grand |ln R3| : 0.0104, 0.0046, 0.0225. Plus grande
  etendue entre absorbeurs : 0.0045, 0.0028, 0.0034. A1 (4 barreaux lisibles partout) : TIENT. A2 (5
  barreaux lisibles partout) : TIENT. A3 (|ln R3| <= 0.02 partout a 4 et 5 barreaux) : TOMBE, a 5
  barreaux et x = 8. A4 (R3 decroit avec x) : TOMBE : a 8 |delta| le residu de l'ordre 3 CHANGE DE
  SIGNE avec la profondeur (-0.0086, +0.0045, +0.0225) et grandit a 5 barreaux. L'ordre 3 est plus
  pres de la 2D que l'ordre 2 a chaque ecart x >= 5 aux trois profondeurs ; a x = 4 et 3 barreaux il
  ne l'est que de 0.0007.
  Au vide, a cote : ln (chaine d'ordre 3 / 2D) vaut de -0.00025 a +0.00016 aux absorbeurs A, B, D,
  et de -0.00233 a -0.00173 a l'absorbeur C.
  BOITE FERMEE, contre les niveaux publies par machine 2 (6 boites : cotes 190, 200, 209 et 300 a 3
  barreaux, 300 a 4 et a 5 barreaux). B1 (memes niveaux) : TIENT ; meme compte partout, ecarts au
  vide egaux a 2.8e-12 |delta| pres. B2 (ma lecture brute contre ses niveaux fiables, a 2 pour cent)
  : TIENT, plus grand ecart 0.0139. B3 (partition contre brut a 1e-3 pres a 3 barreaux) : TOMBE, de
  peu : 1.1e-03 au cote 181, sur 14 boites ; mediane 7.5e-05. B4 (au niveau que machine 2 dit non
  fiable, 5 barreaux, cote 300, x = 6.699 : mes deux lectures par partition d'accord a 1e-3) : TIENT
  ; elles s'accordent a 2.8e-11 pres, quand mes deux lectures brutes different de 0.0112.
  Au cote 300, les deux lectures par partition s'accordent a 2.3e-10, 1.7e-10 et 4.7e-11 pres a 3, 4
  et 5 barreaux ; les deux lectures brutes a 2.7e-04, 0.0083 et 0.0152. Sur toutes les boites
  jouees, la lecture par partition refaite au rayon r_c + 6 s'ecarte de 2.5e-09 au plus.
  ECART A MON ATTENDU, DECLARE. L'attendu disait : "Si B3 ou B4 tombe, la lecture du gel sera la
  lecture brute a deux decalages". B3 est tombe, de peu. Je ne suis PAS cette clause : elle etait
  mal concue. B3 compare la partition au brut, et ce que les pieces montrent est que c'est le brut
  qui flotte (jusqu'a 0.0152 entre mes deux lectures brutes, et 2.6 pour cent entre celles de
  machine 2 au meme niveau), pas la partition. La lecture du gel est la lecture PAR PARTITION.
  Machine 2 peut le refuser.
  GROUPE UN au point sacrifie, 3 barreaux, dix boites des cotes 180 a 189. U1 (n moyen de 8 a 11, lu
  sur le compte des niveaux libres) : TOMBE : n moyen 13.6 (de 10 a 15). Le compte ne suit PAS
  l'escalier des niveaux libres ; il suit le cote. U2 (moyenne de S dans [0.90, 1.15]) : TIENT :
  0.9975 +- 0.0349. U3 (ecart-type de S de 0.08 a 0.20) : TIENT : 0.1103. U4 (tous les niveaux
  fiables) : TIENT. Compte reduit n / (cote x 7.95 x |delta|) : 0.464 ; au cote 300, une boite par
  profondeur : n = 19, 19, 19, soit 0.398 ; S = 1.0428, 1.0424, 1.1107.
  ESSAI A L'AVEUGLE DU CHEMIN delta < 0. Aucune 2D hors du vide n'a ete regardee a delta < 0, a
  aucun w2 ; c'est voulu, et cela laissait les deux sondes jamais executees de ce cote. Elles l'ont
  ete une fois, a w2 = 197/100 (delta = -0.030, non candidat), 3 barreaux : la densite a un
  absorbeur et un barreau, une boite de cote 60, dans un dossier temporaire detruit ensuite. Seuls
  les deux codes de sortie et 13 booleens de forme ont ete lus (desaccord negatif, vide suivi,
  densites finies et positives, fenetre debordee, memes niveaux aux deux lectures, ecarts dans la
  fenetre, poids positifs, niveaux fiables) : tous vrais. Aucun nombre de ces sorties n'a ete
  imprime ni garde (essai_aveugle_delta_negatif_machine1_v1.py et son journal).
  REPETITION de la feuille de verdict sur ces pieces (ce n'est pas un verdict ; le groupe DEUX n'y a
  qu'une boite) : a 3 barreaux, (L) TIENT, pire ln R3 -0.0104 ; (S) TIENT, 1.0016 +- 0.0318 ; (C)
  TIENT, comptes reduits 0.464 et 0.398, rapport 1.397. A 4 et 5 barreaux : (L) TIENT et TIENT.
  Cout sur le poste de machine 1 (2 coeurs, trois calculs de front) : densite, de 379 a 994 s par
  absorbeur a 4 et 5 barreaux ; boite fermee, 44 s en moyenne aux cotes 180 a 189, de 336 a 366 s au
  cote 300, pic de memoire 1.8 Go.

7. LES ENONCES (la cellule pour unite)
  (L) LE LISSE. Une cellule est LISIBLE pour (L) si au moins 10 de ses 12 ecarts le sont (5.2). Elle
      TIENT si, a chaque ecart lisible, |ln R3(x)| <= 0.05 : la chaine d'ordre 3 rend la densite 2D
      du site (0, 0) sous absorbeur a 5 pour cent pres, de 0.05 a 8 |delta| de l'energie du vide.
  (L2) L'ORDRE. Une cellule lisible pour (L) TIENT si, a chaque ecart lisible x >= 5, |ln R3| < |ln
      R2| : l'ordre 3 est plus pres de la 2D que l'ordre 2.
  (S) LA SOMME. Une cellule est LISIBLE pour (S) si chacun de ses deux groupes compte au moins 8
      boites lisibles (5.4). Elle TIENT si la moyenne de S sur toutes ses boites lisibles est dans
      [0.85, 1.15] ET si la moyenne de S de chaque groupe est dans [0.80, 1.20] : la force que
      l'absorbeur lit comme une densite est la somme des poids que les niveaux de la boite fermee
      portent, et elle ne depend pas du cote.
  (C) LE COMPTE. Une cellule est LISIBLE pour (C) si chacun de ses deux groupes compte au moins 8
      boites de compte valide. Elle TIENT si, dans chaque groupe, le COMPTE REDUIT (moyenne de n) /
      (moyenne des cotes x 7.95 x |delta|) est dans [0.33, 0.55] ET si le rapport de la moyenne de n
      du groupe DEUX a celle du groupe UN est dans [1.25, 1.85] : le nombre de niveaux qui portent
      la force croit avec le cote, comme le cote fois |delta|.
  UNE FAMILLE est TENUE si aucune cellule lisible ne tombe et si au moins quatre cellules sont
  lisibles, dont une au moins par creneau ; TOMBEE si une cellule lisible tombe ; NON JUGEE sinon.
  Le verdict est rendu par famille, et par creneau a cote.

8. CE QUE VAUT CE QUI NE SE LIT PAS
  Une cellule illisible pour une famille ne compte ni pour ni contre elle. Un ecart illisible n'est
  pas juge. Une boite dont le compte n'est pas valide sort de (S) et de (C) ; une boite dont les
  niveaux non fiables portent plus de 5 pour cent de la somme sort de (S) et reste dans (C). Aucune
  boite n'est remplacee par une autre : les vingt cotes sont fixes. Si la barriere d'une cellule ne
  finit pas au site m, les sondes refusent : la cellule est illisible pour les quatre familles.
  Aucune tolerance, aucun cote, aucun absorbeur ni aucune definition ne change apres lecture du run.

9. QUESTIONS POSEES A COTE, SANS JUGEMENT
  (Q1) L'EXCES. Au point sacrifie la somme vaut 1.043 +- 0.018 sur les 32 boites de machine 2 (cotes
      190 a 402) et 0.9975 +- 0.0349 sur les dix boites des cotes 180 a 189. La feuille rend la
      moyenne de S toutes boites lisibles confondues et son erreur ; l'exces "se retrouve" si elle
      depasse 1 de plus de deux erreurs.
  (Q2) LES PARTS SONT-ELLES EGALES. Par groupe, le rapport de la moyenne de 1 / participation a
      celle de 3 / (n + 2) : 1 pour des parts tirees d'une loi de Porter-Thomas, moins si elles sont
      plus egales.
  (Q3) LE PONT SANS LA CHAINE. La somme relue avec la densite 2D : chaque y divise par R3 a l'ecart
      du niveau, ln R3 interpole lineairement en x entre les ecarts lisibles. Si (L) tombe dans une
      cellule, c'est cette somme qui dit si la boite fermee et l'absorbeur s'accordent ; elle n'est
      pas jugee.
  (Q4) LE VIDE. Le plateau de la largeur du vide par absorbeur, contre G3*. C'est la grandeur du gel
      du vide (delta 102), a deux w2 qu'il n'a pas joues.

10. CE QUE CHAQUE ISSUE ENGAGE
  (L), (S) et (C) TENUES : le pont tient, aux tolerances dites, sur six cellules neuves ; ce que
  l'absorbeur lit est la force du vide repartie sur les niveaux de la boite fermee, dont le nombre
  croit avec la boite. Cela ne dit rien de la boite infinie, qui reste une extrapolation, ni de la
  resonance exacte.
  (L) TOMBEE, (S) TENUE : la chaine d'ordre 3 ne rend pas la densite hors du vide a 5 pour cent la
  ou elle tombe ; le pont entre boite fermee et absorbeur n'est pas atteint, et (Q3) dit ce qu'il
  vaut sans la chaine.
  (S) TOMBEE : la densite lue sous absorbeur n'est pas, aux tolerances dites, la force portee par
  les niveaux de la boite fermee a ces cotes. La lecture "la largeur sous absorbeur est le taux de
  fuite du systeme ferme" n'a alors plus d'appui ici ; les resultats des deltas 100 et 102 restent
  des resultats sur le systeme sous absorbeur.
  (C) TOMBEE : le nombre de niveaux ne croit pas comme le cote fois |delta| ; la lecture de machine
  1 est fausse la ou elle tombe, et (S) se lit seule.
  (L2) TOMBEE : l'ordre 3 n'ameliore pas l'ordre 2 hors du vide la ou elle tombe ; (L) se lit seule.
  Une famille NON JUGEE n'engage rien. Un creneau qui tient et l'autre qui tombe se disent tels
  quels.

11. LES ANNONCES DE LA PLUME (ecrites avant le run)
  Probabilite que la cellule tienne, selon moi :
    famille  MG3   MG4   MG5   PG3   PG4   PG5    la famille TENUE
    (L)      0.85  0.80  0.50  0.95  0.95  0.90   0.40
    (L2)     0.85  0.85  0.85  0.95  0.95  0.95   0.70
    (S)      0.88  0.85  0.75  0.93  0.90  0.85   0.50
    (C)      0.75  0.75  0.75  0.90  0.90  0.90   0.65
  Les quatre familles tenues : 0.2. L'issue que je crois la plus probable n'est PAS "tout tient" :
  c'est (L) qui tombe a MG5, aux plus grands ecarts, le reste tenant.
  Pourquoi MG5. Au point sacrifie le residu de l'ordre 3 a 8 |delta| vaut +0.0225 a 5 barreaux pour
  un pas de l'ordre 2 a l'ordre 3 de 0.0406 ; a MG5 ce pas vaut 0.0869. Si le residu suit le pas, il
  arrive a la tolerance ; s'il suit son carre, il la depasse.
  PG est presque le point sacrifie (delta = +0.019 contre +0.020) : ce creneau eprouve la
  reproductibilite et les profondeurs 4 et 5 en boite fermee, guere plus. L'epreuve a l'aveugle est
  MG : aucune 2D hors du vide et aucune boite fermee n'ont ete regardees a delta < 0, a aucun w2.
  Paris sur les questions : (Q1) la moyenne de S toutes boites confondues est dans [0.99, 1.05],
  probabilite 0.7 ; l'exces se retrouve, 0.4. (Q2) le rapport est entre 0.8 et 1.1 dans chaque
  groupe, 0.7. Une cellule au moins illisible pour (L), 0.15.

12. CE QUE MACHINE 2 CERTIFIE
  (a) que son tirage, avec la graine 456823 sur la table commune, rend les six cellules de la
      section 2 ;
  (b) que les sections 5 et 7 suffisent a ecrire les feuilles sans lire celles de machine 1, et que
      les trois feuilles de machine 1 font ce que ces sections disent ;
  (c) que les deux sondes tournent sur BOCAL4 au point sacrifie et y redonnent les pieces de la
      section 6 : la densite d'un absorbeur a 5 barreaux, une boite du groupe UN a 3 barreaux et la
      boite de cote 300 a 5 barreaux (memes niveaux, memes poids par partition) ; et ce qu'un run
      complet y coute ;
  (d) la lecture par partition : qu'elle l'accepte comme lecture du gel, ou qu'elle la refuse, et
      alors pourquoi ; et mon ecart a ma propre clause (section 6) ;
  (e) SA table de la section 4, recalculee sur BOCAL4 ;
  (f) qu'aucune 2D du systeme a fantome n'a ete jouee par elle a w2 = 397/200 ni a w2 = 2019/1000
      depuis sa certification de la premiere partie.

13. LE RUN, ET LA SUITE
  (1) machine 2 certifie cette piece ; (2) l'operateur donne le feu vert par ecrit ; (3) machine 2
  joue une fois, aux six cellules : 24 sorties de densite, 120 boites ; (4) elle passe ses sorties
  par les trois feuilles et rend le tout dans un lot, journaux compris ; (5) machine 1 rejoue les
  trois feuilles sur les sorties de machine 2 ; (6) machine 1 ecrit l'acte, machine 2 contresigne,
  l'operateur depose.

14. LIMITES, ET ECARTS DECLARES
  - Les tolerances sont de la plume de machine 1 : 0.05 pour (L), [0.85, 1.15] et [0.80, 1.20] pour
    (S), [0.33, 0.55] et [1.25, 1.85] pour (C). Elles sont posees APRES la calibration au point
    sacrifie et AVANT toute 2D aux cellules tirees.
  - Ecart de redaction, declare : ma premiere tolerance pour (L) etait max(0.02, la moitie du pas de
    l'ordre 2 a l'ordre 3). La calibration a 5 barreaux l'aurait fait tomber au point sacrifie
    (0.0225 a x = 8). Je l'ai remplacee par 0.05 partout, la tolerance du gel de l'ordre 3 dans son
    domaine. C'est un desserrement, fait apres avoir vu le point sacrifie et avant d'avoir vu une
    cellule.
  - (L2) ne juge que x >= 5 : a x = 4 et 3 barreaux, au point sacrifie, l'ordre 3 ne devance l'ordre
    2 que de 0.0007.
  - (C) n'est plus lu sur le compte des niveaux libres : mon attendu U1 est tombe. Le compte reduit
    n'est calibre qu'a un seul |delta| (0.02) ; qu'il vaille pour |delta| = 0.015 et pour l'autre
    signe est une prediction, pas un acquis.
  - La lecture par partition est neuve ; elle n'a jamais ete certifiee. Elle redonne les parts de
    machine 2 la ou ses deux lectures s'accordent.
  - (S) est lue avec le lisse de la chaine. Si (L) tombe dans une cellule, (S) y perd son sens et
    (Q3) la remplace, sans jugement.
  - Deux groupes de cotes seulement : la croissance du compte est jugee sur deux points. Cote 300 au
    plus.
  - Le chemin delta < 0 des deux sondes n'a ete execute qu'une fois, a l'aveugle, a un w2 non
    candidat et sur une petite boite : cela dit que le code s'y execute, pas qu'une boite de cote
    300 ou une densite a 5 barreaux s'y lisent.
  - Le moteur et les blocs sont les memes pour la chaine et pour la 2D, et pour les deux machines :
    l'accord eprouve la reduction a une dimension, les absorbeurs et la boite fermee, pas le moteur.
    Une seule definition du hamiltonien effectif.
  - Rien n'est dit de la duree de vie du systeme ferme, de la boite infinie, de la resonance exacte,
    ni des w2 non tires.

15. PIECES DE CE LOT (convention B)
    e714fe4414ebe599  tirage_pont_graine_456823_machine1_v1.log
    cda5906f9be4b5bf  chaine_pont_bloc_machine1_v1.py
    6ccb8789041391dc  chaine_cellules_pont_machine1_v1.py
    24e45bea8ab8f1e1  chaine_cellules_pont_machine1_v1.log
    b68dcc142d91719a  chaine_cellules_pont_v1.json
    110416aa18270c21  controles_instruments_pont_machine1_v1.py
    b94e8c022d149872  controles_instruments_pont_machine1_v1.log
    968d63a59126a126  controles_instruments_pont_v1.json
    38ad6aa883b6e4fa  sonde_densite_2d_pont_machine1_v1.py
    c5c70a9b08c3bee3  lecture_densite_2d_pont_machine1_v1.py
    443940bd265c495d  sonde_boite_fermee_pont_machine1_v1.py
    a18770415291a726  lecture_boites_pont_machine1_v1.py
    f36f7dd5dd684643  verdict_pont_machine1_v1.py
    a201ea06a51f05f0  controle_details_R1_v1.json
    fd4d542f5e7e102b  controle_details_et_reserve_R1_machine1_v1.log
    296aa81858c71645  controle_details_et_reserve_R1_machine1_v1.py
    ca96f2d201d3d86a  lecture_certification_m2_gel_pont_partie1_machine1_v1.log
    80860dafc11e6b96  lecture_certification_m2_gel_pont_partie1_machine1_v1.py
    76faa4fc1a7e8559  lecture_certification_m2_v1.json
    20b146a4f372a339  tirage_demonstration_table_commune_machine1_v1.log
    728a6f0e3bf36425  attendu_groupe_UN_point_sacrifie_machine1_v1.txt
    7ed5e7b6d2b65623  attendu_qualification_instruments_pont_machine1_v1.txt
    4f613dcd0cdb4fd1  bilan_qualification_pont_machine1_v1.log
    ac22de7bea336d7f  bilan_qualification_pont_machine1_v1.py
    8fd8a4ee94068f9a  bilan_qualification_pont_v1.json
    c8eb781e8b3fd424  boite_SA3_200_v1.jsonl
    0cea4b8d0bc80a59  boite_SA3_200_v1.log
    d1fceab497ab5481  boite_SA3_300_v1.jsonl
    bb5f99d38cf682b5  boite_SA3_300_v1.log
    5e551aec887044b2  boite_SA4_300_v1.jsonl
    b7d030330e31ae80  boite_SA4_300_v1.log
    8e6b6451ec8fbe6a  boite_SA5_300_v1.jsonl
    c0681ff90d49c9f0  boite_SA5_300_v1.log
    379ef5c426d1c229  boites_SA3_UN_v1.jsonl
    93d84770b799290c  boites_SA3_UN_v1.log
    00bdae4b07588675  conversion_exploration_SA3_machine1_v1.log
    fada4869f7d5febd  conversion_exploration_SA3_machine1_v1.py
    2f96b429c8e864e5  densite_2d_SA3_A_v1.json
    e7a599cf061a43ea  densite_2d_SA3_B_v1.json
    576fd6cc9bc2b828  densite_2d_SA3_C_v1.json
    99d0a035391137dd  densite_2d_SA3_D_v1.json
    06cf6c0cba1412c3  densite_2d_SA4_A_v1.json
    340aad37aef57dcb  densite_2d_SA4_A_v1.log
    e2a5e3ffb658acbe  densite_2d_SA4_B_v1.json
    c206f2b0f7995339  densite_2d_SA4_B_v1.log
    6d92bdd1f734287f  densite_2d_SA4_C_v1.json
    7161cd8c06de0880  densite_2d_SA4_C_v1.log
    92fd1aab02b0c0f4  densite_2d_SA4_D_v1.json
    1755e53b811778f9  densite_2d_SA4_D_v1.log
    55ac13dd2bec0f6b  densite_2d_SA5_A_v1.json
    b0e13e9e1e2fbc4b  densite_2d_SA5_A_v1.log
    c705aab87feb8298  densite_2d_SA5_B_v1.json
    b94ab69fa8546855  densite_2d_SA5_B_v1.log
    63ae52950546d30d  densite_2d_SA5_C_v1.json
    acf885b187f76f63  densite_2d_SA5_C_v1.log
    170fa71e6e98f451  densite_2d_SA5_D_v1.json
    678ac03fe8b7f6a1  densite_2d_SA5_D_v1.log
    bd6dd3df604a8726  essai_aveugle_delta_negatif_machine1_v1.log
    de4ae3f8b698c047  essai_aveugle_delta_negatif_machine1_v1.py
    aff270582f4edd33  lecture_boites_qualification_v1.json
    f4300336d6ebf9b3  lecture_boites_qualification_v1.log
    7b145827bc7eac82  lecture_boites_repetition_v1.json
    0967f7a4d9f755e3  lecture_boites_repetition_v1.log
    df13f41af8105547  lecture_densite_2d_SA3_v1.json
    f32ba2b0f64d65a2  lecture_densite_2d_SA3_v1.log
    c0e6efda8b909164  lecture_densite_2d_SA4_v1.json
    01dbedea9c5383e0  lecture_densite_2d_SA4_v1.log
    67432939e6c1e628  lecture_densite_2d_SA5_v1.json
    342da792cafaaf5a  lecture_densite_2d_SA5_v1.log
    0a86ea08f6a2388e  profil_factorisation_machine1_v1.log
    e8b08c11820a0aa0  profil_factorisation_machine1_v1.py
    7654c900f4725c5d  rectificatif_heure_attendu_qualification_machine1_v1.txt
    51054b9902370955  regression_SA3_A_k3.json
    238b049a71c93248  repetition_verdict_v1.json
    40805f3b2534f283  repetition_verdict_v1.log
    (ce script)       construction_gel_pont_partie2_machine1_v1.py

-- FIN gel_pont_partie2_instrument_enonces_pre_enregistrement_v1 --
