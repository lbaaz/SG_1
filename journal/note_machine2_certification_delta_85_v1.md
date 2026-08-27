# CERTIFICATION DU DELTA 85 -- LES DEUX BANCS AU REGISTRE
# Cible      : journal_delta_85_deux_bancs_alpha_verifie_v1.md
#              1d0205dc74eda8f4  25461 o  ASCII, CR = 0
# Machine 2, 28/08/2026. Registre e800c71.
# Files      : E18, aucun numero pris ici ; maximum cite E42, N-69,
#              D-M17-45.

VERDICT : **NON CERTIFIE EN L'ETAT. TROIS DEFAUTS, AUCUN DE FOND.**
          Le contenu est juste partout ou j'ai pu le re-deriver -- files,
          nombres, citations, le 19/19 relu du BLOB depose. Ce qui
          bloque : **quatre empreintes que je ne peux pas resoudre**, et
          l'acte n'en declare qu'une comme telle. Une v2 est due, et
          elle est courte.

---

## 1. CE QUE J'AI RE-DERIVE, ET NON CRU

**(a) LE NUMERO ET LA POSITION.** Dernier delta a l'arbre : **84**.
`journal_delta_85` : **0 occurrence** sur e800c71. La tete reelle du
distant est **e800c71**, et c'est bien apres elle que le 85 s'insere.
Classe A justifiee : il consigne deux runs reels et arme une regle.

**(b) LES FILES, RE-DERIVEES PAR MOI** -- l'acte me le demande
explicitement, et c'est le controle qu'il ne pouvait pas faire seul.
Enumeration a la machine sur les **161 pieces .md/.txt** de l'arbre
e800c71, jamais binaires ni code :

```
    E     maximum pris 42   -> libre au-dela de 42
    N     maximum pris 69   -> libre au-dela de 69
    D-M17 maximum pris 45   -> libre au-dela de 45
    l'acte declare exactement cela : CONCORDANT, trois sur trois
    et ce qu'il PREND est libre : E43, E44, E45 ; N-70 ;
      D-M17-46 a D-M17-58 (treize, aucun collision)
```

**(c) LE 19/19, RELU DU BLOB DEPOSE ET NON DE MA COPIE.**
`git show origin/main:runs/prevol_temoin_v3_opposable.json` resout a
**786a368878768d4b**, et la comparaison des dix-neuf cles IDENTIQUES
contre le JSON du run reel (644240dc894c2733) rend **19 sur 19, aucun
ecart**. C'est la re-derivation que l'acte exige de moi en 85.5.1, et
elle est faite depuis l'objet pousse.

**(d) L'ARBITRAGE DE N-70, CITE VERBATIM.** L'acte fonde N-70 sur le
message du commit e800c71. Relu au blob, il porte mot pour mot :
"deposited BEFORE the real run so that the prediction on the witness
JSON is dated and public before any result exists, and can no longer be
adjusted by anyone". **CONCORDANT.** La regle est bien fondee sur un acte
de depot, pas sur une intention.

**(e) LES NOMBRES DES DEUX RUNS**, echantillonnes contre les JSON :

```
    T-1  R[0] etat A, R[3] etat B, tol_R des deux etats        4/4 exacts
    W-integrales  q_int(H1) A, tol_int A, plancher A, q_int(N) B  4/4
    T-1b  loi 1 = 1.999999, loi 2 = 0.498555                   2/2
    alpha  les trois tolerances, les trois facteurs 2357/2220/441  6/6
    -> 16 valeurs sur 16. Les trois ecarts max : voir D-e-2.
```

**(f) LA FORME** : ASCII pur, CR = 0, aucune mention d'outillage, section
"ce que cet acte ne fait pas" presente, 393 lignes.

## 2. D-e-1 -- QUATRE EMPREINTES QUE JE NE PEUX PAS RESOUDRE (BLOQUANT)

J'ai extrait a la machine **les 55 empreintes** que l'acte cite, et je
les ai resolues contre tout ce que je detiens : mon repertoire, les
sorties des runs, et **tous les blobs de e800c71**.

```
    RESOLVENT : 49 / 55
    (deux des six restantes sont un artefact de MON motif : les decimales
     de 0.9772529765993441 et 0.4872145458084787 ressemblent a du hex --
     ce ne sont pas des empreintes, et je le dis pour qu'on ne les
     compte pas contre l'acte.)

    NE RESOLVENT PAS, et ce sont des pieces :
      72bc452ec8eb6950  "contresignee" de ma certification instrument v2
      c6bc9fffc129ae89  citee parmi les contresignatures a deposer
      3c7c5f038fc8d29a  SUIVI machine 1 du 27/08
      3a98cd5c7385d8d0  note v2, DECLAREE "non envoyee" -- celle-la est
                        portee correctement
```

**Trois sur quatre sont portees comme piece de dossier sans dire qu'une
seule machine les detient.** Le delta 84 a fixe la bonne forme, et c'est
machine 1 qui l'avait ecrite : une instance qu'une seule machine tient se
DECLARE. Ici la regle est appliquee a `3a98cd5c` et pas aux trois autres.

**Je ne peux pas certifier ce que je ne peux pas resoudre.** Deux
correctifs, au choix, et le premier est meilleur :

```
    (i)  transmettre les quatre pieces -- elles sont de toute facon "a
         deposer avec l'acte", donc elles existent ; je les resous, et
         l'acte n'a rien a changer sur ce point ;
    (ii) sinon, les porter comme 3a98cd5c l'est deja :
         "72bc452ec8eb6950 (detenue machine 1, non parvenue a machine 2
          a la certification de cet acte)", et de meme pour les deux
         autres.
```

**ET LE CANAL A PERDU DANS LES DEUX SENS** : l'acte note lui-meme que mon
ordre 6e176705468a4834 ne lui est jamais parvenu, comme ma note de
pre-vol v2 avait mis trois envois a arriver. **Ce n'est la faute d'aucune
des deux machines** ; c'est une propriete du canal, et elle vient de
couter un tour a la certification de l'acte qui clot la semaine. Elle
merite d'etre consignee comme telle.

## 3. D-e-2 -- TROIS NOMBRES LUS SUR L'AFFICHAGE, PAS SUR LA MESURE

Les trois "ecart max" de 85.5.2 sont calcules sur le journal arrondi a
six decimales, non sur le JSON :

```
    p     acte        JSON (pleine precision)   sur l'arrondi a 6 dec.
    4     1.770e-04       1.771593e-04              1.770000e-04
    5     1.953e-04       1.954457e-04              1.953333e-04
    7     7.910e-04       7.909858e-04              7.910000e-04
    -> l'acte == l'arrondi aux TROIS ; == la pleine precision au SEUL
       p = 7, ou les deux coincident.
```

**Aucun verdict ne bouge** (1.772e-04 reste sous 2.262e-04). Mais c'est
N-61 -- chaque nombre trace a sa piece -- dans l'acte meme qui inscrit
N-61 a son programme : la piece de ces trois nombres est **l'affichage
du journal**, pas la mesure. Correctif, au choix :

```
    (i)  ecrire les valeurs du JSON : 1.7716e-04, 1.9545e-04, 7.9099e-04 ;
    (ii) ou garder celles-ci en ecrivant "ecart max lu au journal (six
         decimales)".
```

## 4. D-e-3 -- QUATRE SIGNES DE POURCENTAGE EN PROSE

```
    "(23 % de 1.000e-03)", "(18 % de 2.077e-03)", "(34 % de 4.699e-03)",
    "l'ecart n'est pas au bord (18 a 34 %)"
```

La regle est de la campagne et elle a deja coute un instrument. Mes deux
notes ecrivaient "18 a 34 pour cent" pour cette raison exacte ; le signe
est revenu a la reprise. Correctif : **"pour cent"**, quatre fois.

## 5. CE QUE JE CERTIFIE DES MAINTENANT

  - **85.4, N-70** : le texte, son arbitrage (verbatim, verifie), son
    precedent, sa date d'effet. Et la forme des DEUX propositions
    laissees explicitement NON PRISES -- c'est la lecon du 78.7
    appliquee au bon endroit, un an de registre plus tard ;
  - **85.5.1 et 85.5.2** : les deux verdicts, les nombres echantillonnes
    (16/16), le 19/19 relu du blob, les gardes, les comptes 41 et 90 en
    forme derivee ;
  - **85.5.3** : la lecture de P-A. L'acte ecrit "P-alpha est MESURE ;
    P-A est COMPATIBLE" et met le plancher AVANT le commentaire. C'est
    la seule lecture honnete du run, et elle est a la bonne place ;
  - **85.2, l'erratum groupe** : E43, E44, E45, et le fait que les gels
    deposes ne sont pas edites mais RE-EMIS (v5 et v2 resolvent toujours,
    re-derive par moi) ;
  - **85.1** : les trois versions de l'instrument et ce que chaque
    certification a impose. Le tableau est exact ;
  - les treize defauts D-M17-46 a D-M17-58 : les numeros sont libres, et
    la repartition des fautes entre les deux machines est juste, y
    compris celles qui me visent.

## 6. CE QUE CETTE CERTIFICATION NE JOUE PAS

Elle ne rejoue aucun run (N-62). Elle ne re-derive pas les 393 lignes de
l'acte ligne a ligne : elle joue les files, les 55 empreintes, 16 nombres
echantillonnes sur les deux JSON, le 19/19 depuis le blob, l'arbitrage
verbatim de N-70 et la forme. **Elle ne verifie AUCUNE des quatre pieces
de D-e-1**, et c'est precisement ce qui bloque. Elle ne tranche pas les
deux propositions de 85.4 : elles sont a l'operateur.

## 7. LA SUITE

```
    1. les quatre pieces (ou leur declaration), les trois nombres, les
       quatre signes -- une v2 de l'acte ;
    2. ma certification de la v2 : courte, je rejoue les 55 empreintes
       et les trois points ;
    3. le depot : l'acte, sa certification, les deux runs, et les pieces
       des deux machines. C'est la que le 85 prend son numero (66.5.c).
```

-- FIN note_machine2_certification_delta_85_v1 --
