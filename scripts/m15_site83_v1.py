"""PRE-ENREGISTREMENT M15 -- LE SITE 8/3 EN DOUBLE OBSERVABLE (P1-b, CLASSIQUE PUR)
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
"""
# =====================================================================
# m15_site83_v1.py -- MANCHE M15 (P1-b, site 8/3), machine 1, 2026-08-08
# Gel certifie e41f4da3 (certification croisee v3, note 8081a032, 0
# bloquant). Corps edite SEUL ; le fichier livre est ASSEMBLE (gel
# jumeau + corps) par _gabarit_m15.py -- l'assembleur refuse l'appel
# utcnow par assertion (S7) et re-verifie l'empreinte du gel.
# ARCHITECTURE (precedent m12_ponctuel_v2.py c5659f52) :
#   instrument = m12_pilote_v3.py importe par empreinte, custody
#   transitive (son gel 03e29c86 re-verifie a l'import) ; moteur
#   c8ed357b charge et verifie PAR le pilote -- chaine identique.
# DECLARATIONS DE CE SCRIPT (au JSON, meta.declarations) :
#   N-13 : "assignation R-2'" = argmin de la marge NORMALISEE d/rayon
#     (terme defini au gel v3) ; la lecture ABSOLUE de la certification
#     v2 differe sur 6 des 14 points de F, MEME ensemble F -- consigne.
#   N-14 : si le flanc droit ne rend aucun survivant, G2 n'a pas de
#     cible -- SAUTEE avec motif, recherches jouees = 37, la forme
#     derivee comptes + sautes == attendu porte la sautee.
#   N-15 : la resolution de la manche est chiffree a la note 8081a032,
#     section 5 ; les planchers PAR POINT du run sont consignes dans
#     resultats.pre_run et resultats.P_M15a -- le chiffre s'y re-derive.
#   HERITAGE : G6/balayages/G8b-masques/G4/G5/G3 par IMPORT du pilote
#     (reutilisation testee par l'empreinte 663b17e2 + gel transitif,
#     forme la plus forte du test de reprise exigee par ITEM 5).
# =====================================================================

import argparse, hashlib, importlib.util, json, math, os, sys
from fractions import Fraction

import numpy as np

MARQ_DEBUT = "PRE-" + "ENREGISTREMENT M15"
MARQ_FIN = "=== FIN DU GEL M15 " + "==="

# ---- empreintes gelees (COMPLETES, lecon S5) -------------------------
SHA_GEL = "e41f4da3685e6d1b930848f1e6ad27cf3c12ce291050cbd61194c0ee2326ba72"
SHA_PILOTE = "663b17e2955c79c09f1b6c0fb4443cd0c1f98be0db03ef089f5df682018ce905"
SHA_MOTEUR = "c8ed357b120352c4d1078307add3eaac285940c8bec00acc2ddc9ff386ab2c5c"
SHA_M10_JSON = "7cf3624b45dd7d2bb91d29485bd14599e749bd60ba683c4b0c0b224a28aba3bc"
SHA_M11_JSON = "ad275870847d440ecfb04e7b7108c24748d1a1126eb223c6b3db9a1c9038d124"
SHA_M12_JSON = "fa109da92e582520cfcb63b46bc41fa7d4b62295891f413bb97c6095b2fe59b1"
# reference d'ARRET du pre-run (ITEM 6) : note de certification v3,
# empreinte calculee a reception (brut = canonique, LF seul) --
SHA_NOTE_CERT_V3 = "8081a0325e0821de31d07b26f10f57afcb5f98a93c18e3e2634d314efb4f9402"

# ---- protocole (gel v3) ----------------------------------------------
FLANC_G = [2.62, 2.64, 2.65]
FLANC_D = [2.69, 2.71, 2.73]
POINTS = FLANC_G + FLANC_D
DEGRES = (7, 5, 4)                       # ordre d'execution ; p=4 en dernier (G8)
G8A_POINT = 2.62                         # second cote p=4, G8a/G8b
G1P_POINT = 2.72                         # ancre custody, 5 lignes vs fa109da9
SITE = Fraction(8, 3)
ETENDUE = Fraction(19, 300)              # condition (4) de F
LARGEUR_TRIPLET = Fraction(11, 100)
TOL_APPART = 1e-09                       # regle 11
TOL_G4 = 0.02                            # herite (pilote / m12)
EPS_PORTE = 1e-12
FACTEUR_BARRE = 10.0                     # barre de corde (D-3, forme M14)
B_FOND = Fraction(3, 96)                 # taux de base, compte au registre (D-4)
ALPHA = Fraction(1, 20)                  # seuil de queue, comparaison EXACTE
C_SIGMA = {4: 1.0, 5: 2.25, 7: 1.25}     # coefficients de E (m12, derivation (c))

# ---- REFERENCE D'ARRET DU PRE-RUN (note 8081a032, section 3) ---------
# Ces constantes ne sont JAMAIS utilisees comme valeurs de calcul : le
# script RE-DERIVE F, triplets et K_X depuis les artefacts et S'ARRETE
# si la re-derivation differe de la consignation pre-run de machine 2.
ATTENDU_F_CENT = (170, 173, 176, 184, 186, 215, 222, 227, 230,
                  260, 275, 278, 280, 285)
ATTENDU_TRIPLETS_CENT = ((170, 173, 176), (173, 176, 184), (176, 184, 186),
                         (222, 227, 230), (275, 278, 280), (275, 278, 285),
                         (275, 280, 285), (278, 280, 285))
ATTENDU_K_6DEC = {"E": "27.087844", "S57": "21.714077", "S4": "5.835765"}
TOL_K_REF = 5e-07   # demi-pas de la consignation a 6 decimales (tolerance
                    # DECLAREE : les K sont des flottants mesures -- regle
                    # candidate 15, branche "entrees non exactes")

# ---- comptes attendus, FORME DERIVEE ---------------------------------
def plan_signes(p, w, g8_echec):
    if p != 4:
        return [(+1, "sP"), (-1, "sM")]
    if w == G8A_POINT or g8_echec:
        return [(+1, "sP"), (-1, "sM")]
    return [(+1, "sP")]

def rech_attendues(g8_echec, g2_slot=1):
    prog = sum(len(plan_signes(p, w, g8_echec)) for p in DEGRES for w in POINTS)
    return prog + 5 + 1 + g2_slot        # + G1'(5) + G4(1) + G2 (joue OU saute)

def bal_attendus(g8_echec):
    return sum(len(plan_signes(p, w, g8_echec)) for p in DEGRES for w in POINTS)

assert rech_attendues(False) == 38 and rech_attendues(True) == 43
assert bal_attendus(False) == 31 and bal_attendus(True) == 36

FOUT = os.path.join("out", "m15_results.json")
FOUT_PREVOL = os.path.join("out", "m15_PREVOL.json")

VERDICTS_A = ("PAS-DE-STRUCTURE-RESOLUE", "STRUCTURE-NON-CENTREE",
              "STRUCTURE-AU-SITE-RESOLUE",
              "STRUCTURE-RESOLUE-CENTRAGE-NON-DISCRIMINE",
              "STRUCTURE-CANAL-4-CANDIDATE", "STRUCTURE-RESOLUE-NON-ATTRIBUEE")


# =====================================================================
# S1. GEL JUMEAU (convention : bloc du TITRE au terminateur inclus,
#     saut final inclus = fichier .md entier, 39 712 car.)
# =====================================================================

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
        print("Gel jumeau M15 v3 : sha %s -> %s"
              % (h[:16] + "...", "CONCORDANT" if h == SHA_GEL else "DISCORDANT"))
    if h != SHA_GEL:
        sys.exit("ARRET E19 : le gel jumeau ne correspond pas a la version certifiee.")
    return bloc, h


def _sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


def charger_pilote(chemin="m12_pilote_v3.py", verbeux=True):
    h = _sha(chemin)
    if verbeux:
        print("Instrument (pilote) %s -> %s" % (h[:24] + "...",
              "CONCORDANT" if h == SHA_PILOTE else "DISCORDANT"))
    if h != SHA_PILOTE:
        sys.exit("ARRET : l'instrument n'est pas celui que le gel designe.")
    spec = importlib.util.spec_from_file_location("m12_pilote", chemin)
    P = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(P)
    P.certifier_gel(verbeux=False)      # custody transitive : gel pilote 03e29c86
    if verbeux:
        print("  gel jumeau du pilote re-verifie (03e29c86...) : CONCORDANT")
    for k in ("recherches", "balayages", "sautees", "balayages_sautes"):
        P.CPT[k] = 0
    return P


def charger_artefacts(prevol, rep_prevol):
    """Trois artefacts de la lignee : m10 (p=5,7), m11 (p=4), m12 (carte
    ponctuelle + reference G1'). En REEL les empreintes COMPLETES sont
    exigees ; en PREVOL, sources reelles si conformes, sinon
    synthetiques (banniere, jamais la voie du run reel)."""
    chemins = {"m10": os.path.join("out", "m10_results.json"),
               "m11": os.path.join("out", "m11_results.json"),
               "m12": os.path.join("out", "m12_results.json")}
    attendus = {"m10": SHA_M10_JSON, "m11": SHA_M11_JSON, "m12": SHA_M12_JSON}
    meta = {}

    def reelles(strict):
        out = {}
        for nom, pth in chemins.items():
            if not os.path.exists(pth):
                if strict:
                    sys.exit("ARRET : source certifiee absente (%s)" % pth)
                return None
            h = _sha(pth)
            if h != attendus[nom]:
                if strict:
                    sys.exit("ARRET : %s -- empreinte %s, exigee %s"
                             % (pth, h, attendus[nom]))
                return None
            out[nom] = json.load(open(pth, encoding="utf-8"))["resultats"]
            meta[nom + "_sha256"] = h
        meta["statut"] = "REELLES"
        return out

    if not prevol:
        return reelles(strict=True), meta
    r = reelles(strict=False)
    if r is not None:
        print("PREVOL : sources REELLES presentes et conformes -- utilisees.")
        return r, meta
    out = {}
    for nom in chemins:
        pth = os.path.join(rep_prevol, os.path.basename(chemins[nom]))
        if not os.path.exists(pth):
            sys.exit("ARRET PREVOL : ni sources reelles conformes, ni %s" % pth)
        out[nom] = json.load(open(pth, encoding="utf-8"))["resultats"]
        meta[nom + "_sha256"] = _sha(pth)
    print("=" * 70)
    print("PREVOL : SOURCES SYNTHETIQUES (%s) -- empreintes HORS REGISTRE," % rep_prevol)
    print("valides pour le pre-vol SEULEMENT ; le run reel les refusera.")
    print("Le pre-vol OPPOSABLE est celui de la machine qui detient les")
    print("sources certifiees ; ceci est une REPETITION.")
    print("=" * 70)
    meta["statut"] = "SYNTHETIQUES_PREVOL"
    return out, meta


# =====================================================================
# S2. R-2' : catalogue, proprete, ASSIGNATION (D-6, en toutes lettres)
#     Catalogue et rayons repris du pilote (RESONANCES / rayon) --
#     re-declares ici en Fraction pour l'arithmetique exacte de la
#     selection (regle candidate 15).
# =====================================================================

def rayon_fr(o):
    return (Fraction(12, 100) if o <= 6 else Fraction(3, 100) if o <= 8 else
            Fraction(75, 10000) if o <= 10 else Fraction(1875, 1000000))

CATALOGUE = sorted({(k, l) for k in range(1, 13) for l in range(1, 13)
                    if k + l <= 12 and math.gcd(k, l) == 1 and l <= k <= 3 * l})
MARGE_R2P = Fraction(110, 100)


def est_centieme(w):
    return abs(w * 100 - round(w * 100)) < 1e-9


def analyse_r2p(w):
    """(propre, assignation_v3, marge_min). Entrees centiemes -> Fraction
    exacte ; sinon flottant a tolerance declaree (aucun point du programme
    n'est concerne ; la grille M10/M11 porte sqrt2, ecarte a 0.046 du bord).
    Assignation v3 (N-13) : argmin de d/rayon, la "pire famille" ;
    egalites en exact -> ordre le plus bas, puis denominateur le plus
    petit (gel v3, DEFINITIONS)."""
    exact = est_centieme(w)
    wq = Fraction(round(w * 100), 100) if exact else w
    lignes = []
    for k, l in CATALOGUE:
        r = rayon_fr(k + l)
        d = abs(wq - Fraction(k, l)) if exact else abs(wq - k / l)
        lignes.append((d, r if exact else float(r), k, l))
    marges = [d - MARGE_R2P * r if exact else d - float(MARGE_R2P) * r
              for d, r, k, l in lignes]
    propre = all(m > 0 for m in marges)
    a3 = min(lignes, key=lambda t: (t[0] / t[1], t[2] + t[3], t[3]))
    return propre, (a3[2], a3[3]), min(marges)


# =====================================================================
# S3. PRE-RUN (ITEM 6) : F PAR REGLE, TRIPLETS, COURBURES K_X --
#     re-derives des artefacts, ARRET si la re-derivation differe de la
#     consignation pre-run (note 8081a032, section 3). Les valeurs de
#     reference ne servent QUE d'arret ; les valeurs UTILISEES sont
#     derivees (gel : "jamais tape").
# =====================================================================

def ligne_g6_exclue(res, p, w):
    pref = "%d|%.12f|" % (p, w)
    return any(v.get("exclue") for k, v in res["G6"].items() if k.startswith(pref))


def x_du_point(s4, s5, s7):
    """Clotures du gel (DEFINITIONS + N-8) : E ferme en (a-b)+c, S57 en
    (-b)+c ; E n'egale PAS S4+S57 au bit, AUCUNE porte ne les compare."""
    return {"E": (math.log(s4) - 2.25 * math.log(s5)) + 1.25 * math.log(s7),
            "S57": (-2.25 * math.log(s5)) + 1.25 * math.log(s7),
            "S4": math.log(s4),
            "c5": -2.25 * math.log(s5), "c7": 1.25 * math.log(s7)}


def derive_pre_run(art):
    """F (5 conditions, Fraction), triplets (c-a <= 11/100 exact), K_X.
    |F| et la liste sont des SORTIES (D-6)."""
    grille = sorted(float(k.split("|")[1]) for k in art["m11"]["carte"])
    pts12 = sorted(float(k.split("|")[1]) for k in art["m12"]["carte"]
                   if k.startswith("4|"))
    membres, rejets = [], {}
    for w, src in [(w, "grille") for w in grille] + [(w, "m12") for w in pts12]:
        if src == "grille":
            c1 = not ligne_g6_exclue(art["m11"], 4, w)
            c2 = not (ligne_g6_exclue(art["m10"], 5, w)
                      or ligne_g6_exclue(art["m10"], 7, w))
        else:
            c1 = not ligne_g6_exclue(art["m12"], 4, w)
            c2 = not (ligne_g6_exclue(art["m12"], 5, w)
                      or ligne_g6_exclue(art["m12"], 7, w))
        propre, a3, marge = analyse_r2p(w)
        exact = est_centieme(w)
        c4 = (abs(Fraction(round(w * 100), 100) - SITE) > ETENDUE) if exact \
            else abs(w - float(SITE)) > float(ETENDUE)
        c5 = a3 != (5, 2)
        if c1 and c2 and propre and c4 and c5:
            membres.append((w, src, a3, marge))
        else:
            rejets["%.12f" % w] = "".join(
                c for c, ok in zip("12345", (c1, c2, propre, c4, c5)) if not ok)
    membres.sort()
    X = {}
    for w, src, _, _ in membres:
        if src == "grille":
            s4 = art["m11"]["carte"]["4|%.12f" % w]["sF"]
            s5 = art["m10"]["carte"]["5|%.12f" % w]["sF"]
            s7 = art["m10"]["carte"]["7|%.12f" % w]["sF"]
        else:
            s4, s5, s7 = (art["m12"]["carte"]["%d|%.12f" % (p, w)]["sF"]
                          for p in (4, 5, 7))
        X[w] = x_du_point(s4, s5, s7)
    Fq = [Fraction(round(w * 100), 100) for w, _, _, _ in membres]
    triplets = [(Fq[i], Fq[j], Fq[k])
                for i in range(len(Fq)) for j in range(i + 1, len(Fq))
                for k in range(j + 1, len(Fq)) if Fq[k] - Fq[i] <= LARGEUR_TRIPLET]
    K, realisateurs, table_triplets = {}, {}, []
    for nom in ("E", "S57", "S4"):
        best = None
        for a, b, c in triplets:
            g = (b - a) * (c - b)
            fa, fb, fc = float(a), float(b), float(c)
            res = X[fb][nom] - (X[fa][nom]
                                + (X[fc][nom] - X[fa][nom]) * float((b - a) / (c - a)))
            kloc = abs(res) / float(g)
            if nom == "E":
                table_triplets.append({"triplet": [str(a), str(b), str(c)],
                                       "g_exact": str(g), "res_E": res,
                                       "K_E_local": kloc})
            if best is None or kloc > best[0]:
                best = (kloc, (a, b, c), res)
        K[nom] = best[0]
        realisateurs[nom] = [str(x) for x in best[1]]
    return {"F": [float(q) for q in Fq], "F_cent": [int(q * 100) for q in Fq],
            "assignations_v3": {"%.2f" % w: "%d/%d" % a3
                                for w, _, a3, _ in membres},
            "rejets": rejets, "X": X, "triplets_cent":
                [tuple(int(a * 100) for a in t) for t in triplets],
            "table_triplets": table_triplets, "K": K,
            "realisateurs": realisateurs}


def arret_pre_run(pr):
    """Verrou : la re-derivation doit rendre la consignation pre-run de
    la certification (note 8081a032, section 3). K compares a la
    resolution consignee (6 decimales, tolerance declaree 5e-7)."""
    if tuple(pr["F_cent"]) != ATTENDU_F_CENT:
        sys.exit("ARRET pre-run : F re-derive %r != consignation section 3 %r"
                 % (pr["F_cent"], list(ATTENDU_F_CENT)))
    if tuple(pr["triplets_cent"]) != ATTENDU_TRIPLETS_CENT:
        sys.exit("ARRET pre-run : triplets re-derives != consignation section 3")
    for nom, att in ATTENDU_K_6DEC.items():
        if abs(pr["K"][nom] - float(att)) > TOL_K_REF:
            sys.exit("ARRET pre-run : K_%s = %.9f, consignation %s "
                     "(tolerance declaree %.0e)" % (nom, pr["K"][nom], att, TOL_K_REF))
    return True


# =====================================================================
# S4. CRITERE P-M15a : geometrie des survivants, cordes, residus,
#     planchers PAR POINT (regle 13), barres, clauses, PARTITION D-3.
# =====================================================================

def g_geo(a, b, c):
    return (b - a) * (c - b)             # Fractions


def b_sigma(v, pas_de):
    """B_X du gel : somme ponderee des pas/sF, cloture gauche-droite.
    v = dict p -> (pas_final, sF)."""
    t4 = C_SIGMA[4] * v[4][0] / v[4][1]
    t5 = C_SIGMA[5] * v[5][0] / v[5][1]
    t7 = C_SIGMA[7] * v[7][0] / v[7][1]
    if pas_de == "E":
        return (t4 + t5) + t7
    if pas_de == "S57":
        return t5 + t7
    return t4


def criterer(survivants, X, B, K, largeur_prog=True):
    """Applique P-M15a. survivants : liste triee de w (float centiemes).
    X : w -> {E,S57,S4} ; B : w -> {E,S57,S4} (bruit) ; K : courbures.
    Rend le dossier complet (clauses, verdict, consignations)."""
    fg = sorted(w for w in survivants if w < float(SITE))
    fd = sorted(w for w in survivants if w > float(SITE))
    dossier = {"survivants": survivants, "flanc_gauche": fg, "flanc_droit": fd,
               "plancher_de_comptes": (len(fg) >= 2 and len(fd) >= 2)}
    if not dossier["plancher_de_comptes"]:
        dossier["verdict"] = "NON CONCLUANT DE GEOMETRIE"
        return dossier
    qg = [Fraction(round(w * 100), 100) for w in fg]
    qd = [Fraction(round(w * 100), 100) for w in fd]
    LOINg, LOINd = qg[0], qd[-1]
    PROCHEg, PROCHEd = qg[-1], qd[0]
    interieurs = [q for q in qg + qd if q not in (LOINg, LOINd)]
    n_disc = sum(1 for q in interieurs if q not in (PROCHEg, PROCHEd))
    largeur = PROCHEd - PROCHEg
    dossier.update({"LOIN": [float(LOINg), float(LOINd)],
                    "PROCHE": [float(PROCHEg), float(PROCHEd)],
                    "interieurs": [float(q) for q in interieurs],
                    "n_disc": n_disc,
                    "largeur_centrage": str(largeur),
                    "largeur_centrage_float": float(largeur)})
    wg, wd = float(LOINg), float(LOINd)
    lignes = {}
    for q in interieurs:
        b = float(q)
        t = float((q - LOINg) / (LOINd - LOINg))
        g = float(g_geo(LOINg, q, LOINd))
        rec = {"g_exact": str(g_geo(LOINg, q, LOINd)), "g": g}
        for nom in ("E", "S57", "S4"):
            corde = X[wg][nom] + (X[wd][nom] - X[wg][nom]) * t
            resx = X[b][nom] - corde
            plancher = K[nom] * g
            barre = FACTEUR_BARRE * ((B[wg][nom] + B[wd][nom]) + B[b][nom])
            rec["res_" + nom] = resx
            rec["plancher_" + nom] = plancher
            rec["barre_" + nom] = barre
            rec["seuil_" + nom] = max(plancher, barre)
        # partage par canal (N-8 : couple, somme non exacte, aucune porte)
        r5 = X[b]["c5"] - (X[wg]["c5"] + (X[wd]["c5"] - X[wg]["c5"]) * t)
        r7 = X[b]["c7"] - (X[wg]["c7"] + (X[wd]["c7"] - X[wg]["c7"]) * t)
        rec["partage_S57"] = {
            "canal5": r5, "canal7": r7,
            "somme_moins_res_S57": (r5 + r7) - rec["res_S57"],
            "note": "couple par canal (N-8) : la somme n'egale pas res_S57 "
                    "au bit, declare, AUCUNE porte ne les compare"}
        lignes["%.2f" % b] = rec
    dossier["interieurs_detail"] = lignes
    xM_cle = max(lignes, key=lambda c: abs(lignes[c]["res_E"]))
    xM = lignes[xM_cle]
    dossier["x_M"] = float(xM_cle)
    C1 = abs(xM["res_E"]) > xM["seuil_E"]
    C2 = float(xM_cle) in (float(PROCHEg), float(PROCHEd))
    C3 = abs(xM["res_S57"]) > xM["seuil_S57"]
    C4 = abs(xM["res_S4"]) > xM["seuil_S4"]
    dossier["clauses"] = {"C1": C1, "C2": C2, "C3": C3,
                          "C4_res_S4_sur_seuil4": C4, "n_disc_ge_1": n_disc >= 1}
    dossier["verdict"] = brancher(C1, C2, C3, n_disc >= 1, C4)
    if dossier["verdict"] in ("STRUCTURE-AU-SITE-RESOLUE",
                              "STRUCTURE-RESOLUE-CENTRAGE-NON-DISCRIMINE"):
        rg = lignes.get("%.2f" % float(PROCHEg))
        rd = lignes.get("%.2f" % float(PROCHEd))
        if rg and rd:
            sg, sd = rg["res_E"] > 0, rd["res_E"] > 0
            dossier["forme"] = ("V-BOSSE" if sg and sd else
                                "V-CREUX" if (not sg and not sd) else "FALAISE")
            dossier["forme_signes_PROCHE"] = [rg["res_E"], rd["res_E"]]
        else:
            dossier["forme"] = "NON DERIVABLE (PROCHE == LOIN a 2+2)"
    return dossier


def brancher(C1, C2, C3, nd, C4):
    """Partition D-3 : exclusive et exhaustive sous plancher atteint."""
    if not C1:
        return "PAS-DE-STRUCTURE-RESOLUE"
    if not C2:
        return "STRUCTURE-NON-CENTREE"
    if C3:
        return ("STRUCTURE-AU-SITE-RESOLUE" if nd
                else "STRUCTURE-RESOLUE-CENTRAGE-NON-DISCRIMINE")
    return ("STRUCTURE-CANAL-4-CANDIDATE" if C4
            else "STRUCTURE-RESOLUE-NON-ATTRIBUEE")


# =====================================================================
# S5. P-M15b -- SEUIL DERIVE DU FOND (D-4, option A) : queue binomiale
#     et comparaison a 1/20 en Fraction EXACTE (regle candidate 15).
# =====================================================================

def queue_binomiale(n, k, b):
    """P(X >= k) sous Binomiale(n, b), Fraction exacte."""
    q = 1 - b
    dessous = sum(math.comb(n, i) * b ** i * q ** (n - i) for i in range(k))
    return 1 - dessous


def k_min_derive(n_eff):
    k = 0
    while True:
        k += 1
        if queue_binomiale(n_eff, k, B_FOND) <= ALPHA:
            return k


def compter_signature(res, g8_echec):
    """k et n_eff sur les lignes SIGNEES impaires du programme (unite du
    registre D-4) ; instances consignees avec ratio et resolution (E27).
    Les instances p=4 sont comptees SEPAREMENT (mecanisme distinct
    attendu, delta 48)."""
    inst, inst4, n_eff = [], [], 0
    for p in DEGRES:
        for w in POINTS:
            for sgn, k in plan_signes(p, w, g8_echec):
                bal = res["resultats"]["G6"].get("%d|%.12f|%+d" % (p, w, sgn))
                if bal is None:
                    continue
                sref = res["resultats"]["carte"]["%d|%.12f" % (p, w)][k]["s"]
                if p in (5, 7):
                    n_eff += 1
                s_exp = bal.get("explosion_sous_LO0_0.90s")
                if s_exp is None:
                    continue
                fiche = {"ligne": "%d|%.2f|%+d" % (p, w, sgn),
                         "s_explosion": s_exp,
                         "ratio_s_explosion_sur_s": (s_exp / sref if sref else None),
                         "pas_eff_gros_rel": bal.get("pas_eff_gros_rel"),
                         "fenetre": "GROSSIERE [LO0, 0.90 s*]",
                         "fine_vide_de_sous_seuil": bal.get("explosion_sous_0.98s") is None,
                         "exclue": bool(bal.get("exclue"))}
                (inst if p in (5, 7) else inst4).append(fiche)
    k_obs = len(inst)
    kmin = k_min_derive(n_eff) if n_eff else None
    p_fond = float(queue_binomiale(n_eff, k_obs, B_FOND)) if n_eff else None
    verdict = ("SIGNATURE PRESENTE" if (kmin is not None and k_obs >= kmin)
               else "SIGNATURE NON RESOLUE")
    return {"k": k_obs, "n_eff": n_eff, "k_min": kmin,
            "P_fond_ge_k": p_fond, "b_fond": str(B_FOND),
            "instances_impaires": inst, "instances_p4": inst4,
            "verdict": verdict,
            "note": "une instance sous k_min est une CONSIGNATION, pas un "
                    "verdict ; aucune branche SIGNATURE ABSENTE (gel v3)"}


def verdict_p_m15c(dossier_a, sig, res, g8_echec):
    """Branche de lecture pre-ecrite : les morts au site."""
    if dossier_a["plancher_de_comptes"]:
        return None
    perdues_mordues = []
    for p in (7, 5):
        for w in POINTS:
            for sgn, k in plan_signes(p, w, g8_echec):
                c = "%d|%.12f" % (p, w)
                if c in res["meta"]["exclusions"]:
                    bal = res["resultats"]["G6"].get(c + "|%+d" % sgn)
                    if bal is not None and bal.get("explosion_sous_LO0_0.90s") is not None:
                        perdues_mordues.append("%d|%.2f|%+d" % (p, w, sgn))
    if perdues_mordues:
        return {"verdict": "NON-CONCLUANT-(i)-PAR-SIGNATURE",
                "lignes_perdues_mordues": perdues_mordues,
                "lecture": "la signature sous-seuil au site est assez forte "
                           "pour tuer la mesure de E -- compatible avec un "
                           "rang (3,1) actif SOUS le seuil ; ceci NE mesure "
                           "PAS E et NE prononce RIEN sur l'etage B (gel v3)"}
    return {"verdict": "NON CONCLUANT DE GEOMETRIE",
            "lignes_perdues_mordues": []}


# =====================================================================
# S6. G8b STRUCTUREL (gel v3 : exposant pair -> force IMPAIRE, test
#     d'explosion symetrique, SUR LA SOURCE du moteur). Le gradient est
#     REEL meme en pre-vol (seuls chercher_seuil/integrer sont
#     substitues) : le test vaut dans les deux modes.
# =====================================================================

def _bloc_fonction(texte, nom):
    """Ancrage par STRUCTURE (regle 12) : bloc de la fonction top-level,
    du def au def suivant, dans le fichier VERIFIE c8ed357b."""
    i = texte.index("def %s(" % nom)
    j = texte.find("\ndef ", i)
    return texte[i:] if j < 0 else texte[i:j]


def g8b_predicats(bloc_grad, bloc_integrer, p):
    return {"force_somme_puissance": "(x1 + x2) ** (P - 1)" in bloc_grad,
            "exposant_impair_a_p_pair": (p - 1) % 2 == 1,
            "cap_symetrique":
                "np.maximum(np.abs(x1), np.abs(x2)) > CAP" in bloc_integrer}


def g8b_structurel(m9, chemin_moteur):
    """Gel v3 : test STRUCTUREL sur la SOURCE du moteur -- (i) force
    g*(x1+x2)**(P-1), exposant IMPAIR a p pair (4-1 = 3) ; (ii) cap
    d'explosion SYMETRIQUE (valeur absolue). Lu dans le FICHIER (verifie
    par empreinte AVANT toute substitution) : l'attribut integrer du
    module est factice en pre-vol, le fichier ne l'est jamais."""
    texte = open(chemin_moteur, encoding="utf-8").read()
    pred = g8b_predicats(_bloc_fonction(texte, "grad_rapide"),
                         _bloc_fonction(texte, "integrer"), 4)
    p_avant = getattr(m9, "P", None)
    m9.P = 4
    rng = np.random.default_rng(20260808)
    x1 = rng.uniform(-2, 2, 2048)
    x2 = rng.uniform(-2, 2, 2048)
    a1, a2 = m9.grad_rapide(x1, x2, m9.G_REF)
    b1, b2 = m9.grad_rapide(-x1, -x2, m9.G_REF)
    if p_avant is not None:
        m9.P = p_avant
    parite_info = bool(np.array_equal(b1, -a1) and np.array_equal(b2, -a2))
    ok = all(pred.values())
    return {"predicats_source": pred,
            "parite_bit_du_champ_x_aleatoires": parite_info,
            "parite_bit_note": "INFORMATION, aucune porte : pow n'est pas "
                "symetrique a la negation au dernier ulp ; la preuve M11 "
                "porte sur la STRUCTURE (negation exacte de l'entree, "
                "exposant impair, cap symetrique) et la parite OPPOSABLE "
                "des seuils est MESUREE par G8a et les masques a 2.62",
            "verdict": "PASSE" if ok else "ECHEC",
            "note": "ancrage par bloc de fonction du fichier c8ed357b "
                    "(regle 12), pas de sous-chaine nue sur le fichier"}


# =====================================================================
# S7. PRE-VOL : moteur factice + SCENARIOS QUI TUENT (cert. gel v3,
#     ITEM 5 temps 2 ; deux precedents de banc degenere payes le 02/08).
#     Valeurs SYNTHETIQUES lisses, AUCUNE prediction de classe ;
#     asymetries de signe REELLES a p impair (parade du montage
#     degenere) ; p=4 identique au bit SAUF scenario B.
# =====================================================================

SCENARIOS_PREVOL = {
    "A": {"morts": {(5, 2.64, -1): "fine_sous"},
          "attend": "perte G7 simple ; plancher atteint ; G2 joue"},
    "B": {"morts": {}, "g8_casse": True,
          "attend": "G8a ECHEC -> convention (f) integrale p=4 (+5), "
                    "comptes derives 43/36"},
    "C": {"morts": {(7, 2.64, +1): "fine_sous", (5, 2.71, -1): "fine_sous"},
          "attend": "configuration 2+2 exacte ; n_disc = 0 ; largeur "
                    "consignee"},
    "D": {"morts": {(7, 2.69, +1): "gros", (5, 2.71, -1): "fine_sous"},
          "attend": "plancher manque + grossiere mordue sur ligne perdue "
                    "-> NON-CONCLUANT-(i)-PAR-SIGNATURE ; k >= 1"},
    "E": {"morts": {(5, 2.69, +1): "fine_sous", (7, 2.71, -1): "fine_sous",
                    (5, 2.73, +1): "fine_sous"},
          "attend": "flanc droit sans survivant -> G2 SAUTEE (N-14), "
                    "recherches jouees 37 ; NON CONCLUANT DE GEOMETRIE"},
}


def fabriquer_factice_m15(cible_g1p, scenario):
    sc = SCENARIOS_PREVOL[scenario]
    base = {7: 1.35, 5: 1.95, 4: 6.80}
    asym = {7: 1.006, 5: 1.004, 4: 1.0}

    def s_de(p, w, sgn):
        if abs(w - G1P_POINT) < 1e-9:
            return cible_g1p[(p, sgn)]
        s = base[p] * (1.0 + 0.05 * (w - 2.60))
        if sgn < 0:
            s *= asym[p]
        if sc.get("g8_casse") and p == 4 and sgn < 0:
            s = math.nextafter(s, math.inf)
        return s

    module = {"m": None}

    def chercher(w2, sgn=1, dt=None, g=None):
        m = module["m"]
        s = s_de(m.P, w2, sgn)
        if g is not None and abs(g - m.G_REF) > 0:
            s *= (m.G_REF / g) ** (1.0 / (m.P - 2))   # K-invariance exacte
        return s, "OK|pas=6.03e-07"

    def integrer(w2, s_arr, sgn=1, dt=None, g=None):
        m = module["m"]
        th = s_de(m.P, w2, sgn)
        mode = sc["morts"].get((m.P, round(w2, 2), sgn))
        seuil = {"gros": 0.60, "fine_sous": 0.95}.get(mode, 1.0) * th
        return np.asarray(s_arr, float) >= seuil
    return {"chercher": chercher, "integrer": integrer, "module": module}


def charger_cible_g1p(prevol, rep_prevol, art):
    """Cinq lignes de 2.72 depuis fa109da9 (REEL : conforme exige ;
    PREVOL : reel si conforme, sinon synthetique avec banniere)."""
    c = art["m12"]["carte"]
    cible, meta = {}, {"source": "m12_results.json", "sha256_attendu": SHA_M12_JSON}
    for p, sgn, k in ((4, +1, "sP"), (5, +1, "sP"), (5, -1, "sM"),
                      (7, +1, "sP"), (7, -1, "sM")):
        v = c["%d|%.12f" % (p, G1P_POINT)][k]
        if v is None or v.get("s") is None:
            sys.exit("ARRET : reference G1' incomplete dans fa109da9 (%d|%+d)" % (p, sgn))
        cible[(p, sgn)] = float(v["s"])
    return cible, meta


# =====================================================================
# S8. ASSEMBLAGE DE LIGNE (convention (f) ; p=4 a cote unique sous
#     condition G8a/G8b -- gel v3, P-M12e) et VERIFICATION G1'.
# =====================================================================

def assembler_ligne_m15(p, w, v):
    if "sM" in v:
        sP, sM = v["sP"], v["sM"]
        if sP["recevable"] and sM["recevable"]:
            v["sF"] = min(sP["s"], sM["s"])
            v["frag"] = 1 if sP["s"] <= sM["s"] else -1
            v["asym"] = sP["s"] / sM["s"]
        else:
            motif = sP["motif_exclusion"] or sM["motif_exclusion"] or "non recevable"
            v["sF"] = None; v["sF_motif"] = motif
            v["frag"] = None; v["frag_motif"] = motif
            v["asym"] = None; v["asym_motif"] = motif
    else:
        sP = v["sP"]
        if sP["recevable"]:
            v["sF"] = sP["s"]; v["frag"] = 1
        else:
            v["sF"] = None; v["sF_motif"] = sP["motif_exclusion"]
            v["frag"] = None; v["frag_motif"] = sP["motif_exclusion"]
        v["asym"] = None
        v["asym_motif"] = "cote unique (parite demontree, G8a/G8b -- gel v3)"


def verifier_g1p(mesure, cible):
    ec = (mesure["s"] - cible) if mesure["s"] is not None else None
    return {"mesure": mesure, "cible": cible, "ecart_absolu": ec,
            "verdict": "PASSE" if ec == 0.0 else "ECHEC"}


def verifier_scenario(sc, res, dossier, sig, cverdict, g8_echec, P):
    """BANC QUI TUE : chaque scenario ASSERT la branche qu'il pretend
    traverser -- un pre-vol qui ne tue pas est un banc degenere."""
    if sc == "A":
        assert "5|%.12f" % 2.64 in res["meta"]["exclusions"], "A: perte absente"
        assert dossier["plancher_de_comptes"], "A: plancher devrait tenir"
        assert res["resultats"]["G2"].get("verdict") == "CONSIGNE", "A: G2 non joue"
    elif sc == "B":
        assert g8_echec, "B: G8 aurait du echouer"
        assert P.CPT["recherches"] + P.CPT["sautees"] == rech_attendues(True), \
            "B: comptes non derives sous (f) integrale"
    elif sc == "C":
        assert dossier["plancher_de_comptes"] and dossier["n_disc"] == 0, \
            "C: configuration 2+2 non atteinte"
        assert "largeur_centrage" in dossier, "C: largeur non consignee"
    elif sc == "D":
        assert cverdict and cverdict["verdict"] == "NON-CONCLUANT-(i)-PAR-SIGNATURE", \
            "D: branche P-M15c-signature non atteinte"
        assert sig["k"] >= 1, "D: aucune grossiere mordue comptee"
    elif sc == "E":
        assert res["resultats"]["G2"].get("verdict") == "SAUTEE", "E: G2 non sautee"
        assert cverdict and cverdict["verdict"] == "NON CONCLUANT DE GEOMETRIE", \
            "E: geometrie aurait du manquer sans signature"
    print("PREVOL scenario %s : branche attendue TRAVERSEE -- %s"
          % (sc, SCENARIOS_PREVOL[sc]["attend"]))


# =====================================================================
# S9. MAIN
# =====================================================================

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--prevol", action="store_true")
    ap.add_argument("--scenario", default="A", choices=sorted(SCENARIOS_PREVOL))
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
    art, meta_art = charger_artefacts(a.prevol, a.sources_prevol)

    # ---- PRE-RUN (ITEM 6) : re-derivation + ARRET section 3 -----------
    pre = derive_pre_run(art)
    arret_pre_run(pre)
    print("Pre-run : F (|F| = %d), 8 triplets et K_X re-derives ==" % len(pre["F"]))
    print("  consignation pre-run de la certification (note %s...) ; ARRET arme."
          % SHA_NOTE_CERT_V3[:8])
    K = pre["K"]

    cible_g1p, meta_g1p = charger_cible_g1p(a.prevol, a.sources_prevol, art)
    factice = fabriquer_factice_m15(cible_g1p, a.scenario) if a.prevol else None
    m9 = P.charger_moteur(a.moteur, factice=factice)

    for w in POINTS:
        if not est_centieme(w):
            sys.exit("ARRET rule-11 : %r n'est pas un centieme exact" % w)
    if min(abs(G1P_POINT - float(k.split("|")[1]))
           for k in art["m12"]["carte"]) > TOL_APPART:
        sys.exit("ARRET rule-11 : ancre G1' hors de la carte m12")
    print("rule-11 : six points du programme en centiemes exacts ; ancre G1'")
    print("  sur la carte m12 a 1e-9. Le programme est NEUF par valeur (ITEM 2).")

    g8s = g8b_structurel(m9, a.moteur)
    g8_echec = (g8s["verdict"] == "ECHEC")
    if g8_echec:
        print("G8b STRUCTUREL : ECHEC -- retour convention (f) integrale a p=4.")

    res = {"meta": {"gel_sha256_bloc": hgel, "pilote_sha256": SHA_PILOTE,
                    "moteur_sha256": SHA_MOTEUR, "artefacts": meta_art,
                    "cible_g1p": meta_g1p, "mode": mode,
                    "reference_pre_run": {
                        "note_certification_v3": SHA_NOTE_CERT_V3,
                        "role": "ARRET seulement -- les valeurs UTILISEES "
                                "sont re-derivees des artefacts (ITEM 6)"},
                    "convention_empreinte": "B -- bloc saut final inclus = fichier",
                    "declarations": {
                        "N-13": "assignation R-2' = argmin de la marge "
                                "NORMALISEE d/rayon (gel v3) ; la lecture "
                                "ABSOLUE (cert. v2) differe sur 6 points de "
                                "F, meme ensemble F",
                        "N-14": "flanc droit sans survivant -> G2 SAUTEE "
                                "avec motif, recherches jouees = 37",
                        "N-15": "resolution de la manche chiffree note "
                                "8081a032 section 5 ; planchers PAR POINT "
                                "consignes ici (pre_run + P_M15a)",
                        "G8b": "test STRUCTUREL sur la source du moteur "
                               "(gel v3) ; la comparaison de masques de la "
                               "lignee est consignee en plus, SANS porte",
                        "P-M15b_unite": "ligne SIGNEE impaire du programme "
                               "(unite du registre D-4, denominateur 96)"},
                    "G3_par_degre": [], "gardes": [], "exclusions": {}},
           "resultats": {"carte": {}, "G6": {}, "G8": {"structurel": g8s},
                         "G2": {}, "G4": {}, "G1p": {}, "pre_run": {},
                         "P_M15a": {}, "P_M15b": {}},
           "verdict": {}, "resume": {}}
    res["resultats"]["pre_run"] = {
        "K": {k: K[k] for k in K}, "realisateurs": pre["realisateurs"],
        "F": pre["F"], "assignations_v3": pre["assignations_v3"],
        "rejets_F": pre["rejets"], "triplets": pre["table_triplets"]}
    jg3 = res["meta"]["G3_par_degre"]
    carte = res["resultats"]["carte"]
    excl = res["meta"]["exclusions"]
    if a.prevol:
        res["meta"]["prevol_scenario"] = {"id": a.scenario,
                                          **SCENARIOS_PREVOL[a.scenario]}
        res["meta"]["prevol_scenario"].pop("morts", None)

    def sauve():
        P.sauver(res, fout)

    # ---- G1' D'ABORD (bloquante, 5 recherches) ------------------------
    print("\n--- G1' custody : rejeu au bit des 5 lignes de %.2f ---" % G1P_POINT)
    for p in DEGRES:
        P.rebind(m9, p, jg3)
        for sgn in ((+1, -1) if p != 4 else (+1,)):
            r = P.mesurer(m9, G1P_POINT, sgn)
            fiche = verifier_g1p(r, cible_g1p[(p, sgn)])
            res["resultats"]["G1p"]["%d|%+d" % (p, sgn)] = fiche
            sauve()
            if fiche["verdict"] != "PASSE":
                sys.exit("ARRET G1' : ecart %r != 0 en %d|%.2f|%+d -- custody rompue."
                         % (fiche["ecart_absolu"], p, G1P_POINT, sgn))
    print("  ecarts absolus = 0.0 EXACT sur les 5 lignes : custody intacte.")

    # ---- programme : mesures puis balayages, par degre ----------------
    for p in DEGRES:
        print("\n--- degre p = %d ---" % p)
        P.rebind(m9, p, jg3)
        for w in POINTS:
            v = carte.setdefault(P.cle(p, w), {})
            for sgn, k in plan_signes(p, w, g8_echec):
                m = P.mesurer(m9, w, sgn)
                if p == 4 and sgn < 0:
                    m["role"] = ("regression_G8a" if w == G8A_POINT
                                 else "convention_f_integrale (echec G8)")
                v[k] = m
                sauve()
            if p == 4 and w == G8A_POINT and v["sP"]["recevable"] \
                    and v.get("sM", {}).get("recevable"):
                e8 = v["sP"]["s"] - v["sM"]["s"]
                res["resultats"]["G8"]["G8a"] = {
                    "ligne": "4|%.2f" % w, "ecart_absolu": e8,
                    "verdict": "PASSE" if e8 == 0.0 else "ECHEC"}
                if e8 != 0.0 and not g8_echec:
                    g8_echec = True
                    res["meta"]["gardes"].append(
                        "G8a ECHEC (sP - sM = %r) : retour convention (f) "
                        "integrale a p=4, compte attendu mis a jour en forme "
                        "derivee (gel v3)" % e8)
                    print("  G8a ECHEC -> convention (f) integrale a p=4.")
            assembler_ligne_m15(p, w, v)
            if v["sF"] is None:
                excl.setdefault(P.cle(p, w), []).append("G5 : " + v["sF_motif"])
            sauve()
        for w in POINTS:
            v = carte[P.cle(p, w)]
            plan = plan_signes(p, w, g8_echec)
            if not all(v[k]["recevable"] for _, k in plan if k in v):
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
                    res["meta"]["gardes"].append("DOMAINE %s : %s"
                                                 % (P.cle(p, w), motif))
                    sauve()
                    sys.exit("ARRET domaine : " + motif)
                bal = P.balayer(m9, w, sgn, v[k]["s"])
                P.enrichir_g6(bal, v[k]["s"], v[k]["note"])
                if p == 4:
                    bal["g8b_grossier_attendu"] = ("VIDE (pre-declare, lignee "
                                                   "pilote/M12, note ad8dd209)")
                    if bal["gros_explosifs"] > 0:
                        res["meta"]["gardes"].append(
                            "FAIT NEUF : grossiere a MORDU a p=4, w2=%.2f "
                            "sgn=%+d (%d explosif(s))" % (w, sgn, bal["gros_explosifs"]))
                bal["motif_fenetre"] = "voir cles explosion_* (fenetre nommee, D1-1)"
                bg[k] = bal
                res["resultats"]["G6"][P.cle(p, w) + "|%+d" % sgn] = bal
                if bal["exclue"]:
                    fen = ("GROSSIERE" if bal["explosion_sous_LO0_0.90s"] is not None
                           else "FINE")
                    excl.setdefault(P.cle(p, w), []).append(
                        "G6 sgn=%+d explosion sous seuil (fenetre %s)" % (sgn, fen))
            if p == 4 and w == G8A_POINT and "sP" in bg and "sM" in bg:
                res["resultats"]["G8"]["masques_2.62"] = P.g8b(bg["sP"], bg["sM"])
                res["resultats"]["G8"]["masques_2.62"]["statut"] = \
                    "consignation de lignee, SANS porte (G8b v3 = structurel)"
            sauve()
    sauve()

    # ---- G4 : dt/2 sur l'echelle de force maximale --------------------
    print("\n--- G4 : dt/2 sur la ligne maximisant g*s^(p-1) ---")
    best = None
    for p in DEGRES:
        for w in POINTS:
            v = carte[P.cle(p, w)]
            for sgn, k in plan_signes(p, w, g8_echec):
                if k in v and v[k]["recevable"]:
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
                                  "s_dt2": r4["s"], "ecart": ec4,
                                  "verdict": "PASSE" if ok4 else "NON FIABLE"}
        if not ok4:
            excl.setdefault(P.cle(p, w), []).append("G4 NON FIABLE")
    sauve()

    # ---- survivants (G7 : toute exclusion de ligne perd le point) -----
    def point_survivant(w):
        for p in DEGRES:
            c = P.cle(p, w)
            if c in excl or carte[c].get("sF") is None:
                return False
        return True

    survivants = [w for w in POINTS if point_survivant(w)]

    # ---- G2 (D-5, precedent M14 ; N-14) -------------------------------
    print("\n--- G2 invariance (1 recherche a 2g, 7|PROCHE_droit|+1) ---")
    fd_surv = sorted(w for w in survivants if w > float(SITE))
    if not fd_surv:
        P.CPT["sautees"] += 1
        res["resultats"]["G2"] = {
            "verdict": "SAUTEE",
            "motif": "N-14 : flanc droit sans survivant, G2 sans cible ; "
                     "recherches jouees = 37"}
        res["meta"]["gardes"].append("G2 SAUTEE (N-14) : flanc droit vide")
    else:
        cible2 = fd_surv[0]
        base = carte[P.cle(7, cible2)]["sP"]
        P.rebind(m9, 7, jg3)
        r2 = P.mesurer(m9, cible2, +1, g=2 * m9.G_REF)
        if base["recevable"] and r2["recevable"]:
            ratio = 2.0 * (r2["s"] / base["s"]) ** (7 - 2)
            res["resultats"]["G2"] = {
                "ligne": "7|%.2f|+1" % cible2, "g": "2g",
                "mesure": r2, "K2_sur_K1": ratio,
                "ecart_a_1": abs(ratio - 1.0), "verdict": "CONSIGNE",
                "statut": "SANS PORTE (precedent M14, 273d0a53)"}
        else:
            res["resultats"]["G2"] = {
                "ligne": "7|%.2f|+1" % cible2, "mesure": r2,
                "K2_sur_K1": None, "verdict": "CONSIGNE",
                "motif": "base ou 2g non recevable -- consigne, sans porte"}
    sauve()

    # ---- P-M15a -------------------------------------------------------
    print("\n--- P-M15a : critere au site (partition D-3) ---")
    X, B = {}, {}
    for w in survivants:
        sfs, pas = {}, {}
        for p in DEGRES:
            v = carte[P.cle(p, w)]
            sfs[p] = v["sF"]
            cote = "sP" if (p == 4 or v.get("frag") == 1) else "sM"
            pas[p] = (P.pas_final(v[cote]["note"]), v["sF"])
        X[w] = x_du_point(sfs[4], sfs[5], sfs[7])
        B[w] = {nom: b_sigma(pas, nom) for nom in ("E", "S57", "S4")}
    dossier = criterer(survivants, X, B, K)
    res["resultats"]["P_M15a"] = dossier

    # ---- P-M15b -------------------------------------------------------
    sig = compter_signature(res, g8_echec)
    res["resultats"]["P_M15b"] = sig
    print("P-M15b : k = %d / n_eff = %d, k_min = %s -> %s"
          % (sig["k"], sig["n_eff"], sig["k_min"], sig["verdict"]))

    # ---- verdict de manche --------------------------------------------
    cverdict = verdict_p_m15c(dossier, sig, res, g8_echec)
    if cverdict is None:
        verdict = {"P_M15a": dossier["verdict"], "P_M15b": sig["verdict"],
                   "forme": dossier.get("forme"),
                   "x_M": dossier.get("x_M"), "n_disc": dossier.get("n_disc")}
    else:
        verdict = {"manche": cverdict["verdict"],
                   "P_M15b": sig["verdict"], "detail": cverdict}
    if mode == "PREVOL":
        verdict = {("PREVOL_SYNTHETIQUE_" + k): v for k, v in verdict.items()}
        print("=" * 70)
        print("PREVOL : le 'verdict' ci-dessous est SYNTHETIQUE -- AUCUNE PHYSIQUE.")
        print("=" * 70)
    res["verdict"] = verdict

    # ---- resume, comptes (forme derivee), couverture ------------------
    ventil = {g: sum(1 for ms in excl.values() if any(s.startswith(g) for s in ms))
              for g in ("G4", "G5", "G6")}
    res["resume"] = {
        "survivants": survivants, "points_perdus": sorted(excl),
        "pertes_par_mecanisme": ventil,
        "pertes_note": "ventilation par MECANISME, pas une partition",
        "g8_echec": g8_echec}
    dtmod = __import__("datetime")
    res["meta"]["date_utc"] = dtmod.datetime.now(dtmod.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")
    res["meta"]["forme_canonique"] = ("LF, labels normalises, date omise -- "
                                      "la date ci-dessus est HORS bloc canonique")
    res["meta"]["script_sha256"] = _sha(os.path.abspath(__file__))
    att_r = rech_attendues(g8_echec)
    att_b = bal_attendus(g8_echec)
    res["meta"]["recherches"] = {"comptees": P.CPT["recherches"],
                                 "sautees": P.CPT["sautees"], "attendues": att_r,
                                 "derivation": "31 + 5*g8_echec (programme) + "
                                               "5 (G1') + 1 (G4) + 1 (G2 joue "
                                               "ou saute, N-14)"}
    res["meta"]["balayages"] = {"comptes": P.CPT["balayages"],
                                "sautes": P.CPT["balayages_sautes"],
                                "attendus": att_b}
    for c, v in carte.items():
        for champ in ("sP", "sF", "frag", "asym"):
            if champ not in v:
                sys.exit("ARRET couverture : %s sans champ %s" % (c, champ))
    sauve()
    if P.CPT["recherches"] + P.CPT["sautees"] != att_r:
        sys.exit("ARRET : %d + %d recherches != %d (forme derivee)"
                 % (P.CPT["recherches"], P.CPT["sautees"], att_r))
    if P.CPT["balayages"] + P.CPT["balayages_sautes"] != att_b:
        sys.exit("ARRET : %d + %d balayages != %d"
                 % (P.CPT["balayages"], P.CPT["balayages_sautes"], att_b))
    if a.prevol:
        verifier_scenario(a.scenario, res, dossier, sig, cverdict, g8_echec, P)
    print("\nEcrit : %s" % fout)
    print("Recherches : %d + %d = %d / %d | balayages : %d + %d = %d / %d"
          % (P.CPT["recherches"], P.CPT["sautees"],
             P.CPT["recherches"] + P.CPT["sautees"], att_r,
             P.CPT["balayages"], P.CPT["balayages_sautes"],
             P.CPT["balayages"] + P.CPT["balayages_sautes"], att_b))
    print("sha256 du JSON : %s" % _sha(fout))


# =====================================================================
# S10. SELFTEST -- ce que le script CALCULE (le pre-vol verifie ce
#      qu'il FAIT ; les deux ne sont pas interchangeables).
# =====================================================================

def selftest():
    from itertools import product
    ok = True

    # [1] gel jumeau
    certifier_gel(verbeux=False)
    print("[1] gel jumeau e41f4da3 : CONCORDANT")

    # [2] partition D-3 : 32 combinaisons -> 1 branche, 6 atteintes
    vus = set()
    for c1, c2, c3, nd, c4 in product((False, True), repeat=5):
        v = brancher(c1, c2, c3, nd, c4)
        assert v in VERDICTS_A, v
        vus.add(v)
    assert vus == set(VERDICTS_A), "branches non atteintes : %r" % (set(VERDICTS_A) - vus)
    print("[2] partition : 32 combinaisons, 6 branches atteintes, exclusives")

    # [3] la branche 2+2 MORD (D-2) : extremum au PROCHE, C1^C2^C3 vrais,
    #     n_disc = 0 -> CENTRAGE-NON-DISCRIMINE, jamais AU-SITE
    surv = [2.62, 2.65, 2.69, 2.73]
    Xs = {}
    for w in surv:
        lin = 0.1 * (w - 2.62)
        bump_E = 0.5 if w == 2.65 else 0.0
        bump_S = 0.4 if w == 2.65 else 0.0
        Xs[w] = {"E": lin + bump_E, "S57": lin + bump_S, "S4": lin,
                 "c5": lin + bump_S, "c7": 0.0}
    Bs = {w: {"E": 1e-6, "S57": 1e-6, "S4": 1e-6} for w in surv}
    Ks = {"E": 27.088, "S57": 21.714, "S4": 5.836}
    d = criterer(surv, Xs, Bs, Ks)
    assert d["plancher_de_comptes"] and d["n_disc"] == 0
    assert d["clauses"]["C1"] and d["clauses"]["C2"] and d["clauses"]["C3"]
    assert d["verdict"] == "STRUCTURE-RESOLUE-CENTRAGE-NON-DISCRIMINE"
    assert d["verdict"] != "STRUCTURE-AU-SITE-RESOLUE"
    assert d["largeur_centrage"] == "1/25"      # 2.69 - 2.65 exact
    print("[3] 2+2 : CENTRAGE-NON-DISCRIMINE atteint, AU-SITE interdit, "
          "largeur consignee")

    # [4] D-4 en Fraction exacte : k_min(24) = 3, queues opposables
    q3 = queue_binomiale(24, 3, B_FOND)
    q2 = queue_binomiale(24, 2, B_FOND)
    assert isinstance(q3, Fraction) and isinstance(q2, Fraction)
    assert q3 <= ALPHA < q2, (float(q3), float(q2))
    assert k_min_derive(24) == 3
    q1 = queue_binomiale(24, 1, B_FOND)
    assert q1 > Fraction(46, 100)               # P(k>=1) = 0.5333... : pas de
    print("[4] k_min(24) = 3 exact ; P(k>=1) = %.4f -- branche ABSENTE "
          "impossible (gel v3)" % float(q1))

    # [5] N-13 : assignations v3 gelees (vecteurs de la note 8081a032)
    attendu = {1.73: (3, 2), 1.76: (2, 1), 2.27: (2, 1),
               2.30: (2, 1), 2.60: (3, 1), 2.75: (3, 1)}
    for w, a in attendu.items():
        pr, a3, marge = analyse_r2p(w)
        assert pr and a3 == a, (w, a3)
    assert analyse_r2p(1.70)[2] == Fraction(1, 3000)
    print("[5] N-13 : six assignations v3 reproduites ; marge de 1.70 = "
          "1/3000 EXACTE ; 2.60 -> 3/1 par bris d'egalite")

    # [6] VERROUS QUI MORDENT
    bloc, h = certifier_gel(verbeux=False)
    casse = bloc[:100] + chr(ord(bloc[100]) ^ 1) + bloc[101:]
    assert hashlib.sha256(casse.encode()).hexdigest() != SHA_GEL
    pr_ok = {"F_cent": list(ATTENDU_F_CENT),
             "triplets_cent": [tuple(t) for t in ATTENDU_TRIPLETS_CENT],
             "K": {k: float(v) + 4e-7 for k, v in ATTENDU_K_6DEC.items()}}
    assert arret_pre_run(pr_ok) is True
    pr_ko = dict(pr_ok)
    pr_ko["K"] = {k: float(v) + 6e-7 for k, v in ATTENDU_K_6DEC.items()}
    try:
        arret_pre_run(pr_ko)
        ok = False
        print("  ECHEC : l'arret pre-run n'a pas mordu sur +6e-7")
    except SystemExit:
        pass
    m_ok = {"s": 1.25, "note": "OK|pas=6.03e-07"}
    assert verifier_g1p(m_ok, 1.25)["verdict"] == "PASSE"
    assert verifier_g1p({"s": math.nextafter(1.25, 2.0), "note": ""},
                        1.25)["verdict"] == "ECHEC"
    print("[6] verrous : octet altere -> sha discordant ; K +6e-7 -> ARRET "
          "(+4e-7 passe, tolerance declaree) ; G1' nextafter -> ECHEC")

    # [6c] temoin de bande D-3 embarque (note 8081a032, section 2) :
    #      res_S4 = seuil4 EXACTEMENT -> C4 strict FAUX -> NON-ATTRIBUEE
    v = brancher(True, True, False, True, 0.0163 > 0.0163)
    assert v == "STRUCTURE-RESOLUE-NON-ATTRIBUEE"
    print("[6c] temoin de bande : 0.0163 > 0.0163 est FAUX (strict) -> "
          "NON-ATTRIBUEE, frontiere du trou de partition exhibee")

    # [7] N-8 : clotures -- E et S4+S57 different, borne petite, sans porte
    for s4, s5, s7 in ((2.0055, 0.2780, 1.2971), (6.83, 1.351, 1.9617)):
        x = x_du_point(s4, s5, s7)
        assert abs(x["E"] - (x["S4"] + x["S57"])) <= 1e-15
        assert abs((x["c5"] + x["c7"]) - x["S57"]) <= 1e-15
    print("[7] N-8 : ecart de cloture <= 1e-15, declare, aucune porte")

    # [8] aiguille structurelle -- sur le CORPS seulement : le gel NOMME
    #     l'appel interdit en prose (garde structurelle, ligne 528) et une
    #     aiguille litterale se trouve (lecon M10, 10 instances)
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    fin_gel = src.index(MARQ_FIN) + len(MARQ_FIN) + 1
    assert ("utc" + "now(") not in src[fin_gel:]
    print("[8] aiguille : l'appel interdit est ABSENT du corps (le gel le "
          "nomme en prose -- teste hors bloc)")

    # [9] comptes en forme derivee
    assert rech_attendues(False) == 38 and rech_attendues(True) == 43
    assert bal_attendus(False) == 31 and bal_attendus(True) == 36
    assert len(plan_signes(4, G8A_POINT, False)) == 2
    assert len(plan_signes(4, 2.64, False)) == 1
    assert len(plan_signes(4, 2.64, True)) == 2
    assert all(len(plan_signes(p, w, False)) == 2
               for p in (5, 7) for w in POINTS)
    print("[9] comptes : 38/43 recherches, 31/36 balayages, plans conformes")

    # [10] factice : parade du montage degenere
    from types import SimpleNamespace
    cible = {(p, sgn): 1.0 + 0.1 * p + 0.001 * sgn
             for p in DEGRES for sgn in (+1, -1)}
    fA = fabriquer_factice_m15(cible, "A")
    fA["module"]["m"] = SimpleNamespace(P=5, G_REF=0.05)
    sP1, _ = fA["chercher"](2.64, +1)
    sM1, _ = fA["chercher"](2.64, -1)
    assert sP1 != sM1, "montage degenere : sP == sM a p impair"
    fA["module"]["m"].P = 4
    s4p, _ = fA["chercher"](2.64, +1)
    s4m, _ = fA["chercher"](2.64, -1)
    assert s4p == s4m
    fB = fabriquer_factice_m15(cible, "B")
    fB["module"]["m"] = SimpleNamespace(P=4, G_REF=0.05)
    b4p, _ = fB["chercher"](2.64, +1)
    b4m, _ = fB["chercher"](2.64, -1)
    assert b4p != b4m, "scenario B : G8 devrait casser"
    s2g, _ = fA["chercher"](2.64, +1, g=0.10)
    fA["module"]["m"].P = 7
    s1g, _ = fA["chercher"](2.64, +1)
    s2g7, _ = fA["chercher"](2.64, +1, g=0.10)
    assert abs(2.0 * (s2g7 / s1g) ** 5 - 1.0) < 1e-12, "K-invariance factice"
    print("[10] factice : asymetrie reelle a p impair, p=4 identique (A), "
          "casse (B), K-invariance exacte a 2g")

    # [11] G8b structurel : les predicats MORDENT sur une source alteree
    bon = g8b_predicats("def grad_rapide(x1, x2, g):\n"
                        "    base = g * (x1 + x2) ** (P - 1)\n",
                        "    bad = np.maximum(np.abs(x1), np.abs(x2)) > CAP\n", 4)
    assert all(bon.values()), bon
    mauvais = g8b_predicats("base = g * (x1 + x2) ** (P - 2)", "x1 > CAP", 4)
    assert not mauvais["force_somme_puissance"]
    assert not mauvais["cap_symetrique"]
    assert g8b_predicats("", "", 5)["exposant_impair_a_p_pair"] is False
    print("[11] G8b : predicats structurels vrais sur la forme attendue, "
          "FAUX sur exposant P-2, cap asymetrique, degre impair")

    print("\nSELFTEST : %s" % ("PASSE" if ok else "ECHEC"))
    return 0 if ok else 1


if __name__ == "__main__":
    main()
