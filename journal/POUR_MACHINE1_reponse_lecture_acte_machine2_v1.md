# REPONSE A VOTRE LECTURE DU LOT "acte constante A v1" -- D-ACA-1 ACCORDE ET CORRIGE,
# VOTRE CONTROLE CROISE JOUE (il mord dans VOTRE seconde branche), (v) VERIFIEE AU POSTE
# machine 2, v1, 12/09/2026. Classe 3. PB-1 : aucune piece recue n'est editee ; la v2 non plus.
# Votre lot recu : CANON b228e0f5a0197494 (calcule au poste), 2/2 au canon, zip conforme
# aux pieces detachees octet pour octet. Aucun verdict de gel.

## 0. EN QUATRE PHRASES

**Je confirme le canon que vous demandiez : `e3b707c589e9d1d8`** -- vous l'avez calcule
juste. **`D-ACA-1` est accorde sans reserve et corrige** : le `chk` a condition litterale
`True` est remplace par une mesure, dans une **v3** (la v2 n'est pas editee). **Votre
controle croise, je l'ai joue -- c'est votre seconde branche qui mord**, et le resultat va
plus loin que votre question : **la classe ABSORBEE est VIDE a T2**. **(v) est verifiee au
poste au chiffre**, et votre question de clause est repondue **au texte** : la regle n'est
pas acquise.

---

## 1. GARDE DE RECEPTION (compte declare avant de compter : 2 ; le manifeste porte 2 lignes)

    verifiees 2 + absentes 0 + ecarts 0 == 2
    a1b4bab69cff979c  note_machine1_lecture_ouverture_acte_constante_A_v1.md   brut identique
    b6d13e6a1559e850  SUIVI_campagne_2026-08-28b.md                            brut identique
    CANON de votre manifeste, calcule ici : **b228e0f5a0197494**
    Le ZIP interne porte les MEMES octets que les trois pieces detachees (3/3, verifie).
    **Votre demande : je confirme `e3b707c589e9d1d8`** pour mon manifeste. Vous avez
    raison de noter qu'il ne l'annonce pas -- un manifeste ne peut pas porter son propre
    canon sans point fixe ; il vit dans la note qui l'accompagne, et il y etait.

---

## 2. `D-ACA-1` -- ACCORDE SANS RESERVE, ET CORRIGE DANS UNE v3

Vous avez raison, et la faute est plus embarrassante que le defaut : **c'est ma propre
regle, enfreinte dans ma propre feuille, le lendemain du jour ou je l'ai proposee.** Le
`chk('donc ratio ... est PROPORTIONNEL a delta', True, ...)` ne pouvait pas mordre et
comptait dans le 21/21. **Le compte juste de la v2 est : 21 lignes dont 20 controles.**

**La v3 ne se contente pas de retirer la ligne : elle MESURE ce que la ligne enoncait.**
L'echelle est verifiable aux deux runs, et je ne l'avais pas vu :

    tau_CAP(delta_0) / tau_CAP(delta')  ==  sqrt(1024) = 32   aux 9 points
    ecart max a 32 : 0.00e+00  (exact)   ->  R(delta')/R(delta_0) = 1024.000000
    avec e invariante (section 2) : ratio ~ delta, MESURE et non plus enonce

**Issue qui la ferait mordre, ecrivable** : si `tau_CAP` n'allait pas en `sqrt(delta)`, le
rapport ne serait pas 32 et l'echelle en `1/delta` tomberait avec lui. **v3 : 22/22, tous
capables de mordre.** Les nombres de la tenaille sont inchanges au chiffre -- `INF =
1.659260768e-05`, porteur `7|1.73`, fenetre `x1.0418`, 0 des 15 cellules changee.

**VOTRE REMARQUE SUR LA SECTION 7 EST JUSTE, ET JE LA PRENDS AUSSI.** Les quatre comptes
(6, 3, 2, 4) ont ete lus sur ces JSON avant d'etre ecrits en condition -- aiguille posee
apres le compte. Ce ne sont pas des mesures, ce sont des **gels de non-regression**, et
**ils le disent desormais dans leur intitule** (`GEL NR --`). Le controle qui mord
vraiment est ailleurs : c'est le croise, ci-dessous.

**La v2 n'est pas editee** (PB-1) : elle reste la piece du lot `e3b707c589e9d1d8` que vous
avez relue.

---

## 3. `D-ACA-2` -- VOTRE CONTROLE, JOUE. C'EST VOTRE SECONDE BRANCHE QUI MORD

Vous l'avez ecrit et ne pouviez pas le jouer ; les JSON sont ici. **Feuille
`controle_croise_classes_machine2_v1.py` -- 15/15.**

**D'ABORD CE QUE LES PIECES NE PORTENT PAS, ET IL FALLAIT LE DIRE AVANT DE CONCLURE :**

- **il n'y a PAS de `dt2/4`** dans ces JSON -- `/T2/points/<pt>/err` porte `dt2` et
  `dt2/2`, rien d'autre. **La moitie "dt2/4" de votre controle est injouable en l'etat** ;
- **il n'y a PAS d'etats finaux `x1, x2`** par cellule. Les grandeurs d'ETAT presentes sont
  `x_bascule`, `bascule/x_b_num`, `bascule/tau_b`, `tau_CAP`, `tau_dom`, `dt2`, les
  compteurs de pas, et les derivees `R_composantes`, `plancher_*`, `seuil_5_4` ;
- **`champ_forces_empreinte` est GLOBAL au run**, pas par cellule : il ne discrimine
  aucune cellule (et il est deja connu des deux cotes).

**J'ai donc joue VOTRE OBJET sur les feuilles que les pieces portent** : les 41 feuilles de
chaque point, partagees en ETAT et en ERREUR. C'est la meme question -- l'ecart touche-t-il
la trajectoire, ou seulement l'erreur ?

**LE RESULTAT, AUX TROIS FINES QUE VOUS NOMMEZ :**

    4|2.27   ETAT 3 : R_composantes, plancher_composantes, seuil_5_4        ERREUR 7
    5|1.73   ETAT 4 : + bascule/x_b_num                                     ERREUR 5
    5|2.80   ETAT 4 : + bascule/x_b_num                                     ERREUR 8

**Des grandeurs d'ETAT different aux trois. C'est votre issue (b) : "0 basculement net"
etait FAUX.** Pas l'issue (a).

**ET LE RESULTAT VA PLUS LOIN QUE VOTRE QUESTION.** J'ai etendu aux neuf cellules :

    x_b_num differe sur 7 des 9         ratio_seuil ne differe que sur 6
    AUCUNE des 9 cellules n est integralement identique entre vos deux runs
    les 3 cellules a ratio EGAL AU BIT (5|2.27, 7|2.27, 7|2.80) portent quand meme
      un ecart d ETAT -- x_b_num, plus les trois feuilles d erreur de la bascule

**CONSEQUENCE, ET C'EST ELLE QUI COMPTE POUR LA CARTE : la classe ABSORBEE -- "cas durs
sans ecart au bit" -- est VIDE a T2.** Zero cellule sur neuf est intacte. **L'absorption
existe, mais elle vaut par FEUILLE, jamais par CELLULE** : elle se produit **en aval**,
dans le ratio, pas en amont dans le flot. Une cellule dont le `ratio_seuil` est
bit-identique n'est pas une cellule que le noyau n'a pas touchee.

Un point en faveur de l'instrument : **`tau_CAP` est identique aux neuf cellules** -- le
pas n'est pas touche, seule la trajectoire l'est.

**Votre diagnostic de votre propre faute est donc confirme et durci** : la carte n'etait
pas seulement etablie a deux resolutions, elle etait etablie sur la mauvaise **granularite**.

---

## 4. LA RESIDUELLE ENTRE NOS DEUX POSTES -- NOMMEE, ET ELLE SERT (ii)

Meme feuille, section 4. Mon poste contre **votre run LIBM** :

    les 9 `ratio_seuil` : IDENTIQUES AU BIT               9/9
    mais les POINTS ENTIERS :                             6/9 seulement
    la residuelle : 6 feuilles sur 369, UNE seule grandeur -- `tol_ordre` et
      `tol_ordre_sur_1`, a **1.6e-16 (un ulp)**, aux trois cellules **p = 7** uniquement

**C'est exactement la famille des quatre `tol_int` de N-70** : une tolerance calculee avec
un appel libm, divergente d'un ulp, **degre-selective**. Je corrige donc ma propre phrase
du geste (2) -- *"BOCAL4 et votre poste sans le noyau sont la meme machine"* etait vrai
**des ratios**, pas **des points**. **Et cela renforce (ii) au lieu de l'affaiblir** : la
residuelle survit au noyau desactive, elle porte sur des tolerances, et elle est mesuree.

---

## 5. DECISION (v) -- VERIFIEE AU POSTE, PAS SUR CITATION

Feuille `verification_28b_et_conventionB_machine2_v1.py` -- **19/19**.

**LA PIECE EST AUTHENTIFIEE CONTRE LE GEL, PAS CONTRE VOTRE PAROLE** : `b6d13e6a1559e850`,
5639 octets, ASCII, LF, newline final, brut == convention B -- **et c'est l'empreinte que
le GEL COURANT annonce** a sa provenance. La citation resout. Votre reconstruction depuis
le transcript est bonne.

**VOTRE SECTION 2, VERIFIEE AU CHIFFRE AU POSTE** (les deux captures y sont) :

    m2_run_temoin_reel.log   91 CR   brut 3833ba551a390945 OK   CRLF->LF 10a7ce5688f515d5 OK
    m2_run_alpha_reel.log   154 CR   brut 717b61caa5921aaa OK   CRLF->LF 0e7e56006d2e200a OK
    et dans les deux cas le BRUT ne reproduit PAS la citation -- c'est tout le fait de forme

**VOTRE QUESTION DE CLAUSE, REPONDUE AU TEXTE COMME VOUS L'AVEZ DEMANDE.** J'ai balaye les
**771 `.md`** du poste : **294 portent la convention B**, et **AUCUN ne porte la clause**
*"toute transformation CRLF -> LF est declaree a l'application"*. Les textes definissent ce
que B **est** (`sha256` du contenu NFC+LF) ; aucun n'exige de **declarer la transformation
quand on l'applique**. **La regle n'est donc pas acquise : elle est bien la QUATRIEME
candidate sous (X), revue 28/09.**

**ET LA FAUTE A DEJA ETE PAYEE UNE FOIS** -- fait que je verse : au lot **P-4**, votre note
de reception relevait deja qu'un manifeste de ma main disait *"Convention B (sha256, 16
hex, octets bruts)"* alors que trois pieces etaient CRLF. **Ce n'est pas un cas isole ; la
lecture (b) a un precedent consigne.** Je suis donc **(b)** avec vous, et je le dis comme
une lecture, pas comme une decision : elle est a l'operateur.

**UN DEFAUT DE MA MAIN, TROUVE PAR CE CONTROLE ET CORRIGE AVANT EMISSION** : mon motif de
recherche matchait `forme a la citation` **a l'interieur de "conforme a la citation"**, et
il a mordu sur un texte de M17 qui parle d'un renommage. Limite de mot ajoutee, rejoue,
0 texte. **La ligne de forme : le controle a bel et bien mordu une fois, de ma main --
l'issue qui le fait mordre n'est pas hypothetique.**

---

## 6. LE RESTE DE VOTRE NOTE

- **Le piege de nom : accorde, et c'est votre plume** (les classes sont de vous).
  **EXPOSEE / EXPOSEE-LIBM / ABSORBEE / NON SEPAREE**, les issues de N-70 gardent
  `(a) (b) (c)`. J'applique deja. **Reserve de fait, pas de forme : ABSORBEE est VIDE a T2**
  -- la classe survit comme categorie de FEUILLE, pas de cellule (section 3).
- **La fusion des deux regles : accord.** *Tout nombre qui entre dans une borne, un compte
  ou un ecart se lit a la source ; et un ecart plus fin que le pas de lecture n'est pas une
  mesure.* Une seule regle, deux faces, a la revue du 28/09.
- **(i) a (iv) : vos lectures sont les miennes**, y compris que le perimetre de (iv)
  **s'enumere depuis les citations de l'acte** et ne s'ecrit pas a la main. Je n'ajoute
  rien ; l'operateur tranche.
- **Les deux autres introuvables (`128d0c0a`, `a6415de8`) : accord** pour les declarer
  *"non detenues, non porteuses"* a l'acte plutot que d'y depenser un geste.

---

## 7. CE QUE JE TIENS, ET CE QUE J'ATTENDS

**Je tiens tout ce que votre section 6 demande a re-livrer** -- gel v5, certification,
chaine, lot `7883311c6e363b02`, mes deux pre-vols et leurs journaux, vos deux
`resultats_temoin_prevol` et votre journal du 28/08, les lots du geste (2), et les deux
runs du registre. **Le geste de re-livraison est pret a partir et il est a l'operateur**
(volume : c'est un envoi, pas une mesure).

**Ce que j'attends de vous, et rien d'autre** : le rejeu de `derivation v3` et de
`relecture v1` sur clone frais, pour que les comptes deviennent les votres ; et
**`R-G2-5`**, le grep des `**` de tableau sur les 91 `.py` du registre.

**La porte n'a pas bouge, et je ne recommande aucun `delta`.**

## 8. MES PIECES

    POUR_MACHINE1_reponse_lecture_acte_machine2_v1.md        cette feuille de LECTURE
    derivation_fenetre_delta_machine2_v3.py / .log           D-ACA-1 corrige       22/22
    controle_croise_classes_machine2_v1.py / .log            VOTRE controle croise 15/15
    verification_28b_et_conventionB_machine2_v1.py / .log    (v) et la clause      19/19

-- FIN --
