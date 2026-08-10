# GEL M13 v3 — BALAYAGE DE SATURATION : s\*(ω₂) à p = 4 À TRAVERS 3:1

**Machine 1, 02/08/2026 — v3, éditions de la certification v2**
(`m13_certification_croisee_v2.md` : fond certifié, deux corrections
éditoriales + deux notes). Changements v2 → v3, tous éditoriaux : **C-2**
le prime est retiré — un seul nom, P-M13a, partout ; **C-1** l'empreinte
du `.log` v1 passée en canonique NFC+LF ; **§7** « deux valeurs
distinctes » (le « trois » venait d'une synthèse machine 2, corrigée par
elle-même — cert. v2 §6) ; **N-5** règle d'égalité à l'argmin déclarée
(règle 15) ; **N-6** « toute issue, y compris NON CLASSÉ » au §5 ; la
mention « verbatim » corrigée — le critère est la forme **durcie**
(deux voisins, B_inst par paire), re-testée 5/5 sur son propre texte
(cert. v2 §2, marge minimale 406×). **Aucune dérivation, aucun compte,
aucune branche ne change.** Intouchés : §1, §2, §4, §5 (hors N-6),
recherches = 13, balayages = 10. Certification à vue attendue, puis feu
E19.

## 1. Objet et cible épistémique (exigence re-dérivation m2 §8.1)

Tester **H-SAT** — la saturation du canal 3:1 au degré 4 — et, à travers
elle, l'étage B au site 3:1. La règle de sélection nue (rang (1,1), le
couplage maximal) prédit ici le canyon le plus profond du jeu ; H-SAT
prédit son absence. **L'étage A n'est pas testé par cette manche.**
Un seul degré (p = 4), un seul signe (+1, P-M12e), aucune combinaison E.

## 2. Les deux branches, écrites d'avance

- **Branche LISSE** : profil sans creux au sens de P-M13a ⇒ H-SAT est
  **mesurée dans la chaîne** ; le groupe 3:1 de M12 est expliqué ; second
  test favorable de l'étage B. La lecture du §3 de la note P1 v2 passe de
  « 8 prédits + 3 accommodés » à « 8 prédits + 3 expliqués par un
  mécanisme mesuré ».
- **Branche CANYON** : creux au sens de P-M13a ⇒ **H-SAT est morte** ; la
  lecture du groupe 3:1 s'effondre et avec elle 3 des 11 signes de la
  confrontation ; l'étage A reste intact ; le mécanisme du signe est à
  reconstruire au site 3:1.

## 3. Attente gelée du rédacteur (machine 1, avant tout calcul)

**Branche LISSE.** Profil strictement croissant sur toute la fenêtre ;
|écart de ln s\* à la corde des deux bords, évalué en 3.00| < 0.05 ;
aucune ligne exclue par G6 ; les fenêtres grossières vides sur les 9
lignes (p pair, précédent ad8dd209/M12 : 15/15 vides).

**Provenance déclarée (règle de provenance, m2-§8.6)** : cette attente
n'est **pas** indépendante — les trois points p = 4 de M12 (2.72, 2.78,
2.80) sont déjà strictement croissants et sans approche de canyon ; c'est
la donnée qui a motivé la manche. L'attente est une extrapolation de
l'entraînement, la manche en est le test.

## 4. Géométrie

- **Fenêtre** : ω₂ ∈ [2.85, 3.15] — hors du domaine gelé de M12
  ([1.73, 2.82]) : M13 déclare **son propre domaine**. Une seule famille
  d'ordre ≤ 12 vit dans la fenêtre : 3/1 (q = 4, rayon 0.12) — la fenêtre
  isole le site.
- **Neuf points** : 2.85, 2.90, 2.94, 2.97, 3.00, 3.03, 3.06, 3.10, 3.15.
  Les points de [2.88, 3.12] sont **dans le rayon de 3:1 — échantillonnage
  délibéré, déclaré** (précédent : gel M12 v4, ligne 420). 2.85 et 3.15
  sont R-2′-propres et servent de bords de corde.
- **Signe** : +1 seul au programme (P-M12e — r_s = 1 par démonstration,
  reproduite au bit par le pilote et le run M12). Une ligne de régression
  G8 au point 3.00 (les deux signes) re-vérifie la parité dans la fenêtre
  neuve.
- **Recherche** : géométrie de recherche M12 héritée (bissection, pas
  final ≤ plafond G5, fenêtres fine [0.90 s\*, 1.05 s\*] et grossière
  [LO0, 0.90 s\*], résolutions consignées par ligne — correctif E27,
  parade d'indice 40 par ligne). **Borne haute initiale HI0 = 20**,
  déclarée (s\* attendu croissant au-delà de 8 dans la fenêtre ; la borne
  n'est pas un seuil de garde, seulement un cadre de bissection — si un
  s\* la dépasse, la ligne est consignée BORNE_ATTEINTE et non recevable,
  jamais silencieusement tronquée).

## 5. LA PERTE EST UNE DONNÉE (exigence m2 §8.2)

Le mécanisme d'exclusion G6 (explosion sous 0.98 s\*) est **corrélé au
signal cherché** : si un canyon existe, les lignes proches de 3.00 sont
les plus susceptibles de mourir. Pré-déclaration :

- Toute explosion sous seuil est consignée avec sa position, sa fenêtre
  (fine/grossière) et sa marge — comme dans l'artefact M12.
- **Branche de lecture des pertes, écrite d'avance** : si ≥ 2 exclusions
  G6 tombent sur des points à d ≤ 0.06 de 3.00 et aucune à d > 0.06,
  la manche est lue « STRUCTURE SOUS-SEUIL AU SITE 3:1 » — un résultat,
  consigné séparément de P-M13a, compatible avec **toute issue**
  de P-M13a sur les survivants, y compris NON CLASSÉ. Ni preuve de canyon, ni attrition simple.
- Pertes éparses (sans le motif ci-dessus) : attrition simple, consignée.
- **Plancher** : P-M13a exige m ≥ 7 survivants ET les deux bords de corde
  (2.85, 3.15) survivants. Sinon : NON CONCLUANT DE GÉOMÉTRIE, aucune
  lecture, et la manche suivante redessine la fenêtre.

## 6. Portes

- **P-M13a — le creux, critère ORDINAL** (correctif machine 2, **durci**
  par machine 1 — deux voisins, B_inst par paire — et re-testé 5/5 sur le
  texte durci, certification v2 §2 ; marge minimale 406 × le seuil
  instrumental majoré). Sur les survivants, en ln s\* :
  **CANYON** ssi le profil possède un minimum **intérieur** avec
  argmin ∈ [2.94, 3.06], **et** la chute est résolue par l'instrument des
  **deux** côtés : ln s\*(argmin) ≤ ln s\*(voisin) − 10·B_inst pour chacun
  des deux voisins survivants, avec **B_inst = (pas/s\*)(argmin) +
  (pas/s\*)(voisin)** — somme linéaire des incertitudes des deux lignes
  comparées (forme dérivée, règle 13 ; ordre de grandeur 1e-6 contre des
  structures attendues de 0.1 à 2.7 : cinq à sept ordres de marge, et le
  seuil ne dépend d'aucune quantité que la mesure puisse gonfler).
  **LISSE** ssi le profil est **strictement monotone** sur les survivants.
  **Tout autre motif : NON CLASSÉ** — motif intégral publié (profil,
  argmin, marges), aucune lecture.
  **PAS contre CREUX, par construction** : une marche monotone est classée
  LISSE et consignée ; seule une descente-remontée résolue est un CREUX.
  **Égalité à l'argmin (N-5, règle 15)** : deux points intérieurs sont ex
  æquo si |Δln s\*| ≤ B_inst de leur paire (tolérance déclarée, entrées
  flottantes) ; le verdict CANYON exige que **tous** les ex æquo du
  minimum soient dans [2.94, 3.06] — sinon NON CLASSÉ, motif publié.
  Aucun seuil de lissité n'existe — le défaut de la v1 (B_lisse calculé
  sur des flancs qui sont dans le canyon, seuil anti-corrélé à l'effet,
  2/5 au test négatif) est retiré avec le seuil lui-même.
- **Fait antérieur, consigné (certification v1, §9)** : dans l'artefact
  M12 (`fa109da9`), entre ω₂ = 2.55 et 2.67, **s\*₄ passe de 2.8812 à
  7.4626 — un facteur 2.59** — seul des trois degrés, sans aucune famille
  de rang (1, 1) au catalogue pour p = 4 dans [1.73, 2.82] ; et le « saut
  de E » de la note P1 en est à 101 % le canal 4 (décomposition
  +1.0155 − 0.2829 + 0.2681 = +1.0007). Conséquence de conception : **le
  fond de s\*₄ n'est pas présumé lisse** sur une largeur de 0.30 ; un pas
  dans la fenêtre M13 romprait une corde sans être un creux — c'est
  précisément ce que le critère ordinal absorbe. Ni preuve, ni oubli.
- **P-M13b — consignation, hors porte.** Le profil complet (9 valeurs ou
  moins), les fenêtres G6 par ligne, la structure sous-seuil éventuelle.
  Matière pour la manche P1, pour A(ω₂), et pour la localisation
  éventuelle du pas de s\*₄.

## 7. Gardes et comptes

- **G1′ (custody)** : rejouer 4|2.80|+1 du run M12 ; **cible nommée au
  champ** : `resultats.carte['4|2.800000000000'].sF` de `m12_results.json`
  (`fa109da9`) **= 8.129205119847189**, écart absolu exigé 0.0 (bit). La
  ligne porte **deux** valeurs distinctes dans l'artefact (carte.sF =
  sP.s = G4.s_dt d'une part ; G4.s_dt2 = 8.130084754569644 de l'autre —
  compte corrigé, cert. v2 §6) ; le champ lève l'ambiguïté (bloquant B-3).
- **G3** : erreur backward ≤ 1e-12 à chaque re-liaison (une seule attendue,
  P = 4 ; consignée avec étiquette — recommandation r4 appliquée).
- **G4** : dt/2 sur la ligne d'échelle de force maximale g·s\*³,
  **déterminée au run** sur les s\* mesurés ; « 3.15 » est une **attente**,
  pas une désignation. Écart en forme ratio |s_dt2/s_dt − 1|, convention
  identifiée sur le primaire M12.
- **G5** : pas final ≤ 1e-5, consigné par ligne.
- **G6** : primauté de s\*, fenêtres et parade d'indice 40 héritées M12.
- **G7** : sans objet (un seul degré) — déclaré, pas omis.
- **G8** : au point 3.00, les deux signes — G8a écart au bit, G8b
  structure ; moitiés grossières attendues vides (p pair).
- **G2** : une recherche neuve à 2g au point 3.00, |K2/K1 − 1| consigné.
- **G9** : constructeurs de consignations complets avant run.
- **Selftest à contre-exemples (obligatoire, bloquant)** : le `--selftest`
  du script **rejoue les cinq profils d'archive** (p = 3, 5, 7 à 2:1 :
  CANYON attendu ; p = 4, 6 : LISSE attendu) à travers le classifieur
  P-M13a et **exige 5/5**, en échec bloquant. Ces profils sont des
  **vecteurs de test du code**, pas des données d'argument : aucun chiffre
  M5/M6 n'entre dans un résultat M13 — déclaré ici. Premier contrôle de la
  campagne à embarquer cinq contre-exemples à réponse connue (esprit
  S_TEMOIN_DIVERGENT du pilote).
- **Comptes dérivés** : recherches attendues = 9 (programme) + 1 (G8, −1)
  + 1 (G1′) + 1 (G4) + 1 (G2) = **13** ; **balayages attendus = 10**
  (9 programme, dont 3.00|+1, + 1 ligne G8 −1 — la ligne 3.00|+1 de G8
  **est** le 5ᵉ point du programme, bloquant B-4 corrigé). Forme
  « comptés + sautés == attendus ».
- **Moteur** : `m9_replication_v1.py` (`c8ed357b`), inchangé. Script :
  gabarit m12_ponctuel, réduit à un degré ; pré-vol à moteur factice
  obligatoire, branches de perte parcourues, **joué par machine 2**
  (détentrice des sources — seule forme opposable).

## 8. Ce que cette manche n'établit pas

Rien sur l'étage A (non visé) ; rien sur les magnitudes de E ; rien sur
8/3 ni 5:2 ; rien hors de [2.85, 3.15] ; et la branche LISSE ne dérive pas
le **mécanisme** de la saturation — elle la mesure. Un NON CLASSÉ ou un
NON CONCLUANT DE GÉOMÉTRIE n'est pas une réfutation de H-SAT.

## 9. Chaîne

Parent : gel M12 v4 `bf9866a7` (cert. `f10ffcf3`) — géométrie de recherche,
fenêtres, parade d'indice 40, convention d'empreinte B. Note source :
`note_derivation_P1_signes_E_v3.md`. Re-dérivation machine 2 :
`p1_re_derivation_machine2_v1.md` (`97c02eab`). Certification croisée v1
(NON CERTIFIÉ, quatre bloquants, correctif P-M13a testé 5/5) :
`m13_certification_croisee_v1.md` (`9ad5689b`), `.py` (`9e780287`),
`.log` (canonique NFC+LF `d8e60b61` ; brute `d788e3c4`, octet 0xa7 Latin-1, décodage utf-8/replace). Artefact custody : `m12_results.json` (`fa109da9`).
L'empreinte de ce gel : au message de livraison ; celle de la version
certifiée fera foi.

---

*Fin du gel M13 v3. Machine 2 : six éditions éditoriales de la cert. v2,
zéro changement de fond — certification à vue, puis feu vert E19.*
