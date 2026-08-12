JOURNAL DELTA 76 -- P-g EST REPRODUIT AU BIT : LA LIAISON D'INSTRUMENT
M16 EST VERIFIEE (machine 2, 2026-08-12)
=======================================================================
S'insere apres le delta 75 (e9af644494fd437a). Numero pris A L'ACTE au
depot, sous la regle 66.5.c. Acte de CLASSE B (delta 71) : il satisfait
un PREALABLE NOMME du gel v9, celui dont le gel dit que sans lui
"RIEN ne tourne".

76.1 LE FAIT
  Le point fixe P-g du gel v9 (5f73ee25cbb89821) exige que la ligne
  4|2.62|+1, rejouee sous la liaison declaree, reproduise le verdict
  ET le s* de l'artefact 96d78407. Joue ce jour par machine 2 :
    s* mesure   7.224022666106334
    s* artefact 7.224022666106334
    ecart       0.0            tolerance (pas de l'artefact) 1.82e-06
    note        'OK|pas=1.82e-06'  -- identique a l'artefact
    recevable   True           (artefact : vivante)
  LE POINT FIXE N'EST PAS REPRODUIT "DANS LA TOLERANCE" : IL EST
  REPRODUIT AU BIT. L'ecart est exactement nul, et le pas final
  mesure est celui de l'artefact. La chaine declaree EST l'instrument
  qui a produit 96d78407.

76.2 LA CHAINE EXERCEE, TELLE QUE LE GEL LA NOMME
  couche manche m15_site83_v2.py    41ddebcd72b96e64  CONFORME
    -> charger_pilote() : verifie l'empreinte du pilote ET re-verifie
       son gel jumeau (03e29c86) -- custody transitive
  pilote m12_pilote_v3.py           663b17e2955c79c0  CONFORME
    -> charger_moteur() : verifie l'empreinte du moteur
  moteur m9_replication_v1.py       c8ed357b120352c4  CONFORME
  Aucune piece n'a ete re-frappee : la chaine est celle du registre,
  chargee par ses propres verificateurs.
  Etat d'entree du moteur : P = 5 (le module est cable sur la manche
  M9), G_REF = 0.05, DT = 0.006.
  rebind(m9, 4, journal) : G3 backward = 4.328e-16 contre une
  tolerance de 1e-12 -- la garde d'identite de force passe de trois
  ordres de grandeur.

76.3 CE QUE LE PRE-VOL CORRIGE DANS MA PROPRE PRESCRIPTION
  La note de pre-vol du script v4 (0cb4d8a489e32cbe, D-32) disait que
  le script "re-frappe a la main" une restauration que le pilote
  fournirait. C'EST INEXACT, et je le verse : rebind(m9, p, journal)
  pose P, mesure G3 et journalise -- IL NE RESTAURE PAS. Verifie :
  apres la mesure, m9.P vaut 4 et non 5 ; c'est le harnais qui a du
  restaurer.
  CONSEQUENCE OPPOSABLE : la restauration exigee par N-56 est A LA
  CHARGE DE L'APPELANT. Le script v4 avait donc RAISON de la coder
  (try/finally + assert). Ce qui reste de D-32 : prendre le journal
  et le moteur du pilote (rebind, charger_moteur) au lieu de les
  re-frapper, et appeler une chaine de mesure qui existe -- le
  chercher_seuil_ligne appele par la v4 n'existe toujours pas.

76.4 PREMIER CHIFFRE DE FAISABILITE HORAIRE DE LA MANCHE
  Une recherche p=4 a 2.62 : 29.7 secondes.
  31 lignes hors strate 2 : environ 15 minutes ; avec les quatre
  lignes de strate 2, environ 17. La manche est COURTE -- tout le
  cout de M16 aura ete la preparation, pas la mesure. Chiffre
  consigne d'avance, il servira de reference au run.

76.5 CE QUE CE DELTA N'ETABLIT PAS
  Il ne certifie PAS le script : m16_crible_v4.py (63bf76daf6b35f6f)
  porte six defauts de cablage constates au pre-vol
  (note 0cb4d8a489e32cbe), dont un point d'entree inexistant. AUCUN
  RUN N'EST AUTORISE. Ce delta etablit la LIAISON, pas le script.
  Il ne mesure aucune ligne de la manche : la seule ligne jouee est
  le point fixe, qui est du registre et non de la manche.
  Les degres 5 et 7 n'ont pas ete exerces ; la duree citee vaut pour
  p=4 a un signe.
  Aucun numero d'erratum n'est attribue (E18).
  Borne : 76.

EMPREINTES RE-DERIVEES LE 2026-08-12, relues du disque a l'instant de
la citation (N-48). PIECES CITEES (16 hex ; brut == canonique NFC+LF)
  gel v9 5f73ee25cbb89821 ; script v4 63bf76daf6b35f6f ; note de
  pre-vol v4 0cb4d8a489e32cbe ; harnais P-g 57cc06af1e5260d9 et son
  log 2a13e8983541da51 (machine 2, BOCAL4, fournissables) ; couche
  manche 41ddebcd72b96e64 ; pilote 663b17e2955c79c0 ; moteur
  c8ed357b120352c4 ; artefact 96d784077577d57d ; deltas 73 2706c39a,
  74 2509cc58, 75 e9af6444.

=== FIN DU JOURNAL DELTA 76 ===
