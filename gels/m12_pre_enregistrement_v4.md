PRE-ENREGISTREMENT M12 -- TEST PONCTUEL DE LA CLASSE, SANS AUCUN AJUSTEMENT
(gele avant l'ecriture de toute ligne de code ; bloc ASCII, canonique NFC+LF ;
nom de fichier versionne, regle E19-2 -- version v4)

HISTORIQUE DU GEL
  v1 48ffd952 : NON CERTIFIE (certification 7225c2ca, 01/08 -- date corrigee
      en v3). Six corrections, deux de fond.
  v2 4eed58b2 : NON CERTIFIE (certification 4aa88115, 01/08). Defaut de
      fond : filtre de nouveaute evalue en flottant ; erratum E28 consigne
      par machine 2 contre sa certification v1.
  v3 6134cd82 : CERTIFIE (certification fc61a25c, 01/08). Lecture A tranchee,
      fenetres et liste re-derivees par les deux machines en arithmetiques
      exactes independantes.
  PILOTE, EXECUTE ET OPPOSABLE (01/08) : gel v3 03e29c86 certifie ; script
      m12_pilote_v3.py 663b17e2, certifie par 774f7de4 ; run sur BOCAL4,
      out/m12_pilote_results.json ed0e27b1 ; message de run et
      reconciliation machine 2, 05147405. TOUTES LES GARDES PASSENT.
      Acquis : CALIBRATION 24/24 AU BIT (l'attente G1 du gel pilote --
      "0.2 a 2 %, pas mieux" -- est FALSIFIEE dans le bon sens ; son motif
      etait errone, la geometrie de balayage ne touche pas la recherche, et
      cela est consigne au registre SANS reecrire l'attente) ; le
      diagnostic qu'E27 exigeait est RENDU (la geometrie neuve regarde sous
      s*, l'ancienne n'y consignait rien). Attrition : UNE ligne perdue sur
      douze, 7|1.70|-1 (G6, explosion a 0.90 s* -- s_fin[0], a 3.6e14
      epsilons du bord, temoins S4/S6 sur donnee) ; q_L(80 %) =
      0.2296169327 ; D-N rend N = 13 > 12 : ARRET EXECUTE -- premier arret
      de regle de la campagne, du premier coup, conformement au delta 44.7.
      L'attente G6 du pilote ("0 ou 1 ligne") est TENUE, et la manche
      s'arrete quand meme : la divergence attente/regle consignee avant le
      run s'est realisee.
  v4. Execute la voie que la clause d'arret de v3 prescrivait : la CAPACITE
      de la liste est raffinee. Le plafond 12 de v1-v3 n'etait PAS DERIVE --
      il suivait la table indicative -- et c'est cette constante, elle
      seule, qui a declenche l'arret. Le plafond de v4 est DERIVE :
      l'EPUISEMENT des deux passes declarees, 8 + 8 = 16. La liste est
      etendue aux rangs 13-16 par les MEMES regles, sur la MEME grille,
      sans aucune regle nouvelle ; l'espacement minimal passe de 0.0200 a
      0.0100 et le controle rule-11 est relu en consequence. D-N recoit son
      intrant OPPOSABLE et rend N = 13, minimalite montree par encadrement ;
      le programme est fige a 75 recherches. Les quatre points du pilote
      restent BRULES et hors liste. AUCUNE attente reecrite : la section
      MES ATTENTES est copiee de v1 a l'identique, pour la quatrieme fois.
      (Statut d'erratum du plafond non derive de v1-v3 : decision de
      registre, hors de ce bloc, E18 -- rien n'est reserve ici.)
  AUCUN code de M12 avant qu'un message de certification croisee cite
  l'empreinte de ce bloc (E19-1). Le script s'appellera m12_ponctuel_v1.py.
  C2 NE S'APPLIQUE PAS : M12 est integralement CLASSIQUE -- aucune
  diagonalisation, aucun T_coquille, aucun rho quantique. La clause de
  rearmement interdit une manche QUANTIQUE sans estimateur change ET derive ;
  elle ne bloque pas le programme classique.
  AUCUN BLOC SUBORDONNE RESTANT : le pilote a couru. Son unique nombre
  transmis est l'intrant de la regle D-N, cite plus bas avec sa provenance.

QUESTION
--------
Le bloc L1 v4 (dbe633e2, clos) etablit, sous sa forme BRUTE :
      ln s*_p(w2) = A(w2) . u_p + B(w2),   u_p = 1/(p-2),   PONCTUELLEMENT
A et B sont des fonctions LIBRES de w2 : la classe n'impose aucune forme en
w2, elle impose une structure en p, en chaque w2 separement.

Trois degres mesurent deux parametres. La matrice de conception 3x2 est de
rang 2 (verifie) : le systeme est surdetermine par EXACTEMENT UNE contrainte,
      E(w2) = ln s*_4 - 2.25 . ln s*_5 + 1.25 . ln s*_7 = 0
Les coefficients sont DERIVES et UNIQUES : imposer a.u_5 + b.u_7 = u_4 et
a + b = 1 donne, en arithmetique exacte, a = 9/4 et b = -5/4. L'identite a ete
verifiee symboliquement sur trois couples (A, B) independants.
M12 mesure E en chaque point. AUCUN ajustement n'intervient nulle part.

POURQUOI CETTE MANCHE, ET POURQUOI MAINTENANT
---------------------------------------------
M10 et M11 sont mortes du meme cote : le FIT. G6 a retranche 1.25 en M10, puis
1.30, 1.55 et 1.80 en M11 ; le fit est tombe de 9 a 7 points, sous le plancher
de huit, et trois portes sont tombees par construction. Le levier, Sxx, le
plancher, le dossier de conception des S35-S39 : tout cela protegeait un
ajustement.
E ne traverse NI regression, NI levier, NI Sxx, NI plancher. C'est le premier
chemin vers la question principale que sa cause de mort ne traverse pas.
CONSEQUENCE ASSUMEE : M12 ne mesure PAS beta. Elle teste la classe. Si la
classe tient, beta redevient une cible legitime ; si elle tombe, beta n'a plus
de sens comme objet a une seule valeur par degre.

DERIVATIONS PREALABLES (faites et verifiees AVANT ce gel)
---------------------------------------------------------
(a) Unicite des coefficients : arithmetique exacte (Fraction), a = 9/4,
    b = -5/4 ; identite testee sur (A,B) = (1,0), (0,1), (3/7, -11/5).
(b) Surdetermination : rang 2 sur la matrice [[u_p, 1]] pour p = 4, 5, 7,
    donc exactement un residu. Ni zero (le test existerait pas), ni deux.
(c) BRUIT DE BRACKET, FORME DERIVEE (regle 13 ; correction S1, cert. v1).
    Le pas de G5 est ABSOLU, donc d ln s*_p = pas_p / s*_p, AMPLIFIE aux
    petits s* (cartes certifiees : s*(5) < 1 jusqu'a w2 = 2.15 inclus,
    s*(7) < 1 jusqu'a 2.30 inclus). FORME GELEE, evaluee PAR POINT depuis
    les valeurs mesurees :
        sigma_E(w2)     = sqrt( sum_p ( c_p . pas_p / s*_p(w2) )^2 )
        sigma_E_max(w2) =        sum_p   c_p . pas_p / s*_p(w2)
        c = (1, 2.25, 1.25) ; pas_p = pas final de la recherche du signe
        retenu par la convention (f) au point considere (p=4 : signe unique).
    Les DEUX valeurs sont consignees au JSON, par point ; G9 les couvre.
    ANCRAGE DE CONCEPTION (recalcul machine 2 sur cartes certifiees,
    certifications 7225c2ca et 4aa88115) : sur les douze de la liste v3,
    quadrature de 1.18e-5 a 4.36e-5, pire cas jusqu'a 6.55e-5 au point le
    plus a gauche (1.73). Les seuils de P-M12a se lisent AU PIRE POINT :
        0.03 = 458 x sigma_E_max(pire)   ;   0.10 = 1527 x.
    MARGE SUPPLEMENTAIRE, non revendiquee : le pas final reellement obtenu
    est 6.03e-07 sur 23 des 25 recherches du pilote et 1.82e-06 sur les
    deux autres (ed0e27b1), seize fois sous le plafond G5 au pire.
    COMPLEMENT v4 : les quatre entrants de la liste (1.74, 1.77, 1.86,
    2.57) sont interieurs a [1.73, 2.80] en w2. La lecture "au pire point"
    reste 1.73 SI sigma_E y demeure maximal sur les SEIZE -- POINT DE
    CERTIFICATION EXPLICITE pour machine 2, qui detient les cartes. A
    defaut, l'ancrage serait relu au nouveau pire point ; les seuils,
    declares arbitraires et anterieurs a toute mesure, ne changeraient pas.
(d) R-2' N'EST PAS UNE CONDITION DE VALIDITE ICI, et c'est une difference de
    fond avec M10 et M11. R-2 existait pour proteger une REGRESSION : un point
    resonant a un s* anormal qui deforme une pente. Or A et B sont des
    fonctions libres de w2 : un canyon resonant est ABSORBE par A(w2) et B(w2),
    et E doit valoir zero DANS le canyon comme ailleurs si la classe est vraie.
    R-2' est donc conservee pour une seule raison, declaree : REDUIRE
    L'ATTRITION, les points resonants etant plus exposes a G6. Aucune lecture
    de M12 ne s'appuie sur l'exclusion des resonances.

CHOIX DES POINTS -- MECANIQUE, ET ANTERIEUR A TOUTE MESURE
-----------------------------------------------------------
REGLE R-2' (gelee au S38.6, continuation geometrique de R-2, rapport 4 par
paire d'ordres, reprise ici SANS MODIFICATION) :
      ordre <= 6 : rayon 0.12 | 7-8 : 0.03 | 9-10 : 0.0075 | 11-12 : 0.001875
      au-dela de l'ordre 12 : R-2 ne declare rien, et M12 non plus.
MARGE, declaree : un point est retenu si d >= 1.10 x rayon pour TOUTE fraction
k/l d'ordre k+l <= 12. Motif : sans marge, 1.38 tombe a exactement 1.00 rayon
de 3:2 et 1.63 a 1.08 -- un arrondi deciderait de la grille. La marge est un
RESSERREMENT, jamais un relachement. CENSUS, fait avant gel et FORCE par
l'argument 5-adique (cert. v3 : les seuils 1.10 x rayon portent 5^3 au
denominateur, les distances centieme-resonance au plus 5^2) : AUCUN candidat
ne tombe exactement sur la marge.
NOUVEAUTE (LECTURE A, tranchee en v3) : d >= 0.03 de tout point de la grille
M10/M11, la comparaison evaluee en ARITHMETIQUE EXACTE -- entiers de
centiemes, |W - G| >= 3 ; le point de grille sqrt(2) est traite par
encadrement rationnel (1.41421356237 < sqrt(2) < 1.41421356238), qui tranche
chaque candidat sans ambiguite. TREIZE candidats touchent le seuil a 3/100
EXACT ; ONZE sont retenus par la regle ecrite, 1.27 et 1.28 restent exclus
dans toute lecture (point de grille a 0.02). Les quatre que la lecture
flottante excluait a tort : 2.27, 2.63, 2.72, 2.78.
AUTRES REGLES INCHANGEES : les quatre points du pilote (1.70, 2.15, 2.45,
2.75) sont exclus par la nouveaute (points de grille, d = 0) et BRULES.
GRILLE DE CANDIDATS : multiples de 0.01 dans [1.26, 2.85].

RESULTAT, RE-DERIVE PAR LES DEUX MACHINES EN ARITHMETIQUES EXACTES
INDEPENDANTES (Fraction cote machine 2, entiers de centiemes cote machine 1 --
E28 applique) : il existe exactement HUIT fenetres propres, toutes a partir
de 1.73 --
      [1.73,1.74] [1.76,1.77] [1.83,1.86] [2.18,2.27]
      [2.35,2.42] [2.54,2.57] [2.63,2.72] [2.78,2.82]

LISTE DE PRIORITE, GELEE -- SEIZE RANGS
(regle INCHANGEE : fenetres triees par largeur decroissante, egalite -> plus
petit w2 ; passe 1 = mediane basse de chaque fenetre ; passe 2 = le point le
plus eloigne du retenu de passe 1 dans la meme fenetre, egalite -> plus petit
w2. PLAFOND DERIVE, correction v4 : l'EPUISEMENT des deux passes declarees,
un candidat par fenetre et par passe, 8 + 8 = 16 ; le plafond 12 de v1-v3
n'etait pas derive et suivait la table indicative. Au-dela de 16, une passe 3
exigerait une regle NOUVELLE, qui n'est pas ecrite ici.) :
       1. 2.22    2. 2.67    3. 2.38    4. 2.80    5. 1.84    6. 2.55
       7. 1.73    8. 1.76    9. 2.27   10. 2.72   11. 2.42   12. 2.78
      13. 1.86   14. 2.57   15. 1.74   16. 1.77
LE PROGRAMME PORTE SUR LES N = 13 PREMIERS (application opposable de D-N,
ci-dessous). Les rangs 14-16 existent par la meme derivation et ne sont AU
PROGRAMME D'AUCUNE MANCHE : aucun statut de reserve implicite ; toute
utilisation future exigerait son propre gel.
Controle rule-11, a executer par le script : chaque w2 mesure appartient a
cette liste PAR VALEUR, tolerance 1e-9, soit 1e7 fois sous l'espacement
minimal de la liste, qui vaut 0.01 (entre 1.73 et 1.74, et entre 1.76 et
1.77 ; il valait 0.02 sur les douze de v3 -- la marge reste de sept ordres).
EGALITES : le census des passes ETENDUES ne produit AUCUNE egalite nouvelle.
Celle du rang 12 ([2.78, 2.82], extremes a 2/100 exacts de 2.80, tranchee
2.78 par le departage ecrit avant d'etre rencontree) reste la SEULE exercee
de toute la selection.
L'EGALITE DU RANG 9 CONSIGNEE EN v2 ([2.18,2.26], 1/25 des deux cotes de
2.22) etait un ARTEFACT de la lecture flottante : la fenetre exacte est
[2.18,2.27] et le point le plus eloigne y est 2.27, seul. Retiree en v3
(symptome du defaut de fond, cert. v2) ; le departage de passe 2 qu'elle
avait fait ecrire reste declare -- c'est lui qui tranche le rang 12.
REGLE ELARGIE (cert. v2), gelee pour cette manche : TOUTE comparaison dont le
resultat peut basculer sous une perturbation de l'ordre de l'epsilon machine
-- egalite, ou inegalite evaluee sur son bord -- s'evalue en arithmetique
EXACTE quand les entrees sont exactes, a tolerance declaree sinon.
(Promotion en regle transversale ou en erratum : decision hors de ce bloc,
E18 -- rien n'est reserve ici.)

REGLE D-N -- FORME INCHANGEE ; INTRANT DESORMAIS OPPOSABLE
-----------------------------------------------------------
      q_L  = borne superieure unilaterale a 80 % du taux de perte par LIGNE,
             telle que rendue par le pilote (consignation C-P5)
      s_pt = (1 - q_L)^3            [trois degres, G7 repercute]
      N    = min { n >= 4 : P(Binomiale(n, s_pt) >= 4) >= 0.90 }
APPLICATION OPPOSABLE -- le pilote a couru, rien ici n'est provisoire :
      q_L  = 0.22961693269696845    [transmis_a_M12, ed0e27b1 ; 1 perte sur
                                     12 lignes, Clopper-Pearson 80 %,
                                     reconcilie par machine 2 au dernier
                                     chiffre]
      s_pt = 0.4572147008
      P(Bin(12, s_pt) >= 4) = 0.876124 < 0.90
      P(Bin(13, s_pt) >= 4) = 0.915439 >= 0.90
      N    = 13                     [MINIMAL, par l'encadrement ci-dessus]
LA TABLE INDICATIVE DE v3 EST RETIREE : son intrant est mesure et
l'application ci-dessus la remplace ; ses deux premieres lignes etaient de
toute facon inatteignables a douze lignes de pilote (delta 44.7b).
LA CLAUSE D'ARRET DE v3 (N > 12) S'EST EXECUTEE et ne se rearme pas : N est
desormais un nombre DERIVE d'un intrant opposable qu'aucune garde ne peut
modifier. La capacite de la liste (16) couvre N = 13 ; si une conception
future exigeait N > 16, elle l'ecrirait dans son propre gel.

PORTES
------
P-M12a  LA CLASSE TIENT-ELLE PONCTUELLEMENT ?  [PORTE PRINCIPALE]
  m = nombre de points OU LES TROIS DEGRES SONT PRESENTS et ou aucune garde
      n'a declenche. m est une quantite de plan qu'une garde peut modifier :
      les branches sont donc ecrites en m, jamais en nombres.
  SI m < 3 : NON CONCLUANT PAR CONSTRUCTION. Ecrit avant la mesure.
      [derivation : avec un ou deux points, une violation systematique ne se
       distingue pas d'une violation locale ; P-M12b serait indecidable et la
       manche ne rendrait qu'un fait isole.]
  CLASSE TENUE      : |E| <= 0.03 aux m points.
      [derivation : la classe predit E = 0 exactement. 0.03 vaut 458 fois
       sigma_E_max au PIRE point de la liste et ~1700 au meilleur (derivation
       (c)) : tout ce qui passe cette barre est compatible avec la classe a la
       precision ou nous savons mesurer, et la marge annoncee est celle du
       pire point, pas du meilleur.]
  CLASSE REFUTEE    : |E| >= 0.10 sur au moins ceil(m/2) points.
      [derivation de CETTE branche : E = 0 est une identite, pas une tendance ;
       une violation a 0.10 en unites de ln s* est un facteur 1.105 sur s*_4 a
       s*_5 et s*_7 donnes, tres au-dessus de tout effet de bracket (1527 fois
       sigma_E_max au pire point). Exiger la moitie des points empeche qu'un
       point unique, eventuellement pathologique et non detecte par les
       gardes, emporte le verdict.]
  SINON : NON CONCLUANT.
  LES SEUILS 0.03 ET 0.10 SONT DECLARES ARBITRAIRES ET FIXES AVANT MESURE.
  Deux ancrages, tous deux ecrits ici : sigma_E en forme derivee, lue au pire
  point de la liste -- 0.03 = 458 x, 0.10 = 1527 x (derivation (c)) ; et le
  seul ecart deja au registre, |E(2.85) - E(1.35)| = 0.3466 (S41.4, r(4)
  mesure 7.2252 contre 10.2185 predit), soit 3.5 fois le seuil de refutation.
  RESERVE OBLIGATOIRE SUR CE SECOND ANCRAGE : il compare une mesure M11 a une
  prediction batie sur M10, donc deux resolutions differentes -- c'est
  exactement E27, et cette comparaison n'est PAS opposable. Elle est citee ici
  comme ordre de grandeur ayant servi a fixer un seuil, jamais comme resultat.
  C'est aussi la raison structurelle pour laquelle M12 remesure les TROIS
  degres elle-meme, aux MEMES points, sous la MEME geometrie.

P-M12b  LA VIOLATION EST-ELLE SYSTEMATIQUE ?  [PORTE SECONDAIRE, conditionnelle]
  Ne se lit QUE si P-M12a rend REFUTEE. Sinon elle ne se lit pas, et le fait
  qu'elle ne se lise pas est consigne.
  Tous les E de module >= 0.10 de MEME SIGNE -> VIOLATION SYSTEMATIQUE.
      [derivation : E est lineaire en la deviation a l'affinite en u_p. Une
       erreur de FORME -- l'exposant u_p n'est pas 1/(p-2), ou le terme affine
       est incomplet -- produit une deviation de signe constant en w2.]
  Signes mixtes -> VIOLATION DISPERSEE.
      [derivation : une structure LOCALE (canyon, voisinage resonant) change de
       signe selon la position relative au creux ; M5 a etabli l'asymetrie du
       canyon, donc le changement de signe est attendu dans ce cas.]

P-M12c  CONSIGNATION, AUCUNE PORTE -- A(w2) et B(w2)
  Reconstruits en chaque point a partir de chacune des trois paires de degres
  (4,5), (4,7), (5,7). Sous la classe, les trois reconstructions coincident ;
  leur ecart est une autre facon de lire E, et elle est consignee SANS lecture
  gelee. Materiau pour la derivation d'un mecanisme, qui n'existe pas encore.

P-M12d  CONSIGNATION, AUCUNE PORTE -- STRUCTURE DE E EN w2
  Lecture PRE-DECLAREE, avec sa quatrieme branche (lecon S41.5) :
   (i)   |E| croit avec la proximite relative d/r a une resonance d'ordre <= 12
         -> deviation RESONANTE ;
   (ii)  |E| varie de facon lisse en w2 sans lien a d/r
         -> deviation DE FORME ;
   (iii) |E| sans structure visible dans l'un ni l'autre
         -> NON DEPARTAGE ;
   (iv)  AUCUNE DES TROIS ne s'applique -> le motif est consigne tel quel, et
         RIEN n'est choisi apres coup. Interdiction explicite de designer
         retrospectivement laquelle des trois il "appuierait".
  Aucune de ces branches n'engage de porte, ni ne modifie P-M12a.

P-M12e  CONSIGNATION -- ASYMETRIE DE SIGNE
  r_s = s*(+1)/s*(-1) et le cote fragile, a p=5 et p=7, en chaque point.
  A p=4, r_s = 1 PAR DEMONSTRATION (M11, negation exacte en IEEE, exposant
  impair a p pair, verifiee au bit sur seize lignes ; REPRODUITE au bit par
  le pilote sur une autre geometrie) et non par mesure : un seul signe est
  calcule, et G8a/G8b le controlent en regression.

GARDES
------
  G1' CUSTODY (bloquante, cout 1 recherche) : le script rejoue UNE ligne du
      pilote et exige |s*_M12 - s*_pilote| == 0 EXACTEMENT. LIGNE NOMMEE
      (correction S5a) : (w2 = 1.70, p = 7, sgn = +1).
      [motifs : 1.70 est le premier point de la liste du pilote ; p = 7 y
       porte le plus petit s* des douze lignes -- 0.4728872773 au signe +1,
       MESURE, desormais au registre (ed0e27b1) -- donc la resolution
       RELATIVE la plus exigeante ; le signe +1 est fixe d'avance pour ne
       dependre d'AUCUNE donnee. Memes fenetres, memes pas, meme moteur : le
       calcul est deterministe, donc l'egalite est au bit.]
      [complement v4 : le signe +1 de cette ligne est RECEVABLE et NON exclu
       par G6 -- l'exclusion du pilote porte le signe -1. La chaine de
       custody est intacte ; et la calibration 24/24 au bit du pilote etablit
       que l'exigence "== 0 exactement" est realiste, pas seulement severe.]
      [motif de la garde : les points de M12 sont NEUFS, donc il n'existe
       aucune ancre certifiee a leurs valeurs. La chaine de confiance passe
       par le pilote, calibre AU BIT sur M10 et M11 par sa garde G1.]
  G2  INVARIANCE EN g (regression) : K = g s*^(p-2) mesure a 2g sur le premier
      point de la liste (2.22), aux trois degres, tolerance 10 %. Echec ->
      ligne EXCLUE et consignee.
  G3  IDENTITE DE FORCE : erreur backward <= 1e-12 apres CHAQUE rebinding.
  G4  PAS DE TEMPS : dt/2 sur la ligne maximisant g . s*^(p-1) -- l'echelle de
      force, jamais le plus grand s* (lecon M6). Ecart <= 2 % sinon ligne NON
      FIABLE et exclue. [Cette semantique -- exclusion, donc effet sur m --
      est celle de CE gel ; le pilote transmettait G4 comme fait separe, hors
      q_L, et c'etait le sien (cert. script v1, S3).]
  G5  QUALITE DE BRACKET : pas final <= 1e-5, consigne par recherche ; toute
      recherche au-dessus est EXCLUE.
  G6  PRIMAUTE DE s* : aucune explosion sous 0.98 s*. CONSIGNATION OBLIGATOIRE
      SUR CHAQUE LIGNE, exclue ou non : nombre d'ilots, position de la premiere
      retombee, et min(s explosif)/s*. C'est le defaut S42.3, corrige.
      DOMAINE DECLARE (correction S5b) : ilots et retombees sont comptes dans
      [s*, 1.05 s*]. Ils ne se comparent PAS aux comptes de M10/M11, obtenus
      dans [s*, 1.30 s*] -- meme statut que les taux d'attrition.
      TEMOINS DU BORD (corrections S4/S6 du script pilote, REPRIS ICI) : les
      champs indice_du_seuil_098, explosif_a_l_indice_40, ecart ABSOLU et
      PREDICAT indice_40_compte_comme_sous_seuil -- le temoin calcule
      l'expression de la garde, operation pour operation.
  G7  REPERCUSSION : un point perdu a UN degre est perdu pour E, donc retire
      des trois. Sans exception, et c'est ce qui rend m plus petit que N.
  G8a/G8b PARITE a p=4, en regression sur les points mesures : sP - sM == 0
      exactement. Echec -> la lignee de code a change, ARRET.
  G9  COUVERTURE (correction S4) : le --selftest extrait de ce bloc la liste
      des consignations nommees et verifie, pour chacune et sur chaque ligne
      concernee, que le CHAMP EXISTE au JSON. Une valeur null n'est admise que
      si un champ jumeau <nom>_motif, NON VIDE, consigne sur la meme ligne le
      fait mesure qui la justifie (exemple attendu : "aucune retombee dans la
      fenetre"). Champ absent, ou null sans motif -> ECHEC BLOQUANT avant le
      run. Un null nu est un defaut de consignation ; un null motive est une
      donnee.
      [motif, S42.3 : le --selftest et la certification croisee verifient tous
       deux que le script fait ce qu'IL dit, jamais qu'il fait tout ce que LE
       GEL dit. Il manquait un controle de couverture ; le voici, et il ne
       confond plus un fait mesure avec un champ manquant.]
  E27, CORRECTIF STRUCTUREL, APPLICABLE A TOUTES LES GARDES : chaque
  consignation de garde porte au JSON, A COTE D'ELLE, la resolution a laquelle
  elle a ete obtenue -- bornes des deux balayages, n obtenus, pas relatifs
  effectifs, et sigma_E / sigma_E_max du point (derivation (c)). La resolution
  voyage DANS la donnee. Aucune clause en prose : les deux machines en avaient
  ecrit une et l'ont enfreinte.

GEOMETRIE DE BALAYAGE (alignee sur le code certifie de la lignee -- cert. v2,
corrections S7 et S8 ; VALIDEE PAR LE RUN DU PILOTE)
-----------------------------------------------------------------------------
  Le bracket mesure s* D'ABORD (pas final <= 1e-5, G5) ; le double balayage
  est un DIAGNOSTIC posterieur, bati sur le s* mesure. s* est donc connu des
  la recherche : AUCUNE circularite (mention reprise du gel M11 v4). Une
  seule echelle, une seule notation : s*, celle des comptages de G6 et C-P3.
  LES PAS SONT GELES EN PLAFOND, n EST UNE SORTIE, L'ARRONDI EST NOMME --
  aligne sur balayer() (m11_exposant_v3.py, 80cfa795 ; reprise VERBATIM
  certifiee au byte dans m12_pilote_v3.py, 663b17e2) :
    grossier : [LO0, 0.90 s*], LO0 = 0.05 ;
               n_g = 1 + ceil( (0.90 - LO0/s*) / 0.005 )     ARRONDI : CEIL
               pas effectif <= 0.005 s* (PLAFOND) ; n_g <= 181 ; garde de
               domaine STRICTE s* > LO0/0.90 = 1/18, ceinture n_g >= 2.
    fin      : [0.90 s*, 1.05 s*] ;
               n_f = 1 + round( (1.05 - 0.90) / 0.002 ) = 76 ARRONDI : ROUND
               quotient exact 75 ; IEEE 75.000000000000014 ; l'arrondi est
               NOMME (regle 13) parce que ceil divergerait (77).
    pas relatif EFFECTIF consigne par ligne : pas / s*.
  CONTROLES DE COHERENCE QUI MORDENT (vecteurs 0.47 -> n_g = 160,
  2.05 -> n_g = 177, fenetre fine -> n_f = 76 ; portees declarees : n_g pince
  CEIL, n_f exclut CEIL et ne separe pas round de floor). Le --selftest du
  script pilote les porte deja ; celui de M12 les REPREND par import.
  IDENTIQUE aux trois degres et identique au pilote : la geometrie est
  IMPORTEE de m12_pilote_v3.py (663b17e2), sans duplication de code. C'est la
  condition d'opposabilite des comparaisons INTERNES a M12 -- les seules que
  M12 fasse -- et c'est desormais aussi la condition de G1' (rejeu au bit).

PROGRAMME FIGE
--------------
  p=4 : N points x 1 signe  = 13     [parite acquise au bit, M11 + pilote]
  p=5 : N points x 2 signes = 26
  p=7 : N points x 2 signes = 26
  G1' : 1 ; G2 : 3 x 2 = 6 ; G4 : 1 ; G8 (regression p=4) : 2
  TOTAL = 5N + 10 = 75 recherches (N = 13).
  INVARIANT DE COMPTAGE, forme derivee :
      recherches_comptees + recherches_sautees == 75
  Ecrit sous cette forme parce que les gardes ont le DROIT de retrancher : une
  egalite sur le seul compte des recherches effectuees serait fausse des le
  premier declenchement de G6.
  COUT TOTAL DE LA MANCHE, pilote inclus : 75 + 25 = 100 recherches, dont 25
  deja executees et opposables (ed0e27b1).

MES ATTENTES (ecrites une fois ; elles ne seront pas reecrites)
---------------------------------------------------------------
  J'attends une REFUTATION. Motif honnete et declare : l'ecart deja au registre
  (0.3466 en unites de ln, sous reserve E27) est 3.5 fois mon seuil de
  refutation, et je n'ai aucune raison de croire qu'il soit entierement un
  artefact de resolution.
  Je prevois donc : P-M12a REFUTEE, et P-M12b SYSTEMATIQUE avec E du meme
  signe partout. Je prevois |E| entre 0.15 et 0.45 sur la majorite des points.
  Je prevois A(w2) et B(w2) reguliers, sans saut, sur l'intervalle couvert.
  JE N'AI AUCUNE ATTENTE sur P-M12d -- resonant contre forme est la vraie
  inconnue de la manche, et c'est aussi la seule lecture qui orienterait un
  mecanisme.
  CE QUI ME COUTERAIT : |E| <= 0.03 partout. La classe tiendrait, mon pari
  serait faux, et le programme reviendrait a mesurer beta -- avec, cette fois,
  une raison de croire que beta existe.

LIMITATIONS DECLAREES
---------------------
  - COUVERTURE. Les points accessibles vivent dans [1.73, 2.82] et le
    programme reel a N = 13 couvre [1.73, 2.80] -- les trois fenetres de
    gauche y entrent (1.73, 1.76, 1.84, 1.86). AUCUN point sous 1.73 n'est
    R-2'-propre : les voisinages de 3:2 (rayon 0.12), 4:3 (0.03) et 5:4
    (0.0075) recouvrent la gauche de l'intervalle. Consequence ecrite d'avance :
    une refutation etablie ici NE SE TRANSPORTE PAS au bord gauche, ou vit la
    chaine classique fermee. C'est une limitation de la manche, pas une reserve
    a invoquer apres coup selon le resultat.
  - ATTRITION ATTENDUE, consequence du pilote : s_pt = 0.457 par point ; a
    N = 13, l'esperance de m est ~5.9 et P(m >= 4) >= 0.915. Le pilote a
    montre la perte au plus petit s* de ses lignes ; les rangs de gauche
    (1.73-1.86) sont les plus exposes, et c'est ecrit AVANT la mesure.
  - Une manche ulterieure pourra sampler DELIBEREMENT a l'interieur des rayons,
    puisque la validite ne l'interdit pas (derivation (d)) -- au prix d'une
    attrition plus forte. Cela s'ecrira dans son propre gel, pas ici.
  - M12 MESURE, ELLE NE DERIVE PAS. Une refutation ne designe pas la classe de
    remplacement : elle etablit que la famille affine en u_p, avec A et B
    libres, est fausse. C'est tout, et c'est dit avant.
  - p=3 et p=6 ne sont pas mesures. p=3 n'est pas protocole-defini (E22, s* sur
    un ensemble d'explosion crible) ; p=6 releve de l'hypothese post-hoc du
    S41.6, qui se pre-declarera ailleurs.
  - ANTI-FRANKEN : aucune valeur de s* de M10, M11 ou du pilote n'entre dans la
    formation d'un E. Les seuls E de cette campagne sont formes de trois
    mesures faites au meme point, sous la meme geometrie, dans le meme run.
  - La combinaison E est INVARIANTE par changement d'unite de s* uniquement si
    ce changement est commun aux trois degres, car 1 - 2.25 + 1.25 = 0. Ce fait
    est verifie ici et il protege contre une classe d'erreurs de normalisation,
    PAS contre une difference de resolution entre degres -- d'ou la geometrie
    unique imposee plus haut.

IMPLEMENTATION
--------------
  m12_ponctuel_v1.py, moteur classique repris de m9_replication_v1.py
  (c8ed357b), geometrie de balayage et utilitaires exacts (neuf_exact,
  appartenance rule-11) IMPORTES du script pilote CERTIFIE m12_pilote_v3.py
  (663b17e2), sans duplication de code. Ecrit uniquement
  out/m12_results.json (incremental, une ecriture apres chaque ligne). Gel
  jumeau dans le docstring, du marqueur "PRE-ENREGISTREMENT M12" au
  terminateur inclus, sha256 recalcule au demarrage depuis le fichier source,
  convention d'empreinte B (bloc = fichier, saut de ligne final inclus).
  LE --SELFTEST DOIT MORDRE (cert. v3) ; il verifie au minimum :
    (i)   test NEGATIF du filtre de nouveaute : un candidat a 0.03 EXACT d'un
          point de grille, presente au filtre, doit etre RETENU (lecture A) ;
          un candidat a 0.02 doit etre EXCLU ; le test doit ECHOUER sous une
          comparaison flottante (2.27 suffit) ;
    (ii)  les trois vecteurs de la geometrie, portees declarees ;
    (iii) toute extraction dans ce bloc est ancree sur la STRUCTURE (regle
          12) et testee contre le leurre REEL : la sous-chaine "MES ATTENTES"
          y figure hors en-tete de section ;
    (iv)  la liste des SEIZE et l'appartenance rule-11 a 1e-9 ; le programme
          porte sur les 13 premiers, verifie par compte derive.
  PRE-VOL A MOTEUR FACTICE OBLIGATOIRE, joue par la machine qui detient les
  sources (lecon du pilote, cert. script v1) : il verifie ce que le script
  FAIT, la ou le --selftest verifie ce qu'il CALCULE. Les deux ne se
  remplacent pas.
  DEPOT DU SCRIPT CONDITIONNE a la certification croisee de ce bloc (E19-1).

=== FIN DU GEL M12 ===
