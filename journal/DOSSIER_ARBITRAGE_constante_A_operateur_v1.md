# DOSSIER D'ARBITRAGE -- CONSTANTE A : LES CINQ DECISIONS
# machine 2, v1, 12/09/2026. A LA MAIN DE L'OPERATEUR.
# Classe 3. Rien n'est edite (PB-1). Aucun verdict de gel ; la tenaille n'est pas lue
# comme gel. Feuille de MESURE jointe et rejouable, separee de cette feuille de LECTURE :
#   derivation_fenetre_delta_machine2_v2.py / .log   -- 21/21 controles PASSENT
# Dossier source verifie au poste le 12/09 : gel v5 lot d5ace962a3a6e413 (gel
# 2c0d2dc86054838c, GEL COURANT), certification machine 2 13d2973b0e143a20 (104/104),
# chaine a4c35a2ee691c9a7 (8 pieces), feuille de tenaille v1 lot 7883311c6e363b02.

## 0. EN QUATRE PHRASES

La suspension est levee : le point qui bloquait le banc -- la convergence en dt a
`7|1.73` -- est livre, et **la borne retenue est intacte**. La correction `D-G2-4` est
**appliquee et mesuree** : `INF = 1.659260768e-05`, **aucun changement de statut**.
**Quatre des cinq decisions sont tranchables aujourd'hui ; la cinquieme ne l'est pas**,
et pour une raison qui n'est pas un arbitrage -- la piece dont elle sort est introuvable.
**Rien de ce qui suit ne bouge la porte** : le pre-vol rend branche 4, et l'arbitrage du
29/08 reste entier et a vous.

---

## 1. LA TENAILLE, RE-DERIVEE EN PLEINE PRECISION -- `D-G2-4` EST APPLIQUEE

La v1 lisait les ratios `e/seuil` dans les **journaux**, ou ils sont imprimes a **trois
decimales**, puis divisait `delta'` par ce nombre tronque. La v2 les lit au champ
`/T2/points/<pt>/ratio_seuil` des **JSON**. La definition de la borne retenue est
inchangee : `INF = max(borne(R_MOI, True))`.

**Le champ du JSON porte bien la grandeur que le log tronque** -- ce n'est pas suppose,
c'est mesure : `ratio_seuil == e(dt2/2) / seuil_5_4` **au bit, 9/9**, et arrondi a trois
decimales il retrouve mon journal **9/9** et le sien **9/9**.

    porteur 7|1.73 :   log 0.684   ->   JSON 0.68419170555697806

**LES QUATRE LECTURES** (la plus dure est retenue ; la lecture LIBM est neuve -- ses deux
JSON sont arrives au poste avec la cloture du geste (2), sa ligne quitte donc elle aussi
les trois decimales) :

    machine 1 -- son run a NOYAU        delta >= 1.286193025e-05   (x1.3171)   7|1.73
    machine 1 -- son run a LIBM         delta >= 1.427322916e-05   (x1.4616)   7|1.73
    machine 2 -- mes ratios             delta >= 1.427322916e-05   (x1.4616)   7|1.73
    CONSERVATRICE (e = min des deux)    delta >= 1.659260768e-05   (x1.6991)   7|1.73
    volet A, borne superieure a m=2     delta <= 1.728646463e-05               p=5

**Sa lecture LIBM et la mienne rendent le MEME nombre** -- les neuf ratios sont
**identiques au bit**. Le doute des 11 % ne survit pas a la lecture des JSON.

**CE QUE LA CORRECTION DEPLACE, ET CE QU'ELLE NE DEPLACE PAS** :

    INF v1 (depuis le log)   1.659725811e-05
    INF v2 (depuis le JSON)  1.659260768e-05
    ecart relatif            2.8027e-04
    marge de la fenetre      4.1817e-02      -> l'ecart est 149 x plus petit
    cellules de la carte qui changent de statut : 0 sur 15

    kT    |      m=1       m=2       m=3
    1.00  |  x2.0836   x1.0418      VIDE
    1.15  |  x1.8119      VIDE      VIDE
    1.30  |  x1.6028      VIDE      VIDE
    1.50  |  x1.3891      VIDE      VIDE
    1.74  |  x1.1975      VIDE      VIDE

**LA BORNE RETENUE NE LIT AUCUN NOMBRE DE MACHINE 1, ET CE N'EST PLUS UNE LECTURE DE
CODE : C'EST UNE MESURE.** Toute la chaine qui mene a la borne est enfermee dans une
fonction appelee **deux fois** -- une fois sur ses JSON recus, une fois sur des copies
dont tous les `ratio_seuil` et tous les `e` sont mutes (x3 et x0.5). `INF` sort
**inchange au bit** (`3ef1660b5147653b`), le porteur inchange, **et la mutation deplace
bien sa lecture affichee** (`1.286193025e-05 -> 4.287310084e-06`) -- sans ce troisieme
controle la jambe ne prouverait rien.

**La porte, pour memoire** : `delta' = 9.765625e-06`, soit **0.589 x INF**. Sous la borne
inferieure, comme le 29/08.

---

## 2. CE QUE LA RE-DERIVATION A TROUVE EN PLUS, ET QUE PERSONNE N'AVAIT DEMANDE

L'erratum du geste (2) compte **TROIS** cellules divergentes entre mon poste et son run a
noyau. **Au bit elles sont SIX.**

    4|1.73   1.6517184720338571   vs 1.6138361632355356   2.3e-02   LUE
    4|2.27   2.1211818941156584   vs 2.1211819239061085   1.4e-08   LUE
    4|2.80   2.2729904350723991   vs 2.379096193902754    4.7e-02   LUE
    5|1.73   0.9914845667750477   vs 0.99148457088479625  4.1e-09   non lue
    5|2.80   1.4686543965472436   vs 1.4686543971742234   4.3e-10   LUE
    7|1.73   0.68419170555697806  vs 0.75926589622204754  1.1e-01   non lue

**Le compte de l'erratum avait ete etabli sur les LOGS** : les trois qui manquaient
divergent de 1.4e-08, 4.1e-09 et 4.3e-10 -- **invisibles a trois decimales**. C'est
**exactement la maladie de `D-G2-4`, a un autre endroit du meme dossier** : deuxieme
instance en un jour, et celle-la n'avait ete vue par personne.

La separation est **nette** -- aucune cellule entre 1e-07 et 1e-02 -- et les **six**
s'annulent contre son run LIBM, donc **les six sont du noyau**, pas trois. Le compte juste
est : **six au bit, dont quatre LUES ; trois a la resolution du journal, dont deux LUES**.

**Ce que cela ne change pas** : la borne. Le porteur reste `7|1.73`, et il reste **la
seule des trois grossieres qui ne soit pas lue**. **Ce que cela change** : l'erratum du
geste (2) doit etre corrige avant d'aller au registre, et il a besoin d'un numero --
voir la decision **(iii)**.

---

## 3. DECISION (i) -- LD-16 / DEPOT

**L'OBJET.** Le depot 9bis CLOS embarque les feuilles de **LECTURE** de LD-16
(`/T1`, `/T3a` : `plancher_dt2 = c_pl x eps x N`, statuts `MORD` / `NON LUE`). Toute
LD-16bis change ces feuilles et fait **mordre 9bis sur chaque run legitime** : la custody
tuerait l'instrument qui s'ameliore.

**L'ETAT AU 12/09.** `D-v5-1`, verse par machine 1, est ouvert. La decision est versee au
code (commentaire sur `C_PL`, constante confinee et renommee `c_pl_ld16_herite`). Deux
issues sont sur la table : **depot re-ancre sur un run v8 depose**, ou **LD-16bis en v9**.

**CE QUI A CHANGE DEPUIS LE 29/08.** L'instrument est passe v5 -> v8 et **le v8 est
CERTIFIE** : l'issue qui se lisait "re-ancrage sur un run v5" se lit desormais
"run v8". `D-I-3` est levee. Rien d'autre n'a bouge, et le geste (2) ne touche pas
cette decision.

**CE QU'IL LUI MANQUE -- ET CE N'EST PAS UN ARBITRAGE, C'EST UN PREALABLE.**
**Il faut d'abord dire SOUS QUEL GEL LD-16 LIT AUJOURD'HUI.** La docstring de LD-16 fonde
son plancher sur "la clause de 5.4, W-plancher" -- clause que **la v11 a abrogee**.
LD-16 n'est donc pas seulement *heritee* : elle est **ancree sur une clause qui n'existe
plus**. Et le v5 emet `c_pl_ld16_herite: 10` au reglage du JSON -- **un run depose sous la
v11 porterait une constante que son propre gel declare retiree "et remplacee par aucune
autre"**. Les deux issues se choisissent apres cette phrase, pas avant.

**A VERSER AU MEME ENDROIT** (avertissement du 29/08, contresigne) : **(c) de N-70 et (i)
voyagent ensemble mais ne se substituent pas.** Un re-ancrage produit une reference issue
d'UNE machine ; le controle compare toujours au bit ; l'autre machine divergera pareil.
**Le re-ancrage ne leve pas la dependance machine -- il en change le titulaire.**

**MA PLUME.** Le prealable est une question de **gel**, pas d'instrument, et je ne le
tranche pas. Je recommande seulement de **l'ecrire avant de choisir l'issue** : re-ancrer
sur un gel dont la portee est indeterminee, c'est deposer le probleme au lieu de le
solder.

---

## 4. DECISION (ii) -- ISSUE N-70 (a/b/c)

**L'OBJET.** Quatre cles portent un appel libm **a l'interieur** du perimetre 9bis :
`/T1/A/W_integrales/tol_int(_sur_1)` et `/T3a/A/tol_int(_sur_1)`. La grandeur est
`tol_int = log2((1+b)/(1+b/2))`, `b = sqrt(omega2)*dt` ; **`b` est identique au bit des
deux cotes**, l'ecart nait de `log2` et `sqrt`.

**L'ETAT AU 12/09, ET IL EST PARTICULIER : L'ISSUE (a) EST DEJA LE CAS DE FAIT.**
`registre/runs/run_temoin_delta85/resultats_temoin.json`, **piece deposee**, porte
`0.008578984888782988` sur les huit cles `tol_int` -- **la valeur machine 2**. Machine 1
rend `...986`. Un run du volet T joue chez elle ferait mordre la custody 9bis **avant
toute lecture**, pour une raison qui n'a rien de physique. Personne ne l'a decide ni
ecrit ; c'est inscrit dans un depot.

**CE QUI A CHANGE -- C'EST LA DECISION QUE LE GESTE (2) ALIMENTE LE PLUS.** La
reproduction au bit entre machines a desormais **quatre classes mesurees** : exposees au
noyau ; **sensibles a la libm elle-meme** (le champ de forces a TROIS valeurs, pas deux) ;
tenues par **absorption** (fortuit) ; non separees. Plus une **residuelle glibc/UCRT a un
ulp** sur dix tolerances.

**LA CONSEQUENCE CONTRAINT L'ISSUE, ET ELLE EST MESUREE, PLUS PREFEREE : le 9bis entre
machines COMPARE A TOLERANCE OU IL EXEMPTE. Il ne peut pas exiger le bit, MEME NOYAU
DESACTIVE.** Lecture des trois issues a la lumiere de cela :

    (a) le run se joue sur MACHINE 2 -- aucun texte ne bouge, mais cela FERME la porte
        a tout run inter-machines, et rend definitive une contrainte aujourd'hui
        silencieuse. C'est deja l'etat de fait ; la decision ne ferait que l'ecrire.
    (b) les quatre cles entrent aux EXEMPTIONS -- ce sont des tolerances mesurees, pas
        des durees : cela affaiblit le controle a l'endroit ou il mesure.
    (c) le 9bis acquiert une TOLERANCE pour les cles portant un appel libm -- meme
        remede que 7 (i), autre patient ; la seule qui ne cache rien, la plus couteuse,
        et desormais **la seule que la mesure du geste (2) rende suffisante** pour un
        instrument portable entre machines.

**UN PIEGE DE NOM, A TRANCHER AU MEME GESTE.** Les **issues** de N-70 s'appellent
`(a) (b) (c)` et les **classes** mesurees au geste (2) s'appellent `(a) (a') (b) (c)`.
Deux jeux de lettres, meme dossier, et ils vont se croiser dans la meme phrase au
registre. **Renommer l'un des deux avant le depot**, sinon la campagne paiera la
collision comme elle a paye le "v12" de M17.

**CE QU'IL LUI MANQUE.** Rien de mesure. C'est un arbitrage, entier.

**MA PLUME.** **Aucune issue a ma plume** -- declare le 29/08, je m'y tiens : je controle,
je ne choisis pas le regime de l'instrument qui me controlera. Je verse la contrainte
mesuree et le piege de nom, rien de plus.

---

## 5. DECISION (iii) -- NUMERO DE L'ERRATUM 7 (i), A L'ACTE

**L'OBJET.** `erratum_temoin_v11_clause_7i_tolerance_v1.md` complete le gel v11 **sans
l'editer** (`a2e7ef3e237c5acf` inchange, meme forme que l'arbitrage operateur du 28/08).
Il borne la clause 7 (i) : tirage identique au bit, champ a `x'' <= 2 ulp` et
`D'' <= 2 ulp` en pas representables, au-dela W-transcription MORD -> BANC NON JOUE.

**L'ETAT AU 12/09.** La piece existe et elle est **absente du registre** -- comme toute la
chaine de la constante A (voir la decision (iv)). Les deux bornes valent 2 **pour des
raisons differentes**, les effets sont orthogonaux, et le regime de 7 (i) les cumule ;
c'est declare **MESURE, NON PROUVE**.

**CE QUI A CHANGE.** Rien pour 7 (i) lui-meme. **Mais un second erratum est ne
aujourd'hui** : le compte de trois cellules qui en fait six (section 2). Il est de la
**meme famille** (un compte lu sur un journal tronque) et il doit etre numerote **au meme
geste** -- sinon deux errata voisins partent au registre dont un seul a un numero, et le
second se perdra comme s'est perdu le "seul point" dans un champ de detail.

**CE QU'IL LUI MANQUE.** Rien. **Tranchable immediatement**, et c'est la moins couteuse
des cinq.

**MA PLUME.** A trancher **avec (iv)**, meme geste, meme depot : un numero d'erratum sans
depot ne sert a rien, et un depot groupe qui laisse un erratum sans numero se refera.

---

## 6. DECISION (iv) -- DEPOT GROUPE (X). **C'EST LA PLUS URGENTE, ET ELLE EST DATEE.**

**L'OBJET.** Le calendrier de depots groupes sous (X).

**L'ETAT AU 12/09 -- LE REGISTRE EST A CINQ CRANS EN ARRIERE.** Verifie contre
`origin/main` au 09/09, apres le depot du delta 88 :

    gels/      temoin_negatif_pre_enregistrement  v5, v6, v7   -- le gel qui FAIT FOI : v11
    scripts/   banc_qualification_machine1        v1, v2, v3   -- l'instrument CERTIFIE : v8
    constante_A_pre_enregistrement                AUCUNE version au registre
    enumeration_cles_prevol_N70                   ABSENTE
    erratum_temoin_v11_clause_7i                  ABSENT
    depot_9bis_temoin_v1.json                     ABSENT

**Toute la chaine de la constante A vit hors registre.** Ce n'est pas une faute -- rien
n'a ete depose parce que le dossier n'est pas clos. Mais **un tiers qui lirait le registre
aujourd'hui trouverait un gel de volet T perime de quatre versions et un instrument perime
de cinq.**
*(Attention : `BOCAL4/registre/` est un clone LOCAL ou des pieces ont ete installees a la
main. Ce n'est pas le registre public.)*

**L'URGENCE, ET ELLE EST AU CALENDRIER.** **(X) gele le jeu de regles 30 jours, jusqu'au
28/09** ; les exceptions se comptent et le compte se lit **a la revue** ; (P) et (X)
portent elles-memes cette date. **Il reste SEIZE JOURS.** Un depot groupe qui n'est pas
fait avant la revue arrive **apres** le compte des exceptions -- et trois regles
candidates attendent d'y entrer (section 8).

**CE QU'IL LUI MANQUE.** Rien de mesure. Une decision de calendrier.

**MA PLUME.** **C'est la seule des cinq dont le retard coute quelque chose de date.** Je
recommande de la trancher en premier, avec (iii) dans le meme geste.

---

## 7. DECISION (v) -- **ELLE N'EST PAS TRANCHABLE, ET CE N'EST PAS UN ARBITRAGE**

**L'OBJET, TEL QUE LA FILE LE PORTE** : "(v) suit (iv)", "(v) sort du SUIVI 28b".

**L'ETAT AU 12/09, VERIFIE.** `SUIVI_campagne_2026-08-28b.md`, empreinte
**`b6d13e6a1559e850`**, est **cite a la provenance du gel** -- v4 (l.579) et **v5
(l.587), le gel courant** -- et il est **ABSENT du poste**. Cherche et non trouve dans
`BOCAL4/` et dans `Downloads/` de l'operateur, la ou les trois pertes precedentes avaient
ete retrouvees.

**CE QUE CELA VEUT DIRE, ET IL FAUT LE DIRE NET : je ne peux pas ecrire l'objet de (v).**
La decision existe **par reference a une piece que je n'ai pas**. Tout ce que j'en dirais
viendrait de la memoire, pas d'une piece -- et une decision dont on ne peut pas citer
l'objet ne se tranche pas.

**C'est une TROISIEME piece introuvable**, aux cotes de `128d0c0a` (derivation fenetre
T-2) et `a6415de8` (lot v9), et **celle-ci est la plus genante des trois** : les deux
autres sont des pieces de travail, celle-la est **citee a la provenance du gel courant**.

**CE QU'IL LUI MANQUE.** La piece. **A demander a machine 1**, avec les deux autres, au
message d'ouverture du prochain geste.

**MA PLUME.** Ne pas trancher (v). La reouvrir quand la piece sera au poste.

---

## 8. CE QUI ENTRE AUSSI A L'ACTE, HORS LES CINQ

- **L'ERRATUM DU "SEUL POINT"** (machine 2) -- et **sa propre correction** (section 2) :
  trois cellules au journal, **six au bit**, dont **quatre lues** depuis le 28/08.
- **`R-G2-5`** : tout `**` de tableau des instruments, **moteur compris**, est expose chez
  machine 1. **Le grep reste a faire** -- c'est le seul reste de travail du geste (2).
- **TROIS REGLES CANDIDATES SOUS (X)**, avec la reserve accordee de machine 1 (*une regle
  sous (X) porte sa date de revue ou nomme ce qu'elle remplace*) :
    1. la ligne de plateforme avec **temoin d'arrondi executable** -- `(1765.6704444885254)**6`
       rend `...9c5` / `...9c6` selon le noyau (machine 1) ;
    2. *le champ de detail ne porte aucune affirmation ; elle vit dans la condition*
       (machine 2) -- outillable : un detail qui contient "seul", "tous", "aucun",
       "jamais" est un controle deguise ;
    3. **NEUVE, du jour** : *un compte etabli sur un journal est un compte tronque ; tout
       nombre qui entre dans une borne ou dans un compte se lit a la source.* **Deux
       instances payees le meme jour** -- `D-G2-4` (la borne) et le compte de l'erratum
       (section 2).
- **LE LEVIER `NPY_DISABLE_CPU_FEATURES`**, **a arbitrer PAR USAGE** : il aligne `power`
  et `exp` sur la libm mais **degrade** `log10`, `expm1`, `log1p`, `cbrt`. Ce n'est pas un
  reglage global.

---

## 9. CE QUE JE NE TRANCHE PAS -- **LA PORTE N'A PAS BOUGE**

Le volet A **n'ouvre que sur branche 5** ; le pre-vol rend **branche 4 des deux cotes**
(W-plancher mord a 4 des 9 points, tout p = 7, `5|1.73` sur le fil). Le geste (2) n'a pas
touche cela : il a leve un **doute sur un nombre**, pas une **porte**.

**L'ARBITRAGE DU 29/08 EST ENTIER ET IL EST A VOUS :**

> **la marge du volet A, ou une marge cote T -- PAS LES DEUX.**

La fenetre existe a `m=2, kT=1` et vaut **x1.0418**. Elle est **VIDE** des que `kT >= 1.15`
a `m=2`, et **VIDE partout a `m=3`**. Et **aucun barreau de l'echelle b=4 ne tombe dans la
fenetre** : ce n'est pas la physique qui exclut le recouvrement, c'est **le choix de
l'echelle**.

**Je ne recommande aucun `delta`.** Un reglage choisi en connaissant la valeur est
precisement ce que la campagne s'interdit.

---

## 10. DETTES ET PIECES INTROUVABLES, ETAT AU 12/09

    SUIVI_campagne_2026-08-28b.md  b6d13e6a1559e850  INTROUVABLE -- cite au gel v5 (v)
    derivation fenetre T-2         128d0c0a          INTROUVABLE (dette du 09/09)
    lot v9                         a6415de8          INTROUVABLE (dette du 09/09)
    les 8 ZIP de P-4                                 non verses au registre
    MANIFEST.sha256                                  arrete au delta 80
    D-CERT-6                                         au registre en prose, sans la
                                                     feuille qui le mesure (ouvert pour
                                                     le delta 90)

**Rien n'est ouvert par ailleurs** : aucun run, aucune cellule entamee, ni chez machine 1
ni chez machine 2. Le geste (2) est **clos des deux cotes**.

---

## 11. MES PIECES

    DOSSIER_ARBITRAGE_constante_A_operateur_v1.md     cette feuille de LECTURE
    derivation_fenetre_delta_machine2_v2.py / .log    la feuille de MESURE, 21/21
    relecture_nombres_acte_machine2_v1.py / .log      les nombres de cette feuille,
                                                      relus aux sources

-- FIN --
