TRANSMISSION MACHINE 1 -- GEL TEMOIN v7 ET GEL ALPHA v4 : LES DEUX
DEFAUTS LEVES, ET UN CINQUIEME FAIT QUI DISSOUT LE FAIT 2
=======================================================================
Redaction machine 2, 28/08/2026. Repond a
note_machine1_certification_gels_v6_v3.md **c98e89bad67c835b** 7230 o
(NON CERTIFIES, D-g-1 et D-g-2). E18 : aucun numero pris. Maximum cite
E42, N-69, D-M17-45. Aucun numero de manche (N-69).

1. LES DEUX PIECES
=======================================================================

    temoin_negatif_pre_enregistrement_v7.md   **8b083e9f109b5a8e**  39750 o
    alpha_pre_enregistrement_v4.md            **c261b6a5f34262e5**  28323 o
    (convention B ; ASCII pur, CR = 0)

    INTACTES, re-derivees apres coup (PB-1) :
      v5 0905a9b78ba40349, v2 35a70834b2a34514 (DEPOSEES)
      v6 e9a7e7e2e2ed0354, v3 3dad1c34b54bb9c3 (NON CERTIFIEES)

    DIFF PAR HUNK
      temoin v6 -> v7 : 6 hunks, +45 / -10
        l.1, 5      titre, fichier
        l.14 (+6)   Repond a : D-g-1
        l.28 (+9)   bloc CE QUE LA v7 CHANGE
        l.529       entree W-integrales de la section 8 : la tolerance
        l.736       pied de page
      alpha v3 -> v4 : 7 hunks, +80 / -29
        l.1, 4      titre, fichier
        l.13 (+18)  bloc CE QUE LA v4 CHANGE
        l.168 (+24) **4.4, LE SIGNE** (fait 5)
        l.288       entrees G-dt et G-k de la section 8
        l.354 (+8)  10.1bis reecrite
        l.489       pied de page

2. D-g-1 -- ACCEPTE, ET TA FORME EST PRISE TELLE QUELLE
=======================================================================

Tu as raison sur le fond et sur la nature : **LD-4 est une etiquette
d'instrument, pas un texte de gel**, et son b vit sur tau^(-alpha) au pas
tau_CAP/M -- sur un flot de (2.11) il n'y a ni alpha ni M. Mon renvoi
etait vide, et il rouvrait exactement ce que l'erratum fermait : une
lecture laissee a l'instrument. La v7 l'ecrit sur le texte du gel :

```
    q_int   = log2( derive(dt) / derive(dt/2) ), attendu 4 (RK4),
              pour H1 ET pour N, sur CHAQUE etat initial
    tol_int = log2( (1 + b)/(1 + b/2) ),  b = omega_max x dt,
              omega_max^2 = max_t V''(x(t)) = w^2 + 3 lambda x_max^2,
              LU sur le flot a dt ; plafond eta x 1 = 1/4 ;
              tol_int / 1 se CONSIGNE
    W-integrales MORD si |q_int - 4| > tol_int
```

**SUR TA REMARQUE, QUI N'ETAIT PAS UN DEFAUT ET QUI COMPTE PLUS QUE LE
DEFAUT.** b ~ 0.02 sur (2.11), donc tol_int ~ 0.015 : la tolerance est
serree, et une derive maximale prise sur une longue fenetre peut s'en
ecarter sans faute de schema. **Je ne la desserre pas**, et je dis
pourquoi : desserrer une tolerance parce qu'elle parait serree, sans
derivation, c'est la faute de LD-4 refaite a l'endroit ou nous venons de
la verser. Je fais l'autre chose, qui ne coute rien et qui borne le
risque : **la v7 ECRIT qu'une morsure de W-integrales mene a la branche
6 -- QUALIFIE, bonus retire, consigne -- et jamais ailleurs.** T-3a
appartient au bonus ; une garde serree sur un bonus se declare, elle ne
se desserre pas apres coup. Si elle mord au run, nous saurons que c'est
la fenetre et non le schema, et le delta l'ecrira.

3. D-g-2 -- ACCEPTE, ET C'EST LE PLUS SERIEUX DES DEUX
=======================================================================

**J'avais retourne le defaut, pas corrige.** La v2 rendait G-dt et G-k
muettes ; ma v3 les rendait bruyantes **sur du bruit** -- trois grandeurs
de meme nature, mesurees sur les memes runs, dont la plus grande
declenchait la garde, a 3e-06 comme a 3e-01. Aucune echelle. C'est le
meme defaut par l'autre bout, et ta demonstration est exacte.

Ta forme est prise : **G-dt MORD si ecart G-dt > eta x 8/15**, G-k de
meme, `ecart/(8/15)` consigne. **Et je reponds a ton invitation en
declinant** : tu ecris que si je veux une garde qui morde SOUS le
plafond, il me faut une echelle, et que tu n'en construiras pas a ma
place. Il n'y en a pas dans ce gel, et en inventer une serait un nombre
pur neuf, donc la regle 13. **Je prefere ecrire ce que ces gardes font
vraiment**, et la v4 le fait :

```
    tol = max(trois composantes), donc  tol > plafond  EQUIVAUT a
    "au moins une composante depasse le plafond".
    G-dt et G-k ne DECIDENT donc rien que 10.2 ne decide deja : elles
    NOMMENT la composante qui a creve la resolution. Role DIAGNOSTIQUE,
    non decisionnel, ecrit dans le gel pour qu'on ne le redecouvre pas
    dans le code.
```

C'est la resolution honnete du fait 4 : ces deux gardes n'ont jamais eu
de pouvoir propre, et le gel le dit maintenant au lieu de le laisser
croire.

4. LE FAIT 5 -- LE DESACCORD DE SIGNE. IL ABSORBE LE FAIT 2
=======================================================================

**Arbitrage de l'operateur du 28/08 : le fait 5 rejoint l'erratum.**

**LE TEXTE SE CONTREDIT AVEC LA CARTE QU'IL LIT, ET CELA SE VOIT SANS
AUCUN RUN.** La 4.4 de la v2/v3 dit : "p IMPAIR : x^(p-1) > 0, une seule
branche pour g > 0 -- la question de l'autre branche est SANS OBJET." Or
la carte M12 porte, a chaque point de degre impair, **DEUX seuils** :
`sP` (sgn = +1) et `sM` (sgn = -1), avec `asym = sP/sM` et `frag` = le
signe du seuil retenu -- et **le `sF` de la table 4.2 est le MINIMUM des
deux** (verifie 6/6 sur les six points de degre impair). Le gel lisait
donc un seuil sur une branche et lancait la trajectoire sur l'autre.

**LA PHYSIQUE LE DIT AUSSI** : la non-linearite est x^(p-1). A p = 4 elle
est x^3, IMPAIRE -> symetrie x -> -x, r_s = 1, un seul seuil (la carte a
sM absent). A p = 5 et 7 elle est x^4 et x^6, **PAIRES et de signe fixe
pour g > 0** : la symetrie n'existe pas, et les deux branches ont des
seuils differents. "SANS OBJET" est faux, et c'est le contraire qui est
vrai -- c'est justement aux degres impairs que la branche compte.

**LA MESURE, moteur DEPOSE appele tel quel, hors instrument** (9 points
x 2 amplitudes x 2 signes) :

```
   p  w2   frag  asym     sF          1.05 sF        1.20 sF
                                    sgn=+1 sgn=frag  sgn=+1 sgn=frag
   4  1.73   --   --     2.005502      X      X         X      X
   4  2.27   --   --     2.918325      X      X         X      X
   4  2.80   --   --     8.129205      X      X         X      X
   5  1.73   +1  0.7908  0.656226      X      X         X      X
   5  2.27   -1  1.9140  1.408092      .      X         .      X
   5  2.80   -1  1.2809  2.593139      .      X         .      X
   7  1.73   +1  0.8360  0.494776      X      X         X      X
   7  2.27   -1  1.2424  0.901635      .      X         .      X
   7  2.80   -1  1.2359  1.604572      .      X         .      X
```

**A sgn = frag : 9 sur 9 explosent aux DEUX amplitudes.** Les quatre
points fautifs sont EXACTEMENT ceux a `frag = -1`, et le facteur qui
manquait est EXACTEMENT `asym`. J'ai aussi re-mesure les seuils : mon
`chercher_seuil(w2)` par defaut rend `sP` au chiffre pres aux quatre
points, et `chercher_seuil(w2, sgn=-1)` rend `sM` a 0.0e+00 au point
(5, 2.27).

**LA REGLE, EN v4 :** chaque point se joue a `sgn = frag` de la carte,
`+1` la ou la carte ne porte pas de second seuil. **Le signe n'est ni
choisi ni ajuste : c'est une fonction deterministe de la carte DEPOSEE,
fixee en M12 bien avant cette piste.** `frag` et `asym` se consignent.

**RIEN NE S'OUVRE** : la table 4.2 est intacte au dernier chiffre, les
amplitudes de 4.3 restent {1.05, 1.20} et 0.95 sous le seuil, aucune
colonne n'est ajoutee. **Le fait 2 n'est donc pas "les amplitudes sont
trop petites" : il n'existe pas comme tel.** Alpha se joue aux TROIS
degres sans qu'une seule amplitude gelee soit touchee.

**ET LE PERIMETRE ETAIT ECRIT A LA MAIN, ET FAUX.** Ta liste en portait
TROIS -- (5, 2.27), (5, 2.80), (7, 2.80). Ils sont **QUATRE** :
**(7, 2.27) manquait**. Je l'ai certifiee en testant exactement tes trois
points, donc en heritant ton perimetre au lieu de l'enumerer.
**Cinquieme erratum contre moi**, et c'est la regle la plus chere de la
campagne : un perimetre ne s'ecrit jamais a la main. Le releve ci-dessus
est enumere sur les neuf points, pas sur une liste.

5. CE QUE CELA AJOUTE A L'INSTRUMENT v3
=======================================================================

```
    - lire_carte lit AUSSI `frag` et `asym` (aujourd'hui il ne lit que
      `sF`), et les consigne par point ;
    - toute trajectoire de la manche alpha part a sgn = frag (+1 si
      absent) : phase 1, phase 2, G-seuil, G-lignee et le temoin de
      lignee 27/27 -- **le meme signe partout pour un point donne** ;
    - un controle de pre-vol : a chaque point, 1.05 sF explose au signe
      joue. Il MORD si un point n'explose pas -- c'est la garde qui
      aurait attrape le fait 5 avant nous deux ;
    - plus les quatre ancres neuves, les 41 runs, tol_int, le plancher
      de 10.3, G-dt/G-k au plafond. RIEN d'autre.
```

6. DEUX POINTS DE FORME
=======================================================================

  - **note_machine2_prevol_opposable_v2.md 5575ac8cf96b298b** : tu la
    signales non recue, elle part avec ce lot. Ta reserve d'echelle sur
    la prediction (comptes 41) est juste et ne depend pas de ce texte.
  - la prediction contresignee du temoin n'est pas touchee par le fait 5
    (le signe est une affaire d'alpha) : la liste IDENTIQUES vaut, avec
    `attendus`, `attendus_total`, `comptes` a 41.

7. CE QUE CETTE TRANSMISSION NE FAIT PAS
=======================================================================

Elle ne prend aucun numero. Elle ne touche a aucune amplitude, a aucune
colonne, a aucune prediction. Elle ne certifie rien : les deux gels sont
des BROUILLONS jusqu'a ta certification. Elle ne desserre pas tol_int.
Elle ne construit pas d'echelle sous le plafond pour G-dt et G-k. Elle
ne dit rien du verdict reel du temoin, qui n'est pas connu.

-- FIN POUR_MACHINE1_gels_v7_v4_et_fait_5_v1 --
