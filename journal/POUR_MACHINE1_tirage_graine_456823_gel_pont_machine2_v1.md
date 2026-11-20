# POUR MACHINE 1 -- le tirage du gel "pont" sur la graine 456823, par machine 2

machine 2, 2026-11-17 (matin). Hors chaine. Aucune 2D n'a ete jouee a ces w2 ; aucune ne le sera avant ta seconde partie, sa certification et le feu vert ECRIT de l'operateur. Rien n'est depose. Rien d'autre n'est demande.

## 0. Statut de la graine

- **La graine est 456823.** L'operateur l'a donnee par ecrit dans ma session, le 17/11 vers 09 h 55 ("456823 la graine"). Mon horloge indiquait 09:56:43 au moment du tirage. Elle est reportee telle quelle (aucun zero de tete).
- **Les conditions du gel (section 3) etaient remplies de mon cote** : ma certification de ta piece etait rendue (lot acfecb6da73f20ae) et la table commune existait (canon B 0c10ddbf2813d809). Je n'avais ni choisi, ni propose, ni commente la graine avant de la recevoir.
- **Je ne sais pas si tu as deja recu ma certification ni la graine** : c'est a l'operateur de te la donner, par ecrit, comme a moi.

## 1. Le tirage (mon code, ma table commune)

Journal `tirage_graine_456823_machine2_v1.log` :

    MG rang 0 : sha256 = bab2ed478849ce6c... ; modulo 8 = 3 -> w2 = 1.985 ELIGIBLE
    PG rang 0 : sha256 = 7ba5f5c18c4df1e2... ; modulo 8 = 7 -> w2 = 2.019 ELIGIBLE
    RESULTAT : MG3 : w2 = 1.985, g = 3.63872e-03 ; MG4 : w2 = 1.985, g = 2.77765e-03 ; MG5 : w2 = 1.985, g = 2.20823e-03 ; PG3 : w2 = 2.019, g = 5.23478e-03 ; PG4 : w2 = 2.019, g = 3.99601e-03 ; PG5 : w2 = 2.019, g = 3.17683e-03

**Six cellules : MG3, MG4, MG5 a w2 = 1.985 (397/200) ; PG3, PG4, PG5 a w2 = 2.019 (2019/1000).** Les deux creneaux sortent au rang 0 : aucun rang de repli n'a servi.

## 2. Recoupements

- **Ton code.** `tirage_pont_machine1_v1.py` (non edite), avec TA table d'eligibilite ET la mienne (il en prend le ET) : memes six cellules, memes couplages ecrits (journal `tirage_graine_456823_code_m1_machine2_v1.log`) :

        tables : 2 ; w2 eligibles dans toutes : MG 5 sur 8, PG 8 sur 8
        creneau MG rang 0 : numero 3 sur 8 -> w2 = 397/200 (1.985) : ELIGIBLE, retenu
        TIRAGE : 6 cellules

- **Une troisieme voie pour le hachage** : `sha256sum` de coreutils, sans Python, sur les chaines `456823|MG|0` et `456823|PG|0` ; memes empreintes, memes restes modulo 8 (journal `controle_hachage_sha256sum_graine_456823_machine2_v1.log`) :

        sha256sum(456823|MG|0) = bab2ed478849ce6c... ; modulo 8 = 3
        sha256sum(456823|PG|0) = 7ba5f5c18c4df1e2... ; modulo 8 = 7

  Les listes croissantes de la section 2 du gel sont numerotees a partir de 0 : le numero 3 de MG est 1.985 (1.981, 1.983, 1.984, **1.985**, ...), le numero 7 de PG est 2.019 (2.011, 2.012, 2.013, 2.014, 2.015, 2.016, 2.018, **2.019**).
- **Ton tirage est a toi** : chaque machine tire par son code ; si tes six cellules different des miennes, ou si tu trouves PAS DE GEL, dis-le : "PAS DE GEL tant que l'ecart n'est pas explique par ecrit, et la graine n'est pas changee" (gel, section 6).

## 3. Les six cellules : des faits, aucun jugement

Nombres lus dans mes details d'eligibilite (journal `cellules_tirees_graine_456823_machine2_v1.log`). Colonnes : cellule, w2, |delta|, g, m_bord, e_bord, etendue au vide, plus grande etendue du lisse, plus grand pas, puis le rang de ce pas parmi les 48 cellules (1 = le plus grand) et sa marge au seuil 0.10, puis le rang de l'etendue du lisse et sa marge au seuil 0.03 :

    PG5      2.019    0.019    3.17683e-03  5       0.0961  0.0063        0.0219             0.0384   | 27                                                 +0.0616       | 1                          +0.0081
    MG5      1.985    0.015    2.20823e-03  5       0.0743  0.0026        0.0110             0.0869   | 9                                                  +0.0131       | 21                         +0.0190

(les quatre autres lignes sont dans le journal.) Deux faits utiles a ta seconde partie :

- **Chacun des deux w2 tires a le plus grand |delta| parmi les w2 eligibles de son creneau** :

        le w2 tire de MG a le plus grand |delta| parmi les w2 eligibles de MG : True ; celui de PG a le plus grand |delta| parmi les w2 eligibles de PG : True

  A 1.985 (|delta| = 0.015), la condition (v) tient avec ses marges les plus etroites parmi les w2 eligibles de MG : 0.0690, 0.0774 et 0.0869 pour 0.10 aux trois profondeurs, au lieu de 0.0334 a 0.0411 a 1.989.
- **PG5 a 2.019 est, des 48 cellules, celle dont l'etendue du lisse d'ordre 3 est la plus grande** (0.0219, marge 0.0081 au seuil 0.03 ; c'est le plus grand e_bord, 0.0961, pour un seuil de 0.7).

Ma premiere sortie de ce script de lecture etait fausse : il lisait l'eligibilite de la cellule a 3 barreaux au lieu de celle du w2 (une cellule eligible ne fait pas un w2 eligible : il en faut trois). J'ai garde ce premier passage (`..._premier_passage_eligibilite_par_cellule.log`), dont la derniere ligne dit, a tort :

    le w2 tire de MG a le plus grand |delta| parmi les eligibles de MG : False

(1.983 et 1.984 sont eligibles a 3 barreaux sans que leurs w2 le soient ; la liste des w2 eligibles de MG est 1.985 a 1.989.)

## 4. Suite

(3) chaque machine tire : le mien est ci-dessus, a toi de faire le tien et de comparer ; (4) tu ecris la seconde partie (instrument, table gelee des six cellules, enonces et tolerances) ; (5) je la certifie, l'operateur donne le feu vert ECRIT, je joue UNE fois. E19 : aucune des deux machines ne joue de 2D a ces w2 avant cela.

## 5. Pieces

Chaque piece est citee avec son canon (empreinte B, 16 hex). Le canon du lot est celui du manifeste.

    cette note
    91c3fe58f0b3f7b0  certif_gel_pont_partie1_machine2/tirage_graine_456823_machine2_v1.log
    abbe1a91512de86c  certif_gel_pont_partie1_machine2/tirage_graine_456823_code_m1_machine2_v1.log
    48f43580769af180  certif_gel_pont_partie1_machine2/controle_hachage_sha256sum_graine_456823_machine2_v1.log
    fd6e2a474e71a581  certif_gel_pont_partie1_machine2/cellules_tirees_machine2_v1.py
    1e05138268fc424a  certif_gel_pont_partie1_machine2/cellules_tirees_graine_456823_machine2_v1.log
    713a04f04440b0ee  certif_gel_pont_partie1_machine2/cellules_tirees_graine_456823_machine2_v1_premier_passage_eligibilite_par_cellule.log
    0c10ddbf2813d809  certif_gel_pont_partie1_machine2/table_commune_pont_v1.json
    f144cbd51946b5f4  certif_gel_pont_partie1_machine2/tirage_pont_machine2_v1.py
    (ce script)  fabrique_lot_tirage_graine_456823_pont_machine2_v1.py
