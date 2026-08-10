# M12 PONCTUEL — CERTIFICATION DU RUN ET RÉCONCILIATION INDÉPENDANTE

**machine 2 — 02/08/2026**
Objet : `out/m12_results.json`, sha256 `fa109da92e582520cfcb63b46bc41fa7d4b62295891f413bb97c6095b2fe59b1`
Trace : `m12_reconciliation_ponctuel_machine2_v1.py` + `.log` (10 sections, sortie `TOUT CONCORDE`, exit 0)
Log de run : `m12_ponctuel_run_machine2.log`

---

## 0. VERDICT

**LE RUN EST OPPOSABLE. LES DEUX PORTES SE LISENT.**

| porte | verdict au JSON | recalculé par moi | accord |
|---|---|---|---|
| **P-M12a** (principale) | `CLASSE REFUTEE` | `CLASSE REFUTEE` | ✔ |
| **P-M12b** (secondaire, conditionnelle) | `VIOLATION DISPERSEE` | `VIOLATION DISPERSEE` | ✔ |

`m = 11` sur `N = 13`. Branche appliquée : **|E| ≥ 0.10 sur au moins ceil(m/2) = 6 points** — obtenu sur **11 points sur 11**, marge 5. La branche `m < 3` (NON CONCLUANT PAR CONSTRUCTION) n'a jamais été approchée, et la branche `CLASSE TENUE` a 0 point.

**C'est la première manche conclusive de la campagne depuis M6, et la première lecture de E.**

---

## 1. CE QUI EST RECALCULÉ, PAS LU

Règle de campagne : la réconciliation recalcule brut → résumé, elle ne lit jamais les meta.

- **E recalculé depuis la carte** aux 11 points survivants, `E = ln s*₄ − 2.25 ln s*₅ + 1.25 ln s*₇` sur les `sF` bruts : **écart max 0.00e+00**, exact.
- **σ_E et σ_E_max recalculés en forme dérivée** (`c_p · pas_p / s*_p`, pas **absolu**, jamais relatif — E26/E27) : écart relatif 0.00e+00 et 2.1e-16.
- **m recalculé par le chemin brut** : `G6.exclue` par ligne → répercussion G7 sur les trois degrés du point → 11. Concorde.
- **Invariants de comptage** : 75 + 0 = 75 recherches, 67 + 0 = 67 balayages, et `5N + 10 = 75` re-dérivé à N = 13. Inventaire des 67 balayages reproduit : 13 (p=4,+1) + 2 (p=4,−1, régression G8) + 13×4 (p=5 et p=7, deux signes).
- **Convention de signe** vérifiée ligne à ligne : `sF = min(sP, sM)` à p impair, `sF = sP` à p=4, et p=4 ne porte deux signes **que** sur les deux lignes de régression G8.
- **Tout null porte un motif** : 0 null nu sur l'ensemble du fichier (G9 tenue après run, pas seulement avant).

Toutes les gardes passent : G1′ **écart absolu 0.0 EXACT** sur la ligne nommée au gel (1.70, p=7, +1) — custody transitive intacte ; G3 ≤ 4.75e-16 aux quatre rebindings (tolérance 1e-12) ; G4 écart 1.08e-04 (plafond 2 %) et **sur la ligne que je re-désigne indépendamment** comme maximisant l'échelle de force (p=4, w2=2.80) ; G5 pas final max 1.82e-06 (plafond 1e-5) ; G2 six recherches, écart max 4.9 % (tolérance 10 %) ; G8a écart absolu 0.0 aux deux rangs.

---

## 2. LA MESURE

| w2 | E | σ_E | \|E\| / σ_E_max | résonance d/r (ordre) |
|---|---|---|---|---|
| 1.73 | **+0.764146** | 2.59e-06 | 196 358 | 1.917 (5) |
| 1.76 | **+0.808568** | 2.55e-06 | 211 282 | 2.000 (3) |
| 1.84 | **+0.964440** | 2.53e-06 | 256 474 | 1.333 (3) |
| 1.86 | **+1.015680** | 2.55e-06 | 267 986 | 1.167 (3) |
| 2.22 | **+0.405583** | 1.46e-06 | 180 884 | 1.833 (3) |
| 2.27 | **+0.171548** | 1.29e-06 | 85 511 | 2.250 (3) |
| 2.38 | *point perdu (G7)* | — | — | 3.167 (3) |
| 2.42 | **−0.147267** | 1.03e-06 | 90 459 | 2.667 (7) |
| 2.55 | **−0.483335** | 8.87e-07 | 338 309 | 1.667 (7) |
| 2.67 | *point perdu (G7)* | — | — | 1.778 (11) |
| 2.72 | **+0.517399** | 7.64e-07 | 411 168 | 2.333 (4) |
| 2.78 | **+0.519337** | 7.45e-07 | 422 759 | 1.833 (4) |
| 2.80 | **+0.542579** | 7.38e-07 | 445 891 | 1.667 (4) |

La classe prédit **E = 0 exactement**. Le plus petit module mesuré, 0.147, vaut **90 000 fois** σ_E_max de son point ; le plus grand, 1.016, en vaut 268 000. **Aucune lecture de cette manche ne dépend d'une question de résolution**, et c'est la première fois de la campagne qu'un écart est à cinq ordres de son incertitude sans passer par un fit.

L'attente écrite du gel — « |E| entre 0.15 et 0.45 sur la majorité des points » — est **dépassée** : 8 points sur 11 sont au-dessus de 0.40, quatre au-dessus de 0.76. L'attente de signe unique (« P-M12b SYSTEMATIQUE ») est en revanche **fausse** : deux points portent E < 0.

---

## 3. LES DEUX PERTES — ET ELLES NE SONT PAS DU MÊME MÉCANISME

`meta.exclusions` porte le **même motif** pour les deux, `"G6 sgn=+1 explosion sous seuil"`. L'enregistrement, lui, les distingue :

| ligne | fenêtre fine (< 0.98 s\*) | fenêtre grossière [LO0, 0.90 s\*] | `gros_explosifs` |
|---|---|---|---|
| `7\|2.38\|+1` | **explosion à 1.2241** | — | 0 |
| `7\|2.67\|+1` | *aucune* | **explosion à 1.5489** | 1 |

Les deux exclusions sont **régulières au regard de la lettre de G6** (« aucune explosion sous 0.98 s\* » : la fenêtre grossière est entièrement sous le seuil, et j'ai vérifié que les deux fenêtres sont **contiguës sur les 67 lignes** — aucun trou). Mais la seconde est le **mécanisme d'E27**, celui que le pilote avait isolé, et c'est sa première apparition à un degré autre que celui où il a été trouvé.

**D1-1 (note d'exploitation, aucune donnée touchée) : le motif consigné confond deux mécanismes que la donnée sépare.** À corriger au prochain script : le motif nomme la fenêtre.

**Répercussion G7** : chaque perte est une ligne à p=7 seulement, et elle retire le point à ses trois degrés. C'est ce qui fait m = 11 < 13, sans exception, comme écrit.

---

## 4. TROIS CONTRÔLES QUI ONT MORDU POUR DE BON

**(a) Le piège de l'indice 40 est exercé sur donnée RÉELLE — et la parade tient.**
Le protocole le déclarait « encore ouvert » : l'indice 40 du balayage fin vaut *exactement* 0.98 s\*, seuil d'exclusion de G6, et la conformité tenait à l'arrondi de `linspace`, pas à la règle. La parade gelée était : comparer sur l'**indice entier** (`s < 0.98 s*` ⟺ `i < 40`), plus un test négatif.

La ligne **`5|2.67|+1` est explosive exactement à l'indice 40** — `explosif_a_l_indice_40 = True`, `explosion_sous_0.98s = None`, `indice_40_compte_comme_sous_seuil = False`, **`exclue = False`**. C'est le test négatif exigé, joué par les données elles-mêmes et non par un vecteur : une ligne dont la seule explosion est *au* seuil n'est **pas** exclue. Sur les 67 lignes, elle est la seule ; il aura fallu attendre le run réel pour l'obtenir.

**(b) La moitié grossière de G8b est vide à p=4, exactement comme pré-déclaré — et elle mord ailleurs.**
Pré-déclaration `ad8dd209` / delta 45 v3, écrite avant mesure : « cette moitié sera vide à p=4 sur les 13 points ; si elle mord, fait neuf. » Résultat : **0 explosif grossier sur les 15 lignes p=4**, et **une seule ligne non vide de tout le run**, `7|2.67|+1`. Le contrôle est donc vide là où il était annoncé vide, et non vide ailleurs : **il n'est pas vacant, il est borné** — c'est la différence entre un contrôle sans pouvoir et un contrôle dont le domaine de pouvoir est déclaré. La moitié fine, elle, a du pouvoir réel aux deux rangs (24/52 et 26/50 de part et d'autre de la transition).

**(c) La symétrie de parité tient au bit pour la troisième géométrie indépendante.**
`sP − sM == 0.0` exactement aux deux rangs de régression (2.22 et 1.86), îlots identiques, retombée identique. Acquis M11 → pilote → M12 ponctuel.

---

## 5. DEUX CHIFFRES DU GEL QUE LA MESURE CORRIGE (aucun n'affecte le verdict)

**(a) L'ancrage « 0.03 = 458 × σ_E_max au pire point » était une BORNE, pas une projection.**
Mesuré au pire point (1.73) : σ_E_max = 3.892e-06, donc **0.03 = 7709 ×** et **0.10 = 25 696 ×**. J'ai retrouvé la provenance du 458 : le gel a pris pour `pas_p` le **plafond de G5 (1e-5)**, alors que le pas final réel est 6.03e-07 — rapport 16.6. Recalculé au plafond, j'obtiens 465 ×, contre 458 annoncés (le reliquat vient des s\* projetés depuis M10/M11 au lieu des s\* mesurés).
Conséquence : le chiffre du gel est **conservateur d'un facteur 17**, dans le bon sens. **Il ne doit pas être cité comme une mesure** ; les deux seuils sont encore plus confortables que ce que le gel annonçait. C'est l'inverse d'E21, où une propagation était sous-estimée.

**(b) Le plan d'attrition, hérité du pilote, était très conservateur.**
Plan : `q_L = 0.2296` (borne supérieure unilatérale 80 % sur 1 perte / 12 lignes) → `s_pt = 0.4572` → **E[m] = 5.94**, `P(m ≥ 4) = 0.9154`.
Mesure : **2 lignes perdues sur les 65 du programme (3.1 %)**, 2 cellules point-degré sur 39 (5.1 %) — contre un taux ponctuel du pilote de 8.3 % et une borne retenue de 23.0 %. Sous le plan, `P(m ≥ 11) = 4.8e-03`.
**Je ne propose aucun aménagement de D-N.** La règle a été écrite avant la mesure, elle a produit N = 13, et sa conservativité a coûté des recherches, pas de la validité. Le fait est consigné comme matériau, conformément à `attrition_39` (« AUCUNE application D-N ici »).

---

## 6. P-M12d — CONSIGNATION, AUCUNE PORTE

Le gel impose une lecture pré-déclarée à quatre branches et **interdit explicitement de désigner rétrospectivement** laquelle des trois premières le motif « appuierait » (branche (iv), leçon S41.5). Je consigne donc le motif tel quel, sans le classer :

- **E est lisse et monotone décroissant de 1.86 à 2.55** : +1.0157 → +0.4056 → +0.1715 → −0.1473 → −0.4833, avec **un passage par zéro entre 2.27 et 2.42**.
- **Il croît de 1.73 à 1.86** (+0.7641 → +1.0157), puis
- **il saute de +1.0007 entre 2.55 et 2.72**, et redevient quasi plat sur 2.72–2.80 (+0.5174, +0.5193, +0.5426). Le point perdu 2.67 tombe **dans** cet intervalle de saut.
- ρ(|E|, d/r) = **−0.6393** ; ρ(|E|, w2) = **−0.4364** ; ρ(E, w2) = **−0.4909** (n = 11).
- Les trois régimes coïncident avec trois familles de résonance (ordres 3–5 rayon 0.12 à gauche ; ordre 7 rayon 0.03 au milieu ; ordre 4 rayon 0.12 à droite).

**Ma lecture, à contresigner et non à trancher unilatéralement** : ni (i) ni (ii) ne s'applique proprement — le signe de ρ(|E|, d/r) va dans le sens de (i), mais le saut de 1.00 entre deux points voisins interdit (ii), et (iii) est faux puisqu'il y a une structure visible. **C'est la branche (iv)**, celle que S41.5 a fait écrire, et c'est la première fois qu'elle sert. Le dernier point de la dernière famille coïncidant avec une correspondance ordre/régime est exactement le genre de motif qu'on ne choisit pas après coup ; il se re-mesure.

---

## 7. CE QUE CE RUN N'ÉTABLIT PAS

- **Aucune lecture physique n'est tirée**, dans aucun sens. Le gel le dit lui-même : « M12 MESURE, ELLE NE DÉRIVE PAS. Une réfutation ne désigne pas la classe de remplacement. »
- **La réfutation ne se transporte pas au bord gauche.** Limitation écrite AVANT la mesure : aucun point sous 1.73 n'est R-2′-propre (recouvrement des voisinages 3:2, 4:3, 5:4), et c'est là que vit la chaîne classique fermée. Ce n'est pas une réserve invoquée après coup selon le résultat.
- **p=3 et p=6 ne sont pas mesurés** (E22 pour p=3 ; p=6 relève d'une hypothèse post-hoc à pré-déclarer ailleurs).
- **Le mécanisme du signe négatif à 2.42 et 2.55 n'est pas établi.** Deux points, une seule famille de résonance, aucune réplication.

---

## 8. NOTES D'EXPLOITATION (D1, aucune donnée touchée)

1. **D1-1** — le motif d'exclusion confond fenêtre fine et fenêtre grossière (§3). Le motif doit nommer la fenêtre.
2. **D1-2** — `resume.duree_par_recherche_s` porte `n = 67` alors que **75** recherches ont tourné : la moyenne est calculée sur les recherches **porteuses de balayage**, ce que le nom ne dit pas. Champ à renommer ou à doter d'un renvoi.
3. **D1-3** — la **carte ne porte aucun marqueur d'exclusion** : son champ `recevable` qualifie la *recherche*, pas G6, qui est un diagnostic postérieur. Un lecteur qui recalculerait E depuis la seule carte obtiendrait un E aux deux points perdus, sans avertissement. La donnée est intègre (l'exclusion est intégralement consignée dans le bloc G6, par ligne nommée), mais **le chemin brut → résumé pour m doit passer par G6** — ma première passe de réconciliation est tombée dans le piège, ce qui en fait un piège réel. Parade proposée : un champ `exclue` + `exclue_motif` dupliqué dans la carte, par ligne.
4. `meta.gardes` est une liste vide ; les gardes sont consignées ailleurs (blocs G1p/G2/G4/G6/G8 et `G3_par_degre`). Champ mort à retirer ou à remplir.

---

## 9. EMPREINTES DU RUN

| objet | sha256 |
|---|---|
| JSON de résultats | `fa109da92e582520cfcb63b46bc41fa7d4b62295891f413bb97c6095b2fe59b1` |
| gel M12 v4 (bloc) | `bf9866a763c559d368c0ed23c73697bd1b6fde46a59b08a359c81918b6de9e9b` |
| script `m12_ponctuel_v2.py` | `c5659f52272a43aad556184289db0eeb38d798f91d8b5394da1bce4873cff014` |
| pilote importé `m12_pilote_v3.py` | `663b17e2955c79c09f1b6c0fb4443cd0c1f98be0db03ef089f5df682018ce905` |
| cible G1′ = JSON du pilote (RÉELLE) | `ed0e27b1b6067096f7f9ed3ab95b8a4f3f6362577feea16301fa7534b95ad117` |
| moteur `m9_replication_v1.py` | `c8ed357b120352c4d1078307…` |

Mode `REEL`, aucun factice. Date UTC du run : `2026-08-01T23:52:34Z`. Durée mesurée : 852.94 s sur 67 balayages (12.73 s en moyenne).

**Chaîne E19 complète et dans l'ordre** : gel v4 certifié (`f10ffcf3`, 01/08 21:13) → script v2 déposé et certifié (`5faef5ec`, 02/08 01:25) → pré-vol machine 2 à moteur factice tueur (01:23) → run (01:52) → la présente réconciliation. Aucun maillon n'est postérieur à celui qui l'autorise.
