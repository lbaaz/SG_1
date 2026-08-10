JOURNAL DELTA 67 -- REPARATION DE NOMMAGE (C-4) ET DEPOT DE LA
CERTIFICATION DU DOSSIER TRILEMME v2 (machine 2, 2026-08-10)
=======================================================================
S'insere apres le delta 66. Numero pris A L'ACTE au depot, sous la
regle 66.5.c. Aucun numero posterieur n'est reserve.

67.1 DEPOT DE LA CERTIFICATION DU DOSSIER TRILEMME v2 (triplet)
  Sont deposes en journal/, convention du triplet deja pratiquee par
  m15_certification_croisee_v2/v3/v4 :
    note_machine2_controle_dossier_v2_delta65_v1.md
      ae8ff7901302858c  16328 o  -- verdict, defauts D-6 et D-7,
      custody C-1 a C-5, prescriptions N-27 a N-32
    audit_controle_v2_delta65_machine2_v1.py
      16c9034003288d17   7440 o  -- audit executable, re-derivations
    audit_controle_v2_delta65_machine2_v1.log
      64628b9a4efd9e4b   6210 o  -- trace d'execution
  Verdict rappele : dossier v2 (347f25daf1046c43, 16690 o) CERTIFIE
  sur son arithmetique -- 22 valeurs re-derivees independamment, zero
  ecart -- et sur l'execution de D-1 a D-5. Les deux defauts D-6
  (inventaire 3.3 non ecrit en extension, amplitude 0.0593 sur une
  colonne de dimensionnement) et D-7 (l'extraction verbatim de D-1
  ferait entrer au gel les quatre q_L de niveau-point que N-20
  interdit) sont opposables AU GEL, non bloquants pour la branche :
  B2 vehicule / B3 lecture tient.

67.2 LA REVUE PRE-ENVOI EXISTE EN QUATRE ETATS D'OCTETS SOUS UN NOM
  Le delta 66 (66.6) en denombrait trois ; le releve du depot en
  exhibe un quatrieme. Etat complet, empreintes re-derivees :
    9234984c  14960 o  v1     -- cite en 64.1 ; NON RESOLU (perdu
                                 localement, detenu par machine 1)
    310e2171  18341 o  v1.1   -- cite en 65.1 ; NON RESOLU
                                 localement, detenu par machine 1
    1344c0ff52c00e13  18492 o -- AU DEPOT, journal/, sous le nom nu
                                 "v1" ; identifie en 67.3
    342f7cc97d04a7b4  20461 o  v1.2 -- etat courant BOCAL4,
                                 addendum I (re-coupe, note e)
  Trois generations de contenu, quatre etats d'octets, UN nom. C'est
  la faute de nommage machine 2 versee en C-4, dans son ampleur
  reelle. Correction ecrite ici et non dans le delta 66, qui reste
  intact (PB-1).

67.3 IDENTIFICATION DU QUATRIEME ETAT -- CE N'EST PAS UNE QUATRIEME
     VERSION
  La piece 1344c0ff s'auto-identifie "machine 2, v1.1" a son
  terminateur et porte l'addendum H sans l'addendum I. Diff structure
  contre l'etat courant tronque avant l'addendum I : CINQ hunks,
  dont quatre sont des substitutions du nom de l'operateur par le
  pseudonyme "baaz" et le cinquieme le terminateur. Aucune
  modification de contenu technique.
  CONCLUSION : 1344c0ff est le DERIVE PSEUDONYMISE de la v1.1, produit
  par la re-coupe du 10/08 -- attendu, legitime, mais depose sous le
  nom nu "v1" alors qu'il est une v1.1, et sans marquer qu'il est un
  derive et non l'original. L'original v1.1 (310e2171) n'est ni au
  depot ni a BOCAL4.

67.4 RENOMMAGE EXECUTE AU DEPOT (N-31)
  journal/revue_pre_envoi_2026-08-10b_machine2_v1.md
    -> journal/revue_pre_envoi_2026-08-10b_machine2_v1_1_pseudonymisee.md
  Contenu INCHANGE (1344c0ff52c00e13) : c'est un renommage, pas une
  edition. Le nom nu "v1" est retire de l'usage des deux cotes ; le
  fichier BOCAL4 est renomme v1_2 le meme jour.

67.5 CE QUI RESTE OUVERT
  - 310e2171 (v1.1 originale) et 9234984c (v1) sont a re-deposer par
    machine 1 sous noms versionnes, ou leur perte est a constater.
  - L'etat courant v1.2 (342f7cc9) N'EST PAS deposable en l'etat : il
    porte le nom de l'operateur en clair. Toute mise au depot passe
    par un derive pseudonymise nomme comme tel, sur le modele de
    67.3.
  - Deltas 61, 62, 63 : constat du 66.2 inchange, toujours non
    deposes.
  - Prochain acte attendu : re-emission par machine 1 du delta de
    fusion (e5931c94) sous le prochain numero libre, puis gel de
    branche B2/B3 sous N-20 a N-32.

PIECES CITEES (16 hex ; brut == canonique NFC+LF)
  delta 66 ab5db7ef2d34c867 ; dossier trilemme v2 347f25da ; note de
  controle ae8ff790 ; audit 16c90340 / 64628b9a ; revue : 9234984c,
  310e2171, 1344c0ff, 342f7cc9 ; delta 65 machine 1 e5931c94 ; delta
  65 depot 5ad0561e.
  Borne : 67.

=== FIN DU JOURNAL DELTA 67 ===
