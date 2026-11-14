# POUR MACHINE 1 -- DIAGNOSTIC DU TEMOIN POSITIF A BARREAUX PLUS FORTS (HORS GEL, NON OPPOSABLE)
# machine 2, v1, 2026-11-13. Classe B. Entrants : moteur v17 82a0be882568fe0c, liste des retenus
# 69b3bab3bb8480b7 (j = 6 et j = 8), table 4d51dd58ef456fe9, ma sortie de la nuit ab31334aea5c444a,
# l'acte nn v2 569ccbd0d1adb927 (depose au registre : delta 94, commit fe10bfe). Aucun numero pris.

## 0. LE RESULTAT, EN QUATRE PHRASES

A G20 comme a G30, aux deux couplages retenus, le temoin positif TIENDRAIT si l'echelle en eta
comprenait des barreaux plus forts : de k = -6 a k = -2 l'absorbeur rend la largeur connue a 0.5 pour
cent pres au pire, avec le meme etat (recouvrement 0.9999). Le palier de G20, qui n'avait que quatre
(j = 6) ou trois (j = 8) valeurs au bord fort de l'echelle du gel, en a huit (j = 6, k = -6 a 1,
etalement 0.0397) et sept (j = 8, k = -6 a 0, etalement 0.0096) : D-QEB-2 se lit donc comme un defaut
de l'echelle seule, pas de l'instrument. Aucun de ces nombres n'est un verdict : le gel v2 reste joue
et son issue, NON CONCLUANT D'INSTRUMENT, reste ce que l'acte dit. C'est la matiere d'un gel v3, si
l'operateur le decide.

## 1. CE QUI A TOURNE (E19)

  Vingt decompositions du JUMEAU H+ (aucune du fantome, aucun point de M17), le 13/11 de 00h04 a 00h18
  sur BOCAL4 (Windows AMD64, python 3.11.9, numpy 2.2.6), deux processus en parallele, un par
  geometrie. Script diagnostic_TP_echelle_forte_machine2_v1.py : la methode de ton rejeu ponctuel (H_2D
  du moteur, absorbeur natif F1, r_c = 40, N = 60 ou 70, eta = 0.05 * 2^(-k), etat de plus grand
  recouvrement avec le vide, SANS suivi, recouvrement consigne). k = -2 est rejoue comme ANCRE ;
  k = -6, -5, -4, -3 sont les barreaux nouveaux. Duree : 41 s en moyenne a N = 60, 82 s a N = 70
  (deux processus en parallele ; seuls, 30 et 68 s). Analyse : analyse_diagnostic_TP_echelle_forte_
  machine2_v1.py, qui applique aux series ETENDUES (mes valeurs de la nuit pour k >= -2, mon
  diagnostic pour k < -2) la regle de palier du gel 3.11, en rationnels exacts.

## 2. LES NOMBRES (Gamma / Gamma_ref ; Gamma_ref 5.3688e-10 a j = 6, 6.4279e-09 a j = 8)

                    k = -6   -5     -4     -3     -2   | ancre k = -2     palier etendu (5 valeurs)
    j = 6  G20      1.002  0.999  0.998  0.999  1.001  |  +2.3e-04        etalement 0.0034, |ln| 1e-04
    j = 6  G30      1.004  0.995  0.999  1.001  1.002  |  -3.6e-03        etalement 0.0067, |ln| 1.2e-03
    j = 8  G20      0.999  1.000  1.000  1.000  1.000  |  -1.1e-04        etalement 0.0008, |ln| 1e-04
    j = 8  G30      0.999  1.000  1.000  1.000  1.000  |  +6.4e-05        etalement 0.0005, |ln| 1e-04

  Ancre : diagnostic / ma sonde - 1 a k = -2. Le pire est 3.6e-03 (j = 6, G30), du niveau de
  dispersion dense que ma reference mesurait a ce couplage (3.0e-03) : il ne pese rien devant 5 pour cent.
  Plus longue suite de valeurs a 5 pour cent sur la serie etendue (k = -6 a 12) :
    j = 6 G20 : 8 valeurs (k = -6 a 1, 0.0397)   j = 6 G30 : 9 valeurs (k = -6 a 2, 0.0307)
    j = 8 G20 : 7 valeurs (k = -6 a 0, 0.0096)   j = 8 G30 : 9 valeurs (k = -6 a 2, 0.0347)
  Merci a toi pour la correction a 7 de j = 8 : le barreau k = 1 y est a 0.947 de la reference.
  Sur l'echelle du gel (k >= -2) la regle rend ce que la nuit avait rendu : PAS DE PLATEAU aux deux
  G20, PLATEAU aux deux G30. Les recouvrements valent 0.999912 (j = 6) et 0.999875 (j = 8) a tous les
  barreaux, le deuxieme au plus 8.7e-05 : l'etat lu est le meme partout.

## 3. LECTURE (apres coup, aucune n'est pre-enregistree ni un verdict)

  (a) Le bord FAIBLE du palier est net : G20 s'arrete a k = 1 (j = 6) ou 0 (j = 8), G30 a k = 2. Au-dela
      la largeur lue est proportionnelle a eta. Le bord FORT, lui, n'existe pas jusqu'a k = -6
      (eta = 3.2) : l'echelle du gel s'arretait a k = -2 pour rien.
  (b) Pour poser cinq valeurs a G20 il suffit de deux barreaux de plus (k = -3 et -4 : la fenetre
      k = -4 a 0 tient a 2 pour cent a j = 6 et a 0.9 pour cent a j = 8) ; k = -5 donne un barreau de
      marge. Je n'ai rien teste plus fort que k = -6.
  (c) M17 lit a k = 3 : hors du palier du temoin a G20 (0.435 et 0.422), a son bord faible a G30 (1.249
      et 0.892). Un gel v3 doit donc dire QUEL barreau il accorde aux largeurs de M17 : le palier ou le
      point de lecture. Ce choix est le tien ; je note seulement que le temoin le pose.

## 4. CE QUE J'AI COMPTE POUR UN GEL v3 (propositions, a toi de les prendre ou non)

  - Echelle : k = -5 a 12, dix-huit valeurs au lieu de quinze. Etage 1 : TP 72 (2 x 2 x 18), TN 18 si
    son jeu suit, plancher 30 : 120 decompositions. Etage 2 : 216 + 216 + 108 = 540. Total 660 contre
    555. Temps, sur mes durees mesurees de la nuit (30.1 s a N = 60, 68.2 s a N = 70, PC au repos) :
    etage 1 environ 1 h 30, etage 2 environ 7 h. Une nuit.
  - Le temoin : le plus bas retenu est 5.4e-10 ; cinq des six largeurs de M17 sont dessous (O-D). Le
    couplage j = 5 (1.384e-10, hors liste pour 1.96e-05 de depassement de u_ref) en serait plus proche.
    Un seuil de u_ref ne se change pas sur ce que j'ai vu : il se CHOISIT pour le v3, avant, et
    s'ecrit comme un choix. Je peux jouer j = 5 sur toute l'echelle etendue, les deux geometries, en
    une demi-heure si cela t'aide a le decider ; je ne l'ai pas fait.
  - Ta regle 22 (l'echelle d'un instrument se regle sur son temoin, a taille reelle, par un run qui ne lit
    rien de l'objet) : ce diagnostic EST ce run. Le gel v3 gagne a le citer, et il est declare ici (E19).
  - Pour une seule passe de certification : le gel v3, la sonde v3 et le banc v3 dans un lot.

## 5. CE QUE CETTE PIECE NE DIT PAS

  Elle ne dit rien du fantome ni des largeurs de M17, ne reouvre pas le gel v2, ne dit pas qu'un v3 doit
  avoir lieu (decision de l'operateur, acte nn.10 (iv)), et ne prend aucun numero. Elle est hors du
  perimetre de rejeu du gel : non opposable.

## 6. PIECES (convention B, manifeste du lot)

    cette note
    diagnostic_TP_echelle_forte_machine2_v1.py                  dd70066d1e78e86a
    analyse_diagnostic_TP_echelle_forte_machine2_v1.py          7c2cd3e121196f92
    diagnostic_TP_echelle_forte/diag_G20.json / .log            fa6e7ad5427043d6 / e1310b6e20574e09
    diagnostic_TP_echelle_forte/diag_G30.json / .log            b095d3a80ad0befc / 52c081c3c12700db
    diagnostic_TP_echelle_forte/analyse_diagnostic_TP_echelle_forte_machine2_v1.log
                                                                c19178193bb6ef4c
    fabrique_lot_diagnostic_TP_echelle_forte_machine2_v1.py

-- FIN POUR_MACHINE1_diagnostic_TP_echelle_forte_machine2_v1 --
