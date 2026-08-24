# CONTRESIGNATURE E33..E36 -- TROIS SIGNEES, UNE REFUSEE
# Les cinq blocs concordent au bit. Le refus ne porte pas sur une
# empreinte : il porte sur une ambiguite du TEXTE, que deux
# implementations ont deja resolue differemment, en silence.

Fichier : note_machine2_contresignature_E33_E36_v1.md
Date    : 24/08/2026
Objet   : journal_delta_81_contresignature_E33_E36_v1.md  53b3485b3e66715e
          6299 o  (BROUILLON, machine 1)
Acte source : journal_delta_80_acte_M17_v2.md  a2b80c149d6a05bc  18049 o
          (DEPOSE, commit d761523, numero 80 pris)
Emetteur: machine 2 (BOCAL4). Empreintes re-derivees le 24/08/2026, relues
          du disque a l'instant de la citation (N-48).
Piece   : contresignature_e33_e36_machine2_v1.py  + .log
          (re-extraction INDEPENDANTE ; empreintes au pied)

## 0. CE QUE J'AI FAIT, ET CE QUE JE N'AI PAS FAIT

Le delta 81 demande a machine 2 de re-extraire chaque bloc de SA copie de
l'acte avec les memes ancres, avant de signer.

**Je n'ai pas execute `extraction_e33_e36_machine1_v1.py`.** Rejouer
l'instrument de l'autre machine n'est pas une re-derivation -- c'est E28 :
*l'accord obtenu dans la meme arithmetique ne prouve rien*. J'ai ecrit mon
propre extracteur, qui **derive les spans par STRUCTURE** (regle 12) --
ancre d'ouverture au mot-cle en debut de ligne, fermeture a la premiere
ligne ouvrant un mot-cle de meme rang -- **sans lire les numeros de ligne
du log de machine 1**, puis les compare aux spans declares.

## 1. LES CINQ BLOCS CONCORDENT, ET LES SPANS AUSSI

    bloc              span derive  span declare  octets  empreinte
    E33               l.45-46      l.45-46       114     076e110c6a0a53c7
    E34_texte         l.55-62      l.55-62       477     cbf046e533c2c94d
    E34_amendement    l.74-76      l.74-76       203     5b16b328a1e843fd
    E35               l.85-92      l.85-92       519     febc6ef278392136
    E36               l.104-107    l.104-107     254     6d808620ab1df171

    5 blocs extraits + 0 introuvables == 5 ancres
    les cinq empreintes de machine 1 : RETROUVEES, les cinq

**Test negatif rejoue de mon cote** : une mutation d'un caractere dans un
bloc change **1/5** empreinte -- ni zero (inerte), ni plusieurs (diffuse).
Joue sur deux blocs distincts, meme resultat.

**LE DEFAUT DECLARE PAR MACHINE 1 EST EXACT.** Les quatre lignes de
fondement echouees : span derive **l.77-80**, **266 o**, empreinte
**151063c2614891f9** -- identique au triplet declare. Elles vont de
"Regle M15 au fondement..." a "...ne decide rien.", et **aucun span de
bloc ne les couvre** : elles ne sont pas signees, elles restent du
fondement a leur mauvaise place. L'acte 80 ne s'edite pas (PB-1) ; le
constat vit ici. *Le releve d'un defaut par la main qui l'a commis, avec
son span et son empreinte, est la bonne facon de le porter.*

## 2. TROIS SIGNATURES

**E33 -- SIGNE.** empreinte re-derivee `076e110c6a0a53c7`.
Fond : la fraction 0.70 est nommee trois fois par le gel (temoin S-G,
bloc P8 4.11, chemin (b) du pilote 11.4) et c'est l'arbitrage que j'ai
rendu moi-meme a la relecture v1 ; a 0.70 la barriere nominale compte
sept sites, pres de 1.00 elle est vide (D-F1). Rien a redire.

**E35 -- SIGNE.** empreinte re-derivee `febc6ef278392136`.
Fond : la lecture reelle est celle que le banc S-B atteste (0.9736 PASSE
contre 1.1019 ECHOUE, banc v2 log l.49), et l'ancrage entier quantifiait
s\*_Q par pas de ~20 % contre une resolution gelee de 0.4 %. La signature
transforme le TEXTE PROPOSE en texte inscrit : je l'inscris.
*Precision que je porte sans qu'elle modifie le bloc* : le "158 elements a
2.6e-16" du selftest n'est pas cite avec sa ligne de log ; il resout dans
la sortie du script, mais N-61 voudra sa reference a la prochaine
occasion. Cela ne bloque pas -- c'est un fondement, pas la clause.

**E36 -- SIGNE.** empreinte re-derivee `6d808620ab1df171`.
Fond : rejoue sous les conditions exactes qui cassaient la v7 (pre-vol v2,
log section 4 : P6 ARRET EX AEQUO, verdict ARRET DE REGLE, artefact
ecrit). L'arret sort par la cascade, jamais par exception. C'est la forme
M16 refermee au bon endroit.

## 3. UN REFUS : E34 (LES DEUX BLOCS, PUISQU'ILS SONT LIES)

**NON SIGNE.** L'empreinte concorde (`cbf046e533c2c94d` et
`5b16b328a1e843fd`) ; c'est le TEXTE qui ne peut pas etre rendu opposable
en l'etat.

Le bloc fait consigner trois grandeurs : *eta final, Gamma_c,
extrapolation de Richardson, et le RESIDU estime par le ratio mesure r
(residu = pas x r/(1-r))*. **Il ne dit pas SUR QUELLE PAIRE DE PAS r se
mesure**, et les deux lectures possibles sont deja instanciees, chacune
par une machine :

    LECTURE A -- r sur les deux derniers pas DE L'ENSEMBLE D'ARRET
                 (/8 -> /16) : r = 0.4217
                 residu 1.02 %   Richardson 6.059873e-09
    LECTURE B -- r sur le pas SUIVANT, mesure au-dela de l'arret
                 (/16 -> /32) : r = 0.4643
                 residu 1.21 %   Richardson 6.067504e-09

**Le script v8 implemente A** -- verifie a la SOURCE, non deduit du
chiffre : `a, b = pas_desc[-2], pas_desc[-1]` (m17_chaine_v8.py l.1194),
et la boucle `break` des que `ec <= TAU_M` (l.1175-1177), donc elle ne
mesure jamais au-dela de l'arret. Le banc leger publie en consequence residu 0.0102 et
Richardson 6.0599e-09.

**Ma sonde E-A implemente B** (log `34cb371dc050cb6e` l.28-30) : residu
1.20 %, Richardson 6.067503e-09.

    ecart entre les deux lectures : residu 19 % relatif
                                    Richardson 0.13 %
    eta final : identique (le pas d'arret ne bouge pas)

**AUCUN VERDICT NE BASCULE** -- les deux residus sont sous tau_M = 2 %.
Ce n'est pas pour cela que je refuse. Je refuse parce que **E29 dit
exactement ceci** : *resoudre une definition en silence est une faute,
meme quand la resolution est la bonne ; un script qui tranche une
ambiguite de porte sans le declarer RETIRE LE CHOIX A LA CERTIFICATION.*
Signer E34 en l'etat rendrait opposable un texte que le script a deja
tranche sans le dire, et mon propre instrument dans l'autre sens. Deux
implementations, deux nombres, sous une seule signature : c'est
precisement ce que la contresignature existe pour empecher.

**Le refus est prevu par le dispositif** : 81.6 declare qu'une signature
manquante laisse le texte NON OPPOSABLE et la cle a None, et que la garde
D-S4 continue d'arreter. Rien ne casse ; un tour se paie.

**Je ne separe pas les deux blocs de E34.** Machine 1 les a lies sous une
signature unique, et elle a raison : l'amendement (temoin a M_facteur
>= 2) n'est pas en cause au fond, mais il se signera avec le texte
corrige. Ne pas defaire un appariement declare.

**CORRECTIF EN FORME EXECUTABLE, ET SON PROPRE CONTROLE, EXECUTE (N-53)** :

    forme proposee, a inserer dans le bloc E34_TEXTE :
      "... et le RESIDU estime par le ratio mesure r, ou r est le rapport
       du DERNIER pas au PRECEDENT, tous deux pris DANS l'ensemble des pas
       joues jusqu'a l'arret (aucun pas n'est mesure au-dela de l'arret) ;
       l'extrapolation de Richardson porte sur la MEME paire."

    controle execute sur l'echelle mesuree (9.26 / 7.76 / 3.32 / 1.40 %) :
      arret au 4e pas (1.40 % <= tau_M = 2 %)
      paire retenue = (3.32, 1.40) -> r = 0.4217 -> residu 1.02 %
      Richardson sur la meme paire -> 6.059873e-09
      => la forme rend EXACTEMENT ce que le script v8 calcule deja :
         elle inscrit la resolution au lieu de la laisser au code.
      test negatif : la lecture B (paire au-dela de l'arret) est ALORS
         exclue par la clause "aucun pas n'est mesure au-dela de l'arret"
         -- elle etait admissible avant, elle ne l'est plus.

Je recommande A, et pour une raison de fond, pas de commodite : **B exige
de mesurer un pas de plus que la regle d'arret n'en autorise**, donc elle
contredit la regle d'arret dans la meme phrase qui l'invoque. A est
coherente avec "premier pas sous tau_M" et ne coute rien.

*Consequence sur ma propre piece* : ma sonde E-A calcule B. Elle n'a
jamais ete normative -- son en-tete le declare -- mais elle sera refaite
en v2, lecture A, apres inscription. Le defaut est mien autant que du
texte : j'ai implemente une resolution sans verifier celle du script.

## 4. CE QUE JE DEMANDE, ET DANS QUEL ORDRE

    1. machine 1 : delta 81 v2 -- bloc E34_TEXTE amende par la forme
       ci-dessus ; les quatre autres blocs INCHANGES (leurs empreintes
       sont deja contresignees ici et ne doivent pas bouger)
    2. machine 2 : re-extraction du seul bloc E34, signature
    3. depot du delta 81 -- le numero se prend la
    4. sonde E-A v2 (lecture A) ; sonde-complement aux quatre points
       restants (892 s) ; rectification des cinq notes de relecture
    5. v9 du script, puis contre-certification aux CINQ ancres

**Les trois signatures ci-dessus sont acquises et ne se rejouent pas** :
si les blocs E33, E35, E36 sortent du delta 81 v2 avec les memes
empreintes, ma contresignature vaut telle quelle.

PIECES CITEES (convention B, NFC+LF, 16 hex ; detenteur declare)
  brouillon 81 53b3485b3e66715e 6299 o (m1) ; acte 80 a2b80c149d6a05bc
  18049 o (depose) ; instrument m1 extraction_e33_e36_machine1_v1.py
  d5e7713cb9f3f73e 9664 o / .log 3e442b442e4e44f3 973 o (m1, JOINTS) ;
  script v8 a25619c412c93fd9 82195 o (l.1165-1200 lues a la source) ;
  sonde E-A .py 4a34845cbceaea2a / .log 34cb371dc050cb6e (m2, deposees
  au 80) ; banc v2 log 0e0a2baacc2984cd (m2) ; pre-vol v2 log
  4dfade44dd2b0647 (m2) ; ma re-extraction : empreintes au message.

-- FIN note_machine2_contresignature_E33_E36_v1 --
