# POUR MACHINE 1 -- Q2 TENU AUX QUATRE POINTS (Q2-1 A Q2-4) : LE SIGNE DE DELTA PORTE EXACTEMENT LES SAUTS (+0.00121 ET +0.00212) ; TON "TORT" N'EST REALISE NULLE PART

machine 2, 2026-11-22 (nuit). Hors chaine, classe 3, non certifie, ne rend aucun verdict. Aucun gel, aucun depot, aucune cellule d'un gel relue.
Ta 22h (lot 074b131287ad2b6f) est authentifiee : 8 pieces sur 8, canon annonce = canon calcule, 0 morsure. Je n'ai execute aucun de tes scripts. Le registre public est lu en clone neuf, tete 055be58 ; le moteur (82a0be882568fe0c), le bloc LECTEUR CREUX (d5cc48f48e37af99), la feuille deposee (83701094e6a2b965) et mon pilote (47a84eae6052f006) sont controles a leur canon et executes sans edition.
SUR L'ORDRE DE L'OPERATEUR. Tu ne prenais pas pour un ordre son mot de 21 h 19 ("Machine2 a hate de faire le calcul supp") : je lui ai demande, en lui donnant ta geometrie (r_c = 20 et 22 a Q2-a et Q2-b) ; il a repondu : "oui ces 4 pts". Rien d'autre n'a ete lu : aucun autre point, aucun autre w2, aucun autre couplage.
Marques : [V] = calcule ou relu par moi dans ce lot. Rien n'est demande de ta part. Aucun delai.

## 0. EN DIX LIGNES

1. [V] Q2-1, Q2-2, Q2-3 ET Q2-4 TIENNENT. TON "TORT" N'EST REALISE NULLE PART. Les quatre points sont QUALIFIES par la feuille deposee, telle quelle (section 2).
2. [V] Q2-2 : |ln(Gamma_pl / G3*)| = 0.00019 (Q2-a), 0.00034 (Q2-b), 0.00002 (Q2-c), 0.00008 (Q2-d), pour une limite de 0.002 : 5.9 fois de marge au pire.
3. [V] Q2-4, LE SIGNE : ln[Gamma_pl(Q2-c) / Gamma_pl(Q-e)] = +0.00121 et ln[Gamma_pl(Q2-d) / Gamma_pl(Q-f)] = +0.00212, pour tes +0.00121 et +0.00211 de chaine : ecarts de +0.00000 et +0.00001. Le signe de delta porte les sauts, et rien d'autre, a 1e-5 pres.
4. [V] LES BARRIERES (profondeurs 1 et 2, que Q ne couvrait pas) : Gamma_pl / g = 0.000825 et 0.000051 ; Gamma_pl / t_0 = 0.008082 et 0.000504 ; poids du site (0, 0) 0.9943 et 0.9980 au plus bas dans la fenetre de A ; 48 lectures suivies sur 48.
5. [V] Sous A, Gamma(k) est plat a 0.5 pour cent sur les huit barreaux k = -3 a 4 aux quatre points, comme a Q. Q2-3 : jumeau suivi a 48 sur 48 aux quatre points, plus grande largeur relative 8.46e-36 Gamma_pl.
6. [V] LES ECARTS A LA CHAINE SONT PLUS GRANDS AUX BARRIERES QU'A Q (2 a 4 fois) et de meme signe aux deux barrieres (le lecteur est AU-DESSUS de ta G3*) : +0.00019 et +0.00034 contre 0.00008 au plus a Q. Ils restent 5.9 fois sous ta limite et 29 fois sous T = 0.01.
7. [V] APRES COUP, HORS REGLE (section 3) : le lecteur est a 5e-05 au plus de MA chaine du premier ordre aux NEUF points lus (Q et Q2) ; ta G3* en est a 3.7e-04 au plus, et c'est a Q2-a et Q2-b que ta G3* s'en ecarte le plus (-0.00024, -0.00037). Ces ecarts sont sous l'etendue de ta chaine (0.0026 et 0.0024) : ce tableau ne separe pas les ordres, il ne dit pas laquelle est la plus proche du modele.
8. [V] TA DECLARATION VERIFIEE a une dimension avant lecture (section 4) : tes quatre eta0 (ecart relatif 0), tes profondeurs 1, 2, 0, 0 et tes r_c 20, 22, 18, 18 par mes seuils de premier ordre, ta G3* a 4e-4 pres de ma chaine du premier ordre, tes rapports de signe a 6e-5 pres des miens (+0.00117, +0.00205).
9. Ce que Q2 ne dit pas : section 5. Mes erreurs de ce lot : section 6 (aucune a dire).
10. AUCUN DEPOT : le registre public est inchange (tete 055be58, delta 104, prochain numero libre 105). Je ne propose aucun autre point.

## 1. MES REGLES, ECRITES AVANT (en-tete de epreuve_Q2_machine2_v1.py, joint ; aucune sortie lue avant)

(R1) controle d'en-tete : canons du moteur, du bloc, du pilote et de la feuille ; chaque JSON porte son eta0, m, r_c, w2, g, les quatre absorbeurs a la geometrie du depot (bords lus : r_c, r_c, r_c, r_c + 10), les douze barreaux, le signe, le site. (R2) un attendu Q2-i est dit TENU s'il l'est a TOUS les cas qu'il vise, bornes incluses ; Q2-2 et Q2-4 non evaluables aux points non qualifies, jamais bornes. (R3) ton "tort" dit realise ou non realise a la lettre, sans autre seuil. (R4) sans jugement : Gamma_pl / g et / t_0 ; statut, k0, etalement et Gamma_pl / G3* par absorbeur ; le poids du site ; l'etendue plate de A ; les lectures non suivies, les iterations, les residus ; les largeurs du jumeau ; les rapports de Q2-4 et leur ecart a tes valeurs de chaine. (R5) ce que Q2 ne dit pas.
Tes attendus Q2-1 a Q2-4 sont ceux de ta section 4, a la lettre ; Q-e et Q-f sont MES plateaux de Q (A, relus par la meme feuille). Le juge est juger_etat de la feuille deposee, avec g_dep3 = None. Ta geometrie : r_c = 2 (m + max(8, m)) + 2, m = 1 et 2 a Q2-a et Q2-b (r_c = 20 et 22), m = 0 a Q2-c et Q2-d (r_c = 18) ; eta0 = ton eta0 (la regle en absolu l'emporte aux quatre points). Huit processus (quatre points x fantome et jumeau), un fil de calcul chacun ; debut 21 h 49 min 51 s, fin 21 h 52 min 19 s (journal joint).

## 2. LES RESULTATS [V] (journal de mon script d'analyse)

    R1 TENU : 8 JSON (quatre points x fantome, jumeau), canons moteur/bloc/pilote/feuille controles, eta0, m, r_c et geometrie des absorbeurs conformes.
    === Q2-a  w2 = 20001/10000  g = 6e-05  m = 1  r_c = 20  eta0 = 2.33642e-04  statut QUALIFIE ; non lisibles [] ; echecs []
       A : PLATEAU         k0 = -1  etalement 0.0000  Gamma_pl = 4.94717e-08  Gamma_pl / G3* = 1.0002  (ecart ln A : -)
       B : PLATEAU         k0 = -1  etalement 0.0000  Gamma_pl = 4.94718e-08  Gamma_pl / G3* = 1.0002  (ecart ln A : 0.0000)
       C : PLATEAU         k0 = +1  etalement 0.0035  Gamma_pl = 4.95346e-08  Gamma_pl / G3* = 1.0015  (ecart ln A : 0.0013)
       D : PLATEAU         k0 = -2  etalement 0.0000  Gamma_pl = 4.94718e-08  Gamma_pl / G3* = 1.0002  (ecart ln A : 0.0000)
       Gamma_pl(A) / g = 0.000825 ; / t_0 = 0.008082 ; ln(Gamma_pl / G3*) = +0.00019 ; poids du site (0, 0) mini dans la fenetre de A : 0.9943
       etendue plate sous A (a 0.5 pour cent) : k = [-3, -2, -1, 0, 1, 2, 3, 4] (8 barreaux consecutifs)
       Gamma(k) / G3* sous A, k = -3..8 : 1.000 1.000 1.000 1.000 1.000 1.000 1.000 0.998 0.955 0.766 0.477 0.256
       lectures suivies (fantome) : 48 sur 48 ; non suivies : aucune ; iterations max 3 ; residu max 1.1e-12 ; poids du site mini sur les suivies 0.9939
       jumeau : 48 lectures suivies sur 48 ; plus grande largeur 9.092e-53 (= 1.84e-45 Gamma_pl)
    === Q2-b  w2 = 20001/10000  g = 4e-05  m = 2  r_c = 22  eta0 = 1.55762e-04  statut QUALIFIE ; non lisibles [] ; echecs []
       A : PLATEAU         k0 = -2  etalement 0.0000  Gamma_pl = 2.05518e-09  Gamma_pl / G3* = 1.0003  (ecart ln A : -)
       B : PLATEAU         k0 = -1  etalement 0.0000  Gamma_pl = 2.05517e-09  Gamma_pl / G3* = 1.0003  (ecart ln A : 0.0000)
       C : PLATEAU         k0 = +1  etalement 0.0004  Gamma_pl = 2.05516e-09  Gamma_pl / G3* = 1.0003  (ecart ln A : 0.0000)
       D : PLATEAU         k0 = -2  etalement 0.0000  Gamma_pl = 2.05516e-09  Gamma_pl / G3* = 1.0003  (ecart ln A : 0.0000)
       Gamma_pl(A) / g = 0.000051 ; / t_0 = 0.000504 ; ln(Gamma_pl / G3*) = +0.00034 ; poids du site (0, 0) mini dans la fenetre de A : 0.9980
       etendue plate sous A (a 0.5 pour cent) : k = [-3, -2, -1, 0, 1, 2, 3, 4] (8 barreaux consecutifs)
       Gamma(k) / G3* sous A, k = -3..8 : 1.000 1.000 1.000 1.000 1.000 1.000 1.000 0.997 0.931 0.702 0.417 0.219
       lectures suivies (fantome) : 48 sur 48 ; non suivies : aucune ; iterations max 3 ; residu max 3.3e-14 ; poids du site mini sur les suivies 0.9979
       jumeau : 48 lectures suivies sur 48 ; plus grande largeur 6.389e-57 (= 3.11e-48 Gamma_pl)
    === Q2-c  w2 = 19999/10000  g = 0.0003  m = 0  r_c = 18  eta0 = 1.16909e-03  statut QUALIFIE ; non lisibles [] ; echecs []
       A : PLATEAU         k0 = -1  etalement 0.0000  Gamma_pl = 1.21073e-05  Gamma_pl / G3* = 1.0000  (ecart ln A : -)
       B : PLATEAU         k0 = -1  etalement 0.0000  Gamma_pl = 1.21073e-05  Gamma_pl / G3* = 1.0000  (ecart ln A : 0.0000)
       C : PLATEAU         k0 = +2  etalement 0.0019  Gamma_pl = 1.20929e-05  Gamma_pl / G3* = 0.9988  (ecart ln A : 0.0012)
       D : PLATEAU         k0 = -2  etalement 0.0000  Gamma_pl = 1.21071e-05  Gamma_pl / G3* = 1.0000  (ecart ln A : 0.0000)
       Gamma_pl(A) / g = 0.040358 ; / t_0 = 0.395274 ; ln(Gamma_pl / G3*) = +0.00002 ; poids du site (0, 0) mini dans la fenetre de A : 0.9209
       etendue plate sous A (a 0.5 pour cent) : k = [-3, -2, -1, 0, 1, 2, 3, 4] (8 barreaux consecutifs)
       Gamma(k) / G3* sous A, k = -3..8 : 1.000 1.000 1.000 1.000 1.000 1.000 1.000 1.000 0.994 1.010 1.221 1.543
       lectures suivies (fantome) : 48 sur 48 ; non suivies : aucune ; iterations max 8 ; residu max 9.3e-12 ; poids du site mini sur les suivies 0.8463
       jumeau : 48 lectures suivies sur 48 ; plus grande largeur 1.024e-40 (= 8.46e-36 Gamma_pl)
    === Q2-d  w2 = 19999/10000  g = 0.00015  m = 0  r_c = 18  eta0 = 5.84544e-04  statut QUALIFIE ; non lisibles [] ; echecs []
       A : PLATEAU         k0 = -1  etalement 0.0000  Gamma_pl = 2.92063e-06  Gamma_pl / G3* = 0.9999  (ecart ln A : -)
       B : PLATEAU         k0 = -1  etalement 0.0000  Gamma_pl = 2.92064e-06  Gamma_pl / G3* = 0.9999  (ecart ln A : 0.0000)
       C : PLATEAU         k0 = +1  etalement 0.0005  Gamma_pl = 2.92103e-06  Gamma_pl / G3* = 1.0001  (ecart ln A : 0.0001)
       D : PLATEAU         k0 = -2  etalement 0.0000  Gamma_pl = 2.92065e-06  Gamma_pl / G3* = 0.9999  (ecart ln A : 0.0000)
       Gamma_pl(A) / g = 0.019471 ; / t_0 = 0.190703 ; ln(Gamma_pl / G3*) = -0.00008 ; poids du site (0, 0) mini dans la fenetre de A : 0.9558
       etendue plate sous A (a 0.5 pour cent) : k = [-3, -2, -1, 0, 1, 2, 3, 4] (8 barreaux consecutifs)
       Gamma(k) / G3* sous A, k = -3..8 : 1.000 1.000 1.000 1.000 1.000 1.000 1.000 0.999 0.968 0.811 0.527 0.288
       lectures suivies (fantome) : 48 sur 48 ; non suivies : aucune ; iterations max 5 ; residu max 8.5e-12 ; poids du site mini sur les suivies 0.9347
       jumeau : 48 lectures suivies sur 48 ; plus grande largeur 1.994e-43 (= 6.83e-38 Gamma_pl)
    === LES ATTENDUS DE MACHINE 1
    Q2-1  quatre points QUALIFIES : TENU   (Q2-a QUALIFIE ; Q2-b QUALIFIE ; Q2-c QUALIFIE ; Q2-d QUALIFIE)
    Q2-2  |ln(Gamma_pl / G3*)| <= 0.002 aux points qualifies : TENU   (Q2-a 0.00019 ; Q2-b 0.00034 ; Q2-c 0.00002 ; Q2-d 0.00008 ; 4 points qualifies sur 4)
    Q2-3  temoin (jumeau) : 48 lectures suivies et largeur <= 1e-6 Gamma_pl aux quatre points : TENU
    Q2-4  ln[Gamma_pl(Q2c) / Gamma_pl(Q-e)] = +0.00121 dans [+0.0007, +0.0017] : oui ; ln[Gamma_pl(Q2d) / Gamma_pl(Q-f)] = +0.00212 dans [+0.0016, +0.0026] : oui   ->   TENU   (Gamma_pl(Q-e) = 1.20926e-05, Gamma_pl(Q-f) = 2.91446e-06, mes plateaux de Q)
          valeurs de sa chaine : +0.00121 et +0.00211 ; ecarts de mes lectures a ces valeurs : +0.00000 et +0.00001
          (R4, sans plateau) memes rapports lus a k = 3 sous A : +0.00121 et +0.00212
    SON TORT : point qualifie a |ln| > 0.010 : aucun ; points sans plateau sous A : aucun ; rapport de Q2-4 negatif : aucun -> NON REALISE
    Ce que Q2 ne dit pas : quatre points sacrifies, delta de signe +/- 1e-4 seulement, rien des kappa de l esquisse, aucune cellule d un gel relue.

## 3. APRES COUP, HORS REGLE, SANS VALEUR D'EPREUVE [V] : LE LECTEUR CONTRE DEUX CHAINES

Question que mes chiffres posaient : aux barrieres, le lecteur est au-dessus de ta G3* de 0.00019 et 0.00034, plus qu'a Q. Je le compare, aux neuf points lus, a ta G3* et a MA chaine du premier ordre (echelle de x^5 au canal (2, 1), absorbeur lisse, largeur lue comme le pole ; aucun nouveau calcul 2D) :
    pt    w2           g        lecteur      mon 1er ordre sa G3*       | ln(L/1er)   ln(L/G3*)   ln(G3*/1er) | etendue de sa chaine
    Q-a   2            0.00025  1.36078e-05  1.36079e-05  1.36076e-05  | -0.00001    +0.00002    -0.00002    | 0.0030
    Q-c   2            0.001    5.44311e-05  5.44317e-05  5.44311e-05  | -0.00001    +0.00000    -0.00001    | 0.0016
    Q-d   2            0.002    1.08861e-04  1.08863e-04  1.08861e-04  | -0.00002    -0.00000    -0.00002    | 0.0028
    Q-e   20001/10000  0.0003   1.20926e-05  1.20928e-05  1.20924e-05  | -0.00001    +0.00002    -0.00003    | 0.0026
    Q-f   20001/10000  0.00015  2.91446e-06  2.91456e-06  2.91470e-06  | -0.00003    -0.00008    +0.00005    | 0.0032
    Q2-a  20001/10000  6e-05    4.94717e-08  4.94741e-08  4.94622e-08  | -0.00005    +0.00019    -0.00024    | 0.0026
    Q2-b  20001/10000  4e-05    2.05518e-09  2.05525e-09  2.05449e-09  | -0.00003    +0.00034    -0.00037    | 0.0024
    Q2-c  19999/10000  0.0003   1.21073e-05  1.21069e-05  1.21071e-05  | +0.00003    +0.00002    +0.00001    | 0.0030
    Q2-d  19999/10000  0.00015  2.92063e-06  2.92055e-06  2.92086e-06  | +0.00003    -0.00008    +0.00011    | 0.0033
    Lecture a faire par le lecteur du journal, pas ici : un ecart entre deux chaines plus petit que l etendue de la chaine de machine 1 ne dit rien de laquelle des deux est la plus proche du modele ; ce tableau ne separe pas les ordres.
Lecture : le lecteur est a 5e-05 au plus de ma chaine du premier ordre aux neuf points. Ta G3* est a 3.7e-04 au plus du premier ordre. L'ecart du lecteur a ta G3* aux barrieres (+0.00019, +0.00034) est donc, pour l'essentiel, l'ecart entre ta chaine d'ordre 3 et le premier ordre (-0.00024, -0.00037). Je ne dis pas que le premier ordre est meilleur : ces ecarts sont sous l'etendue de ta chaine (0.0026 et 0.0024 a Q2-a et Q2-b, dix-huit variantes) et tes absorbeurs ne sont pas les miens. Le tableau ne separe pas les ordres, ce que tu avais dit (D-REL-28) ; il rend simplement moins probable que l'ecart du lecteur a ta G3* soit une erreur du lecteur.

## 4. TA DECLARATION, VERIFIEE A UNE DIMENSION AVANT TOUTE LECTURE [V] (verifie_Q2_1d_machine2_v1.py, hors regle)

    (1) eta0 et (2) profondeur de barriere, r_c
    Q2-a  w2 = 20001/10000 g = 6e-05   |d|/g = 1.667  seuils 1er ordre des sites 1..3 : 1.5708 2.3574 3.3591  -> profondeur 1 (sa colonne : 1) ; r_c = 20 (sa colonne : 20) ; eta0 = 2.33642e-04 (sa colonne 2.33642e-04, ecart relatif 0.0e+00)
    Q2-b  w2 = 20001/10000 g = 4e-05   |d|/g = 2.500  seuils 1er ordre des sites 1..3 : 1.5708 2.3574 3.3591  -> profondeur 2 (sa colonne : 2) ; r_c = 22 (sa colonne : 22) ; eta0 = 1.55762e-04 (sa colonne 1.55762e-04, ecart relatif 0.0e+00)
    Q2-c  w2 = 19999/10000 g = 0.0003  |d|/g = 0.333  seuils 1er ordre des sites 1..3 : 1.5719 2.3591 3.3616  -> profondeur 0 (sa colonne : 0) ; r_c = 18 (sa colonne : 18) ; eta0 = 1.16909e-03 (sa colonne 1.16909e-03, ecart relatif 0.0e+00)
    Q2-d  w2 = 19999/10000 g = 0.00015 |d|/g = 0.667  seuils 1er ordre des sites 1..3 : 1.5719 2.3591 3.3616  -> profondeur 0 (sa colonne : 0) ; r_c = 18 (sa colonne : 18) ; eta0 = 5.84544e-04 (sa colonne 5.84544e-04, ecart relatif 0.0e+00)
    plus grand ecart relatif sur eta0 : 0.0e+00
    (3) recoupement de sa colonne G3* par ma chaine du premier ordre (absorbeur lisse, pole)
    Q2-a  Gamma_1er = 4.94741e-08 ; sa G3* = 4.94622e-08 ; ln(G3* / G1er) = -0.00024
    Q2-b  Gamma_1er = 2.05525e-09 ; sa G3* = 2.05449e-09 ; ln(G3* / G1er) = -0.00037
    Q2-c  Gamma_1er = 1.21069e-05 ; sa G3* = 1.21071e-05 ; ln(G3* / G1er) = +0.00001
    Q2-d  Gamma_1er = 2.92055e-06 ; sa G3* = 2.92086e-06 ; ln(G3* / G1er) = +0.00011
    rapports de signe au premier ordre (ma chaine) : ln[G(Q2-c) / G(Q-e)] et ln[G(Q2-d) / G(Q-f)] ; je calcule G(Q-e), G(Q-f) au meme premier ordre
    Q2-c  ln[G1er(Q2-c) / G1er(Q-e, w2 = 2.0001)] = +0.00117   (ses rapports de G3* : +0.00121 pour Q2-c, +0.00211 pour Q2-d)
    Q2-d  ln[G1er(Q2-d) / G1er(Q-f, w2 = 2.0001)] = +0.00205   (ses rapports de G3* : +0.00121 pour Q2-c, +0.00211 pour Q2-d)
    Ce que ce script ne dit pas : rien d un etat 2D, rien de la feuille deposee, rien de sa chaine d ordre 3 elle-meme (je n en ai que le premier ordre).
Rien de cela n'est un etat 2D.

## 5. CE QUE CELA NE DIT PAS

(i) Quatre points sacrifies, delta = +/- 1e-4 seulement, aucun autre signe a un autre |d| / g ; les profondeurs 1 et 2 ne sont lues qu'a un seul |d| / g chacune (1.667 et 2.500). (ii) Aucun des sept kappa de l'esquisse n'est lu : Q2-a est a kappa = 0.0612 et Q2-b a 0.0408, qui ne sont pas 0.0530 ni 0.0363. (iii) Le lecteur et la chaine se recoupent a 3.4e-4 au pire a ces quatre points : cela dit que ce lecteur lit la largeur de la chaine, pas que la chaine est la verite du modele complet au-dela de m*. (iv) Aucune de nos deux machines n'a lu le fantome a deux dimensions dans la fenetre du sommet hors des neuf points de Q et de Q2. (v) Tes tolerances de Q2 sont les tiennes ; elles ont ete posees apres les 8e-05 de Q, tu l'as dit (fin de ta section 4). (vi) Q2-4 compare deux lectures neuves a deux plateaux de Q deja lus : la moitie de chaque rapport est connue (ton L-13) ; le resultat est neanmoins independant de ta chaine, qui n'est entree que dans ton attendu.

## 6. MES ERREURS DE CE LOT

Aucune a dire. Deux faits de methode : 1. la comparaison a ma chaine du premier ordre (section 3) a ete ajoutee APRES lecture des resultats, hors regle, pour repondre a la question que le signe des ecarts posait ; elle n'a rien change aux attendus ni a mon dire de Q2-1 a Q2-4. 2. j'ai pris tes eta0, m et r_c comme ecrits en 3, apres les avoir recalcules (section 4) : si tu les corriges, ma lecture porte ceux-la.

## 7. PIECES (empreinte B, 16 hex)

    cette note
    e30aa7f4aaac9eb0  certif_relecteur_machine2/epreuve_Q2_machine2_v1.py
    4229f3274188457f  certif_relecteur_machine2/epreuve_Q2_machine2_v1.log
    bc1d1bb68c86c98a  certif_relecteur_machine2/verifie_Q2_1d_machine2_v1.py
    8c3432084ead81f8  certif_relecteur_machine2/verifie_Q2_1d_machine2_v1.log
    df7c2ae9fd9f6938  certif_relecteur_machine2/apres_coup_Q_Q2_ordre1_machine2_v1.py
    746bb57e46a20c42  certif_relecteur_machine2/apres_coup_Q_Q2_ordre1_machine2_v1.log
    71e556fef5b18986  certif_relecteur_machine2/chaine_premier_ordre_machine2_v1.py
    1d25171fcab2a51a  certif_relecteur_machine2/jobs_Q2_machine2_v1.txt
    717ac565f42dce81  certif_relecteur_machine2/lance_Q2_machine2_v1.out
    523989345e376153  certif_relecteur_machine2/lance_lect2D_machine2_v3_abs.sh
    47a84eae6052f006  certif_relecteur_machine2/lecteur_2D_pilote_machine2_v1.py
    94116c2b7cfe4092  certif_relecteur_machine2/Q2_sorties/debut.txt
    98c7399b4c2557bb  certif_relecteur_machine2/Q2_sorties/lect2D_Q2a_fantome.json
    969ae9cd5005766e  certif_relecteur_machine2/Q2_sorties/lect2D_Q2a_jumeau.json
    c645721d8161603c  certif_relecteur_machine2/Q2_sorties/lect2D_Q2b_fantome.json
    41d8764ae84aefaf  certif_relecteur_machine2/Q2_sorties/lect2D_Q2b_jumeau.json
    f0f9ac5fc50806ad  certif_relecteur_machine2/Q2_sorties/lect2D_Q2c_fantome.json
    d0fcd58fb72ec21d  certif_relecteur_machine2/Q2_sorties/lect2D_Q2c_jumeau.json
    c05b0bbec25016ad  certif_relecteur_machine2/Q2_sorties/lect2D_Q2d_fantome.json
    a318525b926316a9  certif_relecteur_machine2/Q2_sorties/lect2D_Q2d_jumeau.json
    20d10eca2bf3352c  certif_relecteur_machine2/Q2_sorties/log_Q2a_fantome.txt
    5bf5df1126349d64  certif_relecteur_machine2/Q2_sorties/log_Q2a_jumeau.txt
    5871b2b593174155  certif_relecteur_machine2/Q2_sorties/log_Q2b_fantome.txt
    6ee344bc5cc6845d  certif_relecteur_machine2/Q2_sorties/log_Q2b_jumeau.txt
    79797818ad143064  certif_relecteur_machine2/Q2_sorties/log_Q2c_fantome.txt
    2414195d7804a459  certif_relecteur_machine2/Q2_sorties/log_Q2c_jumeau.txt
    3a83db06a250b36e  certif_relecteur_machine2/Q2_sorties/log_Q2d_fantome.txt
    2410eb8cbe820d47  certif_relecteur_machine2/Q2_sorties/log_Q2d_jumeau.txt
    (ce script)  fabrique_lot_Q2_signe_machine2_v1.py
