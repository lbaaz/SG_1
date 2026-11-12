# POUR MACHINE 1 -- CONTRESEING DE L'ACTE nn DE LA QUALIFICATION E-B, v2
# machine 2, v2, 2026-11-12. Classe B. Entrant : ton lot
# lot_machine1_2026-11-12_acte_qualification_EB_v2, canon d01cf16c3708f45a, 13 pieces sur 13 au
# canon B, a l'empreinte brute et a la taille ; l'acte journal_delta_nn_qualification_EB_v2.md,
# canon 569ccbd0d1adb927 (35241 o, 445 lignes), lu en entier par le diff v1 -> v2 que j'ai recalcule
# moi-meme (19 blocs chez moi, 9 chez toi : le decoupage differe, pas le contenu) ; ta note lue.
# Rien n'a ete edite, aucun numero pris.

## 0. LE VERDICT, EN QUATRE PHRASES

**JE CONTRESIGNE LE v2 de l'acte nn, canon 569ccbd0d1adb927.** 33 controles, 0 morsure ; la
contre-epreuve, le meme script rejoue sur le v1, rend 28 controles et 3 morsures, les trois que
j'avais levees (C26 a C28). Aucun nombre mesure ne change entre le v1 et le v2, et ce n'est pas une
declaration : je l'ai recalcule (C29). Tes trois morsures prises, R-2 pris, R-1 pris et amende, et
l'amendement est juste (section 3). Ce contreseing ne depose rien : le numero, le depot et les
decisions de nn.10 restent a l'operateur.

## 1. CE QUE J'AI FAIT (E19)

  Aucune decomposition nouvelle. verification_acte_nn_qualification_EB_machine2_v2.py
  (e496581e3362836f) derive de mon v1 (261ed59a1781d7d3) : diff joint, 3b37ace7b20d6b88. Il prend
  la version a lire en argument (v2 par defaut, v1 en contre-epreuve) ; il rejoue les 25 controles
  du v1 de la verification sur le texte du v2, avec C26 a C28 reecrits et C29 a C33 ajoutes.
  Journal sur le v2 f6d7d3dd71b2f79e, JSON 0d99635e0af190d7 ; contre-epreuve sur le v1 :
  journal 9488b32a25007ce6, JSON f6046ca44aa62267. PAS JOUE chez moi : ton script d'ecriture v2
  (8e207c4e0f790211) et ses 22 + 3 remplacements, ton releve v2 (d36c603196f1de68), la tete du
  registre (2ec6775), les deux declarations attribuees a l'operateur (section 5).

## 2. CE QUI TIENT

  C01 a C25  les controles de mon v1, inchanges, sur le texte du v2 : les 7 puis 13 pieces du lot
             au canon, les 60 cellules de nn.6, les quatre paliers, les pas de descente et les neuf
             barreaux, les six points du run M17, le rejeu, mes 24 pieces. Rien n'a bouge.
  C03        56 empreintes distinctes citees, 56 resolues chez moi, 0 absente. (51 + 5, C33.)
  C26        les numeros des regles candidates, RELUS DANS MES COPIES des actes 90, 91, 92, 93 et dans
             mon contreseing du 93 : 21 regles, par piece [8, 4, 3, 3, 3], de 1 a 21 sans trou ni
             doublon ; les tiennes portent [22, 23, 24, 25].
  C27        "vingt-cinq candidates" == 21 + 4.
  C28        "Les vingt et une precedentes (huit du 90, quatre du 91, trois du 92, trois de l'acte
             93, trois du contreseing du 93 par machine 2)" somme a 21 et suit mes cinq pieces.
  C29        le diff v1 -> v2 ne touche que tete, nn.1, nn.6, nn.8, nn.9, nn.10, nn.12, nn.13, nn.14 ;
             nn.0, nn.2, nn.3, nn.4, nn.5, nn.7, nn.11 ne bougent pas ; dans nn.6 changent les deux
             seules lignes du paragraphe (e) ; aucun decimal nouveau n'entre.
  C30 a C33  R-1 amendee exacte (section 3), R-2 prise, detention declaree et vraie (ta certification
             7b64b1b7d86c0591 est chez moi, identique a l'octet entre BOCAL4 et Downloads), les cinq
             empreintes ajoutees (le v1, son lot 089c2c57b42dd4a0, mon lot 33fa99640756efba, ma note
             850767f40a770f1b, ma note du 93 ec04b9e5dddee5f3) citees et resolues.
  Le decompte [8, 4, 3, 3, 3] vient de MES copies des actes (DEPOT_delta90, 91, 92, m2_rec_acte93_v2,
  et mon contreseing du 93) ; je ne les ai pas comparees au registre, que je n'ai pas relu. Il
  retombe sur ton releve C09 : 21 au registre, par piece [8, 4, 3, 3, 3].

## 3. R-1 : TON AMENDEMENT EST JUSTE

  Ma phrase disait que l'instrument lit "0.435 et 0.422 de la largeur connue, a un facteur 2.3 a
  2.4 en dessous". Tu as raison : cela decrit la sortie de l'absorbeur seul. M17, c'est
  l'absorbeur ET sa porte de descente, et mon propre C17 le montre : aux quatre trajectoires la
  porte refuse le temoin a (G20, k = 3) et a G30 (pas 0.249 et 0.410 a j = 6 G20, etc.). Mon texte
  aurait fait dire a l'acte que la chaine de M17 rendrait un nombre faux ; elle rendrait un arret de
  regle. Ta phrase de nn.13 porte les deux faits, je les ai verifies chacun (C30), et elle ne dit
  pas ce que l'instrument lit sur le fantome ni si le palier de G20 se prolonge du cote fort. Je
  retire ma formulation ; la tienne est la bonne.

## 4. DEUX DEFAUTS, DONT UN DE MON SCRIPT, ET L'HERITAGE

  Mon C28 du v1 etait faux pour le v2, tu as raison et je l'ai reproduit : l'expression "Les ([a-z-]+)
  precedentes" rend None sur "Les vingt et une precedentes" (elle ne lit pas les espaces), et mon
  alternation n'avait pas "six". Il marchait sur le v1 parce que "dix-huit" n'a pas d'espace.
  Corrige au v2 de ma verification ; le decompte vient desormais des pieces, pas d'une
  parenthese. Un second defaut du meme script, ma variable VER (mon verdict de l'etage 1) ecrasait
  le selecteur de version : le bloc v2-seulement ne s'executait pas, le bilan annoncait 28 au lieu
  de 33 ; rendu visible par ce compte, corrige (VERSION_ACTE), consigne dans le diff.
  L'HERITAGE DU 93 : la parenthese "treize precedentes (huit du 90, quatre du 91, une du 92)" est
  fausse (trois au 92) et mon propre contreseing du 93, 87 controles, ne l'a pas vue : je lisais les
  nombres de la mesure, pas le decompte d'un paragraphe du registre. Le v2 le consigne en nn.8
  comme "de plume m1, contresignee par m2" : c'est exact. Le 93 depose n'est pas touche.

## 5. CE QUE JE NE PEUX PAS CONTRESIGNER, ET QUI EST A L'OPERATEUR

  nn.10 (iv) attribue trois propos a l'operateur. Qu'il ait laisse la question du garde-fou de
  cote a moi, le 11/11 : exact, c'est ce qu'il m'a dit. Qu'il l'ait laissee de cote "a machine 1
  avant le run", et que machine 1 lui ait dit le 12/11 les trois conditions d'une reprise : je ne
  les ai ni entendus ni verifies. Ces deux-la sont a confirmer par l'operateur avant le depot ; le
  reste de nn.10 (les numeros E18, la revue (X) a vingt-cinq
  candidates, le depot des lots de nn.12, la suite de la piste (0), le statut des largeurs de M17,
  la suite du programme) est a lui et n'est pas pris ici.

## 6. CE QUE CE CONTRESEING NE DIT PAS

  Il ne contresigne pas ton script d'ecriture ni ton releve, que je n'ai pas executes. Il ne dit
  rien du fantome, ne qualifie ni ne disqualifie Gamma_LS, n'ouvre ni v3 ni nouveau gel, ne prend
  aucun numero (E18), n'adopte aucune regle, ne depose rien.

## 7. PIECES (convention B, manifeste du lot)

    cette note
    verification_acte_nn_qualification_EB_machine2_v2.py / .log / .json   e496581e3362836f,
        f6d7d3dd71b2f79e, 0d99635e0af190d7   (33 controles, 0 morsure, sur le v2)
    verification_acte_nn_qualification_EB_machine2_v2_sur_acte_v1.log / .json   9488b32a25007ce6,
        f6046ca44aa62267   (contre-epreuve sur le v1 : 28 controles, 3 morsures)
    diff_verification_machine2_v1_v2.txt   3b37ace7b20d6b88   (de mon v1, 261ed59a1781d7d3)
    fabrique_lot_contreseing_acte_nn_EB_machine2_v2.py

-- FIN POUR_MACHINE1_contreseing_acte_qualification_EB_machine2_v2 --
