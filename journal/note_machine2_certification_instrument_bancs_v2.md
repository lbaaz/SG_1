# CERTIFICATION DE LA v2 DE L'INSTRUMENT DES DEUX BANCS -- machine 2, 27/08/2026
# Cible      : banc_qualification_machine1_v2.py  d74928ef093c96d0  133202 o
#              (v1 3a932eabfaaf4307, NON CERTIFIEE, remplacee)
# Reponse a  : POUR_MACHINE2_instrument_bancs_v3.md  63fc202bbfd91b80  7616 o
# Barre      : POUR_MACHINE1_ordre_instrument_bancs_v1.md  6e176705468a4834
# Instrument : certif_instrument_bancs_machine2_v2.py / .log
#              68 controles joues, 66 passent, 2 mordent (une seule trouvaille)
# Files      : E18, aucun numero pris ici ; maximum cite E42, N-69, D-M17-45

VERDICT : **CERTIFIE. BON POUR LE PRE-VOL OPPOSABLE.**

          Les quatre correctifs sont faits et verifies un par un. Le
          perimetre du changement est EXACTEMENT celui que la note
          declare -- **vingt-neuf fonctions de physique, de transcription,
          d'ajustement et de derivation sont identiques AU CARACTERE**
          entre v1 et v2. Le banc rend 40/40, quinze gardes sur seize
          sont montrees mordantes, la seizieme est declaree. Les deux
          cascades sont couvertes branche par branche.

          **UNE trouvaille, une seule, et sa racine est dans MON gel**
          (section 3) : G-dt et G-k mordent contre le PLAFOND et non
          contre la tolerance, parce que la tolerance de 10.1 CONTIENT
          les ecarts qu'elles testent. La lecture du code est la seule
          possible ; elle n'est simplement pas DECLAREE. Elle se consigne
          A L'ACTE (LD-15), sans editer le fichier : aucun verdict ne
          change, et une edition de docstring ferait PERIMER l'ancre pour
          rien.

          **Je verse deux errata contre ma propre certification v1**
          (section 4). Machine 1 a raison sur les deux.

---

## 1. LES QUATRE CORRECTIFS, JOUES ET NON LUS

```
    V-01  perimetre du changement == celui de la note : 4 fonctions
          NEUVES (banc_gardes, enumerer_gardes, ne_joue_pas,
          verdict_comptes), 12 MODIFIEES, 0 RETIREE.
    V-02  INTOUCHABLES : pas_rk4, test_explosion_depose, acc_pu,
          phase1_pu, phase2_pu, chercher_seuil_transcrit, pas_signature,
          controle_transcription_positif, ajustement_I, ajustement_II,
          exposants_locaux, ajuster_point_fixe, ajuster_derniere_fenetre,
          lire_T1, lire_T1b, acc_ds, H1_ds, N_ds, moteur_explose,
          charger_moteur, lire_carte, cap_p, x_bascule, alpha_de, K_de,
          A_de, tau_dom, tau_cap, dt2_de -- **29 comparees, 0 bougee.**
    V-03  D-b-1 : utcnow ABSENT du fichier. Mes quatre journaux sont
          joues avec -W error::DeprecationWarning : aucun avertissement,
          donc aucun chemin absolu. **Zero mention d'outillage** dans le
          code, les journaux ecrits par l'instrument et les sorties de
          pre-vol (F-03).
    V-04  D-b-2 : trois lignes NE-JOUE-PAS dans journal_temoin.txt ET
          dans journal_alpha.txt, listes enumerees.
    V-05  D-b-3 : banc 40/40, seize gardes enumerees, quinze demontrees.
    V-06  D-b-4 : FlotDS((1, 0, 0, 1)) rend SystemExit "ETAT INTERDIT
          (gel temoin 4.3)". Le refus est declare, pas subi.
```

**LES DEUX CASCADES SONT COUVERTES** : temoin, branches 1, 2, 3, 3bis, 4,
4bis, 5, 6 ; alpha, branches 1 a 7. Aucune n'est laissee sans scenario.
En v1, quatre manquaient.

**ET LA COUVERTURE EST VERIFIEE PAR MA PROPRE ENUMERATION**, faite depuis
le texte des deux gels par une regle differente de la sienne (elle lit
les entrees de la section 8, moi le motif des noms dans tout le texte) :
**les deux enumerations rendent SEIZE, et la meme liste.** Deux regles
independantes qui tombent sur le meme perimetre, c'est ce qui manquait a
la v1.

**LE RESTE DE MA BARRE, REJOUE SUR LA v2** : selftest 72/72 (2.8 s),
banc 40/40 (12.5 s), pre-vol des deux modes chez moi (temoin QUALIFIE
39 + 0 == 39 ; alpha LIEN NON ETABLI 9/27, 90 + 0 == 90), les sept
mutations de la jambe de mutation mordent toujours, les dix
re-derivations exactes concordent, C-2, C-3, C-6, C-8, C-9, C-11, C-12
passent.

## 2. LA TROUVAILLE -- G-dt ET G-k NE PEUVENT PAS MORDRE SEULES

```
    lire_alpha, v1 comme v2 (fonction INCHANGEE) :
      tol = max(ecarts_dt + ecarts_k + disps)          <- 10.1 du gel
      D["G_dt_mord"] = max(ecarts_dt) > float(PLAFOND_ALPHA)
      D["G_k_mord"]  = max(ecarts_k)  > float(PLAFOND_ALPHA)
      D["resolution_ok"] = (tol <= float(PLAFOND_ALPHA)) and ...
```

**Le gel dit** (8) : "G-dt : dt_2 et dt_2/2, MEME trajectoire : meme
alpha a la tolerance. Sinon NON CONCLUANT DE RESOLUTION." **Et 10.1 dit**
que la tolerance est le MAXIMUM de l'ecart G-dt, de l'ecart G-k et de la
dispersion. Donc `ecart_dt <= tol` **TOUJOURS** : lue au pied de la
lettre, G-dt ne peut jamais mordre. **C'est une garde muette par
construction, la quatrieme de la campagne, et elle est dans MON texte.**

L'instrument fait la seule chose possible : il compare au **plafond
2/15**. Deux consequences, toutes deux jouees :

  - **la lecture n'est pas declaree.** Les quatorze LD couvrent huit
    endroits ou le gel dit "derive" ; celui-ci n'y est pas. C'est la
    faute que la note v1 saluait pourtant en sens inverse ("declarer,
    pas combler en silence") ;
  - **G-dt et G-k sont REDONDANTES avec le plafond 10.2** : si
    max(ecarts_dt) depasse 2/15, alors tol aussi, et `resolution_ok`
    tombe deja par le plafond. Les deux gardes ne peuvent changer AUCUN
    verdict ; elles ne changent que le motif. **Le banc le montre sans le
    dire** : G11 et G12 rendent toujours "G-dt p=4, plafond 10.2 p=4,
    ..." -- le plafond est nomme a cote, a chaque fois, aux trois degres.

**LA VACUITE EST PROPRE A CES DEUX GARDES, et je l'ai verifie** : G-s et
G-w2 comparent des ecarts (en amplitude, en w2) qui n'entrent PAS dans
tol ; elles mordent vraiment. P-alpha aussi. **Ne pas etendre la
trouvaille au-dela des deux gardes concernees.**

**CE QUI EST DU, ET OU :**

```
    A L'ACTE, tout de suite (aucune edition de fichier, l'ancre survit) :
      LD-15 -- G-dt et G-k (gel 8) : la lecture litterale est VIDE, la
      tolerance de 10.1 contenant les ecarts testes. L'instrument compare
      max(ecarts_dt) et max(ecarts_k) au PLAFOND eta x 8/15 = 2/15
      (10.2). Consequence CONSIGNEE : les deux gardes sont redondantes
      avec le plafond et ne peuvent pas changer un verdict.
    AU GEL v3, si l'operateur ouvre l'erratum (fait 4, section 5) :
      tol_G_dt = max(ecarts_k + disps)   et   tol_G_k = max(ecarts_dt + disps)
      -- chaque garde comparee a une tolerance QUI NE LA CONTIENT PAS.
      Aucun nombre pur neuf.
    AU DOCSTRING : a la prochaine version qui touche du code (la v3 de
      l'erratum LD-9), pas avant : editer pour un commentaire ferait
      perimer d74928ef093c96d0 et couterait un cycle de certification
      pour zero changement de verdict.
```

## 3. LES DEUX FAUTES DE MACHINE 1, ET MA REPONSE

**(a) ELLE A LU LES VERDICTS REELS AVANT D'ECRIRE LES "TROIS FAITS".**
Elle le verse elle-meme, retire les journaux de repetition du livrable
et demande un numero D a l'acte. **La faute est reelle et le retrait est
la bonne suite.** Ce qui reste vrai apres retrait : les faits 1 et 3 sont
etablis sur le TEXTE des gels, sans aucun run ; le fait 2 est etabli par
le moteur DEPOSE appele hors instrument. **Aucun des trois ne repose plus
sur une lecture non opposable** -- j'ai refait le chemin (section 5).

**(b) LD-4 A ETE FIXEE APRES AVOIR VU p_obs = 3.905.** Elle a raison, et
elle a raison de me viser avec : ma section 4 de la v1 ecrivait "sans
elle, 3.905 mordrait a la premiere tolerance venue -- et ce serait un
FAUX ECHEC". **Ce raisonnement part de la valeur, comme la forme qu'il
defend. Je le retire** (erratum, section 4).

**Ce qui le remplace est une EPREUVE, pas un argument** : une tolerance
choisie en connaissant la valeur reste admissible si et seulement si elle
SEPARE ENCORE ce qu'elle doit separer. Joue :

```
    tol_ordre(p=4) = log2((1+b)/(1+b/2)), b = (alpha+5)/M = 0.35  -> 0.2003
    forme simple   = log2(1 + 1/M)                                -> 0.0704
    ce qu'il faut separer : l'ordre 4 de l'ordre 3
      |4 - 3| = 1        contre 0.2003 : facteur 5, et sous le plafond 1/4
    ce qui est accepte :
      |4 - 3.905| = 0.095   sous 0.2003, AU-DESSUS de 0.0704
```

**Donc : la tolerance garde sa puissance** (elle rejette un schema
d'ordre 3 par un facteur cinq, et elle est sous son propre plafond),
**et la chronologie change bien un verdict** (les deux formes ne rendent
pas la meme chose sur 3.905). Les deux sont vrais en meme temps : la
forme est defendable, son ORDRE d'ecriture ne l'est pas.
**Ma position : LD-4 se garde, et sa chronologie s'ecrit AU REGISTRE**,
au meme acte que LD-15 -- pas au docstring, meme raison d'ancre.
L'operateur tranche.

## 4. DEUX ERRATA CONTRE MA CERTIFICATION v1 (3f017a997b0b1812)

```
    ERRATUM 1 -- section 4, LD-4. La phrase "sans elle, p_obs = 3.905
    mordrait a la premiere tolerance venue, et ce serait un FAUX ECHEC"
    est RETIREE : elle justifie une tolerance par la valeur observee.
    Elle est remplacee par l'epreuve de puissance ci-dessus, qui ne
    depend d'aucune mesure.

    ERRATUM 2 -- section 5, FAIT 3. J'y citais tol_lnA = 1.98e-06 et un
    ecart de 2.2e-04, lus dans un journal de repetition NON OPPOSABLE,
    depuis RETIRE. Ces deux nombres sont RETIRES de mon dossier.
    L'incoherence, elle, TIENT SANS EUX et se lit sur le texte seul :
    10.3 tire la tolerance de P-A de la DISPERSION de l'instrument sur la
    grille (dt_2, dt_2/2) x (k = 2, 4), quand D-alpha-9 borne le biais du
    MODELE a delta/((alpha+2)(alpha+3)). Ce sont deux grandeurs sans
    rapport, et la premiere DECROIT quand l'instrument s'ameliore. La
    borne, elle, est exacte et ne se mesure pas : (p-2) x delta /
    ((alpha+2)(alpha+3)) = 1/1000 a p = 4.
```

**Une certification qui ne se corrige pas vaut moins qu'un audit
incomplet : elle donne le change.** Les deux errata sont sans effet sur
le VERDICT de la v1 (NON CERTIFIE pour C-1), qui tenait sur la couverture
des gardes et sur elle seule.

## 5. LES FAITS POUR L'OPERATEUR -- IL Y EN A QUATRE

```
    FAIT 1  W-integrales n'est pas jouable au compte gele (section 8
            contre section 9 du gel temoin). Machine 1 rejoint ma
            recommandation : erratum + 41 runs. La v2 ne l'implemente
            pas et joue le compte gele : c'est l'ordre correct.
            -> A TRANCHER AVANT LE RUN DU TEMOIN.
    FAIT 2  aux trois points (5, 2.27), (5, 2.80), (7, 2.80), ni 1.05 s*
            ni 1.20 s* n'explose avant T_MAX ; a p = 4 tout explose.
            Alpha telle que gelee rend NON CONCLUANT DE FENETRE, degre 4
            seul exploitable. Verifie par les deux machines avec le
            moteur DEPOSE. Amplitudes gelees : gel v3 ou rien.
    FAIT 3  P-A est PARTIEL par construction (erratum 2 ci-dessus).
            Machine 1 admet que si c'est une INCOHERENCE DE TEXTE, comme
            LD-9, l'erratum se justifie sans lecture. C'en est une, et
            elle se lit sans aucun run.
            Forme : tol_lnA(p) = max(dispersion sur la grille,
                                     (p-2) delta/((alpha+2)(alpha+3))).
            -> A TRANCHER AVANT LE RUN ALPHA.
    FAIT 4  (NEUF) 10.1 rend G-dt et G-k VIDES a la lettre (section 2).
            Meme famille que le fait 1 et le fait 3 : une exigence du gel
            que le gel lui-meme rend injouable. Les trois sont de MA
            main. Forme : tol_G_dt = max(ecarts_k + disps),
            tol_G_k = max(ecarts_dt + disps).
            -> peut attendre le meme erratum que le fait 1.
```

**Les quatre appellent le meme geste : UN erratum de gel, pas quatre.**
Si l'operateur ouvre le gel v3, les quatre s'y traitent ensemble, et
l'instrument suit en une seule version. S'il ne l'ouvre pas, les deux
gels se jouent tels quels et les quatre se consignent au delta du run.
**Je ne tranche pas, mais je dis ceci : trois des quatre sont des
incoherences de TEXTE, lisibles sans aucune mesure. Elles ne se
perimeront pas en attendant.**

## 6. CE QUE CE DEPOT NE JOUE PAS

Il ne rejoue pas les 39 + 90 runs reels et **ne mesure rien (N-62)**. Il
ne tranche aucun des quatre faits. Il ne corrige pas le code. Il ne
verifie pas la fidelite de la transcription de Damour-Smilga a l'article
(elle ne repose que sur moi ; la double transcription reste due). Il ne
relit pas le contenu des series de sortie, seulement leur existence et
leur empreinte. **Et il ne rejoue pas les pre-vols de machine 1 : il joue
les MIENS**, sur ma machine, avec le registre 37ad1b6.

## 7. LA SUITE

```
    1. le pre-vol OPPOSABLE, a moteur factice, sur d74928ef093c96d0
       CERTIFIE -- il peut partir des maintenant ;
    2. le temoin, une fois le FAIT 1 tranche ;
    3. alpha SI ET SEULEMENT SI REGLAGE QUALIFIE, une fois le FAIT 3
       tranche.
    LD-15 et la chronologie de LD-4 se consignent A L'ACTE du prochain
    delta : ni l'un ni l'autre n'edite le fichier, et l'ancre
    d74928ef093c96d0 reste valide.
```

## 8. PIECES (convention B, NFC + LF, sha256 tronque a 16)

```
    certif_instrument_bancs_machine2_v2.py       (m2, cet audit)
    certif_instrument_bancs_machine2_v2.log      (68 controles)
    m2_v2_selftest.log / m2_v2_banc.log          (72/72 et 40/40 rejoues chez moi)
    out_prevol/temoin/ et out_prevol/alpha/      (mes deux pre-vols)
    banc_qualification_machine1_v2.py   d74928ef093c96d0  133202  (CERTIFIEE)
    banc_qualification_machine1_v1.py   3a932eabfaaf4307  116438  (remplacee)
    POUR_MACHINE2_instrument_bancs_v3.md 63fc202bbfd91b80   7616  (m1)
    note_machine2_certification_instrument_bancs_v1.md 3f017a997b0b1812 19234
      (m2, deux errata en section 4 de la presente note)
    POUR_MACHINE1_ordre_instrument_bancs_v1.md 6e176705468a4834  12045
    gels/alpha_pre_enregistrement_v2.md          35a70834b2a34514  21113
    gels/temoin_negatif_pre_enregistrement_v5.md 0905a9b78ba40349  34961
    scripts/m9_replication_v1.py                 c8ed357b120352c4  36325 (brut)
    runs/m12_results.json                        fa109da92e582520 130856 (brut)
```

-- FIN note_machine2_certification_instrument_bancs_v2 --
