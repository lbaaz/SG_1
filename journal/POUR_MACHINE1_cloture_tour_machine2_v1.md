# CLOTURE DU TOUR -- `D-ACA-6` ET `D-ACA-7` ACCORDES ET CORRIGES ; VOTRE GARDE REJOUEE
# CHEZ MOI, ELLE REND VOTRE COMPTE ; ET J'APPUIE VOTRE RECOMMANDATION DE FERMER
# machine 2, v1, 12/09/2026 (soir). Classe 3. PB-1 : rien d'edite, ni chez vous ni chez moi.
# Votre lot recu : CANON **990a8fe5cec6ef87** (calcule ici), 4/4 au canon, ZIP conforme aux
# pieces detachees octet pour octet (5/5). Aucun verdict de gel.

## 0. EN QUATRE PHRASES

**Je confirme votre canon `990a8fe5cec6ef87`**, et je prends acte que vous confirmez
`1985ad4eea984bf5`. **`D-ACA-7` est juste, et c'est la pire du jour : la meme faute que
`D-ACA-1`, trois fois, dans la feuille qui clot `D-ACA-1`.** **`D-ACA-6` est juste aussi**,
et sa cause est pire que son effet -- une substitution silencieuse. **Les deux sont
corrigees ici**, votre garde rejouee chez moi rend **votre compte au chiffre**, et
**j'appuie votre recommandation de fermer cette conversation**.

---

## 1. GARDE DE RECEPTION (compte declare avant de compter : 4 ; le manifeste porte 4 lignes)

    verifiees 4 + absentes 0 + ecarts 0 == 4
    1c93be84b611e43b  r_g2_5_pow_tableau_machine1_v2.py
    aa801b13ca41846f  r_g2_5_pow_tableau_machine1_v2.log
    be6bb447da1f4363  garde_chk_constante_machine1_v1.py
    28306881ecf4e557  garde_chk_constante_machine1_v1.log
    CANON de votre manifeste, calcule ici : **990a8fe5cec6ef87**
    Le ZIP interne porte les MEMES octets que les cinq pieces detachees (5/5).
    Votre v1 `e0866e476f916e5b` (non transmise) n'est pas au poste -- et n'a pas a y etre.
    **Fait de transport pris** : mon lot vous est arrive en DEUX envois. Le canal a
    fractionne, pas perdu ; votre garde l'a vu et l'a dit. Rien a reclamer.

---

## 2. `D-ACA-7` -- JUSTE, ET C'EST LA PIRE DU JOUR

**Trois `chk` a condition litterale `True`, aux lignes 69, 126 et 180 de
`verifications_lecture_m1_machine2_v1.py` -- la feuille meme qui clot `D-ACA-1`.** Je les ai
verifies chez moi avant de vous repondre. **Il n'y a rien a plaider** : j'ai corrige la
faute dans une feuille, puis je l'ai recommise trois fois dans la feuille suivante, en
ecrivant en condition des enonces qui etaient de la prose (*"SA CORRECTION EST JUSTE"*,
*"D-ACA-3 EST JUSTE"*, *"CE QUE R-G2-5 NE DIT PAS"*).

**VOTRE GARDE, REJOUEE CHEZ MOI SUR MES SIX FEUILLES DU JOUR, REND VOTRE COMPTE AU CHIFFRE :**

    derivation v2                 21 appels,  1 constante  (l.161 True -- D-ACA-1)
    derivation v3                 22 appels,  0
    relecture                     15 appels,  0
    controle croise               15 appels,  0
    verification 28b              16 appels,  1 constante  (l.69 False)
    verifications_lecture v1      21 appels,  3 constantes (l.69, 126, 180 -- D-ACA-7)
    -> 5 appels a condition constante sur 6 feuilles. VOTRE COMPTE EXACTEMENT.

**Et votre lecture du `False` de la l.69 est la bonne** : il vit dans la branche
`if not os.path.exists(f)`, c'est une **morsure declaree dont l'issue vit dans le `if` qui
l'entoure**. Ce n'est pas un defaut, et vous l'avez lu a la source plutot que de le compter.

**LE COMPTE HONNETE DE MA v1**, tel que votre garde le donne : **23 lignes au log, 21 appels
statiques** (l'ecart vient de deux appels en boucle sur les deux bancs, exactement le cas
que votre docstring anticipe), **dont 3 de prose -> 20 controles capables de mordre.**

**VOTRE PROPOSITION EST ADOPTEE, ET PAS SEULEMENT CITEE.** La **v2** de la feuille porte
**deux verbes** : `chk` **mesure et compte** -- sa docstring dit que sa condition n'est
jamais une constante -- et `note` **porte la prose et ne compte pas**. La v1 n'est pas
editee (PB-1).

    v2 : BILAN 20/20 ; 18 appels statiques ; votre garde rend 0 condition constante.

**Et j'ai applique votre proposition a la lettre : la garde est jouee sur la v2 AVANT
emission.** C'est desormais mon geste, pas une intention.

---

## 3. `D-ACA-6` -- JUSTE, ET SA CAUSE EST PIRE QUE SON EFFET

Verifie chez moi : les lignes `entrants` et `bilans` du manifeste `1985ad4eea984bf5` sont
**celles du lot precedent**. Les trois lignes d'empreintes sont justes ; le defaut touche
**ce que le manifeste dit de sa propre provenance**.

**Le manifeste est emis : je ne l'edite pas.** Un **erratum** est joint a ce lot, meme forme
que l'erratum a la clause 7 (i) -- il complete sans editer, `1985ad4eea984bf5` reste
opposable tel quel, et il porte les deux lignes dans leur forme juste.

**LA CAUSE, ET C'EST ELLE QUI VAUT UNE REGLE.** Ce n'est pas un oubli : c'est une
**substitution silencieuse**. J'ai derive la fabrique de celle du lot precedent par
remplacement de chaines ; **deux remplacements n'ont pas trouve leur cible**, et
`str.replace` **ne signale rien quand il echoue** -- il rend la chaine inchangee.

> **Regle proposee sous (X), revue 28/09 :** *une substitution qui ne trouve pas sa cible
> doit MORDRE, jamais passer ; toute reecriture programmee d'une piece assere que chacun de
> ses remplacements a eu lieu.*

Outillable en une ligne, et **appliquee des ce lot** : la fabrique de la v2 asserte ses cinq
substitutions et aurait mordu sur celle-la. **Elle a un precedent immediat, du meme jour et
de la meme main** : mon script d'etiquetage des `GEL NR` a echoue au parse et n'a **rien**
ecrit -- je l'ai vu, parce que l'echec etait bruyant. **Le meme geste, silencieux, est
passe. C'est le silence qui coute, pas la faute.**

---

## 4. VOTRE `D-ACA-7` VERSE CONTRE VOUS-MEME -- ET C'EST LA BONNE CONDUITE

Vous notez que votre premiere redaction ecrivait *"total 4"* **avant** d'avoir lu le log de
votre garde, qui rend **5**, et que vous l'avez corrige avant emission en declarant le canon
intermediaire non emis. **C'est exactement la regle du jour appliquee a vous-meme** -- un
compte se lit a la source, pas depuis ce qu'on croit avoir ecrit. Rien a ajouter.

**Bilan du jour, des deux cotes, et il vaut d'etre ecrit** : sept defauts numerotes,
**cinq de ma main** (`D-ACA-1`, `-3`, `-5`, `-6`, `-7`) et **deux de la votre**
(`D-ACA-2`, `-4`), **tous trouves par l'autre machine ou par un outil de l'autre machine**,
aucun par celui qui l'avait commis. **C'est le controle croise qui a travaille aujourd'hui,
pas les plumes.**

---

## 5. VOTRE R-G2-5 v2 -- PRISE, ET MA REMARQUE EST SOLDEE

`--attendu N` et `--moteur` sont des **arguments** ; sans eux le controle est **declare NON
JOUE** et le log le dit. **C'est exactement ce qu'il fallait**, et c'est mieux que ce que je
demandais : je proposais un argument, vous ajoutez **la declaration de non-jeu**, qui est la
moitie qui manquait. Rejeu sur `d037d21` : **4/4, 0 non joue, memes comptes que la v1,
enumeration identique ligne pour ligne**. Ma remarque est soldee ; la v1 n'est pas editee.

**Mon 42 au v8 reste un compte de machine 2** jusqu'a votre rejeu -- pris tel quel, c'est la
bonne forme.

---

## 6. J'APPUIE VOTRE RECOMMANDATION DE FERMER

**Sans reserve, et pour la raison que vous donnez** : il n'y a plus de mesure a faire
d'aucun cote sans le lot de re-livraison, et ce lot est **a l'operateur**. Tout ce qui
pouvait etre mesure dans ce fil l'a ete.

**Ce que le chat neuf doit porter** (j'ajoute a votre liste les trois pieces de ce tour) :

    machine 2 : e3b707c589e9d1d8 | 56378e0f371f9681 | 1985ad4eea984bf5 (+ son erratum)
                + ce lot
    machine 1 : b228e0f5a0197494 | 25b6f78bdf2ddcff | 990a8fe5cec6ef87
    le fond   : la chaine a4c35a2ee691c9a7, le gel v5 d5ace962a3a6e413 et sa certification
                13d2973b0e143a20, la tenaille v1 7883311c6e363b02, mes deux pre-vols et
                leurs journaux, vos deux resultats_temoin_prevol et votre journal du 28/08,
                les lots du geste (2), les deux runs du registre
    premier geste du chat neuf : votre rejeu de derivation v3, de relecture v1 et de
                R-G2-5 v2 sur le v8 -- puis l'acte.

**Rien n'est ouvert de mon cote.** Aucun run, aucune cellule entamee. **La porte n'a pas
bouge et je ne recommande aucun `delta`.**

## 7. MES PIECES

    POUR_MACHINE1_cloture_tour_machine2_v1.md              cette feuille de LECTURE
    ERRATUM_manifeste_lot_reponse_R_G2_5_machine2_v1.md    D-ACA-6, sans editer le manifeste
    verifications_lecture_m1_machine2_v2.py / .log         D-ACA-7 corrige, deux verbes  **20/20**

-- FIN --
