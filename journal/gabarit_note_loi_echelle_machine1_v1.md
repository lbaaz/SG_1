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
   paramètre, la même des deux côtés de 2,00. Sur les @@n_dom@@ états jugés, qualifiés et dans le
   domaine (@@n_dom_100@@ du delta 100, @@n_dom_98@@ du delta 98), Gamma_pl / |delta| parcourt
   @@decades@@ décades et suit Phi avec une pente de @@pente@@ (corrélation @@corr@@). Ce que la
   loi laisse, r = ln(Gamma_pl / (|delta| Phi)), vaut @@r_med@@ en médiane et @@r_max@@ au pire
   (un facteur @@r_max_facteur@@), et il est du signe opposé à delta à @@sg_tot@@ : c'est le terme
   en delta, celui que les ordres 2 et 3 calculent. Section 3 et figure.
2. Phi se calcule à toute profondeur. La chaîne de la limite est tridiagonale : sa largeur est une
   fraction continue dont la partie imaginaire se suit en logarithme, sans soustraction. Trois
   arithmétiques (diagonalisation, fraction continue, pôle complexe en précision arbitraire)
   s'accordent ; la diagonalisation, elle, est perdue vers exp(−@@flux_casse_des@@). Section 2.
3. Sa forme quand la barrière devient profonde, à étiquette fixée :
   ln Phi = −B M0 + c_L ln M0 + d_L + o(1), avec M0 = @@M0_dg@@ (|delta| / g)^(2/3) la longueur de
   la barrière en barreaux, B = B(1/3, 1/2) = @@I2@@ et c_L = (18 + 19 n1 + 17 n2) / 11. La durée
   de vie d'un état donné croît donc comme une exponentielle étirée du couplage,
   exp(@@cst_dg@@ (|delta| / g)^(2/3)), à une puissance près : plus vite que toute puissance de
   1 / g. L'exposant 2/3 est 2 / (p − 2). Vérifié sur la chaîne jusqu'à 4096 barreaux, sur quatre
   étiquettes. Section 4.
4. Ce régime n'est pas celui de la campagne. Dans la plage de kappa jouée, l'exposant local des
   états excités va de @@p_joue_min@@ à @@p_joue_max@@, pas 2/3 ; il vaut encore @@p_1e3_00@@ à
   kappa = 0,001, où −ln Phi vaut déjà @@L_1e3_00@@ pour le vide (@@dec_1e3_00@@ décades). Aucun
   lecteur 2D en double précision n'y lira rien. À la profondeur de la campagne, la forme à trois termes est fausse de
   @@err62_16@@ (en logarithme) pour (6, 2) et de @@err103_16@@ pour (10, 3) ; pour le vide (0, 0)
   elle est juste à @@err00_4@@ près dès quatre barreaux. Dans la plage jouée, la loi est Phi
   elle-même, pas sa forme asymptotique.
5. À fraction f du seuil classique fixée, −ln Phi tend vers nu0* × F(f), où nu0* est
   l'occupation de seuil classique du moteur et F une intégrale à une dimension : F(0) = @@F0@@,
   F(0,5) = @@F05@@, F(0,7) = @@F07@@, et plus de barrière vers f = 0,85. C'est le pont avec la
   branche classique : l'exposant est le seuil classique compté en quanta, fois une fonction de
   la fraction du seuil. À la profondeur de la campagne (nu0* = 5,24, f = 0,70), ce terme dominant
   rend l'exposant à @@ecart07_pc@@ pour cent près, soit @@ecart07_ln@@ en logarithme. Chaîne
   seule, et définition à refaire pour f ≥ 0,6. Section 5.
6. La carte. À e_bord fixé, l'écart de la chaîne complète à la loi d'échelle ne grandit pas quand
   la barrière s'allonge. Pour (6, 2) il décroît : à e_bord = 0,7 et delta > 0, de @@c62_12@@ à 12
   barreaux à @@c62_64@@ à 64. Pour le vide il tend vers une fonction bornée : @@c00_64m@@ et
   @@c00_64p@@ à e_bord = 0,7 et 64 barreaux. Les @@n_long@@ points de 24 barreaux ou plus sont
   stables sous l'absorbeur de la chaîne jusqu'à e_bord = 1,0. Les @@n_inst@@ points instables
   ont tous @@inst_mb_max@@ barreaux au plus. Lecture : ce qui casse la chaîne d'ordre 3 n'est pas
   e_bord seul, c'est une barrière courte. La garde e_bord < 0,7 du gel était lue sur des points
   où les deux varient ensemble. C'est une cohérence interne de la chaîne, pas une validation.
   Section 6.
7. Ce qu'on peut écrire, et ce qu'on ne peut pas. On peut écrire : près de la résonance 2:1, là
   où la réduction à une échelle est contrôlée, la largeur d'un état est |delta| Phi(kappa) à un
   facteur d'ordre un près, et Phi décroît comme une exponentielle étirée du couplage. C'est une
   métastabilité au sens technique, dans une fenêtre. On ne peut pas écrire la limite g → 0 à
   désaccord fixé : quand le couplage baisse, e_bord monte, et au-delà de e_bord voisin de 1 le
   saut au bout de la barrière vaut la moitié d'une fréquence ; rien n'y est établi. Et la 2D n'a
   lu que jusqu'à Gamma / |delta| = @@g_min@@ : tout ce qui est plus profond est la chaîne seule.
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

Loin sur l'échelle, tau_m → (X_c / 5) m^(5/2), X_c = @@Xc@@ à w2 = 2 (coefficient dominant du
moteur ; ses deux parts valent 3/11 et 8/11). D'où une variable sans étiquette,
lambda = g X_c / (5 |delta|), le bout de barrière M0 = (2 lambda)^(−2/3) = @@M0_dg@@
(|delta| / g)^(2/3), et le lien avec l'occupation de seuil classique du moteur,
nu0* = (3/5) (5 lambda)^(−2/3) : M0 = @@M0_nu@@ nu0*. À facteur 1 la campagne joue nu0* = 12^(2/3)
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

Sur @@n_ctl@@ contrôles (quatre étiquettes, kappa de 0,30 à 0,03, jusqu'à exp(−@@ctl_plus_profond@@)) :
fraction continue contre pôle exact, @@ctl_fc_mp_tous@@ au pire sur ln Phi, et @@ctl_fc_mp_prof@@
au pire sur les @@n_ctl_prof@@ contrôles plus profonds que exp(−13) (l'écart des barrières courtes
est celui de l'approximation de résonance étroite, de l'ordre de Phi). Fraction continue contre
flux, pour les contrôles au-dessus de exp(−46) : @@ctl_fc_flux@@. Le contrôle le moins profond où
le flux se trompe de plus de 0,01 est à exp(−@@flux_casse_des@@). Signe de delta : la fraction
continue rend la même Phi pour s = −1 et s = +1, écart @@ctl_signe@@ ; c'est attendu (les deux
chaînes se déduisent par une conjugaison).

Contrôle contre la note du 15/11 : pour (6, 2) à kappa = 0,30, Phi = @@phi62@@ ; la série de cette
note donnait Gamma_1 / |delta| = @@g1_moins@@ à delta = −0,0125 et @@g1_plus@@ à +0,0125. Phi
s'écarte de leur moyenne de @@phi62_ecart_moy@@ en relatif.

Contrôle de la limite contre le bloc déposé. Sur @@lim_n@@ états, la chaîne du bloc d'ordre 3
réduite à ses sauts du premier ordre (tables et barrière du moteur, w2 réel), jouée à
|delta| = 0,001 et 0,0001 des deux signes à kappa fixé, rejoint Phi : l'écart sur le logarithme
vaut au plus @@lim_pire@@ à |delta| = 0,0001 et s'annule comme delta, avec un coefficient
par état (de @@lim_coef_min@@ à @@lim_coef_max@@) constant à @@lim_coef_disp@@ près d'un désaccord à
l'autre. Les deux codes ne partagent que les éléments de matrice du moteur.

## 3. Étape 0.1 : la superposition, sur les états déjà joués

États : les @@n_juges_100@@ jugés du delta 100 et les @@n_juges_98@@ jugés et qualifiés du delta 98
(largeurs de plateau du gel ter). Domaine : celui du gel « ordre 3 » (e_bord < 0,7, stabilité de
la chaîne d'ordre 3 au plus 0,05) ; il compte @@n_dom@@ états. Pour chacun, kappa est recalculé
par le moteur (écart au kappa de la feuille du delta 100 : @@ecart_kappa@@) et Phi par la fraction
continue (écart à la diagonalisation : @@sp_arith@@ au pire).

Dans le domaine : Gamma_pl / |delta| va de @@g_min@@ à @@g_max@@ ; kappa de @@kappa_min@@ à
@@kappa_max@@ ; |delta| de @@delta_min@@ à @@delta_max@@ ; barrières de @@mb_min@@ à @@mb_max@@
barreaux. La droite ln(Gamma_pl / |delta|) = a + b ln Phi a pour pente b = @@pente@@, corrélation
@@corr@@, écart-type restant @@sigma_droite@@. |r| vaut @@r_med@@ en médiane, @@r_max@@ au pire ;
rapporté à l'exposant, @@rel_med@@ pour cent en médiane et @@rel_max@@ pour cent au pire (figure :
figure_superposition_loi_echelle_v1.png). Signe :
r > 0 à @@sg_neg@@ états à delta < 0, r < 0 à @@sg_pos@@ à delta > 0. Phi elle-même bouge de
@@stab_phi_med@@ en médiane et @@stab_phi_max@@ au pire sous l'absorbeur de la chaîne (doublé,
divisé par deux, reculé de quatre sites).

Ce r n'est pas un résidu inexpliqué : la chaîne d'ordre 3 le rend. L'écart entre r et sa valeur
par la chaîne d'ordre 3 vaut @@q3_med@@ en médiane et @@q3_max@@ au pire ; c'est le |ln q3| du
delta 100, redit. La superposition ne juge donc rien de plus que E1 ; elle dit que le terme
dominant, à lui seul, est une fonction d'une variable par étiquette, sur sept décades.

Hors du domaine (@@n_hors@@ états) : |r| vaut @@hors_med@@ en médiane, @@hors_max@@ au pire.

VARIANTE, essayée APRÈS avoir vu r, et déclarée comme telle. Prendre la variable d'échelle sur
le saut lointain plutôt que sur le saut du site de départ : kappa* = kappa × (X_c(w2) / X_c(2)) ×
(tau_0(2) / tau_0(w2)). Le changement de variable est minuscule (kappa* / kappa − 1 va de
@@rho_min@@ à @@rho_max@@ pour cent) mais Phi est raide : la pente d ln Gamma / d ln g des états
joués va de 21,5 à 43,9 (note du 15/11). Avec elle, |r*| vaut
@@rs_med@@ en médiane et @@rs_max@@ au pire (un facteur @@rs_max_facteur@@). Surtout, l'étendue de
r à l'intérieur d'une cellule tombe, à delta > 0, de @@et_pos_k@@ à @@et_pos_e@@ (médianes sur
les cellules) : le résidu n'y dépend presque plus de l'état. À delta < 0 elle passe de
@@et_neg_k@@ à @@et_neg_e@@ seulement. Je ne sais pas pourquoi les deux côtés diffèrent.

@@table_superposition@@

## 4. Étape 0.3 : la forme de Phi quand la barrière devient profonde

### 4.1 Le terme dominant et le logarithme

WKB discret sur la barrière, avec t_m / |delta| = lambda m^(5/2) (1 + a_L / m) : l'action vaut
M0 × intégrale de 0 à 1 de arccosh(x^(−3/2)) dx, et deux fois cette intégrale vaut
B(1/3, 1/2) = Gamma(1/3) Gamma(1/2) / Gamma(5/6) = @@I2@@ (par parties). Les logarithmes se
comptent : −3 pour kappa^2, −1 au point tournant, +3/2 pour la somme discrète (Stirling), +2 a_L
pour le premier écart de tau_m à m^(5/2). Avec les deux parts 3/11 et 8/11 de X_c,
a_L = 91/44 + (19 n1 + 17 n2) / 22, d'où c_L = 2 a_L − 5/2 = (18 + 19 n1 + 17 n2) / 11.
En variables physiques : −ln Phi → @@cst_dg@@ (|delta| / g)^(2/3) = @@cst_nu@@ nu0*.

Mesuré sur la chaîne, M0 de 4 à 4096 barreaux :

@@table_B@@

La pente mesurée est celle de −ln Phi − B M0 entre 2048 et 4096 barreaux, divisée par ln 2 ; elle
doit tendre vers c_L. d_L n'est pas dérivé : il est lu. Le rapport −ln Phi / (B M0) dit à quel
point le terme dominant seul est loin : @@rap62_16@@ pour (6, 2) et @@rap103_16@@ pour (10, 3) à
16 barreaux, la profondeur de la campagne ; @@rap00_4096@@ pour le vide à 4096.

Pour le vide : ln Phi = −B M0 + (18/11) ln M0 + @@d00@@, à @@err00_4@@ près dès M0 = 4 et à
@@err00_16@@ près à M0 = 16.

### 4.2 L'exposant local

p = −d ln(−ln Phi) / d ln kappa ; une exponentielle étirée d'exposant 2/3 donne p = 2/3.

@@table_C@@

Dans la plage jouée (kappa de @@kappa_min@@ à @@kappa_max@@), p va de @@p_joue_min@@ à
@@p_joue_max@@ pour (6, 2) et (10, 3). Il n'est qu'à @@p_1e4_103@@ pour (10, 3) à kappa = 0,0001.
C'est le logarithme à grand coefficient qui retarde l'asymptote ; il vient de ce que chaque
quantum de l'étiquette grossit les sauts.

Ma note du 15/11 retirait l'exposant 2/3 comme non testé. Testé : c'est l'exposant asymptotique
de la chaîne, et il n'a rien à dire de la plage jouée.

### 4.3 Jusqu'où la loi descend dans le domaine gardé

En prenant e_bord = m_bord |delta| :

@@table_E@@

La 2D a lu jusqu'à @@decades_plancher@@ décades. À |delta| = 0,035, la garde e_bord < 0,7 laisse
la chaîne descendre à @@dec035_min@@ à @@dec035_max@@ décades selon l'étiquette. Pour les états
bas, e_bord < 0,7 se lit g > @@g_min_coef@@ |delta|^(5/2) (soit @@g_min_035@@ à |delta| = 0,035),
et l'exposant y est au plus @@exp_max_coef@@ / |delta|.

## 5. À fraction du seuil classique

Graines de la famille du moteur, occupations réelles (n1, n2) = f^2 nu0* (25/8, 1) à w2 = 2. En
variables x = m / nu0*, le double du saut rapporté au désaccord est une fonction h(x ; f) qui ne
dépend plus de nu0*, et le WKB donne −ln Phi → nu0* F(f), F(f) = 2 × intégrale de arccosh(x / h)
entre les deux points tournants.

@@table_D@@

Entre parenthèses, kappa. † : kappa > 1/2, l'état de la chaîne n'est plus porté par un site.
« vide » : la règle de barrière ne trouve aucun site. À grand kappa ma règle abandonne dès que
2 kappa tau_m / tau_0 dépasse 4 m au-delà de m = 8 (le « + 1 » de la règle du moteur n'a pas de
limite) : elle manque alors une barrière qui commencerait plus loin. C'est le cas à f = 0,8 et
nu0* = 335, où l'intégrale en voit une.

La chaîne rejoint l'intégrale quand nu0* grandit : @@ch03@@ pour @@F03@@ à f = 0,3, @@ch05@@ pour
@@F05@@ à f = 0,5. À fraction fixée, kappa croît comme nu0* : pour f ≥ 0,6 il dépasse 1/2 dès
nu0* de 10 à 40, l'état « de plus grand recouvrement avec le site 0 » n'est plus un état porté
par ce site, et les valeurs de la chaîne se dispersent de @@disp_grand_kappa@@ pour cent au plus
autour de l'intégrale. F(f) reste défini (c'est une action classique) ; c'est l'objet quantique
qu'on lui compare qui est à redéfinir, par son énergie et non par son recouvrement. Non fait.

À la profondeur de la campagne (nu0* = 5,24, f = 0,70, kappa = @@k07_camp@@) : la chaîne donne
@@ch07_camp@@, l'intégrale @@F07@@. Le terme dominant rend l'exposant à @@ecart07_pc@@ pour cent
près, soit @@ecart07_ln@@ en logarithme, un facteur @@ecart07_fact@@ sur la largeur. La barrière
disparaît vers f = 0,85 (F = @@F085@@) ; à f = 0,8, F = @@F08@@.

## 6. Étape 0.2 : la carte des corrections

Deux étiquettes, (0, 0) et (6, 2). Neuf longueurs de barrière (4 à 64 barreaux), six désaccords
au bout (e = m_bord |delta| de 0,075 à 1,0), les deux signes : @@n_carte@@ points, @@n_carte_calc@@
calculés (@@n_carte_non@@ non calculés : à delta = +0,25 la règle du moteur ne trouve plus de fin
à la barrière). Les w2 parcourus ne sont pas des points de la campagne ; aucune largeur 2D n'y
est lue ni prédite. À chaque point : la loi d'échelle, les chaînes d'ordre 2 et 3 des blocs
déposés, et la stabilité de l'ordre 3 sous son absorbeur (doublé, divisé par deux, reculé de
quatre sites), comme au gel.

Largeur des chaînes d'ordre 2 et 3 : le flux du bloc tant que Gamma / |delta| dépasse 10^−15
(@@n_flux@@ points) ; en dessous, quotient de Rayleigh complexe en précision arbitraire sur la
même matrice (@@n_mp@@ points). Contrôles : ma matrice contre les blocs déposés, écart relatif
@@ctl_mat@@ ; précision arbitraire contre flux, même matrice, @@ctl_mp_flux@@.

r3 à delta < 0 ; à delta > 0. \* : chaîne d'ordre 3 instable (stabilité au-dessus de 0,05).

État (0, 0) :

@@table_carte_00@@

État (6, 2) :

@@table_carte_62@@

Lecture.

- Les @@n_long@@ points de 24 barreaux ou plus sont stables, jusqu'à e = 1,0. |r3| y vaut au
  plus @@r3_long_00@@ pour le vide et @@r3_long_62@@ pour (6, 2) ; les ordres 2 et 3 y diffèrent
  d'au plus @@r32_long@@.
- Pour (6, 2), à e fixé, |r3| décroît avec la longueur. Pour le vide il sature : à e = 0,7,
  @@c00_48m@@ et @@c00_48p@@ à 48 barreaux, @@c00_64m@@ et @@c00_64p@@ à 64, pour un exposant de
  @@lnphi_64_00@@. L'erreur de la loi d'échelle sur ln Gamma reste d'ordre un quand l'exposant se
  compte en centaines.
- Les @@n_inst@@ points instables ont tous @@inst_mb_max@@ barreaux au plus ; le plus petit
  |delta| parmi eux est @@inst_d_min@@. Les @@n_stab@@ points stables vont jusqu'à
  e_bord = @@stab_e_max@@ et |delta| = @@stab_d_max@@.
- Plus grand e pour lequel la chaîne est stable aux deux signes, sans trou. Vide : @@stable_00@@.
  (6, 2) : @@stable_62@@.

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

@@table_vide@@

De 3 à 5 barreaux, Gamma / |delta| va de @@vide_G3@@ à @@vide_G5@@ : la plage de Gamma / |delta|
que la 2D a déjà lue. En largeur absolue c'est plus serré : la plus petite largeur de plateau de
ces deux runs vaut @@gabs_min@@, et à |delta| = 0,02 le vide serait à @@vide_abs_3@@ (3 barreaux) et
@@vide_abs_5@@ (5 barreaux). La forme fermée y est à @@vide_ff_max@@ de la chaîne, et les ordres 2 et 3 ne déplacent
la largeur que de @@vide_r3_max@@ au plus. Mais la chaîne d'ordre 3 y est instable sous son
absorbeur jusqu'à @@vide_stab_max@@ : pour le vide, à ces profondeurs, le meilleur prédicteur
disponible est la loi d'échelle elle-même, avec une tolérance qui porte cette instabilité. Les
couplages vont de @@vide_g_min@@ à @@vide_g_max@@, du même ordre que ceux de la campagne.

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
- L-3. Phi dépend de l'absorbeur de la chaîne à @@stab_phi_max@@ près au pire sur les états
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

@@pieces_registre@@

De ce lot :

@@pieces_lot@@
    (ce script)       construction_note_loi_echelle_machine1_v1.py, gabarit_note_loi_echelle_machine1_v1.md

Le PNG est binaire : son empreinte est l'empreinte brute.
