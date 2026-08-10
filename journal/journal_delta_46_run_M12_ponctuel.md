DELTA 46 -- RUN M12 PONCTUEL : CLASSE REFUTEE, PREMIERE LECTURE DE E
-- version v1
(02/08/2026 ; consigne par machine 1 ; ASCII, NFC+LF ; A CERTIFIER PAR
MACHINE 2 -- l'empreinte du present delta ne peut figurer dans son propre
corps, elle est consignee au message de livraison et sera reportee ici a la
certification)

Objet : le run M12 (JSON fa109da9), la reconciliation machine 2
(m12_reconciliation_ponctuel_machine2_v1.py, 10 sections, TOUT CONCORDE,
exit 0), la certification du run (m12_certification_run_ponctuel_machine2.md)
et la contresignature machine 1 (m12_contresignature_machine1_v1.py, TOUT
CONCORDE, exit 0). Les verdicts sont ceux du gel v4 (bf9866a7, cert
f10ffcf3), appliques a la lettre, independamment, par les deux machines.

46.1 CHAINE E19 ET CHRONOLOGIE
-------------------------------
  gel v4 certifie (f10ffcf3, 01/08 21:13) -> certification du script v2
  (5faef5ec, 02/08 01:25) -> run REEL 01:52 heure de Paris, soit
  2026-08-01T23:52:34Z (coherence de fuseau verifiee, UTC+2) ->
  reconciliation machine 2 -> contresignature machine 1 -> present delta.
  CLARIFICATION (r2, relecture machine 1) : le pre-vol a moteur factice
  tueur (01:23) est un CONSTITUANT de la certification du script (01:25),
  pas un maillon qu'elle autorise -- l'ordre des fleches du paragraphe 9 de
  la certification, lu seul, contredit ses propres horodatages. La phrase
  "aucun maillon n'est posterieur a celui qui l'autorise" est vraie sous
  cette lecture, et sous elle seulement. Reformulation proposee a machine 2.
  Mode REEL, aucun factice. Duree 852.94 s sur 67 balayages porteurs
  (12.73 s en moyenne ; denominateur = balayages, voir D1-2).

46.2 VERDICTS
--------------
  P-M12a : CLASSE REFUTEE. m = 11 sur N = 13 ; branche appliquee
    |E| >= 0.10 sur au moins ceil(m/2) = 6 points, obtenue sur 11/11,
    marge 5. Branche CLASSE TENUE (tous les points a |E| <= 0.03) : 0 point.
    Branche m < 3 (NON CONCLUANT PAR CONSTRUCTION) : jamais approchee.
  P-M12b (conditionnelle, lisible car REFUTEE) : VIOLATION DISPERSEE.
    E > 0 sur 9 points, E < 0 sur 2 (2.42 et 2.55).
  PREMIERE MANCHE CONCLUSIVE DE LA CAMPAGNE DEPUIS M6, ET PREMIERE LECTURE
  DE E. La classe ponctuelle a deux parametres ln s*_p = A(w2) u_p + B(w2),
  u_p = 1/(p-2), est morte : en chaque point mesure, aucun couple (A, B) ne
  reproduit les trois degres.

46.3 LA MESURE
---------------
  E = ln s*4 - 2.25 ln s*5 + 1.25 ln s*7 sur les sF bruts de la carte ;
  coefficients (1, -9/4, +5/4) re-derives en Fraction par machine 1 :
  UNIQUE annihilateur de la classe, a normalisation pres (det = -2/15 != 0).

    w2      E             sigma_E     |E|/sigma_E_max
    1.73   +0.764146      2.59e-06        196 358
    1.76   +0.808568      2.55e-06        211 282
    1.84   +0.964440      2.53e-06        256 474
    1.86   +1.015680      2.55e-06        267 986
    2.22   +0.405583      1.46e-06        180 884
    2.27   +0.171548      1.29e-06         85 511
    2.38    PERDU (G7)       --               --
    2.42   -0.147267      1.03e-06         90 459
    2.55   -0.483335      8.87e-07        338 309
    2.67    PERDU (G7)       --               --
    2.72   +0.517399      7.64e-07        411 168
    2.78   +0.519337      7.45e-07        422 759
    2.80   +0.542579      7.38e-07        445 891

  La classe predit E = 0 exactement. Le plus petit module, 0.147, vaut
  90 000 fois le sigma_E_max de son point ; le plus grand, 1.016, en vaut
  268 000. E recalcule machine 2 depuis la carte : ecart max 0.00e+00 ;
  sigma_E en forme derivee (c_p pas_p / s*_p, pas ABSOLU -- E26/E27) :
  ecarts 0.00e+00 et 2.1e-16.
  COMPARAISONS DE BORD (candidate regle 15) : marge minimale au seuil 0.10
  = 0.047267, soit ~2.9e4 sigma_E_max(2.42) ; au seuil 0.03 = 0.117267.
  Aucune comparaison de la manche ne vit pres d'un bord.

46.4 L'ATTENTE GELEE, CLAUSE PAR CLAUSE (jamais reecrite, byte-prouvee v1)
--------------------------------------------------------------------------
  Clause 1, REFUTATION : TENUE.
  Clause 2, P-M12b SYSTEMATIQUE meme signe : FAUSSE (2.42 et 2.55 negatifs).
  Clause 3, |E| entre 0.15 et 0.45 sur la majorite : FAUSSE, DEPASSEE VERS
    LE HAUT -- census machine 1 : 1 point sous 0.15 (2.42, a 0.1473),
    2 dans la bande (2.27, 2.22), 8 au-dessus de 0.45, 4 au-dessus de 0.76.
  L'attente a donc ete a la fois tenue (le verdict), depassee (le module)
  et falsifiee (le signe) par la meme mesure. C'est la signature d'un
  instrument qui mesure au lieu de confirmer, et le registre le porte sans
  retouche de l'attente.

46.5 LES DEUX PERTES : UN MOTIF CONSIGNE, DEUX MECANISMES DISTINCTS
--------------------------------------------------------------------
  meta.exclusions porte le meme motif ("G6 sgn=+1 explosion sous seuil")
  pour les deux lignes ; l'enregistrement les separe :
    7|2.38|+1 : fenetre FINE (explosion a 1.2241), grossiere vide.
    7|2.67|+1 : fenetre GROSSIERE (explosion a 1.5489), fine vide --
      PREMIERE APPARITION DU MECANISME D'E27 hors du degre ou le pilote
      l'a isole. Fenetres contigues verifiees sur les 67 lignes.
  Les deux exclusions sont regulieres a la lettre de G6 ; repercussion G7
  sur les trois degres de chaque point, d'ou m = 11, sans exception.
  D1-1 (machine 2) : le motif doit nommer la fenetre au prochain script.

46.6 TROIS CONTROLES EXERCES SUR DONNEE REELLE
-----------------------------------------------
  (a) LE PIEGE DE L'INDICE 40 PASSE DE "OUVERT" A "EXERCE". La ligne
      5|2.67|+1 est explosive EXACTEMENT a l'indice 40 (= 0.98 s*) et n'est
      PAS exclue (s < 0.98 s* <=> i < 40 ; explosion_sous_0.98s = None,
      exclue = False). Le test negatif exige par la parade est joue par la
      donnee elle-meme, seule ligne sur 67. La parade gelee TIENT.
  (b) G8b EST BORNE, PAS VACANT. Moitie grossiere VIDE sur les 15 lignes
      p=4, exactement comme pre-declare AVANT mesure (ad8dd209, delta 45
      v3) ; NON vide sur une seule ligne du run, 7|2.67|+1. Un controle
      dont le domaine de pouvoir est declare, et qui mord hors de ce
      domaine la ou il le peut. Moitie fine : pouvoir reel aux deux rangs
      (transitions 24/52 et 26/50).
  (c) PARITE AU BIT, TROISIEME GEOMETRIE INDEPENDANTE : sP - sM == 0.0
      exactement aux deux rangs de regression G8 (2.22 et 1.86), ilots et
      retombees identiques. Lignee M11 -> pilote -> M12.

46.7 DEUX CHIFFRES DU GEL REQUALIFIES PAR LA MESURE (verdicts intacts)
-----------------------------------------------------------------------
  (a) "0.03 = 458 x sigma_E_max au pire point" ETAIT UNE BORNE, PAS UNE
      PROJECTION. Provenance re-derivee machine 1 : 458 = 0.03 / 6.550e-05,
      le sigma_pire du gel (delta 45 v3), construit avec pas = PLAFOND G5
      (1e-5) et s* PROJETES. Mesure au pire point (1.73) : sigma_E_max =
      3.892e-06, d'ou 0.03 = 7709 x et 0.10 = 25 696 x. Conservativite
      mesuree x16.83 (rapport des pas 1e-5/6.03e-07 = 16.58 ; reliquat =
      s* projetes vs mesures ; coherence 7709/16.58 = 465, contre 458 au
      gel, verifiee). OBLIGATION DE LECTURE PERMANENTE, contresignee : le
      458 ne se cite jamais comme une mesure. Sens inverse d'E21.
  (b) LE PLAN D'ATTRITION ETAIT TRES CONSERVATEUR, ET NE BOUGE PAS.
      Plan (herite du pilote) : q_L = 0.2296, s_pt = (1-q_L)^3 =
      0.4572147008, E[m] = 5.94, P(m>=4) = 0.9154 -- encadrement D-N
      P(12) = 0.876124 < 0.90 <= 0.915439 = P(13) re-derive machine 1.
      Mesure : 2 lignes sur 65 (3.1 %), 2 cellules sur 39 (5.1 %) ;
      P(m >= 11 | plan) = 4.8e-3, re-derive. AUCUN amenagement de D-N
      (regle ecrite avant la mesure ; sa conservativite a coute des
      recherches, pas de la validite). Le materiau entre au registre
      conformement a attrition_39 et a la note du delta 45 v3 (45.4) :
      toute mise a jour future de q_L se fait par regle EXHAUSTIVE
      pre-declaree sur TOUTES les lignes balayees sous cette geometrie,
      jamais par selection.

46.8 P-M12d -- CONSIGNATION DOUBLE-SIGNEE : BRANCHE (iv)
---------------------------------------------------------
  Motif consigne (aucune porte ; rho = Spearman, ex aequo moyennes,
  repliques machine 1 a la 4e decimale : -0.6393 / -0.4364 / -0.4909 ;
  les ex aequo de d/r sont exacts en rationnels, 0.22/0.12 et 5/3) :
  - E lisse et monotone decroissant de 1.86 a 2.55, passage par zero
    ENCADRE PAR DES POINTS MESURES entre 2.27 et 2.42 ;
  - E croit de 1.73 a 1.86 ;
  - saut de +1.0007 entre 2.55 et 2.72 (le point perdu 2.67 tombe DANS
    l'intervalle : la nettete du saut n'est bornee que par ses deux
    encadrants survivants), puis quasi-plat 2.72-2.80 ;
  - trois regimes coincidant avec trois familles de resonance (ordres 3-5
    rayon 0.12 / ordre 7 rayon 0.03 / ordre 4 rayon 0.12).
  LECTURE : machine 2 propose la branche (iv) -- aucun des trois motifs
  pre-declares ne s'applique proprement, rien ne se designe apres coup
  (S41.5). CONTRESIGNEE PAR MACHINE 1, avec les exclusions chiffrees :
  - (ii) [variation lisse en w2] tombe sur le saut +1.0007 entre voisins ;
  - (i) [|E| croit quand d/r decroit] ne tient pas comme ORDRE : deux
    contre-paires intra-famille ordre 3, (d/r, |E|) = (1.8333, 0.4056)
    contre (1.9167, 0.7641) et contre (2.0000, 0.8086) ; et d/r seul ne
    determine pas |E| -- a d/r = 1.8333 exactement, |E| vaut 0.4056
    (ordre 3) et 0.5193 (ordre 4). Le signe global de rho va dans le sens
    de (i) ; l'ordre ponctuel le contredit ;
  - (iii) [pas de structure] est faux a vue.
  C'est la premiere utilisation de la branche (iv) de la campagne. Le motif
  se re-mesure ; il ne se choisit pas. Toute hypothese de mecanisme formee
  sur ce motif est desormais POST-HOC et exige son propre gel (precedent
  p=6).

46.9 CONTRESIGNATURE MACHINE 1 : PERIMETRE ET RESULTAT
-------------------------------------------------------
  Artefact : m12_contresignature_machine1_v1.py + .log (TOUT CONCORDE,
  exit 0 ; empreintes en 46.12). Entrees = litteraux consignes des deux
  documents recus ; AUCUNE simulation ; re-derivations exactes (Fraction,
  entiers, binomiale) et replications flottantes marquees comme telles
  (E28). Re-derive et conforme : coefficients et unicite de E ; branches
  P-M12a/P-M12b et leurs marges ; census de l'attente ; saut et zero ;
  les trois Spearman ; le plan D-N complet (s_pt, encadrement, E[m],
  P(m>=11)) ; les quatre ancrages (gel ET mesure) et leur facteur ; les
  invariants 67 et 75 ; la duree ; le fuseau ; G2 a 4.9 %. Reste du lot
  machine 2, non re-derivable sans le JSON : E depuis la carte, sigma_E,
  m par chemin brut, gardes G1'/G3/G4/G5/G8 -- certifies par la
  reconciliation, dont la logique de code a ete relue (chemin brut ->
  resume passant par G6, lettre des branches, piege de l'indice 40).

46.10 NOTES D'EXPLOITATION (aucune donnee touchee)
---------------------------------------------------
  De machine 2 (certification, section 8), consignees :
  D1-1 le motif d'exclusion nomme la fenetre (prochain script).
  D1-2 resume.duree_par_recherche_s : denominateur = 67 recherches
       PORTEUSES DE BALAYAGE, pas 75 -- renommer ou renvoyer.
  D1-3 la carte ne porte aucun marqueur d'exclusion ; le chemin brut ->
       resume pour m DOIT passer par le bloc G6 (piege reel : la premiere
       passe de reconciliation y est tombee). Parade proposee : champs
       exclue + exclue_motif dupliques dans la carte, par ligne.
  D1-4 meta.gardes est une liste vide -- champ mort a retirer ou remplir.
  De machine 1 (relecture de la certification), a accepter ou refuter :
  r1   Section 2 : "8 points sur 11 sont au-dessus de 0.40" -- le compte a
       0.40 est NEUF ; a 0.45 (borne haute de l'attente, lecture voulue par
       le contexte) il est HUIT. Corriger en "8 au-dessus de 0.45" ou
       "9 au-dessus de 0.40". Aucun impact.
  r2   Section 9 : ordre des fleches pre-vol/certification (46.1).
  r3   L'empreinte de m12_ponctuel_run_machine2.log (reference en tete de
       la certification) manque a la table de la section 9 -- a consigner.
  r4   Cosmetique : les deux lignes "G3 p=4" du log de reconciliation sont
       identiques et non etiquetees ; nommer les quatre rebindings.
  VOIE DE TRAITEMENT [DECISION MACHINE 2] : soit une certification v2
  integrant r1-r4 avant certification du present delta ; soit v1 reste
  seule au registre et r1 devient candidat erratum, numero attribue AU
  MOMENT de sa consignation (E18), apres l'arbitrage pendant de la
  collision S42.3/S43.

46.11 CE QUE CE RUN N'ETABLIT PAS
----------------------------------
  - Aucune lecture physique, dans aucun sens : M12 MESURE, ELLE NE DERIVE
    PAS ; une refutation ne designe pas la classe de remplacement.
  - La refutation NE SE TRANSPORTE PAS AU BORD GAUCHE (aucun point sous
    1.73 n'est R-2'-propre ; limitation ecrite AVANT la mesure) -- la
    chaine classique fermee y vit et n'est pas touchee.
  - p=3 (E22) et p=6 (hypothese post-hoc a geler ailleurs) : non mesures.
  - Le mecanisme du signe negatif a 2.42 et 2.55 : non etabli (deux points,
    une famille, zero replication).
  - Le statut d'une eventuelle re-mesure des deux points perdus (2.38,
    2.67 -- ce dernier au coeur de l'intervalle du saut) : DECISION
    OUVERTE ; elle serait motivee par le motif observe, donc post-hoc, et
    exigerait un gel neuf avec sa propre attente.

46.12 REGISTRE DES EMPREINTES (nouvelles, sha256)
--------------------------------------------------
  JSON m12_results.json (machine 2)
    fa109da92e582520cfcb63b46bc41fa7d4b62295891f413bb97c6095b2fe59b1
  certification du run (m12_certification_run_ponctuel_machine2.md)
    6e608e036efb84e14e536e51330a9025fad44d1803d74b4711ffdf35e1a440a4
    (brute = canonique)
  m12_reconciliation_ponctuel_machine2_v1.py
    0970b9b9b61268a3d99aa8dcc1ff3910d4b5003872f5e24a792870f738cf6c76
    (brute = canonique)
  m12_reconciliation_ponctuel_machine2_v1.log
    brute      f5a3a1584cb71b5cd19ba692fda878b946cf2a4efcc63e4e9d063782af1ef3eb
    canonique  370bec8db792199f4a9580192c97e31ee43c03afcd799352af9a34111f705182
    (les deux consignees ; la divergence est de fin de ligne, a confirmer
    par machine 2 sur son original)
  m12_contresignature_machine1_v1.py / .log : empreintes au message de
    livraison machine 1 (fichiers joints, a re-hasher par machine 2).
  Deja au registre, references du run : gel v4 bf9866a7 (cert f10ffcf3) ;
  script m12_ponctuel_v2.py c5659f52 (cert 5faef5ec) ; pilote importe
  663b17e2 ; cible G1' ed0e27b1 ; moteur c8ed357b.
  MANQUANTE (r3) : m12_ponctuel_run_machine2.log.

46.13 CONSEQUENCES DE REGISTRE
-------------------------------
  (a) L'ARC L1 EST CLOS EN TROIS TEMPS : forme brute decouverte et gelee
      (bloc L1 v4, dbe633e2) -> test de la projection sous-alimente par
      construction (M11) -> test ponctuel SANS FIT, refutation a cinq
      ordres de l'incertitude (M12). Le fait de structure du delta 42
      ("la forme brute ne demande ni levier, ni Sxx, ni plancher") a ete
      execute tel quel. L1-h est SANS OBJET : sa cible est morte par la
      voie directe ; toute reactivation exigerait un gel neuf.
  (b) LE REPERE P-M11g N'A PAS EXPIRE : son ecart de -29.3 % se reecrit
      exactement |E(2.85) - E(1.35)| = ln(10.2185/7.2252) = 0.3467 --
      deux points hors programme, du meme ordre que les E mesures. Il
      indiquait par la fenetre, portes fermees, ce que M12 vient de rendre
      par la porte. Il reste SANS porte (delta 41.4) ; l'abstention
      d'alors est retrospectivement le bon geste, et le registre le note.
  (c) beta(p) = F/(p-2) + Z ne peut plus etre qu'une description AJUSTEE :
      la version ponctuelle exacte est morte. Les obligations de
      documentation existantes (mecanismes morts, cote raide, etendue
      d'archive) restent telles quelles, aucune n'est rouverte ici.
  (d) Les 13 points du programme et leur verdict sont VUS ; rangs 14-16
      toujours sans statut de reserve ; toute manche sur la structure de E
      est post-hoc et se gele comme telle.
  (e) TOUJOURS OUVERTS (renvois 44.6 / 45.7) : promotion de la regle 15 --
      le run lui verse un exemple negatif propre (46.3) ; arbitrage de la
      collision S42.3/S43 (aucun numero avant) ; double etat de
      CAMPAGNE_etat_complet, desormais en retard de la manche la plus
      importante depuis M6 -- mise a jour a faire ; bilan des fautes
      M8-M11 (numero au moment de la consignation, E18) ; cahier des
      charges de l'observable quantique (C2), toujours non ecrit -- M12
      ne le remplace pas ; et le dossier d'envoi : l'arc L1 -> M11 -> M12
      donne a la note une fin racontable en une page (une loi proposee, un
      test de projection sous-alimente, un test ponctuel sans fit qui
      refute a cinq ordres). Les deux decisions bloquantes restent
      inchangees (contenu du bundle expedie ; chiffres perimes de la
      note FR).

=== FIN DU DELTA 46 ===
