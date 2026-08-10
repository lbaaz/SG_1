DELTA 45 -- LE RUN DU PILOTE M12 : L'ARRET EXECUTE, DEUX ACQUIS, ET LE GEL v4
-- version v3
(01/08/2026 ; consigne par machine 1 ; ASCII, NFC+LF)

HISTORIQUE DU DELTA
  v1 fb13077a : premiere consignation, avant certification du gel v4.
  v2 c55d9ee0 : corrections 5a/5b de la certification du gel v4 (f10ffcf3)
      integrees ; ecart declare consigne ; pre-declaration de la paire G8.
  Note machine 2 sur le delta 45 v2 (ad8dd209, 01/08) : les deux corrections
      jugees FIDELES ; la paire G8 CONTRESIGNEE sur son seul critere qui
      compte (mecanique, aveugle, anterieure au code) ; le motif (ii) de la
      v2 FALSIFIE par la donnee ; le motif (i) requalifie (tient sous une
      lecture qui se deduit) ; deux consignations nouvelles exigees au
      script.
  v3. Remplace le motif (ii) par le motif de POSITION propose par machine 2
      et adopte verbatim ; consigne la falsification et sa donnee ;
      requalifie le motif (i) avec l'obligation d'enumeration de G2 ;
      consigne "G8b est UN controle, pas deux" et l'attente pre-declaree
      (moitie grossiere VIDE a p=4). Rien d'autre ne change.

45.1 LE RUN, ET LE PREMIER ARRET DE REGLE DE LA CAMPAGNE
---------------------------------------------------------
  Chaine complete : gel PILOTE v3 03e29c86 certifie (fc61a25c) ; script
  m12_pilote_v3.py 663b17e2 certifie (774f7de4) apres deux tours de
  corrections (S2-S7) ; pre-vol OPPOSABLE joue par machine 2 sur sources
  reelles ; run sur BOCAL4 ; JSON ed0e27b1 ; message de run et
  reconciliation independante 05147405 -- tout y est recalcule du brut.
  TOUTES LES GARDES PASSENT : G1 24/0/0 (derive), G3 <= 4.7e-16, G4 0.000 %
  (hors q_L), G5 pas finaux 6.03e-07 et 1.82e-06, G8a ecart 0.0 EXACT aux
  quatre points de p=4, G8b zero deviation, G9 sans defaut, invariants
  25 + 0 = 25 et 24 + 0 = 24.
  ISSUE : UNE ligne perdue sur douze -- 7|1.70|-1, G6. q_L(80 %) =
  0.2296169327 (contre-verifie machine 1 au dernier chiffre), s_pt =
  0.4572147008, N = 13 > 12 : ARRET, gel v4. La regle, ecrite avant la
  mesure et certifiee trois fois, s'est executee du premier coup sans une
  ligne de discussion -- machine 2 a refuse d'avance tout amenagement de
  D-N motive par ce resultat, et machine 1 contresigne.
  Le delta 44.7 s'est realise integralement : l'attente G6 du pilote
  ("0 ou 1 ligne") est TENUE, et la manche s'arrete quand meme -- les deux
  a la fois, comme consigne AVANT le run.

45.2 ACQUIS (1) : CALIBRATION 24/24 AU BIT, ET UNE ATTENTE FALSIFIEE
---------------------------------------------------------------------
  Les 24 lignes du pilote sont BIT-IDENTIQUES aux valeurs certifiees de M10
  et M11 -- ecart maximal 0.00e+00. C'est le controle de non-derive le plus
  severe de la campagne : le moteur c8ed357b reproduit s* au bit sur une
  autre machine, dans un autre script, six jours plus tard.
  L'ATTENTE G1 DU GEL PILOTE EST FALSIFIEE, dans le bon sens : elle
  annoncait "des ecarts de 0.2 a 2 % -- pas mieux : la geometrie de
  balayage a change". Son MOTIF etait errone -- la geometrie de balayage ne
  touche pas la recherche ; le bracket mesure s* d'abord, le balayage est
  un diagnostic posterieur, et le gel v3 l'ecrivait lui-meme en tete de sa
  section GEOMETRIE. L'attente supposait un couplage qui n'existe pas.
  Elle reste TELLE QUELLE (une attente ne se reecrit pas) ; le registre
  porte que son motif etait faux. Consequence utile : l'exigence de G1'
  ("== 0 exactement" au rejeu) est etablie comme REALISTE, pas seulement
  severe.

45.3 ACQUIS (2) : LE DIAGNOSTIC D'E27 EST RENDU, MECANISME NOMME
-----------------------------------------------------------------
  La question du gel -- "la geometrie neuve declenche-t-elle G6 la ou
  l'ancienne ne declenchait pas ?" -- recoit OUI, sur une bascule unique :
  7|1.70|-1, "ok" sous M10, EXCLUE sous le pilote. Mecanisme : la geometrie
  neuve REGARDE SOUS s* ([LO0, 0.90 s*] en 165 points) la ou l'ancienne
  consignait a partir de s* -- le JSON de M10 ne porte aucun champ de
  fenetre grossiere.
  LE POINT QUI EXCLUT : le point explosif est le DERNIER des 165 points de
  la fenetre grossiere, tous sous le seuil 0.98 s* ; les 164 autres sont
  PROPRES. Sous 0.90 s*, au pas de 0.005 s*, RIEN n'explose : le mouchetage
  commence a 0.90 s* et non ailleurs. L'exclusion est un fait de la LIGNE,
  pas de la decoupe de l'instrument. (La coincidence exacte 0.5298467113 =
  0.900000 s* est celle du point de grille partage par les deux fenetres.)
  L'exclusion est a 3.6e14 epsilons du bord 0.98 : les temoins S4/S6
  l'etablissent SUR DONNEE -- zero ligne ou l'indice 40 compte sous le
  seuil, zero explosif a cet indice, sur 24 balayages.
  ILOTS, chacun avec SON domaine, SANS mise en regard (les gels declarent
  ces comptes non comparables, meme statut que les taux d'attrition ; la
  discipline d'E27 n'est pas de comparer avec une reserve, c'est de ne pas
  comparer -- cert. gel v4, 5b) :
      pilote, fenetre fine entiere [0.90, 1.05] s*        : ilots = 8
      pilote, domaine DECLARE [s*, 1.05 s*] (S5b)         : ilots_au_dessus = 4
      M10, domaine "[s*, 1.05 s*] inter [s*, 1.3 s*]"     : ilots = 3
  Autres faits d'instrument, SANS AUCUNE LECTURE PHYSIQUE (le pilote ne
  teste rien, ne forme aucun E) : retombee a 1.002 s*, sous le pas de M10
  (~0.005 s*) ; et la pathologie siege sur le signe NON fragile de la ligne
  (frag = +1, l'exclusion est en -1) -- le mecanisme d'exclusion n'est pas
  attache a la fragilite. La perte est tombee mot pour mot ou le gel
  declarait son hypothese la plus faible : bord gauche, degre le plus
  eleve, plus petit s* des douze lignes.
  La boucle corrective d'E27 est CLOSE pour cette manche : le diagnostic
  exige est rendu, chiffre, et consigne dans la donnee elle-meme.

45.4 LA DECISION v4 : OPTION A SEULE, ET SES DERIVATIONS
---------------------------------------------------------
  Espace examine, chiffre avant decision : (A) etendre la LISTE 12 -> 16,
  memes regles, meme grille -- N = 13 executable, 75 recherches, AUCUNE
  mesure nouvelle, AUCUNE relecture de donnee ; (B) etendre le pilote aux
  trois derniers points fit-survivants (2.30, 2.60, 2.85), 18 recherches,
  issues N = 9 a 14 selon les pertes neuves -- au prix de BRULER les trois
  derniers points mesures non brules, et d'un run de plus avant M12 ;
  (A+B) les deux branches. DECISION (Baaz) : A SEULE. Motifs : le q_L
  opposable entre tel quel dans D-N, la v4 se certifie sur derivation pure,
  et le materiau de pilote -- ressource unique et irreversible -- est
  preserve. NOTE, consignee avant lecture du run de M12 : B reste ouvert
  aux memes conditions, mais deviendra probablement sans objet -- le run de
  M12 produira 39 lignes d'attrition fraiches (13 points x 3 degres), et
  toute mise a jour future de q_L se fera par regle EXHAUSTIVE pre-declaree
  (toutes les lignes balayees sous cette geometrie), jamais par selection.
  CE QUE LA v4 ETABLIT (gel m12_pre_enregistrement_v4.md, bf9866a7) :
  - le plafond 12 de v1-v3 n'etait PAS DERIVE (il suivait la table
    indicative) ; c'est cette constante, elle seule, qui a declenche
    l'arret. Le plafond v4 est DERIVE : epuisement des deux passes, 8+8=16.
    (Statut d'erratum du plafond non derive : decision de registre, E18.)
  - rangs 13-16 = 1.86, 2.57, 1.74, 1.77, par les memes regles, en
    arithmetique exacte (entiers de centiemes machine 1, Fraction machine
    2) ; AUCUNE egalite nouvelle -- celle du rang 12 reste la seule ;
  - espacement minimal 0.0200 -> 0.0100 (paires 1.73/1.74 et 1.76/1.77) ;
    controle rule-11 relu : 1e-9 = 1e7 fois sous l'espacement ;
  - D-N, application opposable : q_L = 0.22961693269696845 (ed0e27b1),
    s_pt = 0.4572147008, minimalite par encadrement P(12) = 0.876124 <
    0.90 <= 0.915439 = P(13) ; N = 13, programme 75 recherches, cout total
    de la manche 100, dont 25 deja executees ;
  - la table indicative est retiree (intrant mesure ; ses deux premieres
    lignes etaient inatteignables, 44.7b) ; la clause d'arret de v3 s'est
    executee et ne se rearme pas ;
  - rangs 14-16 : AUCUN statut de reserve implicite, toute utilisation
    future exigerait son propre gel.

45.5 LA CERTIFICATION DU GEL v4 (f10ffcf3) : CE QU'ELLE TRANCHE ET DECLARE
---------------------------------------------------------------------------
  CERTIFIE ; bf9866a7 autorise le depot de m12_ponctuel_v1.py (E19-1).
  - LE PIRE POINT EST TRANCHE : 1.73, sur les treize du programme comme sur
    les seize de la liste (sigma_pire = 6.550e-05 ; entrants les plus
    proches, 1.74 et 1.77, aux rangs 15-16, hors programme). Ancrages
    INCHANGES : 0.03 = 458 x, 0.10 = 1527 x.
  - L'EXTENSION EST CONTRESIGNEE SUR TEST DECIDABLE : les seize rangs se
    re-derivent sans utiliser q_L, N, ni aucune valeur du run -- aucun
    degre de liberte exerce apres la mesure. Plus propre, note la
    certification, qu'un raffinement de grille, qui aurait cree des rangs
    non derivables avant la mesure.
  - L'ECART A LA LETTRE DE LA CLAUSE DE v3, DECLARE : la clause prescrivait
    de raffiner la GRILLE DE CANDIDATS -- objet nomme et defini, que v4 ne
    touche pas. Ce que v4 corrige est un PLAFOND non derive : strictement
    moins invasif, aucun candidat, aucune fenetre, aucune regle nouvelle.
    La phrase d'historique de v4 presentait cet ecart comme une execution
    de la clause ; la ligne corrective, pre-ecrite par machine 2, est
    consignee ici et entrera dans toute version future du bloc :
    "La clause d'arret de v3 prescrivait de raffiner la GRILLE DE
    CANDIDATS. v4 ne la touche pas : elle corrige un PLAFOND non derive, ce
    qui est strictement moins invasif et n'introduit aucun candidat, aucune
    fenetre et aucune regle. L'ecart a la lettre de la clause est declare."
  - CHIFFRES DE PLAN, ecrits avant la mesure : E[m] = 5.94 ;
    P(m >= 4) = 0.915439 ; P(m >= 3) = 0.976114 ; P(m < 3) = 0.023886 --
    la manche a 2.4 % de chances de rendre NON CONCLUANT PAR CONSTRUCTION
    avant de regarder un seul E. C'est le prix du q_L opposable.
  - FAIT EN FAVEUR DU GEL : l'espacement minimal des TREIZE effectivement
    mesures reste 0.0200 -- les seconds membres des paires a 0.0100 (1.74,
    1.77) sont hors programme. Le 0.0100 declare est le chiffre de la
    LISTE, conservateur et correct pour rule-11.

45.6 PRE-DECLARATION : LA PAIRE G8 DE M12 -- CONTRESIGNEE, MOTIFS CORRIGES
---------------------------------------------------------------------------
  (v3 : motifs mis en conformite avec la note machine 2, ad8dd209)
  Le programme fige porte "G8 (regression p=4) : 2" sans nommer les deux
  points -- meme classe que G1' avant sa correction S5a. PRE-DECLARE, regle
  mecanique, aveugle aux donnees, anterieure au code, et CONTRESIGNEE par
  machine 2 sur ce seul critere :
      G8a/G8b portent sur les RANGS 1 ET 13 de la liste (2.22 et 1.86).
  MOTIF RETENU, DE POSITION (machine 2, adopte verbatim) : les rangs 1 et
  13 sont le PREMIER et le DERNIER du programme, donc la paire la plus
  ecartee EN RANG que la liste permette. Mecanique, verifiable, et cela ne
  pretend rien sur l'informativite.
  MOTIF (ii) DE LA v2, RETIRE -- FALSIFIE PAR LA DONNEE : "le rang 13
  couvre la zone gauche ... ou la regression de parite est la plus
  informative" affirmait un pouvoir differentiel que le pilote dement. Aux
  quatre points de p=4 : la fenetre fine a du pouvoir PARTOUT (transition
  encadree aux quatre, partage explosifs/non explosifs de 19/57 a 26/50,
  variation douce, aucun point privilegie) ; la fenetre grossiere n'en a
  NULLE PART (gros_explosifs = 0 aux quatre -- deux masques tout-False
  compares, et le champ le declare lui-meme : "pouvoir NUL si les deux
  comptes sont 0", la parade (b) en fonctionnement). Une affirmation
  d'informativite qui n'avait pas ete comptee : meme famille que le motif
  errone de l'attente G1 (45.2).
  MOTIF (i), REQUALIFIE : la coherence avec G2 tient sous la SEULE lecture
  de "G2 : 3 x 2 = 6" qui rende le total 75 coherent -- trois degres, DEUX
  SIGNES, six recherches NEUVES a 2g au rang 1 -- mais cette lecture se
  DEDUIT, elle ne se lit pas. OBLIGATION AU SCRIPT : l'enumeration
  EXPLICITE des six recherches de G2, comptee et jamais affirmee (meme
  exigence que G1 ; l'ambiguite est de redaction, pas de plan, et le gel
  v4 certifie n'a pas a etre rouvert pour cela).
  CONSIGNATIONS NOUVELLES, ecrites AVANT la mesure de M12 :
  - G8b N'EST PAS DEUX CONTROLES, C'EN EST UN : sa moitie grossiere a p=4
    compare des masques vides. Un lecteur qui compterait "grossier + fin"
    compterait deux comparaisons la ou une seule mord.
  - ATTENTE PRE-DECLAREE (machine 2, avant la mesure) : la moitie grossiere
    de G8b sera VIDE a p=4 aux treize points de M12 -- les s* de p=4 y sont
    grands (~2.04 a ~8.11 interpoles), la fenetre [LO0, 0.90 s*] couvre une
    plage ou rien n'explose. Si elle MORD, c'est un FAIT NEUF, a consigner
    comme tel.

45.7 REGISTRE
--------------
  Empreintes nouvelles : cert. script pilote v1 6acb1fe9 ; cert. script
  pilote v2 a7ef9362 ; cert. script pilote v3 774f7de4 ; scripts
  m12_pilote_v1/v2/v3 cccc8a7b / 9d88798a / 663b17e2 ; run JSON ed0e27b1 ;
  message de run 05147405 ; gel M12 v4 bf9866a7 ; certification du gel v4
  f10ffcf3 ; delta 45 v1 fb13077a ; delta 45 v2 c55d9ee0 ; note machine 2
  sur delta 45 v2 ad8dd209.
  Toujours ouverts (renvoi 44.6) : promotion de la regle elargie ;
  collision du S42.3 (aucun numero avant arbitrage) ; double etat du
  document de synthese ; bilan des fautes M8-M11, qui prendra le prochain
  numero libre au moment de sa consignation (regle E18).

PROCHAINE ETAPE : m12_ponctuel_v1.py -- gel jumeau v4 (bf9866a7), geometrie
et utilitaires exacts importes du script pilote certifie m12_pilote_v3.py
(663b17e2), G1' au bit contre ed0e27b1, paire G8 des rangs 1 et 13 (45.6),
G2 enumere, moitie grossiere de G8b declaree attendue vide, selftest qui
mord, pre-vol joue par la machine qui detient les sources -- puis le run :
75 recherches, et la premiere lecture de E de toute la campagne.

=== FIN DU DELTA 45 ===
