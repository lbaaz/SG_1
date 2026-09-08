JOURNAL DELTA nn -- LA SEQUENCE P-4 ENTRE AU REGISTRE : LE JUMEAU SANS FANTOME
(MEME MOTEUR, UN SEUL SIGNE CHANGE) N'A NI SEUIL DE FENETRE NI CANYON SUR LES
14 COLONNES SIGNEES JOUEES ; A DEGRE PAIR AUCUNE EXPLOSION (THEOREME, 0 SUR
480) ; A DEGRE IMPAIR UNE BARRIERE D'ENERGIE DERIVEE EN FORME FERMEE PAR LES
DEUX MACHINES, ZERO EXPLOSION SOUS ELLE (0 SUR 1512), QUI BORNE LE SEUIL
MESURE A MIEUX QUE x1.56 SUR ONZE COLONNES ET LE DONNE A LA MAILLE SUR TROIS ;
LES CINQ PREDICTIONS GELEES TIENNENT ; UNE DEPENDANCE EN SIGNE MESUREE,
INVERSEE ENTRE 2:1 ET 3:2, NON DERIVEE ; QUATRE RESIDUS NOMMES, AUCUN
CHANTIER OUVERT
(redaction machine 1, depot operateur, 2026-09-08) -- PROJET, VERSION 1
=======================================================================
S'insere apres le delta 86 (0ff330b, journal_delta_86_sequence_P1_v3
bdd0a7333ca5de18). NUMERO nn PRIS AU DEPOT : plafond releve sur clone frais
lbaaz/SG_1 a HEAD 0ff330b le 08/09 = 86, premier numero libre 87 ; le delta
de la sequence R3 (cce710187ad53e04, certifie machine 2) attend le sien ;
l'ordre 87/88 est de l'operateur, le corps garde "nn" (le numero n'entre que
dans le nom de fichier et le manifeste de depot). Aucun numero de serie (N,
E, D) n'est pris ici ; les defauts portent leurs etiquettes de chantier
(D-P4-x plume machine 2 pour 1 a 3, E-m2-x, R-P4-x) et attendent
l'attribution au depot si l'operateur en decide (E18). Classe du depot : 1
(registre) ; la sequence s'est jouee en classe 2 pour l'instrument (une
machine ecrit, l'autre controle) et en classe 3 pour les derivations et les
lectures, rule (P) ; gel, addendum et precisions de machine 2 deposes AVANT
le run, empreintes en tete du log de run (pre-vol 8/8). Aucune regle nouvelle
((X) jusqu'au 28/09).
Ce projet est de plume machine 1 ; il est a certifier par machine 2 en un
tour avant depot. Chaque nombre de cet acte est RE-DERIVE des pieces de la
section nn.1 par les scripts du lot de ce delta (nn.10), depuis (grille,
t_exp) du JSON e66549fd72f4239b pour les comptes et les seuils, depuis la
forme fermee pour la barriere, et par rejeu au moteur depose (eta = +1, 14
grilles) pour les references fantomes -- aucune valeur de lecture n'est crue.
Moteur unique : m9_replication_v1.py c8ed357b120352c4, charge en lecture
seule, jamais edite (PB-1). Les trois jambes optionnelles (D, S, T = 6400)
sont constatees NON JOUEES ; leur renvoi est a l'operateur (nn.6).

nn.0 POSITION EN TROIS PHRASES
  Avec le seul signe du couplage du mode 1 change dans acc() -- meme moteur,
  meme rayon, memes grilles, memes fenetres T = 400 et 1600 que P-1 -- la
  machinerie ne trouve ni seuil dependant de la fenetre ni canyon sur les 14
  colonnes signees jouees : a degre pair aucune explosion (0 sur 480 points,
  theoreme), a degre impair aucune explosion sous une barriere d'energie
  s_b(w2, p, sgn) derivee en forme fermee (0 sur 1512 points), et les 14
  seuils mesures au-dessus d'elle ne bougent pas de plus d'un pas de grille
  entre T = 400 et T = 1600 (11 exactement au meme indice, 3 a un pas, 0
  au-dela). Au site 2:1, ou le fantome a un cusp de fenetre (33.0 et 20.0
  pas de grille entre les deux memes T), le jumeau n'a aucun seuil sur la
  grille de P-1 et un seuil fixe sur la grille etendue, 2.0 a 4.1 fois plus
  haut que le seuil fantome a T = 400 et 2.6 a 6.6 fois a T = 1600. Fait
  neuf, non gele : la barriere derivee sans run BORNE le seuil du jumeau par
  le bas partout (s*/s_b de 1.0073 a 1.5567 sur onze colonnes) et EST le
  seuil a la maille jouee sur trois ; le jumeau garde une dependance en signe
  qui s'inverse entre w2 = 2.00 et w2 = 1.50, mesuree, non derivee ; quatre
  residus sont nommes, aucun chantier n'est ouvert.

nn.1 LA SEQUENCE ET SES PIECES (convention B, 16 hex ; ordre d'emission ;
     canon d'un lot = convention B de son manifeste interne, sha256 brut du
     ZIP entre crochets ; toutes les pieces de texte sont LF/ASCII sauf
     mention)
  02/09  note critique m1         81ab692160dbcf64  section 5, item 7 : "le temoin
                                                    classique sans fantome" (au delta 86,
                                                    86.1 ; projet, authentifiee 08/09)
  02/09  lot m1 instrument v1     db6054ad58e4ff44  [5107783aa32d1fd5] 11 pieces :
         note v1 3c94af636bd56071 ; instrument integrer_jumeau_machine1_v1.py
         171a02edfbc23864 ; patron integrer_indice.py d303bff2e5e55872
         (reconstitue au bit depuis la conversation P-1 : empreinte du delta
         86) ; derivation de la barriere 80e8280603673992 ; controles
  02/09  lot m2 gel temoin v1     [c351f322a455e4ab] 7 pieces : GEL
         gel_P4_temoin_classique_machine2_v1.md d7eccfbd9b715a6d (21467 o,
         LF, ASCII, brut = B, verifiable par sha256sum) ; derivation m2
         363b3f972d21bf60 (brut ; B d0d190e0bf5fd61a, CRLF). NON PARVENU a
         machine 1 avant le lot addendum v3 (custody, nn.5)
  02/09  lot m2 controle v2       f0f304d0351d592b  [ad2b0440e6f2f768] 6 pieces :
         CONTROLE_machine2_lot_m1_P4_v1.md 7d59cde9b48c0d76 (INSTRUMENT
         CERTIFIE ; D-P4-1 bloquante, D-P4-2, D-P4-3 ; 12 -> 14 colonnes) ;
         controle 76b4e5a89f31c8e5 ; verification des nombres
         c20972fb5efc4801 ; trois pieces CRLF verifiees au BRUT
         2260546cdd13d479, 191d17af09b851d2, 5a1be4a66672c034 (E-m2-1)
  02/09  lot m1 reponse v2        d1ff9faa6e020094  [f1907286e1eb7759] 8 pieces :
         reception 055b56dea8e008fe ; note v2 35aa7ff7176f823b (9 hunks
         sur la v1, non editee) ; reprises 9539f6b4c826fd4e ; banc de
         derive 5b53c2f84a84ef03
  02/09  lot m2 addendum v3       81ddb80ef0433b15  [c1e8a4b553b47d44] 6 pieces :
         ADDENDUM_v2_gel_P4_machine2_v1.md e4d37a4f9ae195d6 ; reception m2
         69416e4bc3b51051 ; gel en clair d7eccfbd9b715a6d ET ZIP imbrique
         c351f322a455e4ab (gel identique au bit dans les deux) ; controle
         du banc de derive m2
  02/09  lot m1 lecture gel v3    fcaa79169534cbea  [ae763220c01bf2e8] 3 pieces :
         note 4d825aeef1b14e2c (tables 14/14 et 14/14, marges 11/11 ;
         deux precisions demandees)
  02/09  lot m2 run v4            3bcac78e23a1d077  [0c86a9cf625bf3d1] 7 pieces :
         NOTE_RUN 02b9f8a807aa0ce6 ; PRECISIONS 918a1ab5112ddf1f (fixees
         avant lecture, run deja lance : exposition declaree, nn.3) ; run
         ea1365396fe38600, log cb22a3e1c3149695 ; JSON e66549fd72f4239b ;
         depouillement bb793be7d4decb3b, log 16b49388caca74bc
  02/09  lot m1 resultat v4       f1d646d9feca7437  [70a43a513f9e0782] 9 pieces :
         note dd6838c0fbbd3a4b ; lecture par enumeration c08bffa3301c533f /
         543092ecbdc6e463 / 08e3ba2aeef92a25 ; rejeu 5939596a716e1f36 ;
         lecture candidate du signe eaaaa8ac096417b8 / b5bc8d1b7277506e /
         9790bc3c54e6b57b ; PREDICTIONS jambe S deb66a426c5959e1 (GELEES,
         NON JOUEES)
  08/09  archive m2 -> m1         les sept lots ci-dessus, octet pour octet
         (MANIFEST_ARCHIVE 77c5fbcb8b040d1d ; POUR_MACHINE1 909bef4ce6cbd9c3 ;
         controle v2 a71b8a344e71733d / a7c412962bb43d52 ; spec de la
         demande m1 8fb9e813713c6283). Reception m1 (nn.10, script et log
         joints) : 4/4 pieces de transmission, 7/7 lots (brut du ZIP, canon,
         taille, pieces contre leur propre manifeste : zero ecart), 26/26
         empreintes nommees retrouvees, 64 pieces (manifestes compris, ZIP
         imbrique deplie).
  Registre lu : clone frais lbaaz/SG_1 a HEAD 0ff330b (delta 86), plafond
  86. Trois empreintes citees par le gel comme sources des ancres et des
  references fantomes ne resolvent pas cote machine 1 et sont declarees
  telles : mesures_classe3.json 8c40ac3a616a44e7, mesures_gel_P1_machine2_
  v1.json bcf2961cfd9d5b40, mesures_gel_regle_amendee_machine2_v5.json
  4e5cd0419d3cc819 (detenues machine 2, hors registre). Les references
  fantomes qu'elles portent sont RE-DERIVEES ici par rejeu (A-4) : elles
  n'ont pas a etre crues. Convention B = sha256 du contenu NFC+LF, 16 hex ;
  pour un fichier LF elle coincide avec le sha256 brut.

nn.2 LES FAITS ACQUIS
  A-1  L'INSTRUMENT : le jumeau est le patron a un signe pres, et c'est
       demontre. integrer_jumeau_machine1_v1.py 171a02edfbc23864 contre
       integrer_indice.py d303bff2e5e55872 : diff textuel hors docstring de
       5 lignes (2 retirees, 3 ajoutees) en trois endroits -- signature
       (mot-cle eta obligatoire, sans defaut), assert eta dans {+1, -1},
       ligne du return de acc() ; 5 noeuds Name(eta) a l'AST, UN SEUL usage
       arithmetique, BinOp(Mult, Name(eta), Name(d1)) ; AST IDENTIQUE au
       patron apres neutralisation de eta * d1 en d1 et retrait de la
       signature et de l'assert ; sur le champ, eta = +1 rend EXACTEMENT
       (egalite, pas tolerance) l'acc du moteur depose et eta = -1 rend
       exactement un -d1/delta ecrit en dur : 24/24 egalites exactes sur 12
       cellules x 200 000 points (re-joue pour cet acte). Le reste de la
       boucle etant identique par l'AST, toute trajectoire l'est : eta = +1
       est identique au bit au moteur depose (controle 6.3 du gel, machine
       2 : 4/4 colonnes 2:1 de la jambe R de P-1, expl ET t_exp au bit,
       T = 1600 ; cote machine 1 : 5 lots P-1 + 12 colonnes). Certifie
       machine 2 (7d59cde9b48c0d76). [classe 2 ; controle m2 ; re-derive
       m1 a l'acte]
  A-2  LA BARRIERE, DERIVEE EN FORME FERMEE, AVANT LE RUN, PAR LES DEUX
       MACHINES SANS SE VOIR (custody : le gel n'a atteint machine 1 qu'avec
       l'addendum). Notations du moteur (W1 = 1, g = 0.05, delta = w2^2 - 1,
       S = x1 + x2) ; energie du jumeau E_j = (v1^2 + x1^2)/2 + (v2^2 +
       w2^2 x2^2)/2 + g S^p/(p delta), partie quadratique DEFINIE POSITIVE
       (le fantome a le signe moins devant le second terme). A degre impair
       le potentiel W(x1, x2) a un seul col : kappa = w2^2/(1 + w2^2),
       S_b = -(delta kappa/g)^(1/(p-2)), E_b = kappa S_b^2 (p-2)/(2p). La
       condition initiale du moteur (v = 0) donne S(0) = sgn s et
       E0(s) = Q s^2 + (g/(p delta)) (sgn s)^p, Q = [(1 + w2^2)^2 +
       4 w2^2]/(2 delta^2) ; s_b(sgn) = plus petite racine de E0(s) = E_b,
       s_b0 = sqrt(E_b/Q) l'approche a -0.12/+0.25 pour cent. S_b = -3.6342
       (5|2.00), -4.0272 (5|2.22), -2.5867 (5|1.50), -2.1689 (7|2.00),
       -2.4198 (7|2.42), -2.4623 (7|2.50), -1.7687 (7|1.50). RECONCILIEES :
       s_b de la derivation m1 (80e8280603673992, deux chemins a 1e-12),
       de la derivation m2 (363b3f972d21bf60) et de la re-derivation de cet
       acte coincident a 4.44e-16 sur les onze colonnes ; E_b(m1) =
       delta x E_b(m2) a 8.88e-16 (deux normalisations du hamiltonien, meme
       physique). La condition (ii) de connexite (le segment 0 -> x0 reste
       sous E0) est derivee par m1 et verifiee m2 11/11 : elle tient pour
       s < s_ii = (2 Q_m1/g)^(1/(p-2)), Q_m1 = delta Q, avec s_ii/s_b de
       2.71 (7|2.50) a 14.41 (5|1.50) -- donc (i) E0 < E_b suffit et "zero
       explosion sous s_b" est un theoreme, pas une attente. Statut :
       derivee des deux cotes, re-derivee une troisieme fois ici ;
       eligible a la chaine (49.5). Portee ecrite au gel : s_b est une borne
       INFERIEURE du seuil ; au-dessus, le gel ne predit rien.
  A-3  DEGRE PAIR : AUCUNE EXPLOSION, THEOREME ET MESURE. p pair : le seul
       point critique de W est l'origine et E_j est une somme de termes
       positifs, |x1| <= sqrt(2 E0), |x2| <= sqrt(2 E0)/w2 ; le plafond ou
       cette borne atteint CAP = 1e4 est s_CAP = 353.66 (4|2.22), 330.56
       (4|2.00), 422.55 (4|3.00), soit 106.7, 110.5 et 38.9 fois le haut
       de la grille de P-1 (le terme g s^p/(p delta) domine : sans lui on
       ecrirait 5304, 4685, 6860, faute D-P4-2). Mesure : 0 explosif sur
       480 points (5 grilles : G_P1 et G_ext a 4|2.22 et 4|2.00, G_P1 a
       4|3.00 dont le 1.15 s_ref = 10.86 depasse HI0 = 6), la ou le fantome,
       memes grilles, explose 10/96 a T = 400 aux trois colonnes (rejoue
       ici). [MESURE-M2 ; rejeu fantome m1]
  A-4  DEGRE IMPAIR SOUS LA BARRIERE, ET LE SITE 2:1. 0 explosif sur 1512
       points de grille situes sous s_b(sgn) (22 grilles, 11 colonnes ;
       compte derive point par point avec la s_b de cet acte). Aux quatre
       colonnes 2:1 sur la grille de P-1, comptes derives de (grille,
       t_exp), jumeau contre fantome REJOUE ICI sur les MEMES 96 valeurs
       de grille, memes T :
         colonne     jumeau       fantome 400 -> 1600      s*_f(400) -> s*_f(1600)   dln f
         5|2.00|+1   0/96, 0/96   10/96 -> 43/96           0.379198 -> 0.237766     -0.4668
         5|2.00|-1   0/96, 0/96   10/96 -> 43/96           0.378468 -> 0.237308     -0.4668
         7|2.00|+1   0/96, 0/96   10/96 -> 30/96           0.397186 -> 0.299320     -0.2829
         7|2.00|-1   0/96, 0/96   10/96 -> 30/96           0.396752 -> 0.298993     -0.2829
       dln fantome = -33.0 et -20.0 pas de grille EXACTEMENT (pas G_P1 =
       ln(1.15/0.3)/95 = 0.014145). Sur la grille etendue G_ext (s_b0 x
       logspace(0.5, 2, 96), pas 0.014593), le jumeau a un seuil, au meme
       indice aux deux T : 1.188317, 1.567994, 0.785172, 0.977298 -- soit
       2.0 a 4.1 fois le seuil fantome a T = 400 (3.13, 4.14, 1.98, 2.46)
       et 2.6 a 6.6 fois a T = 1600 (5.00, 6.61, 2.62, 3.27). Le cusp du
       fantome a 2:1 (delta 86, A-5 : nombre de fenetre, s*(T) =
       (F delta/(g T))^(1/(p-2))) n'a pas d'homologue. Les 14 references
       fantomes du gel (s*_f aux deux T, dln) sont retrouvees par ce rejeu
       14/14, aux cinq decimales de la table du gel et au repr des valeurs
       portees par la derivation m1 : les trois JSON de machine 2 declares
       non resolus en nn.1 ne portent aucun nombre de cet acte que le rejeu
       n'ait re-derive. [MESURE-M2 ; rejeu fantome m1 ; derive m1/m2 pour
       s_b]
  A-5  LE FAIT NEUF, NON GELE : LA BARRIERE EST LE SEUIL, A UN FACTEUR 1.56
       PRES. Sur G_ext, estimateur nomme "premier s explosif de la grille a
       T", s*_j(1600) et rapports (s_b de cet acte ; fantome rejoue) :
         colonne      s_b(sgn)   s*_j(1600)  s*_j/s_b  pas>s_b  1er pt>s_b   expl>s_b  s*_f(400)/s_b  s*_f(1600)/s_b
         5|2.22|-1    1.512281   2.354221    1.5567    30.33    non          18/48     0.807          0.807
         7|2.42|+1    1.092858   1.167926    1.0687     4.55    non          44/48     1.405          1.291
         5|2.00|+1    1.178269   1.188317    1.0085     0.58    OUI          48/48     0.322          0.202
         5|2.00|-1    1.181103   1.567994    1.3276    19.42    non          25/48     0.320          0.201
         7|2.00|+1    0.768065   0.785172    1.0223     1.51    non          47/48     0.517          0.390
         7|2.00|-1    0.768280   0.977298    1.2721    16.49    non          29/48     0.516          0.389
         7|2.50|-1    1.152962   1.285043    1.1146     7.43    non          41/48     1.052          1.052
         5|1.50|+1    0.471130   0.582187    1.2357    14.50    non          34/48     0.826          0.791
         5|1.50|-1    0.471193   0.474611    1.0073     0.50    OUI          48/48     1.282          1.228
         7|1.50|+1    0.351504   0.428043    1.2177    13.50    non          35/48     0.604          0.442
         7|1.50|-1    0.351506   0.354079    1.0073     0.50    OUI          48/48     0.606          0.444
       (0/48 explosifs sous s_b a chaque colonne, deja compte en A-4.) A
       TROIS colonnes (5|2.00|+1, 5|1.50|-1, 7|1.50|-1) les 48 points sous
       s_b n'explosent pas et les 48 au-dessus explosent tous : le seuil est
       dans (dernier point sous s_b, premier au-dessus], intervalle qui
       CONTIENT s_b, et "1.0073" ou "1.0085" est le demi-pas de grille, pas
       un ecart (lecture m2, adoptee) -- a la maille jouee, seuil mesure et
       barriere derivee ne se distinguent pas. A 7|2.00|+1 le premier point
       au-dessus n'explose pas : seuil strictement au-dessus, a 1 ou 2 pas.
       Partout ailleurs s*_j/s_b est entre 1.07 et 1.56 ; 10 colonnes sur
       11 sont sous x1.33, la seule au-dela est 5|2.22|-1 (1.5567, 30.3
       pas). G_P1 donne aussi un seuil a trois colonnes (7|2.42|+1 :
       1.173800 a T = 400, 1.157313 a T = 1600, rapport 1.0590 ; 7|2.50|-1 :
       1.283752, rapport 1.1134 ; 5|1.50|-1 : 0.474829, rapport 1.0077) ;
       ecart entre les deux estimateurs 0.63, 0.07 et 0.03 pas de G_ext,
       coherents. Le rapport fantome/jumeau n'a aucune structure de site :
       s*_f(400)/s_b de 0.32 (5|2.00|-1) a 1.41 (7|2.42|+1) et
       s*_f(400)/s*_j(1600) de 0.24 (5|2.00|-1) a 1.31 (7|2.42|+1) -- la
       barriere ne sait pas ou sont les sites (P4-4, forme m2) ; la ou le
       fantome a son cusp, le jumeau en est le plus loin au-dessus. Les
       trois colonnes nommees AVANT le run au gel (3.4 : 7|2.42|+1,
       5|1.50|-1, 7|2.50|-1, dont 31, 28 et 13 points de G_P1 sont
       au-dessus de s_b) explosent comme le gel le permettait, et deux
       d'entre elles PLUS BAS que le fantome (a T = 400 : 1.1738 contre
       1.5357 ; 0.4748 contre 0.6039) : franchissement de col, dln = 0,
       rien n'est refute. [MESURE-M2 ; comptes re-derives m1]
  A-6  INDEPENDANCE EN T, A LA RESOLUTION D'UN PAS. 14 seuils mesures (11
       sur G_ext, 3 sur G_P1), compares en INDICES entiers de grille (regle
       15) : |i1600 - i400| = 0 pour 11, = 1 pour 3, > 1 pour 0. Les trois
       a un pas : 7|2.42|+1 sur G_P1 (indice 70 -> 69), 5|1.50|+1 sur G_ext
       (63 -> 62), 7|1.50|+1 sur G_ext (62 -> 61) ; ils sont AU BORD de la
       tolerance gelee (un pas), qu'ils satisfont ; le fantome aux memes
       (p, w2, sgn), meme grille G_P1, rejoue ici : dln = -0.0849 (6.0
       pas), -0.0424 (3.0 pas), -0.3112 (22.0 pas). Le cas symetrique
       "s*(400) existe, s*(1600) non" est impossible par construction
       (explosifs a 400 inclus dans explosifs a 1600, meme integration) et
       le compte le confirme : 0. Aucun seuil au premier ni au dernier point
       de sa grille (0 cas de bord). [MESURE-M2 ; compte re-derive m1]
  A-7  LE JUMEAU GARDE UNE DEPENDANCE EN SIGNE, ET ELLE S'INVERSE. A
       w2 = 2.00 le signe +1 colle a la barriere (s*_j/s_b = 1.0085 ; 1.0223
       aux degres 5 et 7) et -1 s'en ecarte (1.3276 ; 1.2721) ; a w2 = 1.50
       c'est l'inverse : -1 colle (1.0073 ; 1.0073), +1 s'ecarte (1.2357 ;
       1.2177). Le MOTIF se reproduit aux deux degres ; les valeurs, non.
       s_b ne porte le signe qu'a |s_b(+1) - s_b(-1)|/s_b0 <= 2.4e-3 (5|2.00 ;
       2.8e-4, 1.3e-4, 4.9e-6 aux trois autres cellules), sous un pas : la
       dependance est dans la DYNAMIQUE. Elle n'etait visible qu'a 14
       colonnes (a 12 il manquait un signe a chaque cellule 3:2 ; c'est la
       raison que machine 2 avait donnee avant le run, 7d59cde9b48c0d76 3).
       MESUREE, NON DERIVEE. Lecture candidate m1 (classe 3, ecrite APRES le
       run, non gelee, non opposable ; re-derivee ici) : l'excursion
       lineaire du rayon vers x < 0, x_lin(t)/s = sgn [(1 + w2^2) cos t -
       2 cos(w2 t)]/delta, minimum sur [0, 400] : 2:1 +1 -2.3333 s /
       -1 -1.1875 s ; 3:2 +1 -3.3993 s / -1 -4.2000 s ; incommensurables
       2.22 : -2.0178 / -2.0182 s, 2.42 : -1.8234 / -1.8237 s, 2.50 :
       -1.5926 / -1.7619 s. Regle lue : le signe a la plus grande excursion
       colle a la barriere ; 4/4 sur les paires jouees, APRES COUP. Ce que
       cette lecture ne donne pas : les valeurs (s_lin(sgn) = |S_b|/|min
       x_lin| donnerait 1.32 et 2.59 s_b a 5|2.00, contre 1.0085 et 1.3276
       mesures). Trois predictions ORDINALES hors echantillon en ont ete
       GELEES pour les signes non joues (deb66a426c5959e1, NON JOUEES ;
       nn.6 b) : 7|2.50|+1 -> s*(+1)/s_b > 1.1146 (excursion -1.5926 contre
       -1.7619 au signe joue) ; 5|2.22|+1 -> ~ 1.5567 a peu de pas pres
       (excursions au rapport 0.9998) ; 7|2.42|-1 -> ~ 1.0687 a peu de pas
       pres (rapport 1.0002). "A peu de pas pres" n'est pas derive ;
       l'ordinal l'est, au lineaire. [MESURE-M2 ; CANDIDAT m1]
  A-8  L'ATTENTE MACHINE 1, HORS GEL, VERSEE TELLE QUELLE : s_b <= s*_j <=
       s_lin (s_lin non derive, exclu du gel par la 6.4 de m1 et par
       l'addendum). La borne basse DERIVEE tient 11/11 ; la borne haute
       tombe a 4 colonnes sur 11 -- 5|2.22|-1 (1.5567 contre s_lin/s_b =
       1.2878), 5|2.00|-1 (1.3276 / 1.2894), 7|2.00|-1 (1.2721 / 1.1831),
       7|1.50|+1 (1.2177 / 1.1832) -- toutes du cote "qui s'ecarte" de A-7.
       Une seule valeur par cellule, calculee sur l'ellipse d'energie sans
       le signe, ne pouvait pas porter une dependance en signe.

nn.3 LE VERDICT DU GEL ET SA PORTEE EXACTE
  Gel d7eccfbd9b715a6d (m2, quatre predictions P4-1 a P4-4, 14 colonnes,
  deux T) + addendum e4d37a4f9ae195d6 (m2, P4-5 sur G_ext en trois branches
  exclusives, 27 grilles, garde de derive 1.1e-3 = marge_min/10) +
  precisions 918a1ab5112ddf1f (m2, forme executable de 6.1 (i) : 5 lignes
  et non 1 ; cas de bord (d) et (e)) : tous emis AVANT toute lecture. Les
  deux jeux de predictions -- m2 au gel, m1 en 6.2 de sa note -- ont ete
  ecrits SANS SE VOIR (le gel n'avait pas atteint m1) et se recoupent :
  P4-4 = P-b, P4-3 = P-a, P4-5 = P-c v2 (la branche (c), issue de la
  D-P4-1 de m2, adoptee mot pour mot par m1). Accident heureux, pas
  methode ; consigne.
    cle            enonce gele                                   compte derive (cet acte)         verdict
    P4-3           degre pair : 0 explosion a tout s             0 / 480 points, 5 grilles        TIENT
    P4-4, P4-5(a)  impair : 0 explosion sous s_b(sgn)            0 / 1512 points, 22 grilles      TIENT
    P4-2           2:1, G_P1 : aucun s* (fantome 43/96, 30/96)   0/96 aux quatre colonnes         TIENT
    P4-1           aucun echappement resonant : toute explosion  toutes a s >= s_b ; aucune ne    TIENT
                   a s >= s_b, sans arithmetique de w2           descend en T au-dela d'un pas
    P4-5(b)        si s*(T) existe, |i1600 - i400| <= 1          14 seuils : 11 a 0, 3 a 1, 0 > 1 TIENT
    P4-5(c)        colonne impaire sans s* sur G_ext             0 (les 11 ont un seuil)          --
    P4-5(d), (e)   cas mixte ; seuil au bord haut ; au bord bas  0 ; 0 ; 0                        --
    garde          derive relative de E+ <= 1.1e-3               max 5.12e-8 (4|3.00|+1 G_P1),    PASSE
                                                                 27/27 grilles
  SUCCES au sens du gel (5, a-d) et de l'addendum : les cinq tiennent ;
  aucune colonne NON CONCLUANTE, aucune non resolue au bord. La garde est
  a quatre ordres de la derive mesuree ; la marge d'energie la plus serree
  du dernier point de grille sous s_b (G_P1 U G_ext) est 1.1288 pour cent a
  7|2.50|-1, dont le dixieme (1.13e-3) majore la garde gelee (la garde a 1
  pour cent du gel initial, retiree par l'addendum, aurait ete a 0.89 de
  cette marge). Estimateur nomme partout (premier s explosif de la grille a
  T, jamais la bissection, A-7 ii du delta 86) ; comparaisons en T faites
  en indices entiers, jamais sur des flottants (regle 15). EXPOSITION
  DECLAREE par m2 (precisions, 3) : le run tournait quand la demande de
  precisions de m1 est arrivee ; 11 des 27 lignes de grille etaient vues ;
  aucune n'etait du type que (d) ou (e) resout, ce que le depouillement
  confirme (0 cas mixte, 0 bord) ; les precisions ne pouvaient pas etre
  formees par les donnees vues. Consigne tel quel, avec la lecon : une
  precision de lecture se demande avec la lecture du gel, avant le
  lancement. Lignee d'instrument au run : pre-vol 8/8 empreintes (moteur,
  patron, instrument, banc, gel, addendum, derivation m2, jambe R de P-1),
  numpy 2.2.6, python 3.11.9, PYTHONUTF8=1 ; controle 6.3 4/4 au bit ; banc
  de derive authentifie sur une grille de la carte (7|2.50|-1 G_ext, 41
  explosifs, (expl, idx) au bit) ; 27 grilles en 354 s ; compte en forme
  derivee "explosifs + non explosifs == 96" sur 27/27 ; rejeu m1 eta = -1
  sur les valeurs de grille du JSON : 8 grilles au bit le 02/09
  (5939596a716e1f36), 2 de plus au bit pour cet acte.
  CE QUE LE SUCCES AUTORISE A DIRE, ET RIEN DE PLUS (phrase externe) :
    "La meme machinerie -- meme moteur, meme rayon, memes grilles, memes
    fenetres T = 400 et 1600 -- avec le seul signe du mode 1 change, ne
    trouve ni seuil dependant de la fenetre, ni canyon, la ou le fantome
    est absent : a degre pair elle ne trouve aucune explosion du tout, ce
    qui est un theoreme ; a degre impair elle retrouve une barriere
    d'energie, derivee en forme fermee par deux machines independamment,
    qui ne sait pas ou sont les sites, borne le seuil mesure par le bas a
    mieux qu'un facteur 1.56 sur onze colonnes et le donne a la maille sur
    trois. Au site 2:1, ou le fantome a un cusp de fenetre (33 et 20 pas
    de grille entre T = 400 et 1600), le jumeau a un seuil fixe, 2.0 a 4.1
    fois plus haut a T = 400 et 2.6 a 6.6 fois a T = 1600, qui ne bouge
    pas d'un pas."
  Qualifieurs obligatoires, dans la meme phrase quand elle sort :
    (q1) 14 colonnes signees ISOLEES, pas un balayage en w2 : "ni canyon"
         est une phrase sur 14 points tant que la jambe D n'est pas jouee ;
    (q2) rien au-dessus de 2 s_b0 ni au-dela de HI0 = 6 au degre pair ;
    (q3) l'independance en T est testee a la resolution d'un pas de grille
         entre 400 et 1600 ; trois colonnes sont au bord de cette tolerance ;
    (q4) la clause A-6 du delta 86 (quels sites sont directs chez le
         fantome) reste empirique ; le jumeau n'en dit rien sinon qu'il n'a
         pas de clause de site ;
    (q5) les valeurs s*/s_b au-dessus de 1 et la dependance en signe sont
         mesurees, non derivees ; le motif du signe est une lecture
         candidate, ses trois predictions gelees ne sont pas jouees.

nn.4 LES RESIDUS -- nommes, non ouverts (portes tels quels de la note
     dd6838c0fbbd3a4b, 7)
  R-P4-1  dependance en signe : motif lu au lineaire (A-7), valeurs non
          derivees ; trois predictions gelees (deb66a426c5959e1), non
          jouees.
  R-P4-2  trois seuils a |d_indice| = 1 entre 400 et 1600 (7|2.42|+1 G_P1,
          5|1.50|+1 G_ext, 7|1.50|+1 G_ext) : resolution d'un pas ;
          T = 6400 sur ces trois grilles separerait une derive lente d'un
          bord crible (3 integrations, ~4 min BOCAL4).
  R-P4-3  s*_j/s_b jusqu'a 1.56 : confinement au-dessus de l'energie du
          col, non derive (tores ? note 81ab692160dbcf64, 2.1) ; largeur de
          la bande criblee du jumeau non mesuree (coherence des deux
          estimateurs 0.03 a 0.63 pas : bandes etroites, sans plus).
  R-P4-4  jambe D (balayage en w2 autour de 2:1 a p = 5, gel section 8) non
          jouee : prediction de machine 2 deja gelee -- zero explosion en
          tout point de la fenetre du cusp sur la grille de P-1.
  Ouvert sans run prevu : les quatre. Rien n'est ouvert au sens (P).

nn.5 LES DEFAUTS CONSIGNES (etiquettes de chantier ; numeros de serie a
     l'acte si l'operateur en decide)
  D-P4-1 (m1, BLOQUANTE, relevee m2)  la prediction P-c v1 de m1 exigeait
       l'EXISTENCE d'un s* sur G_ext comme condition de succes, alors que
       sa propre 5.5 declarait legitime "seuil > 2 s_b0" : un succes pouvait
       se lire comme un ECHEC ; l'existence d'un s* sur G_ext n'est pas
       derivee (c'est l'attente s_lin, hors gel). Reprise en trois branches
       (a)(b)(c), adoptee mot pour mot en 6.2 de la note v2 et gelee comme
       P4-5 par l'addendum. Aucune prediction du dossier n'exige qu'une
       explosion ait lieu.
  D-P4-2 (m1, relevee m2)  plafond pair ecrit sans le terme g s^p/(p delta)
       de l'energie du rayon : "s > 4.7e3" pour ~3.3e2 (A-3) ; sans effet
       sur les grilles (HI0 = 6), retire de la v2, s_CAP re-derives 3/3.
  D-P4-3 (m1, relevee m2)  libelles de compte : "diff = 3 lignes" pour 3
       ENDROITS et 5 lignes ; "eta apparait trois fois" pour 5 noeuds Name
       et un usage arithmetique. Un nombre de perimetre ne s'ecrit pas a la
       main, meme petit. Corriges en v2, script non reedite (erratum a
       l'acte).
  D-P4-4 (m1, relevee A L'ACTE)  la note dd6838c0fbbd3a4b, 4.3, ecrit
       "s*_f/s*_j de 0.32 a 1.32" : la plage re-derivee de s*_f(400)/
       s*_j(1600) est 0.24 (5|2.00|-1) a 1.31 (7|2.42|+1) ; 0.32 est la
       valeur de la seule colonne 5|2.00|+1 (et celle de s*_f(400)/s_b).
       Plage trop etroite, meme sens ; la note n'est pas editee (PB-1),
       l'acte porte la valeur juste (A-5).
  E-m2-1 (m2, relevee m1)  en-tete de manifeste "convention B" sur des
       empreintes BRUTES ; trois pieces CRLF du lot controle v2 (175, 58, 51
       fins de ligne CR : comptes retrouves trois fois, m1 02/09, m2 08/09,
       m1 08/09), a verifier au brut ; le gel lui-meme est LF, brut = B.
       Correctif m2 : manifestes a deux colonnes (brut, B), sorties
       newline LF. Le lot de certification du delta 86 porte le meme
       en-tete mais ses pieces de texte sont CR = 0 : aucune empreinte du
       registre n'est touchee.
  E-m2-2 (m2, relevee m1)  10 lignes, 28 octets non ASCII (guillemets
       typographiques) dans CONTROLE_machine2_lot_m1_P4_v1.md ; gel et
       addendum a 0 octet > 127.
  E-m2-3 (m2, sur elle-meme)  une sonde "grep -cP ... || echo 0" a rendu
       un FAUX NEGATIF sur E-m2-2 : grep -P indisponible, l'echec avale,
       "nonASCII=0" lu sur douze fichiers dont celui qui en portait 28. Une
       sonde qui ne peut pas echouer bruyamment fabrique un succes.
  Clause 6.1 (i) du gel (m2)  "exactement une ligne differente" decrivait un
       signe ecrit en dur, pas l'instrument certifie (eta) ; lue a la lettre
       elle faisait tomber l'instrument ; remplacee par la forme executable
       (5 lignes, 3 endroits, 1 usage, AST identique, 24 egalites) dans les
       precisions, AVANT lecture, portee par le controle 7d59cde9b48c0d76.
  Custody du gel  le gel d7eccfbd9b715a6d n'a pas atteint machine 1 avant
       l'addendum (declare deux fois par m1, une fois par m2) ; les deux
       jeux de predictions ont ete ecrits sans se voir (nn.3). Le canal
       perd ; une piece detenue d'un seul cote se declare a la citation.
  Faits de chantier m1  bloc d'ouverture de sa plume : "canal compact" en
       enonce global a degre impair (faux : le jumeau impair a un col, reprise
       R-1 de m2) et les predits -0.462 / -0.277 de la forme naive cites
       comme mesures fantomes (les mesures sont -0.46677 / -0.28289, reprise
       R-2 de m2) ; marge de garde calculee sur G_ext seule (1.46 pour cent,
       garde 1.5e-3) au lieu de G_P1 U G_ext (1.1288 pour cent, 1.1e-3),
       reprise m2 adoptee ; banc de derive v1 ECHEC 2/4 (amplitude d'echange
       sous-estimee d'un facteur 3, tolerance non relachee, v2 4/4 sur
       amplitude re-derivee) ; attente s_lin fausse par le haut 4/11
       (declaree attente, hors gel, versee telle quelle, A-8) ; demande de
       precisions de lecture arrivee apres le lancement du run (nn.3).
  Faits de chantier m2  exposition declaree 11/27 (nn.3) ; controle de
       l'archive du 08/09 : sa premiere feuille a rendu trois "a lever",
       sept "absentes" et trois "ecarts" qui n'existaient pas (membres
       comptes pour pieces, entrants controles confondus avec pieces
       contenues, convention B imposee a des empreintes brutes) -- declares
       par elle et corriges en v2 avant envoi ; lecon consignee : un
       controle qui compte juste peut encore conclure faux.
  Transit  D-REPRISE-1 (m1, deja versee) : le conteneur de machine 1 a ete
       reinitialise entre chats ; les quatre lots m1 de P-4 ont transite
       vers machine 2 par l'operateur et figurent aussi dans les cartes de
       fichiers du chat P-4 ; aucune perte. Question du canon de
       l'instrument v1 levee par m2 : db6054ad58e4ff44 est le CANON
       (convention B du manifeste), 5107783aa32d1fd5 le sha256 BRUT du ZIP ;
       les deux memoires etaient justes et designaient deux objets.

nn.6 A ARBITRER PAR L'OPERATEUR, NON PRIS ICI (decisions ouvertes a
     l'ouverture de cet acte ; les faits sont constates, les renvois ne
     sont pas ecrits a leur place)
  (a) JAMBE D -- NON JOUEE. Gel d7eccfbd9b715a6d, section 8 : balayage en w2
      a p = 5 dans la fenetre du cusp de P-1 (|w2 - 2| <~ 0.15, points deja
      archives), memes grilles, T = 400 et 1600 ; prediction gelee "zero
      explosion en tout point de la fenetre". Le nombre de points n'est
      ecrit nulle part dans les pieces : "8" est le numero de la section du
      gel, non un compte ; la note de resultat estime 3 a 10 colonnes,
      ~5 min BOCAL4. Tant qu'elle n'est pas jouee, (q1) accompagne la
      phrase externe. Renvoi ou abandon : operateur.
  (b) JAMBE S -- NON JOUEE. Trois integrations G_ext (7|2.50|+1, 5|2.22|+1,
      7|2.42|-1), ~1 min BOCAL4, contre les trois predictions ordinales
      gelees deb66a426c5959e1 ; ne se joue qu'APRES un gel de machine 2 qui
      reprend ces trois lignes. Si 7|2.50|+1 colle (s*/s_b < 1.1146) la
      lecture candidate est FAUSSE et se verse telle quelle ; si les deux
      incommensurables s'ecartent de plus de 3 pas entre signes, elle est
      incomplete. Renvoi ou abandon : operateur.
  (c) T = 6400 -- NON JOUE -- sur les trois grilles de R-P4-2 (3
      integrations, ~4 min BOCAL4), ou renvoi aux tests D1 de machine 2
      (P-D1-4, qui joue T = 6400) : operateur.
  (d) Ordre de depot avec le delta R3 (cce710187ad53e04, certifie) : 87/88 ;
      le corps de cet acte ne change pas.
  (e) Attribution de numeros de serie aux etiquettes D-P4-1..4, E-m2-1..3,
      R-P4-1..4 (E18) : operateur.
  (f) Propositions de forme, sans regle nouvelle sous (X) : (i) tout
      manifeste porte deux colonnes, brut et B, et nomme la voie de
      verification de chaque piece (deja applique par m2 depuis le 02/09) ;
      (ii) tout s* cite nomme sa grille ET son estimateur (les deux grilles
      donnent des seuils distincts a trois colonnes, A-5) ; (iii) toute
      piece detenue d'un seul cote se declare a la citation, avec sa voie
      de re-derivation si elle existe (nn.1).

nn.7 CONSEQUENCES POUR LE REGISTRE ET LA CORRESPONDANCE
  - Le registre recoit son premier temoin classique SANS fantome au meme
    rayon, memes grilles, memes T que la carte : la dependance en fenetre
    (cusp 2:1, delta 86 A-5), la structure de site (clause A-6, empirique)
    et les canyons ne survivent pas au changement du seul signe qui fait le
    fantome. La manche "temoin negatif" de la file (28/08 : "scales sans
    fantome ?") recoit ici sa reponse CLASSIQUE : sans fantome, ni fenetre
    ni site sur 14 colonnes ; ce qui reste de la question est quantique
    (C2) et n'est pas touche.
  - Dossier trilemme du site : la barriere, seule quantite derivee, n'a
    aucune structure de site (s*_f(400)/s_b de 0.32 a 1.41 sans ordre) ;
    indice que la structure de site appartient au fantome, pas une
    derivation. Rien n'est ajoute au dossier ici.
  - Pour la relance Held (note e f03ca623 seulement, D5 ; rien ne sort
    avant le depot de ce delta) : la phrase externe de nn.3 avec (q1) a
    (q3), la formule de la barriere (kappa, S_b, E_b, Q, E0, s_b de A-2 ;
    en notation m1 equivalente : |x_s|^(p-2) = delta w2^2/(g (1 + w2^2)),
    E_b = g |x_s|^p (p-2)/(2p), s_b racine de s^2 Q + sgn (g/p) s^p = E_b,
    avec E_b et Q multiplies par delta) et les deux tables de A-4 et A-5.
    Rien de A-7 avant la jambe S.
  - Rien de cette sequence ne touche la branche quantique ni les manches
    M1-M17 ; R-1, R-2 et la clause d'ordre du delta 86 restent FERMES ; la
    lecture P6(i) de M17 retiree (C-D1-2) le reste.

nn.8 LE CANAL, CONSIGNE COMME PROPRIETE
  - Un conteneur reinitialise ne perd rien de ce qui a ete presente dans
    un chat (cartes de fichiers) ni de ce qui a transite par canon vers
    l'autre machine ; les 4 lots m1 de P-4 sont revenus par les deux voies,
    aux memes canons.
  - Regle de transit appliquee des deux cotes le 08/09 : canon annonce dans
    le message, reception confirmee par le recepteur avant la livraison
    suivante ; l'archive de sept lots a voyage en un envoi avec un manifeste
    d'emission a deux empreintes par lot (brut du ZIP, canon interne).
  - Les ZIP sont preserves par le canal, y compris imbriques : le gel est
    identique au bit en clair et dans c351f322a455e4ab.
  - Fichiers CRLF (E-m2-1) : leur empreinte B differe de leur brut ; un
    manifeste doit dire laquelle il porte ; les comptes de CR sont
    reproductibles (175/58/51, trois fois).
  - Plateforme : numpy 2.2.6 (BOCAL4, run) contre 2.4.4 (bac a sable m1,
    cet acte) ; les 2592 valeurs de grille recalculees par logspace : 2465
    identiques au bit, 127 a moins de 5e-16 relatif (le 02/09, avec le numpy
    du jour, m1 en comptait 921 a 1 ulp) ; le rejeu sur les valeurs de
    grille du JSON est au bit (10/10 grilles en deux dates) et le rejeu
    fantome retrouve 14/14 references : l'indice d'echappement ne depend
    pas de la plateforme (delta 86, 86.8).
  - Une figure fondee : "gel, 8" designe une section, pas un compte (nn.6
    a). Un nombre qui n'est joue par aucune cellule des pieces ne se cite
    pas.

nn.9 CE QUE CE DELTA NE FAIT PAS
  Il ne prend aucun numero ; il n'ouvre aucun chantier ; il ne joue aucun
  run (les seules integrations faites pour l'ecrire sont des rejeux : 2
  grilles du jumeau au bit, 14 grilles du fantome pour re-deriver les
  references) ; il ne tranche ni la jambe D, ni la jambe S, ni T = 6400, ni
  l'ordre de depot ; il ne promeut aucune lecture candidate (A-7) en chaine ;
  il n'edite aucune piece citee par empreinte (PB-1), la note de resultat
  incluse (D-P4-4 vit ici) ; il ne dit rien au-dessus de 2 s_b0, rien hors
  du rayon du moteur, rien de la branche quantique.

nn.10 PIECES DE CE DELTA (lot machine 1, canon = convention B du manifeste)
  journal_delta_nn_P4_v1.md                           cet acte
  reception_archive_P4_machine1_v1.py / .log          reception des 12 fichiers du 08/09
                                                      (4/4, 7/7, 26/26, 64 pieces)
  rederive_P4_acte_machine1_v1.py / .json / .log      comptes et seuils depuis (grille,
                                                      t_exp) ; s_b en forme fermee ;
                                                      controle champ a champ du JSON : 0 ecart
  rejeu_et_fantome_acte_machine1_v1.py / .json / .log rejeu jumeau 2 grilles au bit ;
                                                      fantome rejoue aux quatre 2:1
  fantome_reste_acte_machine1_v1.py / .json / .log    fantome rejoue aux dix autres G_P1
  rederive_complements_acte_machine1_v1.py / .json / .log
                                                      marges, s_CAP, condition (ii),
                                                      attente s_lin, excursions
  perimetre_instrument_acte_machine1_v1.py / .log     diff, eta, AST, 24/24 sur le champ
  Les scripts prennent en premier argument la racine ou les sept lots sont
  extraits (un dossier par lot, nom du ZIP sans extension) ; le moteur est
  charge par charge_moteur.py du lot instrument (chemin BOCAL4 a
  substituer, comme au 02/09). Machine 2 rejoue ce qu'elle veut ; les
  nombres de cet acte sont ceux des logs joints.

-- FIN journal_delta_nn_P4_v1 --
