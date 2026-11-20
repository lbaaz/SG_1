GEL "PONT" -- PREMIERE PARTIE : LA REGLE DE TIRAGE ET D'ELIGIBILITE DES CELLULES
PRE-ENREGISTREMENT v1 -- machine 1, 2026-11-17.
A CERTIFIER PAR MACHINE 2 AVANT QUE L'OPERATEUR DONNE LA GRAINE.

0. STATUT
  Cette piece fixe COMMENT les cellules du gel seront tirees et QUAND un tirage est admis. Elle ne
  fixe ni les enonces juges, ni les tolerances, ni les probabilites, ni l'instrument : c'est la
  seconde partie, ecrite apres le tirage sur les chaines seules, et certifiee avant tout run.
  L'objet du gel, "le pont" : la largeur que le lecteur lit sous absorbeur est-elle la force de
  couplage du vide (l'etat que porte le site (0, 0) du systeme a fantome) au spectre REEL de la
  boite fermee ? Trois appuis ont ete vus, hors chaine, a un seul point, w2 = 101/50, qui est
  sacrifie : (L) loin de l'energie du vide, la densite du vide dans le systeme 2D sous absorbeur est
  celle de la chaine d'ordre 3 ; (S) dans la boite 2D fermee, les parts des niveaux se somment a la
  largeur de la fenetre ; (C) le nombre de niveaux qui portent cette force croit avec le cote de la
  boite. Ce gel les eprouve a des points que personne n'a choisis ni joues.
  Ouverture, selon machine 1 : a la fin de la note du 17/11 (f841cec8c053695d, hors chaine, classe
  3), machine 1 a propose de geler le pont sur un point neuf ; l'operateur a ecrit "Go rediger le
  gel." (17/11/2026, 00 h 56). A l'operateur de l'attester ou de le dementir.
  E19. Selon ses pieces (section 9), machine 1 n'a joue aucune 2D du systeme a fantome a un w2
  candidat de ce gel : ni boite fermee, ni densite sous absorbeur hors de l'energie du vide, ni
  largeur. Les 2D du pont qu'elle a jouees ou lues sont toutes a w2 = 101/50, un centieme : des
  boites fermees jusqu'au cote 201 et des croisements (sa note v3 du pont, 16/11, dans un autre
  conteneur), les niveaux des boites de machine 2 jusqu'au cote 402 (lot dce7431e7a8b4a8c), et des
  densites sous absorbeur de 0.05 a 8 |delta| du vide (note f841cec8c053695d). Le gel "largeur du
  vide" a fait jouer le lecteur creux, a l'energie du vide, a w2 = 1.982, 1.997, 2.005 et 2.017
  (acte 16ba5e594ab18717) : les deux qui tombent dans les creneaux de ce gel sont retires des
  candidats. Aucune des deux machines ne jouera une 2D du systeme a fantome, de quelque sorte, a un
  w2 candidat avant la certification croisee de la seconde partie et le feu vert ecrit de
  l'operateur. Machine 2 dit ce qu'il en est pour elle (section 10, d). Tout ce que cette piece
  calcule est une chaine a une dimension.

1. SOURCES (convention B)
    82a0be882568fe0c scripts/m17_chaine_v17.py (registre 2988237), le moteur
    7cd5977bc27bebc1 scripts/chaine_ordre2_bloc_machine1_v1.py (registre), le bloc d'ordre 2
    534ba246aa3b8973 scripts/ordre3_bloc_machine1_v1.py (registre), le bloc d'ordre 3
    49a40d9098b55361 scripts/chaine_adaptee_bloc_machine1_v1.py (registre), l'absorbeur adapte
    d5cc48f48e37af99 scripts/sonde_lecteur_gel_loi_machine1_v1.py (registre), le lecteur creux ; non
                      lu ici
    b57c9ccdd3946261 gels/gel_largeur_vide_partie1_regle_tirage_pre_enregistrement_v1.md (registre)
                      : la regle dont celle-ci reprend la forme, les kappa_m et le couplage ecrit
    34eb68229983b1f2 scripts/eligibilite_vide_machine1_v1.py (registre), dont l'eligibilite de ce
                      lot derive
    cc1b2df637a9f3cd scripts/tirage_vide_machine1_v1.py (registre), dont le tirage de ce lot derive
    16ba5e594ab18717 journal/journal_delta_102_largeur_vide_v2.md (registre) : les w2 que le gel du
                      vide a joues
    dce7431e7a8b4a8c lot de machine 2 lot_machine2_2026-11-17_grandes_boites_resultats_v1, HORS
                      REGISTRE : les boites fermees des cotes 190 a 402 au point sacrifie ; sa note
                      : b9dd39f6c4ffa922
    ffed1c621093dae6 note_machine1_pont_lecture_grandes_boites_2026-11-17_v1.md, HORS REGISTRE :
                      lecture de ces boites
    f841cec8c053695d note_machine1_pont_lisse_hors_vide_2026-11-17_v1.md, HORS REGISTRE : la chaine
                      d'ordre 3 contre la 2D ouverte, loin de l'energie du vide ; son attendu
                      5bb45d0c8081106f et son rectificatif c0dc8b2732ba7065
  Les deux notes de machine 1 et leurs pieces voyagent avec ce lot. La note v3 du pont et les
  attendus des grandes boites (lot 4e15e302d97e26b8, que la note du lot de machine 2 dit avoir
  authentifie) sont detenus par machine 2 et sont au projet de l'operateur ; ce conteneur de machine
  1 ne les detient pas en fichiers et leurs canons ne sont pas recalcules ici.

2. LES CRENEAUX ET LES CELLULES
  Deux creneaux, huit w2 candidats chacun. Les w2 candidats sont au millieme ; les centiemes en sont
  exclus ; 0.01 < |w2 - 2| < 0.02 ; et les deux w2 que le gel du vide a joues (1.982 et 2.017) en
  sont retires.
    MG, delta < 0 : w2 = 1.981, 1.983, 1.984, 1.985, 1.986, 1.987, 1.988, 1.989
    PG, delta > 0 : w2 = 2.011, 2.012, 2.013, 2.014, 2.015, 2.016, 2.018, 2.019
  Trois PROFONDEURS de barriere m, chacune avec son rapport kappa_m, repris tels quels du gel du
  vide :
    m = 3 : 0.0262 ; m = 4 : 0.0200 ; m = 5 : 0.0159
  Une CELLULE est un couple (w2, m). Son couplage est
        g = kappa_m x |w2 - 2| x P / X(w2) ,
        X(w2) = X_saut_reel(P, 2, 1, 0, 0, w2) du moteur, P = 5,
  calcule en double precision puis ARRONDI a six chiffres significatifs (le format "%.5e" de Python)
  : le couplage de la cellule EST le nombre decimal ainsi ecrit. C'est la regle du gel du vide. Au
  point sacrifie, w2 = 101/50 et m = 3, elle rend le couplage de l'exploration, 5.53067e-03.
  Un tirage donne un w2 par creneau, donc six cellules, nommees par le creneau et la profondeur :
  MG3, MG4, MG5, PG3, PG4, PG5.

3. LE TIRAGE
  Le w2 du creneau s au rang r est l'element de numero
        int( sha256("<graine>|<s>|<r>") ecrit en hexadecimal, 16 )  modulo  n_s
  de la liste CROISSANTE des n_s w2 candidats du creneau, numerotee a partir de 0. La chaine hachee
  est codee en ASCII ; s vaut MG ou PG ; r s'ecrit en decimal, sans zero devant ; la barre verticale
  est le caractere 124. C'est le hachage des deux gels deposes.
  LA GRAINE est une suite de chiffres (0 a 9), d'au moins six chiffres, donnee par L'OPERATEUR, par
  ecrit, aux deux machines, APRES la certification de cette piece et apres que la table commune de
  la section 5 existe. Elle est reportee telle quelle, zeros de tete compris, dans la seconde
  partie. Ni machine 1 ni machine 2 ne la choisit, ne la propose, ni ne la commente avant de l'avoir
  recue.
  Chaque machine tire par SON code. Exemple de controle, sur une graine de demonstration qui n'est
  pas une suite de chiffres et ne peut donc pas etre la graine :
    sha256("DEMONSTRATION|MG|0") = 8254e7d473dd8e66... ; modulo  8 =  5 -> w2 = 1.987
    sha256("DEMONSTRATION|MG|1") = 3bcf50fd02de7108... ; modulo  8 =  4 -> w2 = 1.986
    sha256("DEMONSTRATION|PG|0") = c67ae8de8fe0b645... ; modulo  8 =  7 -> w2 = 2.019
    sha256("DEMONSTRATION|PG|1") = a72d87914f9453df... ; modulo  8 =  7 -> w2 = 2.019

4. L'ELIGIBILITE D'UNE CELLULE (chaine seule, aucune 2D)
  4.1 La barriere : sites = barriere(0, 0, w2, g, avec Sigma2) du moteur ; m_bord = son dernier site
      ; e_bord = |m_bord delta + Sigma2(m_bord) - Sigma2(0)|, avec delta = w2 - 2.
  4.2 Les tables : tables_ordre2(0, 0, w2, g, sites, M_facteur 4) puis tables_ordre3, des blocs
      deposes : par site m de l'echelle, le decalage S_m, le saut t_m, le saut au second voisin U_m,
      et a l'ordre 3 la correction T3_m et les sauts W3_m et W5_m.
  4.3 La chaine sous ABSORBEUR ADAPTE, variante (a, c, L), est la matrice du bloc depose
      (matrice_adaptee) : sur la diagonale, m delta + S_m - S_0 - i W_m ; hors diagonale, t_m + T3_m
      entre m et m + 1, U_m entre m et m + 2, W3_m entre m et m + 3, W5_m entre m et m + 5 ; W_m = a
      |t_m| ((m - debut) / L)^2 pour debut < m <= debut + L, 0 ailleurs, debut = m_bord + c.
      Dix-huit variantes : a = 1, 2, 4 ; c = 6, 8, 10 ; L = 16, 24. La chaine d'ORDRE 2 est la meme
      matrice avec T3, W3 et W5 nuls.
  4.4 Au vide. Largeur d'une variante : Gamma = -2 Im(E), E etant la valeur propre de la matrice
      d'ordre 3 dont le vecteur propre, norme, porte le plus grand poids sur le site 0 (a poids
      egal, la plus petite partie reelle). PLATEAU G3* : exponentielle de la mediane des dix-huit ln
      Gamma (moyenne des deux valeurs centrales) ; ETENDUE : le plus grand moins le plus petit.
      C'est la regle du gel du vide.
  4.5 Hors du vide. Douze ECARTS x, en unites de |delta| : 0.05, 0.25, 0.5, 1, 1.5, 2, 3, 4, 5, 6,
      7, 8. A l'ecart x, pour une variante et un ordre o (2 ou 3) : E_v est la partie reelle de la
      valeur propre du 4.4 prise sur la matrice d'ordre o ; E = E_v - x delta, c'est-a-dire du cote
      OPPOSE au desaccord (sous le vide si delta > 0, au-dessus si delta < 0) ; la DENSITE du site 0
      est
          rho = -(1 / pi) Im [ (E - H)^(-1) ]_00 ,
      H etant la matrice et l'indice 0 le site 0. C'est une propriete de la matrice : chaque machine
      la calcule par sa methode ; machine 1 la lit par le flux, (1 / pi) somme_m W_m |y_m|^2 avec y
      = (E - H)^(-1) e_0, qui lui est egal. Le LISSE rho_o(x) est l'exponentielle de la mediane des
      dix-huit ln rho ; son ETENDUE est le plus grand moins le plus petit des dix-huit ln rho. Le
      PAS de l'ordre 2 a l'ordre 3 est ln rho_2(x) - ln rho_3(x).
  4.6 La cellule (w2, m) est ELIGIBLE si : (i) m_bord = m ; (ii) e_bord < 0.7 ; (iii) les dix-huit
      largeurs au vide sont strictement positives et leur etendue est <= 0.02 ; (iv) a chacun des
      douze ecarts, les dix-huit densites d'ordre 3 sont strictement positives et l'etendue du lisse
      est <= 0.03 ; (v) a chacun des douze ecarts, le pas de l'ordre 2 a l'ordre 3 est, en valeur
      absolue, <= 0.10.
  4.7 Un w2 candidat est ELIGIBLE si ses trois cellules le sont.
  4.8 D'ou viennent les nombres. (i), (ii), (iii), les kappa_m et les dix-huit variantes sont ceux
      du gel du vide. Les douze ecarts sont ceux de l'exploration du 17/11. Les seuils 0.03 et 0.10
      sont poses ici, APRES cette exploration, qui a vu au point sacrifie (3 barreaux) une etendue
      du lisse de 0.0106 au plus et un pas de 0.0450 au plus, et AVANT d'avoir calcule une seule
      cellule candidate sous cette regle. La condition (v) borne le domaine a la region ou la serie
      de la chaine avance a petits pas loin de l'energie du vide ; ce n'est pas une mesure de
      l'erreur de l'ordre 3. Aucun de ces nombres ne sera regle ensuite : ils ne l'ont pas ete quand
      la condition (v) a ecarte des cellules (section 7).

5. LA TABLE COMMUNE, AVANT LA GRAINE
  Chaque machine calcule par SA chaine l'eligibilite des 48 cellules candidates (16 w2) AVANT que la
  graine existe. La table de machine 1 est en section 7. Machine 2 rend la sienne avec sa
  certification. LA TABLE COMMUNE est leur ET : un w2 candidat y est eligible si et seulement s'il
  l'est dans les deux tables ET si les couplages ecrits de ses trois cellules sont les memes dans
  les deux. Elle ne depend d'aucune graine. Un desaccord entre les deux tables est dit dans la
  certification ; il n'arrete pas le gel.
  Format d'une table : JSON, creneaux -> <nom du creneau> -> candidats -> liste de {"w2": "<fraction
  irreductible>", "eligible": true ou false, "cellules": liste de {"m": <entier>, "g": "<le decimal
  a six chiffres>", "eligible": true ou false}}.

6. LA REGLE DES RANGS
  Pour chaque creneau, dans l'ordre MG puis PG et independamment : rang 0 ; si le w2 tire n'est pas
  eligible dans la table commune, rang 1, et ainsi de suite, pour le CRENEAU ENTIER (jamais cellule
  par cellule). Au plus cinq rangs, de 0 a 4. Si un creneau n'a pas de w2 eligible en cinq rangs :
  PAS DE GEL, et on le dit. Un meme w2 peut sortir a deux rangs ; il n'est pas retire de la liste.
  Si les deux machines ne tirent pas les memes cellules, avec les memes couplages ecrits, a partir
  de la meme graine et de la meme table commune : PAS DE GEL tant que l'ecart n'est pas explique par
  ecrit, et la graine n'est pas changee.

7. LA TABLE DE MACHINE 1 (48 cellules)
  Par cellule, dans l'ordre : l'etendue au vide, la plus grande etendue du lisse d'ordre 3 sur les
  douze ecarts, le plus grand pas de l'ordre 2 a l'ordre 3 en valeur absolue ; un point
  d'exclamation marque une cellule ineligible. Les couplages ecrits sont dans la table JSON
  (eligibilite_pont_MG_PG_v1.json, d03c9ca093ea5bfc).
  creneau MG : 5 w2 eligibles sur 8
  1.981  m3 0.0018 0.0048 0.1224!  m4 0.0014 0.0067 0.1388!  m5 0.0023 0.0105 0.1581!  INELIGIBLE
  1.983  m3 0.0014 0.0044 0.0932  m4 0.0014 0.0070 0.1051!  m5 0.0027 0.0107 0.1190!  INELIGIBLE
  1.984  m3 0.0014 0.0045 0.0804  m4 0.0014 0.0072 0.0906  m5 0.0027 0.0109 0.1021!  INELIGIBLE
  1.985  m3 0.0014 0.0046 0.0690  m4 0.0015 0.0074 0.0774  m5 0.0026 0.0110 0.0869  ELIGIBLE
  1.986  m3 0.0017 0.0047 0.0584  m4 0.0020 0.0076 0.0654  m5 0.0028 0.0111 0.0734  ELIGIBLE
  1.987  m3 0.0020 0.0049 0.0490  m4 0.0026 0.0077 0.0549  m5 0.0027 0.0112 0.0613  ELIGIBLE
  1.988  m3 0.0022 0.0050 0.0407  m4 0.0030 0.0079 0.0454  m5 0.0023 0.0116 0.0505  ELIGIBLE
  1.989  m3 0.0025 0.0051 0.0334  m4 0.0032 0.0081 0.0371  m5 0.0017 0.0119 0.0411  ELIGIBLE
  creneau PG : 8 w2 eligibles sur 8
  2.011  m3 0.0046 0.0091 0.0180  m4 0.0033 0.0133 0.0185  m5 0.0044 0.0188 0.0183  ELIGIBLE
  2.012  m3 0.0043 0.0090 0.0207  m4 0.0032 0.0135 0.0214  m5 0.0045 0.0192 0.0209  ELIGIBLE
  2.013  m3 0.0033 0.0092 0.0237  m4 0.0037 0.0139 0.0242  m5 0.0047 0.0196 0.0235  ELIGIBLE
  2.014  m3 0.0029 0.0094 0.0267  m4 0.0039 0.0143 0.0271  m5 0.0050 0.0200 0.0261  ELIGIBLE
  2.015  m3 0.0037 0.0097 0.0297  m4 0.0040 0.0148 0.0300  m5 0.0061 0.0204 0.0287  ELIGIBLE
  2.016  m3 0.0045 0.0099 0.0327  m4 0.0053 0.0153 0.0330  m5 0.0066 0.0208 0.0313  ELIGIBLE
  2.018  m3 0.0057 0.0103 0.0392  m4 0.0066 0.0162 0.0390  m5 0.0068 0.0216 0.0362  ELIGIBLE
  2.019  m3 0.0050 0.0105 0.0421  m4 0.0060 0.0167 0.0418  m5 0.0063 0.0219 0.0384  ELIGIBLE
  Par creneau et par profondeur, sur les huit w2 :
    creneau  m   e_bord   etendue   etendue    pas      plateau predit G3*    rho_3 |delta| a huit
                 max      au vide   du lisse   max      de ... a ...          |delta| : de ... a ...
    MG       3   0.057    0.0025    0.0051     0.1224   1.8e-09 a 3.1e-09    1e-18 a 2e-18
    MG       4   0.075    0.0032    0.0081     0.1388   4.0e-11 a 6.8e-11    4e-21 a 5e-21
    MG       5   0.094    0.0028    0.0119     0.1581   8.3e-13 a 1.4e-12    1e-23 a 2e-23
    PG       3   0.057    0.0057    0.0105     0.0421   1.8e-09 a 3.1e-09    2e-18 a 3e-18
    PG       4   0.077    0.0066    0.0167     0.0418   4.0e-11 a 6.9e-11    8e-21 a 9e-21
    PG       5   0.096    0.0068    0.0219     0.0384   8.4e-13 a 1.4e-12    3e-23 a 4e-23
  Les conditions (i) a (iv) n'ecartent aucune cellule. La condition (v) en ecarte 6, toutes dans le
  creneau MG : a |delta| et a profondeur egaux (21 paires), le plus grand pas de l'ordre 2 a l'ordre
  3 est de 1.9 a 4.1 fois plus grand du cote delta < 0. Restent eligibles 5 w2 sur 8 dans MG (1.985,
  1.986, 1.987, 1.988, 1.989) et 8 sur 8 dans PG. L'eligibilite trie donc ici, a la difference du
  gel du vide : le tirage n'est pas uniforme sur les candidats de MG, et le domaine du gel, du cote
  delta < 0, s'arrete a |delta| = 0.015. La probabilite qu'un creneau n'ait aucun w2 eligible en
  cinq rangs vaut 0.0074 pour MG et 0 pour PG, sous la table de machine 1.
  Le plus petit poids du site 0 dans l'etat lu est 0.9993. La derniere colonne donne l'echelle des
  plus petits poids qu'une boite fermee devra rendre a 8 |delta| du vide (un niveau y porte un poids
  de l'ordre de rho_3 fois sa part, elle-meme une fraction de |delta|). Le meme calcul sous l'autre
  reglage de numpy de machine 1 (sans le levier NPY_DISABLE_CPU_FEATURES) : 0 eligibilite ou
  couplage ecrit change, plus grand ecart sur ln G3 0.
  Controle du script contre la piece de l'exploration, a w2 = 101/50 et 3 barreaux, qui n'est pas
  candidat : 37 comparaisons, plus grand ecart 0 ; la cellule y est eligible.

8. FAISABILITE, ET CE QUE LA SECONDE PARTIE DEMANDERA
  Boites fermees. Au point sacrifie, a 3 barreaux, machine 2 a joue 32 boites des cotes 190 a 402
  sur BOCAL4, chaque niveau lu deux fois ; sa note (b9dd39f6c4ffa922) donne : "36 a 67 s aux cotes
  190-209 ; 158 a 228 s aux cotes 297-302 ; 515 a 734 s aux cotes 397-402", et "environ 1.6 Go par
  processus a 300". Sur 568 niveaux, 1 n'est pas fiable. A 4 et 5 barreaux, machine 1 n'a lu des
  boites fermees que jusqu'au cote 151 (sa note v3 du pont). La seconde partie demandera des boites
  fermees de cote 300 AU PLUS, aux trois profondeurs et aux deux signes de delta.
  Densite 2D sous absorbeur hors du vide. Sur le poste de machine 1, au point sacrifie : boites de
  104 a 134 quanta de cote, de 1.3 a 3.5 s par factorisation creuse, treize factorisations par
  barreau et par absorbeur. Les quatre absorbeurs du lecteur depose s'y accordent a 0.0045 pres sous
  la routine de plateau deposee. La seconde partie demandera ce calcul aux six cellules, a la
  geometrie du lecteur (r_c = 2 (m_bord + max(8, m_bord)) + 2 ; boite = bord + couches), soit des
  boites de 128 au plus pour 5 barreaux, et de 158 si un absorbeur de 100 couches au bord recule de
  30 est ajoute.
  Ce que cette section NE montre PAS : qu'une boite fermee se lit a delta < 0 (rien n'y a ete joue
  en 2D, a aucun w2), ni que les poids les plus petits de la table de la section 7 (5 barreaux, 8
  |delta|) sortent fiables d'une boite de cote 300. La seconde partie dira ce que vaut une cellule
  dont trop de niveaux ne sont pas fiables.

9. VIRGINITE
  Balayage de machine 1, par recherche de texte, des seize w2 candidats : leur fraction irreductible
  ; leur ecriture au millieme apres "w2" ; dans les JSON, une cle "delta" qui les designe.
    Au registre (2988237, 2852 fichiers lus) : 15 fichiers portent un w2 candidat, sous 15 noms. Ce
    sont les pieces de la premiere partie du gel du vide (ses tables d'eligibilite des deux
    machines, ses tirages de demonstration, le texte du gel, sa certification, ses balayages) : des
    chaines a une dimension et des listes. Aucun n'a le nom d'une sortie 2D (sonde, verdict, boite).
    Sur le poste de machine 1, hors des clones du registre et du dossier de ce gel (12819 fichiers
    lus) : 0 fichier porte un w2 candidat. Ce conteneur n'est pas celui ou l'exploration du pont du
    16/11 a ete jouee ; ce balayage ne le voit pas.
  Une recherche de texte n'est pas une preuve d'absence. Machine 2 tient les archives des runs et de
  ses propres explorations, et fait le sien.

10. CE QUE MACHINE 2 CERTIFIE
  (a) que les definitions des sections 2 et 4, avec les blocs deposes, suffisent a calculer
      l'eligibilite sans lire le code de machine 1 ;
  (b) SA table d'eligibilite des 48 cellules, par sa chaine, densites hors du vide comprises ; et la
      table commune qui en resulte ;
  (c) que son tirage, sur la graine de demonstration, rend les memes numeros que la section 3 et que
      le journal d'autotest ;
  (d) SON balayage de ses archives et de ses explorations : aucune boite fermee, aucune densite 2D
      hors de l'energie du vide et aucune largeur 2D du systeme a fantome a un w2 candidat de ce gel
      ;
  (e) ce que BOCAL4 peut jouer : des boites fermees jusqu'au cote 300, a 3, 4 et 5 barreaux, ou
      jusqu'ou il le peut.

11. LA SUITE, DANS L'ORDRE
  (1) machine 2 certifie cette piece et rend sa table ; la table commune existe ;
  (2) l'operateur donne la graine aux deux machines ;
  (3) chaque machine tire ; les cellules sont les memes, ou PAS DE GEL ;
  (4) machine 1 ecrit la seconde partie : l'instrument, la table gelee des six cellules avec ce que
      les chaines seules en predisent, les enonces et leurs tolerances, ce que chaque issue engage,
      ce que vaut une cellule illisible, et les annonces de la plume. Trois familles d'enonces, la
      cellule pour unite : (L) la densite 2D sous absorbeur aux douze ecarts, avec le hamiltonien et
      les absorbeurs du bloc depose du lecteur, contre le lisse d'ordre 3 ; (S) la somme des parts
      des niveaux de la boite fermee, sur la largeur de la fenetre ; (C) la croissance du nombre de
      niveaux de la fenetre avec le cote. L'instrument de la boite fermee sera ecrit par machine 1
      et ne recopiera pas celui de machine 2, qui reste une seconde feuille independante ;
  (5) machine 2 certifie la seconde partie ; l'operateur donne le feu vert par ecrit ; machine 2
      joue, une fois.
  Une question sera posee a cote des enonces, sans faire tomber le gel : au point sacrifie la somme
  des parts vaut 1.043 +- 0.018 sur 32 boites, et ce n'est pas le lisse (la chaine d'ordre 3 y rend
  la densite 2D a 0.0051 pres en moyenne sur la fenetre). Le run dira, toutes cellules confondues,
  si cet exces se retrouve.

12. CE QUE CETTE PIECE NE FAIT PAS, ET SES ECARTS A LA REGLE DU GEL PRECEDENT
  - Elle ne tire rien et ne connait aucune graine.
  - Elle ne donne aucun enonce ni aucune tolerance : c'est a la seconde partie, avant le run.
  - Ecart 1 : deux creneaux au lieu de quatre. Les petits desaccords sont hors de portee des boites
    fermees : au point sacrifie le nombre de niveaux de la fenetre croit comme le cote, et la
    lecture de machine 1, non eprouvee ailleurs, est qu'il croit comme le cote fois |delta|.
  - Ecart 2 : les deux w2 que le gel du vide a joues sont retires des candidats ; huit w2 par
    creneau au lieu de neuf.
  - Ecart 3 : trois profondeurs, toutes jugees ; pas de ligne profonde.
  - Ecart 4 : deux conditions d'eligibilite de plus, (iv) et (v), hors de l'energie du vide. Elles
    viennent d'une exploration a un seul point et a un seul signe de delta ; (v) ecarte trois w2 du
    creneau MG.
  - Le creneau MG est joue a l'aveugle pour la 2D : aucune boite fermee et aucune densite hors du
    vide n'a ete regardee a delta < 0, a aucun w2. C'est voulu.
  - Les bornes des creneaux, les profondeurs, les douze ecarts et les seuils 0.03 et 0.10 sont de la
    plume de machine 1.
  - La definition du hamiltonien effectif est celle des blocs deposes (forme symetrique) ; aucune
    autre n'est essayee.

13. PIECES DE CE LOT (convention B)
    733369d4b82e0b1b  eligibilite_pont_machine1_v1.py
    5ffa5ddc6d1be5cc  eligibilite_pont_MG_PG_v1.log
    d03c9ca093ea5bfc  eligibilite_pont_MG_PG_v1.json
    046013af8f0d8baa  eligibilite_pont_MG_PG_sans_levier_v1.log
    d03c9ca093ea5bfc  eligibilite_pont_MG_PG_sans_levier_v1.json
    16104d467a7b685d  controle_point_sacrifie_machine1_v1.log
    6ab6dbd3c5c24ce5  controle_point_sacrifie_v1.json
    69b8e585f57e0c1e  tirage_pont_machine1_v1.py
    417ea261168ada36  tirage_pont_machine1_v1_autotest.log
    20b146a4f372a339  tirage_pont_machine1_v1_demonstration.log
    af52bf8e4913338f  balayage_virginite_pont_machine1_v1.py
    30f62e4ad10f1206  balayage_virginite_pont_registre_v1.log
    611c608611486746  balayage_virginite_pont_registre_v1.json
    9ef9127363b47764  balayage_virginite_pont_poste_v1.log
    61d7f33c4f79cca6  balayage_virginite_pont_poste_v1.json
  de l'exploration du 17/11, qui voyage avec ce lot :
    f841cec8c053695d  note_machine1_pont_lisse_hors_vide_2026-11-17_v1.md
    5bb45d0c8081106f  attendu_lisse_hors_vide_machine1_v1.txt
    c0dc8b2732ba7065  rectificatif_instrument_lisse_hors_vide_machine1_v1.txt
    e83a884596341a64  lisse_chaine_machine1_v1.py
    249e26206ae60628  lisse_chaine_machine1_v1.log
    4ee91c66556452df  lisse_chaine_v1.json
    95a91f49bb5db12e  lisse_2d_machine1_v1.py
    9168bcb081b741a8  lisse_2d_A_v1.log
    7f4a0f919086744b  lisse_2d_A_v1.json
    fce1fd5769eb16d6  lisse_2d_A_bords_v1.log
    f93987fbc785044d  lisse_2d_A_bords_v1.json
    a2ed82c568c1a047  lisse_2d_B_v1.log
    e0aef8392e43bfe8  lisse_2d_B_v1.json
    b6059a62413eaad2  lisse_2d_B_bords_v1.log
    4fa2b3952b1da541  lisse_2d_B_bords_v1.json
    9df8e2240dff1d29  lisse_2d_C_v1.log
    c311fe04fde26fb5  lisse_2d_C_v1.json
    eba1b9e107de411b  lisse_2d_C_bords_v1.log
    683d22e0cf7062f3  lisse_2d_C_bords_v1.json
    98dcffdcf9beb1e7  lisse_2d_D_v1.log
    4eb14e481856206b  lisse_2d_D_v1.json
    7bd60e29c968b022  lisse_2d_D_bords_v1.log
    0dec1e62a842499e  lisse_2d_D_bords_v1.json
    67091a02bc596961  lisse_2d_E_v1.log
    eb339af32a85402b  lisse_2d_E_v1.json
    c115412d3ca07517  lecture_lisse_hors_vide_machine1_v1.py
    f73f062bce1dcfd0  lecture_lisse_hors_vide_machine1_v1.log
    900c724b33f45661  lecture_lisse_hors_vide_v1.json
    f67024ac1be82697  controle_absorbeur_recule_machine1_v1.py
    60778a8ca2811ccc  controle_absorbeur_recule_machine1_v1.log
    a7de47c7c6641503  controle_absorbeur_recule_v1.json
    2b12a62400de625e  construction_note_lisse_hors_vide_machine1_v1.py
    ffed1c621093dae6  note_machine1_pont_lecture_grandes_boites_2026-11-17_v1.md
    3425606ef5a12cf3  rejeu_grandes_boites_machine1_v1.py
    67ca2781d7a1eddb  rejeu_grandes_boites_machine1_v1.log
    0ecda0209fc4c142  rejeu_grandes_boites_v1.json
    a3677f29373dcf3b  regards_niveaux_machine1_v1.py
    9d9b1d0f53b7ccbd  regards_niveaux_machine1_v1.log
    690359efcf00cd87  regards_niveaux_v1.json
    ed88f3a8886b2579  regards_complements_machine1_v1.py
    30b7c450b485f30c  regards_complements_machine1_v1.log
    93cbf727c43d2c7a  regards_complements_v1.json
    74280e9015b48c50  construction_note_lecture_grandes_boites_machine1_v1.py
    (ce script)       construction_regle_tirage_pont_machine1_v1.py

-- FIN gel_pont_partie1_regle_tirage_pre_enregistrement_v1 --
