# GEL -- QUALIFICATION DE L'ESTIMATEUR E-B (Gamma_LS) -- v2
# Banc de qualification, CLASSE 2 -- plume machine 1 -- 11/11/2026
# Piste (0) de la branche quantique, etape 1. Ce n'est PAS une manche.

## 0. Statut

Gel court d'un banc de qualification d'instrument, a la forme des bancs
du delta 85. Une machine ecrit (m1), l'autre certifie et joue (m2,
BOCAL4). Aucune prediction de physique nouvelle : la seule question est
celle de l'instrument. Regle E19 : aucun run avant certification croisee
du gel ET de la sonde. Un seul tour de correction est admis (section 12).
Le numero de version est dans le nom ; l'empreinte est la convention B
du FICHIER ENTIER, de la premiere ligne au saut de ligne final apres le
terminateur -- "titre a terminateur" ne designait rien d'autre (M-4).
v2 = v1 (8603af9d4f63e9dc) + les hunks de la section 15 : c'est LE tour
de correction de la section 12.

## 1. Question et perimetre

QUESTION. La largeur Gamma_LS que la manche M17 a lue est-elle une
largeur SORTANTE INTRINSEQUE -- independante de la force, de la forme,
de la longueur et de la position de l'absorbeur -- ou depend-elle de la
facon d'absorber ?

CE QUE LA QUESTION N'EST PAS. Elle n'est pas "le hamiltonien est-il
essentiellement auto-adjoint". L'explosion classique en temps fini le
rend douteux (heuristique en deux dimensions, pas theoreme), mais ce
doute ne tue pas une largeur sortante : l'oscillateur cubique est dans
le meme cas et ses resonances sont definies. QUALIFIE voudra dire
"largeur sortante stable sous les variations jouees", rien sur
l'unitarite ni sur les extensions auto-adjointes.

PERIMETRE. Les six points f070 du run M17 (p = 5, canal (2,1), w2 =
1.95, 1.97, 1.98, 2.02, 2.03, 2.05, fraction 0.70), memes w2, g, s et
graine, lus dans les fichiers du run authentifies. Rien d'autre.

## 2. Sources (convention B, 16 hex ; octets du registre)

  moteur    scripts/m17_chaine_v17.py              82a0be882568fe0c  103150 o
  gel M17   gels/m17_pre_enregistrement_quantique_v12_b2.md
                                                    20950e52e7d63225   58507 o
  run M17   dossier manche_m17_v17, manifeste m2    4aecd0e2b23bc818  36 pieces
            (35 des 36 pieces ne sont PAS au registre : detention m2,
             recues par m1 le 11/11 et authentifiees 36/36)
  etape 0   lecture pre-declaree                    20cbc762d58ce1ca
            note de lecture                         2d246b2a5c60c244
            JSON v2                                 37169cd7d595c575
            lot m1                                  94c3749c83d4b044
  registre  lbaaz/SG_1, HEAD 2ec6775, plafond 93 (clone frais du 11/11)
  externe   Riss et Meyer, J. Phys. B 26 (1993) 4503 (trajectoires en eta
            d'un absorbeur complexe en base finie) ; Caliceti, Graffi,
            Maioli (resonances de l'oscillateur cubique).

Le lot de l'etape 0 n'etait pas detenu par m2 au 11/11 (M-3) : il est
JOINT au lot de ce gel. Tout nombre que ce gel en tire se relit dans
les six pieces f070 du run, sans lui.

Ce que l'etape 0 a etabli et que ce gel prend pour acquis : aux six
points, les portes du gel M17 (translation de p couches, N + p) et les
deux derniers pas de descente sont sous tau_LS = 0.05 ; l'etendue de
Gamma_LS sur la grille est ln(2.6614e-09 / 6.5625e-11) = 3.7027. Ce
qu'elle n'a pas pu dire est l'objet de ce gel.

## 3. Choix geles

3.1 MOTEUR. Le moteur depose est charge en LECTURE SEULE ; son chemin
est un argument de la sonde, jamais une constante ; son canon est
verifie avant tout calcul. La sonde n'emprunte que H_2D,
graine_coherente et indexation. Elle ne reecrit aucun element de
matrice.

3.2 PARAMETRES PAR POINT. Lus dans pt_*_f070.json : w2 (Fraction), g,
graine.s, EB.r_c (note r0 : 40 a gauche, 41 a droite), EB.eta (note
eta0 = |w2 - 2|), et la valeur lue par P6, EB.Gamma_LS.H.Gamma_LS
(notee G_run).

3.3 PARTIE HERMITIENNE. H0 = H_2D(N, w2, g, signe, "x5", eta = 0.0,
r_c = None) du moteur. Le hamiltonien absorbe est H(eta) = H0 - i eta
diag(W), W dependant de la forme.

3.4 FORMES D'ABSORBEUR (a, b = occupations des modes 1 et 2) :
  F1 (native) : W = (max(a, b) - r_c)^2 si max(a, b) > r_c, 0 sinon.
  F2 (exposant) : W = (max(a, b) - r_c)^4 / L^2 si max(a, b) > r_c
       (meme valeur que F1 a la distance L, c'est-a-dire a l'indice N,
        HORS boite ; sur la derniere ligne reelle, distance L - 1, le
        rapport F2 / F1 vaut (L - 1)^2 / L^2 ; autre profil).
  F3 (coordonnee) : rho = max(a, 2 b) ; W = (rho - r_c)^2 si rho > r_c
       (bord aligne sur le canal (2,1) : l'absorption commence a
        b = r_c / 2 au lieu de r_c).

3.5 GEOMETRIES (L = N - r_c) :
  G20 : r_c = r0,      N = r0 + 20   (celle du run)
  G30 : r_c = r0,      N = r0 + 30   (absorbeur allonge)
  GT  : r_c = r0 + 10, N = r0 + 30   (bord translate de 10, L = 20)

3.6 ECHELLE EN eta. eta_k = eta0 * 2^(-k), k = -2, -1, 0, ..., 12 :
quinze valeurs, quatre decades et un quart. Les quatre valeurs du run
sont k = 0, 1, 2, 3. La multiplication par une puissance de deux est
exacte : eta se porte en cette seule forme.

3.7 ETAT D'ANCRAGE. A k = 3, l'etat retenu est celui du moteur : plus
grand recouvrement hermitien |<v|psi>|^2 avec la graine, vecteur propre
droit norme L2, meme regle de depart que gamma_LS (lexsort sur la
partie reelle). gamma = -2 Im(E).

3.8 SUIVI PAR CONTINUITE. De k a k + 1 (et de k a k - 1), l'etat suivi
est celui de plus grand |<v'|v>| avec l'etat suivi au pas precedent
(vecteurs normes L2, espace entier). Si ce maximum est < 0.90 : SUIVI
PERDU de ce cote ; la trajectoire s'arrete la. Le suivi ne se fait
JAMAIS par recouvrement avec la graine en dehors de k = 3.

3.9 IDENTITE ENTRE CONFIGURATIONS. L'etat d'ancrage d'une configuration
(G30, GT, F2, F3) est compare a celui de (F1, G20) par leur
recouvrement hermitien restreint au bloc interieur max(a, b) <= r0,
chaque restriction renormee. S'il est < 0.90 : IDENTITE NON ETABLIE, la
configuration est NON LISIBLE a ce point.

3.10 VALEUR LISIBLE. Une valeur gamma_k est LISIBLE si elle est suivie
et si gamma_k > 1e-12. Provenance du plancher : dix fois le plus grand
|Gamma(H+)| du run (7.550e-14), arrondi a la decade superieure.

3.11 PLATEAU. Une FENETRE est une suite de cinq valeurs LISIBLES a k
consecutifs (quatre divisions par deux, un facteur 16 en eta). Il y a
PLATEAU si une fenetre verifie, EN RATIONNELS EXACTS,
    Fraction(max) <= (1 + Fraction(1, 20)) * Fraction(min)
(regle 15 ; E-EB-1 : la forme max / min - 1 <= 0.05 est fausse en
flottants a la borne meme). L'ETALEMENT e = max(gamma) / min(gamma) - 1
n'est plus qu'un affichage. La fenetre retenue est celle de plus petit
rapport max / min, compare lui aussi en rationnels ; a egalite, le plus
petit k de depart. Gamma_pl est la moyenne
geometrique des cinq valeurs de la fenetre retenue. Le meilleur
etalement est CONSIGNE meme sans plateau.

3.12 ACCORD entre deux valeurs de plateau : |ln(Gamma_a / Gamma_b)|
<= tau. Comparaison en flottants : une borne de logarithme n'a pas de
forme exacte ; elle se teste a tau - 1e-6 et a tau + 1e-6 (G-Q7), pas
a la borne.

## 4. Tolerances (aucune n'est fixee apres lecture)

  tau = 0.05 : c'est tau_LS du gel M17 (aout), reprise telle quelle
        pour l'etalement d'une fenetre ET pour tout accord. Elle est
        plus dure ici qu'au gel M17 : elle borne l'etalement de cinq
        valeurs, pas un pas.
  0.90 : seuil de suivi et d'identite.
  1e-12 : plancher de lisibilite (3.10).
  tau_TP = tau + u_ref : accord au temoin positif (5.1).
Ce que la plume a vu avant d'ecrire : les trois pas de descente du run
par point (k = 0 a 3, quatre valeurs). Une fenetre demande cinq
valeurs : aucune issue de ce gel n'est calculable sur ce qui a ete vu.
Vu DEPUIS le v1 (note m2 0d11d6866e3c5f37) : un essai de formule de m2
a UN point de l'echelle du TP, g_8 = 0.10, largeur 6.428e-09 par
rotation complexe. Ce n'est pas la reference et aucune valeur de la
sonde n'existe ; la plume connait donc l'ordre de grandeur a ce g.
Si le temoin positif lui-meme ne tient pas tau, le banc rend NON
CONCLUANT D'INSTRUMENT et NE LIT PAS le fantome ; tau ne se desserre
pas sur les donnees du fantome.

## 5. Temoins

5.1 TEMOIN POSITIF (TP) -- une largeur dont la valeur est connue par
une autre methode. Systeme : le jumeau H+ du moteur (signe_fantome =
+1, potentiel "x5"), w2 = 39/20, p = 5. Etat : celui de plus grand
recouvrement hermitien avec le vide de Fock |0, 0>.
  Echelle de couplage : g_j = 0.05 * 2^(j/8), j = 0, ..., 16 (de 0.05 a
  0.20).
  REFERENCE, a la plume de m2, par ROTATION COMPLEXE (aucun absorbeur) :
    H(theta) = somme_i w_i [cos(2 theta) n_i
                            + (i/2) sin(2 theta) (a_i^2 + a_i^+2)]
               + (1/2)(w1 + w2)(cos(2 theta) - 1)
               + exp(5 i theta) (g/5) x^5
    (le moteur ecrit H sans energie de point zero ; x et les n_i sont
     ceux du moteur). Formule A RE-DERIVER par m2 ; une erreur ici est
     un defaut de ce gel.
    theta dans {0.10, 0.15, 0.20, 0.25, 0.30} rad (tous < pi/7),
    N dans {50, 60, 70}. Gamma_ref = valeur au theta de plus petite
    variation, au plus grand N ; u_ref = plus grand ecart relatif de
    Gamma sur les trois theta centraux et les deux plus grands N.
  RETENUS : parmi les g_j dont Gamma_ref est dans [1e-11, 1e-7] avec
    u_ref <= 0.01, les deux dont ln(Gamma_ref) est le plus proche de
    ln(1e-10) et de ln(1e-8). La selection ne lit QUE la reference.
    Zero retenu : TP NON CONCLUANT.
  MESURE par la sonde, forme F1, r_c = 40, G20 et G30, eta0 = 0.05,
    meme echelle, meme plateau.
  TP TIENT si, a chaque g retenu : PLATEAU a G20 et a G30, et
    |ln(Gamma_pl / Gamma_ref)| <= tau_TP aux deux.
  INTERFACE (precision du v2). Le script de reference ecrit deux
  fichiers : la LISTE des couplages retenus (j, g), sans aucune
  largeur, et la table des references. La sonde ne lit que la liste ;
  la feuille de lecture seule ouvre la table et fait la comparaison.
  Aucun des deux scripts de mesure ne lit une largeur de l'autre.
  Estimation de plume, NON OPPOSABLE (WKB 1D le long de q1 + q2, script
  estimation_TP_wkb_machine1_v1.py joint) : sept des dix-sept g_j, de
  j = 5 a j = 11 (g de 0.077 a 0.130), tombent dans la fenetre. Une
  premiere estimation faite de tete la placait a g entre 0.2 et 0.45 :
  fausse d'un facteur trois, corrigee avant le gel par le calcul.
  L'essai de formule de m2 a g_8 = 0.10 rend 6.428e-09 la ou ce WKB
  rend 1.46e-09 : un facteur 4.4. La fenetre WKB se lit comme un ordre
  de grandeur ; la selection se fait sur la reference seule.

5.2 TEMOIN NEGATIF (TN) -- un etat qui DOIT echouer. Au point 1.95,
(F1, G20) : l'etat de plus grand recouvrement hermitien avec l'etat de
Fock |a = r0 + 10, b = (r0 + 10) // 2>, loge dans l'absorbeur sur le
canal ; suivi sur l'echelle. Attendu : PAS DE PLATEAU (gamma
proportionnelle a eta). S'il est non lisible, on lit le candidat a + 5
puis a - 5 (b = a // 2 a chaque fois) ; trois non lisibles : TN NON
JOUE, consigne au verdict. Les trois candidats sont suivis dans les
MEMES quinze decompositions, jouees a l'etage 1 et propres au TN :
aucune valeur de l'etat d'ile n'y est relevee.
  TN rend PLATEAU : le critere ne mord pas -> NON CONCLUANT
  D'INSTRUMENT.

5.3 PLANCHER. A chaque (point, configuration), k = 3 : Gamma du jumeau
H+ a l'etat de plus grand recouvrement avec la graine. Toutes doivent
verifier |Gamma(H+)| <= 1e-12 ; sinon le plancher 3.10 est faux.

## 6. Epreuves par point

  (a) PLATEAU a (F1, G20) ET a (F1, G30).
  (b) ACCORD de Gamma_pl entre G20 et G30.
  (c) PLATEAU sous F2 et sous F3 a G20, chacun en ACCORD avec
      (F1, G20).
  (d) PLATEAU a (F1, GT), en ACCORD avec (F1, G20).
  (e) CONSIGNE, pas une condition : |ln(G_run / Gamma_pl(F1, G20))|
      <= tau. Sinon : "M17 a lu hors plateau a ce point".
Statut du point :
  QUALIFIE      : (a), (b), (c), (d) tiennent.
  NON QUALIFIE  : l'une echoue sur des valeurs lisibles (une
                  configuration a au moins une fenetre et aucune sous
                  tau, ou un accord echoue).
  NON LISIBLE   : une configuration requise n'a aucune fenetre (suivi
                  perdu, plancher) ou son identite n'est pas etablie,
                  et aucune epreuve n'echoue par ailleurs.

## 7. Lecture des etats voisins (T-etats) -- SANS effet sur le verdict

A (F1, G20), pour les K = 10 etats de plus grand recouvrement hermitien
avec la graine a k = 3 : suivi, plateau, Gamma_pl ; poids bi-orthogonal
c_nu = (v_nu^T psi)^2 / (v_nu^T v_nu) (sans conjugaison : H est
complexe symetrique, psi reelle) ; conditionnement kappa_nu =
(v_nu^+ v_nu) / |v_nu^T v_nu|. Controle : la somme des c_nu sur TOUS
les etats vaut 1 ; si |somme - 1| > 1e-6 : DECOMPOSITION MAL
CONDITIONNEE, T-etats non lu a ce point.
  S_w = max - min de ln(Gamma_pl) sur ceux des K etats qui ont un
  plateau (au moins trois, sinon non lu). med = mediane des S_w lus.
  Lecture, contre E_run = 3.7027 :
    med >= E_run : FLUCTUATION D'ETAT DOMINANTE -- l'etendue de la
        grille de M17 est dans la dispersion d'un etat a l'autre ; un
        test de rang sur un etat par point n'a pas de sens.
    med <  E_run : STRUCTURE DE GRILLE DOMINANTE -- le pic est un fait
        du point.
La largeur ponderee du gel M17 n'est PAS relue : l'etape 0 a montre
qu'elle vaut 5e+03 a 5e+06 fois Gamma_LS, c'est un autre objet.

## 8. Gardes (enumerees ; chaque log dit ce qu'il ne joue pas)

  G-Q1  canon du moteur == 82a0be882568fe0c.
  G-Q2  dossier du run : les 36 LIGNES DU MANIFESTE au canon et a la
        taille == 36. Le compte se fait par le manifeste, jamais par les
        fichiers du dossier ; tout fichier hors manifeste est nomme au
        log, ni ouvert ni compte (M-2 : le dossier de BOCAL4 en a un).
  G-Q3  IDENTITE DE FORME : H0 - i eta diag(W_F1) == H_2D(eta, r_c) du
        moteur, element par element, a chaque (point, G20, k = 3).
  G-Q4  ANCRAGE : |gamma(F1, G20, k = 3) / G_run - 1| <= 1e-3
        (resolution d'instrument du delta 80). L'egalite au bit est
        CONSIGNEE : attendue sur BOCAL4 a plateforme inchangee depuis
        le run, non exigee. Jouee a l'OUVERTURE de l'etage 2 : les six
        decompositions (F1, G20, k = 3) passent avant toute autre.
  G-Q5  PLANCHER (5.3).
  G-Q6  echelle exacte : eta_k * 2^k == eta0.
  G-Q7  selftest de la routine de plateau sur series synthetiques :
        gamma = c eta -> PAS DE PLATEAU ; constante -> PLATEAU ; plateau
        de cinq puis chute lineaire -> PLATEAU, fenetre nommee ; quatre
        valeurs lisibles seulement -> AUCUNE FENETRE. BORNE, a un ulp de
        part et d'autre, sur des valeurs exactement representables :
        (20.0, 20.25, 20.5, 20.75, 21.0) -> PLATEAU ; la meme avec
        nextafter(21.0, +inf) -> PAS DE PLATEAU. ACCORD et accord au
        TP : |ln| = tau - 1e-6 -> ACCORD ; tau + 1e-6 -> PAS D'ACCORD.
  G-Q8  TP (5.1).   G-Q9  TN (5.2).
  G-Q10 comptes, sous la forme joues + sautes == attendus, par famille.
Decompositions attendues (declarees avant de compter), par famille :
trajectoires F1 180 (6 x 2 x 15), formes 180 (6 x 2 x 15), translation
90 (6 x 15), plancher 30 (6 x 5), TP au plus 60 (2 x 2 x 15), TN 15
(E-EB-2 ; un seul jeu de quinze pour les trois candidats, 5.2) : au
plus 555. Hors de ce compte, et declarees comme telles : les
decompositions a geometrie reduite du banc qui tue, et celles du script
de reference de m2.

## 9. Verdict -- cascade ordonnee, premier match l'emporte

  1. NON CONCLUANT D'INSTRUMENT : G-Q1 a G-Q7 ou G-Q10 mord ; TP ne
     tient pas ou est non concluant ; TN rend PLATEAU. Le fantome n'est
     PAS lu : l'etage 2 n'est pas joue si l'etage 1 echoue, et il
     s'arrete a son ouverture si G-Q4 mord.
  2. ESTIMATEUR QUALIFIE : six points QUALIFIES.
  3. QUALIFIE PAR POINT : un a cinq points QUALIFIES ; la liste est le
     verdict. Toute phrase de grille (rang, pic, creux) est caduque.
  4. NON QUALIFIE : zero point QUALIFIE et au moins un NON QUALIFIE.
  5. NON LISIBLE : zero QUALIFIE, zero NON QUALIFIE.
Ordre d'execution : ETAGE 1 = selftest, banc qui tue, TP, TN, G-Q3,
G-Q5 ; la feuille de lecture ecrit le verdict de l'etage 1 ; ETAGE 2 =
les six points, ouvert par G-Q4, et seulement si ce verdict tient.
Reprise par fichier (point, configuration, k) obligatoire.

## 10. Banc qui tue (mutations ; chacune doit faire tomber ce qu'elle vise)

  M-1  gamma suivie remplacee par c eta -> tous les points NON QUALIFIES.
  M-2  Gamma_pl(G30) multipliee par 1.06 -> (b) echoue.
  M-3  reference du TP multipliee par 1.07 -> NON CONCLUANT
       D'INSTRUMENT.
  M-4  ancrage sur le DEUXIEME recouvrement -> G-Q4 mord.
  M-5  un element de W_F1 deplace d'une couche -> G-Q3 mord.
  M-6  seuil de suivi viole (vecteur remplace par un orthogonal) ->
       SUIVI PERDU, configuration NON LISIBLE.
Le banc affirme sa branche a chaque mutation et compte : mordues ==
attendues.

## 11. Annonces de la plume (aveugles ; a compter apres le run)

  A-1  verdict : QUALIFIE PAR POINT 0.5 ; ESTIMATEUR QUALIFIE 0.3 ;
       NON QUALIFIE 0.1 ; NON CONCLUANT D'INSTRUMENT 0.1.
  A-2  2.02 n'est pas QUALIFIE : 0.6 (le dernier pas du run y est plus
       grand que le precedent).
  A-3  la famille de droite (2.02, 2.03, 2.05) compte au moins autant
       de points QUALIFIES que celle de gauche : 0.65 (base propre
       presque orthogonale a droite, poids total 0.998 contre 0.85).
  A-4  T-etats : FLUCTUATION D'ETAT DOMINANTE : 0.7.
  A-5  kappa de l'etat retenu : plus petit des trois de gauche > plus
       grand des trois de droite : 0.6.

## 12. Contrat de script, cout, garde-fou

SONDE (m1) : elle MESURE et ne juge pas ; la FEUILLE DE LECTURE (m1)
juge et ne mesure pas (routine de plateau, statuts, cascade, G-Q7).
Sonde : arguments = moteur, dossier du run, manifeste, liste des
couplages retenus, sortie ;
ASCII ; ligne de plateforme avec temoin d'arrondi ; aucun ** de tableau
hors du moteur ; ordre de parcours declare ; sortie JSON + log, le log
porte son empreinte relue du disque.
REFERENCE TP (m2) : script independant, ne charge du moteur que H_2D a
eta = 0 pour le terme x^5, ou le reecrit.
COUT (estimation, loi cubique sur la mesure 93 a 94 s par
decomposition a N = 70 du delta 80) : etage 1 de l'ordre de 2 a 3 h,
reference comprise si m2 la balaie d'abord grossierement (un theta,
N = 50) avant de raffiner ; etage 2 environ 8 h 30 ; une nuit de BOCAL4.
REJEU m1, PERIMETRE DECLARE : selftest, banc qui tue, et le point 1.95
en (F1, G20) sur l'echelle entiere (15 decompositions), compare a
BOCAL4 a 1e-3, avec le levier NPY_DISABLE_CPU_FEATURES. Le reste n'est
pas rejoue par m1 : repetition non opposable.
GARDE-FOU (proposition de la plume, sous le veto de l'operateur) : un
gel, UN tour de correction,
un run, un acte. Si le TP ne qualifie pas l'instrument apres ce
tour, on l'ecrit et on s'arrete. Aucun rejeu des donnees du fantome sous
d'autres seuils.

## 13. Ce que chaque verdict engage

  ESTIMATEUR QUALIFIE : Gamma_LS est une largeur sortante, citable avec
      sa valeur et son etalement ; "PAS DE SIGNAL" de M17 reste, comme
      reponse a une question de rang. Suite PROPOSEE : le plancher en
      g (c de juillet) remesure avec cet instrument, puis sa
      derivation.
  QUALIFIE PAR POINT : seules les largeurs des points listes sont
      citables ; aucune phrase de grille.
  NON QUALIFIE : toute phrase portant un Gamma depuis juillet est
      reclassee ; reste le fait d'ordre de grandeur "le fantome fuit,
      le jumeau non", et seulement si le TP a tenu.
  NON CONCLUANT D'INSTRUMENT : rien n'est dit du fantome ; l'acte
      consigne le meilleur etalement atteint au TP.

## 14. Limites declarees

Un seul degre (p = 5), une seule resonance (2:1), une seule fraction
(0.70), six points. Deux formes de remplacement et une translation :
"independant de l'absorbeur" veut dire "sous ces variations". Double
precision, decomposition dense : les largeurs sous 1e-12 sont hors de
portee, donc l'axe g vers le bas aussi (P8 du run). Le suivi par
continuite peut se perdre a un croisement evite : c'est un fait du
point, rendu NON LISIBLE, pas un echec. Le TP qualifie la chaine de
calcul sur un systeme a barriere d'energie ; le fantome n'en a pas :
un TP tenu ne prouve pas que la methode vaut pour lui, il prouve
qu'elle sait mesurer une largeur connue.

## 15. Journal v1 -> v2 (certification m2 du 11/11, lot 113e5b84238203de)

m2 : NON CERTIFIE EN L'ETAT, 21 controles, 2 morsures de description,
quatre demandes. Tout est pris, sans reserve.
  E-EB-1  3.11 en rationnels exacts ; 3.12 dit sa comparaison ; G-Q7
          rebati a un ulp de la borne (H1, H2, H9).
  E-EB-2  le TN entre au decompte par famille ; total 555 et non 585 :
          les trois candidats partagent quinze decompositions (H6, H10).
  M-1     F2 : "a la distance L" (H4).
  M-2     G-Q2 compte par le manifeste (H7).
  M-3     lot de l'etape 0 joint (H12).
  M-4     canons confirmes -- gel v1 8603af9d4f63e9dc, WKB
          3eeb30328f9c542c ; "titre a terminateur" = convention B du
          fichier entier (H0). Faute de transit de la plume : deux
          pieces a plat sans manifeste ; le v2 part en lot.
De la plume, declares, hors demandes de m2 :
  P-1     interface du TP : la sonde ne lit que la liste des couplages
          retenus ; sonde = mesure, feuille de lecture = jugement
          (H5a, H13).
  P-2     G-Q4 a l'ouverture de l'etage 2 ; verdict de l'etage 1 ecrit
          par la feuille de lecture (H8, H11a, H11b).
  P-3     ce que la plume a vu depuis le v1 : l'essai de m2 a g_8
          (H3, H5b).
Aucune tolerance ne change ; aucun nombre mesure ne change ; le
decompte passe de 540 a 555. Formule de rotation complexe : re-derivee
et validee par m2, inchangee.

-- FIN --
