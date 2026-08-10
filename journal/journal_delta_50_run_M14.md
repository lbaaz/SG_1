# Delta 50 — run M14 (P1-a) : NÉGATIF RÉSOLU + CANYON-E. Le mécanisme est complet.

Date : 2026-08-02 (machine 1). Contresignature légère : 25 contrôles, TOUT
CONCORDE — E et B_E recalculés depuis la carte au bit, les sept verrous
re-dérivés de la carte, les deux portes ré-appliquées à la lettre.

## 50.1 Chaîne

Gel M14 v2 `273d0a53` certifié (cert. `1bb2936a`) → script v1 `725e477e`
→ **v1b `a43d046d…`** : deux éditions machine 2 consignées
(`meta.declarations.editions_machine2`, écart de répartition déclaré) →
selftest 8 sections exit 0 → pré-vol quatre scénarios, toutes branches →
run BOCAL4, **39 + 0 = 39 recherches, 36 + 0 = 36 balayages, 477.9 s** →
réconciliation machine 2, 7 sections TOUT CONCORDE. JSON
`m14_results.json` **`68df6576…`** — vérifié au bit par les deux machines.

## 50.2 Verdicts

> **P-M14a : NÉGATIF RÉSOLU** — les deux intra E-valides sont négatifs,
> résolus par **2 398×** (2.48) et **37 152×** (2.52) la barre de 10·B_E.
> Aucun point au-dessus de +10·B_E. **La prédiction inconditionnelle
> tient, et B(5:2) avec elle.**
> **P-M14b′ : CANYON-E** — minimum intérieur en 2.52, chute résolue des
> deux côtés (16 995× / 1 429×). m_E = 6, plancher OK, mort_intra false.

Profil mesuré : −0.147 (2.42) · −0.084 (2.46) · **−0.038 (2.48)** ·
*perdu* (2.50) · **−0.561 (2.52)** · −0.519 (2.54) · −0.483 (2.55).
Les six E mesurés sont négatifs.

## 50.3 L'attente P8 est falsifiée sur la FORME — consigné sans réécriture

Attendu : argmin 2.50, |E| ∈ [0.6, 1.5], creux ~symétrique. Mesuré :
**2.50 perdu** (la seule perte) ; **argmin 2.52** — la borne droite de la
fenêtre — avec |E| = 0.561, juste sous la bande ; profil **fortement
asymétrique** : à gauche |E| DÉCROÎT en approchant du site (0.147 → 0.084
→ 0.038 à 2.48, la plus petite valeur mesurée), à droite 0.48–0.56.
**Le signe est confirmé, la forme est autre chose — fait neuf sans
lecture gelée.** Réserve de la certification, adoptée telle quelle :
l'argmin tombe sur la borne de fenêtre et le centre naturel est mort —
cela ne touche pas P-M14a (deux intra suffisent à sa branche), cela borne
ce que P-M14b′ établit. Troisième attente falsifiée de la journée ;
chacune a payé.

## 50.4 La perte, et elle est chirurgicale : `5|2.50|−1`

Une ligne sur 36. **Mécanisme E27 — grossière mordue (explosion à
1.712943 = 0.7904 s\*, gros_explosifs = 5), fenêtre fine VIDE — troisième
occurrence de la campagne** (M12 : 7|2.67|+1 ; M13b : 2.70 ; ici),
**première à p = 5**, et **asymétrique en signe** : 5|2.50|+1 survit,
grossière vide. Les deux recherches de la ligne avaient abouti — la perte
est du balayage, pas de la mesure ; 2.50 perd son E par répercussion G7,
motif porté. Matière au registre, aucune lecture : la résonance structure
le dessous du seuil au degré de rang (3, 1), pendant que le rang (1, 1)
creuse le seuil de E — le motif transversal des deltas 47.4/48.3 gagne sa
troisième instance et son premier degré impair.
`ad8dd209` À SA PORTÉE : 8/8 grossières vides à p = 4 — **47/47 lignes
cumulées, quatre runs** *(la première passe de réconciliation machine 2
l'avait assertée sur 36 lignes, hors portée — auto-attrapée, consignée)*.
Taux intra à 5:2, première mesure — l'inconnue chiffrée du gel :
**1 ligne / 36 ; 1 point intra / 3** — la branche optimiste de la table.

## 50.5 Custody ×7 au bit, et le reste des gardes

G1′ + les six ancres (2.42 et 2.55 aux trois degrés) : **7/7 à 0.0
exact**, re-dérivés de la carte — deux points M12 re-mesurés à froid dans
un autre script : identiques. Le contrôle de non-dérive le plus dense de
la campagne. G8a 0.0 au bit — **parité, sixième géométrie**. G2 (p = 7,
2g) au bit : 0.9999994751. G4 re-désignée indépendamment : 4|2.42, écart
0.000e+00. Quatre re-liaisons G3 étiquetées (≤ 4.75e-16), la quatrième
(G4) déclarée-au-run comme prévu. Durées : 36 mesures, somme au bit.

## 50.6 Deux fautes, consignées avec leurs leçons

**(machine 1)** `porte_a` construisait son `detail` avec des **clés
flottantes** — le sérialiseur du pilote les refuse, et le premier
`sauve()` touchant ce bloc arrive APRÈS les 39 recherches : dix minutes
de mesure puis TypeError, aucun verdict. **Le défaut du pilote M11 v2 à
l'identique, répété par machine 1** ; seul le pré-vol pouvait le voir, et
le pré-vol machine 2 l'a vu. Leçon au registre : *les clés d'un dict
destiné au JSON naissent chaînes* — et les structures de consignation se
font traverser par le pré-vol AVANT le run, jamais seulement par le
selftest (selftest = ce que le script CALCULE ; pré-vol = ce qu'il FAIT —
la distinction maison, payée une fois de plus).
**(machine 2)** l'assertion ad8dd209 hors de sa portée en première passe
de réconciliation — auto-attrapée. Le dispositif mord dans les deux sens,
même jour, même manche.

## 50.7 Où en est la dérivation P1 — LA CHAÎNE EST COMPLÈTE

| étage | statut |
|---|---|
| A — sélection par parité | dérivé ; contrôlé (FFT, chemin indépendant) ; **hors échantillon 5/5** |
| B — hiérarchie | favorable à 2:1 (j gouverne) ; **et maintenant au site 5:2** |
| H-SAT | **mesurée** (M13-L, fermée au bit) |
| le signe au cœur de 5:2 | **NÉGATIF RÉSOLU** |

Confrontation M12 : 8 prédits + 3 expliqués, et les deux négatifs portent
désormais un test de cœur confirmé. Le mécanisme est **dérivé, contrôlé
par un chemin qui ne partage rien, vérifié hors échantillon, et mesuré à
ses deux sites**. Note P1 → **v5** (ce jour).

## 50.8 Ce que la manche n'établit pas, et la suite

Rien sur 8/3 ni la tension 2.67 (**P1-b**, double observable — prochaine
manche naturelle) ; le ratio |δ₅|/|δ₇| **non mesuré** (2.50 mort — les
cordes P-M14c n'étaient pas évaluables ; question de conception ouverte :
récupérer 2.50 exigerait les deux signes, le −1 est structurellement
perdu à cette géométrie) ; la FORME du creux (50.3) sans lecture ; rien
sur le criblé. Restent au programme : P1-b, P1-e, P2 (observable
quantique, règle C2), P4 (dérivation de C), P5. **Et le dossier** : le
mécanisme étant complet et doublement vérifié, la note compagnon P1 et la
phrase M12 du mail de couverture ont maintenant leur histoire entière —
cinquième signalement, la décision reste à Baaz.

## 50.9 Empreintes

JSON `68df6576…` (vérifié m1) · cert. run `16a66ba2` · run log `4b66d461`
· réconciliation `.py` `51ac7416` / `.log` `13a54148` · script v1
`725e477e` (remplacé), v1b `a43d046d…` (exécuté) · gel v2 `273d0a53`
(cert. `1bb2936a`) · contresignature m1 : au message · `fa109da9`,
`70fe5611`, `22fa1760`, `a38b8967` intacts et référencés.
