# Le pont entre la largeur sous absorbeur et le système fermé — note d'exploration, v2

Machine 1, 2026-11-16 (soir). **Hors chaîne, classe 3.** Aucun run de machine 2, aucun gel, machine 2 non consultée. Cette v2 remplace la v1 (qui reste au projet) : elle corrige un signe et ajoute quatre regards (autres degrés, boîte 2D fermée, règle de somme, grandes boîtes). Ouvertures de l'opérateur : « On peut avancer sur la recherche là ? » (21 h 39), puis « Ouvre ! on cherche ! » (21 h 55).

## 0. Défaut de la v1, déclaré

Le tableau de la v1 donnait ln(V²T/Γ) de +0.0057 à +0.0171. Le signe est faux : V²T est SOUS Γ, de -0.0171 à -0.0057 en logarithme. Cause : le script de construction changeait le signe du champ lu. Le texte de la v1 ne dépendait pas du signe ; le tableau ci-dessous est le bon.

## 1. Chaîne fermée : Γ = V² · T

La chaîne fermée (coupée au site N, sans absorbeur) est réelle symétrique : aucune largeur. Quand on fait défiler la condition de bord au bout de la chaîne, le vide subit un croisement évité de demi-écart V avec un niveau du dehors. T est le temps classique d'aller et retour entre la sortie de la barrière et le bout de la chaîne, T(E) = 2 ∫ dm / √(4 t(m)² − (E − m δ)²), calculé sur les sauts du moteur sans rien lire du spectre. Sur 136 croisements (les 16 cellules lisibles du gel « largeur du vide », premier ordre, coupures N de 25 à 40) :

| barreaux | Γ sous absorbeur (de … à) | V (de … à) | 2π / (T·|δ|) | ln(V²T / Γ) (de … à) |
|---|---|---|---|---|
| 3 | 5.0e-10 … 3.0e-09 | 8.1e-07 … 4.9e-06 | 2.838 … 2.905 | -0.0171 … -0.0155 |
| 4 | 1.1e-11 … 6.6e-11 | 1.2e-07 … 7.4e-07 | 2.903 … 2.989 | -0.0134 … -0.0098 |
| 5 | 2.3e-13 … 1.4e-12 | 1.8e-08 … 1.1e-07 | 2.959 … 3.062 | -0.0084 … -0.0068 |
| 6 | 4.4e-15 … 2.6e-14 | 2.5e-09 … 1.5e-08 | 3.008 … 3.100 | -0.0071 … -0.0057 |

Rappel de la v1 : l'attendu écrit AVANT le premier calcul (règle d'or avec l'espacement des niveaux voisins) est tombé, de +0.112 à +0.223 en logarithme ; la lecture par le temps classique est venue APRÈS avoir vu les nombres.

**Épreuve hors échantillon : d'autres degrés.** Attendu écrit avant de lancer : |ln(V^2 T / Gamma)| <= 0.03. Point w2 = 991/500, couplage fixé par la même règle à chaque degré, premier ordre.

| degré p | barreaux | croisements retenus | 2π / (T·|δ|) | ln(V²T / Γ) (de … à) | étendue de l'absorbeur (de … à) |
|---|---|---|---|---|---|
| 3 | 3 | 9 | 1.24 … 1.35 | -0.0227 … -0.0145 | 0.0333 … 0.0333 |
| 3 | 4 | 9 | 1.28 … 1.39 | -0.0184 … -0.0109 | 0.0398 … 0.0398 |
| 3 | 5 | 8 | 1.32 … 1.41 | -0.0181 … -0.0076 | 0.0460 … 0.0460 |
| 3 | 6 | 9 | 1.35 … 1.49 | -0.0168 … -0.0062 | 0.0507 … 0.0507 |
| 5 | 3 | 9 | 2.84 … 2.90 | -0.0171 … -0.0155 | 0.0033 … 0.0033 |
| 5 | 4 | 9 | 2.90 … 2.99 | -0.0134 … -0.0098 | 0.0026 … 0.0026 |
| 5 | 5 | 8 | 2.96 … 3.06 | -0.0083 … -0.0068 | 0.0046 … 0.0046 |
| 5 | 6 | 8 | 3.01 … 3.10 | -0.0071 … -0.0058 | 0.0050 … 0.0050 |
| 7 | 3 | 9 | 4.60 … 4.63 | -0.0142 … -0.0137 | 0.0017 … 0.0017 |
| 7 | 4 | 9 | 4.69 … 4.72 | -0.0100 … -0.0090 | 0.0033 … 0.0033 |
| 7 | 5 | 9 | 4.75 … 4.80 | -0.0073 … -0.0064 | 0.0019 … 0.0019 |
| 7 | 6 | 9 | 4.80 … 4.87 | -0.0049 … -0.0045 | 0.0022 … 0.0022 |
| 9 | 3 | 9 | 6.40 … 6.40 | -0.0136 … -0.0136 | 0.0023 … 0.0023 |
| 9 | 4 | 9 | 6.52 … 6.53 | -0.0089 … -0.0088 | 0.0023 … 0.0023 |
| 9 | 5 | 9 | 6.60 … 6.62 | -0.0063 … -0.0062 | 0.0009 … 0.0009 |
| 9 | 6 | 1 | 6.69 … 6.69 | -0.0050 … -0.0050 | 0.0036 … 0.0036 |

Sur 136 croisements rendus, 133 sont retenus, dont 133 respectent l'attendu. Écartés : 3 faux croisements, tous au degré 9, 6 barreaux (coupures 36, 40) : les deux états n'y portent pas chacun la moitié du vide, et le demi-écart rendu (9.0e-03) n'a rien d'un couplage sous barrière ; le seul croisement lisible de cette case donne V = 2.7e-13, au bord de la double précision. Défaut du chercheur de croisement, qui n'avait pas de garde ; le filtre appliqué ici (chacun des deux poids entre 0.4 et 0.6) est venu après lecture. Au degré 3 l'étendue de l'absorbeur dépasse l'écart mesuré : l'épreuve y est faible.

**Antériorité.** Lire une largeur dans les croisements évités d'un spectre réel, en faisant varier un paramètre de boîte, est la méthode de stabilisation de la chimie quantique (Hazi et Taylor, Phys. Rev. A 1, 1109, 1970) ; la relation Γ = 2π V² × densité de niveaux, avec une densité T/2π pour un seul canal, en est la forme élémentaire. Rien de neuf dans le principe. Ce qui est à nous : le nombre, sur le vide fantôme, avec un T classique fini quelle que soit la longueur de la chaîne. Que la largeur soit portée par plusieurs états quasi discrets voisins, et non par un seul croisement, est aussi relevé dans cette littérature (Kaprálová-Žďánská, arXiv:2004.06372, résumé seul lu) : c'est ce que la section 3 retrouve en 2D. Références relevées par une recherche rapide ce soir, non lues en entier ; la note d'antériorité n'en dit rien encore.

## 2. Boîte 2D fermée, au point sacrifié

Point w2 = 101/50. C'est un centième, exclu de tout tirage ; il est **sacrifié** pour tout gel futur sur le système fermé, puisque machine 1 y a lu la 2D. Cellules : 3 barreaux, g = 5.53067e-03, Γ = 3.2661e-09 ; 4 barreaux, g = 4.22189e-03, Γ = 7.2530e-11 ; 5 barreaux, g = 3.35640e-03, Γ = 1.5154e-12. Boîte carrée en quanta (N × N), paroi dure, potentiel u sur le dernier site de l'échelle du vide pour faire défiler le bord ; diagonalisation complète. Γ : plateau de la chaîne d'ordre 3 sous absorbeur adapté.

Attendu écrit AVANT de regarder : -0.05 ≤ ln(V²T/Γ) ≤ +0.03 dans la boîte 2D, comme dans la chaîne.

| barreaux | côté N | site de coupure M | V trouvé (2D) | V attendu √(Γ/T) | ln(V²T/Γ) 2D | chaîne fermée ordre 1 | chaîne fermée ordre 3 | attendu |
|---|---|---|---|---|---|---|---|---|
| 3 | 23 | 11 | 5.805e-06 | 5.882e-06 | -0.0265 | -0.0184 | -0.0079 | tient |
| 3 | 27 | 13 | 5.672e-06 | 5.752e-06 | -0.0280 | -0.0041 | -0.0043 | tient |
| 3 | 31 | 15 | 4.592e-06 | 5.669e-06 | -0.4216 | +0.0001 | -0.0118 | **faussé** |
| 3 | 35 | 17 | 4.911e-06 | 5.612e-06 | -0.2668 | +0.0004 | -0.0128 | **faussé** |
| 3 | 41 | 20 | 7.905e-07 | 5.553e-06 | -3.8990 | -0.0026 | -0.0099 | **faussé** |
| 4 | 27 | 13 | 8.406e-07 | 8.871e-07 | -0.1075 | -0.0166 | -0.0197 | **faussé** |
| 4 | 35 | 17 | 4.285e-07 | 8.567e-07 | -1.3856 | -0.0026 | pas de croisement trouvé | **faussé** |
| 5 | 27 | 13 | 1.336e-07 | 1.331e-07 | +0.0078 | +0.0036 | +0.0084 | tient |
| 5 | 35 | 17 | 3.240e-08 | 1.269e-07 | -2.7300 | -0.0003 | -0.0088 | **faussé** |

**L'attendu est faussé dans 6 boîtes sur 9.** Il tient dans 3 boîtes (côté 23 à 3 barreaux ; côté 27 à 3 barreaux ; côté 27 à 5 barreaux) ; dans les autres, V est trop petit, jusqu'à un facteur 7.0, soit 49 sur V² (côté 41, 3 barreaux). L'en-tête des deux scripts de la règle de somme dit « 4 boîtes sur 7 » : erreur de décompte de la plume, le compte est celui du tableau. Les chaînes fermées coupées au même site restent à 0.020 près en logarithme (17 lectures ; 1 sans croisement trouvé par le balayage). La boîte 2D fermée n'est donc pas la chaîne fermée dès que la boîte grandit.

## 3. Où est passée la force ?

Deux lectures : le couplage est PERDU (la largeur sous absorbeur ne dirait alors rien de la boîte fermée), ou il est PARTAGÉ entre plusieurs niveaux du dehors. Dans la boîte fermée nue, chaque niveau k du dehors porte un poids c_k² sur l'état (0, 0), et son couplage au vide est V_k² = c_k² (E_k − E_vide)² / poids du vide (premier ordre, loin du croisement). Sous absorbeur la même grandeur est lisse : Γ(E)/2π = (E − E_vide)² ρ(E), ρ étant la densité locale de (0, 0) dans la chaîne d'ordre 3.

**Première passe (somme brute par fenêtre, 3 barreaux, côtés 21 à 45).** Rapport d'ensemble 0.959, mais par fenêtre de 0.107 à 1.740 : Γ(E) perd près d'une décade par |δ|, si bien que la somme est dominée par un ou deux niveaux. Défaut déclaré de cette passe : la densité lisse sortait avec le mauvais signe (résolvante prise à l'envers), corrigé avant relecture, les rapports n'en dépendant pas en valeur absolue ; et elle était prise à énergie absolue égale au lieu d'écart au vide égal (effet de l'ordre du centième de |δ|), corrigé dans la seconde passe.

**Seconde passe (statistique repondérée).** Chaque niveau k porte une largeur d'énergie y_k = c_k² / (poids du vide × ρ(E_k)), comptée en |δ|. Si la force est partagée et non perdue, la somme des y_k sur une fenêtre vaut la largeur de la fenêtre, quel que soit le nombre de niveaux. Fenêtre : de 0.05 à 8 |δ| du vide, du côté opposé à δ (aucun état localisé sous la barrière n'y tombe).

Attendu écrit AVANT de lancer : somme / largeur entre 0.85 et 1.15 pour la boîte 2D, à 3 barreaux pour les côtés 46 à 64, à 4 et à 5 barreaux pour les côtés 21 à 45 ; même bande pour la chaîne d'ordre 3 ; et le nombre de niveaux 2D par boîte croît avec le côté alors que celui de la chaîne ne croît pas. Les côtés 21 à 45 à 3 barreaux étaient déjà lus : ils ne comptent pas comme épreuve.

| échantillon | boîtes | 2D : somme / largeur | chaîne ordre 3 | chaîne ordre 1 | niveaux par boîte, 2D | chaîne ordre 3 | participation 2D | épreuve |
|---|---|---|---|---|---|---|---|---|
| 3 barreaux, côtés 21 à 45 | 25 | 1.017 ± 0.064 | 1.072 ± 0.086 | 0.819 ± 0.054 | 2.20 | 1.48 | 1.80 | déjà lu |
| 3 barreaux, côtés 46 à 64 | 19 | 1.048 ± 0.040 | 0.981 ± 0.078 | 0.886 ± 0.051 | 4.00 | 1.53 | 2.78 | tient |
| 4 barreaux, côtés 21 à 45 | 25 | 1.020 ± 0.083 | 1.007 ± 0.078 | 0.781 ± 0.050 | 1.96 | 1.36 | 1.58 | tient |
| 5 barreaux, côtés 21 à 45 | 25 | 1.021 ± 0.077 | 0.996 ± 0.072 | 0.866 ± 0.054 | 1.84 | 1.40 | 1.55 | tient |

L'attendu tient aux 3 épreuves sur 3. Moyenne pondérée des trois : 1.039 ± 0.033. La barre d'erreur est l'écart type entre boîtes divisé par la racine de leur nombre ; elle suppose des boîtes indépendantes, ce qu'elles ne sont pas tout à fait (deux côtés consécutifs partagent le même site de coupure : pour les chaînes, qui ne dépendent que de ce site, la barre est sous-estimée d'un facteur racine de 2).

**La statistique voit-elle quelque chose ? Contrôle par l'ordre 1.** Sans bruit (deux chaînes sous absorbeur, à écart au vide égal), la densité lisse de l'ordre 1 rapportée à celle de l'ordre 3 vaut :

| écart au vide, en |δ| | 0.05 | 0.25 | 0.50 | 1.00 | 2.00 | 3.00 | 4.00 | 6.00 | 8.00 |
|---|---|---|---|---|---|---|---|---|---|
| g = 5.53067e-03 | 1.014 | 1.006 | 0.996 | 0.976 | 0.933 | 0.889 | 0.845 | 0.761 | 0.682 |
| g = 4.22189e-03 | 1.014 | 1.005 | 0.994 | 0.971 | 0.924 | 0.876 | 0.830 | 0.743 | 0.662 |
| g = 3.35640e-03 | 1.013 | 1.004 | 0.991 | 0.966 | 0.916 | 0.866 | 0.818 | 0.728 | 0.647 |

Les deux ordres s'accordent au vide (c'est là que le gel les a jugés) et s'écartent en s'en éloignant : en moyenne sur la fenêtre, l'ordre 1 vaut 0.82 à 0.85 de l'ordre 3. La chaîne FERMÉE d'ordre 1 lit 0.848, 0.781, 0.866 (voir le tableau) : la statistique voit donc une différence réelle de cet ordre. Rapportée au lisse d'ordre 1, la boîte 2D donnerait 1.251 ± 0.057 (3 barreaux), 1.258 ± 0.121 (4 barreaux), 1.258 ± 0.111 (5 barreaux). **La boîte 2D fermée se range avec l'ordre 3**, y compris loin de l'énergie du vide, où aucun gel n'a rien jugé.

**Le dehors se peuple quand la boîte grandit** (3 barreaux, côtés 21 à 64) :

| côtés | boîtes | 2D : somme / largeur | niveaux 2D par boîte | niveaux de la chaîne | participation 2D | plus petite part y | part médiane |
|---|---|---|---|---|---|---|---|
| 21 à 27 | 7 | 0.98 | 1.29 | 1.43 | 1.21 | 3.5 | 6.4 |
| 28 à 34 | 7 | 1.06 | 2.29 | 1.43 | 1.96 | 0.42 | 3.7 |
| 35 à 41 | 7 | 1.01 | 2.57 | 1.43 | 2.04 | 0.11 | 3.2 |
| 42 à 48 | 7 | 1.04 | 2.86 | 1.71 | 2.15 | 0.061 | 3.5 |
| 49 à 56 | 8 | 1.10 | 3.88 | 1.75 | 2.63 | 0.00089 | 2.2 |
| 57 à 64 | 8 | 0.99 | 4.62 | 1.25 | 3.15 | 0.0044 | 1.5 |

Droite ajustée du nombre de niveaux selon le côté : pente +0.084 par quantum en 2D, +0.000 pour la chaîne. La somme reste entre 0.98 et 1.10 pendant que le nombre de niveaux par boîte est multiplié par 3.6 : la force se partage. Le partage est très inégal (la plus petite part vaut 3.3e-04 fois la médiane), ce qui explique qu'un croisement pris au hasard puisse être très étroit, comme au côté 41 de la section 2.

Où cela commence : un troisième niveau apparaît dans la fenêtre au côté 28, 31, 33 (3, 4, 5 barreaux). Les sauts de l'échelle atteignent 0.5 — la moitié du désaccord d'une unité qui sépare l'échelle du vide de ses voisines — au site 12, 14, 15, soit au côté 25, 29, 31. Le dehors cesse d'être une échelle unique à peu près là où les échelles voisines s'ouvrent ; lecture cohérente, non éprouvée autrement.

## 4. Boîtes plus grandes : le dehors continue-t-il de se peupler ?

La conjecture de la section 5 repose sur la poursuite de cette croissance. Au-delà du côté 64 la diagonalisation complète est trop lourde : décalage-inversion creuse autour de la fenêtre, chaque boîte résolue deux fois (décalages à 2 et à 5 |δ| sous le vide), un niveau n'étant compté fiable que si ses deux lectures de y s'accordent à 2 pour cent près. Contrôle : aux côtés 63 et 64 la méthode creuse rend ce que rend la diagonalisation complète (côté 63 : 5 niveaux et somme 0.939 contre 5 et 0.939 ; côté 64 : 4 niveaux et somme 1.070 contre 4 et 1.070).

| barreaux | côté | états | niveaux dans la fenêtre | non fiables | somme / largeur | participation | plus petite part y |
|---|---|---|---|---|---|---|---|
| 3 | 72 | 5184 | 5 | 0 | 0.718 | 1.97 | 0.19 |
| 3 | 73 | 5329 | 6 | 0 | 1.090 | 3.46 | 0.00011 |
| 3 | 80 | 6400 | 5 | 0 | 0.968 | 2.92 | 0.00092 |
| 3 | 81 | 6561 | 7 | 0 | 1.301 | 3.96 | 0.018 |
| 3 | 96 | 9216 | 7 | 0 | 0.986 | 4.73 | 0.018 |
| 3 | 97 | 9409 | 7 | 0 | 1.135 | 4.87 | 0.11 |
| 3 | 112 | 12544 | 6 | 0 | 0.987 | 3.28 | 0.21 |
| 3 | 113 | 12769 | 7 | 0 | 0.818 | 4.45 | 0.0042 |
| 3 | 128 | 16384 | 9 | 0 | 1.045 | 5.61 | 0.13 |
| 3 | 129 | 16641 | 9 | 0 | 1.043 | 4.78 | 0.17 |
| 3 | 150 | 22500 | 11 | 0 | 0.993 | 5.88 | 0.021 |
| 3 | 151 | 22801 | 11 | 0 | 1.113 | 5.29 | 0.00029 |
| 3 | 200 | 40000 | 16 | 0 | 1.118 | 5.42 | 0.0016 |
| 3 | 201 | 40401 | 13 | 0 | 1.070 | 5.21 | 0.0033 |
| 4 | 96 | 9216 | 7 | 0 | 0.941 | 3.87 | 1.2e-05 |
| 4 | 97 | 9409 | 7 | 0 | 0.710 | 3.24 | 0.00054 |
| 4 | 128 | 16384 | 9 | 0 | 1.069 | 5.82 | 0.0072 |
| 4 | 129 | 16641 | 10 | 0 | 0.960 | 5.97 | 0.023 |
| 4 | 150 | 22500 | 10 | 0 | 1.039 | 8.56 | 0.27 |
| 4 | 151 | 22801 | 13 | 0 | 1.045 | 6.40 | 0.012 |
| 5 | 96 | 9216 | 6 | 0 | 0.931 | 3.48 | 0.12 |
| 5 | 97 | 9409 | 7 | 0 | 1.049 | 4.25 | 0.042 |
| 5 | 128 | 16384 | 11 | 0 | 1.078 | 4.61 | 0.029 |
| 5 | 129 | 16641 | 8 | 0 | 1.120 | 5.38 | 0.12 |
| 5 | 150 | 22500 | 10 | 0 | 0.974 | 6.49 | 0.19 |
| 5 | 151 | 22801 | 13 | 0 | 1.129 | 6.40 | 0.0027 |

Attendus écrits AVANT chaque lancement (en-tête de pont_2d_grand_machine1_v1.py, puis attendu_grand_m4_m5_cote200_machine1_v1.txt), et ce qui est sorti :

| attendu | lu | verdict |
|---|---|---|
| 3 barreaux, côtés 150 et 151 : entre 9 et 15 niveaux (droite prolongée ; 6 ou moins aurait fait tomber la conjecture) | 11.0 | tient |
| 3 barreaux, côtés 72 à 151 : somme / largeur moyenne entre 0.85 et 1.15 | 1.016 | tient |
| 3 barreaux, côtés 128 à 151 : participation au-dessus de celle des côtés 57 à 64 (3.15) | 5.39 | tient |
| 4 barreaux, côtés 150 et 151 : entre 8 et 12 niveaux | 11.5 | tient |
| 5 barreaux, côtés 150 et 151 : entre 7 et 12 niveaux | 11.5 | tient |
| 4 barreaux, six boîtes : somme / largeur moyenne entre 0.85 et 1.15 | 0.961 | tient |
| 5 barreaux, six boîtes : somme / largeur moyenne entre 0.85 et 1.15 | 1.047 | tient |
| 4 barreaux : aucun niveau non fiable | 0 | tient |
| 3 barreaux, côtés 200 et 201 : entre 12 et 19 niveaux | 14.5 | tient |
| 3 barreaux, côtés 200 et 201 : somme / largeur moyenne entre 0.7 et 1.3 | 1.094 | tient |

Les 10 attendus tiennent sur 10. À 3 barreaux, la droite ajustée sur tous les côtés de 21 à 201 a une pente de +0.072 niveau par quantum : le compte croît toujours, un peu moins vite que sur les seuls côtés 21 à 64. Le compte dépend peu de la profondeur (11.0, 11.5, 11.5 niveaux en moyenne aux côtés 150 et 151, à 3, 4, 5 barreaux). **La participation croît moins nettement que le compte** : 4.80 aux côtés 96 et 97, 5.19 aux côtés 128 et 129, 5.59 aux côtés 150 et 151, 5.31 aux côtés 200 et 201 contre 3.15 aux côtés 57 à 64 ; entre 150 et 200 elle ne monte plus de façon lisible, sur deux boîtes seulement. Le nombre de niveaux qui portent vraiment la force pourrait donc croître moins vite que le nombre de niveaux présents — point ouvert.

## 5. Lecture (pas un résultat jugé)

- La largeur sous absorbeur n'est pas un artefact de l'absorbeur : c'est la force de couplage du vide au dehors dans le spectre réel de la boîte fermée. En chaîne elle se lit sur un croisement (V²T) ; en 2D elle ne se lit que sur la somme.
- La chaîne fermée ne vaut comme modèle de la boîte fermée que pour les petites boîtes : au croisement, l'attendu tient aux sites de coupure 11 (3 barreaux), 13 (3 barreaux), 13 (5 barreaux) et tombe aux sites 15 (3 barreaux), 17 (3 barreaux), 20 (3 barreaux), 13 (4 barreaux), 17 (4 barreaux), 17 (5 barreaux) ; les sauts atteignent 0.5 aux sites 12, 14, 15 selon la profondeur. Au-delà, ses propres corrections d'ordre 2 sortent du domaine perturbatif (le décalage diagonal atteint l'unité vers le site 22 à 3 barreaux), et le dehors 2D est une mer, pas une échelle. Sous absorbeur cela ne pèse pas, le gel l'a jugé : le flux est absorbé avant (lecture).
- En chaîne, le temps de retour T est fini quelle que soit la longueur : le nombre de niveaux du dehors par unité d'énergie ne croît pas, le système fermé ne se désintègre jamais, il bat aux conditions de bord accordées. En 2D ce nombre croît avec la boîte, jusqu'au côté 201 où le calcul s'arrête (section 4). **Conjecture, non éprouvée au-delà** : s'il croît sans borne, chaque croisement s'affaiblit, ils se multiplient, et le grand bocal 2D tend vers une vraie désintégration au taux Γ — ce que la réduction à une chaîne ne peut pas montrer.
- Ordre de grandeur, pour ne pas surlire : avec n niveaux se partageant la force, la part des bords « accordés » croît comme √(n Γ T). À 3 barreaux Γ T = 3.1e-07 : il faudrait de l'ordre de 3e+06 niveaux pour que le vide soit mêlé à coup sûr. Dans toute boîte calculable, le vide fermé reste stable hors accidents.
- Prudence sur la littérature : « le système tronqué ne se désintègre pas » et « il se désintègre sous absorbeur » ne se contredisent pas ; en 2D s'y ajoute que la réponse du système tronqué dépend de la taille de la troncature d'une façon que l'image à un canal ne contient pas.

## 6. Limites

- Un seul désaccord en 2D fermée (le point sacrifié), trois profondeurs, côtés jusqu'à 64 en diagonalisation complète et jusqu'à 201 en creux ; boîte carrée en quanta, paroi dure : une autre forme de boîte est une autre condition à l'infini.
- V_k est une formule de premier ordre ; les niveaux à moins de 0.05 |δ| du vide sont hors fenêtre. Les barres d'erreur supposent des boîtes indépendantes.
- Le lisse Γ(E) loin de l'énergie du vide vient de la chaîne d'ordre 3, que le gel n'a jugée qu'à l'énergie du vide. L'accord de la somme 2D avec lui est un fait d'exploration, pas un énoncé gelé.
- La repondération est venue après lecture de la première passe à 3 barreaux ; les épreuves sont les trois échantillons marqués « tient ». La bande d'attente (0.85 à 1.15) est du même ordre que le bruit de deux des trois : épreuve faible prise une à une, plus nette ensemble.
- Double précision : le plus petit poids c_k² lu en diagonalisation complète vaut 2e-24, soit une composante de 1e-12, au bord de ce qu'un vecteur propre rend ; les plus petites parts y sont donc incertaines. Les sommes n'en dépendent pas (elles sont portées par les grandes parts), et dans les grandes boîtes les deux lectures indépendantes de chaque niveau s'accordent. Rien n'a été recalculé en précision étendue. Degré 9, 6 barreaux : illisible.
- Rien n'est gelé, rien n'est rejoué par machine 2. La croissance du nombre de niveaux au-delà du côté 201 est une extrapolation, et rien ne dit que la participation suive le compte.

## 7. Pièces (conteneur de machine 1, non livrées en lot)

pont_ferme_absorbeur_machine1_v1.py, pont_semiclassique_machine1_v1.py (chaîne, v1 de la note) ; pont_degres_machine1_v1.py (degrés) ; pont_2d_sacrifie_machine1_v1.py (boîte 2D, croisement) ; pont_2d_force_machine1_v1.py puis _v2.py (règle de somme, brute puis repondérée) ; pont_lisse_ordres_machine1_v1.py (ordre 1 contre ordre 3, sans bruit) ; pont_sauts_regard_machine1_v1.py (sauts de l'échelle) ; pont_2d_grand_machine1_v1.py et attendu_grand_m4_m5_cote200_machine1_v1.txt (boîtes jusqu'au côté 201) ; leurs journaux et leurs JSON ; ce script. Moteur et blocs : ceux du registre (delta 102), non modifiés.
