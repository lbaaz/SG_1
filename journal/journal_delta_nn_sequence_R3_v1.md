# JOURNAL DELTA nn -- SEQUENCE R3 : UNE PREDICTION HORS ECHANTILLON TENUE PAR UN ESTIMATEUR SANS PARAMETRE,
# PROMOTION 49.5 DE P-A-1 ET P-D-1 -- v1 (brouillon machine 1, a certifier par machine 2 avant depot)
Auteur : machine 1. Date : 08/09/2026. Classe 1 (acte de registre). Numero : pris AU DEPOT (E18) ; "nn" jusque-la.
Registre au brouillon : HEAD 0ff330b (delta 86), verifie sur clone frais le 07/09 ; aucun depot depuis.
Regles : (P) et (X) en vigueur ; aucune regle nouvelle. Aucun signe pour cent dans cet acte.

nn.1  OBJET
  Entre le 07/09 (machine 2 indisponible) et le 08/09, machine 1 a produit en classe 3 deux estimateurs classiques de
  la largeur quantique T_shell de la route A2 (p = 4) : la fraction d'echappement de Wigner (TWA, zero parametre,
  hbar explicite) et la protection de la famille par la phase (r_gen, invariant d'echelle). Leurs predictions sur le
  RANG des dix T_shell a une profondeur jamais calculee (s = 0.8 s*) ont ete gelees, recues par machine 2, puis jugees
  sur un run de machine 2. Cet acte promeut P-A-1 et P-D-1 par re-derivation (49.5) et consigne l'incident de transit.

nn.2  PIECES (convention B : sha256 NFC+LF, 16 hex ; classe entre crochets ; detenteurs : les deux machines sauf mention)
  Predictions, AVANT le run :
    gel P-A 539040b906256194 (P-A-1 rang, P-A-2 ordre par la profondeur, P-A-3 temoin) [3]
    gel P-D 6576c0b0360c120b (P-D-1 rang par -r_gen ; P-D-2 p = 5 non joue ; P-D-3 temoin) [3]
    notes de derivation : branche A 5e871a13ee6c8a5f ; branche D 890f261fbac112ca [3]
    lot de reprise REPRISE v1, manifeste 2e5605191257b0bc, porteur des deux gels, RECU par machine 2 avant le run
    (cite dans son lot) ; REPRISE v2 9061e960af56e2d4 [3]
  Run et lectures :
    lot machine 2 R3 v1, canon 7d905230a792ab30 : mesures 56526d9cd2f9e0e8, pre-vol 2cddc987e4aa0a02, feuille de
    lecture b1bfabb6234b571e, note 060c2be97bcf0c1c, script 6beaeba02a6da8f9 [3]
    lecture machine 1 21405bced28a8c05 (lot 07b3ed2942861461) ; complement machine 2 3b46a72916ab1d7a ; reponse
    machine 1 d7a50a022d9d4dab ; consigne machine 2 b52f4108ac48e48a ; cloture machine 1 74c07f98d3f20fbd [3]
  Contexte de la periode (classe 3, non promu, cite pour la trace) : lots D1 v5 ae36b13b35b49ced, T1 v2
    ae32abcf62145a76, brancheA v1 14cb7ca84a2434d5, brancheD v1 5116f8abdfbe43d5 ; cartographie 4e2511a4d15783fc ;
    SUIVI 08e18edf08c4c0aa, 8142c57e44729ba5, 68fc215b6201df90, f9a123dbdf2df8b5.
  Moteur : m9_replication_v1.py c8ed357b120352c4 (lecture seule, p = 4 en memoire, fichier non modifie).

nn.3  DESIGN ET RUN (machine 2, BOCAL4, 07/09 ; mesures 56526d9cd2f9e0e8)
  Route A2 : p = 4, W1 = 1, nbar1(s*) = 7.04, dix w2 (1.25 .. 2.85), C de la table A2 (journal bundle5, l.405),
  g = C (1 + w2^2)^2 (w2 - 1) / (2 x 7.04), s* = sqrt(2 x 7.04 Delta) / (1 + w2^2), s = 0.8 s*, graine coherente
  (a1 = +sqrt(n1), a2 = -sqrt(n2)), N = 64, methode kron (X tronque puis eleve a la puissance 4), coquille
  35 <= max(n1, n2) <= 45 (891 etats aux dix points), fantome et jumeau NULL+.
  Re-derivation machine 1 : g, s*, s, X1, X2, n1, n2 recalcules des formules, ecart relatif maximal 0.00e+00
  (tolerance declaree avant : 1e-12). Temoin P-A-3 (point moyen classique, RK4 dt 0.006, T = 400, CAP 1e4) : 10 joues,
  0 explosent. Pre-vol de machine 2 a 0.7 et 0.9 s* : reproduit les 20 T_shell de machine 1 (replique kron, lot
  brancheA) a 3.6e-11 relatif -- la chaine est celle de machine 1, reecrite independamment.

nn.4  VERDICTS (deux lectures independantes, identiques au chiffre ; fractions exactes, aucun ex aequo)
  Valeur critique : rho_c(n = 10, alpha = 0.05 unilateral) = 31/55 = 0.5636 par enumeration des 10! permutations
  (P(sum d^2 <= 72) = 0.0481) ; le 0.564 ecrit dans les gels en est l'arrondi, marginalement plus exigeant.
  P-A-1  rho(T_shell(0.8), f_esc TWA) = 113/165 = 0.6848 (sum d^2 = 52), p exact = 0.0173.      TENUE.
  P-D-1  rho(T_shell(0.8), -r_gen)   = 127/165 = 0.7697 (sum d^2 = 38), p exact = 0.0063.      TENUE.
  P-A-2  rapport V/B = 0.3585, V = {1.60, 1.80, 2.00, 2.40}, B = {1.25, 1.35, 2.85} : strictement entre 0.224 (0.7 s*)
         et 0.569 (0.9 s*), et entre 0.225 et 0.634 (journal).                                     TENUE.
  P-A-3  0 temoin sur 10 explose.                                                                  TENUE.
  Consigne sans porte : rho(T_shell(0.8), -r_gauss(0.8)) = 101/165 = 0.6121 (r_gauss 6c3cc45748e54061, producteur
  2bcd3dc5620c9b26 authentifie a 3.8e-16). Compte : portes 4, tenues 4, non tenues 0, non evaluables 0.

nn.5  CE QUE L'ACTE ETABLIT ET CE QU'IL N'ETABLIT PAS
  Etabli (classe 1 par cet acte) : P-A-1 et P-D-1, predictions ordinales deposees avant le run, jugees hors echantillon
  en donnees (0.8 s* n'avait jamais ete calcule par personne) ; c'est la premiere prediction quantitative tenue au
  volet quantique de la campagne depuis C2 (M9), et le premier mediateur classique de la degenerescence C / g_eff
  (ouverte depuis le 25/07) a tenir chez l'autre machine.
  Non etabli : les VALEURS de T_shell (non gelees, non convergees, R-A-1) ; le facteur T_shell / f_esc (0.10-0.26,
  R-A-3) ; le lien r_gen <-> TWA au-dela de la co-ordination ; tout ce qui concerne 2:1 a degre impair (P-D-2, non
  joue). Portee du test : 0.8 s* est ENTRE les deux profondeurs (0.7, 0.9) ou les estimateurs ont ete lus --
  hors echantillon en donnees, dans l'intervalle en profondeur ; une extrapolation (0.6 ou 0.95 s*) n'a pas ete
  jouee. Les f_esc du gel portent un bruit de Poisson (400 tirages) : la prediction tenue est un rang, pas un nombre.
  Estimateur C2 : le TWA n'est PAS un estimateur quantique derive ; C2 reste fermee (pas de manche quantique sans
  estimateur derive) ; l'acte n'ouvre aucune manche.

nn.6  DEFAUTS ET INCIDENT (tous verses dans les pieces citees ; aucun corrige en place, PB-1)
  D-REPRISE-1 (machine 1) : quatre lots de classe 3 livres sans reception confirmee, files retrouves dans les cartes
    des chats ; transit fautif, aucune piece perdue. Geste correctif sans regle neuve : canon annonce dans le message,
    reception confirmee avant la livraison suivante.
  D-A-3 (machine 1, note branche A, I2) : illustration numerique retiree (valeurs "exact" au couplage perime D-A-2,
    valeurs "kron" d'origine inconnue) ; l'enonce "deux troncatures sous le meme nom" reste candidat, non mesure.
  D-D-1 (machine 1) : sortie r_gauss_v1.json deposee sans son producteur ; producteur retrouve et livre.
  Machine 2 : R0.5 (constat de perte) retracte par elle-meme en 3b46a72916ab1d7a. Residus ouverts : R-A-1..3, R-D-1..4.

nn.7  ATTENTES
  Certification de cet acte par machine 2 (re-derivation des fractions et des comptes ; numero au depot) ; depot.
  Decisions operateur non prises par cet acte : delta P-4 (jambes D / S, T = 6400) ; R4 (tests D1) ; R5 (p = 5) ;
  O3 ; relance Held (note e seule) apres le depot P-4. Revue (P)/(X) au 28/09.
-- FIN DE L'ACTE (brouillon v1) --
