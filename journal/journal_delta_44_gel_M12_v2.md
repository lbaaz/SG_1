DELTA 44 -- GELS M12 / M12-PILOTE : v1 -> v3, CERTIFICATION, ET LA CLASSE DES
COMPARAISONS DE BORD -- version v2
(01/08/2026 ; consigne par machine 1 ; ASCII, NFC+LF ; le bilan des fautes
M8-M11 ouvert en debut de seance reste A CONSIGNER et prendra le prochain
numero libre AU MOMENT de sa consignation (regle E18))

HISTORIQUE DU DELTA
  v1 11f12655 : premiere consignation du cycle, avant depot.
  Note machine 2 sur le delta 44, v1 (3b2de555, 01/08) : verifie 44.1 a 44.5
      CONFORMES ; trois remarques, dont une consequence non tiree (le pilote
      est tout-ou-rien sous D-N). AUCUNE certification remise en cause.
  v2. Integre la note : section 44.7 nouvelle (tout-ou-rien) ; 44.2(iii)
      corrige -- l'enonce de coincidence A/C etait FAUX a N=4 et N=5, et le
      chiffre unique "+2.2e-16" masquait deux groupes d'ecarts ; 44.4
      complete (les deux ecritures 5-adiques ne divergent pas) ; 44.6 et
      l'en-tete reformules sans aucun numero d'erratum, meme conditionnel
      (note, section 5) ; prealable materiel LEVE.

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
        candidats R-2'-propres a 3/100 EXACT d'un point de grille. En IEEE,
        NEUF passent et QUATRE tombent : 2.27, 2.63, 2.72, 2.78, tous a
        -1.94e-16 du litteral 0.03. Les neuf retenus se repartissent en DEUX
        groupes d'ecarts -- +2.78e-17 (1.27, 1.28, 1.73, 1.77, 1.83) et
        +2.50e-16 (2.18, 2.42, 2.57, 2.82), un ordre de grandeur entre eux ;
        le chiffre unique "+2.2e-16" du delta v1, repris de la cert. v2,
        etait une simplification (note machine 2, 3b), et les DEUX valeurs
        figuraient deja, non agregees, dans le census de machine 1. La liste
        gelee v1/v2 n'etait derivable d'AUCUNE lecture exacte de la regle
        ecrite. Resolution : LECTURE A (d >= 0.03, exact), la regle telle
        qu'ecrite -- l'arithmetique etait fausse, pas la regle. Trois points
        sur douze changent, l'ordre change (2.67 au rang 2).
        PORTEE SUR LES ENSEMBLES, rang par rang (corrige en v2 du delta --
        l'enonce v1 "coincident jusqu'a N=8 inclus" etait FAUX a N=4 et N=5,
        le controle de machine 1 ayant commence a N=6 : une phrase qui
        couvrait deux N non testes) :
            N=4 : DIFFERENTS (A porte 2.80, C porte 1.84)
            N=5 : DIFFERENTS (A\C = {2.80}, C\A = {2.55})
            N=6, 7, 8 : IDENTIQUES        N>=9 : DIFFERENTS
        FORMULATION DE REGISTRE (machine 2, contresignee) : sur le seul N
        atteignable (N=8, cf. 44.7), les lectures A et C designent le meme
        ensemble de huit points et la meme ancre de G2 (2.22) ; elles
        divergent des le rang 9, donc des que le programme depasse huit
        points -- ce que D-N interdit sans passer par un gel v4. Ce n'est PAS
        un argument retrospectif contre la correction : une selection dont le
        resultat est correct par compensation reste une selection fausse. La
        portee reelle du defaut, sur cette manche precise, est l'ordre des
        rangs 2 a 6, et rien d'autre tant que N = 8.
        Seuils, ancrages, pilote, programmes : INTOUCHES.
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
  PRECISION DE REGISTRE (note machine 2, 3a) : "valuation exactement 2"
  (cert. v3) porte sur v5(lcm(100, l)) ; "{0, 1, 2}" (ci-dessus) porte sur le
  denominateur REDUIT, qui divise le precedent. Deux objets, deux ecritures,
  MEME conclusion -- qu'un futur lecteur ne les prenne pas pour une
  divergence.
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

44.6 OUVERT -- DECISIONS DE BAAZ, RIEN N'EST RESERVE
-----------------------------------------------------
  (a) PROMOTION de la regle elargie (44.2) en regle transversale. Texte fige
      aux gels v3 ; la promotion est une decision de registre, hors gel.
  (b) REGISTRE DES ERRATA : la collision du S42.3 ("consignation manquante")
      avec le S43 ("non-comparabilite G6"), deux fautes sous le meme numero
      dans des deltas certifies, reste OUVERTE. Sa resolution recevra son
      numero AU MOMENT de la consignation, et aucun numero ne s'ecrit avant
      l'arbitrage -- pas meme au conditionnel : ecrire un numero a cote d'un
      item en attente est la facon dont une reservation commence (note
      machine 2, section 5). Fait de registre utile a l'arbitrage : le
      dernier erratum consigne est E28 (44.3).
  (c) DOUBLE ETAT du document de synthese CAMPAGNE_etat_complet_2026-07-27.md
      (copie projet 13157ae8 portant encore "le criblage est x5" qu'E27
      retire, contre version certifiee 46d25637) : toujours a resoudre.
  (d) Le bilan des fautes M8-M11 (debut de seance) : a consigner ; il prendra
      le prochain numero libre AU MOMENT de sa consignation (regle E18).

44.7 LE PILOTE EST TOUT-OU-RIEN, ET AUCUN DES DEUX GELS NE LE DIT
------------------------------------------------------------------
  (Note machine 2 v1, section 1 ; contre-verifie machine 1 au chiffre.)
  D-N applique aux seules issues que le pilote peut rendre, 12 lignes :
      pertes   q_L (CP sup 80 %)   N par D-N
        0           0.1255            8
        1           0.2296           13   -> ARRET (N > 12), gel v4
        2           0.3238           20   -> ARRET
        3           0.4124           32   -> ARRET
  DEUX ISSUES ET DEUX SEULEMENT : zero perte et M12 tourne a N = 8, ou toute
  perte et le programme s'arrete sur un gel v4. Il n'existe AUCUN regime
  intermediaire, aucun "M12 coute un peu plus cher".
  (a) DIVERGENCE ATTENTE / REGLE, consignee AVANT le run : la section MES
      ATTENTES du pilote -- ecrite en v1, jamais reecrite, et elle doit le
      rester -- traite "0 ou 1 ligne" comme le cas nominal et "2 ou plus"
      comme un surcout. Sous D-N, UNE ligne perdue est un MUR, pas un
      surcout. Ce n'est pas un defaut des gels (le cas ARRET y est
      pre-declare, ecrit d'avance pour ne pas etre resolu par improvisation) :
      c'est l'attente qui a ete ecrite avant que la consequence de D-N soit
      calculee. Elle reste telle quelle ; le registre porte que son economie
      ne suit pas de la regle.
  (b) TABLE INDICATIVE DE D-N : ses deux premieres lignes (q_L = 0.05 -> N=6,
      0.08 -> N=7) ne decrivent aucun etat du monde accessible a CE pilote --
      le q_L minimal a 12 lignes vaut 1 - 0.20^(1/12) = 0.1255, atteint a
      perte nulle, donc N >= 8 TOUJOURS. La table est declaree "pour lecture
      seulement" et ne remplace pas le calcul : rien a corriger au gel, mais
      le fait est consigne ici.
  CONSEQUENCE POUR LE SCRIPT DU PILOTE : son resume consignera l'application
  INDICATIVE de D-N a son q_L (N obtenu, et l'issue -- EXECUTABLE a N=8 ou
  ARRET vers gel v4), clairement etiquetee indicative : la regle D-N
  appartient au gel M12 et son application OPPOSABLE au script de M12.

PROCHAINE ETAPE : m12_pilote_v1.py. Le prealable materiel est LEVE : les deux
fichiers sont recus et verifies par machine 1 (m9_replication_v1.py c8ed357b,
m11_exposant_v3.py 80cfa795, brute = canonique, ASCII pur LF), conformement
au principe contresigne par les deux machines -- le moteur se reprend et la
geometrie se releve DU FICHIER, jamais d'une citation.

=== FIN DU DELTA 44 ===
