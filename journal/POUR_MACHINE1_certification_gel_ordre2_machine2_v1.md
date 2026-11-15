# POUR MACHINE 1 -- CERTIFICATION DU GEL "LA CHAINE E-A AU SECOND ORDRE", DE SA SONDE ET DE SA FEUILLE
# machine 2, v1, 2026-11-14. Entrant : ton lot 3bc363266957de56 (34 pieces sur 34 au canon, a l'empreinte
# brute et aux deux tailles) ; le gel 41153158190cf7f1, la sonde 24315c52b234319c, la feuille 0dc8241c680eb1ff,
# le bloc 7cd5977bc27bebc1.

## 0. EN QUATRE PHRASES

CERTIFIE, 0 morsure, avec des reserves (section 2). J'ai recalcule ton bloc A PART, sans en reprendre une ligne :
par une somme generique sur les 36 sauts de x^5, par un Lowdin lu sur la matrice H_2D du moteur, et contre l'energie
exacte a petit g ; Sigma2, u et t sont les tiens a 5e-13 pres, mon solveur le tien a 7e-9, et les quatre constantes
de G-8 sont retrouvees a 8e-12. Mon lecteur independant, ecrit du texte du gel, s'accorde avec ta feuille sur 4000
sondes synthetiques aux bords des seuils (0 ecart, les six issues de la cascade representees). Rien n'a ete joue
aux quatorze points neufs avant cette note (mes seuls calculs : la garde et la boite, sans diagonalisation, et
l'essai aux deux ancres, points connus) ; le run suit dans le meme retour.

## 1. CE QUE J'AI CONTROLE (pieces dans le lot ; chaque ligne vient d'un journal)

  a. Le lot : canon 3bc363266957de56, 34 pieces sur 34. TA construction rejouee par moi redonne le gel octet pour
     octet (C03, 23 canons poses) et la sonde 24315c52b234319c octet pour octet depuis la sonde du registre
     940a21b1d562bb49 et le bloc (tes 6 hunks) ; ton diff a 8 blocs, que j'applique par MON code, redonne la meme
     sonde (C04) ; aucune des 15 lignes otees n'est une ligne de mesure (docstring, table POINTS, dictionnaire de
     consignation), et aucune des 98 lignes ajoutees ne branche sur le statut de la garde ni ne porte un seuil
     (C05). Dans la feuille, les 13 instructions de motif_exclusion qui portent les huit criteres du gel precedent
     sont celles de la feuille du registre 0a760e3a244e547d au caractere pres, arbres ast (C06) ; tes trois criteres
     neufs (9) a (11) suivent. Ton R24, confirme.
  b. Controles de lecture, 22 : les 29 couples (nom, canon) de ta section 1 relus (8 au registre a 79e77d2, aux
     chemins donnes ; 2 hors registre ; 19 de ton lot) ; une seule empreinte non resolue chez moi, la note
     d'anteriorite 119f4e4dcbb4baba, qui ne m'a pas ete remise et dont le gel ne tire rien ; la cascade des sections 6
     et 7, que j'ai ecrite du TEXTE, enumeree sur les 3^12 = 531441 vecteurs de statuts (TENU, TOMBE, NON LISIBLE)
     des douze points juges, == ta fonction lire_bandes, verdict et issue de chaque bande (0 desaccord) ; A-1 somme a
     1.00, quinze annonces ; les quatorze couples (w2, facteur) juges et temoins sont neufs, les facteurs 3/4, 4/3 et
     1/2 n'ont ete joues a aucun w2 (28 couples joues, relus dans les deux JSON du registre et les six points de M17).
     Six de mes controles ont mordu au premier ou au deuxieme jet, tous par ma faute : un litteral flottant de G-8
     pris pour un canon et un plancher de comptes arbitraire (C02) ; la fin de la docstring de ta sonde mal reperee
     (C04b) ; un compte d'instructions de motif_exclusion que j'avais mal fait (C06) ; un regex d'annonce trop large
     (C08) ; un compte de lignes TIENT qui comptait le mot dans les verdicts (C11). Corriges, rejoues ; aucun
     n'a touche a ton gel, a ta sonde ni a ta feuille. Mes controles du bloc : quatre de mes criteres (C3, D1, E2,
     E5, E7) etaient trop serres pour l'arrondi de -2 Im E ou mal poses (u n'agit pas sur l'energie) ; je les ai
     relaches avec leur raison, dite dans le journal.
  c. TON BLOC (bloc_independant_machine2_v1.py, 17 controles, 0 morsure), comme tu me le demandes "sans me croire" :
     A. une somme generique sur les 36 sauts de x^5 depuis chaque site (canal compris, aucune parite supposee,
        aucune liste de 34), avec les elements ENTIERS du moteur : t, Sigma2 et u sont les tiens, ecart relatif
        maximal 0, 5.2e-13 et 4.6e-13 sur 122 etats (les deux ancres, 3 x 3 etiquettes voisines de la graine aux
        quatorze autres points), tous les sites ; les termes entre voisins, a trois et a quatre sites sont nuls
        (0), comme la parite et la portee le veulent ; Sigma2(0) est celui du moteur (Sigma2_site) a 4.5e-15.
     B. un Lowdin lu SUR LA MATRICE H_2D du moteur (x5, eta = 0, hermitienne ; aucun saut enumere par moi) :
        t 0, Sigma2 1.2e-14, u 5.2e-15, termes nuls 0, a cinq etats.
     C. l'energie : l'etat de plus grand recouvrement avec le site 0 du H_2D exact, contre ta chaine, a g, g/2 et
        g/4 : l'erreur relative sur dE passe de 7.5e-5 a 4.6e-6 (A1), de 4.5e-4 a 2.7e-5 (L3), un rapport de 16
        a chaque moitie de g (le signe de dE est donc le bon, et le developpement est a l'ordre annonce) ;
        l'ordre 1 est a 4 pour cent a 14 pour cent de dE, "u seul" aussi, "Sigma2 seul" est aussi bon que le
        complet : l'energie de l'etat central, a cet ordre, c'est Sigma2 ; le role de u (un saut de plus entre
        sites) n'est pas dans l'energie, et je ne l'ai pas isole sur la largeur : il l'est par E et par F.
     D. mon solveur sur mes tables, contre ton gamma_chaine_ordre2 sur les tiennes, 180 (etat, eta) : Gamma_flux
        7e-9, dE 2e-11, recouvrement 4e-13 ; -2 Im E (valeur consignee, non lue) differe de 4.7e-2 au plus aux
        largeurs de la fenetre de lecture et de 2.7 au-dessous de 1e-12 : c'est l'arrondi que ton (iv) declare.
     E. ta note, rejouee de mes sources : les 262 etats des deux JSON du registre, jugees par (1) a (8) et
        l'etiquette unique, 24 points ; mes q2 lus a -2 Im E sont ceux de ton tableau a 2.2e-3 des que
        Gamma_2D >= 1e-11 ; le gel (i) : q2 dans [0.998 ; 1.512] sur 243 etats, EXACT ; (ii) : 88, 118 et 37 etats,
        plus grands q2 1.101, 1.512 et 1.474, EXACT ; l'energie : mediane 0.0011, pire 0.0050, EXACT ; q1 de
        0.375 a 6.987 (tu ecris 7.00 : 0.2 pour cent, un etat a Gamma_2D 2.2e-12, l'arrondi de -2 Im E) ; "241 etats
        sur 243 dans un facteur 1.5" : j'en trouve 242, H2 (10,3) etant a 1.4948 ; 143 sur 243 dans un facteur 2
        au premier ordre, EXACT. Gamma_flux contre -2 Im E : mediane 1.2e-06 (tu : 1.5e-06), pire 1.4e-02 (1.6e-02).
     F. G-8 : ma chaine, mes tables, aux etats (7,2) et (8,2) : Gamma_flux 8e-12 et dE 1e-12 relatif de tes quatre
        constantes (lues dans le texte du gel).
  d. La garde et la boite, sans diagonaliser (garde_et_boites_machine2_v1.py) : les seize points, D1, c_max, site,
     statut et N, a six decimales, == la table de ta section 4, LUE dans le texte du gel (0 ecart) ; delta et bande
     recalcules == ceux de la table ; huit EN DOMAINE et quatre HORS DOMAINE parmi les douze juges. La garde est
     identique au bit a 16 fils (defaut) et a 1 fil.
  e. Le banc de la feuille (banc_feuille_ordre2_machine2_v1.py) : le lecteur independant lit le tableau, les bornes,
     les seuils, les canons et les quatre constantes d'ancre DANS LE TEXTE DU GEL ; ta table, tes bandes, tes bornes,
     tes seuils et tes references sont les siens ; 4000 sondes synthetiques aux bords des seuils, 0 ecart (verdicts
     du lecteur : NON CONCLUANT D'INSTRUMENT 873, NON LISIBLE 940, NE TIENT PAS 975, TIENT JUSQU'A 0.06 290, TIENT JUSQU'A 0.10 254, TIENT 668), verdict, issue de chaque bande, comparaison au pire etat, energies, lecture sans marge
     et etats gardes par la marge, puis a chaque point statut, nombre d'etats juges, motif de chaque etat, palier,
     q1 et q2 (min, median, max), pire ecart des deux ordres, plus grand ecart d'energie, loi apres coup,
     arithmetique. 115 alterations d'une ligne de ta feuille ; survivent a ton selftest : 22 ; survivent a mon banc : 3 ; le tout en une ligne : 115 alterations, survivent au selftest de machine 1 : [11, 14, 15, 22, 24, 28, 48, 56, 61, 66, 69, 70, 71, 72, 73, 83, 85, 91, 101, 109, 110, 114] ; survivent a mon banc : [45, 69, 109] ; survivent aux deux : [69, 109]. M069 (ecart d'energie <= 0.01 devenu < 0.01) ne differe que sur UN flottant, l'ecart exactement 0.01 : equivalente en pratique ; M109 (== NON LISIBLE devenu != NON TENUE) est equivalente, une bande qui n'est pas TENUE n'ayant que ces deux issues ; M045 (l'erreur du moteur sortie du critere (7)) est mordue par ton selftest et pas par mon banc, parce que mon lecteur, comme le gel, compte "erreur du moteur" et "barriere vide" au meme critere (7). Au premier jet mon banc en laissait survivre cinq (45, 56, 69, 109, 114) : M056 (les deux bords stricts de la borne, a l'egalite exacte en flottants) et M114 (une comparaison NON LISIBLE a moins de quatre points lisibles) venaient d'un trou de mon generateur, qui ne produisait ni l'egalite exacte ni les sondes a peu de points lisibles ; je les ai ajoutes et j'ai relance tout (le premier jet est joint).
  f. Les essais aux deux ancres, avec ta sonde : l'etat (7,2) de A1 et (8,2) de A2, une seule fois chacun, rendent
     la lecture de M17 au bit a 16 fils (0) et a 3.5e-4 a 1 fil (G-4 a 1e-2), tes references d'ordre 2 a 8e-11 et
     1e-12 (G-8 a 1e-3 et 1e-6) ; mon essai avec ta sonde retrouve, champ a champ, les 737 champs de mon essai avec
     la sonde certifiee (0 different) ; la garde consignee est EN DOMAINE aux deux, D1 et c_max ceux de la table.
     Contre le tien (autre machine : Windows, numpy 2.2.6, 16 coeurs ; toi : Linux, numpy 2.5.3, X86_V4) : memes
     etiquettes aux 28 etats ; Gamma_2D(3) differe de 1.7e-13 au plus sur tous les etats, de 7.7e-14 aux etats
     de Gamma_2D(3) > 1.33e-12 (R-3) ; Gamma_flux de l'ordre 2 aux etats juges differe de moins de 1e-9 : c'est ton choix
     de Gamma_flux qui tient (voir R-2).
  g. Ton selftest rejoue : 160 cas, 160 tenus ; ton banc rejoue sur ta feuille : table 131 sur 131, code 108 sur 109,
     survivante C82b ; ton releve rejoue sur MON clone du registre a 79e77d2 : 24 controles, 24 tenus.

## 2. RESERVES (aucune n'est une morsure)

  R-1  Ton selftest laisse passer des alterations que mon banc mord : 22 de mes 115 alterations passent ton selftest (11, 14, 15, 22, 24, 28, 48, 56, 61, 66, 69, 70, 71, 72, 73, 83, 85, 91, 101, 109, 110, 114) ; mon banc en mord 20 : les deux tolerances de G-8, B_LOI, trois lignes de la table (D1 de C1, c_max de L1 et de W2), l'etalement de la chaine du moteur a >= au lieu de >, les deux bords stricts de la borne, la mediane de q2, le denominateur de l'ecart d'energie, le signe de delta et la loi apres coup, deux lectures de flux / -2 Im E, le plus grand ecart d'energie lu en minimum, le doublon d'etiquette hors des criteres, l'ancre infaisable, la tolerance sur g, les ancres comptees parmi les points juges, la comparaison NON LISIBLE a moins de quatre points. Ce sont des trous de couverture du
       selftest (G-5), pas des defauts de la feuille, que ton selftest et mon banc lisent a l'identique sur 4000
       sondes. Ce qui tient ces lignes, c'est mon banc ; ta R-1 (la table dans le selftest) est tenue, comme ton
       banc le dit : les 131 alterations de table sont toutes mordues.
  R-2  -2 Im E de la chaine DU MOTEUR (q1, section 8) s'arrondit : entre ta machine et la mienne il differe de 0.2
       a 0.3 pour cent aux etats juges et de 4 a 19 pour cent aux etats de largeur de chaine 2e-13 ; Gamma_flux de
       l'ordre 2, lui, differe de 1e-9. Ton choix de Gamma_flux pour q2 est le bon ; q1 reste lu a -2 Im E, le
       moteur n'etant pas modifie, et la comparaison au pire etat n'en depend que si deux pires ecarts sont a moins
       de 0.3 pour cent l'un de l'autre.
  R-3  La marge d'un plancher (1.33e-13) vaut 1.7 fois le bruit que je mesure sur Gamma_2D(3) aux etats juges : 7.7e-14
       entre 16 et 1 fil sur ma machine, 6.7e-14 et 7.7e-14 contre ton essai (autre machine), 7.3e-14 au run precedent ;
       aux barreaux k = 2 et 4 il atteint 1.2e-13 (mes deux nombres de fils) et 1.7e-13 (contre toi). A la limite de
       Gamma_2D(3) = 1.33e-12 la marge est de dix pour cent. Apres le run, je lirai le verdict sous ce bruit et je le
       rendrai en lecture sans verdict, comme au gel precedent.
  R-4  Section 2 : deux chiffres de ta note differents des miens, l'un a 0.2 pour cent (7.00 contre 6.987), l'autre d'un
       etat (241 contre 242 sur 243) ; ils viennent de l'arrondi de -2 Im E a Gamma_2D de 2e-12 et rien ne s'y appuie.
  R-5  L'ouverture ("ok go", 14/11, 22 h 04) n'est pas verifiable sur piece par machine 2 ; ton gel le dit (section
       0). Le message de transmission de l'operateur le dit ou non.
  R-6  Ce que je ne verifie pas : le rattachement des deux termes a la litterature (tu le dis non verifie) ; la
       note d'anteriorite 119f4e4dcbb4baba ; les choix de la plume (bandes, bornes, points, comparaison au pire etat,
       tolerance d'energie 0.01) : ce sont les tiens, ecrits d'avance ; je verifie qu'ils sont dans le gel et dans
       la feuille, pas qu'ils sont les bons.

## 3. LE RUN

Si tu lis cette note, la certification rend 0 morsure : je joue la sonde aux SEIZE points, W2 compris (le
secteur est branche, 27.8 Go de memoire, 14.7 Go libres : la matrice de 7921 lignes de W2 tient), un seul passage
(48 decompositions ; a l'echelle de mes essais, A1 118 s a N = 60, A2 140 s a N = 61, en N puissance six : de
l'ordre de 2800 s pour les quinze premiers points, de 1300 s pour W2), puis la feuille, par un pilote qui ne decide
rien (lancer_ordre2_machine2_v1.py : canons, sonde, feuille, journal ; il refuse de rejouer si une sortie existe). Ma
lecture du resultat est ecrite AVANT le run (lecture_resultat_ordre2_machine2_v1.py : boites et garde recalculees,
annonces A-1 a A-15 jugees sans seuil nouveau) ; ma relecture independante du JSON (relecture_independante_...) et
ma lecture sous le bruit (stabilite_cascade_...) aussi. Le resultat est un lot a part.

## 4. PIECES (convention B ; le manifeste du lot porte les empreintes brutes)

    cette note
    f05ecff68b22e573  ordre2/controles_gel_ordre2_machine2_v1.py
    830b16e74f339795  ordre2/controles_gel_ordre2_machine2_v1.log
    d8f257237240d7ca  ordre2/controles_gel_ordre2_machine2_v1.json
    5efc87f10a6a68e0  ordre2/bloc_independant_machine2_v1.py
    2adf855b5aba5f50  ordre2/bloc_independant_machine2_v1.log
    79c920909c0bfea6  ordre2/garde_et_boites_machine2_v1.py
    9dd0fc58e38936e9  ordre2/garde_et_boites_machine2_v1.log
    7818d5eb2e540006  ordre2/garde_et_boites_machine2_1fil.log
    81d35a2be7170148  ordre2/banc_feuille_ordre2_machine2_v1.py
    04e47095995210c4  ordre2/banc_feuille_ordre2_machine2_v1.log
    e06c50cc4356bb0b  ordre2/banc_feuille_ordre2_machine2_v1_premier_jet.log
    aa20d5b9c2a59442  ordre2/essai_ancres_machine2.json
    e78553d3dee3b1e8  ordre2/essai_ancres_machine2.log
    ebdeca5f55c333b4  ordre2/lecture_essai_ancres_machine2.log
    3224522cec7b42b7  ordre2/essai_ancres_machine2_1fil.json
    68660645fe654fa4  ordre2/essai_ancres_machine2_1fil.log
    baa85a6d14cabeeb  ordre2/lecture_essai_ancres_machine2_1fil.log
    33585399bf8c0d9b  ordre2/compare_essais_16fils_machine1.log
    8e7d1be438d34c4b  ordre2/compare_essais_1fil_machine1.log
    3cbcac4b64fab103  ordre2/compare_essais_16fils_1fil_machine2.log
    094f1b1b0ea9a63c  ordre2/selftest_machine2.log
    cb13c118fad68112  ordre2/lancer_ordre2_machine2_v1.py
    d5469985a50f40d1  ordre2/lecture_resultat_ordre2_machine2_v1.py
    b3c5e91c67c76ec2  ordre2/relecture_independante_ordre2_machine2_v1.py
    09df1bcf560f61e8  ordre2/stabilite_cascade_machine2_v1.py
    (ce script)  fabrique_lot_certification_gel_ordre2_machine2_v1.py

-- FIN POUR_MACHINE1_certification_gel_ordre2_machine2_v1 --
