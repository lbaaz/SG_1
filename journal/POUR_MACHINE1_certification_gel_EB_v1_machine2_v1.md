# POUR MACHINE 1 -- CERTIFICATION DU GEL E-B v1 (QUALIFICATION DE L'ESTIMATEUR Gamma_LS)
# machine 2, v1, 2026-11-11. Classe B. Entrant : tes deux pieces a plat du 11/11 (13h47),
# qualification_EB_pre_enregistrement_v1.md et estimation_TP_wkb_machine1_v1.py ; aucun manifeste,
# aucun lot. E19 : aucun run de l'etage 1 ni de l'etage 2 n'est joue pour ecrire cette piece (un
# ESSAI DE FORMULE a un seul point de l'echelle du TP est declare en 4).

## 0. LE VERDICT, EN QUATRE PHRASES

**GEL E-B v1 (8603af9d4f63e9dc) : NON CERTIFIE EN L'ETAT -- UN v2 EST DEMANDE, PAS UN ERRATUM**
(le gel n'est pas depose). **21 controles, 2 morsures**, toutes deux de DESCRIPTION, aucune sur un
nombre ni sur une piece : **E-EB-1** (G-Q7 demande un test que la comparaison du gel ne peut pas
rendre en flottants) et **E-EB-2** (le decompte de G-Q10 omet le temoin negatif). Tout le reste
tient : sources au canon, 36/36 pieces, chaque nombre cite relu dans les pieces, la formule de
rotation complexe du TP **re-derivee et validee -- elle est juste telle qu'ecrite**. **La sonde
n'est pas livree** (le script joint est l'estimation WKB, non opposable) : E19 reste dressee pour
toi comme pour moi, et je ne certifie rien de la sonde.

## 1. CE QUE J'AI REJOUE (audit_gel_EB_v1_machine2_v1.py, tous chemins en arguments)

  PIECES LIVREES  gel 8603af9d4f63e9dc (17381 o), WKB 3eeb30328f9c542c (1622 o). Les deux : ASCII
      pur, LF seul, donc empreinte B == empreinte brute (aucune ambiguite de normalisation).
  SOURCES (2)     moteur v17 82a0be882568fe0c 103150 o ; gel M17 v12_b2 20950e52e7d63225
      58507 o ; manifeste du run 4aecd0e2b23bc818 ; **36/36 pieces au canon et a la taille**.
  NOMBRES         r0 = 40 / 41 ; eta0 = |w2 - 2| a 1e-12 ; G_run lu a k = 3 (facteur 0.125) ;
      **E_run = ln(2.6614e-09 / 6.5625e-11) = 3.7027** ; **plancher 7.550e-14**, dix fois ->
      7.55e-13 -> decade 1e-12. Tous exacts.
  DECOMPTES       15 valeurs de k ; 180 + 180 + 90 + 30 + 60 = 540. Juste -- mais voir E-EB-2.
  WKB             ton script tourne chez moi, dans un dossier neutre, et rend j = 5..11, 7 sur 17.
  PORTES (etape 0) aux six points, N + p, la translation de p couches et les deux derniers pas de
      descente sont sous 0.05 (max 0.0469 sur les deux derniers pas, a 2.03 ; 0.0308 sur les portes, a 2.02) ; la premisse de ton
      annonce A-2 est exacte : le dernier pas est plus grand que le precedent a 2.02, et a lui seul.

## 2. LES DEUX MORSURES, ET LA CORRECTION QUE JE PROPOSE

**E-EB-1  G-Q7 : "ETALEMENT 0.05 EXACTEMENT -> PLATEAU" EST INSATISFAISABLE EN FLOTTANTS.** Le gel
definit e = max/min - 1 et PLATEAU si e <= tau = 0.05 (3.11). Sur la serie (1.0 ... 1.05), e vaut
**0.050000000000000044** : e <= 0.05 est FAUX, le selftest du gel rendrait PAS DE PLATEAU la ou il
l'exige. Meme sur des valeurs exactes (20.0, 21.0) le litteral est faux (meme 0.050000000000000044) ;
la forme max <= (1 + tau) * min rend vrai, la comparaison en rationnels aussi. Correction : en 3.11,
**PLATEAU si Fraction(max) <= (1 + Fraction(1, 20)) * Fraction(min)** (e = max/min - 1 n'est plus
qu'un affichage) ; en G-Q7, batir la serie limite sur des valeurs exactement representables :
**(20.0, 21.0) -> PLATEAU** et **(20.0, nextafter(21.0, +inf)) -> PAS DE PLATEAU**, un ulp de part
et d'autre. Meme famille en 3.12 et pour tau_TP : une comparaison de logarithmes n'a pas de borne
"exacte" testable ; ne pas pretendre en tester une, tester a +-1e-6 de la borne, et le dire.

**E-EB-2  LE DECOMPTE ATTENDU OMET LE TEMOIN NEGATIF.** "Decompositions attendues ... au plus 540"
somme F1, formes, translation, plancher et TP ; **le TN (5.2) n'y est pas** : 15 decompositions,
jusqu'a 45 si les replis a + 5 puis a - 5 sont joues. G-Q10 exige "joues + sautes == attendus, par
famille" : la famille TN n'a pas d'attendu. Correction : ajouter "TN 15 (45 au plus avec les deux
replis)" et porter le total a **au plus 585**.

## 3. CE QUE JE DEMANDE EN PLUS, DANS LE MEME TOUR (le gel n'en admet qu'un, section 12)

  M-1  F2 : "meme valeur que F1 au bord de boite" est vrai a la distance L (l'indice N, HORS boite),
       pas sur la derniere ligne reelle (distance L - 1) ou F2/F1 = (L-1)^2 / L^2 = 0.9025 a L = 20.
       Ecrire "a la distance L".
  M-2  G-Q2 : compter par le MANIFESTE (36), pas par les fichiers du dossier. Le dossier de BOCAL4
       en compte 37 : un `pt_39_20_f100.zip` hors manifeste. L'operateur m'annonce avoir envoye le
       contenu du repertoire : si c'est le repertoire entier, tu l'as aussi -- ne le laisse pas
       entrer dans un compte.
  M-3  ETAPE 0 : je n'ai pas tes quatre pieces (20cbc762d58ce1ca, 2d246b2a5c60c244,
       37169cd7d595c575, lot 94c3749c83d4b044) : **0 sur 4** retrouvees sur ce poste (balayage de
       6635 fichiers et 57576 membres de 319 zips, `cherche_etape0_machine2_v1`). Ce que les six
       pieces du run permettent de relire est juste (C10, C11, C20, C21) ; le reste de ce que "l'etape
       0 a etabli" tient sur ta parole. Le dire dans le gel, ou joindre le lot.
  M-4  EMPREINTES : aucun manifeste n'accompagne les deux pieces. Mon canon de lecture est
       8603af9d4f63e9dc (gel) et 3eeb30328f9c542c (WKB). Confirme-les ; et si "titre a terminateur"
       (en-tete du gel) designe autre chose que la convention B pleine, dis laquelle.

## 4. LA ROTATION COMPLEXE DU TP (5.1) -- "FORMULE A RE-DERIVER PAR m2"

Re-derivee depuis x -> e^{i t} x, p -> e^{-i t} p. **Elle est juste telle qu'ecrite, point zero
compris.** Controles : l'oscillateur du gel egale 1/2 e^{-2it} p^2 + 1/2 w^2 e^{2it} x^2 en matrices,
a 3.6e-15 (C16) ; **le x du moteur est (q1 + q2)/sqrt(Delta)** (l_i = 1/sqrt(2 Delta w_i)),
lineaire en q_i, donc x^5 -> e^{5it} x^5 (C17) ; **a t = 0, mon H_rot egale H_2D(N, w2, g, +1,
"x5") du moteur element par element, a 3.55e-15 pour max|H| = 38.35** (C18). La condition t < pi/7
est la bonne plage pour p = 5.

**CE QUE J'AI VU AVANT D'ECRIRE (a la facon de ta section 4).** Un SEUL point de l'echelle du TP, par
l'essai de formule : **g_8 = 0.10**, w2 = 39/20, N dans {30, 40, 50}, t dans {0.15, 0.20, 0.25}.
Largeur du fondamental de H+ : **Gamma = 6.428e-09**, stable a 1.1e-4 relatif sur les neuf calculs (6.4276 a 6.4283e-09) ;
recouvrement avec le vide 0.977 / 0.959 / 0.935. **Ce n'est pas la reference de l'etage 1** (17 g_j,
N jusqu'a 70, aucune selection) : elle reste a jouer, apres certification du gel ET de la sonde. Ton
WKB donne 1.46e-09 au meme g : **un facteur 4.4**, donc une fenetre WKB a lire comme un ordre de
grandeur ; la selection se fait sur ma reference, comme le gel le veut, et je ne tire aucune
conclusion sur la fenetre d'un seul point.

## 5. CE QUE CETTE PIECE NE DIT PAS

Elle ne certifie pas la sonde (absente) ; ne joue ni l'etage 1 ni l'etage 2 ; ne se prononce ni sur
la physique de la question (Riss et Meyer, le critere de plateau) ni sur tes annonces aveugles A-1 a
A-5 (seule la premisse de A-2 est relue). Elle ne prend aucun numero (E18). Le garde-fou de la section
12 est sous veto de l'operateur : ce n'est pas a moi de le trancher.

## 6. CE QUI SUIT

  machine 1 : un **gel v2** (E-EB-1, E-EB-2, M-1 a M-4) et la **sonde** avec sa construction ;
  machine 2 : certification du v2 et de la sonde dans le MEME tour ; puis ma reference du TP (script
      independant, rotation complexe, N jusqu'a 70, selection sur elle seule) ; puis la nuit de BOCAL4
      (etage 1 de l'ordre de 2 a 3 h, etage 2 environ 8 h 30) ;
  operateur : le veto sur le garde-fou ; la confirmation de ce qui a ete envoye (repertoire entier,
      37 fichiers, ou les 36 du manifeste).

## 7. PIECES (convention B, 2026-11-11)

    cette note
    audit_gel_EB_v1_machine2_v1.py / .log / .json          21 controles, 2 morsures
    cherche_etape0_machine2_v1.py / .log                   0 sur 4

-- FIN POUR_MACHINE1_certification_gel_EB_v1_machine2_v1 --
