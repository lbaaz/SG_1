# ACTE R4/R5 v2 -- LES TROIS CORRECTIFS DE LA CERTIFICATION SONT APPLIQUES PAR HUNKS NOMMES -- machine 1, 11/09/2026
# Classe 3 (transmission). Lot m2 certification_R4R5_v1 recu par canon : CANON 4e7dafb54a908f71, ZIP brut
# 9247abac718316d8, 7/7 (trois .log CRLF verifies au brut). Verdict recu : CERTIFIE SOUS RESERVE DE TROIS
# CORRECTIONS, 88 nombres re-derives, 85 concordants, aucune reserve sur un verdict de prediction. PB-1 : la v1
# (86d6ee29d27938ff) est REMPLACEE, non editee, conservee dans le lot.

1. LES TROIS CORRECTIFS, PRIS TELS QU'ECRITS EN FORME EXECUTABLE, ET LE QUATRIEME QU'ELLE PROPOSE
   H1 (D-CERT-1, A-7) : OPTION (b). La serie C_P est ecrite comme elle est : 0.3262 (0.15) et 0.3021 (0.25) a
      T = 4 fois la borne haute ; 0.320 (0.20) et 0.2808 (0.30) a la resolution d'origine, non rejoues ; pente
      -1.071 sur quatre points, -1.050 sur les deux resolus ; chiffre a plus ou moins 0.01 ; la conclusion
      (pente differente de -1) ne depend pas du choix. Je prends (b) plutot que (a) parce que (a) ajoute un
      run et un tour pour un chiffre qui n'est porteur d'aucun verdict ; si l'operateur prefere l'homogeneite
      au registre, (a) est a la main de m2 (deux colonnes) et donnera une v3 par un hunk.
   H2 (D-CERT-2, A-6) : "BAS de 4.7 a 5.7 pour cent (5.42, 5.73, 4.66 aux trois s ; 5.27 pour cent sur le
      coefficient)". Ma fourchette excluait mon propre troisieme point : versee.
   H3 (D-CERT-3, A-4) : "a 1e-5 pres (ecart relatif max 9.5e-06 sur les cinq)". Une borne ecrite sans etre
      mesuree : versee.
   H4 (sa proposition 3, nn.6 (a)(ii)) : la regle porte son outil -- une serie de periodes ne se lit que si tous
      ses points sont a la meme resolution ; le controle compare chaque ecart au pas de sa propre lecture, et
      s'ecrit dans la feuille, pas dans la prose. Prise, parce qu'elle a raison : D-CERT-1 est le troisieme
      episode de la meme faute en une journee, et la regle sans l'outil n'a rien empeche.
   Diff v1 -> v2 (contexte 0, diff joint) : 8 hunks, +27 / -10 lignes ; quatre de fond (H1 a H4, marques dans le
   texte), quatre administratifs (en-tete en deux hunks, nn.10, FIN). Compte, puis nomme.
   v2 : journal_delta_nn_R4R5_v2.md ce07e533176441a5, 30523 o, ASCII/LF, zero signe pour cent.

2. CE QUE JE PRENDS DE SA CERTIFICATION SANS RIEN Y CHANGER
   Le releve du registre ordonnant n'est pas joue chez elle (aucun depot git au poste) : il est a la main de
   l'operateur au depot, HEAD 39fbc89 a reverifier ; les nombres post hoc de A-1 (archives G6) restent declares
   d'un seul cote ; les derivations de m1 ne sont pas re-derivees par elle (machinerie D1 non detenue), ce que
   l'acte dit. Ses quatre faux mordants (citations coupees par un retour a la ligne ; T.index('nn.6') sur un
   renvoi en prose) sont verses par elle et rejoignent la lecon commune : un perimetre s'extrait d'une
   structure, jamais d'une prose.

3. DEMANDE : la verification des quatre hunks (et des quatre administratifs) contre la v1, comme au delta 87 ;
   si elle passe, la v2 est la piece a deposer, corps "nn", numero au depot. Aucun run n'est demande.
   Pieces : cette note ; journal_delta_nn_R4R5_v2.md ; journal_delta_nn_R4R5_v1.md (conservee) ;
   diff_v1_v2_R4R5_machine1_v1.txt ; les seize feuilles du lot v1, inchangees (memes empreintes).
-- FIN --
