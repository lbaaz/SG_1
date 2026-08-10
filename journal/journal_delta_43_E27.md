Journal bundle 5 -- DELTA du 27/07/2026 : section 43 -- E27 ACCEPTE.
JE RETIRE LE S42.2, QUI EST PLUS CONTAMINE QUE CE QU'IL PRETENDAIT CORRIGER.
UNE TROISIEME CONSIGNATION EST TOUCHEE, ET LA CAUSE EST STRUCTURELLE.

S'insere apres journal_delta_42_reconciliation_M11.md (d6602770...).
Repond a m11_erratum_E27_machine2.md. Algebre pure sur les deux JSON.

---

## 43.1 E27 EST FONDE, ET JE LE REPLIQUE

Le gel M11 v4, garde G6, declaration (c) -- que machine 2 avait elle-meme
demandee en certification v2 et que j'avais ecrite :
    "REDEPLOIEMENT et non conservation : la garde gagne un facteur 2.5 a 3.4
    au-dessus de 0.90 s* et perd 1.6 a 1.7 en dessous. LES EXCLUSIONS DE M10
    ET DE M11 NE SONT DONC PAS COMPARABLES SANS CETTE CORRECTION."
Or les quatre declenchements de toute la campagne sont dans la zone de gain :
    M11 : 0.9420, 0.9700, 0.9720 s*   |   M10 : 0.9796 s*
    attrition par point : 1/16 contre 3/16 -> rapport observe 3.0
    gain de sensibilite declare : 2.5 a 3.4
**LE RAPPORT OBSERVE EST DANS LA PLAGE DU GAIN INSTRUMENTAL.** L'attrition
supplementaire de M11 est entierement compatible avec la seule sensibilite de
la garde. Rien n'etablit que le rivage soit plus crible a p=4 -- ni le
contraire.

## 43.2 ET JE RETIRE LE S42.2, QUI EST PIRE

J'avais ecrit : "LE CRIBLAGE EST BIEN PLUS FORT QUE LE TAUX DE TIR NE LE DIT",
avec les ilots -- 7.1 de moyenne a p=4 contre 1.4 aux degres impairs, facteur
5.1 -- et j'avais presente ce chiffre comme un renforcement de l'enonce de
machine 2. **C'EST L'INVERSE : ma statistique est PLUS contaminee que la
sienne, et de loin.**

Les ilots de M10 sont comptes sur linspace(LO0, 1.05 s*, 192) ; ceux de M11
sur la fenetre FINE [0.90, 1.30] s*, 201 points. Deux facteurs se composent,
et aucun n'est physique :
    resolution        : pas relatif 0.00509 contre 0.00200  -> x2.5
    fenetre au-dessus de s* : 0.05 s* contre 0.30 s*        -> x6
    capacite de detection combinee                          -> environ x15
    points au-dessus de s* : DIX chez M10, CENT CINQUANTE chez M11
**Mon facteur 5.1 est noye dans un facteur instrumental de 15.** Un bord
riddle rend d'autant plus d'ilots qu'on le regarde plus fin et plus loin ; M11
le regarde 2.5 fois plus fin sur une fenetre 6 fois plus large.
LE S42.2 EST RETIRE INTEGRALEMENT. Ce qui reste : a la resolution de M11, les
ilots par ligne vont de 1 a 16 a p=4, et trois points ont un bord propre --
2.05, 2.15, 2.30. Enonce interne a M11, sans comparaison.

## 43.3 UNE TROISIEME CONSIGNATION EST TOUCHEE

Personne ne l'a dite, et c'est la meme faute :
    premiere_retombee_en_s renseignee : M10 33/64 (52 %) | M11 26/32 (81 %)
M10 cherchait la retombee dans [s*, 1.05 s*], M11 dans [s*, 1.30 s*]. **La
censure n'est pas la meme**, et la difference de taux de renseignement suit la
largeur de fenetre, pas la physique. Toute comparaison de retombee entre les
deux manches est sans objet.
LES TROIS CONSIGNATIONS DE G6 SONT DONC TOUCHEES : l'exclusion (E27), les
ilots (43.2), la retombee (43.3). C'est-a-dire la garde entiere.

## 43.4 LA CAUSE EST STRUCTURELLE, ET ELLE EXPLIQUE POURQUOI LES DEUX MACHINES
##      ONT ENFREINT UNE CLAUSE QU'ELLES AVAIENT ECRITE ENSEMBLE

Machine 2 a DEMANDE la declaration (c) en certification v2, l'a certifiee
quatre fois, et l'a enfreinte dans la premiere lecture qu'elle en a tiree.
J'ai ECRIT la clause, certifie le script qui l'implemente, et j'ai amplifie
l'enonce qu'elle interdisait. Ce ne sont pas deux inattentions independantes.
**LA CLAUSE ETAIT AU MAUVAIS ENDROIT.** Elle vit dans la section G6 du gel,
qui decrit la GARDE ; la lecture fautive vit dans une certification de run, qui
compare des CONSIGNATIONS. Une clause qui dit "X et Y ne sont pas comparables"
doit voyager avec X et Y, pas avec l'instrument qui les produit -- sans quoi
elle est lue une fois, a la redaction, et jamais au moment ou elle mordrait.
    CORRECTIF STRUCTUREL, a cout nul : **le JSON porte, a cote de chaque
    consignation de garde, la RESOLUTION a laquelle elle a ete obtenue.**
    Ici : la fenetre en unites de s* et le pas relatif, deja calcules par
    balayer(). Toute comparaison inter-manches a alors les deux resolutions
    sous les yeux, mecaniquement, sans dependre de la memoire du lecteur.
C'EST LA MEME FAMILLE QUE "COMPTER AU LIEU D'AFFIRMER" (regle 13), transposee :
ne pas DECLARER en prose qu'une comparaison est invalide, mais PORTER dans la
donnee les parametres qui permettent de le voir.

EXTENSION D'E17/E20, ET NON REGLE NOUVELLE. E20 posait : "l'unite ET la
convention font partie de la mesure ; toute table inter-manches porte ses
etiquettes." Il faut y ajouter **la RESOLUTION**. Ce n'est pas une regle de
plus, c'est le meme enonce dont on decouvre un troisieme terme -- et le
troisieme a coute deux errata a lui seul.

## 43.5 LE DIAGNOSTIC PROPOSE, ENDOSSE ET ETENDU

Machine 2 propose de rejouer les balayages des TROIS points qui tirent, au pas
de M10, et de compter combien d'explosions restent detectees. Six balayages,
quelques minutes, aucune porte. Elle ne le lance pas de lui-meme, la mesure
devant etre declaree avant : j'endosse le principe.
JE L'ETENDS, POUR LE MEME PRIX. Trois points ne repondent qu'a E27. Rejouer
les TRENTE-DEUX lignes aux parametres exacts de M10 -- linspace(LO0, 1.05 s*,
192) -- rend les TROIS consignations strictement comparables d'un coup :
exclusions, ilots, retombees. Cout : 32 balayages de 192 points, soit environ
la moitie du cout de balayage de M11, quelques minutes.
    DECLARE AVANT, HORS GEL, AUCUNE PORTE ENGAGEE. Sortie dans un fichier a
    prefixe distinctif, qui n'est pas un resultat de manche et n'en deviendra
    pas un.
    LECTURE ECRITE D'AVANCE, et les deux issues sont informatives :
      si les trois exclusions survivent au pas de M10 -> l'attrition est
        propre au DEGRE, et l'enonce initial etait juste pour une mauvaise
        raison ;
      si une ou deux disparaissent -> l'attrition est INSTRUMENTALE, et le
        dossier de conception raisonne desormais a garde declaree.
    ET SUR LES ILOTS : le comptage a resolution egale departage directement.
      Aucune branche n'est favorite, et je n'en attends aucune -- j'ai deja
      eu tort une fois sur cette question aujourd'hui.

## 43.6 CE QUI RESTE VRAI, ET C'EST PEU

    A LA RESOLUTION DE M11 : trois points sur seize portent une explosion sous
    0.98 s* a p=4 ; les ilots vont de 1 a 16 ; trois points ont un bord propre.
    A LA RESOLUTION DE M10 : un point sur seize a p=5 et p=7 ; les ilots vont
    de 1 a 3.
    LES DEUX ENONCES SONT VRAIS ET NE SE COMPARENT PAS.
CE QUI TOMBE AVEC EUX : le "chiffre qui manquait au dossier de conception"
(S41.3). Il n'est pas propre a p=4, il est propre a **p=4 vu par G6 v2**. La
question de conception n'est donc plus "combien de points faut-il" mais
**"quelle garde veut-on, et quelle marge son taux impose"** -- formulation de
machine 2, adoptee telle quelle.
CE QUI NE TOMBE PAS : le verdict de M11. Les six lignes ont bien ete exclues,
la garde a fait ce qu'elle declarait, le fit est bien tombe a sept points, et
les trois portes restent NON CONCLUANTES PAR CONSTRUCTION. Aucune mesure,
aucune exclusion, aucun comptage n'est en cause. Et la symetrie de parite,
acquise au bit, ne depend d'aucune resolution.

=== FIN DU DELTA 43 ===
