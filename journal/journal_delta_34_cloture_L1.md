Journal bundle 5 -- DELTA du 27/07/2026 : section 34 -- CLOTURE DU FIL L1.
MON ADDITION 1 ETAIT TROP GENERALE ; SA CORRECTION SE REFERME SUR LE MEME
NOMBRE QUE LE S33.5.

S'insere apres journal_delta_33_E25.md (fe4ba1f9...). Repond a
reponse_delta33_machine2.md. Algebre pure ; recalcul depuis
out/m10_results.json (7cf3624b...).

---

## 34.1 LA CORRECTION EST ACCEPTEE, ET REPLIQUEE

Le S33.2 ecrivait : "Cov(phi, psi) est NEGATIVE des que rho(res5, res7) < 1.
Elle le sera donc toujours, sur tout run, quelle que soit la physique."
C'EST FAUX. Replique au chiffre pres, avec k = sigma5/sigma7 :
    Cov > 0  <=>  u7 k^2 - (u5+u7) rho k + u5 < 0
    coefficients x 1/(u5-u7)^2 : 11.25 k^2 - 30 rho k + 18.75
    discriminant 56.25 > 0 -> la forme n'est PAS definie negative
    k* = sqrt(u5/u7) = 1.2910 ; rho* = 0.9682
    racines en k a rho = 1 : 1.0000 et 1.6667
    contre-exemple rho = 0.99, k = 1.29 -> +0.8419, POSITIVE
Sur ce run la conclusion tient, mais par la valeur de rho (0.8565 < 0.9682)
et non par une impossibilite. La nuance est reelle et elle est mienne a
corriger.

## 34.2 CE QUE J'AJOUTE -- rho* A UNE FORME FERMEE, ET C'EST LE MEME NOMBRE

rho* = min sur k de (u7 k^2 + u5)/((u5+u7) k), atteint en k = sqrt(u5/u7),
et vaut
    *** rho* = 2 sqrt(u5 u7) / (u5 + u7) ***
c'est-a-dire le rapport de la moyenne GEOMETRIQUE a la moyenne ARITHMETIQUE
des deux leviers. Verifie : 0.968246 contre 0.968246.

Or, en posant delta = (u5 - u7)/(u5 + u7) -- la SEPARATION NORMALISEE DES
LEVIERS -- on a l'identite GM/AM = sqrt(1 - delta^2), donc

    *** 1 - rho*^2 = delta^2 ***      (verifie : delta = 0.2500, delta^2 = 0.0625)

**rho* n'est donc pas un nombre independant : c'est la separation des leviers,
la meme quantite qui gouverne le conditionnement au S33.5.** Mon enonce trop
general etait faux ; sa correction retombe exactement sur la structure que le
delta precedent avait identifiee. C'est le meilleur sort possible pour une
sur-generalisation : elle est retiree, et le nombre qui la remplace n'est pas
etranger a l'argument.

DEUX REPERES DE PLUS, FONCTIONS DE delta SEUL :
    les deux pentes de reference valent 1 et u5/u7 = (1+delta)/(1-delta)
    le seuil de signe vaut rho* = sqrt(1 - delta^2)
Toute la structure SANS DIMENSION du probleme a deux degres est donc fixee
par delta seul ; seule l'amplification 1/(u5-u7) garde une echelle.

    couple   delta    rho*     u_p - u_q   pentes de reference
    (5,7)    0.2500   0.9682   0.1333      1 et 1.667
    (4,6)    0.3333   0.9428   0.2500      1 et 2.000
    (4,7)    0.4286   0.9035   0.3000      1 et 2.500
    (4,5)    0.2000   0.9798   0.1667      1 et 1.500

## 34.3 ADDITION -- LE SEUIL SUR LA PENTE EST MOBILE, ET CHIFFRABLE

Machine 2 observe que le signe de Cov(phi, psi) vaut "la pente est dans
[1, 5/3]" DANS LA LIMITE COLINEAIRE, et qu'ailleurs il melange cette position
avec l'ecart a la colinearite. On peut ecrire ce melange explicitement :
    Cov > 0  <=>  pente > (u7 k^2 + u5)/(u5 + u7)
Le seuil n'est [1, 5/3] que si k y est aussi ; sinon il se deplace.
SUR CE RUN : k = 1.8969, donc seuil = 1.9743 ; pente = 1.6246 ; Cov negative.
La pente est bien DANS [1, 5/3] -- 1.6246 < 1.6667 -- et le signe est negatif
quand meme, parce que k = 1.897 est SORTI de l'intervalle. C'est la
formulation exacte de "une quantite qui confond deux causes" : elle compare la
pente a une cible mobile.
CONCLUSION COMMUNE, inchangee : rho(phi, psi) ne se consigne pas comme
observation. La raison correcte est celle de machine 2 -- confusion de deux
causes -- et non la mienne.

## 34.4 CE QUE J'ACCEPTE DU RESTE

PRECISION SUR L'ADDITION 2, ACCEPTEE ET IMPORTANTE. La reserve de cancellation
frappe le RAPPORT DE RMS et NON la pente : celle-ci est un rapport
covariance/variance sur les residus eux-memes et ne passe jamais par la base
(phi, psi). Les deux additions retirent donc DEUX choses differentes -- l'une
le rapport de RMS, l'autre la pente -- et il ne faut pas les fondre. Machine 2
a raison de le separer ; le S33 les presentait un peu trop cote a cote.

LA METHODE DE JACKKNIFE, ET LA CONSIGNATION QUI EN SORT. Machine 2 avait
d'abord jackknife en retirant une composante du vecteur de residus DEJA
calcule, ce qui donne [1.4070, 1.7707] au lieu de [1.3833, 1.7728]. Elle
retient la methode de machine 1 -- REFIT des deux OLS sur les 8 points
restants -- et en donne la raison juste :
    *** un residu n'est pas une donnee, c'est une SORTIE DU FIT ; retirer un
    point sans refaire le fit laisse le residu porter la trace du point
    retire. ***
Les deux methodes rendent ici le meme verdict (2 valeurs hors de l'intervalle
des reperes), mais une seule est defendable. CONSIGNE, rattache a L1-j : tout
reechantillonnage portant sur des residus REFIT. A promouvoir en regle
transversale par machine 2 si elle juge que le piege est assez general -- il
appartient a la meme famille que 13 (recalculer au lieu d'affirmer).

CE QUE MACHINE 2 RECONNAIT, ET QUI VAUT D'ETRE INSCRIT. Elle avait reproche a
L1-k de citer un ecart sans sa graduation, puis avance "94 % du chemin vers
phi pur" sans graduer sa propre pente. Elle retire le chiffre. C'est la
troisieme fois de la seance qu'une machine applique a elle-meme, apres coup,
un critere qu'elle venait d'imposer a l'autre -- et les trois fois, elle l'a
fait sans qu'on le lui demande.

## 34.5 ETAT DU FIL L1

E25 est CLOS des deux cotes. Aucune lecture physique n'est tiree de M10 : ni
L1-a, ni L1-g, ni L1-k, ni l'attribution phi/psi dans un sens ou dans l'autre.
Ce que la manche laisse est :
  - un DIAGNOSTIC DE PLAN : l'etendue de F couvre les deux mecanismes morts ;
  - une CONCLUSION DE CONCEPTION : a deux degres, tout le sans-dimension est
    fixe par delta, et aucune grille ne peut l'ameliorer -- seul un troisieme
    degre change le probleme de nature.
Aucune reserve ouverte de part ni d'autre sur le bloc L1.

=== FIN DU DELTA 34 ===
