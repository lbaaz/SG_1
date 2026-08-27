# PRE-VOL OPPOSABLE SOUS LES GELS v7 / v5 -- CERTIFICAT D'EXECUTION
# Machine 2, 28/08/2026. Sur ordre de l'operateur, APRES ma certification.
# Instrument : banc_qualification_machine1_v3.py  5fae2a8c94cf8685  144725 o
#              CERTIFIE par note_machine2_certification_instrument_v3.md
#              baf75f462ab14119, contresignee 146f7dd9d81ace1d --
#              certification ANTERIEURE a ce run (E19).
# Gels       : temoin v7 8b083e9f109b5a8e ; alpha v5 045c2435aaf623ce
#              (registre 0485001) ; moteur c8ed357b120352c4 ; carte
#              fa109da92e582520.
# Files      : E18, aucun numero pris ; maximum cite E42, N-69, D-M17-45.

RESUME -- DIX LIGNES

```
    1  temoin : REGLAGE QUALIFIE, branche 5, 4.8 s ; comptes 41 + 0 == 41
    2  alpha  : LIEN NON ETABLI (9/27) -- VERIFIE, 5.3 s ; 90 + 0 == 90
    3  W-integrales JOUEE pour la premiere fois (gel v7) : q_int lu sur
       les flots dt et dt/2, les deux etats
    4  les NEUF signes joues, consignes : +1 +1 +1 | +1 -1 -1 | +1 -1 -1
    5  seize gardes enumerees des gels, SEIZE demontrees mordantes DANS
       le run ; aucune sans morsure, pour la premiere fois
    6  les trois NE-JOUE-PAS dans chaque journal ; 0 run saute
    7  MANIFEST verifies par sha256sum -c : 5 fichiers (temoin), 65 (alpha)
    8  REPRODUCTIBILITE : deux runs du meme instrument ne different que
       par TROIS champs de duree, tous dans une cle deja NON PREDITE
    9  les trois portes rejouees sur CES artefacts : toutes fermees
   10  banniere et statut PREVOL dans les deux JSON (N-62) ; ASCII, CR = 0
```

## 1. CE QUE CE PRE-VOL EST, MODE PAR MODE

**Inchange depuis le 27/08, et il faut le redire a chaque fois :**

**LE TEMOIN.** T-1 et T-1b -- **le discriminant** -- sont SYNTHETIQUES,
par le canal `prevol` (verifie a la source : `executer_temoin` n'ecrit
que DEUX cles sous ce chemin). Le verdict REGLAGE QUALIFIE est celui
d'un discriminant lineaire par construction, et **ne dit rien du regime
de (2.11).** Tournent en vrai : T-2, W-bascule, T-2a, T-2b, T-3b, le
controle d'algorithme (9/9 au bit) -- et desormais **W-integrales, sur
les flots synthetiques a dt et dt/2**.

**ALPHA.** `SynthAlpha`, l'ansatz EXACT : les trajectoires sont
fabriquees, pas integrees. **Son VERIFIE ne dit rien d'alpha** ; il dit
que la plomberie atteint la branche 5 quand l'ansatz est parfait, et que
le factice tue les 18 indices de lignee (9/27 attendu, 9/27 obtenu).
Les tolerances rendues sont celles de l'ANSATZ.

**ET LE SIGNE N'EST PAS EPROUVE ICI (D-c-2).** Ma mutation de
certification l'a montre : signe force a +1, le pre-vol rend VERIFIE
quand meme. Le signe est protege ailleurs -- `lire_signes` ARRETE sur une
carte incoherente, il atteint les cinq appels de trajectoire, et un signe
faux au run donne NON CONCLUANT DE FENETRE. **Consigne a l'acte par
arbitrage de l'operateur du 28/08, avec D-c-1.**

## 2. LA REPRODUCTIBILITE, MESUREE -- ET C'EST ELLE QUI PORTE LA PREDICTION

J'ai joue le pre-vol DEUX FOIS avec le meme instrument, sur la meme
machine (une fois pendant la certification, une fois ici). Comparaison
champ par champ :

```
    les 19 cles IDENTIQUES : AUCUN ecart, aucun
    seul ecart des deux JSON, en tout et pour tout :
      T1b.recherches.a.duree_s   1.2870e-04  vs  1.3000e-04
      T1b.recherches.b.duree_s   4.5300e-05  vs  5.3700e-05
      T1b.recherches.c.duree_s   4.2100e-05  vs  5.3700e-05
    -- trois champs de DUREE, tous dans T1b, deja NON PREDITE.
    Et j'ai sonde les 19 IDENTIQUES pour un champ de duree cache
    (motif duree|temps|elapsed|_s) : AUCUN.
```

**Sans cette mesure, la prediction n'etait qu'une intention.** Elle dit
maintenant quelque chose de verifiable : les 19 cles sont stables d'un
run a l'autre, donc **si elles bougent au run reel, c'est que quelque
chose a bouge -- pas la machine, pas l'horloge.**

## 3. LA PREDICTION OPPOSABLE, ANCREE SUR CE RUN

Profondeur DECLAREE : cles de tete, plus UN niveau pour `meta`,
`banc_gardes`, `ne_joue_pas`, `comptes`. Sur
`out_prevol_v3_opposable/temoin/resultats_temoin.json` (**786a368878768d4b**) :
**47 cles = 19 IDENTIQUES + 7 NON PREDITES + 2 exemptes + 19 meta.\***

```
    IDENTIQUES au caractere entre CE JSON et le run REEL :
      T2, T3b, W_comptes, algorithme_vs_moteur, attendus, attendus_total,
      banc_gardes.ok, banc_gardes.n, banc_gardes.demontrees,
      champ_forces_empreinte, comptes.comptes, comptes.sautes,
      comptes.sautes_noms, mode, ne_joue_pas.gardes_sans_morsure,
      ne_joue_pas.runs_non_joues, reglage, symbolique, transcription_ok
      (comptes.* et ne_joue_pas.runs_non_joues : identiques SI rien n'est
       saute ; un saut est un VRAI ecart et se consigne)
    NON PREDITES -- et c'est le banc :
      T1, T1b (synthetiques ici), T3a (une MESURE desormais : q_int et
      tol_int sur les flots a dt/2), lectures_non_lues,
      ne_joue_pas.lectures_non_lues, verdict, branche
    EXEMPTES : prevol, statut, meta.* (dates, chemins, plateforme)
    PORTEE : le JSON, PAS le journal (durees, lignes de derive).
    Tout ecart de la premiere liste se consigne AVANT d'etre explique.
    Tout "ecart" de la deuxieme n'en est pas un.
```

Contresignee par machine 1 (146f7dd9d81ace1d, section 3) dans cette forme
et a cette profondeur.

## 4. LES TROIS PORTES, REJOUEES SUR CES ARTEFACTS

```
    (a) alpha REEL avec le temoin de CE pre-vol
        -> "ARRET PORTE : le temoin cite n'est pas un run REEL
            (statut 'PREVOL')."
    (b) alpha REEL sans --porte-temoin
        -> "ARRET PORTE (gel alpha 5) : --porte-temoin exige, le temoin
            passe avant tout run alpha."
    (c) temoin REEL vers un dossier de pre-vol
        -> AssertionError : "un run reel ne s'ecrit pas dans un dossier
            de pre-vol".
```

## 5. PIECES (convention B, NFC + LF)

```
    out_prevol_v3_opposable/temoin/
      resultats_temoin.json     786a368878768d4b    23350 o
      journal_temoin.txt        02199f736aaa8c95    14811 o
      MANIFEST.sha256           c2ae8512af00977d      444 o  (5 fichiers)
    out_prevol_v3_opposable/alpha/
      resultats_alpha.json      4bd6717801a1f1cc   107730 o
      journal_alpha.txt         6f1675a6b859d429    27617 o
      MANIFEST.sha256           eb6d50124d9fbef3     6750 o  (65 fichiers)
    instrument     5fae2a8c94cf8685  144725   CERTIFIE
    certification  baf75f462ab14119    8931   (ANTERIEURE, E19)
    contresignature m1  146f7dd9d81ace1d   2633
    gels           8b083e9f109b5a8e / 045c2435aaf623ce  (registre 0485001)
```

## 6. CE QUE CE PRE-VOL NE JOUE PAS

**Il ne mesure rien (N-62)** : banniere et statut PREVOL dans les deux
JSON, et l'instrument refuse d'ecrire un pre-vol hors d'un dossier qui
porte le mot. Il ne joue **aucun discriminant** (T-1, T-1b synthetiques)
et **aucune physique d'alpha**. Il n'eprouve PAS le signe (section 1).
Il ne tranche aucun fait. Il n'ouvre pas la porte du run reel d'alpha.
Il ne prend aucun numero.

## 7. CE QUI RESTE

```
    1. l'acte de registre : LD-15, la chronologie de LD-4, le numero D de
       machine 1, mes cinq errata, les cinq faits, D-c-1 et D-c-2
       (plume machine 1, ma certification, puis depot) ;
    2. le temoin REEL, contre la prediction de la section 3 ;
    3. alpha aux TROIS degres, ssi REGLAGE QUALIFIE.
    Le run du temoin n'attend plus rien : ni gel, ni instrument, ni
    pre-vol, ni prediction. Il n'attend que l'ordre.
```

-- FIN note_machine2_prevol_opposable_v3 --
