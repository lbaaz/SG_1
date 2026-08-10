JOURNAL DELTA 60 -- MONTAGE ENREGISTRE, ARBITRAGE R-6 (FAUTE MACHINE 1
VERSEE), DEUX FICHIERS FOURNIS, PRESCRIPTION GEL-JUMEAU (machine 1,
2026-08-10)
=======================================================================
S'insere apres journal_delta_59_stop_pieces.md (10efa4b4, CONTRESIGNE).

60.1 RECEPTION ET ENREGISTREMENTS
  note_machine2_coupe_montage_v1.md : consignee, 3bbb370408f3d736
  (6303 octets, ASCII, CR = 0, LF final unique). Enregistres : 4b
  executee contre le registre entier (88/95 resolues bit-exactes ;
  69d1d01d DERIVEE EXACTE = forme LF de a5fddbc6, rejouee) ; montage
  fait hors arborescence, 24 pieces ligne a ligne, 145 additions au
  log, 0 erreur de copie ; PRE-VOL v2c sur le repertoire de coupe :
  --max 59, RETOUR 0, 59/59 ; racine ecrite (.gitattributes
  705fd4d6, LICENSE f5ceec5c, LICENSE-CODE 047d85cb, README
  BROUILLON c0f8b5b4) ; placements consignes.

60.2 R-6 : FAUTE MACHINE 1 VERSEE, ARBITRAGE ADOPTE
  (i) La faute, verifiee CE JOUR sur piece : le delta 59 enoncait
  une voie de derivation et une attente (641dbe3e) SANS extraction
  depuis la piece porteuse -- delta 49, COPIE PROJET DETENUE, dont
  la sect. 49.7 porte en toutes lettres : a38b8967 (CRLF) == contenu
  LF 15efb410 ; JSON machine 1 d10b27f5 (LF, etiquette machine 1) ;
  cloture canonique 641dbe3e31b51897... = forme du COMPARATEUR
  (LF + etiquettes normalisees + date omise), identique des deux
  cotes, JAMAIS consignee comme fichier. Lecon, la meme qu'a 49.5 :
  on re-derive depuis l'artefact detenu, jamais depuis la memoire
  -- meme pour ecrire une "voie de derivation". La diligence
  machine 2 (variantes jouees puis ARRET : "continuer jusqu'a
  coincidence serait ajuster la regle a la reponse") est la
  discipline exacte ; contresignee.
  (ii) PROPOSITION MACHINE 2 ADOPTEE, regle uniforme pour les deux
  canoniques : les fichiers BRUTS entrent (a38b8967 ; a5fddbc6) ;
  641dbe3e et 69d1d01d restent des VALEURS DE REGISTRE portees par
  des pieces DU bundle (delta 49 ; etat complet l. 437 et registre
  de coupe). AUCUNE materialisation (option declinee) : aucun
  fichier fabrique ; la recette de 69d1d01d tient en une commande
  documentee, celle de 641dbe3e vit dans les implementations citees
  au delta 49. d10b27f5 : meme regle -- valeur de registre portee
  par le delta 49 ; si le fichier resout un jour, il entre en
  multi-version, sinon rien ne se fabrique.

60.3 POINTS 5a-5c : TRANCHES
  5a CONFIRME : le montage porte le NOM REEL du fichier consigne,
     note_outreach_EN_unified_2026-08-10b.md (ede00d94) ; les
     directives v2 ne se re-editent pas (PB-1), l'ecart de nom est
     consigne ici et le MANIFEST fait foi.
  5b CONSIGNE : depot SG_1 (prive, compte lbaaz, push/admin
     verifies) ; le nom des directives 4e etait une proposition ;
     l'URL reelle entre au delta de consignation de la coupe.
  5c PAS DE VETO : la designation deleguee par l'operateur et le
     choix bocal_bundle_3bis/bundle_bocal sont ADOPTES -- le critere
     etait OPERATIONNEL et le choix le suit (le repertoire PORTE
     compare_worst_v2, la piece re-executee du contrat de
     provenance A) ; l'ecart de taille vs "~1.1 Mo" et les 14
     fichiers communs divergents avec l'etat anterieur sont
     consignes tels quels ; le manifeste recursif
     quartic-bundle-MANIFEST-2026-08-10.sha256.txt (f2c95d29,
     57 lignes, sha256 complets) = piece neuve datee, conforme
     PB-1/R-8, AU bundle.

60.4 LES CINQ FICHIERS : DEUX FOURNIS, TROIS EN PRESCRIPTION
  FOURNIS ce jour, re-derives contre les cibles de la sect. 6 :
    gels/m6_pre_enregistrement.md            3a629fb0e05db01d ==
    journal/journal_delta_46_run_M12_ponctuel.md  86bfdca13f5457ae ==
    (v1 remplacee par v2 344e7730 -- multi-version, PB-3a : les
    deux entrent.)
  NON DETENUS comme fichiers cote machine 1 (ni projet, ni
  transcripts, ni embarques aux journaux du projet -- balayage par
  CONTENU execute ce jour, motif "PRE-ENREGISTREMENT M(7|9|10)") :
  gels M7 5c54ac03, M9 v2 90019eba, M10 v8 c1d42aa5. La note de
  montage les disait "copie projet machine 1" : c'etait une
  supposition, le registre de coupe les portait en grade B
  (valeurs), pas en grade A (fichiers).
  PRESCRIPTION D'EXTRACTION GEL-JUMEAU (regle 12, convention
  bloc = fichier) -- les scripts certifies de l'epoque portent le
  gel en docstring (atteste par le gel M10 v1 lui-meme, l. 170 :
  "docstring, bloc de PRE-ENREGISTREMENT M10 a === FIN DU GEL M10
  ===", et par le gel M15 v3) ; un balayage par empreinte ne voit
  pas un bloc embarque. Sur BOCAL4, sur les scripts RESOLUS :
    (a) m10_exposant_v3.py (c3a91f60) : extraire le bloc du titre
        "PRE-ENREGISTREMENT M10" a "=== FIN DU GEL M10 ===" inclus,
        + LF final, NFC ; hacher. Si == c1d42aa5 : gel M10 v8
        RECUPERE par extraction sanctionnee, il ENTRE.
    (b) m9_replication_v1.py (c8ed357b) : meme geste, titre M9,
        cible 90019eba.
    (c) M7 (5c54ac03, aucun porteur connu) : grep de CONTENU
        "PRE-ENREGISTREMENT M7" sur le corpus resolu BOCAL4 ;
        si un porteur apparait, meme extraction.
  Tout resultat se CONSIGNE, egal ou non ; un bloc qui hache
  autrement s'arrete la (pas d'ajustement a la reponse). ECHEC
  RESIDUEL : absence consignee, entree VALEUR-DE-REGISTRE seule
  (portee par l'etat complet, present au bundle), fichier au v2
  s'il se retrouve -- la coupe ne reste pas otage de l'archeologie
  de juillet ; baaz peut prefererer bloquer, c'est sa decision.

60.5 ETAT
  Borne re-derivee : 60 par le present acte. Reste, tout cote
  machine 2 : copier+verifier les deux fournis ; jouer la
  prescription 60.4 et consigner ses verdicts ; puis le mouvement
  unique de la sect. 7 du montage -- README fige, MANIFEST sous
  Git Bash, commit 1 .gitattributes, commit 2 (message avec
  l'empreinte du MANIFEST), tag bundle-v1-held, push SG_1, tar.gz a
  machine 1, clone frais. Puis delta de consignation (HORS bundle)
  et le mail, [HASH] = empreinte du MANIFEST.

=== FIN DU JOURNAL DELTA 60 ===
