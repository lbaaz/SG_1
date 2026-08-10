PRE-ENREGISTREMENT M9 -- PREMIER TEST PROPRE DU +1.00 DE M3 (p=5,
CONVENTION (f) INTEGRALE)
(gele avant l'ecriture de toute ligne de code ; bloc ASCII, canonique NFC+LF ;
nom de fichier versionne conformement a la regle E19 -- version v2)

HISTORIQUE DU GEL
  v1, sha256 4e80db1b3e7eb48735c305ab350d350809661d64cf4db2aac2245011918de05c
  RETIREE A LA CERTIFICATION (audit pre-feu machine 2 du 26/07, defaut
  D-M9-1) : le signe de l'etat initial n'etait pas declare ('s0 = 0.7
  s_cible'), alors que les quatre T de reference de M3 sont TOUS mesures a
  sgn = frag = -1 (m3_parite_2, island_state(sgn*0.7*st)) et que la lignee
  m7/m8 (source des moteurs) implemente s0 positif sans signe
  (corps_m7 lignes 355/371/199, verifie machine 1). Materiel :
  T(+1)/T(-1) = 0.406 a 2.85 -- un M9 en +1 garantissait une fausse alerte
  P-M9c et rendait fausse la clause (e). Premiere application de la regle
  E19 : le defaut est mort avant la premiere ligne de code.
  v2 : (1) s0 signe cote fragile (texte en ETAGE 2) et programme G5 exprime
  en sgn_F ; (2) sqrt2 promue QUATRIEME ancre bloquante de G1a (valeurs
  transmises par l'audit pre-feu), G1c supprimee (absorbee) ; (3) ecart
  s_cible json-M3 vs forme fermee declare en (h), decouvert par la
  verification machine 1 de l'audit ; (4) attente retourne declassee en
  ordre de grandeur. AUCUNE porte ni aucun seuil modifies. Aucun numero
  d'erratum reserve (regle E18). AUCUN code avant qu'un message de
  certification croisee cite l'empreinte du PRESENT bloc v2 (regle E19).
  Le script s'appellera m9_replication_v1.py.

DECISION D3 (arbitrage humain du 26/07, ANTERIEUR a la redaction de ce bloc,
consigne au journal delta 24)
  La clause de M8 v1  interdit d'empiler une troisieme manche quantique sans
  changer d'estimateur  visait, par sa derivation, la REPETITION DU MEME
  TEST. Or il est etabli (S23) que M8 n'a pas execute les systemes de M3 :
  trois points canoniques sur quatre tournaient a un couplage different
  (x1.40 / x1.63 / x1.89). M9 en convention (f) est donc le PREMIER test du
  +1.00 de M3, pas un empilement. Lecture B adoptee A DEUX, avec deux
  compensations GELEES :
  (C1) l'observable differentielle (systeme a signe retourne) est mesuree et
       consignee aux SIX points -- le chantier estimateur avance dans la
       meme manche ;
  (C2) si M9 sort NON CONCLUANT, la clause se REARME a pleine force : aucune
       manche quantique supplementaire, a QUELQUE degre que ce soit, sans un
       estimateur change ET muni d'une derivation. Pas de lecture B deux
       fois.

QUESTION
--------
rho(T, K5) = +1.00 mesure par M3 sur 4 points (p = 0.042, marginal) : ce
signe se confirme-t-il avec puissance (6 points, p <= 0.029, deux
troncatures) quand la carte classique, la calibration et l'etat initial
utilisent la MEME definition du seuil que M3 (sF = min des deux signes) ?

DERIVATIONS PREALABLES (faits verifies avant gel)
-------------------------------------------------
(a) CONVENTION (f), gelee pour TOUTE la manche : s* = min( s*(sgn=+1),
    s*(sgn=-1) ) -- garde-fou M1 pour degre impair, et definition de la
    carte sF de M3. Asymetries r_s = s*(+1)/s*(-1) consignees partout,
    AUCUNE porte dessus. Donnee p=7 (S24) : le cote fragile peut S'INVERSER
    en w2 (-18.9 % a 1.80) et atteindre 38 % (2.40) -- les deux signes sont
    donc indispensables aussi aux points neufs 1.80 et 2.40. Donnee p=3
    (audit du 26/07) : frag = +1 sauf a 2.85 -- la non-uniformite du cote
    fragile est generique, d'ou la forme 'sgn_F par point' de ce gel.
(b) NULLES EXACTES DE SPEARMAN (enumerees, M8 v1) : n=6 : P(rho >= +0.80)
    = 0.0292 ; n=5 : P(rho >= +0.90) = 0.0417 ; n=4 : au mieux 0.0417.
    ECHELLE ADAPTATIVE gelee : seuil +-0.80 si n_retenu = 6 ; +-0.90 si
    n_retenu = 5 ; n_retenu <= 4 -> ECHEC DE DESIGN (pas un verdict
    physique), redesign obligatoire.
(c) COQUILLE FIXE 35 <= max(n1,n2) <= 45 (891 etats a tout N >= 46).
    Tampon a p=5 : 2 sauts (N=56), 3.6 sauts (N=64). Precedent M8 :
    rho(T56,T64) = +1.00 -- la resolution de rang est acquise a p=5.
(d) AUCUN TEMOIN BORNE a p impair (M7-(d), inchange). FREE (g=0) teste le
    pipeline, pas la dynamique. Le retourne est NON borne : il borne le
    canal generique x^5, il n'est pas un controle borne.
(e) ANTI-FRANKEN-RHO (S23, gelee) : le rho de M9 n'utilise QUE la carte de
    M9. En revanche T_M9/T_M3 aux canoniques est desormais LEGITIME et
    central : par construction (meme carte sF, meme calibration, MEME COTE de
    deplacement initial sgn_F), M9 refait les systemes de M3 -- c'est le
    point de toute la manche.
(f) CALIBRATION : nbar1 = 7 ; s_cible = sqrt(14 Delta)/(1+w2^2) ;
    g_cal = K5_min / s_cible^3 avec K5_min = 0.05 x sF^3.
(g) ANCRES DISPONIBLES (provenance machine 2, m3_calib.json, S23) :
    sP/sM : 1.35 : 0.34921/0.31011 ; 2.00 : 0.37477/0.37401 ;
    2.85 : 3.19542/2.58573 ; sqrt2 : 0.38604/0.32665 (asym 18.18 %,
    frag = -1 ; transmis par l'audit pre-feu machine 2 du 26/07 -> ANCRE,
    cf. G1a). 1.80, 2.40 : AUCUNE ancre (points neufs en convention (f)).
(h) ECART DECLARE (decouvert en verifiant l'audit) : les s_cible STOCKES
    par M3 excedent la forme fermee (f) d'un facteur UNIFORME x1.00285
    (mesure aux trois points via g = K/s_cible^3 : formule 8.5807e-4 /
    1.2013e-3 / 0.65905 contre json 8.5080e-4 / 1.1911e-3 / 0.65344, soit
    -0.85 % sur g ; equivalent nbar = 7.04). Cause NON identifiee, a lire
    dans le code de calibration M3. Propagation pire cas sur T : ~3.4 %
    (dlnT/dlng ~ 4 mesure), sous G5 (+-5 %) et sous la fenetre P-M9c
    [0.80, 1.25]. M9 utilise la FORME FERMEE (f) partout (uniformite aux
    points neufs) ; l'ecart aux canoniques est consigne par point.

ETAGE 1 -- CLASSIQUE : LA CARTE sF SUR SIX POINTS
-------------------------------------------------
w2 dans {1.35, sqrt(2), 1.80, 2.00, 2.40, 2.85}, g = 0.05, DEUX signes,
passe dense n = 96 partout.

P-M9-pre  ORDONNANCEMENT (porte prealable, miroir de P-M7a/P-M8-pre)
  argmin K5_min != 2.00 -> LIEN CONFIRME, la prediction rho > 0 conserve sa
    derivation. [attendu : carte sF de M3 donne 1.49e-3 (1.35) < 2.62e-3
    (2.00) sur les canoniques.]
  argmin K5_min = 2.00 -> LIEN REFUTE ; l'etage 2 TOURNE sans prediction,
    interdiction de re-deriver un signe apres coup (lecon E15).

ETAGE 2 -- QUANTIQUE
--------------------
H = -w1 n1 + w2 n2 + (g/5) x^5, diagonalisation exacte, N = 56 et 64.
Etat initial : coherent apparie DU COTE FRAGILE (correction D-M9-1) :
s0 = sgn_F x 0.7 x s_cible, ou sgn_F est le signe realisant le minimum de
la carte sF au point, FIGE depuis la carte a g = 0.05 et consigne par
point -- la regle de M3 (island_state(sgn*0.7*st), sgn = frag). MEME s0
(meme sgn_F) pour GHOST, RETOURNE et FREE. Si le double-signe de G5 revele
un cote fragile different a g_cal, l'ecart est CONSIGNE (aucune porte) ;
la definition reste celle de la carte a g = 0.05, comme M3.
Observable : T_shell.

P-M9a  PORTE PRINCIPALE -- rho de Spearman entre T_shell et K5_min, points
       retenus, AUX DEUX troncatures ; seuil selon (b).
  rho >= seuil AUX DEUX N -> PREMIER SOUTIEN PUISSANTE de la jambe
    quantique de H-PROFONDEUR, et replication du signe de M3.
    [derivation : carte ordonnee par le fond (P-M9-pre) => T suit le fond
     => positif ; M3, coherent sur ses propres systemes (S23), predisait
     le signe.]
  rho <= -seuil AUX DEUX N -> REFUTATION, et cette fois LEGITIME : memes
    systemes que M3 par construction => le +1.00 de M3 est requalifie
    (bruit de petit n) ET la jambe quantique tombe. Les deux consequences
    sont ecrites d'avance.
    [derivation : anti-correlation puissantee avec un creux qui n'ordonne
     pas la carte contredit le coeur de l'hypothese.]
  Tout le reste -> NON CONCLUANT, et LA COMPENSATION C2 SE DECLENCHE :
    rearme de la clause anti-empilement a pleine force (texte en D3).
  ANTI-ARRET-OPTIONNEL : rho dans [0.60, seuil) ne prolonge RIEN.
  Le p exact est reporte dans tous les cas, enumere sur le n effectif.

P-M9b  COMPENSATION C1 -- CANAL GENERIQUE (consigne, AUCUNE porte)
  T_retourne aux SIX points, N = 64. Fourche de lecture PRE-DECLAREE
  (heritee de M8 v1, point par point, PAS de mediane) :
    T_ghost/T_retourne >= 10 partout -> contraste fantome grand a p=5 ;
    <= 3 quelque part -> le caveat cause (2) s'attache au verdict P-M9a ;
    entre : consigne sans lecture.
  En sus, pour le chantier estimateur (C1) : le profil complet
  {T_ghost, T_retourne, g_cal} par point est consigne au JSON -- matiere du
  futur estimateur derive, aucune interpretation gelee ici.

P-M9c  LA REPLICATION DIRECTE (consigne, lecture pre-declaree, AUCUNE porte)
  (i) rho sur le sous-ensemble canonique {1.35, sqrt2, 2.00, 2.85} --
      comparaison de forme a M3 (rappel : n=4, p >= 0.042, non testable
      en soi).
  (ii) T_M9 / T_M3 aux quatre canoniques, N = 64 (T_M3 : 4.2597e-3 /
      8.2337e-3 / 1.0636e-2 / 1.7406e-2, S23). Lecture pre-declaree :
      ratios TOUS dans [0.80, 1.25] -> le protocole refait les systemes de
      M3 (offset de code uniforme tolere) ; motif NON uniforme -> ALERTE,
      investigation avant toute interpretation de P-M9a. Comparaison
      croisee entre codes : elle alerte, elle ne conclut pas.

P-M9d  OPERATIONNALISATION (consigne, AUCUNE porte)
  rho(T, C5_min) avec C5 = K5_min/[(w2-1)^2(1+w2)], rapporte a cote.
  K5_min seul est la porte (anti double-dipping).

P-M9-null  PIPELINE (porte)
  FREE (g=0) a w2 = 1.35 et 2.85, N = 64 : T_shell < 1e-12 -> PASSE, sinon
  ARRET. Teste base et recouvrements, pas la dynamique (cf. (d)).

GARDES
------
  G1a ANCRES M3 (bloquantes) : sP ET sM compares aux valeurs de (g) aux
     QUATRE points ancres (1.35, sqrt2, 2.00, 2.85), tolerance +-2 % PAR
     SIGNE. Echec d'un cote -> ARRET, investigation (croise entre codes :
     bloque, ne conclut pas).
  G1b REGRESSION M8 (bloquante) : s*(+1) de M9 vs M8 aux six points,
     tolerance +-2 % (implementations differentes du meme protocole ;
     precedent jet/modes : <= 0.8 %).
  G2 INVARIANCE : K5_min a 2g sur w2 = 1.35 et 2.85 (les DEUX signes a 2g,
     soit 4 recherches), tolerance 10 %, reprise dense sinon ligne EXCLUE.
  G3 IDENTITE DE FORCE : erreur BACKWARD <= 1e-12.
  G4 PAS DE TEMPS : dt/2 sur la ligne qui maximise g_cal x sF^4 (echelle de
     force, lecon M6) ; ecart <= 2 % sinon ligne NON FIABLE.
  G5 CALIBRATION : re-mesure de s* a g_cal ; aux points ou l'asym a
     g = 0.05 depasse 2 %, la re-mesure court les DEUX signes et compare
     s*_min ; |s*_min - s_cible|/s_cible <= 5 % sinon point EXCLU de rho.
  G6 REPRESENTABILITE : queue de l'etat coherent < 1e-8 sinon EXCLU.
  G7 TRONCATURE : T56/T64 par point ET rho(T56, T64), consignes, aucune
     porte ; diagnostic obligatoire si NON CONCLUANT.

PROGRAMME FIGE
--------------
  Classique : carte 6 x 2 signes (12) ; G2 a 2g x 2 signes x 2 points (4) ;
    G5 : 6 en signe sgn_F, doublees (autre signe) aux points d'asym > 2 %
    (attendu +4 a +5, sqrt2 desormais connue a 18 %) ;
    G4 (1). Soit 23 a 28 recherches, passe dense n = 96 partout.
  Quantique : GHOST 6 x {56, 64} (12) ; retourne 6 x {64} (6) ;
    FREE 2 x {64} (2). Soit 20 diagonalisations.
  Cout annonce : ~15 min machine 2.

ENCHAINEMENTS PRE-DECLARES
  CONFIRMEE -> premier soutien puissante ; la conditionnelle p=7 (S17-bis)
    reste armee ; la manche suivante est le redesign p=7, nourri du profil
    C1.
  REFUTEE -> +1.00 de M3 requalifie (legitimement, memes systemes) ET jambe
    quantique morte ; pivot classique (derivation de r, bord droit (3,1)).
  NON CONCLUANT -> C2 : rearme integral. Plus aucune manche quantique sans
    estimateur change et derive.

MES ATTENTES (pour pouvoir avoir tort de mon propre fait)
  Je ne designe PAS d'issue favorite : CONFIRMEE et NON CONCLUANT me
  paraissent comparables. Chiffres : rho canonique +0.6 a +1.0 si le signal
  M3 est reel ; rho 6 points +0.3 a +0.9. T_M9/T_M3 canoniques dans
  [0.85, 1.15], motif uniforme. Asymetries a 1.80 et 2.40 : 5 a 40 %, cote
  fragile possiblement inverse a 1.80 comme a p=7. T_retourne(2.00) : ordre de
  grandeur 1e-12 attendu SI le cote du deplacement (sgn_F(2.00) = -1, la ou
  M8 mesurait +1) ne change pas le canal generique -- sensibilite au cote
  inconnue, consignation quoi qu'il arrive. Exclusions : 0 ou 1.

LIMITATIONS DECLAREES
  - n = 6 au mieux ; mediateur (C vs g_eff) non identifie : test d'un
    SIGNE, pas d'un mecanisme.
  - Ensemble diagonal suppose non degenere (jamais audite) ; parite non
    conservee a p impair.
  - Aucun temoin dynamique borne (cf. (d)).
  - Magnitudes de T non convergees (S8) ; seul le rang est revendique,
    accord des deux troncatures exige.
  - Ne jamais multiplier les p des deux troncatures (correlees).
  - Les comparaisons inter-manches portent leurs etiquettes de convention
    (lecon E20) : tout chiffre de ce gel est min-convention sauf mention.

IMPLEMENTATION
  m9_replication_v1.py, moteurs repris de la lignee m7/m8 machine 1, ecrit
  uniquement out/m9_results.json (incremental). Gel jumeau dans le
  docstring, bloc de "PRE-ENREGISTREMENT M9" a "=== FIN DU GEL M9 ===