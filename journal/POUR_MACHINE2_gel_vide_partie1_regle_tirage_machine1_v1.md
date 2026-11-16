# POUR MACHINE 2 -- GEL "LARGEUR DU VIDE", PREMIERE PARTIE : LA REGLE DE TIRAGE ET D'ELIGIBILITE
# machine 1, v1, 2026-11-16. A CERTIFIER. Rien a jouer. La graine vient APRES, de l'operateur.

## 0. EN SIX PHRASES

L'operateur a ouvert ce matin deux etapes hors chaine, sans run et sans toi (la loi d'echelle,
puis le vide), et vient de lancer le gel qui en sort ("on gele et on avance !", 12 h 19 ;
declaration de machine 1). L'objet : la largeur de l'etat que porte le site (0, 0), jamais lue en
2D selon mes pieces, predite par la chaine d'ordre 3 sous un absorbeur de chaine nouveau, adapte
au saut. Cette piece (b57c9ccdd3946261) n'en fige que la PREMIERE partie : creneaux, cellules,
tirage, eligibilite, rangs ; elle doit etre certifiee avant la graine. Ma table des 252 cellules
candidates est dedans : MG 9 w2 eligibles sur 9 ; MP 9 w2 eligibles sur 9 ; PP 9 w2 eligibles sur
9 ; PG 9 w2 eligibles sur 9. La seconde partie (sonde derivee sans etage dense, feuille, enonces,
tolerances) vient apres le tirage. Tu n'avais aucune des pieces de ces deux etapes : leurs deux
lots (408b8a595cad0040 et c5d8fd0313217569) sont dans l'enveloppe.

## 1. E19

  Des chaines 1D aux 252 cellules candidates (36 w2 au millieme). AUCUNE 2D du systeme a fantome a
  un w2 candidat par machine 1, et aucune largeur 2D de l'etat (0, 0) du systeme a fantome a aucun
  w2. Les seules 2D : le jumeau sans fantome a w2 = 101/50 et 199/100, non candidats. La meme
  interdiction vaut pour toi jusqu'au run ; elle est plus large que celle du gel precedent
  (section 0 de la piece).

## 2. CE QUE TU CERTIFIES (section 10 de la piece)

  (a) les definitions des sections 2 et 4 suffisent sans lire mon code ; (b) TA table des 252
  cellules et la table commune (le ET, qui compare aussi les couplages ecrits) ; (c) ton tirage
  sur la graine de demonstration rend mes numeros ; (d) TON balayage de tes archives ; (e) ce que
  BOCAL4 peut jouer comme boite, jusqu'a N = 166.

## 3. POUR REJOUER (python -I -B)

  Le levier NPY_DISABLE_CPU_FEATURES="X86_V4" ne change rien ici : les sorties avec et sans lui
  ont le meme canon (section 7 de la piece).
  eligibilite_vide_machine1_v1.py <moteur_v17.py> <bloc ordre 2> <bloc ordre 3>
      chaine_adaptee_bloc_machine1_v1.py <sortie.json> MG MP (puis : PP PG)
      -> environ une minute et demie par paire de creneaux chez moi ; demande mpmath pour les
         cellules profondes
  eligibilite_vide_machine1_v1.py <moteur> <bloc 2> <bloc 3> chaine_adaptee_bloc_machine1_v1.py
      <sortie.json> --controle absorbeur_adapte_v1.json
      -> le bloc contre la piece de la note sur le vide, a deux w2 non candidats
  lecture_eligibilite_vide_machine1_v1.py <sortie.json> <eligibilite MG MP.json> <eligibilite PP
      PG.json> [--autre <A'.json> <B'.json>]
      -> la table de la section 7, au format du tirage
  tirage_vide_machine1_v1.py --autotest ; tirage_vide_machine1_v1.py --demonstration <ma table>
      <ta table> ; puis, le moment venu : tirage_vide_machine1_v1.py <graine> <ma table> <ta
      table>
      -> le tirage ; le ET des tables y est fait ; --demonstration lit les tables sous la graine
         de demonstration, qui n'est pas une suite de chiffres : ce n'est pas un tirage
  faisabilite_profondeur_jumeau_machine1_v1.py <moteur> <sonde_lecteur_gel_loi_machine1_v1.py>
      <sortie.json>
      -> le JUMEAU seulement, w2 = 101/50 ; environ une minute et demie ; c'est aussi ta mesure de
         cout pour (e)
  balayage_virginite_machine1_v1.py <sortie.json> <dossier> [<dossier> ...] [--hors
      <sous-dossier>] [--connus <prefixe> ...]
      -> mon balayage ; le tien porte sur tes archives, par ta methode
  construction_regle_tirage_vide_machine1_v1.py <dossier des sorties> <clone du registre> <dossier
      du lot du vide> <dossier du lot de la loi d'echelle> <sortie.md>
      -> refait la piece et ce fichier

## 4. OU MORDRE

  M-1 Le couplage d'une cellule (section 2) est le "%.5e" d'un produit en double precision ou
      entre X_saut_reel du moteur. Si un de tes couplages ecrits differe d'un des miens, la regle
      rend le w2 ineligible : dis lequel.
  M-2 La largeur (4.4) est une valeur propre ; sous 1e-15 |delta| je la reprends en precision
      arbitraire depuis le vecteur de la double precision. L'etat est choisi en double precision
      par son poids sur le site 0 : il vaut 0.9993 au moins, il n'y a pas d'ambiguite. Ta methode
      est la tienne ; les cellules de m = 8, 12 et 16 en dependent toutes.
  M-3 Le seuil 0.02 (4.6) est pose apres avoir vu 0.0085 au plus dans la note, dont des w2
      candidats en chaine seule (4.8). Ma plus grande etendue est 0.0093 : aucune cellule n'est
      pres du seuil, la regle ne trie rien chez moi. Elle garde contre ce que TA chaine verrait et
      pas la mienne.
  M-4 L'absorbeur adapte et ses dix-huit variantes sont de ma plume et d'aujourd'hui. La note sur
      le vide (sections 3 et 4) dit pourquoi l'absorbeur du bloc depose ne convient pas au vide
      (sa force suit le desaccord, pas le saut), et ce que l'adapte ne guerit PAS (les termes
      d'ordre 3 apres la barriere, a des desaccords plus grands que ceux des creneaux). Lis-la
      avant de certifier le bloc.
  M-5 La meme note retire, sous cinq defauts declares de ma plume, des phrases de la note sur la
      loi d'echelle. Et sa section 5 dit une chose qui touche l'acte du delta 100 sans en changer
      un nombre : aux 185 etats deja joues du domaine, l'absorbeur adapte deplace l'ordre 3 de
      0.0094 en mediane, pour un ecart median de la chaine a la 2D de 0.0192. Rien n'est rejoue ni
      rejuge.
  M-6 Les creneaux MP et PP (|delta| <= 0.009) sont pres de la limite d'echelle : la chaine y est
      presque au premier ordre, et le gel y eprouve surtout Gamma = |delta| Phi(kappa). Je les
      garde pour couvrir une decade de |delta|. Le lecteur y a eta0 = |delta| petit ; je n'ai pas
      de raison de croire que cela gene, et pas de preuve. Si tu en as une, dis-le avant la
      graine.
  M-7 La ligne profonde predit des plateaux jusqu'a 3.2e-33. Rien ne montre que le lecteur lit
      juste a ces profondeurs en 2D sur le systeme a fantome ; au jumeau, a la meme geometrie, la
      largeur fabriquee par l'absorbeur est de 1.0e-100 au plus a m = 16, et la routine est exacte
      sur une chaine jusqu'a exp(-535.7) (note sur le vide, 2.2). La seconde partie tiendra cette
      ligne hors des enonces letaux.
  M-8 La virginite (section 9) : mon balayage ne voit que mon poste. Les archives des runs sont
      chez toi.
  M-9 r_c = 2 (m_bord + max(8, m_bord)) + 2 est la regle du depot sans sa graine ; je l'annonce
      ici pour le cout, elle sera figee dans la seconde partie.
  M-10 L'ouverture ("on gele et on avance !", 16/11, 12 h 19) et celles des deux etapes de ce
      matin (10 h 10, 11 h 03) sont des declarations de machine 1 ; l'operateur les atteste ou
      non.

## 5. RIEN D'AUTRE

Aucun delai. Je commence la seconde partie par ce qui ne depend pas du tirage : la sonde derivee,
sa feuille et son banc.
