# -*- coding: ascii -*-
"""DIFFERENTIEL DES FEUILLES du gel "pont" (seconde partie) : mes feuilles (ecrites du texte) contre celles de machine 1, sur des sorties de sonde SYNTHETIQUES (genere_synthetique_pont_machine2_v4.py).
Pour chaque graine : fabrique les sorties, passe les deux chaines de feuilles (densite x6, boites, verdict), confronte. Machine 2, 2026-11-17.
Mode "mutation NOM" : applique une alteration au texte de l'une des trois feuilles de machine 1 (dans un dossier temporaire, la feuille du lot n'est pas touchee) et dit si le differentiel la voit.
VERSION 4 (generateur v4 : graines >= 100, bord de S) ; VERSION 3 (generateur v3) ; VERSION 2 : compare aussi les LECTURES (ln R3, ln R2, lisible par ecart) et la question Q2.
Usage : py -3.11 -P differentiel_feuilles_machine2_v4.py <registre> <dossier du lot de m1> <dossier de travail neuf> <graine debut> <graine fin> [--mutation NOM]"""
import json
import math
import os
import shutil
import subprocess
import sys

REG, LOT, TRAV, G0, G1 = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
MUT = sys.argv[7] if len(sys.argv) > 7 and sys.argv[6] == '--mutation' else None
BASE = sys.argv[9] if len(sys.argv) > 9 and sys.argv[8] == '--base' else None
HERE = os.path.dirname(os.path.abspath(__file__))
PY = ['py', '-3.11', '-P']
os.makedirs(TRAV, exist_ok=False)
env = dict(os.environ); env['PONT_C2'] = 'a'
BLOCS = [REG + '/scripts/' + b for b in ('m17_chaine_v17.py', 'chaine_ordre2_bloc_machine1_v1.py', 'ordre3_bloc_machine1_v1.py', 'chaine_adaptee_bloc_machine1_v1.py')]
FEUILLES = {n: os.path.join(LOT, n) for n in ('lecture_densite_2d_pont_machine1_v1.py', 'lecture_boites_pont_machine1_v1.py', 'verdict_pont_machine1_v1.py')}
MUTATIONS = {            # nom : (feuille, ancien, nouveau)
    'plateau_105_en_110': ('lecture_densite_2d_pont_machine1_v1.py', 'TAU, SEUIL_ABS = -3, 8, Fraction(1, 20), 0.02', 'TAU, SEUIL_ABS = -3, 8, Fraction(1, 10), 0.02'),
    'etendue_002_en_003': ('lecture_densite_2d_pont_machine1_v1.py', 'Fraction(1, 20), 0.02', 'Fraction(1, 20), 0.03'),
    'etendue_inf_strict': ('lecture_densite_2d_pont_machine1_v1.py', '"lisible": bool(et <= SEUIL_ABS)', '"lisible": bool(et < SEUIL_ABS - 0.0015)'),
    'mediane_en_moyenne': ('lecture_densite_2d_pont_machine1_v1.py', 'med = mediane(lg)', 'med = sum(lg) / 4.0'),
    'w0_sans_mediane': ('lecture_densite_2d_pont_machine1_v1.py', 'w = mediane([v["w0"] for v in suivis]) if suivis else None', 'w = suivis[0]["w0"] if suivis else None'),
    'part_non_fiable_10': ('lecture_boites_pont_machine1_v1.py', 'PART_NON_FIABLE_MAX = F(1, 20), F(8), 0.05', 'PART_NON_FIABLE_MAX = F(1, 20), F(8), 0.10'),
    'compte_sans_couverte': ('lecture_boites_pont_machine1_v1.py', 'and b["couverte_a"] and b["couverte_b"]', ''),
    'S_largeur_8': ('lecture_boites_pont_machine1_v1.py', 'LARGEUR = float(X_HI - X_LO)', 'LARGEUR = float(X_HI)'),
    'participation_inverse': ('lecture_boites_pont_machine1_v1.py', '(tot * tot / sum(yy * yy for yy in y))', '(sum(yy * yy for yy in y) / (tot * tot))'),
    'L_tol_006': ('verdict_pont_machine1_v1.py', 'TOL_L, MIN_ECARTS, X_L2 = 0.05, 10, 5.0', 'TOL_L, MIN_ECARTS, X_L2 = 0.06, 10, 5.0'),
    'L_min_ecarts_9': ('verdict_pont_machine1_v1.py', 'TOL_L, MIN_ECARTS, X_L2 = 0.05, 10, 5.0', 'TOL_L, MIN_ECARTS, X_L2 = 0.05, 9, 5.0'),
    'L2_x_4': ('verdict_pont_machine1_v1.py', 'TOL_L, MIN_ECARTS, X_L2 = 0.05, 10, 5.0', 'TOL_L, MIN_ECARTS, X_L2 = 0.05, 10, 4.0'),
    'L2_large': ('verdict_pont_machine1_v1.py', 'not abs(p["ln_R3"]) < abs(p["ln_R2"])', 'not abs(p["ln_R3"]) <= abs(p["ln_R2"])'),
    'S_cellule_080': ('verdict_pont_machine1_v1.py', 'S_CELLULE, S_GROUPE = (0.85, 1.15), (0.80, 1.20)', 'S_CELLULE, S_GROUPE = (0.80, 1.15), (0.80, 1.20)'),
    'S_groupe_075': ('verdict_pont_machine1_v1.py', 'S_CELLULE, S_GROUPE = (0.85, 1.15), (0.80, 1.20)', 'S_CELLULE, S_GROUPE = (0.85, 1.15), (0.75, 1.20)'),
    'C_reduit_bas_030': ('verdict_pont_machine1_v1.py', 'C_REDUIT, C_RAPPORT = (0.33, 0.55), (1.25, 1.85)', 'C_REDUIT, C_RAPPORT = (0.30, 0.55), (1.25, 1.85)'),
    'C_rapport_haut_200': ('verdict_pont_machine1_v1.py', 'C_REDUIT, C_RAPPORT = (0.33, 0.55), (1.25, 1.85)', 'C_REDUIT, C_RAPPORT = (0.33, 0.55), (1.25, 2.00)'),
    'min_boites_7': ('verdict_pont_machine1_v1.py', 'MIN_BOITES = (180, 189), (291, 300), 8', 'MIN_BOITES = (180, 189), (291, 300), 7'),
    'famille_sans_creneau': ('verdict_pont_machine1_v1.py', 'and creneaux == tous_creneaux', ''),
    'famille_trois_cellules': ('verdict_pont_machine1_v1.py', 'min(4, len(CELLULES))', 'min(3, len(CELLULES))'),
    'groupe_UN_179': ('verdict_pont_machine1_v1.py', 'UN = (180, 189)', 'UN = (179, 189)'),
}
if MUT:
    f, a, b = MUTATIONS[MUT]
    src = open(FEUILLES[f], encoding='ascii').read()
    if MUT == 'min_boites_7':
        a = 'UN = (180, 189); DEUX = (291, 300); MIN_BOITES = 8'; b = 'UN = (180, 189); DEUX = (291, 300); MIN_BOITES = 7'
    if MUT == 'groupe_UN_179':
        a = 'UN = (180, 189); DEUX'; b = 'UN = (179, 189); DEUX'
    assert a in src, 'ancre introuvable : ' + MUT
    mut = os.path.join(TRAV, 'mutee_' + f)
    open(mut, 'w', encoding='ascii').write(src.replace(a, b, 1))
    FEUILLES[f] = mut


def lance(args, **kw):
    r = subprocess.run(args, capture_output=True, text=True, env=env, **kw)
    if r.returncode != 0:
        print('ECHEC', args[:4], r.stderr[-400:])
        raise SystemExit(1)
    return r.stdout


CELLULES = ['MG3', 'MG4', 'MG5', 'PG3', 'PG4', 'PG5']
total = dict(graines=0, desaccords=0, cellules_comparees=0)
etats = {}
for graine in range(G0, G1 + 1):
    d = os.path.join(TRAV, 'g%d' % graine)
    reuse = bool(BASE and MUT and MUTATIONS[MUT][0] != 'lecture_boites_pont_machine1_v1.py')
    if reuse:
        shutil.copytree(os.path.join(BASE, 'g%d' % graine), d)
    else:
        lance(PY + [os.path.join(HERE, 'genere_synthetique_pont_machine2_v4.py'), str(graine), d, REG, os.path.join(LOT, 'chaine_cellules_pont_v1.json')])
    # --- ma chaine de feuilles : ma chaine d'abord (une fois pour toutes, dans le dossier de travail)
    ma_chaine = os.path.join(TRAV, 'ma_chaine.json')
    if BASE and not os.path.isfile(ma_chaine):
        shutil.copy(os.path.join(BASE, 'ma_chaine.json'), ma_chaine)
    if not os.path.isfile(ma_chaine):
        lance(PY + [os.path.join(HERE, 'chaine_pont_machine2_v1.py'), REG, ma_chaine, 'MG3=397/200:3:3.63872e-03', 'MG4=397/200:4:2.77765e-03', 'MG5=397/200:5:2.20823e-03',
                    'PG3=2019/1000:3:5.23478e-03', 'PG4=2019/1000:4:3.99601e-03', 'PG5=2019/1000:5:3.17683e-03'])
    for c in CELLULES:
        if not reuse:
            lance(PY + [os.path.join(HERE, 'feuilles_pont_machine2_v1.py'), 'densite', ma_chaine, c, os.path.join(d, 'moi_lecture_%s.json' % c)] + [os.path.join(d, 'densite_%s_%s.json' % (c, a)) for a in 'ABCD'])
        if not reuse or MUTATIONS[MUT][0] == 'lecture_densite_2d_pont_machine1_v1.py':
          lance(PY + [FEUILLES['lecture_densite_2d_pont_machine1_v1.py'], os.path.join(LOT, 'chaine_cellules_pont_v1.json'), c, os.path.join(d, 'lui_lecture_%s.json' % c)] + [os.path.join(d, 'densite_%s_%s.json' % (c, a)) for a in 'ABCD'])
    if not reuse:
        lance(PY + [os.path.join(HERE, 'feuilles_pont_machine2_v1.py'), 'boites', REG, os.path.join(d, 'moi_boites.json')] + [os.path.join(d, 'boites_%s.jsonl' % c) for c in CELLULES])
    if not reuse or MUTATIONS[MUT][0] == 'lecture_boites_pont_machine1_v1.py':
      lance(PY + [FEUILLES['lecture_boites_pont_machine1_v1.py']] + BLOCS + [os.path.join(LOT, 'chaine_pont_bloc_machine1_v1.py'), os.path.join(d, 'lui_boites.json')] + [os.path.join(d, 'boites_%s.jsonl' % c) for c in CELLULES])
    lance(PY + [os.path.join(HERE, 'feuilles_pont_machine2_v1.py'), 'verdict', os.path.join(d, 'moi_boites.json'), os.path.join(d, 'moi_verdict.json')] + [os.path.join(d, 'moi_lecture_%s.json' % c) for c in CELLULES])
    lance(PY + [FEUILLES['verdict_pont_machine1_v1.py'], os.path.join(LOT, 'chaine_cellules_pont_v1.json'), os.path.join(d, 'lui_boites.json'), os.path.join(d, 'lui_verdict.json')] + [os.path.join(d, 'lui_lecture_%s.json' % c) for c in CELLULES])
    moi, lui = json.load(open(os.path.join(d, 'moi_verdict.json'))), json.load(open(os.path.join(d, 'lui_verdict.json')))
    des = []
    code = lambda t: {True: 'TIENT', False: 'TOMBE', None: 'ILLISIBLE'}[t]
    for c in CELLULES:
        for fam in ('L', 'L2', 'S', 'C'):
            a, b = code(moi['cellules'][c][fam]['tient']), lui['cellules'][c][fam]['verdict']
            etats[(fam, b)] = etats.get((fam, b), 0) + 1
            total['cellules_comparees'] += 1
            if a != b:
                des.append('%s %s : moi %s, lui %s' % (c, fam, a, b))
        # chiffres
        a, b = moi['cellules'][c]['S'], lui['cellules'][c]['S']
        if 'moyenne' in b and abs(a['moyenne'] - b['moyenne']) > 1e-7:
            des.append('%s S moyenne : %.8f / %.8f' % (c, a['moyenne'], b['moyenne']))
        a, b = moi['cellules'][c]['C'], lui['cellules'][c]['C']
        if 'rapport' in b and abs(a['rapport'] - b['rapport']) > 1e-9:
            des.append('%s C rapport : %.8f / %.8f' % (c, a['rapport'], b['rapport']))
    for c in CELLULES:
        a, b = json.load(open(os.path.join(d, 'moi_lecture_%s.json' % c))), json.load(open(os.path.join(d, 'lui_lecture_%s.json' % c)))
        for pa, pb in zip(a['par_x'], b['par_x']):
            if pa['lisible'] != pb['lisible']:
                des.append('%s lecture x=%s lisible : moi %s, lui %s' % (c, pa['x'], pa['lisible'], pb['lisible']))
            elif pa['lisible'] and (abs(pa['ln_R3'] - pb['ln_R3']) > 1e-9 or abs(pa['ln_R2'] - pb['ln_R2']) > 1e-9):
                des.append('%s lecture x=%s ln R3 %.10f / %.10f' % (c, pa['x'], pa['ln_R3'], pb['ln_R3']))
                break
    for g in ('UN', 'DEUX'):
        qa, qb = moi['questions'].get('Q2_groupe_' + g), lui['questions'].get('Q2_' + g)
        if (qa is None) != (qb is None) or (qa and abs(qa['rapport'] - qb['rapport']) > 1e-9):
            des.append('Q2 %s : %s / %s' % (g, qa, qb))
    for fam in ('L', 'L2', 'S', 'C'):
        if moi['familles'][fam]['etat'] != lui['familles'][fam]['verdict']:
            des.append('famille %s : moi %s, lui %s' % (fam, moi['familles'][fam]['etat'], lui['familles'][fam]['verdict']))
        etats[('famille', lui['familles'][fam]['verdict'])] = etats.get(('famille', lui['familles'][fam]['verdict']), 0) + 1
    total['graines'] += 1; total['desaccords'] += len(des)
    print('graine %d : %d desaccord(s) %s' % (graine, len(des), des[:4]), flush=True)
print('BILAN%s : %d graines, %d desaccords sur %d comparaisons cellule x famille' % ((' (mutation %s)' % MUT) if MUT else '', total['graines'], total['desaccords'], total['cellules_comparees']))
print('repartition des verdicts de LUI (couverture des issues) :', ' ; '.join('%s %s : %d' % (k[0], k[1], v) for k, v in sorted(etats.items())))
