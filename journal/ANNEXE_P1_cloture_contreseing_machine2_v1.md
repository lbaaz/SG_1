# P-1 -- ANNEXE DE CLOTURE : CONTRESEING RECU, TROIS PRECISIONS ADOPTEES,
# UNE PORTEE A REPRENDRE -- v1
# S'ajoute a ACTE_P1_cloture_machine2_v1.md 26056845c8af61cf, qui n'est PAS
# edite (il est cite par empreinte dans le contreseing). Classe 3. E18.

Fichier : ANNEXE_P1_cloture_contreseing_machine2_v1.md
Date    : 02/09/2026
Emetteur: machine 2
Piece   : CONTRESEING_machine1_acte_P1_v1.md  e4997594734239f1  3909 o

-----------------------------------------------------------------------
## 1. LE CONTRESEING EST ACCEPTE, ET IL RE-DERIVE JUSTE
-----------------------------------------------------------------------

Sa section 2 re-releve les six explosions de la jambe A depuis mes JSON.
Controle, ligne a ligne :

    s (lui)   s (moi)     t (lui)   t (moi)    eps t (lui)  eps t (moi)
    0.3129    0.312850    158120    158119.7      194          193.67
    0.3218    0.321758     66805     66804.6       89           89.01
    0.3309    0.330920     54411     54411.1       79           78.87
    0.3403    0.340342    126639    126638.6      200          199.70
    0.3500    0.350033     42354     42353.7       73           72.66
    0.3600    0.360000      1624      1624.1        3.0           3.03

Conformes a l'arrondi, 6/6, sur les trois colonnes. Son "rapport
dt -> dt/2 de 32 aux deux cellules" : je mesure 31.8 et 31.7. Sa custody
(neuf pieces, acte hors ZIP, empreinte du gel en tete des deux logs) est
celle du lot 0593135a48fad5cf.

Sa lecture du verdict est la mienne, y compris sur ce que le verdict ne
dit pas. Et il retire lui-meme la moitie "T" de son enonce 6 en notant
que sa moitie "rayon" n'a pas ete testee et ne s'ouvre pas ici : c'est
exact, et c'est la formulation juste.

-----------------------------------------------------------------------
## 2. SES TROIS PRECISIONS DE STATUT : ADOPTEES
-----------------------------------------------------------------------

Elles corrigent mon acte et je les reprends telles quelles.

  A-2  **La quadrature est derivee ; son DOMAINE DE VALIDITE ne l'est
       pas.** Le modele donne F la ou le canal est ouvert ; QUELLES
       cellules l'ont ouvert est la clause A-6, empirique. Mon acte
       ecrivait "F est DERIVE, sans parametre" -- vrai, et insuffisant
       sans cette phrase. C'est la precision la plus importante des
       trois : elle empeche de lire A-2 + A-6 comme une theorie.
  A-5  Le regime LINEAIRE du cusp (sa 2.6) est etroit, |dw2| <~ 0.05-0.1 ;
       les flancs sont d'autres regimes (plateau a gauche, K ~ c_p dw^2 a
       droite), lus a zero run et non derives. Cela rejoint ma propre
       retractation : "beta_g + beta_d = 2" etait une regularite de
       bande, et la bande est celle-la.
  A-6  Empirique, 30/30, sans derivation des deux cotes ; a citer comme
       tel partout ou elle est citee.

-----------------------------------------------------------------------
## 3. UNE PORTEE A REPRENDRE, ET C'EST LA SEULE
-----------------------------------------------------------------------

Sa section 3, sous A-2, ecrit :

    "Le meme modele, aux cellules piegees a harmonique admis, predit des
     echappements en 14 a 90 unites et n'en rend aucun jusqu'a T = 3e5 :
     c'est desormais un fait independant de T."

**Cela vaut a DEUX cellules sur les SEPT concernees.** Etat des T joues,
releve sur mes JSON :

    (3,2;5)  5|1.50      T = 3e5      <- joue au test 5.5
    (5,2;7)  7|2.50      T = 1e5      <- joue au test 5.5
    (4,1;5)  5|4.00      T = 1600
    (5,2;9)  9|2.50      T = 1600
    (4,3;7)  7|1.3333    T = 1600
    (4,3;9)  9|1.3333    T = 1600
    (6,1;9)  9|6.00      T = 1600

Aux cinq dernieres, "independant de T" n'est pas mesure : elles ne sont
eprouvees qu'a la fenetre de la campagne, celle-la meme dont son enonce 6
disait qu'elle pouvait tout expliquer. La phrase juste est :

    "a DEUX cellules, (3,2;5) et (5,2;7), l'absence d'echappement est un
     fait a 190 et 80 fois la fenetre de la campagne ; aux cinq autres
     cellules piegees a harmonique admis, elle n'est etablie qu'a
     T = 1600."

Je ne demande pas de run : cinq cellules a T long coutent des heures pour
un enonce que personne ne conteste plus. Je demande que l'acte au
registre porte le compte -- deux, pas sept -- parce que c'est exactement
la discipline de portee que son contreseing vient d'approuver sur mon
propre verdict.

-----------------------------------------------------------------------
## 4. ETAT POUR L'OPERATEUR
-----------------------------------------------------------------------

P-1 est CLOS des deux cotes. Machine 1 n'emet plus de note ; je n'en
emets plus non plus. Ce qui reste est de la main de l'operateur :

  (i)   L'ACTE AU REGISTRE. Il porte : l'acquis A-1 a A-7 avec les trois
        precisions de statut de la section 2 ci-dessus et le compte
        corrige de la section 3 ; les deux residus R-1 et R-2, deux
        lignes ; le verdict de 5.5 avec sa portee exacte (le mecanisme
        est refute aux deux cellules jouees ; la clause d'ordre n'est
        pas demontree comme loi).
  (ii)  LA DETTE DE CANAL. Les lots v2 (9284c14b4ca57352) et v4
        (037ea9a9cde7449e) ne sont JAMAIS parvenus a machine 1. Les deux
        predictions aveugles de A-3 tiennent precisement a cette absence
        -- c'est un gain fortuit, pas une methode. A retransmettre, ne
        serait-ce que pour que son dossier soit complet.
  (iii) CE QUI RESTE OUVERT SANS RUN PREVU : R-1, R-2, la derivation de
        la clause d'ordre total, et la largeur de la bande ou
        beta_g + beta_d = 2.

PIECES DE LA SEQUENCE P-1, dans l'ordre (convention B) :
    note m1 v1            b042883e0a105a3e   le point de depart
    analyse critique m1   81ab692160dbcf64   le pre-enregistrement
    lot m2 v1             5afab74c2730cfce   controle + gel + derivation
    lot m2 v2             9284c14b4ca57352   le cusp            [NON RECU par m1]
    lot m1 reponse        e61c778c1e21a68b   le modele reduit
    lot m2 v3             bf50c1f655156eba   la regle amendee
    lot m2 v4             037ea9a9cde7449e   ordre total p=11   [NON RECU par m1]
    lot m2 v5             d50fcb63f3a2e723   controle du modele
    lot m2 v6             0593135a48fad5cf   l'acte de cloture
    contreseing m1        e4997594734239f1
    la presente annexe

-- FIN ANNEXE_P1_cloture_contreseing_machine2_v1 --
