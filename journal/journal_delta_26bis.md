# Journal bundle 5 -- DELTA du 26/07/2026 : section 26-bis -- reconciliation
# JSON-niveau de M9 CLOSE, deux consignations nouvelles

*S'insere apres journal_delta_26_E21.md (sha256 afda425bf0fcdaff267024d0875
3929a2f7d54b2a57e3b49b98489f52a24f5ef). Trace executable : audit_m9_json.py.*

---

## 26-bis. RECONCILIATION JSON-NIVEAU : ZERO ECART, ET LE BRUT PAIE ENCORE

**Custody close.** sha256 du fichier recu = 41595413f676df396994da1b7ca6c4ab
c59199b8ca2f93f00e2643c151653210, identique a l'annonce -- aucun ecart de
canal. Gel et script conformes en meta. Toutes les identites internes
(sF = min, asym, K5 = 0.05 sF^3, s_cible forme fermee, g_cal, equiv_M3,
s0 = frag x 0.7 x s_cible, ecart_G5) verifiees a 0.0 ; les huit rho, les
p exacts re-enumeres, les six Q et les quatre ratios P-M9c : conformes.
Regle G5 respectee a la lettre : s_autre = null a 2.00 seulement (asym
0.19 % < 2 %). La boucle machine 2 -> machine 1 est fermee sur du brut,
comme le veut la campagne.

### Consignation A -- L'ASYMETRIE DE SIGNE EST INVARIANTE EN g
### (les s_autre de G5, une donnee que personne n'avait demandee)

| w2 | asym(g = 0.05) | asym(g_cal) | ecart | rescaling de g |
|---|---|---|---|---|
| 1.35 | 1.11860 | 1.11887 | 0.023 % | x0.017 |
| sqrt2 | 1.17785 | 1.18076 | 0.247 % | x0.018 |
| 1.80 | 1.35145 | 1.35346 | 0.149 % | x0.13 |
| 2.00 | 1.00193 | (exempt, regle G5) | -- | x0.024 |
| 2.40 | 1.65162 | 1.65380 | 0.132 % | x3.3 |
| 2.85 | 1.23566 | 1.23565 | 0.001 % | x13.2 |

L'asymetrie survit a des rescalings de g couvrant pres de TROIS DECADES a
<= 0.25 %. Derivation en une ligne (post-hoc, etiquetee) : si K est
invariant PAR COTE (K_side = g s_side^3), alors s_side ~ (K_side/g)^(1/3)
et s+/s- = (K+/K-)^(1/3), independant de g. **Le brut etablit donc
l'invariance de K sur les DEUX cotes du seuil, sur ~3 decades -- tres
au-dela du x2 teste par G2**, et il etablit du meme coup que le cote
fragile est stable en g (frag_cal = frag partout ou mesure). L'asymetrie
r_s devient une quantite STRUCTURELLE de chaque point (le rapport des
deux invariants K), pas un artefact d'amplitude -- a verser au dossier de
la derivation de r et de la loi C.

### Consignation B -- REGRESSION BIT-A-BIT INCIDENTE AU POINT 1.80

1.80 est le seul point frag = +1 : le systeme M9 y coincide PAR
CONSTRUCTION avec celui de M8 (meme g_cal, meme s0 non signe). Le
pipeline le reproduit AU BIT : g_cal, s0, T_ghost aux deux troncatures et
T_retourne strictement identiques (12 chiffres). Regression complete de
la chaine classique + calibration + quantique, obtenue gratuitement --
et qui borne par l'exemple ce que G1b certifiait (stabilite
deterministe d'environnement).

## ETAT (inchange sur le fond)

Verdicts M9 et regime post-C2 : voir §26. Boucles restantes : test croise
symetrique (optionnel, machine 2) ; note FR / contenu du bundle ;
integration au maitre (§18 a §26-bis, E16-E21, D1-D3) ; choix du prochain
chantier -- derivation de r (papier, desormais nourrie par la
consignation A), bord droit (3,1), ou cahier des charges de l'estimateur
(C2).
