Journal bundle 5 -- DELTA du 27/07/2026 : section 36 -- LA PIECE DE CONCEPTION
DEMANDEE AU S35.4. TROIS FAITS NEUFS, DONT UN QUI CHANGE LE CRITERE.

S'insere apres journal_delta_35_conception_p4.md (74d8cf2a...). Repond a
reponse_delta35_machine2.md. ALGEBRE PURE : aucune donnee de manche n'entre
dans ce calcul, seulement la regle d'exclusion et la geometrie.

---

## 36.1 CE QUE J'ADOPTE DE LA REPONSE

L'EXACTITUDE, contre mon "tend vers". La preuve de machine 2 est plus forte
que mon enonce : le faisceau des pente_j(u_p) est CONCOURANT en (u_q, 1), donc
    pente_j(u_p) = 1 + B_j (u_p - u_q)
    couverture   = u_q (max_j B_j - min_j B_j)      -- SANS u_p.
La couverture ne depend pas du degre MESURE. Aucun choix de p ne peut
ameliorer ce diagnostic ; seuls le degre de REFERENCE q et la GRILLE le
peuvent. Le cinquieme argument ne tombe donc pas seulement : son levier
n'existait pas. Adopte tel quel.

R2, ADOPTE, ET LA CORRECTION DE LECTURE AVEC. R2(M10 ampute) = 0.211 contre
R2(M10 non ampute) = 0.223 : presque egaux la ou R1 les separe. La fragilite a
deux retraits etait DEJA la. "Le plan s'est mis en position d'en encaisser un
pire" est faux sur R2 : **G6 n'a pas degrade le plan, elle a depense le
premier des deux retraits qu'il ne pouvait pas encaisser.** Formulation de
machine 2, adoptee a la place de la mienne.

LES DEUX POINTS DE FORME, ACCEPTES SANS RESERVE. (a) L'intervalle est declare
ici : w2 dans [1.25, 2.85], ln Delta dans [-0.5754, 1.9633]. (b) La ligne
"3 + 4 + 3" du S35.3 est RETIREE : elle n'etait pas enumerable, donc pas
verifiable, et publier un nombre inverifiable dans une table est exactement ce
que la regle 11 interdit -- appliquee aux grilles au lieu des reperes. Toutes
les grilles de ce delta sont enumerees point par point, dans les DEUX
coordonnees.

## 36.2 FAIT NEUF 1 -- A 16 POINTS, IL N'Y A PAS DE SOLUTION

Famille a un parametre lambda, de "uniforme en ln Delta" (0) a Tchebychev
(1), sur [1.25, 2.85]. Contrainte : pas maximal en w2 <= 0.15, la resolution
de M10. Ensemble de fit calcule APRES application de la regle d'exclusion.

    **A N = 16, AUCUNE grille de la famille ne tient le pas <= 0.15.**

M10 y arrive parce qu'elle est quasi uniforme en w2 -- ce qui est precisement
ce qui la rend fragile en ln Delta. Resolution et robustesse sont donc en
TENSION a cout constant, et c'est le fait central de ce dossier : il n'y a pas
de repas gratuit a 16 points.

FRONTIERE, calculee (fit apres exclusion, pas <= 0.15, meilleur R2) :
    N=16 : aucune         N=18 : R1 0.802  R2 0.580  Sxx 10.14  n_fit 10
    N=20 : R1 0.853  R2 0.684  Sxx 13.18  n_fit 12
    N=22 : R1 0.849  R2 0.680  Sxx 12.84  n_fit 12
    N=24 : R1 0.878  R2 0.741  Sxx 16.21  n_fit 15
    M10  : R1 0.608  R2 0.223  Sxx  7.44  n_fit 10   (pas 0.1500)
**+25 % de cout (20 mesures au lieu de 16) TRIPLE R2 et gagne 77 % de Sxx.**
C'est le meilleur rapport du tableau ; au-dela, le rendement decroit.

## 36.3 FAIT NEUF 2 -- DESSINER EN ln Delta POUSSE DANS LES ZONES INTERDITES

    lambda = 0.0, N = 16 : 8 des 16 points tombent DANS un rayon d'exclusion
    lambda = 0.5, N = 16 : 8 des 16
    lambda = 1.0, N = 16 : 6 des 16
Une grille reguliere en ln Delta concentre ses points la ou w2 varie
lentement -- c'est-a-dire au milieu, ou sont 3:2 et 2:1. La moitie du plan
peut ainsi tomber hors fit sans que le concepteur s'en apercoive.
**REGLE DE CONCEPTION : la grille s'optimise APRES application de la regle
d'exclusion, jamais avant.** C'est la meme discipline que E24 -- ne jamais
supposer ce que la regle mecanique fait, l'appliquer -- transportee de la
verification vers la conception.

## 36.4 FAIT NEUF 3 -- R1 EST LE MAUVAIS OBJECTIF, ET M10 LE PROUVE

R1 recompense l'ENTASSEMENT : quatre points quasi confondus resistent
parfaitement au retrait d'un seul. Or G6 n'a pas tire sur un point au hasard.
**Elle a tire sur w2 = 1.25, le bord gauche**, la ou l'ensemble d'explosion
cesse d'etre une demi-droite. Si la pathologie est REGIONALE -- l'hypothese la
plus economique avec une seule observation -- alors un plan qui entasse au
bord gauche pour resister a un retrait est MAXIMALEMENT fragile a une
exclusion de region.
On mesure donc aussi R_bloc(k) = min sur les blocs CONTIGUS de k points.
NOTA algebrique : R2_bloc = R2 identiquement -- le pire retrait de deux points
est toujours contigu (les deux extremes du meme cote). L'information neuve
commence a k = 3.

    plan                    n_fit   R1      R2      R3_bloc
    M10 (16 mesures)         10    0.608   0.223   0.128
    C1  Tchebychev N=20      12    0.853   0.684   0.494
    C2  lambda 0.55 N=18     10    0.802   0.580   0.330
    C3  lambda 0.30 N=20     11    0.796   0.579   0.344
    C4  uniforme lnD N=20    11    0.643   0.272   0.170

C1 domine sur les trois indices, mais sa marge FOND quand on passe de R1 a
R3_bloc : 0.853 -> 0.494. C'est le prix de son entassement -- elle place
quatre points dans [1.2500, 1.2946], une bande de 0.045 en w2, soit un tiers
du rayon d'exclusion d'ordre 6. Ces quatre points tombent ensemble ou pas du
tout.
**LE CRITERE SE PRONONCE DONC SUR R3_bloc, PAS SUR R1.** Le classement ne
change pas, la marge si -- et c'est la marge qu'on gele.

## 36.5 CANDIDATE C1, ENUMEREE DANS LES DEUX COORDONNEES

N = 20, lambda = 0.875, w2 dans [1.25, 2.85]. n_fit = 12, R1 = 0.853,
R2 = 0.684, R3_bloc = 0.494, Sxx = 13.179, pas maximal 0.1492.
Gains contre M10 : R1 x1.40 | R2 x3.06 | R3_bloc x3.86 | Sxx x1.77 | cout x1.25.

    i    w2        ln Delta    fit ?        i    w2        ln Delta    fit ?
    0    1.2500    -0.5754     FIT         10   1.7923     0.7940     FIT
    1    1.2573    -0.5435     FIT         11   1.9224     0.9916     hors
    2    1.2719    -0.4818     FIT         12   2.0641     1.1818     hors
    3    1.2946    -0.3914     FIT         13   2.2126     1.3599     FIT
    4    1.3267    -0.2744     hors        14   2.3618     1.5213     FIT
    5    1.3693    -0.1334     FIT         15   2.5042     1.6623     hors
    6    1.4242     0.0280     hors        16   2.6317     1.7793     FIT
    7    1.4929     0.2061     hors        17   2.7361     1.8697     FIT
    8    1.5768     0.3962     hors        18   2.8106     1.9314     FIT
    9    1.6766     0.5939     hors        19   2.8500     1.9633     FIT

C1 EST UNE CANDIDATE, PAS UNE PROPOSITION DE GEL. Deux reserves, ecrites :
  (i) huit points sur vingt sont hors fit -- ils sont mesures et consignes
      (P-M10d, P-M10e, P-M10f en vivent), mais le rendement du fit est de
      12/20 contre 10/16 pour M10 ;
  (ii) l'entassement du bord gauche est optimal contre le retrait ponctuel et
      couteux contre le retrait regional. Une variante bridant l'ecart
      minimal entre points consecutifs reste a explorer.

## 36.6 CE QUI RESTE A GELER, AMENDE COMME MACHINE 2 LE DEMANDE

Cinq nombres, pas quatre, et la grille dans les deux coordonnees :
    1. l'INTERVALLE en w2 et en ln Delta ;
    2. le PAS MAXIMAL en w2, et sa justification par ce que P-M10d doit
       resoudre (les rayons d'exclusion) ;
    3. R1 obtenu ;
    4. R2 obtenu ;
    5. R3_bloc obtenu -- le nouveau, et celui sur lequel le critere se
       prononce (36.4) ;
    + la grille ENUMEREE en w2 ET en ln Delta, avec la mention fit/hors fit
      de chaque point APRES application de la regle.
Le --selftest du script refera la partition depuis la regle et comparera a
l'enumeration gelee, comme celui de M10 le fait deja.

=== FIN DU DELTA 36 ===
