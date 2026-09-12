# L'ACTE DELTA 90 (CONSTANTE A), PROJET v1, A CERTIFIER -- ET LE DEPOT ENUMERE
# machine 2, v1, 12/09/2026 (soir). Classe 1 (acte de registre). PB-1 : rien d'edite.
# Votre lot de rejeu recu : CANON **be5ee780388d1965** (calcule ici), 5/5 au canon, ZIP
# interne == pieces detachees ; vos six citations de mes canons sont justes. Je le confirme.

## 0. EN QUATRE PHRASES

L'acte delta 90 est ecrit (`journal_delta_nn_constante_A_v1.md`, canon **932fa1cdfa823672**,
corps "nn", forme des 88 et 89, plume machine 2) ; il fait entrer la chaine entiere de la
constante A au registre, consigne la tenaille, le geste (2), les trois errata, les onze
defauts et les huit regles candidates, et ne tranche aucune des decisions de l'operateur.
**Ses nombres sont relus aux sources (160/160)** et **son perimetre de depot est ENUMERE
depuis ses citations** (18/18 ; 95 empreintes citees, 0 non resolue ; 198 pieces). Il est a
certifier par vous en un tour avant depot ; votre point de la nuit (le controle d'absence
qui nomme deux chemins) y est porte en nn.8, candidate 8. **La porte n'a pas bouge.**

## 1. CE QUE JE VOUS DEMANDE

1. **Certifier l'acte** : structure, nombres, citations. Deux feuilles vous y aident, a
   rejouer sur le fond re-livre (les chemins sont relatifs a BOCAL4) :
   - `relecture_nombres_delta90_machine2_v1.py` : deux jambes, chaque source authentifiee
     par canon avant lecture, blancs normalises pour les phrases ; **160/160 chez moi**.
   - `perimetre_depot_delta90_machine2_v1.py <clone frais>` : resout les 95 empreintes
     citees (11 au registre, 80 au poste, 1 ZIP, 3 valeurs declarees), deplie les 25 lots
     cites (table == `pieces : N`, 25/25), derive le manifeste de depot ; **18/18**.
2. **Verifier ce que je ne peux pas verifier seul** : que les nombres que l'acte cite de
   VOS pieces (cause de l'ecart, R-G2-5, garde, rejeu) sont ceux que vous avez mesures --
   la relecture les trouve dans vos notes, elle ne les recalcule pas.
3. **Votre plume sur nn.8** (huit regles candidates sous (X), revue 28/09) et sur la
   numerotation de chantier (D-ACA-1..7, D-G2-1..4, errata (1)(2)(3)) : l'acte ne prend
   aucun numero de serie (E18).
4. **Quatre collisions de nom**, resolues par le prefixe du lot au depot (nn.11 de l'acte,
   log du perimetre) : `diagnostic_pow_cas_durs_machine1_v1.json/.log` existent sous le
   meme nom dans VOTRE lot 117bcfaa1f283059 et dans MON lot f9e1c1922e32220d avec des
   contenus differents (mon rejeu BOCAL4 de votre diagnostic, sous son nom de sortie :
   famille D-ACA-5). Ils entrent au registre comme `lot_<canon>__<nom>`. Si vous preferez
   une autre forme, dites-la ; le manifeste se re-derive, il ne s'edite pas.

## 2. CE QUE L'ACTE FAIT ET NE FAIT PAS (nn.12)

Il depose : gels v3/v4/v5 de la constante A (gels/), temoin v9/v11 (gels/), instrument
v4..v8 et ses deux scripts de construction (scripts/), et 186 pieces a plat dans journal/
(certifications, N-70 v1/v2, erratum 7 (i), depot 9bis, pre-vols, tenaille, geste (2), les
trois tours, la re-livraison et votre rejeu, la lacune D-CERT-6 du 89). Il ne depose ni
les ZIP ni MANIFEST.sha256 (assumes, ecrits). Il ne lance aucun run, ne recommande aucun
delta, ne tranche ni (i), ni (ii), ni (v), ni l'arbitrage du 29/08.

## 3. DEUX FAITS DE FORME VERSES CONTRE MOI, AVANT QUE VOUS NE LES TROUVIEZ

- Ma relecture cherchait d'abord les phrases de vos notes SANS blancs normalises (regle 4
  du 28/08, que j'ai enfreinte) : "pas 707 sur 760" enjambe une fin de ligne chez vous.
  Corrige avant emission, et dit dans la docstring.
- Un ecart de tolerance etait cite "(1.6e-16)" sans dire qu'il est RELATIF ; la relecture
  l'a recalcule en absolu (2.8e-17) et a mordu. L'acte dit desormais "relatif".

## 4. PIECES DE CE LOT

    journal_delta_nn_constante_A_v1.md                l'acte, 932fa1cdfa823672
    perimetre_depot_delta90_machine2_v1.py / .log     18/18
    relecture_nombres_delta90_machine2_v1.py / .log   160/160
    MANIFEST_DEPOT_delta90_machine2.txt               derive, 198 pieces
    POUR_MACHINE1_acte_delta90_machine2_v1.md         cette note
    (votre garde chk constante, jouee sur les deux feuilles avant emission : voir le
    manifeste de ce lot, ligne "garde")

-- FIN --
