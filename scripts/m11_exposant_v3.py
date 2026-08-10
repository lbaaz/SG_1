#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""PRE-ENREGISTREMENT M11 -- L1-h : LE TEST DE LA CLASSE, A TROIS DEGRES
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
"""

# =====================================================================
# m11_exposant_v1.py -- machine 1. Ecrit APRES la certification croisee de
# m11_pre_enregistrement_v4.md (E19) et de m11_note_exploitation_v1.md.
#
# GEL JUMEAU : le docstring ci-dessus a ete EXTRAIT du .md certifie par un
# generateur, jamais retranscrit.
#
# CONVENTION D'EMPREINTE, DECLAREE EN CLAIR -- c'est le point que la
# certification de la note n'a pas tranche. Trois valeurs coexistaient :
#     A  bloc SANS le saut de ligne final  1aafa892...
#     B  bloc AVEC le saut de ligne final  b3c27a14...
#     C  fichier brut entier               b3c27a14...  (identique a B)
# Machine 2 a certifie B, deux fois (v3 et v4). M10 v8 avait ete certifie
# sur A, mais son fichier portait quatre lignes de plus que son bloc : les
# deux etaient distinguables. Depuis que l'invariant de cloture (regle 12)
# impose au terminateur d'etre la derniere ligne, le bloc et le fichier ne
# different plus que d'UN OCTET, et les deux conventions sont devenues
# confusibles.
# CE SCRIPT RETIENT B, et pour une raison qui depasse la compatibilite :
# B == C, donc l'empreinte se verifie par un simple sha256sum du fichier,
# SANS AUCUNE REGLE D'EXTRACTION. Or c'est une regle d'extraction qui avait
# tronque l'empreinte de M6 a M10 v6 (D-M10-7). Supprimer la regle supprime
# la classe de defaut.
# =====================================================================

import argparse, hashlib, importlib.util, json, math, os, re, sys, unicodedata
from math import log, sqrt

import numpy as np

MARQ_DEBUT = "PRE-" + "ENREGISTREMENT M11"
MARQ_FIN = "=== FIN DU GEL M11 " + "==="

# ---- empreintes gelees -----------------------------------------------
SHA_GEL    = "b3c27a149766ac4aecb5768923ac3cce2dd1bc052ea988acc72efeb349d79dd4"
SHA_NOTE   = "51e5d26d3cf34f2461b552ca6fc08988b808f0ff39cf5eead4b55ca13858c5f5"
SHA_MOTEUR = "c8ed357b120352c4d1078307add3eaac285940c8bec00acc2ddc9ff386ab2c5c"
SHA_M9     = "41595413f676df396994da1b7ca6c4abc59199b8ca2f93f00e2643c151653210"
SHA_M10    = "7cf3624b45dd7d2bb91d29485bd14599e749bd60ba683c4b0c0b224a28aba3bc"
F_NOTE     = "m11_note_exploitation_v1.md"

# ---- protocole (gel v4) ----------------------------------------------
SQ2 = sqrt(2.0)
DEGRE = 4
GRILLE = [1.25, 1.30, 1.35, SQ2, 1.45, 1.55, 1.70, 1.80,
          1.90, 2.05, 2.15, 2.30, 2.45, 2.60, 2.75, 2.85]
FIT = [1.30, 1.70, 1.80, 2.15, 2.30, 2.45, 2.60, 2.75, 2.85]
HORS_FIT = [1.25, 1.35, SQ2, 1.45, 1.55, 1.90, 2.05]
TOL_APPART = 1e-09                      # regle 11, declaree au gel
A_COEF, B_COEF = 2.25, -1.25            # derives : a/3 + b/5 = 1/2, a + b = 1
U = lambda p: 1.0 / (p - 2)

# ---- portes (gel v4) --------------------------------------------------
PM11A_COMPAT, PM11A_REFUT = 0.01, 0.10          # % de RMS(res4 predit)
PM11B_COMPAT, PM11B_REFUT = 0.05, 0.50          # % de |beta5 - beta7|
EPS_PORTE = 1e-12
MIN_PTS_FIT = 8
PAS_GARANTI_G5 = 1.0e-05

# ---- gardes -----------------------------------------------------------
G1P_POINT, TOL_G1 = 1.80, 0.02
G2_PTS, TOL_G2, TOL_G4 = [1.35, 1.80, 2.85], 0.10, 0.02
G6_PAS_GROS, G6_PAS_FIN = 0.005, 0.002
G6_BAS, G6_MID, G6_HAUT = 0.90, 0.90, 1.30
G6_SEUIL_EXCL = 0.98
N_MAX_LIGNE = 400
G8A_PAS = 2.0                            # |sP - sM| <= 2 x pas_final

# ---- programme fige ---------------------------------------------------
RECH_CARTE = len(GRILLE) * 2             # 16 mesures + 16 controles (N-2)
RECH_G1P, RECH_G2, RECH_G4 = 2, len(G2_PTS) * 2, 1
RECH_ATTENDUES = RECH_CARTE + RECH_G1P + RECH_G2 + RECH_G4      # 41
BAL_ATTENDUS = len(GRILLE) * 2                                   # 32
# CORRECTIF 3c. RECH_ATTENDUES compte ce qui SERA fait ; or les gardes
# peuvent legitimement en retrancher -- une exclusion G5 sur un point de G2
# supprime une recherche, et le run, parfaitement conforme, s'arretait sur un
# desaccord de comptage APRES avoir tout mesure. L'invariant est donc gele
# sous sa forme DERIVEE (regle 13) :
#     recherches_comptees + recherches_sautees == RECH_ATTENDUES
# Les recherches EFFECTUEES sont comptees par ENVELOPPE du moteur, donc
# incontournables ; les SAUTEES ne peuvent l'etre qu'au site, puisqu'elles
# n'ont pas lieu. C'est l'invariant lui-meme qui police ces sites : un site
# qui oublie d'incrementer fait echouer la somme.
# D2 : le correctif 3c n'avait ete applique qu'aux RECHERCHES. La boucle
# G6/G8 saute une ligne entiere quand elle n'est pas recevable, donc DEUX
# balayages, et le test final etait reste strict. Meme forme derivee ici.
CPT = {"recherches": 0, "balayages": 0, "sautees": 0, "balayages_sautes": 0}
FOUT = os.path.join("out", "m11_results.json")

canon = lambda t: unicodedata.normalize("NFC", t).replace("\r\n", "\n").replace("\r", "\n")
cle = lambda p, w: ("%d|" + "%.12f") % (p, w)


def canon_w(x):
    for g in GRILLE:
        if abs(x - g) <= TOL_APPART:
            return g
    return x


def decle(k):
    m = k.split("|")
    return int(m[0]), canon_w(float(m[1]))


def appartient(w, ens, tol=TOL_APPART):
    return any(abs(w - e) <= tol for e in ens)


# =====================================================================
# 1. GEL JUMEAU -- invariant de cloture AVANT tout calcul d'empreinte
# =====================================================================

def invariant_cloture(txt):
    n = txt.count(MARQ_FIN)
    if n != 1:
        return False, "le terminateur apparait %d fois (exige : 1)" % n
    i = txt.index(MARQ_FIN)
    if i == 0 or txt[i - 1] != "\n":
        return False, "le terminateur n'est pas en debut de ligne"
    if txt[i + len(MARQ_FIN):].strip():
        return False, "du texte significatif suit le terminateur"
    return True, "unique, en ligne pleine, en cloture"


def bloc_du_gel(txt):
    """CONVENTION B, declaree : du titre au terminateur, SAUT FINAL INCLUS.
    Le bloc est alors le fichier entier, et l'empreinte se verifie par un
    sha256sum sans aucune regle d'extraction."""
    i = txt.index(MARQ_FIN) + len(MARQ_FIN)
    return txt[txt.index(MARQ_DEBUT): i + 1]


def certifier_gel(verbeux=True):
    src = canon(open(os.path.abspath(__file__), encoding="utf-8").read())
    ok, motif = invariant_cloture(canon(__doc__))
    if not ok:
        sys.exit("ARRET invariant de cloture (gel jumeau) : %s" % motif)
    if src.count(MARQ_FIN) != 1:
        sys.exit("ARRET invariant de cloture (source) : terminateur x%d"
                 % src.count(MARQ_FIN))
    bloc = bloc_du_gel(src)
    h = hashlib.sha256(bloc.encode()).hexdigest()
    if verbeux:
        print("Gel jumeau : %d lignes, %s" % (bloc.count("\n"), motif))
        print("  sha256 (convention B, saut final inclus) : %s" % h)
        print("  sha256 certifie v4                       : %s -> %s"
              % (SHA_GEL, "CONCORDANT" if h == SHA_GEL else "DISCORDANT"))
    if h != SHA_GEL:
        sys.exit("ARRET E19 : le gel jumeau ne correspond pas a la version certifiee.")
    return bloc, h


def empreinte_note(chemin=F_NOTE, verbeux=True):
    """Condition portee au script par la certification de la note : le JSON
    porte note_sha256, recalcule ici et jamais recopie."""
    if not os.path.exists(chemin):
        sys.exit("ARRET : la note d'exploitation est absente (%s). Le gel seul "
                 "ne suffit pas : la note prescrit trois sorties." % chemin)
    h = hashlib.sha256(open(chemin, "rb").read()).hexdigest()
    if verbeux:
        print("Note d'exploitation : %s -> %s"
              % (h[:24] + "...", "CONCORDANTE" if h == SHA_NOTE else "DISCORDANTE"))
    if h != SHA_NOTE:
        sys.exit("ARRET : la note ne correspond pas a la version certifiee.")
    return h


# =====================================================================
# 2. R-2' -- REGLE D'EXCLUSION PROLONGEE, re-derivee et jamais lue
# =====================================================================

def rayon(o):
    return 0.12 if o <= 6 else 0.03 if o <= 8 else 0.0075 if o <= 10 \
        else 0.001875 if o <= 12 else 0.0


def resonances(omax=12, lo=1.15, hi=2.95):
    return sorted({(k, l, k + l, k / l)
                   for l in range(1, omax + 1) for k in range(1, omax + 1)
                   if k + l <= omax and math.gcd(k, l) == 1 and lo <= k / l <= hi},
                  key=lambda t: t[3])


def exclu_r2p(w):
    for k, l, o, v in resonances():
        if abs(w - v) < rayon(o):
            return True, "%d:%d ordre %d a %.4f < %.6f" % (k, l, o, abs(w - v), rayon(o))
    return False, ""


def partition_r2p(grille=None):
    g = GRILLE if grille is None else grille
    fit, hors = [], []
    for w in g:
        (hors if exclu_r2p(w)[0] else fit).append(w)
    return fit, hors


# =====================================================================
# 3. FILTRE DES NOTES ET REGRESSION
# =====================================================================

note_ok = lambda n: isinstance(n, str) and n.startswith("OK|")


def pas_final(note):
    m = re.search(r"pas=([0-9.eE+-]+)", note or "")
    return float(m.group(1)) if m else None


def recevable(s, note):
    if not note_ok(note):
        return False, "note=%s" % note
    if s is None:
        return False, "seuil nul avec note OK -- incoherent"
    pas = pas_final(note)
    if pas is None:
        return False, "pas final illisible"
    if pas > PAS_GARANTI_G5 + EPS_PORTE:
        return False, "G5 pas final %.2e > %.0e" % (pas, PAS_GARANTI_G5)
    return True, ""


def ols(ws, ss):
    x = np.array([log(w * w - 1.0) for w in ws])
    y = np.array([log(v) for v in ss])
    xm, ym = x.mean(), y.mean()
    Sxx = float(((x - xm) ** 2).sum())
    b = float(((x - xm) * (y - ym)).sum() / Sxx)
    a = float(ym - b * xm)
    res = y - (a + b * x)
    n = len(x)
    sig = float(sqrt((res ** 2).sum() / (n - 2))) if n > 2 else float("nan")
    return {"beta": b, "ordonnee": a, "Sxx": Sxx, "sigma": sig,
            "SE": sig / sqrt(Sxx) if n > 2 else float("nan"), "n": n,
            "res": res, "ws": list(ws)}


# RMS declaree au gel : division par le NOMBRE DE POINTS, la meme pour D et
# pour la reference (gel v4, P-M11a).
rms = lambda v: float(sqrt(float((np.asarray(v) ** 2).sum()) / len(v)))


# =====================================================================
# 4. LECTURE DES SOURCES PRIMAIRES
# =====================================================================

def _verifie(chemin, sha, quoi):
    if not os.path.exists(chemin):
        sys.exit("ARRET : source absente : %s (%s)" % (chemin, quoi))
    h = hashlib.sha256(open(chemin, "rb").read()).hexdigest()
    if h != sha:
        sys.exit("ARRET : %s -- empreinte %s, exigee %s" % (chemin, h, sha))
    return open(chemin, encoding="utf-8").read()


def ancres_g1p(chemin=os.path.join("out", "m9_results.json")):
    carte = json.loads(_verifie(chemin, SHA_M9, "ancres G1'"))["resultats"]["carte"]
    for v in carte.values():
        if abs(float(v["w2"]) - G1P_POINT) <= TOL_APPART:
            return float(v["sP"]), float(v["sM"])
    sys.exit("ARRET : ancre G1' absente de la carte M9 a w2=%.2f" % G1P_POINT)


def m10_residus(chemin=os.path.join("out", "m10_results.json")):
    """res5 et res7 sur le fit de M10, RECALCULES depuis la carte brute et
    jamais lus du resume."""
    j = json.loads(_verifie(chemin, SHA_M10, "res5, res7 et l'ensemble de fit"))
    carte = j["resultats"]["carte"]
    fit = sorted(float(w) for w in j["resume"]["w2_retenus_par_degre"]["5"])
    if [round(w, 7) for w in fit] != [round(w, 7) for w in FIT]:
        sys.exit("ARRET : le fit de M10 (%s) differe de celui du gel M11" % fit)
    f = {p: ols(fit, [carte[cle(p, w)]["sF"] for w in fit]) for p in (5, 7)}
    return fit, f, carte


def predictions(f5, f7, ws_fit, carte, grille):
    """Les seize predictions absolues et les residus predits. Tout est
    RECALCULE ; les nombres du gel servent de CONTROLE, jamais de source."""
    r4_fit = A_COEF * f5["res"] + B_COEF * f7["res"]
    ls = lambda p, w: log(carte[cle(p, w)]["sF"])
    s4_abs = {w: math.exp(A_COEF * ls(5, w) + B_COEF * ls(7, w)) for w in grille}
    # residus predits hors fit : les droites de M10 s'evaluent hors du fit
    hors = [w for w in grille if not appartient(w, ws_fit)]
    def r(p, fp, w):
        return ls(p, w) - (fp["ordonnee"] + fp["beta"] * log(w * w - 1.0))
    r4_hors = {w: A_COEF * r(5, f5, w) + B_COEF * r(7, f7, w) for w in hors}
    b4 = A_COEF * f5["beta"] + B_COEF * f7["beta"]
    return r4_fit, s4_abs, r4_hors, b4


# =====================================================================
# 5. MOTEUR : import, empreinte, comptage par enveloppe, rebinding, G3
# =====================================================================

def charger_moteur(chemin="m9_replication_v1.py", verbeux=True):
    h = hashlib.sha256(open(chemin, "rb").read()).hexdigest()
    if verbeux:
        print("Moteur %s -> %s" % (h[:24] + "...",
                                   "CONCORDANT" if h == SHA_MOTEUR else "DISCORDANT"))
    if h != SHA_MOTEUR:
        sys.exit("ARRET : le moteur n'est pas celui que le gel designe.")
    spec = importlib.util.spec_from_file_location("m9_moteur", chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for nom, att in (("W1", 1.0), ("G_REF", 0.05), ("DT", 0.006), ("T_MAX", 400.0),
                     ("CAP", 1.0e4), ("NDENSE", 96), ("LO0", 0.05), ("HI0", 6.0),
                     ("MAX_ELARG", 8), ("NGRID", 48), ("NPASSES", 3)):
        if abs(float(getattr(mod, nom)) - float(att)) > 1e-12:
            sys.exit("ARRET : globale %s = %r, le gel exige %r"
                     % (nom, getattr(mod, nom), att))
    brut = mod.chercher_seuil
    def compte(*a, **kw):
        CPT["recherches"] += 1
        return brut(*a, **kw)
    mod.chercher_seuil = compte          # comptage EXHAUSTIF, jamais au site d'appel
    return mod


def metrique_g3(m9):
    rng = np.random.default_rng(20260726)
    x1 = rng.uniform(-2, 2, 4096); x2 = rng.uniform(-2, 2, 4096)
    dl1, dl2, e1, e2 = m9.grad_explicite(x1, x2)
    dr1, dr2 = m9.grad_rapide(x1, x2, m9.G_REF)
    return float(max(np.max(np.abs(dl1 - dr1) / (e1 + 1e-300)),
                     np.max(np.abs(dl2 - dr2) / (e2 + 1e-300))))


def rebind(m9, p, journal):
    m9.P = p
    e = metrique_g3(m9)
    journal.append({"p": p, "G3_backward": e})
    print("  rebinding m9.P = %d | G3 backward = %.3e" % (p, e))
    m9.garde_G3()
    return e


def mesurer(m9, w2, sgn, g=None, dt=None):
    g = m9.G_REF if g is None else g
    dt = m9.DT if dt is None else dt
    s, note = m9.chercher_seuil(w2, sgn=sgn, dt=dt, g=g)
    ok, motif = recevable(s, note)
    return {"s": (float(s) if s is not None else None), "note": note,
            "recevable": ok, "motif_exclusion": motif}


# =====================================================================
# 6. G6 -- DEUX BALAYAGES A PAS RELATIF CONSTANT, et G8b
# =====================================================================

def balayer(m9, w2, sgn, s_etoile):
    """Deux fenetres, PAS RELATIF gele, n calcule (gel v4, G6). Rend les deux
    masques et les consignations, separement -- note N-1."""
    lo_rel = m9.LO0 / s_etoile
    n_gros = int(math.ceil((G6_BAS - lo_rel) / G6_PAS_GROS)) + 1
    n_fin = int(round((G6_HAUT - G6_MID) / G6_PAS_FIN)) + 1
    if n_gros + n_fin > N_MAX_LIGNE:
        sys.exit("ARRET : %d points par ligne, borne declaree %d"
                 % (n_gros + n_fin, N_MAX_LIGNE))
    s_gros = np.linspace(m9.LO0, G6_BAS * s_etoile, n_gros)
    s_fin = np.linspace(G6_MID * s_etoile, G6_HAUT * s_etoile, n_fin)
    CPT["balayages"] += 1
    m_gros = m9.integrer(w2, s_gros, sgn)
    m_fin = m9.integrer(w2, s_fin, sgn)
    ex_sous = s_gros[m_gros]
    sous_seuil = s_fin[m_fin & (s_fin < G6_SEUIL_EXCL * s_etoile)]
    ilots = int(np.sum(np.diff(m_fin.astype(int)) == 1)) + (1 if m_fin[0] else 0)
    au_dessus = np.where((s_fin >= s_etoile) & (~m_fin))[0]
    return {
        "n_gros": n_gros, "n_fin": n_fin, "n_total": n_gros + n_fin,
        "pas_relatif_gros": G6_PAS_GROS, "pas_relatif_fin": G6_PAS_FIN,
        # note N-1 : les deux masques sont rapportes SEPAREMENT, avec les
        # comptes qui disent si la comparaison etait vide ou informative
        "gros_explosifs": int(m_gros.sum()),
        "fin_explosifs": int(m_fin.sum()),
        "fin_non_explosifs": int((~m_fin).sum()),
        "transition_dans_la_fenetre_fine": bool(m_fin.any() and (~m_fin).any()),
        "explosion_sous_LO0_0.90s": (float(ex_sous.min()) if len(ex_sous) else None),
        "explosion_sous_0.98s": (float(sous_seuil.min()) if len(sous_seuil) else None),
        "exclue": bool(len(sous_seuil) or len(ex_sous)),
        "ilots": ilots,
        "premiere_retombee_en_s": (float(s_fin[au_dessus[0]] / s_etoile)
                                   if len(au_dessus) else None),
        "_m_gros": m_gros, "_m_fin": m_fin,
    }


def g8b(bg_p, bg_m):
    """Symetrie bit a bit entre signes, a degre PAIR. Consignation, aucune
    porte. Rapporte SEPAREMENT le grossier et le fin (note N-1)."""
    d_gros = int(np.sum(bg_p["_m_gros"] != bg_m["_m_gros"])) \
        if bg_p["n_gros"] == bg_m["n_gros"] else -1
    d_fin = int(np.sum(bg_p["_m_fin"] != bg_m["_m_fin"])) \
        if bg_p["n_fin"] == bg_m["n_fin"] else -1
    return {
        "grossier": {"deviations": d_gros, "n": bg_p["n_gros"],
                     "explosifs_+1": bg_p["gros_explosifs"],
                     "explosifs_-1": bg_m["gros_explosifs"],
                     "pouvoir": "NUL si les deux comptes sont 0 (note N-1)"},
        "fin": {"deviations": d_fin, "n": bg_p["n_fin"],
                "explosifs_+1": bg_p["fin_explosifs"],
                "non_explosifs_+1": bg_p["fin_non_explosifs"],
                "transition_encadree": bg_p["transition_dans_la_fenetre_fine"],
                "pouvoir": "REEL si la transition est encadree (note N-1)"},
        "ilots_identiques": bg_p["ilots"] == bg_m["ilots"],
        "retombee_identique": bg_p["premiere_retombee_en_s"] == bg_m["premiere_retombee_en_s"],
        "attendu": "ZERO deviation -- identite demontree au gel, G8b",
    }


# =====================================================================
# 7. PORTES
# =====================================================================

def porte_m11a(D, ref):
    r = rms(D)
    if r <= PM11A_COMPAT * ref + EPS_PORTE:
        v = "CLASSE COMPATIBLE"
    elif r >= PM11A_REFUT * ref - EPS_PORTE:
        v = "CLASSE REFUTEE"
    else:
        v = "NON CONCLUANT"
    return v, r


def porte_m11b(b4, b5, b7):
    c = abs(b4 - A_COEF * b5 - B_COEF * b7)
    ech = abs(b5 - b7)
    if c <= PM11B_COMPAT * ech + EPS_PORTE:
        v = "COMPATIBLE"
    elif c >= PM11B_REFUT * ech - EPS_PORTE:
        v = "REFUTEE"
    else:
        v = "NON CONCLUANT"
    return v, c


def plancher(coef_somme, pas, smin):
    return coef_somme * pas / smin


# =====================================================================
# 8. SELFTEST -- ALGEBRE PURE
# =====================================================================

def selftest():
    ok = [True]; saute = [0]
    def T(nom, cond, det=""):
        ok[0] &= bool(cond)
        print("  [%s] %-56s %s" % ("OK " if cond else "ECHEC", nom, det))

    print("=== 1. INVARIANT DE CLOTURE (avant tout calcul d'empreinte) ===")
    doc = canon(__doc__)
    g, motif = invariant_cloture(doc)
    T("gel jumeau : terminateur unique, en cloture", g, motif)
    T("deux terminateurs -> REFUSE", not invariant_cloture(doc + "\n" + MARQ_FIN)[0])
    T("aucun terminateur -> REFUSE", not invariant_cloture(doc.replace(MARQ_FIN, "x"))[0])
    T("du texte apres -> REFUSE", not invariant_cloture(doc + "\nqueue")[0])

    print("=== 2. EMPREINTES, ET LA CONVENTION DECLAREE ===")
    bloc, h = certifier_gel(verbeux=False)
    T("sha256 du gel jumeau = version certifiee v4", h == SHA_GEL, h[:16] + "...")
    src = canon(open(os.path.abspath(__file__), encoding="utf-8").read())
    i = src.index(MARQ_FIN) + len(MARQ_FIN)
    ha = hashlib.sha256(src[src.index(MARQ_DEBUT):i].encode()).hexdigest()
    T("la convention A (sans saut final) donne un AUTRE hachage",
      ha != SHA_GEL, "A = %s..." % ha[:16])
    T("la convention retenue est B, et elle est declaree au source",
      "CONVENTION D'EMPREINTE, DECLAREE EN CLAIR" in src)
    if os.path.exists(F_NOTE):
        T("note d'exploitation = version certifiee", empreinte_note(verbeux=False) == SHA_NOTE)
    else:
        saute[0] += 1; print("  [SAUTE] note absente (%s)" % F_NOTE)

    print("=== 3. R-2' RE-DERIVEE, JAMAIS LUE ===")
    fit, hors = partition_r2p()
    T("R-2' rend l'ensemble de fit gele (9 points)",
      [round(x, 7) for x in fit] == [round(x, 7) for x in FIT], "%d points" % len(fit))
    T("R-2' rend le hors fit gele (7 points)",
      [round(x, 7) for x in hors] == [round(x, 7) for x in sorted(HORS_FIT)])
    T("1.25 sort par 5:4 ordre 9 sous le rayon 0.0075", "5:4" in exclu_r2p(1.25)[1],
      exclu_r2p(1.25)[1])
    T("le rayon suit le rapport 4 par paire d'ordres",
      (rayon(6), rayon(8), rayon(10), rayon(12)) == (0.12, 0.03, 0.0075, 0.001875))

    print("=== 4. APPARTENANCE PAR VALEUR (regle 11, tol 1e-09) ===")
    esp = min(b - a for a, b in zip(sorted(GRILLE), sorted(GRILLE)[1:]))
    T("tolerance tres inferieure a l'espacement minimal", TOL_APPART < esp / 1e6,
      "tol %.0e vs espacement %.4f (x%.1e)" % (TOL_APPART, esp, esp / TOL_APPART))
    T("les 16 points de la grille s'appartiennent", all(appartient(w, GRILLE) for w in GRILLE))
    T("2.40 est REJETE", not appartient(2.40, GRILLE))
    T("sqrt(2) tronque a 1.41421 est REJETE", not appartient(1.41421, GRILLE))
    T("aller-retour cle/decle exact sur les 16 points",
      all(decle(cle(DEGRE, w)) == (DEGRE, w) for w in GRILLE))

    print("=== 5. COEFFICIENTS DERIVES, JAMAIS TRANSCRITS ===")
    M = np.array([[U(5), U(7)], [1.0, 1.0]]); c = np.linalg.solve(M, np.array([U(4), 1.0]))
    T("a = +2.25 et b = -1.25, solution unique du systeme 2x2",
      abs(c[0] - A_COEF) < 1e-12 and abs(c[1] - B_COEF) < 1e-12,
      "a=%+.6f b=%+.6f" % (c[0], c[1]))

    print("=== 6. FILTRE DES NOTES (piege D-M10-9) ===")
    T("ECHEC_HAUT rejete", not recevable(None, "ECHEC_HAUT")[0])
    T("DENSE_SANS_EXPLOSION rejete MALGRE un flottant valide",
      not recevable(1.2345, "DENSE_SANS_EXPLOSION")[0])
    _s_dense = 1.2345          # ce que rend DENSE_SANS_EXPLOSION : un flottant
    T("le filtre naif (s is not None) l'aurait accepte",
      (_s_dense is not None) and not recevable(_s_dense, "DENSE_SANS_EXPLOSION")[0])
    T("note OK conforme acceptee", recevable(0.5, "OK|pas=6.03e-07")[0])
    T("pas > 1e-05 rejete par G5", not recevable(0.5, "OK|pas=3.0e-05")[0])

    print("=== 7. PORTES SUR ENTREES SYNTHETIQUES ===")
    ref = 0.21191
    T("P-M11a COMPATIBLE sous 1 %", porte_m11a(np.zeros(9), ref)[0] == "CLASSE COMPATIBLE")
    T("P-M11a REFUTEE au-dela de 10 %",
      porte_m11a(np.full(9, 0.03), ref)[0] == "CLASSE REFUTEE")
    T("P-M11a NON CONCLUANT entre les deux",
      porte_m11a(np.full(9, 0.01), ref)[0] == "NON CONCLUANT")
    T("P-M11b COMPATIBLE si la combinaison s'annule",
      porte_m11b(1.109373, 1.023585, 0.954955)[0] == "COMPATIBLE")
    T("P-M11b REFUTEE a 50 % de |beta5-beta7|",
      porte_m11b(1.109373 - 0.0686 * 0.6, 1.023585, 0.954955)[0] == "REFUTEE")

    print("=== 8. LE PLANCHER, SOUS FORME DERIVEE (regle 13) ===")
    T("plancher P-M11a = 4.5 x pas / s*_min",
      abs(plancher(4.5, 1e-5, 0.1641) - 2.741e-04) < 1e-6,
      "%.3e" % plancher(4.5, 1e-5, 0.1641))
    T("plancher P-M11b = 4.5 x somme|w| x pas / s*_min(fit)",
      abs(plancher(4.5 * 1.1494, 1e-5, 0.1789) - 2.891e-04) < 1e-6,
      "%.3e" % plancher(4.5 * 1.1494, 1e-5, 0.1789))
    T("le garanti (1e-05) majore l'obtenu de M10 (6.03e-07)", 1e-5 > 6.03e-7)

    print("=== 9. COMPTAGE DU PROGRAMME FIGE ===")
    T("41 recherches, recalculees depuis la grille",
      RECH_ATTENDUES == 41, "%d + %d + %d + %d" % (RECH_CARTE, RECH_G1P, RECH_G2, RECH_G4))
    T("32 balayages", BAL_ATTENDUS == 32)
    T("le compteur est pose par ENVELOPPE du moteur, pas au site d'appel",
      'CPT["recherches"] += 1' in src[src.index("def charger_moteur"):src.index("def metrique_g3")])

    print("=== 10. SOURCES PRIMAIRES, A FROID ===")
    for nom, ch, fn in (("m9", os.path.join("out", "m9_results.json"), ancres_g1p),
                        ("m10", os.path.join("out", "m10_results.json"), m10_residus)):
        if not os.path.exists(ch):
            saute[0] += 1; print("  [SAUTE] lecteur %s : source absente" % nom); continue
        r = fn(ch)
        T("lecteur %s rend ses valeurs" % nom, r is not None)

    print("=== 11. LES PREDICTIONS DU GEL, RECALCULEES ===")
    if os.path.exists(os.path.join("out", "m10_results.json")):
        fitw, f, carte = m10_residus()
        r4, s4, r4h, b4 = predictions(f[5], f[7], fitw, carte, GRILLE)
        REF9 = [+0.271123, -0.100669, -0.300733, -0.403714, +0.087777,
                +0.084709, +0.162025, +0.154700, +0.044783]
        T("les neuf predictions de P-M11a = celles du gel",
          all(abs(a - b) < 1e-6 for a, b in zip(r4, REF9)))
        T("RMS(res4 predit) = 0.21191", abs(rms(r4) - 0.21191) < 1e-5, "%.5f" % rms(r4))
        T("s*(4) predit a 1.25 = 0.31256113", abs(s4[1.25] - 0.31256113) < 1e-8)
        T("s*(4) predit a 2.85 = 4.62305914", abs(s4[2.85] - 4.62305914) < 1e-8)
        T("beta(4) PREDIT = 1.109373", abs(b4 - 1.109373) < 1e-6, "%.6f" % b4)
        T("r(4) predit = 10.2185", abs(s4[2.85] / s4[1.35] - 10.2185) < 1e-3,
          "%.4f" % (s4[2.85] / s4[1.35]))
        T("les sept predictions hors fit sont calculees", len(r4h) == 7)
        T("somme des residus predits nulle (deux dimensions absorbees)",
          abs(float(np.sum(r4))) < 1e-12)
    else:
        saute[0] += 3; print("  [SAUTE] predictions : m10_results.json absent")

    print("=== 12. REGLE 14 -- LES DEUX VALEURS SUR UN CAS OU ELLES DIFFERENT ===")
    # CORRECTIF 3a. La version v1 employait un indice i HERITE de la section 2
    # -- un index de CARACTERE dans le source, de l'ordre de 42661 -- si bien
    # que le slice n'otait AUCUNE composante. Le test affichait les bonnes
    # valeurs PAR COINCIDENCE : le point retire ne portait pas le maximum.
    # Un controle dont la justesse depend d'une coincidence non declaree dans
    # ses donnees n'est pas un controle.
    # Trois corrections, et non une :
    #   1. l'indice est declare LOCALEMENT et nomme sans ambiguite ;
    #   2. on prend l'ARGMAX, c'est-a-dire le cas ou l'ecart entre les deux
    #      methodes est le PLUS grand -- v1 tombait sur le cas le plus doux ;
    #   3. on VERIFIE que le retrait a bien ote une composante, de sorte que
    #      la degenerescence ne puisse pas revenir en silence.
    # NOTA : le premier correctif de 3a prenait argmax(|res|) mais mesurait
    # max(res) SIGNE. L'argmax tombant sur un residu NEGATIF, retirer sa
    # composante ne changeait pas le maximum signe : le meme accident revenait
    # sous une forme plus subtile, et la garde de LONGUEUR ne le voyait pas.
    # La statistique et l'indice doivent porter sur LA MEME quantite, et la
    # garde doit verifier que le retrait a CHANGE la statistique -- pas
    # seulement qu'il a raccourci le vecteur.
    stat = lambda v: float(np.max(np.abs(np.asarray(v))))
    ws = FIT[:]
    ys = [0.30 * (w * w - 1.0) ** 0.95 * (1 + 0.03 * math.sin(9 * w)) for w in ws]
    f0 = ols(ws, ys)
    plein = stat(f0["res"])
    j_pt = int(np.argmax(np.abs(f0["res"])))          # MEME quantite que stat
    sans = np.delete(np.asarray(f0["res"]), j_pt)
    naif = stat(sans)
    T("le retrait a ote UNE composante", len(sans) == len(f0["res"]) - 1,
      "%d -> %d, point retire : w2 = %.4f" % (len(f0["res"]), len(sans), ws[j_pt]))
    T("et il a REELLEMENT change la statistique (garde anti-degenerescence)",
      naif < plein - 1e-9, "plein %.6f -> naif %.6f" % (plein, naif))
    gj = ws[:j_pt] + ws[j_pt + 1:]; yj = ys[:j_pt] + ys[j_pt + 1:]
    refit = stat(ols(gj, yj)["res"])
    T("jackknife SANS refit et AVEC refit different sur ce cas",
      abs(naif - refit) > 1e-6, "naif %.6f | refit %.6f" % (naif, refit))
    T("l'indice employe est LOCAL, non herite d'une autre section",
      "j_pt = int(np.argmax" in src)
    T("le script emploie le REFIT", True, "regle 14")

    print("=== 13. LE SERIALISEUR, SUR LA FORME REELLE DU RESUME (D1) ===")
    import tempfile as _tf
    faux = {"meta": {"gardes": ["x"], "recherches": {"comptees": 41, "sautees": 0},
                     "_prive": "doit disparaitre"},
            "resultats": {"carte": {cle(DEGRE, 1.30): {"sF": np.float64(0.5),
                                                       "_m_fin": np.zeros(3, bool)}}},
            "resume": {"fit": {("%d" % q): {"beta": np.float64(1.0), "n": 9}
                               for q in (4, 5, 7)},
                       "residus": {("%d" % q): {"1.300000": 0.1} for q in (4, 5, 7)},
                       "P-M11a": {"D": {"1.300000": np.float64(0.0)}}}}
    vrai_fout = FOUT
    try:
        globals()["FOUT"] = os.path.join(_tf.mkdtemp(), "banc.json")
        sauver(faux)
        relu = json.load(open(FOUT, encoding="utf-8"))
        T("sauver() ecrit la forme reelle du resume sans exception", True)
        T("les clefs prefixees '_' sont retirees", "_prive" not in relu["meta"])
        T("les tableaux internes '_m_fin' sont retires",
          "_m_fin" not in relu["resultats"]["carte"][cle(DEGRE, 1.30)])
        T("les clefs de fit et residus sont des CHAINES",
          all(isinstance(k, str) for k in relu["resume"]["fit"]),
          " ".join(sorted(relu["resume"]["fit"])))
        leve = False
        try:
            sauver({"resume": {"fit": {4: {"beta": 1.0}}}})
        except TypeError:
            leve = True
        T("une clef ENTIERE fait LEVER le serialiseur, elle n'est pas convertie",
          leve, "c'etait D1 : json.dump l'aurait convertie en silence")
    finally:
        globals()["FOUT"] = vrai_fout

    print("=== 14. ATTEIGNABILITE DEPUIS main() ===")
    import ast as _a
    arbre = _a.parse(src)
    fns = {n.name: n for n in arbre.body if isinstance(n, _a.FunctionDef)}
    def joign(d, vus=None):
        vus = vus if vus is not None else set()
        for x in _a.walk(fns[d]):
            if isinstance(x, _a.Call) and isinstance(x.func, _a.Name):
                n = x.func.id
                if n in fns and n not in vus and n != "selftest":
                    vus.add(n); joign(n, vus)
        return vus
    att = joign("main")
    for nom in ("certifier_gel", "empreinte_note", "charger_moteur", "rebind",
                "partition_r2p", "m10_residus", "ancres_g1p", "predictions",
                "mesurer", "balayer", "g8b", "ols", "porte_m11a", "porte_m11b",
                "plancher", "sauver"):
        T("main() atteint %s" % nom, nom in att)
    T("selftest n'est pas dans le chemin de la manche", "selftest" not in att)
    # CORRECTIF 3b, version structurelle : res_en etait morte, cassee, et son
    # docstring AFFIRMAIT servir P-M11e. Le controle d'atteignabilite ne la
    # citait pas, donc rien ne la signalait. Desormais toute fonction du module
    # doit etre joignable depuis main() OU depuis selftest().
    att_st = joign("selftest")
    vivantes = att | att_st | {"main", "selftest"}
    mortes = sorted(set(fns) - vivantes)
    T("aucune fonction morte dans le module", not mortes,
      "mortes : %s" % (mortes if mortes else "aucune"))
    # 3c et D2 etaient le MEME defaut sur deux compteurs voisins. Le controle
    # porte donc sur la CLASSE : aucun invariant de comptage ne doit rester
    # sous forme stricte "compte == litteral".
    # DIXIEME OCCURRENCE DU MEME PIEGE, et cette fois dans les deux lignes
    # ecrites pour le detecter : une aiguille litterale se trouve elle-meme.
    # Le commentaire qui expliquait la version precedente contenait le motif
    # cherche, et le controle suivant contenait la chaine qu'il comptait.
    # Aiguilles CONSTRUITES, et les lignes de commentaire sont exclues du
    # balayage : un controle qui lit un source ne lit pas ses propres gloses.
    aig_cpt = "CPT" + "["
    code = [l.strip() for l in src.split("\n") if not l.strip().startswith("#")]
    lignes_cpt = [l for l in code
                  if aig_cpt in l and "!=" in l and "src" not in l and "count(" not in l]
    strict = [l for l in lignes_cpt if "+" not in l.split("!=")[0]]
    T("aucun invariant de comptage sous forme stricte", not strict,
      "%d comparaison(s), toutes en somme" % len(lignes_cpt)
      if not strict else "restants : %s" % strict)
    inv_r = 'CPT["recherches"] + CPT["' + 'sautees"] != RECH_ATTENDUES'
    inv_b = 'CPT["balayages"] + CPT["' + 'balayages_sautes"] != BAL_ATTENDUS'
    T("les deux invariants sont sous forme derivee",
      src.count(inv_r) == 1 and src.count(inv_b) == 1,
      "recherches x%d | balayages x%d" % (src.count(inv_r), src.count(inv_b)))

    print()
    if saute[0]:
        print("SELFTEST INCOMPLET : %d controle(s) saute(s) faute de source." % saute[0])
    print("SELFTEST : %s" % ("TOUT PASSE" if ok[0] else "*** ECHEC ***"))
    return 0 if ok[0] else 1


# =====================================================================
# 9. MANCHE
# =====================================================================

def sauver(res):
    os.makedirs("out", exist_ok=True)
    def nettoie(o):
        if isinstance(o, dict):
            # D1, version STRUCTURELLE : le serialiseur REFUSE ce que JSON ne
            # sait pas representer fidelement, au lieu de le convertir en
            # silence. Une clef non-chaine reintroduite un jour tombe alors au
            # PROCHAIN sauver() -- incremental, donc dans les secondes -- et
            # non au dernier, apres quarante minutes de mesure.
            for k in o:
                if not isinstance(k, str):
                    raise TypeError(
                        "clef non-chaine %r (%s) : JSON n'a pas de clefs "
                        "entieres et json.dump l'aurait convertie en silence"
                        % (k, type(k).__name__))
            return {k: nettoie(v) for k, v in o.items() if not k.startswith("_")}
        if isinstance(o, list):
            return [nettoie(v) for v in o]
        if isinstance(o, (np.floating, np.integer)):
            return o.item()
        if isinstance(o, np.ndarray):
            return o.tolist()
        return o
    with open(FOUT, "w", encoding="utf-8") as f:
        json.dump(nettoie(res), f, indent=1, sort_keys=True, ensure_ascii=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--moteur", default="m9_replication_v1.py")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())

    bloc, hgel = certifier_gel()
    hnote = empreinte_note()
    m9 = charger_moteur(a.moteur)
    fitr, _ = partition_r2p()
    if [round(x, 7) for x in fitr] != [round(x, 7) for x in FIT]:
        sys.exit("ARRET : R-2' ne rend pas l'ensemble de fit gele.")
    fitw, f10, carte10 = m10_residus()
    r4_pred, s4_pred, r4_hors, b4_pred = predictions(f10[5], f10[7], fitw, carte10, GRILLE)

    res = {"meta": {"gel_sha256_bloc": hgel, "note_sha256": hnote,
                    "moteur_sha256": SHA_MOTEUR, "m10_sha256": SHA_M10,
                    "convention_empreinte": "B -- bloc saut final inclus = fichier",
                    "G3_par_degre": [], "gardes": [], "exclusions": {},
                    "balayages_nature": "16 MESURES (sgn +1) et 16 CONTROLES "
                                        "(sgn -1) -- note N-2"},
           "predictions": {"res4_fit": {("%.6f" % w): float(v)
                                        for w, v in zip(fitw, r4_pred)},
                           "s4_absolu": {("%.6f" % w): v for w, v in s4_pred.items()},
                           "res4_hors_fit": {("%.6f" % w): v for w, v in r4_hors.items()},
                           "beta4": b4_pred},
           "resultats": {"carte": {}, "G2": {}, "G4": {}, "G6": {}, "G8": {}}}
    jg3 = res["meta"]["G3_par_degre"]

    # --- G1' : custody de la chaine, a p=5
    print("\n--- G1' : custody de la chaine (p=5, w2=%.2f) ---" % G1P_POINT)
    aP, aM = ancres_g1p()
    rebind(m9, 5, jg3)
    for sgn, anc in ((+1, aP), (-1, aM)):
        m = mesurer(m9, G1P_POINT, sgn)
        if not m["recevable"]:
            sys.exit("ARRET G1' : %s" % m["motif_exclusion"])
        ec = abs(m["s"] / anc - 1.0)
        l = ("G1' p=5 w2=%.4f sgn=%+d : %.10f vs %.10f (%.4f %%) -> %s"
             % (G1P_POINT, sgn, m["s"], anc, 100 * ec, "PASSE" if ec <= TOL_G1 else "ECHEC"))
        print("  " + l); res["meta"]["gardes"].append(l)
        if ec > TOL_G1:
            sys.exit("ARRET G1' : ecart %.2f %%" % (100 * ec))

    # --- carte p=4 : 16 mesures (+1) et 16 controles (-1)
    print("\n--- CARTE p=4 : 16 mesures et 16 controles ---")
    rebind(m9, DEGRE, jg3)
    for w in GRILLE:
        v = res["resultats"]["carte"].setdefault(cle(DEGRE, w), {})
        for sgn, k in ((+1, "sP"), (-1, "sM")):
            v[k] = mesurer(m9, w, sgn)
            sauver(res)
        if v["sP"]["recevable"] and v["sM"]["recevable"]:
            v["sF"] = min(v["sP"]["s"], v["sM"]["s"])
            v["frag"] = 1 if v["sP"]["s"] <= v["sM"]["s"] else -1
            v["asym"] = v["sP"]["s"] / v["sM"]["s"]
        else:
            v["sF"] = None; v["frag"] = None
            res["meta"]["exclusions"].setdefault("%.6f" % w, []).append(
                "G5 : %s" % (v["sP"]["motif_exclusion"] or v["sM"]["motif_exclusion"]))
        print("  w2=%.4f : sP %s | sM %s" % (w, v["sP"]["note"], v["sM"]["note"]))
        sauver(res)

    # --- G8a, G6 et G8b
    print("\n--- G6, G8a, G8b ---")
    anomalies = []
    for w in GRILLE:
        v = res["resultats"]["carte"][cle(DEGRE, w)]
        if v["sF"] is None:
            CPT["balayages_sautes"] += 2      # D2 : les deux signes
            res["meta"]["gardes"].append(
                "G6 w2=%.4f : deux balayages SAUTES (ligne non recevable)" % w)
            continue
        # 3d : chaque recherche rend sa valeur a UN pas pres, donc l'ecart
        # tolerable est pas_P + pas_M, majore par 2 x max des deux. N'employer
        # que le pas de sP rendrait la garde trop STRICTE si le signe -1
        # converge moins bien, et DEUX anomalies arretent la manche.
        pas = max(pas_final(v["sP"]["note"]) or PAS_GARANTI_G5,
                  pas_final(v["sM"]["note"]) or PAS_GARANTI_G5)
        ec = abs(v["sP"]["s"] - v["sM"]["s"])
        g8a = {"ecart_absolu": ec, "en_pas": ec / pas,
               "verdict": "OK" if ec <= G8A_PAS * pas else "ANOMALIE"}
        if g8a["verdict"] == "ANOMALIE":
            anomalies.append(w)
        bg = {}
        for sgn, k in ((+1, "sP"), (-1, "sM")):
            bg[k] = balayer(m9, w, sgn, v[k]["s"])
            res["resultats"]["G6"][cle(DEGRE, w) + "|%+d" % sgn] = bg[k]
            if bg[k]["exclue"]:
                res["meta"]["exclusions"].setdefault("%.6f" % w, []).append(
                    "G6 sgn=%+d explosion sous seuil" % sgn)
        res["resultats"]["G8"][cle(DEGRE, w)] = {"G8a": g8a, "G8b": g8b(bg["sP"], bg["sM"])}
        print("  w2=%.4f : G8a %s (%.2f pas) | G8b gros %d / fin %d deviations"
              % (w, g8a["verdict"], g8a["en_pas"],
                 res["resultats"]["G8"][cle(DEGRE, w)]["G8b"]["grossier"]["deviations"],
                 res["resultats"]["G8"][cle(DEGRE, w)]["G8b"]["fin"]["deviations"]))
        sauver(res)
    if len(anomalies) >= 2:
        sauver(res)
        sys.exit("ARRET G8a : %d anomalies de symetrie (%s). Une est toleree, "
                 "deux ne le sont pas." % (len(anomalies), anomalies))

    # --- G2 et G4
    print("\n--- G2 et G4 ---")
    rebind(m9, DEGRE, jg3)
    for w in G2_PTS:
        for sgn, k in ((+1, "sP"), (-1, "sM")):
            av = res["resultats"]["carte"][cle(DEGRE, w)][k]
            if not av["recevable"]:
                CPT["sautees"] += 1           # 3c : la garde retranche, on compte
                res["meta"]["gardes"].append(
                    "G2 w2=%.4f sgn=%+d : recherche SAUTEE (ligne non recevable)"
                    % (w, sgn))
                continue
            b = mesurer(m9, w, sgn, g=2 * m9.G_REF)
            Ka = m9.G_REF * av["s"] ** (DEGRE - 2)
            Kb = 2 * m9.G_REF * b["s"] ** (DEGRE - 2) if b["recevable"] else None
            ecart = abs(Kb / Ka - 1.0) if Kb else None
            ok2 = ecart is not None and ecart <= TOL_G2 + EPS_PORTE
            res["resultats"]["G2"]["%.6f|%+d" % (w, sgn)] = {
                "K_g": Ka, "K_2g": Kb, "ecart": ecart,
                "verdict": "PASSE" if ok2 else "ECHEC"}
            if not ok2:
                res["meta"]["exclusions"].setdefault("%.6f" % w, []).append("G2 echec")
            print("  G2 w2=%.4f sgn=%+d : ecart %s"
                  % (w, sgn, "%.2f %%" % (100 * ecart) if ecart is not None else "n/a"))
    best = None
    for w in GRILLE:
        v = res["resultats"]["carte"][cle(DEGRE, w)]
        for sgn, k in ((+1, "sP"), (-1, "sM")):
            if not v[k]["recevable"]:
                continue
            e = m9.G_REF * v[k]["s"] ** (DEGRE - 1)
            if best is None or e > best[0]:
                best = (e, w, sgn, v[k]["s"])
    if not best:
        CPT["sautees"] += 1                   # 3c : G4 sans ligne recevable
        res["meta"]["gardes"].append("G4 : recherche SAUTEE (aucune ligne recevable)")
    if best:
        e, w, sgn, sref = best
        r2 = mesurer(m9, w, sgn, dt=m9.DT / 2)
        ec = abs(r2["s"] / sref - 1.0) if r2["recevable"] else None
        okg4 = ec is not None and ec <= TOL_G4 + EPS_PORTE
        res["resultats"]["G4"] = {"echelle_force": e, "w2": w, "sgn": sgn,
                                  "s_dt": sref, "s_dt2": r2["s"], "ecart": ec,
                                  "verdict": "PASSE" if okg4 else "NON FIABLE"}
        if not okg4:
            res["meta"]["exclusions"].setdefault("%.6f" % w, []).append("G4 NON FIABLE")
        print("  G4 w2=%.4f sgn=%+d : ecart %s"
              % (w, sgn, "%.3f %%" % (100 * ec) if ec is not None else "n/a"))
    sauver(res)

    # --- G7, fit, portes
    print("\n--- G7, fit, portes ---")
    exclus = {float(k) for k, v in res["meta"]["exclusions"].items() if v}
    retenus = [w for w in FIT
               if res["resultats"]["carte"][cle(DEGRE, w)]["sF"] is not None
               and not any(abs(w - e) <= TOL_APPART for e in exclus)]
    res["meta"]["w2_retenus"] = retenus
    r = {"w2_retenus": retenus, "n_fit": len(retenus)}
    if len(retenus) < MIN_PTS_FIT:
        r["P-M11a"] = r["P-M11b"] = r["P-M11c"] = {
            "verdict": "NON CONCLUANT PAR CONSTRUCTION",
            "motif": "%d points < %d" % (len(retenus), MIN_PTS_FIT)}
    else:
        f4 = ols(retenus, [res["resultats"]["carte"][cle(DEGRE, w)]["sF"] for w in retenus])
        f5 = ols(retenus, [carte10[cle(5, w)]["sF"] for w in retenus])
        f7 = ols(retenus, [carte10[cle(7, w)]["sF"] for w in retenus])
        r4p = A_COEF * f5["res"] + B_COEF * f7["res"]
        D = f4["res"] - r4p
        va, rmsD = porte_m11a(D, rms(r4p))
        vb, comb = porte_m11b(f4["beta"], f5["beta"], f7["beta"])
        smin = min(min(res["resultats"]["carte"][cle(DEGRE, w)]["sF"] for w in retenus),
                   min(carte10[cle(p, w)]["sF"] for p in (5, 7) for w in retenus))
        x = np.array([log(w * w - 1.0) for w in retenus])
        sw = float(np.abs((x - x.mean()) / f4["Sxx"]).sum())
        # CORRECTIF D1 : clefs CHAINE des la construction. JSON n'a pas de
        # clefs entieres ; json.dump les aurait converties EN SILENCE, rendant
        # le fichier incoherent avec le code qui le relit -- et nettoie()
        # tombait dessus au tout DERNIER sauver(), apres les 41 recherches et
        # les 32 balayages.
        r["fit"] = {("%d" % q): {k: v for k, v in fp.items() if k != "res"}
                    for q, fp in ((4, f4), (5, f5), (7, f7))}
        r["residus"] = {("%d" % q): {("%.6f" % w): float(z)
                                     for w, z in zip(retenus, fp["res"])}
                        for q, fp in ((4, f4), (5, f5), (7, f7))}
        r["P-M11a"] = {"verdict": va, "RMS_D": rmsD, "RMS_ref": rms(r4p),
                       "D": {("%.6f" % w): float(z) for w, z in zip(retenus, D)},
                       "plancher_garanti": plancher(4.5, PAS_GARANTI_G5, smin),
                       "contraintes_independantes": len(retenus) - 2}
        r["P-M11b"] = {"verdict": vb, "combinaison": comb,
                       "beta4_predit": A_COEF * f5["beta"] + B_COEF * f7["beta"],
                       "beta4_mesure": f4["beta"],
                       "plancher_garanti": plancher(4.5 * sw, PAS_GARANTI_G5, smin),
                       "plancher_du_gel": 2.891e-04}
        r["P-M11c"] = {"beta4": f4["beta"], "SE": f4["SE"], "sigma": f4["sigma"],
                       "Sxx": f4["Sxx"],
                       "attente_declaree": "NON CONCLUANT -- l'etendue de grille "
                                           "vaut 2.8 fois l'ecart des mecanismes"}
        r["P-M11d"] = {"ecarts_absolus": {
            ("%.6f" % w): (log(res["resultats"]["carte"][cle(DEGRE, w)]["sF"])
                           - log(s4_pred[w]))
            for w in GRILLE
            if res["resultats"]["carte"][cle(DEGRE, w)]["sF"] is not None}}
        r["P-M11g"] = {"r4_mesure": (res["resultats"]["carte"][cle(DEGRE, 2.85)]["sF"]
                                     / res["resultats"]["carte"][cle(DEGRE, 1.35)]["sF"]
                                     if all(res["resultats"]["carte"][cle(DEGRE, w)]["sF"]
                                            for w in (1.35, 2.85)) else None),
                       "r4_predit": 10.2185, "r4_ere_E20": 7.44}
        print("  beta(4) = %.6f | predit %.6f" % (f4["beta"], r["P-M11b"]["beta4_predit"]))
        print("  P-M11a : %s (RMS(D) = %.3e)" % (va, rmsD))
        print("  P-M11b : %s (combinaison = %.3e)" % (vb, comb))
    res["resume"] = r

    res["meta"]["script_sha256"] = hashlib.sha256(
        open(os.path.abspath(__file__), "rb").read()).hexdigest()
    res["meta"]["date_utc"] = __import__("datetime").datetime.utcnow().strftime(
        "%Y-%m-%dT%H:%M:%SZ")
    res["meta"]["recherches"] = {"comptees": CPT["recherches"],
                                 "sautees": CPT["sautees"],
                                 "somme": CPT["recherches"] + CPT["sautees"],
                                 "attendues": RECH_ATTENDUES,
                                 "invariant": "comptees + sautees == attendues"}
    res["meta"]["balayages"] = {"comptes": CPT["balayages"],
                                "sautes": CPT["balayages_sautes"],
                                "somme": CPT["balayages"] + CPT["balayages_sautes"],
                                "attendus": BAL_ATTENDUS,
                                "invariant": "comptes + sautes == attendus"}
    sauver(res)
    if CPT["recherches"] + CPT["sautees"] != RECH_ATTENDUES:
        sys.exit("ARRET : %d recherches effectuees + %d sautees = %d, le "
                 "PROGRAMME FIGE en declare %d. Un site de saut n'a pas compte."
                 % (CPT["recherches"], CPT["sautees"],
                    CPT["recherches"] + CPT["sautees"], RECH_ATTENDUES))
    if CPT["balayages"] + CPT["balayages_sautes"] != BAL_ATTENDUS:
        sys.exit("ARRET : %d balayages effectues + %d sautes = %d, le PROGRAMME "
                 "FIGE en declare %d. Un site de saut n'a pas compte."
                 % (CPT["balayages"], CPT["balayages_sautes"],
                    CPT["balayages"] + CPT["balayages_sautes"], BAL_ATTENDUS))
    print("\nEcrit : %s" % FOUT)
    print("Recherches : %d + %d sautees = %d / %d | balayages : %d + %d sautes"
          " = %d / %d"
          % (CPT["recherches"], CPT["sautees"], CPT["recherches"] + CPT["sautees"],
             RECH_ATTENDUES, CPT["balayages"], CPT["balayages_sautes"],
             CPT["balayages"] + CPT["balayages_sautes"], BAL_ATTENDUS))
    print("sha256 du JSON : %s" % hashlib.sha256(open(FOUT, "rb").read()).hexdigest())


if __name__ == "__main__":
    main()
