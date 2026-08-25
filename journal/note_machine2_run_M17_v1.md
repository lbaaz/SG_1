# RUN M17 -- LA MANCHE QUANTIQUE EST JOUEE -- machine 2 (BOCAL4)
# 24-25/08/2026, 23h09 -> 00h50 (1 h 41 de moteur)

## RESUME (dix lignes)

    VERDICT : **PAS DE SIGNAL**        (cascade, branche 6)
    P3 ECHOUE  rho 5/7  contre rho_crit 29/35  p_exact 49/720  n_eff 6
    P6 ECHOUE  rho 1/35 contre rho_crit 29/35  p_exact 1/2     n_eff 6
               violations_ii = 0  (le jumeau a signe retourne : 6/6)
    comptes G-5 : **0 repris + 34 calcules == 34 attendus : OK**
    statuts COMPTES : 25 EN DOMAINE, 8 ARRET DE REGLE, 1 SITE EXACT
    gardes : P7 sain ; 0 G-9 mordue ; 0 G-4 mordue ; 0 ex aequo ;
             arrets_points [] ; arrets_sans_index []
    consignes : P2 les deux cotes dans la bande ; P4 dans la bande ;
                P5 0/3 ; P8 non calculable (declare, section 3)
    instrument execute : m17_chaine_v17.py  82a0be882568fe0c  103150 o
    dossier : manche_m17_v17/  MANIFEST 4aecd0e2b23bc818  36 lignes

---

## 1. LE VERDICT, ET IL EST PRONONCE

**PAS DE SIGNAL** -- le nom que le gel (section 8) donne au resultat
NEGATIF. Ce n'est pas un non-concluant : **les deux primaires avaient
leurs six points**, la barre etait franchissable, et elles ne l'ont pas
franchie.

**P3 (lien au registre classique, en rang)** :

    rangs classiques  [3, 2, 1, 4, 5, 6]
    rangs quantiques  [5, 3, 1, 2, 4, 6]
    rho = 5/7 (0,7143)   rho_crit(6, 0.05) = 29/35 (0,8286)
    p_exact = 49/720 (0,0681)

L'estimateur quantique ordonne **presque** comme le classique, et manque
la barre. Le p exact (0,068) est au-dessus d'alpha = 0,05. **A six
points, deux inversions coutent la manche.**

**P6 (validation 2D)** :

    (i)  rho = 1/35 (0,0286)   p_exact = 1/2   -> PLAT
    (ii) violations = **0 / 6**

Le (i) n'est pas "juste en dessous" : il est **nul**. Lambda_c decroit
proprement de 1,2597 a 0,90232 quand w2 monte ; Gamma_LS fait un creux a
2,02 (6,562e-11) puis explose a 2,05 (2,661e-09, trente fois les
autres). **La largeur de resonance ne suit pas la barriere d'action sur
cette grille.**

**Les consignes, qui ne portent pas le verdict** :

    P2  loi en epsilon : gauche 0,97357  droite 1,01838
        -> **les deux cotes dans la bande** (tau_P2 = 0,05)
    P4  ecart-type du residu ln(K_s_Q / K_s_ff) = 0,03008
        contre bande_P4 = 0,6 -> dans la bande, d'un facteur 20
    P5  asymetrie : **0/3** -- le signe predit par Sigma2 echoue aux
        trois paires
    P8  **non calculable** -- voir section 3

**Lecture d'ensemble, et je la donne comme lecture** : l'estimateur
quantique **reproduit les lois d'echelle** (P2 des deux cotes, P4 a un
facteur 20 dans la bande) et **echoue a reproduire les ORDRES** -- celui
du registre classique de peu, celui de la barriere pas du tout, celui de
l'asymetrie 0/3.

---

## 2. **CE QUE LE FANTOME A DONNE** -- le seul element qui porte sur le signe

`violations_ii = 0`, six points sur six. Aux six geometries, la branche
physique (`signe_fantome = -1`) rend une largeur de **8,44e-11 a
2,66e-09** ; le jumeau a signe RETOURNE (`+1`), meme geometrie, meme
graine, meme absorbeur, rend :

    w2 = 1.95  -1,213e-14      w2 = 2.02  -1,322e-14
    w2 = 1.97  +6,752e-15      w2 = 2.03  -6,503e-14
    w2 = 1.98  +5,799e-14      w2 = 2.05  -7,550e-14

**Quatre a cinq ordres de grandeur sous la branche physique, et le SIGNE
CHANGE d'un point a l'autre** : c'est le plancher numerique du solveur,
celui que P7 vient d'apprendre a reconnaitre, pas une petite largeur.

*Ce que ca etablit* : la largeur ne vient ni de la discretisation, ni de
l'absorbeur, ni de la graine -- **elle vient du signe**. Retourner le
fantome la fait disparaitre dans le bruit. C'est un controle negatif qui
tient sur la grille entiere, pour la premiere fois.

*Ce que ca n'etablit pas* : que le fantome existe. La manche prend le
modele pour acquis et teste la COHERENCE de l'estimateur avec ce que la
campagne sait par ailleurs. Le controle qui tient est une pierre, pas
une preuve.

---

## 3. **TROIS FAITS QUE CE RUN A REVELES** -- a la file

**(a) LE CHEMIN DE REJET A L = 30 A ETE PRIS, POUR LA PREMIERE FOIS.**
Le point P8 a g = 1e-3 porte le motif *"erratum 4.6 : descente rejetee a
L = 30 (bord de fenetre)"*. Il a joue L = 20 (dim 8100) **puis** L = 30
(dim 10000) : 67 minutes, la moitie du temps de la manche.
**Consequence a mesurer, et elle est severe** : sous la v14 ou la v15,
ce point serait mort par `KeyError('G9_mordue')` -- **la manche entiere
serait tombee a 00h50, apres 1 h 40 de calcul, sans aucun verdict**. Le
correctif D-M17-31, exige ce soir et joue avant d'etre envoye, est ce
qui a permis a ce run d'exister. *Le chemin que personne n'avait jamais
emprunte a ete emprunte au premier run reel.*

**(b) VINGT-QUATRE POINTS SUR TRENTE-QUATRE NE SONT JAMAIS LUS.**
Compte, pas affirme : l'assembleur ingere le site, les blocs P8 et les
seuls `f070` -- **10 points**. Les 24 autres (fractions 0,50 / 0,85 /
1,00 / 1,20) sont calcules, ecrits, comptes en G-5, et **aucune ligne de
l'assemblage ne les ouvre** : P3, P4, P5 et P6 lisent tous `en_dom`, qui
ne contient que les `f070`. La boucle d'ingestion n'a pas de branche
`else`.

**(c) SIX ARRETS QUE LA CASCADE NE VOIT PAS.** Les six points a fraction
0,50 -- un par w2 -- sont en **ARRET DE REGLE** (motifs : `stationnarite
M operative` jusqu'a 3,091e+285, et `descente non stationnaire (budget
8)`). Ils ne sont pas dans `pts`, donc pas dans `arrets`, donc **la
branche 1 ne les voit pas**. Le verdict de cette manche n'en depend pas
-- il se joue sur les `f070`, comme le gel le prescrit -- mais *un arret
que personne ne lit n'arrete rien*, et la campagne a une regle
la-dessus.

**Deux questions de GEL, que je ne tranche pas** : a quoi servent les
quatre autres fractions que 4.10 prescrit, si rien ne les lit ? et un
ARRET a une fraction non lue doit-il compter en branche 1 ?

**(d, mineur) P8 EST NON CALCULABLE**, et par construction : sa pente
log-log demande Gamma_c a trois valeurs de g, or g = 3e-3 a une
**barriere VIDE** (aucun site, donc aucun Gamma_c), g = 1e-3 est en
arret, et g = 3e-4 est infaisable (`N_derive = 206 > N_max = 120`) --
le gel estimait 231 en 4.11, mesure **206**, ecart 11 pour cent).
P8 ne participe pas au verdict (4.11) : rien n'est en danger, tout est
consigne.

---

## 4. LES GARDES : TOUTES PASSANTES, ET CE SONT DES COMPTES

    P7_sain = True   -- joue POUR DE VRAI sur le dossier de la manche :
                        L_retenu = 20 lu du point NOMME, cellules
                        -4,203035e-14 (marge 51,8 x) et -6,922631e-14
                        (marge 32,6 x), FREE = 0.0 exact
    G-9 mordues      : 0   (G9_points = [])
    G-4 mordues      : 0   (NON APPLICABLE partout, p impair, L9)
    ex aequo         : 0   (arret_ex_aequo = [])
    arrets_points    : []  (aucun point f070 en arret)
    arrets_sans_index: []  (aucun point sans w2)
    carte PR-6       : selectionnees 6 + ecartees 3 == 9 lignes
    appariement      : les six w2 mesures = les six w2 de la carte,
                       PAR VALEUR (regle 11)
    ancres           : ancres_manquantes() = [] ; les quatre erratums
                       E33..E36 sont consignes -- aucune primaire n'est
                       neutralisee par construction

**C'est la premiere fois de la campagne que la branche 1 reste muette.**

---

## 5. CE QUE CE RUN N'ETABLIT PAS -- et ca ne se coupe jamais

- **il ne refute pas le modele** : PAS DE SIGNAL dit que l'estimateur
  quantique et les references de la campagne ne s'ordonnent pas
  ensemble a ce site, pas que le fantome n'existe pas ;
- **six points, c'est le minimum du gel** (n_min = 5). A n = 6, la barre
  est 29/35 et deux inversions suffisent a tout perdre. **La puissance
  de ce test est faible, et le gel le savait** : c'est une limite
  declaree, pas une surprise ;
- il ne dit rien **hors de ce site** (2:1, p = 5) ni hors de la fenetre
  [1,95 ; 2,05] ;
- la marge de P7 n'est etablie **qu'au point nominal** : les cinq autres
  n'ont pas ete confrontes a la clause (leur jumeau borne n'est pas
  mesure) ;
- **S-H** et la reserve **B_N** restent hors manche ;
- la lecture d'ensemble de la section 1 (echelles oui, ordres non) est
  **une lecture**, pas un verdict : le gel ne prevoit pas cette
  categorie, et je la donne comme telle.

---

## 6. PIECES ET CUSTODY

**L'instrument execute, empreinte ET taille, dans ce document** (N-59,
etape 6 du gel -- relevees AVANT le lancement, a 23h09) :

    m17_chaine_v17.py   **82a0be882568fe0c**   **103150 o**

```
    manche_m17_v17_MANIFEST_machine2.txt           4aecd0e2b23bc818    1577
    manche_m17_v17/assemblage.json                 0be34834c78d1fcf    1846
    manche_m17_v17/temoins_P7.json                 28a840cf73a18730     710
    manche_m17_v17/pt_39_20_f070.json              bd012b6b08b56d25    4794
    manche_m17_v17/pt_39_20_P8_g0.001.json         85b167b7ca7724c8    4260
    run_manche_v17_machine2_v1.log                 76371babdf34bdf4      87
    m17_chaine_v17.py                              82a0be882568fe0c  103150
    m17_pre_enregistrement_quantique_v12_b2.md     20950e52e7d63225   58507
    pr6_carte_classique_etendue_v1.json            d32761567d24024f    3600
    note_machine2_certification_v17_m17_v1.md      c344f55940a75772    5333
    note_machine2_pilote_v17_m17_v1.md             9807908e0eb76aba    4605
    controleur_note_run_M17_machine2_v1.py         a0aa97e64be4ffd5    5633
```

Le **controleur de la presente note** est depose avec elle : il re-derive
les empreintes, RE-OUVRE l'assemblage et les 34 points pour recompter
chaque nombre cite, re-derive les **36 lignes du MANIFEST**, et finit par
trois tests negatifs.

Le **MANIFEST** porte les 36 empreintes du dossier de manche (34 points,
temoins_P7.json, assemblage.json), une par ligne, convention B. Toute
piece du run se verifie par lui.

Empreintes re-derivees le 25/08/2026 depuis `d:/devs/bocal/BOCAL4/`.
L'empreinte de la presente note se prend a l'acte, apres figeage.

-- FIN note_machine2_run_M17_v1 --
