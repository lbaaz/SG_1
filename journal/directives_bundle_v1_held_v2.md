DIRECTIVES MACHINE 2 -- CONSTITUTION DU BUNDLE v1 (HELD), TRANSMISSION
GITHUB (machine 1, 2026-08-10) -- v2, POUR ARBITRAGE ET EXECUTION
(v2 : la note EN unifiee remplace la paire principale+compagne au
perimetre notes/ ; les deux notes d'origine restent au registre
interne, hors bundle. Rien d'autre ne change.)
=======================================================================
Objet : couper le bundle externe v1 -- instantane fige, versionne,
auto-porteur, manifeste par empreintes -- et le transmettre a A. Held
via un depot GitHub. La coupe est un instantane opposable : ni
publication, ni cloture de campagne, ni engagement. Le tronc (trilemme,
quantique) continue derriere.

0. DECISIONS PREALABLES (machine 2 arbitre ; machine 1 propose)
  D-B1  Perimetre du contenu : proposition = OPTION LARGE (sect. 2).
        Alternative minimale en sect. 2bis.
  D-B2  Note FR grand public : proposition = EXCLUE du bundle v1
        (chiffres perimes, lectorat autre). Si incluse : rafraichir
        d'abord, nouvelle version datee.
  D-B3  Revue d'anteriorite : proposition = INCLUSE en appendice
        (elle value la nouveaute, pas la correction -- sa presence est
        un acte d'honnetete qui cadre les claims). Sinon : la note
        compagne v2 sect. 9 en porte la synthese.
  D-B4  Visibilite du depot : proposition = PRIVE, invitation de Held
        comme lecteur (ou lien vers une release tar.gz). Public
        possible en v2 apres premier retour.
  D-B5  Licence : proposition = double -- CC-BY 4.0 (notes, journaux),
        MIT (scripts). A defaut de decision : AUCUNE licence au v1
        (tous droits reserves par defaut), decision differee.
  D-B6  Etat complet : la synthese CAMPAGNE_etat_complet la plus
        recente (02/08) precede M13-M15. Proposition = NE PAS la
        rafraichir pour la coupe (les deltas 47-54 font foi) ; l'
        inclure AVEC bandeau "as of 2026-08-02, superseded by deltas
        47-54", ou l'exclure. Trancher.

1. PRINCIPES DE CONSTITUTION
  a. SOURCES CERTIFIEES SEULEMENT : chaque fichier du bundle est la
     copie BOCAL4 dont l'empreinte figure au registre. Aucun fichier
     re-frappe, aucun export d'affichage. En cas d'ecart d'empreinte :
     STOP, consignation, pas de substitution silencieuse.
  b. AUTO-PORTEUR : tout renvoi cite dans une piece du bundle doit
     resoudre DANS le bundle ou etre liste en "external references"
     du README. Aucun fil pendant vers le registre vivant.
  c. FIGE : un commit unique "bundle v1 (Held)", un tag annote
     `bundle-v1-held`. Toute correction ulterieure = bundle v2,
     jamais d'amendement du tag v1.
  d. LE MANIFESTE EST LE CONTRAT : MANIFEST.sha256 liste chaque
     fichier avec son sha256 COMPLET (64 hex ; la convention B 16 hex
     reste l'usage interne, le manifeste externe porte le complet).
     Le README enonce : "verify with `sha256sum -c MANIFEST.sha256`".

2. PERIMETRE PROPOSE (OPTION LARGE, D-B1)
  bundle-v1/
    README.md                    <- ecrit par machine 2 depuis le
                                    gabarit de la sect. 5
    MANIFEST.sha256
    LICENSE / LICENSE-CODE       <- selon D-B5
    notes/
      note_outreach_EN_unified_2026-08-10.md   (note unique de
                                    diffusion ; empreinte au registre)
      [novelty_review.md]                      (selon D-B3)
    gels/          <- TOUS les gels certifies M1..M15 + gel v4
                      heritage 35022c5c (les pre-enregistrements sont
                      le coeur de la credibilite ; n'en retirer aucun)
    scripts/       <- moteur c8ed357b ; pilote 663b17e2 ; ponctuel
                      M12 c5659f52 ; scripts M13/M13b/M13L/M14 ;
                      m15_site83_v2 41ddebcd ;
                      patch_gel_m15_v3_to_v4.py 1824de78
    runs/          <- JSONs primaires : fa109da9 (M12), 70fe5611
                      (M13), 22fa1760 (M13b), 641dbe3e (M13L
                      cloture canonique) + a38b8967 (fichier machine
                      2, CRLF, tel quel -- les DEUX, l'ecart CRLF est
                      documente), 68df6576 (M14), 96d78407 (M15) +
                      log 6af16c16 + note de certification 24f23b75 ;
                      + artefacts M1-M11 au perimetre du registre
    journal/       <- deltas 1..54 INTEGRAUX + errata (dont E29
                      16c6d86e) + certifications croisees (dont gel
                      v4 : 29842047 / ec883c2a / 7ba90bc3). Les
                      fautes des deux signataires y figurent : elles
                      RESTENT (sect. 10 de la note compagne en fait
                      un argument, pas une gene).
    quartic-bundle/ <- le bundle quartique original (~1.1 Mo) de la
                      note principale, tel que deja re-execute,
                      inchange.
  2bis. OPTION MINIMALE (si D-B1 = minimal) : notes/ + gels/ +
     MANIFEST + README + les six JSONs inter-degres + moteur +
     quartic-bundle. Les journaux restent alors disponibles "on
     request" -- l'offre figure au README.

3. PIEGES DE PLATEFORME (BOCAL4 = Windows ; precedents N-10, N-16)
  a. `.gitattributes` A LA RACINE, PREMIER fichier commite, contenu
     exact : une ligne `* -text` (aucune conversion de fin de ligne,
     jamais). SANS ce fichier, git/GitHub peut recrire CRLF/LF et
     TOUTES les empreintes du manifeste meurent silencieusement.
  b. `git config core.autocrlf false` dans le clone local AVANT tout
     add. Verifier : `git config --get core.autocrlf` -> false.
  c. Pas d'edition de fichiers via l'interface web GitHub (elle peut
     normaliser). Tout passe par push local.
  d. Si un rejeu est documente au README : mentionner PYTHONUTF8=1
     (N-16) pour les scripts a sortie unicode sous Windows.

4. PROCEDURE (ordre strict)
  a. Repertoire de coupe local, HORS arborescence de travail.
     Copier les pieces (sect. 2) depuis leurs emplacements certifies.
  b. Verifier CHAQUE empreinte contre le registre AVANT git init :
     `sha256sum *` recursif, rapprochement ligne a ligne. Ecart ->
     STOP (1a).
  c. Generer MANIFEST.sha256 (chemins relatifs, separateur '/',
     ordre lexicographique). L'auto-test : `sha256sum -c
     MANIFEST.sha256` -> tout OK. Le MANIFESTE ne se liste pas
     lui-meme ; le README ne s'y liste pas non plus s'il doit encore
     bouger (proposition : il s'y liste, donc il se fige AVANT la
     generation).
  d. `git init` ; commit 1 = `.gitattributes` seul ; commit 2 =
     tout le bundle, message "bundle v1 (Held) -- manifest sha256:
     <empreinte du MANIFEST lui-meme>". Tag annote `bundle-v1-held`.
  e. Depot GitHub neuf (nom propose : `pu-ghost-campaign-bundle`),
     visibilite selon D-B4. Push + tag.
  f. CONTRE-EPREUVE OBLIGATOIRE : clone FRAIS dans un repertoire
     vierge (idealement l'autre machine physique si disponible),
     `sha256sum -c MANIFEST.sha256` -> 100% OK. C'est le seul test
     qui prouve que la plateforme n'a rien recrit.
  g. Consignation (machine 1, delta suivant, numero a l'acte) :
     empreinte du MANIFEST, hash du commit, nom du tag, URL, verdict
     de la contre-epreuve. Le mail a Held ne part qu'APRES ce delta.
  h. Invitation/partage a Held selon D-B4 ; le mail (livre a part)
     porte l'URL + l'empreinte du MANIFEST en une ligne.

5. GABARIT README (a rediger machine 2 ; EN ; une page max)
  - Titre, une phrase de contexte, lien vers notes/ comme point
    d'entree (une seule note : la note unifiee 2026-08-10).
  - "What this is / is not" : instantane fige d'une campagne en
    cours ; pas une publication.
  - Verification : la ligne sha256sum -c ; note plateforme (LF
    partout, `.gitattributes` en garantit la preservation).
  - Structure du depot (l'arbre de la sect. 2, une ligne par
    repertoire).
  - Contact + l'offre "journaux integraux on request" si D-B1 =
    minimal.
  - AUCUN chiffre scientifique dans le README : les chiffres vivent
    dans les notes et les artefacts.

6. CE QUE CES DIRECTIVES NE COUVRENT PAS
  Le contenu du mail (livre separement) ; la decision de coupe
  elle-meme et les six decisions D-B1..D-B6 (machine 2) ; tout
  rafraichissement de note FR (D-B2) ; la reponse de Held.

=== FIN DES DIRECTIVES (bundle v1, machine 1, POUR ARBITRAGE) ===
