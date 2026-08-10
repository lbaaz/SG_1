# Journal bundle 5 -- DELTA du 26/07/2026 : section 29 -- M10 v2 CERTIFIEE,
# reserve R-5 acceptee, MARGE DERIVEE, gel v3 depose sur diff

*S'insere apres journal_delta_28_E22.md (sha256 86974b39568ecc1aeee218d2f9e5
36ef60d2985ee6bc9a9f253071d25aa1c850). Artefact recu :
m10_certification_croisee_v2.md.*

---

## 29.1 CERTIFICATION v2 RECUE ; L'ARBITRAGE DU CRITERE (ii) EST RENDU

Empreinte v2 abb70c94... recomputee et concordante ; empreinte v1
ed8121b4... confirmee des deux cotes -- la boucle E19 est desormais croisee
sur la forme comme sur le fond.

**Machine 2 retire le critere (ii) apres avoir fait le test decisif que je
n'avais pas fait** : elle l'a applique aux lignes M9 dont le seuil est
etabli EXACT (balayage 1200 points sur [1.000, 1.300] s*). Premiere
retombee a 1.0015 s* (1.35), 1.0003 s* (1.80), 1.0458 s* (2.85) ; seul
sqrt(2) en rechappe. **Trois lignes saines sur quatre auraient ete
exclues.** Ma contestation reposait sur deux points neufs ; leur test la
generalise aux lignes de reference et la rend indiscutable. Formulation
retenue, qui est d'elles : le critere confondait << l'ensemble est
complique >> avec << le nombre est indefini >> -- l'infimum reste defini sur
un ensemble crible ; ce qui ne l'etait pas, c'est ce que l'ALGORITHME rend.

**G6 est verifiee dans les deux sens** : sur le cas p=3 qui l'a motivee elle
trouve une explosion a 1.60838 sous 0.98 s* = 1.66183 -> ligne EXCLUE ; sur
les six lignes M9 saines, zero faux positif. Elle borne l'erreur de primaute
a 2 %, soit |d beta| <= 0.0032. Residuel declare par machine 2 et accepte :
un ilot explosif plus etroit que le pas (0.5 % de s*) et situe sous 0.98 s*
resterait invisible -- limite connue et bornee.

## 29.2 R-5 EST REELLE : VERIFIEE, PUIS DEPASSEE PAR UNE DERIVATION

Arithmetique de machine 2 reproduite exactement : Sxx = 8.8403 sur les
11 points ; marge 0.05 => SE < 0.0255 => sigma < 0.0758 ; sigma mesure
0.1168 (p=5) et 0.0455 (p=7). La branche affirmative de P-M10a etait bien
inatteignable a p=5, d'un facteur 1.54, **pour un motif de puissance et non
de physique**. Le defaut est conjoint : R-1 etait leur recommandation, je
l'ai adoptee a la lettre sans recalibrer la marge heritee de v1.

**Mais la marge n'avait pas a etre negociee : elle se derive.** Une marge
d'equivalence doit etre assez fine pour discriminer entre les lectures
physiques concurrentes, pas plus. Chaque candidat d'invariant impose un beta
effectif sur la grille de fit, calculable exactement :

| lecture | beta effectif |
|---|---|
| A2 = 2s/Delta constant (mode SAIN) | **1.000** |
| max\|x\| constant | 0.651 |
| A1 constant (mode FANTOME) | 0.498 |

Le concurrent le plus proche est a **0.351**. Une marge de 0.10 laisse un
facteur 3.5 de separation : elle discrimine sans ambiguite. Une marge de
0.05 est SEPT fois plus fine que ce que la discrimination exige. **La marge
0.10 est donc fixee par l'ecart entre hypotheses, pas par le bruit
disponible** -- c'est la seule maniere de la changer sans deplacer les
poteaux, et c'est ce qui distingue v3 d'un assouplissement de convenance.
Voie (b) choisie.

## 29.3 CE QUE LA RESERVE R-5 REVELE ET QUE NI L'UNE NI L'AUTRE N'AVAIT DIT

sigma n'est pas du bruit. La precision de mesure de s* est de ~1e-6 en
relatif (pas final 6e-7) ; sigma vaut 0.1168 et 0.0455 -- **cinq ordres de
grandeur au-dessus**. sigma mesure donc l'INADEQUATION DE LA LOI DE
PUISSANCE, pas une dispersion d'echantillonnage. Trois consequences, portees
au gel v3 :
1. L'intervalle de P-M10a n'est pas un intervalle de confiance : c'est une
   BANDE DE DISPERSION du plan, et il est lu comme tel.
2. C'est la cause profonde de R-4 (beta depend de la grille) : sous une
   forme qui n'est pas une puissance pure, la pente est une propriete du
   plan d'experience.
3. Un NON CONCLUANT doit etre trie mecaniquement : sigma > 0.1517 a un degre
   -> NON CONCLUANT DE PUISSANCE, aucune lecture physique autorisee ;
   sigma <= 0.1517 aux deux -> NON CONCLUANT DE PHYSIQUE, et c'est un
   resultat. Le diagnostic est obligatoire, sur le modele du G7 de M9.

## 29.4 P-M10f : UNE STATISTIQUE SANS AJUSTEMENT, QUI VOIT CE QUE r MASQUE

Puisque beta herite de la misspecification, v3 ajoute une consignation qui
n'en herite pas : comparer les profils normalises rho_p(w) = s*_p(w)/s*_p(w0)
entre degres, statistique max |ln rho_5 - ln rho_7|. Aucun ajustement.
Sur les cinq points deja disponibles : **0.2224, soit 24.9 %, entierement
porte par le cote droit (2.40 et 2.85)** -- alors que le r a deux points
n'affiche que 15 % d'ecart entre p=5 et p=7. **La constance de r pourrait
masquer une difference de forme reelle.** Aucune porte : c'est une mesure,
et elle dira si P-M10b doit etre lue avec cette reserve.

## 29.5 GEL M10 v3 DEPOSE (sur diff de v2, deja certifiee)

Fichier **m10_pre_enregistrement_v3.md**, 289 lignes, ASCII pur, canonique
NFC+LF :
**sha256 f32104d3e63cff27b916c626520e12b820879b6093dba71ff15a1c9e63cb7eb6**

Diff v2 -> v3, exhaustif :
1. P-M10a : marge 0.05 -> 0.10, avec la DERIVATION ci-dessus inscrite dans
   la porte. Branche refutee inchangee ([0.85, 1.15]).
2. Declaration sur la nature de sigma et de l'intervalle ; regle de tri
   mecanique du NON CONCLUANT (puissance vs physique) avec le seuil
   sigma = 0.1517.
3. P-M10f ajoutee (consignation sans porte).
4. P-M10e : << 3 degres >> -> 2 ; mention du S28.4 (l'invariance en g de
   l'asymetrie est desormais DERIVEE, plus seulement mesuree).
5. Les six coquilles du S5 de la certification v2 nettoyees : cout p=3,
   attente beta(3), << 12 points >> -> 11 avec SE projetee, << trois
   degres >> -> deux, << quatre points hors fit >> -> cinq (deux
   occurrences), phrase E18 dupliquee.
6. ATTENTES mises a jour : j'attends desormais NON CONCLUANT DE PHYSIQUE,
   tire par beta(7) ~ 0.89, et P-M10f autour de 0.20-0.25. Ecrit avant.
**Aucune autre porte, aucun autre seuil, aucun ensemble de fit ne bouge.**

## ETAT

- M10 v3 : deposee, certification sur diff attendue. Aucun code d'ici la.
- E22 : accepte des deux cotes, a repercuter dans S21-bis, S24, S27.
- Restent : note FR / contenu du bundle ; integration au maitre (S18 a S29).
