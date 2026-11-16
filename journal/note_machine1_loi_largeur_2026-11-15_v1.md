# Note hors chaîne : la loi de la largeur — étalon, ordre 3, structure

Plume : machine 1. Date : 15/11/2026, soir. Statut : exploration hors chaîne, non certifiée, non
rejouée par machine 2, faite APRÈS COUP sur des états déjà joués. Elle ne tranche rien, ne
modifie aucune pièce citée et n'ouvre aucun gel. Ouverture, selon machine 1 : l'opérateur a
demandé la méthode (15/11/2026, 18 h 44), puis écrit « ouvre » (18 h 50).

Aucune largeur 2D n'est calculée ici. Ce qui est calculé : de l'arithmétique sur des pièces, des
chaînes à une dimension (quelques dizaines de sites) et un contrôle d'algèbre sur de petites
matrices hermitiennes, sans absorbeur, où aucune largeur n'est lue (section 3.2). Les éléments
de matrice sont ceux du moteur (82a0be882568fe0c), appelés tels quels. La chaîne d'ordre 2 est
le bloc déposé (7cd5977bc27bebc1).

Référence : les largeurs de plateau Gamma_pl(A) que le run du gel « qualification E-B ter » a
rendues (verdict de BOCAL4 2cd1f84efa02f2ab, lot de résultat 1f057651c8f69eb6). L'acte de ce run
(projet v1, 751165a3eee613d9) attend le contreseing de machine 2 : cette référence n'est pas
déposée. Si un nombre de ce verdict bougeait, la note serait à refaire. Les états sont les 132
que le delta 98 a jugés (sortie 10887c60d5f55bcf, verdict 4195583a970eaf70) ; 131 sont QUALIFIÉS
par le run ter et sont seuls gardés (L3 rang 5 est écarté).

## 0. Verdict

1. L'étalon. Contre la largeur de plateau, les trois bandes du delta 98 tiennent encore : aucun
   état hors borne sur 131, q2 de 1,015 à 1,682 (contre la lecture déposée : 1,002 à 1,679). Et
   le résidu devient presque une constante par point : l'étendue de ln q2 à l'intérieur d'un
   point passe de 0,062 à 0,020 (médianes). La dispersion que le delta 98 voyait d'un état à
   l'autre était, pour l'essentiel, celle de la lecture déposée (k = 3, F1, 20 couches), pas
   celle de la chaîne.
2. L'ordre 3 ferme le résidu là où le développement converge, et pas ailleurs. Trois termes
   d'ordre g^3, dérivés sans paramètre : une correction du saut entre voisins, un saut au
   troisième voisin et un saut au cinquième. Soit e_bord le désaccord atteint au dernier barreau
   de la barrière. Pour e_bord < 0,3 (27 états), l'écart médian à la largeur 2D vaut 24,7 pour
   cent avec la chaîne du moteur, 2,4 avec l'ordre 2, 0,8 avec l'ordre 3. Pour e_bord < 0,7 (83
   états), l'ordre 3 fait mieux que l'ordre 2 à 83 états sur 83. Au-delà (48 états), il fait
   pire à 37, jusqu'à un facteur 6,6 (L4 rang 0), et la chaîne d'ordre 3 n'est plus stable sous
   son propre absorbeur.
3. Contrôle indépendant : les énergies. Le décalage d'énergie de l'état, qui n'a servi à rien
   régler, est rendu à 0,10 pour cent près par l'ordre 2 et à 0,004 pour cent près par l'ordre 3
   (médianes ; pires états 0,46 et 0,08 pour cent). L'ordre 3 l'améliore aux douze points, y
   compris là où sa largeur diverge.
4. La loi. La chaîne est un développement en puissances du désaccord delta, à rapport kappa =
   t_0 / |delta| fixé (saut du site de départ rapporté au désaccord) : Gamma = |delta| ×
   Phi(kappa ; état) × [1 + a delta + b delta^2 + …]. La chaîne seule le montre (section 4.1).
   Les largeurs 2D le montrent par la parité du résidu : après l'ordre 1 il change de signe avec
   delta, après l'ordre 2 il est du même côté des deux côtés de 2,00, après l'ordre 3 il change
   de signe à nouveau (section 4.2). Ce qui décide de l'accord n'est pas delta seul : c'est le
   saut atteint au bout de la barrière, soit e_bord / 2 (section 3.6).
5. Ce que j'avais annoncé à l'opérateur et qui est faux. Ma réponse de méthode disait : « la
   pente vaut deux fois le nombre de barreaux, donc un entier pair ». La chaîne dit de 21,5 à
   43,9, soit de 3,4 à 7,7 par barreau. La barrière est peu profonde (2 t / |e| vaut 0,81 en
   médiane sur ses 932 sites) : ni le produit perturbatif ni le WKB discret n'y sont
   quantitatifs (écart-type 0,81 en logarithme pour le WKB, pire état à un facteur 10). Il n'y a
   pas de formule fermée courte : la loi est la chaîne. L'exposant 2/3 (« un calcul de coin de
   table, à ne pas citer ») n'est pas testé ; je le retire.
6. Cela vaut un gel, sur un énoncé plus étroit que celui que j'espérais : dans un domaine
   calculable avant tout run (e_bord sous un seuil, chaîne d'ordre 3 stable sous son absorbeur),
   l'ordre 3 rend la largeur 2D qualifiée à quelques pour cent. Ici, ce domaine compte 56 états
   sur 131 : écart médian 1,9 pour cent, pire 6,2 pour cent. Section 5.

## 1. Notations

Échelle résonante de l'état (n1, n2) : sites m, (n1 + 2m, n2 + m). Saut t_m entre les sites m et
m + 1. Désaccord du site e_m = m delta + Sigma2(m) − Sigma2(0), delta = w2 − 2. Barrière : les
sites où |e_m| > 2 |t_m| (règle du moteur) ; m_bord est le dernier, e_bord = |e_m| à ce site.
kappa = t_0 / |delta|. q_n = Gamma de la chaîne d'ordre n / Gamma_pl(A) ; ordre 1 : chaîne du
moteur, telle que déposée ; ordre 2 : bloc déposé (déplacements, saut au second voisin, sites
bas) ; ordre 3 : bloc de cette note. « Écart » veut dire |ln q| ; il est donné tel quel dans les
tableaux, et converti en pour cent (exp − 1) dans le verdict.

## 2. Étape 1 : l'étalon

La comparaison du delta 98 est refaite avec Gamma_pl(A) au dénominateur. Rien n'est recalculé :
la chaîne est celle du dépôt.

| bande | borne | états | q2 contre la lecture déposée : min, médiane, max | q2 contre le plateau : min, médiane, max | hors borne |
|---|---|---|---|---|---|
| proche | 1,25 | 46 | 1,002 ; 1,054 ; 1,136 | 1,015 ; 1,079 ; 1,097 | 0 |
| moyenne | 1,60 | 41 | 1,041 ; 1,128 ; 1,447 | 1,085 ; 1,100 ; 1,383 | 0 |
| lointaine | 2,00 | 44 | 1,093 ; 1,271 ; 1,679 | 1,117 ; 1,244 ; 1,682 | 0 |

| point | delta | états | q2 déposé : min ; max | q2 plateau : min ; max |
|---|---|---|---|---|
| C1 | -0,03 | 8 | 1,002 ; 1,055 | 1,017 ; 1,040 |
| C2 | -0,06 | 11 | 1,044 ; 1,136 | 1,079 ; 1,097 |
| C3 | +0,03 | 14 | 1,015 ; 1,032 | 1,015 ; 1,025 |
| C4 | +0,06 | 13 | 1,067 ; 1,091 | 1,079 ; 1,086 |
| M1 | -0,07 | 11 | 1,075 ; 1,140 | 1,088 ; 1,099 |
| M2 | -0,08 | 13 | 1,041 ; 1,144 | 1,085 ; 1,106 |
| M3 | +0,07 | 8 | 1,114 ; 1,153 | 1,153 ; 1,163 |
| M4 | +0,10 | 9 | 1,356 ; 1,447 | 1,352 ; 1,383 |
| L1 | -0,11 | 14 | 1,093 ; 1,226 | 1,117 ; 1,180 |
| L2 | -0,12 | 10 | 1,171 ; 1,314 | 1,204 ; 1,250 |
| L3 | +0,11 | 11 | 1,273 ; 1,350 | 1,259 ; 1,345 |
| L4 | +0,12 | 9 | 1,508 ; 1,679 | 1,599 ; 1,682 |

L'ajustement à un paramètre de la note du 14/11 (022d32238a66df6b), ln q = c delta^2 m_bord,
donne contre le plateau c = 2,66 (corrélation 0,94, écart-type restant 0,042) ; contre la
lecture déposée, 2,64 (0,91 ; 0,052). Un meilleur prédicteur du résidu de l'ordre 2 est e_bord^2
/ m_bord : c = 2,38, corrélation 0,98, écart-type restant 0,030. C'est un ajustement après coup,
pas une dérivation.

## 3. Étape 3 : l'ordre 3

### 3.1 Ce qui est ajouté

Le hamiltonien effectif sur l'échelle, à l'ordre g^3, forme symétrique (formules de Löwdin ; A :
les sites de l'échelle, B : le reste) :

    H3_mm' = −(1/2) Σ_{l∈B, m''∈A} [ V_ml V_lm'' V_m''m' / ((E_m' − E_l)(E_m'' − E_l))
                                    + V_mm'' V_m''l V_lm' / ((E_m − E_l)(E_m'' − E_l)) ]
             +(1/2) Σ_{l,l'∈B} V_ml V_ll' V_l'm' [ 1/((E_m − E_l)(E_m − E_l'))
                                                   + 1/((E_m' − E_l)(E_m' − E_l')) ]

La parité de x^5 ne laisse à cet ordre que des sauts à un nombre impair de barreaux : T3_m,
correction du saut entre voisins ; W3_m, saut au troisième voisin ; W5_m, saut au cinquième
voisin (trois pas de cinq quanta, tous hors échelle). Les énergies sont les énergies libres du
moteur ; absorbeur, longueur et lecture de l'état sont ceux de la chaîne d'ordre 2. Rapportés au
saut du premier ordre, W3 et W5 valent au plus 0,0184 et 0,0009 dans les barrières des 131 états
; retirer W5 déplace la largeur d'ordre 3 d'au plus 0,013 (en |ln|) dans le domaine de la
section 3.6, et d'au plus 0,094 hors de lui.

### 3.2 Contrôles d'algèbre (aucune largeur n'y est lue)

- (V0) Les éléments de x^5 du moteur contre une matrice construite à part (opérateurs
  d'échelle), 3600 éléments : pire écart relatif 6,8e-16.
- (V1) La formule, écrite à part en matrices denses, contre le hamiltonien effectif canonique
  exact d'une base tronquée hermitienne (13 niveaux par mode, w2 = 2,11, échelle de (3, 1),
  quatre couplages de 2e-4 à 1,6e-3). Le reste sur le saut entre voisins décroît comme g^5,00
  avec le terme d'ordre 3 et comme g^3,00 sans lui (attendu : 5 et 3) ; sur le troisième voisin,
  g^5,04 et g^3,00 ; sur la diagonale et le second voisin, g^4,00 et g^4,00 (attendu : 4). Au
  cinquième voisin, la base n'offre qu'un élément, qui tombe au plancher d'arrondi aux petits
  couplages : sans le terme le reste suit g^3,00, et au plus fort couplage le terme n'en laisse
  que la fraction 2,2e-03. Au quatrième voisin, que la parité interdit à l'ordre 3, le reste
  suit g^4,01 (attendu : 4).
- (V2) Les tables du bloc (sommes sur les chemins, éléments du moteur) contre la formule dense,
  sur trois échelles : pire écart relatif 2,8e-13 pour T3, 1,0e-13 pour W3, 2,6e-14 pour W5.

La chaîne d'ordre 2 refaite ici redonne celle du dépôt à 2,1e-09 près au pire, d'une plateforme
à l'autre.

### 3.3 Par classe de e_bord

| e_bord | delta | états | écart médian, ordre 1 | ordre 2 (pire) | ordre 3 (pire) | ordre 3 meilleur que 2 | stabilité de la chaîne d'ordre 3, médiane |
|---|---|---|---|---|---|---|---|
| 0,0 à 0,3 | < 0 | 10 | 0,462 | 0,032 (0,096) | 0,008 (0,014) | 10 sur 10 | — |
| 0,0 à 0,3 | > 0 | 17 | 0,174 | 0,022 (0,078) | 0,008 (0,037) | 17 sur 17 | — |
| 0,0 à 0,3 | tous | 27 | 0,221 | 0,024 (0,096) | 0,008 (0,037) | 27 sur 27 | 0,013 |
| 0,3 à 0,5 | < 0 | 23 | 0,290 | 0,093 (0,164) | 0,019 (0,034) | 23 sur 23 | — |
| 0,3 à 0,5 | > 0 | 9 | 0,494 | 0,081 (0,231) | 0,041 (0,136) | 9 sur 9 | — |
| 0,3 à 0,5 | tous | 32 | 0,406 | 0,092 (0,231) | 0,026 (0,136) | 32 sur 32 | 0,054 |
| 0,5 à 0,7 | < 0 | 22 | 0,129 | 0,090 (0,223) | 0,039 (0,115) | 22 sur 22 | — |
| 0,5 à 0,7 | > 0 | 2 | 0,503 | 0,080 (0,080) | 0,025 (0,026) | 2 sur 2 | — |
| 0,5 à 0,7 | tous | 24 | 0,150 | 0,090 (0,223) | 0,039 (0,115) | 24 sur 24 | 0,027 |
| 0,7 à 1,0 | < 0 | 12 | 0,193 | 0,198 (0,217) | 0,221 (0,413) | 5 sur 12 | — |
| 0,7 à 1,0 | > 0 | 20 | 1,172 | 0,236 (0,311) | 0,209 (0,677) | 6 sur 20 | — |
| 0,7 à 1,0 | tous | 32 | 0,795 | 0,205 (0,311) | 0,210 (0,677) | 11 sur 32 | 0,371 |
| 1,0 à 2,0 | tous | 16 | 2,003 | 0,472 (0,520) | 0,971 (1,891) | 0 sur 16 | 0,239 |

« Stabilité » : le plus grand |ln| du rapport de la largeur d'ordre 3 à elle-même quand
l'absorbeur de la chaîne est deux fois plus fort, deux fois plus faible, ou reculé de quatre
sites. Pour e_bord < 0,3 elle vaut 0,013 en médiane (pire 0,029) : l'accord à 0,8 pour cent de
cette classe est au niveau de ce que la chaîne sait d'elle-même.

### 3.4 Par point

| point | delta | e_bord : min ; max | q2 médian | q3 : min ; médiane ; max | stabilité d'ordre 3, médiane |
|---|---|---|---|---|---|
| C1 | -0,03 | 0,24 ; 0,29 | 1,029 | 0,986 ; 0,997 ; 1,008 | 0,009 |
| C2 | -0,06 | 0,35 ; 0,58 | 1,095 | 0,941 ; 0,966 ; 0,976 | 0,016 |
| C3 | +0,03 | 0,12 ; 0,21 | 1,021 | 1,001 ; 1,008 ; 1,013 | 0,013 |
| C4 | +0,06 | 0,25 ; 0,50 | 1,084 | 1,025 ; 1,038 ; 1,045 | 0,066 |
| M1 | -0,07 | 0,34 ; 0,60 | 1,095 | 0,958 ; 0,966 ; 0,986 | 0,011 |
| M2 | -0,08 | 0,23 ; 0,61 | 1,095 | 0,967 ; 0,985 ; 0,994 | 0,045 |
| M3 | +0,07 | 0,74 ; 0,89 | 1,158 | 1,206 ; 1,232 ; 1,275 | 0,038 |
| M4 | +0,10 | 0,97 ; 1,20 | 1,365 | 1,618 ; 1,882 ; 1,988 | 0,206 |
| L1 | -0,11 | 0,32 ; 0,83 | 1,170 | 0,661 ; 0,948 ; 1,021 | 0,817 |
| L2 | -0,12 | 0,68 ; 0,91 | 1,234 | 0,856 ; 1,036 ; 1,268 | 0,649 |
| L3 | +0,11 | 0,47 ; 0,97 | 1,289 | 0,848 ; 0,999 ; 1,968 | 0,635 |
| L4 | +0,12 | 1,47 ; 1,77 | 1,629 | 2,636 ; 4,113 ; 6,624 | 0,311 |

Aux quatre points lointains (|delta| de 0,11 à 0,12) et à M4, la largeur d'ordre 3 dépend de
l'absorbeur de la chaîne : les q3 de ces lignes sont ceux du réglage du delta 98 et n'ont pas de
sens au-delà.

### 3.5 Une étiquette suivie d'un point à l'autre

L'état (6, 2) est jugé et qualifié à sept points. Rangé par kappa :

| point | delta | kappa | m_bord | e_bord | Gamma_pl / |delta| | q1 | q2 | q3 |
|---|---|---|---|---|---|---|---|---|
| L2 | -0,12 | 0,1775 | 8 | 0,907 | 9,951e-11 | 1,283 | 1,215 | 0,884 |
| M1 | -0,07 | 0,1777 | 9 | 0,603 | 1,436e-10 | 0,896 | 1,089 | 0,960 |
| L1 | -0,11 | 0,2367 | 5 | 0,528 | 8,086e-07 | 0,950 | 1,175 | 1,020 |
| M2 | -0,08 | 0,2369 | 5 | 0,388 | 9,188e-07 | 0,844 | 1,104 | 0,990 |
| C4 | +0,06 | 0,2376 | 6 | 0,373 | 4,944e-07 | 1,613 | 1,085 | 1,044 |
| C3 | +0,03 | 0,2671 | 5 | 0,152 | 1,263e-05 | 1,136 | 1,021 | 1,008 |
| L3 | +0,11 | 0,2676 | 6 | 0,718 | 4,633e-06 | 3,133 | 1,263 | 1,523 |

Les sept points forment trois groupes de kappa presque égal (0,178 ; 0,237 ; 0,267), à des
désaccords très différents. Dans chaque groupe, Gamma_pl / |delta| tient dans un facteur 1,4,
1,9 et 2,7 ; d'un groupe à l'autre, la même quantité parcourt 5,1 décades. C'est la forme Gamma
= |delta| × Phi(kappa) lue sur les largeurs 2D elles-mêmes ; l'écart à kappa égal est la
correction en delta, que q1, q2 et q3 mesurent.

### 3.6 Pourquoi la série casse

Lecture, non démontrée. Le développement a pour petit paramètre, au site m, le saut t_m rapporté
aux dénominateurs des états hors échelle, qui sont de l'ordre de la fréquence de l'oscillateur
(prise pour unité). Or la barrière finit, par définition, au dernier site où |e_m| > 2 t_m : au
bout de la barrière ce paramètre vaut à peu près e_bord / 2 (sur les 131 états, e_bord / t_bord
va de 2,00 à 2,23). e_bord range donc les états parce qu'il mesure le saut au dernier barreau.
Il vaut à peu près m_bord × |delta| : il grandit avec le désaccord et avec la longueur de la
barrière, donc quand le couplage baisse.

Exemple. À L4, état lu (11, 2), la barrière compte 13 sites et finit à un désaccord de 1,77 et
un saut de 0,88. Les deux parts de la correction T3 (chemins hors échelle, chemins repassant par
l'échelle) y valent +8,3 et -8,2 fois le saut du premier ordre, et leur somme +0,07 : le terme
d'ordre 3 y est la différence de deux grands nombres. À C1, la barrière finit à un désaccord de
0,24 à 0,29.

Domaine calculable avant tout run, lu sur ces données : e_bord < 0,7 et stabilité de la chaîne
d'ordre 3 au plus 0,05. Il compte 56 états (C1 8, C2 11, C3 14, C4 5, M1 11, M2 7). L'écart de
l'ordre 3 y vaut 0,019 en médiane, 0,060 au pire ; celui de l'ordre 2, 0,081 et 0,096. L'ordre 3
y fait mieux à 56 états sur 56.

## 4. Étape 2 : la structure

### 4.1 Un développement en delta à kappa fixé (chaîne seule)

À étiquette et kappa fixés, on fait varier delta ; les w2 parcourus ne sont pas des points de la
campagne et aucune largeur 2D n'y est lue ni prédite. Raison attendue : le saut vaut kappa ×
delta × (un élément réduit) ; à kappa fixé, la chaîne du premier ordre est delta fois une
matrice qui ne dépend que de kappa et de l'état, et l'ordre n en g pèse delta^(n − 1) devant
elle (à la dépendance en w2 des éléments de matrice près). Gamma_1 : sauts du premier ordre
seuls, sites bas compris (ce n'est pas la chaîne du moteur) ; Gamma_2, Gamma_3 : ordres 2 et 3
complets. État (6, 2), kappa = 0,30 :

| delta | m_bord | e_bord | Gamma_1 / |delta| | ln(Gamma_2 / Gamma_1) / delta | ln(Gamma_3 / Gamma_2) / delta^2 |
|---|---|---|---|---|---|
| -0,0125 | 3 | 0,037 | 1,958e-04 | -4,59 | -12,8 |
| -0,0250 | 3 | 0,074 | 1,963e-04 | -4,27 | -12,8 |
| -0,0500 | 3 | 0,148 | 1,972e-04 | -3,62 | -12,7 |
| -0,0750 | 3 | 0,220 | 1,982e-04 | -2,96 | -12,7 |
| -0,1000 | 3 | 0,291 | 1,992e-04 | -2,27 | -11,8 |
| +0,0125 | 3 | 0,038 | 1,949e-04 | -5,26 | -12,6 |
| +0,0250 | 4 | 0,101 | 1,921e-04 | -5,51 | -12,2 |
| +0,0500 | 4 | 0,205 | 1,912e-04 | -6,18 | -11,3 |
| +0,0750 | 4 | 0,312 | 1,904e-04 | -6,90 | -9,4 |
| +0,1000 | 4 | 0,421 | 1,895e-04 | -7,69 | -13,3 |

Gamma_1 / |delta| ne bouge que de 5,1 pour cent quand |delta| varie d'un facteur 8 et que delta
change de signe (3 à 4 barreaux ; à kappa = 0,22, 6 à 8 barreaux : 8,3 pour cent ; à (10, 3),
kappa = 0,20, 17 à 21 barreaux : 30 pour cent). La correction d'ordre 2 a un terme dominant
linéaire en delta, qui change de signe avec lui : ln(Gamma_2 / Gamma_1) / delta vaut -4,59 à
delta = −0,0125 et -5,26 à +0,0125 ; la dérive du reste de la colonne est sa courbure. Celle
d'ordre 3 est proportionnelle à delta^2 tant que e_bord reste petit : côté delta < 0, le
coefficient va de -12,65 à -12,76 sur 4 valeurs à kappa = 0,30, de -18,61 à -19,43 sur 4 valeurs
à kappa = 0,22. Côté delta > 0, où la barrière gagne un barreau, il est moins net : de -9,4 à
-13,3 à kappa = 0,30. Dans ces deux séries il est négatif des deux côtés : c'est le résidu d'un
seul signe de l'ordre 2, celui que la note du 14/11 laissait sans cause. À (10, 3), où e_bord
dépasse 0,4 dès |delta| = 0,025, il n'y a plus de coefficient.

### 4.2 La parité du résidu, sur les largeurs 2D

| résidu après | delta < 0 : ln q < 0 | delta > 0 : ln q > 0 | lecture |
|---|---|---|---|
| l'ordre 1 | 52 sur 67 | 64 sur 64 | change de signe avec delta, sauf 15 états côté delta < 0 |
| l'ordre 2 | 0 sur 67 | 64 sur 64 | du même côté : q2 > 1 partout |
| l'ordre 3 | 53 sur 67 | 58 sur 64 | change de signe avec delta |

Dans le domaine de la section 3.6 : 33 sur 37 et 19 sur 19 après l'ordre 3. C'est la signature
d'une série en puissances de delta ; le terme suivant serait impair. Il n'est pas calculé.

### 4.3 Les pentes, et les formes fermées qui ne tiennent pas

Pente d ln Gamma / d ln g de la chaîne d'ordre 2, à état et désaccord fixés (différence centrée
à 2 pour cent) : de 21,5 à 43,9, médiane 30,5. Elle suit pente = 2,60 m_bord + 12,5 (écart-type
2,6), et non 2 m_bord. Une variation de 2 pour cent du couplage change la largeur d'un facteur
1,53 à 2,38.

La raison : sur les 932 sites de barrière des 131 états, 2 t / |e| va de 0,44 à 1,00 (médiane
0,81, premier décile 0,64). La barrière est partout peu profonde, ce qui tient au choix des
points (fraction 0,70 du seuil, largeurs au-dessus de dix planchers). Dans ce régime :

| forme fermée | ln Gamma_pl = a + b × (−2 action) : b | écart-type restant (ln) | pire état (ln) |
|---|---|---|---|
| WKB discret, somme des arccosh(|e_m| / 2 racine(t_{m−1} t_m)) | 0,86 | 0,81 | 2,29 |
| action du moteur, somme des ln(|e_m| / 2 t_m) | 2,21 | 1,03 | 2,33 |
| produit perturbatif, somme des ln(|e_m| / t_{m−1}) | 0,69 | 1,04 | 2,89 |

Une loi exigerait b = 1 et un écart-type de quelques centièmes. Aucune de ces formes n'est la
loi ; la chaîne, qui est le calcul exact sur l'échelle, l'est.

## 5. Ce qu'un gel jugerait (proposition ; rien n'est décidé)

- A. Le domaine. À des points neufs, pour les états où e_bord est sous un seuil gelé et où la
  chaîne d'ordre 3 est stable sous son absorbeur, l'ordre 3 rend la largeur de plateau dans une
  tolérance gelée, et fait mieux que l'ordre 2. Les deux gardes se calculent avant tout run,
  sans 2D.
- B. Le balayage en couplage. À w2 fixé et neuf, quelques couplages sur un facteur 1,3 à 1,5 :
  la chaîne y prédit une largeur qui change de plusieurs décades. C'est l'épreuve la plus dure,
  et la plus lisible.
- C. La parité. Dans le domaine, le signe du résidu de l'ordre 3 suit celui de delta.
- D. Hors domaine. L'ordre 2 reste dans les bandes du delta 98 ; l'ordre 3 y est déclaré non
  applicable d'avance.

Instrument : la sonde et la feuille du gel E-B ter, inchangées, pour que chaque largeur arrive
qualifiée dans le même run. Points : jamais joués, tirés par une règle ou par machine 2. Bornes
et probabilités : annoncées après que la chaîne a calculé les points tirés, pas avant.

## 6. Limites

- L-1. Après coup, sur 131 états connus. L'ordre 3 est dérivé sans paramètre, mais les seuils
  0,3, 0,7 et 0,05 sont lus sur ces données.
- L-2. Une plume. Le bloc d'ordre 3 n'a que mes trois contrôles ; machine 2 n'a rien rejoué.
- L-3. La référence (largeurs de plateau) n'est pas déposée ; elle tient à l'acte en
  contreseing.
- L-4. Hors du domaine, la largeur d'ordre 3 dépend de l'absorbeur de la chaîne : les q3 donnés
  n'y ont pas de sens. Je n'ai pas démêlé si cette instabilité est celle de la série ou un
  artefact d'une chaîne à sauts longs (les sauts au troisième et au cinquième voisin peuvent y
  introduire des solutions parasites).
- L-5. L'ordre 4 n'est pas calculé. « Développement en delta » est établi sur la chaîne aux
  ordres 2 et 3 seulement ; « la série diverge » au-delà de e_bord = 0,7 est une lecture de deux
  symptômes (accord perdu, chaîne instable), pas une démonstration.
- L-6. Domaine couvert : fraction 0,70, canal (2, 1) de x^5, |delta| de 0,03 à 0,12, facteurs
  2/3 à 3/2. Rien au-delà.
- L-7. Défauts de ma plume, dans ma réponse de méthode à l'opérateur (sa demande est de 18 h
  44). D-LOI-1 : « la pente vaut deux fois le nombre de barreaux, donc un entier pair » est faux
  (section 4.3) ; « Elle sera bonne sur la pente et moins sur le préfacteur » aussi : la formule
  fermée n'est bonne ni sur l'une ni sur l'autre. D-LOI-2 : « S'il efface le résidu, la chaîne
  d'ordre 3 est la loi au niveau de l'instrument » n'est vrai que dans le domaine ; et la note
  du 14/11 n'annonçait que « Le troisième ordre (correction du saut entre voisins) », en
  oubliant les sauts au troisième et au cinquième voisin, du même ordre. D-LOI-3 : ma première
  lecture de l'ordre 3, par point, concluait qu'il ne fermait rien ; c'est le classement par
  e_bord qui montre où il ferme. D-LOI-4 : ma première écriture du bloc d'ordre 3 oubliait le
  saut au cinquième voisin (son commentaire disait que la parité ne laissait que deux termes) ;
  je l'ai vu en relisant, avant tout envoi ; les nombres de cette note sont ceux du bloc
  complet.

## 7. Pièces (convention B)

Au registre (8d54bf9) :

    82a0be882568fe0c  scripts/m17_chaine_v17.py
    7cd5977bc27bebc1  scripts/chaine_ordre2_bloc_machine1_v1.py
    10887c60d5f55bcf  journal/sonde_ordre2.json
    4195583a970eaf70  journal/verdict_ordre2.json
    c2f3e5c9102dc1a7  journal/journal_delta_98_ordre2_chaine_EA_v1.md
    022d32238a66df6b  journal/note_machine1_residuel_chaine_EA_second_ordre_2026-11-14_v1.md

Hors registre :

    2cd1f84efa02f2ab  run_EB_ter/verdict_ter.json (machine 2, lot 1f057651c8f69eb6)
    751165a3eee613d9  journal_delta_nn_qualification_EB_ter_v1.md (machine 1, projet v1)

De ce lot :

    07273e069c20890f  etape1_etalon_machine1_v1.py
    f7c7dc606e587301  etape1_etalon_machine1_v1.log
    902e92444c733384  etape1_etalon_v1.json
    534ba246aa3b8973  ordre3_bloc_machine1_v1.py
    e398da8221a761a4  controle_algebre_ordre3_machine1_v1.py
    17c50c505f7b8093  controle_algebre_ordre3_machine1_v1.log
    fdb345c7a72596e2  controle_algebre_ordre3_v1.json
    d4cb7c7605c6da90  calcul_ordre3_machine1_v1.py
    436f66549dc3b2bd  calcul_ordre3_machine1_v1.log
    d356b07c31d2c8ee  ordre3_par_etat_v1.json
    51a78e0ffdcc75ac  forme_fermee_machine1_v1.py
    4bc4513df6602fd5  forme_fermee_machine1_v1.log
    770aa86c4063aecb  forme_fermee_v1.json
    4a788b08aa5192fd  structure_en_delta_machine1_v1.py
    67cac86a6d32d8a6  structure_en_delta_machine1_v1.log
    504409e1a12e46b8  structure_en_delta_v1.json
    (ce script)       construction_note_loi_machine1_v1.py

