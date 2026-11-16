GEL "LARGEUR DU VIDE" -- PREMIERE PARTIE : LA REGLE DE TIRAGE ET D'ELIGIBILITE DES CELLULES
PRE-ENREGISTREMENT v1 -- machine 1, 2026-11-16.
A CERTIFIER PAR MACHINE 2 AVANT QUE L'OPERATEUR DONNE LA GRAINE.

0. STATUT
  Cette piece fixe COMMENT les cellules du gel seront tirees et QUAND un tirage est admis. Elle ne
  fixe ni les enonces juges, ni les tolerances, ni les probabilites, ni l'instrument : c'est la
  seconde partie, ecrite apres le tirage sur les chaines seules, et certifiee avant tout run.
  L'objet du gel : la largeur de l'etat que porte le site (0, 0) du systeme a fantome, "le vide",
  lue en 2D par le lecteur creux, et ce que la chaine a une dimension en predit.
  Ouverture, selon machine 1 : a la fin de la note sur le vide (15641e09a351d56d, hors chaine,
  classe 3), machine 1 a propose ce gel ; l'operateur a ecrit "on gele et on avance !"
  (16/11/2026, 12 h 19). A l'operateur de l'attester ou de le dementir.
  E19. Selon ses pieces (section 9), machine 1 n'a fait aucun calcul 2D du systeme a fantome,
  dense ou creux, a un w2 candidat, et n'a lu aucune largeur 2D de l'etat porte par (0, 0) du
  systeme a fantome a AUCUN w2, candidat ou non. Aucune des deux machines ne fera l'un avant la
  certification croisee de la seconde partie, ni l'autre avant le run. Machine 2 dit ce qu'il en
  est pour elle (section 10, d). Tout ce que cette piece calcule est une chaine a une dimension,
  sauf la section 8, qui lit le JUMEAU SANS FANTOME (signe +1) a un w2 qui n'est pas candidat.

1. SOURCES (convention B)
    82a0be882568fe0c scripts/m17_chaine_v17.py (registre dee73bd), le moteur
    7cd5977bc27bebc1 scripts/chaine_ordre2_bloc_machine1_v1.py (registre), le bloc d'ordre 2
    534ba246aa3b8973 scripts/ordre3_bloc_machine1_v1.py (registre), le bloc d'ordre 3
    d5cc48f48e37af99 scripts/sonde_lecteur_gel_loi_machine1_v1.py (registre), le lecteur creux ;
                      lu ici au jumeau seulement
    b56ca5cb2dd25da1 gels/gel_loi_ordre3_partie1_regle_tirage_pre_enregistrement_v1.md (registre)
                      : la regle de tirage dont celle-ci reprend la forme
    0f608f8ade6ff378 scripts/tirage_machine1_v1.py (registre), le tirage dont celui de ce lot
                      derive
    15641e09a351d56d note_machine1_vide_etape_sans_run_2026-11-16_v1.md (lot c5d8fd0313217569),
                      sections 3, 6 et 7 : l'absorbeur adapte et la proposition
    8548cc16fb746f56 note_machine1_loi_echelle_2026-11-16_v1.md (lot 408b8a595cad0040) : la loi
                      d'echelle et la regle de barriere a la limite
  Les deux derniers lots sont HORS REGISTRE et machine 1 etait seule a les detenir : ils voyagent
  avec ce lot, dans la meme enveloppe.

2. LES CRENEAUX ET LES CELLULES
  Quatre creneaux, neuf w2 candidats chacun. Les w2 candidats sont au millieme ; les centiemes en
  sont exclus, et |w2 - 2| < 0.02.
    MG  delta < 0, grand  delta de -0.019 a -0.011   w2 = 1.981 a 1.989   9 valeurs
    MP  delta < 0, petit  delta de -0.009 a -0.001   w2 = 1.991 a 1.999   9 valeurs
    PP  delta > 0, petit  delta de +0.001 a +0.009   w2 = 2.001 a 2.009   9 valeurs
    PG  delta > 0, grand  delta de +0.011 a +0.019   w2 = 2.011 a 2.019   9 valeurs
  Sept PROFONDEURS de barriere m, chacune avec son rapport kappa_m, constante de ce gel :
    LISIBLES   m = 3 : 0.0262   m = 4 : 0.0200   m = 5 : 0.0159   m = 6 : 0.0130
    PROFONDES  m = 8 : 0.00928   m = 12 : 0.00558   m = 16 : 0.00382
  Une CELLULE est un couple (w2, m). Son couplage est
        g = kappa_m x |w2 - 2| x P / X(w2) ,
        X(w2) = X_saut_reel(P, 2, 1, 0, 0, w2) du moteur, P = 5,
  calcule en double precision puis ARRONDI a six chiffres significatifs (le format "%.5e" de
  Python) : le couplage de la cellule EST le nombre decimal ainsi ecrit. kappa est le rapport du
  saut au pied de l'echelle, t_0 = g X(w2) / P, au desaccord |w2 - 2|. Les kappa_m sont, a trois
  chiffres, le milieu geometrique de l'intervalle de kappa ou la barriere de l'etat (0, 0), a la
  limite du desaccord nul, finit au site m (note sur la loi d'echelle) ; ce gel fige les
  decimales, pas la derivation.
  Un tirage donne un w2 par creneau, donc seize cellules lisibles et au plus douze cellules
  profondes, nommees par le creneau et la profondeur : MG3, MG4, MG5, MG6, MG8, MG12, MG16, et de
  meme pour MP, PP, PG.

3. LE TIRAGE
  Le w2 du creneau s au rang r est l'element de numero
        int( sha256("<graine>|<s>|<r>") ecrit en hexadecimal, 16 )  modulo  n_s
  de la liste CROISSANTE des n_s w2 candidats du creneau, numerotee a partir de 0. La chaine
  hachee est codee en ASCII ; s vaut MG, MP, PP ou PG ; r s'ecrit en decimal, sans zero devant ;
  la barre verticale est le caractere 124.
  LA GRAINE est une suite de chiffres (0 a 9), d'au moins six chiffres, donnee par L'OPERATEUR,
  par ecrit, aux deux machines, APRES la certification de cette piece et apres que la table
  commune de la section 5 existe. Elle est reportee telle quelle, zeros de tete compris, dans la
  seconde partie. Ni machine 1 ni machine 2 ne la choisit, ne la propose, ni ne la commente avant
  de l'avoir recue.
  Chaque machine tire par SON code. Exemple de controle, sur une graine de demonstration qui n'est
  pas une suite de chiffres et ne peut donc pas etre la graine :
    sha256("DEMONSTRATION|MG|0") = 8254e7d473dd8e66... ; modulo  9 =  6 -> w2 = 1.987

4. L'ELIGIBILITE D'UNE CELLULE (chaine seule, aucune 2D)
  4.1 La barriere : sites = barriere(0, 0, w2, g, avec Sigma2) du moteur ; m_bord = son dernier
      site ; e_bord = |m_bord delta + Sigma2(m_bord) - Sigma2(0)|, avec delta = w2 - 2.
  4.2 Les tables : tables_ordre2(0, 0, w2, g, sites, M_facteur 4) puis tables_ordre3, des blocs
      deposes. Par site m de l'echelle : le decalage S_m, le saut du premier ordre t_m (de m a m +
      1), le saut au second voisin U_m, et a l'ordre 3 la correction T3_m du saut et les sauts
      W3_m (de m a m + 3) et W5_m (de m a m + 5).
  4.3 La chaine d'ordre 3 sous ABSORBEUR ADAPTE, variante (a, c, L). debut = m_bord + c. Les sites
      vont du premier site des tables (m_min) au site debut + L. Matrice symetrique complexe : sur
      la diagonale, m delta + S_m - S_0 - i W_m ; hors diagonale, t_m + T3_m entre m et m + 1, U_m
      entre m et m + 2, W3_m entre m et m + 3, W5_m entre m et m + 5. L'absorbeur :
        W_m = a |t_m| ((m - debut) / L)^2   pour debut < m <= debut + L ,   0 ailleurs.
      Dix-huit variantes : a = 1, 2, 4 ; c = 6, 8, 10 ; L = 16, 24. Seuls l'absorbeur et la
      longueur different de la chaine d'ordre 3 du bloc depose.
  4.4 La largeur d'une variante : Gamma = -2 Im(E), E etant la valeur propre de cette matrice dont
      le vecteur propre, norme, porte le plus grand poids sur le site 0. C'est une propriete de la
      matrice : chaque machine la calcule par sa methode. La double precision ne la rend pas sous
      environ 1e-16 |delta| ; machine 1 la lit par le flux tant que Gamma / |delta| > 1e-15 et, en
      dessous, reprend la valeur propre en precision arbitraire (100 chiffres) sur la meme
      matrice.
  4.5 Le PLATEAU G3* est l'exponentielle de la mediane des dix-huit ln Gamma (la moyenne des deux
      valeurs centrales) ; l'ETENDUE est le plus grand moins le plus petit des dix-huit ln Gamma.
      Elle est indefinie si l'une des largeurs n'est pas strictement positive.
  4.6 La cellule (w2, m) est ELIGIBLE si : (i) m_bord = m ; (ii) e_bord < 0.7 ; (iii) l'etendue
      est definie et <= 0.02.
  4.7 Un w2 candidat est ELIGIBLE si ses quatre cellules LISIBLES le sont. Une cellule PROFONDE
      est RETENUE si elle est eligible ; elle ne decide pas de l'eligibilite du w2. Une cellule
      profonde non retenue n'est pas jouee, et c'est dit.
  4.8 D'ou viennent les nombres. 0.7 est la garde du domaine du gel "ordre 3" depose. Le seuil
      0.02 et la condition (i) sont poses ici, APRES la note sur le vide, qui a vu des etendues de
      0.0085 au plus a ses points de 3 a 16 barreaux, et AVANT d'avoir calcule une seule cellule
      sous cette regle. Les deux notes de ce jour avaient deja calcule, en chaine seule et a
      d'autres couplages que ceux des cellules, 4 w2 qui sont des candidats : 1.995, 1.999, 2.001,
      2.005 (section 9). Les profondeurs, les kappa_m et les dix-huit variantes viennent de la
      note sur le vide. Aucun de ces nombres ne sera regle ensuite.

5. LA TABLE COMMUNE, AVANT LA GRAINE
  Chaque machine calcule par SA chaine l'eligibilite des 252 cellules candidates (36 w2) AVANT que
  la graine existe. La table de machine 1 est en section 7. Machine 2 rend la sienne avec sa
  certification. LA TABLE COMMUNE est leur ET : un w2 candidat y est eligible si et seulement s'il
  l'est dans les deux tables ET si les couplages ecrits de ses sept cellules sont les memes dans
  les deux ; une cellule profonde y est retenue si et seulement si elle l'est dans les deux. Elle
  ne depend d'aucune graine. Un desaccord entre les deux tables est dit dans la certification ; il
  n'arrete pas le gel.
  Format d'une table : JSON, creneaux -> <nom du creneau> -> candidats -> liste de {"w2":
  "<fraction irreductible>", "eligible": true ou false, "cellules": liste de {"m": <entier>, "g":
  "<le decimal a six chiffres>", "eligible": true ou false}}.

6. LA REGLE DES RANGS
  Pour chaque creneau, dans l'ordre MG, MP, PP, PG et independamment : rang 0 ; si le w2 tire
  n'est pas eligible dans la table commune, rang 1, et ainsi de suite, pour le CRENEAU ENTIER
  (jamais cellule par cellule). Au plus cinq rangs, de 0 a 4. Si un creneau n'a pas de w2 eligible
  en cinq rangs : PAS DE GEL, et on le dit. Un meme w2 peut sortir a deux rangs ; il n'est pas
  retire de la liste.
  Si les deux machines ne tirent pas les memes cellules, avec les memes couplages ecrits, a partir
  de la meme graine et de la meme table commune : PAS DE GEL tant que l'ecart n'est pas explique
  par ecrit, et la graine n'est pas changee.

7. LA TABLE DE MACHINE 1 (252 cellules)
  Par cellule : l'etendue de la chaine d'ordre 3 sous l'absorbeur adapte. Les couplages ecrits
  sont dans la table JSON (eligibilite_candidates_vide_v1.json, 7b278d2b5a34d0a3).
  creneau MG : 9 w2 eligibles sur 9 ; cellules profondes retenues : 27 sur 27
    1.981  m3 0.0018  m4 0.0014  m5 0.0023  m6 0.0023  m8 0.0053  m12 0.0091  m16 0.0088  ELIGIBLE
    1.982  m3 0.0013  m4 0.0014  m5 0.0026  m6 0.0022  m8 0.0054  m12 0.0092  m16 0.0086  ELIGIBLE
    1.983  m3 0.0014  m4 0.0014  m5 0.0027  m6 0.0020  m8 0.0055  m12 0.0092  m16 0.0084  ELIGIBLE
    1.984  m3 0.0014  m4 0.0014  m5 0.0027  m6 0.0020  m8 0.0056  m12 0.0092  m16 0.0084  ELIGIBLE
    1.985  m3 0.0014  m4 0.0015  m5 0.0026  m6 0.0024  m8 0.0059  m12 0.0093  m16 0.0084  ELIGIBLE
    1.986  m3 0.0017  m4 0.0020  m5 0.0028  m6 0.0027  m8 0.0063  m12 0.0093  m16 0.0084  ELIGIBLE
    1.987  m3 0.0020  m4 0.0026  m5 0.0027  m6 0.0030  m8 0.0064  m12 0.0093  m16 0.0084  ELIGIBLE
    1.988  m3 0.0022  m4 0.0030  m5 0.0023  m6 0.0031  m8 0.0064  m12 0.0093  m16 0.0083  ELIGIBLE
    1.989  m3 0.0025  m4 0.0032  m5 0.0017  m6 0.0031  m8 0.0063  m12 0.0093  m16 0.0083  ELIGIBLE
  creneau MP : 9 w2 eligibles sur 9 ; cellules profondes retenues : 27 sur 27
    1.991  m3 0.0023  m4 0.0032  m5 0.0023  m6 0.0030  m8 0.0061  m12 0.0093  m16 0.0082  ELIGIBLE
    1.992  m3 0.0021  m4 0.0030  m5 0.0027  m6 0.0032  m8 0.0062  m12 0.0093  m16 0.0081  ELIGIBLE
    1.993  m3 0.0028  m4 0.0022  m5 0.0029  m6 0.0033  m8 0.0062  m12 0.0093  m16 0.0080  ELIGIBLE
    1.994  m3 0.0033  m4 0.0015  m5 0.0028  m6 0.0042  m8 0.0063  m12 0.0093  m16 0.0078  ELIGIBLE
    1.995  m3 0.0034  m4 0.0016  m5 0.0027  m6 0.0050  m8 0.0063  m12 0.0092  m16 0.0077  ELIGIBLE
    1.996  m3 0.0032  m4 0.0023  m5 0.0024  m6 0.0056  m8 0.0064  m12 0.0092  m16 0.0076  ELIGIBLE
    1.997  m3 0.0027  m4 0.0029  m5 0.0020  m6 0.0058  m8 0.0064  m12 0.0091  m16 0.0074  ELIGIBLE
    1.998  m3 0.0018  m4 0.0030  m5 0.0028  m6 0.0057  m8 0.0064  m12 0.0090  m16 0.0072  ELIGIBLE
    1.999  m3 0.0023  m4 0.0028  m5 0.0038  m6 0.0053  m8 0.0064  m12 0.0090  m16 0.0070  ELIGIBLE
  creneau PP : 9 w2 eligibles sur 9 ; cellules profondes retenues : 27 sur 27
    2.001  m3 0.0035  m4 0.0022  m5 0.0048  m6 0.0047  m8 0.0065  m12 0.0088  m16 0.0065  ELIGIBLE
    2.002  m3 0.0033  m4 0.0032  m5 0.0047  m6 0.0047  m8 0.0065  m12 0.0087  m16 0.0063  ELIGIBLE
    2.003  m3 0.0028  m4 0.0041  m5 0.0043  m6 0.0049  m8 0.0065  m12 0.0085  m16 0.0060  ELIGIBLE
    2.004  m3 0.0026  m4 0.0045  m5 0.0041  m6 0.0050  m8 0.0067  m12 0.0084  m16 0.0057  ELIGIBLE
    2.005  m3 0.0032  m4 0.0042  m5 0.0041  m6 0.0052  m8 0.0068  m12 0.0083  m16 0.0054  ELIGIBLE
    2.006  m3 0.0039  m4 0.0039  m5 0.0040  m6 0.0053  m8 0.0071  m12 0.0081  m16 0.0050  ELIGIBLE
    2.007  m3 0.0037  m4 0.0038  m5 0.0036  m6 0.0054  m8 0.0076  m12 0.0079  m16 0.0052  ELIGIBLE
    2.008  m3 0.0037  m4 0.0039  m5 0.0038  m6 0.0056  m8 0.0078  m12 0.0077  m16 0.0052  ELIGIBLE
    2.009  m3 0.0036  m4 0.0038  m5 0.0040  m6 0.0057  m8 0.0079  m12 0.0078  m16 0.0054  ELIGIBLE
  creneau PG : 9 w2 eligibles sur 9 ; cellules profondes retenues : 27 sur 27
    2.011  m3 0.0046  m4 0.0033  m5 0.0044  m6 0.0059  m8 0.0080  m12 0.0079  m16 0.0057  ELIGIBLE
    2.012  m3 0.0043  m4 0.0032  m5 0.0045  m6 0.0061  m8 0.0082  m12 0.0079  m16 0.0058  ELIGIBLE
    2.013  m3 0.0033  m4 0.0037  m5 0.0047  m6 0.0068  m8 0.0083  m12 0.0079  m16 0.0060  ELIGIBLE
    2.014  m3 0.0029  m4 0.0039  m5 0.0050  m6 0.0073  m8 0.0082  m12 0.0079  m16 0.0061  ELIGIBLE
    2.015  m3 0.0037  m4 0.0040  m5 0.0061  m6 0.0075  m8 0.0082  m12 0.0078  m16 0.0062  ELIGIBLE
    2.016  m3 0.0045  m4 0.0053  m5 0.0066  m6 0.0074  m8 0.0083  m12 0.0078  m16 0.0064  ELIGIBLE
    2.017  m3 0.0054  m4 0.0063  m5 0.0069  m6 0.0070  m8 0.0084  m12 0.0077  m16 0.0068  ELIGIBLE
    2.018  m3 0.0057  m4 0.0066  m5 0.0068  m6 0.0073  m8 0.0085  m12 0.0076  m16 0.0075  ELIGIBLE
    2.019  m3 0.0050  m4 0.0060  m5 0.0063  m6 0.0076  m8 0.0085  m12 0.0075  m16 0.0081  ELIGIBLE
  Un point d'exclamation marquerait une cellule ineligible : il n'y en a aucune. Par profondeur,
  sur les 36 w2 :
    m    barreaux   etendue   e_bord   plus grande   plateau predit G3*   methode
         trouves    max       max      boite         de ... a ...         de machine 1
    3    3          0.0057    0.057    124           1.7e-10 a 3.1e-09    flux
    4    4          0.0066    0.077    126           3.7e-12 a 6.9e-11    flux
    5    5          0.0069    0.096    128           7.6e-14 a 1.4e-12    flux
    6    6          0.0076    0.115    130           1.5e-15 a 2.8e-14    flux
    8    8          0.0085    0.154    134           4.8e-19 a 9.2e-18    precision arbitraire
    12   12         0.0093    0.232    150           4.2e-26 a 8.1e-25    precision arbitraire
    16   16         0.0088    0.310    166           3.2e-33 a 6.2e-32    precision arbitraire
  La plus grande etendue est 0.0093 (0.0076 aux cellules lisibles) pour un seuil de 0.02 :
  l'eligibilite ne trie rien ici, et le tirage est donc uniforme sur les candidats. Le plus petit
  poids du site 0 dans l'etat lu est 0.9993. La plus grande boite du lecteur serait N = r_c + 100,
  avec r_c = 2 (m_bord + max(8, m_bord)) + 2, la regle du depot sans graine. Le meme calcul sous
  l'autre reglage de numpy de machine 1 (sans le levier NPY_DISABLE_CPU_FEATURES) : 0 eligibilite
  changee, 0 couplage ecrit change, plus grand ecart sur ln G3 0.
  Controle du bloc de l'absorbeur adapte contre la piece de la note sur le vide, a w2 = 99/50 et
  101/50 qui ne sont pas candidats : 20 comparaisons, plus grand ecart 3.6e-15.

8. FAISABILITE DE LA LIGNE PROFONDE (jumeau sans fantome, w2 non candidat)
  Le lecteur depose, lu tel quel, au JUMEAU H+ (signe +1 : aucune echelle resonante, la largeur
  n'y est fabriquee que par l'absorbeur), a w2 = 101/50, a la geometrie qu'aurait une cellule
  profonde ; absorbeurs A et B (la plus grande boite), barreaux k = -3, 3, 8.
    m    g            r_c   boites N     lectures   duree   memoire   plus grande largeur
                                         suivies            max       du jumeau
    8    1.95896e-03  34    114 et 134   6 sur 6    18 s    433 Mo    3.9e-56
    12   1.17791e-03  50    130 et 150   6 sur 6    26 s    578 Mo    1.9e-78
    16   8.06380e-04  66    146 et 166   6 sur 6    36 s    699 Mo    1.0e-100
  A la geometrie de cellules de 3, 4, 5 barreaux, la note sur le vide avait mesure, au jumeau
  aussi, de 94 a 114 s pour les 48 lectures d'une cellule (boites de 124 a 128 au plus), et une
  largeur du jumeau de 1.9e-35 au plus. La largeur fabriquee par l'absorbeur seul est donc tres en
  dessous des plateaux predits de la section 7, la ou elle a ete mesuree. Ce que cette section NE
  montre PAS : que le lecteur lit juste, en 2D, sur le systeme a fantome, a ces profondeurs. C'est
  au run de le dire, par sa qualification ; la seconde partie tiendra la ligne profonde hors des
  enonces qui font tomber le gel.

9. VIRGINITE
  Balayage de machine 1, par recherche de texte : la fraction irreductible de chaque w2 candidat ;
  son ecriture au millieme apres "w2" ; dans les fichiers JSON, une etiquette d'etat (0, 0), et
  une cle "delta" qui designe un w2 candidat.
    Au registre (dee73bd, 2465 fichiers suivis, tous lus) : aucune trace d'un w2 candidat ; 307
    fichiers JSON, aucun ne porte l'etiquette (0, 0) ni une telle cle.
    Sur le poste de machine 1, hors du dossier de ce gel dont les pieces portent les candidats par
    construction (117 fichiers lus) : aucune fraction ni ecriture apres "w2" d'un w2 candidat ; 17
    fichiers JSON portent l'etiquette (0, 0) et 8 portent une cle "delta" qui designe un w2
    candidat (1.995 dans mandataire_absorbeur_2D_v1.json ; 1.995 et 2.005 dans
    absorbeur_adapte_v1.json, sonde_vide_v1.json ; 1.999 et 2.001 dans controle_limite_v1.json),
    tous des deux etapes sans run de ce jour (lots 408b8a595cad0040 et c5d8fd0313217569, et leurs
    brouillons) : ce sont des chaines a une dimension.
  Les seules 2D que machine 1 ait jouees pour preparer ce gel sont celles du jumeau sans fantome,
  a w2 = 101/50 et 199/100, qui ne sont pas candidats. Ce balayage ne voit que le poste de machine
  1, et une recherche de texte n'est pas une preuve d'absence : machine 2 tient les archives des
  runs et fait le sien.

10. CE QUE MACHINE 2 CERTIFIE
  (a) que les definitions des sections 2 et 4, avec les blocs deposes, suffisent a calculer
      l'eligibilite sans lire le code de machine 1 ;
  (b) SA table d'eligibilite des 252 cellules, par sa chaine ; et la table commune qui en resulte
      ;
  (c) que son tirage, sur la graine de demonstration, rend les memes numeros que la section 3 et
      que le journal d'autotest ;
  (d) SON balayage de ses archives : aucun calcul 2D du systeme a fantome a un w2 candidat, et
      aucune largeur 2D de l'etat porte par (0, 0) du systeme a fantome, a aucun w2 ;
  (e) que BOCAL4 peut jouer des boites jusqu'a N = 166 (section 8), ou jusqu'ou il le peut.

11. LA SUITE, DANS L'ORDRE
  (1) machine 2 certifie cette piece et rend sa table ; la table commune existe ;
  (2) l'operateur donne la graine aux deux machines ;
  (3) chaque machine tire ; les cellules sont les memes, ou PAS DE GEL ;
  (4) machine 1 ecrit la seconde partie : l'instrument (la sonde du lecteur derivee du depot, sans
      etage dense, qui lit le site (0, 0) aux cellules tirees ; sa feuille ; le bloc de ce lot
      comme predicteur ; les temoins : le jumeau sans fantome a la geometrie de chaque cellule,
      les ancres et le temoin positif du depot), la table gelee des cellules avec leurs
      predictions calculees sur les chaines seules, les enonces et leurs tolerances, ce que chaque
      issue engage, ce que vaut une cellule que le lecteur ne qualifie pas, et les annonces de la
      plume ;
  (5) machine 2 certifie la seconde partie ; l'operateur donne le feu vert par ecrit ; machine 2
      joue, une fois.

12. CE QUE CETTE PIECE NE FAIT PAS, ET SES ECARTS A LA REGLE DU GEL PRECEDENT
  - Elle ne tire rien et ne connait aucune graine.
  - Elle ne donne aucune tolerance, et ne dit pas ce que vaut une cellule que le lecteur ne
    qualifie pas : c'est a la seconde partie de le dire, avant le run.
  - Ecart 1 : un seul etat par cellule, celui que porte (0, 0), au lieu de quatorze etiquettes ;
    pas d'etage dense, donc ni "jugeable" ni "dix planchers".
  - Ecart 2 : la cellule est un couple (w2, profondeur) dont le couplage vient d'une formule
    arrondie, au lieu de facteur x g_du_point(w2) ; la table commune compare aussi les couplages
    ecrits.
  - Ecart 3 : les cellules profondes ne decident pas de l'eligibilite d'un w2.
  - Ecart 4 : la stabilite est l'etendue sous dix-huit variantes de l'absorbeur adapte, au lieu de
    trois variantes de l'absorbeur du bloc depose. L'absorbeur adapte est une regle de ce jour,
    d'une seule plume ; son bloc est dans ce lot et se certifie avec lui. Son etendue mesure la
    stabilite de la chaine sous ces variantes, pas l'erreur de la chaine.
  - Les bornes des creneaux, les profondeurs et l'ordre MG, MP, PP, PG sont de la plume de machine
    1.
  - La definition du hamiltonien effectif est celle des blocs deposes (forme symetrique) ; aucune
    autre n'est essayee.

13. PIECES DE CE LOT (convention B)
    49a40d9098b55361  chaine_adaptee_bloc_machine1_v1.py
    34eb68229983b1f2  eligibilite_vide_machine1_v1.py
    9c607f28a94c139e  eligibilite_vide_MG_MP_v1.log
    22ca836236f5d9ee  eligibilite_vide_MG_MP_v1.json
    976137c284b35381  eligibilite_vide_PP_PG_v1.log
    9d4293a4a652d5fa  eligibilite_vide_PP_PG_v1.json
    d710ca96735d870e  eligibilite_vide_MG_MP_sans_levier_v1.log
    22ca836236f5d9ee  eligibilite_vide_MG_MP_sans_levier_v1.json
    264a9023a6a3983d  eligibilite_vide_PP_PG_sans_levier_v1.log
    9d4293a4a652d5fa  eligibilite_vide_PP_PG_sans_levier_v1.json
    c21f9117ffb3aec8  lecture_eligibilite_vide_machine1_v1.py
    c42393e8049cd016  lecture_eligibilite_vide_machine1_v1.log
    7b278d2b5a34d0a3  eligibilite_candidates_vide_v1.json
    99acae808e7b21f2  controle_bloc_adapte_machine1_v1.log
    1a7514c4832dbdf4  controle_bloc_adapte_v1.json
    75e7e0259b1be1d4  absorbeur_adapte_v1.json
    cc1b2df637a9f3cd  tirage_vide_machine1_v1.py
    8d09e6c8e44037f8  tirage_vide_machine1_v1_autotest.log
    dddd739e708fc6b5  tirage_vide_machine1_v1_demonstration.log
    a0bac3e110a34785  faisabilite_profondeur_jumeau_machine1_v1.py
    ad0b8136e25fb64e  faisabilite_profondeur_jumeau_machine1_v1.log
    621922fb423d46f8  faisabilite_profondeur_jumeau_v1.json
    f5a9d36605ad74db  balayage_virginite_machine1_v1.py
    e4c99cce3003bed9  balayage_virginite_registre_v1.log
    5af69de254559ec5  balayage_virginite_registre_v1.json
    a2def2c0a2b51e36  balayage_virginite_poste_v1.log
    fa13eef87672b71f  balayage_virginite_poste_v1.json
    (ce script)       construction_regle_tirage_vide_machine1_v1.py

