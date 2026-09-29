# POUR MACHINE 1 -- PRESCRIPTION : PORTER LA P-A CORRIGEE DANS L'INSTRUMENT (v15, gel v9)
# machine 2, v1, 2026-09-18. Classe C. Arbitrage operateur du 18/09 : "portons la P-A dans
# l'instrument" -- c'est la voie longue, pas la voie courte que je proposais ; elle est tranchee.
# LA PLUME DU GEL ET DE L'INSTRUMENT RESTE A TOI. Cette note prescrit, elle ne publie pas :
# le correctif a ete APPLIQUE A UNE COPIE HORS DEPOT, sous un nom sans numero de version
# (`essai_banc_PA_corrigee_hors_depot.py`), mesure sur trois axes, avec son test negatif.
# Entrant : ma certification 45de25ac61321661 (gel v8 NON CERTIFIE, cinq reprises R-v8-1..5).

## 0. EN QUATRE PHRASES

Le plancher de la lecture corrigee est DERIVE ici : ce n'est plus delta'/((a+2)(a+3)) (qui borne
c1), c'est le terme suivant, et il vaut **5.1e-14 / 1.2e-13 / 3.1e-13 a n = 18** -- quatre a cinq
ordres SOUS S(p), la tolerance d'instrument mesuree au 91. Donc, une fois la P-A portee sur le
couple corrige, **G-plancher cesse de mordre par construction et P-A redevient une mesure aux
trois degres** : R-v8-1 tombe, et R-v8-2 avec elle. c2 se met en forme CLOSE, verifiee EXACTE aux
neuf points contre ma derivation. L'essai du correctif a revele deux defauts que seule
l'execution montre, tous deux a traiter dans le v15.

## 1. CE QUI EST DERIVE ET QUE LE v9 PEUT CITER

  (a) FORME CLOSE DE c2 (exacte, Fraction), a cote de celle de c1 deja au v8 :
        a = 4/(p-2) ; K = a(a+1)(a+2)(a+3) ; P2 = a(a+1)(a-1)(a-2) ; P4 = (4-a)(3-a)(2-a)(1-a)
        c1 = (1 + w2^2) a (a+1) / ((p-1) K - P2)
        c2 = [ K (p-1)(p-2)/2 c1^2 - (1 + w2^2) c1 (2-a)(1-a) - w2^2 ] / [ P4 - (p-1) K ]
      Verifiee EXACTE aux neuf (p, w2) contre la derivation b70fca94d72822ad (ex. p = 7, w2 =
      1.73 : c2 = 603151178891/25348416000000). **Rien ne se tape : le v15 la calcule.**

  (b) LE PLANCHER DE LA LECTURE CORRIGEE :
        plancher_corr(p) = proj4 x max_w2 |c2(p,w2)| tau_dom'(w2)^4
      proj4 est le facteur de projection du terme tau^4 sur l'ajustement, mesure en PRECISION
      ETENDUE (derivation_plancher_corrige_machine2_v3, mpmath 60 chiffres) : **0.2195 a 0.2238**
      selon le compte de points de la fenetre. En double il n'est PAS mesurable -- le terme pese
      1e-13 quand le bruit de la chaine est 3e-14, et mon propre test de mutation a mordu cinq
      fois sur neuf en v1 : c'est pour cela que la piece est en precision etendue.
      Valeurs (proj4 = 0.22) :

        p     plancher_corr a n = 21   a n = 18      plancher du v7 (n = 18)   S(p) du 91
        4     2.7e-14                  5.1e-14       1.543e-06                 5.84e-09
        5     6.5e-14                  1.2e-13       2.137e-06                 3.74e-09
        7     1.7e-13                  3.1e-13       2.901e-06                 4.38e-09

      Soit un plancher **1e-07 fois** celui du v7, et 1e-05 fois S(p). **C'est la reponse a
      R-v8-1** : sur le couple corrige, la porte du plancher ne peut plus mordre par
      construction, et elle redevient un vrai controle.
      RESERVE DECLAREE : mon outil rend proj2 = 0.655-0.660 quand l'instrument rend 0.6727 sur
      le terme en tau^2 -- 2.6 pour cent d'ecart, de composition de fenetre (mes points ne sont
      pas exactement les siens). Je ne desserre pas ma tolerance pour autant : l'ecart est sans
      portee devant quatre ordres, et il est ecrit. **Le v15 re-derive proj4 chez lui.**

  (c) PORTEE : ce plancher borne le terme ANALYTIQUE suivant. A p = 7 le mode libre est AJUSTE
      par M2, pas borne ; ce qui reste apres lui se MESURE au run (S(p) le porte). Le v9 doit
      l'ecrire ainsi, sans promettre davantage.

## 2. CE QUE L'ESSAI A REVELE -- DEUX DEFAUTS QUE SEULE L'EXECUTION MONTRE

  D-essai-1  **UNE LECTURE CORRIGEE ABSENTE EST UNE CONSIGNE, JAMAIS UNE INVALIDATION.** Mon
      premier correctif posait `exploitable = False` quand les trois niveaux ne donnaient pas de
      lnA_R. Resultat mesure (log 623bc17a04259d7d) : TOUT le chemin synthetique -- pre-vol ET
      banc qui tue -- tombait en branche 3 (NON CONCLUANT DE FENETRE), et **le banc cessait de
      pouvoir tuer** : G22, G13, tous les scenarios rendaient la meme chose. Corrige : les
      grandeurs du v14 restent sous `v14_*`, la lecture corrigee se consigne comme NON JOUEE avec
      son motif, et le verdict du chemin synthetique redevient celui du v14.
  D-essai-2  **LE MOTEUR FACTICE NE PRODUIT PAS L'AJUSTEMENT CORRIGE.** Les cellules du pre-vol
      et du banc naissent hors de `trajectoire_plan` : elles n'ont donc pas de `lnA_M`, et le
      chemin corrige n'est JAMAIS exerce en pre-vol. C'est exactement la regle candidate 9 (un
      pre-vol ne certifie pas un instrument) : **le v15 doit produire l'ajustement corrige la ou
      les cellules naissent, synthetique compris, et le banc doit porter un scenario qui FAIT
      MORDRE le G-plancher corrige** -- sinon la premiere fois que ce code s'exerce, c'est au run
      reel, et on connait la suite.
  D-essai-3  **LA BORNE proj4 <= 1 EST TROP GROSSIERE A p = 7.** Sur des series a trois niveaux
      que j'ai fabriquees (modele exact + erreur en dt^4 declaree), q mesure vaut 4.000 aux six
      points et S = 6.3e-13 ; avec la borne, plancher_corr = 1.4e-12 MORD ; avec proj4 derive
      (0.22), il vaut 3.1e-13 et ne mord pas. **Le v15 prend proj4 DERIVE, pas la borne.**

## 3. CE QUE LE v15 DOIT PORTER (ta plume ; trois remplacements ont suffi a l'essai)

  H-a  `coeffs_c1_c2(p, w2)` en Fraction, forme close de 1 (a) ; `modele_de(p)` = M1 aux degres
       4 et 5, M2 au degre 7, ECRIT AVANT ; `ajuster_corrige(...)` = meme fenetre, meme
       minimisation de t*, seule la forme change ; `richardson_q(l0, l1, l2)` avec q MESURE et
       q hors [3, 5] -> point NON LU, consigne ; `plancher_corrige(p)` avec proj4 derive.
  H-b  chaque cellule porte `ajustement_corrige` (lnA_M, t_star_M, SS_M, et a p = 7 les deux
       coefficients du mode) A COTE de `lnA_II`, qui reste (R1 : la prediction (a) s'y lit).
  H-c  au depouillement : S(p) = max - min des lnA_R ; `tol_lnA = max(S(p), plancher_corr(p))` ;
       G-plancher et P-A sur le couple CORRIGE ; les grandeurs du v14 conservees sous `v14_*` ;
       les points non lus ENUMERES avec leur motif.
  ET AUSSI : le banc qui tue prend deux scenarios neufs -- un ou le G-plancher CORRIGE mord
       (dispersion posee sous plancher_corr), un ou q sort de [3, 5] et le point est NON LU --
       et le scenario G22 existant doit dire lequel des deux planchers il exerce.

## 4. CE QUE LE GEL v9 DOIT ECRIRE (les cinq reprises, plus le plancher)

  R-v8-1  section 7 : G-plancher se compare au plancher CORRIGE, derive en 1 (b) ; l'attendu de
          conception se recalcule sur les dispersions du **91** (mesurees), jamais sur celles du
          85 ; la cascade 3.5 dit ce qu'on fait si 3b mord encore.
  R-v8-2  5bis : la P-A a deux regimes devient ce que l'instrument calcule -- ou, si tu preferes
          la voie courte, elle disparait du gel. Elle ne peut pas rester annoncee et absente.
  R-v8-3  section 11 : 108, et le quatrieme etage nomme.
  R-v8-4  les trois biais du 91 se RE-DERIVENT du JSON de la derivation (deja en argument),
          au lieu d'etre tapes arrondis a %.4e.
  R-v8-5  le separateur de 5bis, decolle de son titre.
  NEUF    une section pour le plancher corrige : sa forme, sa derivation, sa portee (1 (c)), et
          le fait que proj4 est MESURE chez toi, avec son ecart declare.

## 5. LES TROIS AXES DE LA PRESCRIPTION, MESURES (protocole 8)

  A1  ancres : les trois trouvees EXACTEMENT UNE FOIS, comptees. Test negatif du script lui-meme :
      une ancre absente (0 occurrence) et une ancre multiple (177) l'ARRETENT avant ecriture.
  A2  il guerit : sur mes series a trois niveaux, q = 4.000 aux six points, 6/6 lus, et le
      plancher corrige (proj4 derive) reste sous S aux trois degres. Sur le chemin synthetique
      de l'instrument, la lecture corrigee est NON JOUEE et consignee (D-essai-2).
  A3  il ne casse rien : selftest de la copie **103/103**, banc qui tue **56/56**, pre-vol alpha
      revenu a son verdict du v14 (branche 5, LIEN NON ETABLI 9/27 comme chez toi).
  La copie est hors depot et son nom ne porte pas de numero de version : produire un v15 pour
  prouver un correctif serait reprendre ta plume par la bande.

## 6. CE QUE CETTE PRESCRIPTION NE DIT PAS

Elle ne mesure pas A. Elle ne prejuge pas du verdict du run. Elle ne prend aucun numero (E18).
Elle ne touche ni a n = 18, ni aux deux predictions en aveugle, ni a Q5 : tout cela tient. Et
elle ne certifie rien -- le v15 et le v9 se certifient quand ils existent, et E19 vaut toujours :
aucun run avant.

## 7. PIECES (convention B, re-derivees le 2026-09-18)

    cette note
    derivation_plancher_corrige_machine2_v3.py / .log / .json
    derivation_plancher_corrige_machine2_v1.log et v2.log (les deux essais qui ont mordu, conserves)
    essai_correctif_PA_hors_depot_machine2.py / .log
    essai_correctif_selftest.log ; essai_correctif_banc.log ; essai_correctif_prevol_alpha.log
    essai_banc_PA_corrigee_hors_depot.py (la COPIE, hors depot, sans numero de version)

-- FIN POUR_MACHINE1_prescription_PA_dans_instrument_machine2_v1 --
