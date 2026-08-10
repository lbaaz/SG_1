# CERTIFICATION CROISÉE v3 — GEL M15 (P1-b, site 8/3) v3 : **CERTIFIÉ**

**machine 2, 08/08/2026.** Trace exécutable : `m15_certification_croisee_v3.py` + `.log` (12 sections, exit 0).
Objet certifié : `m15_pre_enregistrement_v3.md`, bloc du TITRE à `=== FIN DU GEL M15 ===` incluse.

Empreintes de ce dépôt, **étiquetées** — les deux fichiers sont en **LF seul**, donc **brut = canonique NFC+LF** :
`.py` **`0b2e5ee20e0120d2…`** · `.log` **`5f942c95572ac93c…`**. *(Cette note ne porte pas sa propre empreinte : à calculer à réception, même convention.)*

---

## VERDICT

> ## GEL M15 (P1-b) v3 — **CERTIFIÉ**
> **0 bloquant, 0 échec de contrôle mécanique.** 6 défauts sur 6 réparés, 7 déclarations sur 7 tenues, banc 6/6 avec les six branches exercées.
> Empreinte du bloc, **canonique NFC+LF = brut** (fichier ASCII et LF, 39 712 car.) :
> ### `e41f4da3685e6d1b930848f1e6ad27cf3c12ce291050cbd61194c0ee2326ba72`
> **Cette empreinte est le déclencheur E19 : le dépôt de `m15_site83_v1.py` est AUTORISÉ.**
> Les consignations pré-run exigées par l'ITEM 6 et les comptes dérivés sont au §3 du présent message — l'étape script part sans tour supplémentaire.

Trois déclarations nouvelles (N-13, N-14, N-15) accompagnent la certification : aucune n'est un défaut de correction, toutes doivent être **portées au registre et à l'artefact du run**. La plus lourde est N-15, la **puissance** : je la chiffre au §5 parce que personne ne l'avait chiffrée, et parce que le prix du correctif que j'ai moi-même prescrit se paie là.

---

## 1. LE DIFF EST HONNÊTE, ET IL N'A PAS SERVI DE SOURCE

`m15_diff_v2_v3.txt` recalculé contre le vrai delta v2 → v3 : **363 lignes ajoutées et 134 retirées, identiques ligne pour ligne**. Le diff ne cache ni n'ajoute rien.

Il n'a pas été relu comme une source pour autant : **tout ce qui suit est re-dérivé du texte v3**, jamais du diff. Un diff exact reste un résumé, et un résumé ne se substitue pas à l'artefact (D1-3).

**Forme (§1 du log).** ASCII pur, LF seul, stable par NFC ; terminateur **une seule fois**, en ligne pleine, dernière ligne, rien après — le corollaire de la règle 12 vérifié **avant** l'empreinte. Vingt empreintes citées, **toutes concordantes**, chacune à sa convention déclarée.

**N-10 est tenu** : la v3 étiquette `61f2610f` **[BRUT]** et dit pourquoi (mon log v1 en CRLF). Mes trois fichiers v2 sont en LF, brut = canonique, et la v3 l'écrit.

**ITEM 3 — condition de re-paraphe.** Le gel le déclare CLOS « à re-parapher seulement si domaine ou registre change ». Les **sept** artefacts de la lignée portent les empreintes qu'ils avaient à ma certification v2 : **registre inchangé**, aucun re-paraphe. Le domaine écrit au gel, [2.35, 2.90[, est celui que j'ai dérivé.

---

## 2. LES SIX DÉFAUTS, RE-DÉRIVÉS UN PAR UN

### D-1 — plancher homogène : **RÉPARÉ**

Le plancher est refondu en **courbure**, `PLANCHER_X(b) = K_X · g(LOIN_g, b, LOIN_d)`, dérivé par point intérieur au run. Re-calculé depuis les artefacts et joué sur les trois cas à réponse connue :

| cas à réponse connue | résidu | plancher par point | verdict |
|---|---|---|---|
| **canyon M14 réel** (x_M = 2.48) | **0.2647** | 0.1138 | **MORD, marge 2.33 ×** ✔ |
| fond réel lisse 2.75↔2.85 (x_M = 2.78) | 0.0220 | 0.0569 | muet ✔ |
| fond lisse synthétique k = 8.0 (x_M = 2.69) | 0.0224 | 0.0758 | muet ✔ |

La marge 2.33 × que le gel inscrit se re-dérive exactement. **Et la circularité du cas (2) est levée** : rejoué en **leave-out** (les triplets touchant 2.78 et 2.80 retirés, `K_E⁻ = 24.1149` contre 27.0878), le fond réel reste muet — le verdict tient **hors des données qui ont calibré le plancher**.

**Les trois formes possibles ont été jouées, et une seule passe** (§10 du log) : le plancher **plat** de la v2 laisse tirer le fond réel *et* le vecteur k = 8 ; la variante **g-appariée** que j'ai testée ici rend 0.0220 partout, que le vecteur k = 8 franchit à 0.0224 — **écartée, pas oubliée** ; la forme **courbure** passe les trois. Le gel a retenu la seule qui tient.

### D-2 — centrage vide à 2+2 : **RÉPARÉ**

`n_disc` et `largeur_centrage` sont définis, consignés au JSON quoi qu'il arrive, et la branche `STRUCTURE-RESOLUE-CENTRAGE-NON-DISCRIMINE` est nommée. **Exercée au banc, cas (6)** : configuration 2+2, extremum au PROCHE gauche 2.64 — `C1 ∧ C2 ∧ C3` vraies, `n_disc = 0` → verdict **différent** de `STRUCTURE-AU-SITE-RESOLUE`, `largeur_centrage = 1/20` consignée contre 1/25 au programme complet. Le contrôle **mord**.

### D-3 — trou de partition : **RÉPARÉ**

La partition est recopiée du seul texte du gel et testée sur les **32 combinaisons** de `(C1, C2, C3, n_disc ≥ 1, C4)` : **chacune tombe dans exactement une branche**, et les **six branches sont atteintes**. Exclusive et exhaustive.

La branche du trou, `STRUCTURE-RESOLUE-NON-ATTRIBUEE`, est **exercée sur un profil construit** (cas 5) : `res_S57 = 0.0605 ≤ 0.0608`, `res_S4 = 0.0163 ≤ 0.0163`, `res_E = 0.0768 > 0.0758`. La bande existe : `K_S57 + K_S4 = 27.5498 > K_E = 27.0878`, **marge 1.7 %** — non vide, mais étroite ; voir N-15.

L'avertissement de ma certification v2 — « D-3 ne se corrige pas sans D-1 » — est suivi : les deux sont refondus ensemble, et le fond réel qui tirait C1 en v2 ne la déclenche plus.

### D-4 — signature atteinte par le fond : **RÉPARÉ**

`k_min = min { k : P(Binom(n_eff, b_fond) ≥ k) ≤ 1/20 }`, **queue et comparaison en `Fraction`**, `b_fond = 3/96` exact. Re-dérivé : P(≥1) = 0.5333 > 1/20 ; P(≥2) = 0.1719 > 1/20 ; **P(≥3) = 0.0379 ≤ 1/20 → k_min = 3** ✔. Et `P(k = 0) = 0.4667` : le gel écrit lui-même qu'il n'y a **aucune branche « SIGNATURE ABSENTE »**, l'absence n'étant pas résolvable à cette taille. C'est la bonne façon de le dire.

### D-5 — compte G2 : **RÉPARÉ**

Précédent **M14 nommé** (`273d0a53`), vérifié verbatim à la source : « une recherche à 2g … **consigné sans porte** » — aucune exclusion possible, donc aucune aggravation du risque de plancher manqué. Total re-dérivé : 30 + 5 + 1 + 1 + 1 = **38** ✔.

### D-6 — ensemble F : **RÉPARÉ**

F est défini **par règle**, cinq conditions, appartenance décidée en `Fraction`, `|F|` et les triplets en **sorties**. Re-appliqué : **|F| = 14**, identique à la lecture A de ma certification v2. Aucun compte de points n'est annoncé dans le texte du gel — le piège du « grille 16 » est fermé.

**N-6 à N-12** : tous re-vérifiés au §4 du log — ordre des rangs de la table §1, les trois instances et leur répartition 2 × (−1) / 1 × (+1), l'écart `E − (S4+S57) = 1.110e-16`, D(g)/D(d) arrondis et non tronqués, les deux voisins morts, la citation littérale de la note v5.

---

## 3. CONSIGNATIONS PRÉ-RUN — ITEM 6 et comptes dérivés

Exigées par le gel dans le même message que la certification. Calculées depuis les artefacts, **avant tout run**.

### Courbures (D-1) — ce qui est opposable avant le run

> ### `K_E = 27.087844` · `K_S57 = 21.714077` · `K_S4 = 5.835765`

| | triplet réalisateur | g exact | résidu |
|---|---|---|---|
| `K_E` | (2.75, 2.78, 2.80) | 3/5000 | −0.0163 |
| `K_S57` | (2.75, 2.78, 2.80) | 3/5000 | — |
| `K_S4` | (1.70, 1.73, 1.76) | 9/10000 | — |

### Ensemble F — **sortie**, |F| = 14

`1.70, 1.73, 1.76, 1.84, 1.86, 2.15, 2.22, 2.27, 2.30, 2.60, 2.75, 2.78, 2.80, 2.85`

### Triplets retenus — **sortie**, 8

| triplet | g exact | res_E | K_E local |
|---|---|---|---|
| (1.70, 1.73, 1.76) | 9/10000 | −0.0217 | 24.11 |
| (1.73, 1.76, 1.84) | 3/1250 | −0.0102 | 4.25 |
| (1.76, 1.84, 1.86) | 1/625 | −0.0098 | 6.14 |
| (2.22, 2.27, 2.30) | 3/2000 | −0.0211 | 14.04 |
| **(2.75, 2.78, 2.80)** | **3/5000** | **−0.0163** | **27.09** |
| (2.75, 2.78, 2.85) | 21/10000 | −0.0220 | 10.45 |
| (2.75, 2.80, 2.85) | 1/400 | −0.0095 | 3.80 |
| (2.78, 2.80, 2.85) | 1/1000 | +0.0062 | 6.18 |

### Planchers par point, sur la géométrie du programme complet

*(dérivés au run ; donnés ici pour la configuration 3+3, corde 2.62↔2.73)*

| b | g exact | PLANCHER_E | PLANCHER_S57 | PLANCHER_S4 |
|---|---|---|---|---|
| 2.64 | 9/5000 | 0.04876 | 0.03909 | 0.01050 |
| 2.65 | 3/1250 | 0.06501 | 0.05211 | 0.01401 |
| 2.69 | 7/2500 | 0.07585 | 0.06080 | 0.01634 |
| 2.71 | 9/5000 | 0.04876 | 0.03909 | 0.01050 |

### Comptes dérivés

`programme 6 × 5 = 30` + `G1′ 5` + `G8a 1` + `G4 1` + `G2 1` = **38** ✔ (voir N-14 pour la seule branche où le total vaut 37).

### Seuil de P-M15b

`b_fond = 3/96` exact · `n_eff = 24` au programme complet · **`k_min = 3`** · `P(k = 0) = 0.4667`.

---

## 4. LE BANC — 6 CAS, 6 BRANCHES, TOUTES CLAUSES

Le critère v3 est re-écrit depuis le **seul texte du gel** (PROCHE/LOIN, corde, résidu, plancher par point, seuils, C1/C2/C3, `n_disc`, partition). Son exécutabilité sans interprétation est donc testée en même temps.

| cas | verdict rendu | attendu du gel | clause bloquante |
|---|---|---|---|
| (1) canyon M14 réel | `STRUCTURE-AU-SITE-RESOLUE (FALAISE)` — C1 2.33 ×, C3 2.85 ×, n_disc 2 | ✔ | — |
| (2) fond réel lisse, pseudo-site **2.79** | `PAS-DE-STRUCTURE-RESOLUE` | ✔ | **C1** |
| (2b) le même, plancher **leave-out** | `PAS-DE-STRUCTURE-RESOLUE` | circularité levée | **C1** |
| (3) pentes monotones ↑ et ↓ | `PAS-DE-STRUCTURE-RESOLUE` (résidus exactement nuls) | ✔ | **C1** |
| (3) creux centré 0.10 | `STRUCTURE-AU-SITE-RESOLUE (V-CREUX)` | ✔ | — |
| (3) bosse centrée 0.10 | `STRUCTURE-AU-SITE-RESOLUE (V-BOSSE)` | ✔ | — |
| (3) fond lisse k = 8.0, max en 2.70 | `PAS-DE-STRUCTURE-RESOLUE` | ✔ | **C1** |
| (3) ondulation 0.02 | `PAS-DE-STRUCTURE-RESOLUE` | ✔ | **C1** |
| (4) canal 4 pur | `STRUCTURE-CANAL-4-CANDIDATE` — C3 fausse **exercée**, res_S4 0.0800 > 0.0140 | ✔ | C3 |
| (5) témoin de bande | `STRUCTURE-RESOLUE-NON-ATTRIBUEE` | ✔ | C3 |
| (6) 2+2, extremum en 2.64 | `STRUCTURE-RESOLUE-CENTRAGE-NON-DISCRIMINE` | ✔ | — |

**La leçon du banc v2 est appliquée** : aux cas négatifs la **clause bloquante est consignée**, pas présumée. L'ondulation 0.02, dont la v2 motivait faussement le non-déclenchement par le plancher, bloque bien sur **C1** désormais (résidu 0.0275 contre plancher 0.0488) — le motif écrit et le motif réel coïncident.

---

## 5. TROIS DÉCLARATIONS NOUVELLES

### N-13 — « assignation R-2′ » a changé de forme, pas de résultat

La v3 définit l'assignation par la marge **normalisée** `|w − q/r| / rayon`. Ma certification v2 avait appliqué la marge **absolue** `|w − q/r| − 1.10 · rayon`. Les deux **ne coïncident pas** : elles diffèrent sur **6 des 14 points de F**.

| point | v3 (normalisée) | v2 (absolue) |
|---|---|---|
| 1.73 | 3/2 | 7/4 |
| 1.76 | 2 | 7/4 |
| 2.27 | 2 | 7/3 |
| 2.30 | 2 | 7/3 |
| 2.60 | 3 | 8/3 |
| 2.75 | 3 | 8/3 |

**Ce qui compte est vérifié : les deux lectures rendent le MÊME ensemble F**, parce que le seul usage fait de l'assignation est l'exclusion 5:2, et que les deux rangent 2.42, 2.45 et 2.55 sous 5:2. **Aucun effet sur cette manche.** Mais la v3 écrit « *(Lecture argmin appliquée par machine 2 à la certification v2)* » : c'est le même mot, pas la même règle. « Assignation R-2′ » entre au registre comme terme défini — **toute réutilisation future sur une autre question divergera sur ces six points**, et le gel ne doit pas la présenter comme ma lecture. À corriger d'un mot dans la prochaine version, sans re-certification.

### N-14 — la désignation de G2 dépend du résultat

G2 porte sur `7|PROCHE_droit|+1`, et PROCHE_droit est un **survivant**. Si le flanc droit ne rend aucun survivant, G2 n'a pas de cible : le compte attendu vaut alors **37**, et la forme dérivée `comptés + sautés == attendu` doit porter G2 en **SAUTÉE avec motif**. Le gel ne l'écrit pas. Probabilité sous le q_L local : **0.030** — faible, non nulle. À porter dans la règle de comptage du script, pas dans un nouveau gel.

### N-15 — LA PUISSANCE, chiffrée parce que personne ne l'avait chiffrée

Le correctif D-1 est le mien, et c'est là que son prix se paie. Trois faits, tous re-dérivés :

**(a) Le seul indice mesuré au site dépasse K_E de 12 %.** Ramené à l'unité du seuil : `res_E(2.67 | 2.60, 2.72) = −0.1059` sur `g = 7/2000` → **courbure équivalente 30.244** contre `K_E = 27.088`. Rapport **1.117**. Si cette courbure se conserve à la géométrie du programme, le résidu attendu vaut 0.0726 en 2.65 (plancher 0.0650) et 0.0847 en 2.69 (plancher 0.0758) : **elle tire, à 1.12 ×**.

**(b) Le contrôle positif du gel lui-même passe de justesse.** Le vecteur « creux centré 0.10 » rend `res_E = 0.0667` contre un plancher de 0.0650 : **marge 1.025 ×**. Un creux de profondeur 0.098 au lieu de 0.10 ne tirerait plus.

**(c) Mon attente inscrite est, pour l'essentiel, sous la résolution de la manche.** Ma note v2 §13 écrit `res_E au PROCHE dans [0.03, 0.08]`. Confrontée aux planchers par point : **30 %** de cet intervalle fait tirer C1 en 2.65, **8 %** en 2.69. *Je ne réécris pas mon attente* — elle est inscrite, elle reste. Je consigne que je l'ai formulée avant d'avoir dérivé les planchers, et que le recouvrement est faible.

**(d) Et il faut encore `n_disc ≥ 1`.** Le verdict `ÉTAGE B FALSIFIÉ` exige au moins un flanc à trois survivants. Sous le q_L local : survie point 0.690, P(plancher de comptes) = 0.596, **P(n_disc ≥ 1) = 0.399**.

> **En clair : le falsifieur ne peut prononcer « étage B falsifié » que dans ~40 % des runs, et seulement si la structure dépasse une courbure que le seul indice mesuré ne dépasse que de 12 %.**

**Ce n'est pas un défaut du critère** — les trois formes de plancher ont été jouées et la forme retenue est la seule qui passe le banc. C'est la **résolution de la manche**, et la discipline E27 veut qu'elle soit dite avant le run : la voici. Le gel la couvre déjà à moitié en LIMITATIONS (« moins profonde que le seuil »), **il doit maintenant porter le chiffre**. À inscrire à l'artefact du run et aux LIMITATIONS de la prochaine version — cela ne conditionne pas le dépôt du script.

---

## 6. RÉPONSE POINT PAR POINT AUX SEPT ITEMS

| ITEM | état |
|---|---|
| 1. R-2′, six points propres | **CLOS** (v1) |
| 2. Nouveauté par valeur exacte | **CLOS** (v2) |
| 3. q_L local + faisabilité | **CLOS** (v2) — registre et domaine inchangés, vérifié ; aucun re-paraphe |
| 4. G2 : désignation et total | **CERTIFIÉ** — précédent M14 vérifié à la source, total 38 (voir N-14) |
| 5. Héritage M12/M14, en deux temps | **temps 1 CLOS** (v2) ; **temps 2 DÛ** à l'étape script |
| 6. Courbures + F + triplets, pré-run | **CERTIFIÉ et CONSIGNÉ** au §3 |
| 7. Test négatif du critère v3 complet | **CERTIFIÉ** — 6 cas, 6 branches, clauses bloquantes consignées |

---

## 7. CE QUI RESTE DÛ, ET CE QUE CE LOG NE JOUE PAS

**Reste dû à l'étape script (ITEM 5, temps 2)** — le gel le déclare désormais lui-même :
les **verrous de custody qui mordent** (forme `math.nextafter` sur une valeur importée, octet altéré sur un bloc, **témoin embarqué**), le `--selftest` (partition exhaustive, cas 2+2 qui mord, `k_min` re-dérivé en `Fraction`), et le **pré-vol à moteur factice** avec un banc qui tue (pertes à l'espérance du q_L local, branche G8 en échec, configuration 2+2, branche P-M15c). **Le pré-vol est le seul dispositif qui voie certaines choses** — deux preuves payées le 02/08.

**Ce que ce log ne joue pas** :

1. **Aucune recherche de s\*** : aucun moteur importé, aucune mesure ; tous les s\* viennent des artefacts vérifiés par empreinte.
2. Il ne certifie **pas** `m15_site83_v1.py` : il n'existe pas.
3. La partition est testée sur les **32 combinaisons booléennes**, ce qui prouve l'exclusivité et l'exhaustivité du **texte** — pas que chaque branche soit atteignable par un profil physique. Les cas (4), (5), (6) en exhibent trois ; (1), (2), (3) les trois autres. Les six le sont donc, mais par deux voies différentes, et c'est dit.
4. **Les vecteurs synthétiques du cas (3) portent un S57 que J'AI choisi** (`S57 = E − 0.52`, S4 plat). Le gel exige des attendus à toutes clauses (N-9) mais **ne fixe pas les canaux de ces vecteurs** : un autre choix changerait C3 sans changer C1 ni C2. À fixer au gel si le banc doit être rejoué à l'identique par le script.
5. Le taux de base exclut les **64 lignes de M10** (champ `gros_explosifs` absent) : dénominateur 96, pas 160.
6. Les probabilités du §5 supposent les morts **indépendantes** ; le registre montre le contraire (bloc contigu M13). Elles sont **optimistes**.
7. Il n'écrit aucun fichier.

**Arithmétique** : exacte (`Fraction`) pour distances, R-2′, assignation, appartenance à F, facteurs géométriques `g`, queue binomiale et comparaison à 1/20. Les K_X, résidus et planchers sont des flottants — des mesures. **Le seul flottant qui décide dans ce log est la marge de puissance 1.117 contre 1** (N-15), et elle est exhibée.

---

## 8. MON ATTENTE — NON RÉÉCRITE

Elle est inscrite dans ma note de certification v2, section 13, empreinte `9088ce59`. **Je ne la réécris pas** : le gel v3 la cite en RÉSUMÉ et désigne la note comme texte opposable — c'est la bonne façon de faire, et le résumé est fidèle, je l'ai relu contre l'original.

Les deux machines divergent, et le gel le consigne : machine 1 attend V-CREUX **ou** FALAISE et une conjonction affaiblie ; j'attends **V-CREUX** et la structure **sans** la signature. Son addendum v3 traduit son attente dans la taxonomie D-4 sans retoucher le texte v1 — c'est exactement ce qu'une attente inscrite autorise.

Une seule chose s'ajoute, au titre de N-15 (c) : j'ai écrit `res_E ∈ [0.03, 0.08]` **avant** d'avoir dérivé les planchers par point. Le recouvrement avec ce que la manche peut résoudre est de 8 à 30 %. Je le consigne au lieu de corriger l'intervalle.

---

## 9. CE QUI EST AUTORISÉ MAINTENANT

Le dépôt de **`m15_site83_v1.py`**, sous l'empreinte `e41f4da3685e6d1b930848f1e6ad27cf3c12ce291050cbd61194c0ee2326ba72` (NFC+LF = brut) citée ci-dessus, avec le gel jumeau au docstring et le sha recalculé au démarrage depuis le fichier source. Les consignations pré-run du §3 sont opposables : le script les **re-dérive** au démarrage et s'arrête si elles diffèrent — elles ne se tapent pas.

Restent à porter, sans re-certification du gel : **N-13** (un mot), **N-14** (la règle de comptage), **N-15** (le chiffre de puissance, aux LIMITATIONS et à l'artefact du run).

*machine 2 — `m15_certification_croisee_v3.py` + `.log`, 12 sections, exit 0 : 0 bloquant, 0 échec de contrôle mécanique, 6 défauts vérifiés réparés, 6 branches exercées, 3 déclarations nouvelles.*
