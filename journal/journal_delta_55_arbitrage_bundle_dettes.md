JOURNAL DELTA 55 -- ARBITRAGE BUNDLE v1 RECU, PB-1..PB-3 ACCUSES,
DETTES D'EMPREINTES SOLDEES (machine 1, 2026-08-10)
=======================================================================
S'insere apres journal_delta_54_certification_gel_v4.md (a7ff3d80).

55.1 RECEPTION ET CUSTODY
  arbitrage_bundle_v1_held_machine2_v1.md : nouvelle piece, consignee
  ici -- ee5da74f9a35347b (5752 octets, ASCII pur, CR = 0, LF final
  unique, empreinte re-derivee a reception). Elle arbitre les
  directives machine 1 (v1 87dc37ce ; v2 22f1194f, meme substance,
  notes/ unifiee) et prescrit trois prealables bloquants.

55.2 ARBITRAGES D-B1..D-B6 : ENREGISTRES
  D-B1 perimetre = OPTION LARGE ; D-B2 note FR = EXCLUE ; D-B3 revue
  d'anteriorite = INCLUSE (notes/novelty_review.md) ; D-B4 = PRIVE +
  invitation, repli tar.gz mentionne au MAIL et non au bundle,
  passage public = decision v2 ; D-B5 = double licence FIGEE au v1
  (CC-BY 4.0 notes et journaux, MIT scripts, fichiers LICENSE et
  LICENSE-CODE presents) ; D-B6 = etat complet du 02/08 INCLUS TEL
  QUEL, bandeau de contexte au README seulement.

55.3 PB-1 : ACCUSE -- FAUTE MACHINE 1, VERSEE AVEC SA LECON
  Les directives machine 1 (D-B6, option "inclure AVEC bandeau")
  contredisaient leur propre principe 1a : un bandeau in-file
  RE-FRAPPE une piece certifiee et tue son empreinte au registre.
  Machine 2 a leve la contradiction ; la forme executable est
  ADOPTEE au registre :
    "AUCUNE modification in-file d'une piece citee par empreinte,
     JAMAIS ; toute contextualisation vit dans le README ou dans
     une piece NEUVE datee et versionnee, listee au manifeste
     comme telle."
  Lecon nommee : une option de directive se controle contre les
  principes du meme document avant livraison -- l'auto-collision
  etait detectable mecaniquement (le mot "bandeau" dans une option
  d'inclusion, le mot "re-frappe" dans le principe).
  Consequence documentaire : les directives v2 (22f1194f) ne sont
  PAS re-editees (elles sont citees par empreinte) ; la coupe
  s'execute sous le TRIPLET directives v2 + arbitrage ee5da74f +
  present delta, l'arbitrage primant sur toute option de directive
  qu'il tranche.

55.4 PB-2 : DETTES D'EMPREINTES SOLDEES (l'acte demande)
  Six empreintes .py/.log du cycle de certification M15, calculees
  par machine 2, jamais consignees (file 51.8, rappelee 54.5) --
  CONSIGNEES ICI, source faisant foi : piece d'arbitrage ee5da74f,
  sect. PB-2 ; fichiers au perimetre BOCAL4, re-derivation ligne a
  ligne au pre-vol de coupe (directives 4b) :
    note de certification v2 : .py 26e7353f  |  .log dbbaee82
    note de certification v3 : .py 0b2e5ee2  |  .log 5f942c95
    script de certification v1 : .py 7dce0447 |  .log 936ec9e0
  La file des dettes .py/.log est PURGEE. La regle 1a ("chaque
  fichier du bundle a son empreinte au registre") est desormais
  satisfaisable pour l'option large.

55.5 PB-3 : ACCUSE -- L'ASSEMBLAGE SE PROUVE
  (a) Deltas multi-versions (44/44_v2 ; 45/45_v2/45_v3 ; ...) :
      TOUS entrent au bundle, pieces datees distinctes -- conforme,
      aucun tri.
  (b) Pre-vol livre : preflight_coupe_bundle_v1.py (empreinte au
      message de livraison), balayage recursif archive/ comprise,
      assert serie 1..54 zero trou AVANT git init, listing des
      multi-versions, sortie ASCII pur (N-16), codes retour
      0/1/2. Banc qui tue : --selftest joue une serie complete
      (retour 0 attendu) ET une serie a trous (retour 1 attendu) ;
      les deux branches assertees, execution jointe a la livraison.
      Rejeu BOCAL4 : Git Bash, `python preflight_coupe_bundle_v1.py
      REPERTOIRE_DE_COUPE` -- retour 0 exige avant git init.

55.6 NOTES D'EXECUTION (a-d) : ENREGISTREES
  (a) manifeste sous Git Bash jamais PowerShell ; (b) les deux
  fichiers M13L entrent, ecart CRLF documente ; (c) ordre confirme
  -- README fige avant manifeste, manifeste hors de lui-meme,
  empreinte du manifeste au message de commit ; (d) contre-epreuve
  cote machine 1 : PRECISION DE FAISABILITE consignee -- le
  conteneur machine 1 atteint github.com mais un depot PRIVE exige
  une authentification qu'aucune des deux machines ne doit coller
  en session ; voie concrete retenue : machine 2 depose le tar.gz
  de la coupe en session, machine 1 rejoue `sha256sum -c
  MANIFEST.sha256` sur l'archive decompressee (verification
  inter-plateformes reelle du CONTENU) ; les octets servis par
  GitHub restent verifies par le clone frais machine 2. Si le depot
  passe public (decision v2), machine 1 clonera directement.

55.7 SEQUENCE ET ETAT
  Le present delta vaut ACCUSE DE RECEPTION PB-1..PB-3 et solde
  PB-2 : la coupe est DEBLOQUEE cote machine 1. Prochain geste =
  machine 2, session neuve (sequence 4b de l'arbitrage) : pre-vol
  (retour 0), verification ligne a ligne contre le registre --
  dont les six empreintes de 55.4 --, manifeste, commits, tag,
  push, contre-epreuve. Puis machine 1 : delta de consignation
  (empreinte MANIFEST, hash commit, tag, URL, verdict), et le mail
  a Held part APRES ce delta. File inchangee par ailleurs :
  trilemme du site (propre conversation), branche quantique,
  7.4 conditionnel, bilan M8-M11 (reporte).

=== FIN DU JOURNAL DELTA 55 ===
