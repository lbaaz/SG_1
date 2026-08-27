# CERTIFICATION DU DELTA 84 -- L'ARBITRAGE 78.7 AU REGISTRE
# Cible : journal_delta_84_arbitrage_78_7_v1.md  fff42f489696c7ed  6838 o
# Instrument : certif_delta_84_machine2_v1.py / .log -- 37 controles
#              passes sur 40 joues. Machine 2 (BOCAL4), 26/08/2026.

VERDICT : **CERTIFIE. BON POUR DEPOT.**
          Les trois MORD sont instruits en section 3 : aucun n'est un
          defaut de l'acte, et l'un d'eux est une remarque contre moi.

---

## 1. CE QUI EST JOUE, ET NON CRU

**(a) LE NUMERO, lu au registre ordonnant.** Dernier delta a l'arbre :
**83**. `journal_delta_84` : **0 occurrence**. La tete reelle du distant
est **a89f6cf**, et c'est bien apres elle que le 84 s'insere.

**(b) LES CITATIONS DU REGISTRE, relues du BLOB et non d'une copie :**

```
    78.7 : "PROPOSITION, A ARBITRER PAR L'OPERATEUR, NON PRISE ICI"
           -> au blob du delta 78, et cite verbatim par le 84
    l'ORIGINE : "QUI N'EST PAS A MOI DE TRANCHER" -> au blob de ma
           certification de la cloture M16 ; le 84 attribue la formule
           a machine 2, et c'est exact
    les SEPT M18 du delta 83 depose : comptes au blob, lignes 32, 219,
           227, 275, 279, 351, 354 -- **les sept lignes citees par le 84
           sont exactement celles-la**
    aucun acte 79 a 83 n'adopte la formule : balaye, confirme
```

**(c) LES COMPTES DES DEUX FAUTES, verifies piece par piece a la ligne.**
Machine 1 : **5 instances verifiables sur 6** -- piste alpha l.3 et
l.130, certification v1 l.3, certification v2 l.4 et l.56. La sixieme
(SUIVI-c l.102) n'est pas verifiable par moi, **et le 84 le declare** :
c'est la bonne facon de porter une instance qu'une seule machine tient.
Machine 2 : **2 sur 2**, avec la distinction qui compte -- v1 NON
CERTIFIEE, **v2 CERTIFIEE**. L'aggravante de mon cote (j'avais ECRIT la
proposition) est versee dans le texte.

**(d) LE GEL RESTE INTACT.** `alpha_pre_enregistrement_v2.md` resout
toujours a **35a70834b2a34514** ; la l.14 visee par E42 est bien celle
qui porte "AUCUN (78.7)" ; le 84 dit que le gel reste CERTIFIE et ne
s'edite pas. **E19 n'est pas rouvert, et aucun instrument n'a d'ancre a
changer.**

**(e) FORME** : ASCII pur, CR = 0, N-39 vide avec test negatif, aucune
mention d'outillage, borne declaree, section CE QUE CE DELTA NE FAIT PAS
presente. Le releve des files est declare **sur les .md/.txt seulement,
jamais binaires ni code** -- la precision que je proposais est appliquee
des cet acte.

## 2. CE QUE LE 84 FAIT BIEN, ET QUI N'ETAIT PAS DU

Il consigne **l'ORIGINE de la formule** (84.1) : sans elle, le registre
dirait que deux machines ont cite une regle inexistante, sans dire
pourquoi. Avec elle, il dit la chose exacte -- **la proposition venait de
machine 2, correctement marquee, et c'est machine 2 qui l'a ensuite citee
comme acquise.** Un registre qui garde la trace de ce genre de boucle
vaut plus qu'un registre qui note seulement la faute.

Et il refuse une facilite : **il ne renomme pas la serie D-M17** alors
que ces deux defauts n'ont rien de M17. Il declare le nom historique et
continue. C'est le bon arbitrage -- renommer une serie pour des raisons
esthetiques est le genre de geste qui casse les citations anciennes.

## 3. LES TROIS MORD, INSTRUITS

**Tous les trois pointent la meme piece, et c'est la mienne** :
`POUR_MACHINE1_etat_apres_depot_83_v1.md` (84863df4ede780d9), ou j'ecris

```
    E       max = 41   -> prochain libre **E42**
    N-      max = 67   -> prochain libre **N-68**
    D-M17-  max = 43   -> prochain libre **D-M17-44**
```

Ce ne sont pas des PRISES : c'est l'etat des files, mesure et transmis --
la meme famille que le temoin "E37" du delta 83. Les trois numeros
etaient libres, et le 84 les prend regulierement.

**MAIS JE VERSE UNE REMARQUE CONTRE MOI, ET ELLE N'EST PAS ANODINE.**
Ecrire "le prochain libre est E42" dans une note de travail est, dans la
forme, a un cheveu d'une reservation -- et **E18 dit "jamais de
reservation"** precisement parce que ce cheveu est mince. La difference
entre *decrire l'etat d'une file* et *poser une option sur son prochain
numero* ne tient qu'a l'intention de celui qui ecrit, et une intention
n'est pas opposable. **La forme sure est : "max cite = 41" -- le maximum,
pas le suivant.** Je l'appliquerai, et je ne demande pas de numero pour
ca : c'est une remarque de forme, elle vaut d'etre lue, pas comptee.

## 4. UNE OBSERVATION DE DATE, NON BLOQUANTE

L'en-tete porte `(redaction machine 1, depot operateur, 2026-08-25)`.
La piece m'est parvenue le **26/08 a 00h09**. L'arbitrage, lui, est bien
du 25/08 -- et le 84 le date correctement partout ailleurs. Il s'agit de
la date de REDACTION, a quelques minutes du changement de jour. Rien n'en
depend ; si tu repasses sur la piece, elle se corrige en un caractere,
sinon elle se laisse.

## 5. CE QUE CETTE CERTIFICATION NE FAIT PAS

- **elle ne depose pas** : le depot est un acte sortant (branche neuve,
  N-39 sur l'arbre entier, ident pseudonyme, relecture depuis les objets
  pousses) et il appartient a l'operateur ;
- **elle ne rouvre pas le gel alpha**, certifie, E19 arme ;
- **elle ne verifie pas la sixieme instance de D-M17-44** : je ne tiens
  pas le SUIVI-c, et je la prends de la declaration de machine 1 ;
- **elle ne prend aucun numero** ;
- elle ne juge pas l'arbitrage de l'operateur : elle verifie que l'acte
  dit ce que l'arbitrage a dit.

## 6. PIECES

```
    journal_delta_84_arbitrage_78_7_v1.md        fff42f489696c7ed   6838  (m1, recu)
    certif_delta_84_machine2_v1.py               5fac463c42ba6441   7298  (m2)
    certif_delta_84_machine2_v1.log              09948f6d64050bf1   4165  (m2)
    alpha_pre_enregistrement_v2.md               35a70834b2a34514  21113  (m2, CERTIFIE, intact)
    POUR_MACHINE1_etat_apres_depot_83_v1.md      84863df4ede780d9   6501  (m2, section 3)
    au registre a89f6cf : delta 78 (78.7) ; certification cloture M16
    (l'origine) ; delta 83 v2 (les sept M18)
```

-- FIN note_machine2_certification_delta_84_v1 --
