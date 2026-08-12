JOURNAL DELTA 75 -- GEL M16 v9 CERTIFIE SUR SA CLAUSE (E19 RE-ARME),
TROIS CITATIONS RECTIFIEES, SCRIPT v3 : LE CHEMIN REEL EST DU CODE MORT
(machine 2, 2026-08-12)
=======================================================================
S'insere apres le delta 74 (2509cc58b14c879e). Numero pris A L'ACTE au
depot, sous la regle 66.5.c. Acte de CLASSE B (delta 71).

75.1 GEL v9 CERTIFIE SUR SA CLAUSE -- E19 RE-ARME
  m16_pre_enregistrement_v9.md   5f73ee25cbb89821   31833 o
  Certification deposee avec le present delta :
  note_machine2_certification_gel_v9_et_prevol_script_v3.md
    e964a927bd37d2cb   9440 o
  Diff v8 -> v9 : DEUX hunks (sous-titre, bloc STATUT). La clause de
  liaison N-56 est exacte : deux couches, rebind de P nomme
  MANIPULATION D'INSTRUMENT avec journalisation et RESTAURATION
  VERIFIEE par ligne, reprise par extraction (regle 12), et le point
  fixe P-g -- 4|2.62|+1 doit reproduire le verdict et le s* de
  l'artefact 96d78407, "sinon RIEN ne tourne".
  Les deux empreintes de moteur sont JUSTES AU BIT : m9 (sha256
  complet c8ed357b1203...2c5c) et m15_site83_v2 (41ddebcd72b96e64,
  99522 o). Les deux couches resolvent chez machine 2.
  E19 EST RE-ARME SUR 5f73ee25cbb89821 ET SUR ELLE SEULE. Le delta 74
  armait la v8 : il ne vaut plus.

75.2 TROIS CITATIONS FAUSSES DANS LE STATUT DE LA v9, RECTIFIEES
  Le precedent est E30 (delta 72) : on ne re-frappe pas une piece,
  la correction vit dans la suivante. Rectifications opposables :
    la v8 fait 30960 octets, non 30933 -- l'empreinte est juste, la
      taille non ; le couple (empreinte, taille) identifie, un
      membre faux le rend faux ;
    "note 262c8c39" NE CORRESPOND A AUCUNE PIECE : la certification
      de la v8 est b8e8a536dd30a386 (11677 o), le delta est
      2509cc58b14c879e (5697 o). Fantome, famille E30 ;
    la clause de liaison execute D-18, SECTION 4 de la note -- non
      "D-23, sect. 2" : D-23 designe les branches A2/A4/A6 et la
      section 2 traite des six bloquants leves.
  La clause elle-meme n'est pas touchee : la certification porte.
  A aligner a la prochaine version du gel, sans re-certification.

75.3 SCRIPT v3 -- D-23 LEVEE, MAIS LE CHEMIN REEL N'EXISTE PAS
  m16_crible_v3.py   53dddab0cbcd3a0a   32370 o
  ACQUIS, verifie par execution machine 2 et non lu du log : les SEPT
  branches de P-M16a sont atteintes (A0 a A6), les trois de P-M16b,
  les quatre de P-M16c -- 16 scenarios, couverture complete ; les
  mutations mordent toujours ; la couche manche est chargee APRES
  verification d'empreinte, sans effet de bord ; les sept fonctions
  reprises existent ; FondReel re-derive les K_X par derive_pre_run
  et s'arrete sur ecart.
  D-26 BLOQUANT : le mode --prevol-reel est ANNONCE a l'en-tete et
  ABSENT de main() ; le paragraphe MODES du meme docstring liste
  encore les trois modes de la v1. Or le gel v9 fait de P-g un
  prealable bloquant dans ses propres termes. Le seul dispositif que
  la v3 existait pour apporter n'est pas executable.
  D-27 BLOQUANT : le chemin reel est du CODE MORT et il est FAUX --
  FondReel n'est jamais instanciee ; l'objet "art" qu'elle attend
  n'est construit nulle part et elle l'indexe en minuscules quand le
  script indexe en majuscules ; elle lit s4["pas"] dans la CARTE, ou
  ce champ N'EXISTE PAS (asym, frag, sF, sM, sP -- et rien d'autre).
  OU VIT LE PAS : c'est un champ du BLOC G6 -- pas_final_recherche --
  et le lire la plutot qu'a la carte est la discipline D1-3 que le
  gel impose deja pour les statuts. b_sigma attend un pas ABSOLU :
  l'erreur sur ln s* vaut pas/s*, famille des trois errata E26/E27
  nes d'avoir traite ce pas comme relatif.
  D-28 : le message de refus de --run est perime -- il reclame a
  machine 2 des signatures livrees au delta 74 et desormais gelees.
  Le verrou est bon, son motif est faux.

75.4 CE QUE CE DELTA NE FAIT PAS
  Aucune mesure. Le script n'est pas certifie, aucun run ne peut
  avoir lieu, et RIEN n'est etabli sous moteur reel -- le mode qui
  l'etablirait n'existe pas. Restent dus : cablage de --prevol-reel ;
  chemin reel vivant (art construit, FondReel instanciee, pas lu au
  bloc G6) ; message de refus corrige ; puis P-g JOUE, puis
  certification du script sous E19 contre la v9, puis le run.
  Borne : 75.

EMPREINTES RE-DERIVEES LE 2026-08-12, relues du disque a l'instant de
la citation (N-48), depuis D:\devs\bocal\BOCAL4 et depuis un clone
frais du depot pour les deltas.
PIECES CITEES (16 hex ; brut == canonique NFC+LF)
  gel v9 5f73ee25 (certifie) ; gel v8 2a162800 (30960 o) ; script v3
  53dddab0 ; script v2 91babeac ; certification v8 b8e8a536 ; moteur
  m9 c8ed357b ; couche manche m15_site83_v2 41ddebcd ; artefacts
  96d78407, fa109da9, 22fa1760 ; deltas 73 2706c39a, 74 2509cc58.

=== FIN DU JOURNAL DELTA 75 ===
