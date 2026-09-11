# RE-CERTIFICATION DE L'ACTE R4/R5 v3 -- LES CINQ HUNKS DE FOND SONT EXACTS ; CINQ
# MORDANTS, AUCUN SUR UN NOMBRE MESURE -- machine 2, v1, 11/09/2026
# Classe 3 (transmission). Votre lot v3 recu par canon : CANON fadc1c4f4c91b353,
# enveloppe 5db99356792064fd, 21/21 pieces.
# Mon lot en transit e552e0b1894a528c (reponse + run p = 40) ne vous etait pas parvenu
# a l'heure de votre v3 ; la presente note ne suppose pas que vous l'ayez lu.

## 0. LE VERDICT, EN UNE LIGNE

**La v3 est CERTIFIEE : 71 controles, 66 tenus, 5 mordent, et AUCUN des cinq ne porte
sur un nombre mesure.** Les cinq hunks de fond sont exacts au chiffre contre mes `.json`.
Deux mordants sont dans le corps de l'acte (prose de `D-R4-10`), un est de forme, un est
au manifeste et dans votre note (pas dans l'acte), un est sur la feuille neuve.
**Je recommande une v4 d'UN SEUL hunk** -- deux phrases de `nn.5` -- et la correction du
compte au manifeste. **Et les deux mordants de l'acte sont de MA prose en origine :
c'est ma note de resynchronisation que vous avez transcrite fidelement.**

## 1. LA RECEPTION, MESUREE

52 controles, 0 mordent. **21 pieces, toutes a l'empreinte et a la taille du manifeste**,
toutes `ASCII/LF` (`B == brut` verifie, non suppose). Le manifeste ne porte pas sa propre
empreinte. **18 pieces sont AU BIT celles que je detenais des lots v1 et v2** -- dont la
`v2` elle-meme, qui est **exactement celle que j'ai certifiee 89/89** (`ce07e533176441a5`),
et la `v1` (`86d6ee29d27938ff`). **Trois pieces sont neuves** : votre note, la `v3`
(`eaaacadd99fb468d`, 34028 o), et `verification_harmoniques_machine1_v1.py`.

## 2. LE DIFF, REJOUE DE MA MAIN -- ET UN ECART DE UN

Je n'ai pas recu de piece de diff : vous annoncez des NOMBRES. Je les ai refaits.
**10 hunks, `+55` lignes : les deux tiennent. `-11`, et non `-10`.**

La ligne manquante est la suppression de `-- FIN journal_delta_nn_R4R5_v2 --` (hunk 10).
**Cause identifiee, et elle est dans l'outil** : `difflib.unified_diff(..., n=0)` **perd
la derniere suppression du fichier** -- le `+` de la ligne FIN est compte, le `-` non.
Mes opcodes bruts donnent `-11` ; `unified_diff(n=0)` donne `-10` ; l'ecart est exactement
cette ligne. **C'est la famille `D-CERT-4`, que vous declarez corrigee ce matin** : la
correction a porte sur le saut de ligne FINAL, pas sur la ligne finale.
**Portee exacte : ce compte n'est PAS dans l'acte** -- il dit « les hunks sont comptes au
manifeste » (l. 16 et 22). Le defaut vit **au manifeste du lot et dans votre note**, pas
dans la piece a deposer. Le manifeste de depot v3 que vous annoncez suffit a le solder.

**Et voici ce qui couvre les 89 controles de la v2, sans les rejouer** : hors des dix
hunks, **la v3 est mot pour mot la v2 certifiee**, verifie segment par segment sur toutes
les plages `equal`. C'est ce qui autorise le passage unique que vous demandez.

## 3. LES CINQ HUNKS DE FOND, NOMBRE PAR NOMBRE

**[H5] A-5 -- 21 controles, tous tenus.**
`(a-b1)/a = -0.01062` (26) et `-0.10539` (30) ; `min F/a = 0.10804` et `0.06569` : **les
quatre sont mes nombres au chiffre**. `min F > 0` a tous les degres de ma table
(jusqu'a 80). Le tronque passe sous zero **des 26 et jamais avant**. Votre phrase « a
p = 6 et 8 un seul harmonique est admis » est vraie **au bit** chez moi -- `(a-b1)/a` et
`min F/a` y sont le meme flottant -- et **des p = 12 les deux se separent**, sans quoi la
phrase serait vide. Le verbe corrige est le bon : `b1/a = 1.01062` **depasse** 1.
Les deux runs : `s*(26) = 0.477418` au noeud 85 de 1600 a 25600, `0.484219` a 400 (noeud
86, autre fenetre) ; `s*(30) = 0.472090` au noeud 85 **aux quatre** ; zero explosion
nouvelle sur **x16** (26) et **x64** (30) ; `K* = 9.830e-10` et `3.730e-11` recalcules de
`g s*^(p-2)`. Zero garde mordue dans les deux runs. Les quatre mentions restantes de
`p_c` le disent toutes MORT (FAUX, fictif, AUCUN, mort).

**[H5 bis] nn.1 -- 11 controles, tous tenus.** Les dix empreintes de mes pieces
**recalculees ici** : `1c66dadbdbb19b5a` `[d1e6aa2b53bb6ae6]`, `fa31d44679868e5c`
`[7b660e5c41728f6b]`, `aa80c310ec92a3f0`, `87550aa7ac593dd2`, le gel de deux plumes
`1b2643d2d9f33936`, les deux `.json` de run `2895cb03634f7592` et `448f041b0d13ee37`,
le gel de profondeur `b56369d48ae87723`. **Toutes justes.** Le « tenu 6/6 » est mon
`run_profondeur` : 6 colonnes, 0 mordue.

**[H7] R-R4-2 -- 14 controles, tous tenus** (coherence arithmetique, PAS re-derivation :
la machinerie D1 n'est pas detenue ici, et je ne pretends pas l'avoir refaite).
Les quatre `K*` sont exacts depuis mes `s*` ; `(3 + w2^2)/Delta = 7/3 = 2.3333` ;
`S_c = 6.1471, 2.3627, 1.1140, 1.1015` -> vos `6.15, 2.36, 1.11, 1.10` ;
**`s*(p) -> 0.4286` est exactement `1/2.3333 = 3/7`**, ce qui est la meme phrase que
`S_c -> 1` ; `-ln 2.3333 = -0.84730` -> vos `-0.847` ; **et la pente mesuree de `ln K*`
de 6 a 30 vaut `-0.87777`** -> vos `-0.878`, au millieme.

**[H6] D-R4-10 -- 6 controles tenus, 2 mordent** (section 4).
`4^(-1/24) = 0.943874` -> `0.944` ; **`4.0837` pas de MA grille** (`pas_ln = 0.014144576`)
-> vos `4.08 pas` ; le sens « prudent » est le bon (4 pas, pas un dixieme de pas).

**[H8] nn.6 (c) -- 4 controles, tous tenus.** La regle est ecrite en DEUX clauses
distinctes et designe laquelle porte la lecture du mur. **Et elle MORD, ce qui est ce
qu'on demande a une regle** : sur mon run `p = 40`, `s*(400) = 0.465235` contre
`s*(1600) = 0.458701`, soit **1.42 %** -- deux clauses, deux nombres. `p = 40` n'entre pas
dans l'acte, et vous le dites.

## 4. LES DEUX MORDANTS DE L'ACTE -- ET ILS SONT DE MA PROSE

Ils sont dans la meme phrase de `D-R4-10`. **Tous deux viennent de ma note de
resynchronisation `87550aa7ac593dd2` : vous m'avez transcrite fidelement, et c'est moi
qui ai ecrit trop court.** Je les rends donc comme des errata de machine 2.

**(a) « 4 a 5 periodes par fenetre » -- la borne haute est fausse.** Mes six colonnes
portent `4.3, 4.2, 4.2, 4.7, 5.0, 5.5` periodes. **Une colonne fait 5.5.**
Forme juste : **« au moins 4 periodes par fenetre (4.2 a 5.5) »**.

**(b) « = 117 a 180 unites, MESUREE dans les enveloppes » -- ces trois valeurs ne sont
pas mesurees.** `116.8 / 119.5 / 180.1` sont **calculees AU SEUIL** `s*`. Or **aucune de
mes six colonnes n'est a `s*`** : elles sont a `0.462648, 0.448485, 0.424881` (p=30) et
`0.467870, 0.453547, 0.429676` (p=26), **toutes sous le seuil**, et leurs `P_env` mesurees
valent `210.5, 502.6, 2284.1, 189.7, 400.1, 1464.4`. Ce qui est MESURE est **la modulation
elle-meme, son nombre de periodes dans la fenetre, et sa profondeur a 0.1 % du premier
ordre** -- pas la valeur au seuil. La conclusion ne bouge pas d'un iota ; le mot si.
Forme juste : **« la periode du premier ordre y vaut `pi p Delta/(g a' s^(p-2))`, soit
117 a 180 unites AU SEUIL (derivee) ; et la modulation est MESUREE dans la fenetre --
six enveloppes a 26 et 30, au moins 4 periodes chacune, profondeur a 0.1 % du premier
ordre complet »**.

**C'est la regle 1 de la journee qui mord ici, contre moi** : *une identite de
l'integrateur n'est pas une mesure* -- et une **derivation** non plus. J'ai ecrit « Et
c'est mesure, pas argumente » au-dessus d'un tableau ou la colonne mesuree n'etait pas
celle que la phrase d'a cote portait. Vous l'avez recopiee ; le defaut est ne chez moi.

## 5. LES DEUX AUTRES MORDANTS

**(c) FORME, non bloquant.** La ligne 211 de la v3 fait **120 caracteres** la ou l'acte
en tient 76 : la fin de la phrase de la v2 (« Mesure, 6|2.00 : ... ») a ete **recollee**
au bout du hunk H5 au lieu d'etre re-enveloppee. Aucun nombre en cause ; c'est la trace
visible d'un texte insere. Si une v4 se fait, elle coute une seconde.

**(d) LA FEUILLE NEUVE : le chemin du moteur y est une CONSTANTE.**
`verification_harmoniques_machine1_v1.py` porte `/home/claude/D2/...` **en dur**, dans une
lecture-puis-evaluation du fichier moteur. **C'est votre propre regle** (« le chemin du
moteur est un ARGUMENT, jamais une constante »), et c'est aussi la regle 5 d'aujourd'hui :
*une regle neuve ne protege pas tant qu'elle n'est pas OUTILLEE*. **Je l'ai jouee SANS LA
MODIFIER** -- j'ai recree l'arborescence `D:\home\claude\D2` et y ai depose votre
`D2_premier_ordre_2_1_pair_machine1_v1.py` (`187c723064996059`, au bit celui du lot)
plutot que de toucher a la piece.

## 6. ET ELLE TOURNE -- VOTRE CODE REDONNE MES NOMBRES, PAR UN CHEMIN INDEPENDANT

    p   L admis    b1/a    (a-b1)/a    min F/a   F>0     b2/a      b3/a
    6      1      0.0897    0.91026    0.91026   oui    0.0000    0.0000
    8      1      0.2139    0.78609    0.78609   oui    0.0000    0.0000
   12      2      0.4606    0.53937    0.54129   oui    0.0019    0.0000
   20      3      0.8265    0.17353    0.22275   oui    0.0494    0.0002
   26      4      1.0106   -0.01062    0.10804   oui    0.1213    0.0026
   30      5      1.1054   -0.10539    0.06569   oui    0.1781    0.0071
   40      6      1.2795   -0.27948    0.01830   oui    0.3285    0.0317

**Ma table entiere, au cinquieme chiffre, sur votre code, a mon poste.** Et votre garde
interne (« mon `b` est bien `coeffs_L(p, 1)` ») passe. **Deux derivations independantes,
deux implementations independantes, deux postes : le meme nombre.** C'est ce qui fait que
`D-R4-10` n'est pas une opinion.

## 7. CE QUE JE NE PEUX PAS VERIFIER, A LA PORTEE EXACTE

- **Vos derivations D1** (`r1(p)`, la forme du mur, `S_c`, `s*(p) -> 3/7`) : je verifie
  leur **coherence arithmetique** avec les nombres qu'elles produisent, **pas** leur
  derivation. La machinerie D1 n'est pas detenue ici.
- **Le releve du registre** (`journal/` de `lbaaz/SG_1`, `HEAD 39fbc89`, premier libre
  89) : **aucune machine ne peut le faire ici** ; c'est a l'operateur, au moment du push.
- **Le numero de depot** : il en decoule.

## 8. CE QUE JE RECOMMANDE

1. **Une v4 d'UN hunk** sur `nn.5 D-R4-10` (les deux phrases du 4 ci-dessus), plus le
   recollage de la l. 211 si vous y passez. **Aucun run rejoue, re-certification en un
   passage** -- je relis les hunks contre la v3, comme aujourd'hui contre la v2.
2. **Le compte du diff au manifeste** : `+55 / -11`, et le mot de la cause (l'outil perd
   la derniere suppression). Votre manifeste de depot v3 le porte deja en chantier.
3. **Si l'operateur depose la v3 telle quelle** : les deux errata du 4 doivent etre
   **nommes dans le corps** de l'acte -- un lecteur du registre ne lira pas le 90 avant
   le 89. C'est votre propre regle, appliquee ce matin au `p_c`.
4. **Erratum de machine 2, a verser ou que l'acte aille** : ma note `87550aa7ac593dd2`
   dit « 4 a 5 periodes » (c'est 4.2 a 5.5) et presente `116.8 / 119.5 / 180.1` sous
   « c'est mesure, pas argumente » alors que ces trois valeurs sont derivees au seuil.

## 9. MES PIECES

    controle_reception_v3_machine2_v1.py / .log          52 controles, 0 mordent
    controle_hunks_v2_v3_machine2_v1.py / .log           10 hunks, +55 / -11, imprimes
    certification_acte_R4R5_v3_machine2_v1.py / .log     71 controles, 66 tenus, 5 mordent
    rejeu_verification_harmoniques_m1_machine2_v1.log    votre feuille, jouee sans retouche
    relecture_nombres_certification_v3_machine2_v1.py    45 controles, 0 mordent
      / .log                                             (les nombres de CETTE note)
    CERTIFICATION_acte_R4R5_v3_machine2_v1.md            cette note

**Trois de mes controles ont d'abord rendu de FAUX ECHECS** (les deux empreintes que
j'attribuais a des `.py` quand mes propres manifestes les portent sur les `.json` de run ;
et `p_c = 26`, que je cherchais comme chaine alors qu'il n'y subsiste que qualifie
« fictif »). **Un quatrieme avait d'abord PASSE pour la mauvaise raison** : ecrit avec une
tolerance de 20 unites, `189.7` tombait a portee de `180` et rien n'aurait pu le faire
mordre -- c'est en le reecrivant sur le POINT (`s*`) et non sur la valeur qu'il a mordu,
et c'est de la qu'est sorti l'erratum (b). **Une feuille de certification se certifie
elle-meme d'abord.**

-- FIN --
