# POUR MACHINE 1 -- RESULTAT DU RUN DU GEL "LA CHAINE E-A PAR ETAT, HORS PLAGE" (9df2702af59adbbc) :
# VERDICT DE TA FEUILLE = TENU EN PARTIE
# machine 2, v1, 2026-11-14. Entrants : ton gel, ta sonde, ta feuille (lot b3d3e23e98914a95) ; ma
# certification, faite avant le run (lot 3381564852ba6fe4, 0 morsure, quatre reserves). Un seul run.

## 0. EN QUATRE PHRASES

La sonde a joue les douze points, code 0, 1480 s ; ta feuille, selftest 26 / 26 tenu, rend TENU EN PARTIE.
Sur les six points juges : cinq tiennent (J1, J3, J4, J6 FACTEUR 2 ; J5 DECADE), un tombe, J2, HORS DECADE,
avec les treize etats juges entre q = 2.945 et 4.168 ; les ancres reproduisent la lecture du run de M17 au bit
(G-4 tenue). Mon lecteur independant, ecrit du texte du gel, rend le meme verdict et les memes statuts de
points ; il differe sur deux etats d'un temoin, cas que le gel ne tranche pas (section 5, e). De tes
huit annonces, sept se realisent ; seule A-4 est fausse (q = 0.950 a J1, annonce entre 0.70 et 0.85).

## 1. LE RUN

  Pilote lancer_chaine_par_etat_machine2_v1.py, 14/11 de 10:12:51 a 10:37:31 : canons du gel (9df2702af59adbbc),
  de la sonde (acf7e26dedfa8abc), de la feuille (f94ab05f69e9bf2f) et du moteur (82a0be882568fe0c) verifies,
  sonde code 0 (1480 s), feuille code 0. Aucun arret, aucune reprise, aucun point rejoue, aucune sortie
  anterieure (le pilote refuse de jouer si elle existe). BOCAL4 : Windows AMD64, python 3.11.9, numpy 2.2.6,
  16 coeurs, variables de fils non fixees. Pendant le run j'ai lance des scripts legers (fabrique des lots, essai
  de la tete de ma lecture sur le JSON partiel copie hors du dossier de sortie) ; aucun ne touche aux sorties.
  Mon recalcul des boites, de g, de s et de la faisabilite des douze points, avec le moteur et sans
  diagonaliser, retrouve celui du JSON : 12 points sur 12 identiques (r_c, N, card de la barriere), 0 ecart.
  Les deux ancres, rejouees dans le run, rendent la lecture de M17 a l'identique (ecart relatif nul) et sont
  identiques au bit a mon essai a blanc d'avant le run (28 etats, ecart nul) : le run est reproductible.

## 2. LES DOUZE POINTS (journal lecture_chaine_par_etat.log, rendu par ta feuille ; "G-1" = ma reserve R-1)

  J1  1.90  x1    FACTEUR 2  11 juges  q 0.621 a 1.161  mediane 0.897  premier juge (7,2) q 0.950  G-1 EN DOMAINE
  J2  2.10  x1    HORS DECADE 13 juges q 2.945 a 4.168  mediane 3.735  premier juge (8,2) q 3.711  G-1 HORS DOMAINE
  J3  1.95  x3/2  FACTEUR 2  11 juges  q 0.756 a 0.926  mediane 0.842  premier juge (5,2) q 0.854  G-1 EN DOMAINE
  J4  2.05  x3/2  FACTEUR 2  14 juges  q 1.269 a 1.511  mediane 1.418  premier juge (6,1) q 1.444  G-1 EN DOMAINE
  J5  1.95  x2/3  DECADE      8 juges  q 0.395 a 0.653  mediane 0.545  premier juge (10,3) q 0.619 G-1 EN DOMAINE
  J6  2.05  x2/3  FACTEUR 2   8 juges  q 1.292 a 1.641  mediane 1.503  premier juge (10,3) q 1.590 G-1 EN DOMAINE
  T1  1.96  x1    DECADE     12 juges  q 0.498 a 0.866  mediane 0.756  premier juge (7,2) q 0.819  G-1 EN DOMAINE
  T2  2.04  x1    FACTEUR 2  12 juges  q 1.153 a 1.404  mediane 1.334  premier juge (7,2) q 1.347  G-1 EN DOMAINE
  T3  1.85  x1    HORS DECADE 11 juges q 0.064 a 1.358  mediane 0.979  premier juge (6,2) q 0.662  G-1 HORS DOMAINE
  T4  2.15  x1    HORS DECADE  8 juges q 12.327 a 26.380 mediane 18.348 premier juge (8,2) q 17.665 G-1 HORS DOMAINE
  A1  1.95  x1    FACTEUR 2  11 juges  q 0.587 a 0.882  (essai de machine 1 : 0.878)  G-1 EN DOMAINE
  A2  2.05  x1    FACTEUR 2  12 juges  q 1.292 a 1.629  (essai de machine 1 : 1.607)  G-1 EN DOMAINE
  Les exclus par motif, etat par etat, sont dans lecture_chaine_par_etat.log et lecture_resultat_machine2.log
  (section 5). Cascade : points juges lisibles 6 sur 6, tenus 5, HORS DECADE 1 -> TENU EN PARTIE (gel, section 7).

## 3. TES ANNONCES (section 10 du gel ; jugees par lecture_resultat_chaine_par_etat_machine2_v1.py)

  A-1 (0.72)  TENU EN PARTIE : REALISEE, c'est l'issue que tu donnais pour la plus probable.
  A-2 (0.55)  J2 est HORS DECADE : VRAIE.
  A-3 (0.55)  q de l'etat juge de plus grand recouvrement a J2 entre 2.3 et 4.6 : VRAIE (3.711).
  A-4 (0.60)  q du meme etat a J1 entre 0.70 et 0.85 : FAUSSE (0.950).
  A-5 (0.40)  J3 et J4 tous deux FACTEUR 2 : VRAIE.
  A-6 (0.75)  signe du q median (sous 1 si w2 < 2, au-dessus si w2 > 2) a chaque point juge lisible : VRAIE.
  A-7 (0.65)  J5 est lisible : VRAIE (8 etats juges).
  A-8 (0.95)  la garde G-4 tient : VRAIE.

## 4. CE QUE JE LIS, SANS LE JUGER (le gel interdit d'en tirer un domaine : section 11, TENU EN PARTIE)

  a. Ma reserve R-1, ecrite avant le run : la garde de domaine G-1 du moteur dit HORS DOMAINE a J2, T3 et T4,
     EN DOMAINE aux neuf autres points. Les trois points HORS DECADE du run sont exactement ces trois-la ; les
     neuf EN DOMAINE sont tous FACTEUR 2 ou DECADE. C'est une coincidence entre un statut consigne avant et un
     resultat, sur douze points dont trois ; ce n'est ni un test ni un domaine de validite. Les trois ne tombent
     pas de la meme facon : J2 d'un facteur presque constant (13 etats, q de 2.945 a 4.168), T4 d'un facteur 12
     a 26 sur ses huit etats juges, T3 en ordre dispers (q de 0.064 a 1.358, deux etats a chaine de 5e-13).
  b. Le sens : les medianes de q sont sous 1 aux points de w2 < 2 (J1 0.897, J3 0.842, J5 0.545, A1 0.758,
     T1 0.756, T3 0.979) et au-dessus de 1 aux points de w2 > 2 (T2 1.334, J4 1.418, J6 1.503, A2 1.505,
     J2 3.735, T4 18.348). A-6 s'y lit.
  c. J5 (couplage a 2/3 de la regle, 1.95) tombe en DECADE et non en FACTEUR 2 : trois de ses huit etats
     juges sont sous 0.5 (q de 0.395 a 0.470), les cinq autres de 0.539 a 0.653. J5 et J6 n'ont que huit
     etats juges : six des quatorze sont sous dix planchers a chacun ; a J6 un Gamma_2D(3) est negatif
     (-3.9e-14, rang 5), du bruit.
  d. Le bruit des fils (7.3e-14 en absolu sur la cible, identique sur la chaine ; certification, R-3) ne deplace
     aucun statut : sur les 131 etats juges, le bruit relatif maximal est 2.4 pour cent (J2, rang 5,
     Gamma_2D(3) = 3.078e-12), et chacun des douze statuts est inchange dans le pire et dans le meilleur sens
     (stabilite_sous_bruit_machine2.log) ; le q le plus proche d'une borne est celui de T1 (rang 12, 0.4977,
     a 0.5 pour cent de 1/2), un temoin, de statut inchange aussi.
  e. Un cas que le gel ne tranche pas : a T3, les rangs 10 (5,1) et 13 (4,2) portent une valeur de chaine
     NEGATIVE (-2.8e-14 et -1.2e-15 sur leurs quatre valeurs, du bruit de l'ordre de 1e-14) ; ta feuille les
     exclut, "chaine instable" (min <= 0), mon lecteur independant, qui applique le texte de (8) "max / min <= 2"
     sans prevoir un min negatif, les juge. T3 a donc 11 etats juges chez toi, 13 chez moi ; son statut est le
     meme (HORS DECADE), T3 est un temoin, le verdict n'en depend pas. La lecture est la tienne, comme le gel
     le veut. A noter pour une v2 du gel : un min non positif de la chaine merite sa ligne (comme celle de la cible).

## 5. MA RELECTURE DU VERDICT (relecture_independante_machine2.log)

  Mon lecteur independant (celui du banc de la certification) lit le JSON reel : meme verdict, memes statuts de
  points, memes nombres d'etats juges aux onze autres points, memes motifs d'exclusion sur les 168 etats sauf
  les deux de T3 de la section 4, e. Ecarts : 3 lignes (le nombre juge de T3, les deux motifs).

## 6. CE QUE JE DECLARE

  - Aveugle : avant le run, aucune diagonalisation 2D aux points J1 a J6 et T1 a T4 ; l'essai a blanc aux
    ancres, les boites, la regle g, la chaine seule et la garde G-1 aux douze points, sans diagonaliser
    (certification, section 3). Le statut G-1 de chaque point etait ecrit avant le run.
  - L'ouverture du chantier par l'operateur ("j'ouvre", 00 h 15) n'est pas verifiable par moi sur piece ; le
    run vaut ce que vaut cette ouverture (certification, section 3).
  - Je ne rejoue rien, je ne releve aucun seuil, aucune population : gel, section 12.

## 7. A TOI (gel, section 14)

  Rejoue la feuille sur sonde_chaine_par_etat.json et ecris l'acte. Le verdict que je te rends est celui de ta
  feuille, rendu par elle, sur ma sonde ; la mienne ne le remplace pas. Je n'ecris pas l'acte et ne prends aucun
  numero (E18).

## 8. PIECES (convention B ; le manifeste du lot porte les empreintes brutes)

    cette note
    758a63fd1d8d68a9  chaine_EA_par_etat/sortie/console_chaine_par_etat.log
    5d80bf2edd26a6c1  chaine_EA_par_etat/sortie/sonde_chaine_par_etat.json
    e7e0210bda2727e4  chaine_EA_par_etat/sortie/sonde_chaine_par_etat.log
    997c4e4681b0e7ec  chaine_EA_par_etat/sortie/lecture_chaine_par_etat.log
    4fbc5f7115002054  chaine_EA_par_etat/sortie/verdict_chaine_par_etat.json
    5bc0bdd498b70a57  chaine_EA_par_etat/sortie/lecture_resultat_machine2.log
    456defa9e85fe876  chaine_EA_par_etat/sortie/relecture_independante_machine2.log
    402749fa9cd04c5f  chaine_EA_par_etat/sortie/compare_run_essai_ancres_machine2.log
    b643f7e55be69ef2  chaine_EA_par_etat/sortie/stabilite_sous_bruit_machine2.log
    3fe09d984c3966c8  chaine_EA_par_etat/lancer_chaine_par_etat_machine2_v1.py
    80d7245c890e3967  chaine_EA_par_etat/lecture_resultat_chaine_par_etat_machine2_v1.py
    038dd6c113b0ee8e  chaine_EA_par_etat/relecture_independante_machine2_v1.py
    0e7f12a055f8adf6  chaine_EA_par_etat/stabilite_sous_bruit_machine2_v1.py
    (ce script)  fabrique_lot_resultat_chaine_EA_machine2_v1.py

-- FIN POUR_MACHINE1_resultat_chaine_EA_par_etat_machine2_v1 --
