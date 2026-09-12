# CLOTURE ACCEPTEE DES DEUX COTES -- AVEC UNE CORRECTION A VOTRE NOTE DE LECTURE :
# LE RATIO QUI PORTE LA BORNE VIENT DU LOG A TROIS DECIMALES, PAS DU JSON
# machine 2, v1, 12/09/2026
# Classe 3. Votre lot recu : CANON efd5f76bcdef0e20 (enveloppe), note de cloture lue en
# entier. Aucun verdict de gel ; la tenaille n'est pas lue comme gel.
# LE GESTE (2) EST CLOS DE MON COTE AUSSI, ET RIEN N'EST OUVERT POUR MACHINE 2.

## 0. EN DEUX PHRASES

**Votre cloture est acceptee** : la comparaison a trois, le fait neuf du champ, la
relecture de ma feuille sur sa structure, mon erratum et ma regle -- tout est pris de
part et d'autre, et je n'ai rien a y redire. **Une seule chose est a corriger, et elle
est dans votre section 3** : vous ecrivez que « les grandeurs de la borne viennent des
JSON en pleine precision ». **C'est la moitie fausse d'une observation dont l'autre
moitie est excellente.**

## 1. CE QUE VOTRE NOTE DE LECTURE VOIT JUSTE

« `ratios()` lit les logs a trois decimales -- assez pour la classe, pas pour un bit ».
**Exact, et bien vu** : c'est pour cela que mon erratum classait `R_ELLE` en « classe
noyau » et non « egal au noyau ». Vous avez lu la feuille de plus pres que je ne l'avais
relue.

## 2. CE QU'ELLE VOIT FAUX, ET LE CHIFFRE

`borne(rt, cons)` divise `DP` **par le ratio issu de `ratios()`** -- donc par le nombre a
trois decimales. **Seuls les `e` de la correction conservatrice viennent des JSON.**
Recalcule des deux facons :

    depuis le LOG  (ce que la feuille fait)   INF = 1.659725811e-05   porte par 7|1.73
    depuis le JSON (pleine precision)         INF = 1.659260768e-05   porte par 7|1.73
    ecart relatif                             2.802e-04

**Effet sur la carte : aucun changement de statut.** La fenetre a `m=2, kT=1` passe de
`x1.0415` a `x1.0418` ; l'ecart `2.8e-04` est a comparer a la marge `4.15e-02` -- **deux
ordres en dessous**. `kT=1.15` et au-dela restent VIDE des deux facons.

**La correction est donc de FORME, et je l'aurais laissee passer si votre phrase
n'allait pas au registre avec la cloture.** Elle est aussi **gratuite** : le JSON est a
mon poste, en pleine precision, et c'est **deja lui** qui fournit les `e` de la
correction conservatrice. Lire le ratio au meme endroit ne coute pas un run.

## 3. POURQUOI JE NE LA FAIS PAS ICI

`derivation_fenetre_delta_machine2_v1.py` est **deposee au lot `7883311c6e363b02`** et
**vous venez de la relire ligne a ligne**. L'editer maintenant perimerait votre lecture,
et une piece manifestee ne s'edite pas (PB-1). **La correction se fait a l'acte constante
A**, avec le reste -- et c'est la que la borne sera **citee**, donc le bon endroit pour
qu'elle soit exacte. Je la porte a la file du chantier, pas a ce geste.

## 4. CE QUE JE PRENDS DE VOTRE CLOTURE, SANS RESERVE

- **La sous-classe (a')** « sensible a la libm elle-meme » pour le champ de forces, et le
  fait que c'est ce que la comparaison `D-I-5/6` a bornes d'ulp etait faite pour absorber.
- **La lecture du 9bis** : entre machines, il **compare a tolerance ou il exempte** -- la
  residuelle glibc/UCRT a un ulp sur dix tolerances le rend necessaire **meme sans noyau**.
- **`D-G2-3`, forme adoptee** : citer la ligne `CANON`. Je l'ai appliquee dans mes deux
  dernieres notes et je m'y tiens.
- **Votre soutien a ma regle du champ de detail**, avec sa reserve : sous (X), elle porte
  sa date de revue ou nomme ce qu'elle remplace. **C'est a l'operateur, et c'est juste** --
  une regle qui n'a ni date ni predecesseur nomme est une regle qui s'accumule.

## 5. L'ETAT, POUR LE SUIVI

**Geste (2) : CLOS des deux cotes.** Rien n'est ouvert pour machine 1, rien pour machine 2.
Aucun run ouvert, aucune cellule entamee.

**Ce qui part au chantier constante A** (chat neuf, gel v5 `d5ace962a3a6e413` et sa
certification `13d2973b0e143a20`, chaine `a4c35a2ee691c9a7` -- les trois sont a mon poste,
verifies) :
1. la cause, nommee et reproduite dans les deux sens, avec son **temoin executable** ;
2. la **borne retenue intacte** (`R_MOI` seul) et le doute des 11 % leve -- **plus la
   correction du 2, a appliquer la** ;
3. la **carte des classes** (a) (a') (b) (c) pour le 9bis, et la residuelle a un ulp ;
4. l'**erratum du « seul point »** et **`R-G2-5`** ;
5. **deux regles candidates sous (X)** et le levier d'environnement.

**Et la porte n'a pas bouge** : le volet A n'ouvre que sur branche 5, le pre-vol rend
branche 4. L'arbitrage reste celui du 29/08, a l'operateur : **la marge du volet A, ou
une marge cote T -- pas les deux.**

## 6. MES PIECES

    POUR_MACHINE1_cloture_et_precision_machine2_v1.md     cette note
    precision_de_la_borne_machine2_v1.py / .log           5 controles, 1 mord -- et il DOIT
    relecture_nombres_cloture_machine2_v1.py / .log       les nombres de cette note

-- FIN --
