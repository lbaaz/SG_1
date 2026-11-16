# Note hors chaîne : la carte du gel de la loi (chaîne seule)

Plume : machine 1. Date : 15/11/2026, nuit. Statut : exploration hors chaîne, non certifiée, non
rejouée par machine 2. Elle ne tranche rien, ne modifie aucune pièce citée, n'ouvre aucun gel et
ne choisit aucun point. Ouverture, selon machine 1 : l'opérateur a écrit « ouvre » (15/11/2026,
21 h 54), après la question « Il faut geler ? » (20 h 52).

Aucun calcul 2D : ni par la sonde dense, ni par le lecteur creux, à aucune cellule. Ce qui est
calculé : des chaînes à une dimension (moteur 82a0be882568fe0c, bloc d'ordre 2 déposé
7cd5977bc27bebc1, bloc d'ordre 3 de la note du 15/11 534ba246aa3b8973) et les règles écrites du
gel du delta 98 (41153158190cf7f1, section 3) pour la graine et la boîte. Suite de la note sur
la loi (84fce9a6faf99c5b, lot e93f1898dcd78a8f), dont c'est l'étape 4.

## 0. Verdict

1. Un gel est jouable. Sur 242 cellules (désaccord de −0,12 à +0,12, facteur sur le couplage de
   1/2 à 2), 81 passent la règle proposée en section 5 : 45 à delta < 0, 36 à delta > 0. Toutes
   sont à |delta| ≤ 0,08 côté négatif et ≤ 0,07 côté positif. À partir de |delta| = 0,09, aucune
   cellule n'a cinq états dans le domaine de l'ordre 3.
2. Le balayage en couplage est possible, et large. Ma crainte d'une fenêtre étroite était
   infondée dans le domaine : pour |delta| ≤ 0,06, à w2 fixé, de 11 à 22 étiquettes restent
   lisibles et dans le domaine à trois facteurs ou plus, et la meilleure y parcourt de 6,2 à 6,6
   décades de largeur prédite pour un couplage multiplié par 1,6.
3. Fait nouveau : « l'ordre 3 fait mieux que l'ordre 2 » ne se juge que du côté négatif. Les
   deux ordres ne diffèrent de plus de 5 pour cent, pour cinq états au moins, qu'à 31 cellules,
   toutes entre delta = −0,04 et −0,08 ; à aucune cellule de delta > 0, où leur écart médian ne
   dépasse pas 0,040. Au seuil de 2 pour cent : 50 cellules côté négatif, 17 côté positif.
4. Ce que vaut la carte comme prédiction, aux seize points déjà joués : boîte, graine et
   couplage identiques à 16 points sur 16 ; 189 étiquettes lues sur 224 sont parmi les quatorze
   prédites ; le passage du plancher est bien prédit pour 214 états sur 224.
5. L'instrument d'un tel gel a deux étages, déjà certifiés l'un et l'autre : la sonde dense du
   delta 98, qui trouve les états, puis le lecteur du gel ter, qui lit leur largeur de plateau à
   partir de la sortie de la première. Leur méthode ne change pas ; deux retouches sont à
   certifier : la table des points de la sonde dense, et la sortie que lit le lecteur, qui sera
   produite par le run lui-même.
6. Mon avis : geler deux lignes de balayage en couplage, une de chaque côté de 2,00, et quelques
   cellules de bord. Section 5 ; rien n'y est décidé.

## 1. Ce que la carte calcule

Une cellule est un couple (w2, facteur). Le point que la sonde dense y jouerait est construit
par les fonctions du moteur et la règle du gel du delta 98 : g = facteur × g_du_point(w2), s =
0,70 s_ff, graine, barrière à la graine, r_c, boîte N = r_c + 20. Les états ne sont pas lus :
les étiquettes (n1, n2) sont PRÉDITES, ce sont les quatorze de plus grand poids de la graine
cohérente (poids de Poisson). Pour chacune, la chaîne donne trois largeurs (moteur, ordre 2,
ordre 3), leur stabilité et le désaccord au bout de la barrière, e_bord.

Un état est dit JUGEABLE si sa barrière n'est pas vide, si les chaînes du moteur et d'ordre 2
sont stables (critères 7, 8 et 11 du gel du delta 98) et si sa largeur prédite dépasse dix
planchers (1,33e-12). Il est DANS LE DOMAINE si de plus e_bord < 0,7 et si la chaîne d'ordre 3
est stable à 0,05 près sous son absorbeur (les deux gardes de la note sur la loi). Il est
DISCRIMINANT si de plus les largeurs d'ordre 2 et d'ordre 3 diffèrent de plus de 5 pour cent
(|ln| ≥ 0,05). Les critères du gel qui demandent la 2D (J net, site majoritaire, suivi, cible
stable) ne sont pas prédits.

## 2. La carte comme prédiction, aux seize points déjà joués

| point | boîte, graine, couplage | étiquettes lues parmi les 14 prédites | parmi les 16 | états jugés au delta 98 | plancher bien prédit |
|---|---|---|---|---|---|
| A1 | identiques | 12 sur 14 | 13 | 11 | 13 sur 14 |
| A2 | identiques | 12 sur 14 | 13 | 12 | 14 sur 14 |
| C1 | identiques | 13 sur 14 | 14 | 8 | 14 sur 14 |
| C2 | identiques | 13 sur 14 | 13 | 11 | 14 sur 14 |
| C3 | identiques | 12 sur 14 | 12 | 14 | 14 sur 14 |
| C4 | identiques | 12 sur 14 | 14 | 13 | 14 sur 14 |
| L1 | identiques | 14 sur 14 | 14 | 14 | 14 sur 14 |
| L2 | identiques | 13 sur 14 | 14 | 10 | 14 sur 14 |
| L3 | identiques | 11 sur 14 | 12 | 12 | 12 sur 14 |
| L4 | identiques | 10 sur 14 | 11 | 9 | 13 sur 14 |
| M1 | identiques | 13 sur 14 | 13 | 11 | 13 sur 14 |
| M2 | identiques | 13 sur 14 | 13 | 13 | 13 sur 14 |
| M3 | identiques | 11 sur 14 | 12 | 8 | 14 sur 14 |
| M4 | identiques | 10 sur 14 | 10 | 9 | 12 sur 14 |
| W1 | identiques | 11 sur 14 | 13 | 11 | 13 sur 14 |
| W2 | identiques | 9 sur 14 | 9 | 3 | 13 sur 14 |

Total : 189 étiquettes sur 224 parmi les quatorze prédites (200 parmi les seize). Le plancher
est prédit à tort au-dessus pour 5 états et à tort au-dessous pour 5. La carte se trompe donc
d'un à quatre états par point sur QUI sera lu ; elle ne se trompe pas sur la boîte. Les points
les moins bien prédits sont les plus éloignés ou les plus faiblement couplés (M4, L4, W2).

## 3. La grille

Par cellule : états jugeables / dans le domaine / discriminants à 5 pour cent. Une étoile marque
une cellule éligible à la règle proposée (section 5) ; « j » un couple déjà joué. Boîtes, e_bord
et largeurs prédites : journal de lecture, tables (B1), (B3), (B4).

| delta | 1/2 | 3/5 | 2/3 | 3/4 | 5/6 | 1 | 6/5 | 4/3 | 3/2 | 5/3 | 2 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| -0,12 | 2/0/0 | 4/0/0 | 6/0/0 | 9/0/0 | 9/0/0 | 10/0/0 j | 13/0/0 | 14/0/0 | 14/0/0 | 13/0/0 | 13/0/0 |
| -0,11 | 2/0/0 | 4/0/0 | 6/0/0 | 9/0/0 | 9/0/0 | 11/0/0 j | 13/0/0 | 14/0/0 j | 14/0/0 | 13/0/0 | 13/0/0 |
| -0,10 | 2/0/0 | 4/0/0 | 6/0/0 j | 9/0/0 | 9/0/0 | 11/1/1 j | 13/0/0 | 14/1/1 | 14/0/0 j | 13/0/0 | 12/0/0 |
| -0,09 | 2/0/0 | 5/0/0 | 6/0/0 j | 9/1/1 | 9/3/3 | 11/3/3 j | 13/0/0 | 14/1/1 | 14/1/1 | 13/0/0 | 12/1/1 |
| -0,08 | 3/0/0 | 5/1/1 | 6/3/3 | 10/4/4 | 9/4/4 | 11/6/6* | 13/5/5* | 14/7/7 j | 14/5/5* | 13/3/3 | 12/1/1 |
| -0,07 | 3/0/0 | 6/3/3 | 7/7/7 | 10/10/10* | 9/9/9* | 12/12/12 j | 13/13/13* | 14/13/13* | 13/11/11* | 13/9/9* | 12/7/3* |
| -0,06 | 4/4/4 | 6/6/6 | 7/7/7 | 11/11/11 j | 10/10/10* | 12/12/12* | 13/13/13* | 14/14/14* | 13/13/12* | 13/6/1* | 12/6/1* |
| -0,05 | 5/5/5 | 6/6/6 | 7/7/7 j | 11/11/11* | 10/10/10* | 12/12/12 j | 14/14/6* | 14/14/0* | 12/12/0 j | 13/13/0* | 12/11/0* |
| -0,04 | 5/5/5 | 7/7/7 | 7/7/7 | 11/11/9* | 10/10/1* | 12/12/0 j | 14/14/0* | 13/13/0* | 12/12/0* | 12/12/0* | 12/12/0* |
| -0,03 | 5/5/0 | 7/7/0 | 8/8/0 j | 11/11/0* | 10/10/0* | 12/12/0 j | 13/13/0* | 12/12/0* | 12/12/0* | 12/12/0* | 12/12/0* |
| -0,02 | 5/5/0 | 6/6/0 | 8/8/0* | 11/11/0* | 10/10/0* | 12/12/0 j | 12/12/0* | 12/12/0* | 11/11/0* | 11/11/0* | 12/12/0* |
| +0,02 | 6/6/0 | 6/6/0 | 10/10/0* | 10/10/0* | 12/12/0* | 13/13/0 j | 13/13/0* | 12/12/0* | 12/12/0* | 10/10/0* | 11/11/0* |
| +0,03 | 8/8/0 | 6/6/0 | 10/10/0* | 12/12/0* | 12/12/0* | 13/13/0 j | 13/13/0* | 12/12/0* | 12/12/0 j | 10/10/0* | 11/11/0* |
| +0,04 | 8/8/0 | 9/9/0 | 10/10/0* | 12/12/0* | 13/13/0* | 13/13/0 j | 13/13/0* | 13/13/0* | 11/11/0* | 10/7/0* | 11/4/0 |
| +0,05 | 9/9/0 | 9/9/0 | 10/10/0 j | 12/12/0* | 13/13/0* | 14/14/0 j | 13/12/0* | 12/8/0* | 11/6/0 j | 10/5/0* | 10/2/0 |
| +0,06 | 9/1/1 | 9/4/0 | 11/10/0* | 13/13/0* | 13/10/0* | 14/9/0* | 13/8/0* | 12/5/0 j | 11/7/0* | 10/0/0 | 10/3/0 |
| +0,07 | 9/0/0 | 10/1/0 | 11/2/0 j | 13/6/0* | 13/6/0* | 14/7/0* | 13/4/0 | 12/2/1 | 11/0/0 | 10/0/0 | 10/1/0 |
| +0,08 | 9/0/0 | 10/0/0 | 11/1/1 j | 13/0/0 | 13/4/0 | 14/2/0 j | 12/0/0 | 12/0/0 | 10/0/0 | 10/2/0 | 10/0/0 |
| +0,09 | 9/0/0 j | 9/0/0 | 11/0/0 | 13/1/1 | 13/1/0 | 14/2/0 j | 12/0/0 | 12/3/1 | 10/0/0 | 10/0/0 | 10/0/0 |
| +0,10 | 9/0/0 | 9/0/0 | 12/0/0 j | 13/0/0 j | 13/0/0 | 14/0/0 j | 12/2/0 | 11/0/0 | 10/0/0 j | 10/0/0 | 10/0/0 |
| +0,11 | 8/0/0 | 10/0/0 | 12/0/0 | 13/0/0 | 13/0/0 | 14/0/0 | 12/0/0 | 11/0/0 | 10/0/0 j | 11/0/0 | 10/0/0 |
| +0,12 | 9/0/0 | 10/0/0 | 12/0/0 j | 12/0/0 | 14/0/0 | 14/0/0 j | 12/0/0 | 11/0/0 | 10/0/0 j | 10/0/0 | 10/0/0 |

Écart médian entre les deux ordres, |ln(ordre 2 / ordre 3)|, sur les états du domaine (tiret :
aucun) :

| delta | 1/2 | 3/5 | 2/3 | 3/4 | 5/6 | 1 | 6/5 | 4/3 | 3/2 | 5/3 | 2 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| -0,09 | — | — | — | 0,293 | 0,261 | 0,208 | — | 0,133 | 0,094 | — | 0,081 |
| -0,08 | — | 0,319 | 0,279 | 0,233 | 0,199 | 0,155 | 0,118 | 0,105 | 0,088 | 0,078 | 0,071 |
| -0,07 | — | 0,243 | 0,209 | 0,178 | 0,155 | 0,122 | 0,097 | 0,084 | 0,073 | 0,064 | 0,047 |
| -0,06 | 0,231 | 0,175 | 0,148 | 0,128 | 0,110 | 0,090 | 0,072 | 0,063 | 0,055 | 0,048 | 0,042 |
| -0,05 | 0,149 | 0,115 | 0,098 | 0,086 | 0,075 | 0,062 | 0,050 | 0,045 | 0,039 | 0,036 | 0,030 |
| -0,04 | 0,088 | 0,068 | 0,060 | 0,053 | 0,046 | 0,038 | 0,032 | 0,028 | 0,025 | 0,023 | 0,020 |
| -0,03 | 0,045 | 0,035 | 0,032 | 0,028 | 0,024 | 0,021 | 0,017 | 0,016 | 0,014 | 0,013 | 0,011 |
| -0,02 | 0,018 | 0,014 | 0,013 | 0,011 | 0,010 | 0,009 | 0,007 | 0,007 | 0,006 | 0,006 | 0,005 |
| +0,02 | 0,006 | 0,007 | 0,007 | 0,007 | 0,007 | 0,007 | 0,006 | 0,006 | 0,006 | 0,006 | 0,005 |
| +0,03 | 0,007 | 0,011 | 0,012 | 0,013 | 0,014 | 0,014 | 0,014 | 0,013 | 0,013 | 0,012 | 0,011 |
| +0,04 | 0,004 | 0,007 | 0,013 | 0,017 | 0,019 | 0,021 | 0,022 | 0,022 | 0,021 | 0,022 | 0,024 |
| +0,05 | 0,033 | 0,008 | 0,005 | 0,015 | 0,021 | 0,028 | 0,031 | 0,031 | 0,030 | 0,032 | 0,027 |
| +0,06 | 0,059 | 0,028 | 0,015 | 0,009 | 0,021 | 0,033 | 0,039 | 0,040 | 0,040 | — | 0,047 |
| +0,07 | — | 0,050 | 0,031 | 0,009 | 0,013 | 0,034 | 0,043 | 0,045 | — | — | 0,036 |
| +0,08 | — | — | 0,059 | — | 0,016 | 0,030 | — | — | — | 0,041 | — |
| +0,09 | — | — | — | 0,056 | 0,016 | 0,024 | — | 0,049 | — | — | — |

Trois lectures. (i) Le domaine s'arrête à |delta| = 0,08 côté négatif et 0,07 côté positif (cinq
états au moins) : c'est e_bord, qui vaut à facteur 1 de 6,9 à 9,4 fois |delta|. (ii) Côté
négatif, l'écart entre les deux ordres croît comme delta^2 : à facteur 1 il vaut de 22,5 à 25,0
fois delta^2 entre −0,08 et −0,02. Côté positif il plafonne (0,021 à +0,04, 0,034 à +0,07) et
vaut de 1,8 à 3,6 fois moins qu'au désaccord opposé : c'est ce qui rend ce côté non
discriminant. (iii) Dans le domaine, l'ordre 2 est au-dessus de l'ordre 3 pour 701 états sur 701
côté négatif et 505 sur 564 côté positif.

## 4. Les balayages en couplage

À w2 fixé, une étiquette n'est lue que tant qu'elle reste parmi les quatorze de la graine, qui
se déplace avec le couplage. Compte, par désaccord, des étiquettes qui restent dans le domaine à
plusieurs facteurs (boîte ≤ 74) :

| delta | à 2 facteurs ou plus | à 3 ou plus | la plus étendue | facteurs | couplage × | décades prédites | pente moyenne |
|---|---|---|---|---|---|---|---|
| -0,12 | 0 | 0 | — | — | — | — | — |
| -0,11 | 0 | 0 | — | — | — | — | — |
| -0,10 | 0 | 0 | — | — | — | — | — |
| -0,09 | 1 | 0 | (9, 3) | 5/6 ; 1 | 1,20 | 2,6 | 32,3 |
| -0,08 | 12 | 4 | (6, 1) | 6/5 ; 5/3 ; 2 | 1,67 | 5,4 | 24,3 |
| -0,07 | 25 | 17 | (8, 3) | 3/4 ; 5/6 ; 1 ; 6/5 | 1,60 | 6,6 | 32,4 |
| -0,06 | 25 | 18 | (8, 3) | 3/4 ; 5/6 ; 1 ; 6/5 | 1,60 | 6,6 | 32,3 |
| -0,05 | 29 | 19 | (8, 3) | 3/4 ; 5/6 ; 1 ; 6/5 | 1,60 | 6,6 | 32,2 |
| -0,04 | 28 | 20 | (8, 3) | 3/4 ; 5/6 ; 1 ; 6/5 | 1,60 | 6,6 | 32,2 |
| -0,03 | 27 | 21 | (8, 3) | 3/4 ; 5/6 ; 1 ; 6/5 | 1,60 | 6,6 | 32,1 |
| -0,02 | 27 | 20 | (8, 3) | 3/4 ; 5/6 ; 1 ; 6/5 | 1,60 | 6,6 | 32,1 |
| +0,02 | 29 | 22 | (7, 3) | 5/6 ; 1 ; 6/5 ; 4/3 | 1,60 | 6,2 | 30,4 |
| +0,03 | 29 | 22 | (8, 3) | 3/4 ; 5/6 ; 1 ; 6/5 | 1,60 | 6,6 | 32,3 |
| +0,04 | 27 | 22 | (8, 3) | 3/4 ; 5/6 ; 1 ; 6/5 | 1,60 | 6,6 | 32,3 |
| +0,05 | 22 | 20 | (8, 3) | 3/4 ; 5/6 ; 1 ; 6/5 | 1,60 | 6,6 | 32,4 |
| +0,06 | 20 | 11 | (8, 3) | 3/4 ; 5/6 ; 1 ; 6/5 | 1,60 | 6,6 | 32,4 |
| +0,07 | 6 | 0 | (10, 3) | 5/6 ; 1 | 1,20 | 2,4 | 30,4 |
| +0,08 | 0 | 0 | — | — | — | — | — |
| +0,09 | 0 | 0 | — | — | — | — | — |
| +0,10 | 0 | 0 | — | — | — | — | — |
| +0,11 | 0 | 0 | — | — | — | — | — |
| +0,12 | 0 | 0 | — | — | — | — | — |

Exemple, l'étiquette (6, 2), des deux côtés (« d » : discriminant à 5 pour cent) :

| delta | facteur | couplage g | largeur d'ordre 3 prédite | e_bord |
|---|---|---|---|---|
| -0,06 | 1 | 2,096e-03 | 8,67e-12 d | 0,52 |
| -0,06 | 6/5 | 2,515e-03 | 2,99e-09 d | 0,41 |
| -0,06 | 4/3 | 2,794e-03 | 5,65e-08 d | 0,35 |
| -0,06 | 3/2 | 3,143e-03 | 1,07e-06 d | 0,23 |
| -0,06 | 5/3 | 3,493e-03 | 1,07e-05 | 0,18 |
| +0,04 | 1 | 2,033e-03 | 3,95e-12 | 0,37 |
| +0,04 | 6/5 | 2,440e-03 | 1,33e-09 | 0,29 |
| +0,04 | 4/3 | 2,711e-03 | 2,51e-08 | 0,25 |
| +0,04 | 3/2 | 3,050e-03 | 4,70e-07 | 0,20 |
| +0,04 | 5/3 | 3,389e-03 | 4,80e-06 | 0,16 |

À delta = −0,06 la largeur prédite passe de 8,7e-12 à 1,1e-05 quand le couplage est multiplié
par 1,67 ; à +0,04, de 3,9e-12 à 4,8e-06 pour 1,67. Ce sont des prédictions de la chaîne d'ordre
3, pas des lectures.

## 5. Ce que je proposerais de geler (rien n'est décidé)

- Règle d'éligibilité d'une cellule, calculable par les deux machines avant tout run : boîte au
  plus 74 (la plus grande déjà jouée), au moins 8 états jugeables dont 5 dans le domaine, couple
  (w2, facteur) jamais joué. Sur la grille : 81 cellules, boîtes de 49 à 74.
- Ligne N : un w2 neuf à delta entre −0,07 et −0,06, aux cinq facteurs 3/4, 5/6, 1, 6/5, 4/3
  (couplage × 1,78). Sur la grille, à −0,06, ces cinq cellules ont de 10 à 14 états jugeables,
  tous dans le domaine et tous discriminants ; à −0,07, tous sauf un au plus sont dans le
  domaine. C'est là que se juge « l'ordre 3 fait mieux que l'ordre 2 ».
- Ligne P : un w2 neuf à delta entre +0,03 et +0,05, aux mêmes cinq facteurs. À +0,04 : de 12 à
  13 états jugeables, tous dans le domaine, aucun discriminant. On y juge « l'ordre 3 dans la
  tolérance », pas la comparaison des deux ordres.
- Deux cellules de bord, à facteur 1 : une vers −0,08, une vers +0,065, là où le domaine se
  défait. Elles éprouvent les deux gardes, pas la loi.
- Les w2 à trois décimales, tirés par machine 2 ou par une règle écrite au gel, pas par moi.
  Douze cellules en tout.
- Énoncés jugés : (E1) pour chaque état lu, qualifié et dans le domaine, l'ordre 3 rend la
  largeur de plateau dans une tolérance ; (E2) sur la ligne N, l'ordre 3 est plus près de la
  largeur de plateau que l'ordre 2 ; (E3) hors domaine, l'ordre 2 reste dans les bandes du delta
  98 et l'ordre 3 est déclaré non applicable. Observé sans être jugé : la parité du résidu, et
  la superposition des deux lignes en Gamma / |delta| à facteur égal.
- Tolérances et probabilités : après que les deux machines ont calculé les chaînes aux points
  tirés, pas avant.

Instrument : la sonde dense du delta 98 aux points tirés, puis le lecteur du gel ter sur sa
sortie (le gel ter lit dans la sortie dense w2, g, r_c, eta0 et, par état, l'étiquette,
l'énergie et la largeur déposée). Les deux runs précédents ont duré 4524 s (delta 98, seize
points, sur batterie) et 4377 s (gel ter, douze points) sur BOCAL4. Deux retouches, sans toucher
à la méthode : la sonde dense porte sa table de points en dur ; le lecteur vérifie le canon de
la sortie dense qu'il lit, et ce canon ne peut pas être écrit d'avance si la sortie est produite
dans le même run. Ses ancres, elles, restent celles du dépôt du delta 98.

## 6. Rectificatif à la note sur la loi

La note sur la loi (84fce9a6faf99c5b) écrit que l'acte du gel ter « attend le contreseing de
machine 2 ». Quand je l'ai écrite, machine 2 l'avait déjà contresigné tel quel (lot
e8ff4d600edf89ef) : son enveloppe est datée de 19 h 02 et ne m'est parvenue qu'à 21 h 43. La
référence de cette note est donc contresignée et non encore déposée. Aucun nombre ne change.

## 7. Limites

- L-1. La carte prédit les étiquettes, elle ne les lit pas : un à quatre états par point
  diffèrent aux seize points joués.
- L-2. Les seuils (0,7 ; 0,05 ; 5 et 2 pour cent ; boîte de 74 ; 8 et 5 états) sont les miens.
  Les deux premiers ont été lus sur les 131 états déjà vus.
- L-3. « Discriminant » compare deux chaînes entre elles. Il ne dit pas laquelle est juste :
  c'est la question du gel.
- L-4. La grille est au centième de w2 et à onze facteurs ; entre ses nœuds, rien n'est calculé.
  Les gardes seront à recalculer aux points tirés.
- L-5. La liste des couples déjà joués est recopiée du gel du delta 98 (section 4) et de ses
  seize points. Si un couple y manque, une étoile est fausse.
- L-6. Une plume. Le bloc d'ordre 3 n'a toujours que mes contrôles.

## 8. Pièces (convention B)

Au registre (8d54bf9) :

    82a0be882568fe0c  scripts/m17_chaine_v17.py
    7cd5977bc27bebc1  scripts/chaine_ordre2_bloc_machine1_v1.py
    10887c60d5f55bcf  journal/sonde_ordre2.json
    4195583a970eaf70  journal/verdict_ordre2.json
    41153158190cf7f1  gels/gel_ordre2_chaine_EA_pre_enregistrement_v1.md

Hors registre :

    534ba246aa3b8973  ordre3_bloc_machine1_v1.py (lot e93f1898dcd78a8f)
    84fce9a6faf99c5b  note_machine1_loi_largeur_2026-11-15_v1.md (même lot)
    e8ff4d600edf89ef  lot du contreseing de machine 2 (canon du manifeste)

De ce lot :

    f0f6581d87176752  carte_chaine_machine1_v1.py
    a7191248d3ef5056  carte_depot_v1.log
    c15d30e4e3e36912  carte_depot_v1.json
    c811e0aaa94618ad  carte_neg_v1.log
    c081f9c38745d98d  carte_neg_v1.json
    c0203401ea031b36  carte_pos_v1.log
    888ff9c8b1e8db67  carte_pos_v1.json
    da84e6de4fdfd23b  lecture_carte_machine1_v1.py
    685e5df1b462b5e3  lecture_carte_machine1_v1.log
    b78cc41e121a92fd  lecture_carte_v1.json
    40c42b2bf0a54154  ecart_exact_C07_machine1_v1.py
    51d07ebf3f58f96c  ecart_exact_C07_machine1_v1.log
    (ce script)       construction_note_carte_machine1_v1.py

