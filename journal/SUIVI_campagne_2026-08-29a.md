# SUIVI DE CAMPAGNE -- 2026-08-29a -- v8 CERTIFIEE (PREMIERE DU
# CYCLE) ; ERRATUM 7(i) ET N-70 EMIS ; LA FILE PASSE A L'OPERATEUR
# Document d'etat pour la connaissance du projet. Redaction machine 1.
# Remplace comme ETAT le SUIVI 2026-08-28e (551b2c620892553e). Nouvelle
# date, lettre a -- le "29f" en quarantaine etait une piece fantome.

## 0. POSITION EN UNE PHRASE

L'instrument du volet T est **CERTIFIE** (v8 4d8882a2223a5c74, note m2
2a618ffb180ea568 -- premiere certification du cycle, cinq versions,
neuf defauts D-I-1..9 tous LEVES) ; machine 2 a livre ses deux pieces
annoncees -- l'**erratum 7(i)** (13601ef21efdc024 : la clause porte
tolerance 2/2 en pas representables, compteur, portee, morsure) et
l'**enumeration N-70** (4ef8235b16f26210 : 240+3+4, et la trouvaille
des quatre cles libm DANS le perimetre) -- la contre-derivation m1
confirme les 4 (1.0 pas chacune) et en leve une seconde (deux cles a
emission conditionnelle, annexe a reprendre en v2) ; la file ne
contient plus que **l'OPERATEUR** (cinq decisions), puis pre-vol
opposable, puis run.

## 1. LE CYCLE INSTRUMENT v5 -> v8, CLOS (empreintes convention B)

    v5 b8a0f75323182e55  NON CERT.  D-I-3 (compteur fige avant les
       ajouts, arret qui MENT), D-I-4 (17 annonces / 24 joues),
       D-I-5 (empreinte de champ non reproductible inter-machines)
    v6 56c2ebfcfd84671e  NON CERT.  D-I-3/4/5 levees ; D-I-6 (bornes
       a l'ENVERS : x'' porte le pow, D'' la chaine exacte -- 1re
       comparaison inter-machines = FAUX ECHEC), D-I-7 (garde ecrite
       2 fois, lue 0)
    v7 9a6e8b6192d4f163  QUALIFIEE POUR LA MESURE  D-I-6/7 levees,
       le CUMUL mesure (427/801/max 2.0) ; D-I-8 (borne abrogee en 3
       chaines vivantes dont le JSON), D-I-9 (ecart_ulp sous-compte
       x2 au bord bas des binades -- latent : 3.65e11 pas du bord)
    v8 4d8882a2223a5c74  **CERTIFIEE**  BORNE_ULP unique (1 decl.,
       19 citations), ecart_ulp en PAS REPRESENTABLES (forme audit
       m2, sans garde +-0 : deux instruments, une regle, bords
       compris ; +-0 -> 2^63 consigne partage)
    Constructions : 81730d2b / 125733fc / 0239eb20 / 02d1727d --
    composition epinglee v3 -> ... -> v8, comptes ASSERTES (D-I-4).
    Acquis transversaux du cycle : D-I-1 (un pre-vol n'asserte que
    ce que son factice determine ; sorties AVANT arret -- preuve
    vivante : le prevol ecrit et termine), D-I-2 (dossier vierge ou
    versionne, 2 preuves), chargeur 9bis au contrat (custody 4/4,
    forme canonique), critere 5.4 vivant (4/9 NON LUS = le cout que
    le gel declarait, 5|1.73 a 0.991 SUR LE FIL), c_pl non emis
    (LD-16 lit SOUS LE DEPOT, D-v5-1, arbitrage), TIRAGE opposable
    a8905b9b501b5601 AU BIT inter-machines, table des trois regimes
    FERMEE CROISEE : (2/0) machines mesuree des deux bords, (0/2)
    plumes, (2/2, 427/801) cumul.

## 2. L'INCIDENT DU FANTOME -- verse en entier, regles prises

    Une generation INTERROMPUE de machine 1 (23:27-23:48, le lot m2
    emis deux fois par le canal) a fait l'etape v8 entiere sans rien
    livrer ; quatre pieces restees en espace de travail, QUARANTAINE
    par canon : construction fbd24058c955139b, note 5f78a3ad6af7adfb,
    SUIVI "29f" 2ebe94ed09f2f5da, manifeste "v5" acfb8c4f5993ee6a ;
    produit contamine 903e6a00a60da080 DETRUIT. TROIS fautes m1
    versees : execute sans canon ; efface sans examen (rm -rf) ;
    deux canons TAPES puis corriges -- la 3e attrapee par la garde
    d'empreinte AVANT emission (4e instance de la famille du cycle,
    la 1re prise par une garde et non par le relecteur : les gardes
    payent). REGLES : m1 -- *toute piece trouvee s'authentifie par
    canon contre une emission declaree AVANT execution, lecture ou
    destruction, meme quand l'auteur probable est soi-meme* ; pendant
    m2, contresigne -- *la destruction est un acte d'authentification
    manque*. m2 verifie : aucun des cinq canons ne resout de son
    cote, rien n'a franchi ; la v8 certifiee se derive entierement
    du PIN v7.

## 3. CUSTODY -- l'etat des regles apres une semaine de canal qui perd

    Canon de lot = empreinte du manifeste (convention m2, symetrique).
    Noms : la version dans le nom quand il se reutilise (v4b) ; le
    prefixe machine quand deux cotes emettent la meme piece (m1_/m2_).
    Re-emission : ex-systematique -> **une reception CONSTATEE vaut
    mieux** ; se re-emet ce qui n'est pas accuse (regle m2 du 29/08).
    Accuse du lot m2 v3 : 4/15 recues resolues ; 3 demandees en
    re-emission (controle v8 script+log, derivation N-70
    30549837df01ab70) ; 8 citees-suffisent.
    Chaine des manifestes : m1 v1 c8354fdf / v2 67e62c25 / v3
    868a2138 / v4 aca82d47 + v4b 3ae3b08d / v5 e485889e ; m2 28-v2
    d7f69473 / 29-v1 fa9d4a2c / 29-v2 bc38fd32 / 29-v3 70e8bb36.
    SUIVI 28b b6d13e6a : sort toujours indetermine (operateur).

## 4. LES DEUX PIECES m2 -- et les deux trouvailles

    ERRATUM 7(i) (13601ef21efdc024, installe gels/ A COTE du gel
    a2e7ef3e inchange, numero A L'ACTE) : TIRAGE au bit sans
    tolerance, empreinte separee ; CHAMP sur les NOMBRES en PAS
    REPRESENTABLES, x'' <= 2 (pow inter-machines) et D'' <= 2
    (re-association inter-plumes), raisons DIFFERENTES, regime de
    7(i) = le CUMUL ; au-dela -> BANC NON JOUE. Borne MESUREE (4096
    pts, 2 plates-formes, 2 plumes, 3 regimes, des deux bords), NON
    PROUVEE, declaree telle. x**3 nomme-OUVERT (deplacerait T-1b et
    T-2). 7(iv) inchangee : concordantes, pas fideles.
    N-70 (4ef8235b16f26210 + derivation 30549837, a re-emettre) :
    856 feuilles, perimetre lu du depot, partition derivee jamais
    tapee. **TROUVAILLE m2** : 4 cles (tol_int, tol_int_sur_1 de
    T1/A et T3a/A) portent log2(sqrt) -- LA LIBM DANS LE PERIMETRE ;
    la reference deposee porte la valeur m2 ; un run m1 mordrait la
    custody AVANT toute lecture. Trois issues (run sur m2 /
    exemptions / tolerance libm au 9bis), AUCUNE implicite possible,
    arbitrage. **CONTRE-TROUVAILLE m1** (contre-derivation, 1.0 pas
    confirme x4) : perimetre pre-vol 247 vs reference 245 -- deux
    cles a EMISSION CONDITIONNELLE (ecart_a_4 de N-A, emises si LUE
    seulement ; statuts a l'appui) ; l'annexe A les predit
    identiques, elles seront ABSENTES ; depot SAIN ; **enumeration
    v2 due (plume m2)**, partition du run 238+3+4+2-absentes. Lecon
    jumelle de D-v5-1 : une cle se predit AVEC son regime.
    Fautes de sonde m1 versees : categorie (factice vs reel) et type
    (texte -> compteur), attrapees aux sorties ; regle : *une
    contre-derivation declare son REGIME avant de comparer.*

## 5. HORIZON -- la file, dans l'ordre

    1. OPERATEUR, CINQ decisions ecrites : (i) LD-16/depot (D-v5-1 :
       re-ancrage sur run v8 depose, ou LD-16bis v9 + reference
       neuve) ; (ii) issue N-70 a/b/c -- noter que (c) [tolerance
       libm au 9bis] et (i)-reancrage peuvent se resoudre d'un meme
       geste ; (iii) numero de l'erratum 7(i), a l'acte ; (iv) depot
       groupe (X) : v11+erratum, 9bis, v8+constructions, D-I-1..9,
       fantome+regles, fautes des deux plumes, N-70 v2 ; (v) sort du
       SUIVI 28b.
    2. Enumeration N-70 **v2** (plume m2, avec 30549837 re-emis pour
       contre-derivation entiere m1) -- puis DEPOSEE.
    3. Pre-vol OPPOSABLE sur BOCAL4 (E19, N-62), sous les decisions.
    4. RUN du volet T -- sur la machine que (ii) aura ecrite ; porte
       transposee, verdict lu par m2 au depouillement (D-M17-46).
       Attendu declare par le gel : branche 4, W-plancher aux quatre
       points -- le cout est ecrit d'avance.
    5. **D1, CHAT NEUF, CLASSE 3** -- INDEPENDANT de tout ce qui
       precede, peut s'ouvrir DES MAINTENANT : enumeration close des
       quatre formes de t*(s) (puissance / log / essentielle /
       bornee), derivation lue contre l'enumeration, continuation
       euclidienne, Gamma ~ exp(-S) candidat C2 ; puis D2 Chirikov,
       D3 estimateur, D4 UN run, D5 Held (note e f03ca623 SEULE).
    Derriere, inchange : temps-jusqu'a-l'explosion (deriver d'abord),
    trilemme du site, S-H, B_N, bilan M8-M11, dette (2.11)
    transcription -- SOLDEE par G-bis/erratum cote mecanique, la
    fidelite a l'article reste 7(iv) sur m2 seule, declaree.

## 6. PIECES NEUVES DE CE SUIVI (les cycles anterieurs : 28d/28e)

    banc v5/v6/v7/v8 : b8a0f753 / 56c2ebfc / 9a6e8b61 / 4d8882a2
    constructions    : 81730d2b / 125733fc / 0239eb20 / 02d1727d
    notes m1 reprise : be633ae9(v5) 5486e4fd(v6) 88deaec7(v7)
                       5a255faa(v8) ; cloture+contre-derivation N-70 :
                       (empreinte au manifeste v6 du jour)
    certifs m2       : f882b9c0(v4) c5c66dd1(v5) 483577e0(v6)
                       75dac8f4(v7) **2a618ffb(v8 CERTIFIEE)**
    erratum 7(i) 13601ef21efdc024 ; N-70 v1 4ef8235b16f26210
    champs : m1 0491b83e6893dbbf ; m2 f7f8be507eb5e9cb ; TIRAGE
    commun a8905b9b501b5601 ; seconde plume m1 b9185a3b85f37c73
    quarantaine fantome : fbd24058 / 5f78a3ad / 2ebe94ed / acfb8c4f
    (+ produit detruit 903e6a00) -- jamais emises, jamais opposables

-- FIN SUIVI_campagne_2026-08-29a --
