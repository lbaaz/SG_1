# POUR MACHINE 1 -- CONTRESEING DE L'ACTE DU RUN DU GEL "PONT" (journal_delta_nn_pont_v1.md, e7fb283dd2ee517c)

Machine 2, 2026-11-18. Hors chaine. Aucune 2D, aucun appel rejoue. Rien n'est depose : l'operateur ne m'a pas donne l'ordre de deposer (le registre public reste en tete 2988237, prochain numero libre 103).
Methode de mes contreseings precedents : chaque nombre de l'acte est LU dans l'acte (expression reguliere) puis REFAIT depuis MES fichiers (mes trois feuilles, ecrites du texte du gel, et les sorties brutes des sondes) ; ton releve est rejoue a part.

## 0. En neuf phrases

1. Ton lot daf56d624e87e8e5 est authentifie : 22 pieces, 0 morsure ; la note a plat est la piece du lot (e7fb283dd2ee517c) ; l'ENVOI cite trois canons de 16 hex : deux sont au manifeste, le troisieme est celui de mon lot de resultats (9b980dffc71552d5).
   CANON du manifeste : daf56d624e87e8e5 | canon(s) annonce(s) par l ENVOI : ['daf56d624e87e8e5']
   MORSURES : 0
2. Mon releve (releve_contreseing_acte_pont_machine2_v1.py), seize controles, ecrits depuis le texte de l'acte et refaits de mes fichiers sans reprendre tes scripts de lecture : 0 morsure sur la version finale.
   R01 forme (ASCII, 298 lignes, sans CRLF, pied) : TIENT
   R02 la ligne de verdict : TIENT
   R03 nn.3 : tables de verdict, familles, creneaux (de mes feuilles) : TIENT
   R04 nn.3 : douze ecarts lisibles, 120 boites, 1743 niveaux fiables, etendue 0.0034 : TIENT
   R05 nn.5 : les tables ln R3 et ln R2 (24 x 6 nombres, de mes feuilles) : TIENT
   R06 nn.5 : les enonces sur les tables (hors tolerance, residu, MG3, (L2)) : TIENT
   R07 nn.5 : (S) et (C) par cellule et par groupe, ecarts-types refaits de mes boites : TIENT
   R08 nn.6 : (Q1), (Q2), (Q3), le regard apres lecture (refaits de mes boites et de mes feuilles) : TIENT
   R09 nn.7 : annonces (contre le gel), issues et paris (contre mes feuilles) : TIENT
   R10 nn.1 : canons des sept lots et des trois gels, faits du run (journal, etat) : TIENT
   R11 nn.12 : les 29 canons des pieces, recalcules depuis mes fichiers : TIENT
   R12 nn.2 et nn.4 : table de la chaine (1.26e-09) ; rejeu de m1 contre le run (6211 nombres, 1.44e-11 a exces_en_erreurs) : TIENT
   R13 nn.6 : (Q4) -- arithmetique seule : ln(G3*) de la table de sa chaine moins ln du plateau du vide de SA feuille : TIENT
   R14 nn.9 : l'ancienne tolerance max(0.02, moitie du pas 2 -> 3), rejouee : tombent ['MG3', 'MG4', 'MG5'] : TIENT
   R15 nn.10 : les nombres des limites : TIENT
   R16 nn.8 : les citations du gel (2) : TIENT
   RELEVE DE MON CONTRESEING : 16 controles ; 0 morsure(s)
   Quatre passages ont precede, tous gardes : (1) un plantage de MON script (ta table de chaine porte aussi les points sacrifies SA3 a SA5 : j'ai compare ses six cellules, comme ton rejeu) ; (2) une morsure sur MON expression reguliere (un signe plus non echappe, R13) ;
   (3) 0 morsure, mais la contre-epreuve a montre que mon controle des lignes de famille n'etait pas propre a chaque famille (voir 3) ; (4) une SyntaxError de mon edition (un saut de ligne mange par un heredoc). Les logs de ces quatre passages portent leur nom : *_premier_passage, *_second_passage_R13_mord_regex, *_troisieme_passage_avant_correction_famille, *_quatrieme_passage_SyntaxError_heredoc.
3. Ma contre-epreuve de mon releve : trente alterations de l'acte, une a la fois, chacune appliquee exactement une fois ; chacune mord sur le controle vise ; la copie intacte ne mord pas.
   copie intacte : 0 morsure
   CONTRE-EPREUVE DE MON RELEVE : 30 alterations, 30 mordues sur le controle vise ; copie intacte sans morsure
   Premier passage : un plantage de mon script (un encodage ASCII pour l'alteration d'une lettre accentuee) ; deuxieme : 29 sur 30, l'alteration des cellules tombees de (L) n'etait PAS mordue, parce que ma phrase attendue se retrouvait aussi sur la ligne de (L2) : j'ai rendu le controle propre a chaque famille ; troisieme : la SyntaxError du heredoc. Tous gardes.
4. TON releve, rejoue sur mon poste avec mes chemins (prepare_releve_m1_chemins_machine2_v1.py ecrit les deux listes de chemins qu'il lit, relatives a la racine de mon depot de travail ; ton releve n'est pas modifie) : dix controles, 0 morsure ; ta contre-epreuve : vingt alterations, vingt mordues.
   RELEVE DE L'ACTE : 10 controles ; 0 morsure
   CONTRE-EPREUVE DE L'ACTE : 20 alterations, 20 mordues
   Premier passage : A02 a mordu, par MON nom de fichier (ma copie installee de ta premiere partie s'appelle ..._recu.md, ton releve compare les noms) ; j'ai pose une copie octet pour octet sous le nom attendu et rejoue : la faute etait chez moi, pas dans l'acte.
5. Les faits de l'acte que je n'ai pas seulement lus mais REFAITS : les tables de verdict (nn.3) et de ln R3, ln R2, sommes et comptes (nn.5) depuis mes feuilles ; les enonces tires des tables (hors tolerance de MG3, MG4, MG5 ; residu negatif et croissant ; borne 0.0136 a 4 |delta| ; MG3 a 0.05024 et une etendue de 0.0008) ;
   les ecarts-types de groupe et les moyennes de groupe depuis mes boites ; (Q1) (-0.67 erreur), (Q2), (Q3) depuis mes boites et mes feuilles ; la place de la 2D entre l'ordre 2 et l'ordre 3 (0.27 a 0.14 aux MG, 3.7 a 7.0 fois trop loin) ; les annonces du gel (nn.7), recopiees du gel et confrontees a mes issues (cinq annonces contre le run) ;
   les canons des sept lots, des trois gels et des 29 pieces de nn.12 ; les faits du run (48 calculs, 11185 s, aucune relance, 24 sorties de densite, 120 boites, 00 h 11) ; 1743 niveaux, tous fiables ; l'etendue 0.0034.
6. Deux choses que ton acte annonce et que j'ai REJOUEES : (a) le rejeu de tes feuilles contre les sorties du run : 6211 nombres compares, plus grand ecart 1.44e-11 (c'est l'exces de (Q1) en erreurs ; sur les parts y : plus grand ecart 6.16e-12) ; la liste des champs au-dessus de 1e-12 est exactement celle que tu dis (les parts y, les participations qui en derivent, l'exces de (Q1) en erreurs : rien de juge) ;
   (b) l'ancienne tolerance, max(0.02, la moitie du pas de l'ordre 2 a l'ordre 3), refaite sur MES ln R3 et la table de ta chaine : MG3, MG4 et MG5 tombent, les memes ; le desserrement n'a sauve aucune cellule. La table de la chaine : plus grand ecart 1.26e-09 entre ta table et celle que la chaine a rendue sur mon poste.
7. Ce que je n'ai PAS refait, et je le dis : (Q4) n'est refaite que par l'arithmetique (ln G3* de la table de ta chaine, moins ln du plateau du vide LU dans ta feuille de densite) : MES feuilles ne calculent pas le plateau du vide ; il n'entre dans aucun enonce juge. L'histoire de la tolerance de (L)
   (desserree pendant la redaction, avant toute cellule) et celle des essais a l'aveugle sont tes declarations : je ne peux pas les refaire. La lecture par partition reste non verifiee en precision etendue (tu le dis, nn.9 et nn.10). Je n'ai verifie AUCUNE interpretation de physique : j'ai lu nn.0 et nn.8 contre la section 10 du gel
   (ses deux citations sont mot pour mot dans le gel, mon controle R16) : l'acte n'ecrit pas plus que ce que la section 10 prevoit pour "(L) TOMBEE, (S) TENUE" et "(L2) TOMBEE", et dit lui-meme ce qu'il n'ecrit pas.
8. Deux imprecisions de redaction, qui ne changent aucune decision et que je ne mets PAS en condition : (a) nn.8 dit que la chaine d'ordre 3 ne rend pas la densite 2D a 5 pour cent "a 7 et 8 |delta|" : c'est vrai de MG5 seule ; MG3 et MG4 ne sont hors tolerance qu'a 8 |delta| (nn.5 le dit exactement : MG3 a x = 8, MG4 a x = 8, MG5 a x = 7 et 8) ;
   (b) nn.4 attribue les ecarts de 1e-12 a "des parts y" et a l'exces de (Q1) ; les participations, qui en derivent (plus grand ecart 5.42e-12), y sont aussi. Corriger l'un ou l'autre demanderait une version 2 ; je ne le demande pas.
9. JE CONTRESIGNE l'acte du run du gel "pont", SANS CONDITION : verdict (S) TENUE, (C) TENUE, (L) TOMBEE, (L2) TOMBEE, six cellules lisibles sur six, aux tolerances du gel, tel que ton acte l'ecrit et tel qu'il le limite. Le feu vert : date ecrite, heure non attestee (nn.9) : je le redis, c'est ce que mon journal a ecrit et ce que l'acte dit.

## 1. Depot

L'operateur ne m'a pas donne l'ordre de deposer ; il m'a ecrit que tu as livre et qu'il faut contresigner. Je ne depose donc rien. S'il l'ordonne, le depot sera le delta 103 (prochain numero libre) : l'acte octet pour octet, le contreseing, et les lots que le registre n'a pas encore ; le numero se DERIVE du registre au moment du depot (plafond + 1).

## 2. Fins de ligne et chemins

Les journaux de ce lot sont portes en LF et leurs chemins de disque (lettre de lecteur) sont remplaces par "<chemin>" dans les octets du zip (3 journaux touches) ; les journaux d'origine sont dans mon depot de travail. Le canon B de chaque piece est celui des octets portes par le zip.
La copie de ta premiere partie posee sous le nom attendu par ton releve (octet pour octet, verifiee) n'est pas portee : elle redouble ta piece.

## 3. Pieces du lot (empreinte B, 16 hex)

    cette note
    ff50b1ae92526ea5  livraison_18a_acte_gel_pont/authentification_envoi_machine2_v1.log
    c4c01b7bb25e6254  livraison_18a_acte_gel_pont/contreseing/champs_au_dessus_de_1e12_machine2_v1.log
    8990b463a35f1089  livraison_18a_acte_gel_pont/contreseing/champs_au_dessus_de_1e12_machine2_v1.py
    9a00d4ba85d6ca1e  livraison_18a_acte_gel_pont/contreseing/chemins_machine2/liste_pieces_acte_machine2.json
    fa2b55f4c1967efd  livraison_18a_acte_gel_pont/contreseing/chemins_machine2/manifestes_machine2.json
    60e5a29ba93ec345  livraison_18a_acte_gel_pont/contreseing/contre_epreuve_releve_contreseing_pont_machine2_v1.log
    4f21f18e0609d547  livraison_18a_acte_gel_pont/contreseing/contre_epreuve_releve_contreseing_pont_machine2_v1.py
    1ec744fd672a4ecc  livraison_18a_acte_gel_pont/contreseing/contre_epreuve_releve_contreseing_pont_machine2_v1_premier_passage.log
    be1b58fee15d5751  livraison_18a_acte_gel_pont/contreseing/contre_epreuve_releve_contreseing_pont_machine2_v1_second_passage_29_sur_30.log
    aaa2bdf1a3a4debe  livraison_18a_acte_gel_pont/contreseing/contre_epreuve_releve_contreseing_pont_machine2_v1_troisieme_passage_SyntaxError_heredoc.log
    a8773982134d6a26  livraison_18a_acte_gel_pont/contreseing/contre_epreuve_releve_m1_rejouee_sur_mon_poste_machine2_v1.log
    b69f9fbbf29e2311  livraison_18a_acte_gel_pont/contreseing/prepare_releve_m1_chemins_machine2_v1.py
    1fc6f4028e33487b  livraison_18a_acte_gel_pont/contreseing/releve_acte_m1_rejoue_sur_mon_poste_machine2_v1.log
    643c3ff36b0fb8d5  livraison_18a_acte_gel_pont/contreseing/releve_acte_m1_rejoue_sur_mon_poste_machine2_v1_premier_passage_A02_mord_nom_de_fichier.log
    deef0a5cbde299d9  livraison_18a_acte_gel_pont/contreseing/releve_contreseing_acte_pont_machine2_v1.json
    e164b38103d8ec6f  livraison_18a_acte_gel_pont/contreseing/releve_contreseing_acte_pont_machine2_v1.log
    6504d1c73eb9adde  livraison_18a_acte_gel_pont/contreseing/releve_contreseing_acte_pont_machine2_v1.py
    5ccfa58936a26cb9  livraison_18a_acte_gel_pont/contreseing/releve_contreseing_acte_pont_machine2_v1_premier_passage.log
    668d824e0ebdd195  livraison_18a_acte_gel_pont/contreseing/releve_contreseing_acte_pont_machine2_v1_quatrieme_passage_SyntaxError_heredoc.log
    45ee82e0656b339a  livraison_18a_acte_gel_pont/contreseing/releve_contreseing_acte_pont_machine2_v1_second_passage_R13_mord_regex.log
    e164b38103d8ec6f  livraison_18a_acte_gel_pont/contreseing/releve_contreseing_acte_pont_machine2_v1_troisieme_passage_avant_correction_famille.log
    (ce script)  fabrique_lot_contreseing_acte_gel_pont_machine2_v1.py
