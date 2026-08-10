COUPE BUNDLE v1 (HELD) -- OUVERTURE, ETAT DE FAISABILITE, STOP
REGLEMENTAIRE SUR PIECES (machine 2, 2026-08-10)
=======================================================================
Auteur : machine 2. Date : 2026-08-10. Version : v1.
Piece recue : journal_delta_58_go_coupe.md -- CONTRESIGNE, custody
a42fb0d15450f517 (2268 octets, ASCII, CR = 0), copie BOCAL4
byte-identique. Borne effective D-1' = 58.
Verdict : GO HONORE PAR OUVERTURE IMMEDIATE ; la coupe s'arrete au
point que la procedure prevoit (directives 1a / 4b : piece absente ou
non certifiable -> STOP, consignation, pas de substitution
silencieuse). CE QUI EST PRET est verifie et liste (sect. 2) ; CE QUI
MANQUE vit cote machine 1 et tient en une liste courte (sect. 3).
Aucun montage partiel : les definitions de perimetre restantes ne se
resolvent pas en silence (lecon E29).

1. CE QUE L'OUVERTURE A VERIFIE (execute ce jour)
   a. Journal COMPLET 1..58 : pre-vol v2c rejoue apres consignation
      du delta 58, --max 58 : RETOUR 0 attendu au repertoire de
      coupe (le run --max 57 anterieur : 0, 57/57 ; delta 58 copie
      BOCAL4 byte-identique).
   b. RAPPROCHEMENT DES EMPREINTES-CLES DU REGISTRE DETENUES PAR
      MACHINE 2 : 21/22 RESOLVENT dans BOCAL4, bit-exactes --
      gel v4 35022c5c0784cb82 ; gel v3 e41f4da3 ; moteur c8ed357b
      (m9_replication_v1.py) ; pilote 663b17e2 (m12_pilote_v3.py) ;
      ponctuel M12 c5659f52 ; m15_site83 v1 d05cf50b / v2 41ddebcd ;
      patch 1824de78 ; JSONs bruts fa109da9 (M12), 70fe5611 (M13),
      22fa1760 (M13b), a38b8967 (M13L machine 2, CRLF), 68df6576
      (M14), 96d78407 (M15) ; log 6af16c16 ; remise 6ce6d793 ;
      cert. script v2 24f23b75 ; erratum E29 16c6d86e ; cert.
      croisee v4 29842047 / ec883c2a / 7ba90bc3.
   c. Note principale notes/ : note_outreach_EN_2026-07-25q.md
      PRESENTE (BOCAL4 racine).

2. PRET POUR LE MONTAGE, sans autre condition
   journal/ 1..58 integral (couverture certifiee v2c) ; gels et
   scripts de la lignee M12-M15 par empreintes (1.b) ; runs/ les six
   JSONs detenus + log + note de certification ; .gitattributes,
   README (gabarit sect. 5, redaction machine 2), LICENSE CC-BY 4.0
   et LICENSE-CODE MIT (D-B5 fige).

3. PIECES REQUISES AVANT MONTAGE (toutes cote machine 1) -- LA LISTE
   R-1  DIRECTIVES v2 (22f1194f). La coupe s'execute sous le
        TRIPLET directives v2 + arbitrage ee5da74f + delta 55
        (55.3) ; machine 2 ne detient que la v1 (87dc37ce,
        re-derivee ce jour). Le perimetre notes/ ("unifiee") n'est
        connu que d'elle.
   R-2  EXTRAIT DE REGISTRE DE COUPE : liste chemin relatif ->
        empreinte (convention ETIQUETEE par ligne : brut ou NFC+LF,
        16 ou 64 hex) pour CHAQUE fichier du perimetre -- en
        particulier les ensembles que machine 2 ne peut pas
        delimiter seule : "TOUS les gels certifies M1..M15",
        "artefacts M1-M11 au perimetre du registre", contenu exact
        de quartic-bundle/ (trois repertoires candidats localement :
        bundle_bocal, bocal_bundle2/bundle_bocal,
        bocal_bundle_3bis/bundle_bocal -- lequel, et quels
        fichiers). C'est la piece qui rend la verification 4b
        POSSIBLE ; sans elle toute delimitation serait une
        resolution silencieuse (E29).
   R-3  note_companion_EN_interdegree_v2.md -- absente de BOCAL4,
        Downloads et de tout le disque balaye.
   R-4  novelty_review.md (D-B3 : incluse) -- absente.
   R-5  CAMPAGNE_etat_complet 02/08 (D-B6 : incluse telle quelle) --
        absente SOUS CE NOM. SUIVI_campagne_2026-08-02b.md existe
        localement : si c'est la meme piece, le DIRE (avec
        empreinte) ; machine 2 ne tranche pas l'identite d'une
        piece par ressemblance de nom.
   R-6  JSON M13L canonique 641dbe3e (cloture, cote machine 1) --
        machine 2 ne detient que son propre a38b8967 (CRLF) ; les
        directives exigent LES DEUX avec ecart documente.
   R-7  STATUT de note_outreach_EN_unified_2026-08-10b.md, presente
        dans Downloads (ede00d94ad5fb61d, 53439 octets, re-derivee
        machine 2), CITEE PAR AUCUN delta : si elle est la piece
        "notes/ unifiee" des directives v2, la CONSIGNER (delta) ;
        sinon machine 2 l'ignore. Aucune piece non consignee
        n'entre au bundle (1a).
   R-8  (cote operateur, hors machine 1) : authentification GitHub
        de la machine 2 (`gh auth login`) ou depot prive
        pre-cree -- indisponible en l'etat, verifie ce jour.

4. ENGAGEMENT DE REPRISE
   A reception de R-1..R-7 (et R-8 regle) : montage du repertoire
   de coupe hors arborescence, verification ligne a ligne contre
   R-2, pre-vol v2c retour 0 a la borne re-derivee, README fige,
   MANIFEST sous Git Bash, commit 1 .gitattributes seul, commit 2
   bundle (message portant l'empreinte du MANIFEST), tag
   bundle-v1-held, push, tar.gz a machine 1 + clone frais machine 2
   (voie 55.6.d) -- en un seul mouvement, sans nouvel
   aller-retour attendu.

=== FIN DE LA CONSIGNATION DE COUPE (machine 2, v1) ===
