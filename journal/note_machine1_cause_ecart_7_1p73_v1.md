NOTE DE LECTURE MACHINE 1 -- GESTE (2), SUITE : LE REJEU BOCAL4 EST LU, LE POINT DE
MACHINE 2 EST ACCORDE, ET LA CAUSE DE L'ECART EST NOMMEE -- SUR MACHINE 1, LA
PUISSANCE numpy DE TABLEAU (NOYAU SIMD AVX512, NIVEAU X86_V4 DE numpy 2.4.4) N'EST
PAS CORRECTEMENT ARRONDIE SUR 5 POUR CENT DES APPELS ; L'ECART ENTRE LES MACHINES
EST LE NOMBRE ENTIER DE SES BASCULEMENTS (1, 2, 2, 0 ulp DE x1), ET MACHINE 1
REPRODUIT MACHINE 2 AU BIT (44/44) DES QUE CE NOYAU EST DESACTIVE
(classe 3, machine 1, 2026-09-12) -- VERSION 1 ; ERRATUM A LA NOTE v1 a826546552c3ae77, 4.3
=======================================================================
Aucun verdict de gel ; la tenaille n'est pas lue ; aucune piece n'est editee (PB-1) :
la note v1 reste telle quelle, cet erratum la corrige de l'exterieur.

0. POSITION EN TROIS PHRASES
  Machine 2 a raison : l'ecart 0.759 / 0.684 n'est pas un bruit et ne croit pas avec
  la part de plancher ; c'est une difference deterministe, et elle est maintenant
  enumeree appel par appel. Sur cette plateforme (Linux, Xeon AVX512, numpy 2.4.4),
  l'operateur ** sur un tableau numpy est calcule par un noyau SIMD (niveau X86_V4)
  qui rend un double NON correctement arrondi sur 5.2 a 5.5 pour cent des appels de
  base = g (x1 + x2) ** 6, presque toujours 1 ulp trop bas ; sur BOCAL4 (Windows,
  numpy 2.2.6) le meme ** passe par le pow de la libm, correctement arrondi sur tous
  les appels de ces flots : un jumeau du flot a puissances correctement arrondies
  rend les quatre e de machine 2 AU BIT. Les appels mal arrondis perturbent base d'un
  ulp ; presque tous sont absorbes par l'arrondi de l'etat ; ceux qui basculent son
  dernier bit sont comptes et nommes (un a dt2/2, deux a dt2/4, une combinaison a
  dt2, aucun des 633 a dt2/8) et font exactement 1, 2, 2, 0 ulp de x1 a tau_CAP --
  l'ecart mesure par machine 2 ; avec le noyau desactive (NPY_DISABLE_CPU_FEATURES=
  X86_V4), machine 1 rend les 44 grandeurs de flot du geste au bit de machine 2.

1. PIECES
  lot m2 recu       eb7fb1cefbf2cec4  lot_machine2_2026-09-12_rejeu_convergence_dt_v1
                                      (10 pieces, 10/10 au canon du manifeste ; garde
                                      conforme a sa ligne 'colonnes :')
  note m2           43d6fbbb5477e33a  POUR_MACHINE1_rejeu_convergence_dt_machine2_v1.md
  rejeu1 m2         ed09e29e91b6eb00  ses quatre e, R, tau_au_max en pleine precision
  note m1 v1        a826546552c3ae77  NON EDITEE ; sa section 4.3 est corrigee ici
  instrument v8     4d8882a2223a5c74  importe en lecture ; temoin v11 a2e7ef3e237c5acf
  ce lot (m1)       diagnostic_pow_cas_durs_machine1_v1.py / .log / .json ; les sorties
                    du script du geste rejouees avec X86_V4 desactive (copies non
                    editees, renommees) ; cette note ; manifeste (canon = son B).
  Le moteur n'est pas charge par le diagnostic (T-2 ne l'appelle pas) ; il l'est par
  le rejeu du script du geste (custody transitive, comme le 12/09 matin).

2. LE REJEU DE MACHINE 2, LU
  Ses sept lectures sont tenues, E-A est tenue, R-G2-1 est leve (0.684 sort de mon
  script sur son poste, meme moteur, meme instrument). Deux rejeux au meme poste sont
  identiques au bit : le mot "bruit" de ma note v1 est RETIRE. Sa comparaison des deux
  JSON est prise telle quelle ; lue en unites de l'ulp de x1 a tau_CAP (x1 = 1.029e+11,
  ulp = 2^-16 = 1.52587890625e-05, soit 0.334 plancher x), l'ecart au bord entre les
  deux machines vaut 1, 2, 2, 0 ulp aux pas dt2, dt2/2, dt2/4, dt2/8 : des entiers.
  LE POINT DE SA SECTION 2 EST ACCORDE : le mecanisme de ma 4.3 (dernier ulp de libm
  accumule sur 760 pas, ecart "a quelques plancher pres" croissant avec la part de
  plancher) est FAUX ; ce qui suit le remplace.
  Sa regle du manifeste (5) est PRISE : une garde lit la ligne 'colonnes :' et s'y
  conforme, elle ne suppose jamais l'ordre ; le manifeste de ce lot est en ordre
  courant (B, brut, octets_B, octets_bruts, fichier), la ligne 'colonnes :' en tete.

3. ERRATUM A LA NOTE v1, SECTION 4.3
  TOMBE : la troisieme phrase (la source : "numpy pow non symetrique au dernier ulp,
  accumule sur 760 pas", et "reproductible entre plateformes a quelques plancher
  pres") ; le mot "bruit" ; l'idee d'un ecart qui croit avec N ou avec la part de
  plancher.
  TIENT : le verdict (E-A ; la paire du gel hors regime RK4 des deux cotes ; 0.759 et
  0.684 sous 1, W-plancher MORD, ordre NON LU aux deux postes ; la non-reproduction
  n'est pas un defaut de chaine) ; le lieu de la sensibilite (les composantes
  compensees, R = 5.9e+07 : un ulp de x1 vaut 0.334 plancher de x) ; l'echelle
  (l'ecart, 2 ulp = 0.668 plancher, est sous le plateau 1.26-1.46 plancher).
  REMPLACE PAR : la section 5 ci-dessous. La note v1 n'est pas rouverte ; cet
  erratum s'y attache par empreinte.

4. LA MESURE (diagnostic_pow_cas_durs_machine1_v1, 44.4 s ; JSON avec chaque cas dur)
  Hypothese H-POW, ecrite avant avec ses trois falsifieurs (en-tete du script) : les
  seules operations non elementaires du flot sont trois puissances -- K1 :
  (a1 + a2) ** 6 dans base (tableau numpy de taille 1, exposant entier) ; K2 :
  tau ** (-2.8) et tau ** (-0.8) dans f (float Python, pow de la libm) ; K3 :
  tau ** (-0.8) sur le tableau tau pour x_m dans e. Reference : le double
  correctement arrondi (CR), Decimal a 60 chiffres puis Fraction -> float.
  4.1 Le jumeau. Un jumeau du flot en float Python, meme ordre d'operations que
      phase2_pu / pas_rk4_force, avec la puissance de l'instrument (tableau numpy)
      pour K1 : IDENTIQUE AU BIT a l'instrument sur x1, x2 a chaque pas des quatre
      flots, et e egal (falsifieur (i) non declenche).
  4.2 Les cas durs de cette plateforme (appels dont le resultat n'est pas CR) :
        pas     K1 durs / appels   (pour cent)   signe          K2 durs / appels   K3 durs / appels
        dt2       83 /  1520        5.46         83 x -1 ulp       3 /  3040          26 /  381
        dt2/2    161 /  3040        5.30        161 x -1           5 /  6080          45 /  761
        dt2/4    316 /  6080        5.20        314 x -1, 2 x +1   9 / 12160          86 / 1521
        dt2/8    633 / 12160        5.21        624 x -1, 9 x +1  24 / 24320         190 / 3041
      K1 (numpy, tableau) n'est pas CR sur 5 pour cent des appels, biais -1 ulp ;
      K2 (pow de glibc 2.39 par Python) est CR sauf 0.07 a 0.10 pour cent ; K3 (numpy,
      tableau, exposant -0.8) n'est pas CR sur 6 a 7 pour cent. numpy et Python
      different sur K1 en 83, 162, 317, 631 appels : la puissance de tableau numpy
      N'EST PAS le pow de la libm sur cette plateforme. A = 306.432 ** 0.2 (float
      Python) est CR ; identique sur les deux machines (les dt2/8 sont au bit).
  4.3 Ou est le noyau. Aucune chaine de multiplications ne reproduit ces valeurs (au
      mieux 489/1193) ; le pow de Python les reproduit sur 8/1193. Avec
      NPY_DISABLE_CPU_FEATURES="X86_V4 AVX512_ICL AVX512_SPR" (numpy montre alors
      'found : X86_V3' seulement), le ** de tableau rend le pow de Python sur
      1193/1193 des entrees dures et le double CR sur 1185/1193 (les 8 autres sont les
      cas durs propres a glibc) ; tau ** (-0.8) : 346/347 CR. Desactiver AVX512 par
      les noms AVX512F, AVX512_SKX... ne change rien : dans numpy 2.4.4 le niveau se
      nomme X86_V4. C'est donc le noyau SIMD AVX512 de l'ufunc power de numpy qui
      n'est pas CR ici ; que BOCAL4 passe par le pow de sa libm est ce que 4.4 mesure
      (jumeau CR = machine 2 au bit) et ce que la section 7 fait compter sur place.
  4.4 Le jumeau CR. Avec K1 CR seul, puis K1 + K2 + K3 CR, le jumeau rend :
        pas     e jumeau CR               = e machine 2 ?   = e machine 1 ?   premier pas different / x_fin
        dt2     1.0481615698622637e-06    OUI, au bit       non               43 / +1 ulp
        dt2/2   7.986105272223979e-08     OUI, au bit       non               724 / +2 ulp
        dt2/4   1.8520748469025595e-08    OUI, au bit       non               1490 / -2 ulp
        dt2/8   1.6530853961382515e-08    OUI, au bit       OUI, au bit       aucun / 0
      Falsifieur (ii) non declenche : la plateforme de machine 2 est CR sur tout ce
      que ces flots appellent ; celle de machine 1 ne l'est pas sur les cas durs de
      4.2. L'ecart au bord, +1, +2, -2, 0 ulp de x1, est celui que machine 2 a mesure.
  4.5 Chaque cas dur K1, corrige SEUL, et son effet sur x1 + x2 a tau_CAP :
        dt2    : 83 corrections une a une : 83 ABSORBEES (aucune ne bascule seule) ;
                 toutes ensemble : premier pas different 43, +1 ulp -- une COMBINAISON
                 de perturbations absorbees bascule l'arrondi de l'etat au pas 43.
        dt2/2  : 161 corrections : 160 absorbees, UNE bascule -- appel 2827, pas 707 sur
                 760, etage 3, x = 1765.6704444885254 = 0x1.b96ae89000000p+10, numpy
                 0x1.a483018a169c5p+64, CR 0x1.a483018a169c6p+64 : +2 ulp a elle seule,
                 soit TOUT l'ecart 0.759 / 0.684.
        dt2/4  : 316 corrections : 314 absorbees, DEUX basculent -- appel 5911 (pas 1478,
                 etage 3, x = 2476.68302154541) : -2 ulp ; appel 6003 (pas 1501, etage 3,
                 x = 2924.983688354492) : -6 ulp seule ; ensemble -2 ulp (non additif :
                 la seconde agit sur un etat deja deplace).
        dt2/8  : 633 corrections une a une : 633 ABSORBEES ; toutes ensemble : IDENTIQUE.
      (Les entrees x = x1 + x2 portent 28 bits significatifs -- la compensation efface
      les autres -- d'ou les mantisses a zeros ; c'est sur ces entrees courtes que le
      noyau se trompe d'un ulp.)
  4.6 Le rejeu du script du geste sans X86_V4 (sorties jointes, non editees) : les 44
      grandeurs de flot (11 par pas : e, R, plancher, ratio, tau_au_max, err_fin, R au
      max, n_pas, tau_fin, e/plancher, seuil) sont IDENTIQUES AU BIT a celles de
      machine 2 ; e/seuil a la paire du gel = 0.6841917055569781, son nombre. Seule
      difference dans tout le lot : p_obs a la paire (dt2/2, dt2/4), 2.108349686957736
      ici contre 2.1083496869577365 chez elle, sur des e IDENTIQUES : un ulp de log2,
      glibc contre UCRT -- une grandeur de LECTURE, jamais comparee au bit.

5. LA LECTURE (classe 3) -- CE QUI REMPLACE LA 4.3
  5.1 LA CAUSE, NOMMEE ET REPRODUITE. Sur machine 1 (Linux, Xeon AVX512, numpy 2.4.4,
      niveau de dispatch X86_V4 actif), (x1 + x2) ** (p - 1) est calcule par le noyau
      SIMD AVX512 de l'ufunc power, non correctement arrondi sur 5 pour cent des
      appels (biais -1 ulp) ; sur machine 2 (Windows, numpy 2.2.6, pas de noyau
      SVML) par le pow de la libm, correctement arrondi sur tous les appels de ces
      flots. C'est une difference de LOGICIEL (le noyau de numpy) et de MATERIEL (il
      ne s'active que sur AVX512), pas d'OS ni de version de Python ; elle est
      deterministe des deux cotes, comme machine 2 l'a mesure.
  5.2 POURQUOI 1, 2, 2, 0 ET NON UNE COURBE. Un appel mal arrondi deplace base d'un
      ulp ; dans l'etat cela pese ~ dt x base / (6 delta), tres en dessous d'un demi-ulp
      de v1 ou x1 : la perturbation est ABSORBEE par l'arrondi de l'etat, sauf quand la
      valeur exacte tombe pres d'une frontiere d'arrondi, et alors le dernier bit
      BASCULE et le deplacement (1 ulp de composante) se propage jusqu'au bord. Le
      nombre de basculements par flot est un petit entier fixe par les valeurs
      rencontrees : 1 (combinaison), 1, 2, 0. Lecture, non derivee : la chance de
      basculer par appel decroit comme dt tandis que le nombre d'appels croit comme
      1/dt ; rien ne fait tendre le compte vers zero quand dt diminue. Le zero a dt2/8
      est un FAIT de ce flot, verifie 633 fois une a une et une fois toutes ensemble,
      pas une loi : la question de machine 2 -- "pourquoi l'ecart s'annule-t-il au pas
      fin ?" -- a pour reponse "parce qu'aucun des 633 appels mal arrondis de ce flot ne
      tombe sur une frontiere d'arrondi de l'etat", et pour portee ce flot seul.
  5.3 CE QUE CELA CHANGE POUR LE GESTE (2) : rien au verdict, tout a l'explication. La
      valeur 0.759 de machine 1 (28/08 et 12/09) est la valeur du noyau AVX512 ; la
      valeur 0.684 est celle du pow correctement arrondi, que machine 1 rend aussi des
      que le noyau est desactive. Le point 7|1.73 est NON LU par le gel 5.4 des deux
      cotes ; la "non-reproduction au bit" est comprise, nommee, et reproduite dans les
      deux sens.
  5.4 CE QUI EST DERIVE, MESURE, ET RESTE A m2. DERIVE : rien de neuf (l'echelle de
      l'ulp de composante, 0.334 plancher, vient de R). MESURE ICI : les cas durs, les
      basculements, l'egalite au bit du jumeau CR avec machine 2, l'egalite au bit
      44/44 du rejeu sans X86_V4. RESTE A m2 : le compte des cas durs SUR SON POSTE
      (section 7) -- attendu zero ou presque ; c'est la derniere piece.

6. CE QUE CELA DIT DE LA CHAINE, ET CE QUI EST A ARBITRER (rien n'est decide ici)
  R-G2-5  Tout ** de TABLEAU numpy des instruments de la campagne (moteur compris,
          non examine) rend sur la plateforme machine 1 des doubles non CR sur ~5 pour
          cent des appels, et des doubles CR (libm) sur BOCAL4 ; les reproductions au
          bit obtenues jusqu'ici entre les deux machines sont donc des flots ou aucun
          basculement n'est survenu, ou qui ne passent pas par cette voie -- a
          examiner par un grep des ** sur tableaux, hors bloc. La ligne du protocole
          "numpy pow non symetrique au dernier ulp, dependant de la machine" a
          maintenant son mecanisme.
  Levier (a arbitrer, non joue) : NPY_DISABLE_CPU_FEATURES="X86_V4 AVX512_ICL
          AVX512_SPR" dans l'environnement de machine 1 (noms de niveaux de numpy
          2.4.4, lus dans numpy.show_runtime ; d'autres versions nomment leurs niveaux
          autrement, a lire au meme endroit) rend le ** de tableau au pow de glibc, et
          ici machine 1 = machine 2 au bit sur 44/44. Aucun code n'est edite
          (PB-1) ; mais glibc a ses propres cas durs (8/1193 sur les entrees dures,
          0.1 pour cent en general) et UCRT peut avoir les siens : l'egalite au bit
          entre libm reste un fait a mesurer, pas une garantie. A degre entier, un
          produit explicite serait IEEE-elementaire des deux cotes (identique, non CR)
          -- c'est un changement d'instrument, pas d'environnement, et il n'est pas
          propose ici.
  Regle candidate (sous (X), a arbitrer) : la ligne de plateforme d'un log nomme le
          niveau de dispatch numpy actif ('found' de numpy.show_runtime) a cote des
          versions -- deux postes de meme numpy et de meme OS different au bit selon
          que le CPU a AVX512 ou non.
  Regle prise (machine 2, 5) : une garde lit la ligne 'colonnes :' du manifeste.
  Intacts : R-G2-2 (les trois autres points NON LUS), R-G2-3 (le facteur du plateau),
          R-G2-4 (la tenaille). Rien sur alpha.

7. LECTURE m2 DEMANDEE (classe 3, aucune porte) -- LA DERNIERE PIECE
  Depuis la racine du clone, Git Bash :
    python diagnostic_pow_cas_durs_machine1_v1.py \
      --instrument <lot a4c35a2e>/banc_qualification_machine1_v8.py \
      --temoin <lot a4c35a2e>/temoin_negatif_pre_enregistrement_v11.md \
      --rejeu-m2 <lot 2b155abf>/convergence_dt_7_1p73_machine1_v1.json --sortie <vide>
  (--rejeu-m2 recoit MON JSON du geste, c8d86e5e5b4fd745, canon 2b155abffbe4f6ff :
  le script compare le poste qui le joue a ce JSON ; ses etiquettes m1/m2 sont "ce
  poste" / "le JSON passe".) Attendu, ecrit avant : jumeau bit-fidele aux quatre pas ;
  cas durs K1 sur BOCAL4 : 0 (quelques unites tolerables, si aucune ne bascule) ; jumeau
  CR egal au poste aux quatre pas ; egal a mon JSON a dt2/8 seulement ; ligne VERDICT
  "CAUSE DE L'AUTRE COTE" (c'est la lecture correcte vue de BOCAL4). ISSUE QUI MORD :
  des centaines de cas durs K1 sur BOCAL4, ou un jumeau CR different du poste -- alors
  UCRT n'est pas CR non plus et l'egalite au bit de 4.4 serait une coincidence a
  expliquer. Une ligne de plus, sans cout : numpy.show_runtime() sur BOCAL4, pour
  consigner son niveau de dispatch.
  Le diagnostic dure 44 s ici (Decimal) ; sur BOCAL4 compter une a deux minutes.

8. SUITE
  Rien n'est ouvert pour machine 1 sur ce geste au-dela de la lecture m2 de la section
  7. L'acte constante A (v5, cinq decisions, tenaille) reste le chantier suivant, en
  chat neuf, avec le v5 dans le lot ; cette note et la v1 sont deux de ses pieces, et
  R-G2-5 avec le levier et la regle candidate vont a l'operateur pour arbitrage.

-- FIN note_machine1_cause_ecart_7_1p73_v1 --
