# SUIVI DE CAMPAGNE -- 2026-08-28b -- DELTA 85 DEPOSE (a4a907a) ; RELEVE 54/54 AU BIT ; HORIZON = LA CONSTANTE A
# Document d'etat pour la connaissance du projet. Redaction machine 1.
# Remplace comme ETAT le SUIVI 2026-08-28 (9d639181f873299f), qui reste
# historique.

## 0. POSITION EN UNE PHRASE

Le delta 85 est depose : HEAD main = a4a907a (2026-08-28 01:50 +0200),
le numero 85 est pris au depot (66.5.c), et machine 1 a re-derive au
bit, sur un clone frais d'un depot devenu PUBLIC, les 54 empreintes
citees en fin d'acte -- 52 par sha256sum direct, 2 (les captures des
runs) par la transformation CRLF -> LF que la convention B declare ;
rien ne manque, et la prochaine etape est la constante A.

## 1. LE RELEVE (machine 1, clone frais, 2026-08-28)

    HEAD main = a4a907a, au-dessus de e800c71 : l'acte v2
    9c7ee2578464c94a ; la certification machine 2 v2 b4c3bcc4b19bda75
    (VERDICT : CERTIFIE. BON POUR DEPOT.) et sa v1 57fcf4c644ba4a68 ;
    les deux runs complets --
      runs/run_temoin_delta85 : resultats 644240dc894c2733,
        journal d8ac838ce2d1bd48, MANIFEST c557a4fa5aa6bd28 ;
      runs/run_alpha_delta85 : resultats 6d7d23130e9322f8,
        journal c30d8e6442bd934d, MANIFEST 932fe5bcd181b127 ;
    les gels non certifies v6/v3/v4, les trois transmissions, les
    pieces perimees de l'arbre 37ad1b6, le SUIVI 2026-08-27
    3c7c5f038fc8d29a, le delta 84 fff42f489696c7ed.
    L'ordre 6e176705468a4834 est DEPOSE
    (journal/POUR_MACHINE1_ordre_instrument_bancs_v1.md) : la piece
    detenue par machine 2 seule a la certification de la v1 entre au
    registre -- cette citation-la est soldee.
    Identites relevees au bit : moteur c8ed357b120352c4 =
    scripts/m9_replication_v1.py ; carte fa109da92e582520 =
    runs/m12_results.json.
    Controle d'exhaustivite : 54 empreintes citees en fin d'acte, 54
    retrouvees dans l'arbre ; les 2 exclusions declarees par l'acte
    (ac157c6450a30182, 3a98cd5c7385d8d0) sont absentes, conforme.
    Le depot est PUBLIC (clone sans authentification, 374 fichiers).

## 2. UN FAIT DE FORME, RELEVE (numerotation : E18, au prochain acte)

    Les deux captures des runs sont deposees en octets CRLF
    (journal/m2_run_temoin_reel.log, brut 3833ba551a390945 ;
    journal/m2_run_alpha_reel.log, brut 717b61caa5921aaa) alors que
    l'acte les cite sous leur empreinte convention B (NFC+LF) :
    10a7ce5688f515d5 et 0e7e56006d2e200a. Le sha256sum direct ne
    reproduit donc pas la citation ; la transformation CRLF -> LF la
    reproduit exactement, aux deux fichiers. Deux lectures, a
    l'arbitrage de l'operateur : (a) conforme -- la convention B
    definit l'empreinte apres normalisation, et le depot garde les
    octets d'origine de BOCAL4 (.gitattributes * -text) ; (b) le
    prochain acte prend un fait de forme et une regle d'ecriture
    (toute piece CRLF citee declare sa forme a la citation). Machine 1
    ne tranche pas ici et ne numerote rien.

## 3. FILES ET DETTES

    Consignes par le 85 : E jusqu'a 45, N jusqu'a 70, D-M17 jusqu'a 58.
    NON PRIS, a arbitrer : (a) une garde ne se compare jamais a une
    tolerance qui contient l'ecart teste ni a un maximum sans echelle ;
    (b) aucune physique du discriminant avant le run depose.
    Dettes ouvertes : D-M17-51 et D-M17-58 -> a la prochaine version de
    l'instrument (v4) ; double transcription de (2.11) contre l'article
    : machine 2 seule ; q_int(N) = 4.96 a l'etat B : consigne, non
    explique ; canal 85.7bis : la regle demeure (l'ordre est solde par
    le depot ; les captures relevent de la section 2).

## 4. HORIZON, DANS L'ORDRE

    1. la CONSTANTE A : un gel avec une fenetre plus pres de la
       singularite, pour que l'instrument et non le plancher de modele
       10.3 fixe la tolerance de P-A ; plume du gel a trancher (machine
       2 ou arbitrage) ; instrument v4, qui prend D-M17-51 (les deux
       en-tetes de code) et D-M17-58 (garde de signe au pre-vol,
       table_factice[(p,w2,sgn)] == sF) et se re-certifie en entier ;
       aucun run avant gel certifie.
    2. le temps jusqu'a l'explosion pres du seuil (s -> s*) : deriver
       avant de jouer.
    3. note d et correspondance Held : PAS DE SIGNAL (M17) et le profil
       verifie (85) -- DEBLOQUEES par le depot ; le registre est
       public, ce qui change la forme possible de l'envoi.
    4. inchange derriere : trilemme du site, S-H, B_N, bilan M8-M11 ;
       branche quantique bloquee sans estimateur derive (C2) -- le
       profil singulier classique reste le candidat de point de depart,
       a deriver.

## 5. PIECES DU RELEVE (convention B sauf mention "brut" ; arbre a4a907a)

    journal/journal_delta_85_deux_bancs_alpha_verifie_v2.md  9c7ee2578464c94a
    journal/note_machine2_certification_delta_85_v2.md       b4c3bcc4b19bda75
    journal/note_machine2_certification_delta_85_v1.md       57fcf4c644ba4a68
    runs/run_temoin_delta85/resultats_temoin.json            644240dc894c2733
    runs/run_alpha_delta85/resultats_alpha.json              6d7d23130e9322f8
    runs/prevol_temoin_v3_opposable.json                     786a368878768d4b
    scripts/banc_qualification_machine1_v3.py                5fae2a8c94cf8685
    gels/temoin_negatif_pre_enregistrement_v7.md             8b083e9f109b5a8e
    gels/alpha_pre_enregistrement_v5.md                      045c2435aaf623ce
    journal/POUR_MACHINE1_ordre_instrument_bancs_v1.md       6e176705468a4834
    journal/m2_run_temoin_reel.log   brut 3833ba551a390945 (NFC+LF 10a7ce5688f515d5)
    journal/m2_run_alpha_reel.log    brut 717b61caa5921aaa (NFC+LF 0e7e56006d2e200a)

-- FIN SUIVI_campagne_2026-08-28b --
