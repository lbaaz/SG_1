# Note hors chaîne : le vide — lecteur, absorbeur de chaîne, ce qu'un gel jugerait (étape sans run)

Plume : machine 1. Date : 16/11/2026. Statut : exploration hors chaîne, classe 3, non certifiée, non
rejouée par machine 2. Elle ne tranche rien, ne modifie aucune pièce citée et n'ouvre aucun gel.
Ouverture, selon machine 1 : à la fin de la note « loi d'échelle » (@@canon_note_v1@@), machine 1 a
proposé une étape sans run avant tout gel du vide ; l'opérateur a écrit « j'ouvre » (16/11/2026,
11 h 03).

AUCUNE LARGEUR 2D DU SYSTÈME À FANTÔME N'EST CALCULÉE ICI, ni pour le vide ni pour un autre état.
Ce qui est calculé : des chaînes à une dimension ; et, en 2D, le seul JUMEAU SANS FANTÔME (signe
+1), où aucune échelle résonante n'existe. Les largeurs 2D citées pour les états déjà joués sont
lues dans les pièces de la note « loi d'échelle ». Registre lu sur clone neuf (tête dee73bd), non
écrit. Tous les nombres sont écrits par un script qui les lit dans les sorties (section 9).

## 0. Verdict

1. Le lecteur déposé sait lire l'état porté par (0, 0) : sa routine le fait déjà, pas sa chaîne de
   pièces. Le mode « étage 1 » du dépôt lit le site (0, 0) depuis l'énergie 0. Mais le mode
   « point » ne lit que des états choisis par la sonde dense (les quatorze de plus grand
   recouvrement avec la graine à fraction 0,70, au-dessus de dix planchers) : il faut une sonde
   dérivée, sans étage dense, et sa feuille. Section 1.
2. Le plancher n'était pas celui du lecteur. Au jumeau sans fantôme, à la géométrie du vide, les
   @@tv_lectures@@ lectures sont suivies et rendent des largeurs de @@tv_min@@ à @@tv_max@@. Les
   « dix planchers » (1,33 × 10^-12) sont ceux de la décomposition dense, qui choisit les états ;
   la routine creuse, qui lit la largeur par le flux, n'a pas de plancher à ce niveau. Coût :
   @@tv_duree_min@@ à @@tv_duree_max@@ s par cellule sur machine 1. Section 2.
3. Le procédé du lecteur n'est pas limité par la double précision. Sur une chaîne dont la largeur
   est connue par ailleurs, la routine déposée rend le logarithme de la largeur à @@pp_pire@@
   près jusqu'à exp(−@@pp_profond@@), soit @@pp_decades@@ décades. Je retire la phrase de la note
   « loi d'échelle » selon laquelle aucun lecteur 2D en double précision ne lirait le régime
   profond : rien ne la soutient. Que le lecteur lise JUSTE à ces profondeurs en 2D n'est pas
   montré pour autant. Section 2.
4. L'instabilité de la chaîne d'ordre 3 a deux causes, et je n'en avais vu qu'une. (a) L'absorbeur
   déposé a une force qui suit le désaccord et non le saut : à barrière courte et petit désaccord
   il absorbe trop peu, et la chaîne du premier ordre en souffre autant que l'ordre 3. Un
   absorbeur adapté au saut la guérit : pour le vide, de 3 à 6 barreaux et |delta| ≤ 0,02, la
   largeur d'ordre 3 ne bouge plus que de @@vide_et_max@@ au plus sous @@n_var@@ variantes.
   (b) À désaccord plus grand, ce sont bien les termes d'ordre 3 après la barrière : @@ca_inst_ada@@
   des @@ca_n@@ points de la carte de 16 barreaux au plus restent instables, alors que les ordres 1
   et 2 y sont stables. Celle-là n'est pas guérie. Sections 3 et 4.
5. Le prédicteur du vide existe. Chaîne d'ordre 3 sous absorbeur adapté : de 3 à 6 barreaux et
   |delta| ≤ 0,02, elle s'écarte de la loi d'échelle de @@vide_r3_max@@ au plus (@@vide_r3_pc@@ pour
   cent), et l'ordre 2 de l'ordre 3 de @@vide_r32_max@@ au plus. La prédiction de la chaîne est donc
   arrêtée à @@vide_et_max@@ près, son étendue. Qu'elle soit juste est une autre question : c'est
   celle qu'un gel poserait. Section 3.
6. Aux états déjà joués, l'absorbeur adapté abaisse l'ordre 3 de @@cj_d_med_abs@@ en médiane,
   moins que l'étendue médiane de chacune des deux règles sur ces états (@@cj_stab3_med@@ pour la
   déposée, @@cj_et_med@@ pour l'adaptée). Il rapproche la chaîne de la 2D
   à delta > 0 (@@cj_mieux_pos@@) et l'en éloigne à delta < 0 (@@cj_pire_neg@@) ; aucun état ne
   sort des tolérances rappelées de E1. L'accord du delta 100 est donc au niveau de ce que
   l'absorbeur de la chaîne laisse indéterminé. Après coup ; ce n'est pas un rejeu du gel, et
   l'instrument déposé ne change pas. Section 5.
7. Une ligne profonde devient pensable. Si le lecteur lit en 2D ce qu'il lit sur une chaîne, le
   vide se prédit et se lirait bien au-delà de 6 barreaux : à 8, 12 et 16 barreaux la chaîne
   reste stable (étendue @@prof_et_max@@ au plus) pour des largeurs jusqu'à @@prof_G_min@@. C'est
   une possibilité, pas un fait. Section 6.
8. Suite, rien n'est décidé : le gel du vide est faisable. Ce qu'il demande est en section 7.

## 1. Le lecteur déposé et le vide (lecture du code)

Pièces lues : la sonde du lecteur du gel « ordre 3 » (d5cc48f48e37af99), sa sonde dense
(68baf04c73ed5d44), la routine de plateau de la feuille du gel ter.

- La routine. lire_etat lit UN état par itération inverse creuse à décalage fixe, depuis le site
  de Fock de l'étiquette, et rend la largeur par le flux, 2 eta <W>. Elle ne dépend d'aucune
  graine. Le mode « étage 1 » (témoin positif) l'appelle déjà au site (0, 0) avec l'énergie de
  départ 0.
- Ce qui manque. Le mode « point » prend ses états dans la sortie de la sonde dense : les
  quatorze états de plus grand recouvrement avec la graine cohérente à fraction 0,70, dont la
  largeur dense à k = 3 dépasse 1,33 × 10^-12 ; sa boîte (r_c) vient de la barrière de la
  graine ; ses refus contrôlent la table et la sortie dense. Le vide n'y entre pas.
- Ce qu'il faut. Une sonde dérivée par remplacements, comme les précédentes : un mode qui lit
  le site (0, 0) aux points d'une table, énergie de départ 0, r_c = 2 (m_bord + max(8, m_bord))
  + 2 (la règle du dépôt, sans graine), eta0 = |delta|, les quatre absorbeurs et les douze
  barreaux du dépôt ; pas d'étage dense. Et une feuille dérivée : la routine de plateau (cinq
  barreaux consécutifs à 5 pour cent) et les accords entre absorbeurs sont ceux du gel ter. Ce
  sont des pièces de classe 2, à certifier.
- Le décalage. Autour de l'énergie 0 les états de l'échelle sont espacés de |delta| ; le
  déplacement d'énergie du vide est très petit devant lui. Le décalage 0 désigne donc le vide.
  Non vérifié sur le système à fantôme, puisque rien n'y est lu ici.

## 2. Ce que le lecteur peut lire (sans lire le vide)

### 2.1 Le jumeau sans fantôme à la géométrie du vide

Routine déposée, lue telle quelle dans la sonde (canon contrôlé). Jumeau H+ : pas d'échelle
résonante, la largeur de l'état porté par (0, 0) n'y est fabriquée que par l'absorbeur. Quatre
absorbeurs, douze barreaux.

@@table_temoin@@

@@tv_suivies@@ lectures suivies sur @@tv_lectures@@. Boîtes de @@tv_N_min@@ à @@tv_N_max@@.
La plus grande largeur du jumeau, @@tv_max@@, est à plus de @@tv_decades@@ décades sous la plus petite
largeur que la chaîne prédit pour le vide de 3 à 6 barreaux (@@vide_G_min@@).

### 2.2 Le procédé sur une barrière profonde

La routine déposée, à qui l'on donne la chaîne de la limite de l'état (0, 0) rangée dans une
« boîte » (les sites en trop sont découplés), sous l'absorbeur de la chaîne déposée. Référence :
la fraction continue en logarithme, contrôlée contre le pôle exact en précision arbitraire dans
la note « loi d'échelle ».

@@table_procede@@

@@pp_suivis@@ lectures suivies. Plus grand écart : @@pp_pire@@. La double précision ne limite
donc pas ce procédé sur une chaîne. En 2D la factorisation n'a pas la même structure : ce
contrôle n'y vaut pas preuve.

### 2.3 L'absorbeur du lecteur convient-il au vide ? Un mandataire à une dimension

Aucune 2D. La chaîne du premier ordre du vide, à qui l'on donne l'absorbeur DU LECTEUR lu le long
de l'échelle (r = max(a, b) = 2 m), aux quatre absorbeurs et aux douze barreaux, puis la règle de
plateau de la feuille déposée. @@md_cas@@ cas (3, 4 et 5 barreaux, |delta| de 0,005 à 0,02).

- Avec la règle du dépôt, eta0 = |delta| : plateau à @@md_dep@@. Dans les fenêtres retenues, la
  largeur est à @@md_dep_r@@ au plus du plateau de l'absorbeur adapté. Les fenêtres retenues vont
  de @@md_k_F2@@ pour les absorbeurs F2 et de @@md_k_F1@@ pour F1. Au barreau le plus faible (k = 8),
  les absorbeurs F2 s'écartent de @@md_k8_min@@ à @@md_k8_max@@ : c'est la sous-absorption, hors
  des fenêtres.
- Avec une règle adaptée au saut (eta0 = saut au site r_c / 2) : plateau à @@md_sau@@, mais à
  @@md_sau_r@@ près seulement. Elle ne fait pas mieux ; je ne la propose pas.

Ce mandataire dit que la force de l'absorbeur du lecteur est du bon ordre pour le vide. Il ne dit
rien de la largeur 2D.

## 3. L'absorbeur de la chaîne

### 3.1 Le diagnostic

Règle déposée : W_m = ef |delta| (m − début)^2, ef = 0,0625. Largeur du vide, en logarithme,
rapportée à la loi d'échelle, quand ef varie seul :

@@table_diag@@

À ef = @@diag_ef_faible@@ la largeur du premier ordre est à @@diag_faible@@ ou moins ; à
ef = @@diag_ef_fort@@ elle descend jusqu'à @@diag_fort@@. Il n'y a pas de plateau large, et le
réglage déposé est au bord du côté faible : sa variante « ef divisé par deux » tombe dans la
pente. L'ordre 1 se comporte comme l'ordre 3 : ce n'est pas un défaut de l'ordre 3. La force de
l'absorbeur suit |delta|, les sauts suivent g m^(5/2) ; aux états joués les deux se trouvaient
du même ordre.

### 3.2 L'absorbeur adapté au saut

W_m = a |t_m| ((m − début) / L)^2 de début à début + L, début = m_bord + c, chaîne coupée à
début + L : l'absorption cumulée vaut a L / 6 quel que soit l'état. @@n_var@@ variantes
(a = 1, 2, 4 ; c = 6, 8, 10 ; L = 16, 24) ; « plateau » : leur médiane ; « étendue » : max − min.
Les tables et les matrices d'ordre 2 et 3 sont celles des blocs déposés ; seuls l'absorbeur et la
longueur changent.

Le vide, |delta| = 0,005, 0,01 et 0,02, les deux signes. Phi* : la limite delta → 0 sous
l'absorbeur adapté. r3* = ln(Gamma_3* / |delta|) − ln Phi*.

@@table_vide@@

- De 3 à 6 barreaux, l'étendue d'ordre 3 vaut @@vide_et_max@@ au plus. À 2 barreaux et
  |delta| = 0,02 elle monte à @@vide_et_max_2@@ : c'est le plus fort couplage de la table, et
  le début de la cause (b).
- Phi* s'écarte de la Phi de la note « loi d'échelle » (règle déposée) de @@vide_dphi_min@@ à
  @@vide_dphi_max@@ ; l'étendue de Phi* vaut @@vide_et_phi@@ au plus. La forme fermée à trois
  termes est à @@vide_ff_min@@ à @@vide_ff_max@@ de Phi*.
- La règle déposée s'écartait du plateau jusqu'à @@vide_dep_pire@@ : c'est l'instabilité que la
  note « loi d'échelle » voyait.
- Pour @@exc_n@@ cas d'états excités, Phi* − Phi va de @@exc_dphi_min@@ à @@exc_dphi_max@@,
  étendue @@exc_et_max@@ au plus.

## 4. Ce qui reste instable : les termes d'ordre 3 après la barrière

La carte de la note « loi d'échelle », rejouée sous l'absorbeur adapté pour ses points de 16
barreaux au plus : @@ca_n@@ points, @@ca_inst_dep@@ instables sous la règle déposée,
@@ca_inst_ada@@ sous l'absorbeur adapté (dont @@ca_deja@@ l'étaient déjà ; @@ca_gueris@@ sont
guéris, @@ca_nouveaux@@ le deviennent). Pour le vide, les @@ca_n_inst_00@@ instables ont tous
|delta| ≥ @@ca_dmin_00@@ ; pour (6, 2), les @@ca_n_inst_62@@ ont |delta| ≥ @@ca_dmin_62@@.

À @@ab_n@@ de ces points, par ordre :

@@table_apres@@

Les ordres 1 et 2 y sont stables (étendue @@ab_et12_max@@ au plus) ; l'ordre 3 bouge de
@@ab_et3_min@@ à @@ab_et3_max@@. À @@ab_signe@@ de ces points le saut corrigé t + T3 change de
signe à l'intérieur de la chaîne : le terme d'ordre 3, en t^3, y dépasse le saut. Là, la lecture
de la note « loi d'échelle » tenait.

Essai, NÉGATIF : couper net les termes d'ordre 3 au-delà du premier site où le saut dépasse un
seuil t_s, ordre 2 au-delà.

@@table_coupure@@

Chaque coupure donne une largeur stable sous l'absorbeur (étendue @@cp_et_max@@ au plus), mais
la largeur dépend du site de coupure : de @@cp_N1@@ à l'état joué N1 rang 0, contre @@cp_autres@@
au plus aux trois autres états joués. Les termes d'ordre 3 juste après la barrière font donc
partie du calcul, au moins à delta < 0 ; une coupure nette n'est pas une règle. Je ne propose
rien pour la cause (b). Elle ne touche pas le vide à |delta| ≤ 0,02.

## 5. Les états déjà joués sous l'absorbeur adapté (après coup)

Les @@cj_n@@ états du domaine des deltas 98 et 100. Même chaîne d'ordre 3, absorbeur adapté.

- Étendue sous les variantes : médiane @@cj_et_med@@, neuvième décile @@cj_et_d9@@, plus grande
  @@cj_et_max@@. Pour ces états l'absorbeur adapté n'a pas le plateau net qu'il a pour le vide.
- ln(G3 adapté / G3 déposé) : médiane @@cj_d_med@@, de @@cj_d_min@@ à @@cj_d_max@@ ; négatif à
  @@cj_d_neg@@.
- |ln q3| : médiane @@cj_q_dep_med@@ (déposé) et @@cj_q_ada_med@@ (adapté) ; pire @@cj_q_dep_max@@
  et @@cj_q_ada_max@@. Hors des tolérances rappelées de E1 : @@cj_hors_dep@@ et @@cj_hors_ada@@.
- L'adapté est plus près de la 2D à @@cj_mieux@@ : @@cj_mieux_pos@@ à delta > 0, @@cj_mieux_neg@@
  à delta < 0. Ce n'est pas un gain : il abaisse l'ordre 3 d'un pour cent presque partout, ce qui
  rapproche là où la chaîne était trop haute et éloigne là où elle était trop basse (à la cellule
  P1 le pire |ln q3| passe de @@cj_P1_dep@@ à @@cj_P1_ada@@, à N2 de @@cj_N2_dep@@ à @@cj_N2_ada@@).
  Les deux règles diffèrent de moins que l'étendue de chacune à @@cj_d_sous_deux@@ (étendue
  médiane de la règle déposée sur ces états : @@cj_stab3_med@@), et l'écart médian de la chaîne à
  la 2D, @@cj_q_dep_med@@, est du même ordre.

@@table_joues@@

Ce n'est pas un rejeu du gel du delta 100 et cela ne change aucun de ses verdicts.

## 6. Une ligne profonde

Le vide à 8, 12 et 16 barreaux, |delta| ≤ 0,02, sous l'absorbeur adapté (six variantes) :

@@table_profond@@

@@prof_n@@ points, étendue @@prof_et_max@@ au plus, |r3*| @@prof_r3_max@@ au plus. Le jumeau
sans fantôme lit bien plus bas que ces largeurs (section 2.1), et la routine lit juste sur une
chaîne à ces profondeurs (section 2.2). Ce qui manque : savoir si elle lit juste en 2D. Un gel
peut le laisser décider par la qualification en cours de run (plateau, accords entre
absorbeurs), en branche non létale.

## 7. Ce qu'un gel du vide jugerait (proposition ; rien n'est décidé)

- Objet. La largeur de plateau de l'état porté par (0, 0), lue par le lecteur creux, qualifiée
  dans le run.
- Énoncé V1, ligne lisible. À des cellules tirées (barrière de 3 à 6 barreaux, |delta| ≤ 0,02,
  les deux signes), la chaîne d'ordre 3 sous absorbeur adapté rend cette largeur dans une
  tolérance gelée. Les largeurs prédites vont de @@vide_G_max@@ à @@vide_G_min@@, pour des
  couplages de @@vide_g_min@@ à @@vide_g_max@@.
- Énoncé V2. La forme fermée à trois termes la rend aussi, dans une tolérance plus large (elle
  est à @@vide_ff_min@@ à @@vide_ff_max@@ de Phi*).
- Énoncé V3, ligne profonde, non létal. À 8 barreaux et plus, là où le lecteur qualifie.
- Instrument. La sonde dérivée et sa feuille (section 1) ; le bloc d'absorbeur adapté pour la
  chaîne ; les témoins : le jumeau sans fantôme à la géométrie de chaque cellule, les ancres du
  dépôt, le témoin positif.
- À décider au gel, pas ici : la règle de tirage et la graine ; les tolérances (la règle de
  plateau du lecteur est à 5 pour cent ; E1 prenait 0,05 pour e_bord < 0,3) ; le nombre de
  cellules ; ce qu'on fait d'un état non qualifié ; les annonces de la plume.

Mon avis : le faire, avec la ligne profonde. C'est le premier énoncé de la campagne sur l'objet
qu'un lecteur extérieur nomme, et il est peu coûteux à jouer.

## 8. Limites, et défauts de ma plume

- L-1. Aucune largeur 2D du vide n'existe. Que le lecteur la lise, et la lise juste, est appuyé
  par trois faits indirects (jumeau, procédé sur une chaîne, mandataire) ; aucun n'est une lecture.
- L-2. L'absorbeur adapté est une règle d'aujourd'hui, d'une plume, non certifiée. Son étendue
  mesure sa stabilité, pas l'erreur de la chaîne.
- L-3. Le mandataire est une chaîne du premier ordre : rien de ce qui est propre à la 2D n'y est.
- L-4. La cause (b) reste ouverte. Le prédicteur du vide n'est établi qu'à |delta| ≤ 0,02.
- L-5. La comparaison aux états joués est après coup.
- L-6. Une seule forme de hamiltonien effectif ; un seul état, (0, 0).

Défauts, tous dans la note « loi d'échelle » (@@canon_note_v1@@), qui n'est pas modifiée :

- D-VIDE-1. Sa section 6 lisait l'instabilité comme celle des termes d'ordre 3 après la
  barrière, et y voyait une raison de regarder la forme à énergie fixée. Pour le vide à petit
  désaccord c'est faux : c'est l'absorbeur, et l'ordre 1 le montre. La lecture ne tient qu'à
  désaccord plus grand (section 4).
- D-VIDE-2. Son verdict 4 disait qu'aucun lecteur 2D en double précision ne lirait le régime
  profond. Retiré (section 2.2).
- D-VIDE-3. Sa section 7 comparait le vide à « la plus petite largeur de plateau de ces deux
  runs » comme à une limite du lecteur. Cette limite est le seuil de la sonde dense.
- D-VIDE-4. Sa section 7 concluait que le meilleur prédicteur du vide était la loi d'échelle,
  avec une tolérance portant l'instabilité. C'est la chaîne d'ordre 3 sous absorbeur adapté.
- D-VIDE-5. Ses valeurs de Phi pour le vide à barrière courte portent l'absorbeur déposé :
  elles sont à @@vide_dphi_min@@ à @@vide_dphi_max@@ du plateau (section 3.2).

## 9. Pièces (convention B)

Au registre (dee73bd), lues :

@@pieces_registre@@

Du lot de la note « loi d'échelle » (408b8a595cad0040), reprises telles quelles :

@@pieces_reprises@@

De ce lot :

@@pieces_lot@@
    (ce script)       construction_note_vide_machine1_v1.py, gabarit_note_vide_machine1_v1.md
