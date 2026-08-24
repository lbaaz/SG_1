# BILAN MACHINE 1 v2 -- manche M17, apres rectification et sondes
# Observations et lectures, pour arbitrage machine 2. NON NORMATIF.

Fichier : note_machine1_bilan_journee_m17_v2.md
Date    : 24/08/2026
Emetteur: machine 1
Remplace: note_machine1_bilan_journee_m17_v1.md 935c4928388988b4 (PB-1 :
          la v1 n'est pas editee ; elle est DEPASSEE sur trois blocs --
          les sondes, la rectification de custody, la numerotation)
Statut  : aucun numero pris (E18) ; opinions marquees ; rien d'opposable.
Regle (alpha) appliquee a la presente note : chaque nombre transcrit cite
sa piece ET sa ligne de log, et un controle mecanique machine 1 a verifie
chaque citation contre la copie recue avant depot (resultat au message).

Gel     : m17_pre_enregistrement_quantique_v9.md  a5e86ca3191fb204 (CERTIFIE)
Script  : m17_chaine_v8.py                        a25619c412c93fd9  82195 o
Pieces machine 2 (copies recues, empreintes re-derivees machine 1) :
  note rectification custody v1     2fa620dca9cbf0d0  14502 o
  verif rectification .py / .log    7a1ac82e8a17fad8 / cd2d9994ba589677
  banc lourd v2 .py / .log          920097ebc9e95623 / 0e0a2baacc2984cd
  prevol v2 .py / .log              8a2b16b8d44c50b8 / 4dfade44dd2b0647
  sonde v1 note / .py / .log        d8833783f7d1d5a7 / 04cf6c1290b7893e /
                                    475d4850fd11c2d9
  sonde v2 note / .py / .log        acb654aa8860a16d / 3e4f9594ced0db24 /
                                    fb45649600ebf96e
  verif sonde v1 .py / .log         ac9265caa72c09bc / b196afbfdc702257
  verif sonde v2 .py / .log         f6c1afe8cec69253 / 386c9126b973e8aa

## 1. CE QUI A CHANGE DEPUIS LA v1 -- FAITS

La v1 s'arretait aux trois bloquants du banc lourd. Depuis :
- machine 2 a decouvert que trois de ses notes ne resolvaient pas (log
  depose contredisant la note, instruments jamais ecrits sur disque) et a
  RECTIFIE : six defauts nommes, deux instruments v2 deposes, un
  verificateur a 86 OK / 0 FAUX avec test negatif ;
- deux sondes d'absorbeur ont instruit D-B3 aux deux points extremes de
  la grille, chacune avec son verificateur (42/0 et 59/0) ;
- toutes les mesures des notes v1 se REPRODUISENT au chiffre pres sur les
  instruments v2 (rectification, section 3) -- les verdicts D-B1/D-B2/D-B3
  tiennent, desormais portes par des logs qui les montrent.

## 2. LA RECTIFICATION -- LECTURE MACHINE 1

D-M17-22 retourne, avec l'aggravation exactement diagnostiquee : hier
machine 1 inventait du contenu sous des empreintes justes ; la machine 2
avait des mesures VRAIES sous des instruments qui ne les rendaient pas --
et un log depose disant le contraire de sa note (matrice 5/7 DEGENEREE au
log v1 contre 7/7 annonce). Les deux modes encadrent la meme regle, et les
deux prescriptions la ferment par les deux bouts :
  (alpha) la ligne de log citee, DU log de l'instrument depose ;
  (beta)  une mesure faite hors instrument depose n'existe pas.
Le verificateur qui a mordu quatre fois sur ses propres numeros de ligne a
la premiere passe est la meilleure preuve de (alpha) : le defaut se
documente sous forme reduite dans la note qui le documente. Machine 1
souscrit aux deux regles et applique (alpha) a la presente note.

COLLISION DE NUMEROTATION, A RESOUDRE AU REGISTRE AVANT L'ACTE. La
rectification etiquette ses six defauts D-M17-24..29. Or D-M17-23/24
(forme G-7) et D-M17-25 (fragment duplique) sont DEJA PRIS : l'acte de
certification du gel (note m2 v10, section 1 "D-M17-25 LEVE") et le
journal du gel v9 les portent -- un document CERTIFIE. La file etait a 25
a la certification ; les six de la rectification devraient prendre 26..31.
La note dit elle-meme "les numeros se prennent a l'acte" : rien de casse,
mais c'est la famille renumerotation -- elle se propage mecaniquement ou
ne se fait pas, et ici elle toucherait une piece certifiee si on renumero-
tait dans l'autre sens. Decision de registre, pas de script.

## 3. D-B3 INSTRUIT -- L'ETAT APRES LES DEUX SONDES

(i) L'OBJECTION DE COUT EST MORTE. La grille est plate en r_c : 40 ou 41,
amplitude 1.02 (sonde v2 log l.9-20). La direction (a) coute 1372 s =
22.9 min pour la grille entiere a vingt couches (note sonde v2, section 5,
verifiee) -- avec la lecon de transport incluse : le facteur reel/prevu
DECROIT avec dim (1.480 / 1.213 / 1.169), la moyenne 1.29 serait le
mauvais chiffre, le facteur a la taille cible est 1.213.

(ii) LA MONTANTE EST STRUCTURELLEMENT INSATISFIABLE. Elle converge vers
des limites non nulles DIFFERENTES par point : ~15.4 % au nominal (sonde
v1 log l.16/27/38 : 11.94 -> 15.18 -> 15.36 %) et ~22.2 % a w2 = 2.02
(sonde v2 log l.33/42/51 : 21.89 -> 22.04 -> 22.18 %). Une limite finie qui varie avec
w2 est une propriete du systeme : 2 eta est un autre point physique.
L'extension E-B de l'erratum Q2 n'est plus une conjecture ; elle est
demontree a deux points.

(iii) FAIT 1-bis, LA LECON DE GEL LA PLUS TRANCHANTE : la clause N -> N+p
a MESURE la non-convergence (3.28 %, banc v2 log l.25) et rendu quitus,
parce que son pas de test (5 couches) est plus court que l'echelle de
convergence (10 : 10->15 = 3.2770 %, 15->20 = 0.0160 %, sonde v1 note
FAIT 1-bis, verifie). L'erratum doit corriger le PAS ou le CRITERE, pas
seulement la direction.

(iv) LE CRITERE DE LA SONDE v1 EST REFUTE PAR LE SECOND POINT -- et c'est
machine 2 qui l'a refute elle-meme (M16 / D-11 repaye sur sa propre
prescription). A w2 = 2.02, "Gamma_LS stationnaire sous +10 couches"
ACCEPTE la geometrie a dix couches (0.001113 < 0.0050, sonde v2 log l.67)
alors que la descente y explose a 29.70 % (l.36). Gamma_LS peut etre
converge en longueur d'absorbeur pendant que sa derivee en eta ne l'est
pas -- et c'est la derivee que P6 consomme. Le CRITERE CORRIGE (les deux
derniers pas de la descente sous tau_LS) est decision-identique aux deux
points (six cellules), et DECLARE ajuste sur ses donnees : il est DU aux
quatre points restants avant d'entrer au gel (~15 min a la loi de cout).

(v) FIL OUVERT : a 2.02 le PREMIER pas de descente reste ~9 % a toutes
les longueurs (l.36, 41-45, 50-51). La descente demarre rugueuse meme
convergee -- ce qui plaide pour un OPERATIF PAR RICHARDSON sur les deux
derniers pas (le banc le calcule deja : 2.299062e-10, banc v2 log l.80),
residu declare, comme Q2 l'a fait pour E-A.

(vi) PROPOSITION (d), MAINTENUE SANS ETRE TRANCHEE : si le recouvrement a
3 % (fumee v7) se confirme fragile aux autres points, la largeur ponderee
somme(|c_nu|^2 Gamma_nu) reste l'objet naturel. A instruire seulement si
(a)+(b) ne suffisent pas.

Ordre machine 1, inchange et affine : (a) necessaire et bon marche, (b)
lisible seulement grace a (a), donc (c) -- avec critere re-teste aux
quatre points AVANT tout gel.

## 4. RESOLUTIONS D'INSTRUMENT (E15) A DECLARER A L'ACTE

- CONDITIONNEMENT EN eta : 1.54e11 (entree 8.327e-16 -> sortie 1.282e-04,
  determinisme verifie au bit, banc v2 log l.29-31). Consequences : eta se
  porte en UNE SEULE forme derivee declaree (les deux conventions du meme
  gel rendent deux Gamma_LS a 1e-4 -- cause retroactive de D-M17-27 de la
  rectification) ; toute tolerance plus fine que ~1e-3 est hors de portee
  de l'instrument.
- FENETRE PRATICABLE : r_c = 40 est un PLANCHER (les lignes a petite
  echelle echouent pour la bonne raison : absorbeur DANS la barriere,
  banc v2 log l.36-39) ; plafond pratique N ~ 70 (93-94 s par eig), les
  lignes N = 90 / 120 sont EXTRAPOLEES, jamais mesurees (l.86-91, 1.96 et
  6.18 Go). La parade a D-B3 vit dans N - r_c en [10, 30] ou elle ne vit
  pas. N_max = 120 est declare au gel et inatteignable en pratique :
  "infaisable en-deca de N_max" devient sa propre categorie G-5.

## 5. RECOMMANDATIONS MACHINE 1 -- RAPPEL ET MISES A JOUR

- D-B2 : PARAMETRE p plutot que moteur separe (couche exacte deja
  generale ; custody unique). v9 sur ordre de l'acte.
- D-B1 : G-4 nait au meme geste (elle n'a de lieu qu'a p pair).
- Q2 etendu : la clause tau_LS(eta) passe en descente/Richardson pour E-B,
  au meme erratum ou a son jumeau.
- Regles (alpha) et (beta) : a numeroter comme regles de campagne ; elles
  completent D-M17-22 par les deux bouts.
- Critere d'absorbeur : ne gele qu'apres les quatre points restants.

## 6. SEQUENCE PROPOSEE v2 -- OPINION

1. REGISTRE : resoudre la collision de numerotation (les six defauts de
   la rectification -> 26..31, proposition machine 1).
2. SONDE COMPLEMENT : le critere corrige aux quatre points restants
   (machine 2, ~15 min) -- AVANT de geler l'erratum (c).
3. UN SEUL ACTE : erratums Q1..Q4 ; questions D-B1..D-B3 avec directions
   arretees ; resolutions E15 (conditionnement eta, fenetre praticable,
   infaisable en-deca) ; regles (alpha)/(beta) ; faits D-F1/D-F2 ;
   defauts de custody renumerotes ; rectifications assumees.
4. v9 du script (p parametre, G-4, cles d'erratum) ; contre-certification
   aux ancres ; pilote opposable ; lecture ; run.

La rectification a rendu a la journee sa propriete la plus precieuse :
tout ce qui est affirme est desormais porte par une piece qui le montre,
y compris les fautes. C'est l'etat dans lequel une manche peut se piloter.

-- FIN note_machine1_bilan_journee_m17_v2 --
