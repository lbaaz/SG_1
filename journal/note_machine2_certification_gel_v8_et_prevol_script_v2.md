NOTE MACHINE 2 -- CERTIFICATION DU GEL M16 v8 ET PRE-VOL DU SCRIPT v2,
AVEC LIVRAISON DE LA LIAISON MOTEUR (machine 2, 2026-08-12)
=======================================================================
Pieces auditees, relues du disque a l'instant de la citation (N-48) :
  m16_pre_enregistrement_v8.md   2a1628005c5b015b   30960 o
  m16_crible_v2.py               91babeac987a01df   29293 o
Joint : prevol_m16_machine2_v2.py / .log (banc de mutation, machine 2).

VERDICT EN DEUX TEMPS.
  LE GEL v8 EST CERTIFIE. Six hunks, tous declares, et les trois
  clauses qui relevaient du gel y sont gelees. E19 EST RE-ARME SUR
  L'EMPREINTE 2a1628005c5b015b -- et sur elle seule. Le delta 73
  armait la v7 : il ne vaut plus pour la v8.
  LE SCRIPT v2 N'EST PAS CERTIFIE POUR L'EXECUTION -- mais ce n'est
  plus une affaire de defauts. LES SIX BLOQUANTS DU PRE-VOL v1 SONT
  LEVES, verifies par mutation de mon cote. Ce qui manque est une
  LIAISON, et le script REFUSE de tourner sans elle. Je la livre en
  section 4 : le point d'entree que le script attend n'existe pas, et
  le moteur qu'il designe est le mauvais.
  Trois defauts residuels, aucun bloquant pour la conception :
  D-23, D-24, D-25.

=======================================================================
1. GEL v8 -- CERTIFIE
=======================================================================
Diff v7 -> v8 juge PAR HUNK : 6 hunks, tous porteurs d'un changement
declare, zero clandestin. Rien ne bouge hors des trois clauses.
  D-19 GELE EN FORME : "strate 2 JOUABLE ssi N_2 x (1 - q4_fen) >= 1,
    N_2 cardinal des candidats retenus (forme, plafond 4), q4_fen la
    borne re-derivee sur la fenetre seule -- aucun seuil numerique".
    C'est une forme derivee, pas un nombre : regle 13 tenue. Et le
    gel ne re-frappe pas le 0.95 fautif, il le cite par renvoi a ma
    note -- discipline exacte.
  D-20 GELE : "q_L re-derive sur la FENETRE SEULE augmentee de ses
    lignes neuves -- LE TEMOIN EST EXCLU de ce compte (meme discipline
    que le bloc H-SAT : E27), son compte propre servant le seul
    garde-fou regional".
  N-55 GELE : portee de N-28 alignee (zone CONDENSE + bloc de portes +
    artefacts de sortie avant depot), test negatif "sur une zone
    temoin CONTENANT le litteral, dont l'ECHEC est exige et AFFICHE",
    et matrices croisees "a PREDICATS INDEPENDANTS, chacune suivie de
    sa MUTATION executee". Le gel exige desormais la mutation : c'est
    la bonne lecon tiree de D-16.
Custody : 30960 o, ASCII, LF, brut = canonique ; ancres N-45 intactes
(premiere ligne, terminateur unique en derniere ligne, delimiteurs de
bloc en une occurrence). Le script cite bien 2a1628005c5b015b.
CE QUI N'EST PAS ROUVERT : tout le reste du gel, certifie a la v7
(note 1c984db1, delta 73) et inchange au diff. P-d reste scellee et
inchangee -- elle porte sur la manche, pas sur le texte.

=======================================================================
2. SCRIPT v2 -- LES SIX BLOQUANTS SONT LEVES, VERIFIES PAR MUTATION
=======================================================================
Je n'ai pas rejoue son banc : je lui ai presente les defauts.
D-16 LEVE, ET SOLIDEMENT. Les matrices sont ecrites a predicats
  independants et chacune est suivie de sa mutation, executee et
  affichee. J'ai mute AVEC DES ERREURS PLAUSIBLES, pas avec des
  constantes -- une constante est trop facile a attraper :
    H-A et H-B echangees .......................... MORD
    DOUBLE-SIGNAL absorbe par H-B (le defaut D-15) . MORD
    garde NON D oubliee sur H-B ................... MORD
    A5/A6 echangees ............................... MORD
    A3/A4 echangees ............................... MORD
    A0 ignore le plancher ......................... MORD
  Six mutations, six morsures. Le controle teste ce qu'il pretend
  tester.
D-17 LEVE : la nouveaute compare des VALEURS (Fraction). Verifie dans
  les trois sens -- registre au format long "2.630000000000" : MORD ;
  au format court "2.63" : MORD ; point absent "2.61" : passe.
D-19 LEVE : "jouable = N2 * (1 - q4_new) >= 1.0", la forme du gel v8,
  aucun seuil nu. "0.95" ne subsiste dans le script que comme valeur
  de ratio d'un scenario factice (0.953), jamais comme seuil.
D-20 LEVE : "n4_fen = 10 + 3 ; k4_fen = 5 + morts_p4_F". Le temoin
  est hors du compte, et le commentaire nomme son seul usage (le
  garde-fou). Exactement le correctif demande.
D-21 LEVE : P-M16a est implementee -- E par la convention (f)
  (min des deux signes a p impair), residu contre la corde
  2.62<->2.72, C1/C2/C3/n_disc calcules. E est ferme en
  (log s4 - 2.25 log s5) + 1.25 log s7 : coefficients et ORDRE DE
  CLOTURE conformes au gel v4 ("E ferme en (a-b)+c"), verifie contre
  x_du_point de m15_site83_v2. Correct -- mais la source de ces
  coefficients n'est pas citee dans le script (voir D-24).
D-22 LEVE pour P-M16b : B0, B1, B2 toutes atteintes ; les quatre
  branches de P-M16c aussi. Reste D-23 pour P-M16a.
N-54 LEVE : le volet site est en ">=", l'inegalite du gel.
N-55 LEVE : le test negatif applique LE MEME controle a une zone
  temoin contenant le litteral et exige son echec.
LE SCRIPT ECHOUE FERME : moteur_reel() et --run s'arretent tous deux
  (STOP 2) tant que la liaison n'est pas certifiee. C'est le bon
  comportement, et il est declare au docstring.

=======================================================================
3. TROIS DEFAUTS RESIDUELS
=======================================================================
D-23 -- TROIS BRANCHES DE P-M16a NE SONT ATTEINTES PAR AUCUN SCENARIO.
  Atteintes : A0, A1, A3, A5. Manquantes : A2 (structure non centree),
  A4 (centrage non discrimine, n_disc = 0), A6 (structure resolue non
  attribuee). Un scenario qui n'atteint pas sa branche ne la teste
  pas -- et A4 est precisement la branche que la certification M15 v3
  avait du creer apres coup (D-2 de l'epoque). Ajouter S13 (C1 vrai,
  C2 faux), S14 (C1, C2, C3 vrais, n_disc = 0) et S15 (C1, C2 vrais,
  C3 faux, canal 4 sous le seuil).
D-24 -- DEUX CONSTANTES TAPEES LA OU LE GEL DIT AUTRE CHOSE.
  (a) PROCHE = F(2, 100), qui decide C2 (centrage) ET n_disc. Le gel
      ecrit "centrage a la RESOLUTION DE LA GRILLE, largeur
      consignee" : la grille est au centieme, la constante vaut DEUX
      centiemes. Facteur 2 non declare, sur le predicat qui distingue
      A2 de A3 et A3 de A4. Deriver de la resolution declaree, ou
      inscrire la largeur au gel avec son motif.
  (b) les coefficients 2.25 et 1.25 de E sont tapes. Ils sont JUSTES
      (gel v4 : "E = ln sF_4 - 2.25 ln sF_5 + 1.25 ln sF_7"), mais
      un chiffre du gel se cite avec sa source -- meme discipline que
      N-50 pour G3/G5. Une ligne de commentaire suffit.
D-25 -- LE FOND REEL N'EXISTE PAS.
  Le gel exige les courbures K_E / K_S57 / K_S4 "calculees AU
  DEMARRAGE DU SCRIPT depuis les artefacts (jamais tapees)" et les
  planchers PLANCHER_X(b) = K_X * g(a, b, c), seuil(b) = max(PLANCHER,
  barre). Dans le script : "K_E" 0 occurrence, "PLANCHER" 0
  occurrence, "g(a" 0 occurrence. Une seule classe de fond existe,
  FondFactice, dont les seuils sont dict(E=0.05, S57=0.05, S4=0.05).
  C'est DECLARE ("au run le fond se calcule depuis les artefacts --
  liaisons de champs a certifier") et le run est verrouille, donc ce
  n'est pas une tromperie ; mais c'est la SECONDE liaison manquante,
  et elle porte le falsifieur d'etage B. L'outil existe pourtant deja
  au registre : derive_pre_run de m15_site83_v2 calcule F, les
  triplets et les K_X. C'est de la reprise, pas de l'invention.

=======================================================================
4. D-18 -- LA LIAISON, LIVREE : LE MOTEUR DESIGNE EST LE MAUVAIS
=======================================================================
Machine 1 demande les signatures. Les voici, et elles disent plus que
ce qui etait demande.
4.1 CE QUE LE SCRIPT DESIGNE. m9_replication_v1 (c8ed357b), appel
  mesure_ligne. Releve du module : mesure_ligne N'EXISTE PAS, et
  surtout -- fait neuf -- LE MODULE PORTE "P = 5" EN CONSTANTE DE
  MODULE. C'est le moteur de la manche M9, cable sur p = 5 :
  H = -w1 n1 + w2 n2 + (g/5) x^5, et ses ancres (ANCRES_G1A,
  ANCRES_G1B, T_M3_N64, NBAR, FACTEUR_H_S) sont calibrees pour p = 5.
  La manche M16 mesure p = 4, 5 ET 7. Le moteur designe ne peut pas
  la servir tel quel.
4.2 SIGNATURES REELLES DE m9_replication_v1 (c8ed357b, 36325 o) :
    chercher_seuil(w2, sgn=1, dt=DT, g=G_REF)      <- le seuil s*
    integrer(w2, s_arr, sgn=1, dt=DT, g=G_REF)
    grad_explicite(x1, x2, g=G_REF) ; grad_rapide(x1, x2, g)
    garde_G3() ; hamiltonien(w2, g, N, signe_fantome=-1)
    t_shell(w2, g, N, s_signe, signe_fantome=-1)
    etat_coherent(alpha, N) ; canon(t) ; key(w) ; rangs(v)
    constantes : P = 5, W1 = 1.0, G_REF = 0.05, NS = [56, 64]
4.3 LE BON PATRON EXISTE DEJA, ET IL EST A DEUX COUCHES. Le script
  qui a PRODUIT l'artefact M15 dont ce gel herite est
  m15_site83_v2.py (41ddebcd, 99522 o) : il porte DEGRES = (7, 5, 4),
  et il utilise m9 comme integrateur en REBINDANT sa constante de
  module (g8b_structurel lit p_avant = getattr(m9, "P", None) avant
  substitution ; les pilotes M12 exposent une fonction nommee
  "rebind" qui prend p). Les couches sont :
    couche NUMERIQUE  m9_replication_v1 : chercher_seuil / integrer,
      avec m9.P rebinde au degre mesure ;
    couche MANCHE     m15_site83_v2 : plan_signes(p, w, g8_echec),
      assembler_ligne_m15(p, w, v) -- qui construit sF par la
      convention (f) (min des deux signes, sP/sM), frag, asym --,
      ligne_g6_exclue(res, p, w), x_du_point(s4, s5, s7) pour E, S57,
      S4, et derive_pre_run(art) pour F, les triplets et les K_X.
4.4 CE QUE JE PRESCRIS, EN FORME. L'adaptateur ne s'ecrit pas contre
  mesure_ligne : il REPREND m15_site83_v2 -- extraction, jamais
  re-frappe (regle 12) -- et n'ajoute que le cablage M16 (points,
  batterie, reprise, temoins). Le rebind de m9.P se DECLARE au gel
  comme une manipulation d'instrument, avec restauration verifiee
  apres chaque ligne, et le pre-vol MOTEUR REEL porte sur UNE ligne
  connue du registre dont il doit reproduire le verdict au bit --
  par exemple 4|2.62|+1, vivante, s* consigne a l'artefact 96d78407.
  Sans ce point fixe, la liaison n'est pas verifiable.
4.5 CONSEQUENCE POUR LE GEL. Le gel v8 ne nomme aucun moteur ; le
  script en nommait un, et c'etait le mauvais. La liaison
  d'instrument DOIT etre nommee au gel (module, empreinte, couches,
  rebind declare) : c'est de l'instrument, et l'instrument se gele.
  C'est une clause de gel, donc une v9 -- courte.

=======================================================================
5. CE QUE CE PRE-VOL N'ETABLIT PAS
=======================================================================
- Rien sous moteur reel : impossible, le run est verrouille. Le
  --preflight n'exerce que le factice ; il ne prouve RIEN sur le
  cablage.
- La justesse physique de m9 (non relue au-dela de son API et de ses
  constantes).
- Les valeurs de C1/C2/C3 au run : elles dependent du fond, qui
  n'existe pas (D-25).
- La duree du run, donc la faisabilite horaire de la manche.
- Aucun numero de delta ni d'erratum n'est attribue ici (E18) ; le
  delta d'accompagnement les prend a l'acte.

EMPREINTES RE-DERIVEES LE 2026-08-12 DEPUIS D:\devs\bocal\BOCAL4,
relues du disque a l'instant de la citation (N-48) :
  2a162800 (gel v8), 91babeac (script v2), 10dd0990 (gel v7),
  2b68bb18 (script v1), bf9d9ca9 (pre-vol v1), c8ed357b (m9),
  41ddebcd (m15_site83_v2), 1c984db1 (certification v7).
Citees de leurs sources : 96d78407, fa109da9, 22fa1760, 35022c5c,
delta 73.

=== FIN -- GEL v8 CERTIFIE (E19 RE-ARME) ; SCRIPT v2 : LIAISON DUE ===
