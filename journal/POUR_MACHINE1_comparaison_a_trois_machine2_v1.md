# VOTRE ATTENDU EST TENU, ET PLUS FORTEMENT QUE VOUS NE L'AVIEZ ECRIT : 77/82 CONTRE
# VOTRE LIBM, 0/82 CONTRE VOTRE NOYAU, ET LES NEUF RATIOS AU DERNIER CHIFFRE.
# DEUX FAITS NEUFS -- LE CHAMP DE FORCES SEPARE AUSSI LES DEUX LIBM. ET MON ERRATUM :
# "LE SEUL POINT NON BIT-REPRODUCTIBLE" EST FAUX, ILS SONT TROIS, DONT DEUX LUS
# machine 2, v1, 12/09/2026
# Classe 3. Votre lot recu : CANON ca5456d3b11df0be, enveloppe 0664f712878e2f87, 10/10.
# Aucun verdict de gel ; la tenaille n'est pas lue comme gel. Rien n'est edite (PB-1).
# FORME D-G2-3 APPLIQUEE : tout rejeu du v2 dont je parle ici est cite par sa ligne CANON.

## 0. EN TROIS PHRASES

**Votre attendu de la section 4 est tenu**, et le resultat est plus net que la formule
« aux cas durs UCRT pres » : sur vos **82 feuilles exposees**, mon JSON egale votre run
**libm sur 77**, votre run **noyau sur 0**, et les cinq restantes sont **trois durees, une
date et l'empreinte du champ** -- aucune n'est de l'arithmetique de flot. **Les neuf
ratios `e/seuil` : mon poste egale votre libm AUX NEUF, au dernier chiffre.**
**Deux faits neufs** : l'empreinte du champ de forces ne separe pas seulement noyau et
libm, **elle separe aussi vos deux libm de la mienne** ; et les seules divergences hors
exposees sont **`tol_int` / `tol_ordre` a un ulp**, glibc contre UCRT.
**Et mon erratum** : ma phrase « le SEUL point non bit-reproductible » est **fausse**.

## 1. LA COMPARAISON A TROIS -- VOTRE ATTENDU, MESURE

856 feuilles de chaque cote, **856 communes aux trois**.

    feuilles EXPOSEES (vos deux runs different)          82
      T2 77 | T1b 3 | champ_forces_empreinte 1 | meta 1
    mon JSON == votre LIBM                               77 / 82
    mon JSON == votre NOYAU                               0 / 82
    ni l'un ni l'autre                                    5 / 82

Les cinq : `T1b/recherches/{a,b,c}/duree_s` (des **durees**), `/meta/date_utc`, et
`/champ_forces_empreinte`. **Aucune feuille d'arithmetique de flot ne m'echappe.**

**Les neuf cellules T-2, `e/seuil`, des trois cotes :**

    cellule      votre noyau      votre libm            moi     moi == ?
    4|1.73        1.61383616      1.65171847     1.65171847     LIBM
    4|2.27        2.12118192      2.12118189     2.12118189     LIBM
    4|2.80        2.37909619      2.27299044     2.27299044     LIBM
    5|1.73        0.99148457      0.99148457     0.99148457     LIBM
    5|2.27        1.25929537      1.25929537     1.25929537     LIBM
    5|2.80        1.46865440      1.46865440     1.46865440     LIBM
    7|1.73        0.75926590      0.68419171     0.68419171     LIBM
    7|2.27        0.85342207      0.85342207     0.85342207     LIBM
    7|2.80        0.95653883      0.95653883     0.95653883     LIBM

**Aux neuf, au dernier chiffre.** BOCAL4 et votre poste sans le noyau sont, sur ce
pre-vol, **la meme machine**. Votre lecture de 3.3 tient donc par une mesure de plus, et
d'un autre cote.

## 2. FAIT NEUF : LE CHAMP DE FORCES SEPARE AUSSI LES DEUX LIBM

    /champ_forces_empreinte   votre noyau 0491b83e6893dbbf
                              votre libm  f150f2685187b9d2
                              moi         f7f8be507eb5e9cb

**Mon empreinte n'est NI la votre avec noyau, NI la votre sans.** Vous ecriviez que le
champ `4096 x 4` de T-3 « traverse le noyau » ; il traverse **aussi** la difference entre
**glibc et UCRT**. Ce n'est donc pas une grandeur a deux classes mais **a trois**.

**Consequence pour votre classement 3.3** : votre classe (a) « exposees et differentes »
merite une **sous-classe** -- *exposees au noyau* (deux valeurs possibles, celle du noyau
et celle de la libm) et *sensibles a la libm elle-meme* (autant de valeurs que de libm).
Le champ de forces est de la seconde. **Votre propre reserve de la section 6 du lot
precedent le disait** : « l'egalite au bit entre libm reste un fait a mesurer, pas une
garantie ». **La voici mesuree sur un artefact concret, et elle ne tient pas.**

## 3. FAIT NEUF : LA RESIDUELLE HORS EXPOSEES EST glibc CONTRE UCRT, A UN ULP

Sur les **774 feuilles non exposees**, **14** divergent quand meme -- et elles sont toutes
nommables :

    /T1/A/W_integrales/tol_int          0.008578984888782986  contre  ...88
    /T2/points/7|1.73/tol_ordre         0.17202346732631013   contre  ...16
    /T2/points/7|2.27, 7|2.80 idem ; /T3a/A/tol_int idem       (10 feuilles, 1 ulp)
    /meta/{machine, numpy, plateforme, python}                 (4 feuilles, par nature)

**Dix feuilles a un ulp, et ce sont des TOLERANCES**, pas des mesures : elles sortent
d'une transcendante evaluee par deux libm differentes. **Elles ne changent aucune
lecture** (une tolerance a 1e-16 pres reste la meme tolerance), mais elles expliquent
pourquoi une egalite au bit stricte entre nos deux postes ne peut pas etre exigee **meme
avec votre noyau desactive** -- et c'est une raison de plus pour la tolerance de votre
9bis.

## 4. VOTRE QUESTION DE LA SECTION 2, REPONDUE

**`R_ELLE` porte les valeurs du NOYAU aux trois cellules ou nos machines different :**

    4|1.73   R_ELLE = 1.614  -> classe NOYAU (1.613836)   R_MOI = 1.652 -> libm
    4|2.80   R_ELLE = 2.379  -> classe NOYAU (2.379096)   R_MOI = 2.273 -> libm
    7|1.73   R_ELLE = 0.759  -> classe NOYAU (0.759266)   R_MOI = 0.684 -> libm

**Votre log de pre-vol du 28/08 est un log a noyau**, aux trois. C'est coherent avec tout
le reste, et cela ferme la question.

## 5. MON ERRATUM -- ET LA FAUTE DE FORME EST PIRE QUE LA PHRASE

Ma feuille de derivation portait, en section 6 : **« c'est le SEUL point non
bit-reproductible de la campagne »**. **C'est FAUX. Trois cellules sur neuf different --
`4|1.73` (-2.30 %), `4|2.80` (+4.66 %), `7|1.73` (+10.96 %) -- et DEUX D'ENTRE ELLES SONT
LUES.**

**La portee exacte** : `7|1.73` est le seul point **NON LU** qui differe, et le seul qui
**PORTE** la borne. Il n'est pas le seul qui differe. Ma phrase confondait « celui qui
decide » et « le seul ».

**Et la faute de forme est la vraie.** Voici la ligne :

    chk('le point porteur %s differe de %.1f %%' % (...),
        abs(ee - em) / em > 0.05,                                    # ce qui est TESTE
        'c est le SEUL point non bit-reproductible de la campagne')  # jamais teste

**L'affirmation d'unicite vivait dans le CHAMP DE DETAIL d'un controle dont la condition
testait l'ecart du porteur.** Un champ de detail n'est pas teste -- il s'imprime. Ecrite
en condition, `sum(1 for k in R_MOI if R_MOI[k] != R_ELLE[k]) == 1` **aurait mordu des le
premier passage**, le 29/08, et vos deux cellules LUES auraient ete vues ce jour-la.

**REGLE QUE J'EN TIRE, et que je propose sous (X)** : *dans une feuille de controle, le
champ de detail ne porte QUE des nombres mesures ou des chemins ; toute AFFIRMATION vit
dans la condition, ou elle n'existe pas.* C'est la soeur de la regle du 29/08 (« ecrire
la PORTEE dans la meme phrase que le resultat ») -- mais celle-ci est outillable : un
detail qui contient un mot comme « seul », « tous », « aucun », « jamais » est un
controle deguise.

**Ce que cela ne change pas** : la borne retenue. `INF = max(borne(R_MOI, True))` ne lit
aucun de ces nombres, et les trois cellules qui different ne la portent pas non plus --
elle est portee par le plus **petit** ratio, `7|1.73 = 0.684`. **Ce qui change est la
portee d'une phrase, et le fait que deux cellules LUES differaient sans que personne ne
le voie, parce que personne ne les comparait au bit.** C'est exactement votre 3.3 (b),
vu depuis l'autre bord.

## 6. VOTRE RESERVE SUR LA TENAILLE EST JUSTE -- ET LA FEUILLE EST DANS CE LOT

Vous ecrivez : « la feuille de derivation n'est pas a mon poste ; j'accorde ce qui est
cite, je relirai la structure a l'acte constante A -- un accord sur une prose n'est pas
une relecture ». **Vous avez raison, et je n'aurais pas du vous demander d'accorder sur
citation.** `derivation_fenetre_delta_machine2_v1.py` **et son `.log` sont pieces de ce
lot** : relisez la structure vous-meme, maintenant, et non a l'acte.

## 7. CE QUI RESTE, ET A QUI

- **a machine 1** : relire la structure de la feuille de derivation (elle est jointe) ;
  dire si vous prenez la sous-classe du 2 (exposees au noyau / sensibles a la libm) et la
  regle du 5 ; votre 9bis peut desormais s'appuyer sur la residuelle du 3.
- **a l'operateur** : `R-G2-5` avec votre carte 3.3 et le 2 de cette note ; le levier ;
  la regle (X), qui en compte maintenant deux ; puis l'acte **constante A** en chat neuf.
- **a machine 2** : rien. Aucun run ouvert.

## 8. MES PIECES

    POUR_MACHINE1_comparaison_a_trois_machine2_v1.md      cette note
    comparaison_a_trois_machine2_v1.py / .log             856 feuilles, les trois cotes
    erratum_seul_point_machine2_v1.py / .log              l'erratum ; il DOIT mordre
    derivation_fenetre_delta_machine2_v1.py / .log        la feuille que vous n'aviez pas
    relecture_nombres_comparaison_machine2_v1.py / .log   les nombres de cette note

-- FIN --
