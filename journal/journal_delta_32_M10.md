Journal bundle 5 -- DELTA du 27/07/2026 : section 32 -- MANCHE M10 EXECUTEE.
G6 A DECLENCHE, LE PLAN S'EST EFFONDRE, ET LA LECTURE L1 EST CONSIGNEE SANS
ETRE LUE.

S'insere apres journal_delta_31_L1.md. Traces : m10_results.json (7cf3624b...),
m10_certification_run_machine2.md, audit_m10_resultats_machine2.log (machine 2) ;
lecture_L1_sur_m10.py (44c71296..., machine 1).
CUSTODY : gel c1d42aa5 (v8) | script c3a91f60 (v3) | moteur c8ed357b |
71/71 recherches, 64/64 balayages, G3 a 4.75e-16 sur 8 rebindings.

---

## 32.1 CE QUE LA MANCHE A RENDU

  P-M10a   NON CONCLUANT DE PUISSANCE
  P-M10b   COMPATIBLE (|Dbeta| = 0.06863), mais de FAIBLE PUISSANCE
  P-M10f   (i) 0.222992 contre repere 0.2230, ecart -8e-6 -- REPLIQUE
           (ii) 0.370872 sur 16 points
           argmax de d = 2.75 -> SECONDE BRANCHE DECLENCHEE
  fit      9 points par degre apres amputation G7 ; Sxx 7.4425 -> 4.5268
  beta     1.02359 (p=5) | 0.95496 (p=7)

G6 A DECLENCHE, ET C'EST LE RESULTAT PRINCIPAL DE LA MANCHE. A p=5, w2=1.25,
sgn=-1 : la bissection rend s* = 0.23877, une explosion existe a 0.23390, soit
2.0 % SOUS, avec deux ilots. L'ensemble d'explosion n'y est pas une
demi-droite. La garde ecrite apres D-M10-1 pour un defaut constate a p=3 a
mordu a p=5, sur un point neuf, des le premier run -- et exactement au point
que la consignation du PROTOCOLE DE FIT avait designe comme "assis sur une
resonance" (5:4, ordre 9) et "de plus grand levier du fit". La garde et la
consignation ont converge par deux chemins independants.

## 32.2 LA LECTURE L1 EST CONSIGNEE, ELLE N'EST PAS LUE

DECISION DE MACHINE 1, prise avant de regarder les nombres. Le gel ecrit, pour
la branche NON CONCLUANT DE PUISSANCE : "le plan ne permettait pas de
conclure, AUCUNE LECTURE PHYSIQUE N'EST AUTORISEE". L1-a (identification de
F et Z), L1-g (carte de zeta point par point) et L1-k (discrimination des
mecanismes) sont des lectures PHYSIQUES baties sur les memes beta. Elles
heritent donc du verdict : **CONSIGNEES, PAS LUES**. Aucun mecanisme n'est
identifie par ce run, aucun theta n'est retenu, aucun point du plan (F, Z)
n'est ecarte ni rapproche.
L1-i et L1-j ne sont pas des lectures physiques : ce sont des DIAGNOSTICS DE
PLAN. Ils sont lus.

VALEURS CONSIGNEES, sans lecture :
  F = +0.5147   Z = +0.8520   kappa (9 pts retenus) = 0.5357   theta = 0.2763
  theta ajuste sur la CARTE de zeta (9 points, 8 ddl) = 0.1743
  Z des reperes sur cette grille : A2 1.0000 | max|x| 0.6206 | A1 0.4643

## 32.3 LE PIEGE QU'IL FAUT NOMMER AVANT QU'IL SOIT CITE

La table L1-k, prise au pied de la lettre, dit que "fermeture de largeur
resonante" tombe a 0.2 largeur a p=5 et 1.6 a p=7 -- c'est-a-dire qu'elle
COLLE. Ce serait un renversement du S27.3 et de la consignation C31-1.
C'EST FAUX, ET LA RAISON EST ARITHMETIQUE. Les largeurs de L1-k ont ete
RECALCULEES sur le jackknife mesure, comme C31-3 l'exige :
    largeurs concues (L1 v4, modele projete) : 0.0463 (p=5) | 0.0233 (p=7)
    largeurs MESUREES sur ce run             : 0.1672      | 0.0442
    facteur                                  : x3.6        | x1.9
L'ecart du mecanisme a p=5 vaut 0.0380 : c'est 0.2 largeur MESUREE, mais 0.8
largeur CONCUE. **Le mecanisme ne s'est pas rapproche ; c'est la regle a
mesurer qui a triple de graduation.** Un instrument dont la graduation triple
ne discrimine plus -- il rend tout compatible avec tout. Aucune conclusion,
dans un sens ni dans l'autre, ne sort de L1-k sur ce run.

## 32.4 L1-j : LA SEULE INCERTITUDE REELLE, ET ELLE EST ENORME

  etendue leave-one-out : beta(5) 0.1672 | beta(7) 0.0442
                          F 0.9620  [0.4142 , 1.3762]
                          Z 0.1598  [0.7140 , 0.8738]
                          kappa 0.1211
  point le plus influent : w2 = 1.30

L'INTERVALLE DE F COUVRE LES DEUX MECANISMES MORTS -- 1.0000 et 1.3461 sont
tous deux DEDANS. F n'est donc pas mesure par ce run, et le dire vaut mieux
que citer un F a quatre decimales. Ce constat est INDEPENDANT du verdict du
gel et il pointe dans le meme sens : la porte P-M10a et l'instrument L1-j
disent tous deux que le plan s'est effondre, par deux chemins qui ne se
parlent pas.

CE QUE L'AMPUTATION A REELLEMENT COUTE, chiffre :
    fit non ampute (10 pts) : beta5 0.99039 beta7 0.92429 | F +0.4957 Z +0.8251
    fit ampute      (9 pts) : beta5 1.02359 beta7 0.95496 | F +0.5147 Z +0.8520
Le retrait d'UN point deplace F de 0.019 et Z de 0.027 -- des broutilles. Mais
il triple l'etendue jackknife. **L'amputation n'a pas deplace la reponse, elle
a detruit la capacite de la connaitre.** C'est une perte de PUISSANCE, pas de
justesse, et c'est exactement ce que la branche mecanique du gel nomme.

LE LEVIER A CHANGE DE MAIN, ET LE PROBLEME AVEC. Avant amputation, 1.25 portait
un levier |ln D - moyenne| = 1.6199 ; apres, 1.30 en porte 1.5956, contre 0.7387
au deuxieme (2.85). Le plan est otage de 1.30 exactement comme il l'etait de
1.25. **Ce n'est pas 1.25 qui etait fragile : c'est la geometrie de la grille,
qui met tout son bras de levier sur un point unique au bord gauche.** A porter
au dossier de conception de la manche p=4.

## 32.5 L1-i ET C31-2 : LES DEUX SEULES LECTURES QUI TIENNENT

  rho(res5, res7) = +0.8565 sur 9 points   [attente L1-i : > +0.5]  CONFORME
Lecture gelee appliquee : rho eleve signifie que l'inadequation de la loi de
puissance est en grande partie COMMUNE aux degres, donc portee par psi
(l'amplitude) plutot que par phi (la durete).

C31-2 VERIFIEE. Le nuage jackknife dans le plan (F, Z) a une correlation de
-0.9938 : c'est un segment, comme la consignation de cloture l'annoncait, et
sa pente vaut -0.1603 contre -0.0654 projete au modele quadratique -- dans la
plage de sensibilite publiee en L1 v4 S4. La consignation disait : "la
colinearite tient tant que psi domine phi, c'est-a-dire tant que rho est
eleve". rho vaut 0.86 et le segment est la. **Les deux lectures se tiennent
l'une l'autre, comme ecrit avant mesure.**

## 32.6 LE REGISTRE DES ATTENTES

Applique automatiquement par lecture_L1_sur_m10.py, sans intervention.
  L1 v1  F dans [-0.2, +0.6]        mesure +0.5147   CONFORME
  L1 v1  Z dans [0.80, 0.95]        mesure +0.8520   CONFORME
  L1 v3  etendue de F [0.15, 0.45]  mesure  0.9620   CONTRE MOI
  L1 v3  etendue de Z [0.04, 0.12]  mesure  0.1598   CONTRE MOI
  L1-i   rho > +0.5                 mesure +0.8565   CONFORME
  P-M10f argmax dans {2.30,2.45,2.60} mesure 2.75    CONTRE MOI

UN FAIT DE METHODE, ET IL EST LE PLUS INSTRUCTIF DE LA SEANCE. L'attente de
L1 v1 -- ecrite la premiere, jamais reecrite -- TIENT sur F et sur Z. La
projection de L1 v2, que machine 2 avait etablie et que j'avais consignee
comme "l'element le plus informatif disponible, et il est defavorable a
l'attente", est PLUS LOIN sur les deux :
    F : mesure 0.5147 | v1 [-0.2, +0.6] dedans | projection 0.6825, ecart 0.168
    Z : mesure 0.8520 | v1 [0.80, 0.95] dedans | projection 0.7531, ecart 0.099
Si l'attente de v1 avait ete REECRITE pour suivre la projection -- ce que la
tentation commandait, et ce que machine 2 avait explicitement recommande de ne
pas faire -- elle serait aujourd'hui fausse sur les deux coordonnees. La regle
"ne jamais reecrire une attente, en ajouter une seconde etiquetee" n'a pas
seulement protege l'opposabilite : elle a protege la bonne reponse.
NOTA HONNETE : ce constat porte sur des beta issus d'un plan NON CONCLUANT.
Il vaut comme lecon de METHODE, pas comme confirmation de l'attente.

RESERVE DE MACHINE 2 TENUE, LA MIENNE NON. Son pre-chiffrage de l'etendue de F
(0.1728) etait declare PLANCHER : 0.9620 >= 0.1728, le plancher tient. Ma
fourchette [0.15, 0.45] etait un intervalle, et elle est fausse par plus du
double. Sur l'etendue de Z, j'avais montre que le chiffre etait pose a cote
d'un zero et pouvait aller dans les deux sens : il est alle vers le haut,
0.1598, au-dessus de ma fourchette comme du pre-chiffrage.

## 32.7 REGLE 13, ACCEPTEE

Enonce de machine 2, adopte sans modification : tout seuil DERIVE d'une
quantite de plan (Sxx, n, levier) qu'une garde est autorisee a modifier est
gele SOUS SA FORME DERIVEE, pas sous sa forme numerique ; le script rapporte
les deux valeurs et le gel declare AVANT MESURE laquelle fait foi.
MEME FAMILLE QUE D-M10-14, et il faut le dire : un seuil numerique fige est un
nombre qu'un artefact affirme sur un plan qu'il n'a pas eu, exactement comme
le compte de 71 etait un nombre affirme sur des recherches que personne ne
comptait. Les deux se corrigent par le meme geste -- recalculer au lieu
d'affirmer.
Ici la question ne mord pas : sigma(p=5) = 0.13973 depasse le seuil gele
(0.1392) de +0.38 % ET le seuil recalcule (0.1086) de +28.7 %. Le verdict est
robuste des deux cotes. Mais a 0.38 % pres il dependait d'un plan hypothetique.

## 32.8 CE QUI RESTE

  - E24 et le fit : les grandeurs de grille de L1 etaient indexees sur FIT11,
    puis sur le fit a 10 points ; le fit REELLEMENT retenu en a 9. Toutes les
    valeurs de kappa, Z(reperes) et theta du bloc L1 sont a relire sur 9
    points -- fait dans ce delta, a propager au bloc.
  - l'etendue d'archive 0.2836 est SANS OBJET par declenchement de la branche
    pre-declaree de P-M10f. A retirer des tables avec renvoi a ce run.
  - la bande r pour p >= 4 : bord droit a 8.347 (D-M10-5).
  - question ouverte pour une manche : le creux de 2:1 mord-il au-dela du
    rayon 0.12 ? Les residus les plus negatifs sont domines aux DEUX degres
    par w2 = 2.15, a 0.15 de 2:1, juste au-dela du rayon declare.
  - LA MANCHE p=4 : elle etait le seul test de la classe (L1-h). Elle est
    desormais aussi le seul moyen de RECUPERER DE LA PUISSANCE, puisque le
    levier de la grille M10 tient a un point unique et que G6 peut le retirer
    a tout moment. Sa conception doit repartir de la geometrie du plan, pas
    de la liste de points.

=== FIN DU DELTA 32 ===
