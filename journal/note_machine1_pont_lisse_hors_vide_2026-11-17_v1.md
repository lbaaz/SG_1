# Le pont — la chaîne d'ordre 3 loin de l'énergie du vide, contre la 2D sous absorbeur — note d'exploration

Machine 1, 2026-11-17 (nuit). **Hors chaîne, classe 3**, point sacrifié w2 = 101/50, 3 barreaux, g = 5.53067e-03. Aucun run de machine 2, aucun gel. Ouverture de l'opérateur : « Go regarder la chaîne d'ordre 3 » (00 h 24). Attendu écrit avant le calcul (canon 5bb45d0c8081106f), rectificatif d'instrument écrit avant de calculer le rapport (c0dc8b2732ba7065). Suite de la note de lecture des grandes boîtes du même jour, dont elle corrige un soupçon.

## 0. En cinq phrases

1. **Mon soupçon est faux.** La chaîne d'ordre 3 rend la densité de l'état (0, 0) du système 2D ouvert à 1 pour cent près sur toute la fenêtre, de 0.05 à 8 |δ| du vide : le rapport R va de 1.0006 à 0.9896, sur 12.5 décades de densité.
2. Attendu : A1 tient (R = 1.0006 au plus près du vide) ; A2 tombe (j'attendais R entre 1.05 et 1.25 à 8 |δ|, il vaut 0.9914). À la lettre l'issue est (iii) : R décroît et passe sous 0.99 de 0.0004 à 7 |δ|, moins que l'incertitude ; en substance c'est (ii), le lisse est bon.
3. Ma spécification d'instrument (A0) ne tenait pas : aux barreaux 5 et 6 l'absorbeur réfléchit. Je l'ai remplacée, avant de calculer R, par la routine de plateau déposée du lecteur. Sous elle les quatre absorbeurs s'accordent à 0.0045 près, et un cinquième, reculé de 30 quanta, rend les mêmes densités à 0.0004 près.
4. Les ordres convergent aussi loin du vide : à 8 |δ| la chaîne d'ordre 1 est à -31.2 pour cent de la 2D, l'ordre 2 à -3.6, l'ordre 3 à +0.9.
5. L'excès de la somme des grandes boîtes (1.043 ± 0.018) ne vient donc pas du lisse. Rapporté à la 2D ouverte il vaut 1.048, à 2.7 écarts types de 1 ; il est porté par les deux dernières tranches d'écart (6 à 8 |δ|). Il reste inexpliqué.

## 1. Ce qui est calculé

Densité locale de (0, 0) sous absorbeur à l'énergie E, lue par le flux : ρ = (η/π) Σ W |x|², x = (E − H + iηW)⁻¹ e₍₀,₀₎, E pris à écart égal du vide de chaque système.
- **Chaîne** : blocs déposés d'ordre 2 et 3, dix-huit variantes de l'absorbeur adapté, médiane des logarithmes. Recoupements : largeur au vide 3.2661e-09 (note v3 : 3.2661e-09) ; rapports ordre 1 sur ordre 3 du tableau de la note v3 retrouvés ; la forme directe −Im G₀₀/π, celle des grandes boîtes, égale la forme par flux à 3e-15 près.
- **2D** : hamiltonien, absorbeurs A, B, C, D et lecture du vide du bloc « lecteur creux » déposé (canon contrôlé), boîtes de 104 à 124 quanta de côté, barreaux k = −3 à 8 ; seule la résolution à énergie fixée est neuve. Poids du vide w0 = 0.99927488. Au vide, le plateau 2D et la chaîne d'ordre 3 s'accordent à 0.00006 près en logarithme sous A, B et D.
- R(x) = ρ_2D(x) / (w0 ρ_chaîne(x)). La somme / largeur des grandes boîtes est, en moyenne, la moyenne de R sur la fenêtre multipliée par ce que la boîte fermée ajoute ou retire au système ouvert.

## 2. Résultat

| écart au vide (|δ|) | log₁₀ ρ 2D | R, ordre 3 | R, ordre 2 | R, ordre 1 | étendue entre absorbeurs 2D | étendue entre variantes de la chaîne |
|---|---|---|---|---|---|---|
| 0.05 | -3.39 | 1.0006 | 0.9981 | 0.9867 | 0.0021 | 0.0042 |
| 0.25 | -5.21 | 1.0003 | 0.9982 | 0.9945 | 0.0027 | 0.0047 |
| 0.5 | -6.27 | 1.0005 | 0.9984 | 1.0044 | 0.0031 | 0.0054 |
| 1 | -7.68 | 1.0006 | 0.9997 | 1.0255 | 0.0019 | 0.0053 |
| 1.5 | -8.74 | 0.9996 | 1.0002 | 1.0479 | 0.0006 | 0.0046 |
| 2 | -9.61 | 0.9985 | 1.0006 | 1.0713 | 0.0017 | 0.0049 |
| 3 | -11.06 | 0.9969 | 1.0036 | 1.1215 | 0.0027 | 0.0059 |
| 4 | -12.26 | 0.9941 | 1.0066 | 1.1761 | 0.0025 | 0.0072 |
| 5 | -13.30 | 0.9926 | 1.0120 | 1.2357 | 0.0013 | 0.0076 |
| 6 | -14.23 | 0.9909 | 1.0186 | 1.3020 | 0.0020 | 0.0057 |
| 7 | -15.07 | 0.9896 | 1.0258 | 1.3744 | 0.0009 | 0.0073 |
| 8 | -15.85 | 0.9914 | 1.0371 | 1.4540 | 0.0045 | 0.0106 |

Moyenne de R (ordre 3) sur la fenêtre, uniforme en écart : 0.9949 ; pente -0.0015 par |δ|. L'écart à 1 (au plus 0.0104) est du même ordre que ce que l'absorbeur de la chaîne laisse indéterminé (étendue des dix-huit variantes : jusqu'à 0.0106) : la chaîne d'ordre 3 n'est pas distinguée de la 2D ouverte au-delà de cette étendue.

## 3. L'attendu, appliqué

- **A0 tel qu'écrit (barreaux 0 à 6, quatre absorbeurs, étendue ≤ 0.02) : ne tient pas.** L'étendue va de 0.08 à 0.41 selon l'écart. Cause : aux barreaux faibles (5, 6 et au-delà) la densité oscille avec l'écart, signe de réflexion ; sous C (forme F1) le bord fort se dégrade aussi. Défaut de ma spécification, pas de la lecture : je n'avais pas repris la règle de plateau du lecteur.
- **Règle de remplacement, fixée avant R** : routine de plateau déposée (cinq barreaux consécutifs de plus petit rapport, plateau si le rapport est au plus 1.05), par absorbeur ; médiane des quatre ; lisible si les quatre rendent un plateau et s'accordent à 0.02. Lisible aux douze écarts.
- **A1 : tient.** **A2 : ne tient pas.** **Issue : (iii) à la lettre, (ii) en substance.** Je m'étais donné 0.50 pour (i), 0.30 pour (ii), 0.20 pour (iii) : la moitié de ma mise était sur la mauvaise issue.
- Contrôle venu après : un absorbeur de forme F2 dont le bord est reculé de 30 (boîte de 134) rend les densités de la médiane à 0.0004 près. La densité ouverte ne dépend pas de l'endroit où l'on absorbe, de 24 à 54 quanta.

## 4. Ce que cela dit

- La chaîne d'ordre 3 n'avait été jugée qu'à l'énergie du vide (gels des deltas 100 et 102). Ici, hors gel et sur un seul point, elle tient à 1 pour cent près jusqu'à 8 |δ| du vide, là où la densité a perdu plus de douze décades. Le lisse que les deux machines partagent pour les grandes boîtes est maintenant confronté à un objet 2D indépendant de la chaîne (même moteur).
- **La somme des grandes boîtes.** Tranches d'écart de 0.05 à 6 |δ| : 0.99 ± 0.06 ; de 6 à 8 |δ| : 1.21 ± 0.13 (32 boîtes, erreurs indicatives). Or R y vaut 0.99. L'excès n'est donc ni le lisse ni, d'après les deux lectures indépendantes de machine 2, une erreur numérique sur les petites parts. Restent : une fluctuation (2 à 3 écarts types ; sept des huit échantillons de la note v3 étaient déjà au-dessus de 1, comme les trois tranches de machine 2), ou un effet propre à la boîte fermée que je ne sais pas nommer. Je ne tranche pas.
- La phrase de ma note de lecture des grandes boîtes, « le lisse de la chaîne d'ordre 3 serait un peu bas loin de l'énergie du vide », est retirée : c'est le contraire, de 1 pour cent au plus.

## 5. Ce que je propose (à l'opérateur d'ouvrir ou non)

1. Pour l'excès de la somme, la seule épreuve nette est le nombre : quatre-vingts boîtes neuves autour du côté 200 (environ une heure et quart chez machine 2 au rythme de ses journaux) ramènent l'erreur à 0.01. Attendu à écrire avant ; c'est elle qui lance.
2. Le pont a maintenant ses trois appuis vérifiés au point sacrifié : la chaîne vaut la 2D ouverte dans toute la fenêtre, la force se retrouve dans la boîte fermée, elle se partage sur un nombre de niveaux qui croît. L'étape qui compte ensuite est de le geler sur un point neuf.

## 6. Limites

- Un seul point (sacrifié), une seule profondeur (3 barreaux), un seul côté du vide (opposé à δ). La chaîne et la 2D partagent le moteur : l'accord éprouve la réduction à une dimension et les absorbeurs, pas le moteur.
- A0 a été remplacé en cours de route ; la règle de remplacement existait (elle est déposée) et a été fixée avant de rapprocher la 2D de la chaîne, mais après avoir vu les densités 2D.
- Le contrôle par l'absorbeur reculé et la lecture par tranches de la somme sont venus après la lecture.

## 7. Pièces (au poste de machine 1, non transmises)

attendu_lisse_hors_vide_machine1_v1.txt, rectificatif_instrument_lisse_hors_vide_machine1_v1.txt ; lisse_chaine_machine1_v1.py, lisse_2d_machine1_v1.py, lecture_lisse_hors_vide_machine1_v1.py, controle_absorbeur_recule_machine1_v1.py, leurs journaux et leurs JSON ; construction_note_lisse_hors_vide_machine1_v1.py (écrit cette note). Registre lu à la tête 2988237 (delta 102), non écrit.
