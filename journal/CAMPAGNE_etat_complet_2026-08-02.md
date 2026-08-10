# LE FANTÔME EN BOCAL — ÉTAT COMPLET DE LA CAMPAGNE
## Métastabilité quantique de l'oscillateur de Pais–Uhlenbeck en interaction
### Document agrégé au 2 août 2026, après le run M12 et sa vérification primaire

> **Statut de ce document.** Synthèse, hors de la chaîne d'artefacts. En cas de
> divergence, les blocs de gel et les deltas de journal font foi, jamais ce
> résumé. Les empreintes citées permettent de remonter à la source.
>
> **Ce qu'il couvre.** La campagne entière : la piste classique fermée du
> bundle 4, les douze manches pré-enregistrées M1–M12 et le pilote M12,
> l'instrument méthodologique, le backlog scientifique, et ce qui reste ouvert.
>
> **Provenance de cette version.** Éditions chirurgicales sur la copie projet
> du 27/07, empreinte mesurée `13157ae8` ; la version certifiée du 27/07 était
> `46d25637`. La présente version dissout ce double état **une fois certifiée
> par machine 2** (diff contre les deux états à la certification). Parties
> touchées : II.3, III, IV, V, VI, VII, VIII, IX, X — dont le retrait de la
> ligne « criblage ×5 » conformément à E27.

---

# PARTIE I — LA QUESTION

Le système est le PU en interaction, sous forme réduite à deux oscillateurs :

> **H₀ = −ω₁n₁ + ω₂n₂ + (g/p)·xᵖ**, avec x = x₁ + x₂

Le mode fantôme porte une énergie de signe négatif : classiquement, rien
n'empêche l'échange de diverger. Pourtant il existe des **îles** de conditions
initiales dont les trajectoires restent bornées, et un **seuil d'amplitude s\***
qui les délimite. Deux questions organisent toute la campagne :

1. **Que fait la mécanique quantique à ces îles classiquement protégées ?**
2. **Qu'est-ce qui fixe le signe et la force de la corrélation entre les
   observables quantiques et les mesures de robustesse classique ?**

Enjeu externe : la viabilité des théories de gravité modifiée à dérivées
supérieures dépend de ce que devient l'instabilité d'Ostrogradsky quand on
quantifie.

---

# PARTIE II — CE QUI EST ÉTABLI

## 1. Le noyau classique — solide, dérivé, reproduit

| Acquis | Statut |
|---|---|
| Réduction à deux oscillateurs | vérifiée **dynamiquement à 10⁻¹³** |
| `K = g·s^(p−2)` seul invariant du seuil | dérivé, puis mesuré à 2g |
| Invariance en g du seuil | **dérivée**, pas seulement constatée |
| Loi des porteurs : porteur résonant de premier ordre **ssi p impair** | démontrée, puis mesurée au spectre (M6) |
| Canyon résonant à ω₂ = 2, côté raide à droite | observé à 2:1 aux deux degrés de M5 |
| Asymétrie de signe invariante en g | dérivée |
| **Symétrie de parité : s\*(+1) = s\*(−1) exactement à p pair** | démontrée sur le code, **vérifiée au bit** (M11) |

## 2. La chaîne gauche est fermée — le résultat le plus abouti de la campagne

Le bord gauche du seuil est **entièrement dérivé**, maillon par maillon, sans
paramètre ajusté a posteriori :

> **Le seuil est l'amplitude où le système, habillant ses propres fréquences
> sous sa contraction adiabatique, entre dans la couche du canal (4,2).**
>
> s\*(ω₂) = solution de **ρ_habillé(s) = 2 − W(ω₂, s)**

- **Auto-habillage** : près de la fuite, les ω_eff migrent vers le voisinage 2:1.
- **Contraction adiabatique** : à actions fixées, le facteur de saturation 3–5
  est dérivé (6/6).
- **W, largeur pendulaire du canal (4,2)** : W = √(V₄₂·H₀″)/ω₁ₑ, avec V₄₂ =
  Λ(g/Δ)²a₁d⁴a₂d² en amplitudes habillées. Λ extraite par réponse forcée.
  **P-DW1′ : 5/5 dans ±35 %.**
- **Assemblage en boucle fermée** : **P-A1 5/5** — s\*_préd/s\*_raf =
  0.954 / 0.989 / 0.992 / 1.009 / 0.978 / 0.939 sur six systèmes, sept points
  chacun, **zéro exclusion, zéro retouche, Λ fixé**.

Résultats annexes : la capture de Floquet linéaire **n'est pas** l'accélérateur
(résultat nul propre, demi-largeur ~0.005) ; c'est la couche chaotique
non linéaire, ×20 plus large. Et **la conjecture C = 1/4 est une affaire de
bord droit** (0.269 ± 0.011) : à gauche, C raffiné glisse de 0.323 à 0.153.

## 3. Le plan (F, Z) — bloc L1, clos ; la classe réfutée par M12

β(p) = **F/(p−2) + Z**, affine en 1/(p−2). **Depuis M12, ceci est une
paramétrisation ajustée par degré, pas une loi de classe.** Les deux mécanismes
candidats y sont deux points, et meurent de la même cause chiffrée — F trop
grand :

| mécanisme | F | Z | statut |
|---|---|---|---|
| équilibre d'énergie | 1.0000 | 0.0000 | mort à tous les degrés |
| fermeture de largeur résonante | 1.3461 | 0.6129 | mort par le **test joint** |

⚠️ **Obligation de documentation permanente (§31.3).** Toute mention de la mort
du second mécanisme porte le qualificatif : *elle tient au caractère joint du
test ; degré par degré, il est à 1.9 (p=5) et 0.2 (p=7) largeurs, donc
apparemment vivant.*

**La forme brute, plus forte que L1-h et découverte tardivement** :

> ln s\*ₚ(ω₂) = A(ω₂)·u_p + B(ω₂), u_p = 1/(p−2), **ponctuellement, sans aucun fit**
>
> d'où **ln s\*₄ − 2.25·ln s\*₅ + 1.25·ln s\*₇ = 0 en chaque point**

Les coefficients (2.25, −1.25) sont **dérivés**, solution unique du système
a/3 + b/5 = 1/2, a + b = 1. L1-h — la forme en résidus — n'en est que la
projection sur le complément des affines, et c'est la projection qui exigeait
un fit.

**M12 a testé cette forme en treize points neufs et l'a réfutée** : 11/11
survivants à |E| ≥ 0.10 (seuil 6), violation dispersée, marges ≥ 2.9×10⁴ σ.
La beauté de la dérivation n'a pas protégé la loi — c'est exactement ce que le
dispositif devait permettre de découvrir.

Acquis annexes : Z(A₂) = 1 exactement ; res_p = φ/(p−2) + ψ ; le nombre
d'adiabaticité N = K/(2ω₂²) ≪ 1 partout, donc mode sain **libre**.

---

# PARTIE III — LES DOUZE MANCHES, ET LE PILOTE

| # | objet | verdict |
|---|---|---|
| M1 | trois degrés, cartes K et T | P-M1b **NON IDENTIFIÉ** — mais le signe de ρ(T,K) change avec la parité |
| M2 | audit et brut | (voir errata E1–E5) |
| M3 | quatre degrés, ρ(T,K) | **H-PARITÉ TUÉE** — p=3 est l'exception, pas « impair » |
| M4 | décomposition en canaux | le canal **(2,1) est le tuyau unique**, quantique et classique |
| M5 | détuning fin + chirurgie | **Q(3) = 57.5**, Q(5) = 4.4 — **H-COURSE TUÉE**, H-PROFONDEUR née |
| M6 | loi des porteurs | **CONFIRMÉE** ; Q déclassé en instrument **ordinal** |
| M7 | H-PROFONDEUR quantique, p=7 | **NON CONCLUANT** — ρ(T₅₆,T₆₄) = +0.60, rangs instables |
| M8 | réplication p=5 | **NON CONCLUANT** — confond de couplage ; gain réel : ρ(T₅₆,T₆₄) = +1.00 |
| M9 | convention (f) intégrale | **NON CONCLUANT** → **C2 déclenchée** |
| M10 | β classique, p=5 et p=7 | **NON CONCLUANT DE PUISSANCE** — G6 a tiré |
| M11 | L1-h, p=4 | **NON CONCLUANT PAR CONSTRUCTION** — G6 a tiré trois fois |
| M12p | pilote : calibration, géométrie, attrition | 24/24 **AU BIT** ; E27 rendu ; **premier arrêt de règle** (N = 13 > 12) |
| M12 | test ponctuel de la classe, 3 degrés | **CLASSE RÉFUTÉE** — 11/11 à \|E\| ≥ 0.10, **VIOLATION DISPERSÉE** |

## Les manches en détail

**M1** — Trois degrés, trois formes de K(ω₂) : la dégénérescence « toute
fonction de ω₂ » est cassée par construction. ρ(T,K) : −1.00 (p=3), +0.20
(p=4), +0.50 (p=6). Le signe change avec la parité — **résultat principal, hors
des deux branches anticipées**.

**M3** — Quatre degrés. ρ(T,K) : −1.00 / +0.20 / **+1.00** / +0.50 pour
p = 3/4/5/6. Le quintique, impair, se range avec les pairs : **H-PARITÉ meurt**,
H-MARGINALITÉ la remplace (post-hoc, étiquetée). Confond restant assumé : pour
les monômes purs, degré, marginalité et ordre trois-ondes sont **un seul axe**.

**M5** — La manche la plus violente. Chirurgie : retirer g·x₁²x₂ fait passer
s\* de 0.52 à 27.2, **R_res = 51.9**. Trois routes indépendantes vers le même
fond cubique : 1.36 / 1.69 / 1.62 — **le fond est universel, et le point
résonant est un canyon creusé dedans**. Le canyon quintique fait ×4.4.
H-PROFONDEUR : *ce qui ordonne la carte de K fixe le signe de ρ(T,K)*.

**M6** — Loi des porteurs **confirmée** par FFT. Et une auto-attaque réussie :
P-M6c déclasse Q de rapport calibré à instrument **ordinal**.

**M9** — Première manche opposable de bout en bout. Un piège nommé au journal :
à N=64, ρ = +0.9429 et le sous-ensemble canonique redonne exactement le +1.00
de M3 — **échos non puissantés, consignés, ni verdicts ni réplication**.

**M10** — G6 tire à ω₂ = 1.25, exactement 5:4, ordre 9 — **le point que le gel
avait désigné comme « assis sur une résonance et de plus grand levier »**. La
garde et la consignation ont convergé par deux chemins indépendants. Sxx tombe
de 39 %, P-M10a devient non concluant. L'argmax de d à 2.75 déclenche la branche
pré-déclarée : **le pic historique à 2.40 était un artefact de grille creuse**.

**M11** — G6 tire à 1.30, 1.55, 1.80. Le fit passe de 9 à 7 points, sous le
plancher de 8 : les trois portes tombent **par construction**. Acquis :
la symétrie de parité au bit. (La comparaison d'attrition inter-manches qui en
avait été tirée est retirée par E27 — les gardes n'étaient pas comparables.)

**M12p, le pilote** — trois livrables : calibration **24/24 au bit**
inter-machines (le contrôle de non-dérive le plus sévère de la campagne) ;
le diagnostic E27 rendu (la géométrie neuve regarde **sous** s\* — bascule
unique 7|1.70|−1, 164 points grossiers propres sur 165) ; attrition mesurée
1/12 → q_L = 0.2296 → N = 13 > plafond 12 → **premier arrêt de règle de la
campagne, exécuté du premier coup** (le plafond de v1–v3 n'était pas dérivé ;
v4 le dérive : épuisement des deux passes 8+8).

**M12** — La première manche conclusive depuis M6, et la première réfutation
propre de la campagne. E = ln s\*₄ − 2.25·ln s\*₅ + 1.25·ln s\*₇, **sans
fit** : 11/11 survivants à |E| ≥ 0.10, marges ≥ 2.9×10⁴ σ, violation
**dispersée** — les deux négatifs sont exactement les deux points d'ordre 7.
Deux pertes G6 → G7 par deux mécanismes (2.38 : fenêtre fine ; 2.67 :
grossière — le mécanisme d'E27, hors degré pair). Le piège de l'indice 40,
ouvert au pilote, exercé une fois sur 67 lignes : la parade a tenu, consignée
par ligne. Custody fermée sur le primaire : `m12_results.json` détenu et
vérifié **au bit** par les deux machines ; vérification indépendante
machine 1 à 100 contrôles. Consignation nommée **P-M12e** : un seul signe au
programme à p=4, la parité étant démontrée puis reproduite au bit.

---

# PARTIE IV — CE QUI EST MORT

| Objet | Cause de décès |
|---|---|
| H-PARITÉ | M3 — p=3 est l'exception, pas la parité |
| H-COURSE | M5 — l'inférence qui la fondait était un artefact de résolution (E15) |
| H-v1, H-v2 (ponts) | routes 0g, 0h — mortes à leurs portes pré-enregistrées |
| SC-v1 (amplitudes fixes) | 0/6 + 0/6 |
| Q comme rapport calibré | M6 / P-M6c → instrument ordinal |
| r(3) et β(3) | E22 — s\* n'est pas défini par le protocole à p=3 |
| Mécanisme « équilibre d'énergie » | 9.7 à 29.5 largeurs |
| Mécanisme « fermeture de largeur résonante » | test **joint** — voir le qualificatif obligatoire |
| Argument n° 1 pour p=4 (levier ×2.25) | l'étendue jackknife de F ne dépend pas du couple de degrés |
| Argument n° 5 (diagnostic de pente) | la couverture ne dépend pas du degré mesuré |
| **La classe ponctuelle ln s\*ₚ = A·u_p + B** | **M12 — 11/11 à \|E\| ≥ 0.10, dispersée, marges ~10⁴ σ** |

**Sept hypothèses pré-enregistrées tuées** au total, dont la plus instructive —
H-PARITÉ — est morte en départageant sa remplaçante.

---

# PARTIE V — CE QUI N'EST PAS MESURÉ

**β n'est pas mesuré.** M10 : non concluant de puissance ; l'étendue jackknife
de F vaut **0.9620**, intervalle [0.4142, 1.3762] — **qui contient les deux
mécanismes morts**. M11 : non concluant par construction.

**La classe est testée — et réfutée** (M12). Deux degrés font un système
exactement déterminé : il ajuste, il ne teste pas. Trois degrés le rendent
surdéterminé ; deux manches à fit avaient échoué, le test **ponctuel** a
délivré. La réfutation ne rétroagit ni sur β, ni sur les mécanismes, ni sur
le criblage pair.

**La jambe quantique est bloquée sur son observable.** Trois manches (M7, M8,
M9), zéro verdict, **aucun ρ quantique significatif à degré impair dans toute
la campagne**. C2 en vigueur : plus aucune manche quantique sans estimateur
**changé et dérivé**. Cahier des charges chiffré, non rempli (→ piste P2 du
backlog, Partie VIII).

**Faiblesse structurelle au registre** : le témoin NULL+ borné n'existe pas aux
degrés impairs (H₀ à p=7 est non borné inférieurement), ce qui affaiblit
rétroactivement les contrôles quantiques de M1 et M3 ; et l'observable en
coquille fixe n'a que ~1.4 sauts de tampon de troncature à p=7 (N = 56).

---

# PARTIE VI — L'INSTRUMENT

## Les gardes

| Garde | Objet |
|---|---|
| G1 / G1′ | régression sur ancres certifiées, ou custody de la chaîne |
| G2 | invariance en g : K mesuré à 2g |
| G3 | identité de force, erreur backward ≤ 10⁻¹² après **chaque** rebinding |
| G4 | pas de temps : dt/2 sur la ligne maximisant **g·s\*^(p−1)** — l'échelle de force, jamais le plus grand s\* |
| G5 | convergence : pas final ≤ 10⁻⁵, filtre sur la **note** et jamais sur la nullité du seuil |
| G6 | **primauté de s\*** : aucune explosion sous 0.98 s\* — a tiré à M10 et M11 |
| G7 | répercussion des exclusions à tous les degrés |
| G8a / G8b | symétrie de parité, sur le seuil et **au bit** sur toute la structure |

## Les quatre règles adoptées en juillet

- **11.** Tout repère pré-déclaré certifie que ses points appartiennent à la
  grille mesurée, **par valeur**, à tolérance déclarée très inférieure à
  l'espacement minimal — jamais sur une étiquette ni un arrondi.
- **12.** Toute extraction dans un artefact gelé s'ancre sur la **structure**,
  jamais sur une sous-chaîne nue. *Corollaire :* un artefact ne contient son
  propre terminateur qu'une fois, en ligne de clôture.
- **13.** Tout seuil dérivé d'une quantité de plan qu'une garde peut modifier
  est gelé **sous sa forme dérivée**, pas numérique.
- **14.** Tout rééchantillonnage portant sur des quantités issues d'un
  ajustement **refait l'ajustement** sur l'échantillon réduit. *Un résidu n'est
  pas une donnée, c'est une sortie du fit.*
- **Candidate 15 (OUVERTE, dossier en cours).** Toute comparaison pouvant
  basculer sous epsilon machine — égalité **ou** inégalité au bord — s'évalue
  en arithmétique **exacte** quand les entrées sont exactes, à tolérance
  déclarée sinon. Six instances au dossier : trois du cycle M12 (sélection
  pilote, pseudo-tie, filtre de nouveauté) et trois de l'artefact primaire
  (d et d/r en float(Fraction) avec contrefactuel division 7/13 à 1 ulp ;
  double témoin d'indice 40 ≤ 2 ulp, verdict par l'indice ; ex æquo Spearman
  détectés en exact et vérifiés au bit).

Les règles 1 à 10 sont au journal maître.

## Vingt-huit errata

E1–E5 (audit du 25/07) · E11–E13 (canal de livraison, certification par
contenu, noms versionnés) · E14 (chaque branche porte sa dérivation) · E15
(l'inférence qui dépasse sa porte) · E16–E17 (unité et convention font partie
de la mesure) · E18 (numéro assigné à la consignation) · E19 (aucun code avant
certification croisée) · E20 (tables inter-manches étiquetées) · E21
(propagation sous-estimée d'un ordre) · E22 (r(3) retiré) · E23–E24 (règle
d'exclusion non appliquée à tous les points) · **E25** (« ρ élevé ⇒ ψ domine »
ne suit pas) · **E26** (7×10⁻⁴ est un écart absolu, pas relatif) · **E27**
(numéro en **collision** entre deux consignations — S42.3 « le gel exige une
consignation que le script ne produit pas » et §43 « la résolution fait partie
de la mesure : comparaison d'attrition M10/M11 interdite par le gel » ;
arbitrage pendant, rien de réservé, règle E18) · **E28** (une re-dérivation
de sélection dans la **même arithmétique** est une réplication, pas un
contrôle).

## Le dispositif à deux machines

Machine 1 gèle, écrit, teste. Machine 2 certifie et exécute. **Aucune ligne de
code avant certification croisée du gel** (E19). Le pré-vol à moteur factice
est **obligatoire** avant tout run long — il a payé trois fois.

Bilan de la séance du 27 juillet : **cinq versions du gel M11, trois du script,
une vingtaine de défauts attrapés, deux errata.** Aucun défaut n'a jamais
touché une porte, un seuil ou une prédiction.

Bilan du cycle M12 (28/07–02/08) : quatre versions du gel (dont le **premier
arrêt de règle** de la campagne, déclenché au pilote par un plafond non
dérivé), trois du script pilote, deux du ponctuel, les défauts S1–S7, **deux
montages dégénérés attrapés au banc d'essai** (un pilote où sP ≡ sF, un banc
où personne ne mourait), et une vérification primaire machine 1 à
**100 contrôles**. La note r5 — une faute d'étiquette machine 1, trouvée par
machine 1 contre l'artefact primaire — documente le dispositif dans l'autre
sens : les littéraux recopiés étaient justes, l'étiquette posée dessus ne
l'était pas.

---

# PARTIE VII — LES LEÇONS QUI VALENT AU-DELÀ DU PROJET

**Ne jamais réécrire une attente.** L'attente de L1 v1, écrite la première et
jamais retouchée, tient sur F et sur Z. La projection déclarée « défavorable »
est plus loin sur les deux. La règle n'a pas seulement protégé l'opposabilité :
**elle a protégé la bonne réponse.**

**Compter, jamais affirmer.** Un script annonçait 71 recherches en en faisant
77. Même famille qu'un seuil figé dérivé d'un plan qu'une garde peut changer.
Et le correctif lui-même a une forme : **compté + sauté == attendu**, parce que
les gardes ont le droit de retrancher.

**Re-dériver, jamais vérifier ce qu'on vous montre.** Un gel exhibait trois
vérifications de sa règle d'exclusion ; les deux machines ont vérifié ces
trois-là, et un point violait la règle depuis quatre versions certifiées.

**Une aiguille écrite dans un texte s'y trouve elle-même.** Dix occurrences,
dont trois dans les tests écrits pour documenter le piège.

**Un test qui ne change pas son objet ne teste rien.** Un contrôle de la
règle 14 était juste par coïncidence ; sa première correction reproduisait le
défaut sous une forme plus subtile. Ce qui a fini par marcher n'est pas d'être
plus attentif — c'est une garde qui mesure **l'effet** du geste, pas sa forme.

**Le selftest et le pré-vol ne se remplacent pas.** Le premier vérifie ce que
le script **calcule**, le second ce qu'il **fait**. Deux défauts bloquants
vivaient dans les branches que seul un parcours complet emprunte.

**Un instrument dégradé ne dit pas « je ne sais pas ».** Il dit « tout est
compatible avec tout », ce qui ressemble beaucoup à un accord. Quand le plan de
M10 s'est effondré, un mécanisme mort a semblé revenir à la vie : c'était la
règle graduée qui avait triplé.

**Un non concluant n'est pas une réfutation.** Le §37 avait retiré une
hypothèse faute de l'avoir vue ; le calcul de puissance a montré qu'une
corrélation vraie de 0.30 aurait été invisible huit fois sur dix.

**Un banc d'essai se conçoit contre ce qui VA arriver.** Deux montages
dégénérés en deux scripts : un pilote où sP ≡ sF rendait la moitié des
contrôles tautologiques, un banc M12 où personne ne mourait — alors que
l'espérance était de 7.1 pertes sur 13. Un banc qui ne peut pas tuer ne
teste pas les branches de mort.

**Un chiffre posé à côté d'un autre EST une comparaison.** La discipline
d'E27 n'est pas de comparer avec réserve — c'est de **ne pas comparer** :
chaque compte avec son domaine, sans mise en regard.

---

# PARTIE VIII — CE QUI EST OUVERT, PAR ORDRE

## 1. Le backlog scientifique — cinq pistes, par rendement attendu

> Discipline commune : tout ce qui naît post-hoc passe par **dérivation à la
> main d'abord**, gel ensuite (précédent : Λ) ; anti-Franken entre chaînes de
> conventions ; une piste n'entre en manche que par un gel certifié. Détail
> et prochains gestes : `SUIVI_campagne_2026-08-02.md`, §5.

| # | Piste | Rendement / coût | Prochain geste |
|---|---|---|---|
| **P1** | **Champ E × loi des porteurs** — le signe de E par famille de résonance est-il dérivable de la parité des ordres croisée aux degrés (4, 5, 7) ? Les deux négatifs de M12 sont exactement les deux points d'ordre 7 | **haut / faible — meilleur pari** | dérivation à la main ; si elle vit, gel prédictif du signe en points **neufs** (cibles : voisinages 5/2 et 8/3) |
| **P2** | **Observable quantique** — le cahier des charges exigé par C2 | le plus haut / élevé | écrire le cahier ; résoudre, pas contourner : témoin borné inexistant à p impair, tampon coquille ~1.4 sauts ; pistes : jumeau borné construit autrement, axe g décroissant |
| **P3** | **Le plan (A₁, A₂) complet** — frontière isotrope-Chirikov ou alignée vallée 1:1 ; **la promesse écrite de la note, §3(a)** | haut / modéré | gel de **géométrie d'échantillonnage** du plan (leçon M10 : la géométrie, jamais une liste) |
| **P4** | **Dérivation de C ≈ 1/4** — forme normale résonante du bord droit (canal (3,1), Chirikov) | haut si elle sort / papier-crayon, risque d'enlisement | tentative bornée dans le temps ; candidat naturel pour l'échange avec Held — « la loi C » = second courrier |
| **P5** | **H-PROFONDEUR — complétion classique** : l'hypothèse survivante | moyen / modéré | R_res à p=7 ; canyon structurellement minimal p=4 en détuning fin |

**Transversal, coût quasi nul** : l'artefact M12 contient de la matière non
exploitée — 39 lignes d'attrition gratuites (règle **exhaustive** pré-déclarée
de mise à jour de q_L), la première géométrie qui regarde systématiquement
sous s\*, retombées et îlots à domaines déclarés. Une exploitation secondaire
**étiquetée** nourrit P1 et P3.

## 2. Le dossier — en retard

Douze manches, 46 deltas, 28 errata, quatorze règles et une candidate, une
chaîne classique fermée, **une réfutation propre** — et **aucun lecteur
extérieur n'a rien vu**. Cinq suivis successifs ont noté que c'était l'étape
au meilleur rendement information/heure. Ce qui bloque n'est pas technique :
**deux décisions humaines** — le contenu du bundle expédié, et les chiffres
périmés de la note FR.

M12 n'entre **pas** dans le corps de la note 25q (contrat de reproductibilité
du préambule, anti-Franken/E17) : une phrase au **mail de couverture**, puis
la note compagnon. Cible : Aaron Held (ENS Paris), puis Deffayet et Vikman,
puis Pisa.

## 3. Le reste

- **Arbitrages et consignations internes** : certification du delta 46 v2 et
  voie r1–r5 (cert. v2 ou erratum) ; collision E27 (S42.3 vs §43) ; promotion
  de la règle 15 ; bilan des fautes M8–M11 — chaque numéro **au moment** de
  sa consignation (E18).
- **p=6** tranche l'hypothèse déposée au §41.6 — désormais **sans appui
  d'attrition** depuis E27 : une seule mesure, à motiver autrement.
- **E27 rattrapable sans remesurer** à M10 : un script de relecture rejouant
  les 32 balayages rendrait min(s explosif)/s\* par ligne. La géométrie M12
  le fait nativement pour ses propres lignes.
- **Le cahier des charges de l'estimateur quantique** → piste P2.
- **Le bord droit** (C = 1/4, canal (3,1), Chirikov) et **« la loi C :
  mécanisme et dérivation »** → pistes P3/P4 et second courrier.

---

# PARTIE IX — LA CHAÎNE D'ARTEFACTS

**Gels certifiés** : M6 · M7 `5c54ac03` · M9 v2 `90019eba` · M10 v8
`c1d42aa5` · M11 v4 `b3c27a14` · gel pilote M12 v3 `03e29c86` · **M12 v4
`bf9866a7` (cert. `f10ffcf3`)**
**Notes de lecture** : bloc L1 v4 `dbe633e2` (clos) · note M11 v1 `51e5d26d`
**Scripts** : `m9_replication_v1.py` `c8ed357b` (moteur) · `m10_exposant_v3.py`
`c3a91f60` · `m11_exposant_v3.py` `80cfa795` · `m12_pilote_v3.py` `663b17e2`
(cert. `774f7de4`) · `m12_ponctuel_v2.py` `c5659f52` (cert. `5faef5ec`)
**Vérifications machine 1** : contresignature `22f4fd53` / `4a1b34e0` ·
**vérification primaire `e03741c5` / `ce4b5a61`** (100 contrôles)
**Résultats** : `m7_results.json` `b7493af7` · `m9_results.json` `41595413` ·
`m10_results.json` `7cf3624b` · `m11_results.json` `ad275870` · pilote
`ed0e27b1` · **`m12_results.json` `fa109da9` — détenu et vérifié AU BIT par
les deux machines** · log de run M12 `a5fddbc6` (canonique `69d1d01d`, CRLF)
· cert. du run (machine 2) `6e608e03`
**Deltas récents** : §41 run M11 `2060e22d` · §42 réconciliation `d6602770` ·
§43 E27 `a94fd607` · §44 v2 `54434d56` · §45 v3 `dd61e570` · **§46 v2
`344e7730`** (remplace v1 `86bfdca1`)

**Convention d'empreinte, tranchée le 27/07** : l'empreinte d'un gel est celle
du **fichier** — bloc, saut de ligne final inclus. L'invariant de clôture rend
les deux identiques, et l'empreinte se vérifie par un `sha256sum`, **sans règle
d'extraction** — or c'est une règle d'extraction qui avait tronqué l'empreinte
de M6 à M10 v6.

---

# PARTIE X — REPRISE À FROID : LES HUIT CHOSES À SAVOIR

1. **La classe est réfutée ; β n'est toujours pas mesuré.** Les deux phrases
   sont vraies ensemble — et la réfutation ne rétroagit sur aucun
   non-concluant.
2. **La forme brute est morte en 75 recherches** : première manche conclusive
   depuis M6, premier arrêt de règle exécuté, custody fermée sur l'artefact
   primaire par les deux machines.
3. **Rien n'est établi sur le criblage à degré pair.** La comparaison
   d'attrition M10/M11 était interdite par le gel M11 (gardes non comparables,
   gain instrumental ×2.5–3.4 au-dessus de 0.90 s\*) : l'unité, la convention
   **et la résolution** font partie de la mesure (E27).
4. **La symétrie de parité est acquise au bit**, reproduite par le pilote et
   le run M12 (P-M12e : un seul signe au programme à degré pair) ; la réserve
   sur la convention s'est levée par une condition écrite d'avance.
5. **Trois phrases ne s'écrivent plus sans qualificatif** : la mort de la
   « fermeture de largeur résonante » (test joint) ; « le côté raide est à
   droite » (observé à 2:1, aux deux degrés de M5) ; l'étendue d'archive 0.2836
   (sans objet).
6. **C2 reste en vigueur** : aucune manche quantique sans estimateur changé
   *et* dérivé — le cahier des charges est la piste P2 du backlog.
7. **Le pré-vol à moteur factice est obligatoire**, et il n'est opposable que
   joué par la machine détentrice des sources.
8. **Le dossier n'est toujours pas parti** — et il a désormais une fin
   racontable.

---

*Fin du document. Les deltas et les blocs de gel font foi.*
