# Journal de bord — bundle 5, séance de reconstruction indépendante (25/07/2026)

*Séance conduite à partir des SEULES trois notes du dossier projet. Aucun script du
bundle 3ter/4 n'était disponible : tout le moteur (classique + quantique) a été
re-dérivé et ré-écrit de zéro. C'est donc, pour la première fois, une **réplication
indépendante par implémentation séparée**, et non une ré-exécution du même code.*

Fichiers produits : `pu_core.py`, `tools2.py`, `classical.py`, `gate_anchors.py`,
`diag_trace.py`, `route_q1.py`, `route_q2.py`, `calib.py`, `route_A.py`, `checkN.py`.
Données : `calib.json`, `route_q1.json`, `route_q2.json`, `route_A_N56.json`.

---

## 0. Porte d'entrée — le modèle est validé, indépendamment

Dérivation refaite à la main avant codage. L'énergie d'Ostrogradsky calculée
explicitement donne E = −½Δ(ẋ₁²+ω₁²x₁²) + ½Δ(ẋ₂²+ω₂²x₂²) = −ω₁J₁ + ω₂J₂ avec
J_i = Δω_i a_i²/2 — donc H₀ = −ω₁n₁ + ω₂n₂ et x_i = (b_i+b_i†)/√(2Δω_i) **émergent
du calcul** au lieu d'être postulés. Les CI donnent A₁ = s(1+ω₂²)/Δ, A₂ = −s(1+ω₁²)/Δ,
qui se réduisent à (3s, −2s) à (1,√2) : les formes de la note sont des cas particuliers
corrects, et la généralisation à ω₂ quelconque est acquise.

**Contrôle classique (le plus contraignant) :**

| ω₂ | s\* reconstruit | s\* note | écart |
|---|---|---|---|
| √2 | 1.251 | 1.27 | −1.5 % |
| 2.85 | 8.565 | 8.10 | +5.7 % |
| 3.00 | 9.434 | 9.58 | −1.5 % |

**Contrôle quantique :** les ancres §4(a) sont reproduites à ×2–3 près sur tout
le domaine s = 0.5 → 1.6, à condition d'ajuster la pente sur le **transitoire initial**
(cf. §1). **[ANNOTATION E4 : contrôle de cohérence, pas validation — la fenêtre a été choisie en connaissant les cibles ; la validation indépendante est le classique seul. Voir ERRATA.]**

---

## 1. RÉSULTAT NÉGATIF : Γ est un taux à temps court, pas une décroissance soutenue

Diagnostic de forme de P_I(t) (box n ≤ 20, N = 64, (1,√2), g = 0.05) :

| s | chute initiale | comportement ensuite |
|---|---|---|
| 0.5 | 1.000 → 0.994 (t≈1000) | **plat** 0.994–0.997 jusqu'à t = 20 000 |
| 0.9 | 1.000 → 0.93 (t≈200) | fluctue 0.84–0.92, sans dérive |
| 1.2 | 1.000 → 0.82 (t≈75) | fluctue 0.78–0.82 |
| 1.6 | 0.992 → 0.56 (t≈40) | fluctue 0.55–0.60 |

- Pente tardive / pente initiale ≈ **1/50 à 1/100** partout, souvent de signe négatif.
- À s = 0.5, τ = 1/Γ = 1.8×10⁵ prédit P(2×10⁴) = 0.82 ; **mesuré 0.994**. La perte sature.

**Route q1 (pré-enregistrée), N = 48/56/64** — N=72 tombé en OOM, à refaire :

- **P-N1 (convergence de la pente initiale) : PASSE.** Γ(48)/Γ(64) = 1.06 / 0.68 / 0.93 / 0.84
  pour s = 0.5 / 0.9 / 1.2 / 1.6. Cohérent avec le Γ₆₄/Γ₇₂ = 0.89–1.09 de la note. **[ANNOTATION E1 : verdict INVALIDE — critère substitué (48/64 pour 48/72) et 0.68 hors bande [0.7,1.4] compté passant. Verdict opérant : §5. Voir ERRATA.]**
- **P-N2 (plateau indépendant de N) : ÉCHOUE** sur les 4 points pour l'observable
  primaire (poids au-delà de n = 34) : le plateau croît ×1.9 / ×4.0 / ×1.9 / ×1.5 de
  N = 48 à N = 64. Le signal existait déjà dans la note (0.045 → 0.101 de N=44 à 72),
  classé en observation §4(b)(iv) et non en contradiction.

**Énoncé.** Le taux de sortie à temps court est réel, robuste et convergé en N.
La décroissance exponentielle soutenue ne l'est pas. Les « lifetimes τ ≈ 10⁵ → 10² »
de §4(a) et la phrase « durées de vie de cent mille à un million » de la note FR sont
des extrapolations d'un transitoire qui s'arrête. **À corriger avant envoi** : renommer
Γ « taux de sortie à temps court » et reporter le plateau comme second observable.
Ce n'est pas fatal — la note revendique déjà explicitement le seul taux sortant
(§4(b)(iii), §6) — mais l'habillage en durée de vie l'est.

---

## 2. ACQUIS MAJEUR : le contrôle sans fantôme, qui manquait à toute la campagne

**Route q2 (pré-enregistrée), N = 64.** Trois systèmes, protocole strictement identique
(mêmes x_i, mêmes α, mêmes boîtes, même t_ref, même estimateur) :
GHOST = −ω₁n₁+ω₂n₂+(g/4)x⁴ ; NULL+ = **+**ω₁n₁+ω₂n₂+(g/4)x⁴ (borné inf., aucune fuite
possible par construction) ; FREE = g = 0.

| s | Γ fantôme | Γ sans fantôme | rapport | W₃₄ fantôme | W₃₄ sans fantôme |
|---|---|---|---|---|---|
| 0.5 | 5.6e−6 | 5.6e−13 | **1.0e7** | 0.0030 | 0.00000 |
| 0.9 | 3.4e−4 | 2.5e−8 | **1.4e4** | 0.0917 | 0.00000 |
| 1.2 | 2.2e−3 | 4.8e−5 | 46 | 0.1191 | 0.00000 |
| 1.6 | 1.4e−2 | 2.5e−3 | 5.9 (zone grise) | 0.2626 | 0.00068 |

P-Q3 (FREE) : Γ = 1.3e−18 — le pipeline ne fabrique pas de taux.

**Énoncé.** Le signal est de la physique de fantôme, pas l'étalement anharmonique
générique d'un état cohérent. Aux petites amplitudes — précisément là où se joue
« ça fuit même au cœur de l'île » — la séparation est de 4 à 7 ordres de grandeur.
**À ajouter à la note :** c'est le contrôle le plus convaincant du corpus.
Réserve : à s = 1.6 le rapport tombe à 5.9 (zone grise pré-enregistrée) — au-dessus
du rivage, une partie du signal est de l'anharmonicité ordinaire.

---

## 3. Le classique reproduit — y compris la mort de C = 1/4

**Route calib.** Invariant K = g s\*² vérifié (P-A0 : 7/8 ; seul échec à ω₂ = 1.25,
13 %, dans la résolution avouée du bord gauche). C par point, code indépendant :

| ω₂ | 1.25 | 1.35 | √2 | 1.60 | 1.80 | 2.00 | 2.40 | 2.85 |
|---|---|---|---|---|---|---|---|---|
| C (ici) | 0.315 | **0.227** | 0.190 | 0.138 | 0.128 | 0.112 | 0.066 | **0.273** |
| C (bundle 4) | 0.323 | **0.229** | — | — | — | — | — | 0.269 ± 0.011 |

**La dérive du bord gauche, le creux de la vallée (facteur 4 sous la loi à ω₂ = 2.4)
et le plateau ~0.27 à droite sont confirmés par une implémentation séparée.**
Le reframing « 1/4 est une affaire de bord droit » n'est plus interne au bundle.

---

## 4. Piste A : balayage quantique en ω₂ à ħ_eff fixé

**Problème de design résolu en route :** à g fixe, n̄₁(s\*) = K(1+ω₂²)²/(2Δg) vaut ~7 à √2
mais ~500 à ω₂ = 3. Balayer ω₂ à g fixe revient à balayer ω₂ **et** ħ_eff : inattribuable.
Correctif : g(ω₂) calibré par l'invariant K pour imposer n̄₁(s\*) = 7.04 partout
(g va de 0.042 à 2.80 ; n̄₁ réalisé 6.1–7.5).

Mesure à s = 0.7 s\* (N = 56, t_ref = 300 gelé) :

| ω₂ | 1.25 | 1.35 | √2 | 1.60 | 1.80 | 2.00 | 2.40 | 2.85 |
|---|---|---|---|---|---|---|---|---|
| Γ | 3.0e−4 | 3.0e−4 | 1.4e−4 | 6.7e−5 | 6.4e−5 | 8.2e−5 | 6.0e−5 | 3.7e−4 |

- **P-A1 : STRUCTURE.** Amplitude ×6.2 à s/s\* = 0.7 (×3.3 à 0.9). La fuite n'est pas
  uniforme en ω₂ même à ħ_eff et proximité relative fixés.
- **P-A2 : ÉCHEC, dans le sens opposé au pré-enregistré.** Rapport vallée/bords = **0.20**
  (critère RAT : > 3). La fuite quantique est **minimale dans la vallée** de recouvrement
  résonant et **maximale sur les bords**. L'hypothèse « tunneling assisté par résonance
  ⇒ fuite max où le réseau résonant est dense » est **réfutée dans cette géométrie**.
- Stabilité en troncature (checkN) : 1.35 et 2.00 stables à ±7 % de N = 48 à 64 ;
  **ω₂ = 2.85 NON convergé** (5.45e−4 → 3.72e−4 → 2.66e−4). Avec la valeur N = 64,
  le rapport vallée/bord reste 0.30 et 0.23 : la conclusion tient, le point 2.85 est à refaire.

**DÉFAUT DE DESIGN ASSUMÉ.** À n̄ et s/s\* fixés, g_eff = g/Δ² = C·(1+ω₂²)²/(2n̄(ω₂−1)(ω₂+1)²)
— donc g_eff ∝ C × f(ω₂) avec f variant seulement ×1.9 quand C varie ×4.8.
**C et g_eff sont dégénérés par construction dans tout balayage 1-D à ħ_eff fixé.**
L'observation post-hoc « Γ ≈ monotone en C, avec Γ ∝ C^1.0 » est donc réelle mais
le médiateur n'est PAS identifié. Ajouter un second n̄ ne casse pas la dégénérescence
(le facteur de forme en ω₂ est le même). À concevoir : comparaison à g_eff égal et C
différent, ce qui exige de relâcher n̄ et réintroduit ħ — problème ouvert.

---

## 5. P-N1 fermee a N=72 : la convergence n'est PAS uniforme en s

| s | G(48) | G(56) | G(64) | G(72) | G64/G72 |
|---|---|---|---|---|---|
| 0.5 | 5.96e-6 | 9.32e-6 | 5.64e-6 | **9.07e-7** | **6.2** |
| 0.9 | 2.36e-4 | 2.93e-4 | 3.44e-4 | 1.70e-4 | 2.0 |
| 1.2 | 2.04e-3 | 1.84e-3 | 2.20e-3 | 2.01e-3 | 1.10 OK |
| 1.6 | 1.22e-2 | 1.41e-2 | 1.45e-2 | 1.53e-2 | 0.95 OK |

Le plateau bouge de la meme facon a petit s (0.0050 / 0.0122 / 0.0041 / 0.0010) :
ce n'est pas l'estimateur ponctuel, c'est le signal. **P-N1 passe pour s >= 1.2,
ECHOUE pour s <= 0.9.** La note annonce Gamma_64/Gamma_72 = 0.89-1.09 « across the
range » ; ce n'est retrouve qu'au-dessus de s = 1.2. **[ANNOTATION E5 : incompatibilité
avec NOTRE estimateur ; protocole vs physique non tranché. Voir ERRATA.]**

Ce qui survit a petit s : le contrat NULL+ (5.6e-6 contre 5.6e-13, soit 10^7).
**Enonce corrige : a petite amplitude la fuite EXISTE (contre-controle a 7 ordres),
mais sa VALEUR numerique n'est pas convergee en troncature.** A porter en §4(b)(i)
et en §6 : la table de taux est fiable au-dessus du milieu de l'ile, indicative en
dessous.

---

## 6. PISTE B : le recensement est structurel — et positivement controle

**Objection testee.** A w2/w1 irrationnel le spectre libre -w1n1+w2n2 est dense ;
« aucun etat lie » pourrait suivre de l'arithmetique, pas de la geometrie de l'ile.

**Route B (pre-enregistree), N = 64, hbar_eff calibre (nbar1(s*) ~ 7).**
Ile = {n1<=8, n2<=8} ; bord = {n1>34 ou n2>34} ; dominante d'ile = poids > 0.5.

| systeme | niveaux libres distincts | etats d'ile | min(w_out) | lies (<1e-9) |
|---|---|---|---|---|
| sqrt2 (irrationnel) | 4096/4096 | 49 | 6.0e-8 | 0 |
| **3/2 (RATIONNEL)** | **314**/4096 | 60 | 3.9e-8 | 0 |
| phi (irrationnel) | 4096/4096 | 59 | 3.0e-6 | 0 |
| **2 (RATIONNEL)** | **190**/4096 | 57 | 4.8e-7 | 0 |

Rapport irrationnel/rationnel = **1.5**, contre 1e3 exige par l'hypothese DENSITE.
**P-B2 : le recensement est STRUCTUREL.** La densite du spectre libre chute d'un
facteur 21 sans que le resultat bouge. Objection refutee.
*(Nota §11 : tableau ensuite homogeneise en coquille fixe — 2.5e-8 / 8.2e-9 /
1.1e-6 / 1.7e-7, rapport 3 ; conclusion inchangee.)*

**Controle positif P-B3 (indispensable : l'instrument voit-il un etat lie ?)**

| systeme | etats d'ile | min(w_out) | mediane | lies (<1e-9) |
|---|---|---|---|---|
| GHOST sqrt2 | 49 | 6.1e-8 | 1.1e-2 | **0 / 49** |
| NULL+ sqrt2 | 74 | -1.6e-15 (zero machine) | 8.9e-16 | **74 / 74** |
| NULL+ w2=2 | 80 | -2.4e-15 | 3.9e-16 | **80 / 80** |

Dans le systeme sans fantome, TOUS les etats a dominante d'ile sont lies a la
precision machine ; dans le systeme fantome, AUCUN, avec une mediane 10^13 fois
plus haute. Le 1e-9 de la note n'est donc pas un plancher numerique.
**§4(c) est desormais controle dans les deux sens. C'est l'enonce le plus solide
du corpus, et je le mettrais en tete plutot que la table de taux.**


---

## Ouverts — liste revisee (remplace la liste archivee ci-dessous) [reinsere, cf. E8]

1. **Reformuler §4(a)** : « taux de sortie a temps court », plateau en second
   observable, ET mention que la convergence en troncature ne tient qu'au-dessus
   de s ~ 1.2 (§5). C'est la correction la plus urgente avant envoi.
2. **Ajouter NULL+ a la note** : en §4(b) comme contre-controle du taux (§2),
   et en §4(c) comme controle positif du recensement (§6). Deux tableaux, gain maximal.
3. **Promouvoir le recensement** devant la table de taux dans l'abstract.
4. Petit s a N >= 96 : le regime ou la note est la plus ambitieuse est le moins converge.
5. w2 = 2.85 quantique a N >= 80 (g = 2.80, etalement plus large).
6. Casser la degenerescence — **[E2 : casseur identifie = second axe en degre
   d'interaction (x3/x6), cf. ERRATA et M1 ; le design du §12 est annule.]**
7. Pistes classiques inchangees (bord droit (3,1), frontiere (A1,A2), PU a 3 modes).

## Bilan de discipline (mi-seance) [reinsere, cf. E8]

Trois hypotheses pre-enregistrees tuees a ce stade, dont deux de mon propre fait :
RAT (P-A2, refutee dans le sens oppose) et DENSITE (P-B2, refutee). Une prediction
de la note infirmee (P-N1 a petit s). Deux controles manquants construits et passes
(NULL+ dynamique, NULL+ spectral). Un defaut de design avoue (C/g_eff). Un OOM,
un estimateur defaillant et une calibration hors tolerance (phi, P-A0) logues.


---

## (archive — dépassé par §5–§12 et ERRATA) Ouverts (par priorité, remplace l'ancienne liste sur le volet quantique)

1. **Refaire N = 72** (build_H_lean corrige l'OOM) pour fermer P-N1 sur la table publiée.
2. **Redéfinir l'estimateur une fois pour toutes** : Γ ≡ pente sur [0, t_ref], nommé
   « taux de sortie à temps court », plateau reporté à côté. Patcher §4(a) et la note FR.
3. **Ajouter le contrôle NULL+ à la note** (§2 ci-dessus) — gain le plus élevé par ligne écrite.
4. **ω₂ = 2.85 en quantique à N ≥ 80** (g = 2.80, étalement plus large).
5. **Casser la dégénérescence C / g_eff** — design à inventer.
6. **Piste B non faite** : recensement à rapport rationnel (3/2, 2) vs irrationnel (√2),
   pour savoir si « aucun état lié » vient de l'île ou de la densité du spectre libre.
7. Pistes classiques inchangées (bord droit (3,1), frontière (A₁,A₂) complète, PU à 3 modes).

## Discipline

Tenue : prédictions chiffrées en en-tête avant exécution (P-N1/2, P-Q2/3, P-A0/1/2),
règles d'exclusion mécaniques, post-hoc étiquetés. Deux hypothèses tuées cette séance,
dont **une de mon propre fait** (RAT, P-A2). Un défaut de design avoué (dégénérescence
C/g_eff) plutôt que masqué. Un OOM et un estimateur défaillant logués.

---

## 7. Route C : la largeur de la fonction de force ne separe PAS le fantome (negatif de methode)

Pour un etat de Fock |n1,n2> (etat propre exact de H0), decomposition sur les etats
propres de H, N = 48/64/72 :

| Fock | GHOST Amax / G50 | NULL+ Amax / G50 |
|---|---|---|
| \|0,0> | 0.9903 / 0 | 0.9991 / 0 |
| \|2,1> | 0.7554 / 0 | 0.7294 / 0 |
| \|4,2> | 0.305 / 0.691 | 0.419 / 0.938 |
| \|7,3> | 0.246 / 1.185 | 0.312 / 1.055 |

(G50 = 0 signifie qu'un seul etat propre porte plus de 50 % de la force.)

**Enonce.** La largeur de MASSE du paquet est dominee par le melange anharmonique
ordinaire |n1,n2> <-> |n1+-2,n2>, que NULL+ possede aussi : facteur < 2 partout.
La physique de fantome n'est pas dans le corps du paquet mais dans sa QUEUE.
**Consequence pour la note :** la phrase de §4(c) « pure Fock states leak at
comparable rates (|2,1> x3.3 ; |7,3> x31) » mesure en partie de l'anharmonicite
generique, surtout a |7,3> pres du rivage ou NULL+ ne donnait plus que 5.9.
Toute mesure de taux au voisinage du rivage doit etre soustraite du controle.

---

## 8. Route D : LA COQUILLE FIXE — l'observable qui porte la revendication

Coquille S = {35 <= max(n1,n2) <= 45}, IDENTIQUE a tout N (891 etats).
Observable stationnaire, sans propagation, sans fenetre de fit :
T_shell(psi0) = somme_k |<k|psi0>|^2 w_shell(k) = moyenne temporelle du poids dans S.

| etat initial | GHOST T_shell (N=56/64/72) | NULL+ (N=72) | rapport |
|---|---|---|---|
| \|0,0> | 2.41e-5 / 1.19e-4 / 1.83e-5 | 1.04e-17 | **1.8e12** |
| \|2,1> | 4.82e-3 / 4.64e-3 / 3.06e-3 | 3.64e-13 | 8.4e9 |
| \|4,2> | 6.78e-2 / 4.20e-2 / 4.27e-2 | 7.99e-10 | 5.3e7 |
| \|7,3> | 1.20e-1 / 1.34e-1 / 9.74e-2 | 2.07e-6 | 4.7e4 |
| coherent s=0.5 | 3.29e-3 / 9.59e-4 / 2.35e-4 | 8.58e-14 | 2.7e9 |
| coherent s=0.9 | 1.83e-2 / 2.46e-2 / 9.25e-3 | 1.38e-10 | 6.7e7 |
| coherent s=1.2 | 3.98e-2 / 4.73e-2 / 3.20e-2 | 1.22e-7 | 2.6e5 |

- **P-C5 (specificite fantome) : PASSE PARTOUT**, et de tres loin (critere : 1e3).
  Rapports 1e4 a 1e12, **croissants a mesure qu'on descend dans l'ile** : le maximum
  est atteint pour |0,0>, l'etat le plus profond possible. Meme si la valeur fantome
  bougeait d'un facteur 10, le temoin est a 1e-17 et ne peut pas rattraper.
- **P-C4 (convergence) : ECHOUE 4/7.** Stable a x1.6 pres pour |2,1>, |4,2>, |7,3>
  et coherent s=1.2. **Pas converge au fond de l'ile** : coherent s=0.5 chute
  x14 de N=56 a 72, de facon MONOTONE ; |0,0> fluctue x6.5 non-monotonement.
- **Direction du biais (constat, pas conjecture) :** la decroissance monotone a
  s=0.5 indique que les petites boites SURESTIMENT. Les taux publies a petite
  amplitude sont donc probablement des majorants.

**Enonce final du volet quantique.** Ce qui est robuste : l'EXISTENCE et l'ORDRE
DE GRANDEUR DE LA SEPARATION. Ce qui ne l'est pas : la MAGNITUDE, au fond de l'ile.
Formulation utilisable telle quelle :

> *Partant de n'importe quel etat d'ile — y compris l'etat de Fock adjacent au
> fondamental — la probabilite moyennee dans le temps de se trouver dans une
> coquille fixe aux occupations 35-45 est 10^4 a 10^12 fois plus grande dans le
> systeme fantome que dans le systeme borne obtenu en retournant le signe du mode
> fantome. La magnitude de ce poids n'est pas convergee en troncature au fond de
> l'ile ; la separation d'avec le temoin l'est.*

Aucune propagation temporelle, aucune fenetre de fit, aucun plateau, aucune
« duree de vie ». C'est la version defendable de §4(a)+§4(c).

---

## ARCHITECTURE PROPOSEE POUR LE VOLET QUANTIQUE DE LA NOTE

1. **Recensement (§6 ci-dessus)** — aucun etat propre d'ile lie ; controle negatif
   (densite spectrale /21) et positif (74/74 lies dans le temoin). => tete de section.
   Meme monnaie que le theoreme d'avril 2026 : leur enonce est spectral, celui-ci
   aussi. La dichotomie devient reelle au lieu d'analogique.
2. **Coquille fixe (§8)** — le compagnon quantitatif, 10^4 a 10^12.
3. **Taux de sortie a temps court (§1, §5)** — retrograde, valable s >= 1.2,
   renomme, avec le plateau en second observable et l'aveu de non-convergence
   sous s ~ 1.2.

---

## 9. Route B2 : le recensement, VRAIMENT ferme cette fois

*Defaut releve par l'humain : route B n'avait ete mesuree qu'a N=64, avec une
region « hors bord » qui GRANDIT avec la boite, resumee par un MINIMUM
(statistique d'extreme). Reprise avec coquille FIXE, quatre troncatures,
distribution complete, et deux definitions d'ile.*

min(poids dans la coquille fixe 35-45), etats a dominante d'ile :

| systeme | N=48 | N=56 | N=64 | N=72 | 48/72 |
|---|---|---|---|---|---|
| sqrt2 (irr) | 1.18e-8 | 1.42e-8 | 2.48e-8 | 1.95e-8 | 0.60, non-monotone |
| 2 (rat) | 1.17e-7 | 4.18e-8 | 1.68e-7 | 1.53e-7 | 0.77, non-monotone |

- **P-B4 (convergence) : PASSE.** Etendue x2 a x4 sur N=48..72, sans derive.
  La coquille fixe guerit le recensement la ou elle ne guerissait PAS le taux (§8).
- **P-B5 (etat lie emergent) : pas d'alerte.** Non-monotone dans les deux systemes.
- **P-B6 (definition de l'ile) : PASSE parfaitement.** n<=8 -> n<=6 fait tomber le
  nombre d'etats de 51 a 32 et laisse le minimum IDENTIQUE a tous les chiffres.
- Mediane egalement stable : 7.9e-3 / 5.6e-3 / 4.4e-3 / 4.2e-3 (sqrt2).
- **L'etat argmin change avec N** (|0,0> -> |0,1> -> |2,0>) : ce n'est pas un
  outlier fragile mais un PLANCHER partage par plusieurs etats profonds — le
  comportement souhaitable pour une statistique d'extreme.

**Ecart a reconcilier avant publication :** la note annonce min = 9.7e-6 avec
67 etats d'ile (N=72) ; ici 1.9e-8 avec 51 etats. Facteur 500, probablement du a
la definition de l'ile. Pas une contradiction (les deux disent « aucun etat
n'approche d'etre lie ») mais a harmoniser. **Version a publier : coquille fixe.**

**Bilan B :** recensement desormais converge en troncature, insensible a la boite,
verifie sur rationnel ET irrationnel, avec controle positif a 1e-17. C'est
l'observable la plus robuste du corpus.

---

## ETAT DU TIER 1 (fin de seance)

- **B (recensement rationnel/irrationnel) : FERMEE**, apres reprise (§9).
  Bonus non prevu : controle positif (§6).
- **A (balayage en w2) : FAITE MAIS A REFAIRE.** **[dépassé par §10 puis ERRATUM E3]** Le balayage existe (P-A1
  STRUCTURE x6.2, P-A2 anti-correlation) mais il a ete mesure avec le Gamma
  temporel a n1 ~ 3.5, regime ou §5 et §8 ont ensuite montre la non-convergence.
  **A refermer en refaisant le balayage avec T_shell** (stationnaire, sans fenetre)
  — 8 diagonalisations, code deja ecrit. Teste au passage si l'anti-correlation
  est physique ou instrumentale.
- **C (test RAT quantitatif) : NON COMMENCEE.** Le precurseur qualitatif est sorti
  CONTRE RAT (P-A2), ce qui affaiblit la motivation sans remplacer le test.

## Lecon de methode de la seance

Trois observables ont ete essayees pour porter la revendication quantique :
  1. taux temporel Gamma          -> non converge sous s ~ 1.2  (§1, §5)
  2. largeur de fonction de force -> ne separe pas GHOST de NULL+ (§7)
  3. poids en coquille FIXE       -> converge pour le recensement (§9),
                                     pas pour la magnitude au fond de l'ile (§8)
**Regle degagee : toute observable dont la region de definition grandit avec la
troncature est suspecte.** Les deux resultats qui tiennent (recensement, separation
GHOST/NULL+) sont ceux qui n'en dependent pas.

---

## 10. Route A2 : LE BALAYAGE REFAIT EN COQUILLE FIXE — A EST FERMEE

Meme design (g calibre, nbar1(s*) = 7.04, s/s* fixe), mais l'observable temporelle
est remplacee par T_shell (stationnaire, coquille 35-45, sans fenetre de fit).
N = 64, dix valeurs de w2.

| w2 | 1.25 | 1.35 | sqrt2 | 1.50 | 1.60 | 1.618 | 1.80 | 2.00 | 2.40 | 2.85 |
|---|---|---|---|---|---|---|---|---|---|---|
| C | 0.315 | 0.227 | 0.190 | 0.147 | 0.138 | 0.163 | 0.128 | 0.112 | 0.066 | 0.273 |
| T_shell (0.7 s*) | 1.30e-2 | 2.69e-2 | 1.08e-2 | 9.32e-3 | 6.48e-3 | 1.25e-2 | 3.35e-3 | 6.77e-3 | 4.65e-3 | 3.08e-2 |
| T_shell (0.9 s*) | 2.99e-2 | 4.49e-2 | 3.11e-2 | 2.24e-2 | 2.19e-2 | 3.55e-2 | 2.36e-2 | 4.12e-2 | 2.53e-2 | 5.77e-2 |

**A s/s* = 0.7 :**
- **P-A1' : STRUCTURE**, amplitude **x9.2** (le domaine temporel donnait x6.2).
- **P-A2' : ANTI-CORRELATION CONFIRMEE**, rapport vallee/bords = **0.225**
  (le domaine temporel donnait 0.20). Deux observables sans rien en commun —
  l'une propage, l'autre pas — tombent sur le meme nombre a 12 % pres.
  **L'anti-correlation est physique, pas instrumentale.**
- **Correlation de rang T_shell vs C : rho = +0.891.**

**A s/s* = 0.9 :** amplitude x2.6, rapport 0.685, rho = +0.442 — l'effet
s'efface pres du rivage. Coherent avec le domaine temporel (0.67). **C'est un
effet de PROFONDEUR dans l'ile.**

**P-A3' (controle NULL+) : PASSE partout.** GHOST/NULL+ a s = 0.7 s* :
4.9e7 (w2=1.35), 3.2e9 (w2=2.00), 6.0e5 (w2=2.85). Toute la structure est
de la physique de fantome.

**CONVERGENCE DE FORME (route A2c, ajoutee apres verification demandee par l'humain).**
Balayage refait integralement a N = 56. Les valeurs point par point bougent de x0.75
a x2.21 (mediane 1.06) — conforme a la non-convergence de T_shell a nbar1 ~ 3.5 (§8).
Mais les statistiques qui portent la conclusion sont stables :

| | N = 56 | N = 64 | verdict |
|---|---|---|---|
| rapport vallee/bords (0.7 s*) | **0.218** | **0.225** | P-A4 OK (ecart 0.007, critere 0.10) |
| rho(T_shell, C) | **+0.855** | **+0.891** | P-A5 OK (critere > 0.6) |
| amplitude max/min | x5.9 | x9.2 | statistique d'extreme, instable |

**La FORME est convergee meme si les VALEURS ne le sont pas** : le rapport est une
moyenne de moyennes et le bruit de troncature s'y annule. Chiffres a publier : 0.22
et +0.87. **Ne pas mettre l'amplitude en avant** (max/min = statistique d'extreme,
meme piege qu'au §9).

**Verification de transcription :** les six premiers points venaient d'un job tue avant
d'ecrire son JSON et avaient ete retapes a la main depuis le log. Re-collationnes :
les douze nombres correspondent chiffre pour chiffre.

**Reserves honnetes :**
- En retirant w2 = 2.85 des « bords », le rapport monte a **0.328** — juste sous
  le critere pre-enregistre de 0.33. La force de la conclusion s'appuie en partie
  sur ce point, qui a par ailleurs nbar1 = 3.67 (calibration a +6 %) et n'etait
  pas converge dans le domaine temporel.
- w2 = 1.618 (phi) a nbar1 = 3.97 : sa calibration avait echoue P-A0. Sa valeur
  est donc gonflee, et elle est exclue des moyennes vallee/bords de toute facon.
- **La degenerescence C / g_eff (§4) reste entiere.** rho = +0.89 avec C est reel,
  mais g_eff co-varie et le mediateur n'est toujours pas identifie.

**HYPOTHESE POUR LA PROCHAINE MANCHE (a pre-enregistrer, non testee).**
Le RAT s'applique quand les resonances sont une perturbation faible sur un fond
integrable. Ici les resonances de la vallee sont fortes et de bas ordre (2:1 et
3:1 qui se recouvrent) : le regime pourrait etre celui du PIEGEAGE dans les ilots
de resonance secondaires, qui LOCALISE au lieu de delocaliser. Prediction
falsifiable : **le RAT devrait reapparaitre (rapport vallee/bords > 1) a g_eff
plus petit**, quand les resonances redeviennent faibles. Un balayage a nbar1
double (g divise par deux) le teste directement.

---

## ETAT FINAL DU TIER 1

- **A : exécutée — FORME convergée, ATTRIBUTION non atteinte** (cf. ERRATA E2/E3).
  Statistiques confirmées : vallée/bords 0.225 (N=64) / 0.218 (N=56), rho +0.891 / +0.855 ;
  ×9.2 est une statistique d'extrême et ne se met pas en avant (cf. addendum §10) ;
  anti-corrélation reproduite à 12 % près par deux fonctionnelles distinctes des mêmes spectres ;
  controle NULL+ a 1e5-1e9. Reserves loguees ci-dessus.
- **B : FERMEE** (§9), avec convergence en troncature, insensibilite a la boite,
  rationnel + irrationnel, et controle positif a 1e-17.
- **C (test RAT quantitatif) : NON COMMENCEE**, et desormais mal motivee :
  le precurseur est sorti CONTRE le RAT deux fois, par deux observables.
  Remplacee en priorite par l'hypothese de piegeage ci-dessus, qui est le meme
  test a l'envers et coute le meme prix.

---

## 11. Correctif d'homogeneite (erreur repérée en verifiant le kit)

Le tableau rationnel/irrationnel de route B utilisait la region CROISSANTE (au-dela
de n=34) tandis que route B2 utilisait la coquille FIXE : deux definitions sous une
seule etiquette dans le kit. Recalcul des deux systemes manquants en coquille fixe,
N = 64 :

| systeme | niveaux distincts | etats d'ile | min(coquille) | mediane |
|---|---|---|---|---|
| sqrt2 (irr) | 4096 | 49 | 2.5e-8 | 4.4e-3 |
| 3/2 (rat) | 314 | 60 | 8.2e-9 | 2.0e-3 |
| phi (irr) | 4096 | 59 | 1.1e-6 | 1.9e-3 |
| 2 (rat) | 190 | 57 | 1.7e-7 | 5.7e-4 |

Rapport irrationnel/rationnel = 3 (contre 1.5 avec l'ancienne definition) : conclusion
inchangee, tableau desormais homogene. Kit corrige.

---

## 12. LA DEGENERESCENCE C / g_eff EST CASSABLE — j'avais tort  **[ANNULÉ — ERRATUM E2]**

J'ai ecrit au §4 et §10 que la degenerescence n'etait pas cassable. C'est faux : elle
n'est pas cassable par un balayage a UNE dimension, ce qui n'est pas la meme chose.

Les trois boutons sont (w2, g, rho = s/s*). C = C(w2) seul (K est g-invariant).
g_eff = g/Delta^2. nbar1 = rho^2 K (1+w2^2)^2 / (2 Delta g).

Design a deux dimensions : **fixer w2 (donc C constant par construction) et faire
varier g**, en ajustant rho ∝ sqrt(g) pour tenir nbar1 constant. Seuls g_eff et rho
varient alors ; C ne bouge pas. En croisant avec le balayage en w2 a nbar fixe (§10),
on separe les deux. Cout : environ 20 diagonalisations, soit une seance.

**C'est ce qui manque pour que A atteigne son objectif initial** (« les deux moities du
projet se referment l'une sur l'autre »). En l'etat, A a produit une CORRELATION
(rho = +0.89 avec C) dont le mediateur n'est pas identifie — ce n'est pas la fermeture
de boucle annoncee.

---

## ERRATA (audit du 25/07 au soir) — corrections datées ; les sections d'origine sont annotées, rien n'est effacé

**E1 — Faute de protocole (§1).** P-N1 déclaré « PASSE » avec (i) substitution du critère
pré-enregistré — Γ(48)/Γ(72) évalué sur Γ(48)/Γ(64) faute de N=72 ; (ii) un point à 0.68,
hors bande [0.7, 1.4], compté passant ; (iii) « cohérent avec 0.89–1.09 » indéfendable
pour 0.68. Verdict opérant : celui du §5 (passe s ≥ 1.2, échoue s ≤ 0.9). Leçon : un
critère pré-enregistré ne se substitue pas, il s'ajourne.

**E2 — Erreur de raisonnement (§12, annulé).** Le design « ω₂ fixe, g variable, ρ ∝ √g à
n̄_état constant » ne casse rien : à ω₂ fixe, n̄_rivage ∝ 1/g **rigidement** — la force
d'interaction et le ħ effectif sont le même bouton — et ρ ∝ √g réintroduit la profondeur,
dont on sait (0.7 vs 0.9 s\*) qu'elle domine. Structure réelle du problème : dans un
balayage 1-D en ω₂, TOUTE fonction de ω₂ est confondue avec toute autre ; C n'est qu'une
candidate parmi g_eff, W, la géométrie de l'île. Casseur propre : un second axe qui rebat
les dépendances en ω₂ elles-mêmes — le **degré d'interaction** (x³ / x⁶), cf. M1.

**E3 — Incohérences internes.** Trois verdicts successifs sur A (« à refaire » /
« FERMÉE » / « objectif non atteint ») sans renvois. Verdict opérant : A **exécutée**,
FORME convergée (P-A4/A5 : vallée/bords 0.225 / 0.218 ; rho +0.891 / +0.855),
ATTRIBUTION non atteinte (E2). Le bloc final citait ×9.2 — la statistique que l'addendum
du §10 interdit de mettre en avant — corrigé en place.

**E4 — Portée de la « réplication » (§0).** La validation indépendante est le classique
seul (RK4, aucun paramètre ajustable, −1.5 % / +5.7 % / −1.5 %). La porte quantique est un
contrôle de cohérence : l'estimateur (pente du transitoire) a été choisi en connaissant
les cibles.

**E5 — Protocole vs physique (§5).** « La note annonce à tort 0.89–1.09 » était trop
fort. L'écart à s ≤ 0.9 peut venir de définitions d'estimateur différentes (fenêtres de
fit de la note inconnues). La dérive du plateau — que la note signale elle-même —
favorise la lecture physique sans la prouver. À réconcilier définitions en main.

**E6 — Asymétries techniques non dites.** (i) NULL+ jamais testé en troncature (une
seule N par usage) — sans conséquence à 10⁻¹⁷–10⁻⁶, mais à déclarer. (ii) À N=48, la
coquille 35–45 est à deux colonnes du mur dur, là où le produit d'opérateurs tronqués
déforme le plus : mécanisme probable de la surestimation des petites boîtes.
(iii) §3 « P-A0 : 7/8 » périmé après calib2 : 8/10 (échecs : ω₂=1.25 à 13 %, et φ).
(iv) route_C.py plantait (division par zéro) avant d'écrire son JSON : bug cosmétique
corrigé, données dans C.log.

**E7 — Chiffres flatteurs.** « Factor 2 » de l'abstract → **2.1** (1.18 → 2.48e−8).
Ajout : ρ leave-out (sans φ ni 2.85, n=8, Σd²=12 à la main) = **+0.857** — la corrélation
tient sans ses points fragiles. « Deux observables sans rien en commun » → deux
fonctionnelles différentes des mêmes spectres (l'une propage, l'autre non) : l'accord
exclut l'estimateur comme source du motif, pas la diagonalisation.

**E8 — Corruption silencieuse réparée (découverte pendant ce passage de correction).**
Le patch censé insérer §5 et §6 (fermeture P-N1 à N=72 ; recensement rat/irr + contrôle
positif) utilisait un `str.replace` sans assertion, avec un ancrage sans accent
(« priorite » vs « priorité ») : échec muet, sections jamais écrites, alors que §8, §9
et l'ERRATA E1/E5 y renvoyaient. Sections réinsérées ce soir à leur place, avec nota vers
l'homogénéisation du §11. **La copie projet porte le même trou : remplacer le fichier du
projet par celui-ci.** Leçon jumelle de E1 : tout replace sans assertion est un échec
muet en puissance — les éditions suivantes utilisaient déjà des asserts, celle-là non.

**Empaquetage.** README.md (affirmation → script → log/JSON), run_all.sh (~40–60 min,
1 cœur, ~4 Go), route_A2_full.py (version incrémentale robuste du balayage, l'originale
ayant été tuée en vol). Verrue assumée : chemins absolus /home/claude hérités de la
séance, documentée dans le README.

**Décision d'auteur (25/07).** Dossier d'envoi mis **en sourdine** ; le kit v2 (corrigé)
reste prêt, sans échéance. Priorité : avancer.

---

## PROCHAINE MANCHE — pré-enregistrements gelés, en attente de feu

**M1 (recommandée) — second axe : degré d'interaction, p = 3 / 4 / 6.**
But double : casser la dégénérescence « toute fonction de ω₂ » (E2) ET tester
dynamiquement le critère de dominance ℓ = m+n (le quartique est marginal).
Protocole : (a) classique — seuils s\*(ω₂; p) pour p = 3 et 6 sur
ω₂ ∈ {1.35, √2, 2.0, 2.85}, invariant K_p = g·s\*^(p−2) vérifié à deux g (tolérance
10 %) ; (b) quantique — T_coquille à occupation de rivage ≈ 7 et s/s\* = 0.7,
N = 56 et 64.
P-M1a : si le critère de dominance est dynamiquement pertinent, p = 6 change de classe
(perte du plateau de C ou effondrement du seuil) là où p = 4 est marginal.
P-M1b (attribution) : corrélations de rang partielles de T sur la grille (ω₂ × p) —
médiateur = la variable (C vs g_eff) dont la corrélation partielle survit (> 0.5) au
contrôle de l'autre ; si les deux tombent < 0.3 : médiateur non identifié, à écrire tel
quel. n ≈ 8 : puissance faible, critères volontairement grossiers.
Garde-fous : p = 3 non borné d'un seul côté — seuil défini par première explosion avec
les DEUX signes de s, toute asymétrie loguée.

**M2 (en réserve) — test du piégeage, déjà pré-enregistré au §10.** Balayage ω₂ à
occupation de rivage ≈ 14 (g divisé ~2). Prédiction : vallée/bords remonte vers ou
au-dessus de 1 si le régime actuel est du piégeage résonant fort. Faisabilité mémoire :
N ≤ 80–88.

