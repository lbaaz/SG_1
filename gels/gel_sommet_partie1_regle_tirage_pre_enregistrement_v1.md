GEL "SOMMET" -- PREMIERE PARTIE : LA REGLE DE TIRAGE ET D'ELIGIBILITE DES CELLULES
PRE-ENREGISTREMENT v1 -- machine 1, 2026-11-22.
A CERTIFIER PAR MACHINE 2 AVANT QUE L'OPERATEUR DONNE LA GRAINE.

0. STATUT
  Cette piece fixe COMMENT les cellules du gel seront tirees, QUAND un tirage est admis, et les
  trois nombres ecrits de chaque cellule (son couplage, l'echelle de l'absorbeur du lecteur, son
  rayon). Elle ne fixe ni les enonces juges, ni les tolerances, ni les probabilites, ni
  l'instrument : c'est la seconde partie, ecrite apres le tirage sur les chaines seules, et
  certifiee avant tout run.
  L'objet du gel : la largeur de l'etat que porte le site (0, 0) du systeme a fantome, "le vide",
  lue en 2D par le lecteur creux, AU SOMMET du profil : la ou le saut au pied de l'echelle n'est
  plus petit devant le desaccord, de deux barreaux de barriere jusqu'a la fenetre sans barriere ; et
  ce que la chaine a une dimension en predit. Le gel "largeur du vide" (delta 102) a juge les ailes,
  a trois barreaux et plus ; celui-ci prolonge la meme loi d'echelle, Gamma = |w2 - 2| Phi(kappa),
  de kappa = 0.0363 a kappa = 1.
  Ouverture, selon machine 1 : sa note du 22/11 proposait d'ouvrir le sommet ; l'operateur a ecrit
  "je dis oui on ouvre. Par contre tous les calculs couteux, c'est sur machine 2 ok ?" (22/11/2026,
  20 h 09). A l'operateur de l'attester ou de le dementir. Depuis, machine 2 a lu neuf points
  sacrifies (les qualifications "Q" et "Q2", section 8) ; les attendus ecrits avant ont tenu et rien
  n'a donne tort a la plume.
  E19. Selon ses pieces (section 9), machine 1 n'a fait AUCUN calcul 2D, du systeme a fantome ou du
  jumeau, dense ou creux, a un w2 candidat. Tout ce que cette piece calcule est une chaine a une
  dimension. Les seules lectures 2D du systeme a fantome au sommet sont les neuf points de machine
  2, a w2 = 2, 20001/10000 et 19999/10000, qui ne sont pas candidats. Aucune des deux machines ne
  fera de calcul 2D a un w2 candidat avant la certification croisee de la seconde partie, ni ne lira
  une cellule tiree avant le run. Machine 2 dit ce qu'il en est pour elle (section 10, d).

1. SOURCES (convention B)
    82a0be882568fe0c scripts/m17_chaine_v17.py (registre 055be58), le moteur
    7cd5977bc27bebc1 scripts/chaine_ordre2_bloc_machine1_v1.py (registre), le bloc d'ordre 2
    534ba246aa3b8973 scripts/ordre3_bloc_machine1_v1.py (registre), le bloc d'ordre 3
    49a40d9098b55361 scripts/chaine_adaptee_bloc_machine1_v1.py (registre), l'absorbeur adapte et
                     son plateau
    b57c9ccdd3946261 gels/gel_largeur_vide_partie1_regle_tirage_pre_enregistrement_v1.md
                     (registre) : la regle dont celle-ci reprend la forme
    cc1b2df637a9f3cd scripts/tirage_vide_machine1_v1.py (registre), le tirage dont celui de ce lot
                     derive
    34eb68229983b1f2 scripts/eligibilite_vide_machine1_v1.py (registre), l'eligibilite dont celle de
                     ce lot derive
    af52bf8e4913338f journal/balayage_virginite_pont_machine1_v1.py (registre), le balayage dont
                     celui de ce lot derive
    1e3bcbb42899069e POUR_MACHINE2_pole_court_lu_et_qualification_du_sommet_machine1_v1.md (lot
                     423ec0fd24240977) : le sommet a une dimension, l'esquisse, la qualification Q
    f59bdc4b2a8bc3d1 POUR_MACHINE2_Q_notee_et_Q2_attendus_machine1_v1.md (lot 074b131287ad2b6f) : la
                     demolition de machine 2 prise, les attendus de Q2
  Les lectures de Q et de Q2 sont dans les lots c58c2b3f533c516b et 295b2b1549b076c2 de machine 2.
  Ces deux lots et les deux de machine 1 cites ci-dessus sont HORS REGISTRE ; les deux machines les
  detiennent.

2. LES CRENEAUX ET LES CELLULES
  Quatre creneaux. Les w2 candidats sont au cent-millieme : w2 = 2 - k / 100000 ou 2 + k / 100000, k
  entier.
    MP  delta < 0, petit  k = 5 a 20, sauf 10   w2 = 1.99980 a 1.99995   15 valeurs
    PP  delta > 0, petit  k = 5 a 20, sauf 10   w2 = 2.00005 a 2.00020   15 valeurs
    MG  delta < 0, grand  k = 25 a 49           w2 = 1.99951 a 1.99975   25 valeurs
    PG  delta > 0, grand  k = 25 a 49           w2 = 2.00025 a 2.00049   25 valeurs
  Ne sont PAS candidats : k = 10 (w2 = 19999/10000 et 20001/10000, sacrifies a tout couplage par les
  qualifications) ; k = 50 (w2 = 3999/2000 et 4001/2000 : machine 2 y a lu le JUMEAU en 2D le 16/11,
  section 9) ; k = 21 a 24, qui separent les creneaux ; w2 = 2, qui n'est d'aucun creneau.
  Sept KAPPA, chacun avec sa PROFONDEUR CIBLE de barriere, constantes de ce gel, numerotes de 1 a
  7 :
    DEUX BARREAUX   1 : 0.0363        UN BARREAU   2 : 0.0530
    SANS BARRIERE   3 : 0.0800   4 : 0.1300   5 : 0.2000   6 : 0.4000   7 : 1.0000
  Une CELLULE est un couple (w2, kappa). Elle a TROIS NOMBRES ECRITS :
      g    = kappa x |w2 - 2| x P / X(w2) ,
               avec X(w2) = X_saut_reel(P, 2, 1, 0, 0, w2) du moteur et P = 5 ;
      eta0 = max( |w2 - 2| , g x X(w2) / (P x kappa_3) ) ,   kappa_3 = 0.0262 ;
      r_c  = 2 (m_bord + max(8, m_bord)) + 2 ,   m_bord etant celui de la section 4.1.
  g est calcule en double precision puis ARRONDI a six chiffres significatifs (le format .5e de
  Python, precede du signe pour cent) : le couplage de la cellule EST le nombre decimal ainsi ecrit.
  eta0 est calcule avec ce couplage ECRIT, puis ecrit de la meme facon. kappa est le rapport du saut
  au pied de l'echelle, t_0 = g X(w2) / P, au desaccord |w2 - 2|. eta0 est l'echelle des absorbeurs
  du lecteur a la cellule (eta_k = eta0 2^(-k)) et r_c son rayon de coeur ; la seconde partie les
  prendra tels qu'ils sont ecrits ici.
  D'ou viennent les kappa : 0.0363 et 0.0530 sont, a trois chiffres, le milieu geometrique de
  l'intervalle de kappa ou la barriere de l'etat (0, 0), a la limite du desaccord nul, finit au site
  2 et au site 1 ; la fenetre sans barriere commence a kappa = 0.06495 ; les cinq autres y sont
  poses a la main, jusqu'a 1. kappa_3 = 0.0262 est le kappa des cellules de trois barreaux du gel
  "largeur du vide". Ce gel fige les decimales, pas la derivation.
  Ce que vaut la regle de eta0 : une CONVENTION. Son premier terme est la regle du depot ; son
  second est la valeur qu'aurait |w2 - 2| a une cellule de trois barreaux jouee au meme couplage.
  Aux neuf points lus, le plateau du lecteur est plat sur huit barreaux sous cette regle : cela dit
  que l'instrument lit a cette echelle ou a peu pres, pas que 0.0262 est la bonne valeur (reserve de
  machine 2, prise).
  Un tirage donne DEUX w2 par creneau, donc huit w2 et cinquante-six cellules, nommees par le
  creneau, le rang du w2 dans le tirage (a pour le premier retenu, b pour le second) et le numero du
  kappa : MPa1 a MPa7, MPb1 a MPb7, et de meme pour PP, MG, PG. Cinquante-six cellules ne sont pas
  cinquante-six epreuves independantes : les sept cellules d'un w2 partagent la meme echelle, et la
  loi d'echelle les lie d'un w2 a l'autre. Ce sont HUIT tirages.

3. LE TIRAGE
  Le w2 du creneau s au rang r est l'element de numero
        int( sha256("<graine>|<s>|<r>") ecrit en hexadecimal, 16 )  modulo  n_s
  de la liste CROISSANTE des n_s w2 candidats du creneau, numerotee a partir de 0. La chaine hachee
  est codee en ASCII ; s vaut MP, PP, MG ou PG ; r s'ecrit en decimal, sans zero devant ; la barre
  verticale est le caractere 124. C'est le hachage des gels "ordre 3", "largeur du vide" et "pont".
  LA GRAINE est une suite de chiffres (0 a 9), d'au moins six chiffres, donnee par L'OPERATEUR, par
  ecrit, aux deux machines, APRES la certification de cette piece et apres que la table commune de
  la section 5 existe. Elle est reportee telle quelle, zeros de tete compris, dans la seconde
  partie. Ni machine 1 ni machine 2 ne la choisit, ne la propose, ni ne la commente avant de l'avoir
  recue.
  Chaque machine tire par SON code. Exemple de controle, sur une graine de demonstration qui n'est
  pas une suite de chiffres et ne peut donc pas etre la graine :
    sha256("DEMONSTRATION|MP|0") = e2635f39a4c07247... ; modulo 15 = 2 -> w2 = 1.99982
    sha256("DEMONSTRATION|MP|1") = 224e72412f5e326d... ; modulo 15 = 5 -> w2 = 1.99985
    sha256("DEMONSTRATION|PP|0") = 4ba38823b0866663... ; modulo 15 = 14 -> w2 = 2.00020
    sha256("DEMONSTRATION|PP|1") = 8b5230465a9345ca... ; modulo 15 = 12 -> w2 = 2.00018
    sha256("DEMONSTRATION|MG|0") = 8254e7d473dd8e66... ; modulo 25 = 4 -> w2 = 1.99955
    sha256("DEMONSTRATION|MG|1") = 3bcf50fd02de7108... ; modulo 25 = 22 -> w2 = 1.99973
    sha256("DEMONSTRATION|PG|0") = c67ae8de8fe0b645... ; modulo 25 = 2 -> w2 = 2.00027
    sha256("DEMONSTRATION|PG|1") = a72d87914f9453df... ; modulo 25 = 16 -> w2 = 2.00041

4. L'ELIGIBILITE D'UNE CELLULE (chaine seule, aucune 2D)
  4.1 La barriere : sites = barriere(0, 0, w2, g, avec Sigma2) du moteur (le site m y entre si |e_m|
      > 2 |t_m|). Si la liste est VIDE : m_bord = 0, e_bord = 0, et les tables recoivent la liste a
      un seul site (0, 0, |t_site(0, 0, 0, w2, g)|). Sinon m_bord est son dernier site et e_bord =
      |m_bord delta + Sigma2(m_bord) - Sigma2(0)|, avec delta = w2 - 2.
  4.2 Les tables : tables_ordre2(0, 0, w2, g, sites, M_facteur 5) puis tables_ordre3, des blocs
      deposes. Par site m de l'echelle : le decalage S_m, le saut du premier ordre t_m (de m a m +
      1), le saut au second voisin U_m, et a l'ordre 3 la correction T3_m du saut et les sauts W3_m
      (de m a m + 3) et W5_m (de m a m + 5). M_facteur vaut 5 et non 4 : quand m_bord = 0 les tables
      de facteur 4 s'arretent au site 32, et la plus longue variante va au site 34.
  4.3 La chaine d'ordre 3 sous ABSORBEUR ADAPTE, variante (a, c, L). debut = m_bord + c. Les sites
      vont du premier site des tables (m_min) au site debut + L. Matrice symetrique complexe : sur
      la diagonale, m delta + S_m - S_0 - i W_m ; hors diagonale, t_m + T3_m entre m et m + 1, U_m
      entre m et m + 2, W3_m entre m et m + 3, W5_m entre m et m + 5. L'absorbeur :
        W_m = a |t_m| ((m - debut) / L)^2   pour debut < m <= debut + L ,   0 ailleurs.
      Dix-huit variantes : a = 1, 2, 4 ; c = 6, 8, 10 ; L = 16, 24. C'est la chaine du gel "largeur
      du vide", calculee par le bloc depose tel quel.
  4.4 La largeur d'une variante : Gamma = -2 Im(E), E etant la valeur propre de cette matrice dont
      le vecteur propre, norme, porte le plus grand poids sur le site 0. C'est une propriete de la
      matrice : chaque machine la calcule par sa methode. Machine 1 la lit par le flux, comme le
      bloc depose le fait tant que Gamma / |delta| > 1e-15 : c'est le cas a toutes les cellules
      candidates.
  4.5 Le PLATEAU G3* est l'exponentielle de la mediane des dix-huit ln Gamma (la moyenne des deux
      valeurs centrales) ; l'ETENDUE est le plus grand moins le plus petit des dix-huit ln Gamma.
      Elle est indefinie si l'une des largeurs n'est pas strictement positive.
  4.6 La cellule (w2, kappa) est ELIGIBLE si : (i) m_bord = la profondeur cible de son kappa ; (ii)
      e_bord < 0.7 ; (iii) l'etendue est definie et <= 0.005.
  4.7 Un w2 candidat est ELIGIBLE si ses SEPT cellules le sont.
  4.8 D'ou viennent les nombres. 0.7 est la garde du domaine du gel "ordre 3" depose. Le seuil 0.005
      est la moitie de la tolerance de 0.01 dont les deux machines sont convenues pour la seconde
      partie ; il est pose APRES l'esquisse du 22/11, qui avait calcule, en chaine seule, 133
      cellules dont 112 sont des cellules candidates d'ici (16 w2 ; etendue de 0.0036 au plus), et
      AVANT d'avoir calcule les 448 autres. La grille au cent-millieme, les deux w2 par creneau, les
      dix rangs et le retrait de k = 50 sont poses ici. Les kappa, la regle de eta0 et celle de la
      barriere vide viennent de l'esquisse et des deux qualifications. Aucun de ces nombres ne sera
      regle ensuite.

5. LA TABLE COMMUNE, AVANT LA GRAINE
  Chaque machine calcule par SA chaine l'eligibilite des 560 cellules candidates (80 w2) AVANT que
  la graine existe. La table de machine 1 est en section 7. Machine 2 rend la sienne avec sa
  certification. LA TABLE COMMUNE est leur ET : un w2 candidat y est eligible si et seulement s'il
  l'est dans les deux tables ET si les trois nombres ecrits (g, eta0, r_c) de ses sept cellules sont
  les memes dans les deux. Elle ne depend d'aucune graine. Un desaccord entre les deux tables est
  dit dans la certification ; il n'arrete pas le gel.
  Format d'une table : JSON, creneaux -> <nom du creneau> -> candidats -> liste de {"w2": "<fraction
  irreductible>", "eligible": true ou false, "cellules": liste de {"kappa": "<le decimal a quatre
  decimales>", "g": "<le decimal a six chiffres>", "eta0": "<le decimal a six chiffres>", "r_c":
  <entier>, "eligible": true ou false}}.

6. LA REGLE DES RANGS
  Pour chaque creneau, dans l'ordre MP, PP, MG, PG et independamment : on parcourt les rangs 0, 1,
  2, ... Le w2 tire a un rang est RETENU s'il est eligible dans la table commune et s'il n'est pas
  deja retenu ; sinon on passe au rang suivant, pour le CRENEAU ENTIER (jamais cellule par cellule).
  On s'arrete a DEUX w2 retenus : le premier est "a", le second "b". Au plus dix rangs, de 0 a 9. Si
  un creneau n'a pas deux w2 eligibles distincts en dix rangs : PAS DE GEL, et on le dit.
  Si les deux machines ne tirent pas les memes cellules, avec les memes trois nombres ecrits, a
  partir de la meme graine et de la meme table commune : PAS DE GEL tant que l'ecart n'est pas
  explique par ecrit, et la graine n'est pas changee.

7. LA TABLE DE MACHINE 1 (560 cellules)
  Par cellule : l'etendue de la chaine d'ordre 3 sous l'absorbeur adapte, dans l'ordre des sept
  kappa. Les trois nombres ecrits de chaque cellule sont dans la table JSON
  (eligibilite_candidates_sommet_v1.json, 77ce2a6c7e867011).
  creneau MP : 15 w2 eligibles sur 15
    1.99980  0.0034 0.0019 0.0019 0.0027 0.0012 0.0011 0.0029  ELIGIBLE
    1.99981  0.0034 0.0019 0.0019 0.0027 0.0011 0.0011 0.0028  ELIGIBLE
    1.99982  0.0034 0.0019 0.0019 0.0027 0.0010 0.0010 0.0027  ELIGIBLE
    1.99983  0.0034 0.0019 0.0019 0.0026 0.0009 0.0009 0.0025  ELIGIBLE
    1.99984  0.0034 0.0020 0.0019 0.0026 0.0008 0.0009 0.0023  ELIGIBLE
    1.99985  0.0034 0.0020 0.0018 0.0026 0.0007 0.0010 0.0025  ELIGIBLE
    1.99986  0.0034 0.0020 0.0018 0.0025 0.0006 0.0011 0.0027  ELIGIBLE
    1.99987  0.0034 0.0020 0.0018 0.0025 0.0005 0.0012 0.0029  ELIGIBLE
    1.99988  0.0034 0.0020 0.0018 0.0024 0.0004 0.0013 0.0030  ELIGIBLE
    1.99989  0.0034 0.0021 0.0018 0.0024 0.0003 0.0015 0.0030  ELIGIBLE
    1.99991  0.0034 0.0021 0.0017 0.0023 0.0003 0.0017 0.0030  ELIGIBLE
    1.99992  0.0034 0.0021 0.0017 0.0023 0.0003 0.0018 0.0031  ELIGIBLE
    1.99993  0.0034 0.0021 0.0017 0.0022 0.0003 0.0019 0.0032  ELIGIBLE
    1.99994  0.0034 0.0021 0.0016 0.0022 0.0004 0.0020 0.0032  ELIGIBLE
    1.99995  0.0034 0.0022 0.0016 0.0022 0.0005 0.0021 0.0031  ELIGIBLE
  creneau PP : 15 w2 eligibles sur 15
    2.00005  0.0033 0.0023 0.0014 0.0018 0.0014 0.0032 0.0010  ELIGIBLE
    2.00006  0.0033 0.0024 0.0014 0.0018 0.0015 0.0032 0.0015  ELIGIBLE
    2.00007  0.0033 0.0024 0.0014 0.0018 0.0016 0.0033 0.0020  ELIGIBLE
    2.00008  0.0033 0.0024 0.0014 0.0018 0.0017 0.0033 0.0024  ELIGIBLE
    2.00009  0.0033 0.0024 0.0013 0.0017 0.0018 0.0033 0.0027  ELIGIBLE
    2.00011  0.0033 0.0024 0.0013 0.0017 0.0019 0.0032 0.0031  ELIGIBLE
    2.00012  0.0033 0.0024 0.0013 0.0016 0.0020 0.0032 0.0032  ELIGIBLE
    2.00013  0.0033 0.0025 0.0012 0.0016 0.0021 0.0031 0.0031  ELIGIBLE
    2.00014  0.0033 0.0025 0.0012 0.0016 0.0022 0.0031 0.0030  ELIGIBLE
    2.00015  0.0032 0.0025 0.0012 0.0015 0.0022 0.0031 0.0031  ELIGIBLE
    2.00016  0.0032 0.0025 0.0012 0.0015 0.0023 0.0030 0.0030  ELIGIBLE
    2.00017  0.0032 0.0025 0.0012 0.0015 0.0024 0.0030 0.0029  ELIGIBLE
    2.00018  0.0032 0.0025 0.0011 0.0014 0.0024 0.0030 0.0029  ELIGIBLE
    2.00019  0.0032 0.0025 0.0011 0.0014 0.0025 0.0029 0.0029  ELIGIBLE
    2.00020  0.0032 0.0026 0.0011 0.0014 0.0026 0.0029 0.0029  ELIGIBLE
  creneau MG : 25 w2 eligibles sur 25
    1.99951  0.0035 0.0013 0.0028 0.0031 0.0028 0.0028 0.0018  ELIGIBLE
    1.99952  0.0035 0.0013 0.0027 0.0031 0.0028 0.0029 0.0017  ELIGIBLE
    1.99953  0.0035 0.0013 0.0027 0.0031 0.0027 0.0029 0.0019  ELIGIBLE
    1.99954  0.0035 0.0013 0.0027 0.0031 0.0027 0.0029 0.0021  ELIGIBLE
    1.99955  0.0035 0.0013 0.0027 0.0031 0.0027 0.0029 0.0022  ELIGIBLE
    1.99956  0.0035 0.0013 0.0026 0.0031 0.0027 0.0029 0.0024  ELIGIBLE
    1.99957  0.0035 0.0014 0.0026 0.0031 0.0026 0.0029 0.0029  ELIGIBLE
    1.99958  0.0035 0.0014 0.0026 0.0031 0.0026 0.0029 0.0032  ELIGIBLE
    1.99959  0.0035 0.0014 0.0025 0.0031 0.0026 0.0029 0.0035  ELIGIBLE
    1.99960  0.0035 0.0014 0.0025 0.0031 0.0025 0.0030 0.0036  ELIGIBLE
    1.99961  0.0035 0.0015 0.0025 0.0031 0.0025 0.0030 0.0037  ELIGIBLE
    1.99962  0.0035 0.0015 0.0025 0.0031 0.0024 0.0030 0.0037  ELIGIBLE
    1.99963  0.0035 0.0015 0.0024 0.0031 0.0024 0.0029 0.0035  ELIGIBLE
    1.99964  0.0035 0.0015 0.0024 0.0031 0.0023 0.0029 0.0033  ELIGIBLE
    1.99965  0.0035 0.0015 0.0024 0.0031 0.0023 0.0028 0.0029  ELIGIBLE
    1.99966  0.0035 0.0016 0.0023 0.0031 0.0022 0.0028 0.0025  ELIGIBLE
    1.99967  0.0035 0.0016 0.0023 0.0030 0.0021 0.0027 0.0022  ELIGIBLE
    1.99968  0.0034 0.0016 0.0023 0.0030 0.0021 0.0026 0.0023  ELIGIBLE
    1.99969  0.0034 0.0016 0.0022 0.0030 0.0020 0.0025 0.0025  ELIGIBLE
    1.99970  0.0034 0.0017 0.0022 0.0030 0.0019 0.0024 0.0025  ELIGIBLE
    1.99971  0.0034 0.0017 0.0022 0.0030 0.0019 0.0023 0.0026  ELIGIBLE
    1.99972  0.0034 0.0017 0.0021 0.0029 0.0018 0.0022 0.0025  ELIGIBLE
    1.99973  0.0034 0.0017 0.0021 0.0029 0.0017 0.0021 0.0024  ELIGIBLE
    1.99974  0.0034 0.0017 0.0021 0.0029 0.0017 0.0019 0.0026  ELIGIBLE
    1.99975  0.0034 0.0018 0.0021 0.0029 0.0016 0.0018 0.0027  ELIGIBLE
  creneau PG : 25 w2 eligibles sur 25
    2.00025  0.0032 0.0026 0.0010 0.0012 0.0028 0.0026 0.0034  ELIGIBLE
    2.00026  0.0032 0.0026 0.0010 0.0012 0.0029 0.0026 0.0035  ELIGIBLE
    2.00027  0.0032 0.0026 0.0010 0.0011 0.0029 0.0025 0.0036  ELIGIBLE
    2.00028  0.0032 0.0027 0.0010 0.0011 0.0029 0.0024 0.0035  ELIGIBLE
    2.00029  0.0032 0.0027 0.0010 0.0011 0.0030 0.0023 0.0033  ELIGIBLE
    2.00030  0.0032 0.0027 0.0010 0.0010 0.0030 0.0023 0.0030  ELIGIBLE
    2.00031  0.0032 0.0027 0.0010 0.0010 0.0030 0.0022 0.0027  ELIGIBLE
    2.00032  0.0031 0.0027 0.0010 0.0009 0.0031 0.0021 0.0023  ELIGIBLE
    2.00033  0.0031 0.0027 0.0010 0.0009 0.0031 0.0020 0.0021  ELIGIBLE
    2.00034  0.0031 0.0027 0.0010 0.0009 0.0031 0.0021 0.0022  ELIGIBLE
    2.00035  0.0031 0.0027 0.0010 0.0009 0.0031 0.0022 0.0023  ELIGIBLE
    2.00036  0.0031 0.0027 0.0011 0.0010 0.0031 0.0023 0.0023  ELIGIBLE
    2.00037  0.0031 0.0027 0.0011 0.0010 0.0031 0.0023 0.0022  ELIGIBLE
    2.00038  0.0031 0.0027 0.0011 0.0010 0.0031 0.0024 0.0021  ELIGIBLE
    2.00039  0.0031 0.0028 0.0012 0.0010 0.0031 0.0024 0.0021  ELIGIBLE
    2.00040  0.0031 0.0028 0.0012 0.0011 0.0031 0.0025 0.0023  ELIGIBLE
    2.00041  0.0031 0.0028 0.0012 0.0011 0.0031 0.0025 0.0027  ELIGIBLE
    2.00042  0.0031 0.0028 0.0012 0.0011 0.0031 0.0026 0.0030  ELIGIBLE
    2.00043  0.0031 0.0028 0.0013 0.0011 0.0031 0.0026 0.0033  ELIGIBLE
    2.00044  0.0031 0.0028 0.0013 0.0011 0.0031 0.0026 0.0035  ELIGIBLE
    2.00045  0.0031 0.0028 0.0013 0.0011 0.0031 0.0026 0.0035  ELIGIBLE
    2.00046  0.0030 0.0028 0.0014 0.0012 0.0031 0.0026 0.0034  ELIGIBLE
    2.00047  0.0030 0.0028 0.0014 0.0012 0.0030 0.0025 0.0033  ELIGIBLE
    2.00048  0.0030 0.0028 0.0014 0.0012 0.0030 0.0026 0.0030  ELIGIBLE
    2.00049  0.0030 0.0028 0.0015 0.0013 0.0030 0.0027 0.0026  ELIGIBLE
  Un point d'exclamation marquerait une cellule ineligible : il y en a 0. Par kappa, sur les 80 w2
  (les intervalles vont du plus petit au plus grand) :
    kappa    cible  barreaux  r_c  boite  etendue  e_bord  poids du  premier site ou
                    trouves        max    max      max     site 0    le saut depasse 1
    0.0363   2      2         22   122    0.0035   0.001   0.9985    63 a 159
    0.0530   1      1         20   120    0.0028   0.000   0.9961    55 a 136
    0.0800   0      0         18   118    0.0028   0.000   0.9881    46 a 116
    0.1300   0      0         18   118    0.0031   0.000   0.9656    38 a 95
    0.2000   0      0         18   118    0.0031   0.000   0.9405    32 a 80
    0.4000   0      0         18   118    0.0033   0.000   0.9129    24 a 61
    1.0000   0      0         18   118    0.0037   0.000   0.9013    17 a 42
    kappa    couplage ecrit g             plateau predit G3*           G3* / g
    0.0363   1.77800e-05 a 1.74597e-04    3.34172e-10 a 3.27493e-09    1.8757e-05 a 1.8825e-05
    0.0530   2.59597e-05 a 2.54921e-04    8.97814e-09 a 8.80033e-08    3.4510e-04 a 3.4649e-04
    0.0800   3.91845e-05 a 3.84786e-04    1.19792e-07 a 1.17421e-06    3.0501e-03 a 3.0628e-03
    0.1300   6.36748e-05 a 6.25278e-04    8.97078e-07 a 8.79299e-06    1.4059e-02 a 1.4114e-02
    0.2000   9.79612e-05 a 9.61966e-04    2.78850e-06 a 2.73321e-05    2.8405e-02 a 2.8517e-02
    0.4000   1.95922e-04 a 1.92393e-03    8.89750e-06 a 8.72079e-05    4.5314e-02 a 4.5495e-02
    1.0000   4.89806e-04 a 4.80983e-03    2.58685e-05 a 2.53553e-04    5.2696e-02 a 5.2910e-02
    kappa    Phi = G3* / |w2 - 2|                 etalement    plus grand      plus grand
                                                  de ln Phi    |ln(G3 / G1)|   |ln(G3 / G2)|
    0.0363   6.68321e-06 a 6.68373e-06           0.0001       0.00010         0.00000
    0.0530   1.79539e-04 a 1.79599e-04           0.0003       0.00024         0.00000
    0.0800   2.39514e-03 a 2.39636e-03           0.0005       0.00034         0.00000
    0.1300   1.79407e-02 a 1.79449e-02           0.0002       0.00018         0.00000
    0.2000   5.57649e-02 a 5.57803e-02           0.0003       0.00017         0.00001
    0.4000   1.77922e-01 a 1.77975e-01           0.0003       0.00017         0.00001
    1.0000   5.17263e-01 a 5.17455e-01           0.0004       0.00019         0.00006
  La plus grande etendue est 0.0037 pour un seuil de 0.005 : l'eligibilite ne trie rien ici, et le
  tirage est donc uniforme sur les candidats. La barriere du moteur est vide a 400 cellules (les
  cinq kappa sans barriere) ; le nombre de cellules ou elle n'a pas la profondeur cible est 0. Le
  plus petit poids du site 0 dans l'etat lu est 0.9013. Toutes les largeurs sont lues par le flux.
  Le second terme de eta0 l'emporte aux 560 cellules : eta0 / g va de 3.8883 a 3.9027, et eta0 / |w2
  - 2| de 1.385 a 38.17. La plus grande boite du lecteur serait N = r_c + 100 = 122, deja jouee a un
  point de Q2.
  G1 et G2 sont le premier ordre et l'ordre 2 de la meme chaine, sous les memes dix-huit variantes.
  L'ordre 3 differe du premier ordre de 0.00034 au plus en logarithme, et de l'ordre 2 de 0.00006 au
  plus : aucun enonce pose sur ces cellules n'opposera les ordres. A kappa egal, Phi varie de 0.0005
  au plus d'un w2 a l'autre : c'est la loi d'echelle, dans la chaine. Le signe de delta, a kappa et
  |w2 - 2| egaux (280 paires) : ln[Phi(delta < 0) / Phi(delta > 0)] va de -0.00007 a +0.00051, sous
  l'etendue de la chaine.
  Ce que le lecteur n'a jamais lu au sommet : a 50 cellules la largeur predite depasse le plus grand
  plateau qualifie (1.08861e-04, point Q-d), jusqu'a 2.33 fois, et les couplages vont jusqu'a
  4.80983e-03 pour 2e-03 a Q-d ; a 42 cellules elle est sous le plus petit plateau qualifie au
  sommet (2.05518e-09, point Q2-b), jusqu'a 0.163 fois. Aux ailes, le delta 102 a qualifie des
  plateaux plus petits encore.
  Le meme calcul sous l'autre reglage de numpy de machine 1 (avec le levier
  NPY_DISABLE_CPU_FEATURES=X86_V4) : 0 eligibilite changee, 0 nombre ecrit change, plus grand ecart
  sur ln G3 0.0e+00.

8. CE QUE LES NEUF POINTS SACRIFIES ONT MONTRE, ET CE QU'ILS NE MONTRENT PAS
  Machine 2 a lu le vide en 2D, par le lecteur creux du depot sous la regle de eta0 de la section 2,
  a neuf points declares sacrifies avant toute lecture ; machine 1 avait ecrit ses attendus et sa
  colonne G3* avant. Les plateaux sont ceux de la feuille deposee (83701094e6a2b965), relus par
  machine 1 dans les sorties de machine 2 :
    point  w2           g        kappa    barreaux  plateau lu   ln(plateau lu / G3*)
    Q-a    2            2.5e-04  infini   0         1.36078e-05  +0.00002
    Q-c    2            1e-03    infini   0         5.44311e-05  +0.00000
    Q-d    2            2e-03    infini   0         1.08861e-04  -0.00000
    Q-e    20001/10000  3e-04    0.3061   0         1.20926e-05  +0.00002
    Q-f    20001/10000  1.5e-04  0.1530   0         2.91446e-06  -0.00008
    Q2-a   20001/10000  6e-05    0.0612   1         4.94717e-08  +0.00019
    Q2-b   20001/10000  4e-05    0.0408   2         2.05518e-09  +0.00034
    Q2-c   19999/10000  3e-04    0.3063   0         1.21073e-05  +0.00002
    Q2-d   19999/10000  1.5e-04  0.1532   0         2.92063e-06  -0.00008
  Ce qu'ils montrent : aux neuf points le lecteur est qualifie par la feuille deposee telle quelle,
  son plateau est a 0.00034 au plus de la colonne G3* en logarithme, il est plat sur huit barreaux
  sous l'absorbeur A, et le jumeau sans fantome tient. Le signe de delta, lu a couplage egal (Q2-c
  contre Q-e, Q2-d contre Q-f), vaut +0.00121 et +0.00212 pour +0.00121 et +0.00211 dans la chaine.
  Ce qu'ils ne montrent pas. (i) AUCUN des sept kappa du gel n'est lu : les points sont a kappa
  infini (trois points), 0.306 (deux points), 0.153 (deux points), 0.0612 et 0.0408 ; chaque kappa
  du gel est encadre par deux kappa lus, 0.0363 l'etant par 0.0408 et par les cellules de trois
  barreaux du delta 102 (0.0262, lues sous la regle du depot). (ii) Un seul desaccord non nul est lu
  au sommet, |w2 - 2| = 0.0001 ; les candidats vont de 0.00005 a 0.00049. (iii) Les profondeurs 1 et
  2 ne sont lues qu'a un point chacune. (iv) Le lecteur et la chaine se recoupent : cela ne dit pas
  que la chaine est la verite du modele complet, et une erreur commune au lecteur et a la chaine ne
  se verrait pas. (v) Les tolerances de Q et de Q2 etaient posees a la main.
  Cout, d'apres machine 2 : les dix lectures de Q ont pris 2 min 35 s sur BOCAL4. Le run compterait
  cent douze lectures (cinquante-six cellules, le fantome et le jumeau), dans des boites de N = 122
  au plus.

9. VIRGINITE
  Balayage de machine 1, par recherche de texte : la fraction irreductible de chaque w2 candidat ;
  son ecriture decimale apres "w2" ; dans les fichiers JSON, une cle "delta" qui designe un w2
  candidat ; son ecriture a cinq decimales, isolee.
    Au registre (055be58, 3553 fichiers lus) : aucune trace d'un w2 candidat. Les deux w2 RETIRES de
    la liste, 3999/2000 et 4001/2000, y sont dans 8 fichiers : la faisabilite "petit delta" de
    machine 2 du 16/11 (le JUMEAU sans fantome, en 2D, a des geometries de 8, 12 et 16 barreaux) et
    les pieces qui la citent. Ce n'est pas le systeme a fantome ; machine 1 les retire plutot que de
    le plaider.
    Sur le poste de machine 1, hors du dossier de ce gel dont les pieces portent les candidats par
    construction (972 fichiers lus) : 16 w2 candidats, dans un seul journal (2 copies),
    esquisse_gel_sommet_machine1_v1.log (lot 423ec0fd24240977) : ce sont des chaines a une
    dimension, les 112 cellules de la section 4.8. Aucun fichier touche n'a le nom d'une sortie 2D.
  Ce balayage ne voit que le poste de machine 1 tel qu'il est ce soir et son clone du registre, et
  une recherche de texte n'est pas une preuve d'absence : un journal qui ecrit un w2 sans le nommer
  lui echappe, sauf par la quatrieme forme. Machine 2 tient les archives des runs et fait le sien.

10. CE QUE MACHINE 2 CERTIFIE
  (a) que les definitions des sections 2 et 4, avec les blocs deposes, suffisent a calculer
      l'eligibilite et les trois nombres ecrits sans lire le code de machine 1 ;
  (b) SA table des 560 cellules, par sa chaine ; et la table commune qui en resulte ;
  (c) que son tirage, sur la graine de demonstration, rend les memes numeros que la section 3 et que
      le journal d'autotest ;
  (d) SON balayage de ses archives : aucun calcul 2D, du systeme a fantome ou du jumeau, a un w2
      candidat ;
  (e) qu'elle accepte, ou refuse, ce qui est neuf ici (section 13) : deux w2 par creneau, la grille
      au cent-millieme, le retrait de k = 50, eta0 et r_c ecrits des cette partie, le seuil de
      0.005, les dix rangs.

11. LA SUITE, DANS L'ORDRE
  (1) machine 2 certifie cette piece et rend sa table ; la table commune existe ;
  (2) l'operateur donne la graine aux deux machines ;
  (3) chaque machine tire ; les cellules sont les memes, ou PAS DE GEL ;
  (4) machine 1 ecrit la seconde partie : l'instrument (le lecteur creux du depot au site (0, 0),
      avec le eta0 et le r_c ecrits de chaque cellule ; sa feuille ; le bloc de l'absorbeur adapte
      comme predicteur ; les temoins : le jumeau sans fantome a chaque cellule, les ancres et le
      temoin positif du depot), la table gelee des cellules avec leurs predictions calculees sur les
      chaines seules, les enonces et leurs tolerances, ce que chaque issue engage, ce que vaut une
      cellule que le lecteur ne qualifie pas, et les annonces de la plume ;
  (5) machine 2 certifie la seconde partie ; l'operateur donne le feu vert par ecrit ; machine 2
      joue, une fois.

12. CE QUE LA SECONDE PARTIE PORTERA : ANNONCE ICI, NON GELE ICI
  - Un seul enonce juge : aux cellules lues, la chaine rend la largeur a T = 0.01 pres en
    logarithme ; la bande est l'etendue de la chaine plus l'etalement du lecteur ; les issues se
    comptent comme a l'enonce V1 du gel "largeur du vide", porte a cinquante-six cellules et huit
    w2.
  - Une lecture non suivie est NON LISIBLE ; une cellule dont l'absorbeur A n'a pas cinq barreaux
    lisibles consecutifs n'est pas lue. Aucune borne sur les couplages : une lecture qui echoue rend
    la cellule non lue, et se compte comme telle.
  - Consigne sans jugement : Phi a kappa egal d'un w2 a l'autre (la loi d'echelle) ; le signe de
    delta ; les ordres 1 et 2 ; la largeur rapportee au saut au pied de l'echelle ; par cellule, les
    barreaux plats sous A.
  - Ce que l'acte ne pourrait pas ecrire : rien de la duree de vie du systeme ferme ; rien de w2 = 2
    exactement ; rien au-dela de kappa = 1 ; rien qui oppose les ordres de la chaine ; et pas
    "cinquante-six cellules" sans dire "huit tirages".

13. CE QUE CETTE PIECE NE FAIT PAS, ET SES ECARTS A LA REGLE DU GEL "LARGEUR DU VIDE"
  - Elle ne tire rien et ne connait aucune graine.
  - Elle ne donne aucune tolerance : la section 12 annonce, elle ne gele pas.
  - Ecart 1 : la cellule est un couple (w2, kappa) de profondeur cible 0, 1 ou 2, au lieu d'un
    couple (w2, profondeur) de trois barreaux et plus. La regle de la barriere vide (4.1) et
    M_facteur = 5 (4.2) sont neufs.
  - Ecart 2 : deux w2 par creneau au lieu d'un, distincts, en dix rangs au lieu de cinq.
  - Ecart 3 : il n'y a pas de cellules "profondes" : les sept cellules d'un w2 decident de son
    eligibilite.
  - Ecart 4 : eta0 et r_c sont des nombres ecrits de la cellule, fixes ici et compares dans la table
    commune ; eta0 n'est plus |w2 - 2| seul.
  - Ecart 5 : le seuil d'etendue est 0.005 au lieu de 0.02.
  - Ecart 6 : les candidats sont au cent-millieme, et l'ordre des creneaux est MP, PP, MG, PG.
  - Les bornes des creneaux, les kappa et l'ordre des creneaux sont de la plume de machine 1.
  - La definition du hamiltonien effectif est celle des blocs deposes (forme symetrique) ; aucune
    autre n'est essayee.

14. PIECES DE CE LOT (convention B)
    7507b79768462046  eligibilite_sommet_machine1_v1.py
    da16444bbfe364fe  eligibilite_sommet_v1.log
    882f55d07d03dfff  eligibilite_sommet_v1.json
    1d0330afd2d6972c  eligibilite_sommet_avec_levier_v1.log
    882f55d07d03dfff  eligibilite_sommet_avec_levier_v1.json
    c08fcb713f18cda7  lecture_eligibilite_sommet_machine1_v1.py
    8f85dcae9266bdb7  lecture_eligibilite_sommet_machine1_v1.log
    77ce2a6c7e867011  eligibilite_candidates_sommet_v1.json
    816ac4d298e82f16  tirage_sommet_machine1_v1.py
    0c01f02c56c0e1a8  tirage_sommet_machine1_v1_autotest.log
    14e0298da1846a7d  tirage_sommet_machine1_v1_demonstration.log
    d7f860abd43fe300  balayage_virginite_sommet_machine1_v1.py
    576bac34d44b1850  balayage_virginite_sommet_registre_v1.log
    ecb489c4196860c4  balayage_virginite_sommet_registre_v1.json
    4e63568689af888c  balayage_virginite_sommet_poste_v1.log
    af1d66cca9262952  balayage_virginite_sommet_poste_v1.json
    8ff0619842f3abc4  note_Q2_machine1_v1.py
    06e7093ce627bd0f  note_Q2_machine1_v1.log
    (ce script)       construction_regle_tirage_sommet_machine1_v1.py
  Le lot porte aussi le controle de cette piece contre ces sorties, sa note d'envoi et leurs
  journaux, ecrits apres elle : le manifeste du lot fait foi.
