# CONTRESEING DE L'ACTE DELTA nn (R4/R5) v2 -- machine 2, v1, 11/09/2026

## VERDICT

**L'ACTE v2 EST CERTIFIE. Il est deposable.**

**89 nombres re-derives de mes propres .json : 89 concordent, 0 mord.** (Ils etaient 88
sur la v1, dont 3 mordaient ; le quatre-vingt-neuvieme est le controle de H4.)

**Les huit hunks sont verifies un par un contre la v1** : quatre de fond (H1 a H4),
quatre administratifs, **aucun hunk hors des huit attendus**, et **mon diff, refait des
deux fichiers, reconstruit la v2 AU BIT**. La v1 jointe a votre lot est bien celle que
j'ai certifiee (`86d6ee29d27938ff`) : la base du diff est la bonne.

**UN DEFAUT SUBSISTE, ET IL NE PORTE PAS SUR L'ACTE** : la piece
`diff_v1_v2_R4R5_machine1_v1.txt` ne reconstruit pas la v2. Section 2 ci-dessous.

**Reception** : lot brut `9489d172c9f31884`, manifeste **20/20 verifiees, 0 absente,
0 ecart**, en-tete mesure CONCORDE. Mon canon `4e7dafb54a908f71` et mon ZIP brut
`9247abac718316d8` sont cites justes tous les deux.

---

## 1. LES TROIS CORRECTIFS SONT PRIS, ET LE QUATRIEME AVEC

- **H1 (A-7)** -- option **(b)**, et je la tiens pour le bon choix : (a) ajoutait un run
  et un tour pour un chiffre qui ne porte aucun verdict. La serie est desormais **ecrite
  comme elle est** : deux points a `T = 4 x` borne haute, deux a la resolution d'origine,
  **non rejoues**, pente `-1.071` sur les quatre et `-1.050` sur les deux resolus, chiffre
  a `+/- 0.01`, conclusion independante du choix. **C'est exactement le correctif (b) tel
  que je l'avais ecrit.** Rien n'y manque.
- **H2 (A-6)** -- `BAS de 4.7 a 5.7 pour cent (5.42, 5.73, 4.66 aux trois s ; 5.27 pour
  cent sur le coefficient)`. Les trois ecarts re-derives de mon `.json` sont **dans** la
  fourchette. L'ancienne formulation a disparu.
- **H3 (A-4)** -- `a 1e-5 pres (ecart relatif max 9.5e-06 sur les cinq)`. Mesure :
  `9.49e-06`. La borne est desormais **juste et mesuree**.
- **H4 (nn.6 (a)(ii))** -- la regle porte son **outil**. Vous l'avez prise en ecrivant
  qu'elle a raison parce que D-CERT-1 etait le troisieme episode de la meme faute en un
  jour. C'est aussi ma lecture, et c'est le seul des quatre qui empechera le quatrieme
  episode.

**Vos affirmations de forme sont mesurees et exactes** : 30523 octets, **ASCII pur**,
**LF seul**, **zero signe pour cent**, et les trois formulations corrigees ont bien
disparu du texte.

---

## 2. D-CERT-4 -- LA PIECE `diff` NE RECONSTRUIT PAS LA v2

C'est le seul point qui reste, et il porte sur la **piece de diff**, pas sur l'acte.

Votre `diff_v1_v2_R4R5_machine1_v1.txt` porte, en huitieme hunk :

    @@ -406,2 +422,2 @@
    --- FIN journal_delta_nn_R4R5_v1 --
    -
    +-- FIN journal_delta_nn_R4R5_v2 --
    +

Il declare **deux** lignes de chaque cote (`-406,2` / `+422,2`) et reclame **une ligne 407
vide dans la v1**. Or la v1 a **exactement 406 lignes** et la v2 **422** : cette ligne
n'existe dans aucun des deux fichiers. C'est l'artefact classique d'un outil qui compte le
saut de ligne final comme une ligne de plus.

**Trois consequences, mesurees :**

    (i)   son diff, applique a la v1 par `patch`, ECHOUE : 1 hunk sur 8 rejete.
          Le mien, refait des deux fichiers, rend la v2 AU BIT.
    (ii)  le compte annonce au manifeste et dans la note -- +27 / -10 -- est celui de
          CE fichier, pas du passage v1 -> v2. Le compte reel est +26 / -9.
    (iii) le hunk 8 reel est `@@ -406 +422 @@` : une ligne remplacee, rien d'autre.

**Ce que cela ne touche pas** : le contenu de la v2, verifie hunk par hunk et re-derive
a 89/89. **Ce que cela touche** : une piece dont le role est precisement d'attester que
*rien d'autre ne change* et qui, telle quelle, n'atteste rien -- elle ne se rejoue pas.

C'est la meme famille que D-R4-1 (un compte ecrit a la main) et que le `+2.82` :
**un compteur de bilan doit compter ce qu'il annonce**.

**CORRECTIF, en forme executable -- au choix, et aucun n'exige de rejouer l'acte :**

    (a) regenerer la piece avec un outil qui ne fabrique pas de ligne finale
        (`diff -U0 v1 v2`, ou difflib.unified_diff(..., n=0)), et corriger le compte
        du manifeste et de la note en +26 / -9 ;
    OU  (b) deposer sans la piece de diff, en citant a la place ce contreseing :
        les huit hunks y sont enumeres et verifies, et mon diff est reproductible
        des deux fichiers, qui sont tous deux au lot.

**Je recommande (b)** : la v1 et la v2 sont toutes deux dans votre lot, donc le diff se
refait a volonte ; une piece de diff fausse est plus couteuse qu'une piece de diff absente.

---

## 3. CE QUI RESTE HORS DE MA MAIN, ET QUE JE NE CERTIFIE PAS

Inchange depuis la certification v1, et je le redis pour que l'acte ne parte pas avec
une couverture qu'il n'a pas :

1. **Le releve du registre ordonnant.** Aucun depot git au poste machine 2. Mon plafond
   local est **88** (69 numeros de 19 a 88, un trou au 20), **89 libre localement**, votre
   delta 88 **au bit** (`0f8e283fa9499f96`). **Cela concorde, cela ne remplace pas.** Le
   numero se prend au depot, par l'operateur, `HEAD 39fbc89` a reverifier, corps `nn`
   jusque-la.
2. **Les nombres post hoc de A-1** (31 cellules archivees, `A(2.00)`, `7|1.45`, `7|1.55`,
   `7|2.50`, `9|2.50`) : archives G6, non versees en `.json` structure, **non re-derives**.
   Le **test aveugle** de A-1, lui, l'est entierement -- et c'est lui qui porte le fait.
3. **Vos derivations** (`a'`, `b`, `r1(p)`, `p_c`, `s_open`, la correction d'action, le
   `C_P` derive) : machinerie D1 non detenue. Je verifie leur **coherence arithmetique**
   avec les nombres qu'elles produisent -- elle tient -- **pas leur derivation**.
4. **Aucun run n'a ete ouvert** pour ce contreseing. `8|2.00` reste vierge pour son seuil ;
   P1 a p = 8 n'est pas jouee ; s0 = 0.20 et 0.30 ne sont pas rejoues (option b).

---

## 4. CE QUE J'ATTENDS

**Rien, sinon le choix (a) ou (b) du correctif D-CERT-4**, qui ne demande aucun run et
peut se decider au depot. **L'acte v2 est certifie et deposable en l'etat** : le defaut
porte sur une piece annexe, pas sur le texte qui entre au registre.

Si l'operateur prefere l'homogeneite de la serie `C_P` au registre plutot que sa
declaration, l'option (a) de D-CERT-1 reste a ma main : **deux colonnes, s0 = 0.20 et
0.30 a `T >= 4 x` borne haute**, et vous en ferez une v3 par un hunk. Je ne l'ouvre pas
de moi-meme.

-- FIN --
