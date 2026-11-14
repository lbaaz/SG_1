# Note hors chaîne — la chaîne E-A contre E-B, état par état, sur les points de M17 (v1)

Machine 1, 13/11/2026. **HORS CHAÎNE, NON OPPOSABLE, POST HOC.** Classe 3, plume machine 1
seule, non contresignée, jouée sur le conteneur machine 1 (levier X86_V4). N'engage aucun
numéro et ne touche à aucun verdict déposé. Suite de
`note_lecture_modes_energie_negative_2026-11-13_v1.md` (546c04b9e54d5f4d), dont elle corrige
le §7 (voir §6 ci-dessous).

## 1. Verdict

1. L'estimateur « dérivable » que je proposais le matin existe déjà : c'est la chaîne E-A du
   moteur v17 (`gamma_chaine`, gel 4.7). Rien de neuf de ce côté.
2. Ce qui est neuf : évaluée aux occupations **entières** des états propres 2D, la chaîne
   rend leurs largeurs à un facteur 0.50 à 1.64 près, sur 72 états-points et sept décades
   (2e-12 à 1.9e-05), aux six points de M17, sans paramètre libre.
3. L'écart d'un facteur 28 à 312 entre Γ_c et Γ_LS au run M17 n'oppose pas les deux
   estimateurs. E-A est évaluée à l'occupation **moyenne** de la graine, E-B lit l'état
   propre **modal**, et la largeur est multipliée par 20 à 25 à chaque quantum.
4. Le saut de Γ_LS à w2 = 2.05 est un changement d'état lu : (7,2) aux cinq autres points,
   (8,2) à 2.05, avec une marge de recouvrement de 0.4 pour cent.

## 2. Ce que dit le moteur (82a0be882568fe0c)

P = 5, potentiel (g/5) x⁵, canal (2,1), énergie libre −n1 + w2·n2 : le mode 1 est le fantôme.
Le saut (+2, +1) coûte δ = w2 − 2. C'est la résonance d'énergie négative de Cherry, au degré 5.
g est réglé par point, proportionnel à |δ| (g = K_ν/κ) : aucun pic n'est attendu à 2.00.

E-A : chaîne tridiagonale le long du canal depuis le site de la graine, diagonale m·δ, saut
t_m, bord absorbant. E-B : H 2D (N = 60) avec absorbeur, largeur de l'état de plus grand
recouvrement avec la graine cohérente.

## 3. Mesure

`comparaison_par_etat_machine1_v1.py` (4eaef82543e4f76f), journaux A (60f09b5a752333e0) et B
(123b6760ece603e3). H_2D du moteur au réglage du run (N = 60, r_c = 40, η = |δ|/8, fraction
0.70), diagonalisé une fois par point. Les quatorze états de plus grand recouvrement sont
étiquetés par J = n1 − 2·n2 et k = ⟨n2⟩. `gamma_chaine` du moteur est appelée à (J + 2k, k).

Les états sont des quasi-états de Fock : écart-type de J entre 0.008 et 0.115, ⟨n2⟩ entier à
0.1 près. La graine s'étale sur eux avec des recouvrements de 0.02 à 0.04 chacun.

| w2 | graine (n1, n2) | état lu | marge rang 0 / rang 1 | Γ_2D lu | Γ chaîne | chaîne/2D (lu) | chaîne/2D (12 états) |
|---|---|---|---|---|---|---|---|
| 1.95 | (7.594, 2.568) | (7,2) | 1.034 | 2.162e-10 | 1.771e-10 | 0.819 | 0.499 à 0.878 |
| 1.97 | (7.765, 2.568) | (7,2) | 1.013 | 1.298e-10 | 1.073e-10 | 0.827 | 0.521 à 0.872 |
| 1.98 | (7.851, 2.568) | (7,2) | 1.003 | 8.441e-11 | 7.186e-11 | 0.851 | 0.579 à 0.890 |
| 2.02 | (8.204, 2.568) | (7,2) | 1.031 | 6.663e-11 | 7.321e-11 | 1.099 | 0.931 à 1.132 |
| 2.03 | (8.294, 2.568) | (7,2) | 1.019 | 9.164e-11 | 1.090e-10 | 1.190 | 1.027 à 1.259 |
| 2.05 | (8.477, 2.568) | (8,2) | 1.004 | 2.665e-09 | 3.924e-09 | 1.472 | 1.281 à 1.642 |

« 12 états » : ceux dont Γ_2D dépasse dix planchers (1.33e-12). Ancre : mon Γ_2D lu redonne
le Γ_LS du run à mieux que 2 pour cent aux six points (2.162, 1.298, 8.442, 6.562, 9.008 e-11
et 2.661e-09 au run).

À 2.05 l'état (7,2) existe toujours : Γ_2D = 1.199e-10, dans la continuité de 2.03. Le facteur
30 du run se décompose en 22 (changement d'état) fois 1.3 (continuité).

Largeur par quantum, à 2.02 et n2 = 2 : 2.4e-12, 6.7e-11, 1.46e-09, 2.57e-08 pour
n1 + n2 = 8, 9, 10, 11, soit des rapports 28, 22, 18.

## 4. Deux coupes

**Résonant seul.** `bissection_chaine_2D_machine1_v2.py` (7cb9dcf62eccf90b), journal
(2fea83deeeb6ced7). H 2D réduit à sa diagonale libre et aux seuls sauts ±(2,1), même graine,
même absorbeur. État lu : 1.864e-10, 7.708e-11, 4.365e-09 à 1.95, 2.02, 2.05. Le H complet
vaut 1.16, 0.86, 0.61 fois cela. La fuite est donc celle du canal 2:1 au premier ordre ; les
termes non résonants la corrigent d'un facteur signé par δ. La chaîne vaut 0.95, 0.95, 0.90
fois le 2D résonant seul.

**Second ordre.** `chaine_second_ordre_machine1_v1.py` (b347c0edb9af04d0), journal
(04d02938789de550). Ajouter à la diagonale de la chaîne le décalage Σ2 du moteur corrige dans
le bon sens mais trop fort : chaîne/2D passe de 0.50–1.64 à 0.58–1.83. Le second ordre n'est
pas dérivé (le saut effectif n'est pas corrigé).

## 5. Ce que cela n'établit pas

- Post hoc, une seule plume, une seule machine, un seul η (k = 3). L'instrument E-B est NON
  QUALIFIE au centième (nuit bis) ; un accord à un facteur 2 est ce qu'il permet de dire.
- Les résiduels par point (0.82 sous 2.00, 1.1 à 1.5 au-dessus) ne sont pas expliqués en
  chiffre.
- Rien n'est dit de la fuite d'un paquet cohérent : c'est une somme sur des états dont les
  largeurs couvrent sept décades.
- Le verdict PAS DE SIGNAL de M17 n'est pas touché. Sa lecture, elle, est à reprendre : P3
  et P6(i) rangeaient Γ_LS, qui change d'état lu d'un point à l'autre.

## 6. Corrections à mes écrits du jour

- Note 546c04b9, §7.3 : l'« estimateur C2 candidat » est E-A, déjà au moteur.
- Note 546c04b9, §7.4(b) : « soit 2:1 n'est pas le canal, soit le premier ordre ne décrit pas
  la fuite ». Réponse : 2:1 est le canal, le premier ordre décrit la fuite à un facteur 2.
  L'absence de pic à 2.00 vient du réglage de g, proportionnel à |δ|.

## 7. Ce que je propose

Un gel, à deux plumes, d'une prédiction hors échantillon : la chaîne aux sites entiers prédit
les largeurs 2D état par état à un facteur 2 près, sur un (w2, g) que personne n'a
diagonalisé. Machine 2 certifie et joue. C'est la première prédiction quantique de la
campagne dont l'issue qui la falsifie s'écrit en une ligne.

## 8. Pièces

Lot `lot_machine1_2026-11-13_chaine_EA_par_etat_v1.zip`, manifeste joint.
`chaine_aux_sites_entiers_machine1_v1.py` (aa74f6fcaeff6a73) et son journal
(5fe02a8e2b6a2812) : premier passage, trois points. `lire_m17_EA_EB_machine1_v1.py`
(85ba4aba558377c2) : lecture de Γ_c et Γ_LS dans les JSON du run. Moteur et run : ceux du
registre et du lot M17 détenus par machine 1.
