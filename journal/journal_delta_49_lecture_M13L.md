# Delta 49 — M13-L : LISSE, fermé au bit par double implémentation. H-SAT EST MESURÉE.

Date : 2026-08-02 (machine 1).

## 49.1 Chaîne

Gel M13-L v1 `f779bbe3` **CERTIFIÉ** (machine 2, `m13L_certification_croisee_v1`,
0 bloquant, 3 notes R-1/R-2/R-3) → évaluation machine 2
(`m13L_lecture_machine2_v1.py`, JSON annoncé `a38b8967…`, date omise) →
**implémentation indépendante machine 1** (ce jour : logique propre —
classifieur importé de `94dedaa0`, extraction machine 1 ; textes consignés
et sérialisation alignés sur la sortie machine 2 publiée, déclaré) →
**comparaison de clôture : IDENTIQUES AU BIT** en forme canonique
(`641dbe3e31b51897e2ca2861a6c605cb…` des deux côtés).

## 49.2 Verdict

> **P-M13L : LISSE** — les onze points de E strictement monotones,
> 8.0041 → 10.3594, à travers ω₂ = 3.00, au degré où la règle de sélection
> place le couplage maximal (rang (1,1)).
> **H-SAT — la saturation du canal 3:1 au degré 4 — EST MESURÉE**, à la
> résolution dérivée de L6.

Statuts, per note R-3 (adoptée) : **le verdict LISSE est opposable au même
titre qu'un verdict de manche** — juge antérieur aux runs, appartenance
mécanique, plancher en comptes qui ne peut que refuser. **La borne
D ≲ 0.08 en ln est une estimation post-hoc étayée**, pas un résultat
gelé : ses chiffres (rugosité 0.05, forme 64 %) sont choisis en
connaissance de E. Le JSON porte cette distinction
(`verdict.resolution_L6_statut`).

## 49.3 La certification machine 2 est allée plus loin que le gel

Sa re-dérivation indépendante de L6 : calibration 39–46 % exacte (flanc
gauche), demi-largeurs équivalentes ≈ 0.043 (la classe ≥ 0.03 du gel est
conservatrice), plancher 64 % tenu par trois formes unimodales, facteurs
d'exclusion 35× / 10× / 6× — et **une mesure que le gel ne faisait pas :
le résidu de 3.02 contre la corde de ses voisins vaut +0.0188 en ln —
POSITIF.** Aucune dépression au point le plus proche du site ; le gel
sous-vendait son propre résultat. Les trois notes, toutes intégrées à la
note P1 v4 : **R-1** la calibration est le flanc GAUCHE des canyons 2:1
(le droit donne 18–60 % ; l'asymétrie est elle-même un fait de M5) ;
**R-2** le plancher 0.05 est un majorant argumenté, pris HORS E (la
marche 2.89→2.92), sens défavorable à la conclusion ; **R-3** ci-dessus.

## 49.4 G-L2 : le quatrième verrou, inter-manches

2.78 est bit-identique entre `fa109da9` (M12) et `22fa1760` (M13b) —
`8.03774683329979` — deux manches, deux scripts, quatre jours d'écart.
Avec G1′ et les ancres 2.85/3.15 : la chaîne se reproduit au bit partout
où on la re-mesure.

## 49.5 Comptabilité de la clôture au bit (trois écarts, trois causes, zéro mystère)

1. **CRLF (machine 2)** : `a38b8967` est le contenu en fins de ligne
   Windows — vérifié par calcul (leur-rejoué→CRLF le reproduit
   exactement). Le gel L8 disait « date omise » mais ne fixait pas la fin
   de ligne : lacune de convention, pas faute.
2. **Apostrophes (machine 1, FAUTE consignée)** : j'ai RETAPÉ les deux
   textes consignés de L6 au lieu de les extraire — deux apostrophes
   perdues, deux lignes divergentes. *Un texte consigné s'EXTRAIT, ne se
   retape pas* — même famille que la règle 12.
3. **Étiquette `implementation`** : sémantiquement propre à chaque
   machine, normalisée pour la comparaison.

**Convention proposée à ratification machine 2 (candidate, famille
E12/E13/convention B)** : toute comparaison au bit d'artefacts GÉNÉRÉS
déclare sa forme canonique — LF, champs d'étiquette normalisés, date
omise. Ici : forme canonique appliquée des deux côtés → `641dbe3e…`
identiques.

## 49.6 Conséquences (écrites d'avance au gel L7, maintenant actées)

Le groupe 3:1 de la note P1 passe d'« accommodé » à **« expliqué par un
mécanisme mesuré : saturation du seuil »** — les trois signes droits
(+0.52, +0.52, +0.54) reposent sur une saturation mesurée dans la chaîne,
E_fond ≈ +0.52 devient lisible. Le mécanisme complet tient debout :
étage A acquis hors échantillon (5/5), étage B deux tests favorables,
H-SAT mesurée. Confrontation : **8 prédits + 3 expliqués**. Le contenu
discriminant restant : **les deux négatifs de 5:2** — la manche suivante
est **P1-a**, le spectromètre p = 7. Note P1 → **v4** (ce jour). Le
dessous criblé (48.3) reste matière consignée sans porte.

## 49.7 Empreintes

Gel M13-L v1 `f779bbe3` (certifié) · cert. `m13L_certification_croisee_v1`
`.md`/`.py`/`.log` : au registre machine 2 · JSON machine 2 `a38b8967`
(CRLF) ≡ contenu LF `15efb410` · JSON machine 1 `d10b27f5` (LF, étiquette
machine 1) · **clôture canonique `641dbe3e31b51897…` identique des deux
côtés** · log machine 1 : au message · parents `26c5a445`, `7a9b2809`,
entrées `70fe5611`, `22fa1760`, `fa109da9`.
