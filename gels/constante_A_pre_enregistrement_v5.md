# PRE-ENREGISTREMENT constante A v5 -- LA FENETRE DESCEND JUSQU'A CE QUE
# L'INSTRUMENT, ET NON LE MODELE, FIXE LA TOLERANCE DE P-A
# BROUILLON MACHINE 1 -- DEVIENT GEL A LA CERTIFICATION MACHINE 2
# v5 = v4 (011c923203fcdaef, 30988 o, REMPLACEE, non editee) + UN hunk de fond : la morsure
# P-A-1 de la certification machine 2 du v4 (9e6376f936708077 ; 96 controles, 95 passent,
# 1 mord) est soldee en 13 -- la ligne du log certif v3 dit maintenant qu'elle cite le sha
# BRUT d'un fichier CRLF (119 CR) et donne sa convention B. Rien d'autre ne change au fond ;
# les hunks administratifs (ce bloc, la liste de 13, la ligne FIN) sont comptes au manifeste.
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
descend la fenetre (delta' = 1/102400, soit 1/1024 de la fenetre du 85)
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
3. LA DERIVATION DE delta' (regle 13 : en forme derivee)
=======================================================================

3.1 Condition de conception : le plancher de la nouvelle fenetre doit
tenir sous la dispersion MESUREE au 85, avec une marge m :

    plancher'(p) = delta' / ((alpha_p + 2)(alpha_p + 3))
                <= dispersion_lnA_85(p) / m       pour CHAQUE p

3.2 Descente declaree : delta' = delta_0 / b^J, delta_0 = 1/100,
b = 4, J minimal qui satisfait 3.1. Nombres purs de conception :
**m = 2** et **b = 4**. Rien d'autre ne se tape.

3.3 Resultat (Fraction, regle 15) : la borne de 3.1 est atteinte en
premier a p = 5 : min_p [ disp_85(p) x (alpha_p+2)(alpha_p+3) ] / m
= 2.393510486697892e-06 x (130/9) / 2 = 1.7286e-05. D'ou

    **J = 5    delta' = 1/102400 = 9.765625e-06    delta'/delta_0 = 1/1024**

    Temoin de minimalite : a J = 4, plancher'(5) = 9/3328000
    = 2.704e-06 > disp_85(5)/2 = 1.197e-06 -- la condition 3.1 echoue.
    J = 5 est le premier qui la satisfait.

    p    plancher'(p) exact      plancher'(p)      plancher'/disp_85
    4    1/2048000               4.8828125e-07     0.2470
    5    9/13312000              6.760817e-07      0.2825
    7    1/1089536               9.178219e-07      0.1235

Les trois planchers tiennent sous la MOITIE des dispersions du 85. Si
la dispersion du present run reste a son niveau, c'est l'instrument qui
fixe tol_lnA aux trois degres -- c'est la porte de la section 7 qui en
decide, sur les grandeurs du run, pas sur celles-ci.

3.4 PRECISION (D-alpha-9 transposee) : a tau_dom', le terme neglige
vaut AU PLUS delta' fois le terme dominant ; le rapport exact est
delta'/((alpha+2)(alpha+3)) = les planchers de 3.3. Aucun autre nombre.

=======================================================================
4. LES ETAGES DE PAS -- le seul changement d'instrument
=======================================================================

4.1 FAIT DERIVE, qui impose la structure : la bascule de la nouvelle
fenetre tombe a tau = k tau_dom' = 3.128e-03 / 2.520e-03 / 2.102e-03
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
    1.73    1.563889e-03   1.563889e-04   1.563889e-04   7.819443e-06
    2.27    1.259825e-03   1.259825e-04   1.259825e-04   6.299123e-06
    2.80    1.051051e-03   1.051051e-04   1.051051e-04   5.255256e-06

4.4 BASCULE 2b -- derivee par degre et par point (jamais partagee,
regle 11.1 v5) : bascule quand |x| >= A_p (k tau_dom'(w2))^(-alpha_p) :

                 w2 = 1.73     w2 = 2.27     w2 = 2.80
    p = 4        5.0077e+06    7.7166e+06    1.1087e+07
    p = 5        2.1098e+04    2.8147e+04    3.5838e+04
    p = 7        3.1701e+02    3.7687e+02    4.3566e+02

4.5 CAP'_p(w2) = A_p (tau_CAP'(w2))^(-alpha_p), fin de l'etage 2b :

                 w2 = 1.73     w2 = 2.27     w2 = 2.80
    p = 4        2.0031e+09    3.0866e+09    4.4346e+09
    p = 5        1.1454e+06    1.5280e+06    1.9456e+06
    p = 7        3.4826e+03    4.1402e+03    4.7859e+03

    Controle de debordement : max g |x|^(p-1) au CAP' = 4.361e+27
    (p = 4, w2 = 2.80), loin du plafond double (1.8e+308). Un
    debordement en cours d'etage rend le point NON CONCLUANT, COMPTE.

4.6 LE COUT -- NOMINAUX DERIVES, COMPTES MESURES. Un compte inscrit se
COMPTE, il ne s'affirme pas (transmission 67a4be1d02b89748 ; la
campagne a deja paye cette regle). Les etages sur-seuil sont a bornes
d'EVENEMENT : 2a part de la bascule 5.3 detectee sur la grille de
phase 1 et finit a la bascule 2b detectee sur sa propre grille ; 2b de
meme vers CAP'. Leurs comptes sont MESURES et CONSIGNES. Nominaux, en
nombres purs :

    n_2a nominal = M (sqrt(delta_0/delta') - 1) = 20 x 31 = 620
    n_2b nominal = M (k - r)/r = 380

Toute garde de compte se compare a l'intervalle DERIVE des deux effets
de grille (depart en retard d'au plus UN pas de la grille AMONT ;
arrivee en retard d'au plus UN pas de la grille PROPRE) :

    n_2a dans [ 620 - ceil(dt_1/dt_2a(w2)) , 621 ]
         soit [581, 621] / [572, 621] / [562, 621]   (w2 = 1.73/2.27/2.80)
    n_2b dans [ 380 - k/r , 381 ] = [360, 381]        (k/r = 20, pur)

Cout nominal de la descente : ~1000 pas par serie sur-seuil --
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
-- son compte n'est PAS 620 :

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

    620 <= n_2s <= 620 + ceil(dt_1/dt_2a(w2))
    soit [620, 659] / [620, 668] / [620, 678]    (w2 = 1.73/2.27/2.80)

Valeurs DERIVEES du reglage prime, re-derivees des deux cotes :
n_2s = 658 / 631 / 646 -- elles se VERIFIENT au run, elles ne
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

    n_2a jumelle : [1162, 1242] / [1144, 1242] / [1124, 1242]
    n_2b jumelle : [720, 762]
    n_2s jumelle : [1240, 1318] / [1240, 1336] / [1240, 1356]
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
   v9, CERTIFIE
=======================================================================

L'histoire, en une ligne, empreintes a l'appui : la passe de
transposition (a6f2f6e27075cda9) a fait tomber W-bascule a delta' ; la
v8 (7ba4af8140b7a385) l'a rendue jouable et n'a PAS ete certifiee
(note machine 1 ded4a5721601bd1e, trois reprises) ; la **v9
(403488b4f6c319e9, 57914 o) est CERTIFIEE** (note machine 1
b5da74783e5f97c6, 28/08) et prend la VOIE A, arbitree par l'operateur.

CE QUE LA PORTE EXIGEAIT, LA v9 LE PORTE : la remise d'etat aux
bascules -- l'organe que le reglage prime complique -- est qualifiee
par W-bascule EN DEUX ETAGES (v9, section 8) : g1 la phase grossiere
du v7, g2 l'etage 2a de ce volet, lecture D-t-19 ECRITE sur la
tolerance de 5.3 (iv), comptes derives aux memes intervalles que 4.6.
ATTENDUS = 41, conserves. La chaine complete (grossier -> etage
intermediaire -> pas raffine) est qualifiee : c'est ce que ce volet
joue.

LE CONTROLE DE REPRODUCTIBILITE (v9, section 9bis) : T-1, T-1b, T-3,
sans delta, se rejouent A L'IDENTIQUE et leurs cles se comparent au
run 85 (644240dc894c2733) ; perimetre ENUMERE ET CLOS -- /T1, /T1b,
/T3a, /T3b a profondeur declaree, deposes avec la prediction (N-70) ;
tout le reste HORS PERIMETRE PAR CONSTRUCTION, y compris /T2 ;
exemptions duree/chemins a l'interieur, enumerees avant le run ; ecart
sur cle du perimetre -> NON CONCLUANT D'INSTRUMENT avant toute
lecture. Ce n'est pas une qualification neuve, et la v9 ne la presente
pas comme telle.

Aucun run du volet A n'est opposable avant le verdict REGLAGE QUALIFIE
(ou PASSE) du volet T sous la **v9**, jouee sous LE MEME reglage
(delta', r, M, k, la regle du pas par etage) et sur le meme instrument
(v4, du) ; sa prediction se depose avant le run par ENUMERATION des
cles, avec la profondeur du perimetre 9bis et ses exemptions, CLOSES
(N-70). Le verdict du volet T est lu par machine 2 sur BOCAL4, au
depouillement du run depose -- jamais avant, par personne (D-M17-46).
Volet T non qualifie -> **ARRET DE PORTE**, le volet A ne se joue pas,
et le delta l'ecrit tel quel.

=======================================================================
6. LES NOMBRES DE CE GEL (regle 13) -- derives d'abord, tapes ensuite
=======================================================================

    delta' = 1/102400   DERIVE en 3 (la derivation est le nombre)
    J = 5               DERIVE en 3 (le minimal de 3.2 ; temoin de
                        minimalite en 3.3 -- il ne se tape pas)
    b = 4, m = 2        la descente et sa marge : les DEUX SEULS
                        nombres purs de conception qui se tapent (3.2)
    r = 1/10, M = 20, k = 2, k' = 4, eta = 1/4, dt_1 = 0.006,
    T_MAX = 400         INCHANGES, cites du v5 section 6 et du reglage
                        du run 85 (cle /reglage, 6d7d23130e9322f8)

=======================================================================
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
degre, passe ou non (v5 10.3) -- attendu de conception : > 3 partout
(3.3), mais c'est le run qui parle, pas la conception.

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
le terme neglige de la fenetre, R_point ~ delta'/delta_0 = 1/1024 =
9.7656e-04. Si R_point ~ 1, l'ecart du 85 n'etait PAS le terme de
fenetre : structure reelle, a consigner.

PUISSANCE, CHIFFREE AVANT LE RUN (E27 ; lecon M15 ; trouvaille 2,
transmission 09c4bdc1f01d782f, re-derivee machine 1) : le bruit sur
R_point est la dispersion de la grille portee sur ln(g A^(p-2)/K),
rapportee au meme denominateur :

    bruit_R(p) = dispersion_lnA_85(p) x (p-2) / |ln(g A_85^(p-2)/K)|_moy
    signal_R   = delta'/delta_0 = 1/1024 = 9.766e-04

    p    bruit_R(p)    bruit/signal   par degre /sqrt(6)   les 18 /sqrt(18)
    4    1.7624e-02        18.0x             7.4x               4.3x
    5    2.0866e-02        21.4x             8.7x               5.0x
    7    5.0582e-02        51.8x            21.1x              12.2x

**L-desc REFUTE R ~ 1 (structure persistante) a 18 a 52 fois le bruit ;
elle NE CONFIRME PAS R ~ 1/1024, qui est indistinguable de R = 0 a la
dispersion du 85. Lecture a UN SEUL SENS, portee declaree avant le
run.** Entre les deux : consigne tel quel, sans interpretation. Si
R ~ 1 sortait, P-A l'aurait deja dit (un biais persistant de 2.2e-04 a
1.6e-03 creve une tolerance a ~2e-06) : L-desc en est le diagnostic
NOMME, pas le juge. Aucune branche, aucune tolerance : dix-huit nombres
au delta.

=======================================================================
10. L'INSTRUMENT v4 -- DU AVANT TOUT RUN
=======================================================================

Part de banc_qualification_machine1_v3.py (5fae2a8c94cf8685). Prend :

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
**v9** -- ATTENDUS = 41 (voie A), en forme derivee. Chaque compte en
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
          pas confirmer 1/1024, section 9) ;
    (iii) la double transcription de (2.11) du temoin reste une dette,
          detenue machine 2 seule -- elle se declare a la citation
          (85.7bis) et ce gel ne la solde pas ;
    (iv)  rien ici ne parle du temps jusqu'a l'explosion (etape 3 de
          l'horizon) : s'il se derive, il se derive AVANT de se jouer.

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

-- FIN constante_A_pre_enregistrement_v5 --
