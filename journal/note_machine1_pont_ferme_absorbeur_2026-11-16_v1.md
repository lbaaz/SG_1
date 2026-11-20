# Le pont entre la largeur sous absorbeur et le système fermé — note d'exploration

Machine 1, 2026-11-16 (soir). **Hors chaîne, classe 3.** Chaîne à une dimension seule : aucune 2D, aucun run, aucun gel, machine 2 non consultée. Ouverture : l'opérateur a écrit « On peut avancer sur la recherche là ? » (21 h 39) ; machine 1 a choisi la question.

## La question

Tous les actes répètent : « rien n'est dit de la durée de vie du système fermé ». La chaîne fermée (coupée au site N, sans absorbeur) est réelle symétrique : spectre discret, aucune largeur. Que devient Γ ?

## Le résultat

Dans la chaîne fermée, l'état du site 0 est couplé aux niveaux de la région d'après la barrière par un élément V, lu comme la demi-largeur du croisement évité quand on fait défiler la condition de bord au bout de la chaîne. Sur 136 croisements (les 16 cellules lisibles du gel « largeur du vide », premier ordre, neuf coupures N de 25 à 40) :

**Γ = V² · T**, où T est le temps classique d'aller et retour entre la sortie de la barrière et le bout de la chaîne, T(E) = 2 ∫ dm / √(4 t(m)² − (E − m δ)²), calculé sur les sauts du moteur sans rien lire du spectre.

| barreaux | Γ sous absorbeur (de … à) | V (de … à) | 2π / (T·|δ|) | ln(V²T / Γ) (de … à) |
|---|---|---|---|---|
| 3 | 5.0e-10 … 3.0e-09 | 8.1e-07 … 4.9e-06 | 2.838 … 2.905 | +0.0155 … +0.0171 |
| 4 | 1.1e-11 … 6.6e-11 | 1.2e-07 … 7.4e-07 | 2.903 … 2.989 | +0.0098 … +0.0134 |
| 5 | 2.3e-13 … 1.4e-12 | 1.8e-08 … 1.1e-07 | 2.959 … 3.062 | +0.0068 … +0.0084 |
| 6 | 4.4e-15 … 2.6e-14 | 2.5e-09 … 1.5e-08 | 3.008 … 3.100 | +0.0057 … +0.0071 |

L'écart va de 0.0057 à 0.0171 en logarithme et diminue quand la barrière s'allonge, comme une relation semi-classique doit le faire. Il est le même aux quatre désaccords à profondeur égale, et il suit la coupure N.

## Ce qui a été faussé en chemin

L'attendu écrit AVANT le calcul prenait pour espacement D la demi-distance aux deux niveaux voisins (règle d'or à spectre discret, Γ = 2πV²/D). Il tombe : 2πV²/D dépasse Γ de +0.112 à +0.223 en logarithme, et de plus en plus avec la profondeur. Les différences centrées à 5 et 7 points font pire (+0.196 à +0.280 ; +0.207 à +0.294). La lecture par le temps classique est donc venue APRÈS avoir vu les nombres ; ce qui la soutient est qu'elle n'a aucun paramètre et qu'elle rend à la fois la profondeur, le désaccord et la coupure. Cause probable de l'échec des voisins, non éprouvée : près de l'énergie du vide le spectre mêle les niveaux de la région de fuite et les états localisés sous la barrière (une échelle de pas |δ|).

## Ce que cela dit du système fermé (lecture, pas un résultat jugé)

- Le temps T est FINI parce que la fuite classique atteint l'infini en temps fini (l'explosion de la branche classique de la campagne). C'est aussi pourquoi le hamiltonien fermé n'est pas essentiellement auto-adjoint (fait connu, note d'antériorité, section 3) : il faut dire ce que devient ce qui arrive à l'infini.
- Si rien ne revient (condition sortante, ce que fait l'absorbeur) : le vide se vide au taux Γ.
- Si tout revient (condition réfléchissante, une extension auto-adjointe, une troncature) : le vide ne se désintègre pas. Il est mêlé aux états de fuite à hauteur de (V/écart)², et ne bat pleinement qu'aux conditions de bord accordées à V près.
- Exemple, MG3 (N = 25) : Γ = 2.96e-09, T = 120, V = 4.92e-06, espacement des niveaux de fuite 2π/T = 2.905 |δ|. Mélange pour un écart de |δ| : (V/|δ|)² = 7.5e-08. Part des conditions de bord qui accordent : de l'ordre de 2V/(2π/T) = 1.9e-04. Période du battement quand c'est accordé : π/V = 6.4e+05.
- « Métastable » et « ne se désintègre pas » ne se contredisent donc pas : ce sont deux conditions à l'infini pour le même nombre. C'est une réponse chiffrée, dans notre modèle, à ce que Maiezza et Nesti observent dans le leur (survie qui plafonne et oscille, irrégularités à certains couplages, deux régularisations qui ne convergent pas vers la même limite).

## Limites

- Chaîne à une dimension, premier ordre. À l'ordre 3 la première passe donne un rapport 2πV²/(Γ|δ|) voisin (de 2.725 à 3.139 sur 130 croisements hors MG3, contre 2.794 à 3.082 au premier ordre). À MG3 la chaîne d'ordre 3 se dégrade quand la coupure s'allonge (N = 25 : 2.782, N = 27 : 2.765, N = 29 : 2.732, N = 31 : 2.726, N = 33 : 2.679, N = 35 : 2.536, N = 37 : 1.347) : ses sites lointains sortent sans doute du domaine perturbatif (lecture non éprouvée). Le temps classique n'a pas été calculé à l'ordre 3.
- Rien en deux dimensions : la 2D fermée a plus d'un canal vers l'infini, et une boîte n'a pas de paramètre de bord continu. C'est le test qui compte, et il demande un gel.
- La relation est connue dans son principe (taux de fuite = couplage² × temps de retour) ; ce qui est à nous est le nombre, et le fait que T soit un temps de fuite classique fini, de la même nature que l'explosion en temps fini de la branche classique.
- Lecture après coup pour le choix de T (voir plus haut). Une seule forme de chaîne ; aucune 2D ; aucun énoncé gelé.

## Pièces (conteneur de machine 1, non livrées en lot)

pont_ferme_absorbeur_machine1_v1.py / .log / pont_v1.json (première passe) ; pont_semiclassique_machine1_v1.py / .log / pont_semiclassique_v1.json (seconde passe) ; ce script.
