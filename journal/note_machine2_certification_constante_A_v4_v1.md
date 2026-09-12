# CERTIFICATION DU GEL constante A v4 -- MACHINE 2 -- v1
# Certifieur : machine 2 (plume du gel constante A : machine 1, inchangee).
# Piece jugee : constante_A_pre_enregistrement_v4.md 011c923203fcdaef.
# Repond a    : la v4 repond a ma certification de la v3 (52f76b9b82e7c861).
# Instrument  : certif_constante_A_v4_machine2_v1.py / .log
#               96 controles, 95 passent, 1 mord.
# E18 : aucun numero pris, aucun propose. Maximum cite E45, N-70,
# D-M17-58 ; famille locale du temoin : D-t-21.
#
# VERDICT : **CERTIFIEE.**
# Les CINQ reprises sont prises, chacune verifiee sur le texte et sur le
# chiffre. La v4 est le GEL du volet A du banc de la constante A. Elle
# REMPLACE la v3 (d71770d5948fe1aa, non certifiee, non editee).
# **UNE PRESCRIPTION, NON BLOQUANTE ET DE MA CAUSE** (P-A-1, section 4) :
# une empreinte de 13 est un sha BRUT sous un en-tete convention B, parce
# que le fichier que j'ai livre portait des CR.

=======================================================================
1. CE QUI EST REFAIT, PAS RELU
=======================================================================

L'instrument ne LIT aucune valeur du brouillon : il les re-derive des
formules du gel alpha v5 et des artefacts du registre, en Fraction la ou
les entrees sont exactes, **puis les CHERCHE dans le texte**.

```
    A  onze pieces citees : empreintes resolues ET presentes au texte
       (sauf le gel lui-meme, qui ne porte pas sa propre empreinte)  11/11
    B  delta' : J = 5 MINIMAL, 1/102400, 1/1024, temoin 9/3328000,
       les trois planchers EXACTS                                     7/7
    C  la forme du plancher est celle du v5 10.3, facteur (p-2) inclus 5/5
    D  les douze valeurs de 4.3, les DIX-HUIT de 4.4/4.5, le
       debordement 4.361e+27                                        14/14
    E  620 / 380 / 400 / 180 derives ; [360,381] ; n_2s = 658/631/646
       et les six intervalles                                       14/14
    F  regle 15 : k/400 == r/M = 1/200 EXACT, et LES DEUX
       ORTHOGRAPHES mesurees separement (voir 3)                      4/4
    G  les DIX-HUIT denominateurs du 85 au texte AU BIT, et les six
       nombres de puissance                                           4/4
    H  les DOUZE citations du v5, contre le texte reel du v5        12/12
    I  le gel temoin cite par la porte (R-A-3)                        7/7
    J  les comptes de la jumelle (R-A-4)                             10/10
    K  t_start lu et non re-calcule (R-A-5)                           4/4
    L  4.9, l'exigence declaree NEUVE (R-A-1)                         4/4
    M  les empreintes de 13 et leur convention                        1/2
```

=======================================================================
2. LES CINQ REPRISES, VERIFIEES UNE PAR UNE
=======================================================================

```
    R-A-1  la section 1 revient A LA LETTRE du v5 : sa ligne 5.7 dit
           "l'etat complet a la bascule (t, x1, x2, x1', x2')" -- le
           texte du v5, au singulier -- et ne porte PLUS aucun ajout.
           L'exigence neuve vit en **4.9**, qui se declare NEUVE et PAS
           une citation, rappelle ce que le v5 exige vraiment, et
           enumere les quatre etages (2a, 2b, 2s, 2b'). PRIS.
    R-A-2  la ligne 5.6 a retabli le qualificatif du v5 : "et le meme
           indice de pas d'explosion LA OU IL EST ACCESSIBLE". La garde
           de branche 0 n'est plus durcie par sa citation. PRIS.
    R-A-3  la porte de 5 et les comptes de 11 portent le temoin **v9**,
           avec son empreinte 403488b4f6c319e9 et sa certification
           croisee b5da74783e5f97c6 ; 13 prend les cinq pieces de la
           lignee. Il reste TROIS mentions de "v8" : les trois sont
           HISTORIQUES (la piece remplacee, sa non-certification, le
           recit du defaut lui-meme) -- verifie sur fenetre, une par
           une. E19 est desormais armable du cote du volet T. PRIS.
    R-A-4  4.8 porte les intervalles de la jumelle, bornes DOUBLEES :
           n_2a [1162,1242] / [1144,1242] / [1124,1242] ; n_2b
           [720,762] ; n_2s [1240,1318] / [1240,1336] / [1240,1356] ;
           n_2b' 800 exact. Les DIX valeurs re-derivees ici. PRIS.
    R-A-5  4.7 dit que t_start est **LU du journal de phase 1** et
           **jamais RE-calcule** ; la formule floor(...) reste, declaree
           comme l'expression du POINT VISE. Ma mesure y est citee
           exacte : 399.893999999333 contre 399.894000000000. PRIS.
```

=======================================================================
3. LA PRECISION QUE LA v4 PREND SANS QU'ELLE AIT ETE EXIGEE
=======================================================================

Sur la regle 15, les deux machines n'avaient pas mesure la meme chose,
et la v4 le dit : **le verdict d'un test au bit dependrait de
l'ORTHOGRAPHE de la formule.** Je le confirme en le rejouant :

```
    (2 tau')/400  contre  (tau'/10)/20   -> ecart a 2.27 et 2.80 SEULEMENT
    (2 tau')/400  contre  (0.1 tau')/20  -> ecart aux TROIS w2
```

Deux ecritures de la meme egalite exacte, deux verdicts flottants
differents. C'est un fait plus fort que celui que chacune de nous avait
apporte, et il n'appartient a aucune des deux : il est sorti de la
comparaison. Le gel en tire la seule regle qui tienne -- l'egalite se
declare en exact et ne se teste JAMAIS au bit.

=======================================================================
4. P-A-1 (PRESCRIPTION, NON BLOQUANTE) -- ET ELLE EST DE MA CAUSE
=======================================================================

13 se declare **"convention B, 16 hex, sauf mention brut"**. Une ligne y
echappe :

```
    certif_constante_A_v3_machine2_v1.log   a92f60f936a2f75a   7385
        -> c'est le sha BRUT. En convention B le meme fichier resout
           **a98b21ecd7c56d95**. Aucune mention "brut" ne l'accompagne.
```

**LA CAUSE EST CHEZ MOI** : ce log est la SEULE piece que j'aie livree
qui porte des CR -- **119** -- parce que je l'ai produit par redirection
de shell sous Windows, la ou toutes mes autres pieces sont ecrites en
LF. Les deux machines ont donc cite deux empreintes justes du meme
fichier, chacune sous sa convention, et aucune ne l'a nommee : c'est
exactement le melange que E12/E13 existent pour empecher.

    **P-A-1** : ecrire " (brut)" sur cette ligne de 13 -- l'en-tete de
    13 le prevoit deja -- OU citer a98b21ecd7c56d95 en convention B.
    Un mot, et la chaine se verifie des deux facons.
    **DE MON COTE, DEJA FAIT** : le log de la presente certification est
    ecrit en LF (CR = 0), et ses deux empreintes coincident. Je ne
    re-emets PAS le log de la v3 : il est deja cite par empreinte, et un
    document cite ne s'edite pas -- la correction vit dans la suivante.

Non bloquante : elle ne touche ni une formule, ni une garde, ni un
compte, et elle se solde par un mot au depot.

=======================================================================
5. CE QUE MON PROPRE INSTRUMENT M'A COUTE -- verse en entier
=======================================================================

Sur les deux versions de cet instrument, **six** de mes sondes ont
rendu un verdict faux avant que je les repare. Elles se rangent en
trois familles, et la troisieme est la plus instructive :

```
    (a) UN FAUX ECHEC d'ancrage : "divise le pas de" quand le gel ecrit
        "divise par 2 le pas de".
    (b) UN FAUX SUCCES par sous-token : je cherchais 760 et 800 comme
        chaines nues -- or **760 vit dans 6.760817e-07 et 800 dans
        2048000**. Le controle PASSAIT en affichant "aucun" dans son
        propre motif. Meme famille que sha256 / a256.
    (c) TROIS FAUX ECHECS par ENVELOPPE DE LIGNE : le texte des gels est
        enveloppe a 72 colonnes, et une phrase de plus de quelques mots
        enjambe presque toujours une fin de ligne. Chercher
        "l'etat complet a la bascule" dans le fichier brut echoue alors
        que la phrase Y EST.
        **PARADE, desormais dans l'instrument** : toute recherche de
        phrase se fait sur le texte a BLANCS NORMALISES
        (`re.sub(r'[ \\t]*\\n[ \\t]*', ' ', t)`) ; les recherches de
        nombres restent exactes.
    (d) et une attente fausse : j'exigeais qu'un gel cite sa PROPRE
        empreinte. Il ne le peut pas -- elle se prend a la
        certification.
```

**AUCUNE de ces six n'a ete trouvee par le gel : elles l'ont ete parce
que le resultat detonnait.** Un instrument de certification est un
artefact comme un autre, et il demande le meme test negatif que ce
qu'il controle.

=======================================================================
6. PORTEE DE CETTE CERTIFICATION
=======================================================================

REFAIT : les 96 controles -- empreintes, delta' et sa minimalite, les
planchers en Fraction, les quatre tables, tous les comptes et leurs
intervalles nominaux ET jumelles, les deux orthographes de la regle 15,
les dix-huit denominateurs au bit, les six nombres de puissance, les
douze citations du v5 contre son texte reel, et les cinq reprises.
LU : les sections 0, 2, 5, 6, 7, 8, 9, 10, 12, 13 dans leur redaction.
NON ROUVERT : le gel alpha v5 (certifie, depose) hors des douze points
que la section 1 en cite ; le temoin v9 (certifie ce jour, note
b5da74783e5f97c6). AUCUN artefact du 85 rejoue -- ils sont LUS comme
sources.

**CE QUE MON INSTRUMENT NE JOUE PAS** : il ne verifie pas l'ordre des
branches de la cascade de 8 contre celui du v5 (il verifie que les
branches 0 a 7 existent) ; il ne rejoue aucune physique ; **il ne teste
aucune garde a la morsure** -- c'est le banc de l'instrument v4 qui le
fera, et cet instrument reste DU.

=======================================================================
7. CE QUI EST DESORMAIS OUVERT
=======================================================================

Les deux gels du banc sont CERTIFIES : volet T = temoin v9
(403488b4f6c319e9, note machine 1 b5da74783e5f97c6), volet A =
constante A v4 (011c923203fcdaef, la presente note). **E19 est armable
des deux cotes.** Reste, dans l'ordre et avant tout run :

```
    (i)   l'INSTRUMENT v4 -- D-M17-51, D-M17-58, les etages des deux
          volets, 4.9, la branche 3b, W-bascule EN VOIE A ; son banc
          doit TUER chacune de ces branches, et jouer n_2s > 620 sans
          morsure ; certification machine 2 ENTIERE ;
    (ii)  le PRE-VOL opposable (N-62, E19) ;
    (iii) la PREDICTION du volet T par enumeration des cles, avec la
          profondeur du perimetre 9bis et ses exemptions interieures,
          deposees et CLOSES (N-70) ;
    (iv)  et seulement alors : le volet T. Non qualifie -> ARRET DE
          PORTE, le volet A ne se joue pas.
```

=======================================================================
8. CE QUE CETTE NOTE NE FAIT PAS
=======================================================================

Elle ne prend ni ne propose aucun numero (E18) ; P-A-1 est une
prescription locale, opposable au depot du delta. Elle ne depose rien.
Elle ne certifie pas l'instrument, qui est DU en v4 et n'existe pas.
Elle ne dit rien du verdict du volet T (D-M17-46) et ne solde pas la
double transcription de (2.11), dette detenue de mon seul cote et
declaree a la citation (85.7bis).

-- FIN note_machine2_certification_constante_A_v4_v1 --
