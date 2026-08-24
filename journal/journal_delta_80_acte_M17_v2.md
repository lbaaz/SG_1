JOURNAL DELTA 80 -- L'ACTE DE LA JOURNEE M17 : E19 CONSIGNE AVEC SON
RETARD, QUATRE ERRATA (E33..E36), SIX DEFAUTS DE CUSTODY (D-M17-26..31),
TROIS BLOQUANTS OUVERTS, DEUX RESOLUTIONS E15, DEUX REGLES (N-61, N-62)
(redaction machine 1, depot operateur, 2026-08-24) -- VERSION 2
=======================================================================
Repond a : note_machine2_certification_delta_80_v1.md 2761c0631ae9a558
(copie recue machine 1 ; a re-deriver du disque machine 2 au depot).
Remplace le brouillon v1 90f7e33cc10a4b12 (non edite). Leves ici :
B-1 (detenteur du bilan v2 declare, piece jointe au depot) ; D-80-1
(la replication inventee retiree) ; D-80-2 (E34 fonde sur l'instrument
sonde_EA livre par machine 2, cite par ses lignes) ; D-80-3 (le couple
de D-F1 cite avec point ET lecture) ; D-80-4 (l'ecart de doublement
cite avec son M) ; reserve de 80.6 (aucune precaution attribuee qui
n'a pas ete prise). Contresignes par anticipation a la certification :
80.1, 80.6 (reformule), 80.7 (sous reserve D-80-1, levee), 80.8,
80.10, 80.11.
S'insere apres le delta 79 (a5175671f93dfaf9). Numero pris A L'ACTE au
depot, sous la regle 66.5.c. Acte de CLASSE B (delta 71) : les pieces
deposees ARMENT des regles et des errata.
Files verifiees avant prise (E18 : jamais de reservation) :
  errata : libre au-dela de E32 (delta 79, "n'attribue aucun autre
    numero" ; note rectification 2fa620dca9cbf0d0, statut) ;
  regles N : libre au-dela de N-60 (derniere citee, note rectification
    section 5) ;
  defauts D-M17 : file consommee jusqu'a 25 (acte de certification du
    gel, note m2 v10, section 1 "D-M17-25 LEVE" ; journal du gel v9,
    section 13). Voir 80.6 pour la resolution de collision.

80.1 E19 -- ARME LE 23/08, CONSIGNE ICI AVEC SON RETARD (N-47, CLASSE B)
  L'empreinte de gel de la manche M17 est a5e86ca3191fb204 (39686 o,
  m17_pre_enregistrement_quantique_v9.md, CERTIFIE par l'acte du 23/08,
  note m2 v10). A compter de cet armement, aucun run n'est opposable
  dont le script ne cite pas cette empreinte dans une certification
  croisee anterieure a son depot.
  RETARD DECLARE : l'armement date du 23/08, la consignation au
  registre date du present delta (24/08). Motif : la fenetre a ete
  consommee par la chaine de l'instrument -- relecture v1..v8 (sept
  defauts D-S), pre-vol N-58 (D-P0..D-P3), banc lourd, rectification de
  custody. Le registre recoit l'armement, il ne le cree pas (N-47).
  ETAT VERIFIE : aucune version du script (v1 d3291b34d0692c5b ..
  v8 a25619c412c93fd9) ne cite l'empreinte ; pre-vol v2, log l.7 :
  "la source cite-t-elle l'empreinte du gel ... False".

80.2 E33 -- ERRATUM Q1 : FRACTION DE LA SERIE P6 (gel 4.11-bis)
  TEXTE : la serie P6 (rangs Gamma_LS contre -Lambda_c, et l'exces
  H - H+) s'evalue a la fraction 0.70 de s*_ff.
  FONDEMENT : le gel nomme deja 0.70 trois fois (temoin S-G, bloc P8
  4.11, chemin (b) du pilote 11.4) ; a 0.70 la barriere nominale compte
  7 sites (Lambda_c a de la dynamique), pres de 1.00 elle s'effondre
  (D-F1, 80.9) et les rangs seraient du bruit. Arbitrage machine 2
  (note relecture script v1), constate au banc.
  EFFET SCRIPT : cle Q1_fraction_P6 = "E33" a la contre-certification.

80.3 E34 -- ERRATUM Q2 : STATIONNARITE eta DE Gamma_c (gel 4.7)
  TEXTE : "double aux stationnarites" devient "MOITIE aux
  stationnarites" -- eta_c initial |delta_des|, divise par deux a
  chaque pas jusqu'a pas <= tau_M, budget 8 pas, chaine M x4. Sont
  consignes : eta final, Gamma_c, extrapolation de Richardson, et le
  RESIDU estime par le ratio mesure r (residu = pas x r/(1-r)) -- la
  regle d'arret borne le pas, le residu se DECLARE. La clause litterale
  est conservee en TEMOIN nomme (Gamma_c_temoin_clause_4_7), non
  operatif.
  FONDEMENT MESURE, PORTE PAR L'INSTRUMENT sonde_EA_m17_machine2_v1
  (.py 4a34845cbceaea2a, .log 34cb371dc050cb6e, detenteur machine 2,
  lignes relevees a la certification) : reference 7.703743e-09 (log
  l.13) ; le doublement DIVERGE, 7.2442 -> 26.50 -> 33.99 % (l.17-21),
  ecart cite A SON M -- 7.2442 % a M >= 30 (M_facteur >= 2, identique a
  10 chiffres de M = 30 a M = 60, l.36-38) ; 7.8046 % au M_facteur par
  defaut (M = 15), NON converge -- c'est la valeur du temoin publie par
  le banc leger (0.078). La descente converge : 9.26 -> 7.76 -> 3.32 ->
  1.40 -> 0.65 %, premier pas sous tau_M a eta = |delta|/16, residu
  declare 1.20 %, Richardson 6.067503e-09. Une grandeur se cite avec la
  condition qui la produit -- ici M (D-80-4).
  AMENDEMENT AU TEXTE (v2, sous la meme contresignature) : le TEMOIN de
  la clause litterale se mesure a M_facteur >= 2 -- la valeur par
  defaut du moteur n'est pas convergee et ne se publie pas seule.
  Regle M15 au fondement : verifier la DIRECTION d'une perturbation,
  pas seulement sa presence. Gamma_c ne porte aucun verdict (P3 juge
  K_s, P6 juge Gamma_LS et Lambda_c ; P8 est non-verdictoire) : la
  lettre tuait la manche sur une quantite qui ne decide rien.
  EFFET SCRIPT : cle Q2_eta_descente = "E34" (procedure operative deja
  en v8, gagee sur cette cle).

80.4 E35 -- ERRATUM Q3 : LECTURE DES OCCUPATIONS DE LA GRAINE (gel 4.4)
  TEXTE PROPOSE (machine 1 ; contresignature machine 2 requise, comme
  pour les trois autres, voir 80.11) : la graine (phi) s'evalue aux
  occupations REELLES de la graine coherente (spec 3.0 et L6, "graine
  sur le rayon"), par continuation analytique exacte, identique aux
  entiers sur les entiers (selftest, 158 elements a 2.6e-16) ;
  l'arrondi de 4.4 (au plus proche, .5 vers le haut) est RESERVE a la
  graine de controle (F). La taille de boite E-B reste entiere par
  exces (ceil), independante de la lecture.
  FONDEMENT : l'ancrage entier quantifie s*_Q par pas ~20 % (dn2 = 1
  sur n2 ~ 2.6) contre une resolution gelee de 0.4 % ; piece portee au
  banc S-B, les deux nombres : entiere 1.1019 (ECHOUE, atteste), reelle
  0.9736 (PASSE, 53 % de la tolerance). Question posee par machine 2
  (E29 : resoudre une definition en silence est une faute meme quand la
  resolution est la bonne) ; les DEUX lectures restent portees par le
  script jusqu'a inscription.
  EFFET SCRIPT : cle Q3_lecture_graine = "E35" ; LECTURE_OCCUPATIONS =
  "reelle" a la contre-certification, apres contresignature.

80.5 E36 -- ERRATUM Q4 : EX AEQUO EXACT DANS UN RANG (gel section 8)
  TEXTE : la branche 1 de la cascade gagne la cause d'arret "ex aequo
  exact dans un rang". L'arret est route PAR la cascade -- etat
  ARRET EX AEQUO consigne dans le bloc de la primaire touchee, motif,
  JSON d'assemblage ECRIT -- jamais par exception.
  FONDEMENT : D-P3 (pre-vol) -- la nulle exacte de Spearman exige des
  rangs stricts ; un chemin d'arret non nomme est un chemin non
  gouverne ; la v7 mourait dans l'ecriture (forme M16). Conforme en v8,
  rejoue sous les conditions qui cassaient (pre-vol v2, log section 4 :
  P6 ARRET EX AEQUO, verdict ARRET DE REGLE, artefact ecrit).
  EFFET SCRIPT : cle Q4_ex_aequo_cascade = "E36".

80.6 D-M17-26..31 -- LES SIX DEFAUTS DE CUSTODY, COLLISION RESOLUE
  La note de rectification (2fa620dca9cbf0d0) a pose ses etiquettes
  24..29 sur une file qu'elle n'avait pas verifiee -- le defaut est
  entier, et c'est machine 2 qui l'a releve contre elle-meme a la
  certification ; sa clause "les numeros se prennent a l'acte" portait
  sur les numeros d'ERRATUM, non sur les etiquettes D-M17. L'ordre
  d'etape du present delta reprenait ces etiquettes. Or la file
  D-M17 est consommee jusqu'a 25 par un document CERTIFIE (voir tete).
  Une renumerotation se propage mecaniquement ou ne se fait pas : elle
  se fait ICI, vers l'avant, et ne touche aucune piece certifiee.
  TABLE DE CORRESPONDANCE (etiquette note -> numero pris) :
    24 -> D-M17-26  le couple (.py,.log) du banc v1 depose n'est pas
                    l'instrument qui a mesure ; le log depose contredit
                    la note (matrice 5/7 DEGENEREE contre 7/7 annonce).
    25 -> D-M17-27  aucun instrument de pre-vol depose ne visait v7 ni
                    v8 (seul depose : cible v6).
    26 -> D-M17-28  "1522 o" annonce "re-verifie" sans re-mesure ; la
                    re-verification reelle change le chiffre (3319 o
                    sur v8, pre-vol v2 log l.54).
    27 -> D-M17-29  un ecart (1,8 %) calcule entre deux tableaux de
                    conventions d'eta differentes ; dans la convention
                    unique : 2.2500 % puis 0.4640 %. Cause physique en
                    80.8 (i).
    28 -> D-M17-30  la mutation de matrice de la v1 etait une CONSTANTE
                    (lambda ignorant son argument) : le "MORD" affiche
                    n'etait pas une mesure. Correctif au banc v2 : la
                    matrice entiere rejouee sous trois mutations, compte
                    MESURE (6 hors-diagonale chacune).
    29 -> D-M17-31  une empreinte citee sans convention nommee ; sans
                    consequence sur la piece (brut == canonique), et
                    c'est precisement ainsi que la regle se perd.
  Les mesures des notes fautives etaient VRAIES et se reproduisent au
  chiffre pres sur les instruments v2 (rectification, section 3) ; les
  verdicts D-B1/D-B2/D-B3 n'ont jamais bouge. C'est D-M17-22 retourne :
  hier contenu invente sous empreintes justes, ici mesures vraies sous
  instruments manquants. Les deux modes fondent N-61 et N-62 (80.10).

80.7 TROIS BLOQUANTS DE GEL -- CONSIGNES OUVERTS, DIRECTION NON PRISE
  D-B1 : G-4 est definie au gel (6) et nommee en branche 1 (8), mais
    calculee nulle part (0 occurrence dans le script) -- une garde
    nommee au verdict qui ne peut pas mordre. Elle n'a de lieu qu'a p
    pair (L9) : elle nait avec D-B2.
  D-B2 : S-D et S-H exigent p = 4 par la structure de L9 (spec 3.8,
    verbatim au banc) ; le script gele P = 5 en constante. Position
    machine 1 consignee : PARAMETRE p plutot que moteur separe (couche
    exacte deja generale, custody unique) ; v9 sur ordre.
  D-B3 : a la geometrie derivee de 4.6, Gamma_LS n'est stationnaire en
    eta dans AUCUNE direction. Dossier instruit par les deux sondes :
    la montante converge vers des limites non nulles DIFFERENTES par
    point (~15.4 % au nominal, sonde v1 log l.16/27/38 ; ~22.2 % a
    w2 = 2.02, sonde v2 log l.33/42/51) -- la clause eta -> 2 eta est
    structurellement insatisfiable ; l'objection de cout est morte
    (grille plate en r_c, 40/41 ; direction (a) chiffree 1372 s =
    22.9 min) ; le critere de la sonde v1 est REFUTE par le second
    point (accepte dix couches, sonde v2 log l.67, la ou la descente
    fait 29.70 %, l.36) ; le critere corrige (deux derniers pas de
    descente sous tau_LS) est decision-identique aux deux points ET
    declare ajuste sur ses donnees. FAIT 1-bis : la clause N -> N+p a
    mesure la non-convergence (3.28 %) et rendu quitus -- pas de test
    (5 couches) plus court que l'echelle (10 : 3.2770 % puis 0.0160 %,
    sonde v1 log l.54 pour la forme 10->20 = 3.2924 %).
  DIRECTION LAISSEE OUVERTE SUR ORDRE OPERATEUR. Les quatre directions
  restent au dossier sans prise : (a) allonger l'absorbeur, (b)
  extrapolation en eta operative (Richardson, banc v2 log l.80 :
  2.299062e-10), (c) les deux, (d) largeur ponderee (voir directive).
  PREREQUIS AVANT TOUT GEL : le critere d'absorbeur est DU aux quatre
  points restants (1.97, 1.98, 2.03, 2.05 ; 892 s = 14.9 min a la loi
  de cout mesuree, facteur 1.213 -- chiffre verifie a la certification).
  DIRECTIVE PERMANENTE (ordre operateur, consignee) : LA DEFINITION DU
  TAUX ENTRE DANS L'ERRATUM QUI OUVRIRA 4.6, quel qu'il soit. Motif :
  la definition gelee ("etat de plus grand recouvrement") accroche
  Gamma_LS a un etat qui porte 2.9 % de la graine au nominal (fumee
  machine 1 sur la v7, NON OPPOSABLE, non repliquee a ce jour --
  `recouvrement` est un champ que gamma_LS rend, la replication se
  mesure a la sonde-complement) ; candidate consignee : la largeur
  ponderee somme(|c_nu|^2 Gamma_nu). Toute ouverture de 4.6 la traite ;
  aucune ouverture de 4.6 ne l'ignore.

80.8 DEUX RESOLUTIONS D'INSTRUMENT (E15), DECLAREES
  (i) CONDITIONNEMENT EN eta : 1.54e11 -- un ecart d'entree de 8.3e-16
    (l'ulp de eta) produit 1.282e-04 en sortie, determinisme verifie au
    bit (banc v2 log l.29-31). Consequences : eta se porte en UNE SEULE
    forme derivee declaree par manche (deux conventions du meme gel
    rendaient deux Gamma_LS a 1e-4 -- cause de D-M17-29) ; toute
    tolerance plus fine que ~1e-3 est HORS DE PORTEE de l'instrument.
  (ii) FENETRE PRATICABLE DE E-B : r_c = 40 est un PLANCHER (les
    geometries a r_c interieur echouent pour la bonne raison :
    absorbeur dans la barriere, banc v2 log l.36/38) ; le plafond
    PRATIQUE est N ~ 70 (93-94 s par eig) ; les lignes N = 90 et 120
    de la table sont EXTRAPOLEES, jamais mesurees (banc v2 log
    l.89-91 ; 1.96 et 6.18 Go). La parade a D-B3 vit dans
    N - r_c en [10, 30] ou elle ne vit pas. N_max = 120 declare au gel
    est inatteignable en pratique : "INFAISABLE EN-DECA DE N_max"
    devient sa propre categorie G-5, comptee.

80.9 DEUX FAITS DE MANCHE
  D-F1 : la forme fermee SUR-ESTIME le seuil de ~21 % en s --
    s*_Q/s*_ff = 0.7910 (w2 = 1.95) et 0.7746 (w2 = 2.02), lecture
    REELLE aux deux, celle qu'inscrit E35 (un rapport se cite avec son
    point ET sa lecture : E17 etendu aux comptes) ; trois des cinq
    fractions du gel (0.85, 1.00, 1.20) sont au-dessus du seuil compte,
    barriere VIDE. P4 n'est pas menace (sa bande porte sur l'ecart-type
    du residu, serre ; le residu MOYEN ~ -0.72 n'est pas teste -- la
    clause "forme fermee = echelle seulement" sera due au verdict). P6
    n'est pas menace : il tourne a 0.70 (E33), ou la barriere a 7
    sites. Le run consignera Lambda_c = 0 avec drapeau barriere_vide
    aux trois fractions hautes (D-P2 conforme en v8).
  D-F2 : P3 en clair -- rho >= 29/35 equivaut a somme d^2 <= 6 : P3
    tolere jusqu'a trois transpositions adjacentes disjointes et pas
    une seule inversion a distance 2. Se lit a cote de PR-7 (ii)
    (rho = 5/7, p = 49/720, retrouve TROIS fois par des chemins
    independants : enumeration d'acte, assemblage factice, assemblage
    sain). La mutation d'assemblage du selftest emploie la distance 2
    (une adjacente donne 33/35 et PASSE : angle mort declare).

80.10 DEUX REGLES DE CAMPAGNE, NEES DE LA RECTIFICATION
  N-61 (alpha) : UNE NOTE QUI TRANSCRIT UNE MESURE CITE LA LIGNE DU LOG
    QUI LA PORTE, ET LE LOG EST CELUI DE L'INSTRUMENT DEPOSE. Tout
    couple (piece, log) depose provient de la MEME execution, et le log
    porte son empreinte relue du disque en fin d'execution. (Extension
    du tranchant de E31/N-59 ; c'est la regle de D-M17-22, decouverte
    executable seulement si l'instrument depose est celui qui a mesure.)
  N-62 (beta) : UNE MESURE FAITE HORS INSTRUMENT DEPOSE N'EXISTE PAS.
    Corriger un harnais en ligne est legitime en exploration ; deposer
    la note sans porter la correction au fichier ne l'est pas. Le
    defaut trouve et non porte est un defaut non trouve (N-60 applique
    a l'instrument).
  Les deux regles ont ete appliquees AVANT d'etre prises : les
  verificateurs des trois notes du 24/08 (86/0, 42/0, 59/0, chacun avec
  test negatif), le controle de certification du present delta (67/2,
  deux morsures utiles) et le bilan machine 1 v2 (21 citations ligne a
  ligne, deux morsures avant depot ; B-1 LEVE : detenteur machine 1,
  piece JOINTE au depot) en sont les premieres executions.

80.11 CE QUE CET ACTE NE FAIT PAS
  Il ne CONTRESIGNE pas les textes d'errata : les numeros E33..E36 sont
  pris (E18), les textes deviennent opposables a la contresignature
  machine 2 (delta a venir, patron du delta 79). Il ne TRANCHE ni
  D-B1, ni D-B2 (position machine 1 consignee, decision a l'acte
  suivant), ni D-B3 (direction ouverte sur ordre). Il ne CERTIFIE pas
  le script : la contre-certification inscrira d'un seul geste les CINQ
  ancres -- GEL_EMPREINTE et les quatre cles E33..E36 -- et les gardes
  D-S4/D-S6 s'eteindront d'elles-memes. Il ne rend OPPOSABLE aucune
  mesure : les Gamma_LS reels du banc v2 et des sondes sont consignes
  comme INSTRUCTION du dossier D-B3 ; le pilote opposable vient apres
  la contre-certification. Il n'attribue aucun autre numero que E33,
  E34, E35, E36, D-M17-26..31, N-61, N-62.

PIECES CONSIGNEES (convention B, NFC+LF, 16 hex ; detenteur declare)
  gel v9 a5e86ca3191fb204 39686 o (CERTIFIE) ; script v8
  a25619c412c93fd9 82195 o (lignee v1..v7 au journal des versions) ;
  note rectification custody 2fa620dca9cbf0d0 14502 o ;
  note sonde v1 d8833783f7d1d5a7 8036 o ; note sonde v2
  acb654aa8860a16d 8139 o ;
  instruments (couples .py/.log de la meme execution, N-61) :
    banc v1 2c4c1d920685c641 / 9d47f2186240e545 (piece de la faute
    D-M17-26, deposee telle quelle) ;
    prevol v1 1d4fa96314242fd5 / 18a0c14a16754277 (cible v6, piece de
    D-M17-27) ;
    banc v2 920097ebc9e95623 / 0e0a2baacc2984cd ;
    prevol v2 8a2b16b8d44c50b8 / 4dfade44dd2b0647 ;
    sonde v1 04cf6c1290b7893e / 475d4850fd11c2d9 ;
    sonde v2 3e4f9594ced0db24 / fb45649600ebf96e ;
  controleurs (N-53, chacun avec test negatif) :
    verif rectification 7a1ac82e8a17fad8 / cd2d9994ba589677 ;
    verif sonde v1 ac9265caa72c09bc / b196afbfdc702257 ;
    verif sonde v2 f6c1afe8cec69253 / 386c9126b973e8aa ;
  bilans machine 1 (detenteur machine 1, JOINTS au depot, N-47) :
  v1 935c4928388988b4 7264 o (depasse) ; v2 3b1f5f84658d8fa2 9144 o ;
  instrument E-A de E34 (D-80-2, detenteur machine 2) :
  sonde_EA_m17_machine2_v1.py 4a34845cbceaea2a 7187 o /
  .log 34cb371dc050cb6e 2915 o ;
  certification du delta (detenteur machine 2) : note v1 2761c0631ae9a558
  (copie recue) ; controle verif_delta_80_machine2_v1.py
  91f0386dc25ba976 10847 o / .log 4945eb28f78d7c11 5950 o -- porte
  aussi les deux infractions E18 que machine 2 consigne contre
  elle-meme ;
  acte de certification du gel : note m2 v10 (empreinte au delta de
  son depot) ; delta precedent : 79 a5175671f93dfaf9.

-- FIN journal_delta_80 --
