# LECTURE MACHINE 1 DE Q5 -- (i) TIENT A p = 7 SUR LES DEUX ARITHMETIQUES ; CE QUE LE GEL v8 PORTERA
# machine 1, v1, 13/09/2026 (nuit). Classe C (rien d'opposable ; le gel v8 n'est pas ecrit, il est
# a ma plume). PB-1 : rien d'edite. Lot m2 4bb9da845608a7dd recu 61/61 au canon ; D-SO-1 close.

## 0. EN QUATRE PHRASES

Q5 rejoue chez moi sur les series de BOCAL4 (levier X86_V4) : 330/330, memes verdicts, le log
identique hors ligne de plateforme et une decimale a 1e-12 dans une note. Puis la contre-epreuve
qu'elle demandait, Q5 sur MES series du 91 (mon run v13, arithmetique glibc) : memes verdicts,
Q5-a, Q5-b, Q5-c vrais, et a p = 7 le meme S au quatrieme chiffre -- M1 2.508e-07, M2 4.378e-09, frequences
fausses 1.194e-07 et 1.176e-07. Les modes libres a (b, w) DERIVES ajustent les series de p = 7 sur les deux
machines ; a p = 4 et 5 ils absorbent la troncature (F4), M1 suffit. Ses cinq reserves a ma
prediction sont prises ; le v8 prend n = 18 et deux predictions en aveugle.

## 1. LE REJEU, CHIFFRE

    series BOCAL4 (rejeu)   S_M1        S_M2        S_M2-       S_M2+
      p = 4                 5.841e-09   9.919e-09   1.493e-08   6.919e-09
      p = 5                 3.742e-09   5.851e-09   8.934e-09   3.674e-09
      p = 7                 2.508e-07   4.378e-09   1.193e-07   1.177e-07
    mes series (glibc)
      p = 4                 5.785e-09   9.611e-09   1.398e-08   6.919e-09
      p = 5                 3.742e-09   7.062e-09   1.071e-08   4.483e-09
      p = 7                 2.508e-07   4.378e-09   1.194e-07   1.176e-07
    A p = 7 le gain M1 -> M2 est x 57 sur les deux, les frequences fausses x 2.1 : specifique.
    A p = 4 et 5 les S de M2 different entre machines au niveau 1e-9 : c'est l'ulp des flots
    amplifie par l'ajustement, la signature de F4 (la base oscillante ajuste du bruit).
    F3 pris : aucun choix de modele sur SS ni sur un critere d'information ; la coherence entre
    points (S) est le seul critere, ecrit avant.

## 2. SES CINQ RESERVES -- PRISES, ET CE QUE J'EN FAIS

    R1  le v8 garde les DEUX ajustements : II sans c1 (ou se lit le biais predit) et M1/M2 avec
        c1 fixe (ou se lit lnA). Pris.
    R2  la tolerance se re-derive au reglage, sous q MESURE ; aucun nombre de tolerance n'est
        tape au v8 avant le run. Pris.
    R3  la puissance tranche : n = 19 ne discrimine pas a p = 7 (3.0 pour cent). Je prends n = 18.
    R4  le choix de n quitte la regle 3.2 du v7 ; le v8 l'ecrit comme regle propre : un test
        d'ECHELLE choisit le barreau de levier maximal qui ouvre la porte (n = 18 : branche 5 a
        mon balayage, e/seuil >= 1.87 ; a confirmer sur BOCAL4 avant tout run). Arbitrage operateur.
    R5  1.06 periode a p = 7 sur la fenetre d'ajustement, pas 1.2 ; corrige. Q5 a separe quand meme.

## 3. LES DEUX PREDICTIONS EN AVEUGLE DU v8, A n = 18 (delta' = 1/32400 ; facteur 441/324 = 1.3611)

    (a) le biais du premier ordre, proportionnel a delta', lu sur l'ajustement II sans c1 apres
        Richardson a ordre mesure : 3.4606e-07 (p = 4), 3.5800e-07 (p = 5), 3.2648e-07 (p = 7, lisible seulement
        a la tolerance (ii) si M2 n'est pas retenu). Contre "biais constant" l'ecart est 36 pour
        cent ; tolerance : le residu de Richardson mesure au run, pas un nombre d'aujourd'hui.
    (b) a p = 7, l'ajout de machine 2, derive : la trajectoire est la meme jusqu'a la bascule,
        l'amplitude e du mode libre aussi ; dans la fenetre normalisee s = tau/tau_dom' les
        coefficients de M2 se transportent par amplitude x (441/324)^(b/2) = 1.4255 (b = 23/10) et
        phase - w ln sqrt(441/324) = -0.4465 rad (w = 2.896550), point par point, a lire sur M2 apres
        Richardson. Les six couples (amplitude, phase) du 91 a n = 21 sont la base : ils vivent
        dans le JSON de Q5 (cle points), ils seront TAPES au gel depuis ce JSON par construction.
        (A n = 19 les memes vaudraient 3.1059e-07 / 3.2131e-07 / 2.9301e-07, x 1.2588 et -0.2899 rad : consigne, non retenu.)

## 4. CE QUE LE GEL v8 PORTERA (ma plume ; les arbitrages restent a l'operateur)

    reglage n = 18 par regle d'echelle (3.2 v8), pre-vol des deux cotes avant tout run ;
    modeles par degre ECRITS AVANT : M1 (c1 fixe, derive) a p = 4 et 5 ; M2 (c1 fixe + mode libre
      a b = alpha + 3/2 et w derives, deux coefficients lineaires) a p = 7 ; M2- et M2+ joues au
      run comme tests negatifs ; jamais de choix sur SS (F3) ;
    Richardson a ordre MESURE : troisieme niveau dt_2b/4 par point -> instrument v14, construit
      depuis le v13 certifie (un etage 2b de plus, ~1520 pas par point), a re-certifier ;
    P-A a deux regimes : instrument-limite a p = 4, 5 (tolerance = S + residu de Richardson,
      re-derives au run) ; a p = 7 sous M2, meme regime ; sous (ii), modele-limite ;
    les deux predictions (a) et (b) ci-dessus, deposees avant le run ;
    ce qu'il ne dira pas : une valeur de A avant que la lecture soit jouee ; un gain projete.
    Le second ordre (c2, deux jeux de racines par degre au JSON de derivation) reste hors v8.

## 5. A L'OPERATEUR, EN TROIS LIGNES

    n = 18 (levier) ou n = 19 (deja mesure a mon balayage seulement) ;
    M2 a p = 7 (Q5 tient sur les deux machines) ou (ii) ;
    v14 (troisieme niveau) : go, et j'ecris le gel v8 et la construction v14 dans le meme lot.

## 6. PIECES

    m1_rejeu_Q5_series_m2.log / .json ; m1_Q5_sur_mes_series.log / .json (330/330 chacun).

-- FIN note_machine1_lecture_Q5_v1 --
