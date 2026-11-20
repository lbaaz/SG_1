DELTA nn -- LE PONT : CE QUE L'ABSORBEUR LIT, ET LES NIVEAUX DE LA BOITE FERMEE. RUN DU 18/11/2026
SOUS LE GEL EN DEUX PARTIES 735ce41be200c5cd (REGLE DE TIRAGE) ET 428ac47649de31f3 (INSTRUMENT,
ENONCES), RECTIFICATIF D'AVANT RUN 9e25019f3b9bdf04.
VERDICT : (S) TENUE, (C) TENUE, (L) TOMBEE, (L2) TOMBEE.
(plume machine 1 ; certifications, run et seconde feuille machine 2)
=======================================================================

nn.0 POSITION
  Ce delta rend le run unique du gel "pont". Sa question : ce que l'absorbeur lit comme une densite,
  et dont le delta 102 a tire la largeur du vide, est-il la force que le vide porte reellement sur
  les niveaux de la boite FERMEE ? Six cellules ont ete tirees par une graine de l'operateur
  (456823) : w2 = 397/200 (delta = -0.015) et w2 = 2019/1000 (delta = +0.019), chacun a 3, 4 et 5
  barreaux de chaine. Par cellule : la densite 2D du site (0, 0) sous quatre absorbeurs, a douze
  ecarts de l'energie du vide, et vingt boites fermees de cotes 180 a 189 et 291 a 300.
  (S) et (C) sont TENUES aux six cellules : la somme des parts des niveaux de la boite fermee vaut
  de 0.9804 a 1.0299 par cellule, et leur nombre croit avec le cote. (L) et (L2) sont TOMBEES aux
  trois cellules de desaccord negatif : a 8 |delta| du vide, la chaine d'ordre 3 s'ecarte de la
  densite 2D de 0.0502 a 0.0745 en logarithme, et l'ordre 2 y est plus pres que l'ordre 3. Elles
  tiennent aux trois cellules de desaccord positif.
  Ce que cela dit. A delta > 0, ou (L) tient, le pont entre l'absorbeur et la boite fermee tient aux
  tolerances du gel. A delta < 0, joue a l'aveugle, la somme tient avec le lisse de la chaine, mais
  ce lisse n'est pas, a 5 pour cent pres, la densite que lit l'absorbeur loin du vide : par les
  enonces JUGES le pont n'y est pas atteint, comme le gel l'avait ecrit d'avance pour cette issue.
  La somme relue avec la densite 2D elle-meme, (Q3), qui n'est pas jugee, y vaut de 0.9979 a 1.0107.
  Cela ne dit rien de la boite infinie, de la resonance exacte, ni de la duree de vie du systeme
  ferme.

nn.1 CE QUI A ETE JOUE, ET DANS QUEL ORDRE
  - 17/11, 00 h 56 : l'operateur ouvre le gel ("Go rediger le gel."). Premiere partie, regle de
    tirage et d'eligibilite : canon 735ce41be200c5cd, lot de machine 1 55612644fc4ca279. Certifiee
    par machine 2 (lot acfecb6da73f20ae), avec une reserve de redaction.
  - 17/11, 09 h 56 : l'operateur donne la graine 456823 aux deux machines. Tirages identiques des
    deux cotes (lot de machine 2 6a83793a2586f4dd) : les deux creneaux au rang 0, MG a w2 = 397/200,
    PG a w2 = 2019/1000.
  - 17/11 : seconde partie, instrument, enonces, tolerances : canon 428ac47649de31f3, lot de machine
    1 7bf7982cceade968. Certifiee par machine 2 sur ses six points, lecture par partition acceptee,
    huit reserves de redaction (lot a77b27f763fb69cd).
  - 17/11 : rectificatif d'avant run de machine 1 (canon 9e25019f3b9bdf04, lot 5d75dd59784d3811) :
    une sortie de densite incomplete se rejoue telle quelle, une sortie complete jamais ; les huit
    reserves prises. Machine 2 prend la regle.
  - 18/11 : feu vert ECRIT de l'operateur a machine 2. La date y est ; l'heure n'y est pas (nn.9).
    Machine 2 l'a recu a 00 h 11 a son horloge.
  - 18/11 : le run, un seul appel du pilote de machine 2 sur BOCAL4 : 48 calculs (par cellule quatre
    densites et quatre lots de boites), huit de front, 11185 s. Aucun calcul relance ; 24 sorties de
    densite completes sur 24 ; 120 boites sur 120. Puis les trois feuilles de machine 1 et celles de
    machine 2. Lot de machine 2 : 9b980dffc71552d5.
  - 18/11 : machine 1 rejoue ses trois feuilles sur les sorties de machine 2 (nn.4) et ecrit cet
    acte.
  Avant le run, aucune 2D du systeme a fantome n'a ete calculee aux deux w2 tires, par aucune
  machine (E19) ; une fois, a w2 = 197/100, machine 1 a execute ses deux sondes a l'aveugle, sans en
  lire aucun nombre (gel, section 6).

nn.2 L'INSTRUMENT
  Celui de la seconde partie du gel, certifie, non modifie : sonde de densite 2D a energie fixee,
  sonde de boite fermee (poids du site (0, 0) lu par partition), feuille de densite, feuille des
  boites, feuille de verdict. Machine 2 a controle apres le run que les 84 pieces du lot de machine
  1 utilisees etaient de canon identique au manifeste. La table de la chaine lue par les feuilles
  est celle que machine 2 a recalculee sur BOCAL4 ; elle s'accorde a celle de machine 1 a 1.3e-09
  pres.

nn.3 LE VERDICT DE LA FEUILLE DU RUN
    cellule  (L)     pire ln R3, a l'ecart x   part de la tolerance   (L2)
    MG3      TOMBE   -0.0502 a x = 8            1.00                   TOMBE
    MG4      TOMBE   -0.0608 a x = 8            1.22                   TOMBE
    MG5      TOMBE   -0.0745 a x = 8            1.49                   TOMBE
    PG3      TIENT   -0.0104 a x = 7            0.21                   TIENT
    PG4      TIENT   -0.0049 a x = 6            0.10                   TIENT
    PG5      TIENT   +0.0180 a x = 8            0.36                   TIENT
    cellule  (S)     moyenne de S       (C)     compte reduit, UN   DEUX    rapport des comptes
    MG3      TIENT   0.9946 +- 0.0179   TIENT   0.486               0.434   1.430
    MG4      TIENT   0.9804 +- 0.0212   TIENT   0.459               0.454   1.584
    MG5      TIENT   0.9848 +- 0.0178   TIENT   0.473               0.443   1.500
    PG3      TIENT   0.9906 +- 0.0230   TIENT   0.441               0.439   1.593
    PG4      TIENT   1.0299 +- 0.0198   TIENT   0.449               0.441   1.576
    PG5      TIENT   0.9869 +- 0.0215   TIENT   0.452               0.437   1.548
    FAMILLE (L), le lisse : TOMBEE ; cellules lisibles 6 sur 6 ; tombees : MG3 MG4 MG5
    FAMILLE (L2), l'ordre : TOMBEE ; cellules lisibles 6 sur 6 ; tombees : MG3 MG4 MG5
    FAMILLE (S), la somme : TENUE ; cellules lisibles 6 sur 6
    FAMILLE (C), le compte : TENUE ; cellules lisibles 6 sur 6
  Par creneau, lu sur les lignes par cellule : MG (delta < 0), (L) et (L2) tombent aux trois
  cellules, (S) et (C) tiennent aux trois ; PG (delta > 0), les quatre familles tiennent aux trois
  cellules. La feuille de machine 2, ecrite depuis le texte, rend les memes 24 jugements.
  Tout est lisible : douze ecarts sur douze aux six cellules, plus grande etendue entre absorbeurs
  0.0034 ; 120 boites lisibles sur 120 ; 1743 niveaux, tous fiables.

nn.4 LE REJEU DE MACHINE 1 (etape 5 du gel)
  Par rejeu_feuilles_run_pont_machine1_v1.py, sur les fichiers du lot de machine 2. Completude,
  controlee avant les feuilles : 24 sorties de densite a douze barreaux d'absorbeur, 120 boites, les
  vingt cotes de chaque cellule une fois chacun, chaque fichier a la cellule du tirage : aucune
  faute. Mes trois feuilles rendent les verdicts de nn.3. Contre les sorties que machine 2 a rendues
  : 6211 nombres compares, plus grand ecart 1.4e-11, aucun desaccord de verdict ni de champ. Refaits
  avec MA table de la chaine au lieu de la sienne : les memes 24 jugements et les memes quatre
  familles.
  Mon rectificatif annoncait une comparaison a 1e-12 pres : elle n'est PAS tenue a ce seuil. Les
  ecarts au-dessus sont sur des nombres derives et non juges (des parts y, recalculees avec la
  densite de la chaine sur chaque machine, et l'exces de (Q1) compte en erreurs). L'annonce etait
  trop serree ; je le dis au lieu de changer le seuil.

nn.5 LECTURE, ENONCE PAR ENONCE
  (L) ln R3 = ln [densite 2D / (w0 x lisse d'ordre 3)], aux douze ecarts x (en |delta|) ; tolerance
  0.05 :
    x      MG3      MG4      MG5      PG3      PG4      PG5
    0.05   +0.0005  +0.0000  -0.0001  +0.0007  +0.0002  +0.0005
    0.25   +0.0004  -0.0002  -0.0003  +0.0005  +0.0004  +0.0009
    0.5    +0.0000  -0.0004  -0.0006  +0.0003  +0.0007  +0.0007
    1      -0.0007  -0.0009  -0.0010  +0.0006  +0.0006  +0.0000
    1.5    -0.0015  -0.0016  -0.0019  -0.0002  -0.0006  -0.0004
    2      -0.0023  -0.0027  -0.0033  -0.0013  -0.0008  -0.0005
    3      -0.0054  -0.0063  -0.0070  -0.0028  -0.0030  -0.0024
    4      -0.0100  -0.0117  -0.0135  -0.0053  -0.0041  -0.0015
    5      -0.0167  -0.0193  -0.0223  -0.0071  -0.0043  -0.0011
    6      -0.0252  -0.0292  -0.0345  -0.0087  -0.0049  +0.0020
    7      -0.0361  -0.0430  -0.0521  -0.0104  -0.0022  +0.0080
    8      -0.0502  -0.0608  -0.0745  -0.0089  +0.0025  +0.0180
  Hors tolerance : MG3 a x = 8 ; MG4 a x = 8 ; MG5 a x = 7 et 8. Partout ailleurs, et a tous les
  ecarts des trois cellules PG, la tolerance est tenue. A delta < 0 le residu est negatif aux trois
  profondeurs a partir de 1 |delta|, croit avec l'ecart, et avec la profondeur a partir de 3 |delta|
  ; jusqu'a 4 |delta| il reste sous 0.0136.
  MG3 tombe de tres peu : 0.05024 pour 0.05, a un seul ecart. C'est une chute a la lettre ;
  l'etendue entre absorbeurs y vaut 0.0008, soit 3 fois l'ecart a la tolerance.
  (L2) ln R2, le meme rapport avec le lisse d'ordre 2 :
    x      MG3      MG4      MG5      PG3      PG4      PG5
    0.05   -0.0004  -0.0009  -0.0012  -0.0016  -0.0023  -0.0024
    0.25   -0.0004  -0.0008  -0.0009  -0.0016  -0.0020  -0.0018
    0.5    -0.0003  -0.0005  -0.0005  -0.0013  -0.0013  -0.0014
    1      +0.0001  +0.0002  +0.0005  -0.0004  -0.0004  -0.0008
    1.5    +0.0010  +0.0014  +0.0017  +0.0005  +0.0001  +0.0004
    2      +0.0021  +0.0024  +0.0027  +0.0008  +0.0016  +0.0022
    3      +0.0043  +0.0049  +0.0057  +0.0035  +0.0043  +0.0052
    4      +0.0069  +0.0076  +0.0078  +0.0060  +0.0085  +0.0113
    5      +0.0095  +0.0103  +0.0106  +0.0109  +0.0148  +0.0181
    6      +0.0125  +0.0132  +0.0130  +0.0169  +0.0215  +0.0275
    7      +0.0160  +0.0153  +0.0131  +0.0233  +0.0319  +0.0405
    8      +0.0187  +0.0165  +0.0125  +0.0331  +0.0443  +0.0564
  Aux trois cellules MG, l'ordre 2 est plus pres de la 2D que l'ordre 3 aux quatre ecarts juges (5,
  6, 7, 8) ; aux trois cellules PG, l'ordre 3 est plus pres aux quatre. A delta < 0 la 2D est entre
  l'ordre 2 et l'ordre 3, et plus pres de l'ordre 2 : l'ordre 3 corrige dans le bon sens et trop.
  (S) moyenne de la somme des parts, par cellule et par groupe de cotes ; (C) nombre moyen de
  niveaux :
    cellule  S, vingt boites    S, UN    S, DEUX   ecart-type UN / DEUX   n, UN   n, DEUX
    MG3      0.9946 +- 0.0179   1.0059   0.9833    0.090 / 0.072          10.70   15.30
    MG4      0.9804 +- 0.0212   0.9339   1.0269    0.091 / 0.077          10.10   16.00
    MG5      0.9848 +- 0.0178   0.9795   0.9902    0.107 / 0.044          10.40   15.60
    PG3      0.9906 +- 0.0230   0.9692   1.0119    0.120 / 0.083          12.30   19.60
    PG4      1.0299 +- 0.0198   1.0273   1.0325    0.098 / 0.084          12.50   19.70
    PG5      0.9869 +- 0.0215   0.9999   0.9739    0.085 / 0.109          12.60   19.50
  La somme est dans [0.85, 1.15] aux six cellules et dans [0.80, 1.20] aux douze groupes ; la
  moyenne de groupe la plus loin de 1 vaut 0.9339. Le compte reduit vaut de 0.434 a 0.486, pour
  [0.33, 0.55] ; le rapport des comptes de 1.430 a 1.593, pour [1.25, 1.85]. A delta < 0, ou rien
  n'avait ete regarde, le compte reduit est celui de delta > 0 : le nombre de niveaux suit bien le
  cote fois |delta|.

nn.6 CE QUI ETAIT CONSIGNE SANS ETRE JUGE
  (Q1) L'exces. Toutes boites confondues : S = 0.9945 +- 0.0082 sur 120 boites, soit -0.67 erreur
      par rapport a 1. L'exces de 4 pour cent vu au point sacrifie ne se retrouve pas.
  (Q2) Les parts sont-elles egales. Rapport a la loi de Porter-Thomas : 0.793 au groupe UN, 0.902 au
      groupe DEUX (60 boites chacun). Les parts sont un peu plus egales que cette loi ; aucune
      erreur n'est attachee a ces deux nombres.
  (Q3) Le pont sans la chaine : la somme relue avec la densite 2D, et (Q4) le vide, ln (G3* de la
      chaine / largeur 2D) :
    cellule  (Q3) S avec la 2D   (S) S avec la chaine   (Q4) absorbeurs A, B, D       absorbeur C
    MG3      1.0107              0.9946                 +0.00015 a +0.00018       +0.00195
    MG4      0.9979              0.9804                 +0.00033 a +0.00034       +0.00171
    MG5      1.0064              0.9848                 +0.00038 a +0.00038       +0.00063
    PG3      0.9956              0.9906                 +0.00004 a +0.00006       -0.00051
    PG4      1.0320              1.0299                 +0.00020 a +0.00023       -0.00192
    PG5      0.9852              0.9869                 -0.00019 a -0.00012       -0.00246
  Aux trois cellules MG, ou (L) tombe, la somme relue avec la densite 2D vaut de 0.9979 a 1.0107 :
  la boite fermee et l'absorbeur s'accordent sans passer par la chaine. Au vide meme, la chaine
  d'ordre 3 rend la largeur 2D a mieux que 0.0004 aux six cellules (hors absorbeur C) : la chaine
  est juste a l'energie du vide et s'en ecarte en s'en eloignant.
  REGARD APRES LECTURE, hors gel, non juge. A 8 |delta|, la place de la 2D entre l'ordre 2 (0) et
  l'ordre 3 (1), soit ln R2 / (ln R2 - ln R3) : MG3 0.27 ; MG4 0.21 ; MG5 0.14 ; PG3 0.79 ; PG4 1.06
  ; PG5 1.47. A delta > 0 l'ordre 3 fait l'essentiel du chemin, ou reste en deca ; a delta < 0 il va
  de 3.7 a 7.0 fois trop loin. Ce n'est pas explique.

nn.7 LES ANNONCES DE LA PLUME, CONFRONTEES AU RUN (gel, section 11)
    famille  MG3         MG4         MG5         PG3         PG4         PG5        la famille
    (L)      0.85 TOMBE  0.80 TOMBE  0.50 TOMBE  0.95 tient  0.95 tient  0.90 tient 0.40 TOMBEE
    (L2)     0.85 TOMBE  0.85 TOMBE  0.85 TOMBE  0.95 tient  0.95 tient  0.95 tient 0.70 TOMBEE
    (S)      0.88 tient  0.85 tient  0.75 tient  0.93 tient  0.90 tient  0.85 tient 0.50 TENUE
    (C)      0.75 tient  0.75 tient  0.75 tient  0.90 tient  0.90 tient  0.90 tient 0.65 TENUE
  Sur 24 annonces, 5 vont contre le run : (L) MG3 annoncee a 0.85, (L) MG4 annoncee a 0.80, (L2) MG3
  annoncee a 0.85, (L2) MG4 annoncee a 0.85, (L2) MG5 annoncee a 0.85. Toutes sont a delta < 0,
  toutes sur la chaine. J'annoncais comme issue la plus probable "(L) qui tombe a MG5, [...] le
  reste tenant" : MG5 tombe, mais MG3 et MG4 aussi, et (L2) avec elles. J'avais transporte a delta <
  0 un residu calibre a delta > 0 ; a 8 |delta| il vaut 0.0502, 0.0608 et 0.0745 en valeur absolue
  aux trois cellules MG, contre 0.0089, 0.0025 et 0.0180 aux trois cellules PG. Sur (S) et (C), mes
  annonces etaient plus prudentes que le run.
  Paris. (Q1) moyenne dans [0.99, 1.05] : tenu, de peu (0.9945). L'exces se retrouve (annonce a 0.4)
  : non. (Q2) rapport entre 0.8 et 1.1 dans chaque groupe : perdu, de peu (0.793 et 0.902). Une
  cellule au moins illisible pour (L) (annonce a 0.15) : aucune.

nn.8 CE QUE CET ACTE ECRIT, ET CE QU'IL N'ECRIT PAS (gel, section 10)
  Le gel prevoyait cette issue : "(L) TOMBEE, (S) TENUE : la chaine d'ordre 3 ne rend pas la densite
  hors du vide a 5 pour cent la ou elle tombe ; le pont entre boite fermee et absorbeur n'est pas
  atteint, et (Q3) dit ce qu'il vaut sans la chaine." Et : "(L2) TOMBEE : l'ordre 3 n'ameliore pas
  l'ordre 2 hors du vide la ou elle tombe".
  IL ECRIT : aux six cellules, la somme des poids que les niveaux de la boite fermee portent sur le
  site (0, 0), rapportee au lisse d'ordre 3 de la chaine, vaut 1 aux tolerances du gel, aux deux
  groupes de cotes ; le nombre de ces niveaux croit comme le cote fois |delta| ; cela vaut a delta <
  0, joue a l'aveugle, comme a delta > 0. Aux trois cellules de delta > 0, ou (L) tient, c'est le
  pont entre la boite fermee et l'absorbeur, aux tolerances dites. A delta < 0, la chaine d'ordre 3
  ne rend pas la densite 2D a 5 pour cent a 7 et 8 |delta| du vide et n'y ameliore pas l'ordre 2 :
  le pont n'y est pas atteint par les enonces juges.
  IL N'ECRIT PAS : que le pont tient a delta < 0 au titre d'un enonce juge (seule (Q3), non jugee,
  l'y montre, de 0.9979 a 1.0107) ; que la largeur sous absorbeur est le taux de fuite d'un systeme
  ferme infini (deux groupes de cotes, 300 au plus) ; une loi en delta (un w2 par signe) ; que la
  chaine d'ordre 3 est fausse au vide (elle y tient, (Q4) et delta 102) ; pourquoi l'ordre 3 corrige
  trop loin du vide a delta < 0 ; rien sur la resonance exacte ni sur des champs.

nn.9 CORRECTIONS DE MACHINE 2, DEFAUTS DE LA PLUME, ECARTS
  - Reserve R1 de machine 2 sur la premiere partie : le 4.4 disait la largeur lue sur la valeur
    propre sans dire que la double precision n'y suffit pas a 4 et 5 barreaux. Faute de la plume,
    rectifiee en section 3 de la seconde partie ; aucune decision ne change.
  - Seconde partie, declares avant le run : une heure fausse dans mon attendu de qualification ; une
    clause de cet attendu que je n'ai pas suivie (la lecture brute des poids en cas de chute de B3),
    acceptee par machine 2 ; une lecture des poids neuve, par partition, acceptee par machine 2 et
    jamais verifiee en precision etendue ; un attendu tombe (U1) qui a change la lecture de (C).
  - Tolerance de (L), desserree pendant la redaction, apres la calibration au point sacrifie et
    avant toute cellule : de max(0.02, la moitie du pas de l'ordre 2 a l'ordre 3) a 0.05 partout.
    Avec la premiere, calculee ici sur le run : les cellules MG3 MG4 MG5 tombent, les memes. Le
    desserrement n'a sauve aucune cellule tombee.
  - Fait trouve par machine 2 a sa certification : ma feuille de densite accepte une sortie
    interrompue ; et mon 5.6 interdisait, a la lettre, de rejouer une densite coupee. Rectificatif
    d'avant run, pris par machine 2. Ni cette regle ni celle des cotes manquants n'ont servi : rien
    n'a ete coupe.
  - Le feu vert. L'operateur l'a ecrit avec sa date ; l'heure etait laissee a completer dans la
    formule que machine 1 lui avait proposee, et elle est partie telle quelle. Machine 2 a porte au
    journal son heure de reception (00 h 11) : ce n'est pas une heure attestee par l'operateur. Le
    feu vert, lui, est ecrit et anterieur au run.
  - Le seuil de 1e-12 annonce pour mon rejeu n'est pas tenu (nn.4).
  - De machine 2, dits par elle : une premiere passe de son script de comparaison repliait les
    boites de deux cellules de meme profondeur (gardee, non corrigee en place) ; la memoire du run
    n'a pas ete mesuree.

nn.10 LIMITES
  - Les tolerances sont de la plume. MG3 tombe pour 0.00024 de trop sur 0.05 : avec une tolerance a
    peine plus large elle tenait, et MG4, MG5 tombaient quand meme.
  - (S) est jugee avec le lisse de la chaine, que (L) montre faux de 0.0502 a 0.0745 en logarithme a
    8 |delta| a delta < 0 ; la somme n'en bouge que de 0.0161 a 0.0215, et (Q3) la donne sans la
    chaine. (Q3) n'est pas jugee.
  - La lecture par partition est jugee sur sa stabilite (decalage, rayon, forme de la coupure, deux
    ecritures, deux machines), pas sur une valeur de reference exacte.
  - Deux groupes de cotes, 300 au plus ; un w2 par signe du desaccord ; PG est presque le point
    sacrifie.
  - Le moteur et les blocs sont les memes pour la chaine et la 2D, et pour les deux machines. Une
    seule definition du hamiltonien effectif.
  - Les deux feuilles ont ete ecrites separement, mais lisent les memes sorties de sondes : les
    sondes de machine 1 n'ont pas de seconde ecriture complete (machine 2 a refait la partition et
    compare les matrices).

nn.11 SUITE
  Contreseing de machine 2 ; depot sur l'ordre de l'operateur (prochain numero libre au registre :
  103). Rien n'est ouvert par cet acte. Ce qu'il laisse sans reponse : pourquoi l'ordre 3 corrige
  trop loin du vide a delta < 0 alors qu'il est juste au vide.

nn.12 PIECES (convention B)
  premiere partie du gel :
    735ce41be200c5cd  gel_pont_partie1_regle_tirage_pre_enregistrement_v1.md
  seconde partie du gel :
    428ac47649de31f3  gel_pont_partie2_instrument_enonces_pre_enregistrement_v1.md
  rectificatif d'avant run :
    9e25019f3b9bdf04  rectificatif_gel_pont_partie2_avant_run_machine1_v1.md
  instrument :
    38ad6aa883b6e4fa  sonde_densite_2d_pont_machine1_v1.py
    443940bd265c495d  sonde_boite_fermee_pont_machine1_v1.py
    c5c70a9b08c3bee3  lecture_densite_2d_pont_machine1_v1.py
    a18770415291a726  lecture_boites_pont_machine1_v1.py
    f36f7dd5dd684643  verdict_pont_machine1_v1.py
    cda5906f9be4b5bf  chaine_pont_bloc_machine1_v1.py
    6ccb8789041391dc  chaine_cellules_pont_machine1_v1.py
  note de machine 2 :
    8e9488e628de7747  POUR_MACHINE1_resultats_run_gel_pont_machine2_v1.md
  pilote de machine 2 :
    fba82f8cb708d12c  run_pont_machine2_v1.py
  lot de machine 2, run :
    229e47bceac1a1f7  run_pont_machine2.log
    138619d5aac8ac14  etat_run.json
    095917742c6da652  chaine_cellules_pont_v1.json
    6dc850c708316bfa  lecture_boites.json
    65e760f718e040ac  verdict.json
  lot de machine 2, sa propre feuille :
    6d230b2f804b1f07  verdict.json
  ce lot, rejeu de machine 1 :
    1515ffb17ffaf43e  rejeu_feuilles_run_pont_machine1_v1.py
    0b38619d9d9d2956  rejeu_feuilles_run_pont_machine1_v1.log
    3225d812e42e60aa  rejeu_feuilles_run_pont_v1.json
    2b5915a4b0fb0850  verdict.json
    d1991994e9641fac  lecture_boites.json
    02b3bf66c6acccbc  lecture_densite_2d_MG3.json
    259f47f19c21259e  lecture_densite_2d_MG4.json
    334f302b602f4a0d  lecture_densite_2d_MG5.json
    9188c39a3e870167  lecture_densite_2d_PG3.json
    76ca14cabef14186  lecture_densite_2d_PG4.json
    c1ae5cde6a3cf00a  lecture_densite_2d_PG5.json

-- FIN journal_delta_nn_pont_v1 --
