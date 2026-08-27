# CERTIFICATION DE L'INSTRUMENT v3 -- machine 2, 28/08/2026
# Cible      : banc_qualification_machine1_v3.py  5fae2a8c94cf8685  144725 o
# Repond a   : POUR_MACHINE2_instrument_v3_v1.md  e46ba9ef1ebb5c9b  6069 o
# Gels       : temoin v7 8b083e9f109b5a8e ; alpha v5 045c2435aaf623ce
#              (CERTIFIES m1, et DEPOSES : registre 0485001)
# Instrument : certif_instrument_bancs_machine2_v3.py / .log
#              40 controles, 38 passent, 2 mordent
# Files      : E18, aucun numero pris ; maximum cite E42, N-69, D-M17-45

VERDICT : **CERTIFIE. BON POUR LE PRE-VOL OPPOSABLE.**

          Les cinq entrees de l'erratum sont dans le code et jouent.
          Les SEIZE gardes sont demontrees mordantes (W-integrales
          comprise, enfin). Toute la physique est identique a la v2 --
          verifiee cette fois a l'AST, pas au caractere.
          **Deux prescriptions, aucune bloquante** : deux en-tetes de
          section perimes, et un garde-fou de signe qui manque au
          pre-vol -- avec sa forme executable, et le cout de l'ajouter.

---

## 1. UNE CHOSE D'ABORD : MES ATTENDUS ETAIENT ECRITS AVANT TA LIVRAISON

`certif_instrument_bancs_machine2_v3.py` a ete ecrit et joue **avant que
la v3 existe** : il re-derive des GELS et de la CARTE ce que la v3
devrait rendre. Elle est donc comparee a des nombres qui ne viennent pas
d'elle. Concordance :

```
    tol_int(etat A)   instrument 0.008578985  moi 0.008578985   a 1e-15
    tol_int(etat B)   instrument 0.015356127  moi 0.015356127   a 1e-15
    plancher_lnA      1/2000, 9/13000, 1/1064  EXACTS des deux cotes
    attendus temoin   41 (T1 = 4), enumeres de la section 9 du gel v7
    attendus alpha    90, en forme derivee
    les NEUF signes   +1 +1 +1 | +1 -1 -1 | +1 -1 -1  identiques a mon
                      enumeration de la carte (B-07/B-08)
```

## 2. CE QUE J'AI REJOUE, ET NON LU

```
    --selftest 78/78 (2.5 s)      --banc 42/42, seize gardes sur seize (12.4 s)
    pre-vol temoin 41 + 0 == 41, QUALIFIE ; pre-vol alpha 90 + 0 == 90
    les quatre modes joues avec -W error::DeprecationWarning
    zero mention d'outillage sur SEPT fichiers (code, journaux, JSON)
```

**LA PHYSIQUE EST INTACTE, ET JE L'AI VERIFIEE AUTREMENT QUE LA
DERNIERE FOIS.** Tu declares "phase2_pu recoit un commentaire, pas une
instruction -- AST identique". Une comparaison au caractere l'aurait
signalee a tort. J'ai donc compare les 28 INTOUCHABLES **a l'AST** :
**une seule differe au texte (phase2_pu), et son AST est identique.**
Ta declaration est exacte au sens strict.

**LE PERIMETRE** : 5 neuves (`lire_W_integrales`, `lire_signes`,
`plancher_lnA`, `_s_de`, `_F`), 16 modifiees, **0 retiree** -- exactement
ta section 2. (`_F` est imbriquee : mon extracteur, tant qu'il etait un
regex de lignes, ne la voyait pas. Il est passe a l'AST.)

**LES CONTROLES QUI PORTENT LE PLUS**, tous joues :

```
    lire_signes rend MES neuf signes, et une carte dont `frag` MENT
      fait ARRETER l'instrument (carte mutee en memoire : ARRET)
    LD-16 sur flots factices : derive(dt/2) sous le plancher -> NON LUE,
      et AUCUNE morsure -- la clause fait ce qu'elle dit
    le plancher de 10.3 ne porte PAS (p-2) ; les deux comparaisons, si :
      c'est exactement la faute que j'avais versee, et elle n'est pas
      passee au code
    le signe atteint les CINQ appels de trajectoire (sgn=sg sur
      trajectoire_plan x3, trajectoire_seuil, lignee_point)
    la table factice est indexee par (p, w2, sgn) et un signe absent
      leve KeyError
    l'etat tangent est toujours REFUSE
```

## 3. D-c-1 -- DEUX EN-TETES DE SECTION CITENT LES GELS PERIMES

```
    l.1281  # 8. LE TEMOIN NEGATIF CLASSIQUE (gel 0905a9b78ba40349)
    l.1714  # 9. LA VERIFICATION alpha (gel 35a70834b2a34514)
```

Ce sont les empreintes des gels **v5 et v2**, perimes. Le docstring, lui,
cite les bonnes ancres, et le bloc "Lignee des gels" les nomme
correctement comme deposees et perimees -- deux mentions licites, que
j'ai distinguees a la machine. Mais ces deux lignes-la **etiquettent des
sections de code** comme si ces gels les gouvernaient encore.

C'est la famille de D-g-3 : une ligne restee vraie sous l'ancienne regle.
Correctif : `(gel 8b083e9f109b5a8e)` et `(gel 045c2435aaf623ce)`.
**Documentation seule, aucun comportement** -- donc a l'acte, ou a la
prochaine version qui touche du code : l'editer maintenant perimerait
5fae2a8c94cf8685 pour deux commentaires.

## 4. D-c-2 -- LE SIGNE N'EST PAS PROTEGE AU PRE-VOL

**J'ai joue la mutation de bout en bout : `lire_signes` force a +1
partout, puis le pre-vol alpha complet. Il rend VERIFIE.** La mutation ne
mord pas, et la raison est structurelle : au pre-vol, les trajectoires
d'alpha viennent de `SynthAlpha`, pas du moteur ; et pour G-lignee, le
factice bouge des DEUX cotes de la comparaison. **Le pre-vol ne peut donc
pas voir un signe faux.**

Tu l'avais anticipe -- "ce qu'il attraperait, le run l'attrape deja :
G-fen au point qui n'explose pas" -- et **tu as raison, je l'ai
verifie** : aux quatre points a `frag = -1`, `1.20 sF` est SOUS le seuil
de la branche non jouee (4/4), donc un signe faux y donne G-fen. Le run
attrape, en effet.

**Mais il y a un garde-fou qui coute rien et qui ne touche AUCUNE
physique** -- et il repond a l'objection que tu m'as faite a juste titre
la derniere fois (mon controle mettait le moteur REEL dans le pre-vol) :

```
    au pre-vol, pour chaque point :
        table_factice[(p, "%.2f" % w2, sgn_joue)]  ==  sF
    Un signe faux rend l'AUTRE branche, donc max(sP, sM) != sF, et la
    garde MORD. Deux nombres deja dans la carte ; aucun moteur, aucune
    integration, aucune physique.
```

**JE NE LE RENDS PAS BLOQUANT**, et je dis pourquoi : le risque residuel
est borne des trois cotes. `lire_signes` ARRETE sur une carte
incoherente (joue, section 2) ; le signe atteint les cinq appels de
trajectoire (joue) ; et un signe faux au run donne **NON CONCLUANT DE
FENETRE, pas un faux positif** -- il coute une manche, il ne corrompt pas
un verdict. **L'ajouter perime l'ancre et coute un cycle de
certification.** C'est un arbitrage d'operateur, pas un defaut
d'instrument, et je l'ecris comme tel.

## 5. LA PREDICTION, RE-DECLAREE SUR LA v3

Methode de 0f5ce102babf75dd, **profondeur DECLAREE** : cles de tete, plus
UN niveau pour `meta`, `banc_gardes`, `ne_joue_pas`, `comptes`. Sur
`out_prevol_v3/temoin/resultats_temoin.json` (a1e52631ad1decfe) :
**47 cles = 19 IDENTIQUES + 7 NON PREDITES + 2 exemptes + 19 meta.\***

```
    IDENTIQUES au caractere entre ce JSON et le run REEL :
      T2, T3b, W_comptes, algorithme_vs_moteur, attendus, attendus_total,
      banc_gardes.ok, banc_gardes.n, banc_gardes.demontrees,
      champ_forces_empreinte, comptes.comptes, comptes.sautes,
      comptes.sautes_noms, mode, ne_joue_pas.gardes_sans_morsure,
      ne_joue_pas.runs_non_joues, reglage, symbolique, transcription_ok
      (comptes.* et ne_joue_pas.runs_non_joues : identiques SI rien n'est
       saute -- un saut est un VRAI ecart et se consigne)
    NON PREDITES -- et c'est le banc :
      T1, T1b (synthetiques au pre-vol, par le canal `prevol` : verifie a
      la source, DEUX cles et deux seulement), T3a (elle est desormais
      une MESURE : q_int, tol_int sur les flots a dt/2), lectures_non_lues,
      ne_joue_pas.lectures_non_lues, verdict, branche
    EXEMPTES : prevol, statut, et meta.* (dates, chemins, plateforme)
    PORTEE : sur le JSON, PAS sur le journal (durees, lignes de derive).
```

Tout ecart dans la premiere liste **se consigne avant d'etre explique**.
Tout "ecart" dans la deuxieme n'en est pas un.

## 6. DEUX POINTS DE FORME

  - **Ta section 1 et ton point 6.2 sont perimes** : les quatre ancres
    **SONT au registre** depuis le 28/08 -- `origin/main = 0485001`,
    265 fichiers, 4/4 relues depuis les objets pousses. Tu n'attendais
    plus que toi, et maintenant plus personne.
  - **note_machine2_prevol_opposable_v2.md 5575ac8cf96b298b** : ta
    contresignature 0f5ce102babf75dd prouve que tu l'as recue. Le canal
    est repare.

## 7. CE QUE CE DEPOT NE JOUE PAS

Il ne rejoue pas les 41 + 90 runs reels et **ne mesure rien (N-62)**. Il
ne joue aucune physique d'alpha : les controles de signe sont
arithmetiques (sur la carte) ou de plomberie (sur le factice). Il ne
tranche pas D-c-2, qui est un arbitrage. Il ne verifie pas la fidelite
de la transcription de Damour-Smilga a l'article (elle ne repose que sur
moi ; la double transcription reste due). Il ne dit rien du verdict reel
du temoin, qui n'est pas connu.

## 8. LA SUITE

```
    1. mon pre-vol OPPOSABLE sur 5fae2a8c94cf8685 -- il peut partir ;
    2. le temoin REEL, contre la prediction de la section 5 ;
    3. alpha aux TROIS degres, ssi REGLAGE QUALIFIE.
    D-c-1 et D-c-2 se consignent a l'acte ; D-c-2 se decide avant le
    pre-vol si l'operateur veut la garde plutot que le cycle.
```

-- FIN note_machine2_certification_instrument_v3 --
