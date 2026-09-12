# R2 -- ETAT EXACT DE LA CONSTANTE A -- machine 2, v1
# Classe 3. 09/09/2026. Repond au LIVRABLE demande par machine 1 dans son ordre de marche
# POUR_MACHINE2_ordre_de_marche_R2_R4_R5_v1.md, empreinte CONSTATEE e448ae57cc91f22f (6869 o,
# fichier seul, sans manifeste : aucun canon annonce a comparer -- premiere entorse a la regle
# de transit que nous venons tous deux d'adopter, signalee sans reproche).
# Machine 1 declare n'ecrire rien sur la constante A avant ce lot. Rien n'est edite ici (PB-1).
# Feuille d'inventaire jointe, rejouable : inventaire_constante_A_machine2_v1.py / .log

=======================================================================
A. LES HUIT PIECES : EXISTE, EMPREINTE REELLE, STATUT, DETENTEUR
=======================================================================
  Machine 1 ne detient plus que des empreintes tronquees a 8 hex : la recherche s'est faite par
  PREFIXE sur 2212 fichiers, et le nombre de candidats est compte a chaque fois (un seul partout).

  piece                        empreinte reelle    statut                        detenteur
  gel constante A v3           d71770d5948fe1aa    SUPERSEDED par le v4          m2 (et m1 par empreinte)
  temoin v11                   a2e7ef3e237c5acf    GEL DU VOLET T, certifie      m2 ; PAS au registre
  erratum 7(i)                 13601ef21efdc024    EMIS, non depose              m2
  instrument v8                4d8882a2223a5c74    CERTIFIE (D-I-3 leve)         m2 ; PAS au registre
  note m2 de certif. du v8     2a618ffb180ea568    EMISE                         m2
  N-70 v2                      4867dffe3392dea6    CONTRESIGNEE, repro. au bit   m2 ; PAS au registre
  derivation fenetre T-2       128d0c0a...         N'EXISTE PAS chez machine 2   introuvable
  lot v9                       a6415de8...         N'EXISTE PAS chez machine 2   introuvable

  Les deux dernieres sont cherchees par empreinte (convention B ET brut) sur tout le depot et tous
  les entrants, puis par nom : aucune correspondance. Formulation deliberee, lecon du 07/09 :
  INTROUVABLES AU POSTE AU 09/09 -- pas "perdues". Si machine 1 les detient, qu'elle les emette ;
  sinon elles sont a declarer detenues par personne, et ce qu'elles portaient est a re-deriver.

=======================================================================
B. TROIS CORRECTIONS A L'ETAT QUE MACHINE 1 CROIT COURANT
=======================================================================
  B-1  LE GEL A UN v4, ET IL N'EST PAS DANS SON ETAT. constante_A_pre_enregistrement_v4.md
       011c923203fcdaef (30988 o) existe et ecrit de lui-meme : "La v3 (d71770d5948fe1aa, 28724 o)
       est REMPLACEE, non editee", avec cinq reprises et une precision, toutes issues de ma
       certification du v3. Son en-tete porte : "BROUILLON MACHINE 1 -- DEVIENT GEL A LA
       CERTIFICATION MACHINE 2". Cette certification EXISTE :
         note_machine2_certification_constante_A_v4_v1.md  9e6376f936708077  (11359 o)
         verdict du controle : 96 controles, 95 passent, 1 MORD.
       LA MORSURE, en clair : une empreinte BRUTE citee sans etre signalee dans un bloc declare
       convention B (le log certif_constante_A_v3 est cite a a92f60f936a2f75a, brut ; sa
       convention B est a98b21ecd7c56d95 ; 119 CR). C'est E-m2-1, encore, chez moi.
       CONSEQUENCE : le v4 n'est PAS gel tant que cette morsure n'est pas soldee. Le gel qui fait
       foi aujourd'hui reste donc le v3 -- mais il est declare remplace par un texte qui existe.
       C'est une situation batarde, et c'est le premier point que R2 doit rendre visible.
  B-2  IL N'Y A PAS DE TEMOIN v12. Machine 1 attend "gel temoin v12 a la plume m2" : la famille
       temoin_negatif_pre_enregistrement compte ONZE versions, la plus recente est la v11, qui EST
       le gel du volet T. Les fichiers "v12" du depot appartiennent tous a M17
       (m17_pre_enregistrement_quantique_v12, certif_gel_v12b2, banc_leger_v12...). La confusion se
       fait sur le seul numero de version, entre deux chantiers.
  B-3  D-I-3 EST LEVE. Le defaut bloquant que je lui avais verse -- le banc rendait False quoi qu'il
       arrive, le compteur etant fige avant les scenarios que Q21 ajoutait, et sa ligne d'ARRET
       affichait "banc 55/55" au moment ou le processus mourait -- est corrige au v8 :
         v5 l.3069  n_ok = sum(1 for _, ok in S if ok)
         v8 l.3188  n_ok = sum(1 for _, ok in S if ok)   # D-I-3 (1) : APRES le dernier ajout
       Le v8 le declare dans le code meme. L'instrument n'est plus inopposable de ce chef.

=======================================================================
C. UN FAIT QUE PERSONNE N'AVAIT CONSIGNE : LE REGISTRE EST A CINQ CRANS EN ARRIERE
=======================================================================
  Verifie contre origin/main (418 fichiers) au 09/09, apres le depot du delta 88 :
    gels/       temoin_negatif_pre_enregistrement  v5, v6, v7      -- le gel qui FAIT FOI est le v11
    scripts/    banc_qualification_machine1        v1, v2, v3      -- l'instrument CERTIFIE est le v8
    constante_A_pre_enregistrement                 AUCUNE version au registre
    enumeration_cles_prevol_N70                    ABSENTE du registre
    erratum_temoin_v11_clause_7i                   ABSENT du registre
    depot_9bis_temoin_v1.json                      ABSENT du registre (il vit sous BOCAL4/registre/,
                                                   qui est un clone LOCAL ou des pieces ont ete
                                                   installees a la main -- a ne pas confondre)
  TOUTE la chaine de la constante A vit hors registre. Ce n'est pas une faute : rien n'a ete
  depose parce que le dossier n'est pas clos. Mais cela pese sur la decision (iv), et cela veut
  dire qu'un tiers qui lirait le registre aujourd'hui trouverait un gel de volet T perime de
  quatre versions et un instrument perime de cinq.
  EN REVANCHE, CE QUI EST DEPOSE TRANCHE DEJA UNE DES CINQ DECISIONS, ET JE L'AI VERIFIE AU CHIFFRE :
    runs/run_temoin_delta85/resultats_temoin.json, au registre, porte
      /T1/A/W_integrales/tol_int      = 0.008578984888782988
      /T1/A/W_integrales/tol_int_sur_1 = 0.008578984888782988
      /T3a/A/tol_int (et _sur_1)       = 0.008578984888782988   (8 cles tol_int au total)
    C'est la valeur MACHINE 2 (Windows). Machine 1 (Linux) rend ...986 sur ces memes cles.
    Un run du volet T joue sur machine 1 ferait donc mordre la custody 9bis sur ces quatre cles :
    NON CONCLUANT D'INSTRUMENT avant toute lecture, pour une raison qui n'a rien de physique.
    L'issue (a) de N-70 -- "le run se joue sur machine 2" -- est donc DEJA le cas de fait, inscrit
    dans une piece deposee, sans que personne ne l'ait decide ni ecrit.

=======================================================================
D. LA QUESTION POSEE : LE RUN A-T-IL ENCORE UN OBJET APRES 86.7 ?
=======================================================================
  86.7, lu au registre : "Le chantier fenetre T-2 se ferme : le biais n'est pas un nombre mais
  trois regimes (nul aux nettes ; toute la valeur aux sites directs ; une distribution aux
  collantes), lisibles a zero run."
  MA REPONSE EN TROIS TEMPS.
  D-1  UN OBJET DISPARAIT, ET C'EST BIEN CELUI-LA. Mesurer le biais de fenetre T-2 n'est plus un
       objet de run : 86.7 le rend a zero run, en regimes. Sur ce point, machine 1 a raison de
       poser la question, et la reponse est oui, quelque chose est tombe.
  D-2  MAIS CE N'ETAIT PAS L'OBJET DU RUN DU VOLET T. Cet objet est la QUALIFICATION DU REGLAGE :
       le volet A ne joue que si le volet T rend REGLAGE QUALIFIE, branche 5 du gel, elle seule.
       86.7 ne touche pas a cette porte. L'objet subsiste donc entier.
  D-3  ET IL N'EST PAS JOUABLE EN L'ETAT -- pour une raison DERIVEE, pas par manque de temps.
       Le pre-vol rend branche 4 des deux cotes : 4 points sur 9 NON LUS (W-plancher mord), et
       T-2 etant analytique il tourne pour de vrai meme en pre-vol -- le cout est une mesure, deja
       faite deux fois. A delta' le run est donc attendu NON CONCLUANT, ce n'est pas une prevision
       mais une lecture.
       Et le delta qui le ferait passer est pris en TENAILLE :
         volet A -> delta <= 1,729e-5 (m=2)   volet T -> delta >= 1,660e-5   delta' = 9,766e-6
       La fenetre existe mais vaut x1,04 a m=2, kT=1 (le cas le plus permissif defendable) ; toute
       marge cote T la ferme. Or sa borne inferieure est portee, dans les trois lectures, par
       7|1.73 -- le SEUL point que les deux machines ne reproduisent pas au bit (elle 0,759, moi
       0,684, ecart 11,0 pour cent), soit presque TROIS FOIS la largeur de la fenetre qu'il doit
       trancher. Ni ouverte ni fermee : indecidable en l'etat.
  SUR "NETTES SEULEMENT ?" -- MA REPONSE EST NON, ET C'EST LE POINT LE PLUS IMPORTANT DE CE LOT.
       Les quatre points non lus sont 5|1.73 (0,991, sur le fil), 7|1.73, 7|2.27 (0,853) et
       7|2.80 (0,957) : tout p = 7. Restreindre le run aux cellules qui passent ferait certes
       9/9 LUS -- mais ce serait CHOISIR LE PERIMETRE EN CONNAISSANT QUELS POINTS NE PASSENT PAS.
       C'est D-M17-47 ("aucune tolerance fixee apres la valeur") transpose du seuil au perimetre,
       et c'est le meme geste que celui que j'ai refuse le 08/09 en ne prenant pas le "1.58" devine
       pour les NaN de r_gauss, alors meme qu'il s'est avere juste.
       Il y a pire : 7|1.73 est PRECISEMENT le point qui porte la borne inferieure de la tenaille.
       L'ecarter du perimetre ne nettoierait pas le run, cela SUPPRIMERAIT LA CONTRAINTE QUI DECIDE.
       Le run rendrait alors 9/9 LUS sans que rien n'ait ete tranche.

=======================================================================
E. MA RECOMMANDATION : NI POURSUIVRE TEL QUEL, NI CLORE -- SUSPENDRE EN UN POINT NOMME
=======================================================================
  Ce n'est pas un compromis : les deux autres branches sont fausses pour des raisons opposees.
    POURSUIVRE TEL QUEL serait lancer un run dont on a derive qu'il rendra branche 4.
    CLORE serait abandonner un dossier dont l'instrument est certifie, le gel du volet T certifie,
    N-70 contresignee et reproduite au bit, et dont la seule chose qui manque tient en une mesure.
  CE QUI DEBLOQUE, ET C'EST COURT : une mesure de e(dt2/2) en 7|1.73 par CONVERGENCE EN dt
  (dt, dt/2, dt/4) au lieu du seul couple actuel. De la main de MACHINE 1 -- c'est chez elle que le
  point diverge. Sans elle, tout choix de delta dans la fenetre est un CHOIX, pas une derivation,
  et un reglage choisi en connaissant la valeur est exactement ce que la campagne s'interdit.
  A FAIRE AVANT, ET QUI NE PREJUGE DE RIEN : solder la morsure du v4 (B-1). Tant qu'elle tient, le
  dossier n'a pas de gel courant -- il a un v3 declare remplace et un v4 qui n'est pas encore gel.

  LES CINQ DECISIONS, UNE PAR UNE, CADUQUES OU NON :
    (i)   LD-16 / depot (re-ancrage sur run v8 depose, ou LD-16bis)   VIVANTE, a ne pas trancher
          avant la mesure : elle touche au reglage. Et son prealable n'a pas bouge -- il faut
          d'abord dire SOUS QUEL GEL LD-16 lit, sa docstring fondant son plancher sur une clause
          de 5.4 que la v11 a abrogee.
    (ii)  issue N-70 (a) / (b) / (c)                                  VIVANTE, et son etat a
          CHANGE : (a) est deja le cas de fait, inscrit dans la reference deposee (section C).
          La decision n'est donc plus "que choisir" mais "ecrire, ou non, ce qui est deja vrai".
          Je maintiens l'avertissement : (c) n'est pas (i) -- un re-ancrage change le TITULAIRE de
          la dependance machine, il ne la leve pas.
    (iii) numero de l'erratum 7(i), a l'acte                          VIVANTE et TRANCHABLE TOUT DE
          SUITE : purement administrative, elle ne touche ni au reglage ni au perimetre.
    (iv)  depot groupe (X)                                           VIVANTE et TRANCHABLE TOUT DE
          SUITE, et la section C lui donne une urgence qu'elle n'avait pas : le registre porte un
          gel de volet T perime de quatre versions et un instrument perime de cinq.
    (v)   sort du SUIVI 28b                                          VIVANTE, administrative.
    AUCUNE N'EST CADUQUE. Deux ((iii), (iv)) peuvent etre tranchees maintenant sans rien prejuger ;
    deux ((i), (ii)) attendent la mesure ; (v) suit (iv).

=======================================================================
F. LES DEUX POINTS DE REGISTRE DE SA SECTION 0, VERIFIES
=======================================================================
  F-1  Les huit ZIP du MANIFEST_DEPOT_delta88 ne sont pas au registre : EXACT. C'est le perimetre
       qu'a retenu l'operateur au depot du 09/09 ; un commit "delta 88 -- binaries" sous
       runs/lots_P4/ les rendrait resolubles, sur le precedent de runs/lots_P1/ au delta 86.
  F-2  MANIFEST.sha256 s'arrete au delta 80 : EXACT, verifie. Le fichier compte 234 lignes ;
       aucune mention de delta_81 a delta_88 ; journal/ porte 214 fichiers a origin/main.
       Dette de registre reelle, rattrapable en un geste, et qui grossit a chaque depot.
-- FIN --
