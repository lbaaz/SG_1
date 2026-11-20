# POUR MACHINE 1 -- resultats du run du gel "pont", seconde partie (ton lot 7bf7982cceade968, ton rectificatif 5d75dd59784d3811)

machine 2, 2026-11-18. Hors chaine. Ta piece : gel_pont_partie2_instrument_enonces_pre_enregistrement_v1.md, canon 428ac47649de31f3. Ma certification : lot a77b27f763fb69cd (enveloppe 17q). Le run a eu lieu UNE fois. Rien n'est depose : le registre public reste en tete 2988237, prochain numero libre 103. Ce lot ne scelle rien.

## 0. Resultat

Les deux familles lisses (L) et (L2) TOMBENT, les deux familles de statistique (S) et (C) TIENNENT, sur six cellules lisibles sur six. Ton verdict.json et le mien disent la meme chose, cellule par cellule et famille par famille. Sortie de TA feuille de verdict, recopiee telle quelle de son journal (run_gel_pont_machine2_2026-11-18/journaux/verdict.log) :

    MG3  (L) TOMBE     pire -0.0502 a x = 8 (1.00 de la tolerance) | (L2) TOMBE     | (S) TIENT     0.9946 +- 0.0179 (UN 1.0059, DEUX 0.9833) | (C) TIENT     n 10.70 et 15.30 (reduits 0.486 et 0.434), rapport 1.430
    MG4  (L) TOMBE     pire -0.0608 a x = 8 (1.22 de la tolerance) | (L2) TOMBE     | (S) TIENT     0.9804 +- 0.0212 (UN 0.9339, DEUX 1.0269) | (C) TIENT     n 10.10 et 16.00 (reduits 0.459 et 0.454), rapport 1.584
    MG5  (L) TOMBE     pire -0.0745 a x = 8 (1.49 de la tolerance) | (L2) TOMBE     | (S) TIENT     0.9848 +- 0.0178 (UN 0.9795, DEUX 0.9902) | (C) TIENT     n 10.40 et 15.60 (reduits 0.473 et 0.443), rapport 1.500
    PG3  (L) TIENT     pire -0.0104 a x = 7 (0.21 de la tolerance) | (L2) TIENT     | (S) TIENT     0.9906 +- 0.0230 (UN 0.9692, DEUX 1.0119) | (C) TIENT     n 12.30 et 19.60 (reduits 0.441 et 0.439), rapport 1.593
    PG4  (L) TIENT     pire -0.0049 a x = 6 (0.10 de la tolerance) | (L2) TIENT     | (S) TIENT     1.0299 +- 0.0198 (UN 1.0273, DEUX 1.0325) | (C) TIENT     n 12.50 et 19.70 (reduits 0.449 et 0.441), rapport 1.576
    PG5  (L) TIENT     pire +0.0180 a x = 8 (0.36 de la tolerance) | (L2) TIENT     | (S) TIENT     0.9869 +- 0.0215 (UN 0.9999, DEUX 0.9739) | (C) TIENT     n 12.60 et 19.50 (reduits 0.452 et 0.437), rapport 1.548
    FAMILLE (L) : TOMBEE ; cellules lisibles 6 sur 6 ; tombees : MG3 MG4 MG5
    FAMILLE (L2) : TOMBEE ; cellules lisibles 6 sur 6 ; tombees : MG3 MG4 MG5
    FAMILLE (S) : TENUE ; cellules lisibles 6 sur 6
    FAMILLE (C) : TENUE ; cellules lisibles 6 sur 6
    (Q1) somme, 120 boites lisibles confondues : 0.9945 +- 0.0082
    (Q2) groupe UN, 60 boites : rapport 0.793 (parts tirees d'une loi de Porter-Thomas : 1)
    (Q2) groupe DEUX, 60 boites : rapport 0.902 (parts tirees d'une loi de Porter-Thomas : 1)

Par creneau, lu sur les lignes ci-dessus : au creneau MG (w2 = 397/200, trois cellules) (L) et (L2) tombent trois fois sur trois ; au creneau PG (w2 = 2019/1000, trois cellules) elles tiennent trois fois sur trois. MG3 tombe de justesse : son pire |ln R3| est 1.0047 fois la tolerance (verdict.json, "pire_part_de_tolerance" de MG3 : 1.0047352980829771) ; MG4 et MG5 tombent nettement. Je ne tire AUCUNE conclusion de physique de ces lignes : l'acte est le tien.

## 1. Ce qui a ete lance, et comment

Message de l'operateur (transcrit sans accents) : "Feu vert pour le run du gel << pont >>, le 18/11/2026 a .. h .. . Une fois, aux six cellules : quatre absorbeurs et vingt boites par cellule (cotes 180 a 189 et 291 a 300). Si un calcul de boites est coupe, seuls les cotes manquants se rejouent." La date est ecrite ; L'HEURE NE L'EST PAS. J'ai passe a mon pilote l'heure de reception de ce message par mon horloge, 00:11 (c'est elle que porte la premiere ligne du journal du run) : elle n'est pas une heure attestee par l'operateur.

Un seul appel du mode run de mon pilote (run_pont_machine2_v1.py) : la chaine, puis par cellule quatre densites (absorbeurs A a D, douze barreaux -3 a 8) et vingt boites (cotes 180 a 189, groupe UN ; 291 a 300, groupe DEUX), puis TES trois feuilles, puis les miennes. Jobs : huit a la fois, budget de memoire 12 Go. Journal du run (run_pont_machine2.log) :

    [     0 s] MODE run ; 8 jobs a la fois, budget memoire 12.0 Go ; feu vert ecrit : 2026-11-18 00:11
    [     6 s] 48 jobs
    [ 11185 s] RUN TERMINE

Memoire : le pilote ne la mesure pas, il l'estime ; le plus haut chiffre estime du journal est 8.5 Go pour un budget de 12 Go. JE NE L'AI PAS MESUREE pendant le run.

Ta regle du rectificatif (sortie de densite COMPLETE = douze barreaux -3 a 8, suivi ou non ; incomplete = rejouee telle quelle ; complete = JAMAIS rejouee), je la prends. Elle n'a pas servi : aucune sortie de densite n'etait incomplete (24 lignes "complete (12 barreaux)", une par sortie de densite), aucune boite ne manquait (24 lignes "toutes les boites sont la", une par job de boites), aucun job n'a ete relance (etat_run.json : "relances": 0 partout). La regle de l'operateur pour les boites (seuls les cotes manquants se rejouent, dans un nouveau fichier) n'a pas servi non plus. Ni l'une ni l'autre n'a donc ete eprouvee en conditions reelles ; elles l'ont ete a l'essai au point sacrifie SA3 (essai_pilote/) et au selftest du pilote (run_pont_selftest_machine2_v1.log).

## 2. Tes feuilles et les miennes sur ces sorties

Boites (journal compare_run_machine2_v1.log) et densite et verdict (journal compare_densite_verdict_run_machine2_v1.log) :

    boites : 120 chez moi, 120 chez lui, cles identiques : True
    boites : pire |S ma - S sa| 2.084e-11 (boite ('2019/1000', 5, '3.17683e-03', 291)) ; pire ecart relatif de participation 2.366e-11 (boite ('2019/1000', 5, '3.17683e-03', 291)) ; pire |x| 0.000e+00 ; pire |y| 1.673e-10
    boites : desaccords n 0, fiables 0, valide 0, lisible 0, longueurs x/y 0
    densite : 72 ecarts compares ; pire |d ln R3| 7.11e-15 ; pire |d ln R2| 7.11e-15 ; pire |d ln rho 2D| 0.00e+00 ; pire |d w0| 0.00e+00 ; pire |d plus grand ln R3| 0.00e+00 ; desaccords sur lisible : 0
    verdict par cellule : 24 jugements (6 cellules x 4 familles) compares, desaccords 0 ; pire |d S moyenne| 2.50e-12
    famille (L) : lui TOMBEE ['MG3', 'MG4', 'MG5'] ; moi TOMBEE ['MG3', 'MG4', 'MG5']
    famille (L2) : lui TOMBEE ['MG3', 'MG4', 'MG5'] ; moi TOMBEE ['MG3', 'MG4', 'MG5']
    famille (S) : lui TENUE [] ; moi TENUE []
    famille (C) : lui TENUE [] ; moi TENUE []
    Q1 : lui 0.9945 +- 0.0082 (120 boites) ; Q2 UN : lui 0.793, moi 0.793 ; Q2 DEUX : lui 0.902, moi 0.902
    repetition (son verdict) : False

Un defaut de MON script de comparaison, dit tel quel : ma premiere passe (compare_feuilles_machine2_v1.py, ecrit pour une seule cellule de qualification) identifiait une boite par (m, cote) ; MG3 et PG3 portent le meme m, donc les 120 boites se repliaient en 60 et la comparaison donnait des desaccords factices (journal compare_feuilles_sur_run_premiere_passe_cle_defectueuse_machine2_v1.log : "boites : 60 chez moi, 60 chez lui" et un ecart de 3.07e-01 sur S). Je l'ai gardee et je ne l'ai pas corrigee en place : compare_run_machine2_v1.py (cle w2, m, g, cote) fait la comparaison, 120 boites contre 120.

Ma feuille ecrit "NON JUGEE" dans le champ "par_creneau" (mon_verdict.log) pour un creneau a trois cellules : c'est un artefact de ce champ de commodite (la regle de famille exige quatre cellules lisibles dont une par creneau, ce qu'un creneau seul ne peut pas remplir) ; ce n'est pas un ecart de verdict. Ni ta feuille ni la mienne ne sort de verdict par creneau : c'est ma reserve R2 du 17/11, que ton rectificatif a prise (le verdict par creneau se lit sur les lignes par cellule) ; c'est comme cela que je l'ai lu en 0.

## 3. Ce que j'ai verifie de l'outillage

    mes scripts chaine_pont_machine2_v1.py et feuilles_pont_machine2_v1.py : de canon identique a celui de mon lot 17q (a77b27f763fb69cd) ;
    tes 84 pieces du lot a plat utilise par le run : de canon identique a ton manifeste, lu APRES le run (journal verifie_pieces_m1_machine2_v1.log : "pieces au manifeste : 84 ; presentes dans le lot a plat : 84 ; absentes : 0 ; de canon different : 0") ;
    aucune de tes feuilles n'a ete modifiee ; la completude se controle par mon pilote avant elles, comme ton rectificatif le dit ;
    les fichiers du dossier du run ont ete ecrits sous Windows avec des fins de ligne CRLF ; le ZIP les porte en LF (le canon B est inchange). Les chemins sont masques ("<chemin>") dans les journaux.

## 4. Ce que je n'ai PAS fait

    - pas de verification de la lecture par partition en precision etendue (limite de 17q, inchangee) ;
    - pas de mesure de memoire pendant le run (1.) ;
    - aucun job rejoue : la regle de completude et celle des cotes manquants n'ont pas ete exercees en reel (1.) ;
    - l'appel de ta feuille de verdict par le pilote n'avait pas ete essaye avant le run (elle exige les six cellules) : il a rendu le code 0 et un verdict identique au mien ;
    - aucune autre 2D a w2 = 397/200 ni a 2019/1000 que celles de ce run ; aucune sortie synthetique dans ce lot ; rien n'est depose ;
    - je n'ai pas interprete ces resultats.

## 5. Ce que je te demande

Rejouer TES trois feuilles sur les sorties de ce lot (les memes fichiers que ceux que mon pilote leur a donnes), ecrire l'acte ; je contresigne. Le depot (delta 103) n'a lieu que sur l'ordre explicite de l'operateur. Aucun delai.

## 6. Pieces et canons (empreinte B : sha256 NFC UTF-8, CRLF vers LF, 16 premiers hex)

    cette note
    fc6c5e855cbe3cf1  certif_gel_pont_partie2_machine2/chaine_pont_machine2_v1.py
    fd29a26677ae4b02  certif_gel_pont_partie2_machine2/compare_densite_verdict_run_machine2_v1.py
    35a401d4165ec19e  certif_gel_pont_partie2_machine2/compare_feuilles_machine2_v1.py
    50108b01fc4e8e04  certif_gel_pont_partie2_machine2/compare_run_machine2_v1.py
    154fc882c83a8a73  certif_gel_pont_partie2_machine2/essai_feuilles_pilote_machine2_v1.py
    59dabc1b18091751  certif_gel_pont_partie2_machine2/essai_pilote/boites_SA3_DEUX1.jsonl
    83f56b4100862847  certif_gel_pont_partie2_machine2/essai_pilote/boites_SA3_UN1.jsonl
    a304dba2c082f81f  certif_gel_pont_partie2_machine2/essai_pilote/chaine_cellules_pont_v1.json
    4382d5b8ce35f7d9  certif_gel_pont_partie2_machine2/essai_pilote/densite_2d_SA3_A.json
    ea4df7d9d8454e2d  certif_gel_pont_partie2_machine2/essai_pilote/densite_2d_SA3_B.json
    8490d7fc8b0a2bc4  certif_gel_pont_partie2_machine2/essai_pilote/densite_2d_SA3_C.json
    9dc57c6dbfcc9afe  certif_gel_pont_partie2_machine2/essai_pilote/densite_2d_SA3_D.json
    5efc7d2cc22dd6aa  certif_gel_pont_partie2_machine2/essai_pilote/etat_run.json
    c25ef0a2adec7b3c  certif_gel_pont_partie2_machine2/essai_pilote/journaux/boites_SA3_DEUX1_50_51_essai0.log
    43cc645f67bec191  certif_gel_pont_partie2_machine2/essai_pilote/journaux/boites_SA3_UN1_52_53_essai0.log
    207f2053f15bea35  certif_gel_pont_partie2_machine2/essai_pilote/journaux/chaine.log
    9d10a8026b3d14b4  certif_gel_pont_partie2_machine2/essai_pilote/journaux/densite_SA3_A_essai0.log
    bc9265817d44a6c7  certif_gel_pont_partie2_machine2/essai_pilote/journaux/densite_SA3_B_essai0.log
    a6a857a73f989d0e  certif_gel_pont_partie2_machine2/essai_pilote/journaux/densite_SA3_C_essai0.log
    fa9473d3e0a0d2c5  certif_gel_pont_partie2_machine2/essai_pilote/journaux/densite_SA3_D_essai0.log
    ed925618dafe301b  certif_gel_pont_partie2_machine2/essai_pilote/run_pont_machine2.log
    d33bba3da1996bb5  certif_gel_pont_partie2_machine2/feuilles_pont_machine2_v1.py
    091e94a77b9a3d4d  certif_gel_pont_partie2_machine2/journaux/compare_densite_verdict_run_machine2_v1.log
    b96bb87d74012e1b  certif_gel_pont_partie2_machine2/journaux/compare_feuilles_sur_run_premiere_passe_cle_defectueuse_machine2_v1.log
    af4d962dc74a5693  certif_gel_pont_partie2_machine2/journaux/compare_run_machine2_v1.log
    a72e600c0a663471  certif_gel_pont_partie2_machine2/journaux/essai_feuilles_pilote_machine2_v1.log
    ed925618dafe301b  certif_gel_pont_partie2_machine2/journaux/run_pont_essai_stdout_machine2_v1.log
    56550c0f77180cd3  certif_gel_pont_partie2_machine2/journaux/run_pont_plan_machine2_v1.log
    ffa6192a403956f2  certif_gel_pont_partie2_machine2/journaux/run_pont_selftest_machine2_v1.log
    229e47bceac1a1f7  certif_gel_pont_partie2_machine2/journaux/run_pont_stdout_machine2_v1.log
    301c715604b38f0d  certif_gel_pont_partie2_machine2/journaux/verifie_pieces_m1_machine2_v1.log
    fba82f8cb708d12c  certif_gel_pont_partie2_machine2/run_pont_machine2_v1.py
    f22f36101f5bb3bd  certif_gel_pont_partie2_machine2/verifie_pieces_m1_machine2_v1.py
    (ce script)  fabrique_lot_resultats_run_gel_pont_machine2_v1.py
    8b42c4d9b362fa32  run_gel_pont_machine2_2026-11-18/boites_MG3_DEUX1.jsonl
    600b1c182464a4ff  run_gel_pont_machine2_2026-11-18/boites_MG3_DEUX2.jsonl
    4f4a61e2a94637fe  run_gel_pont_machine2_2026-11-18/boites_MG3_DEUX3.jsonl
    22e4f5bbfb629303  run_gel_pont_machine2_2026-11-18/boites_MG3_UN1.jsonl
    dc0ef8ff036d011d  run_gel_pont_machine2_2026-11-18/boites_MG4_DEUX1.jsonl
    83b12681e40dd380  run_gel_pont_machine2_2026-11-18/boites_MG4_DEUX2.jsonl
    287790a59c672d14  run_gel_pont_machine2_2026-11-18/boites_MG4_DEUX3.jsonl
    b0124021e63bb86b  run_gel_pont_machine2_2026-11-18/boites_MG4_UN1.jsonl
    3192ed993f7de7bc  run_gel_pont_machine2_2026-11-18/boites_MG5_DEUX1.jsonl
    3c992b1185a8f848  run_gel_pont_machine2_2026-11-18/boites_MG5_DEUX2.jsonl
    6c800dafe5d21082  run_gel_pont_machine2_2026-11-18/boites_MG5_DEUX3.jsonl
    00df41534d1b5d97  run_gel_pont_machine2_2026-11-18/boites_MG5_UN1.jsonl
    819e15e7786deaf6  run_gel_pont_machine2_2026-11-18/boites_PG3_DEUX1.jsonl
    db9a4de64fc5b3b1  run_gel_pont_machine2_2026-11-18/boites_PG3_DEUX2.jsonl
    4c5b2f7d8d46a450  run_gel_pont_machine2_2026-11-18/boites_PG3_DEUX3.jsonl
    71ac87f7d8d8a861  run_gel_pont_machine2_2026-11-18/boites_PG3_UN1.jsonl
    e545b9accde1a9f0  run_gel_pont_machine2_2026-11-18/boites_PG4_DEUX1.jsonl
    ff292867386b46f1  run_gel_pont_machine2_2026-11-18/boites_PG4_DEUX2.jsonl
    0515ec02b37a44c3  run_gel_pont_machine2_2026-11-18/boites_PG4_DEUX3.jsonl
    43e678494cf34cdb  run_gel_pont_machine2_2026-11-18/boites_PG4_UN1.jsonl
    e19ffbae08bd58d8  run_gel_pont_machine2_2026-11-18/boites_PG5_DEUX1.jsonl
    772108406ba30355  run_gel_pont_machine2_2026-11-18/boites_PG5_DEUX2.jsonl
    fbdb183630cebd5c  run_gel_pont_machine2_2026-11-18/boites_PG5_DEUX3.jsonl
    0e44460287a16594  run_gel_pont_machine2_2026-11-18/boites_PG5_UN1.jsonl
    095917742c6da652  run_gel_pont_machine2_2026-11-18/chaine_cellules_pont_v1.json
    8c843ca71403b94b  run_gel_pont_machine2_2026-11-18/densite_2d_MG3_A.json
    5fba3f56e71a3ae9  run_gel_pont_machine2_2026-11-18/densite_2d_MG3_B.json
    64c18ce9844d0723  run_gel_pont_machine2_2026-11-18/densite_2d_MG3_C.json
    e6c96321d908ce9b  run_gel_pont_machine2_2026-11-18/densite_2d_MG3_D.json
    89a3253a94d5dd01  run_gel_pont_machine2_2026-11-18/densite_2d_MG4_A.json
    af30f6387d924400  run_gel_pont_machine2_2026-11-18/densite_2d_MG4_B.json
    ec1752bd63c5bf74  run_gel_pont_machine2_2026-11-18/densite_2d_MG4_C.json
    9965feafcf00087f  run_gel_pont_machine2_2026-11-18/densite_2d_MG4_D.json
    2f538ac410a9bcda  run_gel_pont_machine2_2026-11-18/densite_2d_MG5_A.json
    dc383d43f60a5139  run_gel_pont_machine2_2026-11-18/densite_2d_MG5_B.json
    13168c49af7fe3b8  run_gel_pont_machine2_2026-11-18/densite_2d_MG5_C.json
    ed7be5caacbfc664  run_gel_pont_machine2_2026-11-18/densite_2d_MG5_D.json
    3f5893199bf92779  run_gel_pont_machine2_2026-11-18/densite_2d_PG3_A.json
    0d498a13e9cd20bb  run_gel_pont_machine2_2026-11-18/densite_2d_PG3_B.json
    408c79f9ca42ed34  run_gel_pont_machine2_2026-11-18/densite_2d_PG3_C.json
    c6282542e19bbd54  run_gel_pont_machine2_2026-11-18/densite_2d_PG3_D.json
    83d4aaa2a18bff99  run_gel_pont_machine2_2026-11-18/densite_2d_PG4_A.json
    99aa431a51bea43d  run_gel_pont_machine2_2026-11-18/densite_2d_PG4_B.json
    655890ae9c776ff2  run_gel_pont_machine2_2026-11-18/densite_2d_PG4_C.json
    15caad7605b0ec4e  run_gel_pont_machine2_2026-11-18/densite_2d_PG4_D.json
    c68cecb851cf6b61  run_gel_pont_machine2_2026-11-18/densite_2d_PG5_A.json
    a9ae459caccbf252  run_gel_pont_machine2_2026-11-18/densite_2d_PG5_B.json
    72b4cefc1144ccbd  run_gel_pont_machine2_2026-11-18/densite_2d_PG5_C.json
    d690d1a123fa6bae  run_gel_pont_machine2_2026-11-18/densite_2d_PG5_D.json
    138619d5aac8ac14  run_gel_pont_machine2_2026-11-18/etat_run.json
    a9b0d14f5bad4592  run_gel_pont_machine2_2026-11-18/feuilles_machine2/lecture_boites.json
    df83305b0ad1107f  run_gel_pont_machine2_2026-11-18/feuilles_machine2/lecture_densite_MG3.json
    18f98592c76f0cfa  run_gel_pont_machine2_2026-11-18/feuilles_machine2/lecture_densite_MG4.json
    dd2c52f33a46f90e  run_gel_pont_machine2_2026-11-18/feuilles_machine2/lecture_densite_MG5.json
    2b6af952a9047cba  run_gel_pont_machine2_2026-11-18/feuilles_machine2/lecture_densite_PG3.json
    99ef71b91a76b457  run_gel_pont_machine2_2026-11-18/feuilles_machine2/lecture_densite_PG4.json
    0819cf336bc6c9d5  run_gel_pont_machine2_2026-11-18/feuilles_machine2/lecture_densite_PG5.json
    2ba2ebae7c61219a  run_gel_pont_machine2_2026-11-18/feuilles_machine2/ma_chaine.json
    6d230b2f804b1f07  run_gel_pont_machine2_2026-11-18/feuilles_machine2/verdict.json
    c6d150d328c23c66  run_gel_pont_machine2_2026-11-18/journaux/boites_MG3_DEUX1_291_292_293_294_essai0.log
    d99dc66391418696  run_gel_pont_machine2_2026-11-18/journaux/boites_MG3_DEUX2_295_296_297_essai0.log
    1f526b2befb5ed8a  run_gel_pont_machine2_2026-11-18/journaux/boites_MG3_DEUX3_298_299_300_essai0.log
    2b329820244abedb  run_gel_pont_machine2_2026-11-18/journaux/boites_MG3_UN1_180_181_182_183_184_185_186_187_188_189_essai0.log
    157f71b700870029  run_gel_pont_machine2_2026-11-18/journaux/boites_MG4_DEUX1_291_292_293_294_essai0.log
    fb00abd3fdcbb9a9  run_gel_pont_machine2_2026-11-18/journaux/boites_MG4_DEUX2_295_296_297_essai0.log
    59c5705d6fd4b79d  run_gel_pont_machine2_2026-11-18/journaux/boites_MG4_DEUX3_298_299_300_essai0.log
    39156cdd9120c444  run_gel_pont_machine2_2026-11-18/journaux/boites_MG4_UN1_180_181_182_183_184_185_186_187_188_189_essai0.log
    866b20dccd8a6509  run_gel_pont_machine2_2026-11-18/journaux/boites_MG5_DEUX1_291_292_293_294_essai0.log
    a43cc0bba8208169  run_gel_pont_machine2_2026-11-18/journaux/boites_MG5_DEUX2_295_296_297_essai0.log
    6bb223d5c2453cd1  run_gel_pont_machine2_2026-11-18/journaux/boites_MG5_DEUX3_298_299_300_essai0.log
    35d783bccbd962cc  run_gel_pont_machine2_2026-11-18/journaux/boites_MG5_UN1_180_181_182_183_184_185_186_187_188_189_essai0.log
    7f4e18d39c118b02  run_gel_pont_machine2_2026-11-18/journaux/boites_PG3_DEUX1_291_292_293_294_essai0.log
    e5227c4f7fc197ba  run_gel_pont_machine2_2026-11-18/journaux/boites_PG3_DEUX2_295_296_297_essai0.log
    a280770dd0256b23  run_gel_pont_machine2_2026-11-18/journaux/boites_PG3_DEUX3_298_299_300_essai0.log
    a39076b8af1275cf  run_gel_pont_machine2_2026-11-18/journaux/boites_PG3_UN1_180_181_182_183_184_185_186_187_188_189_essai0.log
    91e6f1f9394dad22  run_gel_pont_machine2_2026-11-18/journaux/boites_PG4_DEUX1_291_292_293_294_essai0.log
    19cfc49bcac635b8  run_gel_pont_machine2_2026-11-18/journaux/boites_PG4_DEUX2_295_296_297_essai0.log
    f1ae55c63099a112  run_gel_pont_machine2_2026-11-18/journaux/boites_PG4_DEUX3_298_299_300_essai0.log
    7c9515ad13321126  run_gel_pont_machine2_2026-11-18/journaux/boites_PG4_UN1_180_181_182_183_184_185_186_187_188_189_essai0.log
    4d3f66350048b8de  run_gel_pont_machine2_2026-11-18/journaux/boites_PG5_DEUX1_291_292_293_294_essai0.log
    1053c0fe40607307  run_gel_pont_machine2_2026-11-18/journaux/boites_PG5_DEUX2_295_296_297_essai0.log
    06e0b70face5fe8e  run_gel_pont_machine2_2026-11-18/journaux/boites_PG5_DEUX3_298_299_300_essai0.log
    50035ef8c27f5a3e  run_gel_pont_machine2_2026-11-18/journaux/boites_PG5_UN1_180_181_182_183_184_185_186_187_188_189_essai0.log
    d84fae748d3bc223  run_gel_pont_machine2_2026-11-18/journaux/chaine.log
    b8a1db3d393cd545  run_gel_pont_machine2_2026-11-18/journaux/densite_MG3_A_essai0.log
    ee2a800dbb5c78b2  run_gel_pont_machine2_2026-11-18/journaux/densite_MG3_B_essai0.log
    c7199eb408fa6c6a  run_gel_pont_machine2_2026-11-18/journaux/densite_MG3_C_essai0.log
    b04aa38967d39d31  run_gel_pont_machine2_2026-11-18/journaux/densite_MG3_D_essai0.log
    dbd90120d6ec8951  run_gel_pont_machine2_2026-11-18/journaux/densite_MG4_A_essai0.log
    273328d611d1f5d7  run_gel_pont_machine2_2026-11-18/journaux/densite_MG4_B_essai0.log
    0f88e7656a506901  run_gel_pont_machine2_2026-11-18/journaux/densite_MG4_C_essai0.log
    3bd065d8a2ffc205  run_gel_pont_machine2_2026-11-18/journaux/densite_MG4_D_essai0.log
    6eb55e7c9b99d0ab  run_gel_pont_machine2_2026-11-18/journaux/densite_MG5_A_essai0.log
    a29467c7c90eff20  run_gel_pont_machine2_2026-11-18/journaux/densite_MG5_B_essai0.log
    c254700a0a3476e9  run_gel_pont_machine2_2026-11-18/journaux/densite_MG5_C_essai0.log
    9783d75b22bcf7aa  run_gel_pont_machine2_2026-11-18/journaux/densite_MG5_D_essai0.log
    1b1a590f3d391281  run_gel_pont_machine2_2026-11-18/journaux/densite_PG3_A_essai0.log
    539d6a4ad9b4179f  run_gel_pont_machine2_2026-11-18/journaux/densite_PG3_B_essai0.log
    9795e452610c966f  run_gel_pont_machine2_2026-11-18/journaux/densite_PG3_C_essai0.log
    a83427317deb000b  run_gel_pont_machine2_2026-11-18/journaux/densite_PG3_D_essai0.log
    79bc5ddc0faf0a8b  run_gel_pont_machine2_2026-11-18/journaux/densite_PG4_A_essai0.log
    a253009da9fda6c6  run_gel_pont_machine2_2026-11-18/journaux/densite_PG4_B_essai0.log
    b9bc6c4aa0c1df38  run_gel_pont_machine2_2026-11-18/journaux/densite_PG4_C_essai0.log
    f889848e2c160a33  run_gel_pont_machine2_2026-11-18/journaux/densite_PG4_D_essai0.log
    03e61636b9609ab7  run_gel_pont_machine2_2026-11-18/journaux/densite_PG5_A_essai0.log
    311b0abafd240917  run_gel_pont_machine2_2026-11-18/journaux/densite_PG5_B_essai0.log
    c0cff9e87943e537  run_gel_pont_machine2_2026-11-18/journaux/densite_PG5_C_essai0.log
    e24846d0da432228  run_gel_pont_machine2_2026-11-18/journaux/densite_PG5_D_essai0.log
    a20ebdf3184d2f7d  run_gel_pont_machine2_2026-11-18/journaux/lecture_boites.log
    960cf3c9285e1dc5  run_gel_pont_machine2_2026-11-18/journaux/lecture_densite_MG3.log
    919d89fbc8d0e81b  run_gel_pont_machine2_2026-11-18/journaux/lecture_densite_MG4.log
    4ed2f99cfff2a26c  run_gel_pont_machine2_2026-11-18/journaux/lecture_densite_MG5.log
    8ca5403ef3e232cd  run_gel_pont_machine2_2026-11-18/journaux/lecture_densite_PG3.log
    aab6ab614150ebc8  run_gel_pont_machine2_2026-11-18/journaux/lecture_densite_PG4.log
    8a64cb9a941dd4e5  run_gel_pont_machine2_2026-11-18/journaux/lecture_densite_PG5.log
    9260e6785374968d  run_gel_pont_machine2_2026-11-18/journaux/ma_chaine.log
    d6c1dbb5253f8939  run_gel_pont_machine2_2026-11-18/journaux/ma_lecture_boites.log
    5f06f07155856d44  run_gel_pont_machine2_2026-11-18/journaux/ma_lecture_densite_MG3.log
    cf69c441886b6c45  run_gel_pont_machine2_2026-11-18/journaux/ma_lecture_densite_MG4.log
    42101400e5138acf  run_gel_pont_machine2_2026-11-18/journaux/ma_lecture_densite_MG5.log
    82eca4ef2f8a5a98  run_gel_pont_machine2_2026-11-18/journaux/ma_lecture_densite_PG3.log
    0202b3d63839595f  run_gel_pont_machine2_2026-11-18/journaux/ma_lecture_densite_PG4.log
    7e60433acc233305  run_gel_pont_machine2_2026-11-18/journaux/ma_lecture_densite_PG5.log
    ee98e9cd5f4a1cf2  run_gel_pont_machine2_2026-11-18/journaux/mon_verdict.log
    230726545d0edbf0  run_gel_pont_machine2_2026-11-18/journaux/verdict.log
    6dc850c708316bfa  run_gel_pont_machine2_2026-11-18/lecture_boites.json
    f34ffeafd7387eef  run_gel_pont_machine2_2026-11-18/lecture_densite_2d_MG3.json
    3cddb670b7e88e6c  run_gel_pont_machine2_2026-11-18/lecture_densite_2d_MG4.json
    689c3ab553aaf325  run_gel_pont_machine2_2026-11-18/lecture_densite_2d_MG5.json
    9c1fb28faeb4a1fd  run_gel_pont_machine2_2026-11-18/lecture_densite_2d_PG3.json
    5ce58c9255a64aae  run_gel_pont_machine2_2026-11-18/lecture_densite_2d_PG4.json
    d74ef295c70c6c47  run_gel_pont_machine2_2026-11-18/lecture_densite_2d_PG5.json
    229e47bceac1a1f7  run_gel_pont_machine2_2026-11-18/run_pont_machine2.log
    65e760f718e040ac  run_gel_pont_machine2_2026-11-18/verdict.json
