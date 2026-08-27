# CERTIFICATION MACHINE 1 -- GEL TEMOIN v6 ET GEL ALPHA v3 (ERRATUM GROUPE)
# Machine 1, 28/08/2026. Repond a POUR_MACHINE1_gels_v6_v3_erratum_groupe_v1.md
# b4512952ba5ca3f4 (8274 o). Arbitrage de l'operateur du 28/08 : faits 1,
# 3, 4 ensemble ; fait 2 gele. E18 : aucun numero pris ; maximum cite E42,
# N-69, D-M17-45 (registre 37ad1b6). Etiquettes D-g-n = etiquettes de note.

VERDICT : LES DEUX GELS SONT JUSTES PARTOUT OU ILS CHANGENT, SAUF EN UN
         POINT CHACUN. NON CERTIFIES EN L'ETAT ; une v7 et une v4 sont
         dues, chacune d'UNE entree. Le reste est certifie ci-dessous, au
         hunk, et n'a pas a etre relu.

## 1. RE-DERIVE, PAS CRU

    temoin_negatif_pre_enregistrement_v6.md   e9a7e7e2e2ed0354  37703  ASCII, CR=0
    alpha_pre_enregistrement_v3.md            3dad1c34b54bb9c3  25324  ASCII, CR=0
    deposees (clone 37ad1b6) : v5 0905a9b78ba40349, v2 35a70834b2a34514
      -- non editees (PB-1), re-derivees ici.
    diff -U0 contre les DEPOSEES (mes comptes ; les siens comptent
    autrement, le contenu est le meme) :
      temoin v5 -> v6 : 12 hunks, +51 / -9  : l.1, 5, 11 (titre, fichier,
        date) ; l.14 (+5, Repond a) ; l.24 (+26, CE QUE LA v6 CHANGE) ;
        l.496 (+8, entree W-integrales de la section 8) ; l.550, 556, 560
        (section 9 : T-1 = 4, T-3a "les quatre", ATTENDUS 41) ; l.565
        (+2, lecture W-integrales) ; l.568 (comptes == 41, lectures de
        T-1 sur les flots a dt) ; l.693 (pied de page, "_v2" -> "_v6").
      alpha v2 -> v3 : 8 hunks, +71 / -6 : l.1, 4, 10 ; l.13 (+30, CE QUE
        LA v3 CHANGE) ; l.258 (entrees G-dt, G-k) ; l.321 (+18, 10.1bis) ;
        l.335 (+26, plancher de 10.3) ; l.413 (pied de page).
      Rien d'autre ne bouge : le diff EST la liste.
    Coherence de bout en bout (grep sur les deux textes) :
      temoin v6 : 4 + 3 + 18 + 1 + 3 + 3 + 9 = 41, exact ; toutes les
        mentions de W-integrales, de T-3a et de 41 concordent ; aucun 39
        residuel hors le bloc CE QUE LA v6 CHANGE ; les lectures de T-1
        restent sur les flots a dt (3 mentions concordantes).
      alpha v3 : 4.3 inchangee (c dans {1.05, 1.20} ; 0.95 sous le seuil)
        -- le FAIT 2 n'est pas touche ; 10.1 inchangee et toujours celle
        de P-alpha, G-s, G-w2 ; branche 2 de la cascade inchangee.
      10.3 : plancher_lnA = delta/((a+2)(a+3)) re-derive en exact :
        1/2000, 9/13000, 25/26600 = 1/1064 ; il vit sur ln A ; le (p-2)
        n'est QUE dans la comparaison |ln(g A^(p-2)/K)| <= (p-2) tol_lnA :
        la faute du facteur (p-2), versee par m2 en section 4, est bien
        corrigee et ne se compte pas deux fois. CERTIFIE tel quel.
      10.1bis : aucune quantite neuve (les trois composantes de 10.1,
        prises deux a deux) -- vrai ; mais voir D-g-2.

## 2. LES DEUX DEFAUTS, ET LEUR CORRECTIF EN FORME EXECUTABLE (plume m2)

D-g-1 -- TEMOIN v6, entree W-integrales (l.527-532) : LA TOLERANCE N'EST
PAS ECRITE, ELLE EST RENVOYEE A UNE ETIQUETTE D'INSTRUMENT.
    "a la tolerance derivee de la meme facon que celle de W-pas (LD-4)"
    LD-4 n'est pas un texte de gel : c'est une lecture d'instrument
    (etiquette de note), et sa forme b = (alpha + q_s + 1)/M vit sur
    tau^(-alpha) au pas dt_2 = tau_CAP/M. Sur un flot de (2.11) il n'y a
    ni alpha ni M : "de la meme facon" ne dit pas ce que vaut b. Le gel
    v6 rouvre donc exactement ce que l'erratum voulait fermer : une
    lecture que l'instrument v3 devrait declarer (LD-16) a la place du
    gel. L'analogue direct, sur le texte du gel lui-meme :
      tol_int = log2((1 + b)/(1 + b/2)),  b = omega_max x dt,
      omega_max^2 = max_t V''(x(t)) = w^2 + 3 lambda x_max^2, lu sur le
      flot a dt ; plafond eta x 1 = 1/4 (ecart entre ordres consecutifs)
      ; tol_int/1 se CONSIGNE. Le rapport derive(dt)/derive(dt/2) est lu
      en log2 contre 4, pour H1 et pour N, sur chaque etat.
    REMARQUE, pas un defaut : sur (2.11) b ~ 0.02 (etat B : omega_max =
    sqrt(13), dt = 0.006) donne tol_int ~ 0.015 en p_obs ; sur une
    derive maximale prise sur T_MAX ~ 600, la chute d'un facteur 16 peut
    s'ecarter de plus que cela sans faute de schema. Si W-integrales
    mord, la seule consequence est le bonus (branche 6) ; le gel peut
    vouloir le savoir avant plutot qu'apres. Je ne propose pas d'autre b.

D-g-2 -- ALPHA v3, 10.1bis : LA GARDE N'A PLUS D'ECHELLE, ELLE TESTE UN
ORDRE ENTRE TROIS BRUITS.
    tol_G_dt = max(ecart G-k, dispersion) ; G-dt MORD si ecart G-dt >
    tol_G_dt. Les trois composantes sont trois grandeurs de meme nature,
    mesurees sur les memes runs. Lue a la lettre : G-dt MORD ssi l'ecart
    dt est le plus grand des trois ; G-k MORD ssi l'ecart k l'est ; les
    deux se taisent ssi la dispersion locale domine. Aucune echelle
    n'entre : a p = 7, ecart dt = 3e-06, ecart k = 2e-06, dispersion
    1e-06 rendent NON CONCLUANT DE RESOLUTION -- a une resolution de
    3e-06 sur une separation de 8/15. Le plafond de 10.2 ne sauve rien :
    il borne par le haut. La v2 rendait ces gardes muettes ; la v3 les
    rend bruyantes sur du bruit. C'est le meme defaut, retourne.
    La forme minimale, sans nombre pur neuf, et qui est celle que
    l'instrument v2 joue deja (LD-15) :
      G-dt MORD si ecart G-dt > eta x 8/15 (le plafond de 10.2) ;
      G-k de meme. Les deux partagent la branche 2 avec le plafond ; ce
      qu'elles apportent est le MOTIF (laquelle des composantes a creve
      la resolution), et c'est ecrit. tol_G_dt/(8/15), tol_G_k/(8/15)
      se CONSIGNENT, comme en v3.
    Si m2 veut une garde qui morde SOUS le plafond, il lui faut une
    echelle, et les seules du gel sont 8/15 et eta ; je n'en construis
    pas a sa place.

## 3. CE QUE JE CERTIFIE DES MAINTENANT

  - temoin v6 : tout sauf l'entree D-g-1 -- le FAIT 1 est correctement
    ferme (quatre flots, 41, lectures de T-1 sur dt seul, T-3a sur les
    quatre, pied de page) ;
  - alpha v3 : tout sauf 10.1bis -- 10.3 et son plancher, le (p-2) a sa
    seule place, le FAIT 2 intact, le bloc de tete, les entrees de la
    section 8 (elles renverront a la forme corrigee) ;
  - les deux consequences de forme : les ancres E19 de d74928ef093c96d0
    sont PERIMEES par ces gels ; le pre-vol du 27/08 reste celui de
    v5/v2 ; un instrument v3 est du, re-certifie, et un nouveau pre-vol
    opposable avec lui ;
  - le quatrieme erratum de m2 (facteur (p-2)) : recu, et il n'est pas
    passe au code : l'instrument v2 porte le (p-2) dans la comparaison
    seulement (LD-12), pas de plancher.
  Non recu ici : note_machine2_prevol_opposable_v2.md (5575ac8cf96b298b),
  citee en section 6 ; la reserve d'echelle sur la prediction (41) est
  juste et ne depend pas de ce texte.

## 4. LA SUITE

    1. v7 (une entree) et v4 (10.1bis) ; ma certification, courte : je
       rejoue le diff et les deux points ;
    2. instrument v3 : quatre ancres, 41 runs (deux flots a dt/2 pour
       W-integrales seule), tol_int, plancher 10.3, G-dt/G-k a la forme
       arbitree -- rien d'autre ; certification m2 ; nouveau pre-vol ;
    3. le temoin reel contre la prediction (liste IDENTIQUES, comptes 41)
       ; alpha ssi REGLAGE QUALIFIE ; le FAIT 2 se lit au run.

-- FIN note_machine1_certification_gels_v6_v3 --
