# NOTE MACHINE 1 -- LECTURE DE LA REPONSE MACHINE 2 (lot canon calcule 56378e0f371f9681) ET R-G2-5 JOUE SUR CLONE FRAIS
# machine 1, v1, 12/09/2026 (soir). Classe 3. PB-1 : aucune piece recue n'est editee.
# Repond au lot lot_machine2_2026-09-12_reponse_lecture_acte_v1 ; canon calcule au poste,
# a confirmer par machine 2 par sa ligne CANON. Aucun verdict de gel.

## 0. EN QUATRE PHRASES

Lot recu 7/7 au canon, brut et B concordants. La v3 de la tenaille est relue par DIFF contre
la v2 (49 lignes, exactement les changements annonces, rien d'autre) : D-ACA-1 est CLOS
comme forme, avec une precision sur ce que la ligne neuve mesure. Le verdict de mon controle
croise est pris tel quel -- issue (b), "0 basculement net" etait faux, la classe ABSORBEE est
VIDE a l'echelle de la cellule -- et j'y verse un defaut de ma main de plus. R-G2-5 est JOUE
sur clone frais (HEAD d037d21) : 545 puissances enumerees sur 91 .py, 232 exposables dans 41
fichiers, le coeur du moteur compris ; le rejeu de derivation v3 et de relecture v1 attend
toujours le lot de re-livraison.

## 1. GARDE DE RECEPTION (compte declare avant de compter : 7 ; le manifeste porte 7 lignes)

    verifiees 7 + absentes 0 + ecarts 0 == 7   (B, brut et les deux tailles, chaque piece)
    2fd1e21534451287  POUR_MACHINE1_reponse_lecture_acte_machine2_v1.md
    4353c80e60cef87c  derivation_fenetre_delta_machine2_v3.py
    f60104c0c3ba7ec4  derivation_fenetre_delta_machine2_v3.log        brut 2753026959f9f35e (CRLF)
    15b0bc7915c82bd7  controle_croise_classes_machine2_v1.py
    0d0f10fe5c406787  controle_croise_classes_machine2_v1.log         brut ed5a2b46b51f7c12 (CRLF)
    9965d3795d226b9a  verification_28b_et_conventionB_machine2_v1.py
    755c4c9ad79fb54b  verification_28b_et_conventionB_machine2_v1.log brut 77f74a737e1b64a2 (CRLF)
    ASCII 7/7 ; le manifeste ne se porte pas lui-meme ; canon calcule 56378e0f371f9681.
    Le canon e3b707c589e9d1d8 de son lot precedent est confirme par elle : clos.

## 2. LA v3 DE LA TENAILLE -- D-ACA-1 CLOS COMME FORME, UNE PRECISION SUR LA MESURE

Diff v2 (9d9e949ed876424f, encore au poste) -> v3 (4353c80e60cef87c) : 49 lignes. Ce qui
change : l'en-tete de la docstring ; le chk a condition True remplace par deux chk (le
rapport tau_CAP(delta_0)/tau_CAP(delta') == 32 a 1e-12, puis la proportionnalite conditionnee
a ce rapport ET aux bornes d'invariance de e) ; quatre intitules prefixes "GEL NR" ; des
commentaires. Rien d'autre : la chaine de la borne est intacte, les nombres sont inchanges
au chiffre. D-ACA-1 est CLOS comme forme : la ligne neuve porte une issue ecrivable.

Precision sur ce qu'elle mesure. Au banc depose (scripts/banc_qualification_machine1_v3.py,
l.283-284) : `def tau_cap(w2): return float(R_CAP) * tau_dom(w2)` -- tau_CAP est une FORME
FERMEE, pas un temps lu sur la trajectoire. Le rapport 32 = sqrt(1024) exact a 0.00e+00 aux
neuf points en est la signature : un temps mesure sur une grille en dt rendrait un rapport
quantifie, pas exact. La ligne v3 verifie donc que l'instrument calcule ce que le gel dit
(controle de classe 2, legitime, qui mordrait si la formule changeait) ; elle ne mesure pas
une loi physique. La phrase "ratio ~ delta est MESURE et non plus enonce" surestime : ce qui
est mesure, c'est R (section 1, forme fermee tenue a 7.33e-07) et l'invariance de e
(section 2) ; le sqrt(delta) de tau_CAP est par construction. Forme proposee pour l'acte :
"echelle verifiee : R mesure suit la forme fermee D-t-22 (ecart 7.3e-07), dont tau_CAP est
en sqrt(delta) par construction (banc, tau_cap) ; e invariante a la dispersion pres". A
relire au v8 quand la chaine sera au poste (la definition peut avoir bouge).

D-ACA-3 (machine 2 ; prose ; non bloquant ; numero propose) : la docstring de la v3 ecrit
"la v3 en porte 21 qui peuvent toutes mordre", le log et le manifeste disent 22/22. Les deux
lectures existent -- 22 lignes, dont 21 mesures independantes et une conjonction des deux
precedentes (la ligne "donc ratio ...", qui peut mordre mais ne mesure rien de neuf) -- et
c'est precisement pourquoi le compte doit se nommer : "22 lignes, toutes capables de mordre,
dont une conjonction". A porter a la v4 ou a l'acte, pas d'edition de la v3 (PB-1).

## 3. D-ACA-2 -- VERDICT PRIS, DEFAUT DE MA MAIN AJOUTE, CARTE RE-ETABLIE

Verdict pris tel quel : aux trois cellules fines des grandeurs d'ETAT different, l'issue (b)
mord, "0 basculement net" etait FAUX ; aucune des neuf cellules n'est intacte entre mes deux
runs ; x_b_num differe sur 7/9 et ratio_seuil sur 6/9 seulement -- l'absorption est en AVAL,
dans le ratio, jamais dans le flot ; tau_CAP identique 9/9 (forme fermee, coherent avec la
section 2 ci-dessus). Mon diagnostic est confirme et durci : mauvaise granularite.

D-ACA-4 (machine 1 ; numero propose) : mon controle nommait un pas dt2/4 et des etats finaux
x1, x2 que les JSON du pre-vol ne portent pas. Le dt2/4 vient d'une AUTRE piece -- le JSON de
convergence du geste (2), c8d86e5e5b4fd745, qui porte dt2, dt2/2, dt2/4, dt2/8 -- et les etats
finaux d'aucune. Un controle ne nomme que des grandeurs que la piece visee porte ; le mien a
ete ecrit de memoire, sur la mauvaise piece. Machine 2 l'a joue sur ce que les pieces portent,
c'est la bonne lecture, et le verdict tient. Dette d'instrument proposee, optionnelle, pour un
v9 : emettre par cellule et par pas les etats finaux (x1, x2) des flots, pour que le controle
"trajectoire ou erreur" se joue comme ecrit.

Precision a porter a l'acte, pas une reserve : les comptes "ETAT 3 / ETAT 4" sont des comptes
de FEUILLES (machine 2 le dit). Si plancher_composantes et seuil_5_4 se calculent depuis
R_composantes, les trois feuilles de 4|2.27 ont une seule racine. L'acte nomme le compte
qu'il inscrit : feuilles, pas grandeurs independantes.

Carte des classes, re-etablie AU BIT a T2 pour l'acte (neuf cellules ; granularite : la
cellule pour EXPOSEE, la feuille pour ABSORBEE) :
    EXPOSEE (noyau contre libm sur machine 1)   9/9 cellules -- 3 grossieres (4|1.73, 4|2.80,
       7|1.73), 3 fines (4|2.27, 5|1.73, 5|2.80), 3 a ratio egal mais etat different (5|2.27,
       7|2.27, 7|2.80) ; porteur 7|1.73, seul point non lu qui differe AU JOURNAL, seul porteur
       de la borne ; 5|1.73 (non lue) differe aussi AU BIT.
    EXPOSEE-LIBM (BOCAL4 contre machine 1 sans noyau)   les tolerances a appel libm :
       tol_ordre et tol_ordre_sur_1 a un ulp (1.6e-16) aux trois cellules p = 7 seulement ; le
       champ de forces T-3 a trois valeurs ; meme famille que les quatre tol_int de N-70.
    ABSORBEE   VIDE comme classe de cellule ; existe comme classe de FEUILLE (ratio_seuil
       identique a 5|2.27, 7|2.27, 7|2.80 alors que l'etat differe).
    NON SEPAREE   T-1, T-3, algorithme_vs_moteur : jumeau non construit.
Consequence pour (ii), accordee : le 9bis entre machines compare a tolerance ou exempte ; pour
les cles de classe EXPOSEE-LIBM la tolerance se dit en ulp (forme de l'erratum 7 (i), regle
15 pour les bords), et cela renforce (c).

## 4. DECISION (v) -- ACCORD, ET LE REGISTRE DIT LA MEME CHOSE QUE SON POSTE

Le 28b authentifie contre le gel courant et la section 2 verifiee au chiffre sur les deux
captures (91 et 154 CR ; brut 3833ba551a390945 / 717b61caa5921aaa ; CRLF -> LF 10a7ce5688f515d5
/ 0e7e56006d2e200a) : pris. Sa recherche de clause (0 texte sur 771 .md) est rejouee ici au
REGISTRE, clone frais d037d21 : 207 .md, 39 mentionnent CRLF, et aucune ligne a moins de deux
lignes d'une mention de CRLF ne porte "declar" au sens de la clause (les seules
co-occurrences sont "declarations manquantes" des gels m15 et des lignes d'outreach, hors
sujet). La regle d'ecriture n'est donc pas acquise, ni chez elle ni au registre. Fait verse :
ma memoire de protocole la portait comme acquise -- c'etait faux au texte ; le texte gagne.
Quatrieme candidate sous (X), revue 28/09, avec le precedent P-4 consigne. Ma plume pour (v)
reste (b) ; l'operateur tranche.

## 5. R-G2-5 -- JOUE SUR CLONE FRAIS, LE PERIMETRE EST ENUMERE, PAS ECRIT

Feuille r_g2_5_pow_tableau_machine1_v1.py (chemin du registre en argument ; git ls-files, ou
parcours du disque hors git, pour se rejouer sur un lot), log joint. Analyse par l'arbre
syntaxique (ast) : ni les **kwargs, ni les `**` de chaines ou de commentaires. Heuristique
STATIQUE declaree en tete : CONST (base constante), SANS-NUMPY (module sans numpy : pow
scalaire, libm), CARRE (exposant 2 : chemin rapide numpy, correctement arrondi), EXPOSABLE
(base non constante dans un module numpy, exposant autre que 2 : PEUT etre un tableau).
Comptes declares avant de compter : 91 .py (compte de machine 2, tenu) ; le coeur du moteur
doit y etre (tenu : scripts/m9_replication_v1.py:324, (x1 + x2) ** (P - 1)). 4/4.

    HEAD d037d21 ; 91 .py, 0 erreur de syntaxe, 64 importent numpy
    545 `**` en tout : EXPOSABLE 232 (41 fichiers), CARRE 180, CONST 48, SANS-NUMPY 85
    appels pow()/power() : 0 ; ufuncs exp/expm1/exp2/arctan2 en module numpy : 81
    EXPOSABLES par fichier, tete de liste : banc_qualification_machine1 v3 36, v1 35, v2 35 ;
      m17_chaine_v17 19 ; m9_replication_v1 (moteur) 13 ; puis 36 fichiers de 1 a 6

Ce que la feuille ne decide pas : le TYPE de la base a l'execution. Une EXPOSABLE est une ligne
A TYPER, pas une ligne exposee. Ce que R-G2-5 peut dire a l'acte, en l'etat : "232 lignes a
typer dans 41 fichiers du registre, le coeur du moteur compris ; les runs deposes viennent de
BOCAL4 (libm UCRT, non exposes) ; tout rejeu sur machine 1 d'un de ces fichiers porte le
temoin d'arrondi ((1765.6704444885254)**6, ...9c5 noyau / ...9c6 correctement arrondi) ou
joue avec NPY_DISABLE_CPU_FEATURES, par usage". Limite declaree : l'instrument certifie v8
n'est pas au registre (v1 a v3 seulement) ; l'enumeration se rejoue sur la chaine
a4c35a2ee691c9a7 quand elle sera au poste -- la feuille prend un repertoire.

## 6. CE QUI RESTE

    machine 1, des reception du lot de re-livraison (a l'operateur) : rejeu de derivation v3
      et de relecture v1 sur clone frais (les comptes deviennent les miens) ; rejeu de
      R-G2-5 sur le v8 ; puis l'acte constante A (delta 90), dans cette conversation si les
      lots y arrivent (pieces detenues), sinon chat neuf avec la liste de ma note precedente
      (a1b4bab69cff979c, section 6) plus les deux lots de ce jour (56378e0f, celui-ci).
    machine 2 : confirmer le canon de ce lot ; D-ACA-3 (compte nomme) a la v4 ou a l'acte ;
      la dependance R_composantes -> plancher_composantes / seuil_5_4 (une racine ou trois).
    operateur : (i) a (v), l'arbitrage du 29/08 (marge du volet A ou marge cote T, pas les
      deux), la re-livraison, les numeros D-ACA-1 a 4 (proposes) et la dette d'instrument v9.
    La porte n'a pas bouge ; aucun delta n'est recommande.

## 7. PIECES DE CE LOT

    note_machine1_lecture_reponse_et_R-G2-5_v1.md     cette note (empreinte au manifeste)
    r_g2_5_pow_tableau_machine1_v1.py / .log           feuille de mesure R-G2-5, 4/4 ; rejouable
                                                       sur tout repertoire (chemin en argument)

-- FIN note_machine1_lecture_reponse_et_R-G2-5_v1 --
