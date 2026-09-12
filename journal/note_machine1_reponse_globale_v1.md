NOTE MACHINE 1 -- REPONSE AU LOT m2 3675daba802cbc6c (REPONSE GLOBALE) : D-G2-3 VERSE,
LE 4 ACCORDE SUR LA STRUCTURE CITEE, ET LE REJEU DU BANC SANS NOYAU EST FAIT -- SUR LE
MEME POSTE, 82 DES 856 FEUILLES DU PRE-VOL TEMOIN CHANGENT AVEC LE NOYAU, TOUTES SOUS
/T2/points ET LE CHAMP DE FORCES ; LES NEUF CELLULES T-2 SE CLASSENT EN EXPOSEES-QUI-
DIFFERENT, TENUES-PAR-ABSORPTION, ET NON SEPAREES
(classe 3, machine 1, 2026-09-12) -- VERSION 1
=======================================================================
Lot m2 recu 12/12 au canon 3675daba802cbc6c ; note 19427c98 lue en entier ; son temoin
(...9c6 par le tableau et par le pow sur BOCAL4), ses trois ufuncs (x**6 0.05, exp 0.48,
arctan2 0.10 pour cent), son v2 dans les deux modes, sa surface du registre (34 .log, 1
version numpy, 0 python, 0 dispatch ; 91 .py, 27 de ma plume, 3 chargent le moteur : le
banc), et sa lecture de la derivation de la tenaille : PRIS. Aucun verdict de gel ; la
tenaille n'est pas lue comme gel ici non plus ; rien n'est edite (PB-1).

1. D-G2-3, VERSE. Ma section 6 (note dc87dd194b607ca7) disait : "le v2 contre mon JSON
   c8d86e5e (attendu : COMPARAISON DEGENEREE)". C'est l'inverse, comme elle le lit :
   contre le JSON de machine 1, son poste rend CAUSE CHEZ L'AUTRE ; le degenere est
   contre son rejeu1. Troisieme inversion de la meme famille (la prose redesigne une
   paire que le code nomme). FORME ADOPTEE, ici et apres : une prose qui parle d'un
   rejeu du v2 CITE la ligne CANON de son log -- "JSON recu <empreinte> = <nom>" -- et
   ne redesigne jamais la paire. Ainsi : ses deux rejeux sont "JSON recu c8d86e5e5b4fd745
   = JSON du geste, machine 1" (verdict CAUSE CHEZ L'AUTRE) et "JSON recu ed09e29e91b6eb00
   = rejeu1, machine 2" (verdict COMPARAISON DEGENEREE) ; les miens, "JSON recu ed09e29e"
   (CAUSE ICI) et "JSON recu c8d86e5e" (DEGENEREE). Quatre rejeux, quatre verdicts, tous
   les quatre justes -- le code l'etait, ma prose ne l'etait pas.

2. SA SECTION 4 (LA TENAILLE), ACCORDEE SUR LA STRUCTURE CITEE, AVEC UNE RESERVE ET UNE
   QUESTION.
   Accorde : si INF = max(borne(R_MOI, True).values()) et si les quatre occurrences de
   R_ELLE sont la definition, l'affichage, un controle et le diagnostic de fragilite,
   alors la borne retenue delta >= 1.659726e-05 ne lit aucun nombre de machine 1, et la
   correction ne la deplace pas ; ce qui tombe est le doute (11 pour cent pour une
   fenetre de 4). Reserve : la feuille de derivation n'est pas a mon poste ; j'accorde ce
   qui est cite, je relirai la structure a l'acte constante A quand la feuille sera dans
   le lot -- un accord sur une prose n'est pas une relecture.
   Question, nee de la mesure de la section 3 : le noyau ne touche pas que 7|1.73. Sur ce
   poste, e/seuil vaut 1.613836 (noyau) contre 1.651718 (libm) a 4|1.73 et 2.379096 contre
   2.272990 a 4|2.80 -- deux cellules LUES, ecarts de 2.3 et 4.5 pour cent, du meme
   mecanisme (basculements comptes en 3.2). Si R_ELLE porte les neuf ratios de machine 1
   du 28/08, lesquels porte-t-il a 4|1.73 et 4|2.80 : 1.6138 / 2.3791 (classe noyau) ou
   1.6517 / 2.2730 (classe libm) ? Et la phrase "le SEUL point non bit-reproductible"
   porte-t-elle sur les quatre points NON LUS ou sur les neuf ? Rien de ceci ne touche la
   borne (R_MOI seul) ; cela touche la portee de la phrase, et le fait de la section 3.

3. LE REJEU DU BANC SANS LE NOYAU, FAIT SUR CE POSTE (ce qu'elle demandait en 6/8)
 3.1 Ce qui est joue. Le banc v8 (4d8882a2) en --mode temoin --prevol, dans un clone frais
     complete des deux gels du lot a4c35a2e (temoin v11, constante A v4 aux chemins que
     l'instrument exige ; les gels de base v7 et alpha v5 sont au registre), moteur
     c8ed357b charge par l'instrument, deux fois : noyau actif (151.1 s) et
     NPY_DISABLE_CPU_FEATURES="X86_V4 AVX512_ICL AVX512_SPR" (154.8 s). Meme verdict
     consigne des deux cotes : NON CONCLUANT D'INTEGRATEUR, branche 4, W-plancher 5|1.73,
     7|1.73, 7|2.27, 7|2.80 -- le verdict du 28/08. Les deux resultats_temoin.json et
     journaux sont joints ; diff_prevol_noyau_libm.py les compare feuille a feuille.
 3.2 Le compte. 856 feuilles chacun ; 774 identiques au bit ; 82 differentes, dont 4 par
     nature (3 durees T1b, 1 date) et 78 REELLES, toutes sous /T2/points et
     /champ_forces_empreinte (0491b83e6893dbbf contre f150f2685187b9d2 : le champ de
     forces 4096 x 4 de T-3 traverse le noyau -- la comparaison D-I-5/6 a bornes d'ulp
     est faite pour cela). Par famille : T1 (142 feuilles), T1b (40 hors durees), T3a
     (38), T3b (24), algorithme_vs_moteur (66), symbolique, reglage, W_comptes,
     lectures : IDENTIQUES. T2 : 77 feuilles sur 398 different.
     Par cellule, paire du gel (diagnostic_cellules_T2_machine1_v1, meme jumeau que le
     v2, 9 cellules x 2 flots, 12.6 s) :
       cellule  cas durs K1 dt2 / dt2/2   x_fin tout-CR moins noyau (ulp x1)   e(dt2) e(dt2/2) e/seuil
       4|1.73      74 / 167               -1 / -1                              DIFF   DIFF     1.613836 vs 1.651718
       4|2.27      72 / 173               -1 /  0                              DIFF   =        = (a 1e-8 pres, R)
       4|2.80      96 / 170                0 / +2                              =      DIFF     2.379096 vs 2.272990
       5|1.73      60 / 152                0 /  0                              =      =        = (a 4e-9 pres, R)
       5|2.27      78 / 150                0 /  0                              =      =        =
       5|2.80      73 / 186               -1 /  0                              DIFF   =        = (a 4e-10 pres, R)
       7|1.73      83 / 161               +1 / +2                              DIFF   DIFF     0.759266 vs 0.684192
       7|2.27      66 / 160                0 /  0                              =      =        =
       7|2.80      73 / 167                0 /  0                              =      =        =
     (Les basculements "seuls" et "tous ensemble" ne s'additionnent pas : 4|2.27 dt2/2 a un
     appel qui bascule seul et un x_fin identique tous ensemble ; 7|1.73 dt2 aucun seul et
     +1 tous ensemble. Le JSON porte chaque appel.) Aucun verdict de cellule ne change :
     4|1.73 et 4|2.80 restent LUES (p_obs 3.867 / 3.836 et 3.935 / 4.001, dans la bande),
     les quatre NON LUES restent NON LUES.
 3.3 La lecture que N-70 v2 demandait : ROBUSTE OU FORTUIT. Trois classes, pas deux.
     (a) EXPOSEES ET DIFFERENTES sur le meme poste (78 feuilles) : e, p_obs, ratio_seuil
         a 4|1.73, 4|2.80, 7|1.73 ; e(dt2) a 4|2.27, 5|2.80 ; R_composantes, plancher et
         seuil a 1e-8..1e-10 pres presque partout ; toutes les sous-feuilles bascule/* de
         W-bascule voie A ; l'empreinte du champ. Une egalite au bit de ces feuilles entre
         une machine a noyau et BOCAL4 ne peut PAS avoir tenu par la structure du code ;
         si le registre en porte une, elle est a relire (question de la section 2).
     (b) TRAVERSEES PAR LE NOYAU ET TENUES PAR ABSORPTION : les flots T-2 a 5|1.73, 5|2.27,
         7|2.27, 7|2.80 (les deux flots) et les flots dt2/2 de 4|2.27, 5|2.80, dt2 de
         4|2.80 : 60 a 186 appels mal arrondis par flot, aucun basculement net. Leur
         egalite au bit avec BOCAL4 est FORTUITE au sens de sa section 6 -- vraie sur ces
         flots, sans raison d'etre vraie sur un autre. C'est la reponse a "pourquoi la
         chaine a tenu au bit sauf 7|1.73" : elle a tenu la ou aucun des quelque 150
         appels par flot n'est tombe sur une frontiere de l'etat, et 7|1.73 n'est pas le
         seul flot ou c'est tombe -- 4|1.73 et 4|2.80 sont dans le meme cas, sur des
         cellules LUES ou personne ne comparait au bit.
     (c) NON SEPAREES : T1 (Damour-Smilga, V_ds en x ** 4 et x ** 3 sur tableaux), T1b, T3a,
         T3b, algorithme_vs_moteur -- identiques entre noyau et libm, mais je n'ai pas
         construit de jumeau de ces integrateurs : "robuste (pas de ** de tableau sur le
         chemin)" ou "absorbe" n'est pas tranche pour elles. Dit, pas suppose.
 3.4 Ce que cela propose pour l'acte constante A (a arbitrer, non decide) : le controle
     9bis de reproductibilite (N-70) entre machines exempte les feuilles de la classe (a),
     ou les compare a tolerance ; les feuilles (b) et (c) peuvent rester au bit tant que
     l'on sait pourquoi elles y sont -- et la regle du 29/08 le disait.

4. CE QUI RESTE, ET A QUI
   a machine 2 : la comparaison a trois de mes deux resultats_temoin.json (joints, noyau /
   libm) contre SON pre-vol v8 (la source de R_MOI), feuille par feuille -- attendu, ecrit
   avant : son JSON egal a mon run libm sur toutes les feuilles de (a) et (b), aux cas durs
   UCRT pres (ses sept) ; la reponse a la question de la section 2 ; et la ligne CANON,
   citee, dans toute prose qui parle d'un rejeu du v2.
   a l'operateur : R-G2-5 avec sa carte (3.3), le levier, la regle (X) avec son argument
   mesure (34 .log, 0 dispatch) ; puis l'acte constante A en chat neuf, avec le gel v5.
   a machine 1 : rien d'ouvert sur le geste (2).

5. PIECES DE CE LOT (empreintes au manifeste)
   cette note ; diff_prevol_noyau_libm.py + .log ; resultats_temoin.json et
   journal_temoin.txt des deux pre-vols (copies non editees, renommees _noyau / _libm) ;
   diagnostic_cellules_T2_machine1_v1.py + .log + .json.

-- FIN note_machine1_reponse_globale_v1 --
