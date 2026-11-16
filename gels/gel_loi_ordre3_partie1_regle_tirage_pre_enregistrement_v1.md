GEL "LOI DE LA LARGEUR, ORDRE 3" -- PREMIERE PARTIE : LA REGLE DE TIRAGE ET D'ELIGIBILITE DES POINTS
PRE-ENREGISTREMENT v1 -- machine 1, 2026-11-15.
A CERTIFIER PAR MACHINE 2 AVANT QUE L'OPERATEUR DONNE LA GRAINE.

0. STATUT
  Cette piece fixe COMMENT les douze points du gel seront tires et QUAND un tirage est admis. Elle
  ne fixe ni les enonces juges, ni les tolerances, ni les probabilites, ni l'instrument : c'est la
  seconde partie, ecrite apres le tirage sur les chaines seules, et certifiee avant tout run.
  Ouverture, selon machine 1 : l'operateur a relaye (15/11/2026, 22 h 41) la phrase de machine 2
  "C'est note: vous retenez la section 5 et vous lancez le gel." (accent retire ici), puis a ecrit
  "Reprends" (22 h 42). Machine 1 le lit comme le "go" du gel. A l'operateur de l'attester ou de
  le dementir.
  E19. Aucun calcul 2D, dense ou creux, n'a ete fait ni ne sera fait par aucune des deux machines
  a un w2 candidat, avant la certification croisee de la seconde partie. Tout ce que cette piece
  calcule est une chaine a une dimension.

1. SOURCES (convention B)
    82a0be882568fe0c scripts/m17_chaine_v17.py (registre 8d54bf9), le moteur
    7cd5977bc27bebc1 scripts/chaine_ordre2_bloc_machine1_v1.py (registre), le bloc d'ordre 2
    534ba246aa3b8973 ordre3_bloc_machine1_v1.py (lot e93f1898dcd78a8f), le bloc d'ordre 3,
                      rederive par machine 2 (lot 889fe9b4c1c1c60a)
    41153158190cf7f1 gels/gel_ordre2_chaine_EA_pre_enregistrement_v1.md (registre), section 3 : la
                      regle du point
    1f6cfb5f9472b1b4 note_machine1_carte_gel_loi_2026-11-15_v1.md (lot 1e8413aed149429f), section
                      5 : la proposition
    548fb2ba8793ecfe lot de la reponse de machine 2 a la carte, sections 3 et 4 : la regle de
                      tirage reprise ici

2. LES CRENEAUX
  Quatre creneaux. Les w2 candidats sont au millieme ; les centiemes en sont exclus : aucun w2
  candidat n'a ete joue, a aucun facteur.
    N   delta dans ]-0.070, -0.060[  w2 = 1.931 a 1.939                    9 valeurs  cinq facteurs
    P   delta dans ]+0.030, +0.050[  w2 = 2.031 a 2.039 et 2.041 a 2.049  18 valeurs  cinq facteurs
    BN  delta dans ]-0.085, -0.075[  w2 = 1.916 a 1.919 et 1.921 a 1.924   8 valeurs  facteur 1
    BP  delta dans ]+0.060, +0.070[  w2 = 2.061 a 2.069                    9 valeurs  facteur 1
    Les cinq facteurs de N et de P : 3/4, 5/6, 1, 6/5, 4/3.
  Une CELLULE est un couple (w2, facteur) ; son couplage est g = facteur x g_du_point(w2), par la
  fonction du moteur. Un tirage donne un w2 par creneau, donc douze cellules : N1 a N5 et P1 a P5
  (facteurs croissants), BN, BP. Les fenetres de BN et BP sont celles que machine 2 a lues dans
  "vers -0.08" et "vers +0.065" ; machine 1 les confirme.

3. LE TIRAGE
  Le w2 du creneau s au rang r est l'element de numero
        int( sha256("<graine>|<s>|<r>") ecrit en hexadecimal, 16 )  modulo  n_s
  de la liste CROISSANTE des n_s w2 candidats du creneau, numerotee a partir de 0. La chaine
  hachee est codee en ASCII ; s vaut N, P, BN ou BP ; r s'ecrit en decimal, sans zero devant ; la
  barre verticale est le caractere 124.
  LA GRAINE est une suite de chiffres (0 a 9), d'au moins six chiffres, donnee par L'OPERATEUR,
  par ecrit, aux deux machines, APRES la certification de cette piece et apres que la table
  commune de la section 5 existe. Elle est reportee telle quelle, zeros de tete compris, dans la
  seconde partie. Ni machine 1 ni machine 2 ne la choisit, ne la propose, ni ne la commente avant
  de l'avoir recue.
  Chaque machine tire par SON code. Exemple de controle, sur une graine de demonstration qui n'est
  pas une suite de chiffres et ne peut donc pas etre la graine :
    sha256("DEMONSTRATION|N|0") = 4b2a1d038c89c813... ; modulo  9 =  4 -> w2 = 1.935

4. L'ELIGIBILITE D'UNE CELLULE (chaine seule, aucune 2D)
  4.1 Le point (regle de la sonde dense, gel du delta 98, section 3) : g = facteur x
      g_du_point(w2) ; s = 0.70 s_ff(w2, g) ; graine (n1g, n2g) = appariement(s, w2), reels ; m =
      dernier site de barriere(n1g, n2g, w2, g, avec Sigma2), 0 si elle est vide ; r_c =
      plafond(n1g) + 2 (m + max(8, m)) + 2 ; boite N = r_c + 20.
  4.2 Les quatorze etiquettes : les couples d'entiers (a, b), a >= 0, b >= 0, de plus grand poids
      de Poisson p(a, b) = exp(-n1g) n1g^a / a! x exp(-n2g) n2g^b / b! ; a poids egal, le plus
      petit a, puis le plus petit b. Ce sont des etiquettes PREDITES : aux seize points deja
      joues, 189 des 224 etiquettes lues en font partie.
  4.3 Par etiquette (a, b) : sites = barriere(a, b, w2, g, avec Sigma2). Chaine du moteur :
      gamma_chaine, M_facteur 4, aux quatre eta de chaine (facteurs 1/4, 1/8, 1/16, 1/32). Chaine
      d'ordre 2 : tables_ordre2 (M_facteur 4), gamma_chaine_ordre2 aux quatre memes facteurs,
      valeur Gamma_flux. Chaine d'ordre 3 : tables_ordre3, gamma_chaine_ordre3 au facteur 1/16,
      valeur Gamma_flux, notee G3 ; STABILITE = le plus grand |ln(G3' / G3)| pour G3' calculee au
      facteur 1/8, au facteur 1/32, et au facteur 1/16 avec l'absorbeur recule de 4 sites ;
      indefinie si l'une de ces quatre largeurs n'est pas strictement positive. e_bord = |m_bord
      delta + Sigma2(m_bord) - Sigma2(0)|, m_bord etant le dernier site de la barriere de
      l'etiquette et delta = w2 - 2.
  4.4 Classement. L'etiquette est DANS LES GARDES si e_bord < 0.7 et si la stabilite est definie
      et <= 0.05. Sa largeur predite G est G3 si elle est dans les gardes, sinon la largeur
      d'ordre 2 au facteur 1/16. Elle est JUGEABLE si sa barriere n'est pas vide, si les quatre
      largeurs du moteur sont strictement positives avec max / min <= 2, si les quatre largeurs
      d'ordre 2 le sont aussi, et si G > 1.33e-12 (dix planchers). Elle est DANS LE DOMAINE si
      elle est jugeable et dans les gardes.
  4.5 Regle COMMUNE (cellules de N et de P) : N <= 74, au moins 8 etiquettes jugeables sur les 14,
      dont au moins 5 dans le domaine.
  4.6 Regle DE BORD (cellules de BN et de BP) : N <= 74, au moins 8 etiquettes jugeables, dont au
      moins 2 dans le domaine ET au moins 2 hors du domaine. Ces cellules sont faites pour
      chevaucher la limite du domaine ; la regle commune ne leur convient pas.
  4.7 Un w2 candidat est ELIGIBLE si toutes ses cellules le sont : cinq pour N et P, une pour BN
      et BP.
  4.8 Les seuils 0.7 et 0.05 ont ete lus sur les 131 etats deja vus (note sur la loi) ; 74, 8 et 5
      sur la carte ; 2 et 2 sont poses ici, apres avoir vu la carte et avant d'avoir calcule un
      seul w2 candidat. Aucun ne sera regle ensuite.

5. LA TABLE COMMUNE, AVANT LA GRAINE
  Chaque machine calcule par SA chaine l'eligibilite des 152 cellules candidates (44 w2) AVANT que
  la graine existe. La table de machine 1 est en section 7. Machine 2 rend la sienne avec sa
  certification. LA TABLE COMMUNE est leur ET : un w2 candidat y est eligible si et seulement s'il
  l'est dans les deux tables. Elle ne depend d'aucune graine. Un desaccord entre les deux tables
  sur un w2 le rend donc ineligible, et il est dit dans la certification ; il n'arrete pas le gel.
  Format d'une table : JSON, creneaux -> <nom du creneau> -> candidats -> liste de {"w2":
  "<fraction irreductible>", "eligible": true ou false}.

6. LA REGLE DES RANGS
  Pour chaque creneau, dans l'ordre N, P, BN, BP et independamment : rang 0 ; si le w2 tire n'est
  pas eligible dans la table commune, rang 1, et ainsi de suite, pour le CRENEAU ENTIER (jamais
  cellule par cellule). Au plus cinq rangs, de 0 a 4. Si un creneau n'a pas de w2 eligible en cinq
  rangs : PAS DE GEL, et on le dit. Un meme w2 peut sortir a deux rangs ; il n'est pas retire de
  la liste.
  Si les deux machines ne tirent pas les memes douze cellules a partir de la meme graine et de la
  meme table commune : PAS DE GEL tant que l'ecart n'est pas explique par ecrit, et la graine
  n'est pas changee.

7. LA TABLE DE MACHINE 1 (152 cellules)
  Par cellule : facteur, boite N, etiquettes jugeables / dans le domaine ; pour BN et BP : / hors
  du domaine.
  creneau N : 9 w2 eligibles sur 9
    1.931  x3/4 68 11/11  x5/6 63 9/9  x1 60 12/12  x6/5 57 13/13  x4/3 55 14/14  ELIGIBLE
    1.932  x3/4 68 11/11  x5/6 63 9/9  x1 60 12/12  x6/5 57 13/13  x4/3 55 14/13  ELIGIBLE
    1.933  x3/4 68 11/11  x5/6 63 9/9  x1 60 12/12  x6/5 57 13/13  x4/3 55 14/13  ELIGIBLE
    1.934  x3/4 68 11/11  x5/6 63 10/10  x1 60 12/12  x6/5 57 13/13  x4/3 55 14/14  ELIGIBLE
    1.935  x3/4 68 11/11  x5/6 63 10/10  x1 60 12/12  x6/5 57 13/13  x4/3 55 14/14  ELIGIBLE
    1.936  x3/4 68 11/11  x5/6 63 10/10  x1 60 12/12  x6/5 57 13/13  x4/3 55 14/14  ELIGIBLE
    1.937  x3/4 68 11/11  x5/6 63 10/10  x1 60 12/12  x6/5 57 13/13  x4/3 55 14/14  ELIGIBLE
    1.938  x3/4 68 11/11  x5/6 63 10/10  x1 60 12/12  x6/5 57 13/13  x4/3 55 14/14  ELIGIBLE
    1.939  x3/4 68 11/11  x5/6 63 10/10  x1 60 12/12  x6/5 57 13/13  x4/3 55 14/14  ELIGIBLE
  creneau P : 18 w2 eligibles sur 18
    2.031  x3/4 69 12/12  x5/6 64 12/12  x1 61 13/13  x6/5 58 13/13  x4/3 55 13/13  ELIGIBLE
    2.032  x3/4 69 12/12  x5/6 64 12/12  x1 61 13/13  x6/5 58 13/13  x4/3 55 13/13  ELIGIBLE
    2.033  x3/4 69 12/12  x5/6 64 12/12  x1 61 13/13  x6/5 58 13/13  x4/3 55 13/13  ELIGIBLE
    2.034  x3/4 69 12/12  x5/6 64 12/12  x1 61 13/13  x6/5 58 13/13  x4/3 55 13/13  ELIGIBLE
    2.035  x3/4 69 12/12  x5/6 64 13/13  x1 61 13/13  x6/5 58 13/13  x4/3 55 13/13  ELIGIBLE
    2.036  x3/4 69 12/12  x5/6 64 13/13  x1 61 13/13  x6/5 58 14/14  x4/3 55 13/13  ELIGIBLE
    2.037  x3/4 69 12/12  x5/6 64 13/13  x1 61 13/13  x6/5 58 14/14  x4/3 55 13/13  ELIGIBLE
    2.038  x3/4 69 12/12  x5/6 64 13/13  x1 61 13/13  x6/5 58 14/14  x4/3 55 13/13  ELIGIBLE
    2.039  x3/4 69 12/12  x5/6 64 13/13  x1 61 13/13  x6/5 58 13/13  x4/3 55 13/13  ELIGIBLE
    2.041  x3/4 69 12/12  x5/6 64 13/13  x1 61 13/13  x6/5 58 13/13  x4/3 55 13/13  ELIGIBLE
    2.042  x3/4 69 12/12  x5/6 64 13/13  x1 61 13/13  x6/5 58 13/13  x4/3 55 13/13  ELIGIBLE
    2.043  x3/4 69 12/12  x5/6 64 13/13  x1 61 13/13  x6/5 58 13/13  x4/3 55 13/13  ELIGIBLE
    2.044  x3/4 69 12/12  x5/6 64 13/13  x1 61 13/13  x6/5 58 13/13  x4/3 55 12/12  ELIGIBLE
    2.045  x3/4 69 12/12  x5/6 64 13/13  x1 61 14/14  x6/5 58 13/13  x4/3 55 12/12  ELIGIBLE
    2.046  x3/4 69 12/12  x5/6 64 13/13  x1 61 14/14  x6/5 58 13/13  x4/3 55 12/11  ELIGIBLE
    2.047  x3/4 69 12/12  x5/6 64 13/13  x1 61 14/14  x6/5 58 13/13  x4/3 55 12/10  ELIGIBLE
    2.048  x3/4 69 12/12  x5/6 64 13/13  x1 61 14/14  x6/5 58 13/13  x4/3 55 12/10  ELIGIBLE
    2.049  x3/4 69 12/12  x5/6 64 13/13  x1 61 14/14  x6/5 58 13/13  x4/3 55 12/8  ELIGIBLE
  creneau BN : 7 w2 eligibles sur 8
    1.916  x1 60 11/1/10 !  INELIGIBLE
    1.917  x1 60 11/5/6  ELIGIBLE
    1.918  x1 60 11/3/8  ELIGIBLE
    1.919  x1 60 11/5/6  ELIGIBLE
    1.921  x1 60 11/6/5  ELIGIBLE
    1.922  x1 60 11/6/5  ELIGIBLE
    1.923  x1 60 11/7/4  ELIGIBLE
    1.924  x1 60 11/7/4  ELIGIBLE
  creneau BP : 9 w2 eligibles sur 9
    2.061  x1 61 14/11/3  ELIGIBLE
    2.062  x1 61 14/8/6  ELIGIBLE
    2.063  x1 61 14/7/7  ELIGIBLE
    2.064  x1 61 14/6/8  ELIGIBLE
    2.065  x1 61 14/6/8  ELIGIBLE
    2.066  x1 61 14/7/7  ELIGIBLE
    2.067  x1 61 14/6/8  ELIGIBLE
    2.068  x1 61 14/9/5  ELIGIBLE
    2.069  x1 61 14/7/7  ELIGIBLE
  Un point d'exclamation marque une cellule ineligible. Largeurs predites des etiquettes jugeables
  de ces cellules : de 1e-12 a 1e-5.

8. CE QUE MACHINE 2 CERTIFIE
  (a) que les creneaux, le tirage et la regle des rangs sont ceux de sa proposition (lot
      548fb2ba8793ecfe, section 4), aux ecarts declares en section 10 ;
  (b) que les definitions de la section 4 suffisent a calculer l'eligibilite sans lire le code de
      machine 1 ;
  (c) SA table d'eligibilite des 152 cellules, par sa chaine ; et la table commune qui en resulte
      ;
  (d) que son tirage, sur la graine de demonstration, rend les memes numeros que la section 3 et
      que le journal d'autotest.

9. LA SUITE, DANS L'ORDRE
  (1) machine 2 certifie cette piece et rend sa table ; la table commune existe ;
  (2) l'operateur donne la graine aux deux machines ;
  (3) chaque machine tire ; les douze cellules sont les memes, ou PAS DE GEL ;
  (4) machine 1 ecrit la seconde partie : l'instrument (un run, deux etages, les quatre conditions
      de la reponse de machine 2), la table gelee des douze points, la feuille d'ordre 3 et son
      banc, les enonces E1 a E3 avec la cellule pour unite, ce que chaque issue engage, et les
      tolerances et probabilites, calculees sur les chaines aux douze cellules, sans aucune
      largeur 2D ;
  (5) machine 2 certifie la seconde partie et, a zero morsure, joue.

10. CE QUE CETTE PIECE NE FAIT PAS, ET SES ECARTS A LA PROPOSITION DE MACHINE 2
  - Elle ne tire rien et ne connait aucune graine.
  - Elle ne dit pas ce que vaut une cellule ou moins de cinq etats LUS seront dans le domaine :
    l'eligibilite porte sur des etiquettes predites, le jugement portera sur les etats lus. C'est
    a la seconde partie de le dire, avant le run.
  - Ecart 1 : la regle de bord (4.6) est ecrite ici ; machine 2 en avait donne l'idee ("au moins
    deux etats de chaque cote de la garde").
  - Ecart 2 : machine 2 ecrivait "Si les deux machines ne s'accordent pas sur l'eligibilite d'un
    tirage, pas de gel". Ici le desaccord est regle AVANT la graine, par le ET des deux tables
    (section 5).
  - Ecart 3 : "au moins six chiffres" pour la graine est ajoute par machine 1.
  - Le bloc d'ordre 3 est celui du lot e93f1898dcd78a8f, inchange ; la definition du hamiltonien
    effectif est la sienne (forme symetrique). Machine 2 a note qu'une autre definition
    deplacerait un peu la largeur d'une chaine tronquee : non chiffre ici.

11. PIECES DE CE LOT (convention B)
    8ae603f6af71abd7  eligibilite_creneaux_machine1_v1.py
    0d1ba49520ed8523  retouches_eligibilite_creneaux_machine1_v1.diff
    12b2c009bfc53941  eligibilite_N_BN_BP_v1.log
    2a94e82159a2076c  eligibilite_N_BN_BP_v1.json
    48a6033a7e94b9a6  eligibilite_P_v1.log
    aa2fe4e7713e0292  eligibilite_P_v1.json
    d52c0b2b01ee825f  lecture_eligibilite_machine1_v1.py
    33e4def1037726f6  lecture_eligibilite_machine1_v1.log
    f11ac4458a336650  eligibilite_candidates_v1.json
    0f608f8ade6ff378  tirage_machine1_v1.py
    e5a079380537398d  tirage_machine1_v1_autotest.log
    (ce script)       construction_regle_tirage_machine1_v1.py

