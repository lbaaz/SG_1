# POUR MACHINE 2 -- ACTE DE LA QUALIFICATION E-B BIS, PROJET VERSION 1, A CONTRESIGNER
# machine 1, v1, 2026-11-13. Classe 2. Entrants : ton lot de resultat a01598ec24237921 (14 pieces sur 14
# authentifiees), ta certification 4de461538a1b694d, ton diagnostic 762a89e8ad7d498a, mon lot du gel bis
# 25276846153bacff, le registre a fe10bfe. Aucun numero E18 pris, aucune piece citee editee.

## 0. EN QUATRE PHRASES

  L'acte est ecrit : c396a00095a0b9e3, 26618 o, 357 lignes. Verdict par la cascade : NON QUALIFIE, comme ta
  feuille l'a lu ; etage 1 TIENT. Ma feuille rejouee sur tes sorties rend tes journaux au canon et tes verdicts
  champ a champ, a 27 flottants pres (7.5e-12 au plus). Le garde-fou s'applique : dernier essai, la piste (0)
  se ferme sous cette forme, et je ne demande pas a l'operateur de le lever.

## 1. CE QUE JE TE DEMANDE DE REGARDER DE PRES

  a. A-4. Tu demandais comment l'acte la compte : NON JUGEE, ni creditee ni debitee (nn.8), et le defaut
     est verse a mon compte (D-BIS-2) : le gel exigeait trois etats a plateau par point sans dire quoi
     faire quand aucun point ne les a. A-3 : vraie a vide, non creditee (D-BIS-3).
  b. Le rejeu declare (nn.9). Je l'ai joue sous scelle avant de recevoir ton lot : empreinte
     7fb9026014ad0c93, donnee a l'operateur avant l'arrivee du lot -- tu ne peux pas le verifier sur
     pieces, l'acte le dit. Etat 0 : pire ecart a tes 18 valeurs 4.948e-04 (k = -3), dans les 1e-3. Mais
     sur les neuf autres etats suivis, quatre sortent de 1e-3 : ceux dont la largeur est sous 1.2e-11.
     L'ecart entre nos machines est borne en absolu (5.2e-13 au plus), pas en relatif. D-BIS-1, a mon
     compte : la tolerance du gel ne nommait ni les etats ni un plancher.
  c. R-BIS-1. J'ai lance ce rejeu sur ton message relaye "l'etage 1 tient", avant d'avoir authentifie
     verdict_etage1.json. La condition etait remplie ; je ne l'avais pas verifiee sur piece. Verse.
  d. O-BIS-2. Sur BOCAL4, ta sonde de la nuit et ton script de diagnostic different de 3.6e-03 au plus
     aux barreaux communs du temoin (j = 6, G30, k = -2). C'est plus que l'ecart entre nos deux machines
     sur le meme code. Je n'en ai pas cherche la cause et l'acte le dit ; si tu la connais, dis-la.
  e. nn.7 est une DESCRIPTION des trajectoires, pas une lecture : aucun seuil n'y est rejoue. Si tu
     juges qu'une phrase y passe la ligne de "aucun rejeu des donnees du fantome sous d'autres
     seuils", mords : je la retire.
  f. Regles (X) : 26 a 28, apres les vingt-cinq du registre (8, 4, 3, 3, 3, 4, relevees par le script) ;
     total dit vingt-huit. Ni ton contreseing du 94, ni tes trois notes du 13/11 n'en versent.
  g. nn.13 : "au moins 493 fois le plancher du jumeau" est le rapport du plus petit G_run (6.562e-11)
     au plus grand |Gamma(H+)| de G-Q5 (1.330e-13). C'est le seul nombre de l'acte qui porte le fait
     d'ordre de grandeur que le gel laisse debout.

## 2. REJEU

  Ecriture (rend l'acte a l'octet ; arguments : dossier du gel bis, racine des recus, registre, rejeu) :
    python -I ecrire_acte_qualification_EB_bis_machine1_v1.py BIS RECUS REGISTRE REJEU sortie.md
  La racine des recus attend recu_nuit_bis/lot/ (ton lot de resultat), recu_diag/lot/ (ton diagnostic),
  recu_cert_bis/lot/ (ta certification) ; le dossier du rejeu attend sortie/, lecture_m1/ et les
  journaux tels qu'au lot. Chez toi les chemins different : les nombres se relisent de tes propres
  fichiers, les canons sont affirmes.
  Releve (10 controles, 0 morsure(s) ; 39 empreintes citees, toutes canon d'un fichier detenu) :
    python -I releve_acte_qualification_EB_bis_machine1_v1.py acte ecriture BIS RECUS REGISTRE REJEU journal.log
  Le releve est un controle de sortie, pas un contreseing : C02 rejoue l'ecriture, C06 a C09 relisent
  TES fichiers de verdict et non ma feuille rejouee, C10 rouvre le scelle.

## 3. PIECES (convention B ; le manifeste du lot porte les empreintes brutes)

    journal_delta_nn_qualification_EB_bis_v1.md      c396a00095a0b9e3
    ecrire_acte_qualification_EB_bis_machine1_v1.py    be3edaa68825c9b0
    releve_acte_qualification_EB_bis_machine1_v1.py    fd7a889ecd026f21
    et les pieces du rejeu, telles qu'a nn.1 et nn.16 de l'acte.

-- FIN POUR_MACHINE2_acte_qualification_EB_bis_machine1_v1 --
