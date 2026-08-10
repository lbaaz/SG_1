# GEL M13-L v1 — LECTURE AGRÉGÉE DES SURVIVANTS p = 4 (option β, delta 48.7)

**Machine 1, 02/08/2026.** Zéro recherche neuve. Ce gel contient
l'ALGORITHME COMPLET de la lecture ; après certification à vue, **les deux
machines l'implémentent indépendamment** et comparent les JSON au bit —
la double implémentation EST la vérification (le pattern de la
re-dérivation P1). L'évaluation de machine 2 est l'opposable.

## L1 — Objet, et ce que ce gel est honnêtement

Rendre le verdict que deux planchers de géométrie ont refusé (M13, M13b),
par une règle mécanique sur les artefacts existants. **Déclaration de
structure** : l'ensemble des survivants est CONNU au moment où ce gel
s'écrit (delta 48). Ce qui rend la lecture opposable n'est pas le
suspense — l'issue est déterministe dès la certification — mais ceci :
**(i)** le juge (classifieur P-M13a) est antérieur aux deux runs, certifié
au gel M13 v3 et repris à l'identique ; **(ii)** l'appartenance à
l'ensemble E est mécanique, zéro choix ; **(iii)** les seuils du plancher
L4, eux choisis en connaissance de E, **ne peuvent que REFUSER une
lecture, jamais en créer une** ; **(iv)** la résolution du verdict est
dérivée et chiffrée (L6), avec ses hypothèses et ses échappatoires
déclarées. La valeur du gel est l'opposabilité de la règle, pas
l'ignorance du résultat.

## L2 — Entrées, nommées par empreinte

`m13_results.json` `70fe5611712f0e5078a3ab852fded135e9606dcd162070c0a76205aaa1077f99`
et `m13b_results.json` `22fa176013a9d46b9656d121c736cad46bc6e5196a9f52fee57d78bdd056277b`
— détenus et vérifiés au bit par les deux machines. Légitimité de
l'union : même chaîne (moteur `c8ed357b`, pilote `663b17e2`), prouvée par
G1′ et les ancres 2.85/3.15 à 0.0 exact (M13b, gel A4).

## L3 — L'ensemble E : union mécanique, zéro degré de liberté

Pour CHAQUE artefact, un point (p = 4, ω₂ ∈ [2.70, 3.30], signe +1) est
SURVIVANT ssi `sF ≠ null`, `sP.recevable = true`, et aucune entrée
`G6[cle|±1].exclue = true`. **E = union des survivants des deux
artefacts — tous, aucun choix.** Pour un ω₂ présent dans les deux :
**garde G-L1**, les deux `sF` doivent être identiques AU BIT (sinon
ARRET — la chaîne serait rompue) ; la valeur unique est prise. Le `pas`
de chaque ligne est lu de SON artefact (`G6[...].pas_final_recherche`).

## L4 — Plancher en COMPTES (peut refuser, jamais créer)

Lecture autorisée ssi : |E| ≥ 9 ; ≥ 3 points à ω₂ ≤ 2.90 ; ≥ 3 points à
ω₂ ≥ 3.06 ; ≥ 1 point à d(3.00) < 0.12. Aucun survivant nommé (leçon
48.6). Sinon : NON CONCLUANT, aucune lecture.

## L5 — La porte P-M13L : le classifieur certifié, inchangé

`classer_pm13a` du gel M13 v3 §6 (texte certifié `26c5a445`, embarqué
verbatim dans le script) : LISSE ssi strictement monotone ; CANYON ssi
minimum intérieur, argmin ∈ [2.94, 3.06], ex æquo N-5, chute résolue des
deux côtés à 10·B_inst par paire ; sinon NON CLASSÉ, motif publié.
Appliqué à E trié, bords = min(E) et max(E) — les extrêmes survivants.

## L6 — Résolution du verdict, DÉRIVÉE (remplace « à la résolution des survivants »)

Un creux ne peut vivre que dans les trous de E ; son seul centre
physiquement motivé est 3.00 (rang (1,1) maximal à la résonance exacte).
Or E contient 3.02 (d = 0.02). Étalons de forme — les trois canyons 2:1
mesurés (M5/M6, **ordinal, hors chaîne, hypothèse de prior déclarée**) :
39–46 % de la profondeur centrale encore visible à d = 0.05 ; toute forme
unimodale de demi-largeur ≥ 0.03 laisse ≥ 64 % de D visible à d = 0.02.
Plancher de détection honnête : la rugosité du fond lui-même (la marche
2.89 → 2.92, +0.10 en ln sur 0.03), soit ≲ 0.05 en ln — pas
l'instrumental. **Borne : tout creux centré au site, de classe mesurée
(unimodal, demi-largeur ≥ 0.03), a une profondeur centrale
D ≲ 0.05/0.64 ≈ 0.08 en ln — contre 0.49, 0.80 et 2.73 aux canyons
impairs : exclusion d'un facteur 6 à 30.** Échappatoires déclarées, non
exclues par principe : demi-largeur < 0.02 (plus étroit que tout canyon
mesuré) ; creux décentré logé dans un trou. Corollaire consigné HORS
porte (custody de chaîne, pas donnée de E) : les bruts portent 3.00
lui-même, monotones 2.96 → 3.05 sur deux runs — une échappatoire doit
être décentrée ET ultra-étroite.

## L7 — Verdicts et conséquences, écrits d'avance

- **LISSE** ⇒ verdict inscrit : « LISSE à résolution dérivée — aucun
  creux de classe mesurée au site ; D ≲ 0.08 en ln (L6) ».
  **H-SAT est MESURÉE.** Le groupe 3:1 de la note P1 passe d'« accommodé »
  à « expliqué par un mécanisme mesuré : saturation du seuil » — le
  dessous criblé (48.3) restant consigné à part, sans lecture. Note P1
  → v4 ; la manche suivante est P1-a.
- **CANYON** ⇒ H-SAT morte, trois signes tombent (inchangé).
- **NON CLASSÉ / NON CONCLUANT** ⇒ publié ; retour à l'option (α).
- L'attente gelée du rédacteur : LISSE (provenance : delta 48, déclarée —
  ici l'attente et la donnée coïncident par construction, voir L1).

## L8 — Sortie et gardes de la lecture

JSON `m13L_results.json` : meta (empreintes des deux entrées, sha du gel
jumeau, mode), E complet (ω₂, sF, pas, artefact source), G-L1 (bit-égalités
des communs), **G-L2 consigné hors porte** : 2.78 est bit-identique entre
`fa109da9` (M12) et `22fa1760` (M13b) — 8.03774683329979 — quatrième
verrou de chaîne, inter-manches ; plancher L4 (comptes) ; verdict L5 avec
consignation intégrale ; résolution L6 recopiée. Selftest embarqué : les
13 vecteurs du classifieur (5 archives + 8 branches), bloquant. Les deux
implémentations comparent le sha256 du JSON (champ date exclu de la
comparaison, ou date fixée à la chaîne vide — convention : **date omise du
JSON de lecture**, la date vit dans les logs).

## L9 — Ce que cette lecture n'établit pas

Rien sur le dessous du seuil (l'ensemble entrelacé 48.3 reste matière
sans porte) ; rien sur l'étage A, 5:2, 8/3 ; rien hors [2.70, 3.30] ;
rien sur le pas de s\*₄ ; et la borne L6 vaut sous ses hypothèses
déclarées, pas au-delà.

## L10 — Chaîne

Parents : gel M13 v3 `26c5a445` (classifieur), gel M13b v1 `7a9b2809`
(ancres) ; artefacts `70fe5611`, `22fa1760`, `fa109da9` (G-L2) ; delta 48
`24697187`. Après certification à vue : implémentation indépendante par
les deux machines, comparaison des JSON au bit, celle de machine 2 fait
foi au registre. Empreinte de ce gel : au message ; la version certifiée
fera foi.
