# Note hors chaîne — lecture des modes d'énergie négative, et jouet quantique de l'île (v1)

Machine 1, 13/11/2026, écrite après la clôture de la piste (0) (nuit bis : NON QUALIFIE).
**HORS CHAÎNE, NON OPPOSABLE.** N'engage aucun numéro, aucune manche, aucun fait de chaîne.
Suite de `note_apports_litterature_2026-11-13_v1.md` (def35e82df8b2e68). Les énoncés sont des
lectures machine 1 ; toute phrase promue en chaîne ou envoyée dehors devra être relue sur les
sources primaires (dettes au §8).

**Question posée par l'opérateur.** Reprendre la genèse : le « bocal v1 » cherchait un analogue
de laboratoire et est mort parce que le vrai bocal est conservatif et indéfini. Un analogue
conservatif existe-t-il dans une autre littérature, et que dit-elle de nos lois ?

## 1. Verdict

1. L'objet classique de la campagne (île, rivage, seuil qui dépend du désaccord, explosion en
   temps fini) est, au degré 3, un objet connu de la physique des plasmas depuis les années
   1960 et de la mécanique céleste depuis 1925 : la résonance entre un mode d'énergie positive
   et un mode d'énergie négative. Notre revue d'antériorité ne l'avait pas couverte.
2. Ce que nous avons dérivé au premier ordre en est la généralisation au degré p. À p = 3 nos
   formules redonnent les leurs (§4). Ce n'est donc pas une découverte de structure.
3. Dans ce que j'ai lu, quatre choses manquent : les lois en degré (L1, le mur), une loi
   chiffrée pour le seuil abaissé par le chaos, la structure fine du bord, et tout taux de
   fuite quantique hors de l'île.
4. La lecture donne un estimateur quantique dérivable, en forme fermée, que le jouet du §6
   vérifie : la largeur de l'état fondamental de l'île de la forme normale suit
   exp(−2 c_p I₁/ħ), et quatre absorbeurs la rendent au millième près.

## 2. Ce qui a été lu, et comment

Lecture par passes d'extraction sur le texte complet de cinq articles ; deux notices de 1973
lues en résumé seulement. Les PDF de 1995 sont des scans : plusieurs formules de Kueny–Morrison
I sont illisibles à l'extraction (détunage effectif, coefficient de couplage, éq. 79, 88, 92).
Je n'ai vu aucune figure.

- Kueny & Morrison, Phys. Plasmas 2, 1926 (1995), partie I.
- Kueny & Morrison, Phys. Plasmas 2, 4149 (1995), partie II.
- Martins, Morrison & Curry, arXiv:1605.04450.
- Arwas & Cohen, « Superfluidity in Bose-Hubbard circuits », arXiv:1612.00251.
- Casti, Morrison & Spiegel, arXiv:astro-ph/9807310 (section 4.3).
- Notices : PRL 30, 49 (1973) et Physica Scripta 7, 217 (1973), stabilisation des
  instabilités explosives par décalage de fréquence non linéaire.

## 3. Fiches

**Kueny–Morrison I.** Deux faisceaux d'ions contre-propagatifs, linéairement stables, dont
deux branches portent une énergie négative. Triplet résonant réduit à un degré de liberté. À
résonance exacte tout part à l'infini sauf l'équilibre ; désaccordé, une région stable entoure
l'origine, bornée par une séparatrice, et grandit avec le désaccord. Les amplitudes critiques
du cas intégrable sont dites connues exactement depuis 1969 (Coppi, Rosenbluth & Sudan ;
Davidson & Kaufman). Aucun terme quartique.

**Kueny–Morrison II.** Cinq ondes, trois degrés de liberté, intégrateur symplectique. Le chaos
des résonances voisines abaisse le seuil sous la valeur intégrable (|Q3| = 0.2 à A = 100,
L = 5000) ; le temps d'évasion monte à pic près d'une « séparatrice réduite » ; cet effet
croît avec la longueur d'onde. Aucune loi d'échelle. Le critère de Chirikov est cité, pas
appliqué. La diffusion d'Arnold n'est pas observée (jusqu'à environ 1e10 périodes). Le bord
n'est pas étudié comme objet (ni fractal ni criblé), seule une dépendance « en pointes » aux
conditions initiales est notée.

**Martins–Morrison–Curry.** Rappel du hamiltonien de Cherry (2:1, cubique) puis application
symplectique 4D jouet. Un seul jeu de paramètres, quelques orbites, diffusion d'Arnold
invoquée sans taux. Rien de quantitatif à reprendre.

**Arwas–Cohen.** Anneau de Bose-Hubbard à M sites ; les excitations de Bogoliubov d'un état de
courant ont des fréquences de signes mêlés hors du régime de Landau. La résonance « 1:2 »
donne H = ωJ + νI + μ I √(J/2 + I) cos φ, Cherry à ν = 0. Séparatrice explicite (leur F1),
rayon de l'île ~ (ν/μ)², évasion hyperbolique en 1/(t_e − t)². Côté quantique : simulations
à N ≤ 120 (ħ = 1/N), reproduites par un nuage semi-classique ; la survie croît avec N à
désaccord fini parce qu'une plus grande part du paquet tient dans l'île. Aucun taux tunnel.
Les termes d'ordre 4 sont négligés (supprimés en √N).

**Casti–Morrison–Spiegel.** Forme normale de Birkhoff à trois ondes, réduction à Cherry,
solutions explicites d'amplitude 1/(ξ − εt), singularité à t* = ξ/ε. Désaccordé : des
séparatrices apparaissent, sans chiffre.

**Notices 1973.** Un décalage de fréquence proportionnel au carré des amplitudes peut
stabiliser l'instabilité explosive, avec des solutions bornées, périodiques ou de type
soliton en temps. Filiation citée : 1966–1970.

## 4. Dictionnaire campagne ↔ littérature

Côté campagne : état du 12/09 (mémoire de projet), à revérifier sur pièces avant tout usage.

| Campagne | Littérature | Statut |
|---|---|---|
| île, rivage | région stable bornée par la séparatrice du triplet désaccordé | connu (K–M I) |
| pas de seuil à résonance exacte, t ~ 1/K | Cherry : amplitude 1/(ξ − εt), t* = ξ/ε | connu (1925) |
| seuil de capture s_open ∝ (\|ν\|Δ/g)^(1/(p−2)) | I_S = (4/9)(ν/μ)² à J = 0, soit amplitude ∝ ν/μ | même loi à p = 3 |
| K = g s^(p−2) paramètre unique | μ√I à p = 3 | même structure |
| tranche protégée par la phase | séparatrice non circulaire | voir ci-dessous |
| île du shift à degré pair, enveloppe périodique sous le seuil | stabilisation par décalage de fréquence non linéaire | connu (1969–1973) |
| seuil abaissé, bords criblés, îlots | séparatrice réduite par le chaos | observé, non chiffré (K–M II) |
| Chirikov sur M3–M14 (non fait) | cité, non appliqué (K–M II) | ouvert des deux côtés |
| le fantôme fuit, le jumeau non | paquet quantique dans l'île, N ≤ 120 | pas de taux (A–C) |

Deux vérifications à la main (machine 1) :

- F1 d'Arwas–Cohen à J = 0 : point selle en φ = π (ν > 0), √I_S = 2ν/(3μ), donc
  I_S = (4/9)(ν/μ)². Retrouvé.
- Énergie de la séparatrice H_S = (4/27) ν³/μ². Sur l'axe φ = 0 elle coupe I = (1/9)(ν/μ)².
  Le seuil d'amplitude varie donc d'un facteur 2 avec la phase dans Cherry. Notre « tranche
  protégée par la phase » (seuil générique 20 à 32 pour cent sous le seuil de famille) est le
  même phénomène ; le chiffre, lui, n'est pas comparé.

## 5. Ce que je n'y ai pas trouvé

Dans les cinq articles, et seulement là :

- aucune loi en degré : ni L1 (ln s* linéaire en 1/(p−2)), ni le régime du mur ;
- aucun profil d'explosion du système complet (α = 4/(p−2)) : leurs modèles sont des formes
  normales, qui donnent 1/(p−2) sur l'amplitude ;
- aucune table de parité, aucune asymétrie de signe sur les flancs ;
- aucune loi pour l'abaissement du seuil par le chaos ;
- aucun taux de fuite quantique, aucun contrôle par jumeau à signe retourné.

Ce n'est pas une preuve d'absence : soixante ans de littérature, cinq articles lus.

## 6. Jouet : l'île de la forme normale, version quantique

Script `jouet_ile_cherry_quantique_machine1_v1.py` (9b1abd9d78070be5), journal
`.log` (1439e8b554d5f7e4). Classe 3, plume machine 1, non contresigné.

**Modèle.** H = νI + μ I^(p/2) cos φ, quantifié par I = ħk : matrice tridiagonale semi-infinie,
diagonale νħk, hors-diagonale (μ/2)(ħ(k+1))^(p/2). L'ordre des facteurs est mon choix.
ν = μ = 1. État lu : celui de plus grand poids sur k = 0.

**Formule dérivée à la main.** Sous la barrière φ = π + iθ, cosh θ = (I₁/I)^((p−2)/2) avec
I₁ = (ν/μ)^(2/(p−2)). Action S = c_p I₁, c_p = ∫₀¹ arccosh(x^(−(p−2)/2)) dx, soit c₃ = 1 et
c₄ = π/2. Prédiction : Γ ∝ exp(−2 c_p I₁/ħ), préfacteur non dérivé.

**Mesure.** Absorbeur −iη x^n au-delà de I₀, échelle η = 2^e (e = −2..8), palier = cinq
valeurs consécutives de plus faible étalement, quatre absorbeurs (I₀, I_max, n) =
(4, 12, 2), (5, 14, 2), (4, 12, 3), (3, 10, 4).

| ħ | Γ, p = 3 | max/min (4 abs.) | Γ, p = 4 | max/min (4 abs.) |
|---|---|---|---|---|
| 0.200 | 1.015e-03 | 1.0019 | 1.69e-05 | 1.033 |
| 0.160 | 1.149e-04 | 1.0007 | 4.36e-07 | 1.007 |
| 0.130 | 8.06e-06 | 1.0009 | 5.90e-09 | 1.005 |
| 0.110 | 5.73e-07 | 1.0005 | 8.75e-11 | 1.002 |
| 0.095 | 3.66e-08 | 1.0002 | 1.12e-12 | 1.018 |
| 0.085 | 3.35e-09 | 1.0001 | (plancher) | 1.80 |

Pente de ln Γ en 1/ħ : à p = 3, −1.866, −1.912, −1.923 (fenêtres de plus en plus basses en ħ)
contre −2 ; à p = 4, sans le point au plancher, −2.99, −3.02, −3.03 (recalculées à la main
depuis le journal) contre −π. L'écart, 3 à 7 pour cent, se resserre quand ħ baisse ; il est
compatible avec un préfacteur en puissance de ħ.

**Cercle limite.** À E fixe, les deux solutions de la récurrence sont de carré sommable pour
p = 3 et 4 (sommes partielles stables à 1e6 termes), divergentes pour p = 2. L'opérateur
tronqué n'est donc pas essentiellement auto-adjoint dès p = 3 : c'est le visage quantique de
l'explosion en temps fini. Sans absorbeur, le résultat dépend de la troncature.

**Ce que le jouet ne dit pas.** Il n'est pas l'oscillateur de Pais-Uhlenbeck : un seul degré
de liberté, un seul secteur, l'état fondamental, ν = μ = 1. Le cercle limite n'y empêche pas
un palier propre : il n'explique donc pas à lui seul l'échec de la piste (0).

## 7. Ce que cela change

1. **Antériorité.** Toute note externe cite Cherry (1925), Kueny–Morrison (1995) et
   Arwas–Cohen, et présente le premier ordre comme une extension au degré p. Ce qui reste
   candidat : les lois en degré, le versant quantique.
2. **Chirikov.** Le chantier n'est pas tué : K–M II a laissé le calcul non fait. Il change de
   statut : c'est la suite déclarée d'un article connu, pas un terrain vierge. Je ne sais pas
   si quelqu'un l'a fait depuis 1995.
3. **Estimateur C2.** La file réclame depuis septembre un estimateur « changé et dérivé ». La
   largeur tunnel de la forme normale en est un : forme fermée, un degré de liberté, palier
   propre. À faire avant tout gel : écrire la forme normale quantique du vrai système au
   degré et à la résonance joués, puis la confronter aux ordres de grandeur de M17.
4. **Deux confrontations déjà écrites.** (a) Au degré 4 la formule donne exp(−πν/(μħ)), donc
   une loi en exp(−c/g) : c'est la forme du « plancher des Tirs », fait mesuré sans modèle.
   Coïncidence de forme, rien de plus tant que c n'est pas calculé. (b) Le jouet prédit une
   fuite maximale à la résonance exacte du canal qui fuit ; M17 ne montre pas de pic à 2.00.
   Donc soit 2:1 n'est pas le canal, soit le premier ordre ne décrit pas la fuite. La
   puissance ħ^(4–5) de K3 contredit aussi une exponentielle pure dans son régime.
5. **Maiezza–Nesti.** Leurs deux régularisations qui convergent vers des limites différentes
   se lisent comme deux extensions auto-adjointes. Hypothèse, non vérifiée sur leur modèle.

## 8. Dettes

1. Formules illisibles de K–M I (détunage effectif, seuil exact) : à relire sur le PDF.
2. Non lus : Coppi–Rosenbluth–Sudan (1969), Davidson–Kaufman (1969), Weiland–Wilhelmsson
   (1977, chap. 10), Pfirsch (1993), les deux articles de 1973 au-delà du résumé.
3. Citations postérieures à 1995 de K–M II non dépouillées (Chirikov fait depuis ?).
4. Littérature quantique du hamiltonien trilinéaire explosif : une seule recherche, sans
   résultat pertinent. Le §6 peut exister ailleurs.
5. Le dictionnaire du §4 cite l'état de la campagne de mémoire, pas sur pièces.
6. INSPIRE (dette 6.1 de la note précédente) toujours ouverte.
