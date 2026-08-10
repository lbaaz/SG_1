DELTA 45 -- LE RUN DU PILOTE M12 : L'ARRET EXECUTE, DEUX ACQUIS, ET LE GEL v4
(01/08/2026 ; consigne par machine 1 ; ASCII, NFC+LF)

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
  fenetre grossiere. Le point qui exclut est a 0.90 s* exactement, soit
  s_fin[0], le PREMIER point que l'instrument regarde sous le seuil -- par
  construction, pas par coincidence -- et a 3.6e14 epsilons du bord 0.98 :
  les temoins S4/S6 l'etablissent SUR DONNEE (zero ligne ou l'indice 40
  compte sous le seuil, zero explosif a cet indice, sur 24 balayages).
  Faits d'instrument annexes, SANS AUCUNE LECTURE PHYSIQUE (le pilote ne
  teste rien, ne forme aucun E) : 8 ilots dans la fenetre elargie contre 3
  chez M10 ; retombee a 1.002 s* que le pas de M10 (~0.005 s*) ne pouvait
  pas voir ; et la pathologie siege sur le signe NON fragile de la ligne
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
  preserve.
  CE QUE LA v4 ETABLIT (gel m12_pre_enregistrement_v4.md) :
  - le plafond 12 de v1-v3 n'etait PAS DERIVE (il suivait la table
    indicative) ; c'est cette constante, elle seule, qui a declenche
    l'arret. Le plafond v4 est DERIVE : epuisement des deux passes, 8+8=16.
    (Statut d'erratum du plafond non derive : decision de registre, E18.)
  - rangs 13-16 = 1.86, 2.57, 1.74, 1.77, par les memes regles, en
    arithmetique exacte (entiers de centiemes, machine 1 ; a re-deriver par
    machine 2 a la certification) ; AUCUNE egalite nouvelle -- celle du
    rang 12 reste la seule exercee ;
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
    future exigerait son propre gel ;
  - point de certification explicite laisse a machine 2 : 1.73 reste-t-il
    le pire point en sigma_E sur les SEIZE (les quatre entrants sont
    interieurs a [1.73, 2.80] en w2) ; a defaut, l'ancrage serait relu sans
    que les seuils changent.

45.5 REGISTRE
--------------
  Empreintes nouvelles : cert. script pilote v1 6acb1fe9 ; cert. script
  pilote v2 a7ef9362 ; cert. script pilote v3 774f7de4 ; scripts
  m12_pilote_v1/v2/v3 cccc8a7b / 9d88798a / 663b17e2 ; run JSON ed0e27b1 ;
  message de run 05147405 ; gel M12 v4 : empreinte au message de livraison.
  Toujours ouverts (renvoi 44.6) : promotion de la regle elargie ;
  collision du S42.3 (aucun numero avant arbitrage) ; double etat du
  document de synthese ; bilan des fautes M8-M11, qui prendra le prochain
  numero libre au moment de sa consignation (regle E18).

PROCHAINE ETAPE : certification croisee du gel M12 v4 (derivation pure,
aucune mesure prealable), puis m12_ponctuel_v1.py -- geometrie et
utilitaires importes du script pilote certifie, gel jumeau v4, selftest qui
mord, pre-vol joue par la machine qui detient les sources -- puis le run :
75 recherches, et la premiere lecture de E de toute la campagne.

=== FIN DU DELTA 45 ===
