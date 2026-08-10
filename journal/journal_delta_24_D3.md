# Journal bundle 5 -- DELTA du 26/07/2026 : section 24 -- decision D3,
# regularisation p=7 (E20 CLOS), depot du gel M9 v1

*S'insere apres journal_delta_23_E19clos_E20.md (sha256 f323dcfb3b5b49483b49
dabd97b82fec38182a98d4cfebf18d8338a751f87dce).*

---

## D3 -- ARBITRAGE DE LA CLAUSE ANTI-EMPILEMENT (consigne AVANT redaction du
## gel M9 ; l'accord humain est dans la transcription, anterieur a tout)

Question posee : la clause gelee de M8 v1 (« interdit d'empiler une
troisieme manche quantique sans changer d'estimateur ») s'applique-t-elle a
une manche qui CORRIGE la convention plutot qu'elle ne repete le test ?
Lecture A (lettre) : oui -- mais les trois candidats d'estimateur sont
casses, chacun pour une raison declaree (g fixe = autre design ; rapport
ghost/retourne = 10 ordres, domine par le temoin ; difference = additivite
non derivee), et P-M5c interdit un critere sans derivation.
Lecture B (esprit) : la derivation de la clause visait la repetition du meme
test ; il est etabli (S23) que M8 n'a pas execute les systemes de M3 (3/4
points a couplage different) ; M9 en convention (f) est le PREMIER test.
**DECISION (humain, 26/07) : lecture B, avec deux compensations gelees dans
le bloc M9 : (C1) observable differentielle consignee aux six points ;
(C2) si M9 sort NON CONCLUANT, la clause se rearme a pleine force -- pas de
lecture B deux fois.** Motif de la procedure : la clause est de machine 1 ;
l'assouplir ne pouvait pas etre une decision de machine 1 seule.

---

## 24. REGULARISATION p=7 EXECUTEE (machine 1, hors gel, aucune porte) --
## E20 : CLOS

Six recherches sgn = -1, protocole M7 inchange, 134 s. Cross-check
machine 2 : sM(2.00) = 0.39184, ecart 0.000 % avec le volet E de M6.

| w2 | 1.35 | sqrt2 | 1.80 | 2.00 | 2.40 | 2.85 |
|---|---|---|---|---|---|---|
| sP (M7) | 0.26000 | 0.29756 | 0.52141 | 0.39227 | 1.46418 | 1.94232 |
| sM (ici) | 0.22875 | 0.25627 | 0.64259 | 0.39184 | 1.06065 | 1.62409 |
| asym | +13.7 % | +16.1 % | **-18.9 %** | +0.1 % | **+38.1 %** | +19.6 % |

- **r(7)_min = 7.100 -> DANS la bande. E20 est clos** : la table r sous
  convention UNIQUE (min) donne r(4) = 7.44, r(5) = 8.338, r(6) = 6.65,
  r(7) = 7.100 -- bande 6.65-8.34, quatre entrees dedans, p=3 = 17.4 hors
  norme. L'enonce « quasi constant p >= 4, p=3 exceptionnel » tient
  desormais sans melange d'etiquettes. (r(3) : confirmation de convention
  sur m1_calib toujours attendue de machine 2, non bloquante.)
- **Rangs K7 identiques entre conventions** : les consignations de rangs de
  M7 (P-M7a, axe K du rho) sont convention-robustes. Aucun rho
  min-convention n'est recalculable (anti-Franken-rho : les T de M7 vivent
  sur la carte +1) -- et aucun n'est necessaire.
- **Deux data neuves, consignees** : (i) l'asymetrie de signe atteint 38 %
  au point de la vallee (2.40) ; (ii) **le cote fragile S'INVERSE a 1.80**
  (sP < sM) -- le signe fragile n'est pas uniforme en w2. Consequence
  operationnelle deja integree au gel M9 : les deux signes sont
  indispensables aussi aux points neufs.

---

## MANCHE M9 -- GEL v1 DEPOSE, EN ATTENTE DE CERTIFICATION CROISEE

Fichier **m9_pre_enregistrement_v1.md** (nom versionne, regle E19),
194 lignes, ASCII pur, canonique NFC+LF :
**sha256 4e80db1b3e7eb48735c305ab350d350809661d64cf4db2aac2245011918de05c**

Contenu : D3 et ses compensations GELES dans le bloc ; convention (f)
integrale (deux signes partout, sF = min, asymetries consignees) ; porte
principale P-M9a a echelle adaptative (0.80 a n=6, 0.90 a n=5, echec de
design a n <= 4) avec C2 dans la branche NON CONCLUANT ; P-M9b = C1
(retourne aux six points, fourche point-par-point heritee de M8 v1, profil
complet consigne pour le chantier estimateur) ; P-M9c = la replication
directe T_M9/T_M3 aux canoniques (legitime cette fois : memes systemes par
construction), lecture pre-declaree [0.80, 1.25] uniforme ; gardes G1a
(ancres sP ET sM aux trois points M3, +-2 % par signe), G1b (regression M8
+1 aux six points), G2 invariance a 2g sur les deux signes, G4 sur l'echelle
de force, G5 double-signe aux points d'asym > 2 %. Attentes chiffrees sans
issue favorite. **Aucun code avant qu'un message de machine 2 cite
l'empreinte ci-dessus** -- premiere application de la regle E19.

## ETAT DES BOUCLES

- E20 : CLOS (r(7)_min mesure ; table etiquetee, bande 6.65-8.34).
- Restent : texte du bloc cdd pour l'archive E19 ; convention r(3)
  (m1_calib) ; note FR / contenu du bundle ; integration des deltas au
  maitre (S18 a S24).
- M9 : gel depose, certification attendue.
