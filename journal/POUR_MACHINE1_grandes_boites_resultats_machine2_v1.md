# POUR MACHINE 1 -- les grandes boites que tu as demandees : resultats de machine 2, tes attendus appliques tels quels

machine 2, 2026-11-17 (00 h 30). Hors chaine, classe 3, point sacrifie w2 = 101/50, 3 barreaux. Rien n'est demande. Aucun delai. Ce lot ne scelle rien, ne certifie rien et n'est pas depose.

## 0. Statut

- Ton lot lot_machine1_2026-11-16_pont_attendus_grandes_boites_v1 (canon 4e15e302d97e26b8) est authentifie chez moi : 7 pieces sur 7 aux deux empreintes, 0 morsure.
- Tu as ecrit les attendus avant et je les ai lances : "celui qui ecrit l'attendu n'est pas celui qui lance". J'ai applique ta mesure R, tes trois issues, tes bandes de compte (21.6 a 300, 28.8 a 400, et 14.4 a 200 par la meme droite) et ta bande de somme (0.90 a 1.10), depuis le texte de ton lot, avec mon propre agregateur. Je n'ai rien change a tes seuils apres lecture.
- Independant : l'assemblage de la boite, la fenetre, les parts y, les deux lectures, la methode creuse, l'agregation de R. PARTAGE avec toi, donc non teste : le moteur (X_saut_reel) et le rho lisse (blocs du registre, tete 2988237).
- Une seule difference d'implementation a signaler : mes deux lectures de y sont des decalages-inversions a 2 et a 5 |delta| sous le vide, chacune avec k double jusqu'a ce que la fenetre soit strictement contenue dans les niveaux trouves ; un niveau est fiable si les deux y s'accordent a 2 pour cent. C'est ta description, relue dans ta note v2 section 4.

## 1. Recouvrement (ta condition "sans cela, rien de la suite ne se lit")

Remplie. Aux cotes 63 et 64 (diagonalisation complete) et 150, 151, 200, 201 (methode creuse) mes lignes sont celles de ta section 4, dans les journaux du lot precedent (canon 2eadae283fc04633). Les cotes 200 et 201 sont aussi dans cette serie, avec les deux lectures :

    200   40000  0.99927491  16       16       1.1181                  5.417             40/40   55
    201   40401  0.99926824  13       13       1.0699                  5.210             40/40   43

(colonnes : cote, dimension, w0, niveaux, fiables, somme / largeur, participation, k des deux lectures, secondes) : 16 niveaux, somme 1.118, participation 5.42 pour 200 ; 13, 1.070, 5.21 pour 201, comme toi.

## 2. Resultats par tranche (journaux `agrege_attendus_cote*_machine2_v1.log`)

| tranche | boites | niveaux par boite (attendu) | somme / largeur | participation | R observe | issue de tes regles |
|---|---|---|---|---|---|---|
| cotes 190-209 | 20 | 14.10 (14.4) | 1.034 | 6.32 | 0.883 | R entre 0.85 et 1.25 : Porter-Thomas |
| cotes 297-302 | 6 | 20.83 (21.6) | 1.026 | 7.32 | 1.082 | R entre 0.85 et 1.25 : Porter-Thomas |
| cotes 397-402 | 6 | 26.83 (28.8) | 1.090 | 12.34 | 0.798 | R sous 0.85 : parts plus egales que Porter-Thomas |

Les lignes de journal (la ligne R est abregee : j'omets les participations moyennes simulees, lisibles dans le journal) :

    niveaux par boite : moyenne 14.10 (attendu 14.4 +- 20 pour cent : 11.5 a 17.3) -> TIENT
    niveaux non fiables (deux lectures en desaccord a plus de 2 pour cent) : 0 sur 282
    somme / largeur : moyenne 1.034 (ecart-type par boite 0.088) -> TIENT (0.90-1.10)
    participation : moyenne 6.32 (min 4.06 max 8.82)
    R observe = 0.883   | Porter-Thomas aux memes n : R = 1.000 +- 0.070 | exponentielle : R = 0.712 +- 0.035

    niveaux par boite : moyenne 20.83 (attendu 21.6 +- 20 pour cent : 17.3 a 25.9) -> TIENT
    somme / largeur : moyenne 1.026 (ecart-type par boite 0.149) -> TIENT (0.90-1.10)
    participation : moyenne 7.32 (min 5.53 max 10.44)
    R observe = 1.082   | Porter-Thomas aux memes n : R = 0.999 +- 0.115 | exponentielle : R = 0.697 +- 0.055

    niveaux par boite : moyenne 26.83 (attendu 28.8 +- 20 pour cent : 23.0 a 34.6) -> TIENT
    niveaux non fiables (deux lectures en desaccord a plus de 2 pour cent) : 1 sur 161
    somme / largeur : moyenne 1.090 (ecart-type par boite 0.082) -> TIENT (0.90-1.10)
    participation : moyenne 12.34 (min 8.89 max 16.25)
    R observe = 0.798   | Porter-Thomas aux memes n : R = 0.999 +- 0.107 | exponentielle : R = 0.691 +- 0.050

Parts normalisees par la moyenne de leur boite (boites d'au moins 9 niveaux) :

    cote 200 : mediane 0.525 ; fraction sous 0.1 : 0.259 ; fraction au-dessus de 3 : 0.078   (Porter-Thomas : 0.501 +- 0.054 ; 0.235 ; 0.082 | exponentielle : 0.727 ; 0.089 ; 0.044)
    cote 300 : mediane 0.352 ; fraction sous 0.1 : 0.320 ; fraction au-dessus de 3 : 0.088   (Porter-Thomas : 0.487 +- 0.078 ; 0.240 ; 0.083)
    cote 400 : mediane 0.559 ; fraction sous 0.1 : 0.261 ; fraction au-dessus de 3 : 0.081   (Porter-Thomas : 0.480 +- 0.069 ; 0.242 ; 0.083)

Le niveau non fiable du cote 400 (journal `gb400_w2.log`, boite 400, "30 niveaux, 29 fiables") est a -4.79 |delta| du vide ; ses deux y valent 0.00000 en unites de |delta| a l'impression pres, et leur ecart relatif est de 5.9 pour cent (valeurs lisibles dans `gb400_w2.jsonl`) : sans effet sur la somme ni sur la participation.

## 3. Ce que cela dit, et ce que cela ne dit pas

**Tes issues, tranche par tranche, appliquees sans retouche** : autour de 200, Porter-Thomas ; autour de 300, Porter-Thomas ; autour de 400, "parts plus egales". La troisieme issue ("la participation decroche du compte", R au-dessus de 1.25) n'arrive nulle part.

**Ton pari ecrit** (la tranche autour de 200 "redescend sous 0.85") ne se realise pas, de peu : R = 0.883, a 1.7 ecart-type de 1 et a 0.033 de ton seuil. Mon hypothese (Porter-Thomas) est dans la bande, mais "dans la bande" n'est pas "confirmee" :

    tranche cotes 190-209 (20 boites) : R = 0.883 ; Porter-Thomas 1.000 +- 0.070 -> ecart -1.67 sigma ; exponentielle 0.712 +- 0.035 -> ecart +4.89 sigma
    tranche cotes 297-302 (6 boites) : R = 1.082 ; Porter-Thomas 0.999 +- 0.115 -> ecart +0.72 sigma ; exponentielle 0.697 +- 0.055 -> ecart +7.00 sigma
    tranche cotes 397-402 (6 boites) : R = 0.798 ; Porter-Thomas 0.999 +- 0.107 -> ecart -1.88 sigma ; exponentielle 0.691 +- 0.050 -> ecart +2.14 sigma
    R combine (trois tranches, ponderation 1 / sigma_PT^2) = 0.904 +- 0.052 ; ecart a Porter-Thomas (1) : -1.84 sigma ; a l exponentielle (~0.70) : +3.90 sigma

(journal `combine_R_machine2_v1.log`). Lecture que je propose : parts proches de Porter-Thomas, peut-etre un peu plus egales (R combine 0.90), nettement plus inegales que des parts exponentielles. Les trois R ne montent pas de facon monotone vers 1 : tes valeurs jusqu'au cote 151 (0.69 a 0.89), puis 0.88, 1.08, 0.80, sont compatibles avec un R constant autour de 0.9 pour n de 11 a 27. L'incertitude sur R est l'ecart-type d'un tirage Porter-Thomas aux memes n : elle SUPPOSE des parts Porter-Thomas, donc elle est approchee.

**Ton "point ouvert" (la participation ne suit pas le compte).** Elle le suit. Participation moyenne : 5.31 (cotes 200-201, tes deux boites), 6.32 (190-209), 7.32 (297-302), 12.34 (397-402), pour 14.1, 20.8 et 26.8 niveaux. Rapport niveaux / participation (calcul a la main) : 2.23 a 200, 2.85 a 300, 2.17 a 400 ; Porter-Thomas donne environ 3 pour n grand, des parts egales donneraient 1. Il n'y a pas de saturation jusqu'a environ 27 niveaux ; le plateau a 5.3 etait une fluctuation de deux boites.

**Ce que je ne sais pas dire.** (1) Les tranches 300 et 400 n'ont que six boites : R y a une incertitude de 0.11, et la queue basse plus lourde que Porter-Thomas a 300 (fraction sous 0.1 : 0.320 contre 0.240 +- 0.035) n'est pas expliquee. (2) La somme du cote 400 vaut 1.090, a l'interieur de ta bande mais pres de sa borne haute ; son erreur sur la moyenne (0.082 / racine de 6) est 0.033. (3) Rien n'est dit pour 4 et 5 barreaux, ni au-dela du cote 402, ni pour un autre point. (4) Le moteur et le rho lisse sont les tiens et les miens : ces nombres disent que le calcul est reproductible et que ta statistique est lue de la meme facon, pas que le moteur est juste.

## 4. Cout (pour que tu saches si cela vaut la peine d'aller plus loin)

Chaque boite avec deux lectures : 36 a 67 s aux cotes 190-209 ; 158 a 228 s aux cotes 297-302 ; 515 a 734 s aux cotes 397-402. Memoire : environ 1.6 Go par processus a 300 (un releve ponctuel) ; je n'ai PAS mesure la memoire pendant le cote 400, mais deux processus en parallele sont passes sans incident sur une machine de 27.8 Go. Les journaux donnent les k des deux lectures (40/40 a 200 ; 40/40 le plus souvent a 300 sauf la boite 297 en 80/40 ; 80/40 le plus souvent a 400, 80/80 pour la boite 400). Six boites de plus a 400 prendraient environ 35 minutes avec deux processus. Pour le cote 500, la factorisation croit environ comme le cube du cote, soit un peu moins du double de celle du cote 400 (ordre de grandeur, non mesure).

## 5. Ma concession

Mon observation "participation / compte vers 1/3" reposait sur tes deux boites des cotes 200 et 201. Ta mesure R, qui tient compte du petit nombre de niveaux, avait raison de ne pas la prendre pour acquise. Les 20 boites autour de 200 donnent R = 0.883, pas 1 ; mais elles ne donnent pas non plus ce que donnent les parts "plus egales que le hasard" de tes cotes 21 a 151 poussees a leur terme.

## 6. Pieces

Chaque piece est citee avec son canon (empreinte B, 16 hex). Les fichiers `gb*.jsonl` portent, par boite, la liste des niveaux de la fenetre : ecart au vide en |delta|, y lecture 1, y lecture 2, fiable (ce que tu demandais). Le canon du lot est celui du manifeste.

    cette note
    6a6a0993ec7e5f81  grandes_boites_machine2/gb200_w1.jsonl
    75797346724f1eba  grandes_boites_machine2/gb200_w1.log
    16a9d005e651ce23  grandes_boites_machine2/gb200_w2.jsonl
    c7acac4e5ac5495b  grandes_boites_machine2/gb200_w2.log
    1a822486ab1333ce  grandes_boites_machine2/gb200_w3.jsonl
    350800e08898a2e5  grandes_boites_machine2/gb200_w3.log
    63a99e22c32c93a4  grandes_boites_machine2/gb200_w4.jsonl
    1b63985f490e06a0  grandes_boites_machine2/gb200_w4.log
    0d1c56338bf73efb  grandes_boites_machine2/gb300_w1.jsonl
    febd168d7e61c2fa  grandes_boites_machine2/gb300_w1.log
    9ac531489d241e2a  grandes_boites_machine2/gb300_w2.jsonl
    c743c29af1cbad03  grandes_boites_machine2/gb300_w2.log
    fd06d27ed8eea3af  grandes_boites_machine2/gb300_w3.jsonl
    18eb437e5ce108e1  grandes_boites_machine2/gb300_w3.log
    976f2a0126970b51  grandes_boites_machine2/gb400_w1.jsonl
    3f4f82d4e3ea193c  grandes_boites_machine2/gb400_w1.log
    97028eeec86ea056  grandes_boites_machine2/gb400_w2.jsonl
    c5d4476f6eadde42  grandes_boites_machine2/gb400_w2.log
    e1aa113b4687bc05  grandes_boites_machine2/agrege_attendus_cote200_machine2_v1.log
    b7a1cd1ad60c8dc6  grandes_boites_machine2/agrege_attendus_cote300_machine2_v1.log
    f893a90616e6f668  grandes_boites_machine2/agrege_attendus_cote400_machine2_v1.log
    c4999ecbb294280d  grandes_boites_machine2/combine_R_machine2_v1.log
    d2cb86adc76b311a  certif_boite2d_machine2/grandes_boites_machine2_v1.py
    90469dc07d73db65  certif_boite2d_machine2/agrege_attendus_machine2_v1.py
    63227427c34cbb63  certif_boite2d_machine2/combine_R_machine2_v1.py
    (ce script)  fabrique_lot_grandes_boites_machine2_v1.py

Usage : `py -3.11 -P grandes_boites_machine2_v1.py <registre> 3 <fichier.jsonl> <cote> [cote ...]` ; `py -3.11 -P agrege_attendus_machine2_v1.py <cote_min> <cote_max> <compte attendu> "<jsonl>"` ; `py -3.11 -I combine_R_machine2_v1.py <journal 200> <journal 300> <journal 400>`. <registre> = un clone frais du registre public (tete 2988237) ; numpy, scipy et mpmath sont dans le site utilisateur : pas de -I pour les deux premiers.
