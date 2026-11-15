# Note hors chaîne : le résiduel de la chaîne E-A est son second ordre

Plume : machine 1. Date : 14/11/2026, soir. Statut : exploration hors chaîne, classe 3, non
certifiée, non rejouée par machine 2, faite APRÈS COUP sur des points déjà joués. Elle ne
tranche rien, ne modifie aucune pièce citée et n'ouvre aucun gel. Demande de l'opérateur :
dériver l'écart entre la chaîne et la lecture 2D (« Fais le alors ! »).

Aucune diagonalisation 2D n'a été faite par machine 1. Les largeurs Gamma_2D(3) et les
énergies E_re sont lues dans les JSON des deux runs déjà joués par machine 2 (sondes
5d80bf2edd26a6c1 et d51a9c6ce98b0452). Les éléments de matrice sont ceux du moteur
(82a0be882568fe0c), appelés tels quels. Les états sont ceux que la feuille 0a760e3a244e547d
juge : 262 états sur 24 points distincts, dont 243 hors des deux points extrêmes (1,85 et 2,15).

## 0. Verdict

1. L'écart entre la chaîne et la 2D n'est pas une affaire de domaine. C'est le terme suivant
   du même calcul : la chaîne du moteur est un premier ordre en g, et il lui manque le
   second ordre (les états hors de l'échelle résonante) et les sites de l'échelle situés
   sous l'état lu.
2. Avec ces deux ajouts, sans aucun paramètre ajusté, q = Gamma_chaîne / Gamma_2D tient dans
   [0,998 ; 1,512] pour les 243 états sur 243 (médiane 1,178), contre
   [0,375 ; 7,00] pour la chaîne du moteur. Dans un facteur 1,5 : 241 états sur 243,
   contre 143 sur 243 dans un facteur 2 au premier ordre.
3. Contrôle indépendant des largeurs : la même chaîne redonne le décalage d'énergie de l'état
   2D à 0,11 pour cent près en médiane (pire état : 0,50 pour cent), contre 7,7 pour cent au
   premier ordre avec les sites bas et 33 pour cent pour la chaîne du moteur.
4. Le second ordre a deux termes de signes opposés (déplacement des niveaux, saut au second
   voisin). Chacun seul fait pire que rien ; c'est leur somme qui tombe juste. Cela explique
   l'échec de l'essai du 13/11 (déplacement seul).
5. Ce qui reste est une surestimation d'un seul côté, qui croît comme le carré du désaccord :
   plus 4 à 5 pour cent à |δ| = 0,05, plus 16 à 32 pour cent à 0,10, plus 40 pour cent à
   0,12, un facteur 2,2 à plus 0,15. Les 4 à 5 pour cent sont au niveau de la précision de la
   lecture 2D elle-même (5 pour cent en médiane entre ses trois absorbeurs) ; le reste la
   dépasse. Sa forme est celle qu'aurait un troisième ordre : conjecture, non calculée.
6. Limites : calcul fait après coup sur 24 points connus ; une première écriture de ma plume
   était fausse et a été écartée (section 5) ; rien n'est certifié. Confiance de la plume :
   0,90 que le second ordre est bien l'explication du résiduel ; 0,85 que la chaîne d'ordre 2
   tiendrait dans un facteur 1,6 sur des points neufs à |δ| au plus 0,12.

## 1. Ce qui est calculé

Hamiltonien 2D du moteur : H = H0 + V, H0 = -n1 + w2 n2, V = (g/5) x^5. L'échelle résonante
de l'état (n1, n2) est la suite des sites m : (n1 + 2m, n2 + m), d'énergie libre m δ avec
δ = w2 - 2. La chaîne du moteur garde, sur les sites m au moins 0, la diagonale m δ et le
saut t_m entre voisins (élément de V pris aux occupations du site).

Le hamiltonien effectif sur l'échelle, à l'ordre g^2, forme symétrique (Schrieffer-Wolff,
ou forme normale au second ordre), est

    H_ab = E_a δ_ab + V_ab + (1/2) Σ_q V_aq V_qb [ 1/(E_a - E_q) + 1/(E_b - E_q) ]

où q parcourt les états hors de l'échelle et les E sont les énergies libres. La parité de
x^5 (chaque saut change n1 + n2 d'un nombre impair) ne laisse passer que deux termes :

- a = b : le déplacement Sigma2(m), déjà calculé par le moteur mais absent de la matrice de
  sa chaîne ;
- b = a + 2 sites : un saut au second voisin u_m, absent du moteur.

Il n'y a pas de correction d'ordre 2 au saut entre voisins ni de saut à trois sites
(interdits par la parité), ni de saut à quatre sites ou plus (hors de portée de deux sauts
de x^5). L'ordre 2 est donc complet avec ces deux termes. L'absorbeur, la lecture de l'état
(recouvrement maximal avec le site 0) et les réglages (M_facteur 4, eta au seizième) sont
ceux de la sonde, inchangés.

Second ajout, indépendant du premier : les sites m négatifs (jusqu'à épuisement de n1 ou de
n2), que la chaîne du moteur ignore. Ils ne portent aucune fuite, mais ils repoussent le
niveau de l'état lu.

## 2. Résultat par point

q = Gamma_chaîne / Gamma_2D(3), états jugés. « ordre 2 » : second ordre complet avec les
sites bas. Dernière colonne : écart relatif médian entre le décalage d'énergie de la chaîne
et celui de l'état 2D (E_re moins énergie libre), pour la chaîne du moteur puis pour l'ordre 2.

| w2 | facteur | id | n | q ordre 1 (moteur) : min, médiane, max | q ordre 2 : min, médiane, max | énergie : écart o1, o2 |
|---|---|---|---|---|---|---|
| 1,85 | 1 | T3 | 11 | 0,066 ; 0,979 ; 1,358 | 0,032 ; 1,038 ; 1,329 | 0,130 ; 0,0029 |
| 1,89 | 1 | H6 | 11 | 0,659 ; 0,958 ; 1,234 | 1,166 ; 1,229 ; 1,268 | 0,163 ; 0,0016 |
| 1,90 | 3/2 | E6 | 13 | 0,726 ; 0,934 ; 1,378 | 1,081 ; 1,111 ; 1,163 | 0,065 ; 0,0016 |
| 1,90 | 1 | J1 | 11 | 0,621 ; 0,897 ; 1,159 | 1,138 ; 1,197 ; 1,246 | 0,170 ; 0,0013 |
| 1,90 | 2/3 | H5 | 6 | 0,506 ; 0,662 ; 0,814 | 1,216 ; 1,300 ; 1,341 | 0,389 ; 0,0019 |
| 1,91 | 1 | E5 | 12 | 0,596 ; 0,845 ; 1,095 | 1,117 ; 1,175 ; 1,209 | 0,189 ; 0,0012 |
| 1,91 | 2/3 | H4 | 7 | 0,375 ; 0,605 ; 0,745 | 1,134 ; 1,210 ; 1,269 | 0,408 ; 0,0015 |
| 1,95 | 3/2 | J3 | 11 | 0,756 ; 0,842 ; 0,926 | 1,001 ; 1,030 ; 1,085 | 0,109 ; 0,0004 |
| 1,95 | 1 | A1 | 11 | 0,587 ; 0,758 ; 0,882 | 1,038 ; 1,062 ; 1,081 | 0,238 ; 0,0004 |
| 1,95 | 2/3 | J5 | 8 | 0,395 ; 0,545 ; 0,652 | 1,024 ; 1,046 ; 1,081 | 0,440 ; 0,0005 |
| 1,96 | 1 | T1 | 12 | 0,498 ; 0,756 ; 0,866 | 0,998 ; 1,042 ; 1,052 | 0,257 ; 0,0003 |
| 2,04 | 1 | T2 | 12 | 1,153 ; 1,334 ; 1,404 | 1,024 ; 1,040 ; 1,055 | 0,316 ; 0,0003 |
| 2,05 | 3/2 | J4 | 14 | 1,269 ; 1,418 ; 1,511 | 1,026 ; 1,052 ; 1,068 | 0,216 ; 0,0004 |
| 2,05 | 1 | A2 | 12 | 1,292 ; 1,505 ; 1,626 | 1,033 ; 1,053 ; 1,064 | 0,331 ; 0,0004 |
| 2,05 | 2/3 | J6 | 8 | 1,292 ; 1,502 ; 1,644 | 1,076 ; 1,092 ; 1,101 | 0,557 ; 0,0005 |
| 2,08 | 1 | E1 | 13 | 1,888 ; 2,529 ; 2,832 | 1,133 ; 1,206 ; 1,249 | 0,389 ; 0,0011 |
| 2,08 | 2/3 | H1 | 8 | 2,325 ; 2,759 ; 3,172 | 1,174 ; 1,185 ; 1,248 | 0,621 ; 0,0012 |
| 2,09 | 1 | E2 | 13 | 2,305 ; 3,094 ; 3,510 | 1,199 ; 1,285 ; 1,321 | 0,412 ; 0,0013 |
| 2,10 | 3/2 | E3 | 13 | 2,337 ; 2,867 ; 3,434 | 1,160 ; 1,270 ; 1,348 | 0,305 ; 0,0016 |
| 2,10 | 1 | J2 | 13 | 2,945 ; 3,735 ; 4,168 | 1,260 ; 1,316 ; 1,343 | 0,436 ; 0,0017 |
| 2,10 | 2/3 | H2 | 9 | 3,751 ; 5,065 ; 5,962 | 1,362 ; 1,465 ; 1,512 | 0,680 ; 0,0018 |
| 2,12 | 3/2 | E4 | 12 | 3,620 ; 4,005 ; 4,615 | 1,243 ; 1,300 ; 1,403 | 0,309 ; 0,0023 |
| 2,12 | 1 | H3 | 14 | 4,526 ; 5,909 ; 7,001 | 1,388 ; 1,426 ; 1,474 | 0,500 ; 0,0024 |
| 2,15 | 1 | T4 | 8 | 12,327 ; 18,348 ; 26,378 | 1,816 ; 2,189 ; 2,686 | 0,583 ; 0,0037 |

Bilan par état, hors 1,85 et 2,15 (243 états) :

| chaîne | états | q min | q médian | q max | dans 1,25 | dans 1,5 | dans 2 | dans racine de 10 |
|---|---|---|---|---|---|---|---|---|
| ordre 1, celle du moteur | 243 | 0,375 | 1,398 | 7,001 | 55 | 112 | 143 | 187 |
| ordre 1 + sites bas | 243 | 0,702 | 1,490 | 7,245 | 86 | 123 | 144 | 171 |
| ordre 2 sans sites bas | 243 | 0,568 | 1,023 | 1,407 | 201 | 239 | 243 | 243 |
| ordre 2 + sites bas (complète) | 243 | 0,998 | 1,178 | 1,512 | 167 | 241 | 243 | 243 |

Lecture du bilan. La ligne « ordre 2 sans sites bas » a la plus petite erreur médiane, mais
par compensation : l'oubli des sites bas abaisse la largeur d'environ dix pour cent et
masque la surestimation de la section 4. La version complète est celle que les énergies
désignent (section 3) ; son erreur est d'un seul signe et régulière.

Les deux points extrêmes. À 2,15 (hors domaine au sens de la garde) : q passe de
[12,3 ; 26,4] à [1,82 ; 2,69]. À 1,85 (D1 au-dessus de 1/5, second canal proche) :
neuf états sur onze vont de 0,30 à 1,33 ; deux restent vingt à trente fois trop bas
((5,2) q = 0,032 ; (6,1) q = 0,053).
La chaîne 2:1 n'y voit pas la fuite, ce qui ressemble au cas « deux chaînes concurrentes »
documenté dans la littérature (note d'antériorité v3).

## 3. Contrôle indépendant : les énergies

Les largeurs ne sont pas la seule donnée des JSON : chaque état 2D a son énergie E_re. Son
écart à l'énergie libre du site est une prédiction de la chaîne qui n'a servi à rien régler.
Sur les 243 états, écart relatif médian (et pire état) :

- chaîne du moteur : 33 pour cent (75) ;
- premier ordre avec les sites bas : 7,7 pour cent (23) ;
- second ordre avec les sites bas : 0,11 pour cent (0,50).

Variantes partielles, avec sites bas (journal des contrôles) : déplacement seul 0,22 pour
cent (pire 1,6), second voisin seul 0,95 pour cent (pire 4,8). Les énergies préfèrent donc
la somme des deux termes à chacun pris seul, indépendamment des largeurs. Le déplacement
Sigma2 du site 0 vaut en médiane 5 pour cent du décalage, de signe opposé (de moins 21 à
plus 9 pour cent selon l'état) : l'accord à un pour mille le vérifie à quelques pour cent
près.

## 4. Décomposition et lois d'échelle

Médianes de q, sans les sites bas (journal de lecture v1), sur dix points :

| w2 | facteur | ordre 1 | + Sigma2 seul | + second voisin seul | les deux |
|---|---|---|---|---|---|
| 1,85 | 1 | 0,979 | 4,646 | 0,096 | 0,962 |
| 1,90 | 1 | 0,897 | 3,184 | 0,250 | 1,097 |
| 1,95 | 1 | 0,758 | 1,495 | 0,462 | 0,959 |
| 1,95 | 2/3 | 0,545 | 1,315 | 0,290 | 0,748 |
| 2,05 | 1 | 1,505 | 0,611 | 2,178 | 0,954 |
| 2,05 | 2/3 | 1,502 | 0,482 | 2,374 | 0,819 |
| 2,10 | 1 | 3,735 | 0,488 | 7,164 | 1,190 |
| 2,10 | 2/3 | 5,065 | 0,364 | 11,423 | 1,101 |
| 2,12 | 1 | 5,909 | 0,440 | 12,231 | 1,272 |
| 2,15 | 1 | 18,348 | 0,441 | 40,655 | 1,942 |

Le déplacement seul renverse l'erreur ; le second voisin seul l'aggrave jusqu'à un facteur
40. Le signe s'explique. Sur tous les sites de barrière des 243 états, Sigma2(m) - Sigma2(0)
est positif et u_m négatif (journal des contrôles v2), alors que la diagonale m δ change de
signe avec δ. Sous 2,00 le déplacement abaisse donc la barrière (la largeur monte) et le
second voisin interfère destructivement avec le chemin du premier ordre (la largeur
baisse) ; au-dessus de 2,00 les deux rôles s'inversent. La somme suit le déplacement, en
partie compensé par le second voisin. C'est le changement de sens de q à w2 = 2,00.

Ordre de grandeur sur un état (A1, (7,2), δ = -0,05) : le second voisin retire de 1 à 3
pour cent d'amplitude par site, soit 19 pour cent sur les neuf sites, donc un facteur 0,65
sur la largeur ; le calcul complet donne 0,61 pour la médiane du point. Les corrections
sont les plus fortes au bord de la barrière, là où saut et désaccord se valent.

Loi d'échelle de la correction (243 états, avec sites bas) : ln(Gamma_1 / Gamma_2) = a δ m_bord
avec a = 1,02 (corrélation 0,94), m_bord étant le dernier site de barrière. L'erreur du
premier ordre croît donc avec le désaccord ET avec la longueur de la barrière, qui est plus
grande à petit couplage. C'est la dépendance au facteur de couplage relevée par l'acte
e718d2db619af9b1, et c'est pourquoi la garde G-1 ne pouvait pas tenir : son critère D2a
favorise les petits couplages, là où la barrière est la plus longue.

Résidu de l'ordre 2 complet, par désaccord :

| δ | états | q ordre 2 : min | médiane | max |
|---|---|---|---|---|
| -0,11 | 11 | 1,166 | 1,229 | 1,268 |
| -0,10 | 30 | 1,081 | 1,163 | 1,341 |
| -0,09 | 19 | 1,117 | 1,189 | 1,269 |
| -0,05 | 30 | 1,001 | 1,053 | 1,085 |
| -0,04 | 12 | 0,998 | 1,042 | 1,052 |
| +0,04 | 12 | 1,024 | 1,040 | 1,055 |
| +0,05 | 34 | 1,026 | 1,055 | 1,101 |
| +0,08 | 21 | 1,133 | 1,201 | 1,249 |
| +0,09 | 13 | 1,199 | 1,285 | 1,321 |
| +0,10 | 35 | 1,160 | 1,322 | 1,512 |
| +0,12 | 26 | 1,243 | 1,398 | 1,474 |

Ajustement à un paramètre : ln q = 2,87 δ^2 m_bord (corrélation 0,90, écart-type restant
0,05). Le résidu est un peu plus fort au-dessus de 2,00 qu'en dessous à |δ| égal. Sa forme
(carré du désaccord, croissant avec la longueur) est celle d'une correction relative du saut
entre voisins à l'ordre g^3, que la parité autorise. Ce terme n'est pas calculé ici ; son
identification est une conjecture de la plume.

## 5. Contrôles, et ce qui a été écarté

- Le premier ordre de mes scripts redonne les largeurs de chaîne des JSON à 3.3e-03 près
  (à 5.8e-02 sur un état de T3) ; Sigma2 du site 0 redonne celui du moteur à 5e-15 près.
- Stabilité numérique de la chaîne d'ordre 2 complète (journal de stabilité) : longueur de
  la chaîne (M_facteur 2 et 8), recul de l'absorbeur, force de l'absorbeur (eta au huitième
  et au trente-deuxième). Toutes variantes confondues, q bouge de 1,4 pour cent en médiane
  et de 3,5 pour cent au neuvième décile. Il bouge de plus de 5 pour cent pour 7 états sur
  243, de deux sortes : quatre états de largeur 2D au plus 3,5e-12, sensibles à la seule chaîne
  longue (pire : 17 pour cent, un état ; cause probable, non vérifiée : l'arrondi de la
  diagonalisation non hermitienne aux plus petites largeurs) ; trois états à barrière courte
  du point E6, sensibles à la seule chaîne courte (5,6 pour cent au plus).
- Précision de la référence : la lecture 2D varie entre ses trois forces d'absorbeur de 4,8
  pour cent en médiane, de 10 pour cent au neuvième décile et de 15 pour cent au pire, sur
  les 243 états jugés (journal des contrôles v2). Un écart de 5 pour cent entre chaîne et 2D
  n'est donc pas interprétable ; un écart de 20 pour cent l'est.
- ÉCARTÉ, défaut de ma plume : ma première écriture (script v1) prenait les dénominateurs à
  l'énergie de l'état au lieu de l'énergie libre de chaque site. Ces dénominateurs passent
  par zéro le long de la chaîne à tous les points (plus petit dénominateur : 0,01 au plus,
  contre 0,7 à 1 avec les énergies libres ; journal des contrôles, partie a) et donnaient
  des largeurs nulles. Elle est écartée pour cette raison, pas pour son résultat.
- NON RETENU comme contrôle : couper les termes d'ordre 2 au-delà d'un site (script v2,
  colonnes « portée ») change q d'un facteur allant jusqu'à 2. Ce n'est pas une fragilité du
  résultat : la coupure crée une marche artificielle sur la diagonale. Le test pertinent est
  celui de la longueur et de l'absorbeur, ci-dessus.
- Choix d'écriture faits en voyant les données : la forme symétrique (standard, sans
  alternative saine essayée) et l'ajout des sites bas (désigné par les énergies, pas par
  les largeurs). Aucun nombre n'a été ajusté.

## 6. Ce que la note ne dit pas

- Elle ne remplace ni l'acte e718d2db619af9b1 ni son verdict : la garde G-1 ne tient pas, et
  cela reste vrai. Elle en propose la cause.
- Elle ne dit rien hors de la fenêtre jouée (w2 de 1,85 à 2,15, facteurs 2/3 à 3/2, états
  jugés par la feuille).
- Elle n'est pas un test : les 24 points étaient connus avant le calcul.
- Rattachement à la littérature (à vérifier sur texte, cité de mémoire de la note
  d'antériorité v3) : le déplacement des niveaux est l'amélioration « énergies non perturbées
  au-delà de l'ordre dominant » de la revue RAT ; le saut au second voisin produit au second
  ordre n'y a pas été cherché.

## 7. Suites possibles, non décidées

- Un gel de la chaîne d'ordre 2 sur des points neufs, avec la borne annoncée d'avance
  (par exemple : tous les états jugés dans un facteur 1,6 pour |δ| au plus 0,12). C'est le
  seul moyen de transformer cette note en résultat.
- Le troisième ordre (correction du saut entre voisins), pour voir si le résidu en δ^2 tombe.
- Porter les deux termes dans le moteur : pas avant un gel, et par une nouvelle version.

## 8. Pièces de la plume (convention B)

- `chaine_ordre2_machine1_v1.py` : dad692fcef3f4551
- `chaine_ordre2_machine1_v1.log` : ab44337d4032a15e
- `chaine_ordre2_machine1_v2.py` : 78ab699fd31c8870
- `ordre2_par_etat.json` : 8f2177ac7de29570
- `lecture_ordre2_machine1_v1.py` : a7e213047655fa89
- `lecture_ordre2_machine1_v1.log` : 609137fb0bca64a5
- `chaine_ordre2_machine1_v3.py` : 78893073e78e2b55
- `ordre2_par_etat_v3.json` : c4ff0e3030b89c0c
- `lecture_ordre2_machine1_v2.py` : 5a9a94a20a443112
- `lecture_ordre2_machine1_v2.log` : 4fc9d7990866da30
- `controles_ordre2_machine1_v1.py` : 683029b3714125ff
- `controles_ordre2_machine1_v1.log` : fa94731ed5a0b08f
- `controles_ordre2_machine1_v2.py` : 6e48257ef99fa6a8
- `controles_ordre2_machine1_v2.log` : afbb06a2a9ffbb0c
- `stabilite_bas_machine1_v1.py` : 08ad981637a1c754
- `stabilite_bas_machine1_v1.log` : 9410ca6c46fac5fb
- `construction_note_residuel_machine1_v1.py` : 3245db2783b34ba2
- `note_residuel_gabarit.txt` : 434c188695ceb051
