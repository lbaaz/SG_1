#!/bin/sh
# lance la verification des nombres et sa contre-epreuve (14 corruptions du gel), chemins explicites
S=C:/Users/bazil/AppData/Local/Temp/claude/75adcc7f3c1d08bf/7d33635e-8345-4a2c-a69e-f6a51f9d8fa7/scratchpad/reg_neuf98
L=../livraison_16a_gel_loi_partie2/ext/lot_m1
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
cd /d/devs/bocal/BOCAL4/certif_gel_loi_partie2_machine2
py -3.11 -P verification_nombres_gel_machine2_v1.py $S/scripts/m17_chaine_v17.py $S/scripts/chaine_ordre2_bloc_machine1_v1.py ../controle_ordre3_machine2/ordre3_machine2_v1.py $L/gel_loi_ordre3_partie2_instrument_enonces_pre_enregistrement_v1.md $L/table_points_gel_loi_ordre3_v1.json retro_machine2_v1.json $L/table_retrospective_v1.json $S/journal/sonde_ordre2.json ../certif_EB_ter/lot_m1/lecture_qualification_EB_ter_machine1_v1.py ../certif_EB_ter/lot_m1/reference_ancres_ter_machine1_v1.json verification_nombres_gel_machine2_v1.json > verification_nombres_gel_machine2_v1.log 2>&1 &
rm -rf contre_epreuve_nombres_travail
py -3.11 -P contre_epreuve_nombres_gel_machine2_v1.py $L/gel_loi_ordre3_partie2_instrument_enonces_pre_enregistrement_v1.md contre_epreuve_nombres_travail contre_epreuve_nombres_gel_machine2_v1.json -- $L/table_points_gel_loi_ordre3_v1.json retro_machine2_v1.json $L/table_retrospective_v1.json $S/journal/sonde_ordre2.json ../certif_EB_ter/lot_m1/lecture_qualification_EB_ter_machine1_v1.py ../certif_EB_ter/lot_m1/reference_ancres_ter_machine1_v1.json $S/scripts/m17_chaine_v17.py $S/scripts/chaine_ordre2_bloc_machine1_v1.py ../controle_ordre3_machine2/ordre3_machine2_v1.py > contre_epreuve_nombres_gel_machine2_v1.log 2>&1
wait
