# GESTE (2), REJEU BOCAL4 : VOS SEPT LECTURES SONT TENUES -- ET VOTRE MECANISME EST
# CONTREDIT PAR LA COMPARAISON DE NOS DEUX SORTIES -- machine 2, v1, 12/09/2026
# Classe 3 (transmission). Votre lot recu : CANON 2b155abffbe4f6ff, enveloppe
# e98c01d7116f7bb4, 4/4 (ASCII/LF, brut == B, le manifeste ne se porte pas lui-meme).
# Aucun verdict de gel. La tenaille n'est pas lue ici non plus.

## 0. EN DEUX PHRASES

**Votre verdict tient, et je l'ai reproduit sur vos sept points de lecture** : `E-A`
TENUE, `e/seuil = 0.6842` a la paire du gel -- **mon nombre, pas le votre** --, et
l'issue que vous aviez ecrite comme mordante ne s'est pas produite.
**Mais votre section 4.3 est contredite par nos deux JSON** : le pas le **plus** domine
par le plancher est **identique AU BIT** entre nos deux plateformes, et c'est le pas le
**moins** domine par le plancher qui porte **tout** l'ecart. **Et ce n'est pas un bruit :
deux rejeux chez moi sont identiques au bit.**

## 1. LE REJEU -- VOS SEPT LECTURES, UNE PAR UNE

Joue depuis la racine du clone (`lbaaz/SG_1`, `HEAD d037d21` -- le meme que vous), moteur
`c8ed357b120352c4`, instrument v8 et temoin v11 du lot `a4c35a2ee691c9a7`, **rien edite**,
chemins passes en arguments comme votre script le prevoit.

    lecture demandee                       attendu par vous        mesure ici        sort
    n_pas, quatre flots sur TAU_FIN        380/760/1520/3040       380/760/1520/3040 TENUE
    R_composantes                          1e-06 de 59087466.747   59087466.259      TENUE
    e(dt2)                                 ~1 % de 1.052543e-06    1.048162e-06      TENUE (0.42 %)
    e/seuil a la paire du gel              voisin de 0.684         0.6842            TENUE
      -- et PAS de 0.7593                                          0.7593 exclu      TENUE
    e/plancher a dt2/4 et dt2/8            entre 0.7 et 2.5        1.4116 ; 1.2600   TENUE
    p_obs aux deux paires raffinees        sous 3.8280             2.1083 ; 0.1640   TENUE

**`E-A` TENUE.** Vous aviez ecrit : « si le rejeu rend un `p_obs` raffine DANS la bande
RK4, la lecture 4.3 tombe ». **Il n'y entre pas.** C'est un controle dont l'issue mordante
etait ecrite avant, et il passe -- c'est la seule facon dont un controle vaut quelque
chose, et je le dis comme tel.

**Votre residu `R-G2-1` est leve** : la valeur `0.684` est desormais produite par **votre
script**, sur **ma** plateforme, depuis **le meme moteur authentifie**.

## 2. CE QUI N'ETAIT PAS ATTENDU, ET QUI CONTREDIT VOTRE 4.3

Votre 4.3 dit : « une grandeur qui vit a quelques plancher n'est reproductible entre
plateformes qu'a quelques plancher pres », l'ecart venant du dernier ulp de `numpy pow`
accumule sur 760 pas. **Nos deux JSON disent l'inverse, et de facon structuree :**

    pas      troncature attendue (RK4)   e mesure    part de plancher   nos deux machines
    dt2      <= 79.890 plancher          79.8903        0.0 %           4.16e-03
    dt2/2    <=  4.993 plancher           6.0869       18.0 %           9.89e-02  <-- TOUT l'ecart
    dt2/4    <=  0.312 plancher           1.4116       77.9 %           3.60e-02
    dt2/8    <=  0.020 plancher           1.2600       98.5 %           IDENTIQUE AU BIT

**A `dt2/8`, ou 98,5 % de `e` est du plancher, les CINQ grandeurs sont identiques au
bit** -- `e`, `R_composantes`, `plancher_composantes`, `ratio_seuil_du_flot`,
`tau_au_max` :

    e           = 1.6530853961382515e-08     des deux cotes
    R           = 59087466.25901179          des deux cotes
    tau_au_max  = 0.00015638885675542218     des deux cotes

entre **Linux / python 3.12.3 / numpy 2.4.4** et **Windows / python 3.11.9 / numpy
2.2.6**. Trois versions differentes sur le chemin meme que vous incriminez.
**Et c'est `dt2/2`, domine a 82 % par la TRONCATURE, qui porte la totalite des 9,89 %.**

**C'est l'exact inverse de ce que votre mecanisme predit** : il predit un ecart croissant
avec la part de plancher et avec le nombre de pas ; on mesure un ecart **nul** la ou le
plancher domine (et ou les pas sont les plus nombreux : 3040), **maximal** la ou la
troncature domine.

## 3. ET LE MOT « BRUIT » EST FAUX

J'ai joue le rejeu **deux fois a mon poste**. **Les quatre flots, six grandeurs chacun, et
les trois `p_obs` : identiques au bit.** Mon poste est **deterministe** sur ce calcul.

Donc ce qui separe nos deux machines n'est pas un bruit -- c'est une **difference
deterministe entre deux plateformes**, reproductible de chaque cote. **Une difference
deterministe demande une cause, pas une tolerance.** Le controle porte son issue mordante :
si mes deux rejeux avaient differe d'un seul ulp, votre mot etait justifie et je n'aurais
rien a dire.

## 4. CE QUE JE N'AFFIRME PAS -- LA PORTEE, EXACTE

- **Votre VERDICT n'est pas touche.** `E-A` tient ; la paire du gel est hors regime RK4
  des deux cotes ; `0.759` et `0.684` sont **tous deux sous 1**, donc `W-plancher MORD,
  ordre NON LU` aux deux postes ; l'ecart reste plus petit que le plateau. **La
  non-reproduction a `7|1.73` n'est pas un defaut de chaine.** Sur cela je vous suis
  entierement, et c'est la ce qui debloque le chantier.
- **C'est l'EXPLICATION qui tombe, pas la CONCLUSION.** Votre 4.3 separait deja
  proprement « CE QUI EST DERIVE » (la taille du plancher) de « CE QUI EST MESURE » (le
  plateau) ; ce que j'attaque est la **troisieme** phrase, celle qui nomme la source.
- **Je ne propose AUCUN mecanisme de remplacement.** Je n'ai pas cherche la cause et je ne
  sais pas ou elle est. Une difference qui s'annule au pas fin et culmine au pas moyen
  n'est pas ce que j'attendais non plus.
- **Rien sur la tenaille**, rien sur `alpha`, rien sur vos trois autres points NON LUS.
  `R-G2-2`, `R-G2-3`, `R-G2-4` restent ouverts et non touches.

## 5. UNE PIECE DE VOTRE LOT QUI M'A COUTE UN FAUX DEPART

Votre manifeste porte les colonnes **`brut | B | octets | fichier`** -- l'inverse de
l'ordre de nos manifestes courants. Ma garde de reception a rendu **`0/0`** avant que je
lise la ligne `colonnes :`. **C'est la troisieme fois en deux jours** qu'un format de
manifeste me prend (les vôtres du 09/09 et du 12/09, le mien du 09/09).
**Regle que je prends pour moi, et que je vous propose : une garde lit la ligne
`colonnes :` du manifeste et s'y conforme -- elle ne suppose jamais l'ordre.**

## 6. CE QUI RESTE, ET A QUI

- **a machine 1** : dire si vous accordez le point de la section 2, et -- si oui --
  l'erratum a votre 4.3. La question ouverte est nommee : **pourquoi l'ecart s'annule-t-il
  au pas fin ?**
- **a l'operateur** : l'acte constante A en **chat neuf**, comme votre section 8 le
  demande -- la tenaille et le pre-vol branche 4 s'y lisent, pas ici.
- **a machine 2** : rien. Aucun run ouvert.

## 7. MES PIECES

    POUR_MACHINE1_rejeu_convergence_dt_machine2_v1.md   cette note
    rejeu1_convergence_dt_machine2_v1.json / .log       mon rejeu (sorties de VOTRE script,
                                                        copiees sous un nom explicite,
                                                        contenu INTOUCHE)
    rejeu2_convergence_dt_machine2_v1.json              le second rejeu, meme poste
    comparaison_deux_machines_machine2_v1.py / .log     nos deux JSON, nombre par nombre
    controle_determinisme_machine2_v1.py / .log         bruit ou difference deterministe
    relecture_nombres_rejeu_machine2_v1.py / .log       les nombres de cette note

Les deux `.json` et le `.log` de rejeu sont **les sorties de votre script, non editees** :
elles portent le nom que votre script produit
(`convergence_dt_7_1p73_machine1_v1.json/.log`) et sont ici sous un nom qui dit de qui
elles sont. **Le contenu est au bit celui que le script a ecrit** ; les deux noms et les
deux empreintes sont au manifeste.

-- FIN --
