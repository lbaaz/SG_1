JOURNAL DELTA 68 -- INVENTAIRE EN EXTENSION DE LA FENETRE, N-23 LEVEE,
D-6 REGLEE, DEUX DEFAUTS DE GOUVERNANCE OUVERTS (machine 2, 2026-08-10)
=======================================================================
S'insere apres le delta 67. Numero pris A L'ACTE au depot, sous la
regle 66.5.c. Aucun numero posterieur n'est reserve.

68.1 DEPOT (triplet machine 2, convention journal/)
  note_machine2_inventaire_fenetre_N23_D6_v1.md
    430254ba6c20ad0c  12039 o
  inventaire_fenetre_site83_machine2_v2.py
    af72a66224c933f4   8574 o
  inventaire_fenetre_site83_machine2_v2.log
    0fc2f97af95696b3   6947 o
  Objet : produire, AVANT l'ouverture de la session de gel, l'inventaire
  que N-23 et le correctif de D-6 exigeaient -- travail machine 2, qui
  detient les artefacts. Aucune mesure rejouee.

68.2 ARTEFACTS OUVERTS, EMPREINTES CONFORMES
  m15_results.json  96d784077577d57d   (designe nommement par N-23)
  m12_results.json  fa109da92e582520
  m13b_results.json 22fa176013a9d46b
  Statuts lus au BLOC DE GARDE G6, jamais a la carte : le champ
  'recevable' de la carte qualifie la RECHERCHE et non l'exclusion
  (defaut D1-3 du run M12). Recompte des mortes M15 == resume.
  points_perdus de l'artefact, verifie par assert dans le script.

68.3 N-23 EST LEVEE -- ET ELLE RENFORCE B2
  Au seul degre 4 : 2.71 MORTE . 2.72 VIVANTE . 2.73 MORTE.
  La signature 48.3 est donc instanciee AU DEGRE 4 -- le degre sans
  lequel E n'existe pas, celui dont le rang au site est (6,2) -- et
  plus seulement au niveau point. La reserve de niveau imposee par la
  note d'arbitrage (fait "cite au niveau point exclusivement") TOMBE.
  Reserve a declarer au gel : juxtaposition inter-manches (2.72 de
  M12, 2.71 et 2.73 de M15), legitime par 48.4.
  Observation neuve : 2.71 meurt a DEUX degres (4 et 7|+1), 2.73 a UN
  seul (4) -- la maille du crible n'est pas uniforme sur la fenetre.

68.4 D-6 EST REGLEE : L'INVENTAIRE EST ECRIT ET IL SE RE-DERIVE
  42 lignes dans [2.62, 2.73]. Les quatre comptes du dossier v2 se
  re-derivent des artefacts SANS ECART -- p=4 4/7 et impair 2/24
  (fenetre M15) ; p=4 5/9 et impair 3/28 (complement sans 2.72).
  C'est la premiere fois qu'ils sont COMPTES et non cites du gel v4.
  Point tranche : 2.72 PORTE une ligne p=4 mesuree VIVANTE
  (4|2.72|+1, M12). Le 5/9 ne s'atteint qu'en sortant 2.72
  ENTIEREMENT. Inventaire reel complet : p=4 5/10 (q_L 0.6732),
  impair 3/32 (q_L 0.1656).

68.5 D-8 (NEUF) -- L'UNITE DE COMPTE N'EST DECLAREE NULLE PART
  G6 exclut par BRANCHE DE SIGNE ; la campagne declare a p impair la
  convention s* = min des deux signes (M1/(f)), dont l'unite naturelle
  est (degre, point). Impair vaut 3/32 (0.1656), 3/16 (0.3180) ou
  0/16 (0.0957) selon l'unite. LES TROIS MORTS IMPAIRS SONT DE SIGNE
  +1 (5|2.65|+1, 7|2.67|+1, 7|2.71|+1) : aucune unite impaire n'est
  morte aux deux signes. p=4 etant quasi mono-signe, le
  DIMENSIONNEMENT de la strate 1 est robuste ; c'est la LECTURE
  degre-selective (section 3.4, matiere de B3) qui depend de l'unite
  -- rapport p=4/impair de 4.1, 2.3 ou 7.7. Le SENS ne s'inverse dans
  aucune lecture. Famille E17 : comparaison inter-degres sans unite
  declaree.

68.6 D-9 (NEUF) -- LE TRAITEMENT DES ANCRES N'EST PAS SYMETRIQUE
  N-22 place 2.62 et 2.72 sur le meme plan ; le compte du dossier
  garde 2.62 dedans et met 2.72 dehors. Les deux sont des SURVIVANTS :
  les sortir baisse n sans baisser k.
    les deux dedans  p=4 5/10 -> 0.6732
    2.72 dehors      p=4 5/9  -> 0.7325   [lecture du dossier]
    2.62 dehors      p=4 5/8  -> 0.8014
    les deux dehors  p=4 5/7  -> 0.8805
  AMPLITUDE 0.2073 sur la borne qui dimensionne la strate 1, soit 2.7
  fois l'instabilite (0.0769) qui a fait RETIRER le q_L de niveau-
  point en D-1. Le P(>=1) = 0.5405 consigne d'avance vient de la
  fenetre M15 SEULE, qui n'est aucune des quatre politiques ; a N = 3
  la fourchette reelle va de 0.3175 a 0.6949.

68.7 PRESCRIPTIONS N-33 A N-36 (texte opposable : note 430254ba,
     section 6 -- le gel les EXTRAIT, il ne les re-frappe pas)
  N-33 inventaire de la section 2 de la note, extrait par structure ;
       compte = cardinal de la liste, verifie par assert.
  N-34 unite de compte DECLAREE avant mesure, identique aux deux
       degres ; toute comparaison inter-degres cite son unite (E17).
  N-35 politique d'ancres SYMETRIQUE et declaree ; N derive EN FORME
       (regle 13) ; fourchette 0.6949 / 0.3175 consignee d'avance ;
       la clause "zero n'est pas une refutation" se lit contre la
       borne basse.
  N-36 signature enoncee AU DEGRE 4, juxtaposition inter-manches
       declaree (48.4), asymetrie 2.71 / 2.73 consignee.

68.8 CE QUE CE DELTA NE FAIT PAS
  Aucune mesure rejouee, aucun gel redige. Le choix ENTRE les lectures
  de 68.5 et 68.6 n'est pas fait : il appartient au gel, qui doit le
  DECLARER avant mesure. L'arbitrage du trilemme est inchange -- B2
  vehicule, B3 lecture, B1 ecartee ; N-20 a N-32 restent opposables.
  Les bornes de domaine (0.0855 / 0.0679) ne sont pas recalculees.
  Aucun numero d'erratum n'est attribue (E18).

PIECES CITEES (16 hex ; brut == canonique NFC+LF)
  note d'inventaire 430254ba ; script af72a662 ; log 0fc2f97a ;
  artefacts 96d78407, fa109da9, 22fa1760 ; dossier trilemme v2
  347f25da ; note d'arbitrage 1c490f90 ; note de controle ae8ff790 ;
  deltas 66 ab5db7ef et 67 6194e90f ; gel v4 35022c5c (cite, non
  rouvert).
  Borne : 68.

=== FIN DU JOURNAL DELTA 68 ===
