# PRE-ENREGISTREMENT alpha v4 -- L'EXPOSANT DU PROFIL D'EXPLOSION EST-IL 4 u_p ?
# BROUILLON MACHINE 2 -- DEVIENT GEL A LA CERTIFICATION MACHINE 1

Fichier    : alpha_pre_enregistrement_v4.md
             (le v1, c6c845a6cf51f93f 17591 o, est NON CERTIFIE et reste
             NON EDITE -- PB-1. Cette v2 leve les SEPT bloquants et les
             CINQ non bloquants de note_machine1_certification_gel_alpha_v1.md
             c39ede93480ef56a 8146 o, D-alpha-1 a D-alpha-12, plus sa
             remarque 4.)
Date       : 28/08/2026
Redacteur  : machine 2 (BOCAL4)
Certifieur : machine 1
Perimetre  : la verification alpha SEULE.

CE QUE LA v4 CHANGE PAR RAPPORT A LA v3 -- DEUX ENTREES
             (a) D-g-2 de note_machine1_certification_gels_v6_v3.md
             c98e89bad67c835b : la v3 (3dad1c34b54bb9c3, NON CERTIFIEE,
             NON EDITEE -- PB-1) comparait l'ecart G-dt au maximum des
             DEUX AUTRES composantes. Les trois sont de meme nature et
             mesurees sur les memes runs : lue a la lettre, la garde
             mordait des que son ecart etait le plus grand des trois,
             **sans aucune echelle** -- 3e-06 contre 2e-06 aurait rendu
             NON CONCLUANT DE RESOLUTION sur une separation de 8/15. La
             v2 les rendait MUETTES, la v3 les rendait BRUYANTES SUR DU
             BRUIT : c'est le meme defaut retourne. La v4 les compare au
             PLAFOND, seule echelle que ce gel possede, et ECRIT que leur
             role est de NOMMER, pas de decider.
             (b) LE FAIT 5, arbitrage de l'operateur du 28/08 : la v3
             lisait un seuil sur une branche et lancait la trajectoire
             sur l'autre (4.4). Corrige en 4.4. **Aucun nombre ne change**
             -- ni la table 4.2, ni les amplitudes de 4.3.

CE QUE LA v3 CHANGE -- DEUX POINTS, ET ILS SONT NOMMES
             La v2 (35a70834b2a34514, 21113 o) est **CERTIFIEE et
             DEPOSEE** (registre 37ad1b6). Elle N'EST PAS EDITEE (PB-1).
             La v3 corrige DEUX tolerances qui ne pouvaient pas jouer, et
             rien d'autre. Aucune prediction, aucune amplitude, aucune
             cellule, aucun nombre pur ne change.
             DEFAUT 1 (10.3) -- LA TOLERANCE DE P-A MESURE L'INSTRUMENT,
             L'ECART VIENT DU MODELE. La v2 tire la tolerance de P-A de
             la seule DISPERSION de A sur la grille : elle DECROIT quand
             l'instrument s'ameliore. Or ce gel BORNE lui-meme (D-alpha-9)
             le terme neglige a delta/((alpha+2)(alpha+3)), soit 1/2000 a
             p = 4 -- deux a trois ordres AU-DESSUS de cette dispersion.
             **P-A rendait donc PARTIEL par construction des que
             l'instrument etait bon.** La v3 lui donne un PLANCHER, et ce
             plancher est ecrit dans ce gel depuis la v2.
             DEFAUT 2 (8 et 10.1) -- G-dt ET G-k NE POUVAIENT PAS MORDRE.
             La v2 les compare "a la tolerance", et 10.1 definit cette
             tolerance comme le MAXIMUM qui CONTIENT leurs propres ecarts.
             L'ecart ne peut donc jamais la depasser : gardes muettes par
             construction, quatrieme instance de la campagne. La v3
             compare chaque garde a une tolerance QUI NE LA CONTIENT PAS.
             CE QUI NE CHANGE PAS : P-alpha et sa tolerance de 10.1, le
             plafond de 10.2, les deux ajustements, la fenetre, la
             cascade et ses branches, les tables 4.2, 4.3, 5.3, 5.4, les
             nombres purs de la section 6.
             CONSEQUENCE DE FORME : ce gel PERIME l'ancre E19 de
             l'instrument banc_qualification_machine1_v2.py
             (d74928ef093c96d0). Un instrument v3 est du, avec sa
             certification croisee, avant tout run sous la v3.
Numero de manche : AUCUN (78.7). E18 : aucun numero E, N ou D n'est
             ecrit ici. Files au registre a89f6cf (143 pieces .md) :
             libres au-dela de E41, N-67, D-M17-43.

=======================================================================
0. CE QUE LA v2 CHANGE, EN UN COUP D'OEIL
=======================================================================

    D-alpha-1   criterion des w2 : DERIVE (4.2) -- et les colonnes
                changent : 1.73, 2.27, 2.80
    D-alpha-2   circularite fenetre/t* : point fixe declare (7.2)
    D-alpha-3   plafond de tolerance eta : le test doit SEPARER (10)
    D-alpha-4   G-seuil rendue MORDABLE : "exposant convergent" defini (8)
    D-alpha-5   P-A lue a alpha FIXE, sur un second ajustement (7.4)
    D-alpha-6   lien au bit MESURE : temoin de lignee, 27/27 (5.6)
    D-alpha-7   temoin negatif : PORTE BLOQUANTE en tete de 5
    D-alpha-8   agregation : les six, chacun ; G-w2 nommee (8)
    D-alpha-9   "au plus delta fois", facteurs (alpha+2)(alpha+3) (6)
    D-alpha-10  attendus ECRIT : 63 phases 2 + 27 lignee = 90 (4.5)
    D-alpha-11  le chiffre en sigma : RE-DERIVE de l'artefact (1)
    D-alpha-12  sortie : etat de bascule + journal de phase 1 (5.7)
    remarque 4  T_MAX = 400 declare en 5.2

**ET UNE CORRECTION QUI VA DANS L'AUTRE SENS** (section 4.2) : la
certification ecrit "TREIZE colonnes ou les trois degres sont RETENUS".
Mesure : **13 colonnes ou les trois degres sont MESURES, 11 ou ils sont
RETENUS** (G6). Les deux exclues sont 2.38 et 2.67 -- et le critere
propose en exemple ("premiere, mediane, derniere" sur treize) tombe
justement sur **2.38, colonne EXCLUE par G6**. Le critere retenu ci-
dessous se prend sur les ONZE.

=======================================================================
1. LA QUESTION, ET CE QU'ELLE PEUT RENDRE
=======================================================================

Pres d'un blow-up en temps fini, l'amplitude diverge comme une puissance
de la distance a l'instant d'explosion. La question est de savoir si
CETTE puissance est celle que l'equation impose, et si l'AMPLITUDE qui
l'accompagne l'est aussi.

Enjeu : **u_p = 1/(p-2) est la seule variable de la campagne qui ait
survecu a M12.** La classe ponctuelle `ln s*_p = A(w2) u_p + B(w2)` est
REFUTEE, 11/11 points a |E| >= 0.10 contre un seuil de 6 (delta 46
depose, l.37). **L'echelle, RE-DERIVEE de l'artefact pour cette v2**
(out/m12_results.json, `resultats.E`, les 11 points qui portent E et
sigma_E_max) : |E|/sigma_E_max va de **85 511** (w2 = 2.27, |E| = 0.1715)
a **445 891** (w2 = 2.80, |E| = 0.5426). *Le "446 000 sigma" du v1 etait
juste mais NON SOURCE dans une piece : il vivait dans une fiche de
suivi. Il est desormais re-derive, avec sa source et ses deux bornes.*

Ce sont A(w2) et B(w2) qui sont tombes, pas u_p. Si l'exposant du profil
vaut exactement 4 u_p, la variable est dans la dynamique.

=======================================================================
2. LA DERIVATION, ET SON STATUT
=======================================================================

2.1 Pres de t*, tau = t* - t, x = A tau^(-alpha) :

    x''''  = A alpha(alpha+1)(alpha+2)(alpha+3) tau^(-alpha-4)
    x''    = A alpha(alpha+1)                   tau^(-alpha-2)
    x      = A                                  tau^(-alpha)

Le bilan dominant de `x'''' + (1 + w2^2) x'' + w2^2 x = g x^(p-1)` est
`x'''' ~ g x^(p-1)`.

2.2  equilibre : alpha + 4 = alpha (p - 1)  =>  **alpha = 4/(p-2) = 4 u_p**
     amplitude : **alpha(alpha+1)(alpha+2)(alpha+3) = g A^(p-2)**

Ni w2 ni s n'entrent. alpha ne depend que de p.

2.3 Exact (Fraction, regle 15) :

    p   u_p   alpha   K                          A = (K/g)^u_p  (g = 0.05)
    4   1/2   2       120                        48.98979
    5   1/3   4/3     3640/81  = 44.938272        9.65048
    7   1/5   4/5     9576/625 = 15.321600        3.14244

2.4 STATUT : re-derivee par les deux machines en exact (m1 3/3, m2 8/8).
Ce que la manche teste est l'EXISTENCE du regime dans le systeme integre,
pas l'algebre.

2.5 Le moteur depose rend `g (x1 + x2)^(P-1)` pour les deux composantes
(`grad_rapide`, c8ed357b120352c4) : la non-linearite est une puissance
pure de **x = x1 + x2**, la variable de 2.1.

=======================================================================
3. LES DEUX PREDICTIONS
=======================================================================

    P-alpha : l'exposant local converge vers 4/(p-2) exact.
    P-A     : a alpha FIXE (7.4), l'amplitude ajustee verifie g A^(p-2) = K.

**P-A decide.** Un ajustement qui trouve "une" loi de puissance passe
P-alpha des que la trajectoire diverge vite ; il ne passe P-A que si la
constante est la bonne. P-alpha sans P-A s'ecrit **PARTIEL** (9).

=======================================================================
4. LE SYSTEME, LES POINTS, LES BRANCHES, LE COMPTE
=======================================================================

4.1 Systeme : celui du moteur depose. w1 = 1, g = 0.05, RK4.

4.2 **CRITERE DES COLONNES (D-alpha-1), derive et sans liberte :**

    Sur la carte M12 (out/m12_results.json 389b270b9f5b145c ; au registre
    a89f6cf sous runs/), retenir les colonnes ou les TROIS degres sont
    RETENUS au sens de G6 -- il y en a ONZE :
      1.73  1.76  1.84  1.86  2.22  2.27  2.42  2.55  2.72  2.78  2.80
    (13 colonnes portent les trois degres ; 2.38 et 2.67 sont EXCLUES
     par G6.)
    **Prendre la PREMIERE, la MEDIANE (6e sur 11) et la DERNIERE :**

    w2      p = 4              p = 5              p = 7
    1.73    2.005502036107     0.656225641109     0.494776327322
    2.27    2.918324587849     1.408091737101     0.901634558208
    2.80    8.129205119847     2.593139026592     1.604571976496

    Le critere fixe les trois colonnes sans choix ; il couvre en outre
    l'etendue maximale de la carte. Aucune autre colonne n'est jouable
    sans amender ce gel.

4.3 Amplitudes DECLAREES : s = c s*, c dans {1.05, 1.20}.

4.4 **BRANCHES ET SIGNE (v4) : CHAQUE POINT SE JOUE AU SIGNE DE SON
PROPRE SEUIL.**

    p PAIR (p = 4) : x^(p-1) est IMPAIRE, le systeme est symetrique sous
    x -> -x (parite acquise en M11, r_s = 1 par demonstration). La carte
    ne porte qu'un seuil (sM absent) ; la manche joue **sgn = +1** et
    DECLARE que -1 en est l'image.

    p IMPAIR (5, 7) : x^(p-1) est PAIRE et de signe fixe pour g > 0 --
    **la symetrie N'EXISTE PAS**, et les deux branches ont des seuils
    DIFFERENTS. La carte les porte TOUTES DEUX (`sP` au signe +1, `sM`
    au signe -1), avec `asym = sP/sM` et `frag` = le signe du seuil
    retenu, et **le `sF` de la table 4.2 EST LE MINIMUM DES DEUX**.

    La v3 declarait l'autre branche "SANS OBJET" tout en lisant `sF` :
    aux points ou `frag = -1`, elle lisait le seuil d'une branche et
    lancait la trajectoire sur l'AUTRE. Le texte se contredisait avec la
    carte qu'il lit, et cela se voit sans aucun run.

    **REGLE : chaque point se joue a `sgn = frag` de la carte**, et
    `sgn = +1` la ou la carte ne porte pas de second seuil (p = 4). Le
    signe n'est ni choisi ni ajuste : c'est une fonction deterministe de
    la carte DEPOSEE, fixee en M12 bien avant cette piste. `frag` et
    `asym` se CONSIGNENT a chaque point.

    **Rien d'autre ne bouge** : la table 4.2 est intacte au dernier
    chiffre, les amplitudes de 4.3 restent {1.05, 1.20} et 0.95 sous le
    seuil, et aucune colonne n'est ajoutee.

4.5 **LE COMPTE, ECRIT (D-alpha-10) :**

    trajectoires du plan          3 degres x 3 w2 x 2 amplitudes = 18
    G-dt (second pas)                                              18
    G-k  (seconde bascule)                                         18
    G-seuil (sous le seuil, 3 x 3)                                  9
    ------------------------------------------------ phases 2 :   63
    temoin de lignee (5.6), sans phase 2                           27
    ------------------------------------------------ ATTENDUS :   90

    G-comptes : `comptes + sautes == 90`, en forme derivee.

=======================================================================
5. L'INSTRUMENT
=======================================================================

**PORTE BLOQUANTE (D-alpha-7).** Aucun run de ce gel n'est opposable
avant le verdict **PASSE** du temoin negatif classique, joue sous les
memes (delta, r, M, k, dt_2) et sur le meme instrument, son gel et son
delta cites par empreinte. Un run alpha anterieur a ce verdict n'existe
pas au sens de N-62.

5.1 Le moteur depose ne peut pas servir : `integrer()` rend un BOOLEEN,
ecrase l'etat des membres exploses, n'a ni `t_eval` ni sortie de serie.
**Il n'est pas modifie (PB-1).** L'instrument est NEUF et porte sa MAIN
dans son nom (N-65).

5.2 PHASE 1 -- schema DEPOSE, pas DEPOSE **dt_1 = 0.006**, plafond de
temps DEPOSE **T_MAX = 400**, depuis l'etat initial jusqu'a la bascule.

5.3 BASCULE -- evenement sur l'etat mesurable, **DERIVE PAR DEGRE ET PAR
POINT** : bascule quand tau <= k tau_dom, soit

    |x| >= A_p (k tau_dom(w2))^(-alpha_p)

    a k = 2 :        w2 = 1.73     w2 = 2.27     w2 = 2.80
        p = 4        4.8903e+03    7.5357e+03    1.0827e+04
        p = 5        2.0767e+02    2.7705e+02    3.5276e+02
        p = 7        1.9813e+01    2.3555e+01    2.7229e+01

Elle ne s'ecrit JAMAIS en valeur absolue partagee : une bascule a
|x| = 1e4 pour les trois degres tombe avant la fenetre a p = 4, dedans a
p = 5, et 107 fois apres a p = 7.

5.4 PHASE 2 -- pas raffine dt_2 (section 6), jusqu'a CAP_p(w2) :

                     w2 = 1.73     w2 = 2.27     w2 = 2.80
        p = 4        1.9561e+06    3.0143e+06    4.3307e+06
        p = 5        1.1274e+04    1.5041e+04    1.9151e+04
        p = 7        2.1766e+02    2.5876e+02    2.9912e+02
        dt_2         2.5022e-04    2.0157e-04    1.6817e-04

5.5 Si la trajectoire n'atteint pas CAP_p avant T_MAX : **G-fen**, le
point est NON CONCLUANT et il est COMPTE tel quel.

5.6 **TEMOIN DE LIGNEE (D-alpha-6) -- le lien au bit se MESURE.** La
phase 1, jouee SANS bascule jusqu'a |x| >= 1e4 ou T_MAX, doit rendre le
MEME booleen que le moteur depose : **explose** aux 18 points sur-seuil,
**n'explose pas** aux 9 sous-seuil, et le meme indice de pas d'explosion
la ou il est accessible. **27/27, ou le lien n'est PAS etabli et le
delta l'ecrit tel quel.** Le v1 affirmait ce lien ; il ne le mesurait pas.

5.7 **SORTIE (D-alpha-12)** : la serie (t, x1, x2) de la phase 2,
empreinte convention B ; **l'etat complet a la bascule** (t, x1, x2,
x1', x2'), empreinte ; le **journal de phase 1** (indice de pas, tau,
|x| a la bascule). Sans l'etat de bascule, G-k compare deux phases 1 de
longueurs differentes sans pouvoir dire ou elles divergent.

=======================================================================
6. LES QUATRE NOMBRES PURS -- et RIEN d'autre ne se tape (regle 13)
=======================================================================

    delta = 1/100   **tau_dom = sqrt(delta / (1 + w2^2))**
                    1.73 : 5.0044e-02   2.27 : 4.0314e-02   2.80 : 3.3634e-02
    r     = 1/10    **tau_CAP = r tau_dom**, d'ou CAP_p (5.4)
    M     = 20      **dt_2 <= tau_CAP / M** (5.4)
    k     = 2       bascule (5.3) ; la garde joue k = 4
    eta   = 1/4     plafond de tolerance (section 10, D-alpha-3)

**PRECISION (D-alpha-9)** : a tau_dom, le terme neglige vaut **AU PLUS**
delta fois le terme dominant. Le rapport exact est
delta / ((alpha+2)(alpha+3)), soit **delta/20** (p = 4), **delta/(130/9)
= delta/14.44** (p = 5), **delta/(266/25) = delta/10.64** (p = 7). La
fenetre est donc plus sure que delta ne le dit ; aucun nombre ne change.

=======================================================================
7. LES DEUX AJUSTEMENTS
=======================================================================

7.1 Forme : moindres carres sur ln|x| = ln A - alpha ln(t* - t).

7.2 **LA FENETRE ET t* SE RESOLVENT PAR POINT FIXE (D-alpha-2).** La
fenetre depend de t*, que l'ajustement estime : la circularite est reelle
et se traite, elle ne se tait pas.

    t*_0     = t_dernier + tau_CAP   (l'ansatz au franchissement de CAP_p)
    fenetre  = { points : tau_CAP <= t*_n - t <= tau_dom }
    ajuster  -> t*_(n+1) ; recommencer
    ARRET    : l'ENSEMBLE des points de la fenetre ne change plus.
    Iterations maximales DECLAREES : **8**. Nombre effectif CONSIGNE.
    Pas de point fixe en 8 iterations -> **NON CONCLUANT DE FENETRE**.

7.3 **AJUSTEMENT I -- alpha LIBRE** (A, alpha, t*). Il rend P-alpha.

7.4 **AJUSTEMENT II -- alpha FIXE a 4/(p-2) exact** (A, t*). Il rend
**P-A**, et lui seul : dans l'ajustement libre, A absorbe l'erreur de
alpha, et un P-A lu sur ce A ne teste pas la constante (D-alpha-5).
g A^(p-2) est compare a K, K en exact.

7.5 Regle 14 : tout reechantillonnage refait les deux ajustements.

=======================================================================
8. LES GARDES -- chacune peut MORDRE, et on dit sur quoi
=======================================================================

    G-dt    dt_2 et dt_2/2, MEME trajectoire : l'ecart en alpha se
            compare **au PLAFOND de 10.2 (10.1bis)**, jamais a la
            tolerance de 10.1 qui le contient. Sinon **NON CONCLUANT DE
            RESOLUTION**, et le motif NOMME la garde.
    G-k     k = 2 et k = 4, MEME trajectoire : meme regle (10.1bis).
            Elle teste l'ERREUR ACCUMULEE par la phase 1 avant la bascule.
            Sinon **NON CONCLUANT DE RESOLUTION**.
    G-s     c = 1.05 et 1.20 : meme alpha. La derivation dit que alpha n'en
            depend pas -> un alpha qui depend de s **REFUTE**.
    G-w2    (D-alpha-8) les trois w2, a degre fixe : meme alpha. Meme
            statut que G-s -> **REFUTE** si elle mord.
    G-seuil **LE BANC QUI TUE, ET IL PEUT MORDRE (D-alpha-4).** Neuf
            trajectoires a s = 0.95 s*. Sous le seuil, la trajectoire
            n'atteint jamais CAP_p : l'ajustement s'applique donc a la
            DERNIERE fenetre de largeur (tau_dom - tau_CAP) avant T_MAX,
            t* LIBRE. "Exposant convergent" est DEFINI par les trois
            conditions conjointes :
              (i)   dispersion de l'exposant local sous la tolerance ;
              (ii)  t* ajuste FINI dans [T_MAX, T_MAX + tau_dom] ;
              (iii) A dans le facteur de tolerance de P-A.
            Un tel triplet sous le seuil = **INSTRUMENT REFUTE**, et la
            manche s'arrete la. *Sans cette definition, la branche 1
            etait inatteignable et le banc etait muet par construction.*
    G-fen   moins de points que 7.2 n'en derive -> NON CONCLUANT, COMPTE.
    G-lignee 5.6 : 27/27, sinon le lien au moteur depose n'est pas etabli.
    G-comptes `comptes + sautes == 90` (4.5).

**AGREGATION (D-alpha-8)** : six alpha par degre (3 w2 x 2 amplitudes).
"P-alpha au degre p" exige **les six, chacun, a la tolerance** -- aucune
statistique d'agregation, aucune moyenne.

**La question taxonomique se tranche ici** : G-seuil et G-fen distinguent
un blow-up en temps fini d'une divergence asymptotique. Si les
trajectoires sur-seuil ne montrent pas de t* fini, la reponse est
"divergence asymptotique", et elle s'ecrit telle quelle.

=======================================================================
9. LA CASCADE DE VERDICT -- branches nommees, ecrites avant
=======================================================================

    branche 0  G-lignee < 27/27
               -> **LIEN NON ETABLI** : la manche se joue, et le delta
               ecrit que ses trajectoires ne sont pas celles du moteur
               depose. Aucune promotion possible.
    branche 1  G-seuil MORD -> **INSTRUMENT REFUTE**. Rien d'autre n'est lu.
    branche 2  G-dt ou G-k MORD -> **NON CONCLUANT DE RESOLUTION**.
    branche 3  G-fen : moins de trois degres exploitables, ou pas de point
               fixe en 7.2 -> **NON CONCLUANT DE FENETRE**.
    branche 4  G-s ou G-w2 MORD -> **REFUTE** (alpha depend de ce dont la
               derivation dit qu'il ne depend pas).
    branche 5  P-alpha (les six par degre) ET P-A aux TROIS degres
               -> **VERIFIE**.
    branche 6  P-alpha aux trois degres, P-A non -> **PARTIEL** : la
               dominance tient, la constante non. Ecrit tel quel.
    branche 7  P-alpha echoue a un degre au moins -> **REFUTE**.

**NON CONCLUANT N'EST PAS UNE REFUTATION** ; REFUTE n'est pas un echec.

=======================================================================
10. LES TOLERANCES SE DERIVENT, ET ELLES ONT UN PLAFOND
=======================================================================

10.1 Aucun pourcentage n'est tape. La tolerance sur alpha, par degre, est
le MAXIMUM de : (i) l'ecart G-dt ; (ii) l'ecart G-k ; (iii) la dispersion
de l'exposant local sur la fenetre.

10.1bis **G-dt ET G-k SE COMPARENT AU PLAFOND, ET LEUR ROLE EST DE
NOMMER (v4).** Deux formes sont fausses et il faut le dire pour qu'on ne
les repropose pas : les comparer a la tolerance de 10.1, qui CONTIENT
leur propre ecart, les rend muettes par construction ; les comparer au
maximum des deux autres composantes, toutes trois de meme nature et
mesurees sur les memes runs, les rend bruyantes SANS AUCUNE ECHELLE --
la garde mordrait des que son ecart est le plus grand des trois, fut-ce
a 3e-06. **Une garde a besoin d'une echelle, et ce gel n'en possede que
deux : 8/15 et eta.**

    G-dt MORD si l'ecart G-dt > eta x 8/15 (le plafond de 10.2) ;
    G-k MORD de meme.
    **ecart_G_dt / (8/15) et ecart_G_k / (8/15) se CONSIGNENT**, passe
    ou non.

**CE QUE CES DEUX GARDES APPORTENT, ET CE QU'ELLES N'APPORTENT PAS.**
Puisque la tolerance de 10.1 est le MAXIMUM des trois composantes,
`tol > plafond` EQUIVAUT exactement a "au moins une composante depasse le
plafond". Les deux gardes ne DECIDENT donc rien que 10.2 ne decide deja :
elles NOMMENT la composante qui a creve la resolution -- le pas, la
bascule, ou la dispersion locale. **C'est leur role, il est diagnostique
et non decisionnel, et il est ecrit ici pour qu'on ne le redecouvre pas
dans le code.** La tolerance de 10.1 reste inchangee et sert P-alpha,
G-s et G-w2, dont les ecarts, eux, n'entrent PAS dans son maximum : ces
trois gardes-la mordent pour leur propre compte.

10.2 **LE PLAFOND (D-alpha-3).** Une tolerance qui grandit avec la
degradation de l'instrument finit par tout accepter. L'ecart minimal
entre exposants predits est **4/3 - 4/5 = 8/15 = 0.5333...**. Si

    tol > eta x 8/15      (eta = 1/4, soit tol > 2/15 = 0.1333...)

le degre est **NON CONCLUANT DE RESOLUTION** : un test qui ne separe pas
les trois exposants predits n'a pas de puissance. **`tol / (8/15)` se
CONSIGNE a chaque degre**, passe ou non.

10.3 La tolerance de P-A se derive de la **dispersion de A sur la grille
(dt_2, dt_2/2) x (k = 2, 4)** de l'ajustement II -- **jamais** par
propagation depuis alpha, puisque alpha y est fixe (D-alpha-5).

**ET ELLE A UN PLANCHER (v3).** Cette dispersion mesure l'INSTRUMENT ;
l'ecart que P-A doit tolerer vient du MODELE, et il est borne en 6
(D-alpha-9) par le terme neglige. La tolerance ne peut pas etre plus
petite que le biais qu'elle doit absorber, sans quoi P-A echoue d'autant
mieux que l'instrument est meilleur. **La grandeur se nomme, sinon le
plancher se compte deux fois** : la tolerance vit sur **ln A**, et la
comparaison porte sur ln(g A^(p-2) / K), d'ou le facteur (p-2) qui est
DEJA dans la comparaison :

    plancher_lnA(p) = delta / ((alpha_p + 2)(alpha_p + 3))
                    = 1/2000 (p=4), 9/13000 (p=5), 1/1064 (p=7)

    tol_lnA(p) = max( dispersion de lnA sur la grille , plancher_lnA(p) )

    P-A PASSE au degre p ssi, aux SIX points,
        | ln( g A^(p-2) / K ) |  <=  (p - 2) x tol_lnA(p)

    tol_lnA(p) / plancher_lnA(p) se CONSIGNE a chaque degre : il dit si
    c'est l'instrument ou le modele qui fixe la tolerance.

**Aucun nombre pur neuf** : delta et les alpha_p sont ceux de la section
6, et la borne est celle que ce gel ecrit deja en 6. Le plafond de
D-alpha-3 ne s'applique PAS a ce plancher -- il vise les tolerances
tirees de la dispersion de la grandeur TESTEE, et celle-ci est tiree de
la borne du MODELE, qui ne bouge pas avec la mesure.

=======================================================================
11. DEUX REGLES QUE CETTE MANCHE PROPOSE (numeros a l'acte, E18)
=======================================================================

11.1 *Un seuil qui se compare a une grandeur dependant du degre (ou de la
cellule) se declare en NOMBRE PUR et se derive ; il ne s'ecrit jamais en
valeur absolue partagee.* Trois instances mesurees le 25/08 : le seuil du
temoin P7 partage entre cellules (E40) ; le CAP partage entre degres ;
la bascule partagee entre degres. Machine 1 la soutient.

11.2 *Un controle de file se joue sur les pieces qui PORTENT des numeros
-- actes et notes -- jamais sur des binaires ni sur du code.* Motif
mesure : un balayage de tout l'arbre rend "E max = 74" en lisant les
octets d'un PNG et des noms de variables Python.

=======================================================================
12. DISCIPLINE
=======================================================================

E19 (ancre du gel dans l'instrument, certification croisee ANTERIEURE au
depot) ; N-59 (empreinte ET taille de la copie executee, relevees avant
lancement) ; N-61 (chaque mesure cite sa ligne de log) ; N-62 (hors
instrument depose, la mesure n'existe pas) ; N-65 (la main dans le nom) ;
N-66 (la reprise refuse un log de format inconnu) ; PB-1 ; section CE QUI
N'A JAMAIS TOURNE au delta qui conclut.

=======================================================================
13. CE QUE CE GEL NE JOUE PAS
=======================================================================

  - il ne teste pas le modele : il teste si l'estimateur voit le regime
    que l'equation impose ;
  - il ne re-mesure aucun s* : ils sont lus au registre (4.2) ;
  - il ne joue aucune colonne hors des trois derivees en 4.2, aucun degre
    hors de 4/5/7, aucune amplitude hors de {0.95, 1.05, 1.20} x s* ;
  - il ne joue pas la branche sgn = -1 (4.4) ;
  - il ne joue pas le temoin negatif : celui-la vient AVANT (porte de la
    section 5) et a son propre gel ;
  - il ne dit rien de P8, de la chaine quantique, ni d'aucune question de
    M17 consignee ouverte ;
  - il ne mesure pas le temps de calcul comme une grandeur : il le consigne.

=======================================================================
14. LECTURE PRE-DECLAREE (machine 2, AVANT toute execution)
=======================================================================

  - P-alpha PASSE aux trois degres : la dominance ne demande que tau
    petit, et la fenetre est declaree pour ca.
  - **P-A est la ou ca peut casser** : elle exige l'amplitude du regime
    PUR ; toute contamination par les termes lineaires la deplace. Je la
    donne moins probable que P-alpha -- d'ou la branche PARTIEL.
  - G-seuil : je l'attends muette. Si elle mord, la piste s'arrete et
    c'est le resultat le plus utile de la manche.
  - G-lignee : je l'attends a 27/27, mais je ne le sais pas -- le v1
    l'affirmait, et c'est precisement la faute que la certification a
    relevee.
  - le point le plus fragile reste p = 7 : CAP_7 vaut 218 a 299 selon la
    colonne, sous le CAP depose ; la trajectoire y passe tres vite.

=======================================================================
15. PIECES CITEES (convention B ; detenteur declare)
=======================================================================

    note_machine1_certification_gel_alpha_v1.md     c39ede93480ef56a   8146  (m1)
    alpha_pre_enregistrement_v1.md                  c6c845a6cf51f93f  17591  (m2, NON CERTIFIE, non edite)
    POUR_MACHINE2_piste_alpha_4up_et_temoin_v1.md   e3fe6cbdc1dd98f2   7962  (m1)
    note_machine1_lecture_inventaire_alpha_v1.md    f5057c2a0d41a915   5668  (m1)
    note_machine1_lecture_controle_precisions_alpha_v1.md
                                                    ee72edf10260f98e   2598  (m1)
    inventaire_trajectoires_alpha_machine2_v1.py    2c068f343f83b325   9412  (m2)
    controle_precisions_alpha_machine2_v1.py        981a0c1ee78cb000   7318  (m2)
    m9_replication_v1.py (moteur)                   c8ed357b120352c4  36325  (registre)
    out/m12_results.json (s*, E, sigma_E_max)       389b270b9f5b145c 130856  (= runs/ a l'arbre)
    table_points_gardes_v1.txt                      08907c477872e935  14808  (m2)

L'empreinte du present brouillon se prend a la certification.

-- FIN alpha_pre_enregistrement_v4 --
