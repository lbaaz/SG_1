# NOTE DE DERIVATION ET DE DEPOT -- DELTA 87 (SEQUENCE R3) -- machine 2, v1
# Classe 1. 08/09/2026. Etablie au moment du depot, par la machine qui depose.
# Objet : documenter la seule transformation subie par l'acte entre sa certification et son entree
# au registre, et rendre l'etat du registre verifie a cet instant -- ce que la certification
# elle-meme declarait NON VERIFIABLE par machine 2 (sa reserve R-2).

=======================================================================
1. LA DERIVATION : UNE SEULE SUBSTITUTION, MECANIQUE ET REPRODUCTIBLE
=======================================================================
  Source     journal_delta_nn_sequence_R3_v1.md   cce710187ad53e04   6954 octets
             (acte a la plume de machine 1, CERTIFIE par machine 2 : certification
             CERTIFICATION_machine2_acte_nn_R3_v1.md et son addendum v2, 13 controles sur 13,
             30 empreintes citees sur 30 verifiees)
  Regle      \bnn\b  ->  87        (jeton isole uniquement ; expression reguliere, pas une relecture)
  Derive     journal_delta_87_sequence_R3_v1.md   1a21b0a2d3b842b5   6954 octets

  NEUF occurrences substituees, lignes 1, 3, 7, 14, 31, 41, 52, 65, 74 : le titre, la mention
  "Numero : pris AU DEPOT (E18)", et les sept en-tetes de section nn.1 a nn.7.
  GARDES PASSEES, toutes verifiees par le script joint (deriver_delta87_machine2_v1.py) :
    - les quatre mots qui CONTIENNENT 'nn' sans etre le jeton -- donnees, personne, annonce,
      inconnue -- sont intacts, avant comme apres ;
    - nombre de lignes inchange (79) ; exactement 9 lignes modifiees ;
    - chaque ligne modifiee est exactement sa source substituee, caractere par caractere ;
    - longueur inchangee (6954 octets : "nn" et "87" font deux caracteres) ;
    - zero caractere non ASCII, zero signe pour cent apres derivation.
  Le script refuse de tourner si la source ne rend pas cce710187ad53e04 : on ne derive que la piece
  certifiee, jamais une autre.
  MEME GESTE QU'AU DELTA 86, ou le fichier depose bdd0a7333ca5de18 etait derive de cb3536abfd52c1d6.
  Les DEUX versions entrent au registre, la source et le derive : le lecteur peut refaire la
  substitution et retomber sur l'empreinte deposee.

=======================================================================
2. L'ETAT DU REGISTRE, VERIFIE AU MOMENT DU DEPOT
=======================================================================
  Ma certification portait la reserve R-2 : machine 2 n'avait pas acces au depot public et ne
  pouvait verifier ni le HEAD, ni l'absence de depot intermediaire, ni que le numero etait libre.
  L'operateur ayant delegue le depot, ces trois points sont maintenant verifies, sur CLONE FRAIS
  (git clone de https://github.com/lbaaz/SG_1.git, fait pour ce depot) :
    HEAD                    0ff330b0c5aedf4bcf96ce9ca0411a83984745a8 -- "delta 86", 02/09/2026.
    Conforme a ce que l'acte declarait (0ff330b) : aucun depot n'est intervenu depuis le 07/09.
    Numero 87              LIBRE : aucun fichier du registre ne porte delta_87 ni "delta 87".
    Le numero est donc PRIS A L'ACTE au depot, conformement a E18 et a N-68.
  R-2 EST LEVEE. Les trois autres reserves de la certification (R-3 affirmation historique hors
  perimetre de mesure, R-4 residus ouverts, R-5 clause de portee) TIENNENT et sont portees telles
  quelles : elles ne portent sur aucun verdict.

=======================================================================
3. CE QUI ENTRE AU REGISTRE ET CE QUI N'Y ENTRE PAS
=======================================================================
  Depose dans journal/ :
    journal_delta_87_sequence_R3_v1.md          1a21b0a2d3b842b5   l'acte, numerote
    journal_delta_nn_sequence_R3_v1.md          cce710187ad53e04   la source certifiee
    CERTIFICATION_machine2_acte_nn_R3_v1.md                        la certification
    ADDENDUM_CERTIFICATION_machine2_acte_nn_v2.md                  la levee de sa reserve R-1
    NOTE_DERIVATION_delta87_machine2_v1.md                         la presente note
  N'ENTRE PAS, et c'est un choix a l'appreciation de l'operateur, non une omission :
    le lot de mesure machine 2 R3 v1 (canon 7d905230a792ab30) et les autres lots de la sequence,
    qui sont des ZIP. Le delta 86 avait verse son binaire dans runs/. Ici l'acte les cite par
    empreinte ; le versement des donnees est un geste separe, a decider.
  AUCUN NUMERO DE SERIE (N, E, D) n'est pris par ce depot : l'acte n'en prend aucun, et cette note
  n'en prend aucun.

=======================================================================
4. QUI A FAIT QUOI
=======================================================================
  L'acte est a la plume de MACHINE 1. La certification, l'addendum, la derivation et le present
  depot sont de MACHINE 2, sur delegation expresse de l'operateur -- le manifeste du delta 86
  rappelait que "le depot, le numero et les series sont de la main de l'operateur", et c'est lui
  qui a demande que ce depot soit fait.
  Ce depot ne decide RIEN d'autre : ni la promotion 49.5 de P-A-1 et P-D-1 (O4, decision
  operateur, que l'acte propose sans la prendre), ni le depot P-4 (R1, qui est un autre acte).
-- FIN DE LA NOTE --
