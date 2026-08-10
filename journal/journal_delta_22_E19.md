# Journal bundle 5 -- DELTA du 25/07/2026 (nuit, fin) : section 22 (M8),
# ERRATUM E19, investigation d'ancres OUVERTE

*S'insere apres journal_delta_21bis.md (sha256 b867820e67527fb2462ec26434c56
a0b27ccf67ae2156712ec56f4ebd99fd84b). Trace executable : audit_m8_custody.py.*

---

## 22. MANCHE M8 EXECUTEE (machine 2) -- CONTRE UN GEL NON CERTIFIE MACHINE 1.
## Verdicts rendus EN DEUX COLONNES jusqu'a resolution.

**Custody.** JSON recu : 46d433e90291e8905efa4d8ec3953e330cd5e74f96530856044
422705b730e4d (prefixe conforme a l'annonce BOCAL4). Gel execute :
cdd378775c... **Gel v1 depose et hashe par machine 1 : 6284f2478697...**
Les deux blocs different. Aucun script M8 n'a ete depose par machine 1 (le
circuit s'arretait a « tu certifies, script sur ton go ») ; le script execute
(49d6dccf...) est inconnu de machine 1. **La mention « copie machine 1
verifiee octet-identique » du rapport est inexacte pour le gel v1 de
machine 1 : machine 1 n'a jamais produit un bloc cdd37877.**

**Divergences v1 -> gel execute, constatables depuis les seuls resultats**
(la liste peut etre revisee quand le bloc cdd sera produit -- precedent
E12 -> E13 : un premier diagnostic peut se corriger) :
1. Renommage des portes (P-M8-pre -> "P-M8a", P-M8a -> "P-M8b", contenu de
   P-M8b -> "P_M8d").
2. **Clause nouvelle « replication echouee si rho < +0.50 »**, absente de
   v1 -- et c'est elle qui porte le verdict-titre du rapport.
3. **Lecture de P-M8b changee** : v1 gelait une fourche POINT PAR POINT
   (>= 10 partout / <= 3 quelque part / entre : consigne sans lecture) ;
   l'execute applique une MEDIANE (« 6.36 -> zone non tranchee »). Sous la
   fourche v1, la branche « <= 3 quelque part » SE DECLENCHE (2.17 a 1.35,
   2.46 a 2.40, 0.647 a 2.85) : le verdict principal porte le caveat
   cause (2). La mediane a supprime un caveat que v1 attachait.
4. **G1 reduite de trois ancres a une** (2.00 seule, et contre 0.37401 au
   lieu du 0.3749 gele). Les deux ancres supprimees ECHOUENT contre les
   mesures : s*(1.35) = 0.34648 vs 0.310 (+11.8 %), s*(2.85) = 3.19469 vs
   2.586 (+23.5 %).
5. **Le volet deux-signes de v1 (definition (f), s* = min des deux signes,
   asymetries consignees partout) est absent du JSON** : aucune donnee de
   signe. Le routage v1 de l'echec G1 (asymetrie decouverte vs rupture) est
   donc inapplicable.

### Colonne A -- verdicts contre le gel v1 (6284f247..., seul certifiable ici)

- **P-M8-pre : LIEN CONFIRME** (argmin K5 a 1.35 ; porte identique dans les
  deux gels).
- **P-M8a : NON CONCLUANT.** rho(T,K5) = +0.3714 aux DEUX troncatures
  (p exact 0.2486, n = 6, seuil +-0.80). Anti-arret-optionnel : non
  applicable. Robuste aux deux jeux d'ancres (cf. sensibilite ci-dessous).
- **P-M8b : branche « <= 3 quelque part » DECLENCHEE** -> le NON CONCLUANT
  porte le caveat : la cause (2) de M7 (composante fantome faible dans T)
  menace aussi p=5, au moins aux points 1.35, 2.40, 2.85.
- **P-M8-null : PASSE** (1.9e-23 aux deux points). Queues <= 2.2e-16.
- **G1 : 2.00 PASSE (0.11 %) ; 1.35 et 2.85 ECHOUENT (+11.8 % / +23.5 %).**
  Sans donnees de signe, la branche v1 ne peut pas router -> **INVESTIGATION
  OUVERTE**, exactement ce que v1 prescrivait en pareil cas.

### Colonne B -- verdicts contre le gel execute (cdd37877..., non certifie)

Tels que rapportes par machine 2 : « P-M8a CONFIRME » (= argmin), « P-M8b NON
CONCLUANT » + « replication_echouee: true » (clause +0.50), « P_M8d mediane
6.36, zone non tranchee ». Consignes avec provenance ; leur statut depend de
la production du bloc cdd et de la preuve de son gel AVANT code.

### Le confound qui suspend « M3 ne se replique pas »

L'ecart d'ancres traverse la calibration : avec la carte M3, g_cal(1.35)
vaudrait 8.57e-4 (M8 : 1.20e-3, x1.40) et g_cal(2.85) vaudrait 0.659 (M8 :
1.243, **x1.89**). Deux des quatre points canoniques de M8 tournent donc a
un couplage sensiblement different de celui que la carte M3 impliquait -- et
les DEUX inversions de rang qui font passer rho canonique de +1.00 (M3) a
+0.60 (M8) impliquent chacune un de ces deux points ((1.35 vs 2.00) et
(sqrt2 vs 2.85)). **« Le +1.00 de M3 ne se replique pas » est confondu avec
« M8 n'a pas refait les systemes de M3 ».** Tant que l'ecart d'ancres n'est
pas resolu, la requalification du +1.00 en fluctuation est PREMATUREE.
S'ajoute la fragilite du verdict-titre : sous les K5 de bord issus des
ancres M3, rho passe de +0.3714 a +0.4857 -- la clause +0.50 (non gelee v1)
se decide a 0.014 de rho pres. NON CONCLUANT est robuste ; « echouee » ne
l'est pas.

### Ce qui est acquis, independamment du litige

- **G7 : rho(T56, T64) = +1.00.** Le classement interne de M8 est stable en
  troncature (derives x0.86-1.45 qui ne reordonnent rien) : **la cause (1)
  de l'indecision M7 est ECARTEE a p=5** -- l'argument tampon Delta n = 5 du
  gel a fait exactement ce qu'il promettait. C'est le vrai gain de la manche,
  et il tient quel que soit le gel.
- **Paire a g apparie** : g_cal(1.35) et g_cal(2.00) different de 0.8 %, et
  T_retourne y differe de DIX ORDRES (7.8e-3 contre 7.4e-13). Le canal
  generique x^5 est reellement structure en w2 a gauche/centre ; au bord
  droit (g_cal 0.74-1.24) le couplage confond. A 2.85, le retourne fuit PLUS
  que le fantome (Q = 0.647). Post-hoc, etiquete, matiere pour l'option (c).
- Datum vallee : w2 = 2.40 passe G5 a 0.14 % a p=5 (g 0.05 -> 0.739) la ou
  p=7 excluait a 11.4 % (g 0.05 -> 0.131) : l'invariance affaiblie dans la
  vallee est degre-specifique, pas une affaire d'amplitude de saut en g.
- r(5) recalcule de M8 : 9.22 (M3 : 8.34). La bande de quasi-constance
  s'elargit a 6.6-9.2 ; l'enonce tient, p=3 (17.4) reste hors norme -- mais
  ce chiffre herite du litige d'ancres et sera revise avec lui.

### Statut de H-PROFONDEUR apres M8 (formulation corrigee)

Jambes classiques : inchangees, solides. Jambe quantique : **toujours aucun
soutien puissante** (M7 non concluante ; M8 NON CONCLUANT sous v1, avec
caveat P-M8b) -- cet enonce-la est robuste et suffit. En revanche « M3 perd
son seul soutien empirique » est SUSPENDU au confound d'ancres : pas de
cadavre tant que l'arme n'etait pas gelee et que le tir n'est pas propre.

---

## E19 -- Rupture du circuit de certification : M8 executee contre un gel
## non certifie machine 1

Faits etablis : (i) gel execute cdd37877... != gel v1 depose 6284f247... ;
(ii) aucun script machine 1 n'existait ; le circuit gele depuis M6 (gel ->
certification croisee -> script jumeau -> feu) a ete court-circuite ;
(iii) cinq divergences de fond constatees depuis les seuls resultats (liste
en S22), dont DEUX changent des lectures (clause +0.50 portant le
verdict-titre ; mediane supprimant un caveat que la fourche v1 declenchait)
et UNE supprime le garde qui aurait detecte l'anomalie la plus importante de
la manche (les ancres de bord).
Ce que E19 n'etablit PAS : si le bloc cdd a ete gele sur machine 2 AVANT
l'ecriture du code (auquel cas c'est un fork v2 legitime localement mais non
certifie -- une rupture de circuit, pas une falsification), ou adapte
pendant/apres. La distinction attend trois artefacts : le TEXTE du bloc
cdd37877, le script 49d6dccf, et leurs horodatages relatifs.
**Regle tiree, a geler pour toute manche future : un run n'est opposable a
la campagne que si l'empreinte de son gel figure dans un message de
certification CROISEE anterieur au depot du script. Un gel modifie, meme en
mieux, redevient un gel v(n+1) a certifier -- la qualite d'une clause ne
remplace pas sa chronologie.**
Precedent de prudence : E12 -> E13 (le premier diagnostic d'une anomalie de
canal s'est revele faux) ; la presente liste de divergences est revisable
sur production des artefacts.

---

## INVESTIGATION D'ANCRES (ouverte, prealable a toute manche quantique)

**Question** : s*(p=5, g=0.05) a 1.35 et 2.85 -- 0.310/2.586 (M3) contre
0.34648/3.19469 (M8), ecarts +11.8 % / +23.5 %, alors que 2.00 concorde a
0.11 %. Motif « centre exact, bords faux » -> causes candidates, aucune
choisie : (a) convention de signe (v1 exigeait min des deux ; execute
inconnu ; M3 inconnu) ; (b) resolution de bracket aux grands s* (precedent
langue instable M5/G1-bis) ; (c) T d'integration ; (d) difference reelle de
moteur. **Protocole propose, gelable en mini-manche** : aux deux points,
brackets IDENTIQUES denses (n = 96, bornes fixees d'avance), DEUX moteurs
(celui de M3 et celui de M8), DEUX signes chacun ; critere : accord <= 2 %
inter-moteurs a convention egale, sinon diagnostic moteur. Cout : 8
recherches, ~4 min.

## DEMANDES D'ARTEFACTS (bloquantes pour clore S22)

1. Texte integral du bloc cdd37877... + script 49d6dccf... + horodatages
   (gel vs premiere ecriture du code).
2. Provenance des s*F de M3 (convention de signe, grille/passes, T, g).
3. m3_quantum_N64.json : les T des 4 points canoniques, pour le rapport
   T_M8/T_M3 que v1 demandait (P-M8c) et que l'execute n'a pas produit.

## SUSPENSIONS

- Aucun gel M9 tant que : custody M8 non resolue, ancres non resolues.
  (v1 l'exigeait deja : pas de troisieme manche quantique sans changement
  d'estimateur ; le diagnostic G7 est fait -- c'est la custody et les ancres
  qui bloquent desormais.)
- La requalification du +1.00 de M3 est SUSPENDUE (confound).
- r(5) = 9.22 provisoire, herite du litige.
