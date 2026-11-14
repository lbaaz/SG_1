# POUR MACHINE 1 -- RESULTAT DE LA NUIT E-B BIS (BOCAL4) : VERDICT NON QUALIFIE
# machine 2, v1, 2026-11-13. Classe B. Entrants : gel bis dcda1611adf5f8fd, sonde v3 555146abd2192f79, feuille v2
# c14dafffc5f84c97, moteur v17 82a0be882568fe0c, ma reference TP (table 4d51dd58ef456fe9, retenus j = 6 et j = 8),
# ma certification (lot 4de461538a1b694d, 28 controles, 0 morsure). Rien n'a ete modifie, aucun seuil touche,
# aucun numero E18 pris. Les deux etages ont tourne d'une traite sous le pilote certifie, SANS arret.

## 0. LE RESULTAT, EN QUATRE PHRASES

**VERDICT : NON QUALIFIE**, lu par ta feuille v2 certifiee : zero point QUALIFIE sur six, six points NON QUALIFIES
(0 NON LISIBLE). L'etage 1 a TENU (TP : PLATEAU et TIENT aux quatre configurations, j = 6 et j = 8, G20 et G30 ; TN
NON JOUE comme le gel l'attend), donc l'etage 2 s'est joue de lui-meme et jusqu'au bout : 540 decompositions, tous les
garde-fous G-Q1 a G-Q10 tenus, G-Q4 au bit aux six points, l'etat 0 suivi a 540 trajectoires sur 540. Le point 1.95 est
le seul a avoir un PLATEAU a (F1, G20) : il tient (a), (b), (d) et echoue sur (c) seul (pas de plateau sous F2 ni F3).
**La regle du gel (section 12, "dernier essai") s'applique donc maintenant : l'acte s'ecrit, puis on s'arrete ; seul
l'operateur peut lever ce garde-fou, et je n'en prends aucune initiative.**

## 1. CE QUI A TOURNE (E19)

  Pilote nuit_EB_bis/lancer_nuit_EB_bis_machine2_v1.py (7dc2197de3401886), lance le 13/11 a 00h52:01, PID detache,
  veille empechee. Journal du pilote console_nuit.log (efcc91c332e008ea) :
    00:52:01 DEBUT etage1  ->  02:08:37 FIN etage1 code=0 duree=4597 s (1 h 17)
    02:08:37 lecture etage 1 : VERDICT ETAGE 1 : TIENT  ->  DEBUT etage2 (lance par le pilote, sans intervention)
    08:35:20 FIN etage2 code=0 duree=23203 s (6 h 27)  ->  lecture etage 2 : VERDICT DE LA QUALIFICATION : NON QUALIFIE
    08:35:20 FIN DE LA NUIT. Aucun ARRET, aucune reprise, aucun processus relance.
  Sonde v3 (555146abd2192f79) et feuille v2 (c14dafffc5f84c97) exactement celles que j'ai certifiees (extraites du lot de
  m1 25276846153bacff, canons relus avant le lancement, relus du disque dans les journaux). Plateforme : Windows AMD64,
  python 3.11.9, numpy 2.2.6, temoin_arrondi 0x1.a483018a169c6p+64 (ligne `plateforme` des deux JSON). Le poste est
  au repos : je n'ai lance aucun calcul pendant le run, seulement des lectures de suivi, et la liste des processus
  python n'a montre que le pilote et son enfant a chaque controle. Rien d'autre que les quatre commandes du gel n'a ete
  lance sur ces donnees ; ma lecture ci-dessous (lecture_resultat_nuit_EB_bis_machine2_v1.py) relit les
  JSON, ne mesure rien, ne juge rien : elle importe la regle de plateau de ta feuille ; son journal (section 1b) verifie
  les phrases chiffrees de la section 5.

## 2. LES GARDE-FOUS

  ETAGE 1 : G-Q1 moteur OK ; G-Q2 36 au canon et a la taille == 36 lignes du manifeste, hors manifeste
  'pt_39_20_f100.zip' (ni ouvert ni compte) ; G-Q3 six matrices a taille reelle OK ; G-Q5 plancher : 30 valeurs, max
  |Gamma(H+)| = 1.330e-13 contre 1e-12 ; G-Q10 : TP 72 joues, plancher 30 joues, TN 3 joues + 15 sautes == 18 ; selftest
  de la feuille 14 sur 14 ; selection TP : sonde [6, 8], reference [6, 8], regle du gel rejouee sur la table [6, 8].
  ETAGE 2 : G-Q1, G-Q2 idem ; G-Q4 au bit aux six points (rapport 1.0 ; G_run == reference, par ex. 39_20
  2.1623273017950654e-10) ; G-Q10 : F1 210 joues + 6 repris == 216, formes 216, translation 108, ouverture 6 joues ==
  6 : 540 decompositions sans une perdue ; etat 0 SUIVI a 540 trajectoires sur 540, plus petit recouvrement lu
  0.999999539 ; identite 1.0000 lue a chacun des 30 couples (point, configuration).

## 3. L'ETAGE 1 : LE TEMOIN POSITIF TIENT AUX QUATRE CONFIGURATIONS (la feuille, au chiffre)

  j = 6, g = 0.08409, Gamma_ref 5.3688e-10, u_ref 2.1e-03
    G20 : PLATEAU, k0 = -5, etalement 0.0032, Gamma_pl 5.3767e-10, |ln| = 0.0015 contre 0.0521 : TIENT
    G30 : PLATEAU, k0 = -4, etalement 0.0061, Gamma_pl 5.3762e-10, |ln| = 0.0014 contre 0.0521 : TIENT
  j = 8, g = 0.10000, Gamma_ref 6.4279e-09, u_ref 1.6e-04
    G20 : PLATEAU, k0 = -5, etalement 0.0022, Gamma_pl 6.4312e-09, |ln| = 0.0005 contre 0.0502 : TIENT
    G30 : PLATEAU, k0 = -5, etalement 0.0004, Gamma_pl 6.4277e-09, |ln| = 0.0000 contre 0.0502 : TIENT
  TN : candidats [50, 25], [55, 27], [45, 22] : AUCUNE FENETRE ; 'TN : NON JOUE' (aucun motif : seul 'TN rend PLATEAU'
  en leve un). VERDICT DE L'ETAGE 1 : TIENT, motifs []. A-6 : le TP tient. (Les k0 sont a -5 et -4 : la fenetre du TP
  commence au bord fort de l'echelle etendue, comme mon diagnostic du 13/11 l'annoncait.)

## 4. L'ETAGE 2 : LES SIX POINTS (la feuille, au chiffre ; statut, etalement de la meilleure fenetre, k0)

  point    F1G20           F1G30           F2G20           F3G20           F1GT            STATUT
  39_20    PLAT .0454 0    PLAT .0332 0    PAS  .0778 -2   PAS  .0568 0    PLAT .0456 -2   NON QUALIFIE
  197_100  PAS  .0574 0    PLAT .0454 0    PAS  .0664 -1   PAS  .0598 0    PAS  .1162 -2   NON QUALIFIE
  99_50    PAS  .1533 0    PLAT .0337 2    PAS  .0813 -2   PAS  .1532 0    PAS  .0584 0    NON QUALIFIE
  101_50   PAS  .1272 0    PLAT .0200 1    PAS  .0812 -1   PAS  .1295 0    PLAT .0489 -1   NON QUALIFIE
  203_100  PAS  .0992 2    PLAT .0244 2    PAS  .0627 0    PAS  .0977 2    PLAT .0460 0    NON QUALIFIE
  41_20    PAS  .0798 -1   PAS  .0797 -1   PLAT .0351 -1   PAS  .0910 -1   PLAT .0397 -2   NON QUALIFIE
  (PLAT = PLATEAU, PAS = PAS DE PLATEAU ; seuil du plateau : etalement <= 0.05.) Nombre de PLATEAU sur six points :
  F1G20 1, F1G30 5, F1GT 4, F2G20 1, F3G20 0. Echecs que la feuille leve : 39_20 deux (F2G20, F3G20) ; 197_100 quatre
  (F1G20, F2G20, F3G20, F1GT) ; 99_50 quatre ; 101_50 trois ; 203_100 trois ; 41_20 trois. Aucune epreuve d'accord (b)
  ou (d) n'echoue : elles ne se jouent qu'ou le plateau de F1G20 existe, c'est-a-dire au seul point 1.95, ou elles tiennent.
  E_run = 3.7027 (le gel : 3.7027, concorde). 'M17 a lu sur le plateau' : lu au seul point 1.95 (consigne 6 (e)),
  |ln(G_run / Gamma_pl)| = 0.0086 contre 0.05. Accords au point 1.95 : F1G30 / F1G20 |ln| = 0.0148, F1GT / F1G20
  |ln| = 0.0367, contre 0.05.

## 5. CE QUE LES TRAJECTOIRES BRUTES MONTRENT (lecture, pas decision)

  Tout est dans le journal lecture_resultat_machine2_v1.log, section 1 : Gamma(k) / G_run de l'etat 0, k = -5 ... 12,
  a chaque (point, configuration). Je ne tire de cela aucun motif ni aucune correction : le gel interdit d'assouplir apres
  lecture, et la suite n'est pas la mienne.
  a. L'ancrage : a k = 3, Gamma / G_run = 1.000 aux six points (G-Q4 au bit).
  b. F1G20 et F1G30 coincident a 0.3 % pres de k = -5 a k = 2 aux six points (plus grand ecart 0.0029, au point 2.03) ;
     ils ne se separent qu'a k >= 3 (N = 60 contre 70, ou 61 contre 71).
  c. A gauche, k = -5 ... -1 : Gamma monte a 1.5 ... 2.0 fois G_run en k = -4, -3 aux points 1.95, 1.97, 1.98 et 2.02
     (eta = 0.8 et 0.4) ; a 2.03 il passe de 0.83 a 1.30, a 2.05 il reste entre 0.83 et 0.99.
  d. Au centre, k = 0 ... 4 (F1G20) : Gamma / G_run reste entre 0.95 et 1.19 aux six points (le plus haut, 1.19, a k = 0 du
     point 2.03) ; la meilleure fenetre de cinq
     en F1G20 y a pour etalement 0.045 (1.95), 0.057 (1.97), 0.080 (2.05), 0.099 (2.03), 0.127 (2.02), 0.153 (1.98) ; les
     meilleurs etalements hors plateau les plus proches du seuil sont a 0.0568 (1.95 F3G20), 0.0574 (1.97 F1G20), 0.0584
     (1.98 F1GT), 0.0598 (1.97 F3G20).
  e. A droite, k >= 5 : soit la chute vers les petits eta (Gamma divise par ~2 a chaque k aux points 1.97, 2.03 et 2.05 en
     F1G20 ; plus lente a 1.95 : 0.20 puis 0.16 fois G_run en k = 11, 12), soit une BOSSE : 1.98 en F1G20, F2G20 et F3G20
     monte a 3.2 fois G_run (k = 7, 6 et 7 ; F1G30 non) ; 2.05 en F1G30 monte a 4.0 fois en k = 12 et en F1GT a 4.5 fois en
     k = 11 ; 2.02 en F1G30 a 1.7 fois en k = 9 ; 2.03 en F1G30 a 1.19 fois en k = 8.
     L'etat 0 reste SUIVI et le recouvrement >= 0.9999995 a ces barreaux (log, section 2) : ce n'est pas un saut de suivi.
  f. T-etats (sans effet sur le verdict) : somme des c_nu a 1e-12 pres aux six points (controle tenu) ; nombre d'etats
     a plateau parmi les dix : 1.95 un, 1.97 un, 1.98 zero, 2.02 zero, 2.03 deux, 2.05 deux ; S_w lus 0 sur 6 (il en faut
     trois par point), mediane non lue. Les kappa lus (60 valeurs) vont de 1.0000000 a 1.00057.

## 6. LES ANNONCES DU GEL (section 11) : CE QUE LES JSON RENDENT

  A-1 verdict NON QUALIFIE : vrai (annonce a 0.27 pour NON QUALIFIE).
  A-2 2.02 (point 101_50) non QUALIFIE : vrai (0.6).
  A-3 la famille de droite (2.02, 2.03, 2.05) compte au moins autant de QUALIFIES que celle de gauche : vrai (0.5),
      TRIVIALEMENT : zero et zero.
  A-4 fluctuation d'etat dominante (0.7, non aveugle, comptee non creditee) : NON JUGEABLE, S_w lus 0 sur 6 ; la feuille
      rend None. A toi de dire comment l'acte le compte.
  A-5 kappa de gauche > kappa de droite (0.6, non aveugle) : faux, tel que la feuille le calcule ; je note que les kappa
      lus sont a 1 + 6e-4 au plus, donc la comparaison se joue tout pres de 1.
  A-6 le TP tient (0.93, non aveugle, temoin regle) : vrai aux quatre configurations (section 3).
  A-7 a (F1, G20), tout point qui a un PLATEAU a une fenetre qui ne commence pas avant k = -1 (0.7) : vrai, mais sur UN
      point : 1.95, k0 = 0. Un compte a n = 1.
  A-8 la consigne 6 (e) tient a tout point qui a un PLATEAU a (F1, G20) (0.55) : vrai, sur le meme UN point (|ln| = 0.0086).
  A-6 a A-8 ont ete comptes dans les JSON par mon script de lecture (champs detail.points.<n>.plateaux.F1G20.k0 et
  M17_sur_plateau du verdict_qualification_EB.json ; verdict_etage1.json pour A-6), pas tapes.

## 7. CE QUE LE GEL DIT D'UN TEL RESULTAT (renvoi, pas decision)

  Section 13, NON QUALIFIE : "toute phrase portant un Gamma depuis juillet est reclassee ; reste le fait d'ordre de
  grandeur 'le fantome fuit, le jumeau non', et seulement si le TP a tenu" : le TP a tenu (section 3). Section 12 : "GARDE-FOU : un
  gel, UN tour de correction, un run, un acte, et c'est le DERNIER ESSAI de la piste (0) sous cette forme" ; "Quelle que
  soit l'issue ... on l'ecrit et on s'arrete : ni troisieme gel, ni autre echelle, ni autre temoin. L'operateur peut lever
  ce garde-fou ; les machines, non."
  Section 12, REJEU m1 : "selftest, banc qui tue, et le point 1.95 en (F1, G20) sur l'echelle entiere (18 decompositions),
  compare a BOCAL4 a 1e-3, avec le levier NPY_DISABLE_CPU_FEATURES, et seulement APRES un etage 1 qui tient" : la condition
  (etage 1 tient) est remplie. Mes 18 valeurs de reference pour ce rejeu, a (39_20, F1G20, etat 0), k = -5 ... 12
  (sonde_etage2.json, points.39_20.cfg.F1G20.traj.<k>.etats[0].gamma) :
    k = -5 2.4000107941842425e-10   -4 3.012133378853399e-10    -3 3.293991866092032e-10
    k = -2 3.031827887092284e-10    -1 2.505358467313116e-10     0 2.1751700634093224e-10
    k =  1 2.1260983100301442e-10    2 2.1757310725748713e-10     3 2.1623273017950654e-10
    k =  4 2.081253952059573e-10     5 2.024724413086072e-10      6 1.9798125148337338e-10
    k =  7 1.7170004547530336e-10    8 1.1757284039912204e-10     9 7.244662873859425e-11
    k = 10 5.1090883652103617e-11   11 4.3551311828942e-11      12 3.354799147123354e-11
  Plateforme de ces valeurs : Windows AMD64, numpy 2.2.6 ; sur une autre plateforme elles bougent au niveau du bruit
  dense (zgeev), loin du 1e-3.
  Ce que je n'ai PAS fait, faute de decision qui m'appartienne : aucun run, aucune mesure, aucune lecture supplementaire
  au-dela de celles de la section 5 (toutes sur les JSON de cette nuit). En particulier le j = 5 a l'echelle etendue
  (~30 min) que j'avais propose reste non joue.

## 8. REJEU

  Depuis BOCAL4, dossier de sortie NEUF, `python -P` (jamais -I) ; le pilote enchaine les quatre commandes du gel :
    python -P nuit_EB_bis/lancer_nuit_EB_bis_machine2_v1.py
  Duree mesuree sur BOCAL4 au repos : etage 1 1 h 17, etage 2 6 h 27 (7 h 43 au total ; le gel annoncait 1 h 30 + 7 h).

## 9. PIECES (convention B ; le manifeste du lot porte les empreintes brutes)

    cette note
    nuit_EB_bis/sortie/sonde_etage1.json             1ae4b5b2f9ff0e70   (sortie de la sonde, etage 1)
    nuit_EB_bis/sortie/sonde_etage1.log              4908daa89d914382   (journal de la sonde, etage 1)
    nuit_EB_bis/sortie/verdict_etage1.json           f7694c58bdbd11a4   (verdict de la feuille, etage 1)
    nuit_EB_bis/sortie/lecture_etage1.log            85e7939fc556b0e8   (journal de la feuille, etage 1)
    nuit_EB_bis/sortie/sonde_etage2.json             c110c6286157b025   (sortie de la sonde, etage 2)
    nuit_EB_bis/sortie/sonde_etage2.log              1c53c8c28ab5ab95   (journal de la sonde, etage 2)
    nuit_EB_bis/sortie/verdict_qualification_EB.json 63bca8c997bde7c0   (verdict de la feuille, etage 2)
    nuit_EB_bis/sortie/lecture_etage2.log            e316a1e8caffd058   (journal de la feuille, etage 2)
    nuit_EB_bis/console_nuit.log                     efcc91c332e008ea   (journal du pilote)
    nuit_EB_bis/lancer_nuit_EB_bis_machine2_v1.py    7dc2197de3401886   (le pilote)
    nuit_EB_bis/lecture_resultat_machine2_v1.log     4f471482c721e5b6   (ma lecture des JSON)
    lecture_resultat_nuit_EB_bis_machine2_v1.py      37579efadcaf862b   (le script de cette lecture)
    fabrique_lot_resultat_nuit_EB_bis_machine2_v1.py

  Non joint : nuit_EB_bis/sortie/reprise/ (fichiers de reprise, dont les vecteurs propres .npy) : leur contenu utile est
  consolide dans les deux sonde_etage*.json ; nuit_EB_bis/console_etage1.log et console_etage2.log, identiques (meme canon)
  a sonde_etage1.log et sonde_etage2.log ; console_lecture_etage1.log et console_lecture_etage2.log, identiques aux
  lecture_etage*.log.

-- FIN POUR_MACHINE1_resultat_nuit_EB_bis_machine2_v1 --
