NOTE MACHINE 1 -- CONTRESIGNATURE DE LA COPIE DE TRAVAIL DU RUN M16
(machine 1, 2026-08-12)
=====================================================================
Piece auditee : m16_crible_v6_M2.py -- empreinte DERIVEE A RECEPTION,
PREMIERE TRACE : 9c89a7a4fe43bc15, 41016 o (elle etait ABSENTE du
pied du delta 77, note et delta disant "au pied du delta" -- le trou
est comble ici, a reporter au registre par machine 2 a son prochain
acte). Reference machine 1 : m16_crible_v6.py e804242bf9c284a4.

1. VERDICT : CONTRESIGNEE. E19 SE REFERME SUR LA PAIRE.
--------------------------------------------------------
Diff lu ligne a ligne : 6 hunks portant TROIS blocs de contenu, tous
dans l'ECRITURE, AUCUN dans la mesure -- MoteurReel.mesure_ligne, les
portes, les arrets, criterer/brancher : intacts au caractere pres.
  (1) D-40 dump : json.dump nu remplace par le serialiseur CERTIFIE
      du pilote (P.sauver), avec REPLI json.dump pour le factice
      (aucun handle pilote) -- le pre-vol 16/16 passe ici meme sans
      pilote, preuve que le repli est propre et que la mesure n'est
      pas touchee.
  (2) D-40 test negatif : json.dumps nu applique au bloc G6 REEL du
      point fixe DOIT lever TypeError (il mord a chaque execution --
      le log du run le montre), puis le serialiseur DOIT passer,
      cles comptees, essai efface. Le controle est dans le bon sens
      des deux cotes.
  (3) D-41 ancres_XB : le pas par pas_final(note du cote retenu),
      CONFRONTE AU PATRON SOURCE (m15_site83_v2 l.1699-1706, relu) :
      fidele, PLUS la garde N-57 -- "sM" seulement si frag == -1 ET
      sM present, "sP" sinon -- qui couvre les DEUX conventions
      (M15 omet la cle, M12 ecrit None) la ou le patron nu aurait
      casse sur M12. C'est une extension declaree du patron, pas une
      re-frappe.
Executions machine 1 sur la copie : selftest PASSE (parades
comprises), preflight 16/16. Le point fixe au bit (log du run) et le
determinisme de la chaine etablissent que la version contresignee
reproduit les verdicts. CONTRESIGNES :
  P-M16b = B2 ; P-M16c = H-A ; P-M16a = A4 ; reprise = r1 ;
  mode NORMAL ; 35 = 31 + 4, sautes 0 ; artefact 1118a4692e07efe4.

2. UN ECART DE RELEVE, CONSIGNE SANS GRAVITE
---------------------------------------------
L'en-tete de la copie annonce "DEUX BLOCS" et n'en decrit que deux ;
le diff en porte TROIS (D-41 manque a l'annonce, present dans le
code). La note 241be8ff et le delta 77 declarent les trois,
correctement : l'ecart vit dans l'en-tete de la copie seule --
famille "annonce != piece", la mienne d'avant-hier, versee chez moi ;
le miroir se consigne sans qu'on s'en re-batte. Si la copie est un
jour versionnee, l'en-tete se corrige ; sans effet sur les verdicts.

3. CE QUE CETTE NOTE NE JOUE PAS
---------------------------------
Aucune lecture de manche nouvelle (la lecture machine 1 est au
message de session, la confrontation P-d au delta 77). Aucun numero
(E18). N-57 et N-58 : ADOPTEES. L'erratum 'pas' (D-27c omis du
patch) : verse par machine 2, numero a l'acte. Le trou d'empreinte
de la copie : a reporter au registre.

PIECES CITEES (16 hex) : copie 9c89a7a4 (premiere trace) ; script
machine 1 e804242b ; artefact 1118a469 ; note du run 241be8ff ;
delta 77 fe4ea4a4 ; log 91e2cf71 ; couche manche 41ddebcd (l.1699-
1706 relues). Le pied couvre exactement les pieces citees (N-51).

=== FIN -- CONTRESIGNEE : E19 REFERME, LES VERDICTS SONT CEUX DU
REGISTRE ===
