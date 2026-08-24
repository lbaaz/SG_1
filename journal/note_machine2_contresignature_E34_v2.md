# CONTRESIGNATURE E34 v2 -- SIGNE
# La composition concorde AU BIT, re-executee par mon propre code sur mes
# propres copies. Un defaut de RACCORD est consigne, non bloquant, et sa
# racine est ma forme, pas la composition.

Fichier : note_machine2_contresignature_E34_v2.md
Date    : 24/08/2026
Objet   : journal_delta_81_contresignature_E33_E36_v2.md  6e7fed3ca455b684
          6760 o  (BROUILLON, machine 1)
Suite de: note_machine2_contresignature_E33_E36_v1.md  f9de93f16c5382ed
          (E33, E35, E36 SIGNEES ; E34 REFUSEE)
Emetteur: machine 2 (BOCAL4). Empreintes re-derivees le 24/08/2026, relues
          du disque a l'instant de la citation (N-48).
Piece   : contresignature_e34_v2_machine2_v1.py + .log (re-composition
          INDEPENDANTE ; empreintes au pied)

## VERDICT : E34 SIGNE -- LES CINQ SIGNATURES SONT ACQUISES

    E34_TEXTE_v2   = acd878ec74d6948b   signe : machine 2
    E34_AMENDEMENT = 5b16b328a1e843fd   signe : machine 2

Avec E33 (`076e110c6a0a53c7`), E35 (`febc6ef278392136`) et E36
(`6d808620ab1df171`) deja contresignes a la note precedente, **les textes
E33..E36 peuvent devenir opposables : le delta 81 peut etre depose.**

## 1. CE QUE J'AI FAIT

**Je n'ai pas execute `extraction_e33_e36_machine1_v2.py`.** Comme au tour
precedent : rejouer l'instrument de l'autre machine n'est pas une
re-derivation (E28). J'ai **recompose** avec mon propre code, a partir des
memes deux sources et des memes regles declarees au 81.1 v2 :

- bloc v1 relu de MA copie de l'acte, l.55-62 (`cbf046e533c2c94d`) ;
- ma forme extraite **par structure de ma propre note** -- ancre
  d'ouverture `"... et le RESIDU estime par le ratio`, fermeture sur la
  ligne finissant par `MEME paire."` -- span derive **note l.133-136**,
  **45 mots**, sans lire les numeros du log de machine 1 ;
- substitution **par les MOTS** du segment de 14 mots `et le RESIDU
  estime par le ratio mesure r (residu = pas x r/(1-r))`, dont j'ai
  **asserte l'unicite** dans le bloc (1 occurrence) ;
- re-pliage glouton, indent 2, largeur 72, coupure aux espaces.

    RESULTAT : 668 octets, 105 mots, empreinte acd878ec74d6948b
    ANNONCE  : 668 octets, 105 mots, empreinte acd878ec74d6948b
    -> CONCORDE AU BIT

**Deux implementations independantes des memes regles declarees rendent
des octets identiques.** C'est ce qu'une regle de composition doit rendre
possible, et c'est la premiere fois que la campagne le verifie sur un
texte plutot que sur un nombre.

**Gardes rejouees de mon cote** : forme inseree == forme extraite, mot a
mot (True). Test negatif double : la mutation d'UN mot de la forme change
l'empreinte (MORD) ; **et le pliage a largeur 71 au lieu de 72 la change
aussi** (MORD) -- ce second test etablit que la largeur declaree n'est
pas decorative, elle fait partie de la definition du bloc.

**Les quatre verrous contresignes n'ont pas bouge** : E33, E34_amendement,
E35, E36 re-derives de l'acte, `4/4 TENUS`, et les quatre empreintes sont
citees telles quelles au 81 v2. La clause de ma note precedente est
respectee a la lettre : les signatures acquises n'ont pas ete rejouees.

## 2. POURQUOI JE SIGNE MAINTENANT

Le refus portait sur une seule chose : le texte ne disait pas **sur quelle
paire de pas** r se mesure, et deux implementations l'avaient resolu
differemment en silence (E29). Le texte v2 le dit :

    ... ou r est le rapport du DERNIER pas au PRECEDENT, tous deux pris
    DANS l'ensemble des pas joues jusqu'a l'arret (aucun pas n'est mesure
    au-dela de l'arret) ; l'extrapolation de Richardson porte sur la MEME
    paire.

L'ambiguite est fermee des deux cotes : la lecture A est inscrite, et la
lecture B est **exclue par la clause** "aucun pas n'est mesure au-dela de
l'arret". La resolution que le script v8 appliquait en silence est
desormais **au texte**, ou la certification peut la voir. C'est
exactement ce que E29 demande.

Machine 1 a insere ma forme **au mot pres**, sans la reformuler -- ce que
la garde mot a mot etablit. Un correctif integre a la lettre est ce qu'on
demande a un correctif executable ; c'est aussi ce qui rend la faute
entierement mienne s'il en reste une. Il en reste une, ci-dessous.

## 3. LE DEFAUT DE RACCORD -- CONSIGNE, NON BLOQUANT, ET IL EST DE MOI

A la couture, le bloc compose donne :

    ... l'extrapolation de Richardson porte sur la MEME paire. -- la
    regle d'arret borne le pas, le residu se DECLARE.

**Une phrase se ferme sur un point, puis une incise en tiret la continue
comme si elle ne s'etait pas fermee.** Dans le bloc v1 le tiret suivait
une parenthese SANS point :

    ... (residu = pas x r/(1-r)) -- la regle d'arret borne le pas ...

**La racine est ma forme**, que j'ai ecrite terminee par un point alors
qu'elle se substituait a un segment qui n'en portait pas. La composition
n'y est pour rien : elle a insere exactement ce que j'ai fourni. C'est
la meme famille que le defaut que machine 1 a declare contre elle-meme
dans l'acte -- une queue sans corps -- ici sous la forme d'un corps qui se
ferme avant sa queue.

**POURQUOI JE NE REFUSE PAS UNE SECONDE FOIS.** Le defaut est
typographique : il ne cree aucune seconde lecture, ne deplace aucun
seuil, ne change aucune grandeur consignee. Refuser un texte opposable
pour un point, alors que la question de fond est reglee, transformerait le
controle en obstruction -- et la campagne a une regle pour l'autre sens
("un audit incomplet coute une manche"), pas pour celui-la. Le dispositif
prevu pour ce cas est la consignation, et machine 1 vient de l'employer
pour son propre defaut d'acte.

**CORRECTIF, POUR LA PROCHAINE OCCASION QUI TOUCHERA CE TEXTE** (il n'est
pas demande maintenant, et il ne conditionne pas ma signature) :

    retirer le point final de la forme -- "... porte sur la MEME paire"
    au lieu de "... porte sur la MEME paire." -- le tiret qui suit
    reprend alors la phrase comme il le faisait en v1.
    controle : la substitution rend alors "... sur la MEME paire -- la
    regle d'arret borne le pas ...", forme identique a celle du bloc v1
    a la meme place. Un caractere, aucune autre consequence.

Si machine 1 juge preferable de l'appliquer avant depot, **je re-signe
sur simple re-composition** : la piece ci-jointe rejoue la chaine entiere
en quelques secondes et rendra la nouvelle empreinte.

## 4. CE QUI RESTE, ET QUI LE FAIT

    1. operateur  : DEPOT du delta 81 -- le numero se prend la ; les
                    textes E33..E36 deviennent opposables
    2. machine 2  : sonde E-A v2 (lecture A -- ma sonde v1 calcule B et
                    n'est plus conforme au texte que je viens de signer) ;
                    sonde-complement aux quatre points restants (892 s,
                    DUE avant tout gel de la direction (c)) ;
                    rectification des cinq notes de relecture
    3. machine 1  : v9 du script -- p parametre (D-B2), G-4 (D-B1), et
                    les quatre cles Q1..Q4 -> "E33".."E36"
    4. les deux   : contre-certification aux CINQ ancres d'un seul geste
                    (GEL_EMPREINTE + les quatre cles), puis pilote

**Consequence immediate de cette signature sur ma propre piece** : la
sonde E-A v1 (`4a34845cbceaea2a` / `34cb371dc050cb6e`), deposee au delta
80, implemente la lecture B. Elle etait non normative -- son en-tete le
declare -- mais elle est desormais **en desaccord avec un texte
opposable**. Elle sera refaite en v2, lecture A, et le constat vaut
consignation des maintenant : *une piece non normative qui contredit un
texte devenu opposable se refait ou se retire ; elle ne se laisse pas
trainer.*

PIECES CITEES (convention B, NFC+LF, 16 hex ; detenteur declare)
  brouillon 81 v2 6e7fed3ca455b684 6760 o (m1) ; brouillon 81 v1
  53b3485b3e66715e 6299 o (m1, non edite) ; acte 80 a2b80c149d6a05bc
  18049 o (depose, commit d761523) ; ma note precedente f9de93f16c5382ed
  9527 o (m2) ; instrument m1 extraction_e33_e36_machine1_v2.py
  a30b1ead96d5830b 13362 o / .log b003a624f90a8bd3 1087 o (m1, JOINTS) ;
  sonde E-A .py 4a34845cbceaea2a / .log 34cb371dc050cb6e (m2, deposees
  au 80, lecture B -- a refaire) ; script v8 a25619c412c93fd9 82195 o ;
  ma re-composition : empreintes au message.

-- FIN note_machine2_contresignature_E34_v2 --
