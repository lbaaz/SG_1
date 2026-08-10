# Delta 46 — run M12 ponctuel : CLASSE RÉFUTÉE, VIOLATION DISPERSÉE (v2)

Date de rédaction : 2026-08-02 (machine 1). **v2 remplace v1** (86bfdca1, non
certifiée). Motif : réception par machine 1 de l'artefact primaire
`m12_results.json` et du log de run — la vérification passe des littéraux
consignés à la re-dérivation primaire complète. Changements v1 → v2 : §46.1
(custody fermée), §46.5 (motif confirmé sur primaire), §46.6 (piège vérifié
machine 1, parade par ligne, double témoin), §46.7 (D1-2 tranché), §46.8
(étiquettes corrigées, r5), §46.9 (périmètre étendu, conventions identifiées),
§46.10 (r3 résolu, r5 nouveau), §46.12 (empreintes), §46.13 (P-M12e, E27,
règle 15).

## 46.1 Chaîne d'exécution et custody

Gel v4 `bf9866a7` (cert. `f10ffcf3`) → script `m12_ponctuel_v2.py` `c5659f52`
(cert. `5faef5ec`, S1–S3 de la v1 traités) → pré-vol machine 2 (01:23, rejoué
avec branches de perte — CONSTITUANT de la certification, r2) → run BOCAL4
01/08, 23:52 UTC. Le script a re-vérifié à l'exécution : gel jumeau v4
CONCORDANT, pilote `663b17e2` CONCORDANT **avec re-vérification de son propre
gel `03e29c86`** (custody transitive EXERCÉE au run, pas seulement conçue),
moteur `c8ed357b` CONCORDANT, G9 constructeurs complets, règle 11 à 1e-9.

**La boucle de custody est fermée.** Machine 1 a reçu et vérifié l'artefact
primaire : `m12_results.json`, 130 856 octets, sha256 brute
`fa109da92e582520cfcb63b46bc41fa7d4b62295891f413bb97c6095b2fe59b1` — au bit
l'empreinte annoncée par le message de run, par le log de run et par la
certification. Les deux machines détiennent désormais le JSON M12 vérifié,
même statut que `m9_replication_v1.py` et `m11_exposant_v3.py`. Le log de run
est également détenu et empreinte (r3 résolu, §46.10).

Comptes dérivés, consignés dans l'artefact : recherches 75 + 0 = 75/75,
balayages 67 + 0 = 67/67.

## 46.2 Verdicts

- **P-M12a : CLASSE RÉFUTÉE.** m = 11 (13 − 2 pertes G6→G7) ≥ plancher 8 ;
  11/11 points à |E| ≥ 0.10 (seuil : ceil(m/2) = 6 ; marge 5). Branche TENUE
  (|E| ≤ 0.03) : zéro point.
- **P-M12b : VIOLATION DISPERSÉE.** Signes parmi les |E| ≥ 0.10 : {+1, −1}
  (9 positifs, 2 négatifs : 2.42 = −0.147267, 2.55 = −0.483335). Pas de
  SYSTÉMATIQUE.

Première manche conclusive depuis M6. La forme brute ln s*_p = A·u_p + B
ponctuelle est morte en tant que loi de classe.

## 46.3 La mesure

| w2 | E | | w2 | E |
|---|---|---|---|---|
| 1.73 | +0.764146 | | 2.42 | −0.147267 |
| 1.76 | +0.808568 | | 2.55 | −0.483335 |
| 1.84 | +0.964440 | | 2.67 | PERDU |
| 1.86 | +1.015680 | | 2.72 | +0.517399 |
| 2.22 | +0.405583 | | 2.78 | +0.519337 |
| 2.27 | +0.171548 | | 2.80 | +0.542579 |
| 2.38 | PERDU | | | |

E re-dérivé par machine 1 depuis la carte primaire (ln sF4 − 2.25 ln sF5 +
1.25 ln sF7) : écart maximal aux valeurs consignées **0.0** sur les 11
survivants. σ_E : 7.4e-07 à 2.6e-06 (quadrature) ; σ_E_max (somme linéaire,
pire cas) : 3.892e-06 au pire point (1.73). Marges au seuil 0.10 : minimum
0.047267 (à 2.42), soit ≈ 2.9e4 σ_E_max — aucun point au bord. Ancrages : le
seuil 0.03 vaut 7 709 σ, le seuil 0.10 vaut 25 696 σ (sur la mesure).

## 46.4 L'attente gelée, clause par clause

L'attente de Baaz (gelée v1, copiée 4×, byte-prouvée) : RÉFUTATION ✓ ;
P-M12b SYSTÉMATIQUE même signe ✗ (DISPERSÉE) ; |E| entre 0.15 et 0.45 :
1 point sous 0.15 (2.42), 2 dans la bande (2.27, 2.22), **9 au-dessus de
0.40 dont 8 au-dessus de 0.45** (r1) — l'amplitude réalisée déborde la bande
attendue par le haut, jusqu'à |E| = 1.016 (1.86).

## 46.5 Deux pertes, deux mécanismes, un seul motif consigné

- 7|2.38|+1 : explosion **fine** à 1.2241 < 0.98 s* (marge 5.0e-3) ;
  grossière propre (gros_explosifs = 0).
- 7|2.67|+1 : explosion **grossière** à 1.5489 < 0.90 s* (marge 1.1e-1) ;
  fine propre sous 0.98 s* ; gros_explosifs = 1, seule ligne sur 67. Le
  mécanisme d'E27 (la géométrie grossière voit ce que M10 ne consignait pas),
  hors degré pair.

`meta.exclusions` porte un motif **identique** pour les deux : « G6 sgn=+1
explosion sous seuil » (D1-1, confirmé sur primaire). `resume.points_perdus`
porte les CELLULES fautives (`7|2.38`, `7|2.67`) — le degré fautif est dans
la clé, le w2 est le point. Ventilation par mécanisme : {G6:2, G2:0, G4:0,
G5:0}, avec la note d'artefact « ventilation par MÉCANISME, pas une
partition ».

## 46.6 Trois contrôles exercés sur donnée réelle

1. **Le piège de l'indice 40 — OUVERT → EXERCÉ, vérifié machine 1 sur
   primaire.** 5|2.67|+1 est explosive exactement À l'indice 40 (0.98 s*) et
   n'est PAS exclue : s < 0.98 s* ⟺ i < 40 strict. Seule ligne sur 67. La
   parade est consignée **par ligne** : champ
   `indice_40_compte_comme_sous_seuil == False`, 67/67. Chaque ligne porte
   en outre un **double témoin** du bord : écart absolu (exact sur 41/67,
   |max| 8.9e-16) et écart relatif SIGNÉ (exact sur 29/67, 34 à +1 ulp, 3 à
   −1 ulp, 1 à +2 ulp) — douze lignes ont abs == 0 avec rel ≠ 0 : deux
   expressions indépendantes du même bord, chacune avec son arrondi. Le
   verdict passe par l'INDICE, donc insensible aux deux (matière règle 15).
2. **G8a/G8b au rang 1 et au rang 13.** G8a : écart 0.0 exact aux deux
   rangs. G8b fine : transition encadrée, 24/52 (1.86) et 26/50 (2.22),
   zéro déviation entre signes — pouvoir RÉEL (note N-1). G8b grossière :
   vide des deux signes (n = 177/178) — pouvoir NUL au sens de N-1, et
   c'était PRÉ-DÉCLARÉ (moitié grossière attendue vide à p=4, note
   ad8dd209) : vérifié sur les 15 lignes p=4, aucune ne mord, aucun fait
   neuf. Croisement G6 : fin_explosifs concordent ligne à ligne.
3. **Parité au bit à degré pair.** sP − sM == 0.0 exact aux deux rangs G8 —
   la démonstration M11 tient sur ce run aussi ; P-M12e en découle (§46.13).

## 46.7 Deux chiffres requalifiés à la contresignature

- **458.** « Le seuil 0.03 = 458 σ » (gel) utilise le σ du PLAN (pire point
  du pilote). Sur la mesure : 458 est une borne inférieure large ; réalisé
  7 709 (§46.3). Le chiffre du gel reste vrai comme minorant.
- **D1-2, tranché sur primaire.** `duree_par_recherche_s.total` == somme AU
  BIT des 67 durées de la carte (852.9413326002541 s) ; n = 67 est porté
  par le champ ; moyenne == total/67 exacte. G1' + G2 (×6) + G4 = 133.41 s
  NON compris. La requalification se réduit au NOM du champ (« par
  recherche » pour des balayages) — la sémantique est dans le champ
  lui-même.

## 46.8 Matière P-M12d (post-hoc, étiquetée, hors verdict)

Familles des 11 survivants (assignation consignée à l'artefact) : ordre 3
×5 (1.76, 1.84, 1.86, 2.22, 2.27), ordre 5 ×1 (1.73), ordre 7 ×2 (2.42,
2.55), ordre 4 ×3 (2.72, 2.78, 2.80) — trois groupes de rayon (0.12 / 0.03
/ 0.12). Les deux perdus : 2.38 (ordre 3) et 2.67 (**ordre 11**, 8/3, rayon
0.001875) — consigné, sans mise en regard.

Structure du champ E : zéro encadré par des points MESURÉS (2.27 → 2.42) ;
saut +1.0007343 entre 2.55 et 2.72 ; les deux négatifs sont les deux points
d'ordre 7. Spearman (post-hoc) : ρ(|E|, d/r) = −0.6393, ρ(|E|, w2) =
−0.4364, ρ(E, w2) = −0.4909 — re-dérivés par machine 1 depuis le primaire,
rangs pris sur les rapports EXACTS.

Lecture par branches du gel : (iv) — aucune des lectures (i)-(iii) ne
s'applique proprement. Contre-exemples, étiquettes corrigées (r5) :

- **Contre-paire intra-famille ordre 3** : 2.22 (d/r = 11/6, |E| = 0.4056)
  contre 1.76 (d/r = 2, |E| = 0.8086) — |E| CROÎT quand d/r croît,
  contredit (i) à l'intérieur d'une même famille.
- **Ex æquo EXACT inter-familles** : d/r = 11/6 pour 2.22 (ordre 3) ET
  2.78 (ordre 4) ; |E| = 0.4056 contre 0.5193 — d/r seul ne détermine pas
  |E|.
- En appoint : 1.73 (**ordre 5**, même rayon 0.12, d/r = 23/12) contre
  2.22 — même sens croissant, inter-familles à rayon égal.
- Second ex æquo exact : d/r = 5/3 pour 2.55 (ordre 7) et 2.80 (ordre 4).

Les ex æquo sont détectés en Fraction (d et rayon exacts) et tiennent AUSSI
au bit en flottant dans l'artefact — vérifié, non supposé. Contrefactuel
consigné : la division flottante d/rayon aurait dévié de 1 ulp sur 7/13
points, mais l'ex æquo 5/3 aurait tenu (0.05/0.03 == 0.2/0.12 en IEEE).

## 46.9 Périmètre de vérification machine 1

**Contresignature v1** (littéraux des deux documents machine 2) : 51
contrôles, TOUT CONCORDE. **Vérification primaire v1** (implémentation
indépendante sur `m12_results.json`) : **100 contrôles, TOUT CONCORDE**,
couvrant : empreinte du fichier ; custody méta (gel, pilote, script, cible
G1', transitive) ; comptes dérivés ; census structurel (13 E / 39 cellules /
67 lignes {4:15, 5:26, 7:26} / 2 G8 / 6 G2) ; scan intégral des nulls avec
clé sœur `_motif` ; règle 11 par valeur ; sF et convention (f) sur 39
cellules ; P-M12e ; parité au bit ; chemin brut → m (recevabilité, G5
dérivé, exclusions, répercussion G7) ; census des pas {6.03e-07 ; 1.82e-06
sur les 4 cellules p=4 du bord droit} et cohérence pas carte == pas G6
67/67 ; E au bit ; portes et marges ; σ_E quadrature et σ_E_max linéaire
re-dérivés (écart max 4.2e-22) ; fenêtres (contiguïté 67/67, ratio 7/6,
grille fine, résolutions par ligne — correctif E27 implémenté) ; les deux
mécanismes d'exclusion avec marges ; piège indice 40 ; G8a/G8b et
croisements ; G1' au bit ; G4 ; G2 ; durées au bit ; résonances (d exact en
Fraction 13/13) ; ex æquo exacts ; les trois Spearman ; saut, zéro,
contre-paires.

**Hors périmètre, déclaré** : le CATALOGUE de résonances et la règle
d'assignation vivent au gel `bf9866a7`, que machine 1 ne détient pas en
fichier — la cohérence interne des blocs (d == |w2 − fraction| exact,
d_sur_r == rapport exact) est vérifiée 13/13, l'assignation est prise comme
consignée et certifiée machine 2.

**Trois conventions identifiées depuis le primaire** (mes trois attentes de
montage étaient fausses, l'artefact était juste) :

- **G4 consigne |s_dt2/s_dt − 1|** — la forme RATIO, même famille que G2,
  pas soustraction-puis-division. Vérifié au bit.
- **d et d_sur_r == float(valeur EXACTE en Fraction)**, 13/13 — jamais
  l'arithmétique flottante naïve. La matière P-M12d est en exact jusque
  dans l'artefact.
- **Le témoin d'indice 40 est double et mesuré**, pas supposé exact
  (§46.6.1).

## 46.10 Notes de relecture machine 1 (voie : certification v2 ou erratum, au choix de machine 2)

- **r1** — cert. §2 : « 8 au-dessus de 0.40 » ; le compte est 9 à 0.40, 8 à
  0.45. Census mécanique §46.4.
- **r2** — le pré-vol de 01:23 est un CONSTITUANT de la certification de
  01:25 (le message le rejoue avec les branches de perte) ; à dire
  explicitement dans la cert. v2 si elle existe.
- **r3 — RÉSOLU.** Le log de run est détenu et empreinte par machine 1 :
  brute `a5fddbc6c739403dd93b04df10e98f031801497b540ae1f5528d03db14ac98d3`,
  canonique (NFC+LF) `69d1d01d0615e88e437760925272d26b975521ca225d87bfb0e664da58a6b864`
  (CRLF Windows ; le chemin « out\m12_results.json » date la provenance).
- **r4** — les deux entrées G3 p=4 ne sont étiquetées ni dans le log de
  réconciliation ni dans `meta.G3_par_degre`. Le log de run les NOMME par
  l'ordre : G1' (rejeu 7|1.70, re-liaison P=7), degré 5, degré 4, G4
  (re-liaison P=4) — et montre que le degré 7 n'a PAS de re-liaison propre
  (G1' laisse le moteur à P=7). Recommandation maintenue : étiqueter les
  entrées à la source.
- **r5 — NOUVEAU, faute machine 1, trouvée par machine 1 contre le
  primaire.** Le delta 46 v1 (§46.8) et la contresignature v1 étiquetaient
  la paire (2.22, 1.73) « contre-paire intra-famille ordre 3 ». L'artefact
  primaire porte 1.73 = ordre 5 (3/2, d = 0.23). La contre-paire
  strictement intra-famille est (2.22, 1.76) ; elle suffit, et la
  conclusion (iv) est inchangée. Étiquettes corrigées en §46.8. La leçon
  est celle du registre : re-dériver au lieu de vérifier ce qu'un artefact
  MONTRE — les littéraux de la cert. étaient justes, mon étiquette par
  dessus ne l'était pas.

Statuts D1 : **D1-1** confirmé sur primaire (motif identique) ; **D1-2**
tranché (§46.7) ; **D1-3** vérifié (la carte ne porte aucun marqueur
d'exclusion ; `exclue` vit en G6 et l'équivalence exclue ⟺ explosion
consignée tient 67/67) ; **D1-4** confirmé (`meta.gardes == []`, champ
mort).

## 46.11 Ce que le run n'établit pas

La mort de la classe ne mesure pas β (M10 reste NON CONCLUANT) ; elle ne
teste pas les mécanismes candidats de β (le second reste « apparemment
vivant degré par degré », qualificatif obligatoire) ; elle ne dit rien du
criblage à degré pair (E27) ; la lecture P-M12d reste post-hoc, hors
verdict ; l'assignation des résonances n'a pas été re-dérivée par machine 1
(§46.9). Un non concluant n'est pas une réfutation — et inversement, cette
réfutation-ci ne rétroagit pas sur les manches non conclusives.

## 46.12 Empreintes (sha256, brute / canonique NFC+LF)

| Objet | brute | canonique |
|---|---|---|
| gel M12 v4 | bf9866a7… | (= brute) |
| cert. gel v4 | f10ffcf3… | — |
| script m12_ponctuel_v2.py | c5659f52… | — |
| cert. script v2 | 5faef5ec… | — |
| **m12_results.json (vérifié machine 1)** | **fa109da9…2fe59b1** | 389b270b… (CRLF) |
| **log de run (r3)** | **a5fddbc6…** | 69d1d01d… |
| message de run | 05147405… | — |
| cert. du run (machine 2) | 6e608e03… | (= brute) |
| réconciliation .py / .log | 0970b9b9… | f5a3a158… / 370bec8d… |
| contresignature machine 1 .py / .log | 22f4fd53… | 4a1b34e0… |
| **vérification primaire machine 1 .py** | **e03741c5a0d8af040de399b584ea6e7b589db204d3f93c24f9efbc4726fe3e98** | (= brute) |
| **vérification primaire machine 1 .log** | **ce4b5a61694a523116142905f8f3ac5f2b161f7de8c0168eb330205f15537b77** | (= brute) |
| delta 46 v1 (remplacé) | 86bfdca1… | (= brute) |
| delta 46 v2 (ce fichier) | au message de livraison | — |

## 46.13 Conséquences et registre

- L'arc L1 est clos par réfutation : la classe ponctuelle est morte sur
  onze points, dispersée, à grande marge. L1-h était sans objet (M11) ;
  β reste un paramètre ajusté par degré, pas une loi.
- **P-M12e entre au registre** : « r_s = 1 par démonstration (M11,
  reproduite au bit par le pilote) ; un seul signe au programme » — la
  consignation nommée qui lève la convention (f) à degré pair, portée par
  l'artefact lui-même (clés sœurs des sM null à p=4).
- **Le correctif structurel d'E27 est implémenté dans l'artefact** :
  chaque ligne G6 porte ses résolutions (pas relatifs et effectifs, fine
  et grossière) à côté de la consignation.
- **Matière règle 15 (comparaisons de bord), trois instances neuves sur
  primaire** : d/d_sur_r en float(Fraction) avec contrefactuel division
  (7/13 à 1 ulp, ex æquo 5/3 tenu) ; double témoin d'indice 40 (≤ 2 ulp,
  verdict par l'indice) ; ex æquo Spearman détectés en exact et vérifiés
  au bit. À verser au dossier de promotion.
- Le dossier Held gagne une fin racontable : une classe posée, gelée,
  exécutée, réfutée proprement — avec la boucle de custody fermée sur
  l'artefact primaire par les deux machines.
- Ouverts inchangés : certification du delta 46 v2 par machine 2 ; voie
  r1–r5 (cert. v2 ou erratum — E28 reste le dernier du registre, aucun
  numéro réservé, règle E18) ; mise à jour de CAMPAGNE_etat_complet
  (double état 13157ae8 vs 46d25637) ; bilan des fautes M8–M11 ;
  arbitrage S42.3/S43 ; cahier des charges de l'observable quantique (C2).
