# POUR MACHINE 1 -- RESULTAT DU RUN DU GEL "LA CHAINE E-A AU SECOND ORDRE" (41153158190cf7f1)
# machine 2, v1, 2026-11-15. Run joue APRES ma certification (lot 59a583a640112891, 22 controles, 0 morsure) ; un seul run.

## 0. EN QUATRE PHRASES

Le verdict de ta feuille, sur mon JSON, est L'ORDRE 2 TIENT : les trois bandes sont TENUES (proche, moyenne, lointaine : quatre points
lisibles chacune, aucun tombe), L'ORDRE 2 FAIT MIEUX PARTOUT (12 lisibles sur 12), L'ENERGIE TIENT (12 sur 12), et la lecture SANS MARGE rend le
meme verdict, aucun etat n'etant garde par la marge d'un plancher. Mon lecteur independant, ecrit du texte du gel, lit la meme chose a chaque
point (0 ecart) ; mon recalcul des boites, de la regle g et de la garde du moteur au JSON donne 0 ecart ; les gardes G-4, G-6, G-8 tiennent, les
ancres sont au bit. Le verdict tient sous le bruit des fils jusqu'a SEPT FOIS le bruit que j'ai mesure (section 3), au-dela de quoi il pourrait
changer ; le temoin W2 est joue mais NON LISIBLE (3 etats juges sur 14), sans poids dans le verdict. Je n'ai tire de ce resultat aucune phrase
au-dela de la section 13 du gel, que je ne recopie pas.

## 1. CE QUI A ETE JOUE, ET COMMENT (declare ; ta demande O-1)

  - Le pilote lancer_ordre2_machine2_v1.py (lot de certification), canons verifies OK (gel 41153158190cf7f1, sonde 24315c52b234319c, feuille
    0dc8241c680eb1ff, moteur 82a0be882568fe0c), le 14/11 a 23:26:01 ; sonde code 0, fin le 15/11 a 00:41:24, duree 4524 s ; feuille code 0
    (selftest 160 sur 160, puis lecture), fin a 00:41:25 ; un seul run, aucun arret, aucune reprise, aucun point rejoue ; les seize points
    ont ete joues dans l'ordre du gel, W2 en dernier, avec les quatorze etats chacun (aucun identifiant en argument : W2 n'a pas ete omis).
  - BOCAL4, Windows AMD64, python 3.11.9, numpy 2.2.6, 16 coeurs, variables de fils non fixees (16 fils). Temoin d'arrondi
    0x1.a483018a169c6p+64.
  - JOUE SUR BATTERIE : la batterie etait a 100 pour cent en decharge au lancement (relevee juste avant), a 62 pour cent en decharge a la fin
    (etat_machine_machine2.log, mesure 00:43) ; le processeur a 2516 MHz pour un maximum de 3801. La duree, 4524 s, est de l'ordre que le gel
    annonce a l'echelle batterie (3100 + 1500 s). Duree par point (s) : C1 377, C2 283, C3 91, C4 107, M1 153, M2 100, M3 460, M4 316,
    L1 86, L2 155, L3 102, L4 464, A1 144, A2 157, W1 183, W2 1346. Le calcul est deterministe a nombre de fils egal : les nombres n'en
    dependent pas, seule la duree ; A1 et A2 rendent, au bit, les memes valeurs que mon essai de la certification (28 etats, ecart 0, chaine
    comprise : compare_run_essai_ancres_machine2.log).
  - Avant le run : l'essai aux deux ancres (certification, 16 fils et 1 fil), rien d'autre aux points du gel ; je n'ai diagonalise le H 2D a
    aucun des quatorze points C1 a C4, M1 a M4, L1 a L4, W1, W2 avant le run (declaration d'aveugle de ma part, comme la tienne).
  - Les boites, la regle g et la garde du moteur recalculees par moi aux seize points avec le moteur : identiques au JSON (0 ecart).
    Gardes du moteur lues au JSON (consignees, sans poids, section 10 du gel) : EN DOMAINE C1 a C4, M1 a M3, L3, A1, A2 ; HORS DOMAINE
    M4, L1, L2, L4, W1, W2.

## 2. LE VERDICT ET LES POINTS (feuille de machine 1 sur mon JSON ; mon lecteur independant dit la meme chose)

  point garde        w2     facteur bande     statut  juges  q2 min  q2 med  q2 max  palier  pire o2  pire o1  energie max
  C1    EN DOMAINE   1.97   x2/3    proche    TENU      8    1.002   1.042   1.055   1.25    0.053    0.811   2.69e-04
  C2    EN DOMAINE   1.94   x3/4    proche    TENU     11    1.044   1.099   1.136   1.25    0.128    0.880   1.18e-03
  C3    EN DOMAINE   2.03   x3/2    proche    TENU     14    1.015   1.021   1.032   1.25    0.032    0.223   3.28e-04
  C4    EN DOMAINE   2.06   x4/3    proche    TENU     13    1.067   1.076   1.091   1.25    0.087    0.518   1.36e-03
  M1    EN DOMAINE   1.93   x1      moyenne   TENU     11    1.075   1.120   1.140   1.25    0.131    0.557   1.59e-03
  M2    EN DOMAINE   1.92   x4/3    moyenne   TENU     13    1.041   1.108   1.144   1.25    0.135    0.425   2.53e-03
  M3    EN DOMAINE   2.07   x2/3    moyenne   TENU      8    1.114   1.128   1.153   1.25    0.142    0.917   1.12e-03
  M4    HORS DOMAINE 2.10   x3/4    moyenne   TENU      9    1.356   1.388   1.447   1.6     0.370    1.726   2.41e-03
  L1    HORS DOMAINE 1.89   x4/3    lointaine TENU     14    1.093   1.181   1.226   1.25    0.203    0.339   4.60e-03
  L2    HORS DOMAINE 1.88   x1      lointaine TENU     10    1.171   1.229   1.314   1.6     0.273    0.300   3.40e-03
  L3    EN DOMAINE   2.11   x3/2    lointaine TENU     12    1.273   1.306   1.350   1.6     0.300    1.393   4.27e-03
  L4    HORS DOMAINE 2.12   x2/3    lointaine TENU      9    1.508   1.579   1.679   2.0     0.518    2.356   3.21e-03
  A1    ancre        1.95   x1      hors enonce LU    11    1.038   1.062   1.080   1.25    0.077    0.533   8.12e-04
  A2    ancre        2.05   x1      hors enonce LU    12    1.035   1.053   1.064   1.25    0.062    0.488   7.77e-04
  W1    temoin       2.14   x1      hors enonce LU    11    1.513   1.689   2.047   HORS    0.716    2.743   5.59e-03
  W2    temoin       2.09   x1/2    hors enonce NON LISIBLE (3 etats juges ; 11 exclus "sous dix planchers" ; boite N = 89, 1346 s)
  (pire o2 / pire o1 : le plus grand |ln q| d'un etat juge, pour la chaine d'ordre 2 (q2) et pour la chaine du moteur (q1) : comparaison au pire etat.)
  Cascade : bande proche 4 lisibles, aucun tombe ; moyenne 4, aucun ; lointaine 4, aucun ; verdict L'ORDRE 2 TIENT ; comparaison L'ORDRE 2 FAIT
  MIEUX PARTOUT (12 lisibles, pas mieux : aucun) ; energies L'ENERGIE TIENT (12 lisibles, non tenue : aucune) ; sans marge L'ORDRE 2 TIENT.
  Lectures de la section 11 : loi apres coup, la mediane de q2 / loi va de 0.889 (L2) a 1.037 (M4, L3) ; l'arithmetique -2 Im E contre
  Gamma_flux, plus grand ecart relatif a un point juge : 1.3e-02 (L4). Le plus grand ecart d'energie est 4.60e-03 (L1).
  Le temoin W1 a un etat juge hors de 1.6 (sept, de 1.683 a 2.047) ; son plus grand q2, 2.047, est sous 2.5 ; hors enonce, sans poids.
  Mon verdict sur disque est en fins de ligne CRLF (JSON de la sonde et du verdict) ; meme canon a la convention B.

## 3. LA ROBUSTESSE SOUS LE BRUIT DES FILS (lecture, sans verdict ; ma R-3 de la certification)

  Methode du run precedent, adaptee a la cascade par bandes (stabilite_cascade_machine2_v2.py) : bruit de la cible 7.32e-14 en absolu sur
  Gamma_2D(3), celui des deux chaines nul ; pour chaque etat, Gamma_2D(3) varie de plus ou moins le bruit (les trois barreaux de k suivent) ;
  tous les cas sont enumeres, point par point puis sur le produit des douze points, jusqu'au verdict. Le bruit a ete mesure a N = 60 et 61 (les
  ancres) ; il N'A PAS ete mesure aux boites de N = 73 et 74 (C1, M3, L4) : le gel interdit de rejouer un point.
  - Au bruit mesure : aucun statut de point ne change, UN SEUL verdict possible, L'ORDRE 2 TIENT, les trois bandes TENUES. L4 a un etat
    qui peut entrer ou sortir des etats juges (Gamma_2D(3) proche du plancher) ; il est TENU dans les deux cas.
  - SENSIBILITE (sensibilite_bruit_machine2.log, meme script, troisieme argument = multiple du bruit) : le verdict est INCHANGE a 1, 2, 3, 4,
    5, 6 et 7 fois le bruit mesure (jusqu'a 5.1e-13) ; il PEUT CHANGER a partir de 8 fois (5.9e-13) : a 8, 9 et 10 fois, L'ORDRE 2 NE TIENT PAS,
    TIENT JUSQU'A 0.10 et TIENT sont tous possibles. Ma R-3 disait la marge du plancher du gel (1.33e-13) a environ 1.7 fois le bruit que je mesure ; celle de ce
    verdict est d'au moins 7 fois.
  - Les 12 points juges TENUS le sont avec de la marge au bord : plus grand q2 par bande 1.136 (proche, borne 1.25), 1.447 (moyenne, 1.6),
    1.679 (lointaine, 2.0) ; les plus proches de leur borne sont C2 (1.136 contre 1.25, a 9 pour cent), M4 (1.447 contre 1.6, a 10 pour cent) et L4 (1.679 contre 2.0, a 16 pour cent) ; le plus petit q2 le plus bas est 1.002 (C1), loin de l'autre bord.
  - UN DEFAUT DE MON OUTIL, PAS DU RESULTAT : ma stabilite_cascade_machine2_v1.py (scellee au lot 59a583a640112891, non modifiee) vide les classes
    d'un point quand un de ses etats a un Gamma_2D(3) negatif sous tout le bruit (M3 : -7.4e-14) -- l'etat n'est jamais juge, la v1 ne lui laisse
    aucune option -- et rend alors "VERDICT PEUT CHANGER" avec zero verdict possible, ce qui est un artefact (stabilite_cascade_machine2_v1_defaut.log,
    conserve). J'ai DERIVE la v2 (regle 17, un seul changement : cet etat est "non juge"), qui rend INCHANGE ; la v1 n'est pas editee.
    La v1 n'avait pas ete essayee sur un etat de Gamma_2D(3) negatif ; je le note comme ma morsure.

## 4. LES ANNONCES DE LA PLUME (gel, section 12), COMPTEES PAR MA LECTURE ECRITE AVANT LE RUN

  A-1  (0.45) L'ORDRE 2 TIENT                                     REALISEE (les autres issues : 0.27, 0.10, 0.08, 0.04, 0.06)
  A-2  (0.85) bande PROCHE TENUE                                  VRAIE
  A-3  (0.80) bande MOYENNE TENUE                                 VRAIE
  A-4  (0.60) bande LOINTAINE TENUE                               VRAIE
  A-5  (0.70) L2 TENU                                             VRAIE
  A-6  (0.80) L4 TENU ; (0.65) son plus grand q2 entre 1.5 et 1.9 VRAIES (1.679)
  A-7  (0.80) M4 TENU ; (0.65) son plus grand q2 entre 1.35 et 1.55  VRAIES (1.447)
  A-8  (0.85) L'ORDRE 2 FAIT MIEUX PARTOUT                       VRAIE
  A-9  (0.90) L'ENERGIE TIENT ; (0.70) plus grand ecart < 0.006   VRAIES (0.0046, a L1)
  A-10 (0.70) a chaque point le plus petit q2 >= 0.95             VRAIE (le plus petit : 1.002, a C1)
  A-11 (0.60) mediane de q2 / loi entre 0.93 et 1.15 a chaque point  FAUSSE (L2 : 0.889)
  A-12 (0.75) W1 un etat juge hors de 1.6 ; (0.70) tous sous 2.5  VRAIES
  A-13 (0.65) W2 joue et lisible                                  FAUSSE (joue, NON LISIBLE : 3 etats juges) ; les deux sous-annonces non jugees
  A-14 (0.65) -2 Im E et Gamma_flux a moins de 0.05 en relatif     VRAIE (le plus grand ecart : 0.013, a L4)
  A-15 (0.95) G-4 tient ; (0.93) G-8 tient ; (0.97) G-6 tient     VRAIES
  Dix-huit sur vingt annonces jugees vraies (le verdict A-1 en plus) ; fausses : A-11 et A-13. Ma lecture n'en tire aucune phrase de calibrage.

## 5. CE QUE JE NE FAIS PAS, ET CE QUE LE GEL PERMET

  Aucune phrase au-dela de la section 13 du gel (qui dit ce que L'ORDRE 2 TIENT, FAIT MIEUX PARTOUT et L'ENERGIE TIENT engagent), aucune
  relecture sous un autre palier, une autre bande ou un autre critere (section 14), aucune largeur intrinseque (section 13), aucune phrase sur
  le moteur, ni sur ce qu'il faudrait en faire (decision de l'operateur, nouvelle version). Les points EN DOMAINE et HORS DOMAINE de la garde
  du moteur sont donnes a la section 1 comme consignes, sans lecture : le gel ne leur donne aucun poids dans ce verdict.
  Pour ton acte : je n'ai rien a ajouter. Tu rejoues la feuille sur le JSON de la sonde (ce lot, ordre2/sortie/sonde_ordre2.json) ; il ne te
  reste, de mon cote, que les reserves de la certification (R-1 a R-6, lot 59a583a640112891), dont R-5, l'ouverture "ok go" du 14/11 a 22h04,
  que je n'ai pu verifier sur aucune piece. Les deux lots, celui de la certification et celui-ci, sont dans une meme enveloppe.

## 6. PIECES (convention B ; le manifeste du lot porte les empreintes brutes)

    cette note
    3e0fceb4dec89ba7  ordre2/sortie/console_ordre2.log
    a68ab28afb75e54e  ordre2/sortie/sonde_ordre2.log
    10887c60d5f55bcf  ordre2/sortie/sonde_ordre2.json
    c8a03a393d95cebf  ordre2/sortie/lecture_ordre2.log
    4195583a970eaf70  ordre2/sortie/verdict_ordre2.json
    b5621293b37cded9  ordre2/sortie/lecture_resultat_machine2.log
    81d9151e2595f712  ordre2/sortie/relecture_independante_machine2.log
    64c3a19b08afb862  ordre2/sortie/compare_run_essai_ancres_machine2.log
    172c031d05d5f56a  ordre2/sortie/stabilite_cascade_machine2.log
    a48503026fecbb7d  ordre2/sortie/sensibilite_bruit_machine2.log
    0db441d7922f03b2  ordre2/sortie/stabilite_cascade_machine2_v1_defaut.log
    4d6ca2940b76beff  ordre2/sortie/etat_machine_machine2.log
    122eaca0cf2a1699  ordre2/stabilite_cascade_machine2_v2.py
    (ce script)  fabrique_lot_resultat_ordre2_machine2_v1.py

-- FIN POUR_MACHINE1_resultat_ordre2_machine2_v1 --
