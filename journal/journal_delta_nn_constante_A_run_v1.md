JOURNAL DELTA nn -- LE BANC DE LA CONSTANTE A A TOURNE, LES DEUX VOLETS, SUR UN
REGLAGE CHOISI PAR LE PRE-VOL ET NON A LA MAIN : LE VOLET T REND REGLAGE QUALIFIE
ET LE VOLET A REND NON CONCLUANT DE PLANCHER, LA BRANCHE QUE LE GEL AVAIT
PRE-ENREGISTREE ; P-alpha (alpha = 4/(p-2)) TIENT AUX TROIS DEGRES A MIEUX DE
2.8e-06, SUR LES DEUX MACHINES ; ET LA TENAILLE EST CHIFFREE -- IL FAUDRAIT UN
REGLAGE 17.5 FOIS PLUS PETIT QUE CE QUE LE VOLET T AUTORISE POUR QUE L'INSTRUMENT,
ET NON LE PLANCHER DU MODELE, FIXE LA TOLERANCE DE P-A, SI BIEN QUE LE CHEMIN VERS
A N'EST PAS UN REGLAGE MAIS UNE DERIVATION AU SECOND ORDRE ; TROIS DEFAUTS
D'INSTRUMENT BLOQUANTS SONT TOMBES, DONT AUCUN N'ETAIT VISIBLE EN PRE-VOL ET DONT
CHACUN RENDAIT SON CONTROLE IMPOSSIBLE A PASSER
(redaction machine 2, depot operateur, 2026-09-13) -- PROJET, VERSION 1
=======================================================================
S'insere apres le delta 90 (e68341f, journal_delta_90_constante_A_v2 11f86226cf4aa612).
NUMERO nn PRIS AU DEPOT : plafond a relever sur clone frais au moment du depot ; le
corps garde "nn" (le numero n'entre que dans le nom de fichier et le manifeste de
depot, forme (a) des deltas 88, 89 et 90). Aucun numero de serie (N, E, D) n'est pris
ici ; les defauts portent leurs etiquettes de chantier (D-v6-x, D-v7-1, D-v9-1,
D-v10-1, D-v11-1, D-v12-1, D-v13-1) et attendent l'attribution au depot (E18).
Classe du depot : 1. Aucune regle nouvelle ((X) jusqu'au 28/09) ; quatre regles
candidates neuves en nn.8, nees de faits payes ce jour.
Ce projet est de plume machine 2 ; il est a certifier par machine 1 en un tour avant
depot. Chaque nombre de cet acte est RELU A LA SOURCE (les deux JSON de run, ceux de
machine 1, les logs de mesure) par relecture_nombres_delta91_machine2_v1.py ; le
perimetre du depot est ENUMERE depuis les citations de cet acte
(perimetre_depot_delta91_machine2_v1.py). Aucune valeur de lecture n'est crue.
Moteur unique : m9_replication_v1.py c8ed357b120352c4, jamais edite (PB-1).

nn.0 POSITION EN TROIS PHRASES
  Le reglage de la fenetre a ete descendu de 1/102400 a 1/44100 par une regle
  declaree avant tout balayage -- le plus grand pas de l'echelle delta_0/n^2 dont le
  PRE-VOL du temoin ouvre la porte avec une marge d'au moins 1.15 -- puis les deux
  volets ont tourne sur les deux machines : le volet T rend REGLAGE QUALIFIE (bonus
  T-3 retire) avec les neuf cellules lues et le controle de reproductibilite a zero
  ecart, et le volet A rend NON CONCLUANT DE PLANCHER, branche 3b, celle que la
  cascade du gel avait ecrite d'avance. P-alpha tient aux trois degres, l'exposant
  mesure valant 4/(p-2) a 2.77e-06 pres au pire, et les deux machines s'accordent sur
  les trois verdicts de degre ; P-A tient a p = 5 et 7 et tombe a p = 4 d'un facteur
  1.13, mais sous une tolerance que le gel lui-meme declare etre celle du MODELE, si
  bien que ce n'est pas une refutation. La question que le banc posait -- l'instrument
  peut-il, seul, fixer la tolerance de P-A ? -- recoit une reponse chiffree : non, pas
  sur cette echelle, et il y manque un facteur 17.5 sur le reglage, borne par p = 7 ;
  comme le volet T interdit de descendre davantage, le chemin vers A n'est pas un
  reglage plus fin mais la derivation au second ordre du terme que le plancher
  represente.

nn.1 PIECES CITEES (convention B, sha256 NFC+LF, 16 hex ; "au registre" = dans
     l'arbre a e68341f, delta 90)
  Le gel et son instrument :
    constante_A_pre_enregistrement_v6.md      847bb3bb2dd19f87  (plume m1, NON CERTIFIE)
    constante_A_pre_enregistrement_v7.md      a2b8463372e1f906  GEL COURANT (v6 + 5 hunks)
    construction_gel_v7_machine2_v1.py        (la construction du v7, ancres uniques)
    certif_constante_A_v6_machine2_v1.py      (114 controles : v6 104/114, v7 114/114)
    banc_qualification_machine1_v8.py         4d8882a2223a5c74  au registre, CERTIFIE
    banc_qualification_machine1_v9.py         9b3ec0b0c4978158  (v8 re-parametre au v6)
    banc_qualification_machine1_v10.py        f65eccbfcdea91c1  (D-v9-1 levee)
    banc_qualification_machine1_v11.py        a9f3fa1d639107d2  (D-v10-1 levee)
    banc_qualification_machine1_v12.py        2c4345515bb02325  (D-v11-1 levee)
    banc_qualification_machine1_v13.py        1ac295648490a86c  (D-v12-1 levee) INSTRUMENT
    et les cinq scripts de construction, chacun a ancres uniques et asserees
    temoin_negatif_pre_enregistrement_v11.md  a2e7ef3e237c5acf  registre, GEL VOLET T
    erratum_temoin_v11_clause_7i_tolerance_v1.md      13601ef21efdc024  au registre
    enumeration_cles_prevol_N70_machine2_v3.md        bbd23a2ee3421da4  (avant le run)
    depot_9bis_temoin_v1.json                 c4310e33da6b9759  au registre
    runs/run_alpha_delta85/resultats_alpha.json       6d7d23130e9322f8  au registre
    runs/run_temoin_delta85/resultats_temoin.json     644240dc894c2733  au registre
    journal_delta_90_constante_A_v2.md        11f86226cf4aa612  au registre
  Les runs (les pieces qui portent le resultat) :
    machine 2, volet T, v12  out_run_delta91/temoin_v12/resultats_temoin.json
    machine 2, volet A, v12  out_run_delta91/alpha_v12/resultats_alpha.json
    machine 2, volet T, v13  out_run_delta91/temoin_v13/resultats_temoin.json
    machine 2, volet A, v13  out_run_delta91/alpha_v13/resultats_alpha.json
    machine 1, volet T, v13  out13_m1/temoin_v13/resultats_temoin.json
    machine 1, volet A, v13  out13_m1/alpha_v13/resultats_alpha.json
  Les feuilles de mesure et de lecture :
    mesure_9bis_tuple_machine2_v1.py / .log       D-v10-1, 11/11
    mesure_jumelle_machine2_v1.py / .log          D-v11-1, 20/20
    lecture_run_delta91_machine2_v1.py / .log     la lecture du run, 35/35
    certif_banc_v13_machine2_v1.py / .log         la certification du v13, 24/24
  Les lots du chantier, par leur ligne CANON :
    machine 2 : 435302fae671f4f8 (le reglage mesure) | f65529ea706a60d2 (gel v7, banc
      v10, N-70 v3) | 41208ad7ac1293cc (le run)
    machine 1 : e0dce16570a048cc (gel v6, banc v9) | 18e4fad746ece324 (contreseing du
      v7, certification du v10) | ddf2070bece83d93 (certification v11/v12, banc v13,
      son run) | 5baebae5a0ad22c5 (son releve de cloture du delta 90)

nn.2 LE REGLAGE -- CHOISI PAR LE PRE-VOL, PAS A LA MAIN
  (a) Le delta 90 avait laisse le reglage sous la borne inferieure de la tenaille :
      delta' = 1/102400 = 9.766e-06 contre INF = 1.659261e-05, et le pre-vol rendait
      branche 4 des deux cotes. La fenetre annoncee alors etait x1.0418 a m = 2.
  (b) Mesure du 12/09 au soir, contre cette fenetre : le rapport e/seuil ne croit pas
      comme delta mais comme delta^0.85 environ (0.684 a 9.77e-06 ; 0.907 a 1.74e-05 ;
      1.527 a 2.5e-05 ; 1.868 a 3.09e-05), de sorte que le seuil vrai du point porteur
      7|1.73 est vers 1.9e-05, AU-DESSUS de la borne superieure a m = 2. LA FENETRE A
      m = 2 EST DONC VIDE EN FAIT : l'invariance de e, mesuree sur une paire a x1024,
      ne tient pas a l'echelle fine. L'arbitrage du 29/08 -- la marge du volet A ou une
      marge cote T, pas les deux -- est ainsi tranche par la mesure : seule la marge
      cote T ouvre.
  (c) Et une troisieme machoire, que la tenaille ignorait : l'ORDRE LISIBLE (W-pas). A
      p = 7 la tolerance vaut 0.172 et l'ecart |p_obs - 4| va de 0.03 a 0.21 selon le
      pas, sans monotonie -- la porte y est marginale sur tout le domaine admissible.
      Aucune des trois machoires ne se derive au dixieme : le reglage se prend AU
      PRE-VOL.
  (d) Regle de choix, ECRITE AVANT le balayage (gel v7, 3.2) : delta' = delta_0/n^2, et
      n est le plus grand entier de l'echelle dont le pre-vol du temoin rend branche 5
      avec e/seuil >= 1.15 aux neuf points. L'instrument n'accepte que cette forme (il
      exige une racine entiere de delta_0/delta'). Balayage joue par machine 1 sur
      l'echelle entiere, n = 18 a 24, et complete par machine 2 a n = 23 :
        n = 18  1/32400  branche 5, e/seuil min 1.868
        n = 19  1/36100  branche 5, e/seuil min 1.631
        n = 20  1/40000  W-pas 7|2.27 MORD
        n = 21  1/44100  branche 5, e/seuil min 1.433   <- retenu
        n = 22  1/48400  W-pas 7|1.73 MORD
        n = 23  1/52900  branche 5, e/seuil min 1.113 (sous la clause (T))
        n = 24  1/57600  W-plancher 7|1.73 MORD
      n = 23 ouvre la porte mais sous la clause (T) : exclu, et exclu par une MESURE,
      non par une derivation. RESULTAT : n = 21, delta' = 1/44100 = 2.267574e-05,
      kT = 1.3666, m = 1.5247. Les deux marges sont partielles ; aucune n'est pleine.
  (e) Le gel v7 porte ce reglage, ses quatre tables re-derivees, et la clause qui
      re-ancre LD-16 sur le parametre du run depose (decision (i) du delta 90). Il est
      de plume machine 1 ; sa v6 n'etait pas certifiable (deux sections non re-derivees,
      nn.7) ; la v7 est certifiee 114/114 et contresignee par diff.

nn.3 LE VOLET T -- REGLAGE QUALIFIE
  Run reel, instrument v12 puis v13, gel v7, sur BOCAL4 ; et sous v13 sur machine 1.
    VERDICT   REGLAGE QUALIFIE (bonus T-3 retire)
              branche 6 : T-3 mord seul (W-integrales, T-3a)
    les neuf cellules de T-2 : W-pas PASSE et W-plancher PASSE, 9/9
    e/seuil de 1.433 (7|1.73) a 5.750 (4|2.80) ; max |p_obs - 4|/tol_ordre = 0.79
    controle de reproductibilite 9bis : 0 ecart, custody 4/4 ; W-comptes 41 + 0 == 41
    sur machine 1 (levier X86_V4) : meme verdict, 0 ecart et 7 feuilles tolerees a
      1 ulp, toutes de la classe EXPOSEE-LIBM (nn.6 d)
  CE QUI RETIRE LE BONUS : a l'etat A, l'integrale de N tombe sous le plancher machine
  et n'est PAS LUE (LD-16) ; W-integrales mord, et elle seule. Fait a consigner, et
  c'est une dette qui se reproduit : a l'etat B, q_int(N) = 4.9598, c'est-a-dire le
  meme 4.96 inexplique que le 28/08, retrouve a un reglage 441 fois plus fin.

nn.4 LE VOLET A -- NON CONCLUANT DE PLANCHER
  Run reel, porte lue par empreinte sur le fichier temoin (statut REEL), meme reglage.
    VERDICT   NON CONCLUANT DE PLANCHER
              branche 3b : G-plancher MORD aux degres [4, 5, 7]
    plan 18 POINT FIXE ; G-dt 18 ; G-k 18 ; seuil 9 AJUSTE ; les trois degres
      EXPLOITABLES ; aucune garde de resolution (G-dt, G-k, conversion 5.3 (iv)) ni de
      dependance (G-s, G-w2) ne mord
    P-alpha : alpha mesure contre 4/(p-2), tolerance du degre
      p = 4  2.0000025 a 2.0000028   ecart max 2.77e-06   tol 2.38e-05   VRAIE
      p = 5  1.3333340 a 1.3333341   ecart max 8.06e-07   tol 8.75e-06   VRAIE
      p = 7  0.7999999 a 0.8000005   ecart max 4.50e-07   tol 2.98e-06   VRAIE
    P-A : |ln(gA^(p-2)/K)| contre (p-2) x tol_lnA
      p = 4  ecart 2.571e-06   borne 2.268e-06   rapport 1.13   FAUSSE
      p = 5  ecart 1.808e-06   borne 4.710e-06   rapport 0.38   vraie
      p = 7  ecart 1.843e-06   borne 1.066e-05   rapport 0.17   vraie
    LES DEUX MACHINES : memes verdicts, memes P-alpha, P-A et G-plancher aux trois
      degres. Sur les cles numeriques de degre, UNE SEULE differe -- dispersion_lnA a
      p = 5, ecart relatif 3.2e-03 : la dispersion de lnA amplifie l'ulp des flots.
  CE QUE P-A A p = 4 NE VAUT PAS : la branche 3b est prononcee AVANT toute lecture de
  P-A, et la tolerance qui la juge est celle du MODELE (nn.5). Le rapport 1.13 n'est
  pas un ecart physique : c'est un ecart a une borne qui n'a pas encore de sens. P-A
  n'est ni tenue ni refutee par ce run.

nn.5 LA QUESTION DU BANC, ET SA REPONSE CHIFFREE
  La question, ecrite au gel depuis le v4 : la tolerance de P-A est-elle fixee par
  l'INSTRUMENT (la dispersion mesuree sur les six cellules d'un degre) ou par le
  MODELE (le plancher delta'/((alpha+2)(alpha+3)), terme neglige de la fenetre) ?
  tol_lnA = max(dispersion, plancher) ; G-plancher mord quand le plancher gagne.
    p    dispersion mesuree   plancher du modele   dispersion/plancher   qui fixe
    4    9.8534e-07           1.1338e-06           0.869                 le MODELE
    5    3.2607e-07           1.5699e-06           0.208                 le MODELE
    7    8.9160e-08           2.1312e-06           0.042                 le MODELE
  tol_lnA/plancher = 1.0 aux trois degres. L'instrument est DEVENU plus fin que le
  plancher du modele -- ce n'est pas une panne, c'est le contraire ; mais la mesure de
  A reste bornee par le modele, donc non concluante.
  DE COMBIEN. Pour que l'instrument fixe tol_lnA a un degre il faut
  delta' < dispersion(p) x (alpha_p + 2)(alpha_p + 3) :
    p = 4   delta' < 1.9707e-05    (facteur 20.0000)
    p = 5   delta' < 4.7099e-06    (facteur 14.4444)
    p = 7   delta' < 9.4867e-07    (facteur 10.6400)   <- le degre qui contraint
  Le volet T exige delta' >= INF = 1.659261e-05. LE RAPPORT EST 17.5. C'est le nombre
  que la campagne cherchait depuis le 29/08, et il est mesure des deux cotes au lieu
  d'etre estime d'un seul.
  ET IL EST PIRE QUE CELA, parce que la dispersion n'est pas fixe : entre le run du
  delta 85 et celui-ci (reglage 441 fois plus fin) elle a baisse d'un facteur 2.01,
  7.34 et 83.36 aux p = 4, 5, 7, soit des pentes en delta^0.114, delta^0.327,
  delta^0.726 (deux points, a prendre comme tels). A p = 4 -- le seul degre ou une
  fenetre existe a dispersion fixe, [1.6593e-05, 1.9707e-05], ou tombe n = 23 --
  l'extrapolation donne une dispersion de 9.65e-07 contre un plancher de 9.45e-07,
  c'est-a-dire une marge de DEUX POUR CENT a un seul degre : elle ne mesurerait rien.
  CONCLUSION, ET C'EST LE RESULTAT DE CE DELTA : le chemin vers A n'est pas un reglage
  plus fin. Le plancher est un terme de modele ; le derive au premier ordre et le
  soustraire laisse un residuel d'ordre delta' fois le plancher, soit 2.57e-11,
  3.56e-11 et 4.83e-11 aux trois degres -- sous la dispersion mesuree d'un facteur
  3.8e+04, 9.2e+03 et 1.8e+03. C'est la derivation au second ordre, non le reglage,
  qui ouvrirait les trois degres. Ce chantier precede tout gel v8.

nn.6 LES INSTRUMENTS -- TROIS DEFAUTS BLOQUANTS, ET CE QU'ILS ENSEIGNENT
  (a) D-v9-1 (banc synthetique) : au reglage neuf, la duree k tau_dom' devient plus
      petite que le pas de la grille de phase 1, et le synthetique du banc demarrait sa
      phase 2 a l'instant de bascule ARRONDI -- donc parfois A L'INTERIEUR de la fenetre
      d'ajustement, qu'il ne peuplait plus assez. Au reglage precedent, la fenetre
      restait couverte par coincidence de grille. Correctif v10 : arrondi vers le bas.
  (b) D-v10-1 (controle 9bis) : il comparait un OBJET PYTHON a une REFERENCE lue dans
      un FICHIER JSON. La serialisation change des types : un tuple devient une liste.
      Neuf cles du perimetre valent un tuple en memoire, si bien que la comparaison
      opposait (1.0, 0.0) a [1.0, 0.0] et mordait, valeurs identiques. Le JSON du run
      contre la meme reference par la meme marche : zero ecart. AUCUN RUN NE POUVAIT
      PASSER CE CONTROLE, un fichier JSON ne portant jamais de tuple. Correctif v11 :
      la comparaison se fait sur la SERIALISATION -- rien n'est relache, les valeurs se
      comparent toujours au bit.
  (c) D-v11-1 (trajectoire jumelle) : la jumelle de G-dt est jouee a pas moitie, et ses
      comptes d'etage doublent par construction ; le gel 4.8 le dit et derive ses
      intervalles. L'appel du run reel n'armait pas le parametre qui double ces
      intervalles : les dix-huit jumelles rendaient G-fen (comptes mesures 721 a 760
      contre [360, 381] au lieu de [720, 762]), les trois degres devenaient
      inexploitables, la cascade rendait branche 3. LA AUSSI, aucun run ne pouvait
      conclure. Le mecanisme existait dans le code et n'etait arme nulle part.
      Correctif v12 : l'armer a l'appel du run reel.
  (d) D-v12-1 (9bis entre machines) : la reference du 9bis est le run depose, produit
      sur BOCAL4. Sur BOCAL4 le controle passe PAR CONSTRUCTION ; sur machine 1 il mord,
      sept feuilles a UN ulp -- quatre tol_int, et aussi disp_y, tol_R,
      tol_R_sur_q_moins_1, c'est-a-dire des grandeurs que l'enumeration de la classe
      EXPOSEE-LIBM au gel ne nommait pas. Le gel v7 prescrit pourtant 2 ulp pour cette
      classe ; l'instrument comparait au bit. C'est l'issue (a) de N-70 -- la contrainte
      muette, "le run se joue sur machine 2" -- que le run a rendue visible. Correctif
      v13 (plume machine 1) : toute feuille flottante finie du perimetre se compare a
      2 ulp, les ecarts toleres sont ENUMERES au JSON et au journal ; entiers, chaines,
      booleens, longueurs et cles restent au bit.
  CE QUE CES QUATRE ENSEIGNENT, ET C'EST LE POINT DE METHODE DU DELTA : aucun n'etait
  visible en PRE-VOL. Le synthetique joue une seule phase et DECLARE ses gardes de
  compte non jouees ; le 9bis n'est pas arme sans son argument. Sept pre-vols de
  balayage, quatre certifications croisees, deux bancs de gardes a 56 scenarios sur 56
  : tous aveugles aux trois defauts bloquants. Et le troisieme ne s'est vu qu'une fois
  le deuxieme leve, le deuxieme qu'une fois le premier leve. SEUL UN RUN REEL LES
  MONTRE, ET UN SEUL RUN N'EN MONTRE QU'UN.

nn.7 DEFAUTS ET ERRATA
  Du gel (plume machine 1, trouves par la certification machine 2) :
  D-v6-1 (forme) le gel v6 emis differait de la sortie de son propre script de
         construction par un hunk MANUEL -- la table du balayage, collee en 3.2 -- alors
         qu'il declarait le script comme sa provenance. Le v9 avait ete epingle sur ce
         gel modifie. Verse au v7 par construction.
  D-v6-2 (forme) la ligne n = 23 du balayage disait "non joue", et son exclusion tenait
         a une marge DERIVEE ; jouee sur BOCAL4, elle ouvre la porte mais a 1.113,
         exclue par la clause (T) MESUREE. La regle rend le meme n, pour une autre
         raison, et la ligne devait le dire.
  D-v6-3 (FOND) la section 4.8 gardait les intervalles de la jumelle du reglage
         precedent (2 x 620) quand l'instrument derivait les nouveaux (2 x 400) : le gel
         et son instrument se contredisaient.
  D-v6-4 (FOND) la section 9 rapportait le bruit a l'ancien signal 1/1024 quand la
         ligne au-dessus disait 1/441 : trois colonnes de rapports non recalculees.
  D-v6-5 (forme) la section 11 comptait le volet T sous un gel temoin remplace.
  D-v7-1 (provenance, plume machine 1, OUVERT) les deux bornes "2.2e-04 a 1.6e-03" de
         la section 9 ne se retrouvent ni au registre ni dans les cles du run 85 ; la
         phrase se re-ecrira sur une source citee a la prochaine version du gel. Aucun
         verdict n'en depend (L-desc n'a ni branche ni tolerance).
  De l'instrument : D-v9-1, D-v10-1, D-v11-1, D-v12-1 (nn.6), tous LEVES.
  De la note de certification (plume machine 1, trouve par machine 2) :
  D-v13-1 (chiffre) le residuel du second ordre y est annonce a "5e-06 x plancher" et
         le gain a "1e+04 a 1e+05" ; la mesure donne delta' = 2.27e-05 fois le plancher,
         et un gain de 1.8e+03 (p = 7) a 3.8e+04 (p = 4). LA CONCLUSION TIENT LARGEMENT
         -- le second ordre ouvre les trois degres -- c'est le chiffre qui est faux.
  Contre machine 2, verses ici : la premiere version de la feuille qui MESURE D-v10-1 a
  mordu sur son propre controle, par la faute exacte qu'elle mesurait (une liste
  comparee a un tuple) ; la garde de la construction du v12 a compte le mot arme dans
  le commentaire qu'elle venait d'inserer ; la garde de relecture du ZIP a attrape deux
  manifestes de sortie aplatis au meme nom. Les trois ont mordu BRUYAMMENT : rien n'a
  ete emis. Une quatrieme, silencieuse, avait ete payee au delta 90 ; c'est la
  difference qui compte.

nn.8 REGLES CANDIDATES SOUS (X) -- revue 28/09, aucune n'est prise ici
  Les huit du delta 90 sont reconduites. Quatre naissent de ce jour :
  9.  UN PRE-VOL NE CERTIFIE PAS UN INSTRUMENT. Tout controle qu'un pre-vol declare NON
      JOUE doit avoir mordu au moins une fois sur un RUN REEL avant que l'instrument
      soit dit certifie -- sans quoi on certifie ce qui n'a pas ete joue. Trois defauts
      bloquants, sept pre-vols, deux bancs a 56/56 : la preuve est faite dans les deux
      sens (nn.6).
  10. UNE COMPARAISON SE FAIT SUR LA SERIALISATION, comme une empreinte. Comparer un
      objet en memoire a une reference lue d'un fichier compare deux representations :
      les types que la serialisation change mordent sans qu'aucune valeur ne differe
      (D-v10-1). Extension directe de la regle du 28/08 sur les empreintes.
  11. UNE TOLERANCE SE SONDE A SON BORD. Un banc qui perturbe une valeur de cent pour
      cent passerait avec une tolerance infinie : il ne borne rien. Toute tolerance
      neuve se sonde a n-1, n et n+1 de son unite (ici : 2 ulp toleres et enumeres,
      3 ulp mordent). Verifie sur le v13, et ce controle-la n'etait dans aucun banc.
  12. UN CONTROLE DE REPRODUCTIBILITE PASSE PAR CONSTRUCTION SUR LA MACHINE DE SA
      REFERENCE. Il n'y mesure rien ; il ne mesure que joue sur l'AUTRE machine. Un tel
      controle se declare donc avec sa machine de reference, et son premier jeu utile
      est ailleurs (D-v12-1). C'est l'issue (a) de N-70, jusqu'ici muette, rendue
      visible par un run.

nn.9 A ARBITRER PAR L'OPERATEUR, NON PRIS ICI
  (i)   La clause (T) a 1.15. Machine 1 recommande de NE PAS la relacher, et machine 2
        souscrit : 1.15 est le bas du besoin mesure ; l'abaisser pour ouvrir p = 4
        serait regler une porte sur le resultat qu'on veut voir ; et la fenetre ainsi
        ouverte vaudrait deux pour cent a un seul degre (nn.5).
  (ii)  Le chantier du second ordre : deriver le terme que le plancher represente, le
        soustraire, et refaire le banc. C'est le seul chemin mesure vers A. Il precede
        tout gel v8 et demande un arbitrage d'engagement, pas de reglage.
  (iii) Les numeros de serie (E18) en un bloc : D-v6-1..5, D-v7-1, D-v9-1, D-v10-1,
        D-v11-1, D-v12-1, D-v13-1, et les numeros encore en attente du delta 90.
  (iv)  L'erratum au gel v7 que D-v12-1 appelle : la classe EXPOSEE-LIBM est plus large
        que son enumeration (disp_y, tol_R en font partie, mesure). Forme de l'erratum
        7 (i) : il complete sans editer, et ne bouge pas le pin.
  (v)   La dette q_int(N) = 4.96, reproduite au reglage neuf et toujours inexpliquee.
  (vi)  Les deux pieces non detenues (128d0c0a, a6415de8), declarees non porteuses.

nn.10 CONSEQUENCES POUR LE REGISTRE
  - Le registre recoit le reglage et son histoire : le gel v6 non certifie et le gel v7
    courant avec leurs constructions et leurs certifications ; les cinq instruments v9 a
    v13 avec leurs scripts ; l'enumeration N-70 v3 deposee avant le run ; les six JSON
    de run des deux machines ; les feuilles de mesure des trois defauts et la lecture
    du run.
  - LE GEL COURANT de la constante A est le v7 a2b8463372e1f906 ; L'INSTRUMENT CERTIFIE
    est le v13 1ac295648490a86c ; le gel du volet T reste le v11 a2e7ef3e237c5acf avec
    son erratum 7 (i).
  - Le reglage depose devient delta' = 1/44100. Le run du delta 85 reste la reference du
    9bis ; il est a delta_0 et ne change pas.
  - Deux verdicts entrent : REGLAGE QUALIFIE (bonus T-3 retire) pour le volet T,
    NON CONCLUANT DE PLANCHER pour le volet A -- les deux sur les deux machines.
  - P-alpha est VERIFIEE aux trois degres au reglage neuf, ce qui prolonge la piste
    alpha du delta 85 d'un facteur 441 sur delta.
  - Rien de cet acte ne touche les manches M1-M17, la sequence R4/R5, ni la branche
    quantique.

nn.11 LE CANAL
  - Sept lots echanges en deux jours sur ce chantier, tous confirmes par canon des deux
    cotes, aucune perte. Les ZIP ne sont pas deposes (precedent non pris).
  - Un fait de transport verse par machine 1 : son premier rejeu a ete lance avec sa
    sortie DANS l'arbre recu, et l'instrument a versionne les repertoires (D-I-2) ; rien
    n'a ete perdu, les deux repertoires ont ete remis a leur nom et resolvent a leurs
    canons. La garde qui a evite la perte est celle que le gel prescrivait.
  - Les .log de machine 2 sont CRLF ; leurs deux empreintes et leurs deux tailles sont
    portees a chaque manifeste.

nn.12 CE QUE CE DELTA NE FAIT PAS
  Il ne mesure pas A : le banc rend une porte, pas une valeur. Il ne refute pas P-A : la
  tolerance qui la juge est celle du modele, et la branche 3b precede sa lecture. Il ne
  confirme pas le signal de L-desc, dont la portee reste a un seul sens. Il ne prend
  aucun numero de serie, ne recommande aucun delta, n'ouvre aucun chantier et n'edite
  aucune piece citee (PB-1). Il ne depose ni les ZIP ni MANIFEST.sha256. Il ne dit rien
  des manches, de la sequence R4/R5 ni de la correspondance.

nn.13 PIECES DE CE DELTA (lot machine 2 ; canon = convention B du manifeste)
  journal_delta_nn_constante_A_run_v1.md          cet acte
  perimetre_depot_delta91_machine2_v1.py / .log   le perimetre ENUMERE depuis les
                                                  citations de cet acte, et le
                                                  manifeste de depot qu'il DERIVE
  relecture_nombres_delta91_machine2_v1.py / .log les nombres de cet acte relus aux
                                                  sources (deux jambes)
  MANIFEST_DEPOT_deltann_machine2.txt             derive par la feuille de perimetre
  Les entrants sont ceux de nn.1 ; les feuilles de mesure, les constructions et les
  JSON de run entrent au depot avec leurs lots.

-- FIN journal_delta_nn_constante_A_run_v1 --
