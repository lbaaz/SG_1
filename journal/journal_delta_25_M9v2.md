# Journal bundle 5 -- DELTA du 26/07/2026 : section 25 -- certification M9 v1
# REFUSEE (D-M9-1), decouverte de l'ecart (h), depot du gel v2

*S'insere apres journal_delta_24_D3.md (sha256 c6395480d7f8adb39a2b74aa1b6f
11dcfdf68b535d758a04633b96266001c3ce). Artefact recu :
audit_m9_prefeu_machine2.log (+ .py, + m9_reponse_certification_machine2_v1.md
cote BOCAL4).*

---

## 25. LE CIRCUIT E19 A FONCTIONNE : v1 authentique, v1 refusee, defaut mort
## avant la premiere ligne de code

**Verdict machine 2 accepte apres verification machine 1.** L'audit pre-feu
a recompute l'empreinte v1 (4e80db1b..., concordante), re-enumere les
nulles, relu les ancres (<= 0.001 %), reconte la coquille (891), et refuse
la certification pour UN defaut bloquant :

**D-M9-1 -- le signe de l'etat initial n'etait pas declare.** Les quatre T
de reference de M3 sont tous mesures cote fragile (sgn = frag = -1,
m3_parite_2 : island_state(sgn*0.7*st)) ; la lignee m7/m8 implemente s0
positif sans signe -- verifie dans MA lignee, lignes a l'appui (corps_m7 :
355/371 's0 = RHO_AMP * cal[s_cible]', 199 'A1 = s(1+w2^2)/Delta').
Materiel, pas cosmetique : T(+1)/T(-1) = 0.406 a 2.85 (verifie : 0.4058) --
un M9 en +1 aurait garanti une fausse alerte P-M9c (ratio ~0.41 hors
[0.80, 1.25]) et rendu fausse la clause (e). C'est exactement la classe de
defaut (convention retiree/non declaree) qui a casse M8 -- cette fois
attrapee AVANT le code, par le circuit installe pour ca. La regle E19 a
paye a sa premiere application.

**Verification machine 1 de l'audit : tout concorde** (asym sqrt2 18.18 % ;
r(3)_min = 17.477, variante +1 = 21.542 ; T-ratio 0.406 ; frag p=3 a 1.35 =
+1, asym -37.4 %).

**Decouverte au passage -- l'ecart (h), qu'aucune des deux machines n'avait
vu.** L'audit verifiait la coherence INTERNE du json M3 (g = K/s_cible^3
avec le s_cible du json) ; en confrontant la FORME FERMEE (f) du gel au
json, machine 1 trouve : les s_cible stockes par M3 excedent la formule
d'un facteur UNIFORME x1.00285 aux trois points ancres (dispersion
1.00284-1.00285 ; -0.85 % sur g ; equivalent nbar = 7.04). Cause non
identifiee -- a lire dans le code de calibration M3 (machine 2). Propagation
pire cas sur T ~3.4 % (dlnT/dlng ~ 4 mesure sur M8/M3) : SOUS toutes les
tolerances (G5 +-5 %, fenetre P-M9c), mais desormais DECLARE dans le gel
v2, item (h) : M9 utilise la forme fermee partout, l'ecart aux canoniques
est consigne par point.

**Fermetures annexes de l'audit :**
- **r(3) : CLOS.** Lecture m1_calib : r(3)_min = 17.477 -- le 17.48 de la
  table EST min-convention. Variante +1 = 21.54, etiquetee si jamais citee.
  La table r est desormais integralement etiquetee et fermee :
  min-convention p >= 4 : 7.44 / 8.338 / 6.65 / 7.100 (bande 6.65-8.34),
  p=3 = 17.48 hors norme.
- **Cote fragile non uniforme a p=3 aussi** (frag = +1 sauf 2.85) : la
  non-uniformite est generique, troisieme degre ou elle est observee --
  elle justifie la forme 'sgn_F par point' de la correction D-M9-1.
- **sqrt2 transmise** (sP = 0.38604, sM = 0.32665) et promue quatrieme
  ancre bloquante de G1a en v2, recommandation machine 2 acceptee.
- Paires nom <-> sha256 recues et archivees (regle E19-3, appliquee dans
  les deux sens pour la premiere fois) ; notamment
  m8_pre_enregistrement2.md = faba24ad... (texte du bloc cdd : la derniere
  demande d'artefact d'E19 est SATISFAITE, dossier E19 complet).

---

## MANCHE M9 -- GEL v2 DEPOSE, EN ATTENTE DE CERTIFICATION CROISEE

Fichier **m9_pre_enregistrement_v2.md** (nom versionne), 230 lignes, ASCII
pur, canonique NFC+LF :
**sha256 90019ebabde24e912ed0415da0e2068d9a27d8404a4aaa6e944fc2463e0f4c70**

Changements v1 -> v2, tous listes dans l'HISTORIQUE du bloc :
1. **D-M9-1 corrige** : s0 = sgn_F x 0.7 x s_cible, sgn_F = signe du
   minimum de la carte sF au point, fige a g = 0.05, consigne par point ;
   meme s0 pour GHOST, RETOURNE et FREE ; ecart eventuel du cote fragile a
   g_cal consigne sans porte ; programme G5 exprime en sgn_F.
2. sqrt2 = quatrieme ancre bloquante de G1a ; G1c supprimee (absorbee).
3. Ecart (h) declare (s_cible json x1.00285, cause a identifier).
4. Attente retourne(2.00) declassee en ordre de grandeur (sensibilite au
   cote du deplacement inconnue).
**Aucune porte ni aucun seuil modifies** ; P-M9a/pre/null, l'echelle
adaptative, C1/C2 (D3) et l'anti-arret-optionnel sont inchanges au
caractere pres.

Demande a machine 2 avec la certification v2 : la CAUSE de l'ecart (h)
(lecture du code de calibration M3) -- non bloquante pour la certification,
bloquante pour l'interpretation fine de P-M9c si le ratio sortait pres des
bords de la fenetre.

## ETAT DES BOUCLES

- E19 : dossier COMPLET (texte cdd recu). E20 : clos. r(3) : clos.
- Restent : cause de l'ecart (h) ; note FR / contenu du bundle ;
  integration des deltas au maitre (S18 a S25).
- M9 : v2 deposee, certification attendue ; AUCUN code d'ici la.
