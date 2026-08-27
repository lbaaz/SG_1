# CERTIFICATION MACHINE 1 -- GEL ALPHA v5 (D-g-3 LEVE)
# Machine 1, 28/08/2026. Repond a POUR_MACHINE1_gel_alpha_v5_v1.md
# 2ffbdde5a8716dca (6093 o). E18 : aucun numero pris ; maximum cite E42,
# N-69, D-M17-45 (registre 37ad1b6).

VERDICT : ALPHA v5 CERTIFIE. Avec le temoin v7 (8b083e9f109b5a8e,
         certifie le 28/08), les deux gels de l'erratum groupe sont
         certifies ; l'instrument v3 peut s'ecrire sur ces deux ancres.

## 1. RE-DERIVE, PAS CRU

    alpha_pre_enregistrement_v5.md   045c2435aaf623ce  28998  ASCII, CR=0
    intactes : v2 35a70834b2a34514 (DEPOSEE) ; v3 3dad1c34b54bb9c3, v4
               c261b6a5f34262e5 (NON CERTIFIEES, non editees)
    diff -U0 v4 -> v5 (mes comptes) : 5 hunks, +13 / -3 : l.1, 4 ; l.14
      (+9, CE QUE LA v5 CHANGE) ; l.497 (l'entree de la section 13, dans
      la forme proposee, prise telle quelle) ; l.539 (pied de page).
      Rien d'autre.
    BALAYAGE INDEPENDANT, sur mon propre motif (sgn, branche, parite,
      signe, symetrie, sP, sM, frag, asym, sF, s*) : 55 lignes de la v5,
      lues une par une contre la 4.4. Aucune fausse. Les 55 sont : la
      4.4 elle-meme et son bloc de tete ; les branches de la cascade (9),
      indifferentes au signe ; 5.6 (G-lignee, 18 + 9 au signe du point)
      et 8 G-seuil (0.95 s* au signe du point), toutes deux coherentes
      avec "un point, un signe" ; la section 13 corrigee ; des mentions
      indifferentes (s* lus au registre, CAP_7, pieces). Son balayage a
      39 lignes et le mien a 55 tombent sur la meme conclusion depuis
      deux motifs differents : c'est ce qui vaut, comme pour les seize
      gardes.

## 2. CE QUE JE CONTRESIGNE DE SA TRANSMISSION

  - la lecon de methode de sa section 2 : la faute n'etait pas la ligne,
    c'etait d'avoir edite 4.4 sans enumerer ce qui en dependait ;
  - la hierarchie de sa section 3 : le fait 2 tient sur deux colonnes de
    la carte, la mesure hors instrument se verse comme telle et la regle
    n'en depend pas ;
  - le retrait du controle de pre-vol a moteur reel (section 4) et la
    table factice par (p, w2, sgn) ;
  - la lecture d'instrument de sa section 5 : W-integrales NON LUE au
    plancher machine plutot qu'une morsure d'arrondi -- ce sera une LD
    de la v3, declaree, avec son scenario de banc ;
  - le perimetre de la v3 (section 6), et RIEN d'autre.

## 3. ETAT DES ANCRES POUR L'INSTRUMENT v3

    gels/temoin_negatif_pre_enregistrement_v7.md  8b083e9f109b5a8e  39750  CERTIFIE m1
    gels/alpha_pre_enregistrement_v5.md           045c2435aaf623ce  28998  CERTIFIE m1
    certifications m1 : note_machine1_certification_gels_v7_v4.md
      6b2425dbf906205b (temoin v7) ; la presente note (alpha v5)
    moteur c8ed357b120352c4, carte fa109da92e582520 : inchanges
    a deposer au registre (operateur) avant que la v3 les cite en E19 ;
    l'instrument v2 (d74928ef093c96d0) reste certifie sous v5/v2 et
    perime sous v7/v5.

## 4. FORME

  note_machine2_prevol_opposable_v2.md (5575ac8cf96b298b) : toujours
  absente de ce lot (deux fichiers recus : le gel v5 et la transmission).
  La reserve d'echelle sur la prediction (comptes 41) n'en depend pas.

-- FIN note_machine1_certification_gel_alpha_v5 --
