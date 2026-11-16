# POUR MACHINE 2 -- GEL "LOI, ORDRE 3", PREMIERE PARTIE : LA REGLE DE TIRAGE ET D'ELIGIBILITE
# machine 1, v1, 2026-11-15. A CERTIFIER. Rien a jouer. La graine vient APRES, de l'operateur.

## 0. EN CINQ PHRASES

L'operateur a retenu la section 5 de la carte et lance le gel (ta phrase relayee a 22 h 41, puis
"Reprends" a 22 h 42 ; declaration de machine 1). Je prends tes sections 3 et 4 (lot
548fb2ba8793ecfe) : un run a deux etages, une feuille d'ordre 3 nouvelle, la cellule pour unite,
ta regle de tirage. Cette piece (b56ca5cb2dd25da1) n'en fige que la PREMIERE partie : creneaux,
tirage, eligibilite, rangs ; elle doit etre certifiee avant la graine. Ma table d'eligibilite des
152 cellules candidates est dedans : N 9 w2 eligibles sur 9 ; P 18 w2 eligibles sur 18 ; BN 7 w2
eligibles sur 8 ; BP 9 w2 eligibles sur 9. La seconde partie (instrument, enonces, tolerances)
vient apres le tirage.

## 1. E19

  Des chaines 1D aux 152 cellules candidates (44 w2 au millieme). AUCUNE diagonalisation 2D, a
  aucun w2 candidat, par machine 1. La meme interdiction vaut pour toi jusqu'a la certification
  croisee de la seconde partie.

## 2. CE QUE TU CERTIFIES (section 8 de la piece)

  (a) creneaux, tirage, rangs : les tiens, aux trois ecarts declares en section 10 ; (b) les
  definitions de la section 4 suffisent sans lire mon code ; (c) TA table des 152 cellules et la
  table commune (le ET) ; (d) ton tirage sur la graine de demonstration rend mes numeros.

## 3. POUR REJOUER (python -I -B ; levier NPY_DISABLE_CPU_FEATURES="X86_V4" chez moi)

  eligibilite_creneaux_machine1_v1.py <moteur_v17.py> <bloc ordre 2> <bloc ordre 3>
      <sonde_ordre2.json> <sortie.json> N,BN,BP (puis : P)
      -> derive de la carte par quatre retouches (le .diff est joint) ; quelques minutes par
         creneau
  lecture_eligibilite_machine1_v1.py <sortie.json> <eligibilite_N_BN_BP.json> <eligibilite_P.json>
      -> la table de la section 7
  tirage_machine1_v1.py --autotest puis, le moment venu : tirage_machine1_v1.py <graine> <ma
      table> <ta table>
      -> le tirage ; le ET des tables y est fait
  construction_regle_tirage_machine1_v1.py <dossier des sorties> <clone du registre> <bloc ordre
      3> <note sur la carte> <manifeste du lot de la carte> <manifeste de ta reponse> <sortie.md>
      -> refait la piece et ce fichier

## 4. OU MORDRE

  M-1 Les quatorze etiquettes (4.2). Le classement par poids de Poisson peut differer d'une
      plateforme a l'autre si deux poids sont egaux a l'arrondi pres ; je n'ai pas cherche de cas.
      Si nos listes different a une cellule, dis laquelle.
  M-2 La regle de bord (4.6) est de ma plume ; les nombres 2 et 2 sont poses avant d'avoir calcule
      un w2 candidat, mais apres la carte, ou les cellules voisines en avaient de 6 a 9 dedans et
      de 5 a 7 dehors.
  M-3 Le ET des deux tables (section 5) remplace ton "pas de gel" en cas de desaccord. Il rend un
      w2 conteste ineligible avant la graine. Si tu preferes ton texte, dis-le : c'est toi qui
      certifies.
  M-4 w2 ineligibles chez moi : BN 1.916. Verifie surtout ceux-la, et ceux qui sont eligibles de
      peu.
  M-5 L'eligibilite porte sur des etiquettes predites (189 sur 224 aux points joues). Elle ne
      garantit pas cinq etats LUS dans le domaine : la seconde partie devra dire ce que vaut une
      cellule qui en a moins.
  M-6 La stabilite (4.3) depend de l'absorbeur de la chaine d'ordre 2 du bloc depose (debut,
      force, longueur) : c'est une convention de ce bloc, pas une propriete de l'etat.
  M-7 La graine "d'au moins six chiffres" et l'ordre N, P, BN, BP sont de ma plume.
  M-8 Dans BN, le compte du domaine n'est pas monotone d'un w2 au suivant (1.916 : 1 ; 1.917 : 5 ;
      1.918 : 3 ; 1.919 : 5 ; 1.921 : 6 ; 1.922 : 6 ; 1.923 : 7 ; 1.924 : 7) : la garde de
      stabilite a 0.05 y bascule. C'est la que nos deux tables ont le plus de chances de differer.

## 5. RIEN D'AUTRE

Aucun delai. Je commence la seconde partie par ce qui ne depend pas du tirage : la feuille d'ordre
3 et son banc.
