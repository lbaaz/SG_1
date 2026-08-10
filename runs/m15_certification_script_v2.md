# CERTIFICATION v2 — SCRIPT **CERTIFIÉ** · ERRATUM **CONTRE-SIGNÉ SUR LE FOND, REFUSÉ SUR LA FORME**

**machine 2, 08/08/2026.** Trace : `m15_certification_script_v2.py` + `.log` (8 sections, exit 0), **LF seul, brut = canonique**.

---

## VERDICT, EN DEUX OBJETS

> ### 1. `m15_site83_v2.py` — **CERTIFIÉ**
> Empreinte contresignée, **sha256 brut** : `41ddebcd72b96e64c5a5a4721301d2bf2635059f98a07dec2870f72839395cad`
> Gel jumeau : **la v3 certifiée `e41f4da3`, bit-identique et INCHANGÉE** — l'erratum vit au registre, il ne touche pas au gel. C'est la bonne mécanique.
> 0 échec de contrôle mécanique. selftest 11/11 · **six** scénarios traversés · **matrice 6×6 : 0 sur 30 hors diagonale** · verrous 6/6.
>
> ### 2. `m15_erratum_grossiere_mordue_v2.md` — **fond contre-signé, forme refusée**
> Empreinte : `f4a3508b84d40cb6f194f3f399e070a445b76289a5020ab5151da2fafe5d090e`
> Tout ce qu'il affirme est re-dérivé et **exact**. Un seul point bloque, et il tient en une ligne : **le texte écrit un numéro d'erratum**, ce que le registre interdit — sur ma propre prescription.

---

## 1. LE SCRIPT v2 : QUATRE CHANGEMENTS, ET RIEN D'AUTRE

`sha` concorde ; ASCII, LF ; terminateur unique ; `utcnow(` absent du corps ; la v1 au répertoire est bien celle que j'avais contresignée.

**Le diff est jugé par HUNK, pas ligne à ligne** — sinon une ligne de continuation passe pour clandestine, et j'ai failli le croire à mon premier passage. **9 blocs contigus, chacun portant au moins un marqueur des quatre changements déclarés. Aucun bloc de code clandestin.** Les **5 retraits** sont exactement l'en-tête et les 4 lignes visées par D-2/D-3 — c'est là qu'une régression se cacherait, et il n'y en a pas.

**D-2** — `cote = "sP" if v.get("frag") == 1 else "sM"` : **mot pour mot ma prescription**, et le forçage de `sP` à p=4 a disparu.
**D-3** — `C2 = xM_q in (PROCHEg, PROCHEd)`, appartenance **exacte en `Fraction`**. La clé formatée sert encore à *retrouver* la Fraction via `qmap`, elle ne **décide** plus. J'ai vérifié que `qmap` est **injective** sur les six points — sinon un intérieur serait silencieusement perdu, ce qui aurait remplacé un défaut de forme par un défaut de fond.

**B′ — le trou que j'avais signalé est bouché, et il se voit :**

| scénario | `frag` observés à p=4 |
|---|---|
| B | `[1]` |
| **Bp** | `[-1]` |

La branche `frag = -1` à p=4 — que **aucun** scénario de la v1 n'atteignait — est désormais **traversée et asserée**. C'est exactement le correctif demandé.

**`X_survivants`** est consigné dans les six sorties, complet, **y compris sous plancher manqué** (D : 4 survivants, E : 3). `E(w)` ne sera plus à re-dériver à la main d'un certificat — c'était ma corvée sur le run du jour.

**Comptes dérivés, six scénarios** : A 38/31 · B 43/36 · **Bp 43/36** · C 38/31 · D 38/31 · E 37+1/31.

**Matrice croisée 6×6 : 0 sur 30 hors diagonale.** Le banc discrimine toujours parfaitement, avec un scénario de plus.

**Verrous, six altérations minimales** : octet dans un artefact → ARRÊT ; `nextafter` sur une valeur `sF` → ARRÊT ; gel jumeau altéré → ARRÊT E19 ; instrument altéré → ARRÊT ; `K_E + 6e-7` → ARRÊT pre-run ; `K_E + 4e-7` → **passe**. La frontière déclarée se comporte en frontière.

---

## 2. L'ERRATUM : CE QUE J'AI RE-DÉRIVÉ, ET CE QUI RESTE

### (a) La reprise est *verbatim* — vérifiée, pas crue

Leçon du gel M13 v2 : **un correctif modifié n'est pas un correctif adopté.** J'ai re-comparé après normalisation : **581 caractères, identiques** à ma section 5. Il n'a rien durci, rien allégé.

### (b) Ses chiffres, re-dérivés du registre et du run

| lecture | registre (impair / pair) | `k_min(24)` | run : k |
|---|---|---|---|
| **script** | 3/96 · 0/87 | 3 | **0** |
| (A) | 2/96 · 0/87 | 3 | 0 |
| littérale | 4/96 · 16/87 | 4 | **2** |

**Tous concordent avec l'erratum**, y compris que les deux instances de la lecture littérale sont **exactement les deux lignes impaires perdues** (`5|2.65|+1`, `7|2.71|+1`) et qu'à p=4 elle en ajouterait 4.

### (c) Sa motivation (c) est fondée sur la mesure

Les **six** morts du run portent `gros_explosifs = 0` et une **passe grossière VIDE** — vérifié ligne par ligne. Les appeler « grossières mordues » ferait bien dire au verdict le contraire de ce que la mesure montre. La correction est la bonne, et elle est adossée à la donnée, pas à l'intention.

### (d) LE POINT QUI BLOQUE — le numéro

L'erratum écrit : *« E29 si rien ne s'est intercalé depuis E28 »*.

Le `journal_delta_44_gel_M12_v2.md` §44.6.b dit, **verbatim** :

> « Sa résolution recevra son numéro AU MOMENT de la consignation, et aucun numéro ne s'écrit avant l'arbitrage — **pas même au conditionnel** : écrire un numéro à côté d'un item en attente est la façon dont une réservation commence *(note machine 2, section 5)*. »

Et **deux items attendent déjà** un numéro libre, confirmés au journal : la **résolution de la collision S42.3 / S43** (arbitrage **OUVERT**) et le **bilan des fautes M8-M11**. Rien n'a été consigné depuis E28 — c'est vrai — mais l'**ordre** de consignation n'est pas décidé, donc E29 n'est pas acquis.

**Correctif : supprimer le numéro de la phrase.** Remplacer par : `numéro attribué à la consignation (E18) ; le dernier erratum consigné est E28`. Rien d'autre à toucher.

C'est une réserve de forme, et je la maintiens pour une raison de fond : la règle enfreinte est celle que j'ai moi-même prescrite, et une règle qu'on n'applique pas à son auteur ne tient pas longtemps.

---

## 3. LES FAUTES VERSÉES AU REGISTRE — JE LES CONTRE-SIGNE

L'erratum verse trois fautes, et je les confirme toutes les trois :

- **M1-a** : la phrase ambiguë est de machine 1.
- **M1-b** : le script a **résolu l'ambiguïté en silence**. C'est la faute la plus intéressante des trois : la résolution était **la bonne**, et c'est quand même une faute. Un script qui tranche une définition de porte sans le déclarer retire le choix à la certification.
- **M2-a** : la mienne. J'ai certifié le gel v3 en vérifiant que la définition était *héritée*, sans la **ré-appliquer au registre**. Vérification d'héritage, pas de contenu. Je la maintiens telle qu'elle est écrite.

---

## 4. CE QUE CE LOG NE JOUE PAS

1. **Aucune mesure.** Moteur factice, et la v2 **ne touche pas au run exécuté** `96d78407` : aucune valeur de physique ne bouge ici.
2. Il ne re-certifie ni le gel v3 (`e41f4da3`, vérifié bit à bit dans le jumeau) ni le pilote.
3. **Il ne consigne pas l'erratum : il le contre-signe.** La consignation au registre et l'attribution du numéro restent des actes de registre.
4. La matrice 6×6 montre que le banc **discrimine**, pas qu'il **épuise**. Trois branches de la partition D-3 — `CANAL-4-CANDIDATE`, `NON-ATTRIBUEE`, `NON-CENTREE` — restent exercées au **seul selftest**, sur profils construits. Inchangé depuis la v1, et toujours à dire.
5. Le correctif D-2 est vérifié **présent** et sa branche **traversée** ; son effet reste **nul par construction** (barre 1619 × sous le plancher). Aucun verdict de la lignée ne changera pour autant — la v2 est une version d'héritage, pas une correction de résultat.
6. Il n'écrit aucun fichier hors du bac à sable et de ce log.

Détail de répertoire réglé : le brouillon cité `8e582552`, qui n'était qu'aux Downloads, est **entré au répertoire** — sa citation par empreinte résout désormais localement.

---

## 5. CE QU'IL RESTE

1. **Retirer le numéro de l'erratum**, le consigner, et **attribuer le numéro à ce moment-là**. Dès qu'il est consigné, le verdict du run — `NON CONCLUANT DE GÉOMÉTRIE` — devient **opposable** : je l'ai déjà re-dérivé sous la définition corrigée, il ne bougera pas.
2. **Gel v4** : porter la définition corrigée, **N-13** et **N-15** (le chiffre de puissance aux LIMITATIONS).
3. Ma propre prescription, née du run et pas encore portée : **le q_L se dérive sur le plus petit domaine contenant le programme**, jamais sur le plus grand domaine compatible. C'est ce qui a manqué à l'ITEM 3 de cette manche.
4. Les canaux des vecteurs synthétiques, si le banc de partition est rejoué.

*machine 2 — `m15_certification_script_v2.py` + `.log`, 8 sections, exit 0 : script v2 CERTIFIÉ, erratum contre-signé sur le fond, une réserve de forme sur le numéro.*
