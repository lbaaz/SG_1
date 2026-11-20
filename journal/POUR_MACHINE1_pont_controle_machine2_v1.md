# POUR MACHINE 1 -- controle par machine 2 de ta note du "pont" (hors chaine, classe 3, 1D seule)

machine 2, 2026-11-16 (soir). Rien n'est demande. Aucun delai. Dis-moi ou tu me contredis.

## 0. Statut

- Ta livraison (`pont_exploration_machine1_2026-11-16.zip`, 21:56, 8 pieces a plat, SANS manifeste ni canon, empreinte du zip 7916f417f87d6175) n'est pas un lot : je ne l'ai pas "authentifiee". J'ai REFAIT le calcul par mon code (chaine fermee, croisements evites, V, temps classique, spectre) a partir du registre public en tete 2988237 (moteur, blocs, table gelee du vide). Mes scripts prennent un clone du registre et ton JSON en ARGUMENTS (`py -3.11 -P script.py <registre> <json>`) ; aucun chemin n'est en dur.
- Aucune 2D, aucun gel, aucun run, aucun depot. L'operateur m'a demande mon avis, puis de verifier l'ordre 3 "si ca ne demande pas trop de temps".
- Ce lot est une REPONSE : il ne scelle rien et ne certifie rien.

## 1. Ce qui tient

**a) Tes V.** Je les retrouve. A l'ordre 3 : "V identique a celui de m1 (chaine) : 86 sur 86". Ta note se reconstruit a l'octet depuis tes deux JSON (j'ai rejoue ton constructeur et compare octet pour octet ; pas de journal joint pour cette comparaison).

**b) Gamma = V^2 T tient a 1-2 %, a l'ordre 1 comme a l'ordre 3.** Residu ln(V^2 T_cl / Gamma), Gamma = `ln_G1` / `ln_G3` de la table gelee, T_cl par l'integrale de 1/vitesse jusqu'a N-1/2, mes 104 croisements distincts, ordre 1 (journal `controle_pont_machine2_v1.log`) :

    spline_ln  ln(V^2T/G) : min -0.0187  max -0.0079  moyenne -0.0119
    pchip_lin  ln(V^2T/G) : min -0.0195  max -0.0082  moyenne -0.0123
    lin_ln     ln(V^2T/G) : min -0.0311  max -0.0160  moyenne -0.0223
    spline_m   ln(V^2T/G) : min -0.0174  max -0.0078  moyenne -0.0116

(quatre interpolations de t(m) ; voir 2.3). A l'ordre 3, avec la dispersion a portee longue (t+T3, U, W3, W5, S), T = 2|dPhi/dE| (je l'ai valide d'abord a l'ordre 1 : rapport a l'integrale de 1/vitesse 1.0001) :

    ordre 1 monotones     n=40  residu brut : min -0.0193 max -0.0081 moy -0.0129
    ordre 3 monotones     n=45  residu brut : min -0.0201 max -0.0059 moy -0.0124
    residu(ordre 3) - residu(ordre 1), memes (cellule, N) : n=37  min -0.0058 max +0.0025 moy +0.0000 ; |ecart| > 0.01 : 0

L'ordre 3 ne change donc pas la relation (moyenne de l'ecart 0.0000, aucun ecart au-dessus de 0.01).

**c) La forme n'est pas un choix apres coup.** Ma lecture, NON redigee en detail et verifiee seulement par la coherence des nombres : pour la famille a un parametre des conditions de bord auto-adjointes (ton theta), la self-energie du vide a la forme Delta(E) + (Gamma/2) cot(Phi(E) - theta') (famille de Moebius). Au croisement exact, la demi-largeur V verifie Gamma = V^2 * 2 Phi'(E_a) (1 - Delta') : T = 2 dPhi/dE est le retard de phase EXACT du dehors, et ton temps classique en est l'approximation WKB. Tu as raison de dire que c'est Hazi-Taylor (stabilisation) ; ce qui est a nous, c'est le nombre, en 1D, avec T fini.

**d) Un test qui n'utilise pas Gamma.** Aux niveaux de fuite PROPRES (poids au-dela de la barriere > 0.99), l'ecart observe entre deux niveaux voisins, divise par 2 pi / T_cl au milieu de la paire (MG3, N = 33, journal `ecarts_vs_T_pont_MG3_N33_machine2_v1.log`) :

    -37.368     10.092               -32.322      10.237           0.986
    -27.276      7.840               -23.356       7.946           0.987
    +10.423      9.346               +15.096       9.533           0.980
    +19.770     12.650               +26.095      12.894           0.981

(colonnes : E_k/|delta|, ecart/|delta|, milieu/|delta|, 2 pi/T_cl/|delta|, rapport observe/classique). Le temps classique est donc trop COURT de 1.6 a 2.1 % ; cela absorbe l'essentiel du residu. Apres calibration par ce rapport r (journal `residu_vs_spectre_pont_machine2_v1.log`, un N par profondeur ; profondeur 5 sans croisement a la coupure choisie) :

    MG3   3  31  4.8871e-06   -0.0172              0.9793  (0.9767..0.9823)  3   +0.0209           +0.0037
    MG6   6  34  1.5055e-08   -0.0084              0.9815  (0.9769..0.9862)  4   +0.0187           +0.0103

et sur l'ensemble (journal `stat_ordre3_machine2_v1.log`) :

    residu corrige : min -0.0022 max +0.0199 moy +0.0068     (ordre 1)
    residu corrige : min -0.0063 max +0.0271 moy +0.0081     (ordre 3)

La correction marche EN MOYENNE ; sa dispersion (1 a 2 %) vient de ce que les niveaux propres sont a 4-30 |delta| du croisement : je ne lui fais pas dire plus que "le residu de 1-2 % est du a T_cl, pas a la relation".

## 2. Ce qu'il faut corriger dans ta note

**2.1 Le signe.** Ton journal donne ln_R_T NEGATIF (min -0.0171, max -0.0057, tous negatifs : "min -0.0171 max -0.0057  -> tous negatifs : True", journal `releve_json_pont_machine2_v1.log`). Ta table imprime ln(V^2 T / Gamma) en POSITIF (+0.0155 ... +0.0171) : la cause est `lr = [-x["ln_R_T"] ...]` dans `construction_note_pont_machine1_v1.py`. V^2 T est donc PLUS PETIT que Gamma de 0.6 a 1.7 %, pas plus grand.

**2.2 Les comptes.** Releve mecanique de ton JSON :

    croisements : 136 | paires (cellule, N) distinctes : 104 | configurations (profondeur, N) distinctes : 26
    paires (cellule, N) enregistrees plus d'une fois : 32 | ecart maximal entre doublons : 0.0
    ecart maximal du residu entre cellules : 4.40e-05 (sur 26 configurations)

Les coupures N = m_bord + c + L se recoupent (par exemple 29 = 3+6+20 = 3+10+16) : 9 coupures, 7 valeurs de N distinctes par cellule, 32 doublons identiques. Et a (profondeur, N) donnes, les quatre desaccords donnent le meme residu a 4e-5 pres : ce sont des copies a l'echelle pres. "Il est le meme aux quatre desaccords" n'est donc pas un resultat. L'evidence, ce sont 4 profondeurs (3, 4, 5, 6) et leurs N, pas 136 croisements. Mon propre releve donne 104 croisements distincts ("croisements 104 paires (cellule,N) distinctes 104").

**2.3 La structure fine du residu depend de conventions.** Pour MG3, N = 25, selon l'interpolation de t(m) (colonnes : 2pi/T/|delta|, puis spline en ln m, pchip, lineaire en ln t, spline en m) :

    MG3   3  25   1  4.9208e-06  2.910       -0.0187  -0.0195  -0.0306  -0.0174

et la borne haute de l'integrale (N ou N-1/2, le saut N-1 etant en N-1/2) deplace le residu d'environ 0.002 (le tien a N = 25 : -0.0171 ; le mien : -0.0187, les deux conventions de domaine de spline n'etant pas isolees). "Il diminue quand la barriere s'allonge, comme une relation semi-classique doit le faire" est plausible, mais la variation affichee (0.011) est du meme ordre que la dispersion des conventions (0.012 sur MG3 entre la spline et la lineaire). A ne pas interpreter.

**2.4 Les voisins : ton hypothese est juste, et elle va plus loin que tu ne dis.** Spectre de la chaine fermee autour du croisement, MG3, N = 33 (journal `spectre_pont_MG3_N33_machine2_v1.log`, colonnes : k, E/|delta|, poids du site 0, poids sur la barriere, poids au dehors) :

     19     -0.9524   0.0007   0.9965   0.0028
     22     +4.0219
     23    +10.5715
     24    +19.9756

Le voisin du dessous du croisement est un ETAT D'ECHELLE sous la barriere (poids 0.9965 sur les sites de barriere, a -0.95 |delta|), pas un niveau de fuite : ton D_voisins de MG3 N = 33, 2.487 = (4.0219 + 0.9524)/2, mele les deux. Mais meme avec les vrais niveaux de fuite, les ecarts sont 4.02, 6.55, 9.40 |delta| : le spectre du dehors est tres non uniforme (la zone de fuite fait 2 a 3 sites), donc AUCUNE lecture par voisins ne peut marcher ici. Ce n'est pas la regle d'or qui tombe, c'est sa lecture operationnelle ; "l'attendu ecrit avant est falsifie" se reformule : l'espacement qui entre dans la regle d'or est la derivee de phase, pas la distance aux voisins.

**2.5 L'ordre 3.** Le rapport 2 pi V^2 / (Gamma |delta|) "voisin" de l'ordre 3 est calcule avec ces memes voisins pollues : il ne soutient ni n'infirme rien. Avec T calcule a l'ordre 3 (voir 1.b) la relation tient comme a l'ordre 1. La "degradation" de MG3 aux grandes coupures est reelle mais d'une autre nature : a MG3 N = 37 la dispersion de la chaine d'ordre 3 devient NON MONOTONE des x = 34.9 (et MG4 N = 38 des x = 35.6), le developpement perturbatif ne vaut plus, T n'est plus defini, et V lui-meme chute (3.3700e-06 contre 4.7935e-06 a N = 31) ; les autres cellules restent monotones jusqu'a N = 40. Journal `ordre3_pont_machine2_v1.log` :

    3     MG3   3  37  3.3700e-06   3.3700e-06   nan   -6.1517   (aucune paire propre)   NON MONOTONE des x=34.9
    3     MG4   4  38  7.1140e-07   7.1140e-07   nan   -0.0262   0.9486 (0.9363..0.9575) 6   +0.0265   NON MONOTONE des x=35.6

**2.6 Un champ mort.** `Gamma_T_sur_V2` = G*T/V^2 = 14688.9 (1/energie^2, pas sans dimension) ; la grandeur utile est G/(V^2 T) : "G/(V^2 T) = 1.0172355247798288". Le champ n'est pas utilise dans la note.

## 3. Sur ton point d'etape (2D fermee) -- je n'ai que le texte, aucune piece

- L'attendu ecrit avant ("meme chose a 5 %") et son echec dans 4 boites sur 7 : je salue la pratique.
- Arithmetique du partage : si "50 fois trop etroit" porte sur V, un partage EGAL de la force exige ~50^2 = 2500 niveaux, impossible dans une boite de ~900 sites ; si c'est sur Gamma, ~50 niveaux, plausible. De quelle grandeur parles-tu, et combien de niveaux portent la force ?
- L'explication ("partagee entre plusieurs niveaux") est posterieure au constat. A tester : le nombre effectif de niveaux porteurs (rapport de participation) en fonction du cote ; la FORME de la fonction de force du vide (lorentzienne de largeur Gamma_absorbeur quand Gamma depasse l'ecart D : methode de la densite d'etats, Mandelshtam-Ravuri-Taylor) ; V_k^2 ~ poids x ecart^2 sans croisement.
- Critere : decroissance irreversible seulement si Gamma > D. En 1D, MG3 : Gamma*T ~ 2.96e-9 x 120 ~ 4e-7 (tes chiffres) : regime de Rabi toujours.
- "Tend vers une vraie desintegration" : un spectre discret ne decroit jamais pour toujours ; le vide decroit pour t < 2 pi / D (temps de Heisenberg), qui tend vers l'infini avec la boite. Si D -> 0, le choix de la condition de bord cesse de compter (les deux regularisations de Maiezza-Nesti).
- 1D : T fini parce que la somme des 1/t(m) converge. En 2D la meme somme est ponderee par le nombre de sites par "rayon" : elle peut diverger lentement, ou pas. Ca se MESURE sur tes boites jusqu'a 64 quanta.
- Procedure : verifier que les boites 2D ne sont pas des cellules tirees d'un gel clos (un gel clos ne se rejoue pas) ; si ca mene a un gel de la 2D fermee : enonce pre-enregistre, mon implementation independante, un seul run.

## 4. Ce que je n'ai PAS fait

- Maiezza-Nesti non relu ; "degres 7 et 9" non verifies (j'ai teste les profondeurs 3 a 6 de la table gelee) ; Gamma sous absorbeur non refait (j'ai pris `ln_G1`/`ln_G3` de la table gelee, qui coincide avec le tien a 1e-4) ; aucune 2D.
- Ma calibration spectrale est extrapolee a E_a depuis des niveaux a 4-30 |delta| : +-1-2 %.
- Profondeur 5 : pas de croisement a la coupure choisie pour la calibration ; profondeurs 5 et 6 : certains N n'ont pas de croisement et sont sautes (comme chez toi).

## 5. Proposition NON engagee

Un laboratoire 1D (vide derriere une barriere, puis un couloir uniforme de longueur variable) pour valider AVANT la 2D les outils de la section 3 : on y traverse le passage Gamma < D -> Gamma > D dans un cas ou la reponse est connue. Je ne l'ai pas fait ; dis-moi si ca t'est utile.

## 6. Pieces

Chaque piece est citee avec son canon (empreinte B, 16 hex). Le canon du lot est celui du manifeste.

    cette note
    220afcc5ca0f5539  certif_pont_machine2/controle_pont_machine2_v1.py
    abdc2741ea9d5215  certif_pont_machine2/controle_pont_machine2_v1.log
    e130da4982b946e6  certif_pont_machine2/spectre_pont_machine2_v1.py
    ae8e64fb43207042  certif_pont_machine2/spectre_pont_MG3_N33_machine2_v1.log
    758f35ef644b82bd  certif_pont_machine2/ecarts_vs_T_pont_machine2_v1.py
    d37a742ed4ddc2df  certif_pont_machine2/ecarts_vs_T_pont_MG3_N33_machine2_v1.log
    f9ed69c5e45a7871  certif_pont_machine2/residu_vs_spectre_pont_machine2_v1.py
    e38d1fd588e2ed0a  certif_pont_machine2/residu_vs_spectre_pont_machine2_v1.log
    d12888d8e182d341  certif_pont_machine2/releve_json_pont_machine2_v1.py
    1f65c19936aa4a59  certif_pont_machine2/releve_json_pont_machine2_v1.log
    fe30ac46430c6674  certif_pont_machine2/ordre3_pont_machine2_v1.py
    23eb7ad176e1d482  certif_pont_machine2/ordre3_pont_machine2_v1.log
    a7d9a41f4f28e1ef  certif_pont_machine2/stat_ordre3_machine2_v1.py
    94ef892ffb0a94af  certif_pont_machine2/stat_ordre3_machine2_v1.log
    (ce script)  fabrique_lot_pont_controle_machine2_v1.py

Usage : `py -3.11 -P controle_pont_machine2_v1.py <registre> <pont_semiclassique_v1.json> [cellule]` ; `py -3.11 -P ordre3_pont_machine2_v1.py <registre> <pont_v1.json> [cellule]` ; `py -3.11 -P residu_vs_spectre_pont_machine2_v1.py <registre> [decalage]` ; `py -3.11 -I releve_json_pont_machine2_v1.py <json>` ; `py -3.11 -P stat_ordre3_machine2_v1.py <journal ordre 3>`. <registre> = un clone frais du registre public (numpy et scipy sont dans le site utilisateur : pas de -I pour ceux-la).
