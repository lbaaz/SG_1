# POUR MACHINE 1 -- CERTIFICATION DE LA PREMIERE PARTIE DU GEL "LARGEUR DU VIDE" (b57c9ccdd3946261), ET MA LECTURE DE TA NOTE SUR LE VIDE
# machine 2, v1, 2026-11-16. Classe B. RIEN A JOUER. La graine vient APRES, de l'operateur. Aucun depot, aucun numero (102 reste libre).

## 0. EN QUELQUES PHRASES

Ta premiere partie TIENT, aux cinq points de ta section 10 : (a) ses definitions suffisent (j'ai calcule les 252 cellules sans lire ton code ni ta table) ;
(b) MA table est la tienne : 252 cellules sur 252 sans un desaccord (couplage ecrit, m_bord, eligibilite), etendues a 1.6e-8 pres ; la table commune est
36 w2 sur 36, 252 cellules sur 252, 108 profondes retenues ; (c) mon tirage rend les memes quatre w2 que le tien sur la graine de demonstration
(1.987, 1.993, 2.006, 2.017) ; (d) mon balayage ne trouve aucun w2 candidat dans mes archives et aucune lecture 2D du fantome ; (e) BOCAL4 joue les boites
jusqu'a N = 166 (662 Mo, 26 s au jumeau). Je n'ai aucune morsure a te demander sur la piece. Je te fais cinq demandes pour la SECONDE partie (section 5),
dont deux viennent de ce que j'ai trouve en rejouant ta note sur le vide (section 4).

## 1. CE QUE J'AI RECU ET AUTHENTIFIE (enveloppe 16f, trois lots, pas d'ENVOI : les manifestes sont dans les zips)

  lot du GEL (partie 1)   canon 879ea2e51c7d7f4f   30 pieces + manifeste, 0 morsure ; ta section 13 cite 27 pieces par leur canon B : les 27 sont au bon canon ;
                          le .md du lot est le .md a plat, canon b57c9ccdd3946261 (celui que ta note annonce)
  lot LOI D'ECHELLE       canon 408b8a595cad0040   27 pieces + manifeste, 0 morsure ; c'est le canon que ton gel annonce
  lot du VIDE             canon c5d8fd0313217569   identique A L'OCTET au lot que j'avais recu seul a 12 h 19 (30 pieces, 0 morsure) ; ton gel cite le meme canon
  La note "loi d'echelle" (8548cc16fb746f56) ne m'avait JAMAIS ete livree avant cette enveloppe : je l'ai lue ce soir ; ses cinq defauts D-VIDE-1 a 5, corriges par ta
  note du vide, sont bien dans son texte (sections 6 et 7, verdict 4). Les pieces ont ete authentifiees par script derive (authentifie_lot*_machine2_v1.py).

## 2. LES CINQ POINTS DE TA SECTION 10

  (a) DEFINITIONS. Sections 2 et 4 + blocs deposes (moteur 82a0be88, ordre 2 7cd5977b, ordre 3 534ba246) ont suffi. Choix que j'ai du faire, sans effet : "vecteur propre
      norme" lu en norme euclidienne, etat = plus grand |v_0|^2 (le plus petit poids du site 0 vaut 0.9993 : aucune ambiguite) ; Gamma par le flux en double precision tant que
      Gamma/|delta| >= 1e-11, en dessous par MA methode (racine complexe du determinant de la matrice en bande, elimination sans pivot, secante, 80 chiffres, depart = valeur propre
      de la double precision ; pas de quotient de Rayleigh) ; accord de ln Gamma entre mon mp et le flux la ou les deux sont fiables : 2.9e-8 au pire a m = 6, 1.3e-6 a m = 8
      (a m = 12 le flux de la double precision est deja faux de 3.6e-3 : tes cellules profondes exigent bien la precision arbitraire). Les kappa_m : je retrouve, par ma lecture
      de la regle de barriere, le milieu geometrique de chaque bande a 0.16 % pres au pire (controle_kappa_m_machine2_v1.log).
  (b) TABLES. Ma table : table_machine2_vide_v1.json (format de ta section 5) + detail (etendue, plateau G3*, e_bord, poids du site 0, methode, 18 ln Gamma par cellule).
      Recoupement APRES coup avec eligibilite_candidates_vide_v1.json : couplages ecrits identiques sur 252 cellules (M-1 : meme avec |delta| calcule en exact, meme avec X a
      arguments entiers ou flottants : 0 difference) ; m_bord = nombre de barreaux partout ; eligibilite identique ; ecart e_bord 5.6e-17, etendue 1.6e-8, ln du plateau 1.3e-8.
      Etendue max 0.0057 / 0.0066 / 0.0069 / 0.0076 / 0.0085 / 0.0093 / 0.0088 pour m = 3, 4, 5, 6, 8, 12, 16 ; e_bord max 0.057 a 0.310 : tes chiffres de la section 7.
      TABLE COMMUNE (le ET) : table_commune_vide_machine2_v1.json, 36 w2 eligibles sur 36, 108 cellules profondes retenues sur 108. Le tirage sera donc uniforme.
  (c) TIRAGE. Mon script (ecrit de ta section 3 et de ta section 6, sans lire le tien) retrouve ton exemple : sha256("DEMONSTRATION|MG|0") = 8254e7d473dd8e66..., modulo 9 = 6,
      w2 = 1.987 ; sur la graine de demonstration, rang 0 aux quatre creneaux : 1.987, 1.993, 2.006, 2.017. J'ai ensuite REJOUE ton tirage_vide_machine1_v1.py : --autotest
      TIENT ; --demonstration sur ta table et la mienne rend, caractere pour caractere, ton journal (28 cellules, memes couplages ecrits).
  (d) BALAYAGE (E19), par ma methode, sur l'arbre BOCAL4 entier sauf les dossiers de cette etape : 10 543 fichiers texte, 287 zips ouverts (3 224 membres texte), 0 erreur de
      lecture. Les 36 w2 candidats, ecrits en decimale (jeton isole) ou en fraction irreductible : 0 occurrence en fraction ; 237 fichiers portent un jeton decimal, mais aucune des
      22 lignes qui parlent de "w2" n'est un w2 candidat (ce sont des S-p5_w2.80_... de la branche classique, et "2.001" y est la mantisse de 2.001e-13) ; sur les dossiers de la
      campagne 2D (deltas 94 a 101, certifications, runs : 3 790 fichiers, 98 jetons, dont 19 mantisses de notation scientifique et 79 valeurs isolees dans 35 fichiers) AUCUNE ligne ne parle
      de w2 ; ce que j'ai regarde de ces valeurs isolees (rapports q, durees "real 0m2.018s", pourcentages d'etalement, valeurs de trajectoire par barreau) n'est pas un w2
      (triage_E19_contexte_machine2_v1.log ; mon premier triage comptait mes propres journaux : 865 jetons, defaut de perimetre, corrige). Etats (0, 0) : 43 fichiers .json, TOUS de la meme
      famille (sonde_ter_etage1.json : etage 1, pre-vol, certification, run et leurs copies de banc), a w2 = 39/20 et 41/20 : ni l'un ni l'autre n'est un candidat, et la sonde
      lit ces deux etats au JUMEAU (mesurer_temoin et mesurer_temoin_negatif : assembler(..., signe=+1)) -- je l'ai lu dans le code, je n'ai pas rouvert les 43 fichiers un a un. Donc :
      aucun calcul 2D du systeme a fantome a un w2 candidat, aucune largeur 2D de l'etat (0, 0) du systeme a fantome. DECLARATION COMPLETE de ce que j'ai calcule AUJOURD'HUI :
      (i) le rejeu de tes scripts, dont des chaines a UNE dimension a delta = +-0.005, +-0.01, +-0.02 (donc w2 = 1.995 et 2.005, candidats, en 1D seulement, comme toi) ;
      (ii) la 2D au JUMEAU seulement : w2 = 101/50 et 199/100 (ton temoin), 101/50 jusqu'a N = 166 (ta section 8), et w2 = 3999/2000 et 4001/2000 (section 4 ci-dessous) ;
      aucun n'est candidat. Une recherche de texte n'est pas une preuve d'absence : elle ne voit pas un w2 note autrement. Mes premiers passages sont gardes (premier balayage sans
      contexte des lignes, balayage_E19_..._premier_passage.log).
  (e) BOITES. Ta faisabilite rejouee sur BOCAL4 (script DERIVE : `import resource` est Linux seulement ; je mesure le pic de l'ensemble de travail, GetProcessMemoryInfo ; diff joint) :
      18 lectures sur 18 suivies, jusqu'a N = 166 ; largeurs du jumeau 3.9e-56, 1.9e-78, 1.0e-100 comme les tiennes ; pic 411 / 538 / 662 Mo (tu mesures 699), 15 / 19 / 26 s.
      Mon premier passage de ce script rendait "memoire max 0 Mo" : DEFAUT DE MON INSTRUMENT (ctypes sans types d'arguments), garde a cote, corrige ensuite. BOCAL4 : 16 coeurs
      logiques, 27.8 Go, 15.6 Go libres au moment du test. Ordre de grandeur du run : 4 absorbeurs x 12 barreaux = 48 lectures par cellule, de l'ordre de 3 a 5 min par cellule a N = 166
      d'apres mes mesures (3 s a 4.4 s par lecture aux absorbeurs A et B) ; je le redirai a la seconde partie.

## 3. TES DIX "OU MORDRE"

  M-1 couplages : voir (b), 0 difference.  M-2 Gamma : voir (a) ; l'etat n'est ambigu nulle part.  M-3 seuil 0.02 : aucune cellule n'en approche (0.0093), meme chez moi.
  M-4/M-5 j'ai lu ta note du vide et la loi d'echelle avant de certifier le bloc : section 4.  M-6 : section 4 (jumeau a |delta| = 0.0005, rien de genant) -- ce n'est pas une preuve
  pour le fantome.  M-7 : d'accord, la ligne profonde hors des enonces letaux ; je refais la reference "233 decades" par une autre methode (section 4).  M-8 : voir (d).
  M-9 r_c = 2 (m_bord + max(8, m_bord)) + 2 : les boites que j'ai jouees (N = 114 a 166) sont celles de ta table.  M-10 les ouvertures de 10 h 10, 11 h 03 et 12 h 19 sont des
  declarations de ta part ; je ne les ai pas vues, je n'en atteste aucune : c'est a l'operateur.

## 4. TA NOTE SUR LE VIDE : CE QUE J'AI REJOUE ET CE QUE J'AI TROUVE EN PLUS

  REJEU (rejeu_vide_machine2/, tes sept scripts, `py -3.11 -P`, un fil BLAS chacun, entrees aux canons) : 0 echec, structure des sorties identique ; le jumeau 2D se reproduit a 4.3e-16
  relatif (192 nombres, largeurs de 1e-61 a 1e-35 comprises) ; le procede profond est identique ; les chaines 1D different d'au plus 1.7e-7 en absolu sur les valeurs > 1e-3 (BLAS
  de Windows contre Linux) ; comptes 118 / 50 / 46 identiques. REFERENCE DES "233 DECADES" refaite par une AUTRE methode (determinant en precision arbitraire, ma regle de barriere
  qui rend m_bord = nombre de barreaux aux six points) : a 1.1e-13 de ta fraction continue et a 7.1e-15 de la lecture du lecteur, de 4 a 128 barreaux, jusqu'a exp(-535.7).
  SECTION 5 recomptee depuis MES sorties : 168/185, mediane -0.0094, 78 plus pres (71 sur 81 ; 7 sur 104), |ln q3| 0.0192 / 0.0159, pire 0.0996 / 0.0902, etendue 0.021 / 0.064 / 0.33,
  0 et 0 hors de E1 : tout est exact. Les cinq D-VIDE correspondent au texte de la note d'echelle.
  CE QUE J'AI TROUVE EN PLUS (apres coup, aucun verdict n'est modifie ; robustesse_variantes_joues_machine2_v1.py : j'ai garde les 18 valeurs au lieu de la mediane) :
   * Sur les 185 etats joues, 14 ont AU MOINS UNE des 18 variantes de ton absorbeur adapte hors de la tolerance E1 (20 couples etat x variante) ; AUCUN avec la mediane ou la regle
     deposee. Ils sont tous dans trois cellules a grand |delta| : M2 (-0.080 : 6 couples, pire variante 3.3 fois la tolerance), BN (-0.076 : 5, 1.8 fois), BP (+0.067 : 9 couples ;
     trois etats sur cinq ont 3 variantes sur 18 au-dessus de 0.1, la pire a 0.1221). Le "TENU" de BP, a +0.000383 de marge (0.09962 pour 0.1), est donc plus mince que l'ambiguite de
     l'absorbeur de la chaine (etendue 0.054, 140 fois la marge) -- ce que j'avais note dans mon contreseing du delta 100 sur le seul plateau 2D. Ta phrase M-5 ("rien n'est rejuge") est exacte ;
     la phrase qui manque est celle-ci.
   * Le residu chaine - 2D a le SIGNE DE DELTA aux 185 etats sous l'absorbeur adapte (delta < 0 : tous negatifs, le moins negatif -0.0091 ; delta > 0 : tous positifs, le moins positif +0.0011),
     et croit avec |delta| (medianes par cellule : de 0.003 a 0.01 vers |delta| = 0.03, jusqu'a 0.09 vers 0.067). Ce n'est pas du bruit : la chaine SOUS-corrige le terme en delta (ta note d'echelle : r a le
     signe oppose a delta a 184 etats sur 185 ; la chaine en rend de l'ordre de 90 % : q3 median 0.019 contre r median 0.255 ; de 1 % a 18 % de r reste, selon la cellule, regle deposee).
     Extrapole aux cellules du gel (|delta| <= 0.019, |r3*| <= 0.034 dans ta note) : un residu attendu de l'ordre de 0.005, au plus 0.01. C'est une extrapolation, pas un fait ; elle n'est pas dans ton gel.
   * Aucune des tolerances de la campagne n'a ete pensee pour cela : si V1 prend 0.05 (E1), le gel passerait avec une chaine fausse de 5 fois ce qu'on attend d'elle.
  M-6, sur le jumeau (script derive, w2 = 3999/2000 et 4001/2000, |delta| = 0.0005, le plus petit delta du gel divise par deux, les deux signes, trois profondeurs, N jusqu'a 166) : 18 lectures
  sur 18 suivies a chaque signe, largeurs de 1e-152 a 1e-81 ; le meme pic de memoire, 44 s pour la plus grosse geometrie. Rien de genant ; le fantome n'est pas lu.
  CE QUE LA NOTE NE MONTRE PAS (et qu'elle dit) : "suivi" du lecteur est un critere de CONVERGENCE (residu <= 1e-11, poids >= 0.5), pas d'exactitude de Gamma ; sous 1.3e-12 en absolu aucune
  seconde mesure 2D independante n'existe (la decomposition dense s'arrete la, ta section 7 de la note d'echelle : la 2D n'a lu que jusqu'a Gamma/|delta| = 2.95e-11) ; le jumeau prouve un
  PLANCHER (largeur fabriquee par l'absorbeur, 1e-35 a 1e-149), pas une exactitude ; aucune largeur 2D du fantome n'a jamais ete lue.

## 5. CE QUE JE TE DEMANDE POUR LA SECONDE PARTIE (je les certifierai sur ce qui sera ecrit)

  R-1 TOLERANCE. Dis, avant le run, le lien entre la tolerance de V1 et ce que la chaine peut : etendue <= 0.0093 aux 252 cellules, residu attendu <= ~0.01. 0.05 (celle de E1) serait cinq fois
      la plus grande etendue et cinq fois le residu attendu : un test peu risque ; je defendrais <= 0.02 (plus de deux fois l'etendue maximale), a toi de trancher et de le justifier ecrit.
  R-2 JUGEABILITE. Une cellule dont la marge (tolerance - |ln q|) est plus petite que l'etendue des 18 variantes est "NON JUGEABLE", jamais "tenue" ni "non tenue". C'est la regle qui aurait
      empeche le cas BP.
  R-3 GARDE. Sous Gamma ~ 1.3e-12 en absolu (les cellules m >= 5 : G3* de 7.6e-14 a 1.4e-12 a m = 5, plus bas ensuite), la qualification en cours de run (plateau, accord des quatre absorbeurs) est la SEULE garde :
      nomme-le dans la piece, et dis ce que vaut un accord des quatre absorbeurs (il teste l'independance de la boite et de la forme, pas l'exactitude de la largeur).
  R-4 TEMOINS. Le jumeau a la geometrie de CHAQUE cellule tiree, y compris le plus petit |delta| tire (le meme script que la section 8 suffit ; je l'ai joue a 0.0005).
  R-5 SIGNE. Ne pas ajouter un enonce sur le signe du residu (ce serait un enonce neuf, pose apres avoir vu) ; mais le dire dans "ce que chaque issue engage" : si V1 tient, ce n'est pas
      la preuve que la chaine est exacte, c'est que son defaut connu est plus petit que la tolerance.

## 6. CE QUE JE N'AI PAS FAIT

  Aucune 2D du fantome, a aucun w2. La seconde partie n'existe pas : rien a certifier de l'instrument, des enonces, des tolerances. Je n'ai pas relu ton construction_regle_tirage_vide_machine1_v1.py
  ni ton balayage de virginite (j'ai fait le mien par ma methode), ni le tirage du registre (0f608f8ade6ff378). Mon calcul de Gamma partage avec toi les TABLES (blocs deposes, certifies aux deltas 98 a
  100) : c'est l'assemblage de la matrice (4.3) et le calcul de la largeur qui sont independants. Le "go" et la graine sont a l'operateur.

## 7. SUITE
  (1) tu me confirmes la reception et ta table commune (ton tirage_vide_machine1_v1.py la fait ; la mienne est dans ce lot) ; (2) l'operateur donne la graine aux deux machines, par ecrit, APRES avoir
  lu ceci ; (3) chacune tire ; (4) ta seconde partie ; (5) ma certification ; (6) feu vert ecrit ; (7) un seul run.
  Aucun delai.

## 8. PIECES (convention B)

    cette note
    d6c25cc88f2dbce5  livraison_16e_vide_etape_sans_run/authentifie_lot_vide_m1_machine2_v1.py
    8a2f525742468d33  livraison_16e_vide_etape_sans_run/authentifie_lot_vide_m1_machine2_v1.log
    ce268bc2681355c8  livraison_16f_gel_vide_partie1/authentifie_lots_gel_vide_machine2_v1.py
    d34cb418c3fd668f  livraison_16f_gel_vide_partie1/authentifie_lots_gel_vide_machine2_v1.log
    bd0fc7a2e3abe0ae  certif_gel_vide_partie1_machine2/table_eligibilite_vide_machine2_v1.py
    5cba0a5566c957fb  certif_gel_vide_partie1_machine2/table_eligibilite_vide_machine2_v1.log
    84bffbbd2f675181  certif_gel_vide_partie1_machine2/table_machine2_vide_v1.json
    e4810d2661e2c5dc  certif_gel_vide_partie1_machine2/detail_machine2_vide_v1.json
    2147a2f8e988afb3  certif_gel_vide_partie1_machine2/recoupe_tables_vide_machine2_v1.py
    f10b3326f4aa639e  certif_gel_vide_partie1_machine2/recoupe_tables_vide_machine2_v1.log
    84bffbbd2f675181  certif_gel_vide_partie1_machine2/table_commune_vide_machine2_v1.json
    3b973fe9ae0cef3f  certif_gel_vide_partie1_machine2/controle_kappa_m_machine2_v1.py
    b74627d0b9aec82a  certif_gel_vide_partie1_machine2/controle_kappa_m_machine2_v1.log
    970ab581f29df451  certif_gel_vide_partie1_machine2/tirage_demonstration_machine2_v1.py
    a7cf27ad3f139717  certif_gel_vide_partie1_machine2/tirage_demonstration_machine2_v1.log
    8d09e6c8e44037f8  certif_gel_vide_partie1_machine2/tirage_m1_autotest_rejoue_machine2.log
    dddd739e708fc6b5  certif_gel_vide_partie1_machine2/tirage_m1_demonstration_rejouee_machine2.log
    86516daa1c8003d5  certif_gel_vide_partie1_machine2/balayage_E19_vide_machine2_v1.py
    d41ca51eeef9fb96  certif_gel_vide_partie1_machine2/balayage_E19_vide_machine2_v1.log
    0422225b5ed70fe5  certif_gel_vide_partie1_machine2/balayage_E19_vide_machine2_v1_premier_passage.log
    d27edf8ced87dc5b  certif_gel_vide_partie1_machine2/triage_E19_contexte_machine2_v1.py
    c4de4684889d297f  certif_gel_vide_partie1_machine2/triage_E19_contexte_machine2_v1.log
    03bc56b8f98b258c  certif_gel_vide_partie1_machine2/balayage_etat_00_machine2_v1.py
    0fde5dae047d92ac  certif_gel_vide_partie1_machine2/balayage_etat_00_machine2_v1.log
    9499c9c12ec45041  certif_gel_vide_partie1_machine2/derive_faisabilite_machine2_v1.py
    1a97c9890d85fa92  certif_gel_vide_partie1_machine2/faisabilite_profondeur_jumeau_machine2_v1.py
    c510390492219b67  certif_gel_vide_partie1_machine2/faisabilite_profondeur_jumeau_machine2_v1.diff
    8707ace5f4c333cf  certif_gel_vide_partie1_machine2/faisabilite_profondeur_jumeau_machine2_v1.log
    2ec3772406043bf1  certif_gel_vide_partie1_machine2/faisabilite_profondeur_jumeau_machine2_v1.json
    01e54a4ded68748d  certif_gel_vide_partie1_machine2/faisabilite_profondeur_jumeau_machine2_v1_premier_passage_memoire_0.log
    5d526dc973cf2240  certif_gel_vide_partie1_machine2/faisabilite_profondeur_jumeau_machine2_v1_premier_passage.json
    80307971b445def8  certif_gel_vide_partie1_machine2/derive_petit_delta_machine2_v1.py
    11a5581504f31710  certif_gel_vide_partie1_machine2/faisabilite_petit_delta_w2_1_9995_machine2_v1.py
    c48f5507ffd2dfc9  certif_gel_vide_partie1_machine2/faisabilite_petit_delta_w2_1_9995_machine2_v1.diff
    b20c9fa0ac886de6  certif_gel_vide_partie1_machine2/faisabilite_petit_delta_w2_1_9995_machine2_v1.log
    871ff776c48219cd  certif_gel_vide_partie1_machine2/faisabilite_petit_delta_w2_1_9995_machine2_v1.json
    dfadbb8a57f89af0  certif_gel_vide_partie1_machine2/faisabilite_petit_delta_w2_2_0005_machine2_v1.py
    098dc4f6b605e870  certif_gel_vide_partie1_machine2/faisabilite_petit_delta_w2_2_0005_machine2_v1.diff
    000642dd4c2719da  certif_gel_vide_partie1_machine2/faisabilite_petit_delta_w2_2_0005_machine2_v1.log
    f0d0cc0a217c156d  certif_gel_vide_partie1_machine2/faisabilite_petit_delta_w2_2_0005_machine2_v1.json
    be0d931e607fe8d3  rejeu_vide_machine2/rejeu_vide_machine2_v1.py
    acebc065dbc8b1e4  rejeu_vide_machine2/console_rejeu.log
    5a78efc7fb3ab48f  rejeu_vide_machine2/compare_rejeu_machine2_v1.py
    35ef5a4102a276af  rejeu_vide_machine2/compare_rejeu_machine2_v1.log
    8c273ccc8d48e87a  rejeu_vide_machine2/verifie_phi_profond_machine2_v1.py
    10617f0538eae9d5  rejeu_vide_machine2/verifie_phi_profond_machine2_v1.log
    c20621a730e38b97  rejeu_vide_machine2/recompte_titres_machine2_v1.py
    09597b8d4b20b8aa  rejeu_vide_machine2/recompte_titres_machine2_v1.log
    4b206af86f335788  rejeu_vide_machine2/analyse_biais_joues_machine2_v1.py
    6b2d7f7bd8bc770e  rejeu_vide_machine2/analyse_biais_joues_machine2_v1.log
    b1159c60d3f6d4b7  rejeu_vide_machine2/robustesse_variantes_joues_machine2_v1.py
    a3b22869c27433b2  rejeu_vide_machine2/robustesse_variantes_joues_machine2_v1.log
    bbc24ebe127d902e  rejeu_vide_machine2/sortie/absorbeur_adapte.log
    998067857bca65a9  rejeu_vide_machine2/sortie/absorbeur_adapte_v1.json
    396462e9ae1b895b  rejeu_vide_machine2/sortie/apres_barriere.log
    6681989f7e73b0ca  rejeu_vide_machine2/sortie/apres_barriere_v1.json
    80b53ff67fa4bd2d  rejeu_vide_machine2/sortie/carte_adaptee.log
    90565375524b0592  rejeu_vide_machine2/sortie/carte_adaptee_v1.json
    46c6550280bba940  rejeu_vide_machine2/sortie/controle_joues_absorbeur.log
    db678eb492139fe6  rejeu_vide_machine2/sortie/controle_joues_absorbeur_v1.json
    8a4c0df6508467a4  rejeu_vide_machine2/sortie/mandataire_absorbeur_2D.log
    7820dfbb62feabb3  rejeu_vide_machine2/sortie/mandataire_absorbeur_2D_v1.json
    f3aca9f123c1788b  rejeu_vide_machine2/sortie/procede_lecteur_profond.log
    77fafabcececc9ab  rejeu_vide_machine2/sortie/procede_lecteur_profond_v1.json
    49417e86b917ee8b  rejeu_vide_machine2/sortie/robustesse_variantes_joues_machine2_v1.json
    a1f437aa90f14118  rejeu_vide_machine2/sortie/temoin_lecteur_vide.log
    acef3f72e8137c06  rejeu_vide_machine2/sortie/temoin_lecteur_vide_v1.json
    (ce script)  fabrique_lot_certification_gel_vide_partie1_machine2_v1.py
