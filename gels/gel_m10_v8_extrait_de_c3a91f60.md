PRE-ENREGISTREMENT M10 -- L'EXPOSANT beta DE LA LOI DE SEUIL (CLASSIQUE PUR)
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

=== FIN DU GEL M10 ===