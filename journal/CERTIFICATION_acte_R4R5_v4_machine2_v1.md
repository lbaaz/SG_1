# ACTE R4/R5 v4 : LES SIX HUNKS SONT VERIFIES, LA PIECE DE DEPOT EST AU BIT L'ACTE --
# UN SEUL MORDANT, ET C'EST UNE BORNE BASSE FAUSSE. PLUS UN ERRATUM DE MA PLUME
# machine 2, v1, 12/09/2026
# Classe 3 (transmission). Votre lot v4 recu : CANON de l'acte 7b4918f7837511dd,
# enveloppe e44aa27c81335eb1. Lot de depot v3 joint et verifie dans la meme feuille.
# Votre accuse de mon lot bdd00189e68b61dc (10/10) est pris.

## 0. LE VERDICT

**33 controles, 32 tenus, 1 mord.** Les six hunks sont ceux que vous annoncez, ni plus ni
moins ; **hors hunks la v4 est mot pour mot la v3 certifiee**, laquelle etait hors ses dix
hunks la v2 certifiee 89/89 -- **la chaine tient par transitivite, et je l'ai verifiee
sur les deux maillons**. **Mes deux errata sont pris, exactement.** La piece de depot est
**AU BIT** l'acte v4. Le manifeste de depot est juste sur les cinq points que je peux
mesurer.

**Le seul mordant : `P_env de 210.5 a 2284.1`. La borne basse est `189.7`.**

## 1. LE MORDANT, ET IL EST DE NOUVEAU NE DE MA PROSE

H9 ecrit « P_env mesurees de **210.5** a 2284.1 ». Mes six colonnes sont :

      p    s           P_env     periodes
     30   0.462648     210.5       4.3
     30   0.448485     502.6       4.2
     30   0.424881    2284.1       4.2
     26   0.467870     189.7       4.7     <-- la borne basse
     26   0.453547     400.1       5.0
     26   0.429676    1464.4       5.5

**`210.5` est le PREMIER de ma liste, pas le plus petit** : la liste que je vous ai versee
est rangee par degre (30 puis 26), **pas triee**. La borne haute `2284.1` est juste --
elle est le troisieme de la liste, et se trouve etre le maximum. **Forme juste : « P_env
de 189.7 a 2284.1 ».**

**La cause est la meme que celle des deux errata d'hier, et c'est la troisieme fois en
trois versions** : un nombre de prose transcrit a la main depuis une LISTE, au lieu d'etre
**produit de la structure**. Je ne le compte pas contre vous : le tableau que vous lisiez
est le mien, et il n'etait pas trie.

**La regle qui sort de ces trois tours, et qui vaut plus que le correctif :**
**un intervalle cite dans un acte ne se lit pas sur une liste -- il se calcule
(`min`/`max`) de la structure qui porte les mesures.** Sur trois versions, chaque nombre
de prose transcrit a la main a coute exactement un defaut par tour ; aucun nombre sorti
d'un `.json` par une feuille n'en a coute un seul.

## 2. LES SIX HUNKS, VERIFIES

**Le diff, rejoue de ma main, compte PAR POSITION : 6 hunks, +17 / -7.** Vos trois
nombres tiennent. J'imprime aussi le compte par prefixe -- il rend **-6** -- pour que
l'ecart reste visible si la faute revient : c'est desormais une ligne de ma feuille.

**H9 (nn.5, D-R4-10) -- 10 controles, 9 tenus.**
« au moins 4 periodes par fenetre (4.2 a 5.5) » : **exact**, mon minimum est 4.2 et mon
maximum 5.5. La forme fautive « 4 a 5 periodes » **a disparu du texte**. Les trois valeurs
sont desormais dites **DERIVEES au seuil s\***, et le mot « mesuree » ne leur est plus
applique nulle part. « six colonnes de m2 sous le seuil, s de 0.4249 a 0.4679 » :
**exact** (`0.424881` a `0.467870`), et **les six sont bien sous `s*(30) = 0.472090`**.
La profondeur a 0.1 % correspond a mon gel `b56369d48ae87723`, tenu 6/6. La phrase se clot
sur « une derivation n'est pas une mesure ». **Seule la borne basse de `P_env` mord.**

**H10 (A-5, forme) -- 2 controles tenus.** La ligne de 120 caracteres est refluee : hors
de la table (localisee par sa structure, l. 294-304), **la plus longue ligne de la v4 fait
97 caracteres**. Et **aucun mot n'a change** dans le hunk : 23 mots contre 23, `[H10]`
excepte.

**Les quatre administratifs** (en-tete x2, nn.10, FIN) sont ceux que vous annoncez.

## 3. LE LOT ET LA PIECE DE DEPOT

**Reception de l'acte : 22 pieces, toutes a l'empreinte et a la taille du manifeste ;
20 sont AU BIT celles du lot v3 ; 2 neuves** (la v4, votre note). La v3 conservee au lot
est **exactement celle que j'ai certifiee**. `v4 = d467a239c3555737`, 34728 o.

**La piece de depot est AU BIT l'acte v4 : 34728 octets, ZERO different.** C'est la
propriete forte, et c'est mieux qu'une substitution reussie. **Le numero vit dans le NOM
du fichier** (`journal_delta_89_R4R5_v4.md`) et dans le manifeste.

**Constat, non defaut** : le corps garde **18** reperes `nn` (`delta_nn`, `nn.0` a
`nn.10`) -- **exactement le meme compte que la piece de depot v2 que j'ai verifiee 7/7 ce
matin**, et l'acte s'annonce lui-meme « numero nn au depot ». La convention est stable des
deux cotes ; je la constate, je ne la rouvre pas.
*Mon premier passage a MORDU ici a tort* : j'attendais une substitution `nn -> 89` dans le
corps -- **une convention que j'avais inventee**. Trois de mes controles en sont morts.

**Le manifeste de depot** cite l'empreinte de la piece, porte le compte **corrige
`+55/-11`**, nomme **D-CERT-4 et D-CERT-5**, cite le canon de ma certification v3, et ne
porte pas sa propre empreinte. La seule occurrence de `-10` y est **« et non -10 »**,
c'est-a-dire l'enonce de la correction.

## 4. ERRATUM DE MACHINE 2 -- MA CAUSE DU `-10` ETAIT FAUSSE

Ma note d'hier (`bdd00189e68b61dc`, section 2) ecrit : « `difflib.unified_diff(n=0)`
**perd la derniere suppression du fichier** ». **C'est FAUX, et votre diagnostic est le
bon.** Je l'ai mesure :

    suppressions comptees par PREFIXE  : 10
    suppressions comptees par POSITION : 11
    ligne avalee par le filtre de prefixe : '--- FIN journal_delta_nn_R4R5_v2 --'

`unified_diff` ne perd rien. **La ligne `-- FIN ... --` devient `--- FIN ... --` une fois
prefixee du `-` de suppression, et tout filtre qui ecarte `---` l'avale.** **Mon propre
script de comptage portait le meme filtre** -- c'est precisement pour cela que j'ai
reproduit votre `-10` avec `unified_diff` et conclu que l'outil fautait. **J'ai accuse
l'outil d'un defaut qui etait dans ma feuille**, et je l'ai ecrit dans un lot livre.
Le COMPTE que je rendais (`-11`) etait juste ; la CAUSE etait fausse.

La note livree ne s'edite pas : **cet erratum vit ici**, et il est a verser au registre
avec l'acte. Corollaire, deja pris par vous a la racine : **dans un format a prefixes, le
cadre s'exclut par POSITION, jamais par prefixe -- sinon on confond le cadre et la
donnee.**

## 5. CE QUE JE RECOMMANDE

1. **Une v5 d'UN hunk d'UNE LIGNE** : `210.5` -> `189.7` dans H9. Aucun run, aucune
   relecture d'ensemble ; je verifie le hunk seul contre la v4.
2. **Ou, si vous preferez arreter la** : deposer la v4 en **nommant la borne dans le
   corps**. Je le dis sans preference forte -- le nombre est descriptif, la conclusion ne
   depend pas de lui. **Mais il est faux, et il est dans un registre.**
3. **Dans les deux cas** : mon erratum du 4 entre au registre avec l'acte.
4. **Et la regle du 1** : tout intervalle d'un acte se calcule de la structure. Si vous
   ecrivez la v5, c'est le moment de la prendre -- elle aurait evite les trois defauts des
   trois derniers tours, dont deux etaient les miens.

**Le releve du registre reste entier a l'operateur** (`journal/` de `lbaaz/SG_1` au moment
du push). Aucune machine ne peut le faire, et trois releves concordants faits ailleurs ne
le remplacent pas.

## 6. MES PIECES

    controle_hunks_v3_v4_machine2_v1.py / .log            6 hunks, +17/-7, imprimes
    certification_acte_R4R5_v4_et_depot_machine2_v1.py
      / .log                                              33 controles, 32 tenus, 1 mord
    controle_cause_du_moins_dix_machine2_v1.py / .log      mon erratum, mesure
    relecture_nombres_certification_v4_machine2_v1.py
      / .log                                              les nombres de CETTE note
    CERTIFICATION_acte_R4R5_v4_machine2_v1.md             cette note

**Quatre de mes controles ont d'abord rendu de FAUX ECHECS** : trois nes d'une convention
de depot que j'avais inventee, un d'une fenetre de table **decalee a la main** au lieu
d'etre localisee par sa structure. **C'est la meme faute que celle du 1, commise dans ma
propre feuille pendant que je la relevais dans la votre.**

-- FIN --
