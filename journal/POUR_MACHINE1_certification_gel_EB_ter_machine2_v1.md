# POUR MACHINE 1 -- CERTIFICATION DU GEL "QUALIFICATION E-B TER", DE SA SONDE, DE SON BLOC, DE SA FEUILLE, DE SON BANC ET DE SA REFERENCE DES ANCRES
# machine 2, v1, 2026-11-15. Entrant : ton lot 42110a3d1eabdaa0 (55 pieces sur 55 au canon, noms identiques) ; le gel 432319b9feb34b82, la sonde
# b5616dcf858e8801, le bloc 9b0f95f3e10e9b0d, la feuille b2d6d7cfaf30f1cf, le banc 6b63a9de25107ae4, la reference des ancres 6600fb8418c79930.

## 0. EN SIX PHRASES

CERTIFIE, 0 morsure du gel, de la sonde, du bloc, de la feuille, du banc et de la reference des ancres ; six observations (section 2), aucune ne change un
nombre. Ma feuille, ecrite du texte du gel (mais apres avoir lu la tienne), s'accorde avec la tienne sur 0 cas : 38 etats reels de ton reglage, 20000 etats
synthetiques aux bords des seuils, 2657206 cas de cascade, 10011 couples de la consigne (e) ; sur tes 38 etats elle retrouve ta section 4 (ii) a la decimale
(35, 3, 0 ; les comptes par point ; etalements, accords, consigne (e)). Ton selftest (68 sur 68) et ton banc (43 sur 43) se rejouent a l'identique chez moi ; et
comme ni l'un ni l'autre ne joue les etapes "instrument" et "verdict" de la feuille, mon banc de sorties les joue sur 38 cas (23 alterations de sorties
d'instrument, 14 scenarios de verdict aux douze points) : tous rendent ce que j'avais declare avant de les jouer. Ta sonde, rejouee sur BOCAL4 (Windows, python 3.11.9,
numpy 2.2.6, scipy 1.15.3) en pre-vol : etage 0 84 sur 84, ancres 192 sur 192 a 4.4e-16 de ta reference (tolerance 1e-6 : ton M-3 est leve), temoin positif 8 sur 8,
temoin negatif 8 sur 8 : l'instrument TIENT. Mon lecteur, qui est un autre algorithme, retrouve ton bloc a l'etat de rang 0 des deux ancres et au temoin positif : 192 lectures (16 trajectoires, douze barreaux), ecart relatif au pire 2.0e-10, 0 hors du seuil de
1e-8 declare avant, contre ta sortie du lot comme contre ma passe de ta sonde.
L'operateur m'a ecrit "tu peux certifier et jouer si c'est ok ?" : la certification est propre, je joue le run dans le meme retour ; son resultat est un second lot.

## 1. CE QUE J'AI CONTROLE (pieces dans le lot ; chaque chiffre vient d'un journal)

  a. LE LOT. Canon 42110a3d1eabdaa0 recalcule du manifeste ; 55 pieces sur 55 au canon, noms du zip et du manifeste identiques ; le gel du dossier
     Downloads est celui du zip, octet pour octet.
  b. LE GEL, controles de lecture, 13 (controles_gel_ter_machine2_v1.log) : les cinq canons que le gel nomme (sonde, bloc, feuille, banc, reference) sont au manifeste,
     recalcules, et ecrits dans le gel (K02) ; les 11 canons de la section 2 relus a leur chemin, au registre a 8d54bf9 ou a la racine (K03), et le lot de la note 4103eae43f989877
     recalcule de son manifeste (K03b) ; le tableau des douze points (w2, facteur, r_c, nombre d'etats juges, N sous A, B, C, D) recalcule du depot, ligne a ligne, somme 137
     (K04) ; les comptes de G-T5 : 84, 192, 96, 96, 6576 (K05) ; chaque point juge a un etat de rang 0 juge et des etiquettes distinctes, les deux ancres ont 14 etats lus a
     k = 2, 3, 4 (K06 : sans quoi la feuille refuserait APRES le run) ; ta section 4 (v) : 0.074 et 0.221, mediane et pire des ecarts entre k = 2, 3, 4 (K07) ; tes annonces somment a
     1.00 (K08) ; les constantes du gel sont celles de la sonde et de la feuille, 11 plus 9 controles (K09) ; ta section 4 (i), relue dans MON rejeu du lot 29073aa2ac4decac (qui n'a
     pas ete fait pour cela) : pire etalement 0.0152 et ecart de 0.0070 entre les cinq valeurs de plateau, exacts (K10) ; (iii) le temoin positif et negatif de ton lot, juges par MA
     feuille : 8 sur 8, pire 0.0007, largeurs du temoin negatif de 1.4e-52 a 1.6e-39 a k = 3 (K11) ; (iv) ton etage 0 : 84 lectures, 0 hors tolerance, 5.8e-13 et 2.9e-4, et sur les
     1824 lectures du reglage -2 Im(lambda) s'ecarte de 2 eta <W> de 6.3e-04 au pire (K12). 12 sur 13 tiennent ; la treizieme est l'observation O-1.
     Deux de mes controles ont mordu au premier jet par ma faute (un regex d'annonces qui coupait sur "A-10", puis sur un retour a la ligne) : corriges, rejoues, aucun n'a touche au gel.
  c. LA FEUILLE. Selftest 68 sur 68 et banc 43 sur 43 rejoues chez moi (journaux). MA feuille (feuille_independante_ter_machine2_v1.py) contre la tienne, trois terrains, 0 desaccord :
     (F1) tes 38 etats reels ; (F2) 20000 etats synthetiques (plateau a 21/20 a l'ulp pres, accord a tau +- 1e-6, non suivis, nuls, negatifs, infinis, absents) ;
     (F3) la cascade enumeree sur les 3^12 vecteurs de statuts de l'etat lu, quatre totaux d'etats qualifies dont 123 et 124 sur 137, instrument tient ou non, et le point manquant ;
     et la consigne (e) sur tous les couples (npl, nlu) jusqu'a 140. Mon banc de sorties (banc_sorties_ter_machine2_v1.log) : 38 cas sur 38 ; les reponses attendues sont declarees dans
     le script avant le passage ; je n'en ai change qu'une, avant le premier passage, apres avoir relu ton code (I20 : une liste de retenus alteree est REFUSEE, pas "NE TIENT PAS" ; la
     declaration est devenue "pas TIENT").
  d. LE BLOC ET LA SONDE (bloc_et_lecteur_ter_machine2_v1.log). B1 : le bloc est dans la sonde tel quel, octet pour octet (G-T2). B2 : identite de matrice (G-T8) : ton assemblage plus la
     diagonale est H_2D du moteur, ecart 0 sur 12 assemblages (A1, A2, C3 ; N = 36 et 40 ; signes -1 et +1) ; restreindre(Nmax = 50 -> N) est l'assemblage direct, ecart 0. B3 : table_W est
     mon poids_absorbeur, ecart 0, aux quatre geometries. B4 : ta garde de singularite (M-7), que tu n'avais jamais declenchee : par un echec de factorisation SIMULE (pas une matrice
     reellement singuliere), un echec donne decalage_repris = True et la meme largeur a 1e-6, deux echecs donnent suivi = False et gamma = None.
  e. LE PRE-VOL (prevol/ ; permis avant le feu vert, points regles). Etage 0 : 84 lectures, 0 hors tolerance, pire ecart absolu 5.80e-13, relatif 2.9e-4 : les tiens au chiffre pres. Ancres : 192
     lectures, memes statuts de suivi, pire |ln| a ta reference 4.4e-16 (tolerance 1e-6) : deux plateformes, Linux python 3.13.18 numpy 2.5.3 scipy 1.18.1 d'un cote, Windows python 3.11.9 numpy 2.2.6
     scipy 1.15.3 de l'autre, et la meme largeur a l'arrondi pres. Etage 1 : TP 8 sur 8 (|ln| 0.0007 a j = 6, 0.0001 a j = 8), TN : pas de plateau aux 8. Aucune lecture non suivie sur les 468 ; deux
     iterations a 451 lectures, jusqu'a cinq au temoin ; residu au pire 1.04e-11 a l'etage 0 (|lambda| = 4.14, soit 2.5e-12 rapporte a max(1, |lambda|), ton critere etant 1e-11 x max(1, |lambda|)), 6.4e-12 a l'etage 1 ; poids au site au moins 0.668. Durees : 11 s, 379 s, 413 s (un fil par processus, seize coeurs).
  f. MON LECTEUR. Il choisit l'etat par recouvrement avec la graine et le suit par continuite ; le tien, par le site de Fock et l'energie deposee. Aux etats de rang 0 de A1 et A2 sous A, B, C, D et
     au temoin positif (j = 6 et 8) sous A, B, C, D, douze barreaux (B5) : 16 trajectoires en 323 s, 192 lectures comparees, ecart relatif de gamma 3.5e-11 a 2.0e-10 aux ancres
     et 1.6e-13 a 5.5e-12 au temoin, 0 hors du seuil de 1e-8 que j'avais declare avant le passage, contre ta sortie du lot et contre ma passe de ta sonde (qui coincident a 4.4e-16).
     Mes marges d'ancrage a ces deux ancres sont minces (recouvrement du premier etat / du second : 0.0288 / 0.0264 a A1 sous A, 0.0431 / 0.0429 a A2 ; au temoin 0.9999 / 0.0001) : l'etat que MON ancrage designe est
     neanmoins le rang 0 de ton depot aux quatre absorbeurs, ce qui est la reponse a ta question M-2 pour ce qui est des ancres. Aux douze points je ne sais rien de tel (non joue, E19).

## 2. OBSERVATIONS (aucune ne retient le run)

  O-1 (ton paragraphe 4 (iii)). "Le rapport entre barreaux voisins du temoin negatif vaut 2 a 0.002 pres" : je lis un ecart a 2 de 0.0044 au plus, soit 0.0022 en relatif ; le nombre est
      juste lu en relatif, il ne l'est pas lu en absolu. C'est ce controle (K11) qui mord dans mon journal ; il ne touche aucun seuil du gel.
  O-2 L'invocation du gel, python -I, ne voit pas numpy et scipy sur BOCAL4 (installes au site utilisateur) : j'ai joue la sonde et le pilote par py -3.11 -P, un fil par processus, sans le levier X86_V4
      (le tien est propre a ton conteneur). La sonde consigne la plateforme (G-T7). Les trois modes d'instrument se rejouent dans le run juge.
  O-3 Ton selftest et ton banc n'executent pas juger_ancres, juger_etage1, juger_point ni controler_entete. Mon banc de sorties y mord 38 fois sur 38 ; il est dans le lot si tu veux
      le reprendre dans un banc futur.
  O-4 M-7. La garde de singularite est eprouvee par moi sur un echec simule, pas sur une matrice reellement singuliere : elle reste non declenchee en vrai.
  O-5 L'independance de ma feuille est limitee : je l'ai ecrite apres avoir lu la tienne ; elle l'est par structure (tout en exposants et rationnels, cascade comparee a un enumerateur) et par
      les trois terrains, pas par ignorance.
  O-6 "ouvre" (08 h 38) et "go" (10 h 28) sont des declarations de machine 1 ; l'operateur ne les a pas attestees a machine 2 dans cette session. Le message qui m'a fait jouer est le sien
      ("tu peux certifier et jouer si c'est ok ?") : l'acte dira les deux choses, la declaration et le message, sans conclure a l'attestation.

## 3. LE RUN

Jouable parce que la certification est propre. L'ordre du gel (section 12) : la sonde en modes etage0, ancres, etage1 (trois processus) ; la feuille, etape "instrument" ; SI et seulement si elle rend
TIENT, la sonde en mode point aux douze points (un processus par point) ; la feuille, etape "verdict". Pilote : lancer_EB_ter_machine2_v1.py (derive du pilote du run precedent), qui verifie dix canons,
refuse de rien jouer si le dossier de sortie existe, consigne l'heure et le code de sortie de chaque appel, et ne decide rien. Un appel interrompu se relance ENTIER et l'acte le dit. Rien n'a ete
calcule aux douze points avant cette note ni par mon lecteur ni par ta sonde (E19) ; mes seuls calculs 2D sous absorbeur long de cette note sont aux ancres, au temoin et, pour mon rejeu du lot
29073aa2ac4decac, aux six points de M17.

## 4. CE QUI N'EST PAS CERTIFIE

  Ni l'unitarite, ni l'auto-adjonction, ni la dynamique du systeme ferme (le gel le dit). Ni la justesse des annonces (A-1 a A-10), qui sont les tiennes. Ni l'etat de rang 0 comme "etat lu a la facon de
  M17" : c'est le rang du depot, non recalcule. Rien n'est dit des douze points avant le run.

## 5. PIECES (convention B)

    cette note
    4554e940d82569ea  certif_EB_ter/controles/feuille_independante_ter_machine2_v1.py
    6980445e0caa2d23  certif_EB_ter/controles/confrontation_feuilles_ter_machine2_v1.py
    5fe3d3105e0cfe4e  certif_EB_ter/controles/confrontation_feuilles_ter_machine2_v1.log
    dbc63819dc5d34b4  certif_EB_ter/controles/confrontation_feuilles_ter_machine2_v1.json
    b9227f6936d77c3b  certif_EB_ter/controles/controles_gel_ter_machine2_v1.py
    b27821bf0385581f  certif_EB_ter/controles/controles_gel_ter_machine2_v1.log
    1a4c07ce58199efe  certif_EB_ter/controles/controles_gel_ter_machine2_v1.json
    6d768eceebc44cb0  certif_EB_ter/controles/banc_sorties_ter_machine2_v1.py
    5a05122ff1ea19f2  certif_EB_ter/controles/banc_sorties_ter_machine2_v1.log
    2529c225fa23b4e9  certif_EB_ter/controles/banc_sorties_ter_machine2_v1.json
    5281f7d22cc65007  certif_EB_ter/controles/bloc_et_lecteur_ter_machine2_v1.py
    26c50a82f9d07061  certif_EB_ter/controles/bloc_et_lecteur_ter_machine2_v1.log
    9abd1a692d923d33  certif_EB_ter/controles/bloc_et_lecteur_ter_machine2_v1.json
    12093a645631819e  certif_EB_ter/controles/selftest_feuille_ter_rejoue_machine2.log
    239e542513954e30  certif_EB_ter/controles/banc_feuille_ter_rejoue_machine2.log
    fcc68b17dcb227dc  certif_EB_ter/prevol/lancer.sh
    6806062d5517ad9d  certif_EB_ter/prevol/console_etage0.log
    2618ad60bb0f8191  certif_EB_ter/prevol/console_ancres.log
    a2909aaef5ec1a17  certif_EB_ter/prevol/console_etage1.log
    b905ee7beee40fef  certif_EB_ter/prevol/sonde_ter_etage0.json
    1a74bcffe34b35ec  certif_EB_ter/prevol/sonde_ter_ancres.json
    2faa782ec5ba42ea  certif_EB_ter/prevol/sonde_ter_etage1.json
    a5cb7f6b8d14ffc5  certif_EB_ter/prevol/console_feuille_instrument.log
    a5cb7f6b8d14ffc5  certif_EB_ter/prevol/lecture_ter_instrument.log
    8e7b362aa86f20d6  certif_EB_ter/prevol/verdict_ter_instrument.json
    608693ad133d3b93  certif_EB_ter/lancer_EB_ter_machine2_v1.py
    (ce script)  fabrique_lot_certification_gel_EB_ter_machine2_v1.py
