RESULTAT DU RUN UNIQUE DU GEL "LARGEUR DU VIDE" -- machine 2 pour machine 1 -- 2026-11-16, v1
Le run est joue, une seule fois. Verdict de TA feuille, jouee par le pilote dans le run : V1 TENU ; VP TENU. Rien n'est depose.

0. CE QUE CE LOT EST, ET CE QUI RESTE A TOI
  C'est le lot de resultat de ta section 11 (4) : les fichiers de l'etage A, les 28 fichiers de cellule, le verdict, les journaux, le journal du pilote ; plus ce que j'ai fait apres le run (ma feuille
  rejouee sur les memes fichiers, une analyse, l'authentification de ton rectificatif). Il reste a toi, section 11 (5) et (6) : authentifier ce lot, rejouer TA feuille sur run_gel_vide_machine2/run_1/,
  ecrire l'acte. Le verdict qui compte est celui de la feuille jouee dans le run ; si ta feuille rejouee en donne un autre, l'acte donne les deux et retient le moins favorable.

1. LE FEU VERT
  Le 16/11 a 19:10 (heure de BOCAL4), l'operateur a ecrit : "M1 a livre, tu peux jouer ensuite si tout te semble propre". Je lis ce message comme le feu vert ecrit de ta section 11 (2), conditionnel : j'ai
  d'abord authentifie ton rectificatif (section 2), puis verifie la machine (section 3), puis joue. Ce message n'atteste pas tes declarations d'ouverture (10 h 10, 11 h 03, "on gele et on avance !" 12 h 19) ;
  je n'en atteste aucune non plus : l'acte les cite comme tes declarations.

2. TON RECTIFICATIF (lot 71ec801a5f86e068, 7 pieces)
  Authentifie : canon du manifeste calcule par moi 71ec801a5f86e068, 0 morsure, note a plat = note du lot (336913aecc732cdf), aucune piece en trop. Mon rejeu de ton verifie_C1_C2_machine1_v1.py sur ses trois
  entrees (table gelee b71206e5daf6c741, superposition aeb9fc40ecc43899, verifie_variantes e9a0a3812de6ad16, canons recoupes) rend ta console et ton json a l'octet. Mes propres sorties recoupent C-1 (rapport
  X(w2)/X(2) de 0.9386 a 1.0704, ecart de la forme fermee 3.42 a MG16), C-2 (184 parts manquees positives, 182 dans ]0,1[, 2 au-dessus de 1, 1 negative) et la partition de A-7 (11 cellules ou les lectures
  different, 5 ou elles coincident, memes etendues minimales par creneau). Je n'ai PAS recalcule les tailles du residu sous (b) (0.0022, 0.0090, ...) : elles sortent de ton script rejoue sur la table gelee.
  D-VIDE-7 et D-VIDE-8 : acceptes comme corrections de texte. Ils ne touchent aucun nombre juge.

3. CONDITIONS DU RUN
  Un lanceur de ma main (lance_run_vide_machine2_v1.py) ; il ne modifie aucun script emis. Avant de lancer il refuse hors secteur et recalcule les 12 canons (pilote a38b1550f8f5e3cf, moteur, depot, retenus, tp_reference,
  reference des ancres, table ordre 3, sonde et feuille du lecteur, table des cellules du gel, sonde_vide, feuille_vide) : tous au canon attendu, journal du lanceur. Secteur branche, batterie 100 %, veille
  interdite pendant le run, charge parasite de 7 % avant le lancement (Chrome, VS Code, un service AMD, chacun sous un demi-coeur). Pilote lance UNE fois, dossier neuf run_1, 8 processus, --drapeau -P,
  python 3.11.9, clone frais du registre a dee73bd. Debut 19:13:54, fin 19:57:11 : 2597 s ; code de sortie 0 ; aucun arret, aucun appel rejoue. Avant la fin du pilote je n'ai lu que le journal de
  demarrage du lanceur (les canons) : ni la console du pilote, ni le dossier du run.

4. RESULTAT (verdict_vide.json de ta feuille ; canon du verdict 8472dba8919a9b6e)
  Instrument du lecteur : TIENT (etage 0 20 s, ancres 659 s, etage 1 700 s ; canon de son verdict cc54f4bc4e175143). 28 cellules : toutes QUALIFIEES ; jumeau tenu 28 sur 28 (48 lectures suivies sur 48,
  plus grande largeur du jumeau 3.89e-36, plus grand rapport au plateau 1.32e-27 contre le seuil 1e-6) ; les quatre absorbeurs en PLATEAU partout ; poids minimal 0.999 ; aucun echec, aucune cellule non lisible.
  V1 (16 lisibles) : TENU, 16 TIENT. VP (12 profondes) : TENU, 12 TIENT. NON JUGEABLE 0, NON LUE 0, TOMBE 0. Le run est complet.
  ln q = ln G3 (table gelee) - ln Gamma_pl : positif quand la chaine d'ordre 3 depasse la mesure. Les 28 cellules :
    cellule  w2         m   ln Gamma_pl  etal.s  etendue  bande b  ln q       T     jugement
    MG3      991/500    3      -19.6443  0.0016  0.0013   0.0030   +0.00024  0.02  TIENT
    MG4      991/500    4      -23.4596  0.0015  0.0014   0.0029   +0.00042  0.02  TIENT
    MG5      991/500    5      -27.3358  0.0004  0.0026   0.0029   +0.00055  0.02  TIENT
    MG6      991/500    6      -31.2989  0.0002  0.0022   0.0024   +0.00068  0.02  TIENT
    MG8      991/500    8      -39.3244  0.0018  0.0054   0.0072   +0.00050  0.05  TIENT
    MG12     991/500    12     -55.6116  0.0005  0.0092   0.0097   +0.00050  0.05  TIENT
    MG16     991/500    16     -72.0324  0.0001  0.0086   0.0087   +0.00122  0.05  TIENT
    MP3      1997/1000  3      -21.4263  0.0022  0.0027   0.0048   -0.00005  0.02  TIENT
    MP4      1997/1000  4      -25.2361  0.0005  0.0029   0.0034   +0.00035  0.02  TIENT
    MP5      1997/1000  5      -29.1067  0.0005  0.0020   0.0025   +0.00036  0.02  TIENT
    MP6      1997/1000  6      -33.0638  0.0010  0.0058   0.0068   +0.00007  0.02  TIENT
    MP8      1997/1000  8      -41.0771  0.0029  0.0064   0.0093   -0.00006  0.05  TIENT
    MP12     1997/1000  12     -57.3391  0.0003  0.0091   0.0094   +0.00041  0.05  TIENT
    MP16     1997/1000  16     -73.7344  0.0003  0.0074   0.0077   +0.00047  0.05  TIENT
    PP3      401/200    3      -20.9155  0.0020  0.0032   0.0052   +0.00019  0.02  TIENT
    PP4      401/200    4      -24.7237  0.0002  0.0042   0.0045   +0.00020  0.02  TIENT
    PP5      401/200    5      -28.5925  0.0011  0.0041   0.0052   +0.00031  0.02  TIENT
    PP6      401/200    6      -32.5478  0.0018  0.0052   0.0070   +0.00024  0.02  TIENT
    PP8      401/200    8      -40.5572  0.0031  0.0068   0.0099   -0.00031  0.05  TIENT
    PP12     401/200    12     -56.8109  0.0014  0.0083   0.0096   +0.00053  0.05  TIENT
    PP16     401/200    16     -73.1973  0.0001  0.0054   0.0055   -0.00030  0.05  TIENT
    PG3      2017/1000  3      -19.6990  0.0006  0.0054   0.0060   +0.00017  0.02  TIENT
    PG4      2017/1000  4      -23.5064  0.0019  0.0063   0.0082   +0.00032  0.02  TIENT
    PG5      2017/1000  5      -27.3743  0.0021  0.0069   0.0090   +0.00006  0.02  TIENT
    PG6      2017/1000  6      -31.3284  0.0023  0.0070   0.0093   -0.00058  0.02  TIENT
    PG8      2017/1000  8      -39.3352  0.0016  0.0084   0.0100   -0.00022  0.05  TIENT
    PG12     2017/1000  12     -55.5832  0.0007  0.0077   0.0085   +0.00073  0.05  TIENT
    PG16     2017/1000  16     -71.9634  0.0004  0.0068   0.0073   +0.00134  0.05  TIENT
  Plus grand |ln q| : 0.0007 aux lisibles (MG6), 0.0013 aux profondes (PG16). Plus petite marge T - b - |ln q| : 0.0101 aux lisibles, 0.0398 aux profondes. Etalement s du lecteur au vide : de 0.0001 a 0.0031,
  mediane 0.0011 (je l'avais mesure aux 144 etats joues du delta 100 : au plus 0.0052). Le |ln q| est sous l'etendue de la chaine a 28 cellules sur 28, et sous la bande b a 28 sur 28.

5. MES CONTROLES APRES LE RUN
  (a) Ma feuille (a6754241629160a7, ecrite de ton texte) rejouee sur les memes fichiers : meme verdict, jugements, statuts du lecteur et temoins identiques a 28 cellules sur 28, ecart nul sur ln q, bande,
      etalement et ln Gamma_pl. Ce zero est moins fort qu'il n'en a l'air : nos deux feuilles appellent la meme routine deposee juger_etat.
  (b) ln q recalcule avec MES predictions (mon ln G3 d'ordre 3, issu de mon script predictions_vide_machine2_v1.py) : ecart maximal a celui de ta feuille 4.26e-09, soit l'ecart entre ta table gelee et mes predictions. Le chemin
      du fantome de ta sonde_vide n'avait jamais tourne avant ce run (le pre-vol ne le lit pas, G-6) : ce qui le garde est que ses 28 largeurs retrouvent des chaines que j'ai calculees de mon cote, a 0.0013 pres
      au pire, sur 54 unites de ln Gamma (de e^-19.6 a e^-73.7, environ 23 decades).
  (c) Le verdict d'instrument du run est celui du pre-vol sur BOCAL4, champ pour champ ; seuls trois canons de fichiers de sortie de l'etage A different (ils portent des durees).
  (d) La consigne de ta feuille est retrouvee : ln q du signe de delta a 12 cellules ; ordre 3 plus pres de la mesure que l'ordre 1 a 26 cellules, que la loi d'echelle a 27 ; plus grand |ln q| de la forme fermee
      0.1136 (consigne, non jugee). Le "19" (signe de la sous-correction) est celui de ta feuille : je ne l'ai pas recompte.

6. TES ANNONCES (section 10), UNE A UNE, SELON LEURS MOTS
  A-1 l'instrument tient : oui. A-2 le temoin tient aux 28 cellules : oui. A-3 le lecteur qualifie les 16 lisibles : oui, 16 sur 16. A-4 V1 : TENU (annonce 0.50) ; l'issue que tu craignais, NON CONCLUANT (0.32),
  ne s'est pas produite : 0 cellule non jugeable. A-5 VP : TENU (annonce 0.35). A-6 plus grand |ln q| aux lisibles sous 0.01 : oui, 0.0007. A-7 le signe de ln q aux lisibles de MG : positif a 4 sur 4 (MG3 a MG6),
  soit la branche (b) ("positif, a trois au moins").
  Ce que A-7 ne dit pas, et que ton rectificatif (3) disait : un signe ne departage que si la taille depasse l'etendue de la chaine. Aux MG, ln q vaut +0.0002, +0.0004, +0.0005, +0.0007 contre des etendues de
  0.0013, 0.0014, 0.0026, 0.0022 : la taille ne la depasse a aucune cellule. A-7 est donc vraie dans sa lettre, et le run ne departage pas (a) de (b).

7. CONSIGNE, SANS JUGEMENT (ma lecture, posterieure au run ; ce n'est pas un enonce du gel)
  ln q > 0 a 22 cellules sur 28 (mediane +0.00032) : MG 7 sur 7, MP 5 sur 7, PP 5 sur 7, PG 5 sur 7. Quand delta < 0 (MG, MP) il est positif a 12 cellules sur 14 ; quand delta > 0 (PP, PG) a 10 sur 14. Son
  signe ne suit donc pas celui de delta : il est du signe de (b) a MG et MP, du signe de (a) a PP4 a PP6, la ou les deux lectures different. Un petit decalage positif commun aux deux signes de delta (de l'ordre
  de 3e-4) est compatible avec ces 28 nombres. Il est sous la bande b a chaque cellule : le gel ne peut ni le confirmer ni l'ecarter, et personne ne l'avait ecrit avant le run. Ne pas en faire un resultat.

8. CE QUE JE N'AI PAS FAIT
  Aucun depot : le registre est a dee73bd (releve a l'instant de la fabrication de l'enveloppe), le numero 102 est libre. Aucun appel rejoue, aucun script emis modifie (pilote, sonde, feuille, lecteur). Je n'ai
  pas verifie que deux executions de l'etage B donnent les memes octets : par regle il n'y a qu'un run. Je n'ai pas relu ta sonde_vide ligne a ligne apres le run ; ma certification de la partie 2 portait sur les
  predictions, la feuille, le banc, les refus et le pre-vol. Ce run ne dit rien des cellules non tirees, ni des |delta| hors de 0.003 a 0.018, ni des centiemes exclus.

9. CE QUI RESTE A TOI
  Authentifier ce lot (le manifeste est dans le ZIP et a cote). Rejouer TA feuille, feuille_vide_machine1_v1.py (ac39a24def6c7420), sur run_gel_vide_machine2/run_1/ : tu dois retrouver verdict_vide.json
  (canon 8472dba8919a9b6e) et ma feuille. Ecrire l'acte : le run est joue une fois, par quel pilote et quelle table, ce que tes annonces valaient, les deux comptes de signes, ton rectificatif C-1 et C-2, et le
  fait que le gel ne departage pas (a) de (b). Aucun depot sans ordre ecrit de l'operateur.

10. PIECES DE CE LOT (convention B)
    cette note
    5a73b5a492d5d4a2  run_gel_vide_machine2/lance_run_vide_machine2_v1.py
    a33094de0bba5714  run_gel_vide_machine2/lanceur_run_1.log
    2d8e6692d862fa37  run_gel_vide_machine2/console_run_1.log
    1d9e8f5da3b1a95a  run_gel_vide_machine2/run_1/console_ancres.log
    06eca800390ce410  run_gel_vide_machine2/run_1/console_etage0.log
    8d2e031aac22074b  run_gel_vide_machine2/run_1/console_etage1.log
    4d8a4a953a99ab8c  run_gel_vide_machine2/run_1/console_vide_MG12.log
    717f3048adddc68e  run_gel_vide_machine2/run_1/console_vide_MG16.log
    02ecb74a08f09459  run_gel_vide_machine2/run_1/console_vide_MG3.log
    bdea1c99a3782624  run_gel_vide_machine2/run_1/console_vide_MG4.log
    2f9bd45a092811ee  run_gel_vide_machine2/run_1/console_vide_MG5.log
    45d3f1b9bfba336b  run_gel_vide_machine2/run_1/console_vide_MG6.log
    406642ede1d230f2  run_gel_vide_machine2/run_1/console_vide_MG8.log
    5502240c4882150e  run_gel_vide_machine2/run_1/console_vide_MP12.log
    d9b05bea0d473325  run_gel_vide_machine2/run_1/console_vide_MP16.log
    7ffe0a30959d2104  run_gel_vide_machine2/run_1/console_vide_MP3.log
    8a01d6da3e8e28e5  run_gel_vide_machine2/run_1/console_vide_MP4.log
    cdf09af06a013575  run_gel_vide_machine2/run_1/console_vide_MP5.log
    3ff6e89d26be6036  run_gel_vide_machine2/run_1/console_vide_MP6.log
    9a9bd5b58b47c2c0  run_gel_vide_machine2/run_1/console_vide_MP8.log
    0898137d7471827e  run_gel_vide_machine2/run_1/console_vide_PG12.log
    7862347a413393f4  run_gel_vide_machine2/run_1/console_vide_PG16.log
    1307c1764d1be4c0  run_gel_vide_machine2/run_1/console_vide_PG3.log
    cb8ec07599c70f36  run_gel_vide_machine2/run_1/console_vide_PG4.log
    6889fa8f7050419b  run_gel_vide_machine2/run_1/console_vide_PG5.log
    36048a92f67c84df  run_gel_vide_machine2/run_1/console_vide_PG6.log
    cd49b62c960d114e  run_gel_vide_machine2/run_1/console_vide_PG8.log
    7a3b7a4a071eeb0b  run_gel_vide_machine2/run_1/console_vide_PP12.log
    8b708eaa993715d4  run_gel_vide_machine2/run_1/console_vide_PP16.log
    5b7d30a21d49ad56  run_gel_vide_machine2/run_1/console_vide_PP3.log
    cf122710bc72a661  run_gel_vide_machine2/run_1/console_vide_PP4.log
    fcf003d1c771cba1  run_gel_vide_machine2/run_1/console_vide_PP5.log
    6d6b4a1ad40eea80  run_gel_vide_machine2/run_1/console_vide_PP6.log
    4a15f2bd73cf6698  run_gel_vide_machine2/run_1/console_vide_PP8.log
    93e754709fe77393  run_gel_vide_machine2/run_1/feuille_vide.log
    d540ad2ad2cc17f1  run_gel_vide_machine2/run_1/lecture_ter_instrument.console.log
    d540ad2ad2cc17f1  run_gel_vide_machine2/run_1/lecture_ter_instrument.log
    2d8e6692d862fa37  run_gel_vide_machine2/run_1/pilote_gel_vide.log
    02adf58596b69da4  run_gel_vide_machine2/run_1/sonde_ter_ancres.json
    a9468bffd475a4e2  run_gel_vide_machine2/run_1/sonde_ter_etage0.json
    21fdb69566e2cc99  run_gel_vide_machine2/run_1/sonde_ter_etage1.json
    daeb043e5bba7433  run_gel_vide_machine2/run_1/sonde_vide_MG12.json
    8e7175c8d9d750d9  run_gel_vide_machine2/run_1/sonde_vide_MG16.json
    ef3a811ded0ef75e  run_gel_vide_machine2/run_1/sonde_vide_MG3.json
    b4056b89fde6ad64  run_gel_vide_machine2/run_1/sonde_vide_MG4.json
    f04b98f7b5a2a472  run_gel_vide_machine2/run_1/sonde_vide_MG5.json
    b94703a79dc7551d  run_gel_vide_machine2/run_1/sonde_vide_MG6.json
    5f1c9c3018af9fbb  run_gel_vide_machine2/run_1/sonde_vide_MG8.json
    4c25cc3db249749e  run_gel_vide_machine2/run_1/sonde_vide_MP12.json
    7520439aaca66227  run_gel_vide_machine2/run_1/sonde_vide_MP16.json
    b479021631cdf036  run_gel_vide_machine2/run_1/sonde_vide_MP3.json
    0f599b636a14c71b  run_gel_vide_machine2/run_1/sonde_vide_MP4.json
    e3273f6fe9e6ec1f  run_gel_vide_machine2/run_1/sonde_vide_MP5.json
    9e1c48c0fb5ed8b7  run_gel_vide_machine2/run_1/sonde_vide_MP6.json
    a0d26038f85c5599  run_gel_vide_machine2/run_1/sonde_vide_MP8.json
    9f0f6f7e28eaf65a  run_gel_vide_machine2/run_1/sonde_vide_PG12.json
    f41540e000345e19  run_gel_vide_machine2/run_1/sonde_vide_PG16.json
    d6911831c53dde9c  run_gel_vide_machine2/run_1/sonde_vide_PG3.json
    b46650d4adcca52a  run_gel_vide_machine2/run_1/sonde_vide_PG4.json
    816b3479fb05b6a3  run_gel_vide_machine2/run_1/sonde_vide_PG5.json
    9d0b9f1b66ad600f  run_gel_vide_machine2/run_1/sonde_vide_PG6.json
    3048f2623a275462  run_gel_vide_machine2/run_1/sonde_vide_PG8.json
    822f65b22820acfe  run_gel_vide_machine2/run_1/sonde_vide_PP12.json
    f752e092a4fdd3a7  run_gel_vide_machine2/run_1/sonde_vide_PP16.json
    d0f9264c1e10206f  run_gel_vide_machine2/run_1/sonde_vide_PP3.json
    bd9979f1b0fae211  run_gel_vide_machine2/run_1/sonde_vide_PP4.json
    13e33bfdc3720da0  run_gel_vide_machine2/run_1/sonde_vide_PP5.json
    6c4af30ba12ad8b8  run_gel_vide_machine2/run_1/sonde_vide_PP6.json
    d9072322a398802c  run_gel_vide_machine2/run_1/sonde_vide_PP8.json
    cc54f4bc4e175143  run_gel_vide_machine2/run_1/verdict_ter_instrument.json
    8472dba8919a9b6e  run_gel_vide_machine2/run_1/verdict_vide.json
    c95df19ff2f16ff7  resultats_run_vide_machine2/verdict_vide_feuille_machine2.json
    48cae27fc06339b9  resultats_run_vide_machine2/compare_feuilles_run_1_machine2_v1.py
    10c42cc8270f46be  resultats_run_vide_machine2/compare_feuilles_run_1_machine2_v1.log
    81ef96ab3a8ba427  resultats_run_vide_machine2/analyse_run_vide_machine2_v1.py
    fb40a36a3112ec79  resultats_run_vide_machine2/analyse_run_vide_machine2_v1.log
    6b101ef713ce83c1  livraison_16i_rectificatif_gel_vide_partie2/authentifie_rectificatif_m1_machine2_v1.py
    237678d171a059ba  livraison_16i_rectificatif_gel_vide_partie2/authentifie_rectificatif_m1_machine2_v1.log
    36d0fa1335d6da0e  livraison_16i_rectificatif_gel_vide_partie2/rejeu_machine2/verifie_C1_C2_rejoue_machine2.log
    d66a7349bae0e43b  livraison_16i_rectificatif_gel_vide_partie2/rejeu_machine2/verifie_C1_C2_rejoue_machine2.json
    (ce script)  fabrique_lot_resultat_run_gel_vide_machine2_v1.py
