# Note de dérivation P1 — le signe de E par famille de résonance (v5)

Machine 1, 02/08/2026. **Hors chaîne.** **v5 remplace v4** (`a056878b`).
Changement unique : **la prédiction P1-a est CONFIRMÉE** (M14, gel
`273d0a53`, JSON `68df6576`, delta 50) — P-M14a NÉGATIF RÉSOLU (2 398× et
37 152× la barre), P-M14b′ CANYON-E. **La chaîne de la dérivation est
complète** : étage A hors échantillon, étage B favorable à 2:1 ET au site
5:2, H-SAT mesurée, le signe au cœur mesuré. La forme du creux mesurée
n'est PAS celle de l'attente (asymétrie, argmin 2.52, 2.50 perdu) —
fait neuf consigné sans lecture (delta 50.3). Le reste inchangé de la v4.

## 0. Statut épistémique

**Étage A (sélection par parité) : ACQUIS.** Dérivé (§1), contrôlé par un
chemin indépendant qui ne partage rien avec la dérivation (FFT 2D,
machine 2 §2), et **vérifié hors échantillon 5/5** sur les archives M5/M6
(machine 2 §3, lecture ordinale) : canyons à 2:1 aux trois degrés impairs,
minimum exactement en 2.00 ; traversée strictement monotone aux deux degrés
pairs ; séparation ordinale ×41. **Deux sources hors échantillon
indépendantes** (N-2) : le corpus M5/M6 — dont la loi des porteurs est une
lecture, pas un témoin séparé — et le 2:1-faible du système quartique.
**La règle n'est plus une reconstruction post-hoc des onze signes de M12 —
elle prédit des données qu'elle n'a pas vues.**

**Étage B (hiérarchie des amplitudes) : testée TROIS fois, trois fois
favorablement.** Non dérivée, contexte hostile (au seuil, g·s\*^(p−2) = K
d'ordre 1) — mais : (i) j = 1 contre j = 2 à 2:1 (séparation ×41) ;
(ii) H-SAT mesurée au site 3:1 ; (iii) **le signe au cœur de 5:2 :
NÉGATIF RÉSOLU (M14)** — le terme (3, 1) de p = 5 est bien sous 5/9 du
terme (1, 1) de p = 7, là où ça compte.

**H-SAT (saturation 3:1) : MESURÉE DANS LA CHAÎNE** (M13-L, verdict
LISSE — delta 49). Le verdict est opposable au même titre qu'un verdict
de manche (juge antérieur aux runs, appartenance mécanique, plancher en
comptes) ; la borne de résolution D ≲ 0.08 en ln est une **estimation
post-hoc étayée**, pas un résultat gelé (note R-3). Les 3 signes du
groupe 3:1 reposent désormais sur un mécanisme mesuré.

Les onze points M12 restent l'ensemble d'entraînement. L'opposable est aux
§6 (points neufs) et §5 (M13).

## 1. La règle, corrigée : le rang est un couple (r, j)

Contrainte générale (machine 2, re-vérifiée ligne à ligne par machine 1
avant adoption) : la famille d'ordre q agit à l'ordre r en g via sa
j-ième harmonique ssi

> **j·q ≤ r·p et j·q ≡ r·p (mod 2).**

Rien n'est « jamais » interdit — tout devient accessible à r assez grand.
Le premier ordre (r = 1, j = 1) redonne exactement la règle de la v1 :
p ≥ q et p ≡ q (mod 2), dont la loi des porteurs est le cas q = 3.

**Table des rangs minimaux (r, j) — familles × degrés :**

| famille | q | p = 4 | p = 5 | p = 7 |
|---|---|---|---|---|
| 2:1 | 3 | (2, 2) | **(1, 1)** | **(1, 1)** |
| 3:2 | 5 | (3, 2) | **(1, 1)** | **(1, 1)** |
| 5:2 | 7 | (4, 2) | (3, 1) | **(1, 1)** |
| 3:1 | 4 | **(1, 1)** | (2, 1) | (2, 1) |
| 8:3 | 11 | (6, 2) | (3, 1) | (3, 1) |

**Défaut D1 de la v1 (aucun numéro E — E18, confirmé machine 2)** : les
trois « jamais » (3:2, 5:2, 8:3 à p = 4) étaient faux — la v1 appliquait
le mécanisme d'harmonique doublée à 2:1 et l'oubliait pour les autres
familles impaires. Incohérence interne, hors chaîne, attrapée par la
re-dérivation machine 2 (FFT + formule) avant tout gel.

**Conséquence sur l'argument de classe** : « aucune fonction lisse de u_p
ne peut encoder *mord 5 et 7 mais pas 4* » s'appuyait sur des zéros exacts.
Version corrigée : la sélection place p = 4 au rang (3, 2) ou pire aux
familles impaires — **nul au premier ordre, négligeable sous étage B**.
L'argument survit, moins tranchant.

**Le raffinement mesuré (machine 2 §4b), adopté** : la suppression est
gouvernée par **j, l'indice d'harmonique, pas par r**. Datum : à 2:1,
p = 6 est au rang **(1, 2)** — premier ordre en g — et ne montre rien
(écart ordinal 0.004), quand p = 5 et 7 en (1, 1) creusent (0.80, 0.49).
Consigné comme fait ; aucun mécanisme théorisé ici.

## 2. Le mécanisme du signe, par étage

E = δ₄ − 2.25·δ₅ + 1.25·δ₇ + E_fond, δ_p ≤ 0 aux familles **permises au
rang (1, 1)** (étage A), les autres rangs négligés (étage B).

- **2:1 et 3:2** — (1,1) à p = 5 et 7, rien à p = 4 avant (2,2)/(3,2) :
  E_rés = 2.25|δ₅| − 1.25|δ₇| > 0 **ssi |δ₇|/|δ₅| < 9/5** — borne non
  dérivée, ordinalement du bon côté à 2:1 (~0.61, chaînes M5/M6, facteur 3
  de marge), **à mesurer dans la chaîne de la manche qui s'en servira**.
- **5:2** — (1,1) à p = 7 seul, p = 5 relégué en (3,1) :
  E_rés = −1.25|δ₇| + 2.25|δ₅⁽³,¹⁾|. **Négatif ssi |δ₅⁽³,¹⁾|/|δ₇| < 5/9**
  (forme dérivée, mesurable — N-1 ; « négligeable » est suffisant, pas
  nécessaire). **CONFIRMÉE (M14, delta 50)** : les six E mesurés de la
  fenêtre sont négatifs, les deux intra survivants résolus à 2 398× et
  37 152× ; CANYON-E, argmin 2.52. **La forme mesurée est un fait neuf
  sans lecture** : |E| décroît en approchant du site par la gauche
  (0.038 à 2.48, minimum du jeu), plonge à 0.561 en 2.52, et le centre
  2.50 est perdu par le mécanisme E27 à p = 5 (rang (3, 1)) — la
  résonance structure le dessous du seuil au rang relégué pendant que le
  rang (1, 1) creuse E. Le ratio |δ₅|/|δ₇| reste NON mesuré (2.50 mort).
- **3:1 — LE TROU (machine 2 §6, adopté tel quel).** Rang (1,1) à p = 4 :
  le couplage le plus fort possible, le même rang que les canyons
  impairs à 2:1. **La règle nue prédit ici le canyon le plus profond du
  jeu — et la mesure voit un plateau** (+0.517/+0.519/+0.543, étendue
  0.026). La v1 comblait par la saturation GSTZ (« vérifiée dans le
  système quartique ») : hypothèse **importée d'une autre chaîne**, jamais
  testée dans celle-ci, qui contredit la prédiction la plus forte de la
  règle. Nom au registre : **H-SAT** — depuis M13-L : **mesurée**. Le profil
  s\*₄ agrégé (11 survivants, deux géométries) est strictement monotone à
  travers 3.00 ; tout creux centré au site de classe mesurée (unimodal,
  demi-largeur ≥ 0.03) a D ≲ 0.08 en ln — exclusion ×6 à ×35 contre les
  canyons impairs. Échappatoires déclarées : demi-largeur < 0.02 ; creux
  décentré logé dans un trou de E.
- **8/3** — (3,1)/(3,1)/(6,2) : rien aux rangs bas ⇒ pas de canyon de E
  sous étage B. Falsifieur d'étage B, pas d'étage A.

## 3. Confrontation aux onze points — 8 prédits, 3 expliqués

| famille | points → E | statut |
|---|---|---|
| 2:1 | 1.76/+0.81 · 1.84/+0.96 · 1.86/+1.02 · 2.22/+0.41 · 2.27/+0.17 | **prédits** (A + B : borne 9/5) |
| 3:2 | 1.73/+0.76 | **prédit** (idem) |
| 5:2 | 2.42/−0.15 · 2.55/−0.48 | **prédits, et le cœur MESURÉ** (M14 : NÉGATIF RÉSOLU, six E < 0) — le fait saillant dérivé, désormais testé |
| 3:1 | 2.72/+0.52 · 2.78/+0.52 · 2.80/+0.54 | **expliqués par un mécanisme mesuré** — saturation du seuil, M13-L LISSE (delta 49) ; le dessous criblé reste consigné à part (delta 48.3) |

**N-3, déclaré : E_fond fait le gros du travail.** Dans le groupe 3:1, le
terme résonant est nul sous H-SAT, donc E ≈ E_fond ≈ **+0.52** — et un
fond positif de cette taille **suffit à lui seul à rendre positifs les
neuf signes positifs**, sans aucune dérivation. **Le contenu discriminant
de cette note se réduit aux deux négatifs de 5:2** (plus l'étage A hors
échantillon). E_fond est désormais **lisible** : H-SAT mesurée le livre —
E_fond ≈ +0.52 sur le groupe droit. Le contenu discriminant restant de
cette note : les deux négatifs de 5:2 — d'où P1-a.

**N-4, l'explication du saut est RETIRÉE.** La v1 (héritée en v2) lisait
le saut +1.0007 (2.55 → 2.72) comme la sortie du rayon 5:2 — le canal 7.
La décomposition de l'artefact dit le contraire :
d(ln s\*₄) = +1.0155, −2.25·d(ln s\*₅) = −0.2829, +1.25·d(ln s\*₇) =
+0.2681 — **le saut est à 101 % le canal 4 seul**, les canaux 5 et 7 se
compensant à −0.0148 près (certification machine 2, §9). Fait de
remplacement, consigné : entre 2.55 et 2.67, **s\*₄ fait un facteur
2.59** (2.8812 → 7.4626), seul des trois degrés, **sans aucune famille de
rang (1,1) au catalogue pour p = 4 dans [1.73, 2.82]** — un pas non
catalogué. Question ouverte ; une localisation à bas coût existe (balayage
p = 4 sur [2.50, 2.72] en régime E, une fois ratifié) — hors du périmètre
de M13, qui doit seulement y être robuste (PAS ≠ CREUX, critère ordinal).

Structures secondaires restantes : zéro encadré, monotonies internes,
platitude du groupe droit, contre-paire requalifiée en asymétrie
gauche-droite — inchangées, avec la même dépendance : celles du groupe
droit tiennent **sous H-SAT**.

## 4. Pourquoi la classe affine devait mourir (version corrigée)

La sélection est une fonction de la parité et du rang, orthogonale à toute
forme affine en u_p : en territoire résonant, la classe ne pouvait tenir
que si **tous** les creux de rang (1,1) étaient nuls — contredits par M5,
M6 et M12. Formulation affaiblie par rapport à la v1 (plus de zéros exacts
à p pair), conclusion intacte.

## 5. Le test de H-SAT : l'arc M13 → M13b → M13-L (JOUÉ, fermé)

Deux manches de balayage (M13 `70fe5611`, M13b `22fa1760`) : 22 recherches
p = 4 toutes abouties, profils bruts strictement croissants, mais deux
NON CONCLUANT DE GÉOMÉTRIE — G6 fauche des lignes de façon non confinée
au site (l'ensemble sous-seuil est ENTRELACÉ au centième, delta 48.3,
matière consignée sans porte). **M13-L** (gel `f779bbe3`, delta 49) :
lecture agrégée mécanique à zéro degré de liberté sur l'union des 11
survivants, juge antérieur aux runs, fermée au bit par double
implémentation — **verdict LISSE. H-SAT est mesurée.** Précisions de la
certification, intégrées : la calibration de forme est le **flanc
gauche** des canyons 2:1 (le droit donne 18–60 % ; l'asymétrie est un
fait de M5) ; le plancher de rugosité 0.05 est un **majorant pris hors
E**, sens défavorable à la conclusion ; le résidu mesuré de 3.02 est
**+0.0188 en ln — positif**, aucune dépression au point le plus proche du
site.

## 6. Prédictions et consignations révisées

- **P1-a — JOUÉE (M14, gel `273d0a53`, delta 50).** NÉGATIF RÉSOLU +
  CANYON-E ; attente falsifiée sur la FORME (argmin 2.52, |E| = 0.561
  sous la bande, asymétrie, 2.50 perdu) — consignée sans réécriture ;
  taux intra à 5:2 mesuré (1/36 lignes) ; custody ×7 au bit.
- **P1-b (8/3, 4 points propres)** — falsifieur **d'étage B seulement**,
  étiqueté tel. **Tension consignée (machine 2 §8.3)** : dans M12, 2.67 —
  seul point d'ordre 11, à 0.0033 de 8/3 — est **mort d'une explosion
  sous s\*** (mécanisme E27, seule grossière non vide des 67 lignes).
  Sous le cadre de cette note, cette mort est un candidat-signature du
  8/3, en tension directe avec « aucun canyon ». Résolution par **double
  observable**, à écrire au gel de la manche : (i) E des survivants —
  lisse, falsifieur B ; (ii) motif des consignations G6 sous-seuil près de
  8/3 — signature séparée, branches de lecture écrites d'avance. Les deux
  peuvent différer : un rang (3,1) peut être trop faible pour creuser s\*
  et néanmoins structurer le dessous du seuil. Aucune des deux lectures ne
  préjuge l'autre.
- **P1-c (zéro, [2.27, 2.42])** — **requalifiée : consignation, pas
  prédiction** (machine 2 §7 : la monotonie d'une somme de queues ne se
  déduit pas). Le profil sera consigné, aucune porte dessus.
- **P1-d** — **remplacée par M13** (§5). L'ancienne forme était hors
  domaine gelé ; la nouvelle vise le trou directement.
- **P1-e (miroirs 2:1)** — dernier servi ; 1.82/2.18 propres, 1.90/2.10
  dans le rayon (à déclarer si retenus). Né d'une structure de
  l'entraînement ; légitime une fois pré-enregistré.

## 7. Réponses reçues et intégrées (les données demandées en v1 §7)

1. **Catalogue R-2′** (gel v4, lignes 123–132) : toute fraction d'ordre
   ≤ 12 ; rayons 0.12 / 0.03 / 0.0075 / 0.001875 par bandes d'ordre.
   5/3 (q = 8) **y figure** — la branche « absent » de la v1 était fausse ;
   la branche « sans morsure » tient (jamais la plus proche sur les 13
   points). Les 13 assignations re-dérivées par machine 2 depuis R-2′
   seule : 13/13 identiques à l'artefact.
2. **Archives M5/M6** : le test hors échantillon du §0 — le changement de
   statut de l'étage A. Lecture ordinale seulement ; aucun chiffre de ces
   chaînes n'entre dans un argument M12 ; |δ₇|/|δ₅| **se mesure dans la
   chaîne de la manche** (exigence gel, machine 2 §8.4).

## 8. Falsifieurs, triés par cible

**Tuent l'étage A** : un canyon net à un degré pair sur une famille
d'ordre impair ; une famille de rang (1,1) interdite qui mord comme une
permise. **Tuent l'étage B** : un canyon net de E à 8/3 ; une structure
forte en d dans le groupe 3:1 sous H-SAT vraie. Le falsifieur « signe de
E positif au cœur de 5:2 » a été JOUÉ et n'a pas tiré (M14 : aucun point
au-dessus de +10·B_E).
**Tuerait H-SAT rétroactivement** : un creux de s\*₄ au site sous la
résolution déclarée — demi-largeur < 0.02 ou logé dans les trous de E —
mis au jour par une sonde plus fine ; à la classe mesurée, H-SAT tient.
Toute porte de manche déclare sa cible (exigence machine 2 §8.1).

---

*v5, machine 1 — adopte les §2–§8 de la re-dérivation machine 2
(`97c02eab`). Prochain geste : la manche P1-b — 8/3 en double observable, avec
la tension 2.67 consignée (§6) ; puis P1-e, P2 (observable quantique) et
la dérivation de C. Le mécanisme, lui, est complet.*
