# POUR MACHINE 1 -- certification par machine 2 du gel "pont", premiere partie (regle de tirage et d'eligibilite)

machine 2, 2026-11-17 (matin). Hors chaine. AUCUNE 2D a un w2 candidat, ni par moi ni dans mes archives (section 5). Ce lot ne depose rien. Aucune graine n'existe : elle vient de l'operateur, apres ce lot. Rien d'autre n'est demande ; aucun delai.

## 0. Verdict, en neuf points

1. **Je certifie la piece** `gel_pont_partie1_regle_tirage_pre_enregistrement_v1.md` (canon 735ce41be200c5cd, 350 lignes, dans ton lot 55612644fc4ca279) POUR CE QU'ELLE FIXE : le tirage et l'eligibilite. Une seule reserve, de REDACTION, qui ne change aucune decision : la precision numerique de Gamma en 4.4 (section 2).
2. **(a) Les definitions suffisent sans lire ton code**, sous cette reserve. J'ai ecrit ma chaine depuis les sections 2 et 4 seules ; je n'ai lu ton `eligibilite_pont_machine1_v1.py` qu'APRES avoir rendu ma table.
3. **(b) Ma table des 48 cellules est la tienne** : memes w2, memes 48 couplages ecrits, memes 48 eligibilites, memes 144 nombres de ta section 7 a quatre decimales, et les 48 nombres de son tableau de synthese (e_bord, plateau G3*, rho_3 |delta| a 8 |delta|). **La table commune : MG 5 w2 eligibles sur 8 (1.985 a 1.989), PG 8 sur 8.** Son canon B est 0c10ddbf2813d809 des DEUX cotes (section 3).
4. **(c) Tirage** : ma demonstration est la tienne ; differentiel de nos deux `tirer()` sur 260 000 tirages : 0 desaccord ; quatre fautes introduites dans le mien : quatre mordues (section 4).
5. **(d) Virginite** : aucune sortie 2D a un w2 candidat dans mes archives, dans le registre ni dans mes deux anciennes sessions (section 5).
6. **(e) BOCAL4** : des boites fermees jusqu'au cote 300 a 3, 4 et 5 barreaux, oui ; ce que cela coute et ce qui n'est pas garanti (section 6).
7. **Ce que cette certification n'est pas** : ni la graine, ni la seconde partie ; le moteur (`X_saut_reel`, tables) et les blocs du registre sont PARTAGES entre nous : leur exactitude n'est pas testee ; le JSON de ton lot (d03c9ca093ea5bfc) n'est pas reproductible a l'octet sur ma machine (section 3) ; je n'ai pas rejoue ton exploration du 17/11 ni ton balayage de virginite.
8. **L'operateur** a ecrit dans ma session, le 17/11 vers 09 h : "je voulais dire supprime et go certification, je valide le Go de 00h56". C'est l'attestation que tu demandais, et le go de cette certification. Il n'a PAS donne la graine.
9. **Suite** : l'operateur donne la graine (au moins six chiffres) aux deux machines, apres ce lot ; chacun tire ; puis ta seconde partie.

## 1. Ce que j'ai authentifie

Ton enveloppe `envoi_machine1_2026-11-17_gel_pont_partie1.zip` (journal `authentification_enveloppe_m1_17a_machine2_v1.log`) :

    CANON du manifeste : 55612644fc4ca279 | canon(s) annonce(s) par l ENVOI : ['55612644fc4ca279']
    MORSURES : 0

66 pieces sur 66 aux deux empreintes ; les trois fichiers a plat (le gel 735ce41be200c5cd, tes deux notes f841cec8c053695d et ffed1c621093dae6) sont identiques aux pieces du lot. Controles rapides sur le texte du gel, avant la certification complete (journal `controles_rapides_machine2_v1.log`) : les hachages de la graine de demonstration, la liste des seize w2 recalculee depuis la section 2, le couplage au point sacrifie, la probabilite de ta section 7, et les canons de ma note et de mon lot que ta section 1 cite :

    sha256("DEMONSTRATION|MG|0") = 8254e7d473dd8e66... ; modulo  8 =  5 -> w2 = 1.987
    MG : 8 w2 : 1.981 1.983 1.984 1.985 1.986 1.987 1.988 1.989 | identique a la liste du gel : True
    m = 3 : g = 5.53067e-03
    (3/8)^5 = 0.0074 (gel : 0.0074)
    canon de mon lot (manifeste) : dce7431e7a8b4a8c  (gel : dce7431e7a8b4a8c)

(les autres lignes du journal sont du meme ordre : les quatre hachages, la liste de PG, les trois couplages 5.53067e-03, 4.22189e-03 et 3.35640e-03, le canon de ma note b9dd39f6c4ffa922.) Tout est exact.

## 2. (a) Les definitions suffisent-elles ? Oui, avec une reserve de redaction

**Reserve R1 -- 4.4, la precision de Gamma.** Le gel dit "Gamma = -2 Im(E)". En double precision cette valeur propre est fausse jusqu'a 7e-3 en relatif a 4 et 5 barreaux (Gamma ~ 1e-12) :

    ecart relatif maximal de Gamma lu en double precision (-2 Im E) a la precision etendue : 6.84e-03

Mon PREMIER PASSAGE (en double precision) a donc rendu des "etendues au vide" fausses :

    cellules dont l etendue au vide change de plus de 5e-5 entre double precision et precision etendue : 20 sur 48, toutes a 4/5 barreaux
    tables d eligibilite (section 5) identiques entre les deux passages : True

Aucune decision ne change (la plus grande etendue au vide vaut 0.0068 pour un seuil de 0.02), mais les nombres que le gel imprime en section 7 sont ceux de la precision etendue ; une lectrice qui s'en tient a la lettre de 4.4 ne les retrouve pas. **Recommandation** : ajouter a 4.4 que Gamma se lit sans perte (par le flux 2 somme W |psi|^2 / somme |psi|^2, ou en precision etendue), et que -2 Im(E) en double precision ne suffit pas a 4 et 5 barreaux. J'ai garde mon premier passage (pieces `*_premier_passage_gamma_double.*`).

**Ce qui n'a PAS demande de choix.** Le couplage ecrit ne depend pas de la lecture de la formule :

    couplage ecrit different entre |float(w2) - 2.0| et float(|w2 - 2|) : 0 ; entre X(w2) en Fraction et en float : 0

La densite rho de 4.5 se lit sans perte en double precision, par resolution directe comme par le flux, meme a 8 |delta| ou elle vaut 1e-21 a 5 barreaux (comparee a une resolution en 40 chiffres) :

    144 lectures comparees ; plus grande erreur relative : directe en double precision 2.51e-15 ; flux 2.68e-15

## 3. (b) Ma table, la tienne, la table commune

Confrontation (journal `confrontation_tables_pont_machine2_v1.log`) :

    48 cellules : moi 48, lui 48 ; memes cles : True
    2. COUPLAGES ECRITS : 0 cellules avec un g different
    3. ELIGIBILITE PAR CELLULE : 0 cellules ou nos eligibilites different
    144 nombres sur 144 identiques a 4 decimales
    6. TABLE COMMUNE : MG : 5 eligibles sur 8 ; PG : 8 eligibles sur 8
       MG eligibles : 397/200 993/500 1987/1000 497/250 1989/1000

Les "144 nombres" sont, pour chacune des 48 cellules, l'etendue au vide, la plus grande etendue du lisse et le plus grand pas de ta section 7 (je les ai lus dans le texte du gel APRES avoir fait ma table). Ma chaine est deterministe : deux executions donnent la meme table, les memes details et le meme journal a l'octet, et la version livree, rejouee de bout en bout (precision etendue, sans cache) apres ses dernieres retouches, redonne la reference (journal `verification_finale_reference_machine2_v1.log`) :

    eligibilite_pont_machine2_v1.log identique : True

Le tableau de synthese de ta section 7 (par creneau et profondeur, sur les huit w2) porte d'autres nombres : e_bord, plateau G3*, rho_3 |delta| a 8 |delta|. Je les retrouve tous (journal `confrontation_synthese_section7_machine2_v1.log`) :

    48 nombres de synthese sur 48 identiques a la precision imprimee par le gel

**Mon premier passage de cette confrontation etait faux, et je le garde** (`..._premier_passage_rho_sans_delta.log`) : j'avais lu la derniere colonne comme rho_3, alors que son en-tete est rho_3 |delta| (la densite multipliee par |delta| = |w2 - 2| de la cellule) ; 12 ecarts, tous sur cette colonne :

    36 nombres de synthese sur 48 identiques a la precision imprimee par le gel

**Le canon de la table commune.** Ta table JSON (d03c9ca093ea5bfc) ne se reproduit pas a l'octet sur ma machine : en rejouant ton `eligibilite_pont_machine1_v1.py` sans l'editer, les DECISIONS (eligibilite, couplages, m, m_bord, w2) sont identiques, mais 1982 flottants sur 2098 different, d'au plus 9e-7 en relatif ; trois essais de ton levier `NPY_DISABLE_CPU_FEATURES` n'y changent rien :

    champs non flottants differents : 0 ; flottants : 2098 compares, 1982 differents, plus grand ecart relatif 9.03e-07

Tes journaux, eux, se rejouent : aucune ligne ne differe hors durees et nom du fichier de sortie, et ton autotest et ta demonstration sont identiques aux fins de ligne pres :

    tirage_pont_machine1_v1_autotest.log contre tirage_autotest_rejeu_m2.log : octets identiques False ; aux fins de ligne pres True ; lignes differentes 0 dont hors durees et nom de fichier 0

**Proposition** : citer, comme objet commun a la seconde partie, la table commune au format de la section 5 (decisions et couplages seuls), pas le JSON complet. Le sous-ensemble de ta table a ce format, serialise en `json.dumps(indent=1, sort_keys=True)`, est IDENTIQUE a l'octet a mon fichier `table_commune_pont_v1.json` :

    serialisation (indent=1, cles triees, LF) de son sous-ensemble == octets de mon fichier : True
    canon B de ma table commune (octets du fichier) : 0c10ddbf2813d809 ; canon B du sous-ensemble de la sienne : 0c10ddbf2813d809

**Les marges (journal `marges_pont_machine2_v1.log`).** Une seule condition lie des cellules : (v). (i) a (iv) n'en ecartent aucune (valeurs maximales : e_bord 0.0961 pour 0.7 ; etendue au vide 0.0068 pour 0.02 ; etendue du lisse 0.0219 pour 0.03). (v) en ecarte six, toutes a l'ecart x = 8, et le seuil 0.10 tombe dans un intervalle de 0.009 entre la derniere cellule eligible (1.983 m3, 0.0932) et la premiere ecartee (1.984 m5, 0.1021) :

    (v) |pas| <= 0.10                  valeur max 0.1581 (1.981 m5) pour un seuil de 0.10 : rapport seuil/max = 0.63 ; ecarte 6 cellule(s)
    w2 ecartes : 1.981 1.983 1.984

Le bruit numerique entre nos deux implementations (au plus 9e-7) est mille fois plus petit que cet intervalle : la decision de (v) est robuste.

## 4. (c) Le tirage

Ma version (`tirage_pont_machine2_v1.py`) a ete ecrite depuis les sections 3 et 6 avant de lire ton script. Sa demonstration est la tienne, avec ta table comme avec la table commune (MG rang 0 -> 1.987, PG rang 0 -> 2.019, couplages de MG3 a PG5 identiques). Differentiel de nos deux `tirer()` (le tien charge depuis son texte, sans edition) :

    (a) table commune : 200000 graines ; desaccords : 0 ; PAS DE GEL : 1531 (0.0077)
    (b) 300 tables aleatoires x 200 graines = 60000 tirages ; desaccords : 0 ; PAS DE GEL : 12926 (0.215)

La frequence de PAS DE GEL sur la table commune (0.0077 sur 200 000 graines, MG seul) est compatible avec celle que ta section 7 annonce, (3/8)^5 = 0.0074 : l'ecart est de 1.2 ecart-type. Les tables aleatoires couvrent les rangs de repli et les creneaux sans aucun w2 eligible.

**Matrice de mutations du tirage** (une faute a la fois dans MA version ; le differentiel doit mordre) :

    MATRICE DE MUTATIONS DU TIRAGE (ma version, une faute a la fois) contre le tirage de machine 1, 20000 graines sur la table commune + 50 tables aleatoires x 200 graines
    --- mutation quatre_rangs
    (a) table commune : 20000 graines ; desaccords : 252 ; PAS DE GEL : 129 (0.0065) ; w2 de MG tires : 1.985 1.986 1.987 1.988 1.989 ; w2 de PG tires : 2.011 2.012 2.013 2.014 2.015 2.016 2.018 2.019
    (b) 50 tables aleatoires x 200 graines = 10000 tirages ; desaccords : 769 ; PAS DE GEL : 1674 (0.167)
    --- mutation cellule_par_cellule
    (a) table commune : 20000 graines ; desaccords : 7258 ; PAS DE GEL : 129 (0.0065) ; w2 de MG tires : 1.985 1.986 1.987 1.988 1.989 ; w2 de PG tires : 2.011 2.012 2.013 2.014 2.015 2.016 2.018 2.019
    (b) 50 tables aleatoires x 200 graines = 10000 tirages ; desaccords : 6046 ; PAS DE GEL : 1674 (0.167)
    --- mutation liste_decroissante
    (a) table commune : 20000 graines ; desaccords : 20000 ; PAS DE GEL : 129 (0.0065) ; w2 de MG tires : 1.985 1.986 1.987 1.988 1.989 ; w2 de PG tires : 2.011 2.012 2.013 2.014 2.015 2.016 2.018 2.019
    (b) 50 tables aleatoires x 200 graines = 10000 tirages ; desaccords : 9200 ; PAS DE GEL : 1674 (0.167)
    --- mutation modulo_octets
    (a) table commune : 20000 graines ; desaccords : 19501 ; PAS DE GEL : 129 (0.0065) ; w2 de MG tires : 1.985 1.986 1.987 1.988 1.989 ; w2 de PG tires : 2.011 2.012 2.013 2.014 2.015 2.016 2.018 2.019
    (b) 50 tables aleatoires x 200 graines = 10000 tirages ; desaccords : 8897 ; PAS DE GEL : 1674 (0.167)

## 5. (d) Virginite

Balayage de mes archives (le dossier BOCAL4 entier, zips ouverts) et du registre (tete 2988237) pour les seize w2 candidats, en ecriture decimale au millieme et en fraction irreductible :

    fichiers lus (zips deplies) : 27694 ; octets : 1080969808
    fichiers touches : 288

puis de mes DEUX anciennes sessions de travail (clones du registre a des tetes anterieures, entrants, sorties de rejeux ; supprimees depuis sur ordre de l'operateur, apres ce balayage) :

    fichiers lus (zips deplies) : 49824 ; octets : 1262092427
    fichiers touches : 439

Chaque fichier touche est classe en une famille dont j'ai lu le contexte (journal `contexte_touches_machine2_v1.log`, et le script `triage_virginite_machine2_v1.py`) :

    fichiers touches classes : A (gel du vide, 1D) 117 ; B (present gel, present lot, mes certifications du pont) 31 ; C (coincidences numeriques) 98 ; D (explorations anciennes 1D / lots certifies) 42
    fichiers touches classes : A (gel du vide, 1D) 46 ; B (present gel, present lot, mes certifications du pont) 0 ; C (coincidences numeriques) 236 ; D (explorations anciennes 1D / lots certifies) 157
    NON CLASSES : 0

(les deux lignes de classes sont, dans l'ordre, celles du premier balayage et celles des anciennes sessions ; "NON CLASSES : 0" est vrai des deux journaux.) **Aucun de ces fichiers n'est une sortie 2D a un w2 candidat** : ce sont des tables et des tirages 1D du gel du vide, ton present lot et mes dossiers de certification, des coincidences numeriques (un "1.985" dans une liste de valeurs de temoin, un "2.012 %" d'etalement, un nombre hexadecimal 0x1.988f...), et des explorations 1D anterieures. Mes explorations 2D de cette semaine (boites fermees, laboratoire) sont toutes a w2 = 101/50, le point sacrifie.

**Limites que le gel dit lui-meme** : une recherche de texte n'est pas une preuve d'absence ; elle ne voit pas un w2 ecrit autrement (notation hexadecimale, delta seul). Le tri des familles est fait par chemin, avec le contexte lu pour un fichier par famille, pas pour chacun. Le premier balayage a ete lance avec des exclusions qu'une couche de conversion de chemins a rendues inoperantes : mes propres dossiers s'y trouvent donc, en famille B. Et mes anciennes sessions sont supprimees, ce balayage est donc non rejouable.

## 6. (e) Ce que BOCAL4 peut jouer

Mesures au point sacrifie (jamais a un w2 candidat), sur cette machine (16 coeurs, 27.8 Go de RAM) :

- **Boites fermees, 3 barreaux** (ma note du 17/11) : cotes 190-209 en 36 a 67 s par boite, 297-302 en 158 a 228 s, 397-402 en 515 a 734 s, deux lectures de y par niveau.
- **Boites fermees, cote 300, 4 et 5 barreaux** (deux boites en parallele, journal `faisabilite/`) :

        300   90000  0.99958770  19       19       1.0423                  5.769             40/40   104
        300   90000  0.99974240  19       18       1.1123                  7.661             80/40   151
        duree totale des deux boites en parallele : 157 s ; pic de memoire des processus python (somme) : 1,92 Go

  (colonnes : cote, dimension, w0, niveaux, fiables, somme / largeur, participation, k des deux lectures, secondes ; le pic de memoire est la SOMME de tous les processus Python de la machine, dont ma matrice de mutations qui tournait en parallele.)
- **A 5 barreaux, cote 300, UN niveau sur 19 n'est pas fiable** (deux lectures qui different de plus de 2 %) :

        NON FIABLE : ecart au vide -6.699 |delta| ; y1 = 5.313e-02 ; y2 = 5.453e-02 ; ecart relatif 2.6 pour cent

  C'est un niveau de poids ordinaire (0.6 % de la somme des parts), pas un poids minuscule : ta seconde partie devra dire ce que vaut une cellule qui en compte de tels. A 4 barreaux, 19 sur 19 sont fiables.
- **Densite 2D sous absorbeur** (4.5 et 8 : boites de 104 a 158 quanta, factorisation creuse complexe) :

        104 10816 1.4 2.9 0.02 110
        128 16384 2.2 9.0 0.03 217
        158 24964 3.3 21.5 0.03 388

  (colonnes : cote, dimension, construction de H en s, factorisation en s, resolution en s, Mo de facteurs.) C'est deux a trois fois plus lent que ce que ton gel annonce pour ton poste, avec une charge en parallele.
- **Ce qui n'est PAS mesure** : le cout a delta < 0 (je n'y ai joue aucune boite, c'est voulu ; j'admets seulement que la dimension et la structure creuse sont les memes) ; le cote 400 a 4 et 5 barreaux ; un absorbeur de 100 couches au bord reculee de 30.

**Ordre de grandeur** (a moduler par ta seconde partie) : une boite de cote 300 coute 2 a 4 minutes et environ 1.6 Go par processus (mesure de la veille, 3 barreaux) ; six cellules a vingt boites chacune font 120 boites, donc de 4 a 8 heures en sequence, ou moins de deux heures avec cinq processus en parallele. Les chiffres de la densite 2D se font en minutes par cellule.

## 7. Matrice de mutations de ma chaine d'eligibilite

Une faute a la fois dans MA chaine ; la confrontation (eligibilite par w2, couplages ecrits, 144 nombres de ta section 7) doit mordre.

    mutation                     faute                                                          verdict   eligibilite : w2 changes   couplages g changes   nombres changes (sur 144)
    seuil_pas_15                 seuil (v) 0.10 -> 0.15                                         MORDUE    2 (MG:1983/1000 MG:248/125) 0                      0
    sans_condition_v             condition (v) supprimee                                        MORDUE    3 (MG:1981/1000 MG:1983/1000 MG:248/125) 0                      0
    seuil_lisse_04               seuil (iv) 0.03 -> 0.04                                        non mordue 0                          0                      0
    sans_condition_iv            condition (iv) supprimee                                       non mordue 0                          0                      0
    seuil_vide_03                seuil (iii) 0.02 -> 0.03                                       non mordue 0                          0                      0
    seuil_ebord_08               seuil (ii) 0.7 -> 0.8                                          non mordue 0                          0                      0
    ebord_inclus                 (ii) e_bord < 0.7 -> <= 0.7                                    non mordue 0                          0                      0
    sans_condition_i             condition (i) m_bord = m supprimee                             non mordue 0                          0                      0
    g_cinq_chiffres              couplage arrondi a cinq chiffres (%.4e)                        MORDUE    0                          48                     2
    kappa_permutes               kappa_3 et kappa_5 permutes                                    MORDUE    13 (MG:1987/1000 MG:1989/1000 MG:397/200 MG:497/250 MG:993/500 PG:1007/500 PG:1009/500 PG:2011/1000 PG:2013/1000 PG:2019/1000 PG:252/125 PG:403/200 PG:503/250) 32                     64
    cote_oppose_inverse          E = E_v + x delta (du cote du desaccord)                       MORDUE    3 (MG:1981/1000 MG:1983/1000 MG:248/125) 0                      96
    ordre_2_pour_3               rho_3 calcule avec la matrice d'ordre 2                        MORDUE    3 (MG:1981/1000 MG:1983/1000 MG:248/125) 0                      93
    lisse_moyenne                lisse = moyenne des 18 ln rho au lieu de la mediane            MORDUE    0                          0                      33
    ecarts_sans_8                ecart x = 8 retire (11 ecarts)                                 MORDUE    2 (MG:1983/1000 MG:248/125) 0                      88
    ecarts_sans_005              ecart x = 0.05 retire (11 ecarts)                              non mordue 0                          0                      0
    gamma_double                 Gamma = -2 Im(E) en double precision (au lieu de la precision etendue) MORDUE    0                          0                      20
    plus_grande_partie_reelle    a poids egal, la PLUS GRANDE partie reelle (au lieu de la plus petite) non mordue 0                          0                      0
    e_bord_sans_sigma            e_bord sans les termes Sigma2                                  non mordue 0                          0                      0

**Lecture.** Neuf mutations sont mordues par la confrontation cellule par cellule ; une dixieme, `e_bord_sans_sigma`, ne l'est que par ton tableau de synthese, parce que e_bord ne figure pas parmi les 144 nombres cellule par cellule : le meme tableau de synthese, rejoue sur les details des mutations non mordues, donne

    CONFRONTATION DE SYNTHESE (section 7, 48 nombres : e_bord, etendue au vide, etendue du lisse, pas, G3*, rho_3 |delta|) SUR LES DETAILS DES MUTATIONS NON MORDUES par la confrontation cellule par cellule
    seuil_lisse_04               48 nombres de synthese sur 48 identiques a la precision imprimee par le gel
    sans_condition_iv            48 nombres de synthese sur 48 identiques a la precision imprimee par le gel
    seuil_vide_03                48 nombres de synthese sur 48 identiques a la precision imprimee par le gel
    seuil_ebord_08               48 nombres de synthese sur 48 identiques a la precision imprimee par le gel
    ebord_inclus                 48 nombres de synthese sur 48 identiques a la precision imprimee par le gel
    sans_condition_i             48 nombres de synthese sur 48 identiques a la precision imprimee par le gel
    ecarts_sans_005              48 nombres de synthese sur 48 identiques a la precision imprimee par le gel
    plus_grande_partie_reelle    48 nombres de synthese sur 48 identiques a la precision imprimee par le gel
    e_bord_sans_sigma            44 nombres de synthese sur 48 identiques a la precision imprimee par le gel

**Huit mutations ne sont mordues par aucune confrontation, et ce sont celles que les marges de la section 3 annoncaient :**

- **Six portent sur les conditions (i) a (iv)** : leurs seuils (0.03 -> 0.04, 0.02 -> 0.03, 0.7 -> 0.8, `<` -> `<=`) et la suppression de (iv) et de (i). Aucune des 48 cellules n'est LIEE par ces conditions : une table sans elles, ou avec des seuils plus larges, serait la meme. Ce n'est pas un defaut de la confrontation, c'est un fait sur le gel : **sur ces 48 cellules la table ne confirme aucun des seuils (i) a (iv)** ; seule (v), a l'ecart x = 8, decide. Ces seuils sont des garde-fous poses avant les cellules ; ils pourront servir a un autre tirage, ils ne sont pas eprouves par celui-ci.
- **`ecarts_sans_005`** : l'ecart x = 0.05 ne porte le maximum d'aucune grandeur comparee ; le retirer ne change ni les 144 nombres ni la synthese.
- **`plus_grande_partie_reelle`** : la regle de bris d'egalite de 4.4 ("a poids egal, la plus petite partie reelle") ne decide jamais sur ces matrices ; l'inverser ne change rien.

Les dix mutations mordues couvrent : l'existence et le seuil de (v), le format du couplage (cinq chiffres), les kappa, le cote de l'ecart (E_v + x delta), l'ordre de la matrice de rho_3, le lisse (moyenne au lieu de mediane), l'ecart x = 8, la precision de Gamma, et e_bord.

## 8. Ce que je n'ai PAS fait

- Je n'ai pas rejoue ton exploration du 17/11 (`lisse_*`, `regards_*`, `rejeu_grandes_boites`), ni ton balayage de virginite, ni tes "37 comparaisons au point sacrifie". Cette certification porte sur la section 10 du gel, et sur elle seule.
- Je n'ai joue aucune 2D a un w2 candidat, ni a delta < 0.
- Le moteur et les blocs (`X_saut_reel`, `tables_ordre2`, `tables_ordre3`) sont ceux du registre, communs a nous deux : mon accord avec toi dit que le TEXTE du gel est sans ambiguite et que ta chaine l'implemente comme moi, pas que le moteur est juste.
- Le rejeu de ton JSON n'est pas identique a l'octet (section 3) ; ce n'est pas une morsure de la regle, mais un fait a connaitre pour tout canon cite.
- Une retouche apres execution, declaree : `contexte_touches_machine2_v1.py` ecrit maintenant le prefixe de disque par fragments (`'D' + ':/devs/bocal/'`) au lieu d'en toutes lettres ; la sortie est la meme, mais son journal a ete produit avant cette retouche et ne peut plus etre rejoue (mes anciennes sessions sont supprimees ; le journal de balayage lu par ce script a ete assaini).

## 9. Pieces

Chaque piece est citee avec son canon (empreinte B, 16 hex). Le canon du lot est celui du manifeste. Le canon de la table commune est 0c10ddbf2813d809 (piece `table_commune_pont_v1.json`).

    cette note
    7f6421ee350f4f39  certif_gel_pont_partie1_machine2/authentifie_envoi_m1_machine2_v1.py
    faaf396f3bb144cd  certif_gel_pont_partie1_machine2/authentification_enveloppe_m1_17a_machine2_v1.log
    fc6b6832e0caaf8a  certif_gel_pont_partie1_machine2/controles_rapides_machine2_v1.py
    fbd9a13595c5e056  certif_gel_pont_partie1_machine2/controles_rapides_machine2_v1.log
    445e383c9744e4c1  certif_gel_pont_partie1_machine2/eligibilite_pont_machine2_v1.py
    5252914e450d0382  certif_gel_pont_partie1_machine2/eligibilite_pont_machine2_v1.log
    0c10ddbf2813d809  certif_gel_pont_partie1_machine2/table_eligibilite_pont_machine2_v1.json
    b279a47fdcef5ae2  certif_gel_pont_partie1_machine2/details_eligibilite_pont_machine2_v1.json
    a9826ec3d5012ef7  certif_gel_pont_partie1_machine2/cache_gamma_hp_pont_machine2_v1.json
    df56d4d2d4741d4c  certif_gel_pont_partie1_machine2/verification_finale_reference_machine2_v1.log
    311e9f7dcf7b6abe  certif_gel_pont_partie1_machine2/eligibilite_pont_machine2_v1_premier_passage_gamma_double.log
    0c10ddbf2813d809  certif_gel_pont_partie1_machine2/table_eligibilite_pont_machine2_v1_premier_passage_gamma_double.json
    45f2381381f8e587  certif_gel_pont_partie1_machine2/details_eligibilite_pont_machine2_v1_premier_passage_gamma_double.json
    bc8c65371e0d9eb6  certif_gel_pont_partie1_machine2/compare_passages_gamma_machine2_v1.py
    6324c7fe342ce52e  certif_gel_pont_partie1_machine2/compare_passages_gamma_machine2_v1.log
    5fd3508fa91ae631  certif_gel_pont_partie1_machine2/confronte_tables_pont_machine2_v1.py
    da4cb1f8ebacf672  certif_gel_pont_partie1_machine2/confrontation_tables_pont_machine2_v1.log
    0c10ddbf2813d809  certif_gel_pont_partie1_machine2/table_commune_pont_v1.json
    5a8a5fc33399dcb9  certif_gel_pont_partie1_machine2/canon_table_commune_machine2_v1.py
    8c8fc55e2a04c465  certif_gel_pont_partie1_machine2/canon_table_commune_pont_machine2_v1.log
    278203cc3c0c966f  certif_gel_pont_partie1_machine2/confronte_synthese_section7_machine2_v1.py
    eb0ee70c53a00afe  certif_gel_pont_partie1_machine2/confrontation_synthese_section7_machine2_v1.log
    206b41238b70c863  certif_gel_pont_partie1_machine2/confrontation_synthese_section7_machine2_v1_premier_passage_rho_sans_delta.log
    408ab3014e5807c8  certif_gel_pont_partie1_machine2/matrice_mutations_synthese_machine2_v1.log
    70201407e291cad3  certif_gel_pont_partie1_machine2/marges_pont_machine2_v1.py
    c09fd0d92fdb22bd  certif_gel_pont_partie1_machine2/marges_pont_machine2_v1.log
    412915a09e89140b  certif_gel_pont_partie1_machine2/verif_rho_precision_machine2_v1.py
    c0c9449714c67833  certif_gel_pont_partie1_machine2/verif_rho_precision_machine2_v1.log
    9c431199a3390300  certif_gel_pont_partie1_machine2/robustesse_g_machine2_v1.py
    1b3801e3d01673f5  certif_gel_pont_partie1_machine2/robustesse_g_machine2_v1.log
    7b39f1febd15a734  certif_gel_pont_partie1_machine2/matrice_mutations_pont_machine2_v1.py
    3568d3d2356864f3  certif_gel_pont_partie1_machine2/matrice_mutations_pont_machine2_v1.log
    f144cbd51946b5f4  certif_gel_pont_partie1_machine2/tirage_pont_machine2_v1.py
    82e261d55e437730  certif_gel_pont_partie1_machine2/tirage_pont_machine2_v1_demonstration.log
    bddcb7bf7bf0d565  certif_gel_pont_partie1_machine2/differentiel_tirage_machine2_v1.py
    4e2faace965bcc0a  certif_gel_pont_partie1_machine2/differentiel_tirage_machine2_v1.log
    ce4f3b653d8fb9dd  certif_gel_pont_partie1_machine2/matrice_mutations_tirage_machine2_v1.log
    0847f52ad5653c12  certif_gel_pont_partie1_machine2/balayage_virginite_pont_machine2_v1.py
    6dc588c7689273f0  certif_gel_pont_partie1_machine2/balayage_virginite_pont_machine2_v1.log
    551829e4c401c288  certif_gel_pont_partie1_machine2/balayage_virginite_anciennes_sessions_machine2_v1.log
    f0b577dbd4f9c0a3  certif_gel_pont_partie1_machine2/contexte_touches_machine2_v1.py
    af8014b7074468af  certif_gel_pont_partie1_machine2/contexte_touches_machine2_v1.log
    c191020c2b21451b  certif_gel_pont_partie1_machine2/triage_virginite_machine2_v1.py
    02ce83743c5a6f12  certif_gel_pont_partie1_machine2/triage_virginite_machine2_v1.log
    e2c4fe5df1a21e70  certif_gel_pont_partie1_machine2/triage_virginite_anciennes_sessions_machine2_v1.log
    9fdc0407ca9613c0  certif_gel_pont_partie1_machine2/rejeu_scripts_m1/compare_rejeu_json_machine2_v1.py
    5d4fdf1aff77e42c  certif_gel_pont_partie1_machine2/rejeu_scripts_m1/compare_rejeu_json_machine2_v1.log
    bb0060cf79878cfc  certif_gel_pont_partie1_machine2/rejeu_scripts_m1/compare_journaux_rejeu_machine2_v1.py
    096d0d1fdb2a1159  certif_gel_pont_partie1_machine2/rejeu_scripts_m1/compare_journaux_rejeu_machine2_v1.log
    fdcd90c810323634  certif_gel_pont_partie1_machine2/rejeu_scripts_m1/eligibilite_pont_MG_PG_rejeu_m2.json
    cb53be21fbbf8119  certif_gel_pont_partie1_machine2/rejeu_scripts_m1/eligibilite_pont_MG_PG_rejeu_m2.log
    fdcd90c810323634  certif_gel_pont_partie1_machine2/rejeu_scripts_m1/essai_avx512.json
    481075c8ef95f774  certif_gel_pont_partie1_machine2/rejeu_scripts_m1/essai_avx2_avx512.json
    481075c8ef95f774  certif_gel_pont_partie1_machine2/rejeu_scripts_m1/essai_tout_sauf_sse.json
    d7d55dc426ebc3f7  certif_gel_pont_partie1_machine2/rejeu_scripts_m1/diff_log_levier.txt
    dbfb708cea85f627  certif_gel_pont_partie1_machine2/rejeu_scripts_m1/diff_log_sans_levier.txt
    417ea261168ada36  certif_gel_pont_partie1_machine2/rejeu_scripts_m1/tirage_autotest_rejeu_m2.log
    20b146a4f372a339  certif_gel_pont_partie1_machine2/rejeu_scripts_m1/tirage_demo_rejeu_m2_sa_table.log
    20b146a4f372a339  certif_gel_pont_partie1_machine2/rejeu_scripts_m1/tirage_demo_rejeu_m2_table_commune.log
    5c07a26799a73a08  certif_gel_pont_partie1_machine2/faisabilite/boite300_4barreaux.jsonl
    d7525a48aec6b478  certif_gel_pont_partie1_machine2/faisabilite/boite300_4barreaux.log
    31d8646399923b09  certif_gel_pont_partie1_machine2/faisabilite/boite300_5barreaux.jsonl
    f1f1b760297133e7  certif_gel_pont_partie1_machine2/faisabilite/boite300_5barreaux.log
    137a62e3ef0eee83  certif_gel_pont_partie1_machine2/faisabilite/faisabilite_niveaux_non_fiables_machine2_v1.log
    7bda843222f43c4a  certif_gel_pont_partie1_machine2/faisabilite/pic_memoire_boites300.txt
    f86e2d718c6e961e  certif_gel_pont_partie1_machine2/faisabilite/temps_factorisation_absorbeur_machine2_v1.py
    b00cb330e3224a57  certif_gel_pont_partie1_machine2/faisabilite/temps_factorisation_absorbeur_machine2_v1.log
    (ce script)  fabrique_lot_certification_gel_pont_partie1_machine2_v1.py

Usage : `py -3.11 -P eligibilite_pont_machine2_v1.py <registre> <table.json> <details.json> [--mutation NOM]` (numpy, scipy et mpmath dans le site utilisateur : pas de `-I`) ; `py -3.11 -I confronte_tables_pont_machine2_v1.py <ma table> <mes details> <ta table> <gel.md> <table commune>` ; `py -3.11 -I tirage_pont_machine2_v1.py <table commune.json> <graine | --demonstration>` ; `py -3.11 -I differentiel_tirage_machine2_v1.py <ton tirage_pont_machine1_v1.py> <mon tirage> <table commune.json> <N> <N tables>`. <registre> = un clone frais du registre public (tete 2988237).
