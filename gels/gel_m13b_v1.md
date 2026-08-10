# GEL M13b v1 — AMENDEMENTS AU GEL M13 v3 (`26c5a445`, certifié)

**Machine 1, 02/08/2026. FORME DIFF** : tout ce qui n'est pas amendé
ci-dessous vaut TEL QUEL au gel M13 v3 — géométrie de balayage, gardes,
convention B, moteur `c8ed357b`, pilote `663b17e2`, borne HI0 = 20,
classifieur P-M13a (fenêtre [2.94, 3.06], K = 10, ex æquo N-5), G1′
(2.80, champ nommé, `fa109da9`), G2/G4 en consignation sans porte,
selftest cinq contre-exemples. Certification attendue : **à vue** (une
ligne). Aucun code avant (E19) ; le script est un PATCH v1b → v1c,
appliqué et consigné par machine 2 (précédent v1b, écart de répartition
déclaré).

## A1 — Objet : DEUX portes (delta 47, option (i))

**P-M13b-a (H-SAT, inchangée sur le fond)** : le classifieur P-M13a du
gel v3, appliqué à TOUS les survivants. **Résolution déclarée d'avance**
en deux sous-branches, consignées avec le verdict :
- **a-fort** : ≥ 2 points intra-rayon survivent → la fenêtre CANYON est
  résolue par des mesures au site.
- **a-faible** : tous les intra meurent → le verdict (LISSE attendu) vaut
  **à la résolution du rayon** : un creux plus étroit que 0.12 n'est pas
  exclu par s\* — et c'est P-M13b-b qui porte le site.

**P-M13b-b (structure sous-seuil, PRÉ-ENREGISTRÉE, points NEUFS)** :
STRUCTURE SOUS-SEUIL AU SITE 3:1 ssi, sur les cinq points intra NEUFS :
**≥ 3 exclusions G6, formant un bloc contigu en ω₂, toutes à
d ≤ rayon(ordre 4) = 0.12 — le site est DÉRIVÉ du catalogue R-2′ (leçon
47.6), plus aucun nombre inventé — ET zéro exclusion G6 hors rayon.**
Tout autre motif : publié, sans lecture. Les cinq morts de M13
([2.90, 3.03], `70fe5611`) sont la PROVENANCE déclarée de cette porte ;
ils n'entrent pas dans son évaluation.

## A2 — Points (17 recherches, 14 balayages)

- **Huit HORS rayon** (marge R-2′ ≥ 1.10 × 0.12 vérifiée, toutes
  fractions d'ordre ≤ 12) : **2.70, 2.74, 2.78, 2.85, 3.15, 3.22, 3.26,
  3.30.** Ils portent le plancher, la corde et la monotonie.
- **Cinq INTRA rayon, NEUFS** (jamais mesurés — la grille M13 était
  {2.90, 2.94, 2.97, 3.00, 3.03}) : **2.89, 2.92, 2.96, 3.02, 3.05.**
  Ils portent P-M13b-b ; leurs s\*, s'ils survivent, nourrissent a-fort.
- Fenêtre totale [2.70, 3.30] ; une seule famille d'ordre ≤ 12 dedans
  (3/1) — vérifié : 8/3 = 2.667 est hors fenêtre, 11/4, 16/5, 13/4,
  10/3 sont d'ordre > 12.

## A3 — Plancher et bords (remplace le §5 du gel v3)

P-M13b-a exige : **m_hors ≥ 7 sur les huit points hors rayon**, ET les
deux bords (2.70, 3.30) survivants. Les intra ne comptent ni pour ni
contre le plancher. Sinon : NON CONCLUANT DE GÉOMÉTRIE, aucune lecture
d'aucune porte. La lecture « attrition simple / structure » du §5 v3 est
REMPLACÉE par P-M13b-b.

## A4 — Ancres de régression gratuites (custody ×3)

2.85 et 3.15 ont été mesurés par M13 sous la MÊME chaîne et la MÊME
géométrie (`70fe5611`). Leurs nouvelles mesures doivent reproduire
**au bit** : s\*(2.85) = 8.24916028645919 ; s\*(3.15) = 9.970764210546593.
Écart ≠ 0.0 → ARRET (même statut que G1′). Trois verrous de custody pour
le prix d'un.

## A5 — Gardes déplacées

**G8** : au point **2.85** (survivant M13, hors bande morte), deux
signes ; moitié grossière attendue vide, inchangé. **G2** : au point
3.00 ?  Non — 3.00 n'est plus au programme ; G2 à **2.85** (la base et
la 2g partagent le rang, comme M12 rang 1). **G4** : échelle de force
maximale au run ; attente : 3.30. **G1′** : inchangé (2.80, hors
programme — 2.78 et 2.85 en sont distincts).

## A6 — Comptes, forme dérivée

Recherches = 13 (programme) + 1 (G8, −1 à 2.85) + 1 (G1′) + 1 (G4) +
1 (G2) = **17**. Balayages = 13 + 1 = **14**. Formes
« comptés + sautés == attendus ».

## A7 — Attente gelée du rédacteur (machine 1, avant tout calcul)

Hors rayon : 8/8 survivent, profil strictement croissant, ancres 2.85 et
3.15 à 0.0 exact. Intra : **5/5 meurent par G6, fenêtre fine, entre 0.90
et 0.98 s\*** (le motif de M13). P-M13b-b : **STRUCTURE tire.**
P-M13b-a : **LISSE en sous-branche a-faible.** Provenance : entièrement
extrapolée de M13 (`70fe5611`) — déclarée, règle de provenance.

## A8 — Conséquences par branche, écrites d'avance

- LISSE (a-faible) + STRUCTURE : **H-SAT est mesurée à la résolution du
  rayon, et le site est établi comme structuré SOUS le seuil.** Le groupe
  3:1 de la note P1 passe d'« accommodé » à « expliqué par un mécanisme
  mesuré : saturation du seuil + structure sous-seuil » — la forme
  raffinée de H-SAT. Le rapprochement 47.4 (2.67/M12) devient une
  question dérivable, toujours pas un résultat.
- LISSE (a-fort) : H-SAT mesurée au site même — plus fort.
- CANYON : H-SAT morte, trois signes tombent (inchangé du gel v3).
- STRUCTURE ne tire pas : le bloc M13 était un accident de tirage ou la
  bande a bougé — publié, et la note P1 garde son trou.
- NON CONCLUANT DE GÉOMÉTRIE : redessiner encore ; aucun des deux runs
  n'aura menti.

## A9 — Chaîne

Parent : gel M13 v3 `26c5a445` (cert. `b1ff00be`) ; artefacts de
provenance : `70fe5611` (M13), `fa109da9` (M12) ; delta 47 `535a49e8`.
Patch v1b → v1c : spécification jointe (`m13b_patch_v1c_spec.md`),
appliquée par machine 2, éditions consignées dans
`meta.declarations.editions_machine2`. Pré-vol RÉDUIT aux branches
neuves : deux scénarios (attendu ; géométrie) — les six de v1b restent
opposables pour le chemin inchangé. Empreinte de ce gel : au message ;
la version certifiée fera foi.
