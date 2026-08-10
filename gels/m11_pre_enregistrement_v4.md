PRE-ENREGISTREMENT M11 -- L1-h : LE TEST DE LA CLASSE, A TROIS DEGRES
(gele avant l'ecriture de toute ligne de code ; bloc ASCII, canonique NFC+LF ;
nom de fichier versionne, regle E19 -- version v4)

HISTORIQUE DU GEL
-----------------
  v2. Repond a la certification croisee du 27/07 (NON CERTIFIE en l'etat).
  AJOUTS, aucun ne touche a une porte existante : la forme BRUTE de la classe
  en derivation (e) ; la porte P-M11b sur les PENTES, exacte, gratuite et
  independante des sept de P-M11a ; les seize predictions ABSOLUES de s*(4)
  en P-M11d ; le repere r(4) en P-M11g.
  CORRECTIONS : l'attente sur beta(4), qui pointait en sens CONTRAIRE de la
  porte principale -- defaut de machine 1, corrige au S MES ATTENTES ; la
  normalisation de RMS ; la tolerance d'appartenance (regle 11) ; le comptage
  bloquant du PROGRAMME FIGE ; les bornes de n sous forme derivee (regle 13).
  v4. Repond aux quatre reserves de la certification v3, dont aucune n'etait
  bloquante. La seule a consequence est la (c) : machine 2 releve que la
  symetrie de parite vaut aussi pour les BALAYAGES, et non pour le seul
  seuil. Machine 1 la retient, et va plus loin -- l'egalite n'est pas
  approchee mais EXACTE, et cela se demontre sur le code du moteur. La garde
  de symetrie est donc dedoublee en G8a (porte, inchangee) et G8b
  (consignation bit a bit).
  Machine 2 avait laisse le choix entre une v4 et une note d'exploitation ;
  machine 1 prend la v4, au motif qu'un controle non declare avant le run
  n'est pas un controle -- s'il mordait, il ne serait qu'une lecture
  post-hoc, et il mordrait precisement la ou M11 est le plus faible.
  AUTRES CORRECTIONS v4 : l'ordre de lecture des gardes est declare (a) ; le
  motif de non-exclusion d'une anomalie G8a est ecrit (b) ; le paragraphe
  caduc sur le plancher de machine 2 est retire (d).
  v3. Corrige le defaut bloquant de la certification v2 : la renumerotation
  de v2 n'avait PAS ete propagee aux renvois internes -- neuf pointaient vers
  la mauvaise porte, et deux creaient une contradiction, le symbole P-M11b
  recevant trois statuts differents dans le meme gel. Les neuf sont corriges
  et les deux renvois incomplets completes.
  LECON CONSIGNEE, et c'est la huitieme occurrence de la meme famille dans la
  campagne : une renumerotation est un RENOMMAGE, et tout renommage se
  propage mecaniquement ou ne se fait pas. Ajouter la porte neuve en fin de
  liste aurait coute zero renvoi. Regle 12, transposee de la lecture d'un
  artefact a sa redaction.
  AUTRES CORRECTIONS v3 : decomposition de P-M11d en 7 + 1 + 1 ; borne de n
  harmonisee entre PROGRAMME FIGE et G6 ; clause de recalcul du plancher de
  P-M11b au run ; quatre sources de l'ere E20 inscrites avec empreintes, et
  provenance distinguee de convention ; garde G8 de symetrie a degre pair,
  dedoublee en G8a et G8b par la v4.
  RENUMEROTATION DE v2, v1 n'ayant pas ete certifiee : l'ancienne P-M11b devient
  P-M11c, l'ancienne P-M11c devient P-M11e, l'ancienne P-M11d devient P-M11f,
  l'ancienne P-M11e devient P-M11g. P-M11a est inchangee.
  v1. Aucun bloc anterieur. Aucun numero d'erratum reserve (E18).
  Origine : le delta 40 arrete le fil de conception d'une grille nouvelle,
  au motif qu'une grille optimisee n'a qu'un point de fit commun avec M10 --
  2.85 -- et que L1-h, etant une identite PONCTUELLE, y serait irrealisable
  sans mesurer les TROIS degres, ce qui coute x3.3 en recherches (machine 2,
  reponse aux deltas 39-40). M11 reutilise donc la grille de M10, deja gelee
  et certifiee au bloc v8 (c1d42aa5...), sans y toucher d'un point.
  Le PROGRAMME FIGE est ecrit EN PREMIER : le fil de conception a produit
  cinq deltas sans jamais ecrire combien de degres seraient mesures, et c'est
  ce silence -- non un defaut de verification -- qui a rendu possible
  l'optimisation d'un objet dont personne ne connaissait les dimensions.
  Regle de redaction adoptee : le programme fige precede le critere de plan,
  jamais l'inverse.
  HERITE ET NON REDISCUTE : R-2' (delta 38.6), le balayage a pas relatif
  (delta 39.3), la regle 14 (refit a chaque reechantillonnage), les quatre
  declarations du delta 39.6.

PROGRAMME FIGE
--------------
  DEGRE MESURE : p = 4, et lui seul.
  GRILLE : celle de M10, seize points, inchangee et non rediscutee --
    1.25, 1.30, 1.35, 1.4142135623730951, 1.45, 1.55, 1.70, 1.80,
    1.90, 2.05, 2.15, 2.30, 2.45, 2.60, 2.75, 2.85
  RECHERCHES : 32 (16 points x 2 signes, p=4 -- dont 16 MESURES et 16
               CONTROLES de symetrie, voir G8a et G8b : a degre pair les deux
               donnent le meme seuil)
             +  2 (G1', reproduction de M10 a p=5, un point, deux signes)
             +  6 (G2, trois points x deux signes, a 2g, p=4)
             +  1 (G4, dt/2 sur une ligne)
             = 41 au total.   [M10 : 71]
  BALAYAGES G6 : 32, un par ligne p=4 mesuree.   [M10 : 64]
  POINTS DE BALAYAGE, SOUS FORME DERIVEE (regle 13) :
    n_grossier = ceil((0.90 - LO0/s*) / 0.005) + 1,  n_fin = 201.
    PROJECTION depuis les s* de M10 (p=5 et p=7) : 322 a 380 par ligne.
    BORNE DURE, valable pour tout s* > LO0/0.90 = 0.0556 : n_grossier tend
    vers 181 quand s* croit, donc n <= 382 par ligne. M11 mesure p=4, dont
    les s* seront PLUS GRANDS que ceux de p=5 (s* decroit avec p), donc la
    projection sera depassee et la borne dure approchee.
    LES DEUX VALEURS VONT AU JSON : la projetee et l'obtenue.
    TOTAL : 32 x 382 = 12 224 au pire.   [M10 : 12 288] -- M11 reste moins
    chere que M10 en balayage comme en recherches, meme au cas dur.
    BORNE SUPERIEURE DECLAREE DE n : 400 par ligne. Depassement -> ARRET.
  SORTIE : out/m11_results.json, incremental, une ecriture apres chaque point.
  COMPTAGE BLOQUANT. Les recherches et les balayages sont COMPTES par
    enveloppe des fonctions du moteur, jamais affirmes. Le JSON porte le
    compte OBTENU et le compte ATTENDU, et le script s'ARRETE si les deux
    different, en citant les deux. Un nombre qu'un artefact affirme sur
    lui-meme doit etre compte (D-M10-14, regle 13).
  APPARTENANCE A LA GRILLE (regle 11). Les seize points sont compares PAR
    VALEUR, tolerance declaree 1e-09. L'espacement minimal de la grille vaut
    0.0358 -- entre sqrt(2) et 1.45 -- soit 3.6e+07 fois la tolerance. Le
    controle figure au --selftest : assert set(sous_ensemble) <= set(grille),
    par valeur et jamais par etiquette formatee.

QUESTION
--------
La classe M(zeta, f) affirme que le seuil obeit a g (zeta(w2) s)^(p-2) = f(w2),
d'ou beta(p) = F/(p-2) + Z, affine en 1/(p-2). Le bloc L1 (v4, dbe633e2...)
en tire une consequence PONCTUELLE, L1-h : en ecrivant res_p le residu du fit
en loi de puissance au degre p, la classe impose
    res_p = phi/(p-2) + psi     en CHAQUE point de la grille,
avec phi et psi INDEPENDANTS de p. A deux degres le systeme est exactement
determine : il ajuste et ne teste rien. A trois degres il est surdetermine, et
la classe devient falsifiable.
M11 mesure le troisieme degre. C'est le SEUL objectif principal de la manche.

DERIVATIONS PREALABLES
----------------------
(a) LES COEFFICIENTS SONT DERIVES, PAS CHOISIS. On cherche a, b tels que
    res4 = a res5 + b res7 pour tout couple (phi, psi). En posant
    u_p = 1/(p-2), cela impose a u5 + b u7 = u4 et a + b = 1, soit
        a/3 + b/5 = 1/2   et   a + b = 1
    systeme 2x2 de determinant non nul, solution UNIQUE :
        a = +2.25   b = -1.25
    Ce sont exactement les coefficients de L1-h, ecrits sous la forme
    res4 - 2.25 res5 + 1.25 res7 = 0. Aucun degre de liberte n'y entre.
(b) LE SIGNAL A REFUTER N'EST PAS UN ZERO. res5 et res7 sont MESURES par
    M10 sur les neuf points de fit ; res4 predit s'en deduit exactement. Sa
    dispersion vaut 0.21191 en RMS et atteint 0.403714 au point 2.15. La
    porte compare donc neuf nombres a neuf nombres, et non une quantite a
    zero.
(c) SEPT CONTRAINTES, PAS NEUF. a4 et b4 -- ordonnee et pente du fit a p=4 --
    sont inconnus avant mesure. La prediction porte donc sur les RESIDUS,
    c'est-a-dire sur ln s*(4) A UNE AFFINE PRES en ln Delta. Les residus OLS
    verifient identiquement somme(res) = 0 et somme((u - moyenne u) res) = 0 :
    deux contraintes sont absorbees. Neuf points moins deux parametres font
    SEPT contraintes independantes. Verifie sur les predictions : la somme
    vaut 5.1e-15 et la somme ponderee -7.9e-16.
(d) LE PLANCHER DE BRUIT, SOUS SA FORME DERIVEE (regle 13). L'ecart de la
    combinaison herite de l'erreur sur chacun des trois residus, ponderee par
    les coefficients :
        plancher = (1 + |a| + |b|) x pas_final / s*_min = 4.50 x pas / s*_min
    Le pas final des recherches est ABSOLU ; l'erreur sur ln s* vaut donc
    pas/s*, maximale au plus PETIT s*. Sur les 64 lignes de M10, s*_min =
    0.1641.
        pas obtenu au run M10 : 6.03e-07 -> plancher 1.65e-05 -> 4.1 decades
        pas GARANTI par G5    : 1.00e-05 -> plancher 2.74e-04 -> 2.9 decades
    FAIT FOI POUR LA PORTE : le plancher GARANTI, 2.74e-04. Le plancher
    obtenu sera consigne a cote. Motif : une porte ne peut pas dependre d'une
    performance que le protocole n'exige pas.

(e) LA FORME BRUTE, DONT L1-h N'EST QUE LA PROJECTION. La classe donne
    s* = (f/g)^(1/(p-2)) / zeta, donc PONCTUELLEMENT
        ln s*_p(w2) = A(w2) u_p + B(w2),   u_p = 1/(p-2),
    avec A = ln f - ln g et B = -ln zeta INDEPENDANTS de p. La meme
    combinaison (1, -2.25, +1.25) annule A et B :
        ln s*4 - 2.25 ln s*5 + 1.25 ln s*7 = 0  EN CHAQUE POINT, SANS AUCUN FIT.
    res_p = u_p phi + psi n'en est que la PROJECTION sur le complement des
    affines : le fit absorbe deux dimensions, et L1-h les perd. Les deux
    enonces sont coherents -- le residu de la combinaison brute egale la
    combinaison des residus, a 6.7e-16 (machine 2).
    CONSEQUENCE, et elle structure la v2 : la classe fournit SEIZE
    predictions ABSOLUES de s*(4) et UNE contrainte sur les pentes, en plus
    des sept contraintes sur les residus. Le bloc v1 testait la projection
    en laissant la source dehors.
    CETTE FORME EST UN RESULTAT DU BLOC L1, pas de M11 : L1 avait formule la
    classe en termes de RESIDUS parce qu'il etait un bloc de lecture sur les
    beta. Elle est portee au journal a ce titre, independamment de M11.

PROTOCOLE DE FIT
----------------
Regression de ln s*(4) sur ln Delta, Delta = w2^2 - 1, moindres carres
ordinaires sans ponderation, sur l'ENSEMBLE DE FIT ci-dessous et lui seul.
Convention (f) integrale : les deux signes partout, sF = min(sP, sM), les
asymetries consignees.
  ENSEMBLE DE FIT (9 points), identique a celui de M10 apres G7 :
    1.30, 1.70, 1.80, 2.15, 2.30, 2.45, 2.60, 2.75, 2.85
  ENSEMBLE HORS FIT (7 points, mesures et CONSIGNES, jamais dans le fit) :
    1.25, 1.35, 1.4142135623730951, 1.45, 1.55, 1.90, 2.05
  R-2' -- REGLE D'EXCLUSION PROLONGEE, gelee ici et NON AJUSTABLE ENSUITE.
    R-2 declare 0.12 (ordre <= 6) et 0.03 (ordres 7-8), puis tronque a 0.
    Le rapport est de 4 par PAIRE d'ordres ; la continuation qui n'est
    ajustee sur rien poursuit ce rapport :
        0.12 (o<=6) | 0.03 (o 7-8) | 0.0075 (o 9-10) | 0.001875 (o 11-12)
    Elle ne deplace aucun poteau : elle supprime une DISCONTINUITE que R-2
    avait laissee, et elle est entierement determinee par deux nombres deja
    geles au bloc M10 v8. Appliquee aux dix points du fit R-2 de M10, elle
    retire 1.25 -- a 0.0000 de 5:4, ordre 9, sous le rayon 0.0075 -- et lui
    seul. Le fit R-2' coincide donc avec le fit ampute par G7 en M10.
    CONSIGNE : cette coincidence est post-hoc et n = 1. Ce n'est pas une
    preuve, et elle ne sera pas invoquee comme telle.
  1.25 reste MESURE : il sert de temoin a la lecture P-M11f.
  Les rayons d'ordre 9-12 servent a EXCLURE et jamais a RESOUDRE ; aucune
  contrainte de pas n'en decoule (delta 39.4).

PORTES
------

P-M11a  LA CLASSE EST-ELLE VRAIE ? (porte principale, a verdict)
  Statistique : D_i = res4(w_i) - 2.25 res5(w_i) + 1.25 res7(w_i) aux neuf
  points de fit, les trois vecteurs de residus etant calcules sur LE MEME
  ensemble de fit.
  LES NEUF PREDICTIONS, PUBLIEES AVANT MESURE :
      w2       res5 (M10)    res7 (M10)    res4 PREDIT
      1.3000   +0.138147     +0.031766     +0.271123
      1.7000   -0.021627     +0.041608     -0.100669
      1.8000   -0.146410     -0.022952     -0.300733
      2.1500   -0.265591     -0.155092     -0.403714
      2.3000   +0.011434     -0.049641     +0.087777
      2.4500   +0.050717     +0.023524     +0.084709
      2.6000   +0.109913     +0.068224     +0.162025
      2.7500   +0.098773     +0.054031     +0.154700
      2.8500   +0.024643     +0.008531     +0.044783
  NORMALISATION DE RMS, DECLAREE (sans quoi le seuil de 1 % n'a pas de
  sens) : RMS(v) = sqrt( somme(v_i^2) / 9 ), division par le NOMBRE DE
  POINTS et non par les degres de liberte, LA MEME pour RMS(D) et pour
  RMS(res4 predit) qui lui sert de reference. Diviser par 7 les changerait
  toutes deux du meme facteur sqrt(9/7) = 1.134 et laisserait le rapport
  inchange, mais les deux doivent etre declarees identiques pour etre
  comparables.
  RMS(res4 predit) = 0.21191. Seuils DERIVES de cette dispersion :
      RMS(D) <= 1 %  de 0.21191, soit 2.119e-03  -> CLASSE COMPATIBLE
      RMS(D) >= 10 % de 0.21191, soit 2.119e-02  -> CLASSE REFUTEE
      entre les deux                              -> NON CONCLUANT
  Le plancher garanti (2.74e-04) vaut 13 % du seuil COMPATIBLE : la porte est
  ATTEIGNABLE avec la seule garantie de G5, sans supposer la performance du
  run.
  LECTURE OBLIGATOIRE EN CAS DE REFUTATION : consigner D_i point par point et
  nommer le ou les points qui portent l'ecart. Une refutation localisee et une
  refutation diffuse ne disent pas la meme chose, et le choix ne se fera pas
  apres coup.
  SI G7 AMPUTE. Une exclusion prononcee a p=4 retire le point du fit commun
  aux trois degres, et res5 comme res7 doivent alors etre RECALCULES sur le
  fit survivant (regle 14 : un residu est une sortie du fit, pas une donnee).
  Les neuf predictions ci-dessus ne vaudraient plus.
      DECISION GELEE : la porte se lit sur le fit SURVIVANT, avec les trois
      vecteurs recalcules et la meme regle de coefficients -- qui ne depend
      pas de la grille. Les seuils, exprimes en POURCENTAGE de RMS(res4
      predit), sont recalcules avec elle.
      La lecture sur le fit AMPUTE est explicitement declaree NON
      PRE-DECLAREE dans ses nombres, et pre-declaree dans sa REGLE. Les neuf
      predictions ci-dessus restent au registre comme la lecture du cas sans
      amputation, qui est le cas attendu.

P-M11b  LA CLASSE SUR LES PENTES (porte a verdict, independante de P-M11a)
  Le fit OLS etant lineaire en y, la pente herite de la relation ponctuelle :
  b_p = u_p b_A + b_B, donc la meme combinaison donne
      beta(4) - 2.25 beta(5) + 1.25 beta(7) = 0
  EXACTEMENT, SUR N'IMPORTE QUELLE GRILLE. Cette contrainte est INDEPENDANTE
  des sept de P-M11a : residus et pente sont orthogonaux par construction
  OLS. Elle est en outre exempte de la dependance de grille qui ruine la
  comparaison des mecanismes, puisqu'elle ne compare pas des pentes entre
  grilles mais les TROIS pentes d'une MEME grille.
      beta(5) = 1.023585 | beta(7) = 0.954955 (M10, fit ampute)
      beta(4) PREDIT = 2.25 x 1.023585 - 1.25 x 0.954955 = 1.109373
  PLANCHER, SOUS FORME DERIVEE (regle 13), et il differe de celui annonce en
  certification -- 8.71e-05 -- que je n'ai pu reproduire par aucune des
  quatre propagations naturelles ; la plus proche, quadratique sur le fit,
  donne 2.63e-05. Je declare donc la mienne, en PIRE CAS :
      plancher sur UNE pente = somme|w_i| x pas_garanti / s*_min(fit)
                             = 1.1494 x 1e-05 / 0.1789 = 6.43e-05
      plancher sur la combinaison = 4.50 x 6.43e-05 = 2.89e-04
  MOTIF DU PIRE CAS : les erreurs de troncature sur des points voisins n'ont
  aucune raison d'etre independantes. Une porte ne se justifie pas par une
  hypothese d'independance qu'on n'a pas verifiee.
  MACHINE 2 A RETIRE SON CHIFFRE EN CERTIFICATION v2 : sa derivation, portee
  point par point, rend 1.279e-04 ; celle-ci la majore d'un facteur 2.26 en
  remplacant s*_i par s*_min dans chaque terme, et sur une porte c'est la
  majoration qui gagne. 2.891e-04 fait foi.
  RECALCUL AU RUN (regle 13), comme pour P-M11a : s*_min(fit) = 0.1789 est
  le minimum sur les DEUX degres DEJA MESURES. A p=4 les s* seront
  differents -- plus grands, s* decroissant avec p -- donc le plancher est
  RECALCULE au run sur le s*_min des TROIS degres, et les deux valeurs vont
  au JSON. La plus CONSERVATRICE fait foi.
  ECHELLES DE COMPARAISON : |beta(5) - beta(7)| = 0.0686 -> dynamique 237,
  soit 2.4 decades. Ecart entre la classe et le beta(4) historique
  (0.1594) -> dynamique 551.
  SEUILS, derives de |beta(5) - beta(7)| = 0.0686 :
      |combinaison| <=  5 % de 0.0686, soit 3.43e-03  -> COMPATIBLE
      |combinaison| >= 50 % de 0.0686, soit 3.43e-02  -> REFUTEE
      entre les deux                                   -> NON CONCLUANT
  Le plancher (2.89e-04) vaut 8.4 % du seuil COMPATIBLE : la porte est
  ATTEIGNABLE avec la seule garantie de G5.
  SI G7 AMPUTE : meme decision que P-M11a -- les trois pentes sont
  recalculees sur le fit survivant, la contrainte etant exacte sur toute
  grille ; les seuils, exprimes en pourcentage de |beta(5) - beta(7)|, sont
  recalcules avec elle.

P-M11c  beta(4) EN VALEUR (porte a verdict, mais dont l'issue est annoncee)
  beta(4), SE, sigma et les residus sur le fit ampute. Verdict selon les memes
  branches que P-M10a, seuils recalcules sur le Sxx obtenu (regle 13) et non
  recopies.
  ATTENTE DECLAREE, ET C'EST LE POINT : sur la grille de M10, beta(4) NE
  DISCRIMINERA PAS les deux mecanismes morts. L'etendue jackknife de F vaut
  0.9620 ; l'ecart entre "equilibre d'energie" (F = 1.0000) et "fermeture de
  largeur resonante" (F = 1.3461) vaut 0.3461. Couverture 278 %.
  ET LE LEVIER N'Y CHANGE RIEN. Sous la classe, res_p = u_p phi + psi et
  l'OLS etant lineaire, la pente jackknife vaut d_p,j = u_p PHI_j + PSI_j,
  d'ou F(G\j) - F(G) = PHI_j pour TOUT couple de degres. L'etendue jackknife
  de F est celle de PHI_j : elle ne depend pas du couple. Verifie par machine
  2 sur six couples, leviers de 0.05 a 0.30 -- toutes a 0.962004.
  CONSEQUENCE, ECRITE AVANT : le "x2.25 du levier (4,7)" porte sur
  l'amplification de l'erreur de MESURE, qui est a cinq ordres sous la
  dependance de grille. Sur le seul terme d'erreur reel, il ne gagne rien.
  L'argument no 1 du dossier p=4 tombe donc, comme le cinquieme, et pour la
  meme raison de fond : une quantite qu'on croyait gagner par le choix des
  degres est fixee par la GRILLE seule.
  UN NON CONCLUANT SUR P-M11c EST DONC UN RESULTAT ATTENDU, PAS UN ECHEC DE
  PLAN. Cette phrase est ecrite avant mesure precisement pour que le fil de
  conception, arrete au delta 40, ne soit pas rouvert sur ce motif.

P-M11d  LES SEIZE PREDICTIONS ABSOLUES DE s*(4) (consignation, aucune porte)
  De la derivation (e), sans aucun fit : s*(4) = exp(2.25 ln s*5 - 1.25 ln s*7)
  en chaque point de la grille. Publiees avant mesure :
      1.2500  0.31256113   1.3000  0.43507471   1.3500  0.45242056
      1.4142  0.44169035   1.4500  0.40063998   1.5500  0.81861678
      1.7000  0.91742847   1.8000  0.90686431   1.9000  0.76219238
      2.0500  0.68545935   2.1500  1.39447632   2.3000  2.75007870
      2.4500  3.25118000   2.6000  4.10725665   2.7500  4.71208689
      2.8500  4.62305914
  CONSIGNATION ET NON PORTE, pour une raison qui est le coeur de l'affaire :
  un ecart AFFINE COMMUN a ces seize valeurs -- ln s*(4) mesure decale de
  a + b ln Delta par rapport au predit -- signalerait un BIAIS DE CONVENTION
  A DEGRE PAIR et non une refutation de la classe. Or ce biais est
  precisement la limitation que ce gel declare : la convention (f) integrale
  n'a jamais ete exercee sur un degre pair dans un run opposable, et E20 est
  ne exactement la.
  LA DECOMPOSITION EST 7 + 1 + 1, ET NON 7 + 2 -- correction relevee en
  certification v2 et adoptee. Sur les neuf points de fit, les ecarts se
  decomposent en TROIS composantes orthogonales qui epuisent les neuf
  dimensions :
      7 residus    -> juges par P-M11a
      1 pente      -> jugee par P-M11b
      1 constante  -> non jugee par une porte, et c'est LA que loge un biais
  ET C'EST LA CONSTANTE SEULE QUI PORTE UN BIAIS D'ECHELLE : un facteur
  multiplicatif c sur s*(4) decale ln s*(4) de ln c, une CONSTANTE, et ne
  touche pas a la pente. Envoyer toute la partie affine au biais ferait
  absorber par << echelle >> une deviation de PENTE, c'est-a-dire exactement
  ce que P-M11b doit juger : la consignation censee completer la porte
  l'aurait neutralisee.
  LECTURE PRE-DECLAREE : ajuster a + b ln Delta sur les seize ecarts ; la
  CONSTANTE a va a P-M11g, la PENTE b est deja jugee par P-M11b, les residus
  par P-M11a. Aucun verdict ne sort de P-M11d : elle SEPARE les trois
  composantes et les remet a leurs trois juges.
  LIMITATION DECLAREE : un biais qui ne serait PAS constant -- une erreur
  systematique variant avec w2 -- fuirait dans la pente et serait lu comme
  une refutation de P-M11b. Rien dans M11 ne l'en distingue. Ecrit d'avance.

P-M11e  LA CLASSE HORS DU FIT (consignation, aucune porte)
  Les droites s'evaluent hors de leur ensemble d'ajustement sans rien
  supposer, et l'identite de classe doit valoir partout ou le mecanisme
  s'applique. Sept predictions supplementaires, publiees avant mesure :
      1.2500 +0.167051 | 1.3500 +0.115348 | 1.4142 -0.125434
      1.4500 -0.331233 | 1.5500 +0.116321 | 1.9000 -0.644121
      2.0500 -0.977188
  CONSIGNATION ET NON PORTE, pour une raison declaree : ces points sont hors
  fit parce qu'ils sont proches d'une resonance, et c'est precisement la que
  la classe peut legitimement echouer sans etre fausse ailleurs. Aucun
  verdict n'en sortira. Mais la lecture est gratuite et double le nombre de
  confrontations, de neuf a seize.

P-M11f  OU G6 TIRE-T-ELLE A p=4 ? (consignation, aucune porte)
  Consigner la position de tout declenchement de G6. Lecture ecrite d'avance,
  et elle departage deux hypotheses laissees ouvertes au delta 38.1 :
    un declenchement a 1.25 -- soit 5:4 exactement, ordre 9 -- appuie
      l'hypothese RESONANTE ;
    un declenchement au bord gauche sans etre sur une resonance appuie
      l'hypothese REGIONALE ;
    aucun declenchement ne departage rien.
  AUCUNE PORTE N'EN DEPEND, et c'est ce qui rend la lecture possible : R-2'
  ayant sorti 1.25 du fit, un declenchement a ce point n'ampute rien.
  RESERVE, heritee du delta 38.1 : les 64 balayages de M10 n'avaient aucune
  puissance sur cette question (|r| critique 0.501 ; une correlation vraie de
  0.30 invisible huit fois sur dix). Un declenchement unique a p=4 n'en aura
  pas davantage. C'est un INDICE consigne, jamais un verdict.

P-M11g  beta(4) DEVIENT OPPOSABLE, ET UN REPERE QUI SE CONFRONTE (consignation)
  Le bloc M10 v8 declare en limitation que beta(4) et beta(6) ne sont pas
  refaits, pour provenance mixte et convention non confirmee (E20). M11, en
  convention (f) integrale, rend beta(4) OPPOSABLE POUR LA PREMIERE FOIS.
  Cela importe au-dela de M11 : la mort de la "fermeture de largeur
  resonante" repose sur p=4 et p=6, les deux degres non opposables, au point
  que la cloture L1 (delta 31.3) exige que toute mention future porte le
  qualificatif "portee par p=4". M11 ne tranchera pas cette mort par F --
  P-M11c l'annonce -- mais il rendra opposable la mesure sur laquelle
  l'enonce s'appuie.
  LES QUATRE SOURCES DE L'ERE E20, FOURNIES EN CERTIFICATION v2 ET INSCRITES
  ICI, empreintes canoniques NFC+LF :
      c6395480d7f8adb3  journal_delta_24_D3.md
        "convention UNIQUE (min) : r(4) = 7.44, r(5) = 8.338, r(6) = 6.65,
         r(7) = 7.100 -- bande 6.65-8.34"
      5e2e1462710f4a13  journal_delta_25_M9v2.md   reprise de la table
      dbaafe2587ed5889  journal_delta_27_derivation_r.md
        beta = 1.32 / 0.95 / 1.02 / 0.88 / 0.91 pour p = 3..7
      b867820e67527fb2  archive/deltas_clos/journal_delta_21bis.md
        table r la plus ancienne : 17.4 / 7.44 / 8.34 / 6.65 / 7.47
  Les valeurs seront lues de ces fichiers apres verification d'empreinte, et
  jamais codees en dur.
  PROVENANCE ET CONVENTION SONT DEUX RESERVES DIFFERENTES, ET UNE SEULE
  SUBSISTE. Le delta 24 etiquette EXPLICITEMENT r(4) = 7.44 comme etant en
  convention MIN, c'est-a-dire la convention (f) elle-meme. La comparaison
  10.2185 contre 7.44 est donc A CONVENTION EGALE, et l'ecart de 37 % ne peut
  pas etre impute a un changement de convention -- ce qui etait l'echappatoire
  la plus evidente. Mieux : par la symetrie de parite (gardes G8a et G8b), la
  convention est SANS OBJET a degre pair, donc doublement hors de cause.
  CE QUI RESTE NON CONFIRME a p=4 par E20 est la PROVENANCE seule : quel run,
  quel moteur, quelle version du protocole. Les deux reserves ne seront plus
  employees l'une pour l'autre.
  REPERE PRE-DECLARE, ET LES DEUX ISSUES SONT INFORMATIVES. L'acquis
  structurel de la campagne pose r = s*(2.85)/s*(1.35) quasi constant entre
  6.65 et 8.35 pour p >= 4, la valeur de p=4 provenant de l'ere E20
  (convention non confirmee, E20). Or la classe predit, depuis P-M11d :
      r(4) PREDIT = 4.62305914 / 0.45242056 = 10.2185
      r(5) mesure, convention (f) = 8.3470 | r(7) mesure = 7.0998
      r(4) de l'ere E20, NON OPPOSABLE = 7.44 -> ecart de 37 %
  LECTURE ECRITE D'AVANCE :
      r(4) proche de 7.4, conforme a l'ere E20 -> LA CLASSE EST REFUTEE et
        l'acquis structurel survit ;
      r(4) proche de 10.2 -> LA CLASSE TIENT et la valeur p=4 de l'acquis
        etait fausse, ce que E20 laissait deja craindre.
  Le repere porte sur DEUX POINTS MESURES -- 1.35 est hors fit mais mesure --
  et il ne coute rien. Il est consigne, sans porte : c'est P-M11b qui juge
  la classe sur les pentes, et P-M11a sur les residus.

GARDES
------
  ORDRE DE LECTURE, DECLARE : G1' G2 G3 G4 G5 G6 G8a G8b G7. La numerotation
  n'est PAS l'ordre de lecture : G7 vient logiquement en DERNIER puisqu'elle
  repercute les exclusions prononcees par les autres, et G8a/G8b s'intercalent avant
  elle parce qu'elle porte sur des mesures et non sur le fit. Ce paragraphe
  existe pour qu'un --selftest qui enumere les gardes dans l'ordre du texte ne
  soit pas lu comme une incoherence. Renumeroter aurait ete un RENOMMAGE, et
  la v3 vient d'en payer le prix : on ne renomme pas pour faire joli.
  G1' CUSTODY DE LA CHAINE (bloquante). M11 n'a AUCUNE ancre opposable a
    p=4 -- c'est l'objet meme de P-M11g. La garde de regression porte donc
    sur le MOTEUR et non sur le degre mesure : rebinder a p=5, mesurer
    w2 = 1.80 aux deux signes, et reproduire la carte M9 a +-2 % PAR SIGNE.
    sP attendu 0.6668205807758855, sM attendu 0.9011724660948772, lus du JSON
    M9 (41595413...) et jamais codes en dur. Le point 1.80 est choisi parce
    que le cote fragile s'y inverse : la garde y controle le moteur ET la
    convention de signe. Echec -> ARRET.
  G2 INVARIANCE EN g (exclusion). K a 2g sur w2 = 1.35, 1.80, 2.85, p=4, deux
    signes, tolerance 10 %. Le cote g est LU DE LA CARTE et non remesure
    (D-M10-14) : six recherches et non douze. Echec -> ligne EXCLUE du fit,
    consignee, repercutee par G7.
    NOTE, pour qu'un relecteur ne s'y trompe pas : 1.35 est HORS FIT sous
    R-2 comme sous R-2'. Une exclusion prononcee par G2 en ce point ne retire
    donc rien du fit. C'est la reproduction fidele de M10, non un defaut.
  G3 IDENTITE DE FORCE (bloquante, metrique obligatoire). Erreur backward
    <= 1e-12, executee APRES CHAQUE REBINDING de la globale P du moteur, donc
    une fois par degre charge -- p=4 pour la carte, p=5 pour G1'. Les deux
    erreurs vont au JSON.
  G4 PAS DE TEMPS (exclusion). dt/2 sur la ligne maximisant g s*^(p-1) --
    l'ECHELLE DE FORCE, et non le plus grand s* : les deux ne coincident pas
    et l'erreur est invisible une fois faite. Ecart <= 2 % ; sinon ligne NON
    FIABLE, EXCLUE, repercutee.
  G5 CONVERGENCE (exclusion). Pas final <= 1e-05. Une recherche qui ne rend
    pas de seuil (ECHEC_HAUT, ECHEC_BAS) ou dont la passe dense n'explose pas
    (DENSE_SANS_EXPLOSION) est EXCLUE au meme titre ; le filtre porte sur la
    NOTE et jamais sur la nullite du seuil, car DENSE_SANS_EXPLOSION rend un
    flottant valide qui n'est pas un seuil mesure.
  G6 PRIMAUTE DE s*, A PAS RELATIF CONSTANT (exclusion + consignation).
    DEUX balayages, dont le PAS RELATIF est gele et dont le nombre de points
    est une SORTIE -- c'est l'inversion du delta 39.3, et c'est elle qui
    supprime le confondant :
      grossier [LO0, 0.90 s*], pas relatif 0.005 -> n de 121 a 179
      fin      [0.90, 1.30 s*], pas relatif 0.002 -> n = 201, constant
      total : PROJECTION 322 a 380 depuis les s* de M10 ; BORNE DURE 382
      pour tout s* > LO0/0.90 = 0.0556 ; borne superieure declaree 400,
      depassement -> ARRET. Meme forme derivee qu'au PROGRAMME FIGE ; les
      deux valeurs, projetee et obtenue, vont au JSON.
    EXCLUSION : toute explosion trouvee sous 0.98 s* -> ligne EXCLUE,
    consignee avec la valeur inferieure trouvee, repercutee par G7.
    CONSIGNATION : nombre d'ilots, position de la premiere retombee, et
    min(s explosif)/s* sur CHAQUE ligne. La fenetre [s*, 1.3 s*] du gel est
    desormais integralement couverte : la censure a 1.05 s*, qui frappait
    48 % des lignes de M10, disparait.
    QUATRE DECLARATIONS, exigees par le delta 39.6 :
      (a) le pas relatif est le parametre gele, n est calcule avant chaque
          balayage a partir de s* et du pas ; aucune circularite, s* etant
          connu des la recherche ;
      (b) toute lecture de structure -- ilots, retombee, regional/resonant --
          se fait sur la fenetre FINE, seule ou le pas relatif est constant ;
      (c) REDEPLOIEMENT PAR RAPPORT A M10, et non conservation : la garde
          gagne un facteur 2.5 a 3.4 au-dessus de 0.90 s* et perd un facteur
          1.6 a 1.7 en dessous. Les exclusions de M10 et de M11 ne sont donc
          pas comparables sans cette correction ;
      (d) l'enonce "aucune explosion sous 0.90 s* en 64 lignes" de M10 vaut A
          LA RESOLUTION DE M10 (pas relatif 0.0039 a 0.0054), et non dans
          l'absolu.
  G8a SYMETRIE A DEGRE PAIR, SUR LE SEUIL (porte a arret conditionnel).
    A p PAIR le
    potentiel (g/p)x^p est PAIR, la force g x^(p-1) est IMPAIRE, et le
    systeme est invariant par x -> -x : les conditions initiales du signe -1
    sont l'image exacte de celles du signe +1, et le seuil est le MEME.
        s*(+1) = s*(-1)   a p pair, EXACTEMENT.
    TROIS CONSEQUENCES, toutes gratuites, relevees en certification v2 :
      (i)  la convention (f) est SANS EFFET a p=4 : sF = sP = sM. La
           limitation declaree au gel -- convention jamais exercee a degre
           pair -- est donc moins lourde qu'ecrite, et surtout elle devient
           TESTABLE ;
      (ii) les seize recherches du signe -1 ne sont pas une mesure : ce sont
           un CONTROLE. Le PROGRAMME FIGE compte donc 16 mesures et 16
           controles, et non 32 mesures ;
      (iii) c'est le SEUL controle interne que M11 possede sur la branche a
           degre pair du moteur -- G1' teste a p=5 et ne le couvre pas.
    SEUIL : |s*(+1) - s*(-1)| <= 2 x pas_final, aux seize points, chaque
    recherche rendant sa valeur a un pas pres.
    ECHEC : la ligne est consignee ANOMALIE avec l'ecart exprime en pas de
    recherche. UNE anomalie est toleree et consignee ; DEUX ou plus -> ARRET.
    NOTA : le seuil de 2 pas est CONSERVATEUR au regard de G8b, qui demontre
    une identite EXACTE. Il est maintenu tel quel pour que la porte ne
    depende pas de la demonstration -- si celle-ci est fausse, G8a tient
    quand meme.
    Motif de ne pas arreter a la premiere : un cas limite peut etre un
    artefact de discretisation ; deux ne le peuvent pas.
    LECTURE ECRITE D'AVANCE : une anomalie signale une rupture de symetrie ou
    un defaut de rebinding du degre, jamais un fait physique -- la symetrie
    est algebrique. C'est un diagnostic d'instrument, pas une mesure.
    POURQUOI UNE ANOMALIE N'EXCLUT PAS LA LIGNE, et G7 ne cite ni G8a ni G8b :
    anomalie de symetrie est un DIAGNOSTIC D'INSTRUMENT, pas un fait
    physique -- la symetrie est algebrique et ne peut pas etre violee par la
    dynamique. Exclure la ligne amputerait le fit sur une mesure qui peut
    etre parfaitement bonne, et surtout cela ENTERRERAIT le defaut dans une
    exclusion. La reponse correcte a un defaut d'instrument est de consigner
    puis d'arreter, jamais d'ecarter la donnee en silence. Motif ecrit, comme
    la certification v3 le demande.
    ETAT DE L'AFFIRMATION : la campagne n'a AUCUNE mesure p=4 aux deux signes
    dans un artefact opposable, ce qui est E20 exactement. La symetrie repose
    sur le delta 23 et sur l'argument de parite ci-dessus, jamais sur une
    mesure de la chaine actuelle. M11 la verifie pour la premiere fois.

  G8b SYMETRIE SUR TOUTE LA STRUCTURE, BIT A BIT (consignation, aucune porte).
    Machine 2 releve que la symetrie vaut aussi pour les BALAYAGES : si le
    systeme est invariant par x -> -x, l'ensemble explosif du signe -1 est
    l'IMAGE de celui du signe +1, donc non seulement s* mais toute la
    structure. G8a compare deux nombres ; G8b compare deux VECTEURS de 322 a
    382 points, aux seize points de la grille. Cout machine : NUL, les
    balayages sont deja au PROGRAMME FIGE.
    ET L'EGALITE N'EST PAS APPROCHEE, ELLE EST EXACTE. Cela se demontre sur
    le moteur, ligne a ligne, et non par un argument de continuite :
      - les conditions initiales sont x1 = sgn s (1+w2^2)/D et
        x2 = -sgn s (1+W1^2)/D : la negation est EXACTE en IEEE-754 ;
      - grad_rapide rend g (x1+x2)^(p-1) ; a p=4 l'exposant vaut 3, impair,
        et (-x)^3 = -(x^3) exactement ;
      - acc combine ces termes lineairement ; l'addition IEEE en
        arrondi-au-plus-proche est SYMETRIQUE autour de zero, donc
        (-a) + (-b) = -(a + b) au bit pres ;
      - les quatre etages de RK4 sont des combinaisons lineaires a
        coefficients exacts (1/2, 1/6, 2) : ils commutent avec la negation ;
      - le test d'explosion est max(|x1|, |x2|) > CAP et ~isfinite : tous
        deux INVARIANTS par changement de signe ;
      - la remise a zero apres explosion ecrit +0.0 dans les DEUX branches.
    Donc le masque d'explosion est IDENTIQUE AU BIT entre les deux signes, et
    chercher_seuil, qui bissecte sur ce masque, rend un s* identique au bit.
    CE QUE G8b CONSIGNE, aux seize points : l'egalite bit a bit du masque
    d'explosion, du nombre d'ilots, de la premiere retombee et de
    min(s explosif)/s*, entre les deux signes.
    ATTENTE ECRITE D'AVANCE : ZERO deviation, sur les seize points et sur
    l'integralite des vecteurs. Ce n'est pas une tolerance, c'est une
    identite demontree ci-dessus.
    TOUTE DEVIATION EST CONSIGNEE avec sa position, son ampleur et le nombre
    de composantes touchees. AUCUNE PORTE N'EN DEPEND : la porte reste G8a,
    a 2 pas. Motif du dedoublement : si la demonstration ci-dessus est fausse
    -- si le moteur contient une operation non symetrique que je n'ai pas
    vue -- une porte bit a bit arreterait la manche pour un artefact
    numerique. La consignation, elle, ne coute rien et dit tout.
    SENSIBILITE : G8a compare deux nombres a 2 pas pres ; G8b compare
    ~370 x 16 booleens a l'exactitude. Deux ordres de grandeur, pour zero
    machine, sur la branche a degre PAIR qui est la limitation declaree de
    cette manche et que G1' ne couvre pas.

  G7 REPERCUSSION. Toute exclusion prononcee par G2, G4, G5 ou G6 retire le
    w2 du fit COMMUN AUX TROIS DEGRES, puisque P-M11a est une comparaison
    ponctuelle. Les fits ampute et non ampute sont consignes ; seul l'ampute
    alimente les portes. Sous 8 points, les TROIS portes a verdict --
    P-M11a, P-M11b et P-M11c -- sont NON CONCLUANTES par construction :
    P-M11c est une estimation de pente et tombe avec le plancher de huit
    points au meme titre que les deux autres. La liste des w2 retenus va au JSON.

MES ATTENTES
------------
  P-M11a : j'attends CLASSE COMPATIBLE. Motif : la classe est une consequence
    algebrique de la forme g (zeta s)^(p-2) = f, et rien dans M10 ne l'a
    contredite -- mais rien ne l'a testee non plus, le systeme a deux degres
    etant exactement determine. J'attends RMS(D) sous 5e-04, soit deux fois
    le plancher garanti. Une valeur au-dessus de 2.1e-03 serait contre moi.
  P-M11a, EN CAS DE REFUTATION : j'attends alors que l'ecart soit PORTE PAR
    2.15, le point qui domine deja les residus aux deux degres de M10 et qui
    est a 0.15 de 2:1, juste au-dela du rayon 0.12. Une refutation diffuse,
    sans point dominant, serait contre moi.
  P-M11c : NON CONCLUANT, pour la raison chiffree ci-dessus. Ce n'est pas une
    attente prudente, c'est une consequence de l'identite sur PHI_j.
  beta(4) : L'ATTENTE DE v1 ETAIT FAUSSE ET JE LA RETIRE. Elle annoncait
    [0.85, 1.05] "par continuite", en extrapolant dans le MAUVAIS SENS :
    F = 0.5147 > 0, donc beta CROIT avec u = 1/(p-2), donc DECROIT avec p, et
    beta(4) doit etre AU-DESSUS de beta(5) = 1.0236, pas en dessous. La
    classe predit 1.1094. Une attente qui, realisee, aurait REFUTE la porte
    principale du gel n'etait pas une attente : c'etait une contradiction
    interne. Defaut de machine 1, releve en certification, corrige ici avant
    toute mesure.
  CE QUE J'ATTENDS REELLEMENT, ET C'EST UNE REFUTATION. Machine 2 offrait
    deux issues : adopter la prediction de la classe, ou declarer qu'on
    attend une refutation. Je prends la seconde, et voici le motif chiffre.
    La classe, calee sur M10, exige beta STRICTEMENT DECROISSANT en p :
        p=4 : 1.1094 | p=5 : 1.0236 | p=6 : 0.9807 | p=7 : 0.9550
    Les quatre beta de l'ere historique valent 0.95 / 1.02 / 0.88 / 0.91 :
    ils sont PLATS, pas decroissants, et le plus grand ecart a la classe est
    EXACTEMENT a p=4, -0.1594. J'attends donc beta(4) entre 0.90 et 1.02,
    c'est-a-dire une REFUTATION de P-M11b, et par coherence une refutation
    de P-M11a.
    CE QUI SERAIT CONTRE MOI : beta(4) au-dessus de 1.07, et RMS(D) sous
    2.1e-03 -- c'est-a-dire la classe qui tient.
    RESERVE QUE JE DECLARE MOI-MEME : les quatre beta historiques sont NON
    OPPOSABLES (E20, provenance mixte, convention non confirmee), et celui de
    p=4 est precisement celui que M11 va rendre opposable. Mon attente repose
    donc sur la mesure la plus faible du dossier. Je la maintiens telle
    quelle : c'est ce que je crois, et si la classe tient, je l'aurai
    annonce a l'envers.
  r(4) : j'attends une valeur proche de 7.4, conforme a l'ere E20, et non de
    10.2. Meme motif, meme reserve.
  P-M11f : j'attends AUCUN declenchement de G6 a p=4. Motif : G6 a tire une
    fois sur 64 lignes en M10, et M11 en compte 32. Un declenchement, ou
    plusieurs, serait contre moi -- et informatif.
  G1' : j'attends une reproduction a mieux que 0.01 %, la chaine etant
    identique a celle de M10 au degre pres.

LIMITATIONS DECLAREES
---------------------
  - M11 ne mesure qu'un degre. Elle teste la classe et ne la remplace pas :
    une refutation dit que l'amplitude pertinente depend de p, sans dire
    pourquoi. Deux causes au moins restent compatibles avec un echec --
    zeta reellement p-dependant, ou la loi de puissance en Delta trop pauvre
    pour porter phi et psi sur trois degres -- et rien dans M11 ne les separe.
    Ecrit d'avance pour qu'aucune ne soit choisie apres coup.
  - La grille est celle de M10, donc son plan est celui, faible, qui a rendu
    P-M10a NON CONCLUANT DE PUISSANCE. C'est sans effet sur P-M11a, qui est
    une identite ponctuelle et non une estimation de pente, et c'est tout
    l'effet sur P-M11c, dont l'issue est annoncee.
  - La convention (f) integrale n'a JAMAIS ete exercee sur un degre PAIR dans
    un run opposable. Le gel M10 la pose "partout", mais E20 est ne
    exactement d'un melange de conventions entre degres. Elle est donc
    re-declaree ici, et G1' en controle l'application au point ou le cote
    fragile s'inverse.
  - P-M11e porte sur des points proches des resonances, ou la classe peut
    echouer legitimement. Aucun verdict n'en sortira, dans un sens ni dans
    l'autre.
  - Le plancher de bruit qui fait foi est celui que G5 GARANTIT, non celui
    que le run obtiendra. Si le run fait mieux -- il l'a fait en M10, d'un
    facteur 17 -- cela sera consigne sans changer la porte.

IMPLEMENTATION
--------------
  m11_exposant_v1.py ecrit uniquement out/m11_results.json (incremental).
  MOTEUR : celui de m9_replication_v1.py, sha256 c8ed357b120352c4d1078307add
  3eaac285940c8bec00acc2ddc9ff386ab2c5c, IMPORTE et NON MODIFIE ; le script
  recalcule cette empreinte au demarrage et s'arrete si elle differe. Le degre
  est fixe par REBINDING de la globale de module P avant chaque bloc de degre.
  Les onze autres globales sont deja aux valeurs de ce gel et ne sont pas
  rebindees.
  SOURCES PRIMAIRES, lues et jamais codees en dur, empreinte verifiee avant
  lecture :
    out/m9_results.json  41595413f676df396994da1b7ca6c4abc59199b8ca2f93f00e
      2643c151653210   (ancres de G1')
    out/m10_results.json 7cf3624b45dd7d2bb91d29485bd14599e749bd60ba683c4b0c
      0b224a28aba3bc   (res5, res7, et l'ensemble de fit)
  Les neuf predictions de P-M11a et les sept de P-M11e sont RECALCULEES par le
  script depuis le JSON M10 et confrontees aux nombres imprimes ci-dessus ; un
  ecart superieur a 1e-09 est une erreur bloquante.
  GEL JUMEAU : le docstring du script porte ce bloc, du titre du gel jusqu'a
  sa ligne de fin incluse, canonique NFC+LF, EXTRAIT du fichier .md et non
  retranscrit ; le sha256 en est recalcule au demarrage depuis le fichier
  source du script.
  INVARIANT DE CLOTURE, verifie au --selftest AVANT tout calcul d'empreinte :
  la ligne de fin du gel n'apparait qu'UNE fois dans le fichier, en ligne
  pleine, et c'est la derniere ligne du bloc.
  REGLE 14 AU HARNAIS : tout reechantillonnage portant sur des residus REFAIT
  les ajustements sur l'echantillon reduit ; le --selftest exhibe les DEUX
  valeurs sur un cas ou elles different, pour que l'ecart soit visible et non
  suppose nul.
  PRE-VOL A MOTEUR FACTICE avant tout run long : le modele de machine 2 a paye
  deux fois, il est desormais obligatoire.
  DEPOT DU SCRIPT CONDITIONNE a la certification croisee (E19).

=== FIN DU GEL M11 ===
