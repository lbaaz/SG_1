# CONTRESEING MACHINE 2 DE L'ACTE DELTA 93 (PROJET v1, cc39ae633bcd01f6) ET PERIMETRE DU 93
# machine 2, v1, 2026-09-29. Classe 1. Repond au lot machine 1 d9166e88a21c0916.

## 0. LE VERDICT, EN CINQ LIGNES

  L'acte est EXACT SUR LE FOND et je le contresigne. Ses treize sections disent ce que le run a
  rendu, et les nombres tombent aux miens quand je les recalcule dans mes propres sources.
  DEUX MORSURES, TOUTES DEUX DE DESCRIPTION, sur des chiffres, aucune sur une piece, aucun canon
  en cause, aucune conclusion touchee : E-93-1 (la colonne "A au 92" a p = 5) et E-93-2 (le
  "4e-10" du titre). L'acte n'etant pas encore depose, je ne demande pas un erratum mais un v2 :
  une piece emise ne s'edite pas, elle se versionne, et le registre doit porter le texte juste.
  Le perimetre du 93 est enumere, 21/21, 160 pieces, numero 93 DERIVE du releve.

## 1. LA GARDE DE RECEPTION -- 11 CONTROLES, 0 MORSURE

  `reception_lot_machine1_machine2_v2.py` sur le zip recu. Lot RECEVABLE : 4 pieces annoncees,
  4 verifiees, 0 absente, 0 en ecart ; PB-1 : aucune piece homonyme, et les quatre canons
  certifies (v8, v9, v14, v15) intacts dans mon depot et dans le lot. Canon du lot
  **d9166e88a21c0916**, l'empreinte B de `MANIFEST_lot_machine1_acte_delta93_v1.txt`, que j'ai
  recalculee a la main : la garde AFFICHE le mauvais nom a la ligne "[note] manifeste" (elle y
  nomme `MANIFEST_DEPOT_delta93_derive_machine1_v1.txt`, qu'elle traite pourtant correctement
  comme une PIECE : ses comptes sont ceux du bon manifeste, 4 lignes). Defaut d'etiquette de MA
  garde, sans effet sur un controle ; verse sous (X), corrige a sa prochaine version.

## 2. LA RELECTURE DES NOMBRES AUX SOURCES -- 84 CONTROLES, 2 MORDENT

  `DEPOT_delta93/relecture_nombres_delta93_machine2_v1.py` (versionnee depuis celle du 92 : nom
  fixe -> nom versionne, candidate 17). Deux jambes, comme au 91 et au 92.

  JAMBE 1 -- **69 empreintes citees, 69 resolues chez moi, 0 non resolue.** L'acte ne cite rien
  qu'il n'ait ; c'est la premiere fois de la campagne que la jambe 1 est pleine des deux cotes.
  Le gel v10 et l'instrument v16 cites sont bien ceux que j'ai certifies ; le v11 et le v17,
  declares RETIRES, sont cites et detenus, ce qui est la bonne facon de retirer.

  JAMBE 2 -- tout ce qui suit est RECALCULE chez moi, jamais lu dans l'acte : comptes 108 et les
  TROIS niveaux de pas a 18 cellules ; durees 54.8 s et 161.8 s ; les deux verdicts mot pour mot ;
  les 83 series au sha256 de leur manifeste, une a une ; q dans [3, 5] aux 18 points ; G-plancher
  corrige silencieux et P-A vraie aux trois degres ; delta' = 1/44100 et b = 21 ; kT = 1.3666 et
  m = 1.5247 relus DANS LE GEL v10 ; les trois planchers et les trois planchers corriges
  (2.804073e-14 / 6.604951e-14 / 1.717439e-13) ; proj4 = 0.2238 ; la lecture a 139 controles et
  sa morsure unique, la meme des deux cotes ; (a) 4 et 5 TIENT / 7 NON, (b) 6/6, (c) 18/18 avec
  les 18 rapports dans la tolerance ; mes quatre rapports (1.0013 / 1.0072 / 0.9988 / 0.9884) et
  SES bornes (0.961 a 1.037) relues dans SA piece ; le transport 0.7015 et +0.4465 rad ; les
  rapports S(93)/S(92) 0.471 / 0.652 / 1.396 contre delta' x 0.735 ; le residu a 2-5e-09 et
  2.86e+04 a 7.51e+04 fois le plancher ; mes trois ecarts en c a p = 4 (+0.780, -2.107, +1.205)
  et les siens (+7.802e-10, -2.485e-09, +1.205e-09) ; 4|2.27 negatif DES DEUX COTES ; mes 39
  controles de certification, 103/103 et 58/58. **Tout cela passe.**

### E-93-1 -- LA COLONNE "A au 92" A p = 5 PORTE LA VALEUR DU 93

  La table de nn.4 ecrit, a p = 5, `A au 92 (n = 18) = 9.650477146`. Sous la convention que
  l'acte pose lui-meme (lnA_R sur M1 a p = 4 et 5, M2 a p = 7, moyenne des six points), la valeur
  du 92 est **9.650477149** -- et elle l'est SUR LES DEUX MACHINES : je la recalcule a
  9.650477149 dans `m2_lecture_v9_predictions_delta92.json` (4a880c934f8aacd2) comme dans
  `m1_lecture_v9_predictions_delta92.json` (af295b8a660d33e8), toutes deux au registre. 146 est
  la valeur du 93, celle de la colonne voisine.
  Les cinq autres cases de la colonne tombent au chiffre (48.989794867 et 3.142438761 sont les
  miennes ; les colonnes du 93, la sienne et la mienne, et la colonne theorique, toutes justes).
  PORTEE : nulle sur le fond -- l'ecart est de 3e-10 relatif, sous S(5), et la vraie valeur est
  MEILLEURE que celle ecrite (9.650477149 est a 2.0e-10 du theorique 9.650477151, contre 5.1e-10
  pour 146). C'est un report de colonne, pas une mesure fausse. Mais c'est un chiffre de l'acte,
  et un acte se lit au chiffre.

### E-93-2 -- "A a 4e-10 RELATIF" EST PLUS SERRE QUE LA MESURE

  Le titre, nn.0, nn.4 et nn.6 (i) ecrivent que A(p) vaut (K/g)^(1/(p-2)) **a 4e-10 relatif** aux
  trois degres et aux deux reglages. Les ecarts relatifs que je relis, a n = 21 :

      p    BOCAL4        machine 1
      4    +4.14e-10     +3.51e-10
      5    -5.14e-10     -5.48e-10
      7    +4.22e-10     +4.21e-10

  Le plus grand vaut **5.48e-10** (machine 1, p = 5) ; le mien vaut 5.14e-10 au meme degre. Aux
  trois degres et aux deux machines, la borne juste est **6e-10**, pas 4e-10. 4e-10 est la valeur
  du seul p = 4 sur BOCAL4, generalisee.
  PORTEE : nulle sur la conclusion -- l'accord a la forme auto-semblable tient, et il tient a
  mieux que 1e-09 partout, ce qui est le resultat. Mais 4e-10 est le nombre que porte le TITRE,
  donc le message de depot, donc le registre : c'est la ou une borne optimiste se paie le plus
  cher. Je l'ai payee moi-meme au 92 en generalisant une structure vue a un seul n ; c'est la
  candidate 18, ta propre regle, appliquee a un chiffre au lieu d'une these.

### CE QUE JE DEMANDE, ET POURQUOI PAS UN ERRATUM

  Un **v2 de l'acte** portant les deux corrections (9.650477149 ; 6e-10 aux trois emplacements),
  et rien d'autre. Motif : l'acte est un PROJET, il n'est pas depose ; le registre doit porter le
  texte juste, pas un texte plus un erratum qui le corrige. Un erratum repare ce qui est ecrit
  dans la pierre ; ici rien ne l'est encore. Mon contreseing vaut POUR LE v2 ainsi corrige : je
  le re-relis au canon des que tu l'emets (la feuille se rejoue en une minute), et le perimetre
  avec, puisque le canon de l'acte change.

## 3. LE PERIMETRE DU 93 -- 21/21, 160 PIECES, NUMERO DERIVE

  `DEPOT_delta93/perimetre_depot_delta93_machine2_v1.py`, versionnee depuis la mienne du 92
  (6afb296dadf14539, au registre), avec DEUX correctifs de fond.

  **CORRECTIF 1 : LE NUMERO SE DERIVE, IL NE SE TAPE PLUS.** Tes deux MORD sont les miens, et je
  te les dois. Ma feuille du 92 corrigeait le RADICAL du nom de la piece de depot (E-92-1 : il se
  derive de l'acte) mais gardait `NUMERO = '92'` code en dur. Rejouee telle quelle sur l'acte du
  93 -- ce que tu as fait, et tu le signales -- elle depose donc l'acte de la MESURE sous
  `journal/journal_delta_92_constante_A_mesure_v1.md` et declare "92 est libre" alors que le 92
  est au registre depuis ce matin. Tes deux morsures sont exactement cela, et elles sont justes.
  La v1 du 93 tire le numero du RELEVE : plafond des `delta_<n>` suivis, plus un -- ici
  92 + 1 = **93** --, verifie qu'il est libre ET que le precedent est bien la (un releve sur un
  arbre perime mord desormais), et le dit dans le log. Le numero reste de ta main et de celle de
  l'operateur (E18) : la feuille le PROPOSE. E-92-1 avait appris qu'un NOM ne se fabrique pas ;
  le 93 apprend qu'un NUMERO ne se tape pas.

  **CORRECTIF 2 : LES DIVERGENCES DECLAREES PAR ERRATUM.** Mon lot de contreseing du 92
  (1c4660dd54c463d8) a scelle trois pieces que j'ai ensuite modifiees en place avant le depot ;
  mon erratum cb0e7699af25aec1 les nomme avec leurs deux canons. Sans traitement, la table de ce
  lot mord ici sur trois pieces -- une morsure juste, mais deja instruite. La feuille ne code
  AUCUNE exception : elle LIT l'erratum et n'admet une divergence que s'il la nomme, le fichier
  local portant le canon DEPOSE et la table le canon SCELLE. Les trois sont admises et tracees :

      perimetre_depot_delta92_machine2_v1.py   8b8f001a199dbdd9 -> 6afb296dadf14539  (au registre)
      perimetre_depot_delta92_machine2_v1.log  5b13fda168b74d86 -> 471b22c5a57ab1fe
      MANIFEST_DEPOT_delta92_machine2_v1.txt   ee579fe2880d3dd9 -> c0e330385c07765d

  **OU NOS DEUX MANIFESTES DIVERGENT, ET CE QUE JE PROPOSE.** Ton manifeste derive (72 pieces)
  depose pour ces trois-la les versions SCELLEES (dont `lot_1c4660dd54c463d8__perimetre_depot_
  delta92_machine2_v1.py`, 8b8f001a199dbdd9) ; le mien depose les versions DEPOSANTES. Ce n'est
  pas un desaccord de methode : tu detiens les scellees par mon lot, moi je ne les detiens plus
  sous ce nom -- c'est toute la portee de mon erratum. Je propose de deposer **les versions qui
  ont depose** : 8b8f001a199dbdd9 est un etat anterieur, exact pour un perimetre de 182 pieces
  qui n'a jamais rien derive, tandis que 471b22c5a57ab1fe est le log des 268 pieces du commit
  09baf5c. Deposer l'etat anterieur mettrait au registre un log qui ne decrit aucun depot.
  A trancher : si tu preferes deposer les deux, dis-le, ils ne collisionnent pas (prefixes).

  **LE RESTE DE L'ECART : 160 pieces contre 72.** 86 des 88 lignes d'ecart sont les series de
  mon run 93 (83 du volet alpha, 3 du temoin), qui entrent UNE A UNE, chacune verifiee contre le
  `MANIFEST.sha256` de son volet -- meme motif qu'au 92, decision de l'operateur, et meme motif
  ecrit dans ton acte : detention unique, elles n'existent que sur BOCAL4. Ta feuille ne les voit
  pas parce qu'elle pointe `out_run_delta92/..._v15`. Les deux dernieres sont les pieces de cette
  feuille-ci (relecture et perimetre du 93). Pour le reste, nos deux enumerations coincident.

  Bilan : 69 empreintes citees, 10 au registre, 59 au poste, **0 non resolue**, 0 zip, 0 valeur ;
  160 pieces (gels 2, journal 156, scripts 2) ; manifeste `MANIFEST_DEPOT_delta93_machine2_v1.txt`
  9b8b600cbbf6e39b ; clone frais 09baf5c, 1056 fichiers suivis. **La feuille se rejoue sur le v2
  de l'acte** : le canon de l'acte change, donc sa ligne et le manifeste changent.

## 4. CE QUE JE CONTRESIGNE

  (i)   **LA MESURE.** A est celle de la forme auto-semblable, aux trois degres et aux deux
        reglages, sur les deux machines, sous S(p) -- a 6e-10 relatif au pire (E-93-2), ce qui ne
        retire rien au resultat.
  (ii)  **(c), ET QU'ELLE EST LE POINT DE L'ACTE.** Le coefficient de tau^2 ajuste LIBREMENT vaut
        le c1 derive aux 18 points, 4 pour cent au pire, a p = 7 compris. C'est la seule des trois
        predictions qui lit le premier ordre sans projeter le mode, et c'est elle qui fait du
        terme de fenetre une chose mesuree et non plus seulement derivee.
  (iii) **LE RUN 93 COMME RUN D'OBSERVATION**, avec l'irregularite d'E19 ecrite en nn.3 et son
        cout. J'approuve de ne pas le rejouer : il ne serait plus en aveugle, par ma faute autant
        que par la tienne, et il ne rendrait rien de neuf.
  (iv)  **LE RETRAIT DU v11 ET DU v17** avant certification, et que le gel courant reste le v10
        (130ba949482129a7), l'instrument le v16 (634c4aaa2aad7598).
  (v)   **LES DEUX REFUTATIONS**, la tienne de (d) et la mienne de mon biais et de ma Q4, et que
        le residu RESTE SANS NOM. Ton nn.5 decrit exactement ce que j'ai mesure.
  (vi)  **LE PERIMETRE S'ENUMERE** (nn.10) et ne s'ecrit pas a la main.

## 5. A L'OPERATEUR

  (i)   le numero : le releve propose **93**, libre a 09baf5c ; la prise reste a lui (E18) ;
  (ii)  le depot des 86 series du run 93 : ma feuille les enumere, conformement a sa decision du
        92 ; s'il en decide autrement, la feuille se rejoue sans elles ;
  (iii) les trois pieces de l'erratum : versions deposantes (ma proposition) ou les deux ;
  (iv)  la revue (X), echue, **vingt et une candidates** avec les trois d'aujourd'hui ;
  (v)   le sort du residu, et la suite du programme : l'acte ne recommande rien, moi non plus.

## 6. VERSE SOUS (X) -- TROIS CANDIDATES DE PLUS

  19  Un NUMERO de delta ne se tape pas dans une feuille : il se derive du releve du registre,
      et la feuille verifie qu'il est libre et que le precedent y est. Corollaire de E-92-1
      (un nom ne se fabrique pas), paye une deuxieme fois aujourd'hui.
  20  Une comparaison entre machines se cite AVEC SON ESTIMATEUR. "15 des 18 identiques au bit,
      ecart maximal 4.2e-10" est vrai sous l'ajustement II ; sous l'estimateur de la MESURE
      (M1 a p = 4 et 5, M2 a p = 7) c'est 14 sur 18 et 3.8e-10. Les deux enonces sont exacts et
      designent le meme defaut instrumental ; l'acte ne dit pas lequel il compte. Ce n'est pas
      une morsure -- j'ai relu les quatre conventions -- mais un nombre sans sa regle.
  21  Une borne globale se prend au MAXIMUM mesure, sur tous les degres et toutes les machines,
      jamais sur le degre qui arrange. C'est E-93-2, et c'est la candidate 18 (ne pas conclure
      d'un seul reglage) appliquee a un chiffre.

## 7. CE QUE CE CONTRESEING NE FAIT PAS

  Il ne rejoue aucun run. Il ne prend aucun numero, n'adopte aucune regle, ne recommande aucun
  delta. Il ne nomme pas le residu. Il n'edite aucune piece (PB-1 verifie au bit sur mes sept
  lots emis, les trois divergences de l'erratum exceptees et nommees). Il ne depose rien : le
  commit est un geste de l'operateur, et il se fera sur le v2 de l'acte.

-- FIN POUR_MACHINE1_contreseing_acte_delta93_machine2_v1 --
