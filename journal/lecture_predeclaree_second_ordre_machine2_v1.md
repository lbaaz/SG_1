# LECTURE PRE-DECLAREE -- CHANTIER DU SECOND ORDRE DE LA CONSTANTE A
# machine 2, 2026-09-13, ecrite AVANT la piece de derivation et AVANT
# l'ouverture des valeurs par point du run 91 (out_run_delta91/alpha_v13).
# Engagement de l'operateur : "go 1" (13/09). Piece de classe C, detenteur
# machine 2. Ce n'est PAS un gel (la plume des gels est a machine 1) :
# c'est le dossier de conception qui doit PRECEDER tout gel v8.

## 0. CE QUI EST DEJA SU AVANT CETTE PIECE -- DECLARE

Avant d'ecrire cette note j'ai lu : gel constante A v7 (sections 0-13),
gel alpha v5 (sections 2, 6, 7, 10), `acc_pu`, `ajustement_II` et
`ajuster_point_fixe` de l'instrument v13. J'ai ESQUISSE DE TETE, sans
piece, trois choses que la derivation doit re-deriver en exact et qui
peuvent donc etre fausses :

  E1  les deux equations de `acc_pu` s'eliminent EXACTEMENT en
      x'''' + (1 + w2^2) x'' + w2^2 x = g x^(p-1), x = x1 + x2 ;
  E2  x = A tau^(-alpha) (1 + c1 tau^2 + ...) donne
      c1 = (1 + w2^2) alpha (alpha+1) / ((p-1) K - P2),
      P2 = alpha (alpha+1) (alpha-1) (alpha-2) ; a p = 4, c1 = (1+w2^2)/60 ;
  E3  les exposants des MODES LIBRES x = x0 (1 + e tau^beta) resolvent
      (beta-alpha)(beta-alpha-1)(beta-alpha-2)(beta-alpha-3) = (p-1) K ;
      beta = -1 (translation de t*) en est racine ; les deux racines
      complexes ont Re beta = alpha + 3/2 = 3.5 / 2.833 / 2.3.

Je n'ai vu du run 91 que ce que porte ma memoire : les rapports P-A
1.13 / 0.38 / 0.17 et les dispersions/planchers 0.869 / 0.208 / 0.042.
Aucune valeur par point.

## 1. CE QUE LA PIECE VERIFIE, ET CE QUI LA FERAIT MORDRE

  C1  (E1) elimination symbolique depuis le texte de `acc_pu`.
      MORD si le reste (D^2+1)(D^2+w^2) x - g x^(p-1) n'est pas nul
      identiquement. Si C1 mord, le gel alpha v5 2.1 decrit un autre
      systeme que l'instrument, et tout le reste s'arrete.
  C2  (E2) c1 en exact (Fraction) aux trois degres, ET substitution :
      le residu de l'EDO a l'ordre tau^(-alpha-2) doit etre nul en
      exact. MORD s'il ne l'est pas.
      Test negatif : c1 perturbe de 1/1000 -> le residu doit etre non nul.
  C3  (E3) racines de l'equation des modes libres. MORD si beta = -1
      n'est PAS racine a l'un des trois degres (controle positif connu :
      la translation de t* est un mode libre exact).
  C4  biais de l'AJUSTEMENT II (le code de l'instrument, importe, pas
      re-frappe) sur serie synthetique tau^(-alpha)(1 + c1 tau^2) posee
      sur la grille nominale dt_2b de la fenetre :
      C4a  c1 = 0 -> |lnA_II - lnA| <= 1e-9 (sinon l'outil de projection
           est faux, la mesure du biais n'a pas de sens) ;
      C4b  MUTATION : c1 -> 2 c1 doit doubler le biais a 1e-2 relatif
           pres (linearite ; sinon le biais n'est pas celui du terme) ;
      C4c  le biais se CONSIGNE par (p, w2), rapporte au plancher
           delta'/((alpha+2)(alpha+3)) du gel v7.

## 2. CE QUI INVALIDERAIT LE CHANTIER LUI-MEME (a lire au resultat)

  I1  Si E3 tient, les modes libres complexes a Re beta = alpha + 3/2 se
      placent ENTRE tau^2 et tau^4 aux trois degres, et a p = 7 seulement
      tau^0.3 au-dessus de tau^2. Leur amplitude est LIBRE (fixee par la
      condition initiale, donc par le point) et leur phase oscille en
      ln tau. Consequence ecrite avant calcul : **soustraire c1 ne laisse
      PAS un residuel en delta'^2** (la projection de l'etat du 13/09,
      "residuel en delta' x plancher, gain 1.8e+03 a 3.8e+04", presuppose
      l'absence de modes libres sous tau^4 et devient NON FONDEE) ; le
      residuel est en delta'^((alpha + 3/2)/2) fois une amplitude
      inconnue. Le gain reel se MESURE, il ne se projette pas.
  I2  Si le biais C4 est tres inferieur a la dispersion du run 91, le
      premier ordre n'est pas ce qui limite P-A : le plancher du gel est
      une borne lache, et le chantier est la REECRITURE DU PLANCHER, pas
      une correction.

## 3. LECTURE A POSTERIORI SUR LE RUN 91 -- NON OPPOSABLE, DECLAREE

Le run 91 est depose et ses agregats sont connus de moi : cette lecture
ne peut RIEN confirmer au sens de N-70. Elle sert a savoir si le chantier
vise la bonne grandeur. Regle ecrite avant ouverture :

  obs(p, w2, c)  = ln(g A_II^(p-2) / K) / (p - 2)  lu au run 91 (v13, m2)
  pred(p, w2)    = biais C4 (ne depend pas de c a cet ordre)
  COMPATIBLE     si |obs - pred| <= 3 x dispersion_lnA_91(p) aux 18 points
  DE SIGNE       si sign(obs) = sign(pred) aux 18 points sans COMPATIBLE
  NON            sinon -- et alors le premier ordre ne rend pas compte de
                 l'ecart, c'est a consigner tel quel.
  Le rapport obs/pred se CONSIGNE aux 18 points, quel que soit le cas.
  Si la cle attendue n'existe pas au JSON sous ce nom : la lecture le DIT
  (NON JOUE), elle ne resout pas la definition en silence.

-- FIN lecture_predeclaree_second_ordre_machine2_v1 --
