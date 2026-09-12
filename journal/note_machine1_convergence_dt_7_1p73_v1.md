NOTE DE LECTURE MACHINE 1 -- GESTE (2) : CONVERGENCE EN dt DE e(dt2/2) A LA
CELLULE 7|1.73 -- LE PLANCHER DE COMPENSATION EST ATTEINT DES dt2/4, ET L'ECART
ENTRE LES DEUX MACHINES (0.759 / 0.684) EST DERIVE DE CE PLANCHER
(classe 3, machine 1, 2026-09-12) -- VERSION 1
=======================================================================
Bloc d'ouverture : SUIVI_campagne_2026-09-12, section 4, GESTE (2). Aucun
delta choisi ; aucun verdict de gel ; la tenaille n'est pas lue ici (le bloc
le dit : la mesure precede toute lecture de la tenaille). Lecture m2 attendue.

0. POSITION EN TROIS PHRASES
  A 7|1.73, l'erreur relative e du banc de solution manufacturee (temoin v11,
  5.3) vaut 80.2, 6.75, 1.46 et 1.26 fois le plancher de compensation
  eps x R aux pas dt2, dt2/2, dt2/4 et dt2/8 : l'ordre observe passe de 3.57 a
  2.21 puis 0.22, et e ne suit plus dt^4 des dt2/4 -- elle se pose sur un
  plateau a 1.3-1.5 plancher (a dt2/4, le max n'est meme plus au bord de la
  fenetre).
  La paire du gel rend ici e/seuil = 0.7593, le nombre de machine 1 du 28/08
  (0.759) a quatre chiffres ; l'ecart avec machine 2 (0.684) vaut 0.67
  plancher, plus petit que le plateau : les deux machines divergent sur une
  grandeur de plancher que 5.4 ecarte de la lecture des deux cotes, et sur
  rien de LU. ECART : DERIVE du plancher (E-A tenue), pas indecidable.

1. PIECES (convention B sauf mention ; toutes detenues par machine 2 ; au
   poste m1 seulement pour cette conversation)
  lot recu            a4c35a2ee691c9a7  lot_machine2_2026-09-09_chaine_constante_A_v1
                                        (8 pieces, 8/8 au canon du manifeste)
  instrument v8       4d8882a2223a5c74  banc_qualification_machine1_v8.py (193651 o)
                                        -- importe EN LECTURE, jamais edite (PB-1)
  temoin v11          a2e7ef3e237c5acf  temoin_negatif_pre_enregistrement_v11.md
                                        (72281 o) -- gel du volet T : 5.3 definit e,
                                        5.4 le plancher et C(p)
  moteur              c8ed357b120352c4  scripts/m9_replication_v1.py, sha256 BRUT
                                        complet celui que l'instrument porte (MOTEUR,
                                        36325 o) ; authentifie sur clone frais
                                        lbaaz/SG_1 HEAD d037d21 (plafond 89) et charge
                                        par charger_moteur de l'instrument (empreinte,
                                        globales heritees, certifier_gel : conforme)
  N-70 v2, erratum 7(i), note m2 v8, gel v4 : recus, authentifies, NON LUS ici
                                        (hors du geste).
  DECLARE : le gel constante A v5 (2c0d2dc86054838c) n'est pas dans ce lot,
  qui est du 09/09, anterieur a la certification du v5 ; ce geste n'en a pas
  besoin -- e(dt2/2), la cellule et le pas sont definis par le temoin v11 et
  produits par jouer_T2 de l'instrument v8, dont les fonctions sont reutilisees
  telles quelles. Rien n'est contourne, ceci est dit pour ne pas etre cherche.
  Livrable (ce lot) : script convergence_dt_7_1p73_machine1_v1.py, log, JSON,
  cette note, manifeste ; canon = empreinte B du manifeste.

2. CE QUI EST JOUE, ET COMMENT
  Cellule (p, w2) = (7, 1.73) ; alpha = 4/5 ; A = 3.142438761846983 ;
  tau_dom = 1.563888567554228e-03 ; tau_CAP = 1.5638885675542283e-04 ;
  dt2 = tau_CAP / M = 7.819442837771142e-06 ; depart a tau0 = k tau_dom =
  3.127777135108456e-03 sur l'etat EXACT de x_m (quatre composantes,
  xm_et_derivees puis vers_composantes) ; integration par phase2_pu de
  l'instrument (pas_rk4_force, forcage f(tau) du temoin 5.1, arret TAU_FIN a
  tau_CAP) ; e = max |x1 + x2 - x_m| / |x_m| sur la fenetre ; R = max
  (|x1| + |x2|) / |x1 + x2| sur le flot ; plancher = eps x R ; lecture 5.4 par
  lecture_5_4 de l'instrument sur le flot FIN de chaque paire, exactement
  comme l'instrument lit la paire du gel. QUATRE flots : dt2, dt2/2, dt2/4,
  dt2/8 = les TROIS paires (dt, dt/2) du bloc, bases dt2 (paire du gel),
  dt2/2, dt2/4. Compte declare avant : 4 flots, n_pas = 380 x 2^k derive de
  (k/r - 1) M ; joues 4 + sautes 0 = 4 ; les quatre finissent sur TAU_FIN.
  Les attentes E-A, E-B, E-C sont imprimees au log AVANT la premiere
  integration (script, section 3). Plateforme : python 3.12.3, numpy 2.4.4,
  Linux x86_64 glibc 2.39 ; 1.0 s.

3. LA MESURE (JSON convergence_dt_7_1p73_machine1_v1.json, tous les chiffres
   en pleine precision ; ici arrondis a la quatrieme decimale)

  pas     n_pas   e             e/plancher   R_composantes    tau du max    err a tau_CAP
  dt2      380    1.052543e-06   80.2243     59087266.2392    tau_CAP       1.053e-06
  dt2/2    760    8.862395e-08    6.7548     59087456.0606    tau_CAP       8.862e-08
  dt2/4   1520    1.921167e-08    1.4643     59087465.9732    1.7789e-04    9.758e-09  (0.744 plancher)
  dt2/8   3040    1.653085e-08    1.2600     59087466.2590    tau_CAP       1.653e-08

  plancher_composantes = eps x R = 1.312001e-08 (dt2), 1.312005e-08 (les trois
  autres) ; eps = 2^-52 ; C_eff(7) = 8.896551724137932 (pleine precision) ;
  tol_ordre(7) = 0.17202346732631013 ; bande RK4 [3.8280, 4.1720].
  R forme fermee 5.4, 2 alpha (alpha+1) / ((w2^2 - 1) tau_CAP^2) =
  59087466.747 ; ecarts relatifs des R mesures : -3.4e-06, -1.8e-07,
  -1.3e-08, -8.3e-09 -- R converge vers la forme fermee avec le pas : c'est
  une grandeur lisse du flot, elle n'est pas en cause.

  paire            p_obs    e/seuil (flot fin)   lecture 5.4
  (dt2,   dt2/2)   3.5700   0.7593               W-plancher MORD, ordre NON LU   [PAIRE DU GEL]
  (dt2/2, dt2/4)   2.2057   0.1646               MORD, NON LU
  (dt2/4, dt2/8)   0.2168   0.1416               MORD, NON LU

  Deplacement de l'ordre a la paire du gel : 4 - 3.5700 = 0.4300, le nombre
  que le temoin v11 5.4 verse (D-t-25 : "le deplacement observe vaut 0.4300").

4. LA LECTURE (classe 3)
 4.1 LA PAIRE DU GEL REPRODUIT MACHINE 1. e/seuil = 0.7593 ici, 0.759 au bac
     a sable m1 du 28/08 (instrument v5 alors, meme chemin de code T-2) :
     machine 1 se reproduit a deux dates et deux versions d'instrument, a
     quatre chiffres. Machine 2 rend 0.684 sur BOCAL4. Ce n'est pas une
     attente tenue (E-B etait large par construction) : c'est une
     reproduction, versee comme telle.
 4.2 LE PLANCHER EST ATTEINT DES dt2/4. e/plancher : 80.2, 6.75, 1.46, 1.26 ;
     p_obs : 3.57, 2.21, 0.22. Sous la loi RK4 (e_tronc en dt^4), la part de
     troncature au pas dt2/4 est au plus e(dt2/2)/16 = 0.42 plancher et au pas
     dt2/8 au plus 0.03 plancher ; e y mesure 1.46 et 1.26 plancher : des
     dt2/4, plus d'un plancher de e n'est PAS de la troncature. Au pas dt2/4 le
     max n'est plus au bord (tau = 1.7789e-04, ou R vaut 4.57e+07) et l'erreur
     au bord vaut 0.744 plancher : c'est le max d'un bruit, pas un profil. Le
     plateau 1.26-1.46 plancher est la grandeur que le temoin 5.4 nommait sans
     pouvoir la mesurer -- b, reconstruit des trois Dp du degre a 1.15-1.74
     plancher. La forme fermee eps x R (D-t-22, kappa = 1) tient donc a un
     facteur 1.5 pres au point ou elle etait la moins sure, et la mesure
     confirme la portee que D-t-25 lui donnait : une borne d'UNE evaluation,
     que le flot depasse d'un facteur d'ordre 1, pas d'ordre N.
 4.3 L'ECART ENTRE MACHINES EST DERIVE DU PLANCHER. En unites de plancher :
     m1 28/08 6.752, m1 12/09 6.755, m2 6.085 ; ecart m1 - m2 = 0.667
     plancher = 9.9 pour cent de e(dt2/2). Le bruit de plancher, mesure la ou
     la troncature ne compte plus (dt2/4, dt2/8), vaut 1.26-1.46 plancher :
     l'ecart est plus petit que le bruit dont il est fait. Sa source est
     ecrite au protocole (numpy pow non symetrique au dernier ulp, comportement
     dependant de la machine) : f(tau) appelle tau ** (-a-2) et tau ** (-a) a
     chacun des quatre etages du pas, sur 760 pas, et x_m une fois par point ;
     chaque dernier ulp des composantes x1, x2 pese R = 5.9e+07 eps sur
     x = x1 + x2. Une grandeur qui
     vit a quelques plancher n'est reproductible entre plateformes qu'a
     quelques plancher pres, et 0.67 en est.
     CE QUI EST DERIVE : la taille du plancher (eps x R, forme fermee) et le
     fait que l'ecart tient dedans. CE QUI EST MESURE : le plateau, ici, sur
     une plateforme. CE QUI RESTE A m2 : le rejeu BOCAL4 (section 7) -- s'il
     rend 0.684 a la paire du gel ET un plateau du meme ordre aux pas raffines,
     la lecture est complete des deux cotes.
     CONSEQUENCE : le "seul point non reproduit au bit entre les machines"
     n'est pas un defaut de chaine -- c'est une grandeur de plancher, que le
     gel 5.4 ecarte de la lecture DES DEUX COTES (0.759 et 0.684 sont tous deux
     sous 1 : W-plancher MORD, ordre NON LU, aux deux postes). Les machines ne
     divergent sur rien de LU. Un ecart plus fin que le pas de lecture n'est pas
     une mesure ; celui-ci est plus fin que le plancher.
 4.4 CE QUE LA MESURE NE DIT PAS.
     - Rien sur la tenaille (delta >= 1.660e-5) : non lue, par le bloc.
     - Rien sur les trois autres points NON LUS du reglage prime (5|1.73 sur
       le fil a 0.991 ; 7|2.27 a 0.853 ; 7|2.80 a 0.957) : meme mecanisme
       attendu, NON mesure, hors bloc.
     - Rien sur alpha : le point 7|1.73 est NON LU par le gel et le reste.
       Cette note ne le rouvre pas et ne propose aucun critere neuf.
     - La decomposition troncature / plancher de 4.2 est une lecture bornee
       (au plus e/16), pas un modele ajuste : aucun b n'est estime, kappa = 1
       reste au caractere.
     - e(dt2) = 80 plancher est dominee par la troncature et se reproduit
       entre plateformes a ~1 pour cent ; ce n'est pas elle que 5.4 lit.

5. LES ATTENTES, ECRITES AVANT LE RUN, ET LEUR SORT
  E-A  p_obs HORS [3.8280, 4.1720] aux deux paires raffinees      TENUE (2.2057, 0.2168)
  E-B  e(dt2/2)/plancher dans [4.35, 8.49] (0.684 et 0.759 x C_eff,
       elargis de 1.74 plancher)                                  TENUE (6.7548)
  E-C  aucune attente ; signe de p_obs a la derniere paire        +0.2168, consigne
  E-B etait large par construction (elle testait l'appartenance a la famille
  des deux machines, pas la reproduction de 0.759) ; la reproduction a quatre
  chiffres n'etait pas predite et n'est pas comptee comme telle.

6. RESIDUS -- nommes, non ouverts
  R-G2-1  la moitie plateforme : ce geste est joue sur UNE plateforme ; la
          valeur 0.684 n'est pas reproduite ici et ne peut pas l'etre.
  R-G2-2  les trois autres points NON LUS (5|1.73, 7|2.27, 7|2.80) : plateau
          attendu, non mesure.
  R-G2-3  le facteur du plateau (1.26-1.46 plancher a 7|1.73) : mesure, non
          derive ; aucun modele du max d'un bruit sur N points n'est propose
          (il exigerait un choix -- temoin 5.4, derniere phrase).
  R-G2-4  la tenaille : intacte, par le bloc.

7. LECTURE m2 DEMANDEE -- LE REJEU SUR BOCAL4 (classe 3, aucune porte)
  Depuis la RACINE du clone (charger_moteur et certifier_gel du moteur y sont
  relatifs), Git Bash :
    python convergence_dt_7_1p73_machine1_v1.py \
      --moteur <clone>/scripts/m9_replication_v1.py \
      --instrument <lot a4c35a2e>/banc_qualification_machine1_v8.py \
      --temoin <lot a4c35a2e>/temoin_negatif_pre_enregistrement_v11.md \
      --sortie <dossier vide>
  Le script s'arrete si l'une des trois empreintes ne repond pas. A comparer,
  sans tolerance de porte (lectures, ecrites avant le rejeu) :
    n_pas 380 / 760 / 1520 / 3040 : EXACTS, les quatre sur TAU_FIN ;
    R_composantes : a 1e-06 relatif de 59087466.747 (grandeur lisse) ;
    e(dt2) : a ~1 pour cent de 1.052543e-06 (80 plancher, troncature) ;
    e/seuil a la paire du gel : voisin de 0.684 (le nombre de m2), PAS de
      0.7593 -- c'est l'objet meme du geste ; les deux sous 1 ;
    e/plancher aux pas dt2/4 et dt2/8 : entre 0.7 et 2.5 (plateau) ;
    p_obs aux deux paires raffinees : sous 3.8280 ;
    lecture : ECART DERIVE si les deux dernieres lignes tiennent.
  Si le rejeu rend un p_obs raffine DANS la bande RK4, la lecture 4.3 tombe et
  l'ecart redevient INDECIDABLE : c'est l'issue qui mord, elle est ecrite.

8. SUITE (a la main de l'operateur et de machine 1)
  Cette note est une piece pour l'acte constante A (chantier (2) de la file
  m1 : v5, cinq decisions suspendues, tenaille), a ouvrir en chat neuf ; elle
  rend au chantier son point suspendu : la non-reproduction a 7|1.73 est une
  grandeur de plancher, ecartee de la lecture par le gel des deux cotes, et
  ne bloque plus le run du volet T par elle-meme. Ce que le pre-vol branche 4
  et la tenaille x1.04 disent du run reste a lire a l'acte, pas ici.

-- FIN note_machine1_convergence_dt_7_1p73_v1 --
