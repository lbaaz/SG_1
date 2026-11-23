#!/bin/bash
# Variante de lance_lect2D_machine2_v2_abs.sh (non editee), seule difference : le nombre de processus simultanes est un 5e argument facultatif (defaut 8) ; ancienne variante de lance_lect2D_machine2_v1.sh (non editee) : une ligne de jobs = un processus (une cellule, un signe, UN SOUS-ENSEMBLE d'absorbeurs, option --abs deja prevue et documentee par le pilote), 8 processus a la fois.
# Usage : bash lance_lect2D_machine2_v3_abs.sh <jobs.txt> <dossier de sortie> <moteur> <bloc source> [nombre de processus]
# jobs.txt : ID W2 G M ETA0 SIGNE RC ABS   (ABS = lettres parmi ABCD)
JOBS="$1"; OUT="$2"; MOTEUR="$3"; BLOC="$4"
ICI="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$OUT"
export JOBS_ICI="$ICI" JOBS_OUT="$OUT" JOBS_MOTEUR="$MOTEUR" JOBS_BLOC="$BLOC"
cat "$JOBS" | xargs -P "${5:-8}" -L 1 bash -c '
id="$0"; w2="$1"; g="$2"; m="$3"; eta0="$4"; signe="$5"; rc="$6"; ab="$7"
[ "$signe" = "1" ] && qui="jumeau" || qui="fantome"
py -3.11 -P "$JOBS_ICI/lecteur_2D_pilote_machine2_v1.py" "$JOBS_MOTEUR" "$JOBS_BLOC" "$JOBS_OUT" "$id" "$w2" "$g" "$m" "$eta0" "$signe" --rc "$rc" --abs "$ab" > "$JOBS_OUT/log_${id}_${qui}.txt" 2>&1
echo "fini $id $qui (code $?)"
'
echo "toutes les lectures sont finies"
