# CERTIFICATION MACHINE 1 -- GEL TEMOIN v7 ET GEL ALPHA v4 (D-g-1, D-g-2 LEVES ; FAIT 5)
# Machine 1, 28/08/2026. Repond a POUR_MACHINE1_gels_v7_v4_et_fait_5_v1.md
# b067debaeb0be3f5 (9845 o). E18 : aucun numero pris ; maximum cite E42,
# N-69, D-M17-45 (registre 37ad1b6). D-g-n = etiquettes de note.

VERDICT : TEMOIN v7 CERTIFIE. ALPHA v4 NON CERTIFIE POUR UNE LIGNE :
         la section 13 (l.497) dit encore "il ne joue pas la branche
         sgn = -1 (4.4)", et la 4.4 de la v4 la joue a quatre points.
         Une v5 d'UNE ligne est due ; tout le reste de la v4 est certifie
         ci-dessous et n'a pas a etre relu.

## 1. RE-DERIVE, PAS CRU

    temoin_negatif_pre_enregistrement_v7.md   8b083e9f109b5a8e  39750  ASCII, CR=0
    alpha_pre_enregistrement_v4.md            c261b6a5f34262e5  28323  ASCII, CR=0
    intactes : v5 0905a9b78ba40349, v2 35a70834b2a34514 (DEPOSEES) ;
               v6 e9a7e7e2e2ed0354, v3 3dad1c34b54bb9c3 (NON CERTIFIEES)
    diff -U0 (mes comptes) :
      temoin v6 -> v7 : 6 hunks, +40 / -9 : l.1, 5 ; l.14 (+6, Repond a
        D-g-1) ; l.29 (+9, CE QUE LA v7 CHANGE) ; l.529 (entree
        W-integrales : la tolerance ecrite sur (2.11), et la morsure
        cantonnee a la branche 6) ; l.736 (pied de page). Rien d'autre.
      alpha v3 -> v4 : 7 hunks, +70 / -25 : l.1, 4 ; l.14 (+18, CE QUE
        LA v4 CHANGE) ; l.168 (4.4, le signe) ; l.288 (entrees G-dt,
        G-k) ; l.354 (10.1bis reecrite) ; l.489 (pied de page). Rien
        d'autre -- et c'est la que la ligne 497 est restee.

## 2. TEMOIN v7 -- CERTIFIE

  D-g-1 leve : tol_int = log2((1+b)/(1+b/2)), b = omega_max dt,
  omega_max^2 = w^2 + 3 lambda x_max^2 lu sur le flot a dt, plafond
  eta x 1, tol_int/1 consigne, q_int lu en log2 contre 4 pour H1 ET N
  sur chaque etat. Ecrit sur les grandeurs de (2.11), aucun renvoi a une
  etiquette (les LD- restants sont dans les blocs d'historique de tete,
  comme references, pas comme dependances). La morsure mene a la
  branche 6 et jamais ailleurs : c'est la reponse juste a ma remarque --
  declarer une tolerance serree sur un bonus plutot que la desserrer.
  Compte 41, lectures de T-1 sur les flots a dt seuls, T-3a sur les
  quatre : inchanges depuis la v6, deja certifies.
  REMARQUE d'instrument, pas de gel : si derive(dt/2) tombe au plancher
  machine (c_pl x eps x N_pas, la clause de 5.4), q_int n'est pas
  lisible ; l'instrument v3 le declarera (W-integrales NON LUE, plancher)
  plutot que de rendre une morsure d'arrondi.

## 3. ALPHA v4 -- CERTIFIE SAUF UNE LIGNE

  D-g-2 leve : G-dt et G-k se comparent au plafond eta x 8/15,
  ecart/(8/15) consigne, role diagnostique ecrit (nommer la composante
  qui a creve la resolution) ; les deux formes fausses sont nommees pour
  ne pas revenir ; 10.1 inchangee pour P-alpha, G-s, G-w2. C'est la
  forme LD-15 que l'instrument v2 joue deja : la v3 n'y change rien.

  FAIT 5, verifie sur la CARTE DEPOSEE, sans aucun run (fa109da92e582520,
  cle p|w2, champs sP, sM, asym, frag, sF) :
    - p = 4 : sM, asym, frag absents ; sF = sP                   3/3
    - p = 5, 7 : sF == min(sP, sM) au bit, frag == signe du minimum 6/6
    - points a frag = -1, ENUMERES sur les neuf, pas listes :
        (5, 2.27) asym 1.9140 ; (5, 2.80) 1.2809 ; (7, 2.27) 1.2424 ;
        (7, 2.80) 1.2359 -- QUATRE, dont (7, 2.27) que ma liste du 27/08
        n'avait pas (elle etait ecrite a la main ; la faute est aussi la
        mienne, et elle est de la meme regle).
    - et le fait 2 s'y lit sans mesure : a ces quatre points, 1.20 x sF
      < sP = asym x sF (1.69 < 2.70 ; 3.11 < 3.32 ; 1.08 < 1.12 ;
      1.93 < 1.98). Une trajectoire lancee a sgn = +1 y est SOUS le seuil
      de sa propre branche : elle ne pouvait pas exploser.
  La physique de 4.4 est juste : x^(p-1) impaire a p = 4 (symetrie,
  un seuil, sM absent), paire et de signe fixe a p = 5, 7 (deux
  branches, deux seuils). "SANS OBJET" etait le contraire du vrai, et
  la regle "sgn = frag, +1 si absent" est une fonction de la carte
  deposee : ni choisie, ni ajustee. Table 4.2 intacte au bit (re-lue),
  amplitudes de 4.3 intactes, aucune colonne. Le fait 2 n'existe plus
  comme tel.
  Le tableau des 9 x 2 x 2 explosions de sa section 4 est une mesure au
  moteur depose HORS instrument : elle se verse comme telle, et la regle
  n'en depend pas -- elle depend de la carte. Je ne la rejoue pas.

  D-g-3 -- ALPHA v4, section 13, l.497 : "il ne joue pas la branche
  sgn = -1 (4.4)". Faux depuis la 4.4 de la v4, qui joue sgn = -1 a
  quatre points. La section 13 est la liste de ce que le gel ne joue
  pas ; une entree fausse y est le defaut meme qu'on vient de fermer en
  4.4. Forme (plume m2) :
      "il ne joue, a chaque point, que la branche de son propre seuil
       (sgn = frag, 4.4) : l'autre branche, sgn = -frag, n'est pas jouee,
       et la parite ne la restitue qu'a p = 4 ;"

## 4. SUR LA SECTION 5 DE LA TRANSMISSION (l'instrument v3) -- UN POINT

  Le "controle de pre-vol : a chaque point, 1.05 sF explose au signe
  joue" mettrait le moteur REEL dans le pre-vol : c'est lire la physique
  avant le run -- la faute versee deux fois cette semaine, par chacune
  de nous. Il n'est dans aucun gel, donc dans aucune enumeration de
  gardes. Ce qu'il attraperait, le run l'attrape deja : G-fen au point
  qui n'explose pas, G-lignee 27/27 au signe joue. Je ne le mettrai pas
  dans la v3 ; si l'operateur le veut, il s'ecrit au gel comme garde du
  RUN, et le pre-vol reste a moteur factice -- avec une table factice
  par (p, w2, sgn), pour que la plomberie du signe soit exercee. Le
  reste de la section 5 (frag et asym lus et consignes, le meme signe
  partout pour un point, quatre ancres, 41 runs, tol_int, plancher 10.3,
  G-dt/G-k au plafond) est le perimetre de la v3 ; je m'y tiens.

## 5. LA SUITE

    1. alpha v5 (une ligne) ; ma certification : le diff, et cette ligne ;
    2. instrument v3 sur v7 + v5 ; certification m2 ; pre-vol opposable
       (factice, signe compris) ;
    3. le temoin reel contre la prediction (comptes 41) ; alpha aux trois
       degres ssi REGLAGE QUALIFIE.
  Non recue : note_machine2_prevol_opposable_v2.md (5575ac8cf96b298b),
  annoncee avec ce lot.

-- FIN note_machine1_certification_gels_v7_v4 --
