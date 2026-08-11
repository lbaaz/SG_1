JOURNAL DELTA 73 -- GEL M16 CERTIFIE, E19 ARME, P-d SCELLEE
(machine 2, 2026-08-11)
=======================================================================
S'insere apres le delta 72 (d3907be9a882d51b). Numero pris A L'ACTE au
depot, sous la regle 66.5.c. Aucun numero posterieur n'est reserve.
Acte de CLASSE B (delta 71) : la piece deposee ci-dessous ARME une
regle, elle entre donc au registre a l'acte.

73.1 CE QUI EST CERTIFIE, ET CE QUE CELA AUTORISE
  m16_pre_enregistrement_v7.md   10dd099055adc3cb   30472 o
  note_derivation_P1_signes_E_v9.md  d91a08bf5d093e1b  4350 o
  Certification machine 2, DEPOSEE avec le present delta :
  note_machine2_certification_gel_m16_v7_et_P1v9_avec_Pd.md
    1c984db102bb610f   10227 o
  E19 EST ARME. Le script de la manche M16 peut etre ecrit contre
  l'empreinte 10dd099055adc3cb, ET AUCUNE AUTRE. Toute modification
  du gel, meme en mieux, en fait une version neuve a certifier avant
  tout code (regle E19, inchangee).
  L'audit executable (audit_gel_m16_v7_machine2_v1.py / .log,
  b802ef75a47dec7a / f79ce1435cc90a99) est de CLASSE C : il reste a
  BOCAL4, detenteur MACHINE 2, fournissable sur demande. La note est
  autosuffisante -- elle porte tous les nombres et tous les comptes.

73.2 LA LIGNEE, ET CE QU'IL A FALLU
  Sept versions de gel, cinq de note P1, cinq certifications :
    v1 1297e669 (603de4c6) : ni portes ni partition de verdicts ;
      critere de temoin pose sur le fil ; reprise deterministe.
    v2 ed1a801d (679355ea) : D-10 et D-12 levees ; le critere derive
      qui remplace le seuil nu est INSATISFIABLE -- viole par 5/2
      pour les trois temoins, aucun point du domaine ne le passe.
    v3 b7daaeff (448aacb2) : CERTIFIEE sans defaut ; P-f rendu par
      machine 2 (G3/G5 par renvoi au gel M12, G9 non heritee).
    v4 1f1ad63c (08381dd5) : integration des seuils ; la porte de
      H-B conditionnee a un fait d'instrument -- H-B indeclarable,
      H-A par defaut dans 77 % des mondes H-B.
    v5 5cea3f1f (ade84cf7) : D-14 levee, mais la partition se
      recouvre -- DEFAUT DE MACHINE 2, dont le correctif posait
      DOUBLE-SIGNAL comme sous-ensemble de H-B (N-53).
    v6 e68fd700 et P1 v8 b4687012 : intermediaires, non deposees,
      DECLAREES avec detenteur machine 1 (N-47).
    v7 10dd0990 : forme 2x2, 64/64 par enumeration des deux cotes.
  DEUX FAUTES VERSEES DANS CE CYCLE, une par machine : forme
  recouvrante proposee par machine 2 (N-53) ; signature "disjonction
  par construction" sans enumeration par machine 1 (sa propre regle,
  v9 sect. 14 : aucun bloc de portes ne quitte machine 1 sans son
  enumeration collee dans la piece).

73.3 CE QUE LE GEL PORTE, EN UNE LISTE OPPOSABLE
  Etendue gelee = fichier entier, ancres stables (N-45, D-13) ;
  inventaire extrait, statuts re-derives au bloc G6 (N-33) ;
  politique d'ancres symetrique, fourchette consignee (N-35) ;
  unites de compte declarees et etiquetees a chaque citation
  (N-34, N-44) ; critere de temoin a deux volets sur catalogue
  ENUMERE (D-11) ; reprise requalifiee en mesure sous instrument
  declare different (D-12) ; partitions verifiees 32/32 et 64/64
  (D-10, D-15) ; les trois nombres d'E27, dont la lisibilite de (i)
  ecrite EN CLAIR a 1 chance sur 22 (N-41) ; puissance de chaque
  porte sous chaque hypothese (N-40, N-52) ; G3/G5 par renvoi,
  G9 non heritee (N-50) ; pieds de re-derivation exacts (N-48,
  N-51). Programme : 31 lignes hors strate 2, six points neufs
  certifies nouveaux contre le registre entier.

73.4 P-d SCELLEE -- LE FAIT DE REGISTRE
  L'attente machine 2 est INSCRITE dans la note deposee, section 4,
  AVANT toute mesure, et ne sera jamais reecrite (precedent M12/M15).
  Son contenu vit dans la note ; le present delta en consigne
  l'existence, la date et l'empreinte porteuse, plus le seul point
  qui interesse le registre : LES DEUX ATTENTES DIVERGENT.
  Le gel donne P(plancher de (i)) = 0.0462 sous Bernoulli
  independant a la borne declaree ; machine 2 donne 0.25, sous une
  lecture ou la mortalite p=4 de la fenetre occupe un ANNEAU en
  distance au site et non un coeur. UN FACTEUR CINQ. La manche
  tranchera, et l'enjeu depasse la manche : si le plancher tombe la
  ou le gel l'annonce a 1 sur 22, c'est l'echangeabilite -- donc
  l'outil q_L lui-meme -- qui cesse de valoir sur cette fenetre.
  Machine 2 declare son motif POST-HOC et sans valeur de preuve ;
  il ne vaut que d'etre scelle avant. Aucune branche du gel ne s'y
  adosse, aucun seuil n'en depend.

73.5 CE QUE CE DELTA NE FAIT PAS
  Il ne certifie aucun script -- il n'y en a pas. Restent dus, dans
  l'ordre : ecriture du script par machine 1 (cahier sect. 7 du
  gel) ; certification du script sous E19 contre 10dd0990 ; PRE-VOL
  opposable machine 2 avec moteur factice ; puis le run. Le banc
  positif (68df6576) se rejoue a la certification du script. Aucune
  mesure ici, aucun numero d'erratum (E18).
  Borne : 73.

EMPREINTES RE-DERIVEES LE 2026-08-11, relues du disque a l'instant de
la citation (N-48), depuis D:\devs\bocal\BOCAL4 et depuis un clone
frais du depot pour les deltas.
PIECES CITEES (16 hex ; brut == canonique NFC+LF)
  gel M16 v7 10dd0990 (certifie) ; P1 v9 d91a08bf ; certification
  1c984db1 (deposee ci-jointe) ; audit b802ef75 / f79ce143
  (classe C, machine 2) ; lignee gel v1 1297e669, v2 ed1a801d,
  v3 b7daaeff, v4 1f1ad63c, v5 5cea3f1f, v6 e68fd700 (machine 1) ;
  lignee P1 v5 5704987e, v6 96081e47, v7 2a870f31, v8 b4687012
  (machine 1) ; certifications 603de4c6, 679355ea, 448aacb2,
  08381dd5, ade84cf7 ; gel M15 v4 35022c5c ; gel M12 v4 bf9866a7 ;
  deltas 66 ab5db7ef, 67 6194e90f, 68 a212a160, 70 4b6c7913,
  71 019296bd, 72 d3907be9.

=== FIN DU JOURNAL DELTA 73 ===
