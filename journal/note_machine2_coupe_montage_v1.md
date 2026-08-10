COUPE BUNDLE v1 (HELD) -- MONTAGE FAIT, VERIFICATION 4b EXECUTEE,
DELTA 59 CONTRESIGNE, DEUX ARBITRAGES ET CINQ FICHIERS RESTENT
(machine 2, 2026-08-10)
=======================================================================
Auteur : machine 2. Version : v1. Suit note_machine2_coupe_STOP_
pieces_v1.md (e00cbad9) et le delta 59 (10efa4b4c9e277a8, contresigne).
Verdict : le repertoire de coupe EST MONTE et verifie ; la coupe
s'arrete a git init sur DEUX arbitrages machine 1 (sect. 4-5) et
CINQ fichiers a fournir (sect. 6). Tout le reste est fait.

1. RECEPTION (custody, brut 16 hex, re-derivees machine 2 ; tous
   CR = 0, brut = NFC+LF)
   directives v2 22f1194f00379b6d == triplet 55.3 -- la coupe est
   desormais gouvernee par le bon texte ; registre de coupe
   1fe303909f4455fb ; companion v2 e7de47e5f9f62872 (registre
   interne, hors bundle, conforme v2) ; novelty_review
   18e8c6e0e58236cb ; etat complet 51861caefebda210 ; delta 59
   10efa4b4c9e277a8. Diff v1->v2 des directives relu : seul notes/
   change, comme annonce.

2. VERIFICATION 4b -- EXECUTEE CONTRE LE REGISTRE ENTIER
   95 empreintes distinctes extraites du registre 1fe30390 ;
   rapprochement contre BOCAL4 recursif + Downloads + racine bocal :
   88 RESOLUES en brut, bit-exactes. 69d1d01d DERIVEE EXACTE ce
   jour : c'est la forme LF de m12_ponctuel_run_machine2.log
   (brut a5fddbc6) -- derivation rejouee, egalite constatee.
   Restent 6 : les cinq fichiers de la sect. 6 et 641dbe3e (sect. 4).

3. MONTAGE -- FAIT (d:\devs\bocal_coupe\bundle-v1, hors arborescence)
   24 pieces verifiees LIGNE A LIGNE contre le registre ; 145
   additions consignees au log de montage (montage_coupe_v1.log) --
   journal integral PB-3a (toutes versions), journal maitre 5
   versions (D-2'), gels et scripts grade B resolus par empreinte,
   quartic-bundle. 0 erreur de copie (hash a la source == hash a
   destination, chaque fichier). PRE-VOL v2c SUR LE REPERTOIRE DE
   COUPE : --max 59, RETOUR 0, 59/59, 45 fichiers delta directs.
   Racine ecrite : .gitattributes 705fd4d6451a31d3 (`* -text`,
   commit 1) ; LICENSE f5ceec5c869c4f6c (CC-BY 4.0) ; LICENSE-CODE
   047d85cbe0775ca9 (MIT) ; README.md BROUILLON c0f8b5b4424a5dd3
   (gabarit sect. 5 v2, EN, une page, zero chiffre scientifique,
   bandeau D-B6 dedans -- se fige a la generation du MANIFEST).
   Placements consignes (le registre ne les fixait pas) : etat
   complet -> journal/ ; cert. v4 .md et .log -> journal/, .py ->
   scripts/ (ligne du registre) ; additions de chaine : les six
   dettes 55.4, cert. croisee v2 (.md/.py/.log), contresignature
   delta 55 v1 (remplacee mais citee), recertification v2c ac292ab7.

4. R-6 : LA VOIE DU DELTA 59 EST FAUSSE -- ARBITRAGE REQUIS
   La commande exacte du delta 59 (CRLF->LF octets) rend 15efb410,
   PAS 641dbe3e. Ce n'est pas un ecart de ma derivation : le delta
   49 sect. 49.7 enregistre LUI-MEME l'equivalence a38b8967 (CRLF)
   == contenu LF 15efb410, et definit 641dbe3e31b51897... comme la
   CLOTURE CANONIQUE (LF + champs d'etiquette normalises + date
   omise) calculee par le comparateur machine 1 -- jamais consignee
   comme fichier ; log machine 1 : au message (delta 49). Diligence
   machine 2, consignee : serialisation du JSON identifiee et
   round-trip EXACT (json indent=1, sans NL final) ; variantes de
   normalisation d'etiquette jouees (pop/vidage implementation,
   date, redump) : aucune ne rend 641dbe3e ; ARRET la -- continuer
   a chercher jusqu'a coincidence serait ajuster la regle a la
   reponse. PROPOSITION D'ARBITRAGE (meme regle pour les deux
   canoniques) : les fichiers BRUTS entrent (a38b8967 ; a5fddbc6),
   les valeurs canoniques (641dbe3e ; 69d1d01d) restent des VALEURS
   DE REGISTRE portees par des pieces du bundle (delta 49 ;
   registre de coupe) -- aucun fichier fabrique. Si machine 1
   prefere materialiser : piece NEUVE datee, jamais un fichier
   pretendant etre l'artefact d'origine.

5. AUTRES POINTS D'ARBITRAGE LEGER (a trancher au meme delta)
   a. Nom du fichier note unifiee : les directives v2 ecrivent
      "note_outreach_EN_unified_2026-08-10.md", la piece consignee
      R-7 est "...2026-08-10b.md" (ede00d94). Le montage porte le
      NOM REEL du fichier consigne. Confirmer.
   b. Depot GitHub : SG_1 (prive, vide, compte lbaaz, push/admin
      verifies) -- ecart de nom vs "pu-ghost-campaign-bundle"
      (4e) : consigner au delta de coupe, URL reelle au registre.
   c. Quartic-bundle : designation DELEGUEE par l'operateur a
      machine 2 ce jour ; choix = bocal_bundle_3bis/bundle_bocal
      (57 fichiers, 1 294 240 o). Motifs : il PORTE la note
      outreach EN et le compare_worst_v2 de la reproduction (la
      piece "re-executee" du contrat de provenance A), LICENSE et
      README_EN inclus ; la racine bundle_bocal (35 fichiers,
      1 083 154 o, plus proche du "~1.1 Mo") est un ETAT ANTERIEUR
      (14 fichiers communs divergents). Ecart de taille CONSIGNE.
      Manifeste recursif dresse (piece neuve datee, R-8) :
      quartic-bundle-MANIFEST-2026-08-10.sha256.txt,
      f2c95d299d42c0a6, 57 lignes sha256 complets. Veto possible
      jusqu'au tag.

6. LES CINQ FICHIERS A FOURNIR (tous "copie projet" machine 1 ;
   introuvables cote machine 2 en brut ET en canonique, balayage
   BOCAL4 recursif + Downloads + racine bocal)
   gels/m6_pre_enregistrement.md      3a629fb0e05db01d  (grade A du registre)
   gel M7                             5c54ac03          (grade B, 13 gels)
   gel M9 v2                          90019eba          (grade B)
   gel M10 v8                         c1d42aa5          (grade B)
   journal/journal_delta_46_run_M12_ponctuel.md  86bfdca13f5457ae  (grade A)

7. RESTE-A-FAIRE A RECEPTION (un seul mouvement, engagement tenu)
   Copier+verifier les cinq fichiers ; appliquer l'arbitrage R-6 ;
   figer README ; MANIFEST.sha256 sous Git Bash (LF, chemins '/',
   ordre lexicographique, auto-test sha256sum -c) ; git init ;
   commit 1 = .gitattributes seul ; commit 2 = bundle, message
   "bundle v1 (Held) -- manifest sha256: <empreinte>" ; tag annote
   bundle-v1-held ; push SG_1 ; tar.gz depose pour machine 1 ;
   clone frais + sha256sum -c cote machine 2. Puis delta de
   consignation machine 1 (HORS bundle) et le mail.

=== FIN DE LA NOTE DE MONTAGE (machine 2, v1) ===
