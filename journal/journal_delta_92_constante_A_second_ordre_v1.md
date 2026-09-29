JOURNAL DELTA nn -- LE TERME DU PREMIER ORDRE DE LA CONSTANTE A EST DERIVE EN EXACT, LES
MODES LIBRES DE L'APPROCHE DE LA SINGULARITE AUSSI, ET LES DEUX SONT TESTES EN AVEUGLE PAR
UN RUN A REGLAGE DEPLACE (n = 18, LEVIER 441/324) SOUS UN GEL v9 ET UN INSTRUMENT v15 QUI
PORTENT LA P-A CORRIGEE : LE BIAIS DU PREMIER ORDRE EST PROPORTIONNEL A delta' A p = 4 ET 5
(2 POUR CENT, DOUZE POINTS), LES MODES LIBRES SE TRANSPORTENT A p = 7 (SIX POINTS, 5 POUR
CENT, 0.04 rad), LA LECTURE CORRIGEE REND UN RUN QUI PARLE LA OU LE PLANCHER DU MODELE
L'AURAIT TU AUX TROIS DEGRES ; LA SEULE PREDICTION QUI NE TIENT PAS (a, p = 7) A UNE CAUSE
MESUREE SUR LES DEUX MACHINES ; A N'EST TOUJOURS PAS MESUREE
(redaction machine 1, contreseing machine 2, depot operateur, 2026-09-29) -- PROJET, VERSION 1
=======================================================================
S'insere apres le delta 91 (729f9a9, journal_delta_91_constante_A_run_v2.md
035e19806db14910). Numero pris au depot (E18) ; "nn" dans le corps. Rien de ce qui est
cite n'est edite (PB-1) ; les pieces se citent par leur canon (convention B, sha256 NFC+LF,
16 hex), les lots par leur ligne CANON. Ce delta ne prend aucun numero de serie, ne
recommande aucun delta et n'adopte aucune regle.

nn.0 POSITION EN TROIS PHRASES
  Entre le 13/09 et le 29/09 la campagne a derive ce que le delta 91 designait : le terme de
  fenetre neglige par le gel alpha v5 (c1, exact, sans w2 en unites de tau_dom'), le terme
  suivant (c2, forme close), et les modes libres de la linearisation autour de la solution
  auto-semblable -- exposants complexes de partie reelle alpha + 3/2 par une symetrie du
  polynome, frequence en ln tau, amplitude et phase fixees par le point. Un gel v9 et un
  instrument v15 ont porte cette lecture dans l'instrument (P-A sur le couple corrige,
  plancher du terme suivant a 1e-13, Richardson a ordre mesure sur trois niveaux) et
  pre-enregistre deux predictions ; le run du 29/09, sur BOCAL4 puis sur machine 1, les a
  jugees : la premiere tient a p = 4 et 5 et ne tient pas a p = 7, la seconde tient six fois
  sur six a p = 7. La cause de la morsure est mesuree apres coup : la prediction se lisait
  sur un ajustement qui projette le mode libre ; A n'est pas mesuree, le chemin pour la
  mesurer est ecrit.

nn.1 PIECES CITEES (convention B ; "au registre" = dans l'arbre a 729f9a9, delta 91 ;
     detention declaree : "les deux" = detenue par les deux machines a la date de l'acte)
  Le chantier du second ordre (machine 2, 13/09 ; lus et rejoues par machine 1) :
    lecture_predeclaree_second_ordre_machine2_v1.md   99080e4822bf0108  les deux
    derivation_second_ordre_machine2_v1.py / .log     f0333c0afcf86583 / 2409f40ed2a61c61
    derivation_second_ordre_machine2_v1.json          b70fca94d72822ad  REPRODUIT AU BIT par m1
    exploration_richardson_second_ordre_machine2_v1.py / .log  9562f34b1b5d6d4a / 28f599270bcce9ea
    dossier_conception_second_ordre_machine2_v1.md    d8b601eee9941086  les deux
    lecture_predeclaree_Q5_modes_libres_machine2_v1.md fc6ca127f8eabc8b  les deux
    ajustement_modes_libres_Q5_machine2_v1.py / .log / .json  e7ff0b5664efe1c2 / ad6fdfc7bccf4a36
                                                      / 4634a795a008a562  (lot 4bb9da845608a7dd,
                                                      avec le JSON b2c5f8cc47c6e611 du run 91 v13
                                                      de BOCAL4 et ses 54 series ; les deux)
    note_machine1_lecture_second_ordre_v1.md          c8390c986806649b  (lot 588abe7cd9c6f6bd)
    note_machine1_lecture_Q5_v1.md                    8640542955081128  (lot ff42b9a8588cd7aa)
  Le gel et l'instrument, par versions :
    constante_A_pre_enregistrement_v7.md              a2b8463372e1f906  au registre, REMPLACE
    constante_A_pre_enregistrement_v8.md              800fc6a9a8e56e49  plume m1, NON CERTIFIE
                                                      (certification m2 45de25ac61321661 : cinq
                                                      reprises R-v8-1..5), REMPLACE
    constante_A_pre_enregistrement_v9.md              b515abc5a6da73c5  GEL COURANT (v8 + les
                                                      cinq reprises + 7bis), CERTIFIE m2
                                                      b5568d8f31f8492e, contresigne par
                                                      construction identique au bit
    construction_gel_v8_banc_v14_machine1_v1.py       faf29c378ab88dda  (39 hunks, 32 rempl.)
    construction_gel_v9_banc_v15_machine1_v1.py       d6d7ac766b8f5ac6  (13 hunks, 10 rempl.)
    banc_qualification_machine1_v13.py                1ac295648490a86c  au registre, REMPLACE
    banc_qualification_machine1_v14.py                dc91676c640d4323  CERTIFIE m2 (etage dt/4),
                                                      REMPLACE
    banc_qualification_machine1_v15.py                a1553f6eb5cc74b8  INSTRUMENT (lecture
                                                      corrigee), CERTIFIE m2 b5568d8f31f8492e
    lecture_v8_machine1_v1.py                         4f1679c48f68aa6f  REMPLACEE
    lecture_v9_machine1_v1.py                         4144c0086a3a99e7  la feuille de lecture,
                                                      deposee avec le gel avant le run
    base_modes_libres_n21_machine1_v2.json            79099ef4ea51adf6  (m2 : 0a7d411197d0603d ;
                                                      tables a 1.9e-16, canons distincts)
    derives_v9.json                                   156f9a455f52313e  (planchers, proj4, pred.)
    POUR_MACHINE1_prescription_PA_dans_instrument_machine2_v1.md  b86f25c573fd5b05  (lot m2
                                                      289ae2620e1d1063, 18/09)
    essai_correctif_PA_hors_depot_machine2.py         0dcfd901a0551d0f  (les trois remplacements
                                                      du v15, repris tels quels)
    derivation_plancher_corrige_machine2_v3.py / .log / .json  b0e107f45e0bc17b / 33a515251ac3311a
                                                      / 3b12117a58dde698  (proj4 ; REJOUE AU BIT
                                                      par m1 le 29/09, log 6194df14ffd3d12e)
    note_machine2_certification_v8_v14_v1.md          0e3aa516ad021159  (lot 45de25ac61321661)
    POUR_MACHINE1_certification_v9_v15_machine2_v1.md c3745a9c71978f54  (lot b5568d8f31f8492e ;
                                                      certif 8c4a74f5f6c3636b, 69 controles)
    ERRATUM_manifeste_lot_gel_v9_banc_v15_machine1_v1.md  e9babf9830ebe308  (lot 802a84bb706b6124)
  Le run delta 92 :
    lot machine 2 fb456f007eab7c61 : POUR_MACHINE1 511f897547a84ba2 ; certification du run
      7a693228a172cdad / b09d4e0d0412742c / 90d0f63215b33257 (45 controles, 0 morsure) ;
      journaux 7503c5a40aefcf7a (temoin), a1b97554adf19cde (alpha) ; resultats_temoin.json
      9f5cbd763fbcc0ee ; resultats_alpha.json 5a1032b29d3f03c7 ; MANIFEST des volets
      6e4d2afc73a6bc6d, 81ee9c622716ff67 (83 series) ; lecture des predictions
      d52e40dc52fd52e1 / 4a880c934f8aacd2 ; repetition sur le 91 240836e9c5c0f1d3
    lot machine 1 af86e5b281d037e9 : note 990039aac7497586 ; journaux 63b775988765c71c (temoin),
      93010e493b614b67 (alpha) ; resultats_temoin.json 6c931574d30f50c8 ; resultats_alpha.json
      541252658a7af032 ; lecture des predictions 80feccfeac6b767f / af295b8a660d33e8 ; cause
      de 7|1.73|1.20 abe4c268551f0235 / 399e6664cfe27182 / 5af3647b91ee39cd
  DETENTION UNIQUE, DECLAREE A LA CITATION : les 83 series du volet alpha de BOCAL4 sont
  detenues par machine 2 seule (leur MANIFEST.sha256 81ee9c622716ff67 est au lot et les 83
  de mon rejeu sont au mien, par leur propre manifeste) ; le contreseing machine 2
  71d410cd531d06ab (cite par son lot du run) n'a pas ete transmis a machine 1. Tout le reste
  resout aux deux postes.

nn.2 LE CHANTIER DU SECOND ORDRE -- CE QUI EST DERIVE, ET CE QUI EST MESURE A POSTERIORI
  (a) Le terme de fenetre. Pour x = A tau^(-alpha) (1 + c1 tau^2 + c2 tau^4 + ...) dans
  x'''' + (1 + w2^2) x'' + w2^2 x = g x^(p-1) (equation eliminee EXACTEMENT depuis le texte
  de acc_pu de l'instrument, reste symbolique nul, test negatif tenu) :
      c1 = (1 + w2^2) alpha (alpha+1) / ((p-1) K - P2),  P2 = alpha (alpha+1)(alpha-1)(alpha-2)
      c2 = [ K (p-1)(p-2)/2 c1^2 - (1 + w2^2) c1 (2-alpha)(1-alpha) - w2^2 ] / [ P4 - (p-1) K ]
  Le coefficient de tau^(-alpha-2) est nul en exact aux neuf (p, w2) ; c1 x 1.001 le rend non
  nul. c1 tau_dom'^2 = delta' alpha(alpha+1)/((p-1)K - P2) ne depend pas de w2 : 1/3, 65/261,
  133/795 du plancher delta'/((alpha+2)(alpha+3)) aux p = 4, 5, 7. Le plancher du gel v5 etait
  une borne, d'un facteur 3 a 6, pas le terme.
  (b) Les modes libres. x = x0 (1 + e tau^beta) : (beta-alpha)(beta-alpha-1)(beta-alpha-2)
  (beta-alpha-3) = (p-1) K. beta = -1 (translation de t*) est racine exacte. Le polynome en
  m = beta - alpha est symetrique par m -> 3 - m ; ses racines vont par paires (m, 3-m) et la
  paire complexe a Re m = 3/2 EXACTEMENT : Re beta = alpha + 3/2 = 7/2, 17/6, 23/10 ;
  frequence en ln tau 4.213075, 3.492054, 2.896550. Entre tau^2 et tau^4 aux trois degres ;
  a p = 7, tau^0.3 au-dessus du terme c1. Amplitude et phase libres par point.
  (c) La projection. L'ajustement II de l'instrument (sans c1) projette c1 tau^2 sur lnA avec
  un facteur 0.6727 (forme de fenetre r = 1/10 ; 0.6638 a un demi-pas de decalage) : biais
  2.542e-07 / 2.630e-07 / 2.399e-07 a n = 21.
  (d) A posteriori sur le run 91, non opposable : Richardson a q = 4 suppose explique l'ecart
  P-A a 2 pour cent a p = 4 et 5 et pas a p = 7 ; l'ambiguite d'ordre (q = 3 a 5) pesait
  13 pour cent -- d'ou le troisieme niveau du v14. Q5 (lecture fc6ca127f8eabc8b ecrite avant) :
  le modele M2 (c1 fixe + mode libre a (b, w) DERIVES, deux coefficients lineaires) reduit
  la somme des carres a p = 7 de 2.508e-07 a 4.378e-09 (x 57) quand une frequence fausse
  (w/2, 2w) ne la reduit que de x 2.1 ; identique au chiffre sur les series BOCAL4 et sur
  celles de machine 1 (glibc). A p = 4 et 5 le mode n'apporte rien (il absorbe la
  troncature) : M1 y suffit.
  (e) La dispersion LD-12 de l'instrument est, par definition (v13 l.225-230), l'ecart de
  lnA_II entre les grilles (dt_2b, k=2), (dt_2b/2, k=2), (dt_2b, k=4) : de l'erreur
  d'integrateur, que Richardson retire.

nn.3 LE GEL v9 ET L'INSTRUMENT v15 -- CE QU'ILS PORTENT, ET COMMENT ILS ONT ETE FAITS
  Le gel v8 (plume m1, 13/09) = v7 + 39 hunks par construction a ancres uniques : regle
  d'echelle (n = 18 : le barreau de levier maximal qui ouvre la porte, e/seuil >= 1.15 aux
  neuf points, balayage machine 1 confirme sur BOCAL4 a 1.868), tables re-derivees a
  delta' = 1/32400, section 5bis (M1 a p = 4, 5 ; M2 a p = 7 ; Richardson a ordre mesure ;
  deux predictions), instrument v14 = v13 + etage dt_2b/4 (cle G_dt4, 108 series). Machine 2
  l'a NON CERTIFIE (45de25ac61321661) : R-v8-1 (G-plancher rendrait le run muet avant 5bis :
  sous les deux lois de transport de la dispersion du 91, trois degres mordus), R-v8-2 (la
  P-A a deux regimes annoncee, implementee nulle part), R-v8-3 (90 contre 108), R-v8-4 (trois
  biais tapes), R-v8-5 (un separateur colle). L'arbitrage operateur du 18/09 a pris la voie
  longue : porter la P-A corrigee dans l'instrument. Machine 2 l'a prescrite (289ae2620e1d1063)
  et l'a essayee sur une copie hors depot (trois remplacements, selftest 103/103, banc 56/56),
  en derivant le plancher du terme suivant : plancher_corr(p) = proj4 x max_w2 |c2| tau_dom'^4,
  proj4 mesure en precision etendue (0.2195 a 0.2238 selon le compte de points de la fenetre ;
  en double le terme n'est pas mesurable, 1e-13 contre un bruit de chaine 3e-14).
  Le gel v9 (plume m1, 18/09) = v8 + les cinq reprises + une section 7bis : G-plancher et P-A
  sur le COUPLE CORRIGE (tol_lnA = max(S(p), plancher_corr(p))), grandeurs du v7 conservees
  sous v14_*, lecture absente = consigne, comptes 108, biais re-derives par (p, w2) du JSON de
  la derivation, phrase de 9 aux bornes non tracees (D-v7-1) remplacee par une phrase sourcee.
  L'instrument v15 = v14 + les trois remplacements de l'essai repris tels quels, credites,
  + proj4 DERIVE (0.2238, borne haute de la mesure), + deux scenarios du banc qui tue qui
  exercent la lecture corrigee par mutation des lnA_M (G35 : q = 4 mesure aux 18 points et
  S_p = 0 -> G-plancher corrige mord, branche 3b ; G36 : q = 2 -> 18 points NON LUS, lecture
  NON JOUEE, verdict du v14 inchange), + G22 nomme. Planchers corriges a n = 18, derives par
  le script, c2 exact aux neuf points contre la derivation : 5.194891e-14 / 1.223649e-13 /
  3.181768e-13.
  Certification machine 2 (21/09, b5568d8f31f8492e, 69 controles) : gel et banc reconstruits
  IDENTIQUES AU BIT depuis le v8 et le v14 non edites ; reglage et planchers re-derives par
  ses formules ; sur le couple corrige, tol/plancher_corr de 1.7e+04 a 2.1e+05 sous les deux
  lois de transport ; selftest 103/103, banc 58/58, pre-vol temoin REGLAGE QUALIFIE branche 5
  (marge 1.868), pre-vol alpha branche 5 ; base rejouee a 1.9e-16. Une morsure : E-v9-1, mon
  manifeste annoncait "banc 103/103" (compte du selftest recopie ; cause : le journal du banc
  porte deux lignes "bilan", le motif prenait la premiere) -- erratum emis le 29/09
  (e9babf9830ebe308). La dette proj4 (une seule machine) est close le meme jour : la
  derivation de machine 2 rejouee sur machine 1 rend un JSON identique au bit.

nn.4 LE RUN -- LES DEUX VOLETS, SUR BOCAL4 (REFERENCE) PUIS SUR MACHINE 1
  Declenchement operateur du 29/09, E19 levee des deux cotes. BOCAL4 : volet temoin
  (--controle-9bis journal/depot_9bis_temoin_v1.json) 118.0 s ; volet alpha (--porte-temoin
  sur le fichier temoin reel) 252.3 s ; 83 series deposees au sha256 de leur manifeste.
  Machine 1 (levier X86_V4, clone frais 729f9a9) : memes lignes de commande ; alpha 187.9 s.
    volet temoin   REGLAGE QUALIFIE (bonus T-3 retire) -- branche 6 : T-3 mord seul
                   (W-integrales, T-3a) ; 9bis 0 ecart, 7 toleres a un ulp ; IDENTIQUE sur
                   les deux machines. T-3 : q_int H1 = 4.0943 (etat A, N NON LUE au plancher
                   machine, LD-16) et 4.1072 (etat B, N = 4.9598) ; le 91 rendait la meme
                   branche 6 ; le pre-vol rend branche 5 parce que le moteur factice ne joue
                   pas les integrales -- limite du pre-vol, deja versee (candidate 9).
    volet alpha    VERIFIE -- branche 5 : P-alpha les six par degre ET P-A aux trois degres ;
                   IDENTIQUE sur les deux machines ; trois niveaux deposes (plan 18, G_dt 18,
                   G_dt4 18), comptes 108 = 18 x 4 + 9 + 27.

nn.5 LA LECTURE CORRIGEE -- ELLE EXISTE, ET LA PORTE NE MORD PLUS
  Par point, l'ordre est MESURE sur les trois niveaux : q entre 3.792 et 3.964 (p = 4),
  3.715 et 4.116 (p = 5), 3.779 et 4.050 (p = 7) ; dix-huit points lus sur dix-huit, aucun
  hors [3, 5]. Par degre :
    p    S(p) BOCAL4    S(p) machine 1   plancher_corr    tol/plancher (BOCAL4 / m1)   G-plancher   P-A
    4    4.4679e-09     3.5429e-09       5.194891e-14     8.60e+04 / 6.82e+04          silencieux   True
    5    3.7152e-09     3.7152e-09       1.223649e-13     3.04e+04 / 3.04e+04          silencieux   True
    7    3.5182e-09     3.5182e-09       3.181768e-13     1.11e+04 / 1.11e+04          silencieux   True
  Les planchers coincident au chiffre avec ceux que machine 2 re-derive par sa forme close.
  LE CONTRASTE, mesure et non plaide : sous la lecture du v14 (LD-12), dispersion / plancher
  = 1.0086e-06 / 1.5432e-06, 3.2839e-07 / 2.1368e-06, 8.6748e-08 / 2.9008e-06 -- G-plancher
  aurait MORDU AUX TROIS DEGRES (v14_G_plancher_mord True, sur les deux machines) et le run
  aurait ete NON CONCLUANT DE PLANCHER, comme le 91. R-v8-1 etait la difference entre un run
  qui parle et un run qui se tait.
  Entre les deux machines : DIX-SEPT des dix-huit lnA_R de l'ajustement II sont IDENTIQUES AU
  BIT ; un seul differe, 4|2.27|1.20, de 9.15e-10 -- une cellule EXPOSEE du geste (2) -- et
  c'est lui seul qui fait S(4) passer de 4.4679e-09 a 3.5429e-09 ; q differe d'au plus 3.3e-02.
  Aucun verdict n'en depend. Le transport des S du 91 annonce a la certification du v9
  (1.7e+04 a 2.1e+05) etait optimiste d'un facteur ~1.4 : consigne par machine 2, sans effet.

nn.6 LES DEUX PREDICTIONS, EN AVEUGLE JUSQU'AU RUN -- ET LA CAUSE DE LA SEULE MORSURE
  Pre-enregistrees au gel v8 (13/09) et reprises telles quelles au v9 ; lues par lecture_v9
  (121 controles, 1 morsure, la meme sur les deux machines).
  (a) Le biais du premier ordre est proportionnel a delta' : lu sur l'ajustement II sans c1,
  apres Richardson a ordre mesure, contre pred = biais_91(p, w2) x 441/324, biais re-derive du
  JSON de la derivation (3.4606e-07 / 3.5799e-07 / 3.2647e-07 aux p = 4 / 5 / 7). TIENT au
  degre si obs_R/pred est dans [0.8, 1.2] aux six points et |obs_R - pred| <= 3 S(p).
    p = 4   TIENT   0.982 0.990 0.986 0.998 0.986 0.985
    p = 5   TIENT   0.983 0.990 0.982 0.986 0.990 0.988
    p = 7   NON     0.867 0.284 0.963 1.234 1.089 0.881
  A p = 4 et 5 : douze points a 2 pour cent, tous legerement sous 1 (consigne, non
  explique ici). La proportionnalite en delta' tient contre un biais constant (ecart 36 pour
  cent) et contre une loi de modes libres delta'^((alpha+3/2)/2) (26 et 15 pour cent).
  (b) Le transport des modes libres a p = 7 : les coefficients (a, c) de M2, apres Richardson,
  contre la base du 91 transportee par amplitude x (441/324)^(b/2) = 1.4255 et phase
  - w ln sqrt(441/324) = -0.4465 rad. TIENT au point a 20 pour cent et 0.3 rad.
    7|1.73|1.05  0.946  -0.006 rad    7|1.73|1.20  1.004  -0.001 rad    7|2.27|1.05  0.959  -0.010 rad
    7|2.27|1.20  0.993  +0.008 rad    7|2.80|1.05  1.017  -0.002 rad    7|2.80|1.20  1.011  -0.036 rad
  SIX SUR SIX, a 5 pour cent d'amplitude et 0.036 rad de phase -- un ordre de grandeur sous
  les tolerances ; identique avec l'une ou l'autre base. Le point qui fait tomber (a) est
  celui qui tient (b) le mieux.
  LA CAUSE, A POSTERIORI (classe C ; feuille cause_7_1p73_1p20_machine1_v1.py, jouee sur les
  deux runs ; a rejouer par machine 2) : l'ajustement II n'a ni c1 ni mode dans sa forme et
  projette l'un et l'autre sur lnA ; le biais lu est biais_c1 + biais_mode, et biais_mode
  depend de l'amplitude et de la phase du mode au point. Une serie synthetique
  x = A tau^-alpha exp(c1 tau^2 + s^b (a cos(w ln s) + c sin(w ln s))) portant les (a, c)
  que M2 a ajustes au run, posee sur la grille de l'instrument et lue par II, rend
  biais_total / biais_c1 = 0.886 / 0.284 / 0.971 / 1.249 / 1.103 / 0.889 contre les ratios
  observes 0.867 / 0.284 / 0.963 / 1.234 / 1.089 / 0.881 -- a 0.02 pres, 0.284 au chiffre ;
  la phase opposee (a, c -> -a, -c) rend 1.114 / 1.716 / 1.029 / 0.751 / 0.897 / 1.111 et ne
  les reproduit pas. 7|1.73|1.20 n'est pas un point anormal : c'est celui ou le mode libre
  est le plus grand (c_mode 5.64e-07, quatre fois les autres), et la repetition de machine 2
  sur le run 91 (0.138 apres correction du levier) le voyait deja. Ce que (a) mesure a
  p = 7 sur II, c'est c1 plus la projection du mode ; ce que (b) mesure, c'est le mode. La
  prediction (a) a p = 7 reste NON au sens du gel v9, et sa forme correcte est ecrite : a
  p = 7, le terme du premier ordre se lit sur l'ajustement qui porte le mode, c1 laisse
  LIBRE dans M2 -- a pre-enregistrer au gel v10, pas ici.

nn.7 DEFAUTS ET ERRATA (numeros de chantier ; numeros de serie au depot, E18)
  D-v6-1..5 (m1, gel v8/v6 : table collee, rangee n = 23, 4.8 et 9 substitues et non
    recalcules, v9 -> v11) : levees au v7 par machine 2 (H6-H10). D-v9-1 a D-v12-1 : au 91.
  D-SO-1 (m2, citation) : le JSON du run v13 de BOCAL4 cite "au registre" n'y etait pas ;
    transmis avec Q5, close.
  D-v7-1 (m1, provenance) : bornes "2.2e-04 a 1.6e-03" de la section 9 non tracees ;
    remplacees au v9 par les planchers du 85, source citee ; close.
  D-v13-1 (m1, projection) : "residuel en delta' x plancher, gains 1e+03 a 1e+04" -- faux,
    les modes libres le placent en delta'^((alpha+3/2)/2) x amplitude inconnue ; retire ;
    le gain reel est mesure : 8.6e+04 / 3.0e+04 / 1.1e+04 sur le plancher corrige.
  R-v8-1..5 (m2 sur le v8) : reprises au v9 ; certifiees.
  D-essai-1 (m2, instrument) : une lecture corrigee absente est une consigne, jamais une
    invalidation -- sinon le banc cesse de tuer ; levee au v15.
  D-essai-2 (m2, instrument) : le chemin corrige n'etait exerce ni au pre-vol ni au banc ;
    mesure au v15 : les cellules synthetiques portent l'ajustement corrige mais n'ont pas
    d'ordre en dt lisible (q = 8.6, NON JOUEE consignee) ; le banc l'exerce par mutation
    (G35, G36) ; levee au v15.
  D-essai-3 (m2, instrument) : la borne proj4 <= 1 trop grossiere a p = 7 ; proj4 derive au
    v15 ; levee.
  E-v9-1 (m1, manifeste) : "banc 103/103" pour 58/58 ; erratum e9babf9830ebe308 ; cause
    mesuree (deux lignes "bilan" au journal du banc) ; aucun canon ne bouge.
  Dette proj4 (m1, declaree au gel v9 7bis) : close le 29/09 par rejeu au bit ; la ligne du
    gel qui la declare est perimee, a lever au gel v10 (PB-1 : pas d'edition du v9).
  Faits verses sans numero : le transport des S du 91 par machine 2 optimiste d'un facteur
    1.4 ; la feuille --base exige l'instrument qui a produit le run (36/75 avec le v15 sur un
    run du v13, 0/75 avec le v13) -- consigne de depouillement ; le clone du registre de
    machine 2 vide par un nettoyage de Temp entre le 21 et le 29, restaure a 729f9a9 et
    selftest repasse avant le run ; le conteneur de machine 1 reinitialise a chaque
    conversation (rejeux depuis les lots).

nn.8 REGLES CANDIDATES SOUS (X) -- revue du 28/09 ECHUE, aucune n'est prise ici
  13  (m2, 29/09) Un compte se lit par un motif ANCRE en debut de ligne, a la ligne qui le
      porte ; deux instances le meme jour (E-v9-1 ; la recidive de machine 2).
  14  (m1) Une lecture qui exige un ordre en dt ne se joue pas sur un synthetique exact en
      dt : le pre-vol la consigne NON JOUEE, le banc l'exerce par mutation ; corollaire de
      la candidate 9.
  15  (m2) Une base ajustee se cite par sa table a tolerance declaree, jamais par son canon,
      qui est machine-dependant (1.9e-16 entre les deux bases du 91).
  Les huit du delta 90 et les quatre du delta 91 attendent la meme revue.

nn.9 A ARBITRER PAR L'OPERATEUR, NON PRIS ICI
  (i)   les numeros de serie de nn.7 (E18), en un bloc ;
  (ii)  la revue (X), echue depuis le 28/09 : quinze candidates ;
  (iii) le depot des 83 series du volet alpha (BOCAL4) : par leur manifeste seul (comme ce
        lot) ou une a une (precedent du 91 : les series entrees avec le lot) ;
  (iv)  le gel v10 : mesurer A -- restaurer la regle du plus grand n (v7 3.2) avec le
        plancher corrige, lire (a) a p = 7 sur M2 a c1 libre, lever la ligne de 7bis ;
        ordre des chantiers ensuite : lot p = 40, re-pose de P-D1-9, Chirikov M3-M14, le
        jumeau quantique puis C2, Held apres.

nn.10 CONSEQUENCES POUR LE REGISTRE
  Gel courant de la constante A : v9 (b515abc5a6da73c5) ; instrument : v15 (a1553f6eb5cc74b8)
  avec ses constructions v8/v14 et v9/v15 ; feuille de lecture v9 et bases ; le chantier du
  second ordre entier (dossier, lecture pre-declaree, derivation, exploration, Q5 et ses
  series du 91) ; les certifications et prescriptions de machine 2 ; les deux lots du run ;
  l'erratum ; la cause. Le perimetre s'ENUMERE depuis les citations de cet acte (feuille de
  perimetre du 91 rejouee sur ce texte, manifeste derive) et ne s'ecrit pas a la main.

nn.11 LE CANAL
  Lots echanges sur ce chantier (canons) : machine 2 -- second ordre (7 pieces, 13/09), Q5
  4bb9da845608a7dd, certification v8/v14 45de25ac61321661, prescription 289ae2620e1d1063,
  certification v9/v15 b5568d8f31f8492e, run fb456f007eab7c61 ; machine 1 -- lecture second
  ordre 588abe7cd9c6f6bd, lecture Q5 ff42b9a8588cd7aa, gel v8/banc v14 b87f7a97f6477449, gel
  v9/banc v15 1f1d56d351e352dc, erratum et proj4 802a84bb706b6124, certification du run
  af86e5b281d037e9. Detention unique declaree en nn.1. Aucun run n'a ete joue par machine 1
  avant la certification croisee du gel et de l'instrument : les predictions etaient
  aveugles jusqu'au 29/09.

nn.12 CE QUE CE DELTA NE FAIT PAS
  Il ne mesure pas A : le run rend une porte et deux tests, pas une valeur ; la P-A corrigee
  vraie aux trois degres est un test a tolerance d'instrument (~4e-09), pas une mesure de
  A(w2). Il ne retire pas la morsure de (a) a p = 7 : la cause est mesuree apres coup, la
  prediction reste NON au sens du gel qui la portait. Il n'explique pas le "legerement sous
  1" des douze points de p = 4 et 5. Il ne prend aucun numero, n'adopte aucune regle, ne
  recommande aucun delta et n'edite aucune piece citee (PB-1). Il ne depose ni les ZIP ni
  MANIFEST.sha256.

nn.13 PIECES DE CE DELTA (lot machine 1 ; canon = convention B du manifeste)
  journal_delta_nn_constante_A_second_ordre_v1.md    cet acte
  perimetre_depot_delta91_machine2_v1.py             la feuille de perimetre du 91 (m2),
                                                     rejouee telle quelle sur cet acte ; log
                                                     et manifeste de depot derives au manifeste
  note_machine1_acte_delta92_v1.md                   la note d'accompagnement
  Les entrants sont ceux de nn.1 ; les feuilles de mesure, les constructions, les JSON et
  journaux de run entrent au depot avec leurs lots. Relecture des nombres : a la
  certification machine 2 (contreseing).

-- FIN journal_delta_nn_constante_A_second_ordre_v1 --
