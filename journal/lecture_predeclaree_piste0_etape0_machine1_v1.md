# LECTURE PRE-DECLAREE -- PISTE (0), ETAPE 0 -- machine 1 -- 11/11/2026
# Lecture a ZERO RUN des artefacts du run M17 (dossier manche_m17_v17)
# CLASSE 3 (hors chaine, aucun verdict de manche, aucune porte nouvelle)

ETAPE   : piste (0), etape 0 -- budget d'absorbeur de Gamma_LS aux six
          points f070 du run M17
FICHIERS: dossier manche_m17_v17 (36 pieces, MANIFEST machine 2
          4aecd0e2b23bc818, manifeste au registre sous
          journal/manche_m17_v17_MANIFEST_machine2.txt), recu de
          l'operateur en un ZIP le 11/11/2026
LIVRABLE: table par point + cinq lectures ci-dessous + JSON et log
CIBLE   : decider le contenu de l'etape 1 (gel court de qualification)
CLASSE  : 3

## 0. ETAT DE LA PLUME AU MOMENT D'ECRIRE (ce qui est deja connu)

Ecrit AVANT toute ouverture d'un fichier pt_*.json. Seuls ont ete lus :
la liste des noms et tailles du ZIP ; le gel v12-b2 ; le script v17 ;
la note machine 2 du run ; l'assemblage depose (verdicts seulement).
Sont donc DEJA CONNUS, et ne peuvent pas compter comme aveugles :
  - l'allure de Gamma_LS sur la grille (creux a 2.02, pic a 2.05,
    facteur ~30 a 40), les six valeurs du jumeau H+ (~1e-14) ;
  - les nombres du NOMINAL portes par le gel 4.6 : translation 1.96
    pour cent, N + p 1.56 pour cent, recouvrement 2.8803 pour cent,
    poids total 0.867, ecart de la montante 15.36 pour cent, et la
    phrase "six points, six limites de 6 a 22 pour cent" ;
  - qu'aucun point f070 n'est en arret (donc que les deux portes G-3
    sont sous tau_LS = 0.05 aux six points).
Ne sont PAS connus : les indicateurs PAR POINT (hors nominal) -- pas de
descente, ecart 2 eta, translation, N + p, residu, recouvrement, poids
total, Gamma_pondere, nombre de resonances retenues, L retenu.

## 1. QUANTITES (noms du script v17, bloc EB de chaque pt_*_f070.json)

Par point i (six points : w2 = 1.95, 1.97, 1.98, 2.02, 2.03, 2.05) :
  G    = EB.Gamma_LS.H.Gamma_LS          (largeur a eta/8, celle que lit P6)
  R    = EB.operatif_4_6.Richardson ; r = EB.operatif_4_6.r
  res  = EB.operatif_4_6.residu_declare
  p1, p2, p3 = pas de la descente a la geometrie retenue
               (EB.critere_absorbeur.essais, essai accepte)
  m    = EB.temoin_montante.ecart        (2 eta)
  t    = EB.stationnarites.translation_p ; n = EB.stationnarites.N_plus_p
  rec  = EB.Gamma_LS.H.recouvrement ; W = EB.Gamma_LS.H.poids_total
  Gp   = EB.Gamma_LS.H.Gamma_pondere ; q = Gp / G
  nres = EB.Gamma_LS.H.n_resonances
  c    = EB.Gamma_LS.H.poids_cumule / W
  Hp   = EB.Gamma_LS.Hplus.Gamma_LS
  L    = EB.critere_absorbeur.L_retenu ; N, r_c, eta = EB.N, EB.r_c, EB.eta
  Lam  = EA.Lambda_c
Compte attendu, declare avant de compter : 6 fichiers f070 lus + 0
ecarte == 6 ; tout fichier sans bloc EB faisable est ECARTE et nomme.

## 2. REGLE "HORS PLAGE" (fixee ici, avant lecture)

Ensemble de reference O = {1.95, 1.97, 1.98, 2.03} ; points testes
T = {2.02, 2.05} (le creux et le pic). Pour un indicateur X :
lo = min_O X, hi = max_O X, w = hi - lo. X_j est HORS PLAGE si
X_j > hi + w ou X_j < lo - w (une largeur de plage au-dela de la plage :
la marge porte son echelle). Si w = 0 : HORS PLAGE si X_j != lo, et la
ligne porte la mention "plage nulle".
  Groupe A (absorbeur) : p1, p2, p3, m, t, n, |res|, L
  Groupe I (identite de l'etat) : rec, W, q, nres, c

## 3. LES CINQ LECTURES ET LEURS ATTENDUS

L-1 (COHERENCE, NON AVEUGLE). B_i = max(t, n, p3, |res|) au point i ;
    E = ln(max_i G / min_i G). Attendu : max_i B_i < 0.05 ET E > ln 10.
    Si max_i B_i >= 0.05 : les fichiers contredisent "aucun f070 en
    arret" -- defaut a verser, on s'arrete la. Si les deux tiennent :
    la structure de Gamma_LS en w2 n'est pas faite par l'absorbeur A
    L'ECHELLE DES PORTES (5 couches, un facteur 8 en eta), et rien de
    plus -- cette lecture ne dit rien d'un plateau en eta.

L-2 (AVEUGLE). A 2.05 : au moins un indicateur du groupe I est HORS
    PLAGE. Probabilite annoncee par la plume : 0.5.
L-3 (AVEUGLE). A 2.05 : aucun indicateur du groupe A n'est HORS PLAGE.
    Probabilite annoncee : 0.6.
    Table de lecture de (L-2, L-3) au pic :
      I hors plage, A dans la plage  -> ANOMALIE D'ETAT : le pic est
          candidat a un effet d'UN etat (croisement evite) ; l'etape 1
          doit lire les largeurs des etats voisins (T-etats).
      A hors plage                   -> ANOMALIE D'ABSORBEUR : le pic est
          suspect ; T-eta est decisif a ce point.
      ni I ni A                      -> pic SANS SIGNATURE sur les
          indicateurs disponibles ; l'etape 0 n'apprend rien sur lui.
    Le creux 2.02 est consigne par la meme regle, SANS attendu.

L-4 (AVEUGLE). Rang de Spearman rho(G, Gp) sur les six points, seuil
    de la campagne a n = 6 : 29/35. Attendu : rho >= 29/35 avec
    probabilite annoncee 0.4. Si rho < 29/35 : les deux definitions du
    taux n'ordonnent pas la grille de la meme facon, et tout verdict de
    rang depend de la definition. Consigne en plus, SANS VERDICT ET
    DECLARE EXPLORATOIRE : rho(rangs de Gp, rangs de -Lam), c'est-a-dire
    P6 (i) relu sous la largeur ponderee ; et rho(G, R), attendu 1.

L-5 (AVEUGLE). Signe du dernier pas de descente, lu sans les valeurs
    intermediaires (non stockees) : signe(R - G) = signe(G(eta/8) -
    G(eta/4)) puisque R = G + (G - G4) r/(1-r) avec 0 < r < 1.
    Attendu : MEME SIGNE aux six points, probabilite annoncee 0.6.
    Signes meles = les points ne sont pas dans le meme regime de la
    trajectoire en eta, et P6 a compare des regimes differents.

## 4. CE QUE L'ETAPE 0 NE PEUT PAS DIRE (ecrit avant)

Elle ne teste ni l'existence d'un plateau en eta sous eta/8, ni la
forme de l'absorbeur, ni un deplacement de plus de 5 couches, ni un
temoin positif. Les pas de descente sont stockes en valeur absolue :
la trajectoire G(eta) n'est pas reconstructible au-dela du signe du
dernier pas. Les points f050 (arret) et P8 sont consignes pour leur
motif, sans lecture. Une lecture "sans anomalie" n'est pas une
qualification de l'estimateur.

-- FIN --
