PRE-ENREGISTREMENT M15 -- LE SITE 8/3 EN DOUBLE OBSERVABLE (P1-b, CLASSIQUE PUR)
(gele avant l'ecriture de toute ligne de code ; bloc ASCII, canonique NFC+LF ;
nom de fichier versionne, regle E19 -- version v3, machine 1, 2026-08-07)

HISTORIQUE DU GEL
  v1 a2bb2dcd : NON CERTIFIE par machine 2 (certification a944511d
  [canonique NFC+LF], log 61f2610f [BRUT -- fichier v1 en CRLF, son
  empreinte canonique differe : N-10], script d'audit 32714630
  [canonique NFC+LF] -- 3 bloquants, 5 declarations manquantes,
  0 echec mecanique ; numerotation propre a la certification v1).
  CORRECTIFS PORTES PAR LA v2 (numerotation v1) :
    D-1 : la barre d'instrument ne peut pas juger une structure -- seuil
      refondu en max(barre de paire, PLANCHER de rugosite derive du fond
      opposable), clause de centrage, et critere reconstruit puis soumis
      au test negatif sur archives a reponse connue (ITEM 7). Constat
      aggravant, verifie par machine 1 : la clause (2) v1, appliquee au
      canyon M14 reel (68df6576), rend D(g) = +0.1096 et D(d) = -0.0781
      (N-11 : inscriptions arrondies au plus proche, jamais
      tronquees), signes OPPOSES -- elle aurait manque le seul canyon mesure de la
      campagne (profil en falaise, pas en V). Le critere v2 est concu
      pour mordre les deux formes.
    D-2 : la consignation canal 4 par "signes opposes" nommait centre
      le profil monotone ; elle est REMPLACEE (le critere v2 est en
      residu a la corde, sans clause de signes de paire).
    D-3 : barre definie PAR PAIRE/CORDE en forme derivee ; convention
      N-3 de M14 (ordre de sommation, cloture au bit) RECONDUITE ;
      test execute des verrous de custody exige (forme math.nextafter).
    N-1 a N-5 : declarees dans le corps (pas de s*4 localise ; manche
      non aveugle et fait anterieur au site ; critere de nouveaute
      nomme ; etiquette parite corrigee ; q_L local et branche de
      lecture P-M15c pour les morts au site).
  v2 c92c58e5 : NON CERTIFIE par machine 2 (note de certification
  croisee v2 -- empreinte calculee a reception, brut = canonique
  [fichier LF seul] : 9088ce59 ; trace executable .py 26e7353f /
  .log dbbaee82, empreintes completes a consigner au registre, la
  note les livre tronquees a 16 hex) : 6 bloquants D-1..D-6
  (7 assertions), 7 declarations manquantes N-6..N-12, 1 echec de
  controle mecanique. NUMEROTATION DE LA CERTIFICATION v2, seule
  utilisee dans la suite du present gel.
  ACQUIS DE LA v2, conserves : le critere refondu MORD le seul
  canyon mesure de la campagne (68df6576 : x_M = 2.48, res_E =
  +0.2647, forme FALAISE, porte par les canaux 5/7) ; ITEM 2
  certifie ; ITEM 5 certifie pour moitie (recopie) ; ITEM 3 rendu
  (q_L local, cite au corps) ; les faits (a)-(f) se re-derivent
  tous.
  CORRECTIFS PORTES PAR LA v3 :
    D-1 : le PLANCHER v2 n'etait pas HOMOGENE a ce qu'il doit
      exclure -- un fond parfaitement lisse le franchissait dans la
      fenetre (temoin synthetique D-1a ET fond reel mesure D-1b de
      la certification). Refondu en COURBURE : K_X consigne
      pre-run, plancher derive PAR POINT INTERIEUR au run (forme
      derivee, regle 13). Banc rejoue par machine 2 sur le
      correctif : le canyon mord a 2.33x, les deux fonds lisses se
      taisent.
    D-2 : au plancher de comptes exact (2+2), la clause de centrage
      ne testait rien. Ajout de n_disc et largeur_centrage, branche
      STRUCTURE-RESOLUE-CENTRAGE-NON-DISCRIMINE, selftest qui MORD
      sur la configuration 2+2.
    D-3 : la partition des verdicts avait un trou NON VIDE (C1 et
      C2 et non-C3 sans canal 4 se lisait "l'etage B tient").
      Partition refondue, branches exclusives et exhaustives,
      branche STRUCTURE-RESOLUE-NON-ATTRIBUEE nommee. Corrige AVEC
      D-1, jamais seul -- l'avertissement de la certification est
      suivi a la lettre.
    D-4 : le seuil "au moins 1 ligne" de P-M15b tombait par le fond
      une fois sur deux (P = 0.5333 sous le taux de base). CHOIX
      MACHINE 1 : option (A), seuil k_min derive du fond ; sous
      k_min le verdict est SIGNATURE NON RESOLUE, k et P consignes.
    D-5 : le compte G2 n'etait pas derivable (heritages M12 et M14
      incompatibles, facteur 6, une seule porte tueuse). CHOIX
      MACHINE 1 : precedent M14 (273d0a53) nomme, 1 recherche,
      consignation sans porte -- total 38.
    D-6 : le texte v2 ne determinait pas F (lecture A par la regle
      contre lecture B par la parenthese : |F| 14 contre 16,
      PLANCHER_S4 dans un rapport 3.18). F refonde PAR REGLE, |F|
      et triplets en SORTIES, aucun compte de points dans le
      texte ; "assignation R-2'" definie en toutes lettres.
    N-6 a N-12 : declarees dans le corps aux emplacements que la
      certification prescrit. ITEM 5 : declare se certifier EN
      DEUX TEMPS (recopie au gel ; verrous, selftest et pre-vol a
      l'etape script).
  La v3 est une VERSION NEUVE a certifier ; aucun code avant qu'un
  message de certification croisee cite l'empreinte du present
  bloc (E19). Le script s'appellera m15_site83_v1.py.
  CONVENTION D'EMPREINTES (N-10) : toute empreinte livree est
  ETIQUETEE (brut / canonique NFC+LF). Le present fichier est
  ASCII et LF seul : brut = canonique, dit ici une fois.
  C2 NE S'APPLIQUE PAS : M15 est integralement classique.
  SOURCE DE LA MANCHE : note de derivation P1 v5 (hors chaine,
  empreinte canonique NFC+LF 5704987e, au repertoire machine 2 --
  reserve v1 TOMBEE, certification v2 : empreinte concordante,
  citation litterale verifiee), section 6, entree P1-b -- falsifieur
  d'ETAGE B
  SEULEMENT, etiquete tel. La tension consignee par machine 2 (section
  8.3 de la re-derivation 97c02eab) est l'objet de l'observable (ii).
  Les exigences 8.1, 8.2 et 8.6 citees ci-dessous sont celles de la
  re-derivation 97c02eab (re-attribution demandee par la certification).
  ATTENTE MACHINE 2 : INSCRITE avant certification, dans la note
  de certification v2 elle-meme (section 13, note 9088ce59,
  "inscrite ici, jamais reecrite" -- regle de campagne, precedent
  M12). Le texte opposable est la note ; rappel au dossier,
  etiquete RESUME : P-M15a = STRUCTURE-AU-SITE-RESOLUE attendu,
  forme V-CREUX (~0.55 ; ~0.35 PAS-DE-STRUCTURE-RESOLUE ; ~0.10
  autre forme), res_E au PROCHE dans [0.03, 0.08] ; P-M15b = k
  dans {0, 1, 2}, donc SIGNATURE NON RESOLUE au seuil k_min = 3 ;
  manche : ~0.25 sur P-M15c, ~0.40 sur plancher de comptes
  manque. Les attentes des deux machines DIVERGENT sur (ii) et
  sur la forme de (i) -- consigne ; aucune ne se reecrit.

QUESTION
--------
Au site 8/3 (w2 = 8/3, ordre q = 11), la table des rangs (note P1 v5,
section 1, etage A ACQUIS) donne : p=4 -> (6,2) ; p=5 -> (3,1) ;
p=7 -> (3,1). Sous l'etage B (hierarchie des amplitudes : rangs
relegues negligeables), AUCUNE structure de E n'existe a 8/3. Mais
dans M12, le point 2.67 -- seul point d'ordre 11 du programme, a
1/300 de 8/3 -- est mort d'une explosion SOUS s* (mecanisme E27 :
grossiere mordue, seule grossiere non vide des 67 lignes, degre
impair). Candidat-signature du site. M15 separe les deux questions
par DEUX observables independantes :
  (i)  P-M15a -- E des survivants au voisinage du site : une structure
       de E resolue au-dessus du PLANCHER de rugosite du fond, centree
       au site a la resolution de la grille, portee par les canaux
       5/7, FALSIFIE l'etage B. Son absence a la resolution declaree
       le laisse tenir -- sans le prouver.
  (ii) P-M15b -- motif des consignations sous-seuil pres du site, par
       mecanisme et par degre : la signature "grossiere mordue a degre
       impair" est-elle reproductible en points neufs ?
Un rang (3,1) peut etre trop faible pour creuser E et neanmoins
structurer le dessous du seuil : les deux lectures peuvent differer,
AUCUNE ne prejuge l'autre (note v5, section 6). Le cas ou les morts
au site empechent (i) de conclure recoit sa branche de lecture ecrite
d'avance, P-M15c -- l'asymetrie epistemique qui reste est declaree en
LIMITATIONS (exigence 8.2 : la perte est une donnee, pas de
l'attrition).

DERIVATIONS PREALABLES (faits, sources par empreinte)
-----------------------------------------------------
(a) Rangs a 8/3 : (6,2)/(3,1)/(3,1) pour p = 4/5/7 -- j*q <= r*p et
    j*q = r*p (mod 2), q = 11. CORRECTIF N-4 : le rang (6,2) a p=4
    est PERMIS par la condition de parite (2*11 = 22 <= 6*4 = 24,
    memes parites). Une structure canal 4 au site n'est donc PAS une
    violation de l'etage A : elle contredirait la hierarchie des
    amplitudes (etage B), au rang (6,2) -- consignation nommee plus
    bas, aucune porte automatique.
    DECLARATION N-6 : la note v5 enonce le triplet des rangs dans
    DEUX ordres (table de la section 1 contre prose de la section
    2) ; l'ordre opposable est celui de la table section 1 --
    (6,2)/(3,1)/(3,1) pour p = 4/5/7 -- confirme par la
    re-derivation machine 2 ; la correction de la note est hors
    chaine, due a sa prochaine version.
(b) CORRECTIF N-1 -- le pas de s*4 est LOCALISE par la chaine :
      s*4(2.55) = 2.881241 (fa109da9)
      s*4(2.60) = 7.157439 (ad275870, M11)
      s*4(2.67) = 7.462573 (fa109da9)
    facteur total 2.590, dont 95.6 % consomme dans [2.55, 2.60] en
    ln ; la calibration inter-manches est bit-identique (pilote M12,
    24/24). Le programme (2.62 a 2.73) est ENTIEREMENT AU-DESSUS du
    pas. La crainte de contamination canal 4 a gauche tombe ; la
    redondance du flanc gauche est requalifiee : attrition generale
    seulement. La pente residuelle du fond canal 4 reste consignee
    comme PAS/FOND, jamais lue comme 8/3.
(c) Le crible sous-seuil p=4 dans [2.70, 3.30] est ENTRELACE au
    centieme (delta 48.3, JSON 22fa1760) ; 2.70 y est MORT (fenetre
    fine, 0.924-0.966 s*), a 1/100 de 2.69 ET de 2.71. CONSEQUENCE
    GELEE : risque d'attrition declare au flanc droit ; plancher en
    COMPTES par flanc, bords = extremes SURVIVANTS, aucun survivant
    nomme (lecon 48.6).
(d) Prior du mecanisme vise par (ii) : trois instances consignees de
    "grossiere mordue" dans la lignee, toutes a degre impair
    (7|1.70|-1, pilote ed0e27b1 ; 7|2.67|+1, run fa109da9 ;
    5|2.50|-1, M14 68df6576). CORRECTIF N-7 -- un compte inscrit se
    compte : les TROIS instances portent un cote au registre (cle
    G6 = p|w|sgn), repartition 2 x (-1) pour 1 x (+1) ; a 2.50 le
    cote +1 survit avec grossiere vide (delta 50.4). DECLARATION
    (materiau D-4) : la restriction du prior a la parite impaire
    n'est PAS etablie statistiquement -- 3/96 impair contre 0/87
    pair, Fisher unilateral p = 0.1422 (certification v2) ; elle
    reste la classe PRE-ENREGISTREE (mecanisme echantillonne,
    lecon 48.5), et les instances p=4 sont comptees separement
    quoi qu'il arrive. Aucune clause de contiguite nulle part.
(e) Parite a degre pair demontree puis reproduite au bit (M11 ;
    P-M12e) : une seule ligne p=4 par point, sous condition G8a/G8b.
(f) DECLARATION N-2 -- la manche n'est PAS aveugle. E est deja connu
    a 0.01-0.03 des six points du programme (exigence 8.6 : la
    provenance d'une geometrie qui suit une reconnaissance se
    declare) :
      2.60  E = +0.5554  (M10+M11 : ad275870 x 7cf3624b)
      2.67  E = +0.4274  (M12 -- POINT PERDU, valeur NON OPPOSABLE)
      2.72  E = +0.5174  (fa109da9)
      2.75  E = +0.5251  (M10+M11)
      2.78  E = +0.5193  (fa109da9)
      2.80  E = +0.5426  (fa109da9)
    L'ancre G1' 2.72 tombe entre 2.71 et 2.73 ; son E recalcule est
    consigne comme contexte du flanc droit, aucune porte.
    FAIT ANTERIEUR, consigne tel (ni preuve ni oubli) : en
    recombinant la carte brute au site -- 2.67 est un point PERDU en
    M12, la valeur n'est pas opposable, et un resume ne se recalcule
    pas depuis un bloc brut (D1-3) -- E(2.67) est environ +0.427,
    soit -0.106 sous la corde 2.60<->2.72, porte principalement par
    le canal 7, c'est-a-dire le rang (3,1). Le materiau anterieur
    pointe donc vers une STRUCTURE au site, contre l'attente v1 de
    machine 1 (voir ATTENTES, addendum).

GEOMETRIE ET PROGRAMME FIGE
---------------------------
Site : w2 = 8/3 EXACT (Fraction(8,3)). Toutes les distances au site
et toutes les selections sont evaluees en arithmetique EXACTE
(entrees = centiemes exacts ; regle candidate 15, instance declaree).
Points du programme, grille au centieme, TOUS PROPRES (ITEM 1 v1 :
CERTIFIE, log section 5 -- rayons <=6 : 0.12 | 7-8 : 0.03 | 9-10 :
0.0075 | 11-12 : 0.001875, marge 1.10, six marges strictement
positives) :
  flanc gauche : 2.62, 2.64, 2.65   (d = 14/300, 8/300, 5/300)
  flanc droit  : 2.69, 2.71, 2.73   (d = 7/300, 13/300, 19/300)
CRITERE DE NOUVEAUTE, NOMME (correctif N-3) : nouveaute par VALEUR
EXACTE -- aucun des six points ne porte de ligne mesuree dans aucun
artefact de la lignee (7cf3624b, ad275870, fa109da9, ed0e27b1,
70fe5611, 22fa1760, 68df6576) ; verifie par la certification v1
(log section 6, lecture litterale : six NEUFS). La regle de distance
d >= 0.03 a la grille M10/M11 (bf9866a7) n'est PAS reconduite,
motifs declares : (1) elle etait propre a M12 -- precedent M14, qui
a mesure 2.46 a 1/100 de 2.45 ; (2) tester un site situe a moins de
0.01 d'un point de grille impose des points dans ce rayon.
Proximites consignees : 2.62 a 1/50 de 2.60 (grille M10/M11, E
connu) ; 2.73 a 1/50 de 2.75 (point de grille ET brule du pilote --
le brulage porte le point 2.75 par valeur, pas un voisinage).
Six points = les quatre requis par la note v5 + un point de
redondance par flanc (attrition : (c) a droite, generale a gauche
apres N-1).
Lignes par point : p=4 une ligne (cote pre-designe : +1) ; p=5 deux
cotes ; p=7 deux cotes. Convention (f) aux degres impairs :
s*_p = min(sP, sM), asymetries consignees.
Protocole de la lignee, inchange : w1 = 1, g = 0.05, RK4 dt = 0.006,
T = 400, cap 1e4, moteur c8ed357b SANS MODIFICATION.

DEFINITIONS COMMUNES DES PORTES (forme derivee, regle 13)
---------------------------------------------------------
  pas_p, sF_p : pas final de la fenetre fine et s* retenu par la
    convention (f) de la ligne, consignes au JSON, par ligne.
  B_E(point) = ((pas_4/sF_4) + 2.25*(pas_5/sF_5)) + 1.25*(pas_7/sF_7)
    -- FORME ET ORDRE DE SOMMATION DE M14 (N-3) RECONDUITS :
    evaluation gauche-droite, convention de cloture au bit.
  B_E57(point) = (2.25*(pas_5/sF_5)) + 1.25*(pas_7/sF_7)
    -- convention NOUVELLE, declaree ici : meme ordre gauche-droite.
  B_E4(point) = pas_4/sF_4.
  E(point) = (ln sF_4 - 2.25*ln sF_5) + 1.25*ln sF_7 (cloture M12).
  S57(point) = (-2.25*ln sF_5) + 1.25*ln sF_7. S4(point) = ln sF_4.
  DECLARATION N-8 : E(point) n'egale PAS S4(point) + S57(point) au
    bit (clotures differentes : E ferme en (a-b)+c, S57 en (-b)+c ;
    ecart mesure 1.110e-16, certification v2). AUCUNE porte ne
    compare E a S4 + S57. Le "partage p=5 / p=7 de res_S57" est
    consigne comme COUPLE de residus par canal, chaque canal contre
    sa propre corde ; sa somme n'egale res_S57 qu'a la cloture
    pres -- declare non exact, aucune porte dessus.
  Par flanc, parmi les survivants du flanc : PROCHE = distance exacte
    minimale au site ; LOIN = distance exacte maximale.
  CORDE : pour une grandeur X, corde_X(x) = interpolation lineaire
    entre (LOIN_g, X(LOIN_g)) et (LOIN_d, X(LOIN_d)).
  RESIDU : res_X(b) = X(b) - corde_X(b), evalue aux survivants
    STRICTEMENT interieurs (les LOIN sont les ancres de la corde,
    residu nul par construction).
  BARRE DE CORDE (D-3, forme M14 par paire, etendue a une corde --
    la resolution d'une corde combine ses deux ancres) :
    barre(b)   = 10*((B_E(LOIN_g) + B_E(LOIN_d)) + B_E(b))
    barre57(b) = 10*((B_E57(LOIN_g) + B_E57(LOIN_d)) + B_E57(b))
    barre4(b)  = 10*((B_E4(LOIN_g) + B_E4(LOIN_d)) + B_E4(b))
  ASSIGNATION R-2' (D-6, definie en toutes lettres) : pour un
    point w, la marge normalisee d'une famille q:r du catalogue
    R-2' est |w - q/r| / rayon(classe d'ordre de r) ; l'ASSIGNATION
    R-2'(w) est la famille qui REALISE LE MINIMUM de cette marge
    (la "pire famille"). Egalites decidees en Fraction ; en cas
    d'egalite exacte, ordre le plus bas puis denominateur le plus
    petit. (Lecture argmin appliquee par machine 2 a la
    certification v2 : elle range 2.42, 2.45 et 2.55 sous 5:2.)
  PLANCHER DE RUGOSITE EN COURBURE (D-1, refondu -- homogene a ce
    qu'il doit exclure) :
    Ensemble F, PAR REGLE (D-6 ; |F| est une SORTIE, aucun compte
    de points dans le present texte) :
      F = { w : w appartient a (grille M10/M11 : ad275870 x
            7cf3624b) union (points M12 : fa109da9), tel que
            (1) la ligne p=4 en w n'est PAS exclue G6 dans son
                artefact ;
            (2) les lignes p=5 et p=7 en w ne sont PAS exclues G6
                dans leur artefact ;
            (3) w est R-2'-PROPRE (meme regle que ci-dessus) ;
            (4) distance exacte |w - 8/3| > 19/300 (l'etendue du
                programme) ;
            (5) assignation R-2'(w) differente de 5:2 (la seule
                structure de E mesuree hors 8/3 ; les points
                68df6576 n'entrent pas dans F pour la meme
                raison, declare). }
      Appartenance decidee en Fraction (entrees = centiemes
      exacts).
    Facteur geometrique, exact : g(a, b, c) = (b - a) * (c - b),
      en Fraction.
    COURBURES PRE-RUN : sur tous les triplets a < b < c de F avec
      c - a <= 11/100 (la largeur du programme, en exact),
      residu(b | a, c) = X(b) - interpolation lineaire a<->c en b,
      K_X = max des |residu(b | a, c)| / g(a, b, c),
      pour X = E, S57, S4 respectivement.
    PLANCHER PAR POINT, derive AU RUN (regle 13 -- jamais un
      nombre) : pour chaque survivant strictement interieur b,
      PLANCHER_X(b) = K_X * g(LOIN_g, b, LOIN_d).
    Calcul des K_X au demarrage du script depuis les artefacts
      (jamais tape) ; K_E, K_S57, K_S4, F et la liste des triplets
      CONSIGNES PRE-RUN a la certification (ITEM 6) et re-derives
      au run : la resolution de structure est opposable avant le
      run en courbure, et par point des que la geometrie des
      survivants est connue (discipline E27 : la resolution fait
      partie de la mesure).
  SEUILS, PAR POINT : seuil(b) = max(PLANCHER_E(b), barre(b)) ;
    seuil57(b) = max(PLANCHER_S57(b), barre57(b)) ;
    seuil4(b) = max(PLANCHER_S4(b), barre4(b)).
    Sens declare : defavorable au declenchement du falsifieur.
  CENTRAGE DISCRIMINANT (D-2) :
    n_disc = nombre de survivants strictement interieurs b tels
      que b n'appartient pas a {PROCHE_g, PROCHE_d} ;
    largeur_centrage = PROCHE_d - PROCHE_g, en Fraction,
      consignee au JSON quoi qu'il arrive.

PORTES
------
P-M15a  UNE STRUCTURE DE E, AU SITE, PORTEE PAR LES CANAUX 5/7 ?
        (cible declaree : ETAGE B -- exigence 8.1 de 97c02eab)
  Clauses, sur les survivants du programme :
    (C1) AMPLITUDE : max des |res_E(b)| sur les interieurs > seuil(b)
         au point x_M qui le realise.
    (C2) CENTRAGE, a la resolution de la grille : x_M appartient a
         {PROCHE(gauche), PROCHE(droit)}. La resolution de centrage
         est la largeur de l'intervalle (PROCHE_g, PROCHE_d),
         consignee (au programme complet : 1/25, le site interieur).
    (C3) CANAUX : |res_S57(x_M)| > seuil57(x_M).
  VERDICTS (D-3 : partition en branches EXCLUSIVES et EXHAUSTIVES
  sous plancher de comptes atteint -- tout profil tombe dans
  exactement une branche, teste au selftest) :
    PAS-DE-STRUCTURE-RESOLUE ssi NON C1
      -> l'etage B TIENT AU SITE, A LA RESOLUTION PORTEE
         (courbures consignees pre-run, planchers par point +
         geometrie ; voir LIMITATIONS).
    STRUCTURE-NON-CENTREE (consignation, aucune lecture 8/3) ssi
      C1 ET NON C2 : structure resolue ailleurs dans la fenetre,
      matiere.
    STRUCTURE-AU-SITE-RESOLUE ssi C1 ET C2 ET C3 ET n_disc >= 1
      -> ETAGE B FALSIFIE AU SITE. Consignes : le partage p=5 /
         p=7 de res_S57 (couple par canal, N-8 ; mesure directe de
         la balance (3,1)) ; la FORME, par les signes des residus
         aux deux PROCHE -- memes signes : V-CREUX (negatifs) ou
         V-BOSSE (positifs) ; signes opposes : FALAISE, sens
         consigne (precedent : M14).
    STRUCTURE-RESOLUE-CENTRAGE-NON-DISCRIMINE (consignation,
      AUCUNE lecture 8/3) ssi C1 ET C2 ET C3 ET n_disc == 0 : au
      plancher de comptes exact (2+2), tout interieur est un
      PROCHE et C2 ne teste rien (D-2) ; largeur_centrage au
      JSON -- la resolution de centrage passee de 1/25 a jusqu'a
      7/100 est DITE, pas tue.
    STRUCTURE-CANAL-4-CANDIDATE ssi C1 ET C2 ET NON C3 ET
      |res_S4(x_M)| > seuil4(x_M) : cible ETAGE B au rang (6,2)
      permis (correctif N-4) ; REPLICATION REQUISE avant toute
      lecture ; aucune porte automatique.
    STRUCTURE-RESOLUE-NON-ATTRIBUEE (consignation) ssi C1 ET C2
      ET NON C3 ET |res_S4(x_M)| <= seuil4(x_M) : la bande D-3
      est non vide des que K_S57 + K_S4 > K_E ; l'etage B N'EST
      PAS declare tenir dans cette branche.
    NON CONCLUANT DE GEOMETRIE ssi plancher de comptes manque --
      renvoi P-M15c ; les six branches ci-dessus supposent le
      plancher atteint.
  PLANCHER DE COMPTES (lecon 48.6) : au moins 2 points survivants
    PAR flanc. Un point est SURVIVANT ssi ses cinq lignes aboutissent
    (toute exclusion de ligne -> point perdu, repercussion G7, motif
    porte).

P-M15b  LA SIGNATURE SOUS-SEUIL EST-ELLE REPRODUCTIBLE EN POINTS
        NEUFS ? (cible declaree : la tension 8.3 -- ni confirmation
        ni refutation de l'etage B, dit d'avance)
  Domaine : les lignes du programme de cette manche, cette geometrie,
  cette resolution ; AUCUNE juxtaposition avec les comptes d'une
  autre manche (discipline E27) ; l'instance 2.67 de fa109da9 est le
  PRIOR motivant, jamais poolee.
  Compte : k = nombre de lignes a degre IMPAIR (p dans {5,7}) avec
    "grossiere mordue" : explosion consignee sous s* dans la passe
    grossiere (ratio s_explosion/s* et resolution de passe
    consignes) avec fenetre fine vide, OU exclusion G6 par
    explosion sous-seuil -- definitions et seuils HERITES A
    L'IDENTIQUE de la chaine M12/M14 (ITEM 5), resolutions par
    consignation (correctif E27).
  SEUIL DERIVE DU FOND (D-4, option A retenue par machine 1 --
    forme derivee, regle 13) :
    b_fond = 3/96 exact -- taux de base compte au registre par la
      certification v2 (champ grossiere present, degre impair ;
      les 64 lignes de M10 sont HORS denominateur, champ absent --
      dit, pas cache) ;
    n_eff = nombre de lignes impaires du programme dont la passe
      grossiere est consignee (24 au programme complet ; les
      gardes peuvent soustraire : forme derivee) ;
    k_min = min { k : P(Binomiale(n_eff, b_fond) >= k) <= 1/20 },
      queue calculee en Fraction (b_fond exact), comparaison a
      1/20 EXACTE (regle candidate 15 : aucune frontiere
      flottante) ; k_min = 3 pour n_eff = 24.
  SIGNATURE PRESENTE ssi k >= k_min.
  SIGNATURE NON RESOLUE ssi k < k_min ; k, n_eff, k_min et
    P_fond(>= k) consignes -- une instance sous k_min est une
    CONSIGNATION, pas un verdict.
  (Aucune branche "SIGNATURE ABSENTE" : sous le taux de base,
  k = 0 sur n_eff = 24 a une probabilite 0.4667 -- l'absence
  n'est pas resolvable a cette taille, dit d'avance.)
  Consignes systematiques, par degre et par cote, comptes separes :
  instances p=4 (mecanisme distinct attendu, delta 48 : fenetre
  fine) ; marges sous s* ; positions. Comptes en forme derivee :
  comptes + sautes == attendu, par categorie.

P-M15c  BRANCHE DE LECTURE ECRITE D'AVANCE -- LES MORTS AU SITE
        (correctif N-5 ; exigence 8.2 : la perte est une donnee)
  Si le plancher de comptes de (i) tombe ET qu'au moins une des
  lignes perdues est une "grossiere mordue" a degre impair (comptee
  par P-M15b), le verdict de manche est nomme :
    NON-CONCLUANT-(i)-PAR-SIGNATURE
  Lecture jointe, pre-ecrite : la signature sous-seuil au site est
  assez forte pour tuer la mesure de E -- compatible avec un rang
  (3,1) actif SOUS le seuil ; ceci NE mesure PAS E et NE prononce
  RIEN sur l'etage B. L'asymetrie epistemique restante (dans la
  configuration ou l'effet cherche est le plus fort, la manche ne
  peut pas falsifier l'etage B par (i)) est declaree en LIMITATIONS,
  et le chemin de sortie est NOMME : une manche ulterieure a
  geometrie reculee (distances superieures au site), hors du present
  gel. Si le plancher tombe SANS aucune grossiere mordue impaire :
  NON CONCLUANT DE GEOMETRIE ordinaire.

TEST NEGATIF DU CRITERE COMPLET (ITEM 7 -- rejoue sur le critere v3)
--------------------------------------------------------------------
  Joue par machine 2 A LA CERTIFICATION, en codant le critere depuis
  le SEUL texte du present gel -- ce qui teste aussi son
  executabilite sans interpretation. CHAQUE branche de la partition
  D-3 porte au moins un vecteur (la certification v2 relevait que
  C3 n'etait exercee qu'une fois : corrige). Les ATTENDUS portent
  TOUTES les clauses qu'ils pretendent exercer (N-9) ; aux cas
  negatifs, le banc CONSIGNE la clause qui bloque -- un verdict
  juste pour une mauvaise raison n'est pas un test passe (lecon du
  banc v2 : l'ondulation 0.02 ne tirait pas par C2, pas par le
  plancher, alors que le motif ecrit disait le plancher).
  (1) M14 reel (68df6576), mappe deux-flancs autour de 5/2 :
      LOIN 2.42/2.55, interieurs 2.46, 2.48, 2.52, 2.54.
      ATTENDU : STRUCTURE-AU-SITE-RESOLUE -- C1 (x_M = 2.48,
      res_E = +0.2647, marge 2.33x sur le plancher-courbure,
      valeurs certification v2) ; C2 (x_M dans {PROCHE}) ; C3
      (res_S57 = +0.2598, au-dessus de son seuil par point) ;
      n_disc >= 1 (quatre interieurs, deux non-PROCHE). Forme
      FALAISE (residus aux PROCHE +0.2647 / -0.156, signes
      opposes). Le canyon DOIT mordre.
  (2) Troncon lisse REEL : le groupe droit de F. Pseudo-site
      designe par machine 2 parmi les choix rendant le banc
      jouable -- la v2 proposait "par exemple 2.76", qui rend le
      banc injouable (un seul point a gauche du pseudo-site) ;
      machine 2 a designe 2.79, seul choix donnant 2+2. ATTENDU :
      PAS-DE-STRUCTURE-RESOLUE, clause bloquante C1 (propriete
      d'homogeneite du plancher-courbure : residu = courbure
      locale x g <= K_X x g ; joue par machine 2 : residu 0.0220
      sous plancher 0.0569). Un fond que la campagne a MESURE ne
      doit pas faire tirer le falsifieur.
  (3) Vecteurs synthetiques (banc v1, log section 9), rejoues sur
      le critere v3 :
      - pente monotone croissante / decroissante -> PAS-DE-
        STRUCTURE-RESOLUE (la corde detrend toute pente) ; clause
        bloquante consignee : C1 ;
      - creux centre 0.10 -> STRUCTURE-AU-SITE-RESOLUE, forme
        V-CREUX (TOUTES clauses : C1, C2, C3, n_disc consigne) ;
      - bosse centree -> STRUCTURE-AU-SITE-RESOLUE, forme V-BOSSE
        (toutes clauses) ;
      - extremum hors site (fond lisse k = 8.0, max en 2.70) ->
        NE TIRE PAS : residu a l'argmax interieur 2.69 = 0.0224
        SOUS le plancher-courbure 0.0758 (certification v2), la
        ou le plancher plat v2 tirait (temoin D-1a) ; clause
        bloquante consignee : C1 ;
      - ondulation 0.02 -> verdict attendu : PAS
        STRUCTURE-AU-SITE-RESOLUE ; la clause bloquante est
        CONSIGNEE, pas presumee.
  (4) Vecteur canal 4 : structure portee par S4 seul (E deplace
      via ln sF_4, S57 plat). ATTENDU : STRUCTURE-CANAL-4-
      CANDIDATE -- C1 vraie, C2 vraie, C3 FAUSSE exercee,
      |res_S4| > seuil4.
  (5) Temoin de bande (certification v2 : res_S57 et res_S4
      chacun sous son seuil, res_E au-dessus du sien --
      realisable des que K_S57 + K_S4 > K_E). ATTENDU :
      STRUCTURE-RESOLUE-NON-ATTRIBUEE -- la branche du trou D-3,
      nommee, exercee ; l'etage B n'est PAS declare tenir.
  (6) Configuration 2+2 (plancher de comptes exact), extremum au
      PROCHE gauche (2.64 dans la configuration testee).
      ATTENDU : verdict DIFFERENT de STRUCTURE-AU-SITE-RESOLUE --
      STRUCTURE-RESOLUE-CENTRAGE-NON-DISCRIMINE si C1 et C2 et C3
      (n_disc = 0, D-2) ; exerce au banc ET au selftest du script.

GARDES
------
  Heritage : G1-G8 reprises A L'IDENTIQUE de la chaine M12 (gel v4
  bf9866a7) / M14 (gel 273d0a53), correctif E27 inclus (resolution
  par consignation). La reprise "a l'identique" est TESTEE par
  execution au script (toute reutilisation verbatim porte son test
  execute) -- ITEM 5. Designations propres a M15 :
  G1' CUSTODY (bloquante) : le point 2.72 re-mesure EN ENTIER (5
    lignes) contre fa109da9, ecart exige 0.0 EXACT par ligne. 2.72
    n'entre dans aucune porte : ancre, pas programme ; son E est
    consigne comme contexte du flanc droit.
  G2 INVARIANCE (D-5 -- precedent NOMME : M14, gel 273d0a53) : UNE
    recherche a 2g sur la ligne 7|PROCHE_droit|+1 (PROCHE_droit =
    survivant du flanc droit a distance exacte minimale du site,
    connu en fin de programme -- forme derivee) ; |K2/K1 - 1|
    CONSIGNE SANS PORTE. La designation M12 ("premier point de la
    liste", 6 recherches, tolerance 10 %, porte tueuse) n'est PAS
    reconduite, motifs : aucun referent de liste dans M15 ; une
    porte qui peut exclure une ligne aggrave le risque de
    plancher manque (0.40, certification v2).
  G4 PAS DE TEMPS : dt/2 sur la ligne maximisant g*s*^(p-1) parmi
    les lignes abouties, re-designee independamment par les deux
    machines.
  G6/G7 : heritees ; chaque consignation G6 porte sa resolution
    (E27) et alimente P-M15b selon son mecanisme.
  G8a/G8b PARITE (condition de la ligne p=4 unique) : au point 2.62,
    la ligne p=4 est mesuree des DEUX cotes ; G8a exige sP identique
    a sM au bit ; G8b est le test STRUCTUREL (exposant pair, test
    d'explosion symetrique) sur la source du moteur. Echec de l'un
    -> retour a la convention (f) integrale a p=4 (les deux cotes
    partout ; compte attendu mis a jour en forme derivee), consigne.
  VERROUS DE CUSTODY QUI MORDENT (correctif D-3) : le script porte
    un test execute montrant que CHAQUE verrou d'empreinte declenche
    sur une alteration minimale (forme math.nextafter sur une valeur
    importee, octet altere sur un bloc), temoin embarque -- la
    parade M14 est reconduite, pas seulement annoncee.
  Garde structurelle : l'APPEL utcnow( est interdit dans les sources
    (l'aiguille litterale du test se documente elle-meme).

COMPTES ATTENDUS (forme derivee -- des comptes, pas des affirmations)
---------------------------------------------------------------------
  programme : 6 points * (1 + 2 + 2) = 30 recherches
  G1' : 5 ; G8a : +1 (second cote p=4 en 2.62) ; G4 : +1 ;
  G2 : +1 (D-5, precedent M14)
  total : 38 ; balayages derives au script par la regle de la
  lignee. Verification : comptes + sautes == attendu, par categorie,
  derive dans l'artefact.
  REGLE D'ARRET ET FAISABILITE (ITEM 3 : RENDU par machine 2 a la
  certification v2, cite par empreinte 9088ce59) : le q_L LOCAL
  est derive sur le DOMAINE OPPOSABLE [2.35, 2.90[ -- le bloc p=4
  de [2.90, 3.05] (M13/M13b) est regime H-SAT, domaine DISTINCT
  au sens d'E27, jamais poole avec les morts du site ; la v2 les
  melangeait, corrige. Morts du domaine : 2.67 (M12), 2.70 a p=4
  (M13b), 5|2.50|-1 (M14). Valeurs consignees (bornes superieures
  q_L, unite = ligne signee) : p=4 -> 0.0855 (1 mort sur 34
  lignes) ; impair -> 0.0679 (3 sur 80). Jugement machine 2 :
  geometrie JOUABLE (~8 min), lecture a ~60 % -- P(plancher de
  comptes atteint aux deux flancs) = 0.60 ; P(configuration 3+3,
  la seule ou C2 discrimine) = 0.11 ; P(2+2 exact) = 0.20 ;
  chiffres OPTIMISTES deux fois (independance des morts supposee
  contre bloc contigu M13 au registre ; fait N-12). AUCUN arret
  mecanique n'est arme sur cette base : la manche reste jouable
  sous forte attrition PARCE QUE P-M15c en fait une lecture -- la
  perte est une donnee (8.2). Si machine 2 juge a la
  certification que la geometrie est devenue infaisable, le
  retour au gel est la voie ordinaire.

MES ATTENTES (machine 1 -- pour pouvoir avoir tort de mon propre fait)
  v1, CONSERVEE TELLE QUELLE :
    P-M15a : PAS-DE-STRUCTURE-RESOLUE. Flanc droit : E dans
    [0.45, 0.60] (continuite avec le groupe droit de fa109da9).
    Flanc gauche : AUCUNE attente ferme -- la position du pas de
    s*4 commande ; s'il faut choisir : pas acheve sous 2.62, donc
    flanc gauche aussi dans [0.45, 0.60] et D4 non resolu. J'ecris
    l'incertitude bimodale plutot que de la cacher.
    P-M15b : SIGNATURE PRESENTE -- 1 a 3 instances, p=5 plus
    probable que p=7, cote -1 plus probable que +1, marges dans
    [0.75, 0.95] s*.
    Le coeur de mon attente : LA DISSOCIATION -- (i) tient, (ii)
    presente.
  ADDENDUM v2 (2026-08-07, PRE-RUN, sur les seuls faits de chaine
  exhibes par la certification v1 ; la v1 ci-dessus reste au dossier
  comme trace de ce que je croyais avant compilation) :
    (1) N-1 leve la bimodalite : le pas est SOUS la fenetre. Flanc
    gauche attendu dans [0.45, 0.60] comme le droit ; res_S4 de
    fond, sous seuil4.
    (2) N-2 change mon attente centrale, et je le fais a decouvert :
    le fait anterieur (E(2.67) environ +0.427, non opposable,
    -0.106 sous la corde, porte canal 7 -- exactement le rang (3,1)
    de la derivation) pointe vers une structure au site. J'attends
    desormais : P-M15a = STRUCTURE-AU-SITE-RESOLUE, forme V-CREUX
    ou FALAISE, res_S57 dominant en canal 7, SI la structure atteint
    la largeur de la grille (5/300) ; PAS-DE-STRUCTURE-RESOLUE si
    elle est plus etroite. Je juge la premiere branche plus
    probable. P-M15b inchangee : SIGNATURE PRESENTE. L'attente
    centrale passe de la dissociation a la CONJONCTION
    structure + signature -- les deux faces d'un meme rang (3,1)
    actif.
  ADDENDUM v3 (2026-08-07, PRE-RUN ; la v1 et l'addendum v2
  restent ecrits tels quels -- une attente inscrite ne se reecrit
  pas, elle se traduit a decouvert) :
    (3) D-4 refonde le verdict de (ii) : k_min = 3 derive du
    fond. Mon attente v1 "1 a 3 instances" etait, sous le taux de
    base seul, satisfaite plus d'une fois sur deux (P(k >= 1) =
    0.53) -- c'est exactement ce que D-4 corrige ; j'en tire la
    lecon au lieu de retoucher le texte. Traduction dans la
    taxonomie v3, inscrite avant run : je mets la masse sur k
    dans {1, 2}, donc SIGNATURE NON RESOLUE au sens D-4,
    instances consignees avec marges et cotes. L'attente centrale
    s'affaiblit d'autant : la CONJONCTION que j'attends devient
    structure resolue (P-M15a) + instances consignees (k >= 1) ;
    le verdict PRESENTE au sens fort (k >= 3) reste possible, non
    attendu. Si k >= 3 tombe, la signature est un fait au sens
    D-4 ; si k = 0, mon attente v1 etait fausse de mon propre
    fait.

LIMITATIONS DECLAREES
  - Falsifieur d'ETAGE B SEULEMENT (etiquette note v5) ; ne touche
    ni l'etage A (acquis ailleurs), ni H-SAT, ni beta, ni la jambe
    quantique.
  - ASYMETRIE N-5, ecrite : dans la configuration ou l'effet est le
    plus fort (morts au site), la manche ne peut pas falsifier
    l'etage B par (i) -- elle rend NON-CONCLUANT-(i)-PAR-SIGNATURE
    (P-M15c). Le chemin de sortie est une geometrie reculee,
    ulterieure.
  - FAIT N-12, consigne : les deux seuls points jamais mesures a
    moins de 4/100 du site -- 2.67 (M12) et 2.70 (M13b) -- sont
    morts tous les deux. C'est la tension que la manche vient
    mesurer, et c'est aussi ce qui la menace (certification v2).
  - PAS-DE-STRUCTURE-RESOLUE n'est PAS une preuve : echappatoires
    declarees -- structure plus etroite que la distance du
    survivant le plus proche au site (au programme complet : 5/300
    a gauche, 7/300 a droite), moins profonde que le seuil (COURBURES
    consignees pre-run + planchers par point au run, ITEM 6), ou
    logee dans les trous si des points
    meurent. Le verdict porte sa resolution (E27).
  - CENTRAGE a la resolution de la grille seulement : un extremum
    reel dans l'intervalle (PROCHE_g, PROCHE_d) elargi d'un pas de
    grille est indiscernable d'un extremum au site ; la largeur est
    consignee. STRUCTURE-NON-CENTREE couvre le reste.
  - La manche n'est PAS aveugle (N-2) : les E voisins sont connus et
    declares en (f) ; le fait anterieur au site est consigne. La
    valeur de la manche est de rendre OPPOSABLE ce qui ne l'est pas.
  - Le PLANCHER (courbures K_X du fond opposable, HORS site et
    hors 5:2) mesure la rugosite deja observee ; sa
    representativite dans la fenetre est une hypothese declaree,
    au sens defavorable au declenchement.
  - |delta5|/|delta7| a 5:2 (exigence du gel M14) n'est PAS adresse.
  - Les E, residus et partages par canaux sont consignes quoi qu'il
    arrive : matiere pour N-4 (le pas), P3/P4. Aucune lecture
    mecanistique du crible (48.3) dans cette manche.
  - Protocole de la lignee inchange ; aucun fit nulle part (la regle
    14 est sans objet : E est ponctuel, les cordes sont des
    references locales a deux points, pas des ajustements).

ITEMS A CERTIFIER (v3, machine 2)
  1. CLOS (v1) -- R-2' et proprete des six points ; aucun retour.
  2. CLOS (v2) -- nouveaute par valeur exacte ; aucun retour.
  3. CLOS (v2) -- q_L local rendu, cite au corps (REGLE D'ARRET) ;
     a re-parapher seulement si domaine ou registre change.
  4. G2 : compte ECRIT (D-5, precedent M14 nomme, total 38) --
     valider la designation et le total.
  5. Heritage M12/M14, EN DEUX TEMPS (declare) : temps 1, recopie
     des definitions (grossiere, fenetre fine, G6), N-3 reconduit,
     barres par corde -- CLOS (v2) ; temps 2, verrous de custody
     qui mordent (math.nextafter, temoin embarque), selftest et
     pre-vol a moteur factice -- DUS A L'ETAPE SCRIPT, par la
     machine detentrice des sources certifiees.
  6. COURBURES K_E, K_S57, K_S4 (D-1) + ensemble F et triplets
     (D-6) : calcules par machine 2 depuis les artefacts a la
     certification, |F| et liste en SORTIES, CONSIGNES PRE-RUN --
     la resolution en courbure est opposable avant le run ; les
     planchers par point se derivent au run.
  7. TEST NEGATIF du critere v3 complet, code depuis le seul
     texte du gel : chaque branche de la partition exercee,
     attendus a toutes clauses (N-9), clause bloquante consignee
     aux cas negatifs. Le canyon doit mordre ; les DEUX fonds
     lisses doivent se taire.

IMPLEMENTATION
  m15_site83_v1.py, moteur classique c8ed357b SANS MODIFICATION,
  ecrit uniquement out/m15_results.json (incremental, une ecriture
  par point ; cles JSON = chaines ; forme canonique LF, labels
  normalises, date omise). Custody transitive : le script re-verifie
  a l'import les empreintes fa109da9 (reference G1'), ad275870 et
  7cf3624b (ensemble F du PLANCHER), et celle du present gel ; la
  note v5 (5704987e) est au repertoire des deux machines. Gel jumeau
  dans le docstring, bloc du TITRE a la ligne de cloture du present
  fichier, inclus, canonique NFC+LF, sha256 recalcule au demarrage
  depuis le fichier source. Selftest (ce que le script
  CALCULE) : la partition D-3 testee EXHAUSTIVE (tout profil
  tombe dans exactement une branche) ; le cas 2+2 MORD (D-2 :
  extremum au PROCHE gauche -> verdict different de
  STRUCTURE-AU-SITE-RESOLUE) ; k_min re-derive en Fraction,
  comparaison a 1/20 exacte (D-4). Pre-vol a moteur factice (ce
  que le script FAIT), joue par la machine detentrice des sources
  certifiees, avec un banc qui TUE : scenario de pertes a
  l'esperance derivee du q_L local (ITEM 3), branches de mort
  traversees, y compris la branche G8 en echec, la configuration
  2+2 et la branche P-M15c. DEPOT DU SCRIPT CONDITIONNE a la certification
  croisee (E19).

=== FIN DU GEL M15 ===
