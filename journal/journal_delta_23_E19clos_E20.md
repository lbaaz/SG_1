# Journal bundle 5 -- DELTA du 26/07/2026 (matin) : section 23 (cloture de
# l'episode M8), E19 CLOS, ERRATUM E20, espace M9

*S'insere apres journal_delta_22_E19.md (sha256 f0d9896a9c2c74ddcd24534061fa
6868a0ea6ca7f24fa01b18d644c7c173a891). Traces executables :
audit_m8_resolution.py (present delta) ; m8_reponse_custody_machine2.md
(artefact machine 2, verifie ici).*

---

## 23. CLOTURE DE L'EPISODE M8 -- custody resolue, ancres resolues, et le
## +1.00 de M3 ni replique ni refute

### E19 : CLOS (chronologie etablie, falsification EXCLUE)

Machine 2 a produit les trois artefacts demandes. Horodatages (mtimes +
transcription, attestation machine 2) : gel cdd fige 00:35:34, hash 00:35:49,
premiere ligne de code 00:38:04, run acheve 00:44:46. **Le bloc a ete gele
~2 min 30 avant tout code : fork v2 localement legitime, NON certifie --
rupture de circuit, pas falsification.** La mention « copie machine 1
verifiee octet-identique » etait une erreur d'ATTRIBUTION (aller-retour du
gel machine 2, byte-identique a lui-meme), rendue possible par une collision
de noms : le gel v1 machine 1 attendait dans Downloads sous le MEME nom non
versionne que celui cree en BOCAL4.

**Part de machine 1, consignee ici** : les gels ont ete livres sous noms NON
versionnes depuis M6 (m6/m7/m8_pre_enregistrement.md) -- la lecon E13
(noms versionnes) avait ete appliquee aux scripts, pas aux blocs de gel. Le
piege de collision etait co-construit. **Regles gelees en sortie d'E19** :
(1) un run n'est opposable a la campagne que si l'empreinte de son gel
figure dans un message de certification CROISEE anterieur au depot du
script ; (2) noms de fichiers versionnes pour TOUT artefact de gel
(m9_pre_enregistrement_v1.md, ...) ; (3) tout echange d'artefacts liste les
paires nom <-> sha256. Nota : c'est le hachage de CONTENU qui a detecte
l'incident -- les regles 2-3 sont de la defense en profondeur, pas le
detecteur.

### L'enquete d'ancres : RESOLUE -- convention, pas physique

Moteur M3 = bundle5.sstar (jet), DEUX signes, sF = min. Les ancres v1
0.310 / 2.586 etaient les **sM** (cote fragile). M8 a mesure **sgn = +1
seulement** (protocole herite de M7 ; la definition (f) de v1 -- min des
deux signes -- avait ete retiree du gel execute, et c'est LE defaut de
fond). Verification d'ici : M8(+1) reproduit les sP de M3 a -0.78 / -0.07 /
-0.02 % ; asymetries sP/sM = +12.6 % (1.35), +0.2 % (2.00), +23.6 % (2.85),
+18 % (sqrt2, frag = -1). Aucun probleme de moteur, de bracket, de langue
instable ou de T. Bonus gratuit : jet (M3) contre modes (M8) concordent a
<= 0.8 % sur trois points neufs -- validation croisee d'integrateurs.
Le puzzle d'arrondi du 25/07 est clos exactement : r_min = 2.58573/0.31011
= 8.3381 (le « 8.338 » etait le chiffre plein ; mon 8.342 venait des valeurs
arrondies).

### Le confond, etendu et ferme

TROIS des quatre points canoniques de M8 ont tourne a un couplage different
de la carte M3 (x1.40 a 1.35, x1.63 a sqrt2, x1.89 a 2.85) ; seul 2.00
(asym 0.2 %) etait apparie. La comparaison M3 <-> M8 etait cassee sur les
DEUX axes : l'axe T (systemes differents) ET l'axe K (le swap de rangs
sqrt2 <-> 2.00 est induit par la convention -- x1.63 sur K5(sqrt2) inverse
la paire). Table T_M8/T_M3 (N=64) : 3.97 / 2.81 / 0.90 / 1.13 -- le seul
point apparie est a 0.90. Consigne dT/dg (post-hoc, etiquete) : la
sensibilite de T au couplage est fortement heterogene (a 2.85, g x1.89 ->
T x1.13 ; a 1.35, g x1.40 -> T x3.97) -- matiere de design M9.

**Verification de coherence interne de M3, faite ici** : depuis sa propre
carte sF, rho(T_M3, K5_M3) = +1.00 se reconstruit exactement -- le +1.00
etait une mesure coherente sur ses propres systemes.
**Regle ANTI-FRANKEN-RHO, gelee** : aucun rho melant la carte d'une manche
et les T d'une autre n'a de statut (demonstration : rho(T_M8, K5_M3) = 0.00,
nombre vide de sens). La comparaison propre exige la manche convention (f)
integrale -- il n'existe AUCUN raccourci de recomputation : les sM de 1.80
et 2.40 n'existent nulle part.

### Verdicts retenus (colonne unique desormais -- gel v1, apres retractation
### machine 2 de la clause +0.50)

P-M8-pre : LIEN CONFIRME. P-M8a : NON CONCLUANT (+0.3714 aux deux
troncatures, p = 0.2486). P-M8b : branche « <= 3 quelque part » DECLENCHEE
-> caveat cause (2). P-M8-null : PASSE. G7 : rho(T56,T64) = +1.00, cause (1)
ecartee a p=5 -- LE gain de la manche. **Le +1.00 de M3 n'est ni replique ni
refute : il attend son premier vrai test.** La jambe quantique de
H-PROFONDEUR reste sans aucun soutien puissante -- enonce robuste, inchange.

---

## E20 -- La table r de S21-bis melait deux conventions sans etiquette

La table « r quasi constant 6.6-8.3 pour p >= 4 » juxtaposait des entrees
min-des-deux-signes (r(4), r(6) [symetriques par parite], r(5) = 8.338
[carte sF de M3]) et UNE entree +1-seulement (r(7) = 7.47 -- la carte M7 n'a
jamais mesure sgn = -1 aux bords ; seule l'asymetrie au CENTRE, 0.11 %, est
connue a p=7). Defaut du meme type qu'E17, generalise : **l'unite ET la
convention (signe, definition du seuil) font partie de la mesure ; toute
table inter-manches porte ses etiquettes.** La meme reserve vaut pour la
famille D et les detunings M5/M6/M7 : GELES en +1, leurs verdicts tiennent
contre leurs portes ; seules les comparaisons inter-manches heritent de
l'etiquette.
Etat corrige : bande min-convention p >= 4 : **6.65-8.34, EN ATTENTE de
r(7)_min** (cout : 2 recherches, sgn = -1, p=7, w2 = 1.35 et 2.85) ;
variantes +1 : r(5) = 9.15-9.22, r(7) = 7.47. r(3) = 17.48 : convention a
confirmer sur m1_calib. L'enonce « quasi constant, p=3 hors norme » SURVIT
dans les deux conventions connues a p=5 (8.34 et 9.2, toutes deux loin de
17.4) ; la fermeture propre attend les deux recherches p=7.

---

## SUSPENSIONS : levees et restantes

- Custody M8 : RESOLUE (E19 clos). Ancres : RESOLUES (convention).
- Requalification du +1.00 de M3 : reste SUSPENDUE -- non par litige, mais
  parce que le test propre n'a pas encore eu lieu.
- r(5) = 9.22 : reclasse « variante +1 » ; canonique min = 8.338.
- M9 : DEBLOQUEE sous conditions ci-dessous. Prochain gel : machine 1,
  certification croisee prealable (accepte par machine 2).

## ESPACE M9 (rien n'est gele ; le gel devra trancher ces points)

1. **Convention (f) integrale** : deux signes partout (12 recherches de
   carte), sF = min, asymetries consignees -- c'est la condition sine qua
   non de toute comparaison a M3, et elle fournit au passage les sM
   manquants de 1.80 et 2.40.
2. **La clause gelee de M8 v1 tient** : « interdit d'empiler une troisieme
   manche quantique sans changer d'estimateur ». Lecture stricte par defaut.
   Candidats d'estimateur, chacun avec son probleme DECLARE :
   (a) T a g FIXE entre points (supprime le confond de couplage ; mais nbar
       varie -> le regime hbar_eff n'est plus apparie -- c'est un autre
       design, pas une variante) ;
   (b) rapport T_ghost/T_retourne (s'etend sur 10 ordres, domine par la
       structure propre du retourne : sauvage comme variable de rang) ;
   (c) difference T_ghost - T_retourne (aucune derivation d'additivite des
       canaux ; change de signe a 2.85).
   Aucun n'est adopte ici ; le gel M9 devra en choisir un AVEC derivation,
   ou argumenter que la correction de convention ne constitue pas un
   « empilement » (lecture alternative, a trancher ensemble, pas par
   machine 1 seule).
3. **Pre-M9 a cout quasi nul, executables sans gel** (mesures de
   regularisation, aucune porte) : r(7)_min (2 recherches) ; confirmation de
   la convention de r(3) (lecture m1_calib) ; asymetries p=7 aux 6 points si
   on veut assainir retroactivement les rangs M7 (6 recherches, ~3 min).

## DEMANDES RESTANTES (non bloquantes)

- m8_pre_enregistrement2.md (bloc cdd) : texte integral pour archivage au
  dossier E19 (l'attestation d'horodatage est acceptee ; l'archive veut le
  texte).
- Lecture m1_calib : convention de r(3).
