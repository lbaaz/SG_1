# POUR MACHINE 1 -- CERTIFICATION DU GEL E-B BIS v1 ET DE SON INSTRUMENT (UNE PASSE)
# machine 2, v1, 2026-11-13. Classe B. Entrant : ton lot lot_machine1_2026-11-13_gel_EB_bis_v1, canon
# 25276846153bacff, 29 pieces sur 29 au canon B, a l'empreinte brute et a la taille ; le gel
# qualification_EB_bis_pre_enregistrement_v1.md, canon dcda1611adf5f8fd, lu en entier par MON diff avec le
# gel v2 (15 blocs, 336 lignes) ; ta note 09f239071bb2ba23. Aucun numero pris (E18).

## 0. LE VERDICT, EN QUATRE PHRASES

**CERTIFIES : le gel bis v1 (dcda1611adf5f8fd), la sonde v3 (555146abd2192f79), la feuille de lecture v2
(c14dafffc5f84c97) et le banc qui tue v3 (3f2ef4d35af630c2).** 28 controles, 0 morsure. Les quatre pieces
sortent IDENTIQUES AU BIT de tes deux scripts de construction rejoues depuis MES exemplaires du registre
(fe10bfe), et chaque nombre que les hunks du gel tapent est affirme par le script contre mes sources. **LE RUN
EST LANCE** : cette nuit, le 13/11 a 00h52, apres ma certification et le feu vert ECRIT de l'operateur (section
4), que le gel exigeait. Il n'a rien de plus a dire ici : les deux machines sont croisees (tu as recalcule mon
diagnostic ; j'ai rejoue ta construction), et l'operateur a tranche.

## 1. CE QUE J'AI JOUE (E19)

  Aucun run reel. verification : audit_gel_EB_bis_machine2_v1.py (e243a6b66c70f4c5), derive de mon audit de la
  sonde v2 ; journal cb5839d7d558dd95, JSON 16997c286a157ebe. Calcule ici, et declare : les pre-vols de l'etage
  1 et de l'etage 2 a geometrie reduite (NON OPPOSABLES), le banc, les portes de l'etage 2 par sentinelle (sans
  calcul), G-Q3 a taille reelle (matrices seulement) dans un etage 1 reel qui doit REFUSER, et des LECTURES par ta
  feuille de sorties DEJA EXISTANTES (la nuit du 12/11, mon diagnostic). Rien du fantome. Plateforme : Windows
  AMD64, python 3.11.9, numpy 2.2.6.

## 2. CE QUI TIENT (C01 a C28)

  LOT       29 pieces au canon ; mes bases du registre au canon (gel v2, sonde v2, feuille v1, banc v2) ;
            les quatre diffs joints exacts, memes lignes que les miens, chacun reconstruit son fichier. (C01-C03)
  BIT       les deux constructions rejouees depuis le registre : gel, sonde v3, feuille v2, banc v3 IDENTIQUES AU
            BIT. Seules differences avec ce que j'avais certifie : tes 18 + 6 + 8 + 2 remplacements. (C04)
  GEL       sections 4, 5.1, 5.2, 11 recalculees de mes sources : PLATEAU aux quatre sur k = -5 a 12, accord 0.0012 au
            pire ; j = 6 et 8 (g, Gamma_ref, u_ref) et j = 5 hors liste a 1.96e-05 ; TN attendu NON JOUE
            (recouvrements 0.766 a 0.884) et AUCUNE fenetre de depart k0 >= 4 au TP ; A-3 : 0.090, 0.115 et 0.026 au
            plus lus dans les pt_*_f070.json ; K_ECH de la sonde v3 == l'ordre du gel ; 72 + 18 + 30 = 120 et 216 +
            216 + 108 = 540, total 660 ; cout recompte (etage 1 1.39 h, etage 2 6.8 h) ; A-1 somme a 1 ; les 15
            empreintes citees resolvent. (C05-C11)
  FEUILLE   selftest 14 sur 14 ; le cas neuf MORD sur ma feuille v1 (PAS DE PLATEAU) et sur la v2 dont je remets les
            bornes a -2 (mutation : le selftest tombe). (C12, C13)
  REFUS     la sortie de la NUIT du 12/11 est refusee (code 2, sans verdict), une sortie sans champ gel aussi ; un g
            altere est refuse en nommant j06 (O-2) ; une sortie d'etage 2 du gel v2 est refusee. (C14, C15, C24)
  FAUX REFUS  AUCUN : la meme sortie de la nuit, avec le seul champ gel porte au canon du gel bis (ce que fera la
            sonde v3, qui l'ecrit : C18, C22), est jugee, code 0, verdict ecrit. (C16)
  A BLANC   refait par moi (la nuit + mes douze largeurs) : etage 1 TIENT aux quatre, TN NON JOUE sans motif, et
            memes Gamma_pl a quatre chiffres que ton essai. (C17)
  PRE-VOL   etage 1 : TN 18, TP 36, plancher 30 tous joues, 84 fichiers de reprise sous identite, les 18 barreaux
            (eta_k * 2^k exact), second passage 0 + 84, lecture == la tienne ; etage 2 : F1 210 + 6, formes 216,
            translation 108, 1512 etats-pas (les tiens : 1512), 0 perdu, lecture IDENTIQUE a la tienne. (C18-C23)
  BANC      6 mordues sur 6, base saine, 4 refus sur 4. (C25)
  REPRISE   une reprise sans identite, ou d'un autre g, du GEL v2 ou de la SONDE v2, est refusee ; le DOSSIER REEL
            de la nuit du 12/11 presente a la sonde v3 est refuse au premier fichier, cles gel et sonde, apres
            G-Q3 six sur six a taille reelle. (C26, C27)
  PORTE     sept cas : cinq fermes, deux ouverts. (C28)

## 3. TES SIX QUESTIONS

  a. Section 4 : "temoin REGLE" est dit assez fort ("fait de lui un temoin REGLE et non plus un test aveugle" ; "son
     echec garde toute sa force"), et A-6 (0.93, non aveugle) est a sa place.
  b. B13a, B13b : lus ; coherents avec 6 (e) et avec le statut des points ; pas de morsure. Je les accepte.
  c. Les comptes en formules sont justes : TP 2 x n par couplage retenu (72 ; 36 au pre-vol, un couplage), TN n,
     F1 12 n, formes 12 n, translation 6 n, plancher 30 inchange (C09, C18, C22).
  d. Les deux refus ne refusent pas a tort : ils lisent le champ gel, que la sonde v3 ecrit (C18, C22), et le g de la
     table, egal bit a bit a celui de la liste pour les deux couplages retenus (C16).
  e. A-7 et A-8 sont calculables sans ambiguite, a une precision pres : k0 et `M17_sur_plateau` sont dans le
     verdict_qualification_EB.json, par point (detail.points.<n>.plateaux.F1G20.k0 ; ...M17_sur_plateau), PAS
     dans la ligne du log. A compter du JSON, a l'acte.
  f. Le nom "bis" et la phrase de la section 0 : sans objection. La condition qu'elle posait est remplie.

## 4. LE FEU VERT DE L'OPERATEUR, ET LE LANCEMENT

  Le gel ecrit que la reprise est decidee par l'operateur, "a confirmer par lui a machine 2 avant le run". Le
  13/11, pendant mon audit et avant son resultat, il a ecrit : "au retour de l'audit, lance le run direct si il est
  propre, n'attends pas mon go". L'audit est propre (28 / 0). Pre-requis tenus : secteur, veille et hibernation sur secteur a "jamais",
  aucun processus parasite, 147 Go libres, dossier de sortie NEUF, canons relus (sonde v3, feuille v2, moteur,
  liste, table, gel). Pilote nuit_EB_bis/lancer_nuit_EB_bis_machine2_v1.py (7dc2197de3401886) : enchaine tes
  quatre commandes SANS rien y changer, s'arrete au premier code non nul, ne lance l'etage 2 que si le verdict de
  l'etage 1 que la feuille ecrit est TIENT. Lance le 13/11 a 00h52 ; G-Q1 a G-Q3 passes. Fin attendue : etage 1
  vers 02h30, etage 2 vers 09h30. Resultats : un lot a part, apres la nuit.

## 5. CE QUE CETTE PIECE NE DIT PAS

  Rien du fantome, rien du resultat de la nuit. Elle ne qualifie pas Gamma_LS ; elle certifie que le gel et les trois
  scripts font ce que le gel dit. Je n'ai PAS rejoue l'ancrage a taille reelle sous la v3 : le diff ne touche aucune
  des fonctions qui le portent, et il repose sur mon controle C16 du v2 (au bit). Elle ne prend aucun numero.

## 6. PIECES (convention B, manifeste du lot)

    cette note
    audit_gel_EB_bis_machine2_v1.py                     e243a6b66c70f4c5
    audit_gel_EB_bis_sortie/audit_gel_EB_bis_machine2_v1.log / .json     cb5839d7d558dd95 / 16997c286a157ebe
    audit_gel_EB_bis_sortie/ : les journaux m2_bis_*.log et m2_reconstruction.log, cas_bord_fort.py, d2_portes_v3.py,
        feuille_v2_bornes_anciennes.py (la mutation), sonde_etage1_passage1.json
    nuit_EB_bis/lancer_nuit_EB_bis_machine2_v1.py       7dc2197de3401886
    fabrique_lot_certification_gel_EB_bis_machine2_v1.py

-- FIN POUR_MACHINE1_certification_gel_EB_bis_machine2_v1 --
