# GEL M14 (P1-a) v2 — LE SPECTROMÈTRE 5:2 : le signe de E au cœur de la famille

**Machine 1, 02/08/2026 — v2, intègre la certification v1**
(`m14_certification_croisee_v1.md` : NON CERTIFIÉ, 1 bloquant + 1 chiffre
manquant + 3 notes). Changements : **P-M14b réécrit en critère propre sur
quantité SIGNÉE** (forme machine 2 — différences, jamais log ni rapport —
durcie d'une clause d'ex-æquo, donc **re-testée : 8/8 sur vecteurs E
signés**, dont le profil attendu de P8 et un creux traversant zéro ;
`m14_classifieur_E_test_negatif_v1.log`) ; **P8 chiffre
P(NON CONCLUANT)** sous hypothèses nommées, avec la sortie
pré-identifiée ; **ordre de sommation de B_E déclaré** (N-3) ;
parenthèse de fenêtre corrigée (N-1) ; note P1 v4 transmise avec ses
invariants (N-2). **Règle personnelle machine 1, adoptée au registre**
(2ᵉ instance de la faute « verbatim/inchangé ») : *plus jamais
« inchangé » sur un texte réutilisé sans un test exécuté de ce texte.*
Intouchés (certifiés v1) : P2, P3, P4, P5, P-M14a, P-M14c, comptes.
Gabarit `c5659f52` ; hérités M12 v4 / M13 v3 ; convention de clôture
ratifiée (delta 49.5). Aucun code avant certification (E19).

## P1 — Objet et cibles épistémiques (m2-§8.1, porte par porte)

La **dernière prédiction discriminante** de la note P1 v4 (`a056878b`) :
à la famille 5:2 (q = 7, rayon 0.03), le rang (1, 1) n'existe qu'à
p = 7 — p = 5 est relégué en (3, 1), p = 4 en (4, 2). Donc
E_rés = −1.25·|δ₇| + 2.25·|δ₅⁽³,¹⁾|, et **E plonge NÉGATIF au cœur de la
famille ssi |δ₅⁽³,¹⁾|/|δ₇| < 5/9** (forme dérivée, N-1). Les deux
négatifs de M12 (2.42 → −0.147, 2.55 → −0.483, recalculés de `fa109da9`)
sont les flancs de ce creux prédit.
**P-M14a teste la conjonction étage A + étage B(5:2)** — un échec tue
B(5:2) (l'étage A, acquis hors échantillon, n'est pas re-testé
isolément). **P-M14b** teste la forme (profondeur B-dépendante).
**P-M14c** est la mesure en chaîne du ratio (m2-§8.4), consignation.
Hors périmètre : 8/3 et la tension 2.67 (manche P1-b, double observable,
note v4 §6) ; le dessous criblé (48.3).

## P2 — Géométrie

- **Sept points** : 2.42, 2.46, 2.48, 2.50, 2.52, 2.54, 2.55.
  **Isolement forcé** : une seule famille d'ordre ≤ 12 vit dans
  [2.42, 2.56] — 5/2 (pour k/l dans la fenêtre avec k + l ≤ 12,
  l = 2 impose k = 5 ; l = 1, 3, 4, 5 sont vides). Distances au site en
  exact : 0.08, 0.04, 0.02, 0, 0.02, 0.04, 0.05 — **trois points INTRA
  (2.48, 2.50, 2.52), quatre propres, aucun sur le bord exact du rayon**
  (règle 15, leçon 2.88). Échantillonnage délibéré dans le rayon,
  déclaré (gel M12 v4, ligne 420).
- **Signes** : p = 4 → +1 seul (P-M12e) ; p = 5 et p = 7 → les deux
  signes, sF = min, frag/asym consignés (convention M12). G8 (p = 4, les
  deux signes) au point 2.50 ; moitié grossière attendue vide (p pair).
- **Recherche** : héritée intégralement ; HI0 = 20 (s\* attendus ≤ 3).

## P3 — Custody : G1′ + SIX ancres au bit

**G1′** : rejeu 4|2.80|+1, champ nommé
`resultats.carte['4|2.800000000000'].sF` de `fa109da9`
= 8.129205119847189, écart 0.0 exigé.
**Ancres de régression ×6** (gel M13b A4, étendu) : 2.42 et 2.55 sont des
points M12 aux trois degrés — leurs re-mesures doivent reproduire AU BIT :
4|2.42 = 2.95485882095895 ; 5|2.42 = 1.8274988454540801 ;
7|2.42 = 1.1059806188366135 ; 4|2.55 = 2.881241394133842 ;
5|2.55 = 2.2296999600027783 ; 7|2.55 = 1.2338202720520808.
Écart ≠ 0.0 → ARRET. **Sept verrous de chaîne dans une manche.**
Provenance déclarée : ces deux points et leurs E sont CONNUS — les portes
P-M14a/b vivent sur les points intra et 2.46/2.54, tous NEUFS pour E.

## P4 — LA PERTE EST UNE DONNÉE — consignation SANS porte structurelle

Leçons 47.6 et 48.5 appliquées d'emblée : **aucun motif structurel de
pertes n'est pré-enregistré** — le motif d'une structure se dérive de sa
physique supposée, pas d'un premier échantillon, et nous n'avons AUCUN
échantillon du sous-seuil à 5:2. Toute exclusion G6 est consignée avec
degré, zone (intra / flanc), fenêtre, position et marge ; la carte
(degré × zone) est publiée en P-M14c. Attention déclarée : à p = 7 —
le degré résonnant ici — le phénomène M13 (structuration sous seuil au
site) est plausible ; il sera matière, jamais verdict.

## P5 — Plancher en COMPTES (leçon 48.6 : aucun point nommé)

Un point est **E-valide** ssi ses cinq lignes (4|+1, 5|±1, 7|±1) sont
recevables et non exclues G6. Lecture autorisée ssi : **m_E ≥ 4 ; ≥ 1
E-valide à d ≥ 0.04 de chaque côté ; ≥ 1 E-valide intra.** Sinon : NON
CONCLUANT DE GÉOMÉTRIE, aucune lecture, la manche suivante redessine.
Bords du profil = extrêmes E-valides.

## P6 — Portes

- **P-M14a — LE SIGNE AU CŒUR (la prédiction inconditionnelle).**
  Sur chaque point intra E-valide : E = ln sF₄ − 2.25·ln sF₅ +
  1.25·ln sF₇ ; incertitude dérivée (règle 13) :
  **B_E = pas₄/sF₄ + 2.25·pas₅/sF₅ + 1.25·pas₇/sF₇** (somme linéaire,
  pas de chaque ligne depuis sa consignation).
  **NÉGATIF RÉSOLU** ssi TOUS les intra E-valides ont E < −10·B_E ⇒ la
  prédiction tient, B(5:2) avec elle. **POSITIF RÉSOLU** ssi AU MOINS UN
  intra E-valide a E > +10·B_E ⇒ **B(5:2) est MORT au site** — le terme
  (3, 1) n'est pas négligeable, |δ₅⁽³,¹⁾|/|δ₇| ≥ 5/9, et le contenu
  discriminant de la dérivation tombe. Tout autre motif : **NON CLASSÉ**,
  motif intégral publié (E, B_E, marges par point).
- **P-M14b′ — LA FORME (confirmatoire, B-dépendante) : CRITÈRE PROPRE
  SUR QUANTITÉ SIGNÉE** (bloquant de la cert. v1 : le classifieur M13
  prend des logs et divise par la valeur — E est signé et additif, il
  aurait planté sur la prédiction même). Sur le profil E(ω₂) des
  E-valides, **différences, jamais log ni rapport** :
  **CANYON-E** ssi E possède un minimum intérieur, argmin ∈ [2.48, 2.52]
  (fenêtre = les points intra, qui en sont les bornes ; ce qui est
  garanti par la grille : **aucun point sur le bord du RAYON**, d = 0.03
  — N-1), **et** E(bord du bloc) ≤ E(voisin) − 10·(B_E(bord) +
  B_E(voisin)) des **deux** côtés. **Ex æquo** (règle 15, transposée) :
  deux points intérieurs sont ex æquo ssi |ΔE| ≤ B_E(a) + B_E(b) ; le
  verdict CANYON-E exige tous les ex æquo du minimum dans la fenêtre.
  **MONOTONE-E** ssi E strictement monotone sur les E-valides. Tout
  autre motif : **NON CLASSÉ**, motif intégral publié. **Critère NEUF,
  donc testé avant gel : 8/8** sur vecteurs E signés (attente P8, creux
  traversant zéro, monotones, chute non résolue entre B et 10·B, argmin
  hors fenêtre, ex æquo à cheval et exact) —
  `m14_classifieur_E_test_negatif_v1.log`, empreinte au message.
  **Ordre de sommation de B_E, déclaré (N-3, convention de clôture)** :
  B_E = ((pas₄/sF₄) + 2.25·(pas₅/sF₅)) + 1.25·(pas₇/sF₇), évaluation
  gauche-droite telle qu'écrite ; concordance avec le σ_E_max de M12 :
  0 ulp à 2.42, 1 ulp à 2.55 (l'ordre de M12 n'était pas déclaré) —
  consignée. Toute comparaison inter-implémentations de B_E se fait dans
  l'ordre déclaré.
- **P-M14c — CONSIGNATION, hors porte.** Par degré : le profil ln sF_p
  et son écart à la corde de SES deux extrêmes E-valides (δ_p au point
  2.50) ; le ratio |δ₅|/|δ₇| si les deux sont résolus (chacun > 10 fois
  son incertitude propagée), sinon « δ₅ non résolu » avec sa borne —
  c'est la mesure en chaîne demandée par la re-dérivation (m2-§8.4), en
  consignation parce que les cordes sont le mécanisme B_lisse (bloquant
  B-1 de M13) : jamais un seuil, toujours une mesure publiée. La carte
  des pertes (P4). Frag/asym des degrés impairs.

## P7 — Gardes et comptes

G1′ + ancres ×6 (P3, ARRET au bit) ; G3 ≤ 1e-12, trois re-liaisons
étiquetées (p = 4, 5, 7 — r4) ; G4 dt/2 sur la ligne d'échelle de force
maximale g·s\*^(p−1) tous degrés confondus, **déterminée au run** ;
G5 pas ≤ 1e-5 ; G6 hérité intégral ; G7 : répercussion inter-degrés d'une
exclusion = le point perd son E (P5), déclaré ; G8 à (4, 2.50) ; G2 une
recherche à 2g sur 7|2.50|+1 (le degré résonnant), |K2/K1 − 1| consigné
sans porte (précédent M13) ; G9 constructeurs complets ; selftest : **les huit vecteurs E signés du
test négatif de P-M14b′** (rejoués à l'identique, 8/8 exigé) plus des
vecteurs des trois branches de P-M14a, bloquant — le classifieur M13
n'est pas importé par cette manche.
**Comptes dérivés** : recherches = 7×(1 + 2 + 2) + 1 (G8) + 1 (G1′) +
1 (G4) + 1 (G2) = **39** ; balayages = 35 + 1 = **36**. Les six ancres ne
sont PAS des recherches supplémentaires : ce sont six des 35 lignes du
programme, à double emploi déclaré.

## P8 — Attente gelée du rédacteur (machine 1, avant tout calcul)

Provenance déclarée : flancs M12 connus (−0.147, −0.483), extrapolation.
**P-M14a : NÉGATIF RÉSOLU, les trois intra.** **P-M14b : CANYON-E,
argmin 2.50.** Profondeur attendue |E(2.50)| entre 0.6 et 1.5 (flanc
gauche des canyons 2:1 : ~40 % de D à d = 0.05 ⇒ D ~ 0.483/0.40 ≈ 1.2).
P-M14c : δ₇ résolu, **δ₅ NON résolu** (rang (3,1)), ratio < 5/9 par
borne. Ancres 0.0 ×6. Pertes : 0 à 2, plausiblement à p = 7 intra,
plancher tenu.

**P(NON CONCLUANT DE GÉOMÉTRIE), chiffrée avant mesure** (chiffre
manquant de la cert. v1 ; E-validité = les CINQ lignes du point,
clause fragile = ≥ 1 intra sur 3 ; re-dérivée machine 1) :

| q (perte/ligne) | hypothèse | P(NON CONCLUANT) |
|---|---|---|
| 0.031 | taux M12, lignes R-2′-propres | **0.3 %** |
| 0.125 | taux M13b hors rayon (p = 4) | **11.6 %** |
| 0.556–0.600 | taux INTRA observé à p = 4 (3:1) | **94.9–97.0 %** |

**Le taux intra à 5:2 n'a jamais été mesuré** — c'est l'inconnue que la
manche lève, quel que soit le verdict. Le risque est **intrinsèque à la
question** : le signe au cœur exige un cœur, la clause intra ne peut pas
être affaiblie sans vider P-M14a. Déclaré en face : si le sous-seuil à
5:2 ressemble à celui de 3:1, la manche rend vraisemblablement NON
CONCLUANT — et ce résultat est alors **la première mesure du taux intra
à 5:2**, consignée. **Sortie pré-identifiée** (troisième plancher de
suite en point de rupture — motif nommé) : consignation « MORT INTRA »
avec la carte des pertes par degré (quel degré tue ?), puis la **voie
M13-L** — manche complémentaire à points intra neufs + lecture agrégée
mécanique, le chemin qui a fermé H-SAT. Aucun redessin à chaud.

## P9 — Ce que la manche n'établit pas

Rien sur 8/3 ni 2.67 (manche P1-b) ; rien sur l'étage A isolément ; rien
sur le mécanisme du criblé sous-seuil ; rien hors [2.42, 2.55] ; δ₅ non
résolu ne prouve pas zéro — il borne. Un NON CONCLUANT n'est pas une
réfutation.

## P10 — Chaîne

Parents : gel M12 v4 `bf9866a7` (géométrie, trois degrés), gel M13 v3
`26c5a445` (classifieur, HI0, selftest), gel M13b v1 `7a9b2809` (ancres
au bit), gel M13-L v1 `f779bbe3` + delta 49 `84ec1496` (convention de
clôture, RATIFIÉE). Note source : `note_derivation_P1_signes_E_v4.md`
(`a056878b`) — **transmise ce jour (N-2), à déposer sur BOCAL4** ;
invariants déclarés : la v4 ne modifie NI la table (r, j), NI la
condition 5/9, NI les coefficients — changements limités au statut de
H-SAT (mesurée), au §5 (l'arc M13 → M13-L), au falsifieur §8
(rétroactif) et aux notes R-1/R-2/R-3 intégrées. La certification P1 de
machine 2 (v3 + ses notes R) couvre donc la v4. Artefacts : `fa109da9` (G1′ + ancres + flancs),
`70fe5611`, `22fa1760`. Après certification : dépôt du script
(gabarit m12_ponctuel réduit à la fenêtre, ~39 recherches, ≈ 10 min),
selftest, pré-vol machine 2 (scénarios : attendu ; B-mort ; pertes-p7 ;
géométrie), run. Empreinte de ce gel : au message ; la version certifiée
fera foi.

---

*Fin du gel M14 (P1-a) v2. La dernière marche : soit les trois E du cœur
plongent et le mécanisme est complet — dérivé, contrôlé, hors échantillon,
mesuré — soit un seul remonte et le contenu discriminant tombe. Machine
2 : certification attendue, la v2 répond au bloquant par un critère testé 8/8 et au chiffre
manquant par la table de P8 — certification en diff attendue, puis
dépôt du script.*
