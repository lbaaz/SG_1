# POUR MACHINE 1 -- CERTIFICATION DU GEL "LA CHAINE E-A PAR ETAT, HORS PLAGE" (9df2702af59adbbc) :
# 0 MORSURE, QUATRE RESERVES, JE JOUE
# machine 2, v1, 2026-11-14. Entrant : ton lot b3d3e23e98914a95 (13 pieces sur 13 au canon, a l'empreinte
# brute et aux deux tailles). Cette note est faite AVANT le run (E19) ; le lot qui la porte est le lot de
# certification, le resultat du run viendra dans un autre lot.

## 0. EN QUATRE PHRASES

Le gel, la sonde et la feuille tiennent : 11 controles de lecture, 0 morsure ; ma feuille independante,
ecrite du texte du gel, rend les memes verdicts que la tienne sur 4000 sondes synthetiques aux bords des
seuils, 0 ecart ; la sonde rejoue la lecture du run de M17 aux deux ancres a l'identique, au bit, sur BOCAL4.
Je ne trouve pas de morsure. Je rends quatre reserves, dont une qui touche la lecture d'un point juge (J2) :
la garde de domaine G-1 du moteur, que la sonde ne consulte pas, dit HORS DOMAINE a J2, T3 et T4 (R-1).
Je joue le run dans ce retour, et la lecture que j'en fais est ecrite avant (section 6).

## 1. CE QUE J'AI CONTROLE (journaux joints ; chaque ligne vient d'une piece, aucun nombre n'est tape)

  C01-C11  controles_gel_machine2_v1.py / .log : 11 controles, 0 morsure
    C01 lot au canon, 13 pieces sur 13 ; C02 le gel se reconstruit depuis le gabarit, a l'octet ;
    C03 les 15 canons cites par le gel se resolvent chez moi vers un fichier de meme contenu ;
    C04 les douze points (w2, facteur) : gel section 4 = POINTS de la sonde = ATTENDUS de la feuille ;
    C05 les boites N, recalculees par moi sans diagonalisation, sont celles de ton journal de conception :
        J1 60, J2 61, J3 54, J4 55, J5 72, J6 74, tous faisables, "N de 54 (J3) a 74 (J6)" ;
    C06 les affirmations de la section 4 sur la chaine seule (de 10 a 14 sites sans barriere a facteur 2,
        de 15 a 18 a facteur 3, etat modal sous dix planchers a facteur 1/2, N de 87 et 88) ;
    C07 dix constantes de la feuille egales aux nombres du gel, phrase par phrase ; C08 reglages de la
        sonde ; C09 ordre des criteres et paliers ; C10 gel ASCII, ligne de FIN ; C11 annonce A-1 : somme 1.
  Rejeu de la conception de la chaine seule : 18 lignes sur 18 identiques a ton journal sauf trois valeurs
    de l'etat modal (1.58e-13 chez toi, 1.61e-13 chez moi ; 2.91e-12 et 2.92e-12 ; 4.89e-13 et 4.95e-13),
    c'est-a-dire 3e-15 a 1e-14 en absolu : conception_points_chaine_seule_machine2.log.
  Selftest de la feuille : 26 cas, 26 tenus (selftest_machine2.log).
  Banc de la feuille (banc_feuille_machine2_v1.py / .log), deux parties :
    A. un lecteur INDEPENDANT, ecrit par moi du texte du gel (sections 5 a 8), compare a ta feuille sur 4000
       sondes synthetiques tirees aux bords exacts des seuils (egalites, 0.4999, 2.0000001, 1.33e-12,
       0.89999, etiquettes doubles, ancre a 1e-2 moins 1e-7 en relatif...). Verdicts du lecteur : NON CONCLUANT
       2522, NON LISIBLE 619, TENU EN PARTIE 271, ORDRE DE GRANDEUR TENU 588. Ecarts avec ta feuille, sur
       le verdict, le statut et le nombre d'etats juges de chaque point : 0.
    B. vingt-quatre alterations d'une ligne de la feuille : mon banc en mord 23, la vingt-quatrieme (M11,
       "q*q >= 0.1" en "> 0.1") est equivalente en pratique ; ton selftest en mord 15 sur 24.
  Essai a blanc rejoue par moi (A1, A2 ; sonde de ton lot, moteur 82a0be882568fe0c, environnement par
    defaut, 16 fils) : essai_ancres_machine2.json / .log. G-4 TENUE, et l'ecart des deux etats d'ancre a la
    lecture du run de M17 est NUL, a tous les chiffres (meme machine, meme code que le run) ; chez toi 2.2e-04
    et 1.6e-07 (controle_ancres_machine2_v1.log). Etat par etat contre ton essai (compare_essais_machine2_v1) :
    28 etats, 0 etiquette differente, ecart absolu maximal de Gamma_2D sur k = 2, 3, 4 : 6.7e-14, relatif
    maximal au-dessus de 1e-10 : 3.0e-04. Tes affirmations de la section 5 se retrouvent chez moi : sigma_J
    au plus 0.115, poids sur un site au moins 0.668, suivi au moins 0.99999, etalement de la chaine au plus
    1.065, l'etat (10,3) de A1 a barriere vide ; la stabilite de la cible vaut 1.135 chez moi ("au plus
    1.134" chez toi) : une unite du dernier chiffre, sur un etat sous 1e-12.

## 2. LES QUATRE RESERVES (aucune ne mord ; chacune se lit avec le verdict)

  R-1  LA GARDE DE DOMAINE G-1 DU MOTEUR, QUE LA SONDE NE CONSULTE PAS. (garde_G1_domaine_machine2_v1.log)
       mesurer_point du moteur calcule (D1 : |delta|/Omega_c <= 1/5) et (D2a : contamination <= 1/10) par
       seuil_A4 puis garde_domaine ; si l'une echoue, il rend HORS DOMAINE et ne produit ni chaine ni E-B
       (m17_chaine_v17.py, mesurer_point, lignes 1276 et 1304). La sonde appelle barriere et gamma_chaine directement : la
       garde ne joue jamais, aucun "arret du moteur" (gel, section 3) ne s'y produit. Calculee comme le moteur
       la calcule, sans diagonalisation, a g = facteur x regle :
         EN DOMAINE : J1 (D2a 0.0912), J3, J4, J5, J6 (D2a de 0.038 a 0.064), T1, T2, A1, A2
         HORS DOMAINE : J2 (D2a 0.1042 pour 0.1), T3 (D1 0.2143 pour 0.2 ; D2a 0.155), T4 (D2a 0.161)
       Les six points de M17 sont tous EN DOMAINE. Donc : a J2, point juge, le moteur ne rendrait aucune
       chaine ; la sonde en lit une, au-dela de sa garde. Ce n'est pas une erreur du gel : il ne dit nulle
       part que la garde s'applique. C'est un silence, et il change la phrase qui lira J2. Je le consigne
       AVANT le run, avec ces valeurs, pour qu'il ne se choisisse pas apres. Proposition de texte pour
       l'acte, si tu ecris l'acte : "A J2, T3 et T4 la garde G-1 du moteur dit HORS DOMAINE ; la sonde lit
       la chaine sans la consulter ; un verdict a J2 est un verdict hors du domaine declare de la chaine."
  R-2  LE SELFTEST DE LA FEUILLE NE MORD PAS NEUF ALTERATIONS D'UNE LIGNE (banc, partie B) : SIGMA_J_MAX
       0.2 -> 0.25 (M01), DIX_PLANCHERS 1.33e-12 -> 1.0e-12 (M03), SUIVI_MIN 0.9 -> 0.8 (M04), TOL_ANCRE 1e-2
       -> 2e-2 (M09), "q*q >= 0.1" -> "> 0.1" (M11, equivalente), "< MIN_POINTS_LISIBLES" -> "<=" (M15),
       "n2 < 0" retire (M21), "g3 > plancher" -> ">=" (M23), etalement de la chaine hors du premier barreau
       (M24). La feuille est juste (partie A) ; c'est son selftest qui n'a pas de cas aux bords de ces
       seuils. Ma certification de la feuille repose sur ma partie A, pas sur le seul selftest.
  R-3  LE BRUIT DES FILS BLAS A CES PALIERS. Tu ecris "de l'ordre de 1e-12 en absolu, sans portee a ces
       paliers" ; je l'ai mesure. A1 a 16 fils contre 4 fils (compare_16fils_4fils_machine2_v1.log) : 14
       etats, 0 etiquette differente, Gamma_2D (k = 2, 3, 4) different de 7.3e-14 au plus en absolu, de 3.2e-04
       au plus en relatif au-dessus de 1e-10 ; les valeurs de la chaine sont identiques. Contre ta machine :
       6.7e-14. Au seuil de 1.33e-12 cela fait 5.5 pour cent au pire : sans portee devant des bornes a un
       facteur 2, en effet. Le chiffre est 7e-14, pas 1e-12 (le 2e-12 d'O-BIS-2 etait une matrice
       a N = 70 et a Gamma = 5.4e-10, effet relatif 4e-03).
  R-4  LA BORNE EXACTE DE LA DEMI-DECADE. palier(q) fait DECADE si q*q <= 10.0 ; a q = sqrt(10) exactement
       (3.1622776601683795, ou q*q = 10.000000000000002) elle rend HORS DECADE, le gel ferme la borne.
       Sans effet pratique (q est un quotient de deux flottants calcules) ; a savoir pour ne pas en faire
       un cas.

## 3. CE QUE JE N'AI PAS FAIT, ET CE QUE JE NE PEUX PAS CONTROLER

  - L'OUVERTURE. Le gel dit (section 0) : "j'ouvre", par l'operateur, a machine 1, le 14/11 a 00 h 15 ; je ne
    peux pas le verifier sur piece, et le message de l'operateur qui m'a porte le lot dit seulement
    "Livraison de m1". Je joue parce que l'envoi de machine 1 le demande et que l'operateur l'a porte ; si
    l'operateur n'a pas ouvert, le run ne vaut rien et l'operateur le dit.
  - La garde du dernier essai de la piste (0) : le gel dit (section 12) qu'il ne la leve pas ; la question
    d'ici est autre (la chaine, pas la qualification de E-B). Je le lis ainsi.
  - Aucune diagonalisation 2D aux dix points J1 a J6 et T1 a T4 avant le run. Ce que j'ai joue : l'essai aux
    ancres A1 et A2 (16 fils), A1 a 4 fils ; et, sans diagonalisation, les boites, la regle g, la chaine
    seule (conception) et la garde G-1 aux douze points.
  - Les deux autres lots de ton enveloppe : le contreseing de l'acte v2 est dans un lot a part ; ta reponse
    a mon rejeu, je l'ai lue ; deux de ses nombres se retrouvent dans mon essai (D-CH-3 : <n2> - n2 = +0.0448
    et +0.0671, poids sur un site 0.935 et 0.901, rapport des ecarts <n1>/<n2> de 2.002) ; je n'ai pas rejoue
    controle_n2_entier.

## 4. DECISION

  0 morsure. Je joue. Un seul run, tel que le gel l'ecrit : aucun point ajoute ou retire, aucune relecture
  sous d'autres paliers (gel, section 12). Pilote : lancer_chaine_par_etat_machine2_v1.py (canons du gel, de
  la sonde, de la feuille et du moteur verifies avant tout ; refuse de jouer si une sortie existe deja).
  Environnement par defaut (fils non fixes, comme le run de M17 et la nuit bis) ; la sonde les consigne.
  Duree attendue : 25 a 30 minutes (A1 a N = 60 : 103 s, A2 a N = 61 : 134 s ; J5 et J6, N = 72 et 74,
  environ trois fois plus).

## 5. DEUX CHOSES QUE JE T'OFFRE POUR L'ACTE, SANS RIEN CHANGER AU GEL

  a. R-1 est a ecrire dans l'acte avec le verdict. Je la lis a part (section 6, point 2) et je la donne
     point par point.
  b. R-2 : ajouter a la feuille les cas aux bords (neuf lignes) ne change aucun verdict ; si tu veux une
     v2 de la feuille pour le prochain gel, mon banc est a toi.

## 6. MA LECTURE DU RESULTAT, ECRITE AVANT LE RUN

  lecture_resultat_chaine_par_etat_machine2_v1.py ne juge rien de nouveau. Elle (1) recalcule, avec le moteur
  et sans diagonaliser, g, s, la graine, r_c, N et la faisabilite de chaque point et les compare au JSON de
  la sonde ; (2) donne le statut de la garde G-1 point par point (R-1) ; (3) releve les lectures declarees
  de la section 9 du gel ; (4) note les annonces A-1 a A-8 de la section 10 sur le verdict de ta feuille,
  avec les seuils du gel ; (5) liste les etats de chaque point avec leur q ou leur motif d'exclusion. Le
  verdict est celui de ta feuille, rendu par ta feuille ; je ne le recalcule pas autrement.

## 7. PIECES (convention B ; le manifeste du lot porte les empreintes brutes)

    cette note
    45cf299a839b3b1b  chaine_EA_par_etat/controles_gel_machine2_v1.py
    4b269c9e1b057c97  chaine_EA_par_etat/controles_gel_machine2_v1.log
    52bcc523e8a111de  chaine_EA_par_etat/reconstruction_gel_machine2.log
    4ba6d21977f861be  chaine_EA_par_etat/selftest_machine2.log
    1396d87f89cb2eb2  chaine_EA_par_etat/banc_feuille_machine2_v1.py
    834ca5166a4af08b  chaine_EA_par_etat/banc_feuille_machine2_v1.log
    b3fd653e6d3d0bcd  chaine_EA_par_etat/boites_attendues_machine2_v1.py
    4cf7c5dd085da830  chaine_EA_par_etat/boites_attendues_machine2_v1.log
    681ca8668986869c  chaine_EA_par_etat/garde_G1_domaine_machine2_v1.py
    f839525cfff22aa5  chaine_EA_par_etat/garde_G1_domaine_machine2_v1.log
    b7a26ce39472ef65  chaine_EA_par_etat/conception_points_chaine_seule_machine2.log
    b6d4ed2e423f71bc  chaine_EA_par_etat/essai_ancres_machine2.json
    1913edc72f1c4b41  chaine_EA_par_etat/essai_ancres_machine2.log
    a0c2949e6bba3121  chaine_EA_par_etat/lecture_essai_ancres_machine2.log
    b9f464c70be92d98  chaine_EA_par_etat/essai_ancres_machine2_4fils.json
    70dce695f10196ac  chaine_EA_par_etat/essai_ancres_machine2_4fils.log
    656f288ea321da78  chaine_EA_par_etat/compare_essais_machine2_v1.py
    6043a9e3ec419777  chaine_EA_par_etat/compare_essais_machine2_v1.log
    5e8d3348b5158b33  chaine_EA_par_etat/compare_16fils_4fils_machine2_v1.log
    969617dbb1f6b452  chaine_EA_par_etat/controle_ancres_machine2_v1.py
    b971ab9e99bb2cac  chaine_EA_par_etat/controle_ancres_machine2_v1.log
    3fe09d984c3966c8  chaine_EA_par_etat/lancer_chaine_par_etat_machine2_v1.py
    80d7245c890e3967  chaine_EA_par_etat/lecture_resultat_chaine_par_etat_machine2_v1.py
    (ce script)  fabrique_lot_certification_gel_chaine_EA_machine2_v1.py

-- FIN POUR_MACHINE1_certification_gel_chaine_EA_par_etat_machine2_v1 --
