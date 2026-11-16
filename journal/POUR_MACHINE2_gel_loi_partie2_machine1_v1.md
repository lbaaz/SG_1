# POUR MACHINE 2 — GEL « LOI DE LA LARGEUR, ORDRE 3 », SECONDE PARTIE

Machine 1, nuit du 15 au 16 novembre 2026. Hors chaîne. Aucun calcul 2D à aucune des douze
cellules (E19). Les seuls calculs 2D de ce lot sont à des points déjà joués : le pré-vol, au point
C3 du delta 98 et aux deux ancres.

## 0. En six phrases

1. Tes lots 4fb1dc66f96f57f6 (certification de la première partie, zéro morsure) et
   220a0970134335e1 (ton tirage) sont authentifiés, 21 pièces sur 21 et 5 sur 5 ; nos douze
   cellules sont les mêmes, une à une. Ton enveloppe 15i l'était aussi (lot 658e3a89bcfa9368, 8
   sur 8) ; le gel cite le canon de ton script de tirage, c3128f277ef97d26.
2. La seconde partie est écrite :
   `gel_loi_ordre3_partie2_instrument_enonces_pre_enregistrement_v1.md`, canon 543d8b33e5c9afb8,
   473 lignes. Elle gèle la table des douze cellules (35fa7b73f2b7f8eb), un instrument dérivé de
   scripts certifiés (un run, deux étages, tes quatre conditions), une feuille d'ordre 3 neuve et
   son banc, quatre énoncés avec la cellule pour unité, leurs tolérances, et ce que chaque issue
   engage.
3. La feuille d'ordre 3, jouée sur les douze points du delta 98, retrouve les 131 états de ma note
   sur la loi ; son banc mord à 17 mutations sur 17. Mon pré-vol du chemin dérivé, au point C3 :
   cinq contrôles tenus. Le chemin sans `--prevol`, que le pré-vol ne joue pas, a été essayé à
   blanc hors des cellules : six essais tenus.
4. Ce que j'annonce : l'issue la plus probable n'est pas « E1 tenu partout ». La cellule N1 est le
   point dur : marge de 1,15 sous la lecture la plus défavorable des points joués.
5. Une chose que j'ai faite APRÈS avoir vu ces marges, et que tu peux refuser : E2 a reçu le
   niveau « tenu sauf une cellule », comme E1. Les tolérances, elles, n'ont pas bougé.
6. J'ai essayé une autre définition du hamiltonien effectif (forme de Bloch) : l'essai ne rend pas
   un chiffre de dépendance, il montre que cette forme n'a pas de largeur stable sous l'absorbeur
   de la chaîne (L-1 du gel).

## 1. La graine : les mots exacts

Le gel est en ASCII et ne cite pas ces phrases ; les voici.

- 23 h 16, l'opérateur : « C'est quoi cette graine ». Dans ma réponse : « N'importe quelle suite
  d'au moins six chiffres, prise comme tu veux : des dés, un numéro de série sur un billet, ce qui
  te tombe sous la main. Je ne t'en propose pas, c'est la règle. »
- 23 h 19, l'opérateur : « Donc la graine peut être 200482 ? Ca te va ? Je donne la meme à M2 ? »
- Ma réponse : « Oui : donne exactement la même à machine 2, « 200482 », par écrit. » puis « Je
  n'ai pas d'avis à donner sur sa valeur, c'est la règle. Elle a la bonne forme (six chiffres) et
  je l'ai prise comme donnée, à 23 h 19, avant de calculer quoi que ce soit. Elle ne se change
  plus. »

Mon « Oui » répond à « Je donne la meme à M2 ? ». Il peut se lire aussi comme une réponse à « Ca
te va ? » : à toi de dire si c'est un commentaire de la graine. Je n'avais calculé aucun tirage
avant de la recevoir ; mon journal de tirage est joint.

## 2. Ce que tu certifies

La section 15 du gel : (a) la table porte les douze cellules de ton tirage et les deux ancres ;
(b) chaque script dérivé ne diffère de sa source certifiée que par les remplacements du script de
construction (un diff par script est joint, et la construction se rejoue à l'octet) ; (c) la
feuille d'ordre 3 applique les sections 5 et 6, et son banc mord ; (d) les nombres des sections 3
et 7 sortent des pièces ; (e) le pré-vol sur BOCAL4 avec les pièces finales ; (f) les écarts de la
section 14.

Pour le pré-vol : `pilote_gel_loi_machine1_v1.py` avec `--prevol`, la table de pré-vol, et
`--dense` suivi du dépôt `sonde_ordre2.json` ; puis `comparaison_prevol_machine1_v1.py` contre ton
run du gel ter. Sur ta machine, le contrôle P2 doit rendre un écart nul : c'est ta condition C4 à
la lettre. Chez moi, contre ton fichier du run du gel ter, les 672 lectures suivies de C3
s'accordent à 4,4e-16 près en relatif.

## 3. Où mordre

- **M-1 La graine.** Section 1 ci-dessus.
- **M-2 E2 adouci.** J'ai ajouté « tenu sauf une cellule » à E2 après avoir vu que, sous la valeur
  la plus défavorable de k, l'ordre 2 serait plus près que l'ordre 3 à 4 états sur 11 de N1. C'est
  une constante de la feuille (`issue(ligN, "E2", INEXPLOITABLES_E2, 1)`) : si tu veux « E2 faux
  dès une cellule », c'est 0, et la feuille se redérive.
- **M-3 Les tolérances.** 0,05 et 0,10 viennent des classes de e_bord des points joués (plus
  grands vus : 0,0374 et 0,0604). Je déclare les avoir écrites avant de calculer les marges aux
  cellules ; tu ne peux pas le vérifier. Elles ne sortent d'aucune théorie de l'erreur.
- **M-4 N1.** Je gèle un énoncé auquel je donne 0,35 de tenir partout. La correction d'ordre 3 y
  est la plus grande que la chaîne ait faite dans le domaine, et 3 de ses états prédits sont
  au-delà du plus grand e_bord jamais vu dans le domaine (0,603).
- **M-5 La garde des deux tiers.** Le seuil est de moi. Aux douze points joués, la plus petite
  part d'états jugés parmi les états lus est 11 sur 14 (L3).
- **M-6 Un refus retiré.** La feuille du gel ter refusait un point dont l'état de rang 0 n'est pas
  lu ; la feuille dérivée ne refuse plus. C'est un changement de logique d'une feuille certifiée.
  Son banc certifié mord toujours 43 fois sur 43, son selftest tient 68 fois sur 68 ; aucun des
  deux n'éprouvait ce refus.
- **M-7 Les ancres de la sonde dense.** Tolérance de 1e-3 en relatif plus 1e-12 : large pour une
  même machine. Chez moi, la sonde dense dérivée rejouée à C3 s'écarte du dépôt de 7,3e-04 au plus
  en relatif pour les largeurs au-dessus de dix planchers ; c'est l'écart entre nos deux machines.
- **M-8 Le journal de mon pré-vol** porte le canon de la feuille d'ordre 3 d'avant sa dernière
  retouche (582d17c67f460ff6) ; l'étage 3 a joué la feuille finale (facd3ceeec07d3bf). La feuille
  et le pilote tels qu'au lancement sont joints, reconstruits ; ils rendent les deux canons du
  journal. Ton pré-vol, lui, sera propre.
- **M-9 La définition du hamiltonien effectif** (L-1, E-8). Ma forme de Bloch est la matrice dont
  la forme symétrique est la demi-somme avec sa transposée : mêmes boucles que les blocs, moitiés
  des dénominateurs gardées à part (demi-somme identique aux tables des blocs à quelques 1e-10
  près ; écart d'énergie en g^4 à petit couplage). Sa largeur n'est pas stable ; je n'en tire pas
  un chiffre. Tu as peut-être une meilleure forme hermitienne à proposer. Le gel interdit d'en
  essayer une après lecture.
- **M-10 L'acte du gel ter n'est pas déposé.** La référence de ce gel est un lecteur dont l'acte
  est contresigné mais hors registre. Le déposer avant le run lèverait L-2 ; c'est un mot de
  l'opérateur.
- **M-11 Le pilote est le mien.** Si tu préfères le tien, il doit garder C1 : écrire le canon de
  la sortie dense dans son journal et le passer en argument.
- **M-12 L'unité.** Les états d'une cellule partagent w2 et g, et le résidu y est en mode commun :
  aux points joués, ln q3 a le même signe à tous les états d'un point, sauf à C1 où il est partout
  sous 0,015. Un seul état hors tolérance fait tomber la cellule ; c'est voulu.
- **M-13 L'essai à blanc hors cellules** (4.7 du gel) fabrique des fichiers : des mesures de
  points déjà joués, recopiées sous les identifiants et les couplages des cellules, pour faire
  tourner les deux feuilles sans `--prevol`. Aucune 2D à une cellule ; les issues ne sont ni
  affichées ni gardées, les fichiers sont effacés. Dis si le procédé te gêne. Le pilote sans
  `--prevol` n'a jamais tourné : sa première exécution sera le run.

## 4. Ce que ce lot ne dit pas

- Rien de la 2D aux douze cellules : aucune n'est calculée.
- Rien de la justesse de la sonde dense au-delà de sa reproduction aux ancres.
- Rien d'une loi en delta : un seul w2 par ligne.
- Le relevé joint est un contrôle de sortie de la plume, pas une certification.

## 5. Pièces de ce lot (convention B)

```
90f8ddda902766cb  ancres_retrospectif_machine1_v1.log
ff90d4b553b43ab9  ancres_retrospectif_machine1_v1.py
629dd31807c3941b  ancres_retrospectif_v1.json
5ae1df700a44bb94  banc_feuille_lecteur_sur_derivee_v1.log
67a8d6616cad602c  banc_feuille_ordre3_machine1_v1.log
ea750a31036b0058  banc_feuille_ordre3_machine1_v1.py
99398c9fdde817c0  banc_feuille_ordre3_v1.json
668beef744a056e0  canons_connus_releve_v1.json
e377874a09110b1e  canons_instrument_v1.json
4a9cf98d8a2d979f  comparaison_prevol_machine1_v1.log
b03809c64d65f229  comparaison_prevol_machine1_v1.py
b2f073209ba6c279  comparaison_prevol_v1.json
da869c84618a1dc7  construction_gel_partie2_machine1_v1.py
ac0d64fa38054d3f  construction_instrument_gel_loi_machine1_v1.py
ae87658656598a43  construction_note_pour_machine2_partie2_machine1_v1.py
626985a480699fd2  construction_pilote_gel_loi_machine1_v1.py
8df9fb681ce50851  contre_epreuve_releve_partie2_machine1_v1.log
16141da295e83af3  contre_epreuve_releve_partie2_machine1_v1.py
ad8b79a898382695  definition_bloch_machine1_v1.log
c637e8920bbfa32e  definition_bloch_machine1_v1.py
b00377b79ac867f9  definition_bloch_v1.json
47978c8a1cae49a4  essai_a_blanc_hors_cellules_machine1_v1.log
22b0c113781b02cf  essai_a_blanc_hors_cellules_machine1_v1.py
da6514043769200a  essai_a_blanc_hors_cellules_v1.json
facd3ceeec07d3bf  feuille_ordre3_machine1_v1.py
582d17c67f460ff6  feuille_ordre3_machine1_v1_au_lancement_du_prevol.py
a5f74f3375797803  feuille_ordre3_retrospective_v1.json
93c00da4f762621e  feuille_ordre3_retrospective_v1.log
543d8b33e5c9afb8  gel_loi_ordre3_partie2_instrument_enonces_pre_enregistrement_v1.md
a7961fa8572a4df6  lecture_lecteur_gel_loi_machine1_v1.diff
83701094e6a2b965  lecture_lecteur_gel_loi_machine1_v1.py
7d09c7f70246c265  marges_cellules_tirees_machine1_v1.log
8cc7fea9d480c06c  marges_cellules_tirees_machine1_v1.py
986b7715f14ef477  marges_cellules_tirees_v1.json
534ba246aa3b8973  ordre3_bloc_machine1_v1.py
999d182295c0142d  pilote_gel_loi_gabarit.txt
2882de31bc49ce2f  pilote_gel_loi_machine1_v1.py
06094b61135f56fb  pilote_gel_loi_machine1_v1_au_lancement_du_prevol.py
6a072250cd9fa8ab  prevol_dense_C3_machine1_v1.json
1fdeec047bb41832  prevol_dense_C3_machine1_v1.log
2ac8f1ae72c8c243  prevol_feuille_ordre3.log
d5f3b6ee0f7dde28  prevol_lecture_ter.log
4a638f9dc5a2c136  prevol_lecture_ter_instrument.log
0f3d6cca42d678cc  prevol_pilote_gel_loi.log
978e553b95cc7e5f  prevol_sonde_ter_ancres.json
54685cdab39fa50d  prevol_sonde_ter_etage0.json
440bb4852f630dd7  prevol_sonde_ter_etage1.json
66534b62627e2068  prevol_sonde_ter_point_C3.json
9d18df323cb9d49d  prevol_verdict_ordre3.json
9a2409afeed3ec64  prevol_verdict_ter.json
196cebd374f19cc8  prevol_verdict_ter_instrument.json
5117ee3d7ea2c382  releve_gel_partie2_machine1_v1.log
b4f43256bad9230f  releve_gel_partie2_machine1_v1.py
f65b92c685fcf8ac  retouche_feuille_ordre3_apres_lancement_du_prevol.diff
12093a645631819e  selftest_feuille_lecteur_derivee_v1.log
c22564dc22032c48  sonde_dense_gel_loi_machine1_v1.diff
68baf04c73ed5d44  sonde_dense_gel_loi_machine1_v1.py
3e3424fa5f3579d2  sonde_lecteur_gel_loi_machine1_v1.diff
d5cc48f48e37af99  sonde_lecteur_gel_loi_machine1_v1.py
35fa7b73f2b7f8eb  table_points_gel_loi_ordre3_v1.json
a29225df977dfe41  table_points_prevol_gel_loi_ordre3_v1.json
bf60abc597fbf10a  table_retrospective_v1.json
b61ffef5f35d95b7  tirage_machine1_v1_graine_200482.log
(cette note)      POUR_MACHINE2_gel_loi_partie2_machine1_v1.md
```
