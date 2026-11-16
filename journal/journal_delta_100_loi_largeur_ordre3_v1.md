DELTA nn -- LOI DE LA LARGEUR, CHAINE D'ORDRE 3 : RUN DU 16/11/2026 SOUS LE GEL EN DEUX PARTIES
b56ca5cb2dd25da1 (REGLE DE TIRAGE) ET 543d8b33e5c9afb8 (INSTRUMENT, ENONCES).
VERDICT : E1 TENU, E2 TENU, E1B TENU, E3 TENU.
-- PROJET, VERSION 1
(plume machine 1 ; certification, run et seconde feuille machine 2 ; a contresigner par machine 2)
=======================================================================

nn.0 POSITION
  Ce delta rend le run unique du gel "loi de la largeur, ordre 3". Sa question : la chaine a une
  dimension poussee a l'ordre 3, qui rendait la largeur de plateau a quelques centiemes pres sur
  131 etats de points deja joues, la rend-elle a des points que personne n'a choisis ? Douze
  cellules ont ete tirees au sort par une graine de l'operateur (200482) : cinq couplages a delta
  = -0.065, cinq a delta = +0.035, et deux cellules de bord a delta = -0.076 et +0.067.
  Reponse de la feuille du run : E1 TENU (dix cellules de ligne sur dix), E2 TENU (cinq sur cinq),
  E1B TENU (les deux bords), E3 TENU (douze sur douze). Aucune cellule n'est tombee, aucune n'est
  inexploitable. 144 etats lus, tous QUALIFIES par le lecteur ; 141 juges, dont 129 dans le
  domaine. Machine 1 a rejoue les feuilles sur sa machine : memes issues, memes comptes, memes
  etats.
  A savoir avant tout le reste : la cellule de bord BP tient a 0.000383 pres (|ln q3| = 0.099617
  pour une tolerance de 0.10). Elle est A LA LIMITE. Elle ne change pas l'issue de E1 (gel,
  section 8).

nn.1 CE QUI A ETE JOUE, ET DANS QUEL ORDRE
  Premiere partie du gel (b56ca5cb2dd25da1, regle de tirage) : certifiee par machine 2 a zero
  morsure (lot 4fb1dc66f96f57f6). Graine donnee par l'operateur, tirage identique sur les deux
  machines (lot 220a0970134335e1). Seconde partie (543d8b33e5c9afb8, lot 76ed746ef4db3b0c) :
  certifiee par machine 2 AVANT le run (lot 5a5ba910be8b3b29) : aucune morsure d'instrument ; une
  morsure de description sans effet (O-1, nn.9) ; quatre reserves sans correction (nn.9). Son
  pre-vol sur BOCAL4 avec les pieces finales tient 5 sur 5.
  Feu vert. Machine 2 rapporte que l'operateur lui a ecrit, vers 1 h le 16/11 : "Tu peux
  considerer que tu as mon feu vert pour lancer, car je vais me coucher et je veux que ca avance
  dans la nuit, ok ? Evidemment si et seulement si la certification est ok pour toi". Machine 1
  n'a pas vu ce message ; l'operateur lui a seulement dit, a 01 h 01, qu'il pensait machine 2 deja
  partie sur le run. C'est a l'operateur de l'attester.
  Run. UN run, dans un dossier neuf, lance le 2026-11-16 a 01:49:18 et fini a 03:32:04 ; duree
  totale 6166 s ; 19 appels, tous au code 0 ; aucun arret, aucune relance (journal du pilote,
  125ebdb9027a3dfb). Table jouee : 35fa7b73f2b7f8eb, sans --prevol. Les douze canons que le pilote
  imprime au depart sont ceux du gel. Durees : sonde dense 1548 s ; les douze points du lecteur de
  3329 a 3805 s, en parallele ; feuille d'ordre 3 56 s.
  Pilote. Machine 2 a joue un pilote DERIVE de celui du gel (15998497f3422765, derive de
  2882de31bc49ce2f ; reserve R-2). Machine 1 a compare les deux textes : trois blocs different, et
  eux seuls. Les sous-processus sont lances avec -P au lieu de -I (numpy est dans le site
  utilisateur de BOCAL4) ; les fils BLAS valent 1 pour tous les appels sauf la sonde dense, qui
  garde les fils par defaut comme au depot du delta 98 ; un paragraphe d'en-tete. La condition C1
  est gardee ; le pilote n'est pas une piece dont une garde verifie le canon. Machine 1 l'accepte
  : le gel le permettait (note d'accompagnement, M-11).
  E19. Machine 1 n'a calcule aucune largeur 2D a l'une des douze cellules, ni avant ni apres le
  run : son rejeu ne joue que les feuilles. Machine 2 declare n'en avoir calcule aucune en dehors
  du run, et n'avoir rejoue aucun appel apres lecture de sa sortie.

nn.2 L'INSTRUMENT
  Ancres de la sonde dense contre le depot du delta 98 : 2 ancres, 0 ecart. Instrument du lecteur
  (etage 0, ancres, etage 1) : TIENT. Le lecteur a lu 144 etats aux douze cellules ; les 144 sont
  QUALIFIES ; son verdict de cascade, que ce gel ne juge pas, est "ESTIMATEUR QUALIFIE". La
  lecture deposee a k = 3 est sur le plateau a 142 etats sur 144.
  Sorties du run (convention B) : sortie dense 7fb8ad918c8ba795 ; verdict de l'instrument du
  lecteur d5d3880d73a2d3d7 ; verdict du lecteur 158fc924414ddbca ; verdict d'ordre 3
  87e9221cfc5f8f9b.

nn.3 LE VERDICT DE LA FEUILLE DU RUN
  Par cellule : etats lus / juges / dans le domaine / hors du domaine ; E1 (ou E1B aux bords), E2,
  E3 ; plus grand |ln q3| du domaine ; plus petite marge T - |ln q3| ; plus grand |ln q2|.
    N1  11 / 11 / 11 /  0   TIENT TIENT TIENT   |ln q3| 0.0740   marge +0.0260   |ln q2| 0.1048
    N2  11 / 11 / 11 /  0   TIENT TIENT TIENT   |ln q3| 0.0427   marge +0.0573   |ln q2| 0.0987
    N3  12 / 11 / 11 /  0   TIENT TIENT TIENT   |ln q3| 0.0355   marge +0.0645   |ln q2| 0.0841
    N4  14 / 14 / 14 /  0   TIENT TIENT TIENT   |ln q3| 0.0208   marge +0.0422   |ln q2| 0.0747
    N5  14 / 13 / 13 /  0   TIENT TIENT TIENT   |ln q3| 0.0157   marge +0.0476   |ln q2| 0.0699
    P1   9 /  9 /  9 /  0   TIENT -     TIENT   |ln q3| 0.0336   marge +0.0164   |ln q2| 0.0493
    P2  10 / 10 / 10 /  0   TIENT -     TIENT   |ln q3| 0.0302   marge +0.0198   |ln q2| 0.0470
    P3  12 / 12 / 12 /  0   TIENT -     TIENT   |ln q3| 0.0219   marge +0.0281   |ln q2| 0.0392
    P4  13 / 13 / 13 /  0   TIENT -     TIENT   |ln q3| 0.0217   marge +0.0283   |ln q2| 0.0387
    P5  13 / 13 / 13 /  0   TIENT -     TIENT   |ln q3| 0.0201   marge +0.0299   |ln q2| 0.0362
    BN  12 / 11 /  7 /  4   TIENT -     TIENT   |ln q3| 0.0461   marge +0.0539   |ln q2| 0.1106
    BP  13 / 13 /  5 /  8   TIENT -     TIENT   |ln q3| 0.0996   marge +0.0004   |ln q2| 0.1204
  E1 : TENU (10 cellules, 10 exploitables, aucune tombee). E2 : TENU (5 cellules, 5 exploitables,
  aucune tombee). E1B : TENU (2 cellules, 2 exploitables, aucune tombee). E3 : TENU (12 cellules,
  aucune tombee). Etats : 144 lus, 141 juges, 129 dans le domaine, 12 hors. Trois etats lus ne
  sont pas juges, tous pour "barriere vide" : N3 rang 12, N5 rang 13, BN rang 13.

nn.4 LE REJEU DE MACHINE 1 (etape 5 du gel)
  Lot de resultat authentifie : 54ccae1713f92bc9, 56 pieces sur 56. Lot de certification :
  5a5ba910be8b3b29, 79 sur 79.
  Feuille du lecteur, rejouee sur une copie des fichiers du run (etapes "instrument" et "verdict")
  : memes etats, memes statuts ; les deux journaux de lecture sont identiques ligne a ligne. Les
  deux verdicts ne sont pas identiques a l'octet : fins de ligne de Windows, et dernier chiffre de
  quelques largeurs de plateau (plus grand ecart relatif : 7.3e-15).
  Feuille d'ordre 3, rejouee sur la sortie dense et le verdict du lecteur du run : memes issues,
  memes comptes, memes cellules, memes exclusions, memes domaines, etat par etat. Plus grands
  ecarts entre les deux machines sur les 141 etats juges : 1.6e-09 sur ln q3, 1.1e-09 sur ln q2,
  1.7e-09 sur la stabilite ; e_bord identique. La plus petite marge du run (BP) vaut plus de cent
  mille fois cet ecart : la regle "deux machines" du gel (lecture la moins favorable) n'a pas a
  jouer. Rejouee aussi sur le verdict du lecteur de machine 1 : memes issues.
  Hors verdict, machine 2 a joue sa seconde feuille (adf4418505262df6, ecrite des sections 5 et 6
  du gel seules, avec ses propres chaines) sur les fichiers du run : aucune difference sur les 141
  etats juges. C'est une seconde ecriture sur la meme machine, pas une seconde machine.

nn.5 LECTURE, ENONCE PAR ENONCE
  E1. Aux dix cellules de ligne, 117 etats juges du domaine ; |ln q3| vaut 0.0175 en mediane et
  0.0740 au plus (N1). Par classe de e_bord, bords compris (129 etats) : [0, 0.3[ : 40 etats,
  mediane 0.0166, plus grand 0.0336 ; [0.3, 0.5[ : 59, 0.0160, 0.0770 ; [0.5, 0.7[ : 30, 0.0411,
  0.0996. La plus petite marge d'une cellule de ligne est +0.0164, a P1 : un etat de e_bord < 0.3
  a |ln q3| = 0.0336 pour T = 0.05. N1, que la plume annoncait comme le point dur, tient avec
  +0.0260 de marge.
  E2. Sur la ligne N, l'ordre 3 est plus pres du plateau que l'ordre 2 a 60 etats juges du domaine
  sur 60 : N1 11 sur 11, N2 11 sur 11, N3 11 sur 11, N4 14 sur 14, N5 13 sur 13. L'ordre 2 y est
  trop grand (ln q2 median de +0.0627 a +0.1026 selon la cellule), l'ordre 3 trop petit (ln q3
  median de -0.0464 a -0.0094).
  E1B. BN (delta = -0.076) : 7 etats du domaine, |ln q3| au plus 0.0461, marge +0.0539. BP (delta
  = +0.067) : 5 etats du domaine, ln q3 de +0.0768 a +0.0996 ; le plus grand, a l'etat de rang 3,
  vaut 0.099617 pour T = 0.10 : marge +0.000383. BP TIENT selon la regle gelee, et l'acte n'en dit
  pas plus : a cette cellule l'erreur de l'ordre 3 EST la tolerance. Ce verdict ne tient pas aux
  gardes : les 8 etats de BP qui sont hors du domaine ont tous |ln q3| <= 0.0948, sous la
  tolerance eux aussi ; il tient au seul etat de rang 3. Plus petites distances d'un etat juge a
  une garde, dans tout le run : 0.0100 a e_bord = 0.7 (BP rang 5), 0.0041 a la stabilite 0.05 (BP
  rang 4).
  E3. L'ordre 2 est dans la borne du delta 98 aux 141 etats juges : ligne N (borne 1.6), |ln q2|
  au plus 0.1048 ; ligne P (borne 1.25), au plus 0.0493 ; BN 0.1106 ; BP 0.1204. La plus petite
  marge en logarithme est 0.173, sur la ligne P.

nn.6 CE QUI ETAIT CONSIGNE SANS ETRE JUGE
  Signe de ln q3 dans le domaine : ligne N, negatif a 58 etats sur 60 ; ligne P, positif a 57 sur
  57 ; BN negatif a ses 7 etats ; BP positif a ses 5 etats. L'ordre 3 corrige trop a delta < 0 et
  pas assez a delta > 0, comme aux points deja joues.
  Hors du domaine : 12 etats juges (BN 4, BP 8), de e_bord 0.489 a 0.711 ; 10 ne sortent du
  domaine que par la garde de stabilite. L'ordre 3 n'y est plus loin que l'ordre 2 a AUCUN : |ln
  q3| au plus 0.0948, |ln q2| au plus 0.1204. Le second volet que la note de la carte donnait a E3
  (hors du domaine, l'ordre 3 declare non applicable) n'est donc pas ce qu'on observe a ces deux
  bords ; ce n'etait pas un enonce. A la ligne P, l'ordre 3 est plus pres que l'ordre 2 aux 57
  etats du domaine ; ce n'etait pas un enonce non plus, et les deux ordres n'y different que peu
  (gel, section 6).
  Statut des points par la feuille du lecteur : "ESTIMATEUR QUALIFIE". Etiquettes : 132 des 144
  etats lus portent une etiquette parmi les quatorze predites de leur cellule. La superposition
  des deux lignes en Gamma / |delta| n'est pas calculee ici (gel, E-1).

nn.7 LES ANNONCES ET LES ATTENTES DE LA PLUME, CONFRONTEES AU RUN
  Annonces (gel, section 10). A-1 (0.90, l'instrument tient) : il tient. A-2 : la plume donnait
  0.35 a "E1 TENU" et 0.40 a "TENU SAUF UNE CELLULE" : c'est E1 TENU. A-3 : elle donnait 0.45 a la
  chute de N1 : N1 tient. A-4 : 0.50 a "E2 TENU" : c'est E2 TENU. A-5 (0.85, E3 TENU) : tenu. A-6
  : BN tient (annonce 0.65) ; BP tient (annonce 0.40), a la limite. A-7 (0.80, les signes) :
  observe. La plume etait pessimiste sur N1 : elle annoncait que l'issue la plus probable n'etait
  PAS un E1 tenu partout, et c'est un E1 tenu partout qui est sorti.
  Regularite a delta < 0 (gel, 7.2) : k = -ln q3 / (ln(G3 / G2))^2. Avant le run : mediane 1.99,
  au plus 3.24. Aux 67 etats du domaine du run a delta < 0 : mediane 2.03, au plus 2.85 ; aucun
  etat au-dessus de 3.24. Les attentes de 7.3, ecrites avec la valeur la plus defavorable, sont
  tenues aux six cellules de ce cote : le realise est sous l'attente a N1 (0.0740 pour 0.0866),
  N2, N3, N4, N5 et BN.
  Regularites a delta > 0 (gel, 7.2) : elles NE TIENNENT PAS comme bornes. ln q3 / delta^3 atteint
  784 (avant le run : au plus 493) et depasse l'ancien maximum a 15 etats sur 62 ; ln q3 / delta^2
  atteint 27.4 (avant : au plus 15.0) et le depasse a 28 etats. Le realise est au-dessus de
  l'attente de 7.3 a 4 cellules de la ligne P sur cinq (P1, P2, P3, P4) : 0.0336 a P1 pour une
  attente de 0.0211. Sur la ligne P, le plus grand |ln q3| d'une cellule croit quand le couplage
  baisse (de 0.0201 au facteur 4/3 a 0.0336 au facteur 3/4) ; la mediane, elle, bouge peu (de
  0.0134 a 0.0210). Les trois points joues a delta > 0 etaient tous au facteur 1 ou au-dessus et
  ne pouvaient pas le montrer. Tout reste sous la tolerance. A BP, le realise (0.0996) est entre
  les deux attentes (0.0672 et 0.1481).
  Etats au-dela du plus grand e_bord vu avant le run (0.603) : 5 etats du domaine (N1 rang 1, N1
  rang 3, BP rang 1, BP rang 3, BP rang 10) ; |ln q3| de 0.0722 a 0.0996. La garde e_bord < 0.7 y
  etait eprouvee pour la premiere fois : elle tient a N1, et a BP elle tient a la limite.

nn.8 CE QUE CET ACTE ECRIT, ET CE QU'IL N'ECRIT PAS (gel, section 8)
  E1 TENU et E2 TENU. L'acte ecrit donc la phrase que le gel autorisait : a douze cellules tirees
  au sort, la chaine d'ordre 3 rend la largeur de plateau des etats juges du domaine a 0.05 pres
  en logarithme (e_bord < 0.3) et a 0.10 pres au-dela, et elle est plus pres que l'ordre 2 sur la
  ligne negative.
  Le bloc d'ordre 3 (534ba246aa3b8973) peut etre propose au depot ; la decision est a l'operateur.
  Il n'ecrit PAS : une loi en delta (un seul w2 par ligne) ; que la tolerance est large (BP est a
  la limite, et P1 a 0.0336 pour 0.05) ; que l'ordre 3 est JUGE meilleur que l'ordre 2 a delta > 0
  (c'est observe, nn.6 ; ce n'etait pas un enonce) ; que le domaine s'etend au-dela des gardes ;
  rien sur une autre definition du hamiltonien effectif. Aucun seuil, aucune garde, aucune
  tolerance n'a ete regle apres lecture.

nn.9 RESERVES DE MACHINE 2, ECARTS
  O-1 (morsure de description de machine 2, acceptee). Le gel ecrit, section 6, que |ln(G3 / G2)|
  va "de 0.066 a 0.164" aux etiquettes predites de la ligne N. Le plus grand est 0.16338 : la
  plume l'avait arrondi par exces. Il se lit 0.163. Rien n'en depend.
  R-1 (E2 adouci apres lecture des marges). Machine 2 demandait les deux lectures de E2. Lecture
  du gel (une cellule tombee donnerait TENU SAUF UNE CELLULE) : TENU. Lecture stricte (une cellule
  tombee donnerait TOMBE) : TENU. Aucune cellule de la ligne N n'est tombee ni inexploitable :
  l'adoucissement n'a pas joue.
  R-2 (pilote derive) : accepte, nn.1. R-3 (la regle des marges n'etait ecrite que dans le script)
  : exact ; elle est redite en nn.7. R-4 : l'acte du gel ter reste contresigne et non depose ; la
  reference de ce run est donc toujours un lecteur dont l'acte est hors registre (gel, L-2).
  Ecart de la plume : le gel (section 11) citait 2.2e-05 en relatif comme ecart de chaine entre
  les deux machines, mesure aux ancres au gel du delta 98. Sur ce run il est de 1.6e-09 sur ln q3.
  La plume avait cite le plus grand ecart du moteur, pas celui des blocs d'ordre 2 et 3 qui font
  la largeur jugee.

nn.10 LIMITES
  Celles du gel, section 13, restent : un seul w2 par ligne ; la reference est le lecteur du gel
    ter ; l'objet juge est UNE chaine, forme symetrique ; les tolerances sont lues sur des points
    joues, pas tirees d'une theorie.
  BP tient a 0.000383 pres. Un run a un autre w2 du meme creneau pourrait tomber ; l'acte ne dit
    pas ou passe le bord du domaine a delta > 0.
  A delta > 0 le plus grand ecart de l'ordre 3 croit quand le couplage baisse, et la ligne P
    s'arrete au facteur 3/4 : rien n'est dit en dessous.
  P1 et P2 n'ont que 9 et 10 etats lus (12 et 13 predits dans le domaine) : aux faibles couplages,
    moins d'etats depassent dix planchers que la chaine ne le predisait.
  Le feu vert de l'operateur est rapporte par machine 2 ; machine 1 ne l'a pas vu.

nn.11 SUITE
  Contreseing de machine 2. Depot : a la decision de l'operateur, numero pris au depot (E18) ;
  l'acte du gel ter, contresigne, est a deposer avant ou avec celui-ci, puisque ce run s'appuie
  sur son lecteur. Ce gel ne se rejoue pas.

nn.12 PIECES (convention B)
    b56ca5cb2dd25da1 gel, premiere partie (lot 596a45bf6d4f97d7)
    543d8b33e5c9afb8 gel, seconde partie (lot 76ed746ef4db3b0c)
    5a5ba910be8b3b29 lot de machine 2 : certification de la seconde partie
    54ccae1713f92bc9 lot de machine 2 : resultat du run
    89914c76edb0453c sa note de certification
    0adbc286a08c56ad sa note de resultat
    125ebdb9027a3dfb journal du pilote du run
    15998497f3422765 pilote joue (derive par machine 2)
    7fb8ad918c8ba795 sortie dense du run
    d5d3880d73a2d3d7 verdict de l'instrument du lecteur
    158fc924414ddbca verdict du lecteur
    87e9221cfc5f8f9b verdict d'ordre 3 du run
    a34e5369e36bd10b verdict d'ordre 3 rejoue par machine 1
    b0fcb117f8d5107e verdict du lecteur rejoue par machine 1

-- FIN journal_delta_nn_loi_largeur_ordre3_v1 --
