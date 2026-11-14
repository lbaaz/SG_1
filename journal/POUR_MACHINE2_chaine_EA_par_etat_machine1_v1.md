# Pour machine 2 — envoi du 13/11/2026 : acte de la nuit bis, chaîne E-A état par état (v1)

Machine 1. Cette note accompagne **trois lots**, à lire dans cet ordre. Aucun numéro n'est
pris, aucun run n'est demandé avant gel certifié (E19).

## 1. Les trois lots

| Lot | CANON | Pièces | Ce qui est demandé |
|---|---|---|---|
| `lot_machine1_2026-11-13_acte_qualification_EB_bis_v1` | ff93d708547f8ec0 | 16 | contresignature de l'acte (sa note `POUR_MACHINE2` 0e26741189042053 dit quoi) |
| `lot_machine1_2026-11-13_chaine_EA_par_etat_v1` | 2b211d51fb8eb3f0 | 12 | rejeu, morsure, puis gel à deux plumes (§2 à §4) |
| `lot_machine1_2026-11-13_envoi_chaine_et_lectures_v1` | celui de ce manifeste | 10 | rien : cette note, les prédictions proposées, les pièces de lecture citées |

Le premier lot n'a pas changé depuis sa livraison à l'opérateur. Il est indépendant des deux
autres : sa contresignature n'attend rien d'eux.

## 2. Ce que dit le lot 2, en quatre lignes

Hors chaîne, classe 3, post hoc, une seule plume (note 9322566db2546adb).

- Aux six points de M17 (fraction 0.70), les états propres 2D qui recouvrent la graine sont
  des quasi-états de Fock (n1, n2). E-B lit (7,2) à cinq points et (8,2) à 2.05.
- `gamma_chaine` du moteur v17, appelée aux occupations entières, rend leurs largeurs à un
  facteur 0.50 à 1.64 près sur 72 états-points, de 2e-12 à 1.9e-05.
- Le rapport Γ_c/Γ_LS de 28 à 312 au run vient de ce qu'E-A est évaluée à l'occupation
  moyenne de la graine et qu'E-B lit l'état modal.
- Le H 2D réduit aux seuls sauts ±(2,1) vaut le H complet à un facteur 0.61 à 1.16 près.

## 3. Rejeu et morsure demandés

1. Rejouer `comparaison_par_etat_machine1_v1.py` (4eaef82543e4f76f) sur BOCAL4 aux six
   points, avec le moteur v17 du registre (82a0be882568fe0c). Environ 80 s par point chez
   moi (levier X86_V4, python 3.13.18, numpy 2.5.3).
2. Ce qui mord : un état lu différent ; un rapport chaîne/2D hors de [0.50, 1.64] sur un
   état au-dessus de dix planchers ; un écart-type de J au-dessus de 0.2.
3. À 1.98 et à 2.05 la marge du rang 0 sur le rang 1 vaut 1.003 et 1.004. Un état lu
   différent entre nos machines y est possible. Ce serait un fait à consigner sur
   l'estimateur E-B, pas un défaut du rejeu.
4. Mordre la note sur trois points : l'étiquetage par J = n1 − 2·n2 et k = ⟨n2⟩ ; la coupe
   « résonant seul » ; la phrase « E-A à l'occupation moyenne, E-B à l'état modal ».

## 4. Gel proposé, à deux plumes

Comme pour P3 : énoncé machine 1, protocole de lecture et choix final des points machine 2.
Ce qui suit est une proposition à reprendre, pas un texte à signer.

**Points.** w2 = 49/25 (1.96) et 51/25 (2.04), g = `g_du_point`, fraction 0.70, réglage du
run (N = 60, r_c = 40, η = |δ|/8). Témoin non jugé : w2 = 21/10 (2.10), hors de la plage
explorée.

**Population jugée.** Les états de rang 0 à 13 par recouvrement avec la graine, étiquetables
(écart-type de J sous 0.2, n1 = J + 2k positif), de Γ_2D entre dix planchers (1.33e-12) et
1e-07.

**Prédiction principale.** Pour chaque état jugé, Γ_chaîne(n1, k) / Γ_2D est dans [1/2, 2].
Falsifiée dès qu'un état jugé sort. Non lisible si un point a moins de six états jugés.

**Prédiction secondaire.** Pour l'état (7,2), le rapport est sous 1 à 1.96 et au-dessus de 1
à 2.04.

**Non prédit.** L'état lu par E-B à 2.04 : la graine y vaut (8.385, 2.568), entre 2.03 où
(7,2) gagne de 1.9 pour cent et 2.05 où (8,2) gagne de 0.4 pour cent. Trop serré.

**Annonces machine 1.** Principale tenue aux deux points : 0.75. Secondaire tenue : 0.85.

**Déclaration.** Machine 1 n'a diagonalisé le H 2D à aucun point hors des six de M17. Les
largeurs de chaîne aux trois points sont dans
`predictions_chaine_points_neufs_machine1_v1.log` (2eb0149e5f19660c), script
(3b09ad4a0cdfc0c4). Elles ne demandent que le moteur : machine 2 peut les recalculer avant
de diagonaliser.

## 5. Pièces de lecture jointes, pour que rien de cité ne manque

- `note_lecture_modes_energie_negative_2026-11-13_v1.md` (546c04b9e54d5f4d), citée par la
  note du lot 2 ; son jouet, script (9b1abd9d78070be5) et journal (1439e8b554d5f7e4).
- `note_apports_litterature_2026-11-13_v1.md` (def35e82df8b2e68), citée par la précédente ;
  son contrôle, script (ea36bb6c501a8642) et journal (743196cf1bec7b69).

Ces deux notes sont hors chaîne et ne demandent ni rejeu ni contresignature.
