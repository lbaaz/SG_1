# Journal bundle 5 -- DELTA du 26/07/2026 : section 26 -- M9 executee (NON
# CONCLUANT, C2 REARME), investigation P-M9c RESOLUE, ERRATUM E21

*S'insere apres journal_delta_25_M9v2.md (sha256 5e2e1462710f4a13212cf923ac
079eb0e9eb630ad99458cbee8c929b970d27f2). Artefacts recus : m9_run.log,
diagnostic_g7_m9.log ; JSON out/m9_results.json annonce sha
41595413f676df396994da1b7ca6c4abc59199b8ca2f93f00e2643c151653210 (fichier
non transmis -- reconciliation LOG-niveau faite ici, zero ecart sur les
quatre rho, G7, et les gardes ; JSON-niveau en attente).*

---

## 26. M9 : LA PREMIERE MANCHE OPPOSABLE DE BOUT EN BOUT -- verdict NON
## CONCLUANT, compensation C2 declenchee, et une investigation qui paie

**Opposabilite.** Gel v2 certifie AVANT script (m9_certification_croisee_v2),
empreinte verifiee au demarrage, G1a/G1b/G2/G3/G4/G6/FREE tous verts,
6/6 points retenus, zero exclusion. La manche est propre ; le signal est
ambigu -- et le circuit E19 aura tenu d'un bout a l'autre pour la premiere
fois.

### Verdicts (mecaniques, contre le gel v2)

- **P-M9-pre : LIEN CONFIRME** (argmin K5_min a 1.35). Troisieme
  confirmation de l'ordonnancement par le fond, et la premiere sur la carte
  sF -- le lien tient dans les deux conventions.
- **P-M9a : NON CONCLUANT.** rho(T, K5_min) = +0.4857 (N=56) / +0.9429
  (N=64), seuil +-0.80 exige AUX DEUX troncatures. **La compensation C2 se
  declenche, texte gele : plus aucune manche quantique, a quelque degre que
  ce soit, sans un estimateur change ET muni d'une derivation.** C'est
  desormais une contrainte permanente de la campagne.
- **P-M9b : zone intermediaire, consigne sans lecture** (Q de 3.11 a
  2.4e10). Proximite consignee : Q(1.35) = 3.11 frole la branche <= 3 a
  3.7 % sans la declencher -- la fourche est mecanique, la proximite est
  une donnee.
- **P-M9c : ALERTE declenchee** (sqrt2 : 0.598 hors [0.80, 1.25]) ->
  investigation obligatoire AVANT interpretation de P-M9a. RESOLUE
  ci-dessous.
- **P-M9-null : PASSE** (1.9e-23).

### Le piege, nomme avant qu'il ne morde

A N=64 : rho = +0.9429 (p = 0.0083) sur 6 points, et le sous-ensemble
canonique redonne EXACTEMENT le +1.00 de M3 (p = 0.042) -- memes systemes,
cette fois. La lecture motivee dirait « la replication a reussi, N=56
gache ». INTERDIT : la porte exigeait les deux troncatures precisement
parce que les magnitudes ne sont pas convergees ; choisir la troncature qui
arrange apres coup est du double-dipping, et multiplier les p des deux N
(correles) l'est aussi. **Statut gele du +1.00 canonique a N=64 : echo non
puissante, consigne** -- ni verdict, ni replication.

### Diagnostic G7 (les faits)

A N=56, les rangs se decident sur des ecarts de 0.5 % (2.00 vs 2.85) et
1.4 % (1.35 vs 1.80) sous des derives de troncature de 23 a 87 % : rangs
NON resolus. A N=64, le plus petit ecart est 4.4 % : rangs resolus, une
seule inversion (1.80/2.00, ecart 41 % -- reelle, pas du bruit).
rho(T56, T64) = +0.66 : la resolution de rang acquise par M8 (+1.00, cote
+1) NE s'est PAS transportee aux systemes sgn_F -- **le cote fragile est
plus dur en troncature** (hypothese mecanique : il fuit plus, donc plus de
poids pres du mur). T56/T64 de 0.59 a 1.87, sens non uniforme (2.85 seul a
monter avec N).

### INVESTIGATION P-M9c : RESOLUE (machine 1, hors gel, 6 diagonalisations)

**Test croise decisif -- mon moteur x entrees exactes de M3 :**
| point | T(mon moteur, entrees M3) | T_M3 | ratio |
|---|---|---|---|
| sqrt2 | 8.23435e-3 | 8.23370e-3 | **1.000** (0.008 %) |
| 1.35 | 4.25981e-3 | 4.25970e-3 | **1.000** (0.0003 %) |

**Les deux moteurs quantiques sont numeriquement identiques.** L'ecart
P-M9c est ENTIEREMENT porte par les entrees : Delta g = +0.5 a +0.8 %,
Delta s0 = -0.28 % (l'ecart de spec (h), 7.04 vs 7.00) produisent des
ecarts de sortie de -40 % a +16 %. Sensibilites locales effectives
|Delta ln T| / |Delta ln g| : **12.7 (2.00), 18.1 (2.85), 20.4 (1.35),
80.6 (sqrt2)**. Trajectoire en N a sqrt2 (entrees M9) : 6.62 / 7.09 /
4.93 / 5.39 e-3 pour N = 48/56/64/72 -- NON monotone, +-30 %.
**Mecanisme candidat, etiquete NON teste** : sqrt2 est le seul point
irrationnel de la grille ; quasi-degenerescences du spectre libre
(min |-n1 + sqrt2 n2| ~ 0.012 a (41, 29) dans la boite) tres inferieures
aux couplages x^5 -> melanges quasi-degeneres hypersensibles aux entrees
et a N. Prediction datee, non gelee : la sensibilite locale devrait
chuter aux points rationnels et culminer pres des irrationnels forts --
coherent avec 12.7/20.4 (rationnels) vs 80.6 (sqrt2).
**Bonus structurel** : l'identite des moteurs a 0.008 % est la premiere
validation croisee du pipeline QUANTIQUE entre deux implementations
(reserve de lignee : les deux descendent de sessions Claude ;
l'independance est celle des codes, pas des auteurs).
**Demande symetrique a machine 2, non bloquante** : leur moteur x entrees
M9 a sqrt2 (attendu ~4.92e-3) pour boucler le carre.

---

## E21 -- L'item (h) du gel M9 v2 sous-estimait la propagation d'un ordre
## de grandeur (defaut conjoint, certifie par les deux machines)

(h) chiffrait la propagation de l'ecart de spec nbar 7.04/7.00 a « ~3.4 %
pire cas sur T », via la pente SECANTE dlnT/dlng ~ 4 -- mesuree entre des
g differant de x1.4, c'est-a-dire moyennee sur les oscillations. La pente
LOCALE aux points calibres vaut 13 a 20 (points rationnels) et ~80
(sqrt2) : la propagation reelle atteint -40 % a sqrt2, hors de la fenetre
P-M9c que (h) declarait sure. **Redige par machine 1, certifie par
machine 2 : les deux ont manque la distinction.** Aucune porte n'a rendu
de faux verdict -- l'alerte pre-declaree P-M9c a fait exactement son
travail, et le test croise a localise la cause en un tour. **Lecons a
geler** : (i) toute propagation d'incertitude declare sa pente comme
LOCALE ou SECANTE ; une secante ne borne rien pres d'une structure
quasi-degeneree ; (ii) la sensibilite locale de T est elle-meme un
observable, variable d'un ordre de grandeur en w2 -- elle entre au cahier
des charges de l'estimateur (C2).

---

## CONSIGNATIONS ANNEXES

- **G1b reclassee** : 0.00 % exact aux six points = chemins deterministes
  IDENTIQUES (le script M8 etait un fork de la lignee m7) -- G1b a teste
  la stabilite d'environnement, pas l'independance d'implementation.
  L'independance classique reste G1a (jet M3, 0.01-0.78 %) ; l'independance
  quantique est acquise ce jour (0.008 %, supra).
- **Cote fragile** : inversion confirmee a 1.80 (frag = +1, asym -26 %),
  et asym(2.40) = +65 % -- HORS de mon attente gelee (5-40 %).
- **Q est fortement dependant du cote** : Q(2.85) passe de 0.647 (cote +1,
  M8) a 9.42 (cote fragile, M9), x15 par le seul signe de s0.
- **Attentes gelees : ~6/9 dans les fourchettes** (canoniques 2/2 ; 6 pts
  N=56 in, N=64 OUT au-dessus ; fenetre P-M9c RATEE ; asym 2.40 OUT ;
  retourne(2.00) et exclusions OK). La calibration des attentes reste
  moyenne ; leur role consultatif reste justifie.

## REGIME POST-C2 (etat de la campagne)

- **Bloque** : toute manche quantique, tout degre, jusqu'a un estimateur
  change ET derive. Le cahier des charges est desormais CHIFFRE par
  M7+M8+M9 : robuste a des derives de troncature x0.6-1.9, a des
  sensibilites d'entree 13-80, aux quasi-degenerescences aux w2
  irrationnels ; les profils C1 (ghost/retourne/g_cal, 12 points sur deux
  cotes) sont l'intrant.
- **Ouvert (classique)** : derivation de r (attaque papier, cout quasi
  nul) ; bord droit (3,1) via Chirikov ; « la loi C : mecanisme et
  derivation ».
- **Statut H-PROFONDEUR** : jambes classiques solides (porteurs,
  creux/fond ordinal, argmin x3 dont les deux conventions) ; jambe
  quantique VIVANTE mais NON soutenue -- trois manches puissantees, zero
  verdict, des echos positifs non puissantes qui s'accumulent en
  consignation (+1.00 canonique N=64, +0.9429 six points N=64), et la
  demonstration que le goulot est l'OBSERVABLE, ni la physique ni le
  protocole. C'est exactement ce que C2 force a corriger avant de
  continuer.

## BOUCLES

- Transmettre m9_results.json (41595413...) pour la reconciliation
  JSON-niveau ; demande symetrique du test croise (non bloquante).
- Note FR / contenu du bundle (inchange). Integration au maitre :
  §18 a §26 + E16-E21 + D1-D3.
