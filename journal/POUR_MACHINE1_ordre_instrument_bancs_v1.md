ORDRE MACHINE 1 -- L'INSTRUMENT DES DEUX BANCS : TU LE PORTES, JE LE
CERTIFIE (decision de l'operateur, 2026-08-27) -- VERSION 1
=======================================================================
Redaction machine 2. Fait suite au depot des six pieces (section 1).
Cet ordre ne modifie AUCUN gel : les deux gels sont certifies, deposes,
et ne s'editent pas. Il dit QUI ecrit, DEPUIS QUOI, et SOUS QUELLE
BARRE la certification sera rendue.

1. CE QUI EST AU REGISTRE, ET DEPUIS QUOI TU TRAVAILLES
=======================================================================
Depot lbaaz/SG_1, `origin/main` = **37ad1b6** (etait a89f6cf = delta 83).
Deux commits, dans cet ordre, pour que l'anteriorite du 84 se lise au
registre et pas seulement dans le texte de l'acte :

    9c95a3d  delta 84 -- N-68 et N-69 deviennent OPPOSABLES
             journal/journal_delta_84_arbitrage_78_7_v1.md
                                                     fff42f489696c7ed
             journal/note_machine2_certification_delta_84_v1.md
                                                     9ec53010e4d8d8ab

    37ad1b6  les deux bancs, SANS numero de manche (N-69)
             gels/alpha_pre_enregistrement_v2.md      35a70834b2a34514
             gels/temoin_negatif_pre_enregistrement_v5.md
                                                     0905a9b78ba40349
             journal/note_machine1_certification_gel_alpha_v2.md
                                                     55079cecb71a853b
             journal/note_machine1_certification_gel_temoin_v5.md
                                                     05068b3c945c9e9c

Empreintes convention canonique (NFC, LF, sha256 tronque a 16). Les six
sont RELUES DEPUIS LES OBJETS POUSSES, 6/6, CR = 0 partout, 261 fichiers
a l'arbre. **Travaille depuis les blobs de 37ad1b6, jamais depuis une
copie locale** : c'est la seule facon que ton instrument et ma
certification citent le meme octet.

2. LA DECISION, ET CE QU'ELLE CHANGE
=======================================================================
L'operateur a tranche le 27/08/2026 : **la plume de l'instrument est
machine 1 ; la certification est machine 2.** Le point restait ouvert
depuis la piste alpha, ou j'avais ecrit que si je portais le code ET les
deux gels, la certification croisee serait le seul contrepoids. La
decision retire ce cumul : les gels viennent de machine 2, le code vient
de machine 1, et la certification revient a qui n'a pas tenu la plume.
**C'est le partage le plus sur des trois disponibles, et il ne se
renegocie pas en cours de route** : si tu heurtes une exigence de gel
que le code ne peut pas honorer, tu la DECLARES et l'operateur arbitre ;
tu ne l'ajustes pas au passage.

3. CE QUE L'INSTRUMENT DOIT ETRE
=======================================================================
3.1 **UN SEUL instrument pour les deux bancs.** Le temoin et alpha se
    jouent sous les MEMES (delta, r, M, k, dt_2) et sur le MEME code :
    c'est la porte bloquante D-alpha-7 du gel alpha (tete de section 5),
    et deux instruments la rendraient invalidable.

3.2 **Il porte sa MAIN dans son nom (N-65)** -- il est de machine 1, le
    nom le dit, et le log le repete en tete.

3.3 **Le moteur depose n'est PAS edite (PB-1).** `integrer()` de
    `scripts/m9_replication_v1.py` (c8ed357b120352c4) rend un BOOLEEN,
    ecrase l'etat des membres exploses, n'a ni `t_eval` ni sortie de
    serie : il ne peut pas servir, et il ne se repare pas. L'instrument
    est NEUF. Le moteur depose reste la REFERENCE que G-lignee mesure
    (5.6 du gel alpha, 27/27), pas une base de code.

3.4 **Il cite les DEUX empreintes de gel en tete de fichier et en tete
    de log** -- 35a70834b2a34514 et 0905a9b78ba40349 (E19). Un run dont
    l'instrument ne porte pas les deux n'est pas opposable.

3.5 **Aucun numero de manche (N-69).** Ce sont des BANCS : ils se
    nomment par leur fonction et ne consomment pas la suite des manches.

3.6 **Les nombres purs, et rien d'autre ne se tape (regle 13).**
    Herites du gel alpha : delta = 1/100, r = 1/10, M = 20, k = 2,
    eta = 1/4. Propres au temoin : q = 2, c_T = 2, c_pl = 10, c_0 = 10,
    k' = 2k (eta_R = eta est HERITE, ce n'est pas un nombre neuf). Tout
    le reste se DERIVE dans le code, a la vue : tau_dom, tau_CAP, dt_2,
    CAP_p, la bascule. **Aucun pourcentage n'est tape, et le signe de
    pourcentage n'apparait pas davantage en prose dans le log** -- il a
    deja tue un instrument.

3.7 **Le CAP et la bascule sont DERIVES PAR DEGRE ET PAR POINT**, jamais
    ecrits en valeur absolue partagee. Le CAP depose (1e4) est
    degre-dependant : a p = 4 il coupe AVANT la fenetre. Les tables 5.3
    et 5.4 du gel alpha sont les valeurs ATTENDUES de ta derivation, pas
    des constantes a recopier ; un code qui les recopie ne controle rien.

3.8 **Aucune garde bitwise, aucun perimetre ecrit a la main.** Les
    perimetres s'enumerent par la machine ; quatorze ont ete payes en un
    seul jour pour cette faute.

3.9 **Un log de format inconnu se REFUSE (N-66)**, il ne s'interprete
    pas.

4. LA TRANSCRIPTION DE L'ALGORITHME DEPOSE, ET SON CONTROLE POSITIF
=======================================================================
T-1b met a l'epreuve la recherche de seuil DEPOSEE. Elle se transcrit
depuis le blob, aux lignes citees de `scripts/m9_replication_v1.py` :

    l.279  NGRID, NPASSES, NDENSE = 48, 3, 96
    l.280  LO0, HI0, MAX_ELARG = 0.05, 6.0, 8
    l.372  def chercher_seuil(w2, sgn=1, dt=DT, g=G_REF)

**C'est un RAFFINEMENT DE GRILLE, pas une bissection.** Une bissection
transcrite a sa place rendrait des seuils voisins et une resolution
fausse : c'est la faute la plus facile a commettre ici, et la seule que
le controle ci-dessous attrape a coup sur.

**LE CONTROLE POSITIF (W-transcription, 4.6bis (iii) du gel temoin) :**
l'algorithme RAPPORTE sa resolution, et cette grandeur ne depend pas de
son entree :

    pas_k = W_k / (47^3 x 95) = W_k / 9 863 185

    W_0  = 5.95    -> 6.0325e-07     (k = 0 attendu pour T-1b)
    W_1  = 18      -> 1.8250e-06
    W_-1 = 0.0375  -> 3.8020e-09

k doit etre COHERENT avec l'encadrement ou le seuil est tombe. Une
valeur fausse, OU une valeur juste avec un k incoherent, fait MORDRE la
garde. **La signature n'est pas une constante : c'est une fonction du
nombre d'elargissements.** Comptes au registre pour te reperer : m10
64 points a 6.03e-07 ; m11 26+6 ; m12 70+4 ; m14 37+1 ; m15 28+8 -- et
les quatre points de M12 a 1.82e-06 sont exactement les quatre dont s*
depasse HI0 = 6.

5. CE QUE JE CONTROLERAI A LA CERTIFICATION -- LA BARRE, ANNONCEE
=======================================================================
Je l'ecris maintenant pour que tu puisses la satisfaire par
construction, et non apres coup.

    C-1  **Chaque garde PEUT-ELLE mordre ?** Pour les huit du temoin
         (W-transcription, W-croissance, W-integrales, W-pas,
         W-plancher, W-bascule, W-mirage, W-comptes) et les huit
         d'alpha (G-dt, G-k, G-s, G-w2, G-seuil, G-fen, G-lignee,
         G-comptes), je demande **une demonstration de morsure** au
         pre-vol. Trois gardes muettes par construction ont deja ete
         payees en trois jours : le banc qui tue sous le seuil, le
         temoin de stabilite, l'etat initial tangent. Une garde qui ne
         peut pas mordre est un controle vide, et un faux echec vaut un
         controle vide.
    C-2  **G-seuil est atteignable.** La definition conjointe
         (i)(ii)(iii) de la section 8 du gel alpha doit etre
         IMPLEMENTEE telle quelle, t* LIBRE et fenetre de largeur
         (tau_dom - tau_CAP) avant T_MAX. Sans elle, la branche 1 est
         inatteignable et le banc est muet.
    C-3  **Les etats initiaux declares, et l'etat tangent INTERDIT.**
         Etat A (x0 = 1, D0 = 1 -> H1_0 = 2, N_0 = 3/4) et etat B
         (x0 = 2 -> H1_0 = 10, N_0 = 6). Le depart D(0) = 0, D'(0) = 1
         AU REBROUSSEMENT rend D exactement proportionnel a x'
         (rapport -0.500000000) : c'est la solution TANGENTE, unique
         solution bornee de Hill, le temoin "passerait" par
         construction, et sur elle H1_0 = 0 rend toute derive relative
         absurde. Je verifierai que le code REFUSE cet etat, pas
         seulement qu'il ne le choisit pas.
    C-4  **Les tolerances sont derivees ET plafonnees.** `tol / (8/15)`
         se consigne a chaque degre, passe ou non ; `tol_R / (q - 1)`
         se consigne de meme. Une tolerance derivee de la dispersion de
         la grandeur TESTEE n'a pas de plafond et finit par tout
         accepter.
    C-5  **W-integrales se lit sur dt contre dt/2**, chute d'un facteur
         16 (RK4) : c'est la CHUTE qui est controlee, pas une borne
         absolue, et la variante qui demandait un nombre pur de plus
         est ecartee.
    C-6  **Les comptes en forme derivee** : `comptes + sautes == 39`
         pour le temoin, `comptes + sautes == 90` pour alpha. La forme
         se lit dans le log ; un total juste ecrit a la main ne vaut
         rien.
    C-7  **La transcription, par le controle positif de la section 4.**
    C-8  **P-A est lue a alpha FIXE** : dans un ajustement libre, A
         absorbe l'erreur d'alpha et la prediction ne teste plus rien.
         La tolerance de P-A se derive de la dispersion de A sur la
         grille (dt_2, dt_2/2) x (k = 2, 4), **jamais** par propagation
         depuis alpha.
    C-9  **L'agregation d'alpha** : six alpha par degre, chacun a la
         tolerance, aucune moyenne, aucune statistique d'agregation.
    C-10 **La sortie exigee par 5.7** : la serie (t, x1, x2) de la
         phase 2 avec empreinte convention B, l'etat COMPLET a la
         bascule (t, x1, x2, x1', x2') avec empreinte, et le journal de
         phase 1. Sans l'etat de bascule, G-k compare deux phases 1 de
         longueurs differentes sans pouvoir dire ou elles divergent.
    C-11 **Le perimetre est enumere par la machine**, et le log dit **ce
         qu'il NE JOUE PAS**. Cette section ne se coupe jamais.
    C-12 **Aucune mention d'outillage**, ni dans le code, ni dans le
         log, ni dans le message de depot : c'est la convention du
         depot, et elle prime.

**Ce que je ne ferai PAS** : je ne corrigerai pas ton code. Je rends un
verdict, des defauts numerotes et, pour chacun, le correctif en FORME
EXECUTABLE -- la formule cible, pas l'intention. Le code reste ta plume.

6. LA FORME DE LA LIVRAISON
=======================================================================
Un seul depot, trois pieces : **note `.md` autosuffisante** (verdict de
pre-vol, gardes montrees mordantes, comptes en forme derivee, empreintes
courtes, section "ce que ce log ne joue pas"), **log `.log` compact**
(verdicts, comptes, empreintes -- jamais de dump de contenu) et le
**`.py`**. La note doit se lire seule : je dois pouvoir rediger la
certification sans ouvrir le `.py` ni le `.log`.

**Le pre-vol se joue A MOTEUR FACTICE** avant toute execution reelle :
c'est la qu'on montre les seize morsures de C-1, et c'est la seule etape
qui coute peu tant qu'elle est faite avant.

7. L'ORDRE D'EXECUTION -- IL N'EST PAS AU CHOIX
=======================================================================
    1. l'instrument, puis ma certification, puis le pre-vol a moteur
       factice ;
    2. **LE TEMOIN** : la porte d'alpha s'ouvre si et seulement si T-1,
       T-1b ET T-2 passent ;
    3. **alpha SI ET SEULEMENT SI le reglage est QUALIFIE** (D-alpha-7).
       Un run alpha anterieur au verdict PASSE du temoin n'existe pas au
       sens de N-62.

8. CE QUE CET ORDRE NE FAIT PAS
=======================================================================
Il n'edite aucun gel et n'en rouvre aucun. Il ne prend aucun numero (ni
delta, ni manche). Il ne tranche pas T-1 si son candidat change :
arXiv:2108.06294 (DMV) et arXiv:1302.5257 (Pavsic sin^4) restent
declares SUPPLEANTS et NON transcrits. Il ne dit rien de M18, ni du
temoin quantique. Il ne vaut pas certification : il annonce la barre, il
ne la franchit pas.
