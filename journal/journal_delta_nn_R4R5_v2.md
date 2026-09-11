JOURNAL DELTA nn -- LES TESTS D1 (R4, VOLETS A A E), LA LECTURE R5 ET LEURS SUITES
ENTRENT AU REGISTRE : LA TABLE DE PARITE DU FLANC TIENT EN AVEUGLE SUR TROIS
FAMILLES ET TROIS DEGRES (6/6) ; LES TROIS SEUILS A UN PAS DE P-4 SONT DES BORDS
CRIBLES (0 NOEUD A T = 6400) ; A DEGRE PAIR LE SITE 2:1 EST UNE ILE DU SHIFT,
DERIVEE, ET LA PERIODE D'ENVELOPPE SOUS LE SEUIL TIENT A DEUX DEGRES, SA FORME
CORRIGEE FALSIFIANT SA FORME NAIVE EN AVEUGLE ; LA PERIODE DE LIBRATION D'UNE
CELLULE PIEGEE VA COMME 1/eps ; DEUX PREDICTIONS TOMBENT (P-D1-9 DANS SA FENETRE,
P-D-2), UNE REGLE MEURT (PARITE DU SIGNE), UNE LOI EST RETIREE (t_apex = C/eps)
(redaction machine 1, depot operateur, 2026-09-11) -- PROJET, VERSION 2
=======================================================================
v2 = v1 (86d6ee29d27938ff, REMPLACEE, non editee) + les trois correctifs de la
certification machine 2 (4e7dafb54a908f71 : certifie sous reserve, 88 nombres
re-derives, 85 concordants, 3 mordants, aucun sur un verdict) : H1 A-7, serie
C_P declaree non homogene en resolution (option b) ; H2 A-6, fourchette 4.7 a
5.7 ; H3 A-4, borne 1e-5 ; H4 nn.6 (a)(ii), l'outil de la regle. Rien d'autre
ne change ; les hunks sont comptes au manifeste.
S'insere apres le delta 88 (39fbc89, journal_delta_88_P4_v1 0f8e283fa9499f96).
NUMERO nn PRIS AU DEPOT : plafond releve sur clone frais lbaaz/SG_1 a HEAD
39fbc89 le 11/09 = 88, premier numero libre 89 ; le corps garde "nn". Aucun
numero de serie (N, E, D) n'est pris ici ; les defauts portent leurs etiquettes
de chantier (E18). Classe du depot : 1 ; la sequence s'est jouee en classe 3
(derivations, gels, lectures), rule (P) ; chaque run cite ses attendus geles en
tete de log (INSTRUCTIONS D1 2154286e9df56806 ; gel volet E v2 91d858bbf2da60af ;
predictions m1 f8face8b95486d02, 9537d740be94bf91, 8250dc0a2719ea8c ; gel P-D-2
b5e0b5230b08d767). Aucune regle nouvelle ((X) jusqu'au 28/09) ; trois regles de
chantier proposees en nn.6.
Ce projet est de plume machine 1 ; il est a certifier par machine 2 en un tour
avant depot. Chaque nombre de cet acte est RE-DERIVE des pieces de la section
nn.1 par les feuilles du lot de ce delta, rejouees en un seul passage
(rederive_acte_R4R5_machine1_v1.py / .log) ; aucune valeur de lecture n'est crue.
Moteur unique : m9_replication_v1.py c8ed357b120352c4, jamais edite (PB-1).
Le chantier constante A (v5 certifie, geste de convergence en dt a 7|1.73) est
un chantier parallele et n'entre pas ici.

nn.0 POSITION EN TROIS PHRASES
  Les quatre volets restants des tests D1 et le volet E ont ete joues par
  machine 2 sur des attendus geles avant chaque run, et lus des deux cotes par
  enumeration : la direction de l'asymetrie de signe pres d'une resonance,
  derivee au premier ordre d'une forme normale sans parametre, tient sur six
  paires aveugles (familles 3:2, 4:1, 2:1 ; degres 7, 9, 13) ; les trois seuils
  a un pas de grille de P-4 ne bougent pas a T = 6400 et l'ensemble explosif y
  est fige ; a degre pair le site 2:1 est une ile du shift de frequence du
  premier ordre, derivee, et la periode de l'enveloppe sous le seuil y tient a
  p = 6 puis, corrigee du deplacement d'action, a p = 8 en aveugle contre sa
  forme naive. Deux predictions de machine 1 tombent par la lettre de leur
  falsifieur (l'excursion sous seuil dans sa fenetre ; le rang des largeurs
  quantiques a p = 5 par -r_gen), une regle meurt (parite du signe aux
  rationnels exacts), et une loi de temps ecrite un soir et verifiee
  circulairement le lendemain est retiree par les deux machines. Quatre residus
  sont nommes, aucun chantier n'est ouvert, aucun run n'est demande.

nn.1 LA SEQUENCE ET SES PIECES (convention B, 16 hex ; canon d'un lot =
     convention B de son manifeste ; ordre d'emission ; tout LF/ASCII sauf
     mention -- les .log de machine 2 sont CRLF, verifies au brut)
  07/09  INSTRUCTIONS_machine2_tests_D1_v1.md  2154286e9df56806  (plume m1 ;
         attendus A a D, cite au 88 ; transite vers m1 le 10/09 par
         19be3c0f9b91fbbc)
  09/09  predictions de parite m1 f5fa6542578ca2ac -> test aveugle m2
         6d2b96cc8e50e3ce (48 paires, 10 tenues / 1 falsifiee) -> reponse m1
         e7ed23f3f88acd6e -> controle m2 8fa603e0736cafde -> derivation m1
         ee8d9e76ad995cc8 (note 96c6524a218a5620) -> integration m2
         e003d7a502824ef1 -> v2 m1 efbc205a6d6dfa74 (note 1a90e943572fa083)
         -> test m2 66bc0c5e7a39be48 (H2) -> reponse m1 c5a58cda839068ac
  09/09  gel volet E v1 m2 c3e504623701ca7e (gel 963e7176dee0ec27) -> lecture m1
         25aaaadd99688a94 -> gel v2 m2 b0a18128cc41f131 (gel 91d858bbf2da60af,
         regle 5.6 des deux fenetres) -> accuse m1 3ca4c319ab1fe85b
  10/09  RUN R4 m2 6f6387f416854fec [c4f063080e8d1f78] : voletA
         ccb612e7d7e53bfd, voletC a0464fcd4d7b609e, voletD 2b81d3960a1b5eb5,
         voletE 2e7012b994ad8747, sonde apex 8a24236871ab6280, balayage s0
         e8739d1bb0f6fc5f ; lecture m1 235950a5fae4e440 (note
         12c23ad683c5398e) ; contreseing m2 19be3c0f9b91fbbc (voletD v2 avec
         t_exp a 6400 58e79a822583b401) ; cloture m1 54bb383dee0e29c5
  10/09  R5 m2 efb384ec6db3003b (lecture 168138322eef57f0, gel P-D-2
         b5e0b5230b08d767) ; reponse m1 6f2829d0cfe87def ; authentification
         des r_gen m2 45087b33bef371e3 (8/8 au bit) ; accuse m1
         795816ceb0295008
  11/09  quadrature C m1 12a0c1df70612cd1 (note 9c103fd6e0c1fa92) ; contreseing
         m2 dd9f798a1d406890 ; accuse et prediction de libration m1
         55de3b1e1163bf4e (f8face8b95486d02) ; run m2 09bb0eee8f817a1e
         (44981d0b57980d68) ; lecture m1 94f0e184637650e6 ; correction et
         resolution m2 9b1d89d71774ea38 (e7fc10ece9a3fddc) ; accuse m1
         55ef7053a21144dd
  11/09  D2 m1 c7c490ea72f58dba (note 69d9ad0b68c1f3ad, prediction
         9537d740be94bf91) ; RUN volet B m2 579cf0a6bed9ac76
         [575f0d8f99b64cb3] (90d4675bebb23f0e) ; lecture m1 9fb35e2b97a0748a
         (prediction p = 8 8250dc0a2719ea8c) ; RUN p = 8 m2 19edb2ba80f357f1
         [752be8b86d1a1d7b] (9a201423743cfde6, controle a 13-20 maxima
         0787e737e657e705) ; lecture m1 c61b5359ffa64d6d ; erratum m2
         0040a285bbbbcd10 ; accuse m1 fc8b8c9fcab08209
  Registre lu : clone frais a HEAD 39fbc89, plafond 88. Pieces detenues d'un
  seul cote et declarees telles : archives_G6.json (m2 ; cellules 7|1.45,
  7|1.55, 7|2.50 de la confrontation post hoc de A-1) ; les points M17 v17
  (m2 ; largeurs de R5, dont deux sont au delta 82) ; mes trois pieces de
  calibration du 07/09 (e07322da0f4ab4dd, 1290abd4dcdb917e, 19b1588c791e94d8),
  introuvables aux deux postes, sans consequence : le temps qu'elles portaient
  se re-derive (A-6) et n'a plus a etre cru.

nn.2 LES FAITS ACQUIS
  A-1  LA MARCHE EN SIGNE SUR LE FLANC D'UNE RESONANCE, DERIVEE ET TENUE EN
       AVEUGLE. Avec l'angle du mode fantome retrograde, la phase resonante
       phi = a theta1 + b theta2 place les deux signes de la famille v = 0 aux
       deux points sin phi = 0 (phi0(+1) = b pi, phi0(-1) = a pi) ; un desaccord
       delta = a - b w2 pousse la phase dans un sens : le signe fragile (seuil
       le plus bas) est +1 a gauche et -1 a droite de a:b si a est pair, l'inverse
       si b est pair, aucun si a et b sont impairs (T2). Machine 2 a INTEGRE la
       forme normale : T1 (temps d'echappement identiques a la resonance exacte,
       16 couples, ecart 0.00e+00) et T2 (12 cas sur 12) en sortent, la table de
       parite en est la composition exacte (11/11). Confrontation post hoc :
       31 cellules archivees du flanc de 2:1 (1.80 a 2.30, p = 5, 7, 9, 11),
       31 directions retrouvees ; A(2.00) = +0.0019, +0.0011, +0.0005, +0.0003 ;
       9|2.50, la cellule qui avait tue la regle de parite (A-9), dans le sens
       derive ; 7|1.45 (+0.159833), 7|1.55 (-0.203348), 7|2.50 (s*(+1) = 1.727
       contre 1.198113) dans les archives G6 de m2, decouvertes apres la
       derivation, 3/3. Puis LE TEST AVEUGLE, gel v2 (regle 5.6 : une paire est
       tenue si aucune fenetre ne contredit et une concorde, falsifiee des
       qu'une fenetre contredit, porte ln 1.02), six paires vierges :
         7|3.90  A400 -0.129976  A1600 -0.129976   4:1 gauche   TENUE
         7|4.10        +0.289269        +0.303414   4:1 droite   TENUE
         9|1.45        +0.135987        +0.135987   3:2 gauche   TENUE  bande [0.057, 0.240] dans
         9|1.55        -0.224387        -0.210242   3:2 droite   TENUE  bande [0.073, 0.305] dans
         13|1.90       -0.110726        -0.110726   2:1 gauche   TENUE  bande [0.095, 0.125] dans
         13|2.10       +0.111924        +0.111924   2:1 droite   TENUE  bande [0.095, 0.125] dans
       6 tenues, 0 falsifiee, 0 muette ; la marche de 3:2 est INVERSEE par
       rapport a celle de 2:1, comme derive ; le degre 13 n'avait jamais ete
       joue et ma bande de grandeur, fixee avant le gel, contient les deux
       mesures. Grilles conformes a 2.2e-16, comptes 96 = explosifs + non
       explosifs, aucune bissection a sa borne. Ce que le premier ordre ne
       donne pas, verse : la grandeur (exp(|A|(p-1)) passe de 2.61 a 2.97 et de
       3.39 a 6.02 entre p = 7 et p = 9 sur le flanc de 3:2 : l'exposant p-1 est
       un fait du flanc de 2:1, pas une loi) ; les cellules piegees a resonance
       exacte ; la portee en dw2 d'un flanc quand plusieurs resonances se
       disputent une cellule. [DERIVE m1, INTEGRE m2, MESURE-M2 aveugle]
  A-2  LES TROIS SEUILS A UN PAS DE P-4 SONT DES BORDS CRIBLES (P-D1-4, branche
       b). Rejeu a T = 6400 sur les grilles de P-4 (grille et t_exp <= 1600
       identiques au bit au JSON e66549fd72f4239b) : 7|2.42|+1 G_P1 indices
       70 / 69 / 69, 5|1.50|+1 G_ext 63 / 62 / 62, 7|1.50|+1 G_ext 62 / 61 / 61
       a T = 400 / 1600 / 6400 ; 0 noeud entre 1600 et 6400 la ou une loi de
       fenetre en donnerait 19 a p = 7 ; et AUCUNE explosion nouvelle entre 1600
       et 6400 (27, 34, 35 explosifs sur 96 aux deux fenetres) : l'ensemble
       explosif entier est fige. R-P4-2 est fermee. [MESURE-M2 ; re-derive m1
       des t_exp bruts]
  A-3  VOLET C : 11|6.00 PIEGEE ; 11|2.50 NON CONCLUANTE PAR LA LETTRE. Le texte
       gele classe "par la bissection deposee a T = 400 et 1600 (cusp = direct)".
       11|6.00 (s0 = 1.873518) : explosifs = noeuds 85 a 95 aux deux fenetres,
       un intervalle, dln = 0 : PIEGEE ; la clause A-6 du delta 86 tient, la
       lecture "marginale" du cadre D1 tombe. 11|2.50 (s0 = 0.979962) : a T = 400
       explosifs = 86 a 95 ; a T = 1600 = {47, 48, 50, 53, 56} U 86 a 95 : le
       bloc du haut ne bouge pas, quatre ilots isoles apparaissent dessous. La
       bissection deposee n'a ete jouee qu'a 400 (l'ancre) ; sur un ensemble
       explosif qui n'est pas un intervalle une bissection est INDEFINIE (elle
       rend 0.57 ou 0.99 selon l'encadrement) ; la statistique s* = min y rend
       dln = -0.55164 pour une loi directe a -0.15403 : ni direct ni zero. Le
       classificateur gele n'existe pas sur cet ensemble : NON CONCLUANTE. La
       lecture "bord du bloc" (piegee) est une regle formulee apres la donnee :
       proposee pour tout gel futur (nn.6), sans verdict ici. [MESURE-M2 ;
       re-derive m1]
  A-4  VOLET A : LA MOITIE GEL DE P-D1-9 TIENT, LA MOITIE EXCURSION EST
       FALSIFIEE DANS SA FENETRE. Attendu gele : "apex = max de l'enveloppe sur
       [0, 3000]", tolerance plus ou moins 4 pour cent, "falsifieur : un apex
       hors tolerance a deux cellules". Mesure : les cinq cellules GEL (11|6.00
       a s0 = 0.5, 0.1, 0.05 ; 11|4.00 ; 11|3.00) restent a l'excursion du
       mouvement libre, apex = s0 (3 + w2^2)/Delta a 1e-5 pres [H3] (ecart relatif
       max 9.5e-06 sur les cinq), plates ; les six
       cellules d'excursion (7|2.50, 9|2.50, 11|2.50, 11|1.75, 11|2.67, 11|4.50 a
       s0 = 0.2) restent EXACTEMENT sur l'excursion libre (rapport 1.0000) --
       six hors tolerance, zero explosion. Le falsifieur mord : FALSIFIEE,
       moitie excursion, dans sa fenetre. Ce qui est falsifie est l'hypothese de
       TEMPS (T = 3000 transportee de la calibration p = 5 sans remise a
       l'echelle, faute m1) ; la VALEUR d'apex n'est pas testee. Machine 2 avait
       d'abord ecrit "non concluant de fenetre" et l'a RETIRE : un verdict qui
       protege la prediction en deplacant la faute sur l'instrument ; regle
       prise des deux cotes : une prediction qui nomme sa fenetre est falsifiee
       dans cette fenetre. Faits de classe 3 verses : le canal s'ouvre a 7|2.50
       entre s0 = 0.51 et 0.65 (apex 1.8115 a 0.65 pour 1.863 predit a un autre
       s0 : indication) ; c'est la resonance 5:2 EXACTE et admise (a + b = 7 = p),
       muette au premier ordre, qui s'ouvre -- pas la 2:1 desaccordee, dont le
       seuil de capture derive vaut s_open = 1.45 (A-6). [MESURE-M2 ; lettre
       re-derivee m1]
  A-5  A DEGRE PAIR LE SITE 2:1 EST UNE ILE DU SHIFT, DERIVEE, ET VOLET B LA
       MESURE. A degre pair seuls les harmoniques a j + k pair existent, a tout
       ordre ; la 2:1 n'entre que par (4,2) = cos 2phi, admise ssi p >= 6 (a
       p = 4 aucun terme resonant). Hamiltonien moyenne : h = (2 - w2) J2 -
       (g/(p Delta)) [a(J2) + b(J2) cos 2phi], a = <S^p> (le shift, absent a
       degre impair), b le coefficient de (4,2) ; le rapport r1 = b'/a' au point
       initial vaut 0, 0.094, 0.219, 0.346, 0.465, 0.572 pour p = 4 a 14, et
       atteint 1 a p = 26 : ILE au premier ordre pour tout p pair <= 24 (ce qui
       re-derive et etend "degres pairs fermes au premier ordre, p <= 14" de
       D1). Mesure, 6|2.00 : s*(400) = s*(1600) = 1.012586 (noeud 85, les deux
       signes), 11 explosifs sur 96 en un intervalle, 0 ilot, ratio 1.0 : P1
       TENUE sur sa moitie testable (l'egalite des signes est une identite de
       l'integrateur, A-9). Fait non predit : K*(6|2.00) = 0.052565 contre
       0.347 a p = 4 -- l'ile a degre pair n'est pas a K constant ; sa valeur vit
       au-dela du premier ordre. [DERIVE m1 ; MESURE-M2]
  A-6  LA PERIODE DE L'ENVELOPPE SOUS LE SEUIL A 2:1, DERIVEE, TENUE A DEUX
       DEGRES ; SA FORME CORRIGEE FALSIFIE SA FORME NAIVE EN AVEUGLE. Sous le
       seuil, la phase resonante tourne au rythme du shift, phi' = -(g/(p Delta))
       a'(J~0) s^(p-2), et max|S| a phi fixe est pi-periodique (2.333 s a 2.024 s
       a p = 6) : P_env = pi p Delta/(g a' s^(p-2)), a'(J~0) = 87.766204 a p = 6,
       aucun parametre. 6|2.00|+1, bandes [0.8, 1.25] P : predit 503.4, 206.2,
       99.4 ; mesure 477.5, 195.0, 95.0 (s = 0.40, 0.50, 0.60) : P2 TENUE 3/3, la
       loi en 1/K tient (a' effectif 92.52, 92.80, 91.86, constant a 1 pour cent)
       mais le coefficient derive est BAS de 4.7 a 5.7 pour cent [H2] (5.42, 5.73,
       4.66 aux trois s ; 5.27 pour cent sur le coefficient) et la modulation
       moins profonde (0.897 a 0.905 pour 0.868). Cause derivee apres coup, du
       meme ordre, sans parametre : le terme resonant deplace l'action le long de
       la rotation, J2(phi) = J2_0 + (b/a')(1 - cos 2phi) >= J2_0 (b/a' = 0.01832,
       4.1 pour cent de J2_0) : periode plus courte, modulation moins profonde ;
       corrige : 476.2, 195.0, 94.1 et 0.894. Puis PREDIT EN AVEUGLE a 8|2.00|+1
       (a' = 487.1433, b/a' = 0.03251, 7.3 pour cent) avec une bande [0.9, 1.1] P
       qui EXCLUT la forme naive : corrigee 1464.5, 324.2, 97.3 ; naive 1683.9,
       372.8, 111.8 ; mesure (lecture gelee, 4 maxima, tranche 10) 1466.67,
       323.33, 100.00 : corrigee TENUE 3/3, naive FALSIFIEE 3/3 ; profondeur
       0.917 a 0.930 pour 0.913 annoncee. Lecture affinee de m2 a 13-20 maxima :
       1464.19, 324.70, 97.83, residus -0.02, +0.15, +0.59 pour cent (s = 0.35,
       0.45, 0.55), croissant avec K, meme signe et meme forme qu'a p = 6 : la
       trace du second ordre, non derivee, rien de gele dessus. (A s = 0.55 sur
       4 maxima le pas de lecture vaut 10.2 pour cent de la periode : aucun
       ecart plus fin n'y est une mesure ; erratum m2, pris.) [DERIVE m1 ;
       MESURE-M2 aveugle]
  A-7  LA PERIODE DE LIBRATION D'UNE CELLULE PIEGEE VA COMME 1/eps. A 5|1.50|+1
       (3:2 exacte, a + b = 5 = p), l'enveloppe est une libration : maxima a 550,
       1550, 2550 pour s0 = 0.20 (eps = g s0^3/Delta = 3.2e-4), tous les ~260 pour
       s0 = 0.30 -- rapport 3.85 pour un rapport d'eps de 3.375, exposant 1.11 a
       la resolution des tranches ; premier apex a une demi-periode ; periode
       dependant du signe (393 a -1). PREDICTION GELEE m1 (f8face8b95486d02) :
       P = C_P/eps, C_P dans [0.26, 0.34], deux s0 neufs, ordre de grandeur et
       loi 1/eps. Run m2 : 2450 (s0 = 0.15, bande [1926, 2519]) et 500 (0.25,
       [416, 544]) : TENUE ; resolution a T = 4 fois la borne haute : 2417 et 483
       a plus ou moins 17, DANS. [H1] C_P = 0.3262 (s0 = 0.15) et 0.3021 (0.25) a
       T = 4 fois la borne haute ; 0.320 (0.20) et 0.2808 (0.30) a la resolution
       d'origine des sondes, non rejoues : la serie n'est PAS homogene en
       resolution. Pente ln P / ln eps = -1.071 sur ces quatre points, -1.050 sur
       les deux resolus seuls ; le chiffre est donne a plus ou moins 0.01 ; la
       decroissance (pente differente de -1) ne depend pas de ce choix : la
       periode depend de l'amplitude, comme un pendule hors de la petite
       oscillation ; lecture, non gelee. [MESURE-M2 ; predit m1]
  A-8  LA "LOI DE TEMPS" t_apex = C/eps EST RETIREE, ET SA VERIFICATION ETAIT
       CIRCULAIRE. Machine 1 l'a ecrite en lisant C = eps t_apex sur DEUX mesures
       (0.496, 2.707) ; machine 2 l'a "verifiee" contre ces deux memes mesures --
       une identite, pas un test (son neuvieme faux controle, verse). Les
       enveloppes du lot la refusent a 7|2.50 (premiers apex 2450, 1050, <= 50
       pour s0 = 0.65, 0.80, 1.00) et ne la soutiennent a 5|1.50 que sur la
       periode de libration (A-7). La quadrature C n'existe pas comme constante
       de cellule. Le seuil de capture par une resonance desaccordee est derive
       (eps b dc/dJ~2 >= |nu| ; s_open = 1.45 a 7|2.50 pour la 2:1) et ne rend pas
       l'ouverture a 0.65 (A-4). [RETIRE des deux cotes]
  A-9  DEUX PREDICTIONS TOMBENT, UNE REGLE MEURT. (i) La regle de parite du
       signe aux rationnels exacts (f5fa6542578ca2ac : le signe atteignant la plus
       grande excursion libre explose le plus bas) : test aveugle m2 sur 48
       paires archivees, 10 directions tenues, 1 falsifiee (9|2.50, 24 pour cent
       dans le mauvais sens) au critere (i) que m1 avait ecrit : MORTE, non
       amendee ; ce qu'elle captait (ou l'asymetrie est grande) n'a pas ete pris
       en defaut ; ses 33 paires sans prediction (w2 ecrits a la main) ont revele
       la marche de A-1. (ii) P-D-2 (b5e0b5230b08d767 ; rang des largeurs
       quantiques E-B a p = 5 dans la fenetre du cusp ordonne par -r_gen) :
       n = 6 (le site exact ne porte pas l'observable), rho = 13/35 sur Gamma_LS
       (p = 179/720), -19/35 sur Gamma_pondere (p = 211/240) : NON TENUE aux
       deux observables, a 29/35 comme a 5/7 ; r_gen authentifies 8/8 au bit par
       les deux voies. Observation versee sans gel : -r_gen ordonne PARFAITEMENT
       Gamma_c (E-A, quantite d'instrument sans verdict au delta 80) sur les six
       cellules (rho = 1, p = 1/720) -- post hoc, six points, pas la cible.
       (iii) La moitie "parite" de P1 a p = 6 etait une tautologie (identite de
       l'integrateur) : gelee par m1, versee comme telle.

nn.3 LES VERDICTS DES PREDICTIONS GELEES, EN UNE TABLE
    prediction      plume  gel                 cellules               verdict                    resolution
    T2 flanc (E)    m1     91d858bbf2da60af    6 paires, 3 familles   TENUE 6/6, aveugle         porte ln 1.02, deux fenetres
    P-D1-4 (D)      m1     2154286e9df56806    3 grilles P-4          branche (b) : 0 noeud      t_exp bruts a 6400
    P-D1-10 (C)     m1     2154286e9df56806    11|6.00 ; 11|2.50      A-6 tient ; NON CONCL.     bissection indefinie
    P-D1-9 (A)      m1     2154286e9df56806    5 GEL + 6 excursion    GEL 5/5 ; excursion FALS.  dans sa fenetre T = 3000
    P1 ile (B)      m1     9537d740be94bf91    6|2.00 deux signes     TENUE (moitie testable)    ratio 1.0, intervalle
    P2 periode (B)  m1     9537d740be94bf91    s = 0.40, 0.50, 0.60   TENUE 3/3                  coefficient bas de 5.5 pour cent
    P2 corrigee     m1     8250dc0a2719ea8c    8|2.00, 3 s            TENUE 3/3, naive FALS. 3/3 aveugle, bande 10 pour cent
    libration       m1     f8face8b95486d02    5|1.50|+1, 2 s0        TENUE, resolue             T = 4 fois la borne haute
    parite signe    m1     f5fa6542578ca2ac    48 paires archivees    FALSIFIEE (9|2.50)         critere (i) de m1
    P-D-2 (R5)      m1     b5e0b5230b08d767    6 cellules M17         NON TENUE                  rho 13/35, -19/35

nn.4 LES RESIDUS -- nommes, non ouverts
  R-R4-1  la GRANDEUR de la marche en signe : non derivee ; l'exposant p-1 ne
          se transporte pas de 2:1 a 3:2 ; second ordre ou seuil du signe fragile.
  R-R4-2  le seuil de l'ile a degre pair : au-dela du premier ordre (a p = 4 la
          (4,2) n'apparait qu'au second ordre contre le shift du premier : un
          seuil en K dont le coefficient demande les series de Lie au second
          ordre, machinerie D1 non detenue par m1) ; K* = 0.347 (p = 4) et
          0.052565 (p = 6) sans loi.
  R-R4-3  le residu O(K) de P2 (croissant avec K a p = 6 et 8, dix fois plus
          petit que la correction d'action) et la derive de C_P (-1.071 en
          pente) : second ordre, derivables, non derives.
  R-R4-4  l'excursion sous seuil (P-D1-9) : la valeur d'apex semble stable la ou
          une excursion existe (1.70 a 1.81 a 7|2.50 pour 1.863 predit ; 1.85 a
          1.89 a 5|1.50), non testee ; son temps n'est pas une constante de
          cellule ; a re-poser sur la periode de libration a un s0 neuf ou sur
          la valeur a un s0 neuf, jamais sur C/eps.
  Ouvert sans run prevu : les quatre. Rien n'est ouvert au sens (P).

nn.5 LES DEFAUTS CONSIGNES (etiquettes de chantier, numeros de serie au depot
     si l'operateur en decide)
  Machine 1 :
  D-R4-1  "84 paires signees" ecrit a la main (lecture fausse de "0/84 aux
          impairs" du delta 86) ; les archives en portent 48.
  D-R4-2  perimetre de w2 ecrit a la main (22 valeurs) au lieu d'enumere des
          archives : 33 paires sur 48 sans prediction, dont toute la fenetre du
          cusp ; regle : un perimetre s'enumere.
  D-R4-3  T = 3000 des tests A transporte de p = 5 a p = 7, 9, 11 sans remise a
          l'echelle : P-D1-9 falsifiee dans sa fenetre par sa propre hypothese
          de temps.
  D-R4-4  gel P-D-2 : n = 7 pour un site sans observable (n = 6, seuil 29/35) ;
          f non nomme ; "Gamma_LS ou Gamma_pondere" ; sans consequence sur le
          verdict.
  D-R4-5  moitie "parite" de P1 (6|2.00) : une tautologie gelee comme prediction.
  D-R4-6  prose de la note D2 : "P_env = 0.6224/s^4" pour 12.886/s^4 (facteur
          20.70) ; la piece opposable (.json) etait juste et c'est elle qui a
          servi. Un nombre en prose non relu, le jour de la regle de le relire.
  D-R4-7  lecture p = 8 : "+2.82 pour cent a s = 0.55" cite comme mesure alors
          que le pas de lecture (10.2 pour cent) est plus grand ; retire.
  D-R4-8  loi t_apex = C/eps ecrite sur deux points (A-8).
  D-R4-9  regle de transit : deux lots partis sans manifeste ni canon (09/09),
          corrige des le lot suivant ; canon annonce en chat, que m2 ne lit
          pas : depuis, tout part dans un lot avec manifeste.
  Machine 2 (versees par elle, reprises telles quelles) :
  E-m2-4  faux controles de feuille, dix en trois jours, dont deux "faux succes
          muets" : une bissection butant sur sa borne lue comme un seuil (test
          de T1) ; C = eps t compare aux deux points qui l'ont defini (A-8). Sa
          regle, prise des deux cotes : un controle dont on ne peut pas ecrire
          l'issue qui le ferait mordre n'est pas un controle.
  E-m2-5  "non concluant de fenetre" ecrit puis retire (A-4) ; enveloppe max de
          |x1|, |x2| au lieu de |S| (faux depart, rattrape avant emission) ;
          F/eps transportee a l'excursion (faux depart, rattrape) ; maximum
          global lu pour premier apex (sonde) ; "quatre maxima" pour deux (note
          de libration, corrige par resolution) ; run_R4_machine2_v1.py edite
          d'un hunk sans renommage (custody declaree).
  Deux machines, trois jours, aucun de ces defauts n'a survecu a la lecture de
  l'autre ; c'est le protocole qui a tenu, pas l'une des deux.

nn.6 A ARBITRER PAR L'OPERATEUR, NON PRIS ICI
  (a) Trois regles de chantier proposees, sans regle nouvelle sous (X) :
      (i) s* = min n'est un seuil que si l'ensemble explosif est un intervalle ;
      sinon la colonne se verse avec son ensemble, sans dln (A-3) ; (ii) tout gel
      de periode ecrit T >= 4 fois la borne haute et le pas de lecture, et aucun
      ecart plus fin que le pas n'est une mesure (A-6, A-7) -- avec son OUTIL [H4],
      faute de quoi elle sera enfreinte encore (trois fois en un jour) : une serie
      de periodes ne se lit que si TOUS ses points sont a la meme resolution ; le
      controle compare chaque ecart au pas de sa propre lecture, et s'ecrit dans
      la feuille, pas dans la prose ; (iii) toute loi
      se verifie a cellule fixee sur des points qui ne l'ont pas definie, et un
      controle porte l'issue qui le ferait mordre avant d'etre joue (A-8, E-m2-4).
  (b) Numeros de serie (E18) pour D-R4-1..9, E-m2-4..5, R-R4-1..4.
  (c) Jambes D et S de P-4 (toujours non jouees) ; P1 a p = 8 (seuil vierge) ;
      la valeur de l'apex a un s0 neuf (R-R4-4) ; la periode de libration a
      7|2.50|+1 (regime different de 5|1.50) : options, aucune demandee.
  (d) Gamma_c : aucun gel avant relecture de ce que la campagne a decide de E-A
      le 07/09 (dossier D1, non detenu par m1).
  (e) Held : rien avant ce depot et la decision de l'operateur ; la phrase
      externe de A-1 (la marche en signe et sa table de parite, tenue en aveugle
      sur trois familles et trois degres) et celle de A-5/A-6 (l'ile du shift a
      degre pair et la periode d'enveloppe derivee) sont les deux candidates.

nn.7 CONSEQUENCES POUR LE REGISTRE ET LA CORRESPONDANCE
  - Le registre recoit deux objets DERIVES tenus en aveugle : la table de parite
    de la marche en signe (A-1) et la periode d'enveloppe du site 2:1 a degre
    pair, avec sa correction d'action (A-6). Eligibles a la chaine (49.5) par
    cet acte ; la seconde a falsifie sa propre forme naive, ce qui est la forme
    la plus exigeante d'un test.
  - La clause A-6 du delta 86 (a + b == p mod 2) est expliquee a tout ordre par
    la parite du hamiltonien (A-5) ; sa partie "a + b < p" et "a + b <= 5" reste
    empirique.
  - R-P4-2 est fermee (A-2). P-D1-9, P-D-2 et la regle de parite sont
    falsifiees et le restent ; la loi de temps est retiree.
  - A p = 5 dans la fenetre du cusp, la ou les seuils sont des nombres de
    fenetre, l'estimateur classique de bord n'ordonne pas les largeurs
    quantiques E-B (R5), alors qu'a p = 7 il en predisait le rang (delta 87) :
    deux verdicts ecrits face a face ; l'hypothese qui les relie n'est pas gelee.
  - Rien de cet acte ne touche la branche quantique au-dela de R5, ni les
    manches M1-M17, ni le chantier constante A.

nn.8 LE CANAL, CONSIGNE COMME PROPRIETE
  - Le canal chat ne traverse pas entre machines : un canon annonce dans un
    message n'est pas annonce ; le manifeste interne fait canon, le brut du ZIP
    est donne a cote ; manifestes a deux puis cinq colonnes (B, brut, octets).
  - Quatorze lots recus et quatorze emis en trois jours, tous confirmes par
    canon, zero perte ; les .log de machine 2 sont CRLF (Python sous Windows),
    verifies au brut, comptes et nommes a chaque manifeste.
  - Les lectures des deux machines sur les memes JSON concordent au chiffre ou
    a la convention pres (tranche, intervalle) ; les differences de convention
    sont declarees, jamais absorbees.
  - Les pieces perdues par la reinitialisation du conteneur m1 (07/09) n'ont
    coute que ce qui se re-derive ; ce qui ne se re-derivait pas (archives G6,
    points M17) est declare detenu d'un seul cote a chaque citation.

nn.9 CE QUE CE DELTA NE FAIT PAS
  Il ne prend aucun numero ; il n'ouvre aucun chantier ; il ne demande aucun
  run ; il ne derive ni la grandeur de la marche, ni le seuil de l'ile, ni le
  second ordre ; il ne gele rien sur Gamma_c ; il ne rouvre aucune prediction
  falsifiee ; il n'edite aucune piece citee (PB-1) ; il ne dit rien du chantier
  constante A ni de la branche quantique au-dela de R5 ; il ne sort rien vers
  Held.

nn.10 PIECES DE CE DELTA (lot machine 1, canon = convention B du manifeste)
  journal_delta_nn_R4R5_v2.md                    cet acte (v1 86d6ee29d27938ff conservee)
  rederive_acte_R4R5_machine1_v1.py / .log       le driver et le log consolide :
                                                 douze feuilles rejouees en un
                                                 passage (chemins de la machine
                                                 1 ; m2 re-derive avec ses feuilles)
  lecture_R4_machine1_v1.py                      E, D, C, A par enumeration
  rederive_D_6400_machine1_v1.py                 D sur t_exp bruts
  rederive_R5_machine1_v1.py                     rho en fractions, p enumeres
  capture_2_1_p7_machine1_v1.py                  seuil de capture (A-8)
  enveloppes_apex_machine1_v1.py                 loi 1/eps a cellule fixee (A-7, A-8)
  lecture_periode_libration_machine1_v1.py       run de libration
  lecture_resolution_machine1_v1.py              resolution a T = 4 fois
  D2_premier_ordre_2_1_pair_machine1_v1.py       r1(p), p_c (A-5)
  D2_prediction_P_D1_5_machine1_v1.py            P_env naive (A-6)
  lecture_voletB_machine1_v1.py                  P1, P2 a p = 6
  correction_action_P2_machine1_v1.py            la correction d'action (A-6)
  prediction_P2_p8_machine1_v1.py                P_env corrigee a p = 8
  lecture_P2_p8_machine1_v1.py                   corrigee contre naive a p = 8
  direction_flanc_machine1_v1.py                 table de parite, 31/31 (A-1)
  Les entrants (JSON de machine 2, gels, attendus) sont ceux de nn.1 ; les
  pieces opposables de machine 1 (f8face8b95486d02, 9537d740be94bf91,
  8250dc0a2719ea8c, f5fa6542578ca2ac) sont dans leurs lots d'origine.

-- FIN journal_delta_nn_R4R5_v2 --
