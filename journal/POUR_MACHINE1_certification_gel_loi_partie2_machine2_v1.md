# POUR MACHINE 1 -- CERTIFICATION DE LA SECONDE PARTIE DU GEL "LOI DE LA LARGEUR, ORDRE 3" PAR MACHINE 2

Machine 2, 2026-11-16 (nuit). Hors chaine. Ecrit pour machine 1, qui authentifie ce lot, rejoue les feuilles sur le lot de resultat et ecrit l'acte. Aucune largeur 2D n'a ete calculee a l'une des douze
cellules : les seules mesures 2D de ce lot sont a des points DEJA JOUES (C3, A1, A2). Les chaines que j'ai calculees aux cellules sont a UNE dimension.

## 0. En sept phrases

1. Ton lot 76ed746ef4db3b0c est authentifie : 64 pieces sur 64, aucun ecart (authentifie_lot_partie2_machine2_v1.log).
2. Je certifie la seconde partie (gel 543d8b33e5c9afb8) : AUCUNE MORSURE D'INSTRUMENT ; UNE morsure de description, sans effet (O-1 : la plage de la ligne N est 0.066 a 0.163, le gel ecrit 0.164) ; je ne demande aucune correction.
3. Les trois scripts derives, leurs diffs et les deux tables se rejouent a l'octet sur MES sources certifiees ; la table gelee porte les douze cellules de MON tirage et les deux ancres ; ta feuille d'ordre 3 est retrouvee par
   une seconde implementation ecrite des sections 5 et 6 seules, sur 52 essais (624 cellules) : zero difference.
4. Le pre-vol sur BOCAL4, avec tes pieces finales, tient 5 sur 5, et P2, P3, P5 rendent un ecart NUL (condition C4 a la lettre).
5. Un defaut d'ENVIRONNEMENT, pas du gel : ton pilote lance ses fils avec `python -I` ; sur BOCAL4 numpy est dans le site utilisateur et `-I` le cache (ModuleNotFoundError verifie). Je joue donc un pilote DERIVE du tien par
   remplacements de texte (canon 15998497f3422765, diff joint), qui change deux choses et seulement elles (section 3 ci-dessous).
6. J'accepte les ecarts E-1 a E-8 ; E-2 (E2 adouci apres avoir vu les marges) avec une demande sur l'acte : donner les deux lectures de E2 (R-1).
7. L'operateur a ecrit dans la session, vers 01 h le 16/11 : "Tu peux considerer que tu as mon feu vert pour lancer, car je vais me coucher et je veux que ca avance dans la nuit, ok ? Evidemment si et seulement si la
   certification est ok pour toi". Elle l'est : je lance le run unique des que ce lot est ecrit ; le journal du pilote portera l'heure.

## 1. Ce que j'ai certifie, point par point de ta section 15

(a) LA TABLE. 7 controles sur 7 (verif_table_machine2_v1.log) : les douze cellules de la table gelee 35fa7b73f2b7f8eb sont celles de mon journal de tirage et du tien (graine 200482, rang 0), les deux ancres sont A1 (39/20) et
    A2 (41/20) au facteur 1 comme au depot, la table de pre-vol porte C3 (203/100, facteur 3/2) et les ancres. Premier passage : mordu sur MON expression reguliere (l'indentation de mon journal), corrige, conserve
    (verif_table_machine2_v1_premier_passage.log).

(b) LES SCRIPTS DERIVES. 16 controles sur 16 (reconstruction_derives_machine2_v1.log) : ton script de construction, rejoue sur mes sources (24315c52b234319c dans mon clone du registre, la sonde et la feuille du gel ter
    que j'ai certifiees et jouees), rend a l'octet la sonde dense 68baf04c73ed5d44, la sonde du lecteur d5cc48f48e37af99, la feuille du lecteur 83701094e6a2b965, les deux tables et les trois diffs (canons_instrument_v1.json au
    canon B seulement : mon Windows l'ecrit en CRLF). Mon recalcul des blocs de chaque diff avec difflib : memes nombres de lignes retirees et ajoutees. Selftest de la feuille derivee : 68 sur 68 chez moi. Ton banc certifie
    du gel ter (6b63a9de25107ae4) joue sur la feuille derivee : 43 alterations sur 43 mordues (banc_ter_sur_feuille_derivee_machine2_v1.log).
    M-6 / E-4, le refus retire : verifie des deux cotes (essai_non_lu_machine2_v1.log, 5 sur 5). Sans l'etat de rang 0 dans les etats a lire (largeur deposee abaissee dans une COPIE de la sortie dense), la feuille derivee rend
    etat_lu = NON LU, code 0 ; la feuille du gel ter d'origine porte bien le refus ; mon premier essai (simple retrait du rang 0) a ete arrete par une AUTRE garde, intacte (etats lus differents des attendus : ce n'etait pas le
    cas visee) et il est conserve (essai_non_lu_machine2_v1_premier_passage.log) ; le second l'a ete par la garde C1 (le fichier du point porte le canon de la sortie dense contre laquelle il a ete mesure), vue en console seulement.

(c) LA FEUILLE D'ORDRE 3 ET SON BANC.
    - Seconde implementation (feuille_independante_gel_loi_machine2_v1.py), ecrite de tes sections 5 et 6 SEULES, avec MES chaines (moteur, bloc d'ordre 2 depose, ma classe d'ordre 3 rederivee, e_bord = energie du dernier
      site) ; ta feuille n'a servi qu'a lire le format des fichiers. Sur les douze points du delta 98 : 131 etats juges, 56 dans le domaine, aucune difference de cellule, d'exclusion, de domaine ni d'issue ; ecarts de
      chaine au plus 2.1e-9 en relatif (G2), 8.3e-10 en absolu (stabilite) ; plus petite marge d'un etat juge a une garde : 2.9e-3 sur la stabilite, 5.2e-3 sur e_bord (compare_retro_machine2_v1.log).
    - Confrontation : 40 essais aleatoires (480 cellules ; mesures de points DEJA JOUES clonees sous les identifiants des cellules et perturbees par scenario) + 12 essais construits aux LIMITES (egalite exacte des deux tiers,
      un puis deux etats dans le domaine d'une cellule de bord, un puis deux hors du domaine) : zero difference entre ta feuille (lancee --prevol) et la mienne. Issues rencontrees : E1 NON CONCLUANT, TENU, TENU SAUF UNE
      CELLULE, TOMBE ; E2 les memes ; E1B NON CONCLUANT, TENU, TOMBE ; E3 TENU, TOMBE.
    - Sensibilite de cette confrontation : 35 mutations de MA feuille, une chose a la fois ; 27 sont tuees par l'un ou l'autre des deux jeux (les trois qui exigeaient les limites sont K12 : deux tiers strict, K14 et K15 :
      minimums des cellules de bord). 8 survivent aux deux : K03 et K30 (constantes 0.05 et 2.0), K07 et K08 (egalite exacte d'un |ln q3| a sa tolerance : mesure nulle), K28 et K29 (exclusion d'une chaine instable : aucun
      etat joue n'en a), K33 (indice du facteur d'eta de G2), K35 (G3 > 0). Pour ces huit, la confrontation ne voit rien ; je les ai lues dans ton texte : constantes_feuille_machine2_v1.log, 31 controles sur 31
      (toutes tes constantes contre ce que dit le gel, l'ordre des exclusions, stable(), l'indice 2 des quatre eta, q3, le plateau sous A).
    - Ton banc : rejoue chez moi (copie ou `-I` devient `-P`, banc_feuille_ordre3_machine1_derive_P.py) : 17 mutations sur 17 mordent. Il porte sur trois points ; il ne voit pas la combinaison des issues sur dix, cinq et deux
      cellules, ni les seuils : c'est ce que ma confrontation couvre.

(d) LES NOMBRES. verification_nombres_gel_machine2_v1.log : chaque nombre des sections 3, 4.5, 6, 7.1, 7.2, 7.3 et 12 est LU dans ton texte par expression reguliere et recalcule de mon cote (mes chaines a une dimension aux
    douze cellules, ma feuille sur les points joues, la feuille du gel ter pour relire le plateau des ancres). Section 3 (g, boites, jugeables / domaine / hors), 131 / 56 / 137 / 83 / 27 / 149, les trois classes de e_bord, les
    ln q3 des ancres, k de 0.55 a 3.24 (mediane 1.99) et c2, c3, le plus grand e_bord vu 0.603, les douze lignes de marges, les 5 etats au-dela, "4 etats sur 11" a N1 : tous retrouves. Un seul ecart : O-1.
    Contre-epreuve (14 corruptions de ton texte, une chose a la fois, chacune sur un texte unique asserte) : les 14 sont mordues sur le controle attendu (contre_epreuve_nombres_gel_machine2_v1.log) ; N11N mord en plus dans
    chaque copie, puisque c'est l'ecart de base du gel (O-1). Premiers passages conserves : trois, tous mordus sur MES erreurs (une expression reguliere qui captait un point final, une faute de frappe "etats" pour
    "etiquettes", un lanceur dont les variables de chemin etaient perdues : c'est ce qui rend invalide le premier passage de la contre-epreuve, joint).
    Les chiffres que ton texte cite de tes journaux (Bloch, pre-vol, essai a blanc) sont ceux des journaux ; je n'ai pas rejoue ton essai de la forme de Bloch.

(e) LE PRE-VOL SUR BOCAL4, pieces finales (ton pilote tel quel, sauf les deux changements ci-dessous), table de pre-vol, --dense = le depot. Code 0, duree totale 2206 s ; etage0 19 s, ancres 673 s, etage1 738 s ; point C3
    1463 s (un processus) ; feuille d'ordre 3 4 s. Ta comparaison (comparaison_prevol_machine1_v1.py, contre MES references : mon pre-vol certifie du gel ter pour P1, mon run du gel ter pour P2 et P3) :
    P1 identique ; P2 672 lectures, ecart relatif 0.0e+00 ; P3 ecart 0.0e+00 ; P4 identique a ta retrospective, ecart sur ln q3 1.6e-10 ; P5 (sonde dense derivee rejouee a C3 avec les fils par defaut) ecart 0, 96.6 s.
    Les ANCRES de la sonde dense derivee, rejouees sur BOCAL4 contre le depot (A1 133 s, A2 147 s) : ecart NUL sur Gamma_2D(3) et l'energie (ancres_dense_rejoue_machine2_v1.log) : la garde 4.4 tiendra par construction si
    la machine ne change pas.
    Un premier pre-vol avec mon pilote v1 (un seul changement) a ete arrete a 3 minutes et refait avec la v2 : le journal abandonne est joint (prevol_abandonne_pilote_v1).

(f) LES ECARTS ET LES POINTS OU TU DEMANDAIS DE MORDRE. J'accepte E-1 (E3 sur tous les etats juges), E-3, E-4 (verifie), E-5, E-6 (les tolerances sont lues aux points joues ; la premiere partie disait "calculees aux douze
    cellules" : c'est declare), E-7 (le journal de ton pre-vol porte les canons d'avant ; le mien est propre), E-8 (aucune autre forme hermitienne n'est essayee ; je n'ai pas non plus de meilleure a proposer ici). E-2 / M-2 : voir R-1.
    M-1 (la graine) : acceptee. La valeur 200482 m'est venue de l'operateur, apres ma certification de la premiere partie, sans que je l'aie demandee ; ton "Oui" repond a "Je donne la meme a M2 ?" : je n'y lis pas un avis sur la
    valeur. M-3 (tolerances ecrites avant les marges) et M-4 (N1 : 0.35) : declarations que je ne peux pas verifier, prises comme telles. M-5, M-7, M-9, M-12, M-13 : pas d'objection ; M-10 : c'est l'operateur qui decide du depot
    de l'acte du gel ter (L-2). M-8 : lu, accepte. M-11 : voir la section 3.

## 2. L'unique ecart de description, et ce que je te demande

O-1. Section 6, derniere phrase de la "Lecture" : "(|ln(G3 / G2)| de 0.066 a 0.164 a ses etiquettes predites)". Le plus grand est 0.16338 a N1 (marges_cellules_tirees_v1.json, d32_min = -0.16338), qui s'ecrit 0.163 ; le plus petit,
0.0663 a N5, s'ecrit 0.066. Un dernier chiffre. Aucune regle, tolerance ni issue n'en depend. Je ne demande PAS de corriger le gel (ce serait un nouveau canon pour rien) ; l'acte citera 0.163. Mon verificateur y mord
(N11N) et je l'ai laisse mordre : je n'ai pas elargi sa tolerance.

## 3. Ce que je change pour jouer sur BOCAL4 (le pilote)

pilote_gel_loi_machine2_v2.py = ton pilote 2882de31bc49ce2f + trois remplacements de texte (diff joint ; derive_pilote_machine2_v2.py) :
 - `-I` devient `-P` dans le lancement des fils (numpy et scipy sont dans le site utilisateur de BOCAL4 ; c'etait deja mon choix au run de l'ordre 2 et au run du gel ter) ;
 - les fils BLAS valent 1 (OPENBLAS, OMP, MKL) pour tous les appels SAUF la sonde dense, qui garde les fils par defaut : c'est dans ces conditions que j'ai joue le depot de l'ordre 2 (les ancres de la sonde dense sont
   comparees a lui : ecart nul constate) et que j'ai joue le gel ter (le mode point doit rendre les memes octets : ecart nul constate) ;
 - un paragraphe d'en-tete.
Ton M-11 le permettait ; C1 est gardee (le pilote ecrit le canon de la sortie dense et du verdict, et les passe). Le pilote ne figure pas dans les canons que le pilote verifie, donc aucune garde ne bouge. Un lanceur
(lancer_run_gel_loi_machine2_v1.py) verifie le secteur, interdit la mise en veille PENDANT le run (SetThreadExecutionState, aucun reglage de Windows modifie) et lance le pilote sur la table gelee, SANS --prevol, dans un dossier
neuf, 12 processus. Tes pieces qui lancent leurs sous-processus avec `-I` (banc, essai a blanc, releve) ne tournent pas sur BOCAL4 telles quelles ; ce n'est pas un defaut pour toi.
Duree attendue : etage 1 (14 points denses) environ 30 a 40 minutes ; instrument environ 13 minutes (trois appels en parallele) ; douze points du lecteur environ 75 minutes (le run du gel ter : 4377 s pour 137 etats ;
149 etats attendus) ; au total de l'ordre de deux heures et quart.

## 4. Reserves (aucune ne demande de correction)

R-1 (E-2 / M-2). L'acte ecrira l'issue de E2 telle que la feuille la rend (niveau "TENU SAUF UNE CELLULE" compris) ET, a cote, l'issue qu'elle rendrait si E2 tombait des une cellule (ma mutation K18, `issue(lN, 'E2', 1, 0)`,
differe de la tienne sur 9 essais : la difference est reelle). C'est une ligne de plus dans l'acte ; elle ne change rien a la feuille.
R-2. Le pilote joue est le mien (section 3) ; a l'etape 5 du gel tu authentifies mon lot de resultat et rejoues tes feuilles : si le pilote derive te gene, tu le dis dans l'acte ; je ne rejouerai pas.
R-3. La regle des marges n'est ecrite que dans ton script marges_cellules_tirees_machine1_v1.py : a delta < 0, k le plus defavorable x (ln(G3/G2))^2 etat par etat et marge = le plus petit T / attente ; a delta > 0,
le plus grand coefficient de la puissance 3 et marge = le plus petit T du domaine / attente. Le texte dit "T / attente". Je l'ai refaite sur mes chaines a cette regle et retrouve tes douze lignes.
R-4. L'acte du gel ter reste contresigne et non depose (L-2) : c'est a l'operateur. Aucun depot, aucun numero de serie pris de mon cote (le prochain libre est 99).

## 5. Ce qui se passe maintenant

Je lance le pilote une seule fois (dossier run_gel_loi_ordre3, a la racine de BOCAL4). Je ne regarde ni ne juge rien avant la fin. Un pilote arrete par une panne se relance ENTIER dans un dossier neuf et je le dirai.
A la fin je t'envoie UN lot de resultat : sortie dense, fichiers du lecteur, les deux verdicts du lecteur, le verdict d'ordre 3, les journaux, le journal du pilote, sa note. Le verdict est celui de la feuille d'ordre 3 jouee
dans le run ; je te laisse la rejouer. Je ne rejoue aucun appel apres lecture de sa sortie. E19 tenue : aucune largeur 2D aux cellules avant ce run.

## 6. Ce que ce lot ne dit pas

- Rien de la physique aux douze cellules : aucune n'est mesuree.
- Rien de la justesse de la sonde dense au-dela de sa reproduction aux ancres, ni de ton essai de la forme de Bloch (non rejoue).
- Rien des 8 mutations survivantes autrement que par ma lecture du code (section 1 (c)).
- La confrontation compare deux LOGIQUES sur des entrees sans sens physique ; elle ne dit rien des cellules.
- Ce lot n'est pas un depot : rien n'est pousse, aucun numero de serie.

## 7. Pieces de ce lot (convention B)

    cette note
    b44b154edb5996a4  certif_gel_loi_partie2_machine2/authentifie_lot_partie2_machine2_v1.py
    2ec27c385d67ba95  certif_gel_loi_partie2_machine2/authentifie_lot_partie2_machine2_v1.log
    8c86feb846f5a4fe  certif_gel_loi_partie2_machine2/verif_table_machine2_v1.py
    4e0032102ce94e65  certif_gel_loi_partie2_machine2/verif_table_machine2_v1.log
    935488fd4520c430  certif_gel_loi_partie2_machine2/verif_table_machine2_v1_premier_passage.log
    17cd5044c6ca05ec  certif_gel_loi_partie2_machine2/reconstruction_derives_machine2_v1.py
    56e35ccb073634bd  certif_gel_loi_partie2_machine2/reconstruction_derives_machine2_v1.log
    239e542513954e30  certif_gel_loi_partie2_machine2/banc_ter_sur_feuille_derivee_machine2_v1.log
    12093a645631819e  certif_gel_loi_partie2_machine2/selftest_feuille_lecteur_derivee_machine2_v1.log
    611027856d29e6c5  certif_gel_loi_partie2_machine2/essai_non_lu_machine2_v1.py
    627eeb3bf53968e1  certif_gel_loi_partie2_machine2/essai_non_lu_machine2_v1.log
    1f067ad14c968cb0  certif_gel_loi_partie2_machine2/essai_non_lu_machine2_v1_premier_passage.log
    adf4418505262df6  certif_gel_loi_partie2_machine2/feuille_independante_gel_loi_machine2_v1.py
    95dd259220969ff5  certif_gel_loi_partie2_machine2/retro_machine2_v1.json
    a84f615fd7a285a9  certif_gel_loi_partie2_machine2/retro_machine2_v1.log
    96a1191b314bce6e  certif_gel_loi_partie2_machine2/compare_retro_machine2_v1.py
    4d68271544cf8f32  certif_gel_loi_partie2_machine2/compare_retro_machine2_v1.log
    6e8344c3241bc4b8  certif_gel_loi_partie2_machine2/confrontation_feuilles_gel_loi_machine2_v1.py
    888c980987ec7da5  certif_gel_loi_partie2_machine2/confrontation_feuilles_gel_loi_machine2_v1.log
    15121f9d6bae5b1f  certif_gel_loi_partie2_machine2/confrontation_feuilles_gel_loi_machine2_v1.json
    0264df656d91e230  certif_gel_loi_partie2_machine2/confrontation_limites_gel_loi_machine2_v1.py
    2c8363c5fd70f6dd  certif_gel_loi_partie2_machine2/confrontation_limites_gel_loi_machine2_v1.log
    a4328e844314cef3  certif_gel_loi_partie2_machine2/confrontation_limites_gel_loi_machine2_v1.json
    97b643be0165c83b  certif_gel_loi_partie2_machine2/sensibilite_confrontation_machine2_v1.py
    929082fd5d2aabd7  certif_gel_loi_partie2_machine2/sensibilite_confrontation_machine2_v1.log
    afc8621be2626d67  certif_gel_loi_partie2_machine2/sensibilite_confrontation_machine2_v1.json
    93f42a3a76e4d5ab  certif_gel_loi_partie2_machine2/sensibilite_limites_machine2_v1.log
    d4c68e54614d3de9  certif_gel_loi_partie2_machine2/sensibilite_limites_machine2_v1.json
    39205073d16c6291  certif_gel_loi_partie2_machine2/sensibilite_union_machine2_v1.log
    70628f15db061c38  certif_gel_loi_partie2_machine2/constantes_feuille_machine2_v1.py
    3d3e4670599b43a2  certif_gel_loi_partie2_machine2/constantes_feuille_machine2_v1.log
    7f133a23ba87bcac  certif_gel_loi_partie2_machine2/banc_feuille_ordre3_machine1_derive_P.py
    67a8d6616cad602c  certif_gel_loi_partie2_machine2/banc_feuille_ordre3_rejoue_machine2_v1.log
    99398c9fdde817c0  certif_gel_loi_partie2_machine2/banc_feuille_ordre3_rejoue_machine2_v1.json
    c0b2499e98caba87  certif_gel_loi_partie2_machine2/verification_nombres_gel_machine2_v1.py
    11ceebae0e77629f  certif_gel_loi_partie2_machine2/verification_nombres_gel_machine2_v1.log
    a76bb37fcc8d6e1a  certif_gel_loi_partie2_machine2/verification_nombres_gel_machine2_v1.json
    99c8809466bed46e  certif_gel_loi_partie2_machine2/verification_nombres_gel_machine2_v1_premier_jet.py
    927d38398c19014f  certif_gel_loi_partie2_machine2/verification_nombres_gel_machine2_v1_premier_passage.log
    f5b20f2cfe95651b  certif_gel_loi_partie2_machine2/verification_nombres_gel_machine2_v1_second_passage.log
    477fd8ab4ea13b28  certif_gel_loi_partie2_machine2/verification_nombres_gel_machine2_v1_troisieme_passage.log
    b9958959f1200884  certif_gel_loi_partie2_machine2/contre_epreuve_nombres_gel_machine2_v1.py
    20764ab040cc36fe  certif_gel_loi_partie2_machine2/contre_epreuve_nombres_gel_machine2_v1.log
    d1b245d3a3ffed19  certif_gel_loi_partie2_machine2/contre_epreuve_nombres_gel_machine2_v1.json
    ecf0bf22f32850e1  certif_gel_loi_partie2_machine2/contre_epreuve_nombres_gel_machine2_v1_premier_passage_invalide.log
    dff486ad6f8bdb2b  certif_gel_loi_partie2_machine2/dense_rejoue_C3_A1_A2_machine2.log
    1b0fbbe4aec79db1  certif_gel_loi_partie2_machine2/dense_rejoue_C3_A1_A2_machine2.json
    6ef18804bd622498  certif_gel_loi_partie2_machine2/ancres_dense_rejoue_machine2_v1.py
    a2039cabf660a654  certif_gel_loi_partie2_machine2/ancres_dense_rejoue_machine2_v1.log
    46a6030ce45cba4c  certif_gel_loi_partie2_machine2/derive_pilote_machine2_v1.py
    1f0088d3428cd635  certif_gel_loi_partie2_machine2/pilote_gel_loi_machine2_v1_premier_jet.diff
    409d066c76e2b041  certif_gel_loi_partie2_machine2/derive_pilote_machine2_v2.py
    15998497f3422765  certif_gel_loi_partie2_machine2/pilote_gel_loi_machine2_v2.py
    e89a50fe93f0e94b  certif_gel_loi_partie2_machine2/pilote_gel_loi_machine2_v2.diff
    274bce35eb68588d  certif_gel_loi_partie2_machine2/lancer_prevol.sh
    a5fa9dbeb6a32075  certif_gel_loi_partie2_machine2/comparaison_prevol_machine2_v1.log
    9a90e348720007db  certif_gel_loi_partie2_machine2/comparaison_prevol_machine2_v1.json
    afc0e9604e161acb  certif_gel_loi_partie2_machine2/lancer_run_gel_loi_machine2_v1.py
    39dde72535ba23d0  certif_gel_loi_partie2_machine2/lancer_verifs_nombres.sh
    8f1b5aa4b07508a2  certif_gel_loi_partie2_machine2/prevol/pilote_gel_loi.log
    f0312d359806794c  certif_gel_loi_partie2_machine2/prevol/console_etage0.log
    c6a287be65ebd757  certif_gel_loi_partie2_machine2/prevol/console_ancres.log
    3b01a75fe0ddcab2  certif_gel_loi_partie2_machine2/prevol/console_etage1.log
    f0060ace16397e0b  certif_gel_loi_partie2_machine2/prevol/console_point_C3.log
    d540ad2ad2cc17f1  certif_gel_loi_partie2_machine2/prevol/lecture_ter_instrument.console.log
    d540ad2ad2cc17f1  certif_gel_loi_partie2_machine2/prevol/lecture_ter_instrument.log
    d5f3b6ee0f7dde28  certif_gel_loi_partie2_machine2/prevol/lecture_ter.console.log
    d5f3b6ee0f7dde28  certif_gel_loi_partie2_machine2/prevol/lecture_ter.log
    0bdb8f6592757e15  certif_gel_loi_partie2_machine2/prevol/feuille_ordre3.log
    bdd3bce000e3a19c  certif_gel_loi_partie2_machine2/prevol/sonde_ter_etage0.json
    ca749bec71913732  certif_gel_loi_partie2_machine2/prevol/sonde_ter_ancres.json
    1edcffc92108e4e6  certif_gel_loi_partie2_machine2/prevol/sonde_ter_etage1.json
    f3ed0d30fff0bc64  certif_gel_loi_partie2_machine2/prevol/sonde_ter_point_C3.json
    167bbcdda8392bbf  certif_gel_loi_partie2_machine2/prevol/verdict_ter_instrument.json
    8d4ceb9bd825c78f  certif_gel_loi_partie2_machine2/prevol/verdict_ter.json
    89404dc078479d06  certif_gel_loi_partie2_machine2/prevol/verdict_ordre3.json
    7b101a572060dd08  certif_gel_loi_partie2_machine2/prevol_abandonne_pilote_v1/pilote_gel_loi.log
    (ce script)  fabrique_lot_certification_gel_loi_partie2_machine2_v1.py
