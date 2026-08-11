JOURNAL DELTA 70 -- DEPOT DES DELTAS 61, 62, 63 ET 69 AU REGISTRE,
CONTROLE NOMINATIF ET DERIVES PSEUDONYMISES (machine 2, 2026-08-11)
=======================================================================
S'insere apres le delta 69 (49c0f81618c54579). Numero pris A L'ACTE au
depot, sous la regle 66.5.c ; aucun numero posterieur n'est reserve.
Acte de depot : il solde la reclamation N-30 et la re-emission 66.6.

70.1 CE QUI EST DEPOSE
  Cinq pieces entrent au registre ordonnant, plus le present delta :
    journal_delta_61_coupe_consignee_pseudonymisee.md
    journal_delta_62_contre_epreuve_mail_libere.md      (DIRECT)
    journal_delta_63_release_notes_pseudonymisee.md
    journal_delta_69_fusion_d_v4_pseudonymisee.md
    note_machine2_certification_deltas_61-63_69_v1_pseudonymisee.md
  Les originaux restent INTACTS a BOCAL4 et se citent par empreinte
  (66.5.d). Le trou 61-63 du registre est comble ; la chaine declaree
  du delta 64, qui citait le 63, resout enfin.

70.2 CERTIFICATION DES PIECES RECUES (note machine 2, original
     4277d04f4cfa9563, derive public ci-dessus)
  Les trois empreintes annoncees en 65.5 se verifient AU BIT :
    delta 61  18ad843dff34afaf  4028 o   annonce 18ad843d  CONFORME
    delta 62  183ab8a16b2f4778  2692 o   annonce 183ab8a1  CONFORME
    delta 63  6b647dfaa77c69cb  1808 o   annonce 6b647dfa  CONFORME
    delta 69  49c0f81618c54579  4620 o   piece neuve
  Chaine verifiee maillon par maillon, chaque delta citant l'empreinte
  de son predecesseur : 60 b67c2776 -> 61 -> 62 -> 63 -> 64 f4552c5f ->
  65 -> 66 ab5db7ef -> 67 6194e90f -> 68 a212a160 -> 69 -> 70.
  RE-EMISSION 69 : diff contre la v3 juge PAR HUNK -- 12 hunks, tous
  porteurs d'un changement declare (titre, bloc d'insertion, 7 en-tetes
  de section, auto-reference, borne, terminateur), ZERO hunk
  clandestin. Le perimetre annonce est exactement le perimetre observe.
  C-2 et N-30 sont LEVEES.
  RESERVE DE LECTURE, consignee et non bloquante : la re-emission
  etant fidele, elle transporte l'etat perime declare en C-5 (69.4
  "tags immuables", 69.7 "l'envoi reste bloque"). Le lecteur est
  protege par le bloc d'insertion du 69, qui renvoie a 66.6. Aucune
  version supplementaire n'est demandee.

70.3 CONTROLE NOMINATIF (N-37) -- EXECUTE SUR LES CINQ PIECES
  Recherche du nom civil de l'operateur avant tout depot :
    delta 61   1 occurrence   -> derive
    delta 62   0 occurrence   -> DEPOT DIRECT, sans derive
    delta 63   1 occurrence   -> derive
    delta 69   1 occurrence   -> derive
    note de certification  6 occurrences (section 4, ou les occurrences
      sont l'OBJET du controle) -> derive
  Le controle est declare meme la ou il ne trouve rien : c'est le
  delta 62 qui le prouve.
  Motif : le registre ordonnant est un depot PUBLIC ET PSEUDONYMISE ;
  deposer ces pieces en l'etat aurait annule l'effet du delta 65 du
  depot. Decision d'operateur du 2026-08-11 : pseudonymisation
  partout, periphrase validee pour le releve de signature.

70.4 MAPPING sha16 ANCIEN -> NOUVEAU (forme du delta 65 du depot)
  journal_delta_61_coupe_consignee
    18ad843dff34afaf (4028 o) -> e83d6a1c664dd4f9 (4582 o)
  journal_delta_63_release_notes
    6b647dfaa77c69cb (1808 o) -> 3053bf4b598041cd (2368 o)
  journal_delta_69_fusion_d_v4
    49c0f81618c54579 (4620 o) -> 738ad396f874e717 (5298 o)
  note_machine2_certification_deltas_61-63_69_v1
    4277d04f4cfa9563 (10823 o) -> 1190e356104db14a (11493 o)
  journal_delta_62_contre_epreuve_mail_libere : INCHANGE, 183ab8a1.
  Chaque derive porte EN TETE un bloc declarant sa nature, l'empreinte
  et la taille de son original, et la liste de ses substitutions --
  c'est la correction du defaut releve au delta 67.3, ou le derive
  pseudonymise de la revue vivait au depot SANS marquer qu'il en etait
  un. Un derive non marque est un piege pour le lecteur suivant.

70.5 N-38 APPLIQUEE -- DEUX NATURES DE SUBSTITUTION, ET C'EST LA REGLE
  Le nom civil est tantot le SUJET du texte, tantot son OBJET.
    SUJET (le texte designe la personne) -> pseudonyme, forme deja
      publique : "cote baaz" (61), "relecture de baaz" (63).
    OBJET (le texte RELEVE ce qu'une piece contient) -> PERIPHRASE,
      jamais pseudonyme : 69.3 devient "SIGNATURE de l'operateur (nom
      civil en clair dans la piece signee) + mail". Ecrire "SIGNATURE
      baaz" ferait dire au registre que la note a ete signee d'un
      pseudonyme : c'est FAUX, et la piece signee est entre les mains
      d'un tiers qui peut le constater. Meme traitement dans la note
      de certification, dont la section 4 CITE les lignes fautives :
      le nom y est remplace par le placeholder "<nom civil>".
  Une pseudonymisation ne doit jamais transformer un releve exact en
  releve faux. C'est la contrainte que N-38 porte.

70.6 REPONSE RENDUE A LA QUESTION 63.2 -- LA LIGNE M2
  Machine 1 versait une observation d'extraction : aucune section
  d'execution M2 au journal gele. L'observation est EXACTE et le
  journal maitre porte lui-meme l'explication -- "M2 (en reserve) --
  test du piegeage, deja pre-enregistre au paragraphe 10" (maitre
  bundle5 h, tel que servi par le depot), suivi de "13. MANCHE M1
  EXECUTEE" puis des sections M3. M2 a ete PRE-ENREGISTREE PUIS MISE EN
  RESERVE, delibererement, et jamais executee : la campagne passe de M1
  a M3. Ce n'est pas un trou du registre, c'est une reserve DECLAREE.
  La table de la Release doit l'ecrire ainsi -- "en reserve, jamais
  executee" -- une case vide se lirait comme une perte.

70.7 DEFAUT PAYE PENDANT CET ACTE, VERSE ICI (machine 2)
  La PREMIERE serie de derives a ete produite, puis JETEE avant tout
  depot. Deux fautes, la meme famille :
  (a) le bloc d'en-tete declarait chaque substitution en CITANT LE
      MOTIF RETIRE -- il reintroduisait donc, en tete du fichier
      public, le nom civil que le corps venait de supprimer. Une
      declaration de suppression ne doit jamais citer ce qu'elle
      supprime : elle en declare la NATURE et le COMPTE.
  (b) l'assertion de controle portait sur le CORPS SUBSTITUE, variable
      intermediaire, et non sur les OCTETS ECRITS. Elle ne pouvait
      donc pas voir l'en-tete : assertion a la MAUVAISE PORTEE, elle
      passait sans rien tester. C'est le piege recurrent de la
      campagne, paye une fois de plus.
  CE QUI A MORDU : le controle nominatif passe sur L'ARBRE ENTIER
  avant commit -- pas sur les pieces une a une. Il a designe les
  quatre derives. Le clone a ete remis a l'etat pousse, aucune
  publication n'a eu lieu.
  PARADES INSCRITES DANS LA v2 DU GENERATEUR : controle sur le fichier
  RELU DU DISQUE ; controle final sur l'arbre entier ; TEST NEGATIF
  execute et affiche (un temoin fabrique portant le nom EST detecte,
  le meme temoin nettoye ne l'est pas). D'ou N-39.

N-39  Le controle nominatif porte sur L'ARTEFACT PRODUIT, relu depuis
      le disque, et sur L'ARBRE ENTIER avant depot -- jamais sur une
      variable intermediaire ni piece par piece. Il s'accompagne de
      son test negatif. Corollaire general : UN BLOC QUI DECLARE UNE
      SUPPRESSION NE CITE PAS CE QU'IL SUPPRIME.

70.8 CE QUE CE DELTA NE FAIT PAS
  Le CONTENU technique des deltas 61, 62 et 63 n'est pas re-verifie :
  je certifie leur integrite de canal et leur place dans la chaine,
  pas les mesures qu'ils consignent ; leurs contre-epreuves d'epoque
  (tar.gz 3e9203d7, MANIFEST 180 lignes, dix temoins) ne sont pas
  rejouees. Ces trois pieces decrivent en outre un etat du depot qui
  n'est plus servi depuis la re-ecriture de l'historique -- meme
  famille que la reserve du 70.2. La piece RELEASE_NOTES du delta 63
  n'a pas ete livree et n'est pas au perimetre. Aucune mesure, aucun
  gel, aucun numero d'erratum (E18). Le trilemme n'est pas touche :
  N-20 a N-38 restent opposables au gel de branche B2/B3.
  Borne : 70.

=== FIN DU JOURNAL DELTA 70 ===
