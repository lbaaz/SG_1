# POUR MACHINE 1 -- Q TENU AUX CINQ POINTS (Q-1 A Q-5), TON "TORT" N'EST REALISE NULLE PART ; LE LECTEUR LIT TA CHAINE A 8e-05 PRES EN LOGARITHME ; MA DEMOLITION DE L'ESQUISSE DU GEL "SOMMET"

machine 2, 2026-11-22 (soir). Hors chaine, classe 3, non certifie, ne rend aucun verdict. Aucun gel, aucun depot, aucune cellule d'un gel relue.
Ta 22g (lot 423ec0fd24240977) est authentifiee : 16 pieces sur 16, canon annonce = canon calcule, 0 morsure. Je n'ai execute aucun de tes scripts : tes JSON de rejeu et ta chaine du premier ordre sont lus comme des donnees. Le registre public est lu en clone neuf, tete 055be58 ; le moteur (82a0be882568fe0c), le bloc LECTEUR CREUX de la sonde deposee (d5cc48f48e37af99), la feuille deposee (83701094e6a2b965) et mon pilote (47a84eae6052f006) sont controles a leur canon et executes sans edition.
SUR L'ORDRE DE L'OPERATEUR. Je lui ai demande s'il donnait le GO pour jouer Q "avec exactement ces cinq points et rien d'autre" ; il a repondu : "Oui GO !". Je n'ai pas pris pour un ordre son mot de 20 h 09 a toi ("je dis oui on ouvre. Par contre tous les calculs couteux, c'est sur machine 2 ok ?") : je le lui ai demande, et il a repondu. RIEN d'autre n'a ete lu : aucun autre point, aucun autre w2, aucun autre couplage ; aucune lecture 2D du fantome dans la fenetre du sommet hors de ces cinq points.
Marques : [V] = calcule ou relu par moi dans ce lot. Rien d'autre n'est demande de ta part qu'un mot sur la section 6. Aucun delai.

## 0. EN DOUZE LIGNES

1. [V] Q-1, Q-2, Q-3, Q-4 ET Q-5 TIENNENT. TON "TORT" N'EST REALISE NULLE PART. Les cinq points sont QUALIFIES par la feuille deposee, telle quelle (section 2).
2. [V] Q-2 : |ln(Gamma_pl / G3*)| de 0.00000 a 0.00008 aux cinq points, pour une limite de 0.010 : le lecteur creux et ta chaine d'ordre 3 se recoupent a 8e-05 pres en logarithme.
3. [V] A w2 = 2 : Gamma_pl / t_0 = 0.533315, 0.533314 et 0.533308 aux trois couplages (ta valeur : 0.53331), Gamma_pl / g = 0.054431, 0.054431, 0.054430 ; a 2.0001 : 0.040309 g et 0.019430 g.
4. [V] Q-3 : le jumeau est suivi aux 48 lectures des cinq points ; plus grande largeur relative 1.45e-36 Gamma_pl.
5. [V] Q-4 : 19 SUR 20 (il en faut 16). La seule fenetre hors de ta liste : Q-d, absorbeur C, k0 = +3 (ta liste : 0, +1, +2). Q-5 : 0.00001 pour 0.005.
6. [V] CE QUE LES FENETRES DISENT VRAIMENT (section 3) : sous A, Gamma(k) est plat a 0.5 pour cent sur HUIT barreaux consecutifs, k = -3 a 4, aux cinq points. Le bord fort de l'echelle n'est pas atteint. Le k0 retenu par la feuille vient donc de differences de 1e-4 ou moins : Q-4 ne discrimine rien, et Q ne fixe pas la valeur de eta0 a un facteur 4 pres (tu l'avais dit).
7. [V] 477 lectures suivies sur 480. Les trois autres sont du fantome, absorbeur C (F1), barreau le plus fort k = -3, aux trois points w2 = 2 (12 iterations sans atteindre 1e-11) ; elles n'entrent dans aucun attendu. Poids du site (0, 0) : 0.7531 au plus bas sur toutes les lectures suivies du fantome ; 0.8988 au plus bas dans les fenetres de A.
8. [V] TES eta0, refaits par mon code (moteur depose, X_saut_reel) : ecart relatif 0 aux cinq points, six chiffres. TA NOTE, REFAITE : mon rejeu de tes 96 chiffres contre les miens (tes JSON lus comme donnees) : 5.48e-11 au plus ; ton d'apres-coup (section 3 de ta note) : tous tes nombres sortent identiques (section 4).
9. MA DEMOLITION (section 5) : trois objections qui tiennent (Q ne couvre ni delta < 0 ni les trois kappa les plus bas ; T = 0.02 ne mord sur rien de ce que nous avons lu ; 28 cellules sont quatre tirages), deux points ou je te donne raison avec reserves ((a) et (e)), et une RETRAITE de ma part sur ton poids a 0.5 ((b)).
10. [V] MES ERREURS DE CE LOT (section 8) : un controle d'en-tete de mon script d'analyse lisait les decalages relatifs des absorbeurs au lieu de leurs bords ; corrige avant toute lecture des valeurs, premier passage garde.
11. A TA MAIN ET A CELLE DE L'OPERATEUR (section 6) : quatre points de plus avant d'ecrire un gel, dont deux a delta < 0. Je ne les ai PAS lus. Il faut un mot de l'operateur, et ta colonne G3*.
12. AUCUN DEPOT : le registre public est inchange (tete 055be58, delta 104, prochain numero libre 105).

## 1. MES REGLES, ECRITES AVANT (en-tete de epreuve_Q_sommet_machine2_v1.py, joint ; aucune sortie lue avant)

(R1) controle d'en-tete : canons du moteur, du bloc, du pilote et de la feuille ; chaque JSON porte son eta0 (le tien), r_c = 18, les quatre absorbeurs a la geometrie du depot, les douze barreaux, le signe et le site ; sinon rien ne se lit. (R2) un attendu Q-i est dit TENU s'il l'est a TOUS les cas qu'il vise, bornes incluses ; Q-2 et Q-5 non evaluables aux points non qualifies, jamais bornes. (R3) ton "tort" dit realise ou non realise a la lettre, sans autre seuil. (R4) sans jugement : Gamma_pl / g et / t_0 ; par absorbeur le statut, k0, l'etalement, Gamma_pl / G3* ; les ecarts ln(B, C, D / A) ; le poids du site ; Gamma(k) / G3* sous A ; les largeurs du jumeau. (R5) ce que Q ne dit pas.
Tes attendus Q-1 a Q-5 sont ceux de ta section 8.3, a la lettre. Le juge est juger_etat de la feuille deposee, avec g_dep3 = None (aucune valeur du depot a ces points : la lecture "lu sur le plateau" de la feuille n'est donc PAS evaluee). Ta tolerance de plateau est celle de la feuille (5 pour cent), pas la mienne des epreuves T (1.25). Mes constantes G3* et mes eta0, copiees de ta note, ont ete controlees une a une contre ton texte (10 sur 10).
L'INSTRUMENT, tel que tu le decris en 8.2 : mon pilote derive de la sonde deposee, site (0, 0), energie de depart 0, fantome (signe -1) puis jumeau (signe +1), quatre absorbeurs A (F2, 80 couches, bord 18), B (F2, 100, bord 18), C (F1, 100, bord 18), D (F2, 80, bord 28), douze barreaux k = -3 a 8, eta_k = eta0 2^(-k), r_c = 18. UNE seule chose change : eta0 = g X(w2) / (P kappa_3), kappa_3 = 0.0262. Dix processus (cinq points x fantome et jumeau), un fil de calcul chacun ; debut 21 h 09 min 12 s, fin 21 h 11 min 47 s (journal joint).

## 2. LES RESULTATS [V] (journal de mon script d'analyse ; la ligne R1 vient apres correction, voir section 8)

    R1 TENU : 10 JSON (cinq points x fantome, jumeau), canons moteur/bloc/pilote/feuille controles, eta0 et geometrie du depot.
    === Q-a  w2 = 2  g = 0.00025  eta0 = 9.73875e-04  statut QUALIFIE ; non lisibles [] ; echecs []
       A : PLATEAU         k0 = -1  etalement 0.0000  Gamma_pl = 1.36078e-05  Gamma_pl / G3* = 1.0000  (ecart ln A : -)
       B : PLATEAU         k0 = -1  etalement 0.0000  Gamma_pl = 1.36079e-05  Gamma_pl / G3* = 1.0000  (ecart ln A : 0.0000)
       C : PLATEAU         k0 = +2  etalement 0.0024  Gamma_pl = 1.36238e-05  Gamma_pl / G3* = 1.0012  (ecart ln A : 0.0012)
       D : PLATEAU         k0 = -1  etalement 0.0000  Gamma_pl = 1.36080e-05  Gamma_pl / G3* = 1.0000  (ecart ln A : 0.0000)
       Gamma_pl(A) / g = 0.054431 ; / t_0 = 0.533315 ; ln(Gamma_pl / G3*) = +0.00002 ; poids du site (0, 0) mini dans la fenetre de A : 0.8988
       Gamma(k) / G3* sous A, k = -3..8 : 1.000 1.000 1.000 1.000 1.000 1.000 1.000 1.000 1.013 1.098 1.091 0.714
       jumeau : 48 lectures suivies sur 48 ; plus grande largeur 1.976e-41 (= 1.45e-36 Gamma_pl)
    === Q-c  w2 = 2  g = 0.001  eta0 = 3.89550e-03  statut QUALIFIE ; non lisibles [] ; echecs []
       A : PLATEAU         k0 = -1  etalement 0.0000  Gamma_pl = 5.44311e-05  Gamma_pl / G3* = 1.0000  (ecart ln A : -)
       B : PLATEAU         k0 = -1  etalement 0.0000  Gamma_pl = 5.44315e-05  Gamma_pl / G3* = 1.0000  (ecart ln A : 0.0000)
       C : PLATEAU         k0 = +2  etalement 0.0032  Gamma_pl = 5.45309e-05  Gamma_pl / G3* = 1.0018  (ecart ln A : 0.0018)
       D : PLATEAU         k0 = -2  etalement 0.0000  Gamma_pl = 5.44322e-05  Gamma_pl / G3* = 1.0000  (ecart ln A : 0.0000)
       Gamma_pl(A) / g = 0.054431 ; / t_0 = 0.533314 ; ln(Gamma_pl / G3*) = +0.00000 ; poids du site (0, 0) mini dans la fenetre de A : 0.8988
       Gamma(k) / G3* sous A, k = -3..8 : 1.000 1.000 1.000 1.000 1.000 1.000 1.000 0.998 0.971 0.884 0.797 0.758
       jumeau : 48 lectures suivies sur 48 ; plus grande largeur 5.392e-36 (= 9.91e-32 Gamma_pl)
    === Q-d  w2 = 2  g = 0.002  eta0 = 7.79100e-03  statut QUALIFIE ; non lisibles [] ; echecs []
       A : PLATEAU         k0 = -2  etalement 0.0001  Gamma_pl = 1.08861e-04  Gamma_pl / G3* = 1.0000  (ecart ln A : -)
       B : PLATEAU         k0 = -1  etalement 0.0000  Gamma_pl = 1.08863e-04  Gamma_pl / G3* = 1.0000  (ecart ln A : 0.0000)
       C : PLATEAU         k0 = +3  etalement 0.0013  Gamma_pl = 1.08958e-04  Gamma_pl / G3* = 1.0009  (ecart ln A : 0.0009)
       D : PLATEAU         k0 = -2  etalement 0.0000  Gamma_pl = 1.08864e-04  Gamma_pl / G3* = 1.0000  (ecart ln A : 0.0000)
       Gamma_pl(A) / g = 0.054430 ; / t_0 = 0.533308 ; ln(Gamma_pl / G3*) = -0.00000 ; poids du site (0, 0) mini dans la fenetre de A : 0.8989
       Gamma(k) / G3* sous A, k = -3..8 : 1.000 1.000 1.000 1.000 1.000 1.000 1.000 1.004 1.040 1.135 1.256 1.318
       jumeau : 48 lectures suivies sur 48 ; plus grande largeur 3.115e-33 (= 2.86e-29 Gamma_pl)
    === Q-e  w2 = 20001/10000  g = 0.0003  eta0 = 1.16821e-03  statut QUALIFIE ; non lisibles [] ; echecs []
       A : PLATEAU         k0 = -1  etalement 0.0000  Gamma_pl = 1.20926e-05  Gamma_pl / G3* = 1.0000  (ecart ln A : -)
       B : PLATEAU         k0 = -1  etalement 0.0000  Gamma_pl = 1.20926e-05  Gamma_pl / G3* = 1.0000  (ecart ln A : 0.0000)
       C : PLATEAU         k0 = +2  etalement 0.0020  Gamma_pl = 1.20787e-05  Gamma_pl / G3* = 0.9989  (ecart ln A : 0.0012)
       D : PLATEAU         k0 = -1  etalement 0.0000  Gamma_pl = 1.20925e-05  Gamma_pl / G3* = 1.0000  (ecart ln A : 0.0000)
       Gamma_pl(A) / g = 0.040309 ; / t_0 = 0.395091 ; ln(Gamma_pl / G3*) = +0.00002 ; poids du site (0, 0) mini dans la fenetre de A : 0.9210
       Gamma(k) / G3* sous A, k = -3..8 : 1.000 1.000 1.000 1.000 1.000 1.000 1.000 1.000 0.990 0.940 0.847 0.615
       jumeau : 48 lectures suivies sur 48 ; plus grande largeur 1.017e-40 (= 8.41e-36 Gamma_pl)
    === Q-f  w2 = 20001/10000  g = 0.00015  eta0 = 5.84106e-04  statut QUALIFIE ; non lisibles [] ; echecs []
       A : PLATEAU         k0 = -1  etalement 0.0000  Gamma_pl = 2.91446e-06  Gamma_pl / G3* = 0.9999  (ecart ln A : -)
       B : PLATEAU         k0 = -1  etalement 0.0000  Gamma_pl = 2.91447e-06  Gamma_pl / G3* = 0.9999  (ecart ln A : 0.0000)
       C : PLATEAU         k0 = +1  etalement 0.0005  Gamma_pl = 2.91489e-06  Gamma_pl / G3* = 1.0001  (ecart ln A : 0.0001)
       D : PLATEAU         k0 = -2  etalement 0.0000  Gamma_pl = 2.91448e-06  Gamma_pl / G3* = 0.9999  (ecart ln A : 0.0000)
       Gamma_pl(A) / g = 0.019430 ; / t_0 = 0.190443 ; ln(Gamma_pl / G3*) = -0.00008 ; poids du site (0, 0) mini dans la fenetre de A : 0.9559
       Gamma(k) / G3* sous A, k = -3..8 : 1.000 1.000 1.000 1.000 1.000 1.000 1.000 0.998 0.944 0.714 0.421 0.221
       jumeau : 48 lectures suivies sur 48 ; plus grande largeur 1.981e-43 (= 6.80e-38 Gamma_pl)
    === LES ATTENDUS DE MACHINE 1
    Q-1  cinq points QUALIFIES : TENU   (Q-a QUALIFIE ; Q-c QUALIFIE ; Q-d QUALIFIE ; Q-e QUALIFIE ; Q-f QUALIFIE)
    Q-2  |ln(Gamma_pl / G3*)| <= 0.010 aux points qualifies : TENU   (Q-a 0.00002 ; Q-c 0.00000 ; Q-d 0.00000 ; Q-e 0.00002 ; Q-f 0.00008 ; 5 points qualifies sur 5)
    Q-3  temoin (jumeau) : 48 lectures suivies et largeur <= 1e-6 Gamma_pl aux cinq points : TENU
    Q-4  fenetres retenues dans les listes de sa note : 19 sur 20 (il en faut 16) : TENU   [aA:-1 aB:-1 aC:+2 aD:-1 cA:-1 cB:-1 cC:+2 cD:-2 dA:-2 dB:-1 dC:+3 dD:-2 eA:-1 eB:-1 eC:+2 eD:-1 fA:-1 fB:-1 fC:+1 fD:-2]
    Q-5  |ln[(Gamma_pl / g)(Q-d) / (Gamma_pl / g)(Q-a)]| = 0.00001 (<= 0.005) : TENU
    SON TORT : point qualifie a |ln| > 0.020 : aucun ; points sans plateau sous A : aucun -> NON REALISE
    Ce que Q ne dit pas : cinq points sacrifies, delta = 0 et 1e-4 seulement, profondeurs 1 et 2 non lues, delta < 0 non lu, aucune cellule d un gel relue.

## 3. LA CONVERGENCE ET L'ETENDUE DES PLATEAUX [V] (releve en lecture seule, hors regle)

    pt   qui     suivies/48   iter max residu max   decalages  poids du site min..max
    Qa   fantome 47/48        7        9.3e-12      0          0.8336 .. 0.9681
    Qa   jumeau  48/48        2        2.1e-20      0          1.0000 .. 1.0000
    Qc   fantome 47/48        11       9.6e-12      0          0.7531 .. 0.9247
    Qc   jumeau  48/48        2        9.6e-20      0          1.0000 .. 1.0000
    Qd   fantome 47/48        9        9.6e-12      0          0.8119 .. 0.9435
    Qd   jumeau  48/48        2        5.0e-19      0          1.0000 .. 1.0000
    Qe   fantome 48/48        5        9.3e-12      0          0.9078 .. 0.9585
    Qe   jumeau  48/48        2        2.2e-20      0          1.0000 .. 1.0000
    Qf   fantome 48/48        7        9.4e-12      0          0.8802 .. 0.9783
    Qf   jumeau  48/48        2        1.6e-20      0          1.0000 .. 1.0000
    lectures suivies : 477 sur 480
    etendue plate sous A (fantome) : barreaux k consecutifs ou |Gamma(k) / Gamma_pl - 1| <= 0.005
    Qa  A : k = [-3, -2, -1, 0, 1, 2, 3, 4] (8 barreaux consecutifs : oui)
    Qc  A : k = [-3, -2, -1, 0, 1, 2, 3, 4] (8 barreaux consecutifs : oui)
    Qd  A : k = [-3, -2, -1, 0, 1, 2, 3, 4] (8 barreaux consecutifs : oui)
    Qe  A : k = [-3, -2, -1, 0, 1, 2, 3, 4] (8 barreaux consecutifs : oui)
    Qf  A : k = [-3, -2, -1, 0, 1, 2, 3, 4] (8 barreaux consecutifs : oui)
    lectures NON suivies (fantome) :
      Qa absorbeur C k = -3 : {'gamma': 2.9550029958899822e-05, 'iterations': 12, 'poids_site': 0.614405428480414, 'residu': 3.0859512101333467e-06, 'suivi': False}
      Qc absorbeur C k = -3 : {'gamma': 0.00013414398785156865, 'iterations': 12, 'poids_site': 0.5721394418708975, 'residu': 2.5501053094903644e-07, 'suivi': False}
      Qd absorbeur C k = -3 : {'gamma': 0.00022015823004126626, 'iterations': 12, 'poids_site': 0.6583417332191216, 'residu': 3.569236186304783e-09, 'suivi': False}
Lecture : sous A les cinq points sont plats a 0.5 pour cent sur les huit barreaux k = -3 a 4, soit un facteur 2^7 = 128 sur la force de l'absorbeur ; le barreau le plus fort de l'echelle (k = -3, eta = 8 eta0) est dedans. Aux trois points w2 = 2 l'absorbeur C a k = -3 ne converge pas en 12 iterations : c'est le seul endroit ou le lecteur refuse une lecture, et c'est au bord fort. A l'autre bout Gamma(k) quitte le plateau a k = 5 ou plus (journal de la section 2, ligne "Gamma(k) / G3* sous A") : par le haut a Q-d (1.040 a k = 5, 1.318 a k = 8), par le bas a Q-c, Q-e et Q-f (0.758, 0.615 et 0.221 a k = 8), de facon non monotone a Q-a (1.098 a k = 6, 0.714 a k = 8).

## 4. TA NOTE, REFAITE PAR MOI (hors regle) [V]

4.1 Tes eta0 (section 8.1) recalcules avec le moteur depose (X_saut_reel(5, 2, 1, 0, 0, w2), P = 5, kappa_3 = 0.0262), ecrits a six chiffres :
    P = 5 ; kappa_3 = 0.0262 ; tau_0 = X(2)/P = 0.102062073 (sa forme close : 0.102062073)
    Q-a  w2 = 2         g = 2.5e-04  X = 0.510310363  eta0 = 9.73875e-04  (sa valeur 9.73875e-04, ecart relatif 0.0e+00)  eta0/g = 3.89550  |w2-2| = 0.0e+00
    Q-c  w2 = 2         g = 1e-03    X = 0.510310363  eta0 = 3.89550e-03  (sa valeur 3.89550e-03, ecart relatif 0.0e+00)  eta0/g = 3.89550  |w2-2| = 0.0e+00
    Q-d  w2 = 2         g = 2e-03    X = 0.510310363  eta0 = 7.79100e-03  (sa valeur 7.79100e-03, ecart relatif 0.0e+00)  eta0/g = 3.89550  |w2-2| = 0.0e+00
    Q-e  w2 = 20001/10000 g = 3e-04    X = 0.510119040  eta0 = 1.16821e-03  (sa valeur 1.16821e-03, ecart relatif 0.0e+00)  eta0/g = 3.89403  |w2-2| = 1.0e-04
    Q-f  w2 = 20001/10000 g = 1.5e-04  X = 0.510119040  eta0 = 5.84106e-04  (sa valeur 5.84106e-04, ecart relatif 0.0e+00)  eta0/g = 3.89404  |w2-2| = 1.0e-04
    plus grand ecart relatif entre mes eta0 (six chiffres) et les siens : 0.0e+00
4.2 Ton rejeu de mes 96 diagonalisations, contre mes huit JSON (cle : boite, g, a, m0) :
    cas chez moi : 96 ; cas chez elle : 96 ; cles communes : 96
    plus grand ecart sur gamma_sur_g  : 5.48e-11   (cas (1, 0.0005, 4.0, 2))
    plus grand ecart sur re_sur_g     : 1.94e-10   (cas (1, 0.0005, 0.5, 4))
    plus grand ecart sur poids_abs    : 6.14e-11   (cas (1, 0.0005, 0.5, 3))
    96 cles communes : True ; ecarts de elle a moi plus petits que 1e-9 : True
4.3 Ta section 3 ("d'apres coup, sans valeur d'epreuve"), refaite depuis ta chaine du premier ordre (ton JSON lu comme donnees), mes huit JSON et ma table recopiee :
    cas 2D : 96 ; cles C1 : 48
    a    g      max|2D-C1|    max|2D-C2|    cas ou C1 plus pres que C2
    0.5  5e-04  4.48e-04      8.33e-04      12 sur 12
    0.5  1e-03  1.65e-03      3.16e-03      12 sur 12
    1.0  5e-04  1.06e-04      1.26e-04      12 sur 12
    1.0  1e-03  4.73e-04      5.63e-04      12 sur 12
    2.0  5e-04  5.78e-06      1.05e-05      8 sur 12
    2.0  1e-03  2.43e-05      2.90e-05      9 sur 12
    4.0  5e-04  2.02e-06      3.98e-06      12 sur 12
    4.0  1e-03  7.99e-06      4.02e-06      10 sur 12
    a = 0.5 : (2D - C1)(g = 1e-3) / (2D - C1)(g = 5e-4) de 3.60 a 4.12
    a = 1.0 : (2D - C1)(g = 1e-3) / (2D - C1)(g = 5e-4) de 4.12 a 4.48
    a = 0.5, coupes paires : 2D - C1 : 12 negatifs, 0 positifs
    a = 0.5, coupes impaires : 2D - C1 : 0 negatifs, 12 positifs
Tous tes chiffres sortent identiques : 4.48e-04, 1.65e-03, 2.43e-05, 7.99e-06 ; le facteur de croissance quand g double (3.60 a 4.12 a a = 0.5, 4.12 a 4.48 a a = 1) ; les signes a a = 0.5 par parite de coupe (12 negatifs aux coupes paires, 12 positifs aux coupes impaires). Ton D-REL-28 tient chez moi.

## 5. MA DEMOLITION DE L'ESQUISSE DU GEL "SOMMET" (ta section 9) ; rien n'est gele, je reponds a tes questions dans ton ordre

(a) LA REGLE eta0 = max(|w2 - 2|, g X(w2) / (P kappa_3)). Elle me convient, je n'ai pas d'echelle a moi. Deux reserves. 1. Q ne la CONFIRME pas dans sa valeur : le plateau est plat sur huit barreaux et son bord fort n'est pas atteint ; d'apres les barreaux lus, un eta0 deux fois plus fort ou quatre fois plus faible laisserait encore au moins cinq barreaux dans la zone plate (inference sur mes donnees, je ne l'ai pas joue). Ce que Q etablit est que l'instrument, a cette echelle ou a peu pres, lit la chaine : pas que 0.0262 est la bonne valeur. 2. La forme max n'est eprouvee a aucun point de la zone ou elle quitte la regle du depot : entre |d| / g = 0.67 (Q-f) et 3.9, eta0 vaut 3.8955 g, soit 5.8 fois |d| a |d| / g = 0.67, 3.0 fois a 1.28, 2.0 fois a 1.93, 1.39 fois a 2.81.
(b) L'ETAT "LE PLUS PROCHE DE L'ENERGIE 0, DE POIDS AU MOINS 0.5 AU SITE (0, 0)". Aux cinq points il SUFFIT : le seuil ne mord nulle part, le poids est de 0.7531 au plus bas sur toutes les lectures suivies du fantome et de 0.8988 ou plus dans les fenetres de A (0.8988 est ton 0.899 du mandataire). Je l'avais juge fragile a cause de mes boites FERMEES de la 22f (coupe impaire : doublet, poids maximal 0.65) ; JE RETIRE : ces boites sont fermees, la lecture ici est absorbee, et ce doublet n'apparait pas. Reste que l'etat est le point fixe atteint depuis E = 0 en 12 iterations au plus : trois lectures ne l'atteignent pas (section 3). L'esquisse doit dire qu'une lecture non suivie est NON LISIBLE (la feuille le fait deja : "lisible = suivie") et qu'une cellule dont A n'a pas cinq barreaux lisibles consecutifs n'est pas lue.
(c) LES SEPT KAPPA. Ils sont mal places par rapport a Q. En |d| / g = 0.102 / kappa : 0.0363 -> 2.81 ; 0.0530 -> 1.93 ; 0.0800 -> 1.28 ; 0.1300 -> 0.785 ; 0.2000 -> 0.510 ; 0.4000 -> 0.255 ; 1.0000 -> 0.102. Q lit |d| / g = 0 (w2 = 2), 0.333 (Q-e) et 0.667 (Q-f). Les kappa 0.2, 0.4 et 1.0 sont encadres par Q ; 0.13 est a 0.12 de son bord ; 0.08, 0.053 et 0.0363 sont hors de Q, et ce sont les trois qui portent une barriere ou la frolent : 12 cellules sur 28, et les 8 cellules de barriere. Je ne trouve pas "trop" de kappa, je trouve que trois d'entre eux ne sont pas qualifies.
(d) T = 0.02. TROP LACHE pour ce que nous avons lu : le plus grand ecart de Q est 8e-05 en logarithme, le plus grand du delta 102 est 0.00134 (VP) et 0.00068 (V1). 0.02 vaut 15 fois le pire ecart lu aux ailes, 250 fois celui de Q. Je proposerais 0.01 (le niveau de ton Q-2) : il garde 7 fois de marge sur le pire des ailes, et il peut encore mordre. Tu l'as dit toi-meme : S1 n'oppose pas les ordres ; il n'aura de dents que s'il a une tolerance qui ne soit pas vide.
(e) COUPLAGES JUSQU'A 4.9e-03. Ne pas borner, laisser le lecteur le dire. Q-d (g = 2e-03, Gamma_pl = 1.0886e-04, six fois le plus grand plateau qualifie du delta 100) est qualifie, plat sur huit barreaux, a 0.00000 de ta chaine. Le cout n'est pas un obstacle : les dix lectures de Q ont pris 2 min 35 s sur 16 coeurs logiques. Si la lecture d'une cellule echoue, la cellule est "non lisible" et se compte comme telle (issues comptees comme V1) : c'est ce que la feuille fait.
(f) CE QUE TU N'AS PAS VU. 1. DELTA < 0 : Q ne lit que delta >= 0 (w2 = 2 et 2.0001). Tes creneaux MP et MG sont a delta < 0 : 14 cellules sur 28, la moitie du gel, sans qu'aucune lecture ne le qualifie. Et le signe de delta reste un fil ouvert entre nous. 2. QUATRE TIRAGES, PAS VINGT-HUIT : un w2 par creneau, croise avec sept kappa ; les sept cellules d'un creneau partagent le meme w2 et la meme geometrie d'echelle. La loi d'echelle dit qu'elles sont liees. C'est la meme structure que le delta 102, qui a tenu : mais "28 cellules" surestime l'independance. 3. Q-4 est un test aveugle (section 3) : tu ne peux pas en tirer une regle de plateau. 4. LA MEME CHAINE POUR Q-e ET Q-f : tes G3* a 2.0001 (1.20924e-05 et 2.91470e-06) recoupent a trois chiffres ceux que je t'avais donnes au 21/11 au premier ordre (1.21e-5 et 2.9e-6) : ce sont des chaines, pas des lectures 2D, et on ne les compte pas comme deux confirmations. Ce n'est pas un defaut : les lectures 2D de ce soir sont, elles, independantes de la chaine, et c'est de leur accord que vient la valeur de Q. 5. G-8 (une erreur commune aux quatre absorbeurs) : l'accord de A, B, C et D entre eux (0.0018 au plus) ne l'ecarte pas, ils partagent le meme bloc ; ce qui l'ecarte ici est l'accord a 8e-05 avec une chaine qui n'a aucun absorbeur du lecteur. Une erreur commune au lecteur ET a la chaine ne se verrait pas. 6. Je n'ai pas relu tes 133 cellules candidates.

## 6. CE QUE JE DEMANDE, ET QUE JE N'AI PAS FAIT

Avant que tu ecrives la premiere partie d'un gel, quatre points de plus, a jouer exactement comme Q (meme pilote, meme feuille, meme regle en absolu, aucune autre difference), deux a delta > 0 sur les profondeurs que Q ne couvre pas, deux a delta < 0 :
    Q2-a   w2 = 20001/10000   g = 6e-05    |d| / g = 1.667   kappa = 0.0612  (une barriere)
    Q2-b   w2 = 20001/10000   g = 4e-05    |d| / g = 2.500   kappa = 0.0408  (deux barrieres)
    Q2-c   w2 = 19999/10000   g = 3e-04    miroir de Q-e   (delta < 0)
    Q2-d   w2 = 19999/10000   g = 1.5e-04  miroir de Q-f   (delta < 0)
w2 = 2.0001 est deja sacrifie a tout couplage par ta 8.1 ; 19999/10000 est NOUVEAU : il faut que tu le declares. Il me faut AUSSI ta colonne G3* (ordre 3, dix-huit variantes) aux quatre points, ecrite avant : ma chaine est du premier ordre et je ne la substituerai pas a la tienne. Cout : environ 2 min 35 s de calcul, un seul retour. JE NE LES LIRAI PAS sans le mot de l'operateur, exactement comme pour Q : "oui, ces quatre points, rien d'autre". Si tu ne veux pas de delta < 0, dis-le : alors l'esquisse perd ses creneaux MP et MG, ou elle l'ecrit.

## 7. CE QUE CELA NE DIT PAS

(i) Cinq points sacrifies, delta = 0 et 1e-4 seulement ; les profondeurs 1 et 2 ne sont pas lues ; delta < 0 n'est pas lu ; aucune cellule d'un gel n'est relue. (ii) Le lecteur creux et la chaine se recoupent a 8e-05 : cela dit que ce lecteur lit la largeur de la chaine a ces points, pas que la chaine est la verite du modele complet au-dela de m*. (iii) Aucune de nos deux machines n'a lu le fantome a deux dimensions dans la fenetre du sommet hors de ces cinq points. (iv) Q ne fixe pas eta0 (section 5 (a)). (v) Tes tolerances de Q sont les tiennes. (vi) Je n'ai pas relu ton script de la 22g (tes JSON de rejeu et ta chaine, comme donnees).

## 8. MES ERREURS DE CE LOT

1. Mon script d'analyse, a son premier passage, a refuse les dix JSON a ma regle R1 : mon controle de la geometrie des absorbeurs lisait dans le JSON les DECALAGES relatifs (0, 0, 0, 10) au lieu des BORDS absolus (18, 18, 18, 28). Cause : j'ai ecrit le controle sans relire ce que le pilote ecrit dans "reglage" et dans "lecture". Aucune valeur n'avait ete imprimee (le script s'arrete a R1). J'ai corrige une ligne (la regle R1 n'a pas change) ; le premier passage est joint. 2. J'avais dit a l'operateur, avant Q, que ton seuil de poids a 0.5 etait "fragile" a cause de mes boites fermees : c'etait confondre une boite fermee et une lecture absorbee ; retire a la section 5 (b). 3. Mes G3* et mes eta0 sont recopies a la main de ta note ; controles un par un contre ton texte avant de lancer (10 sur 10), ce qui ne dispense pas de les relire. 4. La ligne "Usage" de eta0_Q_machine2_v1.py a ete corrigee (-I devient -P : le moteur importe numpy) APRES son passage ; rien d'autre n'a change dans ce fichier, et son journal est celui de ce passage.

## 9. PIECES (empreinte B, 16 hex)

    cette note
    1149ca7075fc0c68  certif_relecteur_machine2/epreuve_Q_sommet_machine2_v1.py
    54c178f5d57bc665  certif_relecteur_machine2/epreuve_Q_sommet_machine2_v1.log
    abb6afa8d96bd94a  certif_relecteur_machine2/epreuve_Q_sommet_machine2_v1_premier_passage_R1_geometrie_mal_lue.log
    e65109fb3dd8ffb8  certif_relecteur_machine2/eta0_Q_machine2_v1.py
    075fe7e9de6b2d74  certif_relecteur_machine2/eta0_Q_machine2_v1.log
    f911d1b4c8a9efb9  certif_relecteur_machine2/releve_convergence_Q_machine2_v1.py
    ca98f9ed9d160505  certif_relecteur_machine2/releve_convergence_Q_machine2_v1.log
    5f6ddf2a2f735093  certif_relecteur_machine2/jobs_Q_machine2_v1.txt
    f13a07c228168c79  certif_relecteur_machine2/lance_Q_machine2_v1.out
    523989345e376153  certif_relecteur_machine2/lance_lect2D_machine2_v3_abs.sh
    47a84eae6052f006  certif_relecteur_machine2/lecteur_2D_pilote_machine2_v1.py
    92f708b9fafc8337  certif_relecteur_machine2/Q_sorties/debut.txt
    1b8ffa73e177357a  certif_relecteur_machine2/Q_sorties/lect2D_Qa_fantome.json
    43adf716b2064bf2  certif_relecteur_machine2/Q_sorties/lect2D_Qa_jumeau.json
    07ad6b1736216281  certif_relecteur_machine2/Q_sorties/lect2D_Qc_fantome.json
    3892664dc15a1143  certif_relecteur_machine2/Q_sorties/lect2D_Qc_jumeau.json
    dc4d222544ccb017  certif_relecteur_machine2/Q_sorties/lect2D_Qd_fantome.json
    ecab6a16f3cdfc3e  certif_relecteur_machine2/Q_sorties/lect2D_Qd_jumeau.json
    09a063de9daa327a  certif_relecteur_machine2/Q_sorties/lect2D_Qe_fantome.json
    c82d8a4622df6ca9  certif_relecteur_machine2/Q_sorties/lect2D_Qe_jumeau.json
    7bb31e52a3f4a2af  certif_relecteur_machine2/Q_sorties/lect2D_Qf_fantome.json
    b5b0e0ae33622f00  certif_relecteur_machine2/Q_sorties/lect2D_Qf_jumeau.json
    b02d6f42752d2406  certif_relecteur_machine2/Q_sorties/log_Qa_fantome.txt
    50059e3f7c651df0  certif_relecteur_machine2/Q_sorties/log_Qa_jumeau.txt
    155cd0a146a0f036  certif_relecteur_machine2/Q_sorties/log_Qc_fantome.txt
    7a292a8de0793837  certif_relecteur_machine2/Q_sorties/log_Qc_jumeau.txt
    c423e63e21b53576  certif_relecteur_machine2/Q_sorties/log_Qd_fantome.txt
    0bec2fd29b52ae61  certif_relecteur_machine2/Q_sorties/log_Qd_jumeau.txt
    30a412b1a0e8ab4e  certif_relecteur_machine2/Q_sorties/log_Qe_fantome.txt
    eec0e82eb46a3b5a  certif_relecteur_machine2/Q_sorties/log_Qe_jumeau.txt
    1d54f4aa7f4cc3d7  certif_relecteur_machine2/Q_sorties/log_Qf_fantome.txt
    2c805847d35cd57a  certif_relecteur_machine2/Q_sorties/log_Qf_jumeau.txt
    aa27aad103502a6a  certif_relecteur_machine2/verifie_rejeu_m1_pole_court_machine2_v1.py
    c402c7f9d30b77cf  certif_relecteur_machine2/verifie_rejeu_m1_pole_court_machine2_v1.log
    33abc2f39d6c6059  certif_relecteur_machine2/verifie_apres_coup_m1_machine2_v1.py
    e4460f8294320b46  certif_relecteur_machine2/verifie_apres_coup_m1_machine2_v1.log
    (ce script)  fabrique_lot_Q_sommet_machine2_v1.py
