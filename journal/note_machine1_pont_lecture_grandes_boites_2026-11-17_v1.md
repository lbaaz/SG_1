# Le pont — lecture des grandes boîtes de machine 2 (côtés 190 à 402), note d'exploration

Machine 1, 2026-11-17 (nuit). **Hors chaîne, classe 3**, point sacrifié w2 = 101/50, 3 barreaux. Aucun calcul de physique de machine 1 : relecture des niveaux du lot de machine 2 lot_machine2_2026-11-17_grandes_boites_resultats_v1 (canon dce7431e7a8b4a8c, 27 pièces sur 27 au manifeste). Suite de la note v3 du pont et des attendus écrits avant le calcul (v1 c1ec807742b57f3b, tenue par machine 2 ; v2 écrite avant aussi).

## 0. En cinq phrases

1. Mes agrégats, recalculés depuis ses 568 niveaux, sont les siens au chiffre imprimé : comptes, sommes, participations, R, repères tirés.
2. Mes attendus : le compte tient aux trois tranches, la somme aux trois ; les parts sortent « poids aléatoires » autour de 200 (R = 0.883) et de 300 (1.082), « plus égales » autour de 400 (0.798). **Mon pari écrit est perdu** : la tranche autour de 200 ne redescend pas sous 0.85.
3. La saturation est exclue : une participation bloquée à 5.31 aurait donné R = 1.43 et 1.81 autour de 300 et de 400 ; le rapport R(400)/R(300) vaut 0.74, contre 1.26 pour une participation bloquée et 1.01 ± 0.16 pour un régime stationnaire.
4. Les deux choses dont le pont a besoin tiennent donc jusqu'au côté 402 : la force est conservée (règle de somme) et elle se partage entre un nombre de niveaux qui croît avec la boîte.
5. Ce qui ne se tranche pas : Porter-Thomas exact ou parts un peu plus égales. Et l'énoncé sur le bocal infini reste une extrapolation, sur six ordres de grandeur en côté (section 3).

## 1. Mes attendus, appliqués tels quels

| tranche | boîtes | niveaux par boîte (attendu, à 20 pour cent) | somme / largeur (attendu 0.90 à 1.10) | participation | R | Porter-Thomas aux mêmes comptes | exponentielle | issue |
|---|---|---|---|---|---|---|---|---|
| 190 à 209 | 20 | 14.10 (14.4) : tient | 1.034 ± 0.020 : tient | 6.32 | 0.883 | 1.000 ± 0.070 | 0.711 ± 0.035 | poids aléatoires |
| 297 à 302 | 6 | 20.83 (21.6) : tient | 1.026 ± 0.061 : tient | 7.32 | 1.082 | 0.999 ± 0.115 | 0.697 ± 0.055 | poids aléatoires |
| 397 à 402 | 6 | 26.83 (28.8) : tient | 1.090 ± 0.034 : tient | 12.34 | 0.798 | 1.001 ± 0.107 | 0.691 ± 0.049 | plus égales |

Machine 2 a appliqué les seuils de la v1 (0.85 et 1.25). La v2 remontait le seuil haut à 1.35 et 1.55 : aucune issue ne change, le plus grand R vaut 1.082. Le compte attendu autour de 200 (14.4) est ma droite, lue par elle. Niveaux non fiables : 1 sur 568 ; écart médian entre ses deux lectures de y : 7e-07 à 5e-06 selon la tranche.

## 2. Regards venus APRÈS lecture (pas des épreuves)

- **La densité de niveaux est uniforme dans la fenêtre** (rapport entre 7.5 et 0.5 |δ| : 0.98, 1.18, 1.03 aux trois tranches). Normaliser les parts par la moyenne de la boîte ne biaise donc pas R : normalisé localement, R vaut 0.882, 1.092, 0.799.
- **Le compte croît comme le côté** : 0.0690 niveau par quantum de côté dans la fenêtre, soit 0.00867 par |δ| et par quantum (droite par l'origine, 32 boîtes). Lecture : avec une énergie de forme indéfinie, les états voisins d'une énergie donnée longent une ligne du plan des quanta, pas une surface ; d'où une croissance comme le côté et non comme son carré.
- **La somme d'ensemble dépasse 1** : 1.043 ± 0.018 sur 32 boîtes. Par tranche d'écart au vide elle vaut 1.02, 1.11, 0.91, 1.01, 0.89, 0.99, 1.17, 1.25 (de 0.05–1 à 7–8 |δ|) ; pente +0.024 ± 0.014 par |δ| ; extrapolée à l'écart nul 0.945 ± 0.050, à 8 |δ| 1.14 ± 0.07. Lecture possible, non établie : le lisse de la chaîne d'ordre 3 serait un peu bas loin de l'énergie du vide, là où aucun gel ne l'a jugé (le lisse d'ordre 1 y vaut 0.682 fois celui d'ordre 3 à 8 |δ|, note v3). Je ne le lis pas comme de la force gagnée.
- **Le bas de la distribution est celui de Porter-Thomas, pas d'une exponentielle** : fraction des parts sous un dixième de la moyenne locale 0.255, 0.336, 0.261 (Porter-Thomas 0.248 ; exponentielle 0.095) ; au-dessus de trois fois la moyenne 0.085, 0.088, 0.081 (0.083 ; 0.050). L'écart à Porter-Thomas est dans la variance (1.34, 2.06, 1.27 fois le carré de la moyenne, contre 2) : il manque de très grosses parts autour de 200 et de 400. C'est la même information que R.
- **Deux boîtes de côtés consécutifs se comportent comme deux tirages** : corrélation des logarithmes des parts entre niveaux appariés au plus proche -0.05, -0.03, -0.14. La réserve de la note v3 (boîtes voisines non indépendantes) ne pèse pas sur les parts.
- **L'issue « plus égales » autour de 400 tient à trois boîtes** : côtés impairs R = 0.668, côtés pairs R = 0.944 (trois boîtes chacun). Autour de 200, pairs et impairs donnent 0.882 et 0.883 : pas d'effet de parité, donc une fluctuation probable.
- **Le vide est accroché dans deux boîtes sur 32** : il lui manque 2.9e-04 de poids au côté 193 et 5.2e-05 au côté 302, sans doute par un niveau tombé tout près de lui, hors de la fenêtre (non vérifié : les fichiers ne portent que la fenêtre, et aucun niveau de la fenêtre n'en est assez proche). Ce seraient les accidents attendus, rares.

## 3. Ce que cela dit, et l'échelle qu'il ne faut pas oublier

- Le pont tient jusqu'au côté 402 : la largeur lue sous absorbeur est bien la force de couplage du vide au spectre réel de la boîte fermée, et cette force se répartit, avec des poids proches du hasard, sur des niveaux dont le nombre croît comme le côté.
- Sur la question fine, je n'ai pas eu raison et machine 2 n'est pas confirmée : un R constant vers 0.9 (son R combiné 0.904 ± 0.052) décrit les trois tranches. Les parts « plus égales » des petites boîtes (R de 0.69 à 0.89 jusqu'au côté 151) ne se prolongent pas telles quelles.
- **L'échelle.** Dans la fenêtre il y a 0.434 niveau par unité d'énergie et par quantum de côté. Un niveau du dehors par largeur Γ = 3.2661e-09 demande un côté d'environ 7e+08. Les boîtes calculées s'arrêtent à 402 : dire que le bocal infini se désintègre au taux Γ, c'est prolonger sur six ordres de grandeur une tendance vue sur un facteur vingt. La conjecture de la note v3 reste une conjecture ; ce lot lui enlève une objection (la saturation), il ne la démontre pas.

## 4. Ce que je propose (à l'opérateur d'ouvrir ou non)

1. Ne plus grossir les boîtes pour départager R : la question est secondaire pour le pont. Six boîtes de plus autour de 400 (35 minutes chez machine 2, selon elle) ne valent que si l'on veut savoir si 0.80 était une fluctuation.
2. Contrôler directement le lisse loin de l'énergie du vide, sans bruit de comptage : densité locale de l'état (0, 0) sous absorbeur en 2D contre la chaîne d'ordre 3, de 0 à 8 |δ|, au point sacrifié. C'est ce que la somme à 1.043 laisse soupçonner et ne peut pas établir.
3. Ensuite seulement, geler le pont sur un point neuf (règle de somme et croissance du compte), joué par machine 2.

## 5. Limites

- Tous les regards de la section 2 sont venus après lecture des agrégats. Six boîtes seulement autour de 300 et de 400 ; 3 barreaux ; un seul point, sacrifié.
- Mon rejeu relit les niveaux de machine 2 : il éprouve l'agrégation, pas ses boîtes. Le moteur et le lisse d'ordre 3 sont partagés par les deux machines.
- Les parts y reposent sur une formule de premier ordre ; les niveaux à moins de 0.05 |δ| du vide sont hors fenêtre. Les barres d'erreur sur R supposent des parts de Porter-Thomas.

## 6. Pièces

rejeu_grandes_boites_machine1_v1.py, regards_niveaux_machine1_v1.py, regards_complements_machine1_v1.py, leurs journaux et leurs JSON ; construction_note_lecture_grandes_boites_machine1_v1.py (écrit cette note). Au poste de machine 1, non transmises.
