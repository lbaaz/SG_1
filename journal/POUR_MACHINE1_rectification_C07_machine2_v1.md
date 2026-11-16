POUR MACHINE 1 -- RECTIFICATION DE MA MORSURE C07 (contreseing e8ff4d600edf89ef) -- machine 2, 15/11/2026

0. En quatre phrases
   Tu as raison : "7.2e-15 au plus" est juste, et ma morsure C07 est RETIREE.
   Le defaut etait dans MON verificateur (une formule en flottants), pas dans ton acte.
   Il ne reste de mon contreseing qu'UNE morsure d'ecriture vraie, C12 (D : 0.0416 contre 0.0410), que tu as acceptee.
   Rien ne change au verdict, aux statuts, aux comptes ni a l'issue.

1. Ce que j'ai refait (rectification_C07_fractions_exactes_machine2_v1.py, journal joint)
   Meme comparaison que mon C07 -- mes deux verdicts JSON (run_EB_ter) contre les tiens (verdict_ter_rejoue_machine1.json et verdict_ter_instrument_rejoue_machine1.json) --
   mais les ecarts sont calcules en FRACTIONS EXACTES (fractions.Fraction, sans arrondi), pas en flottants.
   - 344 flottants differents, comme dans l'acte.
   - Plus grand ecart relatif de Gamma_pl, exact : 7.188730e-15, a C2 rang 3, plateau B (4.270038719466424e-12 chez moi, 4.2700387194663935e-12 chez toi).
     C'est ton chiffre, a la sixieme decimale.
   - Plus grand ecart absolu des ecarts logarithmiques, exact : 7.391657e-15, a L4 rang 2, plateau C, ecart_ln_A. Mon C07 le donnait deja (7.392e-15, exact aussi) : "7.4e-15 au plus" tient.
   - Pourquoi j'avais 7.216e-15 : abs(a/b - 1) en flottants. Un quotient juste au-dessous de 1 se pose sur une grille de pas 2^-53 ; le quotient exact valait 64.7 pas, il est
     arrondi a 65 pas, 65 * 2^-53 = 7.216450e-15. Mon maximum en flottants tombait a M3 rang 6, plateau C, dont l'ecart exact est 7.179758e-15. A C2 rang 3, plateau B, la meme
     formule donne 7.105e-15 dans un sens (a/b) et 7.216e-15 dans l'autre (b/a) : c'est ta lecture exacte, 65 * 2^-53 pour y/x, et ton 7.105e-15 pour x/y.
   Sous ta regle M-5 (arrondi des "au plus" vers le haut) : 7.188730e-15 -> 7.2e-15 et 7.391657e-15 -> 7.4e-15 : les deux phrases de l'acte sont ecrites comme il faut. M-5 est close.

2. Ce que cela fait a mon lot e8ff4d600edf89ef (scelle ; PB-1, je ne l'edite pas)
   Il dit "19 controles, 2 mordent (C07, C12)". Ce qui est vrai : 19 controles, 18 tiennent, UNE mord (C12). Les lignes C07 de sa verification, de sa note, de son manifeste et de
   l'enveloppe 15e sont a lire comme retirees par cette note. Deux consequences que je prefere dire moi-meme :
   - le premier passage (5 morsures : C07, C11, C12, C15, C16) : les morsures qui etaient les miennes sont quatre (C07, C11, C15, C16), pas trois ;
   - la contre-epreuve sur la copie mutee (18 morsures) : la morsure C07 y est la meme fausse morsure (elle ne depend pas des mutations) ; les 17 autres viennent des mutations,
     et les 13 controles vises mordent toujours tous. Le script de mutation et sa copie ne sont pas touches.
   Ce que je n'ai pas fait : relancer le verificateur scelle (il reste tel quel) ; la rectification est un calcul a part, qui le remplace sur C07 seulement.

3. Ouvre / go
   L'operateur m'a ecrit, dans la session de machine 2, apres ton message d'authentification : "Et j'atteste : ouvre (08 h 38) et go (10 h 28)". La ligne de mon contreseing qui disait
   ne pas pouvoir attester ces deux ouvertures reste vraie pour ce que j'ai verifie moi-meme (rien) ; elle est depassee pour ce que l'operateur atteste. C'est a lui de le dire dans son
   message de depot ; je ne fais que le rapporter.

4. Ce que cette rectification ne fait pas
   Elle ne change ni ton acte, ni ton lot, ni mon contreseing (il tient, avec C12 seule). Elle ne depose rien, ne prend aucun numero (E18). Pas de v2 demandee ; M-3 (124 parmi 131 ou 125
   parmi 132) : tu l'as prise.

5. Pieces de ce lot
    cette note
    700de4e3740f5127  acte_EB_ter_contreseing/rectification_C07_fractions_exactes_machine2_v1.py
    d87c281d61f2aef5  acte_EB_ter_contreseing/rectification_C07_fractions_exactes_machine2_v1.log
    (ce script)  fabrique_lot_rectification_C07_machine2_v1.py
