# CERTIFICATION MACHINE 1 DU RUN DELTA 93 (RUN D'OBSERVATION SOUS v16 / GEL v10, n = 21) --
# REPRODUIT AU VERDICT ET AU NOMBRE ; (c) 18/18 ; A AUX DEUX REGLAGES ; MA PREDICTION (d) DU v11
# EST REFUTEE A p = 4 ET LE v11/v17 EST RETIRE AVANT CERTIFICATION
# machine 1, v1, 29/09/2026. Classe B. Entrant : lot m2 90a0b0ca445989ef, 12/12 au canon.

## 1. LE REJEU (v16 634c4aaa2aad7598, gel v10 130ba949482129a7 au registre local, clone 09baf5c, levier X86_V4)
    temoin   REGLAGE QUALIFIE (bonus T-3 retire) -- branche 6 ; 9bis 0 ecart, 7 toleres ; IDENTIQUE
    alpha    VERIFIE -- branche 5 : P-alpha les six par degre ET P-A aux trois degres ; IDENTIQUE
    lecture  139 controles, 1 morsure, la meme ((a) p = 7, cause connue) ; (a) TIENT p = 4, 5 ;
             (b) 6/6 ; (c) 18/18, rapports c1_R / c1_derive entre 0.9612 et 1.0370 chez moi
    lnA_R(II) : 15 des 18 identiques au bit entre machines, ecart maximal 4.2e-10 (p = 4)
    A(p)     48.989794873 / 9.650477146 / 3.142438763 (BOCAL4 : ...876 / ...146 / ...763 ;
             forme auto-semblable (K/g)^(1/(p-2)) : ...856 / ...151 / ...762) -- a 4e-10 relatif
    S(p) M1/M1/M2 : 2.49e-09 / 2.42e-09 / 4.92e-09 (BOCAL4 2.11e-09 / 2.42e-09 / 4.91e-09)
  Le run est certifie comme run d'OBSERVATION : E19 n'etait levee que d'un cote quand il a tourne
  (mon lot v11/v17 est arrive apres), l'operateur l'a lance "pour voir" ; ses predictions etaient
  pre-enregistrees dans un gel certifie par machine 2 et ecrit par machine 1, mais pas encore
  re-certifiees par moi -- je l'ecris tel quel, sans le masquer ni le plaider.

## 2. CE QU'IL DIT, ET QUI TIENT
  (c) est le resultat de la journee : le coefficient du terme tau^2, AJUSTE LIBREMENT, vaut le c1
  derive aux dix-huit points et aux trois degres, a 4 pour cent au pire (1.2 aux premiers points)
  quand la prediction en tolerait 10 -- p = 7 compris, la ou (a) tombe parce qu'elle projette le
  mode. Le premier ordre est mesure, pas seulement borne. Et A est mesuree aux deux reglages, 92
  et 93, aux trois degres, accordee a la forme auto-semblable a 4e-10 relatif, sous une borne
  S(p) de 2 a 5e-09 ; la regle du plus grand n a fait baisser S a p = 4 et 5 (x 0.47 / x 0.65)
  comme elle le promettait, et l'a fait monter a p = 7 (x 1.4), ou le mode domine.

## 3. CE QU'IL REFUTE -- CHEZ MACHINE 2 ET CHEZ MOI
  Machine 2 retire sa reserve de fond (le biais de fenetre a signe unique) et sa Q4 : je prends
  acte, et je lui rends la pareille. Mon gel v11 (ac398dc92badbdc5, lot c446e2b99e53d2a3) ecrivait
  S(p) comme un SYSTEMATIQUE DE FENETRE DETERMINISTE et pre-enregistrait (d) : "a n = 21, sous M1
  a p = 4 et 5, les six ecarts en c sont de meme signe, positif". Lu sur le 93 : p = 4 MELE
  (+7.8e-10, -2.5e-09, +1.2e-09), p = 5 meme signe, p = 7 mele. (d) est FAUSSE a p = 4 -- et elle
  n'etait pas opposable non plus : ecrite avant que je voie le 93, mais apres qu'il a tourne. Ce
  qui reste vrai du v11 est la borne (S + plancher_corr majore ce qu'on ne sait pas nommer) ; ce
  qui est faux est le nom que je donnais au residu, comme machine 2 avant moi. LE v11 ET LE v17
  SONT RETIRES avant certification ; le gel courant reste le v10, l'instrument le v16, tous deux
  certifies, et le 93 a tourne sous eux. Le residu de 2 a 5e-09 est sans structure connue ; ni
  M2 aux degres 4 et 5 (mesure au 92), ni un signe reproductible (93) ne le nomment.

## 4. CE QUE JE RECOMMANDE A L'OPERATEUR
  Ne pas rejouer un "run d'acte" a n = 21 : il ne serait plus en aveugle, et il ne rendrait rien
  que le 93 n'a pas rendu. Ecrire l'acte delta 93 comme un run d'OBSERVATION qui consigne : les
  quatre resultats, les deux refutations (la sienne, la mienne), l'irregularite d'E19 et son cout,
  A aux deux reglages. Puis fermer le chantier de la constante A sur ce que la campagne sait : A
  est celle de la forme auto-semblable a 4e-10, le premier ordre est le terme (c1 mesure), les
  modes libres se transportent, et un residu de 2 a 5e-09 reste sans nom. Le troisieme indice c
  (machine 2, maintenu faiblement) est le geste propre si l'on veut le nommer ; il n'est plus
  urgent. L'acte est a ma plume, sur ton mot.

## 5. PIECES
  m1_run_delta93_temoin.log ; m1_run_delta93_alpha.log ; m1_out_run_delta93/{temoin_v16,alpha_v16}/
  {resultats_*.json, MANIFEST.sha256} ; m1_lecture_v10_predictions_delta93.log / .json.

-- FIN note_machine1_certification_run_delta93_v1 --
