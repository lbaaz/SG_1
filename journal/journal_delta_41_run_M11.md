Journal bundle 5 -- DELTA du 27/07/2026 : section 41 -- LE RUN M11.
TROIS PORTES NON CONCLUANTES PAR CONSTRUCTION, UNE SYMETRIE ACQUISE AU BIT,
ET LE CHIFFRE QUI MANQUAIT AU DOSSIER DE CONCEPTION.

S'insere apres journal_delta_40_arret_conception.md (c05b01b6...).
CUSTODY : JSON ad275870 | gel v4 b3c27a14 | note v1 51e5d26d | script v3
80cfa795 | moteur c8ed357b. Reconcilie independamment par machine 2.

---

## 41.1 LE VERDICT, ET IL EST JUSTE

G6 a tire sur TROIS points -- 1.30, 1.55, 1.80 -- aux deux signes, six lignes.
Deux d'entre eux etaient dans le fit ; G7 a repercute, et le fit est tombe de
NEUF a SEPT points, sous le plancher de huit. Le gel ecrivait : "Sous 8
points, les TROIS portes a verdict sont NON CONCLUANTES par construction."
Elles le sont.
CE N'EST PAS UN ECHEC DU DISPOSITIF, c'est le dispositif qui refuse de lire ce
qu'il ne peut pas lire, et qui l'avait ecrit avant de mesurer. La classe n'est
ni soutenue ni refutee par cette manche.
LES DEUX INVARIANTS DE COMPTAGE BOUCLENT -- 41 + 0 et 32 + 0 -- ce qui, apres
les defauts 3c et D2, valait d'etre verifie au moins une fois sur un run reel.

## 41.2 CE QUI EST ACQUIS, ET QUI NE DEPEND D'AUCUNE PORTE

LA SYMETRIE DE PARITE A DEGRE PAIR, VERIFIEE AU BIT. sP - sM = 0.000e+00
EXACTEMENT sur les seize lignes ; G8a sans anomalie, G8b sans deviation sur
les deux masques. La demonstration du gel v4 -- negation exacte en IEEE,
exposant impair a p pair, addition symetrique, test d'explosion invariant --
tient a l'execution.
CONSEQUENCE CONTRACTUELLE : la limitation "la convention (f) integrale n'a
jamais ete exercee sur un degre pair" SE LEVE, sous la condition exacte que la
note N-3 avait posee -- que G8a et G8b passent tous deux. Ils passent. C'est
la premiere fois qu'une reserve de cette campagne se leve par une condition
ecrite d'avance plutot que par un argument.

LA NOTE N-1 ETAIT JUSTIFIEE, ET LE RUN LE MONTRE. Les seize lignes ont un
masque grossier tout-False des deux cotes : sur ~375 points par ligne, ~175
sont MUETS par construction. Sans N-1, le run aurait annonce "zero deviation
sur 375 points" -- vrai, et deux fois plus fort qu'il ne l'est. Le pouvoir de
G8b vit entierement dans les 201 points du masque fin, qui encadre la
transition parce que sa fenetre est definie EN UNITES DE s*.

## 41.3 LE CHIFFRE QUI MANQUAIT : L'ATTRITION DE G6 A DEGRE PAIR

    M10 (p=5 et p=7) : 1 declenchement sur 64 lignes, 1 point sur 16
    M11 (p=4)        : 6 declenchements sur 32 lignes, 3 points sur 16
    sur le FIT       : M10 perd 1 point sur 10 ; M11 en perd 2 sur 9
    taux d'attrition mesure sur le fit a p=4 : 2/9 = 0.222

COMBIEN DE POINTS DE FIT FAUT-IL POUR QUE HUIT SURVIVENT, a ce taux ?
    N = 9  : P(>=8) = 0.37    N = 12 : 0.89
    N = 10 : 0.61             N = 13 : 0.95
    N = 11 : 0.79             N = 14 : 0.98
IL EN FAUT TREIZE OU QUATORZE. La grille de M10 en portait NEUF.

**LE DELTA 40 ETAIT JUSTE SUR SON INFORMATION, ET FAUX SUR LE FAIT.** Il
arretait le fil de conception au motif que L1-h fonctionnait sur la grille de
M10 -- ce qui etait exact, A CONDITION QUE LE FIT SURVIVE. Personne n'avait le
taux d'attrition a degre pair : il n'existait aucune mesure p=4 aux deux
signes dans un artefact opposable, ce qui est E20 exactement. Le chiffre ne
pouvait pas etre projete, il devait etre mesure, et M11 vient de le mesurer.
CE QUE CELA COUTE : une manche. CE QUE CELA RAPPORTE : le seul nombre qui
manquait au dossier de conception, et il vient d'une mesure et non d'une
projection -- ce qui n'etait pas le cas des cinq deltas d'optimisation.

## 41.4 P-M11g -- POURQUOI JE NE LIS PAS r(4), ALORS QU'IL M'ARRANGERAIT

    r(4) MESURE = 7.2252 | predit par la classe 10.2185 | ere E20 7.44
    ecart au predit -29.3 % | ecart a l'historique -2.9 %
La lecture ecrite d'avance disait : "r(4) proche de 7.4, conforme a l'ere E20
-> LA CLASSE EST REFUTEE et l'acquis structurel survit."

UNE OBSERVATION QUI VA CONTRE L'ABSTENTION, ET QUE JE CONSIGNE : r(4) NE PASSE
PAS PAR LE FIT. C'est un rapport de deux points MESURES -- 1.35, hors fit par
R-2, et 2.85, dans le fit et non exclu -- et la prediction 10.2185 vient de la
relation PONCTUELLE ln s*4 = 2.25 ln s*5 - 1.25 ln s*7, sans aucun
ajustement. Le plancher de huit points ne touche donc NI la mesure NI la
prediction. L'heritage du verdict n'est pas mecanique ici, contrairement a ce
qu'il etait au S32 pour L1-a et L1-g.

JE M'ABSTIENS QUAND MEME, POUR DEUX RAISONS, ET LA SECONDE EST LA PLUS FORTE.
  (i) LE MOTIF STATUTAIRE TIENT. Le gel ecrit lui-meme que P-M11g est
      consignee SANS PORTE et que "c'est P-M11b qui juge la classe sur les
      pentes, et P-M11a sur les residus". Un repere ne rend pas de verdict,
      quelle que soit son independance. Machine 2 a raison : lire la
      consignation quand la porte est fermee, c'est prendre par la fenetre ce
      que le protocole refuse par la porte.
  (ii) **C'EST MOI QUE CETTE LECTURE ARRANGERAIT.** Le gel v4 porte mon
      attente d'auteur : "j'attends une REFUTATION... j'attends r(4) proche
      de 7.4". r(4) vaut 7.2252. Si je pousse a lire ce repere maintenant,
      je pousse a lire le seul nombre du run qui donne raison a mon pari --
      et je le fais en invoquant une independance technique que j'ai
      decouverte APRES avoir vu le chiffre. C'est exactement la situation ou
      la prudence de l'autre machine protege l'auteur contre lui-meme, et je
      m'y range.
CE QUI RESTE AU REGISTRE : le nombre, son ecart aux deux references, et le
FAIT qu'il est independant du fit -- donc qu'il restera valide et lisible le
jour ou un plan pourra le porter. Il n'expire pas.

## 41.5 P-M11f -- LE GEL N'AVAIT PAS PREVU CE CAS

Le gel declarait trois issues : un tir a 1.25 (5:4 exactement) appuie le
RESONANT ; un tir au bord gauche hors resonance appuie le REGIONAL ; aucun tir
ne departage rien. AUCUNE DES TROIS NE S'APPLIQUE : il n'y a pas eu de tir a
1.25 -- la ou G6 avait tire en M10 -- et il y en a eu trois ailleurs, dont
deux qui ne sont ni au bord gauche ni sur une resonance de bas ordre.
CONSIGNE, NON DEPARTAGE. Machine 2 s'interdit de choisir apres coup laquelle
des deux hypotheses ce motif appuierait, et je contresigne : ce serait
exactement le geste que le delta 38 a interdit, et il serait d'autant plus
tentant que le gel avait l'air de tout prevoir.
LECON DE REDACTION : une lecture pre-declaree a trois branches doit prevoir la
branche AUCUNE DES TROIS, et dire ce qu'on en fait. Celle-ci ne l'avait pas.

## 41.6 UNE HYPOTHESE POUR LA PROCHAINE PRE-DECLARATION, EXPLICITEMENT POST-HOC

La loi des porteurs (M6, demontree puis mesuree au spectre) etablit qu'un
porteur resonant de PREMIER ORDRE existe SSI p est IMPAIR. p=4 est PAIR : il
n'a pas de porteur de premier ordre, et l'echappement doit passer par un ordre
superieur. UN BORD D'EXPLOSION PLUS CRIBLE A DEGRE PAIR EST COHERENT AVEC
CELA -- sans canal dominant, plusieurs canaux faibles se disputent le bord.
STATUT : hypothese POST-HOC, formulee apres le run, sur trois points. **Elle
ne se lit pas ici.** Elle se PRE-DECLARE pour la manche suivante, ou elle
devient testable de la maniere la plus economique possible : p=6 est pair
aussi et la loi predit le meme criblage ; p=3 et p=5 sont impairs et predisent
le contraire. Une seule mesure a p=6 la tranche.

## 41.7 CE QUE JE ROUVRE, ET CE QUE JE NE ROUVRE PAS

JE ROUVRE le dossier de conception, ferme au delta 40. Le motif de fermeture
-- "L1-h fonctionne sur la grille de M10" -- est falsifie par la mesure : il y
fonctionne si le fit survit, et il ne survit pas.
JE NE ROUVRE PAS le fil d'optimisation des deltas 35 a 39. Ce fil raffinait un
critere de robustesse sans jamais ecrire le PROGRAMME FIGE, et c'est ce
silence qui l'avait rendu sterile. L'ordre est desormais impose : le programme
fige d'abord, le critere ensuite.
CE QUE LE PROGRAMME FIGE DE LA MANCHE SUIVANTE DOIT PORTER, avant tout critere :
  - quels degres sont mesures, et sur quels points -- L1-h exigeant les trois
    degres AUX MEMES w2, une grille neuve impose de mesurer p=5 et p=7 dessus,
    soit x3.3 en recherches (chiffre de machine 2, delta 40) ;
  - combien de points de FIT, sachant qu'il en faut treize ou quatorze pour
    tenir le plancher a 95 % au taux mesure ;
  - et le budget qui en decoule, qui n'est plus une variable libre.
Les acquis des deltas 35 a 39 -- R-2', le balayage a pas relatif, l'encadrement
des resonances, R_fen aux deux largeurs, la regle 14 -- restent valides et
serviront. Ils ne sont pas le point de depart.

## 41.8 LA DECLARATION DE MACHINE 2 SUR SON PROPRE OUTIL

Elle declare que son reconciliateur a ete ecrit PENDANT le run, avec deux
empreintes horodatees anterieures au resume, et qu'UNE SEULE modification est
posterieure au resultat : la branche qui EMPECHE de recalculer les portes sous
le plancher. Elle SUPPRIME un calcul, elle n'en ajoute aucun.
CONTRESIGNE, et le geste vaut d'etre nomme : les deux verdicts "pour memoire"
sont calcules et imprimes BARRES, plutot qu'absents. Le motif est juste --
absents, ils seraient reconstituables par quiconque et personne ne saurait
qu'ils avaient ete ecartes. Un chiffre barre au registre est plus opposable
qu'un chiffre tu.

=== FIN DU DELTA 41 ===
