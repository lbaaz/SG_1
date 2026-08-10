#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PRE-ENREGISTREMENT M10 -- L'EXPOSANT beta DE LA LOI DE SEUIL (CLASSIQUE PUR)
(gele avant l'ecriture de toute ligne de code ; bloc ASCII, canonique NFC+LF ;
nom de fichier versionne, regle E19 -- version v8)

HISTORIQUE DU GEL
  v1, sha256 ed8121b432ede8eb39de7c15eb2905d98d7c41115c17f5234408437bbbd797ad
  REFUSEE A LA CERTIFICATION (audit pre-feu machine 2 du 26/07 : D-M10-1,
  D-M10-2, D-M10-3). Les trois defauts sont ACCEPTES apres verification
  independante machine 1. v2 :
  (1) D-M10-1 -- l'ensemble d'explosion n'est PAS monotone en s. Verifie ici
      a p=3, w2=1.35, sgn=-1 : premier s explosif = 1.696 / 3.182 / 1.608 /
      1.640 / 1.595 pour n = 48 / 96 / 192 / 480 / 2000, avec 3 / 2 / 3 / 11 /
      33 ilots ; 47.9 % de [0.05, 6] explose ; le sM publie (2.95642) est a
      -46.1 % du balayage fin. La suite ne converge pas : a p=3, s* n'est pas
      defini par le protocole. => GARDE G6 ajoutee (bloquante), et p=3 RETIRE
      de la manche (P-M10c supprimee) plutot que garde par une ancre qui
      declencherait a coup sur.
  (2) D-M10-2 -- G1 n'ancrait aucune ligne p=3 : sans objet, p=3 est retire.
  (3) D-M10-3 -- amputation asymetrique du fit : G7 de repercussion ajoutee.
  (4) R-1 adopte : P-M10a devient un vrai test d'EQUIVALENCE sur l'IC 95 %.
  (5) R-2 adopte : rayon d'exclusion DEPENDANT DE L'ORDRE ; sqrt(2) sort du fit.
  (6) R-4 adopte : dependance de beta a la grille declaree en limitations.
  CONTRE-PROPOSITION MOTIVEE, seul point de divergence : le critere (ii) du
  correctif demande (aucune retombee a la stabilite sur [s*, 1.3 s*]) est
  mesure ici comme NON APPLICABLE -- aux deux points neufs testes (p=5
  w2=2.60, p=7 w2=1.25) la premiere retombee est a 1.000 s* et 1.001 s*. Le
  bord d'explosion est CRIBLE partout ; c'est le rivage fractal deja
  documente par la campagne, pas un defaut de mesure. En faire une porte
  n'exclurait pas les lignes pathologiques : il exclurait TOUTES les lignes.
  G6 retient donc le critere de PRIMAUTE (celui qui teste la definition de
  s*) comme bloquant, et la densite d'ilots comme consignation sans porte.
  Machine 2 arbitre : si elle maintient (ii) bloquant, la manche est
  irrealisable et il faut redefinir l'observable avant tout.
  Aucun numero d'erratum reserve (E18).
  v8 (sur diff de v7, non certifiee) : corrige D-M10-9. E24 avait fait passer
  la partition de 11+5 a 10+6 ; TROIS phrases du corps decrivaient encore
  l'ancienne. Machine 2 les a toutes cherchees plutot que de verifier celles
  qu'on lui montrait -- balayage de tous les comptes, de tout motif "n
  points", de tout "hors fit" et de tout "1.35", HISTORIQUE excepte -- et il
  y en a exactement trois. Les faux voisins ont ete verifies un par un et
  sont sains : le "repere a cinq points" est celui de P-M10f, sans rapport
  avec le fit ; le "sous 8 points" de G7 est le seuil de non-conclusion.
  (1) PROTOCOLE DE FIT, motif de la separation. L'enonce n'etait pas
  seulement perime, il etait devenu FAUX : 1.35 est a 0.1500 de 3:2 et 0.6500
  de 2:1, au-dela de 0.12 dans les deux cas ; il ne sort pas pour ce motif-la
  mais pour 4:3, ordre 7, sous le rayon 0.03. Le tableau exhaustif ajoute en
  v6 le disait correctement dix lignes plus haut ; le paragraphe de motif
  n'avait pas suivi. C'est ce point, et lui seul, qui retenait le tampon de
  v7 -- certifier aurait fait entrer un enonce faux dans un artefact
  opposable, ce qui est exactement la genese d'E23.
  (2) P-M10a, incise "calcule sur les 11 points" : le fit en a 10. Les
  nombres qui suivent etaient DEJA ceux du fit corrige ; seule la phrase
  etait restee en arriere. Elle n'est pas cosmetique : c'est elle qui dit a
  un tiers sur quelle grille REFAIRE la derivation de la marge.
  (3) P-M10d, "cinq points hors fit" : ils sont six. Et le sixieme est le
  plus proche d'une resonance d'ordre <= 8 de toute la grille. Un NOTA le
  consigne, place A COTE de la lecture pre-declaree et non dedans : une
  lecture ne s'enrichit pas a l'occasion d'une correction de compte.
  CLASSIFICATION. Le critere employe pour D-M10-4, D-M10-6 et D-M10-8 --
  un script conforme au gel ne peut pas etre ecrit -- n'est PAS atteint :
  aucune de ces trois phrases n'est une instruction au script, et M10
  tournerait correctement sur v7. Defaut attrape AVANT certification, donc
  aucun numero d'erratum (regle D1, precedents v1 et v5) : E24 reste le seul
  erratum de la serie.
  CONSIGNE SANS SPAN, parce que sa place est dans le script et non dans le
  gel : machine 2 signale qu'un filtre sur la NULLITE du seuil n'attrape pas
  les trois cas de la clause "recherches sans seuil" -- DENSE_SANS_EXPLOSION
  rend un FLOTTANT, float(hi_d), accompagne de sa note. Le filtre doit porter
  sur la NOTE : seule une note commencant par "OK|" ouvre le droit d'entrer
  dans le fit. Encode comme cas de test PERMANENT du --selftest, au meme
  titre que les regressions connues.
  DIFF ANNONCE, cinq emplacements : EN-TETE, HISTORIQUE, PROTOCOLE DE FIT,
  P-M10a, P-M10d. Aucun recalcul, aucun nombre nouveau : les trois spans sont
  ceux fournis mot pour mot par machine 2.
  v7 (sur diff de v6, non certifiee) : corrige D-M10-7 et D-M10-8, tous deux
  dans IMPLEMENTATION, tous deux de la meme famille que D-M10-4 et D-M10-6 --
  une specification gelee que rien ne confronte a ce qu'elle decrit.
  D-M10-7, TRONCATURE DE L'EMPREINTE. Le terminateur du gel figurait DEUX
  fois dans le fichier : une fois cite entre guillemets dans IMPLEMENTATION,
  une fois en ligne de cloture. La convention "premiere occurrence" coupait
  donc l'empreinte mi-phrase, laissant cinq lignes hors perimetre, dont la
  clause qui conditionne le depot du script. VOIE (b), arbitree par machine 2
  et non par preference : elle a MESURE que changer le perimetre de facon
  retroactive casse la custody de M9 -- le gel M9 porte lui aussi deux
  occurrences, et l'empreinte stockee dans m9_results.json est celle de la
  convention en vigueur, pas celle d'un ancrage structurel. Reparer un angle
  mort en rendant non reproductible l'empreinte d'une manche opposable serait
  un mauvais echange. La v7 supprime donc l'ambiguite A LA SOURCE : la phrase
  d'IMPLEMENTATION ne cite plus le terminateur. Premiere occurrence =
  derniere = ligne de cloture, la convention publiee reste vraie mot pour
  mot, et l'empreinte couvre enfin la clause E19.
  INVARIANT MECANIQUE, exige par machine 2 en plus du rephrasage, parce
  qu'une correction doit etre verifiable et pas seulement faite : le
  terminateur n'apparait qu'UNE fois dans le fichier, en ligne pleine, et
  c'est la derniere ligne du bloc. Controle au --selftest AVANT tout calcul
  d'empreinte. Consigne au journal, sans re-annonce : les gels M6 a M10 v6
  portent une empreinte tronquee de cinq lignes ; le hors-empreinte est
  verifie identique en v4, v5 et v6 ; l'invariant vaut a partir de v7.
  D-M10-8, LE MOTEUR NE PREND PAS p EN PARAMETRE. La clause disait "repris
  de m9_replication_v1.py sans modification (p parametre)". Or p n'est pas
  un parametre dans M9 : c'est la globale de module P = 5, lue par
  grad_explicite et grad_rapide, donc par integrer et chercher_seuil.
  Litteralement : ou l'on modifie le moteur et "sans modification" tombe, ou
  on le prend tel quel et "p parametre" tombe. Trouve independamment par les
  deux machines dans la meme fenetre, a partir du meme fichier. Resolution
  identique des deux cotes : IMPORT du module et REBINDING de la globale,
  fichier non touche -- "sans modification" devient verifiable par empreinte
  a chaque run, ce qu'une copie ne permet pas.
  CONSEQUENCE SUR G3, relevee par machine 2 et acceptee par machine 1 :
  garde_G3 compare grad_explicite a grad_rapide, qui lisent toutes deux P.
  Une execution unique de G3 ne verifie donc l'identite de force QU'AU DEGRE
  ALORS CHARGE, et le second degre tournerait avec une garde a metrique
  obligatoire non verifiee. G3 est donc executee APRES CHAQUE REBINDING.
  Executer une garde bloquante deux fois au lieu d'une ne relache aucune
  exigence : la section GARDES n'est pas rouverte.
  AJOUT MACHINE 1, meme raisonnement : chercher_seuil peut ne rendre AUCUN
  seuil (ECHEC_HAUT, ECHEC_BAS) ou une passe dense sans explosion. G5
  n'excluait que les recherches dont le pas final depasse 1e-5 ; une
  recherche qui ne rend aucun pas n'etait ni couverte ni exclue. La clause
  ci-dessous l'exclut explicitement. Elle DURCIT G5 sans la relacher, donc
  elle est declaree ici plutot que dans GARDES, par le meme argument que
  machine 2 emploie pour G3. Si machine 2 prefere qu'elle vive dans G5, cela
  coute un quatrieme emplacement et machine 1 s'y range.
  DIFF ANNONCE, trois emplacements : EN-TETE, HISTORIQUE, IMPLEMENTATION.
  Le contenu de v6 est repris tel quel, sans une virgule de changement.
  Aucun numero d'erratum nouveau : D-M10-7 et D-M10-8 sont attrapes avant
  toute execution et avant la certification de v6, qui n'a jamais ete
  posee. E24 (D-M10-6) reste le seul erratum de la serie.
  v6 (post-certification v5, sur diff) : correction de D-M10-6 -- ERRATUM
  E24, defaut entre dans un artefact CERTIFIE (precedent E23, regle D1).
  L'ENSEMBLE DE FIT enumere contenait w2 = 1.35, que la REGLE D'EXCLUSION
  gelee dans le meme paragraphe met HORS FIT : 1.35 est a 0.0167 de la
  resonance 4:3, d'ordre 7, et le rayon d'ordre 7-8 vaut 0.03. Les deux
  specifications de l'ensemble de fit, toutes deux gelees, etaient donc
  INCOMPATIBLES, et aucun script conforme ne pouvait etre ecrit.
  CAUSE : la regle (R-2, adoptee en v2) n'a jamais ete appliquee de facon
  EXHAUSTIVE. Le gel verifiait sqrt(2), 1.70 et 2.45 -- les trois cas
  limites auxquels on avait pense -- et jamais 1.35 contre 4:3. Meme
  famille que E14 et E23, et meme forme que D-M10-4 : un ensemble gele non
  confronte a la regle gelee qui le definit. Manquement partage : machine 1
  a redige, machine 2 a certifie v2 a v5, et l'auto-audit v5 de machine 1
  testait l'appartenance du sous-ensemble a la GRILLE (regle 11) sans
  jamais confronter le FIT a la regle d'exclusion.
  CORRECTION, voie unique : la regle est MECANIQUE et la campagne
  n'admet aucune exception ; 1.35 passe donc HORS FIT. Fit 11 -> 10 points,
  hors fit 5 -> 6. Le point reste MESURE aux deux degres et aux deux
  signes : G1, P-M10e et P-M10f ne sont pas affectes, et le PROGRAMME FIGE
  ne bouge pas d'une recherche. Le sous-ensemble de P-M10f garde 1.35, qui
  n'a jamais eu besoin d'appartenir au fit.
  CE QUI BOUGE, tout par re-evaluation de la MEME formule sur le fit
  corrige, aucune formule reecrite : Sxx 8.8403 -> 7.4425 (-15.8 %) ; le
  seuil sigma de P-M10a, sigma_max = marge x sqrt(Sxx)/1.96, 0.1517 ->
  0.1392 ; le contre-exemple R-5 a marge 0.05, 0.0758 -> 0.0696 ; les SE
  projetees des ATTENTES, ~0.015/~0.039 -> ~0.017/~0.043.
  CE QUI NE BOUGE PAS, verifie : la MARGE 0.10 et sa derivation. Les trois
  beta_eff concurrents valent 1.0000 / 0.6513 / 0.4990 sur le fit corrige
  contre 1.0000 / 0.6513 / 0.4982 sur l'ancien ; l'ecart au concurrent le
  plus proche reste 0.3487 et le facteur de separation 3.49. La marge
  n'etait donc pas ajustee sur la grille, et c'est un point en sa faveur.
  CONSEQUENCE DECLAREE : G7 rend P-M10a et P-M10b NON CONCLUANTES sous 8
  points de fit. La marge d'exclusions absorbables passe de 3 a 2.
  DIFF ANNONCE, cinq emplacements : EN-TETE, HISTORIQUE, PROTOCOLE DE FIT,
  P-M10a, MES ATTENTES. Aucune autre porte, aucune autre garde, aucun autre
  seuil ne bouge. P-M10b, P-M10d, P-M10e, P-M10f, G1 a G7 et le PROGRAMME
  FIGE sont intacts.
  v5 (post-suspension v4, sur diff) : correction du seul defaut releve a
  l'audit v4 -- D-M10-4. Le sous-ensemble historique de P-M10f contenait
  w2 = 2.40, ABSENT de la grille des 16 points que M10 mesure (elle porte
  2.45 a la place) : l'instruction (i) etait INEXECUTABLE telle qu'ecrite,
  et pas seulement non comparable comme en v3. Un script conforme au gel ne
  pouvait pas etre ecrit. Voie (b) de machine 2 ADOPTEE : sous-ensemble
  ramene aux quatre points reellement communs, repere porte de 0.2836 a
  0.2230, portee de (i) declaree, consignation de l'argmax de d ajoutee,
  etendue a cinq points conservee comme donnee d'archive.
  VOIE (a) ECARTEE ET MOTIVEE : ajouter 2.40 a la grille le ferait tomber
  DANS l'ensemble de fit -- 2.40 est a 0.10 de 5:2 (ordre 7) et le rayon
  d'ordre 7-8 vaut 0.03 -- portant le fit de 11 a 12 points, changeant Sxx,
  donc les SE de P-M10a et le seuil sigma = 0.1517. Cout reel tres
  superieur a son apparence.
  AUCUNE porte, aucun seuil, aucune garde, aucun ensemble de fit ne bouge :
  P-M10f reste une consignation. DIFF ANNONCE, quatre emplacements :
  l'EN-TETE (marqueur de version, 1 ligne), HISTORIQUE, P-M10f, MES
  ATTENTES. L'en-tete est signale explicitement parce qu'il sort des trois
  emplacements annonces au correctif : un fichier v5 portant "version v4"
  serait lui-meme un defaut.
  Aucun numero d'erratum : defaut attrape AVANT certification (precedent
  v1, regle D1) ; a promouvoir par machine 2 si elle juge autrement.
  v4 (post-certification v3, sur diff) : correction du seul defaut releve a
  la certification v3 -- P-M10f definissait sa statistique avec une
  normalisation (rho_p = s*_p(w)/s*_p(1.25)) alors que son repere
  pre-declare etait calcule a w0 = 1.35, et que la statistique DEPEND du
  point de normalisation (0.2224 a 0.2836 selon w0, 27 % d'ecart). Defaut
  de machine 1, entre dans un artefact CERTIFIE : erratum E23 (S30). La
  correction adopte la version SANS normalisation, conformement a
  l'argument qui avait motive P-M10f. AUCUNE porte, aucun seuil, aucun
  ensemble de fit, aucune garde ne bouge : P-M10f est une consignation.
  v3 (post-certification v2, sur diff) : la reserve R-5 de machine 2 est
  ACCEPTEE, et la marge d'equivalence de P-M10a passe de 0.05 a 0.10 --
  non par convenance, mais par DERIVATION (voir P-M10a). S'y ajoutent : la
  declaration que sigma est de l'inadequation de modele et non du bruit
  (consequences sur la lecture de l'intervalle et sur celle d'un NON
  CONCLUANT), une consignation sans porte de la forme de la carte (P-M10f),
  et le nettoyage des six coquilles signalees au S5 de la certification v2.
  AUCUNE autre porte, aucun autre seuil, aucun ensemble de fit ne bouge.
  AUCUN code avant qu'un message de certification croisee cite l'empreinte de
  ce bloc (E19). Le script s'appellera m10_exposant_v1.py.
  **C2 NE S'APPLIQUE PAS** : M10 est integralement CLASSIQUE. Aucun
  diagonalisation, aucun T_shell, aucun rho quantique. La clause de
  rearmement (D3/C2) interdit une manche QUANTIQUE sans estimateur derive ;
  elle ne bloque pas le programme classique, qui est explicitement nomme
  comme voie ouverte au S26.

QUESTION
--------
Le S27 demontre exactement : (i) le systeme se reduit a
(dt^2+w1^2)(dt^2+w2^2)x = g x^(p-1) avec x(0)=x''(0)=s, x'(0)=x'''(0)=0
(verifie a 1e-13 par integration independante) ; (ii) K = g s^(p-2) est
l'unique parametre, donc s* = (K*(w2;p)/g)^(1/(p-2)) et l'invariance en g
est DERIVEE (verifiee a 0.5-1.4 % sur deux decades) ; (iii) par consequent
r(p) = [Delta(2.85)/Delta(1.35)]^beta = 8.6596^beta.
Tout le contenu empirique de  r quasi-constant  tient donc dans UN
exposant : s* = kappa_p Delta^beta(p), Delta = w2^2 - w1^2. Les valeurs
disponibles (5 points par degre au mieux, provenance mixte) donnent
beta = 1.32 / 0.95 / 1.02 / 0.88 / 0.91 pour p = 3..7, avec des residus de
-15 a +11 % qui ne separent pas courbure et bruit.
M10 MESURE beta sur grille dense, en convention (f), a provenance unique.
**M10 ne derive pas beta** : elle etablit ce qu'une derivation devra
reproduire. C'est dit d'avance pour qu'aucun resultat ne soit presente
comme une explication.

DERIVATIONS PREALABLES (faits, verifies avant gel -- trace S27)
---------------------------------------------------------------
(a) Reduction et CI : verifiees dynamiquement, ecart 9.6e-14 / 7.7e-14 /
    6.0e-14 sur trois couples (w2, p).
(b) E0 = -Delta s^2/2 ; energie totale conservee a 1.2e-12.
(c) K invariant : dispersion 0.53 % (p=5, w2=1.80) et 1.42 % (p=7, w2=2.40)
    sur g = 0.005 / 0.05 / 0.5. **Consequence gelee : aucun volet
    d'invariance en g n'est reconduit dans M10 au-dela de G2** -- re-tester
    a x100 ce qui est verifie a 1e-13 par la reduction serait du temps
    machine gaspille. G2 (x2, 3 points) est conserve comme garde de
    regression, pas comme test de la loi.
(d) Convention (f) INTEGRALE : s* = min(s*(+1), s*(-1)) partout, asymetries
    consignees, aucune porte dessus. Justification : le cote fragile n'est
    uniforme ni en w2 ni en p (inversion mesuree a w2=1.80 pour p=5 ET p=7 ;
    frag=+1 sauf a 2.85 pour p=3).

PROTOCOLE DE FIT, GELE AVANT MESURE
-----------------------------------
beta(p) = pente de la regression lineaire ordinaire de ln s* sur ln Delta,
sans ponderation, sur l'ENSEMBLE DE FIT ci-dessous et lui seul. Aucun point
n'est retire apres coup, aucune ponderation n'est introduite, aucune forme
non lineaire n'est ajustee. L'incertitude reportee est l'erreur standard de
la pente OLS.

  RAYON D'EXCLUSION DEPENDANT DE L'ORDRE (R-2) : hors fit si a moins de 0.12
  d'une resonance k/l d'ordre k+l <= 6, ou a moins de 0.03 d'une resonance
  d'ordre 7 ou 8 ; au-dela de l'ordre 8, aucun rayon.
  ENSEMBLE DE FIT (10 points) :
    1.25, 1.30, 1.70, 1.80, 2.15, 2.30, 2.45, 2.60, 2.75, 2.85
  ENSEMBLE HORS FIT (6 points, mesures et CONSIGNES, jamais dans le fit) :
    1.35, 1.4142135623730951, 1.45, 1.55, 1.90, 2.05
  APPLICATION EXHAUSTIVE DE LA REGLE, POINT PAR POINT (correction E24).
  Les seules resonances k/l irreductibles d'ordre k+l <= 8 de l'intervalle
  sont 4:3 (o.7), 3:2 (o.5), 5:3 (o.8), 2:1 (o.3) et 5:2 (o.7). Exclusions
  prononcees, avec leur distance :
    1.35   a 0.0167 de 4:3, ordre 7 < 0.03   -> HORS FIT  [E24]
    sqrt2  a 0.0858 de 3:2, ordre 5 < 0.12   -> HORS FIT
    1.45   a 0.0500 de 3:2, ordre 5 < 0.12   -> HORS FIT
    1.55   a 0.0500 de 3:2, ordre 5 < 0.12   -> HORS FIT
    1.90   a 0.1000 de 2:1, ordre 3 < 0.12   -> HORS FIT
    2.05   a 0.0500 de 2:1, ordre 3 < 0.12   -> HORS FIT
  Restent DANS le fit, verifies un par un : 1.30 (0.0333 de 4:3 > 0.03),
  1.70 (0.0333 de 5:3 > 0.03), 2.45 (0.0500 de 5:2 > 0.03), et 1.25, 1.80,
  2.15, 2.30, 2.60, 2.75, 2.85, hors de portee de tout rayon.
  Le --selftest du script REFAIT ce tableau et compare a l'enumeration
  ci-dessus ; un desaccord est une erreur bloquante (regle 11, esprit).
  CONSIGNE, aucune porte : w2 = 1.25 est EXACTEMENT 5:4, resonance d'ordre
  9, donc hors de tout rayon PAR LA REGLE, qui ne pose aucun rayon au-dela
  de l'ordre 8. Il reste dans le fit. Mais c'est le point de plus grand
  levier du fit et il est assis sur une resonance : P-M10d doit etre lue en
  le sachant, et un residu anormal a 1.25 n'aura pas la meme valeur qu'un
  residu anormal ailleurs.
  CLARIFICATION (machine 2, S8) : le eps = 0.15 du S27.3 est la DISTANCE a la
  resonance dans un mecanisme candidat MORT, pas une demi-largeur mesuree.
  Aucun conflit avec les rayons ci-dessus.
  Motif de la separation, declare : CINQ des six points hors fit encadrent
  les resonances k/l d'ordre k+l <= 6 presentes dans l'intervalle (3:2 = 1.5
  et 2:1 = 2.0) a moins de 0.12. Le sixieme, 1.35, sort pour un motif
  DIFFERENT, et le tableau exhaustif ci-dessus le donne : 0.0167 de 4:3,
  resonance d'ordre 7, sous le rayon 0.03 (correction E24). Le motif de
  separation n'est donc pas unique, et c'est la regle -- non ce paragraphe --
  qui fait foi. Le point 2.00 lui-meme n'est pas mesure : son
  canyon est deja cartographie (M5/M6). Les points 1.70 et 2.45, proches de
  5:3 et 5:2 (ordre 8), sont DANS le fit -- c'est P-M10d qui regarde s'ils
  s'en detachent.

PORTES
------
P-M10a  beta VAUT-IL 1 ? -- TEST D'EQUIVALENCE, MARGE DERIVEE 0.10
  DERIVATION DE LA MARGE (v3, remplace le 0.05 herite de v1) : la marge doit
  etre assez fine pour DISCRIMINER entre les lectures physiques concurrentes,
  pas plus. Chaque candidat d'invariant impose un beta effectif sur la grille
  de fit (calcule sur les 10 points du fit corrige E24, exact) :
      A2 = 2s/Delta constant  (mode SAIN)      -> beta_eff = 1.000
      max|x| constant                          -> beta_eff = 0.651
      A1 constant             (mode FANTOME)   -> beta_eff = 0.499
  Le concurrent le plus proche est a 0.3487. Une marge de 0.10 laisse un
  facteur 3.5 de separation : elle discrimine sans ambiguite. Une marge de
  0.05 est SEPT fois plus fine que ce que la discrimination exige, et machine
  2 montre (R-5) qu'elle rend la branche affirmative inatteignable a p=5
  (elle exigerait sigma < 0.0696 quand sigma mesure vaut 0.1168). La marge
  0.10 est donc fixee par l'ecart entre hypotheses, non par le bruit
  disponible -- c'est la seule facon de la choisir sans deplacer les poteaux.
  IC 95 % de beta (beta +- 1.96 SE, SE = erreur standard OLS de la pente)
  CONTENU dans [0.90, 1.10] AUX DEUX degres -> LOI s* ~ Delta CONFIRMEE.
    [derivation : beta = 1 <=> A2 = 2s/Delta constant au seuil, i.e. le seuil
     est fixe par l'amplitude initiale du mode d'energie POSITIVE, non par
     celle du fantome ni par max|x| -- ces trois lectures sont exclusives.]
  IC 95 % DISJOINT de [0.85, 1.15] a l'un ou l'autre degre -> LOI REFUTEE.
  DECLARATION OBLIGATOIRE SUR LA NATURE DE L'INTERVALLE : la precision de
  mesure de s* est de ~1e-6 en relatif (pas final 6e-7), tandis que sigma
  observe vaut 0.1168 (p=5) et 0.0455 (p=7) -- CINQ ordres de grandeur
  au-dessus. sigma n'est donc PAS du bruit d'echantillonnage : c'est
  l'inadequation de la loi de puissance elle-meme. En consequence
  l'intervalle ci-dessus n'est pas un intervalle de confiance
  d'echantillonnage mais une BANDE DE DISPERSION du plan, et il est lu comme
  tel. C'est aussi pourquoi beta depend de la grille (limitations, R-4).
  LECTURE OBLIGATOIRE D'UN NON CONCLUANT (diagnostic, sur le modele du G7 de
  M9) : reporter SE et sigma par degre, et trancher mecaniquement --
    sigma > 0.1392 a un degre  -> NON CONCLUANT DE PUISSANCE : le plan ne
      permettait pas de conclure, aucune lecture physique n'est autorisee ;
    sigma <= 0.1392 aux deux    -> NON CONCLUANT DE PHYSIQUE : beta differe
      reellement de 1 a la precision du plan, et c'est un resultat.
    [derivation de CETTE branche : un exposant franchement different de 1
     detruit la lecture  mode sain  et impose de chercher l'invariant
     ailleurs ; la cible de la derivation change.]
  Entre -> NON CONCLUANT.

P-M10b  beta EST-IL INDEPENDANT DU DEGRE ? (le contenu reel de  r constant )
  |beta(5) - beta(7)| <= 0.08 -> P-INDEPENDANCE COMPATIBLE.
  |beta(5) - beta(7)| >= 0.20 -> REFUTEE : la constance de r sur p >= 4 est
    une coincidence des deux bords choisis, et r doit etre abandonne comme
    statistique.
  Entre -> NON CONCLUANT.

P-M10c  SUPPRIMEE. La question << beta(3) est-il anormal ? >> est MAL POSEE
  tant que s*(p=3) n'est pas defini par un protocole (D-M10-1). Reportee a une
  manche dediee, qui devra d'abord FIXER une definition du seuil sur un
  ensemble d'explosion crible (candidats NON geles ici : infimum a resolution
  declaree ; premiere explosion de mesure superieure a un seuil de densite ;
  amplitude a probabilite d'explosion 1/2). Consequence consignee au S28
  (E22) : r(3) = 17.48 et beta(3) = 1.32 ne sont pas des nombres defendables ;
  l'enonce ORDINAL p=3 tres au-dessus des autres degres survit largement.

P-M10d  STRUCTURE DES RESIDUS (consigne, AUCUNE porte)
  Residus du fit par point, aux deux degres. Lecture PRE-DECLAREE, qui
  n'engage rien : si les residus les plus negatifs se localisent aux w2 les
  plus proches des k/l d'ordre <= 8 (1.70 pres de 5:3 ; 2.45 pres de 5:2 ;
  et les six points hors fit), la deviation a la loi est resonante et
  chaque resonance creuse son propre canyon. Sinon, la deviation est une
  courbure lisse et la loi en puissance est incomplete. Les deux lectures
  sont ecrites ici ; aucune ne sera choisie apres coup sans le dire.
  NOTA CONSIGNE AVANT MESURE, consequence non declaree d'E24 : le passage de
  1.35 hors fit RENFORCE cette lecture. 1.35 est a 0.0167 de 4:3, contre
  0.0333 pour 1.70 et 0.0500 pour 2.45 : c'est le point le plus proche d'une
  resonance d'ordre <= 8 de toute la grille, et il est desormais hors fit,
  donc son ecart a la loi se lit contre une EXTRAPOLATION du fit plutot que
  contre un fit qui le contient. La lecture resonante y gagne son meilleur
  temoin ; c'est dit avant de mesurer. Consignation, aucune porte.
  Nota consigne d'avance : le residu de -15 % deja vu a w2=1.80 (p=5) tombe
  au point ou le cote fragile s'inverse. Coincidence ou structure : M10 aura
  1.70, 1.80 et 1.90 pour trancher.

P-M10e  ASYMETRIE DE SIGNE (consigne, AUCUNE porte)
  r_s = s*(+1)/s*(-1) et le cote fragile aux 16 points x 2 degres. Le
  S26-bis a etabli que r_s est invariant en g, et le S28.4 l'a DERIVE (les
  deux signes sont les seuils de +-K du meme probleme reduit) ; M10 en donne
  la carte en w2. Materiau pour la derivation de r et pour la loi C.

P-M10f  FORME DE LA CARTE, SANS AJUSTEMENT NI NORMALISATION (consigne,
  AUCUNE porte -- v5)
  Statistique : d(w) = ln s*_5(w) - ln s*_7(w) sur les points communs aux
  deux degres, et ETENDUE(d) = max d - min d. Ni ajustement, ni point de
  reference : la statistique ne comporte AUCUN degre de liberte de
  convention. C'est la correction du defaut E23 -- la version v3 fixait un
  point de normalisation, ce qui contredisait l'argument meme qui motivait
  P-M10f (aucun ajustement, donc rien a choisir).
  PROPRIETE, verifiee : etendue(d) = sup sur w0 de max_w |ln rho_5 - ln
  rho_7| avec rho_p = s*_p(w)/s*_p(w0). La version sans normalisation est
  donc l'ENVELOPPE CONSERVATRICE de toute la famille normalisee -- elle ne
  choisit pas une convention, elle les majore toutes.
  MONOTONIE, declaree : l'etendue CROIT mecaniquement avec le nombre de
  points (max moins min sur un sur-ensemble ne peut que grandir). Comparer
  une etendue a 16 points a un repere a 5 points serait biaise vers le haut.
  M10 rapporte donc DEUX valeurs : (i) sur le SOUS-ENSEMBLE HISTORIQUE
  COMMUN A LA GRILLE M10, {1.35, sqrt(2), 1.80, 2.85} -- 2.40 est ecarte
  parce que M10 mesure 2.45 et non 2.40 ; le point n'est pas substituable,
  d y ayant un extremum (d monte de +0.2796 de 1.80 a 2.40, puis redescend
  de -0.0606 de 2.40 a 2.85) -- seule comparable au repere ci-dessous ;
  (ii) sur les 16 points mesures, a cote, sans comparaison.
  REPERE PRE-DECLARE, sur le sous-ensemble historique commun (M9 et
  consignation S24) : d(w) = 0.3031 / 0.2420 / 0.2460 / 0.4649, min a
  sqrt(2), max a 2.85, ETENDUE = 0.2230. Le profil est PLAT A GAUCHE et
  saute A DROITE ; le r a deux points n'affiche que 15 % d'ecart entre
  degres. Si M10 reproduit ce motif, la constance de r masque une
  difference de forme reelle, et P-M10b devra etre lue avec cette reserve.
  Aucune porte : c'est une mesure, pas un verdict.
  DONNEE D'ARCHIVE, sans comparaison : l'etendue a CINQ points de
  l'historique, 2.40 inclus, vaut 0.2836. Elle reste vraie ; elle n'est
  simplement plus le repere. 2.40 n'etant pas mesure par M10, elle ne sera
  jamais repliquee en provenance unique -- perte acceptee et consignee.
  PORTEE DE (i), DECLAREE AVANT MESURE. Le sous-ensemble commun est
  exactement la liste de points de G1, et il ne peut pas en etre autrement :
  les deux sont l'intersection de la grille historique et de la grille M10.
  Si G1 passe a +-2 % par signe, alors |d_M10 - d_hist| <= 0.0404 en chaque
  point, et l'etendue mesuree est confinee a 0.2230 +- 0.0808, soit
  [0.1422, 0.3038], AVANT toute physique. (i) est donc une statistique de
  REPLICATION, bornee par une garde bloquante qui teste la meme chose plus
  finement -- point par point et par signe ; ce n'est PAS une statistique
  de FORME. Aucune lecture de forme ne sera tiree de (i), quel que soit le
  nombre qu'elle rende. La lecture de forme est (ii), qui n'a pas de repere
  et n'en aura pas.
  LOCALISATION DU MAXIMUM DE d, PRE-DECLAREE (consignation, aucune porte).
  L'historique donne d(1.80) = 0.2460 < d(2.40) = 0.5255 > d(2.85) = 0.4649 :
  le maximum de d est INTERIEUR a (1.80, 2.85). La grille M10 echantillonne
  cet intervalle en 1.90 / 2.05 / 2.15 / 2.30 / 2.45 / 2.60 / 2.75.
  Consigner l'argmax de d sur les 16 points. Lecture ecrite d'avance : un
  argmax dans {2.30, 2.45, 2.60} confirme que le pic historique a 2.40 est
  un trait de la carte et non un artefact de grille creuse ; un argmax hors
  de cet ensemble etablit l'inverse, et retire retroactivement tout sens au
  repere a cinq points.

GARDES
------
  G1 REGRESSION (bloquante) : aux points communs, s* de M10 contre les
    valeurs etablies, tolerance +-2 % PAR SIGNE.
      p=5, 1.35 / 1.4142 / 1.80 / 2.85 : carte M9 (sP et sM).
      p=7, 1.35 / 1.4142 / 1.80 / 2.85 : sP = M7, sM = consignation S24.
    Echec -> ARRET, investigation.
  G2 INVARIANCE (regression, pas test de loi) : K a 2g sur w2 = 1.35, 1.80,
    2.85 pour p=5, deux signes, tolerance 10 % ; echec -> ligne EXCLUE du fit
    et consignee.
  G3 IDENTITE DE FORCE : erreur BACKWARD <= 1e-12 (metrique obligatoire).
  G4 PAS DE TEMPS : dt/2 sur la ligne maximisant g s*^(p-1) ; ecart <= 2 %
    sinon ligne NON FIABLE (et EXCLUE du fit, consignee).
  G5 QUALITE DE BRACKET : passe dense n = 96 partout ; pas final consigne ;
    toute recherche dont le pas final depasse 1e-5 est EXCLUE du fit.
  G6 PRIMAUTE DE s* (NOUVELLE, bloquante ligne par ligne -- correctif
    D-M10-1) : apres la passe dense, re-balayer [LO0, 1.05 s*] a n = 192 avec
    le meme integrateur. Si une explosion est trouvee sous 0.98 s*, alors s*
    n'est PAS la plus petite amplitude explosive : ligne EXCLUE du fit et
    consignee avec la valeur inferieure trouvee.
    [derivation : chercher_seuil suppose que {s : explose} est une
     demi-droite ; D-M10-1 montre que c'est faux a p=3. G6 teste exactement
     cette hypothese, ligne par ligne, y compris aux points neufs jamais
     mesures.]
    CONSIGNE SANS PORTE : nombre d'ilots et position de la premiere retombee
    dans [s*, 1.3 s*] -- le bord est crible partout (1.000 s* et 1.001 s*
    mesures), c'est le rivage fractal connu, il ne ferme aucune porte.
  G7 REPERCUSSION DES EXCLUSIONS (correctif D-M10-3, cout machine nul) :
    toute exclusion prononcee par G2, G4, G5 ou G6 a UN degre retire le meme
    w2 du fit a TOUS les degres entrant dans une porte comparative. Les fits
    ampute et non ampute sont consignes ; SEUL l'ampute alimente les portes.
    Si l'amputation fait descendre un degre sous 8 points, P-M10a et P-M10b
    sont NON CONCLUANTES par construction. La liste des w2 retenus PAR DEGRE
    va au JSON.

PROGRAMME FIGE
--------------
  p=5 : 16 points x 2 signes = 32
  p=7 : 16 points x 2 signes = 32
  p=3 : RETIRE (D-M10-1 : s* non defini par le protocole a ce degre).
  G2 : 3 points x 2 signes = 6 ;  G4 : 1
  G6 monotonie : 1 balayage n = 192 par ligne mesuree = 64
  Total 71 recherches completes + 64 balayages G6, passe dense n = 96 partout.
  Cout annonce : ~35-50 min machine 2 (25 s par recherche mesures a p=5 et
  p=7 ; p=3 est retire, cf. HISTORIQUE).

MES ATTENTES (pour pouvoir avoir tort de mon propre fait)
  beta(5) et beta(7) dans [0.88, 1.05], donc P-M10a plus probablement NON
  CONCLUANT que CONFIRME -- je l'ecris avant. |beta(5)-beta(7)| <= 0.08.
  Residus les plus negatifs a 1.80 et pres des points hors fit. Erreur
  standard sur beta, projetee sur les 10 points du fit (Sxx = 7.4425) :
  ~0.017 (p=7) a ~0.043 (p=5). J'attends donc P-M10a NON CONCLUANT DE
  PHYSIQUE, tire par beta(7) ~ 0.89.
  P-M10f, DEUX ATTENTES DISTINCTES.
  (i) La remise a l'echelle mecanique de l'attente v4 (0.25-0.32 pour un
  repere de 0.2836) par 0.2230/0.2836 = 0.7863 donne 0.197-0.252. Mais
  cette attente est ecrite APRES avoir appris que le repere baissait de
  21.4 % : elle est contaminee, et je le declare. L'attente que je defends
  est celle qui ne depend pas du repere -- G1 passera nettement sous 1 %
  (reproductibilite bit-a-bit constatee au S26-bis), donc (i) tombera dans
  [0.183, 0.263], et le plus probablement dans [0.203, 0.243]. Une valeur
  hors [0.142, 0.304] signifierait que G1 a echoue, donc ARRET par G1 avant
  toute lecture de P-M10f.
  (ii) Sur 16 points, j'attends une etendue STRICTEMENT SUPERIEURE a (i),
  pour deux causes cumulees et non separables : le nombre de points
  (monotonie) et l'echantillonnage du maximum interieur, que les quatre
  points communs manquent par construction. J'attends 0.35-0.60 ; une
  etendue (ii) inferieure a 0.30 serait contre moi.
  ARGMAX de d : j'attends 2.45, avec 2.30 et 2.60 comme voisins plausibles.
  Un argmax a 1.90 ou 2.05 -- c'est-a-dire colle au canyon -- serait contre
  moi et demanderait une manche.
  Je n'ai AUCUNE attente sur la forme des residus (courbure vs resonances) :
  c'est la vraie inconnue de la manche.

LIMITATIONS DECLAREES
  - M10 mesure, ne derive pas. Un beta precis ne devient une explication
    qu'accompagne d'un mecanisme, et les deux candidats naturels sont morts
    (S27.3).
  - Une loi en puissance pure est une HYPOTHESE de forme ; P-M10d peut la
    contredire sans qu'aucune porte ne le dise -- ce serait alors le
    resultat le plus interessant de la manche, et il faudrait une manche
    nouvelle pour le geler.
  - beta(4) et beta(6) ne sont PAS refaits ici : provenance mixte, convention
    non confirmee (E20). M10 ne prononce rien sur eux.
  - beta DEPEND DE LA GRILLE (R-4) : machine 2 mesure beta(5) = 1.0230 sur la
    grille M9 (5 points) contre 0.9806 sur la grille M10 projetee, et
    beta(7) = 0.9109 contre 0.8896. Sous une forme qui n'est pas une puissance
    pure, beta est une propriete de la grille autant que du systeme : les
    valeurs de M10 ne sont comparables qu'a elles-memes.
  - DECLARATION : machine 1 a mesure hors gel, en verifiant D-M10-1, la
    premiere amplitude explosive a six points neufs sur balayage grossier
    (p=5 : 0.23617 / 0.97340 / 2.26170 a 1.25 / 2.15 / 2.60 ; p=7 : 0.17660 /
    0.72766 / 1.41277 aux memes). Ces valeurs n'ont servi qu'a tester la
    faisabilite de G6 ; elles n'ont ajuste aucun seuil, aucune porte, aucun
    ensemble de fit.
  - Le point w2 = 2.00 n'est pas mesure : hors sujet pour beta, deja
    cartographie comme canyon.
  - Tout est a w1 = 1, g = 0.05, sgn des deux cotes, RK4 dt = 0.006, T = 400,
    cap 1e4 -- protocole de la lignee, inchange.

IMPLEMENTATION
  m10_exposant_v1.py ecrit uniquement out/m10_results.json (incremental, une
  ecriture apres chaque point).
  MOTEUR (clause D-M10-8). Le moteur classique est celui de
  m9_replication_v1.py, sha256 c8ed357b120352c4d1078307add3eaac285940c8bec
  00acc2ddc9ff386ab2c5c, IMPORTE et NON MODIFIE : le script recalcule cette
  empreinte au demarrage et s'arrete si elle differe. Le degre est fixe par
  REBINDING de la globale de module P avant chaque bloc de degre -- p est un
  parametre DU RUN, non de la fonction, et le fichier moteur n'est touche
  d'aucun octet. La valeur de P au moment de chaque mesure va au JSON. Les
  deux symboles employes sont integrer(w2, s_arr, sgn, dt, g), oracle
  d'explosion vectorise, et chercher_seuil(w2, sgn, dt, g) -> (s*, note).
  Les onze autres globales du moteur sont deja aux valeurs de ce gel et ne
  sont pas rebindees : W1 1.0, G_REF 0.05, DT 0.006, T_MAX 400.0, CAP 1e4,
  NDENSE 96, LO0 0.05, HI0 6.0, MAX_ELARG 8, NGRID 48, NPASSES 3.
  G3 APRES CHAQUE REBINDING. grad_explicite et grad_rapide lisent P : une
  execution unique de G3 ne verifierait l'identite de force qu'au degre
  alors charge. G3 est donc executee une fois PAR DEGRE, apres rebinding, et
  les deux erreurs backward vont au JSON. La section GARDES n'est pas
  modifiee : une garde bloquante executee deux fois n'est pas relachee.
  RECHERCHES SANS SEUIL. Une recherche qui ne rend pas de seuil (ECHEC_HAUT,
  ECHEC_BAS) ou dont la passe dense n'explose pas (DENSE_SANS_EXPLOSION) est
  EXCLUE du fit au meme titre qu'une recherche dont le pas final depasse le
  seuil de G5, et repercutee par G7. Le motif est consigne au JSON. Cette
  clause DURCIT G5 sans la relacher.
  ANCRES DE G1, lues de sources primaires et jamais codees en dur ; leur
  empreinte est verifiee avant lecture :
    p=5, sP et sM : out/m9_results.json, resultats.carte, sha256 41595413
      f676df396994da1b7ca6c4abc59199b8ca2f93f00e2643c151653210
    p=7, sP : out/m7_results.json, resultats.classique, sha256 b7493af743bd
      1c9bf80e11292edfd501540e3a5549d984ac12950c8e6e1df24e
    p=7, sM : journal_delta_24_D3.md section 24, sha256 c6395480d7f8adb39a
      2b74aa1b6f11dcfdf68b535d758a04633b96266001c3ce
  LIMITATION DECLAREE : l'ancre sM a p=7 n'a pas de JSON. Sa source primaire
  est une consignation a CINQ DECIMALES, soit une quantification de 5e-6
  absolu, ~2e-5 en relatif au pire point -- mille fois a l'interieur de la
  tolerance +-2 % de G1, qui n'en est pas affectee. Elle est neanmoins de
  precision inferieure a l'ancre sP, et cela est ecrit.
  GEL JUMEAU. Le docstring du script porte le bloc de pre-enregistrement, du
  titre du gel jusqu'a sa ligne de fin incluse, canonique NFC+LF, EXTRAIT du
  fichier .md et non retranscrit ; le sha256 en est recalcule au demarrage
  depuis le fichier source du script.
  INVARIANT DE CLOTURE (clause D-M10-7), verifie au --selftest AVANT tout
  calcul d'empreinte : la ligne de fin du gel n'apparait qu'UNE fois dans le
  fichier, en ligne pleine, et c'est la derniere ligne du bloc.
  DEPOT DU SCRIPT CONDITIONNE a la certification croisee (E19).

=== FIN DU GEL M10 ==="""

# =====================================================================
# m10_exposant_v1.py -- machine 1. Ecrit APRES la certification croisee de
# m10_pre_enregistrement_v8.md (E19). Le docstring ci-dessus est le GEL
# JUMEAU : il a ete EXTRAIT du .md par un script de generation, jamais
# retranscrit. Son empreinte est recalculee au demarrage depuis CE fichier.
#
# Marqueurs construits par concatenation (regle 12) : aucun d'eux
# n'apparait litteralement ailleurs dans ce source, donc aucun ne peut
# s'auto-capturer.
# =====================================================================

import argparse, hashlib, importlib.util, json, math, os, re, sys, unicodedata
from math import sqrt, log

import numpy as np

MARQ_DEBUT = "PRE-" + "ENREGISTREMENT M10"
MARQ_FIN = "=== FIN DU GEL M10 " + "==="

# ---- empreintes gelees (v8, certifiee) ------------------------------
SHA_GEL     = "c1d42aa51796b879fa5ca42f1dc20c5abd7fa45bd9076280f13a7499dcecba76"
SHA_MOTEUR  = "c8ed357b120352c4d1078307add3eaac285940c8bec00acc2ddc9ff386ab2c5c"
SHA_M9      = "41595413f676df396994da1b7ca6c4abc59199b8ca2f93f00e2643c151653210"
SHA_M7      = "b7493af743bd1c9bf80e11292edfd501540e3a5549d984ac12950c8e6e1df24e"
SHA_S24     = "c6395480d7f8adb39a2b74aa1b6f11dcfdf68b535d758a04633b96266001c3ce"

# ---- protocole de fit (gel v8, PROTOCOLE DE FIT) --------------------
SQ2 = sqrt(2.0)
FIT = [1.25, 1.30, 1.70, 1.80, 2.15, 2.30, 2.45, 2.60, 2.75, 2.85]
HORS_FIT = [1.35, SQ2, 1.45, 1.55, 1.90, 2.05]
GRILLE = sorted(FIT + HORS_FIT)
RAYONS = ((6, 0.12), (8, 0.03))      # (ordre max, rayon) ; rien au-dela de 8
TOL_APPART = 1e-6                    # regle 11 amendee : appartenance a la GRILLE
# TOL_ETIQUETTE est un objet DIFFERENT : elle rapproche une ETIQUETTE DE
# TABLEAU ("sqrt2", "1.80") d'une valeur de grille, pas une valeur mesuree
# d'un point gele. Deux tolerances, deux objets, toutes deux declarees.
TOL_ETIQUETTE = 1e-4
DEGRES = (5, 7)

# ---- portes et gardes (gel v8) --------------------------------------
MARGE = 0.10
BANDE_CONF = (0.90, 1.10)
BANDE_REFUT = (0.85, 1.15)
SIGMA_MAX = 0.1392
PM10B_COMPAT, PM10B_REFUT = 0.08, 0.20
# Les seuils du gel sont des litteraux DECIMAUX compares a des quantites
# calculees en flottant : |1.00-0.80| vaut 0.19999999999999996, donc une
# comparaison nue rendrait NON CONCLUANT la ou le gel ecrit REFUTEE.
# Tolerance de comparaison DECLAREE : 1e-12 -- un million de fois au-dessus
# du bruit flottant (1e-16) et un million de fois SOUS la resolution de beta
# (~1e-6, pas final 6e-7). Elle restitue la frontiere ecrite ; elle ne
# deplace aucune porte.
EPS_PORTE = 1e-12
G1_PTS = [1.35, SQ2, 1.80, 2.85]
TOL_G1 = 0.02
G2_PTS = [1.35, 1.80, 2.85]
TOL_G2, TOL_G4 = 0.10, 0.02
PAS_MAX_G5 = 1e-5
G6_N, G6_HAUT, G6_SEUIL = 192, 1.05, 0.98
MIN_PTS_FIT = 8
REPERE_F = 0.2230
SOUS_ENS_F = [1.35, SQ2, 1.80, 2.85]
FOUT = os.path.join("out", "m10_results.json")
# Le PROGRAMME FIGE est RECALCULE depuis la grille, jamais recopie : un
# nombre qu'un artefact affirme sur lui-meme doit etre COMPTE (D-M10-14).
RECHERCHES_CARTE = len(GRILLE) * len(DEGRES) * 2
RECHERCHES_G2 = len(G2_PTS) * 2
RECHERCHES_G4 = 1
RECHERCHES_ATTENDUES = RECHERCHES_CARTE + RECHERCHES_G2 + RECHERCHES_G4
BALAYAGES_G6_ATTENDUS = len(GRILLE) * len(DEGRES) * 2
CPT = {"recherches": 0, "balayages_G6": 0}

canon = lambda t: unicodedata.normalize("NFC", t).replace("\r\n", "\n").replace("\r", "\n")

# --- CLES DE CARTE (correctif D-M10-13) ------------------------------
# Le defaut : la carte etait indexee par "%.6f", donc float("1.414214")
# != sqrt(2). Le code TESTAIT l'appartenance a la tolerance puis INDEXAIT
# avec la valeur non tolerancee -- les deux moities du meme geste, une
# seule faite. Correction STRUCTURELLE plutot que ponctuelle : une seule
# fabrique de cle, un seul parseur, et le parseur RECANONICALISE vers la
# valeur de grille.
#   - FMT_W a 12 decimales : l'ecart etiquette <-> valeur tombe de 4.4e-7
#     (44 % de TOL_APPART -- marge trop mince, signalee par machine 2) a
#     ~1e-13, six ordres sous la tolerance ;
#   - canon_w() rattrape le cas ou il subsisterait.
# Les deux ensemble, pas l'un ou l'autre.
FMT_W = "%.12f"


def canon_w(x):
    """Ramene une etiquette de carte a la valeur de grille qu'elle designe."""
    for g in GRILLE:
        if abs(x - g) <= TOL_APPART:
            return g
    return x


def cle(p, w):
    return ("%d|" + FMT_W) % (p, w)


def decle(k):
    m = k.split("|")
    return int(m[0]), canon_w(float(m[1]))


# =====================================================================
# 1. GEL JUMEAU -- invariant de cloture AVANT tout calcul d'empreinte
# =====================================================================

def invariant_cloture(txt):
    """Regle 12, corollaire. Retourne (ok, motif). AUCUNE empreinte n'est
    calculee avant que ceci passe."""
    n = txt.count(MARQ_FIN)
    if n != 1:
        return False, "le terminateur apparait %d fois (exige : 1)" % n
    i = txt.index(MARQ_FIN)
    if i == 0 or txt[i - 1] != "\n":
        return False, "le terminateur n'est pas en debut de ligne"
    reste = txt[i + len(MARQ_FIN):]
    if reste.strip():
        return False, "%d caractere(s) significatif(s) apres le terminateur" % len(reste.strip())
    return True, "unique, en ligne pleine, en cloture"


def bloc_du_gel(txt):
    return txt[txt.index(MARQ_DEBUT): txt.index(MARQ_FIN) + len(MARQ_FIN)]


def certifier_gel(verbeux=True):
    src = canon(open(os.path.abspath(__file__), encoding="utf-8").read())
    doc = canon(__doc__)
    ok, motif = invariant_cloture(doc)
    if not ok:
        sys.exit("ARRET invariant de cloture (gel jumeau) : %s" % motif)
    if src.count(MARQ_FIN) != 1:
        sys.exit("ARRET invariant de cloture (source) : le terminateur apparait "
                 "%d fois dans le fichier" % src.count(MARQ_FIN))
    bloc = bloc_du_gel(src)
    h = hashlib.sha256(bloc.encode()).hexdigest()
    if verbeux:
        print("Gel jumeau : %d lignes, invariant de cloture %s" % (bloc.count("\n") + 1, motif))
        print("  sha256 recalcule : %s" % h)
        print("  sha256 certifie  : %s  -> %s"
              % (SHA_GEL, "CONCORDANT" if h == SHA_GEL else "DISCORDANT"))
    if h != SHA_GEL:
        sys.exit("ARRET E19 : le gel jumeau ne correspond pas a la version certifiee.")
    return bloc, h


# =====================================================================
# 2. REGLE D'EXCLUSION -- RE-DERIVEE, jamais lue d'une liste
# =====================================================================

def resonances(ordre_max, lo=1.15, hi=2.95):
    out = set()
    for l in range(1, ordre_max):
        for k in range(1, ordre_max):
            if k + l > ordre_max or math.gcd(k, l) != 1:
                continue
            if lo <= k / l <= hi:
                out.add((k, l, k + l, k / l))
    return sorted(out, key=lambda t: t[3])


def exclu_par_regle(w):
    for ordre_max, rayon in RAYONS:
        for k, l, o, v in resonances(ordre_max):
            if abs(w - v) < rayon:
                return True, "%d:%d ordre %d a %.4f < %.2f" % (k, l, o, abs(w - v), rayon)
    return False, ""


def partition_mecanique(grille=None):
    grille = GRILLE if grille is None else grille
    fit, hors, motifs = [], [], {}
    for w in grille:
        ex, m = exclu_par_regle(w)
        (hors if ex else fit).append(w)
        if ex:
            motifs[w] = m
    return fit, hors, motifs


# =====================================================================
# 3. APPARTENANCE PAR VALEUR (regle 11 amendee)
# =====================================================================

def appartient(w, ensemble, tol=TOL_APPART):
    return any(abs(w - e) <= tol for e in ensemble)


def espacement_min(grille=None):
    g = sorted(GRILLE if grille is None else grille)
    return min(b - a for a, b in zip(g, g[1:]))


# =====================================================================
# 4. FILTRE DES NOTES -- piege D-M10-9 (machine 2)
# =====================================================================
# chercher_seuil rend (None, "ECHEC_HAUT"), (None, "ECHEC_BAS") ET
# (float(hi_d), "DENSE_SANS_EXPLOSION"). Le troisieme rend un FLOTTANT
# VALIDE qui n'est PAS un seuil mesure : filtrer sur la nullite laisserait
# entrer une borne de bracket dans le fit. Le filtre porte sur la NOTE.

def note_admissible(note):
    return isinstance(note, str) and note.startswith("OK|")


def pas_final(note):
    m = re.search(r"pas=([0-9.eE+-]+)", note or "")
    return float(m.group(1)) if m else None


def recevable(s, note):
    """(admissible_pour_le_fit, motif). Applique le filtre de note PUIS G5."""
    if not note_admissible(note):
        return False, "note=%s" % note
    if s is None:
        return False, "seuil nul avec note OK -- incoherent"
    pas = pas_final(note)
    if pas is None:
        return False, "pas final illisible dans la note"
    if pas > PAS_MAX_G5 + EPS_PORTE:
        return False, "G5 pas final %.2e > %.0e" % (pas, PAS_MAX_G5)
    return True, ""


# =====================================================================
# 5. REGRESSION
# =====================================================================

def ols(ws, ss):
    x = np.array([log(w * w - 1.0) for w in ws])
    y = np.array([log(s) for s in ss])
    xm, ym = x.mean(), y.mean()
    Sxx = float(((x - xm) ** 2).sum())
    beta = float(((x - xm) * (y - ym)).sum() / Sxx)
    a = float(ym - beta * xm)
    res = y - (a + beta * x)
    n = len(x)
    sigma = float(sqrt((res ** 2).sum() / (n - 2))) if n > 2 else float("nan")
    se = sigma / sqrt(Sxx) if n > 2 else float("nan")
    return {"beta": beta, "ordonnee": a, "Sxx": Sxx, "sigma": sigma, "SE": se,
            "n": n, "residus": {("%.6f" % w): float(r) for w, r in zip(ws, res)}}


def porte_m10a(fits):
    lignes = []
    for p in DEGRES:
        f = fits[p]
        lo, hi = f["beta"] - 1.96 * f["SE"], f["beta"] + 1.96 * f["SE"]
        lignes.append((p, lo, hi, f["sigma"]))
    conf = all(lo >= BANDE_CONF[0] - EPS_PORTE and hi <= BANDE_CONF[1] + EPS_PORTE
               for _, lo, hi, _ in lignes)
    refut = any(hi < BANDE_REFUT[0] - EPS_PORTE or lo > BANDE_REFUT[1] + EPS_PORTE
                for _, lo, hi, _ in lignes)
    if conf:
        v = "CONFIRMEE"
    elif refut:
        v = "REFUTEE"
    else:
        pire = max(s for _, _, _, s in lignes)
        v = ("NON CONCLUANT DE PUISSANCE" if pire > SIGMA_MAX + EPS_PORTE
             else "NON CONCLUANT DE PHYSIQUE")
    return v, [{"p": p, "IC95": [lo, hi], "sigma": s} for p, lo, hi, s in lignes]


def porte_m10b(fits):
    d = abs(fits[5]["beta"] - fits[7]["beta"])
    if d <= PM10B_COMPAT + EPS_PORTE:
        return "P-INDEPENDANCE COMPATIBLE", d
    if d >= PM10B_REFUT - EPS_PORTE:
        return "REFUTEE", d
    return "NON CONCLUANT", d


# =====================================================================
# 6. P-M10f -- repere reproduit depuis les s*, JAMAIS depuis les d imprimes
# =====================================================================

def etendue_d(s5, s7, points):
    d = [log(s5[w]) - log(s7[w]) for w in points]
    return max(d) - min(d), d


def enveloppe_ok(s5, s7, points, tol=1e-12):
    """etendue(d) = sup sur w0 de max_w |ln rho5 - ln rho7|."""
    et, d = etendue_d(s5, s7, points)
    sup = max(max(abs(a - b) for a in d) for b in d)
    return abs(sup - et) <= tol, et, sup


# =====================================================================
# 7. MOTEUR : import, empreinte, rebinding de P, G3 par degre
# =====================================================================

def charger_moteur(chemin="m9_replication_v1.py", verbeux=True):
    h = hashlib.sha256(open(chemin, "rb").read()).hexdigest()
    if verbeux:
        print("Moteur %s\n  sha256 recalcule : %s\n  sha256 gele      : %s  -> %s"
              % (chemin, h, SHA_MOTEUR, "CONCORDANT" if h == SHA_MOTEUR else "DISCORDANT"))
    if h != SHA_MOTEUR:
        sys.exit("ARRET : le moteur n'est pas celui que le gel designe.")
    spec = importlib.util.spec_from_file_location("m9_moteur", chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # COMPTEUR EXHAUSTIF (D-M10-14). Le fichier moteur n'est pas touche --
    # son empreinte vient d'etre verifiee ; on enveloppe la fonction DANS
    # NOTRE module. Toute recherche est donc comptee, quel que soit
    # l'appelant : aucun site ne peut etre oublie.
    brut = mod.chercher_seuil
    def compte(*a, **kw):
        CPT["recherches"] += 1
        return brut(*a, **kw)
    mod.chercher_seuil = compte
    for nom, attendu in (("W1", 1.0), ("G_REF", 0.05), ("DT", 0.006), ("T_MAX", 400.0),
                         ("CAP", 1.0e4), ("NDENSE", 96), ("LO0", 0.05), ("HI0", 6.0),
                         ("MAX_ELARG", 8), ("NGRID", 48), ("NPASSES", 3)):
        v = getattr(mod, nom)
        if abs(float(v) - float(attendu)) > 1e-12:
            sys.exit("ARRET : globale %s du moteur = %r, le gel exige %r" % (nom, v, attendu))
    return mod


def metrique_g3(m9):
    """Reproduit le nombre de garde_G3 avec SES fonctions et SA graine.
    garde_G3 ne retourne pas sa valeur ; on la recalcule pour la consigner,
    puis on appelle la garde elle-meme pour l'application bloquante."""
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
    print("  rebinding m9.P = %d | G3 erreur backward = %.3e" % (p, e))
    m9.garde_G3()          # application bloquante par la garde du moteur
    return e


# =====================================================================
# 8. ANCRES -- lues de sources primaires, jamais codees en dur
# =====================================================================

def _verifie(chemin, sha, quoi):
    if not os.path.exists(chemin):
        sys.exit("ARRET : source d'ancres absente : %s (%s)" % (chemin, quoi))
    h = hashlib.sha256(open(chemin, "rb").read()).hexdigest()
    if h != sha:
        sys.exit("ARRET : %s -- empreinte %s, le gel exige %s" % (chemin, h, sha))
    return open(chemin, encoding="utf-8").read()


def ancres_p5(chemin=os.path.join("out", "m9_results.json")):
    txt = _verifie(chemin, SHA_M9, "ancres G1 p=5")
    carte = json.loads(txt)["resultats"]["carte"]
    sP, sM = {}, {}
    for v in carte.values():
        w = float(v["w2"])
        for cible in G1_PTS:
            if abs(w - cible) <= TOL_APPART:
                sP[cible] = float(v["sP"]); sM[cible] = float(v["sM"])
    manquants = [w for w in G1_PTS if w not in sP]
    if manquants:
        sys.exit("ARRET : ancres p=5 absentes de la carte M9 : %s" % manquants)
    return sP, sM


def ancres_p7_sP(chemin=os.path.join("out", "m7_results.json")):
    txt = _verifie(chemin, SHA_M7, "ancres G1 p=7 cote sP")
    cl = json.loads(txt)["resultats"]["classique"]
    out = {}
    for cle, v in cl.items():
        w = float(cle)
        for cible in G1_PTS:
            if abs(w - cible) <= TOL_APPART:
                out[cible] = float(v["s_star"] if isinstance(v, dict) else v)
    manquants = [w for w in G1_PTS if w not in out]
    if manquants:
        sys.exit("ARRET : ancres p=7 sP absentes du JSON M7 : %s" % manquants)
    return out


def ancres_p7_sM(chemin="journal_delta_24_D3.md"):
    """Source primaire : consignation S24, CINQ DECIMALES. Limitation
    declaree au gel : quantification 5e-6 absolu, ~2e-5 relatif au pire
    point, mille fois a l'interieur de la tolerance +-2 % de G1."""
    txt = _verifie(chemin, SHA_S24, "ancres G1 p=7 cote sM")
    return _table_sM(txt, chemin)


def _table_sM(txt, chemin="<fixture>"):
    """Parsing SEUL, isole de la verification d'empreinte pour pouvoir etre
    exerce A FROID au --selftest (machine 2 : un lecteur de source primaire
    jamais exerce est un piege arme)."""
    lignes = [l for l in txt.split("\n") if l.strip().startswith("|")]
    entete = next(l for l in lignes if re.match(r"\|\s*w2\s*\|", l))
    cols = [c.strip() for c in entete.strip().strip("|").split("|")][1:]
    ws = [SQ2 if c.lower().startswith("sqrt") else float(c) for c in cols]
    ligne = next(l for l in lignes
                 if l.strip().strip("|").split("|")[0].strip().startswith("sM"))
    vals = [c.strip() for c in ligne.strip().strip("|").split("|")][1:]
    table = {w: float(v) for w, v in zip(ws, vals)}
    out = {}
    for cible in G1_PTS:
        for w, v in table.items():
            if abs(w - cible) <= TOL_ETIQUETTE:
                out[cible] = v
    manquants = [w for w in G1_PTS if w not in out]
    if manquants:
        sys.exit("ARRET : ancres p=7 sM introuvables dans %s pour %s." % (chemin, manquants))
    return out


# =====================================================================
# 9. MESURE ET GARDES DE LIGNE
# =====================================================================

def mesurer(m9, w2, sgn, g=None, dt=None):
    g = m9.G_REF if g is None else g
    dt = m9.DT if dt is None else dt
    s, note = m9.chercher_seuil(w2, sgn=sgn, dt=dt, g=g)
    ok, motif = recevable(s, note)
    return {"s": (float(s) if s is not None else None), "note": note,
            "recevable": ok, "motif_exclusion": motif}


def g6_primaute(m9, w2, sgn, s_etoile):
    """Balayage bloquant declare : [LO0, 1.05 s*] a n = 192.
    CONSIGNATION : le gel nomme [s*, 1.3 s*] pour les ilots et la premiere
    retombee ; le balayage declare s'arrete a 1.05 s*. On rapporte donc sur
    l'INTERSECTION [s*, 1.05 s*], et on le declare -- aucune porte n'en
    depend, et le bord est crible des 1.000-1.001 s* (gel, G6)."""
    s = np.linspace(m9.LO0, G6_HAUT * s_etoile, G6_N)
    CPT["balayages_G6"] += 1
    ex = m9.integrer(w2, s, sgn)
    sous = s[ex & (s < G6_SEUIL * s_etoile)]
    ilots = int(np.sum(np.diff(ex.astype(int)) == 1)) + (1 if ex[0] else 0)
    au_dessus = np.where((s >= s_etoile) & (~ex))[0]
    retombee = float(s[au_dessus[0]] / s_etoile) if len(au_dessus) else None
    return {"explosion_sous_0.98s": (float(sous.min()) if len(sous) else None),
            "exclue": bool(len(sous)), "ilots": ilots,
            "premiere_retombee_en_s": retombee,
            "fenetre_consignation": "[s*, 1.05 s*] -- intersection avec [s*, 1.3 s*] du gel"}


def garde_g2(m9, carte, journal, journal_g3):
    """K a 2g sur 3 points, p=5, deux signes, tolerance 10 %.
    SIX recherches, pas douze : le cote g est DEJA dans la carte -- meme p,
    meme w2, meme signe, meme g, meme dt -- donc identique au bit pres. Le
    remesurer depassait le PROGRAMME FIGE de six recherches (D-M10-14), et
    M9 procedait deja ainsi. Passe par rebind() pour que G3 suive chaque
    rebinding, comme la clause du gel l'exige (note d'exploitation (a))."""
    rebind(m9, 5, journal_g3)
    out, exclues = {}, set()
    for w in G2_PTS:
        for sgn in (+1, -1):
            a = carte[cle(5, w)]["sP" if sgn > 0 else "sM"]
            b = mesurer(m9, w, sgn, g=2 * m9.G_REF)
            if not (a["recevable"] and b["recevable"]):
                exclues.add(w); out["%.6f|%+d" % (w, sgn)] = {"verdict": "NON MESURABLE"}
                continue
            Ka = m9.G_REF * a["s"] ** 3
            Kb = 2 * m9.G_REF * b["s"] ** 3
            ec = abs(Kb / Ka - 1.0)
            ok = ec <= TOL_G2 + EPS_PORTE
            if not ok:
                exclues.add(w)
            out["%.6f|%+d" % (w, sgn)] = {"K_g": Ka, "K_2g": Kb, "ecart": ec,
                                          "verdict": "PASSE" if ok else "ECHEC"}
            l = ("G2 w2=%.4f sgn=%+d : K(g)=%.6g K(2g)=%.6g ecart %.2f %% -> %s"
                 % (w, sgn, Ka, Kb, 100 * ec, "PASSE" if ok else "ECHEC"))
            print("  " + l); journal.append(l)
    return out, exclues


def garde_g4(m9, carte, journal, journal_g3):
    """dt/2 sur la ligne maximisant g s*^(p-1) -- ECHELLE DE FORCE, non le
    plus grand s* : les deux ne coincident pas, et l'erreur est invisible
    une fois faite (piege deja paye par la campagne)."""
    best = None
    for k_, v in carte.items():
        p, w = decle(k_)
        for sgn, k in ((+1, "sP"), (-1, "sM")):
            if not v.get(k, {}).get("recevable"):
                continue
            ech = m9.G_REF * v[k]["s"] ** (p - 1)
            if best is None or ech > best[0]:
                best = (ech, p, w, sgn, v[k]["s"])
    if best is None:
        return {"verdict": "AUCUNE LIGNE MESURABLE"}, set()
    ech, p, w, sgn, s_ref = best
    rebind(m9, p, journal_g3)
    r2 = mesurer(m9, w, sgn, dt=m9.DT / 2)
    s2, ok2, motif = r2["s"], r2["recevable"], r2["motif_exclusion"]
    if not ok2:
        journal.append("G4 p=%d w2=%.4f sgn=%+d : dt/2 non recevable (%s)" % (p, w, sgn, motif))
        return {"p": p, "w2": w, "sgn": sgn, "verdict": "NON FIABLE", "motif": motif}, {w}
    ec = abs(s2 / s_ref - 1.0)
    ok = ec <= TOL_G4 + EPS_PORTE
    l = ("G4 ligne la plus raide (g s*^(p-1) = %.4g) p=%d w2=%.4f sgn=%+d : "
         "s*(dt)=%.5f s*(dt/2)=%.5f ecart %.3f %% -> %s"
         % (ech, p, w, sgn, s_ref, s2, 100 * ec, "PASSE" if ok else "ECHEC"))
    print("  " + l); journal.append(l)
    return ({"p": p, "w2": w, "sgn": sgn, "echelle_force": ech, "s_dt": s_ref,
             "s_dt2": s2, "ecart": ec, "verdict": "PASSE" if ok else "NON FIABLE"},
            set() if ok else {w})


def appliquer_g7(carte, exclusions):
    """Toute exclusion a UN degre retire le w2 du fit a TOUS les degres.
    Rend (retenus_par_degre, ampute, non_ampute)."""
    exclus = set()
    for w, motifs in exclusions.items():
        if motifs:
            exclus.add(float(w))
    non_ampute, ampute = {}, {}
    for p in DEGRES:
        na, am = [], []
        for w in FIT:
            v = carte.get(cle(p, w))
            if not v or v.get("sF") is None:
                continue
            na.append(w)
            if not any(abs(w - e) <= TOL_APPART for e in exclus):
                am.append(w)
        non_ampute[p], ampute[p] = na, am
    return ampute, non_ampute


def resume(carte, ampute):
    """Fit par degre sur l'ensemble AMPUTE, puis les portes."""
    fits, out = {}, {}
    for p in DEGRES:
        ws = ampute[p]
        if len(ws) < MIN_PTS_FIT:
            fits[p] = None
            continue
        fits[p] = ols(ws, [carte[cle(p, w)]["sF"] for w in ws])
    out["fit"] = {p: fits[p] for p in DEGRES}
    out["w2_retenus_par_degre"] = {p: ampute[p] for p in DEGRES}
    if any(fits[p] is None for p in DEGRES):
        out["P-M10a"] = {"verdict": "NON CONCLUANT PAR CONSTRUCTION",
                         "motif": "un degre est sous %d points de fit" % MIN_PTS_FIT}
        out["P-M10b"] = {"verdict": "NON CONCLUANT PAR CONSTRUCTION"}
        return out, fits
    va, det = porte_m10a(fits)
    out["P-M10a"] = {"verdict": va, "detail": det,
                     "lecture_non_concluant": {p: {"SE": fits[p]["SE"],
                                                   "sigma": fits[p]["sigma"],
                                                   "sigma_max": SIGMA_MAX} for p in DEGRES}}
    vb, d = porte_m10b(fits)
    out["P-M10b"] = {"verdict": vb, "ecart_beta": d}
    out["P-M10d"] = {"residus": {p: fits[p]["residus"] for p in DEGRES}}
    return out, fits


def consignation_m10f(carte):
    sF = {p: {} for p in DEGRES}
    for k_, v in carte.items():
        p, w = decle(k_)
        if v.get("sF") is not None:
            sF[p][w] = v["sF"]
    communs = [w for w in sorted(set(sF[5]) & set(sF[7]))]
    sous = [w for w in SOUS_ENS_F if any(abs(w - c) <= TOL_APPART for c in communs)]
    out = {"points_communs": communs}
    if len(sous) == len(SOUS_ENS_F):
        eti, _ = etendue_d(sF[5], sF[7], sous)
        env, _, sup = enveloppe_ok(sF[5], sF[7], sous)
        out["(i)_sous_ensemble_commun"] = {"etendue": eti, "repere": REPERE_F,
                                           "ecart_au_repere": eti - REPERE_F,
                                           "enveloppe_verifiee": env, "sup": sup}
    else:
        out["(i)_sous_ensemble_commun"] = {"verdict": "INCALCULABLE",
                                           "manquants": [w for w in SOUS_ENS_F if w not in sous]}
    if communs:
        etii, d = etendue_d(sF[5], sF[7], communs)
        out["(ii)_tous_points_mesures"] = {"etendue": etii, "n": len(communs),
                                           "repere": None}
        out["argmax_d"] = {"w2": communs[int(np.argmax(d))],
                           "attendu": [2.30, 2.45, 2.60],
                           "d_par_point": {("%.6f" % w): dd for w, dd in zip(communs, d)}}
    return out


def reconcilier(chemin, ampute):
    """Relit le JSON ECRIT et RECALCULE beta depuis la carte brute ; ne lit
    jamais les meta. Toute divergence est un arret."""
    j = json.load(open(chemin, encoding="utf-8"))
    carte = j["resultats"]["carte"]
    for p in DEGRES:
        ws = ampute[p]
        if len(ws) < MIN_PTS_FIT:
            continue
        b = ols(ws, [carte[cle(p, w)]["sF"] for w in ws])["beta"]
        stocke = j["resume"]["fit"][str(p)]["beta"]
        if abs(b - stocke) > 1e-12:
            sys.exit("ARRET reconciliation p=%d : brut %.15f vs resume %.15f" % (p, b, stocke))
    return True


# =====================================================================
# 10. SELFTEST -- ALGEBRE PURE, aucune integration
# =====================================================================

def selftest():
    ok = [True]
    def T(nom, cond, detail=""):
        ok[0] &= bool(cond)
        print("  [%s] %-58s %s" % ("OK " if cond else "ECHEC", nom, detail))

    print("=== 1. INVARIANT DE CLOTURE (avant tout calcul d'empreinte) ===")
    doc = canon(__doc__)
    good, motif = invariant_cloture(doc)
    T("gel jumeau : terminateur unique, en cloture", good, motif)
    T("un texte a deux terminateurs est REFUSE",
      not invariant_cloture(doc + "\n" + MARQ_FIN)[0])
    T("un texte sans terminateur est REFUSE",
      not invariant_cloture(doc.replace(MARQ_FIN, "xx"))[0])
    T("du texte apres le terminateur est REFUSE",
      not invariant_cloture(doc + "\nqueue")[0])

    print("=== 2. EMPREINTE DU GEL JUMEAU ===")
    bloc, h = certifier_gel(verbeux=False)
    T("sha256 du bloc = version certifiee v8", h == SHA_GEL, h[:16] + "...")
    T("le bloc est extrait, pas retranscrit : il finit sur la cloture",
      bloc.rstrip().endswith("\n" + MARQ_FIN))

    print("=== 3. REGLE D'EXCLUSION RE-DERIVEE (E24) ===")
    res = resonances(8)
    T("resonances d'ordre <= 8 dans l'intervalle : 5", len(res) == 5,
      " ".join("%d:%d" % (k, l) for k, l, _, _ in res))
    fit, hors, motifs = partition_mecanique()
    T("la regle rend l'ensemble de fit gele (10 points)",
      [round(x, 7) for x in fit] == [round(x, 7) for x in FIT], "%d points" % len(fit))
    T("la regle rend l'ensemble hors fit gele (6 points)",
      [round(x, 7) for x in hors] == [round(x, 7) for x in sorted(HORS_FIT)],
      "%d points" % len(hors))
    T("1.35 sort par 4:3 ordre 7 (E24)", "4:3" in motifs.get(1.35, ""), motifs.get(1.35, ""))
    T("1.25 = 5:4 ordre 9 reste dans le fit", appartient(1.25, fit))
    T("motif : 5 des 6 points hors fit sont couverts par l'ordre <= 6",
      sum(1 for w in hors if min(abs(w - 1.5), abs(w - 2.0)) < 0.12) == 5)

    print("=== 4. APPARTENANCE PAR VALEUR (regle 11 amendee) ===")
    em = espacement_min()
    T("tolerance tres inferieure a l'espacement minimal",
      TOL_APPART < em / 1000, "tol %.0e vs espacement %.4f (x%d)" % (TOL_APPART, em, em / TOL_APPART))
    T("sous-ensemble P-M10f inclus dans la grille",
      all(appartient(w, GRILLE) for w in SOUS_ENS_F))
    T("2.40 est REJETE (D-M10-4)", not appartient(2.40, GRILLE))
    T("sqrt(2) tronque a 1.41421 est REJETE a la tolerance declaree",
      not appartient(1.41421, GRILLE))
    T("l'arrondi commun round(w,4) confondrait 1.41421 et sqrt(2) : methode exclue",
      round(1.41421, 4) == round(SQ2, 4))

    print("=== 5. FILTRE DES NOTES (piege D-M10-9) ===")
    T("ECHEC_HAUT rejete", not recevable(None, "ECHEC_HAUT")[0])
    T("ECHEC_BAS rejete", not recevable(None, "ECHEC_BAS")[0])
    T("DENSE_SANS_EXPLOSION rejete MALGRE un flottant valide",
      not recevable(1.234567, "DENSE_SANS_EXPLOSION")[0])
    filtre_naif = lambda s, note: s is not None
    T("le filtre NAIF (s is not None) accepte a tort DENSE_SANS_EXPLOSION",
      filtre_naif(1.234567, "DENSE_SANS_EXPLOSION")
      and not recevable(1.234567, "DENSE_SANS_EXPLOSION")[0],
      "d'ou le filtre sur la NOTE")
    T("note OK avec pas conforme acceptee", recevable(0.5, "OK|pas=6.03e-07")[0])
    T("note OK avec pas > 1e-5 rejetee par G5", not recevable(0.5, "OK|pas=3.00e-05")[0])

    print("=== 6. REGRESSION ===")
    f = ols(FIT, [2.0 * (w * w - 1.0) ** 0.93 for w in FIT])
    T("loi de puissance exacte : beta retrouve", abs(f["beta"] - 0.93) < 1e-12,
      "beta=%.12f" % f["beta"])
    T("Sxx du fit corrige = 7.4425", abs(f["Sxx"] - 7.4425) < 5e-5, "%.4f" % f["Sxx"])
    T("seuil sigma = marge*sqrt(Sxx)/1.96 = 0.1392",
      abs(MARGE * sqrt(f["Sxx"]) / 1.96 - SIGMA_MAX) < 5e-5,
      "%.4f" % (MARGE * sqrt(f["Sxx"]) / 1.96))
    T("residus orthogonaux au regresseur",
      abs(sum(f["residus"].values())) < 1e-12)

    print("=== 7. PORTES, sur entrees synthetiques ===")
    faux = lambda b, se, sg: {"beta": b, "SE": se, "sigma": sg}
    T("P-M10a CONFIRMEE si les deux IC sont dans [0.90, 1.10]",
      porte_m10a({5: faux(1.00, 0.01, 0.05), 7: faux(0.99, 0.01, 0.05)})[0] == "CONFIRMEE")
    T("P-M10a REFUTEE si un IC est disjoint de [0.85, 1.15]",
      porte_m10a({5: faux(0.50, 0.01, 0.05), 7: faux(0.99, 0.01, 0.05)})[0] == "REFUTEE")
    T("NON CONCLUANT DE PUISSANCE si sigma > 0.1392 a un degre",
      porte_m10a({5: faux(0.95, 0.05, 0.20), 7: faux(0.95, 0.05, 0.05)})[0]
      == "NON CONCLUANT DE PUISSANCE")
    T("NON CONCLUANT DE PHYSIQUE si sigma <= 0.1392 aux deux",
      porte_m10a({5: faux(0.95, 0.05, 0.10), 7: faux(0.89, 0.05, 0.04)})[0]
      == "NON CONCLUANT DE PHYSIQUE")
    T("P-M10b compatible a 0.08", porte_m10b({5: faux(1.00, 0, 0), 7: faux(0.92, 0, 0)})[0]
      == "P-INDEPENDANCE COMPATIBLE")
    T("P-M10b refutee a 0.20 EXACTEMENT (frontiere flottante)",
      porte_m10b({5: faux(1.00, 0, 0), 7: faux(0.80, 0, 0)})[0] == "REFUTEE",
      "|1.00-0.80| = %.17f" % abs(1.00 - 0.80))
    T("P-M10b compatible a 0.08 EXACTEMENT (frontiere flottante)",
      porte_m10b({5: faux(1.00, 0, 0), 7: faux(0.92, 0, 0)})[0]
      == "P-INDEPENDANCE COMPATIBLE", "|1.00-0.92| = %.17f" % abs(1.00 - 0.92))
    T("juste au-dela de la frontiere, le verdict change bien",
      porte_m10b({5: faux(1.00, 0, 0), 7: faux(0.895, 0, 0)})[0] == "NON CONCLUANT")

    print("=== 8. P-M10f : REPERE DEPUIS LES s*, JAMAIS DEPUIS LES d IMPRIMES ===")
    s5 = {1.35: 0.30974221815772490, SQ2: 0.32641734895979340,
          1.80: 0.66682058077588550, 2.85: 2.58541195364377740}
    s7 = {1.35: 0.22875, SQ2: 0.25627, 1.80: 0.52141, 2.85: 1.62409}
    et, d = etendue_d(s5, s7, SOUS_ENS_F)
    T("etendue depuis les s* = 0.2230", abs(et - REPERE_F) < 5e-5, "%.6f" % et)
    T("etendue depuis les d IMPRIMES donne 0.2229, et ne doit PAS servir",
      abs((0.4649 - 0.2420) - REPERE_F) > 5e-6, "%.4f" % (0.4649 - 0.2420))
    env, _, sup = enveloppe_ok(s5, s7, SOUS_ENS_F)
    T("propriete d'enveloppe : etendue = sup sur w0", env, "sup=%.6f" % sup)
    s5b = dict(s5); s5b[2.40] = 1.79395264911895
    s7b = dict(s7); s7b[2.40] = 1.06065
    et5, _ = etendue_d(s5b, s7b, SOUS_ENS_F + [2.40])
    T("monotonie : l'etendue a 5 points (archive) = 0.2836", abs(et5 - 0.2836) < 5e-5,
      "%.6f" % et5)

    print("=== 9. CONVENTION (f) ET INVERSION DU COTE FRAGILE ===")
    T("convention (f) = min par point : p=5 a 1.80, sF = sP",
      min(0.6668205807758855, 0.9011724660948772) == 0.6668205807758855)
    T("convention (f) = min par point : p=7 a 1.80, sF = sP",
      min(0.52141, 0.64259) == 0.52141)
    T("l'ancre sM p=7 a 1.80 vaut 0.64259, pas 0.52141",
      abs(0.64259 - 0.52141) > 0.02 * 0.64259 * 9,
      "un sM errone y ferait echouer G1 de 9.4x la tolerance")

    print("=== 10. ATTEIGNABILITE DEPUIS main() (reponse a D-M10-11) ===")
    import ast as _ast
    arbre = _ast.parse(open(os.path.abspath(__file__), encoding="utf-8").read())
    fns = {n.name: n for n in arbre.body if isinstance(n, _ast.FunctionDef)}
    def joignables(depart, vus=None):
        vus = vus if vus is not None else set()
        for x in _ast.walk(fns[depart]):
            if isinstance(x, _ast.Call) and isinstance(x.func, _ast.Name):
                n = x.func.id
                if n in fns and n not in vus and n != "selftest":
                    vus.add(n); joignables(n, vus)
        return vus
    atteints = joignables("main")
    for nom in ("ols", "porte_m10a", "porte_m10b", "etendue_d", "enveloppe_ok",
                "garde_g2", "garde_g4", "appliquer_g7", "resume",
                "consignation_m10f", "reconcilier"):
        T("main() atteint %s" % nom, nom in atteints)
    T("selftest n'est pas dans le chemin de la manche", "selftest" not in atteints)

    print("=== 11. LECTEURS DE SOURCES PRIMAIRES, A FROID ===")
    attendus = {"m9": (os.path.join("out", "m9_results.json"), ancres_p5),
                "m7": (os.path.join("out", "m7_results.json"), ancres_p7_sP),
                "s24": ("journal_delta_24_D3.md", ancres_p7_sM)}
    ref_sM7 = {1.35: 0.22875, SQ2: 0.25627, 1.80: 0.64259, 2.85: 1.62409}
    saute = [0]
    for nom, (ch, fn) in attendus.items():
        if not os.path.exists(ch):
            saute[0] += 1
            print("  [SAUTE] lecteur %-4s : source absente (%s)" % (nom, ch))
            continue
        r = fn(ch)
        vals = r[0] if isinstance(r, tuple) else r
        T("lecteur %s rend les 4 points de G1" % nom,
          all(w in vals for w in G1_PTS), " ".join("%.5f" % vals[w] for w in G1_PTS))
        if nom == "s24":
            T("sM p=7 a 1.80 vaut bien 0.64259 (et non le sP 0.52141)",
              abs(vals[1.80] - ref_sM7[1.80]) < 1e-9, "%.5f" % vals[1.80])
            T("les quatre ancres sM p=7 concordent avec la table S24",
              all(abs(vals[w] - ref_sM7[w]) < 1e-9 for w in G1_PTS))

    print("=== 12. PARSEUR S24 EXERCE A FROID (fixture verbatim machine 2) ===")
    fixture = "\n".join([
        "| w2 | 1.35 | sqrt2 | 1.80 | 2.00 | 2.40 | 2.85 |",
        "|---|---|---|---|---|---|---|",
        "| sP (M7) | 0.26000 | 0.29756 | 0.52141 | 0.39227 | 1.46418 | 1.94232 |",
        "| sM (ici) | 0.22875 | 0.25627 | 0.64259 | 0.39184 | 1.06065 | 1.62409 |",
        "| asym | +13.7 % | +16.1 % | **-18.9 %** | +0.1 % | **+38.1 %** | +19.6 % |"])
    t = _table_sM(fixture)
    T("le parseur lit la LIGNE sM, pas la ligne sP",
      abs(t[1.80] - 0.64259) < 1e-9, "1.80 -> %.5f (sP y vaut 0.52141)" % t[1.80])
    T("les quatre ancres de G1 sont lues", all(w in t for w in G1_PTS),
      " ".join("%.5f" % t[w] for w in G1_PTS))
    T("l'etiquette 'sqrt2' est reconnue comme sqrt(2)", abs(t[SQ2] - 0.25627) < 1e-9)
    T("a 1.35 le parseur rend le sM 0.22875, jamais le sP 0.26000",
      abs(t[1.35] - 0.22875) < 1e-9 and abs(t[1.35] - 0.26000) > 1e-3)
    sans_sM = "\n".join(l for l in fixture.split("\n") if "sM" not in l)
    try:
        _table_sM(sans_sM); leve = False
    except StopIteration:
        leve = True
    T("un tableau sans ligne sM leve, il ne rend pas silencieusement autre chose", leve)

    print("=== 13. CLES DE CARTE (D-M10-13) ===")
    T("aller-retour cle/decle exact sur les 16 points de la grille",
      all(decle(cle(p, w)) == (p, w) for p in DEGRES for w in GRILLE))
    T("sqrt(2) revient a l'IDENTIQUE, pas seulement a la tolerance",
      decle(cle(5, SQ2))[1] == SQ2, "%.17g" % decle(cle(5, SQ2))[1])
    ecart12 = abs(float(FMT_W % SQ2) - SQ2)
    ecart6 = abs(float("%.6f" % SQ2) - SQ2)
    T("le format %.12f met l'ecart 6 ordres sous la tolerance",
      ecart12 < TOL_APPART / 1e5,
      "%.1e (contre %.1e en %%.6f, soit %.0f %% de la tolerance)"
      % (ecart12, ecart6, 100 * ecart6 / TOL_APPART))
    T("canon_w rattrape une etiquette tronquee a 6 decimales",
      canon_w(float("%.6f" % SQ2)) == SQ2)
    src_ = open(os.path.abspath(__file__), encoding="utf-8").read()
    # aiguilles construites par concatenation : un test qui contient
    # litteralement ce qu'il cherche se declenche sur lui-meme (regle 12,
    # cinquieme occurrence du meme piege dans cette campagne).
    vieux_fmt = '"%d|' + '%.6f"'
    vieux_idiome = "cle.split" + '("|")'
    T("plus aucun site ne fabrique une cle de carte au vieux format",
      src_.count(vieux_fmt) == 0, "occurrences : %d" % src_.count(vieux_fmt))
    T("plus aucun site n'emploie le vieux parseur de cle",
      src_.count(vieux_idiome) == 0, "occurrences : %d" % src_.count(vieux_idiome))
    besoin_decle = "def " + "decle"
    T("decle est defini une seule fois et une seule",
      src_.count(besoin_decle) == 1, "occurrences : %d" % src_.count(besoin_decle))

    print("=== 14. COMPTAGE DU PROGRAMME FIGE (D-M10-14) ===")
    T("le total attendu est RECALCULE depuis la grille, pas recopie",
      RECHERCHES_ATTENDUES == 16 * 2 * 2 + 6 + 1,
      "carte %d + G2 %d + G4 %d = %d"
      % (RECHERCHES_CARTE, RECHERCHES_G2, RECHERCHES_G4, RECHERCHES_ATTENDUES))
    T("il vaut les 71 du gel", RECHERCHES_ATTENDUES == 71)
    T("les balayages G6 attendus valent les 64 du gel", BALAYAGES_G6_ATTENDUS == 64)
    T("garde_g2 prend la carte en argument : le cote g n'est plus remesure",
      "carte" in garde_g2.__code__.co_varnames[:4],
      " ".join(garde_g2.__code__.co_varnames[:4]))
    T("le compteur est pose PAR ENVELOPPE du moteur, pas au site d'appel",
      "CPT[\"recherches\"] += 1" in src_[src_.index("def charger_moteur"):
                                          src_.index("def metrique_g3")])
    T("garde_g2 et garde_g4 passent par rebind (G3 apres chaque rebinding)",
      "rebind(m9, 5, journal_g3)" in src_ and "rebind(m9, p, journal_g3)" in src_)

    print("=== 15. G7 : REPERCUSSION ===")
    ret = {p: [w for w in FIT if w != 1.80] for p in DEGRES}
    T("une exclusion a un degre retire le point a tous",
      all(1.80 not in ret[p] for p in DEGRES))
    T("sous 8 points, les portes sont NON CONCLUANTES par construction",
      len(FIT[:7]) < MIN_PTS_FIT)

    print()
    if saute[0]:
        print("SELFTEST INCOMPLET : %d lecteur(s) saute(s) faute de source. "
              "A relancer avec out/m9_results.json, out/m7_results.json et "
              "journal_delta_24_D3.md presents." % saute[0])
    print("SELFTEST : %s" % ("TOUT PASSE" if ok[0] else "*** ECHEC ***"))
    return 0 if ok[0] else 1


# =====================================================================
# 11. MANCHE
# =====================================================================

def sauver(res):
    os.makedirs("out", exist_ok=True)
    with open(FOUT, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=1, sort_keys=True, ensure_ascii=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--moteur", default="m9_replication_v1.py")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())

    bloc, hgel = certifier_gel()
    m9 = charger_moteur(a.moteur)
    fit_regle, hors_regle, _ = partition_mecanique()
    if [round(x, 7) for x in fit_regle] != [round(x, 7) for x in FIT]:
        sys.exit("ARRET : la regle d'exclusion ne rend pas l'ensemble de fit gele.")

    res = {"meta": {"gel_sha256_bloc": hgel, "moteur_sha256": SHA_MOTEUR,
                    "partition": {"fit": FIT, "hors_fit": sorted(HORS_FIT)},
                    "G3_par_degre": [], "gardes": [], "exclusions": {}},
           "resultats": {"carte": {}, "G2": {}, "G4": {}, "G6": {}}}
    journal_g3 = res["meta"]["G3_par_degre"]

    aP5, aM5 = ancres_p5()
    aP7 = ancres_p7_sP()
    aM7 = ancres_p7_sM()
    ancres = {5: (aP5, aM5), 7: (aP7, aM7)}

    # --- phase 1 : les points de G1, aux deux degres, avant toute lecture
    print("\n--- PHASE 1 : G1 (bloquante) sur %d points communs ---" % len(G1_PTS))
    for p in DEGRES:
        rebind(m9, p, journal_g3)
        aP, aM = ancres[p]
        for w in G1_PTS:
            for sgn, anc in ((+1, aP[w]), (-1, aM[w])):
                m = mesurer(m9, w, sgn)
                res["resultats"]["carte"].setdefault(cle(p, w), {})[
                    "sP" if sgn > 0 else "sM"] = m
                sauver(res)
                if not m["recevable"]:
                    sys.exit("ARRET G1 : p=%d w2=%.4f sgn=%+d non recevable (%s)"
                             % (p, w, sgn, m["motif_exclusion"]))
                ec = abs(m["s"] / anc - 1.0)
                ligne = ("G1 p=%d w2=%.4f sgn=%+d : %.5f vs %.5f (%.2f %%) -> %s"
                         % (p, w, sgn, m["s"], anc, 100 * ec,
                            "PASSE" if ec <= TOL_G1 else "ECHEC"))
                print("  " + ligne); res["meta"]["gardes"].append(ligne); sauver(res)
                if ec > TOL_G1:
                    sys.exit("ARRET G1 : ecart %.2f %% > %.0f %%" % (100 * ec, 100 * TOL_G1))
    print("G1 PASSE aux %d lignes. La manche continue." % (len(G1_PTS) * 4))

    # --- phase 2 : le reste de la grille
    print("\n--- PHASE 2 : les %d points restants ---" % (len(GRILLE) - len(G1_PTS)))
    for p in DEGRES:
        rebind(m9, p, journal_g3)
        for w in GRILLE:
            if appartient(w, G1_PTS):
                continue
            for sgn in (+1, -1):
                m = mesurer(m9, w, sgn)
                res["resultats"]["carte"].setdefault(cle(p, w), {})[
                    "sP" if sgn > 0 else "sM"] = m
                sauver(res)
                print("  p=%d w2=%.4f sgn=%+d : %s" % (p, w, sgn, m["note"]))

    # --- phase 3 : convention (f) et G6, un rebinding PAR DEGRE (note (a))
    print("\n--- PHASE 3 : convention (f) et G6 ---")
    carte = res["resultats"]["carte"]
    for p in DEGRES:
        rebind(m9, p, journal_g3)
        for k_, v in carte.items():
            if decle(k_)[0] != p:
                continue
            w = decle(k_)[1]
            if not (v["sP"]["recevable"] and v["sM"]["recevable"]):
                v["sF"] = None; v["frag"] = None
                res["meta"]["exclusions"].setdefault("%.6f" % w, []).append(
                    "G5 p=%d : %s" % (p, v["sP"]["motif_exclusion"] or v["sM"]["motif_exclusion"]))
                continue
            v["frag"] = 1 if v["sP"]["s"] <= v["sM"]["s"] else -1
            v["sF"] = min(v["sP"]["s"], v["sM"]["s"])
            v["asym"] = v["sP"]["s"] / v["sM"]["s"]
            for sgn in (+1, -1):
                g6 = g6_primaute(m9, w, sgn, v["sP"]["s"] if sgn > 0 else v["sM"]["s"])
                res["resultats"]["G6"][cle(p, w) + "|%+d" % sgn] = g6
                if g6["exclue"]:
                    res["meta"]["exclusions"].setdefault("%.6f" % w, []).append(
                        "G6 p=%d sgn=%+d explosion a %.5f" % (p, sgn, g6["explosion_sous_0.98s"]))
            sauver(res)

    # --- phase 4 : G2 (6 recherches) et G4 (1 recherche)
    print("\n--- PHASE 4 : G2 et G4 ---")
    g2, ex2 = garde_g2(m9, carte, res["meta"]["gardes"], journal_g3)
    res["resultats"]["G2"] = g2
    for w in ex2:
        res["meta"]["exclusions"].setdefault("%.6f" % w, []).append("G2 echec")
    g4, ex4 = garde_g4(m9, carte, res["meta"]["gardes"], journal_g3)
    res["resultats"]["G4"] = g4
    for w in ex4:
        res["meta"]["exclusions"].setdefault("%.6f" % w, []).append("G4 ligne NON FIABLE")
    sauver(res)

    # --- phase 5 : G7, fit, portes, consignations
    print("\n--- PHASE 5 : G7, fit, portes ---")
    ampute, non_ampute = appliquer_g7(carte, res["meta"]["exclusions"])
    res["meta"]["fit_non_ampute_par_degre"] = non_ampute
    r, fits = resume(carte, ampute)
    r["P-M10e"] = {(cle(p, w)): {"r_s": carte[cle(p, w)].get("asym"),
                                          "frag": carte[cle(p, w)].get("frag")}
                   for p in DEGRES for w in GRILLE if cle(p, w) in carte}
    r["P-M10f"] = consignation_m10f(carte)
    res["resume"] = r
    for p in DEGRES:
        if fits[p]:
            print("  p=%d : beta=%.5f  SE=%.5f  sigma=%.5f  n=%d"
                  % (p, fits[p]["beta"], fits[p]["SE"], fits[p]["sigma"], fits[p]["n"]))
    print("  P-M10a : %s" % r["P-M10a"]["verdict"])
    print("  P-M10b : %s" % r["P-M10b"]["verdict"])
    sauver(res)

    # --- reconciliation : RECALCULEE depuis le brut, jamais lue des meta
    reconcilier(FOUT, ampute)
    print("  reconciliation brut <-> resume : CONCORDANTE")

    res["meta"]["script_sha256"] = hashlib.sha256(
        open(os.path.abspath(__file__), "rb").read()).hexdigest()
    res["meta"]["date_utc"] = __import__("datetime").datetime.utcnow().strftime(
        "%Y-%m-%dT%H:%M:%SZ")
    res["meta"]["recherches"] = {"comptees": CPT["recherches"],
                                 "attendues": RECHERCHES_ATTENDUES,
                                 "detail_attendu": {"carte": RECHERCHES_CARTE,
                                                    "G2": RECHERCHES_G2, "G4": RECHERCHES_G4}}
    res["meta"]["balayages_G6"] = {"comptes": CPT["balayages_G6"],
                                   "attendus": BALAYAGES_G6_ATTENDUS}
    sauver(res)
    if CPT["recherches"] != RECHERCHES_ATTENDUES:
        sys.exit("ARRET : %d recherches effectuees, le PROGRAMME FIGE en declare %d."
                 % (CPT["recherches"], RECHERCHES_ATTENDUES))
    if CPT["balayages_G6"] != BALAYAGES_G6_ATTENDUS:
        sys.exit("ARRET : %d balayages G6, le PROGRAMME FIGE en declare %d."
                 % (CPT["balayages_G6"], BALAYAGES_G6_ATTENDUS))
    print("\nEcrit : %s" % FOUT)
    print("Recherches COMPTEES : %d (PROGRAMME FIGE : %d) | balayages G6 : %d (%d)"
          % (CPT["recherches"], RECHERCHES_ATTENDUES,
             CPT["balayages_G6"], BALAYAGES_G6_ATTENDUS))
    print("sha256 du JSON : %s" % hashlib.sha256(open(FOUT, "rb").read()).hexdigest())


if __name__ == "__main__":
    main()
