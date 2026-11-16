#!/bin/sh
# PRE-VOL de machine 2 (section 11 du gel) : pilote derive (-P), table de pre-vol (C3 deja joue + ancres), sortie dense = depot du delta 98.
S=C:/Users/bazil/AppData/Local/Temp/claude/75adcc7f3c1d08bf/7d33635e-8345-4a2c-a69e-f6a51f9d8fa7/scratchpad
R=D:/devs/bocal/BOCAL4
L=$R/livraison_16a_gel_loi_partie2/ext/lot_m1
J=$S/reg_neuf98/journal
cd $R/certif_gel_loi_partie2_machine2
py -3.11 -P pilote_gel_loi_machine2_v2.py $L $S/reg_neuf98/scripts/m17_chaine_v17.py $S/reg_neuf98/scripts/chaine_ordre2_bloc_machine1_v1.py $L/ordre3_bloc_machine1_v1.py \
  $J/sonde_ordre2.json $J/tp_retenus_machine2_v1.json $J/tp_reference_machine2_v1.json $R/certif_EB_ter/lot_m1/reference_ancres_ter_machine1_v1.json \
  $L/table_points_prevol_gel_loi_ordre3_v1.json $R/certif_gel_loi_partie2_machine2/prevol 12 --prevol --dense $J/sonde_ordre2.json
