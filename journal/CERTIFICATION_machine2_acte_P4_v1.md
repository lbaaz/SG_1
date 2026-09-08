# CERTIFICATION PAR MACHINE 2 DE L'ACTE DELTA nn P-4 -- v1
# Classe 1. Machine 2, 09/09/2026. Demandee par machine 1 : "a certifier par machine 2 en un tour
# avant depot" (en-tete de l'acte), "certification machine 2 en un tour" (manifeste du lot).
# PIECE CERTIFIEE : journal_delta_nn_P4_v1.md, empreinte convention B 0f8e283fa9499f96 (= brut),
# 39338 octets, dans le lot machine1_2026-09-08_P4_acte_v1, canon 710498cdc372ed02.
# Feuilles de controle jointes. PB-1 : l'acte n'est pas edite par machine 2. Aucun numero pris.

=======================================================================
1. RECEPTION
=======================================================================
  Canon du lot : 710498cdc372ed02. Manifeste a deux colonnes (B et brut, egales : tout est LF).
  17 lignes, 17 pieces : verifiees 17, absentes 0, ecarts 0 ; somme = lignes. ZIP : 18 membres,
  identiques aux fichiers livres hors ZIP.

=======================================================================
2. COMMENT J'AI CERTIFIE
=======================================================================
  a) PERIMETRE EXTRAIT, JAMAIS RECOPIE : les 63 empreintes citees par l'acte sont tirees de son
     texte par expression reguliere, puis cherchees dans tout ce que machine 2 detient (depot et
     entrants, fichiers nus, membres de ZIP, ZIP imbriques), en convention B et en brut.
     63 citees, 63 retrouvees, 0 non detenue. Y compris les trois JSON que machine 1 declare non
     resolus de son cote (8c40ac3a616a44e7, bcf2961cfd9d5b40, 4e5cd0419d3cc819) : machine 2 les
     detient, ce qui confirme la declaration de nn.1 -- ils sont detenus d'un seul cote.
  b) AUCUNE FEUILLE DE LECTURE RELUE, NI LA SIENNE NI LA MIENNE. Tous les comptes sont re-derives
     de (grille_repr, t_exp) du JSON du run e66549fd72f4239b, dont l'empreinte est verifiee avant
     usage. La barriere est re-derivee de la FORME FERMEE de A-2, pas lue dans un fichier.
  c) LES DEUX FENETRES DU MEME TABLEAU : t_exp porte le temps d'explosion a T = 1600 ; "explose a
     T = 400" s'en deduit par 0 < t_exp <= 400. Les comparaisons en T sont faites en INDICES
     ENTIERS de grille (regle 15), jamais sur des flottants.
  d) LE FANTOME REJOUE PAR MACHINE 2 ELLE-MEME, et non repris de machine 1 (voir 3, controle 11).

=======================================================================
3. CE QUI EST CERTIFIE : TREIZE CONTROLES, TREIZE PASSES
=======================================================================
  FORME
   1. Perimetre : 63 empreintes citees, 63 detenues, 0 manquante.
      Acte : 0 caractere non ASCII ; 0 signe pour cent ; 5 "pour cent" en toutes lettres.
  LA DERIVATION (A-2, A-3)
   2. S_b re-derives de kappa, S_b = -(delta kappa/g)^(1/(p-2)) : 7 cellules sur 7 conformes
      (-3.634241, -4.027214, -2.586702, -2.168944, -2.419780, -2.462330, -1.768674).
   3. s_CAP du degre pair, re-derives avec le terme g s^p/(p delta) : 330.56, 353.66, 422.55 --
      3 sur 3. Et la forme FAUTIVE (sans ce terme) redonne exactement 4685, 5304, 6860 : la
      faute D-P4-2 est reproduite au chiffre, ce qui la confirme comme diagnostiquee.
  L'INSTRUMENT (A-1)
   4. Noeuds Name(eta) a l'AST : 5. Usages arithmetiques BinOp(Mult, eta, d1) : UN SEUL.
   5. AST IDENTIQUE au patron d303bff2e5e55872 apres neutralisation de eta*d1 en d1 et retrait de
      la signature et de l'assert : verifie. C'est ce qui fait que "le jumeau est le patron a un
      signe pres" est une demonstration et non une inspection.
  LES COMPTES DU RUN (A-3, A-4, nn.3)
   6. JSON du run relu a l'empreinte e66549fd72f4239b : conforme.
   7. Degre pair : 480 points, 0 explosion. Conforme au theoreme et au compte de l'acte.
   8. Degre impair sous s_b (s_b de MA re-derivation, point par point) : 1512 points, 0 explosion.
   9. Site 2:1 sur G_P1 : 0/96 aux quatre colonnes signees.
  10. Garde de derive : max 5.118e-08 contre 1.1e-3 -- quatre ordres de marge ; 27 grilles sur 27
      passent ; la somme derivee "explosifs + non explosifs == 96" tombe juste 27 fois sur 27.
  LE FANTOME, REJOUE PAR MACHINE 2
  11. Rejeu independant a eta = +1 sur les memes valeurs de grille, T = 1600, quatre colonnes 2:1 :
        5|2.00|+1  10/96 -> 43/96   s*_f 0.379198 -> 0.237766   dln -0.4668 = -33.0 pas
        5|2.00|-1  10/96 -> 43/96   s*_f 0.378468 -> 0.237308   dln -0.4668 = -33.0 pas
        7|2.00|+1  10/96 -> 30/96   s*_f 0.397186 -> 0.299320   dln -0.2829 = -20.0 pas
        7|2.00|-1  10/96 -> 30/96   s*_f 0.396752 -> 0.298993   dln -0.2829 = -20.0 pas
      4 colonnes sur 4 conformes, aux six decimales, et les "-33.0 et -20.0 pas EXACTEMENT" de
      l'acte sont retrouves. Le pas de G_P1 re-derive vaut ln(1.15/0.3)/95 = 0.014144576.
      Consequence : les references fantomes de l'acte ne dependent d'aucune piece detenue d'un
      seul cote, et le cusp du fantome au site 2:1 est etabli de facon independante.
  L'INDEPENDANCE EN T ET LE FAIT NEUF (A-5, A-6)
  12. 14 seuils : |d_indice| = 0 pour 11, = 1 pour 3, > 1 pour 0. Les trois a un pas sont
      exactement ceux que l'acte nomme en R-P4-2 : 7|2.42|+1 sur G_P1 (70 -> 69), 5|1.50|+1 sur
      G_ext (63 -> 62), 7|1.50|+1 sur G_ext (62 -> 61). Aucun seuil au bord de sa grille.
  13. s*_j(1600)/s_b, re-derive avec MA barriere et MON depouillement : les onze valeurs de la
      table A-5 sont retrouvees a 5e-4 pres (1.0073, 1.0085, 1.0223, 1.0687, 1.1146, 1.2177,
      1.2357, 1.2721, 1.3276, 1.5567), et la plage [1.0073, 1.5567] est celle de l'acte.

  Les cinq predictions gelees (P4-1 a P4-5) tiennent sur les comptes ci-dessus, et la lecture
  "1.0073 / 1.0085 est le demi-pas de grille, pas un ecart" est celle que machine 2 avait deja
  portee : l'acte l'adopte en la nommant. A la maille jouee, seuil mesure et barriere derivee ne
  se distinguent pas a trois colonnes.

=======================================================================
4. UN FAIT QUI A CHANGE DEPUIS L'ECRITURE DE L'ACTE : L'ORDRE 87/88 EST TRANCHE
=======================================================================
  L'acte declare, en en-tete et en nn.1 : "plafond releve sur clone frais lbaaz/SG_1 a HEAD
  0ff330b le 08/09 = 86, premier numero libre 87 ; l'ordre 87/88 est de l'operateur".
  Ce constat etait EXACT A SA DATE. Il ne l'est plus : entre-temps, sur delegation de l'operateur,
  machine 2 a depose le delta de la sequence R3. Etat reel verifie a la certification, sur clone
  re-fetche : origin/main = d199d33, "delta 87 -- the R3 sequence enters the register", et
  journal/journal_delta_87_sequence_R3_v1.md est au registre ; aucun fichier delta_88.
    -> LE NUMERO 87 EST PRIS. Le premier libre est 88. La decision (d) de nn.6 est tranchee par
       les faits, non par un arbitrage : cet acte prend 88.
  CE POINT NE ROUVRE PAS L'ACTE, et c'est la conception de machine 1 qui l'evite : elle a ecrit
  que "le corps garde nn (le numero n'entre que dans le nom de fichier et le manifeste de depot)".
  Aucune substitution n'est donc necessaire, contrairement au delta 87 ; le fichier depose portera
  l'empreinte 0f8e283fa9499f96, celle-la meme que je certifie, et ma certification ne peut pas
  devenir caduque par le seul fait du depot. C'est la bonne facon de faire, et je la releve.
  Reste a l'operateur : le geste du depot, et lui seul.

=======================================================================
5. UNE OBSERVATION DE LIBELLE, ET TROIS FAUX ECHECS DE MA PROPRE FEUILLE
=======================================================================
  O-1  "diff textuel hors docstring de 5 lignes (2 retirees, 3 ajoutees) en trois endroits" (A-1).
       Le compte de LIGNES est exact : je retrouve 2 retirees et 3 ajoutees, 5 au total. Les
       "trois endroits" sont trois modifications SEMANTIQUES -- signature, assert, ligne du return
       -- mais elles tombent en DEUX hunks de diff unifie, la signature et l'assert etant
       adjacentes. Les deux lectures se defendent ; je releve seulement que c'est le genre de
       libelle que D-P4-3 visait deja ("3 lignes" pour 3 sites), et qu'il gagnerait a nommer sa
       voie : trois modifications, deux hunks. Aucune consequence sur A-1, que les controles 4 et
       5 etablissent independamment.
  MES PROPRES FAUX ECHECS, declares comme machine 1 declare les siens. Trois fois aujourd'hui ma
  feuille a rendu un echec qui n'existait pas :
    - mon transformateur d'AST renommait aussi la fonction IMBRIQUEE acc, d'ou un "AST different"
      qui n'etait que mon propre renommage ;
    - j'ai compare du code DEPARSE la ou l'acte annonce un diff TEXTUEL, d'ou 2/4/2 au lieu de
      2/3/2 ;
    - (la veille, sur l'archive P-4) membres comptes pour pieces, entrants confondus avec pieces
      contenues, convention B imposee a des empreintes brutes.
  La lecon que machine 1 a consignee en nn.5 a partir de mon cas vaut donc aussi pour ce
  document-ci : UN CONTROLE QUI COMPTE JUSTE PEUT ENCORE CONCLURE FAUX. Ce qui a mordu chaque
  fois, c'est de regarder CE QUE le controle comparait, pas seulement s'il totalisait bien.

=======================================================================
6. CE QUE CETTE CERTIFICATION NE COUVRE PAS
=======================================================================
  R-1  Les lectures que l'acte declare lui-meme CANDIDATES ou NON DERIVEES ne sont pas certifiees,
       et il ne le demande pas : le motif de signe de A-7 (lu au lineaire, apres coup), les trois
       predictions ordinales gelees non jouees, l'attente s_lin de A-8 (versee telle quelle, fausse
       par le haut 4 colonnes sur 11). Elles sont etiquetees CANDIDAT dans l'acte, ce qui est le
       traitement correct.
  R-2  Les trois jambes optionnelles (D, S, T = 6400) sont CONSTATEES NON JOUEES ; je le confirme
       et ne me prononce pas sur leur renvoi, qui est a l'operateur (nn.6 a, b, c).
  R-3  Le controle 6.3 (identite au bit du jumeau a eta = +1 avec le moteur depose) a ete fait par
       machine 2 le 02/09 (7d59cde9b48c0d76) et n'est pas rejoue ici comme tel ; il est toutefois
       corrobore de facon independante par le controle 11, ou mon rejeu a eta = +1 retombe sur les
       references fantomes de l'acte aux six decimales.
  R-4  L'attribution des numeros de serie aux etiquettes (D-P4-1..4, E-m2-1..3, R-P4-1..4) et
       l'etat du registre AU MOMENT DU DEPOT appartiennent a qui depose. J'ai verifie l'etat du
       registre a l'instant de cette certification (section 4) ; il peut changer d'ici la.
  R-5  Les quatre residus R-P4-1..4 restent ouverts, sans chantier, comme l'acte l'ecrit.

=======================================================================
7. AVIS
=======================================================================
  Les treize controles passent. Les derivations, les comptes, les seuils, les rapports a la
  barriere et les references fantomes sont re-derives independamment et conformes ; aucun ecart
  n'a ete trouve entre l'acte et les pieces. Le seul fait a corriger n'est pas dans l'acte mais
  dans le monde : le numero 87 a ete pris depuis qu'il a ete ecrit.
  MACHINE 2 CERTIFIE l'acte delta nn P-4 (0f8e283fa9499f96) POUR LE DEPOT, sous le numero 88,
  et sous les cinq reserves de la section 6, dont aucune ne porte sur un verdict.
  Si machine 1 amende l'acte avant depot, cette certification devient caduque : elle porte sur
  l'empreinte 0f8e283fa9499f96 et sur elle seule.
-- FIN DE LA CERTIFICATION --
