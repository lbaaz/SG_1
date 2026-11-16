#!/bin/sh
# usage : lancer.sh <mode>   (depuis BOCAL4)
S=C:/Users/bazil/AppData/Local/Temp/claude/75adcc7f3c1d08bf/7d33635e-8345-4a2c-a69e-f6a51f9d8fa7/scratchpad
J=$S/reg_neuf98/journal
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
py -3.11 -P certif_EB_ter/lot_m1/sonde_qualification_EB_ter_machine1_v1.py m17_chaine_v17.py $J/sonde_ordre2.json $J/tp_retenus_machine2_v1.json certif_EB_ter/prevol "$1"
