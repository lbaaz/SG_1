# Journal bundle 5 -- DELTA du 25/07/2026 (nuit) : section 21 (M7 executee),
# DECISIONS, annotation M5, options M8

*S'insere apres le delta §19-§20 + E16-E17 (fichier
journal_delta_19-20_E16-E17.md, sha256 f222e57c87f02e8ac4708e95bb87379b4040
fe7a2a23996ab7ec8cd695d4346a).*

---

## 21. MANCHE M7 EXECUTEE (machine 2) -- P-M7a CONFIRMEE, P-M7b NON
## CONCLUANTE ; le diagnostic est une question de RESOLUTION, pas un verdict

**Artefacts** : m7_run.log recu (machine 1). sha256 du JSON annonce par le
run : b7493af743bd1c9bf80e11292edfd501540e3a5549d984ac12950c8e6e1df24e --
**fichier non transmis a ce stade** ; la reconciliation ci-dessous porte sur
le LOG (s*, K7, g_cal, T, gardes, rho : tout recalcule, zero ecart avec les
valeurs affichees ; la reconciliation JSON-niveau, histos compris, reste a
faire a reception). Trace executable : audit_m7_log.py.
Certification : gel 5c54ac03... conforme, script 11b143b6... conforme,
G3 backward 4.4e-16.

### Etage 1 -- classique

| w2 | 1.35 | sqrt2 | 1.80 | 2.00 | 2.40 | 2.85 |
|---|---|---|---|---|---|---|
| s* | 0.2600 | 0.2976 | 0.5214 | 0.3923 | 1.4642 | 1.9423 |
| K7 | 5.94e-5 | 1.17e-4 | 1.93e-3 | 4.64e-4 | 0.336 | 1.382 |

- **P-M7a : LIEN CONFIRME.** argmin K7 au bord gauche (1.35), pas au point
  resonant -- la prediction rho > 0 conserve sa derivation. Le creux resonant
  est VISIBLE dans la carte (K7(2.00) x4.2 sous K7(1.80)) mais n'ordonne rien.
- **Calibration** : 5/6 points a <= 1.9 % ; **w2 = 2.40 EXCLU par G5**
  (11.39 %, regle mecanique). Observation post-hoc etiquetee : c'est le point
  de la VALLEE (zone de recouvrement 2:1/3:1 de la note §3(a)), et
  l'invariance de K y casse entre g = 0.05 et g_cal = 0.131 alors qu'elle
  tient a 0.06 % a 2.85 avec g_cal = 0.88. Compatible avec une invariance
  affaiblie dans la vallee ; non teste, a l'inventaire.
- **Gardes vertes** : G1 regression 0.001 % ; G2 0.00/0.06 % ; **G4 correctement
  ciblee cette fois** -- le critere corrige (max g s*^(p-1)) a designe
  w2 = 2.85, g_cal = 0.88, la ligne authentiquement la plus raide de la
  campagne, ecart dt/2 = 0.000 %. La lecon M6 a fonctionne.
- Nota : les g_cal s'etendent de 2.37e-5 a 0.88 -- x37 000 entre points. La
  limitation gelee ("M7 teste un signe, pas un mecanisme ; le mediateur n'est
  pas identifie") pese donc lourd : la "meme physique classique a nbar fixe"
  s'achete au prix d'un g qui varie de plus de quatre ordres.

### Etage 2 -- quantique, et le verdict

| w2 (retenus) | 1.35 | sqrt2 | 1.80 | 2.00 | 2.85 |
|---|---|---|---|---|---|
| T (N=56) | 1.332e-2 | 2.230e-2 | 1.101e-2 | 6.836e-3 | 1.283e-2 |
| T (N=64) | 1.460e-2 | 1.926e-2 | 7.058e-3 | 1.293e-2 | 1.940e-2 |
| T56/T64 (G7) | 0.91 | 1.16 | 1.56 | 0.53 | 0.66 |

- **P-M7b : NON CONCLUANT contre sa porte.** rho(T,K7) = -0.50 (N=56) /
  +0.10 (N=64), signes discordants, aucun n'approche +-0.80. p exacts
  reportes comme exige (0.225 / 0.475). Verrou anti-arret-optionnel : non
  applicable (aucun rho dans [0.60, 0.80)) ; toute suite est une manche
  neuve de toute facon.
- **P-M7-null : PASSE** (FREE = 1.9e-23 aux deux points). Queues <= 2.2e-16 :
  aucune exclusion G6.

### Diagnostic de resolution (la vraie information de la manche)

Recalcule du log : la derive de troncature va de x0.53 a x1.56 avec une
DIRECTION variable par point ; **rho(T56, T64) = +0.60** -- le classement de
T n'est pas meme stable entre les deux troncatures. L'etendue de T sur les
points retenus est x2.8-3.3, contre x23 268 pour K7 : l'observable est quasi
PLATE la ou la robustesse classique varie de quatre ordres, et les rangs se
decident sur des ecarts de 0.73 % (sqrt2 vs 2.85 a N=64) a 3.8 % -- tres en
dessous de la derive de troncature. **La mesure ne resout pas le classement.**

**Sur la "cause identifiee" (formule du resume machine 2) : NON -- deux
causes candidates, non departagees, et les nommer "identifiees" serait
E15-bis.**
  (1) Troncature a Delta n = 7 : compatible avec l'inquietude PRE-declaree
      (§20, faiblesse n°3 : tampon de coquille ~1.4 sauts a N=56), soutenue
      par la non-uniformite de G7 -- c'est la candidate favorite, et elle a
      l'avantage d'avoir ete ecrite avant lecture.
  (2) Correlation reellement faible ou nulle : soutenue par le point suivant.
Aucune montee en N ne departagera (2) : si rho vrai ~ 0, N = 72 donnera un
troisieme signe aleatoire.

### La donnee qui borne tout test quantique a degre impair

GHOST / signe retourne = **2.61** (1.35) et **3.27** (2.85). Consigne comme
donnee brute, aucune conclusion dans M7 (gel respecte). Lecture POST-HOC
etiquetee, pour le design de M8 : a p impair le systeme retourne est LUI
AUSSI non borne (derivation (d)) et fuit presque autant que le fantome --
T contient un canal generique de barriere x^7 qui pese ~1/3 a 1/2.5 du
signal. **La composante specifiquement fantome de T est bornee a ~x3.** Un
rho(T, K7) ne pouvait capter qu'une fraction du contraste ; c'est un argument
de design, pas un verdict.

### Le piege a eviter, nomme avant qu'il ne morde

P-M7c/d, cellule "4 canoniques, N=64, rho(T,C7) = +1.00, p = 0.042" : c'est
LA cellule qu'une lecture motivee saisirait. Interdit : (i) aucune porte
(gele explicitement, "choisir apres coup celui qui arrange serait du
double-dipping") ; (ii) une cellule sur HUIT rapportees -- 0.042 ne survit a
aucune correction de comparaisons multiples ; (iii) elle tient sur le MEME
ecart de 0.73 % entre sqrt2 et 2.85 que le diagnostic ci-dessus declare etre
du bruit ; (iv) son homologue N=56 vaut +0.40. Elle est consignee, elle n'est
pas un resultat.

### Statistique declaree du §20 : premiere verification

creux_K/fond_K a p=7 = 11.6 / 23 268 = **5.0e-4**, contre 0.88 a p=3.
L'effondrement predit (date du 25/07, avant lecture -- statut : declaration
datee, PAS pre-enregistrement, les donnees existaient sur machine 2) est
verifie a p=7, et la table des fonds s'ordonne :
  etendue du fond : p=3 x17 ; p=4 x55 ; p=6 x1953 ; p=7 x23 268.
Avec E17 (creux en K quasi constant aux impairs : 15.4 / 11.1 / 11.6),
l'histoire structurelle s'unifie : **ce n'est pas le canyon qui retrecit avec
p, c'est le fond qui explose.** Ce que p=3 a d'exceptionnel : un fond
suffisamment plat pour que le canyon l'ordonne. Reste du : creux/fond a p=5
(attend m3_calib.json).

### Statut de H-PROFONDEUR apres M7

Jambes classiques : solides (porteurs M6, decroissance-en-s* M6 avec
l'annotation E17, ordonnancement P-M7a, cote raide (i) passe sur trois
degres). **Jambe quantique : toujours jamais testee avec puissance.** M7 non
concluante ; et si la grille p=5 de M3 compte n=3 points (boucle ouverte
§20.2), alors rho = +1.00 y vaut p = 0.167 et AUCUN rho quantique
significatif n'existe a degre impair dans toute la campagne. La verification
de cette taille de grille est devenue LE prealable a tout M8.

---

## DECISIONS (25/07, consignees pour la chaine)

**D1 -- Metrique G3 : NOTE D'EXPLOITATION, pas d'erratum.** Critere de chaine
adopte et enonce ici : un numero E marque un defaut entre dans un artefact
gele/certifie ou un livrable, et susceptible de porter sur des conclusions ;
les attrapes de pre-vol qui n'ont touche aucune donnee vivent dans les notes
de livraison et les sections de journal. Cas G3 : l'identite mathematique du
gel est exacte (l'algebre EST exacte) ; ce qui a echoue est la METRIQUE de
verification v1 (erreur relative avant sur une somme mal conditionnee),
defaut d'implementation attrape au pre-vol, aucune donnee touchee, aucun
verdict affecte, lecon deja propagee (G3 du gel M7 enonce la metrique
backward et sa raison). Decision reversible en une ligne : si l'humain la
promeut, elle prend le numero E18. [La reservation informelle "E16" de la
note de livraison M6 etait deja levee au §20.]

**D2 -- Patch "Q/Q1_null" des verdicts M5 : REFUSE.** La branche LIMITE de
P-M6c prevoyait "correction appliquee et documentee" ; la correction que le
gel imaginait (division par un null constant) n'est PAS soutenue par les
donnees de la manche meme qui devait la calibrer : (i) les deux nulls
different de 21 % (1.41 / 1.16) ; (ii) Q1(7) = 1.17, AVEC porteurs, est sous
le null p=4 ; (iii) structurellement, aucun null n'est mesurable aux degres
impairs -- ceux ou Q sert. Diviser par 1.4 transporterait une mesure d'un
degre a un autre. La correction documentee est donc la REQUALIFICATION
(§19) : Q instrument ordinal, contamination 16-41 % mesuree aux pairs, non
transportable. Les verdicts M5 tiennent en ordre. A la place du patch,
l'annotation ci-dessous est a coller dans le maitre.

**Annotation a inserer en tete du §17 (et a referencer depuis §15/M3) :**

> **[ANNOTATION P-M6c + E17 (25/07) : Q est requalifie en instrument ORDINAL.
> Contamination d'asymetrie de modes 16-41 % mesuree aux degres pairs (M6 :
> Q1(4) = 1.41, Q1(6) = 1.16), non transportable aux impairs, ou aucun null
> n'est mesurable (les porteurs y existent toujours). Les verdicts de M5
> tiennent en ORDRE ; les magnitudes Q = 57.5 et Q = 4.375 ne sont pas des
> rapports calibres, et leur comparaison inter-degres depend de l'unite
> (E17 : en unites K, 51.9 contre 82.9 -- le sens s'inverse). Voir §19, §21.]**

---

## Boucles ouvertes -- etat consolide apres M7

1. **Taille de la grille p=5 de M3 (n = 3 ou 4 ?)** -- PREALABLE a M8 : fixe
   ce que M8 doit etablir (premier test puissante a degre impair, ou
   replication d'un resultat p=5 deja significatif). Cout : lecture
   d'artefacts, zero calcul.
2. Reconciliation JSON-niveau de M7 (fichier b7493af7... non transmis).
3. creux/fond a p=5 (attend m3_calib.json).
4. Note FR : chiffres perimes ("cinq erreurs", "deux re-executions") ; lie a
   la decision du contenu du bundle expedie. bundle5.py joint : a trancher.
5. Integration au maitre : deltas §18, §19-§20 + E16-E17, §21 + annotations.
6. Arbitrage D1 si l'humain veut le renverser (-> E18).

---

## M8 -- OPTIONS DE DESIGN (rien n'est gele ; couts et angles, au choix)

L'indecision de M7 a deux causes candidates non departagees ; un bon M8 doit
pouvoir les distinguer, pas seulement "monter N".

- **(a) Monter la troncature** (N = 72, voire 80 : dim 6400, eigh ~1.3 Go,
  faisable machine 2). Attaque la cause (1) seulement. Si rho vrai ~ 0
  (cause 2), N = 72 produit un troisieme signe aleatoire et rien n'est
  appris. Rupture de comparabilite M1/M3 a assumer dans le gel.
- **(b) Re-deriver la coquille pour Delta n = 7** (descendre/elargir le
  tampon, ex. coquille 30-40 a N = 64 : ~3.4 sauts). Attaque la cause (1)
  par l'autre bout, casse la comparabilite avec §8 -- deja douteuse a p
  impair de toute facon.
- **(c) Observable differentielle T_ghost / T_retourne par point.** La seule
  option qui attaque la cause (2) : elle soustrait le canal generique x^7
  (le x2.6-3.3 mesure) et isole la composante fantome. Cout : +6 a +12
  diagonalisations. C'est aussi la reponse structurelle a l'absence de
  temoin borne aux impairs (derivation (d)).
- **(d) D'abord, cout nul : trancher la boucle n°1** (grille p=5). Elle
  decide de l'enjeu de M8 avant d'en ecrire le gel.

Suggestion de sequencement, a valider : (d), puis un gel M8 combinant (c)
avec (a) ou (b) selon ce que (d) revele. Un gel M8 qui ne ferait que (a)
laisserait la cause (2) intacte et risquerait une deuxieme manche non
concluante au prix fort.
