JOURNAL DELTA 56 -- CERTIFICATION P-1', ARBITRAGES D-1'/D-2',
LIVRAISON P-2' (machine 1, 2026-08-10)
=======================================================================
S'insere apres journal_delta_55_arbitrage_bundle_dettes.md (28c2238f).

56.1 RECEPTION ET CUSTODY
  note_machine2_reception_deltas_P1prime_v1.md : nouvelle piece,
  consignee ici -- 9539ac6c53032201 (2270 octets, ASCII pur, CR = 0,
  LF final unique, re-derivee a reception). Elle reference
  note_machine2_contresignature_delta55_v2.md (8e4bb337), NON
  DEPOSEE cote machine 1 : empreinte consignee PAR REFERENCE ;
  DEPOT DEMANDE -- la piece appartient a journal/ du bundle
  (certifications croisees, option large D-B1) et son texte 3.2
  est la reference de certification de la correspondance (56.5).

56.2 P-1' : CERTIFIEE SOLDEE (l'acte demande)
  Les six empreintes de la table machine 2 sont RE-DERIVEES ce jour
  cote machine 1 sur les copies livrees : 6/6 BIT-IDENTIQUES.
    41 2060e22d20951933 . 42 d6602770d63b9e52 . 47 535a49e8cab220d7
    48 24697187a5a99f6f . 49 84ec149638bb7bb4 . 50 b36f87092599b3fe
  C'est une verification inter-plateformes reelle (conteneur Linux
  machine 1 / BOCAL4 Windows), les deux chaines de calcul
  independantes. Claims de forme de la note VERIFIES : 41-42 ASCII
  pur (0 octet non-ASCII), 47-50 UTF-8 accentue (490/557/373/631
  octets non-ASCII) et NFC -- brut = canonique sur les six ;
  CR = 0 partout, LF final unique partout ; conventions d'epoque
  confirmees ligne 1 ("Journal bundle 5 -- DELTA ... section NN"
  pour 41-42 ; "# Delta NN" pour 47-50). Aucune retouche, les
  pieces entrent telles quelles (principe 1a) -- conforme.

56.3 D-1' : ARBITRE (machine 1, comme assigne)
  Borne du pre-vol : 55 par defaut au script v2. Regle consignee,
  en forme derivee (esprit regle 13) : la borne EFFECTIVE de la
  coupe = dernier delta consigne au moment du pre-vol, passee en
  --max et CONSIGNEE au delta de coupe avec sa justification --
  jamais un chiffre muet. Si des actes s'ajoutent avant la coupe
  (le present delta en est un), la borne suit le registre, pas le
  script.

56.4 D-2' : ARBITRE (machine 1, comme assigne)
  Les versions anterieures datees du journal maitre (et de tout
  fichier porteur de la correspondance) entrent TOUTES au bundle --
  coherence directe avec PB-3a : pieces datees distinctes, aucun
  tri. Le pre-vol v2 les liste ("TOUTES au bundle (D-2')") sans en
  exclure aucune ; le manifeste les porte toutes.

56.5 P-2' : LIVREE (pre-vol v2 a correspondance declaree)
  preflight_coupe_bundle_v2.py, empreinte au message de livraison.
  Un numero est repute present si un fichier journal_delta_NN*
  existe OU si sa ligne de CORRESPONDANCE DECLAREE trouve au moins
  un porteur : 1..17 <- /journal_bundle5/ (journal maitre) ;
  18 <- /section_?18/ ; 19-20 <- /journal_delta_19-20/. La table
  est AUTOREE machine 1 depuis le resume de la note P-1' ; elle
  doit etre CERTIFIEE par machine 2 contre 8e4bb337 sect. 3.2
  AVANT usage en coupe -- tout ecart de motif ou de perimetre se
  corrige au script (version c) sur son texte, pas de memoire.
  Banc qui tue, trois scenarios : couverture complete avec porteurs
  multi-versions -> 0 ; porteur du 18 supprime -> 1 ; borne
  au-dela des directs -> 1. Selftest execute a la livraison,
  0 echec. Rejeu BOCAL4 (Git Bash) : retour 0 exige sur le
  repertoire de coupe, a la borne D-1'.

56.6 ETAT
  Restent avant la session de coupe (sequence 4b, ee5da74f) :
  (i) certification machine 2 de la correspondance 56.5 contre
  8e4bb337 sect. 3.2 ; (ii) pre-vol v2 retour 0 sur le repertoire
  de coupe a la borne effective ; (iii) depot de 8e4bb337 (56.1).
  Puis : coupe, contre-epreuve, delta de consignation, mail.
  File inchangee par ailleurs.

=== FIN DU JOURNAL DELTA 56 ===
