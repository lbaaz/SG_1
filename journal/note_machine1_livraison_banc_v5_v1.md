# LIVRAISON DE L'INSTRUMENT v5 -- MACHINE 1 -- v1
# Redaction machine 1, 28/08/2026. Repond a la certification
# f882b9c04c7b7ced (v4 NON CERTIFIEE, D-I-1 bloquant), a ma reponse
# 3258684af5ba744c (perimetre fige), au contrat du chargeur
# e69d8a006f584063, et s'ancre sur le gel temoin v11 CERTIFIE
# (a2e7ef3e237c5acf, note v2 7fc5f2412b99ad50).
# E18 : aucun numero pris. E19 : construit sous gels certifies.
# Certification machine 2 ENTIERE requise avant tout usage opposable.

=======================================================================
1. LES PIECES
=======================================================================

    construction_banc_v5_machine1_v1.py     81730d2bf7095c1f   22449 o
    banc_qualification_machine1_v5.py       b8a0f75323182e55  184866 o
    selftest_v5_machine1.log                30c2e32330f8c75f   11231 o
    banc_v5_machine1.log                    80c14a03ab946ea3   24753 o
    prevol_temoin_v5_machine1.log           a8b1e76e4267a3a9   18277 o
    prevol_alpha_v5_machine1.log            1d193010b238e4f3   30118 o
    (convention B ; ASCII pur, CR = 0, partout)

PROVENANCE, EPINGLEE : v3 DEPOSEE (5fae2a8c94cf8685) -- construction v4
(35b9ff3b8e5b7ef0, 53 rempl.) --> v4 **PIN 36a3f06f19871c38** (reproduite
AU BIT par les deux machines) -- LE PRESENT SCRIPT (24 remplacements
Q01..Q24, chacun a UNE occurrence) --> v5. PB-1 : rien d'edite.

=======================================================================
2. LE PERIMETRE, TENU -- ET D-v5-1, LA TROUVAILLE QUI LE PLIE
=======================================================================

(i) D-I-1, (ii) D-I-2, (iii) critere 5.4, (v) chargeur au contrat :
LIVRES (sections 3 a 5). (iv) LD-16 sans c_pl : **NON LIVRE, et voici
pourquoi -- c'est la trouvaille de la seance.**

    **D-v5-1 (dette, arbitrage requis)** : le depot 9bis CLOS
    (c4310e33da6b9759) embarque les feuilles de LECTURE du run 85
    (/T1, /T3a : plancher_dt2 = c_pl x eps x N, statuts "MORD" /
    "NON LUE (plancher, LD-16)"). Toute LD-16bis change ces feuilles
    -- valeurs ET statuts -- et fait mordre 9bis sur CHAQUE run
    legitime : le controle de custody tuerait l'instrument qui
    s'ameliore. Decision versee AU CODE MEME (commentaire sur C_PL) :
    LD-16 HERITE VERBATIM, c_pl confine et nomme
    ("c_pl_ld16_herite" au reglage), zero usage ailleurs.
    Arbitrage : depot re-ancre sur un run v5 depose, ou LD-16bis en
    v6 avec nouvelle reference. Lecon pour tous les perimetres a
    venir : SEPARER les feuilles de MESURE des feuilles de LECTURE.

=======================================================================
3. LE CRITERE 5.4 -- W-plancher est la garde, et le cout tombe juste
=======================================================================

lecture_5_4 (helper unique, servi par T-2, le banc et le selftest) :
W-plancher = e(dt2/2) >= C(p) x plancher_comp, C(p) = 1/(1-2^-tol_ordre)
en PLEINE PRECISION, consigne : **7.7143 / 8.3158 / 8.8966**. Sous le
seuil : W-plancher MORD (v11 8, ligne 1008 : c'est la garde), et
l'ordre N'EST PAS LU -- p_obs mis a None, ni dans un sens ni dans
l'autre. Ratio e/seuil consigne a chaque point ; SUR LE FIL se lit au
ratio, sans nombre nouveau (D-M17-47).

Le prevol temoin reproduit le cout que le gel declarait, point pour
point : **4/9 NON LUS** -- 5|1.73 (ratio 0.991, sur le fil : le point
a -0.85 pour cent), 7|1.73 (0.759), 7|2.27 (0.853), 7|2.80 (0.957) ;
les cinq autres LUS et PASSE (ratios 1.26 a 2.38). Verdict consigne :
NON CONCLUANT D'INTEGRATEUR, branche 4, les quatre nommes.

=======================================================================
4. D-I-1 ET D-I-2 -- prouvees EN CONDITIONS, pas seulement au banc
=======================================================================

    AVANT (v4) : le prevol temoin MOURAIT sur AssertionError, ligne
    3061, APRES mesure, AVANT ecriture -- rien n'existait.
    APRES (v5) : le MEME prevol SE TERMINE -- FIN a 184.9 s, JSON
    0557f3d6b6d4ce21 (27473 o), MANIFEST, journal, prevol_fautes [].
    Le verdict se CONSIGNE ; les fautes du factice s'assertent APRES
    ecriture (arret_prevol_si_fautes, demontre au banc par G32).
    prevol_alpha au meme regime : VERIFIE, 9/27, fautes [], rc 0,
    JSON 2eae06b29895c1d7 (113949 o), FIN a 181.5 s.

    D-I-2, DEUX preuves vivantes dans out_prevol/ : le dossier du run
    plante versionne (temoin.avant_20260828T201716Z), puis le dossier
    partiel de l'essai alpha tue par timeout versionne a son tour
    (alpha.avant_20260828T202752Z). Rien n'ecrase rien.

=======================================================================
5. LE CHARGEUR AU CONTRAT (a)-(d)+(c') -- joue sur le DEPOT REEL
=======================================================================

charger_depot_9bis : depot autoporteur (empreinte B consignee),
comptes ET profondeur minimale-suffisante RE-DERIVES de la copie
embarquee (arret sinon), custody contre le registre par sous-arbre en
forme canonique -- json.dumps(sort_keys, ensure_ascii, separateurs PAR
DEFAUT), sha256 16 hex -- divergence = ARRET AVANT toute lecture ;
present-mais-illisible = le meme ARRET ; absent = custody NON JOUE
consigne, le controle se joue sur la copie. Au banc : G29 charge le
depot REEL (c4310e33da6b9759, custody 4/4, identite 0 ecart) ; G30
perturbe une feuille -> "depot et registre divergent (/T1b :
55be152cd5aac578 vs bbd3e50146c72ccc)" -- et bbd3e50146c72ccc est
EXACTEMENT le hash du contrat : la forme canonique se reproduit ;
G31 reference absente -> NON JOUE consigne, le controle joue.

=======================================================================
6. LES COMPTES -- sur l'artefact CITE, et deux fautes versees
=======================================================================

Tout ce qui suit est joue sur **b8a0f75323182e55** (le log selftest
consigne l'empreinte au demarrage, E19) : selftest **103/103** (+ ligne
v5 : C(p), lecture_5_4 trois branches, forme canonique = separateurs
par defaut, en asserts durs) ; banc **55/55**, gardes enumerees 17,
demontrees 17, sans morsure [] ; les deux prevols ci-dessus.

Verse : (1) les premiers comptes 103/103 et 55/55 avaient ete obtenus
sur l'intermediaire 658920fb -- REJOUES ici sur le final, un compte
cite se compte sur la piece citee ; (2) deux iterations de
construction : `re` absent de la v4 (strip de suffixe a la place), et
Q20 pose AVANT l'init de lectures_non_lues -- KeyError avant ecriture :
**la ligne qui documentait D-I-1 a commis D-I-1**, re-ancree apres
l'init ; (3) le premier log alpha (506da3b898d64a31) etait TRONQUE par
timeout, sans valeur, remplace par un run entier.

=======================================================================
7. RECONSTRUCTION MACHINE 2 -- quatre commandes
=======================================================================

    # v4 et v5 a cote du script ; registre = clone SG_1 avec la v11,
    # la note v2 et journal/depot_9bis_temoin_v1.json installes
    python construction_banc_v4_machine1_v1.py      # -> 36a3f06f19871c38
    python construction_banc_v5_machine1_v1.py      # -> b8a0f75323182e55
    python banc_qualification_machine1_v5.py --selftest --registre SG_1
    python banc_qualification_machine1_v5.py --banc     --registre SG_1
    # puis les deux prevols (--prevol --mode temoin|alpha)

=======================================================================
8. CE QUE CETTE NOTE NE FAIT PAS
=======================================================================

Elle ne prend aucun numero (E18) et ne depose rien. Elle ne certifie
pas : la certification machine 2 est ENTIERE -- reconstruction au bit,
comptes, prevols rejouees, lecture des 24 remplacements. Elle ne
tranche pas D-v5-1 (arbitrage operateur) ni l'autre moitie de N-70
(les cles du pre-vol, a deposer avant tout run). Elle ne prononce
aucun verdict du volet T (D-M17-46) : le NON CONCLUANT du prevol est
une sortie de FACTICE, bannieres partout, N-62.

-- FIN note_machine1_livraison_banc_v5_v1 --
