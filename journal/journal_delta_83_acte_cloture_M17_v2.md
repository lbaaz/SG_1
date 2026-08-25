JOURNAL DELTA 83 -- ACTE DE CLOTURE M17 : v17 CONTRESIGNEE, LE VERDICT
PAS DE SIGNAL AU FORMAT DES CLOTURES, CINQ ERRATA (E37..E41), TROIS REGLES
(N-65..N-67), HUIT DEFAUTS (D-M17-36..43), LA FILE DES DIX-HUIT SOLDEE,
DEUX QUESTIONS DE GEL ET UNE CELLULE CONSIGNEES OUVERTES
(redaction machine 1, depot operateur, 2026-08-25) -- VERSION 2
=======================================================================
Repond a : note_machine2_certification_delta_83_v1.md 20417e08843f36b6
8702 o (copie recue ; CERTIFIE SUR LE FOND, un bloquant de forme, leve
ici). Remplace le brouillon v1 98efbd6c9837eef2 (non edite, PB-1).
Leves ici : la tete du distant (section 1 de la certification, forme
executable portee telle quelle, en-tete et 83.16) ; trois citations de
table a une ligne pres (l.163, l.472, l.35) ; le temoin "E37" de
l'instrument machine 2 signale comme non-prise. La contresignature
demandee en 83.1 est rendue : CONFORME.
Repond aussi a : POUR_MACHINE1_reponse_file_83_v1.md c05d7f15847f319a 8643 o
(les onze et l'etat de D-M17-33/34) ; POUR_MACHINE1_envoi_archive_
cloture_M17_v1.md 8c836535a745f8f6 (l'archive, 76 pieces, recue 26/26) ;
POUR_MACHINE1_reponse_cause_P7_v1.md 66f0915d95788912 (la cause P7) ;
note_machine2_lecture_reconciliation_delta82_v1.md be9f83d69f17725d.
S'insere apres le delta 82 (commit cd9ba3777bd5f35fbad9b9e363cb4652
8805003f, arbre 9e440c34) ; la tete du distant au moment de la redaction
est 1e940f9 (1e940f97838df22e883ba4a2d5f1356779a9490b, releve par
machine 1 le 25/08 : parent cd9ba37, un seul fichier touche, README.md,
aucun journal_delta_83 a l'arbre, dernier delta 82), un commit de
REPARATION du README public, sans numero de delta, pousse par machine 2
sur ordre de l'operateur le 25/08 -- il ne touche que README.md et ne
modifie aucune piece de registre. L'ancre 66f71c5 reste PERIMEE, absente
du distant, citee nulle part par machine 1.
Numero pris A L'ACTE au depot, sous la regle 66.5.c. Acte de CLASSE B
(delta 71) : il contresigne le texte joue et arme des errata.
Acte de CONSIGNATION seulement : il ne tranche aucune question de gel,
il ne rejuge rien, il n'ouvre pas M18.
Files verifiees avant prise (E18 : jamais de reservation) :
  errata E : le gel v12-b2 cite E13, E15, E18, E19, E27, E29, E32, E34 ;
    la table ERRATUMS_CONSIGNES du script v17 (l.274) porte E33..E36 ;
    aucune piece de l'archive (76) ni du complement (13) ne cite au-dela
    de E36 -> libre au-dela de E36. Un "E37" existe sur le disque machine
    2 dans certif_gel_v10_machine2_v1.py l.220 et son log v2 l.51 : c'est
    un TEMOIN DE TEST NEGATIF (mutation fabriquee pour verifier que le
    controle E18 mordrait), pas une prise -- signale pour qu'aucun
    controle futur ne morde dessus (certification 83 v1, section 3.ii) ;
  regles N : derniere citee N-64 (certification gel v11 l.77) -> libre
    au-dela de N-64 ;
  defauts D-M17 : cites jusqu'a 35 ; 33 et 34 PRIS par la contre-
    certification v14 (l.142, l.355), 35 (l.359), "consignes ici et ne
    demandent pas de numero d'erratum" (l.472) -> libre au-dela de 35.
Toute valeur ci-dessous est RELEVEE a la ligne citee d'une piece de
l'arbre cd9ba37, de l'archive m17_cloture_pieces_v1 (MANIFEST
c1e336a00647cf8a) ou du complement (MANIFEST 981c9dbcb99edad5) ; 79
citations de ligne verifiees mecaniquement, 2 tests negatifs, log joint.
Mapping declare : virgule decimale des notes machine 2 -> point ASCII.

83.1 LA CONTRESIGNATURE : LE TEXTE JOUE EST LE TEXTE CERTIFIE
  m17_chaine_v17.py  82a0be882568fe0c  103150 o -- CERTIFIE (certification
  v17 l.3, 75/75) ; JOUE tel quel (note de run l.187, releve a 23h09
  AVANT le lancement, l.185, N-59). Certifie == joue a l'empreinte et a la
  taille : diff ZERO, aucun bloc d'en-tete ne les separe. E19 : l'ancre
  du script est 20950e52e7d63225, le gel v12-b2, dont l'empreinte figure
  dans une certification croisee anterieure, de6f702f0d4b052e
  (certification v17 l.17-19) -- chronologie opposable. Une seule fonction
  separe la v17 de la v16 (temoins_P7, certification v17 l.66-67).
  Ligne de contresignature MACHINE 2, rendue a la certification du
  present acte (20417e08843f36b6) : "CONFORME. m17_chaine_v17.py
  82a0be882568fe0c 103150 o -- l'empreinte et la taille du texte
  CERTIFIE sont celles du texte JOUE, releve a 23h09 avant lancement
  (note de run l.185-187, N-59). Aucun bloc d'en-tete ne les separe :
  diff ZERO."  Le script est CLOS.

83.2 VERDICT DE MANCHE, AU FORMAT DES CLOTURES (patron delta 78)
  "M17 : PAS DE SIGNAL (cascade, branche 6) -- P3 ECHOUE : rho = 5/7 contre
  rho_crit 29/35, p_exact 49/720 ; P6 ECHOUE : (i) rho = 1/35, PLAT ; (ii)
  violations 0/6 ; LE CONTROLE EN SIGNE TIENT SUR LA GRILLE ENTIERE."
  Chaque clause adossee a son artefact : assemblage.json l.123 (verdict),
  l.61-62 (5/7, 29/35), l.44 (49/720), l.108 (1/35), l.110
  (violations_ii 0). La lecture "echelles reproduites, ordres non" est
  portee comme LECTURE, hors gel (note de run l.60), et ne fait pas partie
  du verdict. Ce que la manche n'etablit pas, tel que la note de run le
  dit : elle ne refute pas le modele ; six points est le minimum du gel ;
  rien hors de ce site ni de la fenetre [1.95 ; 2.05].
  Contraste de lignee : M7, M8, M9 sans verdict (C2) ; M17 est LA PREMIERE
  MANCHE QUANTIQUE DE LA CAMPAGNE QUI CONCLUT (SUIVI 2026-08-25, section 0,
  a4ba101d3e53d6c2) -- sur un negatif, exact, et defendable ligne a ligne.

83.3 E37 -- ERRATUM 4.6, DIRECTION (c) AU GABARIT E34 (gel v10)
  TEXTE : la montante eta -> 2 eta devient TEMOIN NOMME ; l'operatif est la
  descente + Richardson par le ratio + residu declare ; la geometrie est
  fixee PAR POINT par le critere d'absorbeur, L dans {20, 30}, nominal 20 ;
  le TAUX est la largeur ponderee somme(|c_nu|^2 Gamma_nu) a retention
  RELATIVE, poids_total consigne (gel v10, section 4.6 ; la definition du
  taux y ENTRE, directive permanente de l'operateur).
  FONDEMENT : tous les chiffres du gel se re-derivent des mesures machine
  2 -- Richardson au nominal 2.157522e-10, residu 0.0022, chiffre (b)
  2.299062e-10 declare NON REPORTABLE (certification gel v10 l.66-71).
  ARBITRAGE : GEL CERTIFIE 96076b26be766304 46176 o (l.11-12) ; condition
  (iii) DECHARGEE par artefact opposable, recouvrement 2.8803 % (l.89,
  l.96) ; la portee de la directive n'est pas tranchee par la
  certification (section 6), l'operateur l'a tranchee a la v11 (83.4).
  EFFET SCRIPT : trois ordres, dont le re-ancrage (l.123) ; joues en
  v13/v14 (RA + GEO + POND), certifies en v15.
  Ferme les items 12 et 16 de la file (83.9).

83.4 E38 -- ERRATUM DES PORTES PAR TRANSLATION (gel v11)
  TEXTE : la porte en r_c se lit PAR TRANSLATION, r_c -> r_c + p ET
  N -> N + p conjoints, L conserve (gel v11 l.353) ; mesuree au nominal :
  MORD a N fixe (6.71 %), PASSE par translation (1.96 %) (l.360) ;
  N_plus_p seul demeure, 1.56 % (l.364).
  FONDEMENT : sous la v15, moteur reel, rc_plus_p = 6,712623e-02 (l.163)
  contre tau_LS 0,05 -> la manche entiere rendait ARRET DE REGLE par la
  branche 1 (certification v15 l.162-167).
  ARBITRAGE : arbitrage operateur (i), la translation (certification gel
  v11 l.1, CERTIFIE l.17) ; N-64 executee (l.77).
  EFFET SCRIPT : porte de position (v15 l.1504, certification v12-b2
  l.92-94) ; nom translation_p ; au pilote v17 translation_p =
  0.01958476, EN DOMAINE (pilote v17 l.26, l.12).
  Ferme l'item 15 de la file (83.9).

83.5 E39 -- ERRATUM P7 : MODULE, SEUIL RELATIF, PAR TRANSLATION (gel v12-b2)
  TEXTE : |Gamma_LS(jumeau)| <= 1e-2 x Gamma_LS(H), au MEME point et a la
  MEME geometrie que la mesure, aux DEUX points r_c et r_c + p lus PAR
  TRANSLATION ; LA SOUS-CLAUSE DE MONOTONIE EST RETIREE (gel v12-b2
  l.658-661).
  FONDEMENT : quatre cellules rejouees, marges 51,8 / 31,4 / 10,7 / 56,1
  (certification v12-b2 l.16-19) -- deux d'entre elles sont reprises par
  E40 ci-dessous.
  ARBITRAGE : CERTIFIE 20950e52e7d63225 58507 o (l.4-5), 20 controles.
  EFFET SCRIPT : temoins_P7 reecrite (v16, puis v17 : chemin nomme par
  _chemin_point) ; jouee POUR DE VRAI au run : P7_sain = True, cellules
  -4.203035e-14 (51,8 x) et -6.922631e-14 (32,6 x) (note de run l.141-144).
  Ferme l'item 17 de la file (83.9).

83.6 E40 -- ERRATUM DE LA CERTIFICATION v12-b2 (PIECE DEPOSEE) : LE SEUIL
     EST PAR CELLULE ; 32,6 x ET NON 31,4 x
  TEXTE (forme executable machine 2, lecture be9f83d69f17725d section 2) :
  certification du gel v12-b2, table de la clause P7, ligne "L = 20,
  translate" : le seuil lu est 2.175170e-12 (celui de la cellule r_c) ;
  le seuil de CETTE cellule est 2.255359e-12 (= 1e-2 x son propre
  signal_H, temoins_P7.json ; lecture l.52). La marge est donc 32,6 x et
  non 31,4 x (l.17). La clause passe dans les deux lectures ; le verdict
  P7 est inchange. La note de run et le delta 82 sont JUSTES : rien a
  rectifier au registre.
  CAUSE (forme executable machine 2, reponse cause section 2, adoptee mot
  pour mot) : la clause P7 a ete certifiee sur quatre cellules alors que
  le signal H n'avait ete mesure qu'au SEUL r_c, une fois par L (sondes
  cf97c641db146ae4 : 2.175170e-10, 1 occurrence, l.25 ; 0cc590845d8fbf8c
  : 2.175346e-10, 1 occurrence, l.30). L'instrument
  verif_clause_P7_v12b2_machine2_v1.py (a9063716a6cbc2e6) a donc apparie
  un signal PAR L, la ou le gel demande le signal H "au MEME point" --
  PAR CELLULE. L'appariement par L n'etait pas un choix : c'etait le seul
  possible avec les mesures existantes. Ce qui manquait n'etait pas une
  regle, c'etait une diagonalisation. Aucune valeur du verdict n'en
  depend.
  FAIT VERSE par machine 2 contre elle-meme : la forme "DU MEME POINT" est
  ecrite dans la sonde qui a propose la clause (sonde v2 l.37-38, cite en
  reponse cause l.69), reprise par le gel, jamais jouee par la table qui
  la certifiait.
  D-M17-36 (machine 2) : clause certifiee sur des cellules sans signal
  propre -- quatrieme instance du 24/08 de la regle "le fondement chiffre
  d'une clause = les cellules qu'elle JOUE". LEVE pour L = 20 par le run
  (la mesure manquante existe : 2.2553591793172693e-10) ; OUVERT pour
  L = 30 (83.8).
  Comment il est sorti : par une troisieme lecture -- la reconciliation du
  82 (note machine 1 b4704e2ef81cef9b, b.4) a trouve deux pieces de
  machine 2 en desaccord sur une valeur non portee par le verdict ; c'est
  l'ARTEFACT (temoins_P7.json, main machine 2) qui a departage, contre la
  certification.

83.7 E41 -- ERRATUM DE PROSE DU GEL v12-b2 : 11,7 -> 10,7 ; CINQ
     GEOMETRIES -> LES QUATRE CELLULES JOUEES PLUS LES TROIS DE DIAGNOSTIC
  TEXTE : les deux nombres de prose a corriger, releves a la certification
  v12-b2 l.52-53 ; le fondement du coefficient portait sur des cellules
  que la clause ne joue pas, et la marge vraie a L = 30 est 10,7 x (l.18,
  l.45-46). Le verdict ne bascule pas (l.48). Le gel ne s'edite pas
  (PB-1) : la correction vit a la version suivante. C'est l'item 18 de la
  file (certification v12-b2 l.128-129).

83.8 UNE CELLULE CONSIGNEE OUVERTE : L = 30, TRANSLATE (gabarit 80.7)
  La certification v12-b2 l.19 porte 56,1 x pour cette cellule, calcule
  sous le signal H de r_c ; ce signal n'a ete mesure qu'une fois a L = 30
  (reponse cause l.30) : la ligne n'est PAS ETABLIE. La ligne r_c (10,7 x,
  pire marge de la clause) est intacte. Bornes re-derivees par les deux
  machines : la pire marge quitterait r_c si signal_H(translate, L = 30)
  < 4.1460e-11 (5,2 x sous r_c) ; la CLAUSE echouerait a cette cellule si
  < 3.8789e-12 (56 x sous r_c). A L = 20 le signal translate mesure est
  plus GRAND de 3,7 pour cent (1.0369). Observe, non prouve a L = 30. La
  reparer est une diagonalisation NEUVE : geste d'instrument, pas de cet
  acte. DIRECTION NON PRISE. Aucun point du run ne joue P7 a L = 30.

83.9 LA FILE DES DIX-HUIT, SOLDEE ITEM PAR ITEM
  La file est un COMPTE porte par les certifications (SEPT contrecert v9
  l.298 ; HUIT certification v10 l.264 ; NEUF certification v11 l.172 ;
  DIX banc lourd v3 l.174 ; ONZE prevol v11 l.163 ; DOUZE certification
  gel v10 l.209 ; SEIZE certification v15 l.217 ; DIX-SEPT certification
  gel v11 l.246 ; DIX-HUIT certification v12-b2 l.128 ; le chainon DIX
  n'etait dans aucune liste des deux machines -- reponse file section 2).
  Enumeree par machine 2 (reponse file section 1), relue ligne a ligne :
   1. R-1, "8 chiffres et non 10" (contrecert v9 l.299 ; certification du
      delta 80 l.91-96 : caracteres de tete communs 8) -> D-M17-38
      (machine 2), CLOS dans la piece meme qui le declare.
   2. les quatre lignes de fondement echouees de l'acte 80 (delta 81
      l.79-81 : acte l.77-80, 266 o, 151063c2614891f9, non signees, lues
      comme fondement) -> D-M17-37 (machine 1, plume de l'acte 80) ;
      CLOS : le fondement E34 est porte par la contresignature du delta
      81 (E34_TEXTE_v2 acd878ec74d6948b).
   3. les ecarts D2a du gel v9 (contrecert v9 l.299-300 ; borne de (D2a)
      = 1/10, certification m17 v10 l.130) -> NON INSTRUIT par cet acte :
      nomme, source, RESTE A LA FILE sans numero. Un item que l'acte ne
      sait pas instruire ne prend pas de numero.
   4. collision de nom entre deux instruments de meme lignee ecrits par
      les deux mains (croisement sonde v3 l.186-190) -> N-65 : un
      instrument porte sa MAIN dans son nom des lors que les deux
      machines peuvent en ecrire un de la meme lignee.
   5. la reprise qui lit zero sur un log qu'elle ne sait pas lire
      (l.191-194) -> N-66 : un mecanisme de reprise REFUSE un log dont il
      ne reconnait pas le format, au lieu de le compter vide.
   6. D-M17-30, le sixieme site, racine dans l'ordre machine 2
      (contrecert v9 l.300-301) -> deja numerote au delta 80 ; la
      RACINE est consignee ici avec attribution partagee. Pas de numero.
   7. la question B_N, doit-il suivre p ? (l.301) -> QUESTION DE GEL,
      consignee OUVERTE, direction non prise, routee a M18.
   8. stat M desc, 4.1e-07 contre 4.2e-06 entre les deux mains
      (certification v10 l.120-121) -> CLOS, environnemental, rapport
      10,2 (certification v17 l.70). Resolution d'instrument declaree
      (E15), pas de numero.
   9. le fragment de docstring cite la FORME CANONIQUE, pas le litteral
      Python (certification v11 l.71-73) -> N-67.
  10. S-H (banc lourd v3 l.174-175) -> QUESTION DE GEL, consignee OUVERTE,
      routee a M18 (opinion machine 1 consignee au SUIVI : erratum via le
      rho de Spearman existant).
  11. l'arret-par-exception de l'assembleur (prevol v11 l.163-164) ->
      D-M17-39 (machine 1) ; LEVE en v12 (l'arret sort par la cascade),
      confirme au run : arrets_points [], arrets_sans_index [] (note de
      run l.148-149).
  12. le chiffre (b) NON REPORTABLE, 2.299062e-10 (certification gel v10
      l.69) -> declare par le gel lui-meme comme son exception ; ferme
      par E37. Pas de numero.
  13. D-M17-31 -> deja numerote ; LEVE (certification v15 l.22) ; son
      contrefactuel mesure au run est au delta 82 (82.5.a).
  14. D-M17-32 -> deja numerote ; LEVE, les deux extrapolations declarees
      des deux cotes (certification v15 l.25, l.218-219).
  15. la porte rc_plus_p -> fermee par E38 (83.4) et le nom translation_p.
  16. la condition (ii) du taux et sa retention -> fermee par E37 :
      retention RELATIVE, poids_total consigne (0,867056 au nominal,
      certification v15 l.176 ; "precision de gel due" l.178, rendue).
  17. P7 -> E39 (83.5).
  18. les deux chiffres de prose -> E41 (83.7).
  HORS DU COMPTE, porte depuis le debut et jamais compte (reponse file
  section 3) : le nom propre errone en l.4 du docstring, herite de la v8
  (contrecert v9 l.253-256) -> D-M17-40 (machine 1) ; LEVE en v17
  (certification v17 l.56-57, controle non nul).
  HORS DU COMPTE : D-M17-33, D-M17-34, D-M17-35 -- pris par la contre-
  certification v14, sans numero d'erratum, repondus par machine 1 le
  jour meme (reponse file section 4, l.107). Rien d'ouvert.

83.10 LE DEFAUT D'ORDRE DE LA v16, LEVE -- D-M17-41 (machine 1)
  La v16 lisait "le premier w2 qui matche" dans le dossier de run ; le tri
  ASCII y place pt_39_20_P8_g0.0003.json avant pt_39_20_f070.json
  (retrait v16 l.22-26) : P7_sain = False, la manche entiere en ARRET DE
  REGLE apres cinq heures de moteur. Ce n'est pas le contenu qui bloque,
  c'est l'ordre des noms (l.35). Certification v16 RETIREE par machine 2
  dans l'heure (85537791102f3ae1) ; le pre-vol a mordu AVANT le pilote.
  LEVE en v17 : chemin NOMME par _chemin_point, la fonction qui a ecrit le
  point ; deux tests negatifs (certification v17 section 2). Le piege est
  visible dans l'artefact depose : MANIFEST de manche l.18-22. Regle
  acquise : un temoin qui lit un DOSSIER se joue sur un dossier de la
  forme que le run produit.

83.11 LES QUATRE FAITS DU RUN ; DEUX QUESTIONS DE GEL CONSIGNEES OUVERTES
  (a) le chemin L = 30 a ete pris au premier run reel (P8 g = 1e-3, 67
      minutes) ; contrefactuel : sous v14/v15 la manche mourait a 00h50
      sans verdict (delta 82 82.5.a). Consigne.
  (b) 24 points sur 34 ne sont jamais lus -- recompte du MANIFEST depose
      seul : 34 - (site 1 + P8 3 + f070 6) = 24, fractions f050/f085/
      f100/f120 (note reconciliation b.3). QUESTION DE GEL, CONSIGNEE
      OUVERTE, direction non prise : un lecteur, ou la sortie de grille.
      Par N-62, un lecteur est un instrument neuf : il est de M18 et ne
      peut rien au verdict de M17.
  (c) six arrets f050 que la cascade ne voit pas. QUESTION DE GEL,
      CONSIGNEE OUVERTE (avis machine 1 verse : consignation minimale a
      l'assemblage), direction non prise, routee a M18.
  (d) P8 non calculable par construction ; N_derive 206 contre N_max 120,
      le gel estimait 231 (delta 82 82.5.d). Consigne.

83.12 TROIS RESIDUS DE L'INSTRUMENT, A LA MAIN DE L'OPERATEUR
  - E29, le denominateur par cellule : LEVE PAR DECLARATION au docstring
    v17 (certification v17 l.58-60 : ecart 3,69 % au nominal, meme
    verdict, code inchange). L'operateur CONFIRME ou REVOQUE la levee par
    declaration ; le present acte ne la tranche pas.
  - la garde de la l.4, proposee, NON JOUEE (certification v16 l.141) :
    consignee non jouee.
  - le depot des deux pieces de classe B (83.14).

83.13 LES FAUTES DE PROSE DES DEUX MACHINES, CLOSES
  D-M17-42 (machine 1) : "23/720" et "26/720" inventes en ecrivant a la
  premiere lecture du verdict, verses au 82.6 (delta 82 l.106-108). CLOS :
  n'existent nulle part comme valeurs, seulement comme texte de leur
  consignation ; aucun des deux n'est une queue atteignable a n = 6 ;
  les opposables 21/720 et 49/720 se re-derivent des rangs deposes.
  D-M17-43 (machine 2) : "29/35 est bien le plus grand seuil dont la queue
  reste sous alpha" (ordre 5302f3a3a60af328 l.112-113) ; superlatif a
  l'envers, nombres justes ; verse par machine 2 contre machine 2
  (lecture section 4). Forme correcte : 29/35 est le PLUS PETIT seuil
  atteignable dont la queue reste sous alpha (21/720 = 0,0292) ; le cran
  en dessous, 27/35, passe a 37/720 = 0,0514.

83.14 LA RECONCILIATION DU 82 ET LE REGISTRE
  Le delta 82 (14e44b01d74c8559) a ete reconcilie apres depot depuis les
  objets pousses (note machine 1 b4704e2ef81cef9b, 58/58 ; lecture
  machine 2 be9f83d69f17725d, 44/44) : cinq blobs 5/5, 121 aiguilles, 0
  ecart delta/blob ; l'amendement du commit (66f71c5 -> cd9ba37, trailer
  d'outillage retire, arbres egaux selon machine 2, 121 s entre les
  dates) est consigne ; 66f71c5 ne se cite pas.
  Apres cd9ba37, un commit sans numero de delta, 1e940f9 (README, machine
  2 sur ordre operateur, 25/08) : trois citations du README public etaient
  fausses -- point d'entree vers une note absente de l'arbre (10d ; servies
  10b et 10e), revue pre-envoi annoncee livree alors que consignee PERDUE
  au delta 78, plan "deltas 1..60, 61-63" au lieu de 19..82 -- reparees ;
  apres push, tout chemin cite a la racine resout, quartic-bundle 57/57,
  N-39 = 0 sur 249 fichiers (certification 83 v1, section 1). Consigne.
  CE QUI N'EST PAS AU REGISTRE (precedent 78.6) : le gel v12-b2
  20950e52e7d63225 (qui arme E19) et le script v17 82a0be882568fe0c (le
  texte joue, contresigne en 83.1) sont ABSENTS de l'arbre cd9ba37 --
  cherches par empreinte sur les 249 fichiers. Une piece qui arme une
  regle est de classe B et se depose au registre, a l'acte : DEPOT DU,
  a la main de l'operateur, avec le present delta ou apres lui. Idem pour
  toute piece citee ci-dessus par empreinte et absente de l'arbre (les
  76 de l'archive, les 13 du complement) : citees "copie recue,
  detenteur machine 2", elles ne resolvent pas pour un tiers tant
  qu'elles ne sont pas deposees.
  FAIT DE CUSTODY (reponse file section 5) : la levee de D-P0..D-P3
  (pre-vol N-58) n'est etablie que par le bilan machine 1 v1
  (935c4928388988b4 l.21), piece hors registre ; le bilan v2 DEPOSE ne la
  porte pas. Consigne.

83.15 CE QUI N'A JAMAIS TOURNE (discipline anti-effet-d'annonce)
  - 24 points sur 34 : calcules, ecrits, comptes en G-5, ouverts par
    aucune ligne (83.11.b) ;
  - les six arrets f050 : hors pts, hors arrets, hors branche 1 ;
  - P7 hors du point nominal : les 33 autres points ont chacun leur
    signal et leur bruit, rien n'y est mesure (certification v12-b2
    section 5, note de run section 5) ;
  - la cellule L = 30 translate (83.8) ;
  - P8 : aucune pente calculee (barriere vide a 3e-3, arret a 1e-3,
    infaisable a 3e-4) ;
  - la garde de la l.4 : proposee, jamais jouee ;
  - la reparation de la ligne L = 30 : aucune diagonalisation neuve.
  Rien, dans cette liste, ne porte le verdict ; tout y est nomme pour
  qu'aucune cloture ne puisse etre lue comme "plus rien devant".

83.16 CE QUE CET ACTE NE FAIT PAS
  Il ne tranche ni (b) ni (c) de 83.11, ni B_N, ni S-H, ni 83.8 : tous
  consignes OUVERTS, direction non prise, pour l'acte de conception M18.
  Il ne rejuge pas le verdict : PAS DE SIGNAL reste prononce par la
  cascade. Il n'instruit pas l'item 3 de la file. Il ne depose rien : le
  distant est a 1e940f9, tete inchangee par le present acte. Il n'ouvre pas M18 ; rien ne part vers Held
  avant sa consignation. Il ne prend aucun numero de manche. Il attribue
  E37, E38, E39, E40, E41, N-65, N-66, N-67, D-M17-36..43 et rien d'autre.
  Borne : 83.

EMPREINTES RE-DERIVEES LE 2026-08-25 (N-48), depuis un clone frais du
depot pour l'arbre, depuis l'archive et le complement pour le reste.
PIECES CITEES (16 hex ; detenteur declare) :
  au registre cd9ba37 : delta 82 14e44b01d74c8559 ; note de run
  fc905d9b195c2a76 ; certification gel v12-b2 de6f702f0d4b052e ; MANIFEST
  de manche 4aecd0e2b23bc818 ; assemblage 0be34834c78d1fcf ; delta 81 ;
  certification du delta 80 v2 ; certification m17 v10 ; bilan v2.
  archive (machine 2, MANIFEST c1e336a00647cf8a) : gel v12-b2
  20950e52e7d63225 58507 ; script v17 82a0be882568fe0c 103150 ; gels v9
  a5e86ca3191fb204, v10 96076b26be766304, v11 a4d8126f2cfd0879, v12
  4d4d2fae34ccb63b ; scripts v13 6ca5edc8d72a05cb, v14 01242ffdb8259ea3,
  v15 cedd270109b469c4, v16 a2081c7ee9b75683 ; certifications gel v10
  11eaf547481e7bce, v11 8810fe72d401c011, v12 883079ed8d1f69da ;
  certifications v15 e3524ffdc6e970f6, v16 c4038bcd0b82c7b0, RETRAIT v16
  85537791102f3ae1, v17 c344f55940a75772 ; pilote v17 9807908e0eb76aba ;
  sondes cf97c641db146ae4, 0cc590845d8fbf8c ; verif_clause_P7
  a9063716a6cbc2e6 ; temoins_P7.json 28a840cf73a18730 ; ordre
  5302f3a3a60af328 ; lecture be9f83d69f17725d ; reponse cause
  66f0915d95788912.
  complement (machine 2, MANIFEST 981c9dbcb99edad5) : contrecert v9
  2699f22f1c985d18 ; certification v10 ea93c063c6d69bf1 ; v11
  9209337b4c5d7c7a ; banc lourd v3 ab6abf4f3fc3e83d ; prevol v11
  56c96991c62d4c54 ; croisement sonde v3 1efd80ce3df81bba ; contrecert
  v14 5292c217db83449d ; bilan v1 935c4928388988b4 ; note v12 machine 1
  686ae74d3910d089.
  machine 1 (ce jour) : note reconciliation b4704e2ef81cef9b ; SUIVI
  2026-08-25 a4ba101d3e53d6c2 ; SUIVI-b 4cc4f0a29a0d8512 ; question file
  6c94f32c2abd81c5 ; demande d'archive ead69774e9031994.
  reponse file c05d7f15847f319a ; envoi archive 8c836535a745f8f6 ;
  certification du delta 83 v1 20417e08843f36b6 8702 o (copie recue ;
  instrument certif_delta_83_machine2_v1.py 0cd71b913a4c47e7 / .log
  271e76bfc2810828, detenteur machine 2) ; controle N-61 v2 du present
  acte, N61_acte83_v2.txt (joint).
Certification du present delta (v1, 20417e08843f36b6, et sa lecture de la
v2 a venir) : pieces a deposer avec lui.

=== FIN DU JOURNAL DELTA 83 ===
