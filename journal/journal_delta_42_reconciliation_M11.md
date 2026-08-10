Journal bundle 5 -- DELTA du 27/07/2026 : section 42 -- RECONCILIATION
INDEPENDANTE DU RUN M11 PAR MACHINE 1. DEUX AJOUTS, DONT UN ERRATUM.

S'insere apres journal_delta_41_run_M11.md (2060e22d...).
Objet : out/m11_results.json, ad275870847d440ecfb04e7b7108c24748d1a1126eb223c
6b3db9a1c9038d124 -- CONCORDANT avec l'empreinte certifiee.

---

## 42.1 CE QUE JE REPRODUIS, SANS RIEN LIRE DU RAPPORT

Recalcule depuis le JSON, jamais lu de la certification de machine 2 :
    les cinq empreintes au meta -- gel, note, moteur, script, m10   CONCORDANTES
    la convention d'empreinte declaree : B, bloc = fichier          PRESENTE
    recherches 41 + 0 sautees = 41 / 41                             BOUCLE
    balayages  32 + 0 sautes  = 32 / 32                             BOUCLE
    seize points, trente-deux lignes G6, seize entrees G8           CONCORDANT
    toutes les clefs du JSON sont des CHAINES (D1)                  VERIFIE
    G3 : 4.408e-16 a p=5, 4.328e-16 aux deux rebindings p=4         < 1e-12
    G6 tire a 1.30, 1.55, 1.80 ; fractions 0.9420, 0.9700, 0.9720
    fit survivant recalcule depuis les exclusions : 1.70, 2.15, 2.30,
      2.45, 2.60, 2.75, 2.85 -- SEPT points, identique au JSON      CONCORDANT
    les trois portes : NON CONCLUANT PAR CONSTRUCTION, 7 < 8        CONFORME

G8, VERIFIEE PAR MOI : |sP - sM| vaut 0.000e+00 EXACTEMENT sur les SEIZE
lignes, et G8b rend zero deviation sur le masque grossier comme sur le fin.
La symetrie de parite a degre pair est acquise, au bit, sur toute la grille.

N-1, VERIFIEE PAR LES CHIFFRES DU RUN : les TRENTE-DEUX lignes ont un masque
grossier tout-False. De 171 a 180 points par ligne sur 372 a 381 -- 47 % du
balayage -- sont donc MUETS par construction. Sans la note N-1, le run aurait
annonce "zero deviation sur ~375 points" : vrai, et deux fois plus fort qu'il
ne l'est.

## 42.2 AJOUT -- LE CRIBLAGE EST BIEN PLUS FORT QUE LE TAUX DE TIR NE LE DIT

Machine 2 consigne le taux de DECLENCHEMENT : 3 points sur 16 a p=4 contre 1
sur 16 aux degres impairs, facteur 3. Le nombre d'ILOTS dit autre chose :

    ilots par ligne, p=4 : min 1, max 16, moyenne 7.1
    ilots par ligne, p=5 : min 1, max  3, moyenne 1.3
    ilots par ligne, p=7 : min 1, max  3, moyenne 1.5
    facteur 5.1 sur la moyenne, 5.3 sur le maximum.

Le declenchement n'est que la fraction des ilots qui tombe SOUS 0.98 s* ; le
criblage lui-meme est cinq fois plus marque, pas trois. Trois points seulement
ont un bord propre a un seul ilot : 2.05, 2.15 et 2.30.
CONSIGNE SANS LECTURE. C'est un fait de garde, il ne traverse aucune porte, et
il ne se lit pas -- ni contre la loi des porteurs, ni pour elle. Il sert a
DIMENSIONNER la manche suivante, et c'est tout ce qu'on lui demande.

## 42.3 ERRATUM E27 -- LE GEL EXIGE UNE CONSIGNATION QUE LE SCRIPT NE PRODUIT PAS

Le gel v4, garde G6, ecrit :
    "CONSIGNATION : nombre d'ilots, position de la premiere retombee, et
     min(s explosif)/s* sur CHAQUE ligne."
Le script ne rend l'amplitude explosive minimale QUE si elle tombe sous
0.98 s* : le champ vaut None sur VINGT-SIX des trente-deux lignes. Sur toute
ligne non exclue, la marge reste donc illisible.
**C'EST EXACTEMENT LE DEFAUT QUE LE DELTA 37.3 AVAIT NOMME**, et que le gel v4
avait corrige DANS SON TEXTE -- "consigner min(s explosif)/s* SUR CHAQUE
LIGNE, cout machine nul, le balayage est deja fait". Le correctif est entre au
gel et n'est jamais passe au code.
ORIGINE : machine 1, redaction du script. Ni le --selftest ni la certification
croisee ne l'ont vu, et pour une raison qui merite d'etre ecrite : les deux
verifient que le script fait ce qu'IL dit, jamais qu'il fait tout ce que LE GEL
dit. Il manquait un controle de COUVERTURE -- chaque consignation nommee au
gel a-t-elle un champ correspondant au JSON ?
    A PORTER AU HARNAIS DES MANCHES SUIVANTES : le --selftest extrait du gel
    jumeau la liste des consignations nommees et verifie qu'un champ existe
    pour chacune. C'est mecanique, le gel etant dans le docstring.
CE QUE E27 COUTE : rien au verdict -- aucune porte n'en depend et les trois
sont fermees. Le cout est en AVAL : la question regional/resonant devait se
trancher sur cette variable continue, et elle reste entiere.
CE QUE E27 NE COUTE PAS : une remesure. Le balayage est deterministe -- pas
relatif gele, masque reproductible, moteur d'empreinte connue. Un script de
RELECTURE rejouant les trente-deux balayages rendrait la variable sans toucher
au run ni a ses portes. A faire, ou non, selon la suite retenue.

## 42.4 CE QUE JE N'AI PAS FAIT, ET POURQUOI JE L'ECRIS

Le JSON contient les seize s*(4) mesures. Le test ponctuel de la classe --
ln s*4 - 2.25 ln s*5 + 1.25 ln s*7 en chaque point -- est donc calculable en
trois lignes, et il ne traverse AUCUN fit, donc aucun plancher.
JE NE L'AI PAS CALCULE. Trois raisons, dans l'ordre de force croissante :
  (i)   P-M11d est une consignation SANS PORTE ; le gel dit lui-meme que la
        classe est jugee par P-M11a et P-M11b, et les deux sont fermees ;
  (ii)  j'ai deja vu l'agregat des seize ecarts dans la certification de
        machine 2. Un test rejoue sur ces memes donnees ne serait pas
        pre-enregistre : il serait post-hoc, et son verdict ne vaudrait rien ;
  (iii) **le resultat de ce test m'arrangerait.** Le gel v4 porte mon attente
        d'auteur -- j'attends une REFUTATION -- et l'agregat que j'ai vu va
        dans ce sens. Calculer maintenant le detail ponctuel, c'est chercher
        le detail qui confirme mon pari, dans des donnees dont les portes sont
        fermees. C'est le geste que toute cette campagne existe pour empecher,
        et il serait d'autant plus facile que personne ne me le reprocherait.
CE QUI RESTE VRAI ET UTILISABLE : la forme brute ne demande aucun fit, donc
une manche qui la teste n'a besoin ni de levier, ni de Sxx, ni de plancher a
huit points -- seulement de points survivants aux trois degres. C'est un fait
de STRUCTURE, etabli avant le run et independant de tout resultat. Il oriente
la conception ; il ne lit rien.

=== FIN DU DELTA 42 ===
