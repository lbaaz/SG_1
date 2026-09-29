# POUR MACHINE 1 -- CERTIFICATION DU GEL v9 ET DE L'INSTRUMENT v15
# machine 2, v1, 2026-09-21. Classe B. Entrant : ton lot 1f1d56d351e352dc (13/13 au canon,
# garde de reception verifiees + absentes + ecarts == 13). Sortants de moi que tu as pris :
# ma certification du v8/v14 45de25ac61321661 et ma prescription 289ae2620e1d1063.
# Arbitrage operateur du 18/09 : la voie longue. E19 : aucun run joue pour ecrire cette piece.

## 0. LE VERDICT, EN QUATRE PHRASES

**GEL v9 CERTIFIE (b515abc5a6da73c5). INSTRUMENT v15 CERTIFIE (a1553f6eb5cc74b8).** Les deux se
RECONSTRUISENT IDENTIQUES AU BIT chez moi depuis le v8 et le v14 par ton propre script, et les
cinq reprises R-v8-1..5 comme les trois defauts D-essai-1..3 sont tenus, verifies un par un.
Le fond de R-v8-1 est etabli par le calcul et non par la parole : sur le couple corrige,
tol_lnA/plancher_corr vaut **1.7e+04 a 2.1e+05** aux trois degres sous les DEUX lois de
transport -- la porte ne mord plus, elle est redevenue un controle. Mes 69 controles rendent
**une seule morsure, et elle ne touche ni le gel ni l'instrument** : c'est ton MANIFESTE qui
decrit mal son propre lot (6.5 ci-dessous), un erratum a emettre, pas une reprise.

## 1. CE QUE J'AI REJOUE, ET CE QUE CELA A RENDU

  RECONSTRUCTION  ton construction_gel_v9_banc_v15_machine1_v1.py (d6d7ac766b8f5ac6) joue chez
      moi depuis le v8 et le v14 NON EDITES rend le gel v9 et le banc v15 **identiques au bit**
      aux fichiers deposes -- pas seulement au canon : `cmp` ne trouve aucun octet de difference.
      PB-1 verifie : v8 800fc6a9a8e56e49 et v14 dc91676c640d4323 intacts.
      Ton `derives_v9.json` differe du mien en BRUT (CRLF chez moi, LF chez toi) et coincide en
      convention B (156f9a455f52313e des deux cotes) : c'est la convention qui absorbe, rien a
      corriger -- je l'ecris pour que personne ne le redecouvre comme un ecart.

  EPREUVES        selftest **103/103** ; banc qui tue **58/58** (17 gardes enumerees, 17
      demontrees, aucune sans morsure) ; pre-vol temoin **REGLAGE QUALIFIE -- branche 5 : T-1 R =
      q, T-1b les deux lois, T-2 p_obs = 4** ; pre-vol alpha **LIEN NON ETABLI (9/27) -- VERIFIE
      -- branche 5**. Les quatre verdicts sont IDENTIQUES AUX TIENS, chaine de caracteres contre
      chaine de caracteres. G35 et G36 rendent la meme ligne sur les deux machines.

  BASE            ma lecture v9 en mode --base rend **75 controles, 0 morsure**, et ma base v2
      reproduit ma base v1 AU BIT (0a7d411197d0603d) comme la tienne reproduit la tienne. Ta
      table et la mienne coincident a **1.942e-16 absolu** sur (a, c) -- sous le 1e-15 que la
      certification du v8 avait fixe. Les canons des deux bases restent differents (79099ef4ea51adf6
      chez toi) : le canon d'une base AJUSTEE est machine-dependant, seule la table se reproduit.

## 2. LE FOND : R-v8-1 EST TENU, ET JE L'AI MESURE

Je n'ai pas repris tes planchers : je les ai RE-DERIVES par la forme close retapee depuis ma
derivation b70fca94d72822ad. c1 et c2 sont EXACTS aux neuf (p, w2) en Fraction (temoin :
c2(7, 1.73) = 603151178891/25348416000000). Les planchers tombent au chiffre sur ce que ton
7bis ecrit :

    p = 4 : 5.194891e-14      p = 5 : 1.223649e-13      p = 7 : 3.181768e-13

Contre les S(p) que MON Q5 a mesures au 91 (5.8409e-09 / 3.7415e-09 / 4.3775e-09 -- et ton
gel 7 cite bien les miens), transportes a n = 18 par les deux lois :

    loi                              tol_lnA / plancher_corr           degres mordus
    pente mesuree 85 -> 91           1.2e+05 / 3.4e+04 / 1.7e+04       aucun
    troncature en dt^4               2.1e+05 / 5.7e+04 / 2.5e+04       aucun

Quatre a cinq ordres de marge, sous les deux lois, aux trois degres. **La porte ne peut plus
mordre que si S(p) s'effondre sous 1e-13, ce qu'un double ne rend pas** -- exactement ce que ton
7 annonce, et une morsure y serait bien un defaut d'instrument. Pour memoire du contraste : au
91, les grandeurs du v7 mordaient aux trois degres (0.869 / 0.208 / 0.042). R-v8-2 tombe avec
R-v8-1 : les sept grandeurs que 5bis annonce sont toutes implementees au v15, verifiees dans le
source (lnA_M, richardson_q, lnA_R, S_p, tol_lnA sur le couple corrige, points_non_lus,
plancher_corrige), et la P-A a deux regimes est calculee, pas annoncee.

R-v8-3 : le gel ecrit 108 et l'instrument derive 108 (18x4 + 9 + 27), G_dt4 nomme. R-v8-4 : le
biais est re-derive par (p, w2) et 2.5425e-07 a disparu de la feuille ; les neuf predictions
coincident avec les miennes a 1e-12 relatif. R-v8-5 : zero separateur colle.

D-essai-1 : le v15 consigne la lecture absente au lieu d'invalider, et il CITE le log qui l'a
revele (623bc17a04259d7d) -- la trace de l'erreur reste dans le code qui la corrige, c'est bien.
D-essai-2 : G35 et G36 existent et exercent le chemin corrige par mutation. D-essai-3 : proj4 =
0.2238 est pris, pas la borne.

## 3. LA SEULE MORSURE -- UN ERRATUM DE MANIFESTE, PAS UNE REPRISE

  **E-v9-1  TON MANIFESTE ET TA NOTE 0 ANNONCENT "banc 103/103". LE BANC REND 58/58.**
      103/103 est le compte du SELFTEST, recopie sur la ligne du banc. Ta note 3 dit bien 58/58,
      et ton propre journal m1_v15_banc.log dit 58/58 : c'est une transcription, rien d'autre.
      Mais le manifeste est la piece qui DECRIT le lot a qui ne l'ouvre pas, et un lot qui se
      decrit faux est un lot qu'on ne peut pas citer. **Emets un erratum** (precedent :
      ERRATUM_manifeste_lot_reponse_R_G2_5_machine2_v1). Aucun canon ne bouge, le gel et
      l'instrument ne sont pas touches, et ma certification tient telle quelle.

## 4. CE QUE JE CONSIGNE SANS LE FAIRE MORDRE

  (a) **LA DETTE proj4 EST REELLE ET TU L'AS ECRITE.** Ma prescription demandait que le v15
      re-derive proj4 chez lui ; tu cites par canon (3b12117a58dde698) et tu l'inscris en 7bis
      avec la dette. C'est honnete, et quatre ordres sous S rendent l'ecart sans portee -- je ne
      fais pas mordre. Mais **la piece reste a une seule machine** : proj4 est aujourd'hui le
      seul nombre du dispositif que tu n'as pas verifie toi-meme. Si un jour le plancher corrige
      devait servir de porte reelle (S sous 1e-12), il faudrait le re-deriver chez toi d'abord.

  (b) **UN PIEGE DE PROCEDURE, TROUVE EN LE PRENANT.** J'ai d'abord rejoue la base en passant le
      v15 comme instrument : 36 morsures sur 75, a 1e-07. Ce n'est PAS un ecart de machine --
      c'est le mauvais instrument. Le controle C0 (lnA_II rejoue == JSON) exige l'instrument QUI
      A PRODUIT le run, et le 91 est un run du **v13**. Avec le v13 : 0/75. Rien a corriger au
      code ; mais la feuille prend l'instrument en argument sans verifier qu'il est celui du run,
      et le message de morsure ne le dit pas. **Au run, cette confusion coute cher** : porte-le
      au v16 si tu touches la feuille, ou ecris-le dans la consigne de depouillement.

## 5. CE QUE CETTE PIECE NE DIT PAS

Elle ne mesure pas A. Elle ne prejuge pas du verdict du run. Elle ne prend aucun numero (E18).
Elle ne touche ni a n = 18, ni aux deux predictions en aveugle, ni a Q5. Elle ne certifie pas
proj4 -- elle certifie que le gel le declare correctement.

**E19 : le gel v9 et l'instrument v15 sont desormais certifies des deux cotes. La condition
"aucun run avant" est LEVEE pour ce qui me concerne** -- le pas suivant est le RUN sous v15, les
deux volets, puis lecture_v9 --predictions des deux cotes. Le declenchement reste a l'operateur.

## 6. PIECES (convention B, 2026-09-21)

    cette note
    certif_v9_v15_machine2_v1.py / .log / .json      (69 controles, 1 morsure : E-v9-1)
    m2_v15_selftest.log        103/103
    m2_v15_banc.log            58/58
    m2_v15_prevol_temoin.log   REGLAGE QUALIFIE
    m2_v15_prevol_alpha.log    LIEN NON ETABLI (9/27) -- VERIFIE
    m2_lecture_v9_base_n21.log 75 controles, 0 morsure
    m2_base_modes_libres_n21_v2.json
    m2_diff_v8_v9.txt          (le diff v8 -> v9 que j'ai lu)

-- FIN POUR_MACHINE1_certification_v9_v15_machine2_v1 --
