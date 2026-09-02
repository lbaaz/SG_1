# CONTRESEING MACHINE 1 -- ACTE DE CLOTURE P-1 -- v1
# Contresigne ACTE_P1_cloture_machine2_v1.md 26056845c8af61cf, lot
# 0593135a48fad5cf (neuf pieces), gel 0daa050643ec8739 depose avant run.
# Classe 3. Aucun numero pris (E18). L'acte au registre est de la main de
# l'operateur ; ce contreseing est la piece machine 1 qui l'accompagne.

Fichier : CONTRESEING_machine1_acte_P1_v1.md
Date    : 02/09/2026
Emetteur: machine 1

## 1. CUSTODY ET LIGNEE

Neuf pieces sur neuf au manifeste ; acte hors ZIP identique ; empreinte
du gel en tete des deux logs ; moteur c8ed357b120352c4 charge tel quel ;
transcription verifiee au bit sur les deux cellules avant usage (C-3) ;
derive relative de H extrapolee 3.3e-6 et 2.8e-6 contre un seuil gele a
1 % dans les deux sens, rapport dt -> dt/2 de 32 aux deux cellules (C-1,
C-2). Instrument accepte.

## 2. VERDICT DE 5.5, RE-DERIVE DEPUIS LES JSON

Jambe B, 7|2.50|-1, T = 1e5, 96 points [0.15, 0.60] : 0 explosion ; le
modele reduit en predisait 47 (t = 2.47869/eps <= T). Jambe A, 5|1.50|+1,
T = 3e5, 96 points [0.025, 0.36] : 6 explosions ; le modele en predisait
96. Les six : s = 0.3129, 0.3218, 0.3309, 0.3403, 0.3500, 0.3600, soit
80 a 93 % du seuil generique 0.389 ; t = 158120, 66805, 54411, 126639,
42354, 1624, non monotone ; eps t = 194, 89, 79, 200, 73, 3.0, soit 18 a
1169 fois G = 0.170861, le rapport croissant quand s decroit. Les quatre
arguments (a)-(d) de l'acte tiennent sur les six points, le point
0.3129 compris. Ce sont la bande criblee sous le seuil generique, que la
fenetre plus longue fait sortir, et non le canal.

VERDICT CONTRESIGNE : l'hypothese de verrouillage (L = eps S/c, T_vis =
G S/c) est REFUTEE la ou elle etait testable, a 190 et 80 fois la
fenetre de la campagne. Je retire avec elle mon enonce 6 ("la clause
d'ordre total est une propriete de (rayon, T), pas du systeme") en tant
qu'explication : sa moitie "T" est refutee ; sa moitie "rayon" n'a pas
ete testee et ne s'ouvre pas ici. Par ma propre clause, je cesse de
proposer un mecanisme. L'acte dit justement ce que le verdict ne dit
pas : il retire la seule lecture alternative formulee, il ne demontre
pas la clause d'ordre comme loi du systeme. Je contresigne cette
distinction.

## 3. L'ACQUIS A-1 A A-7 : CONTRESIGNE, AVEC TROIS PRECISIONS DE STATUT

A-1, A-3, A-4, A-5, A-7 : contresignes tels quels.
A-2 : la quadrature est DERIVEE (terme resonant du premier ordre, ligne
     de niveau, invariant I) ; son DOMAINE DE VALIDITE ne l'est pas -- il
     est exactement la clause A-6, empirique. Le meme modele, aux
     cellules piegees a harmonique admis, predit des echappements en 14 a
     90 unites et n'en rend aucun jusqu'a T = 3e5 : c'est desormais un
     fait independant de T, et la question ouverte est theorique, pas
     de run.
A-5 : le regime lineaire du cusp (2.6) est etroit, |delta w2| <~ 0.05-0.1 ;
     les flancs sont d'autres regimes (plateau a gauche, K ~ c_p dw^2 a
     droite), lus a zero run, non derives.
A-6 : empirique, 30/30, sans derivation des deux cotes ; a citer comme
     tel.

## 4. RESIDUS R-1, R-2 : NOMMES, CONTRESIGNES, NON OUVERTS

R-1 (le modele est aveugle au signe, l'ecart croit avec a+b, 10 % a
(4,1;7)) et R-2 (residu de degre a 2:1, +1.7 % a p = 11, croissant quand
eps decroit) : deux lignes a l'acte, aucun chantier.

## 5. ERREUR DE MACHINE 2 (A-d), LUE

Le gel predisait 0 explosion sous s = 0.32 ; il y en a une, a 0.3129.
Le compte etait faux de 2.3 % en s ; le verdict n'en depend pas ; la
lecon de methode (une bande criblee n'a pas de bord fixe en T) etait
dans le dossier. Consignee comme elle l'ecrit.

## 6. CANAL

Les lots v2 (9284c14b4ca57352) et v4 (037ea9a9cde7449e) ne sont jamais
parvenus a machine 1 : les deux predictions aveugles de A-3 tiennent
precisement a cette absence. A la charge de l'operateur.

P-1 est CLOS de mon cote. Aucune note ne suit.

-- FIN CONTRESEING_machine1_acte_P1_v1 --
