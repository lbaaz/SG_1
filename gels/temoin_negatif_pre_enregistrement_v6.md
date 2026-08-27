# PRE-ENREGISTREMENT DU TEMOIN NEGATIF CLASSIQUE -- v6
# LE BANC QUI QUALIFIE LE REGLAGE AVANT QUE alpha SOIT JOUE
# BROUILLON MACHINE 2 -- DEVIENT GEL A LA CERTIFICATION MACHINE 1

Fichier    : temoin_negatif_pre_enregistrement_v6.md
             (v1 7c6d958e829a4ec1, v2 7275931b305ad5f1, v3
             26da379a551f06ea, v4 46f462e361d225fd : NON CERTIFIES,
             conserves NON EDITES -- PB-1. La v5 leve D-t-13 et D-t-14 de
             note_machine1_certification_gel_temoin_v4.md 222883abcd47df9d,
             apres D-t-1..8 (v3) et D-t-9..12 (v4).)
Date       : 28/08/2026
Redacteur  : machine 2 (BOCAL4)
Certifieur : machine 1
Repond a   : LE FAIT 1, seul (voir CE QUE LA v6 CHANGE, ci-dessous) --
             incoherence entre la section 8 et la section 9 de la v5,
             relevee par l'instrument (LD-9), confirmee par les deux
             machines, arbitrage de l'operateur du 28/08/2026 ;
             note_machine1_certification_gel_temoin_v4.md 222883abcd47df9d
             (NON CERTIFIE, D-t-13 et D-t-14) ;
             note_machine1_certification_gel_temoin_v3.md 4a74b1339e07363d
             (NON CERTIFIE, D-t-9 a D-t-12, leves en v4) ;
             note_machine1_certification_gel_temoin_v2.md fb6a64cf433ba19a
             (NON CERTIFIE, D-t-1 a D-t-8, leves en v3) ;
             note_machine1_lecture_temoin_negatif_v1.md 465e891c4334b5bb
             (la solution manufacturee) ;
             note_machine1_lecture_damour_smilga_transcription_v1.md
             47af9a507c25a49a (les deux pieges, T-1 redessine).
Perimetre  : le temoin CLASSIQUE seul.

CE QUE LA v6 CHANGE -- UN SEUL POINT, ET IL EST NOMME
             La v5 (0905a9b78ba40349, 34961 o) est **CERTIFIEE et
             DEPOSEE** (registre 37ad1b6). Elle N'EST PAS EDITEE (PB-1) :
             elle reste le gel sous lequel le pre-vol opposable du
             27/08 a ete joue. La v6 corrige UNE incoherence interne et
             RIEN d'autre.
             LE DEFAUT : la section 8 exige que la tolerance de
             W-integrales se lise **sur dt contre dt/2** (chute d'un
             facteur 16, RK4) ; la section 9 ne compte que **DEUX flots,
             tous deux au pas dt**, et T-3a = 0. A compte gele, le flot a
             dt/2 n'existe pas : **la garde est injouable, et elle est
             restee muette au pre-vol.** Aucune des deux sections n'est
             fausse ; leur conjonction l'est.
             LA CORRECTION : deux flots de plus, un par etat initial, au
             pas dt/2, joues POUR W-integrales SEULE. T-1 passe de 2 a 4
             runs, les ATTENDUS de 39 a 41.
             CE QUI NE CHANGE PAS : les lectures de T-1 (t_c, R, tol_R,
             saturation, fenetres) restent lues sur les flots a dt et sur
             eux seuls -- **quatre flots ne font pas quatre etats** ; la
             cascade, ses branches et leurs verdicts ; tout le reste du
             gel, au caractere.
             CONSEQUENCE DE FORME : ce gel PERIME l'ancre E19 de
             l'instrument banc_qualification_machine1_v2.py
             (d74928ef093c96d0). Un instrument v3 est du, avec sa
             certification croisee, avant tout run sous la v6.
Numero de manche : AUCUN -- BANC DE QUALIFICATION au sens de N-69
             (delta 84 fff42f489696c7ed, certifie, **non depose** : ce
             gel ne se depose pas avant lui).
E18        : aucun numero E, N ou D n'est ecrit ici. Files en MAXIMUM
             CITE : E42, N-69, D-M17-45, tous pris par le 84 non depose.

=======================================================================
0. CE QUE LA v5 CHANGE
=======================================================================

```
    D-t-1  T-1 annoncait qualifier LA RECHERCHE DE SEUIL sans la jouer
           -> forme (b) adoptee : T-1b LA JOUE, et son attente est
              QUANTITATIVE (4.6). C'est le banc qui met a l'epreuve
              l'outil dont depend toute la carte des s*.
    D-t-2  W-lignee ne pouvait PAS se jouer ici (le moteur depose
           n'integre pas (2.11)) -> elle SORT de ce gel (8, 11).
    D-t-3  le compte et la base de l'echelle -> CAP_0 DERIVE (c_0),
           CINQ plafonds, ATTENDUS recompte (3, 4.4, 9).
    D-t-4  la tolerance de R n'avait pas de plafond -> eta_R (8, 10).
    D-t-5  T_MAX derive A L'EXECUTION, en deux temps, T_0 declare (4.5).
    D-t-6  la conversion de la tolerance de P-alpha, ecrite (5.3).
    D-t-7  le depart de la phase grossiere de W-bascule, declare (8).
    D-t-8  T-1 joue DEUX etats initiaux, et le compte le porte (4.3, 9).
```

**CE QUE LA v4 AJOUTE, PAR-DESSUS :**

```
    D-t-9   T-1b disait jouer "la recherche de seuil deposee" sans la
            TRANSCRIRE -> 4.6bis : parametres HERITES et cites A LEURS
            LIGNES, variable balayee DECLAREE, tolerance DERIVEE de la
            passe dense -- et un CONTROLE POSITIF de transcription.
    D-t-10  la cascade avait une issue sans branche (R ni q ni 1)
            -> branche 3bis NON CONCLUANT DE REGIME (10).
    D-t-11  les invariants de l'etat B, ecrits (4.3).
    D-t-12  W-integrales : la tolerance se lit sur dt contre dt/2, comme
            W-pas -- **aucun nombre pur de plus** (8).
```

**CE QUE LA v5 AJOUTE :**

```
    D-t-13  le controle positif etait FAUX SUR LE REGISTRE ("une seule
            valeur") -> 4.6bis (iii) reecrit : la resolution est une
            FONCTION du nombre d'elargissements, pas une constante --
            et c'est un controle PLUS fort.
    D-t-14  le test d'explosion est transcrit VARIABLE PAR VARIABLE (4.4).
```

**ET UNE SECONDE FAUTE DE MA MAIN, VERSEE** (D-t-13) : j'ai ecrit que le
motif `OK|pas=` portait "une seule valeur" sur les cartes deposees. **Il
en porte DEUX.** Mon compte affichait la valeur la plus frequente par
artefact, et j'ai lu ce sommet comme la distribution entiere. Comptes
exacts, re-derives : m10 64 x 6.03e-07 ; m11 26 + 6 ; m12 70 + 4 ;
m14 37 + 1 ; m15 28 + 8. **Un compte qui ne montre que son sommet n'est
pas un compte** -- et c'est la deuxieme fois en deux pieces que je verse
une faute d'instrument contre moi.

**ET UNE FAUTE DE MA MAIN, VERSEE EN v4** : le mirage de la v3 etait
mesure par une BISSECTION geometrique. Le moteur depose n'en fait pas : il fait un
RAFFINEMENT DE GRILLE. **Je mesurais sur un sosie** -- ce que D-t-9
reproche au gel, mon instrument le faisait deja. Refait a l'algorithme
depose (4.6), les deux mesures s'accordent a 3e-06 : la loi est une
propriete du SYSTEME, pas de l'algorithme. **Cela n'excuse rien : le gel
doit citer l'algorithme depose, et desormais il le cite.**

=======================================================================
1. A QUOI SERT CE BANC, ET POURQUOI IL PASSE AVANT
=======================================================================

La verification alpha exige de CHANGER le reglage du moteur : plafond
jusqu'a x245, pas x15 plus fin, et une bascule derivee entre deux
phases. Aucun des trois n'a jamais ete joue par la campagne. Un plafond
releve est exactement ce qui peut FABRIQUER un seuil. Ce banc existe pour
que cette possibilite soit mesuree AVANT que quoi que ce soit d'autre
soit lu. **Il ne teste pas la physique : il teste l'appareil.**

=======================================================================
2. TROIS COMPOSANTES, ET UNE SEULE PORTE
=======================================================================

```
    T-1  LE DISCRIMINANT DE REGIME (section 4)
         Le systeme a ghost BENIN de Damour-Smilga, dans l'instrument, et
         la question : le franchissement du plafond est-il un BLOW-UP ou
         une CROISSANCE LINEAIRE ? Qualifie : la phase 1 et le TEST
         D'EXPLOSION.
    T-1b LA RECHERCHE DE SEUIL DEPOSEE, MISE A L'EPREUVE (4.6)
         Le balayage en s qui a produit TOUS les s* de la campagne, joue
         sur un systeme dont on sait qu'il n'explose pas. Qualifie : la
         recherche de seuil elle-meme. **Sans lui, T-1 annoncerait
         qualifier ce qu'il ne joue pas** (D-t-1).
    T-2  LE BANC D'INTEGRATEUR PAR SOLUTION MANUFACTUREE (section 5)
         Exacte par construction, sans article. Qualifie : le pas
         raffine, la fenetre, la remise d'etat a la bascule.
         + T-2a (lineaire seul) et T-2b (non-linearite seule), qui
         separent les causes.
    T-3  LES DEUX INTEGRALES ET LA FORME FERMEE (section 6) -- BONUS.
         Jamais une porte.

    LA PORTE DE alpha S'OUVRE SI ET SEULEMENT SI T-1, T-1b ET T-2
    PASSENT.
    Un echec de T-3 retire un bonus et se consigne ; il ne ferme rien.
```

=======================================================================
3. LE REGLAGE : CELUI DU GEL alpha, PLUS TROIS NOMBRES PURS
=======================================================================

Herites du gel alpha CERTIFIE (35a70834b2a34514), non rouverts :

    delta = 1/100    r = 1/10    M = 20    k = 2    eta = 1/4

Propres a ce banc, declares ici, et tout le reste s'en derive :

    q     = 2        raison de l'echelle GEOMETRIQUE des plafonds (4.4)
    c_T   = 2        T_MAX >= c_T fois le t_c predit au plus grand CAP
    c_pl  = 10       e(dt/2) doit rester c_pl fois au-dessus du plancher
                     machine, sinon l'ordre mesure ne veut rien dire (5.4)
    c_0   = 10       CAP_0 = c_0 |D(0)| -- la BASE de l'echelle se derive
                     de l'etat initial, elle ne se tape pas (D-t-3) ;
                     c_0 met la premiere lecture hors du transitoire
    k'    = 2 k      depart de la phase grossiere de W-bascule (D-t-7)
    eta_R = eta      plafond de la tolerance de R : HERITE, pas nouveau
                     (D-t-4 ; meme forme que D-alpha-3)

**Aucun autre nombre n'est tape.** Les tolerances se derivent (section 8).

=======================================================================
4. T-1 -- LE DISCRIMINANT DE REGIME
=======================================================================

4.1 LE SYSTEME, TRANSCRIT (Damour-Smilga, arXiv:2110.11175, classe (i),
section 2 ; PDF en main de machine 2, sha256 BRUT 50abf013c268779d) :

```
    H1(x, D; p, P) = p P + D V'(x)                            (2.10)
    x'' + V'(x) = 0        D'' + V''(x) D = 0                 (2.11)
    V(x) = w^2 x^2 / 2 + lambda x^4 / 4 ,  lambda > 0         (2.13)
    integrales : H1  et  N(x,P) = P^2/2 + V(x)                (2.12)
```

4.2 CE QUE LA PREUVE ETABLIT -- **et ce n'est PAS la bornitude.**
Verbatim de l'article, note 2 :

```
    "Note that we are not requiring that the motions indefinitely stay
     within a bounded domain [...] We are simply excluding finite-time
     blow-up."
```

et, sur le secteur ghost : *"an oscillatory behavior with an amplitude
rising linearly in time. A benign ghost again."*

**L'attente gelee est donc : PAS DE BLOW-UP EN TEMPS FINI. Jamais "pas de
seuil".** Un test `|x| > CAP` se declenche toujours sur une croissance
lineaire ; il suffit d'attendre.

4.3 **L'ETAT INITIAL EST DECLARE, ET UN ETAT EST INTERDIT.**

```
    ETAT A :  x(0) = 1 ,  x'(0) = 0 ,  D(0) = 1 ,  D'(0) = 0
              (w = lambda = 1)  ->  H1_0 = 2 ,  N_0 = 3/4
    ETAT B :  x(0) = 2 ,  x'(0) = 0 ,  D(0) = 1 ,  D'(0) = 0
              -> H1_0 = 10 ,  N_0 = 6   (D-t-11, re-derives : N_0 = V(2)
                 = 2 + 4 ; H1_0 = D(0) V'(2) = 2 + 8)
                 (D-t-8 : le discriminant ne doit pas dependre de
                 l'orbite, et deux etats le montrent au lieu de
                 l'argumenter)
    ETAT INTERDIT :  D(0) = 0 , D'(0) = 1 au rebroussement
```

Motif, mesure des deux cotes : sur l'etat interdit, **D est exactement
proportionnel a x'** (rapport -0.500000000, dispersion relative 5e-11) --
c'est la solution TANGENTE a l'orbite, l'unique solution bornee de
l'equation de Hill. |D| y reste sous 0.62 sur T = 400. **Un temoin lance
la ne franchirait aucun plafond et "passerait" par construction** :
troisieme instance de la famille D-alpha-4, cette fois par ETAT INITIAL.
Et sur ce meme etat H1_0 = 0, ce qui rend toute derive RELATIVE absurde
(section 8, W-integrales).

4.4 **LA MESURE : LE PLAFOND EST LA VARIABLE.**

```
    CAP_0 = c_0 |D(0)| -- la BASE se derive de l'etat initial ;
    echelle GEOMETRIQUE CAP_j = q^j CAP_0, j = 0..4 : q^4 = 16 >= 10,
    donc **CINQ plafonds et QUATRE rapports R** (D-t-3) ;
    pour chaque CAP : t_c(CAP) = premier temps ou LE TEST DEPOSE mord.
    **LE TEST EST TRANSCRIT VARIABLE PAR VARIABLE** (D-t-14) : le moteur
    depose teste `~isfinite OU max(|x1|, |x2|) > CAP` (l.362-363), sur les
    deux POSITIONS. Sur (2.11) les positions sont x et D, donc :
        **non fini  OU  max(|x|, |D|) > CAP**
    et non "|D| > CAP". |x| reste borne (mouvement dans un potentiel
    confinant, N conservee), donc le test porte DE FAIT sur D -- mais
    "de fait" n'est pas "par transcription", et c'est la transcription
    qui est gelee ;
    statistique :   R = t_c(q CAP) / t_c(CAP)
      croissance lineaire   ->  R = q
      blow-up en temps fini ->  R -> 1  (t_c sature vers t*)
    T_MAX se DERIVE **A L'EXECUTION, EN DEUX TEMPS** (D-t-5) :
      (1) courir jusqu'a T_0 = 400 (le plafond de temps DEPOSE) et lire
          t_c(CAP_0) ; W-croissance exige que ce franchissement ait eu
          lieu avant T_0, sinon NON CONCLUANT DE TEMOIN ;
      (2) predire t_c(CAP_4) = t_c(CAP_0) x CAP_4/CAP_0, poser
          T_MAX = c_T fois cette prediction, et continuer.
      La prediction est CONSIGNEE avant d'etre verifiee : c'est elle que
      le rapport R met a l'epreuve.
```

**Ce test ne peut pas etre trompe par le plafond, puisque le plafond est
la variable.** La garde "le verdict ne doit pas dependre de s_max" de la
v1 disparait : elle EST la mesure.

4.6 **T-1b -- LA RECHERCHE DE SEUIL DEPOSEE, MISE A L'EPREUVE** (D-t-1)

Le balayage en s qui a produit tous les s* de la campagne est joue sur ce
systeme, dont l'article dit qu'il n'explose PAS en temps fini. Il rendra
un "seuil" : le secteur ghost obeit a une equation LINEAIRE en D, donc
mettre s en facteur sur D(0) met s en facteur sur D(t), et
"|D| franchit CAP avant T_MAX" devient s > CAP/(v T_MAX).

**MESURE AVANT D'ETRE GELE** (instrument joint, 4/4) :

```
    CAP    T_MAX   seuil mesure   CAP/(v T_MAX)
    100    200     0.977250       0.973710
    200    200     1.954478       1.947420
    400    200     3.908915       3.894839
    100    400     0.487224       0.486855
    100    800     0.243255       0.243427
```

**ATTENTE GELEE, QUANTITATIVE :**

```
    s*(q CAP, T_MAX) / s*(CAP, T_MAX)   = q      (mesure : 2.0000, 2.0000)
    s*(CAP, c_T T_MAX) / s*(CAP, T_MAX) = 1/c_T  (mesure : 0.4986, 0.4993)
```

Un seuil qui NE suit PAS ces deux lois -- en particulier un seuil STABLE
sous les deux variations -- est un blow-up vu par l'appareil, et le
verdict est **REGLAGE REFUTE**. Trois recherches suffisent : (CAP, T_MAX),
(q CAP, T_MAX), (CAP, c_T T_MAX).

**Ce que ce banc met a l'epreuve n'est pas un detail : c'est l'outil qui a
produit les 138 points mesures de la campagne.**

4.6bis **L'ALGORITHME EST TRANSCRIT, PAS EVOQUE** (D-t-9)

Le moteur depose ne peut pas courir (2.11) : c'est l'instrument neuf qui
rejoue l'ALGORITHME. Un algorithme evoque est un sosie. Donc :

**(i) LES PARAMETRES SONT HERITES ET CITES A LEURS LIGNES** (moteur
depose c8ed357b120352c4) :

```
    l.278  DT, T_MAX, CAP = 0.006, 400.0, 1.0e4
    l.279  NGRID, NPASSES, NDENSE = 48, 3, 96
    l.280  LO0, HI0, MAX_ELARG = 0.05, 6.0, 8
    l.339  def integrer  -- le test : ~isfinite OU |.| > CAP
    l.372  def chercher_seuil -- grille de NGRID points, elargissement
           x4 jusqu'a MAX_ELARG, NPASSES-1 raffinements sur l'intervalle
           encadrant, puis passe DENSE de NDENSE points
```

**Ce n'est PAS une bissection** : c'est un raffinement de grille, et le
gel le dit parce que la difference se voit dans la resolution finale.

**(ii) LA VARIABLE BALAYEE EST DECLAREE** : `s` multiplie **D(0) et
D'(0) SEULEMENT** ; le secteur x est fixe par l'etat (4.3). C'est ce qui
rend la loi exacte -- l'equation en D est lineaire a x(t) donne, donc
D(t ; s) = s D(t ; 1), et "|D| >= CAP avant T_MAX" equivaut a
s >= CAP / max_{t <= T_MAX} |D_1(t)|.

**(iii) UN CONTROLE POSITIF DE LA TRANSCRIPTION -- ET IL EST DERIVE, PAS
CONSTANT** (D-t-13). L'algorithme rapporte sa resolution finale dans son
motif, `OK|pas=...`. Cette resolution se DERIVE de la structure de la
recherche : grille initiale de NGRID points sur l'encadrement de largeur
W, puis NPASSES-1 = 2 raffinements qui divisent chacun par NGRID - 1 = 47,
puis passe DENSE de NDENSE = 96 points sur la cellule finale :

```
    **pas_k = W_k / (47^3 x 95)**    (47^3 x 95 = 9 863 185)

    W_0 = 6.0 - 0.05 = 5.95            -> pas_0  = 6.0325e-07
    W_1 = 24 - 6 = 18   (un elargissement VERS LE HAUT, x4)
                                       -> pas_1  = 1.8250e-06
    W_-1 = 0.05 - 0.0125 = 0.0375 (un elargissement vers le bas)
                                       -> pas_-1 = 3.8020e-09
```

**LA SIGNATURE N'EST DONC PAS UNE CONSTANTE : c'est une FONCTION du
nombre d'elargissements** -- et c'est un controle PLUS fort qu'une
constante, puisqu'il lie la resolution rendue a l'endroit ou le seuil est
tombe.

**Le registre le confirme, et ma v4 le disait faux.** Comptes exacts sur
les cartes deposees :

```
    m10_results.json   64 x 6.03e-07
    m11_results.json   26 x 6.03e-07  +  6 x 1.82e-06
    m12_results.json   70 x 6.03e-07  +  4 x 1.82e-06
    m14_results.json   37 x 6.03e-07  +  1 x 1.82e-06
    m15_results.json   28 x 6.03e-07  +  8 x 1.82e-06
```

Et les QUATRE points de M12 a 1.82e-06 sont **exactement** ceux dont le
seuil depasse HI0 = 6, donc ceux qui ont demande un elargissement :

```
    p = 4, w2 = 2.67 -> 7.46      p = 4, w2 = 2.72 -> 7.95
    p = 4, w2 = 2.78 -> 8.04      p = 4, w2 = 2.80 -> 8.13
    (les seuls points de la carte M12 avec sF > 6 : quatre, comme les
     quatre occurrences de 1.82e-06)
```

**FORME GELEE** : la passe dense doit rendre `pas = W_k/(47^3 x 95)` avec
**k coherent avec l'encadrement ou le seuil est tombe**. Pour les trois
recherches de T-1b, dont les seuils vont de 0.49 a 1.95, tous dans
[LO0, HI0] = [0.05, 6] : **k = 0 attendu, pas = 6.03e-07**. Toute autre
valeur, ou une valeur juste avec un k incoherent, **fait MORDRE
W-transcription**.

Ma transcription, jouee sur Damour-Smilga -- systeme que la campagne n'a
jamais integre -- rend `pas = 6.03e-07` a k = 0. La resolution finale est
une signature de l'algorithme, pas du systeme.

**(iv) LA TOLERANCE DE W-mirage SE DERIVE** de la resolution de la passe
dense (`pas / s*`) et de l'oscillation de l'enveloppe de |D| -- **jamais
tapee** -- et elle porte le meme plafond que R (section 8) : au-dela de
eta (q - 1) pour la loi 1, de eta (1 - 1/c_T) pour la loi 2, le banc est
**NON CONCLUANT DE RESOLUTION**.

Seuils rendus par l'algorithme TRANSCRIT (instrument v2 joint, 8/8) :

```
    CAP   T_MAX   seuil            motif
    100   200     0.977252977      OK|pas=6.03e-07
    200   200     1.954505406      OK|pas=6.03e-07
    100   400     0.487214546      OK|pas=6.03e-07
    -> loi 1 : 1.999999      loi 2 : 0.498555
```

4.7 **LA MEME STATISTIQUE, SUR L'AUTRE SYSTEME.** Rejouee sur les
trajectoires sur-seuil de alpha (s > s*), elle repond a la question
taxonomique laissee entiere par le gel alpha (13, "il ne verifie pas que
le blow-up existe") : **R -> 1 y est attendu**. Une seule statistique,
deux systemes, deux verdicts opposes -- et si elle rend q sur les
trajectoires de alpha, ce n'est pas un blow-up en temps fini qu'elles
montrent, et le delta l'ecrit tel quel.

=======================================================================
5. T-2 -- LE BANC D'INTEGRATEUR PAR SOLUTION MANUFACTUREE
=======================================================================

5.1 LA SOLUTION, EXACTE PAR CONSTRUCTION. Avec les constantes du gel
alpha (A_p^(p-2) = K_p / g) :

```
    x_m(t) = A_p tau^(-alpha_p) ,  tau = t* - t
    ->  x_m'''' = g x_m^(p-1)  EXACTEMENT   (verifie symbolique, 3/3)
    ->  x_m est solution exacte de l'equation COMPLETE avec le forcage
        f(t) = A_p [ (1+w2^2) alpha(alpha+1) tau^(-alpha-2)
                     + w2^2 tau^(-alpha) ]     (verifie symbolique, 3/3)
        a p = 4 : f = 2 sqrt(30/g) (w2^2 tau^2 + 6 w2^2 + 6) / tau^4
```

**Aucune transcription externe. La substitution est nulle par
construction** ; le seul objet transcrit est f, dont la forme est
verifiee en symbolique par les deux machines.

5.2 **LA RAIDEUR EST LA BONNE, ET C'EST LE POINT.** f est SINGULIER en
t* ; dans la fenetre, le terme en tau^-(alpha+2) domine l'autre d'un
facteur **900 (p=7) a 3750 (p=4)**. Le banc exerce donc le pas raffine
sur un probleme de meme raideur que celui de alpha. **Un banc a forcage
regulier ne qualifierait pas la meme chose.**

5.3 PROTOCOLE, en forme derivee :

```
    (i)   etat initial EXACT de x_m a tau_0 = k tau_dom -- le point de
          bascule -- les quatre composantes (x, x', x'', x''') ;
    (ii)  integration avec le schema de la PHASE 2, dt_2 = tau_CAP / M,
          jusqu'a tau_CAP : exactement la fenetre que alpha mesure ;
    (iii) e(dt) = max |x - x_m| / |x_m| sur la fenetre ; repete a dt_2/2 ;
          ordre observe p_obs = log2( e(dt_2) / e(dt_2/2) ) ;
    (iv)  attente gelee : p_obs = 4 (RK4), a la tolerance derivee (8) ;
          ET e(dt_2) sous la tolerance de P-alpha CONVERTIE, et la
          conversion est ecrite (D-t-6) : sur ln|x| = ln A - alpha ln tau,
          une erreur e sur ln|x| pese e / ln(tau_dom/tau_CAP) sur alpha,
          et ln(tau_dom/tau_CAP) = ln(1/r) = ln 10 ; donc
              **e(dt_2) <= tol_alpha x ln 10**
          -- sinon le pas ne resout pas ce que alpha lit ;
    (v)   joue aux TROIS degres et aux TROIS w2 du gel alpha : neuf bancs.
```

5.4 **LE PLANCHER.** Si e(dt_2/2) descend a moins de c_pl fois le
plancher machine, l'ordre mesure ne veut rien dire : le point est **NON
CONCLUANT DE PLANCHER**, et il est COMPTE tel quel.

5.5 T-2a et T-2b, qui separent les causes :

```
    T-2a  g = 0, f = 0 : x = a cos(t+phi1) + b cos(w2 t+phi2) annule
          l'operateur lineaire (verifie symbolique) -- qualifie la
          transcription des termes LINEAIRES ;
    T-2b  l'equation TRONQUEE x'''' = g x^(p-1), dont x_m est solution
          exacte SANS forcage (verifie, 3 degres) -- qualifie la
          NON-LINEARITE seule.
    Si T-2 mord et que T-2a et T-2b passent, la faute est dans f ou dans
    la remise d'etat a la bascule ; si T-2a mord, elle est dans
    l'operateur lineaire.
```

=======================================================================
6. T-3 -- LE BONUS, ET IL N'OUVRE AUCUNE PORTE
=======================================================================

```
    T-3a  CONSERVATION : H1 et N sont des integrales premieres
          ({N, H1} = 0, verifie symbolique). La derive relative sur T_MAX
          qualifie l'integrateur SANS seuil, SANS solution exacte et SANS
          article. Mesure a titre indicatif : 4.7e-09 (H1) et 2.3e-10 (N)
          au pas 0.005 sur T = 400.
    T-3b  FORME FERMEE du secteur x : x(t) = x0 cn[Omega(t-t0), k],
          (2.16)-(2.17). Verifiee contre le Duffing standard : a
          w = lambda = x0 = 1, Omega = sqrt(2), k^2 = 1/4, et la formule
          de x0 rend 1.000000000000.
```

=======================================================================
7. LA TRANSCRIPTION RESTE SOUS CONTROLE, MEME AVEC L'ARTICLE EN MAIN
=======================================================================

**Une lecture n'est pas une transcription.** Machine 2 tient le PDF ;
cela ne dispense de rien :

```
    (i)   le systeme (2.10)-(2.13) est transcrit DEUX FOIS,
          independamment, et les deux transcriptions doivent rendre le
          meme champ de forces sur un tirage declare ;
    (ii)  le flot transcrit doit redonner (2.11) depuis (2.10) par les
          equations de Hamilton -- verifie en symbolique, des deux cotes ;
    (iii) toute formule citee l'est avec son numero d'equation ;
    (iv)  machine 1 n'a PAS acces a l'article : ce qu'elle a verifie,
          c'est que la transcription est COHERENTE avec elle-meme et avec
          la mecanique standard. **Coherent n'est pas fidele**, et la
          fidelite repose sur la seule machine 2 -- le gel le declare au
          lieu de le masquer.
```

=======================================================================
8. LES GARDES
=======================================================================

```
    W-transcription  section 7. Si elle mord : BANC NON JOUE.
    W-croissance     (piege 4.3) |D| doit avoir franchi le PLUS PETIT
                     plafond de l'echelle. Sinon le temoin ne mesure
                     rien : NON CONCLUANT, jamais "PASSE".
    W-integrales     derive relative de H1 et N sur T_MAX, **avec la
                     clause de reference** : l'etat initial doit donner
                     H1_0 et N_0 NON NULS (4.3) -- sur l'etat interdit,
                     H1_0 = 0 et la derive relative rend 1e289.
                     **TOLERANCE (D-t-12) : elle se LIT sur dt contre
                     dt/2, comme W-pas** -- la derive doit chuter d'un
                     facteur 16 (RK4), et c'est cette chute qui est
                     controlee, pas une borne absolue. **Aucun nombre pur
                     de plus** : la variante c_int x N_pas x dt^4 en
                     aurait demande un, et elle est ecartee pour ca.
                     **LES FLOTS QUE CETTE LECTURE EXIGE SONT COMPTES
                     (v6)** : pour chaque etat initial, le flot a dt ET
                     le flot a dt/2 -- quatre au total en section 9. La
                     garde MORD si le rapport derive(dt)/derive(dt/2)
                     n'est pas 16 a la tolerance derivee de la meme
                     facon que celle de W-pas (LD-4), plafonnee de meme.
                     Les flots a dt/2 ne servent QU'A ELLE : aucune
                     lecture de T-1 ne se prend dessus.
    W-pas            5.3 (iii)-(iv) : p_obs = 4 a la tolerance derivee.
    W-plancher       5.4.
    W-bascule        T-2 joue avec et sans bascule, la phase grossiere
                     partant de tau_start = k' tau_dom, k' = 2k DECLARE
                     (D-t-7) : meme approche de la solution exacte des
                     deux cotes.
    W-mirage         (T-1b) les deux rapports de 4.6 a la tolerance
                     DERIVEE de la passe dense et de l'oscillation de
                     l'enveloppe (4.6bis (iv)), plafonnee comme R.
                     Un seuil STABLE sous les deux variations
                     -> REGLAGE REFUTE ; un seuil qui ne suit NI l'une NI
                     l'autre loi -> NON CONCLUANT DE REGIME (10).
    W-transcription  porte le CONTROLE POSITIF de 4.6bis (iii) :
                     la passe dense doit rendre **pas = W_k/(47^3 x 95)**
                     avec k coherent avec l'encadrement ou le seuil est
                     tombe (k = 0 attendu pour T-1b -> 6.03e-07). Une
                     valeur fausse, OU une valeur juste avec un k
                     incoherent, fait MORDRE.
    W-comptes        `comptes + sautes == attendus` (section 9).

    **W-lignee EST SORTIE DE CE GEL (D-t-2).** Elle comparait la phase 1
    au booleen du moteur depose "sur les points de T-1" -- or le moteur
    depose (c8ed357b) n'integre que le systeme PU : il n'a AUCUN booleen
    a rendre sur (2.11), et PB-1 interdit de le modifier. La garde
    existe, elle est G-lignee du gel alpha (5.6, 27/27, sur les points
    PU), elle se joue UNE fois, et elle n'appartient pas ici.
```

**TOUTES LES TOLERANCES SE DERIVENT** : de la dispersion de t_c/CAP
mesuree sur l'echelle (T-1), de l'ordre du schema et du nombre de pas
(W-integrales, W-pas), du plancher machine (W-plancher). **Aucun
pourcentage n'est tape.**

**ET LA TOLERANCE DE R A UN PLAFOND (D-t-4).** Une tolerance derivee de
la dispersion de la grandeur TESTEE peut tout accepter : un t_c qui
SATURE disperse lui aussi, et une tolerance issue de sa dispersion
rendrait R = 1 et R = q "compatibles". L'ecart a separer est q - 1 :

```
    si  tol_R > eta_R (q - 1)   ->  NON CONCLUANT DE RESOLUTION
    (eta_R = eta = 1/4 herite ; a q = 2 : tol_R > 1/4 disqualifie)
    tol_R / (q - 1) se CONSIGNE, passe ou non.
```

C'est exactement la forme de D-alpha-3, deuxieme instance : **une
tolerance sans plafond ne mesure rien.**

=======================================================================
9. LE COMPTE, ECRIT AVANT
=======================================================================

```
    RUNS
      T-1   2 etats initiaux (A, B), DEUX flots chacun
            (au pas dt, et au pas dt/2 pour W-integrales)     =   4
      T-1b  3 recherches de seuil :
            (CAP, T), (q CAP, T), (CAP, c_T T)               =   3
      T-2   3 degres x 3 w2 x 2 pas                          =  18
      T-2a  1                                                =   1
      T-2b  3 degres                                         =   3
      T-3a  inclus dans les flots de T-1 (les quatre)        =   0
      T-3b  3 jeux de parametres declares                    =   3
      W-bascule  T-2 rejoue sans bascule, 9 points           =   9
      ---------------------------------------------------------
      **ATTENDUS = 41 runs**

    LECTURES (sur les flots ci-dessus, sans run de plus)
      t_c : 5 plafonds x 2 etats initiaux                    =  10
      R   : 4 rapports x 2 etats initiaux                    =   8
      W-mirage : 2 rapports                                  =   2
      W-integrales : 2 rapports de derives (un par etat),
            chacun sur son couple (dt, dt/2)                 =   2
```

`comptes + sautes == 41` en forme derivee ; les lectures se comptent a
part et ne s'ajoutent pas aux runs. **Les lectures de T-1 (t_c, R) se
prennent sur les DEUX flots a dt, et sur eux seuls** : les flots a dt/2
n'appartiennent qu'a W-integrales.

=======================================================================
10. LA CASCADE DE VERDICT -- ecrite avant
=======================================================================

```
    branche 1  W-transcription MORD          -> BANC NON JOUE
    branche 2  W-croissance MORD             -> NON CONCLUANT DE TEMOIN
                                                (le temoin n'a rien mesure)
    branche 3  T-1 rend R -> 1 (saturation), OU W-mirage mord (un seuil
               stable sous les deux variations de 4.6)
                                             -> REGLAGE REFUTE :
                                                l'appareil voit un blow-up
                                                la ou il n'y en a pas
    branche 4  W-pas, W-plancher ou W-bascule MORD
                                             -> NON CONCLUANT
                                                D'INTEGRATEUR
    branche 3bis  R n'est NI dans la fenetre de q NI dans celle de 1
               (par exemple 1.5 a q = 2), ou les rapports de W-mirage ne
               suivent ni l'une ni l'autre loi
                                             -> **NON CONCLUANT DE
                                                REGIME** : ni blow-up ni
                                                croissance lineaire A LA
                                                RESOLUTION DU BANC. Porte
                                                FERMEE, verdict consigne.
                                                (D-t-10 : sans elle, une
                                                issue reelle n'avait pas
                                                de branche, et le verdict
                                                se serait decide apres
                                                coup.)
    branche 4bis  tol_R > eta_R (q-1)        -> NON CONCLUANT DE
                                                RESOLUTION (8)
    branche 5  T-1 rend R = q ET T-1b rend les deux rapports de 4.6 ET
               T-2 rend p_obs = 4 avec e(dt_2) <= tol_alpha ln 10
                                             -> **REGLAGE QUALIFIE**
                                                la porte de alpha s'ouvre,
                                                et elle ne s'ouvre que la
    branche 6  T-3 mord seul                 -> QUALIFIE, bonus retire,
                                                consigne
```

=======================================================================
11. CE QUE CE GEL NE JOUE PAS
=======================================================================

  - il ne teste aucune prediction de la campagne : ni alpha, ni P-A, ni
    u_p ;
  - il ne joue pas le temoin QUANTIQUE (apres l'acte de conception) ;
  - **il ne prouve pas que le reglage est bon** : il cherche a le
    refuter, et l'absence de refutation est ce qu'il rend ;
  - il ne juge pas l'article : il transcrit sous controle, et declare que
    la FIDELITE de la transcription ne repose que sur machine 2 ;
  - il n'ecrit aucun instrument : le code vient apres la certification
    croisee (E19) et citera l'empreinte de ce gel ;
  - **il ne joue pas les deux autres candidats** (DMV arXiv:2108.06294,
    Pavsic arXiv:1302.5257) : ils restent SUPPLEANTS, non transcrits ;
  - **il ne joue pas W-lignee** (D-t-2) : elle appartient au gel alpha,
    ou le moteur depose a un booleen a rendre. Ici il n'en a aucun ;
  - **il ne rejoue pas le moteur depose** : il en TRANSCRIT l'algorithme
    (4.6bis), avec un controle positif de transcription -- et si ce
    controle mord, c'est la transcription qui est refusee, pas le
    moteur ;
  - **il ne qualifie pas la recherche de seuil AU-DELA de ce systeme** :
    T-1b montre que l'outil rend un mirage la ou il DOIT en rendre un ;
    il ne dit rien de ce que l'outil rend sur un systeme qui explose
    vraiment -- c'est la question taxonomique, et elle est en 4.7.

=======================================================================
12. LECTURE PRE-DECLAREE (machine 2, AVANT toute execution)
=======================================================================

  - **T-1 : j'attends R = q**, la croissance lineaire. Elle est deja
    mesuree hors gel des deux cotes (t_c/CAP stable de 2.010 a 1.947 sur
    deux decades) -- ce banc la rejoue DANS l'instrument, ou elle peut
    tres bien ne pas survivre au reglage.
  - **W-pas reste la garde la plus susceptible de mordre** : un RK4 a pas
    fixe pres d'une singularite ne converge pas toujours a l'ordre 4. Si
    p_obs est franchement sous 4, ce n'est pas la transcription, c'est le
    schema qui atteint sa limite -- et le reglage de alpha devra changer
    AVANT que alpha joue.
  - **W-croissance : je l'attends muette, et je m'en mefie** : c'est la
    garde nee d'un piege que nous avons failli ne pas voir.
  - T-3a devrait passer largement : les derives mesurees hors gel sont a
    1e-9 et 1e-10, loin de toute tolerance derivable.
  - **T-1b : j'attends les deux rapports, et je les ai deja mesures hors
    gel, DEUX FOIS** -- par une bissection (1.9999 / 0.4986) puis par
    l'algorithme DEPOSE transcrit (1.999999 / 0.498555). Ce banc ne peut
    pas me surprendre sur le SYSTEME ; il peut me surprendre sur
    L'INSTRUMENT, qui n'est pas celui des mesures hors gel. C'est tout ce
    qu'on lui demande.
  - **W-transcription : j'attends pas = 6.03e-07, a k = 0.** C'est le
    controle que je crois le plus discriminant du banc, et le moins
    couteux : une resolution finale est une signature d'algorithme, et
    elle ne depend pas du systeme integre. **Elle depend en revanche du
    nombre d'elargissements**, ce que ma v4 avait manque -- et cette
    dependance la rend plus discriminante, pas moins.

=======================================================================
13. PIECES CITEES (convention B ; detenteur declare)
=======================================================================

    alpha_pre_enregistrement_v2.md               35a70834b2a34514  21113  (m2, CERTIFIE)
    temoin_negatif_pre_enregistrement_v1.md      7c6d958e829a4ec1  13280  (m2, NON CERTIFIE, non edite)
    note_machine1_lecture_temoin_negatif_v1.md   465e891c4334b5bb   5441  (m1)
    note_machine1_lecture_damour_smilga_transcription_v1.md
                                                 47af9a507c25a49a   5292  (m1)
    controle_solution_manufacturee_machine2_v1.py 0319fdbca1676af8  4209  (m2, 14/14)
    controle_damour_smilga_machine2_v1.py        fb5d40bee64e70df   6859  (m2, 18/18)
    controle_mirage_seuil_machine2_v1.py         38a9df063a872987    3497  (m2, 4/4, SOSIE)
    controle_mirage_seuil_machine2_v2.py         0b9ef50aa82af7b3     5748  (m2, 8/8, ALGORITHME DEPOSE)
    note_machine1_certification_gel_temoin_v4.md 222883abcd47df9d    4358  (m1, NON CERTIFIE)
    note_machine1_certification_gel_temoin_v3.md 4a74b1339e07363d    4703  (m1, NON CERTIFIE)
    temoin_negatif_pre_enregistrement_v4.md      46f462e361d225fd   31212  (m2, NON CERTIFIE, non edite)
    temoin_negatif_pre_enregistrement_v3.md      26da379a551f06ea   25237  (m2, NON CERTIFIE, non edite)
    note_machine1_certification_gel_temoin_v2.md fb6a64cf433ba19a   6029  (m1, NON CERTIFIE)
    temoin_negatif_pre_enregistrement_v2.md      7275931b305ad5f1  18940  (m2, NON CERTIFIE, non edite)
    journal_delta_84_arbitrage_78_7_v1.md        fff42f489696c7ed   6838  (m1, CERTIFIE, non depose)
    m9_replication_v1.py (moteur depose)         c8ed357b120352c4  36325  (registre a89f6cf)
    arXiv:2110.11175 (piece EXTERNE, main machine 2)
                                    sha256 BRUT  50abf013c268779d 1973693

L'empreinte du present brouillon se prend a la certification.

-- FIN temoin_negatif_pre_enregistrement_v6 --
