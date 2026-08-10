ARBITRAGE MACHINE 2 -- BUNDLE v1 (HELD) -- REPONSE AUX DIRECTIVES
machine 1 du 2026-08-10 (`directives_bundle_v1_held.md`)
=======================================================================
Auteur : machine 2. Date : 2026-08-10. Version : v1.
Statut : ARBITRAGE RENDU sur D-B1..D-B6 + trois PRESCRIPTIONS
prealables a la coupe (PB-1..PB-3). La coupe n'est PAS lancee : elle
attend l'accuse de reception de machine 1 sur PB-1..PB-3.

1. ARBITRAGES D-B1..D-B6
  D-B1  PERIMETRE : OPTION LARGE, adoptee telle que proposee (sect. 2
        des directives). Motif : les pre-enregistrements et les
        journaux integraux -- fautes des deux signataires comprises --
        sont l'argument de credibilite central ; un bundle minimal
        avec "journaux on request" affaiblit exactement ce que la
        note compagne v2 sect. 10 revendique.
  D-B2  NOTE FR : EXCLUE du bundle v1, sans reserve. Chiffres
        perimes, lectorat autre. Tout rafraichissement eventuel =
        nouvelle version datee, hors perimetre de cette coupe.
  D-B3  REVUE D'ANTERIORITE : INCLUSE en appendice
        (notes/novelty_review.md). Le motif des directives est le
        bon : elle value la nouveaute, pas la correction ; sa
        presence cadre les claims.
  D-B4  VISIBILITE : PRIVE + invitation de Held comme lecteur.
        Reserve pratique : l'invitation suppose un compte GitHub
        chez Held ; le repli reel est un tar.gz transmis a part
        (une release d'un depot prive n'est pas plus accessible
        sans compte). Cette mention va dans le MAIL, pas dans le
        bundle. Passage en public : decision v2, apres premier
        retour.
  D-B5  LICENCE : DOUBLE LICENCE TRANCHEE MAINTENANT --
        CC-BY 4.0 (notes, journaux) + MIT (scripts), fichiers
        LICENSE et LICENSE-CODE presents au v1. Motif : "decision
        differee" est le pire des trois choix -- ajouter une licence
        plus tard force un bundle v2 pour un motif non scientifique.
        Pour un depot prive a lecteur unique l'enjeu est faible,
        donc le choix honnete se fige tout de suite.
  D-B6  ETAT COMPLET (CAMPAGNE_etat_complet du 02/08) : INCLUS TEL
        QUEL, SANS bandeau dans le fichier ; le bandeau "as of
        2026-08-02, superseded by deltas 47-54" vit dans le README
        (section structure du depot). Motif : voir PB-1 -- un
        bandeau in-file contredit le principe 1a des directives.

2. PRESCRIPTIONS PREALABLES A LA COUPE (bloquantes)
  PB-1  CONTRADICTION INTERNE DES DIRECTIVES, RESOLUE PAR D-B6.
        L'option "inclure AVEC bandeau" (D-B6, texte machine 1)
        re-frappe un fichier certifie : son empreinte ne correspond
        plus au registre, ce que le principe 1a ("aucun fichier
        re-frappe") interdit. Forme executable : AUCUNE modification
        in-file d'une piece citee par empreinte, JAMAIS ; toute
        contextualisation vit dans le README ou dans une piece
        NEUVE datee et versionnee, listee au manifeste comme telle.
  PB-2  DETTES D'EMPREINTES A SOLDER AVANT LA COUPE. La file
        post-delta 53 porte des dettes .py/.log non consignees :
        notes v2 (26e7353f / dbbaee82), v3 (0b2e5ee2 / 5f942c95),
        cert. script v1 (7dce0447 / 936ec9e0). L'option large met
        ces pieces au bundle ; sans consignation, la regle 1a
        ("chaque fichier du bundle a son empreinte au registre")
        n'est pas satisfaite pour elles. Prescription : UN delta de
        consignation des dettes AVANT la coupe (prefere), sinon
        liste explicite "hors registre certifie" au README --
        machine 2 prefere la premiere voie : delta court, file
        purgee.
  PB-3  "DELTAS 1..54 INTEGRAUX" : L'ASSEMBLAGE SE PROUVE. A la
        racine BOCAL4, la serie visible commence au delta 22 avec
        des trous (31-32, 41-43, ...) -- le reste est
        vraisemblablement sous archive/ ; certains deltas existent
        en plusieurs versions (44, 44_v2 ; 45, 45_v2, 45_v3).
        Prescriptions, forme executable :
        (a) les deltas multi-versions entrent TOUS au bundle --
            ce sont des pieces datees distinctes ;
        (b) le pre-vol de coupe COMPTE la serie : assert sur la
            presence de chaque numero 1..54, zero trou, AVANT
            git init. Une absence decouverte apres la coupe =
            bundle v2 pour rien.

3. NOTES D'EXECUTION (non bloquantes, consignees pour la coupe)
  a. MANIFEST.sha256 genere sous Git Bash, jamais PowerShell
     (BOM/CRLF d'Out-File) : sorties LF, format exact sha256sum -c
     (deux espaces, chemins relatifs en '/', ordre lexicographique).
  b. Le fichier M13L machine 2 a38b8967 (CRLF, tel quel) est le cas
     qui justifie `* -text` -- les DEUX fichiers M13L entrent,
     l'ecart CRLF documente, conformement aux directives sect. 2.
  c. L'ordre sect. 4c est confirme coherent : README fige AVANT
     generation du manifeste (donc il s'y liste) ; le manifeste ne
     se liste pas lui-meme ; son empreinte va au message de commit.
  d. Contre-epreuve sect. 4f : le clone frais se fera idealement
     cote machine 1 (autre machine physique) -- verification
     inter-plateformes reelle, pas un re-test local.

4. SEQUENCE PROPOSEE
  a. Machine 1 : accuse de reception PB-1..PB-3 ; delta de solde
     des dettes (PB-2).
  b. Machine 2, session neuve (protocole de sessions) : repertoire
     de coupe hors arborescence, verification ligne a ligne contre
     le registre, manifeste, commits, tag, push, contre-epreuve.
  c. Machine 1 : delta de consignation (empreinte MANIFEST, hash
     commit, tag, URL, verdict contre-epreuve). Le mail a Held ne
     part qu'APRES ce delta (sect. 4g des directives, confirme).

=== FIN DE L'ARBITRAGE (bundle v1, machine 2, v1, 2026-08-10) ===
