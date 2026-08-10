PRE-ENREGISTREMENT M6 -- LA LOI DES PORTEURS ET LA DECROISSANCE DU CANYON
(gele avant l'ecriture de toute ligne de code ; bloc ASCII, canonique NFC+LF)

QUESTION (issue de S17 et de E15)
--------------------------------
M5 a etabli que le plafond classique a w2 = 2 est resonant a p=3 (Q = 57.5) ET
a p=5 (Q = 4.4), et que ce qui distingue le cubique est la PROFONDEUR du canyon,
pas sa nature. H-PROFONDEUR (post-hoc, etiquetee) fait dependre le signe de
rho(T,K_p) de ce qui ordonne la carte de K : canyon profond => resonances ;
canyon plat => fond. Deux jambes restent non testees :
  (1) la loi des PORTEURS : le canyon existe-t-il exactement quand un monome
      porteur de premier ordre existe ?
  (2) la DECROISSANCE : la profondeur tombe-t-elle avec p ?

DERIVATION PREALABLE (algebre, non testee ici -- c'est un fait, pas une porte)
----------------------------------------------------------------------------
V = (g/p)(x1+x2)^p = somme de monomes c x1^a x2^b avec a+b = p.
x1^a engendre les harmoniques k w1 avec k = a (mod 2), |k| <= a ; idem pour l.
La resonance a trois ondes 2w1 - w2 = 0 exige (k,l) = (2,1) : a PAIR, b IMPAIR,
donc a+b IMPAIR. Meme condition sur la force : dV/dx2 doit contenir (2,0)
[b-1 pair, a pair] et dV/dx1 doit contenir (1,1) [a-1 impair, b impair].
=> PORTEUR DE PREMIER ORDRE EXISTE SI ET SEULEMENT SI p EST IMPAIR.
p=3 : x1^2 x2. p=5 : x1^4 x2, x1^2 x2^3. p=7 : x1^6 x2, x1^4 x2^3, x1^2 x2^5.
p=4, p=6 : AUCUN. (Ceci n'est PAS H-PARITE, refutee en M3 : H-PARITE portait
sur le signe de rho(T,K), pas sur l'existence de porteurs.)
La quantite testee est donc l'implication CANYON <=> PORTEUR, pas la parite.

STATISTIQUES (auto-normalisees -- lecon S17-bis)
-----------------------------------------------
D(p,d) = sqrt( s*(2-d) * s*(2+d) ) / s*(2)
  Profondeur du canyon par detuning fin. La moyenne geometrique des voisins
  annule au premier ordre la tendance de fond log-lineaire en w2 : D = 1 pour
  un s*(w2) sans creux local, quelle que soit sa pente. Aucun ajustement.
Q1(p) = s*_abl(x1^(p-1) x2) / s*_abl(x1 x2^(p-1))
  Profondeur par chirurgie, variante MONO-MONOME, definie pour TOUT p, egale a
  Q de M5 a p=3, comparable d'un degre a l'autre. Paire miroir, coefficients
  strictement egaux (binomial C(p,1)/p = g des deux cotes). s*_full s'annule.

VALEURS DE REFERENCE (deja mesurees, machine 2, m5_results.json, S17-bis)
  D(3, 0.05) = 3.628   D(3, 0.10) = 15.369   Q(3) = 57.5
  D(5, 0.05) = 1.753   D(5, 0.10) = 2.229    Q(5) = 4.375
Aucune de ces valeurs n'est recalculee en M6 : elles servent de bornes gelees.

PORTES -- chaque branche AVEC sa derivation (lecon E14)
------------------------------------------------------
P-M6a  NULL STRUCTUREL (p=4 ET p=6)
  D(4,0.10) <= 1.25 ET D(6,0.10) <= 1.25 -> LOI DES PORTEURS CONFIRMEE cote null.
    [derivation : aucun porteur de premier ordre => aucun canyon de premier
     ordre => les voisins encadrent le centre sans creux => D ~ 1.]
  D(4,0.10) >= 1.75 OU D(6,0.10) >= 1.75 -> LOI REFUTEE.
    [derivation de CETTE branche : 1.75 est le canyon quintique a d=0.05, donc
     un creux de magnitude quintique SANS porteur de premier ordre ; la
     profondeur ne peut plus etre imputee au canal (2,1), et l'interpretation
     de Q(3) et Q(5) en M5 perd son mecanisme.]
  Entre les deux -> NON CONCLUANT. Aucune lecture "confirme faible" autorisee.
  RESOLUTION DECLAREE (lecon E15) : cette porte est AVEUGLE a un canyon de
  demi-largeur < 0.05 en w2. Elle ne dit rien en dessous.

P-M6b  DECROISSANCE AVEC p (jambe d'ordonnancement de H-PROFONDEUR)
  D(7,0.10) < 2.229 -> DECROISSANCE CONFIRMEE.
    [derivation : H-PROFONDEUR exige que seul p=3 ait un canyon assez profond
     pour reordonner la carte de K ; la profondeur doit donc tomber avec p.]
  D(7,0.10) >= 3.34 (= 1.5 x D(5,0.10)) -> DECROISSANCE REFUTEE.
    [derivation de CETTE branche : un canyon a p=7 plus profond qu'a p=5
     obligerait H-PROFONDEUR a predire rho(T,K7) < 0, ce que l'hypothese
     n'autorise pas hors p=3 ; la jambe d'ordonnancement tombe.]
  Entre -> NON CONCLUANT.
P-M6b' SOUS-BRANCHE : D(7,0.10) <= 1.10 -> PORTEUR SANS CANYON.
    [derivation : p=7 a des porteurs par algebre ; s'ils ne creusent rien,
     l'existence d'un porteur n'est pas suffisante et la loi devient
     "porteur ET quelque chose d'autre" -- a etiqueter, non a expliquer ici.]

P-M6c  CALIBRATION NULLE DE Q -- auto-attaque de la statistique vedette de M5
  Q1(4) <= 1.3 ET Q1(6) <= 1.3 -> Q EST UN INSTRUMENT PROPRE.
    [derivation : paire miroir, coefficients egaux, aucun porteur des deux
     cotes => tout exces au-dessus de 1 serait de l'asymetrie 1<->2 generique
     (w1 != w2, signe fantome) et non du contenu resonant.]
  Q1(4) >= 2.0 OU Q1(6) >= 2.0 -> Q N'EST PAS UN INSTRUMENT PROPRE.
    [derivation de CETTE branche : une part de Q(3)=57.5 et Q(5)=4.4 serait de
     l'asymetrie de modes ; les verdicts M5 devraient etre re-exprimes en
     Q/Q1_null et le journal patche en consequence.]
  Entre -> LIMITE : correction appliquee et documentee.

P-M6d  ECHELLE INTER-DEGRES (impairs, variante mono-monome)
  Q1(7) < Q1(5) -> coherent avec P-M6b. Sinon -> incoherence D/Q1 a documenter.
  AUCUNE branche gagnante : D et Q1 mesurent la meme profondeur par deux routes
  differentes ; un desaccord est une information sur l'estimateur, pas un verdict.

PREDICTION CONDITIONNELLE GELEE (NON testee dans M6 -- pour une manche ulterieure)
  Si D(7,0.10) < D(5,0.10), alors H-PROFONDEUR predit rho(T,K7) > 0 (comme p=5
  et les pairs). Si D(7,0.10) >= 3.34, elle predit rho(T,K7) < 0 (comme p=3).
  Enregistre maintenant pour que le test quantique de p=7 soit un vrai test.

MES ATTENTES (pour pouvoir avoir tort de mon propre fait)
  D(4,0.10) ~ 1.05-1.15 ; D(6,0.10) ~ 1.05-1.20 ; D(7,0.10) ~ 1.3-1.8 ;
  Q1(4) ~ 1.0-1.2 ; Q1(6) ~ 1.0-1.2 ; Q1(5) ~ 2-4 ; Q1(7) ~ 1.5-3.

PROTOCOLE (repris de M5 sans modification, sauf mention NOUVEAU)
  EOM canoniques en modes : xdd1 = -w1^2 x1 + (dV/dx1)/Delta ,
  xdd2 = -w2^2 x2 - (dV/dx2)/Delta ; CI (x1,v1,x2,v2) = (A1,0,A2,0) avec
  A1 = sgn*s(1+w2^2)/Delta , A2 = -sgn*s(1+w1^2)/Delta .
  w1 = 1, g = 0.05, sgn = +1 gele, RK4 dt = 0.006, T = 400,
  cap = 1e4 sur max(|x1|,|x2|), grille 48, 3 passes, auto-elargissement.
  NOUVEAU (lecon G1-bis) : passe finale DENSE n = 96 sur le dernier bracket
  pour TOUT s* entrant dans un rapport. M5 avait enjambe une langue instable
  de largeur 3-8e-3 avec un pas de 8.4e-3 ; le pas final passe sous la largeur
  mesuree.

PROGRAMME FIGE (26 recherches)
  (A) Detuning : p dans {4,6,7} x w2 dans {1.90,1.95,2.00,2.05,2.10}, full = 15
  (B) Chirurgie Q1 : p dans {4,5,6,7} x {abl x1^(p-1)x2 , abl x1 x2^(p-1)}
      a w2 = 2.00 = 8   (p=5 inclus pour ancrer l'echelle mono-monome sur la
      valeur multi-monomes deja connue ; p=3 NON refait, repris de M5)
  (C) G2 invariance : p dans {4,6} au centre a 2g = 2
  (D) G4 : 1 re-run a dt/2 sur la recherche de plus grand s*
  Estimation : 10-15 min machine 2.

GARDES
  G1 ancres M1 (bloquantes la ou elles existent) :
     s*_full(4, 2.0) vs sqrt(0.337/0.05) = 2.596 a +-8 %
     s*_full(6, 2.0) vs (0.053/0.05)^(1/4) = 1.0147 a +-8 %
     p=7 : aucune ancre independante -> note, NON bloquant, et la ligne p=7
     reste un resultat de code B seul jusqu'a replication.
  G2 invariance : K_p = g s*^(p-2) a 2g, tolerance 10 %, reprise dense n=96
     sinon la ligne est EXCLUE (regle M1 gelee, appliquee sans exception).
  G3 identite de force : la somme des monomes doit redonner g(x1+x2)^(p-1)
     exactement ; assert au demarrage du run, arret si faux.
  G4 NOUVEAU pas de temps : les forces vont en x^(p-1) avec p = 7, plus raide
     que tout ce qui a ete integre dans la campagne. Sur la recherche de plus
     grand s*, re-run a dt/2 ; ecart sur s* <= 2 % sinon la ligne est marquee
     NON FIABLE (et non corrigee silencieusement).
  G5 controle positif en lecture seule : verifier sur m5_results.json que le
     motif p=3 est bien un minimum LOCAL sur les 5 points de detuning. Si la
     relecture ne le reproduit pas, ARRET avant toute interpretation de M6.

LIMITATIONS DECLAREES
  - L'ablation monomiale retire aussi les harmoniques NON resonantes du meme
    monome (limitation M5, inchangee) : la specificite est portee par le miroir,
    pas par une chirurgie d'harmonique, impossible polynomialement.
  - D est aveugle sous une demi-largeur de 0.05 en w2 (E15).
  - Q1 a p=5 n'est pas Q(5) : mono-monome contre multi-monomes. Les deux sont
    mesures pour que l'echelle soit lisible, aucun n'est substitue a l'autre.
  - Aucun quantique dans M6. La prediction conditionnelle ci-dessus est gelee,
    pas testee.

IMPLEMENTATION
  m6_porteurs_v1.py (nom versionne), integrateur modes autonome, ecrit
  uniquement out/m6_results.json (incremental). Gel jumeau dans le docstring :
  bloc de "PRE-ENREGISTREMENT M6" jusqu'a "=== FIN DU GEL M6 ===" inclus,
  canonique NFC+LF, sha256 imprime au demarrage et compare au sha256 livre.

=== FIN DU GEL M6 ===
