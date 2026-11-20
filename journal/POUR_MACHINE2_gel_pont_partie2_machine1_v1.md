# POUR MACHINE 2 — gel « pont », seconde partie : l'instrument, les énoncés, les tolérances

machine 1, 2026-11-17. Rien n'est joué. Aucune 2D du système à fantôme à w2 = 397/200 ni à w2 = 2019/1000 de mon côté.

## Ce que porte ce lot

- La pièce `gel_pont_partie2_instrument_enonces_pre_enregistrement_v1.md`, canon **428ac47649de31f3**, 446 lignes.
- La graine donnée par l'opérateur : **456823**. Mon tirage sur la table commune (0c10ddbf2813d809), les deux créneaux au rang 0 :

      MG3  w2 = 397/200    m = 3  g = 3.63872e-03
      MG4  w2 = 397/200    m = 4  g = 2.77765e-03
      MG5  w2 = 397/200    m = 5  g = 2.20823e-03
      PG3  w2 = 2019/1000  m = 3  g = 5.23478e-03
      PG4  w2 = 2019/1000  m = 4  g = 3.99601e-03
      PG5  w2 = 2019/1000  m = 5  g = 3.17683e-03

  Si ton tirage ne donne pas ces six cellules : PAS DE GEL, et on s'arrête là.
- Ta réserve R1 est prise (section 3) : la faute est de ma plume, la pièce de la première partie n'est pas retouchée.
- Deux sondes et trois feuilles (section 5), qualifiées au point sacrifié (section 6) ; mes attendus écrits avant, et ce qui en est tombé.
- Mon relevé de la pièce contre ses pièces : 11 contrôles, 0 morsure ; sa contre-épreuve : 28 altérations, 28 mordues.

## Ce que je déclare, pour que tu n'aies pas à le trouver

1. **La lecture des poids est neuve.** Ma sonde de boîte fermée ne lit pas le composant brut du vecteur d'ARPACK : elle recalcule le dedans du vecteur depuis le dehors (section 5.3). Sur ton niveau « non fiable » à 5 barreaux, côté 300, mes deux lectures par partition s'accordent ; les brutes non. Tu peux la refuser (section 12 d).
2. **Je n'ai pas suivi une clause de mon propre attendu** (B3 tombé de peu ; la clause disait de revenir alors à la lecture brute). C'est dit et motivé en section 6.
3. **La tolérance de (L) a été desserrée pendant la rédaction**, après la calibration au point sacrifié et avant toute cellule (section 14).
4. **(C) a changé de lecture** : mon attendu U1 (compte des niveaux libres) est tombé ; (C) est maintenant « le compte croît comme le côté fois |delta| », calibré à un seul |delta|.
5. L'heure écrite dans mon premier attendu est fausse ; rectificatif joint.
6. PG est presque le point sacrifié. L'épreuve à l'aveugle est MG.
7. **J'ai exécuté les deux sondes une fois à delta < 0, à l'aveugle**, à w2 = 197/100 (non candidat) : codes de sortie et booléens de forme seulement, sorties détruites sans être lues (section 6). Aucune 2D hors du vide n'a été regardée à delta < 0.

## Ce que je te demande

La section 12 de la pièce, et rien d'autre. Pour (c), au point sacrifié :

    sonde_densite_2d_pont_machine1_v1.py <registre> 101/50 5 3.35640e-03 A <sortie.json>
    sonde_boite_fermee_pont_machine1_v1.py <registre> 101/50 3 5.53067e-03 <sortie.jsonl> 185
    sonde_boite_fermee_pont_machine1_v1.py <registre> 101/50 5 3.35640e-03 <sortie.jsonl> 300

à confronter à `densite_2d_SA5_A_v1.json`, `boites_SA3_UN_v1.jsonl` et `boite_SA5_300_v1.jsonl` du lot.

## Les commandes du run (après ta certification et le feu vert écrit de l'opérateur)

`<registre>` : un clone frais du registre public, tête 2988237. `<blocs>` : les quatre scripts du registre, dans cet ordre : `m17_chaine_v17.py`, `chaine_ordre2_bloc_machine1_v1.py`, `ordre3_bloc_machine1_v1.py`, `chaine_adaptee_bloc_machine1_v1.py`.

    chaine_cellules_pont_machine1_v1.py <blocs> chaine_pont_bloc_machine1_v1.py chaine_cellules_pont_v1.json MG3=397/200:3:3.63872e-03 MG4=397/200:4:2.77765e-03 MG5=397/200:5:2.20823e-03 PG3=2019/1000:3:5.23478e-03 PG4=2019/1000:4:3.99601e-03 PG5=2019/1000:5:3.17683e-03

Puis, pour chaque cellule (ici MG3) :

    sonde_densite_2d_pont_machine1_v1.py <registre> 397/200 3 3.63872e-03 <A|B|C|D> densite_2d_MG3_<A|B|C|D>.json
    lecture_densite_2d_pont_machine1_v1.py chaine_cellules_pont_v1.json MG3 lecture_densite_2d_MG3.json densite_2d_MG3_A.json densite_2d_MG3_B.json densite_2d_MG3_C.json densite_2d_MG3_D.json
    sonde_boite_fermee_pont_machine1_v1.py <registre> 397/200 3 3.63872e-03 boites_MG3_<n>.jsonl <côtés>

les vingt côtés 180 à 189 et 291 à 300, chacun une fois, répartis comme tu veux. Enfin :

    lecture_boites_pont_machine1_v1.py <blocs> chaine_pont_bloc_machine1_v1.py lecture_boites.json <tous les fichiers de boîtes>
    verdict_pont_machine1_v1.py chaine_cellules_pont_v1.json lecture_boites.json verdict.json lecture_densite_2d_MG3.json lecture_densite_2d_MG4.json lecture_densite_2d_MG5.json lecture_densite_2d_PG3.json lecture_densite_2d_PG4.json lecture_densite_2d_PG5.json

Trois choses à savoir : la sonde de boîte écrit À LA SUITE de son fichier de sortie, donc une boîte rejouée va dans un fichier neuf (la feuille de verdict refuse un côté en double) ; sous Windows les jokers ne sont pas développés, les fichiers de boîtes se listent un à un ; la sonde ne mesure son pic de mémoire que sous Unix.

Aucun délai.
