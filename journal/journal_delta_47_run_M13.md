# Delta 47 — run M13 : NON CONCLUANT DE GÉOMÉTRIE ; deux faits consignés

Date : 2026-08-02 (machine 1). Contresignature légère (régime deux vitesses,
plan d'action §5.0) : 26 contrôles, TOUT CONCORDE.

## 47.1 Chaîne

Gel M13 v3 `26c5a445` (cert. `b1ff00be`) → script v1 `94dedaa0` (dépôt
machine 1) → **v1b `1cb38518…`** : quatre éditions machine 2, toutes hors du
chemin de mesure, consignées dans l'artefact
(`meta.declarations.editions_machine2`) et à la certification — écart à la
répartition machine 1/machine 2, déclaré. Selftest 9 sections exit 0 ;
pré-vol six scénarios, toutes branches, invariant à terme sauté exercé ; run
BOCAL4 ; réconciliation machine 2, 8 sections TOUT CONCORDE
(`m13_reconciliation_machine2_v1.py` `2c46dce5`, `.log` `3742e4d1` brute) ;
certification du run `96cd155a`. JSON `m13_results.json`
**`70fe5611…077f99`** — détenu et vérifié au bit par les deux machines.
Comptes dérivés : 13 + 0 = 13 recherches, 10 + 0 = 10 balayages.

## 47.2 Verdict

**P-M13a : NON CONCLUANT DE GÉOMÉTRIE** — m = 4 < plancher 7. Le plancher
pré-déclaré a mordu exactement comme écrit. **Lecture des pertes (gel §5) :
« attrition simple »** — quatre pertes à d ≤ 0.06 (2.94, 2.97, 3.00, 3.03)
**et une à d = 0.10 (2.90)** : la clause « aucune au-delà » est violée par un
point, la règle rend attrition simple, et elle n'est pas réécrite.
**H-SAT n'est ni mesurée ni réfutée.** Les trois signes du groupe 3:1 de la
note P1 restent **accommodés**, pas expliqués. Aucune des deux branches du
gel n'est atteinte : la manche a rendu une troisième chose.

## 47.3 Les deux faits consignés (matière, pas verdicts)

**(a) Un bloc contigu de cinq pertes G6 exactement au site.** 2.90–3.03,
zéro perte en dehors, mécanisme UNIQUE sur les cinq : explosion dans la
fenêtre **fine**, entre 0.924 et 0.948 s\*, jamais dans la grossière
(ad8dd209 tient une deuxième fois, 10/10 après le 15/15 de M12 — aucun fait
neuf). Les quatre survivants sont les quatre points extérieurs. La bande
s'arrête net entre 2.85/2.90 et 3.03/3.06.

**(b) Les neuf recherches ont TOUTES abouti, et le profil brut est
strictement croissant** — 8.2492 → 9.9708, aucun creux. Consigné, **pas
lu** : le plancher a échoué, le gel écrit « aucune lecture ». La pente de
ln s\*₄ chute de +2.03 à +0.12–0.23 sur le plateau des points morts puis
remonte — consigné également, sans lecture.

Parade de l'indice 40 exercée une fois de plus : 4|2.90|+1 est explosive
exactement À l'indice et son exclusion vient d'une explosion franche à
0.924 s\* (marge 0.51), pas de l'indice.

## 47.4 Le point dur, nommé (certification §6)

**À ce site, l'obstacle n'est pas la mesure de s\*₄ — c'est G6.** Une
géométrie qui veut m ≥ 7 doit soit s'écarter du site, soit accepter que le
diagnostic sous-seuil et la mesure de s\* ne cohabitent pas dans le rayon.
Rapprochement au registre, sans mise en regard chiffrée : 2.67 (M12), seul
point d'ordre 11, est mort par la fenêtre grossière ; les cinq d'ici
meurent par la fine, au site (1,1). Dans les deux cas, une résonance à
p = 4 a structuré **le dessous du seuil** sans qu'un creux de s\* soit
établi. Matière pour la note P1, à dériver avant toute lecture.

## 47.5 Faute machine 1, consignée : le selftest [9] ne testait rien

Le littéral `8.129205119847188` est **le même double** que la cible
(`…189`) — ulp 1.776e-15 > écart 1e-15. Mon test négatif de custody ne
pouvait pas échouer. Correction machine 2 (v1b) : `math.nextafter`, plus
une assertion qui vérifie que l'ancien littéral EST la cible — **le test
négatif embarque désormais son propre contre-exemple**. Motif adopté au
registre : *un test négatif doit embarquer la preuve qu'il peut échouer* —
même famille que les deux montages dégénérés du cycle M12, versant
flottant. Défaut de classe D1 (hors chaîne d'affirmation, attrapé à la
certification), aucun numéro E (E18).

Les trois autres éditions v1b : déclaration `classement_ex_aequo` (mon
extension bloc-d'ex-æquo, AJOUT à la règle gelée, direction non
conservatrice, inatteignable en pratique) ; `attrition_9` (dénominateur en
POINTS, unités corrigées) ; retrait d'une empreinte invérifiable d'un
commentaire.

## 47.6 Leçon de conception, consignée sans réécriture

Le site de la lecture §5 était **un nombre inventé** (0.06) là où le
catalogue gelé portait la quantité dérivée : le rayon R-2′ de la famille
(0.12 pour l'ordre 4). Écrit à d ≤ rayon, le motif aurait tiré (les cinq
pertes sont toutes à d ≤ 0.10 < 0.12, aucune dehors). Ceci ne relit PAS la
manche — la règle gelée a rendu « attrition simple » et ce verdict tient —
c'est une contrainte pour le prochain gel : **un site se dérive du
catalogue, il ne s'invente pas** (même famille que la règle 13).

## 47.7 La suite : gel M13b, deux options

- **(i) Deux objets, deux portes — recommandée.** Fenêtre élargie
  (~[2.70, 3.30]) : sept-huit points R-2′-propres HORS rayon portent le
  plancher et la corde de P-M13b-a (le test H-SAT, inchangé sur le fond) ;
  les points INTRA-rayon sont assumés comme **diagnostic sous-seuil
  pré-enregistré** (P-M13b-b : site = rayon du catalogue, motif de bloc
  contigu, mécanisme fine/grossière consigné par ligne) — la perte y est
  l'observable, plus un accident. Une manche, ~13–15 recherches.
- **(ii) L'objet bascule.** La structure sous-seuil au site devient la
  cible primaire ; H-SAT attend. Moins cher, mais laisse le trou de la
  note P1 ouvert.

Le gel M13b (option retenue par Baaz) est le prochain dépôt machine 1.

## 47.8 Ce que la manche n'établit pas

H-SAT (ni mesurée ni réfutée) ; rien sur l'étage A (non visé) ; rien sur
5:2 ni 8/3 ; le pas de s\*₄ (2.55–2.67) reste non localisé ; la lecture
mécanistique du §47.4 est une matière, pas un résultat.

## 47.9 Empreintes

JSON `70fe5611…` (brute ; canonique 89f609a5, CRLF) — vérifié machine 1 ·
cert. run `96cd155a` · réconciliation `.py` `2c46dce5` / `.log` `3742e4d1`
· contresignature machine 1 `.py` / `.log` : au message de livraison ·
script v1 `94dedaa0` (remplacé), v1b `1cb38518…` (exécuté) · gel v3
`26c5a445` inchangé · `m12_results.json` `fa109da9` intact et référencé.
