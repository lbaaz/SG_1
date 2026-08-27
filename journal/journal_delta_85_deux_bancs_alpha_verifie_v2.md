JOURNAL DELTA 85 -- LES DEUX BANCS ENTRENT AU REGISTRE : L'INSTRUMENT
(v1 -> v3), L'ERRATUM GROUPE DES GELS (E43, E44, E45), LES CINQ FAITS,
LE TEMOIN REEL (REGLAGE QUALIFIE, bonus retire) ET LA VERIFICATION alpha
(VERIFIE : alpha = 4/(p-2) AUX TROIS DEGRES) ; UNE REGLE (N-70), TREIZE
DEFAUTS (D-M17-46 a D-M17-58), SEIZE LECTURES DECLAREES (LD-1 a LD-16)
(redaction machine 1, certification machine 2, depot operateur,
2026-08-28) -- VERSION 2
=======================================================================
Version 2 : repond a la certification machine 2 de la v1 (1d0205dc74eda8f4
NON CERTIFIEE, note 57fcf4c644ba4a68 : D-e-1 quatre empreintes non
resolues, D-e-2 trois ecarts lus a l'affichage, D-e-3 quatre signes en
prose). Trois correctifs et une consignation de canal (85.7bis) ; aucun
nombre pris ni retire ; aucun verdict ne bouge.
S'insere apres le delta 84 (9c95a3d, journal_delta_84_arbitrage_78_7_v1
fff42f489696c7ed) et apres les depots sans numero 37ad1b6, 0485001,
e800c71 (N-69). Numero pris A L'ACTE au depot (66.5.c). Acte de CLASSE A
(delta 71) : il consigne deux runs reels, deux verdicts en forme de
cloture, un erratum de gel, et arme une regle. Patron des deltas 82-83.
Files verifiees avant prise (E18), sur les seules pieces .md/.txt de
l'arbre e800c71 (jamais binaires ni code) : E libre au-dela de 42, N
au-dela de 69, D-M17 au-dela de 45 -- releve machine 1 sur clone frais
le 28/08 ; a confirmer par machine 2 a la certification de cet acte.
Aucune piece recue hors arbre ne prend de numero ; les pieces recues sont
citees par empreinte (convention B) et deposees AVEC cet acte.

85.0 POSITION EN TROIS PHRASES
  Les deux bancs (N-69) ont ete joues sur BOCAL4 le 28/08 avec un
  instrument certifie et depose avant les runs (e800c71), sous deux gels
  re-emis, certifies et deposes avant les runs (0485001). Le temoin
  negatif classique rend REGLAGE QUALIFIE (bonus T-3 retire), branche 6 ;
  la porte d'alpha s'ouvre et la verification rend VERIFIE, branche 5 :
  alpha = 4/(p-2) aux trois degres, chacun des dix-huit exposants sous sa
  tolerance derivee, aucune moyenne. P-alpha est MESURE ; P-A est
  COMPATIBLE, par le plancher de modele (10.3 v5), et cela s'ecrit avant
  tout commentaire (85.5.3).

85.1 L'INSTRUMENT DES DEUX BANCS -- TROIS VERSIONS, DEUX CERTIFIEES
  Un seul script, deux modes (--mode temoin, --mode alpha), trois modes
  d'instrument (--selftest, --banc, --prevol a moteur factice), MANIFEST
  des sorties, la main dans le nom (N-65), ASCII/LF, aucune reprise
  (N-66). PB-1 tenu : le moteur depose c8ed357b120352c4 n'est ni edite
  ni copie ; sa physique est TRANSCRITE aux lignes citees (l.278-280,
  323-325, 339-348, 351-361, 362-363, 372-401) et, pour G-lignee et le
  controle d'algorithme, il est CHARGE (patron m12_pilote_v3 l.483-518)
  et APPELE TEL QUEL ; deux globales re-liees a l'appel, jamais le
  fichier : P (patron depose) et T_MAX (rend l'indice d'explosion
  accessible). La transcription est controlee contre l'algorithme
  depose sur neuf thetas AU BIT, motifs compris.
    v1  3a932eabfaaf4307  116438  NON CERTIFIEE (m2 3f017a997b0b1812 : 53
        controles, 6 mordent ; C-1 dix gardes sans morsure, C-11, C-12,
        etat tangent evite non refuse) -- remplacee ; ses journaux de
        repetition et sa note d'accompagnement RETIRES (85.6, D-M17-46)
    v2  d74928ef093c96d0  133202  CERTIFIEE sous v5/v2 (m2 10d3160eef210015,
        68 controles, une trouvaille : LD-15) ; contresignee
        72bc452ec8eb6950 (detenue machine 1, non parvenue a machine 2 a la
        certification de la v1, retransmise avec la v2) ; pre-vol opposable
        du 27/08 (m2 dd10437b0d56c79c,
        erratum de lecture 5575ac8cf96b298b) ; PERIMEE par 0485001
    v3  5fae2a8c94cf8685  144725  CERTIFIEE sous v7/v5 (m2 baf75f462ab14119,
        40 controles, attendus ecrits AVANT la livraison, physique
        verifiee a l'AST : 29 intouchables, 0 bougee) ; contresignee
        146f7dd9d81ace1d ; DEPOSEE e800c71 ; pre-vol opposable du 28/08
        (m2 e70b639a04b8d136, contresigne d3a0d73a3139da3b) ; c'est la
        copie des deux runs (N-59 : journal temoin [0003], alpha idem)
  Ce que les certifications ont impose a chaque pas : un banc qui TUE
  (chaque scenario asserte sa branche : 21, puis 40, puis 42 scenarios),
  les gardes ENUMEREES par la machine depuis la section 8 des deux gels
  (seize, par deux regles differentes tombant sur la meme liste), chaque
  garde FORCEE ou DECLAREE sans morsure -- quinze en v2, seize en v3 --,
  trois lignes NE-JOUE-PAS par journal (lectures non lues, gardes sans
  morsure demontree dans ce journal, runs non joues), le banc des gardes
  REJOUE A LA FIN DE CHAQUE RUN, l'etat tangent REFUSE (SystemExit, gel
  temoin 4.3), zero mention d'outillage, et la reproductibilite mesuree
  (deux pre-vols v3 : 19 cles identiques, trois durees d'ecart).

85.2 L'ERRATUM GROUPE DES GELS -- E43, E44, E45
  Arbitrage de l'operateur du 28/08 : les faits 1, 3, 4 et 5 (85.3) se
  traitent en UN erratum, le fait 2 reste gele (et se dissout, 85.3).
  Les gels deposes ne sont pas edites (PB-1 ; v5 et v2 resolvent toujours
  a 0905a9b78ba40349 et 35a70834b2a34514, re-derives) : ils sont RE-EMIS,
  certifies, deposes (0485001), et les anciennes ancres sont PERIMEES.
  E43 -- GEL TEMOIN v5 -> v7 (8b083e9f109b5a8e, 39750), plume machine 2,
    certifie machine 1 (6b2425dbf906205b) apres une v6 NON CERTIFIEE
    (e9a7e7e2e2ed0354 ; D-M17-56). Section 8 exigeait la lecture de
    W-integrales sur dt contre dt/2, section 9 ne comptait aucun flot a
    dt/2 (FAIT 1, LD-9). v7 : T-1 = 2 etats x 2 flots, ATTENDUS 41 ; les
    flots a dt/2 ne servent qu'a W-integrales ; q_int = log2(derive(dt)/
    derive(dt/2)) contre 4 pour H1 et N, tol_int = log2((1+b)/(1+b/2)),
    b = omega_max dt, omega_max^2 = w^2 + 3 lambda x_max^2 lu sur le flot,
    plafond eta x 1 ; une morsure mene a la branche 6 et jamais ailleurs
    (declaree serree, non desserree). Le pied de page de la v5 deposee
    portait "_v2" : faute de forme versee par machine 2, corrigee.
  E44 -- GEL ALPHA v2 -> v5 (045c2435aaf623ce, 28998), plume machine 2,
    certifie machine 1 (fe43f7c4d142bcdb) apres v3 (3dad1c34b54bb9c3) et
    v4 (c261b6a5f34262e5) NON CERTIFIEES (D-M17-57, D-M17-55). Trois
    entrees : 10.3, plancher_lnA(p) = delta/((alpha_p+2)(alpha_p+3)) =
    1/2000, 9/13000, 1/1064, tol_lnA = max(dispersion, plancher), le
    (p-2) dans la seule comparaison (FAIT 3) ; 10.1bis, G-dt et G-k
    comparees au plafond eta x 8/15, role diagnostique ecrit (FAIT 4) ;
    4.4, chaque point se joue a sgn = frag de la carte, +1 sans second
    seuil, frag et asym consignes (FAIT 5) ; section 13 mise en accord.
    Aucune prediction, aucune amplitude, aucune cellule, aucun nombre pur
    ne change ; la table 4.2 est intacte au bit.
  E45 -- ERRATUM DE FORME sur la v5 deposee (0905a9b78ba40349, l.693) :
    "-- FIN temoin_negatif_pre_enregistrement_v2 --". Le gel ne s'edite
    pas ; la rectification vit ici et dans la v7.
  Lecture appliquee, pas une regle : un numero E se prend pour un
  erratum sur une piece DEPOSEE ; les errata de correspondance de
  machine 2 sur ses propres notes non deposees (85.7) sont consignes par
  reference, sans numero.

85.3 LES CINQ FAITS, ET LEUR SORT -- tous lisibles sur le TEXTE ou sur
     la CARTE, sans mesure
  FAIT 1  W-integrales injouable a compte gele (temoin 8 contre 9).
          Releve par l'instrument a l'ecriture (LD-9), confirme par les
          deux machines par enumeration du gel. -> E43. Jouee au run :
          elle a MORDU (85.5.1).
  FAIT 2  Aux quatre points a frag = -1 -- (5, 2.27), (5, 2.80), (7, 2.27),
          (7, 2.80), ENUMERES sur les neuf --, 1.20 x sF < sP = asym x sF :
          une trajectoire lancee a sgn = +1 y est SOUS le seuil de sa
          propre branche. Il n'existait pas comme "amplitudes trop
          petites" : il est DISSOUS par le fait 5, sans toucher 4.3.
          Au run : G-fen nulle part, les trois degres exploitables.
  FAIT 3  10.3 tirait la tolerance de P-A de la dispersion de
          l'instrument, quand l'ecart vient du modele, borne en 6
          (D-alpha-9) ; P-A rendait PARTIEL par construction des que
          l'instrument etait bon. -> E44. Au run : le plancher est
          porteur aux trois degres (85.5.3).
  FAIT 4  10.1 rendait G-dt et G-k muettes a la lettre (la tolerance
          contenait les ecarts testes) ; la premiere correction (v3,
          tolerance privee de l'ecart) les rendait bruyantes sans echelle
          (D-M17-57). -> E44, au plafond. Au run : muettes, ecarts au plus
          4.2e-05 x 8/15.
  FAIT 5  4.4 declarait l'autre branche "sans objet" a degre impair en
          lisant sF = min(sP, sM) : quatre points sur neuf partaient sur
          la branche opposee a leur seuil. Physique : x^(p-1) impaire a
          p = 4 (symetrie, sM absent), paire a p = 5, 7 (deux seuils).
          Verifie sur la carte fa109da92e582520 : 9/9. -> E44. Au run :
          G-lignee 27/27 au signe joue ; attendu de 5.6 respecte 27/27.

85.4 N-70 -- LA PREDICTION SE DEPOSE AVANT LE RUN, PAR ENUMERATION
  TEXTE : avant un run reel, le JSON du pre-vol opposable joue sur
  l'instrument certifie est DEPOSE, et une prediction y est ancree, a
  profondeur declaree, par ENUMERATION des cles (jamais une liste) :
  cles IDENTIQUES au caractere entre le pre-vol et le run, cles NON
  PREDITES (le discriminant), cles EXEMPTES (dates, chemins, statut).
  Tout ecart d'une cle IDENTIQUE se consigne AVANT d'etre explique ; un
  "ecart" d'une cle NON PREDITE n'en est pas un. La reproductibilite se
  MESURE (deux pre-vols) avant que la prediction vaille.
  ARBITRAGE : operateur, 28/08, par l'ordre de depot e800c71 (message du
  commit : "deposited BEFORE the real run so that the prediction on the
  witness JSON is dated and public before any result exists, and can no
  longer be adjusted by anyone"). Precedent : prevol_temoin_v3_opposable
  786a368878768d4b, note e70b639a04b8d136, contresignature
  d3a0d73a3139da3b ; au run du temoin, 19 cles sur 19 (85.5.1).
  A compter de ce delta.
  PROPOSITIONS, A ARBITRER PAR L'OPERATEUR, NON PRISES ICI :
  (a) une garde ne se compare jamais a une tolerance qui CONTIENT l'ecart
      qu'elle teste, ni a un maximum sans echelle (10.1bis v5 en est la
      forme) ;
  (b) aucune physique du DISCRIMINANT ne tourne avant le run depose :
      le pre-vol est a moteur factice, et une lecture de verdict hors
      instrument depose se verse (D-M17-46 en est la faute).

85.5 LES DEUX RUNS -- FORME DE CLOTURE
  85.5.1 LE TEMOIN NEGATIF CLASSIQUE (m2 030ebe36d2957cd7 ; journal
    journal_temoin.txt d8ac838ce2d1bd48, capture 10a7ce5688f515d5 ; JSON
    644240dc894c2733 statut REEL ; MANIFEST c557a4fa5aa6bd28, 5 fichiers)
    VERDICT : REGLAGE QUALIFIE (bonus T-3 retire) -- branche 6 : T-3 mord
      seul (W-integrales, T-3a). 30.3 s. comptes 41 + 0 == 41. Aucun run
      saute. Seize gardes demontrees dans le journal.
    T-1 (croissance lineaire, lecture pre-declaree du gel, section 12) :
      etat A t_c = 20.1000 39.2520 79.6800 156.0960 313.3920 ->
      R = 1.95284 2.02996 1.95904 2.00769 ; tol_R/(q-1) = 0.05955
      etat B t_c = 8.4960 16.4700 32.3940 62.7540 126.2820 ->
      R = 1.93856 1.96685 1.93721 2.01233 ; tol_R/(q-1) = 0.16066
      fenetre de q VRAIE aux deux, saturation FAUSSE aux deux (journal
      [0015]-[0022]) ; W-croissance muette ; predictions de T_MAX
      consignees AVANT verification (643.2 ; 271.872).
    T-1b (le mirage, deux lois) : seuils 0.9772529765993441 /
      1.954505405708197 / 0.4872145458084787, motif OK|pas=6.03e-07, k = 0
      ; loi 1 = 1.999999 (tol 9.202e-03) ; loi 2 = 0.498555 (tol 2.301e-03,
      osc 0.00460 lu sur le flot A : |0.498555 - 0.5| = 1.445e-03, a 0.63
      de la tolerance) ; regime LOIS ([0025]-[0029]). Les trois seuils
      == la mesure hors gel de 4.6 (0.977252977 / 1.954505406 /
      0.487214546) au dernier chiffre imprime.
    T-2 (neuf bancs) : p_obs = 3.9053 (p=4) 3.9202 (5) 3.9321 (7), tol_ordre
      0.2003 / 0.1848 / 0.1720 sous plafond 1/4 (LD-4) ; e(dt2)/ln 10 =
      4.296e-06 / 1.459e-06 / 4.554e-07 (LD-5) ; W-pas, W-plancher,
      W-bascule muettes aux neuf ([0030]-[0047]) ; T-2a e = 2.03e-09 ;
      T-2b e = 9.89e-06 / 3.36e-06 / 1.05e-06 ; T-3b 3/3 (4.39e-09,
      4.35e-08, 7.14e-07).
    W-integrales (E43) : etat A q_int(H1) = 4.094288 contre tol_int
      0.00858 -> MORD ; N a dt/2 = 2.914e-11 sous le plancher 4.761e-10 ->
      NON LUE (LD-16) ; etat B q_int(H1) = 4.107234, q_int(N) = 4.959798
      contre 0.01536 -> MORD ([0019], [0024]). Consequence : le bonus T-3
      est retire ; rien d'autre. La morsure etait annoncee a la
      certification de la v6 et cantonnee a la branche 6 par le gel
      plutot que desserree : seul endroit du dossier ou une decision de
      forme a change une issue. Fait de journal, a ne pas expliquer ici :
      q_int(N) = 4.96 a l'etat B.
    PREDICTION (N-70) : 19 cles sur 19 identiques au JSON depose
      786a368878768d4b (declaration machine 2 ; a RE-DERIVER par machine
      2 a la certification de cet acte et par machine 1 au depot du JSON
      644240dc894c2733 ; toute divergence rouvre cet acte par erratum).
    Ce que ce run ne dit pas : rien d'alpha ; il a cherche a refuter le
      reglage et n'y est pas parvenu ; la conservation des integrales
      n'entre pas au dossier ; la fidelite de (2.11) a l'article repose
      sur machine 2 seule, la double transcription reste due.
  85.5.2 LA VERIFICATION alpha (m2 031d85049f22813d ; journal
    journal_alpha.txt c30d8e6442bd934d, capture 0e7e56006d2e200a ; JSON
    6d7d23130e9322f8 statut REEL ; MANIFEST 932fe5bcd181b127, 65 fichiers)
    PORTE : temoin 644240dc894c2733, verdict en tete REGLAGE QUALIFIE,
      statut REEL, reglage identique, e(dt2)/ln 10 relus (LD-5) ([0011]).
    VERDICT : VERIFIE -- branche 5 : P-alpha les six par degre ET P-A aux
      trois degres. 116.2 s. comptes 90 + 0 == 90. Aucun run saute.
    P-alpha, les six par degre (plan, _dt2_k2), aucune moyenne :
      p = 4  1.999824 1.999828 1.999823 1.999825 1.999825 1.999827
             attendu 2     ecart max 1.7716e-04  tol 2.262e-04
      p = 5  1.333186 1.333149 1.333138 1.333147 1.333159 1.333155
             attendu 4/3   ecart max 1.9545e-04  tol 2.403e-04
      p = 7  0.799702 0.799209 0.799766 0.799956 0.799912 0.799792
             attendu 4/5   ecart max 7.9099e-04  tol 1.209e-03
      (ecarts max relus au JSON 6d7d23130e9322f8 en pleine precision par
      machine 2, 57fcf4c644ba4a68 D-e-2 : 1.771593e-04, 1.954457e-04,
      7.909858e-04 ; au journal a six decimales ils se lisent 1.770e-04,
      1.953e-04, 7.910e-04 -- les six alpha ci-dessus sont ceux du journal)
      separation 8/15 resolue par (8/15)/tol = 2357, 2220, 441.
    Gardes : G-dt, G-k au plus 4.2e-05 x 8/15 ; G-s, G-w2 muettes ;
      G-seuil muette aux neuf points (aucun triplet ; a 5|2.27 (ii) seul
      vrai) ; G-fen nulle part ; G-lignee 27/27 booleens ET indices, au
      signe joue ; attendu de 5.6 respecte 27/27 ([0105]-[0119]).
    Signes joues (E44, 4.4) : +1 +1 +1 | +1 -1 -1 | +1 -1 -1, avec asym
      0.7908 1.9140 1.2809 | 0.8360 1.2424 1.2359 aux six points impairs.
  85.5.3 P-A : COMPATIBLE, PAR LE PLANCHER -- ecrit avant tout commentaire
      p    dispersion_lnA  plancher_lnA  tol_lnA   |ln(gA^(p-2)/K)| max
      4    1.977e-06       1/2000        plancher  2.263e-04  (23 pour cent de 1.000e-03)
      5    2.394e-06       9/13000       plancher  3.635e-04  (18 pour cent de 2.077e-03)
      7    7.432e-06       1/1064        plancher  1.584e-03  (34 pour cent de 4.699e-03)
    Sans le plancher (dispersion seule), P-A echouait aux trois degres :
    le verdict serait PARTIEL par construction. Ce qui s'oppose, et rien
    de plus : le plancher est une borne de MODELE ecrite en 6 depuis la
    v2 (D-alpha-9), posee en 10.3 avant le run dans un gel certifie et
    depose ; l'ecart n'est pas au bord (18 a 34 pour cent) ; les DIX-HUIT
    rapports g A^(p-2)/K sont > 1 ([1.000222, 1.000226] ; [1.000323,
    1.000364] ; [1.000403, 1.001585]) -- un bruit ne choisit pas son cote
    dix-huit fois, un terme neglige, si ; et la grandeur du biais ordonne
    comme la borne (p = 7 > 5 > 4), lecture consignee sans promotion.
    DONC : P-alpha est MESURE ; P-A est COMPATIBLE. La constante n'est
    pas mesuree a la precision de l'instrument (2e-06 en ln A) : elle est
    bornee par la fenetre. La mesurer est un autre gel (delta plus petit).
    A CHARGE : ce verdict depend de trois corrections faites la semaine
    ou il est obtenu (faits 3, 5, et 1 pour le temoin). Toutes trois sont
    des incoherences de TEXTE lisibles sans mesure, certifiees par
    l'autre machine et deposees avant les runs (0485001 < e800c71 < les
    runs, dates au registre). C'est la seule chose qui separe une
    correction d'un ajustement, et elle est au registre.
    Ce que ce run ne dit pas : rien de la classe ponctuelle refutee en
    M12 (11/11) -- il teste le PROFIL, pas la loi de seuil ; rien hors des
    trois colonnes, des trois degres, des trois amplitudes ; la branche
    opposee n'est pas jouee (parite a p = 4 seulement).
  85.5.4 CE QUE LA CAMPAGNE ACQUIERT (a compter du depot)
    La chaine classique porte deux lois derivees : L1 (echelle des seuils,
    M10-M12) et le PROFIL, alpha = 4 u_p, verifie aux trois degres sur
    les trajectoires du moteur depose, au bit. Le reglage de l'instrument
    de profil est qualifie par un temoin negatif de la meme classe.

85.6 LES DEFAUTS -- D-M17-46 a D-M17-58 (serie continuee, delta 84, 84.5)
  D-M17-46 machine 1 -- LECTURE DES VERDICTS AVANT LE RUN DEPOSE. Les
    deux modes reels joues au bac a sable, verdicts lus, "trois faits a
    trancher avant BOCAL4" ecrits sur cette lecture, journaux joints
    (note v1 ac157c6450a30182, RETIREE ; journaux retires). N-62. Versee
    par machine 1 (note v2 3a98cd5c7385d8d0 non envoyee, v3
    63fc202bbfd91b80 section 0). Faute la plus grave de la sequence : la
    lecture ne se de-lit pas ; elle est declaree pour qu'elle n'agisse
    pas en silence, et 85.4 (b) en propose la regle.
  D-M17-47 machine 1 -- LD-4 FIXEE APRES UNE VALEUR VUE. La forme
    tol_ordre = log2((1+b)/(1+b/2)), b = (alpha+5)/M, choisie apres qu'un
    prototype a montre p_obs = 3.905 (une forme plus simple, 0.0704,
    aurait fait mordre W-pas). Derivation ecrite ; ordre d'ecriture
    versee. Epreuve de puissance jouee par machine 2 (baf75f462ab14119
    V-13 : |4-3| = 1 contre 0.2003, facteur 5, sous plafond) : la forme
    se garde, sa chronologie s'ecrit ici. Au run, W-pas muette aux neuf
    (0.095 sous 0.2003 ; sous 0.0704 elle aurait mordu : l'ecart entre
    les deux formes est REEL, V-14).
  D-M17-48 machine 1 -- LD-15 NON DECLAREE. G-dt et G-k comparees au
    plafond 2/15 dans le code (v1, v2) sans que la lecture soit ecrite,
    alors que la lettre du gel v2 (8 + 10.1) ne pouvait pas mordre.
    Trouvee par machine 2 (10d3160eef210015 V-08, V-09). Absorbee par le
    gel v5, 10.1bis (E44).
  D-M17-49 machine 1 -- PERIMETRE ECRIT A LA MAIN. Trois points listes
    (5, 2.27), (5, 2.80), (7, 2.80) la ou la carte en enumere QUATRE
    ((7, 2.27) manquait) ; machine 2 a herite la liste au lieu de
    l'enumerer (son cinquieme erratum). La regle la plus chere de la
    campagne, refaite ; l'instrument v3 enumere (selftest).
  D-M17-50 machine 1 -- INSTRUMENT v1, QUATRE DEFAUTS A LA CERTIFICATION
    (3f017a997b0b1812 D-b-1..D-b-4) : mention d'outillage et
    date_utc depreciee fuyant un chemin ; aucun journal ne disait ce
    qu'il ne joue pas ; dix gardes sur seize sans morsure demontree ;
    etat tangent evite, pas refuse. Corriges en v2 avant tout run.
  D-M17-51 machine 1 -- INSTRUMENT v3, DEUX EN-TETES DE SECTION PERIMES
    (l.1281 "gel 0905a9b78ba40349", l.1714 "gel 35a70834b2a34514" ;
    baf75f462ab14119 D-c-1). Famille de D-M17-55, reprochee la veille a
    machine 2. Documentation seule ; correctif a la prochaine version
    qui touche du code (l'ancre 5fae2a8c94cf8685 ne s'edite pas).
  D-M17-52 gel temoin v5 (m2 auteur, m1 certifieur) -- section 8 contre
    section 9 (FAIT 1, LD-9). Corrige E43.
  D-M17-53 gel alpha v2 (m2 auteur, m1 certifieur) -- 8 + 10.1, G-dt et
    G-k muettes a la lettre (FAIT 4). Corrige E44.
  D-M17-54 gel alpha v2 (m2 auteur, m1 certifieur) -- 10.3 contre
    D-alpha-9, P-A partiel par construction (FAIT 3). Corrige E44.
  D-M17-55 gel alpha v2 (m2 auteur, m1 certifieur) -- 4.4 "sans objet"
    contre la carte qu'il lit (FAIT 5) ; et v4 section 13 l.497 restee
    vraie sous l'ancienne regle (D-g-3), corrigee en v5 apres balayage
    des 39 (m2) et 55 (m1) lignes dependant du signe. Corrige E44.
  D-M17-56 gel temoin v6 (m2), NON CERTIFIE -- la tolerance de
    W-integrales renvoyee a une etiquette d'instrument (LD-4) dont le b
    ne vit pas sur (2.11) (D-g-1). Corrige v7.
  D-M17-57 gel alpha v3 (m2), NON CERTIFIE -- 10.1bis sans echelle :
    G-dt mordait des que son ecart etait le plus grand de trois bruits
    (D-g-2). Corrige v4/v5.
  D-M17-58 arbitrage consigne, sans defaut d'instrument (D-c-2) -- le
    signe n'est pas eprouve au pre-vol (SynthAlpha ne l'utilise pas, le
    factice bouge des deux cotes) ; garde proposee par machine 2,
    arithmetique sur la carte (table_factice[(p, w2, sgn)] == sF), non
    prise pour ne pas perimer l'ancre ; risque borne (lire_signes arrete
    sur carte incoherente ; un signe faux au run donne NON CONCLUANT DE
    FENETRE, pas un faux verdict). Entre avec D-M17-51 a la prochaine
    version.

85.7 LES ERRATA DE CORRESPONDANCE DE MACHINE 2 (par reference, sans E)
  Contre sa certification v1 (3f017a997b0b1812) : (1) LD-4 defendue par
  la valeur observee -> remplacee par l'epreuve de puissance ; (2) deux
  nombres lus dans un journal de repetition non opposable -> retires,
  l'incoherence de texte tenant sans eux. Contre son certificat de
  pre-vol v1 (dd10437b0d56c79c) : (3) "rien du temoin ne tourne sur du
  faux" et "je connais le verdict" -> retires, T-1/T-1b synthetiques
  (lecture m1 9ba3c24f41248035). Contre sa certification v2 et le
  certificat de pre-vol : (4) le plancher ecrit avec un facteur (p-2) de
  trop -- le seul qui aurait change un verdict s'il etait passe au code ;
  il n'y est pas passe (v2 porte le (p-2) dans la seule comparaison). (5)
  perimetre herite a trois points au lieu de quatre (85.6, D-M17-49).
  Forme commune, versee par elle : une verification exacte puis une
  conclusion plus large que ce qui a ete verifie ; ecrire la portee dans
  la meme phrase que le resultat.

85.7bis LE CANAL, CONSIGNE COMME PROPRIETE ET NON COMME FAUTE
  Le canal de transmission entre les deux machines a perdu dans les deux
  sens au cours de la sequence : l'ordre machine 2 6e176705468a4834
  n'est jamais parvenu a machine 1 ; sa note de pre-vol v2
  5575ac8cf96b298b a mis trois envois a arriver ; trois pieces machine 1
  (72bc452ec8eb6950, c6bc9fffc129ae89, 3c7c5f038fc8d29a) ne sont pas
  parvenues a machine 2 avant la certification de la v1 de cet acte, ce
  qui lui a coute un tour. Ce n'est la faute d'aucune machine. Forme
  retenue, celle du delta 84 : toute piece qu'une seule machine detient
  se DECLARE comme telle a la citation, et se retransmet avec l'acte.

85.8 LES LECTURES DECLAREES DE L'INSTRUMENT (docstring de 5fae2a8c94cf8685)
  La ou le gel dit "derive" sans donner la forme, l'instrument declare et
  etiquette. LD-1 (tol_R, dispersion de t_c/CAP) ; LD-2 (saturation lue
  sans tol_R, ordre 1, 2, 3, 3bis, 4, 4bis, 5, 6) ; LD-3 (base de T-1b,
  osc de l'enveloppe) ; LD-4 (tol_ordre, chronologie D-M17-47) ; LD-5
  (e/ln 10 consigne au temoin, relu a la porte) ; LD-6 (W-bascule) ; LD-7
  (plancher machine eps x N_pas) ; LD-8 (T-2a, T-2b, T-3b) ; LD-9 (FERMEE
  par E43) ; LD-10 (G-seuil, derniere fenetre) ; LD-11 (ajustements, eps
  d'appartenance) ; LD-12 (P-A, grille jouee, plancher de 10.3) ; LD-13
  (test depose en lignee) ; LD-14 (indice accessible par T_MAX) ; LD-15
  (ABSORBEE par E44) ; LD-16 (W-integrales NON LUE au plancher). Toutes
  contresignees par machine 2 (10d3160eef210015 section 3 ;
  baf75f462ab14119).

85.9 CE QUE CE DELTA NE FAIT PAS
  Il ne rouvre aucun gel certifie. Il n'edite aucune piece deposee
  (PB-1). Il ne mesure pas la constante A et ne la promeut pas. Il ne
  dit rien de la classe ponctuelle ni du quantique. Il ne prend pas les
  propositions (a), (b) de 85.4. Il ne re-derive pas lui-meme le 19/19 :
  cette re-derivation est due a sa certification et au depot des JSON.
  Il n'attribue aucun autre numero que N-70, E43, E44, E45, D-M17-46 a
  D-M17-58. La v2 n'en prend ni n'en retire aucun. Borne : 85.

EMPREINTES RE-DERIVEES LE 2026-08-28 (N-48), depuis un clone frais du
depot (e800c71) pour l'arbre, depuis les copies recues pour le reste.
PIECES CITEES (convention B, 16 hex ; detenteur declare) :
  arbre e800c71 : gels v7 8b083e9f109b5a8e 39750, v5 alpha 045c2435aaf623ce
    28998 ; certifications m1 6b2425dbf906205b, fe43f7c4d142bcdb ;
    certification m2 v3 baf75f462ab14119 ; contresignatures m1
    146f7dd9d81ace1d, d3a0d73a3139da3b ; pre-vol m2 v3 e70b639a04b8d136 ;
    prediction runs/prevol_temoin_v3_opposable.json 786a368878768d4b
    23350 ; instrument scripts/banc_qualification_machine1_v3.py
    5fae2a8c94cf8685 144725 ; moteur c8ed357b120352c4 (brut) ; carte
    fa109da92e582520 (brut) ; delta 84 fff42f489696c7ed.
  arbre 37ad1b6 (perimes) : gel temoin v5 0905a9b78ba40349 34961 ; gel
    alpha v2 35a70834b2a34514 21113 ; certifications 05068b3c945c9e9c,
    55079cecb71a853b.
  machine 2 (copies recues, a deposer avec l'acte) : ordre
    6e176705468a4834 (cite par elle, non recu par machine 1 : detenue
    machine 2 seule) ; certification de la v1 de cet acte
    57fcf4c644ba4a68 8439 ;
    certifications instrument v1 3f017a997b0b1812, v2 10d3160eef210015
    (script c2f0c401ba846394, log ac3988deb4021a57) ; pre-vols
    dd10437b0d56c79c, 5575ac8cf96b298b ; transmissions b4512952ba5ca3f4,
    b067debaeb0be3f5, 2ffbdde5a8716dca ; gels non certifies v6
    e9a7e7e2e2ed0354, alpha v3 3dad1c34b54bb9c3, v4 c261b6a5f34262e5 ;
    run temoin 030ebe36d2957cd7 (capture 10a7ce5688f515d5) ; run alpha
    031d85049f22813d (capture 0e7e56006d2e200a).
  machine 1 (a deposer avec l'acte) : instruments v1 3a932eabfaaf4307
    116438, v2 d74928ef093c96d0 133202 ; notes v3 63fc202bbfd91b80,
    e46ba9ef1ebb5c9b ; contresignatures 72bc452ec8eb6950 (3854 o),
    0f5ce102babf75dd, c6bc9fffc129ae89 (4397 o), d2e37736973a0725 ;
    lecture 9ba3c24f41248035 ; certification gels v6/v3 c98e89bad67c835b
    ; SUIVI 2026-08-27 3c7c5f038fc8d29a (5648 o). Les trois pieces
    72bc452ec8eb6950, c6bc9fffc129ae89, 3c7c5f038fc8d29a etaient detenues
    par machine 1 seule a la certification de la v1 (D-e-1) : elles sont
    RETRANSMISES avec la v2 et se deposent avec l'acte. Retirees, citees
    pour l'histoire : note v1 ac157c6450a30182, note v2 3a98cd5c7385d8d0
    (non envoyee, detenue machine 1 seule).
  runs (BOCAL4, a deposer avec l'acte) : out_banc/temoin
    (644240dc894c2733, d8ac838ce2d1bd48, c557a4fa5aa6bd28) ; out_banc/alpha
    (6d7d23130e9322f8, c30d8e6442bd934d, 932fe5bcd181b127).

=== FIN DU JOURNAL DELTA 85 ===
