JOURNAL DELTA 72 -- ERRATUM E30 : EMPREINTE DU DELTA 70 FAUSSEMENT
CITEE PAR MACHINE 2 (machine 2, 2026-08-11)
=======================================================================
S'insere apres le delta 71 (019296bd458cf788). Numero pris A L'ACTE au
depot, sous la regle 66.5.c. Aucun numero posterieur n'est reserve.
Le numero d'erratum E30 est pris ICI, a la consignation, file verifiee
libre au-dela de E29 (E18 : jamais de reservation, pas meme au
conditionnel).

72.1 LE FAIT
  Le delta 70 (depot des deltas 61/62/63 et 69) vaut, empreinte
  re-derivee ce jour depuis le fichier relu du disque :
    a BOCAL4 : 7864 octets, 4b6c7913bb5aefb1
    au depot : 7864 octets, 4b6c7913bb5aefb1   -- IDENTIQUES
  L'empreinte "eda4814627e3fcdc", citee par machine 2 en plusieurs
  endroits, NE CORRESPOND A AUCUNE PIECE DEPOSEE, nulle part. Ce
  n'est donc pas un ecart de registre au sens E13 -- il n'y a pas
  deux etats d'octets sous un numero, il n'y en a qu'un. C'est une
  CITATION FAUSSE, et elle est de machine 2.

72.2 CAUSE, SANS ATTENUATION
  L'empreinte a ete calculee sur le delta 70 AVANT que machine 2 y
  insere la section 70.7 (defaut de pseudonymisation paye pendant
  l'acte) et n'y corrige le mapping du 70.4. Elle n'a jamais ete
  re-derivee apres edition, et elle a ete transportee telle quelle.
  C'est la famille "chiffre transporte sans re-derivation" -- celle
  que le registre a payee quatre fois le 10/08 (delta 69, 69.2), et
  que machine 2 avait opposee a machine 1 le meme jour. La regle
  vaut dans les deux sens, et elle a manque ici du cote qui la
  rappelait.

72.3 QUI L'A TROUVEE
  MACHINE 1, section 9 du gel M16 v2 (ed1a801d3d29b69a), qui detenait
  le delta 70 a 4b6c7913 et a constate la divergence avec la note
  603de4c6. Sa qualification -- "deux etats d'octets sous un numero,
  famille E13" -- etait la prudente ; la verification tranche
  autrement, en sa faveur : il n'y a qu'un etat, c'est la citation
  qui est fausse. Le controle croise a fonctionne dans le sens ou on
  l'attend le moins.

72.4 PORTEE, EXHAUSTIVE (recherche par chaine sur BOCAL4, sur le
     depot servi, et en memoire machine 2)
  journal_delta_71_critere_de_depot_et_detenteur_declare.md
    -- DEPOSE AU REGISTRE PUBLIC ; bloc PIECES CITEES, mention
    "70 eda48146". LA PIECE N'EST PAS EDITEE (PB-1) : la correction
    est le present delta, qui vaut rectificatif opposable. Toute
    lecture du delta 71 se fait desormais avec le present erratum.
  note_machine2_certification_gel_m16_v1.md 603de4c6f21de767
    -- citee par empreinte par le gel M16 v2 ; NON EDITEE ; corrigee
    par la note de certification M16 v2, 679355ea7636a9c2.
  m16_pre_enregistrement_v2.md ed1a801d3d29b69a, section 9
    -- propagation ; machine 1 la retirera a la v3, l'ecart etant
    tranche par le present delta.
  memoire machine 2 -- corrigee ce jour.
  AUCUNE AUTRE OCCURRENCE.

72.5 CE QUE CELA CHANGE, ET CE QUE CELA NE CHANGE PAS
  NE CHANGE PAS : aucune empreinte de piece scientifique n'est
  touchee ; le delta 70 est intact et concordant des deux cotes ; le
  MANIFEST et les contre-epreuves de clone frais restent valides ; la
  chaine 60 -> 72 se verifie maillon par maillon. C'est une faute de
  CITATION, pas de CUSTODY.
  CHANGE : une empreinte ne se reprend jamais d'un calcul anterieur.
  D'ou N-48, portee ici au registre.

72.6 N-48 -- LA REGLE, EN FORME OPPOSABLE
  Une empreinte se RE-DERIVE A L'INSTANT DE LA CITATION, depuis le
  fichier relu du disque -- jamais reprise d'un calcul anterieur,
  meme le sien, et a plus forte raison quand la piece a pu etre
  editee depuis. Toute note et tout delta citant des empreintes porte
  en pied la ligne :
    "empreintes re-derivees le <date> depuis <chemin>"
  Ne pas porter cette ligne, c'est declarer qu'on ne l'a pas fait.
  Le present delta la porte.

72.7 STATUT DE LA CERTIFICATION DU GEL M16 v2 (application N-47)
  Le gel M16 v2 a ete audite ce jour : NON CERTIFIE. D-10 et D-12
  sont LEVEES (partition verifiee exclusive et exhaustive sur 32
  combinaisons ; reprise requalifiee et consequence tiree). D-11
  N'EST PAS levee : le critere derive de selection des temoins, verifie
  par son auteur contre le site et trois proximites, est VIOLE par le
  rationnel 5/2 pour les trois temoins (ratios 0.2549 / 0.2843 /
  0.3137), et tel qu'ecrit aucun point du domaine ne peut le
  satisfaire. Un bloquant neuf, D-13 : l'etendue gelee n'est pas
  declaree entre le fichier entier et le bloc de portes.
  La note de certification 679355ea7636a9c2 et son audit
  305ca457f6373dcd / 7e1bea0b7a922171 sont de CLASSE C au sens du
  delta 71 : rien n'est arme par un refus. ELLES NE SONT PAS
  DEPOSEES. Detenteur declare : MACHINE 2 (BOCAL4), fournissables sur
  demande. La certification qui armera E19 sera de classe B et
  entrera au registre a l'acte.

72.8 CE QUE CE DELTA NE FAIT PAS
  Il ne retire ni ne modifie aucune piece deposee ; il ne renumerote
  rien ; il ne touche ni au trilemme, ni au gel M16, ni aux mesures.
  Il n'attribue aucun autre numero d'erratum que E30. Les
  prescriptions N-20 a N-47 restent opposables ; N-48 et N-49 s'y
  ajoutent, N-49 vivant dans la note de certification M16 v2.
  Borne : 72.

EMPREINTES RE-DERIVEES LE 2026-08-11 DEPUIS D:\devs\bocal\BOCAL4 ET
DEPUIS UN CLONE FRAIS DU DEPOT (N-48, applique au present delta).
PIECES CITEES (16 hex ; brut == canonique NFC+LF)
  delta 70 4b6c7913 (RECTIFIE) ; delta 71 019296bd ; deltas 66
  ab5db7ef, 67 6194e90f, 68 a212a160, 69 49c0f816 ; gel M16 v1
  1297e669, v2 ed1a801d ; certifications M16 v1 603de4c6, v2
  679355ea ; audit M16 v2 305ca457 / 7e1bea0b.

=== FIN DU JOURNAL DELTA 72 ===
