# POUR MACHINE 1 -- MA REFERENCE DU TEMOIN POSITIF (gel E-B v2, 5.1), A CERTIFIER
# machine 2, v1, 2026-11-11. Classe B. Entrants : gel v2 cde0cd11a763f26d ; moteur v17 82a0be882568fe0c ;
# ta feuille de lecture b3ac958a1a2b915b et ta sonde v2 facc7536ba4637cb (certifiees par moi) ; ton interface
# P-1. E19 : aucune mesure de la sonde n'a ete jouee sur le TP ; ce que j'ai calcule est en 6.

## 0. L'ESSENTIEL, EN CINQ PHRASES

Ma reference du TP est calculee, par rotation complexe, sur les 17 couplages g_j, et **la regle du gel retient
j = 6 (g = 0.08408964152537146, Gamma_ref 5.369e-10) et j = 8 (g = 0.1, Gamma_ref 6.428e-09)**. Les deux
fichiers de l'interface P-1 sont ecrits, et ta feuille certifiee, rejouee sur ma table, retrouve la meme liste.
Mon audit : 16 controles, 0 morsures -- **apres qu'il en a fait mordre un, sur mon premier jet** (3.1). **Un
bord est a connaitre avant ta lecture : j = 5 est exclu par la regle pour 2e-5 de depassement de u_ref (3.2) ;
je ne l'ai pas corrige, je te le consigne.** Je te demande de CERTIFIER la reference ; la nuit ne part qu'apres.

## 1. CE QUE J'AI ECRIT ET CE QUE JE LIS DU GEL

Script `reference_TP_rotation_complexe_machine2_v1.py` (canon 5fd3a1897ca0442a). Il ne lit NI ta sonde NI ta
feuille NI aucune largeur mesuree ; il n'importe le moteur que pour la garde R1.

  Formule     H(theta) = somme_i w_i [cos2t n_i + (i/2) sin2t (a_i^2 + a_i^+2)] + (w1+w2)/2 (cos2t - 1)
              + e^{5 i t} (g/5) x^5, x = l1 (a1 + a1^+) + l2 (a2 + a2^+), l_i = 1/sqrt(2 Delta w_i). Re-derivee
              de x -> e^{it} x, p -> e^{-it} p ; la tienne est juste. x^5 est EXACT dans le bloc N x N (base
              etendue a N + 5, puissances de x_tilde, produit de Kronecker).
  Etat        plus grand recouvrement hermitien |<0,0|v>|^2 avec le vide de Fock ; Gamma = -2 Im E.
  Grille      g_j = 0.05 * 2.0 ** (j / 8.0), j = 0..16 ; theta dans {0.10, 0.15, 0.20, 0.25, 0.30} ; N dans
              {50, 60, 70}. Diagonalisation dense (numpy, zgeev).
  LECTURES DECLAREES, que le gel laisse ouvertes :
   (L-1) "theta de plus petite variation" : parmi les TROIS theta centraux, a N = 70, celui dont le plus
         grand ecart |ln Gamma| a ses deux theta voisins est le plus petit ; egalite : le plus petit theta.
         Gamma_ref = Gamma a ce theta, N = 70.
   (L-2) u_ref = max |Gamma(theta, N) / Gamma_ref - 1| sur theta dans {0.15, 0.20, 0.25} et N dans {60, 70}.
         Toute autre lecture de L-1 deplace Gamma_ref d'au plus u_ref : c'est ce que u_ref est fait pour porter.
   (L-3) RAFFINEMENT (economie de calcul) : les 17 g_j sont d'abord calcules a (N = 50, theta = 0.20) ; la grille
         complete n'est jouee que pour ceux dont ce Gamma est dans [1e-12, 1e-6], une decade de marge de chaque
         cote de la fenetre du gel. Les six autres (j = 0, 1, 13..16) portent Gamma_ref = ce Gamma, u_ref = 1.0 et
         raffine = false : ils ne peuvent pas etre retenus. **Mon engagement O-1/O-2 est tenu** : un nombre
         partout, u_ref = 1.0 si non raffine, g de la liste == g de la table en repr (C04 a C06).
  SELECTION   telle que le gel l'ecrit, sur la table seule : parmi Gamma_ref dans [1e-11, 1e-7] et u_ref <= 0.01,
              les deux dont ln(Gamma_ref) est le plus proche de ln(1e-10) et de ln(1e-8) ; egalite : le plus
              petit j.
  Reprise      par fichier SOUS IDENTITE (la lecon de ton D-1) : un fichier repris porte (w1, w2, p, signe, j, g,
              N, theta, formule) ou le calcul s'arrete, code 2.

Gardes jouees AVANT tout calcul, toutes tenues (journal) : moteur au canon ; **H(theta = 0) == H_2D du moteur a
3.553e-15** (N = 14, g = 0.10) ; H(theta) complexe symetrique (2.979e-15) ; g = 0 : les six premiers niveaux sont
0, 1, 1.95, 2, 2.95, 3 (1.4e-13, N = 40) ; la formule tient en theta (etalement 1.3e-5 a N = 30) **et la phase
fausse e^{4it} mord** (Gamma negatif : -1.3e-4 a -2.0e-4) ; la selection sur une table synthetique ([3, 4], puis
aucune).

## 2. LE RESULTAT

  j   g                       Gamma_ref      u_ref     raffine        j   g                       Gamma_ref      u_ref
  0   0.05                    5.031e-13      1.0       non            9   0.10905077326652578     2.000e-08      1.1e-04
  1   0.054525386633262889    9.004e-13      1.0       non           10   0.11892071150027211     5.832e-08      1.9e-05
  2   0.059460355750136057    1.469e-12      0.90      oui           11   0.12968395546510098     1.599e-07      1.8e-05
  3   0.064841977732550488    8.341e-12      0.32      oui           12   0.14142135623730953     4.134e-07      6.5e-06
  4   0.070710678118654766    3.323e-11      0.097     oui           13   0.15422108254079409     1.012e-06      1.0       non
  5   0.077110541270397043    1.384e-10      0.010020  oui           14   0.16817928305074292     2.353e-06      1.0       non
  6   0.084089641525371461    5.369e-10      2.1e-03   oui           15   0.18340080864093425     5.208e-06      1.0       non
  7   0.091700404320467124    1.930e-09      1.9e-03   oui           16   0.2                     1.101e-05      1.0       non
  8   0.1                     6.428e-09      1.6e-04   oui

  RETENUS (regle du gel, sur la table seule) : j = 6 et j = 8. `tp_retenus_machine2_v1.json` porte {j, g} et
  RIEN d'autre : pas une largeur.
  Les deux largeurs retenues sont stables : Re E identique a 2e-12 sur tous leurs points (j = 6 : -1.48499382e-4 ;
  j = 8 : -2.10756982e-4), recouvrement avec le vide 0.90 a 0.99, Gamma(N = 50, theta = 0.20) a 1.6e-3 (j = 6) et
  1.1e-4 (j = 8) de Gamma_ref. Mon essai du gel a g_8 = 0.10 (6.428e-09, N <= 50) est retrouve : 6.4279e-09 a
  N = 70. Ton WKB (1.46e-09) est a un facteur 4.4, comme tu l'avais declare.
  Calcul : 149 points (17 + 132) en 3301 s sur BOCAL4, six processus de deux fils ; une diagonalisation a N = 70
  prend 93 s seule, 270 a 290 s a six en parallele.

## 3. CE QUE J'AI TROUVE EN ROUTE (a lire avant de certifier)

3.1 **UN DEFAUT DE MON PREMIER JET, trouve par mon audit, corrige, conserve.** Mon controle C09 recalcule la table
des 11 raffines d'un autre code. Il a MORDU : a j = 12, theta = 0.15 et theta = 0.20 sont a egalite EXACTE de
variation (leur plus grand ecart est le meme, celui entre ces deux theta). Ma regle declaree dit "le plus petit
theta" ; mon script departageait par l'arrondi flottant de log(x / y) contre log(y / x) (7e-17) et prenait
theta = 0.20. Corrige : la variation se calcule sur des DIFFERENCES de logarithmes (x - y et y - x sont exactement
opposes), l'egalite est exacte et la regle s'applique. Effet : **j = 12 seul** change (Gamma_ref 4.134445e-07 ->
4.134457e-07, u_ref 5.3e-06 -> 6.5e-06, theta 0.20 -> 0.15) ; j = 2 a 11 ne changent qu'a l'affichage
`variation_theta` (1e-16) ; **la liste des retenus ne change pas.** Le premier jet est joint
(`..._premier_jet.py`, canon af73dfe9a648960a), avec le journal de CALCUL de ses 149 points ; le calcul n'a pas
ete refait : le script corrige a repris les 149 fichiers sous identite (149 repris, 0 joue). La seule difference
entre les deux scripts est la fonction `variation` de `reduire` : `diff` te le dira.

3.2 **LE BORD : j = 5.** Gamma_ref(j = 5) = 1.384e-10 est le plus proche de la cible 1e-10 (|ln| 0.325 contre 1.681
pour j = 6), mais **u_ref = 0.010019582, soit 1.96e-05 au-dessus du seuil 0.01** ; la regle l'exclut. L'ecart qui
fait u_ref est un seul point dense, (N = 60, theta = 0.25) : 1.3977e-10 contre 1.3839e-10. Ma lecture : c'est le
BRUIT de la diagonalisation dense (de l'ordre de 1e-2 en relatif a Gamma = 1.4e-10, Im E = 7e-11), pas de la
physique. **Diagnostic, pas correction** : une seconde methode (Arnoldi en inversion decalee, creux, N = 60, theta =
0.20) donne j = 5 : 1.38557e-10, a 1.2e-3 de Gamma_ref ; j = 6 : 5.3726e-10 (7.1e-4) ; j = 8 : 6.42827e-09
(5.7e-5). Les deux methodes s'accordent aux deux retenus, et a j = 5 a 1.2e-3. **Je n'ai pas touche la liste** : la
selection ne lit que la reference declaree, et desserrer u_ref ou changer de methode apres avoir vu le bord est
exactement ce que le gel interdit. Consequence a connaitre : la liste est tenue au bruit pres a j = 5 ; un rejeu a
un autre nombre de fils peut donner j = 5 au lieu de j = 6 (le fichier certifie fait foi, pas le rejeu). Si tu
veux que cela devienne une observation de l'acte, c'est ta plume.

## 4. CE QUE JE TE DEMANDE ET COMMENT LE REJOUER

  a. Re-deriver la formule (1), sans la prendre de moi : H(theta = 0) == H_2D est la garde R1, mais c'est le
     facteur e^{5it} sur x^5 et le couple (cos2t, sin2t) qui portent la rotation.
  b. Rejouer UN point : `python -P` ; `resoudre(50, g_de(8), 0.20)` dans le script (15 s) rend 6.428e-09 (a 2e-4
     pres : mon journal porte 6.4286e-09, un rejeu isole 6.4278e-09, c'est le bruit de zgeev) ; j = 6 a N = 50 :
     5.377e-10. Ou la reference entiere : `python -P reference_TP_rotation_complexe_
     machine2_v1.py --moteur m17_chaine_v17.py --sortie DOSSIER --travailleurs 6 --threads 2` (environ une heure).
  c. Relire mon audit (`audit_reference_TP_machine2_v1.py`, 16 controles) : il recalcule la table d'un autre code,
     fait rejouer la selection par TA feuille (canon verifie) et PROUVE que le controle est vivant (C13 : j = 5 a
     u_ref = 0.0099 change la liste en [5, 8] ; C14 : un Gamma_ref x 1.5 est vu).
  d. Les noms. Sonde : `--etage 1 --retenus tp_retenus_machine2_v1.json`. Feuille : `--etage 1 --reference
     tp_reference_machine2_v1.json`. Les deux fichiers portent aussi "prevol": false, "script_canon", "moteur",
     "gel" : des cles en plus que ni ta sonde ni ta feuille ne lisent.

## 5. CE QUE JE NE FAIS PAS

Je ne retouche ni tau, ni u_ref, ni les fenetres, ni la liste. Je ne lis aucune valeur de ta sonde sur le TP : elle
n'a pas ete jouee. Je ne prends aucun numero (E18).

## 6. CE QUE J'AI CALCULE ET VU (E19), EN CLAIR

Cette reference (149 points) ; le smoke-test en geometrie reduite (N = 20 a 28, NON OPPOSABLE, retenus j = 6 et
8 aussi) ; les gardes ; l'Arnoldi aux trois g de 3.2, **a N = 60, theta = 0.20 seulement**. Rien de la sonde sur
le TP, rien de l'etage 1 ni de l'etage 2 n'a ete joue. Avant le gel v2 j'avais vu UN point (g_8, 6.428e-09), que
le gel nomme.

## 7. CE QUI SUIT

  machine 1  : certifier cette reference (ou la rendre, avec les defauts) ; puis le garde-fou est sous le veto de
               l'operateur ;
  la nuit    : etage 1 avec `--retenus tp_retenus_machine2_v1.json` ; lecture ; etage 2 seulement si l'etage 1
               TIENT ; je joue, tu lis.

## 8. CE QUE CETTE PIECE NE DIT PAS

Elle ne dit rien du resultat de l'etage 1 ni de l'etage 2. Elle ne dit pas que la sonde mesure juste le TP (c'est
la nuit qui le dit, par ta feuille). Elle ne dit pas que j = 5 aurait ete retenu hors bruit : elle dit que la
regle, appliquee a la reference declaree, le laisse dehors, et que cela tient a 2e-5.

## 9. PIECES (convention B, 2026-11-11)

    cette note
    reference_TP_rotation_complexe_machine2_v1.py                     5fd3a1897ca0442a   le script, corrige
    reference_TP_rotation_complexe_machine2_v1_premier_jet.py         af73dfe9a648960a   le premier jet (3.1)
    tp_retenus_machine2_v1.json                                       69b3bab3bb8480b7   LA LISTE (j, g), sans largeur
    tp_reference_machine2_v1.json                                     4d51dd58ef456fe9   LA TABLE, pour la feuille
    tp_reference_machine2_v1_calculs.json                             fe25da36c3ad27fd   les 149 points
    tp_reference_machine2_v1.log                                      7d718e42909528ca   journal de la reduction (reprise)
    tp_reference_machine2_v1_calcul_initial.log                       aa3ef994316b2ca2   journal du CALCUL des 149 points
    audit_reference_TP_machine2_v1.py / .log / .json                  b5efed9ca4b4f6cf / ef3a67caf4682289 /
                                                                      72f87564b00e6f74   16 controles, 0 morsures
    lot_6bed68e12ec21e18/                                             JOINT : ma certification de ta sonde v2 et de
        ton banc v2, avec, dedans, ma certification du gel v2 (lot 3b388a98d30695e3). Si tu les as deja recus,
        ignore ce sous-dossier ; sinon, un seul zip porte tout.

-- FIN POUR_MACHINE1_reference_TP_machine2_v1 --
