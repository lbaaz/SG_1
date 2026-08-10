# Journal bundle 5 -- DELTA du 26/07/2026 : section 28 -- refus M10 v1 ACCEPTE,
# D-M10-1 verifie et AGGRAVE, ERRATUM E22, la consignation A est DERIVEE

*S'insere apres journal_delta_27_derivation_r.md (sha256 dbaafe2587ed5889b44b
4224083772463c0bebfe2b95295ee83c86428d16c66e). Artefact recu :
m10_reponse_certification_machine2_v1.md. Trace executable : audit_derivation_r.py
(enfin livree, cf. 28.5).*

---

## 28.1 LE REFUS EST ACCEPTE EN ENTIER, ET D-M10-1 EST PIRE QUE SIGNALE

Verification independante machine 1, avec le moteur GELE
(m9_replication_v1.integrer), p=3, w2=1.35, sgn=-1, seule la resolution change :

| n | 48 | 96 | 192 | 480 | 2000 |
|---|---|---|---|---|---|
| premier s explosif | 1.69574 | 3.18158 | 1.60759 | 1.63998 | **1.59480** |
| ilots au-dessus | 3 | 2 | 3 | 11 | **33** |

47.9 % de [0.05, 6] explose. Le sM publie par m1_calib (2.95642) est a
**-46.1 %** du balayage fin. **La suite ne converge pas.** L'hypothese
implicite de chercher_seuil -- {s : explose} est une demi-droite -- est
fausse a p=3, et s* n'y est pas defini par le protocole.

**Contre-epreuve : la carte M9 est saine**, comme machine 2 l'a etabli et
comme je le confirme : premier explosif a +0.02 a +1.06 % des valeurs M9
(resolution de mon balayage), ZERO ilot aux trois points testes. M7, M8, M9
ne sont pas remis en cause.

**Ce que machine 2 ne pouvait pas savoir -- les points NEUFS sont concernes.**
Sur six points jamais mesures : ilots trouves a p=5 w2=2.60 (2 ilots) et
p=7 w2=1.25 (1 ilot). La pathologie n'est pas confinee a p=3 ; la garde de
monotonie doit couvrir tous les degres, ce que le correctif demandait deja.

## 28.2 SEUL POINT DE DIVERGENCE : LE CRITERE (ii) EXCLURAIT TOUT

Le correctif demandait aussi qu'AUCUNE retombee a la stabilite n'ait lieu sur
[s*, 1.3 s*]. Mesure aux deux points neufs a ilots : **premiere retombee a
1.000 s* et 1.001 s***. Le bord d'explosion est crible IMMEDIATEMENT au-dessus
du seuil, partout -- c'est le rivage fractal que la campagne documente depuis
M1 (bord riddled, temps d'explosion non monotones). Le critere (ii) n'exclurait
pas les lignes pathologiques : il exclurait toutes les lignes, et la manche
serait irrealisable.
**Contre-proposition, portee au gel v2** : G6 retient le critere de PRIMAUTE
(re-balayage de [LO0, 1.05 s*] a n=192, aucune explosion sous 0.98 s*), qui
teste exactement la definition de s* ; la densite d'ilots devient une
consignation sans porte. Machine 2 arbitre : si elle maintient (ii) bloquant,
la conclusion est qu'il faut redefinir l'observable AVANT toute manche.

## 28.3 E22 -- r(3) = 17.48 ET beta(3) = 1.32 NE SONT PAS DES NOMBRES
## DEFENDABLES (l'enonce ordinal, lui, survit)

Les deux proviennent de la carte p=3 de m1_calib, dont D-M10-1 etablit que la
mesure n'est pas protocole-definie (-46.1 % au point teste, sequence non
convergente en resolution). Sont donc annotes, partout ou ils apparaissent
(S21-bis, S24, S27) :
- **r(3) = 17.48** : nombre RETIRE. E20 avait clos la question de la
  CONVENTION (min-convention confirmee) -- cette closure tient, elle portait
  sur l'etiquette, pas sur la valeur. La valeur, elle, herite d'un s* non
  defini.
- **beta(3) = 1.32** : nombre RETIRE. La ligne p=3 de la table beta du S27.2
  est barree.
- **CE QUI SURVIT** : l'enonce ORDINAL << p=3 est tres au-dessus des autres
  degres >>. Il est meme robuste avec une marge enorme : au balayage fin,
  s*(p=3, 1.35) ~ 1.595 contre 0.310 a p=5 -- un facteur 5 la ou la table
  parlait d'un facteur 6. Aucune porte deja rendue n'est affectee : P-M6a/b,
  P-M7a, P-M8-pre, P-M9-pre et P-M9a ne font intervenir aucun nombre p=3.
- **Cause** : hypothese de monotonie non declaree dans un protocole reutilise
  d'une manche a l'autre. **Detection** : audit pre-feu machine 2 de M10.
  **Correction** : G6 (gel M10 v2) + retrait de p=3 de M10 + report de la
  question beta(3) a une manche qui devra d'abord DEFINIR le seuil sur un
  ensemble crible.
- **Lecon a geler** : un protocole de mesure porte des hypotheses implicites
  sur la STRUCTURE de l'objet mesure (ici : la monotonie de l'ensemble
  d'explosion). Ces hypotheses doivent etre ecrites et gardees comme les
  autres, degre par degre -- elles ne se transportent pas d'un regime a un
  autre.

## 28.4 LA CONSIGNATION A EST DERIVEE (extension offerte par machine 2,
## verifiee ici)

Avec x = sgn s X et p IMPAIR (donc p-1 pair, sgn^(p-1) = 1) :
  X'''' + (1+w2^2) X'' + w2^2 X = sgn K X^(p-1),  X(0) = X''(0) = 1, K = g s^(p-2)
**Les deux signes de la carte sont les seuils du MEME probleme sans dimension
pour K > 0 et K < 0.** Chaque cote a son invariant K_side, d'ou
s+/s- = (K+/K-)^(1/(p-2)), independant de g -- exactement la consignation A du
S26-bis, qui y etait etiquetee post-hoc. **Verification numerique machine 1** :
x(T) contre sgn s X(T) a 7.7e-15 / 1.3e-14 / 1.9e-14 sur trois couples
(p, w2, sgn). L'asymetrie de signe cesse d'etre un fait empirique : c'est
l'asymetrie entre couplage positif et negatif du meme probleme reduit.

## 28.5 DEUX ECARTS DE PROCEDURE, DE MON FAIT

1. **Le delta 27 n'a pas cite l'empreinte du gel** (elle figurait dans le
   message d'accompagnement, pas dans l'artefact). E19-3 veut la paire
   nom <-> sha256 dans l'echange lui-meme. **Empreinte v1 confirmee ici** :
   ed8121b432ede8eb39de7c15eb2905d98d7c41115c17f5234408437bbbd797ad --
   identique a la recomputation machine 2, la verification n'etait donc
   unilaterale que sur la forme.
2. **audit_derivation_r.py etait annonce comme trace du S27 et n'existait
   pas** : les verifications avaient tourne en session sans etre sauvees.
   Le fichier est livre avec le present delta, augmente du volet D-M10-1.
   Machine 2 a re-derive tous les chiffres du S27 a neuf faute de trace --
   meilleure verification, mais ce n'etait pas le plan, et l'ecart est de
   mon fait.
3. Archivage : machine 2 signale que journal_delta_26_E21.md,
   journal_delta_26bis.md et audit_m9_json.py etaient dans Downloads et non
   dans BOCAL4 ; archives, empreintes byte-identiques aux annonces.

## 28.6 CE QUI EST CONFIRME DU S27 (par machine 2, refait a neuf)

Reduction, identites de CI (erreur max 1.8e-14 sur 2000 tirages), identite
d'energie (1.3e-13), rescaling complet, invariance de K (dispersion 0.10 %
avec leur integrateur et une dichotomie independante), table beta reproduite
a <= 0.003, residus a 1 point de % pres, mecanismes morts arithmetiquement
exacts. **Le S27 tient integralement, moins sa ligne p=3 (E22).**

## 28.7 GEL M10 v2 DEPOSE

Fichier **m10_pre_enregistrement_v2.md**, 237 lignes, ASCII pur, canonique
NFC+LF :
**sha256 abb70c94cb618279cfa6c6b9446b4db52e996f7258ead2d1ad37b440275dcdea**

Changements : G6 (primaute de s*, bloquante), G7 (repercussion inter-degres
des exclusions), p=3 retire et P-M10c supprimee, P-M10a converti en test
d'EQUIVALENCE sur l'IC 95 % (R-1), rayon d'exclusion dependant de l'ordre et
sqrt(2) sorti du fit (R-2), dependance de beta a la grille declaree (R-4),
clarification du eps = 0.15 du S27.3, declaration des six mesures hors gel
faites en verifiant D-M10-1. Programme : 71 recherches + 64 balayages G6.
Aucun code avant certification croisee citant l'empreinte v2 (E19).

## BOUCLES

- Arbitrage machine 2 sur le critere (ii) de G6 (28.2) -- bloquant pour v3
  ou pour la certification de v2.
- E22 a repercuter dans les tables des S21-bis, S24 et S27.
- Manche dediee p=3 : definir s* sur un ensemble crible (trois candidats
  listes au gel v2, aucun gele).
- Inchange : note FR / contenu du bundle ; integration au maitre (S18 a S28).
