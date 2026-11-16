POUR MACHINE 1 -- (i) L'ORDRE 3 REDERIVE PAR MON CODE, ET REJEU DE L'ETAPE 1 -- machine 2, 15/11/2026
Hors chaine, une plume de plus, 1D seulement : AUCUNE largeur 2D calculee, aucun point neuf (E19). Le point (iii) de ton POUR_MACHINE2 attend la carte : je n'y ai pas touche.

0. En six phrases
   L'operateur a demande (i) : rederiver le terme d'ordre 3 par mon code et le confronter a tes tables. C'est fait, sur tes 132 etats juges du delta 98.
   J'ai ecrit la formule 3.1 de ta note a partir de son texte seul et je n'ai pas lu ordre3_bloc_machine1_v1.py avant d'avoir fini et lance mes scripts.
   Mes T3, W3 et W5 coincident avec les tiens aux 132 etats : T3 a 1.2e-11 pres en relatif au pire, W3 a 1.1e-11, le maximum de |W5/t| a 1.0e-14 ; les deux parts de T3 (chemins hors echelle,
   chemins repassant par l'echelle) a 6e-16 pres (relatif a la somme de leurs valeurs absolues, donc malgre leur compensation) ; ma chaine d'ordre 3 (ton bloc d'ordre 2 depose et mes trois tables) redonne tes G_c3 a 5.8e-10 pres, et tes six variantes a 2.0e-9.
   Sur le vrai operateur, dans une base tronquee d'une autre echelle ((3, 1), w2 = 2.07), la formule contre l'effectif exact : le reste decroit comme g^3.00 sans l'ordre 3 et g^4.00 avec ;
   W3 et W5 pris chacun a part contre l'exact : ecart relatif au saut lui-meme en g^2, comme attendu.
   Je ne trouve aucun terme manquant au troisieme ordre ; je n'ai rien dit, et rien teste, de ce que l'ordre 3 vaut hors de son domaine.

1. Ce que j'ai fait (mes scripts, mes journaux ; les chiffres ci-dessous y sont tous)
   (a) formule_ordre3_jouet_machine2_v1.py : ta formule 3.1 contre l'effectif exact (des Cloizeaux : projections des 4 etats propres de plus grand poids sur A, orthonormalisation symetrique)
       d'un jouet aleatoire (A : 4 niveaux a 0.03 pres, B : 7 niveaux, couplage dense). Exposants de g : 2.99, 2.97, 2.96 sans l'ordre 3 ; 3.98, 3.96, 3.90 avec.
   (b) ordre3_machine2_v1.py : mon enumeration explicite des chemins sur l'echelle (sauts hors echelle de au plus 5 quanta, parite impaire, elements de x^5 du moteur 82a0be882568fe0c).
       Controles internes : hermiticite (H_{m,m+j} = H_{m+j,m}) a 1.4e-14 ; mon ordre 2 refait par la meme methode (S et U) identique au bloc depose 7cd5977bc27bebc1 (ecart nul) ;
       aucun saut d'ordre 3 aux j pairs ni a la diagonale (nuls par construction, verifies dans la base tronquee).
       Portee : trois sauts de 5 quanta ne laissent que j = 1, 3, 5 barreaux (3 j <= 15) ; j = 7 est impossible.
       Contre tes tables (ordre3_par_etat_v1.json) aux 132 etats : T3/t et ses deux parts, W3, maxima de |W3/t| et de |W5/t| sur la barriere (3.8e-13 et 1.0e-14), chaine d'ordre 3 (G_c3 a 5.8e-10,
       variantes T3_seul, W3_seul, sans_W5, ef_double, ef_demi, recul_4 a 2.0e-9 au pire : c'est la sensibilite de la diagonalisation, pas une difference de table).
   (c) le meme script avec --boite : le vrai operateur dans une base tronquee (0 <= n1 <= 11, 0 <= n2 <= 6, echelle de (3, 1), w2 = 2.07, 6 sites, B 78 etats). V est hermitien (ecart nul).
       La formule 3.1 ecrite en matrices denses contre l'effectif exact : exposants 3.00 / 4.00 ; mes chemins contre la formule dense a 1.8e-15 du plus grand saut (4.2e-15, 3.3e-15 et 1.2e-15 de
       chaque saut lui-meme aux j = 1, 3, 5) ; les sauts j = 3 et j = 5 contre l'exact, a g croissant : ecarts relatifs 4.7e-05, 1.9e-04, 7.4e-04 (j = 3) et 7.4e-03, 2.9e-02, 1.1e-01 (j = 5),
       rapports 3.95, 3.95 et 3.92, 3.87 : en g^2, c'est le terme d'ordre 5 qui reste, pas une erreur sur l'ordre 3.
   (d) etape1_rejeu_machine2_v1.py : ton etape 1 rejouee sur mes copies (registre 8d54bf9, mon verdict_ter.json 2cd1f84efa02f2ab) : 2921 feuilles, ecart relatif au pire 4.4e-16 avec ta sortie ;
       etendue de ln q2 par point 0.0622 -> 0.0205 (medianes) ; tableau 3.5 aux sept points a quatre chiffres ; dependance de MA reference a l'absorbeur (|ln(Gamma_pl(X)/Gamma_pl(A))|,
       136 etats QUALIFIES) : mediane au plus 0.0008, maximum 0.0264 (D) ; aux six points de ton domaine (72 etats), maximum 0.0057 : ton accord a 0.8 pour cent y est au-dessus.

2. Position sur ton "ou mordre"
   M-1 (la formule). Elle tient, sur un jouet et sur le vrai operateur ; mon "exact" est la meme famille que le tien (effectif de des Cloizeaux, canonique) : je n'ai PAS essaye une autre
       definition de l'effectif (Bloch, Feshbach dependant de l'energie), qui change les sauts d'ordre 3 d'une rotation dans l'echelle ; la largeur du systeme complet n'en depend pas, celle de la
       chaine tronquee (absorbeur pose sur des sites) un peu. Le cinquieme voisin : un seul element dans la base tronquee, 6.1e-14 a g0, au plancher d'arrondi ; je l'ai donc pris a g croissant
       (point (c)) et, sur les vrais etats, par son maximum (1.0e-14 d'accord). Terme manquant : je n'en trouve ; mon enumeration est generique (tout chemin de trois sauts qui revient sur
       l'echelle), elle ne suppose pas de regle de parite pour decider quels sauts existent, et elle donne le W5 que ta premiere ecriture avait oublie (D-LOI-4).
   M-2 a M-3, M-5 a M-9 : pas testes. M-4 : la reference est precise (point (d)) ; elle reste celle d'un acte que je viens de contresigner (et d'une morsure que j'ai retiree : voir le lot de
       rectification dans la meme enveloppe).

3. Ce que ce controle ne dit pas
   - Il ne dit pas que l'ordre 3 est la loi hors de son domaine, ni que ta lecture de L-4 (la serie diverge, ou les sauts longs ajoutent des solutions parasites) est la bonne : il porte sur
     l'exactitude du terme, pas sur la convergence de la serie. Il ecarte une cause : un defaut d'ecriture de l'ordre 3 (formule, chemins, W5).
   - Deux plumes sur le meme texte de formule (la tienne et la mienne) ; la formule elle-meme est controlee contre l'exact, pas contre une seconde source.
   - Rien en 2D. La section 5 de ta note (le gel) n'est pas jugee ici : (iii) attend la carte.
   - Je ne contresigne rien : ta note n'a rien a contresigner. Ce lot est un controle, il ne change aucun statut.

4. Pieces de ce lot
    cette note
    cea376571154f7ae  controle_ordre3_machine2/formule_ordre3_jouet_machine2_v1.py
    a665826ecd45028d  controle_ordre3_machine2/formule_ordre3_jouet_machine2_v1.log
    4d227d827b84c8bd  controle_ordre3_machine2/ordre3_machine2_v1.py
    3c3e6070117e3991  controle_ordre3_machine2/ordre3_machine2_v1.log
    0ca2afb7279cc852  controle_ordre3_machine2/ordre3_machine2_v1.json
    c720b1e744547261  controle_ordre3_machine2/ordre3_machine2_v1_base_tronquee.log
    e6f4867aaf981d49  controle_ordre3_machine2/etape1_rejeu_machine2_v1.py
    796afa10fef963e7  controle_ordre3_machine2/etape1_rejeu_machine2_v1.log
    e1a4acad8f69cadd  controle_ordre3_machine2/etape1_rejeu_machine2_v1.json
    (ce script)  fabrique_lot_ordre3_machine2_v1.py
