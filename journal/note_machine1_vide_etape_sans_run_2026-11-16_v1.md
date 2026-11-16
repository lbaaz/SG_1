# Note hors chaîne : le vide — lecteur, absorbeur de chaîne, ce qu'un gel jugerait (étape sans run)

Plume : machine 1. Date : 16/11/2026. Statut : exploration hors chaîne, classe 3, non certifiée, non
rejouée par machine 2. Elle ne tranche rien, ne modifie aucune pièce citée et n'ouvre aucun gel.
Ouverture, selon machine 1 : à la fin de la note « loi d'échelle » (8548cc16fb746f56), machine 1 a
proposé une étape sans run avant tout gel du vide ; l'opérateur a écrit « j'ouvre » (16/11/2026,
11 h 03).

AUCUNE LARGEUR 2D DU SYSTÈME À FANTÔME N'EST CALCULÉE ICI, ni pour le vide ni pour un autre état.
Ce qui est calculé : des chaînes à une dimension ; et, en 2D, le seul JUMEAU SANS FANTÔME (signe
+1), où aucune échelle résonante n'existe. Les largeurs 2D citées pour les états déjà joués sont
lues dans les pièces de la note « loi d'échelle ». Registre lu sur clone neuf (tête dee73bd), non
écrit. Tous les nombres sont écrits par un script qui les lit dans les sorties (section 9).

## 0. Verdict

1. Le lecteur déposé sait lire l'état porté par (0, 0) : sa routine le fait déjà, pas sa chaîne de
   pièces. Le mode « étage 1 » du dépôt lit le site (0, 0) depuis l'énergie 0. Mais le mode
   « point » ne lit que des états choisis par la sonde dense (les quatorze de plus grand
   recouvrement avec la graine à fraction 0,70, au-dessus de dix planchers) : il faut une sonde
   dérivée, sans étage dense, et sa feuille. Section 1.
2. Le plancher n'était pas celui du lecteur. Au jumeau sans fantôme, à la géométrie du vide, les
   144 lectures sont suivies et rendent des largeurs de 1,9 × 10^-61 à 1,9 × 10^-35. Les
   « dix planchers » (1,33 × 10^-12) sont ceux de la décomposition dense, qui choisit les états ;
   la routine creuse, qui lit la largeur par le flux, n'a pas de plancher à ce niveau. Coût :
   94 à 114 s par cellule sur machine 1. Section 2.
3. Le procédé du lecteur n'est pas limité par la double précision. Sur une chaîne dont la largeur
   est connue par ailleurs, la routine déposée rend le logarithme de la largeur à 1,1 × 10^-13
   près jusqu'à exp(−535,7), soit 233 décades. Je retire la phrase de la note
   « loi d'échelle » selon laquelle aucun lecteur 2D en double précision ne lirait le régime
   profond : rien ne la soutient. Que le lecteur lise JUSTE à ces profondeurs en 2D n'est pas
   montré pour autant. Section 2.
4. L'instabilité de la chaîne d'ordre 3 a deux causes, et je n'en avais vu qu'une. (a) L'absorbeur
   déposé a une force qui suit le désaccord et non le saut : à barrière courte et petit désaccord
   il absorbe trop peu, et la chaîne du premier ordre en souffre autant que l'ordre 3. Un
   absorbeur adapté au saut la guérit : pour le vide, de 3 à 6 barreaux et |delta| ≤ 0,02, la
   largeur d'ordre 3 ne bouge plus que de 0,0077 au plus sous 18 variantes.
   (b) À désaccord plus grand, ce sont bien les termes d'ordre 3 après la barrière : 46
   des 118 points de la carte de 16 barreaux au plus restent instables, alors que les ordres 1
   et 2 y sont stables. Celle-là n'est pas guérie. Sections 3 et 4.
5. Le prédicteur du vide existe. Chaîne d'ordre 3 sous absorbeur adapté : de 3 à 6 barreaux et
   |delta| ≤ 0,02, elle s'écarte de la loi d'échelle de 0,034 au plus (3,5 pour
   cent), et l'ordre 2 de l'ordre 3 de 0,0038 au plus. La prédiction de la chaîne est donc
   arrêtée à 0,0077 près, son étendue. Qu'elle soit juste est une autre question : c'est
   celle qu'un gel poserait. Section 3.
6. Aux états déjà joués, l'absorbeur adapté abaisse l'ordre 3 de 0,0094 en médiane,
   moins que l'étendue médiane de chacune des deux règles sur ces états (0,0126 pour la
   déposée, 0,021 pour l'adaptée). Il rapproche la chaîne de la 2D
   à delta > 0 (71 sur 81) et l'en éloigne à delta < 0 (97 sur 104) ; aucun état ne
   sort des tolérances rappelées de E1. L'accord du delta 100 est donc au niveau de ce que
   l'absorbeur de la chaîne laisse indéterminé. Après coup ; ce n'est pas un rejeu du gel, et
   l'instrument déposé ne change pas. Section 5.
7. Une ligne profonde devient pensable. Si le lecteur lit en 2D ce qu'il lit sur une chaîne, le
   vide se prédit et se lirait bien au-delà de 6 barreaux : à 8, 12 et 16 barreaux la chaîne
   reste stable (étendue 0,0085 au plus) pour des largeurs jusqu'à 1,5 × 10^-32. C'est
   une possibilité, pas un fait. Section 6.
8. Suite, rien n'est décidé : le gel du vide est faisable. Ce qu'il demande est en section 7.

## 1. Le lecteur déposé et le vide (lecture du code)

Pièces lues : la sonde du lecteur du gel « ordre 3 » (d5cc48f48e37af99), sa sonde dense
(68baf04c73ed5d44), la routine de plateau de la feuille du gel ter.

- La routine. lire_etat lit UN état par itération inverse creuse à décalage fixe, depuis le site
  de Fock de l'étiquette, et rend la largeur par le flux, 2 eta <W>. Elle ne dépend d'aucune
  graine. Le mode « étage 1 » (témoin positif) l'appelle déjà au site (0, 0) avec l'énergie de
  départ 0.
- Ce qui manque. Le mode « point » prend ses états dans la sortie de la sonde dense : les
  quatorze états de plus grand recouvrement avec la graine cohérente à fraction 0,70, dont la
  largeur dense à k = 3 dépasse 1,33 × 10^-12 ; sa boîte (r_c) vient de la barrière de la
  graine ; ses refus contrôlent la table et la sortie dense. Le vide n'y entre pas.
- Ce qu'il faut. Une sonde dérivée par remplacements, comme les précédentes : un mode qui lit
  le site (0, 0) aux points d'une table, énergie de départ 0, r_c = 2 (m_bord + max(8, m_bord))
  + 2 (la règle du dépôt, sans graine), eta0 = |delta|, les quatre absorbeurs et les douze
  barreaux du dépôt ; pas d'étage dense. Et une feuille dérivée : la routine de plateau (cinq
  barreaux consécutifs à 5 pour cent) et les accords entre absorbeurs sont ceux du gel ter. Ce
  sont des pièces de classe 2, à certifier.
- Le décalage. Autour de l'énergie 0 les états de l'échelle sont espacés de |delta| ; le
  déplacement d'énergie du vide est très petit devant lui. Le décalage 0 désigne donc le vide.
  Non vérifié sur le système à fantôme, puisque rien n'y est lu ici.

## 2. Ce que le lecteur peut lire (sans lire le vide)

### 2.1 Le jumeau sans fantôme à la géométrie du vide

Routine déposée, lue telle quelle dans la sonde (canon contrôlé). Jumeau H+ : pas d'échelle
résonante, la largeur de l'état porté par (0, 0) n'y est fabriquée que par l'absorbeur. Quatre
absorbeurs, douze barreaux.

| barrière du vide | w2 | g | r_c | boîtes N | lectures suivies | largeur du jumeau : de ... à ... | durée (machine 1) |
|---|---|---|---|---|---|---|---|
| 3 barreaux | 101/50 | 5,54 × 10^-3 | 24 | 104 à 124 | 48 sur 48 | 2,4 × 10^-51 à 1,9 × 10^-35 | 100 s |
| 4 barreaux | 199/100 | 1,89 × 10^-3 | 26 | 106 à 126 | 48 sur 48 | 1,9 × 10^-61 à 2,8 × 10^-43 | 94 s |
| 5 barreaux | 101/50 | 3,35 × 10^-3 | 28 | 108 à 128 | 48 sur 48 | 2,8 × 10^-59 à 1,6 × 10^-42 | 114 s |

144 lectures suivies sur 144. Boîtes de 104 à 128.
La plus grande largeur du jumeau, 1,9 × 10^-35, est à plus de 20 décades sous la plus petite
largeur que la chaîne prédit pour le vide de 3 à 6 barreaux (7,1 × 10^-15).

### 2.2 Le procédé sur une barrière profonde

La routine déposée, à qui l'on donne la chaîne de la limite de l'état (0, 0) rangée dans une
« boîte » (les sites en trop sont découplés), sous l'absorbeur de la chaîne déposée. Référence :
la fraction continue en logarithme, contrôlée contre le pôle exact en précision arbitraire dans
la note « loi d'échelle ».

| barreaux | sites | ln Φ, fraction continue | ln Φ, routine du lecteur | écart | itérations |
|---|---|---|---|---|---|
| 4 | 49 | −19,432881 | −19,432881 | 6,8 × 10^-14 | 2 |
| 8 | 65 | −35,276798 | −35,276798 | 7,1 × 10^-15 | 2 |
| 16 | 129 | −67,889776 | −67,889776 | 0 | 2 |
| 32 | 257 | −134,113053 | −134,113053 | 0 | 2 |
| 64 | 513 | −267,616703 | −267,616703 | 5,7 × 10^-14 | 2 |
| 128 | 1025 | −535,715843 | −535,715843 | 1,1 × 10^-13 | 2 |

6 sur 6 lectures suivies. Plus grand écart : 1,1 × 10^-13. La double précision ne limite
donc pas ce procédé sur une chaîne. En 2D la factorisation n'a pas la même structure : ce
contrôle n'y vaut pas preuve.

### 2.3 L'absorbeur du lecteur convient-il au vide ? Un mandataire à une dimension

Aucune 2D. La chaîne du premier ordre du vide, à qui l'on donne l'absorbeur DU LECTEUR lu le long
de l'échelle (r = max(a, b) = 2 m), aux quatre absorbeurs et aux douze barreaux, puis la règle de
plateau de la feuille déposée. 6 cas (3, 4 et 5 barreaux, |delta| de 0,005 à 0,02).

- Avec la règle du dépôt, eta0 = |delta| : plateau à 24 séries sur 24. Dans les fenêtres retenues, la
  largeur est à 0,0063 au plus du plateau de l'absorbeur adapté. Les fenêtres retenues vont
  de k = −2 à +3 pour les absorbeurs F2 et de k = +1 à +6 pour F1. Au barreau le plus faible (k = 8),
  les absorbeurs F2 s'écartent de −1,65 à +0,93 : c'est la sous-absorption, hors
  des fenêtres.
- Avec une règle adaptée au saut (eta0 = saut au site r_c / 2) : plateau à 24 sur 24, mais à
  0,037 près seulement. Elle ne fait pas mieux ; je ne la propose pas.

Ce mandataire dit que la force de l'absorbeur du lecteur est du bon ordre pour le vide. Il ne dit
rien de la largeur 2D.

## 3. L'absorbeur de la chaîne

### 3.1 Le diagnostic

Règle déposée : W_m = ef |delta| (m − début)^2, ef = 0,0625. Largeur du vide, en logarithme,
rapportée à la loi d'échelle, quand ef varie seul :

| cas | ordre | ef = 0,000976562 | ef = 0,00390625 | ef = 0,015625 | ef = 0,0625 | ef = 0,25 | ef = 1 | ef = 4 | ef = 16 |
|---|---|---|---|---|---|---|---|---|---|
| vide, 3 barreaux, δ = −0,020 | 1 | −3,031 | −1,658 | −0,447 | −0,005 | +0,001 | −0,027 | −0,165 | −0,198 |
| vide, 3 barreaux, δ = −0,020 | 3 | −3,258 | −1,881 | −0,616 | −0,032 | −0,006 | −0,029 | −0,174 | −0,398 |
| vide, 4 barreaux, δ = +0,010 | 1 | −3,044 | −1,669 | −0,441 | +0,003 | +0,002 | −0,030 | −0,141 | +0,054 |
| vide, 4 barreaux, δ = +0,010 | 3 | −2,302 | −0,961 | −0,063 | +0,004 | −0,002 | −0,036 | −0,116 | +0,213 |
| vide, 5 barreaux, δ = +0,020 | 1 | −2,744 | −1,379 | −0,261 | +0,008 | +0,002 | −0,032 | −0,096 | +0,312 |
| vide, 5 barreaux, δ = +0,020 | 3 | −2,419 | −1,071 | −0,114 | −0,006 | −0,012 | −0,044 | −0,001 | +0,673 |

À ef = 0,000976562 la largeur du premier ordre est à −2,74 ou moins ; à
ef = 4 elle descend jusqu'à −0,17. Il n'y a pas de plateau large, et le
réglage déposé est au bord du côté faible : sa variante « ef divisé par deux » tombe dans la
pente. L'ordre 1 se comporte comme l'ordre 3 : ce n'est pas un défaut de l'ordre 3. La force de
l'absorbeur suit |delta|, les sauts suivent g m^(5/2) ; aux états joués les deux se trouvaient
du même ordre.

### 3.2 L'absorbeur adapté au saut

W_m = a |t_m| ((m − début) / L)^2 de début à début + L, début = m_bord + c, chaîne coupée à
début + L : l'absorption cumulée vaut a L / 6 quel que soit l'état. 18 variantes
(a = 1, 2, 4 ; c = 6, 8, 10 ; L = 16, 24) ; « plateau » : leur médiane ; « étendue » : max − min.
Les tables et les matrices d'ordre 2 et 3 sont celles des blocs déposés ; seuls l'absorbeur et la
longueur changent.

Le vide, |delta| = 0,005, 0,01 et 0,02, les deux signes. Phi* : la limite delta → 0 sous
l'absorbeur adapté. r3* = ln(Gamma_3* / |delta|) − ln Phi*.

| barreaux | κ | ln Φ* | Φ* − Φ déposée | forme fermée − Φ* | plus grand \|r3*\| | plus grand \|r3* − r2*\| | étendue d'ordre 3 : max | règle déposée − plateau : de ... à ... | Γ3* / \|δ\| |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 0,0363 | −11,928 | −0,020 | +0,068 | 0,012 | 0,0022 | 0,0360 | −0,150 à +0,020 | 6,6 × 10^-6 |
| 3 | 0,0262 | −15,605 | +0,013 | +0,050 | 0,013 | 0,0026 | 0,0041 | −0,033 à +0,057 | 1,7 × 10^-7 |
| 4 | 0,0200 | −19,425 | +0,007 | +0,039 | 0,019 | 0,0029 | 0,0049 | −0,023 à −0,002 | 3,7 × 10^-9 |
| 5 | 0,0159 | −23,325 | +0,003 | +0,033 | 0,026 | 0,0034 | 0,0065 | −0,004 à −0,001 | 7,4 × 10^-11 |
| 6 | 0,0130 | −27,275 | +0,002 | +0,028 | 0,034 | 0,0038 | 0,0077 | −0,003 à +0,001 | 1,4 × 10^-12 |

- De 3 à 6 barreaux, l'étendue d'ordre 3 vaut 0,0077 au plus. À 2 barreaux et
  |delta| = 0,02 elle monte à 0,036 : c'est le plus fort couplage de la table, et
  le début de la cause (b).
- Phi* s'écarte de la Phi de la note « loi d'échelle » (règle déposée) de −0,020 à
  +0,013 ; l'étendue de Phi* vaut 0,0050 au plus. La forme fermée à trois
  termes est à 0,028 à 0,068 de Phi*.
- La règle déposée s'écartait du plateau jusqu'à 0,15 : c'est l'instabilité que la
  note « loi d'échelle » voyait.
- Pour 10 cas d'états excités, Phi* − Phi va de −0,015 à +0,005,
  étendue 0,029 au plus.

## 4. Ce qui reste instable : les termes d'ordre 3 après la barrière

La carte de la note « loi d'échelle », rejouée sous l'absorbeur adapté pour ses points de 16
barreaux au plus : 118 points, 50 instables sous la règle déposée,
46 sous l'absorbeur adapté (dont 43 l'étaient déjà ; 7 sont
guéris, 3 le deviennent). Pour le vide, les 27 instables ont tous
|delta| ≥ 0,0375 ; pour (6, 2), les 19 ont |delta| ≥ 0,0625.

À 8 de ces points, par ordre :

| point | g | ordre 1 : r (étendue) | ordre 2 | ordre 3 | saut > 1 au site | t + T3 change de signe au site | fin de la plus longue variante |
|---|---|---|---|---|---|---|---|
| (0, 0), 4 barreaux, δ = −0,0375 | 6,37 × 10^-3 | −0,005 (0,003) | −0,047 (0,009) | −0,052 (0,489) | 14 | 24 | 38 |
| (0, 0), 4 barreaux, δ = −0,0750 | 1,10 × 10^-2 | −0,017 (0,003) | −0,201 (0,018) | +0,492 (1,662) | 11 | 16 | 38 |
| (0, 0), 6 barreaux, δ = −0,0500 | 5,25 × 10^-3 | −0,022 (0,005) | −0,150 (0,009) | −0,160 (0,548) | 15 | 25 | 40 |
| (0, 0), 8 barreaux, δ = −0,0625 | 4,47 × 10^-3 | −0,039 (0,006) | −0,315 (0,007) | −0,311 (0,806) | 16 | 25 | 42 |
| (6, 2), 4 barreaux, δ = +0,0750 | 6,88 × 10^-3 | −0,025 (0,009) | −0,578 (0,005) | −0,642 (0,218) | 13 | aucun | 39 |
| (6, 2), 6 barreaux, δ = +0,0833 | 6,52 × 10^-3 | −0,029 (0,009) | −0,764 (0,007) | −0,821 (0,403) | 14 | aucun | 41 |
| (6, 2), 8 barreaux, δ = −0,0875 | 3,01 × 10^-3 | +0,028 (0,019) | +0,180 (0,006) | +0,047 (0,879) | 15 | 25 | 41 |
| (0, 0), 12 barreaux, δ = −0,0833 | 3,30 × 10^-3 | −0,082 (0,012) | −0,847 (0,008) | −0,823 (1,788) | 17 | 27 | 45 |

Les ordres 1 et 2 y sont stables (étendue 0,019 au plus) ; l'ordre 3 bouge de
0,22 à 1,79. À 6 sur 8 de ces points le saut corrigé t + T3 change de
signe à l'intérieur de la chaîne : le terme d'ordre 3, en t^3, y dépasse le saut. Là, la lecture
de la note « loi d'échelle » tenait.

Essai, NÉGATIF : couper net les termes d'ordre 3 au-delà du premier site où le saut dépasse un
seuil t_s, ordre 2 au-delà.

| cas | m_bord | t_s = 0,15 : m_s, r | t_s = 0,30 | t_s = 0,50 | écart entre les trois | sans coupure : r (étendue) | 2D lue | déposée |
|---|---|---|---|---|---|---|---|---|
| (0, 0), 4 barreaux, δ = −0,0375 | 4 | 6, −0,059 | 9, −0,054 | 11, +0,003 | 0,062 | −0,052 (0,489) | — | — |
| (0, 0), 4 barreaux, δ = −0,0750 | 4 | 5, −0,170 | 6, −0,225 | 8, −0,080 | 0,145 | +0,492 (1,662) | — | — |
| (0, 0), 6 barreaux, δ = −0,0500 | 6 | 7, −0,134 | 9, −0,177 | 11, −0,130 | 0,046 | −0,160 (0,548) | — | — |
| (0, 0), 8 barreaux, δ = −0,0625 | 8 | 8, −0,228 | 9, −0,259 | 12, −0,249 | 0,031 | −0,311 (0,806) | — | — |
| (6, 2), 4 barreaux, δ = +0,0750 | 5 | 5, −0,598 | 7, −0,632 | 9, −0,650 | 0,052 | −0,642 (0,218) | — | — |
| (6, 2), 6 barreaux, δ = +0,0833 | 7 | 7, −0,789 | 7, −0,789 | 10, −0,807 | 0,018 | −0,821 (0,403) | — | — |
| (6, 2), 8 barreaux, δ = −0,0875 | 7 | 7, +0,187 | 8, +0,160 | 10, −0,022 | 0,209 | +0,047 (0,879) | — | — |
| (0, 0), 12 barreaux, δ = −0,0833 | 11 | 11, −0,359 | 11, −0,359 | 13, −0,511 | 0,152 | −0,823 (1,788) | — | — |
| (0, 0), 4 barreaux, δ = −0,0188 | 4 | 9, −0,009 | 11, +0,002 | 14, −0,011 | 0,013 | −0,010 (0,001) | — | — |
| (6, 2), 8 barreaux, δ = −0,0375 | 8 | 9, +0,150 | 12, +0,124 | 16, +0,135 | 0,026 | +0,135 (0,008) | — | — |
| joué N1 rang 0, (9, 3), δ = −0,065 | 9 | 9, +0,321 | 10, +0,291 | 13, +0,108 | 0,213 | +0,185 (0,022) | +0,253 | +0,201 |
| joué BP rang 3, (8, 1), δ = +0,067 | 9 | 9, −0,796 | 9, −0,796 | 12, −0,791 | 0,005 | −0,802 (0,054) | −0,892 | −0,793 |
| joué P1 rang 0, (9, 2), δ = +0,035 | 11 | 11, −0,402 | 14, −0,410 | 19, −0,405 | 0,008 | −0,410 (0,016) | −0,429 | −0,413 |
| joué C1 rang 0, (10, 3), δ = −0,030 | 10 | 11, +0,230 | 16, +0,217 | 21, +0,217 | 0,013 | +0,210 (0,026) | +0,221 | +0,213 |

Chaque coupure donne une largeur stable sous l'absorbeur (étendue 0,029 au plus), mais
la largeur dépend du site de coupure : de 0,21 à l'état joué N1 rang 0, contre 0,013
au plus aux trois autres états joués. Les termes d'ordre 3 juste après la barrière font donc
partie du calcul, au moins à delta < 0 ; une coupure nette n'est pas une règle. Je ne propose
rien pour la cause (b). Elle ne touche pas le vide à |delta| ≤ 0,02.

## 5. Les états déjà joués sous l'absorbeur adapté (après coup)

Les 185 états du domaine des deltas 98 et 100. Même chaîne d'ordre 3, absorbeur adapté.

- Étendue sous les variantes : médiane 0,021, neuvième décile 0,064, plus grande
  0,33. Pour ces états l'absorbeur adapté n'a pas le plateau net qu'il a pour le vide.
- ln(G3 adapté / G3 déposé) : médiane −0,0094, de −0,023 à +0,005 ; négatif à
  168 états sur 185.
- |ln q3| : médiane 0,0192 (déposé) et 0,0159 (adapté) ; pire 0,0996
  et 0,0902. Hors des tolérances rappelées de E1 : 0 et 0.
- L'adapté est plus près de la 2D à 78 états sur 185 : 71 sur 81 à delta > 0, 7 sur 104
  à delta < 0. Ce n'est pas un gain : il abaisse l'ordre 3 d'un pour cent presque partout, ce qui
  rapproche là où la chaîne était trop haute et éloigne là où elle était trop basse (à la cellule
  P1 le pire |ln q3| passe de 0,0336 à 0,0190, à N2 de 0,0427 à 0,0551).
  Les deux règles diffèrent de moins que l'étendue de chacune à 153 états sur 185 (étendue
  médiane de la règle déposée sur ces états : 0,0126), et l'écart médian de la chaîne à
  la 2D, 0,0192, est du même ordre.

| pièce | id | δ | états | étendue max | adapté − déposé : min ; médiane ; max | \|ln q3\| max, déposé | \|ln q3\| max, adapté |
|---|---|---|---|---|---|---|---|
| delta 98 | M2 | −0,080 | 7 | 0,329 | −0,016 ; −0,005 ; −0,004 | 0,0220 | 0,0333 |
| delta 100 | BN | −0,076 | 7 | 0,136 | −0,020 ; −0,010 ; −0,006 | 0,0461 | 0,0520 |
| delta 98 | M1 | −0,070 | 11 | 0,073 | −0,018 ; −0,006 ; −0,002 | 0,0431 | 0,0446 |
| delta 100 | N1 | −0,065 | 11 | 0,026 | −0,020 ; −0,018 ; +0,003 | 0,0740 | 0,0706 |
| delta 100 | N2 | −0,065 | 11 | 0,023 | −0,019 ; −0,013 ; −0,008 | 0,0427 | 0,0551 |
| delta 100 | N3 | −0,065 | 11 | 0,037 | −0,018 ; −0,006 ; +0,001 | 0,0355 | 0,0354 |
| delta 100 | N4 | −0,065 | 14 | 0,042 | −0,010 ; −0,005 ; −0,000 | 0,0208 | 0,0214 |
| delta 100 | N5 | −0,065 | 13 | 0,064 | −0,015 ; −0,003 ; −0,000 | 0,0157 | 0,0157 |
| delta 98 | C2 | −0,060 | 11 | 0,025 | −0,019 ; −0,017 ; +0,004 | 0,0604 | 0,0568 |
| delta 98 | C1 | −0,030 | 8 | 0,027 | −0,019 ; −0,008 ; +0,005 | 0,0143 | 0,0119 |
| delta 98 | C3 | +0,030 | 14 | 0,011 | −0,012 ; −0,006 ; +0,002 | 0,0133 | 0,0032 |
| delta 100 | P1 | +0,035 | 9 | 0,032 | −0,021 ; −0,001 ; +0,003 | 0,0336 | 0,0190 |
| delta 100 | P2 | +0,035 | 10 | 0,029 | −0,019 ; −0,011 ; +0,001 | 0,0302 | 0,0150 |
| delta 100 | P3 | +0,035 | 12 | 0,022 | −0,017 ; −0,008 ; −0,001 | 0,0219 | 0,0105 |
| delta 100 | P4 | +0,035 | 13 | 0,023 | −0,020 ; −0,011 ; −0,000 | 0,0217 | 0,0085 |
| delta 100 | P5 | +0,035 | 13 | 0,021 | −0,018 ; −0,009 ; +0,001 | 0,0201 | 0,0066 |
| delta 98 | C4 | +0,060 | 5 | 0,050 | −0,022 ; −0,022 ; −0,011 | 0,0415 | 0,0300 |
| delta 100 | BP | +0,067 | 5 | 0,054 | −0,023 ; −0,010 ; −0,009 | 0,0996 | 0,0902 |

Ce n'est pas un rejeu du gel du delta 100 et cela ne change aucun de ses verdicts.

## 6. Une ligne profonde

Le vide à 8, 12 et 16 barreaux, |delta| ≤ 0,02, sous l'absorbeur adapté (six variantes) :

| barreaux | δ | ln Φ* | r3* | étendue | Γ3* / \|δ\| | Γ3* |
|---|---|---|---|---|---|---|
| 8 | −0,0188 | −35,28 | −0,045 | 0,0053 | 4,6 × 10^-16 | 8,6 × 10^-18 |
| 8 | −0,0094 | −35,28 | −0,017 | 0,0061 | 4,7 × 10^-16 | 4,4 × 10^-18 |
| 8 | +0,0094 | −35,28 | +0,006 | 0,0078 | 4,8 × 10^-16 | 4,5 × 10^-18 |
| 8 | +0,0187 | −35,28 | +0,001 | 0,0085 | 4,8 × 10^-16 | 9,0 × 10^-18 |
| 12 | −0,0125 | −51,50 | −0,043 | 0,0035 | 4,1 × 10^-23 | 5,1 × 10^-25 |
| 12 | −0,0063 | −51,50 | −0,018 | 0,0040 | 4,2 × 10^-23 | 2,6 × 10^-25 |
| 12 | +0,0063 | −51,50 | +0,012 | 0,0048 | 4,3 × 10^-23 | 2,7 × 10^-25 |
| 12 | +0,0125 | −51,50 | +0,016 | 0,0055 | 4,4 × 10^-23 | 5,5 × 10^-25 |
| 16 | −0,0188 | −67,89 | −0,107 | 0,0043 | 2,9 × 10^-30 | 5,5 × 10^-32 |
| 16 | −0,0094 | −67,89 | −0,044 | 0,0050 | 3,1 × 10^-30 | 2,9 × 10^-32 |
| 16 | −0,0047 | −67,89 | −0,019 | 0,0047 | 3,2 × 10^-30 | 1,5 × 10^-32 |
| 16 | +0,0047 | −67,89 | +0,014 | 0,0018 | 3,3 × 10^-30 | 1,6 × 10^-32 |
| 16 | +0,0094 | −67,89 | +0,023 | 0,0020 | 3,4 × 10^-30 | 3,1 × 10^-32 |
| 16 | +0,0187 | −67,89 | +0,027 | 0,0027 | 3,4 × 10^-30 | 6,3 × 10^-32 |

14 points, étendue 0,0085 au plus, |r3*| 0,107 au plus. Le jumeau
sans fantôme lit bien plus bas que ces largeurs (section 2.1), et la routine lit juste sur une
chaîne à ces profondeurs (section 2.2). Ce qui manque : savoir si elle lit juste en 2D. Un gel
peut le laisser décider par la qualification en cours de run (plateau, accords entre
absorbeurs), en branche non létale.

## 7. Ce qu'un gel du vide jugerait (proposition ; rien n'est décidé)

- Objet. La largeur de plateau de l'état porté par (0, 0), lue par le lecteur creux, qualifiée
  dans le run.
- Énoncé V1, ligne lisible. À des cellules tirées (barrière de 3 à 6 barreaux, |delta| ≤ 0,02,
  les deux signes), la chaîne d'ordre 3 sous absorbeur adapté rend cette largeur dans une
  tolérance gelée. Les largeurs prédites vont de 3,3 × 10^-9 à 7,1 × 10^-15, pour des
  couplages de 6,2 × 10^-4 à 5,5 × 10^-3.
- Énoncé V2. La forme fermée à trois termes la rend aussi, dans une tolérance plus large (elle
  est à 0,028 à 0,068 de Phi*).
- Énoncé V3, ligne profonde, non létal. À 8 barreaux et plus, là où le lecteur qualifie.
- Instrument. La sonde dérivée et sa feuille (section 1) ; le bloc d'absorbeur adapté pour la
  chaîne ; les témoins : le jumeau sans fantôme à la géométrie de chaque cellule, les ancres du
  dépôt, le témoin positif.
- À décider au gel, pas ici : la règle de tirage et la graine ; les tolérances (la règle de
  plateau du lecteur est à 5 pour cent ; E1 prenait 0,05 pour e_bord < 0,3) ; le nombre de
  cellules ; ce qu'on fait d'un état non qualifié ; les annonces de la plume.

Mon avis : le faire, avec la ligne profonde. C'est le premier énoncé de la campagne sur l'objet
qu'un lecteur extérieur nomme, et il est peu coûteux à jouer.

## 8. Limites, et défauts de ma plume

- L-1. Aucune largeur 2D du vide n'existe. Que le lecteur la lise, et la lise juste, est appuyé
  par trois faits indirects (jumeau, procédé sur une chaîne, mandataire) ; aucun n'est une lecture.
- L-2. L'absorbeur adapté est une règle d'aujourd'hui, d'une plume, non certifiée. Son étendue
  mesure sa stabilité, pas l'erreur de la chaîne.
- L-3. Le mandataire est une chaîne du premier ordre : rien de ce qui est propre à la 2D n'y est.
- L-4. La cause (b) reste ouverte. Le prédicteur du vide n'est établi qu'à |delta| ≤ 0,02.
- L-5. La comparaison aux états joués est après coup.
- L-6. Une seule forme de hamiltonien effectif ; un seul état, (0, 0).

Défauts, tous dans la note « loi d'échelle » (8548cc16fb746f56), qui n'est pas modifiée :

- D-VIDE-1. Sa section 6 lisait l'instabilité comme celle des termes d'ordre 3 après la
  barrière, et y voyait une raison de regarder la forme à énergie fixée. Pour le vide à petit
  désaccord c'est faux : c'est l'absorbeur, et l'ordre 1 le montre. La lecture ne tient qu'à
  désaccord plus grand (section 4).
- D-VIDE-2. Son verdict 4 disait qu'aucun lecteur 2D en double précision ne lirait le régime
  profond. Retiré (section 2.2).
- D-VIDE-3. Sa section 7 comparait le vide à « la plus petite largeur de plateau de ces deux
  runs » comme à une limite du lecteur. Cette limite est le seuil de la sonde dense.
- D-VIDE-4. Sa section 7 concluait que le meilleur prédicteur du vide était la loi d'échelle,
  avec une tolérance portant l'instabilité. C'est la chaîne d'ordre 3 sous absorbeur adapté.
- D-VIDE-5. Ses valeurs de Phi pour le vide à barrière courte portent l'absorbeur déposé :
  elles sont à −0,020 à +0,013 du plateau (section 3.2).

## 9. Pièces (convention B)

Au registre (dee73bd), lues :

    82a0be882568fe0c  scripts/m17_chaine_v17.py
    7cd5977bc27bebc1  scripts/chaine_ordre2_bloc_machine1_v1.py
    534ba246aa3b8973  scripts/ordre3_bloc_machine1_v1.py
    d5cc48f48e37af99  scripts/sonde_lecteur_gel_loi_machine1_v1.py
    68baf04c73ed5d44  scripts/sonde_dense_gel_loi_machine1_v1.py
    b2d6d7cfaf30f1cf  scripts/lecture_qualification_EB_ter_machine1_v1.py

Du lot de la note « loi d'échelle » (408b8a595cad0040), reprises telles quelles :

    8859a0c49b854d6f  phi_echelle_machine1_v1.py
    6abf1d8b59bf41dc  carte_machine1_v1.py
    406f13baa939eded  carte_v1.json
    aeb9fc40ecc43899  superposition_v1.json
    2e2ed5b9b745790c  forme_phi_v1.json
    9ea4bc086f5768a2  canon_fichiers_v1.py

De ce lot :

    f5dece5de40e95bd  absorbeur_adapte_machine1_v1.py
    32d2025510772c57  absorbeur_adapte_machine1_v1.log
    75e7e0259b1be1d4  absorbeur_adapte_v1.json
    fbb265a397264107  controle_joues_absorbeur_machine1_v1.py
    4c8147d15296d25f  controle_joues_absorbeur_machine1_v1.log
    1d54b893ce452a98  controle_joues_absorbeur_v1.json
    aafa9250d5e29af1  carte_adaptee_machine1_v1.py
    9b458140e1b4d1f3  carte_adaptee_machine1_v1.log
    a2b653fdc9e44dce  carte_adaptee_v1.json
    8cab41eacb52a59e  apres_barriere_machine1_v1.py
    396462e9ae1b895b  apres_barriere_machine1_v1.log
    4151fbd94fe1682a  apres_barriere_v1.json
    2f2ad0871b591791  temoin_lecteur_vide_machine1_v1.py
    a57cf1dedefe07ba  temoin_lecteur_vide_machine1_v1.log
    ce4ba267f1e6a4bc  temoin_lecteur_vide_v1.json
    77612d9494d610f7  procede_lecteur_profond_machine1_v1.py
    f3aca9f123c1788b  procede_lecteur_profond_machine1_v1.log
    77fafabcececc9ab  procede_lecteur_profond_v1.json
    8c75dcf10654bc46  mandataire_absorbeur_2D_machine1_v1.py
    bf202788797f5dd6  mandataire_absorbeur_2D_machine1_v1.log
    f03c9608aa612176  mandataire_absorbeur_2D_v1.json
    (ce script)       construction_note_vide_machine1_v1.py, gabarit_note_vide_machine1_v1.md
