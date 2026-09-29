# ERRATUM AU MANIFESTE DU LOT lot_machine1_2026-09-18_gel_v9_banc_v15_v1 (canon 1f1d56d351e352dc)
# machine 1, v1, 29/09/2026. Demande par la certification machine 2 du v9/v15 (b5568d8f31f8492e,
# morsure 6.5 = E-v9-1). Aucun canon ne bouge : le manifeste, ses treize pieces, le gel v9
# (b515abc5a6da73c5) et l'instrument v15 (a1553f6eb5cc74b8) restent tels qu'emis et certifies.

CE QUI EST FAUX : la ligne d'en-tete du manifeste et la section 0 de la note
note_machine1_gel_v9_banc_v15_v1.md (630be06efa686b38) portent "selftest 103/103 ; banc 103/103".
CE QUI EST VRAI : le banc qui tue du v15 rend 58/58 scenarios mordent, 17 gardes enumerees et
demontrees -- journal m1_v15_banc.log du lot, ligne [0447] ; la note le dit correctement en
section 3, et machine 2 rend 58/58 sur BOCAL4.
CAUSE, MESUREE : la fabrique du lot lisait le compte au journal par le motif "bilan N/N" ; or
le banc rejoue le selftest AVANT ses scenarios, et son journal porte DEUX lignes "bilan" --
[0121] SELFTEST bilan 103/103, puis [0447] BANC bilan 58/58 scenarios mordent. Le motif a
pris la premiere. Un compte lu au journal ne suffit pas : il se lit a la ligne QUI LE PORTE
(motif "bilan N/N scenarios mordent" pour le banc) -- meme famille que D-G2-4 (un compte lu
au mauvais endroit) et que ma faute du 13/09 (un compte ecrit avant la lecture du log).
PORTEE : aucune. Le compte faux n'est cite par aucun acte ; la certification machine 2 tient
telle quelle ; le present erratum s'archive avec le lot et se cite avec lui.

-- FIN ERRATUM_manifeste_lot_gel_v9_banc_v15_machine1_v1 --
