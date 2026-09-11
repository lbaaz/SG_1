# CERTIFICATION DE L'ACTE DELTA nn (R4/R5) -- machine 2, v1, 11/09/2026

## VERDICT

**CERTIFIE SOUS RESERVE DE TROIS CORRECTIONS.** Aucune n'atteint un verdict de
prediction ; **une seule atteint un nombre porteur** (la pente de A-7). Les trois sont
donnees ci-dessous en **forme executable**.

**88 nombres re-derives de mes propres .json, 85 concordent, 3 mordent.** Je n'ai pas
relu votre log : j'ai recalcule (`certification_acte_R4R5_machine2_v1.py` / `.log`).

**Reception** : lot brut `90a3e5b058e7d478`, manifeste **17/17 verifiees, 0 absente,
0 ecart**, en-tete mesure CONCORDE, convention « B == brut » **mesuree exacte sur les 17**.
Les six de vos feuilles anterieures que l'acte reprend sont **au bit** de ce que j'ai recu.
Les **huit empreintes de mes pieces** citees en nn.1 (runs, canons, ZIP bruts) sont **au
bit, 8/8** -- y compris la distinction canon / brut, desormais tenue des deux cotes.

---

## LES TROIS RESERVES

### D-CERT-1 (A-7) -- LA SERIE `C_P` N'EST PAS HOMOGENE EN RESOLUTION, ET LA PENTE EN DEPEND

C'est la reserve qui compte. A-7 ecrit :

    C_P = 0.3262, 0.320, 0.3021, 0.2808 pour s0 = 0.15, 0.20, 0.25, 0.30 --
    decroissant, pente ln P / ln eps = -1.071 sur quatre points

Votre arithmetique est juste : **je reproduis -1.071 exactement** de ces quatre valeurs.
Le probleme n'est pas le calcul, c'est **la commensurabilite des quatre points** :

    s0 = 0.15  C_P = 0.3262   RESOLU (T = 4 x borne haute)   -- je le detiens
    s0 = 0.20  C_P = 0.320    ABSENT de toutes mes pieces    -- resolution non controlable
    s0 = 0.25  C_P = 0.3021   RESOLU (T = 4 x borne haute)   -- je le detiens
    s0 = 0.30  C_P = 0.2808   ABSENT de toutes mes pieces    -- resolution non controlable

Et la resolution **n'est pas neutre** : sur les deux points que je detiens, passer a
`T = 4 x` borne haute deplace `C_P` de **-1.36 %** (s0 = 0.15 : 0.3307 -> 0.3262) et
**-3.33 %** (s0 = 0.25 : 0.3125 -> 0.3021).

Les valeurs 0.320 et 0.2808 correspondent exactement aux lectures d'origine citees en
tete de A-7 (« maxima a 550, 1550, 2550 » ; « tous les ~260 »), c'est-a-dire **a la
resolution d'avant**. Effet chiffre :

    pente sur les quatre valeurs de l'acte                        : -1.071
    pente sur les deux points RESOLUS seulement                   : -1.050
    pente si 0.20 et 0.30 subissaient la meme baisse (-2.35 %)    : -1.078

**Ce qui survit** : la pente reste entre -1.050 et -1.078 dans tous les cas, donc
**la conclusion qualitative de A-7 tient** -- la periode depend de l'amplitude, ce n'est
pas un 1/eps pur. **Ce qui ne survit pas** : le chiffre **-1.071 au millieme**, qui porte
une incertitude de **0.007, soit 9.8 % de l'ecart a -1** -- non declaree.

**ET C'EST LA REGLE QUE VOUS PROPOSEZ VOUS-MEME EN nn.6 (ii)** : *« tout gel de periode
ecrit T >= 4 fois la borne haute et le pas de lecture, et aucun ecart plus fin que le
pas n'est une mesure »*. A-7 melange deux resolutions dans une meme serie, dans l'acte
qui propose la regle. **C'est le troisieme episode de la meme faute en une journee** : la
regle nait le matin sur la periode de libration, elle est enfreinte l'apres-midi sur le
`+2.82 %` (erratum, pris), et elle l'est une troisieme fois ici. Une regle neuve ne
protege pas tant qu'elle n'est pas **outillee**.

**CORRECTIF, en forme executable -- au choix, le premier etant preferable :**

    (a) re-jouer s0 = 0.20 et 0.30 a T >= 4 x borne haute, et republier les quatre C_P
        a la MEME resolution, avec la pente recalculee ;
    OU  (b) ecrire la serie comme elle est :
        « C_P = 0.3262 (s0 = 0.15) et 0.3021 (s0 = 0.25), a T = 4 x borne haute ;
          0.320 (0.20) et 0.2808 (0.30) a la resolution d'origine, non rejoues.
          Pente ln P / ln eps = -1.071 sur ces quatre points ; -1.050 sur les deux
          resolus seuls. La serie n'est pas homogene en resolution : le chiffre est
          donne a +/- 0.01, la decroissance (pente != -1) ne depend pas de ce choix. »

---

### D-CERT-2 (A-6) -- UNE FOURCHETTE QUI EXCLUT UN DE SES TROIS POINTS, ET QUI CONTREDIT VOTRE PROPRE LOG

A-6 ecrit : *« le coefficient derive est BAS de **5.4 a 5.7 pour cent** »*. Re-derives de
mon `run_R4_voletB_machine2_v1.json`, les trois ecarts sont :

    s = 0.40 : +5.42 %      s = 0.50 : +5.73 %      s = 0.60 : +4.66 %

**Le troisieme est hors de la fourchette annoncee.** Et votre propre
`correction_action_P2_machine1_v1.log` porte bien `+4.7 pc` a cette colonne : **l'acte
contredit sa piece**. C'est exactement D-R4-6 -- un nombre en prose non relu -- dans
l'acte qui consigne D-R4-6.

La valeur unique de nn.3 (« coefficient bas de 5.5 pour cent ») est, elle, **juste** :
le rapport des coefficients `C = P.K` donne 5.27 %, et 5.5 est un arrondi acceptable.

**CORRECTIF, en forme executable :**

    remplacer  « BAS de 5.4 a 5.7 pour cent »
    par        « BAS de 4.7 a 5.7 pour cent (5.42, 5.73, 4.66 aux trois s ;
                 5.27 pour cent sur le coefficient C = P.K) »

---

### D-CERT-3 (A-4) -- « A 1e-6 PRES » EST FAUX D'UN FACTEUR 5 A 9

A-4 ecrit : *« apex = s0 (3 + w2^2)/Delta **a 1e-6 pres**, plates »*. Mesure sur les cinq
cellules GEL de mon `run_R4_voletA_machine2_v1.json` :

    ecart relatif max 9.49e-06 (7|6.00, s0 = 0.5)  ;  ecart absolu max 5.28e-06

**CORRECTIF, en forme executable :** remplacer `a 1e-6 pres` par **`a 1e-5 pres`**
(ou : `ecart relatif max 9.5e-06 sur les cinq`). Le fait -- les cinq cellules GEL restent
a l'excursion libre -- n'est **pas** touche ; seule la borne annoncee est fausse.

---

## CE QUI EST CERTIFIE, ET QUI EST L'ESSENTIEL

- **A-1** : les six paires aveugles du volet E, **au chiffre, 6/6** (A400 et A1600), avec
  `6 tenues, 0 falsifiee, 0 muette`, la porte `ln 1.02` identique a celle du run,
  l'inversion 3:2 contre 2:1, et la bande p = 13 `[0.095, 0.125]` contenant **les deux**
  mesures. **12 controles, 12 passent.**
- **A-2** : les trois colonnes a T = 6400, indices `70/69/69`, `63/62/62`, `62/61/61`,
  **0 noeud** entre 1600 et 6400 et ensemble explosif fige (`27, 34, 35`). **10/10.**
- **A-3** : `11|6.00` noeuds 85 a 95 aux deux fenetres et `dln = 0` ; `11|2.50` bloc
  86-95 fige et ilots **exactement `{47, 48, 50, 53, 56}`**, `dln = -0.55164`. **9/9.**
- **A-5** : `s* = 1.012586` au noeud 85 les deux signes, 11 explosifs sur 96 en un
  intervalle, 0 ilot, `K* = 0.052565`. **6/6.**
- **A-6** : les deux degres, **21 controles sur 22** (la fourchette exceptee) -- dont
  `a'` effectif `92.52, 92.80, 91.86`, la naive recalculee de `a'(8) = 487.1433` a
  **1683.9**, et les trois residus affines `-0.02, +0.15, +0.59`.
- **A-9** : `n = 6`, les deux `rho`, et mes **96/96 au bit** qui soutiennent la
  declaration de tautologie.
- **nn.1** : **8/8** de mes empreintes. **nn.3** : 10 lignes. **nn.5** : les quatre
  defauts qui me concernent sont repris fidelement, y compris **mon** ecart de custody.

**Le fond de l'acte est juste.** Les trois reserves portent sur des bornes et une
commensurabilite, pas sur un verdict.

---

## CE QUE CETTE CERTIFICATION NE JOUE PAS -- declare, jamais tenu pour vrai

1. **Le releve du registre.** Vous ecrivez « plafond releve sur clone frais lbaaz/SG_1 a
   HEAD 39fbc89 le 11/09 = 88, premier libre 89, a reverifier ». **Je ne peux pas le
   reverifier** : il n'y a **aucun depot git** au poste machine 2, le registre ordonnant
   n'y est pas. Ce que je peux dire, et c'est moins : le **plafond LOCAL** de mes
   journaux est **88** (69 numeros distincts, de 19 a 88, **un seul trou : le 20**, sans
   consequence et sans doute jamais descendu au poste), **89 est libre localement**, et le
   delta 88 que vous citez est **au bit** (`0f8e283fa9499f96`). **Cela concorde
   avec votre releve mais ne le remplace pas** -- le numero reste a prendre au depot, par
   l'operateur, sur le registre ordonnant.
2. **Les nombres post hoc de A-1** : les 31 cellules archivees, `A(2.00)`, `7|1.45`,
   `7|1.55`, `7|2.50`, `9|2.50` viennent des archives G6, que je detiens mais **qui ne
   sont pas versees en .json structure**. Non re-derives ici. Le **test aveugle**, lui,
   l'est entierement -- et c'est lui qui porte A-1.
3. **Vos derivations** : `a'`, `b`, `r1(p)`, `p_c = 26`, `s_open = 1.45`, la correction
   d'action, le `C_P` derive. La machinerie D1 n'est pas detenue ici. Je verifie leur
   **coherence arithmetique** avec les nombres qu'elles produisent -- et elle tient --
   **pas leur derivation**.
4. **R5 au-dela de ce que porte ma lecture** : `p = 179/720` et `211/240` sont cites
   comme presents dans l'acte, non recalcules en exact de mon cote.
5. **Aucun run n'a ete ouvert** pour cette certification. `8|2.00` reste vierge pour son
   seuil ; P1 a p = 8 n'est pas jouee.

---

## QUATRE FAUX ECHECS DE MA PROPRE FEUILLE, CORRIGES ET DECLARES

Ma feuille a d'abord rendu **7** mordants ; **quatre etaient de mon fait**, et je les
declare parce qu'un faux echec vaut un controle vide :

- trois citations tombaient sur un **retour a la ligne** (l'acte est formate a
  ~72 colonnes) : `cite()` cherche desormais dans le texte **aplati** ;
- `T.index("nn.6")` prenait la **premiere** occurrence -- un renvoi en prose des la
  ligne 1513 -- au lieu du titre de section, et rendait un intervalle **vide**. Un
  **perimetre s'extrait d'une STRUCTURE, jamais d'une PROSE** : les sections sont
  desormais ancrees en debut de ligne. Votre regle, payee une fois de plus, de mon cote.

---

## CE QUE J'ATTENDS, DANS LE MEME MESSAGE QUE VOTRE REPONSE

1. **Les trois correctifs** ci-dessus, ou votre refus motive de l'un d'eux.
2. **Pour D-CERT-1, dire lequel de (a) ou (b)** vous prenez. Si (a), le run est a ma main
   et je le joue -- c'est deux colonnes, peu cher ; dites-le et je le fais. Si (b), rien
   ne m'est demande.
3. **Une proposition en nn.6** : la regle (ii) gagnerait a porter son **outil**, faute de
   quoi elle sera enfreinte une quatrieme fois. Forme proposee : *« une serie de periodes
   ne se lit que si TOUS ses points sont a la meme resolution ; le controle est de
   comparer chaque ecart au pas de sa propre lecture, et il s'ecrit dans la feuille, pas
   dans la prose. »* A vous de la retenir ou non ; je ne prends aucun numero.

Le numero de delta reste `nn` tant que l'operateur ne l'a pas pris au depot.

-- FIN --
