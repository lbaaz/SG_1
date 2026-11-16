# POUR MACHINE 1 -- RESULTAT DU RUN JUGE DU GEL "QUALIFICATION E-B TER" (432319b9feb34b82), v1
# machine 2, 2026-11-15. Entrant : ton lot 42110a3d1eabdaa0. Ma certification : lot d2f50caa808cfb1c, scelle a 13 h 42 min 03 s, AVANT le debut du run (pilote : 13 h 42 min 11 s).
# Ce lot-ci est celui du resultat. Il ne contient PAS l'acte : l'acte est le tien (gel, section 12) ; je le contresignerai apres avoir tout recalcule de mes sources.

## 0. EN SIX PHRASES

Le run juge a ete joue UNE fois sur BOCAL4, le 15/11/2026 de 13 h 42 a 14 h 55 (4377 s), tous les appels a code 0, aucun rejoue, sur secteur ; l'instrument TIENT dans le run, aux memes chiffres qu'au pre-vol
(etage 0 84 sur 84, ancres 192 sur 192 a 4.4e-16, temoin positif 8 sur 8, temoin negatif 8 sur 8). Verdict de ta feuille : ESTIMATEUR QUALIFIE : l'etat lu (rang 0) est QUALIFIE aux douze points, et 136
etats sur 137 le sont (le seuil est 124). Issue de la consigne (e) : LA LECTURE DEPOSEE EST SUR LE PLATEAU A NEUF ETATS SUR DIX AU MOINS (130 sur 137) ; a l'etat lu elle l'est a onze points sur douze, L4 non
(|ln| = 0.0686 pour tau 0.05). Le seul etat NON QUALIFIE est L3 rang 5, (7, 2) : un etat large (G_dep 7.9e-6, pour une mediane de 2.3e-9 sur les 137 etats ; les plus larges du jeu vont jusqu'a 2.3e-4), dont l'accord C / A vaut 0.0659
pour tau 0.05 ; c'est le point que ton L-10 nommait. Ma feuille, independante de la tienne, rejuge les 137 etats et rend le meme verdict, la meme issue, les memes comptes et les memes plateaux : 0 ecart. Aucun appel
interrompu, 6576 lectures dont 0 non suivie ; je n'ai lance aucun calcul ni aucune lecture au-dela des douze appels et du pre-vol, et je n'ai rien depose (E18).

## 1. DEROULEMENT (pilote_EB_ter.log, avec les heures et les codes de sortie)

  13:42:11  debut du pilote ; dix canons verifies OK (gel, sonde, bloc, feuille, banc, reference des ancres, moteur, depot, retenus, table du temoin) ; Windows 10.0.26300, 16 coeurs, AMD64 ; BatteryStatus 2 (secteur).
  13:42:25 -> 13:48:47  etape 1 : etage0 (14 s), ancres (362 s), etage1 (396 s), trois processus, un fil chacun, code 0 ; feuille "instrument" : TIENT.
  13:48:47 -> 14:55:08  etape 3 : la sonde en mode point aux douze points, un processus par point, tous code 0, de 3772 s (M3) a 3981 s ; etape 4 : la feuille "verdict", code 0.
  Duree totale 4377 s. Python 3.11.9, numpy 2.2.6, scipy 1.15.3, un fil par processus, pas de levier X86_V4 ; chaque sortie consigne sa plateforme (G-T7) et le canon de la sonde b5616dcf858e8801 (G-T2).
  Un seul run : le pilote refuse si le dossier de sortie existe. Aucun appel n'a ete relance ; aucune sortie de la sonde n'a ete lue avant la fin du douzieme appel (je n'ai compte que les lignes de progression des consoles).

## 2. LES CHIFFRES (lecture_ter.log de ta feuille ; recalcules par ma relecture)

  Etats : 137 juges, 136 QUALIFIES, 1 NON QUALIFIE (L3 rang 5, epreuve (c) : accord C / A |ln| = 0.0659), 0 NON LISIBLES. Etats lus QUALIFIES : 12 sur 12. PLATEAU sous A, B, C et D a 137 etats sur 137.
  Par point (QUALIFIES / juges ; deposee sur le plateau) : C1 8/8 ; 8   C2 11/11 ; 11   C3 14/14 ; 14   C4 13/13 ; 13   M1 12/12 ; 12   M2 14/14 ; 14   M3 8/8 ; 8   M4 9/9 ; 8   L1 14/14 ; 14   L2 11/11 ; 10
  L3 13/14 ; 12   L4 9/9 ; 6.
  Etalement de la meilleure fenetre : sous A mediane 0.0001, plus grand 0.0234 ; sous B 0.0000 et 0.0204 ; sous C 0.0025 et 0.0376 ; sous D 0.0001 et 0.0416. Au reglage, tes plus grands etaient 0.0409, 0.0442,
  0.0657 et 0.0410 : les plateaux des douze points sont plus plats que ceux des points de reglage.
  Accords a A : B mediane 0.0000, plus grand 0.0129 ; C mediane 0.0008, plus grand 0.0659 ; D mediane 0.0000, plus grand 0.0264 (|ln|, 137 etats chacun).
  Consigne (e) : |ln(G_dep / Gamma_pl(A))| mediane 0.0193, plus grand 0.1023 ; au-dessus de tau a 7 etats sur 137 : M4 rang 12, L2 rang 5, L3 rangs 7 et 13, L4 rangs 0, 1 et 4 (tous QUALIFIES).
  A l'etat lu, G_dep / Gamma_pl(A) en logarithme : C1 +0.0076, C2 -0.0049, C3 -0.0099, C4 +0.0088, M1 -0.0373, M2 -0.0029, M3 +0.0287, M4 +0.0116, L1 -0.0256, L2 +0.0253, L3 -0.0038, L4 +0.0686 : la
  lecture deposee de l'etat lu est au-dessus de son plateau de 7 pour cent a L4, et sur le plateau aux onze autres points.
  Lectures : 6576, 0 non suivie ; 6461 a deux iterations, 110 a trois, 5 a quatre ; poids au site au moins 0.657 ; residu rapporte a max(1, |lambda|) au pire 9.8e-12 pour ton critere de 1e-11.

## 3. MA RELECTURE (relecture_independante_EB_ter_machine2_v1.log)

  MA feuille (0 desaccord a la certification sur 38 etats reels, 20000 synthetiques et 2657206 cas de cascade) rejuge les douze sonde_ter_point_*.json et le depot : verdict ESTIMATEUR QUALIFIE, issue
  "neuf etats sur dix au moins", 137 / 136 / 137 / 130 pour (juges, QUALIFIES, a plateau sous A, lus sur le plateau) : les tiens ; 0 ecart de statut, de plateau (k0, Gamma_pl a 1e-12) ou de consigne (e),
  etat par etat et absorbeur par absorbeur. Elle calcule aussi tes annonces, par MA lecture, non opposable : A-1 ESTIMATEUR QUALIFIE (annonce a 0.46), A-2 "neuf sur dix au moins" (0.23), et A-3 a A-10 tiennent
  (A-4 : L3 est seul avec un etat non QUALIFIE ; A-5 aux six points de delta negatif aucune fenetre sous A ni B ne depasse 0.02 ; A-6 plus grand ecart B / A 0.0129 ; A-8 : zero etat sans plateau partout, que ton
  texte compte comme vrai ; A-9 mediane 0.0193 ; A-10 zero etat non lisible). Le jugement des annonces est le tien.

## 4. CE QUE LE GEL AUTORISE A ECRIRE (section 9, pour ton acte ; rien n'est ecrit ici)

  ESTIMATEUR QUALIFIE : la phrase de la section 9, pour les douze points, les etats QUALIFIES (136) et avec pour valeur Gamma_pl(A) ; le reclassement du delta 95 est leve pour ces etats, et SEULEMENT pour eux ;
  il n'est leve pour une LARGEUR DEPOSEE que si la consigne (e) tient a cet etat : elle ne tient pas a sept etats (liste section 2), dont L4 rang 0, l'etat lu de L4. Le gel dit aussi : aucun verdict
  depose n'est reecrit, rien hors des douze points, de la fraction 0.70, du canal (2, 1) de x^5, ni des etats sous dix planchers du depot ; rien sur l'unitarite ; la chaine n'est pas qualifiee.
  L-1 (post hoc : longueurs, forme de reference et echelle choisies apres la nuit bis et apres quatorze points deja joues), L-7 (tu connais les largeurs deposees) et L-9 (C n'isole pas la forme) restent a dire.

## 5. CE QUI N'EST PAS FAIT

  Pas d'acte, pas de contreseing, pas de depot, pas de numero (E18) ; l'acte est a toi, le contreseing a moi apres. Mon lecteur n'a pas lu les douze points (le gel dit "ne se rejoue pas ... apres lecture" ; un
  controle de ton bloc par mon lecteur aux douze points serait une decision de l'operateur, sous un autre nom). L'attestation de "ouvre" et "go" par l'operateur : non donnee a machine 2 (O-6 de ma
  certification) ; l'acte dit la declaration et le message de l'operateur, sans conclure.

## 6. PIECES (convention B)

    cette note
    5d261985d0dce458  run_EB_ter/pilote_EB_ter.log
    5d261985d0dce458  certif_EB_ter/pilote_console.log
    944baacf1c64cc46  run_EB_ter/console_etage0.log
    3c0674204ba1bff4  run_EB_ter/console_ancres.log
    e29f84206fbd1b31  run_EB_ter/console_etage1.log
    066051f178a0bac8  run_EB_ter/console_point_C1.log
    0263344090307d94  run_EB_ter/console_point_C2.log
    5401a6c02f90ba35  run_EB_ter/console_point_C3.log
    9333bc6625847635  run_EB_ter/console_point_C4.log
    366177664a4eb61c  run_EB_ter/console_point_M1.log
    668a205db864782b  run_EB_ter/console_point_M2.log
    bede3dfbbecd45cd  run_EB_ter/console_point_M3.log
    efe5f46029af88e6  run_EB_ter/console_point_M4.log
    84f519ccc57741bc  run_EB_ter/console_point_L1.log
    a6f23648bf535c72  run_EB_ter/console_point_L2.log
    268db1e1120ccbc0  run_EB_ter/console_point_L3.log
    8f1c89b5540d9799  run_EB_ter/console_point_L4.log
    cfd3020e5a0d8a77  run_EB_ter/sonde_ter_etage0.json
    e51e8b56d2317130  run_EB_ter/sonde_ter_ancres.json
    f88a21eff655f6e8  run_EB_ter/sonde_ter_etage1.json
    73d4b1ea9cf5cc6d  run_EB_ter/sonde_ter_point_C1.json
    803f04c6ee0184e2  run_EB_ter/sonde_ter_point_C2.json
    26bf65590fe3a568  run_EB_ter/sonde_ter_point_C3.json
    2ef8dcb688d004a1  run_EB_ter/sonde_ter_point_C4.json
    ccd8ea674055d74f  run_EB_ter/sonde_ter_point_M1.json
    e31782c77231aa41  run_EB_ter/sonde_ter_point_M2.json
    544ae7e76f479d44  run_EB_ter/sonde_ter_point_M3.json
    171bce83277f2e76  run_EB_ter/sonde_ter_point_M4.json
    84b307184c91b501  run_EB_ter/sonde_ter_point_L1.json
    40eecf8d5d67d548  run_EB_ter/sonde_ter_point_L2.json
    f858e00396a6cab0  run_EB_ter/sonde_ter_point_L3.json
    d774cae11d3622c5  run_EB_ter/sonde_ter_point_L4.json
    a5cb7f6b8d14ffc5  run_EB_ter/lecture_ter_instrument.log
    a5cb7f6b8d14ffc5  run_EB_ter/lecture_ter_instrument.console.log
    3e9d22bcb044f75a  run_EB_ter/verdict_ter_instrument.json
    4db341d830781530  run_EB_ter/lecture_ter.log
    4db341d830781530  run_EB_ter/lecture_ter.console.log
    2cd1f84efa02f2ab  run_EB_ter/verdict_ter.json
    de535f989f02d069  certif_EB_ter/controles/relecture_independante_EB_ter_machine2_v1.py
    e0ce06dd37a91061  certif_EB_ter/controles/relecture_independante_EB_ter_machine2_v1.log
    6e7c721de5ac8311  certif_EB_ter/controles/relecture_independante_EB_ter_machine2_v1.json
    (ce script)  fabrique_lot_resultat_EB_ter_machine2_v1.py
