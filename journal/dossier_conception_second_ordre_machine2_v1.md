# DOSSIER DE CONCEPTION -- SECOND ORDRE DE LA CONSTANTE A
# machine 2, 2026-09-13. Engagement operateur "go 1" (13/09).
# Classe C, detenteur machine 2. PAS UN GEL : la plume du gel v8 est a
# machine 1 (roles m1/m2). Ce dossier dit ce qui est DERIVE, ce qui est
# MESURE a posteriori (non opposable), ce qui est FAUX dans la projection
# du 13/09 au matin, et les questions qu'un gel v8 doit trancher.

## 0. EN UNE PHRASE

Le terme du premier ordre neglige par le gel alpha v5 se derive en exact
(c1 = (1+w2^2) alpha(alpha+1)/((p-1)K - P2)) ; projete par l'ajustement II
de l'instrument, il rend a p = 4 et p = 5 l'ecart observe au run 91 A 2 %
PRES apres extrapolation de Richardson sur la jumelle G-dt, SANS parametre
libre -- lecture a posteriori, non opposable ; a p = 7 il ne le rend qu'a
+/- 20 %, et un point a 0.14, ce que la derivation attribue aux MODES
LIBRES en tau^2.3, dont l'amplitude n'est pas derivable.

## 1. CE QUI EST DERIVE (derivation_second_ordre_machine2_v1, 93 chk, 0 mord)

Lecture pre-declaree figee AVANT la piece : 99080e4822bf0108 (17:29).

  C1  Les deux equations de `acc_pu` (texte extrait a l'AST de l'instrument
      v13) s'eliminent EXACTEMENT en x'''' + (1+w2^2) x'' + w2^2 x = g x^(p-1).
      Reste symbolique nul ; test negatif (couplage mutile) : reste non nul.
      L'equation du gel alpha v5 2.1 est donc celle du systeme, sans reste.

  C2  x = A tau^(-alpha) (1 + c1 tau^2 + ...), coefficient tau^2 nul EN EXACT
      aux neuf (p, w2) ; c1 x 1.001 le rend non nul (neuf tests negatifs).

      p   alpha  K          P2        c1/(1+w2^2)   c1 tau_dom'^2    / plancher v7
      4   2      120        0         1/60          1/2646000        1/3
      5   4/3    3640/81    -56/81    1/58          1/2557800        65/261 = 0.249
      7   4/5    9576/625   216/625   5/318         1/2804760        133/795 = 0.167

      c1 tau_dom'^2 NE DEPEND PAS de w2 (tau_dom'^2 = delta'/(1+w2^2)). Le
      plancher du gel (delta'/((a+2)(a+3))) majore le vrai terme d'un facteur
      3 / 4 / 6 : c'etait une borne, pas le terme.

  C3  Modes libres x = x0 (1 + e tau^beta) :
      (beta-alpha)(beta-alpha-1)(beta-alpha-2)(beta-alpha-3) = (p-1) K.
      beta = -1 racine EXACTE aux trois degres (controle positif : translation
      de t*) ; les autres racines :

      p   reelle   complexes                    Re beta = alpha + 3/2
      4   8        3.5   +/- 4.2131 i           entre tau^2 et tau^4
      5   20/3     17/6  +/- 3.4921 i           entre tau^2 et tau^4
      7   28/5     23/10 +/- 2.8966 i           tau^0.3 AU-DESSUS de tau^2

      Amplitude et phase LIBRES (fixees par la condition initiale, donc par le
      point (w2, c)), oscillation en ln tau.

  C4  Biais de lnA_II sur serie synthetique A tau^(-alpha)(1 + c1 tau^2), code
      d'ajustement de l'instrument IMPORTE (ajuster_point_fixe, v13), grille
      dt_2b nominale, 180 points. c1 = 0 -> biais <= 1.4e-12 ; 2 c1 -> biais
      x 2 a 2.1e-5 pres.

      p   biais lnA (grille alignee)   / (c1 tau_dom'^2)   / plancher v7
      4   2.5425e-07                   0.6727              0.224
      5   2.6302e-07                   0.6727              0.168
      7   2.3986e-07                   0.6727              0.113

      Le facteur de projection 0.6727 est UNIVERSEL (forme de fenetre r = 1/10) ;
      au decalage de grille d'un demi-pas il vaut 0.6638 : **sensibilite de
      grille 1.3 %**, a porter comme tolerance de toute correction.

## 2. CE QUI EST MESURE A POSTERIORI -- NON OPPOSABLE (N-70), PORTEE DITE

(a) Section 3 de la lecture pre-declaree, jouee telle qu'ecrite : COMPATIBLE
    18/18. **Ce verdict est FAIBLE et je le dis** : a p = 4 et p = 5 la
    tolerance 3 x disp_91 contient aussi pred = 0 (obs/disp = 1.2 a 1.8) ;
    seul p = 7 (obs/disp ~ 3) discriminait. Ma regle ne pouvait pas mordre
    la ou elle devait trancher.

(b) exploration_richardson_second_ordre_machine2_v1 (NEE APRES (a), regle
    ecrite dans le docstring avant execution, script 9562f34b1b5d6d4a) :
    (obs - pred)/disp_91 valait ~1.0 aux douze points p = 4, 5 -- signature de
    l'erreur RK4 au pas dt_2b, que la jumelle mesure. Richardson q = 4 sur
    (dt_2b, dt_2b/2) :

      p   obs_R / pred aux six points          lecture
      4   1.021 1.006 1.004 1.023 1.014 0.998  EXPLIQUE
      5   0.989 0.981 0.988 0.989 0.990 0.988  EXPLIQUE
      7   0.821 0.138 0.905 1.187 1.094 0.909  NON (modes libres designes)

    Tests negatifs de la regle : pred = 0 -> NON partout ; pred x 2 -> NON.
    **Sensibilite a l'ordre suppose** : a p = 4, q = 3 donne 0.71-0.76 et
    q = 5 donne 1.13-1.14. Le "2 %" presuppose q = 4 ; l'ambiguite d'ordre
    pese +/- 13 % de pred (~3e-8) -- plus que le residu lui-meme.

(c) RELECTURE DU RUN 91 qui en decoule (portee : cellules du plan, v13, m2) :
    l'ecart P-A a p = 4 (1.13 de la tolerance) se decompose en ~79 %
    d'erreur d'integrateur au pas dt_2b (9.5e-7) et ~21 % du terme c1
    (2.5e-7). La "dispersion d'instrument" du 91 est, a p = 4 et 5,
    essentiellement cette erreur de troncature (obs(dt) - obs(dt/2) ~ disp).

## 3. CE QUI EST FAUX DANS L'ETAT DU 13/09 AU MATIN -- A CORRIGER

  F1  "soustraire le terme laisse un residuel en delta' x plancher, gain
      1.8e+03 a 3.8e+04" : NON FONDE. Les modes libres (C3) placent le
      residuel en delta'^((alpha+3/2)/2) x amplitude inconnue, pas en
      delta'^2 ; a p = 7 le residuel observe (b) va jusqu'a 2.1e-7, soit un
      gain ~10 sur le plancher, pas 1.8e+03.
  F2  "le modele fixe la tolerance, l'instrument est plus fin que lui" : A
      NUANCER. Le PLANCHER du gel fixe la tolerance (c'est la regle), mais
      le terme reel est 3 a 6 fois plus petit que le plancher, et l'ecart
      observe a p = 4 est domine par la troncature RK4, pas par le modele.

  Gains REALISTES, mesures a posteriori, sur le plancher v7 :
      p = 4 : residu |obs_R - pred| <= 5.9e-9, mais ambiguite d'ordre ~3e-8
              -> gain ~40 (ordre non mesure) a ~190 (ordre mesure)
      p = 5 : <= 4.9e-9, ambiguite ~1.6e-8 (q 3..5)     -> ~100 a ~320
      p = 7 : jusqu'a 2.1e-7 (modes libres)             -> ~10

## 4. CE QU'UN GEL v8 DOIT TRANCHER (plume machine 1 ; arbitrages operateur)

  Q1  LA CORRECTION : soustraire b1(p) derive par projection sur la grille
      REELLE du point (decalage compris), ou ajuster lnA avec le terme c1
      tau^2 a coefficient FIXE dans l'ajustement II. Les deux sont derives ;
      la seconde supprime la sensibilite de grille de 1.3 %. Recommandation
      machine 2 : la seconde.
  Q2  L'INTEGRATEUR : Richardson exige un ORDRE MESURE, pas suppose. Il faut
      un troisieme niveau (dt_2b/4) pour mesurer q par point -- le temoin v11
      mesure deja p_obs, mais sur une autre grandeur. Cout : un etage 2b de
      plus par point (~1520 pas), negligeable.
  Q3  LES MODES LIBRES -- LA VRAIE QUESTION. Leur amplitude n'est pas
      derivable. Trois voies, a arbitrer :
        (i)   les AJUSTER (deux parametres par point : amplitude, phase ; la
              frequence 2.8966 / 3.4921 / 4.2131 et Re beta sont DERIVES) --
              le prix est la puissance, a chiffrer AVANT ;
        (ii)  les BORNER par une tolerance de modele mesuree sur la variation
              en c a (p, w2) fixe (le point 7|1.73|1.20 contre 1.05 en est
              l'echelle) -- c'est une tolerance tiree des donnees, regle 10.3
              a ne pas contourner ;
        (iii) les ECRASER en descendant delta' : le volet T n'autorise plus
              qu'un facteur kT = 1.37 de descente, et a p = 7 les modes libres
              ne reculent devant le terme c1 qu'en delta'^0.15 (un facteur 10
              exigerait delta' / 4.6e+06). Voie (iii) MORTE ; consignee pour
              qu'on ne la repropose pas.
  Q4  CE QUE P-A DEVIENT : a p = 4 et 5 le test peut passer d'une tolerance
      de PLANCHER (1e-6) a une tolerance d'INSTRUMENT (~1e-8) -- la constante
      A y deviendrait MESUREE, pas bornee. A p = 7, sauf (i), elle reste
      bornee. Un P-A a deux regimes selon le degre doit etre ECRIT tel quel.
  Q5  LES SERIES DEPOSEES du 91 (serie_fichier, 54 series) permettent de
      tester (i) SANS nouveau run, par prediction pre-declaree : frequence
      et Re beta derives, amplitude libre, residu attendu au niveau de
      Richardson. C'est le prochain geste le moins cher -- s'il est engage.

## 5. CE QUE CE DOSSIER NE DIT PAS

  Il ne mesure pas A. Il ne refute ni ne confirme P-A (toute lecture sur le
  91 est a posteriori). Il ne prend aucun numero (E18) et ne recommande aucun
  delta. Il n'ecrit aucun gel. Les chiffres de 2 et 3 ne valent que sur les
  cellules du plan du run 91 sous v13, sur BOCAL4.

## 6. PIECES (convention B, 16 hex ; detenteur machine 2 sauf mention)

    lecture_predeclaree_second_ordre_machine2_v1.md       99080e4822bf0108   4847
    derivation_second_ordre_machine2_v1.py                f0333c0afcf86583  15299
    derivation_second_ordre_machine2_v1.log               2409f40ed2a61c61  14809
    derivation_second_ordre_machine2_v1.json              b70fca94d72822ad  10781
    exploration_richardson_second_ordre_machine2_v1.py    9562f34b1b5d6d4a   4227
    exploration_richardson_second_ordre_machine2_v1.log   28f599270bcce9ea   2972
    out_run_delta91/alpha_v13/resultats_alpha.json        b2c5f8cc47c6e611 163658  (au registre, 729f9a9)
    banc_qualification_machine1_v13.py                    1ac295648490a86c 196862  (au registre)
    constante_A_pre_enregistrement_v7.md                  a2b8463372e1f906  41061  (au registre)

  Empreintes re-derivees le 2026-09-13 depuis D:\devs\bocal\BOCAL4. Ce
  dossier ne porte pas sa propre empreinte (auto-reference declaree).

-- FIN dossier_conception_second_ordre_machine2_v1 --
