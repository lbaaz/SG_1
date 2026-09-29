# NOTE MACHINE 1 -- GEL v10 ET INSTRUMENT v16 : MESURER A
# machine 1, v1, 29/09/2026. Go operateur du 29/09. Classe 3 ; le gel devient classe 1 a la
# certification m2. PB-1 : v9 et v15 non edites ; un seul script construit les deux.

## 0. EN QUATRE PHRASES
Le gel v10 = v9 certifie + 41 hunks : la regle du plus grand n (v7 3.2) restauree -> n = 21, le
barreau du 91 ; tous les nombres du reglage re-derives par la machinerie du v6/v8 (ancres a
n = 18, remplacements a n = 21) ; la MESURE de A definie avant le run (lnA_R par point, delta_p et
S(p) par degre, A(p) = (K/g)^(1/(p-2)) exp(delta_p), incertitude S + plancher_corr) ; trois
predictions en aveugle -- (a) le biais du premier ordre au levier 1, les biais C4 eux-memes a
p = 4 et 5 ; (b) le transport des modes libres du 92 vers le 91, levier 324/441 (x 0.7015,
+0.4465 rad), base = les (a, c) du 92 apres Richardson ; (c) NEUVE : le coefficient du terme
tau^2 AJUSTE LIBREMENT vaut c1 derive aux 18 points a 10 pour cent, la forme qui lit le premier
ordre a p = 7 sans projeter le mode. Le banc v16 = v15 certifie + 27 remplacements : reglage
n = 21, pin v10, une forme d'ajustement de plus (ajuster_c1_libre, cle ajustement_c1_libre :
c1_fit, erreur-type, lnA ; aucun verdict), et deux corrections du banc qui tue qu'il a fallu
faire pour qu'il tourne a n = 21.

## 1. LES DEUX CORRECTIONS DU BANC, MESUREES (elles sont a certifier avec le reste)
  D-v16-1 (memoire) : au scenario sans_cap, le synthetique integrait jusqu'a T_MAX_DEPOSE a
    dt_2b/4 -- 63 M pas a n = 21, 483 Mio par tableau -- et machine 1 (4 Go) tuait le banc a
    2.7 Go. Le v16 borne l'horizon du synthetique sans CAP a 20 N_2BP pas : le verdict (T_MAX
    -> G-fen) ne depend pas de la longueur, la memoire si. Le chemin reel n'est pas touche.
  D-v16-2 (G22) : au v15, la lecture corrigee de G22 etait NON JOUEE par ACCIDENT (le q du
    synthetique tombait hors [3, 5] a n = 18) ; a n = 21 il tombe dans [3, 5] a p = 5, la lecture
    corrigee s'y joue, son G-plancher ne mord pas et G22 ne rendait plus que deux degres sur
    trois. Le v16 rend la lecture NON JOUEE PAR CONSTRUCTION (mutation q = 2, helper au niveau
    module) ; G22 le dit dans son nom. Le v15 restait juste a n = 18 ; il ne l'aurait pas ete a
    tout reglage : c'est une fragilite de scenario, pas d'instrument.

## 2. LES EPREUVES SUR MACHINE 1 (levier X86_V4, clone frais 729f9a9, gel v10 au registre local)
  selftest 103/103 ; banc qui tue 58/58 (17 gardes) ; pre-vol temoin REGLAGE QUALIFIE branche 5 ;
  pre-vol alpha LIEN NON ETABLI (9/27) VERIFIE branche 5, ajustement_c1_libre present a chaque
  cellule, lecture corrigee NON JOUEE consignee (synthetique). Planchers corriges a n = 21,
  derives : 2.8041e-14 / 6.6050e-14 / 1.7174e-13 (proj4 = 0.2238 ; machine 2 a proj4 mesure par
  point rend 2.75e-14 / 6.48e-14 / 1.68e-13, coherent a 2 pour cent = le rapport des proj4).

## 3. LA FEUILLE lecture_v10 : essai a blanc sur le 92
  Sur mes series du 92 (v15, sans (c)), avec leviers 441/324 : elle rend EXACTEMENT la lecture
  v9 (121 controles, la meme morsure (a) p = 7 ; (b) 6/6), (c) NON JOUEE (18 points, cle absente)
  et la mesure de A -- a posteriori pour ce gel, non opposable : delta_p = +7.4e-11 / -2.0e-10 /
  -2.7e-10, S(p) = 3.54e-09 / 3.72e-09 / 3.52e-09, A(4) = 48.989794859 contre (K/g)^(1/2) =
  48.989794856. Ce que le v10 pre-enregistre a n = 21, le 92 le donne deja a n = 18 sans que
  personne l'ait annonce : c'est pourquoi ce gel le fait annoncer avant le run.

## 4. A CERTIFIER PAR MACHINE 2, EN UN PASSAGE
  gel par diff contre le v9 (41 hunks, nombres re-derives), v16 par construction depuis le v15
  (le script lit machinerie_reglage.py extrait de la construction du v8), selftest, banc 58/58,
  pre-vols a n = 21 sur BOCAL4, essai a blanc de lecture_v10 sur ses series du 92 ; puis le run
  sous v16 et lecture_v10 --predictions <base 92> 1 324/441 des deux cotes ; puis l'acte 93.

-- FIN note_machine1_gel_v10_banc_v16_v1 --
