# Journal bundle 5 -- DELTA du 26/07/2026 : section 27 -- DERIVATION DE r
# (noyau exact demontre, exposant NON derive), et deux auto-catches

*S'insere apres journal_delta_26bis.md (sha256 b1424a31eb5ffbb43fee103b0c260
865be4053fa552ed86512d441ae68080e48). Trace executable : audit_derivation_r.py.
Statut global : resultat PARTIEL et honnete -- le noyau se demontre, la clef
de voute manque, et la manche M10 (gel depose separement) va la chercher.*

---

## 27.1 CE QUI SE DEMONTRE (et qui est verifie numeriquement)

### (i) Reduction : le systeme se referme sur UNE equation

En appliquant (dt^2 + w2^2) a l'equation du mode 1, (dt^2 + w1^2) a celle du
mode 2, et en additionnant, les termes de couplage se recombinent en
(w2^2 - w1^2) x (dV/dx)/Delta = dV/dx :

  (dt^2 + w1^2)(dt^2 + w2^2) x = g x^(p-1),   x = x1 + x2

C'est l'oscillateur de Pais-Uhlenbeck en forme du quatrieme ordre, avec sa
non-linearite. **VERIFICATION NUMERIQUE (test dynamique, pas algebrique)** :
integration independante des deux systemes (modes vs 4e ordre) sur [0, 25],
RK4 dt = 1e-4 -- ecart relatif max 9.6e-14 (w2=1.35, p=5), 7.7e-14
(2.85, p=7), 6.0e-14 (2.00, p=3). La reduction n'est pas une manipulation
formelle : les deux systemes tracent la meme trajectoire.

### (ii) La famille de CI de la campagne s'effondre en quatre nombres

Avec A1 = s(1+w2^2)/Delta, A2 = -s(1+w1^2)/Delta :
  x(0)   = A1 + A2                = s        (identite exacte)
  x'(0)  = 0
  x''(0) = -w1^2 A1 - w2^2 A2     = s        (identite exacte, TOUT w2)
  x'''(0)= 0
Verifie a 1e-16 sur (w2, s) varies. **Le parametre s de toute la campagne
n'est donc pas un reglage : c'est l'amplitude initiale de la coordonnee
d'interaction elle-meme**, et la famille est la diagonale x(0) = x''(0).

### (iii) Identite d'energie

E0 (part quadratique) = -Delta s^2 / 2, exactement -- toujours negative :
le fantome domine cette famille par construction. Energie totale conservee
E = -Delta s^2/2 + (g/p) s^p. **Verifie** : la forme a masses (-Delta, +Delta)
se conserve a 1.2e-12 sur [0, 25].

### (iv) K = g s^(p-2) est LE parametre, pas une commodite

Le rescaling x = lambda X a temps fixe (le temps n'est pas rescalable, les
frequences le fixent) donne un coefficient non lineaire g lambda^(p-2) :
c'est l'unique combinaison invariante. Le probleme sans dimension est

  X'''' + (1+w2^2) X'' + w2^2 X = K X^(p-1),  X(0)=X''(0)=1, X'(0)=X'''(0)=0

donc le seuil est une fonction K*(w2; p) SEULE, et s* = (K*/g)^(1/(p-2)).
**Ceci DERIVE l'invariance en g de K**, mesuree par G2 (x2) puis par la
consignation A du S26-bis (x0.017 a x13, <= 0.25 %). Verification directe
supplementaire de machine 1, sur DEUX decades de g (0.005 / 0.05 / 0.5) :
dispersion de K = 0.53 % (p=5, w2=1.80) et 1.42 % (p=7, w2=2.40).
La derivation arrive APRES la mesure : c'est une post-diction, et c'est le
bon ordre.

### (v) Consequence exacte : r est un rapport de seuils a couplage unite

Avec a = K^(1/(p-2)) = s g^(1/(p-2)) (amplitude du probleme a couplage 1) :

  **r(p) = a*(2.85) / a*(1.35)**, exactement.

## 27.2 CE QUE LE CALCUL REVELE : r est l'ombre a deux points d'une loi

r = [Delta(2.85)/Delta(1.35)]^beta = **8.6596^beta**. Tout est dans beta,
ajuste en log-log sur les points hors resonance :

| p | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|
| beta | **1.32** | 0.95 | 1.02 | 0.88 | 0.91 |
| 8.66^beta | 17.2 | 7.7 | 9.1 | 6.6 | 7.1 |
| r mesure | 17.48 | 7.44 | 8.34 | 6.65 | 7.10 |

**« r quasi-constant pour p >= 4 » EQUIVAUT a « beta ~ 0.92 », c'est-a-dire
s* proportionnel a Delta = w2^2 - w1^2.** Et l'anomalie de p=3 n'est pas un
rapport bizarre : c'est un EXPOSANT different. La loi vit sur cinq points par
degre au lieu de deux -- elle est bien plus attaquable, et c'est l'objet de
M10.

**Lecture physique de beta = 1** : A2 = 2s/Delta est l'amplitude initiale du
mode SAIN (energie positive). beta = 1 <=> A2 constant au seuil. L'enonce
serait : *le seuil est atteint a amplitude fixe du mode d'energie positive,
quelle que soit w2*.

## 27.3 CE QUI N'EST PAS DERIVE -- beta lui-meme, et DEUX MECANISMES MORTS

- **Equilibre d'energie** (g/p)s^p ~ |E0| = Delta s^2/2 => K* ~ p Delta/2
  => beta = 1/(p-2) => r = 2.94 / 2.05 / 1.72 / 1.54 pour p = 4..7.
  Mesure : 7.44 / 8.34 / 6.65 / 7.10. **MORT.**
- **Fermeture de largeur resonante** (mecanisme du pont) : r = [G(1.35)/
  G(2.85)] x 18.28^(1/(p-2)) avec G = (3+w2^2)/Delta. Le prefacteur 3.755
  est p-independant (bonne structure) mais l'exposant residuel tue :
  16.1 / 9.9 / 7.8 / 6.7. **MORT.**
  (L'estimation utilise eps = 0.15 aux deux bords, avec 3:2 et 3:1 comme
  resonances atteignables -- choix declare, non derive.)
Les deux echouent DE LA MEME FACON : ils predisent un r decroissant. C'est
de l'information : ce qui fixe le seuil ne peut etre ni un simple bilan
energetique, ni la fermeture d'UNE resonance -- il faut un mecanisme qui
produise un exposant p-independant.

## 27.4 AUTO-AUDIT : DEUX « CONTROLES » DE MOI, CIRCULAIRES, RETIRES

*Regle D1 appliquee (un numero E marque un defaut entre dans un artefact
gele ou un livrable) : ces deux enonces ont ete faits a l'oral a machine 2 et
retires AVANT d'entrer dans le present delta -> note d'exploitation, pas
erratum. A promouvoir par machine 2 si elle juge autrement.*

1. **« La loi beta reproduit la loi C aux bords a 8 % »** : C est DEFINI
   comme K/[(w2-1)^2 (w2+1)] et beta est ajuste sur les MEMES K. Le test ne
   compare que le fit 3 points a ses deux extremites : quasi tautologique.
   **RETIRE de la liste des controles.**
2. **« A2 plat a +-11 % quand A1 varie de x3 »** presente comme trois tests :
   A1, A2 et max|x| sont lies algebriquement a s* ; une fois beta ~ 1 mesure,
   la platitude de A2 et la variation de A1 SONT LA MEME AFFIRMATION.
   **Enonce corrige** : les donnees selectionnent beta ~ 1 dans la famille
   s* ~ Delta^beta, et beta = 1 SE LIT comme « amplitude du mode sain fixee ».
   Une lecture, pas une preuve.

## 27.5 RESERVES SUR LES DONNEES (sans lesquelles le tableau ne vaut rien)

- **beta(4) n'est pas solide** : 0.947 (K4 machine 1 seance) contre 0.927
  (K4 machine 2 calib.json) -- l'ecart de provenance deplace r predit de
  7.72 a 7.40. Lecon E20 en action.
- **beta(4) et beta(6) reposent sur 3 points** de cartes M1 dont la
  **convention de signe n'est pas confirmee** (seul p=3 l'est : r(3)_min).
- **Residus du fit** : p=5 : +10.6 / -4.1 / -15.2 / +6.7 / +2.0 % ;
  p=7 : +4.5 / -1.9 / -4.4 / -2.0 / +3.9 %. Le motif est une courbure douce,
  pas une signature de 3:1 au bord droit. **Mais cinq points ne separent pas
  courbure et bruit** -- c'est precisement ce que M10 doit trancher.
  Nota : le residu de -15 % a w2=1.80 (p=5) est au point ou le cote fragile
  s'inverse (frag = +1). Coincidence ou structure : non tranche.
- Le point w2 = 2.00 est exclu partout (c'est le canyon, la deviation A la
  loi -- et desormais la loi donne un sens quantitatif au canyon : le deficit
  de s* par rapport a kappa_p Delta).

## 27.6 CE QUE CA CHANGE POUR LE DOSSIER

- **Le « fond qui explose » est derive** : K* ~ Delta^(p-2) beta, donc
  l'explosion du fond en unites K est la puissance (p-2) d'une carte s*
  quasi-lineaire en Delta. E17/E18 trouvaient l'enonce ordinal ; on a
  maintenant la forme fonctionnelle candidate.
- **La loi C de la note devient un cas particulier approche** : K ~
  (w2-1)^(2beta)(w2+1)^(2beta) contre la forme publiee (w2-1)^2(w2+1). A
  reexaminer si M10 confirme beta -- impact potentiel sur la note d'outreach.
- **Aucun impact sur C2** : tout ceci est classique.
