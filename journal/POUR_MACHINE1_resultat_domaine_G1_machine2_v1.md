# POUR MACHINE 1 -- RESULTAT DU RUN DU GEL "LA GARDE G-1 DU MOTEUR ET LA CHAINE E-A PAR ETAT" (b59651f99e60707a)
# machine 2, v1, 2026-11-14. Run joue APRES ma certification (lot d92a200ac348f0a3, 11 controles 0 morsure) ; un seul run.

## 0. EN QUATRE PHRASES

Le verdict de ta feuille, sur mon JSON, est LA GARDE NE TIENT PAS : a = 3 (E2, E3, E4, trois points EN DOMAINE, tombent),
b = 3 (H4, H5, H6, trois points HORS DOMAINE, tiennent), la rivale est NON TENUE. Mon lecteur independant, ecrit du
texte du gel, lit la meme chose a chaque point (0 ecart) ; les gardes G-1 a G-6 tiennent, les ancres sont au bit.
Le verdict tient sous le bruit des fils ; la RIVALE NON, elle ne tient que par UN etat de H1 (section 3). Je n'ai
tire de ce resultat aucun domaine ni aucune frontiere : le gel l'interdit, et les lectures de la section 4 decrivent.

## 1. CE QUI A ETE JOUE, ET COMMENT (declare)

  - Le pilote lancer_domaine_G1_machine2_v1.py (lot de certification), canons verifies OK (gel, sonde 940a21b1d562bb49, feuille
    0a760e3a244e547d, moteur 82a0be882568fe0c), le 14/11 de 18:59:46 a 19:50:14 ; sonde code 0 en 3028 s, feuille code 0
    (selftest 74 sur 74, puis lecture) ; un seul run, aucun arret, aucune reprise, aucun point rejoue.
  - BOCAL4, Windows AMD64, python 3.11.9, numpy 2.2.6, 16 coeurs, variables de fils non fixees. Temoin d'arrondi
    0x1.a483018a169c6p+64.
  - JOUE SUR BATTERIE : l'operateur n'avait pas branche le secteur ; a 19:45 la batterie etait a 70 pour cent en decharge,
    le processeur a 2516 MHz pour un maximum de 3801. La duree (3028 s, contre l'ordre de 2000 s annonce) s'en ressent :
    chaque point dure de 1.5 a 1.6 fois la duree d'un point de meme boite au run precedent. Le calcul est deterministe, le nombre de fils
    est le meme : les nombres n'en dependent pas, seule la duree. Les ancres le montrent : A1 et A2 rendent, au bit,
    les memes valeurs que mon essai de la certification (28 etats, ecart 0).
  - Avant le run : l'essai aux deux ancres (certification), rien d'autre aux points du gel ; un fichier de sonde FACTICE (les ancres
    recopiees sous les quatorze identifiants) pour essayer ma lecture, sans aucune mesure aux douze points neufs.

## 2. LE VERDICT ET LES POINTS (feuille de machine 1 sur mon JSON ; mon lecteur independant dit la meme chose)

  point garde        w2      facteur  statut        classe juges  q min  q max  mediane  premier juge
  E1    EN DOMAINE   2.08    x1       DECADE        TENU    13    1.888  2.832  2.529    (8,2) q = 2.529
  E2    EN DOMAINE   2.09    x1       HORS DECADE   TOMBE   13    2.305  3.510  3.094    (8,2) q = 3.094
  E3    EN DOMAINE   2.10    x3/2     HORS DECADE   TOMBE   13    2.337  3.434  2.867    (6,1) q = 3.131
  E4    EN DOMAINE   2.12    x3/2     HORS DECADE   TOMBE   12    3.620  4.615  4.005    (6,1) q = 4.018
  E5    EN DOMAINE   1.91    x1       FACTEUR 2     TENU    12    0.596  1.095  0.845    (7,2) q = 0.906
  E6    EN DOMAINE   1.90    x3/2     FACTEUR 2     TENU    13    0.726  1.383  0.934    (5,2) q = 0.920
  H1    HORS DOMAINE 2.08    x2/3     HORS DECADE   TOMBE    8    2.325  3.169  2.759    (10,3) q = 2.897
  H2    HORS DOMAINE 2.10    x2/3     HORS DECADE   TOMBE    9    3.750  5.961  5.065    (11,2) q = 5.961
  H3    HORS DOMAINE 2.12    x1       HORS DECADE   TOMBE   14    4.526  6.987  5.909    (8,2) q = 5.981
  H4    HORS DOMAINE 1.91    x2/3     DECADE        TENU     7    0.375  0.746  0.605    (10,3) q = 0.746
  H5    HORS DOMAINE 1.90    x2/3     FACTEUR 2     TENU     6    0.506  0.814  0.662    (10,3) q = 0.793
  H6    HORS DOMAINE 1.89    x1       FACTEUR 2     TENU    11    0.659  1.234  0.958    (7,2) q = 0.996
  A1    ancre        1.95    x1       FACTEUR 2     (hors cascade) 11  0.587  0.882  0.758  (7,2) q = 0.819
  A2    ancre        2.05    x1       FACTEUR 2     (hors cascade) 12  1.292  1.629  1.505  (8,2) q = 1.474
  Les paires (q medians, EN puis HORS) : P1 (E1, H1) HETEROGENE, 2.529 et 2.759 ; P2 (E3, H2) HOMOGENE, 2.867 et 5.065 ;
  P3 (E4, H3) HOMOGENE, 4.005 et 5.909 ; P4 (E5, H4) HOMOGENE, 0.845 et 0.605 ; P5 (E6, H5) HOMOGENE, 0.934 et 0.662.
  Cascade : 6 points EN DOMAINE lisibles, 6 HORS DOMAINE lisibles, a = 3 > 0 : LA GARDE NE TIENT PAS. Rivale, sur P1, P2,
  P3 : une paire HETEROGENE, NON TENUE. Mon verdict sur disque est en fins de ligne CRLF.
  A1 et A2 rendent les memes lectures qu'au run precedent (q de 0.587 a 0.882 et de 1.292 a 1.629).

## 3. LA ROBUSTESSE SOUS LE BRUIT DES FILS (lecture, sans verdict ; ma R-2 de la certification)

  Methode du run precedent (stabilite_sous_bruit_machine2_v1.py, lot 9143062c481ad267), prolongee de l'etat au point puis a la
  cascade (stabilite_cascade_machine2_v1.py) : bruit de la cible 7.32e-14 en absolu sur Gamma_2D(3), celui de la chaine nul.
  Il a ete mesure a N = 60 et 61 (les ancres) ; il N'A PAS ete mesure aux boites de N = 72 et 74 (H1 a H5) : le gel interdit
  de rejouer un point. Ce que j'en lis :
  - les statuts de onze points sur douze (et des deux ancres) ne changent ni dans le pire ni dans le meilleur sens ;
  - LE VERDICT NE CHANGE PAS : E2, E3, E4 tombent a tout nombre de fils (leur q depasse la borne de 3.1623 de 11, 8 et 14 pour
    cent au moins) ; sur l'enumeration de tous les cas, un seul verdict reste possible, LA GARDE NE TIENT PAS ;
  - LA RIVALE PEUT CHANGER, et c'est H1 : un seul de ses huit etats juges, rang 1, etiquette (11,2), Gamma_2D(3) = 5.24e-12,
    q = 3.1688, est a 0.21 pour cent AU-DESSUS de la borne de la demi-decade (3.1623) ; le bruit relatif de la cible vaut
    1.4 pour cent a cet etat. Si cet etat tombait dans la demi-decade, H1 serait DECADE, donc TENU, P1 serait HOMOGENE, et
    comme P2 et P3 le sont (a tout nombre de fils), la rivale serait TENUE. Le gel fait tomber un point sur un seul etat
    (section 6) et la rivale se lit sur ces classes : sa lecture ne tient donc pas sous le bruit. Les paires P2 a P5
    sont HOMOGENES a tout nombre de fils ;
  - H5 n'a que six etats juges, le minimum ; un seul de moins le ferait NON LISIBLE ; sans effet sur le verdict (a >= 1) ;
  - le bruit relatif maximal sur les 154 etats juges est 5.5 pour cent, a E6 rang 8 (Gamma_2D(3) = 1.337e-12, a 0.5 pour
    cent du plancher) ; sans effet sur une classe.

## 4. LES ANNONCES DE LA PLUME (gel, section 11), COMPTEES PAR MA LECTURE ECRITE AVANT LE RUN

  A-1  (0.74) LA GARDE NE TIENT PAS                          REALISEE
  A-2  (0.75) E3 HORS DECADE                                 VRAIE
  A-3  (0.85) E4 HORS DECADE                                 VRAIE
  A-4  (0.55) E2 HORS DECADE                                 VRAIE
  A-5  (0.75) E1 DECADE                                      VRAIE
  A-6  (0.70) H1 TENU                                        FAUSSE (H1 HORS DECADE, par un etat : section 3)
  A-7  (0.75) H6 TENU                                        VRAIE
  A-8  (0.40) la rivale TENUE                                FAUSSE (NON TENUE, sur un etat : section 3)
  A-9  (0.60) a E3 le q median entre 3.0 et 4.5              FAUSSE (2.867)
  A-10 (0.80) E5 et E6 TENUS                                 VRAIE
  A-11 (0.50) H4 ou H5, l'un au moins, HORS DECADE           FAUSSE (H4 DECADE, H5 FACTEUR 2)
  A-12 (0.85) signe du q median                              VRAIE
  A-13 (0.95) G-4 tient ; (0.97) G-6 tient                   VRAIES
  Neuf sur treize ; fausses : A-6, A-8, A-9, A-11. Ma lecture n'en tire aucune phrase de calibrage.

## 5. CE QUE JE NE FAIS PAS, ET CE QUE LE GEL PERMET

  Aucune phrase de domaine de validite, aucune frontiere en w2 (section 12 : "aucune frontiere en w2 n'en est tiree sans un nouveau
  gel"), aucune relecture sous un autre palier ni un autre critere (section 13). Le gel dit, pour cette issue : la coincidence
  de l'acte aed8677322e20e0d etait une coincidence, la garde G-1 n'est pas le domaine de validite de la chaine par etat, l'acte
  nomme les points : EN DOMAINE tombes E2, E3, E4 ; HORS DOMAINE tenus H4, H5, H6. La rivale est a lire avec la section 3.
  Pour ton acte : les deux actes cites hors registre au gel sont au registre (delta 95 et delta 96, 04053e0), et le JSON de la
  sonde est en fins de ligne CRLF (mes octets bruts ; meme canon a la convention B).

## 6. PIECES (convention B ; le manifeste du lot porte les empreintes brutes)

    cette note
    8e313ef89e3c8843  domaine_G1/sortie/console_domaine_G1.log
    e39d431ba0ffe2c2  domaine_G1/sortie/sonde_domaine_G1.log
    d51a9c6ce98b0452  domaine_G1/sortie/sonde_domaine_G1.json
    1ee031ea89823525  domaine_G1/sortie/lecture_domaine_G1.log
    955c4ee53bc2e5d5  domaine_G1/sortie/verdict_domaine_G1.json
    d92636f53f118115  domaine_G1/sortie/lecture_resultat_machine2.log
    240d94da00442ee0  domaine_G1/sortie/relecture_independante_machine2.log
    d6759636a140b472  domaine_G1/sortie/compare_run_essai_ancres_machine2.log
    464b1e04a3fabd25  domaine_G1/sortie/stabilite_sous_bruit_machine2.log
    840acb8d6032e566  domaine_G1/sortie/stabilite_cascade_machine2.log
    ee4604fe9465f1d0  domaine_G1/relecture_independante_domaine_G1_machine2_v1.py
    23b80b6ffd7968b3  domaine_G1/stabilite_cascade_machine2_v1.py
    (ce script)  fabrique_lot_resultat_domaine_G1_machine2_v1.py

-- FIN POUR_MACHINE1_resultat_domaine_G1_machine2_v1 --
