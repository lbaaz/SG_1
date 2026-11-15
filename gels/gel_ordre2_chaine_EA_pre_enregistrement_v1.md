GEL -- LA CHAINE E-A AU SECOND ORDRE : COMPLETEE PAR SON SECOND ORDRE ET PAR SES SITES BAS, LA
CHAINE REND-ELLE LA LECTURE DE E-B, SUR DES POINTS NEUFS, DANS DES BORNES ANNONCEES D'AVANCE ?
PRE-ENREGISTREMENT, VERSION 1
(plume machine 1, certification machine 2, chantier ouvert par l'operateur, 2026-11-14)
=======================================================================

0. STATUT ET POSITION
  Ce gel fait suite au gel "la garde G-1 du moteur et la chaine E-A par etat" (b59651f99e60707a),
  joue le 14/11/2026, verdict LA GARDE NE TIENT PAS (acte e718d2db619af9b1, contresigne, depose au
  delta 97). Cet acte laisse trois suites ouvertes, dont : deriver le residuel de la chaine. Machine
  1 l'a derive hors chaine, apres coup, sur les points deja joues (note 022d32238a66df6b) : l'ecart
  entre la chaine du moteur et la lecture 2D serait le second ordre du meme calcul. Une note apres
  coup n'est pas un test. Ce gel est le test : la chaine d'ordre 2, sur douze points jamais joues,
  contre des bornes ecrites ici avant tout run.
  La lecture de E-B garde le statut que le gel bis lui laisse ("bonne a l'ordre de grandeur") ;
  aucune phrase de ce chantier ne dira "largeur" sans "lue a k = 3".
  Pour la methode, la chaine E-A est l'effet tunnel assiste par resonance, connu depuis 2002 (note
  d'anteriorite hors chaine 119f4e4dcbb4baba) ; ce gel ne revendique rien sur la methode. Le
  rattachement des deux termes du second ordre a cette litterature n'a pas ete verifie sur texte.
  Ouverture : l'operateur a ecrit "ok go" a machine 1 le 14/11/2026 a 22 h 04, apres que machine 1
  lui a ecrit que seul un gel sur des points neufs ferait de la note un resultat. Machine 2 ne peut
  pas le verifier sur piece ; le message de transmission de l'operateur le dit ou non.
  Tete du registre relevee par la plume apres l'ouverture : 79e77d2 (delta 97).
  Rien ne se joue avant la certification croisee (E19).

1. PIECES CITEES (convention B)
  Au registre (79e77d2)
    scripts/m17_chaine_v17.py  82a0be882568fe0c
        le moteur ; il n'est pas modifie
    journal/manche_m17_v17_MANIFEST_machine2.txt  4aecd0e2b23bc818
        le manifeste du run de M17
    gels/gel_domaine_G1_chaine_EA_pre_enregistrement_v1.md  b59651f99e60707a
        le gel precedent
    journal/journal_delta_97_domaine_G1_chaine_EA_v1.md  e718d2db619af9b1
        son acte, et ses trois regles candidates (a), (b), (c), sous (X)
    scripts/sonde_domaine_G1_machine1_v1.py  940a21b1d562bb49
    scripts/lecture_domaine_G1_machine1_v1.py  0a760e3a244e547d
        la sonde et la feuille du gel precedent, certifiees
    journal/sonde_chaine_par_etat.json  5d80bf2edd26a6c1
    journal/sonde_domaine_G1.json  d51a9c6ce98b0452
        les JSON des deux runs deja joues, lus par la note
  Hors registre, joints au lot pour lecture
    note_machine1_residuel_chaine_EA_second_ordre_2026-11-14_v1.md  022d32238a66df6b
        la note hors chaine de machine 1 ; non certifiee
    ordre2_par_etat_v3.json  c4ff0e3030b89c0c
        son tableau par etat (262 etats)
  De ce lot
    sonde_ordre2_machine1_v1.py  24315c52b234319c
        la sonde : elle mesure et ne juge pas ; derivee de 940a21b1d562bb49 par six hunks
    construction_sonde_ordre2_machine1_v1.py  953023fef69adddd
        les six hunks
    chaine_ordre2_bloc_machine1_v1.py  7cd5977bc27bebc1
        le bloc de la chaine d'ordre 2, insere tel quel dans la sonde par un des hunks
    essai_bloc_machine1_v1.py  3230b0bbab0c591c
    essai_bloc_machine1_v1.log  467a11b8883bf698
        le bloc redonne les 262 valeurs de la note au bit pres ; Gamma_flux contre -2 Im E
    lecture_ordre2_machine1_v1.py  0dc8241c680eb1ff
        la feuille : elle juge et ne mesure pas
    lecture_selftest_machine1.log  094f1b1b0ea9a63c
        les 160 cas de la feuille, construits sur une copie de la section 4 tapee a part
    banc_feuille_ordre2_machine1_v1.py  773abd09f6796a3a
    banc_feuille_ordre2_machine1_v1.log  10924c2fb4d17920
        la feuille alteree contre son selftest : la table, 131 alterations, 131 mordues ; le
        code, 109 alterations, 108 mordues ; la survivante (C82b) est equivalente : une ancre
        absente fait mordre G-4 qu'elle soit obligatoire a G-2 ou non
    conception_points_ordre2_machine1_v1.py  c42ae7fc3e711e39
    conception_points_ordre2_machine1_v1.log  c6c1f6bc29d72fab
        la garde, la chaine du moteur et la chaine d'ordre 2 SEULES sur 168 points candidats ;
        aucune decomposition 2D
    garde_aux_points_ordre2_machine1_v1.py  d75304c78b809a75
    garde_aux_points_ordre2_machine1_v1.log  4e6c51018ae51dfd
        la garde G-1 du moteur et la boite attendue aux seize points, a six decimales
    chaines_aux_points_ordre2_machine1_v1.py  2b933ac5f360a0cf
    chaines_aux_points_ordre2_machine1_v1.log  2d11530783a76a59
        les deux chaines, par les fonctions de la sonde elle-meme, aux seize points, sur les 512
        sites voisins des graines : aucune exception ; aucune decomposition 2D
    reference_ancres_ordre2_machine1_v1.py  1a005bdb31f6e07e
    reference_ancres_ordre2_machine1_v1.log  0316c1ad78ac20a4
        la chaine d'ordre 2 aux deux etats d'ancre, sans decomposition 2D : references de G-8
    sonde_essai_ancres_machine1.json  29502272f288f2d1
    lecture_essai_ancres_machine1.log  9d3e6005f39dabb5
        essai a blanc aux deux ancres, non opposable

2. CE QUI A MENE ICI
  La chaine du moteur est un premier ordre en g : sur l'echelle resonante de l'etat (n1, n2), sites
  m >= 0 d'occupations (n1 + 2m, n2 + m), elle garde la diagonale m delta (delta = w2 - 2) et le
  saut t_m entre voisins. La note y ajoute, sans parametre ajuste, (1) le second ordre par les
  etats hors de l'echelle, qui se reduit par parite a deux termes, le deplacement Sigma2(m) de
  chaque site et un saut u_m au second voisin, et (2) les sites m < 0 de l'echelle.
  Ce que la plume a vu, et qu'elle doit dire.
  (i) La note, sur les 243 etats juges de 22 points deja joues (w2 de 1.89 a 2.12, facteurs 2/3, 1
  et 3/2) : q2 = Gamma d'ordre 2 / Gamma_2D(3) tient dans [0.998 ; 1.512], contre [0.375 ; 7.00]
  pour la chaine du moteur ; le decalage d'energie de l'etat 2D est rendu a 0.11 pour cent en
  mediane, 0.50 au pire. Ces nombres sont APRES COUP : les 22 points etaient connus.
  (ii) Le residu de l'ordre 2 est d'un seul cote et croit avec le desaccord. Plus grand q2 de la
  note : 1.101 pour |delta| <= 0.05 (88 etats) ; 1.512 pour |delta| de 0.08 a 0.10 (118 etats) ;
  1.474 pour |delta| de 0.11 a 0.12 (37 etats). Hors de cette fenetre : de 1.82 a 2.69 a 2.15, et a
  1.85 deux etats sur onze restent de l'ordre de vingt a trente fois trop bas (D1 > 1/5 ; un
  second canal, a ce que la plume suppose).
  (iii) La plume a ecrit a l'operateur, AVANT de calculer la grille de ce gel, qu'elle donnait 0.85
  a "tous les etats juges dans un facteur 1.6 pour |delta| <= 0.12". Elle a ensuite calcule la
  chaine seule sur 168 points candidats (journal de conception) et situe q2 par la loi apres coup de
  la note, ln(q2) = 2.87 delta^2 m_bord. Cette loi sous-estime les points connus a petit facteur
  au-dessus de 2.00 (a 2.10 et facteur 2/3 : 1.411 au plus pour 1.512 lu). Au coin |delta| = 0.12
  et facteur 2/3 elle donne jusqu'a 1.711. La plume ne croit donc plus a 1.6 jusqu'a 0.12. C'est le
  defaut D-G1-3 de l'acte precedent, refait le meme jour ; elle l'ecrit a l'operateur avec ce gel.
  D'ou des bornes PAR BANDE de desaccord (section 6) au lieu d'une borne unique.
  (iv) La valeur lue change d'arithmetique, pas de definition. La note lisait -2 Im E de l'etat de
  la chaine. La sonde lit Gamma_flux = 2 <W> / <psi|psi>, W etant l'absorbeur de la chaine : c'est
  la meme quantite pour un etat propre exact. Journal de l'essai du bloc : au reglage de la sonde
  les deux different de 1.5e-06 en mediane et de 1.6e-02 au pire sur les 243 etats ; quand la chaine
  est deux fois plus longue, -2 Im E bouge jusqu'a 17 pour cent (arrondi de la diagonalisation non
  hermitienne aux plus petites largeurs), Gamma_flux de 1.7e-05 au plus. Les bornes de la section 6
  ont ete posees sur les nombres de la note, lus a -2 Im E.
  (v) La comparaison a la chaine du moteur ne se fait pas sur la mediane : a 1.89 et 1.90, facteur
  1, la mediane de la chaine du moteur est plus pres de 1 que celle de l'ordre 2 (0.958 contre
  1.229 ; 0.897 contre 1.197), par compensation d'erreurs de signes opposes. Au PIRE ETAT,
  l'ordre 2 fait mieux aux 22 points connus. La section 8 compare donc au pire etat.
  Les trois regles candidates de l'acte e718d2db619af9b1, sous (X), sont appliquees ici sans etre
  adoptees : (a) le selftest de la feuille ne construit aucun cas depuis la table qu'il eprouve ;
  (b) la borne porte une marge de bruit d'un plancher, et la lecture sans marge se rend avec le
  verdict (section 11) ; (c) la tete du registre a ete relevee, et ce qui se calcule sans run a ete
  calcule avant les annonces de la section 12 -- mais apres la phrase rapportee en (iii).

3. CE QUI EST MESURE (la sonde)
  Les mesures 2D et la chaine du moteur sont celles du gel precedent, au caractere pres (la sonde en
  derive par six hunks). Par point (w2, g) : s = 0.70 s_ff(w2, g) ; graine coherente du moteur ;
  boite par la regle de executer_EB du moteur a L = 20 : r_c = plafond(n1 de la graine) + 2 (m +
  max(8, m)) + 2, ou m est le dernier site de la barriere a la graine (0 si elle est vide), et N =
  r_c + 20 ; le point est INFAISABLE si N > N_MAX_EB = 120. H_2D du moteur (x^5, signe du fantome
  -1) a eta_k = eta0 2^(-k), eta0 = |w2 - 2|, pour k = 2, 3, 4 : trois decompositions par point.
  A k = 3, les 14 etats de plus grand recouvrement avec la graine, dans l'ordre du moteur. Pour
  chacun : J moyen et son ecart-type (J = n1 - 2 n2), <n1>, <n2> ; ETIQUETTE : n2 = arrondi de
  <n2>, n1 = arrondi de J + 2 n2 ; poids de l'etat sur le site (n1, n2) ; E_re = Re E ; Gamma_2D(3)
  = -2 Im E. Le meme etat est suivi a k = 2 et a k = 4 par plus grand recouvrement entre vecteurs
  normes, ce qui donne Gamma_2D(2), Gamma_2D(4) et deux recouvrements de suivi.
  Chaine du moteur : barriere(n1, n2, w2, g) avec Sigma2, puis gamma_chaine au site entier,
  M_facteur 4, a quatre eta de chaine (facteurs 1/4, 1/8, 1/16, 1/32) ; valeur lue : facteur 1/16.
  La garde G-1 du moteur est consignee a chaque point et jamais appliquee, comme au gel precedent.
  EN PLUS, pour chaque etat dont la chaine du moteur est definie, la CHAINE D'ORDRE 2 (le bloc) :
    sites m de m_min a M, m_min = -min(partie entiere de n1 / 2, n2), M comme gamma_chaine ;
    t_m : le saut du moteur, (g/5) X_saut_reel du canal (2, 1), aux occupations du site m ;
    Sigma2(m) : somme sur les 34 sauts de x^5 hors du canal de V^2 / (E_site - E_intermediaire) ;
    u_m : somme sur les memes sauts, de m a m + 2, de (1/2) V V' [1/(E_m - E_q) + 1/(E_m+2 - E_q)] ;
    diagonale : m delta + Sigma2(m) - Sigma2(0), plus l'absorbeur de gamma_chaine, inchange ;
    energies : celles, libres, du moteur ; un saut vers une occupation negative vaut zero ;
    etat lu : celui de plus grand recouvrement avec le site 0, comme gamma_chaine.
  Aux quatre memes eta de chaine : Gamma_flux (la valeur lue, au facteur 1/16), -2 Im E, et dE =
  Re E + Sigma2(0), le decalage d'energie de l'etat compte de l'energie libre du site. La sonde
  consigne aussi cette energie libre, E_libre = -n1 + w2 n2, par la fonction du moteur.
  Un arret du moteur ou du bloc se consigne et ne se rattrape pas.
  La sonde n'affiche aucun rapport et n'applique aucun seuil.

4. LES SEIZE POINTS (fraction 0.70 ; g = facteur x g_du_point(w2))
  La garde est celle du journal garde_aux_points (six decimales). N est la boite attendue.
  JUGES, bande PROCHE (|delta| <= 0.06)
    C1  w2 = 197/100  facteur 2/3   delta -0.03   D1 0.031915  c_max 0.039186  EN DOMAINE    N 73
    C2  w2 = 97/50    facteur 3/4   delta -0.06   D1 0.068182  c_max 0.066595  EN DOMAINE    N 68
    C3  w2 = 203/100  facteur 3/2   delta +0.03   D1 0.030000  c_max 0.022594  EN DOMAINE    N 55
    C4  w2 = 103/50   facteur 4/3   delta +0.06   D1 0.060000  c_max 0.046008  EN DOMAINE    N 56
  JUGES, bande MOYENNE (0.06 < |delta| <= 0.10)
    M1  w2 = 193/100  facteur 1     delta -0.07   D1 0.081395  c_max 0.059553  EN DOMAINE    N 60
    M2  w2 = 48/25    facteur 4/3   delta -0.08   D1 0.095238  c_max 0.069702  EN DOMAINE    N 55
    M3  w2 = 207/100  facteur 2/3   delta +0.07   D1 0.070000  c_max 0.090110  EN DOMAINE    N 74
    M4  w2 = 21/10    facteur 3/4   delta +0.10   D1 0.100000  c_max 0.130464  HORS DOMAINE  N 69
  JUGES, bande LOINTAINE (0.10 < |delta| <= 0.12)
    L1  w2 = 189/100  facteur 4/3   delta -0.11   D1 0.141026  c_max 0.102322  HORS DOMAINE  N 54
    L2  w2 = 47/25    facteur 1     delta -0.12   D1 0.157895  c_max 0.114482  HORS DOMAINE  N 60
    L3  w2 = 211/100  facteur 3/2   delta +0.11   D1 0.110000  c_max 0.086367  EN DOMAINE    N 55
    L4  w2 = 53/25    facteur 2/3   delta +0.12   D1 0.120000  c_max 0.158143  HORS DOMAINE  N 74
  ANCRES, connues, pour les gardes G-4, G-6 et G-8
    A1  w2 = 39/20    facteur 1     delta -0.05   D1 0.055556  c_max 0.040917  EN DOMAINE    N 60
    A2  w2 = 41/20    facteur 1     delta +0.05   D1 0.050000  c_max 0.051012  EN DOMAINE    N 61
  TEMOINS, hors enonce, lus sans verdict, joues en dernier
    W1  w2 = 107/50   facteur 1     delta +0.14   D1 0.140000  c_max 0.148692  HORS DOMAINE  N 62
    W2  w2 = 209/100  facteur 1/2   delta +0.09   D1 0.090000  c_max 0.139955  HORS DOMAINE  N 89
  Aucun des quatorze couples (w2, facteur) juges ou temoins n'a ete joue : ni par M17 (1.95, 1.97,
  1.98, 2.02, 2.03, 2.05 a facteur 1), ni par le gel "hors plage" (1.85, 1.90, 1.96, 2.04, 2.10,
  2.15 a facteur 1 ; 1.95 et 2.05 a facteurs 3/2 et 2/3), ni par le gel "garde G-1" (2.08, 2.09,
  1.91, 2.12, 1.89 a facteur 1 ; 2.10, 2.12, 1.90 a facteur 3/2 ; 2.08, 2.10, 1.91, 1.90 a facteur
  2/3). Les facteurs 3/4, 4/3 et 1/2 n'ont ete joues a aucun w2.
  Choix, fait sur la garde et les chaines SEULES. Chaque bande porte quatre points, deux de chaque
  cote de 2.00, a quatre facteurs differents. Les coins sont pris et non evites : M4
  (2.10, facteur 3/4) pour la borne 1.6 ; L4 (2.12, facteur 2/3) pour la borne 2 ; L2 (1.88), le
  plus bas, vers le second canal vu a 1.85. La garde G-1 du moteur ne choisit rien : elle dit HORS
  DOMAINE a quatre points juges, et l'acte precedent a montre qu'elle n'est pas le domaine.
  W1 prolonge le desaccord (0.14). W2 prolonge le facteur (1/2, barriere de douze sites a la
  graine) ; sa boite de 89 le rend environ dix fois plus couteux qu'un point de boite 60 : il est
  FACULTATIF (section 16).

5. LES ETATS JUGES
  A un point, un des 14 etats est JUGE s'il passe, dans cet ordre, douze criteres : les neuf du
  gel precedent, et trois sur la chaine d'ordre 2, (9) a (11), places avant le dernier :
    (1) J net : ecart-type de J < 0.2 ;
    (2) etiquette dans le domaine : n1 >= 0 et n2 >= 0 ;
    (3) site majoritaire : poids sur le site (n1, n2) >= 0.5 ;
    (4) au-dessus de dix planchers : Gamma_2D(3) > 1.33e-12 ;
    (5) etat suivi : les deux recouvrements de suivi >= 0.9 ;
    (6) cible stable : les trois Gamma_2D (k = 2, 3, 4) strictement positives, et max / min <= 2 ;
    (7) chaine du moteur definie : pas d'arret du moteur, barriere non vide ;
    (8) chaine du moteur stable : ses quatre valeurs strictement positives, et max / min <= 2 ;
    (9) chaine d'ordre 2 sans erreur ;
    (10) chaine d'ordre 2 definie ;
    (11) chaine d'ordre 2 stable : ses quatre Gamma_flux strictement positives, et max / min <= 2 ;
    (12) etiquette unique parmi les 14 : deux etats de meme etiquette sont exclus tous les deux.
  Aucun plafond sur Gamma_2D. Un etat exclu est compte avec son premier motif et ne pese pas.
  Ces criteres ne lisent aucun rapport chaine / 2D. La population est la meme pour l'ordre 1 et
  l'ordre 2. Un point est NON LISIBLE s'il est infaisable ou compte moins de 6 etats juges.

6. LA BORNE ET LE STATUT D'UN POINT
  Pour chaque etat juge : G2 = Gamma_flux de la chaine d'ordre 2 au facteur 1/16, G3 = Gamma_2D(3),
  q2 = G2 / G3. Chaque bande a sa borne B :
    PROCHE      |delta| <= 0.06           B = 1.25
    MOYENNE     0.06 < |delta| <= 0.10    B = 1.6
    LOINTAINE   0.10 < |delta| <= 0.12    B = 2
  Un etat est DANS LA BORNE si (G3 - p) / B <= G2 <= B (G3 + p), ou p = 1.33e-13 est le plancher du
  jumeau de la nuit bis. Cette marge d'un plancher sur la lecture 2D est la marge de bruit de la
  regle candidate (b) : elle vaut dix pour cent de G3 au seuil du critere (4), un pour cent a
  1.33e-11, un pour mille a 1.33e-10. Le bruit de fils mesure par machine 2 au run precedent est
  de 7.32e-14.
  Statut d'un point juge lisible : TENU si tous ses etats juges sont DANS LA BORNE ; TOMBE sinon.
  Un seul etat hors de la borne fait tomber le point : c'est voulu, et la marge est celle-la.
  D'ou viennent les bornes (section 2 (ii)) : 1.25 pour un plus grand q2 connu de 1.101 a 0.05 ;
  1.6 pour 1.512 a 0.10 ; 2 pour 1.474 a 0.12 et facteur 1, et pour le coin attendu jusqu'a 1.9.

7. LA CASCADE : LE VERDICT
  Une bande est NON LISIBLE si moins de 3 de ses 4 points sont lisibles ; TENUE si tous ses points
  lisibles sont TENUS ; NON TENUE sinon. Les bandes se lisent dans l'ordre PROCHE, MOYENNE,
  LOINTAINE, et la premiere qui n'est pas TENUE arrete la lecture :
    NON CONCLUANT D'INSTRUMENT     si une garde de la section 10 mord ;
    NON LISIBLE                    sinon, si la bande PROCHE est NON LISIBLE ;
    L'ORDRE 2 NE TIENT PAS         sinon, si la bande PROCHE est NON TENUE ;
    L'ORDRE 2 TIENT JUSQU'A 0.06   sinon, si la bande MOYENNE n'est pas TENUE ;
    L'ORDRE 2 TIENT JUSQU'A 0.10   sinon, si la bande LOINTAINE n'est pas TENUE ;
    L'ORDRE 2 TIENT                sinon.
  Ancres et temoins ne pesent pas. "N'est pas TENUE" couvre NON TENUE et NON LISIBLE : l'acte dit
  laquelle, et nomme les points et les etats.

8. LA COMPARAISON A LA CHAINE DU MOTEUR, AU PIRE ETAT
  q1 = Gamma de la chaine du moteur au facteur 1/16 / G3. A un point lisible, sur ses etats juges :
  pire ecart de l'ordre 1 = max |ln q1| ; pire ecart de l'ordre 2 = max |ln q2|. Le point est MIEUX
  si le pire ecart de l'ordre 2 est strictement plus petit que celui de l'ordre 1 ; PAS MIEUX sinon.
    L'ORDRE 2 FAIT MIEUX PARTOUT   si tous les points juges lisibles sont MIEUX ;
    PAS PARTOUT                    sinon ; NON LISIBLE si aucun point juge n'est lisible.
  Cette issue est propre ; elle n'entre pas dans le verdict de la section 7. Aucune marge ici.

9. LES ENERGIES
  Pour chaque etat juge : dE_2D = E_re - E_libre ; dE_2 = le dE de la chaine d'ordre 2 au facteur
  1/16 ; ecart = |dE_2 - dE_2D| / |dE_2D| (infini si dE_2D est nul). Un point lisible est TENU en
  energie si tous ses etats juges ont un ecart <= 0.01.
    L'ENERGIE TIENT                si tous les points juges lisibles sont tenus en energie ;
    L'ENERGIE NE TIENT PAS         sinon ; NON LISIBLE si aucun point juge n'est lisible.
  Cette issue est propre ; elle n'entre pas dans le verdict de la section 7. Plus grand ecart de la
  note sur les 243 etats : 0.0050.

10. GARDES
  G-1  le moteur lu par la sonde est au canon 82a0be882568fe0c.
  G-2  les douze points juges et les deux ancres sont presents ; aucun point inconnu ni en double ;
       chaque point present porte le role, le w2 et le facteur de la section 4, et g = facteur x
       g_du_point(w2). Les temoins sont facultatifs.
  G-3  chaque point present et faisable porte 14 etats.
  G-4  ancres : a A1 l'etat d'etiquette (7,2), a A2 l'etat d'etiquette (8,2), existe une seule fois
       et rend la lecture du run de M17 a 1e-2 pres en relatif : 2.1623273017950654e-10 et
       2.6613925716641374e-09.
  G-5  la feuille passe son selftest (160 cas) avant de lire.
  G-6  a chaque point present, la garde du moteur consignee par la sonde est sans erreur, porte le
       statut de la section 4, et ses D1 et c_max sont ceux de la section 4 a 5e-5 pres.
  G-7  la sonde qui a produit le JSON est au canon 24315c52b234319c.
  G-8  ancres : aux deux memes etats, la chaine d'ordre 2 est definie et rend les references de
       machine 1 (journal reference_ancres, sans decomposition 2D) : Gamma_flux a 1e-3 pres en
       relatif, 2.3236497766513317e-10 et 2.794344791699548e-09 ; dE a 1e-6 pres en relatif,
       0.002118984943055927 et -0.0028201377357584354.

11. LECTURES DECLAREES, SANS VERDICT
  Par point, juges, ancres et temoins : q2 et q1 minimal, median, maximal ; les deux pires ecarts ;
  le plus grand ecart d'energie ; le PALIER ATTEINT, plus petite des trois bornes 1.25, 1.6, 2 qui
  contient tous les etats juges, marge comprise, ou aucune ; le compte des exclus par motif.
  La lecture SANS MARGE (regle candidate (b)) : les etats que la marge d'un plancher a gardes DANS
  LA BORNE et que la borne nue (G3 / B <= G2 <= B G3) aurait sortis, nommes, et le verdict qu'elle
  aurait rendu.
  La loi apres coup : par point, la mediane de q2 / exp(2.87 delta^2 m_bord).
  L'arithmetique : par point, le plus grand ecart relatif entre -2 Im E et Gamma_flux.
  Ces lectures decrivent ; elles ne rejouent aucun seuil.

12. ANNONCES DE LA PLUME (machine 1), AVANT TOUT RUN
  Ce que la plume sait est en section 2. Ses attentes en sortent ; ce sont des estimations, posees
  apres le calcul de la grille.
  A-1  le verdict : L'ORDRE 2 TIENT 0.45 ; TIENT JUSQU'A 0.10 0.27 ; TIENT JUSQU'A 0.06 0.10 ; NE
       TIENT PAS 0.08 ; NON LISIBLE 0.04 ; NON CONCLUANT D'INSTRUMENT 0.06.
  A-2  (0.85) la bande PROCHE est TENUE.
  A-3  (0.80) la bande MOYENNE est TENUE.
  A-4  (0.60) la bande LOINTAINE est TENUE.
  A-5  (0.70) L2 est TENU. S'il tombe, c'est par un etat trop BAS (0.80) : le second canal.
  A-6  (0.80) L4 est TENU ; (0.65) son plus grand q2 est entre 1.5 et 1.9.
  A-7  (0.80) M4 est TENU ; (0.65) son plus grand q2 est entre 1.35 et 1.55.
  A-8  (0.85) L'ORDRE 2 FAIT MIEUX PARTOUT.
  A-9  (0.90) L'ENERGIE TIENT ; (0.70) le plus grand ecart d'energie des points juges est < 0.006.
  A-10 (0.70) un seul cote : a chaque point juge lisible, le plus petit q2 est >= 0.95.
  A-11 (0.60) la loi : a chaque point juge lisible, la mediane de q2 / loi est entre 0.93 et 1.15.
  A-12 (0.75) W1 a un etat juge hors de 1.6 ; (0.70) tous ses etats juges sont sous 2.5.
  A-13 (0.65) W2 est joue et lisible ; s'il l'est : (0.60) tous ses q2 sont sous 1.6 ; (0.80) il est
       MIEUX.
  A-14 (0.65) a chaque point juge lisible, -2 Im E et Gamma_flux different de moins de 0.05, en
       relatif. Le journal des chaines aux points donne deja 0.046 a un site voisin de M4.
  A-15 (0.95) la garde G-4 tient ; (0.93) la garde G-8 tient ; (0.97) la garde G-6 tient.
  Une annonce qui nomme un point est non jugee si ce point est NON LISIBLE.

13. CE QUE CHAQUE ISSUE ENGAGE
  L'ORDRE 2 TIENT : l'acte pourra ecrire que, sur douze points neufs, aux facteurs de 2/3 a 3/2, la
    chaine completee par son second ordre et ses sites bas a rendu la lecture de E-B a k = 3 a un
    facteur 1.25 pres pour |delta| <= 0.06, 1.6 pres jusqu'a 0.10, 2 pres jusqu'a 0.12 ; rien de
    plus. C'est un domaine, borne par bande, de cette chaine-la contre cette lecture-la.
  L'ORDRE 2 TIENT JUSQU'A 0.10, JUSQU'A 0.06 : la meme phrase, arretee a cette bande ; au-dela,
    l'acte nomme ce qui est tombe ou ce qui n'a pas ete lisible, et ne tire rien.
  L'ORDRE 2 NE TIENT PAS : la lecture de la note est retiree comme enonce general ; elle reste une
    description apres coup des 22 points connus.
  L'ORDRE 2 FAIT MIEUX PARTOUT : l'acte pourra ecrire que le second ordre est ce qui manquait a la
    chaine du moteur, aux points lus. PAS PARTOUT : il nomme les points et ne l'ecrit pas.
  L'ENERGIE TIENT : l'acte pourra ecrire que la chaine d'ordre 2 rend aussi le decalage d'energie
    des etats, a un pour cent pres, ce que les largeurs ne controlent pas. NE TIENT PAS : il nomme.
  NON LISIBLE, NON CONCLUANT D'INSTRUMENT : rien n'est appris, et l'acte le dit.
  Dans tous les cas : aucune largeur intrinseque n'est affirmee ; le moteur n'est pas modifie, et
  porter l'ordre 2 dans le moteur demanderait une nouvelle version et une decision de l'operateur ;
  les verdicts PAS DE SIGNAL de M17, NON QUALIFIE de la nuit bis, TENU EN PARTIE et LA GARDE NE
  TIENT PAS des deux gels precedents ne sont pas touches.

14. GARDE-FOUS
  Un seul run. Aucun point n'est ajoute, retire ou rejoue apres lecture ; aucune relecture sous
  d'autres bornes, d'autres bandes, d'autres criteres ou une autre population. W2 peut etre omis
  AVANT le run, par machine 2, pour une raison de machine qu'elle ecrit ; il ne peut pas l'etre
  apres une lecture. Si la certification mord, rien ne se joue et la plume corrige par hunks. Ce
  gel ne rouvre pas la piste (0) et n'en leve pas le garde-fou.

15. DECLARATIONS D'AVEUGLE
  Machine 1 n'a diagonalise le H 2D a aucun des quatorze points C1 a C4, M1 a M4, L1 a L4, W1, W2.
  Elle y a calcule la garde du moteur, la chaine du moteur et la chaine d'ordre 2, seules. Elle a
  joue la sonde aux deux ancres, points deja connus (essai a blanc joint, non opposable) : les 737
  champs de l'essai du gel precedent y sont retrouves a l'identique. Machine 2 dit dans sa
  certification ce qu'elle a joue.

16. LE CANAL
  Machine 2 certifie le gel, la sonde (par ses six hunks sur 940a21b1d562bb49 et le bloc) et la
  feuille. Si la certification rend 0 morsure, elle joue dans le meme retour : un passage de la
  sonde, puis la feuille ; elle rend le JSON de la sonde, le verdict et les journaux. La sonde joue
  les points dans l'ordre de la section 4 et ecrit son JSON apres chacun ; les temoins viennent en
  dernier, W2 le tout dernier. Duree attendue sur BOCAL4, a l'echelle de la boite puissance six et
  du run precedent (3028 secondes, sur batterie) : de l'ordre de 3100 secondes pour les quinze
  premiers points, de 1500 pour W2 seul. Si W2 ne peut pas etre joue (memoire, duree), machine 2
  l'ecrit et joue la sonde avec les quinze autres identifiants en arguments ; la garde G-2 l'admet.
  Machine 1 rejoue la feuille sur ce JSON et ecrit l'acte. Machine 1 ne joue pas la sonde aux
  points juges ni aux temoins avant d'avoir recu le lot de resultat de machine 2.

17. CE QUE CE GEL NE DIT PAS
  Il n'eprouve l'ordre 2 qu'aux facteurs de 2/3 a 3/2 (W2 a part, sans verdict), qu'a la fraction
  0.70, qu'au canal 2:1 de x^5, et que pour |delta| de 0.03 a 0.12. Il ne dit pas que la chaine est
  "qualifiee", ni qu'elle rend une largeur intrinseque : la cible reste la lecture de E-B a k = 3,
  que la piste (0) n'a pas qualifiee. Il ne calcule pas le troisieme ordre et ne dit pas d'ou vient
  le residu. Il ne dit rien d'autres degres ni d'autres canaux. Il ne prend aucun numero, n'adopte
  aucune regle, n'edite aucune piece citee (PB-1).

-- FIN gel_ordre2_chaine_EA_pre_enregistrement_v1 --
