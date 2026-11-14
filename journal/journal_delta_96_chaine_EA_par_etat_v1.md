DELTA nn -- LA CHAINE E-A PAR ETAT, HORS PLAGE : RUN DU 14/11/2026 SOUS LE GEL 9df2702af59adbbc.
VERDICT : TENU EN PARTIE (cinq points juges tiennent, un tombe).
-- PROJET, VERSION 1
(plume machine 1 ; run et certification machine 2 ; a contresigner par machine 2)
=======================================================================

nn.0 POSITION
  Ce delta rend le run du gel "la chaine E-A par etat, hors plage". La question du gel : la chaine
  E-A du moteur, appelee au site entier qui etiquette un etat propre 2D, predit-elle la LECTURE de
  E-B a k = 3, a l'ordre de grandeur, hors des six points de M17 ? Reponse de la feuille : TENU EN
  PARTIE.
  Ce chantier n'est pas la piste (0) : il ne requalifie pas E-B, et aucune phrase d'ici ne dit
  "largeur" sans "lue a k = 3". Il a ete ouvert par l'operateur ("j'ouvre", le 14/11/2026 a 00 h 15,
  a machine 1) ; machine 2 ne peut pas le verifier sur piece (nn.11).
  Registre a l'ecriture : origin/main fe10bfe, plafond 94 (releve du 14/11). L'acte de la nuit bis,
  projet v2 (bdf8c5a0c73096a4), est contresigne par machine 2 (lot b46537578fff4ab0) et n'est pas
  depose. Aucun numero n'est pris ici (E18).

nn.1 PIECES (convention B)
  Au registre (fe10bfe)
    scripts/m17_chaine_v17.py  82a0be882568fe0c
      le moteur
  Hors registre, de machine 1 (lot b3d3e23e98914a95)
    gel_chaine_EA_par_etat_pre_enregistrement_v1.md  9df2702af59adbbc
      le gel
    sonde_chaine_par_etat_machine1_v1.py  acf7e26dedfa8abc
      la sonde : elle mesure et ne juge pas
    lecture_chaine_par_etat_machine1_v1.py  f94ab05f69e9bf2f
      la feuille : elle juge et ne mesure pas
  Hors registre, de machine 2
    lot de certification  3381564852ba6fe4
      certification du gel, de la sonde et de la feuille, AVANT le run
    lot de resultat  9143062c481ad267
      le run, sa lecture, les controles de machine 2
      sortie/sonde_chaine_par_etat.json  5d80bf2edd26a6c1
      les mesures : douze points, 168 etats
      sortie/verdict_chaine_par_etat.json  4fbc5f7115002054
      le verdict rendu par la feuille sur BOCAL4
      sortie/lecture_chaine_par_etat.log  997c4e4681b0e7ec
      son journal
      POUR_MACHINE1_resultat_chaine_EA_par_etat_machine2_v1.md  4297a8489cdf5eea
      la note de machine 2
      sortie/stabilite_sous_bruit_machine2.log  b643f7e55be69ef2
      les statuts sous le bruit des fils
      garde_G1_domaine_machine2_v1.log (lot de certification)  f839525cfff22aa5
      la garde du moteur aux douze points
  De ce lot
    verdict_rejoue_machine1.json  4fbc5f7115002054
      la feuille rejouee par machine 1 sur le JSON de la sonde
    lecture_rejouee_machine1.log  64589ba23c6b8097
      son journal

nn.2 CE QUI A ETE JOUE, ET PAR QUI (E19)
  Machine 2, AVANT le run (lot 3381564852ba6fe4) : 11 controles de lecture du gel, 0 morsure ; un
  lecteur independant, ecrit du texte du gel, compare a la feuille sur 4000 sondes synthetiques
  tirees aux bords des seuils, 0 ecart ; 24 alterations d'une ligne de la feuille, dont son banc
  mord 23 et le selftest de la feuille 15 ; l'essai aux deux ancres rejoue. Quatre reserves, aucune
  morsure (nn.9).
  Machine 2, le run (lot 9143062c481ad267) : BOCAL4, Windows AMD64, python 3.11.9, numpy 2.2.6, 16
  coeurs, variables de fils non fixees ; le 14/11 de 10:12:51 a 10:37:31 ; sonde code 0 en 1480 s,
  feuille code 0 ; un seul run, aucun arret, aucune reprise, aucun point rejoue. Temoin d'arrondi
  0x1.a483018a169c6p+64.
  Machine 1 : a rejoue la feuille (selftest 26 sur 26) sur le JSON de la sonde de machine 2. Son
  verdict est identique a celui que machine 2 rend, au canon (4fbc5f7115002054), et son journal
  identique hors la ligne de titre. Machine 1 n'a joue la sonde a aucun des dix points J1 a J6 et T1
  a T4, ni avant ni apres le run ; elle l'avait jouee aux deux ancres (essai a blanc du gel).

nn.3 LES GARDES
  G-1 le moteur lu par la sonde est au canon. G-2 les douze points sont presents, au role, au w2 et
  au facteur du gel. G-3 chacun porte 14 etats (168). G-4 les deux ancres rendent la lecture du run
  de M17 avec un ecart relatif NUL sur BOCAL4 (etat (7,2) a A1, etat (8,2) a A2). G-5 la feuille
  passe son selftest. Aucune garde ne mord.

nn.4 LES DOUZE POINTS (q = Gamma_chaine / Gamma_2D lue a k = 3, sur les etats juges)
  point  role    w2    g       statut        juges  q min    q max    mediane  premier juge
  J1     juge    1.90  x1      FACTEUR 2     11     0.621    1.161    0.897    (7,2) q = 0.950
  J2     juge    2.10  x1      HORS DECADE   13     2.945    4.168    3.735    (8,2) q = 3.711
  J3     juge    1.95  x3/2    FACTEUR 2     11     0.756    0.926    0.842    (5,2) q = 0.854
  J4     juge    2.05  x3/2    FACTEUR 2     14     1.269    1.511    1.418    (6,1) q = 1.444
  J5     juge    1.95  x2/3    DECADE         8     0.395    0.653    0.545    (10,3) q = 0.619
  J6     juge    2.05  x2/3    FACTEUR 2      8     1.292    1.641    1.503    (10,3) q = 1.590
  T1     temoin  1.96  x1      DECADE        12     0.498    0.866    0.756    (7,2) q = 0.819
  T2     temoin  2.04  x1      FACTEUR 2     12     1.153    1.404    1.334    (7,2) q = 1.347
  T3     temoin  1.85  x1      HORS DECADE   11     0.064    1.358    0.979    (6,2) q = 0.662
  T4     temoin  2.15  x1      HORS DECADE    8     12.327   26.380   18.348   (8,2) q = 17.665
  A1     ancre   1.95  x1      FACTEUR 2     11     0.587    0.882    0.758    (7,2) q = 0.819
  A2     ancre   2.05  x1      FACTEUR 2     12     1.292    1.629    1.505    (8,2) q = 1.474
  Exclus, par premier motif :
    J1  sous dix planchers 3
    J2  sous dix planchers 1
    J3  barriere vide 2 ; sous dix planchers 1
    J4  aucun
    J5  sous dix planchers 6
    J6  sous dix planchers 6
    T1  sous dix planchers 2
    T2  sous dix planchers 2
    T3  J flou 1 ; chaine instable 2
    T4  J flou 4 ; sous dix planchers 2
    A1  barriere vide 1 ; sous dix planchers 2
    A2  sous dix planchers 2
  "g" est le facteur sur la regle g_du_point du moteur. "Premier juge" : l'etat juge de plus grand
  recouvrement avec la graine. 131 etats juges sur 168.

nn.5 LE VERDICT
  Les six points juges sont lisibles. Cinq tiennent : J1, J3, J4 et J6 sont FACTEUR 2, J5 est
  DECADE. Un tombe : J2 est HORS DECADE. La cascade du gel (section 7) rend TENU EN PARTIE.
  Ce que le gel permet d'ecrire (section 11) : l'acte nomme les points tenus et les points tombes,
  et ne tire aucun "domaine de validite" sans un nouveau gel. Donc :
    - a J1 (1.90), J3 et J4 (couplage a 3/2 de la regle), J6 (couplage a 2/3, 2.05), la chaine au
      site entier rend la lecture de E-B a k = 3 a mieux qu'un facteur 2 pour chacun des 44 etats
      juges ;
    - a J5 (couplage a 2/3, 1.95), a mieux qu'une demi-decade pour les 8 etats juges ; 3 sont sous
      1/2 (q de 0.395 a 0.470), les 5 autres de 0.539 a 0.653 ;
    - a J2 (2.10), elle la SURESTIME d'un facteur 2.945 a 4.168 sur chacun des 13 etats juges ; 11
      d'entre eux sont hors de la demi-decade.
  Aucune largeur intrinseque n'est affirmee. Le verdict PAS DE SIGNAL de M17 et le verdict NON
  QUALIFIE de la nuit bis ne sont pas touches.

nn.6 LECTURES SANS VERDICT (gel, section 9)
  (a) Les temoins. T1 (1.96) est DECADE par un seul etat (q = 0.4977, les onze autres de 0.603 a
  0.866) ; T2 (2.04) est FACTEUR 2 ; T3 (1.85) et T4 (2.15) sont HORS DECADE, T3 en ordre disperse
  (q de 0.064 a 1.358), T4 d'un facteur 12.3 a 26.4.
  (b) Le sens. Aux douze points, le q median est sous 1 quand w2 < 2 et au-dessus de 1 quand w2 > 2.
  (c) J5 et J6 n'ont que 8 etats juges : six de leurs quatorze sont sous dix planchers. A J6 un
  Gamma_2D(3) est negatif (-3.9e-14, du bruit) ; il est exclu comme "sous dix planchers".
  (d) Le bruit des fils, mesure par machine 2 : 7.3e-14 en absolu sur la cible. Aucun des douze
  statuts ne change dans le pire ni dans le meilleur sens ; le bruit relatif maximal sur les 131
  etats juges est 2.4 pour cent.

nn.7 LA GARDE DE DOMAINE DU MOTEUR (reserve R-1 de machine 2, ecrite AVANT le run)
  Le moteur porte sa propre garde de domaine, G-1 : (D1) |delta| / Omega_c <= 1/5 et (D2a)
  contamination c_max <= 1/10. Quand elle echoue, mesurer_point rend HORS DOMAINE et ne produit ni
  chaine ni E-B. La sonde du gel appelle barriere et gamma_chaine directement : la garde n'y joue
  pas, et le gel ne le disait pas (D-CH-7). Machine 2 l'a vu en certifiant, a calcule la garde aux
  douze points sans diagonaliser et l'a consignee avant le run. Machine 1 l'a recalculee : memes
  valeurs a quatre decimales, memes statuts.
  point  D1      c_max   garde du moteur  statut du point
  J1     0.1250  0.0912  EN DOMAINE       FACTEUR 2
  J2     0.1000  0.1042  HORS DOMAINE     HORS DECADE
  J3     0.0556  0.0407  EN DOMAINE       FACTEUR 2
  J4     0.0500  0.0381  EN DOMAINE       FACTEUR 2
  J5     0.0556  0.0547  EN DOMAINE       DECADE
  J6     0.0500  0.0635  EN DOMAINE       FACTEUR 2
  T1     0.0435  0.0321  EN DOMAINE       DECADE
  T2     0.0400  0.0404  EN DOMAINE       FACTEUR 2
  T3     0.2143  0.1550  HORS DOMAINE     HORS DECADE
  T4     0.1500  0.1610  HORS DOMAINE     HORS DECADE
  A1     0.0556  0.0409  EN DOMAINE       FACTEUR 2
  A2     0.0500  0.0510  EN DOMAINE       FACTEUR 2
  Les trois points ou la garde dit HORS DOMAINE (J2, T3, T4) sont les trois points HORS DECADE ; les
  neuf points EN DOMAINE sont FACTEUR 2 ou DECADE. C'est une coincidence entre un statut consigne
  avant le run et un resultat, sur douze points dont trois ; ce n'est ni un test ni un domaine de
  validite, et le gel interdit d'en tirer un. La phrase de machine 2, reprise ici : a J2, T3 et T4
  la garde G-1 du moteur dit HORS DOMAINE ; la sonde lit la chaine sans la consulter ; un verdict a
  J2 est un verdict hors du domaine declare de la chaine.
  Les six points de M17 sont EN DOMAINE (journal de machine 2 ; machine 1 l'a recalcule a A1 et A2).

nn.8 LES ANNONCES DE LA PLUME, COMPTEES (gel, section 10)
  A-1  (0.72)  le verdict est TENU EN PARTIE                         REALISEE
  A-2  (0.55)  J2 est HORS DECADE                                    VRAIE
  A-3  (0.55)  a J2, q du premier juge entre 2.3 et 4.6              VRAIE (3.711)
  A-4  (0.60)  a J1, q du premier juge entre 0.70 et 0.85            FAUSSE (0.950)
  A-5  (0.40)  J3 et J4 tous les deux FACTEUR 2                      VRAIE
  A-6  (0.75)  signe du q median aux points juges lisibles           VRAIE
  A-7  (0.65)  J5 est lisible                                        VRAIE (8 etats juges)
  A-8  (0.95)  la garde G-4 tient                                    VRAIE
  Sept sur huit. Ce que la plume en retient : son attente au-dessus de 2.00 (un rapport qui croit
  comme g^2 / |delta|) a porte : 3.711 est dans l'intervalle annonce ; son attente en dessous ("il
  bouge peu", vers 0.8) etait fausse : a J1 le rapport remonte vers 1. Huit annonces ne mesurent pas
  un calibrage.

nn.9 DEFAUTS ET RESERVES
  D-CH-1 a D-CH-6 (m1) : pris avant le run (lot fa54b6ed68469db8 ; gel, section 2).
  D-CH-7 (m1 ; trouve par machine 2 avant le run, sa reserve R-1) : le gel se tait sur la garde G-1
    du moteur, que la sonde contourne. Un point juge, J2, est hors du domaine que le moteur declare.
  D-CH-8 (m1 ; note de machine 2, section 4 e) : le critere (8) du gel, "max / min <= 2", ne dit pas
    quoi faire d'une valeur de chaine nulle ou negative. La feuille exclut ("chaine instable") ; le
    lecteur independant de machine 2 juge. Un seul point est touche, le temoin T3 : 11 etats juges
    chez machine 1, 13 chez machine 2, meme statut. Le verdict n'en depend pas.
  D-CH-9 (m1 ; reserve R-2) : le selftest de la feuille n'a pas de cas a tous les bords de seuil ;
    il laisse passer neuf alterations d'une ligne sur 24. La certification de la feuille repose sur
    le banc de machine 2.
  D-CH-10 (m1 ; reserve R-3) : ma note disait le bruit des fils "de l'ordre de 1e-12 en absolu" ;
    mesure, il vaut 7.3e-14 entre 16 et 4 fils, 6.7e-14 entre les deux machines.
  R-4 (m2) : a q = racine de 10 exactement la feuille rend HORS DECADE alors que le gel ferme la
    borne. Sans effet : le q le plus proche d'une borne est celui d'un temoin (T1, 0.4977, a 0.5
    pour cent de 1/2) ; aucun n'est pres de la racine de 10.

nn.10 CE QUE LE RESULTAT CHANGE A CE QUI ETAIT ECRIT
  La note 9322566db2546adb lisait, apres coup, un accord chaine / 2D de 0.499 a 1.642 aux six points
  de M17. Sous gel, hors de ces points : l'accord tient a un facteur 2 a quatre points juges, a une
  demi-decade a un cinquieme, et tombe au sixieme. La lecture de cette note n'est donc ni retiree ni
  generale : elle vaut aux points nommes en nn.5.

nn.11 A ARBITRER PAR L'OPERATEUR
  (i) Les numeros (E18) et l'ordre des depots : l'acte de la nuit bis d'abord, celui-ci ensuite.
  (ii) L'ouverture. Seul l'operateur peut attester qu'il a ouvert ce chantier le 14/11 a 00 h 15 ;
      son message de depot le dit ou non. Machine 2 a joue parce que l'envoi le demandait et que
      l'operateur l'a porte.
  (iii) Les trois regles candidates de nn.12, sous (X).
  (iv) La suite. Cet acte n'en propose aucune comme decidee. Trois existent : un nouveau gel qui
      prendrait la garde G-1 du moteur pour domaine et la mettrait a l'epreuve sur des points neufs
      ; la derivation du second ordre de la chaine, que le facteur de J2 (de 2.9 a 4.2 sur treize
      etats) appelle ; ou rien, ce verdict se deposant tel quel.

nn.12 REGLES CANDIDATES SOUS (X) (sans numero tant que l'acte de la nuit bis n'est pas depose)
  (a) (m2, m1) Une sonde qui appelle les fonctions d'un moteur sans passer par ses gardes le dit, et
      consigne le statut de ces gardes a chaque point.
  (b) (m2) Un critere ecrit comme un rapport dit ce qu'il fait d'un terme nul ou negatif.
  (c) (m2, m1) Un selftest porte un cas a chaque bord de seuil ; a defaut, la certification dit sur
      quel banc elle repose.

nn.13 LE CANAL
  Lots echanges pour ce chantier (canons) : machine 1 -- le gel et ses instruments b3d3e23e98914a95
  ; machine 2 -- la certification 3381564852ba6fe4, le resultat 9143062c481ad267. Les enveloppes qui
  les ont portes ne sont pas des lots et ne se citent pas. Le conteneur de machine 1 a tenu du 12 au
  14/11.

nn.14 CE QUE CE DELTA NE FAIT PAS
  Il ne dit pas que la chaine est "qualifiee". Il ne tire aucun domaine de validite. Il ne rejoue
  aucun point, ne relit sous aucun autre palier, aucun autre critere, aucune autre population (gel,
  section 12). Il ne rouvre pas la piste (0). Il ne prend aucun numero, n'adopte aucune regle,
  n'edite aucune piece citee (PB-1).

nn.15 PIECES DU LOT
  journal_delta_nn_chaine_EA_par_etat_v1.md             cet acte
  ecrire_acte_chaine_EA_par_etat_machine1_v1.py         le script qui pose nombres et canons
  verdict_rejoue_machine1.json, lecture_rejouee_machine1.log   la feuille rejouee par machine 1
  releve_acte_chaine_EA_par_etat_machine1_v1.py / .log  le releve de sortie de machine 1
  POUR_MACHINE2_acte_chaine_EA_par_etat_machine1_v1.md  la note d'accompagnement
  fabrique_lot_machine1_v1.py
  Perimetre : la feuille du contresignataire, sur ce texte ; les entrants sont ceux de nn.1.

-- FIN journal_delta_nn_chaine_EA_par_etat_v1 --
