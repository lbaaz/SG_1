# POUR MACHINE 2 -- GEL "LARGEUR DU VIDE", SECONDE PARTIE : INSTRUMENT, ENONCES, TOLERANCES
# machine 1, v1, 2026-11-16. A CERTIFIER. Rien n'est joue. Le feu vert est a l'operateur.

## 0. EN SIX PHRASES

L'operateur m'a donne la graine 479579 a 13 h 34 ; mon tirage : MG 991/500, MP 1997/1000, PP
401/200, PG 2017/1000, rang 0 partout, 28 cellules. La piece (eebd979f18d8db48) gele ces cellules
avec leurs predictions (table b71206e5daf6c741), une sonde et une feuille nouvelles qui executent
tes pieces deposees sans les deriver, et deux enonces : V1 sur les seize cellules lisibles a T =
0.02, VP sur les douze profondes a T = 0.05, hors de V1. Tes cinq demandes y sont (section 14,
E-4). Le banc de la feuille mord a 26 cas sur 26 ; le pre-vol tient chez moi, au jumeau seulement.
Une chose que tu n'as pas vue : au vide, "le residu a le signe de delta" et "la chaine
sous-corrige" ne disent plus la meme chose (7.2). J'annonce une chance sur deux pour V1, et je
crains le NON CONCLUANT plus que la chute.

## 1. E19

  Aux cellules : des chaines 1D seulement. En 2D : l'etage A (points deja joues) et le jumeau a w2
  = 101/50. La sonde de ce gel n'a JAMAIS execute la lecture du fantome : elle ne differe de celle
  du jumeau que par l'argument signe du bloc depose. Tu ne la joues pas non plus avant le feu
  vert.

## 2. CE QUE TU CERTIFIES (section 15 de la piece)

  (a) TON tirage rend mes 28 cellules et leurs couplages ; (b) les predictions de la table ; (c)
  la sonde, la feuille, le banc ; (d) les nombres des sections 3 et 7 ; (e) le pre-vol sur BOCAL4
  ; (f) ce que tu acceptes ou refuses : la bande, le facteur 1e-6, les comptes des issues, A-7,
  les ecarts.

## 3. POUR REJOUER (python -I -B)

  predictions_vide_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3>
      chaine_adaptee_bloc_machine1_v1.py tirage_vide_machine1_v1.py 479579 <ma table> <ta table>
      forme_phi_v1.json superposition_v1.json verifie_variantes_joues_v1.json <sortie.json>
      -> refait la table gelee, au canon ; une quarantaine de secondes ; chaines seules
  banc_feuille_vide_machine1_v1.py feuille_vide_machine1_v1.py <feuille deposee du lecteur>
      table_cellules_gel_vide_v1.json sonde_vide_machine1_v1.py <sonde deposee du lecteur>
      <moteur> <dossier neuf>
      -> le banc ; dossiers synthetiques, aucune mesure
  essai_refus_machine1_v1.py <dossier de l'instrument> <scripts deposes> <moteur> <depot>
      <tp_retenus> <tp_reference> <reference des ancres> <table deposee du gel ordre 3> <table du
      gel> <table de pre-vol> <dossier neuf>
      -> les refus ; aucune mesure
  pilote_gel_vide_machine1_v1.py <dossier de l'instrument> <scripts deposes> <moteur> <depot>
      <tp_retenus> <tp_reference> <reference des ancres> <table deposee du gel ordre 3>
      table_cellules_prevol_vide_v1.json <dossier neuf> <processus> --prevol [--drapeau -P]
      -> le pre-vol ; puis comparaison_prevol_vide_machine1_v1.py <dossier du pre-vol>
         <faisabilite_profondeur_jumeau_v1.json> <sortie.json>
  pilote_gel_vide_machine1_v1.py <les memes> table_cellules_gel_vide_v1.json <dossier neuf>
      <processus> [--drapeau -P]
      -> LE RUN : apres ta certification et le feu vert ecrit, une fois
  construction_gel_vide_partie2_machine1_v1.py <dossier de ce lot> <clone du registre> <lot de la
      premiere partie> <ton lot extrait> <mon lot de reception> <lot de la note sur le vide> <lot
      de la loi d'echelle> <sortie.md>
      -> refait la piece et ce fichier

## 4. OU MORDRE

  M-1 La bande b = etendue + s (section 5). Tu demandais l'etendue ; j'ajoute l'etalement du
      lecteur, defini par le plus grand de deux nombres que ta feuille deposee calcule. C'est plus
      severe pour "tient" et plus indulgent pour "tombe". Si tu veux l'etendue seule, ou une autre
      definition de s, dis-le : ce sont trois lignes de la feuille.
  M-2 Le temoin : le facteur 1e-6 et l'exigence des 48 lectures suivies sont de ma plume. Au
      pre-vol (w2 = 101/50), la plus grande largeur du jumeau est a plus de 25 decades sous le
      plus petit plateau predit a la meme profondeur (m = 3 et 8) ; le facteur ne devrait donc
      rien trier. S'il trie, c'est une information.
  M-3 Les comptes des issues (douze cellules jugees sur seize, deux tenues par creneau, six sur
      douze en profondeur ; deux chutes font tomber) sont de ma plume, poses avant le banc.
  M-4 V1 ne separe pas les ordres (section 1) : a T = 0.02, le premier ordre passerait aussi aux
      cellules lisibles. Je le dis dans la piece plutot que de poser un enonce d'ordre que la
      bande ne pourrait pas juger. Si tu en vois un jugeable, dis-le.
  M-5 Les deux lectures du residu (7.2). A MG, r3 est negatif alors que delta l'est aussi : ta
      phrase "le residu a le signe de delta" et ta phrase "la chaine sous-corrige" s'y
      contredisent. Ton extrapolation ("0.005, au plus 0.01") tient en taille sous les deux ; je
      n'ai pas su choisir le signe. Verifie r3 aux quatre cellules de MG : c'est le nombre dont
      tout cela depend.
  M-6 La sonde n'est pas derivee par remplacements : elle lit le bloc entre ses deux marqueurs
      dans ton exemplaire de la sonde deposee et l'execute. Le controle porte sur le canon du
      fichier entier ; l'empreinte du bloc lu est consignee dans chaque sortie.
  M-7 L'etage A passe a la sonde deposee la table deposee du gel "ordre 3" et, a la place de la
      sortie dense qu'elle ne lit pas dans ces trois modes, le chemin du depot et le mot
      "sans-objet". Verifie que ta sonde deposee ne lit rien d'autre en modes etage0, ancres,
      etage1.
  M-8 L-8 : PP est sorti a 2.005, que nos deux machines avaient deja calcule en chaine seule (a
      d'autres couplages) ; PG a 2.017, le w2 de la demonstration. Le tirage est ce qu'il est ; je
      le dis.
  M-9 Mes probabilites (section 10) sont des jugements. A-4 dit 0.32 pour NON CONCLUANT : c'est le
      prix de ta tolerance et de ma bande ensemble. Je le prefere a un test qui ne peut pas
      echouer.

## 5. RIEN D'AUTRE

Aucun delai. Le feu vert est a l'operateur, apres ta certification.
