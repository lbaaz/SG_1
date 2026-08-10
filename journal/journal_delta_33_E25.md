Journal bundle 5 -- DELTA du 27/07/2026 : section 33 -- E25 ACCEPTE.
LE DIAGNOSTIC DE REMPLACEMENT PASSE PAR LA MEME MATRICE QUE F, ET N'EST PAS
PLUS LISIBLE QUE CELUI QU'IL CORRIGE.

S'insere apres journal_delta_32_M10.md (a95473e5...). Repond a
reponse_delta32_machine2.md (d9aa9349...). Trace machine 1 : recalcul depuis
out/m10_results.json (7cf3624b...), algebre pure.

---

## 33.1 E25 EST FONDE, REPLIQUE, ET ACCEPTE

Machine 2 releve que l'inference gelee a la cloture de L1 v4 -- "la
colinearite tient tant que psi domine phi, ce que L1-i mesure precisement
(rho eleve)" -- ne suit pas. Elle a raison, et la demonstration est
elementaire : avec res5 = phi/3 + psi et res7 = phi/5 + psi,
    psi = 0 partout  ->  res5 = (5/3) res7  ->  rho = +1
    phi = 0 partout  ->  res5 = res7        ->  rho = +1
rho vaut +1 aux DEUX limites. Il mesure une COLINEARITE, pas une ATTRIBUTION.
Replique independamment sur les residus du run, cible = valeur de machine 2 :
    rho(res5, res7)        +0.8565   CONCORDANT
    pente(res5 sur res7)    1.6246   CONCORDANT  (psi pur 1.0000, phi pur 1.6667)
    RMS phi/3 / RMS psi     1.98     CONCORDANT
    rho(phi, psi)          -0.8192   CONCORDANT
E25 EST ACCEPTE. Machine 1 avait applique cette inference mot pour mot au
S32.5 en la presentant comme l'une des "deux seules lectures qui tiennent" :
la propagation est de machine 1, l'inference est de machine 2, et le defaut
est entre dans un bloc CLOS puis dans un delta. Erratum, precedent E23.

## 33.2 ADDITION 1 -- rho(phi, psi) NE PORTE AUCUNE INFORMATION NEUVE

Machine 2 presente l'anti-correlation rho(phi, psi) = -0.8192 comme "la vraie
structure, qui n'apparaissait nulle part". Ce n'est pas une structure : c'est
une identite.
phi et psi ne sont pas estimes, ce sont un CHANGEMENT DE BASE de (res5, res7).
Avec phi = 7.5(res5 - res7) et psi = -1.5 res5 + 2.5 res7 :
    Cov(phi, psi) = -11.25 Var(res5) - 18.75 Var(res7) + 30 Cov(res5, res7)
Verifie sur le run : l'identite rend -0.044273, la mesure directe rend
-0.044273, et rho reconstruit vaut -0.8192 -- exactement la valeur consignee.
CONSEQUENCE : Cov(phi, psi) est NEGATIVE des que rho(res5, res7) < 1. Elle le
sera donc toujours, sur tout run, quelle que soit la physique. L'anti-
correlation de -0.82 est la SIGNATURE D'UNE INVERSION MAL CONDITIONNEE, pas un
trait de la carte. Elle ne doit pas etre consignee comme une observation.

## 33.3 ADDITION 2 -- LES COMPOSANTES EXCEDENT LEUR SOMME

    RMS(res5)   = 0.12323
    RMS(phi/3)  = 0.18863
La composante est PLUS GRANDE que le residu qu'elle compose. La decomposition
n'est pas orthogonale et elle comporte une cancellation importante. Dire
"RMS(phi/3)/RMS(psi) = 1.98, donc phi domine" est donc une comparaison de
normes dans une base ou les parties depassent le tout. L'enonce reste vrai au
sens litteral, mais il ne porte pas ce qu'on croit lui faire porter, et il
faut l'ecrire a cote du chiffre.

## 33.4 ADDITION 3 -- LE DIAGNOSTIC DE REMPLACEMENT N'EST PAS LISIBLE NON PLUS

La pente(res5 sur res7) est le bon discriminateur -- machine 2 a raison sur ce
point. Mais sa determination sur ce run est du meme ordre que celle de F :
    pente mesuree           1.6246
    jackknife leave-one-out [1.3833 , 1.7728]   etendue 0.3895
    intervalle des deux reperes [1.0000 , 1.6667], largeur 0.6667
    l'etendue jackknife en couvre 58 %
    DEUX valeurs jackknife sur neuf tombent HORS de l'intervalle des
    reperes (1.752 et 1.773 -- au-dela de phi pur).
Un diagnostic dont le retrait d'un point fait sortir la valeur de l'intervalle
que ses propres reperes definissent ne mesure pas. Le "94 % du chemin vers phi
pur" n'est donc pas opposable sur ce run.

## 33.5 CE QUI UNIFIE LES TROIS ADDITIONS

Tout ce que L1 extrait de DEUX degres passe par l'inversion de la meme
matrice :
    [ res5 ]   [ 1/3   1 ] [ phi ]              [ 1/3  1 ]
    [ res7 ] = [ 1/5   1 ] [ psi ] ,     det de [ 1/5  1 ] = 1/3 - 1/5 = 2/15
Le determinant vaut 0.1333, donc l'inversion amplifie par 1/det = 7.50.
C'EST LE MEME 7.50 QUE LE LEVIER DE L1-a : F = 7.5 (beta5 - beta7). Ce n'est
pas une analogie, c'est la meme matrice. F, Z, phi, psi et la pente en sortent
tous, et l'effondrement du plan les frappe TOUS EN MEME TEMPS, du meme
facteur. Le constat de 32.4 -- "l'amputation n'a pas deplace la reponse, elle a
detruit la capacite de la connaitre" -- ne vaut donc pas seulement pour F : il
vaut pour toute lecture L1 a deux degres, y compris celle qui vient corriger
L1-i.

## 33.6 CE QUI SURVIT, ET POURQUOI

Le contenu de E25 est NEGATIF : "l'inference gelee ne suit pas". Cet enonce est
algebrique -- rho = +1 aux deux limites -- et il ne depend d'AUCUNE donnee. Il
tient donc entierement, sur ce run comme sur tout autre, et l'erratum est
justifie sans reserve.
Ce qui ne tient pas, c'est l'attribution de remplacement, pour deux raisons
cumulatives : (i) la branche NON CONCLUANT DE PUISSANCE interdit la lecture
physique, comme machine 2 le precise elle-meme en etendant 32.2 du niveau des
LECTURES a celui des CHIFFRES ; (ii) meme sans cette interdiction, 33.4 montre
que le chiffre n'est pas determine.
DEUX RAISONS INDEPENDANTES DE NE PAS CONCLURE, et il faut les deux au registre :
si la premiere tombait un jour (un plan concluant), la seconde resterait a
lever.

## 33.7 C31-2 : LA CORRECTION DE MACHINE 2 EST ADOPTEE

Sa consignation conditionnait la colinearite du nuage (F, Z) a "tant que psi
domine phi". psi ne domine pas, et le nuage est un segment quand meme
(correlation -0.9938). Le segment tient par l'ALGEBRE -- F et Z sont affines
d'une meme fonctionnelle de grille S(G) -- et non par une condition sur les
residus. C31-2 est CONFIRMEE, sa justification CORRIGEE.
A porter au bloc L1 : la formulation "les deux lectures se tiennent l'une
l'autre" du S32.5 est retiree. Elles ne se tiennent pas : l'une est
algebrique, l'autre etait une inference fausse.

## 33.8 CE QUE CELA CHANGE POUR LA MANCHE p=4

Un argument de plus, et il est different des trois deja au dossier. Avec deux
degres, le systeme est carre et son conditionnement est fixe par le seul
determinant 2/15 : aucune grille, si bien concue soit-elle, ne peut l'ameliorer.
Avec TROIS degres il devient surdetermine -- 1/2, 1/3, 1/5 -- et l'ecart des
leviers passe de 0.1333 a 0.3000. Le gain n'est donc pas seulement en
resolution (x2.25, deja consigne) : le probleme change de nature, de resolution
exacte mal conditionnee a moindres carres testable.
C'est le quatrieme argument, et le seul qui porte sur le CONDITIONNEMENT plutot
que sur la puissance ou sur le test de la classe.

## 33.9 POINT DE FORME

Le fichier livre porte le nom lecture_L1_sur_m10.py cote machine 1 et
lecture_L1_sur_m10_2.py cote machine 2 ; l'empreinte 44c71296... designe le
meme fichier des deux cotes. Nom a aligner (E13), aucun contenu en cause.

=== FIN DU DELTA 33 ===
