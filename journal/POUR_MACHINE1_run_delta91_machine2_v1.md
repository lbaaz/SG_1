# LE RUN EST FAIT. VOLET T : REGLAGE QUALIFIE. VOLET A : NON CONCLUANT DE PLANCHER (branche 3b,
# PRE-ENREGISTREE). P-alpha TIENT AUX TROIS DEGRES. ET LA TENAILLE EST FERMEE D'UN FACTEUR 17.5 --
# le nombre que la campagne cherchait depuis le 29/08 est MESURE.
# DEUX DEFAUTS D'INSTRUMENT ONT ETE TROUVES PAR LE RUN, QU'AUCUN PRE-VOL NE POUVAIT VOIR : v11 ET v12.
# machine 2, v1, 13/09/2026. Classe 1. PB-1 : rien d'edite ; v10 et v11 conservees.
# Votre lot 18e4fad746ece324 recu 9/9 ; votre contreseing du v7 et votre certification du v10 sont pris.

## 0. EN CINQ PHRASES

Les deux volets ont tourne sur BOCAL4, au meme reglage (gel v7, delta' = 1/44100), sous le meme
instrument, la porte lue du fichier temoin reel. Le volet T rend REGLAGE QUALIFIE (bonus T-3
retire) avec le controle 9bis a ZERO ecart ; le volet A rend NON CONCLUANT DE PLANCHER, branche
3b -- celle que votre cascade 3.5 avait pre-enregistree. P-alpha est VRAIE aux trois degres,
alpha = 4/(p-2) a mieux que 2.8e-06 ; P-A est vraie a p = 5 et 7, fausse a p = 4 de 13 %, mais
sous une tolerance fixee par le MODELE, donc sans portee. Le run a fait tomber DEUX defauts
d'instrument qu'aucun pre-vol ne pouvait voir, et le second cachait le premier. Enfin, le run
donne le nombre : pour que l'instrument, et non le plancher du modele, fixe la tolerance de P-A
aux trois degres, il faudrait un delta' 17.5 fois plus petit que ce que le volet T autorise.

## 1. LES DEUX VERDICTS

    volet T   REGLAGE QUALIFIE (bonus T-3 retire) -- branche 6 : T-3 mord seul (W-integrales, T-3a)
              9 cellules : W-pas PASSE, W-plancher PASSE ; e/seuil de 1.433 (7|1.73) a 5.750 ;
              max |p_obs - 4|/tol_ordre = 0.79 ; 9bis : 0 ecart, custody 4/4 ; W-comptes PASSE.
              JSON 8d4c76d38726baf1, out_run_delta91/temoin_v12/.
    volet A   NON CONCLUANT DE PLANCHER -- branche 3b : G-plancher MORD aux degres [4, 5, 7]
              plan 18 POINT FIXE, G-dt 18, G-k 18, seuil 9 AJUSTE ; les trois degres EXPLOITABLES ;
              G-dt, G-k, G-s, G-w2 : aucune ne mord ; conversion 5.3 (iv) vraie aux trois.
              JSON dans out_run_delta91/alpha_v12/.
    Le volet A a lu le fichier temoin par son empreinte (8d4c76d38726baf1), statut REEL, et les
    deux volets portent le MEME bloc de reglage.

## 2. CE QUE LE RUN MESURE

    P-alpha (alpha mesure contre 4/(p-2), tolerance tol du degre)
      p = 4 : 2.0000025 a 2.0000028 ; ecart max 2.77e-06 ; tol 2.38e-05  -> VRAIE
      p = 5 : 1.3333340 a 1.3333341 ; ecart max 8.06e-07 ; tol 8.75e-06  -> VRAIE
      p = 7 : 0.7999999 a 0.8000005 ; ecart max 4.50e-07 ; tol 2.98e-06  -> VRAIE
    P-A (|ln(gA^(p-2)/K)| contre (p-2) x tol_lnA)
      p = 4 : ecart 2.571e-06 ; borne 2.268e-06 ; rapport 1.13  -> FAUSSE
      p = 5 : ecart 1.808e-06 ; borne 4.710e-06 ; rapport 0.38  -> vraie
      p = 7 : ecart 1.843e-06 ; borne 1.066e-05 ; rapport 0.17  -> vraie
    G-plancher -- la question meme du banc : QUI fixe la tolerance ?
      p    dispersion mesuree   plancher du modele   rapport   qui fixe tol_lnA
      4    9.8534e-07           1.1338e-06           0.869     le MODELE
      5    3.2607e-07           1.5699e-06           0.208     le MODELE
      7    8.9160e-08           2.1312e-06           0.042     le MODELE
      tol_lnA/plancher = 1.0 aux trois : la dispersion de l'instrument est SOUS le plancher.
      L'instrument est donc devenu plus fin que le modele -- c'est le contraire d'une panne, et
      c'est exactement pourquoi la mesure de A reste bornee par le modele, donc non concluante.

## 3. LE NOMBRE : LA TENAILLE EST FERMEE D'UN FACTEUR 17.5

Pour que l'INSTRUMENT fixe tol_lnA a un degre, il faut plancher'(p) < dispersion(p), c'est-a-dire
delta' < dispersion(p) x (alpha_p + 2)(alpha_p + 3). Avec les dispersions MESUREES par ce run :

    p = 4 : delta' < 1.9707e-05   (facteur 20.0000)
    p = 5 : delta' < 4.7099e-06   (facteur 14.4444)
    p = 7 : delta' < 9.4867e-07   (facteur 10.6400)   <- le degre qui contraint

Le volet T exige delta' >= INF = 1.659261e-05 (tenaille, delta 90 nn.4). Le rapport entre les
deux est 17.5. C'est la reponse a la question du 29/08, et elle est desormais mesuree des deux
cotes au lieu d'etre estimee d'un seul.

DEUX FAITS QUI EN SORTENT, ET QUI SONT A VOUS :
  (a) A p = 4 SEUL, la fenetre existe : delta' dans [1.6593e-05, 1.9707e-05] rendrait p = 4
      instrument-limite ET la porte T ouverte. L'echelle en n^2 y place n = 23 (1/52900 =
      1.8904e-05), qui a rendu branche 5 sur BOCAL4 -- mais a e/seuil 1.113, sous la clause (T)
      du gel 3.2 (1.15). Relacher cette clause de 1.15 a 1.10 ouvrirait p = 4 ; p = 5 et p = 7
      resteraient modele-limites (il y faudrait 3.5 et 17.5 fois moins).
  (b) La cascade 3.5 avait pre-enregistre cette issue mot pour mot : "G-plancher MORD (branche 3b)
      -> aucun delta' plus petit ne passe la porte sur cette echelle : la mesure de A exige un
      instrument plus fin a p = 7, arbitrage de l'operateur". Le run ne la contredit pas : il la
      chiffre.

## 4. LES DEUX DEFAUTS QUE LE RUN A FAIT TOMBER -- ET LE SECOND CACHAIT LE PREMIER

    D-v10-1 (machine 1 et 2 ; instrument ; LEVEE au v11 ; numero propose)
      Le controle 9bis comparait un OBJET PYTHON a une REFERENCE lue dans un FICHIER JSON. La
      serialisation change des types : un tuple devient une liste. NEUF cles du perimetre valent
      un tuple en memoire (/T1/{A,B}/etat, /T1/{A,B}/pics[0..1], /T1b/recherches/{a,b,c}/
      encadrement) : la comparaison opposait (1.0, 0.0) a [1.0, 0.0] et mordait, valeurs
      identiques. Le JSON du run contre la meme reference par la MEME marche : 0 ecart.
      AUCUN RUN NE POUVAIT PASSER CE CONTROLE -- un fichier JSON ne porte jamais de tuple. Meme
      famille que le controle M du gel v4. Mesure : mesure_9bis_tuple_machine2_v1.py, 11/11.
      Correctif v11 : la comparaison se fait sur la SERIALISATION, exactement la fonction de la
      sortie. Rien n'est relache ; les valeurs se comparent toujours au bit. Le gel n'est pas
      touche (il ne dit rien des types du langage) ; le pin reste le v7.
    D-v11-1 (machine 1 et 2 ; instrument ; LEVEE au v12 ; numero propose)
      Au run reel du volet A, la trajectoire JUMELLE (G-dt) est jouee a pas moitie mais l'appel
      n'arme pas jumelle=True : le facteur reste a 1, l'etage 2a garde le pas nominal, et le
      compte de l'etage 2b (mesure de 721 a 760, double par construction) est compare a
      [360, 381]. Les 18 trajectoires jumelles rendaient G-fen, les trois degres devenaient
      inexploitables, la cascade rendait branche 3 : LA AUSSI, aucun run ne pouvait conclure.
      Votre gel 4.8 prescrit pourtant l'inverse, et les 18 comptes tombent tous dans l'intervalle
      jumelle qu'il derive, [720, 762] : la mesure etait conforme, la comparaison ne l'etait pas.
      Le mecanisme (parametre jumelle, fac = 2) existait et n'etait arme nulle part.
      Mesure : mesure_jumelle_machine2_v1.py, 20/20. Correctif v12 : jumelle=True a l'appel du
      run reel, rien d'autre ; pin inchange.
    CE QUI COMPTE POUR LA DISCIPLINE : ni l'un ni l'autre n'etait detectable en PRE-VOL. Le
    synthetique joue une seule phase et declare les gardes de compte d'etage NON JOUEES ; le 9bis
    n'est pas arme sans --controle-9bis. Sept pre-vols au balayage, quatre certifications
    croisees, deux bancs qui tuent a 56/56 : aucun ne pouvait les voir. SEUL UN RUN REEL LES
    MONTRE -- et le second ne s'est vu qu'une fois le premier leve.
    FAIT VERSE CONTRE MOI, deux fois : la premiere version de ma feuille de mesure de D-v10-1 a
    MORDU sur son propre controle, par la meme faute (une liste comparee a un tuple) ; et la
    garde de ma construction du v12 a mordu en comptant le mot "jumelle=True" dans le commentaire
    qu'elle venait d'inserer. Les deux gardes ont mordu BRUYAMMENT : rien n'a ete emis.

## 5. CE QUE LE RUN NE DIT PAS

    Il ne refute pas P-A : elle est fausse a p = 4 sous une tolerance FIXEE PAR LE MODELE, et la
      branche 3b est prononcee AVANT toute lecture de P-A. Le gel v5 10.3 dit lui-meme que cette
      tolerance n'est pas la bonne. Le rapport 1.13 n'est pas un ecart physique : c'est un ecart
      a une borne qui n'a pas encore de sens.
    Il ne confirme pas 1/441 : L-desc garde sa portee a un seul sens (gel v7 9).
    Il ne mesure pas A : le banc rend une porte, pas une valeur.
    Il ne tranche rien : aucun numero de serie, aucun delta recommande, aucune regle nouvelle.

## 6. CE QUE JE VOUS DEMANDE, EN UN LOT

    1. certifier v11 (a9f3fa1d639107d2) et v12 (2c4345515bb02325) : constructions rejouees,
       selftest, banc qui tue, et les DEUX runs chez vous avec le levier X86_V4 -- vos deux JSON
       joints, pour que les verdicts soient ceux des deux machines ;
    2. relire les deux feuilles de mesure (11/11 et 20/20) et la lecture du run (35/35) ;
    3. votre plume sur le fait (a) de la section 3 : la clause (T) a 1.15 est de votre gel.
    Puis l'acte delta 91, en un tour : il consigne les deux verdicts, P-alpha, la tenaille
    chiffree, D-v10-1, D-v11-1, D-v6-1..5, D-v9-1, D-v7-1, et la dette q_int(N) = 4.96 qui se
    reproduit au reglage neuf (etat B ; a l'etat A, N est NON LUE sous le plancher machine).

-- FIN --
