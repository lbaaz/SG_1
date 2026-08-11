[DERIVE PSEUDONYMISE -- produit par machine 2, 2026-08-11]
Copie destinee au registre public. Original INTACT a BOCAL4 :
  note_machine2_certification_deltas_61-63_69_v1.md
  4277d04f4cfa9563  10823 octets
Substitutions (N-37) -- declarees par NATURE et par COMPTE ; le
motif retire n'est pas cite, sans quoi la declaration reintroduirait
ce qu'elle supprime :
  2 x  nom civil OBJET du releve -> placeholder (N-38)
       -> "<nom civil>"
  4 x  nom civil OBJET du releve -> placeholder (N-38)
       -> "<nom civil>"
Aucune autre modification. Mapping consigne au delta de depot.
-----------------------------------------------------------------------
NOTE MACHINE 2 -- CERTIFICATION DES DELTAS 61, 62, 63 ET DE LA
RE-EMISSION 69 (machine 2, 2026-08-11)
=======================================================================
Objet : controle des quatre pieces livrees par machine 1 en reponse aux
reclamations N-30 (deltas 61-63) et 66.6 (re-emission de la piece de
fusion). Aucune mesure, aucun gel, aucun numero attribue (E18).
LF seul, CR = 0 : brut = canonique (N-10). UN seul caractere non-ASCII,
le "§" d'une citation verbatim du journal maitre (section 3) -- il n'est
pas transcrit en ASCII parce qu'une citation verbatim ne se retouche pas.
CETTE NOTE EST ELLE-MEME SOUS N-37 : elle cite le nom civil de
l'operateur six fois (section 4, ou c'est l'objet meme du controle) et
ne peut donc pas entrer au registre public sans derive pseudonymise.

VERDICT
  LES QUATRE PIECES SONT CERTIFIEES. Les trois empreintes annoncees
  depuis le delta 65 se verifient au bit ; la re-emission est propre au
  hunk ; LA CHAINE DU REGISTRE EST REFERMEE DE 60 A 69. C-2 et N-30
  sont LEVEES. MAIS LE DEPOT EST BLOQUE : trois des quatre pieces
  nomment l'operateur en clair, et le registre public est pseudonymise.
  Le blocage est de forme, pas de fond, et sa resolution appartient a
  l'operateur (section 4).

=======================================================================
1. CUSTODY -- TROIS SUR TROIS AU BIT, LA RECLAMATION N-30 EST SOLDEE
=======================================================================
Empreintes re-derivees localement, brut == canonique, CR = 0, ASCII pur :
  journal_delta_61_coupe_consignee.md
    18ad843dff34afaf   4028 o   annoncee 65.5 : 18ad843d   CONFORME
  journal_delta_62_contre_epreuve_mail_libere.md
    183ab8a16b2f4778   2692 o   annoncee 65.5 : 183ab8a1   CONFORME
  journal_delta_63_release_notes.md
    6b647dfaa77c69cb   1808 o   annoncee 65.5 : 6b647dfa   CONFORME
  journal_delta_69_fusion_d_v4.md
    49c0f81618c54579   4620 o   piece neuve
Les trois valeurs annoncees le 10/08 dans une piece qui ne resolvait
elle-meme pas encore (delta 65) sont exactes. Le canal a tenu.

NOMS DE CANAL NORMALISES : les pieces sont arrivees suffixees par le
navigateur ("(1)", "(2)"). Renommees aux noms canoniques, contenus
INCHANGES ; l'ancien delta 64 local portait le meme defaut, corrige au
passage. Les octets font foi (61.2, doctrine machine 1) mais un nom
suffixe est une collision E13 en puissance.

LA CHAINE EST REFERMEE, ET ELLE SE VERIFIE MAILLON PAR MAILLON :
  60 b67c2776  <- cite par 61, resout localement
  61 18ad843d  <- cite par 62, resout
  62 183ab8a1  <- cite par 63, resout
  63 6b647dfa  <- cite par 64, resout
  64 f4552c5f  <- cite par 65 et par 69, resout
  65 e5931c94 (machine 1, intacte) et 5ad0561e (depot) -- les deux 65
  66 ab5db7ef -> 67 6194e90f -> 68 a212a160 -> 69 49c0f816
FAIT A CONSIGNER : le delta 64 declarait s'inserer apres le delta 63
(6b647dfa). Ce maillon PENDAIT depuis le 10/08 -- 63 ne resolvait nulle
part. Le trou 61-63 n'etait donc pas seulement un transfert manque :
il cassait la chaine declaree du 64. Il est referme.

=======================================================================
2. LA RE-EMISSION 69 EST PROPRE -- DIFF PAR HUNK, 12 SUR 12 DECLARES
=======================================================================
Regle appliquee : un diff se juge PAR HUNK, jamais ligne a ligne ;
chaque bloc contigu doit porter le marqueur d'un changement declare.
Diff journal_delta_65_fusion_d_v3.md -> journal_delta_69_fusion_d_v4.md :
  12 hunks, ventiles ainsi
    1 titre                       65 -> 69
    1 bloc d'insertion (4 lignes) nouveau, DECLARE : renvoi 66.5.c,
      66.5.e / 66.6, empreinte et taille de la v3, mention "INTACTE a
      BOCAL4", perimetre du changement annonce
    7 en-tetes de section         65.x -> 69.x
    1 auto-reference dans 69.5    "le present delta 65" -> "69"
    1 borne                       65 -> 69
    1 terminateur                 FIN DU JOURNAL DELTA 65 -> 69
  ZERO hunk clandestin. Le perimetre annonce ("contenu inchange hors
  numero, insertion et borne") est EXACTEMENT le perimetre observe.
  Le numero 69 est le premier libre : 66, 67 et 68 sont pris. La
  regle 66.5.e est executee a la lettre, la v3 reste intacte a BOCAL4,
  et le dossier trilemme v2 qui cite e5931c94 par empreinte reste
  valide sans retouche.

RESERVE DE LECTURE, NON BLOQUANTE : la re-emission etant fidele, elle
transporte l'ETAT PERIME que C-5 avait declare -- 69.4 "Tags immuables :
v1 88ed9158 ; v2 ; v3" alors que l'historique public a ete reecrit et
le tag v1-held re-emis (0ace0d19), et 69.7 "UNE SEULE CHOSE BLOQUE
ENCORE L'ENVOI : A3, depot prive" alors que le depot est PUBLIC et que
LE MAIL EST PARTI. C'est la consequence directe de "contenu inchange",
et c'est le bon arbitrage : une piece de registre ne se corrige pas en
la re-ecrivant. Le lecteur est protege par le bloc d'insertion, qui
renvoie a 66.6 -- section qui declare precisement cette desynchronisation.
Aucune v5 n'est demandee : le cout d'un cycle pour une ligne de caveat
n'est pas justifie quand le pointeur existe.

=======================================================================
3. REPONSE A LA QUESTION DE 63.2 -- LA LIGNE M2
=======================================================================
Machine 1 verse une observation d'extraction et demande sa validation :
"M2 est au sommaire des pre-enregistrements du maitre mais AUCUNE
section d'execution M2 n'apparait au journal gele".
L'OBSERVATION EST EXACTE, ET LE MAITRE PORTE LUI-MEME L'EXPLICATION.
Verifie ce jour dans journal_bundle5_v2026-07-25h.md, tel que servi par
le depot :
  "**M2 (en reserve) -- test du piegeage, deja pre-enregistre au §10.**
   Balayage w2 a occupation de rivage ~ 14 (g divise ~2). Prediction :
   vallee/bords remonte vers ou au-dessus de 1 si le regime actuel est
   du piegeage resonant fort. Faisabilite memoire : N <= 80-88."
La section suivante est "## 13. MANCHE M1 EXECUTEE", puis "## MANCHE M3
-- PRE-ENREGISTREMENT" et "## 15. MANCHE M3 EXECUTEE".
CONCLUSION OPPOSABLE : M2 a ete PRE-ENREGISTREE PUIS MISE EN RESERVE,
delibererement, et jamais executee ; la campagne passe de M1 a M3. Ce
n'est pas un trou du registre, c'est une reserve DECLAREE. La table de
la Release peut porter la mention telle quelle a condition d'ecrire
"en reserve, jamais executee" -- une case vide se lirait comme une
perte. Aucune reconciliation n'est due.

=======================================================================
4. LE BLOCAGE : TROIS PIECES SUR QUATRE NOMMENT L'OPERATEUR
=======================================================================
Le registre ordonnant (66.5) est le journal/ d'un depot PUBLIC ET
PSEUDONYMISE -- la re-coupe du 10/08 a substitue "baaz" au nom de
l'operateur sur l'ENSEMBLE de l'historique, et le delta 65 du depot
(5ad0561e) consigne cette decision. Or :
  delta 61, l.67  "placeholders restants cote <nom civil> : NOM, EMAIL"
  delta 63, l.33  "La piece attend la relecture de <nom civil>"
  delta 69, l.45  "SIGNATURE <nom civil> + mail -> A1 CLOS"
  delta 62        aucune occurrence
Deposer ces pieces en l'etat DE-PSEUDONYMISERAIT le depot public et
annulerait l'effet du delta 65. Je ne le fais pas, et je ne tranche pas
seul : c'est une decision d'operateur.

METHODE DEJA ETABLIE PAR LA CAMPAGNE (a appliquer si l'operateur la
retient) : deposer un DERIVE PSEUDONYMISE, nomme comme tel, l'original
restant intact a BOCAL4 et cite par empreinte -- exactement ce qui a ete
fait pour la revue pre-envoi (v1.1 originale 310e2171 chez machine 1,
derive pseudonymise 1344c0ff au depot, renomme au delta 67) et pour
l'ensemble de l'arbre par la re-coupe. Le delta 65 du depot consigne
deja le mapping sha16 ancien -> nouveau, fichier par fichier : la forme
existe, il suffit de l'etendre.

UN POINT DE SUBSTITUTION DEMANDE UN ARBITRAGE, PAS UNE REGLE :
  61 et 63 se substituent sans dommage ("cote <nom civil>" -> "cote
  operateur", "relecture de <nom civil>" -> "relecture de l'operateur") :
  la phrase garde son sens exact.
  69 NON. "SIGNATURE <nom civil> + mail" est le RELEVE DU CONTENU
  d'une piece signee et envoyee. Ecrire "SIGNATURE baaz" ferait dire au
  registre que la note a ete signee d'un pseudonyme -- c'est FAUX, et
  la note d est entre les mains d'un tiers qui peut le constater. Forme
  proposee, a valider : "SIGNATURE de l'operateur (nom civil en clair
  dans la piece signee) + mail". Une pseudonymisation ne doit jamais
  transformer un releve exact en releve faux.

=======================================================================
5. PRESCRIPTIONS (suite de N-36 ; N-37 et N-38)
=======================================================================
N-37  Toute piece entrant au registre ordonnant passe un CONTROLE
      NOMINATIF avant depot (recherche du nom civil et du courriel de
      l'operateur). Une occurrence => derive pseudonymise nomme comme
      tel, original intact chez son detenteur, mapping sha16 ancien ->
      nouveau consigne au delta de depot. Zero occurrence => depot
      direct. Le controle se declare dans le delta de depot, meme
      quand il ne trouve rien.
N-38  Une substitution de pseudonymisation ne doit JAMAIS rendre faux
      un releve exact. Quand le nom civil est l'OBJET du releve (et non
      son sujet), la substitution se fait par PERIPHRASE et non par
      pseudonyme, et l'ecart est declare au delta de depot.

=======================================================================
6. CE QUE CE CONTROLE NE JOUE PAS
=======================================================================
- Aucune verification du CONTENU technique des deltas 61, 62, 63 : je
  certifie leur integrite de canal et leur place dans la chaine, PAS
  les mesures qu'ils consignent. Les contre-epreuves qu'ils decrivent
  (tar.gz 3e9203d7, MANIFEST 180 lignes, 10 temoins) ne sont pas
  rejouees ici -- elles l'ont ete a l'epoque, des deux cotes.
- Le tar.gz 3e9203d7 correspond a l'ANCIENNE coupe (avant re-ecriture
  de l'historique) : les pieces 61-63 decrivent un etat du depot qui
  n'est plus servi. Meme famille que la reserve de la section 2.
- La piece RELEASE_NOTES_bundle-v1-held.md (delta 63) n'est pas au
  perimetre : elle n'a pas ete livree et n'est pas controlee.
- Aucun q_L, aucun inventaire, aucune mesure : cette note ne touche pas
  au trilemme. N-20 a N-38 restent opposables au gel de branche.
- Aucun numero de delta ni d'erratum attribue (E18).

PIECES CITEES (16 hex ; brut == canonique NFC+LF)
  deltas 61 18ad843d, 62 183ab8a1, 63 6b647dfa, 69 49c0f816 (recus) ;
  60 b67c2776 ; 64 f4552c5f ; 65 e5931c94 (machine 1) et 5ad0561e
  (depot) ; 66 ab5db7ef ; 67 6194e90f ; 68 a212a160 ; revue v1.1
  pseudonymisee 1344c0ff ; note d 74950a6b ; maitre bundle5 h (cite,
  servi par le depot).

=== FIN DE LA NOTE DE CERTIFICATION -- machine 2, v1 ===
