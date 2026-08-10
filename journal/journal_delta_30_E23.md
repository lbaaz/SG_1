# Journal bundle 5 -- DELTA du 26/07/2026 : section 30 -- M10 v3 CERTIFIEE,
# R-5 levee, ERRATUM E23, gel v4 depose

*S'insere apres journal_delta_29_M10v3.md (sha256 acc789b4bdeeba28f2fefb721e
7f569b86b434f3fccb0523f7182151284e5703). Artefacts recus :
m10_certification_croisee_v3.md, audit_m10v3_machine2.log.*

---

## 30.1 v3 CERTIFIEE, R-5 LEVEE

Empreinte f32104d3... recomputee et concordante. Diff v2 -> v3 verifie exact
et exhaustif, y compris les deux sections que le S29.5 ne citait pas
nommement (motif du PROTOCOLE, P-M10d), controlees ligne a ligne : elles ne
changent que par les coquilles. Les sept coquilles sont nettoyees, verifiees
une par une.

**La derivation de la marge est validee sur le point qui comptait : la
non-circularite.** Machine 2 a recalcule les trois beta effectifs a partir
des seules formes algebriques -- 1.0000 / 0.6513 / 0.4982, ecart au plus
proche 0.3487 contre 0.351 annonce, facteur de separation 3.49 -- et a
verifie qu'AUCUNE valeur mesuree de s* n'y entre. Le poteau n'est pas
deplace vers le resultat.
**Limite inherente, consignee (machine 2)** : le facteur 3.5 vaut pour la
liste des TROIS candidats declaree au gel. Une quatrieme lecture dont le
beta effectif tomberait a moins de 0.10 de 1.000 ne serait pas discriminee.
La liste est declaree, donc la limite est bornee -- mais elle est reelle.

R-5 tombe : sigma < 0.1517 satisfait aux deux degres (0.1168 et 0.0455), la
branche affirmative est atteignable, et sur les attentes ecrites la porte
rendrait NON CONCLUANT DE PHYSIQUE tire par p=7 (IC [0.903, 1.057] a p=5,
contenu ; [0.860, 0.920] a p=7, non contenu et non disjoint). La porte peut
prendre plus d'une valeur : elle est informative.

Machine 2 acte aussi, de son propre chef, avoir traite sigma comme une
dispersion d'echantillonnage dans R-1 et R-5 sans le dire -- tolerable pour
dimensionner une puissance, faux comme lecture d'intervalle. La
requalification en bande de dispersion est retenue des deux cotes.

---

## 30.2 E23 -- P-M10f portait une convention de normalisation, dans un
## artefact CERTIFIE, en contradiction avec l'argument qui l'a motivee

**Fait.** Le gel v3 definit rho_p(w) = s*_p(w)/s*_p(1.25) tandis que le
repere pre-declare (0.2224) est calcule a w0 = 1.35. La statistique depend
du point de normalisation : sur les points disponibles elle vaut 0.2224
(w0=1.35), 0.2836 (sqrt2), 0.2796 (1.80), 0.2836 (2.40), 0.2230 (2.85) --
27 % d'ecart. M10 normaliserait a 1.25, point neuf non mesure : la valeur
produite n'aurait PAS ete comparable au repere, et la lecture pre-declaree
<< si M10 reproduit ce motif >> aurait ete faussee.

**Cause.** Defaut de machine 1. J'ai introduit P-M10f precisement parce
qu'elle est << sans ajustement, donc insensible a l'inadequation >>, puis
j'y ai laisse un degre de liberte arbitraire. L'argument valait aussi pour
w0 ; je ne l'ai pas applique jusqu'au bout. Incoherence interne au
demeurant visible sans aucune donnee : la definition disait 1.25, le repere
disait 1.35.

**Detection.** Certification croisee v3, machine 2 -- qui a certifie quand
meme, P-M10f n'ayant aucune porte, et a propose deux correctifs a cout nul
en indiquant sa preference.

**Correction.** Gel v4 : statistique SANS normalisation, etendue de
d(w) = ln s*_5(w) - ln s*_7(w). Correctif (b) de machine 2, adopte pour la
raison qu'elle donne -- il supprime le degre de liberte au lieu de le fixer
par convention.

**Deux apports de machine 1 a la correction, verifies :**
1. **Propriete d'enveloppe.** etendue(d) = sup sur w0 de
   max_w |ln rho_5 - ln rho_7|. Verifie : 0.2224 / 0.2836 / 0.2796 / 0.2836 /
   0.2230 selon w0, sup = 0.2836 = etendue. La version sans normalisation ne
   choisit donc pas une convention : **elle les majore toutes**. Le repere
   devient bien pose au lieu d'etre conventionnel.
2. **Monotonie en nombre de points, que personne n'avait relevee.** Une
   etendue est un max moins un min : elle ne peut que CROITRE sur un
   sur-ensemble. Comparer l'etendue a 16 points au repere a 5 points aurait
   ete biaise vers le haut, et aurait recree le defaut sous une autre forme.
   v4 exige donc DEUX valeurs : sur le sous-ensemble historique de 5 points
   (seule comparable au repere 0.2836) et sur les 16 points, a cote, sans
   comparaison.

**Portee.** Nulle sur les verdicts : P-M10f n'a aucune porte, aucune donnee
M10 n'existe, aucun resultat anterieur n'en depend. **Premier erratum dans
un artefact CERTIFIE de la campagne** -- la chaine l'a attrape a la
certification, pas avant : c'est le comportement attendu, mais il vaut d'etre
note que la relecture croisee a fait ce que ma propre relecture n'avait pas
fait.

**Lecon a geler.** Quand une statistique est introduite au motif qu'elle est
sans ajustement, l'argument doit etre applique a TOUS ses degres de liberte,
y compris ceux qui ne ressemblent pas a un ajustement -- un point de
reference en est un.

---

## 30.3 GEL M10 v4 DEPOSE (diff minimal sur v3, deja certifiee)

Fichier **m10_pre_enregistrement_v4.md**, 311 lignes, ASCII pur, canonique
NFC+LF :
**sha256 4b497765f94e29bd648407a5c69961c70067bd3d0fa13150a1c3e9701d42a8c4**

Diff v3 -> v4, exhaustif, trois emplacements :
1. HISTORIQUE : entree v4 (motif, renvoi a E23, mention explicite qu'aucune
   porte ni garde ni ensemble de fit ne bouge).
2. P-M10f : reecrite sans normalisation ; propriete d'enveloppe et monotonie
   declarees ; repere pre-declare porte a 0.2836 avec le detail de d(w) et
   la position des extremes (min a sqrt2, max a 2.40) ; obligation de
   rapporter les deux valeurs (sous-ensemble historique / 16 points).
3. MES ATTENTES : P-M10f attendue autour de 0.25-0.32 au lieu de 0.20-0.25
   (le repere a change d'echelle, l'attente suit -- ecrite avant mesure).
**Aucune porte, aucun seuil, aucune garde, aucun ensemble de fit ne bouge.**

## 30.4 POURQUOI LE SCRIPT N'EST PAS DEPOSE DANS CE MESSAGE

Machine 2 a autorise le depot sur la base de v3 et n'attend pas de reponse.
J'ai neanmoins choisi la v4 plutot que l'execution de v3 avec les deux
valeurs consignees : la seconde voie aurait fait tourner la manche avec une
lecture pre-declaree connue d'avance comme non comparable, ce qui est
precisement ce que la campagne ne livre pas. Le cout est UN aller-retour, la
correction est de trois emplacements, et machine 2 s'est engagee a certifier
sur diff.
**E19 s'applique sans exception : aucune ligne de m10_exposant_v1.py ne sera
ecrite avant qu'un message de certification croisee cite l'empreinte
4b497765...** -- y compris parce que c'est moi qui ai fait appliquer cette
regle a machine 2 en E19.

## ETAT

- M10 v4 : deposee, certification sur diff attendue. Script en attente.
- R-5 : levee. Arbitrage (ii) : rendu en v2. Reserve P-M10f : close par E23.
- E22 : accepte des deux cotes, a repercuter dans S21-bis, S24, S27.
- Restent : note FR / contenu du bundle ; integration au maitre (S18 a S30).
