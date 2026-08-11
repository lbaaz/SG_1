JOURNAL DELTA 74 -- GEL M16 v8 CERTIFIE (E19 RE-ARME), SCRIPT v2 :
LES SIX BLOQUANTS LEVES, LA LIAISON D'INSTRUMENT RESTE DUE
(machine 2, 2026-08-12)
=======================================================================
S'insere apres le delta 73 (2706c39a152ce728). Numero pris A L'ACTE au
depot, sous la regle 66.5.c. Acte de CLASSE B (delta 71) : la piece
deposee ARME une regle.

74.1 GEL v8 CERTIFIE -- E19 RE-ARME, ET LE 73 NE VAUT PLUS
  m16_pre_enregistrement_v8.md   2a1628005c5b015b   30960 o
  Certification machine 2, DEPOSEE avec le present delta :
  note_machine2_certification_gel_v8_et_prevol_script_v2.md
    b8e8a536dd30a386   11677 o
  Diff v7 -> v8 : 6 hunks, tous declares, zero clandestin. Le gel
  inscrit les trois clauses que le pre-vol du script avait fait
  remonter au niveau du gel : D-19 (faisabilite de la strate 2 en
  FORME DERIVEE, N_2 x (1 - q4_fen) >= 1, aucun seuil numerique) ;
  D-20 (q_L re-derive sur la FENETRE SEULE, temoin exclu, meme
  discipline qu'E27) ; N-55 (portee de N-28 alignee, test negatif a
  zone temoin, et MATRICES A PREDICATS INDEPENDANTS SUIVIES DE LEUR
  MUTATION -- le gel exige desormais la mutation).
  E19 EST RE-ARME SUR 2a1628005c5b015b ET SUR ELLE SEULE. Le delta 73
  armait la v7 (10dd0990) : il ne vaut plus. Le script doit se
  certifier CONTRE LA v8 -- il la cite deja.
  P-d reste scellee et inchangee (delta 73.4) : elle porte sur la
  manche, pas sur le texte du gel.

74.2 SCRIPT v2 -- LES SIX BLOQUANTS DU PRE-VOL SONT LEVES
  m16_crible_v2.py   91babeac987a01df   29293 o
  Le pre-vol opposable ne rejoue pas le banc : il lui presente le
  defaut. Six MUTATIONS PLAUSIBLES (pas des constantes -- une
  constante est trop facile a attraper) : H-A/H-B echangees ;
  DOUBLE-SIGNAL absorbe par H-B, c'est-a-dire le defaut D-15
  lui-meme ; garde NON D oubliee ; A5/A6 echangees ; A3/A4
  echangees ; A0 ignorant le plancher. SIX MORSURES SUR SIX. Les
  controles testent ce qu'ils pretendent tester.
  N-3 mord dans les deux formats du registre (long et court) et se
  tait sur un point absent. D-19 et D-20 sont dans le code sous la
  forme du gel. P-M16a est implementee, E ferme en (a-b)+c conforme
  au gel v4. Le script ECHOUE FERME : moteur_reel() et --run
  s'arretent tant que la liaison n'est pas certifiee.

74.3 LA LIAISON D'INSTRUMENT -- LE MOTEUR DESIGNE EST LE MAUVAIS
  Machine 1 demandait les signatures ; le releve dit plus que cela.
  Le script designe m9_replication_v1 (c8ed357b) et l'appel
  mesure_ligne. Cet appel n'existe pas -- et le module porte
  "P = 5" EN CONSTANTE DE MODULE : c'est le moteur de la manche M9,
  cable sur p = 5, ancres comprises. La manche M16 mesure p = 4, 5
  et 7. LE MOTEUR DESIGNE NE PEUT PAS LA SERVIR TEL QUEL.
  LE BON PATRON EXISTE DEJA AU REGISTRE, A DEUX COUCHES : la couche
  NUMERIQUE est bien m9 (chercher_seuil, integrer), mais avec sa
  constante P REBINDEE au degre mesure ; la couche MANCHE est
  m15_site83_v2.py (41ddebcd), le script qui a PRODUIT l'artefact
  96d78407 dont ce gel herite -- DEGRES = (7, 5, 4), plan_signes,
  assembler_ligne_m15 (convention (f), sP/sM, frag, asym),
  ligne_g6_exclue, x_du_point (E, S57, S4) et derive_pre_run (F,
  triplets, K_X).
  PRESCRIPTION : l'adaptateur REPREND m15_site83_v2 par extraction
  (regle 12) et n'ajoute que le cablage M16 ; le rebind de m9.P se
  DECLARE AU GEL comme manipulation d'instrument, avec restauration
  verifiee apres chaque ligne ; le pre-vol MOTEUR REEL porte sur UNE
  ligne connue du registre dont le verdict doit se reproduire --
  4|2.62|+1, vivante a l'artefact 96d78407. Sans ce point fixe, la
  liaison n'est pas verifiable.
  CONSEQUENCE : l'instrument se gele. La liaison (module, empreinte,
  couches, rebind) doit etre NOMMEE AU GEL -- donc une v9, courte.

74.4 TROIS DEFAUTS RESIDUELS, AUCUN BLOQUANT DE CONCEPTION
  D-23 : A2, A4 et A6 ne sont atteintes par aucun scenario -- et A4
    est la branche que la certification M15 v3 avait du creer apres
    coup. Trois scenarios a ajouter.
  D-24 : deux constantes tapees -- PROCHE = 2/100 quand le gel dit
    "a la resolution de la grille" (le centieme), sur le predicat
    qui separe A2 de A3 et A3 de A4 ; et les coefficients 2.25 /
    1.25 de E, JUSTES mais cites sans leur source (meme discipline
    que N-50).
  D-25 : le fond reel n'existe pas -- ni K_X, ni PLANCHER_X(b) =
    K_X * g(a, b, c), la seule classe etant FondFactice a seuils
    0.05. C'est DECLARE et le run est verrouille, donc ce n'est pas
    une tromperie, mais c'est la seconde liaison manquante et elle
    porte le falsifieur d'etage B. derive_pre_run de m15_site83_v2
    calcule deja les K_X : c'est de la reprise, pas de l'invention.

74.5 CE QUE CE DELTA NE FAIT PAS
  Aucune mesure. Le script n'est PAS certifie pour l'execution et
  aucun run ne peut avoir lieu. Rien n'est etabli sous moteur reel.
  Restent dus, dans l'ordre : gel v9 (liaison d'instrument nommee) ;
  adaptateur par extraction de m15_site83_v2 ; fond reel (K_X) ;
  scenarios A2/A4/A6 ; certification du script sous E19 contre la
  v9 ; PRE-VOL MOTEUR REEL sur la ligne temoin ; puis le run.
  Borne : 74.

EMPREINTES RE-DERIVEES LE 2026-08-12, relues du disque a l'instant de
la citation (N-48), depuis D:\devs\bocal\BOCAL4 et depuis un clone
frais du depot pour les deltas.
PIECES CITEES (16 hex ; brut == canonique NFC+LF)
  gel v8 2a162800 (certifie) ; gel v7 10dd0990 ; script v2 91babeac ;
  script v1 2b68bb18 ; pre-vol v1 bf9d9ca9 ; moteur m9 c8ed357b ;
  m15_site83_v2 41ddebcd ; certification v7 1c984db1 ; artefacts
  96d78407, fa109da9, 22fa1760 ; gel M15 v4 35022c5c ; deltas
  71 019296bd, 72 d3907be9, 73 2706c39a.

=== FIN DU JOURNAL DELTA 74 ===
