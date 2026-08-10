# Note de dérivation P1 — le signe de E par famille de résonance (v2)

Machine 1, 02/08/2026. **Hors chaîne.** **v2 remplace v1** (`fc311e15`) et
intègre la re-dérivation machine 2 (`p1_re_derivation_machine2_v1.md`,
`97c02eab`). Changements : §1 corrigé en rangs (r, j) — trois « jamais »
étaient faux ; §2 restructuré en deux étages (cadre machine 2, adopté) ;
le groupe 3:1 requalifié : H-SAT est une **hypothèse** qui porte 3 des 11
signes ; P1-c requalifiée en consignation ; P1-d remplacée par la manche
M13 ; la tension 2.67/P1-b consignée ; le test hors échantillon 5/5 de
machine 2 enregistré comme changement de statut.

## 0. Statut épistémique

**Étage A (sélection par parité) : ACQUIS.** Dérivé (§1), contrôlé par un
chemin indépendant qui ne partage rien avec la dérivation (FFT 2D,
machine 2 §2), et **vérifié hors échantillon 5/5** sur les archives M5/M6
(machine 2 §3, lecture ordinale) : canyons à 2:1 aux trois degrés impairs,
minimum exactement en 2.00 ; traversée strictement monotone aux deux degrés
pairs ; séparation ordinale ×41. Avec la loi des porteurs (q = 3) et le
2:1-faible du système quartique, trois succès hors échantillon. **La règle
n'est plus une reconstruction post-hoc des onze signes de M12 — elle
prédit des données qu'elle n'a pas vues.**

**Étage B (hiérarchie des amplitudes) : HYPOTHÈSE, premier test favorable.**
Non dérivée, et le contexte est hostile : au seuil, g·s\*^(p−2) = K est
d'ordre 1 — un comptage d'ordres ne garantit aucune hiérarchie de
magnitudes. Testée une fois (j = 1 contre j = 2 à 2:1), favorablement.

**H-SAT (saturation 3:1) : HYPOTHÈSE IMPORTÉE, non testée en chaîne,
portant 3 des 11 signes.** Le §5 lui donne son test — c'est le prochain
geste.

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

**Erratum de la v1** : les trois « jamais » (3:2, 5:2, 8:3 à p = 4) étaient
faux — la v1 appliquait le mécanisme d'harmonique doublée à 2:1 et
l'oubliait pour les autres familles impaires. Incohérence interne, attrapée
par la re-dérivation machine 2 (FFT + formule).

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
  E_rés = −1.25|δ₇| + 2.25|δ₅⁽³,¹⁾|. **Négatif ssi le terme (3,1) est
  négligeable** — c'est un test d'étage B au site 5:2, pas un
  inconditionnel absolu. Reste la prédiction la plus propre du jeu, et la
  famille reste un spectromètre du degré 7 sous étage B.
- **3:1 — LE TROU (machine 2 §6, adopté tel quel).** Rang (1,1) à p = 4 :
  le couplage le plus fort possible, le même rang que les canyons
  impairs à 2:1. **La règle nue prédit ici le canyon le plus profond du
  jeu — et la mesure voit un plateau** (+0.517/+0.519/+0.543, étendue
  0.026). La v1 comblait par la saturation GSTZ (« vérifiée dans le
  système quartique ») : hypothèse **importée d'une autre chaîne**, jamais
  testée dans celle-ci, qui contredit la prédiction la plus forte de la
  règle. Nom au registre : **H-SAT**. Trois des onze signes en dépendent.
- **8/3** — (3,1)/(3,1)/(6,2) : rien aux rangs bas ⇒ pas de canyon de E
  sous étage B. Falsifieur d'étage B, pas d'étage A.

## 3. Confrontation aux onze points — 8 prédits, 3 accommodés

| famille | points → E | statut |
|---|---|---|
| 2:1 | 1.76/+0.81 · 1.84/+0.96 · 1.86/+1.02 · 2.22/+0.41 · 2.27/+0.17 | **prédits** (A + B : borne 9/5) |
| 3:2 | 1.73/+0.76 | **prédit** (idem) |
| 5:2 | 2.42/−0.15 · 2.55/−0.48 | **prédits** (A + B au site 5:2) — le fait saillant dérivé |
| 3:1 | 2.72/+0.52 · 2.78/+0.52 · 2.80/+0.54 | **accommodés par H-SAT** — la platitude est cohérente avec H-SAT, mais H-SAT n'est pas testée en chaîne |

Structures secondaires : saut, zéro encadré, monotonies internes,
platitude du groupe droit, contre-paire requalifiée en asymétrie
gauche-droite — inchangées de la v1, avec la même dépendance : celles du
groupe droit tiennent **sous H-SAT**.

## 4. Pourquoi la classe affine devait mourir (version corrigée)

La sélection est une fonction de la parité et du rang, orthogonale à toute
forme affine en u_p : en territoire résonant, la classe ne pouvait tenir
que si **tous** les creux de rang (1,1) étaient nuls — contredits par M5,
M6 et M12. Formulation affaiblie par rapport à la v1 (plus de zéros exacts
à p pair), conclusion intacte.

## 5. Le test décisif : M13 (recommandation machine 2 §6, adoptée)

**Balayage s\*(ω₂) au seul degré 4 à travers ω₂ = 3.0** — l'analogue exact
du test M6 à 2:1. Deux branches, chacune informative :
profil lisse et monotone ⇒ **H-SAT mesurée en chaîne**, le groupe 3:1
expliqué, second test favorable d'étage B ; canyon en 3.0 ⇒ H-SAT morte,
la lecture du groupe 3:1 s'effondre **avec 3 des 11 signes** — étage A
intact. Coût : une ligne de géométrie, deux minutes de calcul. **Avant
toute manche P1.** Gel : `gel_m13_balayage_saturation_v1.md` (brouillon
joint, à certifier).

## 6. Prédictions et consignations révisées

- **P1-a (5:2, 2.44–2.56)** — à jouer en premier après M13. Étiquette :
  teste A + B(5:2). Points 2.48/2.50/2.52 **dans le rayon** :
  échantillonnage délibéré à déclarer (précédent gel v4 ligne 420), et
  **la perte est une donnée** (§7.2).
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
forte en d dans le groupe 3:1 sous H-SAT vraie ; un terme (3,1) non
négligeable à 5:2 (signe de E positif au cœur de la famille).
**Tue H-SAT** : un canyon de s\*₄ à travers 3.0 — M13, branche 2.
Toute porte de manche déclare sa cible (exigence machine 2 §8.1).

---

*v2, machine 1 — adopte les §2–§8 de la re-dérivation machine 2
(`97c02eab`). Prochain geste : certification du gel M13, run (deux
minutes), puis gel de la manche P1 (P1-a, P1-b double observable, P1-e)
selon la branche.*
