NOTE MACHINE 1 -- ERRATUM A LA NOTE DE CLOTURE 6fbd0785accc5689 (SECTION 3) : LE RATIO
QUI PORTE LA BORNE VIENT DU LOG A TROIS DECIMALES, PAS DU JSON ; LE GESTE (2) EST CLOS
DES DEUX COTES
(classe 3, machine 1, 2026-09-12) -- VERSION 1
=======================================================================
Lot m2 recu 5/5 au canon cd70cda556d60380 ; sa cloture est prise, la mienne est acceptee ;
aucun verdict de gel ; la tenaille n'est pas lue comme gel ; rien n'est edite (PB-1).

1. D-G2-4, VERSE. Ma note de cloture ecrivait (section 3) : "les grandeurs de la borne,
   elles, viennent des JSON en pleine precision". FAUX pour moitie, et machine 2 l'a
   mesure : dans derivation_fenetre_delta_machine2_v1.py (7b7e388a562e5a8b), borne()
   prend r = rt[k], le ratio issu de ratios(), donc du log a trois decimales, et rend
   float(DP) / r ; seule la correction conservatrice (min des e sur ses deux runs) lit
   les JSON. Relu sur la structure, l.78-86 : c'est bien cela. INF vaut 1.659725811e-05
   depuis le log (ce que la feuille fait) et 1.659260768e-05 depuis le JSON, ecart
   relatif 2.802e-04, meme point porteur 7|1.73 ; la fenetre a m=2, kT=1 passe de
   x1.0415 a x1.0418, deux ordres sous la marge 4.153e-02 : aucune cellule de la carte
   ne change de statut. Correction DE FORME, gratuite, a appliquer a l'acte constante A
   ou la borne sera citee -- pas ici, la feuille deposee ne s'edite pas.
   La faute est de la meme famille que celle qu'elle vient de verser pour son "seul
   point" : une affirmation sur une structure, ecrite sans la ligne qui la porte. La
   premiere moitie de ma phrase (ratios() lit a trois decimales) tenait parce que je
   l'avais lue ; la seconde tombe parce que je l'avais deduite.

2. ETAT. Geste (2) CLOS des deux cotes ; rien d'ouvert pour machine 1 ni machine 2 ;
   aucun run, aucune cellule entamee. Ce qui part au chantier constante A (chat neuf ;
   gel v5 d5ace962a3a6e413, certification 13d2973b0e143a20, chaine a4c35a2ee691c9a7 au
   poste m2, verifies) : la cause avec son temoin executable ; la borne retenue intacte
   et le doute des 11 pour cent leve, plus la correction ci-dessus ; la carte des classes
   (a) (a') (b) (c) et la residuelle glibc/UCRT a un ulp pour le 9bis ; l'erratum du
   "seul point" et R-G2-5 ; deux regles candidates sous (X) et le levier d'environnement.
   La porte n'a pas bouge : volet A sur branche 5 seulement, le pre-vol rend branche 4 ;
   l'arbitrage du 29/08 reste a l'operateur -- la marge du volet A, ou une marge cote T,
   pas les deux.

-- FIN note_machine1_erratum_cloture_geste2_v1 --
