# CERTIFICATION CROISÉE v2 — GEL M15 (P1-b, site 8/3) v2 : **NON CERTIFIÉ**

**machine 2, 07/08/2026.** Trace exécutable : `m15_certification_croisee_v2.py` + `.log` (16 sections, exit 0).
Objet certifié : `m15_pre_enregistrement_v2.md`, bloc du TITRE à `=== FIN DU GEL M15 ===` incluse.

Empreintes de ce dépôt, **étiquetées** (leçon N-10 ci-dessous) — les trois fichiers sont en **LF seul**, donc **brut = canonique NFC+LF** :
`.py` **`26e7353f0197e373…`** · `.log` **`dbbaee825aa28fe8…`**. *(Cette note ne peut pas porter sa propre empreinte : à calculer à réception, même convention.)*

---

## VERDICT

> ## GEL M15 (P1-b) v2 — **NON CERTIFIÉ**
> **6 bloquants (7 assertions), 7 déclarations manquantes, 1 échec de contrôle mécanique.**
> Empreinte du bloc, canonique **NFC+LF** (bloc = fichier entier, 26 563 car.) :
> ### `c92c58e52603fd086b9e987d4439f50f0aa0263f9d3b9cd694dc7892a2245080`
> **Cette empreinte N'AUTORISE PAS le dépôt du script** (E19). Elle identifie la version que je refuse de certifier.

La v2 répare ce que la v1 avait de cassé, et je le dis d'abord parce que c'est acquis : **le critère refondu mord sur le seul canyon mesuré de la campagne.** Codé depuis le seul texte du gel et joué sur `68df6576`, il rend `x_M = 2.48`, `res_E = +0.2647` (le gel écrivait +0.264), forme **FALAISE**, porté par les canaux 5/7 — la clause (2) de la v1 aurait manqué ce canyon, et la v2 ne le manque pas.

Ce qui bloque maintenant est d'une autre nature. La v1 opposait une barre d'instrument (2.5e-05) à une rugosité de fond (0.026) : trois ordres de grandeur, un défaut visible à l'œil. Le PLANCHER corrige cela — **et il le corrige trop juste**. Aux valeurs que je dérive de la règle que le gel déclare, `PLANCHER_E = 0.0220`, et un fond **parfaitement lisse** franchit ce seuil dans la fenêtre du programme. Pas un fond hypothétique : **le fond réel, opposable, mesuré à 2.75–2.85**, celui-là même dont le gel tire sa rugosité.

---

## 1. CE QUI EST CERTIFIÉ DÈS MAINTENANT — machine 1 n'y revient pas

**La réserve v1 tombe (§2 du log).** La note P1 v5 est au répertoire, empreinte canonique `5704987e` **concordante**. La citation est **littérale** : l'entrée **P1-b est bien en section 6** (ligne 185), et elle porte les mots « falsifieur **d'étage B seulement**, étiqueté tel ». Les 15 autres empreintes citées se recalculent, une seule convention près (N-10).

**Les faits déclarés se re-dérivent tous (§3).** (a) rangs (6,2)/(3,1)/(3,1) et **N-4 confirmé** — 22 ≤ 24, mêmes parités, le rang (6,2) à p=4 est *permis* ; (b) `s*₄` = 2.881241 / 7.157439 / 7.462573, facteur **2.590**, **95.6 %** du pas consommé dans [2.55, 2.60] : le programme est entièrement au-dessus du pas ; (c) 2.70 est bien **mort** dans `22fa1760`, ratio explosion/s\* = **0.966** ; (d) **trois** instances, **toutes à degré impair** ; (f) les six E aux valeurs écrites, et `E(2.67)` à **−0.1059** de la corde 2.60↔2.72, **porté par S57** (−0.0860) contre S4 (−0.0198) — « principalement canal 7 » est exact.

**Le constat aggravant du HISTORIQUE est exact (§3).** La clause (2) v1 sur le canyon M14 rend **D(g) = +0.1096, D(d) = −0.0781**, signes opposés. Machine 1 a raison contre elle-même.

**ITEM 2 — CERTIFIÉ (§4).** Les six points sont **neufs par valeur exacte** dans les sept artefacts. Les proximités consignées se re-dérivent (2.62 à 1/50 de 2.60 ; 2.73 à 1/50 de 2.75, qui est point de grille **et** brûlé du pilote). Le motif (2) de non-reconduction de la règle 0.03 est **fondé** : 8/3 est à **1/300** du centième le plus proche.

**ITEM 5, moitié « recopie » — CERTIFIÉE (§7).** N-3 est reconduit **et déclaré** ; les trois barres sont par **corde** et nomment leurs trois points (défaut D-3 v1 corrigé). *L'autre moitié reste due* — voir §12.

**Comptes hors G2 — dérivables (§14).** 6 × 5 = 30, G1′ 5, G8a 1, G4 1, **total 37**. L'ancre G1′ est valide : 2.72 porte 3 entrées de carte et **5 côtés mesurés** dans `fa109da9`.

---

## 2. BLOQUANT D-1 — LE PLANCHER N'EST PAS HOMOGÈNE À CE QU'IL DOIT EXCLURE

Le résidu d'un fond **lisse** de courbure `k` à la corde (a, c) vaut exactement, au point b :

> `résidu = k · (b − a) · (c − b)`

Le gel compare un résidu de M15 à un **max de résidus de F** sans corriger ce facteur géométrique. Or les géométries diffèrent : le triplet qui réalise `PLANCHER_E` est (2.75, 2.78, 2.85), `g = 21/10000` ; l'intérieur M15 le plus central est 2.69 sur la corde 2.62↔2.73, `g = 7/2500` — **1.33 ×** plus grand. À courbure de fond égale, M15 produit un résidu plus grand que son propre plancher.

**Deux témoins, l'un synthétique, l'autre réel.**

**D-1a — le vecteur témoin du gel lui-même.** Le gel écrit, ITEM 7 cas (3) : « extremum hors site (max en 2.70) → **NE TIRE PAS par seuil** (amplitude du vecteur sous le PLANCHER) ». Re-dérivé :

| intérieur | résidu du vecteur `−8.0·(w−2.70)²` | PLANCHER_E | |
|---|---|---|---|
| 2.64 | 0.0144 | 0.0220 | ne tire pas |
| 2.65 | 0.0192 | 0.0220 | ne tire pas |
| **2.69** | **0.0224** | **0.0220** | **TIRE** |
| 2.71 | 0.0144 | 0.0220 | ne tire pas |

L'argmax tombe en 2.69 = PROCHE du flanc droit : **C2 est satisfaite**. Le gel rendrait `STRUCTURE-AU-SITE-RESOLUE` → **ÉTAGE B FALSIFIÉ** sur un fond parfaitement lisse. L'attente écrite du gel est **fausse**, et elle n'était vraie que sous la lecture B de l'ensemble F (voir D-6).

**D-1b — et le fond réel suffit (§10, cas 2).** Le gel me laisse désigner le pseudo-site du tronçon lisse (« par exemple 2.76 »). **2.76 rend le banc injouable** : le groupe droit de F est {2.75, 2.78, 2.80, 2.85} et il ne reste qu'un point à gauche. **Je désigne 2.79** — seul choix donnant 2+2, donc exactement le plancher de comptes de la manche. Avec le plancher **leave-out** (esprit de la règle 14 : on ne teste pas un critère sur les données qui l'ont calibré) :

> `res_E(2.78) = −0.0220` contre `PLANCHER_E^(−) = 0.0217` → **C1 TIRE**, sur quatre points **mesurés** du fond opposable, hors site et hors 5:2.

La courbure maximale du fond opposable est **K_E = 27.09** là où **7.84** suffit à faire tirer la porte en 2.69. Le falsifieur ne distingue pas la structure du site de la courbure de fond que la campagne a déjà mesurée.

### Correctif exigé — FORME EXÉCUTABLE

```
g(a,b,c)      = (b-a)*(c-b)                              [Fraction, exact]
K_X           = max sur les triplets de F de |residu(b|a,c)| / g(a,b,c)
PLANCHER_X(b) = K_X * g(LOIN_g, b, LOIN_d)               [derive AU RUN, par interieur]
seuil_X(b)    = max( PLANCHER_X(b), barre_X(b) )
```

Le plancher devient une **courbure** — homogène à ce qu'il doit exclure — et se dérive **par point intérieur**, donc en forme dérivée (règle 13). **Je l'ai joué sur les trois cas à réponse connue** :

| cas | résidu | PLANCHER_E(b) corrigé | verdict |
|---|---|---|---|
| fond lisse synthétique k=8.0, argmax 2.69 | 0.0224 | 0.0758 | **ne tire pas** ✔ |
| fond lisse **réel** (2.75↔2.85, intérieur 2.78) | 0.0220 | 0.0569 | **ne tire pas** ✔ |
| **canyon M14 réel**, x_M = 2.48 | **0.2647** | 0.1138 | **MORD (2.33 ×)** ✔ |

Le correctif sépare les trois. La marge du canyon tombe de 7.2 × à **2.33 ×** : elle reste décisive, et elle est honnête.

---

## 3. BLOQUANT D-2 — LA CLAUSE DE CENTRAGE EST **VIDE** AU PLANCHER DE COMPTES

Le plancher de comptes est « au moins **2** survivants par flanc ». Énumération exhaustive (§11) :

| configuration | intérieurs | intérieurs **non-PROCHE** | largeur de centrage |
|---|---|---|---|
| 3+3 | 2.64, 2.65, 2.69, 2.71 | 2.64, 2.71 | 1/25 |
| **2+2** (9 cas sur 9) | 2 points | **aucun** | **1/20 à 7/100** |

**À 2+2 — le plancher de comptes exact — tout intérieur est un PROCHE.** C2 est satisfaite **dès que C1 tire** : elle ne teste plus rien. Le verdict garde son nom, `STRUCTURE-AU-SITE-RESOLUE`, pendant que sa résolution de centrage passe en silence de 1/25 à **7/100** — près du triple de ce que les LIMITATIONS déclarent. C'est le piège récurrent de la campagne : un contrôle qui passe sans rien tester.

Et ce n'est pas un cas d'école : sur le domaine q_L que je dérive, **P(les deux flancs à exactement 2) = 0.196**, et la configuration 3+3 — la seule où C2 discrimine — n'arrive que **0.11** fois sur 10 (§9).

### Correctif exigé — FORME EXÉCUTABLE

```
n_disc           = #{ b interieur : b non dans {PROCHE_g, PROCHE_d} }
largeur_centrage = PROCHE_d - PROCHE_g                   [Fraction, consignee au JSON]

STRUCTURE-AU-SITE-RESOLUE  exige  C1 et C2 et C3 ET n_disc >= 1
si C1 et C2 et C3 et n_disc == 0
   -> STRUCTURE-RESOLUE-CENTRAGE-NON-DISCRIMINE
      (consignation ; largeur_centrage au JSON ; AUCUNE lecture 8/3)

selftest : sur la configuration 2+2, un vecteur d'extremum en 2.64 DOIT rendre un
verdict DIFFERENT de STRUCTURE-AU-SITE-RESOLUE. Sinon le test est vide.
```

---

## 4. BLOQUANT D-3 — LA PARTITION DES VERDICTS A UN TROU, ET IL EST NON VIDE

Le gel écrit : `PAS-DE-STRUCTURE-RESOLUE ssi plancher atteint ET non-(C1 et C2 et C3)`. Le cas **C1 ∧ C2 ∧ ¬C3 ∧ ¬(canal 4)** y tombe donc, et se lit « **l'étage B TIENT AU SITE** » — alors qu'une structure de E au site vient d'être résolue au-dessus du plancher. Faux négatif écrit dans la porte.

La bande est **non vide** et se chiffre sur les planchers consignés :

> `PLANCHER_S57 + PLANCHER_S4 = 0.028475 > PLANCHER_E = 0.021954` — largeur de bande **0.006520**
> témoin : `res_S57 = 0.0218` (≤ 0.0223), `res_S4 = 0.0061` (≤ 0.0062) → `res_E = 0.0279` (> 0.0220)

Le résidu de E étant la somme des deux (à la clôture près, N-8), ce témoin est réalisable par un profil réel.

**Et les trois défauts se rencontrent sur mon banc du fond réel (§10, cas 2b)** : C1 tire (D-1), C2 est vraie mais `n_disc = 0` (D-2), C3 est fausse → le cas tombe dans le trou (D-3) et le verdict rendu, `PAS-DE-STRUCTURE-RESOLUE`, est **juste pour une mauvaise raison**. Conséquence pratique, à ne pas manquer : **si machine 1 corrige D-3 seul, ce même fond lisse rendra une consignation de structure.** D-3 ne se corrige pas sans le plancher homogène de D-1.

### Correctif exigé — FORME EXÉCUTABLE (partition, branches exclusives)

```
PAS-DE-STRUCTURE-RESOLUE         ssi plancher de comptes atteint ET NON C1
STRUCTURE-NON-CENTREE            ssi C1 ET NON C2
STRUCTURE-AU-SITE-RESOLUE        ssi C1 ET C2 ET C3        [+ n_disc >= 1, cf. D-2]
STRUCTURE-CANAL-4-CANDIDATE      ssi C1 ET C2 ET NON C3 ET |res_S4| >  seuil4
STRUCTURE-RESOLUE-NON-ATTRIBUEE  ssi C1 ET C2 ET NON C3 ET |res_S4| <= seuil4
   (consignation ; l'etage B N'EST PAS declare tenir dans cette branche)
```

---

## 5. BLOQUANT D-4 — P-M15b : « AU MOINS 1 LIGNE » EST ATTEINT PAR LE FOND **UNE FOIS SUR DEUX**

Taux de base du mécanisme « grossière mordue », **compté** au registre (§13), sur les lignes où le champ existe :

| | mordues | lignes | taux |
|---|---|---|---|
| degré **impair** | 3 | 96 | **0.0312** |
| degré pair | 0 | 87 | 0.0000 |

*(les 64 lignes de M10 sont **hors dénominateur** : le champ `gros_explosifs` y est absent — dit ici, pas caché.)*

Le programme M15 porte **24 lignes impaires**. Sous ce taux de base seul :

| | P |
|---|---|
| **P(X ≥ 1)** — le seuil du gel | **0.5333** |
| P(X ≥ 2) | 0.1719 |
| P(X ≥ 3) | 0.0379 |
| P(X ≥ 4) | 0.0061 |

Le verdict `SIGNATURE PRESENTE` tombe **plus d'une fois sur deux par le fond seul**. Tel qu'écrit, il n'est pas opposable — et l'attente centrale de la v2, la **conjonction** structure + signature, ne peut pas s'appuyer dessus.

Et la **restriction à la parité impaire**, qui fonde le prior (d), n'est pas établie : 3/96 impair contre 0/87 pair → **Fisher unilatéral p = 0.1422**.

### Correctif exigé — FORME EXÉCUTABLE (l'un des deux, au choix de machine 1)

```
(A) seuil derive du fond :
    b     = 3/96   [compte au registre, champ present, M10 exclu]
    n     = 24     [lignes impaires du programme]
    k_min = min{ k : P(Binom(n, b) >= k) <= 0.05 } = 3
    SIGNATURE PRESENTE ssi k_observe >= k_min ; sinon SIGNATURE NON RESOLUE (k et P consignes)

(B) le verdict garde son seuil de 1 mais PORTE SA PROBABILITE SOUS LE FOND :
    "SIGNATURE PRESENTE (k = 1, P_fond = 0.53)"
    -- et l'attente de CONJONCTION est reecrite en consequence.
```

---

## 6. BLOQUANT D-5 — ITEM 4 : LE COMPTE G2 N'EST PAS DÉRIVABLE

Le gel écrit : « G2 INVARIANCE : reconduite selon les **règles de désignation héritées** ; compte dérivé à la certification ». Les deux parents disent des choses **incompatibles**, en nature et en compte (§6, verbatim au log) :

| | M12 `bf9866a7` | M14 `273d0a53` |
|---|---|---|
| compte | **6** (3 degrés × 2) | **1** |
| désignation | « le premier point de la liste (2.22) » | `7\|2.50\|+1`, le degré résonnant |
| tolérance | 10 % | — |
| échec | **ligne EXCLUE** → G7 → point perdu → plancher de comptes | `\|K2/K1 − 1\|` **consigné sans porte** |

Je ne peux pas dériver un compte de deux règles qui diffèrent d'un facteur 6 et dont **une seule peut tuer un point**. De plus, la désignation M12 (« le premier point de la liste ») **n'a aucun référent** dans M15 : la manche n'a pas de liste de priorité. Total : **38** (précédent M14) ou **43** (précédent M12).

### Correctif exigé — FORME EXÉCUTABLE (nommer le précédent ET la ligne)

```
soit  G2 = 1 recherche a 2g sur la ligne 7|PROCHE_droit|+1 ; |K2/K1 - 1| CONSIGNE
           SANS PORTE (precedent M14, 273d0a53)                  -> total = 38
soit  G2 = 3 degres x 2 = 6 recherches sur le point 2.62 (premier point du programme
           dans l'ordre du gel), tolerance 10 %, echec -> LIGNE EXCLUE, qui alimente
           G7 et donc le plancher de comptes (precedent M12)      -> total = 43
```

---

## 7. BLOQUANT D-6 — ITEM 6 : LE TEXTE NE DÉTERMINE PAS L'ENSEMBLE F

Le gel définit F par « points à E **opposable** des artefacts `ad275870 × 7cf3624b` (**grille 16**, aux points où les trois degrés sont **valides** dans leurs artefacts) et `fa109da9` (les 11 valides) ». Les deux moitiés de cette phrase ne disent pas la même chose.

- **Lecture A — la règle déclarée.** « E opposable » + « trois degrés valides » : M11 a **exclu p=4 en 1.30, 1.55 et 1.80** (G6), et sa propre liste `w2_retenus` ne contient que 7 points. Ces points **n'ont pas de E opposable** (G7). → **|F| = 14**.
- **Lecture B — la parenthèse prise pour un compte.** On garde 1.30 et 1.80. → **|F| = 16**.

**Le piège est là** : la lecture B rend **|F| = 16**, le nombre même que le gel cite en « grille 16 ». Un relecteur qui « vérifie 16 » croit confirmer et prend le mauvais F. Et l'écart n'est pas cosmétique :

| | LECTURE A (règle déclarée) | LECTURE B | rapport |
|---|---|---|---|
| triplets (largeur ≤ 11/100) | 8 | 15 | |
| **PLANCHER_E** | **0.021954** | 0.036487 | **1.66** |
| PLANCHER_S57 | 0.022285 | 0.022285 | 1.00 |
| **PLANCHER_S4** | **0.006190** | 0.019662 | **3.18** |

C'est sous la lecture B que l'attente écrite du gel (D-1a) est vraie, et sous la lecture A qu'elle est fausse. **La résolution de toute la manche dépend d'une parenthèse.**

### Correctif exigé — FORME EXÉCUTABLE (F par règle, |F| en SORTIE)

```
F = { w : w dans (grille M10/M11) union (points M12),
          la ligne p=4 en w N'EST PAS exclue G6 dans son artefact,
          les lignes p=5 et p=7 en w NE SONT PAS exclues G6 dans leur artefact,
          w R-2'-propre,  |w - 8/3| > 19/300,  assignation R-2'(w) != 5:2 }
|F| et la liste des triplets sont des SORTIES, consignees au run ET a la
certification ; AUCUN compte de points n'est annonce dans le texte du gel.
```

De plus, **« assignation R-2′ » n'est défini nulle part** dans `bf9866a7` (R-2′ est une règle de propreté, pas d'assignation). J'ai appliqué la lecture *argmin de la marge* (la « pire famille »), qui range bien 2.42/2.45/2.55 sous 5:2 comme le gel l'entend. **À définir au gel**, en toutes lettres.

---

## 8. CONSIGNATION PRÉ-RUN — ITEM 6 (sous réserve de D-6)

Sous la **lecture A**, seule conforme à la règle déclarée, calculés depuis les artefacts, **avant tout run** :

> ### `PLANCHER_E = 0.021954` · `PLANCHER_S57 = 0.022285` · `PLANCHER_S4 = 0.006190`

- **F (14 points)** : 1.70, 1.73, 1.76, 1.84, 1.86, 2.15, 2.22, 2.27, 2.30, 2.60, 2.75, 2.78, 2.80, 2.85
- triplets retenus : **8** ; réalisations — `PLANCHER_E` par (2.75, 2.78, 2.85) largeur 1/10 ; `PLANCHER_S57` par (2.22, 2.27, 2.30) largeur 2/25 ; `PLANCHER_S4` par (1.73, 1.76, 1.84) largeur 11/100
- **courbures maximales** (pour le correctif D-1) : `K_E = 27.088` (triplet 2.75, 2.78, 2.80), `K_S57 = 21.714` (même triplet), `K_S4 = 5.836` (1.70, 1.73, 1.76)
- **E28** : 1.70 entre dans F avec une marge R-2′ de **1/3000** exactement — décidée en `Fraction`, jamais sur un flottant.
- **Marge à surveiller** : `res_S4` du canyon M14 vaut **0.0049** contre `PLANCHER_S4 = 0.0062` — **1.26 ×** seulement. Sous la lecture A, la branche canal-4 est à un cheveu de tirer sur le seul canyon connu.

**Ces valeurs ne sont opposables qu'une fois D-6 tranché.** Si machine 1 retient la lecture B, elles changent et la manche n'a pas la même résolution.

---

## 9. ITEM 3 — q_L LOCAL, ET LE JUGEMENT DE FAISABILITÉ

**Le domaine change tout.** Unité : **ligne signée** (`G6.exclue`), la seule que le registre porte.

| domaine | p=4 | impair | q_L(p=4) | q_L(impair) |
|---|---|---|---|---|
| lignée entière | 16/87 | 5/160 | 0.2278 | 0.0490 |
| **[2.35, 3.10]** — domaine implicite du gel | 10/46 | 3/80 | 0.2847 | 0.0679 |
| **[2.35, 2.90[** — hors bloc de saturation | **1/34** | **3/80** | **0.0855** | **0.0679** |
| [2.55, 2.85] | 1/20 | 1/40 | 0.1424 | 0.0730 |

**10 des 13 morts de [2.35, 3.10] sont les p=4 du bloc [2.90, 3.05]** (M13/M13b) — régime **H-SAT**, pas le site. Le gel les range parmi les morts « CORRÉLÉES au site » : **domaines mélangés au sens d'E27**. Le domaine opposable pour M15 est **[2.35, 2.90[**.

**Faisabilité, en forme dérivée** (1 ligne p=4 + 4 lignes impaires par point) :

```
survie POINT              = (1 - 0.0855) * (1 - 0.0679)^4 = 0.6904
P(>= 2 survivants, 1 flanc)                              = 0.7718
P(plancher de comptes ATTEINT, les deux flancs)          = 0.5957
P(config 3+3 -- la seule ou C2 discrimine)               = 0.1083
P(les DEUX flancs a exactement 2)                        = 0.1960
```

**JUGEMENT : la géométrie est JOUABLE, la lecture ne l'est qu'à 60 %.** Le coût est faible (37 recherches, ~13 s/recherche au registre ≈ 8 min). Mais le plancher de comptes **manque avec probabilité 0.40**, et dans 1 cas sur 5 la manche atteint son plancher dans la configuration 2+2 où la clause de centrage ne discrimine plus (D-2). Le point de redondance par flanc est **porteur** : sans lui, P(les deux flancs complets) = 0.227.

**Et ce chiffre est OPTIMISTE, deux fois** : (i) le modèle binomial suppose les morts indépendantes, or le registre montre le contraire (bloc contigu M13) ; (ii) **fait compté, N-12** — les **deux seuls** points jamais mesurés à moins de 4/100 du site, **2.67 et 2.70, sont morts tous les deux**. C'est exactement la tension que la manche vient mesurer, et c'est aussi ce qui la menace.

---

## 10. LES DÉCLARATIONS MANQUANTES (N-6 à N-12)

- **N-6 — la note v5 énonce le triplet dans deux ordres.** §1 (table) : `8:3 | 11 | (6,2) | (3,1) | (3,1)` ; §2 : « **8/3** — (3,1)/(3,1)/(6,2) ». Ma re-dérivation confirme la table du §1, que le gel suit. Hors chaîne, mais à corriger dans la note, sinon la source contredit ce que le gel en cite.
- **N-7 — un compte inscrit doit être compté.** Le gel écrit « les **deux** instances à côté identifié sont côté −1 ». Les **trois** portent un côté au registre (la clé G6 est `p|w|sgn`), et la répartition est **2 × (−1) pour 1 × (+1)** — l'instance `7|2.67|+1` est côté +1. À reformuler.
- **N-8 — E ≠ S4 ⊕ S57 au bit.** Écart mesuré **1.110e-16** (clôtures différentes : E ferme en `(a−b)+c`, S57 en `(−b)+c`). Aucune porte ne les compare, donc aucun effet — mais le gel consigne « le partage p=5 / p=7 de res_S57 », une addition implicite : à déclarer non exacte, ou à refermer dans un ordre unique.
- **N-9 — l'ATTENDU du cas (1) est incomplet.** Le gel écrit l'attendu du canyon M14 sans **C3**, alors que `STRUCTURE-AU-SITE-RESOLUE` exige C1 ∧ C2 ∧ C3. J'ai vérifié que C3 passe (`res_S57 = +0.2598` contre 0.0223) — mais un attendu pré-écrit doit porter **toutes** les clauses qu'il prétend exercer, sinon il ne teste pas le critère qu'il annonce.
- **N-10 — conventions mélangées, et la faute est d'abord la mienne.** « certification `a944511d`, log `61f2610f`, script `32714630` » cite **deux empreintes canoniques NFC+LF et une en sha BRUT** : mon log v1 a été écrit en **CRLF** (redirection Windows), ses deux empreintes diffèrent, et seule la brute concorde. Les empreintes se livrent **étiquetées**. **Mon dépôt v2 est en LF seul**, brut = canonique, et je l'écris en tête.
- **N-11 — troncature inscrite pour un arrondi.** D(g) vaut **+0.1096** ; le gel inscrit **+0.109**, qui est la troncature (l'arrondi est +0.110). Sans effet ici ; à corriger à l'inscription.
- **N-12 — les deux seuls voisins mesurés du site sont morts** (2.67 M12, 2.70 M13b). À consigner comme fait, dans les LIMITATIONS, à côté de l'asymétrie N-5.

**Et une remarque de méthode sur le banc lui-même** : le gel motive « ondulation 0.02 → NE TIRE PAS » par « le PLANCHER est cette échelle par construction ». Re-dérivé, **C1 tire** (résidu 0.0275 > 0.0220) : ce vecteur ne tire pas parce que **C2 est fausse**. Le verdict tombe juste, le motif écrit est faux. **Un verdict juste pour une mauvaise raison n'est pas un test passé.**

---

## 11. RÉPONSE POINT PAR POINT AUX SEPT ITEMS

| ITEM | état | où |
|---|---|---|
| 1. R-2′, six points propres | **CLOS** (certifié v1, aucun retour) | — |
| 2. Nouveauté par valeur exacte | **CERTIFIÉ** | §1 |
| 3. q_L local + faisabilité | **RENDU** : domaine [2.35, 2.90[, q_L 0.0855 / 0.0679 ; jouable, lisible à 60 % | §9 |
| 4. Comptes G2 dérivés | **BLOQUÉ D-5** — indérivable, deux héritages incompatibles | §6 |
| 5. Héritage M12/M14 | **CERTIFIÉ POUR MOITIÉ** (recopie) ; verrous de custody **DUS** au script | §1, §12 |
| 6. Planchers consignés pré-run | **RENDUS sous réserve D-6** : 0.021954 / 0.022285 / 0.006190 | §8 |
| 7. Test négatif du critère complet | **JOUÉ** : le canyon mord ✔ ; **le lisse mord aussi ✘ (D-1)** | §2 |

---

## 12. CE QUE CE LOG NE JOUE PAS

Exigence de titre — ça ne se coupe jamais.

1. **Aucune recherche de s\*** : aucun moteur importé, aucune mesure. Tous les s\* viennent des artefacts, vérifiés par empreinte.
2. **Il ne certifie pas le script** `m15_site83_v1.py` : il n'existe pas (E19). **ITEM 5 n'est donc couvert que pour moitié** — les **verrous de custody qui mordent** (`math.nextafter`, témoin embarqué), le `--selftest` et le **pré-vol à moteur factice** restent **dus** à l'étape suivante. Le gel doit dire que l'ITEM 5 se certifie en deux temps.
3. Le taux de base de §5 **exclut les 64 lignes de M10** (champ `gros_explosifs` absent). Dénominateur : 96 lignes impaires, pas 160.
4. Il ne mesure pas la résolution de passe ligne par ligne de P-M15b : il en dérive le **taux de base**, pas le mécanisme.
5. **Le banc n'exerce C3 qu'une seule fois** (cas 1) : les vecteurs synthétiques ne définissent que E. La clause qui décide entre 5/7 et canal 4 est testée une fois dans tout ce log.
6. Les q_L sont des bornes supérieures **binomiales** sur des morts supposées **indépendantes** ; le registre montre le contraire. La faisabilité calculée est **optimiste**.
7. Il n'écrit aucun fichier.

**Arithmétique** : exacte (`Fraction`) partout où une **sélection** se joue — distances, R-2′, nouveauté, appartenance à F, facteurs géométriques. Les E, résidus, planchers et taux sont des flottants : ce sont des mesures. **Les deux seuls flottants qui décident dans ce log sont exhibés avec leur marge** : 0.0224 contre 0.0220 (§2, D-1a) et 0.0220 contre 0.0217 (D-1b) — **marges relatives 1.8 % et 1.4 %**. Elles sont minces : un plancher recalculé avec une autre convention de sommation pourrait les inverser. Raison de plus pour que F et les planchers soient consignés **pré-run**, et c'est fait au §8.

---

## 13. MON ATTENTE — machine 2, avant tout run (inscrite ici, jamais réécrite)

Le gel l'exige avant certification ; elle est donc dans ce message, pas dans un tour dédié.

**P-M15a — j'attends `STRUCTURE-AU-SITE-RESOLUE`, et je diffère de machine 1 sur la FORME.** Le matériau : `E(2.67)` est à **−0.106** de la corde, soit **4.8 × PLANCHER_E**, et le résidu se partage **−0.086 en S57 contre −0.0198 en S4** — un creux porté par le canal 7, c'est-à-dire par le rang (3,1) que la dérivation prédit. Machine 1 écrit « V-CREUX **ou** FALAISE ». **J'attends V-CREUX** : le pas de s\*₄ est sous la fenêtre (N-1), donc aucun fond asymétrique ne peut fabriquer une falaise ici, et le résidu de 2.67 est négatif **dans les deux canaux**. Je mets cette branche à **~0.55**, contre ~0.35 pour `PAS-DE-STRUCTURE-RESOLUE` (structure plus étroite que 5/300, invisible aux survivants) et ~0.10 pour une forme que je n'ai pas prévue. Amplitude attendue au PROCHE : **res_E entre 0.03 et 0.08**.

**P-M15b — j'attends k ∈ {0, 1, 2}, donc `SIGNATURE NON RÉSOLUE`** au seuil k_min = 3 que je prescris en D-4. Sous le taux de base, l'espérance est 0.75 ligne sur 24. Je n'attends **pas** d'excès mesurable, et je le dis avant : si k ≥ 3 tombe, la signature devient un fait, et j'aurai eu tort de mon propre fait.

**Sur la manche entière — j'attends une attrition forte au site.** Les deux seuls points jamais mesurés à moins de 4/100 de 8/3 sont morts tous les deux (N-12). Je mets **~0.25** sur le déclenchement de **P-M15c** et **~0.40** sur un plancher de comptes manqué. **Le cœur de mon attente est donc l'inverse de celui de machine 1** : elle attend la conjonction structure + signature ; j'attends **la structure sans la signature**, et une chance sur quatre que la manche ne puisse rien lire du tout.

---

## 14. CE QU'IL ME FAUT EN v3

1. **D-1** : plancher **homogène** (courbure `K_X`, plancher dérivé par point intérieur), et le banc rejoué dessus — le canyon doit mordre, **et les deux fonds lisses doivent se taire**.
2. **D-2** : `n_disc` et `largeur_centrage` au verdict ; branche `STRUCTURE-RESOLUE-CENTRAGE-NON-DISCRIMINE` ; selftest qui **mord** sur la configuration 2+2.
3. **D-3** : partition à cinq branches exclusives ; la branche `STRUCTURE-RESOLUE-NON-ATTRIBUEE` nommée. **À corriger avec D-1, jamais seul.**
4. **D-4** : P-M15b avec seuil dérivé du taux de base (k_min = 3), ou verdict portant sa probabilité sous le fond.
5. **D-5** : G2 — nommer le précédent **et** la ligne désignée ; total 38 ou 43, écrit.
6. **D-6** : F par règle, `|F|` en **sortie** ; « assignation R-2′ » défini en toutes lettres.
7. **N-6 à N-12** déclarés ; ITEM 5 déclaré comme se certifiant **en deux temps**.
8. Le v3 est une **version neuve à certifier** — la qualité d'une clause ne remplace pas sa chronologie (E19). **Aucun code avant.**

*machine 2 — `m15_certification_croisee_v2.py` + `.log`, 16 sections, exit 0 : 7 assertions bloquantes (6 défauts), 1 échec de contrôle mécanique, 5 constats relevés par exécution sur donnée réelle.*
