# Note hors chaîne — reprise de la piste (0) : sous un absorbeur long, la lecture 2D a un plateau (v1)

Machine 1, 15/11/2026. **HORS CHAÎNE, NON OPPOSABLE, POST HOC.** Classe 3, plume machine 1 seule, non
contresignée, jouée sur le conteneur de machine 1 (Linux x86_64, python 3.13.18, numpy 2.5.3, scipy
1.18.1, levier X86_V4). N'engage aucun numéro, ne touche à aucun verdict déposé, et ne relit pas la
nuit bis sous d'autres seuils : son verdict reste NON QUALIFIÉ, sous son gel. Ouverture par
l'opérateur : « ouvre », 15/11/2026, 08 h 38, sur la proposition de machine 1 de « calculer d'abord
ce qui se calcule sans run, puis dire si cela vaut un gel ». Le garde-fou « dernier essai » du gel
bis n'est pas levé par cette note : l'opérateur seul le lève.

## 1. Verdict

1. Aux six points de M17, l'état lu a une largeur 2D qui ne dépend plus de l'absorbeur dès que
   celui-ci est long. Sous un absorbeur quartique (forme F2 du gel bis) de 60 couches, la largeur
   tient dans 0,5 % sur 6 à 9 barreaux consécutifs selon le point ; à
   80 couches, sur 8 à 9. La nuit bis en demandait cinq, à 5 %.
2. La valeur du plateau est la même à 0,70 % près, au pire des six points, sous cinq
   absorbeurs : F2 à 60 et à 80 couches, F1 à 80, F3 à 60, F1 au bord translaté de 10 à 60 couches.
   Force, forme, longueur, position : les quatre variations que le gel bis voulait éprouver.
3. La nuit bis a rendu NON QUALIFIÉ parce que ses absorbeurs, de 20 et 30 couches, étaient trop
   courts pour un critère de cinq barreaux. Avec le même critère et 40 couches, F1 aurait un plateau
   à 6 points sur six, F2 à 6, F3 à 6 (tableau du §5).
4. M17 avait lu juste : sa valeur (k = 3, F1, 20 couches) vaut 0,9789 à 1,0168 fois le
   plateau, soit 2,1 % d'écart au pire.
5. La chaîne d'ordre 2, lue sur son propre plateau, vaut 1,0083 à 1,0582 fois le
   plateau 2D. C'est le résiduel de la chaîne débarrassé de l'absorbeur des deux côtés.
6. Cela vaut un gel : celui du §8, proposé, non décidé. Il ne porte que sur l'état lu de six points
   déjà joués ; rien n'est dit ici des autres états ni des autres points.

## 2. Ce qui a été calculé, et où

Trois calculs, dans l'ordre où ils ont été faits.

- **La chaîne seule** (aucune diagonalisation 2D) : son plateau sous son propre absorbeur (§6), puis
  une tentative d'émuler sur la chaîne l'absorbeur de la lecture 2D (§7).
- **Un lecteur 2D creux**, validé contre les sorties de la sonde certifiée de la nuit bis (§3).
- **L'exploration** : ce lecteur, sous des absorbeurs que la nuit bis n'a pas joués, à l'état lu des
  six points de M17 et au témoin positif (§4, §5).

E19. Les diagonalisations 2D de cette note sont toutes aux six points f070 du run M17 (1,95, 1,97,
1,98, 2,02, 2,03, 2,05) et au témoin, tous déjà joués sous deux gels. Machine 1 n'a rien calculé en
2D à aucun point des deltas 96, 97 et 98, ni à aucun point neuf. Ces six points sont désormais vus
de machine 1 sous absorbeur long : ils ne peuvent plus être des points jugés.

Sources, au registre à 8d54bf9 (convention B) :

    82a0be882568fe0c  scripts/m17_chaine_v17.py — le moteur
    dcda1611adf5f8fd  gels/qualification_EB_bis_pre_enregistrement_v1.md — le gel bis
    bdf8c5a0c73096a4  journal/journal_delta_95_qualification_EB_bis_v2.md — l'acte 95 (nuit bis : NON QUALIFIÉ)
    c110c6286157b025  journal/lot_a01598ec24237921__sonde_etage2.json — la sortie de la sonde certifiée, étage 2 de la nuit bis
    1ae4b5b2f9ff0e70  journal/lot_a01598ec24237921__sonde_etage1.json — idem, étage 1 (témoin)
    4d51dd58ef456fe9  journal/tp_reference_machine2_v1.json — la référence du témoin, par rotation complexe (machine 2)
    41153158190cf7f1  gels/gel_ordre2_chaine_EA_pre_enregistrement_v1.md — le gel de la chaîne d'ordre 2
    c2f3e5c9102dc1a7  journal/journal_delta_98_ordre2_chaine_EA_v1.md — l'acte 98
    10887c60d5f55bcf  journal/sonde_ordre2.json — la sortie de la sonde du delta 98
    d51a9c6ce98b0452  journal/sonde_domaine_G1.json — idem, delta 97
    5d80bf2edd26a6c1  journal/sonde_chaine_par_etat.json — idem, delta 96

## 3. Le lecteur creux

La sonde certifiée décompose toute la matrice (3600 à 5041 lignes à la nuit bis) et lit −2 Im E.
Le lecteur creux assemble le même hamiltonien, élément par élément, par la fonction du moteur, puis
cherche le seul état voulu par décalage-inversion autour de son énergie ; il retient, parmi les
voisins, l'état de plus grand poids au site de Fock de l'étiquette, et lit la largeur par
l'identité Γ = 2 η ⟨W⟩, exacte pour un vecteur propre droit.

- Assemblage : écart nul, à l'élément près, au H_2D du moteur à N = 60.
- Contre la sonde certifiée de la nuit bis : 180 lectures (état lu, 18 barreaux ; les cinq
  configurations à 1,98, F1 à 20 couches aux cinq autres points), pire écart relatif
  0,39 %. Les énergies concordent à 3e-13 près.
- Cet écart est le bruit de la sonde dense, pas celui du lecteur : sur les 2400 lectures de
  l'exploration, les deux lectures du lecteur creux (2 η ⟨W⟩ et −2 Im E) concordent à
  6e-12 près en relatif, et le pire résidu du vecteur propre vaut 2e-15. Le
  « plancher » de 1,33e-13 des gels précédents est celui de la décomposition dense.
- Témoin positif (jumeau H+, j = 6 et j = 8, référence par rotation complexe) : sous F1 et F2 à 60
  et 80 couches, la largeur lue reste à moins de 0,5 % de la référence sur 8 à
  11 barreaux consécutifs depuis k = −5, pire écart 0,13 %. L'incertitude
  déclarée de la référence est de 0,2 % à j = 6.

Ce lecteur n'est pas certifié. Il coûte d'une demi-seconde (N = 60) à six secondes (N = 120) par
lecture sur deux cœurs, contre une demi-minute par décomposition à N = 60 sur BOCAL4.

## 4. Résultat : cinq absorbeurs longs, six points

Chaque case donne la valeur de la meilleure fenêtre de cinq barreaux (règle 3.11 du gel bis),
rapportée à la lecture de M17 ; entre parenthèses, l'étalement de cette fenêtre et le nombre de
barreaux consécutifs qui tiennent dans 0,5 %. Échelle : k = −5 à 14, η_k = η0 · 2^(−k). Bord à r0
sauf la colonne « translaté » (r0 + 10).

| w2 | F2, 60 couches | F2, 80 | F1, 80 | F3, 60 | F1 translaté, 60 | M17 / plateau | chaîne / plateau |
|---|---|---|---|---|---|---|---|
| 1,95 | 1,0217 (0,05 %, 6) | 1,0216 (0,00 %, 8) | 1,0207 (0,72 %, 4) | 1,0175 (1,48 %, 3) | 1,0213 (0,32 %, 6) | 0,9789 | 1,0483 |
| 1,97 | 1,0055 (0,00 %, 7) | 1,0055 (0,00 %, 8) | 1,0021 (0,63 %, 4) | 0,9996 (1,48 %, 3) | 1,0060 (0,11 %, 5) | 0,9946 | 1,0181 |
| 1,98 | 1,0025 (0,01 %, 7) | 1,0025 (0,01 %, 9) | 1,0020 (0,83 %, 4) | 0,9975 (0,85 %, 3) | 1,0045 (0,49 %, 5) | 0,9975 | 1,0083 |
| 2,02 | 1,0099 (0,03 %, 9) | 1,0098 (0,00 %, 8) | 1,0073 (0,57 %, 4) | 1,0071 (0,62 %, 4) | 1,0112 (0,29 %, 5) | 0,9903 | 1,0088 |
| 2,03 | 1,0020 (0,03 %, 6) | 1,0020 (0,01 %, 8) | 1,0031 (0,23 %, 6) | 1,0027 (0,17 %, 5) | 1,0004 (0,27 %, 5) | 0,9980 | 1,0208 |
| 2,05 | 0,9838 (0,22 %, 6) | 0,9835 (0,06 %, 8) | 0,9882 (1,52 %, 3) | 0,9882 (1,17 %, 4) | 0,9866 (0,56 %, 4) | 1,0168 | 1,0582 |

« Plateau » dans les deux dernières colonnes : la colonne F2 à 80 couches. « Chaîne » : la chaîne
d'ordre 2 sans boîte, sur son plateau (§6).

Les cinq absorbeurs ont un PLATEAU au sens du gel bis aux six points : pire étalement
1,52 %, contre un seuil de 5 %. Par absorbeur, pire étalement sur les six points : F2
à 60 couches 0,22 %, F2 à 80 0,06 %, F1 à 80 1,52 %, F3
à 60 1,48 %, F1 translaté 0,56 %. Le quadratique (F1, F3) converge
plus lentement que le quartique : 3 à 6 barreaux à 0,5 % sous F1 à
80 couches.

## 5. Pourquoi la nuit bis n'a pas vu ce plateau

Étalement de la meilleure fenêtre de cinq barreaux, en pour cent, par forme et par longueur, bord à
r0 ; dernière colonne : nombre de points à PLATEAU au seuil de 5 % du gel bis. Les lignes à 20 et 30
couches de F1, et à 20 couches de F2, sont des configurations de la nuit bis, relues ici par le
lecteur creux sur la même échelle (k = −5 à 12) ; elles rendent les mêmes comptes que la nuit (1, 5
et 1 sur six).

| forme | couches | 1,95 | 1,97 | 1,98 | 2,02 | 2,03 | 2,05 | PLATEAU |
|---|---|---|---|---|---|---|---|---|
| F1 | 20 | 4,54 | 5,81 | 15,31 | 12,79 | 9,94 | 7,98 | 1 sur 6 |
| F1 | 30 | 3,42 | 4,58 | 3,36 | 1,94 | 2,43 | 7,98 | 5 sur 6 |
| F1 | 40 | 1,37 | 3,26 | 2,00 | 2,16 | 1,37 | 4,02 | 6 sur 6 |
| F1 | 60 | 1,55 | 1,71 | 0,92 | 0,59 | 0,21 | 2,17 | 6 sur 6 |
| F1 | 80 | 0,72 | 0,63 | 0,83 | 0,57 | 0,23 | 1,52 | 6 sur 6 |
| F2 | 20 | 7,74 | 6,67 | 8,20 | 8,08 | 6,30 | 3,51 | 1 sur 6 |
| F2 | 30 | 1,35 | 1,28 | 0,61 | 1,25 | 1,48 | 3,18 | 6 sur 6 |
| F2 | 40 | 0,37 | 0,69 | 0,48 | 0,10 | 0,12 | 0,40 | 6 sur 6 |
| F2 | 60 | 0,05 | 0,00 | 0,01 | 0,03 | 0,03 | 0,22 | 6 sur 6 |
| F2 | 80 | 0,00 | 0,00 | 0,01 | 0,00 | 0,01 | 0,06 | 6 sur 6 |
| F3 | 30 | 3,57 | 4,60 | 3,17 | 1,90 | 1,63 | 9,13 | 5 sur 6 |
| F3 | 40 | 1,43 | 2,93 | 2,01 | 2,13 | 0,81 | 4,40 | 6 sur 6 |
| F3 | 60 | 1,48 | 1,48 | 0,85 | 0,62 | 0,17 | 1,17 | 6 sur 6 |

Deux effets distincts bornent la zone plate. Du côté de l'absorbeur fort, la réflexion sur le front
de l'absorbeur : elle ne dépend pas de la longueur (sous F1, les trajectoires à 20, 30, 40, 60 et
80 couches coïncident à 0,16 % près de k = −5 à k = 2, aux six points) mais de la forme, et
le quartique allongé la supprime. Du côté faible,
le retour depuis le bord de la boîte : il recule quand la boîte s'allonge. À 20 couches, il ne
reste presque rien entre les deux.

Un absorbeur dont le bord est ramené vers l'état perd son plateau. À r0 − 10 et 50 couches, la
meilleure fenêtre s'étale de 4,9 à 14,2 % selon le point (1 point sur six
sous 5 %). À r0 − 20, où le bord entre dans la barrière, la largeur lue monte, selon le point,
jusqu'à 4,3 à 13,0 fois celle de M17. Le bord doit rester au-delà de la barrière.

## 6. La chaîne sans boîte a aussi son plateau

La chaîne d'ordre 2 du gel 41153158190cf7f1, longue de 400 sites, sous son propre absorbeur
(début à 8, 16 et 24 sites après le bord de la barrière ; force 1/8, 1/16, 1/32, 1/64 de |δ|) : la
largeur de l'état lu tient dans 0,50 % sur les douze réglages, au pire des six
points. La lecture retenue par le gel du delta 98 (début à 4 sites, force 1/16) est au-dessus de ce
plateau de 0,05 à 1,19 % : sans effet sur un verdict jugé à des bornes de 1,25 à
2, mais le résiduel déposé est surestimé d'autant à ces six points.

## 7. La voie essayée d'abord, et ce qu'elle vaut

Avant d'allonger l'absorbeur, machine 1 a tenté de faire de la chaîne un modèle de l'instrument :
la chaîne tronquée à la boîte de la lecture 2D, munie du même absorbeur, intermédiaires compris.

- Aux quatre points centraux (1,97 à 2,03), sur k = 0 à 2 et les cinq configurations de la nuit
  bis, le rapport lecture 2D / émulation s'étale de 1,1 à 3,8 %, là où la
  lecture brute s'étale de 7,2 à 25,0 %. La chaîne rend donc l'essentiel
  de la dépendance à la forme du côté fort : c'est une réflexion sur le front, à une dimension.
- À 1,95 et 2,05, elle ne le rend pas : étalement 22,9 et 10,0 % après division, contre
  5,2 et 13,8 % brut. Explication probable, non éprouvée : le saut de la chaîne n'y est plus
  petit devant les écarts d'énergie à l'endroit de l'absorbeur.
- Elle ne prédit pas le verdict de plateau : accord avec la nuit bis à 19 couples
  (point, configuration) sur 30, quand répondre « pas de plateau » partout en donne 19.
- Sur 257 états des trois sondes déposées (k = 2, 3, 4, données qui n'ont pas servi à l'écrire),
  elle ne réduit pas la dispersion : entre k = 2 et k = 3, écart médian 1,6 % brut,
  1,3 % après division ; entre k = 4 et k = 3, 4,6 % et 4,6 %.

Cette voie est abandonnée comme voie de qualification. Elle laisse une explication, pas un
instrument.

## 8. Le gel que cela vaut (proposition ; rien n'est décidé)

La question est celle du gel bis, mot pour mot : la largeur lue est-elle indépendante de la force,
de la forme, de la longueur et de la position de l'absorbeur ? Une seule différence de fond : des
absorbeurs de 60 et 80 couches au lieu de 20 et 30, et le lecteur qui les rend abordables.

- **Instrument.** Le lecteur creux, à réécrire indépendamment et à certifier par machine 2. Étage
  0 du run : il doit redonner la sonde dense certifiée aux deux ancres.
- **Témoin.** Le jumeau H+ aux deux couplages retenus, sous les mêmes absorbeurs : plateau, et
  accord à la référence. Il est réglé (vu au §3), pas aveugle.
- **Points jugés.** Les douze points jugés du delta 98, où machine 2 a lu à k = 2, 3, 4 sous 20
  couches et où machine 1 n'a rien calculé en 2D. Les six points de M17 deviennent des ancres
  réglées.
- **Absorbeurs.** F2 à 60 couches (référence), F2 à 80 (longueur), F1 à 80 (forme), F2 translaté
  de 10 à 60 (position).
- **Ce qu'un succès autoriserait à écrire.** Aux états jugés, la largeur est une largeur sortante
  indépendante de l'absorbeur ; les lectures déposées à k = 3 en sont à tant pour cent ; le
  reclassement « ordre de grandeur » du delta 95 est levé pour ces états. Et le résiduel de la
  chaîne devient un écart entre deux largeurs intrinsèques.
- **Ce qui reste à calculer avant d'écrire une seule borne.** Les autres états des six points de
  M17 (seul l'état lu est exploré ici), pour fixer tolérances et annonces. Aucune probabilité
  n'est annoncée dans cette note.

Coût estimé du run : quelques heures sur BOCAL4, à préciser quand le lecteur de machine 2 existe.

## 9. Limites

- Un seul état par point (l'état lu), six points, fraction 0,70, canal (2,1) de x⁵, |δ| de 0,02 à
  0,05. Rien au-delà.
- Post hoc : l'absorbeur a été allongé après avoir vu la nuit bis échouer. Le critère (cinq
  barreaux, 5 %) est celui du gel bis, non retouché ; les seuils de 0,5 % sont des descriptions.
- Le lecteur creux n'est pas la sonde certifiée ; il choisit l'état par son poids au site de
  l'étiquette, pas par recouvrement avec la graine puis suivi. Aux 180 lectures comparées,
  c'est le même état (énergies à 3e-13 près).
- « Indépendante de l'absorbeur » ne dit rien de l'unitarité, de l'auto-adjonction ni de la
  dynamique du système fermé : l'absorbeur ne mesure qu'un taux sortant.

## 10. Défauts et observations (numéros de chantier)

- D-P0R-1 (m1, gels v2 et bis). Les longueurs d'absorbeur du banc (20 et 30 couches) ont été
  reprises de la géométrie du run sans qu'aucun balayage en longueur ne sépare « il n'y a pas de
  plateau » de « l'absorbeur est trop court ». La clause de reclassement (gel bis, section 13)
  attachait une conséquence sur l'objet à un critère qui éprouvait d'abord l'instrument.
- D-P0R-2 (m1). Le matin même, machine 1 a d'abord cherché du côté de la chaîne (§7) ; l'épreuve
  décisive, allonger l'absorbeur, était plus simple et n'a été faite qu'ensuite.
- O-P0R-1. Le lecteur creux n'a pas de plancher à 1e-13 : le plancher des gels précédents est
  celui de la décomposition dense (§3).
- O-P0R-2. La lecture de chaîne du gel du delta 98 est de 0,05 à 1,19 % au-dessus
  du plateau de la chaîne aux six points (§6). À porter à un acte suivant.
- O-P0R-3. Aucune pièce déposée n'est éditée (PB-1). L'acte 95 dit vrai « au sens du gel ».

## 11. Pièces (convention B)

    1d9b525c48f3ca4f  lecteur_2D_creux_machine1_v1.py
    555f8235cb13e1e7  lecteur_2D_creux_machine1_v2.py
    9f9f576679bcd7b8  validation_lecteur_creux_machine1_v1.py
    0873e592d0af7692  validation_lecteur_creux_v1.log
    d4fe9da79b5c97cf  exploration_absorbeurs_machine1_v1.py
    1724631cadfcc69d  exploration_v1.json
    213c0909f29598e6  exploration_v1b.json
    c852beafc6f7dc07  lecture_exploration_machine1_v1.py
    fae4089b28a73d3c  temoin_absorbeurs_longs_machine1_v1.py
    cc40ac6d3727d6ab  temoin_absorbeurs_longs_v1.log
    3f6d8f57e1dec837  chaine_sans_boite_machine1_v1.py
    eebe2c4542b7cc0e  chaine_sans_boite_v1.json
    51b7fd10b089f4b6  chaine_longue_plateau_machine1_v1.py
    f35f46a024501290  chaine_longue_plateau_v1.log
    7ea9551653c20cff  emulation_absorbeur_machine1_v1.py
    41e354c7eece90e6  emulation_v1.json
    6882062f9237af34  lecture_emulation_machine1_v1.py
    976521a5431065db  lecture_corrigee_machine1_v1.py
    bc05fbcc9a257de1  plateaux_emulation_machine1_v1.py
    96b0d864aecc24f3  emulation_hors_echantillon_machine1_v1.py
    4d7d4d891ccb2145  emulation_hors_echantillon_v1.json
    5faff44c9219409a  lecture_hors_echantillon_machine1_v1.py
    5e927fca16cf6f89  lecture_hors_echantillon_v1.log
    (ce script)        construction_note_piste0_reprise_machine1_v1.py
    0de6c0ef8bb76352  note_piste0_reprise_gabarit.txt
