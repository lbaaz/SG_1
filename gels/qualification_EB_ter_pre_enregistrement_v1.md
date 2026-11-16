# GEL -- QUALIFICATION DE L'ESTIMATEUR E-B (Gamma_LS) -- TER, v1
# Banc de qualification, CLASSE 2 -- plume machine 1 -- 15/11/2026
# Piste (0) de la branche quantique, reprise sous absorbeur long. Ce n'est PAS une manche, et ce
# n'est PAS une relecture de la nuit bis.

## 0. Statut

Gel d'un banc de qualification d'instrument, a la forme des gels cde0cd11a763f26d et
dcda1611adf5f8fd. Une machine ecrit (m1), l'autre certifie et joue (m2, BOCAL4). Regle E19 : aucun
run avant certification croisee du gel, de la sonde ET de la feuille. Un seul tour de correction
est admis (section 12). L'empreinte est la convention B du FICHIER ENTIER.
C'est le TROISIEME gel de la piste (0). Le gel bis ecrivait "DERNIER ESSAI", "ni troisieme gel, ni
autre echelle, ni autre temoin", "L'operateur peut lever ce garde-fou ; les machines, non".
L'operateur l'a leve en deux temps, selon sa conversation avec machine 1 : "ouvre" (15/11/2026,
08 h 38), pour un calcul hors chaine ; puis "go" (15/11/2026, 10 h 28), au vu de la note hors
chaine 42c822811167b826 (lot 4103eae43f989877), pour ce gel. Ce sont des declarations de machine 1 ;
l'operateur les atteste, ou non, a machine 2 avant le run.
Le verdict de la nuit bis (delta 95, NON QUALIFIE) reste ce qu'il est, sous son gel. Ce gel-ci
pose la meme question a d'autres absorbeurs, par un autre instrument, sur d'autres points : trois
differences de fond, dites en section 15.

## 1. Question et perimetre

QUESTION, celle du gel bis : "La largeur Gamma_LS que la manche M17 a lue est-elle une largeur
SORTANTE INTRINSEQUE -- independante de la force, de la forme, de la longueur et de la position de
l'absorbeur -- ou depend-elle de la facon d'absorber ?", posee ici aux largeurs que la sonde du
delta 98 a lues a la facon de M17 (k = 3, F1, 20 couches) aux douze points juges de ce delta.

CE QUE LA QUESTION N'EST PAS. Elle n'est pas "le hamiltonien est-il essentiellement
auto-adjoint". QUALIFIE voudra dire "largeur sortante stable sous les variations jouees", rien sur
l'unitarite, ni sur les extensions auto-adjointes, ni sur la dynamique du systeme ferme.

PERIMETRE. Les douze points juges du delta 98 (p = 5, canal (2,1), fraction 0.70), aux memes w2,
g, r_c et eta0, lus dans la sortie deposee de la sonde de ce delta (10887c60d5f55bcf). A chaque
point, les etats de cette sortie dont la largeur deposee a k = 3 depasse dix planchers de la
decomposition dense (1.33e-12) : 137 etats. Rien d'autre.

  point  w2        facteur  r_c  etats juges   N sous A, B, C, D
  C1     197/100   2/3       53   8            133, 153, 153, 143
  C2     97/50     3/4       48  11            128, 148, 148, 138
  C3     203/100   3/2       35  14            115, 135, 135, 125
  C4     103/50    4/3       36  13            116, 136, 136, 126
  M1     193/100   1/1       40  12            120, 140, 140, 130
  M2     48/25     4/3       35  14            115, 135, 135, 125
  M3     207/100   2/3       54   8            134, 154, 154, 144
  M4     21/10     3/4       49   9            129, 149, 149, 139
  L1     189/100   4/3       34  14            114, 134, 134, 124
  L2     47/25     1/1       40  11            120, 140, 140, 130
  L3     211/100   3/2       35  14            115, 135, 135, 125
  L4     53/25     2/3       54   9            134, 154, 154, 144

## 2. Sources (convention B, 16 hex)

  Au registre lbaaz/SG_1, HEAD 8d54bf9, plafond 98 (releve du 15/11)
    dcda1611adf5f8fd  gels/qualification_EB_bis_pre_enregistrement_v1.md
        le gel bis, JOUE (delta 95)
    bdf8c5a0c73096a4  journal/journal_delta_95_qualification_EB_bis_v2.md
        l'acte 95 : NON QUALIFIE
    82a0be882568fe0c  scripts/m17_chaine_v17.py
        le moteur
    10887c60d5f55bcf  journal/sonde_ordre2.json
        la sortie deposee de la sonde du delta 98 : points, etats, G_dep
    c2f3e5c9102dc1a7  journal/journal_delta_98_ordre2_chaine_EA_v1.md
        l'acte 98
    69b3bab3bb8480b7  journal/tp_retenus_machine2_v1.json
        les couplages retenus du temoin, j = 6 et j = 8
    4d51dd58ef456fe9  journal/tp_reference_machine2_v1.json
        la table de reference du temoin (machine 2)
    c110c6286157b025  journal/lot_a01598ec24237921__sonde_etage2.json
        la sortie de la sonde dense, nuit bis
    5d80bf2edd26a6c1  journal/sonde_chaine_par_etat.json
        la sortie deposee du delta 96 (points de reglage J1, J2, J3, J5)
    d51a9c6ce98b0452  journal/sonde_domaine_G1.json
        la sortie deposee du delta 97 (points de reglage E4, H1)
  Hors registre, lot de machine 1 du 15/11 (4103eae43f989877), remis a l'operateur
    42c822811167b826  note_machine1_piste0_reprise_absorbeur_long_2026-11-15_v1.md
        la note hors chaine (classe 3, post hoc) : ce que la plume a vu aux six points de M17
  Externe : Riss et Meyer, J. Phys. B 26 (1993) 4503 (trajectoires en eta d'un absorbeur complexe
  en base finie).

## 3. Choix geles

3.1 MOTEUR. Le moteur depose est charge en LECTURE SEULE ; son chemin est un argument ; son canon
est verifie avant tout calcul. Le lecteur n'emprunte que X_saut_reel, P et W1. Il ne reecrit aucun
element de matrice : il assemble, element par element, la matrice que H_2D du moteur assemble
(memes boucles, meme demi-espace de sauts), sous forme creuse.

3.2 PARAMETRES. Lus dans la sortie deposee 10887c60d5f55bcf : par point, w2 (Fraction), g, r_c, eta0
(= |w2 - 2|) ; par etat, le rang, l'etiquette entiere (n1, n2), l'energie reelle a k = 3 (E_dep)
et la largeur deposee a k = 3 (G_dep), lue par la sonde dense du delta 98 sous F1 a 20 couches.

3.3 LE LECTEUR (bloc 9b0f95f3e10e9b0d, insere tel quel dans la sonde). H(eta) = H0 - i eta diag(W),
H0 la partie hermitienne du moteur. Pour un etat d'etiquette (n1, n2) et une energie cible E
reelle : factorisation creuse de H(eta) - E (scipy.sparse.linalg.splu, ordre MMD_ATA), puis
iteration inverse : x <- solution de (H(eta) - E) y = x, normee ; lambda = <x|H(eta)|x> ; residu
||H(eta) x - lambda x||. Au moins 2 iterations, au plus 12 ; arret quand le residu ne depasse pas
1e-11 fois max(1, |lambda|). Aucun tirage aleatoire.
LARGEUR : Gamma = 2 eta <x|W|x>, x norme. C'est -2 Im(lambda) quand x est vecteur propre droit et
H0 hermitien ; -2 Im(lambda) est consignee a cote et n'est pas la valeur jugee.

3.4 ABSORBEURS (a, b = occupations des modes 1 et 2 ; r = max(a, b) ; bord B ; L couches ; boite
N = B + L) :
  F1 : W = (r - B)^2 si r > B, 0 sinon.            (la forme native du moteur)
  F2 : W = (r - B)^4 / L^2 si r > B, 0 sinon.      (la forme F2 du gel bis)
  A : F2, B = r_c,      L = 80   -- REFERENCE
  B : F2, B = r_c,      L = 100  -- longueur
  C : F1, B = r_c,      L = 100  -- forme
  D : F2, B = r_c + 10, L = 80   -- position
F2 depend de L par sa norme : de A a B changent la longueur ET, a distance egale du bord, la force
(d'un facteur 16/25) ; l'echelle en eta couvre ce facteur. C differe de A par la forme ET par la
longueur : F1 est jouee a la longueur ou elle a un plateau aux points de reglage (section 4). La
forme F3 du gel bis n'est PAS jouee (section 14).

3.5 ECHELLE EN eta. eta_k = eta0 * 2^(-k), k = -3, -2, ..., 8 : douze valeurs, un facteur 2048.
ORDRE DE PARCOURS : k = 3, puis 4 a 8, puis 2, 1, 0, -1, -2, -3.

3.6 DEPART ET SUIVI. A k = 3 : energie cible E_dep, vecteur de depart le site de Fock (n1, n2).
A chaque autre barreau : energie cible et vecteur de depart ceux du barreau voisin deja lu, s'il
est SUIVI ; sinon ceux du dernier barreau suivi de la serie, ou a defaut ceux du depart.
Un barreau est SUIVI si le residu final ne depasse pas 1e-11 fois max(1, |lambda|) ET si le poids
du vecteur au site de l'etiquette, |x(n1, n2)|^2, vaut au moins 0.5.

3.7 VALEUR LISIBLE. Une valeur Gamma_k est LISIBLE si elle est suivie, finie et strictement
positive. Il n'y a PAS de plancher de lisibilite : le plancher des gels precedents (1e-12) etait
celui de la decomposition dense, et le lecteur ne passe pas par elle (section 4, (iv)). Le
plancher du depot, lui, borne les etats juges (section 1) et la tolerance de l'etage 0.

3.8 PLATEAU (regle 3.11 du gel bis, inchangee). Une FENETRE est une suite de cinq valeurs LISIBLES
a k consecutifs (un facteur 16 en eta). Il y a PLATEAU si une fenetre verifie, EN RATIONNELS
EXACTS, Fraction(max) <= (1 + Fraction(1, 20)) * Fraction(min). La fenetre retenue est celle de
plus petit rapport max / min, compare en rationnels ; a egalite, le plus petit k de depart.
Gamma_pl est la moyenne geometrique des cinq valeurs de la fenetre retenue. L'ETALEMENT
max / min - 1 est un affichage. Sur l'echelle de ce gel, huit fenetres, de k0 = -3 a k0 = 4.

3.9 ACCORD (regle 3.12 du gel bis, inchangee) entre deux valeurs de plateau :
|ln(Gamma_a / Gamma_b)| <= tau, en flottants, teste a tau - 1e-6 et a tau + 1e-6, pas a la borne.

## 4. Tolerances, et ce que la plume a vu (aucune tolerance n'est fixee apres lecture)

  tau = 0.05 : celle du gel bis, elle-meme tau_LS du gel M17. Ni desserree ni resserree, pour
        l'etalement d'une fenetre ET pour tout accord.
  0.5 : poids au site, pour le suivi. 1e-11 : residu.
  tau_TP = tau + u_ref : accord au temoin positif (6.1).
  ETAGE 0 : |Gamma_lue - G_dep| <= 1e-3 G_dep + 1e-12. Le 1e-3 est la tolerance du rejeu entre
        machines du gel bis (section 12) ; le 1e-12 est son plancher de lisibilite (3.10).
  ANCRES : |ln(Gamma_m2 / Gamma_m1)| <= 1e-6 (5.2).
  9/10 : part des etats (section 8).
Ce que la plume a vu avant d'ecrire, et qui fait de ce gel un gel REGLE sur des points deja joues :
  (i)   aux six points f070 de M17, l'etat lu sous vingt absorbeurs, k = -5 a 14 (la note
        42c822811167b826) : sous F2 a 60 et 80 couches, F1 a 80, F3 a 60 et F1 translate de 10
        a 60, la regle 3.8 rend PLATEAU aux six points, pire etalement 0.0152 ; les
        cinq valeurs de plateau s'accordent a 0.0070 pres au pire.
  (ii)  a huit points des deltas 96, 97 et 98 qui ne sont PAS des points juges de ce gel (A1, A2,
        J1, J2, J3, J5, E4, H1 ; |delta| de 0.05 a 0.12, facteurs 2/3, 1 et 3/2, r_c de 34 a
        54), sous les quatre absorbeurs et sur l'echelle de ce gel, par le bloc de ce gel, juges
        par la feuille de ce gel. Etats lus, parmi ceux au-dessus de dix planchers :
        E4 tous (14), J2 rangs 0 a 6 (7 sur 13), H1 rangs 0 a 3 (3 sur 8),
        A2 rangs 0 a 2 (3 sur 12), A1 rangs 0 a 2 (3 sur 12), J1 rangs 0 a 2 (3 sur 11),
        J3 rangs 0 a 2 (3 sur 13), J5 rangs 0 a 2 (2 sur 8) ;
        38 etats :
        35 QUALIFIES, 3 NON QUALIFIES, 0 NON LISIBLES ; etat lu QUALIFIE a 8 points sur 8 ;
        par point (QUALIFIES / juges) : A1 3/3, A2 3/3, J1 3/3, J2 7/7,
        J3 3/3, J5 2/2, E4 11/14, H1 3/3 ;
        etalement de la meilleure fenetre sous A : mediane 0.0069, plus grand 0.0409 ;
        etalement de la meilleure fenetre sous B : mediane 0.0024, plus grand 0.0442 ;
        etalement de la meilleure fenetre sous C : mediane 0.0116, plus grand 0.0657 ;
        etalement de la meilleure fenetre sous D : mediane 0.0080, plus grand 0.0410 ;
        accord B / A, |ln| : mediane 0.0006, plus grand 0.0417 ;
        accord C / A, |ln| : mediane 0.0024, plus grand 0.0409 ;
        accord D / A, |ln| : mediane 0.0013, plus grand 0.0784 ;
        consigne (e), |ln(G_dep / Gamma_pl(A))| : mediane 0.0223, plus grand 0.1403 ; au-dessus de
        tau a 11 etats sur 38.
  (ii bis) le PREMIER JEU d'absorbeurs, celui que la plume avait d'abord retenu (F2 a 60 et 80
        couches, F1 a 80, F2 translate a 60), a six de ces points, 56 etats lus avant
        l'arret (A1 12, A2 12, J1 11, J2 13, J3 6, J5 2) : plus grand etalement
        de la meilleure fenetre 0.0249 sous F2 a 60 couches, 0.0123 sous F2 a 80,
        0.0421 sous F1 a 80 (J2 rang 7), 0.0284 sous F2 translate. Et, par un essai a part
        au point E4 : l'etat lu n'a pas de plateau sous F2 a 60 couches (meilleur etalement
        0.0506), et sa valeur sous F2 translate s'en ecarte de 0.0790 en logarithme.
        C'est ce qui a fait allonger chaque absorbeur de 20 couches. Ce reglage est fait sur des
        points de reglage, il est dit, et il est le dernier : les longueurs ne bougent plus.
  (iii) le temoin positif sous les quatre absorbeurs et le temoin negatif aux deux ancres, par la
        sonde de ce gel, sur le conteneur de machine 1 : le temoin positif a PLATEAU aux huit
        (couplage, absorbeur), pire |ln(Gamma_pl / Gamma_ref)| = 0.0007 ; le temoin negatif
        n'a de plateau nulle part : sa largeur se divise par deux a chaque barreau (a 0.002
        pres sur le rapport), et vaut 1e-52 a 2e-39 a k = 3.
  (iv)  le lecteur contre la sonde dense deposee : aux deux ancres, 84 lectures (14 etats, k = 2,
        3, 4, F1 a 20 couches), pire ecart absolu 5.8e-13, pire ecart relatif au-dessus de
        mille planchers 2.9e-04 ; aucune hors de la tolerance de l'etage 0. Sa lecture jugee,
        2 eta <W>, concorde a 1.1e-12 pres en relatif, a l'etat lu de 1.98 sur vingt
        barreaux, avec celle du lecteur d'exploration de la note, qui est un autre algorithme.
        -2 Im(lambda), elle, est arrondie a quelques 1e-16 en absolu : sur les 1824
        lectures de (ii) elle s'ecarte de 2 eta <W> de 6e-04 au pire, aux plus petites
        largeurs. C'est pourquoi elle n'est pas la valeur jugee.
  (v)   AUX DOUZE POINTS JUGES : rien sous absorbeur long, ni par le lecteur, ni autrement. La
        plume y connait ce qui est depose : les largeurs de la sonde dense a k = 2, 3, 4 sous F1 a
        20 couches, et les chaines. Entre k = 2, 3 et 4, ces largeurs deposees s'ecartent de
        0.074 en mediane et de 0.221 au pire (max / min - 1, sur les 137
        etats juges) : la consigne (e) n'est donc pas acquise.
La tenue des etages 0 et 1 est ATTENDUE ; elle doit etre REFAITE par la sonde certifiee dans le
run juge, et son echec garde toute sa force. tau ne se desserre pas sur les donnees du fantome.

## 5. Etage 0 : l'instrument

5.1 LE LECTEUR CONTRE LA SONDE DENSE. Aux deux ancres A1 (39/20) et A2 (41/20) du depot, a la
geometrie deposee (F1, bord r_c, 20 couches), k = 2, 3, 4, pour les 14 etats de chaque ancre :
la largeur lue par le lecteur doit etre SUIVIE et verifier la tolerance de l'etage 0 contre la
largeur deposee au meme k. 84 lectures ; l'etage 0 TIENT si les 84 tiennent.

5.2 ANCRES REGLEES. Aux memes ancres, les etats de rang 0 et 1, sous les quatre absorbeurs et les
douze barreaux : 192 lectures, comparees a celles que la sonde a rendues sur le conteneur de
machine 1 (reference_ancres_ter_machine1_v1.json, 6600fb8418c79930). Elles TIENNENT si le statut
de suivi est le meme a chaque lecture et si |ln(Gamma_m2 / Gamma_m1)| <= 1e-6 a chaque lecture
suivie. C'est la garde d'identite de l'instrument d'une machine a l'autre.

## 6. Etage 1 : temoins

6.1 TEMOIN POSITIF (TP) : celui du gel bis (5.1), inchange. Le jumeau H+ du moteur (signe +1,
potentiel x^5), w2 = 39/20, aux deux couplages retenus (liste 69b3bab3bb8480b7 : j = 6 et j = 8),
etat du vide (0, 0), bord 40, eta0 = 0.05, energie cible de depart 0. Reference par rotation
complexe : la table 4d51dd58ef456fe9, reprise a l'octet ; aucune reference n'est recalculee.
Mesure : sous A, B, C et D, sur l'echelle 3.5. TP TIENT si, a chaque couplage et sous chaque
absorbeur : PLATEAU, et |ln(Gamma_pl / Gamma_ref)| <= tau + u_ref. Huit epreuves.
Le temoin est REGLE (section 4, (iii)), pas aveugle.

6.2 TEMOIN NEGATIF (TN) : une largeur que seul l'absorbeur fabrique. A chaque ancre, le jumeau H+
(signe +1) aux w2, g, r_c et eta0 de l'ancre, a l'etiquette de l'etat de rang 0 de l'ancre,
energie cible de depart l'energie libre du jumeau a ce site ; sous A, B, C et D. Attendu : PAS DE
PLATEAU aux huit (ancre, absorbeur), la largeur etant proportionnelle a eta.
TN rend PLATEAU a l'un des huit : le critere ne mord pas -> NON CONCLUANT D'INSTRUMENT.
Ce temoin remplace celui du gel bis (un etat loge dans l'absorbeur), qui n'a jamais pu etre suivi
a taille reelle. Sa limite est dite en section 14.

6.3 VERDICT DE L'INSTRUMENT. TIENT si le selftest de la feuille tient, si l'etage 0 tient, si les
ancres tiennent et si TP et TN tiennent. Sinon : NON CONCLUANT D'INSTRUMENT, et l'etage 2 n'est
PAS joue.

## 7. Etage 2 : l'objet, etat par etat

Ouvert seulement si l'instrument TIENT. A chacun des douze points, pour chaque etat juge :
  (a) PLATEAU sous A.
  (b) LONGUEUR : PLATEAU sous B, en ACCORD avec A.
  (c) FORME : PLATEAU sous C, en ACCORD avec A.
  (d) POSITION : PLATEAU sous D, en ACCORD avec A.
  (e) CONSIGNE, pas une condition : |ln(G_dep / Gamma_pl(A))| <= tau. Si elle tient, "la lecture
      deposee est sur le plateau" a cet etat ; elle ne se lit que si A a un PLATEAU.
Statut de l'etat :
  QUALIFIE      : (a), (b), (c), (d) tiennent.
  NON QUALIFIE  : l'une echoue sur des valeurs lisibles (un absorbeur a au moins une fenetre et
                  aucune sous tau, ou un accord echoue).
  NON LISIBLE   : un absorbeur n'a aucune fenetre (suivi perdu) et aucune epreuve n'echoue par
                  ailleurs.
L'ETAT LU d'un point est son etat de rang 0 : celui que la lecture a la facon de M17 retient (plus
grand recouvrement avec la graine). Il est juge aux douze points.

## 8. Cascade (premier cas qui s'applique) et issue separee

  NON CONCLUANT D'INSTRUMENT : l'instrument ne tient pas (6.3).
  RUN INCOMPLET              : l'un des douze points manque ; aucun verdict n'est rendu.
  ESTIMATEUR QUALIFIE        : l'etat lu est QUALIFIE aux douze points ET neuf dixiemes au moins
                               des 137 etats juges sont QUALIFIES (au moins
                               124).
  QUALIFIE A L'ETAT LU       : l'etat lu est QUALIFIE aux douze points, moins de neuf dixiemes des
                               etats juges le sont.
  QUALIFIE PAR POINT         : l'etat lu est QUALIFIE a un point au moins, pas a tous.
  NON QUALIFIE               : l'etat lu n'est QUALIFIE a aucun point, et NON QUALIFIE a un au
                               moins.
  NON LISIBLE                : sinon.
ISSUE SEPAREE, sur la consigne (e), comptee sur les etats ou A a un PLATEAU :
  LA LECTURE DEPOSEE EST SUR LE PLATEAU                              : a tous ces etats ;
  LA LECTURE DEPOSEE EST SUR LE PLATEAU A NEUF ETATS SUR DIX AU MOINS : sinon, a neuf dixiemes ;
  LA LECTURE DEPOSEE N'EST PAS PARTOUT SUR LE PLATEAU                 : sinon.
Les deux se lisent independamment. L'acte donne, a cote, les comptes par point et par absorbeur.

## 9. Ce que chaque issue autorise a ecrire

  ESTIMATEUR QUALIFIE : "aux douze points et aux etats juges QUALIFIES, la largeur lue sous
      absorbeur long est une largeur sortante stable sous les variations jouees de force, de
      forme, de longueur et de position, a tau pres". Le reclassement du delta 95 ("toute phrase
      portant un Gamma depuis juillet est reclassee") est leve pour ces etats, ET SEULEMENT pour
      eux, avec pour valeur Gamma_pl(A). Il n'est leve pour une largeur deposee que si, de plus,
      la consigne (e) tient a cet etat.
  QUALIFIE A L'ETAT LU : la meme phrase, pour les etats lus des douze points et pour ceux des
      autres etats qui sont QUALIFIES ; l'acte nomme ceux qui ne le sont pas.
  QUALIFIE PAR POINT : la phrase vaut point par point, aux etats QUALIFIES ; l'acte nomme les
      points ou l'etat lu echoue, et rien n'est dit de l'estimateur en general.
  NON QUALIFIE ou NON LISIBLE : la piste (0) se ferme. Le plateau vu aux points de reglage ne
      s'etend pas aux points juges ; le reclassement du delta 95 reste entier.
  NON CONCLUANT D'INSTRUMENT : rien n'est lu du fantome.
Dans tous les cas : aucun verdict depose n'est reecrit, aucune piece citee n'est editee (PB-1), et
le verdict de la nuit bis reste NON QUALIFIE sous son gel. Aucune issue ne dit rien hors des douze
points, de la fraction 0.70, du canal (2,1) de x^5, ni des etats sous dix planchers du depot.
Aucune issue ne dit que la chaine est qualifiee : ce gel ne lit pas la chaine.

## 10. Gardes (enumerees ; chaque log dit ce qu'il ne joue pas)

  G-T1  canons du moteur (82a0be882568fe0c), du depot (10887c60d5f55bcf) et de la liste des retenus
        (69b3bab3bb8480b7) : verifies par la sonde avant tout calcul, a chaque appel ; elle refuse
        sinon. La feuille verifie de son cote le depot, la table du temoin (4d51dd58ef456fe9) et la
        reference des ancres (6600fb8418c79930).
  G-T2  la sonde (b5616dcf858e8801) porte le bloc du lecteur (9b0f95f3e10e9b0d) tel quel ; chaque
        sortie consigne le canon de la sonde qui l'a ecrite, et la feuille (b2d6d7cfaf30f1cf)
        refuse toute sortie d'un autre canon.
  G-T3  le reglage consigne dans chaque sortie (echelle, absorbeurs, seuils du lecteur) est celui
        de ce gel ; la feuille refuse sinon.
  G-T4  completude : a chaque point, les etats lus sont exactement ceux que la regle de la
        section 1 tire du depot ; chaque etat a ses quatre absorbeurs et ses douze barreaux ;
        chacun des douze points est lu une fois et une seule. La feuille refuse sinon.
  G-T5  comptes : etage 0, 84 lectures ; ancres, 192 ; etage 1, 96 au temoin positif et 96 au
        temoin negatif ; etage 2, 6576 lectures (137 etats, quatre absorbeurs,
        douze barreaux).
  G-T6  selftest de la feuille : 68 cas tenus sur 68, rejoue a chaque
        lecture ; banc qui tue (6b63a9de25107ae4) : 43 alterations du code de la feuille,
        43 mordues.
  G-T7  plateforme consignee dans chaque sortie : systeme, python, numpy, scipy, fils.
  G-T8  identite de matrice : au bloc N = 60 du point 1.98 de M17, la matrice assemblee par le
        lecteur d'exploration est celle de H_2D du moteur a l'element pres (note, section 3) ; le
        bloc de ce gel assemble par les memes boucles, et l'etage 0 l'eprouve sur 84 lectures.

## 11. Annonces de la plume (ecrites apres le calcul de la section 4 ; aveugles aux douze points)

Si l'instrument ne tient pas, A-2 a A-6 et A-8 a A-10 sont NON JUGEES : ni creditees ni debitees.
Une annonce qui porte sur des etats "a PLATEAU" est NON JUGEE s'il n'y en a aucun.
  A-1  le verdict. ESTIMATEUR QUALIFIE : 0.46 ; QUALIFIE A L'ETAT LU : 0.08 ;
       QUALIFIE PAR POINT : 0.40 ; NON QUALIFIE : 0.01 ; NON LISIBLE : 0.01 ;
       NON CONCLUANT D'INSTRUMENT : 0.04.
       Raison : au point de reglage le plus dur (E4, g = 1.2e-2), l'etat lu passe avec une marge
       d'un peu plus d'un centieme et trois etats sur quatorze echouent ; le point juge L3 en
       est proche. Ailleurs le reglage tient largement. L'instrument peut manquer sur une autre
       plateforme (tolerance des ancres, installation).
  A-2  l'issue de la lecture deposee. SUR LE PLATEAU a tous les etats : 0.02 ; A NEUF ETATS SUR DIX
       AU MOINS : 0.23 ; PAS PARTOUT : 0.75. Raison : a E4, la lecture deposee s'ecarte du
       plateau de plus de tau a la majorite des etats ; les points juges de fort couplage
       portent plus de la moitie des etats juges.
  A-3  l'etat lu est QUALIFIE aux onze points autres que L3 : 0.80.
  A-4  L3 est le point qui compte le plus d'etats non QUALIFIES, ex aequo admis : 0.55.
  A-5  aux six points de delta negatif (C1, C2, M1, M2, L1, L2), aucun etat n'a, sous A ni sous
       B, de meilleure fenetre d'etalement superieur a 0.02 : 0.80.
  A-6  a tout etat ou A et B ont un PLATEAU, |ln(Gamma_pl(B) / Gamma_pl(A))| <= 0.02 : 0.60.
  A-7  l'instrument tient (non aveugle : etages regles) : 0.96.
  A-8  C est l'absorbeur sous lequel le plus d'etats n'ont pas de PLATEAU, ex aequo admis et zero
       partout compte comme vrai : 0.70.
  A-9  la mediane de |ln(G_dep / Gamma_pl(A))|, sur les etats ou A a un PLATEAU, est entre 0.01
       et 0.04 : 0.75.
  A-10 trois etats au plus sont NON LISIBLES : 0.80.
Ces probabilites sont ecrites apres le reglage de la section 4 et avant tout calcul aux douze
points. Aucune n'a ete donnee a l'operateur avant ce reglage.

## 12. Deroulement, E19, et ce qui est permis

ORDRE. (1) certification croisee du gel, de la sonde, de la feuille et du banc par machine 2 ; un
seul tour de correction ; feu vert ecrit de l'operateur. (2) la sonde en modes etage0, ancres et
etage1 ; la feuille en etape "instrument". (3) si et seulement si elle rend TIENT : la sonde en
mode point, un appel par point ou par groupe de points, en parallele si machine 2 le veut (les
appels sont independants et sans tirage) ; la feuille en etape "verdict".
PRE-VOL. Avant le feu vert, machine 2 peut jouer la sonde en modes etage0, ancres et etage1 pour
eprouver son installation (scipy, durees) : ce sont des points regles, que machine 1 a joues. Si
la tolerance des ancres (1e-6) y mord pour une raison de plateforme, c'est un defaut de ce gel, a
traiter dans le tour de correction, pas un resultat. Le run juge rejoue ces trois modes.
UNE SEULE EXECUTION. Dans le run juge, chaque appel est joue une fois. Un appel interrompu se
relance ENTIER, et l'acte le dit ; aucun appel n'est rejoue apres lecture de sa sortie.
E19. Aucun calcul 2D sous absorbeur long, par aucune des deux machines, a aucun des douze points,
avant la certification croisee. Machine 1 ne joue la sonde a aucun des douze points avant d'avoir
recu et authentifie le lot de resultat ; elle peut ensuite rejouer, et compare alors a 1e-6 en
relatif sur les lectures suivies, tolerance declaree ici. Les etages 0 et 1 et les ancres sont
regles : machine 1 les a joues (section 4).
PIECES DU RESULTAT. Les fichiers sonde_ter_*.json, les deux verdicts et les deux journaux de la
feuille, le journal du pilote avec heures et codes de sortie, l'etat de la machine.
Ce gel ne se rejoue pas sous d'autres seuils, d'autres absorbeurs ou une autre echelle apres
lecture : une suite demanderait un autre gel et une autre decision de l'operateur.

## 13. Couts (mesures sur le conteneur de machine 1, deux coeurs, un fil par processus)

  Etage 0 : 20 s (84 lectures a N = 60 et 61). Etage 1 : 1095 s ; ancres :
  730 s ; ces deux-la avec trois ou quatre processus sur les deux coeurs.
  Etage 2 : 6576 lectures. Aux points de reglage, un etat (quatre absorbeurs, douze
  barreaux) a coute de 135 s a 309 s selon r_c et selon la charge, deux
  ou trois processus se partageant les deux coeurs ; soit, pour 137 etats, de l'ordre
  de 7.1 h de calcul cumule, a diviser par le nombre de processus de BOCAL4.
  Memoire : pic mesure de 571 Mo pour une lecture a la plus grande boite du gel
  (N = 154). scipy est requis sur BOCAL4.

## 14. Limites declarees

  L-1  Post hoc. Les longueurs (80 et 100), la forme de reference (F2) et l'echelle ont ete
       choisies apres l'echec de la nuit bis et apres exploration de quatorze points deja joues,
       en deux temps (section 4, (ii bis)). Les douze points juges n'ont servi a rien de cela.
  L-2  La forme F3 du gel bis (bord aligne sur le canal) n'est pas jouee. Aux six points de M17, a
       60 couches, elle rend la meme valeur de plateau que F1 a 80 couches a 0.0046 pres au
       pire (note, tableau de la section 4) : elle n'ajoutait pas une variation distincte de (c).
  L-3  Le temoin negatif mord sur une largeur proportionnelle a eta. Il ne dit pas que le critere
       rejetterait une largeur fabriquee autrement par l'absorbeur ; ce sont les epreuves (b), (c)
       et (d) qui portent cette charge.
  L-4  L'etat est choisi par son etiquette de Fock et son energie deposee, pas par recouvrement
       avec la graine puis suivi par continuite comme au gel bis. Un etat dont le poids au site
       tombe sous 0.5 est NON LISIBLE, pas NON QUALIFIE.
  L-5  Les etats juges sont ceux que la sonde dense a lus au-dessus de dix planchers. Les etats
       plus etroits, que le lecteur pourrait lire, ne sont pas juges : il n'y a pas de lecture
       deposee a leur comparer.
  L-6  Cinq barreaux font un facteur 16 en eta. Un plateau plus court n'est pas un plateau au
       sens de ce gel, quel que soit son etalement.
  L-7  Machine 1 connait les largeurs deposees aux douze points (k = 2, 3, 4, 20 couches). La
       consigne (e) n'est donc pas aveugle a G_dep ; elle l'est a Gamma_pl.
  L-8  D translate F2, que la plume n'a vu translate qu'aux points de reglage de (ii) ; aux six
       points de M17 c'est F1 qui avait ete translate.
  L-9  C n'isole pas la forme : F1 y est jouee a 100 couches, contre F2 a 80 sous A. Sous F1 a 80
       couches, des etats des points de reglage de delta positif n'ont pas cinq barreaux a tau.
  L-10 Aux plus forts couplages vus (E4, g = 1.2e-2), la largeur lue oscille avec eta de quelques
       centiemes sous tous les absorbeurs essayes, jusqu'a 100 couches : le plateau y tient a tau
       de peu, ou pas. Le point juge L3 (g = 1.07e-2) est de ce cote.
  L-11 La fenetre retenue est celle de plus petit rapport, meme quand une autre fenetre a PLATEAU
       serait en accord avec A. Vu une fois, au premier jeu : J2, rang 5, sous F1 a 80
       couches, une fenetre du cote fort (k0 = -3, etalement 0.0121) retenue a 0.1418 de A en
       logarithme. La regle du gel bis
       n'est pas changee pour autant.

## 15. Differences avec le gel bis (dcda1611adf5f8fd)

  (1) ABSORBEURS. 80 et 100 couches au lieu de 20 et 30 ; reference F2 au lieu de F1 ; F3 retiree ;
      la translation porte sur F2. Echelle k = -3 a 8 au lieu de -5 a 12.
  (2) INSTRUMENT. Un lecteur creux, un etat a la fois, au lieu de la decomposition dense ; Gamma
      lue par 2 eta <W> ; plus de plancher de lisibilite ; etat choisi par etiquette (L-4). Un
      etage 0 et des ancres reglees eprouvent ce lecteur contre la sonde dense deposee.
  (3) OBJET. Douze points du delta 98, etat par etat (137 etats), au lieu de l'etat lu
      des six points de M17 ; la cascade garde l'etat lu au premier rang et ajoute la part des
      etats. Les T-etats du gel bis (section 7) ne sont pas repris : chaque etat est ici juge.
  Inchanges : la question (portee a d'autres lectures), tau, la regle de plateau, la regle
  d'accord, le temoin positif et sa reference, les quatre variations (force, forme, longueur,
  position), la consigne (e).
  Change : le temoin negatif (6.2).

## 16. Pieces de ce gel (lot machine 1 ; canon = convention B du manifeste)

  qualification_EB_ter_pre_enregistrement_v1.md           CE GEL ; il fait foi
  sonde_qualification_EB_ter_machine1_v1.py               la sonde : elle mesure et ne juge pas
  lecteur_plateau_bloc_machine1_v1.py                     le bloc du lecteur
  lecture_qualification_EB_ter_machine1_v1.py             la feuille : elle juge et ne mesure pas
  banc_feuille_ter_machine1_v1.py                         le banc qui tue de la feuille
  reference_ancres_ter_machine1_v1.json                   la reference des ancres (5.2)
  essais, exploration de reglage, constructions, releve : nommes au manifeste et a la note
  d'accompagnement ; aucun n'est opposable.

-- FIN qualification_EB_ter_pre_enregistrement_v1 --
