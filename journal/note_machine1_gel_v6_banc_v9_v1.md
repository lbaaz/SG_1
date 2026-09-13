# NOTE MACHINE 1 -- GEL constante A v6 ET BANC v9 : LE REGLAGE EST PRIS AU PRE-VOL, LA PORTE OUVRE
# machine 1, v1, 12/09/2026 (nuit). Classe 3 ; le gel devient classe 1 a la certification m2.
# Directive operateur : un gel propre, un envoi, pas de tours de forme. PB-1 : v5 et v8 non edites.

## 0. EN QUATRE PHRASES

Le gel v6 = v5 (2c0d2dc86054838c) + 26 hunks appliques par un script de construction a ancres
uniques ; le banc v9 = v8 certifie (4d8882a2223a5c74) + 26 remplacements du meme script, tables
et attentes du selftest re-derivees (103/103). Le reglage n'est plus tape : delta' = delta_0/n^2
et n est choisi par le PRE-VOL, sur l'echelle entiere n = 18..24, par une regle declaree avant le
balayage (3.2) -- n = 21, delta' = 1/44100, kT = 1.37, m = 1.52. Le pre-vol temoin a n = 21
rend REGLAGE QUALIFIE, branche 5, les neuf points lus : c'est la premiere fois. Un point reste
ouvert sur l'instrument, declare : D-v9-1.

## 1. LA TROISIEME MACHOIRE, TROUVEE PAR LE BALAYAGE

La tenaille (delta 90 nn.4) ne connaissait que W-plancher (borne T) et le biais du volet A.
W-pas, le test d'ordre |p_obs - 4| <= tol_ordre(p), est une troisieme machoire a p = 7 : il MORD
a n = 20 (7|2.27, p_obs 3.79) et a n = 22 (7|1.73, p_obs 3.81) alors qu'il PASSE a 18, 19, 21.
Il fluctue avec la grille et ne se derive pas au dixieme : d'ou la regle 3.2 (le pre-vol choisit,
la plus grande marge A parmi les n qui ouvrent la porte avec e/seuil >= 1.15). Table :

    n   delta'     kT     m      verdict du pre-vol temoin (machine 1, levier X86_V4)   min e/seuil  max |p_obs-4|/tol_ordre  gardes rejouees
    18  1/32400   1.860  1.120  branche 5 REGLAGE QUALIFIE                           1.868        0.62                    G11/G12 DEGENERES
    19  1/36100   1.669  1.248  branche 5 REGLAGE QUALIFIE                           1.631        0.59                    G11/G12 DEGENERES
    20  1/40000   1.507  1.383  branche 4 : W-pas 7|2.27 MORD                        1.527        1.22                    G11/G12 DEGENERES
    21  1/44100   1.367  1.525  branche 5 REGLAGE QUALIFIE                           1.433        0.79                    G11/G12 DEGENERES
    22  1/48400   1.245  1.673  branche 4 : W-pas 7|1.73 MORD                        1.356        1.12                    G11/G12 DEGENERES
    23  1/52900   1.139  1.829  pre-vol NON ABOUTI (interrompu ; exclu par la regle : kT < 1.15)   -            -                       -
    24  1/57600   1.046  1.991  branche 4 : W-plancher 7|1.73 MORD                   0.907        0.80                    G11/G12 DEGENERES


    n = 23 et n = 24 rendent branche 4 (voir la table) ; n = 17 aurait m < 1 (plancher au-dessus de la dispersion a p = 5).
    Les pre-vols des deux machines doivent concorder au bit (levier X86_V4 ici) : le balayage
    se rejoue sur BOCAL4 par la meme feuille avant certification.

## 2. CE QUE LE v6 TRANCHE, A MA PLUME, SOUS TON VETO

    (vi) marge : n = 21 -- les deux marges partielles (kT 1.37, m 1.52), aucune pleine ;
    (i)  LD-16 re-ancree sur /reglage/c_pl = 10 du run 85 (section 5) ;
    (ii) N-70 issue (c) : cles EXPOSEE-LIBM comparees a 2 ulp entre machines (section 5) ;
    temoin d'arrondi executable sur la ligne de plateforme de tout journal de run (section 5) ;
    cascade 3.5 sur verdict de porte seulement ; L-desc a 1/441 (section 9 re-derivee).

## 3. D-v9-1 (machine 1 ; instrument ; OUVERT ; numero propose)

Le banc des gardes rejoue a la fin du pre-vol (D-b-3) DEGENERE a n = 21 : la scenario G11
(alpha(dt2) != alpha(dt2/2) -> G-dt, branche 2) rend NON CONCLUANT DE FENETRE (branche 3) --
G-fen mord avant G-dt sur la serie synthetique. Meme chose G12 a n = 20, et aux autres n du
balayage. Le verdict de porte (branche 5) est acquis AVANT ce rejeu et n'en depend pas ; mais un
banc qui n'assert pas sa branche est degenere (v5 10) : les series synthetiques SynthAlpha
(dep_dt, dep_k) ont ete taillees au reglage 1/102400 et doivent etre re-derivees au reglage v6
(fenetre [tau_CAP', tau_dom'] plus large d'un facteur 1.5). A faire au v9 AVANT certification ;
je ne l'ai pas fait ce tour.

## 4. CE QUE MACHINE 2 A A FAIRE, EN UN PASSAGE

    gel v6 : certification par diff -- les 26 hunks sont enumeres par le script, les nombres
      de 3.3, 4.3-4.7 se re-derivent en le rejouant (chemins en arguments) ;
    banc v9 : selftest (103/103 ici), rejeu du balayage sur BOCAL4 (7 pre-vols, meme feuille),
      D-v9-1 (re-derivation des scenarios G11/G12), puis banc qui tue et pre-vol opposable ;
    rien d'autre : les defauts de forme de ce lot, s'il y en a, se versent a l'acte suivant.

## 5. PIECES

    constante_A_pre_enregistrement_v6.md            le gel, n = 21
    banc_qualification_machine1_v9.py               l'instrument re-parametre, pin du gel v6
    construction_gel_v6_et_banc_v9_machine1_v1.py   la construction (v5, v8, sortie, n en args) + .log
    selftest_v9_machine1.log                        103/103 a n = 21
    prevol_temoin_v9_n21_machine1.log               branche 5, puis D-v9-1 en fin de rejeu
    balayage_resume.txt, balayage/                  le balayage : feuille + 7 pre-vols
    contre moi, versees ici : (a) la premiere version du balayage tapait 1/40000 dans le banc
    (cinq points identiques) ; (b) une substitution 1/1024 -> 1/n^2 sans frontiere de mot a
    change 1/102400 en 1/40000 dans six phrases historiques, corrigee par une substitution
    a frontiere de mot ; (c) j'ai annonce n = 18 avant la fin du balayage.

-- FIN note_machine1_gel_v6_banc_v9_v1 --
