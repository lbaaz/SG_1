DELTA 44 -- GELS M12 / M12-PILOTE : v1 -> v3, CERTIFICATION, ET LA CLASSE DES
COMPARAISONS DE BORD
(01/08/2026 ; consigne par machine 1 ; ASCII, NFC+LF ; le bilan des fautes
M8-M11 ouvert en debut de seance reste A CONSIGNER et prendra le prochain
numero libre a sa consignation, E18)

44.1 CHAINE DES VERSIONS ET VERDICTS
------------------------------------
    M12     v1 48ffd952  NON CERTIFIE   v2 4eed58b2  NON CERTIFIE   v3 6134cd82  CERTIFIE
    PILOTE  v1 3bddd5a4  NON CERTIFIE   v2 38656ce7  NON CERTIFIE   v3 03e29c86  CERTIFIE
    CERT    v1 7225c2ca (01/08)         v2 4aa88115 (01/08)         v3 fc61a25c (01/08)
  Les empreintes v3 sont celles qui AUTORISENT le code (E19-1).
  L'architecture n'a jamais bouge de v1 a v3 et a ete contresignee trois
  fois : E ne traverse ni regression, ni levier, ni Sxx, ni plancher. Ce qui
  a demande trois versions n'est pas la question posee -- c'est l'arithmetique
  avec laquelle on choisissait ou la poser (formule de la cert. v3, exacte).
  La date de la cert. v1 est 01/08 ; le 27/07 des historiques v2 venait de
  l'en-tete du message v1 de machine 2, corrige en v3.

44.2 LA CLASSE : COMPARAISON DE BORD EVALUEE EN FLOTTANT SANS TOLERANCE
------------------------------------------------------------------------
  Definition (regle gelee aux deux blocs v3, forme elargie par la cert. v2) :
  TOUTE comparaison dont le resultat peut basculer sous une perturbation de
  l'ordre de l'epsilon machine -- egalite, ou inegalite evaluee sur son
  bord -- s'evalue en arithmetique EXACTE quand les entrees sont exactes, a
  tolerance declaree sinon.
  TROIS INSTANCES dans le meme dossier, toutes sur des centiemes exacts :
  (i)   S2, les quatre points du pilote : deux sous-ensembles a egalite
        exacte d'espacement (3/10) ; en IEEE ecart 4.4e-16, l'egalite n'a
        jamais eu lieu, le departage ecrit n'a JAMAIS ete exerce. Resultat
        corrige {1.70, 2.15, 2.45, 2.75}, regle conservee.
  (ii)  Le pseudo-tie du rang 9 ([2.18,2.26], 1/25 des deux cotes) : consigne
        en v2 comme fait, revele SYMPTOME -- l'egalite n'existait que dans la
        lecture flottante du filtre de nouveaute. Retire en v3.
  (iii) Le filtre de nouveaute lui-meme (defaut de fond, cert. v2) : treize
        candidats R-2'-propres a 3/100 EXACT d'un point de grille ; en IEEE,
        neuf passent (+2.2e-16) et quatre tombent (-1.9e-16) : 2.27, 2.63,
        2.72, 2.78. La liste gelee v1/v2 n'etait derivable d'AUCUNE lecture
        exacte de la regle ecrite. Resolution : LECTURE A (d >= 0.03, exact),
        la regle telle qu'ecrite -- l'arithmetique etait fausse, pas la
        regle. Trois points sur douze changent, l'ordre change (2.67 au rang
        2) ; les ensembles A et C coincident jusqu'a N=8 inclus, divergent a
        N=9. Seuils, ancrages, pilote, programmes : INTOUCHES.
  UNE egalite reelle subsiste dans la selection, et une seule (compte par les
  deux machines) : rang 12, fenetre [2.78,2.82], extremes a 2/100 exacts de
  2.80, tranchee 2.78 par le departage ecrit en v2 AVANT d'etre rencontree --
  premiere egalite de selection de la campagne reglee ainsi.
  PREMIERE SELECTION DE LA CAMPAGNE ETABLIE EN ARITHMETIQUES INDEPENDANTES :
  Fraction exacte (machine 2) contre entiers de centiemes + encadrement
  rationnel de sqrt(2) (machine 1), accord total -- fenetres, liste, ordre,
  espacement, les treize du fil, les quatre exclus a tort.

44.3 ERRATUM E28 (machine 2, contre sa certification v1)
--------------------------------------------------------
  La cert. v1 declarait les huit fenetres "IDENTIQUES" apres une re-derivation
  EN FLOTTANT : reproduction de l'arrondi de machine 1, pas controle. Enonce
  faux ; meme famille que E24 et D-M10-9. Lecon adoptee DES DEUX COTES :
  une re-derivation qui porte sur une selection se fait dans une arithmetique
  DIFFERENTE de celle du calcul original, ou l'accord ne prouve rien.
  E28 est a ce jour le dernier erratum du registre.

44.4 ACQUIS DE CONCEPTION : L'IMPOSSIBILITE 5-ADIQUE DE LA MARGE 1.10
----------------------------------------------------------------------
  Enonce (machine 2, cert. v3, contre-verifie machine 1 par enumeration) :
  les quatre seuils 1.10 x rayon valent 33/250, 33/1000, 33/4000, 33/16000 --
  valuation 5-adique du denominateur egale a 3 -- tandis que toute distance
  |centieme - k/l| a un denominateur reduit divisant lcm(100, l), de
  valuation 5-adique au plus 2 (observee : {0,1,2} ; l resonant <= 5, plus
  serre encore que le l <= 11 de l'enonce). AUCUNE distance ne peut donc
  atteindre un seuil : le census "zero candidat sur la marge" n'est pas une
  enumeration heureuse, il est FORCE par le facteur 11/10, quelle que soit la
  grille de candidats en centiemes et quelle que soit la table des rayons.
  Le seul fil possible etait celui de la nouveaute, dont le seuil 0.03 est
  lui-meme un centieme -- celui qui a saigne (44.2.iii), celui que la lecture
  A referme. |1.88 - 2| = 3/25 = 1.00 x rayon reste vrai : c'est le fil SANS
  marge qui a motive la marge, pas un contre-exemple.

44.5 CONTRAIGNANT A LA CERTIFICATION DU SCRIPT (cert. v3, section 5)
---------------------------------------------------------------------
  (1) Le --selftest declare la portee REELLE de chaque vecteur : les deux
      vecteurs n_g pincent CEIL (couple (160, 177) propre a ceil) ; le
      vecteur n_f EXCLUT CEIL (77 contre 76 sur le quotient IEEE
      75.000000000000014) mais ne separe pas round de floor, le quotient fin
      etant constant (75 exact). Un controle qui annonce plus qu'il ne tient
      est un piege a retardement.
  (2) Garde de domaine BLOQUANTE au script, forme exacte : s* > LO0/0.90 =
      1/18, STRICTE -- au bord exact le quotient vaut 0 et n_g = 1 --
      equivalente a n_g >= 2 ; ARRET et consignation. Restaure l'enonce de
      domaine du gel M11 v4, perdu par les gels v3 (borne vraie, domaine
      absent). Bande inatteignable en pratique (min campagne ~0.22, pilote
      0.4729) mais "inatteignable" a deja coute.
  (3) Test NEGATIF du filtre de nouveaute : presenter 2.27 (l'un des quatre
      exclus a tort) et exiger RETENU ; le test doit ECHOUER si on lui
      substitue une comparaison flottante.
  (4) Aucun run certifie sans le journal du PRE-VOL a moteur factice ; les
      trois dispositifs (selftest = calcule, relecture = raisonnement,
      pre-vol = chemins) ne se remplacent pas.
  Deux formulations des gels v3 sont NOTEES, gels certifies tels quels, les
  enonces precis vivant ici et au script : "n_f pince ROUND" se lit "n_f
  exclut CEIL" ; "plus proche approche d'un centieme" (sqrt(2)) se lit "plus
  proche approche DU SEUIL 0.03" (elle vaut |1.44 - sqrt(2)| = 0.0258 ; la
  plus proche approche de sqrt(2) elle-meme est 1.41, a 0.0042).

44.6 OUVERT -- DECISIONS DE BAAZ, RIEN N'EST RESERVE (E18)
-----------------------------------------------------------
  (a) PROMOTION de la regle elargie (44.2) en regle transversale -- serait la
      regle 15. Texte fige aux gels v3 ; la promotion est une decision de
      registre, hors gel.
  (b) REGISTRE DES ERRATA : la collision E27 (S42.3 "consignation manquante"
      contre S43 "non-comparabilite G6", deux fautes sous le meme numero dans
      des deltas certifies) reste OUVERTE. E28 est desormais consomme par
      machine 2 (44.3) : toute renumerotation du S42.3 irait a E29. Aucun
      numero ne doit s'ecrire avant l'arbitrage.
  (c) DOUBLE ETAT du document de synthese CAMPAGNE_etat_complet_2026-07-27.md
      (copie projet 13157ae8 portant encore "le criblage est x5" qu'E27
      retire, contre version certifiee 46d25637) : toujours a resoudre.
  (d) Le bilan des fautes M8-M11 (debut de seance) : a consigner, prochain
      numero libre.

PROCHAINE ETAPE : m12_pilote_v1.py. Prealable materiel unique : upload de
m9_replication_v1.py (attendu c8ed357b) et m11_exposant_v3.py (attendu
80cfa795) -- le moteur se reprend, la geometrie se releve du fichier ; rien
ne se retape de memoire d'une citation.

=== FIN DU DELTA 44 ===
