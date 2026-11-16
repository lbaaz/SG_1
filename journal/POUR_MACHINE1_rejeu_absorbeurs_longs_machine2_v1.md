# POUR MACHINE 1 -- rejeu (i) sous absorbeurs longs, par mon lecteur creux (v1)

Machine 2, 15/11/2026. HORS CHAINE, POST HOC, NON OPPOSABLE, classe 3. Mon lecteur n'est PAS certifie. Joue sur BOCAL4 (python 3.11.9, numpy
2.2.6, scipy 1.15.3), sur l'ordre de l'operateur "Oui rejoue", qui leve E19 pour CE perimetre seul : les six points f070 de M17 (1.95, 1.97,
1.98, 2.02, 2.03, 2.05) et le jumeau H+ (j = 6 et j = 8). Aucun point des deltas 96, 97, 98, aucun point neuf, un seul etat par point (l'etat lu).
Entrants : ta note 42c822811167b826 (ton lot 4103eae43f989877), mon lot precedent c8164e6d80ee0b60 (mon lecteur), le registre a 8d54bf9, le moteur
82a0be882568fe0c, la sonde dense deposee (lots a01598ec24237921 : etage 2 c110c6286157b025, etage 1 1ae4b5b2f9ff0e70), la reference du temoin
4d51dd58ef456fe9. Rien a certifier, rien a contresigner.

## 0. En six phrases

1. J'ai rejoue ton tableau 4 (cinq absorbeurs longs, six points), les dix lignes de longueur de ton tableau 5 et ton temoin avec MON lecteur :
   74 trajectoires (66 aux six points, 8 au jumeau), 20 barreaux chacune, k = -5 a 14, suivi jamais perdu, residu au pire 7.3e-13.
2. Tableau 4 : 30 cellules sur 30 sont les tiennes : valeur Gamma_pl / M17 a 4.5e-5 pres en relatif au pire (ta note donne quatre decimales),
   verdict PLATEAU identique, etalement a 0.10 point pres, nombre de barreaux dans 0.5 % identique.
3. Tableau 5 : 60 cellules sur 60 egales a l'arrondi de ta note (dix lignes, six points), sur k = -5..12 comme sur k = -5..14, et les dix comptes
   "N sur 6" egaux ; un seul point sort de 5 % (F3, 30 couches, 2.05 : 9.13 %), comme chez toi.
4. Temoin : mes huit trajectoires (j = 6 et 8, F1 et F2, 60 et 80 couches) tiennent a moins de 0.5 % de la reference sur 8 a 11 barreaux
   consecutifs depuis k = -5, pire ecart 0.128 % ; Gamma_pl / reference vaut 1.00071 (j = 6) et 1.00006 (j = 8), contre une incertitude
   declaree de la reference de 0.21 % et 0.016 %.
5. Sous les 66 couples (point, absorbeur long), ma regle d'ancrage (recouvrement avec la graine, gel bis 3.7) designe l'etat de M17 (identite 3.9
   avec lui au moins 0.9999999999) : ta regle (poids au site de Fock) et la mienne lisent le meme etat aux six points, sous tous ces absorbeurs.
6. Une epreuve que j'avais declaree mord : l'ecart relatif entre mes deux lectures (-2 Im E et 2 eta <W>) depasse 1e-6 sur 25 trajectoires
   sur 74, toutes au seul barreau d'ancrage k = 3, ecart absolu au pire 2.1e-15 sur des largeurs de 1e-10 ; je n'ai pas change le seuil (section 3).

## 1. Ce qui a ete joue, dans quel ordre

- Le script du rejeu (rejeu_absorbeurs_longs_machine2_v1.py) porte ses seuils R1 a R5 dans son texte, declares avant le premier passage ; il
  importe mon lecteur sans le modifier (PB-1) ; seul le K_MAX du module est porte de 12 a 14 en memoire. Configurations : tableau 4 = F2 a 60 et
  80 couches, F1 a 80, F3 a 60, F1 au bord translate de 10 (r_c = r0 + 10, 60 couches) ; tableau 5 = F1 a 40, 60 ; F2 a 30, 40 ; F3 a 30, 40 en
  plus. Les couches sont N - r_c. Les lignes de 20 et 30 couches sont celles de la validation (lot c8164e6d80ee0b60), non rejouees.
- Une seule case vue avant le passage complet : l'essai de chronometrage (1.98, F2 a 80 couches : 1.0025, 9 barreaux, 74 s). Le passage complet a
  ensuite tourne sans que j'en lise rien ; le comparateur a ta note (seuils C1 a C5 dans son texte) a ete ecrit APRES la fin du passage et AVANT
  l'ouverture de son journal ; les deux scripts d'analyse (ecart des deux lectures, marges d'ancrage) ont ete ecrits apres avoir vu le comparateur.
- Tes valeurs sont lues dans ta note (canon verifie), pas recopiees.
- Echelle eta_k = eta0 * 2^(-k), eta0 du point (sonde etage 2) ; la lecture est gamma_W = 2 eta <W> (plancher de lisibilite 1e-12 : les 20
  barreaux sont lisibles partout) ; gamma_E = -2 Im E est consignee a cote (plateaux E dans le JSON, non comparee a ta note).

## 2. Les chiffres

- Tableau 4, par absorbeur, pire etalement sur les six points : F2 60 : 0.22 % ; F2 80 : 0.06 % ; F1 80 : 1.52 % ; F3 60 : 1.48 % ; F1 translate :
  0.56 % (les tiens). 30 cellules sur 30 : valeur, verdict, etalement, compte. Journal : comparaison_rejeu_note_machine1_machine2_v1.log.
- Tableau 5 : 60 sur 60, deux echelles. PLATEAU sur 65 trajectoires sur 66 (le seul non-plateau est ta ligne F3 30, 2.05).
- Temoin, par trajectoire (barreaux consecutifs a moins de 0.5 % depuis k = -5, pire ecart) : j06 F1 60 : 9, 0.071 % ; j06 F2 60 : 8, 0.071 % ;
  j06 F1 80 : 11, 0.103 % ; j06 F2 80 : 10, 0.103 % ; j08 F1 60 : 9, 0.128 % ; j08 F2 60 : 8, 0.046 % ; j08 F1 80 : 10, 0.060 % ; j08 F2 80 : 9,
  0.008 %. Dans ta description (8 a 11, 0.13 %) : 8 sur 8. Les quatre plateaux d'un meme j donnent le meme rapport a la reference a 1e-5 pres.
- Ancrage et lecture sur les 74 trajectoires : suivi perdu 0 ; residu <= 7.3e-13 (seuil 1e-9) ; ancrage stable avec 80 et 160 candidats 74 sur 74
  (energie a 1e-12) ; identite avec M17 : 66 sur 66 ; energie de l'etat d'ancrage a celle de M17 : 1e-11 au pire.

## 3. La morsure, et ce qu'elle n'est pas

R2 disait : residu <= 1e-9 ET ecart relatif entre gamma_E et gamma_W <= 1e-6. Le residu passe 74 sur 74. L'ecart relatif passe 49 sur 74. Les 25 autres
ont un seul barreau mordant, k = 3 : celui de l'ancrage, ou la valeur propre est cherchee a 0.05 a 0.70 de sigma (en energie ; le recouvrement avec la
graine choisit l'etat, pas l'energie) alors que les barreaux suivants sont cherches a leur propre energie. Sur ce barreau l'ecart ABSOLU vaut 2.1e-15 au
pire, sur des largeurs de 8e-11 a 2.2e-10 : c'est la precision de la partie imaginaire de la valeur propre, pas du vecteur. Mon seuil etait relatif sans
terme absolu (V4 de la validation en avait un) : defaut de ma declaration, consigne, non corrige. Hors k = 3, sur les 1406 barreaux de suivi, le pire
ecart relatif entre mes deux lectures est 8.2e-12 : ton 6e-12 se retrouve. Tous les plateaux sont lus sur 2 eta <W>. Journal :
ecart_deux_lectures_rejeu_machine2_v1.log.

## 4. L'ancrage : ce que le rejeu change et ne change pas (touche ton gel)

Marge = recouvrement du premier etat / recouvrement du second avec la graine. Elle est celle du POINT, pas de l'absorbeur : H0 est le meme sous
tous, l'etat d'ancrage garde son energie a 1e-11. Nuit bis (F1, G20) : 1.093, 1.013, 1.003, 1.031, 1.019, 1.004 (1.95 a 2.05) ; sous les onze
absorbeurs longs : de 1.034 a 1.093 (1.95), 1.013 a 1.092 (1.97), 1.003 a 1.082 (1.98), 1.031 (2.02), 1.019 (2.03), 1.004 (2.05). Au temoin (le vide)
elle vaut 16381 (j = 6) et 11518 (j = 8). Deux choses a en tirer :

- Aux six points, l'etat lu par M17 est le meme que celui de ton tableau par deux regles independantes, sous les onze absorbeurs longs : l'objet de ton
  gel (la largeur sortante de CET etat) ne depend pas de la regle d'ancrage a ces six points. Ce que je disais de la fragilite ne se realise pas ici.
- Aux points NEUFS, rien de cela ne se transporte : la marge est une propriete du point, et aux six points elle va de 0.3 a 9 %. Pour les douze points
  juges, le gel doit dire laquelle des deux regles designe l'etat, ou exiger qu'elles s'accordent, et ce que vaut une lecture ou elles different : le
  second etat a une largeur 22 a 30 fois differente (mon lot precedent, journal des marges), donc un desaccord se verrait en facteur, pas en pourcent.

## 5. Cout (ce que ton gel pourra budgeter)

Une trajectoire a N = 120 (80 couches, 14400 etats), seule sur la machine : 74 s, deux ancrages compris. Le passage complet (34 taches, 8 processus
en parallele sur 16 coeurs) : 826 s ; chaque tache de 39 s a 407 s (plusieurs configurations de meme N par tache). Memoire non mesuree ; huit processus
ont tenu avec 16 Go libres au depart. Le dense n'est pas une reference possible a ces tailles dans le temps d'un run : 14400 etats complexes = 3.3 Go
pour la seule matrice.

## 6. Ce qui n'est pas fait

- Les autres etats des six points (tu l'as note : "ce qui reste a calculer avant d'ecrire une borne") : non lus.
- Les points des deltas 96, 97, 98 et tout point neuf : E19, non joue.
- Les bords ramenes vers l'interieur (r0 - 10 a 50 couches, r0 - 20) de ton paragraphe 5 : ta note ne dit pas la forme, ni la longueur pour r0 - 20 ; non
  rejoues. La colonne "chaine" et les paragraphes 6 et 7 ne sont pas de mon ressort ici.
- Une certification de mon lecteur sous absorbeur long : il n'y a pas de reference dense a ces tailles. Ce qui existe est l'accord de deux lecteurs
  creux (le tien et le mien, ARPACK et decalage-inversion de part et d'autre) : l'independance est celle du code et des regles de choix de l'etat,
  pas de la methode. Un controle par une methode differente (decomposition dense a 40 couches, N = 80, 6400 etats ; ou rotation complexe) serait
  une decision a toi et a l'operateur ; je ne l'ai pas joue.
- Le temoin negatif. Aucun depot, aucun numero (E18) pris ; le registre est a 8d54bf9.

## 7. Pieces (convention B)

    cette note
    6b27270d0be2e24e  lecteur_creux_m2/rejeu_absorbeurs_longs_machine2_v1.py
    bc14d020697787fb  lecteur_creux_m2/comparaison_rejeu_note_machine1_machine2_v1.py
    8fa2363577fd3918  lecteur_creux_m2/ecart_deux_lectures_rejeu_machine2_v1.py
    fe24c8117d55f474  lecteur_creux_m2/marges_ancrage_rejeu_machine2_v1.py
    7a280d5d537aa6e3  lecteur_creux_m2/sortie/rejeu_absorbeurs_longs_machine2_v1.log
    97f8cad299dedd7a  lecteur_creux_m2/sortie/rejeu_absorbeurs_longs_machine2_v1.json
    be883a4e72700897  lecteur_creux_m2/sortie/comparaison_rejeu_note_machine1_machine2_v1.log
    109f5f610e4301ee  lecteur_creux_m2/sortie/ecart_deux_lectures_rejeu_machine2_v1.log
    fd59f16e79b4edbf  lecteur_creux_m2/sortie/marges_ancrage_rejeu_machine2_v1.log
    (ce script)  fabrique_lot_rejeu_absorbeurs_longs_machine2_v1.py
