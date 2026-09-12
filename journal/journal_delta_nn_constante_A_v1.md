JOURNAL DELTA nn -- LA CHAINE DE LA CONSTANTE A ENTRE AU REGISTRE : LE GEL v5
CERTIFIE (104/104), LE TEMOIN v11 CERTIFIE AVEC SON ERRATUM 7 (i), L'INSTRUMENT
v8 CERTIFIE (NEUF DEFAUTS LEVES), L'ENUMERATION N-70 v2 CONTRESIGNEE AU BIT ;
LE PRE-VOL REND BRANCHE 4 DES DEUX COTES ET LE RUN N'EST PAS LANCE ; LA
TENAILLE SUR delta EST DERIVEE ET RE-DERIVEE AU BIT PAR LES DEUX MACHINES
(1.659260768e-05 <= delta <= 1.728646463e-05 A m=2, FENETRE x1.0418, LE REGLAGE
COURANT EST SOUS LA BORNE) ; LE POINT QUI SUSPENDAIT LE BANC (7|1.73 NON
REPRODUIT AU BIT) A SA CAUSE NOMMEE, ENUMEREE ET REPRODUITE DANS LES DEUX SENS
(NOYAU SIMD DE numpy SUR MACHINE 1, NON CORRECTEMENT ARRONDI SUR 5 POUR CENT
DES APPELS) ET LA BORNE RETENUE NE LIT AUCUN NOMBRE DE MACHINE 1 ; TROIS
ERRATA, ONZE DEFAUTS, HUIT REGLES CANDIDATES ; LA PORTE N'A PAS BOUGE ET
AUCUN delta N'EST RECOMMANDE
(redaction machine 2, depot operateur, 2026-09-12) -- PROJET, VERSION 1
=======================================================================
S'insere apres le delta 89 (d037d21, journal_delta_89_R4R5_v5 c0f0f4f3b5477310).
NUMERO nn PRIS AU DEPOT : plafond releve sur clone frais lbaaz/SG_1 a HEAD
d037d21 le 12/09 = 89, aucun fichier delta_90, premier numero libre 90 ; le
corps garde "nn" (le numero n'entre que dans le nom de fichier et le
manifeste de depot, forme (a) des deltas 88 et 89). Aucun numero de serie
(N, E, D) n'est pris ici ; les defauts portent leurs etiquettes de chantier
(D-ACA-x, D-G2-x, D-I-x, D-v5-x) et les errata leur rang (1) (2) (3), tous
en attente d'attribution au depot si l'operateur en decide (E18). Classe du
depot : 1 (le chantier constante A est classe 1 : son instrument porte la
porte P-A) ; les lectures, derivations et le geste (2) se sont joues en
classe 3, regle (P). Aucune regle nouvelle ((X) jusqu'au 28/09) ; huit
regles candidates sont versees en nn.8 avec leur date de revue.
Ce projet est de plume machine 2 ; il est a certifier par machine 1 en un
tour avant depot. Chaque nombre de cet acte est RELU A LA SOURCE par la
feuille de relecture du lot de ce delta (relecture_nombres_delta90_machine2
_v1.py / .log : deux jambes, presence litterale dans l'acte ET recalcul ou
presence dans la piece citee) ; les nombres de la tenaille viennent d'une
feuille de mesure (derivation_fenetre_delta_machine2_v3, 22/22) dont le log
est reproduit AU BIT par machine 1 sur le fond re-livre ; aucune valeur de
lecture n'est crue. Le perimetre du depot n'est pas ecrit a la main : il est
ENUMERE depuis les citations de cet acte (perimetre_depot_delta90_machine2
_v1.py / .log) -- toute empreinte citee resout par canon au poste ou au
clone frais, et tout lot cite entre avec ses pieces de table.
Moteur unique : m9_replication_v1.py c8ed357b120352c4, jamais edite (PB-1).
Aucune piece citee n'est editee ; les versions remplacees sont conservees.

nn.0 POSITION EN TROIS PHRASES
  La chaine de la constante A -- gel v5 certifie par machine 2 (104/104),
  gel du volet T v11 certifie par machine 1 et complete par un erratum de
  tolerance a sa clause 7 (i), instrument v8 certifie apres neuf defauts
  leves en cinq versions, enumeration N-70 v2 des cles du pre-vol
  contresignee au bit sur machine adverse -- vivait entierement hors du
  registre, qui portait un temoin perime de quatre versions et un instrument
  perime de cinq : elle y entre par cet acte, sans qu'aucun run ait ete
  lance, parce que le pre-vol rend branche 4 des deux cotes (W-plancher mord
  a quatre des neuf points de T-2, tous a p = 7 sauf 5|1.73 sur le fil) et
  que le volet A n'ouvre que sur branche 5. Le reglage delta est pris en
  tenaille entre le volet A (delta <= 1.728646463e-05 a m = 2, exact) et le
  volet T (delta >= 1.659260768e-05, lecture conservatrice sur les JSON de
  machine 2), fenetre x1.0418 a m = 2 et kT = 1, vide des que kT >= 1.15 a
  m = 2 et vide partout a m = 3 ; le reglage courant delta' = 1/102400 =
  9.765625e-06 vaut 0.589 fois la borne inferieure, et le choix d'une marge
  -- celle du volet A ou une marge cote T, pas les deux -- reste a
  l'operateur. Le point qui suspendait le banc depuis le 29/08 -- 7|1.73, le
  seul point non lu qui differe entre les deux machines et le seul qui porte
  la borne, 0.759 chez machine 1 contre 0.684 chez machine 2 -- a sa cause :
  sur machine 1 la puissance de tableau numpy passe par un noyau SIMD AVX512
  non correctement arrondi sur cinq pour cent des appels, l'ecart est un
  nombre entier de basculements du dernier bit de l'etat (1, 2, 2, 0 aux
  quatre pas), et machine 1 reproduit machine 2 au bit (44/44) des que ce
  noyau est desactive ; la borne retenue est construite sur les ratios de
  machine 2 seuls, la jambe de mutation le mesure, et le doute qui empechait
  de conclure tombe en faveur de la valeur deja utilisee.

nn.1 PIECES CITEES (convention B, sha256 NFC+LF, 16 hex ; les lots par leur
     ligne CANON = empreinte B de leur manifeste ; "au registre" = deja dans
     l'arbre a d037d21, verifie par canon sur clone frais)
  Gel de la constante A (plume machine 1) :
    constante_A_pre_enregistrement_v3.md      d71770d5948fe1aa  REMPLACE par v4
    constante_A_pre_enregistrement_v4.md      011c923203fcdaef  REMPLACE par v5
    constante_A_pre_enregistrement_v5.md      2c0d2dc86054838c  GEL COURANT
      lot machine 1 d5ace962a3a6e413 (09/09)
    note_machine2_certification_constante_A_v4_v1.md  9e6376f936708077
      (96 controles, 95 passent, 1 MORD : P-A-1)
    certif_constante_A_v3_machine2_v1.log     a92f60f936a2f75a  (B ; CRLF)
    CERTIFICATION_machine2_constante_A_v5_v1.md       df0431a0a57cc2b6
      (VERDICT CERTIFIE, 104/104 ; lot 13d2973b0e143a20, 10/09)
  Gel du volet T (temoin negatif) :
    temoin_negatif_pre_enregistrement_v7.md   8b083e9f109b5a8e  au registre
    temoin_negatif_pre_enregistrement_v9.md   403488b4f6c319e9  SUPERSEDED
    temoin_negatif_pre_enregistrement_v11.md  a2e7ef3e237c5acf  GEL DU VOLET T
    note_machine1_certification_temoin_v11_v2.md      7fc5f2412b99ad50
      (VERDICT CERTIFIEE)
    depot_9bis_temoin_v1.json                 c4310e33da6b9759  CLOS avec la v11
    erratum_temoin_v11_clause_7i_tolerance_v1.md      13601ef21efdc024
      (complete la v11 sans l'editer ; rang (1) en nn.6)
  Instrument du volet T (plume machine 1, controle machine 2) :
    banc_qualification_machine1_v3.py         5fae2a8c94cf8685  au registre
    construction_banc_v4_machine1_v1.py       35b9ff3b8e5b7ef0  v3 -> v4
    banc_qualification_machine1_v4.py         36a3f06f19871c38  PIN v4
    construction_banc_v5_machine1_v1.py       81730d2bf7095c1f  v4 -> v5
    banc_qualification_machine1_v5.py         b8a0f75323182e55  (D-I-3)
    banc_qualification_machine1_v6.py         56c2ebfcfd84671e
    banc_qualification_machine1_v7.py         9a6e8b6192d4f163
    banc_qualification_machine1_v8.py         4d8882a2223a5c74  CERTIFIE
    note_machine1_livraison_banc_v5_v1.md     be633ae91ae295b5
    note_machine2_controle_instrument_v8_v1.md        2a618ffb180ea568
      (VERDICT CERTIFIEE ; selftest 103/103)
    note_machine1_cloture_cycle_contre_derivation_N70_v1.md  aa98fa8b4ba921d8
    SUIVI_campagne_2026-08-28b.md             b6d13e6a1559e850  (objet de (v))
    SUIVI_campagne_2026-08-29a.md             d0747b01700e4ad8
  N-70, enumeration des cles du pre-vol (plume machine 2) :
    enumeration_cles_prevol_N70_machine2_v1.md        4ef8235b16f26210  SUPERSEDEE
    enumeration_cles_prevol_N70_machine2_v2.md        4867dffe3392dea6
      (reproduite AU BIT par machine 1 sur sa machine)
    la chaine transmise le 09/09 : lot machine 2 a4c35a2ee691c9a7 (8 pieces)
  Pre-vols de l'instrument v8, mode temoin :
    m2_v8_prevol_temoin_resultats.json        0a24121e441cc0c3  (29/08, BOCAL4)
    m2_v8_prevol_temoin.log                   1a66059068654b4b
    prevol_temoin_v8_machine1.log             c45ac9f59907fbf4  (28/08, a NOYAU)
    resultats_temoin_prevol_noyau_machine1.json       d3417a81e03b2861  (12/09)
    resultats_temoin_prevol_libm_machine1.json        95acd5d9c844eacc  (12/09)
      lot machine 1 ca5456d3b11df0be
  Runs deposes du delta 85 (au registre) :
    runs/run_temoin_delta85/resultats_temoin.json     644240dc894c2733
    runs/run_alpha_delta85/resultats_alpha.json       6d7d23130e9322f8
    journal/m2_run_temoin_reel.log   B 10a7ce5688f515d5  brut 3833ba551a390945
    journal/m2_run_alpha_reel.log    B 0e7e56006d2e200a  brut 717b61caa5921aaa
  La tenaille (plume machine 2 ; feuilles de MESURE) :
    derivation_fenetre_delta_machine2_v1.py   7b7e388a562e5a8b  (lot 7883311c6e363b02)
    derivation_fenetre_delta_machine2_v2.py   9d9e949ed876424f  (lot e3b707c589e9d1d8)
    derivation_fenetre_delta_machine2_v3.py   4353c80e60cef87c  (lot 56378e0f371f9681)
    derivation_fenetre_delta_machine2_v3.log  f60104c0c3ba7ec4  (B ; reproduit au
      bit par machine 1, lot be5ee780388d1965)
    precision_de_la_borne_machine2_v1.py      5231ce763b007399  (lot cd70cda556d60380)
    DOSSIER_ARBITRAGE_constante_A_operateur_v1.md     cbf120b4113bc8b1  (lecture)
  Le geste (2) -- convergence en dt a 7|1.73, cause, carte des classes :
    machine 1 : 2b155abffbe4f6ff (mesure : convergence_dt_7_1p73_machine1_v1.json
      c8d86e5e5b4fd745, note a826546552c3ae77) | 117bcfaa1f283059 (cause + erratum
      a la note v1) | 5ea2fa8d7457a125 (reponse cas durs, exposition, script v2) |
      ca5456d3b11df0be (rejeu du banc sans noyau, neuf cellules, note
      950feb280cbcd92e) | 4cb991ce22ca35d0 (cloture, note 6fbd0785accc5689) |
      1859bbc126bb52c7 (erratum de cloture D-G2-4, note 1f80e0e9b88f2ff2)
    machine 2 : eb7fb1cefbf2cec4 (rejeu BOCAL4) | f9e1c1922e32220d (cas durs BOCAL4)
      | 3675daba802cbc6c (reponse globale) | 7883311c6e363b02 (comparaison a trois
      be8aad100ff77f52, erratum 19f6b47b930591cf, derivation v1) | cd70cda556d60380
      (cloture, precision de la borne)
  Les trois tours du 12/09 sur l'acte :
    machine 2 : e3b707c589e9d1d8 (ouverture : dossier, derivation v2, relecture v1
      6e1409b06e887d97) | 56378e0f371f9681 (derivation v3, controle croise
      15b0bc7915c82bd7, verification 28b 9965d3795d226b9a) | 1985ad4eea984bf5
      (verifications de sa lecture v1 2121738de50e2324) + erratum au manifeste
      2304eec6aba3545b | 5c84c48e9a9c72eb (cloture du tour ; verifications v2
      412c6bb0a4c6d7b7)
    machine 1 : b228e0f5a0197494 (lecture de l'ouverture ; le 28b retrouve) |
      25b6f78bdf2ddcff (lecture de la reponse ; R-G2-5 v1 sur clone frais) |
      990a8fe5cec6ef87 (R-G2-5 v2 1c93be84b611e43b ; garde be6bb447da1f4363)
  La re-livraison du fond et son rejeu :
    lot machine 2 RELIVRAISON d0ab94382e1b5808 (158 pieces ; ZIP brut
      bb9a94f13a2ed2cc, non depose) ; feuille d'assemblage v2 df3bd37cbca40c36
    lot machine 1 be5ee780388d1965 (rejeu : derivation v3 au bit, relecture v1
      39/39, R-G2-5 v2 sur le v8 42/9/6)
  Etat du 09/09 : lot machine 2 R2 7ee2d2d4fc0b27a1 (l'etat exact de la constante
    A, verifie sur pieces : le registre a cinq crans en arriere)
  Lacune du delta 89 (D-CERT-6) : lots machine 2 de certification v3
    bdd00189e68b61dc et v4 704f2b6b84f4c6a0, dont seules les notes sont au
    registre ; leurs feuilles entrent ici (nn.7).
  Non detenues, non porteuses, declarees : 128d0c0a (derivation fenetre T-2,
    piece de travail du 09/09) et a6415de8 (lot v9) ; citees par aucune
    mesure, aucun gel, aucun acte.

nn.2 LA CHAINE : GEL, TEMOIN, INSTRUMENT, N-70 -- CE QUI ENTRE AU REGISTRE
  (a) Le gel de la constante A a trois versions. La v3 (d71770d5948fe1aa) est
      declaree remplacee par la v4 (011c923203fcdaef), qui se disait "brouillon,
      devient gel a la certification machine 2" : la certification machine 2 du
      v4 (9e6376f936708077) rend 96 controles, 95 passent, 1 MORD -- P-A-1, une
      empreinte brute (celle du log certif_constante_A_v3, a92f60f936a2f75a en B)
      citee non signalee dans un bloc declare convention B. La v5
      (2c0d2dc86054838c, lot d5ace962a3a6e413) solde la morsure par un seul
      hunk de fond ; la certification machine 2 du v5 (df0431a0a57cc2b6, lot
      13d2973b0e143a20) rend 104 controles, 104 passent, 0 mord : VERDICT
      CERTIFIE, la v5 est le GEL COURANT de la constante A. Un defaut de
      l'instrument de certification y est verse contre machine 2 : le controle
      M du v4 testait la PRESENCE de l'empreinte brute, jamais son SIGNALEMENT ;
      reecrit, il mord sur le v4 et passe sur le v5.
  (b) Le gel du volet T est la v11 du temoin negatif (a2e7ef3e237c5acf),
      certifiee par machine 1 (7fc5f2412b99ad50, VERDICT CERTIFIEE) ; la v9
      (403488b4f6c319e9) est superseded, certifiee, non editee ; le depot 9bis
      (c4310e33da6b9759), attache a la v11 par sa cle gel, prend le meme verdict
      et vaut CLOS. Le registre portait les v5, v6, v7 (la v7 8b083e9f109b5a8e
      est la derniere deposee). L'erratum a la clause 7 (i)
      (13601ef21efdc024) COMPLETE la v11 sans l'editer : le tirage est
      identique au bit, le champ et D'' a 2 ulp en pas representables, au-dela
      W-transcription MORD -> BANC NON JOUE ; les deux bornes valent 2 pour des
      raisons differentes et leur regime est declare MESURE, NON PROUVE.
  (c) L'instrument du volet T est passe de la v3 deposee (5fae2a8c94cf8685) a
      la v8 (4d8882a2223a5c74) en cinq versions, la provenance epinglee par
      deux scripts de construction (v3 -> v4 par 35b9ff3b8e5b7ef0, 53
      remplacements, PIN 36a3f06f19871c38 ; v4 -> v5 par 81730d2bf7095c1f, 24
      remplacements Q01..Q24), reconstruction AU BIT par machine 2. Neuf
      defauts D-I-1 a D-I-9 ont ete leves ; le v8 est CERTIFIE par machine 2
      (2a618ffb180ea568, selftest 103/103) ; le SUIVI 29a (d0747b01700e4ad8)
      et la cloture de machine 1 (aa98fa8b4ba921d8) le consignent. D-I-3, la
      seule bloquante, est nommee en nn.7 parce qu'elle vaut une regle.
      D-v5-1 (LD-16 sans c_pl) reste OUVERTE : nn.9 (i).
  (d) N-70 : l'enumeration des cles du pre-vol (v2, 4867dffe3392dea6) part au
      depot AVANT tout run du volet T. Perimetre au run 245 = perimetre de la
      reference deposee ; 238 predites identiques, 3 exemptes, 4 non predites
      (les quatre cles tol_int a appel libm), 2 predites absentes (regle
      d'emission conditionnelle derivee, 16 groupes sur 16 : ecart_a_4 est
      emise si et seulement si l'integrale est lue, MORD comptant comme LUE).
      La v2 est contresignee aux deux forces : ensembles egaux (annexe A
      parsee contre la derivation de machine 1) et reproduction AU BIT sur
      machine adverse -- une piece de controle qui ne calcule pas est
      bit-reproductible par construction. La v1 (4ef8235b16f26210) portait 247
      cles et une classe de moins ; elle est conservee.
  (e) Le registre etait a cinq crans en arriere (etat R2 du 09/09,
      7ee2d2d4fc0b27a1, verifie contre origin/main) : gels du temoin v5/v6/v7
      pour un gel qui fait foi v11 ; bancs v1/v2/v3 pour un instrument
      certifie v8 ; aucune version du gel de la constante A ; ni N-70, ni
      l'erratum 7 (i), ni le depot 9bis. Cet acte les depose tous, versions
      remplacees comprises.

nn.3 LE PRE-VOL ET LA PORTE
  Le pre-vol de l'instrument v8 en mode temoin (0a24121e441cc0c3, 29/08,
  BOCAL4 ; c45ac9f59907fbf4, 28/08, machine 1) rend des deux cotes :
    verdict  NON CONCLUANT D'INTEGRATEUR
    branche  4 : W-plancher 5|1.73, W-plancher 7|1.73, W-plancher 7|2.27,
             W-plancher 7|2.80 MORD  (4 des 9 points de T-2 NON LUS)
    comptes  41 comptes, 0 saute, 41 attendus ; 0 faute de pre-vol
    C(p)     7.7143 (p = 4), 8.3158 (p = 5), 8.8966 (p = 7)
  Le volet A ne joue que si le volet T rend REGLAGE QUALIFIE, branche 5 du gel,
  elle seule. T-2 est analytique et tourne pour de vrai en pre-vol : la porte
  n'est pas un artefact du factice, elle est une mesure, faite deux fois. Le
  run n'est donc pas lance, et il n'est pas restreint aux cellules qui passent :
  les quatre non lues sont tout p = 7 plus 5|1.73 (ratio 0.991, sur le fil),
  et 7|1.73 porte la borne inferieure de la tenaille -- l'ecarter ne
  nettoierait pas le run, cela supprimerait la contrainte qui decide.
  Le prealable de portee a un pre-vol : il n'asserte que ce que son moteur
  factice determine, et ses sorties s'ecrivent AVANT tout assert (JSON,
  MANIFEST, NE-JOUE-PAS, custody) -- c'est la forme du v8.

nn.4 LA TENAILLE SUR delta -- DERIVEE, RE-DERIVEE AU BIT, ET SES DEUX ECHELLES
     VERIFIEES AVANT USAGE
  (a) La contrainte a deux cotes n'avait jamais ete ecrite comme telle. Feuille
      derivation_fenetre_delta_machine2_v3 (4353c80e60cef87c), 22 lignes, toutes
      capables de mordre, dont une conjonction (D-ACA-3) ; log f60104c0c3ba7ec4
      reproduit AU BIT par machine 1 (73 lignes, 0 differente) sur le fond
      re-livre, si bien que les comptes sont ceux des deux machines.
      volet A (exacte, aucune extrapolation ; portee par p = 5) :
        m = 1  delta <= 3.457292925e-05
        m = 2  delta <= 1.728646463e-05
        m = 3  delta <= 1.152430975e-05
      volet T (quatre lectures, la plus dure retenue ; portee par 7|1.73 aux
      quatre) :
        machine 1, son run a NOYAU     delta >= 1.286193025e-05  (x1.3171)
        machine 1, son run a LIBM      delta >= 1.427322916e-05  (x1.4616)
        machine 2, mes ratios          delta >= 1.427322916e-05  (x1.4616)
        CONSERVATRICE (e = min)        delta >= 1.659260768e-05  (x1.6991)
      RETENUE : INF = 1.659260768e-05, definie INF = max(borne(R_MOI, True))
      sur les ratios de machine 2 seuls (sa lecture LIBM et la mienne rendent
      le MEME nombre, les neuf ratios identiques au bit).
      carte (m = marge volet A, kT = marge volet T ; D-t-25 a mesure
      b = 1.15 a 1.74, kT = 1 est le cas le plus permissif defendable) :
        kT    |      m=1       m=2       m=3
        1.00  |  x2.0836   x1.0418      VIDE
        1.15  |  x1.8119      VIDE      VIDE
        1.30  |  x1.6028      VIDE      VIDE
        1.50  |  x1.3891      VIDE      VIDE
        1.74  |  x1.1975      VIDE      VIDE
      reglage courant : delta' = 1/102400 = 9.765625e-06, soit 0.589 fois INF
      -- SOUS la borne inferieure. Aucun barreau de l'echelle b = 4 depuis
      1/100 ne tombe dans la fenetre (J = 5 trop bas, J = 4 trop haut meme a
      m = 1) : ce n'est pas la physique qui exclut le recouvrement, c'est le
      choix de l'echelle.
  (b) Les deux echelles sont verifiees, pas supposees. Le plancher va en
      1/delta : R mesure suit la forme fermee D-t-22 aux neuf points (ecart max
      7.33e-07), dont tau_CAP est en sqrt(delta) PAR CONSTRUCTION (banc,
      tau_cap : forme fermee, le rapport 32 = sqrt(1024) exact a 0.00e+00 en
      est la signature, pas une mesure). L'erreur e est invariante en delta a
      la dispersion pres : entre le run delta_0 depose et le pre-vol delta',
      facteur 1024, le rapport e(delta')/e(delta_0) tient dans
      [0.9367, 1.1625] ; c'est cette dispersion qui fixe la marge. Donc
      ratio proportionnel a delta. (Une premiere version supposait dt2 ~ sqrt(delta)
      et concluait ratio ~ delta^3 : fausse, le nombre de pas ne change pas.)
  (c) La borne retenue ne lit aucun nombre de machine 1, et c'est une MESURE :
      la chaine qui mene a INF est appelee deux fois, sur ses JSON recus puis
      sur des copies dont tous les ratio_seuil et tous les e sont mutes (x3 et
      x0.5) ; INF sort inchange au bit (3ef1660b5147653b), le porteur
      inchange, et la mutation deplace bien sa lecture affichee
      (1.286193025e-05 -> 4.287310084e-06) -- sans ce troisieme controle la
      jambe ne prouverait rien.
  (d) D-G2-4, appliquee ici : la v1 (7b7e388a562e5a8b, relue ligne a ligne par
      machine 1) lisait les ratios e/seuil dans les journaux, a trois decimales
      ; la v3 les lit au champ /T2/points/<pt>/ratio_seuil des JSON, et le
      champ porte bien la grandeur que le log tronque (ratio_seuil ==
      e(dt2/2)/seuil_5_4 au bit, 9/9 ; arrondi a trois decimales il retrouve
      les deux journaux 9/9). INF passe de 1.659725811e-05 a 1.659260768e-05,
      ecart relatif 2.8027e-04 contre une marge de 4.1817e-02 (149 fois plus
      petit) ; aucune des 15 cellules de la carte ne change de statut ; la
      fenetre a m = 2, kT = 1 passe de x1.0415 a x1.0418. Correction de forme,
      gratuite, appliquee a l'endroit ou la borne est citee.
  (e) Ce que la tenaille N'EST PAS : un gel. Elle est une derivation de classe
      3, relue par les deux machines ; aucun delta n'en sort.

nn.5 LE GESTE (2) -- LA CAUSE DU 7|1.73, LA CARTE DES CLASSES, R-G2-5
  (a) Le point. Le pre-vol de machine 1 du 28/08 rend e/seuil = 0.759 a 7|1.73,
      BOCAL4 0.684 : ecart 11.0 pour cent, pres de trois fois la largeur de la
      fenetre (4 pour cent) qu'il devait trancher. Machine 1 a joue la
      convergence en dt (dt2, dt2/2, dt2/4, dt2/8 ; c8d86e5e5b4fd745), machine
      2 l'a rejouee sur BOCAL4 : deux rejeux au meme poste sont identiques au
      bit (le mot "bruit" est retire), l'erreur se pose sur un plateau de
      plancher des dt2/4, l'ordre reste NON LU aux deux postes, et au pas le
      plus domine par le plancher (dt2/8) les deux plateformes sont identiques
      au bit sur cinq grandeurs : ce n'est pas du bruit.
  (b) La cause, nommee par machine 1 (lot 117bcfaa1f283059) et confirmee par
      machine 2 (3675daba802cbc6c) : sur machine 1 (Linux, Xeon AVX512,
      numpy 2.4.4, niveau de dispatch X86_V4) l'operateur ** sur un tableau
      numpy est
      calcule par un noyau SIMD non correctement arrondi sur 5.2 a 5.5 pour cent
      des appels de base = g (x1 + x2) ** 6, biais -1 ulp ; sur BOCAL4
      (Windows, numpy 2.2.6) le meme ** passe par le pow de la libm UCRT,
      correctement arrondi sur tous les appels de ces flots. Les appels mal
      arrondis sont presque tous absorbes par l'arrondi de l'etat ; ceux qui
      basculent son dernier bit sont comptes et nommes (une combinaison a dt2,
      un seul appel a dt2/2 -- x = 1765.6704444885254, pas 707 sur 760, qui
      porte a lui seul tout l'ecart 0.759 / 0.684 --, deux a dt2/4, aucun des
      633 a dt2/8) et font 1, 2, 2, 0 ulp de x1 a tau_CAP. Avec le noyau
      desactive (NPY_DISABLE_CPU_FEATURES=X86_V4) machine 1 rend les 44
      grandeurs de flot du geste AU BIT de machine 2. Ce n'est pas la version
      de numpy qui decide (numpy 2.2.6 sur son conteneur rend le meme temoin) :
      c'est le couple roue x dispatch, active par le CPU. Le temoin executable
      : (1765.6704444885254) ** 6 rend ...9c5 sous le noyau et ...9c6
      correctement arrondi ; BOCAL4 rend ...9c6 pour power, exp et arctan2, la
      roue Windows n'embarquant de noyau SIMD pour aucune des trois.
  (c) La comparaison a trois (be8aad100ff77f52) : 856 feuilles de chaque cote,
      856 communes ; sur les 82 feuilles ou les deux runs de machine 1
      different, le pre-vol BOCAL4 egale son run LIBM sur 77 et son run NOYAU
      sur 0, les cinq restantes etant trois durees, une date et l'empreinte du
      champ de forces ; les neuf ratios e/seuil egalent son run LIBM au dernier
      chiffre. Deux faits neufs : le champ de forces de T-3 a TROIS valeurs
      (0491b83e6893dbbf noyau, f150f2685187b9d2 libm glibc, f7f8be507eb5e9cb
      BOCAL4), il traverse le noyau et la libm ; et hors des exposees, 14
      feuilles sur 774 divergent a un ulp entre glibc et UCRT, dix tolerances
      (tol_int, tol_ordre) et quatre meta. Consequence mesuree pour le 9bis :
      entre machines il compare a tolerance ou il exempte ; il ne peut pas
      exiger le bit, meme noyau desactive.
  (d) La carte des classes, re-etablie AU BIT a T-2 sur les JSON (lettres
      retirees a la plume de machine 1 pour ne pas collisionner avec les issues
      (a)(b)(c) de N-70) :
        EXPOSEE (noyau contre libm, machine 1)   9/9 cellules : 3 grossieres
          (4|1.73, 4|2.80, 7|1.73), 3 fines (4|2.27, 5|1.73, 5|2.80), 3 a ratio
          egal mais etat different (5|2.27, 7|2.27, 7|2.80)
        EXPOSEE-LIBM (BOCAL4 contre machine 1 sans noyau)   tol_ordre et
          tol_ordre_sur_1 a un ulp (1.6e-16 relatif) aux trois cellules p = 7 ;
          le
          champ de forces ; meme famille que les quatre tol_int de N-70
        ABSORBEE   VIDE comme classe de cellule (0 des 9 intacte ; x_b_num
          differe sur 7 des 9, ratio_seuil sur 6 des 9) : l'absorption vaut par
          FEUILLE, en aval, dans le ratio ; tau_CAP identique 9/9
        NON SEPAREE   T-1, T-3 hors champ, algorithme_vs_moteur : jumeau non
          construit
      Les six cellules qui different au bit (ecart relatif) :
        4|1.73 (2.3e-02)   4|2.27 (1.4e-08)   4|2.80 (4.7e-02)
        5|1.73 (4.1e-09)   5|2.80 (4.3e-10)   7|1.73 (1.1e-01)
      La separation gros/fin est nette (aucune entre 1e-07 et 1e-02) ; les
      six s'annulent contre le run LIBM, donc les six sont du noyau. Compte
      juste : SIX au bit dont QUATRE lues ; TROIS a la resolution du journal
      dont DEUX lues ; le porteur 7|1.73 reste la seule grossiere qui ne soit
      pas lue.
  (e) R-G2-5, le perimetre expose, ENUMERE et non ecrit (feuille de machine 1,
      v2 1c93be84b611e43b, arbre syntaxique, heuristique statique declaree) :
      sur le clone frais d037d21, 91 fichiers .py, 545 puissances ** dont 232
      EXPOSABLES dans 41 fichiers, le coeur du moteur compris
      (m9_replication_v1.py:324) ; sur le v8 certifie, 57 puissances dont 42
      EXPOSABLES, 9 CARRE, 6 CONST (36 au v3 depose). Une EXPOSABLE est une
      ligne A TYPER, pas une ligne exposee : le type de la base a l'execution
      n'est pas decidable statiquement. Les runs deposes viennent de BOCAL4
      (libm UCRT) ; tout rejeu sur machine 1 porte le temoin d'arrondi ou joue
      avec le levier d'environnement, par usage (nn.9).
  (f) Ce que le geste (2) ne change pas : la borne (nn.4 c), la porte (nn.3).
      Ce qu'il change : le doute sur la borne, et deux cellules LUES (4|1.73,
      4|2.80) qui differaient entre machines depuis le 28/08 sans que personne
      ne les compare au bit.

nn.6 LES TROIS ERRATA, NUMEROTES AU MEME GESTE ; LE FAIT DE FORME DE (v)
  (1) Erratum a la clause 7 (i) du gel v11 (13601ef21efdc024, plume machine 2)
      : la clause exigeait "le meme champ de forces sur un tirage declare" sans
      dire a quelle tolerance ; l'omission a coute trois versions d'instrument
      (D-I-5, D-I-6, D-I-7). Le regime est fixe (nn.2 b), MESURE, NON PROUVE ;
      le gel n'est pas edite.
  (2) Erratum du "seul point" (plume machine 2, feuille 19f6b47b930591cf, puis
      sa propre correction en nn.5 d) : la feuille de tenaille v1 portait "c'est
      le SEUL point non bit-reproductible de la campagne". FAUX : au journal
      trois cellules sur neuf different, dont deux lues ; au bit six, dont
      quatre lues. Portee exacte : 7|1.73 est le seul point NON LU qui differe
      au journal, et le seul qui porte la borne. La faute de forme est la vraie
      : l'affirmation vivait dans le champ de detail d'un chk qui testait
      l'ecart du porteur ; ecrite en condition elle mordait des le 29/08. Le
      compte "trois" de l'erratum avait lui-meme ete etabli sur les logs
      (deuxieme instance de D-G2-4 le meme jour).
  (3) Erratum au manifeste du lot 1985ad4eea984bf5 (2304eec6aba3545b, plume
      machine 2, D-ACA-6) : ses lignes "entrants" et "bilans" etaient celles du
      lot precedent, par substitution silencieuse (str.replace sans cible ne
      signale rien). Le manifeste emis n'est pas edite ; l'erratum porte les
      deux lignes justes et le canon 1985ad4eea984bf5 reste opposable.
  Fait de forme, objet de la decision (v), section 2 du SUIVI 28b
  (b6d13e6a1559e850, cite a la provenance du gel v5 l.587) : les deux captures
  des runs du delta 85 sont deposees en octets CRLF (91 et 154 CR ; brut
  3833ba551a390945 et 717b61caa5921aaa) et citees a l'acte 85 sous convention
  B (10a7ce5688f515d5, 0e7e56006d2e200a) ; le sha256 direct ne reproduit pas
  la citation, la transformation CRLF -> LF la reproduit exactement. Verifie
  au poste (9965d3795d226b9a, 19/19). La pratique des deux machines est deja
  la lecture (b) -- deux empreintes, deux tailles a chaque manifeste -- mais
  la clause d'ecriture n'est dans AUCUN texte (0 sur 771 .md chez machine 2,
  0 sur 207 au registre chez machine 1) : elle est la candidate 4 de nn.8. Le
  numero de ce fait de forme est a l'operateur (E18).

nn.7 DEFAUTS ET LACUNE REPRISE
  De l'acte et de ses tours (12/09 ; sept defauts numerotes, cinq de machine
  2, deux de machine 1, TOUS trouves par l'autre machine ou par un outil de
  l'autre machine, aucun par celui qui l'avait commis) :
  D-ACA-1 (m2 ; forme) un chk a condition litterale True dans derivation v2
          (l.161) : aucune issue ecrivable ne le fait mordre ; corrige en v3
          (le rapport 32 a 1e-12, puis la proportionnalite conditionnee) ; la
          v2 valait "21 lignes dont 20 controles".
  D-ACA-2 (m1 ; fond) sa carte des classes du geste (2) etablie a la mauvaise
          granularite (le journal pour e/seuil, les basculements de x1 pour
          l'absorption) : son controle croise, joue par machine 2 sur les JSON
          (15b0bc7915c82bd7, 15/15), rend "0 basculement net" FAUX et la classe
          ABSORBEE VIDE a l'echelle de la cellule ; carte re-etablie au bit
          (nn.5 d).
  D-ACA-3 (m2 ; prose) docstring de la v3 "21" contre log 22 : le compte doit
          se nommer, "22 lignes, toutes capables de mordre, dont une
          conjonction".
  D-ACA-4 (m1 ; forme) son controle nommait un pas dt2/4 et des etats finaux
          x1, x2 que les JSON du pre-vol ne portent pas (le dt2/4 vit dans sa
          piece de convergence c8d86e5e5b4fd745, les etats finaux dans aucune)
          : un controle ne nomme que des grandeurs que la piece visee porte.
          Dette d'instrument proposee pour un v9 : emettre par cellule et par
          pas les etats finaux des flots.
  D-ACA-5 (m2 ; custody) un fichier sous le nom de machine 1 portant le contenu
          de machine 2 (son rejeu1 ed09e29e91b6eb00), au poste machine 2 : une
          piece se resout par son CANON, jamais par son nom, y compris chez soi.
  D-ACA-6 (m2 ; forme) manifeste 1985ad4eea984bf5 portant les lignes entrants
          et bilans du lot precedent (erratum (3)) ; cause : substitution
          silencieuse.
  D-ACA-7 (m2 ; forme) TROIS chk a condition True (l.69, 126, 180) dans la
          feuille meme qui clot D-ACA-1 (verifications_lecture v1
          2121738de50e2324) ; trouves par la garde syntaxique de machine 1
          (be6bb447da1f4363), qui rend 5 appels a condition constante sur 7
          feuilles, dont un False sous condition qui n'est pas un defaut (une
          morsure declaree dont l'issue vit dans le if) ; rejouee chez machine
          2 elle rend le meme compte. Corrige en v2 (412c6bb0a4c6d7b7, 20/20,
          deux verbes chk/note, garde jouee avant emission).
  Du geste (2) :
  D-G2-1, D-G2-2 (m1 ; forme ; soldes par le script v2) : la garde du
          diagnostic n'acceptait qu'un canon et son verdict n'etait pas
          symetrique ; le v2 accepte l'un ou l'autre canon, nomme lequel il a
          recu, rend "cause chez l'autre" et nomme le cas degenere.
  D-G2-3 (m1, m2 ; prose ; forme adoptee) : trois fois dans le geste la prose a
          interverti une paire de fichiers que le code designait juste ; tout
          rejeu est desormais cite par la ligne CANON de la feuille jouee.
  D-G2-4 (m1 ; prose) "les grandeurs de la borne viennent des JSON" : faux
          pour moitie -- le ratio venait du log a trois decimales, seuls les e
          de la correction conservatrice venaient des JSON ; mesure par machine
          2 (5231ce763b007399), verse par machine 1 (1f80e0e9b88f2ff2), applique
          en nn.4 d.
  De l'instrument (29/08, pour memoire, tous leves au v8 ; notes
  be633ae91ae295b5, 2a618ffb180ea568) :
  D-I-3   (m1 ; bloquante, levee) le compteur de bilan n_ok du banc v5 etait
          calcule AVANT que Q21 n'ajoute cinq scenarios : 50 == 55 -> False quoi
          qu'il arrive, et le message d'arret recalculait la somme et
          annoncait "banc 55/55" a l'instant ou le processus mourait (rc = 1).
          Deux regles en sont sorties : un compteur de bilan se calcule apres
          le dernier ajout ; un message d'arret ne doit jamais pouvoir se lire
          comme un succes. Levee au v8 (n_ok calcule apres le dernier ajout,
          declare dans le code).
  D-v5-1  (m1 ; OUVERTE) LD-16 lit un plancher c_pl x eps x N herite d'une
          clause de 5.4 que la v11 a abrogee "et remplacee par aucune autre" ;
          le v5 emet c_pl_ld16_herite: 10 au reglage du JSON. Decision (i),
          nn.9.
  Lacune du delta 89, reprise ici (D-CERT-6 : l'erratum de machine 2 sur la
  cause du "-10" est au registre EN PROSE, sans la feuille qui le mesure) :
  la liste de depot du 89 appliquait deux poids -- lots v1/v2 : note, feuilles
  et manifeste ; lots v3/v4 : note seule. Les feuilles et manifestes des lots
  de certification v3 (bdd00189e68b61dc) et v4 (704f2b6b84f4c6a0), dont
  controle_cause_du_moins_dix_machine2_v1 (0c577a23d67586c8), entrent par cet
  acte ; le perimetre les enumere depuis ces deux citations.

nn.8 REGLES CANDIDATES SOUS (X) -- revue 28/09, aucune n'est prise ici
  Chacune porte sa date de revue (28/09) et l'instance payee qui la fonde.
  1. La ligne de plateforme d'un log de run porte un temoin d'arrondi
     EXECUTABLE -- (1765.6704444885254) ** 6 rend ...9c5 sous le noyau SIMD et
     ...9c6 correctement arrondi (m1) ; le registre ne permet pas de dater
     l'exposition autrement (34 logs deposes, 1 nomme numpy, 0 un dispatch).
  2. Dans une feuille de controle, le champ de detail ne porte que des nombres
     mesures ou des chemins ; toute affirmation vit dans la condition, ou elle
     n'existe pas (m2 ; erratum (2)). Outillable : un detail qui contient
     "seul", "tous", "aucun", "jamais" est un controle deguise.
  3. Tout nombre qui entre dans une borne, un compte ou un ecart se lit A LA
     SOURCE ; et un ecart plus fin que le pas de lecture n'est pas une mesure
     (fusion accordee des deux plumes ; instances : D-G2-4, le compte "trois"
     de l'erratum (2), et le "16 regions" du 09/09).
  4. Toute transformation CRLF -> LF est DECLAREE a l'application (fait de
     forme de (v) ; la pratique est acquise, le texte non ; precedent P-4).
  5. Une substitution qui ne trouve pas sa cible doit MORDRE, jamais passer :
     toute reecriture programmee d'une piece assere chacun de ses remplacements
     (m2 ; D-ACA-6). C'est le silence qui coute, pas la faute.
  6. Deux verbes dans une feuille : chk MESURE et compte, note porte la prose
     et ne compte pas ; et la garde syntaxique se joue sur la feuille AVANT
     emission (m1, adoptee et outillee par m2 ; D-ACA-1, D-ACA-7).
  7. Le compte attendu est un ARGUMENT, comme le chemin ; sans l'argument, le
     controle est DECLARE NON JOUE et le log le dit (m2 puis m1 ; R-G2-5 v2).
  8. Un manifeste porte deux sortes de lignes, TABLE (une piece du lot, a cote
     de son manifeste, canon dans sa ligne) et CITATION (une piece d'un autre
     lot, resolue par canon n'importe ou au poste) ; et le compte de table d'un
     lot EGALE le "pieces : N" que son manifeste declare (m2 ; deux pertes
     silencieuses a l'assemblage de la re-livraison, dont un 11/11 qui perdait
     une piece). Instance de 3 et de D-ACA-5 ; un controle d'absence qui nomme
     deux chemins ne mesure pas l'absence au poste (m1, sur relecture v1
     section 6 : le 28b y est declare absent alors qu'il est au poste).

nn.9 A ARBITRER PAR L'OPERATEUR, NON PRIS ICI
  (i)   LD-16 / depot 9bis (D-v5-1). Prealable, ecrit ici : LD-16 lit
        aujourd'hui sous le gel v11, dont la clause d'ancrage (5.4, W-plancher)
        est abrogee "et remplacee par aucune autre" ; un run depose sous la v11
        porterait une constante que son gel declare retiree. Issues : erratum
        de re-ancrage (forme de 7 (i), sans editer la v11) ou retrait a l'acte ;
        si LD-16 releve de (X), c'est une occasion nommee. Et (c) de N-70 et
        (i) voyagent ensemble sans se substituer : un re-ancrage ne leve pas la
        dependance machine, il en change le titulaire. Plumes : m1 et m2
        accordees sur le prealable, aucune ne tranche l'issue.
  (ii)  N-70, issue (a) (b) (c) pour les quatre cles tol_int a appel libm.
        Contrainte mesuree par le geste (2) : le 9bis entre machines compare a
        tolerance ou exempte, meme noyau desactive (residuelle glibc/UCRT a un
        ulp, tol_ordre a un ulp sur tout p = 7, champ de forces a trois
        valeurs). (a) est deja le cas de fait : run_temoin_delta85 depose porte
        0.008578984888782988 sur ses cles tol_int, la valeur machine 2, sans
        que personne ne l'ait decide. Plume m1, sans decider : (c) ; plume m2 :
        aucune issue. Le piege de nom est tranche a la plume de m1 : les
        classes s'appellent EXPOSEE, EXPOSEE-LIBM, ABSORBEE, NON SEPAREE ; les
        issues de N-70 gardent (a) (b) (c).
  (iii) Numeros de serie (E18) pour les errata (1) (2) (3), le fait de forme de
        (v), D-ACA-1 a 7, D-G2-1 a 4, D-I-1 a 9, D-v5-1.
  (iv)  Le depot groupe : cet acte en est le vehicule, avant la revue du 28/09.
        Non deposes, assumes et ecrits : les ZIP des lots (un seul ZIP a jamais
        ete depose ; precedent non pris seul) ; MANIFEST.sha256 (dette
        anterieure, arret au delta 80).
  (v)   Fait de forme des captures CRLF : les deux plumes lisent (b) (fait de
        forme numerote a l'acte, regle d'ecriture candidate 4), avec le
        precedent P-4 ; l'operateur tranche.
  (vi)  L'arbitrage du 29/08, ENTIER : la marge du volet A, ou une marge cote T
        -- PAS LES DEUX. Un reglage choisi en connaissant la valeur est ce que
        la campagne s'interdit ; aucun delta n'est recommande.
  (vii) La dette d'instrument v9 (etats finaux x1, x2 par cellule et par pas,
        D-ACA-4) ; le levier NPY_DISABLE_CPU_FEATURES, a arbitrer PAR USAGE (il
        aligne power et exp sur la libm mais degrade log10, expm1, log1p,
        cbrt) ; les deux pieces non detenues 128d0c0a et a6415de8 (declarees
        non porteuses ; leur reconstruction depuis un transcript n'est pas
        tentee sans demande).

nn.10 CONSEQUENCES POUR LE REGISTRE
  - Le registre recoit la chaine entiere de la constante A : le gel courant v5
    et ses deux versions remplacees ; le gel du volet T v11, sa v9, sa
    certification, son depot 9bis et son erratum 7 (i) ; l'instrument v8 et sa
    lignee v4 a v7 avec ses deux scripts de construction ; N-70 v1 et v2 ; les
    deux pre-vols et les deux JSON de machine 1 ; la tenaille et le geste (2)
    avec toutes leurs feuilles ; les lots des trois tours ; la lacune du 89.
  - Le gel courant de la constante A est le v5 2c0d2dc86054838c ; le gel du
    volet T est le v11 a2e7ef3e237c5acf ; l'instrument certifie est le v8
    4d8882a2223a5c74. Les v7 du temoin et v3 du banc deposes sont des versions
    remplacees.
  - Aucun run du volet T ni du volet A n'est depose ; aucun verdict de gel ;
    le pre-vol rend branche 4 et le run n'est pas lance.
  - La reference deposee run_temoin_delta85 porte la valeur machine 2 de
    tol_int : consigne, non decide.
  - La tenaille est une derivation de classe 3 relue par les deux machines ;
    elle n'est pas un gel et ne fixe aucun delta.
  - Rien de cet acte ne touche la sequence R4/R5, les manches M1-M17, la
    branche quantique ni la correspondance.

nn.11 LE CANAL, CONSIGNE COMME PROPRIETE
  - Le conteneur de machine 1 a ete reinitialise le 07/09 : le fond a ete
    re-livre en un lot de 158 pieces a l'arbre preserve (d0ab94382e1b5808),
    recu 158/158, et les trois feuilles s'y rejouent apres simple depliage
    (derivation v3 au bit, relecture v1 39/39 a six chemins pres, R-G2-5 v2
    42/9/6) ; l'assemblage a paye deux pertes silencieuses avant d'etre juste
    (nn.8, candidate 8).
  - Sept lots echanges le 12/09 sur l'acte, plus la re-livraison et son
    rejeu, et onze sur le geste (2), tous confirmes par canon des deux
    cotes, zero perte ; le canal fractionne
    (un lot arrive en deux envois) et ne renomme pas quand il transporte un
    ZIP ; le manifeste interne fait canon, le brut du ZIP est donne a cote.
  - Un lot ne vivait que dans son ZIP, jamais extrait : un balayage de disque
    ne voit pas une piece restee en archive. Une piece se resout par son
    canon sur TOUT le poste, jamais par un chemin nomme.
  - Le SUIVI 28b, cite a la provenance du gel v5 et detenu nulle part, a ete
    reconstruit par machine 1 depuis le transcript du 28/08 et authentifie par
    canon avant toute lecture (b6d13e6a1559e850, 5639 octets).
  - Les .log de machine 2 sont CRLF (Python sous Windows), verifies au brut,
    comptes et nommes a chaque manifeste ; les pieces des deux machines sont
    ASCII/LF hors ces logs.

nn.12 CE QUE CE DELTA NE FAIT PAS
  Il ne prend aucun numero de serie ; il ne lance aucun run et n'en recommande
  aucun ; il ne rend aucun verdict sur le volet A ni sur le volet T ; il ne
  fixe aucun delta et ne lit pas la tenaille comme un gel ; il ne tranche ni
  (i), ni (ii), ni (v), ni l'arbitrage du 29/08 ; il ne prend aucune regle
  nouvelle ; il n'edite aucune piece citee (PB-1) ; il ne depose ni les ZIP
  ni MANIFEST.sha256 ; il ne reconstruit pas les deux pieces non detenues ; il
  ne dit rien de la sequence R4/R5 ni de la branche quantique ; il ne sort
  rien vers Held.

nn.13 PIECES DE CE DELTA (lot machine 2 ; canon = convention B du manifeste)
  journal_delta_nn_constante_A_v1.md              cet acte
  perimetre_depot_delta90_machine2_v1.py / .log   le perimetre ENUMERE depuis
                                                  les citations de cet acte,
                                                  et le manifeste de depot
                                                  qu'il DERIVE
  relecture_nombres_delta90_machine2_v1.py / .log les nombres de cet acte relus
                                                  aux sources (deux jambes)
  MANIFEST_DEPOT_delta90_machine2.txt             derive par la feuille de
                                                  perimetre, jamais ecrit a la
                                                  main
  Les entrants sont ceux de nn.1 ; les feuilles de mesure du chantier
  (derivation v3, controle croise, verification 28b, verifications v2,
  comparaison a trois, erratum, precision de la borne) sont dans leurs lots
  d'origine et entrent au depot avec eux.

-- FIN journal_delta_nn_constante_A_v1 --
