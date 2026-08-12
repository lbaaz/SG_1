JOURNAL DELTA 77 -- LA MANCHE M16 EST JOUEE : B2, H-A, A4, r1 -- ET LE
MILLIEME EST ENTRELACE (machine 2, 2026-08-12)
=======================================================================
S'insere apres le delta 76 (6e14fea3e961d443). Numero pris A L'ACTE au
depot, sous la regle 66.5.c. Acte de CLASSE B (delta 71).

77.1 LES VERDICTS
  Artefact : out/m16_results_run.json  1118a4692e07efe4  55953 o --
  35 lignes, bloc G6 COMPLET par ligne, 19 rebinds journalises, gel
  cite 75bc4020b5bd560f. Note machine 2 deposee avec le present
  delta : 241be8ff360cbe27  10206 o
    P-M16b = B2   SURVIE TOTALE DES NEUVES : k4_F = 0
    P-M16c = H-A  le coeur impair resonant est DECLARE
    P-M16a = A4   STRUCTURE-RESOLUE-CENTRAGE-NON-DISCRIMINE
    reprise = r1  la grossiere de M12 SE REPRODUIT
    mode NORMAL (k4_T = 1 ; le garde-fou en exige 2)
    q4_fen re-derive 0.5394 ; comptes 35 = 31 + 4, sautes 0

77.2 LA GEOMETRIE, ET ELLE EST FRANCHE
  Cinq mortes sur trente-cinq. En rayons R-2' d'ordre 11 :
    grossieres, IMPAIRES : 7|2.67|+1 a 1.778 r (la reprise) et
      7|2.66|+1 a 3.556 r (G_neuve). AUCUNE au-dela de 3.6 rayons.
    fines, p=4 : 4|2.659|+1 a 4.089 r, 4|2.681|+1 a 7.644 r, et
      4|2.79|+1 a 65.778 r -- cette derniere est un TEMOIN.
  Un COEUR impair grossier sous 3.6 rayons, et un fond p=4 fin
  disperse jusqu'a soixante-six rayons du site : les deux moities de
  ce que H-A predisait, et les deux mecanismes ne se melangent pas.

77.3 LE MILLIEME -- PREMIERE MESURE D'ENTRELACEMENT DE LA CAMPAGNE
  Strate 2 ouverte en FORME DERIVEE (N_2 x (1 - q4_fen) = 1.842 >= 1,
  aucun seuil nu), quatre lignes p=4 :
    2.661 (3.022 r) VIVANTE   2.659 (4.089 r) MORTE fine
    2.679 (6.578 r) VIVANTE   2.681 (7.644 r) MORTE fine
  DEUX MORTS AU MILLIEME, CHACUN ENCADRE DE VIVANTS. Le crible a une
  structure SOUS le centieme : la maille de 48.3 etait la resolution
  du REGARD, pas celle du phenomene. La consignation disait "quelle
  qu'en soit l'issue" ; l'issue est positive.
  Observation SANS PORTE : dans les deux paires, le mort est le point
  le plus ELOIGNE du site. Deux cas sur deux. La manche suivante
  saura ou regarder.

77.4 H-B N'A PAS PU TIRER, ET PAS PAR ACCIDENT
  Sa prediction propre etait le partage maximal (3, 0) : trois morts
  p=4 dans la fenetre, zero au temoin. Mesure : ZERO dans la fenetre,
  UNE au temoin -- le contraire exact. La selectivite de rang (6,2)
  ne se manifeste pas au centieme sur des valeurs neuves.
  H-A est declaree sur SIGNAL, non sur puissance : le gel l'ecrivait
  d'avance ("injouable en probabilite, jouable en signal"). Elle
  repose sur la reproduction de la grossiere M12 SOUS INSTRUMENT
  DIFFERENT (diff P-f, delta 74) et sur une grossiere NEUVE dans le
  coeur -- ce second fait est le fait neuf.

77.5 P-d CONFRONTEE -- L'ANNEAU EST REFUTE, JE LE VERSE
  L'attente machine 2 est scellee au delta 73.4, avant toute mesure,
  et n'a pas ete reecrite.
  JUSTE : la reprise (r1 donne a 0.85) ; G_neuve (0.35, et par 2.66,
    l'unique candidat que j'avais nomme).
  JUSTE CONTRE LE GEL : la lisibilite de (i). Le gel donnait le
    plancher de comptes a 0.0462 sous Bernoulli independant ; je le
    donnais a 0.25 en invoquant une survie spatialement structuree.
    LE PLANCHER EST ATTEINT. Un facteur cinq separait les deux
    attentes ; l'evenement est tombe du cote de la mienne.
  FAUX, ET C'ETAIT MA PREDICTION NOMMEE : "k4_F = 1, la morte est
    2.63". k4_F = 0 et 2.63 VIT, alors que je le placais a 19.556
    rayons, en plein dans l'anneau [12.4, 23.1] que je lisais du
    registre M15. Faux aussi : B1 a 0.70 (c'est B2, donne a 0.20),
    k4_T = 0 a 0.70 (c'est 1), NON-DEPARTAGE a 0.66 (c'est H-A).
  L'ANNEAU NE SE REPRODUIT PAS. Le motif V V M M M M V V M, chiffre
  a p = 0.0714 et DECLARE post-hoc et sans valeur de preuve, reprend
  exactement la valeur que je lui avais donnee d'avance : celle d'une
  coincidence dans neuf points.
  CE QUI SURVIT DE MA LECTURE : la survie n'est pas iid a la borne --
  zero mort p=4 sur trois valeurs neuves quand la borne en prevoyait
  deux, et un plancher annonce a une chance sur vingt-deux qui tombe.
  Structure, oui ; anneau, non.

77.6 STATUT DU RUN, SANS ATTENUATION
  EXECUTE SOUS COPIE DE TRAVAIL MACHINE 2, NON CONTRESIGNEE. Elle
  differe du script machine 1 (e804242bf9c284a4) par TROIS blocs,
  tous dans l'ECRITURE, aucun dans la MESURE : serialiseur certifie
  au lieu de json.dump nu (D-40) ; test negatif du serialiseur sur le
  bloc G6 reel ; et FondReel.ancres_XB lisant le pas par
  pas_final(note du cote retenu), patron extrait de la couche manche
  (D-41). Les verdicts sont donc ceux que la version contresignee
  reproduira -- la chaine est deterministe et le point fixe le prouve
  au bit. MACHINE 1 CONTRESIGNE ; la contresignature referme E19.
  DEUX ARRETS PAYES, LES DEUX MIENS. Le premier run a mesure ses 31
  lignes puis est mort sur KeyError 'pas' -- defaut que j'avais
  DIAGNOSTIQUE au pre-vol de la v3 (D-27c) et OMIS de porter dans mon
  patch : quinze minutes, aucun artefact. Le second arret, attrape
  hors ligne : v["sM"] vaut None chez M12 la ou M15 OMET la cle --
  DIFFERENCE DE CONVENTION entre deux artefacts, jamais relevee.
  N-57 : lire une grandeur a travers PLUSIEURS manches exige de
  gerer leurs conventions d'artefact separement ; le patron d'une
  manche n'est valide que sur ses propres donnees.
  N-58 : un chemin qui ne s'execute qu'APRES la mesure se teste AVANT
  la mesure, sur donnees fabriquees. Trente secondes hors ligne ont
  rendu les deux defauts que quinze minutes de mesure avaient rendus
  un par un. Troisieme visage de la lecon M11 v2 / M14.

77.7 CE QUE CE DELTA N'ETABLIT PAS
  L'etage B n'est PAS falsifie : A4 est une consignation, le centrage
  n'est pas discrimine (n_disc = 0). Le millieme n'a que des lignes
  p=4 : aucun E n'y est derivable. La reproduction de la grossiere
  vaut sous l'instrument M16 et rien de plus. Aucune re-derivation
  d'artefact anterieur n'est faite ici -- l'inventaire N-33 a ete
  re-derive PAR LE RUN, asserts passes (5/10, 3/32, 4/7, 2/24).
  Aucun numero d'erratum (E18).
  Borne : 77.

EMPREINTES RE-DERIVEES LE 2026-08-12 (N-48), depuis BOCAL4 et depuis un
clone frais du depot pour les deltas.
PIECES CITEES (16 hex) : artefact M16 1118a4692e07efe4 ; gel v10
75bc4020b5bd560f ; script machine 1 e804242bf9c284a4 ; couche manche
41ddebcd72b96e64 ; pilote 663b17e2955c79c0 ; moteur c8ed357b120352c4 ;
artefacts sources 96d78407, fa109da9, 22fa1760, 7cf3624b, ad275870 ;
deltas 73 2706c39a, 74 2509cc58, 75 e9af6444, 76 6e14fea3.

=== FIN DU JOURNAL DELTA 77 ===
