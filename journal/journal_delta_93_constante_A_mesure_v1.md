JOURNAL DELTA nn -- LA CONSTANTE A EST MESUREE : AU BARREAU DU 91 (n = 21), SOUS LE GEL v10 ET
L'INSTRUMENT v16, LE COEFFICIENT DU TERME tau^2 AJUSTE LIBREMENT VAUT c1 DERIVE AUX DIX-HUIT
POINTS ET AUX TROIS DEGRES (PREDICTION (c), 18/18), LE BIAIS DU PREMIER ORDRE EST CELUI DE LA
DERIVATION AU LEVIER 1 (a, p = 4 ET 5), LES MODES LIBRES SE TRANSPORTENT DU 92 AU 93 (b, 6/6),
ET A(p) VAUT (K/g)^(1/(p-2)) A 4e-10 RELATIF AUX DEUX REGLAGES ; UN RESIDU DE 2 A 5e-09 RESTE
SANS NOM ; DEUX CONCLUSIONS SUR SA NATURE, UNE DE CHAQUE MACHINE, SONT REFUTEES PAR CE RUN ; LE
RUN EST UN RUN D'OBSERVATION, JOUE E19 LEVEE D'UN SEUL COTE, ET L'ACTE LE DIT
(redaction machine 1, contreseing machine 2, depot operateur, 2026-09-29) -- PROJET, VERSION 1
=======================================================================
S'insere apres le delta 92 (09baf5c, journal_delta_92_constante_A_second_ordre_v1.md
0a526d04fd9a8bda). Numero pris au depot (E18) ; "nn" dans le corps. Rien de ce qui est cite
n'est edite (PB-1) ; les pieces se citent par leur canon (convention B, sha256 NFC+LF, 16 hex),
les lots par leur ligne CANON. Ce delta ne prend aucun numero de serie, ne recommande aucun
delta, n'adopte aucune regle.

nn.0 POSITION EN TROIS PHRASES
  Le delta 92 avait derive le terme de fenetre et les modes libres, et montre a n = 18 que le
  premier ordre est le terme a p = 4 et 5 ; il ne mesurait pas A et le disait. Le gel v10 (plume
  machine 1, certifie machine 2) a defini la mesure avant le run -- lnA_R par point, delta_p et
  S(p) par degre -- et pre-enregistre une prediction neuve, (c) : le coefficient du terme tau^2
  laisse LIBRE dans l'ajustement vaut c1 derive, ce qui lit le premier ordre a p = 7 sans projeter
  le mode ; le run du 29/09 a n = 21, lance par l'operateur pendant que machine 1 relisait la
  certification, la rend 18/18 a 4 pour cent au pire, et A a 4e-10 de la forme auto-semblable
  aux trois degres, sur les deux machines. Ce que ni l'une ni l'autre machine ne sait nommer est
  ecrit tel quel : un residu de 2 a 5e-09 en lnA, dont le 93 a refute les deux noms proposes --
  le "biais de fenetre a signe unique" de machine 2, le "systematique de fenetre deterministe"
  et sa prediction (d) de machine 1.

nn.1 PIECES CITEES (convention B ; "au registre" = dans l'arbre a 09baf5c, delta 92 ; detention
     declaree : "les deux" = detenue par les deux machines a la date de l'acte)
  Le gel et l'instrument sous lesquels le run a tourne :
    constante_A_pre_enregistrement_v10.md          130ba949482129a7  GEL COURANT ; = v9 (au
                                                   registre) + 38 hunks appliques et 3
                                                   fragments sans ancre (E-v10-2) ; certifie m2
    banc_qualification_machine1_v16.py             634c4aaa2aad7598  INSTRUMENT ; = v15 (au
                                                   registre) + ajuster_c1_libre + D-v16-1,
                                                   D-v16-2 ; certifie m2
    construction_gel_v10_banc_v16_machine1_v1.py   13e9be0e067fcdf8  (lit machinerie_reglage.py
                                                   a0bb221e40bdfec7, extraite de la construction
                                                   du v8 faf29c378ab88dda, au registre)
    lecture_v10_machine1_v1.py                     c72c7348b863328b  la feuille de lecture,
                                                   deposee avec le gel ; essai a blanc sur le 92
                                                   32b058f0980e9003 / 160a4d12ee2f2749
    derives_v10.json                               c79c114595f9bba8
    note_machine1_gel_v10_banc_v16_v1.md           3c246646db1cab59  (lot 26ecd16e21783e5e ;
                                                   selftest be0875510e2fc9ad, banc e8abeedc430c1d90,
                                                   pre-vols af907b3591f510ca, ed17854299e6c23b)
    POUR_MACHINE1_certification_v10_v16_machine2_v1.md  4f856a34d6e887a8  (lot 996dc8be7d245387 ;
                                                   certif bdfdcf11d3c2e604 / 07fce55317825079 /
                                                   bcbe2b2f6d589bda, 39 controles, 0 morsure ;
                                                   epreuves BOCAL4 0342f665870bd57a, d8243dc9fb84b9ea,
                                                   9da882c22ef6d961, 7ab2871cb22ede77 ; essai
                                                   lecture e122267ef74a5723 / d6a0f2159c5c113c)
    ce_qui_borne_A_machine2_v1.py / .log / .json   ed5bbce867f0a41d / fb4163b7893c5070 /
                                                   55532af50289e38a  (7 controles ; REFUTEE en
                                                   partie par le 93, nn.5)
    ERRATUM_lot_contreseing_acte_delta92_machine2_v1.md  cb0e7699af25aec1  (deux pieces editees
                                                   sous le meme nom ; le registre fait foi)
  Le gel v11 et l'instrument v17, RETIRES avant certification (nn.5) :
    constante_A_pre_enregistrement_v11.md          ac398dc92badbdc5  RETIRE
    banc_qualification_machine1_v17.py             f914156a2c341f4b  RETIRE (= v16 + pin v11)
    construction_gel_v11_banc_v17_machine1_v1.py   e28749e8c84207f3
    note_machine1_gel_v11_banc_v17_v1.md           33d19b7ecb54c9ca  (lot c446e2b99e53d2a3 ;
                                                   releve du 92 f471ec91b6cb681c)
  Le run delta 93 :
    lot machine 2 90a0b0ca445989ef : POUR_MACHINE1 0c90082db29ee718 ; ce_qui_borne_A v2
      3035b9a733853bf6 / 7b8cd71029a65c22 / ea98455afc1169e5 (6 controles) ; journaux
      5100bde802a588bf (temoin), 32fcdc2013702093 (alpha) ; resultats_temoin.json 66547ce46ca6d821 ;
      resultats_alpha.json ba03f8023318c30d ; MANIFEST des volets 37eb4a976ce09e26, 6df42b6aeba84547
      (83 series) ; lecture des predictions 7a7cfbe3c8236b91 / 3e7d344106027a1d
    lot machine 1 c40bc1962170ca87 : note e06cdb73aabc231a ; journaux 054a1a3b07892ac7 (temoin),
      e5757a6872866ea7 (alpha) ; resultats_temoin.json c718fec4a2d3ae66 ; resultats_alpha.json
      0a8fadb16d6981fa ; MANIFEST des volets 880f22789d8bd10c, 91fc85380bb6dd77 ; lecture
      3adb387f841ac60a / 7376a0bc05151320
    bases pour (b) : m1_lecture_v9_predictions_delta92.json af295b8a660d33e8 (machine 1, au
      registre) ; m2_lecture_v9_predictions_delta92.json 4a880c934f8aacd2 (machine 2, au registre)
  Au registre, cites sans depot nouveau : derivation b70fca94d72822ad ; plancher corrige
    3b12117a58dde698 ; gel v9 b515abc5a6da73c5 ; v15 a1553f6eb5cc74b8 ; acte 92 0a526d04fd9a8bda.
  DETENTION UNIQUE, DECLAREE : les 83 series du volet alpha de BOCAL4 (manifeste 6df42b6aeba84547)
  sont detenues par machine 2 seule ; les 83 de mon rejeu par moi seul (91fc85380bb6dd77). Tout le
  reste resout aux deux postes.

nn.2 LE GEL v10 ET L'INSTRUMENT v16 -- CE QU'ILS PORTENT, CE QUI A ETE CERTIFIE
  Le v10 (29/09, plume m1) = v9 + : la regle du plus grand n qui ouvre la porte (v7 3.2)
  RESTAUREE -> n = 21, le barreau du 91, delta' = 1/44100 ; tous les nombres du reglage
  re-derives (kT = 1.3666, m = 1.5247, planchers 1/882000, 1/637000, 1/469224 ; planchers
  corriges 2.804073e-14 / 6.604951e-14 / 1.717439e-13 a proj4 = 0.2238) ; la MESURE de A definie
  avant le run ; trois predictions en aveugle : (a) le biais du premier ordre au levier 1 -- les
  biais C4 eux-memes, 2.542e-07 / 2.630e-07 --, lu sur l'ajustement II, p = 4 et 5 ; (b) le
  transport des modes libres du 92 (n = 18) vers n = 21, levier 324/441, amplitude x 0.7015,
  phase +0.4465 rad, base = les (a, c) du 92 apres Richardson ; (c) le coefficient du terme tau^2
  AJUSTE LIBREMENT (M1c a p = 4, 5 ; M2c a p = 7) vaut c1 derive, c1_R / c1_derive dans
  [0.9, 1.1] aux 18 points, c1_derive = (1 + w2^2) alpha(alpha+1)/((p-1)K - P2). La dette proj4 du
  v9 est levee (re-derivee par machine 1 au bit). Le v16 = v15 + ajuster_c1_libre (c1_fit,
  erreur-type, lnA a chaque cellule ; aucun verdict) + reglage n = 21 + deux corrections du
  banc qui tue : D-v16-1, l'horizon du synthetique sans CAP borne a 20 N_2BP pas (63 M pas a
  dt/4 tuaient machine 1 a 2.7 Go) ; D-v16-2, la lecture corrigee de G22 rendue NON JOUEE par
  construction (mutation q = 2) -- au v15 elle l'etait par accident a n = 18 et ne l'etait plus a
  p = 5 a n = 21. Certification machine 2 (29/09, 996dc8be7d245387, 39 controles, 0 morsure) :
  gel et banc reconstruits IDENTIQUES AU BIT depuis le v9 et le v15 ; reglage et planchers
  re-derives ; selftest 103/103, banc 58/58, pre-vols branche 5 sur BOCAL4 ; l'essai a blanc de
  lecture_v10 sur ses series du 92 rend A(p) a 2 a 3e-10 du theorique. Deux reserves, prises au
  v11 puis rendues sans objet par son retrait : E-v10-1 (la construction assertait le canon de la
  base 92 de machine 1, machine-dependant -- une base se verifie par sa table), E-v10-2 (41 hunks
  annonces, 38 appliques, 3 sans ancre non declares).

nn.3 LE RUN 93 -- UN RUN D'OBSERVATION, ET POURQUOI
  Le 29/09, l'operateur a lance le run sous v16 a n = 21 sur BOCAL4 "pour voir", pendant que
  machine 1 relisait la certification 996dc8be7d245387 et ecrivait le v11 : E19 (aucun run avant
  la certification croisee du gel et de l'instrument) n'etait levee que du cote machine 2. Le gel
  v10 etait ecrit par machine 1 et certifie par machine 2 -- les predictions etaient donc
  pre-enregistrees, par les deux machines, avant que le run tourne ; ce qui manquait etait la
  re-certification par machine 1 de la certification de machine 2, un tour de contreseing. Le
  run n'est pas opposable au sens strict d'E19 ; il n'est pas un run d'acte ; il est une mesure
  entiere, rejouee par machine 1, et cet acte le consigne comme run d'OBSERVATION. Son cout : les
  predictions (a), (b), (c) ne peuvent plus etre jouees en aveugle a n = 21, et un rejeu "dans les
  regles" ne rendrait rien que le 93 n'a pas rendu ; les deux machines le disent, et aucune ne
  recommande de le rejouer.
  BOCAL4 : temoin 54.8 s, alpha 161.8 s, 83 series au sha256 de leur manifeste. Machine 1 (levier
  X86_V4, clone frais 09baf5c, gel v10 place au registre local) : memes lignes de commande.
    volet temoin   REGLAGE QUALIFIE (bonus T-3 retire) -- branche 6 : T-3 mord seul
                   (W-integrales, T-3a) ; 9bis 0 ecart, 7 toleres ; IDENTIQUE ; comme au 91 et 92
    volet alpha    VERIFIE -- branche 5 : P-alpha les six par degre ET P-A aux trois degres ;
                   IDENTIQUE ; trois niveaux, comptes 108 ; lecture corrigee jouee 18/18, q dans
                   [3, 5] partout ; G-plancher corrige silencieux aux trois degres

nn.4 LA MESURE -- CE QUE LE 93 REND
  Lecture v10 (139 controles, 1 morsure, la meme sur les deux machines : (a) p = 7) :
  (a) p = 4 TIENT, p = 5 TIENT, p = 7 NON -- meme cause qu'au 92 (la projection du mode libre sur
      l'ajustement II, delta 92 nn.6) ; au levier 1 la prediction est le biais C4 lui-meme.
  (b) 6/6 : le transport du 92 vers le 93 tient aux six points de p = 7.
  (c) 18/18 : c1_R / c1_derive entre 0.961 et 1.037 chez machine 1, 1.0013 / 1.0072 / 0.9988 /
      0.9884 aux premiers points chez machine 2, pour une tolerance de 10 pour cent. LE PREMIER
      ORDRE EST MESURE, AUX TROIS DEGRES, p = 7 COMPRIS : la forme qui porte le mode lit c1 sans
      le projeter.
  A(p), par degre (lnA_R sur M1 a p = 4, 5, M2 a p = 7 ; delta_p ; S(p) = max - min des six) :
    p    A au 92 (n = 18)   A au 93, BOCAL4   A au 93, machine 1   (K/g)^(1/(p-2))   S(93) BOCAL4 / m1
    4    48.989794867       48.989794876      48.989794873         48.989794856      2.107e-09 / 2.485e-09
    5     9.650477146        9.650477146       9.650477146          9.650477151      2.423e-09 / 2.423e-09
    7     3.142438761        3.142438763       3.142438763          3.142438762      4.912e-09 / 4.918e-09
  Deux reglages independants (levier 441/324), deux machines, la meme valeur a 1e-09 pres,
  accordee a la forme auto-semblable gA^(p-2) = K a 4e-10 relatif -- SOUS S(p). Entre machines,
  15 des 18 lnA_R sont identiques au bit, l'ecart maximal vaut 4.2e-10 (a p = 4, la cellule
  exposee du geste (2)) ; c'est lui qui fait S(4) differer (2.107e-09 contre 2.485e-09), et S(4)
  ne se cite pas comme un nombre a deux machines. La regle du plus grand n a livre ce qu'elle
  promettait la ou la lecture etait bornee : S(4) x 0.471 et S(5) x 0.652 du 92 au 93 pour
  delta' x 0.735 ; a p = 7, S x 1.396 -- le mode domine, et le levier n'y achete rien.

nn.5 CE QUE LE 93 REFUTE -- UNE CONCLUSION DE CHAQUE MACHINE
  Machine 2, ce_qui_borne_A v1 (7 controles, joints a la certification du v10) : "a p = 4 et 5 la
  dependance en c a un seul signe aux six points ; la valeur vraie est au-dela du couple ; A(p)
  porte un biais de fenetre de ~1.6e-09, sept a neuf fois delta_p ; un plus grand n n'y achete
  rien (Q4)". Mesure exacte au 92, reproduite au bit entre les machines ; conclue pour tout
  reglage. Le 93 (ce_qui_borne_A v2, 6 controles) : le signe est MELE a p = 4 (+0.78, -2.11,
  +1.21, en 1e-09), unique a p = 5 seulement ; l'argument du biais tombe, machine 2 le retire, et
  retire sa Q4 (S a baisse comme delta' et davantage a p = 4 et 5).
  Machine 1, gel v11 (ac398dc92badbdc5, emis le 29/09 apres la certification et AVANT reception du
  93, mais apres qu'il a tourne) : ecrivait S(p) comme un SYSTEMATIQUE DE FENETRE DETERMINISTE,
  y ajoutait la mesure que sous M2 a p = 4 et 5 l'effet de c ne disparait pas (vraie), et
  pre-enregistrait (d) : "a n = 21, sous M1 a p = 4 et 5, les six ecarts en c sont de meme signe,
  positif". Lue sur le 93 par machine 1 : p = 4 MELE (+7.8e-10, -2.5e-09, +1.2e-09), p = 5 meme
  signe, p = 7 mele. (d) est FAUSSE a p = 4, et n'etait pas opposable. Le v11 et le v17 sont
  RETIRES avant certification ; le gel courant reste le v10, l'instrument le v16, tous deux
  certifies, sous lesquels le 93 a tourne. Ce qui reste vrai du v11 : la borne S(p) +
  plancher_corr majore ce qu'on ne sait pas nommer. Ce qui reste du residu : 2 a 5e-09 en lnA,
  de meme ordre aux deux reglages, 3e+04 a 8e+04 fois le plancher analytique, present sous M1 et
  sous M2 aux degres 4 et 5, sans signe reproductible, deterministe a reglage fixe (au bit entre
  machines, hors cellule exposee) : ni le terme suivant, ni le mode libre, ni un biais monotone.
  L'ACTE NE LE NOMME PAS.

nn.6 CE QUE LA CAMPAGNE SAIT DE LA CONSTANTE A, A LA CLOTURE DE CE DELTA
  (i)   A^(p-2) = K/g : la relation de la forme auto-semblable est verifiee a 4e-10 relatif aux
        trois degres et aux deux reglages, sous une borne de 2 a 5e-09 ; P-A corrigee vraie aux
        trois degres au 92 et au 93 ; G-plancher corrige silencieux.
  (ii)  le terme de fenetre c1 = (1 + w2^2) alpha(alpha+1)/((p-1)K - P2) est le premier ordre :
        derive en exact (delta 92), teste en aveugle par sa proportionnalite a delta' (92, p = 4
        et 5), MESURE librement a 4 pour cent aux 18 points (93, (c)), les trois degres ;
  (iii) les modes libres, Re beta = alpha + 3/2 par symetrie, frequence derivee, se transportent
        d'un reglage a l'autre (92 : 21 -> 18 ; 93 : 18 -> 21, six sur six) ; a p = 7 ils dominent
        la fenetre et se lisent sur M2 ;
  (iv)  ce qui borne la mesure n'est pas le modele (le plancher est a 1e-13) mais un residu de
        l'instrument, de l'ordre de 1e-09, que deux valeurs de c ne suffisent pas a caracteriser.
  Le chantier de la constante A, ouvert le 28/08, rend ici ce qu'il pouvait rendre avec ce plan.

nn.7 DEFAUTS ET ERRATA (numeros de chantier ; numeros de serie au depot, E18)
  D-v16-1 (m1, instrument) : memoire du synthetique sans CAP a dt/4 ; horizon borne ; leve au
    v16, certifie. D-v16-2 (m1, banc) : G22 NON JOUEE par accident ; par construction au v16.
  E-v10-1, E-v10-2 (m2 sur le v10) : reprises au v11, sans objet apres son retrait ; consignees.
  E-v9-1 (m1, manifeste) : erratum e9babf9830ebe308 ; E-92-1 (m2 sur le manifeste derive de
    machine 1 au 92) : corrige par la feuille de perimetre du 92 ; deux errata de machine 2 sur
    ses propres lots (reception editee, contreseing edite : cb0e7699af25aec1) -- le registre fait
    foi, aucun canon depose n'est faux.
  Retraits : ce_qui_borne_A v1 (m2), conclusions (i) et (ii) ; gel v11 et instrument v17 (m1).
  E19 : levee d'un seul cote au moment du run 93 ; consigne en nn.3 avec son cout.

nn.8 REGLES CANDIDATES SOUS (X) -- revue ECHUE depuis le 28/09 ; aucune n'est prise ici
  16  (m2, 29/09) Rejouer le script d'une autre machine se fait dans un repertoire a soi, jamais
      a la racine du depot : une sortie porte le nom que son auteur lui a donne, et ecrase.
  17  (m2, 29/09) Une piece emise ne s'edite pas, elle se versionne ; une sortie dont le nom est
      fixe dans un script se versionne avec le script.
  18  (m1) Une conclusion tiree d'UN reglage sur la nature d'un residu n'est pas un fait : deux
      fois en une journee (m2 sur le 92, m1 au v11) elle a ete refutee par le reglage suivant.
      Un residu se nomme apres deux reglages au moins, ou ne se nomme pas.
  Les treize precedentes (huit du 90, quatre du 91, une du 92) attendent la meme revue.

nn.9 A ARBITRER PAR L'OPERATEUR, NON PRIS ICI
  (i)   les numeros de serie de nn.7 (E18) ;
  (ii)  la revue (X), echue : dix-huit candidates ;
  (iii) le depot des 83 series du 93 (BOCAL4) : une a une, comme au 92 ;
  (iv)  le sort du residu : un troisieme indice c (prescription machine 2, maintenue faiblement),
        une moyenne sur le decalage de grille (C4 l'a mesuree a 1.3 pour cent), ou laisser le
        residu sans nom et fermer ; l'acte ne recommande rien ;
  (v)   la suite du programme : le lot p = 40, la re-pose de P-D1-9, Chirikov M3-M14, le jumeau
        quantique puis C2, Held apres.

nn.10 CONSEQUENCES POUR LE REGISTRE
  Gel courant de la constante A : v10 (130ba949482129a7) ; instrument : v16 (634c4aaa2aad7598) ;
  le v11 et le v17 entrent au registre comme RETIRES, avec leur construction et leur note, pour
  que la refutation de (d) soit lisible ; les deux lots du run 93 ; la certification du v10/v16 et
  les deux ce_qui_borne_A ; la feuille de lecture v10 et ses essais ; les errata. Le perimetre
  s'ENUMERE depuis les citations de cet acte par la feuille de perimetre du contresignataire et
  ne s'ecrit pas a la main (E-92-1).

nn.11 LE CANAL
  Lots echanges depuis le delta 92 (canons) : machine 2 -- contreseing du 92 1c4660dd54c463d8 et
  son erratum, certification v10/v16 996dc8be7d245387, run 93 90a0b0ca445989ef ; machine 1 --
  erratum et proj4 802a84bb706b6124, gel v10/banc v16 26ecd16e21783e5e, gel v11/banc v17
  c446e2b99e53d2a3 (retire), certification du run 93 c40bc1962170ca87. Detention unique declaree
  en nn.1. Le conteneur de machine 1 est reinitialise a chaque conversation (rejeux depuis les
  lots et le clone) ; le clone de machine 2 a ete restaure a 729f9a9 avant le 92 et porte 09baf5c
  depuis.

nn.12 CE QUE CE DELTA NE FAIT PAS
  Il ne nomme pas le residu de 2 a 5e-09. Il ne retire pas la morsure de (a) a p = 7 (cause
  mesuree au 92, forme correcte mesuree au 93 par (c)). Il ne fait pas du 93 un run d'acte au sens
  d'E19. Il ne mesure pas A(w2) : l'etendue entre w2 est sous le residu. Il ne prend aucun numero,
  n'adopte aucune regle, ne recommande aucun delta, n'edite aucune piece citee (PB-1), ne depose
  ni ZIP ni MANIFEST.sha256.

nn.13 PIECES DE CE DELTA (lot machine 1 ; canon = convention B du manifeste)
  journal_delta_nn_constante_A_mesure_v1.md          cet acte
  note_machine1_acte_delta93_v1.md                   la note d'accompagnement
  Perimetre : la feuille du contresignataire, sur ce texte ; les entrants sont ceux de nn.1.

-- FIN journal_delta_nn_constante_A_mesure_v1 --
