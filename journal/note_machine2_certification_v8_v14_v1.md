# CERTIFICATION MACHINE 2 DU GEL constante A v8 ET DE L'INSTRUMENT v14
# machine 2, v1, 2026-09-18. Classe B (elle arme E19). Entrant : lot machine 1 b87f7a97f6477449,
# 11/11 au canon ; lot 588abe7cd9c6f6bd et lot ff42b9a8588cd7aa (Q5 rejoue), 5/5 chacun.
# Feuille : certif_v8_v14_machine2_v2.py a714d474af0abc04, log 7c7227ddeeac2ae3 -- 62 controles,
# 52 passent, 10 mordent. PB-1 : rien d'edite ; le v7 et le v13 sont intacts chez moi.

## 0. VERDICT

**LE GEL v8 N'EST PAS CERTIFIE EN L'ETAT. L'INSTRUMENT v14 L'EST, sous la reserve unique qu'il
n'implemente pas ce que la section 5bis du gel annonce.** Cinq reprises nommees ci-dessous ;
deux sont de FOND (R-v8-1, R-v8-2) et commandent une v9 (PB-1 : le v8 ne s'edite pas). Aucun run
n'est opposable avant cette v9 et sa certification (E19). Rien dans ce qui mord ne met en cause
la derivation du second ordre, ni Q5, ni le choix de n = 18.

## 1. CE QUI PASSE, ET QUI EST SOLIDE (52 controles)

  PROVENANCE. J'ai rejoue `construction_gel_v8_banc_v14_machine1_v1.py` sur MES copies du v7
  (a2b8463372e1f906) et du v13 (1ac295648490a86c) : le gel v8 (800fc6a9a8e56e49) et le banc v14
  (dc91676c640d4323) se reconstruisent **IDENTIQUES AU BIT**, canon B et brut. 39 hunks, 32
  remplacements. Cela etablit la provenance, pas la justesse : le reste est re-derive.

  LE REGLAGE, RE-DERIVE PAR MES FORMULES (jamais par son script) : delta' = 1/32400 exact ;
  levier 1/324 ; kT = 1.8601 (>= 1.15, la clause (T) n'est pas relachee) ; m = 1.1202 ;
  SUP(1) = 3.457292925e-05 ; les trois planchers exacts (1/648000, 1/468000, 1/344736), leurs
  decimales et leurs rapports a disp_85 ; les douze nombres de 4.3 ; les neuf bascules 2b et les
  neuf CAP' ; le controle de debordement 1.381e+26 ; n_2a = 340 ; le signal L-desc 3.0864e-03.
  **Tout concorde au chiffre imprime.**

  LA SECTION 5bis, CONTRE MA PROPRE DERIVATION : les trois rapports c1 tau_dom'^2 / plancher
  (1/3, 65/261, 133/795) en exact ; Re beta = 7/2, 17/6, 23/10 en exact ; les trois frequences ;
  le levier 441/324 ; le transport amplitude x 1.4255 et phase -0.4465 rad. La base des modes
  libres, rejouee chez moi par sa feuille sur mes series (75/75), rend les memes S que Q5 au
  chiffre et la table du gel a **2.0e-16 absolu** (un nombre sur 24 differe au 7e chiffre : c'est
  l'ulp ; la table se cite donc AVEC SA TOLERANCE, pas comme un chiffre exact -- et le CANON de
  la base, lui, est machine-dependant : ma base rend 0a7d411197d0603d, la sienne 79099ef4ea51adf6).

  L'INSTRUMENT v14 SUR BOCAL4 : selftest **103/103** (b3be375fb9d1d5f0) ; banc qui tue **56/56**,
  gardes enumerees des gels **17, demontrees 17** (e40ac1870f8c718a) ; pin GEL_ALPHA portant
  chemin, canon ET taille du v8. **PRE-VOL TEMOIN : REGLAGE QUALIFIE, branche 5** (c69d1b85cb271303),
  marge minimale e/seuil = 1.868 au point 7|1.73, tres au-dessus du 1.15 exige -- **la condition
  que le gel posait ("BOCAL4 a jouer avant tout run") est donc levee a n = 18** ; pre-vol alpha
  branche 5, LIEN NON ETABLI (9/27) comme chez elle (3e9327019295afb6). Mes quatre journaux
  concordent avec les siens hors ligne de plateforme.

  (Mes deux premiers faux echecs, retires AVANT emission et declares : la v1 de ma feuille
  127c766817486e0d cherchait le pin sous un nom qu'il n'a pas, et comparait la table au chiffre
  imprime au lieu d'une tolerance. Corriger une attente FAUSSE est legitime ; je le dis pour que
  la v1 ne circule pas.)

## 2. R-v8-1 (FOND) -- LA PORTE DU PLANCHER REND LE RUN MUET AVANT TOUTE LECTURE

La section 7 est INCHANGEE : G-plancher MORD au degre p si tol_lnA(p) <= plancher_lnA(p), et la
branche 3b est lue AVANT P-A. Or tol_lnA reste, dans l'instrument, `max(dispersion LD-12,
plancher)`. Je transporte a n = 18 la dispersion que le run 91 a **MESUREE** (9.853e-07 /
3.261e-07 / 8.916e-08), par les deux seules lois dont on dispose :

    loi de transport                    p = 4              p = 5              p = 7
    pente mesuree 85 -> 91              1.021e-06  MORD    3.607e-07  MORD    1.115e-07  MORD
    troncature en dt^4 (delta'^2)       1.825e-06  passe   6.041e-07  MORD    1.652e-07  MORD
    plancher' a n = 18                  1.543e-06          2.137e-06          2.901e-06

**Sous les deux lois, il ne reste pas trois degres exploitables : la cascade rend NON CONCLUANT
DE PLANCHER, comme au 91, avant d'avoir rien lu de 5bis.** L'attendu que le gel imprime en 7
(1.28 / 1.12 / 2.56) est calcule sur les dispersions du **85**, soit 2.0 / 7.3 / 83.4 fois celles
que le 91 a mesurees : c'est un attendu ancre sur une grandeur que le run precedent a deja
refutee. Et la cascade 3.5, non reprise, parle encore du "reglage v6" et d'un "v10" : elle ne dit
pas ce qu'on fait quand 3b mord de nouveau.

**Ce que je propose (ta plume) : la voie courte.** La feuille de lecture, elle, ne consulte
aucune branche : elle lit le JSON et les series. Il suffit que le gel l'ECRIVE -- (i) que la
branche 3b ne suspend PAS la feuille ; (ii) que P-A reste, a ce run, la P-A du v7 (non corrigee,
probablement non concluante de plancher) et que le TEST du run soit les deux predictions ; ou
alors (iii) rendre le plancher lui-meme au terme qu'il doit borner (apres soustraction de c1, ce
n'est plus delta'/((a+2)(a+3))), ce qui est le vrai chantier et ne se fait pas a la main.

## 3. R-v8-2 (FOND) -- 5bis ANNONCE UNE P-A QUE RIEN N'IMPLEMENTE

5bis ecrit : *"la lecture P-A reste celle de 10.3, a deux regimes : instrument-limite a p = 4 et
5 -- tolerance S(p) + residu de Richardson --, et a p = 7 sous M2"*. Or, au texte du v14 :

    D["P_A"] = all(abs(math.log(v)) <= (p - 2) * D["tol_lnA"] for v in ratios.values())

les `ratios` sont les `gA_II_sur_K` de l'ajustement II **non corrige**, et `tol_lnA` est
`max(dispersion, plancher)`. Ni S(p), ni le residu de Richardson, ni M1/M2 n'entrent dans la P-A
que l'instrument ecrit ; les modeles vivent dans la feuille, hors cascade. **Le gel promet donc
une lecture que le run ne rendra pas.** Deux issues : l'ecrire tel que c'est construit (la P-A du
run est celle du v7 ; la lecture corrigee est une CONSIGNE de la feuille, sans verdict), ou porter
la P-A corrigee dans l'instrument -- ce qui fait un v15 et une certification de plus.

## 4. R-v8-3 (COMPTE) -- LE GEL DIT 90, L'INSTRUMENT DERIVE 108

Section 11 enumere encore "plan 18, G_dt 18, G_k 18, G_seuil 9, G_lignee 27 ; comptes + sautes
== 90". L'instrument v14 derive `{"plan", "G_dt", "G_k", "G_dt4", "G_seuil", "G_lignee"}`, soit
**108**. La garde G-comptes ne mordra pas (elle lit la forme derivee), mais le gel declare 18
trajectoires de moins que ce que le run jouera, et le quatrieme etage n'est nomme nulle part dans
ses comptes. Un compte inscrit se compte.

## 5. R-v8-4 (REGLE 13) -- TROIS NOMBRES TAPES LA OU ILS SE DERIVENT

`construction_gel_v8...py` et `lecture_v8_machine1_v1.py` portent `BIAIS_91 = {4: 2.5425e-07,
5: 2.6302e-07, 7: 2.3986e-07}` : ce sont MES biais du dossier C4 **arrondis a la main a %.4e**
(vrais : 2.542476e-07, 2.630167e-07, 2.398576e-07). Les predictions du gel en heritent : a p = 5
il imprime 3.5800e-07 quand la re-derivation donne 3.5799e-07, a p = 7 3.2648e-07 contre
3.2647e-07. **L'ecart est de 1.4e-05 et 2.2e-05 en relatif, sans aucune portee** devant la
tolerance de 20 pour cent -- mais la regle 13 dit qu'un nombre derivable ne se tape pas, et le
JSON de la derivation est deja en argument de la construction.

## 6. R-v8-5 (FORME) -- UN SEPARATEUR COLLE A SON TITRE

Ligne 465 : `===...===5bis. LES MODELES D'AJUSTEMENT...` -- la ligne de separation et le titre
sont concatenes. Toute extraction de section s'ancre sur la structure (delimiteur en colonne 0) ;
ce gel a desormais une section que ce chemin-la ne trouve pas. Rien d'autre n'est touche : la
ligne FIN figure une fois, et l'en-tete est bien forme.

## 6bis. LES DIX MORSURES, NOMMEES, ET LA REPRISE QUI LES COUVRE

    controle qui mord (nom exact au log 7c7227ddeeac2ae3)                       reprise
    4.1 : sous au moins une loi de transport il reste TROIS degres non mordus    R-v8-1
    4.3 : la P-A de l instrument lit la tolerance de 5bis (S + residu de Richardson)  R-v8-2
    4.4 : la P-A de l instrument lit le lnA CORRIGE (M1/M2)                      R-v8-2
    4.5 : la cascade de l instrument connait les modeles de 5bis                 R-v8-2
    gel 11 : le compte ECRIT au gel egale celui que l instrument derive          R-v8-3
    gel 11 : le quatrieme etage est NOMME dans les comptes du gel                R-v8-3
    5bis (a) p=5 : et elle est RE-DERIVEE, non arrondie a la main                R-v8-4
    5bis (a) p=7 : et elle est RE-DERIVEE, non arrondie a la main                R-v8-4
    5bis (a) : la feuille RE-DERIVE le biais du 91 au lieu de le taper           R-v8-4
    5.1 : aucun separateur de section colle a son titre                          R-v8-5

Aucune morsure n'est laissee sans reprise ; aucune reprise ne couvre autre chose que ce qui
mord. Le controle 4.5 est un test de STRUCTURE (il cherche les modeles dans le texte de
l'instrument) : il dit la meme chose que 4.3 et 4.4, par un autre chemin.

## 7. CE QUE CETTE CERTIFICATION NE DIT PAS

Elle ne juge ni la derivation du second ordre (la mienne, rejouee par machine 1 au bit), ni Q5
(rejoue sur les deux arithmetiques), ni le choix de n = 18, qui est un arbitrage de l'operateur
et que le pre-vol BOCAL4 confirme ouvrable. Elle ne prend aucun numero (E18 ; max cite inchange).
Elle n'autorise aucun run : E19 demande une v9 certifiee. Elle ne mesure pas A.

## 8. PIECES (convention B, re-derivees le 2026-09-18 depuis D:\devs\bocal\BOCAL4)

    certif_v8_v14_machine2_v2.py                  a714d474af0abc04   15512
    certif_v8_v14_machine2_v2.log                 7c7227ddeeac2ae3   10131
    certif_v8_v14_machine2_v2.json                b398c344c1b94c31    1239
    certif_v8_v14_machine2_v1.log (faux echecs, conservee)  127c766817486e0d    9715
    m2_v14_selftest.log                           b3be375fb9d1d5f0   11475
    m2_v14_banc.log                               e40ac1870f8c718a   25048
    m2_v14_prevol_temoin.log                      c69d1b85cb271303   17845
    m2_v14_prevol_alpha.log                       3e9327019295afb6   34059
    m2_base_modes_libres_n21_v1.json              0a7d411197d0603d    5884
    m2_lecture_v8_base_n21.log                    072cf6edf90f3e6e    9192
    entrants : gel v8 800fc6a9a8e56e49 ; banc v14 dc91676c640d4323 ; construction faf29c378ab88dda ;
    feuille 4f1679c48f68aa6f ; base m1 79099ef4ea51adf6 ; v7 a2b8463372e1f906 ; v13 1ac295648490a86c ;
    clone frais 729f9a9 (le gel v8 y a ete place pour le pre-vol : il n'est pas depose).

-- FIN note_machine2_certification_v8_v14_v1 --
