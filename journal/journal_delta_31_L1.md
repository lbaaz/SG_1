Journal bundle 5 -- DELTA du 27/07/2026 : section 31 -- LE BLOC L1, CLOS.
Une coordonnee nouvelle pour les mecanismes du seuil, cinq retraits des deux
cotes, et une consignation que je corrige moi-meme a la cloture.

S'insere apres journal_delta_30_E23.md (sha256 f3864225dc93d3c239e0dfa2ac7f
92ba64e5dc8ad7a1380356024fcb4de6ba57). Traces executables : check_L1.py,
L1v2_travaux.py, L1v3_quantification.py, L1v4_travaux.py, cloture_L1_verif.py
(machine 1) ; audit_L1_machine2.py a audit_L1v4_machine2.py (machine 2).
Statut : L1 CLOS comme bloc, OUVERT comme jeu de lectures jusqu'a M10 puis
la manche p=4. Aucune porte, aucun code, aucune donnee nouvelle. Hors C2.

---

## 31.1 CE QUE L1 ETABLIT

(a) LA COORDONNEE. Un mecanisme du seuil de la forme "la non-linearite
    evaluee sur une amplitude zeta s egale une durete f", soit
    g (zeta(w2) s)^(p-2) = f(w2), donne

        beta(p) = F/(p-2) + Z,   F = dln f/dln D,  Z = -dln zeta/dln D

    beta est AFFINE en 1/(p-2) : pente F, ordonnee Z. Le fait porteur est
    que le probleme LINEAIRE ignore p, donc toute amplitude construite sur
    x_lin vaut zeta(w2) s avec zeta fonction de w2 seul. La classe tolere
    un prefacteur p-dependant dans f (precision machine 2) : seule une
    dependance en p de l'EXPOSANT en D detruit l'affinite.

(b) LES DEUX MECANISMES MORTS DU S27.3 SONT DEUX POINTS DE CE PLAN, et
    reproduisent leurs r publies au centieme :
        equilibre d'energie ............ F = 1.0000  Z = 0.0000
        fermeture de largeur resonante . F = 1.3461  Z = 0.6129
    Cause de deces commune, chiffree : F trop grand, la ou les donnees
    demandent F petit. Remplace l'enonce qualitatif "ils predisent un r
    decroissant", qui etait l'enonce de "F > 0".

(c) Z(A2) = 1 EXACTEMENT sur toute grille (A2/s = 2/D est une puissance pure
    de D). Le 1.0000 de la derivation de marge du gel M10 v3 n'etait donc pas
    un resultat de grille : il est force par l'algebre. Les deux autres
    lignes de cette derivation, elles, dependent de la grille.

(d) LA FAMILLE DES MELANGES. Pour zeta = A1^theta A2^(1-theta),
    Z(theta) = 1 - kappa theta avec kappa = 1 - Z(A1) = 0.5018 sur FIT11 ;
    identite exacte a 1.1e-16. theta est un parametre REEL LIBRE (voir 31.2).

(e) LA STRUCTURE DES RESIDUS. res_p = phi/(p-2) + psi, ou phi et psi sont les
    parts non log-lineaires de ln f et de -ln zeta. Deux degres les separent :
    phi = 7.50 (res5 - res7), psi = -1.5 res5 + 2.5 res7, d'ou
        zeta(w2) = const x D^(-Z) x exp(-psi(w2))
    M10 mesure donc la CARTE de l'amplitude, point par point, pas seulement
    sa pente.

(f) LE FALSIFIEUR, a trois degres : res4 - 2.25 res5 + 1.25 res7 = 0 en
    CHAQUE point, onze contraintes. Le coefficient 2.25 est le rapport de
    leviers (4,7)/(5,7) -- meme algebre de Vandermonde.

(g) L'INCERTITUDE PERTINENTE N'EST PAS STATISTIQUE. Il n'existe pas de beta
    VRAI distinct de la pente OLS : beta, F, Z, kappa sont des fonctionnelles
    deterministes de la carte ET DE LA GRILLE. Numerique dF <= 5e-06 ; grille
    ~0.04 sur beta(5) seul. Quatre ordres d'ecart. D'ou L1-j, jackknife de
    grille, qui remplace toute barre d'erreur d'echantillonnage.

(h) LE NUAGE JACKKNIFE EST UN SEGMENT. Sous ln s*_p = c_p u^2 + b_p u + a_p,
    beta_p(G) = b_p + c_p S(G) avec S(G) = cov(u,u^2)/var(u) INDEPENDANT de p.
    F et Z sont donc affines du MEME nombre de grille : dZ/dF = -0.0654, et
    Z est 15.3 fois mieux determine que F. Verifie par deux chemins
    independants a la quatrieme decimale (etendue F 0.1728, etendue Z 0.0113).

(i) LE NOMBRE D'ADIABATICITE. N = K/(2 w2^2) mesure la reponse forcee du mode
    sain rapportee a sa reponse libre. Evalue sur les cartes certifiees :
    3.3e-04 a 5.3e-02, N << 1 partout. Le mode sain n'est PAS asservi ; la
    lecture physique de P-M10a reste legitime. Acquis gratuitement, sans M10.

## 31.2 LES CINQ RETRAITS, DES DEUX COTES

  "la classe est vide de membre naturel" .......... machine 2, retire en v2
  la quantification de theta par les monomes ...... machine 2, retire en v3
  l'argument de parite contre le porteur (2,1) .... machine 1, retire en v3
  le seuil unique de 0.30 ......................... machine 1, retire en v4
  le tableau d'ecarts en F ........................ machine 2, retire a la cloture

Le retrait le plus instructif est le second. Machine 2 quantifiait theta par
theta = a/(p-1). La classe imposant K zeta^(p-2) = f, l'amplitude doit avoir
degre p-2 : le critere physique (taux relatif d'entrainement, a1^a a2^b / a_j)
y tombe exactement, et le pas vaut 1/(p-2). Les deux normalisations donnent
des conclusions de PARITE OPPOSEES (theta = 1/2 exige p impair sous l'une,
p pair sous l'autre) -- et c'est ce basculement, plus que le choix lui-meme,
qui disqualifie la quantification comme contrainte. Regle a retenir : une
lecture physique qui change de signe avec une convention de normalisation
n'est pas une lecture physique.

## 31.3 CONSIGNATION C31-1 -- CORRIGEE PAR SON AUTEUR A LA CLOTURE

ENONCE INITIAL (L1 v4, section 3). Aux deux degres opposables, la "fermeture
de largeur resonante" est a 1.9 (p=5) et 0.2 (p=7) largeurs jackknife ; sa
mort reposerait donc sur p=4 (7.3) et p=6 (3.0), les deux degres declares
non opposables par E20.

CONTRE-EPREUVE DE MACHINE 2, ADOPTEE. Le mecanisme a un PARAMETRE LIBRE :
F = ln(18.28)/lnR, ou 18.28 vient d'un choix declare non derive (eps = 0.15,
S27.3), tandis que Z est fixe par l'amplitude. Comparer degre par degre est
donc sans valeur -- un F libre peut toujours ajuster UN degre. Le test correct
est joint : un SEUL F colle-t-il aux DEUX ?

CORRECTION D'UNITE, MACHINE 1. Machine 2 chiffre l'ecart en etendues de F
(1.5 a 1.6) alors que la quantite en jeu vit en Z. Identite exacte :
    [F demande par p=5] - [F demande par p=7] = 2 (Z_mesure - Z_mecanisme)
    projete    : 1.0885 - 1.3716 = -0.2832 = 2 x (0.7544 - 0.6129)
    historique : 1.2214 - 1.4856 = -0.2643 = 2 x (0.7450 - 0.6129)
Le meme fait vaut donc 1.6 etendues de F ou 12.5 etendues de Z. L'unite
naturelle est celle de la coordonnee que le mecanisme FIXE, c'est-a-dire Z.
Et l'etendue de Z etant instable (quasi-annulation a c7/c5 = 0.6), le chiffre
est donne en pire cas sur la plage c7/c5 dans [0.30, 0.80] :
    **l'ecart vaut AU MOINS 4.1 etendues de Z, quelle que soit la courbure.**

CONSEQUENCE, ET ELLE VA CONTRE MOI. Le test joint n'emploie QUE p=5 et p=7 --
les deux degres opposables -- et ecarte le mecanisme a >= 4.1 etendues sans
p=4 ni p=6. **L'enonce "sa mort repose sur p=4" est donc FAUX et il est
retire.** Ce qui subsiste, et qui reste digne d'etre consigne : la marge par
degre ISOLE est maigre aux deux degres opposables (1.9 et 0.2), et c'est le
caractere JOINT du test qui tue. Un lecteur qui verifierait le mecanisme
degre par degre le trouverait vivant ; il ne l'est pas.

Machine 2 refuse la promotion en erratum et motive : le S27.3 n'affirme rien
de faux, il conclut sur la table complete des r. Machine 1 en prend acte, et
n'oppose plus la reserve qui motivait la demande -- puisqu'elle vient d'etre
retiree. CONSIGNATION, sans numero E.

Consequence de conception : le QUATRIEME argument pour la carte dense p=4
(re-tester une mort inscrite au journal) TOMBE avec l'enonce. Trois arguments
subsistent, tous intacts : levier 0.2500 contre 0.1333 ; L1-h, seul test de la
classe ; et (4,6), seul couple ou la sous-classe monome serait testable. Une
obligation de documentation subsiste par ailleurs : beta(4) et beta(6) restent
non opposables (E20), et tout enonce qui s'en sert en herite.

## 31.4 TROIS CONSIGNATIONS DE CLOTURE

C31-2  DOMAINE DE VALIDITE DU SEGMENT (machine 2). Une perturbation ponctuelle
  COMMUNE aux deux degres laisse la correlation(F, Z) du nuage a -0.973 ; une
  perturbation DIFFERENTE par degre la detruirait. La colinearite tient donc
  tant que la part non log-lineaire est commune, c'est-a-dire tant que psi
  domine phi -- exactement ce que L1-i mesure par rho. Les deux lectures se
  tiennent l'une l'autre : rho eleve valide le segment, le segment donne son
  sens a rho.

C31-3  LARGEURS DE L1-k A RECALCULER (machine 2). Les largeurs d beta5 =
  0.0463 et d beta7 = 0.0233 viennent des courbures du modele quadratique
  PROJETE. Apres M10, elles doivent etre recalculees sur le jackknife
  REELLEMENT mesure (L1-j) avant que la table de L1-k serve, sans quoi la
  table comparerait des ecarts mesures a des largeurs predites.

C31-4  L1-k ET LE GEL M10 (machine 2). L1-k a besoin de c5 et c7. Le gel M10
  interdit qu'"aucune forme non lineaire ne soit ajustee" : l'interdiction
  porte sur la DETERMINATION DE beta dans le protocole de fit, non sur une
  consignation posterieure. Les courbures restent calculables depuis la carte,
  HORS protocole et etiquetees comme telles. Dit explicitement pour que L1-k
  ne soit pas lu comme une violation du gel M10.

## 31.5 REGISTRE DES ATTENTES -- OPPOSABLE, NON REECRIT

  v1 : F dans [-0.2, +0.6] ; Z dans [0.80, 0.95]
  v2 : projection sur grille reelle F = +0.6825, Z = +0.7531 (DEFAVORABLE a v1)
  v3 : etendue de F dans [0.15, 0.45] ; de Z dans [0.04, 0.12] ;
       une etendue de F sous 0.10 serait contre machine 1
  v4 : pre-chiffrage machine 2, etendue F = 0.1728 (dans la fourchette),
       etendue Z = 0.0113 (SOUS la fourchette d'un facteur 4)
  L1-i : rho(res5, res7) > +0.5 attendu sur les onze points
  L1-d(ii) : traversee N = 1 vers w2 ~ 5.9 (p=5) et ~ 4.0 (p=7) --
       HORS PORTEE de M10, a verser au dossier bord droit / Chirikov

Aucune de ces attentes n'a ete reecrite apres l'arrivee d'un element
defavorable. Deux l'ont ete apres coup en ETIQUETANT une seconde attente a
cote de la premiere -- c'est la conduite arretee au R-L1-4 et elle a tenu
quatre fois.

## 31.6 CE QUI RESTE, ET QUAND

  a la sortie de M10 : L1-a (F, Z) ; L1-g (carte de zeta point par point) ;
                       L1-i (rho) ; L1-j (jackknife) ; L1-k (apres C31-3)
  a la sortie de p=4 : L1-h -- LE SEUL TEST DE LA CLASSE
  jamais par M10     : L1-d (ii)

Etat reel a la cloture : M10 mesurera (F, Z) et la carte de zeta, mais ne
pourra PAS tester la classe -- deux degres font un systeme exactement
determine. La formulation juste n'est pas "M10 manque de puissance" mais
"M10 ne peut pas tester la classe".

## 31.7 PAIRES nom <-> sha256 (E19-3)

  lecture_L1_prereg_v1.md  93c2426259da8b706bc5033278c91e03e5bf9f45c5650947fdcf225866fa4859
  check_L1.py              4a1130a28f215730a2358a8fb369a0d4f980f1258d885d1d1e39dee93f752c1e
  lecture_L1_prereg_v2.md  34c8fc3c913bfb27e418ead73bc18abf4deffcf36a3b0056de7ce133637377e4
  L1v2_travaux.py          608b7d8e9d2d7f69bf3d0608c3080eaad42898a14a7c273a3e9547297315563a
  lecture_L1_prereg_v3.md  4d70db89e014b7c2fe95ed07ddd542f4a6d6da6ea72847056f7c9d85c11a3cf3
  L1v3_quantification.py   b5ade55babeac0a856724a201be584655b7efcf62a89874e1033d9db605e4479
  lecture_L1_prereg_v4.md  dbe633e206810e3d2226a845ed61d044ca0304eb1bd330ffc49824a72dc79fd8
  L1v4_travaux.py          1496007ca60a203c75f810229a1c86244f3c6df8bde8742461720efef61952cb
  cloture_L1_verif.py      [empreinte donnee au message]
  journal_delta_31_L1.md   [empreinte donnee au message]
  audit_L1_machine2.py     32a49481199984767a66be421b762a1121e9cbf0e7d1a075b3e6e2822b98b7cc
  audit_L1v2_machine2.py   438072a16b9a23255f8fe726d1f3c2a855bf891645ef38b8339747b066dc59f2
  audit_L1v3_machine2.py   86e0589b3a99afa51b5e7b4a40ecf4b6034a44fb1b7ceaf3b357aa9020af97ac
  audit_L1v4_machine2.py   db0b7a21e17c5630f35a19bf9da709fa24d1de26d2a82575fa3b3a872b740644

=== FIN DU DELTA 31 ===
