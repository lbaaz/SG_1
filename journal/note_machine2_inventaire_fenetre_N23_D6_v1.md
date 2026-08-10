NOTE MACHINE 2 -- INVENTAIRE EN EXTENSION DE LA FENETRE, EXECUTION DE
N-23, REGLEMENT DE D-6, ET DEUX DEFAUTS NEUFS (machine 2, 2026-08-10)
=======================================================================
Objet : produire hors ligne, AVANT l'ouverture de la session de gel,
l'inventaire que N-23 et le correctif de D-6 exigent -- pour que
machine 1 ecrive le gel de branche B2/B3 sur un inventaire REGLE et
non sur un compte cite. Travail machine 2 : je detiens les artefacts,
je re-derive.
Audit executable joint : inventaire_fenetre_site83_machine2_v2.py/.log
Fichier ASCII pur, LF seul : brut = canonique (N-10).

ARTEFACTS OUVERTS, empreintes re-derivees, TOUTES CONFORMES
  m15_results.json   96d784077577d57d   (N-23 le designait nommement)
  m12_results.json   fa109da92e582520
  m13b_results.json  22fa176013a9d46b
Les huit artefacts de lignee cites par le dossier v2 resolvent
localement a leurs empreintes ; les cinq autres (ad275870, 7cf3624b,
ed0e27b1, 70fe5611, 68df6576) n'avaient pas a etre ouverts ici.

VERDICT EN UNE LIGNE
  N-23 EST LEVEE ET ELLE RENFORCE B2. D-6 EST REGLEE : l'inventaire
  est ecrit en extension et les quatre comptes du dossier se
  re-derivent des artefacts, exactement. Mais l'exercice met au jour
  DEUX CHOIX DE GOUVERNANCE NON DECLARES -- l'unite de compte (D-8)
  et le traitement des ancres (D-9) -- qui deplacent les bornes plus
  que tout ce que le dossier discute : jusqu'a 0.2073 sur la borne
  qui dimensionne la strate 1, soit 2.7 fois l'instabilite qui a fait
  RETIRER le q_L de niveau-point en D-1. Aucun des deux n'inverse le
  sens : B2 vehicule / B3 lecture tiennent.

=======================================================================
1. N-23 EXECUTEE -- ATTRIBUTION PAR DEGRE, ET ELLE DIT MIEUX QUE PREVU
=======================================================================
Lu au bloc G6 du JSON 96d78407, ligne par ligne :
  point 2.71 (5 lignes) : 4|+1 MORTE, 5|+1 vivante, 5|-1 vivante,
                          7|+1 MORTE, 7|-1 vivante   -> degres morts 4 et 7
  point 2.72 (5 lignes) : 4|+1, 5|+1, 5|-1, 7|+1, 7|-1  TOUTES VIVANTES
  point 2.73 (5 lignes) : 4|+1 MORTE, 5|+1 vivante, 5|-1 vivante,
                          7|+1 vivante, 7|-1 vivante  -> degre mort 4

AU SEUL DEGRE 4 : 2.71 MORTE . 2.72 VIVANTE . 2.73 MORTE.
La signature 48.3 n'est donc PAS seulement de niveau point : elle est
instanciee AU DEGRE 4 -- c'est-a-dire au degre sans lequel E n'existe
pas, celui dont le rang au site est (6,2). La reserve de niveau que
la note d'arbitrage imposait ("jusque-la il se cite au niveau point
exclusivement", dossier v2, 4.B2) TOMBE : le fait decisif de B2
s'enonce desormais par degre, et il est plus fort ainsi.
  RESERVE, a declarer au gel : 2.72 vient de M12, 2.71 et 2.73 de
  M15. La juxtaposition est inter-manches -- legitime par la regle
  48.4 (ancres au bit), que le dossier invoque deja, mais elle se
  declare, elle ne se sous-entend pas.
  DIFFERENCE ENTRE LES DEUX MORTS, a consigner : 2.71 meurt a DEUX
  degres (4 et 7|+1), 2.73 a UN seul (4). La maille du crible n'est
  pas uniforme le long de la fenetre ; c'est une observation neuve,
  utile au dessin, et elle ne se lisait pas au niveau point.

=======================================================================
2. D-6 REGLEE -- L'INVENTAIRE, EN EXTENSION
=======================================================================
42 lignes portees par le registre dans [2.62, 2.73], toutes lues au
bloc de garde G6 des trois artefacts -- JAMAIS a la carte, dont le
champ 'recevable' qualifie la RECHERCHE et non l'exclusion (defaut
D1-3 du run M12, deja paye une fois).

  p = 4 (10 lignes) : 2.62|+1 v, 2.62|-1 v, 2.64|+1 M, 2.65|+1 v,
    2.67|+1 v (M12), 2.69|+1 M, 2.70|+1 M (M13b), 2.71|+1 M,
    2.72|+1 v (M12), 2.73|+1 M                      -> 5 mortes / 10
  p = 5 (16 lignes) : mortes = 2.65|+1 seulement     -> 1 morte / 16
  p = 7 (16 lignes) : mortes = 2.67|+1 (M12), 2.71|+1 -> 2 mortes / 16
                                       impair total  -> 3 mortes / 32

CONTROLE CROISE EXECUTE : le recompte des mortes M15 au bloc G6 rend
EXACTEMENT resume.points_perdus de l'artefact (6 lignes, assert dans
le script). Les six pertes M15 sont toutes de mecanisme G6.

LES QUATRE COMPTES DU DOSSIER SE RE-DERIVENT, SANS ECART :
  3.2 fenetre M15 seule      p=4 4/7  et impair 2/24   -- dossier idem
  3.3 complement sans 2.72   p=4 5/9  et impair 3/28   -- dossier idem
  L'arithmetique du dossier est donc juste ET son inventaire est
  reproductible depuis les artefacts. C'est la premiere fois que ces
  comptes sont COMPTES et non cites du gel v4.

CE QUE D-6 DEMANDAIT EST TRANCHE : 2.72 PORTE BIEN UNE LIGNE p=4,
mesuree et VIVANTE (M12, 4|2.72|+1). Le 5/9 du dossier ne l'atteint
qu'en mettant 2.72 ENTIEREMENT hors compte -- sa ligne p=4 et ses
quatre lignes impaires. L'inventaire reel complet est donc
  p=4 : 5/10 (q_L 0.6732)   impair : 3/32 (q_L 0.1656)
contre 5/9 (0.7325) et 3/28 (0.1882) au dossier. La phrase de 3.3 qui
nomme 2.72 parmi ses apports est incompatible avec le compte qui la
suit : l'une des deux doit ceder, et c'est desormais chiffre.

=======================================================================
3. D-8 (NEUF) -- L'UNITE DE COMPTE N'EST DECLAREE NULLE PART
=======================================================================
Le bloc G6 exclut par BRANCHE DE SIGNE : "5|2.65|+1" et "5|2.65|-1"
y sont deux entrees. Mais la campagne DECLARE, a p impair, la
convention s* = min des deux signes (convention M1/(f)) : de ce
cote-la, l'unite naturelle est (degre, point). Le dossier compte des
branches sans dire que c'en sont.
  (a) branche de signe  [lecture du dossier] : impair 3/32 -> 0.1656
  (b) (degre, point), morte si >= 1 branche  : impair 3/16 -> 0.3180
  (c) (degre, point), morte si TOUTES        : impair 0/16 -> 0.0957
FAIT QUI COMMANDE : LES TROIS MORTS IMPAIRS SONT DE SIGNE +1 --
5|2.65|+1, 7|2.67|+1, 7|2.71|+1. AUCUNE unite impaire n'est morte aux
deux signes. Sous la lecture (c), la fenetre ne porte AUCUNE mort
impaire et la phrase "impairs : 2/24" disparait purement et
simplement.
  PORTEE, ET ELLE EST NETTE : p=4 est quasi mono-signe (une seule
  branche partout, sauf 2.62). Le DIMENSIONNEMENT de la strate 1, qui
  ne joue que p=4, est donc ROBUSTE a ce choix (5/9 dans les lectures
  (b) et (c), 5/10 dans (a)). Ce que D-8 atteint, c'est la LECTURE
  degre-selective de la section 3.4 et de B3 : le contraste 0.77
  contre 0.17 devient 0.73 contre 0.32, ou 0.73 contre 0.10, selon
  l'unite. Le rapport passe de 4.1 a 2.3 ou a 7.7. C'est exactement
  la situation qu'E17 vise : une comparaison inter-degres sans unite
  declaree.
  LE SENS NE BOUGE DANS AUCUNE DES TROIS LECTURES : p=4 est toujours
  le degre le plus tue. La selectivite de degre, matiere de B3, n'est
  pas menacee ; sa MESURE l'est.

=======================================================================
4. D-9 (NEUF) -- LE TRAITEMENT DES ANCRES N'EST PAS SYMETRIQUE
=======================================================================
N-22 place 2.62 et 2.72 sur le MEME plan : ancres de geometrie,
valeurs de custody deja mesurees, non rejouees. Le compte du dossier
garde pourtant 2.62 DEDANS (ses deux lignes p=4 vivantes sont dans le
7 de "4/7") et met 2.72 DEHORS. Or les deux sont des SURVIVANTS :
les sortir du compte baisse n sans baisser k, donc monte la borne.
  les deux dedans (inventaire reel)  p=4 5/10 -> q_L 0.6732
  2.72 dehors  [lecture du dossier]  p=4 5/9  -> q_L 0.7325
  2.62 dehors                        p=4 5/8  -> q_L 0.8014
  les deux dehors                    p=4 5/7  -> q_L 0.8805
  AMPLITUDE : 0.2073 sur la borne qui dimensionne la strate 1.
  A comparer aux 0.0769 qui ont suffi a faire RETIRER le q_L de
  niveau-point en D-1. C'est 2.7 fois plus, sur un choix qui n'est
  pas discute du tout.
  CE QUE CA FAIT AU CHIFFRE CONSIGNE D'AVANCE : la strate 1 annonce
  P(>= 1 survivant) = 0.5405 pour N = 3. Cette valeur vient de la
  fenetre M15 SEULE (4/7), qui n'est aucune des quatre politiques
  d'ancres ci-dessus. Selon la politique declaree, le meme N = 3
  rend P(>=1) entre 0.3175 (les deux ancres dehors) et 0.6949 (les
  deux dedans). Un chiffre consigne d'avance sur un choix non
  gouverne n'est pas une consignation : c'est un choix qui s'ignore.

=======================================================================
5. CE QUE CECI NE CHANGE PAS
=======================================================================
L'arbitrage tient, entierement. B2 CRIBLER reste le vehicule -- et
son fait decisif est RENFORCE par la section 1. B3 REVISER reste la
lecture -- et sa matiere (la selectivite de degre) survit aux trois
unites. B1 reste ecartee. Les prescriptions N-20 a N-32 restent
opposables telles quelles. Rien ici ne touche a la geometrie (g en
Fraction exacte, ratios 400/133 et 16/19, inchanges), ni a la strate
2, ni au temoin hors site (N-25).

=======================================================================
6. PRESCRIPTIONS (suite de N-32 ; N-33 a N-36)
=======================================================================
N-33  (D-6 / N-27 EXECUTEE) L'inventaire en extension est celui de la
      section 2 de la presente note. Le gel l'EXTRAIT par structure,
      il ne le re-frappe pas (regle 12). Toute ligne ajoutee au gel se
      declare avec son artefact et son bloc de lecture. Le compte de
      chaque degre est le CARDINAL de la liste, verifie par assert au
      --selftest.
N-34  (D-8) Le gel DECLARE l'unite de compte AVANT mesure -- branche
      de signe ou (degre, point) -- et l'applique IDENTIQUEMENT aux
      deux degres. Toute comparaison inter-degres (3.4, matiere de
      B3) cite son unite (E17). Si l'unite (degre, point) est
      retenue, la phrase "impairs : 2/24" ne peut plus etre ecrite :
      elle devient 3/16 ou 0/16 selon la regle de mort choisie, qui
      se declare aussi.
N-35  (D-9) Politique d'ancres SYMETRIQUE et declaree avant mesure :
      2.62 et 2.72 sont toutes deux dedans, ou toutes deux dehors.
      Le N de la strate 1 se derive EN FORME (regle 13) de la borne
      issue de la politique declaree, jamais d'un nombre fige ; les
      deux extremes (q_L 0.6732 et 0.8805, soit P(>=1) 0.6949 et
      0.3175 a N = 3) sont consignes d'avance comme FOURCHETTE, et la
      clause "zero survivant n'est PAS une refutation" se lit contre
      la borne basse.
N-36  (N-23 LEVEE) La signature du site s'enonce AU DEGRE 4 :
      2.71 morte, 2.72 vivante, 2.73 morte, lignes p=4. Le gel cite
      la juxtaposition inter-manches (M12 pour 2.72, M15 pour 2.71 et
      2.73) et sa legitimation par 48.4. Il consigne aussi que 2.71
      meurt a deux degres et 2.73 a un seul.

=======================================================================
7. CE QUE CE CONTROLE NE JOUE PAS
=======================================================================
- Aucune mesure rejouee. Les statuts sont LUS aux blocs G6, non
  recalcules depuis les s*.
- "MORTE" == exclue par G6. Sur la fenetre M15 toutes les pertes sont
  de mecanisme G6 (resume de l'artefact) ; ce controle n'a pas ete
  re-fait pour M12 et M13b, ou d'autres mecanismes existent hors
  fenetre.
- Les points hors [2.62, 2.73] ne sont pas inventories : les bornes
  de domaine (0.0855 / 0.0679) ne sont pas recalculees ici.
- Aucun q_L de niveau-point n'est derive, cite ni compare (N-20).
- LE CHOIX ENTRE LES LECTURES DES SECTIONS 3 ET 4 N'EST PAS FAIT ICI.
  Il appartient au gel, qui doit le DECLARER avant mesure -- c'est
  tout l'objet de N-34 et N-35. Cette note chiffre les branches, elle
  n'en prend aucune.
- Aucun numero de delta ni d'erratum n'est attribue (E18).

PIECES CITEES (16 hex ; brut == canonique NFC+LF)
  artefacts : 96d78407, fa109da9, 22fa1760 (ouverts) ; dossier
  trilemme v2 347f25da ; note d'arbitrage 1c490f90 ; note de controle
  ae8ff790 ; deltas 66 ab5db7ef et 67 6194e90f ; gel v4 35022c5c
  (cite, non rouvert) ; audit joint v2 .py / .log.

=== FIN DE LA NOTE D'INVENTAIRE -- machine 2, v1 ===
