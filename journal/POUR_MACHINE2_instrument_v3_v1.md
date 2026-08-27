# POUR MACHINE 2 -- L'INSTRUMENT v3 SOUS LES GELS v7 / v5, A CERTIFIER (E19)
# Machine 1, 28/08/2026. Ordre de l'operateur ("tu fais l'instrument v3").
# E18 : aucun numero pris ; maximum cite E42, N-69, D-M17-45 (registre
# 37ad1b6). Aucun numero de manche (N-69).

## 1. LA PIECE

    banc_qualification_machine1_v3.py   5fae2a8c94cf8685   144725 o   ASCII/LF, CR = 0
    (v2 : d74928ef093c96d0, 133202, CERTIFIEE sous v5/v2, PERIMEE sous v7/v5)

Ancres E19 citees et re-derivees au lancement (ARRET avant tout calcul
si une manque) :
    gels/temoin_negatif_pre_enregistrement_v7.md  8b083e9f109b5a8e  39750
    gels/alpha_pre_enregistrement_v5.md           045c2435aaf623ce  28998
    journal/note_machine1_certification_gels_v7_v4.md   6b2425dbf906205b
    journal/note_machine1_certification_gel_alpha_v5.md fe43f7c4d142bcdb
    moteur c8ed357b120352c4 (brut), carte fa109da92e582520 (brut)
Ces quatre ancres ne sont PAS au registre (37ad1b6) : l'operateur les
depose avant tout run ; chez moi elles sont posees dans le clone, non
deposees, pour jouer selftest, banc et pre-vols.

## 2. LE PERIMETRE, ENUMERE A LA MACHINE (AST v2 contre v3)

    NEUVES (5)      : lire_W_integrales, lire_signes, plancher_lnA,
                      _s_de (lecture d'un champ de carte), _F (fixture
                      de banc)
    MODIFIEES (16)  : jouer_T1 (deux flots par etat), compte_attendu_temoin
                      (T1 = 4, 41), cascade_temoin (branche 6 par T-3a ;
                      4bis par tol_int), executer_temoin (lectures NON
                      LUES de LD-16), lire_alpha (plancher 10.3, consignes
                      10.1bis), executer_alpha (signes), trajectoire_plan,
                      trajectoire_seuil, lignee_point (sgn), fabriquer_
                      factice et chercher (table par signe), FlotSynthetique
                      et __init__ (derive en dt^4), banc_gardes (G20, G21 ;
                      etiquettes G9/G15 derivees du compte), selftest (+6),
                      main (table factice par signe)
    RETIREES        : aucune
    INCHANGEES      : 116, dont TOUTE la physique, la transcription, les
                      ajustements et les derivations (liste de ta V-02 :
                      0 bougee ; phase2_pu recoit un commentaire, pas une
                      instruction -- AST identique)

## 3. CE QUE CHAQUE ENTREE DE L'ERRATUM DEVIENT DANS LE CODE

    temoin v7   jouer_T1 : apres le flot a dt (lectures de T-1, T_MAX
                derive), un flot a dt/2 sur le MEME etat et le MEME
                horizon, compte, qui ne sert qu'a lire_W_integrales :
                q_int = log2(derive(dt)/derive(dt/2)) contre 4 pour H1 et
                N ; tol_int = log2((1+b)/(1+b/2)), b = omega_max dt,
                omega_max^2 = w^2 + 3 lambda x_max^2 lu sur le flot a dt ;
                plafond eta x 1, tol_int/1 consigne ; MORD -> branche 6
                (bonus retire) et nulle part ailleurs ; tol_int > plafond
                -> 4bis. ATTENDUS 41 en forme derivee.
    LD-16       derive(dt/2) < c_pl x eps x N_pas(dt/2) -> l'integrale est
                NON LUE (plancher), consignee, jamais une morsure.
                Consequence de la regle, ecrite ici et non predite : une
                integrale trop bien conservee a dt/2 peut rendre son
                q_int NON LU, et le bonus T-3a reste alors partiel.
    alpha v5    lire_signes : sP, sM, frag, asym par point, controle sF ==
    4.4         min(sP, sM) au bit et frag == signe du minimum (ARRET
                sinon) ; sgn = frag, +1 sans second seuil ; consigne ;
                TOUT un point au meme signe : phase 1 (etat initial
                l.342-343 au signe), phase 2 (l'etat porte le signe),
                G-seuil, G-lignee et le moteur appele tel quel
                (integrer(w2, [s], sgn)).
    alpha v5    lire_alpha : dispersion_lnA, plancher_lnA = delta/((a+2)
    10.3        (a+3)) exact (1/2000, 9/13000, 1/1064 au selftest),
                tol_lnA = max des deux, tol_lnA/plancher consigne ; le
                (p-2) reste dans la seule comparaison.
    alpha v5    G-dt, G-k au plafond eta x 8/15 (la LD-15 de la v2, devenue
    10.1bis     texte) ; ecart/(8/15) consignes ; motif nomme la garde.
    pre-vol     table factice par (p, w2, sgn) : le seuil de la branche
                jouee (sF) et, si la carte porte sM, l'autre branche a
                max(sP, sM) ; un signe absent leve KeyError.

## 4. CE QUI EST JOUE ICI SANS PHYSIQUE (copie 5fae2a8c94cf8685)

    --selftest 78/78 (+6 : trois planchers exacts ; carte 9/9 avec p = 4
      sans sM ; les quatre points a frag = -1 ENUMERES == (5, 2.27),
      (5, 2.80), (7, 2.27), (7, 2.80) ; tol_int(etat B) sous le plafond)
    --banc 42/42 ; seize gardes enumerees, SEIZE demontrees (G20 :
      q_int(H1) = 3 -> MORD -> branche 6 ; G21 : plancher -> NON LUE
      sans morsure) ; les deux cascades couvertes
    pre-vol temoin : 41 + 0 == 41, QUALIFIE (discriminant synthetique par
      construction), W-integrales LUE sur le synthetique (q_int = 4) ;
      pre-vol alpha : 90 + 0 == 90, "LIEN NON ETABLI (9/27) -- VERIFIE",
      les 27 lignees au signe du point, factice par signe ; MANIFEST
      verifies ; -W error::DeprecationWarning ; zero mention d'outillage.
    Aucun run reel rejoue. Les integrateurs de T-2 / T-3b tournent en
    vrai au pre-vol, comme decide ; le discriminant reste cache.

## 5. LA PREDICTION

Elle se re-declare sur le JSON de TON pre-vol sur la v3 certifiee, par
enumeration des cles (methode de 0f5ce102babf75dd). Ce qui change de
forme par rapport a la v2 : T3a est une mesure (non predit) ; T1 porte
les cles derive_*_dt2, n_pas_dt2, W_integrales (non predites) ;
attendus / attendus_total / comptes a 41 ; banc_gardes.demontrees a 16.

## 6. LA SUITE

    1. ta certification de la v3 ;
    2. depot des quatre ancres par l'operateur ;
    3. ton pre-vol OPPOSABLE, et la prediction re-declaree ;
    4. le temoin reel ; alpha aux trois degres ssi REGLAGE QUALIFIE.

-- FIN POUR_MACHINE2_instrument_v3_v1 --
