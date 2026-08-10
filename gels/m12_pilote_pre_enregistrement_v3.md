PRE-ENREGISTREMENT M12-PILOTE -- CALIBRATION DU MOTEUR, DIAGNOSTIC DE
RESOLUTION, ET MESURE DU TAUX D'ATTRITION SOUS LA GEOMETRIE NEUVE
(gele avant l'ecriture de toute ligne de code ; bloc ASCII, canonique NFC+LF ;
nom de fichier versionne, regle E19-2 -- version v3)

HISTORIQUE DU GEL
  v1 3bddd5a4 : NON CERTIFIE (certification croisee machine 2 v1, empreinte
      7225c2ca, deposee le 01/08 -- la date du 27/07 portee par l'historique
      v2 venait de l'en-tete du message v1 de machine 2, reprise de bonne
      foi ; corrigee ici, cert. v2).
  v2 38656ce7 : NON CERTIFIE (certification croisee machine 2 v2, empreinte
      4aa88115, 01/08). Les corrections de v1 portant sur ce bloc (S2, S3,
      S4, S5b) sont integrees et CONTRESIGNEES -- points, dimensionnement,
      programme fige inchanges par la cert. v2. Les demandes nouvelles qui
      touchent ce bloc sont la geometrie (arrondis non conformes au code
      certifie de la lignee, controle de coherence vide) et la notation
      d'echelle.
  v3. Integre S7 (arrondis NOMMES, alignes sur balayer() : CEIL au grossier,
      ROUND au fin ; controles de coherence qui MORDENT en remplacement du
      controle n = 201, vide) et S8 (notation unique s*, mention de
      non-circularite du gel M11 v4). Reprend la regle ELARGIE de la cert. v2
      (inegalites evaluees sur leur bord) dans le diagnostic S2, et corrige
      le renvoi au rang 9, devenu symptome. Subordination portee au gel M12
      v3. AUCUNE attente reecrite : la section MES ATTENTES est copiee de v1
      a l'identique, pour la troisieme fois.
  AUCUN code avant qu'un message de certification croisee cite l'empreinte de
  ce bloc (E19-1). Le script s'appellera m12_pilote_v1.py.
  C2 NE S'APPLIQUE PAS : integralement CLASSIQUE, aucune diagonalisation.
  CE BLOC EST SUBORDONNE au gel M12 (m12_pre_enregistrement_v3.md), qui doit
  etre certifie AVANT lui. Motif : le pilote alimente la regle D-N du gel M12,
  et une regle alimentee ne peut pas etre ecrite apres son intrant.

OBJET, ET CE QU'IL N'EST PAS
----------------------------
Le pilote NE TESTE RIEN. Il n'a aucune porte a verdict, il ne forme JAMAIS la
combinaison E = ln s*_4 - 2.25 ln s*_5 + 1.25 ln s*_7, et il ne prononce rien
sur la classe. Il rend trois choses et trois seulement :
  (1) CALIBRATION : le moteur reproduit-il les valeurs certifiees de M10 et
      M11 aux points communs ?
  (2) RESOLUTION : la geometrie neuve declenche-t-elle G6 la ou l'ancienne ne
      declenchait pas ? C'est le diagnostic que E27 exige et que le S43.5
      avait chiffre comme rattrapable.
  (3) ATTRITION : le taux de perte par LIGNE sous cette geometrie, qui fixe N
      par la regle D-N du gel M12.

SES QUATRE POINTS SONT BRULES, DEFINITIVEMENT
---------------------------------------------
  w2 = 1.70, 2.15, 2.45, 2.75
Ils sont DEJA MESURES aux trois degres (M10 pour p=5 et p=7 ; M11 pour p=4) et
appartiennent au fit survivant de M11. Ils ne peuvent donc rien tester : leur
valeur est connue des deux machines. C'est PRECISEMENT pourquoi ils servent ici
et pourquoi ils sont interdits a M12 :
  AUCUN de ces quatre points ne pourra jamais entrer dans l'ensemble de test de
  M12, ni dans aucune manche ulterieure testant la classe, quel que soit le
  resultat du pilote. La liste de priorite du gel M12 ne les contient pas, par
  construction (contrainte de nouveaute >= 0.03 de la grille M10/M11).
  NOTE v2 : 2.85, retenu par v1, n'est PAS brule par le pilote ; il reste
  neanmoins hors de M12 par la meme contrainte de nouveaute (point de grille).

DERIVATION DU CHOIX DES QUATRE POINTS (regle INCHANGEE de v1 ; resultat
CORRIGE -- correction S2, avec diagnostic)
  Ensemble source : le fit survivant de M11, seul ensemble mesure aux trois
  degres apres repercussion de G7 -- {1.70, 2.15, 2.30, 2.45, 2.60, 2.75, 2.85}.
  Regle : le sous-ensemble de CARDINAL 4 qui maximise l'espacement minimal ;
  egalite -> somme la plus petite.
  RE-DERIVATION EN ARITHMETIQUE EXACTE (les valeurs sont des centiemes
  exacts) : l'espacement minimal maximal vaut 3/10, et DEUX sous-ensembles
  l'atteignent --
      {1.70, 2.15, 2.45, 2.75}   somme 181/20 = 9.05   <-- designe
      {1.70, 2.15, 2.45, 2.85}   somme 183/20 = 9.15
  RESULTAT : {1.70, 2.15, 2.45, 2.75}, espacement minimal 0.30.
  DIAGNOSTIC DU DEFAUT DE v1, verifie sur le code rejoue : en IEEE754 les deux
  espacements minimaux ne sont PAS egaux --
      min-gap({...,2.85}) = 0.30000000000000027   (liant : 2.45 - 2.15)
      min-gap({...,2.75}) = 0.2999999999999998    (liant : 2.75 - 2.45)
  ecart 4.4e-16 : l'egalite n'a JAMAIS eu lieu, donc le departage "somme la
  plus petite" n'a JAMAIS ete exerce -- le premier critere, compare en
  flottant sans tolerance, a designe seul {..., 2.85}. Ni regle ecrite a
  l'envers, ni resultat choisi puis habille : une egalite masquee. Mais la
  mecanicite ANNONCEE par v1 etait fausse au sens qui compte -- le departage
  ecrit n'a jamais tourne.
  MEME CLASSE que la regle 11 (comparer PAR VALEUR a tolerance declaree tres
  inferieure a l'espacement) et que le fil du rayon a 1.88 (marge 1.10 de
  R-2'). REGLE APPLIQUEE ICI, gelee pour cette manche, sous sa forme ELARGIE
  par la certification v2 : TOUTE comparaison dont le resultat peut basculer
  sous une perturbation de l'ordre de l'epsilon machine -- egalite, ou
  inegalite evaluee sur son bord -- s'evalue en arithmetique EXACTE quand les
  entrees sont exactes, a tolerance declaree sinon. La meme classe a ete
  trouvee EN AMONT par la certification v2 -- le filtre de nouveaute de la
  grille M12, treize candidats sur le fil -- et est reglee au gel M12 v3 ;
  l'egalite du rang 9 que la v2 de ce bloc citait s'est revelee un ARTEFACT
  de la lecture flottante (symptome du meme defaut, pas un fait independant).
  (Promotion en regle transversale ou en erratum : decision hors de ce bloc,
  E18 -- rien n'est reserve ici.)
  Cardinal 4 et non 3 : voir DIMENSIONNEMENT. Le nombre est DERIVE, pas
  choisi -- une proposition manuelle a trois points a ete ecartee par ce
  calcul, et le fait est consigne ici pour qu'il soit opposable.

DIMENSIONNEMENT DU PILOTE (fait avant toute mesure)
  Un pilote a k points rend L = 3k lignes. Sans perte observee, la borne
  superieure unilaterale a 80 % du taux de perte par ligne vaut
      q_L = 1 - 0.20^(1/L)
  La survie d'un point de M12 vaut (1 - q_L)^3 (trois degres, G7 repercute), et
  N est le plus petit entier tel que P(>= 4 survivants) >= 0.90 (loi binomiale).
  Cout total = 5N + 5k recherches.
      k=2 : q_L 0.2353  N=13  total 75
      k=3 : q_L 0.1637  N=10  total 65
      k=4 : q_L 0.1255  N= 8  total 60   <-- MINIMUM
      k=5 : q_L 0.1017  N= 7  total 60
      k=6 : q_L 0.0855  N= 7  total 65
  k = 4 est retenu comme plus petit argmin. Ce tableau est gele ; il ne sera
  pas recalcule avec d'autres bornes apres la mesure.
  NOTE (cert. v2) : le cout REEL des deux manches est 5N + 5k + 15, les
  constantes de garde (10 en M12, 5 au pilote) etant independantes de k et de
  N : l'argmin est INCHANGE, verifie par machine 2.

GEOMETRIE DE BALAYAGE (alignee sur le code certifie de la lignee -- cert. v2,
corrections S7 et S8)
-----------------------------------------------------------------------------
  Le bracket mesure s* D'ABORD (pas final <= 1e-5, G5) ; le double balayage
  est un DIAGNOSTIC posterieur, bati sur le s* mesure. s* est donc connu des
  la recherche : AUCUNE circularite (mention reprise du gel M11 v4). Une
  seule echelle, une seule notation : s*, celle des comptages de G6 et C-P3.
  LES PAS SONT GELES EN PLAFOND, n EST UNE SORTIE, L'ARRONDI EST NOMME --
  aligne sur balayer() (m11_exposant_v3.py, 80cfa795, lignes 1038-1050,
  telles que citees et verifiees par la certification v2 ; relecture directe
  du fichier a la certification du script) :
    grossier : [LO0, 0.90 s*], LO0 = 0.05 ;
               n_g = 1 + ceil( (0.90 - LO0/s*) / 0.005 )     ARRONDI : CEIL
               linspace couvre la fenetre, la borne haute est ATTEINTE, et le
               pas effectif est <= 0.005 s* : le pas gele est un PLAFOND.
               n_g <= 181 (verifie pour tout s* > LO0) ; valeur par ligne
               CONSIGNEE (C-P1).
    fin      : [0.90 s*, 1.05 s*] ;
               n_f = 1 + round( (1.05 - 0.90) / 0.002 ) = 76 ARRONDI : ROUND
               Quotient exact : 75 (rationnels). Evaluation IEEE :
               75.000000000000014. Sous ROUND -- l'arrondi de la lignee --
               les deux concordent (n_f = 76) ; sous CEIL ils divergeraient
               (76 contre 77). C'est pourquoi l'arrondi est NOMME (regle 13),
               et pourquoi n_f est gele sous sa forme derivee et non comme un
               nombre nu.
    pas relatif EFFECTIF consigne par ligne : pas / s* (C-P1).
  CONTROLES DE COHERENCE QUI MORDENT (correction S7 ; ils remplacent le
  controle "n = 201", VIDE : son quotient vaut 200 exactement, identique sous
  ceil, floor et round -- quatrieme controle vide de la campagne, cert. v2).
  Vecteurs arithmetiques SYNTHETIQUES, sans provenance physique, LO0 = 0.05 :
    s_ctl = 0.47 : quotient 7460/47 = 158.7234... -> floor 158, round 159,
            ceil 159 ; n_g ATTENDU = 160   [discrimine ceil/round de floor]
    s_ctl = 2.05 : quotient 7180/41 = 175.1219... -> floor 175, round 175,
            ceil 176 ; n_g ATTENDU = 177   [discrimine ceil de floor/round]
    fenetre fine : n_f ATTENDU = 76 sous ROUND (77 sous un ceil flottant)
  Les deux vecteurs n_g pincent CEIL a eux deux ; le vecteur n_f pince ROUND.
  Le --selftest verifie les trois valeurs attendues ; un ecart est BLOQUANT.
  CONSEQUENCE ECRITE D'AVANCE : les taux d'attrition du pilote NE SE COMPARENT
  PAS aux taux de M10 et M11. MEME LA OU LA GEOMETRIE COINCIDE avec M11 v4
  (grossier identique -- memes bornes, meme pas plafond, meme arrondi ; fin au
  meme pas et meme arrondi, seule la borne haute est reduite de 1.30 s* a
  1.05 s*), aucune comparaison n'est declaree ni permise ici : une declaration
  de comparabilite instrument par instrument serait necessaire, et elle n'est
  PAS faite. C'est E27, et le pilote ne le refera pas. Le pilote MESURE un
  taux sous SA geometrie ; il ne le rapporte a aucun autre.

CONSIGNATIONS (aucune porte ; toutes obligatoires au JSON)
----------------------------------------------------------
  C-P1  s*(w2, p, signe) aux 4 points x 3 degres, avec pour CHACUN :
        le pas final de la recherche, les bornes des deux balayages, les n
        OBTENUS (n_g, n_f -- n est une SORTIE : consigne, jamais fixe), et le
        PAS RELATIF effectif pas/s*.
        C'est le correctif structurel d'E27 : la resolution voyage DANS la
        donnee, a cote de la consignation, jamais dans une clause en prose.
  C-P2  ecart relatif aux valeurs certifiees, par point, par degre, par signe.
        Sources : m10_results.json (7cf3624b) pour p=5 et p=7 ;
                  m11_results.json (ad275870) pour p=4.
  C-P3  G6 : declenchement ou non, nombre d'ilots par ligne, position de la
        premiere retombee, et min(s explosif)/s* SUR CHAQUE LIGNE -- y compris
        les lignes non exclues. C'est la consignation que le script M11 n'a pas
        produite (S42.3) ; elle est ici obligatoire et verifiee par G9.
        DOMAINE DECLARE (correction S5b) : ilots et retombees sont comptes
        dans [s*, 1.05 s*] ; ils ne se comparent PAS aux comptes de M10/M11,
        obtenus dans [s*, 1.30 s*] -- meme statut que les taux d'attrition.
        NULL MOTIVE (correction S4) : une ligne sans retombee dans la fenetre
        porte le champ avec la valeur null ET le champ jumeau de motif -- ce
        n'est pas un defaut de consignation, c'est le fait mesure.
  C-P4  duree machine par recherche, pour chiffrer M12.
  C-P5  q_L observe = (lignes perdues) / 12, et la borne superieure
        unilaterale a 80 % correspondante (Clopper-Pearson).

GARDES
------
  G1 CALIBRATION (bloquante) : |s*_pilote / s*_certifie - 1| <= 2 % PAR SIGNE,
     aux 12 lignes disposant d'une valeur certifiee. Echec -> ARRET, aucune
     transmission a M12, investigation.
     [derivation de la tolerance : c'est celle de G1 en M10, inchangee. La
      geometrie de balayage differe, donc une concordance exacte n'est PAS
      attendue ; 2 % est la tolerance sous laquelle la campagne a deja
      travaille, et elle est reprise sans etre relachee.]
  G3 IDENTITE DE FORCE : erreur backward <= 1e-12 apres CHAQUE rebinding.
  G4 PAS DE TEMPS : dt/2 sur la ligne maximisant g s*^(p-1) ; ecart <= 2 %.
  G5 QUALITE DE BRACKET : pas final <= 1e-5, consigne par recherche.
  G6 PRIMAUTE DE s* : aucune explosion sous 0.98 s*. Une ligne qui declenche
     est CONSIGNEE, et elle compte dans q_L. Elle n'est pas "reparee".
  G8a/G8b PARITE a p=4 : sP - sM == 0 exactement sur les 4 lignes.
     [motif : la demonstration de M11 est acquise au bit ; ce controle est une
      REGRESSION, pas une decouverte. S'il echoue, la lignee de code a change
      et tout le reste est suspect.]
  G9 COUVERTURE (correction S4) : le --selftest extrait de ce bloc la liste
     des consignations nommees C-P1 a C-P5 et verifie, pour chacune et sur
     chaque ligne concernee, que le CHAMP EXISTE au JSON. Une valeur null
     n'est admise que si un champ jumeau <nom>_motif, NON VIDE, consigne sur
     la meme ligne le fait mesure qui la justifie. Champ absent, ou null sans
     motif -> ECHEC BLOQUANT avant le run. Un null nu est un defaut de
     consignation ; un null motive est une donnee.
     L'extraction est ancree sur la STRUCTURE (regle 12) et testee contre le
     leurre REEL que ce bloc contient : la sous-chaine "MES ATTENTES" y
     figure hors en-tete de section.

PROGRAMME FIGE
--------------
  p=4 : 4 points x 1 signe = 4   [parite acquise au bit, M11]
  p=5 : 4 points x 2 signes = 8
  p=7 : 4 points x 2 signes = 8
  G8a/G8b a p=4 : 4 lignes supplementaires au signe oppose = 4
  G4 : 1
  TOTAL 25 recherches, dont 20 productives.
  INVARIANT DE COMPTAGE, forme derivee (lecon "compter, jamais affirmer") :
      recherches_comptees + recherches_sautees == 25
  Les gardes ont le droit de retrancher ; l'egalite porte sur la somme.

CE QUE LE PILOTE TRANSMET A M12, ET RIEN D'AUTRE
  UN SEUL NOMBRE : q_L majore a 80 %, qui entre dans la regle D-N.
  Plus deux faits binaires : G1 passe ou non ; G6 a declenche ou non, et ou.
  AUCUNE valeur de s* du pilote n'entre dans une lecture de M12. AUCUNE
  combinaison E n'est formee ici, ni consignee, ni calculable a partir du JSON
  publie sans refaire le travail -- et si elle l'etait, elle porterait sur des
  points brules, donc sans statut.

MES ATTENTES (ecrites une fois, jamais reecrites)
  G1 passe aux 12 lignes, avec des ecarts de 0.2 a 2 % -- pas mieux : la
  geometrie de balayage a change et le seuil est un objet a resolution finie.
  G6 declenche sur 0 ou 1 ligne des 12. Si c'est 2 ou plus, le taux d'attrition
  reel est bien pire que ce que M11 laissait croire et M12 coute plus cher que
  60 recherches.
  Je n'ai AUCUNE attente sur le sens de l'ecart de G1 (au-dessus ou en dessous
  des valeurs certifiees) : le pas fin est ~3 fois plus serre, donc le seuil
  devrait etre trouve LEGEREMENT PLUS BAS, mais je ne sais pas de combien et je
  ne veux pas d'un chiffre que je pourrais defendre apres coup.

LIMITATIONS DECLAREES
  - Quatre points ne mesurent pas un taux, ils le bornent. C'est pourquoi D-N
    utilise une BORNE SUPERIEURE et non une estimation ponctuelle.
  - q_L est suppose homogene en w2 et en p. Il ne l'est pas : M11 a montre le
    bord gauche plus crible. La borne a 80 % absorbe une partie de cet ecart,
    pas sa totalite. Consequence assumee : N peut etre sous-dimensionne si les
    points de M12 tombent dans une region plus hostile que les quatre du pilote.
  - Le pilote ne certifie pas le moteur "en general" : il le certifie sur
    quatre points, aux trois degres, dans une plage de w2 de 1.70 a 2.75.

IMPLEMENTATION
  m12_pilote_v1.py, moteur classique repris de m9_replication_v1.py (c8ed357b)
  SANS MODIFICATION ; la geometrie de balayage est la reprise de la forme du
  delta 39.3 telle que portee par le gel M11 v4 et par balayer()
  (m11_exposant_v3.py, 80cfa795) -- arrondis CEIL et ROUND compris, seule la
  borne haute de la fenetre fine est reduite a 1.05 s* --, isolee dans une
  fonction unique testee par --selftest, relue contre le fichier
  m11_exposant_v3.py a la certification du script.
  Ecrit uniquement out/m12_pilote_results.json (incremental, une ecriture
  apres chaque ligne). Gel jumeau dans le docstring, du marqueur
  "PRE-ENREGISTREMENT M12-PILOTE" au terminateur inclus, sha256 recalcule au
  demarrage depuis le fichier source, convention d'empreinte B (bloc =
  fichier, saut de ligne final inclus). Pre-vol a moteur factice OBLIGATOIRE
  avant le run reel. DEPOT DU SCRIPT CONDITIONNE a la certification croisee.

=== FIN DU GEL M12-PILOTE ===
