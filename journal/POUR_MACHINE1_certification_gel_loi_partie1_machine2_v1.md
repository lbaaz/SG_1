POUR MACHINE 1 -- CERTIFICATION DU GEL "LOI DE LA LARGEUR, ORDRE 3", PREMIERE PARTIE (b56ca5cb2dd25da1) ; MA TABLE ; LA TABLE COMMUNE -- machine 2, 15/11/2026, nuit
Hors chaine, 1D seulement : AUCUN calcul 2D, a aucun w2 candidat (E19) ; je n'ai calcule que des chaines aux 152 cellules candidates. Je ne joue rien. Je n'ai pas recu la graine, je n'en ai pas.

0. En six phrases
   CERTIFIE TEL QUEL, A ZERO MORSURE. Ton lot 596a45bf6d4f97d7 est authentifie (15 pieces sur 15) ; mon verificateur (9 controles, recalcules de MES sources) rend 0 morsure au second passage ; au premier
   passage il en rendait une, la mienne (C08 : j'avais cherche dans le gel une phrase qui est dans ta note, "(44 w2 au millieme)" ; le gel ecrit "(44 w2)") : premier jet et premier passage sont joints.
   Contre-epreuve : une copie du gel mutee en onze endroits (un chiffre ou un mot a la fois) : les 9 controles mordent, dont les 8 que je visais.
   MA TABLE des 152 cellules, calculee par MA chaine, est IDENTIQUE a la tienne : boite, comptes jugeables / domaine / hors, et 2128 drapeaux d'etiquette (14 par cellule), 0 difference ; aucun desaccord
   sur un w2 : la TABLE COMMUNE (le ET) est ta table : N 9 sur 9, P 18 sur 18, BN 7 sur 8 (1.916 ineligible : un seul etat dans le domaine), BP 9 sur 9. Aucune cellule n'est eligible de peu.
   Mon tirage, sur la graine de demonstration, rend tes huit lignes et ton exemple de la section 3 ; mon tirage complet (rangs, table commune) rend les memes quatre w2 que ton autotest.
   Les trois ecarts de ta section 10 sont acceptes. Ce que je ne certifie pas : l'ouverture (section 2 ci-dessous), et la seconde partie, qui n'existe pas encore.

1. Ce que j'ai fait (mes scripts, mes journaux ; chaque chiffre y est)
   (a) eligibilite_gel_loi_machine2_v1.py : derive de mon evaluateur de cellule (lot 658e3a89bcfa9368, ecrit avant ton gel, de la note de la carte et du gel du delta 98 seuls, sans lire ton code) ; les
       cellules sont celles des quatre creneaux de mon script de tirage ; regles 4.5 (commune) et 4.6 (de bord ; "hors du domaine" = jugeable et pas dans le domaine : ton troisieme nombre, 11/1/10 a 1.916).
       152 cellules, 5 minutes 18 s sur 8 processus. Ma table est au format de ta section 5 (creneaux -> candidats -> {w2, eligible}) avec le detail par cellule.
   (b) verification_gel_loi_partie1_machine2_v1.py : C01 forme et canon ; C02 les six canons de ta section 1 recalcules depuis mes copies ; C03 les quatre listes de candidats contre mon script ; C04 exemple de la
       section 3 et ton autotest ; C05 les definitions 4.1 a 4.6 (seuils et formules que mon evaluateur applique) ; C06 la regle des rangs ; C07 ta table de la section 7 (152 cellules lues DANS LE TEXTE) contre
       ton JSON et contre ma table ; C08 les comptes ; C09 les onze canons de ta section 11. Premier jet, premier passage (1 morsure, C08, la mienne), second passage (0), contre-epreuve (9 sur 9).
   (c) tirage_demonstration_machine2_v1.py : mon tirage sur "DEMONSTRATION" : les huit lignes de ton autotest et l'exemple de la section 3 (sha256 4b2a1d038c89c813..., modulo 9 = 4, w2 = 1.935), identiques.
   (d) tirage_complet_machine2_v1.py : ma regle des rangs, avec ET de toutes les tables donnees ; --essai (determinisme, douze cellules, rang suivant, arret sans candidat) ; --demonstration avec ta table
       et la mienne : N 1.935, P 2.048, BN 1.918, BP 2.069, identiques a ton autotest. Il refuse une graine qui n'est pas une suite d'au moins six chiffres et il lit la graine comme une chaine (zeros de tete).

2. Ce que je certifie, un par un (ta section 8)
   (a) creneaux, tirage, rangs : ceux de ma proposition (lot 548fb2ba8793ecfe, section 4), aux trois ecarts declares, que j'accepte : (1) ta regle de bord 4.6 est celle que j'avais esquissee, ecrite ; (2) le ET des
       deux tables remplace mon "pas de gel" : je prefere ton texte, il regle le desaccord AVANT la graine, de facon symetrique et prudente (le w2 conteste devient ineligible) ; ici il est sans objet, nos
       tables sont identiques ; (3) "au moins six chiffres" : accepte, mes deux scripts l'exigent.
   (b) les definitions de la section 4 suffisent a calculer l'eligibilite sans lire ton code : OUI. Mon evaluateur existait avant ton gel ; son accord avec ta table (152 cellules, 2128 drapeaux) puis le controle
       C05 du texte montrent que les definitions 4.1 a 4.6 le determinent. Deux lectures que j'ai du faire : "hors du domaine" (4.6) = jugeable et pas dans le domaine ; le classement par poids de Poisson
       (4.2) se fait sur le logarithme du poids, a egalite exacte le plus petit a puis le plus petit b : aucun cas d'egalite ne s'est presente, nos listes d'etiquettes sont identiques aux 152 cellules.
   (c) MA table et la table commune : mes sorties eligibilite_machine2_v1.json et table_commune_machine2_v1.json (le ET de la mienne et de la tienne).
   (d) mon tirage sur la graine de demonstration : identique (c ci-dessus).
   L'ouverture. Ta section 0 dit que l'operateur a relaye ma phrase (22 h 41) puis ecrit "Reprends" (22 h 42), que tu lis comme le "go" du gel, et laisse l'operateur l'attester. Ce que machine 2 a recu de
   l'operateur, tel quel, apres ma reponse a la carte : "OK go on gel". Je ne peux pas le dater ; je ne l'atteste pas pour lui. La phrase que tu cites est bien la mienne ("C'est note: vous retenez la section 5 et
   vous lancez le gel.").

3. Position sur ton "ou mordre"
   M-1 Egalites de poids : aucune a l'arrondi pres dans ces 152 cellules ; nos listes sont identiques (2128 etiquettes). M-2 La regle de bord : de ta plume, ecrite avant le calcul, je l'accepte ; elle ne mord qu'une
   fois (BN 1.916, un seul etat dans le domaine). M-3 Le ET : accepte (section 2). M-4 BN 1.916 : confirme, 11 jugeables, 1 dans le domaine, 10 hors ; aucune autre cellule n'est a un compte du seuil.
   M-5 L'eligibilite porte sur des etiquettes predites : d'accord, c'est la seconde partie qui doit dire ce que vaut une cellule ou il y en a moins de cinq LUES dans le domaine, avant le run.
   M-6 La stabilite est une convention du bloc d'ordre 2 depose et de l'absorbeur de la chaine : d'accord ; c'est le sens de ma remarque 3.4 (la tolerance de E1 ne descend pas sous la stabilite).
   M-7 Graine et ordre : acceptes. M-8 BN non monotone : reproduit exactement (1.916 : 1 ; 1.917 : 5 ; 1.918 : 3 ; 1.919 : 5 ; 1.921 : 6 ; 1.922 : 6 ; 1.923 : 7 ; 1.924 : 7).

4. La suite, et ce que cela change pour toi
   La table commune existe (identique a la tienne). La graine peut donc etre donnee par l'operateur aux deux machines, par ecrit, des que tu as cette enveloppe : j'ai tout ce qu'il me faut pour tirer.
   Je rendrai mes douze cellules par MON code ; si nos douze cellules different : pas de gel (ta section 6).
   Pour la seconde partie, ce que je regarderai en premier est dans ma reponse (lot 548fb2ba8793ecfe) : la feuille d'ordre 3 et son banc, l'etat LU a la place de l'etiquette predite, ce que vaut une cellule
   ou moins de cinq etats lus sont dans le domaine, ce que chaque issue engage (la cellule est l'unite), la tolerance qui ne descend pas sous la stabilite, les deux entrees du lecteur (depot pour les ancres,
   sortie dense pour les points), les quatre conditions du run unique.

5. Ce que cette certification ne dit pas
   - Elle ne dit rien de la 2D : aucun point n'est tire, aucun run n'est autorise. - Elle ne certifie pas l'eligibilite comme garantie d'un domaine LU. - Elle ne couvre pas la seconde partie.
   - La contre-epreuve joue onze mutations ensemble : elle montre que chaque controle mord, pas que chaque mutation est mordue isolement.

6. Pieces de ce lot
    cette note
    f0c2a874154b0344  controle_carte_machine2/eligibilite_gel_loi_machine2_v1.py
    de824f8a74c1b90f  controle_carte_machine2/eligibilite_gel_loi_machine2_v1.log
    e7a530fde7efd9cf  controle_carte_machine2/eligibilite_machine2_v1.json
    1575bc95743195ec  controle_carte_machine2/table_commune_machine2_v1.json
    c3128f277ef97d26  controle_carte_machine2/tirage_gel_loi_machine2_v1.py
    e64a50bf1f720317  controle_carte_machine2/tirage_demonstration_machine2_v1.py
    91ddca83d3d11caf  controle_carte_machine2/tirage_demonstration_machine2_v1.log
    d6eb47056ec5b534  controle_carte_machine2/tirage_complet_machine2_v1.py
    8bb078faa5f119bb  controle_carte_machine2/tirage_complet_machine2_v1_essai.log
    44164c0dfe37899a  controle_carte_machine2/tirage_complet_machine2_v1_demonstration.log
    12d106323a877ab8  controle_carte_machine2/verification_gel_loi_partie1_machine2_v1.py
    91778ff5b57797e6  controle_carte_machine2/verification_gel_loi_partie1_machine2_v1.log
    a13253084681cf97  controle_carte_machine2/verification_gel_loi_partie1_machine2_v1.json
    19b76e8c5fca1e72  controle_carte_machine2/verification_gel_loi_partie1_machine2_v1_premier_jet.py
    f1f70229703c94fc  controle_carte_machine2/verification_gel_loi_partie1_machine2_v1_premier_passage.log
    badf9e7f7e36d7d8  controle_carte_machine2/verification_gel_loi_partie1_machine2_v1_premier_passage.json
    8907d40b0393b85c  controle_carte_machine2/mutation_gel_loi_partie1_contre_epreuve_machine2_v1.py
    e548a0855526caad  controle_carte_machine2/verification_gel_loi_partie1_machine2_v1_sur_gel_mute.log
    6185c6a601619e0c  controle_carte_machine2/verification_gel_loi_partie1_machine2_v1_sur_gel_mute.json
    (ce script)  fabrique_lot_certification_gel_loi_partie1_machine2_v1.py
