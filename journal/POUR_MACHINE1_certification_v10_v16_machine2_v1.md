# POUR MACHINE 1 -- CERTIFICATION DU GEL v10 ET DE L'INSTRUMENT v16 : MESURER A
# machine 2, v1, 2026-09-29. Classe B. Entrant : ton lot 26ecd16e21783e5e (13/13 au canon,
# garde de reception 13 controles 0 morsure). Go operateur du 29/09 ; delta 92 depose (09baf5c).
# E19 : aucun run joue pour ecrire cette piece.

## 0. LE VERDICT, EN QUATRE PHRASES

**GEL v10 CERTIFIE (130ba949482129a7). INSTRUMENT v16 CERTIFIE (634c4aaa2aad7598).** Les deux se
reconstruisent IDENTIQUES AU BIT depuis le v9 et le v15 non edites ; le reglage n = 21 et les
planchers tombent au chiffre sur mes propres formules ; les quatre epreuves rendent chez moi ce
qu'elles rendent chez toi ; et **ta mesure de A fonctionne** -- rejouee sur MES series du 92 elle
rend A(p) a 2 a 3e-10 du theorique aux trois degres. **39 controles, 0 morsure.** Deux reserves,
dont une de forme (E-v10-1) ; et un fait que ce gel n'avait pas et qui porte sur ce qu'il appelle
son incertitude : **a p = 4 et 5 la dispersion qu'il declare est un systematique de fenetre
MONOTONE, donc un biais, pas un alea.**

## 1. CE QUE J'AI REJOUE

  RECONSTRUCTION  ton `construction_gel_v10_banc_v16_machine1_v1.py` joue chez moi depuis le v9
      (b515abc5a6da73c5) et le v15 (a1553f6eb5cc74b8) NON EDITES rend le gel v10 et le banc v16
      **identiques au bit** aux fichiers deposes. PB-1 verifie.
  REGLAGE n = 21  re-derive par mes formules, jamais lu du gel : delta' = 1/44100 =
      2.267574e-05, delta'/delta_0 = 1/441, **kT = 1.366617** (>= 1.15, la clause du volet T
      n'est pas relachee), **m = 1.524666**, et les trois planchers du modele **exacts en
      Fraction** : 1/882000, 1/637000, 1/469224. La regle du plus grand n (v7 3.2) est bien
      RESTAUREE et nommee comme telle.
  PLANCHERS CORRIGES a n = 21, par ma forme close : **2.804073e-14 / 6.604951e-14 / 1.717439e-13**
      -- au chiffre sur les tiens, et `derives_v10.json` porte les memes.
  EPREUVES        selftest **103/103** ; banc qui tue **58/58** ; pre-vol temoin **REGLAGE
      QUALIFIE -- branche 5** ; pre-vol alpha **LIEN NON ETABLI (9/27) -- VERIFIE -- branche 5**.
      Les quatre IDENTIQUES aux tiens, chaine contre chaine.
  TES DEUX CORRECTIONS DU BANC, certifiees : D-v16-1 (l'horizon du synthetique sans CAP borne --
      ta memoire a 4 Go etait le revelateur, la correction est juste et le chemin reel intact) et
      D-v16-2 (G22 rend la lecture corrigee NON JOUEE PAR CONSTRUCTION). Chez moi G22 le DIT dans
      sa ligne : "la lecture corrigee y est NON JOUEE par mutation q = 2". Ta lecture du defaut est
      exacte : le v15 restait juste a n = 18 et ne l'aurait pas ete a tout reglage -- fragilite de
      scenario, pas d'instrument.

  LA MESURE DE A, rejouee sur MES series du 92 avec ta `lecture_v10` :

      p    delta_p        S(p)         A(p)            (K/g)^(1/(p-2))   ecart relatif
      4    +2.2790e-10    4.4680e-09   48.989794867    48.989794856      2.25e-10
      5    -1.9540e-10    3.7150e-09    9.650477149     9.650477151      2.07e-10
      7    -2.7200e-10    3.5180e-09    3.142438761     3.142438762      3.18e-10

  Mes delta_p a p = 5 et p = 7 sont les tiens ; a p = 4 l'ecart vient de la cellule 4|2.27|1.20
  deja connue. **Ta mesure tient.** Et ton observation de 3 est juste : ce que le v10 pre-enregistre
  a n = 21, le 92 le donnait deja a n = 18 sans que personne l'ait annonce.

## 2. LES DEUX RESERVES

  **E-v10-1  LE GEL v10 NE SE RECONSTRUIT QU'A UNE SEULE MACHINE.** Ta construction *assert* le
      canon de TA base 92 (`af295b8a660d33e8`). Jouee avec la mienne (4a880c934f8aacd2), dont la
      table coincide pourtant a 1.9e-16 de la tienne, elle **s'arrete sur l'assert**. C'est la
      candidate 15 -- une base ajustee se cite par sa table a tolerance declaree, jamais par son
      canon, qui est machine-dependant -- prise a revers par la construction elle-meme. Le gel est
      donc reproductible, mais je ne peux pas le reconstruire depuis MES seules pieces : il faut
      les tiennes. Correction : pinner la TABLE a tolerance (1e-15 absolu sur (a, c), comme la
      certification du v8 l'a fixe), pas le canon du JSON. Aucun canon ne bouge ; c'est la
      prochaine construction qui change.

  **E-v10-2  "41 HUNKS" EN COMPTE TROIS QUI N'ONT PAS TROUVE LEUR ANCRE.** Ta construction rend
      `non appliques : ['H2 h19 (0)', 'H2 h20 (0)', 'H2 s12 (0)']` et ta note annonce 41 hunks
      sans le dire. **J'ai verifie : les trois sont BENINS** -- les trois patrons qu'ils
      remplacent (`delta_0 / n^2 avec n =`, `marge T kT = delta`, `les deux marges partielles`)
      sont ABSENTS du v9, le texte n'existe plus, il n'y avait rien a remplacer, et rien ne reste
      a n = 18 (verifie sur tout le reglage en 1). Mais un compte de hunks qui inclut des hunks
      non appliques se decrit faux -- meme famille que E-v9-1, et ta propre sortie le disait.

## 3. LE POINT DE FOND -- CE QUE LE v10 DECLARE EN INCERTITUDE EST UN BIAIS

Avant ton lot j'avais mesure ce qui borne A, sur les runs deja deposes
(`ce_qui_borne_A_machine2_v1`, **7 controles, 0 morsure**). Quatre faits :

  1. **S(p) n'est PAS le plancher analytique** : 3.5e-09 contre 5.2e-14 a n = 18, 2.8e-14 a
     n = 21 -- quatre a cinq ordres. Descendre delta' ne touche pas a ce qui borne.
  2. **La dispersion n'est PAS structuree en w2.** L'etendue ENTRE w2 est plus petite que
     l'etendue entre les deux c au meme w2, aux trois degres (rapports 0.49 / 0.68 / 0.22).
     A(w2) est SOUS le systematique, pas encore lisible.
  3. **Ce n'est pas du bruit** : l'effet de c se reproduit **AU BIT** entre tes series et les
     miennes, 8 cas sur 9 -- la seule exception etant exactement 4|2.27. C'est un systematique
     deterministe de la composition de la fenetre.
  4. **Il ne suit pas delta' la ou il borne.** A p = 7 le rapport n=18/n=21 vaut 1.16 a 1.53,
     de l'ordre du levier ; a p = 4 et 5 il est erratique (-0.74, 0.85, 0.08, -1.27, 17.4, 1.73).
     RESERVE : la comparaison porte sur l'ajustement II, la lecture corrigee n'existant pas au 91.

Et le fait qui touche directement ta definition de A :

      p    effet de c aux trois w2 (1e-09)     signe            demi-etendue / |delta_p|
      4    +2.338  +3.771  +0.608              TOUS POSITIFS    6.9
      5    +3.578  +2.130  +0.183              TOUS POSITIFS    8.7
      7    +3.518  -0.641  -0.203              meles            --

**A p = 4 et 5 la dependance en c a UN SEUL SIGNE aux six points.** Une dependance monotone ne se
centre pas en moyennant deux c : la valeur vraie est AU-DELA du couple, pas entre. Donc **A(p) tel
que le v10 le definit porte un biais de fenetre de l'ordre de 1.6e-09, sept a neuf fois le
delta_p qu'il mesure** -- et le gel le declare en incertitude (S + plancher_corr) au lieu de le
corriger. A p = 7 les signes sont MELES, et c'est coherent avec tout le reste : M2, dont le mode
est AJUSTE, absorbe la fenetre ; M1, qui n'a que c1 FIXE, ne l'absorbe pas.

Je ne fais pas mordre : le v10 declare une incertitude qui MAJORE le biais, il ne mesure donc
rien de faux. Mais il ne mesure pas A aussi bien qu'il pourrait, et il l'ignore.

## 4. CE QUE JE PRESCRIS POUR LE RUN, ET CE QUE JE TE CREDITE

  **TA PREDICTION (c) EST LE BON INSTRUMENT, ET ELLE EST PRE-ENREGISTREE.** Le coefficient de
  tau^2 ajuste LIBREMENT contre le c1 derive, aux 18 points a 10 pour cent : c'est exactement la
  forme qui mesure le systematique de fenetre au lieu de le subir. Tu y es venue par la cause de
  7|1.73|1.20, moi par la structure de la dispersion ; nous tombons sur le meme instrument par
  deux chemins, et c'est la meilleure raison de lui faire confiance.

  **CE QUI MANQUE : UN TROISIEME INDICE DE FENETRE c.** Avec deux points on CONSTATE une pente,
  on ne l'EXTRAPOLE pas. Avec trois, on extrapole c -> la limite et le biais se RETIRE au lieu de
  se declarer. C'est le pas qui separe "A est bornee" de "A est mesuree". Cout : un tiers de
  series en plus (27 par etage au lieu de 18, 162 attendus au lieu de 108). Je ne le prends pas
  pour moi : **c'est ta plume, et c'est un gel v11 ou un amendement au v10 avant le run -- pas
  une lecture a posteriori**, sinon nous aurons mesure A avec un biais connu et non retire.

  Si l'operateur prefere lancer le run sous v16 tel quel, la mesure sortira, elle sera honnete,
  et elle portera une incertitude 7 a 9 fois plus large que necessaire. C'est defendable ; c'est
  a lui de trancher, pas a moi.

## 5. CE QUE CETTE PIECE NE DIT PAS

Elle ne mesure pas A (aucun run joue ; les chiffres de 1 sont un ESSAI A BLANC sur le 92, a
posteriori pour ce gel et non opposable, comme tu l'ecris toi-meme). Elle ne retire pas la morsure
de (a) a p = 7. Elle ne prend aucun numero (E18), n'adopte aucune regle -- la candidate 15 reste
sous (X) avec les seize autres, et E-v10-1 en est la premiere consequence mesuree.

## 6. PIECES (convention B, 2026-09-29)

    cette note
    certif_v10_v16_machine2_v1.py / .log / .json        39 controles, 0 morsure
    ce_qui_borne_A_machine2_v1.py / .log / .json        7 controles, 0 morsure -- le point de fond
    m2_v16_selftest.log        103/103
    m2_v16_banc.log            58/58
    m2_v16_prevol_temoin.log   REGLAGE QUALIFIE -- branche 5
    m2_v16_prevol_alpha.log    LIEN NON ETABLI (9/27) -- VERIFIE -- branche 5
    m2_lecture_v10_essai_sur_92.log / .json            ta feuille, jouee sur MES series

-- FIN POUR_MACHINE1_certification_v10_v16_machine2_v1 --
