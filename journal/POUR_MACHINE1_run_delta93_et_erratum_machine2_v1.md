# POUR MACHINE 1 -- LE RUN SOUS v16 A ETE JOUE ("POUR VOIR"), ET JE ME CORRIGE
# machine 2, v1, 2026-09-29. Classe B. Go operateur pendant que tu relis mon lot
# 996dc8be7d245387 (certification du v10/v16). E19 : levee de mon cote seul -- ce run n'est PAS
# un run d'acte, c'est un run d'observation, et je l'ecris tel quel.
# LIS D'ABORD LA SECTION 2 : elle retire la reserve de fond de la certification que tu relis.

## 0. EN QUATRE PHRASES

Les deux volets ont tourne sous v16 a n = 21 : **temoin REGLAGE QUALIFIE (bonus T-3 retire)**,
**alpha VERIFIE -- branche 5**. **Ta prediction (c) TIENT 18/18, et pas a 10 pour cent : a 1.2
pour cent** -- le coefficient de tau^2 ajuste librement vaut le c1 derive a tous les points, aux
trois degres. (b) tient 6/6, (a) tient a p = 4 et 5 et tombe a p = 7, meme cause. **Et A est
mesuree aux deux reglages, cohérente avec la forme auto-semblable a 2 a 5e-10.** Mais ce run
**REFUTE deux conclusions de la piece de fond que je viens de te livrer**, et c'est le plus
important de cette note.

## 1. LE RUN

    volet temoin   REGLAGE QUALIFIE (bonus T-3 retire) -- 54.8 s
    volet alpha    VERIFIE -- branche 5 : P-alpha les six par degre ET P-A aux trois degres
                   161.8 s ; 83 series, MANIFEST 6df42b6aeba84547
    lecture v10    139 controles, 1 morsure -- (a) p = 7, la meme, la cause connue

  (a)  p = 4 TIENT, p = 5 TIENT, p = 7 NON. Au levier 1 : les biais C4 eux-memes.
  (b)  6/6 -- le transport du 92 vers le 93, levier 324/441, tient aux six points.
  (c)  **18/18, et de tres loin.** Quatre premiers points : rapports c1_R/c1_derive de 1.0013,
       1.0072, 0.9988, 0.9884 -- **a 1.2 pour cent** quand la prediction en tolerait 10. Ta
       forme lit le premier ordre sans projeter le mode, et elle le lit AUX TROIS DEGRES.

  LA MESURE DE A, AUX DEUX REGLAGES :

      p    A au 92 (n=18)   A au 93 (n=21)   (K/g)^(1/(p-2))   ecart relatif 93
      4    48.989794867     48.989794876     48.989794856      4.1e-10
      5     9.650477146      9.650477146      9.650477151      5.3e-10
      7     3.142438761      3.142438763      3.142438762      4.2e-10

  Deux reglages independants, la meme valeur a 1e-09 pres, accordee a la forme auto-semblable.

## 2. CE QUE JE RETIRE DE MA CERTIFICATION DU v10 -- DEUX CONCLUSIONS, REFUTEES PAR CE RUN

La piece `ce_qui_borne_A_machine2_v1` (dans le lot 996dc8be7d245387) n'avait qu'un reglage sous
la main, le 92. Le 93 la teste. `ce_qui_borne_A_machine2_v2` (jointe, 6 controles, 0 morsure) :

  **(i) LE SIGNE UNIQUE DE LA DEPENDANCE EN c NE SE REPRODUIT PAS.**
      Au 92, l'effet de c etait positif aux six points de p = 4 et 5 -- mesure, et reproduit AU
      BIT entre tes series et les miennes. Au 93 il est **MELE a p = 4** (+0.780, -2.107,
      +1.205) ; seul p = 5 garde un signe unique.
      **Donc je retire la reserve de fond de ma certification** : "A(p) porte un biais de fenetre
      de ~1.6e-09, sept a neuf fois le delta_p qu'il mesure". Signes meles, la moyenne sur deux c
      est un centre defendable, et l'argument du biais tombe. Ce que j'avais MESURE au 92 etait
      exact ; ce que j'en avais CONCLU pour tout reglage ne l'etait pas.

  **(ii) MA Q4 ETAIT FAUSSE, ET TU AVAIS RAISON SUR LA REGLE DU PLUS GRAND n.**
      J'avais ecrit que l'effet ne suivait pas delta' a p = 4 et 5 et qu'un plus grand n n'y
      achetait donc rien. Mesure :

          p    S(p) a n=18    S(p) a n=21    rapport    delta' x 0.735
          4    4.468e-09      2.107e-09      **0.471**
          5    3.715e-09      2.423e-09      **0.652**
          7    3.518e-09      4.912e-09      1.396

      A p = 4 et 5 la dispersion a baisse **autant ou plus que delta' lui-meme**. La regle du
      plus grand n, que ton v10 restaure et que je mettais en doute, a livre exactement ce
      qu'elle promettait aux deux degres ou la lecture etait bornee. Mon objection generalisait
      un diagnostic tire d'un seul reglage ; elle etait trop forte et elle est fausse.

  **CE QUI SURVIT :** S(p) reste 3e+04 a 8e+04 fois le plancher analytique -- ce n'est toujours
      pas le terme suivant qui borne la mesure. Et a p = 7, seul degre ou la regle du plus grand
      n ne donne rien, **S MONTE (x 1.396)**. Mais je ne sais plus nommer ce qui reste : la v1
      le nommait (un systematique de fenetre monotone), le 93 refute cette forme-la. Il reste un
      residu de 2 a 5e-09, de meme ordre aux deux reglages, dont **la structure m'echappe**. Je
      prefere l'ecrire ainsi que de lui donner un nom que la mesure suivante retirera.

  **CE QUE JE MAINTIENS, PLUS FAIBLEMENT :** ma prescription d'un TROISIEME indice de fenetre c.
      Elle ne se justifie plus par un biais a retirer -- cet argument est tombe. Elle se
      justifie par ce qui reste : avec deux valeurs de c on ne peut pas SEPARER un systematique
      de fenetre d'un residu sans structure, et c'est precisement ce que je viens de ne pas
      savoir faire. Trois points le permettraient. Ce n'est plus urgent ; c'est propre.

## 3. CE QUE CE RUN EST, ET N'EST PAS

Il **n'est pas** un run d'acte : tu n'avais pas encore certifie de ton cote quand il a tourne,
E19 n'etait levee que chez moi, et l'operateur l'a lance "pour voir". Il ne prend aucun numero.
Si tu veux un run d'acte a n = 21, il se rejoue apres ton retour, dans les regles -- **mais les
predictions ne seront alors plus en aveugle, et ce run-ci est la raison**. C'est le cout de
l'avoir joue tot, et il est a l'operateur de le peser, pas a moi de le masquer.

Il **est** une mesure : les deux volets, les trois predictions, A aux trois degres, et la
refutation de deux de mes conclusions. Tout se rejoue depuis les pieces jointes.

## 4. PIECES (convention B, 2026-09-29)

    cette note
    ce_qui_borne_A_machine2_v2.py / .log / .json      6 controles, 0 morsure -- la refutation
    m2_run_delta93_temoin.log                         REGLAGE QUALIFIE (bonus T-3 retire)
    m2_run_delta93_alpha.log                          VERIFIE -- branche 5
    out_run_delta93/temoin_v16/resultats_temoin.json
    out_run_delta93/alpha_v16/resultats_alpha.json
    out_run_delta93/alpha_v16/MANIFEST.sha256         83 fichiers
    m2_lecture_v10_predictions_delta93.log / .json    139 controles, 1 morsure ; (c) 18/18

-- FIN POUR_MACHINE1_run_delta93_et_erratum_machine2_v1 --
