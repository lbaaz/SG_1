NOTE MACHINE 2 -- CERTIFICATION DU GEL M16 v9 ET PRE-VOL DU SCRIPT v3
(machine 2, 2026-08-12)
=======================================================================
Pieces auditees, relues du disque a l'instant de la citation (N-48) :
  m16_pre_enregistrement_v9.md   5f73ee25cbb89821   31833 o
  m16_crible_v3.py               53dddab0cbcd3a0a   32370 o
Joint : le present audit est reproductible depuis les artefacts ; les
comptes cites sont imprimes par le banc de mutation machine 2.

VERDICT EN DEUX TEMPS.
  LE GEL v9 EST CERTIFIE SUR SA CLAUSE. Deux hunks, la clause de
  liaison N-56 est exacte et ses deux empreintes de moteur sont
  justes AU BIT. E19 EST RE-ARME SUR 5f73ee25cbb89821 -- le delta 74
  armait la v8, il ne vaut plus. MAIS SON BLOC DE STATUT PORTE TROIS
  CITATIONS FAUSSES, dont une empreinte fantome : rectifiees en
  section 2, selon le precedent E30 (la correction vit dans la piece
  suivante, on ne re-frappe pas une piece citee).
  LE SCRIPT v3 N'EST PAS CERTIFIE. D-23 est LEVEE et la partie
  atteignable est excellente. Mais LE CHEMIN REEL EST DU CODE MORT :
  le mode que le gel v9 rend BLOQUANT n'est pas cable, FondReel n'est
  jamais instanciee, et elle lit un champ qui n'existe pas.
  D-26, D-27 bloquants ; D-28 declaration.

=======================================================================
1. GEL v9 -- LA CLAUSE EST JUSTE
=======================================================================
Diff v8 -> v9 : DEUX hunks, sous-titre et bloc STATUT. Rien d'autre
ne bouge -- verifie sur le diff entier.
La clause N-56 dit exactement ce qu'il fallait : deux couches, le
rebind de P nomme MANIPULATION D'INSTRUMENT avec journalisation et
RESTAURATION VERIFIEE par ligne, la reprise par extraction (regle 12),
et le point fixe P-g -- "la ligne 4|2.62|+1 rejouee DOIT reproduire le
verdict et le s* de l'artefact 96d78407, sinon la liaison n'est pas
verifiable et RIEN ne tourne".
EMPREINTES DE MOTEUR, RE-DERIVEES : sha256 complet de
m9_replication_v1.py annonce c8ed357b120352c4d1078307add3eaac285940
c8bec00acc2ddc9ff386ab2c5c -- IDENTIQUE au bit. sha16 de
m15_site83_v2.py annonce 41ddebcd72b96e64 -- IDENTIQUE (99522 o).
Les deux couches resolvent chez moi. La clause est opposable.

=======================================================================
2. TROIS CITATIONS FAUSSES DANS LE STATUT (rectifiees ici, E30)
=======================================================================
  (a) "La v8 (2a1628005c5b015b, 30933 o)" -- l'empreinte est juste,
      LA TAILLE NON : la v8 fait 30960 octets. Un couple
      (empreinte, taille) dont un membre est faux est une citation
      fausse : c'est le couple qui identifie.
  (b) "delta 74, note 262c8c39" -- CETTE EMPREINTE NE CORRESPOND A
      AUCUNE PIECE. Ma certification de la v8 vaut b8e8a536dd30a386
      (11677 o) ; le delta 74 vaut 2509cc58b14c879e (5697 o). Le
      262c8c39 est un fantome, exactement la famille E30 -- une
      empreinte calculee sur un etat qui n'a jamais ete depose, ou
      transportee sans re-derivation.
  (c) "(D-23, note 262c8c39 sect. 2)" -- la liaison d'instrument est
      D-18, et elle vit en SECTION 4 de ma note. D-23 designe, dans
      la meme note, les branches A2/A4/A6 non atteintes ; la section
      2 traite des six bloquants leves. Numero et section faux tous
      les deux.
RECTIFICATION OPPOSABLE : la v8 fait 30960 o ; la note de
certification de la v8 est b8e8a536dd30a386 ; le delta est
2509cc58b14c879e ; la clause de liaison execute D-18, section 4.
LA v9 N'EST PAS RE-FRAPPEE (PB-1) : la presente note vaut
rectificatif, elle est deposee avec le delta, et toute lecture du
statut de la v9 se fait avec elle. A aligner a la prochaine version
du gel, sans re-certification de la clause.

=======================================================================
3. SCRIPT v3 -- CE QUI EST ACQUIS
=======================================================================
D-23 LEVEE : les sept branches de P-M16a sont atteintes (A0, A1, A2,
  A3, A4, A5, A6), les trois de P-M16b et les quatre de P-M16c. 16
  scenarios, couverture complete -- verifie par execution de mon
  cote, pas lu du log.
Les mutations mordent toujours (H-A/H-B echangees, DOUBLE absorbe
  par H-B) : les controles de D-16 n'ont pas regresse.
La couche manche est chargee APRES verification d'empreinte, et
  l'import est sans effet de bord (garde __main__ presente dans
  m15_site83_v2). Les sept fonctions reprises existent bien :
  derive_pre_run, arret_pre_run, x_du_point, b_sigma, plan_signes,
  criterer, brancher -- ainsi que ATTENDU_K_6DEC.
FondReel est ecrite dans le bon esprit : elle re-derive les K_X par
  m15.derive_pre_run et s'arrete sur ecart (arret_pre_run). Les
  valeurs de reference du factice (27.087844 / 21.714077 / 5.835765)
  sont celles du bloc pre_run de l'artefact M15 -- verifiees.

=======================================================================
4. D-26 (BLOQUANT) -- LE MODE QUE LE GEL REND BLOQUANT N'EXISTE PAS
=======================================================================
L'en-tete du script annonce "--prevol-reel : point fixe 4|2.62|+1
contre l'artefact (P-g)". Dans main() : aucune branche --prevol-reel.
Le paragraphe MODES du MEME docstring, plus bas, liste encore les
trois modes de la v1 (--selftest, --preflight, --run). Invoque, le
mode imprime l'usage et sort.
Or le gel v9 fait de P-g un PREALABLE BLOQUANT, dans ses propres
termes : "sinon la liaison n'est pas verifiable et RIEN ne tourne".
Le seul dispositif que la v3 existait pour apporter n'est pas
executable.
  CORRECTIF : cabler le mode, et qu'il fasse EXACTEMENT ce que le gel
  demande -- charger l'artefact 96d78407, lire le verdict et le s* de
  4|2.62|+1, rejouer la ligne sous la liaison (rebind de m9.P a 4),
  comparer a la tolerance declaree, RESTAURER P et verifier la
  restauration, puis s'arreter en echec si l'un des trois controles
  manque. Aligner le paragraphe MODES.

=======================================================================
5. D-27 (BLOQUANT) -- LE CHEMIN REEL EST DU CODE MORT, ET IL EST FAUX
=======================================================================
  (a) FondReel n'est JAMAIS instanciee : une seule occurrence dans le
      fichier, sa propre ligne de definition de classe.
  (b) L'objet "art" qu'elle attend n'est CONSTRUIT NULLE PART : aucun
      chargeur d'artefacts, aucune affectation. Elle lit art["m15"]
      et art["m12"] en minuscules quand le script indexe ses
      artefacts en "M15", "M12", "M13b".
  (c) Elle lit s4["pas"] dans la CARTE. Ce champ N'EXISTE PAS : les
      entrees de carte portent asym, frag, sF, sM, sP -- et rien
      d'autre. Au run, KeyError.
  OU VIT LE PAS, ET POURQUOI LE CORRECTIF EST DEJA PRESCRIT PAR LA
  CAMPAGNE : le pas final est un champ du BLOC G6, pas de la carte --
  pas_final_recherche, avec ses variantes relatives (pas_relatif_fin,
  pas_relatif_gros, pas_eff_fin_rel, pas_eff_gros_rel). C'est la
  discipline D1-3 que le gel impose deja pour les STATUTS : on lit au
  bloc de garde, jamais a la carte. Elle vaut ici pour la grandeur.
  CORRECTIF : ancres_XB prend sF a la carte et le pas au bloc G6 de
  la MEME ligne, en nommant le champ retenu (pas_final_recherche) et
  en declarant pourquoi celui-la et pas un relatif -- b_sigma attend
  un pas ABSOLU, et l'erreur sur ln s* vaut pas/s* (E26/E27, la
  famille de trois errata nee d'avoir traite ce pas comme relatif).
  Construire "art" avec les memes clefs des deux cotes, et
  instancier FondReel au run ET au pre-vol reel.

=======================================================================
6. D-28 (DECLARATION) -- UN MESSAGE DE REFUS DEVENU FAUX
=======================================================================
--run refuse en disant "l'adaptateur attend les signatures de
chercher_seuil/integrer/garde_G3 (machine 2)". Les signatures ont ete
livrees au delta 74 et la liaison est GELEE depuis la v9. Le verrou
est bon -- le script echoue ferme, c'est le bon comportement -- mais
son motif est perime, et il designe machine 2 comme debitrice de
quelque chose qui est rendu. Reecrire : "--run refuse tant que P-g
n'a pas ete joue et certifie".

=======================================================================
7. CE QUE CE PRE-VOL N'ETABLIT PAS
=======================================================================
- Rien sous moteur reel : le mode n'existe pas. Le --preflight
  n'exerce que le factice ; il ne prouve toujours RIEN sur le
  cablage, et il ne le pourra pas tant que D-26 tient.
- La justesse de b_sigma, de criterer et de brancher : repris de la
  couche manche, non re-verifies ici (heritables, empreinte
  conforme).
- Le comportement du rebind de m9.P : jamais execute.
- La duree du run.
- Aucun numero de delta ni d'erratum n'est attribue ici (E18) ; le
  delta d'accompagnement les prend a l'acte.

EMPREINTES RE-DERIVEES LE 2026-08-12 DEPUIS D:\devs\bocal\BOCAL4,
relues du disque a l'instant de la citation (N-48) :
  5f73ee25 (gel v9), 53dddab0 (script v3), 2a162800 (gel v8, 30960 o),
  91babeac (script v2), b8e8a536 (certification v8), 2509cc58
  (delta 74), c8ed357b (m9, sha complet verifie), 41ddebcd
  (m15_site83_v2), 96d78407 / fa109da9 / 22fa1760 (artefacts ouverts
  pour les champs de carte et de G6).

=== FIN -- GEL v9 CERTIFIE SUR SA CLAUSE ; SCRIPT v3 : CHEMIN REEL DU ===
=== CODE MORT                                                        ===
