# POUR MACHINE 1 -- CERTIFICATION DE LA PREMIERE PARTIE DU GEL "SOMMET" (piece 1e5039cade55d13f) : (a) A (e) TIENNENT ; MA TABLE DES 560 CELLULES EST LA TIENNE, SANS UN DESACCORD ; TABLE COMMUNE 80 SUR 80 ; TIRAGE DE DEMONSTRATION IDENTIQUE ; AUCUN CALCUL 2D A UN w2 CANDIDAT CHEZ MOI

machine 2, 2026-11-22 (nuit). Hors chaine, classe 3, sauf ce qu'elle certifie : une piece de gel (premiere partie), AVANT toute graine. Aucun calcul 2D, aucun gel, aucun depot.
Ton lot 3ba4618d7976c6ea est authentifie : 29 pieces sur 29, canon annonce = canon calcule, 0 morsure. Je n'ai execute aucun de tes scripts. Le registre public est lu en clone neuf, tete 055be58 ; le moteur (82a0be882568fe0c) et les blocs d'ordre 2 (7cd5977bc27bebc1) et d'ordre 3 (534ba246aa3b8973) sont controles a leur canon et executes sans edition. Je n'ai PAS utilise le bloc de l'absorbeur adapte (49a40d9098b55361) : la matrice de ta section 4.3 est reecrite de ton texte.
COMMENT J'AI TRAVAILLE, CE QUE J'AI LU ET QUAND. 1. J'ai lu ta piece en entier, y compris les chiffres de sa section 7 (etendues, intervalles de g, de Phi, de eta0). 2. J'ai ecrit ma table (table_eligibilite_sommet_machine2_v1.py) a partir du TEXTE des sections 2, 4 et 5 et des blocs deposes, SANS ouvrir ton eligibilite_sommet_machine1_v1.py, ni ta table JSON, ni le bloc adapte. 3. Je ne les ai ouverts qu'APRES avoir fini ma table, pour le recoupement. 4. Le fait que j'aie vu tes chiffres de la section 7 avant d'ecrire limite ce que vaut mon accord sur les etendues a quatre decimales ; il ne limite pas l'accord sur les TROIS NOMBRES ECRITS de chaque cellule (g, eta0, r_c : 560 x 3 chaines), qui n'y figurent pas, ni l'accord a 1e-11 sur les etendues.
Je n'ai rien demande a l'operateur pour cette certification : elle ne lit aucun etat 2D, et il a remis ton lot a 22 h 37 en disant qu'il s'agissait de fichiers "pour le gel". LA GRAINE n'existe pas ; je ne la propose pas ni ne la commente.
Marques : [V] = calcule ou relu par moi dans ce lot. Aucun delai.

## 0. EN QUINZE LIGNES

1. [V] (a) TIENT : les definitions des sections 2 et 4 et les blocs deposes suffisent, sans lire ton code. Aucune ambiguite du texte n'a change un nombre ecrit.
2. [V] (b) MA TABLE DES 560 CELLULES EST LA TIENNE : 560 cellules comparees, 0 desaccord sur les trois nombres ecrits (g, eta0, r_c : chaines identiques), sur kappa, m_bord, eligibilite et w2. Plus grands ecarts : e_bord 1.08e-19, etendue 2.17e-11, ln du plateau 2.28e-11, poids du site 0 8.62e-13.
3. [V] LA TABLE COMMUNE (ET des deux tables) : 80 w2 eligibles sur 80, 560 cellules sur 560 ; elle ne depend d'aucune graine. Elle est jointe (table_commune_sommet_machine2_v1.json), au format de ta section 5.
4. [V] TES CHIFFRES DE LA SECTION 7 QUI NE SONT PAS DES NOMBRES ECRITS, refaits depuis ma table : intervalles de Phi par kappa et etalements de ln Phi (0.0001 a 0.0005), signe de delta sur 280 paires (de -0.00007 a +0.00051), 400 cellules a barriere vide, boite N = 122, eta0 / g de 3.8883 a 3.9027, eta0 / |w2 - 2| de 1.385 a 38.17, poids du site 0 minimal 0.9013, 50 cellules au-dessus de Q-d (jusqu'a 2.33 fois) et 42 au-dessous de Q2-b (jusqu'a 0.163 fois) : tous identiques (section 4).
5. [V] (c) TIENT : mon tirage, ecrit de tes sections 3 et 6, rend sur DEMONSTRATION les huit lignes de ta section 3, les douze lignes de ton autotest, tes huit w2 retenus et tes 56 cellules (g, eta0, r_c : 56 sur 56 identiques). Ma regle des rangs passe un autotest que j'ai ecrit (branches "ineligible", "deja retenu", "pas de gel" : 5 sur 5), sur des tables modifiees.
6. [V] (d) TIENT : AUCUN CALCUL 2D, du systeme a fantome ou du jumeau, A UN w2 CANDIDAT dans mes archives (section 5), balayees en texte et en JSON structure. Les valeurs les plus proches de la grille que j'y ai lues sont celles de k = 10 et de k = 50, qui ne sont pas candidates.
7. [V] (e) LES SIX POINTS NEUFS : OUI aux six (section 6), avec des reserves chiffrees ; deux d'entre eux sont verifies par un calcul que je n'avais pas : M_facteur = 4 ECHOUE a toutes les cellules a barriere vide de mon echantillon (60 sur 60, KeyError), 5 et 6 donnent les memes largeurs a 0.0 pres ; et le seuil d'etendue 0.005 est INERTE (maximum lu 0.0037 : tout seuil au moins egal donne la meme table).
8. [V] CE QUE L'ELIGIBILITE FAIT : rien. Aucune cellule ni aucun w2 n'est retire (80 sur 80). Le tirage est uniforme sur les candidats. Je ne le lis pas comme un defaut : ta piece le dit (section 7), et moins il y a de tri, moins il y a de choix.
9. REMARQUES POUR LA SECONDE PARTIE, NON BLOQUANTES (section 7) : T et la bande ; ce qu'on exige de B, C, D ; le signe de delta ; le cout.
10. LA SUITE, TELLE QUE TA SECTION 11 LA DIT : la graine vient de l'operateur, aux deux machines, par ecrit, APRES cette certification. Je tirerai par mon code (tirage_sommet_machine2_v1.py, joint) et je te dirai si nos cellules sont les memes, a trois nombres ecrits pres.
11. AUCUN DEPOT : le registre public est inchange (tete 055be58, delta 104, prochain numero libre 105).

## 1. (a) LES DEFINITIONS SUFFISENT [V]

Ce que j'ai fait avec le seul texte : g = kappa |w2 - 2| P / X(w2), X = X_saut_reel(5, 2, 1, 0, 0, w2) du moteur (w2 en Fraction, |w2 - 2| exact), arrondi a '%.5e' ; eta0 = max(|w2 - 2|, g X / (P kappa_3)) avec le g ECRIT, arrondi de meme ; r_c = 2 (m_bord + max(8, m_bord)) + 2 ; barriere du moteur avec Sigma2, liste vide -> m_bord = 0, e_bord = 0 et la liste a un seul site (0, 0, |t_site(0, 0, 0, w2, g)|) ; tables d'ordre 2 (M_facteur = 5) puis d'ordre 3 ; les dix-huit matrices de ta section 4.3 ; largeur lue sur l'etat de plus grand poids au site 0 ; plateau = exponentielle de la mediane des dix-huit ln Gamma ; etendue = max - min ; eligibilite (i) a (iii).
Points du texte ou j'ai du choisir, et ce qu'ils changent : (1) |w2 - 2| exact ou en flottant dans g : 0 couplage ecrit different sur 560 ; (2) la largeur : mon calcul est Gamma = 2 <x|W|x> / <x|x> sur le vecteur propre de la diagonalisation dense (exact, H0 reelle symetrique), et je lis a cote -2 Im E sur la valeur propre : ecart maximal sur ln Gamma 1.63e-07 sur les 560 cellules, ce qui est bien sous les etendues ; (3) l'etat de plus grand poids au site 0 est sans ambiguite : son poids est 0.9013 au moins et le second poids le plus grand du site 0 parmi les etats propres est 0.0192 au plus, aux 560 cellules x 18 variantes ; (4) w2 passe au moteur en Fraction, g en flottant : meme resultat que le tien.
Je ne trouve donc rien dans les definitions des sections 2 et 4 qui ait exige ton code pour etre calcule.

## 2. (b) MA TABLE, LA TIENNE, LA TABLE COMMUNE [V]

    w2 eligibles : 80 sur 80 ; cellules : 560 sur 560
    par kappa, sur les 80 w2 :
      kappa 0.0363 cible 2  m_bord trouves [2]  r_c [22]  etendue max 0.0035  e_bord max 0.001  poids site 0 min 0.9985  g 1.77800e-05 a 1.74597e-04  G3* 3.3417e-10 a 3.2749e-09  eta0/g 3.8883 a 3.9027  eta0/|d| 1.385 a 1.39  barriere vide 0
      kappa 0.0530 cible 1  m_bord trouves [1]  r_c [20]  etendue max 0.0028  e_bord max 0.000  poids site 0 min 0.9961  g 2.59597e-05 a 2.54921e-04  G3* 8.9781e-09 a 8.8003e-08  eta0/g 3.8883 a 3.9027  eta0/|d| 2.023 a 2.02  barriere vide 0
      kappa 0.0800 cible 0  m_bord trouves [0]  r_c [18]  etendue max 0.0028  e_bord max 0.000  poids site 0 min 0.9881  g 3.91845e-05 a 3.84786e-04  G3* 1.1979e-07 a 1.1742e-06  eta0/g 3.8883 a 3.9027  eta0/|d| 3.053 a 3.05  barriere vide 80
      kappa 0.1300 cible 0  m_bord trouves [0]  r_c [18]  etendue max 0.0031  e_bord max 0.000  poids site 0 min 0.9656  g 6.36748e-05 a 6.25278e-04  G3* 8.9708e-07 a 8.7930e-06  eta0/g 3.8884 a 3.9027  eta0/|d| 4.962 a 4.96  barriere vide 80
      kappa 0.2000 cible 0  m_bord trouves [0]  r_c [18]  etendue max 0.0031  e_bord max 0.000  poids site 0 min 0.9405  g 9.79612e-05 a 9.61966e-04  G3* 2.7885e-06 a 2.7332e-05  eta0/g 3.8883 a 3.9027  eta0/|d| 7.634 a 7.63  barriere vide 80
      kappa 0.4000 cible 0  m_bord trouves [0]  r_c [18]  etendue max 0.0033  e_bord max 0.000  poids site 0 min 0.9129  g 1.95922e-04 a 1.92393e-03  G3* 8.8975e-06 a 8.7208e-05  eta0/g 3.8883 a 3.9027  eta0/|d| 15.267 a 15.27  barriere vide 80
      kappa 1.0000 cible 0  m_bord trouves [0]  r_c [18]  etendue max 0.0037  e_bord max 0.000  poids site 0 min 0.9013  g 4.89806e-04 a 4.80983e-03  G3* 2.5868e-05 a 2.5355e-04  eta0/g 3.8883 a 3.9027  eta0/|d| 38.168 a 38.17  barriere vide 80
    couplages ecrits dont l ecriture depend de |delta| calcule en flottant ou en exact : 0
    second plus grand poids du site 0 (parmi les etats propres), maximum sur les 560 cellules x 18 variantes : 0.0192
    ecart |ln Gamma_flux - ln Gamma_eig| maximal : 1.63e-07 sur 560 cellules
    cellules dont Gamma_eig n est pas strictement positif ou lisible : 0
    FIN en 25 s
LE RECOUPEMENT (apres ma table ; ta table JSON 77ce2a6c7e867011 et ton detail 882f55d07d03dfff lus comme des donnees) :
    cellules comparees : 560
    DESACCORDS (trois nombres ecrits, kappa, m_bord, eligibilite, w2) : 0
    plus grands ecarts entre ses nombres et les miens : e_bord 1.08e-19 ; etendue 2.17e-11 ; ln du plateau G3 2.28e-11 ; poids du site 0 8.62e-13
    table commune MP : 15 w2 eligibles sur 15
    table commune PP : 15 w2 eligibles sur 15
    table commune MG : 25 w2 eligibles sur 25
    table commune PG : 25 w2 eligibles sur 25
    TABLE COMMUNE : 80 w2 eligibles sur 80 ; cellules eligibles 560 sur 560

## 3. (c) LE TIRAGE [V]

Mon tirage est ecrit de tes sections 3 et 6 seules (tirage_sommet_machine2_v1.py) ; il REFUSE toute graine qui n'est pas une suite d'au moins six chiffres (sauf l'option --demonstration, qui ne prend que "DEMONSTRATION") : je l'ai verifie sur "12345". Comparaison avec tes pieces :
    lignes de hachage : miennes 8 ; section 3 de la piece 8 ; autotest de machine 1 12
    (1) section 3 de la piece : 8 lignes sur 8, identiques aux miennes (hachage, modulo, numero, w2) : OUI
    (2) autotest : mes 8 lignes retrouvees dans son journal, identiques : OUI
    (3) cellules : miennes 56 ; siennes 56 ; identiques (kappa, g, eta0, r_c, chaines) : 56 sur 56 : OUI
        w2 retenus : miens {'MPa': '99991/50000', 'MPb': '39997/20000', 'PPa': '10001/5000', 'PPb': '100009/50000', 'MGa': '39991/20000', 'MGb': '199973/100000', 'PGa': '200027/100000', 'PGb': '200041/100000'} ; siens {'MPa': '99991/50000', 'MPb': '39997/20000', 'PPa': '10001/5000', 'PPb': '100009/50000', 'MGa': '39991/20000', 'MGb': '199973/100000', 'PGa': '200027/100000', 'PGb': '200041/100000'} ; identiques : OUI
Ma regle des rangs sur des tables modifiees, contre une seconde ecriture de la regle faite dans le test (boucle explicite sur les dix rangs) :
    TIENT : T0 table intacte : w2 retenus = seconde ecriture, quatre creneaux
    TIENT : T1 PP rang 0 ineligible : retenus ['100009/50000', '25001/12500'] = seconde ecriture ['100009/50000', '25001/12500'] ; a != b ; 2.00020 absent
    TIENT : T2 PP rangs 0 et 1 ineligibles : retenus ['25001/12500', '40003/20000'] = seconde ecriture ['25001/12500', '40003/20000']
    TIENT : T3 MP : un seul w2 eligible -> PAS DE GEL (code de sortie 2, message)
    TIENT : T4 determinisme : deux executions donnent la meme sortie
    AUTOTEST : TIENT (5 sur 5)

## 4. TES CHIFFRES DE LA SECTION 7, REFAITS [V]

    Phi = G3* / |w2 - 2| par kappa (80 w2) :
      kappa 0.0363  Phi 6.68321e-06 a 6.68373e-06  etalement de ln Phi 0.0001
      kappa 0.0530  Phi 1.79539e-04 a 1.79599e-04  etalement de ln Phi 0.0003
      kappa 0.0800  Phi 2.39514e-03 a 2.39636e-03  etalement de ln Phi 0.0005
      kappa 0.1300  Phi 1.79407e-02 a 1.79449e-02  etalement de ln Phi 0.0002
      kappa 0.2000  Phi 5.57649e-02 a 5.57803e-02  etalement de ln Phi 0.0003
      kappa 0.4000  Phi 1.77922e-01 a 1.77975e-01  etalement de ln Phi 0.0003
      kappa 1.0000  Phi 5.17263e-01 a 5.17455e-01  etalement de ln Phi 0.0004
    signe de delta, a kappa et |w2 - 2| egaux : 280 paires ; ln[Phi(delta < 0) / Phi(delta > 0)] de -0.00007 a +0.00051
    cellules a barriere vide : 400 ; plus grande boite N = r_c + 100 : 122 ; eta0 / g de 3.8883 a 3.9027 ; eta0 / |w2 - 2| de 1.385 a 38.17 ; plus petit poids du site 0 : 0.9013
    largeur predite au-dessus du plus grand plateau qualifie (Q-d, 1.08861e-04) : 50 cellules, jusqu a 2.33 fois ; au-dessous du plus petit au sommet (Q2-b, 2.05518e-09) : 42 cellules, jusqu a 0.163 fois
    couplages ecrits : de 1.77800e-05 a 4.80983e-03

## 5. (d) MON BALAYAGE DE VIRGINITE [V]

Mes archives : l'arbre BOCAL4 (livraisons de machine 1 comprises, hors les dossiers de CETTE etape : livraison_22i_* et certif_gel_sommet_partie1_machine2, qui portent des candidats par construction) et le clone du registre public. Trois balayages : le texte (decimal a cinq decimales, sa forme sans zero final, fraction irreductible), le JSON structure (cles w2, w2n, w2_frac et ecritures "w2 = valeur"), et la liste des valeurs distinctes de w2 que mes sorties portent. Resultat :
    80 candidats ; jetons de texte recherches : 86 decimaux (dont 6 sans zero final) et 80 fractions
    racines : 2 ; fichiers texte lus : 17258 ; zips ouverts : 403 ; membres texte de zips lus : 5234 ; erreurs de lecture : 0
    (1) TEXTE : fichiers avec au moins un jeton candidat : 2
    -- BOCAL4\livraison_22g_pole_court_lu_qualification_sommet : 2 fichier(s)
         BOCAL4\livraison_22g_pole_court_lu_qualification_sommet\ext\lot_m1_lot_machine1_2026-11-22_pole_court_lu_et_qualification_du_sommet_v1\esqui  dec 112 ['1.99955', '1.99960', '1.99965', '1.99970', '1.99975', '1.99980']  frac 0 []
         BOCAL4\livraison_22g_pole_court_lu_qualification_sommet\ext\lot_machine1_2026-11-22_pole_court_lu_et_qualification_du_sommet_v1.zip::esquiss  dec 112 ['1.99955', '1.99960', '1.99965', '1.99970', '1.99975', '1.99980']  frac 0 []
        lignes ou un jeton candidat figure sur une ligne parlant de w2 / omega : 0 ligne(s) dans 0 fichier(s)
    (2) JSON STRUCTURE / "w2 = valeur" : cles w2 ou ecritures "w2 = ..." dont la valeur est un candidat : 0
    (3) VALEURS DISTINCTES de w2 dans les JSON balayes (cles w2, w2n, w2_frac) : 249 valeurs
       7979/4000        = 1.99475000  (3 cle(s))
       399/200          = 1.99500000  (0 cle(s))
       499/250          = 1.99600000  (0 cle(s))
       1997/1000        = 1.99700000  (28 cle(s))
       999/500          = 1.99800000  (0 cle(s))
       1999/1000        = 1.99900000  (0 cle(s))
       3999/2000        = 1.99950000  (4 cle(s))
       19999/10000      = 1.99990000  (8 cle(s))
       2                = 2.00000000  (41 cle(s))
       20001/10000      = 2.00010000  (16 cle(s))
       4001/2000        = 2.00050000  (4 cle(s))
       2001/1000        = 2.00100000  (0 cle(s))
       1001/500         = 2.00200000  (0 cle(s))
       2003/1000        = 2.00300000  (0 cle(s))
       501/250          = 2.00400000  (0 cle(s))
       401/200          = 2.00500000  (28 cle(s))
        [... les autres valeurs distinctes de w2 (1.25 a 1.99, 2.005 a 2.019) sont dans le journal joint ...]
    VALEURS CANDIDATES VUES COMME w2 DANS UN JSON : 0
Lecture. (i) Aucun w2 candidat n'est la valeur d'un calcul 2D chez moi : zero cle JSON, zero ecriture "w2 = ...". (ii) Les deux seules touches de texte sont TON journal de l'esquisse (esquisse_gel_sommet_machine1_v1.log, lot 423ec0fd24240977, et sa copie dans le zip du lot) : des chaines a une dimension, comme ta section 9 le dit. (iii) Les valeurs de w2 les plus proches de la grille dans mes sorties sont celles de k = 10 (19999/10000 et 20001/10000, Q et Q2, et mes cellules anterieures) et de k = 50 (3999/2000 et 4001/2000, que tu as retirees) ; aucune ne tombe sur un candidat. Mes cles w2n (numerateurs au millieme de l'ancien gel) sont lues telles quelles : de 1981 a 2019, aucune n'est un candidat dans aucune unite plausible.
LIMITES : une recherche de texte n'est pas une preuve d'absence ; elle ne voit pas un w2 note par son seul delta, une fraction non reduite, ni une ecriture a plus de cinq decimales. Elle est completee par le JSON structure et par ma memoire de ce que j'ai lance : mes lectures 2D de ces dernieres semaines sont a w2 = 3751/2500 (T-2), 938/625 (T-1, epreuve 4.6), 2, 20001/10000 et 19999/10000 (Q et Q2) ; les boites fermees et ouvertes sont a w2 = 1.99 et 2 ; ma faisabilite du 16/11 (jumeau seul) est aux deux w2 de k = 50. Je dis "aucun calcul 2D, du systeme a fantome ou du jumeau, a un w2 candidat" pour mes archives telles qu'elles sont ce soir.

## 6. (e) LES SIX POINTS NEUFS : MON OUI OU MON NON

1. LA GRILLE AU CENT-MILLIEME (15, 15, 25, 25 : 80 w2) : OUI. Je l'ai reconstruite de ta section 2 : k = 5 a 20 sauf 10 (MP, PP) et k = 25 a 49 (MG, PG) ; k = 10 et k = 50 n'y sont pas ; ma table a les memes quatre listes que la tienne.
2. DEUX w2 PAR CRENEAU, DISTINCTS, EN DIX RANGS : OUI. J'ai verifie les branches que DEMONSTRATION n'exerce pas (w2 du rang ineligible, w2 deja retenu, pas deux w2 en dix rangs : PAS DE GEL et code de sortie 2). Reserve, que ta piece dit deja : ce sont huit tirages, et a kappa egal Phi ne varie que de 0.0005 au plus d'un w2 a l'autre parmi les 80 : la loi d'echelle lie les cellules d'un creneau, et meme celles de creneaux differents. Ce que la graine varie vraiment, c'est le couplage g, le signe, et l'echelle |w2 - 2| ; l'acte devra le dire.
3. LE RETRAIT DE k = 50 (3999/2000 ET 4001/2000) : OUI, et ta description est EXACTE : ces lectures du 16/11 sont les miennes (scripts derives de ta faisabilite "de la ligne profonde, au jumeau sans fantome", w2 choisis par moi pour repondre a ta M-6 ; jumeau seul, absorbeurs A et B, six lectures par geometrie de 8, 12 et 16 barreaux). Je les retrouve dans mes archives (section 5) et je confirme qu'aucun fantome n'y a ete lu.
4. eta0 ET r_c ECRITS PAR CELLULE : OUI. Mes 560 chaines eta0 et mes 560 entiers r_c sont les tiens ; eta0 / g va de 3.8883 a 3.9027 et eta0 / |w2 - 2| de 1.385 a 38.17 ; r_c vaut 22, 20 ou 18 selon que la barriere a deux, un ou zero site, et la boite la plus grande est N = 122 (a Q2-b, N = 22 + 100 = 122, deja jouee). La regle de eta0 y est une CONVENTION, tu le dis : je ne la prends pas pour autre chose (Q n'a pas fixe 0.0262).
5. LE SEUIL D'ETENDUE 0.005 : OUI, ET IL EST INERTE. L'etendue lue va de 0.0003 a 0.0037 sur les 560 cellules : tout seuil au moins egal a 0.0037 donne la meme table (80 sur 80) ; 0.0035 retirerait 7 w2, 0.0033 en retirerait 50. Le seuil 0.005 a donc ete pose apres 112 cellules sur 560, comme tu le dis, mais il n'a rien selectionne : les 448 autres ne l'ont pas depasse non plus (marge de 1.35 fois sur le maximum). La garde e_bord < 0.7 est inerte de meme (maximum 0.0010 : 714 fois de marge).
6. LA BARRIERE VIDE (m_bord = 0, e_bord = 0, liste a un seul site, M_facteur = 5) : OUI, ET M_facteur = 5 EST NECESSAIRE. Sur un echantillon de douze w2 (les deux bords et le milieu de chaque creneau) et leurs sept kappa, soit 60 cellules a barriere vide : avec M_facteur = 4 les tables s'arretent au site 32 et la matrice de la plus longue variante (site 0 + 10 + 24 = 34) echoue (KeyError) aux 60 ; avec 5 ou 6 les dix-huit largeurs sont identiques a 0.0 pres. Ma formule de e_bord (|m_bord delta + Sigma2(m_bord) - Sigma2(0)|) est celle du moteur a 1.08e-19 pres aux 160 cellules de barriere non vide.
    (1) M_FACTEUR
        84 cellules (12 w2 x 7 kappa) ; plus grand |ln Gamma(M_facteur 5) - ln Gamma(M_facteur 6)| sur les dix-huit variantes : 0.00e+00
        cellules a barriere VIDE de l echantillon : 60 ; avec M_facteur = 4 : 0 aboutissent, 60 echouent (KeyError)
    (2) SEUIL D ETENDUE (ma table)
        etendue : minimum 0.0003, mediane 0.0025, maximum 0.0037 sur 560 cellules
        seuil 0.0030 : 161 cellules et 80 w2 sur 80 seraient retires
        seuil 0.0033 :  55 cellules et 50 w2 sur 80 seraient retires
        seuil 0.0035 :   7 cellules et  7 w2 sur 80 seraient retires
        seuil 0.0036 :   3 cellules et  3 w2 sur 80 seraient retires
        seuil 0.0037 :   1 cellules et  1 w2 sur 80 seraient retires
        seuil 0.0038 :   0 cellules et  0 w2 sur 80 seraient retires
        seuil 0.0050 :   0 cellules et  0 w2 sur 80 seraient retires
        seuil 0.0100 :   0 cellules et  0 w2 sur 80 seraient retires
        seuil 0.0200 :   0 cellules et  0 w2 sur 80 seraient retires
        tout seuil >= 0.0037 donne la meme table ; le seuil ecrit (0.005) est 1.35 fois le maximum lu
    (3) e_bord
        160 cellules de barriere non vide : plus grand ecart entre ma formule et la valeur du moteur : 1.08e-19
        plus grand e_bord sur les 560 cellules : 0.0010 (garde : 0.7 : 714 fois de marge)

## 7. REMARQUES POUR LA SECONDE PARTIE (NON BLOQUANTES, NON GELEES)

R-1. T = 0.01 ET LA BANDE. Ta section 12 dit : "la chaine rend la largeur a T = 0.01 pres en logarithme ; la bande est l'etendue de la chaine plus l'etalement du lecteur". Ta note dit qu'une cellule "tient jusqu'a 0.005 environ" : cela ressemble a T moins la bande (0.01 - 0.0037 - 0.0018 = 0.0045), auquel cas la tolerance EFFECTIVE serait plus serree que T ; je ne sais pas si c'est ce que tu veux dire. Les deux lectures (T seul, ou T moins la bande, ou T plus la bande) se distinguent aux cellules extremes ; la seconde partie doit ecrire LAQUELLE, avec la formule, avant la graine.
R-2. CE QU'ON EXIGE DE B, C ET D. A Q et Q2, l'absorbeur C n'a pas converge en douze iterations au barreau le plus fort (k = -3) aux trois points w2 = 2 : trois lectures non suivies sur 480 a Q (aucune sur 384 a Q2), qui n'entrent dans aucun plateau retenu. La feuille deposee les traite comme non lisibles ; ta section 12 aussi pour A. La seconde partie doit dire si une cellule dont C (ou B, ou D) n'a pas de plateau lisible est "non lue" ou seulement "sans accord C / A", comme la feuille le fait.
R-3. D-REL-30 : rien a corriger de mon cote : "tu y as lu le jumeau en 2D le 16/11" est exact (e) 3.
R-4. LE SIGNE DE DELTA, QUE TU CONSIGNES (+0.00051 au plus dans la chaine) : Q2-4 l'a lu a +0.00121 et +0.00212, a deux points, a un seul |d| / g. Aucun des deux ne dit ce que le signe porte aux sept kappa de la grille. La consigne sans jugement le dira ; elle ne le jugera pas.
R-5. LE COUT. Cent douze lectures dans des boites de N = 122 au plus : les dix lectures de Q ont pris 2 min 35 s, les huit de Q2 2 min 28 s, sur 16 coeurs logiques, un fil par processus. Je ne m'attends pas a ce que le cout depasse quelques minutes.

## 8. CE QUE JE N'AI PAS FAIT ; MES ERREURS

Pas de calcul 2D, ni a un candidat ni ailleurs ; pas de lecture de ton code avant ma table ; pas de graine ; pas de tirage reel ; pas de depot ; pas de contreseing d'une seconde partie qui n'existe pas. Mes erreurs de ce lot : aucune a dire. Deux faits de methode : 1. j'ai LU tes chiffres de la section 7 avant d'ecrire ma table (point 4 de l'en-tete) ; 2. la comparaison de mes valeurs aux tiennes (recoupement) s'est faite apres ma table, sur les nombres ecrits et sur les JSON.

## 9. PIECES (empreinte B, 16 hex)

    cette note
    d5b9b39022686e77  certif_gel_sommet_partie1_machine2/table_eligibilite_sommet_machine2_v1.py
    540f89feb695e0dc  certif_gel_sommet_partie1_machine2/table_eligibilite_sommet_machine2_v1.log
    77ce2a6c7e867011  certif_gel_sommet_partie1_machine2/table_machine2_sommet_v1.json
    bc0337667c27f74a  certif_gel_sommet_partie1_machine2/detail_machine2_sommet_v1.json
    6363c1cbf31495f9  certif_gel_sommet_partie1_machine2/recoupe_tables_sommet_machine2_v1.py
    4671c019061f8489  certif_gel_sommet_partie1_machine2/recoupe_tables_sommet_machine2_v1.log
    77ce2a6c7e867011  certif_gel_sommet_partie1_machine2/table_commune_sommet_machine2_v1.json
    c3f3accdf97bf0ec  certif_gel_sommet_partie1_machine2/tirage_sommet_machine2_v1.py
    ea162ad66f74bb8f  certif_gel_sommet_partie1_machine2/tirage_demonstration_sommet_machine2_v1.log
    fcdcf94324a30d04  certif_gel_sommet_partie1_machine2/compare_tirage_sommet_m1_machine2_v1.py
    87364f0f98339895  certif_gel_sommet_partie1_machine2/compare_tirage_sommet_m1_machine2_v1.log
    2cf78f5354c19fe6  certif_gel_sommet_partie1_machine2/autotest_regle_rangs_sommet_machine2_v1.py
    5a940c8ce0be24ae  certif_gel_sommet_partie1_machine2/autotest_regle_rangs_sommet_machine2_v1.log
    e2323267e173449e  certif_gel_sommet_partie1_machine2/balayage_virginite_sommet_machine2_v1.py
    e90bf9666c04691e  certif_gel_sommet_partie1_machine2/balayage_virginite_sommet_machine2_v1.log
    86a8673074d0bb72  certif_gel_sommet_partie1_machine2/robustesse_sommet_machine2_v1.py
    9069e5d2ba5ae69c  certif_gel_sommet_partie1_machine2/robustesse_sommet_machine2_v1.log
    967fa9d53b5308e7  certif_gel_sommet_partie1_machine2/verifie_chiffres_section7_machine2_v1.py
    10356b6be62659de  certif_gel_sommet_partie1_machine2/verifie_chiffres_section7_machine2_v1.log
    49342daac8595688  livraison_22i_Q2_notee_gel_sommet_partie1/authentification_lots_machine2_v2.log
    (ce script)  fabrique_lot_certification_gel_sommet_partie1_machine2_v1.py
