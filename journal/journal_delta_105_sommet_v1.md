DELTA nn -- LARGEUR DU VIDE AU SOMMET DU PROFIL, DE KAPPA = 0.0363 A KAPPA = 1 :
RUN DU 23/11/2026 SOUS LE GEL EN DEUX PARTIES 1e5039cade55d13f (REGLE DE TIRAGE) ET
81a2febcfce49007 (INSTRUMENT, ENONCE).
VERDICT : S1 TENU.
-- PROJET, VERSION 1
(plume machine 1 ; certifications, run et juge independant machine 2 ; a contresigner par machine 2)
=======================================================================

nn.0 POSITION
  Ce delta rend le run unique du gel "sommet". Le delta 102 avait montre que la chaine a une
  dimension rend la largeur de l'etat que porte le site (0, 0), le vide, aux ailes de la resonance
  2:1 : trois a seize barreaux de barriere, |delta| de 0.003 a 0.018, kappa au plus 0.0262. La
  question de ce gel : la rend-elle encore au sommet, de deux barreaux jusqu'a la fenetre sans
  barriere, la ou le saut au pied de l'echelle vaut jusqu'au desaccord lui-meme, a des cellules que
  personne n'a choisies ? Cinquante-six cellules ont ete tirees par une graine de l'operateur
  (114565) : huit w2 (1.99989, 1.99993, 2.00008, 2.00011, 1.99968, 1.99956, 2.00039, 2.00048), sept
  kappa chacun (0.0363, 0.0530, 0.0800, 0.1300, 0.2000, 0.4000, 1.0000). Les predictions etaient
  gelees dans une table (4238e2b262119f83) avant toute lecture.
  Reponse de la feuille du run : S1 TENU. Cinquante-six cellules lues, cinquante-six tenues ; aucune
  n'est tombee, aucune n'est non jugeable, aucune n'est non lue ; sept tenues sur sept a chaque w2,
  huit sur huit a chaque kappa ; la portee est les sept kappa. Machine 1 a rejoue la feuille sur les
  fichiers du run : meme verdict, memes 56 jugements.
  A savoir avant tout le reste. (1) L'ecart de la chaine au plateau lu, |ln q|, vaut 0.00025 au plus
  (PPb2), pour une tolerance de 0.01, a des largeurs de 4.68e-10 a 2.48e-04 et des couplages de
  2.48901e-05 a 4.71149e-03. (2) Cet ecart est sous l'etendue de la chaine a 56 cellules sur 56 : le
  gel est tenu a sa tolerance, et il ne MESURE pas l'erreur de la chaine en dessous de ce que son
  absorbeur laisse indetermine. (3) Il n'oppose pas les ordres de la chaine. (4) Cinquante-six
  cellules sont HUIT tirages, tous a |delta| de 0.00048 au plus : ce gel et le delta 102 ne se
  recouvrent pas (nn.8). (5) La largeur jugee est celle d'un etat sous absorbeur ; cet acte ne dit
  rien de la duree de vie du systeme ferme.

nn.1 CE QUI A ETE JOUE, ET DANS QUEL ORDRE
  Ouverture. L'operateur a ecrit a machine 1 "je dis oui on ouvre. Par contre tous les calculs
  couteux, c'est sur machine 2 ok ?" (22/11/2026, 20 h 09) : declaration de machine 1. A l'operateur
  de l'attester. Depuis, machine 1 n'a fait aucun calcul a deux dimensions.
  Qualifications. Avant le gel, machine 2 a lu le vide en 2D a neuf points declares sacrifies avant
  toute lecture (w2 = 2 a trois couplages ; w2 = 20001/10000 et 19999/10000), sur des mots de
  l'operateur qu'elle rapporte ("Oui GO !", "oui ces 4 pts") ; machine 1 avait ecrit ses attendus
  avant ; ils ont tenu (lots c58c2b3f533c516b et 295b2b1549b076c2 de machine 2, 423ec0fd24240977 et
  074b131287ad2b6f de machine 1). Ces neuf points ne sont pas des cellules ; ils sont les temoins
  positifs du run.
  Premiere partie du gel (1e5039cade55d13f, regle de tirage et d'eligibilite, lot
  3ba4618d7976c6ea) : certifiee par machine 2 sans refus (lot 21e9bddfe5db83b2, 22 pieces) ; sa
  table des 560 cellules candidates, ecrite du texte, est celle de machine 1 octet pour octet (table
  commune 77ce2a6c7e867011).
  Graine. L'operateur a ecrit a machine 1 "graine 114565" (22/11, 23 h 21), apres lui avoir remis
  cette certification. Machine 2 rapporte qu'il lui a ecrit la meme graine apres son compte rendu de
  certification. Les deux machines ont tire chacune par son code, sans avoir lu le tirage de
  l'autre : memes huit w2, memes 56 cellules, memes trois nombres ecrits par cellule (lot
  3db782eea5023b31 de machine 2 ; comparaison de machine 1, 56 sur 56).
  Seconde partie (81a2febcfce49007, instrument, enonce, tolerances, lot a2dc5cb2b9c3da0d) :
  certifiee par machine 2 (lot b7f328b916ba720d, 62 pieces) aux six points demandes, sans correction
  demandee, avec cinq remarques non bloquantes (nn.9) ; AVANT le run d'apres ses pieces (son pre-vol
  finit a 00:05:47, le run part a 00:16:01) ; machine 1 ne l'a lue qu'apres (ci-dessous). Son propre
  juge, ecrit du texte des sections 5 et 6, rend les memes resultats que la feuille du gel a 38
  scenarios sur 38 ; les deux bancs de machine 1 rejouent chez elle (30 cas sur 30, 12 sur 12). Elle
  a joue le PRE-VOL sur un mot de l'operateur qu'elle rapporte ("GO") : etage A, neuf temoins,
  garde ; aucune cellule lue ; l'instrument tient, les neuf temoins rendent leur reference, 1120 s.
  C'etait la premiere execution reelle du pilote de machine 1.
  Feu vert. Machine 2 rapporte qu'apres sa certification elle a dit a l'operateur que le run
  attendait son feu vert ecrit, et qu'il a ecrit : "RUn". Machine 1 n'a pas vu ce message. A
  l'operateur de l'attester.
  Un fait de deroulement. La seconde partie (section 11) prevoyait, apres la certification de
  machine 2, un tour de correction, puis le feu vert. La certification n'est parvenue a machine 1
  que le 23/11 a 1 h 37, APRES le lot de resultat (1 h 15) : le tour n'a pas ete attendu. Il n'avait
  rien a porter : la certification ne demandait aucune correction, machine 1 n'en avait aucune, et
  le run a joue les pieces du gel a leurs empreintes (nn.2). Machine 2 le dit elle-meme dans sa note
  de resultat.
  Run. UN run, dans un dossier neuf, lance le 2026-11-23 00:16:01 et fini a 01:05:05 (heure de
  BOCAL4) ; duree totale 2944 s ; 136 appels, tous au code 0 ; aucun arret, aucune relance. Pilote
  joue : celui du gel, tel quel (ed4c3886b17fcdc3), 12 processus, drapeau -P, sans --prevol. Les
  canons que le pilote imprime au depart sont ceux du gel. Durees : etage A 20 s, 846 s et 897 s
  (etage 0, ancres, etage 1, en parallele) ; les dix-huit lectures des temoins de 129 a 180 s ; les
  112 lectures des cellules de 115 a 206 s, 12 a la fois.
  E19. Machine 1 n'a lu en 2D le systeme a fantome ni le jumeau a aucune cellule ni a aucun w2 tire,
  ni avant ni apres le run : son rejeu ne joue que la feuille. Machine 2 declare n'avoir lu aucune
  cellule avant la fin du pilote.

nn.2 L'INSTRUMENT
  Celui de la seconde partie, section 4, sans changement : etage A (la sonde et la feuille deposees
  du lecteur, d5cc48f48e37af99 et 83701094e6a2b965, sur les pieces du depot) ; etage A' (les neuf
  temoins positifs du sommet) ; la garde (la feuille du gel, etape --temoins, AVANT toute cellule) ;
  etage B (les 56 cellules, le jumeau sans fantome puis le fantome, par le pilote de lecture de
  machine 2, 47a84eae6052f006, qui execute le bloc du lecteur depose) ; etage C (la feuille du gel,
  ac934e0caaa59c08). Table jouee : 4238e2b262119f83.
  Etage A : l'instrument du lecteur TIENT (verdict c11edf7b49007d05). Garde : TIENT
  (707b6d999a2b9100), jouee a 00:36:05, avant la premiere lecture de cellule. Les neuf temoins
  positifs TIENNENT, chacun a 0 de son plateau de reference : c'est le meme code sur la meme
  machine ; ils disent que l'instrument du jour est celui des qualifications, pas qu'il lit juste.
    temoin  w2           g        plateau lu   reference    ln(lu / reference)
    Qa      2            2.5e-4   1.36078e-05  1.36078e-05  +0.0e+00
    Qc      2            1e-3     5.44311e-05  5.44311e-05  +0.0e+00
    Qd      2            2e-3     1.08861e-04  1.08861e-04  +0.0e+00
    Qe      20001/10000  3e-4     1.20926e-05  1.20926e-05  +0.0e+00
    Qf      20001/10000  1.5e-4   2.91446e-06  2.91446e-06  +0.0e+00
    Q2a     20001/10000  6e-5     4.94717e-08  4.94717e-08  +0.0e+00
    Q2b     20001/10000  4e-5     2.05518e-09  2.05518e-09  +0.0e+00
    Q2c     19999/10000  3e-4     1.21073e-05  1.21073e-05  +0.0e+00
    Q2d     19999/10000  1.5e-4   2.92063e-06  2.92063e-06  +0.0e+00

nn.3 LE VERDICT DE LA FEUILLE DU RUN
  Verdict du run : S1 TENU (canon 2c39171a593d95df). Par cellule : le plateau lu sous l'absorbeur A,
  l'etalement s du lecteur, l'etendue de la chaine (table), la bande b = etendue + s, ln q = ln(G3*
  / plateau lu), le jugement. Tolerance T = 0.01 a toutes : la cellule TIENT si |ln q| <= T - b. Les
  56 cellules sont QUALIFIEES et leur temoin tient.
    cellule  w2       kappa   g            plateau lu   s       etendue  bande   ln q      jugement
    MPa1     1.99989  0.0363  3.91071e-05  7.35185e-10  0.0021  0.0034   0.0055  +0.00000  TIENT
    MPa2     1.99989  0.0530  5.70985e-05  1.97574e-08  0.0012  0.0021   0.0032  -0.00024  TIENT
    MPa3     1.99989  0.0800  8.61865e-05  2.63580e-07  0.0009  0.0018   0.0027  -0.00008  TIENT
    MPa4     1.99989  0.1300  1.40053e-04  1.97366e-06  0.0009  0.0024   0.0033  +0.00001  TIENT
    MPa5     1.99989  0.2000  2.15466e-04  6.13451e-06  0.0016  0.0003   0.0019  +0.00010  TIENT
    MPa6     1.99989  0.4000  4.30932e-04  1.95759e-05  0.0008  0.0015   0.0022  -0.00004  TIENT
    MPa7     1.99989  1.0000  1.07733e-03  5.69138e-05  0.0009  0.0030   0.0040  -0.00000  TIENT
    MPb1     1.99993  0.0363  2.48901e-05  4.67848e-10  0.0021  0.0034   0.0054  +0.00001  TIENT
    MPb2     1.99993  0.0530  3.63409e-05  1.25728e-08  0.0012  0.0021   0.0033  -0.00024  TIENT
    MPb3     1.99993  0.0800  5.48542e-05  1.67731e-07  0.0009  0.0017   0.0026  -0.00008  TIENT
    MPb4     1.99993  0.1300  8.91380e-05  1.25595e-06  0.0015  0.0022   0.0037  +0.00001  TIENT
    MPb5     1.99993  0.2000  1.37135e-04  3.90372e-06  0.0001  0.0003   0.0004  +0.00007  TIENT
    MPb6     1.99993  0.4000  2.74271e-04  1.24573e-05  0.0008  0.0019   0.0027  -0.00003  TIENT
    MPb7     1.99993  1.0000  6.85677e-04  3.62175e-05  0.0010  0.0032   0.0042  -0.00002  TIENT
    PPa1     2.00008  0.0363  2.84618e-05  5.34666e-10  0.0021  0.0033   0.0054  +0.00003  TIENT
    PPa2     2.00008  0.0530  4.15558e-05  1.43683e-08  0.0012  0.0024   0.0036  -0.00025  TIENT
    PPa3     2.00008  0.0800  6.27258e-05  1.91683e-07  0.0009  0.0014   0.0023  -0.00010  TIENT
    PPa4     2.00008  0.1300  1.01929e-04  1.43529e-06  0.0015  0.0018   0.0033  +0.00001  TIENT
    PPa5     2.00008  0.2000  1.56814e-04  4.46123e-06  0.0008  0.0017   0.0025  +0.00007  TIENT
    PPa6     2.00008  0.4000  3.13629e-04  1.42365e-05  0.0007  0.0033   0.0040  -0.00004  TIENT
    PPa7     2.00008  1.0000  7.84072e-04  4.13903e-05  0.0020  0.0024   0.0044  -0.00003  TIENT
    PPb1     2.00011  0.0363  3.91394e-05  7.35167e-10  0.0021  0.0033   0.0054  +0.00003  TIENT
    PPb2     2.00011  0.0530  5.71457e-05  1.97563e-08  0.0012  0.0024   0.0037  -0.00025  TIENT
    PPb3     2.00011  0.0800  8.62576e-05  2.63560e-07  0.0009  0.0013   0.0022  -0.00014  TIENT
    PPb4     2.00011  0.1300  1.40169e-04  1.97354e-06  0.0009  0.0017   0.0026  +0.00002  TIENT
    PPb5     2.00011  0.2000  2.15644e-04  6.13417e-06  0.0009  0.0019   0.0028  +0.00007  TIENT
    PPb6     2.00011  0.4000  4.31288e-04  1.95750e-05  0.0008  0.0032   0.0040  -0.00004  TIENT
    PPb7     2.00011  1.0000  1.07822e-03  5.69112e-05  0.0008  0.0031   0.0039  -0.00004  TIENT
    MGa1     1.99968  0.0363  1.13677e-04  2.13887e-09  0.0021  0.0034   0.0055  -0.00005  TIENT
    MGa2     1.99968  0.0530  1.65974e-04  5.74796e-08  0.0005  0.0016   0.0022  -0.00022  TIENT
    MGa3     1.99968  0.0800  2.50527e-04  7.66835e-07  0.0006  0.0023   0.0029  -0.00006  TIENT
    MGa4     1.99968  0.1300  4.07106e-04  5.74193e-06  0.0015  0.0030   0.0045  +0.00002  TIENT
    MGa5     1.99968  0.2000  6.26317e-04  1.78469e-05  0.0015  0.0021   0.0036  +0.00013  TIENT
    MGa6     1.99968  0.4000  1.25263e-03  5.69506e-05  0.0008  0.0026   0.0035  -0.00004  TIENT
    MGa7     1.99968  1.0000  3.13159e-03  1.65573e-04  0.0016  0.0023   0.0039  +0.00006  TIENT
    MGb1     1.99956  0.0363  1.56235e-04  2.94090e-09  0.0021  0.0035   0.0056  -0.00007  TIENT
    MGb2     1.99956  0.0530  2.28112e-04  7.90383e-08  0.0006  0.0013   0.0019  -0.00020  TIENT
    MGb3     1.99956  0.0800  3.44319e-04  1.05443e-06  0.0006  0.0026   0.0033  -0.00006  TIENT
    MGb4     1.99956  0.1300  5.59519e-04  7.89545e-06  0.0008  0.0031   0.0039  +0.00002  TIENT
    MGb5     1.99956  0.2000  8.60799e-04  2.45402e-05  0.0015  0.0027   0.0042  +0.00013  TIENT
    MGb6     1.99956  0.4000  1.72160e-03  7.83098e-05  0.0006  0.0029   0.0035  -0.00002  TIENT
    MGb7     1.99956  1.0000  4.30399e-03  2.27666e-04  0.0009  0.0024   0.0034  +0.00005  TIENT
    PGa1     2.00039  0.0363  1.38913e-04  2.60644e-09  0.0022  0.0031   0.0053  +0.00007  TIENT
    PGa2     2.00039  0.0530  2.02820e-04  7.00386e-08  0.0014  0.0028   0.0041  -0.00025  TIENT
    PGa3     2.00039  0.0800  3.06144e-04  9.34353e-07  0.0010  0.0012   0.0021  -0.00021  TIENT
    PGa4     2.00039  0.1300  4.97483e-04  6.99639e-06  0.0016  0.0010   0.0026  +0.00010  TIENT
    PGa5     2.00039  0.2000  7.65359e-04  2.17468e-05  0.0009  0.0031   0.0041  +0.00009  TIENT
    PGa6     2.00039  0.4000  1.53072e-03  6.93987e-05  0.0008  0.0024   0.0032  -0.00009  TIENT
    PGa7     2.00039  1.0000  3.82680e-03  2.01765e-04  0.0015  0.0021   0.0036  -0.00013  TIENT
    PGb1     2.00048  0.0363  1.71027e-04  3.20777e-09  0.0019  0.0030   0.0049  +0.00008  TIENT
    PGb2     2.00048  0.0530  2.49709e-04  8.61995e-08  0.0008  0.0028   0.0036  -0.00024  TIENT
    PGb3     2.00048  0.0800  3.76919e-04  1.14992e-06  0.0010  0.0014   0.0024  -0.00022  TIENT
    PGb4     2.00048  0.1300  6.12494e-04  8.61072e-06  0.0016  0.0012   0.0029  +0.00009  TIENT
    PGb5     2.00048  0.2000  9.42298e-04  2.67646e-05  0.0017  0.0030   0.0047  +0.00009  TIENT
    PGb6     2.00048  0.4000  1.88460e-03  8.54123e-05  0.0005  0.0026   0.0031  -0.00010  TIENT
    PGb7     2.00048  1.0000  4.71149e-03  2.48322e-04  0.0014  0.0030   0.0044  -0.00014  TIENT
  S1 : TENU. Tenues 56, tombees 0, non jugeables 0, non lues 0. Tenues par w2 (sur sept) : 1.99989
  7 ; 1.99993 7 ; 2.00008 7 ; 2.00011 7 ; 1.99968 7 ; 1.99956 7 ; 2.00039 7 ; 2.00048 7. Tenues par
  kappa (sur huit) : 0.0363 8 ; 0.0530 8 ; 0.0800 8 ; 0.1300 8 ; 0.2000 8 ; 0.4000 8 ; 1.0000 8.
  Portee : 0.0363 0.0530 0.0800 0.1300 0.2000 0.4000 1.0000.
  Lectures. Fantome : 2679 lectures suivies sur 2688 ; les 9 non suivies (MPa7 A k = +8 ; MPb7 D k =
  +8 ; PPa7 A k = +8 ; PPa7 D k = +7 ; PPa7 D k = +8 ; MGa6 A k = +8 ; MGa7 C k = -3 ; MGb7 C k =
  -3 ; PGa7 B k = +8) sont hors des fenetres retenues et n'ont rendu aucune cellule non qualifiee.
  Jumeau : 0 non suivie sur 2688 ; sa plus grande largeur vaut 4.8e-26 du plateau au plus (seuil
  1e-6). Plus petit poids du site (0, 0) sur les lectures suivies du fantome : 0.7181. Sous A, la
  largeur est plate a 0.005 pres aux barreaux k = -3 a 4 a toutes les cellules.

nn.4 LE REJEU DE MACHINE 1 (etape 5 du gel)
  Machine 1 a authentifie le lot de resultat (735b9394013b02db, 284 pieces, aucun ecart) et rejoue
  la feuille du gel, a son canon, sur les 130 fichiers de lecture et le verdict de l'instrument, lus
  comme des donnees ; rien du lot n'est execute. Verdict rejoue : S1 TENU (canon ab4629fe72da3e92) ;
  meme issue, memes comptes, meme portee, memes 56 jugements et statuts ; plus grand ecart sur ln q,
  le plateau, la bande et l'etalement : 3.7e-15 (deux bibliotheques de calcul ; les deux fichiers ne
  sont donc pas identiques a l'octet). Les nombres de cet acte sont ceux du verdict rejoue.
  Le juge independant de machine 2, ecrit du texte du gel avant le run, rejoue par elle sur les
  memes fichiers, rend le meme verdict, la meme portee et les memes jugements cellule par cellule
  (sa note de resultat). Trois lectures du meme run s'accordent ; il n'y a qu'UNE mesure 2D.

nn.5 LECTURE DE L'ENONCE
  S1 tient largement a sa tolerance : la plus grande bande est 0.0056, et la cellule la plus pres de
  sa limite (MGb1) garde 0.0044 entre |ln q| et T - b. Ce que cela ne dit pas : |ln q| est sous
  l'etendue de la chaine a 56 cellules sur 56, et sous l'etalement du lecteur a 56. L'accord a
  quelques dix-milliemes n'est donc pas resolu par ce gel ; il est compatible avec ce que
  l'absorbeur de la chaine laisse indetermine. Et a kappa egal les huit w2 rendent le meme Phi a
  0.0003 pres (nn.6) : ce gel a lu sept valeurs de Phi(kappa), chacune a huit echelles du desaccord
  et du couplage, et non cinquante-six largeurs independantes.

nn.6 CE QUI ETAIT CONSIGNE SANS ETRE JUGE
  Le residu par kappa. ln q n'est pas un bruit : a kappa donne il a le meme signe aux huit w2 a 5
  kappa sur sept. C'est une fonction de kappa de l'ordre de 2e-04, sous l'etendue de la chaine. Rien
  n'en est juge, et cet acte n'en donne pas la cause.
            ln q aux huit w2              negatifs  Phi lu = plateau / |delta|  etalement, ln Phi
    kappa   minimum   maximum   moyenne   sur huit  minimum      maximum      lu       chaine
    0.0363  -0.00007  +0.00008  +0.00001  2         6.68286e-06  6.68398e-06  0.00017  0.00004
    0.0530  -0.00025  -0.00020  -0.00024  8         1.79582e-04  1.79633e-04  0.00028  0.00032
    0.0800  -0.00022  -0.00006  -0.00012  8         2.39568e-03  2.39644e-03  0.00032  0.00048
    0.1300  +0.00001  +0.00010  +0.00003  0         1.79390e-02  1.79442e-02  0.00029  0.00022
    0.2000  +0.00007  +0.00013  +0.00009  0         5.57596e-02  5.57732e-02  0.00024  0.00028
    0.4000  -0.00010  -0.00002  -0.00005  8         1.77942e-01  1.77977e-01  0.00019  0.00027
    1.0000  -0.00014  +0.00006  -0.00003  6         5.17338e-01  5.17423e-01  0.00016  0.00035
  La superposition en kappa. A kappa egal, la largeur lue rapportee au desaccord varie de 0.00032 au
  plus en logarithme entre les huit w2, pour des desaccords de 0.00007 a 0.00048 et les deux
  signes ; la chaine donne 0.00048 au plus. A ces desaccords la loi d'echelle nue, Gamma = |w2 - 2|
  Phi(kappa), se lit donc a quelques dix-milliemes. Ce n'etait PAS le cas aux ailes : au delta 102,
  a profondeur egale, les quatre w2 (|delta| de 0.003 a 0.018) s'ecartaient de 0.0098 a trois
  barreaux jusqu'a 0.1262 a seize, et c'est la chaine qui rendait ces ecarts. Consigne, pas juge.
  Le signe de delta. Le tirage a sorti une paire de w2 miroirs (1.99989 et 2.00011). A kappa egal,
  ln[Phi(delta < 0) / Phi(delta > 0)] lu, et celui de la chaine entre parentheses : 0.0363 +0.00003
  (-0.00001) ; 0.0530 +0.00005 (+0.00006) ; 0.0800 +0.00008 (+0.00014) ; 0.1300 +0.00006
  (+0.00005) ; 0.2000 +0.00006 (+0.00008) ; 0.4000 +0.00005 (+0.00005) ; 1.0000 +0.00005 (+0.00008).
  L'effet du signe est sous 1e-04 ; le lecteur et la chaine s'y accordent a 0.00006 pres.
  Les ordres. L'ordre 3 est plus pres du plateau lu que le premier ordre a 35 cellules sur 56 : le
  gel ne les separe pas, comme sa section 1 l'ecrivait. ln q est negatif (le lecteur au-dessus de la
  chaine) a 32 cellules, et du signe de delta a 28.
  La largeur rapportee au saut au pied de l'echelle, moyenne par kappa : 0.0363 0.0002 ; 0.0530
  0.0034 ; 0.0800 0.0300 ; 0.1300 0.1380 ; 0.2000 0.2788 ; 0.4000 0.4449 ; 1.0000 0.5174. A la
  resonance exacte, lue aux trois temoins positifs de w2 = 2 et non aux cellules, elle vaut 0.5333
  (le saut y est interpole entre les deux w2 miroirs).

nn.7 LES ANNONCES DE LA PLUME, CONFRONTEES AU RUN (gel, section 10)
  A-1 (0.95) l'instrument tient : oui. A-2 (0.97) les neuf temoins positifs tiennent : oui. A-3
    (0.95) le temoin tient aux 56 cellules : oui. A-4 (0.70) le lecteur qualifie les 56 cellules :
    oui.
  A-5 S1 TENU (0.80) : c'est l'issue.
  A-6 (0.75) plus grand |ln q| sous 0.001 : oui (0.00025).
  A-7 (0.70) ln q negatif a douze cellules de barriere au moins sur seize : NON. Il l'est a 10 : aux
    huit de kappa = 0.0530 et a 2 des huit de kappa = 0.0363, ou il est de part et d'autre de zero.
    La plume avait generalise les deux points de barriere des qualifications.
  A-8 (0.65) aux paires miroirs, rapport lu a 0.0001 de celui de la chaine a cinq paires au moins :
    oui (7 sur 7).
  A-9 (0.75) a chaque kappa, etalement de ln(plateau / |delta|) sous 0.001 : oui (0.00032 au plus).
  Huit annonces sur neuf sont du cote annonce ; A-7 tombe. Ce sont des jugements de plume, pas des
  enonces juges. La crainte ecrite, une cellule non lue au bord de ce que le lecteur avait qualifie,
  ne s'est pas realisee.

nn.8 CE QUE CET ACTE ECRIT, ET CE QU'IL N'ECRIT PAS (gel, section 8)
  Il ecrit : a cinquante-six cellules tirees au sort, en huit tirages, pour |delta| de 0.00007 a
  0.00048 et kappa de 0.0363 a 1, la chaine d'ordre 3 des blocs deposes, sous absorbeur adapte, rend
  la largeur de l'etat porte par (0, 0) a 0.01 pres en logarithme, au-dela de sa propre etendue et
  de l'etalement du lecteur.
  Le gel permettait d'ajouter : "avec le delta 102, la loi d'echelle de la largeur du vide est alors
  eprouvee des ailes au sommet". Cet acte ecrit moins, et autrement. (i) Ce que les deux gels
  eprouvent est la CHAINE : aux ailes la loi d'echelle nue s'ecarte du plateau, et c'est la chaine
  qui rend l'ecart (nn.6). (ii) Les deux domaines ne se touchent pas : le delta 102 est a |delta| de
  0.003 a 0.018 et kappa au plus 0.0262 ; ce gel est a |delta| de 0.00048 au plus. Au sommet a
  |delta| plus grand, donc a couplage plus fort (kappa = 1 a |delta| = 0.01 demande g voisin de
  0.1), rien n'est lu.
  Il N'ecrit PAS : que la chaine est exacte (l'ecart est sous son etendue, et il a une structure en
  kappa) ; que l'ordre 3 fait mieux que le premier ordre ; quoi que ce soit de la duree de vie du
  systeme ferme ; quoi que ce soit de w2 = 2 exactement, lu aux seuls temoins positifs, ni au-dela
  de kappa = 1 ; quoi que ce soit du sommet a |delta| au-dela de 0.0005 ; "cinquante-six cellules"
  sans dire "huit tirages" : a kappa egal la chaine ne varie que de 0.0005 d'un w2 a l'autre, et ce
  que la graine a fait varier est le couplage, le signe et l'echelle du desaccord ; que la regle de
  eta0 est la bonne : c'est une convention dans une zone plate.

nn.9 REMARQUES DE MACHINE 2, DEFAUTS DE LA PLUME, ECARTS
  Remarques de machine 2 a sa certification, non bloquantes, sans correction : R-1, devant un
    fichier de cellule malforme la feuille rend "RUN INCOMPLET" avec le code 0 et le pilote ecrit sa
    fin : le verdict se lit dans le fichier, pas a la fin du pilote (c'est ce que fait cet acte) ;
    R-2, le cout ; R-3, le dossier neuf ; R-4, l'etage A eprouve l'instrument aux ailes et sert peu
    au sommet ; R-5, eta0 se reduit a (kappa / 0.0262) |w2 - 2| aux 560 cellules.
  Ecarts du gel, declares dans sa seconde partie et acceptes par machine 2 : E-1 (les neuf temoins
    positifs et la garde s'ajoutent a ce que la premiere partie annoncait) ; E-2 (le pilote de
    lecture est celui de machine 2) ; E-3 (la portee) ; E-4 (le pre-vol sur la table gelee).
  Defauts de la plume de machine 1. D-REL-29 : a la qualification Q, son attendu Q-4 ne pouvait pas
    mordre ; vu par machine 2. D-REL-30 : son esquisse portait deux w2 ou machine 2 avait lu le
    jumeau en 2D le 16/11 ; trouves par balayage et retires AVANT la premiere partie. Son annonce
    A-7 (nn.7). Le champ "poids_min" de sa feuille prend aussi les lectures non suivies (il vaut
    0.5348) : il ne sert a aucun jugement ; le poids dit en nn.3 est relu sur les lectures suivies.
    Son pilote n'avait jamais joue une lecture reelle avant le pre-vol de machine 2 : dit dans le
    gel.
  Le tour de correction non attendu : nn.1.
  Erreurs que machine 2 dit a sa certification : trois criteres de son propre test etaient faux a
    ses deux premiers passages ; la feuille du gel n'avait rien a corriger.

nn.10 LIMITES
  Celles du gel, section 13, restent (L-1 a L-9) : S1 ne separe pas les ordres ; huit tirages ;
    aucun des sept kappa n'avait ete lu en 2D avant le run ; eta0 est une convention ; une seule
    definition du hamiltonien effectif.
  Le domaine : |delta| de 0.00007 a 0.00048, couplages de 2.5e-05 a 4.7e-03. Ce gel et le delta 102
    ne se recouvrent pas (nn.8).
  La 2D des cellules a ete calculee sur une seule machine (BOCAL4), une seule fois, par un pilote de
    lecture ecrit par machine 2. Machine 1 n'en a rejoue aucune. Trois juges ont lu les memes
    fichiers.
  La chaine et la 2D partagent le moteur (82a0be882568fe0c). L'accord eprouve la reduction a une
    dimension et les absorbeurs, pas le moteur ; une erreur commune au lecteur et a la chaine ne se
    verrait pas.
  Les temoins positifs sont le meme code sur la meme machine : ils eprouvent la reproduction, pas
    l'exactitude.
  La largeur est celle d'un etat sous absorbeur, stable sous quatre absorbeurs. Rien n'est dit du
    systeme ferme.
  Les mots de l'operateur a machine 2 (qualifications, pre-vol, feu vert) sont rapportes par elle ;
    l'ouverture et la graine donnee a machine 1 sont des declarations de machine 1.

nn.11 SUITE
  Contreseing de machine 2. Depot : a la decision de l'operateur, numero pris au depot. Ce run
  s'appuie sur des pieces qui ne sont pas au registre : les deux parties du gel et leurs lots (table
  gelee, feuille, pilote, tirage), les lots des qualifications, des certifications, du tirage et du
  resultat, et le pilote de lecture de machine 2. Ce gel ne se rejoue pas.

nn.12 PIECES (convention B)
    1e5039cade55d13f gel, premiere partie (lot 3ba4618d7976c6ea)
    81a2febcfce49007 gel, seconde partie (lot a2dc5cb2b9c3da0d)
    4238e2b262119f83 table gelee des 56 cellules et des neuf temoins
    77ce2a6c7e867011 table commune d'eligibilite
    49a40d9098b55361 bloc de l'absorbeur adapte (registre)
    ac934e0caaa59c08 feuille du gel
    ed4c3886b17fcdc3 pilote du gel, joue tel quel
    47a84eae6052f006 pilote de lecture de machine 2
    c58c2b3f533c516b lot de machine 2 : qualification Q
    295b2b1549b076c2 lot de machine 2 : qualification Q2
    21e9bddfe5db83b2 lot de machine 2 : certification de la premiere partie
    3db782eea5023b31 lot de machine 2 : son tirage
    b7f328b916ba720d lot de machine 2 : certification de la seconde partie, pre-vol
    735b9394013b02db lot de machine 2 : resultat du run
    c46c3aa3977366f4 sa note de certification de la seconde partie
    c462991d2484064c sa note de resultat
    f6382d96633043ff journal du pilote du run
    c11edf7b49007d05 verdict de l'instrument du lecteur
    707b6d999a2b9100 verdict de la garde
    2c39171a593d95df verdict de la feuille du run
    ab4629fe72da3e92 verdict rejoue par machine 1

-- FIN journal_delta_nn_sommet_v1 --
