# -*- coding: ascii -*-
"""MATRICE DE MUTATIONS de la feuille de machine 1 : pour chaque faute plausible, je DERIVE une copie de feuille_vide_machine1_v1.py (remplacement exactement une fois, la piece de m1 n'est pas editee) et je rejoue le
test differentiel (ma feuille contre la copie fautive). Une mutation est ATTRAPEE si le test trouve au moins un run ecarte. Mon test mord s'il attrape toutes les mutations qui changent un comportement.
Usage : py -3.11 -I mutations_feuille_vide_machine2_v1.py <feuille m1> <ma feuille> <feuille deposee du lecteur> <table> <dossier de travail (neuf)> <N par mutation> <graine>"""
import os
import subprocess
import sys

F1, F2, FL, TABLE, TRAVAIL, N, GRAINE = sys.argv[1:8]
ICI = os.path.dirname(os.path.abspath(__file__))
src = open(F1, 'rb').read().decode('ascii').replace('\r\n', '\n')
MUT = [
    ('m01 TIENT strict (< au lieu de <=)', 'abs(lnq) <= Tt - b', 'abs(lnq) < Tt - b'),
    ('m02 TOMBE large (>= au lieu de >)', 'abs(lnq) > Tt + b', 'abs(lnq) >= Tt + b'),
    ('m03 bande sans etalement du lecteur', 'b = r["etendue"] + s', 'b = r["etendue"]'),
    ('m04 bande sans l\'etendue de la chaine', 'b = r["etendue"] + s', 'b = s'),
    ('m05 s sans ln(1 + etalement de A)', 's = max([math.log(1.0 + A["etalement"])] + [lec', 's = max([0.0] + [lec'),
    ('m06 temoin a 1e-5', 'TEMOIN_MAX = 1e-6;', 'TEMOIN_MAX = 1e-5;'),
    ('m07 V1 : onze cellules jugees suffisent', 'V1_JUGEES_MIN, V1_TENUES_PAR_CRENEAU_MIN, VP_JUGEES_MIN = 12, 2, 6', 'V1_JUGEES_MIN, V1_TENUES_PAR_CRENEAU_MIN, VP_JUGEES_MIN = 11, 2, 6'),
    ('m08 V1 : une tenue par creneau suffit', 'V1_JUGEES_MIN, V1_TENUES_PAR_CRENEAU_MIN, VP_JUGEES_MIN = 12, 2, 6', 'V1_JUGEES_MIN, V1_TENUES_PAR_CRENEAU_MIN, VP_JUGEES_MIN = 12, 1, 6'),
    ('m09 VP : cinq cellules jugees suffisent', 'V1_JUGEES_MIN, V1_TENUES_PAR_CRENEAU_MIN, VP_JUGEES_MIN = 12, 2, 6', 'V1_JUGEES_MIN, V1_TENUES_PAR_CRENEAU_MIN, VP_JUGEES_MIN = 12, 2, 5'),
    ('m10 TOMBE a trois chutes', 'if len(tom) >= 2:', 'if len(tom) >= 3:'),
    ('m11 temoin : 47 lectures suivies suffisent', 'tm["suivies"] == tm["lectures"]', 'tm["suivies"] >= 47'),
    ('m12 temoin strict (< au lieu de <=)', 'tm["rapport_au_plateau"] <= TEMOIN_MAX', 'tm["rapport_au_plateau"] < TEMOIN_MAX'),
    ('m13 la geometrie des absorbeurs n\'est plus controlee', 'if (g["forme"], g["bord"], g["couches"], g["N"]) != (forme, c["r_c"] + dr, couches, c["r_c"] + dr + couches):', 'if False:'),
    ('m14 le couplage ecrit n\'est plus controle', '(x.get("id"), x.get("w2"), x.get("m"), x.get("g"), x.get("r_c")) != (c["id"], c["w2"], c["m"], c["g"], c["r_c"])', '(x.get("id"), x.get("w2"), x.get("m"), x.get("r_c")) != (c["id"], c["w2"], c["m"], c["r_c"])'),
    ('m15 le mode pre-vol du fichier n\'est plus controle', 'if S.get("prevol") is not PREVOL or S.get("table_canon") != canon_B(TABLE):', 'if S.get("table_canon") != canon_B(TABLE):'),
    ('m16 la tolerance de la ligne profonde = 0.02 (au lieu de la table)', 'Tt = r["tolerance"]', 'Tt = 0.02'),
    ('m17 l\'instrument n\'arrete plus le jugement', 'if inst != "TIENT" or incomplet:', 'if incomplet:'),
    ('m18 NON LUE possible pour V1 (au lieu de VP seul)', 'issue_ligne(lis, V1_JUGEES_MIN, V1_TENUES_PAR_CRENEAU_MIN, False)', 'issue_ligne(lis, V1_JUGEES_MIN, V1_TENUES_PAR_CRENEAU_MIN, True)'),
    ('m19 VP exige deux tenues par creneau', 'issue_ligne(pro, VP_JUGEES_MIN, 0, True)', 'issue_ligne(pro, VP_JUGEES_MIN, V1_TENUES_PAR_CRENEAU_MIN, True)'),
    ('m20 ln q calcule avec le plateau sous B', 'A = lec["plateaux"]["A"]; gpl = A["Gamma_pl"]', 'A = lec["plateaux"]["A"]; gpl = lec["plateaux"]["B"]["Gamma_pl"]'),
]
os.makedirs(TRAVAIL, exist_ok=False)
tot, attrapees, ratees = 0, 0, []
for nom, ancien, nouveau in MUT:
    if src.count(ancien) != 1:
        print('  %-62s : REFUS DE DERIVATION (%d occurrences)' % (nom, src.count(ancien)))
        ratees.append(nom + ' (derivation)')
        continue
    t = src.replace(ancien, nouveau)
    p = os.path.join(TRAVAIL, nom.split()[0] + '_feuille.py')
    open(p, 'w', newline='\n').write(t)
    r = subprocess.run([sys.executable, '-I', os.path.join(ICI, 'difftest_feuille_vide_machine2_v1.py'), p, F2, FL, TABLE, os.path.join(TRAVAIL, nom.split()[0] + '_travail'), N, GRAINE], capture_output=True, text=True)
    ligne = [l for l in r.stdout.split('\n') if l.startswith('RUNS')]
    n_ecart = int(ligne[0].split('AVEC ECART :')[1]) if ligne else -1
    tot += 1
    if n_ecart > 0:
        attrapees += 1
    else:
        ratees.append(nom)
    print('  %-62s : %4d runs ecartes sur %s  %s' % (nom, n_ecart, N, 'ATTRAPEE' if n_ecart > 0 else 'NON ATTRAPEE'), flush=True)
print('MUTATIONS ATTRAPEES : %d sur %d' % (attrapees, tot))
if ratees:
    print('NON ATTRAPEES :', ratees)
