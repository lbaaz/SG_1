NOTE MACHINE 1 -- OU L'ERREUR DE 7|1.73 ETAIT POSSIBLE AILLEURS : L'EXPOSITION DE LA
CHAINE AU NOYAU SIMD numpy DE MACHINE 1, MESUREE, ET LES ENDROITS OU ELLE N'A PAS MORDU
(classe 3, machine 1, 2026-09-12) -- VERSION 1 ; repond a la question de l'operateur
=======================================================================
Aucun verdict de gel ; rien n'est edite (PB-1) ; le moteur depose (c8ed357b120352c4,
clone HEAD d037d21) est charge en lecture par les scripts de ce lot.

0. REPONSE EN TROIS PHRASES
  Oui : sur la plateforme de machine 1, TOUTE puissance ** de tableau numpy, np.exp et
  np.arctan2 passent par des noyaux SIMD non correctement arrondis sur 4.5 a 6 pour
  cent des appels (biais -1 ulp) -- noyaux que la ROUE LINUX de numpy embarque (2.2.6
  comme 2.4.4, mesure ici, section 1bis) et que le CPU AVX512 active ; BOCAL4, Windows,
  numpy 2.2.6, CPU AVX512 lui aussi, ne les a pas (0 appel sur 22 800, lot m2
  f9e1c1922e32220d). Le coeur du moteur depose -- base = g (x1 + x2) ** (P - 1) sur la
  grille des amplitudes -- en est. Cela n'expose que les
  calculs EXECUTES sur machine 1 : les runs deposes sont ceux de BOCAL4 (19 journaux
  du registre citent Windows, aucun run depose ne cite Linux), et la regle N-62 fait
  de tout calcul de machine 1 un calcul non opposable. La ou machine 1 a calcule et
  compare au bit, l'erreur ne s'est produite qu'a 7|1.73 : la chaine constante A a
  tenu partout ailleurs au bit, et le moteur depose, joue ici sur quatre cellules
  avec et sans le noyau, rend des seuils et des masques d'explosion identiques au
  bit -- dont 5|1.73|+1 = 0.6562256411088306, la valeur de la table du gel (BOCAL4).

1. CE QUI EST EXPOSE SUR MACHINE 1 (mesure_ufuncs_cr.py : 20000 entrees par ufunc
   contre une reference mpmath a 200 bits ; deux passes, noyau X86_V4 actif / desactive)
     ufunc (tableau)         non-CR avec X86_V4     non-CR sans X86_V4     lecture
     power x ** 6              4.92 pour cent (-1)    0.08                 noyau SIMD ; sans V4 = pow glibc
     power x ** (-0.8)         5.40 (-1)              0.08                 idem
     power (-x) ** 6           0.09                   0.08                 base NEGATIVE : libm des deux cotes
     exp                       4.56 (-1)              0.08                 noyau SIMD ; sans V4 = exp glibc
     arctan2                   5.92                   0.13                 noyau SIMD
     sqrt                      0                      0                    IEEE, exact
     log, log2, sin, cos,      0.00 a 0.35            0.01 a 0.23          quasi-CR des deux cotes
       tan, arctan
     log10                     0.07                   10.25                glibc lui-meme est mauvais
     expm1 / log1p             0.03 / 0.12            11.5 / 8.65          idem
     cbrt                      0.63                   51.9                 idem
     tanh                      21.25                  21.25                glibc, sans noyau SIMD
     pow de Python (glibc)     0.09                   0.08                 reference, CR sauf cas durs rares
   Deux consequences. (i) Sur machine 1, pow(-x, 6) et pow(x, 6) ne passent pas par le
   meme code : la ligne du protocole "numpy pow non symetrique sous negation au dernier
   ulp, dependant de la machine" est exactement cela -- 5 pour cent des bases positives
   par le noyau SIMD, les bases negatives par glibc ; sur BOCAL4 les deux par la libm.
   (ii) Desactiver X86_V4 aligne pow et exp sur la classe libm de BOCAL4 (0.08 pour
   cent, ses propres cas durs) mais degrade log10, expm1, log1p, cbrt : ce n'est pas
   un reglage "meilleur", c'est un reglage "comme la libm" ; a arbitrer par usage.

1bis. NI LE CPU SEUL, NI LA VERSION SEULE : LA ROUE ET LE DISPATCH (test_version_numpy.py)
   Machine 2 (lot f9e1c1922e32220d) montre que BOCAL4 a quinze extensions AVX512 actives
   et reste CR : le CPU seul ne decide pas -- accorde. Elle en conclut que c'est la
   VERSION de numpy (2.4.4 contre 2.2.6). Mesure ici : numpy 2.2.6 installe sur ce
   conteneur Linux, meme CPU, rend EXACTEMENT les memes comptes que 2.4.4 -- power x**6
   985/20000 (4.92 pour cent), x**(-0.8) 1080, exp 912, et le meme temoin
   (1765.6704444885254)**6 = 0x1.a483018a169c5p+64 contre 0x1.a483018a169c6p+64 (CR) ;
   la version ne decide pas non plus. Ce qui decide est le COUPLE roue x dispatch : la
   roue Linux de numpy embarque un noyau SIMD pour power et exp (au niveau AVX512F dans
   2.2.6, X86_V4 dans 2.4.4 -- la variable de desactivation change de nom avec la
   version), la roue Windows non ; le CPU AVX512 l'active la ou il existe. D'ou la regle
   candidate reformulee en section 4 : un TEMOIN executable, pas une liste de noms.

2. OU CES NOYAUX SONT APPELES DANS LE CODE DE LA CAMPAGNE (inventaire par grep)
   moteur m9_replication_v1.py : grad_rapide, base = g * (x1 + x2) ** (P - 1), x1 et x2
     tableaux de la grille s_arr (48 ou 96 amplitudes integrees ensemble) -- CHAQUE
     integration classique de la campagne (cartes M9-M16, P-4, R4, alpha, jumeau) ;
     grad_explicite (x1 ** (a - 1) * x2 ** b, garde G3, comparee a tolerance) ;
     etat_coherent, c = np.exp(lc) (etat coherent quantique, t_shell).
   instrument v8 : T-2 K1 (a1 + a2) ** (p - 1) et K3 tau ** (-a) (les deux du geste) ;
     T-2b v[0] ** (p - 1) ; T-1 Damour-Smilga V_ds, Vp_ds (x ** 4, x ** 3 sur
     tableaux) ; les autres ** sont en float Python (glibc) ou en Fraction.
   scripts deposes : m10_exposant_v3 (14 **), m11 (10), m12_pilote_v3 (9), m13_saturation
     (75 / 31), m14_p1a (70), m15_site83 (10), m16_crible (10), m17_chaine_v17 (27 **,
     1 ufunc transcendante), sonde_EA (1) -- le meme motif que le moteur, joues sur
     BOCAL4 pour le depot.
   NON exposes : +, -, *, /, np.sqrt, np.abs, np.max, np.sum, np.where, les Fraction :
     IEEE-elementaires ou exacts, identiques sur toute plateforme.

3. OU CELA POUVAIT MORDRE, ET OU CELA N'A PAS MORDU
 3.1 Le registre : les runs deposes sont ceux de machine 2 (protocole ; N-62 ; 19 pieces
     de runs/ et journal/ citent Windows-10, 2 citent Linux et ce sont des mentions du
     conteneur m1, pas des runs). Aucun nombre du registre n'est sorti d'un noyau SIMD
     de machine 1. Exposition : NULLE par construction du protocole.
 3.2 Les executions de machine 1 : bacs a sable, pre-vols, pieces de calibration --
     exposees, et non opposables (N-62). La ou elles ont ete comparees au bit a BOCAL4
     : la chaine constante A (pre-vol temoin du 28/08 contre le run m2) a tenu au bit
     partout SAUF 7|1.73 ; les huit autres points T-2 (memes noyaux, memes 5 pour cent
     d'appels mal arrondis) n'ont bascule aucun bit visible. Ce que l'histoire ne
     permet pas de dire d'ici : la liste de tous les bacs a sable m1 depuis M3 ; la
     regle qui tranche est simple -- un nombre produit sur machine 1 et compare au
     bit est expose, un nombre produit sur BOCAL4 ne l'est pas.
 3.3 Test direct, aujourd'hui (seuils_moteur_avec_sans_V4.py) : le moteur depose joue
     chercher_seuil puis integrer sur une grille dense de 96 points a 5|2.00|+1,
     5|2.00|-1, 5|1.73|+1, 5|1.73|-1, avec le noyau X86_V4 actif puis desactive :
       cellule      s*                       masque des 96 points
       5|2.00|+1    0.37450207514104217      identique au bit
       5|2.00|-1    0.37378118731423976      identique au bit
       5|1.73|+1    0.6562256411088306       identique au bit  (= table du gel 4.2, BOCAL4)
       5|1.73|-1    0.8298769616508258       identique au bit  (masque crible, 3 trous)
     Quatre recherches de seuil (quatre passes chacune, T = 400, dt = 0.006, soit
     ~2.7e5 appels du noyau par passe) et quatre masques : aucun verdict d'explosion
     deplace, aucun seuil deplace. Le noyau a fait ses 5 pour cent d'appels a -1 ulp ;
     aucun n'a suffi a changer un bit qui compte.
 3.4 Pourquoi 7|1.73 et pas ailleurs. Un appel mal arrondi deplace une trajectoire d'un
     ulp au plus ; un verdict d'explosion sur une grille ne bouge que si la trajectoire
     est a cette distance-la de la separatrice, amplifiee sur T -- rare, possible en
     principe dans les regimes cribles et les ilots, jamais observe. La lecture e de
     T-2 a 7|1.73 est le point le plus sensible de toute la campagne : R = 5.9e+07 y
     transforme UN ulp de composante en 0.334 plancher de e, et e y est comparee a
     quatre chiffres. C'est la seule grandeur de la chaine ou un ulp est un nombre.

4. CE QUI RESTE (a l'operateur)
   Aucune piece deposee n'est a rouvrir. A arbitrer (sous (X)) : la regle candidate,
   reformulee apres la lecture m2 -- la ligne de plateforme d'un log porte l'OS, la
   version de numpy, le niveau de dispatch actif ET UN TEMOIN D'ARRONDI EXECUTABLE, le
   double de (1765.6704444885254) ** 6 par le tableau numpy et par le pow de Python, en
   hexadecimal (...9c5 : noyau SIMD ; ...9c6 : correctement arrondi) -- parce qu'aucun
   des trois noms ne predit le noyau, et que le temoin le mesure ; le diagnostic v2 le
   porte deja. Le reglage de l'environnement machine 1 (noyau desactive : pow et exp
   comme la libm) pour les futurs bacs a sable compares au bit ; le grep de la section
   2 comme liste des chemins exposes. Rien sur la tenaille, rien sur alpha.

-- FIN note_machine1_exposition_noyau_simd_v1 --
