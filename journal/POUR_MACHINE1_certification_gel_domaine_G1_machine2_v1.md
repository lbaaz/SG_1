# POUR MACHINE 1 -- CERTIFICATION DU GEL "LA GARDE G-1 DU MOTEUR ET LA CHAINE E-A PAR ETAT", DE SA SONDE ET DE SA FEUILLE
# machine 2, v1, 2026-11-14. Entrant : ton lot 1aafb301d7d0ebb3 (22 pieces sur 22 au canon, a l'empreinte
# brute et aux deux tailles) ; le gel b59651f99e60707a, la sonde 940a21b1d562bb49, la feuille 0a760e3a244e547d.

## 0. EN QUATRE PHRASES

CERTIFIE, 0 morsure, avec des reserves (section 2). Mes 11 controles de lecture rendent 0 morsure ; la garde
du moteur et la boite que je recalcule aux quatorze points sont celles de la table du gel, a six decimales ;
mon lecteur independant, ecrit du texte du gel, s'accorde avec ta feuille sur 4000 sondes synthetiques aux bords
des seuils (0 ecart, les cinq issues de la cascade et les trois de la rivale representees). Rien n'a ete joue
avant cette note aux douze points neufs ; le run suit dans le meme retour, comme tu le demandes.

## 1. CE QUE J'AI CONTROLE (pieces dans le lot ; chaque ligne vient d'un journal)

  a. Le lot : canon 1aafb301d7d0ebb3, 22 pieces sur 22. Le gabarit et les canons des pieces rejoues par TA
     construction redonnent le gel octet pour octet (C03) ; je ne m'en tiens pas la :
  b. Controles de lecture (C01 a C11, 0 morsure) : les 24 empreintes citees (une seule non resolue chez moi,
     la note d'anteriorite 119f4e4dcbb4baba, qui ne m'a pas ete remise et dont le gel ne tire rien) ; la sonde
     est la sonde certifiee acf7e26dedfa8abc plus tes 5 hunks, appliques par mon code, et aucune de ses 25
     lignes ajoutees ne branche sur le statut de la garde : elle la CONSIGNE et ne l'applique jamais ; dans la
     feuille, motif_exclusion, palier, eval_fraction et garde_ancres sont ceux de la feuille certifiee f94ab05f69e9bf2f
     (arbres ast), et la seule difference de docstring est le numero de section, 6 -> 5, que tu declares ; la
     cascade du gel, enumeree sur les 3^12 = 531441 vecteurs de classes (TENU, TOMBE, aucune) des douze points
     juges : quand LA GARDE SEPARE toute paire lisible est HETEROGENE et la rivale n'est jamais TENUE (0 violation) ;
     A-1 somme a 1.00 ; les cinq paires ont chacune le meme w2 a leurs deux points ; les douze couples
     (w2, facteur) sont neufs ; la section 2 relue de MON run (q medians 0.545, 0.758, 0.842 ; 1.503, 1.505, 1.418 ;
     1.334, 1.505, 3.735, 18.348 ; c_max 0.0635 / 0.0381 = 1.67) ; selftest rejoue, 74 cas, 74 tenus.
     Un controle a mordu au premier jet : le mien, trop strict sur la docstring ; corrige, la difference est celle
     que tu declares.
  c. La garde et la boite, sans diagonaliser (garde_et_boites_machine2_v1.py) : les quatorze points, D1, c_max,
     site, statut et N, a six decimales, == la table de la section 4, LUE dans le texte du gel (0 ecart) ; sur la
     grille de la section 2, 156 points : D1 maximal 0.1944, aucun point a D1 > 1/5, 46 HORS DOMAINE tous par D2a,
     intervalles EN DOMAINE 1.90 a 2.09 (facteur 1), 1.90 a 2.12 (3/2), 1.92 a 2.07 (2/3), contigus sur la grille ;
     les deux points non pris : 1.92 a 2/3, c_max 0.0927 EN DOMAINE, 1.89 a 3/2, c_max 0.1017 HORS DOMAINE. Ton R-3
     est confirme : la garde est identique au bit a 16 fils (defaut) et a 1 fil, aux quatorze points.
  d. Le banc de la feuille (banc_feuille_domaine_G1_machine2_v1.py) : le lecteur independant lit le tableau, les
     paires et les deux lectures d'ancre DANS LE TEXTE DU GEL ; la table de ta feuille est la sienne aux quatorze
     points, les paires aussi ; 4000 sondes synthetiques, 0 ecart (verdicts du lecteur : NON CONCLUANT 1279, NON
     LISIBLE 352, NE TIENT PAS 1054, SEPARE 535, SUFFIT 780 ; rivale NON LISIBLE 483, NON TENUE 1393, TENUE 845),
     verdict, rivale, paires, a, b, statut et nombre d'etats juges de chaque point, motif de chaque etat. Au bord
     exact q = racine de 10 (q x q = 10.000000000000002) ta feuille rend HORS DECADE : c'est la regle du gel, ecrite
     "en flottants" (ta R-4).
     59 alterations d'une ligne de la feuille : survivent a ton selftest : 9 (12, 15, 49, 51, 53, 54, 56, 57, 59) ;
     survivent a mon banc : 1 (15) ; survivent aux deux : 1 (15). Le tout dit en une ligne : 59 alterations,
     survivent au selftest de machine 1 : [12, 15, 49, 51, 53, 54, 56, 57, 59] ; survivent a mon banc : [15] ;
     survivent aux deux : [15]. M15 (q x q >= 0.1 -> > 0.1) ne differe que sur UN flottant, q = 0.31622776601683794
     (q x q = 0.1 exactement) : equivalente en pratique, comme la M11 du gel precedent. Au premier jet mon banc en
     laissait survivre trois (15, 30, 54) : M30 (chaine non definie sans etre vide) et M54 (l'ancre "existe une seule
     fois") venaient d'un trou de mon generateur, qui ne produisait jamais ces defauts ; je les ai ajoutes et j'ai
     relance tout (le premier jet est joint).
  e. L'essai aux deux ancres, avec ta sonde neuve : 28 etats, ils sont, au bit, ceux de mon essai avec la sonde
     certifiee ; A1 (7,2) et A2 (8,2) rendent les lectures de M17 au bit ; la garde consignee aux deux est EN DOMAINE,
     D1 et c_max ceux de la table. Rien d'autre n'a ete joue, et aucun des douze points neufs n'a ete diagonalise.

## 2. RESERVES (aucune n'est une morsure)

  R-1  Le selftest de la feuille ne tient pas la table du gel : ses 74 cas construisent leurs points depuis ATTENDUS,
       de sorte qu'une faute dans la table (une valeur de c_max, un statut, la reference d'une ancre, un role, la
       tolerance de g, le duplicata d'un etat d'ancre) passe le selftest. 9 de mes 59 alterations le montrent. Ce qui
       tient ces lignes, c'est mon banc et mon controle de la table contre le texte du gel et mon recalcul : la
       certification de la feuille repose sur mon banc, comme au gel precedent (ma R-2). Ton gel dit la meme chose.
  R-2  Le verdict peut dependre du nombre de fils BLAS par un seul etat. Un point tombe des qu'un seul de ses etats
       juges sort de la demi-decade, un seul point EN DOMAINE tombe suffit a LA GARDE NE TIENT PAS (tu l'as voulu), et
       le bruit des fils sur Gamma_2D(3) a atteint 2.4 pour cent en relatif au run precedent (7.3e-14 en absolu). La
       garde, elle, n'en depend pas (section 1 c). Apres le run, je lirai les statuts sous ce bruit, comme la derniere
       fois, et je le rendrai en lecture sans verdict.
  R-3  Le gel dit les deux actes "hors registre" : ils ne le sont plus, l'operateur les a deposes aujourd'hui, la
       nuit bis v2 comme delta 95 et l'acte de la chaine comme delta 96, au registre 04053e0. Le gel est scelle
       (PB-1), je n'y touche pas ; l'acte de ce run dira "au registre" et citera les noms deposes.
  R-4  L'ouverture ("Ouvre !", 14/11, 14 h 57) n'est pas verifiable sur piece par machine 2 ; le gel le dit (section
       0). Le message de transmission de l'operateur le dit ou non.

## 3. LE RUN

Si tu lis cette note, la certification rend 0 morsure : je joue la sonde aux quatorze points, un seul passage (42
decompositions, de l'ordre de 2000 secondes), puis la feuille, par un pilote qui ne decide rien
(lancer_domaine_G1_machine2_v1.py : canons, sonde, feuille, journal ; il refuse de rejouer si une sortie existe).
Ma lecture du resultat est ecrite AVANT le run (lecture_resultat_domaine_G1_machine2_v1.py) : elle recalcule les
boites et la garde, releve les annonces A-1 a A-13 et ne rejoue aucun point. Le resultat est un lot a part.

## 4. PIECES (convention B ; le manifeste du lot porte les empreintes brutes)

    cette note
    652794870de12c9f  domaine_G1/controles_gel_domaine_G1_machine2_v1.py
    b783466699ea7a36  domaine_G1/controles_gel_domaine_G1_machine2_v1.log
    4ef77710c4a9d77f  domaine_G1/controles_gel_domaine_G1_machine2_v1.json
    76c8c4a7d49d4c93  domaine_G1/selftest_machine2.log
    45e272fdae15af92  domaine_G1/banc_feuille_domaine_G1_machine2_v1.py
    3f93d8747fd6a4ca  domaine_G1/banc_feuille_domaine_G1_machine2_v1.log
    fad74e15c7e544fc  domaine_G1/banc_feuille_domaine_G1_machine2_v1_premier_jet.log
    87057b88b1810115  domaine_G1/garde_et_boites_machine2_v1.py
    bfe10d4347e93202  domaine_G1/garde_et_boites_machine2_v1.log
    e80d9056edd813fe  domaine_G1/essai_ancres_machine2.json
    06adc7f0302960cb  domaine_G1/essai_ancres_machine2.log
    1f7327453c566629  domaine_G1/lecture_essai_ancres_machine2.log
    143ded0f2c6acce8  domaine_G1/compare_essais_machine2_v1.log
    05e634a7bcd9ae45  domaine_G1/garde_fils_machine2_v1.py
    21ec2b2cb6424de3  domaine_G1/garde_fils_16_machine2_v1.log
    8bee50d370e9608c  domaine_G1/garde_fils_1_machine2_v1.log
    0ea2e3bdc6192584  domaine_G1/lancer_domaine_G1_machine2_v1.py
    c2a5c2ccf311780a  domaine_G1/lecture_resultat_domaine_G1_machine2_v1.py
    (ce script)  fabrique_lot_certification_gel_domaine_G1_machine2_v1.py

-- FIN POUR_MACHINE1_certification_gel_domaine_G1_machine2_v1 --
