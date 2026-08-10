JOURNAL DELTA 66 -- AUTORITE DE NUMEROTATION UNIQUE : journal/ EST LE
REGISTRE ORDONNANT (machine 2, 2026-08-10)
=======================================================================
S'insere apres LES DEUX pieces numerotees 65 (c'est l'objet meme du
present delta, voir 66.1). Numero 66 pris A L'ACTE (E18), au depot,
sous la regle que ce delta adopte. Aucun numero posterieur n'est
reserve.

66.1 LE FAIT : LE NUMERO 65 A ETE PRIS DEUX FOIS, LE MEME JOUR
  machine 1  journal_delta_65_fusion_d_v3.md
             e5931c94518916ce   4380 o  "machine 1, 2026-08-10"
             (fusion version d, bundle v3, revue v1.1, transfert
             61-63) -- depose a BOCAL4, jamais au depot.
  machine 2  journal/journal_delta_65_pseudonymisation_baaz.md
             5ad0561e14ec563e   3003 o  "machine 2, 2026-08-10"
             (pseudonymisation du depot public, note e, README EN)
             -- depose au depot, jamais a BOCAL4 jusqu'a ce jour.
  Les DEUX declarent, mot pour mot, "S'insere apres
  journal_delta_64_revue_note_c.md". Ce n'est pas une collision de
  NOM (famille E13, deja payee deux fois le 10/08 sur les versions c
  de la note) : c'est une collision sur l'EPINE DORSALE du registre,
  la suite de numeros par laquelle toutes les pieces se citent.
  Constate par machine 2 le 10/08 : empreintes re-derivees
  localement, listing du depot releve par
  gh api repos/lbaaz/SG_1/contents/journal.

66.2 CONSTAT JOINT : LES DELTAS 61, 62 ET 63 N'EXISTENT DANS AUCUN
     DES DEUX REGISTRES
  Le delta 65 machine 1 (65.5) les declare "re-derives ce jour ==
  registre (18ad843d, 183ab8a1, 6b647dfa) et RE-PRESENTES pour
  integration". Recherche exhaustive PAR EMPREINTE sur l'arborescence
  BOCAL4 entiere : les trois sont introuvables. Listing du journal/
  du depot : 50..60, 64, 65 -- 61, 62, 63 absents.
  Ils ne resolvent que dans la copie projet de machine 1.
  CE CONSTAT N'EST PAS UNE RESERVATION DE NUMERO (E18 tient) : les
  trois pieces EXISTENT et portent deja leurs numeros du fait de
  l'acte de machine 1 ; le present delta constate seulement qu'elles
  ne sont deposees nulle part. Elles restent deposables sous 61, 62,
  63. Si elles ne le sont pas, le trou est un trou declare, pas des
  numeros brules.

66.3 CAUSE : LA SCISSION DE REGISTRE, DECLAREE
  Deux registres actifs numerotaient independamment sans se lire :
  BOCAL4 (echange de fichiers machine 1 <-> machine 2) et journal/ au
  depot (ecrit par la session de re-coupe). Le 65 n'a pas ete
  "oublie" d'un cote : il a ete consigne des DEUX cotes, en meme
  temps, a des contenus differents. La re-depose du 10/08 a repare la
  PIECE (reserve R-1 levee), pas la CAUSE.
  Consequence qui rendait la suite impossible : E18 -- "le numero se
  prend a l'acte" -- n'etait plus EXECUTABLE, faute de suite unique
  ou le prendre. Le delta de decision du trilemme du site 8/3 ne
  pouvait donc pas etre consigne.

66.4 DECISION D'OPERATEUR (adoption de la prescription N-29)
  Prescription N-29 proposee par machine 2 dans
  note_machine2_controle_dossier_v2_delta65_v1.md (ae8ff7901302858c,
  16328 o, BOCAL4) ; ADOPTEE PAR L'OPERATEUR le 2026-08-10.
  Motif de la variante retenue : le journal/ du depot est public,
  ordonne et immuable par construction ; il porte deja son 65 dans un
  historique qui a ete reecrit une fois -- on ne le rouvre pas une
  seconde fois pour un renumerotage.

66.5 LA REGLE, DANS SA FORME OPPOSABLE
  (a) journal/ du depot est LE REGISTRE ORDONNANT. Il n'existe pas
      d'autre suite de numeros de delta.
  (b) Tout delta, quelle que soit la machine qui l'ecrit, VIT dans
      journal/. Un delta non depose n'a pas de numero opposable.
  (c) Le numero se prend A L'ACTE DE DEPOT dans journal/, jamais a
      la redaction, jamais par avance (E18 inchangee, seul son lieu
      d'application est fixe). L'ordre de depot decide entre pieces
      concurrentes.
  (d) journal/ ordonne les NUMEROS, il ne detient pas toutes les
      PIECES : les notes de machine 2, gels de travail et audits
      vivent a BOCAL4 et se citent PAR EMPREINTE, convention deja
      pratiquee par le delta 64 pour la revue pre-envoi. Une piece
      citee doit resoudre chez son detenteur, sur demande.
  (e) Toute piece deja numerotee hors journal/ se regularise en
      version suivante (PB-1 : l'originale n'est pas modifiee en
      place) et prend son numero au depot.

66.6 EFFETS IMMEDIATS
  - Les deux pieces 65 restent INTACTES l'une et l'autre (PB-1). La
    piece du depot conserve le numero 65 ; la piece machine 1
    e5931c94 est a RE-EMETTRE en v4 sous le prochain numero libre au
    moment de son depot, contenu inchange hors numero et borne. Sa
    v3 reste opposable a BOCAL4 comme piece historique, et le
    dossier trilemme v2 (347f25da) qui la cite par empreinte reste
    valide sans retouche.
  - Aucun numero n'est attribue ici a la re-emission ni au delta de
    decision du trilemme : ils se prennent a l'acte, dans l'ordre
    des depots.
  - Une copie de la piece 65 du depot est deposee a BOCAL4 sous
    depot_journal_delta_65_pseudonymisation_baaz_COPIE.md
    (5ad0561e), nommee COPIE parce qu'elle n'est pas une piece
    BOCAL4 d'origine.
  - Nommage machine 2, faute versee (C-4 de la note de controle) :
    revue_pre_envoi_2026-08-10b_machine2_v1.md avait ete EDITEE EN
    PLACE apres citation par empreinte -- trois etats sous un nom
    (9234984c 14960 o, cite en 64.1 ; 310e2171 18341 o, cite en
    65.1 ; 342f7cc9 20461 o, etat courant). Le fichier courant est
    renomme revue_pre_envoi_2026-08-10b_machine2_v1_2.md, contenu
    342f7cc97d04a7b4 inchange ; le nom nu "v1" est retire de
    l'usage ; 310e2171 est a re-deposer par machine 1 sous nom
    versionne. 9234984c n'est plus resolu localement.
  - Etat desynchronise consigne (C-5) : le delta 65 machine 1 ecrit
    "tags immuables v1 88ed9158 / v2 9db2afa4 / v3 2f898234" et
    "une seule chose bloque encore l'envoi : A3". A l'heure de sa
    lecture, l'historique public a ete reecrit et force-pushe, le
    tag v1-held re-emis (0ace0d19), le depot est PUBLIC et LE MAIL
    EST PARTI avec la note d en piece jointe. Ce n'est pas une
    faute de machine 1 : c'est le symptome de 66.3, et c'est la
    raison pour laquelle la regle 66.5 existe.

66.7 CE QUE CE DELTA NE FAIT PAS
  Aucune mesure, aucun gel, aucun arbitrage scientifique. Le
  trilemme du site 8/3 reste arbitre comme au 10/08 (B2 vehicule,
  B3 lecture, B1 ecartee) et son dossier v2 reste sous les
  prescriptions N-20 a N-32. Aucun numero d'erratum n'est attribue.
  L'historique public n'est pas retouche.

PIECES CITEES (16 hex ; brut == canonique NFC+LF sauf mention)
  dossier trilemme v2                347f25daf1046c43  16690 o
  note machine 2 d'arbitrage         1c490f90fafcf8ff  16106 o
  note machine 2 de controle         ae8ff7901302858c  16328 o
  audit joint (.py / .log)           16c9034003288d17 / 64628b9a4efd9e4b
  delta 65 machine 1                 e5931c94518916ce   4380 o
  delta 65 depot                     5ad0561e14ec563e   3003 o
  delta 64                           f4552c5f6fe40446   4357 o
  revue pre-envoi v1_2               342f7cc97d04a7b4  20461 o
  deltas 61 / 62 / 63 annonces       18ad843d / 183ab8a1 / 6b647dfa
                                     -- NON RESOLUS (66.2)
  Borne : 66.

=== FIN DU JOURNAL DELTA 66 ===
