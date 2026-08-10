Journal bundle 5 -- DELTA du 27/07/2026 : section 40 -- ARRET DU FIL DE
CONCEPTION. UNE GRILLE OPTIMISEE AURAIT RENDU L1-h IMPOSSIBLE.

S'insere apres journal_delta_39_quatre_decisions.md (07914fe5...).
Algebre pure sur out/m10_results.json. AUCUNE mesure.

---

## 40.1 LE FAIT

L1-h s'ecrit : **res4 - 2.25 res5 + 1.25 res7 = 0 EN CHAQUE POINT.** C'est
une identite PONCTUELLE. Elle exige res4 sur les MEMES w2 que res5 et res7,
sans quoi la combinaison n'est pas definie.

    points de fit ou vivent res5 et res7 (M10, apres G7) : 9
        1.30  1.70  1.80  2.15  2.30  2.45  2.60  2.75  2.85
    points de fit de C1, candidate du S36                : 12
        1.2500 1.2573 1.2719 1.2946 1.3693 1.7923 2.2126
        2.3618 2.6317 2.7361 2.8106 2.8500
    POINTS COMMUNS : UN SEUL -- 2.85.

**Une grille optimisee n'a pas de points communs avec M10. L1-h y serait
impossible.** Les sections 35 a 39 optimisaient donc une manche dont le but
principal declare -- le seul test de la classe -- aurait ete detruit par le
resultat de l'optimisation.
Personne ne l'a vu : ni machine 1 qui a ouvert le fil au S35.4, ni machine 2
qui a calcule 53 combinaisons au S38.4. Le critere a change quatre fois --
max R, puis R3_bloc, puis R_fen, puis R_fen aux deux largeurs plus
encadrement -- et a aucun moment la contrainte la plus dure n'a ete ecrite :
**la grille de la manche p=4 est deja fixee, c'est celle de M10.**

## 40.2 ET L1-h NE DEMANDE AUCUNE PUISSANCE

C'est le second fait, et il rend le premier sans consequence.
    RMS(res5) = 0.12323 | RMS(res7) = 0.06497
    plancher de bruit de la combinaison : (1 + 2.25 + 1.25) x 6e-07 = 2.7e-06
    signal attendu si la classe est FAUSSE : de l'ordre de 0.1
    DYNAMIQUE : environ CINQ DECADES.
L1-h est un test d'IDENTITE PONCTUELLE sur des residus, pas une estimation de
pente. Il ne depend ni de Sxx, ni du levier, ni du conditionnement, ni de la
puissance du plan. **Il fonctionne sur la grille effondree de M10.**
La motivation entiere du fil de conception -- recuperer de la puissance --
portait sur beta(4), qui est un objectif SECONDAIRE. Le principal n'en avait
pas besoin.

## 40.3 CE QUE CELA COUTE, ET CE QUE CELA RAPPORTE

MANCHE M11, sur la grille de M10, inchangee :
    recherches : 16 points x 2 signes = 32, plus G2 (6) et G4 (1) = 39
                 (M10 : 71)
    balayages  : 32  (M10 : 64)
    points de balayage, au pas relatif du S39.3 : 32 x 401 = 12 832
                 (M10 : 64 x 192 = 12 288, soit x1.04)
**M11 est MOINS CHERE QUE M10 en recherches, et equivalente en balayage**
malgre le pas relatif qui multiplie les points par 1.8 -- parce qu'il y a
deux fois moins de lignes.
CE QU'ELLE REND :
  - L1-h, le SEUL test de la classe, a cinq decades de dynamique ;
  - beta(4), avec le levier (4,7) = 0.3000 contre 0.1333, x2.25 sur F --
    sous la reserve que le plan reste celui, faible, de M10 ;
  - la position d'un eventuel declenchement G6 a p=4, qui departage regional
    et resonant sans qu'aucune porte n'en depende (R-2' ayant sorti 1.25 du
    fit tout en le gardant mesure).

## 40.4 CE QUI SURVIT DU FIL DE CONCEPTION, ET CE QUI EST SUSPENDU

SURVIT, et s'applique a M11 :
    R-2' (S38.6), derivee et gelee avant la grille ;
    le balayage a PAS RELATIF (S39.3), qui supprime le confondant ;
    les quatre declarations du gel de balayage (S39.6) ;
    la regle 14 (refit a chaque reechantillonnage).
SUSPENDU, et rendu a son vrai statut -- une manche FUTURE, pas la prochaine :
    l'entree 2 en encadrement (S39.4), les entrees 6 et 7, R_fen aux deux
    largeurs, le choix N=20 / N=24, les candidates C1 et C5, et les 53
    combinaisons du S38.4.
Rien n'est retire : tout cela vaut pour une manche qui RE-PLANIFIERAIT la
carte. Mais cette manche-la n'est pas la prochaine, et elle ne le devient que
si L1-h et beta(4) le justifient.
**LA CONSIGNE A MACHINE 2 DU S39.7 EST ANNULEE** : ne pas refaire
l'enumeration des candidates. Elle porterait sur une manche qui n'est plus a
l'ordre du jour.

## 40.5 CE QUE CE FIL AURA APPRIS, MALGRE TOUT

Le fil a produit quatre acquis reels -- R-2', le pas relatif, l'encadrement,
et la regle 14 -- et une lecon de methode qui vaut d'etre inscrite :
**cinq echanges d'optimisation successifs, chacun corrigeant le precedent,
sans qu'aucun ne revienne verifier que l'objet optimise servait encore le but
declare.** C'est la meme famille que E24 et D-M10-9 -- une specification qu'on
raffine sans la confronter a ce qu'elle doit produire -- deplacee de la
verification vers la conception.
    CONSIGNE, sans en faire une regle de plus : avant d'optimiser un plan,
    ecrire ce que la manche doit RENDRE, et verifier a chaque tour que
    l'optimisation ne le detruit pas. Le cout de ne pas le faire, ici, a ete
    cinq deltas.

## 40.6 LA SUITE, CONCRETEMENT

  1. rediger le pre-enregistrement M11 : grille de M10 (deja gelee et
     certifiee en v8), R-2', balayage a pas relatif, portes P-M11a (L1-h) et
     les consignations heritees ;
  2. certification croisee ;
  3. depot du script -- le moteur, les lecteurs d'ancres et le harnais de
     M10 sont reutilisables tels quels, seul le degre change ;
  4. execution, et lecture de L1-h.
Le chemin critique est la redaction du gel M11. Il n'y a plus de calcul de
conception a faire avant.

=== FIN DU DELTA 40 ===
