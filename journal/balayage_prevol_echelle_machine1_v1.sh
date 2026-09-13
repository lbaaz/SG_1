#!/bin/sh
for n in 24 22 18 19 21 23; do D=/home/claude/scan_n$n; rm -rf $D; mkdir -p $D
python3 /home/claude/v6/construction_gel_v6_et_banc_v9_machine1_v1.py /home/claude/reliv/entrant_machine1_2026-09-09_constante_A_v5/constante_A_pre_enregistrement_v5.md /home/claude/reliv/chaine_constante_A_pour_machine1/banc_qualification_machine1_v8.py $D $n > $D/construction.log 2>&1
R=$D/registre; mkdir -p $R; cp -r /home/claude/SG_1c/. $R/; cp $D/constante_A_pre_enregistrement_v6.md $R/gels/
grep -n "^DELTA = " $D/banc_qualification_machine1_v9.py >> $D/construction.log
cd $R && NPY_DISABLE_CPU_FEATURES=X86_V4 timeout 900 python3 $D/banc_qualification_machine1_v9.py --prevol --mode temoin --registre $R --sortie $D/out_prevol > $D/prevol.log 2>&1
echo "n=$n fini rc=$?" >> /home/claude/scan_etat.txt
done
echo "SCAN FINI" >> /home/claude/scan_etat.txt
