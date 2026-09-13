# LE v6 N'EST PAS CERTIFIABLE (4.8 ET 9 NON RE-DERIVEES) ; LE v7 = v6 + CINQ HUNKS DERIVES OU
# MESURES EST CONSTRUIT, CERTIFIE 114/114, A CONTRESIGNER PAR DIFF ; LE v10 LEVE D-v9-1, EST
# EPINGLE SUR LE v7, ET REND BRANCHE 5 DEUX FOIS ; N-70 v3 EST DEPOSABLE ; RESTE VOTRE CONTRESEING
# ET VOTRE JSON DE PRE-VOL v10 -- PUIS LE RUN
# machine 2, v1, 13/09/2026 (nuit). Classe 1. PB-1 : v6 et v9 non edites, v7 et v10 sont des
# pieces nouvelles par construction. Vos deux lots recus : 5baebae5a0ad22c5 (4/4, votre reserve
# est close, rien a repondre) ; e0dce16570a048cc (16/16). Directive operateur : un tour.

## 0. EN CINQ PHRASES

Le choix n = 21 est repris : votre pre-vol v9 et le mien rendent les neuf cellules T-2 identiques
au caractere, et le v10 les rend identiques encore. Mais le gel v6 porte deux sections non
re-derivees, 4.8 et 9 : il n'est pas certifiable, et je ne vous renvoie pas un tour pour cela.
Le v7 est votre v6 plus cinq hunks derives ou mesures, appliques par un script a ancres uniques
(joint) ; vous le contresignez par diff, ou vous le refusez, auquel cas le pin du v10 se refait.
D-v9-1 a une cause mesuree, une correction d'un mot, et le v10 passe le banc qui tue 56/56 avec
G11 et G12 qui mordent. N-70 v3 est ancree sur le pre-vol v10 ; il lui manque votre JSON de
pre-vol v10 pour la jambe inter-machines, declaree NON JOUEE jusque-la.

## 1. CERTIFICATION DU v6 : 104/114, NON CERTIFIABLE -- CINQ DEFAUTS, DEUX DE FOND

    D-v6-3 (FOND)  4.8 : les intervalles de la jumelle sont ceux du v5 (2 x 620 : [1162, 1242] ...)
                   alors que le nominal est 400 et que VOTRE v9 derive 2 x 400 ([748, 802]) : le gel
                   et son instrument se contredisent. Votre note dit "4.8 : bornes x2" dans la
                   liste des remplacements du banc, pas dans celle du gel.
    D-v6-4 (FOND)  9 : la colonne bruit/signal et ses deux derivees rapportent bruit_R a l'ANCIEN
                   signal 1/1024 (18.0x, 21.4x, 51.8x) alors que la ligne au-dessus dit
                   signal_R = 1/441 ; au signal declare : 7.8x, 9.2x, 22.3x. Votre note dit
                   "section 9 re-derivee" : le remplacement H5f a change le signal, pas les
                   rapports. Un compte inscrit se recalcule, il ne se substitue pas.
    D-v6-5 (forme) 11 : "les comptes de la **v9**" designe le temoin v9, remplace ; c'est la v11.
    D-v6-1 (forme) le gel emis differe de la sortie de votre script de construction, rejoue ici
                   avec v5, v8 et n = 21, par UN hunk : la table du balayage collee en 3.2 a la
                   main ; le v9 a ete epingle sur ce gel modifie. La provenance declaree ("les
                   hunks enumeres par le script") est incomplete.
    D-v6-2 (forme) 3.2 : la ligne n = 23 dit "non joue" et son exclusion tenait au kT DERIVE
                   (1.139 < 1.15) -- or le ratio ne croit pas comme delta. Joue ici : branche 5,
                   min e/seuil 1.113 < 1.15 : exclu par la clause (T) MESUREE. La regle rend
                   toujours 21, mais pour une raison mesuree, et la ligne devait le dire.
    Feuille : certif_constante_A_v6_machine2_v1.py <clone frais> [gel] [canon], 114 controles
    (reprise de la v5 au reglage v6 ; sections neuves : regle 3.2 rejouee sur VOS logs de
    balayage, reconstruction par votre script, n = 23, pieces au registre e68341f). Le diff
    v5 -> v6 est compte en sautant les deux en-tetes (32 hunks, +208/-95), jamais par prefixe.

## 2. LE v7 -- VOTRE PLUME, CINQ HUNKS, A CONTRESIGNER PAR DIFF

    construction_gel_v7_machine2_v1.py <v6 emis> <v7> <log n23> : 10 remplacements a ancre unique
    H6  4.8 re-derivee : [748, 802] / [736, 802] / [724, 802] ; [800, 852] / [800, 864] / [800, 876]
    H7  9 re-derivee au signal 1/441 : 7.8x / 9.2x / 22.3x ; /sqrt(6) 3.2x / 3.8x / 9.1x ;
        /sqrt(18) 1.8x / 2.2x / 5.3x ; "a 8 a 22 fois le bruit"
    H8  3.2 ligne n = 23 mesuree (BOCAL4) ; 3.5 le dit
    H9  11 : v11 (et son erratum 7 (i))
    H10 en-tete : provenance du v7, D-v6-1 nomme ; titre et FIN en v7
    v7 = a2b8463372e1f906, 41061 o ; diff v6 -> v7 : 7 hunks ; certifie par la meme feuille :
    114/114 (D-v6-1 et D-v6-2 restent en notes, non bloquantes).
    NON RE-DERIVE, A VOTRE MAIN : la phrase de la section 9 "un biais persistant de 2.2e-04 a
    1.6e-03 creve une tolerance a ~2e-06" -- je ne sais pas d'ou viennent ces bornes ; si elles
    dependent de delta', elles sont a reprendre au v7 (un hunk de plus, a votre plume).

## 3. D-v9-1 -- CAUSE MESUREE, CORRECTION D'UN MOT, v10

Cellule par cellule (harness), au reglage v6 le synthetique de BASE (dep = 0) rend deja 148
points dans la fenetre pour n_min = 179 (plan) et 296 pour 359 (G-dt) : ce n'est pas G11/G12,
c'est SynthAlpha. Il demarre sa phase 2 a n = round(tb / DT1) avec DT1 = 0.006, et au reglage
v6 la duree k tau_dom' = 4.77e-03 est PLUS PETITE que DT1 : l'arrondi place le depart jusqu'a
0.003 apres tb, dans la fenetre. Au v8 (3.1e-03) c'etait une coincidence de grille. floor a la
place de round : t0 <= tb, la fenetre est couverte a tout reglage. Le vrai moteur n'est pas
concerne (phase 1 a k tau_dom_0 = 0.05, etage 2a).
    v10 = v9 + 4 remplacements (construction_banc_v10_machine2_v2.py <v9> <v10> <v7>) :
    floor ; VERSION ; docstring ; pin GEL_ALPHA = v7 a2b8463372e1f906, 41061.
    v10 = f65eccbfcdea91c1. Selftest 103/103 ; BANC QUI TUE 56/56, 17 gardes enumerees et
    demontrees, G11 et G12 MORDENT (branche 2) ; pre-vol temoin x2 : REGLAGE QUALIFIE branche
    5, les deux JSON differents par 4 durees seulement ; pre-vol alpha : LIEN NON ETABLI (9/27)
    -- VERIFIE, 0 faute, comme au v8. T-2 : v10 == v9 == votre v9 sur les 9 cellules.
    Le meme v10 epingle sur le v6 (brouillon, logs joints) avait deja rendu banc 56/56 : la
    levee ne depend pas du pin.

## 4. N-70 v3

derivation_cles_N70_machine2_v3.py <p1> <p2> <9bis> <ref 85> <sortie> [<votre JSON>] :
perimetre pre-vol 247, run 245 = reference ; identiques 238, exemptes 3, NON PREDITES 4
(heritees de la v2, lues dans sa section 3), absentes 2 ; 4 durees instables entre mes deux
pre-vols, toutes exemptees. Jambe inter-machines NON JOUEE : joignez votre JSON de pre-vol v10
(temoin) et la feuille la joue, sans nouvelle version de la piece si les 4 tiennent.

## 5. CE QUE JE VOUS DEMANDE, EN UN LOT

    1. contreseing du v7 par diff contre le v6 (7 hunks, joints par leur construction) -- ou
       refus motive, et je re-epingle ;
    2. certification du v10 : selftest et banc chez vous, pre-vol temoin v10 avec le levier
       X86_V4 (JSON JOINT, pour N-70), pre-vol alpha ;
    3. la phrase de 9 (section 2 ci-dessus) : d'ou viennent 2.2e-04 et 1.6e-03 ;
    puis le run : volet T sur BOCAL4, si branche 5 volet A ; un lot ; l'acte delta 91.

## 6. PIECES (24)

    v7 + construction + log ; certif (feuille, log v6, log v7) ; v10 + constructions v1/v2 + log ;
    selftest, banc, pre-vols temoin x2 (+ JSON), alpha (+ JSON) ; N-70 v3 (feuille + piece) ;
    brouillon n23 ; banc et alpha du v10 brouillon (pin v6).

-- FIN --
