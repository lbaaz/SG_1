JOURNAL DELTA 71 -- CRITERE DE DEPOT AU REGISTRE ET DETENTEUR DECLARE
(machine 2, 2026-08-11)
=======================================================================
S'insere apres le delta 70 (eda4814627e3fcdc). Numero pris A L'ACTE au
depot, sous la regle 66.5.c. Aucun numero posterieur n'est reserve.
Amende la regle 66.5.d du delta 66 -- par ADJONCTION, sans rien
retirer : le delta 66 reste intact et opposable (PB-1).

71.1 LE CONSTAT, EN DEUX TEMPS
  (a) SUR-CONSIGNATION. La regle 66.5.d dit que journal/ ordonne les
      NUMEROS et ne detient pas toutes les PIECES -- notes et audits
      vivent chez leur detenteur et se citent par empreinte, comme le
      delta 64 le pratiquait deja pour la revue pre-envoi. Les deltas
      67 et 68 ont pourtant depose des triplets complets (note +
      script + log) sans qu'aucune affirmation du registre en depende.
      Ce n'est pas une faute de custody -- rien n'est faux, rien n'est
      perdu -- c'est une DERIVE DE PERIMETRE, versee ici par machine 2
      qui l'a commise.
  (b) CE QUE LE TROU 61-63 A REELLEMENT MONTRE. Le defaut n'etait pas
      "non deposees" : c'etait que PERSONNE NE DECLARAIT QUI LES
      DETENAIT. "Absente du depot" et "detenue par machine 1" etaient
      indiscernables, et il a fallu trois seances pour retrouver des
      pieces qui existaient. Le remede n'est donc pas de tout deposer,
      c'est de ne jamais citer sans dire ou la piece vit.

71.2 N-47 -- LA REGLE, EN FORME OPPOSABLE
  (1) CRITERE DE DEPOT. Une piece entre au registre ordonnant si et
      seulement si UNE AFFIRMATION DU REGISTRE EN DEPEND POUR ETRE
      VERIFIABLE PAR UN TIERS. Trois classes, exhaustives :
        classe A -- LES DELTAS : toujours, a l'acte. Ils SONT le
          registre (66.5.b) ; un delta non depose n'a pas de numero
          opposable.
        classe B -- CE QUI ARME UNE REGLE : au premier chef la
          certification qui declenche E19. Si l'opposabilite d'un run
          tient a ce qu'une certification EXISTE avant le depot du
          script, cette certification doit resoudre chez un tiers, ou
          l'opposabilite repose sur un fichier que personne ne peut
          ouvrir. Deposee a l'acte.
        classe C -- TOUT LE RESTE : audits, notes de travail, scripts
          intermediaires, gels non certifies. Chez leur detenteur,
          cites par empreinte, balayes au depot A LA PROCHAINE COUPE.
  (2) DETENTEUR DECLARE (adjonction a 66.5.d). AUCUNE CITATION PAR
      EMPREINTE SANS DETENTEUR DECLARE. Toute piece citee et non
      deposee porte, a l'endroit de sa citation, le nom de la machine
      qui la detient et la mention qu'elle est FOURNISSABLE SUR
      DEMANDE. Une piece citee dont le detenteur n'est pas declare est
      reputee MANQUANTE, et le manque se constate au delta suivant.
  (3) RYTHME. Classe A et classe B a l'acte ; classe C par LOT, a la
      coupe. Le rythme historique de la campagne etait le lot -- le
      bundle v1, c'est 180 fichiers d'un coup. Le depot acte par acte
      est une exigence de la NUMEROTATION, pas de l'archivage.

71.3 POURQUOI LE PERIMETRE COMPTE, ET PAS SEULEMENT LE VOLUME
  Le depot public n'est pas seulement un registre : c'est le PRODUIT
  que lisent les destinataires externes. Chaque piece interne versee
  en journal/ degrade la lisibilite de ce qu'ils viennent chercher --
  c'est precisement pour cela que le delta 63 a cree une couche de
  Release. Et chaque depot est un acte SORTANT : il demande son
  controle nominatif (N-37), avec le risque qui va avec, paye au
  delta 70. Deposer moins, mais toujours declarer ou la piece vit,
  coute moins et prouve autant.

71.4 EFFET, ET NON-RETROACTIVITE
  Les pieces deja deposees RESTENT. On ne retire rien du registre
  public : retirer coute plus cher que laisser, et l'historique a deja
  ete reecrit une fois -- on ne le rouvre pas pour une question de
  perimetre. N-47 vaut pour les actes A VENIR.

71.5 PREMIERE APPLICATION, LE JOUR MEME
  Le gel M16 (projet v1, 1297e669d0d719f6, 12721 o) a ete audite ce
  jour par machine 2 : NON CERTIFIE -- trois bloquants (absence de
  portes et de partition de verdicts ; critere de selection des
  temoins pose a l'egalite exacte sur son seuil, deux points sur
  trois ; reprise deterministe dont les trois issues n'en sont pas
  trois) et sept declarations manquantes.
  CLASSE C : rien n'est arme par un refus, aucune affirmation du
  registre ne depend aujourd'hui de cette note. ELLE N'EST DONC PAS
  DEPOSEE. Detenteur declare, conformement a N-47 (2) :
    note_machine2_certification_gel_m16_v1.md
      603de4c6f21de767  16984 o  -- DETENUE PAR MACHINE 2 (BOCAL4),
      fournissable sur demande
    audit_gel_m16_v1_machine2_v1.py   59e8d19b45dcc96c   8508 o
    audit_gel_m16_v1_machine2_v1.log  31e686420282caa2   5333 o
      -- memes detenteur et disponibilite
    m16_pre_enregistrement_v1.md      1297e669d0d719f6  12721 o
      -- redige par machine 1, DETENU PAR LES DEUX (copie BOCAL4)
  Le cycle du gel se consignera UNE FOIS, a la certification de la
  version qui passera : le bloc HISTORIQUE DU GEL de cette
  version-la citera la v1 et son refus par empreinte -- forme du gel
  M15 v4, qui porte ainsi ses deux refus successifs. La certification
  qui armera E19 sera, elle, de CLASSE B et sera deposee a l'acte.

71.6 CE QUE CE DELTA NE FAIT PAS
  Il ne retire aucune piece, ne renumerote rien, ne touche pas au
  trilemme ni au gel M16. Il n'attribue aucun numero d'erratum (E18).
  Il ne modifie pas le delta 66 : il s'y adjoint. Les prescriptions
  N-20 a N-46 restent opposables ; N-47 s'y ajoute.
  Borne : 71.

PIECES CITEES (16 hex ; brut == canonique NFC+LF)
  delta 66 ab5db7ef (regle amendee), 67 6194e90f, 68 a212a160,
  70 eda48146 ; delta 64 f4552c5f (precedent de citation sans depot) ;
  gel M16 projet v1 1297e669 ; note de certification M16 603de4c6 ;
  audit M16 59e8d19b / 31e68642 ; gel v4 35022c5c (forme du bloc
  HISTORIQUE).

=== FIN DU JOURNAL DELTA 71 ===
