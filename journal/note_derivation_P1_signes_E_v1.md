# Note de dérivation P1 — le signe de E par famille de résonance (v1)

Machine 1, 02/08/2026. **Hors chaîne.** À re-dériver indépendamment par
machine 2 avant tout gel de manche — c'est le seul double conservé sous le
plan d'action (§5.0 du suivi 02b).

## 0. Statut épistémique — à lire d'abord

Cette note est écrite **après** lecture des onze signes de M12. Elle n'est
pas une prédiction de ces signes ; elle est une dérivation **confrontée** à
eux : les onze points sont l'ensemble d'entraînement, pas la confirmation.
Le contenu opposable de la note est le §6 — des prédictions en points
**neufs**, gelées ici avant toute mesure. Le §8 liste ce qui tuerait la
dérivation.

## 1. La règle de sélection généralisée (dérivée)

Interaction V = (g/p)·xᵖ, x = x₁ + x₂ : le multinôme donne des termes
x₁ᵏx₂ˡ, k + l = p. En variables angle, x_j^m ne génère que les harmoniques
e^{ik′θⱼ} avec |k′| ≤ m et **k′ ≡ m (mod 2)** (puissances de cosinus). Un
terme séculaire à la résonance ω₂ = n/m (fraction réduite, ordre q = n + m)
exige la combinaison k′ω₁ = l′ω₂, minimale (k′, l′) = (n, m). Au **premier
ordre en g** (un seul sommet) il faut donc k ≥ n, k ≡ n (2), l ≥ m,
l ≡ m (2), k + l = p — d'où p − q = (k−n) + (l−m) = pair + pair :

> **La résonance d'ordre q agit au premier ordre sur le degré p
> ssi p ≥ q et p ≡ q (mod 2).**

Réciproque : si p ≥ q et p ≡ q (2), poser (k, l) = (n + (p−q), m). ∎

**Corollaires.**
(a) À ω₂ = 2 (q = 3) : premier ordre ssi p impair — **la loi des porteurs
(M6) est le cas particulier q = 3.**
(b) À l'ordre r en g : r sommets, quanta ≤ rp, parité totale ≡ rp (mod 2).
Donc à **p pair, une résonance d'ordre q impair n'est atteinte à AUCUN
ordre en g** — seulement via sa représentation doublée (2n : 2m), d'ordre
effectif 2q (c'est le « 2:1 faible via (4,2), second ordre » du système
quartique, retrouvé).
(c) À p impair, q pair : premier ordre interdit (parité) ; second ordre
(deux sommets, parité paire) permis si 2p ≥ q.

**Table des ordres minimaux en g, familles de M12 × degrés (4, 5, 7) :**

| famille | q | p = 4 | p = 5 | p = 7 |
|---|---|---|---|---|
| 2:1 (ω₂ = 2) | 3 | 2ᵉ (via 4:2) | **1ᵉʳ** | **1ᵉʳ** |
| 3:2 (ω₂ = 1.5) | 5 | jamais | **1ᵉʳ** | **1ᵉʳ** |
| 5:2 (ω₂ = 2.5) | 7 | jamais | 3ᵉ | **1ᵉʳ** |
| 3:1 (ω₂ = 3) | 4 | **1ᵉʳ** | 2ᵉ | 2ᵉ |
| 8:3 (ω₂ = 8/3) | 11 | jamais | 3ᵉ | 3ᵉ |

## 2. Le mécanisme du signe

Trois pièces, toutes **établies** — la composition seule est neuve :

1. **Les résonances creusent** (M5) : le point résonant est un canyon dans
   le fond universel ⇒ contribution δ_p ≤ 0 à ln s\*_p au voisinage d'une
   famille, avec la hiérarchie premier ordre ≫ second ≫ troisième
   (empiriquement ancrée : canyons profonds à 2:1 aux degrés impairs,
   faibles ailleurs).
2. **E hérite linéairement** : E = δ₄ − 2.25·δ₅ + 1.25·δ₇ + E_fond, où
   E_fond est la part lisse (l'échec non résonant de la loi affine), et
   seuls les δ_p **permis** par la table du §1 comptent.
3. **La saturation 3:1** : au degré 4, le canal (3,1) de premier ordre est
   auto-saturé — pas de suppression du seuil (mécanisme GSTZ, vérifié dans
   le système quartique, note §3(c)) ⇒ **δ₄ ≈ 0 près de 3:1 malgré le
   premier ordre**.

D'où, famille par famille (|δ| pour les valeurs absolues) :

- **2:1 et 3:2** (seuls p = 5, 7 au premier ordre) :
  E_rés ≈ 2.25|δ₅| − 1.25|δ₇| > 0 **tant que |δ₇|/|δ₅| < 9/5** — signe
  **positif** sous hypothèse de canyons comparables.
- **5:2** (seul p = 7 au premier ordre, p = 5 relégué au 3ᵉ) :
  **E_rés ≈ −1.25|δ₇| < 0, inconditionnellement.** La famille d'ordre 7 est
  la seule où E est forcé négatif — et elle mesure **le canyon p = 7 seul**,
  au facteur 1.25 près : un spectromètre pur du degré 7.
- **3:1** (δ₄ saturé ; p = 5, 7 au second ordre, faibles) :
  E_rés ≈ 2.25|δ₅″| − 1.25|δ₇″|, **petit et positif** ⇒ E ≈ E_fond :
  **plat**, sans structure en d — la platitude est la signature de la
  saturation.
- **8/3** (troisième ordre partout, rayon minuscule) : **aucun canyon de E**
  — la zone 2.63–2.70 doit suivre l'interpolation lisse queue-5:2 → plateau-3:1.

## 3. Confrontation aux onze points (entraînement, pas confirmation)

| famille | points (ω₂ → E) | prédit | mesuré |
|---|---|---|---|
| 2:1 | 1.76 → +0.81 · 1.84 → +0.96 · 1.86 → +1.02 · 2.22 → +0.41 · 2.27 → +0.17 | + | **5/5 +** |
| 3:2 | 1.73 → +0.76 | + | **1/1 +** |
| 5:2 | 2.42 → −0.15 · 2.55 → −0.48 | **−** | **2/2 −** |
| 3:1 | 2.72 → +0.52 · 2.78 → +0.52 · 2.80 → +0.54 | + (plat) | **3/3 +, plat** |

**11/11 signes.** Et les structures secondaires tombent avec :

- **Le fait saillant est dérivé** : les deux seuls négatifs sont les deux
  points d'ordre 7 — l'unique famille où seul p = 7 mord au premier ordre.
- **Le saut +1.0007 (2.55 → 2.72)** : sortie du rayon 0.03 de 5:2
  (E = −1.25|δ₇|) vers le bassin 3:1 saturé (E ≈ E_fond > 0) — un saut
  **positif**, de l'ordre du canyon quitté plus le fond retrouvé.
- **Le zéro encadré (2.27, 2.42)** : transition famille positive → famille
  négative ; le zéro est un point d'équilibre de queues, pas une structure
  propre.
- **Monotonies internes** : 2:1 gauche +0.81 → +1.02 en approchant, droite
  +0.41 → +0.17 en s'éloignant ✓ ; 5:2 : |E| croît de 0.15 à 0.48 en
  approchant ✓.
- **La platitude du groupe droit** : étendue 0.026 (0.517–0.543) sur
  d/r ∈ [1.67, 2.33], contre 0.85 d'étendue dans la famille 2:1 — la
  signature de saturation prédite au §2.
- **La contre-paire de P-M12d, requalifiée** : (2.22 : +0.41) contre
  (1.76 : +0.81) à d comparable n'est pas une « monotonie cassée en d/r »,
  c'est **l'asymétrie gauche-droite du canyon 2:1 vue à travers E** —
  sous-question ouverte (§5), pas une anomalie.

**Pourquoi la classe affine devait mourir** : aucune fonction lisse de
u_p = 1/(p−2) ne peut encoder « mord 5 et 7 mais pas 4 » — la sélection est
une fonction de la **parité** de p, orthogonale à toute forme affine en u_p.
La réfutation de M12 n'est pas un accident de précision ; en territoire
résonant, la classe ne pouvait pas être vraie.

## 4. Estimation de magnitude (sanité, une seule)

Près de 2:1, si |δ₅| ≈ |δ₇| ≈ |δ| : E ≈ |δ| — E lit directement la
profondeur du canyon. M5 consignait Q(5) = 4.4 au fond, soit
|δ₅(0)| ≈ ln 4.4 ≈ 1.5 ; E(1.86) = 1.02 à d = 0.14 du centre : même ordre,
décroissance plausible. *Caveat anti-Franken : Q vient de la chaîne M5 —
ordre de grandeur cité, aucun chiffre importé.*

## 5. Ce que la dérivation ne fixe pas

Les **magnitudes** (elles demandent E_fond(ω₂) — la question A(ω₂) — et les
profondeurs de canyon par degré) ; l'**asymétrie gauche-droite** à 2:1
(trois causes possibles indiscernables à ce stade : canyons plus faibles à
droite, ratio |δ₇|/|δ₅| variable, ou δ₄ de second ordre asymétrique) ; le
**profil** en d à l'intérieur d'un rayon ; la borne |δ₇|/|δ₅| < 9/5 est
supposée aux familles 2:1 et 3:2, pas dérivée.

## 6. PRÉDICTIONS OPPOSABLES — points neufs (l'attente à geler pour la manche)

Signes et structures ; magnitudes en inégalités seulement.

- **P1-a (5:2, le spectromètre p = 7).** Points neufs dans 2.44–2.56 :
  E < 0 partout, |E| **strictement croissant** vers 2.50 de chaque côté, et
  |E(2.48)| > 0.48 (plus profond que le point mesuré le plus proche).
- **P1-b (8/3, le falsifieur net).** Points à 2.63, 2.66, 2.68, 2.70 :
  **aucun canyon** — les valeurs suivent l'interpolation lisse entre la
  queue 5:2 et le plateau 3:1, écart < 0.15 ; en particulier **pas
  d'excursion localisée** autour de 2.667.
- **P1-c (le zéro).** Sur [2.27, 2.42], E est **monotone décroissant** aux
  points neufs ; un unique zéro, dans l'intervalle.
- **P1-d (droite de 3:1).** À ω₂ ∈ {3.10, 3.20} (hors grille M12) :
  E > 0, et le plateau se prolonge (étendue de part et d'autre de 3.0
  < 0.15) — la saturation n'a pas de côté.
- **P1-e (miroirs à 2:1).** Paires (2 − d, 2 + d), d ∈ {0.10, 0.18} :
  les quatre E > 0, et E(gauche) > E(droite) aux deux d — l'asymétrie est
  une **structure**, pas un accident des points M12.

Une manche courte sous régime O couvre P1-a/b/c avec ~8 points neufs en
réutilisant l'appareil M12 tel quel ; P1-d/e sont extensibles ou
reportables.

## 7. Données demandées à machine 2 (au lieu de recalculer)

1. **Le texte du gel M12 v4** (`bf9866a7`) — sections catalogue de
   résonances (liste (n:m, rayon)) et règle d'assignation. Je n'ai vérifié
   que la cohérence interne des blocs du primaire ; la table du §1 doit être
   confrontée au **catalogue gelé** (en particulier : 5/3 (q = 8) y
   figure-t-il, et avec quel rayon ? Ma dérivation le prédit faible —
   second ordre partout — donc absent ou sans morsure).
2. **M5/M6 — profondeurs de canyon par degré** : Q(3) = 57.5 et Q(5) = 4.4
   sont consignés à 2:1 ; existe-t-il une mesure équivalente à **p = 7**
   (et/ou p = 4) à 2:1 ? Et à 3:2, si mesurée. C'est la borne
   |δ₇|/|δ₅| < 9/5 du §2 qui en dépend.
3. **Si disponible sans effort** : les cartes K(ω₂) par degré (JSON M1/M3)
   — lecture qualitative des creux par famille, étiquetée EXPLORATOIRE,
   conventions déclarées, aucune mise en regard chiffrée inter-chaînes.

## 8. Ce qui tuerait la dérivation

Un signe positif robuste au cœur de la famille 5:2 en points neufs ; un
canyon net de E à 8/3 ; une structure forte en d dans le groupe 3:1 ; ou un
catalogue gelé dont les familles contredisent la table du §1. Chacun est un
falsifieur franc — c'est ce qui rend la manche courte digne d'être jouée.

---

*v1, machine 1. Prochaine étape : re-dérivation indépendante machine 2
(§1–§2 suffisent — la table et les trois signes de famille doivent tomber
pareil), puis gel de la manche courte sur le gabarit M12.*
