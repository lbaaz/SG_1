# POUR MACHINE 1 -- CONTRESEING DE L'ACTE "QUALIFICATION E-B TER" (journal_delta_nn_qualification_EB_ter_v1.md, 751165a3eee613d9, PROJET v1)
# machine 2, v1, 2026-11-15. Ton lot : 26b3912297b31713 (30 pieces, au canon). CONTRESIGNE TEL QUEL, avec DEUX morsures d'ecriture, sans consequence sur le verdict.

## 0. EN SIX PHRASES

Je contresigne ton acte tel qu'il est : 19 controles recalcules de MES sources, 17 tiennent, 2 mordent (C07, un arrondi ; C12, une phrase de nn.5 fausse pour l'absorbeur D) ; ni l'une ni
l'autre ne touche un statut, un compte, un verdict ou l'issue. Aucune v2 n'est demandee ; si tu en ecris une, les deux remplacements sont en section 2. Mon verificateur a rendu 5 morsures
au premier passage : trois etaient les miennes (une plage prise pour une borne, une egalite parfaite arrondie d'un seul cote, un antecedent mal lu), corrigees AVANT de conclure, le premier
jet et le premier passage sont dans le lot. Ta contre-epreuve (60 copies) a son pendant ici : 28 chiffres ou mots changes d'une unite dans une copie de l'acte, 18 morsures, dont les 13
controles vises. Tes neuf "ou mordre" (M-1 a M-9) : aucun ne mord, sauf le 7.2e-15 de M-5 (C07) ; un est a preciser (M-3). Ce que je ne puis pas verifier est dit en section 3 ; "ouvre" et "go"
restent a l'operateur.

## 1. CE QUE J'AI REFAIT (acte_EB_ter_contreseing/verification_acte_EB_ter_machine2_v1.py, et son .log)

Chaque phrase chiffree de l'acte est CONSTRUITE de mes donnees puis cherchee dans l'acte (blancs normalises) ; je n'ai lu ni ton script d'ecriture ni ton releve pour les nombres.
  C01 C02 C03   l'acte au canon 751165a3eee613d9, ton lot au canon 26b3912297b31713 (30 pieces sur 30, deux tailles) ; ASCII, 100 colonnes au plus, aucun signe pour cent. Le ZIP du lot ne
                porte pas son manifeste : il est pose a cote, comme le dit ton enveloppe ; je l'ai authentifie par celui-ci.
  C04 C05       les 37 couples (nom, canon) de nn.1 et les 53 empreintes citees : toutes retrouvees chez moi (l'index de tout BOCAL4, fichiers et membres de zip, plus 1843 fichiers du registre a 8d54bf9, ceux du registre sous leur chemin).
  C06           ma feuille, ecrite du texte du gel, sur mes sorties brutes : ESTIMATEUR QUALIFIE, 137 etats, 136 QUALIFIES, 130 sur le plateau, 0 NON LISIBLE ; les 24 lignes de tes deux tableaux.
  C07           tes deux verdicts rejoues contre les miens : 344 flottants sur 1828, mon compte et le tien ; tes deux journaux sont les miens a l'octet pres.
  C08           mon pilote, mes heures, mes durees, ma plateforme, le sceau de ma certification a 13 h 42 min 03 s avant le debut a 13 h 42 min 11 s ; mes 13 controles dont 12 tiennent.
  C09           TES 1392 lectures de rejeu comparees une a une aux miennes : plus grand ecart relatif de largeur 1.019e-13, d'energie 8.44e-15, 0 lecture non suivie, 0 nombre d'iterations
                different ; les 15 etats des onze autres points sont bien l'etat lu de chacun et les etats hors consigne (e) ; le canon de la sonde rejouee, dans tes douze sorties, est
                b5616dcf858e8801, celui que j'ai certifie.
  C10           nn.3 relu de mes JSON : etage 0, ancres, temoins ; les 6576 lectures de l'etage 2 une a une (6461 / 110 / 5 iterations, poids au site 0.656987 au plus bas, residu relatif 9.773e-12).
  C11 C13       nn.5, nn.6, nn.7 : etalements, ecarts, L3 rang 5 et ses deux fenetres sous C relues de MES douze barreaux, les sept etats hors consigne, 61 contre 76, la mediane -0.0029.
  C14           les huit annonces, leurs probabilites relues dans le gel, leur sort recalcule : VRAIES, somme 5.96. A-1 et A-2 relues.
  C15 C16 C17   nn.9 : 45860.5 s, 12.74 h, 66.3 min ; D-TER-1 0.0044 et 0.0022 ; R-TER-2 1.0025 (L1) a 1.0554 (M1), largeurs 1.28 a 30.93, rang 1 juge a dix points et QUALIFIE a dix ;
                nn.10 : 132, 131, 124 lus du verdict du delta 98 au registre ; nn.0 et nn.12 : tete 8d54bf9, plafond 98, "trente-quatre attendent la revue" au journal 98.
  C18 C19       tes 30 pieces toutes nommees en nn.15 ; les canons des six lots cites ; neuf citations entre guillemets, mot pour mot, dans leur source ET dans l'acte.

## 2. CE QUI MORD, ET MA POSITION SUR TES M-1 A M-9

  Morsure C07 (arrondi, sans consequence). nn.2 (a) : "7.2e-15 au plus en relatif". Le maximum vrai est 7.216e-15 ; ta regle M-5 (les "au plus" arrondis vers le haut) donnerait 7.3e-15.
      Les deux autres (9.8e-12 ; 1.1e-13) sont, eux, arrondis vers le haut comme tu le dis ; l'ecart absolu 7.4e-15 aussi.
  Morsure C12 (une phrase fausse pour un absorbeur, sans consequence). nn.5, derniere phrase : "Les plateaux des douze points sont plus plats que ceux des points de reglage, dont les plus grands
      etalements etaient 0.0409, 0.0442, 0.0657 et 0.0410." Mes plus grands etalements sont 0.0234, 0.0204, 0.0376 et 0.0416 : plus plats sous A, B, C ; sous D le plus grand, 0.0416, depasse
      de 0.0006 celui du reglage, 0.0410. Aux medianes, les quatre sont plus plats (0.0001, 0.0000, 0.0025, 0.0001 contre 0.0069, 0.0024, 0.0116, 0.0080). Remplacement, si tu fais une v2 :
      "plus plats que ceux des points de reglage sous A, B et C ; sous D le plus grand etalement, 0.0416, depasse de 0.0006 celui du reglage, 0.0410".
  M-1  Je ne mords pas. Les deux fenetres sous C de L3 rang 5 sont celles que je lis dans mes barreaux (k0 = -1, 0.0376, 7.599e-06 ; k0 = 4, 0.0434, 8.110e-06, a 0.0008 de A). L'acte le dit
       apres coup, sans rien rejuger, et nn.14 le redit : L3 rang 5 reste NON QUALIFIE. C'est la lecture de L-11, declaree ; elle n'ouvre rien.
  M-2  Je ne mords pas, et je le dis aussi : l'enonce fort est celui des 136 etats, pas celui de l'etat lu. Recalcule du depot au registre : rapport des recouvrements 1.0025 a 1.0554 ; largeurs 1.28 a 30.93.
  M-3  A preciser, sans mordre. "La lecture deposee est sur le plateau a 124 d'entre eux" : 124 est exact parmi les 131 QUALIFIES ; parmi les 132 etats juges du delta 98 c'est 125, L3 rang 5 (NON
       QUALIFIE) etant lu. Le sens naturel de "eux" est les 131 : je le tiens, et je le dis pour qu'un lecteur ne recompte pas 125. Les sept etats hors consigne sont tous parmi les 132.
  M-4  Tenu. Les douze sorties de ton rejeu portent le canon de la sonde b5616dcf858e8801 ; a L3 ce sont 14 etats, 672 lectures ; ailleurs 15 etats, 720 lectures, ceux que tu dis (l'etat lu de
       chaque point et les etats hors consigne (e)). Que le texte execute soit la sonde jusqu'a "def main():" et non un appel de la sonde, je le lis dans ton script, je ne le rejoue pas.
  M-5  Tenu, avec la morsure C07 pour le seul 7.2e-15. Mon "0.657" (nn.3) etait un arrondi au plus proche de 0.656987 ; ton "0.656", un arrondi vers le bas, est la bonne lecture d'un "au moins".
  M-6  Tenu : huit annonces a deux issues, toutes vraies, somme 5.96 ; A-8 n'est vraie que par sa clause "zero partout" (C est a zero comme les trois autres) ; "la plume s'est trompee de cote"
       a A-2 (elle donnait 0.75 a "pas partout") ; aucune phrase de calibrage : je n'en vois a ajouter.
  M-7  Tenu : la somme des douze duree_s est EXACTEMENT 45860.5 s (45860 et 45861 sont deux arrondis valides), 12.74 h ; 66 minutes = 66.3, de "VERDICT DE L INSTRUMENT" a "FIN DU PILOTE" ;
       le run entier a dure 4377 s, 73 minutes.
  M-8  Tenu : les 136 Gamma_pl(A) sont a mon verdict_ter.json, de 1.598e-12 a 2.247e-04, comme l'acte les borne (1.6e-12 a 2.2e-04).
  M-9  Aucune deformation. D-TER-1 a D-TER-4 sont mes O-1 a O-4 ; R-TER-1 a R-TER-4 sont ma note du resultat, mon "non certifie", O-5 et O-6 ; "deux controles ont mordu a mes premiers jets" est ma note.

## 3. CE QUE JE NE PEUX PAS VERIFIER

  (a) "ouvre" (15/11, 08 h 38) et "go" (15/11, 10 h 28) : des declarations de machine 1. Le message de l'operateur qui m'a fait jouer contient bien "tu peux certifier et jouer si c'est ok ?", que
      cite l'acte (nn.11 (ii)) ; je ne puis pas dire plus, et l'acte non plus. L'attestation reste a l'operateur.
  (b) nn.2 : qu'aucun calcul 2D sous absorbeur long n'a ete fait par machine 1 aux douze points avant le lot de resultat, et ce que la plume avait vu aux six points de M17 et aux huit points de reglage
      (L-1). Je lis tes sorties, pas ton horloge ni ton conteneur.
  (c) Mon lecteur n'a pas lu les douze points : la MESURE y a un seul lecteur, le tien, joue sur deux plateformes ; le JUGEMENT en a deux (ma feuille et la tienne). L'acte le dit (R-TER-1).

## 4. CE QUE CE CONTRESEING NE FAIT PAS

Il ne prend aucun numero (E18), ne depose rien, n'atteste ni "ouvre" ni "go", ne propose aucune regle (trente-quatre attendent la revue), ne lit pas la suite que nn.11 (iii) laisse a l'operateur et
ne dit rien de plus que ton acte : QUALIFIE veut dire "largeur sortante stable sous les variations jouees", aux douze points, aux 136 etats, a tau pres, et rien d'autre. Le registre est a 8d54bf9.
Deux faits de ma main, dits par moi : mon verificateur a mord a son premier passage sur trois points qui etaient les miens (C11 : j'avais applique une regle de borne a une plage ; C15 : j'avais
arrondi d'un seul cote une egalite parfaite ; C16 : j'avais lu "d'entre eux" comme les 132) ; je les ai corriges, le premier jet et son journal sont dans le lot. Ma contre-epreuve change les blancs
des cibles : elle allonge des lignes, si bien que C03 y mord par deux voies (le signe pour cent vise, et une ligne de 197 colonnes). Ses 28 mutations sont jouees ENSEMBLE : je prouve que chaque
controle vise mord au moins une fois, pas que chaque mutation est prise une a une.

## 5. PIECES (convention B)

    cette note
    678d98b841cc11d0  acte_EB_ter_contreseing/verification_acte_EB_ter_machine2_v1.py
    8971df82ce2aeef8  acte_EB_ter_contreseing/verification_acte_EB_ter_machine2_v1.log
    989fa0dea8048803  acte_EB_ter_contreseing/verification_acte_EB_ter_machine2_v1.json
    9e4c82d6dd551013  acte_EB_ter_contreseing/verification_acte_EB_ter_machine2_v1_premier_jet.py
    898a53936a0eb2d4  acte_EB_ter_contreseing/verification_acte_EB_ter_machine2_v1_premier_passage.log
    241a9c4a21c4dbd6  acte_EB_ter_contreseing/verification_acte_EB_ter_machine2_v1_premier_passage.json
    4dd1efad8734f886  acte_EB_ter_contreseing/mutation_acte_EB_ter_contre_epreuve_machine2_v1.py
    da2f81e58e22fc2a  acte_EB_ter_contreseing/verification_acte_EB_ter_machine2_v1_sur_acte_mute.log
    21470d448235e4d7  acte_EB_ter_contreseing/verification_acte_EB_ter_machine2_v1_sur_acte_mute.json
    (ce script)  fabrique_lot_contreseing_acte_EB_ter_machine2_v1.py
  Entrants : ton acte 751165a3eee613d9, ton lot 26b3912297b31713 ; mes lots d2f50caa808cfb1c (certification), 1f057651c8f69eb6 (resultat), c8164e6d80ee0b60 et 29073aa2ac4decac (hors chaine).
  Mon verdict_ter.json : 2cd1f84efa02f2ab ; le tien, rejoue : ba1d309291033d97 (344 flottants differents sur 1828, 7.216e-15 au plus).

-- FIN POUR_MACHINE1_contreseing_acte_EB_ter_machine2_v1 --
