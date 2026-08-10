"""PRE-ENREGISTREMENT M12-PILOTE -- CALIBRATION DU MOTEUR, DIAGNOSTIC DE
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
"""
# =====================================================================
# m12_pilote_v1.py -- CALIBRATION, RESOLUTION, ATTRITION (25 recherches)
# ---------------------------------------------------------------------
# Le gel jumeau (docstring ci-dessus) est le bloc CERTIFIE
# m12_pilote_pre_enregistrement_v3.md ; son empreinte est recalculee au
# demarrage (convention B, saut final inclus) et confrontee a SHA_GEL.
# Moteur : m9_replication_v1.py, repris SANS MODIFICATION, charge par
# empreinte (SHA_MOTEUR) -- patron de m11_exposant_v3.py (80cfa795...).
# Geometrie : balayer() reprise VERBATIM de m11_exposant_v3.py:1038-1072 ;
# la SEULE difference est la constante module G6_HAUT = 1.05 (gel v3).
# Obligations de la certification v3 (section 5) et du delta 44 :
#   (1) le --selftest declare la portee REELLE de chaque vecteur ;
#   (2) garde de domaine STRICTE s* > LO0/0.90 = 1/18, avec ARRET et
#       consignation, doublee de la ceinture n_gros >= 2 ;
#   (3) test NEGATIF du filtre de nouveaute sur 2.27 exact, qui MORD ;
#   (4) pre-vol a moteur factice obligatoire avant tout run reel
#       (--prevol : sorties vers un fichier SEPARE, jamais FOUT) ;
#   (5) le pre-vol n'est OPPOSABLE que joue par la machine qui detient les
#       sources certifiees ; execute sur sources synthetiques, c'est une
#       REPETITION (cert. du script, section 1 -- cinquieme controle vide).
# HISTORIQUE DU SCRIPT :
#   v1 cccc8a7b... NON CERTIFIE (cert. script v1, 6acb1fe9...) -> S2 G1
#      COMPTE ; S3 G4 HORS q_L + ventilation ; S4 bord 0.98 s* observable ;
#      S5 empreinte m11 complete.
#   v2 9d88798a... NON CERTIFIE (cert. script v2, a7ef9362...) -> S6 le
#      temoin du bord calcule l'EXPRESSION DE LA GARDE (ecart ABSOLU +
#      predicat ; le relatif reste, lecture humaine) ; S7 date timezone-aware
#      RESTAUREE -- la regression venait d'une edition du fichier ASSEMBLE et
#      non du corps source ; toute edition passe desormais par le corps, et
#      l'assembleur refuse utcnow par assertion.
#   GEL JUMEAU INCHANGE dans toutes les versions (03e29c86...).
# =====================================================================

import argparse, hashlib, importlib.util, json, math, os, re, sys, time, unicodedata
from fractions import Fraction
from types import SimpleNamespace

import numpy as np

MARQ_DEBUT = "PRE-" + "ENREGISTREMENT M12-PILOTE"
MARQ_FIN = "=== FIN DU GEL M12-PILOTE " + "==="

# ---- empreintes gelees -----------------------------------------------
SHA_GEL = "03e29c861197147e896ccdd928cea2d98eb7c4979f82d83d28ade7f8cb82f09a"
SHA_MOTEUR = "c8ed357b120352c4d1078307add3eaac285940c8bec00acc2ddc9ff386ab2c5c"
# releve de m11_exposant_v3.py:725 (fichier verifie 80cfa795...) :
SHA_M10_JSON = "7cf3624b45dd7d2bb91d29485bd14599e749bd60ba683c4b0c0b224a28aba3bc"
# confirmee OPPOSABLE par la certification du script v1 (S5) :
SHA_M11_JSON = "ad275870847d440ecfb04e7b7108c24748d1a1126eb223c6b3db9a1c9038d124"
SHA_M11_SCRIPT = "80cfa79582d5128d843afac254b32f9d985b0cf062b82fe20c4894bf23c98b97"

# ---- protocole (gel v3) ----------------------------------------------
POINTS = [1.70, 2.15, 2.45, 2.75]
DEGRES = (7, 5, 4)                       # ordre d'execution ; p=4 en dernier (G8)
LO0 = 0.05                               # verifie contre m9.LO0 au chargement
TOL_APPART = 1e-09                       # regle 11
TOL_G1, TOL_G4 = 0.02, 0.02
PAS_GARANTI_G5 = 1.0e-05
EPS_PORTE = 1e-12
G6_PAS_GROS, G6_PAS_FIN = 0.005, 0.002
G6_BAS, G6_MID = 0.90, 0.90
G6_HAUT = 1.05                           # SEULE difference avec la lignee (1.30)
G6_SEUIL_EXCL = 0.98
N_MAX_LIGNE = 400
# vecteur gele (cert. script v2, S6) : a cet s*, le temoin RELATIF de v2
# contredit le predicat de la garde a l'indice 40 -- la classe GRAVE (abs = 0
# exactement, rel < 0) reste exhibee a jamais par le selftest [10].
S_TEMOIN_DIVERGENT = 0.4179

# ---- programme fige, forme derivee -----------------------------------
RECH_MESURES_57 = len(POINTS) * 2 * 2    # p=5 et p=7, deux signes        = 16
RECH_MESURES_4 = len(POINTS)             # p=4, signe +1 (parite)         =  4
RECH_G8 = len(POINTS)                    # p=4, signe -1, REGRESSION      =  4
RECH_G4 = 1
RECH_ATTENDUES = RECH_MESURES_57 + RECH_MESURES_4 + RECH_G8 + RECH_G4    # 25
assert RECH_ATTENDUES == 25, "programme fige : 25 recherches (gel v3)"
LIGNES = [(p, w) for p in DEGRES for w in POINTS]                        # 12
BAL_ATTENDUS = len(LIGNES) * 2                                           # 24
CPT = {"recherches": 0, "balayages": 0, "sautees": 0, "balayages_sautes": 0}
FOUT = os.path.join("out", "m12_pilote_results.json")
FOUT_PREVOL = os.path.join("out", "m12_pilote_PREVOL.json")

canon = lambda t: unicodedata.normalize("NFC", t).replace("\r\n", "\n").replace("\r", "\n")
cle = lambda p, w: ("%d|" + "%.12f") % (p, w)


# =====================================================================
# 1. GEL JUMEAU -- invariant de cloture puis empreinte (convention B)
#    Patron repris de m11_exposant_v3.py (80cfa795...), lignes 800-837.
# =====================================================================

def invariant_cloture(txt):
    n = txt.count(MARQ_FIN)
    if n != 1:
        return False, "le terminateur apparait %d fois (exige : 1)" % n
    i = txt.index(MARQ_FIN)
    if i == 0 or txt[i - 1] != "\n":
        return False, "le terminateur n'est pas en debut de ligne"
    if txt[i + len(MARQ_FIN):].strip():
        return False, "du texte significatif suit le terminateur"
    return True, "unique, en ligne pleine, en cloture"


def bloc_du_gel(txt):
    """CONVENTION B : du titre au terminateur, SAUT FINAL INCLUS."""
    i = txt.index(MARQ_FIN) + len(MARQ_FIN)
    return txt[txt.index(MARQ_DEBUT): i + 1]


def certifier_gel(verbeux=True):
    src = canon(open(os.path.abspath(__file__), encoding="utf-8").read())
    ok, motif = invariant_cloture(canon(__doc__))
    if not ok:
        sys.exit("ARRET invariant de cloture (gel jumeau) : %s" % motif)
    if src.count(MARQ_FIN) != 1:
        sys.exit("ARRET invariant de cloture (source) : terminateur x%d"
                 % src.count(MARQ_FIN))
    bloc = bloc_du_gel(src)
    h = hashlib.sha256(bloc.encode()).hexdigest()
    if verbeux:
        print("Gel jumeau : %d lignes, %s" % (bloc.count("\n"), motif))
        print("  sha256 (convention B) : %s" % h)
        print("  sha256 certifie v3    : %s -> %s"
              % (SHA_GEL, "CONCORDANT" if h == SHA_GEL else "DISCORDANT"))
    if h != SHA_GEL:
        sys.exit("ARRET E19 : le gel jumeau ne correspond pas a la version certifiee.")
    return bloc, h


# =====================================================================
# 2. SOURCES PRIMAIRES ET MOTEUR
# =====================================================================

def _sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


def _verifie(chemin, sha, quoi):
    if not os.path.exists(chemin):
        sys.exit("ARRET : source absente : %s (%s)" % (chemin, quoi))
    h = _sha(chemin)
    if h != sha:
        sys.exit("ARRET : %s -- empreinte %s, exigee %s" % (chemin, h, sha))
    return open(chemin, encoding="utf-8").read()


def charger_sources(prevol, rep_prevol):
    """Cartes certifiees : m10 (p=5,7) et m11 (p=4). En mode REEL les
    empreintes COMPLETES sont exigees, m10 et m11 (S5, cert. script v1).
    En PREVOL, les sources reelles sont
    utilisees si presentes et conformes ; sinon des sources SYNTHETIQUES
    (chemin --sources-prevol) avec banniere -- chemins seulement, jamais
    la voie du run reel."""
    m10p = os.path.join("out", "m10_results.json")
    m11p = os.path.join("out", "m11_results.json")
    meta = {}

    def reelles(strict):
        if not (os.path.exists(m10p) and os.path.exists(m11p)):
            if strict:
                sys.exit("ARRET : sources certifiees absentes (%s, %s)" % (m10p, m11p))
            return None
        h10 = _sha(m10p)
        if h10 != SHA_M10_JSON:
            if strict:
                sys.exit("ARRET : %s -- empreinte %s, exigee %s" % (m10p, h10, SHA_M10_JSON))
            return None
        h11 = _sha(m11p)
        if h11 != SHA_M11_JSON:
            if strict:
                sys.exit("ARRET : %s -- empreinte %s, exigee %s"
                         % (m11p, h11, SHA_M11_JSON))
            return None
        meta.update({"statut": "REELLES", "m10_sha256": h10, "m11_sha256": h11})
        c10 = json.load(open(m10p, encoding="utf-8"))["resultats"]["carte"]
        c11 = json.load(open(m11p, encoding="utf-8"))["resultats"]["carte"]
        return c10, c11

    if not prevol:
        return reelles(strict=True) + (meta,)
    r = reelles(strict=False)
    if r is not None:
        print("PREVOL : sources REELLES presentes et conformes -- utilisees.")
        return r + (meta,)
    p10 = os.path.join(rep_prevol, "m10_results.json")
    p11 = os.path.join(rep_prevol, "m11_results.json")
    if not (os.path.exists(p10) and os.path.exists(p11)):
        sys.exit("ARRET PREVOL : ni sources reelles conformes, ni sources "
                 "synthetiques dans %s" % rep_prevol)
    print("=" * 70)
    print("PREVOL : SOURCES SYNTHETIQUES (%s) -- empreintes HORS REGISTRE," % rep_prevol)
    print("valides pour le pre-vol SEULEMENT ; le run reel les refusera.")
    print("=" * 70)
    print("Le pre-vol OPPOSABLE est celui de la machine qui detient les")
    print("sources certifiees ; ceci est une REPETITION (cert. script, S1).")
    meta.update({"statut": "SYNTHETIQUES_PREVOL",
                 "m10_sha256": _sha(p10), "m11_sha256": _sha(p11)})
    c10 = json.load(open(p10, encoding="utf-8"))["resultats"]["carte"]
    c11 = json.load(open(p11, encoding="utf-8"))["resultats"]["carte"]
    degen = sorted(k for k, r in c10.items() if r["sP"]["s"] == r["sM"]["s"])
    meta["degenere_p_impair"] = degen
    if degen:
        print("ATTENTION MONTAGE DEGENERE (parade b) : sP == sM sur %s --"
              " aucune asymetrie de signe a p impair, une confusion"
              " signe/minimum serait INVISIBLE ici." % degen)
    return c10, c11, meta


def charger_moteur(chemin="m9_replication_v1.py", factice=None, verbeux=True):
    """Patron de m11_exposant_v3.py:983-1004 : empreinte exigee, globales
    verifiees, comptage EXHAUSTIF par enveloppe. `factice` substitue
    chercher_seuil et integrer (pre-vol) APRES ces verifications : la
    chaine de custody du moteur est identique dans les deux modes."""
    h = _sha(chemin)
    if verbeux:
        print("Moteur %s -> %s" % (h[:24] + "...",
                                   "CONCORDANT" if h == SHA_MOTEUR else "DISCORDANT"))
    if h != SHA_MOTEUR:
        sys.exit("ARRET : le moteur n'est pas celui que le gel designe.")
    spec = importlib.util.spec_from_file_location("m9_moteur", chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for nom, att in (("W1", 1.0), ("G_REF", 0.05), ("DT", 0.006), ("T_MAX", 400.0),
                     ("CAP", 1.0e4), ("NDENSE", 96), ("LO0", 0.05), ("HI0", 6.0),
                     ("MAX_ELARG", 8), ("NGRID", 48), ("NPASSES", 3)):
        if abs(float(getattr(mod, nom)) - float(att)) > 1e-12:
            sys.exit("ARRET : globale %s = %r, le gel exige %r"
                     % (nom, getattr(mod, nom), att))
    if abs(mod.LO0 - LO0) > 0:
        sys.exit("ARRET : LO0 du moteur differe de la constante du script.")
    if factice is not None:
        factice["module"]["m"] = mod
        brut = factice["chercher"]
        mod.integrer = factice["integrer"]
        print("PREVOL : moteur FACTICE substitue (chercher_seuil, integrer) ;"
              " comptage exhaustif conserve ; G3 et garde_G3 restent REELS.")
    else:
        brut = mod.chercher_seuil

    def compte(*a, **kw):
        CPT["recherches"] += 1
        return brut(*a, **kw)
    mod.chercher_seuil = compte          # comptage EXHAUSTIF, jamais au site d'appel
    return mod


def fabriquer_factice(carte10, carte11):
    """Table (p, w, sgn) -> s* certifie ; chercher_seuil rend la valeur avec
    la note de la lignee ; integrer explose a partir de s*. G4 (dt/2) rend
    la meme valeur : ecart 0, chemin exerce."""
    table = {}
    for p, carte in ((5, carte10), (7, carte10), (4, carte11)):
        for w in POINTS:
            rec = carte[cle(p, w)]
            for sgn, k in ((+1, "sP"), (-1, "sM")):
                table[(p, "%.12f" % w, sgn)] = float(rec[k]["s"])
    module = {"m": None}

    def chercher(w2, sgn=1, dt=None, g=None):
        return table[(module["m"].P, "%.12f" % w2, sgn)], "OK|pas=6.03e-07"

    def integrer(w2, s_arr, sgn=1, dt=None, g=None):
        th = table[(module["m"].P, "%.12f" % w2, sgn)]
        return np.asarray(s_arr, float) >= th
    return {"chercher": chercher, "integrer": integrer, "module": module}


# =====================================================================
# 3. MESURE, GARDES DE RECHERCHE (patrons m11:890-908, 1007-1031)
# =====================================================================

note_ok = lambda n: isinstance(n, str) and n.startswith("OK|")


def pas_final(note):
    m = re.search(r"pas=([0-9.eE+-]+)", note or "")
    return float(m.group(1)) if m else None


def recevable(s, note):
    if not note_ok(note):
        return False, "note=%s" % note
    if s is None:
        return False, "seuil nul avec note OK -- incoherent"
    pas = pas_final(note)
    if pas is None:
        return False, "pas final illisible"
    if pas > PAS_GARANTI_G5 + EPS_PORTE:
        return False, "G5 pas final %.2e > %.0e" % (pas, PAS_GARANTI_G5)
    return True, ""


def metrique_g3(m9):
    rng = np.random.default_rng(20260726)
    x1 = rng.uniform(-2, 2, 4096); x2 = rng.uniform(-2, 2, 4096)
    dl1, dl2, e1, e2 = m9.grad_explicite(x1, x2)
    dr1, dr2 = m9.grad_rapide(x1, x2, m9.G_REF)
    return float(max(np.max(np.abs(dl1 - dr1) / (e1 + 1e-300)),
                     np.max(np.abs(dl2 - dr2) / (e2 + 1e-300))))


def rebind(m9, p, journal):
    m9.P = p
    e = metrique_g3(m9)
    journal.append({"p": p, "G3_backward": e})
    print("  rebinding m9.P = %d | G3 backward = %.3e" % (p, e))
    m9.garde_G3()
    return e


def mesurer(m9, w2, sgn, g=None, dt=None):
    g = m9.G_REF if g is None else g
    dt = m9.DT if dt is None else dt
    t0 = time.perf_counter()
    s, note = m9.chercher_seuil(w2, sgn=sgn, dt=dt, g=g)
    duree = time.perf_counter() - t0
    ok, motif = recevable(s, note)
    return {"s": (float(s) if s is not None else None), "note": note,
            "recevable": ok, "motif_exclusion": motif,
            "duree_s": float(duree)}


def verifier_domaine(s_etoile):
    """Garde de domaine du gel M11 v4, restauree (cert. v3, note (b) ; delta
    44.5(2)) : STRICTE, s* > LO0/0.90 = 1/18 exactement -- au bord exact le
    quotient vaut 0 et n_gros vaut 1, le balayage grossier degenere. La
    ceinture n_gros >= 2 est verifiee en plus apres chaque balayage."""
    if G6_BAS * s_etoile > LO0:
        return True, ""
    return False, ("s* = %r <= LO0/0.90 = 1/18 : balayage grossier degenere "
                   "(domaine M11 v4 restaure, cert. v3)" % s_etoile)


# =====================================================================
# 4. G6 -- balayer() REPRISE VERBATIM de m11_exposant_v3.py:1038-1072
#    (80cfa795...). SEULE difference : G6_HAUT = 1.05 (constante module,
#    gel v3). Le corps ci-dessous est BYTE-IDENTIQUE a la lignee ; la
#    preuve par diff est jointe a la livraison et refaite a la
#    certification du script.
# =====================================================================

def balayer(m9, w2, sgn, s_etoile):
    """Deux fenetres, PAS RELATIF gele, n calcule (gel v4, G6). Rend les deux
    masques et les consignations, separement -- note N-1."""
    lo_rel = m9.LO0 / s_etoile
    n_gros = int(math.ceil((G6_BAS - lo_rel) / G6_PAS_GROS)) + 1
    n_fin = int(round((G6_HAUT - G6_MID) / G6_PAS_FIN)) + 1
    if n_gros + n_fin > N_MAX_LIGNE:
        sys.exit("ARRET : %d points par ligne, borne declaree %d"
                 % (n_gros + n_fin, N_MAX_LIGNE))
    s_gros = np.linspace(m9.LO0, G6_BAS * s_etoile, n_gros)
    s_fin = np.linspace(G6_MID * s_etoile, G6_HAUT * s_etoile, n_fin)
    CPT["balayages"] += 1
    m_gros = m9.integrer(w2, s_gros, sgn)
    m_fin = m9.integrer(w2, s_fin, sgn)
    ex_sous = s_gros[m_gros]
    sous_seuil = s_fin[m_fin & (s_fin < G6_SEUIL_EXCL * s_etoile)]
    ilots = int(np.sum(np.diff(m_fin.astype(int)) == 1)) + (1 if m_fin[0] else 0)
    au_dessus = np.where((s_fin >= s_etoile) & (~m_fin))[0]
    return {
        "n_gros": n_gros, "n_fin": n_fin, "n_total": n_gros + n_fin,
        "pas_relatif_gros": G6_PAS_GROS, "pas_relatif_fin": G6_PAS_FIN,
        # note N-1 : les deux masques sont rapportes SEPAREMENT, avec les
        # comptes qui disent si la comparaison etait vide ou informative
        "gros_explosifs": int(m_gros.sum()),
        "fin_explosifs": int(m_fin.sum()),
        "fin_non_explosifs": int((~m_fin).sum()),
        "transition_dans_la_fenetre_fine": bool(m_fin.any() and (~m_fin).any()),
        "explosion_sous_LO0_0.90s": (float(ex_sous.min()) if len(ex_sous) else None),
        "explosion_sous_0.98s": (float(sous_seuil.min()) if len(sous_seuil) else None),
        "exclue": bool(len(sous_seuil) or len(ex_sous)),
        "ilots": ilots,
        "premiere_retombee_en_s": (float(s_fin[au_dessus[0]] / s_etoile)
                                   if len(au_dessus) else None),
        "_m_gros": m_gros, "_m_fin": m_fin,
    }


def g8b(bg_p, bg_m):
    """Symetrie bit a bit entre signes, a degre PAIR. Consignation, aucune
    porte. Rapporte SEPAREMENT le grossier et le fin (note N-1).
    [reprise verbatim m11_exposant_v3.py:1075-1095]"""
    d_gros = int(np.sum(bg_p["_m_gros"] != bg_m["_m_gros"])) \
        if bg_p["n_gros"] == bg_m["n_gros"] else -1
    d_fin = int(np.sum(bg_p["_m_fin"] != bg_m["_m_fin"])) \
        if bg_p["n_fin"] == bg_m["n_fin"] else -1
    return {
        "grossier": {"deviations": d_gros, "n": bg_p["n_gros"],
                     "explosifs_+1": bg_p["gros_explosifs"],
                     "explosifs_-1": bg_m["gros_explosifs"],
                     "pouvoir": "NUL si les deux comptes sont 0 (note N-1)"},
        "fin": {"deviations": d_fin, "n": bg_p["n_fin"],
                "explosifs_+1": bg_p["fin_explosifs"],
                "non_explosifs_+1": bg_p["fin_non_explosifs"],
                "transition_encadree": bg_p["transition_dans_la_fenetre_fine"],
                "pouvoir": "REEL si la transition est encadree (note N-1)"},
        "ilots_identiques": bg_p["ilots"] == bg_m["ilots"],
        "retombee_identique": bg_p["premiere_retombee_en_s"] == bg_m["premiere_retombee_en_s"],
        "attendu": "ZERO deviation -- identite demontree au gel, G8b",
    }


MOTIFS_NULL_G6 = {
    "premiere_retombee_en_s": "aucune retombee dans la fenetre [s*, 1.05 s*]",
    "explosion_sous_0.98s": "aucune explosion sous 0.98 s* dans la fenetre fine",
    "explosion_sous_LO0_0.90s": "aucune explosion dans la fenetre grossiere [LO0, 0.90 s*]",
}


def enrichir_g6(bal, s_etoile, note_recherche):
    """Extension E27 (la resolution voyage DANS la donnee) + domaine declare
    du gel v3 (S5b) + null motive (S4). N'altere PAS balayer : recalcul des
    grilles a l'identique depuis (n, bornes)."""
    if bal["n_gros"] < 2:
        sys.exit("ARRET : n_gros = %d < 2 -- ceinture de la garde de domaine "
                 "(cert. v3, section 5, point 2)" % bal["n_gros"])
    s_fin = np.linspace(G6_MID * s_etoile, G6_HAUT * s_etoile, bal["n_fin"])
    mfin = bal["_m_fin"]
    haut = mfin & (s_fin >= s_etoile)
    bal["ilots_au_dessus"] = int(np.sum(np.diff(haut.astype(int)) == 1)) \
        + (1 if haut[0] else 0)
    bal["ilots_au_dessus_domaine"] = "[s*, 1.05 s*] -- domaine declare, gel v3 (S5b)"
    bal["ilots_domaine_lignee"] = "[0.90 s*, 1.05 s*] -- champ 'ilots', balayer lignee"
    bal["bornes_gros"] = [LO0, G6_BAS * s_etoile]
    bal["bornes_fin"] = [G6_MID * s_etoile, G6_HAUT * s_etoile]
    bal["pas_eff_gros_rel"] = (G6_BAS * s_etoile - LO0) / ((bal["n_gros"] - 1) * s_etoile)
    bal["pas_eff_fin_rel"] = (G6_HAUT - G6_MID) / (bal["n_fin"] - 1)
    bal["pas_final_recherche"] = pas_final(note_recherche)
    idx = int(round((G6_SEUIL_EXCL - G6_MID) / G6_PAS_FIN))
    bal["indice_du_seuil_098"] = idx
    bal["explosif_a_l_indice_40"] = bool(mfin[idx])
    bal["ecart_relatif_indice_40_au_seuil"] = float(s_fin[idx] / s_etoile
                                                    - G6_SEUIL_EXCL)
    # S6 (cert. script v2) : le temoin calcule l'EXPRESSION DE LA GARDE,
    # operation pour operation -- meme produit, meme comparaison. La
    # soustraction est EXACTE ici (Sterbenz, operandes dans un facteur 2) :
    # le signe de l'ecart absolu encode fidelement le predicat. Le champ
    # relatif ci-dessus reste pour la lecture humaine et ne JUGE pas.
    bal["ecart_absolu_indice_40_au_seuil"] = float(
        s_fin[idx] - G6_SEUIL_EXCL * s_etoile)
    bal["indice_40_compte_comme_sous_seuil"] = bool(
        s_fin[idx] < G6_SEUIL_EXCL * s_etoile)
    for champ, motif in MOTIFS_NULL_G6.items():
        if bal[champ] is None:
            bal[champ + "_motif"] = motif
    return bal


# =====================================================================
# 5. G9 -- COUVERTURE (S4/S42.3) : champ EXISTANT, null MOTIVE
# =====================================================================

REQUIS_MESURE = ("s", "note", "recevable", "motif_exclusion", "duree_s")
REQUIS_CARTE = ("sP", "sM", "sF", "frag", "asym", "G1")
NULLABLES_CARTE = ("sF", "frag", "asym")
REQUIS_G6 = ("n_gros", "n_fin", "n_total", "pas_relatif_gros", "pas_relatif_fin",
             "gros_explosifs", "fin_explosifs", "fin_non_explosifs",
             "transition_dans_la_fenetre_fine", "explosion_sous_LO0_0.90s",
             "explosion_sous_0.98s", "exclue", "ilots", "ilots_au_dessus",
             "premiere_retombee_en_s", "bornes_gros", "bornes_fin",
             "pas_eff_gros_rel", "pas_eff_fin_rel", "pas_final_recherche",
             "indice_du_seuil_098", "explosif_a_l_indice_40",
             "ecart_relatif_indice_40_au_seuil",
             "ecart_absolu_indice_40_au_seuil",
             "indice_40_compte_comme_sous_seuil")
NULLABLES_G6 = tuple(MOTIFS_NULL_G6)


def g9_verifier(res):
    """Rend la liste des defauts de couverture (vide = conforme). Un champ
    absent est un defaut ; un null sans champ jumeau <nom>_motif non vide est
    un defaut ; un null motive est une donnee."""
    defauts = []
    for k, v in res["resultats"]["carte"].items():
        for ch in REQUIS_CARTE:
            if ch not in v:
                defauts.append("carte[%s] : champ absent %s" % (k, ch)); continue
            if v[ch] is None:
                if ch not in NULLABLES_CARTE:
                    defauts.append("carte[%s] : %s null non admissible" % (k, ch))
                elif not v.get(ch + "_motif"):
                    defauts.append("carte[%s] : %s null SANS motif" % (k, ch))
        for sk in ("sP", "sM"):
            m = v.get(sk)
            if not isinstance(m, dict):
                continue
            for ch in REQUIS_MESURE:
                if ch not in m:
                    defauts.append("carte[%s].%s : champ absent %s" % (k, sk, ch))
            if m.get("s") is None and not m.get("motif_exclusion"):
                defauts.append("carte[%s].%s : s null SANS motif_exclusion" % (k, sk))
    for k, b in res["resultats"]["G6"].items():
        for ch in REQUIS_G6:
            if ch not in b:
                defauts.append("G6[%s] : champ absent %s" % (k, ch)); continue
            if b[ch] is None:
                if ch not in NULLABLES_G6:
                    defauts.append("G6[%s] : %s null non admissible" % (k, ch))
                elif not b.get(ch + "_motif"):
                    defauts.append("G6[%s] : %s null SANS motif" % (k, ch))
    return defauts


def _stub_integrer_seuil(seuil):
    return lambda w2, s, sgn=1, dt=None, g=None: np.asarray(s, float) >= seuil


def _record_synthetique():
    """Construit une ligne et un balayage par LES MEMES fonctions que le run
    (assembler_ligne, balayer, enrichir_g6) -- G9 avant-run et selftest."""
    res = {"resultats": {"carte": {}, "G6": {}}}
    v = res["resultats"]["carte"].setdefault(cle(5, 9.99), {})
    fake = {"s": 1.234, "note": "OK|pas=6.03e-07", "recevable": True,
            "motif_exclusion": "", "duree_s": 0.0}
    v["sP"] = dict(fake); v["sM"] = dict(fake, s=1.334)
    assembler_ligne(v)
    v["G1"] = {"sP": {"verdict": "SYNTHETIQUE"}, "sM": {"verdict": "SYNTHETIQUE"}}
    ns = SimpleNamespace(LO0=LO0, integrer=_stub_integrer_seuil(1.234))
    cpt0 = dict(CPT)
    bal = balayer(ns, 9.99, +1, 1.234)
    CPT.update(cpt0)                      # le stub ne compte pas au programme
    res["resultats"]["G6"][cle(5, 9.99) + "|+1"] = enrichir_g6(bal, 1.234, fake["note"])
    return res


def garde_G9_avant_run():
    d = g9_verifier(_record_synthetique())
    if d:
        sys.exit("ARRET G9 (avant le run) : le constructeur de consignations "
                 "est incomplet :\n  " + "\n  ".join(d))
    print("G9 avant-run : constructeur de consignations COMPLET (record "
          "synthetique conforme).")


# =====================================================================
# 6. ASSEMBLAGE D'UNE LIGNE (sF, frag, asym -- convention (f))
# =====================================================================

def assembler_ligne(v):
    sP, sM = v["sP"], v["sM"]
    if sP["recevable"] and sM["recevable"]:
        v["sF"] = min(sP["s"], sM["s"])
        v["frag"] = 1 if sP["s"] <= sM["s"] else -1
        v["asym"] = sP["s"] / sM["s"]
    else:
        motif = sP["motif_exclusion"] or sM["motif_exclusion"] or "recherche non recevable"
        v["sF"] = None; v["sF_motif"] = motif
        v["frag"] = None; v["frag_motif"] = motif
        v["asym"] = None; v["asym_motif"] = motif


# =====================================================================
# 7. FILTRE DE NOUVEAUTE EXACT -- utilitaire PARTAGE pour m12_ponctuel_v1.py
#    (gel M12 v3, IMPLEMENTATION (i)) ; teste ICI car la certification du
#    script pilote est le premier point de controle (cert. v3, sect. 5.3).
# =====================================================================

GRILLE_CENT = (125, 130, 135, 145, 155, 170, 180, 190, 205, 215, 230, 245,
               260, 275, 285)             # + sqrt(2), traite par encadrement
SQ2_LO = Fraction(141421356237, 10 ** 11)
SQ2_HI = Fraction(141421356238, 10 ** 11)
assert SQ2_LO * SQ2_LO < 2 < SQ2_HI * SQ2_HI


def neuf_exact(W):
    """Lecture A (gel M12 v3) : d >= 0.03, ENTIERS de centiemes ; sqrt(2) par
    encadrement rationnel, ambiguite interdite par assertion."""
    if any(abs(W - G) < 3 for G in GRILLE_CENT):
        return False
    w = Fraction(W, 100)
    d_lo, d_hi = sorted((abs(w - SQ2_LO), abs(w - SQ2_HI)))
    seuil = Fraction(3, 100)
    assert (d_lo >= seuil) == (d_hi >= seuil), "encadrement sqrt(2) ambigu"
    return d_lo >= seuil


def neuf_flottant(W):
    """Replique de la lecture C (le defaut) -- sert au test NEGATIF : le
    selftest exige que 2.27 soit RETENU par neuf_exact et EXCLU par ceci."""
    wf = W / 100.0
    grille_f = [g / 100.0 for g in GRILLE_CENT] + [1.4142135623730951]
    return all(abs(wf - g) >= 0.03 for g in grille_f)


# =====================================================================
# 8. C-P5 : CLOPPER-PEARSON, ET APPLICATION INDICATIVE DE D-N (delta 44.7)
# =====================================================================

def cp_borne_sup(x, n, conf=0.80):
    """Borne superieure unilaterale : plus petit q tel que
    P(X <= x ; n, q) <= 1 - conf. Bisection sur la CDF binomiale exacte."""
    if x >= n:
        return 1.0
    alpha = 1.0 - conf
    lo, hi = x / n, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        cdf = sum(math.comb(n, i) * mid ** i * (1 - mid) ** (n - i)
                  for i in range(x + 1))
        if cdf > alpha:
            lo = mid
        else:
            hi = mid
    return hi


def n_indicatif_dn(q):
    """Application INDICATIVE de la regle D-N du gel M12 v3. L'application
    OPPOSABLE appartient au script de M12 (delta 44.7)."""
    s = (1.0 - q) ** 3
    n = 4
    while sum(math.comb(n, i) * s ** i * (1 - s) ** (n - i)
              for i in range(4, n + 1)) < 0.90:
        n += 1
        if n > 100:
            return None
    return n


# =====================================================================
# 9. SELFTEST -- il MORD, et il declare la portee reelle de chaque controle
# =====================================================================

def selftest():
    print("=" * 70)
    print("SELFTEST m12_pilote_v1.py")
    print("=" * 70)
    certifier_gel()

    print("\n[1] programme fige, forme derivee")
    assert RECH_ATTENDUES == 25 and BAL_ATTENDUS == 24 and len(LIGNES) == 12
    print("    25 recherches (16+4+4+1), 24 balayages, 12 lignes : CONFORME")

    print("\n[2] extraction STRUCTURELLE du gel (regle 12) et leurre reel")
    bloc, _ = certifier_gel(verbeux=False)
    tags = [m.group(1) for l in bloc.split("\n")
            for m in [re.match(r"^  (C-P\d)  ", l)] if m]
    assert tags == ["C-P1", "C-P2", "C-P3", "C-P4", "C-P5"], tags
    nu = bloc.count("MES ATTENTES")
    tetes = sum(1 for l in bloc.split("\n") if l.startswith("MES ATTENTES"))
    assert nu >= 2 and tetes == 1, (nu, tetes)
    print("    consignations extraites par structure : %s" % tags)
    print("    leurre : 'MES ATTENTES' x%d en sous-chaine nue, x1 en en-tete"
          " -> l'ancrage naif echouerait, le structurel tient" % nu)

    print("\n[3] vecteurs de geometrie -- PORTEE REELLE DECLAREE (cert. v3)")
    ns = SimpleNamespace(LO0=LO0,
                         integrer=lambda w2, s, sgn=1, dt=None, g=None:
                         np.zeros(np.asarray(s).shape, bool))
    cpt0 = dict(CPT)
    couples = {}
    for arrondi, f in (("floor", math.floor), ("round", round), ("ceil", math.ceil)):
        couples[arrondi] = tuple(1 + f((G6_BAS - LO0 / s) / G6_PAS_GROS)
                                 for s in (0.47, 2.05))
    for s_ctl, att in ((0.47, 160), (2.05, 177)):
        b = balayer(ns, 9.99, +1, s_ctl)
        assert b["n_gros"] == att, (s_ctl, b["n_gros"], att)
        assert b["n_fin"] == 76, b["n_fin"]
        print("    s_ctl=%.2f : n_gros=%d (attendu %d), n_fin=%d" %
              (s_ctl, b["n_gros"], att, b["n_fin"]))
    CPT.update(cpt0)
    assert couples == {"floor": (159, 176), "round": (160, 176), "ceil": (160, 177)}
    assert int(round((G6_SEUIL_EXCL - G6_MID) / G6_PAS_FIN)) == 40
    Xf = (G6_HAUT - G6_MID) / G6_PAS_FIN
    assert (1 + math.floor(Xf), 1 + round(Xf), 1 + math.ceil(Xf)) == (76, 76, 77)
    assert (Fraction(21, 20) - Fraction(9, 10)) / Fraction(1, 500) == 75
    print("    couples n_g : floor %s | round %s | ceil %s" %
          (couples["floor"], couples["round"], couples["ceil"]))
    print("    PORTEE : les deux vecteurs n_g PINCENT CEIL -- (160, 177) lui")
    print("    est propre. Le vecteur n_f EXCLUT CEIL (77 sur le quotient IEEE")
    print("    %.17g) mais NE SEPARE PAS round de floor : le quotient fin est" % Xf)
    print("    CONSTANT (75 exact). Il tue le risque reel, rien de plus.")

    print("\n[4] garde de domaine STRICTE (s* > 1/18) et sa ceinture")
    assert not verifier_domaine(1.0 / 18.0)[0]
    assert not verifier_domaine(0.0555)[0]
    assert verifier_domaine(0.0556)[0]
    cpt0 = dict(CPT)
    assert balayer(ns, 9.99, +1, 0.0556)["n_gros"] == 2
    CPT.update(cpt0)
    print("    1/18 (flottant) -> ARRET ; 0.0555 -> ARRET ; 0.0556 -> n_gros=2")

    print("\n[5] filtre de nouveaute : le test NEGATIF MORD (cert. v3, 5.3)")
    assert neuf_exact(227) is True, "2.27 doit etre RETENU (lecture A)"
    assert neuf_flottant(227) is False, "la replique flottante doit l'exclure"
    assert neuf_exact(213) is False, "0.02 d'un point de grille -> EXCLU"
    print("    2.27 : exact RETENU, flottant EXCLU -> le test discrimine ;")
    print("    2.13 (a 0.02 de 2.15) : EXCLU. Conforme au gel M12 v3, item (i).")

    print("\n[6] G9 : couverture complete, et defauts DETECTES (tests negatifs)")
    r = _record_synthetique()
    assert g9_verifier(r) == []
    k = cle(5, 9.99)
    r2 = _record_synthetique()
    del r2["resultats"]["carte"][k]["sF"]
    d1 = g9_verifier(r2)
    r3 = _record_synthetique()
    r3["resultats"]["G6"][k + "|+1"]["premiere_retombee_en_s"] = None
    r3["resultats"]["G6"][k + "|+1"].pop("premiere_retombee_en_s_motif", None)
    d2 = g9_verifier(r3)
    r4 = _record_synthetique()
    del r4["resultats"]["G6"][k + "|+1"]["explosif_a_l_indice_40"]
    d3 = g9_verifier(r4)
    r5 = _record_synthetique()
    del r5["resultats"]["G6"][k + "|+1"]["indice_40_compte_comme_sous_seuil"]
    d4 = g9_verifier(r5)
    assert d1 and d2 and d3 and d4, (d1, d2, d3, d4)
    print("    record conforme : 0 defaut ; champ supprime : %d ; null nu :"
          " %d ; champ S4 supprime : %d ; predicat S6 supprime : %d"
          % (len(d1), len(d2), len(d3), len(d4)))

    print("\n[7] Clopper-Pearson et application indicative de D-N (delta 44.7)")
    assert abs(cp_borne_sup(0, 12) - (1 - 0.20 ** (1 / 12))) < 1e-9
    assert cp_borne_sup(1, 12) > cp_borne_sup(0, 12)
    forc = [(x, cp_borne_sup(x, 12), n_indicatif_dn(cp_borne_sup(x, 12)))
            for x in range(4)]
    assert [n for _, _, n in forc] == [8, 13, 20, 32]
    for x, q, n in forc:
        print("    pertes=%d : q_L(80%%)=%.4f -> N=%d%s"
              % (x, q, n, "" if n <= 12 else "  -> ARRET (N > 12)"))
    print("    TOUT-OU-RIEN confirme : zero perte ou arret (delta 44.7).")

    print("\n[8] filtres de note et parseur du pas final")
    assert pas_final("OK|pas=6.03e-07") == 6.03e-07
    assert recevable(1.0, "OK|pas=2.00e-05")[0] is False
    assert recevable(None, "ECHEC_HAUT")[0] is False
    print("    'OK|pas=6.03e-07' lu ; pas > 1e-5 rejete ; ECHEC_* rejete")

    print("\n[9] G1 : compte, jamais affirme (cert. script v1, S2 ; D-M10-14)")
    der = lambda c: (c["ECHEC"] == 0 and c["NON EVALUABLE"] == 0
                     and c["PASSE"] == len(LIGNES) * 2)
    assert der({"PASSE": 24, "ECHEC": 0, "NON EVALUABLE": 0}) is True
    assert der({"PASSE": 23, "ECHEC": 0, "NON EVALUABLE": 1}) is False
    print("    24/0/0 -> True ; 23/0/1 -> False : NON EVALUABLE n'est pas PASSE")

    print("\n[10] temoin du bord = expression de la GARDE (cert. script v2, S6)")
    ns2 = SimpleNamespace(LO0=LO0,
                          integrer=lambda w2, s, sgn=1, dt=None, g=None:
                          np.zeros(np.asarray(s).shape, bool))
    cpt0 = dict(CPT)
    cat = lambda x: 0 if x == 0 else (1 if x > 0 else -1)
    for s in (0.4729, 0.96813, 2.8164, S_TEMOIN_DIVERGENT):
        b = enrichir_g6(balayer(ns2, 9.9, +1, s), s, "OK|pas=6.03e-07")
        sf = np.linspace(G6_MID * s, G6_HAUT * s, b["n_fin"])
        garde = bool((sf < G6_SEUIL_EXCL * s)[b["indice_du_seuil_098"]])
        assert b["indice_40_compte_comme_sous_seuil"] == garde
        assert (b["ecart_absolu_indice_40_au_seuil"] < 0) == garde
    rel = b["ecart_relatif_indice_40_au_seuil"]
    absu = b["ecart_absolu_indice_40_au_seuil"]
    assert cat(rel) != cat(absu), (rel, absu)
    CPT.update(cpt0)
    print("    identite temoin == garde : 4 vecteurs, operation pour operation")
    print("    divergence rel/abs EXHIBEE a s* = %r :" % S_TEMOIN_DIVERGENT)
    print("      relatif %+.3e vs absolu %+.3e -- le relatif LIT, le" % (rel, absu))
    print("      predicat JUGE. Un temoin temoigne du fait juge, pas d'un voisin.")

    print("\nSELFTEST : TOUT PASSE (10 sections).")
    return 0


# =====================================================================
# 10. RUN
# =====================================================================

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--prevol", action="store_true",
                    help="pre-vol a moteur factice ; ecrit un fichier SEPARE")
    ap.add_argument("--moteur", default="m9_replication_v1.py")
    ap.add_argument("--sources-prevol", default="prevol_sources")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())

    bloc, hgel = certifier_gel()
    mode = "PREVOL" if a.prevol else "REEL"
    fout = FOUT_PREVOL if a.prevol else FOUT
    assert (not a.prevol) or fout != FOUT, "le pre-vol n'ecrit JAMAIS le fichier reel"
    carte10, carte11, meta_src = charger_sources(a.prevol, a.sources_prevol)
    factice = fabriquer_factice(carte10, carte11) if a.prevol else None
    m9 = charger_moteur(a.moteur, factice=factice)
    garde_G9_avant_run()

    res = {"meta": {"gel_sha256_bloc": hgel, "moteur_sha256": SHA_MOTEUR,
                    "geometrie_provenance": "balayer(), m11_exposant_v3.py:"
                    "1038-1072, %s ; reprise verbatim, G6_HAUT 1.30 -> 1.05"
                    % SHA_M11_SCRIPT,
                    "mode": mode, "sources": meta_src,
                    "convention_empreinte": "B -- bloc saut final inclus = fichier",
                    "G3_par_degre": [], "gardes": [], "exclusions": {}},
           "resultats": {"carte": {}, "G6": {}, "G8": {}, "G4": {}},
           "resume": {}}
    jg3 = res["meta"]["G3_par_degre"]
    g1_cpt = {"PASSE": 0, "ECHEC": 0, "NON EVALUABLE": 0}

    def sauve():
        sauver(res, fout)

    def ancre(p, w, sgn):
        carte = carte11 if p == 4 else carte10
        rec = carte.get(cle(p, w))
        if rec is None:
            sys.exit("ARRET : ancre certifiee absente pour %s" % cle(p, w))
        return float(rec["sP" if sgn > 0 else "sM"]["s"])

    for p in DEGRES:
        print("\n--- degre p = %d : recherches, G1, puis balayages ---" % p)
        rebind(m9, p, jg3)
        for w in POINTS:
            v = res["resultats"]["carte"].setdefault(cle(p, w), {})
            for sgn, k in ((+1, "sP"), (-1, "sM")):
                m = mesurer(m9, w, sgn)
                if p == 4 and sgn < 0:
                    m["role"] = "regression_G8"
                v[k] = m
                g1 = {}
                if m["recevable"]:
                    ref = ancre(p, w, sgn)
                    ec = abs(m["s"] / ref - 1.0)
                    g1 = {"certifie": ref, "mesure": m["s"], "ecart": ec,
                          "verdict": "PASSE" if ec <= TOL_G1 + EPS_PORTE else "ECHEC"}
                else:
                    g1 = {"verdict": "NON EVALUABLE", "motif": m["motif_exclusion"]}
                v.setdefault("G1", {})[k] = g1
                g1_cpt[g1["verdict"]] += 1
                sauve()
                if g1["verdict"] == "ECHEC":
                    res["meta"]["gardes"].append(
                        "G1 %s sgn=%+d : ecart %.4f %% > 2 %%" % (cle(p, w), sgn, 100 * ec))
                    sauve()
                    sys.exit("ARRET G1 : %s sgn=%+d, ecart %.4f %% -- aucune "
                             "transmission a M12." % (cle(p, w), sgn, 100 * ec))
                print("  p=%d w2=%.2f sgn=%+d : %s | G1 %s" %
                      (p, w, sgn, m["note"], g1["verdict"]))
            assembler_ligne(v)
            if v["sF"] is None:
                res["meta"]["exclusions"].setdefault(cle(p, w), []).append(
                    "G5 : " + v["sF_motif"])
            if p == 4 and v["sP"]["recevable"] and v["sM"]["recevable"]:
                ecart = v["sP"]["s"] - v["sM"]["s"]
                g8a = {"ecart_absolu": ecart,
                       "verdict": "OK" if ecart == 0.0 else "ECHEC"}
                res["resultats"]["G8"].setdefault(cle(p, w), {})["G8a"] = g8a
                if ecart != 0.0:
                    sauve()
                    sys.exit("ARRET G8a : sP - sM = %r != 0 en w2=%.2f -- la "
                             "lignee de code a change." % (ecart, w))
            elif p == 4:
                res["meta"]["exclusions"].setdefault(cle(p, w), []).append(
                    "G8 non evaluable (regression sgn -1 non recevable)")
            sauve()

        for w in POINTS:
            v = res["resultats"]["carte"][cle(p, w)]
            if not (v["sP"]["recevable"] and v["sM"]["recevable"]):
                CPT["balayages_sautes"] += 2
                res["meta"]["gardes"].append(
                    "G6 %s : deux balayages SAUTES (ligne non recevable)" % cle(p, w))
                sauve()
                continue
            bg = {}
            for sgn, k in ((+1, "sP"), (-1, "sM")):
                ok, motif = verifier_domaine(v[k]["s"])
                if not ok:
                    res["meta"]["gardes"].append("DOMAINE %s sgn=%+d : %s"
                                                 % (cle(p, w), sgn, motif))
                    sauve()
                    sys.exit("ARRET domaine : " + motif)
                bal = balayer(m9, w, sgn, v[k]["s"])
                enrichir_g6(bal, v[k]["s"], v[k]["note"])
                bg[k] = bal
                res["resultats"]["G6"][cle(p, w) + "|%+d" % sgn] = bal
                if bal["exclue"]:
                    res["meta"]["exclusions"].setdefault(cle(p, w), []).append(
                        "G6 sgn=%+d explosion sous seuil" % sgn)
            if p == 4:
                g8 = g8b(bg["sP"], bg["sM"])
                res["resultats"]["G8"].setdefault(cle(p, w), {})["G8b"] = g8
                if (g8["grossier"]["deviations"] != 0 or g8["fin"]["deviations"] != 0
                        or not g8["ilots_identiques"] or not g8["retombee_identique"]):
                    sauve()
                    sys.exit("ARRET G8b : masques non identiques en w2=%.2f -- "
                             "la lignee de code a change." % w)
            print("  balayages w2=%.2f : n_gros=%d n_fin=%d | exclue %s/%s" %
                  (w, bg["sP"]["n_gros"], bg["sP"]["n_fin"],
                   bg["sP"]["exclue"], bg["sM"]["exclue"]))
            sauve()

    # --- G4 : dt/2 sur la ligne maximisant g s*^(p-1) --------------------
    print("\n--- G4 : dt/2 sur l'echelle de force maximale ---")
    best = None
    for p in DEGRES:
        for w in POINTS:
            v = res["resultats"]["carte"][cle(p, w)]
            for sgn, k in ((+1, "sP"), (-1, "sM")):
                if not v[k]["recevable"]:
                    continue
                e = m9.G_REF * v[k]["s"] ** (p - 1)
                if best is None or e > best[0]:
                    best = (e, p, w, sgn, v[k]["s"])
    if best is None:
        CPT["sautees"] += 1
        res["meta"]["gardes"].append("G4 : recherche SAUTEE (aucune ligne recevable)")
    else:
        e, p, w, sgn, sref = best
        rebind(m9, p, jg3)
        r2 = mesurer(m9, w, sgn, dt=m9.DT / 2)
        ec = abs(r2["s"] / sref - 1.0) if r2["recevable"] else None
        okg4 = ec is not None and ec <= TOL_G4 + EPS_PORTE
        res["resultats"]["G4"] = {"echelle_force": e, "p": p, "w2": w, "sgn": sgn,
                                  "s_dt": sref, "s_dt2": r2["s"], "duree_s": r2["duree_s"],
                                  "ecart": ec,
                                  "ecart_motif": (None if ec is not None else
                                                  r2["motif_exclusion"]),
                                  "verdict": "PASSE" if okg4 else "NON FIABLE"}
        res["resultats"]["G4"]["dans_q_L"] = False
        res["resultats"]["G4"]["declaration"] = (
            "G4 n'entre PAS dans q_L : le pilote mesure une attrition de "
            "GEOMETRIE ; G4 est un diagnostic de pas de temps, transmis "
            "comme fait separe (cert. script v1, S3, recommandation suivie)")
        if not okg4:
            res["meta"]["gardes"].append(
                "G4 NON FIABLE sur %s sgn=%+d -- HORS q_L, transmis separement"
                % (cle(p, w), sgn))
        print("  G4 p=%d w2=%.2f sgn=%+d : ecart %s" %
              (p, w, sgn, "%.3f %%" % (100 * ec) if ec is not None else "n/a"))
    sauve()

    # --- C-P5 : attrition, borne sup 80 %, application indicative D-N ----
    lignes = {}
    for p, w in LIGNES:
        k = cle(p, w)
        motifs = list(res["meta"]["exclusions"].get(k, []))
        if res["resultats"]["carte"][k]["sF"] is None and not any(
                m.startswith("G5") for m in motifs):
            motifs.append("G5 : sF absent (fallback)")
        lignes[k] = {"perdue": bool(motifs), "motifs": motifs}
    x = sum(1 for l in lignes.values() if l["perdue"])
    ventil = {m: sum(1 for l in lignes.values()
                     if any(s.startswith(m) for s in l["motifs"]))
              for m in ("G5", "G6", "G8")}
    q_obs = x / len(LIGNES)
    q80 = cp_borne_sup(x, len(LIGNES))
    n_ind = n_indicatif_dn(q80)
    durees = [res["resultats"]["carte"][cle(p, w)][k]["duree_s"]
              for p, w in LIGNES for k in ("sP", "sM")]
    if res["resultats"]["G4"].get("duree_s") is not None:
        durees.append(res["resultats"]["G4"]["duree_s"])
    res["resume"] = {
        "lignes": lignes,
        "lignes_perdues": x,
        "q_L_observe": q_obs,
        "q_L_borne_sup_80": q80,
        "methode": "Clopper-Pearson, borne superieure unilaterale a 80 %",
        "duree_par_recherche_s": {"n": len(durees), "total": float(sum(durees)),
                                  "min": float(min(durees)), "max": float(max(durees)),
                                  "moyenne": float(sum(durees) / len(durees))},
        "G1": {"n_passe": g1_cpt["PASSE"], "n_echec": g1_cpt["ECHEC"],
               "n_non_evaluable": g1_cpt["NON EVALUABLE"],
               "attendu": len(LIGNES) * 2,
               "regle": "G1_passe = n_echec == 0 ET n_non_evaluable == 0 ET "
                        "n_passe == attendu -- compte, jamais affirme "
                        "(cert. script v1, S2 ; D-M10-14)"},
        "pertes_par_mecanisme": ventil,
        "pertes_par_mecanisme_note": "ventilation par MECANISME, pas une "
            "partition : une ligne a plusieurs motifs compte dans plusieurs "
            "seaux ; la somme peut exceder lignes_perdues (cert. script v2, 4a)",
        "transmis_a_M12": {
            "q_L_80": q80,
            "G1_passe": (g1_cpt["ECHEC"] == 0
                         and g1_cpt["NON EVALUABLE"] == 0
                         and g1_cpt["PASSE"] == len(LIGNES) * 2),
            "G6_declenche": any("G6" in " ".join(l["motifs"]) for l in lignes.values()),
            "G6_ou": sorted(k for k, l in lignes.items()
                            if any(m.startswith("G6") for m in l["motifs"])),
            "G4_fiable": (res["resultats"]["G4"].get("verdict") == "PASSE"
                          if res["resultats"]["G4"] else None),
            "G4_fiable_motif": (None if res["resultats"]["G4"] else
                                "recherche G4 sautee (aucune ligne recevable)"),
        },
        "application_D_N_indicative": {
            "N": n_ind,
            "issue": ("EXECUTABLE (N = %d)" % n_ind) if (n_ind or 99) <= 12
                     else "ARRET (N > 12) -> gel v4",
            "statut": "INDICATIF -- la regle D-N appartient au gel M12 ; son "
                      "application OPPOSABLE au script de M12 (delta 44.7)",
        },
    }

    res["meta"]["script_sha256"] = _sha(os.path.abspath(__file__))
    dtmod = __import__("datetime")
    res["meta"]["date_utc"] = dtmod.datetime.now(dtmod.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")
    res["meta"]["recherches"] = {"comptees": CPT["recherches"],
                                 "sautees": CPT["sautees"],
                                 "somme": CPT["recherches"] + CPT["sautees"],
                                 "attendues": RECH_ATTENDUES,
                                 "invariant": "comptees + sautees == attendues"}
    res["meta"]["balayages"] = {"comptes": CPT["balayages"],
                                "sautes": CPT["balayages_sautes"],
                                "somme": CPT["balayages"] + CPT["balayages_sautes"],
                                "attendus": BAL_ATTENDUS,
                                "invariant": "comptes + sautes == attendus"}
    defauts = g9_verifier(res)
    if defauts:
        sauve()
        sys.exit("ARRET G9 (apres run) : %d defaut(s) de couverture :\n  %s"
                 % (len(defauts), "\n  ".join(defauts)))
    sauve()
    if CPT["recherches"] + CPT["sautees"] != RECH_ATTENDUES:
        sys.exit("ARRET : %d recherches + %d sautees = %d, le PROGRAMME FIGE "
                 "en declare %d." % (CPT["recherches"], CPT["sautees"],
                                     CPT["recherches"] + CPT["sautees"], RECH_ATTENDUES))
    if CPT["balayages"] + CPT["balayages_sautes"] != BAL_ATTENDUS:
        sys.exit("ARRET : %d balayages + %d sautes = %d, le PROGRAMME FIGE en "
                 "declare %d." % (CPT["balayages"], CPT["balayages_sautes"],
                                  CPT["balayages"] + CPT["balayages_sautes"], BAL_ATTENDUS))
    print("\nEcrit : %s" % fout)
    print("Recherches : %d + %d sautees = %d / %d | balayages : %d + %d sautes = %d / %d"
          % (CPT["recherches"], CPT["sautees"], CPT["recherches"] + CPT["sautees"],
             RECH_ATTENDUES, CPT["balayages"], CPT["balayages_sautes"],
             CPT["balayages"] + CPT["balayages_sautes"], BAL_ATTENDUS))
    print("Lignes perdues : %d / 12 | q_L(80%%) = %.4f | D-N indicatif : %s"
          % (x, q80, res["resume"]["application_D_N_indicative"]["issue"]))
    print("sha256 du JSON : %s" % _sha(fout))


def sauver(res, chemin):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)

    def nettoie(o):
        if isinstance(o, dict):
            for k in o:
                if not isinstance(k, str):
                    raise TypeError("clef non-chaine %r (%s)" % (k, type(k).__name__))
            return {k: nettoie(v) for k, v in o.items() if not k.startswith("_")}
        if isinstance(o, list):
            return [nettoie(v) for v in o]
        if isinstance(o, (np.floating, np.integer)):
            return o.item()
        if isinstance(o, np.ndarray):
            return o.tolist()
        return o
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(nettoie(res), f, indent=1, sort_keys=True, ensure_ascii=True)


if __name__ == "__main__":
    main()
