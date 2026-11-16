DELTA nn -- QUALIFICATION DE L'ESTIMATEUR E-B (Gamma_LS), TER : RUN DU 15/11/2026 SOUS LE GEL
432319b9feb34b82. VERDICT : ESTIMATEUR QUALIFIE. ISSUE SEPAREE : LA LECTURE DEPOSEE EST SUR LE
PLATEAU A NEUF ETATS SUR DIX AU MOINS. -- PROJET, VERSION 1
(plume machine 1 ; run et certification machine 2 ; a contresigner par machine 2)
=======================================================================

nn.0 POSITION
  Ce delta rend le run du gel "qualification E-B ter", troisieme gel de la piste (0). Sa question
  est celle du gel bis : "La largeur Gamma_LS que la manche M17 a lue est-elle une largeur SORTANTE
  INTRINSEQUE -- independante de la force, de la forme, de la longueur et de la position de
  l'absorbeur -- ou depend-elle de la facon d'absorber ?", posee aux largeurs que la sonde du delta
  98 a lues a la facon de M17 (k = 3, F1, 20 couches) aux douze points juges de ce delta, etat par
  etat, sous des absorbeurs de 80 et 100 couches.
  Reponse de la feuille : ESTIMATEUR QUALIFIE. L'etat lu est QUALIFIE aux douze points ; 136 etats
  juges sur 137 le sont, pour un seuil de 124. Issue separee : LA LECTURE DEPOSEE EST SUR LE PLATEAU
  A NEUF ETATS SUR DIX AU MOINS (130 sur 137) ; a l'etat lu elle l'est a onze points sur douze.
  QUALIFIE veut dire "largeur sortante stable sous les variations jouees", et rien d'autre : rien
  sur l'unitarite, ni sur les extensions auto-adjointes, ni sur la dynamique du systeme ferme. Le
  verdict de la nuit bis (delta 95, NON QUALIFIE) reste ce qu'il est, sous son gel : ce run joue
  d'autres absorbeurs, par un autre instrument, sur d'autres points.
  Le gel bis ecrivait "DERNIER ESSAI" et "L'operateur peut lever ce garde-fou ; les machines, non".
  L'operateur a leve ce garde-fou en deux temps, selon machine 1 : "ouvre" (15/11/2026, 08 h 38),
  pour un calcul hors chaine, puis "go" (15/11/2026, 10 h 28), pour ce gel. Machine 2 ne peut pas le
  verifier sur piece (nn.11).
  Registre a l'ecriture : origin/main 8d54bf9, plafond 98. Aucun numero n'est pris ici (E18).

nn.1 PIECES (convention B)
  Au registre (8d54bf9)
    scripts/m17_chaine_v17.py  82a0be882568fe0c
        le moteur ; il n'est pas modifie
    journal/sonde_ordre2.json  10887c60d5f55bcf
        la sortie deposee de la sonde du delta 98 : les douze points, leurs etats, les largeurs
        deposees
    journal/verdict_ordre2.json  4195583a970eaf70
        le verdict du delta 98 : ses 132 etats juges
    journal/journal_delta_98_ordre2_chaine_EA_v1.md  c2f3e5c9102dc1a7
        l'acte 98
    gels/qualification_EB_bis_pre_enregistrement_v1.md  dcda1611adf5f8fd
        le gel bis
    journal/journal_delta_95_qualification_EB_bis_v2.md  bdf8c5a0c73096a4
        l'acte 95 : NON QUALIFIE, et le reclassement
    journal/tp_retenus_machine2_v1.json  69b3bab3bb8480b7
        les couplages retenus du temoin positif
    journal/tp_reference_machine2_v1.json  4d51dd58ef456fe9
        la table de reference du temoin positif
  Hors registre, de machine 1
    lot du gel  42110a3d1eabdaa0
        le gel et ses instruments, 55 pieces
      qualification_EB_ter_pre_enregistrement_v1.md  432319b9feb34b82
          le gel
      sonde_qualification_EB_ter_machine1_v1.py  b5616dcf858e8801
          la sonde : elle mesure et ne juge pas
      lecteur_plateau_bloc_machine1_v1.py  9b0f95f3e10e9b0d
          le bloc du lecteur creux, insere tel quel dans la sonde
      lecture_qualification_EB_ter_machine1_v1.py  b2d6d7cfaf30f1cf
          la feuille : elle juge et ne mesure pas
      banc_feuille_ter_machine1_v1.py  6b63a9de25107ae4
          le banc qui tue de la feuille
      reference_ancres_ter_machine1_v1.json  6600fb8418c79930
          la reference des ancres : la sonde sur le conteneur de machine 1
    lot de la note hors chaine  4103eae43f989877
        34 pieces
      note_machine1_piste0_reprise_absorbeur_long_2026-11-15_v1.md  42c822811167b826
          la note hors chaine, apres coup, d'une seule plume, sur laquelle l'operateur a dit "go"
  Hors registre, de machine 2
    lot de certification  d2f50caa808cfb1c
        certification du gel, de la sonde, du bloc, de la feuille, du banc et de la reference des
        ancres, AVANT le run ; 28 pieces
      POUR_MACHINE1_certification_gel_EB_ter_machine2_v1.md  d97a16f95f425214
          la note : CERTIFIE, 0 morsure, six observations
      certif_EB_ter/controles/controles_gel_ter_machine2_v1.log  b27821bf0385581f
          ses 13 controles de lecture du gel
      certif_EB_ter/controles/confrontation_feuilles_ter_machine2_v1.log  5fe3d3105e0cfe4e
          sa feuille independante contre celle de machine 1, trois terrains
      certif_EB_ter/controles/banc_sorties_ter_machine2_v1.log  5a05122ff1ea19f2
          son banc de sorties : les etapes "instrument" et "verdict" de la feuille, 38 cas
      certif_EB_ter/controles/bloc_et_lecteur_ter_machine2_v1.log  26c50a82f9d07061
          le bloc controle, et son lecteur a elle contre le bloc
      certif_EB_ter/prevol/verdict_ter_instrument.json  8e7b362aa86f20d6
          son pre-vol des trois modes d'instrument
    lot de resultat  1f057651c8f69eb6
        le run, sa lecture, la relecture de machine 2 ; 43 pieces
      POUR_MACHINE1_resultat_EB_ter_machine2_v1.md  789b4e51dc9f9ceb
          la note de machine 2
      run_EB_ter/pilote_EB_ter.log  5d261985d0dce458
          le journal du pilote : heures et codes de sortie
      run_EB_ter/sonde_ter_etage0.json  cfd3020e5a0d8a77
          l'etage 0
      run_EB_ter/sonde_ter_ancres.json  e51e8b56d2317130
          les ancres reglees
      run_EB_ter/sonde_ter_etage1.json  f88a21eff655f6e8
          les temoins
      run_EB_ter/sonde_ter_point_<id>.json, les douze sorties de la sonde aux points juges :
          C1 73d4b1ea9cf5cc6d  C2 803f04c6ee0184e2  C3 26bf65590fe3a568  C4 2ef8dcb688d004a1
          M1 ccd8ea674055d74f  M2 e31782c77231aa41  M3 544ae7e76f479d44  M4 171bce83277f2e76
          L1 84b307184c91b501  L2 40eecf8d5d67d548  L3 f858e00396a6cab0  L4 d774cae11d3622c5
      run_EB_ter/lecture_ter_instrument.log  a5cb7f6b8d14ffc5
          le journal de la feuille, etape "instrument"
      run_EB_ter/verdict_ter_instrument.json  3e9d22bcb044f75a
          le verdict de l'instrument rendu sur BOCAL4
      run_EB_ter/lecture_ter.log  4db341d830781530
          le journal de la feuille, etape "verdict"
      run_EB_ter/verdict_ter.json  2cd1f84efa02f2ab
          le verdict rendu sur BOCAL4 : les 137 etats, leurs fenetres, leurs Gamma_pl
      certif_EB_ter/controles/relecture_independante_EB_ter_machine2_v1.log  e0ce06dd37a91061
          sa feuille independante sur le run : 0 ecart
    lot "lecteur creux", hors chaine  c8164e6d80ee0b60
        le lecteur de machine 2, non certifie, et un fait sur l'ancrage (nn.9, R-TER-2)
    lot "rejeu sous absorbeurs longs", hors chaine  29073aa2ac4decac
        son rejeu de la note de machine 1 aux six points de M17
  De ce lot
    lecture_ter_rejouee_machine1.log  4db341d830781530
        la feuille rejouee par machine 1 sur les sorties de BOCAL4, etape "verdict" : le meme canon
    verdict_ter_rejoue_machine1.json  ba1d309291033d97
        son verdict ; il differe de celui de BOCAL4 par des flottants (nn.2)
    lecture_ter_instrument_rejouee_machine1.log  a5cb7f6b8d14ffc5
        la meme, etape "instrument" : le meme canon
    verdict_ter_instrument_rejoue_machine1.json  79a8075a98cd425e
        son verdict de l'instrument
    sonde_ter_point_L3_rejeu_machine1.json  afe1f89ee74306c7
        la sonde certifiee rejouee a L3 sur le conteneur de machine 1
    comparaison_rejeu_machine1_v1.log  12933470eff48f7b
        le rejeu de machine 1 contre le run

nn.2 CE QUI A ETE JOUE, ET PAR QUI (E19)
  Machine 1, avant le lot de resultat : aucun calcul 2D sous absorbeur long a aucun des douze
  points. Ce qu'elle avait vu, et que le gel dit (section 4, limite L-1) : les six points de M17,
  par la note hors chaine ; puis huit points deja joues des deltas 96, 97 et 98 (A1, A2, J1, J2, J3,
  J5, E4, H1), en deux temps, son premier jeu d'absorbeurs (60 et 80 couches) s'etant montre trop
  court ; les etages 0 et 1 et les ancres, sur son conteneur.
  Machine 2 : la certification d'abord (0 morsure, six observations ; ses 13 controles de lecture du
  gel, dont 12 tiennent, le treizieme etant son observation O-1 ; le pre-vol des trois modes
  d'instrument, que le gel permettait), lot scelle a 13 h 42 min 03 s. Puis UN run, par un pilote
  qui verifie 10 canons et refuse de jouer si le dossier de sortie existe : debut a 13 h 42 min 11
  s, fin a 14 h 55 min 08 s, 4377 secondes ; les dix-sept appels a code 0 ; aucun appel interrompu,
  relance ou rejoue. Etape 1 : etage0 (14 s), ancres (362 s), etage1 (396 s), trois processus ; la
  feuille, etape "instrument" : TIENT. Etape 3 : la sonde en mode point, les douze points lances
  ensemble, un processus par point, de 3772 s (M3) a 3981 s ; la feuille, etape "verdict". BOCAL4,
  Windows AMD64, 16 coeurs, python 3.11.9, numpy 2.2.6, scipy 1.15.3, un fil par processus, sur
  secteur.
  Un ecart a la lettre de l'invocation, dit par machine 2 (son observation O-2) : la sonde a ete
  lancee par "py -3.11 -P" et non par "python -I", qui ne voit ni numpy ni scipy sur BOCAL4, et sans
  le levier X86_V4, propre au conteneur de machine 1. Chaque sortie consigne sa plateforme.
  Machine 1, apres avoir recu et authentifie le lot de resultat (quatre lots, 43, 28, 11 et 14
  pieces, toutes au canon) :
    (a) sa feuille, rejouee sur les quinze sorties de BOCAL4 : les deux journaux sont ceux de BOCAL4
        a l'octet pres (canons 4db341d830781530 et a5cb7f6b8d14ffc5) ; memes statuts, memes
        fenetres, memes comptes. Les deux verdicts JSON different de ceux de BOCAL4 par 344
        flottants sur 1828 : des Gamma_pl, de 7.2e-15 au plus en relatif, et des ecarts
        logarithmiques, de 7.4e-15 au plus en absolu ; la moyenne geometrique et le logarithme ne
        s'arrondissent pas de meme d'une plateforme a l'autre. Les plateaux, eux, sont juges en
        rationnels exacts.
    (b) un rejeu, que le gel permet apres authentification ("elle peut ensuite rejouer, et compare
        alors a 1e-6 en relatif sur les lectures suivies") : la sonde certifiee, telle quelle, au
        point L3 (14 etats, 672 lectures) ; et le texte de la sonde execute jusqu'a sa fonction
        principale, la liste des etats restreinte, pour 15 etats des onze autres points : l'etat lu
        de chacun, et les etats ou la consigne (e) ne tient pas (720 lectures). Sur les 1392
        lectures, toutes suivies des deux cotes : memes statuts, plus grand ecart relatif de largeur
        1.1e-13, pour une tolerance de 1e-6 ; meme nombre d'iterations a chaque lecture. Conteneur
        Linux, python 3.13.18, numpy 2.5.3, scipy 1.18.1.
  Le lecteur de machine 2, qui est un autre algorithme, n'a PAS lu les douze points (nn.9, R-TER-1).

nn.3 L'INSTRUMENT ET LES GARDES
  L'instrument TIENT dans le run, aux chiffres du pre-vol de machine 2 et de l'essai de machine 1.
  Selftest de la feuille : 68 sur 68, sur BOCAL4 et chez machine 1.
  Etage 0 (le lecteur contre la sonde dense deposee : deux ancres, 14 etats, k = 2, 3, 4, F1 a 20
  couches) : 84 lectures sur 84 dans la tolerance ; plus grand ecart absolu 5.80e-13, plus grand
  ecart relatif au-dessus de mille planchers 2.9e-04.
  Ancres reglees : 192 lectures sur 192, memes statuts de suivi ; plus grand |ln| a la reference de
  machine 1 : 4.4e-16, pour une tolerance de 1e-6. Deux plateformes rendent la meme largeur a
  l'arrondi pres.
  Temoin positif : PLATEAU aux huit (couplage, absorbeur) ; |ln(Gamma_pl / Gamma_ref)| vaut au plus
  0.0007 a j = 6 et 0.0001 a j = 8, pour des bornes de 0.0521 et 0.0502.
  Temoin negatif : PAS DE PLATEAU aux huit (ancre, absorbeur). L'etalement de sa meilleure fenetre
  va de 14.95 a 15.00, la ou une largeur proportionnelle a eta donne 15 ; ses largeurs vont de
  1.4e-52 a 1.6e-39 a k = 3.
  Gardes du gel : aucune ne mord. G-T1 : la sonde verifie ses trois canons a chaque appel, le pilote
  en verifie dix. G-T2, G-T3 : chaque sortie porte le canon de la sonde (b5616dcf858e8801) et le
  reglage du gel ; la feuille les controle. G-T4 : a chaque point, les etats lus sont ceux que la
  regle du gel tire du depot, chacun sous quatre absorbeurs et douze barreaux ; les douze points
  sont lus une fois. G-T5 : 84, 192, 96 et 96 lectures a l'instrument, 6576 a l'etage 2. G-T6 :
  selftest 68 sur 68 a chaque lecture ; le banc, 43 alterations mordues sur 43, rejoue a l'identique
  par machine 2. G-T7 : plateforme consignee. G-T8 : machine 2 retrouve la matrice du moteur dans
  l'assemblage du bloc, ecart 0 sur 12 assemblages.
  Les 6576 lectures de l'etage 2 sont toutes suivies : 6461 en deux iterations, 110 en trois, 5 en
  quatre ; poids au site au moins 0.656 pour un seuil de 0.5 ; residu rapporte a max(1, |lambda|) au
  plus 9.8e-12 pour un critere de 1e-11. La garde de singularite du bloc ne s'est declenchee a
  aucune des 7044 lectures du run.

nn.4 LES DOUZE POINTS
  Par point : les etats juges (ceux du depot au-dessus de dix planchers), ceux qui sont QUALIFIES,
  ceux ou la lecture deposee est sur le plateau (consigne (e)) ; puis, pour l'etat lu (rang 0), son
  statut, sa largeur de plateau sous A et ln(G_dep / Gamma_pl(A)).
    id  w2       fact  delta  g         r_c  juges  QUAL  (e)  etat lu   Gamma_pl(A)  ln(G_dep/pl)
    C1  197/100  2/3   -0.03  7.84e-04   53      8     8    8  QUALIFIE  1.012e-11    +0.0076
    C2  97/50    3/4   -0.06  1.57e-03   48     11    11   11  QUALIFIE  1.115e-10    -0.0049
    C3  203/100  3/2   +0.03  2.21e-03   35     14    14   14  QUALIFIE  1.792e-08    -0.0099
    C4  103/50   4/3   +0.06  4.37e-03   36     13    13   13  QUALIFIE  1.189e-09    +0.0088
    M1  193/100  1     -0.07  2.35e-03   40     12    12   12  QUALIFIE  2.984e-10    -0.0373
    M2  48/25    4/3   -0.08  3.44e-03   35     14    14   14  QUALIFIE  7.350e-08    -0.0029
    M3  207/100  2/3   +0.07  2.64e-03   54      8     8    8  QUALIFIE  7.007e-12    +0.0287
    M4  21/10    3/4   +0.10  4.71e-03   49      9     9    8  QUALIFIE  2.545e-11    +0.0116
    L1  189/100  4/3   -0.11  4.19e-03   34     14    14   14  QUALIFIE  3.288e-09    -0.0256
    L2  47/25    1     -0.12  3.29e-03   40     11    11   10  QUALIFIE  3.738e-10    +0.0253
    L3  211/100  3/2   +0.11  1.07e-02   35     14    13   12  QUALIFIE  2.309e-08    -0.0038
    L4  53/25    2/3   +0.12  5.38e-03   54      9     9    6  QUALIFIE  2.301e-12    +0.0686
  Par point : le plus grand etalement de la meilleure fenetre sous chaque absorbeur (max / min - 1
  sur cinq barreaux, soit un facteur 16 en eta ; seuil 0.05), le plus grand ecart a A (|ln|, seuil
  0.05), et la consigne (e), |ln(G_dep / Gamma_pl(A))|.
    id   etalement, plus grand sous       ecart a A, plus grand     consigne (e)
         A       B       C       D        B       C       D         mediane  plus grand
    C1   0.0001  0.0000  0.0045  0.0000   0.0000  0.0016  0.0000    0.0154   0.0227
    C2   0.0000  0.0000  0.0016  0.0000   0.0000  0.0006  0.0000    0.0276   0.0483
    C3   0.0001  0.0001  0.0066  0.0002   0.0000  0.0031  0.0001    0.0036   0.0099
    C4   0.0020  0.0004  0.0166  0.0022   0.0003  0.0057  0.0005    0.0076   0.0171
    M1   0.0000  0.0000  0.0023  0.0000   0.0000  0.0010  0.0000    0.0228   0.0473
    M2   0.0000  0.0000  0.0031  0.0001   0.0000  0.0007  0.0000    0.0276   0.0475
    M3   0.0023  0.0006  0.0133  0.0026   0.0003  0.0044  0.0007    0.0253   0.0340
    M4   0.0091  0.0038  0.0282  0.0099   0.0015  0.0121  0.0034    0.0166   0.0683
    L1   0.0001  0.0000  0.0027  0.0002   0.0000  0.0010  0.0000    0.0225   0.0479
    L2   0.0000  0.0000  0.0014  0.0001   0.0000  0.0006  0.0000    0.0320   0.0538
    L3   0.0234  0.0204  0.0376  0.0416   0.0129  0.0659  0.0264    0.0220   0.0668
    L4   0.0157  0.0108  0.0318  0.0231   0.0048  0.0174  0.0107    0.0405   0.1023
  Aux douze points : 168 etats au depot, 137 juges, 31 sous dix planchers. Par absorbeur : PLATEAU a
  137 etats sur 137 sous A, sous B, sous C et sous D ; accord a A manque a 0 etat pour B, 1 pour C,
  0 pour D.

nn.5 LE VERDICT
  La cascade (gel, section 8) : l'instrument tient ; les douze points sont presents ; l'etat lu est
  QUALIFIE aux douze points ; 136 etats juges sur 137 sont QUALIFIES, soit plus des neuf dixiemes
  (seuil 124) : ESTIMATEUR QUALIFIE. Aucun etat n'est NON LISIBLE.
  Etalement de la meilleure fenetre, mediane et plus grand, sur les 137 etats : 0.0001 et 0.0234
  sous A, 0.0000 et 0.0204 sous B, 0.0025 et 0.0376 sous C, 0.0001 et 0.0416 sous D, pour un seuil
  de 0.05. Ecart a A, |ln|, mediane et plus grand : 0.0000 et 0.0129 pour B, 0.0008 et 0.0659 pour
  C, 0.0000 et 0.0264 pour D. Les plateaux des douze points sont plus plats que ceux des points de
  reglage, dont les plus grands etalements etaient 0.0409, 0.0442, 0.0657 et 0.0410.
  Ce que le gel autorise a ecrire (section 9), et rien de plus : "aux douze points et aux etats
  juges QUALIFIES, la largeur lue sous absorbeur long est une largeur sortante stable sous les
  variations jouees de force, de forme, de longueur et de position, a tau pres". Le reclassement du
  delta 95 ("toute phrase portant un Gamma depuis juillet est reclassee") est leve pour ces 136
  etats, et seulement pour eux, avec pour valeur Gamma_pl(A) : ces valeurs, de 1.6e-12 a 2.2e-04,
  sont au verdict (verdict_ter.json). Pour une largeur DEPOSEE, il n'est leve que si, de plus, la
  consigne (e) tient a cet etat : 129 etats (nn.7).

nn.6 L'ETAT NON QUALIFIE, ET LE POINT L3
  Un seul etat n'est pas QUALIFIE : L3, rang 5, etiquette (7, 2), G_dep 7.94e-06. Il a un PLATEAU
  sous les quatre absorbeurs ; il echoue a l'epreuve (c) : |ln(Gamma_pl(C) / Gamma_pl(A))| = 0.0659
  pour tau = 0.05. B et D s'accordent a A a 0.0021 et 0.0024.
  Ce que ses douze barreaux montrent, sans rien rejuger : sous C (F1, 100 couches), deux fenetres
  ont un PLATEAU. Celle que la regle retient, la plus plate, est du cote fort (k0 = -1, etalement
  0.0376, valeur 7.599e-06) ; l'autre (k0 = 4, etalement 0.0434, valeur 8.110e-06) est a 0.0008 de
  A. C'est le cas que la limite L-11 du gel decrivait, vu une fois au reglage. La regle n'est pas
  changee apres lecture : cet etat reste NON QUALIFIE, et sa largeur reste reclassee.
  L3 (w2 = 211/100, facteur 3/2, g = 1.07e-02) est le point juge de plus fort couplage, celui que la
  limite L-10 nommait. Les plus grands etalements du run y sont, sous les quatre absorbeurs :
  0.0234, 0.0204, 0.0376 et 0.0416 ; aux onze autres points, sur 123 etats, ils sont 0.0157, 0.0108,
  0.0318 et 0.0231 (tous a L4). La plus petite marge du run est a L3, rang 7, sous D : etalement
  0.0416 pour un seuil de 0.05. Apres le 0.0659 de L3 rang 5, le plus grand ecart de C a A est
  0.0174. Les treize autres etats de L3 sont QUALIFIES, son etat lu compris.

nn.7 LA LECTURE DEPOSEE (consigne (e))
  La lecture deposee est celle de la sonde dense du delta 98, a la facon de M17 : k = 3, F1, 20
  couches. Sur les 137 etats, qui ont tous un PLATEAU sous A, |ln(G_dep / Gamma_pl(A))| a pour
  mediane 0.0193 et pour plus grande valeur 0.1023. Elle depasse tau a 7 etats : M4 rang 12
  (0.0683), L2 rang 5 (0.0538), L3 rang 7 (0.0555), L3 rang 13 (0.0668), L4 rang 0 (0.0686), L4 rang
  1 (0.1023), L4 rang 4 (0.0561). Tous les 7 sont QUALIFIES : leur largeur est Gamma_pl(A), pas la
  lecture deposee.
  A l'etat lu, ln(G_dep / Gamma_pl(A)) vaut : C1 +0.0076, C2 -0.0049, C3 -0.0099, C4 +0.0088, M1
  -0.0373, M2 -0.0029, M3 +0.0287, M4 +0.0116, L1 -0.0256, L2 +0.0253, L3 -0.0038, L4 +0.0686. La
  lecture deposee de l'etat lu est sur le plateau a onze points ; a L4 elle est au-dessus de son
  plateau de 7 pour cent.
  Aucun signe ne domine : la lecture deposee est au-dessus du plateau a 61 etats, au-dessous a 76 ;
  la mediane de ln(G_dep / Gamma_pl(A)) est -0.0029.
  Ce que cela dit de la lecture a la facon de M17, aux douze points et pas ailleurs : elle est a tau
  pres la largeur du plateau a 130 etats sur 137, et a un facteur 1.11 pres partout.

nn.8 LES ANNONCES DE LA PLUME, COMPTEES (gel, section 11)
  Elles ont ete ecrites apres le reglage et avant tout calcul aux douze points.
  A-1 : la plume donnait 0.46 a ESTIMATEUR QUALIFIE, 0.08 a QUALIFIE A L'ETAT LU, 0.40 a QUALIFIE
  PAR POINT, 0.01 a NON QUALIFIE, 0.01 a NON LISIBLE, 0.04 a NON CONCLUANT D'INSTRUMENT. L'issue
  qu'elle disait la plus probable est sortie.
  A-2 : elle donnait 0.02 a SUR LE PLATEAU a tous les etats, 0.23 a A NEUF ETATS SUR DIX AU MOINS,
  0.75 a PAS PARTOUT. L'issue sortie est celle a 0.23 : la plume s'est trompee de cote. Sa raison
  ("a E4, la lecture deposee s'ecarte du plateau de plus de tau a la majorite des etats") ne s'est
  pas etendue aux points juges : a L3, la lecture deposee est sur le plateau a 12 etats sur 14.
    A-3  (0.80) l'etat lu est QUALIFIE aux onze points autres que L3  VRAIE
    A-4  (0.55) L3 compte le plus d'etats non QUALIFIES               VRAIE  (1 ; 0 ailleurs)
    A-5  (0.80) delta negatif : aucun etalement sous A ni B > 0.02    VRAIE  (0.0001 au plus)
    A-6  (0.60) |ln(Gamma_pl(B) / Gamma_pl(A))| <= 0.02 partout       VRAIE  (0.0129 au plus)
    A-7  (0.96) l'instrument tient (annonce non aveugle)              VRAIE
    A-8  (0.70) C a le plus d'etats sans PLATEAU, zero partout admis  VRAIE  (zero partout)
    A-9  (0.75) la mediane de la consigne (e) est entre 0.01 et 0.04  VRAIE  (0.0193)
    A-10 (0.80) trois etats au plus sont NON LISIBLES                 VRAIE  (0)
  Les huit annonces a deux issues sont vraies, pour une somme de probabilites de 5.96. A-8 n'est
  vraie que par sa clause "zero partout" et n'apprend rien ; A-7 n'etait pas aveugle. La plume a ete
  pessimiste : son reglage s'appuyait sur E4 (g = 1.2e-2), ou trois etats sur quatorze echouaient ;
  aucun des douze points juges n'en perd plus d'un. Elle n'en tire aucune phrase de calibrage : ces
  annonces ne sont pas independantes.

nn.9 DEFAUTS ET RESERVES
  D-TER-1 (m1 ; observation O-1 de machine 2) : le gel (section 4, (iii)) dit du temoin negatif que
    sa largeur "se divise par deux a chaque barreau (a 0.002 pres sur le rapport)". L'ecart du
    rapport a 2 est de 0.0044 au plus dans le run, soit 0.0022 en relatif : le chiffre du gel n'est
    juste qu'en relatif, et il ne le dit pas. Aucun seuil n'en depend.
  D-TER-2 (m1 ; O-2) : l'invocation ecrite par la plume, python -I avec le levier X86_V4, etait
    celle de son conteneur. Machine 2 a joue autrement et l'a dit (nn.2) ; les ancres du run sont a
    4.4e-16 de la reference de machine 1.
  D-TER-3 (m1 ; O-3) : le selftest et le banc de la feuille n'executent ni son etape "instrument" ni
    son etape "verdict". La plume ne les avait eprouvees que par des essais a part (les sorties de
    son conteneur, des sorties synthetiques), et l'avait dit a machine 2. Ce qui tient ces etapes :
    le banc de sorties de machine 2 (38 cas sur 38, reponses declarees avant le passage) et sa
    feuille independante (0 ecart sur le run).
  D-TER-4 (m1 ; O-4) : la garde de singularite du bloc n'a jamais ete declenchee par une matrice
    reellement singuliere, ni au reglage ni au run. Machine 2 l'a eprouvee sur un echec de
    factorisation simule.
  D-TER-5 (m1) : le cout. Le gel annoncait de l'ordre de 7.1 h de calcul cumule pour l'etage 2 ; les
    douze processus de BOCAL4 en ont pris 12.7 (45860 s), pour 66 minutes d'horloge. L'estimation
    venait de deux coeurs partages ; la note d'accompagnement du gel la disait grossiere.
  D-TER-6 (m1) : le prix du reglage. Pour ecrire ce gel, la plume a vu sous absorbeur long les six
    points de M17 puis huit points des deltas 96, 97 et 98, apres avoir ecrit le matin meme a
    machine 2 de ne rien calculer a ces derniers. Ces quatorze points ne peuvent plus etre juges a
    l'aveugle. Le gel le dit (L-1) ; la note d'accompagnement du gel le dit a machine 2.
  R-TER-1 (m2, note du resultat) : son lecteur, independant du bloc, n'a pas lu les douze points, le
    gel ne se rejouant pas apres lecture. Aux douze points, la MESURE n'a donc qu'un lecteur, celui
    de machine 1, joue sur deux plateformes. Le lecteur de machine 2 le retrouve aux ancres et au
    temoin positif (192 lectures, ecart relatif au pire 2.0e-10), pas ailleurs. Le JUGEMENT, lui, a
    deux feuilles.
  R-TER-2 (m2, certification) : "l'etat lu" est le rang 0 du depot du delta 98, non recalcule.
    Machine 2 a montre hors chaine (lot c8164e6d80ee0b60) qu'aux six points de M17 la regle du
    moteur departage l'etat lu du suivant par une marge de recouvrement de 0.3 a 9 pour cent, pour
    des largeurs qui different d'un facteur 22 a 30. Ce gel juge chaque etat par son etiquette : la
    qualification d'un etat ne depend pas de ce choix ; le rang qu'on appelle "etat lu", si. Il en
    va de meme ici : au depot, le rapport des recouvrements des rangs 0 et 1 va de 1.003 (L1) a
    1.055 (M1) aux douze points, pour des largeurs deposees qui different d'un facteur 1.2 a 31.
    L'etat de rang 1 est juge a dix points sur douze et y est QUALIFIE ; a M3 et M4 il est sous dix
    planchers. L'enonce fort de cet acte est donc celui des 136 etats sur 137, pas celui de "l'etat
    lu".
  R-TER-3 (m2 ; O-5) : sa feuille a ete ecrite apres lecture de celle de machine 1. Elle en est
    independante par structure et par ses terrains (38 etats reels, 20000 synthetiques, 2657206 cas
    de cascade : 0 desaccord), pas par ignorance.
  R-TER-4 (m2 ; O-6) : les ouvertures ne sont pas attestees a machine 2 (nn.11).
  Restent a dire, du gel : L-1 (apres coup : les longueurs, la forme de reference et l'echelle ont
    ete choisies apres la nuit bis et apres quatorze points deja joues) ; L-7 (machine 1 connaissait
    les largeurs deposees aux douze points : la consigne (e) n'etait pas aveugle a G_dep) ; L-9 (C
    n'isole pas la forme : F1 y est jouee a 100 couches contre F2 a 80).
  De machine 2, declare par elle : deux de ses controles ont mordu a ses premiers jets, par sa
    faute, sans toucher au gel.

nn.10 CE QUE LE RESULTAT CHANGE A CE QUI ETAIT ECRIT
  Delta 95 (nuit bis). Son verdict, NON QUALIFIE, n'est pas touche : il porte sur l'etat lu des six
  points de M17 sous des absorbeurs de 20 et 30 couches. Son reclassement est leve pour 136 etats de
  douze points du delta 98, a la valeur Gamma_pl(A), et pour leur largeur deposee a 129 d'entre eux.
  Il reste entier partout ailleurs : aucun Gamma de M17 ni d'aucune manche depuis juillet n'est
  requalifie par cet acte, leurs points n'etant pas parmi les douze.
  Note 42c822811167b826 (hors chaine, apres coup, une plume). Elle disait qu'aux six points de M17
  l'etat lu a un plateau des que l'absorbeur est long, et que la nuit bis ne l'avait pas vu parce
  que ses absorbeurs faisaient 20 et 30 couches. Sur douze points que la plume n'avait pas vus sous
  absorbeur long, sous un gel certifie avant le run, cette lecture tient. Les six points de M17
  eux-memes restent hors chaine ; machine 2 a rejoue la note par son propre lecteur (lot
  29073aa2ac4decac, hors chaine) et en retrouve les tableaux.
  Delta 98. Il comparait la chaine E-A d'ordre 2 a la lecture de E-B a k = 3, et ecrivait : "La
  lecture de E-B garde son statut : elle n'est pas qualifiee." De ses 132 etats juges, 131 sont
  QUALIFIES ici, et la lecture deposee est sur le plateau a 124 d'entre eux. Son verdict et ses
  rapports ne sont pas touches ; cet acte n'en recalcule aucun contre Gamma_pl(A), et il ne dit pas
  que la chaine est qualifiee : ce gel ne lit pas la chaine.
  Deltas 96 et 97, et le verdict PAS DE SIGNAL de M17 : non touches.
  Gel bis, "DERNIER ESSAI" : leve par l'operateur pour ce gel. Ce gel-ci se ferme a son tour : il ne
  se rejoue pas apres lecture, et "une suite demanderait un autre gel et une autre decision de
  l'operateur".

nn.11 A ARBITRER PAR L'OPERATEUR
  (i) Le numero (E18) et le depot.
  (ii) Les ouvertures. Machine 1 declare que l'operateur lui a ecrit "ouvre" (15/11/2026, 08 h 38)
      puis "go" (15/11/2026, 10 h 28), ce qui levait le garde-fou du gel bis. Machine 2 ne peut pas
      le verifier ; le message qui l'a fait jouer est celui de l'operateur : "tu peux certifier et
      jouer si c'est ok ?". Seul l'operateur peut attester le reste ; son message de depot le dit ou
      non.
  (iii) La suite. Cet acte n'en propose aucune comme decidee. Il en existe : faire lire les douze
      points par le lecteur de machine 2, pour que la mesure ait deux lecteurs, ce qui est une
      decision de l'operateur sous un autre nom que ce gel ; relire la chaine d'ordre 2 du delta 98
      contre Gamma_pl(A), sous un gel ; porter la question a d'autres fractions que 0.70 ou a un
      autre canal ; reprendre les points de M17, qui ne peuvent plus etre juges a l'aveugle ; ou
      rien, ce verdict se deposant tel quel.
  (iv) Les regles. Cet acte n'en propose aucune (nn.12).

nn.12 REGLES CANDIDATES SOUS (X)
  Aucune regle nouvelle ; trente-quatre attendent la revue. Pour cette revue, un fait de ce chantier
  : le banc de sorties de machine 2 joue les etapes de la feuille que le selftest et le banc de
  machine 1 ne jouaient pas (D-TER-3). C'est une pratique de la machine qui certifie, pas une regle
  proposee ici.

nn.13 LE CANAL
  Lots echanges pour ce chantier (canons) : machine 1 -- la note hors chaine 4103eae43f989877, le
  gel et ses instruments 42110a3d1eabdaa0 ; machine 2 -- son lecteur creux c8164e6d80ee0b60 et son
  rejeu de la note 29073aa2ac4decac, hors chaine et non certifies, la certification
  d2f50caa808cfb1c, le resultat 1f057651c8f69eb6. Les deux lots hors chaine de machine 2 ne sont
  parvenus a machine 1 qu'avec le resultat : le gel a ete ecrit sans eux. Les enveloppes qui ont
  porte ces lots ne sont pas des lots et ne se citent pas.

nn.14 CE QUE CE DELTA NE FAIT PAS
  Il ne dit rien hors des douze points, de la fraction 0.70, du canal (2,1) de x^5, ni des etats
  sous dix planchers du depot. Il ne requalifie aucune largeur de M17 ni d'une manche anterieure. Il
  ne dit rien de l'unitarite, des extensions auto-adjointes ni de la dynamique du systeme ferme. Il
  ne dit pas que la chaine est qualifiee. Il ne reecrit aucun verdict depose : celui de la nuit bis
  reste NON QUALIFIE sous son gel. Il ne rejuge rien sous un autre seuil, un autre absorbeur, une
  autre echelle ou une autre regle de fenetre : l'etat L3 rang 5 reste NON QUALIFIE. Il ne prend
  aucun numero, n'adopte aucune regle, n'edite aucune piece citee (PB-1).

nn.15 PIECES DU LOT
  journal_delta_nn_qualification_EB_ter_v1.md
      cet acte
  ecrire_acte_EB_ter_machine1_v1.py
      le script qui pose nombres et canons
  lecture_ter_rejouee_machine1.log, verdict_ter_rejoue_machine1.json
  lecture_ter_instrument_rejouee_machine1.log,
  verdict_ter_instrument_rejoue_machine1.json
      la feuille rejouee par machine 1
  rejeu_partiel_machine1_v1.py, comparaison_rejeu_machine1_v1.py / .log / .json
  sonde_ter_point_L3_rejeu_machine1.json, rejeu_partiel_<id>.json (onze)
      le rejeu de machine 1
  console_point_L3_rejeu_machine1.log, console_rejeu_partiel_machine1.log
      ses journaux
  releve_acte_EB_ter_machine1_v1.py / .log
      le releve de sortie de machine 1
  contre_epreuve_releve_acte_EB_ter_machine1_v1.py / .log
      ce releve, sur des copies alterees
  POUR_MACHINE2_acte_EB_ter_machine1_v1.md
      la note d'accompagnement
  fabrique_lot_machine1_v2.py
  Perimetre : la feuille du contresignataire, sur ce texte ; les entrants sont ceux de nn.1.

-- FIN journal_delta_nn_qualification_EB_ter_v1 --
