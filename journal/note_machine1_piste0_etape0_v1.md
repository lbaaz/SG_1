# NOTE DE LECTURE -- PISTE (0), ETAPE 0 -- machine 1 -- 11/11/2026
# Lecture a zero run des artefacts du run M17 -- CLASSE 3, hors chaine

Pieces : lecture pre-declaree 20cbc762d58ce1ca (ecrite et empreintee AVANT
l'ouverture des points) ; script v1 c5debf99604d3c28 ; script v2 = v1 + 7
remplacements a ancre unique (trois defauts de la plume, section 4) ; les
cinq lectures rendent le meme resultat sous v1 et v2. Les nombres MESURES
de cette note sont ecrits par code depuis le JSON v2 ; seuils, annonces et
libelles de fichiers sont du texte.

## 1. AUTHENTIFICATION
Dossier manche_m17_v17 recu de l'operateur en un ZIP : 36 pieces au canon
et a la taille + 0 differente + 0 absente == 36 lignes du manifeste
machine 2 (4aecd0e2b23bc818, au registre). Aucune de ces 36 pieces n'est
au registre, sauf l'assemblage : detention unique a declarer.

## 2. TABLE DES SIX POINTS f070 (w2 = 1.95, 1.97, 1.98, 2.02, 2.03, 2.05)
  eta                0.05       0.03       0.02       0.02       0.03       0.05
  r_c                  40         40         40         41         41         41
  N                    60         60         60         61         61         61
  G (eta/8)     2.162e-10  1.298e-10  8.442e-11  6.562e-11  9.008e-11  2.661e-09
  Richardson    2.158e-10  1.314e-10  8.736e-11        nan  9.004e-11  2.525e-09
  r                 0.264      0.472      0.638      2.311      0.094      0.645
  residu           0.0022     0.0127     0.0355        nan     0.0005     0.0497
  pas 1            0.0226     0.0171     0.0264     0.0904     0.1150     0.0127
  pas 2            0.0233     0.0302     0.0316     0.0039     0.0469     0.0424
  pas 3            0.0062     0.0142     0.0201     0.0091     0.0044     0.0273
  2 eta            0.1518     0.1713     0.1823     0.2204     0.0916     0.0621
  translation      0.0196     0.0034     0.0111     0.0308     0.0056     0.0025
  N + p            0.0156     0.0019     0.0058     0.0039     0.0027     0.0029
  recouvr.         0.0288     0.0280     0.0275     0.0437     0.0434     0.0431
  poids total      0.8671     0.8496     0.8450     0.9978     0.9977     0.9977
  n reson.            136        120        123         82         82         82
  G pondere     9.892e-04  4.838e-04  3.540e-04  5.703e-06  8.606e-06  1.359e-05
  Gp / G          4.6e+06    3.7e+06    4.2e+06    8.7e+04    9.6e+04    5.1e+03
  jumeau H+      -1.2e-14    6.8e-15    5.8e-14   -1.3e-14   -6.5e-14   -7.5e-14

## 3. LES CINQ LECTURES
L-1 (coherence, non aveugle) : TIENT. Budget max = 0.0497 (au point 2.05,
    c'est le residu declare, a 99.4 pour cent du seuil 0.05) ; etendue de G
    x40.6. La structure en w2 n'est pas faite par l'absorbeur A L'ECHELLE
    DES PORTES ; le pic 2.05 vaut x12.3 le second point et x40.6 le plus bas.
L-2 (aveugle, annoncee 0.5) : NE TIENT PAS. Aucun indicateur d'identite
    hors plage a 2.05.
L-3 (aveugle, annoncee 0.6) : TIENT. Aucun indicateur d'absorbeur hors
    plage a 2.05. Par la table pre-declaree : pic SANS SIGNATURE, l'etape
    0 n'apprend rien sur lui. Le creux 2.02 : rien hors plage non plus.
L-4 (aveugle, annoncee 0.4 qu'elle tienne) : NE TIENT PAS. rho(G, Gp) =
    19/35 contre 29/35. Exploratoire, sans verdict : rho(Gp, -Lambda_c) = -27/35
    (P6 (i) rejoue sur G : 1/35, identique a l'assemblage).
L-5 (aveugle, annoncee 0.6) : NE TIENT PAS. Signe du dernier pas : 1.95:-1 1.97:+1 1.98:+1 2.02:+0 2.03:-1 2.05:-1
    (0 = non defini). Les six points ne sont pas au meme endroit de leur
    trajectoire en eta. Les ecarts en jeu restent sous 5 pour cent.
Bilan des annonces : L-3 (0.6) tenue ; L-5 (0.6) et L-2 (0.5) non tenues ;
    L-4 (0.4) non tenue, dans le sens annonce.

## 4. DEFAUTS DE LA PLUME (verses, corriges en v2 par hunks nommes)
D-P0-1 : la regle HORS PLAGE rendait 'dans la plage' sur une valeur non
    finie (residu a 2.02) -- silence deguise en passage. v2 : NON LISIBLE.
D-P0-2 : rho(G, R) calcule avec un R non fini rendait 33/35 ; sur les 5
    points ou R existe, rho = 1. v2 : compte declare.
D-P0-3 : le signe de L-5 n'existe que si 0 < r < 1 ; v1 rendait -1 a 2.02.
D-P0-4 (conception, NON corrige) : l'ensemble de reference O melange deux
    familles (section 5), sa plage contient presque tout : la regle de
    L-2 / L-3 etait sans puissance. Elle reste comme ecrite.

## 5. OBSERVATIONS HORS PRE-DECLARATION (post hoc, aucune lecture attachee)
O-1 : DEUX FAMILLES de part et d'autre de 2:1. A gauche (1.95, 1.97, 1.98) :
    r_c = [40], poids total 0.845 a 0.867, recouvrement 0.0275 a 0.0288, 120 a 136
    resonances retenues. A droite (2.02, 2.03, 2.05) : r_c = [41], poids
    total 0.9977 a 0.9978, recouvrement 0.0431 a 0.0437, [82] resonances.
    La base propre est nettement non orthogonale sur le support de la
    graine a gauche, presque orthogonale a droite. Le NOMINAL de toute la
    qualification de l'instrument (1.95) est dans la famille de gauche.
O-2 : Gp / G va de 5.1e+03 a 4.6e+06 : la largeur ponderee n'est pas une autre
    estimation du meme taux, c'est un autre objet, domine par des etats
    larges : l'etat retenu y contribue pour rec x G, soit 6e-09 a 8e-06 de
    Gp. Une lecture faite sur elle (dont R5) lit cet autre objet.
O-3 : a 2.02, r = 2.311 : le dernier pas est plus grand que le precedent,
    Richardson et residu n'existent pas ; l'operatif du gel 4.6 y est
    vide et P6 a lu la valeur brute. Point EN DOMAINE malgre cela.
O-4 : G / |H+| va de 3.1 a 4.5 ordres de grandeur (la note de run ecrit
    'quatre a cinq') ; H+ est joue a eta, H a eta/8. A la plume de m2.
O-5 : P8 a g = 0.001 : plus grand pas de descente 2.2e+30 (L = 20) et 1.0e+30
    (L = 30), descente rejetee aux deux longueurs --
    largeur sous le plancher numerique. Les six f050 sont en arret par
    E-A (chaine), pas par E-B.

## 6. CE QUE CELA CHANGE POUR L'ETAPE 1
(a) T-etats passe en premier et se lit PAR COTE ; y ajouter le
    conditionnement de l'etat retenu et les poids BI-ORTHOGONAUX (produit
    c, H complexe symetrique), qui somment a 1 la ou les |c_nu|^2 du
    script somment a 0.845 au plus bas.
(b) T-eta inchange, avec 2.02 comme point a tourner (r > 1).
(c) La largeur ponderee sort de l'instrument comme 'taux'.
(d) Temoin positif inchange. Rien ici ne qualifie l'estimateur.

-- FIN --
