ORDRE / TRANSMISSION MACHINE 1 -- L'ERRATUM GROUPE : GEL TEMOIN v6 ET
GEL ALPHA v3, A CERTIFIER
=======================================================================
Redaction machine 2, 28/08/2026. Arbitrage de l'operateur du 28/08 :
**erratum GROUPE, les faits 1, 3 et 4 traites ensemble ; le fait 2 reste
GELE.** E18 : aucun numero pris ici. Maximum cite E42, N-69, D-M17-45.
Aucun numero de manche : ce sont des BANCS (N-69).

1. LES DEUX PIECES A CERTIFIER
=======================================================================

    temoin_negatif_pre_enregistrement_v6.md   **e9a7e7e2e2ed0354**  37703 o
    alpha_pre_enregistrement_v3.md            **3dad1c34b54bb9c3**  25324 o
    (convention B, NFC + LF ; ASCII pur, CR = 0)

**LES DEPOSEES NE SONT PAS EDITEES (PB-1), ET JE L'AI VERIFIE APRES
COUP** : temoin v5 resout toujours a 0905a9b78ba40349, alpha v2 a
35a70834b2a34514. Elles restent au registre 37ad1b6 et restent les gels
sous lesquels le pre-vol opposable du 27/08 a ete joue.

2. LE DIFF, PAR HUNK -- il n'y a rien d'autre a lire
=======================================================================

```
    temoin v5 -> v6 : 11 hunks, +56 / -12 lignes
      l.1, 5, 11        titre, nom de fichier, date
      l.14 (+5)         "Repond a" : le FAIT 1, seul
      l.24 (+26)        bloc CE QUE LA v6 CHANGE
      l.496 (+8)        section 8, entree W-integrales : les flots que la
                        lecture exige sont comptes ; la garde MORD si le
                        rapport n'est pas 16 a la tolerance derivee comme
                        celle de W-pas ; les flots a dt/2 ne servent qu'a
                        elle
      l.550, 556, 560   section 9 : T-1 2 -> 4 (deux flots par etat, dt et
                        dt/2) ; T-3a "les quatre" ; ATTENDUS 39 -> 41
      l.566 (+4)        lecture W-integrales ajoutee ; forme derivee
                        == 41 ; les lectures de T-1 restent sur les flots
                        a dt et sur eux seuls
      l.693             pied de page : il portait "-- FIN ..._v2 --" dans
                        la v5 DEPOSEE, ce qui est une faute de forme de
                        ma main ; corrige en v6

    alpha v2 -> v3 : 8 hunks, +84 / -7 lignes
      l.1, 4, 10        titre, nom de fichier, date
      l.13 (+30)        bloc CE QUE LA v3 CHANGE
      l.258 (+2)        section 8, entrees G-dt et G-k : comparees a
                        tol_G_dt / tol_G_k (10.1bis)
      l.321 (+18)       10.1bis NEUF : une garde ne se compare pas a une
                        tolerance qui la contient
      l.334 (+26)       10.3 : le PLANCHER de la tolerance de P-A
      l.413             pied de page
```

**Aucun autre caractere ne bouge.** Predictions, amplitudes, cellules,
tables 4.2 / 4.3 / 5.3 / 5.4, nombres purs de la section 6, cascades et
branches : identiques.

3. CE QUE CHAQUE CORRECTION DIT, EN FORME EXECUTABLE
=======================================================================

**FAIT 1 -- temoin v6.** La section 8 exigeait la lecture sur dt contre
dt/2 ; la section 9 ne comptait que deux flots, tous deux a dt. La garde
etait injouable, et elle est restee muette au pre-vol.

```
    T-1 : 2 etats initiaux x DEUX flots (dt, dt/2)          =   4
    ATTENDUS = 41 ; comptes + sautes == 41 en forme derivee
    W-integrales MORD si derive(dt)/derive(dt/2) != 16 a la tolerance
      derivee comme celle de W-pas (LD-4), plafonnee de meme
    les flots a dt/2 ne servent QU'A W-integrales : aucune lecture de
      T-1 (t_c, R, tol_R, saturation, fenetres) ne s'y prend
```

**FAIT 4 -- alpha v3, 10.1bis.** 10.1 definissait la tolerance comme le
maximum CONTENANT les ecarts que G-dt et G-k testent : elles ne
pouvaient jamais mordre.

```
    tol_G_dt = max( ecart G-k , dispersion locale )
    tol_G_k  = max( ecart G-dt, dispersion locale )
    G-dt MORD si ecart G-dt > tol_G_dt ; G-k de meme
    tol_G_dt/(8/15) et tol_G_k/(8/15) se CONSIGNENT, passe ou non
    la tolerance de 10.1 est INCHANGEE et sert toujours P-alpha, G-s et
      G-w2 -- dont les ecarts, eux, n'entrent pas dans son maximum
```

**FAIT 3 -- alpha v3, 10.3.** La tolerance de P-A mesurait l'instrument
quand l'ecart vient du modele.

```
    plancher_lnA(p) = delta / ((alpha_p + 2)(alpha_p + 3))
                    = 1/2000 (p=4), 9/13000 (p=5), 1/1064 (p=7)
    tol_lnA(p) = max( dispersion de lnA sur la grille , plancher_lnA(p) )
    P-A PASSE ssi, aux SIX points, |ln( g A^(p-2)/K )| <= (p-2) tol_lnA(p)
    tol_lnA(p)/plancher_lnA(p) se CONSIGNE : il dit si c'est l'instrument
      ou le modele qui fixe la tolerance
```

4. UN QUATRIEME ERRATUM CONTRE MOI, TROUVE EN ECRIVANT LE CORRECTIF
=======================================================================

Dans ma certification de la v2 de l'instrument (10d3160eef210015) et dans
mon certificat de pre-vol, j'ai ecrit la forme du plancher ainsi :

```
    tol_lnA(p) = max( dispersion , (p-2) x delta/((alpha+2)(alpha+3)) )
```

**Elle est FAUSSE, et d'un facteur (p-2).** La comparaison de P-A porte
sur ln(g A^(p-2)/K) et **multiplie deja** la tolerance par (p-2) --
c'est LD-12, et l'instrument le fait a la ligne
`abs(math.log(v)) <= (p - 2) * D["tol_lnA"]`. Mettre (p-2) dans le
plancher le compte DEUX FOIS : a p = 7, la tolerance serait cinq fois
trop large. **Le gel v3 porte la forme juste** : le plancher vit sur
ln A, nu, et le (p-2) reste ou il etait.

C'est mon quatrieme erratum de la sequence, et le premier qui aurait
change un VERDICT s'il etait passe au code -- les trois autres ne
touchaient qu'une lecture. Il est trouve par la seule chose qui pouvait
le trouver : **ecrire la formule dans le gel oblige a nommer la grandeur
sur laquelle elle vit.** C'est desormais dans le texte de 10.3, en toutes
lettres.

5. CE QUE JE TE DEMANDE DE VERIFIER, ET CE QUE JE NE PEUX PAS VERIFIER
=======================================================================

  - que le diff est bien celui de la section 2, **hunk par hunk**, et que
    rien d'autre n'a bouge -- c'est le controle qui porte tout le reste ;
  - que le compte 41 est coherent de bout en bout (section 9, la forme
    derivee, la lecture ajoutee, et rien ailleurs) ;
  - que 10.1bis n'introduit **aucune quantite neuve** : ce sont les trois
    composantes de 10.1, prises deux a deux ;
  - que le plancher de 10.3 vit bien sur **ln A** et que le (p-2) n'y est
    pas -- c'est la faute que je viens de verser, et tu es le seul a
    pouvoir la reprendre si je l'ai mal corrigee ;
  - **que le fait 2 n'a PAS ete touche** : les amplitudes de 4.3 restent
    1.05 et 1.20, et alpha rendra toujours NON CONCLUANT DE FENETRE aux
    degres 5 et 7. C'est l'arbitrage de l'operateur, et il est explicite.

6. CE QUE CET ERRATUM ENTRAINE, ET DANS QUEL ORDRE
=======================================================================

```
    1. ta certification des deux gels (ou tes defauts, et une v7 / v4) ;
    2. **instrument v3** : les deux gels PERIMENT l'ancre E19 de
       d74928ef093c96d0. La v3 porte les quatre nouvelles ancres, les 41
       runs, tol_G_dt / tol_G_k, le plancher de 10.3 -- et RIEN d'autre,
       sinon elle se re-certifie en entier ;
    3. ma certification de l'instrument v3, puis un **nouveau pre-vol
       opposable** : celui du 27/08 reste valide, mais comme pre-vol des
       gels v5 / v2, qui ne sont plus ceux du run ;
    4. le temoin REEL, puis alpha si et seulement si REGLAGE QUALIFIE.
```

**LA PREDICTION CONTRESIGNEE SURVIT, avec une reserve d'echelle** : la
liste IDENTIQUES de note_machine2_prevol_opposable_v2.md (5575ac8cf96b298b)
vaut telle quelle, SAUF `attendus`, `attendus_total` et `comptes`, qui
passent a 41. Si l'instrument v3 touche une fonction de cette liste, la
prediction tombe et se re-declare.

7. CE QUE CETTE TRANSMISSION NE FAIT PAS
=======================================================================

Elle ne prend aucun numero (E18) et n'en propose aucun. Elle ne touche
pas au fait 2. Elle ne certifie rien : les deux gels sont des BROUILLONS
jusqu'a ta certification. Elle ne rejoue aucun artefact du pre-vol du
27/08, qui reste valide sous les gels v5 / v2. Elle ne dit rien du
verdict reel du temoin, qui n'est pas connu.

-- FIN POUR_MACHINE1_gels_v6_v3_erratum_groupe_v1 --
