DOSSIER D'ARBITRAGE POST-M15 (machine 1, 2026-08-09) -- v1
CANDIDATES 15 ET 16 . COLLISION S42.3/S43 . INTRANTS DU GEL v4 . REPORT
=======================================================================
Citations transcrites en ASCII (accents supprimes) ; les sources citees
font foi par empreinte. Pieces au perimetre machine 1, empreintes
RE-DERIVEES ce jour (sha256, 16 hex) :
  m15_erratum_grossiere_mordue_v3.md   16c6d86e389da2a9  == consignee 51.1
  journal_delta_42_reconciliation_M11  d6602770d63b9e52  == registre (S42)
  journal_delta_51_cloture_M15         7c48f060b7b04a46  copie projet ;
    empreinte certifiee au message de livraison machine 2, a rapprocher.

0. OBJET, PERIMETRE, DECISIONS ATTENDUES
   File 51.9 (journal delta 51, MANCHE M15 CLOSE) : le present dossier
   couvre les items hors manche qui conditionnent le prochain gel.
   Machine 1 PROPOSE ; l'arbitrage ADOPTE (51.7). Cinq decisions :
     D1  regle candidate 15 : adoption / rejet / amendement
         (D1b optionnel : corollaire du fait 51.3.e, texte en 1.4)
     D2  regle candidate 16 : adoption / rejet / amendement
     D3  collision S42.3/S43 : option O1 / O2 / O3 (section 3)
     D4  fourniture des pieces P1-P3 du gel v4 (section 4)
     D5  report explicite du bilan des fautes M8-M11 (section 5)
   Rien ici n'est une mesure : aucune porte, aucune attente chiffree.
   Hors perimetre, inchanges : trilemme du site (decision de manche,
   ITEM 3 a deriver), branche quantique (specification d'estimateur),
   dossier externe (Held), canaux des vecteurs synthetiques (7.4) si
   banc rejoue.

1. CANDIDATE 15 -- COMPARAISONS DE BORD EN ARITHMETIQUE EXACTE
1.1 Texte enregistre (extraction CAMPAGNE_etat_complet_2026-08-02,
    Partie VI ; identique au SUIVI du 02/08) :
      "Toute comparaison pouvant basculer sous epsilon machine --
       egalite OU inegalite au bord -- s'evalue en arithmetique
       EXACTE quand les entrees sont exactes, a tolerance declaree
       sinon."
1.2 Dossier au 02/08, six instances : trois du cycle M12 (selection
    pilote, pseudo-tie, filtre de nouveaute) ; trois de l'artefact
    primaire (d et d/r en float(Fraction), 13/13, avec contrefactuel
    division -- 7/13 a 1 ulp, l'ex aequo 5/3 tenu ; double temoin
    d'indice 40, <= 2 ulp, verdict par l'indice ; ex aequo Spearman
    detectes en exact et verifies au bit).
1.3 Pieces M15 versees au dossier ce jour :
    (a) fait d'environnement 51.3.e -- pow numpy non symetrique a la
        negation au dernier ulp, ET environnement-dependant (False
        conteneur machine 1, True BOCAL4) ;
    (b) pratique de banc 51.5 -- trois comparaisons cassees par une
        hypothese d'ORDRE dans le meme cycle (matiere adjacente :
        canonicaliser avant de comparer, toujours).
1.4 D1b (optionnel ; texte fixe a l'acte si retenu) : eriger 51.3.e
    en corollaire normatif -- "toute garde numerique AU BIT portant
    sur la sortie d'une fonction de librairie est proscrite : garde
    structurelle ou garde mesuree a tolerance declaree, rien entre."
    51.3.e le consigne deja comme fait ("proscrites de fait") ; le
    corollaire le rendrait opposable aux gels futurs.
1.5 Effet operationnel si D1 adoptee : les comparaisons de bord des
    scripts futurs s'ecrivent en Fraction / entiers quand les entrees
    sont exactes, a tolerance declaree sinon ; le selftest porte un
    controle nomme. Aucune retro-action : les verdicts passes
    tiennent sur leurs gardes telles que gelees.
1.6 Position machine 1 : ADOPTION, texte 1.1 inchange. D1b : propose
    sans insistance -- le fait consigne suffit peut-etre au registre.

2. CANDIDATE 16 -- q_L DERIVE PAR DEGRE, PLUS PETIT DOMAINE
2.1 Texte propose (extraction journal delta 51.7, verbatim) :
      "Le q_L se derive sur le plus PETIT domaine contenant le
       programme, par DEGRE ; si le registre y porte n <= 3 lignes,
       le q_L n'est pas derivable et la faisabilite se juge sur la
       borne."
2.2 Origine et soutiens (51.7) : proposee machine 2 (remise du run
    M15, sect. 2) ; soutenue machine 1 (precision par-degre). La
    motivation detaillee et la justification du seuil "n <= 3" sont
    a la remise (piece machine 2) : A CITER A L'ACTE de consignation.
2.3 Effet operationnel si D2 adoptee : le dimensionnement d'attrition
    de toute manche future -- dont la branche "crible 48.3" du
    trilemme -- derive son q_L par degre, sur le plus petit domaine
    contenant le programme ; a n <= 3 lignes au registre sur ce
    domaine, pas de q_L : la faisabilite se juge sur la borne, dit
    d'avance au gel.
2.4 Position machine 1 : ADOPTION (soutien deja consigne). Point de
    redaction pour l'acte : "n <= 3" est une constante de METHODE
    declaree, pas un seuil de garde -- la regle 13 ne s'y applique
    pas ; consigner neanmoins la justification du 3 (remise, cf 2.2).

3. COLLISION S42.3 / S43 -- DEUX CONTENUS SOUS LE NUMERO E27
3.1 Les deux actes.
    (a) S42.3 = section 42.3 du journal delta 42 (27/07, machine 1,
        delta d6602770) : "ERRATUM E27 -- le gel exige une
        consignation que le script ne produit pas". Instance M11 :
        min(s explosif)/s* rendu None sur 26 des 32 lignes ; lecon
        nommee : controle de COUVERTURE gel -> JSON au selftest.
        Texte integral au perimetre machine 1 (fichier projet).
    (b) S43 = journal delta 43 (a94fd607), cite au registre comme
        "S43 E27". Contenu-souche tel que les pieces certifiees le
        citent depuis : "l'unite, la convention ET la resolution
        font partie de la mesure" (etat complet 02/08, Partie X.3) ;
        discipline associee : ne pas comparer, plutot que comparer
        avec reserve (delta 45.3) ; correctif structurel implemente
        dans l'artefact M12 (resolutions par ligne). Texte integral
        NON detenu par machine 1 (transcripts non montes).
3.2 La collision : deux actes de consignation, deux contenus
    distincts, un seul numero. E18 attribue le numero A L'ACTE, sans
    reservation -- il ne dit pas lequel des deux actes tient le
    numero quand le second l'a repris. Tout le registre POSTERIEUR
    cite E27 au sens (b) : etat complet X.3, delta 45.3, delta 46,
    suivis, et jusqu'a l'erratum consigne au delta 51 (motivation,
    sect. 4a : "L'unite fait partie de la mesure (E27)").
3.3 Options.
    O1 (usage) : E27 = le principe (b). Le contenu (a) est
       requalifie "faute de couverture M11, instance" et recoit,
       s'il doit porter un numero propre, le prochain numero libre
       AU MOMENT de sa consignation -- numero non ecrit ici (51.5,
       faute M1-c). Cout : une consignation ; toutes les citations
       existantes restent justes.
    O2 (chronologie stricte) : E27 = (a), acte du 27/07, anterieur ;
       le principe (b) est renumerote. Cout : cascade d'errata sur
       toutes les citations posterieures (etat complet, deltas
       45-46, delta 51, suivis). Exige le texte integral de S43 sur
       table avant decision.
    O3 (unification) : E27 = UN erratum a deux volets -- instance
       fondatrice (a) + principe general (b) ; texte canonique
       designe = S43 ; S42.3 requalifie "instance fondatrice, meme
       numero", renvoi croise au registre. Cout citationnel nul ;
       aucun numero nouveau ; une consignation d'arbitrage suffit.
3.4 Position machine 1 : O3, sinon O1. O2 deconseillee : cout de
    cascade sans gain epistemique ; E18 protege contre la
    RESERVATION de numeros, pas contre l'unification a posteriori de
    deux actes de meme souche. Caveat : machine 1 ne detient pas
    S43 ; si la collision porte sur autre chose que le numero et le
    contenu-souche, la presente section s'amende au premier message
    de machine 2, avant toute decision.
3.5 Quel que soit le choix : l'acte d'arbitrage se consigne au
    journal (delta suivant, numero a l'acte), avec renvoi croise
    S42.3 <-> S43.

4. GEL v4 D'HERITAGE -- INTRANTS ET METHODE
4.1 Tenu par machine 1 : la definition unique "grossiere mordue"
    (erratum E29, fichier 16c6d86e re-verifie ce jour, section 3,
    forme executable de machine 2 adoptee verbatim ; portage
    prescrit par sa section 7 : "REPRISE au gel v4 (avec N-13 et
    N-15), sans re-certification de la presente manche").
4.2 Requis de machine 2 (un texte consigne s'EXTRAIT, ne se retape
    pas -- 49.5, regle 12 ; transcripts non montes cote machine 1) :
    P1  le FICHIER source du gel M15 v3 (e41f4da3), tel que certifie
        (ASCII/LF, bloc = fichier, convention B) ;
    P2  le texte consigne de N-13, avec l'empreinte de son acte ;
    P3  le texte consigne de N-15, idem. (N-14 est cite 51.3.d
        "exerce en reel" ; si N-13/N-14/N-15 partagent une piece,
        une seule fourniture suffit.)
4.3 Methode annoncee : gel v4 = gel v3 + section de portage
    (definition E29 + N-13 + N-15), par patchs assertes sur source
    (src.count(ancien) == 1, sinon sys.exit) ; empreinte convention
    B ; certification croisee AVANT tout usage par une manche.
    Aucun re-parcours de la manche close (E29, sect. 7).
4.4 Question a trancher a l'acte : les regles 15/16, si adoptees,
    entrent-elles au gel v4 ou au registre maitre ? Position
    machine 1 : registre maitre (les regles 1-14 y vivent ; le gel
    herite des definitions et normes de MESURE -- E29, N-x).

5. BILAN DES FAUTES M8-M11 -- REPORT
   Acte propre, numero attribue au moment de sa consignation (E18),
   hors du present perimetre pour ne pas meler arbitrage de regles
   et consignation de fautes. Le report explicite etait deja la voie
   du SUIVI 02/08 (sect. 7). Position machine 1 : D5 = report,
   consigne comme tel au delta d'arbitrage.

6. APRES LES DECISIONS
   A reception de D1-D5 et des pieces P1-P3 : machine 1 consigne
   l'acte (journal delta, numero de delta a l'acte), livre le gel v4
   en patchs assertes + fichier assemble + empreinte convention B,
   et la file 51.9 se reduit a : trilemme du site (ITEM 3 a
   deriver), branche quantique, dossier Held, 7.4 conditionnel.

=== FIN DU DOSSIER (v1, POUR ARBITRAGE) ===
