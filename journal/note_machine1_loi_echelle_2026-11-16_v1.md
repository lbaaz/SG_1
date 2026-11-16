# Note hors chaîne : la loi d'échelle de la largeur — superposition, forme de Φ, carte

Plume : machine 1. Date : 16/11/2026. Statut : exploration hors chaîne, classe 3, non certifiée, non
rejouée par machine 2 ; APRÈS COUP pour tout ce qui touche des états déjà joués. Elle ne tranche
rien, ne modifie aucune pièce citée et n'ouvre aucun gel. Ouverture, selon machine 1 : sur sa
proposition d'une « étape 0 » sans run (16/11/2026, matin), l'opérateur a écrit « Allez ouvre on
va explorer ! » (16/11/2026, 10 h 10).

Aucune largeur 2D n'est calculée ici. Celles qui sont citées sont LUES dans des pièces déposées :
les largeurs de plateau Gamma_pl(A) du run du gel ter (delta 99) aux douze points du delta 98, et
celles du run « loi de la largeur, ordre 3 » (delta 100) aux douze cellules tirées. Ce qui est
calculé : des chaînes à une dimension. Les éléments de matrice sont ceux du moteur
(82a0be882568fe0c), appelés tels quels ; les tables d'ordre 2 et 3 sont celles des blocs déposés
(7cd5977bc27bebc1, 534ba246aa3b8973), appelés tels quels. Registre lu sur clone neuf (tête
dee73bd), non écrit. Tous les nombres de cette note sont écrits par un script qui les lit dans les
sorties (section 11) ; aucun n'est tapé.

## 0. Verdict

1. La loi d'échelle tient sur ce qui est joué. Gamma = |delta| × Phi(kappa ; n1, n2), où Phi est
   la limite delta → 0, à kappa = t_0 / |delta| fixé, de la chaîne de l'état : une fonction sans
   paramètre, la même des deux côtés de 2,00. Sur les 185 états jugés, qualifiés et dans le
   domaine (129 du delta 100, 56 du delta 98), Gamma_pl / |delta| parcourt
   6,97 décades et suit Phi avec une pente de 0,9978 (corrélation 0,9977). Ce que la
   loi laisse, r = ln(Gamma_pl / (|delta| Phi)), vaut 0,255 en médiane et 0,892 au pire
   (un facteur 2,44), et il est du signe opposé à delta à 184 états sur 185 : c'est le terme
   en delta, celui que les ordres 2 et 3 calculent. Section 3 et figure.
2. Phi se calcule à toute profondeur. La chaîne de la limite est tridiagonale : sa largeur est une
   fraction continue dont la partie imaginaire se suit en logarithme, sans soustraction. Trois
   arithmétiques (diagonalisation, fraction continue, pôle complexe en précision arbitraire)
   s'accordent ; la diagonalisation, elle, est perdue vers exp(−66,0). Section 2.
3. Sa forme quand la barrière devient profonde, à étiquette fixée :
   ln Phi = −B M0 + c_L ln M0 + d_L + o(1), avec M0 = 2,00275 (|delta| / g)^(2/3) la longueur de
   la barrière en barreaux, B = B(1/3, 1/2) = 4,206546 et c_L = (18 + 19 n1 + 17 n2) / 11. La durée
   de vie d'un état donné croît donc comme une exponentielle étirée du couplage,
   exp(8,4247 (|delta| / g)^(2/3)), à une puissance près : plus vite que toute puissance de
   1 / g. L'exposant 2/3 est 2 / (p − 2). Vérifié sur la chaîne jusqu'à 4096 barreaux, sur quatre
   étiquettes. Section 4.
4. Ce régime n'est pas celui de la campagne. Dans la plage de kappa jouée, l'exposant local des
   états excités va de 1,06 à 2,53, pas 2/3 ; il vaut encore 0,694 à
   kappa = 0,001, où −ln Phi vaut déjà 175 pour le vide (76 décades). Aucun
   lecteur 2D en double précision n'y lira rien. À la profondeur de la campagne, la forme à trois termes est fausse de
   0,50 (en logarithme) pour (6, 2) et de 1,75 pour (10, 3) ; pour le vide (0, 0)
   elle est juste à 0,046 près dès quatre barreaux. Dans la plage jouée, la loi est Phi
   elle-même, pas sa forme asymptotique.
5. À fraction f du seuil classique fixée, −ln Phi tend vers nu0* × F(f), où nu0* est
   l'occupation de seuil classique du moteur et F une intégrale à une dimension : F(0) = 12,914,
   F(0,5) = 6,632, F(0,7) = 2,887, et plus de barrière vers f = 0,85. C'est le pont avec la
   branche classique : l'exposant est le seuil classique compté en quanta, fois une fonction de
   la fraction du seuil. À la profondeur de la campagne (nu0* = 5,24, f = 0,70), ce terme dominant
   rend l'exposant à 4,5 pour cent près, soit 0,65 en logarithme. Chaîne
   seule, et définition à refaire pour f ≥ 0,6. Section 5.
6. La carte. À e_bord fixé, l'écart de la chaîne complète à la loi d'échelle ne grandit pas quand
   la barrière s'allonge. Pour (6, 2) il décroît : à e_bord = 0,7 et delta > 0, de −0,602 à 12
   barreaux à −0,055 à 64. Pour le vide il tend vers une fonction bornée : −0,236 et
   +0,147 à e_bord = 0,7 et 64 barreaux. Les 96 points de 24 barreaux ou plus sont
   stables sous l'absorbeur de la chaîne jusqu'à e_bord = 1,0. Les 50 points instables
   ont tous 17 barreaux au plus. Lecture : ce qui casse la chaîne d'ordre 3 n'est pas
   e_bord seul, c'est une barrière courte. La garde e_bord < 0,7 du gel était lue sur des points
   où les deux varient ensemble. C'est une cohérence interne de la chaîne, pas une validation.
   Section 6.
7. Ce qu'on peut écrire, et ce qu'on ne peut pas. On peut écrire : près de la résonance 2:1, là
   où la réduction à une échelle est contrôlée, la largeur d'un état est |delta| Phi(kappa) à un
   facteur d'ordre un près, et Phi décroît comme une exponentielle étirée du couplage. C'est une
   métastabilité au sens technique, dans une fenêtre. On ne peut pas écrire la limite g → 0 à
   désaccord fixé : quand le couplage baisse, e_bord monte, et au-delà de e_bord voisin de 1 le
   saut au bout de la barrière vaut la moitié d'une fréquence ; rien n'y est établi. Et la 2D n'a
   lu que jusqu'à Gamma / |delta| = 2,95 × 10^-11 : tout ce qui est plus profond est la chaîne seule.
   Section 9.
8. Suite proposée, rien n'est décidé : une prédiction à l'aveugle de la largeur du VIDE. C'est
   l'état où la forme fermée est déjà juste à la profondeur qu'un lecteur 2D atteint, et c'est
   le nombre qu'un lecteur extérieur attend. Sections 7 et 8.

## 1. Objet et notations

Site m de l'échelle de l'état (n1, n2) : (n1 + 2 m, n2 + m). L'énergie libre du moteur est
−n1 + w2 n2 : monter d'un barreau ajoute deux quanta au mode 1 (fréquence 1, celui que le moteur
compte en énergie négative) et un quantum au mode 2 (fréquence w2), et coûte delta = w2 − 2. Saut
entre les sites m et m + 1 : t_m = g tau_m, tau_m = X_{2,1}(n1 + 2 m, n2 + m) / 5 (élément de x^5
du moteur). kappa = t_0 / |delta|.

À kappa fixé, la chaîne du premier ordre divisée par |delta| est
H = s m + kappa (tau_m / tau_0) (saut m ↔ m + 1), s le signe de delta ; les déplacements Sigma2 et
le saut au second voisin pèsent delta devant elle, l'ordre 3 pèse delta^2. La limite delta → 0 est
donc cette chaîne tridiagonale, prise avec les éléments de matrice à w2 = 2 exactement, les sites
bas (m < 0) compris. Phi(kappa ; n1, n2) est la largeur de son état de plus grand recouvrement
avec le site 0, sous l'absorbeur de la chaîne déposée (ef = 0,0625, M_facteur = 4, règle de
barrière du moteur).

Loin sur l'échelle, tau_m → (X_c / 5) m^(5/2), X_c = 0,882063 à w2 = 2 (coefficient dominant du
moteur ; ses deux parts valent 3/11 et 8/11). D'où une variable sans étiquette,
lambda = g X_c / (5 |delta|), le bout de barrière M0 = (2 lambda)^(−2/3) = 2,00275
(|delta| / g)^(2/3), et le lien avec l'occupation de seuil classique du moteur,
nu0* = (3/5) (5 lambda)^(−2/3) : M0 = 3,07003 nu0*. À facteur 1 la campagne joue nu0* = 12^(2/3)
= 5,24.

r désigne partout ln(largeur / (|delta| Phi)) ; r2 et r3 quand la largeur est celle de la chaîne
d'ordre 2 ou 3.

## 2. Phi : trois arithmétiques

- Diagonalisation dense, même construction que le bloc d'ordre 3 déposé (lecture par le flux).
- Fraction continue. La self-énergie de droite du site 0 s'écrit g_m = 1 / (E − s m + i W_m −
  T_m^2 g_{m+1}) = u_m − i v_m, avec v_m = Y / (X^2 + Y^2) et Y = W_m + T_m^2 v_{m+1} : des
  produits et des sommes de termes positifs, suivis en logarithme. Phi = 2 Z (−Im Sigma) à la
  racine réelle de E − Re Sigma(E), Z le poids du site 0.
- Pôle complexe exact de la même fraction continue, en précision arbitraire (mpmath), sans
  l'approximation de résonance étroite.

Sur 19 contrôles (quatre étiquettes, kappa de 0,30 à 0,03, jusqu'à exp(−319,0)) :
fraction continue contre pôle exact, 7,8 × 10^-7 au pire sur ln Phi, et 7,2 × 10^-12
au pire sur les 16 contrôles plus profonds que exp(−13) (l'écart des barrières courtes
est celui de l'approximation de résonance étroite, de l'ordre de Phi). Fraction continue contre
flux, pour les contrôles au-dessus de exp(−46) : 7,8 × 10^-7. Le contrôle le moins profond où
le flux se trompe de plus de 0,01 est à exp(−66,0). Signe de delta : la fraction
continue rend la même Phi pour s = −1 et s = +1, écart 0 ; c'est attendu (les deux
chaînes se déduisent par une conjugaison).

Contrôle contre la note du 15/11 : pour (6, 2) à kappa = 0,30, Phi = 1,9534 × 10^-4 ; la série de cette
note donnait Gamma_1 / |delta| = 1,9581 × 10^-4 à delta = −0,0125 et 1,9488 × 10^-4 à +0,0125. Phi
s'écarte de leur moyenne de 1,4 × 10^-5 en relatif.

Contrôle de la limite contre le bloc déposé. Sur 4 états, la chaîne du bloc d'ordre 3
réduite à ses sauts du premier ordre (tables et barrière du moteur, w2 réel), jouée à
|delta| = 0,001 et 0,0001 des deux signes à kappa fixé, rejoint Phi : l'écart sur le logarithme
vaut au plus 8,0 × 10^-5 à |delta| = 0,0001 et s'annule comme delta, avec un coefficient
par état (de −0,80 à +0,22) constant à 6 × 10^-4 près d'un désaccord à
l'autre. Les deux codes ne partagent que les éléments de matrice du moteur.

## 3. Étape 0.1 : la superposition, sur les états déjà joués

États : les 141 jugés du delta 100 et les 131 jugés et qualifiés du delta 98
(largeurs de plateau du gel ter). Domaine : celui du gel « ordre 3 » (e_bord < 0,7, stabilité de
la chaîne d'ordre 3 au plus 0,05) ; il compte 185 états. Pour chacun, kappa est recalculé
par le moteur (écart au kappa de la feuille du delta 100 : 0) et Phi par la fraction
continue (écart à la diagonalisation : 1,2 × 10^-6 au pire).

Dans le domaine : Gamma_pl / |delta| va de 2,95 × 10^-11 à 2,75 × 10^-4 ; kappa de 0,100 à
0,488 ; |delta| de 0,030 à 0,080 ; barrières de 3 à 11
barreaux. La droite ln(Gamma_pl / |delta|) = a + b ln Phi a pour pente b = 0,9978, corrélation
0,9977, écart-type restant 0,305. |r| vaut 0,255 en médiane, 0,892 au pire ;
rapporté à l'exposant, 1,7 pour cent en médiane et 7,3 pour cent au pire (figure :
figure_superposition_loi_echelle_v1.png). Signe :
r > 0 à 103 sur 104 états à delta < 0, r < 0 à 81 sur 81 à delta > 0. Phi elle-même bouge de
0,0093 en médiane et 0,023 au pire sous l'absorbeur de la chaîne (doublé,
divisé par deux, reculé de quatre sites).

Ce r n'est pas un résidu inexpliqué : la chaîne d'ordre 3 le rend. L'écart entre r et sa valeur
par la chaîne d'ordre 3 vaut 0,019 en médiane et 0,100 au pire ; c'est le |ln q3| du
delta 100, redit. La superposition ne juge donc rien de plus que E1 ; elle dit que le terme
dominant, à lui seul, est une fonction d'une variable par étiquette, sur sept décades.

Hors du domaine (87 états) : |r| vaut 0,776 en médiane, 2,768 au pire.

VARIANTE, essayée APRÈS avoir vu r, et déclarée comme telle. Prendre la variable d'échelle sur
le saut lointain plutôt que sur le saut du site de départ : kappa* = kappa × (X_c(w2) / X_c(2)) ×
(tau_0(2) / tau_0(w2)). Le changement de variable est minuscule (kappa* / kappa − 1 va de
−0,44 à +0,56 pour cent) mais Phi est raide : la pente d ln Gamma / d ln g des états
joués va de 21,5 à 43,9 (note du 15/11). Avec elle, |r*| vaut
0,197 en médiane et 0,758 au pire (un facteur 2,13). Surtout, l'étendue de
r à l'intérieur d'une cellule tombe, à delta > 0, de 0,092 à 0,033 (médianes sur
les cellules) : le résidu n'y dépend presque plus de l'état. À delta < 0 elle passe de
0,194 à 0,145 seulement. Je ne sais pas pourquoi les deux côtés diffèrent.

| pièce | id | facteur | δ | états | r : min ; médiane ; max | r* : min ; médiane ; max |
|---|---|---|---|---|---|---|
| delta 98 | M2 | — | −0,080 | 7 | −0,033 ; +0,186 ; +0,258 | −0,039 ; +0,133 ; +0,175 |
| delta 100 | BN | 1 | −0,076 | 7 | +0,147 ; +0,219 ; +0,279 | +0,058 ; +0,132 ; +0,199 |
| delta 98 | M1 | — | −0,070 | 11 | +0,012 ; +0,187 ; +0,280 | +0,035 ; +0,108 ; +0,204 |
| delta 100 | N1 | 3/4 | −0,065 | 11 | +0,186 ; +0,275 ; +0,344 | +0,129 ; +0,202 ; +0,260 |
| delta 100 | N2 | 5/6 | −0,065 | 11 | +0,149 ; +0,248 ; +0,316 | +0,120 ; +0,189 ; +0,245 |
| delta 100 | N3 | 1 | −0,065 | 11 | +0,033 ; +0,196 ; +0,278 | +0,055 ; +0,121 ; +0,205 |
| delta 100 | N4 | 6/5 | −0,065 | 14 | +0,004 ; +0,174 ; +0,255 | +0,009 ; +0,124 ; +0,189 |
| delta 100 | N5 | 4/3 | −0,065 | 13 | +0,031 ; +0,161 ; +0,252 | −0,024 ; +0,125 ; +0,179 |
| delta 98 | C2 | — | −0,060 | 11 | +0,195 ; +0,272 ; +0,338 | +0,143 ; +0,209 ; +0,257 |
| delta 98 | C1 | — | −0,030 | 8 | +0,191 ; +0,220 ; +0,251 | +0,175 ; +0,185 ; +0,195 |
| delta 98 | C3 | — | +0,030 | 14 | −0,256 ; −0,222 ; −0,185 | −0,205 ; −0,192 ; −0,169 |
| delta 100 | P1 | 3/4 | +0,035 | 9 | −0,459 ; −0,427 ; −0,366 | −0,391 ; −0,373 ; −0,362 |
| delta 100 | P2 | 5/6 | +0,035 | 10 | −0,448 ; −0,408 ; −0,344 | −0,367 ; −0,353 ; −0,329 |
| delta 100 | P3 | 1 | +0,035 | 12 | −0,397 ; −0,362 ; −0,308 | −0,324 ; −0,314 ; −0,292 |
| delta 100 | P4 | 6/5 | +0,035 | 13 | −0,350 ; −0,311 ; −0,258 | −0,290 ; −0,280 ; −0,240 |
| delta 100 | P5 | 4/3 | +0,035 | 13 | −0,333 ; −0,289 ; −0,227 | −0,269 ; −0,257 ; −0,236 |
| delta 98 | C4 | — | +0,060 | 5 | −0,614 ; −0,566 ; −0,528 | −0,520 ; −0,516 ; −0,513 |
| delta 100 | BP | 1 | +0,067 | 5 | −0,892 ; −0,816 ; −0,744 | −0,758 ; −0,746 ; −0,736 |

## 4. Étape 0.3 : la forme de Phi quand la barrière devient profonde

### 4.1 Le terme dominant et le logarithme

WKB discret sur la barrière, avec t_m / |delta| = lambda m^(5/2) (1 + a_L / m) : l'action vaut
M0 × intégrale de 0 à 1 de arccosh(x^(−3/2)) dx, et deux fois cette intégrale vaut
B(1/3, 1/2) = Gamma(1/3) Gamma(1/2) / Gamma(5/6) = 4,206546 (par parties). Les logarithmes se
comptent : −3 pour kappa^2, −1 au point tournant, +3/2 pour la somme discrète (Stirling), +2 a_L
pour le premier écart de tau_m à m^(5/2). Avec les deux parts 3/11 et 8/11 de X_c,
a_L = 91/44 + (19 n1 + 17 n2) / 22, d'où c_L = 2 a_L − 5/2 = (18 + 19 n1 + 17 n2) / 11.
En variables physiques : −ln Phi → 8,4247 (|delta| / g)^(2/3) = 12,9142 nu0*.

Mesuré sur la chaîne, M0 de 4 à 4096 barreaux :

| étiquette | c_L dérivé | pente mesurée au dernier doublement | d_L (lu à 4096 barreaux) | −ln Φ / (B M0) à 16 ; 4096 | erreur de la forme à trois termes à M0 = 16 ; 64 ; 1024 |
|---|---|---|---|---|---|
| (0, 0) | 1,6364 | 1,6364 | +2,671 | 0,893 ; 0,9991 | 0,012 ; 0,004 ; 0,0002 |
| (2, 1) | 6,6364 | 6,6369 | +6,075 | 0,638 ; 0,9964 | 0,090 ; 0,021 ; 0,0010 |
| (6, 2) | 15,0909 | 15,0932 | +3,540 | 0,333 ; 0,9925 | 0,496 ; 0,098 ; 0,0048 |
| (10, 3) | 23,5455 | 23,5509 | −4,098 | 0,117 ; 0,9889 | 1,754 ; 0,233 ; 0,0114 |

La pente mesurée est celle de −ln Phi − B M0 entre 2048 et 4096 barreaux, divisée par ln 2 ; elle
doit tendre vers c_L. d_L n'est pas dérivé : il est lu. Le rapport −ln Phi / (B M0) dit à quel
point le terme dominant seul est loin : 0,33 pour (6, 2) et 0,12 pour (10, 3) à
16 barreaux, la profondeur de la campagne ; 0,9991 pour le vide à 4096.

Pour le vide : ln Phi = −B M0 + (18/11) ln M0 + 2,671, à 0,046 près dès M0 = 4 et à
0,012 près à M0 = 16.

### 4.2 L'exposant local

p = −d ln(−ln Phi) / d ln kappa ; une exponentielle étirée d'exposant 2/3 donne p = 2/3.

| étiquette | κ | m_bord | −ln Φ | exposant local p | pente d ln Φ / d ln κ |
|---|---|---|---|---|---|
| (0, 0) | 0,03 | 3 | 14,0 | 0,865 | 12,1 |
| (0, 0) | 0,01 | 8 | 33,3 | 0,765 | 25,5 |
| (0, 0) | 0,001 | 42 | 175,1 | 0,694 | 121,5 |
| (0, 0) | 0,0001 | 201 | 842,6 | 0,674 | 568,3 |
| (6, 2) | 0,3 | 3 | 8,5 | 2,423 | 20,7 |
| (6, 2) | 0,15 | 11 | 29,1 | 1,377 | 40,1 |
| (6, 2) | 0,1 | 17 | 48,4 | 1,155 | 55,9 |
| (6, 2) | 0,03 | 46 | 158,6 | 0,869 | 137,7 |
| (6, 2) | 0,001 | 503 | 2044,2 | 0,694 | 1417,8 |
| (6, 2) | 0,0001 | 2357 | 9820,4 | 0,674 | 6617,4 |
| (10, 3) | 0,4 | 7 | 12,8 | 2,527 | 32,3 |
| (10, 3) | 0,22 | 17 | 39,6 | 1,475 | 58,4 |
| (10, 3) | 0,1 | 36 | 104,5 | 1,058 | 110,6 |
| (10, 3) | 0,03 | 91 | 319,0 | 0,835 | 266,4 |
| (10, 3) | 0,001 | 962 | 3929,6 | 0,689 | 2709,3 |
| (10, 3) | 0,0001 | 4501 | 18778,3 | 0,673 | 12632,6 |

Dans la plage jouée (kappa de 0,100 à 0,488), p va de 1,06 à
2,53 pour (6, 2) et (10, 3). Il n'est qu'à 0,673 pour (10, 3) à kappa = 0,0001.
C'est le logarithme à grand coefficient qui retarde l'asymptote ; il vient de ce que chaque
quantum de l'étiquette grossit les sauts.

Ma note du 15/11 retirait l'exposant 2/3 comme non testé. Testé : c'est l'exposant asymptotique
de la chaîne, et il n'a rien à dire de la plage jouée.

### 4.3 Jusqu'où la loi descend dans le domaine gardé

En prenant e_bord = m_bord |delta| :

| \|δ\| | étiquette | e = 0,3 : m_bord ; ν0* ; décades | e = 0,7 : m_bord ; ν0* ; décades |
|---|---|---|---|
| 0,100 | (0, 0) | 3 ; 1,61 ; 6,8 | 7 ; 2,90 ; 13,6 |
| 0,100 | (6, 2) | 3 ; 3,64 ; 3,5 | 7 ; 4,63 ; 7,3 |
| 0,100 | (10, 3) | 3 ; 5,20 ; 3,4 | 7 ; 5,87 ; 5,7 |
| 0,065 | (0, 0) | 4 ; 1,93 ; 8,4 | 10 ; 3,88 ; 18,8 |
| 0,065 | (6, 2) | 4 ; 3,84 ; 4,2 | 10 ; 5,53 ; 11,1 |
| 0,065 | (10, 3) | 4 ; 5,27 ; 3,6 | 10 ; 6,68 ; 8,8 |
| 0,035 | (0, 0) | 8 ; 3,23 ; 15,3 | 20 ; 7,13 ; 36,6 |
| 0,035 | (6, 2) | 8 ; 4,93 ; 8,5 | 20 ; 8,69 ; 25,8 |
| 0,035 | (10, 3) | 8 ; 6,13 ; 6,7 | 20 ; 9,73 ; 21,9 |
| 0,020 | (0, 0) | 15 ; 5,50 ; 27,7 | 35 ; 12,01 ; 63,7 |
| 0,020 | (6, 2) | 15 ; 7,10 ; 18,2 | 35 ; 13,53 ; 50,0 |
| 0,020 | (10, 3) | 15 ; 8,17 ; 15,0 | 35 ; 14,52 ; 44,6 |
| 0,010 | (0, 0) | 30 ; 10,39 ; 54,6 | 70 ; 23,41 ; 127,1 |
| 0,010 | (6, 2) | 30 ; 11,92 ; 41,8 | 70 ; 24,90 ; 109,8 |
| 0,010 | (10, 3) | 30 ; 12,92 ; 36,8 | 70 ; 25,86 ; 102,2 |

La 2D a lu jusqu'à 10,5 décades. À |delta| = 0,035, la garde e_bord < 0,7 laisse
la chaîne descendre à 22 à 37 décades selon l'étiquette. Pour les états
bas, e_bord < 0,7 se lit g > 4,84 |delta|^(5/2) (soit 1,1 × 10^-3 à |delta| = 0,035),
et l'exposant y est au plus 2,94 / |delta|.

## 5. À fraction du seuil classique

Graines de la famille du moteur, occupations réelles (n1, n2) = f^2 nu0* (25/8, 1) à w2 = 2. En
variables x = m / nu0*, le double du saut rapporté au désaccord est une fonction h(x ; f) qui ne
dépend plus de nu0*, et le WKB donne −ln Phi → nu0* F(f), F(f) = 2 × intégrale de arccosh(x / h)
entre les deux points tournants.

| f | F(f), intégrale | points tournants x = m / ν0* | chaîne, ν0* = 5,24 (κ) | ν0* = 41,9 (κ) | ν0* = 335 (κ) |
|---|---|---|---|---|---|
| 0,00 | 12,9142 | 0,000 ; 3,070 | 11,540 (0,004) | 12,661 (0,000) | 12,872 (0,000) |
| 0,30 | 10,0107 | 0,001 ; 2,859 | 9,257 (0,020) | 9,911 (0,030) | 9,998 (0,18) |
| 0,50 | 6,6319 | 0,014 ; 2,466 | 6,184 (0,087) | 6,580 (0,31) | 6,632 (2,19) † |
| 0,60 | 4,7813 | 0,038 ; 2,177 | 4,474 (0,17) | 4,767 (0,74) † | 4,773 (5,41) † |
| 0,70 | 2,8874 | 0,097 ; 1,803 | 2,764 (0,31) | 2,951 (1,55) † | 2,893 (11,65) † |
| 0,75 | 1,9345 | 0,154 ; 1,569 | 1,941 (0,41) | 1,870 (2,17) † | 1,937 (16,43) † |
| 0,80 | 0,9816 | 0,256 ; 1,277 | vide (0,54) | 0,883 (2,98) † | vide (22,66) |
| 0,85 | 0,0313 | 0,573 ; 0,757 | vide (0,69) | vide (4,01) | vide (30,66) |
| 1,00 | pas de barrière | — | vide (1,42) | vide (8,90) | vide (68,97) |

Entre parenthèses, kappa. † : kappa > 1/2, l'état de la chaîne n'est plus porté par un site.
« vide » : la règle de barrière ne trouve aucun site. À grand kappa ma règle abandonne dès que
2 kappa tau_m / tau_0 dépasse 4 m au-delà de m = 8 (le « + 1 » de la règle du moteur n'a pas de
limite) : elle manque alors une barrière qui commencerait plus loin. C'est le cas à f = 0,8 et
nu0* = 335, où l'intégrale en voit une.

La chaîne rejoint l'intégrale quand nu0* grandit : 9,998 pour 10,011 à f = 0,3, 6,632 pour
6,632 à f = 0,5. À fraction fixée, kappa croît comme nu0* : pour f ≥ 0,6 il dépasse 1/2 dès
nu0* de 10 à 40, l'état « de plus grand recouvrement avec le site 0 » n'est plus un état porté
par ce site, et les valeurs de la chaîne se dispersent de 3 pour cent au plus
autour de l'intégrale. F(f) reste défini (c'est une action classique) ; c'est l'objet quantique
qu'on lui compare qui est à redéfinir, par son énergie et non par son recouvrement. Non fait.

À la profondeur de la campagne (nu0* = 5,24, f = 0,70, kappa = 0,31) : la chaîne donne
2,764, l'intégrale 2,887. Le terme dominant rend l'exposant à 4,5 pour cent
près, soit 0,65 en logarithme, un facteur 1,9 sur la largeur. La barrière
disparaît vers f = 0,85 (F = 0,031) ; à f = 0,8, F = 0,98.

## 6. Étape 0.2 : la carte des corrections

Deux étiquettes, (0, 0) et (6, 2). Neuf longueurs de barrière (4 à 64 barreaux), six désaccords
au bout (e = m_bord |delta| de 0,075 à 1,0), les deux signes : 216 points, 214
calculés (2 non calculés : à delta = +0,25 la règle du moteur ne trouve plus de fin
à la barrière). Les w2 parcourus ne sont pas des points de la campagne ; aucune largeur 2D n'y
est lue ni prédite. À chaque point : la loi d'échelle, les chaînes d'ordre 2 et 3 des blocs
déposés, et la stabilité de l'ordre 3 sous son absorbeur (doublé, divisé par deux, reculé de
quatre sites), comme au gel.

Largeur des chaînes d'ordre 2 et 3 : le flux du bloc tant que Gamma / |delta| dépasse 10^−15
(70 points) ; en dessous, quotient de Rayleigh complexe en précision arbitraire sur la
même matrice (144 points). Contrôles : ma matrice contre les blocs déposés, écart relatif
0 ; précision arbitraire contre flux, même matrice, 8,6 × 10^-12.

r3 à delta < 0 ; à delta > 0. \* : chaîne d'ordre 3 instable (stabilité au-dessus de 0,05).

État (0, 0) :

| barreaux | −ln Φ | e = 0,15 | e = 0,30 | e = 0,50 | e = 0,70 | e = 1,00 |
|---|---|---|---|---|---|---|
| 4 | 19,4 | −0,192\* ; +0,004 | +0,522\* ; −0,624\* | −0,915\* ; −1,763\* | −2,988\* ; −3,791\* | +0,548\* ; — |
| 6 | 27,3 | −0,050 ; −0,008\* | −0,221\* ; +0,003\* | −0,564\* ; −0,605\* | −0,989\* ; −1,250\* | −0,573\* ; −1,791\* |
| 8 | 35,3 | −0,046 ; +0,002 | −0,133 ; −0,035\* | −0,338\* ; −0,040\* | −0,645\* ; −0,892\* | −1,243\* ; −1,705\* |
| 12 | 51,5 | −0,043 ; +0,015 | −0,113 ; +0,001 | −0,240 ; −0,062\* | −0,398 ; −0,124 | −0,761\* ; −0,165\* |
| 16 | 67,9 | −0,044 ; +0,023 | −0,107 ; +0,026 | −0,218 ; +0,003 | −0,348 ; −0,041 | −0,559\* ; +0,008\* |
| 24 | 100,9 | −0,044 ; +0,030 | −0,100 ; +0,048 | −0,194 ; +0,054 | −0,302 ; +0,049 | −0,470 ; +0,043 |
| 32 | 134,1 | −0,044 ; +0,034 | −0,097 ; +0,058 | −0,182 ; +0,079 | −0,277 ; +0,091 | −0,424 ; +0,111 |
| 48 | 200,8 | −0,044 ; +0,038 | −0,095 ; +0,069 | −0,170 ; +0,102 | −0,251 ; +0,129 | −0,371 ; +0,168 |
| 64 | 267,6 | −0,045 ; +0,040 | −0,093 ; +0,074 | −0,164 ; +0,113 | −0,236 ; +0,147 | −0,339 ; +0,190 |

État (6, 2) :

| barreaux | −ln Φ | e = 0,15 | e = 0,30 | e = 0,50 | e = 0,70 | e = 1,00 |
|---|---|---|---|---|---|---|
| 4 | 9,7 | +0,138 ; −0,255 | +0,161 ; −0,687\* | −0,117\* ; −1,661\* | −0,388\* ; −1,786\* | +1,678\* ; — |
| 6 | 14,2 | +0,111 ; −0,176 | +0,153 ; −0,412 | +0,097 ; −0,846\* | −0,193\* ; −1,560\* | +0,977\* ; −2,532\* |
| 8 | 19,6 | +0,092 ; −0,137 | +0,135 ; −0,314 | +0,115 ; −0,603\* | +0,031\* ; −0,926\* | −0,289\* ; −1,807\* |
| 12 | 32,0 | +0,070 ; −0,099 | +0,108 ; −0,222 | +0,106 ; −0,406 | +0,043 ; −0,602 | −0,180\* ; −0,935\* |
| 16 | 45,3 | +0,054 ; −0,074 | +0,083 ; −0,166 | +0,083 ; −0,304 | +0,033 ; −0,445 | −0,132 ; −0,598\* |
| 24 | 73,9 | +0,036 ; −0,050 | +0,056 ; −0,109 | +0,053 ; −0,197 | +0,014 ; −0,281 | −0,113 ; −0,369 |
| 32 | 103,7 | +0,025 ; −0,036 | +0,038 ; −0,078 | +0,033 ; −0,139 | −0,003 ; −0,195 | −0,113 ; −0,243 |
| 48 | 165,5 | +0,013 ; −0,020 | +0,018 ; −0,044 | +0,007 ; −0,077 | −0,025 ; −0,103 | −0,119 ; −0,112 |
| 64 | 228,8 | +0,006 ; −0,011 | +0,005 ; −0,025 | −0,009 ; −0,043 | −0,040 ; −0,055 | −0,125 ; −0,044 |

Lecture.

- Les 96 points de 24 barreaux ou plus sont stables, jusqu'à e = 1,0. |r3| y vaut au
  plus 0,470 pour le vide et 0,369 pour (6, 2) ; les ordres 2 et 3 y diffèrent
  d'au plus 0,162.
- Pour (6, 2), à e fixé, |r3| décroît avec la longueur. Pour le vide il sature : à e = 0,7,
  −0,251 et +0,129 à 48 barreaux, −0,236 et +0,147 à 64, pour un exposant de
  268. L'erreur de la loi d'échelle sur ln Gamma reste d'ordre un quand l'exposant se
  compte en centaines.
- Les 50 points instables ont tous 17 barreaux au plus ; le plus petit
  |delta| parmi eux est 0,0187. Les 164 points stables vont jusqu'à
  e_bord = 1,09 et |delta| = 0,083.
- Plus grand e pour lequel la chaîne est stable aux deux signes, sans trou. Vide : 4 barreaux : aucun ; 6 barreaux : 0,075 ; 8 barreaux : 0,150 ; 12 barreaux : 0,300 ; 16 barreaux : 0,700 ; 24 barreaux : 1,000 ; 32 barreaux : 1,000 ; 48 barreaux : 1,000 ; 64 barreaux : 1,000.
  (6, 2) : 4 barreaux : 0,150 ; 6 barreaux : 0,300 ; 8 barreaux : 0,300 ; 12 barreaux : 0,700 ; 16 barreaux : 0,700 ; 24 barreaux : 1,000 ; 32 barreaux : 1,000 ; 48 barreaux : 1,000 ; 64 barreaux : 1,000.

Ce que j'en lis, sans le démontrer : l'instabilité de l'ordre 3 est celle de la région APRÈS la
barrière. Les sauts y croissent comme m^(5/2) ; à barrière courte, l'absorbeur de la chaîne
commence, en proportion, plus loin du bout (règle b_M = max(8, m_bord)), là où le saut n'est plus
petit devant une fréquence et où le terme d'ordre 3, en t^3, n'a plus de sens. Le vide, dont les
sauts croissent le plus vite depuis le site de départ, en souffre le plus. Si c'est cela, le
défaut est dans la géométrie de l'absorbeur de la chaîne et dans la forme « à énergie libre » du
hamiltonien effectif après la barrière, pas dans la barrière. C'est une raison précise de
regarder la forme à énergie fixée ; ce n'est pas une preuve.

## 7. Le vide à profondeur lisible

Sonde de l'état (0, 0) à des barrières de 2 à 6 barreaux et |delta| = 0,005, 0,01 et 0,02, les
deux signes.

| barreaux | κ | ν0* | Γ / \|δ\| (loi d'échelle) | forme fermée − chaîne (ln) | plus grand \|r3\| aux six δ | stabilité d'ordre 3 : min ; max |
|---|---|---|---|---|---|---|
| 2 | 0,0363 | 1,30 | 6,73 × 10^-6 | +0,049 | 0,181 | 0,038 ; 0,405 |
| 3 | 0,0262 | 1,61 | 1,65 × 10^-7 | +0,063 | 0,059 | 0,037 ; 0,281 |
| 4 | 0,0200 | 1,93 | 3,63 × 10^-9 | +0,047 | 0,026 | 0,005 ; 0,178 |
| 5 | 0,0159 | 2,26 | 7,39 × 10^-11 | +0,036 | 0,025 | 0,003 ; 0,050 |
| 6 | 0,0130 | 2,58 | 1,42 × 10^-12 | +0,030 | 0,034 | 0,005 ; 0,065 |

De 3 à 5 barreaux, Gamma / |delta| va de 1,6 × 10^-7 à 7,4 × 10^-11 : la plage de Gamma / |delta|
que la 2D a déjà lue. En largeur absolue c'est plus serré : la plus petite largeur de plateau de
ces deux runs vaut 1,3 × 10^-12, et à |delta| = 0,02 le vide serait à 3,3 × 10^-9 (3 barreaux) et
1,5 × 10^-12 (5 barreaux). La forme fermée y est à 0,063 de la chaîne, et les ordres 2 et 3 ne déplacent
la largeur que de 0,059 au plus. Mais la chaîne d'ordre 3 y est instable sous son
absorbeur jusqu'à 0,28 : pour le vide, à ces profondeurs, le meilleur prédicteur
disponible est la loi d'échelle elle-même, avec une tolérance qui porte cette instabilité. Les
couplages vont de 7,6 × 10^-4 à 5,5 × 10^-3, du même ordre que ceux de la campagne.

Je ne sais pas si le lecteur du gel ter lit l'état du vide tel qu'il est déposé : il lit les
états de plus grand recouvrement avec une graine à fraction 0,70. Non regardé ici.

## 8. Ce qu'un gel jugerait (propositions ; rien n'est décidé)

- A. Le vide. À quelques cellules neuves de petit |delta| et de barrière de 3 à 5 barreaux, la
  largeur de plateau de l'état porté par (0, 0) vaut |delta| Phi(kappa ; 0, 0) dans une tolérance
  gelée ; et, second énoncé, la forme fermée à trois termes la rend aussi. C'est la durée de vie
  du vide du fantôme, prédite sans paramètre. Avant tout gel, une étape sans run : le lecteur
  lit-il le vide, à quels |delta| ; et une règle d'absorbeur de chaîne qui tienne à barrière
  courte.
- B. La loi en delta. Plusieurs w2 à g / |delta| égal, donc à kappa presque égal par étiquette :
  Gamma_pl / |delta| doit se superposer, à un terme en delta près que la chaîne prédit. C'est la
  superposition de la section 3 faite à l'aveugle, avec la variable d'échelle choisie d'avance.
  L'instrument du delta 100 devrait y suffire.
- C. La forme à énergie fixée, pour la raison de la section 6 : barrières courtes.
- D. Sans run : F(f) pour f ≥ 0,6, avec un état défini par son énergie ; et le lien de la
  fraction où la barrière disparaît (vers 0,85) avec les seuils classiques de la campagne.

Mon avis : A, précédé de son étape sans run. B est le moins cher et le moins neuf.

## 9. Limites

- L-1. Après coup. La superposition porte sur des états connus. La variante kappa* a été essayée
  après lecture du résidu ; elle ne vaut que comme observation.
- L-2. Une plume. Rien n'est rejoué par machine 2 ; les scripts sont d'aujourd'hui.
- L-3. Phi dépend de l'absorbeur de la chaîne à 0,023 près au pire sur les états
  joués : aux barrières courtes, la fonction limite n'est pas connue mieux.
- L-4. La carte est la chaîne seule. « Stable » veut dire stable sous l'absorbeur de la chaîne,
  et « r3 petit » veut dire que les ordres 2 et 3 restent près du premier : une cohérence
  interne. Deux étiquettes, e ≤ 1,0. Aucune largeur 2D n'existe à ces profondeurs.
- L-5. c_L est un comptage WKB, vérifié numériquement sur quatre étiquettes ; d_L est lu ; le
  reste o(1) n'est pas borné.
- L-6. F(f) : terme dominant seulement, graines de la famille, occupations réelles (une
  continuation), et un objet quantique mal défini pour f ≥ 0,6.
- L-7. Domaine : canal (2, 1) de x^5, voisinage de 2:1. Rien sur les autres résonances, rien sur
  g → 0 à delta fixé au-delà de e_bord voisin de 1, rien sur une autre définition du hamiltonien
  effectif, rien sur la dynamique du système fermé.
- L-8. Quand la barrière est vide (kappa grand), Phi n'est pas définie par cette chaîne.

## 10. Défauts de ma plume

- D-ECH-1. Ma proposition de ce matin disait que dans la fenêtre de résonance « la largeur est
  linéaire en g, donc pas de métastabilité ». Non éprouvé ici : là où kappa est grand, la
  barrière est vide et cette note ne calcule rien (L-8). Cela reste une lecture.
- D-ECH-2. Ma vue d'ensemble du 16/11 au matin, telle que je l'ai consignée, disait que monter
  d'un barreau ajoute « deux quanta de l'oscillateur normal et un du fantôme ». Le moteur dit
  l'inverse : deux quanta du mode d'énergie négative (fréquence 1) et un du mode de fréquence w2.
- D-ECH-3. La même proposition disait que si la loi vivait au-delà de e_bord = 0,7, la forme à
  énergie fixée deviendrait nécessaire. La carte dit autre chose : au-delà de 24 barreaux la
  chaîne actuelle tient jusqu'à e_bord = 1,0, et c'est à barrière courte qu'elle casse.
- D-ECH-4. Deux fautes de script, corrigées avant toute lecture de nombre : la voie de précision
  arbitraire oubliait le terme diagonal nul du site 0 (arrêt immédiat) ; la carte s'arrêtait
  faute de mémoire à delta = +0,25, où la barrière du moteur n'a pas de fin (garde ajoutée, les
  deux points sont déclarés non calculés). Les nombres de la note sont ceux des versions finales.

## 11. Pièces (convention B)

Au registre (dee73bd), lues :

    82a0be882568fe0c  scripts/m17_chaine_v17.py
    7cd5977bc27bebc1  scripts/chaine_ordre2_bloc_machine1_v1.py
    534ba246aa3b8973  scripts/ordre3_bloc_machine1_v1.py
    87e9221cfc5f8f9b  journal/lot_54ccae1713f92bc9__verdict_ordre3.json
    d356b07c31d2c8ee  journal/ordre3_par_etat_v1.json
    902e92444c733384  journal/etape1_etalon_v1.json
    504409e1a12e46b8  journal/structure_en_delta_v1.json
    2cd1f84efa02f2ab  journal/verdict_ter.json

De ce lot :

    8859a0c49b854d6f  phi_echelle_machine1_v1.py
    a7e3083f44faacd1  phi_echelle_machine1_v1.log
    bb1540d38b00717c  phi_echelle_controle_v1.json
    fc38165bd2ec5f59  superposition_machine1_v1.py
    d2090a0119a87112  superposition_machine1_v1.log
    aeb9fc40ecc43899  superposition_v1.json
    6f4ff443eac1feb1  forme_phi_machine1_v1.py
    63dd661109365a7b  forme_phi_machine1_v1.log
    2e2ed5b9b745790c  forme_phi_v1.json
    6abf1d8b59bf41dc  carte_machine1_v1.py
    530292ef45dc6979  carte_machine1_v1.log
    406f13baa939eded  carte_v1.json
    c8573e4a76420021  lecture_carte_machine1_v1.py
    d0e5f131bd0b552c  lecture_carte_machine1_v1.log
    2b4c26e469ce9033  lecture_carte_v1.json
    665eeb6f96eb220a  sonde_vide_machine1_v1.py
    0a0219b34806d90e  sonde_vide_machine1_v1.log
    6dc2d303350b87e6  sonde_vide_v1.json
    9c63e2931b8e59f8  controle_limite_machine1_v1.py
    b4ba090acbdc3ec3  controle_limite_machine1_v1.log
    6be7d355de412969  controle_limite_v1.json
    f9f0dd351410536b  figure_superposition_machine1_v1.py
    f0b2fe1350028b84  figure_superposition_loi_echelle_v1.png
    9ea4bc086f5768a2  canon_fichiers_v1.py
    (ce script)       construction_note_loi_echelle_machine1_v1.py, gabarit_note_loi_echelle_machine1_v1.md

Le PNG est binaire : son empreinte est l'empreinte brute.
