"""PRE-ENREGISTREMENT M12 -- TEST PONCTUEL DE LA CLASSE, SANS AUCUN AJUSTEMENT
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
"""
# =====================================================================
# m12_ponctuel_v1.py -- LE TEST PONCTUEL : 75 recherches, premiere
# lecture de E de toute la campagne.
# ---------------------------------------------------------------------
# Le gel jumeau (docstring ci-dessus) est le bloc CERTIFIE
# m12_pre_enregistrement_v4.md ; empreinte recalculee au demarrage
# (convention B) et confrontee a SHA_GEL.
# TOUT L'OUTILLAGE est IMPORTE du script pilote CERTIFIE
# m12_pilote_v3.py, charge par empreinte et dont le gel jumeau propre est
# re-verifie a l'import (custody transitive) : moteur (charger_moteur ->
# m9), rebind + G3, mesurer, balayer (verbatim lignee), enrichir_g6
# (temoins S4/S6), g8b, garde de domaine, neuf_exact / neuf_flottant,
# sauver, comptage exhaustif (P.CPT).
# Obligations tenues (cert. gel v4 f10ffcf3, note ad8dd209, delta 45 v3) :
#   1. PAIRE G8 pre-declaree : RANGS 1 ET 13 (2.22, 1.86), motif de
#      POSITION -- premier et dernier du programme, la paire la plus
#      ecartee en rang que la liste permette.
#   2. G2 ENUMERE : six recherches NEUVES a 2g, trois degres x deux
#      signes, au rang 1 (2.22) ; le compte 6 est DERIVE de l'enumeration
#      G2_RECHERCHES, jamais affirme.
#   3. G8b EST UN SEUL CONTROLE : sa moitie grossiere est ATTENDUE VIDE a
#      p=4 (pre-declare avant mesure) ; si elle mord, FAIT NEUF consigne.
#   4. G1' CUSTODY au bit contre le JSON pilote (empreinte complete) ;
#      temoins du bord en expression de garde ; G9 couverture avec null
#      motive ; selftest qui mord (leurre reel du bloc) ; le pre-vol
#      OPPOSABLE est celui de la machine qui detient les sources --
#      execute ailleurs, c'est une REPETITION.
# HISTORIQUE DU SCRIPT :
#   v1 ddfa8381... NON CERTIFIE (cert. script ponctuel v1, 29da21e4...) -> S1
#      le moteur factice TUE deux lignes par deux mecanismes (G5 en
#      5|2.78|-1, G6 en 7|2.42|+1, rangs 12 et 11) -- un banc d'essai se
#      concoit contre ce qui VA arriver (esperance : 7.1 points perdus
#      sur 13), pas contre ce qu'on espere ; S2 declaration : G2 exclut
#      aussi sur NON EVALUABLE ; S3 declaration : sigma_E vit dans la
#      section E, renvoi depuis chaque enregistrement G6.
# ANTI-FRANKEN : aucune valeur de M10, M11 ou du pilote n'entre dans un
# E ; la seule lecture du JSON pilote est la cible de G1'.
# =====================================================================

import argparse, hashlib, importlib.util, json, math, os, sys
from fractions import Fraction

import numpy as np

MARQ_DEBUT = "PRE-" + "ENREGISTREMENT M12"
MARQ_FIN = "=== FIN DU GEL M12 " + "==="

# ---- empreintes gelees (COMPLETES -- lecon S5) -----------------------
SHA_GEL = "bf9866a763c559d368c0ed23c73697bd1b6fde46a59b08a359c81918b6de9e9b"
SHA_PILOTE = "663b17e2955c79c09f1b6c0fb4443cd0c1f98be0db03ef089f5df682018ce905"
SHA_PILOTE_JSON = "ed0e27b1b6067096f7f9ed3ab95b8a4f3f6362577feea16301fa7534b95ad117"

# ---- protocole (gel v4) ----------------------------------------------
LISTE16 = [2.22, 2.67, 2.38, 2.80, 1.84, 2.55, 1.73, 1.76,
           2.27, 2.72, 2.42, 2.78, 1.86, 2.57, 1.74, 1.77]
N = 13
POINTS = LISTE16[:N]
DEGRES = (7, 5, 4)
G8_PAIRE = (LISTE16[0], LISTE16[12])        # rangs 1 et 13 -- delta 45 v3
G2_POINT = LISTE16[0]                       # rang 1, ancre de G2
G1P_LIGNE = (1.70, 7, +1)                   # gel v4, G1' -- ligne du PILOTE
# ---- plan de pertes du PRE-VOL (cert. script v1, S1) -----------------
# Regle mecanique, declaree : les deux derniers rangs du programme HORS
# paire G8 -- rangs 12 et 11 (2.78, 2.42). Jamais la ligne de G1' ni la
# paire G8, dont l'echec provoquerait un ARRET tronquant le pre-vol.
PREVOL_TUE_G5 = (5, LISTE16[11], -1)   # note au-dessus du plafond -> G5
PREVOL_TUE_G6 = (7, LISTE16[10], +1)   # explosion sous 0.98 s*    -> G6
TOL_APPART = 1e-09
TOL_G2, TOL_G4 = 0.10, 0.02
EPS_PORTE = 1e-12
SEUIL_TENUE, SEUIL_REFUT = 0.03, 0.10
U = {4: 0.5, 5: 1.0 / 3.0, 7: 0.2}          # u_p = 1/(p-2)
C_SIGMA = {4: 1.0, 5: 2.25, 7: 1.25}        # derivation (c)

# ---- G2 ENUMERE (obligation 2) : six recherches NEUVES a 2g ----------
G2_RECHERCHES = [(p, G2_POINT, sgn) for p in DEGRES for sgn in (+1, -1)]

# ---- programme fige, forme derivee -----------------------------------
RECH_ATTENDUES = (N                          # p=4, signe +1
                  + 2 * N * 2                # p=5 et p=7, deux signes
                  + len(G8_PAIRE)            # regression G8, sgn -1
                  + len(G2_RECHERCHES)       # G2, enumere
                  + 1                        # G1'
                  + 1)                       # G4
assert RECH_ATTENDUES == 75, "programme fige : 5N + 10 = 75 (gel v4)"
BAL_ATTENDUS = 2 * N * 2 + (2 * len(G8_PAIRE) + (N - len(G8_PAIRE)))
assert BAL_ATTENDUS == 67
LIGNES = [(p, w) for p in DEGRES for w in POINTS]
assert len(LIGNES) == 39
FOUT = os.path.join("out", "m12_results.json")
FOUT_PREVOL = os.path.join("out", "m12_PREVOL.json")


# =====================================================================
# 1. GEL JUMEAU (convention B) et CHARGEMENT DU PILOTE (custody
#    transitive : empreinte du fichier + re-verification de SON gel)
# =====================================================================

def _sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


def certifier_gel(verbeux=True):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    if src.count(MARQ_FIN) != 1:
        sys.exit("ARRET invariant de cloture : terminateur x%d" % src.count(MARQ_FIN))
    doc = __doc__
    i = doc.index(MARQ_FIN)
    if doc[i - 1] != "\n" or doc[i + len(MARQ_FIN):].strip():
        sys.exit("ARRET invariant de cloture du gel jumeau")
    bloc = src[src.index(MARQ_DEBUT): src.index(MARQ_FIN) + len(MARQ_FIN) + 1]
    h = hashlib.sha256(bloc.encode()).hexdigest()
    if verbeux:
        print("Gel jumeau M12 v4 : sha %s -> %s"
              % (h[:16] + "...", "CONCORDANT" if h == SHA_GEL else "DISCORDANT"))
    if h != SHA_GEL:
        sys.exit("ARRET E19 : le gel jumeau ne correspond pas a la version certifiee.")
    return bloc, h


def charger_pilote(chemin="m12_pilote_v3.py", verbeux=True):
    h = _sha(chemin)
    if verbeux:
        print("Script pilote %s -> %s" % (h[:24] + "...",
              "CONCORDANT" if h == SHA_PILOTE else "DISCORDANT"))
    if h != SHA_PILOTE:
        sys.exit("ARRET : le script pilote n'est pas celui que le gel designe.")
    spec = importlib.util.spec_from_file_location("m12_pilote", chemin)
    P = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(P)
    P.certifier_gel(verbeux=False)      # custody transitive : gel pilote 03e29c86
    if verbeux:
        print("  gel jumeau du pilote re-verifie (03e29c86...) : CONCORDANT")
    for k in ("recherches", "balayages", "sautees", "balayages_sautes"):
        P.CPT[k] = 0
    global P_PAS_FINAL
    P_PAS_FINAL = P.pas_final
    return P


def charger_cible_g1p(prevol, rep_prevol, P):
    """Cible de G1' : s*(1.70, 7, +1) du JSON pilote, empreinte COMPLETE
    exigee en REEL ; en PREVOL, source reelle si conforme, sinon
    synthetique avec banniere (repetition)."""
    chemin = os.path.join("out", "m12_pilote_results.json")
    meta = {}

    def lire(pth):
        j = json.load(open(pth, encoding="utf-8"))
        return float(j["resultats"]["carte"][P.cle(7, 1.70)]["sP"]["s"])

    if os.path.exists(chemin) and _sha(chemin) == SHA_PILOTE_JSON:
        meta.update({"statut": "REELLE", "sha256": SHA_PILOTE_JSON})
        return lire(chemin), meta
    if not prevol:
        sys.exit("ARRET : %s absent ou d'empreinte non conforme (exigee %s)"
                 % (chemin, SHA_PILOTE_JSON))
    p = os.path.join(rep_prevol, "m12_pilote_results.json")
    if not os.path.exists(p):
        sys.exit("ARRET PREVOL : ni JSON pilote reel conforme, ni synthetique dans %s"
                 % rep_prevol)
    print("=" * 70)
    print("PREVOL : cible G1' SYNTHETIQUE (%s) -- empreinte HORS REGISTRE." % p)
    print("Le pre-vol OPPOSABLE est celui de la machine qui detient les")
    print("sources certifiees ; ceci est une REPETITION (cert. script, S1).")
    print("=" * 70)
    meta.update({"statut": "SYNTHETIQUE_PREVOL", "sha256": _sha(p)})
    return lire(p), meta


def fabriquer_factice(val_g1p):
    """Moteur factice du pre-vol : valeurs SYNTHETIQUES lisses, AUCUNE
    prediction de classe embarquee ; K-invariance exacte pour exercer le
    chemin PASSE de G2 ; p=4 identique aux deux signes (G8a/b) ; masques
    grossiers tout-False (l'attente pre-declaree, obligation 3). ET IL
    TUE (cert. script v1, S1) : une recherche non recevable en
    PREVOL_TUE_G5, une explosion sous 0.98 s* en PREVOL_TUE_G6 -- deux
    points distincts, m reste >= 3, les branches de perte tournent."""
    base = {4: 2.0, 5: 0.8, 7: 0.5}
    module = {"m": None}

    def s_de(p, w, sgn):
        if (w, p, sgn) == G1P_LIGNE:
            return val_g1p
        v = base[p] * (0.6 + w / 2.0)
        return v if (p == 4 or sgn > 0) else v * 1.1

    def chercher(w2, sgn=1, dt=None, g=None):
        m = module["m"]
        v = s_de(m.P, w2, sgn)
        if g is not None and g > 0.075:            # branche 2g
            return v * 2.0 ** (-1.0 / (m.P - 2)), "OK|pas=6.03e-07"
        if (m.P, w2, sgn) == PREVOL_TUE_G5:
            return v, "OK|pas=2.00e-05"            # > plafond G5 : tue
        return v, "OK|pas=6.03e-07"

    def integrer(w2, s_arr, sgn=1, dt=None, g=None):
        m = module["m"]
        th = s_de(m.P, w2, sgn)
        if (m.P, w2, sgn) == PREVOL_TUE_G6:
            return np.asarray(s_arr, float) >= 0.5 * th   # explose sous seuil
        return np.asarray(s_arr, float) >= th
    return {"chercher": chercher, "integrer": integrer, "module": module}


# =====================================================================
# 2. ASSEMBLAGE D'UNE LIGNE M12 (convention (f) ; p=4 a un seul signe
#    hors paire G8 -- P-M12e : parite par demonstration, null motive)
# =====================================================================

MOTIF_P4 = ("P-M12e : r_s = 1 par demonstration (M11, reproduite au bit "
            "par le pilote) ; un seul signe au programme")


def assembler_ligne_m12(p, w, v):
    sP, sM = v["sP"], v.get("sM")
    if p == 4 and sM is None:
        v["sM"] = None
        v["sM_motif"] = MOTIF_P4
        if sP["recevable"]:
            v["sF"] = sP["s"]
        else:
            v["sF"] = None
            v["sF_motif"] = sP["motif_exclusion"] or "recherche non recevable"
        v["frag"] = None
        v["frag_motif"] = MOTIF_P4
        v["asym"] = None
        v["asym_motif"] = MOTIF_P4
        return
    if sP["recevable"] and sM["recevable"]:
        v["sF"] = min(sP["s"], sM["s"])
        v["frag"] = 1 if sP["s"] <= sM["s"] else -1
        v["asym"] = sP["s"] / sM["s"]
    else:
        motif = sP["motif_exclusion"] or sM["motif_exclusion"] or "non recevable"
        for ch in ("sF", "frag", "asym"):
            v[ch] = None
            v[ch + "_motif"] = motif


# =====================================================================
# 3. E, SIGMA, A/B, RESONANCES (derivations (a)-(c) executees)
# =====================================================================

def rayon(o):
    return (0.12 if o <= 6 else 0.03 if o <= 8 else
            0.0075 if o <= 10 else 0.001875)


RESONANCES = sorted({(k, l) for k in range(1, 13) for l in range(1, 13)
                     if k + l <= 12 and math.gcd(k, l) == 1
                     and l <= k <= 3 * l})


def matiere_p_m12d(w):
    """Consignation P-M12d : proximite relative d/r a la resonance la plus
    contraignante d'ordre <= 12. Distances en Fraction (regle elargie)."""
    wq = Fraction(round(w * 100), 100)
    best = None
    for k, l in RESONANCES:
        d = abs(wq - Fraction(k, l))
        r = Fraction(rayon(k + l)).limit_denominator(10 ** 7)
        dr = d / r
        if best is None or dr < best[0]:
            best = (dr, k, l, d, r)
    dr, k, l, d, r = best
    return {"fraction": "%d/%d" % (k, l), "ordre": k + l,
            "d": float(d), "rayon": float(r), "d_sur_r": float(dr)}


def former_E(v4, v5, v7):
    return math.log(v4) - 2.25 * math.log(v5) + 1.25 * math.log(v7)


P_PAS_FINAL = None    # lie a P.pas_final par main()/selftest apres import


def sigma_du_point(carte, w, cle):
    sig2, sigmax = 0.0, 0.0
    for p in DEGRES:
        v = carte[cle(p, w)]
        k = "sP" if (p == 4 or v["frag"] == 1) else "sM"
        pas = P_PAS_FINAL(v[k]["note"])
        t = C_SIGMA[p] * pas / v["sF"]
        sig2 += t * t
        sigmax += t
    return math.sqrt(sig2), sigmax


def reconstruire_AB(s4, s5, s7):
    out = {}
    for (pa, sa), (pb, sb) in ((( 4, s4), (5, s5)), ((4, s4), (7, s7)),
                               ((5, s5), (7, s7))):
        A = (math.log(sa) - math.log(sb)) / (U[pa] - U[pb])
        out["A_%d%d" % (pa, pb)] = A
        out["B_%d%d" % (pa, pb)] = math.log(sa) - A * U[pa]
    return out


def porte_a(E_vals):
    """P-M12a sur la liste des E des points survivants."""
    m = len(E_vals)
    if m < 3:
        return "NON CONCLUANT PAR CONSTRUCTION", "m = %d < 3" % m
    if all(abs(e) <= SEUIL_TENUE + EPS_PORTE for e in E_vals):
        return "CLASSE TENUE", "|E| <= 0.03 aux %d points" % m
    gros = [e for e in E_vals if abs(e) >= SEUIL_REFUT - EPS_PORTE]
    if len(gros) >= math.ceil(m / 2):
        return "CLASSE REFUTEE", "%d/%d points a |E| >= 0.10 (seuil %d)" % (
            len(gros), m, math.ceil(m / 2))
    return "NON CONCLUANT", "ni tenue ni refutee (m = %d)" % m


def porte_b(E_vals):
    gros = [e for e in E_vals if abs(e) >= SEUIL_REFUT - EPS_PORTE]
    signes = {1 if e > 0 else -1 for e in gros}
    return ("VIOLATION SYSTEMATIQUE" if len(signes) == 1
            else "VIOLATION DISPERSEE"), sorted(signes)


# =====================================================================
# 4. G9 -- COUVERTURE M12 (champ existant, null motive)
# =====================================================================

REQUIS_MESURE = ("s", "note", "recevable", "motif_exclusion", "duree_s")
REQUIS_CARTE = ("sP", "sM", "sF", "frag", "asym")
NULLABLES_CARTE = ("sM", "sF", "frag", "asym")
REQUIS_E = ("E", "sigma_E", "sigma_E_max", "AB", "resonance")
NULLABLES_E = REQUIS_E


def g9_verifier_m12(res):
    defauts = []
    for k, v in res["resultats"]["carte"].items():
        for ch in REQUIS_CARTE:
            if ch not in v:
                defauts.append("carte[%s] : champ absent %s" % (k, ch))
                continue
            if v[ch] is None:
                if ch not in NULLABLES_CARTE:
                    defauts.append("carte[%s] : %s null non admissible" % (k, ch))
                elif not v.get(ch + "_motif"):
                    defauts.append("carte[%s] : %s null SANS motif" % (k, ch))
        for sk in ("sP", "sM"):
            m = v.get(sk)
            if not isinstance(m, dict):
                continue
            for ch in REQUIS_MESURE:
                if ch not in m:
                    defauts.append("carte[%s].%s : champ absent %s" % (k, sk, ch))
            if m.get("s") is None and not m.get("motif_exclusion"):
                defauts.append("carte[%s].%s : s null SANS motif" % (k, sk))
    for k, b in res["resultats"]["G6"].items():
        for ch in ("n_gros", "n_fin", "exclue", "ilots", "ilots_au_dessus",
                   "premiere_retombee_en_s", "pas_final_recherche",
                   "ecart_absolu_indice_40_au_seuil",
                   "indice_40_compte_comme_sous_seuil"):
            if ch not in b:
                defauts.append("G6[%s] : champ absent %s" % (k, ch))
                continue
            if b[ch] is None and not b.get(ch + "_motif"):
                defauts.append("G6[%s] : %s null SANS motif" % (k, ch))
    for w, e in res["resultats"]["E"].items():
        for ch in REQUIS_E:
            if ch not in e:
                defauts.append("E[%s] : champ absent %s" % (w, ch))
                continue
            if e[ch] is None and not e.get(ch + "_motif"):
                defauts.append("E[%s] : %s null SANS motif" % (w, ch))
    return defauts


def _record_synthetique(P):
    """G9 avant-run : une ligne p=5, une ligne p=4 hors paire, un balayage,
    un E -- par LES MEMES constructeurs que le run."""
    from types import SimpleNamespace
    res = {"resultats": {"carte": {}, "G6": {}, "E": {}}}
    fake = {"s": 1.234, "note": "OK|pas=6.03e-07", "recevable": True,
            "motif_exclusion": "", "duree_s": 0.0}
    v5 = {"sP": dict(fake), "sM": dict(fake, s=1.334)}
    assembler_ligne_m12(5, 9.99, v5)
    res["resultats"]["carte"][P.cle(5, 9.99)] = v5
    v4 = {"sP": dict(fake)}
    assembler_ligne_m12(4, 9.99, v4)
    res["resultats"]["carte"][P.cle(4, 9.99)] = v4
    ns = SimpleNamespace(LO0=0.05,
                         integrer=lambda w2, s, sgn=1, dt=None, g=None:
                         np.asarray(s, float) >= 1.234)
    cpt0 = dict(P.CPT)
    bal = P.enrichir_g6(P.balayer(ns, 9.99, +1, 1.234), 1.234, fake["note"])
    P.CPT.update(cpt0)
    res["resultats"]["G6"][P.cle(5, 9.99) + "|+1"] = bal
    res["resultats"]["E"]["9.99"] = {"E": None, "E_motif": "synthetique",
                                     "sigma_E": None, "sigma_E_motif": "synthetique",
                                     "sigma_E_max": None, "sigma_E_max_motif": "synthetique",
                                     "AB": None, "AB_motif": "synthetique",
                                     "resonance": None, "resonance_motif": "synthetique"}
    return res


# =====================================================================
# 5. SELFTEST -- il mord, portees declarees
# =====================================================================

def selftest():
    from types import SimpleNamespace
    print("=" * 70)
    print("SELFTEST m12_ponctuel_v1.py")
    print("=" * 70)
    bloc, _ = certifier_gel()
    P = charger_pilote(verbeux=False)
    print("pilote importe par empreinte, gel pilote re-verifie")

    print("\n[1] programme fige, DERIVE d'enumerations (jamais affirme)")
    assert RECH_ATTENDUES == 75 and BAL_ATTENDUS == 67 and len(LIGNES) == 39
    assert len(G2_RECHERCHES) == 6 and all(w == G2_POINT for _, w, _ in G2_RECHERCHES)
    assert G8_PAIRE == (LISTE16[0], LISTE16[12]) == (2.22, 1.86)
    assert PREVOL_TUE_G5[1] != PREVOL_TUE_G6[1]
    for _, wtue, _ in (PREVOL_TUE_G5, PREVOL_TUE_G6):
        assert wtue not in G8_PAIRE and wtue != G1P_LIGNE[0]
    print("    75 recherches (13+52+2+6+1+1), 67 balayages, 39 lignes ;")
    print("    plan de pertes du pre-vol : hors G1' et paire G8, points distincts ;")
    print("    G2 : six recherches ENUMEREES (3 degres x 2 signes a 2g, rang 1) ;")
    print("    paire G8 = rangs 1 et 13 -- motif de POSITION (delta 45 v3)")

    print("\n[2] liste des seize, programme, espacements (entiers de centiemes)")
    cents = [round(w * 100) for w in LISTE16]
    assert POINTS == LISTE16[:13]
    e16 = min(abs(a - b) for i, a in enumerate(cents) for b in cents[i + 1:])
    e13 = min(abs(a - b) for i, a in enumerate(cents[:13]) for b in cents[i + 1:13])
    assert (e16, e13) == (1, 2)
    assert all(min(abs(w - x) for x in LISTE16) <= TOL_APPART for w in POINTS + [G2_POINT])
    print("    espacement 16 : 0.01 ; espacement des TREIZE mesures : 0.02 ;")
    print("    appartenance rule-11 a 1e-9 : PROGRAMME + ancre G2. G1' rejoue")
    print("    une ligne du PILOTE (1.70), hors liste PAR CONSTRUCTION -- exempte.")

    print("\n[3] coefficients de E : unicite EXACTE et identite symbolique")
    u4, u5, u7 = Fraction(1, 2), Fraction(1, 3), Fraction(1, 5)
    a = (u4 - u7) / (u5 - u7)
    b = 1 - a
    assert (a, b) == (Fraction(9, 4), Fraction(-5, 4))
    for A, B in ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)),
                 (Fraction(3, 7), Fraction(-11, 5))):
        E = (A * u4 + B) - Fraction(9, 4) * (A * u5 + B) + Fraction(5, 4) * (A * u7 + B)
        assert E == 0
    assert len({u4, u5, u7}) == 3
    print("    a = 9/4, b = -5/4, uniques ; E(A u_p + B) == 0 sur trois (A,B) ;")
    print("    rang 2 (u_p distincts deux a deux)")

    print("\n[4] sigma_E : formule au point d'ancrage de la certification")
    s = {4: 2.04, 5: 0.65, 7: 0.49}
    smax = sum(C_SIGMA[p] * 1e-5 / s[p] for p in DEGRES)
    assert abs(smax - 6.5e-5) < 0.1e-5
    print("    pire cas ~%.2e a (2.04, 0.65, 0.49), pas 1e-5 -- concorde" % smax)

    print("\n[5] portes P-M12a / P-M12b : unites de branche")
    assert porte_a([0.01, 0.02])[0].startswith("NON CONCLUANT PAR")
    assert porte_a([0.01, -0.02, 0.005, 0.0])[0] == "CLASSE TENUE"
    v, _ = porte_a([0.2, 0.15, 0.3, 0.01, 0.02])
    assert v == "CLASSE REFUTEE" and porte_b([0.2, 0.15, 0.3])[0] == "VIOLATION SYSTEMATIQUE"
    assert porte_b([0.2, -0.15, 0.3])[0] == "VIOLATION DISPERSEE"
    assert porte_a([0.2, 0.15, 0.01, 0.02, 0.03])[0] == "NON CONCLUANT"
    print("    m<3 ; TENUE ; REFUTEE (ceil(5/2)=3 atteint) + SYSTEMATIQUE ;")
    print("    DISPERSEE ; NON CONCLUANT (2 gros < 3) -- toutes branches mordues")

    print("\n[6] geometrie et domaine, via le module PILOTE importe")
    ns = SimpleNamespace(LO0=0.05,
                         integrer=lambda w2, s, sgn=1, dt=None, g=None:
                         np.zeros(np.asarray(s).shape, bool))
    cpt0 = dict(P.CPT)
    assert P.balayer(ns, 9.9, +1, 0.47)["n_gros"] == 160
    assert P.balayer(ns, 9.9, +1, 2.05)["n_gros"] == 177
    assert P.balayer(ns, 9.9, +1, 2.05)["n_fin"] == 76
    P.CPT.update(cpt0)
    assert not P.verifier_domaine(1.0 / 18.0)[0] and P.verifier_domaine(0.0556)[0]
    print("    vecteurs 160 / 177 / 76 (portees : n_g pince CEIL, n_f exclut")
    print("    CEIL sans separer round de floor) ; domaine strict s* > 1/18")

    print("\n[7] filtre de nouveaute : le test negatif MORD (import pilote)")
    assert P.neuf_exact(227) is True and P.neuf_flottant(227) is False
    assert P.neuf_exact(213) is False
    print("    2.27 : exact RETENU, flottant EXCLU ; 2.13 : EXCLU")

    print("\n[8] G9-M12 : couverture, et defauts DETECTES")
    r = _record_synthetique(P)
    assert g9_verifier_m12(r) == []
    r2 = _record_synthetique(P)
    del r2["resultats"]["carte"][P.cle(5, 9.99)]["sF"]
    r3 = _record_synthetique(P)
    r3["resultats"]["carte"][P.cle(5, 9.99)]["sM"] = None
    r3["resultats"]["carte"][P.cle(5, 9.99)].pop("sM_motif", None)
    r4 = _record_synthetique(P)
    del r4["resultats"]["E"]["9.99"]["resonance"]
    d2, d3, d4 = (g9_verifier_m12(x) for x in (r2, r3, r4))
    assert d2 and d3 and d4
    print("    conforme : 0 ; sF supprime : %d ; sM null nu (p=5) : %d ;"
          % (len(d2), len(d3)))
    print("    champ E supprime : %d -- et le p=4 hors paire (sM null +"
          % len(d4))
    print("    motif P-M12e) est CONFORME, verifie positivement")

    print("\n[9] G1' : l'exactitude au bit est testable")
    assert (0.4728872773 - 0.4728872773) == 0.0
    assert (0.4728872773 - 0.4728872774) != 0.0
    print("    egal -> 0.0 exact ; different -> detecte")

    print("\n[10] matiere P-M12d : resonance la plus contraignante")
    m = matiere_p_m12d(2.22)
    assert m["d_sur_r"] > 1.10 - 1e-12
    print("    2.22 -> %s (ordre %d), d/r = %.3f >= 1.10 (marge R-2')"
          % (m["fraction"], m["ordre"], m["d_sur_r"]))

    print("\nSELFTEST : TOUT PASSE (10 sections).")
    return 0


# =====================================================================
# 6. RUN
# =====================================================================

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--prevol", action="store_true")
    ap.add_argument("--pilote", default="m12_pilote_v3.py")
    ap.add_argument("--moteur", default="m9_replication_v1.py")
    ap.add_argument("--sources-prevol", default="prevol_sources")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())

    bloc, hgel = certifier_gel()
    mode = "PREVOL" if a.prevol else "REEL"
    fout = FOUT_PREVOL if a.prevol else FOUT
    assert (not a.prevol) or fout != FOUT, "le pre-vol n'ecrit JAMAIS le fichier reel"
    P = charger_pilote(a.pilote)
    val_g1p, meta_g1p = charger_cible_g1p(a.prevol, a.sources_prevol, P)
    factice = fabriquer_factice(val_g1p) if a.prevol else None
    m9 = P.charger_moteur(a.moteur, factice=factice)
    d = g9_verifier_m12(_record_synthetique(P))
    if d:
        sys.exit("ARRET G9 (avant le run) :\n  " + "\n  ".join(d))
    print("G9 avant-run : constructeurs de consignations COMPLETS.")
    for w in POINTS + [G2_POINT]:
        if min(abs(w - x) for x in LISTE16) > TOL_APPART:
            sys.exit("ARRET rule-11 : %r hors liste" % w)
    print("rule-11 : 13 points du programme + ancre G2 sur la liste, 1e-9 ;")
    print("  G1' rejoue une ligne du PILOTE (1.70) -- hors liste par construction.")

    res = {"meta": {"gel_sha256_bloc": hgel,
                    "pilote_sha256": SHA_PILOTE,
                    "pilote_json_sha256_attendu": SHA_PILOTE_JSON,
                    "cible_g1p": meta_g1p, "mode": mode,
                    "convention_empreinte": "B -- bloc saut final inclus = fichier",
                    "declarations": {
                        "G8_paire": "rangs 1 et 13 (2.22, 1.86) -- motif de "
                                    "POSITION, delta 45 v3, note ad8dd209",
                        "G2": "six recherches NEUVES a 2g, 3 degres x 2 "
                              "signes, rang 1 ; compte derive de l'enumeration",
                        "G8b": "UN SEUL controle : moitie grossiere ATTENDUE "
                               "VIDE a p=4 (pre-declare) ; si elle mord, "
                               "FAIT NEUF consigne",
                        "G2_non_evaluable": "AJOUT DECLARE a la regle gelee "
                               "(cert. script v1, S2) : le script exclut "
                               "AUSSI sur NON EVALUABLE, le gel n'ecrivant "
                               "que ECHEC ; direction conservatrice -- une "
                               "invariance non verifiee n'est pas une "
                               "invariance verifiee",
                        "sigma_E_emplacement": "sigma_E / sigma_E_max sont "
                               "des quantites de POINT (trois degres) : "
                               "elles vivent dans resultats.E, et chaque "
                               "enregistrement G6 porte un renvoi (S3)"},
                    "G3_par_degre": [], "gardes": [], "exclusions": {}},
           "resultats": {"carte": {}, "G6": {}, "G8": {}, "G2": {}, "G4": {},
                         "G1p": {}, "E": {}},
           "verdict": {}, "resume": {}}
    jg3 = res["meta"]["G3_par_degre"]
    if a.prevol:
        res["meta"]["prevol_plan_de_pertes"] = {
            "G5": "%d|%.2f|%+d" % PREVOL_TUE_G5,
            "G6": "%d|%.2f|%+d" % PREVOL_TUE_G6,
            "regle": "les deux derniers rangs du programme HORS paire G8 "
                     "(rangs 12 et 11) ; jamais G1' ni la paire G8 (S1)"}
    carte = res["resultats"]["carte"]
    excl = res["meta"]["exclusions"]

    def sauve():
        P.sauver(res, fout)

    def plan_signes(p, w):
        if p != 4:
            return [(+1, "sP"), (-1, "sM")]
        return [(+1, "sP")] + ([(-1, "sM")] if w in G8_PAIRE else [])

    # ---- G1' D'ABORD (bloquante, 1 recherche) -------------------------
    print("\n--- G1' custody : rejeu au bit de (1.70, p=7, +1) ---")
    P.rebind(m9, 7, jg3)
    r = P.mesurer(m9, 1.70, +1)
    ec = (r["s"] - val_g1p) if r["s"] is not None else None
    res["resultats"]["G1p"] = {"ligne": "7|1.70|+1", "mesure": r,
                               "cible": val_g1p, "ecart_absolu": ec,
                               "verdict": "PASSE" if ec == 0.0 else "ECHEC"}
    sauve()
    if ec != 0.0:
        sys.exit("ARRET G1' : ecart %r != 0 -- la chaine de custody est rompue." % ec)
    print("  ecart absolu = 0.0 EXACT : custody intacte.")

    for p in DEGRES:
        print("\n--- degre p = %d ---" % p)
        if p != 7:
            P.rebind(m9, p, jg3)
        for w in POINTS:
            v = carte.setdefault(P.cle(p, w), {})
            for sgn, k in plan_signes(p, w):
                m = P.mesurer(m9, w, sgn)
                if p == 4 and sgn < 0:
                    m["role"] = "regression_G8"
                v[k] = m
                sauve()
            assembler_ligne_m12(p, w, v)
            if v["sF"] is None:
                excl.setdefault(P.cle(p, w), []).append("G5 : " + v["sF_motif"])
            if p == 4 and w in G8_PAIRE and v["sP"]["recevable"] and v["sM"]["recevable"]:
                e8 = v["sP"]["s"] - v["sM"]["s"]
                res["resultats"]["G8"].setdefault(P.cle(p, w), {})["G8a"] = {
                    "ecart_absolu": e8, "verdict": "OK" if e8 == 0.0 else "ECHEC"}
                if e8 != 0.0:
                    sauve()
                    sys.exit("ARRET G8a : sP - sM = %r != 0 en w2=%.2f" % (e8, w))
            sauve()
        for w in POINTS:
            v = carte[P.cle(p, w)]
            plan = plan_signes(p, w)
            if not all(v[k]["recevable"] for _, k in plan):
                P.CPT["balayages_sautes"] += len(plan)
                res["meta"]["gardes"].append(
                    "G6 %s : %d balayage(s) SAUTE(S), ligne non recevable"
                    % (P.cle(p, w), len(plan)))
                sauve()
                continue
            bg = {}
            for sgn, k in plan:
                ok, motif = P.verifier_domaine(v[k]["s"])
                if not ok:
                    res["meta"]["gardes"].append("DOMAINE %s : %s" % (P.cle(p, w), motif))
                    sauve()
                    sys.exit("ARRET domaine : " + motif)
                bal = P.balayer(m9, w, sgn, v[k]["s"])
                P.enrichir_g6(bal, v[k]["s"], v[k]["note"])
                if p == 4:
                    bal["g8b_grossier_attendu"] = ("VIDE (pre-declare avant mesure, "
                                                   "note ad8dd209 / delta 45 v3)")
                    if bal["gros_explosifs"] > 0:
                        res["meta"]["gardes"].append(
                            "FAIT NEUF : moitie grossiere de G8b a MORDU a "
                            "p=4, w2=%.2f sgn=%+d (%d explosif(s))"
                            % (w, sgn, bal["gros_explosifs"]))
                bal["sigma_E_renvoi"] = ("quantite de POINT : voir "
                                         "resultats.E['%.2f'] (S3)" % w)
                bg[k] = bal
                res["resultats"]["G6"][P.cle(p, w) + "|%+d" % sgn] = bal
                if bal["exclue"]:
                    excl.setdefault(P.cle(p, w), []).append(
                        "G6 sgn=%+d explosion sous seuil" % sgn)
            if p == 4 and w in G8_PAIRE:
                g8 = P.g8b(bg["sP"], bg["sM"])
                res["resultats"]["G8"].setdefault(P.cle(p, w), {})["G8b"] = g8
                if (g8["grossier"]["deviations"] != 0 or g8["fin"]["deviations"] != 0
                        or not g8["ilots_identiques"] or not g8["retombee_identique"]):
                    sauve()
                    sys.exit("ARRET G8b : masques non identiques en w2=%.2f" % w)
            sauve()
        # ---- G2 a ce degre : les deux recherches enumerees a 2g -------
        for pp, w2g, sgn in [t for t in G2_RECHERCHES if t[0] == p]:
            k = "sP" if sgn > 0 else "sM"
            base = carte[P.cle(p, G2_POINT)].get(k)
            r2 = P.mesurer(m9, w2g, sgn, g=2 * m9.G_REF)
            if base and base["recevable"] and r2["recevable"]:
                ratio = 2.0 * (r2["s"] / base["s"]) ** (p - 2)
                v2 = "PASSE" if abs(ratio - 1.0) <= TOL_G2 + EPS_PORTE else "ECHEC"
            else:
                ratio, v2 = None, "NON EVALUABLE"
            res["resultats"]["G2"]["%d|%+d" % (p, sgn)] = {
                "w2": w2g, "g": "2g", "mesure": r2, "K2_sur_K1": ratio,
                "ratio_motif": (None if ratio is not None else
                                "base ou 2g non recevable"),
                "verdict": v2}
            if v2 != "PASSE":
                excl.setdefault(P.cle(p, G2_POINT), []).append(
                    "G2 sgn=%+d : %s" % (sgn, v2))
            sauve()
        print("  degre %d : recherches, balayages, G2 consignes" % p)

    # ---- G4 -----------------------------------------------------------
    print("\n--- G4 : dt/2 sur l'echelle de force maximale ---")
    best = None
    for p in DEGRES:
        for w in POINTS:
            v = carte[P.cle(p, w)]
            for sgn, k in plan_signes(p, w):
                if v[k]["recevable"]:
                    e = m9.G_REF * v[k]["s"] ** (p - 1)
                    if best is None or e > best[0]:
                        best = (e, p, w, sgn, v[k]["s"])
    if best is None:
        P.CPT["sautees"] += 1
        res["meta"]["gardes"].append("G4 : recherche SAUTEE (rien de recevable)")
    else:
        e, p, w, sgn, sref = best
        P.rebind(m9, p, jg3)
        r4 = P.mesurer(m9, w, sgn, dt=m9.DT / 2)
        ec4 = abs(r4["s"] / sref - 1.0) if r4["recevable"] else None
        ok4 = ec4 is not None and ec4 <= TOL_G4 + EPS_PORTE
        res["resultats"]["G4"] = {"p": p, "w2": w, "sgn": sgn, "s_dt": sref,
                                  "s_dt2": r4["s"], "duree_s": r4["duree_s"],
                                  "ecart": ec4,
                                  "ecart_motif": (None if ec4 is not None
                                                  else r4["motif_exclusion"]),
                                  "verdict": "PASSE" if ok4 else "NON FIABLE"}
        if not ok4:
            excl.setdefault(P.cle(p, w), []).append("G4 NON FIABLE")
        print("  G4 sur %d|%.2f|%+d : %s" % (p, w, sgn,
              res["resultats"]["G4"]["verdict"]))
    sauve()

    # ---- E, sigma, A/B, resonances, portes ----------------------------
    print("\n--- E aux points survivants, et portes ---")
    E_vals = []
    for w in POINTS:
        cles = [P.cle(p, w) for p in DEGRES]
        motifs = sum((excl.get(c, []) for c in cles), [])
        sfs = {p: carte[P.cle(p, w)]["sF"] for p in DEGRES}
        if motifs or any(sfs[p] is None for p in DEGRES):
            mot = " ; ".join(motifs) or "sF absent"
            res["resultats"]["E"]["%.2f" % w] = {
                "E": None, "E_motif": "point perdu (G7) : " + mot,
                "sigma_E": None, "sigma_E_motif": mot,
                "sigma_E_max": None, "sigma_E_max_motif": mot,
                "AB": None, "AB_motif": mot,
                "resonance": matiere_p_m12d(w)}
            continue
        E = former_E(sfs[4], sfs[5], sfs[7])
        sig, sigmax = sigma_du_point(carte, w, P.cle)
        res["resultats"]["E"]["%.2f" % w] = {
            "E": E, "sigma_E": sig, "sigma_E_max": sigmax,
            "AB": reconstruire_AB(sfs[4], sfs[5], sfs[7]),
            "resonance": matiere_p_m12d(w)}
        E_vals.append(E)
        sauve()
    m = len(E_vals)
    va, da = porte_a(E_vals)
    verdict = {"m": m, "P_M12a": va, "detail_a": da}
    if va == "CLASSE REFUTEE":
        vb, signes = porte_b(E_vals)
        verdict["P_M12b"] = vb
        verdict["signes_gros"] = signes
    else:
        verdict["P_M12b"] = "NON LUE (P-M12a != REFUTEE) -- consigne"
    if mode == "PREVOL":
        verdict = {("PREVOL_SYNTHETIQUE_" + k): v for k, v in verdict.items()}
        print("=" * 70)
        print("PREVOL : le 'verdict' ci-dessous est SYNTHETIQUE -- AUCUNE PHYSIQUE.")
        print("=" * 70)
    res["verdict"] = verdict

    # ---- resume -------------------------------------------------------
    pertes = {c: ms for c, ms in excl.items()}
    ventil = {g: sum(1 for ms in pertes.values()
                     if any(s.startswith(g) for s in ms))
              for g in ("G2", "G4", "G5", "G6")}
    durees = [carte[P.cle(p, w)][k]["duree_s"]
              for p in DEGRES for w in POINTS
              for sgn, k in plan_signes(p, w)]
    res["resume"] = {
        "m": m, "points_perdus": sorted(pertes),
        "pertes_par_mecanisme": ventil,
        "pertes_par_mecanisme_note": "ventilation par MECANISME, pas une "
            "partition (une ligne peut porter plusieurs motifs)",
        "attrition_39": {"lignes_perdues": len(pertes), "sur": len(LIGNES),
                         "statut": "FAIT consigne ; AUCUNE application D-N "
                                   "ici ; materiau de la regle exhaustive "
                                   "pre-declaree (delta 45, 45.4)"},
        "duree_par_recherche_s": {"n": len(durees),
                                  "total": float(sum(durees)),
                                  "moyenne": float(sum(durees) / len(durees))},
    }
    dtmod = __import__("datetime")
    res["meta"]["date_utc"] = dtmod.datetime.now(dtmod.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")
    res["meta"]["script_sha256"] = _sha(os.path.abspath(__file__))
    res["meta"]["recherches"] = {"comptees": P.CPT["recherches"],
                                 "sautees": P.CPT["sautees"],
                                 "attendues": RECH_ATTENDUES}
    res["meta"]["balayages"] = {"comptes": P.CPT["balayages"],
                                "sautes": P.CPT["balayages_sautes"],
                                "attendus": BAL_ATTENDUS}
    d = g9_verifier_m12(res)
    if d:
        sauve()
        sys.exit("ARRET G9 (apres run) : %d defaut(s) :\n  %s"
                 % (len(d), "\n  ".join(d)))
    sauve()
    if P.CPT["recherches"] + P.CPT["sautees"] != RECH_ATTENDUES:
        sys.exit("ARRET : %d + %d recherches != %d"
                 % (P.CPT["recherches"], P.CPT["sautees"], RECH_ATTENDUES))
    if P.CPT["balayages"] + P.CPT["balayages_sautes"] != BAL_ATTENDUS:
        sys.exit("ARRET : %d + %d balayages != %d"
                 % (P.CPT["balayages"], P.CPT["balayages_sautes"], BAL_ATTENDUS))
    print("\nEcrit : %s" % fout)
    print("Recherches : %d + %d = %d / %d | balayages : %d + %d = %d / %d"
          % (P.CPT["recherches"], P.CPT["sautees"],
             P.CPT["recherches"] + P.CPT["sautees"], RECH_ATTENDUES,
             P.CPT["balayages"], P.CPT["balayages_sautes"],
             P.CPT["balayages"] + P.CPT["balayages_sautes"], BAL_ATTENDUS))
    print("m = %d | %s" % (m, res["verdict"].get("P_M12a",
          res["verdict"].get("PREVOL_SYNTHETIQUE_P_M12a"))))
    print("sha256 du JSON : %s" % _sha(fout))


if __name__ == "__main__":
    main()
