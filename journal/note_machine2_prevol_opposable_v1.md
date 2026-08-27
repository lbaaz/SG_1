# PRE-VOL OPPOSABLE DES DEUX BANCS -- CERTIFICAT D'EXECUTION
# Machine 2, 27/08/2026. Sur ordre de l'operateur, apres certification.
# Instrument : banc_qualification_machine1_v2.py  d74928ef093c96d0  133202 o
#              CERTIFIE par note_machine2_certification_instrument_bancs_v2.md
#              10d3160eef210015 -- certification ANTERIEURE a ce run (E19).
# Registre   : 37ad1b6 ; moteur c8ed357b120352c4 ; carte fa109da92e582520.
# Files      : E18, aucun numero pris ; maximum cite E42, N-69, D-M17-45.

RESUME -- DIX LIGNES

```
    1  temoin  : REGLAGE QUALIFIE, branche 5, 5.1 s ; comptes 39 + 0 == 39
    2  alpha   : LIEN NON ETABLI (9/27) -- VERIFIE, 5.6 s ; 90 + 0 == 90
    3  T-1 (A et B, identiques) : R = 1.9557 2.0227 1.9888 2.0056 ;
       disp 0.02245 ; tol_R 0.04491 ; tol_R/(q-1) 0.04491 (plafond 0.25)
    4  T-1b : seuils 0.9765628547 / 1.9531251619 / 0.4882817011,
       motif OK|pas=6.03e-07, k = 0 aux trois -- W-transcription (iii) PASSE
    5  T-3b : trois jeux PASSE (e = 4.4e-08, 7.1e-07 sur dix periodes)
    6  transcription contre l'algorithme DEPOSE : 9/9 AU BIT, motifs compris
    7  gardes : 16 enumerees des gels, 15 demontrees mordantes DANS LE RUN,
       W-integrales declaree non jouee (LD-9)
    8  les trois NE-JOUE-PAS sont dans chaque journal ; 0 run saute
    9  MANIFEST verifie par sha256sum -c : 5 fichiers (temoin), 65 (alpha)
   10  aucune mention d'outillage ; ASCII, CR = 0 ; banniere PREVOL et
       statut PREVOL dans les deux JSON (N-62 : aucune mesure n'existe ici)
```

## 1. CE QUE CE PRE-VOL EST, MODE PAR MODE -- ET ILS NE SONT PAS PAREILS

**C'est le point principal de ce certificat, et il ne se lit pas dans les
verdicts.**

**LE TEMOIN : le pre-vol EST le calcul du temoin, complet.** Le factice
substitue `integrer` et `chercher_seuil` du moteur depose. Or le temoin
n'appelle le moteur qu'a UN endroit, `controle_algorithme_contre_moteur`,
et cette fonction utilise `mod._chercher_depose` -- capture **AVANT** la
substitution (`charger_moteur` : `mod._chercher_depose = mod.chercher_seuil`
precede le remplacement) -- en lui fournissant son PROPRE integrateur
synthetique. **Donc rien du temoin ne tourne sur du faux.** Les flots de
(2.11), T-1, T-1b, T-2, T-3b sont la vraie physique de l'instrument.

**Consequence, et je la verse maintenant plutot que de la laisser
apparaitre plus tard :** je connais desormais le verdict du temoin,
REGLAGE QUALIFIE. C'est, en nature, la faute que machine 1 a versee
contre elle-meme (lire un verdict avant que l'attente soit reglee). Elle
est ici SANS consequence a une condition, que je pose en avance :

```
    PREDICTION PRE-DECLAREE, avant tout run reel du temoin :
    le JSON du run REEL doit etre IDENTIQUE a
    out_prevol_opposable/temoin/resultats_temoin.json (609acaf7f8f8df99)
    hors les seuls champs 'prevol', 'statut', la date et les chemins.
    Un ECART, quel qu'il soit, signifie que quelque chose a bouge HORS
    de l'instrument, et il se consigne avant d'etre explique.
    Si l'erratum du FAIT 1 passe a 41 runs, les comptes changent et la
    prediction porte alors sur les 39 runs communs, un par un.
```

Rien ne peut plus etre ajuste apres coup : le resultat est ecrit, gele et
date avant l'arbitrage.

**ALPHA : le pre-vol n'est PAS le calcul d'alpha.** `prevol_alpha`
injecte `SynthAlpha(s_etoile)`, l'ansatz EXACT : les trajectoires sont
fabriquees, pas integrees. **Son verdict VERIFIE ne dit rien de alpha ;
il dit que la plomberie atteint la branche 5 quand l'ansatz est exact**
-- et que le factice tue bien les 18 indices de lignee (9/27 attendu,
9/27 obtenu). Lire "VERIFIE" ici comme un resultat serait un contresens,
et c'est la seule facon de mal lire ce depot.
Les tolerances rendues (1.3e-04, 1.3e-04, 1.0e-04 ; tol_lnA 4.3e-08,
2.0e-08, 2.1e-08) sont celles de l'ANSATZ, pas de la physique : elles
mesurent le bruit d'ajustement de l'instrument sur une solution exacte.
**Elles sont d'ailleurs la meilleure illustration du FAIT 3** : une
tolerance de P-A de 4e-08 sur un biais de modele borne a 1e-03.

## 2. LES TROIS PORTES, JOUEES SUR LES PIECES DE CE RUN

Aucune n'est plaidee : chacune est jouee contre les artefacts produits
ci-dessus.

```
    (a) --mode alpha --porte-temoin <le temoin de CE pre-vol>
        -> "ARRET PORTE : le temoin cite n'est pas un run REEL
            (statut 'PREVOL')."
        La porte lit d'abord le fichier (elle affiche le reglage, les
        e/ln10 par degre), PUIS refuse. Un temoin de pre-vol n'ouvre pas
        la manche reelle.
    (b) --mode alpha sans --porte-temoin
        -> "ARRET PORTE (gel alpha 5) : --porte-temoin exige, le temoin
            passe avant tout run alpha."
    (c) --mode temoin --sortie out_prevol_triche (run REEL vers un
        dossier de pre-vol)
        -> AssertionError : "un run reel ne s'ecrit pas dans un dossier
            de pre-vol". La reciproque est gardee de meme.
```

## 3. CE QUE LE RUN A DEMONTRE DE LUI-MEME

Le banc des gardes se rejoue **A LA FIN DE CHAQUE RUN** (D-b-3) : chaque
journal porte donc, en propre, la demonstration que quinze de ses seize
gardes peuvent mordre -- ce n'est pas une propriete d'un banc joue a
part, c'est une propriete du journal qu'on lit. Les trois lignes
NE-JOUE-PAS enumerent, par la machine : les lectures non lues (au temoin :
T-3a / W-integrales, LD-9 ; a alpha : aucune), les gardes sans morsure
(W-integrales), les runs sautes (aucun).

## 4. PIECES (convention B, NFC + LF, sha256 tronque a 16)

```
    out_prevol_opposable/temoin/
      resultats_temoin.json     609acaf7f8f8df99    21140 o
      journal_temoin.txt        544f10dce5fff05f    14242 o
      MANIFEST.sha256           41b4ae7caa4713ee      444 o   (5 fichiers)
      + temoin_T1_flot_A.txt, temoin_T1_flot_B.txt,
        temoin_champ_forces_tirage.txt
    out_prevol_opposable/alpha/
      resultats_alpha.json      9cf4f242528dd057   104471 o
      journal_alpha.txt         f6eb3bc4decac991    26322 o
      MANIFEST.sha256           ea96e937fad7c157     6750 o  (65 fichiers)
      + 63 series alpha_serie_*.txt
    champ de forces (2.11) sur tirage declare : empreinte B f7f8be507eb5e9cb
      -- la double transcription reste due de mon cote (gel temoin 7).
    instrument   banc_qualification_machine1_v2.py  d74928ef093c96d0 133202
    certification note_machine2_certification_instrument_bancs_v2.md
                 10d3160eef210015  14174   (ANTERIEURE a ce run, E19)
    gels         35a70834b2a34514 / 0905a9b78ba40349   (registre 37ad1b6)
```

## 5. CE QUE CE PRE-VOL NE JOUE PAS

**Il ne mesure rien (N-62)** : les deux JSON portent la banniere et le
statut PREVOL, et l'instrument refuse d'ecrire un pre-vol ailleurs que
dans un dossier qui porte le mot. Il ne joue pas W-integrales (FAIT 1).
Il ne joue **aucune physique d'alpha** (section 1). Il ne tranche aucun
des quatre faits. Il n'ouvre pas la porte du run reel d'alpha, et il ne
prend aucun numero.

## 6. CE QUI EST DU, ET DANS QUEL ORDRE

```
    1. FAIT 1 (W-integrales, erratum et 41 runs, ou garde declaree non
       jouee) -- AVANT le run reel du temoin, qui en depend au compte.
    2. le run REEL du temoin, contre la PREDICTION PRE-DECLAREE ci-dessus.
    3. FAIT 3 (le plancher de tolerance de P-A) -- AVANT le run alpha.
    4. alpha SI ET SEULEMENT SI le temoin rend REGLAGE QUALIFIE en REEL.
    Les FAITS 2 et 4 se traitent au meme erratum, ou se consignent au
    delta du run.
```

-- FIN note_machine2_prevol_opposable_v1 --
