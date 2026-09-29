# NOTE MACHINE 1 -- GEL constante A v8 ET INSTRUMENT v14 : LE TEST EN AVEUGLE DU PREMIER ORDRE
# machine 1, v1, 13/09/2026 (nuit). Classe 3 ; le gel devient classe 1 a la certification m2.
# Engagement operateur : "go" (13/09) sur n = 18, M2 a p = 7, v14 (troisieme niveau).
# PB-1 : v7 et v13 non edites ; un seul script construit le gel et l'instrument.

## 0. EN QUATRE PHRASES

Le gel v8 = v7 certifie + 39 hunks appliques par construction_gel_v8_banc_v14_machine1_v1.py :
regle d'echelle (n = 18, levier 441/324 = 1.3611), tous les nombres du reglage re-derives
par les formules de la construction du v6 (les fragments a n = 21 servent d'ancres, jamais
tapes), section 5bis neuve (modeles M1/M2, Richardson a ordre mesure, les deux predictions
en aveugle), instrument v14, D-v7-1 close par une phrase sourcee. Le banc v14 = v13 certifie
+ 32 remplacements du meme script : reglage n = 18, pin v8, et UN etage de plus -- la jumelle
a dt_2b/4 (cle G_dt4, series _dt2s4_k2, intervalles x4, sans verdict de cascade), jouee aussi
par les deux boucles du banc qui tue. Selftest 103/103, banc 56/56, pre-vol temoin branche 5
et pre-vol alpha branche 5 (9/27 verifie) a n = 18 sur machine 1, levier X86_V4 -- BOCAL4
avant tout run. La feuille de lecture est deposee avec le gel : rien ne se lit apres coup.

## 1. LES DEUX PREDICTIONS, CALCULEES EN CODE (5bis)

    (a) biais du premier ordre x 441/324, sur l'ajustement II sans c1, apres Richardson a
        ordre MESURE : 3.4606e-07 (p = 4), 3.5800e-07 (p = 5), 3.2648e-07 (p = 7, sous M2).
        TIENT si obs_R/pred dans [0.8, 1.2] aux six points ET |obs_R - pred| <= 3 S(p).
    (b) transport des modes libres a p = 7 : amplitude x 1.4255, phase - 0.4465 rad, contre la
        base du 91 (six couples (a, c) apres Richardson, JSON base_modes_libres_n21, tapes au
        gel par construction) ; TIENT au point a 20 pour cent en amplitude et 0.3 rad en phase.
    La feuille lecture_v8_machine1_v1.py joue les deux ; en mode --base sur les series BOCAL4
    du 91 elle REPRODUIT la table S de Q5 au chiffre (M1 2.508e-07, M2 4.378e-09 a p = 7) --
    c'est son controle positif -- et ecrit la base.

## 2. CE QUE LA CERTIFICATION m2 DOIT REJOUER, EN UN PASSAGE

    gel v8 : par diff contre le v7 (le script enumere ses hunks et re-derive ses nombres) ;
    banc v14 : construction au bit depuis le v13, selftest, banc qui tue, pre-vols temoin et
      alpha a n = 18 sur BOCAL4 (la porte doit y ouvrir : branche 5 -- sinon 3.5 du v7) ;
    lecture_v8 en mode --base sur ses series du 91 : la base doit se reproduire ;
    puis le run des deux volets sous v14, et la lecture en mode --predictions, des deux cotes.

## 3. CE QUE CE GEL NE DIT PAS

    Une valeur de A ; un gain projete (D-v13-1 est prise) ; le second ordre c2 ; la puissance
    de M2 hors p = 7. La regle 3.2 du v7 est suspendue, non abrogee : mesurer A reviendra.

## 4. PIECES

    constante_A_pre_enregistrement_v8.md ; banc_qualification_machine1_v14.py ;
    construction_gel_v8_banc_v14_machine1_v1.py ; lecture_v8_machine1_v1.py ;
    base_modes_libres_n21_machine1_v1.json + lecture_v8_base_n21_m1.log (75/75) ;
    m1_v14_selftest.log ; m1_v14_banc.log ; m1_v14_prevol_temoin.log ; m1_v14_prevol_alpha.log.

-- FIN note_machine1_gel_v8_banc_v14_v1 --
