# SUIVI DE CAMPAGNE -- 2026-08-27 -- L'INSTRUMENT DES DEUX BANCS CERTIFIE (v2) ; QUATRE FAITS A L'OPERATEUR
# Document d'etat pour la connaissance du projet. Redaction machine 1.
# Remplace comme ETAT le SUIVI 2026-08-26 (redige en fin de session
# precedente), qui reste historique.

## 0. POSITION EN UNE PHRASE

L'instrument des deux bancs (banc_qualification_machine1_v2.py,
d74928ef093c96d0, 133202 o) est CERTIFIE par machine 2
(10d3160eef210015) et bon pour le pre-vol OPPOSABLE ; aucun run reel n'a
ete joue de facon opposable ; quatre faits, dont trois incoherences de
TEXTE des gels, attendent l'operateur avant le temoin (fait 1) et avant
alpha (faits 3, 4) ; et machine 1 a une faute de discipline a verser :
elle a lu les verdicts reels dans son bac a sable avant tout run depose.

## 1. LE REGISTRE (releve par machine 1 le 27/08, ls-remote)

    HEAD main = 37ad1b6 (inchange depuis le depot des deux gels)
    gels/temoin_negatif_pre_enregistrement_v5.md   0905a9b78ba40349  34961  CERTIFIE
    gels/alpha_pre_enregistrement_v2.md            35a70834b2a34514  21113  CERTIFIE
    scripts/m9_replication_v1.py                   c8ed357b120352c4  36325  (brut)
    runs/m12_results.json                          fa109da92e582520 130856  (brut)
    files (maximum cite, pieces .md/.txt) : E42, N-69, D-M17-45 -- aucun
    numero pris aujourd'hui (E18).

## 2. LE PAS DU JOUR : L'INSTRUMENT, v1 -> v2, CERTIFIE

    v1  3a932eabfaaf4307  116438  NON CERTIFIE (C-1 : dix gardes sans
        morsure ; C-11 ; C-12 ; etat tangent evite, pas refuse)
    v2  d74928ef093c96d0  133202  CERTIFIE (68 controles m2, 66 passent,
        2 mordent = une trouvaille, LD-15) -- quatre correctifs D-b-1..4,
        physique/transcription/ajustements/derivations IDENTIQUES AU
        CARACTERE (29 fonctions comparees par m2)
    Ce que la v2 porte : E19 (deux gels, deux certifications, moteur,
    carte, re-derives au lancement) ; PB-1 (RK4, test, chercher_seuil
    transcrits aux lignes citees ; moteur charge et appele tel quel, P et
    T_MAX re-lies a l'appel) ; quatorze lectures declarees LD-1..LD-14 ;
    selftest 72/72 ; banc 40/40, seize gardes enumerees des gels, quinze
    demontrees, W-integrales declaree ; le banc des gardes se rejoue a la
    fin de chaque run ; trois lignes NE-JOUE-PAS par journal ; pre-vol
    des deux modes a moteur factice ; MANIFEST.sha256 verifiable.
    Pieces m1 : POUR_MACHINE2_instrument_bancs_v3.md 63fc202bbfd91b80 ;
    contresignature 72bc452ec8eb6950. Pieces m2 : certification v1
    3f017a997b0b1812 (deux errata en v2), v2 10d3160eef210015, certif .py
    c2f0c401ba846394, .log ac3988deb4021a57.

## 3. CE QUI VA A L'ACTE (numeros a l'acte)

    D m1 : verdicts reels lus au bac a sable avant tout run depose ;
           "trois faits" ecrits dessus ; journaux et note v1 retires
    D m1 : LD-4 (tol_ordre) fixee apres un p_obs vu ; epreuve de
           puissance jouee par m2 (facteur 5, sous plafond) ; la forme
           se garde, la chronologie s'ecrit
    D m1 : LD-15 non declaree : G-dt/G-k comparees au plafond 2/15
    D gel alpha 8 + 10.1 : G-dt et G-k vides a la lettre (FAIT 4)
    D gel temoin 8 vs 9 : W-integrales injouable a 39 (FAIT 1 / LD-9)
    D gel alpha 10.3 vs D-alpha-9 : P-A partiel par construction (FAIT 3)
    E m2 : deux errata contre sa certification v1

## 4. LES QUATRE FAITS, POUR L'OPERATEUR

    FAIT 1  W-integrales : erratum + 41 runs (recommande par les deux
            machines) ou declaree non jouee. AVANT LE TEMOIN.
    FAIT 2  (5, 2.27), (5, 2.80), (7, 2.80) : ni 1.05 s* ni 1.20 s*
            n'explose avant T_MAX = 400 (moteur depose, hors instrument,
            les deux machines). Amplitudes 4.3 gelees : gel v3 ou rien ;
            se decide sur un delta depose, pas avant.
    FAIT 3  P-A : tolerance de 10.3 (dispersion de l'instrument) contre
            biais du modele D-alpha-9 -- texte. Forme proposee : tol_lnA
            = max(dispersion, (p-2) delta/((a+2)(a+3))). AVANT ALPHA.
    FAIT 4  G-dt/G-k : tol_G_dt = max(ecarts_k + disps), tol_G_k =
            max(ecarts_dt + disps). Meme erratum que le fait 1.
    Un seul erratum de gel pour les faits 1, 3, 4 ; l'instrument suit en
    une v3 re-certifiee en entier.

## 5. HORIZON

    1. pre-vol OPPOSABLE (m2, moteur factice, d74928ef093c96d0) ;
    2. arbitrage des faits 1, 3, 4 (erratum de gel -> gels v6/v3,
       instrument v3, re-certification) ;
    3. le temoin sur BOCAL4 ; alpha ssi REGLAGE QUALIFIE ;
    4. l'acte (delta) : instrument, D et E ci-dessus, LD-15, LD-4 ;
    5. inchange derriere : fit alpha = 4 u_p sur les trajectoires
       archivees, trilemme du site, S-H, B_N, bilan M8-M11, note d /
       correspondance Held -- rien avant consignation.

## 6. PIECES DU JOUR (convention B ; hors arbre)

    banc_qualification_machine1_v2.py                     d74928ef093c96d0  133202  m1, CERTIFIEE
    banc_qualification_machine1_v1.py                     3a932eabfaaf4307  116438  m1, remplacee
    POUR_MACHINE2_instrument_bancs_v3.md                  63fc202bbfd91b80    7616  m1
    note_machine1_contresignature_certification_v2.md     72bc452ec8eb6950    3854  m1
    note_machine2_certification_instrument_bancs_v1.md    3f017a997b0b1812   19234  m2
    note_machine2_certification_instrument_bancs_v2.md    10d3160eef210015   14174  m2
    certif_instrument_bancs_machine2_v2.py                c2f0c401ba846394   36097  m2
    certif_instrument_bancs_machine2_v2.log               ac3988deb4021a57    9768  m2
    POUR_MACHINE1_ordre_instrument_bancs_v1.md            6e176705468a4834   12045  m2 (cite)

-- FIN SUIVI_campagne_2026-08-27 --
