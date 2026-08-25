# JOURNAL -- DELTA 82 : LE RUN DE M17 EST JOUE, LE VERDICT EST PRONONCE
# Redaction machine 1 sur ordre operateur ("go") ; depot machine 2.
# Piece de registre. Aucun numero E pris (E18 : a l'acte).

Fichier  : journal_delta_82_run_M17.md
Date     : 25/08/2026
Redige   : machine 1 (valeurs RELEVEES de la note de run machine 2 et
           de ses pieces, jamais retapees de memoire ; mapping declare
           virgule-source -> point-ASCII ; re-derivations machine 1
           marquees comme telles). Empreintes convention B.

## 82.1 N-59 -- L'INSTRUMENT, EMPREINTE ET TAILLE, RELEVES AVANT LANCEMENT

    m17_chaine_v17.py   82a0be882568fe0c   103150 o   (CERTIFIE
      c344f55940a75772 ; releves a 23h09, avant le lancement)
    gel v12-b2          20950e52e7d63225    58507 o   (CERTIFIE
      de6f702f0d4b052e) ; E19 : l'ancre du script EGALE ce gel,
      certification croisee ANTERIEURE au depot -- chronologie opposable
    run : 24-25/08/2026, 23h09 -> 00h50, 1 h 41 de moteur, BOCAL4
    dossier manche_m17_v17/ ; MANIFEST 4aecd0e2b23bc818, 36 lignes
      (34 points + temoins_P7.json + assemblage.json), une empreinte
      par ligne ; log de run 76371babdf34bdf4 (exit=0)

## 82.2 LES COMPTES (formes derivees, relevees)

    grille : 0 repris + 34 calcules == 34 attendus : OK
    statuts COMPTES : 25 EN DOMAINE, 8 ARRET DE REGLE, 1 SITE EXACT
    gardes, toutes muettes -- premiere fois de la campagne :
      P7_sain = True (joue POUR DE VRAI sur le dossier de manche ;
      L_retenu = 20 lu du point NOMME ; cellules -4.203035e-14,
      marge 51.8 x, et -6.922631e-14, marge 32.6 x ; FREE = 0.0 exact)
      G-9 : 0 ; G-4 : 0 (NON APPLICABLE partout, p impair) ;
      ex aequo : 0 ; arrets_points [] ; arrets_sans_index [] ;
      carte PR-6 : 6 + 3 == 9 ; appariement PAR VALEUR (regle 11) ;
      ancres_manquantes() = [] ; E33..E36 consignes

## 82.3 LE VERDICT : PAS DE SIGNAL (cascade, branche 6)

Prononce -- pas un non-concluant : les deux primaires avaient leurs six
points, la barre etait franchissable, elles ne l'ont pas franchie.

  P3 (lien au registre classique, en rang) : ECHOUE
    rangs classiques [3, 2, 1, 4, 5, 6] ; quantiques [5, 3, 1, 2, 4, 6]
    rho = 5/7 ; rho_crit(6, 0.05) = 29/35 ; p_exact = 49/720
    RE-DERIVE machine 1 en exact depuis les rangs imprimes (enumeration
    des 720 permutations) : Somme d^2 = 10 -> rho = 5/7 ; queue exacte
    a 29/35 : 21/720 = 0.0292 ; cran inferieur 27/35 : 37/720 = 0.0514
    -- le seuil est bien la ; p_exact = 49/720 = 0.0681 > 0.05.
    L'echec est arithmetique.
  P6 (validation 2D) : ECHOUE
    (i) rho = 1/35 -- PLAT, pas limite ; lambda_c decroit de 1.2597 a
    0.90232 ; Gamma_LS creuse a 2.02 (6.562e-11) puis explose a 2.05
    (2.661e-09, trente fois les autres) : la largeur ne suit pas la
    barriere d'action sur cette grille
    (ii) violations = 0/6 (consigne en 82.4)
  Consignes (ne portent pas le verdict) :
    P2 gauche 0.97357, droite 1.01838 -- les deux cotes dans la bande
    P4 ecart-type 0.03008 contre bande 0.6 -- dans la bande, facteur 20
    P5 asymetrie 0/3 ; P8 non calculable (82.5.d)
  Lecture machine 2, portee comme LECTURE (hors gel) : les ECHELLES
  sont reproduites (P2, P4), les ORDRES ne le sont pas (P3 de peu,
  P6 pas du tout, P5 0/3). Lecture machine 1, marquee de meme : a
  n = 6 le P3 echoue dans l'epaisseur du trait ; le fait physique dur
  est le P6(i) plat et la resonance a 2.05 que la barriere ne voit pas.

## 82.4 L'ACQUISITION : LE CONTROLE EN SIGNE TIENT SUR LA GRILLE ENTIERE

Jumeau a signe RETOURNE (+1), meme geometrie, meme graine, meme
absorbeur, aux six points : -1.213e-14, +6.752e-15, +5.799e-14,
-1.322e-14, -6.503e-14, -7.550e-14 -- quatre a cinq ordres sous la
branche physique (8.44e-11 a 2.66e-09), LE SIGNE CHANGE d'un point a
l'autre : le plancher numerique, celui que P7 reconnait. La largeur
vient du SIGNE du fantome ; ni de la discretisation, ni de
l'absorbeur, ni de la graine. Premiere contre-epreuve complete de la
campagne. Ce que ca n'etablit pas, releve tel quel : que le fantome
existe -- la manche teste la COHERENCE de l'estimateur, pas le modele.

## 82.5 QUATRE FAITS DU RUN, CONSIGNES ET ROUTES A LA FILE

  (a) LE CHEMIN L = 30 A ETE PRIS, premiere fois (P8 g = 1e-3 : motif
      "erratum 4.6 : descente rejetee a L = 30 (bord de fenetre)" ;
      L = 20 dim 8100 PUIS L = 30 dim 10000 ; 67 minutes, la moitie de
      la manche). CONTREFACTUEL MESURE : sous v14/v15 ce point mourait
      par KeyError('G9_mordue') -- la manche entiere tombait a 00h50
      sans verdict. D-M17-31, exige et joue le soir meme, est ce qui a
      permis a ce run d'exister.
  (b) VINGT-QUATRE POINTS SUR TRENTE-QUATRE NE SONT JAMAIS LUS
      (compte : l'assembleur ingere site + P8 + f070 = 10 ; les
      fractions 0.50/0.85/1.00/1.20 sont calculees, ecrites, comptees
      en G-5, et aucune ligne ne les ouvre). QUESTION DE GEL, non
      tranchee ici : un lecteur, ou la sortie de grille.
  (c) SIX ARRETS QUE LA CASCADE NE VOIT PAS (les f050, stationnarite M
      jusqu'a 3.091e+285, descente non stationnaire budget 8 ; hors
      pts, hors arrets, hors branche 1). QUESTION DE GEL, non tranchee
      ici : consignation minimale a l'assemblage.
  (d) P8 NON CALCULABLE par construction (g = 3e-3 barriere VIDE ;
      1e-3 en arret ; 3e-4 infaisable, N_derive = 206 contre N_max =
      120 -- le gel estimait 231 en 4.11, mesure 206, ecart 11 pour
      cent). Ne participe pas au verdict (4.11) ; tout est consigne.

## 82.6 FILE DU PROCHAIN ACTE (numeros A L'ACTE, E18)

Les DIX-HUIT numeros de la certification v17 ; le defaut d'ordre v16
(leve) ; les faits (a)-(d) ci-dessus, dont DEUX questions de gel ; et
une faute de prose machine 1 a la premiere lecture du verdict (deux
nombres inventes en ecrivant -- "23/720", "26/720" -- contredits par
son propre calcul trois lignes plus haut ; les opposables sont 21/720
et 49/720, re-derives ; versee par machine 1 contre elle-meme).

## 82.7 PIECES (convention B ; detenteur declare)

    note_machine2_run_M17_v1.md              (copie recue fc905d9b195c2a76)
    manche_m17_v17_MANIFEST_machine2.txt     4aecd0e2b23bc818   1577
    run_manche_v17_machine2_v1.log           76371babdf34bdf4     87
      (copie recue 76371babdf34bdf4, 87 o)
    manche_m17_v17/assemblage.json           0be34834c78d1fcf   1846
    manche_m17_v17/temoins_P7.json           28a840cf73a18730    710
    manche_m17_v17/pt_39_20_f070.json        bd012b6b08b56d25   4794
    manche_m17_v17/pt_39_20_P8_g0.001.json   85b167b7ca7724c8   4260
    m17_chaine_v17.py                        82a0be882568fe0c 103150
    m17_pre_enregistrement_quantique_v12_b2.md 20950e52e7d63225 58507
    pr6_carte_classique_etendue_v1.json      d32761567d24024f   3600
    controleur m2 de la note de run          a0aa97e64be4ffd5   5633
    re-derivation P3 machine 1               (dans la conversation du
      25/08 ; enumeration exacte des 720 permutations)

Depot : machine 2, au registre, a sa main. La note de run porte que
son empreinte se prend a l'acte ; la presente piece cite sa COPIE
RECUE et le declare.

-- FIN journal_delta_82_run_M17 --
