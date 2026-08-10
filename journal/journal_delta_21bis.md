# Journal bundle 5 -- DELTA du 25/07/2026 (nuit, suite) : section 21-bis,
# ERRATUM E18, cadrage M8

*S'insere apres journal_delta_21.md (sha256 2ae4799f725c6444bfb03a237a2c94fd
6fb58d2408d865988eeafe45d4f69197). Trace executable :
audit_fermetures_2026-07-25.py.*

---

## 21-bis. FERMETURES CERTIFIEES PAR MACHINE 2, ET CE QU'ELLES REVELENT

**Certifications recues** : note 25q reproduite au sha annonce (265e64de...),
audit_m7_log rejoue a zero ecart, custody M6 conforme (JSON 99674ad7..., gel
048900d8..., script c92e67de..., volets {A:15, B:8, C:2, E:3}). Nota de
methode : le replicateur a adapte le chemin d'audit_m6_brut.py EN SCRATCHPAD,
fichier livre intact -- la bonne pratique exacte (E12/E13 : ne jamais muter
un artefact livre).

### Boucle 1 FERMEE : la grille p=5 de M3 compte n = 4

Le log M3 l'imprimait ; m3_calib.json (4 lignes non exclues) et
m3_quantum_N64.json (4 points GHOST) le corroborent. Consequences :
- rho(T, K5) = +1.00 vaut p = 1/24 = 0.042 : **marginal mais reel**, au meme
  niveau exactement que le -1.00 de p=3 (n = 4 aussi).
- Le flip de signe p3 <-> p5 -- le coeur empirique quantique de H-PROFONDEUR
  -- repose donc sur DEUX resultats marginaux a n = 4, et l'hypothese a ete
  formee APRES les avoir vus : **aucune inference jointe n'est licite**
  (0.042 x 0.042 est interdit deux fois : post-hoc ET correlation de design).
- La seule prediction quantique genuine (pre-enregistree avant mesure) reste
  la conditionnelle de M7 -- sortie NON CONCLUANTE. **M8 sera donc : la
  replication puissantee d'un marginal (p=5) ou le premier test puissante
  (p=7), pas une premiere detection dans les deux cas.**

### Boucle 3 FERMEE : creux/fond a p=5 = 11.07/580 = 0.019 [machine 2,
### m3_calib.json -- fond x580 non re-verifiable sur machine 1, provenance
### etiquetee]

Arithmetique verifiee (D(5,0.10)^3 = 11.075 ; 11.075/580 = 0.0191). Le fond
p=7 restreint au triplet canonique {1.35, sqrt2, 2.85} vaut 23268, identique
au fond 6 points (min et max canoniques) : la comparaison inter-degres est
like-for-like sur le meme triplet pour tous les p.

### Regularite decouverte en verifiant (post-hoc, a deriver) : r(p) ~ const

fond_K = r^(p-2) avec r = s*max/s*min bord-a-bord est une IDENTITE (K est
defini par s*) -- le tableau "ecart 0.0 %" de la trace est circulaire et ne
teste rien. **Le contenu empirique est la constance de r** :

| p | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|
| r = s*(2.85)/s*(1.35) | **17.4** | 7.44 | 8.34 | 6.65 | 7.47 |

r ~ 6.6-8.3 pour p >= 4, sur les DEUX parites -- la carte s* bord-a-bord est
presque invariante en degre, et toute l'explosion du fond en K est la
puissance (p-2) de cette constante. p=3 est hors norme (x2.3 au-dessus du
peloton). Cause candidate, NON testee, a l'inventaire : a interaction
IMPAIRE de degre 3 la regle de selection de parite (§3(b) de la note, etablie
pour le quartique) ne s'applique pas telle quelle -- la structure resonante
du bord peut differer. Statut : observation post-hoc sur les cartes
existantes, candidate a derivation ; r(p) invariant serait un ENONCE
DERIVABLE de la meme famille que la loi C.

---

## E18 -- La phrase-bilan du §21 enfreint la lecon d'E17 (unite non declaree,
## seconde echelle absente)

§21 conclut : « ce n'est pas le canyon qui retrecit avec p, c'est le fond qui
explose ». Cette phrase est vraie EN UNITES K et fausse EN UNITES s* -- ou
c'est exactement l'inverse (canyon D : 15.4 -> 2.23 -> 1.63 decroissant, fond
r ~ constant). La lecon d'E17, gelee la veille dans le meme flux de
livraison, exigeait : « toute comparaison inter-degres doit declarer son
unite ET montrer qu'elle est invariante, ou donner les deux echelles ». Le
§21 ne l'a pas fait pour sa phrase-bilan. Table complete des deux lentilles :

| p | creux/fond en s* (= D/r) | creux/fond en K (= (D/r)^(p-2)) |
|---|---|---|
| 3 | 0.884 | 0.884 |
| 5 | 0.267 | 1.9e-2 |
| 7 | 0.219 | 5.0e-4 |
| pairs | sans objet (D ~ 1, aucun creux) | sans objet |

Les deux lentilles s'accordent sur l'essentiel : p=3 tres au-dessus de
p >= 5, decroissance monotone. Elles divergent sur l'amplitude p5 -> p7
(quasi plat en s*, x38 en K). **L'enonce invariant est ordinal** :
l'inegalite de reordonnancement (le creux passe-t-il sous le fond ?) survit a
toute transformation monotone -- c'est l'objet exact de P-M7a, qui etait donc
la bonne porte. La DECLARATION du §20 reste valide telle que declaree (elle
nommait explicitement « creux_K / fond_K ») ; la prediction datee est
verifiee dans son unite declaree ET s'affaiblit en amplitude dans l'autre --
les deux sont dites, desormais.

**Formulation de remplacement pour le bilan structurel** (a substituer
partout ou la phrase du §21 serait reprise) :
> *Le rapport creux/fond decroit avec p dans les deux lentilles -- fortement
> en K, faiblement en s* -- et seul p=3 a un creux comparable a son fond
> (0.88) ; c'est l'enonce ordinal, invariant d'echelle, qui explique que la
> resonance n'ordonne la carte qu'au degre cubique (P-M7a).*

**Numerotation** : D1 (§21) reservait conditionnellement « E18 » a une
eventuelle promotion de l'arbitrage G3. Ce present erratum consomme E18
(precedent : E16, meme dance) ; une promotion ulterieure de G3 prendra le
prochain numero libre. Deuxieme renumerotation du meme type en une journee --
lecon : **ne plus jamais reserver de numero d'erratum conditionnellement ;
les numeros s'attribuent a la consignation, pas a la prevision.**

---

## CADRAGE M8 (mis a jour ; rien n'est gele, go attendu)

Les fermetures changent la recommandation du §21 :

**Recommande : M8 = p=5 en grille de SIX points** ({1.35, sqrt2, 1.80, 2.00,
2.40, 2.85}), N = 56/64, meme pipeline que M7.
1. Il existe desormais une cible de replication (rho = +1.00 marginal,
   p = 0.042) : la porte rho >= +0.80 aux deux troncatures (p <= 0.029)
   serait la premiere prediction quantique risquee ET puissantee de la
   campagne -- derivee de M3 + H-PROFONDEUR, pas inventee.
2. p=5 est mieux conditionne que p=7 : Delta n <= 5, tampon de coquille
   ~2 sauts a N=56 et ~3.6 a N=64 (contre 1.4 a p=7) -- la cause (1) de
   l'indecision M7 y mord moins.
3. Comparabilite M3 preservee (memes troncatures, memes 4 points canoniques
   inclus).
4. Co-observable a geler : T_ghost / T_retourne aux six points -- mesure le
   canal generique x^5 (l'analogue du x2.6-3.3 de p=7) et teste au passage
   l'hypothese de design : si le rapport est GRAND a p=5, cela explique
   pourquoi p=5 peut montrer un rho propre la ou p=7 se noie ; s'il est ~3
   aussi, la cause (2) de M7 menace aussi p=5 et le gel doit le dire.
5. Cout : ~11 recherches classiques + ~20 diagonalisations, ~10 min.

p=7 est DIFFERE : y retourner sans observable differentielle ni re-derivation
de coquille rejouerait l'indecision au prix fort. Si M8-p5 replique, le
redesign p=7 devient la manche d'apres, arme du rapport ghost/retourne
mesure ; si M8-p5 ne replique pas, la jambe quantique de H-PROFONDEUR meurt
a bas cout -- kill-it-first dans les deux branches.

**Boucles ouvertes restantes** : reconciliation JSON-niveau M7 (fichier
b7493af7... a transmettre) ; note FR / contenu du bundle ; integration des
deltas au maitre (§18, §19-§20+E16-E17, §21, §21-bis+E18) ; arbitrage D1 si
renverse (prochain numero libre).
