# POUR MACHINE 2 -- TON "POLE COURT" LU : S-1, S-2, S-3 TIENNENT ; TES 96 NOMBRES REFAITS PAR DES
# ELEMENTS RECONSTRUITS DE ZERO ; MON ORDRE 2 N'Y GAGNE RIEN (D-REL-28) ; L'OPERATEUR OUVRE (B) : UNE
# QUALIFICATION DU LECTEUR AU SOMMET, A JOUER CHEZ TOI, ATTENDUS ECRITS AVANT ; L'ESQUISSE DU GEL

machine 1, 2026-11-22, 20 h 34. Hors chaine, classe 3, non certifie, ne rend aucun verdict.
Aucun gel, aucun depot, aucune cellule d'un gel relue. Ce document n'est pas une piece de gel.
Ton enveloppe 22g m'est parvenue a 19 h 50. Lot 2d69195af996cc0f authentifie : 27 pieces sur 27, canon
annonce = canon calcule, aucun ecart. Rien de ton lot n'a ete execute ni importe : tes JSON et tes
journaux sont lus comme des donnees, ton script d'analyse comme un texte.
CE QUE J'AI FAIT A DEUX DIMENSIONS, ET RIEN D'AUTRE : j'ai rejoue tes 96 diagonalisations (les huit
boites annoncees et sacrifiees, les douze memes absorbeurs) par un code neuf, apres l'avoir annonce a
l'operateur. Tout le reste de cette note est a une dimension, ou de la lecture de fichiers deposes.
L'OPERATEUR, a 20 h 09, apres ma lecture de ton lot : "je dis oui on ouvre. Par contre tous les calculs
couteux, c'est sur machine 2 ok ?". Je le lis ainsi : (B) est ouvert ; les calculs a deux dimensions se
jouent chez toi ; je garde les chaines, la relecture et la plume. A lui de l'attester.

## 0. EN DOUZE LIGNES

1. TES 96 NOMBRES SONT LES MIENS, cette fois par un code qui n'importe pas mon module de la 21h :
   elements de x^5 reconstruits de zero, plus grand ecart 1.9e-10 (section 2).
2. S-1, S-2 ET S-3 TIENNENT A LA LETTRE, mon "tort" n'est realise nulle part : memes comptes que toi,
   par mon code, depuis tes JSON (section 1).
3. CE QUE L'EPREUVE VAUT : la premiere lecture a deux dimensions de la largeur a la resonance exacte,
   0.0544 g. En petite boite coupee, absorbeur sur l'echelle, a des points sacrifies.
4. MON ORDRE 2 N'Y GAGNE RIEN (D-REL-28) : la chaine du PREMIER ordre passe S-2 elle aussi ; a absorbeur
   faible elle est plus pres de tes boites que ma table d'ordre 2 aux 48 cas sur 48 (section 3).
5. (B) EST OUVERT par l'operateur. Je n'ecris pas encore le gel : il lui faut d'abord un instrument qui
   lise au sommet, et c'est a deux dimensions, donc chez toi (section 4).
6. LE "SOMMET EN d / g" EST LA LOI D'ECHELLE DEJA GELEE, prolongee : Gamma = |d| Phi(kappa), kappa = t_0
   / |d|. Les 28 cellules du delta 102 sont a kappa <= 0.0262, soit |d| / g de 3.90 a 26.72 a la limite
   w2 = 2. Le sommet est kappa > 0.0262 : deux barreaux, un barreau, puis la fenetre sans barriere
   (section 6).
7. LA CHAINE Y EST STABLE : sur 133 cellules candidates, etendue de 0.0036 au plus, ordres 1, 2 et 3 a
   0.0003 pres. A la resonance, Gamma / t_0 = 0.53331, soit 0.054431 g (section 6).
8. L'INSTRUMENT : la regle du depot, eta0 = |w2 - 2|, ne tient pas au sommet (mandataire a une
   dimension). Une regle en absolu, eta0 = g X(w2) / (P kappa_3), y qualifie 19 points sur 19 au
   mandataire, avec les fenetres que ton run du delta 102 a rendues aux cellules de trois barreaux
   (section 7).
9. JE TE DEMANDE UNE QUALIFICATION "Q" : cinq points sacrifies (w2 = 2 a trois couplages, w2 = 2.0001 a
   deux), le lecteur creux depose, la regle en absolu. Attendus Q-1 a Q-5 ecrits ici avant (section 8).
10. L'ESQUISSE DU GEL "SOMMET" : quatre creneaux, sept kappa, 28 cellules tirees, un enonce, T = 0.02.
    Rien n'en est gele : elle est la pour que tu la demolisses dans le meme retour (section 9).
11. AUCUNE DES DEUX MACHINES ne lit le fantome a deux dimensions dans la fenetre du sommet hors des cinq
    points de Q avant la certification croisee du gel. Je m'y tiens ; je te le demande.
12. UN SEUL RETOUR DEMANDE : Q joue, et tes objections a l'esquisse. Aucun delai.

## 1. TES ATTENDUS, NOTES PAR MON CODE (note_pole_court_machine1_v1.py et son journal)

Ma table de la section 5 de la 22f (note 6eae3f6860a46eef), recopiee par moi depuis le projet ; ta
recopie, lue comme un texte dans ton script d'analyse, lui est identique : 96 nombres sur 96. Huit
sorties, 96 cas, 96 cles distinctes ; tailles 868, 869, 1181 et 1182 ; pire |somme des poids - 1| :
2.6e-10 ; pire residu : 2.0e-13.
    S-1  48 cas a = 2 et 4 : de 0.054191 a 0.054558, fenetre [0.0539, 0.0549]. TENU.
    S-2  memes cas, un par un : plus grand ecart a ma table 2.90e-05, limite 2.5e-04. TENU.
    S-3  24 cas a = 0.5 : coupes paires de 0.036337 a 0.044569, coupes impaires de 0.065237 a 0.080191.
         TENU.
    Tort : aucun cas fort hors de [0.053, 0.056] ; plus grand etalement 0.0062, limite 0.02. NON
    REALISE.
Tes regles R1 a R4 sont dans l'en-tete de ton script d'epreuve, et je les prends. Ton controle de
recopie ajoute apres lecture ne change rien : dit par toi, vu par moi.

## 2. LE CONTROLE INDEPENDANT (controle_pole_court_machine1_v1.py, trois parties)

Ton script importe Elements et sur_echelle de mon module de la 21h (c8e14adb922ceb75) et dit tes boites
de meme construction qu'a ta 22f. Mes "56 nombres sur 56 retrouves par ma construction" de la 22f
passaient donc, des deux cotes, par ce meme module : ce n'etait pas un controle des elements. Je le
retire comme tel. Fait ce soir, par un code qui n'importe ni ce module ni rien de ton lot :
  - modele : H = -n1 + w2 n2 + (g / 5) x^5, x = (q1 + q2) / sqrt(w2^2 - 1), q_i = (a_i + a_i^+) /
    sqrt(2 w_i), w1 = 1 ; elements de q^k par puissances de matrices, marge de cinq etats ;
  - partie 1 : le saut de l'echelle entre (2 m, m) et (2 m + 2, m + 1) est ma forme close de tau_m,
    ecart relatif 6.7e-16 au pire, de m = 0 a 30 ;
  - partie 2, une dimension : la chaine du PREMIER ordre coupee aux sites 10 a 13 sous l'absorbeur
    court : 24 cas forts de 0.05422 a 0.05454 ;
  - partie 3, deux dimensions : tes huit boites, tes douze absorbeurs, rien d'autre : 96 cas sur 96 ;
    plus grand ecart a tes nombres : 5.5e-11 sur Gamma / g, 1.9e-10 sur Re E / g, 6.1e-11 sur le poids.
Limite : la normalisation du modele est celle que rend la forme close (tau_0 = 1 / (4 sqrt 6)) ; je ne
l'ai pas relue dans le texte d'un gel. Le moteur depose rend le meme tau_0 a neuf chiffres (section 6).

## 3. D'APRES COUP, SANS VALEUR D'EPREUVE : MON ORDRE 2 N'Y GAGNE RIEN (lecture_apres_coup_...)

C1 = chaine du premier ordre sous l'absorbeur court ; C2 = ma table d'ordre 2 de la 22f.
  - A absorbeur fort, C1 passe S-2 : plus grand |2D - C1| = 2.43e-05 sur 48 cas. S-2 ne separait donc
    pas l'ordre 2 du premier ordre : sa tolerance valait dix fois l'effet.
  - A absorbeur faible (a = 0.5 et 1, 48 cas, sans attendu de ma part), C1 est plus pres de tes boites
    que C2 aux 48 cas : plus grand |2D - C1| = 1.65e-03, plus grand |2D - C2| = 3.16e-03. A a = 0.5, 2D
    - C1 est negatif aux douze cas de coupe paire et positif aux douze de coupe impaire ; C2 - C1 a le
    signe OPPOSE aux 24 cas.
  - 2D - C1 est multiplie par 3.60 a 4.48 quand g double : un terme en g^2 dans Gamma / g. Lu comme un
    changement de force de l'absorbeur, il est negatif aux 48 cas (un absorbeur plus faible a deux
    dimensions) et grandit avec la coupe. Ce n'est pas un nombre unique : un signe, pas une loi.
    Candidat non eprouve : ton absorbeur est sur les sites nus, ma chaine sur les sites habilles.
  - Le plateau lui-meme ne bouge pas : moyenne des 48 cas forts 0.054413 aux deux couplages ; d'un
    couplage a l'autre Gamma / g change de 1.9e-05 au plus.
Ce que j'en tire pour un gel : la chaine predit le PLATEAU, pas la dependance en absorbeur. Un attendu
sur le sommet se lit a absorbeur sature, et aucune de mes tolerances ne doit pretendre separer les
ordres.

## 4. (B) EST OUVERT : CE QUE CELA VEUT DIRE CE SOIR

Le mot de l'operateur est en tete de cette note. Ce que j'en fais :
  - je n'ecris PAS le gel ce soir. Le 21/11 tu as ecrit (D4, que j'ai pris) que le profil ne se joue pas
    avec les instruments tels quels : l'echelle des absorbeurs vaut |w2 - 2| ; l'etat sans barriere n'a
    pas de definition gelee ; le lecteur est a requalifier a un point sacrifie. Les sections 6 et 7 sont
    ma part de ce travail, a une dimension ; la section 8 est la tienne, a deux dimensions ;
  - la qualification Q se joue CHEZ TOI. Je ne lirai rien a deux dimensions aux points de Q avant
    d'avoir recu et authentifie ton lot ;
  - l'esquisse de la section 9 n'engage personne. Le gel s'ecrira en deux parties, comme les deux
    precedents, apres ton retour.

## 5. CE QUI EST DEJA ECRIT CHEZ NOUS, ET DONT (B) PART

Cherche avant d'ecrire, apres mes defauts D-REL-27 et celui de l'acte 86 :
  - gel "largeur du vide", partie 1 (b57c9ccdd3946261) : la cellule est (w2, m), son couplage g =
    kappa_m |w2 - 2| P / X(w2) ecrit a six chiffres ; kappa_m = 0.0262, 0.0200, 0.0159, 0.0130
    (lisibles), 0.00928, 0.00558, 0.00382 (profondes) ; kappa = t_0 / |w2 - 2|, t_0 = g X(w2) / P ;
  - meme gel, partie 2 (eebd979f18d8db48), 4.2 et 5 : le lecteur creux au site (0, 0) depuis l'energie
    0, quatre absorbeurs (A : F2, 80 couches ; B : F2, 100 ; C : F1, 100 ; D : F2, bord r_c + 10, 80),
    douze barreaux k = -3 a 8, eta_k = eta0 2^(-k), r_c = 2 (m + max(8, m)) + 2, eta0 = |w2 - 2| ;
    plateau : cinq barreaux consecutifs, max <= 1.05 min ; B, C, D a 0.05 de A en logarithme ; temoin :
    le jumeau sans fantome, plus grande largeur <= 1e-6 Gamma_pl ; bande = etendue de la chaine +
    etalement du lecteur ; T = 0.02 (lisible) et 0.05 (profonde) ;
  - le predicteur : la chaine d'ordre 3 des blocs deposes sous l'absorbeur adapte (bloc
    49a40d9098b55361), plateau et etendue de ses dix-huit variantes ;
  - ma note sur le vide du 16/11 (15641e09a351d56d), 2.3 : le mandataire a une dimension de l'absorbeur
    du lecteur (r = 2 m le long de l'echelle ; F1 : eta (r - bord)^2 ; F2 : eta (r - bord)^4 / L^2) ;
  - acte du delta 102 : V1 et VP TENUS a 28 cellules, plus grand |ln q| 0.00068 et 0.00134 ;
  - nos echanges du 21/11 : le lecteur a qualifie jusqu'a 1.785e-05 (delta 100, cellule N4) ; le point
    sacrifie alors PROPOSE, w2 = 2.0001, ou tes chiffres et les miens se recoupent (0.0403 g et
    0.0194 g) ; eta0 = |w2 - 2| dans toutes les sorties deposees ; le pole a 0.0544 g.
Ce que je n'ai pas relu ce soir : la feuille deposee du lecteur (83701094e6a2b965) ligne a ligne ; le
bloc LECTEUR CREUX de la sonde deposee (d5cc48f48e37af99). Si l'un ou l'autre porte |w2 - 2| ailleurs
que dans eta0, c'est a toi de le voir en jouant Q, et c'est exactement ce que Q doit trouver.

## 6. A UNE DIMENSION : OU EST LE SOMMET, ET CE QUE LA CHAINE Y PREDIT (sommet_1d_machine1_v1.py)

Le moteur (82a0be882568fe0c) et les trois blocs deposes (7cd5977bc27bebc1, 534ba246aa3b8973,
49a40d9098b55361) sont lus dans un clone neuf du registre public, tete 055be58, au canon controle, et
charges sans etre edites.
6.1 La barriere, en kappa. Regle du moteur : le site m est dans la barriere si |e_m| > 2 |t_m|. A la
limite du desaccord nul, tau_0 = X(2) / P = 0.102062073 (ma forme close : 0.102062073), et :
    le site 1 entre pour |d| / g > 1.5713, soit kappa < 0.06495 ;   le site 2 : 2.3582, 0.04328 ;
    le site 3 : 3.3604, 0.03037 ;   le site 4 : 4.5077, 0.02264.
    profondeur 0 (fenetre SANS barriere) : kappa > 0.06495 ;
    profondeur 1 : milieu geometrique 0.0530, |d| / g = 1.925 ;
    profondeur 2 : milieu geometrique 0.0363, |d| / g = 2.815 ;
    profondeur 3 : milieu geometrique 0.0262, |d| / g = 3.892 : c'est le kappa_3 du gel du vide.
Les sept profondeurs du gel du vide sont a |d| / g = 3.90, 5.10, 6.42, 7.85, 11.00, 18.29 et 26.72. Ma
phrase de la 22f, "je n'ai pas recalcule leur d / g ce soir", est levee : le delta 102 a juge les AILES,
et rien en deca de |d| / g = 3.66 (cellule PG3, d'apres son fichier depose). Mon "profil qui ne depend
que de d / g" n'est rien d'autre que la loi d'echelle Gamma = |d| Phi(kappa), ecrite a w2 voisin de 2.
6.2 La chaine au sommet. Points de qualification (w2 = 2 exactement ; w2 = 2.0001) et grille de 42
cellules (sept kappa, trois couplages vises de 2.5e-04 a 3e-03, deux signes), ordres 1, 2 et 3 sous
l'absorbeur adapte, dix-huit variantes :
    point            w2       g        G3* / g     G3*          etendue
    Q-a              2        2.5e-04  0.054431    1.36076e-05  0.0030
    Q-c              2        1e-03    0.054431    5.44311e-05  0.0016
    Q-d              2        2e-03    0.054430    1.08861e-04  0.0028
    Q-e              2.0001   3e-04    0.040308    1.20924e-05  0.0026
    Q-f              2.0001   1.5e-04  0.019431    2.91470e-06  0.0032
Sur la grille : etendue d'ordre 3 de 0.0040 au plus ; |ln(G3 / G1)| de 0.0043 au plus ; |ln(G3 / G2)| de
0.0005 au plus. La loi d'echelle y tient a 0.0032 pres en logarithme a kappa fixe, d'un couplage a
l'autre et d'un signe a l'autre.
6.3 Deux choses que le bloc depose ne fait pas, et que le gel devra fixer :
  (i) quand la barriere du moteur est VIDE (kappa > 0.06495), sites[-1] n'existe pas : j'ai pose m_bord
      = 0 a la main, et M_facteur = 5 au lieu de 4 pour que les tables couvrent les dix-huit variantes ;
  (ii) a w2 = 2 exactement la regle de lecture du bloc divise par |d|. J'ai refait la meme lecture (le
      flux) sans cette division. La ou d n'est pas nul, elle rend le plateau et l'etendue du bloc depose
      a 0.0e+00 pres, a 44 points sur 44.
6.4 Les cellules candidates de l'esquisse (esquisse_gel_sommet_machine1_v1.py) : 133 cellules (19 w2, 7
kappa), toutes eligibles au sens du gel du vide (m_bord = cible, etendue <= 0.02) :
    kappa    profondeur  Phi = G3* / |d|            G3* / g
    0.0363   2           6.6833e-06 a 6.6837e-06    1.8756e-05 a 1.8827e-05
    0.0530   1           1.7954e-04 a 1.7960e-04    3.4509e-04 a 3.4650e-04
    0.0800   0           2.3951e-03 a 2.3964e-03    3.0499e-03 a 3.0630e-03
    0.1300   0           1.7941e-02 a 1.7945e-02    1.4059e-02 a 1.4115e-02
    0.2000   0           5.5765e-02 a 5.5780e-02    2.8404e-02 a 2.8518e-02
    0.4000   0           1.7792e-01 a 1.7798e-01    4.5313e-02 a 4.5497e-02
    1.0000   0           5.1726e-01 a 5.1746e-01    5.2694e-02 a 5.2912e-02
Couplages de 1.77800e-05 a 4.90817e-03 ; largeurs predites de 3.34172e-10 a 2.58728e-04 ; etendue de
0.0036 au plus ; |ln(G3 / G1)| de 0.0003 au plus. Le premier site ou le saut depasse 1 (m*) va de 16 a
159 ; a aucune cellule l'absorbeur du lecteur ne commence au-dela de m*. A 43 cellules la largeur
predite depasse 1.785e-05, jusqu'a 14.5 fois : c'est pourquoi Q porte un point a g = 2e-03.
A la jonction : aux quatre cellules de trois barreaux du delta 102, lues dans leurs fichiers deposes,
Gamma_pl / |d| va de 1.6342e-07 a 1.6503e-07, pour |d| / g de 3.657 a 4.170.

## 7. LE MANDATAIRE DU LECTEUR AU SOMMET (partie 3 du meme script ; UNE dimension, premier ordre)

C'est le mandataire de ma note du 16/11, porte au sommet : la chaine du premier ordre, a qui l'on donne
les quatre absorbeurs DU LECTEUR lus le long de l'echelle, douze barreaux, puis la regle de plateau et
la regle d'accord de la feuille deposee. L'etat lu est le plus proche de l'energie 0 ; r_c = 18, 20 ou
22 selon la profondeur 0, 1 ou 2.
  - Regle du depot, eta0 = |w2 - 2|. Degeneree a w2 = 2. NON QUALIFIE au point Q-e (pas de plateau sous
    D, rapport 1.0742) et aux quatre cellules de kappa = 0.4 et 1 ; ailleurs les fenetres glissent vers
    le bord fort de l'echelle (A et B a k0 = -3 des kappa = 0.08). Elle se defait a mesure que |d| / g
    baisse : c'est notre accord du 21/11.
  - Regle en absolu, eta0 = g X(w2) / (P kappa_3), kappa_3 = 0.0262 : la valeur qu'aurait |w2 - 2| a une
    cellule de trois barreaux du gel du vide jouee au meme couplage (eta0 / g = 3.8955 a w2 = 2).
    QUALIFIE a 19 points sur 19 : les cinq points de Q et quatorze cellules de la grille. Fenetres : A a
    k0 = -1 partout ; B a -1 ou 0 ; C a 0, +1 ou +2 ; D a -2 ou -1. Plus grand |ln(X / A)| : 0.0054.
    Poids du site 0 dans les fenetres : 0.899 au moins. A w2 = 2 le plateau est celui de l'absorbeur
    adapte a 0.0043 pres (sous C). Aux points de Q la regle supporte un facteur 4 dans les deux sens :
    memes plateaux, fenetres deplacees de deux barreaux.
  - APRES COUP, ce que valait ce mandataire la ou la 2D existe (fenetres_vide_delta102_machine1_v1.py,
    lecture de tes sorties deposees du delta 102) : aux quatre cellules de trois barreaux, eta0 / g de
    3.657 a 4.170, les fenetres retenues sont A a -2 ou -1, B a -1, C a +1 ou +2, D a -2. A un barreau
    pres, ce sont celles que le mandataire annonce au sommet sous la regle en absolu.
Ce que le mandataire ne dit pas : rien de la 2D. Il ne contient ni les etats hors echelle, ni ce que le
systeme fait au-dela de m*. Aux barreaux faibles des fenetres et aux plus forts couplages, l'absorption
peut se faire au-dela de m* : estimation a la main, que je n'ai pas journalisee.

## 8. LA QUALIFICATION "Q" : A JOUER CHEZ TOI

8.1 Les points. Tous sacrifies, declares ici AVANT toute lecture :
    Q-a   w2 = 2          g = 2.5e-04    eta0 = 9.73875e-04
    Q-c   w2 = 2          g = 1e-03      eta0 = 3.89550e-03
    Q-d   w2 = 2          g = 2e-03      eta0 = 7.79100e-03
    Q-e   w2 = 20001/10000   g = 3e-04   eta0 = 1.16821e-03
    Q-f   w2 = 20001/10000   g = 1.5e-04   eta0 = 5.84106e-04
w2 = 2 exactement, de 2.5e-04 a 2e-03, est deja hors de tout tirage futur (ma 22e, ta 22f). J'y ajoute,
des maintenant : w2 = 2.0001 a TOUT couplage. Aucun autre point n'est sacrifie.
8.2 L'instrument. Le bloc LECTEUR CREUX de la sonde deposee (d5cc48f48e37af99), execute depuis son
fichier, comme le fait la sonde du gel du vide (0f82986cca133330) : site (0, 0), energie de depart 0, le
jumeau (signe +1) puis le fantome (signe -1) ; les quatre absorbeurs du depot ; douze barreaux k = -3 a
8, eta_k = eta0 2^(-k) ; r_c = 18, soit 2 (0 + max(8, 0)) + 2. UNE SEULE chose change : eta0 = g X(w2) /
(P kappa_3), calcule en double precision et ecrit a six chiffres (les valeurs du 8.1 sont les miennes ;
dis les tiennes). Jugement : juger_etat de la feuille deposee (83701094e6a2b965), telle quelle ;
temoin : le jumeau, 48 lectures suivies et plus grande largeur <= 1e-6 Gamma_pl. Le pilote est le tien.
8.3 Les attendus, ecrits avant toute lecture 2D a ces points par cet instrument :
  Q-1  les cinq points sont QUALIFIES par la feuille deposee. 0.8.
  Q-2  a chaque point qualifie, |ln(Gamma_pl / G3*)| <= 0.010, G3* etant la colonne du 6.2 :
       1.36076e-05, 5.44311e-05, 1.08861e-04, 1.20924e-05, 2.91470e-06. 0.75.
  Q-3  le temoin tient aux cinq points. 0.9.
  Q-4  les fenetres retenues, aux vingt (point, absorbeur) : A et B a k0 = -2, -1 ou 0 ; C a 0, +1 ou
       +2 ; D a -3, -2 ou -1 ; a 16 au moins sur 20. 0.6. Une epreuve du mandataire, pas du lecteur.
  Q-5  si Q-a et Q-d sont qualifies, |ln[(Gamma_pl / g)(Q-d) / (Gamma_pl / g)(Q-a)]| <= 0.005. 0.75.
CE QUI ME DONNERAIT TORT : un point qualifie ou |ln(Gamma_pl / G3*)| depasse 0.02 ; ou deux points ou
plus sans plateau sous A. Alors la regle en absolu n'est pas le bon remede, ou ce que cet instrument lit
au sommet n'est pas le pole de la chaine.
CE QUE CHAQUE ISSUE ENGAGE. Tout tient : j'ecris la premiere partie du gel avec cette regle. Q-d seul
manque : le gel borne ses couplages sous 2e-03 et le dit. Q-2 tombe a 0.010 mais rien ne depasse 0.02 :
la tolerance du gel se discute AVANT que je l'ecrive, pas apres. Mon tort est realise : pas de gel ; on
ecrit pourquoi.
8.4 Ce que Q ne dit pas : rien hors de ces cinq points ; rien de delta < 0 ; rien des profondeurs 1
et 2. Les tolerances de Q-2, Q-4 et Q-5 sont posees a la main (0.010 vaut trois fois l'etendue de la
chaine).

## 9. L'ESQUISSE DU GEL "SOMMET" (RIEN N'EST GELE ; A DEMOLIR DANS LE MEME RETOUR)

OBJET. La largeur de plateau de l'etat porte par (0, 0), lue par le lecteur creux sous la regle en
absolu, qualifiee dans le run, a des cellules tirees.
CELLULES. (w2, kappa) ; couplage ecrit g = kappa |w2 - 2| P / X(w2), six chiffres : la regle du gel du
vide. Sept kappa par w2 : 0.0363 (deux barreaux), 0.0530 (un barreau), 0.0800, 0.1300, 0.2000, 0.4000,
1.0000 (fenetre sans barriere). Quatre creneaux, un w2 tire par creneau, donc 28 cellules :
    MP  delta < 0   |w2 - 2| = 0.5, 1.0, 1.5, 2.0 dix-milliemes
    PP  delta > 0   |w2 - 2| = 0.5, 1.5, 2.0 dix-milliemes (2.0001 est retire)
    MG  delta < 0   |w2 - 2| = 2.5, 3.0, 3.5, 4.0, 4.5, 5.0 dix-milliemes
    PG  delta > 0   les memes
Tirage par le hachage des deux gels deposes, graine donnee par l'operateur apres la certification de la
premiere partie ; table commune d'eligibilite avant la graine.
INSTRUMENT. Celui de Q s'il qualifie, avec eta0 = max(|w2 - 2|, g X(w2) / (P kappa_3)), qui redonne la
regle du depot a trois barreaux et plus ; r_c = 2 (m + max(8, m)) + 2 avec m = 0 quand la barriere du
moteur est vide ; l'etage A du gel du vide inchange (ancres, temoins du depot) ; le jumeau a chaque
cellule. Le predicteur : la chaine d'ordre 3 du bloc depose, avec les deux points du 6.3 fixes par
ecrit.
ENONCE S1, unique. Aux cellules lues, la chaine rend la largeur a T = 0.02 pres en logarithme, bande =
etendue + etalement du lecteur, issues comptees comme V1.
CONSIGNE SANS JUGEMENT. Gamma_pl / |d| a kappa egal d'un creneau a l'autre (la loi d'echelle) ; le
signe ; les ordres 1 et 2 ; Gamma_pl / t_0.
CE QUE S1 SEPARE ET NE SEPARE PAS. Aux 133 candidates l'ordre 3 differe du premier ordre de 0.0003 au
plus : S1 n'oppose pas les ordres. Il eprouve ceci : le mecanisme de l'echelle et la chaine rendent la
largeur du vide de trois barreaux jusqu'a la fenetre sans barriere, la ou elle vaut jusqu'a la moitie du
saut au pied de l'echelle.
CE QUE L'ACTE NE POURRAIT PAS ECRIRE : rien de la duree de vie du systeme ferme ; rien de w2 = 2
exactement, qui n'est pas tire (il est lu a Q, hors gel) ; rien au-dela de kappa = 1.
MES QUESTIONS, pour ta demolition :
  (a) la regle eta0 = max(|w2 - 2|, g X(w2) / (P kappa_3)) te convient-elle, ou veux-tu une echelle a
      toi ?
  (b) "l'etat le plus proche de l'energie 0, de poids au moins 0.5 au site (0, 0)" suffit-il a definir
      l'etat sans barriere, ou faut-il autre chose (ton D4 (iii)) ?
  (c) sept kappa, dont cinq sans barriere : trop, trop peu, mal places ? kappa = 1 est a |d| / g =
      0.102 ;
  (d) T = 0.02 : au delta 102 le plus grand |ln q| lisible etait 0.00068. Veux-tu plus serre ?
  (e) des couplages jusqu'a 4.9e-03 (creneaux MG et PG a kappa = 1) : la largeur y vaut 14.5 fois le
      plus grand plateau qualifie. Faut-il borner, ou laisser le lecteur le dire dans le run ?
  (f) ce que je n'ai pas vu.

## 10. LIMITES, ET DEFAUTS DE MA PLUME

L-9   Les sections 6 et 7 sont a une dimension. Le mandataire est du premier ordre, le long de l'echelle
      seule. Qu'il ait rendu les fenetres aux cellules de trois barreaux est un constat d'apres coup.
L-10  Au sommet l'etat lu n'est isole par aucune barriere. C'est la premiere fois que le lecteur y est
      envoye ; l'accord de ses quatre absorbeurs n'eprouve pas une erreur commune aux quatre (G-8 du gel
      du vide).
L-11  Les tolerances de Q et de l'esquisse sont posees a la main.
L-12  La normalisation de mes elements neufs est lue sur tau_0, pas dans un gel.
D-REL-28  Ma 22f donnait la table d'ordre 2 pour reference de S-2 et ecrivait "l'ordre 2 deplace Gamma /
          g de 1.5e-03 au plus" sans verifier que S-2 separait l'ordre 2 du premier ordre (il ne les
          separe pas) ni dire dans quel sens tes boites iraient. L'attendu a tenu ; il ne dit rien de
          l'ordre 2. Et mes "56 sur 56" de la 22f n'etaient pas un controle independant des elements
          (section 2).

## 11. PIECES (convention B)

    cette note
    note_pole_court_machine1_v1.py                      S-1 a S-3 notes depuis tes JSON
    note_pole_court_machine1_v1.log
    controle_pole_court_machine1_v1.py                  elements neufs, chaine du premier ordre, rejeu
    controle_pole_court_machine1_v1.log                 ses trois parties (la troisieme : huit boites)
    lecture_apres_coup_pole_court_machine1_v1.py        2D contre les deux chaines, apres coup
    lecture_apres_coup_pole_court_machine1_v1.log
    sommet_1d_machine1_v1.py                            barriere, predicteur, mandataire
    sommet_1d_machine1_v1.log
    esquisse_gel_sommet_machine1_v1.py                  les 133 cellules candidates au predicteur
    esquisse_gel_sommet_machine1_v1.log
    fenetres_vide_delta102_machine1_v1.py               les fenetres de ton run du delta 102, lues
    fenetres_vide_delta102_machine1_v1.log
    controle_note_pole_court_lu_machine1_v1.py          le controle de cette note
    controle_note_pole_court_lu_machine1_v1.log
    fabrique_envoi_22g_machine1_v1.py                   la fabrique du lot et de l'enveloppe
Entrants : ton lot 2d69195af996cc0f (lu comme des donnees) ; mon lot 2c546b0a617f1a0d et sa note
6eae3f6860a46eef ; le registre public en tete 055be58, clone neuf, lu, non ecrit : le moteur
82a0be882568fe0c, les blocs 7cd5977bc27bebc1, 534ba246aa3b8973 et 49a40d9098b55361, executes au canon
controle, et les quatre sorties sonde_vide_MG3, MP3, PP3 et PG3 du delta 102, lues.
