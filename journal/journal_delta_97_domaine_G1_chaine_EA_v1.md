DELTA nn -- LA GARDE G-1 DU MOTEUR ET LA CHAINE E-A PAR ETAT : RUN DU 14/11/2026 SOUS LE GEL
b59651f99e60707a.
VERDICT : LA GARDE NE TIENT PAS (a = 3, b = 3). RIVALE : NON TENUE, A UN ETAT PRES.
-- PROJET, VERSION 1
(plume machine 1 ; run et certification machine 2 ; a contresigner par machine 2)
=======================================================================

nn.0 POSITION
  Ce delta rend le run du gel "la garde G-1 du moteur et la chaine E-A par etat". Sa question : la
  garde de domaine G-1 du moteur, calculee avant toute diagonalisation, dit-elle ou la chaine E-A au
  site entier rend la LECTURE de E-B a k = 3 a une demi-decade pres ? Reponse de la feuille : LA
  GARDE NE TIENT PAS. Trois points que la garde dit EN DOMAINE tombent, trois points qu'elle dit
  HORS DOMAINE tiennent.
  Ce chantier n'est pas la piste (0) : il ne requalifie pas E-B, et aucune phrase d'ici ne dit
  "largeur" sans "lue a k = 3". Il a ete ouvert par l'operateur ("Ouvre !", le 14/11/2026 a 14 h 57,
  a machine 1) ; machine 2 ne peut pas le verifier sur piece (nn.11).
  Registre a l'ecriture : origin/main 04053e0, plafond 96 (releve du 14/11 au soir). Les deltas 95
  et 96 y sont depuis le 14/11 a 14 h 12 et 14 h 13. Aucun numero n'est pris ici (E18).

nn.1 PIECES (convention B)
  Au registre (04053e0)
    scripts/m17_chaine_v17.py  82a0be882568fe0c
        le moteur ; sa garde G-1 est garde_domaine
    gels/gel_chaine_EA_par_etat_pre_enregistrement_v1.md  9df2702af59adbbc
        le gel precedent
    journal/journal_delta_96_chaine_EA_par_etat_v1.md  aed8677322e20e0d
        son acte : la coincidence que ce gel eprouve
  Hors registre, de machine 1 (lot 1aafb301d7d0ebb3)
    gel_domaine_G1_chaine_EA_pre_enregistrement_v1.md  b59651f99e60707a
        le gel
    sonde_domaine_G1_machine1_v1.py  940a21b1d562bb49
        la sonde : elle mesure et ne juge pas
    lecture_domaine_G1_machine1_v1.py  0a760e3a244e547d
        la feuille : elle juge et ne mesure pas
  Hors registre, de machine 2
    lot de certification  d92a200ac348f0a3
        certification du gel, de la sonde et de la feuille, AVANT le run
      POUR_MACHINE1_certification_gel_domaine_G1_machine2_v1.md  c3092a2dfbbcf462
          la note : 0 morsure, quatre reserves
      domaine_G1/garde_et_boites_machine2_v1.log  bfe10d4347e93202
          la garde et la boite recalculees aux quatorze points
      domaine_G1/banc_feuille_domaine_G1_machine2_v1.log  3f93d8747fd6a4ca
          le banc de la feuille
    lot de resultat  86a677dc0ff8ba9d
        le run, sa lecture, les controles de machine 2
      domaine_G1/sortie/sonde_domaine_G1.json  d51a9c6ce98b0452
          les mesures : quatorze points, 196 etats
      domaine_G1/sortie/verdict_domaine_G1.json  955c4ee53bc2e5d5
          le verdict rendu par la feuille sur BOCAL4
      domaine_G1/sortie/lecture_domaine_G1.log  1ee031ea89823525
          son journal
      POUR_MACHINE1_resultat_domaine_G1_machine2_v1.md  7d4558a5322b2b00
          la note de machine 2
      domaine_G1/sortie/stabilite_sous_bruit_machine2.log  464b1e04a3fabd25
          les statuts sous le bruit des fils
      domaine_G1/sortie/stabilite_cascade_machine2.log  840acb8d6032e566
          le verdict et la rivale sous ce bruit
      domaine_G1/sortie/relecture_independante_machine2.log  240d94da00442ee0
          son lecteur independant, 0 ecart
      domaine_G1/sortie/compare_run_essai_ancres_machine2.log  d6759636a140b472
          les ancres du run contre son essai
  De ce lot
    verdict_rejoue_machine1.json  955c4ee53bc2e5d5
        la feuille rejouee par machine 1 sur le JSON de la sonde
    lecture_rejouee_machine1.log  31aa65c9983b79a4
        son journal

nn.2 CE QUI A ETE JOUE, ET PAR QUI (E19)
  Machine 2, AVANT le run (lot d92a200ac348f0a3) : 11 controles de lecture du gel, 0 morsure ; la
  garde du moteur et la boite recalculees aux quatorze points, egales a la table du gel a six
  decimales, et la garde identique au bit a 16 fils et a 1 fil ; un lecteur independant, ecrit du
  texte du gel, compare a la feuille sur 4000 sondes synthetiques tirees aux bords des seuils, 0
  ecart ; la cascade enumeree sur les 531441 vecteurs de classes des douze points : quand la garde
  separe, la rivale n'est jamais tenue ; 59 alterations d'une ligne de la feuille, dont 9 survivent
  au selftest de la feuille et une seule a son banc (equivalente en pratique) ; l'essai aux deux
  ancres rejoue, 28 etats au bit. Quatre reserves, aucune morsure (nn.9).
  Machine 2, le run (lot 86a677dc0ff8ba9d) : BOCAL4, Windows AMD64, python 3.11.9, numpy 2.2.6, 16
  coeurs, variables de fils non fixees ; le 14/11 de 18:59:46 a 19:50:14 ; sonde code 0 en 3028 s,
  feuille code 0 ; un seul run, aucun arret, aucune reprise, aucun point rejoue. Temoin d'arrondi
  0x1.a483018a169c6p+64. Le run a ete joue sur batterie (70 pour cent en decharge a 19:45,
  processeur a 2516 MHz pour un maximum de 3801) : chaque point dure de 1.5 a 1.6 fois un point de
  meme boite du run precedent, d'ou 3028 s contre l'ordre de 2000 s que le gel annoncait. Les
  nombres n'en dependent pas : les deux ancres rendent, au bit, les valeurs de l'essai de la
  certification.
  Machine 1 : a rejoue la feuille (selftest 74 sur 74) sur le JSON de la sonde de machine 2. Son
  verdict est identique a celui que machine 2 rend, au canon (955c4ee53bc2e5d5), et son journal
  identique hors la ligne de titre. Machine 1 n'a joue la sonde a aucun des douze points E1 a E6 et
  H1 a H6, ni avant ni apres le run ; elle l'avait jouee aux deux ancres (essai a blanc du gel).

nn.3 LES GARDES
  G-1 le moteur lu par la sonde est au canon. G-2 les quatorze points sont presents, au role, au w2
  et au facteur du gel. G-3 chacun porte 14 etats (196). G-4 les deux ancres rendent la lecture du
  run de M17 avec un ecart relatif NUL sur BOCAL4 (etat (7,2) a A1, etat (8,2) a A2). G-5 la feuille
  passe son selftest. G-6 a chacun des quatorze points la garde du moteur consignee par la sonde est
  sans erreur, au statut de la table du gel, et ses D1 et c_max sont ceux de la table a moins de
  5e-7 pres (tolerance du gel : 5e-5). Aucune garde ne mord.

nn.4 LES QUATORZE POINTS (q = Gamma_chaine / Gamma_2D lue a k = 3, sur les etats juges)
  pt  garde  w2    g     statut       classe   juges  q min  q max  med.   premier juge
  E1  EN     2.08  x1    DECADE       TENU     13     1.888  2.832  2.529  (8,2) q = 2.529
  E2  EN     2.09  x1    HORS DECADE  TOMBE    13     2.305  3.510  3.094  (8,2) q = 3.094
  E3  EN     2.10  x3/2  HORS DECADE  TOMBE    13     2.337  3.434  2.867  (6,1) q = 3.131
  E4  EN     2.12  x3/2  HORS DECADE  TOMBE    12     3.620  4.615  4.005  (6,1) q = 4.018
  E5  EN     1.91  x1    FACTEUR 2    TENU     12     0.596  1.095  0.845  (7,2) q = 0.906
  E6  EN     1.90  x3/2  FACTEUR 2    TENU     13     0.726  1.383  0.934  (5,2) q = 0.920
  H1  HORS   2.08  x2/3  HORS DECADE  TOMBE     8     2.325  3.169  2.759  (10,3) q = 2.897
  H2  HORS   2.10  x2/3  HORS DECADE  TOMBE     9     3.750  5.961  5.065  (11,2) q = 5.961
  H3  HORS   2.12  x1    HORS DECADE  TOMBE    14     4.526  6.987  5.909  (8,2) q = 5.981
  H4  HORS   1.91  x2/3  DECADE       TENU      7     0.375  0.746  0.605  (10,3) q = 0.746
  H5  HORS   1.90  x2/3  FACTEUR 2    TENU      6     0.506  0.814  0.662  (10,3) q = 0.793
  H6  HORS   1.89  x1    FACTEUR 2    TENU     11     0.659  1.234  0.958  (7,2) q = 0.996
  A1  EN     1.95  x1    FACTEUR 2    (ancre)  11     0.587  0.882  0.758  (7,2) q = 0.819
  A2  EN     2.05  x1    FACTEUR 2    (ancre)  12     1.292  1.629  1.505  (8,2) q = 1.474
  Exclus, par premier motif :
    E1  sous dix planchers 1
    E2  sous dix planchers 1
    E3  J flou 1
    E4  J flou 2
    E5  sous dix planchers 2
    E6  J flou 1
    H1  sous dix planchers 6
    H2  sous dix planchers 5
    H3  aucun
    H4  sous dix planchers 7
    H5  J flou 1 ; sous dix planchers 7
    H6  sous dix planchers 3
    A1  barriere vide 1 ; sous dix planchers 2
    A2  sous dix planchers 2
  "garde" : EN pour EN DOMAINE, HORS pour HORS DOMAINE, statut de la garde G-1 du moteur consigne
  par la sonde. "g" est le facteur sur la regle g_du_point du moteur. "Premier juge" : l'etat juge
  de plus grand recouvrement avec la graine. Les deux ancres sont hors cascade. 154 etats juges sur
  196.

nn.5 LE VERDICT
  Les six points juges EN DOMAINE et les six points juges HORS DOMAINE sont lisibles. a = 3 : E2, E3
  et E4, EN DOMAINE, sont TOMBES. b = 3 : H4, H5 et H6, HORS DOMAINE, sont TENUS. La cascade du gel
  (section 7) rend LA GARDE NE TIENT PAS.
  Ce que le gel fait ecrire (section 12) : la coincidence de l'acte aed8677322e20e0d etait une
  coincidence ; la garde G-1 n'est pas le domaine de validite de la chaine par etat ; l'acte nomme
  les points. Les voici.
    - EN DOMAINE et TOMBES. E2 (2.09, facteur 1) : la chaine surestime la lecture d'un facteur 2.305
      a 3.510 sur ses 13 etats juges, dont 6 hors de la demi-decade ; le plus grand q depasse la
      borne de 11.0 pour cent. E3 (2.10, facteur 3/2) : de 2.337 a 3.434, 3 etats sur 13 hors de la
      demi-decade, le plus grand la depassant de 8.6 pour cent. E4 (2.12, facteur 3/2) : de 3.620 a
      4.615, les 12 etats juges hors de la demi-decade, le plus petit la depassant de 14.5 pour
      cent.
    - EN DOMAINE et TENUS. E1 (2.08, facteur 1) est DECADE : q de 1.888 a 2.832, 12 etats juges sur
      13 au-dessus de 2. E5 (1.91, facteur 1) et E6 (1.90, facteur 3/2) sont FACTEUR 2.
    - HORS DOMAINE et TENUS. H4 (1.91, facteur 2/3) est DECADE : q de 0.375 a 0.746, 2 etats juges
      sur 7 sous 1/2. H5 (1.90, facteur 2/3) est FACTEUR 2 avec 6 etats juges, le minimum du gel. H6
      (1.89, facteur 1) est FACTEUR 2.
    - HORS DOMAINE et TOMBES. H2 (2.10, facteur 2/3) et H3 (2.12, facteur 1) : tous leurs etats
      juges sont hors de la demi-decade (9 et 14). H1 (2.08, facteur 2/3) tombe par un seul etat
      (nn.6).
  Aucune largeur intrinseque n'est affirmee. Les verdicts PAS DE SIGNAL de M17, NON QUALIFIE du
  delta 95 et TENU EN PARTIE du delta 96 ne sont pas touches.

nn.6 LA RIVALE, ET CE QUI LA TIENT
  La rivale du gel (section 8) : au-dessus de 2.00, a w2 fixe, la classe d'un point ne depend pas du
  facteur. Elle se lit sur P1, P2, P3. P2 (E3, H2) et P3 (E4, H3) sont HOMOGENES : leurs deux points
  tombent. P1 (E1, H1) est HETEROGENE : E1 tient, H1 tombe. La feuille rend RIVALE NON TENUE.
  Cette issue tient a UN etat, et machine 2 l'a montre (sa lecture sous le bruit des fils, sans
  verdict). H1 tombe par un seul de ses 8 etats juges : rang 1, etiquette (11,2), Gamma_2D(3) =
  5.24e-12, q = 3.1688, a 0.21 pour cent au-dessus de la borne de la demi-decade (3.1623). Le bruit
  des fils sur la cible, 7.32e-14 en absolu, vaut 1.4 pour cent de cette lecture ; il a ete mesure
  aux boites des ancres (N = 60 et 61) et pas a celle de H1 (N = 74), le gel interdisant de rejouer
  un point. Si cet etat passait sous la borne, H1 serait DECADE, P1 HOMOGENE, et la rivale TENUE.
  Le verdict sur la garde, lui, ne depend pas de ce bruit : machine 2 enumere tous les cas et n'en
  trouve qu'un, LA GARDE NE TIENT PAS ; aucun etat de E2, E3 ou E4 n'est incertain.
  Ce que l'acte en fait. Il applique la section 12 du gel : la lecture (iii) de sa section 2, "le
  desaccord seul compte", est retiree comme enonce general. Il dit que cette issue tient a un etat
  dans le bruit. Et il rend la lecture declaree des q medians par paire (gel, section 10), qui ne
  depend pas de cet etat :
    paire  w2    point EN DOMAINE        point HORS DOMAINE      lecture de la paire
    P1     2.08  E1 facteur 1    2.529    H1 facteur 2/3  2.759    HETEROGENE
    P2     2.10  E3 facteur 3/2  2.867    H2 facteur 2/3  5.065    HOMOGENE
    P3     2.12  E4 facteur 3/2  4.005    H3 facteur 1    5.909    HOMOGENE
    P4     1.91  E5 facteur 1    0.845    H4 facteur 2/3  0.605    HOMOGENE
    P5     1.90  E6 facteur 3/2  0.934    H5 facteur 2/3  0.662    HOMOGENE
  Dans les cinq paires, le point au plus petit facteur a le q median le plus loin de 1. A 2.10 le
  run precedent avait lu 3.735 a facteur 1 (J2) : ce w2 porte donc trois facteurs, 2.867 (3/2),
  3.735 (1) et 5.065 (2/3). A 2.05 il avait lu 1.418 (3/2), 1.505 (1) et 1.503 (2/3). Entre les
  facteurs 2/3 et 3/2, le rapport des q medians vaut 1.06 a 2.05 et 1.77 a 2.10. Ces lectures
  decrivent ; elles ne rejouent aucun seuil et ne tirent aucune frontiere.

nn.7 LECTURES SANS VERDICT (gel, section 10)
  (a) De part et d'autre de 2.00. Au-dessous, les cinq points juges (E5, E6, H4, H5, H6) sont TENUS,
  que la garde les dise EN DOMAINE ou HORS DOMAINE. Au-dessus, des sept points juges un seul est
  TENU, E1, et il est DECADE. Aucune frontiere en w2 n'en est tiree (gel, section 12).
  (b) Le sens. Aux quatorze points, le q median est sous 1 quand w2 < 2 et au-dessus de 1 quand w2 >
  2.
  (c) Les exclus. A facteur 2/3 le motif "sous dix planchers" ecarte de 5 a 7 etats sur 14 (H1 6, H2
  5, H4 7, H5 7) ; H5 n'a que 6 etats juges : un de moins et le point etait NON LISIBLE, sans effet
  sur le verdict.
  (d) Le bruit des fils, lu par machine 2 : les statuts de onze points juges sur douze et des deux
  ancres ne changent ni dans le pire ni dans le meilleur sens ; le douzieme est H1 (nn.6). Le bruit
  relatif maximal sur les 154 etats juges est 5.5 pour cent, a E6 rang 8, sans effet sur une classe.
  (e) Les ancres rendent les lectures du run precedent : q de 0.587 a 0.882 a A1, de 1.292 a 1.629 a
  A2.

nn.8 LES ANNONCES DE LA PLUME, COMPTEES (gel, section 11)
  A-1   (0.74)  le verdict est LA GARDE NE TIENT PAS             REALISEE
  A-2   (0.75)  E3 est HORS DECADE                               VRAIE
  A-3   (0.85)  E4 est HORS DECADE                               VRAIE
  A-4   (0.55)  E2 est HORS DECADE                               VRAIE
  A-5   (0.75)  E1 est DECADE                                    VRAIE
  A-6   (0.70)  H1 est TENU                                      FAUSSE (HORS DECADE, par un etat)
  A-7   (0.75)  H6 est TENU                                      VRAIE
  A-8   (0.40)  la rivale est TENUE                              FAUSSE (NON TENUE, par un etat)
  A-9   (0.60)  a E3, le q median entre 3.0 et 4.5               FAUSSE (2.867)
  A-10  (0.80)  E5 et E6 tous les deux TENUS                     VRAIE
  A-11  (0.50)  H4 ou H5, l'un au moins, HORS DECADE             FAUSSE (DECADE et FACTEUR 2)
  A-12  (0.85)  signe du q median aux points juges lisibles      VRAIE
  A-13  (0.95)  la garde G-4 tient ; (0.97) la garde G-6 tient   VRAIES
  Neuf sur treize, comme machine 2 les compte. Ce que la plume en retient. Elle attendait que la
  garde tombe, et par E3 et E4 : c'est arrive. Mais la lecture qu'elle lui opposait etait trop
  simple : elle donnait 0.60 a un q median de E3 dans l'intervalle de J2 (de 3.0 a 4.5) et il vaut
  2.867 ; elle donnait une chance sur deux a la chute d'un point a facteur 2/3 au-dessous de 2.00,
  et les deux tiennent. Treize annonces ne mesurent pas un calibrage.

nn.9 DEFAUTS ET RESERVES
  D-G1-1 (m1 ; reserve R-1 de machine 2) : le selftest de la feuille construit ses cas depuis la
    table qu'il devrait eprouver ; une faute dans cette table (un c_max, un statut, la reference
    d'une ancre) le passe. Neuf des 59 alterations de machine 2 le montrent. La certification de la
    feuille repose sur le banc de machine 2 et sur son controle de la table contre le texte du gel.
  D-G1-2 (m1 ; reserve R-3 de machine 2) : le gel cite le registre a fe10bfe et dit "hors registre"
    les actes de la nuit bis et de la chaine. Ils etaient deposes depuis le 14/11 a 14 h 12 et 14 h
    13 (deltas 95 et 96, 04053e0), avant l'ouverture de ce chantier. La plume n'a pas releve la tete
    du registre avant d'ecrire. Le gel est scelle (PB-1) ; cet acte cite les noms deposes.
  D-G1-3 (m1 ; declare au gel, section 2) : la plume a conseille ce gel a l'operateur en lui
    annoncant que la garde tiendrait a 70 chances sur 100, avant d'avoir calcule la garde sur une
    grille, ce qui ne demandait aucun run. Le calcul fait, elle a annonce l'inverse (0.74 qu'elle ne
    tienne pas) et l'a ecrit a l'operateur avant de finir le gel.
  D-G1-4 (m1 ; reserve R-2 de machine 2) : la regle "un seul etat juge hors de la demi-decade fait
    tomber le point" ne porte aucune marge au bruit de l'instrument. Voulue pour le verdict sur la
    garde, ou elle n'a rien coute, elle passe a la rivale, dont l'issue tient a un etat a 0.21 pour
    cent de la borne (nn.6).
  R-4 (m2) : l'ouverture n'est pas verifiable sur piece par machine 2 (nn.11).

nn.10 CE QUE LE RESULTAT CHANGE A CE QUI ETAIT ECRIT
  Delta 96, section nn.7 : les trois points ou la garde disait HORS DOMAINE etaient les trois points
  HORS DECADE, et l'acte ecrivait "coincidence". Mise a l'epreuve sur douze points neufs, elle ne se
  reproduit pas : six points sur douze contredisent la garde, trois dans chaque sens. La phrase du
  delta 96, "un verdict a J2 est un verdict hors du domaine declare de la chaine", reste vraie de la
  garde du moteur ; mais cette garde ne dit pas ou la chaine par etat rend la lecture de E-B.
  Gel b59651f99e60707a, section 2 (iii) : "si le desaccord seul compte" est retire comme enonce
  general (nn.6).
  Le defaut D-CH-7 du delta 96 (une sonde qui contourne la garde sans le dire) reste un defaut de
  forme, et la sonde de ce gel le corrige ; il n'etait pas la cause de la chute de J2.

nn.11 A ARBITRER PAR L'OPERATEUR
  (i) Le numero (E18) et le depot.
  (ii) L'ouverture. Seul l'operateur peut attester qu'il a ouvert ce chantier le 14/11 a 14 h 57 ;
      son message de depot le dit ou non. Machine 2 a joue parce que l'envoi le demandait et que
      l'operateur l'a porte.
  (iii) Les trois regles candidates de nn.12, sous (X).
  (iv) La suite. Cet acte n'en propose aucune comme decidee. Trois existent : deriver le residuel de
      la chaine, que les lectures de nn.6 decrivent sans l'expliquer (il change de sens a 2.00,
      croit avec le desaccord et depend du facteur) ; un nouveau gel sur un autre domaine declare,
      ecrit avant tout run ; ou rien, ce verdict se deposant tel quel.

nn.12 REGLES CANDIDATES SOUS (X) (numerotees au depot ; trente et une attendent deja la revue)
  (a) (m2, m1) Un selftest ne construit pas ses cas depuis la table qu'il doit eprouver ; a defaut,
      la certification dit quel controle tient cette table.
  (b) (m2, m1) Un critere qui fait tomber un point ou une issue sur un seul etat dit sa marge au
      bruit de l'instrument, et la lecture sous ce bruit se rend avec le verdict.
  (c) (m1) Avant d'ecrire un gel, la plume releve la tete du registre ; avant d'en conseiller un,
      elle calcule ce qui se calcule sans run.

nn.13 LE CANAL
  Lots echanges pour ce chantier (canons) : machine 1 -- le gel et ses instruments
  1aafb301d7d0ebb3 ; machine 2 -- la certification d92a200ac348f0a3, le resultat 86a677dc0ff8ba9d.
  Les enveloppes qui les ont portes ne sont pas des lots et ne se citent pas.

nn.14 CE QUE CE DELTA NE FAIT PAS
  Il ne tire aucun domaine de validite et aucune frontiere en w2. Il ne dit pas que la chaine est
  "qualifiee", ni qu'elle est disqualifiee : elle tient aux points nommes et tombe aux points
  nommes. Il ne rejoue aucun point, ne relit sous aucun autre palier, aucun autre critere, aucune
  autre paire, aucune autre population (gel, section 13). Il ne rouvre pas la piste (0). Il ne prend
  aucun numero, n'adopte aucune regle, n'edite aucune piece citee (PB-1).

nn.15 PIECES DU LOT
  journal_delta_nn_domaine_G1_chaine_EA_v1.md           cet acte
  ecrire_acte_domaine_G1_machine1_v1.py                 le script qui pose nombres et canons
  verdict_rejoue_machine1.json, lecture_rejouee_machine1.log   la feuille rejouee par machine 1
  releve_acte_domaine_G1_machine1_v1.py / .log          le releve de sortie de machine 1
  contre_epreuve_releve_machine1_v1.py / .log           ce releve, sur des copies alterees de l'acte
  POUR_MACHINE2_acte_domaine_G1_machine1_v1.md          la note d'accompagnement
  fabrique_lot_machine1_v2.py
  Perimetre : la feuille du contresignataire, sur ce texte ; les entrants sont ceux de nn.1.

-- FIN journal_delta_nn_domaine_G1_chaine_EA_v1 --
