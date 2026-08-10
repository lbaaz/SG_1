# Journal bundle 5 -- DELTA du 25/07/2026 (soir) : sections 19-20, gel M7, ERRATA E16-E17

*Ce delta s'insere APRES le §18 livre plus tot ce jour (fichier
journal_delta_section18.md, sha256 cf9cc4842f73cb0bd47f8c0183bb51bad3ded0ca
5f1a7eb74aa3d15290487845). Etat du maitre au moment de l'ecriture :
journal_bundle5_v2026-07-25j.md (§0-17-bis, E1-E15) + delta §18.*

---

## 19. MANCHE M6 EXECUTEE (machine 2) -- la loi des porteurs tient des deux
## cotes ; Q est declasse en instrument ordinal ; un defaut de garde (G4)

**Artefacts primaires** : m6_results.json, sha256
99674ad73910c3693254404d9cd94b38803fa4098d4028bee5419c1ec99441e4.
Gel certifie au demarrage (048900d8...), script conforme (c92e67de...),
28 recherches + G4 en ~6.5 min machine 2, pas final 6e-07 partout.
**Reconciliation resume <-> brut (machine 1)** : 7 statistiques recalculees
depuis runs[].s_star, pire ecart 2.8e-3 (arrondis d'affichage). ZERO ecart
de fond. Premiere fermeture machine2 -> machine1 sur du brut pour M6.

### Portes (appliquees mecaniquement contre les seuils geles)

- **P-M6a : LOI DES PORTEURS CONFIRMEE cote null.** D(4,0.10) = 0.9881,
  D(6,0.10) = 1.0037 (seuil <= 1.25). Lecture forte du brut, au-dela du
  chiffre : les lignes s*(w2) des degres PAIRS sont MONOTONES CROISSANTES sur
  toute la fenetre 1.90-2.10 -- il n'y a pas un creux aplati par la moyenne
  geometrique, il n'y a AUCUNE structure. Et la loi tient aux DEUX detunings
  (delta = 0.05 : 3.63 / 1.75 / 1.42 / 0.99 pour p = 3/5/7/pairs).
- **P-M6b : DECROISSANCE CONFIRMEE contre sa porte.** D(7,0.10) = 1.6334
  < 2.229. P-M6b' (porteur sans canyon, <= 1.10) : non cochee -- les porteurs
  creusent. **[ANNOTATION E17 : la porte est gelee en unites s* ; en unites K
  la hierarchie s'aplatit (15.4 / 11.1 / 11.6) et p5 -> p7 REMONTE. Le verdict
  TIENT contre sa porte ; l'inference inter-degres est reformulee. Voir E17.]**
- **P-M6c : LIMITE.** Q1(4) = 1.4125 (zone grise 1.3-2.0), Q1(6) = 1.1633
  (confirme). La branche gelee prevoyait une correction "Q/Q1_null" ; le brut
  la REFUSE : (i) les deux nulls different de 21 % (1.41 vs 1.16) -- ce n'est
  pas une constante ; (ii) Q1(7) = 1.1723, AVEC porteurs, est INFERIEUR au
  null p=4 ; (iii) structurellement, le null de Q n'est mesurable qu'aux
  degres PAIRS (aux impairs il y a toujours un porteur, par le theoreme meme
  de la manche), or Q ne sert qu'aux impairs -- la division par un null
  transporterait une mesure d'un degre a un autre. **Reformulation retenue :
  Q porte une contamination d'asymetrie de modes de 16 a 41 % selon le degre,
  mesuree aux pairs, non transportable aux impairs. Q est un instrument
  ORDINAL, pas un rapport calibre.** Les verdicts M5 tiennent en ORDRE
  (l'exces resonant existe aux deux degres impairs), pas en echelle.
- **P-M6d :** Q1(7) = 1.17 < Q1(5) = 1.77, coherent avec P-M6b. La divergence
  D/Q annoncee comme information sur l'estimateur se chiffre : rapport de
  profondeur p3/p5 = 6.90 par D contre 13.14 par Q (et voir E17 pour l'unite).

### Gardes

- **G1 : clouees.** p=4 : 2.60187 vs 2.596 (0.23 %) ; p=6 : 1.01429 vs 1.0147
  (0.04 %) ; p=7 sans ancre, non bloquant, ligne code B seul.
- **Asymetrie de signe r = s*(+1)/s*(-1) : 1.000000 aux pairs -- TAUTOLOGIE,
  pas une mesure.** V pair => (x,v) -> (-x,-v) est une symetrie EXACTE des
  EOM => la trajectoire a sgn=-1 est la negation de l'autre. Le volet E aux
  pairs est donc un TEST UNITAIRE (passe : pas de bug de signe), a ne pas
  verser au dossier comme donnee physique. La seule mesure est r(p=7) =
  1.001096 : asymetrie quasi nulle au point resonant meme en degre impair.
- **G2 :** 0.43 % / 0.00 %. **G3 :** backward 1.2e-13 (marge x8000).
- **G4 : DEFAUT DE CIBLAGE.** La derivation invoquait p=7 ("x^6, plus raide
  que tout ce qui a ete integre") mais le critere d'application etait "le plus
  grand s*", tombe sur p=4 (B|p4|abl_mono1, ecart 0.31 %). p=7 n'avait recu
  AUCUNE verification de pas de temps. Comble HORS GEL, machine 1 :
  s*(p=7, w2=2, dt/2) = 0.39227 vs 0.39227, ecart 0.001 % -- et machine 1
  reproduit machine 2 a cinq chiffres sur cette ligne (meme code B :
  independance d'environnement, pas d'implementation). **Lecon, integree au
  gel M7 : une garde s'applique la ou sa derivation la motive** (G4 de M7 est
  redefinie sur max de g s*^(p-1), l'echelle de force).
- **G5 :** motif p=3 relu en lecture seule et confirme avant interpretation.

### Complements du brut

- **H-PROFONDEUR(i) passe son DEUXIEME falsifieur, sur un TROISIEME degre.**
  p=7 : vrai minimum local (ratios > 1 des deux cotes : 1.311/1.208 dessous,
  1.671/2.034 dessus), cote raide w2 > 2 comme p=3 et p=5. L'asymetrie decroit
  comme la profondeur : 17.6 -> 1.86 -> 1.55. ATTENTION : les pairs n'entrent
  pas dans cette colonne -- leur fond est monotone, "cote raide" n'y a pas
  de sens.
- **Attentes gelees de l'auteur : 2/7 dans la fourchette** (D(7) et Q1(6)
  dedans ; D(4), D(6), Q1(4), Q1(5), Q1(7) dehors). Nota de reconciliation :
  le resume machine 2 comptait "quatre predictions, deux dedans, deux dehors" ;
  le decompte complet des sept fourchettes donne 2/7. Ecart de decompte sans
  consequence, consigne par discipline. Lecon : la calibration des attentes
  personnelles est mauvaise -- ce qui justifie retroactivement de ne jamais
  leur donner de role de porte.

**Bilan M6 :** le canal (2,1) n'existe que la ou l'algebre met un porteur
(verifie par mesure spectrale independante AVANT le gel), les degres pairs
sont un null propre a 1-2 % de D=1, et l'auto-attaque P-M6c a produit son
effet : l'instrument vedette de M5 est requalifie. Verdicts M5 intacts en
ordre. G1/G2/G3/G5 nettes, G4 comblee avec lecon.

---

## MANCHE M7 -- PRE-ENREGISTREMENT GELE, SCRIPT DEPOSE, EXECUTION EN COURS

**Gel v1** f477246ecfa53e127cedcb2ef29d146906a68be07fc36770f85058119f09a14a,
**RETIRE avant toute ligne de code** : la consequence retroactive de la
derivation (b) chiffrait la tranche p=6 de M1 sur la nulle a n=4 alors qu'elle
compte n=3 points ((6,sqrt2) exclu par l'invariance). Releve par la
certification machine 2. **Gel v2**
5c54ac0342cdb6ba1c2203d13a42b976266e3b3224fdfcaaaaa6ec422e05eec7 (216 lignes),
corrections : nulle a n=3 enumeree (rho=+0.50 -> p=0.500 exactement ; meme
rho=+1.00 n'y vaut que 0.167 -- l'argument SORT RENFORCE), provenance des
reperes K4 etiquetee (deux jeux, ecarts jusqu'a 6 %, meme argmin), N=72
requalifie en CHOIX DE DESIGN (comparabilite M1/M3), pas en contrainte machine.

**Contenu du gel** : deux etages proteges l'un par l'autre. Etage 1 classique
(P-M7a : l'argmin de K7 sur SIX points -- si le point resonant est le minimum,
le lien tombe et l'etage 2 tourne SANS prediction, interdiction de re-deriver
un signe apres coup). Etage 2 quantique (P-M7b : rho(T_coquille, K7) de
Spearman, porte a |rho| >= 0.80 AUX DEUX troncatures, p <= 0.029 par la nulle
exacte ; verrou anti-arret-optionnel gele : [0.60, 0.80) ne declenche AUCUNE
prolongation). P-M7c/d secondaires sans porte. Gardes G1-G7, dont G4 corrigee
(cf. lecon M6) et G7 = consigne du rapport T(56)/T(64) SANS porte (magnitude
non convergee, §8 ; seul le rang est revendique).

**Decouverte structurelle de l'audit pre-gel, derivation (d)** : le temoin
borne NULL+ N'EXISTE PAS aux degres impairs -- +w1 n1 + w2 n2 + (g/p) x^p est
NON borne inferieurement a p impair. Explique apres coup pourquoi la campagne
ne l'a jamais fait tourner qu'a p=6. **Faiblesse retroactive declaree de M1
(p=3) et M3 (p=5)** : leurs volets quantiques n'ont jamais eu de temoin
dynamique borne. M7 ne pretend pas l'avoir : null FREE seulement (pipeline,
pas dynamique), et le systeme a signe retourne est consigne comme donnee brute
SANS interpretation gelee.

**Script** : m7_profondeur_v1.py (655 lignes), sha256
11b143b61423df6d1639066be235f6b5a5c6cc0150fe17afbdbca61d7ef245e1, bloc jumeau
EXTRAIT du .md (pas retape), empreinte recalculee au demarrage depuis le
fichier source. **Pre-vol machine 1** : G1 regression 0.39227 vs ancre M6
0.39227 (0.001 %) ; G3 backward 4.4e-16 ; coquille 891 etats conformes ;
null FREE 8.3e-56 (seuil 1e-12) ; diagonalisation 10.6 s (N=56) / 22.6 s
(N=64) -> cout revise ~12 min total (le gel annoncait 20-40 min de quantique :
estimation conservatrice, non regelee). T_shell pre-vol : 4.29e-2 (N=56) vs
2.83e-2 (N=64), rapport 1.51 -- la non-convergence de magnitude connue (§8),
raison d'etre de G7. **Execution lancee sur machine 2 ; resultats non lus au
moment ou ce delta est ecrit** (pertinent pour le statut du §20).

---

## 20. AUDIT ADVERSARIAL DU 25/07 (pendant l'execution de M7) -- deux errata,
## une reformulation d'echelle, faiblesses structurelles versees au dossier

*Commande de l'humain : critiquer la demarche et chercher les erreurs d'Opus
pendant que M7 tourne en local. Aucun resultat M7 vu pendant cet audit.
Trace executable : audit_critique_2026-07-25.py.*

### Erreurs concretes trouvees (dans les livrables de la seance meme)

- **E16 (voir ERRATA)** : deux defauts dans l'abstract de la note EN 25p,
  introduits par le patch Q1-Q3 de seance. Corriges en version 25q.
- Le gel M6 v1 avait deja ete tue par son propre audit (ancres G1 comparant
  deux conventions de signe) et le gel M7 v1 par la certification machine 2
  (nulle n=4 pour une tranche n=3) : DEUX gels retires avant toute donnee dans
  la meme journee. Le protocole "audit pre-feu" fait son travail, mais le taux
  de defauts de premiere ecriture est une donnee en soi : AUCUN gel n'est
  sorti juste du premier coup aujourd'hui.

### E17 en bref (voir ERRATA pour l'entree formelle)

La "profondeur du canyon" de M6 est mesuree en s* ; dans l'invariant K de la
campagne, elle vaut D^(p-2) : 15.4 / 11.1 / 11.6 pour p = 3/5/7 -- quasi
constante, et p5 -> p7 remonte. La chirurgie M5 s'inverse meme en unites K
(51.9 contre 82.9). Les rangs etant invariants d'echelle, LES PORTES DE M7 NE
BOUGENT PAS ; c'est la narration inter-degres qui est reformulee. Candidat de
remplacement, DECLARE AVANT LECTURE de m7_results.json (les donnees existent
deja sur machine 2 : declaration DATEE, pas pre-enregistrement, valeur
probante limitee et dite telle quelle) : **creux_K / fond_K par degre** --
p=3 : creux x3.9 sous un fond x17, ratio 0.22, le canyon est COMPARABLE au
fond, d'ou le reordonnancement ; prediction : effondrement du ratio pour
p >= 4. Calculable pour p=5 (m3_calib.json) et p=7 (m7_results.json).

### Faiblesses structurelles, non levees, versees au dossier

1. **Analyste unique sur l'espace de design.** Les gels contraignent APRES
   ecriture ; le choix des statistiques, des echelles et des observables reste
   a un seul auteur (Claude), et D/Q1 comme E17 montrent que ce choix porte du
   signal. La certification humaine verifie les derivations, pas
   l'exhaustivite de l'espace des designs. Mitigation partielle seulement.
2. **T_shell = ensemble diagonal**, c'est-a-dire moyenne temporelle infinie
   SI le spectre est non degenere. Jamais audite depuis §8. Point neuf : a p
   IMPAIR, x^p est de parite impaire donc H ne commute plus avec la parite --
   toute la campagne paire avait une structure en blocs que M7 n'a pas.
   Double tranchant : pas de degenerescences de symetrie (rassurant pour
   l'ensemble diagonal), mais un spectre structurellement different, non
   signale dans le gel M7.
3. **La coquille 35-45 a ete concue pour x^4 (Delta n <= 4) et jamais
   re-derivee pour x^7 (Delta n <= 7).** Du sommet (45), un saut atteint 52
   contre un mur a 55 pour N=56 : ~1.4 sauts de tampon (2.5 pour x^4).
   L'accord de rang N=56/64 exige par P-M7b est une garde partielle : un biais
   de mur commun aux deux troncatures et uniforme en w2 passerait.
4. **G5 tolere 5 % sur s*, soit jusqu'a x1.28 sur le K effectif** (1.05^5) et
   ~10 % sur nbar1. Acceptable mais non chiffre dans le gel.
5. **Ne jamais multiplier les p des deux troncatures** : N=56 et N=64 sont
   correlees ; la conjonction rho >= 0.8 aux deux ne vaut pas 0.029^2.
6. **Garden of forking paths** : M5 -> M6 -> M7 s'enchainent sur le meme flux
   de donnees, et D(5) = 2.229 joue DOUBLE ROLE (donnee M5 et ingredient de
   porte M6/M7). Chaque manche est honnete localement ; la trajectoire globale
   ne se rachete que par des predictions sur du neuf -- M7, precisement.

### Boucles ouvertes consolidees (etat au soir du 25/07)

1. **Arbitrage G3 (metrique backward)** : note d'exploitation attachee a M6,
   ou erratum ? TOUJOURS PENDANT, a la main de l'humain. La reservation
   informelle du numero "E16" faite dans la note de livraison M6 est LEVEE
   (E16 est consomme ci-dessous) ; s'il est promu, cet arbitrage prendra le
   prochain numero libre.
2. **Taille de la grille p=5 de M3 (n=3 ou n=4 ?)** -- a verifier sur les
   artefacts M3. Si n=3 : rho = +1.00 y vaut p = 0.167, et AUCUN rho quantique
   significatif n'existe a degre impair avant M7, qui devient le premier test
   correctement puissante de toute la campagne.
3. **Note FR** : "cinq erreurs" / "deux re-executions" = chiffres de l'ere
   bundle 3ter, perimes (E1-E17, trois implementations). La mise a jour
   suppose de decider ce que le bundle expedie contient.
4. **bundle5.py joint ou non** : la disclosure EN ne le promet pas ; a trancher.
5. **Journal maitre** : integrer §18 (livre), §19-§20 + E16-E17 (present
   delta), puis §21 = M7 executee, des reception du brut.

---

## ERRATA -- troisieme serie (audit adversarial du 25/07 au soir)

## E16 -- Deux defauts dans l'abstract de la note EN 2026-07-25p

(a) "with a median seven to thirteen orders above the twin's floor" : le
"seven" ne correspond a AUCUN calcul -- contamination du 10^4-10^7 des taux
dynamiques dans la phrase du recensement. Le corps (§4(c)) dit "10^13" ;
valeurs correctes : 4.2e-3 / 8.9e-16 ~ 4.7e12 (coquille, N=72) et
1.1e-2 / 8.9e-16 ~ 1.2e13 (like-for-like, N=64), soit 12-13 ordres.
(b) Couture rhetorique : la separation "four to seven orders deep inside the
island" (mesuree a s <= 0.9, regime NON converge en troncature) etait accolee
dans la meme phrase a "truncation-stable for s >= 1.2" (ou le rapport n'est
que 46 puis 5.9). Chaque clause vraie isolement ; la jonction attachait la
separation spectaculaire au regime stable -- precisement le glissement que le
§4(b)(i) de la meme note s'interdit.
**Cause commune** : compression de deux regimes en une phrase d'abstract par
l'auteur du patch (Claude). **Detection** : auto-audit commande par l'humain,
AVANT tout envoi. **Correction** : version 2026-07-25q, sha256
265e64de538e7cec0f9ba0a50ec64ec7bc3c56bf6c8815f96fd74d99426669ed --
(a) "twelve to thirteen orders of magnitude" ; (b) phrase scindee, l'existence
de la fuite profonde rebasee explicitement sur le controle sans fantome et la
coquille fixe, pas sur le taux. La note FR est verifiee indemne de defauts
equivalents et reste en 25p.

## E17 -- La "profondeur du canyon" depend de l'echelle ; l'inference
## inter-degres de P-M6b depassait sa porte (troisieme lecon du type E14/E15)

P-M6b est gelee et jugee en unites s* : D(7,0.10) = 1.633 < 2.229, verdict
DECROISSANCE CONFIRMEE -- **le verdict tient contre sa porte, rien n'est
retire**. Mais H-PROFONDEUR parle de ce qui ordonne la carte de K, et
K_p = g s*^(p-2) : la profondeur DANS LA CARTE K est D^(p-2) = 15.4 / 11.1 /
11.6 pour p = 3/5/7 -- quasi constante aux impairs, p5 -> p7 REMONTE. La
chirurgie M5 s'inverse meme : R_res en K vaut 51.9 (p=3) contre 82.9 (p=5).
L'enonce "la profondeur decroit avec p, donc seul p=3 peut reordonner la
carte" etait donc une inference DEPENDANTE D'UN CHOIX D'UNITE jamais discute,
promue au-dela de sa porte -- jumeau d'E15 (une porte mesure ce qu'elle
mesure) avec l'unite comme angle mort. Sauvegardes : (i) les rangs sont
invariants sous s* -> s*^(p-2) a p fixe, donc P-M7a et P-M7b (Spearman) sont
INTACTES ; (ii) le sens physique survivant est le rapport creux/fond PAR
degre (p=3 : 0.22 ; pairs : 0), declare date au §20, a calculer pour p=5 et
p=7. **Lecon a geler pour les manches futures : toute comparaison
inter-degres doit declarer son unite ET montrer qu'elle est invariante, ou
donner les deux echelles.**
