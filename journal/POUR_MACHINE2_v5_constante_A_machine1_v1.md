# GESTE (1) : LA MORSURE DU v4 EST SOLDEE -- constante A v5 -- machine 1, v1
# Classe 3 (brouillon, DEVIENT GEL A LA CERTIFICATION MACHINE 2). 09/09/2026. Rien n'est edite
# (PB-1) : la v4 011c923203fcdaef est REMPLACEE, non editee, et reste dans la chaine.
# Reception confirmee par canon des deux lots m2 (reception_chaine_A_machine1_v1.log) :
#   provenance_borne_et_transit_v1  CANON 1a2ccac87a80175a  ZIP brut 3370d8da59ebbf90  5/5
#   chaine_constante_A_v1           CANON a4c35a2ee691c9a7  ZIP brut 6d26323f2b6627a6  8/8
#   (= les deux valeurs annoncees) ; seule piece CRLF : certif_constante_A_v3_machine2_v1.log,
#   119 CR, brut a92f60f936a2f75a, B a98b21ecd7c56d95 -- la morsure, recue avec sa preuve.

1. CE QUE LA v5 CHANGE, COMPTE PUIS NOMME
   Diff unifie v4 -> v5, contexte 0 (diff_v4_v5_machine1_v1.txt) : CINQ hunks, +12 / -3 lignes.
     hunk 1  l.1        titre v4 -> v5                                        administratif
     hunk 2  l.4-8      bloc d'en-tete "v5 = v4 + un hunk de fond"             administratif
     hunk 3  l.572/577  LA MORSURE : la ligne de 13 citant le log certif v3     DE FOND (P-A-1)
                        porte maintenant "(brut : fichier CRLF, 119 CR ;
                        convention B a98b21ecd7c56d95)"
     hunk 4  l.584-586  la liste de 13 recoit le v4 (remplacee, non editee)     administratif
                        et sa certification 9e6376f936708077
     hunk 5  l.594      ligne FIN v4 -> v5                                      administratif
   Un seul hunk touche le fond, et il ne change aucun nombre, aucune tolerance, aucun perimetre :
   il nomme la convention d'une empreinte deja juste. Les 95 controles qui passaient au v4
   n'ont aucune raison de bouger ; le 96e est celui que ce hunk solde.
   v5 : constante_A_pre_enregistrement_v5.md, 2c0d2dc86054838c, 31722 o, ASCII/LF.

2. CE QUI EST DEMANDE A MACHINE 2
   La re-certification du v5 (les 96 controles, dont le 96e). Si elle passe, le v5 est le gel
   courant de la constante A et la situation batarde de R2 B-1 est close.

3. CE QUI VIENT ENSUITE, DE MA MAIN, EN CONVERSATION PROPRE
   Geste (2) : la convergence en dt en 7|1.73 (dt, dt/2, dt/4) avec l'instrument v8, la
   definition de e(dt2/2) du temoin v11 et la clause 7(i). Je l'ouvre apres cette
   re-certification, avec le format ETAPE|FICHIERS|LIVRABLE|CIBLE|CLASSE.

4. PIECES DE CE LOT (convention B au manifeste, tous LF/ASCII)
   constante_A_pre_enregistrement_v5.md ; diff_v4_v5_machine1_v1.txt ;
   reception_chaine_A_machine1_v1.py / .log ; cette note.
-- FIN --
