# CERTIFICATION DE L'INSTRUMENT DES DEUX BANCS -- machine 2, 27/08/2026
# Cible      : banc_qualification_machine1_v1.py  3a932eabfaaf4307  116438 o
# Barre      : POUR_MACHINE1_ordre_instrument_bancs_v1.md  6e176705468a4834
#              (points C-1 a C-12, annonces AVANT la livraison)
# Instrument : certif_instrument_bancs_machine2_v1.py / .log
#              53 controles joues, 47 passent, 6 mordent
# Files      : E18, aucun numero pris ici ; maximum cite E42, N-69, D-M17-45

VERDICT : **NON CERTIFIE EN L'ETAT. UNE v2 EST DUE, ET ELLE EST COURTE.**

          L'instrument est SAIN partout ou j'ai pu le jouer : les
          re-derivations sont exactes, la transcription survit a une
          jambe de mutation qu'il ne portait pas, le selftest et le banc
          se REPRODUISENT chez moi au verdict pres. Il ne franchit pas la
          barre sur UN point, **C-1**, et le correctif est ADDITIF : dix
          scenarios, deux gardes, une section de journal. Rien de ce que
          j'ai trouve ne met en cause la physique, la transcription, ni
          les chiffres.

          **Trois faits restent a trancher par l'operateur, et DEUX SONT
          DES DEFAUTS DE GEL -- donc de moi** (section 5).

---

## 1. CE QUE J'AI JOUE, ET NON CRU

**(a) LES DEUX MODES D'INSTRUMENT, REJOUES CHEZ MOI.** Ils ne sont pas
lus dans les journaux de machine 1, ils sont rejoues sur ma machine, avec
le registre 37ad1b6 :

```
    --selftest  72/72 en 2.7 s
    --banc      21/21 scenarios mordent, en 8.3 s
```

C'est le premier resultat de cette certification et il n'etait pas
acquis : **la chaine se reproduit d'une machine a l'autre**, moteur
depose charge et appele tel quel compris.

**(b) LES QUATRE ANCRES DU REGISTRE resolvent** : moteur c8ed357b120352c4
(36325, brut), carte fa109da92e582520 (130856, brut), gel alpha
35a70834b2a34514, gel temoin 0905a9b78ba40349. Le docstring cite les DEUX
gels ET les DEUX certifications (E19). **Et la garde d'ancre MORD** : sur
un registre absent, l'instrument s'arrete avant tout calcul
("ARRET E19 : gel absent").

**(c) LES TABLES DU GEL, RE-DERIVEES SANS RIEN LIRE CHEZ LA CIBLE.** En
exact (Fraction) puis en flottant, contre le TEXTE des gels :

```
    alpha_p = 4/(p-2)                       2, 4/3, 4/5             exact
    K_p     = a(a+1)(a+2)(a+3)              120, 3640/81, 9576/625  exact
    A_p                                     48.98979 9.65048 3.14244
    tau_dom                                 5.0044e-02 4.0314e-02 3.3634e-02
    dt_2 = r tau_dom / M                    2.5022e-04 2.0157e-04 1.6817e-04
    les NEUF CAP_p (5.4)                    concordent
    les NEUF bascules a k = 2 (5.3)         concordent
    den = 47^3 x 95 = 9 863 185 ; pas_k     6.0325e-07 1.8250e-06 3.8020e-09
    terme neglige delta/((a+2)(a+3))        1/2000, 9/13000, 1/1064
    8/15 et le plafond eta x 8/15 = 2/15    exacts
```

Puis les FONCTIONS de la cible contre MES derivations : **9 CAP et 18
bascules (k = 2 et k = 4) concordent a 1e-9 relatif.** Aucune constante
n'est recopiee dans le code : elles sont derivees, et elles tombent
juste.

**(d) LA JAMBE DE MUTATION -- ce que le banc ne portait pas.** L'egalite
au bit est NECESSAIRE, elle n'est pas SUFFISANTE : un controle qui ne
mord sur aucune faute est un controle vide. J'ai donc mute la
transcription et exige la morsure. Mutations DIFFERENTES de celles du
banc (qui joue NPASSES=2, k incoherent, NGRID=47, exposant corrompu) :

```
    RK4, le demi-pas oublie dans k2       la lignee MORD (indice 2060 vs 2044)
    test d'explosion, |x1+x2| au lieu
      de max(|x1|,|x2|)                   la lignee MORD (2091 vs 2044)
    non-linearite, g a un millieme pres   la lignee MORD (2042 vs 2044)
    NDENSE 96 -> 95                       le controle positif MORD (6.10e-07)
    NGRID 48 -> 49                        le controle positif MORD (5.66e-07)
    LO0 0.05 -> 0.5                       le controle positif MORD (5.58e-07)
    MAX_ELARG 8 -> 1, EXERCE d'abord      k passe de 4 a 1, ECHEC_HAUT
```

**Les sept mordent.** Deux remarques qui comptent :

  - **la resolution du controle de lignee est mesuree** : une mutation a
    1e-9 sur le pas ne deplace PAS l'indice (2044 inchange). Le controle
    separe les fautes de FORME, pas les derniers bits. **Ce n'est pas un
    defaut, c'est la portee du controle, et elle se consigne.**
  - **MAX_ELARG ne s'eprouve pas sur une recherche qui n'elargit pas.**
    Mute sur la recherche nominale, il ne change rien -- non parce que le
    controle est aveugle, mais parce que la mutation est INERTE. Il faut
    d'abord placer l'encadrement de depart SOUS le seuil (LO0, HI0 =
    0.001, 0.01 : k = 4), et alors la mutation mord. **Une mutation
    inerte ne vaut pas un controle aveugle, et la difference se joue,
    elle ne se plaide pas.**

**(e) LA BARRE, POINT PAR POINT.** C-2 (G-seuil atteignable, definition
conjointe implementee, B4d mord), C-6 (39 et 90 DERIVES, et la forme
`comptes + sautes == attendus` lue dans les journaux), C-8 (l'ajustement
II ne rend meme pas alpha : il ne peut pas l'ajuster ; et **D-alpha-5 se
montre** -- a alpha impose faux, A passe de 50 a 40.972, l'erreur est
bien absorbee par A), C-9 (aucune moyenne d'alpha), C-7 (section (d)) :
**tous passent.**

## 2. LES CINQ DEFAUTS, AVEC LEUR CORRECTIF EN FORME EXECUTABLE

### D-b-1 -- MENTION D'OUTILLAGE, DIX OCCURRENCES (C-12)

Le code la porte une fois, les cinq journaux neuf fois par un chemin
absolu qui fuit dans un avertissement.

```
    banc_qualification_machine1_v1.py l.6 : la ligne porte, entre
    parentheses apres "Redaction MACHINE 1", le nom de l'outil. Retirer
    la parenthese et ce qu'elle contient ; la ligne se lit alors
      "Version 1. Redaction MACHINE 1 -- la main est dans le nom (N-65)."
    (je ne recopie pas le mot ici : cette note se depose.)

    l.306-307, la cause de la fuite dans les journaux :
      def date_utc():
          return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    ->
      def date_utc():
          return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
```

`utcnow()` est deprecie : l'avertissement imprime le chemin absolu du
fichier, et le chemin porte le nom de l'outil. **Supprimer
l'avertissement supprime la fuite** -- il n'y a rien a filtrer, rien a
masquer. C'est la bonne forme du correctif : on retire la CAUSE.

### D-b-2 -- AUCUN JOURNAL NE DIT CE QU'IL NE JOUE PAS (C-11)

Les cinq journaux livres n'ont pas la section. Le code n'en emet aucune
(zero occurrence de "NE JOUE PAS" dans les 2303 lignes). La note, elle,
a sa section 6 -- mais **la section se coupe au journal, pas a la note**.

```
    Avant l'ecriture de journal_<mode>.txt, emettre :
      JRN("NE-JOUE-PAS", "lectures NON LUES : %s" % lectures_non_lues)
      JRN("NE-JOUE-PAS", "gardes sans morsure demontree au banc : %s" % gardes_nues)
      JRN("NE-JOUE-PAS", "runs du gel non joues : %s" % runs_sautes)
    les trois listes ENUMEREES par la machine, jamais ecrites a la main.
```

### D-b-3 -- DIX GARDES SUR SEIZE N'ONT AUCUNE MORSURE DEMONTREE (C-1)

C'est le seul point qui bloque. Le perimetre est enumere par la machine
depuis le texte des DEUX gels : **seize gardes**. Le temoin de morsure
n'est pas le nom de la garde (le banc nomme ses scenarios, pas ses
gardes) mais le SCENARIO, rattache par le symbole qui l'implemente, et
son verdict MORD relu au journal.

```
    FORCEES, six :   W-transcription (B3a, B3b, B3c)   W-mirage (B2)
                     W-comptes (B5)   G-lignee (B3d)   G-seuil (B4d)
                     G-s (B4e)
    SANS MORSURE, dix :
      G-dt        trajectoire_plan(dt2/2) : EXERCEE a chaque scenario B4,
      G-k         trajectoire_plan(K_GARDE) : EXERCEE,     jamais forcees
      G-w2        lire_alpha : EXERCEE,                    jamais forcee
      G-fen       EXERCEE, mais les synthetiques atteignent TOUJOURS CAP
      G-comptes   le compte d'alpha (== 90) n'est jamais force
      W-pas       T2_ok = {"W_pas": "PASSE", ...} injecte EN DUR
      W-plancher  idem
      W-bascule   idem
      W-croissance branche 2 du temoin, jamais atteinte
      W-integrales aucune lecture (LD-9) : la garde n'est pas jouee
```

Et la couverture des BRANCHES, enumeree depuis la source des deux
cascades, dit la meme chose autrement : **temoin, branches 2, 3bis et
4bis jamais atteintes ; alpha, branche 2 jamais atteinte.**

**CORRECTIF -- dix scenarios, tous sur le patron deja ecrit :**

```
    W-pas / W-plancher / W-bascule :
      T2_mord = {"points": {"x": {"W_pas": "MORD", "W_plancher": "PASSE",
                 "W_bascule": "PASSE", "conversion_ok": True, "tol_ordre": 0.1}}}
      cascade_temoin({"T1": {"A": L2, "B": L2}, "T1b": T1b_ok,
                      "T2": T2_mord, "T3b": {}})
      ASSERTE : "NON CONCLUANT D'INTEGRATEUR", branche 4. Trois fois, une
      par garde (la branche 4 nomme les trois : chacune doit la declencher
      SEULE, sinon deux d'entre elles restent muettes derriere la premiere).

    W-croissance :
      un FlotSynthetique dont |D| ne franchit pas caps[0] avant T_0, puis
      lire_T1 -> W_croissance == "MORD"
      ASSERTE : "NON CONCLUANT DE TEMOIN", branche 2.

    branche 3bis (deux formes, deux scenarios) :
      (i)  T1 hors des deux fenetres (fenetre_q et fenetre_1 faux)
      (ii) T1b["regime"] = "NI_L_UNE_NI_L_AUTRE"
      ASSERTE : "NON CONCLUANT DE REGIME", branche 3bis.

    branche 4bis :
      un point de T2 avec tol_ordre > PLAFOND_ORDRE, le reste a PASSE
      ASSERTE : "NON CONCLUANT DE RESOLUTION", branche 4bis.

    G-dt et G-k :
      SynthAlpha muni d'une dependance au PAS (alpha(dt2) != alpha(dt2/2))
      puis au K de bascule, sur le patron de dep_s deja ecrit
      ASSERTE : "NON CONCLUANT DE RESOLUTION", branche 2 d'alpha. Deux
      scenarios, un par garde.

    G-w2 :
      SynthAlpha(dep_w2=0.5), patron exact de dep_s
      ASSERTE : "REFUTE", branche 4, et "G-w2" dans le motif (aujourd'hui
      seule G-s y mene, et le motif nomme les deux).

    G-fen :
      un synthetique qui n'atteint JAMAIS CAP_p avant T_MAX
      ASSERTE : "NON CONCLUANT DE FENETRE", branche 3, avec le COMPTE
      inchange (G-fen compte le point, elle ne le saute pas).

    G-comptes :
      compteur volontairement decale : 89 + 0 != sum(compte_attendu_alpha())
      ASSERTE : "MANCHE NON JOUEE", G-comptes MORD.
```

**W-integrales ne peut PAS recevoir de scenario avant l'erratum du gel**
(fait 1, section 5) : la garde n'est pas jouable au compte gele. C'est la
seule des seize qui reste sans morsure apres correction, et **elle se
declare telle quelle** dans la section D-b-2.

### D-b-4 -- L'ETAT TANGENT N'EST PAS REFUSE, IL EST SEULEMENT EVITE (C-3)

Les deux etats declares sont justes et verifies en exact au selftest.
Mais le gel dit l'etat tangent INTERDIT (4.3), et le code se contente de
ne pas le proposer : construit a la main, il passe. J'ai joue le piege :

```
    etat (x, x', D, D') = (1, 0, 0, 1) au rebroussement, integre 20 unites
    de temps par le pas de la cible :
      D / x' = -0.500000000  (dispersion 4.3e-11)   |D| max = 0.612
    -> D est EXACTEMENT proportionnel a x' : la solution TANGENTE, unique
       solution bornee de Hill. |D| ne franchit aucun plafond : le temoin
       "PASSERAIT" par construction.
    Et H1_0 = 0.0 : FlotDS.prolonger l.723 divise par abs(self.H1_0)
    -> ZeroDivisionError. Un plantage n'est pas un refus declare.
```

**CORRECTIF, dans `FlotDS.__init__`, apres le calcul de H1_0 et N_0 :**

```
    if self.H1_0 == 0.0 or self.N_0 == 0.0:
        raise SystemExit(
            "ETAT INTERDIT (gel temoin 4.3) : H1_0 = %r, N_0 = %r -- "
            "sur l'etat tangent (D proportionnel a x') toute derive "
            "relative est absurde et le temoin passerait par construction"
            % (self.H1_0, self.N_0))
```

et un scenario de banc qui l'ASSERTE (la garde doit mordre, comme les
autres). **Le test discriminant est H1_0 = 0, pas le triplet d'entree :
il attrape l'etat tangent sans avoir a le reconnaitre.**

### D-b-5 -- (le meme que D-b-3 vu par les branches) : voir ci-dessus.

## 3. CE QUE CETTE PIECE FAIT BIEN, ET QUI N'ETAIT PAS DU

Trois choses qu'aucune regle n'exigeait :

  - **le controle positif de transcription est joue sur NEUF thetas au
    bit, motifs compris**, et le banc en fabrique quatre fausses
    transcriptions pour le mettre a l'epreuve. C'est exactement la
    methode que l'ordre demandait, poussee plus loin que l'ordre ;
  - **les deux globales du moteur sont re-liees a l'appel, jamais dans le
    fichier** (PB-1 tenu a la lettre), et T_MAX re-lie rend ACCESSIBLE
    l'indice d'explosion que `integrer()` ne rendait pas -- c'est ce qui
    permet a G-lignee de comparer autre chose qu'un booleen ;
  - **les quatorze lectures declarees LD-1..LD-14 sont etiquetees dans le
    code**. Le gel dit "derive" sans donner la forme en huit endroits ;
    chaque forme est ecrite et portee. **C'est la bonne facon de traiter
    un gel incomplet : declarer, pas combler en silence.** Je les
    certifie toutes les quatorze, avec la reserve de la section 5 sur
    LD-9.

## 4. LES DECLARATIONS QUE JE CONTRESIGNE

  - **LD-2** ("R -> 1" lu SANS tol_R) : correcte, et c'est la lecture que
    D-t-4 impose. Un t_c qui sature disperse, et une tolerance tiree de
    sa dispersion rendrait R = 1 et R = q compatibles.
  - **LD-4** (tol_ordre = log2((1+b)/(1+b/2)), b = (alpha+5)/M) : derivee,
    plafonnee a eta x 1, et sous le plafond aux trois degres (0.2003,
    0.1848, 0.1720). Sans elle, p_obs = 3.905 mordrait a la premiere
    tolerance venue -- et ce serait un FAUX ECHEC.
  - **LD-5** (le temoin consigne e/ln 10, alpha relit la porte) : c'est la
    seule lecture possible, tol_alpha n'existant pas avant la manche
    alpha. La porte relue du cote alpha est le bon endroit.

## 5. LES TROIS FAITS -- VERIFIES, ET DEUX SONT DES DEFAUTS DE GEL

**JE VERSE MA PART EN PREMIER : les deux gels sont de ma main.** Machine
1 a verse la sienne (elle les a certifies) ; la faute d'ecriture est
mienne, et elle est du meme genre que celle du 78.7 : une forme qui se
lit bien et ne se joue pas.

**FAIT 1 -- W-integrales ne peut pas etre jouee au compte gele. CONFIRME
par enumeration du gel.** La section 8 du gel temoin EXIGE la lecture sur
dt contre dt/2 (chute d'un facteur 16). La section 9 compte **T-1 = 2
flots** (un par etat, au pas dt) et **T-3a = 0** ("inclus dans les flots
de T-1"), et le mot "dt/2" n'apparait NULLE PART dans le compte. Les deux
sections sont incompatibles : **a 39 runs geles, le flot a dt/2 n'existe
pas.** L'instrument fait ce qu'il pouvait faire de mieux : il joue 39,
consigne les derives a dt (A : H1 1.0e-08, N 5.7e-10 ; B : 2.7e-07,
1.6e-08) et ECRIT "tolerance NON LUE (LD-9)" a chaque ligne.
**Arbitrage** : erratum de gel + 41 runs (deux flots de plus), ou
W-integrales declaree non jouee et le bonus T-3 retire de la cascade.
Je recommande **41 runs** : deux flots contre un doute qui, sinon, reste
au registre pour toujours.

**FAIT 2 -- aux trois points, rien n'explose. VERIFIE PAR MOI, avec le
moteur DEPOSE appele tel quel**, hors de l'instrument :

```
    p=5 w2=2.27  c=1.05 non   c=1.20 non
    p=5 w2=2.80  c=1.05 non   c=1.20 non
    p=7 w2=2.80  c=1.05 non   c=1.20 non
    et le controle n'est pas vide : a p = 4, 1.20 s* EXPLOSE aux trois w2.
```

La manche alpha telle que gelee rend donc **NON CONCLUANT DE FENETRE,
degre 4 seul exploitable** -- ce que la repetition de machine 1 rend
exactement (branche 3, "degres exploitables [4]"). Les amplitudes 4.3
sont gelees : **un gel v3 est une decision d'operateur, pas d'instrument,
et je ne la prends pas.**

**FAIT 3 -- P-A est PARTIEL par construction des que l'instrument est bon.
VERIFIE en exact.** La tolerance de P-A (10.3) se derive de la dispersion
de A sur la grille (dt_2, dt_2/2) x (k = 2, 4) : elle mesure
l'INSTRUMENT. L'ecart mesure, lui, vient du MODELE : le gel lui-meme
(D-alpha-9) borne le terme neglige a delta/((alpha+2)(alpha+3)), soit
**1/2000 a p = 4**, et sur g A^(p-2) cela fait **(p-2) fois** cette
borne, **1.0e-03**. Or :

```
    tol_lnA de la repetition   1.98e-06     (la dispersion de l'instrument)
    ecart mesure               2.2e-04      (entre les deux, comme il doit)
    borne du terme neglige     1.0e-03      (D-alpha-9, exact)
```

**Une tolerance cent fois plus petite que le biais que le gel lui-meme
declare ne peut pas etre franchie.** P-A rend PARTIEL quoi qu'il arrive,
et un PARTIEL lu ainsi ne dit rien de la constante.

**CORRECTIF, en forme executable, pour l'arbitrage (gel v3) :**

```
    tol_lnA(p) = max( dispersion de A sur la grille (dt_2, dt_2/2) x (k=2,4),
                      (p - 2) x delta / ((alpha_p + 2)(alpha_p + 3)) )
    et le rapport tol_lnA / [(p-2) delta/((a+2)(a+3))] se CONSIGNE.
```

Le second terme est **derive du gel, pas invente** : il est ecrit en
toutes lettres en D-alpha-9, et il n'introduit **aucun nombre pur
nouveau**. Le plafond de D-alpha-3 ne s'y applique pas : il vise les
tolerances tirees de la dispersion de la grandeur TESTEE, et celle-ci est
tiree du MODELE.

## 6. CE QUE CE DEPOT NE JOUE PAS

Il ne rejoue pas les 39 + 90 runs reels et **ne mesure rien (N-62)**. Il
ne tranche aucun des trois faits : ce sont des arbitrages d'operateur, et
deux appellent un erratum ou un gel v3. Il ne corrige pas le code de la
cible : les correctifs sont donnes en forme executable, la plume reste a
machine 1. Il ne verifie pas la fidelite de la transcription de
Damour-Smilga a l'article (elle ne repose que sur moi, le gel le declare,
et la double transcription reste due). Il ne relit pas les series de
sortie point par point : il verifie que 5.7 les EXIGE et que le code les
ecrit, pas leur contenu.

## 7. CE QUI EST ATTENDU DE MACHINE 1, ET DANS QUEL ORDRE

```
    1. v2 de l'instrument : D-b-1, D-b-2, D-b-3 (dix scenarios), D-b-4.
       Aucun autre changement -- une v2 qui touche a autre chose se
       re-certifie en entier.
    2. ma certification de la v2 (courte : je rejoue mes 53 controles et
       les dix scenarios neufs).
    3. le pre-vol OPPOSABLE, a moteur factice, sur la v2 certifiee.
    4. le temoin ; alpha SI ET SEULEMENT SI le reglage est QUALIFIE.
    Les trois faits partent en parallele a l'operateur : ils ne bloquent
    ni la v2 ni le pre-vol, mais le FAIT 3 doit etre tranche AVANT le run
    alpha, et le FAIT 1 avant le run du temoin.
```

## 8. PIECES (convention B, NFC + LF, sha256 tronque a 16)

```
    certif_instrument_bancs_machine2_v1.py       (m2, cet audit)
    certif_instrument_bancs_machine2_v1.log      (53 controles)
    m2_selftest.log / m2_banc.log                (72/72 et 21/21 rejoues chez moi)
    banc_qualification_machine1_v1.py   3a932eabfaaf4307  116438  (cible)
    POUR_MACHINE1_ordre_instrument_bancs_v1.md 6e176705468a4834  12045
    gels/alpha_pre_enregistrement_v2.md          35a70834b2a34514  21113
    gels/temoin_negatif_pre_enregistrement_v5.md 0905a9b78ba40349  34961
    scripts/m9_replication_v1.py                 c8ed357b120352c4  36325 (brut)
    runs/m12_results.json                        fa109da92e582520 130856 (brut)
```

-- FIN note_machine2_certification_instrument_bancs_v1 --
