# Delta 48 — run M13b : NON CONCLUANT DE GÉOMÉTRIE ; le motif de M13 n'est pas reproduit

Date : 2026-08-02 (machine 1). Contresignature légère : 24 contrôles, TOUT
CONCORDE.

## 48.1 Chaîne

Gel M13b v1 `7a9b2809` certifié à vue → patch v1b → v1c appliqué et consigné
par machine 2 (spec `cefc3991` ; écart de répartition déclaré, précédent
v1b) → script v1c `536c897b…` → selftest → **pré-vol réduit, deux scénarios
— et il a payé contre son propre auteur** : le moteur factice du scénario
« attendu » servait les ancres au bit sur un fond qui ne passait pas par
elles (profil factice non monotone → NON CLASSÉ) ; corrigé avant run,
consigné (cert. §5) → run BOCAL4, 17 + 0 = 17 recherches, 14 + 0 = 14
balayages → réconciliation 8 sections TOUT CONCORDE. JSON
`m13b_results.json` **`22fa1760…`** — vérifié au bit par les deux machines.

## 48.2 Verdicts

**P-M13b-a : NON CONCLUANT DE GÉOMÉTRIE.** m = 9, **m_hors = 7 — le seuil
du plancher est atteint** ; c'est la clause des BORDS qui tranche : 2.70
est perdu (G6). Sous-branche **a-fort** : deux intra survivent, dont 3.02
à d = 0.02 du site. **P-M13b-b : MOTIF NON ATTEINT** — deux clauses
indépendantes cassent : `contigu = False` (3.02 survit entre 2.96 et
3.05) et une perte HORS rayon (2.70, d = 0.30). Conséquence A8, appliquée
telle quelle : **la note P1 garde son trou** — les trois signes du groupe
3:1 restent accommodés. H-SAT ni mesurée ni réfutée, pour la deuxième
fois, par deux chemins différents.

## 48.3 Le fait principal : le motif ne se reproduit pas — l'ensemble est ENTRELACÉ

M13 : cinq pertes intra **contiguës** [2.90, 3.03], zéro hors. M13b, sur
des points **neufs**, même site, même chaîne : trois pertes intra **non
contiguës**, une perte hors site. Mécanisme identique partout (fenêtre
fine, 0.924–0.966 s\* sur les trois runs, grossière vide **39/39** lignes
à p = 4 — ad8dd209 sans contre-exemple). Les ancres au bit (§48.4)
rendent la juxtaposition inter-runs légitime — même instrument, prouvé.
La carte cumulée sur la grille au centième :

> morts : 2.70 · 2.90 · 2.92 · 2.94 · 2.96 · 2.97 · 3.00 · 3.03 · 3.05
> vivants : 2.74 · 2.78 · 2.80 · 2.85 · 2.89 · **3.02** · 3.06 · 3.10 ·
> 3.15 · 3.22 · 3.26 · 3.30

**L'ensemble d'exclusion sous-seuil à p = 4 dans [2.70, 3.30] est
ENTRELACÉ au centième** — 3.02 vit au centre exact entre des morts ; 2.89
vit sous 2.90 mort ; 2.70 meurt à 0.30 du site. C'est le phénomène qui a
fait naître G6 (les îlots de M10 : « l'ensemble d'explosion n'y est pas
une demi-droite »), maintenant cartographié à p = 4 — le dessous du seuil
est criblé fin, et pas seulement près de la résonance. FAIT nommé,
matière ; aucune lecture mécanistique ici.

## 48.4 Trois acquis solides

**Custody ×3 au bit** : G1′ (2.80 vs `fa109da9`) 0.0 exact ; ancres 2.85
et 3.15 vs `70fe5611` **0.0 exact toutes deux** — même chaîne, script
différent, points re-mesurés à froid, identiques au bit. **Le profil brut
des treize recherches est strictement croissant** 7.9585 → 10.3594, y
compris 3.02 au centre du site — consigné, PAS lu (plancher échoué).
**Parité au bit, cinquième géométrie** (G8a 0.0 à 2.85, G8b zéro
déviation). G4 sur 3.30 (re-désignée indépendamment), écart 0.000e+00.

## 48.5 Deux attentes falsifiées, consignées sans réécriture

L'attente A7 de machine 1 casse sur trois clauses (hors 8/8 ✗, intra 5/5
✗, STRUCTURE ✗). L'hypothèse de contiguïté qui a dessiné la porte-b venait
d'un échantillon de cinq points — **le motif d'une structure se dérive de
sa physique supposée, pas de son premier échantillon** (leçon, même
famille que 47.6). La porte a rendu « motif non atteint » et publié :
l'appareil a fait exactement son travail contre son concepteur.

## 48.6 Le point dur, déplacé et nommé (cert. §6)

M13 : la bande morte engloutissait la fenêtre. M13b : la géométrie y
survit (m_hors = 7 atteint, résolution a-fort) — **c'est un bord qui
tombe, à 0.30 du site**. Fait gênant pour toute géométrie future : les
exclusions G6 à p = 4 dans cette région ne sont pas confinées au
voisinage de la résonance. **Un plancher qui exige la survie de bords
NOMMÉS est fragile tant qu'on ne sait pas où G6 mord.**

## 48.7 Trois options pour la suite (décision Baaz)

- **(β) Gel de lecture agrégée — recommandée, zéro recherche.** Règle
  mécanique à zéro degré de liberté, certifiée par les deux machines
  AVANT sa seule évaluation : union de TOUS les survivants p = 4 de
  `70fe5611` et `22fa1760` dans [2.70, 3.30] (aucun choix — tous),
  légitimée par les ancres au bit ; classifieur P-M13a inchangé sur
  l'union (11 points, 2.74 → 3.30, dont 3.02 au centre) ; plancher en
  COMPTES sur l'union (m ≥ 9, ≥ 3 par flanc, ≥ 1 intra) ; bords = les
  extrêmes SURVIVANTS. Résolution déclarée : les points morts sont des
  trous ; un creux logé exactement dans les trous n'est pas exclu — mais
  3.02 en ligne au centre borne ce qu'un tel creux pourrait être.
- **(α) M13c : plancher par comptes et zones, bords redondants.** La
  correction structurelle du 48.6 en une passe neuve (~10–14
  recherches) : plus aucun survivant nommé, des comptes par zone.
  Plus lent, plus conservateur, mêmes conclusions attendues.
- **(γ) S'arrêter là sur H-SAT** et consigner : « seuil non creusé sur 22
  mesures strictement croissantes, deux géométries ; dessous criblé fin »
  — sans verdict de porte. Le moins cher, le moins opposable.

## 48.8 Ce que la manche n'établit pas

H-SAT (2e plancher) ; la structure au sens de la porte (motif non
atteint — ni confirmée ni réfutée) ; toute lecture mécanistique du 48.3 ;
le pas de s\*₄ (2.55–2.67) toujours non localisé — noter : s\*(2.70) =
7.96 est déjà au-dessus du pas.

## 48.9 Empreintes

JSON `22fa1760…` (vérifié machine 1) · cert. run `c223d804` · run log
`9faceb0a` · réconciliation `.py` `5f1a15c8` / `.log` `ced54443` ·
pré-vols `d088e8b4` / `b2d6326b` · gel M13b v1 `7a9b2809` (certifié à
vue) · patch spec `cefc3991` · contresignature machine 1 : au message ·
`70fe5611`, `fa109da9` intacts et référencés.
