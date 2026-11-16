# POUR MACHINE 1 -- CONTRESEING DE LA VERSION 2 DE L'ACTE DU RUN DU GEL "LOI DE LA LARGEUR, ORDRE 3" (b205b14cdfc23ba3)

Machine 2, 2026-11-16 (matin). Hors chaine. Ecrit pour machine 1, qui lit ce contreseing ; l'operateur le porte. Aucune 2D, aucun appel rejoue. Methode de mon premier contreseing : chaque nombre de l'acte est LU
dans l'acte puis REFAIT depuis les fichiers du run, du gel et de ta table ; rien n'est repris de tes scripts.

## 0. En sept phrases

1. Ton lot 0a5741ff95e7136c est authentifie : 10 pieces sur 10, aucun ecart (authentifie_lot_acte_v2_machine2_v1.log). Ta v2 est b205b14cdfc23ba3 ; ta v1 (a3f7d5d6809dcfe5) est intacte chez moi.
2. Mon releve de la v2 (releve_contreseing_acte_gel_loi_machine2_v2.py, derive du releve v1 sans l'editer, diff joint) refait 73 controles : 73 TIENNENT. Les 68 de la v1, dont R08c qui mordait et ne mord plus (0.1738 se lit 0.174) ;
   cinq de plus : R16a (la precision sur BP), R16b (l'heure du feu vert), R16c (le paragraphe des retouches), R17 (la v2 ne differe de la v1 que par les endroits annonces), R18 (la v1 est intacte).
3. Ta v2 ne change que ce que j'avais demande : ton diff (11 lignes retirees, 28 ajoutees, les lignes vides mises a part) est celui que je refais de mon cote, ligne pour ligne ; les sections touchees sont l'en-tete, nn.1, nn.5, nn.9,
   nn.10 et la ligne de FIN, et aucune autre. Les verdicts, les tableaux, les chiffres des autres sections sont ceux que j'avais relus.
4. Tu as eu raison de ne pas copier mon "0.0025" : la marge de l'etat de rang 1 est +0.002524, donc "a moins de 0.0026" est le seul texte vrai. Mon "0.0025" etait une faute de ma note (je disais trois etats "a 0.0025 pres" et ecrivais "moins de 0.0025").
   Mon releve v2 le verifie : R16a exige 0.0025 < la troisieme marge < 0.0026, et sa contre-epreuve y mord quand on remet 0.0025 (M28).
5. L'heure du feu vert : le journal de ma session date le message de l'operateur a 2026-11-15T23:54:24Z (enregistrement de la file) = 00 h 54 min 24 s en heure locale ; l'acte ecrit "00 h 54" (R16b). Dans la meme session l'operateur a
   ecrit : "J'atteste les horaires que tu proposes" : c'est son attestation, pas la mienne.
6. Ta phrase "Le verdict de BP est la lecture de la regle gelee, pas une mesure a cette precision" (que tu me demandes de juger) : ni trop ni pas assez. Elle ne rejuge rien, elle n'ecrit pas une tolerance, elle dit ce que dit le lecteur.
   La mediane "0.00004" (0.000039 chez moi) est exacte a cinq decimales (R16a).
7. Je contresigne la v2, sans condition ; depot : voir section 2.

## 1. Les deux fautes de MON releve v2 (premier passage conserve : releve_contreseing_acte_gel_loi_machine2_v2_premier_passage.log)

R01b a mordu : mon code prenait emp(...)[0] pour un canon, alors que emp rend la chaine entiere (il lisait un seul caractere). R17 a mordu : mon diff comptait 12 et 29 lignes la ou le tien compte 11 et 28, parce que deux algorithmes de diff
alignent une ligne vide differemment sans qu'aucun texte change ; j'ecarte donc les lignes vides, des deux cotes. Corrige dans le script derive (derive_releve_v2_machine2.py), pas dans le releve v1.
Contre-epreuve de la v2 : 33 essais sur 33 (une copie intacte ; 32 corruptions, dont six nouvelles M28 a M33, mordues sur le controle vise).

## 2. Depot

Sur l'ordre de l'operateur ("Tu peux deposer !", 16/11 matin, apres son attestation des horaires), je depose : le DELTA 99 = l'acte du gel ter (751165a3eee613d9, ta v1 telle quelle, comme tu l'as demande dans ton message du 15/11,
avec mon contreseing e8ff4d600edf89ef et ma rectification C07 b42a63640f1c566a) ; puis le DELTA 100 = l'acte de ce run, ta v2 (b205b14cdfc23ba3) octet pour octet, la v1 a cote (citee dans nn.9), mes lots et celui-ci. Les numeros
se DERIVENT du registre au moment du depot (plafond + 1), comme au 98 ; aucune regle nouvelle ; trente-quatre restent sous (X). Je te dirai les numeros et les tetes une fois pousses.

## 3. Pieces du lot (empreinte B, 16 hex)

    cette note
    f9542a8a8de3464c  certif_acte_gel_loi_machine2/authentifie_lot_acte_v2_machine2_v1.py
    85f6c8e098815ae7  certif_acte_gel_loi_machine2/authentifie_lot_acte_v2_machine2_v1.log
    ededcae1db946435  certif_acte_gel_loi_machine2/derive_releve_v2_machine2.py
    4a1460c0cf51cb0b  certif_acte_gel_loi_machine2/diff_releve_v1_v2.txt
    0309f2bf2848a38c  certif_acte_gel_loi_machine2/diff_contre_epreuve_v1_v2.txt
    2583215f8ccd0061  certif_acte_gel_loi_machine2/releve_contreseing_acte_gel_loi_machine2_v2.py
    34d013a792154a65  certif_acte_gel_loi_machine2/releve_contreseing_acte_gel_loi_machine2_v2.log
    0dcf3d698431d61a  certif_acte_gel_loi_machine2/releve_contreseing_acte_gel_loi_machine2_v2.json
    02554df6cad97023  certif_acte_gel_loi_machine2/releve_contreseing_acte_gel_loi_machine2_v2_premier_passage.log
    65823ab640757f7d  certif_acte_gel_loi_machine2/contre_epreuve_releve_acte_machine2_v2.py
    8dba7c0729750263  certif_acte_gel_loi_machine2/contre_epreuve_releve_acte_machine2_v2.log
    6047e0ccf5765454  certif_acte_gel_loi_machine2/contre_epreuve_releve_acte_machine2_v2.json
    (ce script)  fabrique_lot_contreseing_acte_gel_loi_v2_machine2_v1.py
