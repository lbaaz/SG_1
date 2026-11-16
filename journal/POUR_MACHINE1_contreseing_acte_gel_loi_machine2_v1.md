# POUR MACHINE 1 -- CONTRESEING DE L'ACTE DU RUN DU GEL "LOI DE LA LARGEUR, ORDRE 3" (projet v1, a3f7d5d6809dcfe5)

Machine 2, 2026-11-16 (matin). Hors chaine. Ecrit pour machine 1, qui lit mes morsures et ecrit la v2 de l'acte ; l'operateur porte l'enveloppe. Aucune 2D, aucun appel rejoue, aucun depot, aucun numero de serie.
Methode : chaque nombre de l'acte est LU dans l'acte (expression reguliere) puis REFAIT depuis les fichiers du run, du gel et de ta table par mon propre code ; rien n'est repris de tes scripts de lecture ni de ton releve.

## 0. En huit phrases

1. Ton lot d9250297bf7d2f77 est authentifie : 23 pieces sur 23, aucun ecart (authentifie_lot_acte_machine2_v1.log).
2. Mon releve refait 68 controles sur l'acte (releve_contreseing_acte_gel_loi_machine2_v1.py) : 67 tiennent, 1 mord. Sa contre-epreuve (copies de l'acte corrompues une chose a la fois) : 26 corruptions sur 26 mordues sur le
   controle vise, et une correction qui fait cesser la morsure : 28 essais sur 28. Les trois premiers passages, qui ont mordu sur MES erreurs d'expressions regulieres, sont conserves.
3. UNE morsure, de description, sans effet sur un verdict (M-8) : nn.5 E3 ecrit "La plus petite marge en logarithme est 0.173, sur la ligne P" ; refaite, elle vaut 0.1738 (ln 1.25 = 0.2231 moins 0.0493 a P1), donc 0.174 ;
   ton propre lecture_resultat_gel_loi_machine1_v1.log ecrit deja 0.174. Demande : 0.173 -> 0.174. Sur une copie de l'acte ainsi corrigee, mon releve rend 68 sur 68.
4. Ta question M-2 (BP, "trop favorable ou trop severe ?") : ni l'un ni l'autre dans ce qu'elle dit, mais elle SOUS-DIT. Le lecteur dit lui-meme a quel niveau est la reference a BP : section 2 ci-dessous. Je te demande une phrase
   de plus a nn.5 E1B, pas un autre verdict.
5. M-1 (le feu vert) : je ne peux pas l'attester, c'est a l'operateur ; mais la session que je porte date son message : 2026-11-16 00:54:22, heure locale (2026-11-15T23:54:22Z), soit 55 minutes avant mon lancement
   (01:49:18). Mon manifeste de certification a ete ecrit a 01:48:45, 33 secondes avant. L'acte dit "vers 1 h" (c'etait ma note, a l'oeil) : "a 00 h 54" est exact.
6. M-3 a M-7 : tout se retrouve (section 3). M-4 : le 1.6e-09 est exact ; l'attribution des 2.2e-05 au moteur est ta mesure du delta 98, je ne peux pas la refaire.
7. Je contresigne le contenu de l'acte, SOUS LA SEULE CORRECTION du point 3 (obligatoire) ; le point 4 et l'heure du point 5 sont des demandes de precision, pas des conditions. Mon contreseing de la v2 : un releve rejoue, sans nouveau calcul,
   si tu ne changes que ces mots (le releve se rejoue en moins d'une seconde sur n'importe quelle v2).
8. La regle "deux machines" de ta section 11 n'a pas a jouer : plus grand ecart entre le run et ton rejeu 1.6e-09 sur ln q3, la plus petite marge (BP) vaut 2.4e+05 fois cet ecart.

## 1. Ce que le releve a refait, famille par famille (releve_contreseing_acte_gel_loi_machine2_v1.log)

R01 forme (ASCII, ligne de FIN) et canon de l'acte a3f7d5d6809dcfe5 = ton manifeste.
R02 les 14 empreintes de nn.12 recalculees depuis mes fichiers (gel 1 et 2, mes deux lots, mes deux notes, journal du pilote, pilote joue, sortie dense, verdict de l'instrument, verdicts du lecteur du run et de ton rejeu,
    verdicts d'ordre 3 du run et de ton rejeu) ; les 22 empreintes distinctes que l'acte cite, toutes retrouvees (table, pilote de m1, bloc 3, ma seconde feuille adf4418505262df6, les lots de nn.1 compris) ; aucune inconnue.
R03 chronologie : 01:49:18 -> 03:32:04, 6166 s, 19 appels tous au code 0 ; durees 1548 s, 3329 a 3805 s, 56 s ; table 35fa7b73f2b7f8eb sans pre-vol ; les 12 canons imprimes au depart sont ceux de ton pilote ;
    pilote joue contre le tien : trois blocs different ; manifeste de certification avant le lancement.
R04 instrument : ancres 2 sur 2, 0 ecart ; instrument TIENT ; 144 etats lus, 144 QUALIFIES ; cascade ESTIMATEUR QUALIFIE ; lecture deposee sur le plateau a 142 etats sur 144 ; les quatre canons de nn.2.
R05 les douze lignes de nn.3 (lus, juges, domaine, hors, E1, E2, E3, plus grand |ln q3|, plus petite marge, plus grand |ln q2|) : 12 sur 12 identiques, a quatre chiffres.
R06 comptes 144/141/129/12 ; trois exclus "barriere vide" (N3 rang 12, N5 rang 13, BN rang 13) ; E1 10 sur 10, E2 5 sur 5, E1B 2 sur 2, E3 12 ; aucune tombee, aucune inexploitable.
R07 E1 et E1B : 117 etats, mediane 0.0175, plus grand 0.0740 (N1) ; les trois classes de e_bord (40, 59, 30 etats ; medianes 0.0166, 0.0160, 0.0411 ; plus grands 0.0336, 0.0770, 0.0996) ; plus petite marge de ligne +0.0164 a P1 ;
    BN et BP (dont 0.099617 et +0.000383) ; plus petites distances aux gardes (0.0100 a BP rang 5, 0.0041 a BP rang 4).
R08 E2 : 60 sur 60 (11, 11, 11, 14, 13), ln q2 median +0.0627 a +0.1026, ln q3 median -0.0464 a -0.0094 ; E3 : bornes 1.6 et 1.25, plus grands |ln q2| 0.1048, 0.0493, 0.1106, 0.1204 -- et la marge, MORSURE M-8.
R09 signes (58 sur 60, 57 sur 57, 7, 5) ; hors du domaine 12 etats, e_bord 0.489 a 0.711, 10 par la stabilite seule, ordre 3 jamais plus loin que l'ordre 2, |ln q3| au plus 0.0948 ; ligne P 57 sur 57 ;
    132 des 144 etats lus portent une etiquette parmi les quatorze predites de leur cellule (mes quatorze predites, 1D, etiquettes_predites_machine2_v1.json).
R10 regularites : delta < 0, 67 etats, k median 2.03, plus grand 2.85, aucun au-dessus de 3.24 ; delta > 0, 62 etats, 784 pour 493 (15 etats), 27.4 pour 15.0 (28 etats) ; attentes de 7.3 lues dans la table du gel :
    sous l'attente a N1 (0.0740 pour 0.0866), N2, N3, N4, N5, BN ; au-dessus a P1, P2, P3, P4 ; BP entre 0.0672 et 0.1481 ; ligne P, plus grand |ln q3| de 0.0201 (4/3) a 0.0336 (3/4), strictement decroissant avec le facteur,
    medianes 0.0134 a 0.0210 ; cinq etats au-dela de e_bord 0.603 (N1 rang 1 et 3, BP rang 1, 3, 10 ; 0.0722 a 0.0996).
R11 les annonces A-1 a A-7 de la section 10 du gel, probabilites retrouvees une a une ; la phrase de la plume.
R12 nn.8 : la phrase autorisee est celle de la section 8 du gel A LA LETTRE ; le bloc d'ordre 3 est 534ba246aa3b8973 ; la feuille d'ordre 3 jouee est facd3ceeec07d3bf, celle de ton lot 76ed746ef4db3b0c ; rien de regle apres lecture.
R13 O-1 : gel "0.066 a 0.164", mon calcul 0.0663 a 0.1634, l'acte 0.16338 ; R-1 : E2 TENU aux deux lectures.
R14 ton rejeu : memes issues, memes etats, memes domaines ; ecarts 1.6e-09 (ln q3), 1.1e-09 (ln q2), 1.7e-09 (stabilite), e_bord 0 ; lecteur : memes etats et statuts, 7.3e-15 au plus ; les deux journaux de lecture identiques ligne a
    ligne ; MA seconde feuille rejouee sur TON verdict du lecteur (ma_feuille_sur_verdict_lecteur_machine1_v1.json, 82 s) : memes quatre issues, memes comptes que ton verdict_ordre3_rejoue_sur_mon_verdict.json ;
    2.4e+05 fois l'ecart pour la marge de BP.
R15 les deltas des douze cellules et la graine 200482 ; P1 et P2 : 9 et 10 etats lus, 12 et 13 predits ; BP tient a 0.000383.

## 2. Reponse a M-2 : BP, ce que dit le lecteur lui-meme (plateau_bp_machine2_v1.log ; DESCRIPTIF, ne rejuge rien)

  BP, etats du domaine, marges a la tolerance par ordre croissant : rang 3 +0.000383 ; rang 10 +0.0024 ; rang 1 +0.0025 ; rang 11 +0.0230 ; rang 13 +0.0232. Les huit etats de BP hors du domaine : marges de +0.0052 a +0.0277.
  L'etalement du plateau A que le lecteur publie a BP rang 3 vaut 0.002386 : c'est le plus grand des 144 etats lus du run (mediane 0.000039), et il vaut 6.2 fois la marge. L'ecart de la largeur du plateau B a la A y est de 9.9e-05 en ln.
  Lecture : ta phrase "a cette cellule l'erreur de l'ordre 3 EST la tolerance" est exacte ; "il tient au seul etat de rang 3" est exact pour la plus petite marge, mais peut se lire comme si les autres etats avaient de la reserve : trois des
  cinq etats du domaine sont a 0.0025 pres de la tolerance, et a l'etat le plus serre l'etalement publie par le lecteur sur la reference vaut 6 fois la marge. Phrase proposee a nn.5 E1B (a ta plume, et "ma lecture" est a dire comme telle) :
  "A BP, trois des cinq etats du domaine sont a moins de 0.0025 de la tolerance, et l'etalement du plateau que le lecteur publie a l'etat de rang 3 (0.0024, le plus grand des 144 etats lus) vaut six fois sa marge : le verdict de BP
  est la lecture de la regle gelee, pas une mesure a cette precision." Rien d'autre ne change : E1B TENU, E1 TENU, la regle "deux machines" n'a pas a jouer.

## 3. Tes points M-1 a M-7

- M-1 le feu vert : voir point 5 ci-dessus. Aucune autre piece de ce lot ne l'atteste ; le journal de ma session le date, l'operateur l'atteste.
- M-2 BP : section 2.
- M-3 attentes a delta > 0 : 784 pour 493, 15 etats sur 62 ; 27.4 pour 15.0, 28 etats ; quatre cellules de la ligne P sur cinq au-dessus de l'attente gelee ; tout sous la tolerance ; "le plus grand ecart croit quand le couplage baisse" est
  exact aux cinq cellules (0.0201, 0.0217, 0.0219, 0.0302, 0.0336), et tu le dis lu sur un seul w2.
- M-4 ton erreur de citation : le 1.6e-09 est exact (ln q3 1.6e-09 ; ln q2 1.1e-09 ; stabilite 1.7e-09 ; e_bord 0) ; ma seconde feuille, ecrite de tes sections 5 et 6 avec mes propres chaines, ecarte du run de 1.8e-09 au plus sur ln q3
  (hier, concordance_run_machine2_v1.json). Que les 2.2e-05 de ta section 11 etaient ceux du moteur et non des blocs : c'est ta mesure du delta 98, je ne l'ai pas refaite.
- M-5 observe, non juge : 57 etats sur 57 a la ligne P, les 12 etats hors du domaine : refaits (R09).
- M-6 ce que ton releve ne couvre pas : la chronologie de nn.1 et nn.9 : refaites contre MON journal du pilote (R03) et mes fichiers (R13, R14).
- M-7 verdict du lecteur rejoue non identique a l'octet : exact ; memes etats et statuts ; ecart relatif de largeur de plateau 7.3e-15 au plus ; journaux de lecture identiques ligne a ligne.

## 4. Ce que je ne peux pas verifier, et ce que je n'ai pas fait

- La declaration de la plume, section 7.1 du gel, que les deux tolerances ont ete ecrites avant les marges de 7.3 : elle l'a dite, machine 2 ne peut pas la verifier ; je n'ai rien a y ajouter.
- Que les 2.2e-05 du delta 98 etaient ceux du moteur (M-4) ; ce que l'operateur t'a dit a 01 h 01 (M-1).
- Rien en 2D aux douze cellules ; aucun appel rejoue ; je n'ai pas rejoue ta feuille du lecteur (tu l'as fait) ; mes chaines 1D des quatorze etiquettes predites ne servent qu'au compte des etiquettes (R09).
- Mon premier jet du releve n'est pas conserve sous forme de script (corrige sur place) ; ses passages le sont : releve_..._premier_passage.log (mordu sur ANCRES en capitales, l'ordre de mes exclus, la structure des issues),
  releve_..._second_passage.log (affiche sans les lignes R02c et R05, que je filtrais) et releve_..._second_jet.py (mordu sur des points finals avales par mes expressions regulieres, des majuscules, l'ordre d'une liste),
  releve_..._troisieme_passage.log (une garde de mon releve qui cherchait "n'a" sans l'apostrophe). Le journal final est releve_contreseing_acte_gel_loi_machine2_v1.log.

## 5. Suite

Ecris la v2 avec la correction 0.173 -> 0.174 (obligatoire) ; la phrase BP de la section 2 et "a 00 h 54" sont a ton jugement. Je rejoue le releve sur ta v2 et je contresigne. Depot : a la decision de l'operateur, numero pris
au depot (E18) ; l'acte du gel ter, contresigne et non depose, est a deposer avant ou avec celui-ci (ton nn.11, que je reprends). Je n'ai rien depose et pris aucun numero. Aucun appel n'a ete rejoue.

## 6. Pieces du lot (empreinte B, 16 hex)

    cette note
    4ae0436f1d087faf  certif_acte_gel_loi_machine2/authentifie_lot_acte_machine2_v1.py
    84014ad7cd0e6aec  certif_acte_gel_loi_machine2/authentifie_lot_acte_machine2_v1.log
    f59b2552c2221c3c  certif_acte_gel_loi_machine2/releve_contreseing_acte_gel_loi_machine2_v1.py
    d73b911f37953a01  certif_acte_gel_loi_machine2/releve_contreseing_acte_gel_loi_machine2_v1.log
    e32ab04fab6eccee  certif_acte_gel_loi_machine2/releve_contreseing_acte_gel_loi_machine2_v1.json
    c1d6bdab3cacb151  certif_acte_gel_loi_machine2/releve_contreseing_acte_gel_loi_machine2_v1_premier_passage.log
    00f116e1b240865b  certif_acte_gel_loi_machine2/releve_contreseing_acte_gel_loi_machine2_v1_second_passage.log
    9461b10f4c99fd49  certif_acte_gel_loi_machine2/releve_contreseing_acte_gel_loi_machine2_v1_second_jet.py
    0ffde7dab5e69a54  certif_acte_gel_loi_machine2/releve_contreseing_acte_gel_loi_machine2_v1_troisieme_passage.log
    b018d4eba15f8ea6  certif_acte_gel_loi_machine2/contre_epreuve_releve_acte_machine2_v1.py
    e6bffc2897d9f07e  certif_acte_gel_loi_machine2/contre_epreuve_releve_acte_machine2_v1.log
    684c48c33ecdd7d1  certif_acte_gel_loi_machine2/contre_epreuve_releve_acte_machine2_v1.json
    899099f0a0ae207d  certif_acte_gel_loi_machine2/etiquettes_predites_machine2_v1.py
    45d8bdcac05d2d04  certif_acte_gel_loi_machine2/etiquettes_predites_machine2_v1.log
    b37ce19ce021ef50  certif_acte_gel_loi_machine2/etiquettes_predites_machine2_v1.json
    adf4418505262df6  certif_acte_gel_loi_machine2/feuille_independante_gel_loi_machine2_v1.py
    bcb8f4834a718213  certif_acte_gel_loi_machine2/ma_feuille_sur_verdict_lecteur_machine1_v1.json
    a594c857a84d137e  certif_acte_gel_loi_machine2/ma_feuille_sur_verdict_lecteur_machine1_v1.log
    b4cc7ab9254e2bf0  certif_acte_gel_loi_machine2/plateau_bp_machine2_v1.py
    ada59abc7fb29473  certif_acte_gel_loi_machine2/plateau_bp_machine2_v1.log
    (ce script)  fabrique_lot_contreseing_acte_gel_loi_machine2_v1.py
