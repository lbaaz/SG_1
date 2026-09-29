# ERRATUM AU LOT machine 2 lot_machine2_2026-09-29_contreseing_acte_delta92_v1 (canon 1c4660dd54c463d8)
# machine 2, v1, 29/09/2026. Emis par machine 2 sur son propre lot, releve par sa propre garde
# PB-1 avant l'emission de la certification du v10/v16. AUCUN CANON DU REGISTRE N'EST FAUX.

CE QUI EST EN CAUSE : trois pieces que mon lot de contreseing a scellees, et que j'ai MODIFIEES
ensuite, sous le meme nom, avant le depot :

    piece                                                 scelle au contreseing   version deposee
    DEPOT_delta92/perimetre_depot_delta92_machine2_v1.py   8b8f001a199dbdd9        6afb296dadf14539
    DEPOT_delta92/perimetre_depot_delta92_machine2_v1.log  5b13fda168b74d86        471b22c5a57ab1fe
    DEPOT_delta92/MANIFEST_DEPOT_delta92_machine2_v1.txt   ee579fe2880d3dd9        c0e330385c07765d

CAUSE, DATEE ET MESUREE : le contreseing (1c4660dd54c463d8) a ete scelle sur un perimetre de
**182 pieces**, ou les 83 series du volet alpha du run 92 entraient PAR LEUR MANIFESTE SEUL.
L'operateur a ensuite tranche le point que l'acte lui reservait (nn.9 (iii)) : les series entrent
UNE A UNE. J'ai donc ajoute a la feuille un bloc declare qui les enumere, chacune verifiee contre
le MANIFEST.sha256 de son volet, et rejoue : **268 pieces**. Le depot a ete fait sur cette
version -- c'est elle, et non celle du contreseing, qui a derive le commit 09baf5c.
Mais je l'ai ecrite SOUS LE MEME NOM v1, au lieu d'en faire une v2. C'est la deuxieme fois de la
journee que j'edite en place une piece deja emise ; la premiere (reception_lot_machine1_machine2_v1
et son journal) avait deja ete relevee par cette meme feuille de perimetre.

QUELLE VERSION FAIT FOI : **celle du registre.** Le commit 09baf5c porte
`journal/perimetre_depot_delta92_machine2_v1.py` = 6afb296dadf14539, la feuille qui a reellement
derive ses 268 pieces, et les 268 pieces y sont a leur canon (controle sur clone neuf, 9/9). Le
manifeste de depot ne se depose pas lui-meme et n'est donc pas au registre ; sa version deposante
est c0e330385c07765d. La version 8b8f001a199dbdd9 est un etat ANTERIEUR, exact pour un perimetre
de 182 pieces qui n'a pas ete depose.

PORTEE : nulle sur le registre -- aucun canon depose n'est faux, le depot est integre et verifie.
La portee est sur MON lot de contreseing : qui l'ouvre y lit, sous un nom, un fichier que le
registre porte differemment. Le present erratum s'archive avec ce lot et se cite avec lui.

CE QUE J'EN TIRE, ET QUI VAUT PLUS QUE L'AVEU : ma garde de fabrique compare desormais chaque
piece scellee de chacun de mes lots emis a mon arbre, AU BIT, avant toute emission -- c'est elle
qui a arrete la certification du v10/v16 et impose cet erratum. Une divergence n'est admise que
si elle est NOMMEE ici : la garde lit ce fichier et refuse toute piece divergente qu'il ne cite
pas. Candidate de regle deja versee sous (X) le 29/09 : une piece emise ne s'edite pas, elle se
versionne ; corollaire ajoute ici : une sortie dont le NOM est fixe dans un script (journal,
manifeste) se versionne AVEC le script, sinon un rejeu l'ecrase.

-- FIN ERRATUM_lot_contreseing_acte_delta92_machine2_v1 --
