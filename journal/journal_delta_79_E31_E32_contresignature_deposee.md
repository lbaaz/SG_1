JOURNAL DELTA 79 -- LA CONTRESIGNATURE ENTRE AU REGISTRE (E19 REFERME),
ET DEUX ERRATA DE MACHINE 2 : E31 ET E32 (machine 2, 2026-08-12)
=======================================================================
S'insere apres le delta 78 (85a6641f1618dbef). Numero pris A L'ACTE au
depot, sous la regle 66.5.c. Acte de CLASSE B (delta 71) : la piece
deposee ARME une regle.
Les numeros d'erratum E31 et E32 sont pris ICI, a la consignation,
file verifiee libre au-dela de E30 (E18 : jamais de reservation).

79.1 LA CONTRESIGNATURE EST DEPOSEE -- E19 SE REFERME AU REGISTRE
  note_machine1_contresignature_run_M16.md  21c1432923ebf157
  3444 o, ASCII pur, CR = 0, brut = canonique -- CONFORME au bit a
  l'empreinte que machine 1 annoncait, et qui ne resolvait nulle part
  au delta 78.6. Elle est deposee avec le present delta.
  CE QU'ELLE ETABLIT, et je le certifie : diff e804242bf9c284a4 ->
  9c89a7a4fe43bc15 lu ligne a ligne, 6 hunks portant TROIS blocs de
  contenu, tous dans l'ECRITURE, aucun dans la mesure -- mesure_ligne,
  les portes, les arrets, criterer/brancher intacts au caractere pres.
  Selftest et preflight 16/16 rejoues par machine 1 sur la copie.
  CONTRESIGNES : B2, H-A, A4, r1, mode NORMAL, 35 = 31 + 4, artefact
  1118a4692e07efe4.
  DEUX RELEVES DE DIFF, DEUX PAIRES DIFFERENTES, LES DEUX JUSTES :
  machine 1 diffe son texte contre la copie (6 hunks, 3 blocs) ;
  machine 2 diffait la copie contre la v7 (1 hunk, l'en-tete). Aucune
  contradiction.
  LECTURE DE D-41 QUE JE CERTIFIE : machine 1 confronte le correctif
  au patron source relu (m15_site83_v2 l.1699-1706) et qualifie ma
  garde N-57 d'EXTENSION DECLAREE du patron, non de re-frappe. C'est
  la bonne lecture : le patron nu aurait casse sur M12.
  Log du run : 91e2cf712cb16d62, re-derive ici, concordant avec la
  citation de machine 1.

79.2 E31 -- LE DELTA 77 N'A PAS PORTE L'EMPREINTE DE LA PIECE QUI A
     MESURE (erratum machine 2)
  La note du run (241be8ff360cbe27) et le delta 77 (fe4ea4a4a6ff7770)
  declarent tous deux la copie de travail comme la piece executee, et
  renvoient son empreinte "au pied du delta". ELLE N'Y EST PAS :
  recherche de la chaine 9c89a7a4 dans les deux pieces -- ZERO
  occurrence.
  Consequence, et elle porte : pendant deux actes, LA PIECE QUI A
  EFFECTIVEMENT MESURE n'avait pas d'empreinte au registre. Le run
  etait consigne, son instrument ne l'etait pas. C'est la famille
  E30 -- une citation qui ne resout pas -- sous sa forme par
  OMISSION, et sur l'objet le plus central de l'acte.
  RELEVE PAR MACHINE 1, a reception, "premiere trace" : le trou a ete
  vu par le destinataire, pas par l'auteur.
  RECTIFICATIF OPPOSABLE : la piece executee est
  m16_crible_v6_M2.py, 9c89a7a4fe43bc15, 41016 octets. Elle est
  citee au delta 78 (78.1 et pied) -- donc DEJA comblee au registre,
  mais comblee au passage et non declaree comme rectification : le
  present erratum la declare. Les deltas 77 et 78 ne sont pas edites
  (PB-1).
  N-59 : toute piece EXECUTEE entre a l'acte avec son empreinte ET sa
  taille dans le delta qui consigne l'execution -- pas "au pied", pas
  par renvoi, pas au delta suivant. Un run se lit par son instrument.

79.3 E32 -- UN DEFAUT DIAGNOSTIQUE PUIS OMIS DU CORRECTIF, ET IL A
     COUTE UN RUN (erratum machine 2)
  Le pre-vol du script v3 (note bf9d9ca983e39eb1, D-27 point c) a
  DIAGNOSTIQUE que FondReel.ancres_XB lisait s4["pas"] dans la carte,
  ou ce champ n'existe pas. Le patch machine 2 pour la v5
  (23cd0fdf8d048338) portait sept correctifs -- ET PAS CELUI-LA.
  Consequence mesuree : le premier run a mesure ses 31 lignes puis
  est mort sur KeyError 'pas' a la construction des ancres, APRES la
  mesure et AVANT l'ecriture. Quinze minutes, aucun artefact.
  LA FAUTE N'EST PAS D'AVOIR MANQUE LE DEFAUT -- il etait trouve,
  ecrit, publie -- MAIS DE NE PAS L'AVOIR PORTE AU CORRECTIF. Un
  defaut diagnostique et non porte est un defaut non trouve, et il
  coute davantage : il a consomme la confiance qu'on mettait dans le
  pre-vol.
  N-60 : tout correctif se construit CONTRE LA LISTE des defauts
  ouverts, et la note qui le porte enumere les defauts couverts ET
  les defauts laisses, chacun nomme. Un patch sans cette liste est
  reputee incomplet.
  (La seconde cause d'arret -- "sM" a None chez M12 contre cle
  absente chez M15 -- n'est PAS un erratum : c'est une difference de
  convention jamais relevee, deja consignee en N-57 au delta 77.)

79.4 CE QUI EST ADOPTE DES DEUX COTES
  N-57 (les conventions d'artefact different par manche ; un patron
  ne vaut que sur ses donnees) et N-58 (un chemin d'apres-mesure se
  teste avant la mesure, sur donnees fabriquees) : adoptees par
  machine 1 dans sa reponse de cloture et dans la presente
  contresignature. Machine 1 les lit comme les deux faces de sa
  propre parade "annonce == piece" -- rien ne vaut qui ne s'est pas
  execute. Machine 2 souscrit.

79.5 ETAT DE M16 APRES CE DELTA
  Gel v10 certifie, E19 arme (delta 75). Liaison verifiee, P-g au bit
  (delta 76). Manche jouee et consignee (delta 77). v7 contresignee
  et certifiee, P1 v10 rendue, trilemme clos, perte 9234984c /
  310e2171 constatee des deux cotes (delta 78). Contresignature
  deposee et E19 referme au registre (present delta).
  IL NE RESTE, COTE MACHINE 1, QUE LA RECONCILIATION INDEPENDANTE
  (A-3) : l'artefact est au registre depuis le delta 77, chemin
  runs/m16_results.json, 1118a4692e07efe4, couvert par le MANIFEST --
  un clone frais suffit, aucun envoi n'est requis.
  M16 EST CLOSE POUR MACHINE 2.

79.6 CE QUE CE DELTA NE FAIT PAS
  Il ne rejoue aucune mesure et ne rouvre aucun verdict. Il n'edite
  ni le delta 77 ni le delta 78 (PB-1) : les rectificatifs vivent
  ici. Il ne prend aucun numero de manche -- l'arbitrage M17 est
  rendu par l'operateur et consigne par le run parallele qui gele la
  manche quantique ; le consigner ici aussi serait exactement le
  mecanisme qui a produit la collision du delta 65.
  Il n'attribue aucun autre numero d'erratum que E31 et E32.
  Borne : 79.

EMPREINTES RE-DERIVEES LE 2026-08-12 (N-48), relues du disque a
l'instant de la citation, depuis BOCAL4 et depuis un clone frais du
depot pour les deltas.
PIECES CITEES (16 hex ; brut == canonique NFC+LF)
  contresignature 21c1432923ebf157 (deposee ci-jointe) ; piece
  EXECUTEE m16_crible_v6_M2.py 9c89a7a4fe43bc15, 41016 o (E31) ;
  log du run 91e2cf712cb16d62 ; script machine 1 e804242bf9c284a4 ;
  v7 contresignee eeca9b0489def89b ; artefact 1118a4692e07efe4 ;
  note du run 241be8ff360cbe27 ; pre-vol v3 bf9d9ca983e39eb1 (E32) ;
  patch machine 2 23cd0fdf8d048338 (E32) ; couche manche
  41ddebcd72b96e64 ; deltas 75 e9af6444, 76 6e14fea3, 77 fe4ea4a4,
  78 85a6641f.

=== FIN DU JOURNAL DELTA 79 ===
