# PRE-ENREGISTREMENT constante A v7 -- LA FENETRE DESCEND JUSQU'A CE QUE
# L'INSTRUMENT, ET NON LE MODELE, FIXE LA TOLERANCE DE P-A ; LE REGLAGE EST
# PRIS DANS LA FENETRE DE LA TENAILLE, LA OU LE VOLET T LIT ET OU LE VOLET A MESURE
# BROUILLON MACHINE 1 -- DEVIENT GEL A LA CERTIFICATION MACHINE 2
# v7 = v6 (847bb3bb2dd19f87, 40158 o, NON CERTIFIEE par machine 2 -- D-v6-3 : 4.8 non re-derivee,
# D-v6-4 : section 9 non re-derivee -- REMPLACEE, non editee) + cinq hunks derives ou mesures,
# appliques par construction_gel_v7_machine2_v1.py (machine 2 ; plume machine 1 conservee, a
# contresigner par diff) : H6 4.8 re-derivee au reglage v6 (2 x 400) ; H7 section 9, colonnes
# bruit/signal re-derivees au signal 1/441 ; H8 3.2, la ligne n = 23 MESUREE sur BOCAL4 (branche 5,
# min e/seuil 1.113 < 1.15 : exclue par la clause (T), mesuree) et 3.5 le dit ; H9 11, le volet T
# se compte sous la v11 ; H10 cette provenance. Fait de forme du v6 (D-v6-1) : sa table 3.2 etait
# un hunk MANUEL, hors du script de construction qu'il declarait comme provenance.
# v6 = v5 (2c0d2dc86054838c, 31722 o, CERTIFIEE 104/104 par machine 2, REMPLACEE, non
# editee) + les hunks enumeres par construction_gel_v6_et_banc_v9_machine1_v1.py :
#   H1  section 3 : delta' n'est plus delta_0 / 4^5 = 1/102400 -- ce reglage est SOUS la
#       borne inferieure de la tenaille (INF = 1.659260768e-05, derivation v3
#       4353c80e60cef87c, reproduite au bit par les deux machines) et le pre-vol du v8 y
#       rend branche 4 des deux cotes (4 des 9 points de T-2 non lus). Descente declaree
#       delta' = delta_0 / n^2 avec n = 21 : delta' = 1/44100 = 2.267574e-05, DANS la fenetre --
#       marge T kT = delta'/INF = 1.3666, marge A m = 1.5247 (delta 90, nn.4 : les deux
#       marges pleines sont impossibles ; ni l'une ni l'autre n'est pleine ici, les deux
#       sont > 1) ; n est CHOISI PAR LE PRE-VOL (balayage de l'echelle, 3.2), pas a la
#       main : trois machoires, W-plancher, W-pas et le plancher du volet A.
#       Cascade de reglage PRE-ENREGISTREE en 3.5.
#   H2  tables 4.1, 4.3, 4.4, 4.5, 4.6 re-derivees au reglage v6 ; 4.7 : n_2s se re-derive
#       au pre-vol v9 par la formule inchangee.
#   H3  section 5 : la porte porte le temoin v11 (a2e7ef3e237c5acf, certifie
#       7fc5f2412b99ad50) et son erratum 7 (i) (13601ef21efdc024) ; l'instrument est le v9,
#       re-parametre depuis le v8 CERTIFIE (4d8882a2223a5c74, 2a618ffb180ea568) ; la
#       tolerance du 9bis entre machines est dite EN ULP pour les cles de classe
#       EXPOSEE-LIBM ; la ligne de plateforme de tout journal de run porte le temoin
#       d'arrondi executable.
#   H4  LD-16 re-ancree : c_pl = 10 est un parametre du reglage depose (run 85,
#       /reglage/c_pl), pas une clause de 5.4.
#   H5  sections 6, 7, 10, 12, 13 mises au reglage v6 et aux pieces du delta 90.
# Aucun autre nombre de fond ne change ; delta'/delta_0 passe de 1/1024 a 1/441 partout (section 9 comprise).
# Banc de verification (N-69 : sans numero de manche ; numero du delta au
# depot, N-68). Plume machine 1 sur arbitrage operateur du 2026-08-28
# (ouverture de l'etape A, "go"). Aucun run avant certification croisee.

CE QUE LA v4 CHANGE PAR RAPPORT A LA v3 -- CINQ REPRISES ET UNE
PRECISION, NOMMEES
             La v3 (d71770d5948fe1aa, 28724 o) est REMPLACEE, non
             editee. Source : la certification machine 2
             (note_machine2_certification_constante_A_v3_v1.md,
             52f76b9b82e7c861 ; instrument 1fa0c0eb3a341e09 ; log
             a92f60f936a2f75a ; 93 controles, 88 passent, 5 mordent),
             chaque morsure RE-DERIVEE par machine 1 avant reprise :
             1. R-A-1 / R-A-2 (fond, section 1) : le bloc "rien ne
                change" AJOUTAIT en 5.7 ("et a chaque depart d'etage",
                notion absente du v5) et RETRANCHAIT en 5.6 ("la ou il
                est accessible", qualificatif du v5 tombe -- la
                citation DURCISSAIT une garde de branche 0). La meme
                faute, retournee. La section 1 revient A LA LETTRE du
                v5 ; l'exigence neuve vit en 4.9, ecrite comme NEUVE.
                Troisieme et quatrieme assertions fausses de brouillon
                machine 1 de la journee (apres "mecanique inchangee"
                de la v1 et "620 exactement" de la v2) : a verser a
                l'acte, numeros au depot (E18).
             2. R-A-3 (fond, E19, sections 5/11/13) : la porte citait
                un gel qui n'existe pas (dix "v8", zero "v9"). Tri
                site par site, pas de sed : la porte porte desormais
                le temoin v9 CERTIFIE (403488b4f6c319e9, certification
                b5da74783e5f97c6) ; la v8 ne reste que comme piece
                historique remplacee ; 13 prend les pieces.
             3. R-A-4 (fond mineur, 4.8) : la jumelle a pas moitie
                DOUBLE chaque compte d'etage ; ses intervalles (bornes
                x2, forme derivee) sont ecrits -- sans eux, toute
                garde de compte mordait a tort sur toutes les
                jumelles.
             4. R-A-5 (forme, 4.7) : t_start se LIT du journal de
                phase 1, il ne se re-calcule pas -- la grille
                s'accumule et le recalcul n'est pas le meme double
                (mesure machine 2 : ecart -6.7e-10). La formule reste
                l'expression du point vise.
             5. PRECISION regle 15 (4.7, prise sans etre exigee) : les
                deux machines ont mesure DEUX orthographes de la meme
                egalite -- l'une differe aux trois w2, l'autre est
                nulle a 1.73 et vit a 2.27/2.80. Le verdict d'un test
                au bit dependrait de l'ORTHOGRAPHE de la formule.
                C'est ecrit.
             RIEN d'autre ne change : delta' et sa derivation (3), les
             tables 4.1-4.6, la porte du plancher (7), la cascade (8),
             la lecture L-desc et sa puissance (9), les sections 0, 2,
             12.

=======================================================================
0. CE QUE CE BANC DEMANDE, EN UNE PHRASE
=======================================================================

Au 85, P-A est COMPATIBLE par le plancher de modele : tol_lnA/plancher
= 1.0 aux TROIS degres, les dix-huit rapports g A^(p-2)/K sont > 1 et la
constante A n'est pas mesuree, elle est bornee par la fenetre. Ce banc
descend la fenetre (delta' = 1/44100, soit 1/441 de la fenetre du 85 ; le v5
descendait a 1/102400, SOUS la porte du volet T, section 3)
jusqu'a ce que le plancher passe SOUS la dispersion de l'instrument,
et rejoue P-A -- meme formule, deux cotes, tolerance d'instrument.

Une issue en branche 4 ou 7 (REFUTE) contredirait le verdict VERIFIE du
85 : elle s'ecrirait telle quelle, avec la mention de la contradiction,
et appellerait l'arbitrage de l'operateur. Ce gel ne l'adoucit pas.

=======================================================================
1. CE QUI NE CHANGE PAS -- par citation du gel alpha v5 (PB-1)
=======================================================================

Le gel alpha v5 (gels/alpha_pre_enregistrement_v5.md, 045c2435aaf623ce,
28998 o) reste la base. NE CHANGENT PAS, et valent ici par citation --
a la lettre du v5, sans ajout ni retranchement (R-A-1, R-A-2) :

    2      la derivation ; alpha = 4/(p-2) ; alpha(alpha+1)(alpha+2)
           (alpha+3) = g A^(p-2) ; K exacts (120 ; 3640/81 ; 9576/625) ;
           A_p = (K/g)^u_p, g = 0.05 : 48.98979 / 9.65048 / 3.14244
    3      les deux predictions P-alpha et P-A ; P-A decide ;
           P-alpha sans P-A = PARTIEL
    4      les 27 points : (p, w2) sur {4,5,7} x {1.73, 2.27, 2.80},
           c dans {0.95, 1.05, 1.20} sur s* de la carte ; sgn de 4.4 :
           p = 4 a sgn = +1 ; p = 5, 7 au signe frag de leur seuil
           (+1 a 1.73 ; -1 a 2.27 et 2.80, verifie au bit sur le run 85) ;
           comptes + sautes == 90
    5.2    phase 1 : dt_1 = 0.006, T_MAX = 400, schema depose
    5.3    la bascule (k = 2), seuils par degre et par point -- elle
           devient la bascule de l'ETAGE 2a (section 4 ci-dessous)
    5.6    temoin de lignee : 27/27 au booleen, et le meme indice de
           pas d'explosion la ou il est accessible, ou le lien n'est
           pas etabli
    5.7    la sortie : serie de la fenetre, l'etat complet a la
           bascule (t, x1, x2, x1', x2'), journal de phase 1,
           empreintes convention B
    7      les deux ajustements ; point fixe fenetre/t* (8 iterations
           max) ; ajustement II a alpha FIXE rend P-A ; regle 14
    8      les gardes G-dt, G-k (au plafond, 10.1bis), G-s, G-w2,
           G-seuil (le triplet qui tue), G-fen, G-lignee, G-comptes ;
           agregation : les six par degre, chacun, aucune moyenne
    9      la cascade et ses branches 0..7 (la branche 3b s'y insere,
           section 8 ci-dessous)
    10     les tolerances : 10.1, 10.1bis, 10.2 (plafond eta x 8/15),
           10.3 (P-A : tol_lnA = max(dispersion lnA grille, plancher),
           |ln(g A^(p-2)/K)| <= (p-2) tol_lnA aux SIX points) --
           AUCUNE formule ne change ; delta seul bouge et entraine tout
           par les formules memes

Ce gel n'ecrit aucune nouvelle formule de tolerance. Il ecrit : un
nouveau delta, des etages de pas pour l'atteindre (des deux cotes du
seuil) avec leurs sorties propres (4.9), une porte de qualification sur
le temoin v9 CERTIFIE, une porte de plancher, une lecture consignee a
portee declaree.

=======================================================================
2. LA QUESTION, ET SA PROVENANCE (N-61 : chaque nombre a sa source)
=======================================================================

Source : runs/run_alpha_delta85/resultats_alpha.json, empreinte
6d7d23130e9322f8 (depot a4a907a), cles citees verbatim.

    /degres/p/tol_lnA_sur_plancher = 1.0 aux trois degres : le MODELE
    fixe la tolerance partout.

    /degres/p/dispersion_lnA :
        p = 4 : 1.97714978966701e-06
        p = 5 : 2.393510486697892e-06
        p = 7 : 7.43220491195018e-06

    /degres/p/plancher_lnA (delta = 1/100) :
        p = 4 : 1/2000 = 5.0e-04
        p = 5 : 9/13000 = 6.923e-04
        p = 7 : 1/1064 = 9.398e-04

Le plancher domine la dispersion par des facteurs 253 / 289 / 126.
La constante n'est pas mesuree : elle est bornee par la fenetre, et les
dix-huit rapports du meme cote, ordonnes comme la borne (SUIVI 28/08,
section 3), disent que l'ecart observe est COMPATIBLE avec le terme
neglige -- sans le demontrer. Ce banc le met a l'epreuve.

=======================================================================
3. LA DERIVATION DE delta' (regle 13 : en forme derivee) -- TROIS MACHOIRES
=======================================================================

3.1 Trois conditions de conception. Le v5 n'en ecrivait qu'une :

    (A) plancher'(p) = delta' / ((alpha_p + 2)(alpha_p + 3))
                    <= dispersion_lnA_85(p) / m,  m >= 1, pour CHAQUE p   (volet A)
    (T) W-plancher lit aux neuf points de T-2 : e/seuil >= 1 partout, et
        e/seuil >= 1.15 (besoin mesure D-t-25) ; en forme derivee, delta' >=
        kT x INF, INF = 1.659260768e-05 (tenaille, delta 90 nn.4)      (volet T)
    (O) W-pas lit aux neuf points : |p_obs - 4| <= tol_ordre(p) (v11, 7 (i))

(T) et (O) tirent en sens contraires de (A) : le ratio e/seuil est
proportionnel a delta (le plancher de compensation va en 1/delta, e est
invariante a la dispersion pres) ; l'ordre observe se degrade quand dt_2b
grossit, et dt_2b va en sqrt(delta). Au reglage du v5 (1/102400) le
pre-vol du v8 rend branche 4 des deux cotes (W-plancher MORD a 5|1.73,
7|1.73, 7|2.27, 7|2.80). Aucune des trois machoires ne se derive sur le
papier au dixieme pres : (O) FLUCTUE avec la grille d'un n a l'autre. Le
reglage se prend donc AU PRE-VOL, sur l'echelle entiere.

3.2 Descente declaree : delta' = delta_0 / n^2, delta_0 = 1/100, n entier
(le compte nominal 4.6 reste entier : M(n - 1)). REGLE DE CHOIX, declaree
avant le balayage : n est le PLUS GRAND entier de l'echelle (le plus petit
delta', donc la plus grande marge du volet A) tel que le pre-vol du temoin
rende branche 5 avec e/seuil >= 1.15 aux neuf points. Aucune valeur de A
n'entre dans ce choix : le pre-vol est une mesure d'instrument. Balayage
sur machine 1 (levier X86_V4, arithmetique de BOCAL4 au bit) :

    n   delta'      kT     m     verdict (machine 1, levier X86_V4)          min e/seuil   max |p_obs-4|/tol
    18  1/32400    1.860  1.120  REGLAGE QUALIFIE -- branche 5 : T-1 R = q, T 1.868         0.62
    19  1/36100    1.669  1.248  REGLAGE QUALIFIE -- branche 5 : T-1 R = q, T 1.631         0.59
    20  1/40000    1.507  1.383  NON CONCLUANT D'INTEGRATEUR -- branche 4 : W 1.527         1.22
    21  1/44100    1.367  1.525  REGLAGE QUALIFIE -- branche 5 : T-1 R = q, T 1.433         0.79
    22  1/48400    1.245  1.673  NON CONCLUANT D'INTEGRATEUR -- branche 4 : W 1.356         1.12
    23  1/52900    1.139  1.829  REGLAGE QUALIFIE -- branche 5 : T-1 R = q, T-1 1.113         0.72   (BOCAL4)
    24  1/57600    1.046  1.991  NON CONCLUANT D'INTEGRATEUR -- branche 4 : W 0.907         0.80

3.3 Resultat (Fraction, regle 15) :

    **n = 21    delta' = 1/44100 = 2.267574e-05    delta'/delta_0 = 1/441**
    kT = delta'/INF = 1.3666  (D-t-25 a mesure le besoin du volet T entre
                            1.15 et 1.74) ; m = SUP(1)/delta' = 1.5247
    SUP(1) = min_p disp_85(p)(alpha_p+2)(alpha_p+3) = 3.457292925e-05 (p = 5)

    p    plancher'(p) exact      plancher'(p)      plancher'/disp_85
    4    1/882000                1.133787e-06     0.5734
    5    1/637000                1.569859e-06     0.6559
    7    1/469224                2.131178e-06     0.2867

Les trois planchers tiennent SOUS les dispersions du 85 (m > 1 aux trois
degres) : si la dispersion du present run reste a son niveau, c'est
l'instrument qui fixe tol_lnA -- la porte de la section 7 en decide, sur
les grandeurs du run. Le v5 (n = 32) donnait kT = 0.59 : hors fenetre.

3.4 PRECISION (D-alpha-9 transposee) : a tau_dom', le terme neglige
vaut AU PLUS delta' fois le terme dominant ; le rapport exact est
delta'/((alpha+2)(alpha+3)) = les planchers de 3.3. Aucun autre nombre.

3.5 CASCADE DE REGLAGE, PRE-ENREGISTREE (aucun reglage ne se choisit
apres avoir vu une valeur ; les branches se declenchent sur un VERDICT DE
PORTE, jamais sur A) :
    porte T en branche 4 sur BOCAL4 au reglage v6  ->  v7 au plus grand n
        du balayage inferieur a 21 qui rende branche 5 sur BOCAL4 (le
        balayage est alors rejoue sur BOCAL4, meme feuille, meme regle) ;
    G-plancher MORD (branche 3b) au reglage v6  ->  aucun delta' plus petit
        ne passe la porte sur cette echelle (n = 22 et n = 24 mordent ; n = 23
        ouvre mais a e/seuil = 1.113 < 1.15, clause (T) mesuree) :
        la mesure de A exige un instrument plus fin a p = 7 (v10 : dt_2b
        plus petit ou compensation du plancher), arbitrage de l'operateur.
    Un seul pas de cascade par run ; au-dela, arbitrage de l'operateur.

=======================================================================
4. LES ETAGES DE PAS -- le seul changement d'instrument
=======================================================================

4.1 FAIT DERIVE, qui impose la structure : la bascule de la nouvelle
fenetre tombe a tau = k tau_dom' = 4.766e-03 / 3.839e-03 / 3.203e-03
(w2 = 1.73 / 2.27 / 2.80), SOUS le pas de phase 1 (dt_1 = 0.006). Elle
est irresoluble en phase 1 seule. Il faut un etage intermediaire.

4.2 LA REGLE DU PAS PAR ETAGE (generalise v5 5.4, meme M) : un etage
integre jusqu'a son tau TERMINAL avec

    dt_etage <= tau_terminal(etage) / M        (M = 20, v5 section 6)

Le v5 est l'instance a un etage (terminal tau_CAP). Ce gel en joue deux
apres la bascule de 5.3 :

    etage 2a : de tau = k tau_dom_0 (bascule v5 5.3, memes seuils)
               a   tau = k tau_dom'   ; dt_2a <= k tau_dom' / M
    etage 2b : de tau = k tau_dom'  (bascule 2b, table 4.4)
               a   tau = tau_CAP' = r tau_dom' ; dt_2b <= tau_CAP' / M

La fenetre d'ajustement est [tau_CAP', tau_dom'], peuplee a dt_2b :
M (1 - r)/r = 180 points, comme au v5 -- le peuplement de la fenetre ne
depend pas de delta.

4.3 LES QUATRE TABLES (derivees ; tau_dom' = sqrt(delta'/(1 + w2^2))) :

    w2      tau_dom'       tau_CAP'       dt_2a <=       dt_2b <=
    1.73    2.383068e-03   2.383068e-04   2.383068e-04   1.191534e-05
    2.27    1.919733e-03   1.919733e-04   1.919733e-04   9.598664e-06
    2.80    1.601602e-03   1.601602e-04   1.601602e-04   8.008009e-06

4.4 BASCULE 2b -- derivee par degre et par point (jamais partagee,
regle 11.1 v5) : bascule quand |x| >= A_p (k tau_dom'(w2))^(-alpha_p) :

                 w2 = 1.73     w2 = 2.27     w2 = 2.80
    p = 4        2.1566e+06    3.3233e+06    4.7746e+06
    p = 5        1.2032e+04    1.6052e+04    2.0438e+04
    p = 7        2.2633e+02    2.6906e+02    3.1103e+02

4.5 CAP'_p(w2) = A_p (tau_CAP'(w2))^(-alpha_p), fin de l'etage 2b :

                 w2 = 1.73     w2 = 2.27     w2 = 2.80
    p = 4        8.6265e+08    1.3293e+09    1.9098e+09
    p = 5        6.5318e+05    8.7142e+05    1.1095e+06
    p = 7        2.4863e+03    2.9558e+03    3.4168e+03

    Controle de debordement : max g |x|^(p-1) au CAP' = 3.483e+26
    (p = 4, w2 = 2.80), loin du plafond double (1.8e+308). Un
    debordement en cours d'etage rend le point NON CONCLUANT, COMPTE.

4.6 LE COUT -- NOMINAUX DERIVES, COMPTES MESURES. Un compte inscrit se
COMPTE, il ne s'affirme pas (transmission 67a4be1d02b89748 ; la
campagne a deja paye cette regle). Les etages sur-seuil sont a bornes
d'EVENEMENT : 2a part de la bascule 5.3 detectee sur la grille de
phase 1 et finit a la bascule 2b detectee sur sa propre grille ; 2b de
meme vers CAP'. Leurs comptes sont MESURES et CONSIGNES. Nominaux, en
nombres purs :

    n_2a nominal = M (sqrt(delta_0/delta') - 1) = 20 x 20 = 400
    n_2b nominal = M (k - r)/r = 380

Toute garde de compte se compare a l'intervalle DERIVE des deux effets
de grille (depart en retard d'au plus UN pas de la grille AMONT ;
arrivee en retard d'au plus UN pas de la grille PROPRE) :

    n_2a dans [ 400 - ceil(dt_1/dt_2a(w2)) , 401 ]
         soit [374, 401] / [368, 401] / [362, 401]   (w2 = 1.73/2.27/2.80)
    n_2b dans [ 380 - k/r , 381 ] = [360, 381]        (k/r = 20, pur)

Cout nominal de la descente : ~780 pas par serie sur-seuil --
negligeable devant la phase 1 (jusqu'a 61 135 pas au 85).

4.7 SOUS LE SEUIL (G-seuil) -- LES ETAGES S'ANCRENT EN t, PAS EN tau.
Sous le seuil il n'y a ni bascule ni t* : la mecanique v5 ("rejouer la
derniere fenetre avant T_MAX") ne se transpose PAS au reglage prime.
Mesure : la fenetre lue, de largeur tau_dom' - tau_CAP' = 0.9 tau_dom',
vaut 0.158 a 0.235 pas de phase 1, et passer de dt_1 a dt_2b d'un coup
saute un facteur 767 a 1142 -- c'est l'argument de 4.1 vu du cote
sous-seuil (trouvaille 1, transmission 09c4bdc1f01d782f). Les etages
descendent donc EN t DEPUIS T_MAX :

    depart_2s  = T_MAX - k tau_dom_0(w2)     (la borne v5 5.3, inchangee)
    depart_2b' = T_MAX - k tau_dom'(w2)
    fin        = T_MAX
    etage 2s  sur [t_start , depart_2b']   : dt_2s  (ci-dessous)
    etage 2b' sur [depart_2b', fin]        : dt_2b' (ci-dessous)
    fenetre lue = [T_MAX - (tau_dom' - tau_CAP'), T_MAX], peuplee a
    dt_2b : M (1 - r)/r = 180 points, comme au sur-seuil ; t* LIBRE.

COMPTES (meme regle qu'en 4.6 ; forme de la transmission
67a4be1d02b89748) : l'etage 2s part de l'etat de phase 1 au dernier
pas de la grille avec t <= depart_2s, jusqu'a UN dt_1 AVANT depart_2s
-- son compte n'est PAS 400 :

    t_start : l'instant de cet etat, **LU du journal de phase 1 (5.7)
    -- jamais RE-calcule** (R-A-5). La grille s'accumule, et le
    recalcul floor(depart_2s/dt_1) x dt_1 n'est pas le meme double :
    mesure machine 2, accumulee 399.893999999333 contre recalcul
    399.894000000000 (w2 = 1.73), ecart -6.7e-10 -- sans consequence
    sur n_2s a ce reglage (4e-06 d'un pas de dt_2a), mais c'est la
    faute que ce gel nomme lui-meme ci-dessous. La formule
    floor(depart_2s/dt_1) x dt_1 reste l'expression du POINT VISE,
    non de la valeur employee.

    n_2s    = ceil( (depart_2b' - t_start) / (k tau_dom'(w2)/M) )
    dt_2s   = (depart_2b' - t_start) / n_2s      [<= k tau_dom'(w2)/M]

L'etage ATTERRIT exactement sur depart_2b'. n_2s se COMPTE, jamais ne
s'affirme ; toute garde le compare a l'intervalle derive

    400 <= n_2s <= 400 + ceil(dt_1/dt_2a(w2))
    soit [400, 426] / [400, 432] / [400, 438]    (w2 = 1.73/2.27/2.80)

Valeurs DERIVEES du reglage prime, re-derivees des deux cotes :
n_2s = 425 / 408 / 418 (formule ci-dessous, au reglage v6 ; le v5 donnait
658 / 631 / 646 a 1/102400) -- elles se VERIFIENT au run, elles ne
s'assertent pas dans le code.

L'etage 2b' part de depart_2b' PAR CONSTRUCTION (l'atterrissage
ci-dessus) : son compte est exact, n_2b' = M k / r = 400, au pas
dt_2b' = (fin - depart_2b') / 400 = k tau_dom' / 400.

REGLE 15, ECRITE (mesures des DEUX machines, 28/08) : k tau_dom'/400
et tau_CAP'/M sont EGAUX en arithmetique exacte (k/400 = r/M = 1/200,
Fraction) ; en flottant, les deux expressions DIFFERENT au bit selon
l'ordre d'evaluation. Et la mesure est plus fine encore, chaque
machine en tenant un morceau : sur la paire (2 tau')/400 contre
(0.1 tau')/20, l'ecart vit aux TROIS w2 (machine 1) ; sur la paire
(2 tau')/400 contre (tau'/10)/20, il est NUL a 1.73 et vit a 2.27 et
2.80 (machine 2). **Le verdict d'un test au bit dependrait de
l'ORTHOGRAPHE de la formule.** L'egalite du pas 2b' a sa borne de 4.2
se DECLARE en exact et ne se teste JAMAIS au bit ; aucune garde de ce
gel ne compare deux derivations flottantes d'une meme grandeur.

Le triplet qui tue (i)(ii)(iii) de v5 8/G-seuil est INCHANGE ; (iii)
se lit a la tolerance de ce gel, plus serree : le banc tue plus fort.

4.8 G-dt AUX ETAGES : la trajectoire jumelle divise par 2 le pas de
CHAQUE etage (2a ET 2b sur-seuil ; 2s ET 2b' sous-seuil), meme
trajectoire, meme regle 10.1bis. G-k inchange (k = 2 contre k' = 4 sur
la bascule de 5.3).

LES COMPTES DE LA JUMELLE (R-A-4) : a pas moitie, chaque compte
d'etage DOUBLE. Les intervalles de 4.6 et 4.7 valent pour le pas
NOMINAL ; pour la jumelle, leurs DEUX bornes sont multipliees par 2 --
forme derivee, jamais recopiee -- et le compte reste MESURE :

    n_2a jumelle : [748, 802] / [736, 802] / [724, 802]
    n_2b jumelle : [720, 762]
    n_2s jumelle : [800, 852] / [800, 864] / [800, 876]
    n_2b' jumelle : 800 exact (atterrissage, meme construction)

4.9 L'ETAT AUX DEPARTS D'ETAGE -- EXIGENCE NEUVE DE CE GEL, PAS UNE
CITATION (R-A-1). 5.7 du v5 exige l'etat complet A LA BASCULE. Ce gel
AJOUTE : l'etat complet A CHAQUE DEPART D'ETAGE (2a, 2b, 2s, 2b'),
meme forme (t, x1, x2, x1', x2'), meme empreinte convention B. Sans
lui, l'etage 2s ne peut pas repartir de la grille de phase 1
(t_start, 4.7) et 10 (iii) n'a pas d'objet. La v3 logeait cette
exigence dans un bloc "rien ne change" : elle vit ici, comme neuve.

=======================================================================
5. LA PORTE DE QUALIFICATION (D-alpha-7 transposee) -- SUR LE TEMOIN
   v11, CERTIFIE, AVEC SON ERRATUM 7 (i) ; INSTRUMENT v9
=======================================================================

L'histoire, empreintes a l'appui : la v9 du temoin (403488b4f6c319e9,
certifiee b5da74783e5f97c6) a ete SUPERSEDEE par la v11 (a2e7ef3e237c5acf,
certifiee par machine 1 7fc5f2412b99ad50), completee sans edition par
l'erratum de tolerance a sa clause 7 (i) (13601ef21efdc024) ; le depot 9bis
(c4310e33da6b9759) vaut CLOS avec elle ; l'enumeration N-70 v2 des cles du
pre-vol (4867dffe3392dea6) est contresignee au bit sur machine adverse.
L'instrument est passe du v4 au v8 CERTIFIE (4d8882a2223a5c74, selftest
103/103, note 2a618ffb180ea568) ; le v9 de la section 10 le re-parametre.
Tout cela est au registre depuis le delta 90 (11f86226cf4aa612, e68341f).
LE FAIT QUI COMMANDE CE GEL : le pre-vol du v8 en mode temoin, au reglage
1/102400, rend NON CONCLUANT D'INTEGRATEUR, branche 4, DES DEUX COTES
(0a24121e441cc0c3 BOCAL4 ; c45ac9f59907fbf4 machine 1) -- W-plancher MORD
a 5|1.73, 7|1.73, 7|2.27, 7|2.80. Le reglage v6 (section 3) le remonte
dans la fenetre ; le pre-vol se rejoue au v9, des deux cotes, AVANT tout
run : attendu branche 5, sinon 3.5.

CE QUE LA PORTE EXIGEAIT, LA v11 LE PORTE (comme la v9 avant elle) : la remise d'etat aux
bascules -- l'organe que le reglage prime complique -- est qualifiee
par W-bascule EN DEUX ETAGES (v11, section 8) : g1 la phase grossiere
du v7, g2 l'etage 2a de ce volet, lecture D-t-19 ECRITE sur la
tolerance de 5.3 (iv), comptes derives aux memes intervalles que 4.6.
ATTENDUS = 41, conserves. La chaine complete (grossier -> etage
intermediaire -> pas raffine) est qualifiee : c'est ce que ce volet
joue.

LE CONTROLE DE REPRODUCTIBILITE (v11, section 9bis) : T-1, T-1b, T-3,
sans delta, se rejouent A L'IDENTIQUE et leurs cles se comparent au
run 85 (644240dc894c2733) ; perimetre ENUMERE ET CLOS -- /T1, /T1b,
/T3a, /T3b a profondeur declaree, deposes avec la prediction (N-70) ;
tout le reste HORS PERIMETRE PAR CONSTRUCTION, y compris /T2 ;
exemptions duree/chemins a l'interieur, enumerees avant le run ; ecart
sur cle du perimetre -> NON CONCLUANT D'INSTRUMENT avant toute
lecture. Ce n'est pas une qualification neuve, et la v9 ne la presente
pas comme telle.

TOLERANCE DU 9bis ENTRE MACHINES, MESUREE AU GESTE (2) (delta 90 nn.5) :
les cles de classe EXPOSEE-LIBM -- les quatre tol_int a appel libm,
tol_ordre et tol_ordre_sur_1 -- se comparent entre machines A 2 ULP
(residuelle glibc/UCRT mesuree a 1 ulp, degre-selective, p = 7) ; toute
autre cle du perimetre au bit, exemptions N-70 comprises ; c'est l'issue
(c) de N-70, prise ici pour ce gel. LA LIGNE DE PLATEFORME de tout journal
de run (pre-vol, temoin, alpha) porte le temoin d'arrondi EXECUTABLE
(1765.6704444885254) ** 6 en tableau numpy, en hexadecimal, plus la version
de numpy et le niveau de dispatch : ...9c6 correctement arrondi (BOCAL4,
libm UCRT ; machine 1 avec NPY_DISABLE_CPU_FEATURES=X86_V4), ...9c5 sous le
noyau SIMD (machine 1 sans levier). Un run joue sous ...9c5 est NON
CONCLUANT D'INSTRUMENT avant toute lecture.

LD-16, RE-ANCREE (decision (i) du delta 90, prise ici pour ce gel) : le
plancher c_pl x eps x N de LD-16 lit c_pl = 10 comme PARAMETRE DU REGLAGE
DEPOSE (run 85, 6d7d23130e9322f8, cle /reglage/c_pl = 10), repris tel quel
au reglage v6 ; la clause 5.4 abrogee par la v11 n'en est plus la source.
Le v9 emet la cle c_pl_ld16_herite comme le v8, sa provenance est celle-ci.

Aucun run du volet A n'est opposable avant le verdict REGLAGE QUALIFIE
(ou PASSE) du volet T sous la **v11 et son erratum 7 (i)**, jouee sous LE
MEME reglage (delta' = 1/44100, r, M, k, la regle du pas par etage) et sur
le meme instrument (v9, du) ; sa prediction se depose avant le run par ENUMERATION des
cles, avec la profondeur du perimetre 9bis et ses exemptions, CLOSES
(N-70). Le verdict du volet T est lu par machine 2 sur BOCAL4, au
depouillement du run depose -- jamais avant, par personne (D-M17-46).
Volet T non qualifie -> **ARRET DE PORTE**, le volet A ne se joue pas,
et le delta l'ecrit tel quel.

=======================================================================
6. LES NOMBRES DE CE GEL (regle 13) -- derives d'abord, tapes ensuite
=======================================================================

    delta' = 1/44100    DERIVE en 3 (le pre-vol est le nombre, regle 3.2)
    n = 21              choisi par le balayage, jamais tape (3.2)
    kT = 1.3666, m = 1.5247 DERIVES en 3.3 (les marges se mesurent, ne se tapent pas)
    cascade 3.5         pre-enregistree, sur verdict de porte seulement
    r = 1/10, M = 20, k = 2, k' = 4, eta = 1/4, dt_1 = 0.006,
    T_MAX = 400, c_pl = 10   INCHANGES, cites du v5 section 6 et du reglage
                        du run 85 (cle /reglage, 6d7d23130e9322f8)

====
7. LA PORTE DU PLANCHER (G-plancher) -- la question meme du banc
=======================================================================

Au depouillement, par degre, sur les grandeurs DU RUN :

    G-plancher MORD au degre p si tol_lnA(p) <= plancher_lnA(p)
    (la dispersion de la grille ne depasse pas le plancher : le modele
    fixe encore la tolerance, P-A n'y est pas une mesure).

JUSTIFICATION DE BORD (regle 15, ecrite) : tol_lnA = max(dispersion,
plancher) PROPAGE le double IDENTIQUE du plancher quand celui-ci
domine ; l'egalite du test est alors une egalite d'objet, pas une
coincidence d'arrondi -- la comparaison de bord est exacte par
construction. Au cas d'egalite au bit dispersion == plancher, max()
rend l'un des deux memes doubles et G-plancher MORD : cote
conservateur, le banc prefere se taire que mesurer au bord.

Un degre mordu est **NON CONCLUANT DE PLANCHER**. S'il ne reste pas
TROIS degres exploitables et non mordus, le banc rend NON CONCLUANT DE
PLANCHER global. `tol_lnA(p)/plancher_lnA(p)` se CONSIGNE a chaque
degre, passe ou non (v5 10.3) -- attendu de conception : 1.74 / 1.52 / 3.49
aux p = 4 / 5 / 7 (3.3, m = 1.52 au plus contraint), mais c'est le run qui
parle, pas la conception.

G-plancher se compare a une grandeur qui ne contient pas son ecart et
qui porte une echelle (le plancher, fixe par le modele et delta') : il
est conforme a la proposition non prise (a) du 85 sans la prejuger.

=======================================================================
8. LA CASCADE -- v5 section 9, une branche s'insere
=======================================================================

    branche 3b  G-plancher (section 7) -> **NON CONCLUANT DE PLANCHER**.
                Elle se lit APRES la branche 3 (G-fen) et AVANT la
                branche 4 (G-s / G-w2).

Ordre de lecture complet : porte T (5) -> branche 0 (G-lignee) ->
1 (G-seuil) -> 2 (G-dt / G-k) -> 3 (G-fen) -> 3b (G-plancher) ->
4 (G-s / G-w2) -> 5/6/7 (P-alpha puis P-A, v5). NON CONCLUANT n'est
pas une refutation ; REFUTE n'est pas un echec.

=======================================================================
9. LECTURE CONSIGNEE L-desc -- elle ne decide RIEN, et sa portee est
   CHIFFREE AVANT LE RUN
=======================================================================

Par point sur-seuil, cellule du plan (dt_2b, k = 2) contre la cellule
du plan du 85 (cle /degres/p/gA_sur_K, 6d7d23130e9322f8) :

    R_point = ln(g A'^(p-2) / K) / ln(g A_85^(p-2) / K)

Les dix-huit denominateurs, cites verbatim du 85 :

    p = 4 : 1.73|1.05 1.0002255189790104   1.73|1.20 1.0002220245707594
            2.27|1.05 1.0002263374195814   2.27|1.20 1.0002248081041585
            2.80|1.05 1.0002242012315197   2.80|1.20 1.0002235024850268
    p = 5 : 1.73|1.05 1.0003232252819152   1.73|1.20 1.0003513564092497
            2.27|1.05 1.0003635764885663   2.27|1.20 1.000350628716041
            2.80|1.05 1.0003359379708845   2.80|1.20 1.0003404002878518
    p = 7 : 1.73|1.05 1.0007773567104048   1.73|1.20 1.001585286092158
            2.27|1.05 1.000683162652881    2.27|1.20 1.000422996112198
            2.80|1.05 1.0004030732548506   2.80|1.20 1.0005382392075273

(le rapport R_point se calcule sur les logarithmes de ces valeurs, pas
sur les valeurs).

ATTENDU A L'ORDRE DOMINANT, ecrit avant le run : si l'ecart du 85 est
le terme neglige de la fenetre, R_point ~ delta'/delta_0 = 1/441 =
2.2676e-03. Si R_point ~ 1, l'ecart du 85 n'etait PAS le terme de
fenetre : structure reelle, a consigner.

PUISSANCE, CHIFFREE AVANT LE RUN (E27 ; lecon M15 ; trouvaille 2,
transmission 09c4bdc1f01d782f, re-derivee machine 1) : le bruit sur
R_point est la dispersion de la grille portee sur ln(g A^(p-2)/K),
rapportee au meme denominateur :

    bruit_R(p) = dispersion_lnA_85(p) x (p-2) / |ln(g A_85^(p-2)/K)|_moy
    signal_R   = delta'/delta_0 = 1/441 = 2.268e-03

    p    bruit_R(p)    bruit/signal   par degre /sqrt(6)   les 18 /sqrt(18)
    4    1.7624e-02          7.8x              3.2x                1.8x
    5    2.0866e-02          9.2x              3.8x                2.2x
    7    5.0582e-02         22.3x              9.1x                5.3x

**L-desc REFUTE R ~ 1 (structure persistante) a 8 a 22 fois le bruit ;
elle NE CONFIRME PAS R ~ 1/441, qui est indistinguable de R = 0 a la
dispersion du 85. Lecture a UN SEUL SENS, portee declaree avant le
run.** Entre les deux : consigne tel quel, sans interpretation. Si
R ~ 1 sortait, P-A l'aurait deja dit (un biais persistant de 2.2e-04 a
1.6e-03 creve une tolerance a ~2e-06) : L-desc en est le diagnostic
NOMME, pas le juge. Aucune branche, aucune tolerance : dix-huit nombres
au delta.

=======================================================================
10. L'INSTRUMENT v9 -- DU AVANT TOUT RUN
=======================================================================

Part du v8 CERTIFIE (banc_qualification_machine1_v8.py 4d8882a2223a5c74,
note machine 2 2a618ffb180ea568, selftest 103/103), construit par
construction_gel_v6_et_banc_v9_machine1_v1.py : les seuls remplacements sont
le reglage (DELTA = 1/44100 ; B_DESC, M_MARGE, J_DESC = 21, 1, 2 -- la racine
de descente vaut 21, PURE ; le selftest du reglage et ses attentes 3.3, 4.6,
4.7 re-derivees ; les tables du gel ; la cle /reglage/delta du JSON) et les
mentions de 1/102400, 620 et 1/1024 des commentaires ; RIEN d'autre. Toutes les tables se re-derivent de DELTA au chargement, comme au
v8. Le v9 se re-certifie EN ENTIER par machine 2 (selftest, banc qui tue,
NE-JOUE-PAS) et son pre-vol se joue des deux cotes au reglage v6 avant tout
run. Les exigences du v4 ci-dessous restent celles du v9 (elles sont
portees par le v8 depuis le 29/08, neuf defauts D-I leves) :

    (i)   D-M17-51 : les deux en-tetes de code perimes de la v3,
          corriges et cites au gel qu'ils servent ;
    (ii)  D-M17-58 : la garde de signe au pre-vol,
          `table_factice[(p, w2, sgn)] == sF`, jouee au moteur factice ;
    (iii) les etages 2a/2b sur-seuil (4.2) ET les etages 2s/2b'
          sous-seuil ancres en t (4.7), avec leurs sorties -- l'etat
          complet a la bascule (5.7 du v5) ET a chaque depart d'etage
          (4.9, exigence de CE gel), empreintes ; AUCUN compte d'etage
          n'est asserte dans le code : les comptes se MESURENT et se
          consignent, toute garde de compte se compare aux intervalles
          derives de 4.6/4.7 (pas nominal) et 4.8 (jumelle) ;
    (iv)  la branche 3b et la consignation tol_lnA/plancher ;
    (v)   la lecture L-desc (dix-huit rapports, consignes, avec la
          portee de 9 rappelee dans le journal).

Le selftest et le banc qui tue s'ETENDENT : le banc DOIT tuer la
branche 3b (un cas synthetique ou la dispersion tient sous le
plancher), l'etage 2a (un cas ou son absence casse la bascule 2b),
l'etage 2s (un cas sous-seuil ou son absence casse la fenetre lue), la
garde (ii), et il joue un cas ou n_2s > 620 SANS morsure -- un 620
asserte quelque part est un banc mort. Un banc qui n'assert pas sa
branche est degenere. Les gardes s'enumerent depuis le texte des gels
(section 8 du v5 + 5 et 7 d'ici) et le journal dit ce qu'il NE JOUE
PAS.

Certification machine 2 ENTIERE (selftest, banc qui tue, gardes
demontrees, NE-JOUE-PAS), pre-vol opposable machine 2 (N-62, E19), et
depot de l'instrument, de ses certifications et de la prediction
enumeree AVANT le run reel -- l'ordre du 85 (arbre e800c71) fait
modele. Tout byte-patch passe `all(x < 128 for x in bytes)`.

=======================================================================
11. LES COMPTES
=======================================================================

Volet A : identiques au v5 4.5 -- plan 18, G_dt 18, G_k 18, G_seuil 9,
G_lignee 27 ; `comptes + sautes == 90`. Volet T : les comptes de la
**v11** (et son erratum 7 (i)) -- ATTENDUS = 41 (voie A), en forme derivee. Chaque compte en
forme derivee, jamais recopie.

=======================================================================
12. CE QUE CE GEL NE DIT PAS
=======================================================================

    (i)   si G-plancher mord, la constante n'est toujours pas mesuree,
          et le banc le DIT au lieu de le cacher dans une tolerance ;
    (ii)  une derive commune aux dix-huit points, d'origine
          instrumentale et insensible a (dt, k), resterait invisible a
          la dispersion ; G-dt et G-k la bornent, et L-desc separerait
          une structure PERSISTANTE (elle refute R ~ 1 ; elle ne peut
          pas confirmer 1/441, section 9) ;
    (iii) la double transcription de (2.11) du temoin reste une dette,
          detenue machine 2 seule -- elle se declare a la citation
          (85.7bis) et ce gel ne la solde pas ;
    (iv)  rien ici ne parle du temps jusqu'a l'explosion (etape 3 de
          l'horizon) : s'il se derive, il se derive AVANT de se jouer ;
    (v)   delta' est pris dans la fenetre de la tenaille, une grandeur
          d'INSTRUMENT (ratios du pre-vol et dispersion du 85) : aucune
          valeur de A n'entre dans ce choix, et la cascade 3.5 ne se
          declenche que sur un verdict de porte ; l'arbitrage du 29/08
          (une marge, pas les deux) est tranche ici par le balayage,
          n = 21, les deux marges partielles, a la plume de machine 1
          sous veto de l'operateur.

=======================================================================
13. PIECES CITEES (convention B, 16 hex, sauf mention brut)
=======================================================================

    gels/alpha_pre_enregistrement_v5.md                045c2435aaf623ce  28998
    temoin_negatif_pre_enregistrement_v9.md            403488b4f6c319e9  57914  (m2, CERTIFIE)
    note_machine1_certification_temoin_v9_v1.md        b5da74783e5f97c6   7085
    gels/temoin_negatif_pre_enregistrement_v7.md       8b083e9f109b5a8e  39750  (gel du 85, depose)
    temoin_negatif_pre_enregistrement_v8.md            7ba4af8140b7a385  52661  (NON CERTIFIEE, remplacee)
    note_machine1_certification_temoin_v8_v1.md        ded4a5721601bd1e   8959
    runs/run_alpha_delta85/resultats_alpha.json        6d7d23130e9322f8
    runs/run_temoin_delta85/resultats_temoin.json      644240dc894c2733
    scripts/banc_qualification_machine1_v3.py          5fae2a8c94cf8685  144725
    scripts/m9_replication_v1.py (moteur, brut)        c8ed357b120352c4
    runs/m12_results.json (carte, brut)                fa109da92e582520
    journal/journal_delta_85_deux_bancs_alpha_verifie_v2.md  9c7ee2578464c94a
    journal/journal_delta_84_arbitrage_78_7_v1.md      fff42f489696c7ed
    POUR_MACHINE1_constante_A_v1_deux_trouvailles_v1.md  09c4bdc1f01d782f  8247
    POUR_MACHINE1_constante_A_v2_compte_2s_v1.md       67a4be1d02b89748  3279
    note_machine2_transposition_temoin_v7_delta_prime_v1.md  a6f2f6e27075cda9  10827
    note_machine2_certification_constante_A_v3_v1.md   52f76b9b82e7c861  11774
    certif_constante_A_v3_machine2_v1.py               1fa0c0eb3a341e09  10417
    certif_constante_A_v3_machine2_v1.log              a92f60f936a2f75a   7385  (brut : fichier CRLF, 119 CR ; convention B a98b21ecd7c56d95)
    constante_A_pre_enregistrement_v1.md (remplacee,
      non editee)                                      a860ad06e481a1ec  18514
    constante_A_pre_enregistrement_v2.md (remplacee,
      non editee)                                      69dd3c6a1e8a21f4  24038
    constante_A_pre_enregistrement_v3.md (remplacee,
      non editee)                                      d71770d5948fe1aa  28724
    constante_A_pre_enregistrement_v4.md (remplacee,
      non editee)                                      011c923203fcdaef  30988
    note_machine2_certification_constante_A_v4_v1.md   9e6376f936708077  11359
    SUIVI_campagne_2026-08-28b.md                      b6d13e6a1559e850
    depot : arbre a4a907a (registre public), au-dessus de e800c71

Empreinte de ce fichier : au gel, apres certification machine 2, par
sha256sum sur le fichier entier, newline final compris (convention du
2026-07-27).

Pieces ajoutees par la v6 (toutes au registre a e68341f, delta 90) :
    constante_A_pre_enregistrement_v5.md              2c0d2dc86054838c  REMPLACEE
    derivation_fenetre_delta_machine2_v3.py / .log    4353c80e60cef87c / f60104c0c3ba7ec4
    temoin_negatif_pre_enregistrement_v11.md          a2e7ef3e237c5acf  GEL DU VOLET T
    erratum_temoin_v11_clause_7i_tolerance_v1.md      13601ef21efdc024
    enumeration_cles_prevol_N70_machine2_v2.md        4867dffe3392dea6
    banc_qualification_machine1_v8.py                 4d8882a2223a5c74  CERTIFIE, REMPLACE PAR LE v9
    m2_v8_prevol_temoin_resultats.json                0a24121e441cc0c3  (pre-vol branche 4, BOCAL4)
    prevol_temoin_v8_machine1.log                     c45ac9f59907fbf4  (pre-vol branche 4, machine 1)
    journal_delta_90_constante_A_v2.md                11f86226cf4aa612  (l'acte qui consigne tout cela)
    banc_qualification_machine1_v9.py et son script de construction : empreintes au manifeste du lot v6

-- FIN constante_A_pre_enregistrement_v7 --
