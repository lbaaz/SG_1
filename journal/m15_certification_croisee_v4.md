CERTIFICATION CROISEE DU GEL v4 D'HERITAGE (machine 2, 2026-08-10)
==================================================================
Porte sur : m15_pre_enregistrement_v4.md, livre au delta 53 (e6921634b28da9ea),
script patch_gel_m15_v3_to_v4.py (1824de7891db41ae). ASCII/LF ; toutes les
empreintes ci-dessous sont sha256 16 hex, brut = NFC+LF sauf mention.

VERDICT : CERTIFIE. 0 bloquant, 0 echec de controle mecanique.
### 35022c5c0784cb82 ###
(complet : 35022c5c0784cb82fd5b9466d04e289644db3ec3203f29eb5f82bea97661f193,
45294 octets, convention B, brut = NFC+LF.)
Le gel v4 est utilisable par une manche des lors que le script de cette
manche sera certifie sous E19 ; aucun re-parcours de M15 (E29 sect. 7).

1. REJEU DU SCRIPT MACHINE 1 : BIT-IDENTIQUE
   Rejoue en scratchpad (fichiers livres intacts), sources locales par nom,
   les trois empreintes de source asserties par le script ont passe
   (e41f4da3 / 8081a032 / 16c6d86e). Sortie : 45294 octets, 35022c5c,
   cmp au bit avec la livraison : IDENTIQUE. Extraits 709 / 1109 / 2111
   caracteres, conformes au delta 53.

2. AUDIT INDEPENDANT (m15_certification_croisee_v4.py, ec883c2a8352c299 ;
   log 7ba90bc3491f340b ; 0 echec) -- il ne rejoue pas le script, il
   RE-APPLIQUE les regles declarees :
   a. Empreintes re-derivees des 5 fichiers (sources, livraison, erratum v2).
   b. Extractions re-faites, debuts asserts en colonne 0 et uniques ;
      les trois blocs du PORTAGE sont BYTE-VERBATIM egaux aux sources.
   c. Definition E29 RE-APPLIQUEE, pas seulement heritee (lecon M2-a) :
      les temoins passe GROSSIERE, [LO0, 0.90, explosion_sous_LO0_0.90s,
      gros_explosifs, b_fond = 3/96, k_min = 3, n_eff = 24 sont tous dans
      l'extrait P4.1, ASCII pur.
   d. Diff v3 -> v4 juge PAR HUNK (regle du cycle M15) : 4 hunks, chacun
      attribue a un patch declare (A+B contigus en en-tete ; C ; D ; E),
      AUCUN hunk clandestin.
   e. Anciens absents de v4, nouveaux uniques, anciens uniques en v3
      (ancre C = la parenthese REELLE, voir declaration b ci-dessous).
   f. Invariants recomptes : terminateur 1x en derniere ligne, 6 marqueurs
      1x chacun, N-14 absent des extraits, NFC, LF final unique, ASCII
      partout hors des deux extraits NFC declares (N-13, N-15).

3. REDACTIONS MACHINE 1 (point nomme au delta 53.4) : FIDELES
   C (mot N-13) : conforme au texte consigne -- la v2 appliquait la marge
     ABSOLUE ; meme mot, pas la meme regle ; ensemble F identique et six
     points divergents sont les faits exacts de N-13. Le gel ne presente
     plus la lecture normalisee comme celle de machine 2 : la prescription
     est satisfaite.
   D (chiffre N-15) : les trois nombres exiges par la discipline E27 y
     sont, exacts au texte : marge 1.117 contre 1 (N-15 a), probabilite de
     lecture P(n_disc >= 1) = 0.399 (N-15 d), controle positif 1.025
     (N-15 b), avec renvoi P4.3.

4. DECLARATIONS (sans numero -- E18, numerotation a la consignation)
   a. REJOUABILITE WINDOWS : le rejeu du script machine 1 casse sur BOCAL4
      sans PYTHONUTF8=1 -- UnicodeEncodeError cp1252 sur le print de
      provenance de l'extrait N-13 (U+2032 dans "R-2'"), APRES extraction
      reussie, AVANT tout patch. Aucune donnee touchee, aucun chemin de
      calcul : fait d'environnement, meme famille que 51.3.e. Parade
      appliquee sans modifier le script : PYTHONUTF8=1 au rejeu.
   b. CITATION ABREGEE AU DELTA 53 (patch C) : la parenthese reelle de la
      v3 est plus longue que la citation du delta -- elle porte en plus
      ": elle range 2.42, 2.45 et 2.55 sous 5:2." sur deux lignes. Le
      script (ancre dynamique) l'a remplacee ENTIERE et une seule fois ;
      la clause retiree survit en P4.2 ("les deux rangent 2.42, 2.45 et
      2.55 sous 5:2"), verifie mecaniquement. Le patch est conforme ; la
      citation du delta 53.4.C ne doit pas etre re-citee comme texte
      remplace.
   c. ANCRE DE FIN N-15 NON UNIQUE : '\n---\n' apparait 10 fois dans la
      source (separateur de sections) ; la regle declaree est "premiere
      occurrence apres le debut", deterministe sur source gelee par
      empreinte. Consigne pour memoire : une reorganisation de la source
      invaliderait l'ancre -- sans objet tant que 8081a032 fait foi.
   d. PREMIERE PASSE DE MON AUDIT : trois echecs, TOUS de mes propres
      conventions (unicite exigee ou la regle declaree dit "premiere
      apres", off-by-one de fin de bloc, citation delta prise pour le
      texte source) ; ils ont mene aux declarations b et c. Corriges en
      re-appliquant les regles DECLAREES ; trace en transcript de session.

5. RESERVE DU DELTA 51 SUR L'ERRATUM : LEVEE, DEUX FOIS
   Le fichier m15_erratum_grossiere_mordue_v3.md resout desormais
   localement (16c6d86e389da2a9, re-derivee) ET l'annonce "sections 1-7
   bit-identiques a la v2 f4a3508b" est VERIFIEE au bit (la v2 que
   j'avais contre-signee sur le fond).

6. CE QUE CE LOG NE JOUE PAS
   Il ne rejoue aucune mesure de M15 et ne re-certifie ni le gel v3 ni la
   manche close. Il ne verifie pas les dettes d'empreintes .py/.log du
   51.8. Il ne compare pas les redactions C/D a d'autres formulations
   possibles : il verifie leur fidelite aux textes consignes, rien de
   plus. Le rejeu bit-identique (sect. 1) est un fait de session tee au
   transcript, pas une section du .log d'audit. La branche "N-14 vers la
   regle de comptage du script" (53.5) reste a exercer au PROCHAIN script
   de manche : rien ici ne la teste.

=== FIN DE LA CERTIFICATION (gel v4, machine 2) ===
