# POUR MACHINE 1 -- MON TIRAGE DU GEL "SOMMET" SUR LA GRAINE 114565 (DONNEE PAR L'OPERATEUR) : HUIT w2, CINQUANTE-SIX CELLULES, AUX RANGS 0 ET 1 DES QUATRE CRENEAUX ; AUCUN CALCUL 2D

machine 2, 2026-11-22 (nuit). Hors chaine, classe 3, non certifie, ne rend aucun verdict. Aucun calcul 2D, aucun gel, aucun depot.
LA GRAINE : l'operateur l'a ecrite dans le message qui a suivi mon compte rendu de ma certification (mon enveloppe 22j, lot 21e9bddfe5db83b2 ; je ne sais pas si elle t'est deja parvenue) : "graine 114565". Elle est une suite de six chiffres, sans zero de tete. Je la reporte telle quelle. Je ne l'ai ni proposee, ni commentee, ni choisie ; je ne sais pas encore si l'operateur te l'a donnee de son cote : la piece (section 3) dit "aux deux machines, par ecrit". Je n'ai pas lu ton tirage.
LA TABLE : la table COMMUNE de ma certification (table_commune_sommet_machine2_v1.json, jointe), le ET des deux tables : 80 w2 eligibles sur 80, 560 cellules sur 560 ; elle ne depend d'aucune graine et existait avant celle-ci.
MON CODE : tirage_sommet_machine2_v1.py, ecrit des sections 3 et 6 de la piece 1e5039cade55d13f seules ; il refuse toute graine qui n'est pas une suite d'au moins six chiffres. Autotest et comparaison a ton tirage de demonstration : mon lot 21e9bddfe5db83b2.
Marques : [V] = calcule ou relu par moi dans ce lot. Rien d'autre n'est demande. Aucun delai.

## 0. EN HUIT LIGNES

1. [V] LES HUIT w2 : MPa = 199989/100000 (1.99989) ; MPb = 199993/100000 (1.99993) ; PPa = 25001/12500 (2.00008) ; PPb = 200011/100000 (2.00011) ; MGa = 6249/3125 (1.99968) ; MGb = 49989/25000 (1.99956) ; PGa = 200039/100000 (2.00039) ; PGb = 12503/6250 (2.00048).
2. [V] LES RANGS : 0 et 1 dans les quatre creneaux ; aucun w2 tire n'est ineligible, aucun n'est deja retenu ; les branches "rang suivant" et "PAS DE GEL" ne servent pas.
3. [V] LES CINQUANTE-SIX CELLULES, avec leurs trois nombres ecrits (g, eta0, r_c), sont dans le journal de la section 1 (et rappelees en section 2) ; mes 56 cellules sont retrouvees identiques (chaines) dans MA table et dans TA table JSON (77ce2a6c7e867011).
4. [V] UNE SECONDE ECRITURE de la regle des rangs, faite dans un script separe (verifie_tirage_graine_sommet_machine2_v1.py), et les hachages recalcules par hashlib hors de mon script de tirage, rendent les memes huit w2.
5. [V] OBSERVATION SUR LA REGLE DE eta0 (section 4) : eta0 = max(|w2 - 2|, g X / (P kappa_3)) se reduit, en reportant g, a (kappa / kappa_3) |w2 - 2|, independant de X ; le premier terme ne l'emporte a aucune des 560 cellules. Ce n'est pas un defaut ; c'est une simplification, que la seconde partie peut ecrire telle quelle.
6. LE TIRAGE EST UN TIRAGE DE LA TABLE COMMUNE, a la graine de l'operateur : si ton tirage rend les memes huit w2 et les memes cinquante-six cellules a trois nombres ecrits pres, nos tirages coincident ; sinon, section 6 de la piece : PAS DE GEL tant que l'ecart n'est pas explique par ecrit, et la graine n'est pas changee.
7. DEPUIS CE TIRAGE, AUCUNE DES DEUX MACHINES NE LIT UNE CELLULE TIREE AVANT LE RUN (section 0 de la piece, E19). Je ne le fais pas. Je n'ai fait aucun calcul 2D a un w2 candidat, avant ni apres.
8. AUCUN DEPOT : le registre public est inchange (tete 055be58, delta 104, prochain numero libre 105).

## 1. MON JOURNAL DE TIRAGE [V]

    graine : 114565 ; table commune : lue
    les huit lignes de controle de la section 3 (rangs 0 et 1 bruts, avant la regle des rangs) :
        sha256("114565|MP|0") = 075d562d52484be8... ; modulo 15 = 9 -> w2 = 1.99989
        sha256("114565|MP|1") = ca2fef773b2d924b... ; modulo 15 = 12 -> w2 = 1.99993
        sha256("114565|PP|0") = 45ca0c879ef2a590... ; modulo 15 = 3 -> w2 = 2.00008
        sha256("114565|PP|1") = 1a37a5fa7a9a1e40... ; modulo 15 = 5 -> w2 = 2.00011
        sha256("114565|MG|0") = c4599ce5a0078c03... ; modulo 25 = 17 -> w2 = 1.99968
        sha256("114565|MG|1") = dd20c4b207612810... ; modulo 25 = 5 -> w2 = 1.99956
        sha256("114565|PG|0") = 970e004a58200fbc... ; modulo 25 = 14 -> w2 = 2.00039
        sha256("114565|PG|1") = 71a77b17c3bff9f4... ; modulo 25 = 23 -> w2 = 2.00048
    tirage (regle des rangs, section 6) :
      MP rang 0 : indice 9 sur 15 -> w2 = 1.99989 ; eligible dans la table commune : True ; deja retenu : False
      MP rang 1 : indice 12 sur 15 -> w2 = 1.99993 ; eligible dans la table commune : True ; deja retenu : False
      => MPa : w2 = 199989/100000 = 1.99989
           MPa1  kappa 0.0363  g = 3.91071e-05  eta0 = 1.52405e-04  r_c = 22
           MPa2  kappa 0.0530  g = 5.70985e-05  eta0 = 2.22519e-04  r_c = 20
           MPa3  kappa 0.0800  g = 8.61865e-05  eta0 = 3.35878e-04  r_c = 18
           MPa4  kappa 0.1300  g = 1.40053e-04  eta0 = 5.45801e-04  r_c = 18
           MPa5  kappa 0.2000  g = 2.15466e-04  eta0 = 8.39694e-04  r_c = 18
           MPa6  kappa 0.4000  g = 4.30932e-04  eta0 = 1.67939e-03  r_c = 18
           MPa7  kappa 1.0000  g = 1.07733e-03  eta0 = 4.19847e-03  r_c = 18
      => MPb : w2 = 199993/100000 = 1.99993
           MPb1  kappa 0.0363  g = 2.48901e-05  eta0 = 9.69848e-05  r_c = 22
           MPb2  kappa 0.0530  g = 3.63409e-05  eta0 = 1.41603e-04  r_c = 20
           MPb3  kappa 0.0800  g = 5.48542e-05  eta0 = 2.13741e-04  r_c = 18
           MPb4  kappa 0.1300  g = 8.91380e-05  eta0 = 3.47328e-04  r_c = 18
           MPb5  kappa 0.2000  g = 1.37135e-04  eta0 = 5.34350e-04  r_c = 18
           MPb6  kappa 0.4000  g = 2.74271e-04  eta0 = 1.06870e-03  r_c = 18
           MPb7  kappa 1.0000  g = 6.85677e-04  eta0 = 2.67176e-03  r_c = 18
      PP rang 0 : indice 3 sur 15 -> w2 = 2.00008 ; eligible dans la table commune : True ; deja retenu : False
      PP rang 1 : indice 5 sur 15 -> w2 = 2.00011 ; eligible dans la table commune : True ; deja retenu : False
      => PPa : w2 = 25001/12500 = 2.00008
           PPa1  kappa 0.0363  g = 2.84618e-05  eta0 = 1.10840e-04  r_c = 22
           PPa2  kappa 0.0530  g = 4.15558e-05  eta0 = 1.61832e-04  r_c = 20
           PPa3  kappa 0.0800  g = 6.27258e-05  eta0 = 2.44275e-04  r_c = 18
           PPa4  kappa 0.1300  g = 1.01929e-04  eta0 = 3.96945e-04  r_c = 18
           PPa5  kappa 0.2000  g = 1.56814e-04  eta0 = 6.10686e-04  r_c = 18
           PPa6  kappa 0.4000  g = 3.13629e-04  eta0 = 1.22137e-03  r_c = 18
           PPa7  kappa 1.0000  g = 7.84072e-04  eta0 = 3.05344e-03  r_c = 18
      => PPb : w2 = 200011/100000 = 2.00011
           PPb1  kappa 0.0363  g = 3.91394e-05  eta0 = 1.52405e-04  r_c = 22
           PPb2  kappa 0.0530  g = 5.71457e-05  eta0 = 2.22519e-04  r_c = 20
           PPb3  kappa 0.0800  g = 8.62576e-05  eta0 = 3.35878e-04  r_c = 18
           PPb4  kappa 0.1300  g = 1.40169e-04  eta0 = 5.45803e-04  r_c = 18
           PPb5  kappa 0.2000  g = 2.15644e-04  eta0 = 8.39695e-04  r_c = 18
           PPb6  kappa 0.4000  g = 4.31288e-04  eta0 = 1.67939e-03  r_c = 18
           PPb7  kappa 1.0000  g = 1.07822e-03  eta0 = 4.19847e-03  r_c = 18
      MG rang 0 : indice 17 sur 25 -> w2 = 1.99968 ; eligible dans la table commune : True ; deja retenu : False
      MG rang 1 : indice 5 sur 25 -> w2 = 1.99956 ; eligible dans la table commune : True ; deja retenu : False
      => MGa : w2 = 6249/3125 = 1.99968
           MGa1  kappa 0.0363  g = 1.13677e-04  eta0 = 4.43360e-04  r_c = 22
           MGa2  kappa 0.0530  g = 1.65974e-04  eta0 = 6.47328e-04  r_c = 20
           MGa3  kappa 0.0800  g = 2.50527e-04  eta0 = 9.77100e-04  r_c = 18
           MGa4  kappa 0.1300  g = 4.07106e-04  eta0 = 1.58779e-03  r_c = 18
           MGa5  kappa 0.2000  g = 6.26317e-04  eta0 = 2.44275e-03  r_c = 18
           MGa6  kappa 0.4000  g = 1.25263e-03  eta0 = 4.88548e-03  r_c = 18
           MGa7  kappa 1.0000  g = 3.13159e-03  eta0 = 1.22138e-02  r_c = 18
      => MGb : w2 = 49989/25000 = 1.99956
           MGb1  kappa 0.0363  g = 1.56235e-04  eta0 = 6.09618e-04  r_c = 22
           MGb2  kappa 0.0530  g = 2.28112e-04  eta0 = 8.90078e-04  r_c = 20
           MGb3  kappa 0.0800  g = 3.44319e-04  eta0 = 1.34351e-03  r_c = 18
           MGb4  kappa 0.1300  g = 5.59519e-04  eta0 = 2.18321e-03  r_c = 18
           MGb5  kappa 0.2000  g = 8.60799e-04  eta0 = 3.35878e-03  r_c = 18
           MGb6  kappa 0.4000  g = 1.72160e-03  eta0 = 6.71757e-03  r_c = 18
           MGb7  kappa 1.0000  g = 4.30399e-03  eta0 = 1.67939e-02  r_c = 18
      PG rang 0 : indice 14 sur 25 -> w2 = 2.00039 ; eligible dans la table commune : True ; deja retenu : False
      PG rang 1 : indice 23 sur 25 -> w2 = 2.00048 ; eligible dans la table commune : True ; deja retenu : False
      => PGa : w2 = 200039/100000 = 2.00039
           PGa1  kappa 0.0363  g = 1.38913e-04  eta0 = 5.40345e-04  r_c = 22
           PGa2  kappa 0.0530  g = 2.02820e-04  eta0 = 7.88931e-04  r_c = 20
           PGa3  kappa 0.0800  g = 3.06144e-04  eta0 = 1.19084e-03  r_c = 18
           PGa4  kappa 0.1300  g = 4.97483e-04  eta0 = 1.93511e-03  r_c = 18
           PGa5  kappa 0.2000  g = 7.65359e-04  eta0 = 2.97710e-03  r_c = 18
           PGa6  kappa 0.4000  g = 1.53072e-03  eta0 = 5.95421e-03  r_c = 18
           PGa7  kappa 1.0000  g = 3.82680e-03  eta0 = 1.48855e-02  r_c = 18
      => PGb : w2 = 12503/6250 = 2.00048
           PGb1  kappa 0.0363  g = 1.71027e-04  eta0 = 6.65038e-04  r_c = 22
           PGb2  kappa 0.0530  g = 2.49709e-04  eta0 = 9.70992e-04  r_c = 20
           PGb3  kappa 0.0800  g = 3.76919e-04  eta0 = 1.46565e-03  r_c = 18
           PGb4  kappa 0.1300  g = 6.12494e-04  eta0 = 2.38168e-03  r_c = 18
           PGb5  kappa 0.2000  g = 9.42298e-04  eta0 = 3.66412e-03  r_c = 18
           PGb6  kappa 0.4000  g = 1.88460e-03  eta0 = 7.32826e-03  r_c = 18
           PGb7  kappa 1.0000  g = 4.71149e-03  eta0 = 1.83206e-02  r_c = 18
    8 w2, 56 cellules : MPa=199989/100000 MPb=199993/100000 PPa=25001/12500 PPb=200011/100000 MGa=6249/3125 MGb=49989/25000 PGa=200039/100000 PGb=12503/6250

## 2. LES CINQUANTE-SIX CELLULES, DANS LA TABLE COMMUNE [V]

Les lignes "=> MPa : w2 = ..." et les cellules MPa1 a PGb7 du journal de la section 1 sont les cellules de la table commune aux huit w2 tires, avec leur couplage ECRIT (six chiffres), leur eta0 ECRIT et leur rayon r_c. Aucune n'a ete calculee autrement que par la regle de la section 2 de la piece (certification, lot 21e9bddfe5db83b2).

## 3. VERIFICATION DE MON TIRAGE PAR UNE SECONDE ECRITURE, ET DES CELLULES CONTRE LES DEUX TABLES [V]

    MP : rangs lus 2 ; w2 retenus ['199989/100000', '199993/100000'] ; trace (rang, indice, w2, eligible, deja) [(0, 9, '199989/100000', True, False), (1, 12, '199993/100000', True, False)]
    PP : rangs lus 2 ; w2 retenus ['25001/12500', '200011/100000'] ; trace (rang, indice, w2, eligible, deja) [(0, 3, '25001/12500', True, False), (1, 5, '200011/100000', True, False)]
    MG : rangs lus 2 ; w2 retenus ['6249/3125', '49989/25000'] ; trace (rang, indice, w2, eligible, deja) [(0, 17, '6249/3125', True, False), (1, 5, '49989/25000', True, False)]
    PG : rangs lus 2 ; w2 retenus ['200039/100000', '12503/6250'] ; trace (rang, indice, w2, eligible, deja) [(0, 14, '200039/100000', True, False), (1, 23, '12503/6250', True, False)]
    (1) seconde ecriture contre le journal de mon tirage : IDENTIQUES
    (2) cellules du journal : 56 ; retrouvees identiques dans ma table : 56 ; dans la table de machine 1 : 56
    (3) hachages recalcules ici : 114565|MP|0 -> 075d562d52484be8 ; 114565|MP|1 -> ca2fef773b2d924b ; 114565|PP|0 -> 45ca0c879ef2a590 ; 114565|PP|1 -> 1a37a5fa7a9a1e40 ; 114565|MG|0 -> c4599ce5a0078c03 ; 114565|MG|1 -> dd20c4b207612810 ; 114565|PG|0 -> 970e004a58200fbc ; 114565|PG|1 -> 71a77b17c3bff9f4
    TIENT

## 4. OBSERVATION SUR eta0, HORS REGLE, SANS AUCUN ETAT 2D [V]

    cellules : 560 ; plus grand ecart relatif entre eta0 ecrit et (kappa / kappa_3) |w2 - 2| : 6.04e-06 (arrondi du g ecrit a six chiffres) ; cellules ou |w2 - 2| l emporterait : 0
    couples (|w2 - 2| au cent-millieme, kappa) : 280 ; avec UN SEUL eta0 ecrit pour les deux signes de delta : 164 ; avec deux eta0 ecrits (dernier chiffre, arrondi de g) : 116
En clair : avec g = kappa |w2 - 2| P / X, le terme g X / (P kappa_3) vaut (kappa / kappa_3) |w2 - 2|, X disparait ; comme le plus petit kappa de la grille (0.0363) vaut 1.385 kappa_3, le second terme du max l'emporte partout. Deux w2 de meme |w2 - 2| (ici MPa = 1.99989 et PPb = 2.00011) ont le meme eta0 a l'arrondi pres du dernier chiffre pour un meme kappa, alors que leurs couplages different de X. Cela ne change aucun nombre ecrit de la piece ; je le consigne parce que "eta0 depend de g" (section 2 de la piece) est vrai et trompeur : il depend de kappa et de |w2 - 2|.

## 5. CE QUE CECI NE DIT PAS

(i) Aucune cellule n'est lue : ni fantome ni jumeau, ni a un w2 tire ni a un autre candidat. (ii) La seconde partie n'existe pas encore : ce tirage ne fixe ni enonce, ni tolerance, ni instrument ; il est LE tirage de la premiere partie, que ta seconde partie reportera avec la graine telle quelle. (iii) Je n'ai pas de raison de croire que ton tirage differe ; je ne l'ai pas lu, et je ne dis pas qu'il coincide.

## 6. MES ERREURS DE CE LOT

Aucune a dire.

## 7. PIECES (empreinte B, 16 hex)

    cette note
    77ce2a6c7e867011  certif_gel_sommet_partie1_machine2/table_commune_sommet_machine2_v1.json
    c3f3accdf97bf0ec  certif_gel_sommet_partie1_machine2/tirage_sommet_machine2_v1.py
    31f4e690d145a8ee  certif_gel_sommet_partie1_machine2/tirage_graine_114565_sommet_machine2_v1.log
    5e515902266df9dc  certif_gel_sommet_partie1_machine2/verifie_tirage_graine_sommet_machine2_v1.py
    ecce5c305ba61465  certif_gel_sommet_partie1_machine2/verifie_tirage_graine_114565_sommet_machine2_v1.log
    bc9587ebd8e60169  certif_gel_sommet_partie1_machine2/verifie_eta0_forme_sommet_machine2_v1.py
    6948d0cba0847212  certif_gel_sommet_partie1_machine2/verifie_eta0_forme_sommet_machine2_v1.log
    (ce script)  fabrique_lot_tirage_graine_114565_gel_sommet_machine2_v1.py
