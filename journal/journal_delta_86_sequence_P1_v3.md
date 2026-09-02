JOURNAL DELTA 86 -- LA SEQUENCE P-1 ENTRE AU REGISTRE : LE TEMPS D'ECHAPPEMENT
AUX SITES DIRECTS EST UNE QUADRATURE DU PREMIER ORDRE RESONANT (VERIFIEE AU
DEMI-POUR-CENT AU SITE 2:1, DEGRES 5, 7, 9, DEUX PREDICTIONS AVEUGLES), LE
FOND DU CANYON 2:1 EST UN
NOMBRE DE FENETRE, LA CLAUSE D'ORDRE TOTAL EST EMPIRIQUE (30/30), ET
L'HYPOTHESE DE VERROUILLAGE EST REFUTEE LA OU ELLE ETAIT TESTABLE
(redaction machine 1, depot operateur, 2026-09-02) -- VERSION 3 (DEPOSEE)
=======================================================================
Remplace les versions 1 (c234b44f12ed960d) et 2 (e5d56ef55800c2ef),
non editees, PB-1. La v2 integrait les trois corrections de la
certification machine 2 v1 (4f7c52ac9279f161) ; la certification v2
(928c9e67ede3e30e) a releve que C-1 et C-3 y etaient MAL REFERMEES --
un critere contenant son propre resultat, et une explication fausse.
Cette v3 applique C-1' et C-3' dans la formulation de cette
certification : DEUX HUNKS, en 86.2 A-3 et 86.2 A-5, et rien d'autre.
Application mecanique de plume machine 2 ; la redaction reste machine 1.
Aucun resultat, aucun chiffre, aucune empreinte n'est touche.
S'insere apres le delta 85 (a4a907a, journal_delta_85_deux_bancs_alpha_
verifie_v2). NUMERO 86 PRIS A L'ACTE au depot (N-68), sous reserve
qu'aucun delta n'ait ete depose apres a4a907a (git log au depot).
Aucun numero de serie (N, E, D) n'est pris ici : les files
libres releves sur l'arbre a4a907a sont N > 70, E > 45, D-M17 > 58 ; les
defauts de cette sequence portent leurs etiquettes de chantier (D-P1-x,
plume machine 2) et attendent l'attribution au depot si l'operateur en
decide. Classe du depot : 1 (registre) ; la sequence elle-meme s'est
jouee en classe 3 (chantier hors chaine, rule (P)), avec des gels courts
de machine 2 deposes AVANT leurs runs, empreinte en tete de chaque log.
Ce projet est de plume machine 1 ; il est a certifier par machine 2
avant depot (elle a redige l'acte 26056845c8af61cf que ce delta reprend
avec son contreseing e4997594734239f1 et son annexe 1e4f296c38accfcb).
Moteur unique de toute la sequence : m9_replication_v1.py
c8ed357b120352c4, charge tel quel, jamais edite (PB-1).

86.0 POSITION EN TROIS PHRASES
  Aux cellules ou l'echappement est direct, le temps d'echappement est
  t = F/eps + B avec eps = g s^(p-2)/(w2^2 - 1) et F une quadrature, sans
  parametre, du seul terme resonant du premier ordre, verifiee a mieux
  que 0.6 % sur les six colonnes bien conditionnees -- qui sont toutes le
  site 2:1, aux degres 5, 7 et 9, deux signes -- dont deux predites en
  aveugle, et a -0.35 % a un second site, (3,2;7) signe +1 ; en
  consequence, les seuils du registre a 2:1 aux degres
  impairs (5|2.00 = 0.3745, 7|2.00 = 0.392) sont des nombres de fenetre,
  s*(T) = (F delta/(g T))^(1/(p-2)), et le "canyon 2:1" est un cusp.
  Quelles cellules sont directes est une clause empirique, 30/30, sans
  derivation d'aucun cote : p impair, a + b == p mod 2, a + b < p
  (strict), a + b <= 5. L'hypothese de verrouillage qui aurait fait de
  cette clause une propriete de la fenetre est refutee aux deux cellules
  ou elle etait testable (T = 3e5 et 1e5) ; deux residus sont nommes,
  aucun chantier n'est ouvert.

86.1 LA SEQUENCE ET SES PIECES (convention B, 16 hex ; ordre d'emission)
  02/09  note critique m1            81ab692160dbcf64  pre-enregistrement des
                                                       discriminants (2.4-2.9, 3.2-3.4)
  02/09  note P-1 m1 v1              b042883e0a105a3e  archives + bac a sable
  02/09  lot m2 v1                   5afab74c2730cfce  controle 1a7879842846b4de,
         gel 1cd65f61529ad85e, JSON bcf2961cfd9d5b40 (canon hors duree
         c9fc0815cba888dc), sonde 3:1 b2e1ec8cd4169e75
  02/09  reponse m1                  c8fb920be2c08036  + note P-1 v2 9216f09b29023e23
  02/09  lot m2 v2                   9284c14b4ca57352  le cusp : gels 0435cebc98d510a2,
         c9ffb7fd5e38799e, 491ca6d38439f8dc ; note 3cb68a9967a3cdf3
         [recu par m1 seulement a la reemission, voir 86.8]
  02/09  lot m2 v3                   bf50c1f655156eba  regle amendee : note
         afc65e62ff11c301 ; gels f4c5b267c5c4d0f9, d44bef9ec1ae9058,
         77ce74da8b87f373
  02/09  lot m1 reponse v3           e61c778c1e21a68b  note 321d25b58df6a23d ; modele
         reduit d92c637e26a79d23 ; diagnostic e14d97314d018e44 ; test
         0a988a04e86e1ab1
  02/09  lot m2 v4                   037ea9a9cde7449e  ordre total p = 11 : gel
         31010d29a32dd002 ; note 512d78c7cd263b24  [idem 86.8]
  02/09  lot m2 v5                   d50fcb63f3a2e723  controle du modele : note
         dc4aa58a40bbe411 ; quadrature a0fad324b9d71d0a
  02/09  lot m2 v6                   0593135a48fad5cf  ACTE 26056845c8af61cf ; gel
         0daa050643ec8739 ; controle de derive 12380e109ac70b86
  02/09  contreseing m1              e4997594734239f1
  02/09  lot m2 v7                   e1f06224cc9f0abb  ANNEXE 1e4f296c38accfcb
  02/09  reemission m2 (v2 + v4)     62a9850e43133478  ZIP imbriques, test de canal
  Registre lu : clone public lbaaz/SG_1 a HEAD a4a907a ; JSON M10-M16
  extraits et re-verifies champ a champ (289/289 apres R-B).
  Deux empreintes appellent une note (certification 4f7c52ac9279f161,
  section 1) : c9fc0815cba888dc n'est PAS un fichier -- c'est le canon
  du JSON bcf2961cfd9d5b40 calcule HORS champ `duree` (json.dumps,
  sort_keys, ensure_ascii), recalculable, non versable ; et
  e61c778c1e21a68b (ZIP de reponse m1) ne resout que dans Downloads,
  pas dans BOCAL4 : si le delta le cite au registre, l'operateur verse
  le ZIP lui-meme. Certification : 41 empreintes citees, 41 resolvent.

86.2 LES FAITS ACQUIS (A-1 a A-7 de l'acte, avec les trois precisions de
     statut du contreseing, adoptees a l'annexe)
  A-1  Aux cellules directes, t = F/eps + B, avec eps = g s^(p-2)/delta
       le seul endroit ou s entre (covariance exacte du pas RK4 a dt
       fixe ; le plafond CAP devient CAP/s). L'invariant est eps t.
       [derive m2 ; verifie]
  A-2  F est DERIVE, sans parametre : quadrature du seul terme resonant
       du premier ordre, F = G = int_{J20}^inf dJ2 / (b sqrt(c(J)^2 -
       c(J20)^2)) le long de la ligne de niveau c cos(phi) = c0 cos(phi0),
       invariant du canal I = b J1 - a J2 (indefini), c(J) = (2/p)
       sum_{m+n=p, m>=a, n>=b, parites} C(p,m) C(m,(m-a)/2)
       C(n,(n-b)/2) 2^-p (2J1)^(m/2) (2J2/w2)^(n/2). Derivation m1,
       re-derivee au crayon et re-integree par m2 (substitution tau^2,
       erreur <= 1e-11 ; l'integration m1 par somme de Riemann portait
       un biais de -0.19 a -0.58 %, corrige, controle m1 a 1e-6).
       PRECISION DE STATUT : la quadrature est derivee ; son DOMAINE DE
       VALIDITE ne l'est pas -- il est exactement la clause A-6. Aux
       cellules piegees a harmonique admis, le meme modele predit des
       echappements en 14 a 90 unites et n'en rend aucun : a DEUX
       cellules, (3,2;5) et (5,2;7), ce fait est etabli a 190 et 80 fois
       la fenetre de la campagne ; aux cinq autres, a T = 1600 seulement.
  A-3  Le critere de recevabilite est pose sur l'AJUSTEMENT SEUL,
       avant de regarder l'ecart : B eps/F0 <= 0.04 sur la plage
       mesuree (au-dela, F0 est une extrapolation mal contrainte). Il
       retient NEUF colonnes. Sur ces neuf, l'accord au modele
       (quadrature corrigee) est meilleur que 0.6 % sur SIX -- le site
       2:1 aux degres 5, 7 et 9, deux signes : (2,1;5) +0.02/-0.25 % ;
       (2,1;7) -0.19/+0.02 % ; (2,1;9) +0.59/+0.34 % -- et il SORT de
       cette barre sur TROIS : (2,1;11) +1.79/+1.67 %, qui est R-2, et
       (4,1;7) signe -1 -9.10 %, qui est R-1. A un dixieme site,
       (3,2;7) signe +1, l'accord est de -0.35 % avec un conditionnement
       plus lache (0.251) ; (3,2;9) +2.54/+1.35 % et (3,2;7) signe -1
       (inutilisable, B eps = F0) ne sont pas recevables. Les six
       colonnes du demi-pour-cent sont donc UN site a trois degres, pas
       plusieurs sites, et les trois qui en sortent sont exactement les
       deux residus nommes en 86.4. Dont DEUX PREDICTIONS AVEUGLES deposees par m1 sans les colonnes
       (lot v2 non recu) : F(2,1;9) = 0.01173 contre 0.011738 mesure
       (+0.07 %) ; F(2,1;11) = 0.002319 contre 0.002293 (-1.14 %) --
       re-derivees par m1 sur pieces a la reemission : F0 = 0.011724 /
       0.011753 et 0.002291 / 0.002294 par signe.
  A-4  s*(T) = (F delta/(g T))^(1/(p-2)) rend les seuils de tous les sites
       directs SANS les mesurer (s_c(1600) predit/mesure : 0.235/0.2378,
       0.296/0.2993, 0.154/0.1554, 0.170/0.1701, 0.849/0.852-0.859), et
       ln s*(T2)/s*(T1) = -(1/(p-2)) ln((T2-B)/(T1-B)) ; la forme naive
       -ln4/(p-2) n'en est le cas limite que pour B << T. Constantes
       mesurees : B de 2 a 6 aux huit colonnes 2:1 (p = 5, 7, 9, 11) ; de
       0.3 a 157 aux dix autres colonnes directes (11|4.00|-1 0.28 ...
       7|1.50|-1 157), sans structure degagee -- la dichotomie "petit B a
       2:1, grand ailleurs" n'existe pas ; l'affine reste un ajustement.
  A-5  Le "canyon 2:1" est un CUSP : s* descend vers zero au site ; le
       seuil 0.3745 du registre (5|2.00, T = 400) est un nombre de
       fenetre (eps T = F a 1.4 % pres ; 0.05 x 0.37450^3 x 400/3 =
       0.3502 contre F = 0.3455). L'ecart est le terme B de A-4 : le
       seuil vrai verifie F/eps + B = T, donc eps T = F T/(T - B) =
       F (1 + B/(T - B)), soit +1.47 % pour B = 5.78 a l'ancre deposee
       (signe +1), mesure +1.36 %. Ce n'est PAS le pas de grille, qui
       porterait l'ecart a +5.22 % (au premier s explosif, s = 0.379198)
       au lieu de l'expliquer. Troisieme occurrence du meme terme B,
       apres le deficit de pente de A-1 et la forme en (T - B) de A-4.
       Predit par m1 (2.6, gele avant), mesure
       par m2 en aveugle de 2.6 sur quatre degres et deux cotes.
       PRECISION DE STATUT : le regime LINEAIRE (K ~ kappa |dw2|) est
       etroit, |dw2| <~ 0.05-0.1 ; sous |dw2| ~ 0.013 a T = 400 c'est la
       coupure de fenetre ; les flancs sont d'autres regimes, lus a zero
       run sur les archives et non derives : a droite K ~ c_p dw2^2
       (p = 5 : 1.78 dw^1.96 ; p = 7 : 0.54 dw^2.16, quinze points par
       degre de 2.15 a 2.60), a gauche un plateau (K_L(5) ~ 0.0145 sur
       [1.73, 1.86] ; K_L(7) ~ 0.0020) puis la region de la loi beta de
       M10. "beta_g + beta_d = 2" etait une regularite de bande
       (retractee par m2 comme loi) : le croisement de ces regimes.
  A-6  CLAUSE D'ORDRE TOTAL, 30/30 : echappement direct <=> p impair ET
       a + b == p mod 2 ET a + b < p (STRICT) ET a + b <= 5. Empirique,
       sans derivation d'aucun cote ; six cellules neuves hors
       echantillon (p = 11 : 11|4.00, 11|1.50 directes ; 11|3.50,
       11|1.25 piegees ; deux predictions exclusives gagnees contre la
       regle m1 : 9|6.00 piegee, 9|1.50 directe). A citer comme
       empirique partout ou elle est citee.
  A-7  Deux faits d'instrument : (i) au degre PAIR, x -> -x envoie une
       trajectoire sur son opposee exacte ; sP = sM au bit (20/20 a
       p = 4, contre 0/84 aux impairs) ; 22 des 96 entrees G6 a p = 4
       sont redondantes ; (ii) la bissection deposee (chercher_seuil) et
       le "premier s explosif de la grille" ne sont pas interchangeables :
       ecart sans signe fixe, jusqu'a 2.9 pas dans les deux sens (7|3.00 :
       grille 1.58 % SOUS la bissection ; 11|1.25|-1 : -0.12 pas) -- la
       premiere passe de 48 points enjambe un point explosif isole et les
       passes suivantes ne raffinent que le dernier intervalle. Tout s*
       cite nomme son estimateur.
  A-8  (de la note P-1, hors acte, verifie par m2 sur les grilles) Les
       colonnes de la campagne se classent a zero run par les comptes de
       fenetre fine deja deposes : 46 NETTES (seuil exact, T-independant,
       rien sous s* jusqu'a T = 6400 sur 3 % de largeur, discontinuite
       de l'echappement infini -> 35-170), 1 MORDUE, 111 COLLANTES (bande
       criblee, s*(T) derive, survie en T^(-0.35) a 7|2.42). Le biais de
       fenetre cherche par le chantier T-2 n'existe pas comme nombre.

86.3 LE VERDICT DE 5.5 ET SA PORTEE EXACTE
  Gel 0daa050643ec8739 (m2), deux predictions exclusives deposees avant
  run : modele reduit deverrouille a petit eps (m1) contre rien a aucun
  s (clause d'ordre, m2) ; seuil d'instrument gele dans les deux sens
  (derive de H <= 1 % a la fenetre cible, sinon jambe non concluante).
    Jambe B : 7|2.50|-1, T = 1e5, 96 points [0.15, 0.60] : 0 explosion
              (47 predites par m1).
    Jambe A : 5|1.50|+1, T = 3e5, 96 points [0.025, 0.36] : 6 explosions
              (96 predites par m1), toutes entre 80 et 93 % du seuil
              generique 0.389, non monotones (158120, 66805, 54411,
              126639, 42354, 1624), eps t de 18 a 1169 fois G, rapport
              croissant quand s decroit : la bande criblee, pas un canal.
    Instrument : derive relative de H extrapolee 3.3e-6 et 2.8e-6,
              rapport dt -> dt/2 de 32 ; transcription au bit au moteur
              sur les deux cellules avant usage.
  L'hypothese de verrouillage (L = eps S/c ; T_vis = G S/c ; "PIEGE est
  une propriete de la fenetre") est REFUTEE la ou elle etait testable ;
  m1 retire son enonce 6 ("la clause d'ordre est une propriete de
  (rayon, T)") en tant qu'explication : sa moitie "T" est refutee, sa
  moitie "rayon" n'est pas testee et ne s'ouvre pas. Le verdict ne
  demontre pas la clause d'ordre comme loi du systeme : il retire la
  seule lecture alternative formulee. Cette distinction est a l'acte.
  Sort des attentes m1 dans la sequence : 2.4 (1/T aux (1,1) impairs)
  VERIFIEE a 2:1 aux deux degres et deux signes, REFUTEE a 7|2.50 ;
  3.2 (forme (a), gamma ~ 3 aux nettes) FAUSSE, cause nommee ; clause
  b = 1 MORTE (7|1.50 directe) ; F-1 ratee a 5|4.00 ; hypothese de
  verrouillage REFUTEE. Sort des attentes m2 : H_A (parite a 2:1)
  confirmee ; amendement "a + b < p seul" 16/18 ; B-1 (demi-largeur en
  sqrt(eps)) refutee ; "beta_g + beta_d = 2" retractee ; A-d (0 sous
  s = 0.32) ECHOUE (une explosion a 0.3129). Aucune attente n'a ete
  reecrite apres coup ; toutes sont dans les gels.

86.4 LES RESIDUS -- nommes, non ouverts
  R-1  Le modele est aveugle au signe (c ne depend que des actions), la
       mesure ne l'est pas, et l'ecart croit avec a + b : 0.3 % a 2:1,
       1.2 % a (3,2;9), 10 % a (4,1;7) ou les deux signes different de
       10 % entre eux et ou le mieux conditionne s'ecarte du modele de
       -9.1 %. Rejoint, cote modele, "le signe porte l'amplitude" du cusp.
  R-2  Residu de degre a 2:1 : +0.02, -0.19, +0.47, +1.73 % a p = 5, 7,
       9, 11, croissant alors que eps decroit d'un facteur 80 : pas un
       O(eps^2). Candidats : dt = 0.006 fixe quand la fin de course
       raidit avec p ; c(J) a grand p. Non tranche.
  Ouvert sans run prevu : R-1, R-2, la derivation de la clause d'ordre
  total, la largeur de la bande de "beta_g + beta_d = 2".

86.5 LES DEFAUTS CONSIGNES (etiquettes de chantier, plume m2 ; numeros
     de serie a l'acte si l'operateur en decide)
  D-P1-1 (m1)  comptage de la section 2 de la note v1 : deux champs
       confondus (survivants ; morsure a 0.98) -- 46/1/111 en v2.
  D-P1-2 (m1)  phrase fausse sur les comptes negatifs ; corrigee en v2.
  D-P1-3 (m2)  redondance des signes a degre pair (A-7 i).
  D-P1-4 (m2)  estimateur : bissection deposee != grille (A-7 ii).
  D-P1-5 (m1)  une figure, trois contenus sous un nom : le canal
       re-encode les PNG au telechargement ; le manifeste decrivait le
       fichier ecrit, pas le fichier recu.
  N-P1-a (m2)  toute colonne se cite avec son signe (le signe renverse
       la classe : 7|2.27|+1 collante, 7|2.27|-1 nette).
  Biais de quadrature (m1) : -0.19 a -0.58 %, somme de Riemann a gauche
       sur singularite en racine ; corrige par m2, controle par m1.
  Convention "moyenne des deux signes" (m2) : retiree (mele un
       ajustement propre et un ajustement vide, (3,2;7)|-1 : B eps = F0).
  A-d (m2) : compte gele faux (0 predit, 1 mesure sous 0.32) ; lecon :
       une bande criblee n'a pas de bord fixe en T.
  Fautes de portee (m1) : "L1 verifiee" dans le resume de memoire du
       01/09 (registre : refutee M12) ; "independant de T" ecrit a sept
       cellules pour deux (repris a l'annexe) ; formulation circulaire
       de 4.2 (Q-2), reconnue.

86.6 PROPOSITIONS, A ARBITRER PAR L'OPERATEUR, NON PRISES ICI
  (a) Tout binaire porteur d'empreinte voyage DANS un ZIP ; les figures
      portent leur version dans leur nom. Test de canal passe des deux
      cotes, y compris ZIP imbrique (86.8). Le seul depot binaire que
      cite ce delta est la figure 355c11b7642d99d8 dans e61c778c1e21a68b.
  (b) Tout s* cite nomme son estimateur ("bissection deposee" ou
      "premier s explosif de la grille [bornes, pas]").
  (c) Toute profondeur de canyon citee porte son T ; les valeurs du
      registre a 5|2.00 et 7|2.00 (et tout site direct) se lisent comme
      F delta/(g T), avec F au registre.
  (d) Un champ "classe de colonne" (nette / mordue / collante) au
      registre, derive des comptes de fenetre fine deja deposes (A-8),
      en remplacement de la calibration b_h^2 du chantier T-2.
  (e) A degre pair, les deux signes ne comptent que pour un tirage.
  (f) Le mot "L1" est retire ; on ecrit "invariance en g (derivee)",
      "classe affine (refutee M12)", "profil alpha (verifie)".
  (g) La regle du programme a sa jumelle : rien ne se certifie qui ne
      soit d'abord derive ou declare empirique.

86.7 CONSEQUENCES POUR LE REGISTRE ET LA CORRESPONDANCE
  - Le chantier fenetre T-2 se ferme : le biais n'est pas un nombre mais
    trois regimes (nul aux nettes ; toute la valeur aux sites directs ;
    une distribution aux collantes), lisibles a zero run.
  - D1 etape 1 est rendue comme mesure : forme (e) t ~ C/K (avec F
    derive) aux sites directs ; forme (d) avec discontinuite aux
    nettes ; distribution aux collantes ; aucune des formes (a), (b),
    (c) n'est observee ; l'enumeration de D1 etape 0 doit porter (e).
  - Pour la relance Held (note e seulement) : "pas d'ile a 2:1 a degre
    impair ; temps d'echappement t = F/eps + B avec F derive du premier
    ordre resonant, verifie au demi-pour-cent aux degres 5, 7, 9, 11
    dont deux en aveugle ; au meme site a degre pair, ile reelle, seuil
    sept fois plus haut, independant de T ; la clause qui dit quels
    sites sont directs est empirique, 30/30." Les constantes a citer
    sont F (0.3455 ; 0.0611 ; 0.01179 ; 0.00233 aux 2:1 de p = 5, 7,
    9, 11 ; quadrature corrigee), avec delta et le rayon.
  - Rien de cette sequence ne touche la branche quantique ni les
    manches M1-M17.

86.8 LE CANAL, CONSIGNE COMME PROPRIETE
  - Les lots v2 (9284c14b4ca57352) et v4 (037ea9a9cde7449e) ne sont
    parvenus a m1 qu'a la reemission 62a9850e43133478, apres cloture ;
    les deux predictions aveugles de A-3 tiennent a cette absence :
    gain fortuit, pas methode.
  - Les PNG nus sont re-encodes par l'interface au telechargement
    (D-P1-5) ; les ZIP sont preserves, y compris imbriques (reemission :
    9284c14b4ca57352 et 037ea9a9cde7449e rendus apres une
    decompression, 13/13 et 5/5 pieces internes conformes apres deux).
  - np.logspace differe d'une ulp sur 3 a 7 points entre plateformes ;
    l'indice d'echappement n'en depend pas (4 x 96 identiques au bit).
  - Les processus d'arriere-plan du bac a sable m1 ne survivent pas a un
    appel d'outil ; les lots longs (T >= 1e5) sont a BOCAL4 (39-45 us
    par pas, cout domine par le nombre de pas).

86.9 CE QUE CE DELTA NE FAIT PAS
  Il ne prend aucun numero ; il n'ouvre aucun chantier ; il ne joue
  aucun run ; il ne promeut aucune derivation en chaine sans la
  re-derivation 49.5 (la quadrature A-2 est deja re-derivee et
  re-integree par les deux machines ; le reste des lectures de la note
  81ab692160dbcf64 garde son statut de classe 3) ; il ne modifie pas
  l'acte 26056845c8af61cf, qu'il reprend par empreinte.

-- FIN journal_delta_86_sequence_P1_v3 --
