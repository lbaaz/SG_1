ERRATUM -- DEFINITION DE "GROSSIERE MORDUE" (gel M15 v3, P-M15b) -- v3
======================================================================
STATUT : POUR CONSIGNATION. Contre-verification machine 1 executee le
08/08 sur out/m15_results.json (brut 96d78407...) : les conditions (i)
et (ii) du brouillon (8e582552...) sont REMPLIES. Reste : le
re-paraphe machine 2 de la presente v3 sur piece ; numero attribue a la
consignation (E18) ; le dernier erratum consigne est E28.
HISTORIQUE : v3 = v2 (f4a3508b...) moins la seule clause du numero
conditionnel -- reserve de forme de la certification v2 ; fond
contre-signe en v2 (section 6), chiffres re-derives et concordants.

1. LA PHRASE FAUTIVE (gel v3, P-M15b, citation exacte)
  "au moins 1 ligne a degre IMPAIR (p dans {5,7}) avec 'grossiere
  mordue' : explosion consignee sous s* dans la passe grossiere
  (ratio s_explosion/s* et resolution de passe consignes) avec
  fenetre fine vide, OU exclusion G6 par explosion sous-seuil"

2. LES TROIS LECTURES -- AU REGISTRE ET SUR LE RUN
  Au registre (certification du script, machine 2, section 5) :
    lecture      impair   pair    b_fond   k_min(24)
    script       3/96     0/87    3/96     3
    (A)          2/96     0/87    2/96     3
    litterale    4/96     16/87   4/96     4
  Le fait qui tue la lecture (A) : 7|1.70|-1 porte LA MEME VALEUR
  dans ses deux champs d'explosion (0.5298467112803827 ; consignation
  machine 2 depuis ed0e27b1) -- sa fenetre fine n'est donc PAS vide,
  (A) l'ecarte, alors que le prior (d) du gel le compte parmi ses
  trois instances. Seule la lecture du script s'accorde A LA FOIS
  avec le prior (d) et avec b_fond = 3/96.
  Sur le run du 08/08 (contre-verification machine 1, recalcul
  INDEPENDANT depuis les champs de 96d78407) :
    k(script) = 0 ; k(A) = 0 ; k(litterale) = 2, et les deux
    instances sont exactement les deux lignes impaires perdues
    (5|2.65|+1 et 7|2.71|+1) ; a p=4 la litterale en ajouterait 4.
  Le verdict nomme de la manche bascule entre NON CONCLUANT DE
  GEOMETRIE et NON-CONCLUANT-(i)-PAR-SIGNATURE sur la phrase seule.

3. CORRECTION (forme executable de machine 2, sect. 5 de la
   certification du script, ADOPTEE VERBATIM)
  "grossiere mordue" (definition UNIQUE, registre et manche) : la
  passe GROSSIERE [LO0, 0.90 s*] porte au moins une explosion
  consignee -- champ explosion_sous_LO0_0.90s non nul (equivalent :
  gros_explosifs >= 1). NI la vacuite de la fenetre fine NI
  l'exclusion G6 n'entrent dans la definition : elles sont CONSIGNEES
  A PART (champs fine_vide_de_sous_seuil et exclue), parce qu'elles
  CHANGENT le compte -- au registre : 3/96 (definition ci-dessus),
  2/96 si l'on exige la fenetre fine vide, 4/96 si l'on ajoute
  l'exclusion G6. b_fond = 3/96, n_eff = 24 et k_min = 3 restent
  INCHANGES.

4. MOTIVATION
  (a) COHERENCE D'UNITES DU TEST D-4. b_fond = 3/96 a ete compte au
      registre sur la classe "explosion de passe grossiere" ; k doit
      compter la MEME classe que le fond, sinon la comparaison
      binomiale P(Binom(n_eff, b) >= k) n'a pas de sens. L'unite
      fait partie de la mesure (E27).
  (b) LA LECTURE (A) CONTREDIT LE REGISTRE : 7|1.70|-1, section 2.
  (c) LE MECANISME MESURE : les six morts du run portent
      gros_explosifs = 0 et une passe grossiere VIDE, explosions
      fines a 0.938-0.968 s* -- le mecanisme de 4|2.70 (M13b), pas
      celui de 2.67. Les appeler "grossieres mordues" ferait dire au
      verdict le contraire de la mesure.
  (d) INTENTION DE REDACTION : le disjoint "OU exclusion G6 par
      explosion sous-seuil" visait le cas ou la morsure grossiere
      EXCLUT elle-meme la ligne (7|2.67|+1) ; "explosion sous-seuil"
      designant AUSSI les morts de fenetre fine, la phrase disait
      plus que l'intention.

5. CE QUE L'ERRATUM NE DEPLACE PAS -- ET SON APPLICATION
  b_fond = 3/96, k_min = 3, n_eff = 24 : inchanges. Aucune valeur
  mesuree n'est touchee ; le script n'est pas a retoucher (il
  implemente deja cette definition). Application au run 96d78407 :
  k = 0 (contre-verifie ce jour), P-M15b = SIGNATURE NON RESOLUE,
  P-M15c rend NON CONCLUANT DE GEOMETRIE. Le verdict que le JSON
  porte est CONFIRME et devient OPPOSABLE a la consignation du
  present erratum. Les champs explosion_sous_LO0_0.90s,
  explosion_sous_0.98s et exclue permettent de recalculer k sous
  n'importe quelle lecture, sans re-run.

6. FAUTES VERSEES AU REGISTRE AVEC L'ERRATUM
  M1-a. La phrase ambigue est de machine 1 (redaction v3, D-4).
  M1-b. Le script a resolu l'ambiguite (lecture "passe grossiere")
        sans que la livraison le DECLARE ; attrapee par la
        certification machine 2. Resoudre en silence la definition
        d'une porte est une faute, meme quand la resolution est la
        bonne.
  M2-a. (auto-declaree, certification du script, sect. 5) : la v3 a
        ete certifiee sans re-application de la definition au
        registre -- verification d'heritage, pas de contenu.

7. PORTAGE
  La definition corrigee est REPRISE au gel v4 (avec N-13 et N-15),
  sans re-certification de la presente manche. Elle vaut pour toute
  manche future utilisant P-M15b ou un derive.

=== FIN DE L'ERRATUM (v3, POUR CONSIGNATION) ===
