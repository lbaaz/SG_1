# LA VERIFICATION alpha -- RUN REEL, CERTIFICAT D'EXECUTION
# Machine 2, 28/08/2026. Sur ordre de l'operateur, porte ouverte par le
# temoin REEL (644240dc894c2733, REGLAGE QUALIFIE).
# Instrument : banc_qualification_machine1_v3.py  5fae2a8c94cf8685
#              CERTIFIE, contresigne, DEPOSE avant les runs (e800c71).
# Gels       : alpha v5 045c2435aaf623ce ; temoin v7 8b083e9f109b5a8e
#              (registre 0485001) ; moteur c8ed357b120352c4.
# Files      : E18, aucun numero pris ; maximum cite E42, N-69, D-M17-45.

VERDICT : **VERIFIE -- branche 5 : P-alpha les six par degre ET P-A aux
          TROIS degres.**  116.2 s.

          **alpha = 4/(p-2) = 4 u_p EST VERIFIE AUX TROIS DEGRES.**
          Et il faut lire la suite avant de s'en rejouir : **P-A ne
          passe que par le PLANCHER introduit cette semaine** (section 3).

RESUME -- DIX LIGNES

```
    1  verdict VERIFIE, branche 5, 116.2 s ; comptes 90 + 0 == 90
    2  p = 4 : six alpha entre 1.999823 et 1.999828   (attendu 2)
    3  p = 5 : six alpha entre 1.333138 et 1.333186   (attendu 4/3)
    4  p = 7 : six alpha entre 0.799209 et 0.799956   (attendu 4/5)
    5  ecart max a 4/(p-2) : 1.77e-04, 1.95e-04, 7.91e-04 -- sous
       tolerance aux dix-huit points
    6  la separation 8/15 est resolue par un facteur 2357, 2220, 441
    7  P-A vrai aux trois degres, MAIS tol_lnA == plancher aux trois :
       sans le plancher, P-A echouait aux trois
    8  les DIX-HUIT rapports g A^(p-2)/K sont > 1, du meme cote
    9  G-lignee 27/27 : le lien au moteur depose est etabli, au bit
   10  seize gardes sur seize demontrees ; MANIFEST verifie ; statut REEL
```

## 1. CE QUI EST MESURE

```
    p = 4        p = 5        p = 7          (six points par degre :
    1.999824     1.333186     0.799702        3 colonnes x 2 amplitudes)
    1.999828     1.333149     0.799209
    1.999823     1.333138     0.799766
    1.999825     1.333147     0.799956
    1.999825     1.333159     0.799912
    1.999827     1.333155     0.799792
    ---------    ---------    ---------
    2            4/3          4/5            attendus, exacts
    ecart max    1.77e-04     1.95e-04     7.91e-04
    tolerance    2.26e-04     2.40e-04     1.21e-03   (derivee, 10.1)
```

**Aucune moyenne n'est prise** : les six alpha de chaque degre sont sous
tolerance CHACUN (D-alpha-8). Les gardes G-dt, G-k, G-s et G-w2 sont
toutes muettes, avec leurs ecarts consignes -- au plus 4.2e-05 fois 8/15.

**CE QUI FAIT DE CE RESULTAT UNE LOI ET NON UN NOMBRE.** alpha = 4/(p-2)
est une loi EN p ; jouee a un seul degre, elle ne teste qu'un exposant.
Ici les trois exposants predits sont separes de 8/15 = 0.533, et la
mesure les resout **par un facteur 2357, 2220 et 441**. Les trois valeurs
tombent chacune sur la sienne. **C'est le degre qui varie, et la
prediction suit.**

## 2. LA LIGNEE, ET CE QU'ELLE VAUT

**G-lignee 27/27.** Les trajectoires de cette manche sont celles du
moteur DEPOSE, au bit : meme booleen d'explosion et meme indice de pas,
aux 27 points, **au signe joue de chaque point**. Ce n'est pas un detail
de forme : sans elle, la manche mesurerait un exposant sur des
trajectoires qui ne sont pas celles de la campagne.

Et cette lignee-la n'aurait pas ete possible avant le fait 5 : quatre
des neuf points partaient sur la branche opposee a leur propre seuil.

## 3. CE QUI DOIT ETRE DIT AVANT TOUT COMMENTAIRE : P-A PASSE PAR LE
##    PLANCHER, ET SANS LUI IL ECHOUAIT AUX TROIS DEGRES

```
    p    dispersion_lnA   plancher_lnA   tol_lnA retenue   qui domine
    4      1.977e-06        5.000e-04      5.000e-04      LE PLANCHER
    5      2.394e-06        6.923e-04      6.923e-04      LE PLANCHER
    7      7.432e-06        9.398e-04      9.398e-04      LE PLANCHER

    ecart max |ln(g A^(p-2)/K)|   contre (p-2) x tol_lnA
    p = 4     2.263e-04      <     1.000e-03      (23 pour cent de la borne)
    p = 5     3.635e-04      <     2.077e-03      (18 pour cent)
    p = 7     1.584e-03      <     4.699e-03      (34 pour cent)
    sans le plancher (dispersion seule) : ECHEC aux TROIS degres.
```

**Le plancher est porteur, aux trois degres, et il a ete introduit cette
semaine** (gel alpha v5, 10.3, fait 3). Quiconque veut attaquer ce
resultat attaquera la, et il aura raison de le faire. Voici ce que je
peux opposer, et rien de plus :

  - **le plancher n'est pas ajuste sur la mesure** : il vaut
    `delta/((alpha_p+2)(alpha_p+3))`, il est ecrit en toutes lettres dans
    la section 6 du gel **depuis la v2** (D-alpha-9), et il a ete pose
    dans 10.3 le 28/08 **avant** ce run, dans un gel certifie et depose ;
  - **l'ecart mesure n'est pas au bord de la borne** : il en fait 18 a
    34 pour cent. Une tolerance taillee pour faire passer serait serree
    au bord ; celle-ci ne l'est pas ;
  - **et le biais a un SIGNE** : les **dix-huit** rapports
    g A^(p-2)/K sont **superieurs a 1**, aucun en dessous. Un bruit de
    mesure ne choisit pas son cote dix-huit fois. Un terme neglige, si.
    C'est la signature attendue de D-alpha-9, et c'est le seul element
    qui distingue "compatible avec la borne" de "sous une tolerance
    large".

**DONC, EN TOUTE RIGUEUR : P-alpha est MESURE ; P-A est COMPATIBLE.**
La constante n'est pas mesuree a la precision de l'instrument -- elle ne
peut pas l'etre tant que la fenetre porte le terme neglige. Le dire
autrement serait mentir par omission.

## 4. CE QUE CE RUN DOIT A L'ERRATUM DE LA SEMAINE -- ET C'EST A CHARGE
##    AUTANT QU'A DECHARGE

```
    sans le FAIT 5 (le signe)   : quatre points sur neuf partaient sur la
      mauvaise branche -> degres 5 et 7 NON CONCLUANTS DE FENETRE, et la
      loi en p n'etait pas testee du tout
    sans le FAIT 3 (le plancher): P-A echouait aux trois degres -> verdict
      PARTIEL, par construction et non par la physique
    sans le FAIT 1 (W-integrales) : la garde restait muette, et le temoin
      rendait un QUALIFIE dont une garde n'avait jamais pu mordre
```

Trois corrections faites **avant** les runs, sur des gels certifies et
deposes, chacune derivee d'une incoherence de TEXTE lisible sans aucune
mesure. Mais il faut l'ecrire dans l'autre sens aussi : **ce verdict
depend de trois corrections que nous avons faites nous-memes, la semaine
ou nous l'avons obtenu.** Les trois sont documentees, datees, certifiees
par l'autre machine et publiques au registre avant les runs. C'est la
seule chose qui separe une correction d'un ajustement.

## 5. CE QUE CE RUN NE DIT PAS

  - **il ne dit rien de la classe ponctuelle** refutee en M12 (11/11) :
    il teste le PROFIL D'EXPLOSION, pas la loi de seuil ;
  - **il ne mesure pas la constante** (section 3) ;
  - il ne joue aucune colonne hors des trois de 4.2, aucun degre hors de
    4/5/7, aucune amplitude hors de {0.95, 1.05, 1.20} ;
  - il ne joue, a chaque point, que la branche de son propre seuil : la
    branche opposee n'est pas jouee, et la parite ne la restitue qu'a
    p = 4 ;
  - il ne dit rien de la fidelite de la transcription de Damour-Smilga :
    elle ne repose que sur moi, la double transcription reste due ;
  - il ne prend aucun numero.

## 6. PIECES (convention B, NFC + LF)

```
    out_banc/alpha/
      resultats_alpha.json   6d7d23130e9322f8   107686 o   statut REEL
      journal_alpha.txt      c30d8e6442bd934d    27619 o
      MANIFEST.sha256        932fe5bcd181b127     6750 o  (65 fichiers, verifie)
      + 63 series alpha_serie_*.txt
    out_banc/temoin/resultats_temoin.json  644240dc894c2733  (la porte)
    instrument 5fae2a8c94cf8685 ; gels 045c2435aaf623ce / 8b083e9f109b5a8e
```

## 7. LA SUITE

```
    1. la contresignature de machine 1 sur ce run et sur la section 3 ;
    2. l'acte de registre (plume machine 1) : les deux runs, l'erratum
       groupe, les cinq faits, les D, les E, LD-1..LD-16, N-61 ;
    3. le depot des deux runs avec l'acte.
    Rien n'est acquis a la campagne tant que l'acte n'est pas depose.
```

-- FIN note_machine2_run_alpha_reel_v1 --
