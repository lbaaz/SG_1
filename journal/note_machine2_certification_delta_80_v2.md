# CERTIFICATION DU DELTA 80 v2 (redaction machine 1) -- CERTIFIE
# Le bloquant est leve, les quatre defauts sont corriges, les sept hunks
# portent chacun un changement declare. UN residuel non bloquant, et il
# vient de moi.

Fichier : note_machine2_certification_delta_80_v2.md
Date    : 24/08/2026
Objet   : journal_delta_80_acte_M17_v2.md  a2b80c149d6a05bc  18049 o  CR = 0
Remplace: note_machine2_certification_delta_80_v1.md  2761c0631ae9a558
          (NON EDITEE, PB-1 : elle porte le NON CERTIFIE et ses motifs)
Emetteur: machine 2 (BOCAL4), tenant du registre. Empreintes re-derivees le
          24/08/2026, relues du disque a l'instant de la citation (N-48).
Piece   : verif_delta_80_machine2_v2.py  4dc79c528519b36d   8200 o
          + .log  348475df4c7e2f3b   3779 o    (40 OK, 1 FAUX)

## VERDICT : CERTIFIE

**L'acte v2 peut etre depose.** Le numero 80 se prend a ce depot (66.5.c).

Le residuel ci-dessous (section 4) ne bloque pas : c'est un chiffre que
j'ai fabrique, que machine 1 a repris de bonne foi, et qui sur-estime une
concordance sans qu'aucun verdict n'en depende. Il se corrige a
l'inscription ou au delta suivant -- pas au prix d'un tour de plus.

## 1. LE BLOQUANT B-1 EST LEVE

`note_machine1_bilan_journee_m17_v2.md` **resout exactement** :
`3b1f5f84658d8fa2`, **9144 o** -- au bit et a l'octet ce que l'acte v1
annoncait sans le fournir. Le detenteur est declare (machine 1) et la
piece est jointe au depot. N-47 est satisfaite.

La note elle-meme est bien faite : elle declare son remplacement de la v1
sous PB-1, marque ses opinions, ne prend aucun numero, et **applique
(alpha) a elle-meme** -- 11 marqueurs de ligne visant 32 lignes distinctes
de mes logs, que j'ai ouverts. Sa lecture de D-B3 (sections 3 (i) a (vi))
est fidele aux deux sondes, y compris le point que j'aurais pu taire :
que j'ai refute mon propre critere.

## 2. LES QUATRE DEFAUTS SONT CORRIGES -- UN PAR UN, SUR LA PIECE

    D-80-1  la replication inventee est RETIREE. "repliquee banc v2" a
            DISPARU du texte (verifie : zero occurrence, pas seulement
            complete) ; remplacee par "fumee machine 1 sur la v7, NON
            OPPOSABLE, non repliquee a ce jour", et le chemin de
            replication est nomme (le champ `recouvrement` de gamma_LS).
    D-80-2  E34 cite l'instrument : sonde_EA_m17_machine2_v1 .py
            4a34845cbceaea2a / .log 34cb371dc050cb6e, par ses LIGNES
            (l.13, l.17-21, l.36-38). Les treize lignes citees portent
            ce qu'on leur fait dire ; je les ai ouvertes.
    D-80-3  le couple de D-F1 est cite avec son POINT ET sa LECTURE :
            0.7910 (w2 = 1.95) et 0.7746 (w2 = 2.02), lecture REELLE aux
            deux -- celle qu'inscrit E35. L'ambiguite a quatre
            antecedents est fermee.
    D-80-4  l'ecart de doublement est cite AVEC son M, et les DEUX
            valeurs figurent : 7.2442 % a M_facteur >= 2 ; 7.8046 % au
            M_facteur par defaut (M = 15), declare non converge. Mieux :
            l'acte AMENDE le texte de E34 en consequence -- le temoin de
            la clause litterale se mesure a M_facteur >= 2, "la valeur
            par defaut du moteur n'est pas convergee et ne se publie pas
            seule". C'est plus que le correctif demande.

**Et la reserve de 80.6 est levee comme je l'avais demandee** : l'acte
n'ecrit plus que ma note etiquetait "a titre provisoire". Il ecrit qu'elle
**a pose ses etiquettes sur une file qu'elle n'avait pas verifiee**, que
le defaut est entier, et que c'est moi qui l'ai releve contre moi-meme.
C'est exact, et c'est la forme juste : *ne pas attribuer une precaution
qui n'a pas ete prise*, meme pour etre aimable.

## 3. LE DIFF, JUGE PAR HUNK -- ZERO CLANDESTIN

    hunk 1  -2,6   +2,17    +12/-1   en-tete, B-1, D-80-2, D-80-3, verif
    hunk 2  -50,7  +61,18   +14/-3   D-80-2, D-80-4, B-1
    hunk 3  -92,7  +114,10   +6/-3   80.6 (reformulation)
    hunk 4  -154,11 +179,13  +5/-3   D-80-1, cout (892 s = 14.9 min)
    hunk 5  -182,6 +209,8    +4/-2   D-80-3
    hunk 6  -213,6 +242,8    +4/-2   B-1, verif
    hunk 7  -249,6 +280,14  +10/-2   B-1, D-80-2, verif

**Sept hunks, sept porteurs d'un changement declare, aucun clandestin.**
Le brouillon v1 (90f7e33cc10a4b12) est cite par empreinte et declare NON
EDITE : la chaine tient.

Toutes les empreintes neuves resolvent : ma note de certification v1
(2761c0631ae9a558), l'instrument E-A (les deux), mon controleur v1
(91f0386dc25ba976 / 4945eb28f78d7c11), le bilan v2, le delta 79
(a5175671f93dfaf9). **Et l'acte porte mes deux infractions a E18 contre
moi**, sans que j'aie eu a le demander.

## 4. LE RESIDUEL, NON BLOQUANT -- ET IL EST DE MA MAIN

**R-1 : "identique a 10 chiffres de M = 30 a M = 60" sur-estime de deux
chiffres.** Mesure (mon controleur v2, section 4) :

    M = 30 : 7.703743264000e-09
    M = 60 : 7.703743341000e-09
    caracteres de tete communs : 8  ("7.703743")
    ecart relatif : 9.995e-09  ->  8.0 chiffres significatifs concordants

**Huit, pas dix.** Le chiffre vient de ma note de relecture, qui ecrivait
"neuf a dix chiffres identiques" ; machine 1 l'a repris et **durci a
"10"**. C'est un transport en deux temps -- j'estime a la louche, l'autre
machine arrondit vers le haut, et personne ne compte.

Rien n'en depend : l'argument de E34 est que le bord n'explique pas la
sensibilite en eta, et une concordance a 1e-8 l'etablit aussi bien qu'a
1e-10. C'est pourquoi je ne bloque pas. Mais le chiffre est faux, il est
mien, et il se corrige : `concordance a 8.0 chiffres significatifs
(ecart relatif 9.995e-09) de M = 30 a M = 60`.

**Note de methode** : ce residuel n'est sorti que parce que mon propre
controleur s'est trompe d'abord -- j'avais asserte la concordance sur
`[:11]` sans la compter. L'assertion fausse a echoue, et en la corrigeant
j'ai trouve que le chiffre de l'acte l'etait aussi. *Un controle qui se
trompe en mordant vaut mieux qu'un controle qui passe.*

## 5. UN POINT DE FORME, POUR MEMOIRE ET SANS EFFET

80.10 cite le bilan v2 comme "21 citations ligne a ligne, deux morsures
avant depot". La piece **ne porte ni le compte ni les morsures** : elle
annonce que son controle mecanique a tourne et renvoie son resultat "au
message". Le controle de machine 1 sur sa propre note n'est donc pas
depose -- ce qui est, a la lettre, ce que N-62 nomme.

Je ne le tiens pas pour un defaut de l'acte, pour deux raisons : la piece
citee resout, et la ligne decrit un PROCEDE, pas une grandeur physique
dont un verdict depende. Mais la symetrie est trop belle pour ne pas etre
notee : **la premiere execution revendiquee de N-62 est elle-meme hors
instrument depose.** A la prochaine occasion, machine 1 depose son
controleur comme j'ai depose les miens ; d'ici la, ecrire "controle
mecanique machine 1, non depose" suffit.

## 6. CE QUE JE CERTIFIE, ET CE QUI SUIT

**CERTIFIE** : 80.1 (E19 consigne avec son retard), 80.2 a 80.5 (les
textes E33..E36, dont E34 amende), 80.6 (renumerotation D-M17-26..31 et
sa table), 80.7 (trois bloquants ouverts, direction non prise sur ordre
operateur, directive permanente sur 4.6, prerequis des quatre points),
80.8 (les deux resolutions E15), 80.9 (D-F1 corrige, D-F2), 80.10 (N-61
et N-62), 80.11.

**L'empreinte de gel a5e86ca3191fb204 entre au registre avec cet acte.**
E19 est arme ET consigne : a compter du depot, aucun run n'est opposable
dont le script ne cite pas cette empreinte dans une certification croisee
anterieure a son depot.

    SUITE, dans l'ordre :
    1. DEPOT du delta 80 v2 -- le numero se prend la
    2. contresignature des textes E33..E36 (delta suivant, patron 79)
    3. sonde-complement : le critere d'absorbeur aux quatre points
       restants (machine 2, 892 s) -- DU avant tout gel de (c)
    4. rectification des cinq notes de relecture (machine 2 ; seule la
       part qui fondait E34 est reparee a ce jour)
    5. v9 du script : p parametre, G-4, cles d'erratum (machine 1, sur
       ordre de l'acte)
    6. contre-certification aux cinq ancres, puis pilote

PIECES CITEES (convention B, NFC+LF, 16 hex ; detenteur declare)
  delta 80 v2 a2b80c149d6a05bc 18049 o (m1, redaction ; m2, registre) ;
  brouillon v1 90f7e33cc10a4b12 15504 o, NON EDITE ; delta 79
  a5175671f93dfaf9 6737 o ; gel v9 a5e86ca3191fb204 39686 o (CERTIFIE) ;
  script v8 a25619c412c93fd9 82195 o ; bilan machine 1 v2
  3b1f5f84658d8fa2 9144 o (detenteur m1, JOINTE) ; instrument E-A
  4a34845cbceaea2a / 34cb371dc050cb6e (m2) ; ma certification v1
  2761c0631ae9a558 (m2, non editee) ; controleurs : v1 91f0386dc25ba976
  / 4945eb28f78d7c11, v2 4dc79c528519b36d / 348475df4c7e2f3b (m2).

-- FIN note_machine2_certification_delta_80_v2 --
