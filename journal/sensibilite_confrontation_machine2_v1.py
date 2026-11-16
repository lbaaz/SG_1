# -*- coding: ascii -*-
"""SENSIBILITE DU TEST DIFFERENTIEL -- machine 2, 2026-11-16. La confrontation (40 essais) a montre que ma feuille et celle de machine 1 s'accordent. Cela ne vaut que si les essais EXERCENT chaque
regle des sections 5 et 6. Ici : pour chaque regle, une MUTATION de ma feuille (une seule chose changee, texte unique asserte), rejouee sur les memes 40 essais ; la mutation est TUEE si au moins un essai rend
autre chose que ma feuille intacte (cellule, etat, issue). Si ma feuille mutee differe de la mienne a l'essai k, elle differe aussi de celle de machine 1 (egale a la mienne) : une meme mutation dans la
feuille de machine 1 serait donc VUE par la confrontation. Une mutation SURVIVANTE = une regle que les 40 essais n'exercent pas (angle mort declare).
Usage : py -3.11 -P sensibilite_confrontation_machine2_v1.py <moteur> <bloc2> <ordre3_machine2_v1.py> <depot> <dossier de la confrontation> <sortie.json>"""
import importlib.util
import json
import os
import sys

MOTEUR, BLOC2, SCRIPT3, DEPOT, CONF, SORTIE = sys.argv[1:7]
SRC_PATH = 'feuille_independante_gel_loi_machine2_v1.py'
SRC = open(SRC_PATH, encoding='ascii').read()


def charger_module(texte, nom, env=None):
    chem = os.path.join(os.path.dirname(os.path.abspath(SRC_PATH)), '_mut_%s.py' % nom)
    open(chem, 'w', encoding='ascii').write(texte)
    spec = importlib.util.spec_from_file_location(nom, chem)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    if env is None:
        m.charger(MOTEUR, BLOC2, SCRIPT3)
    else:
        m._ENV.update(env)
    return m


BASE = charger_module(SRC, 'base')
ENV = BASE._ENV
DEP = json.load(open(DEPOT))
ESSAIS = []
for d in sorted(os.listdir(CONF)):
    p = os.path.join(CONF, d)
    if os.path.isdir(p) and os.path.exists(os.path.join(p, 'table.json')):
        ESSAIS.append(tuple(json.load(open(os.path.join(p, n + '.json'))) for n in ('table', 'dense', 'verdict')))


def empreinte(out):
    """Tout ce que la feuille rend, sauf les flottants bruts."""
    if out['instrument'] != 'TIENT':
        return ('NE TIENT PAS',)
    cel = []
    for c in out['cellules']:
        cel.append((c['id'], c['n_lus'], c['n_juges'], c['n_domaine'], c['n_hors'], c['exploitable'], c['E1'], c['E2'], c['E3'], c['n_pres'], c['seuil_E2'],
                    tuple((e['rang'], e['exclu'], e.get('domaine'), e.get('tient_E1'), e.get('pres'), e.get('bande_ok')) for e in c['etats'])))
    return (tuple(cel), out['E1'][0], tuple(out['E1'][1]), out['E2'][0], tuple(out['E2'][1]), out['E1B'][0], tuple(out['E1B'][1]), out['E3'][0], tuple(out['E3'][1]))


def jouer(m):
    return [empreinte(m.juger(t, d, v, DEP)) for t, d, v in ESSAIS]


REF = jouer(BASE)
print('%d essais ; reference rejouee (ma feuille intacte, cache de chaines partage)' % len(REF), flush=True)
MUT = [
    ('K01 J net 0.2 -> 0.3', "elif not e['J_ecart_type'] < 0.2:", "elif not e['J_ecart_type'] < 0.3:"),
    ('K02 e_bord du domaine 0.7 -> 0.75', "c['e_bord'] < 0.7 and", "c['e_bord'] < 0.75 and"),
    ('K03 stabilite du domaine 0.05 -> 0.06', "c['stab3'] <= 0.05)", "c['stab3'] <= 0.06)"),
    ('K04 T bas 0.05 -> 0.06', "T = 0.05 if c['e_bord'] < 0.3 else 0.10", "T = 0.06 if c['e_bord'] < 0.3 else 0.10"),
    ('K05 T haut 0.10 -> 0.11', "T = 0.05 if c['e_bord'] < 0.3 else 0.10", "T = 0.05 if c['e_bord'] < 0.3 else 0.11"),
    ('K06 seuil de classe 0.3 -> 0.35', "T = 0.05 if c['e_bord'] < 0.3 else 0.10", "T = 0.05 if c['e_bord'] < 0.35 else 0.10"),
    ('K07 tolerance stricte (<= devient <)', "'tient_E1': bool(dom and l3 <= T)", "'tient_E1': bool(dom and l3 < T)"),
    ('K08 plus pres : < devient <=', "'pres': bool(dom and l3 < l2)", "'pres': bool(dom and l3 <= l2)"),
    ('K09 seuil E2 arrondi par defaut', "seuil = -(-3 * len(dom) // 4)", "seuil = 3 * len(dom) // 4"),
    ('K10 seuil E2 deux tiers au lieu de trois quarts', "seuil = -(-3 * len(dom) // 4)", "seuil = -(-2 * len(dom) // 3)"),
    ('K11 garde des deux tiers -> la moitie', "3 * len(jug) >= 2 * len(etats)", "2 * len(jug) >= 1 * len(etats)"),
    ('K12 garde des deux tiers stricte', "3 * len(jug) >= 2 * len(etats)", "3 * len(jug) > 2 * len(etats)"),
    ('K13 domaine minimum des lignes 5 -> 4', "expl = assez and len(dom) >= 5", "expl = assez and len(dom) >= 4"),
    ('K14 domaine minimum des bords 2 -> 1', "expl = assez and len(dom) >= 2 and len(hors) >= 2", "expl = assez and len(dom) >= 1 and len(hors) >= 2"),
    ('K15 hors-domaine minimum des bords 2 -> 1', "expl = assez and len(dom) >= 2 and len(hors) >= 2", "expl = assez and len(dom) >= 2 and len(hors) >= 1"),
    ('K16 E1 : inexploitables admises 2 -> 3', "out['E1'] = issue(lig, 'E1', 2, 1)", "out['E1'] = issue(lig, 'E1', 3, 1)"),
    ('K17 E1 : chutes admises 1 -> 2', "out['E1'] = issue(lig, 'E1', 2, 1)", "out['E1'] = issue(lig, 'E1', 2, 2)"),
    ('K18 E2 : chutes admises 1 -> 0 (la lecture stricte de E2)', "out['E2'] = issue(lN, 'E2', 1, 1)", "out['E2'] = issue(lN, 'E2', 1, 0)"),
    ('K19 E2 : inexploitables admises 1 -> 2', "out['E2'] = issue(lN, 'E2', 1, 1)", "out['E2'] = issue(lN, 'E2', 2, 1)"),
    ('K20 E1B : chutes admises 0 -> 1', "out['E1B'] = issue(brd, 'E1', 0, 0)", "out['E1B'] = issue(brd, 'E1', 0, 1)"),
    ('K21 E1B : inexploitables admises 0 -> 1', "out['E1B'] = issue(brd, 'E1', 0, 0)", "out['E1B'] = issue(brd, 'E1', 1, 0)"),
    ('K22 bande 1.25 -> 1.3', "return 1.25", "return 1.3"),
    ('K23 bande 1.6 -> 1.7', "return 1.6", "return 1.7"),
    ('K24 E3 sur les seuls etats du domaine', "e3 = 'VIDE' if not jug else ('TIENT' if all(r['bande_ok'] for r in jug) else 'TOMBE')", "e3 = 'VIDE' if not jug else ('TIENT' if all(r['bande_ok'] for r in dom) else 'TOMBE')"),
    ('K25 E3 sans borne basse', "'bande_ok': bool(1.0 / B <= q2 <= B)", "'bande_ok': bool(q2 <= B)"),
    ('K26 J flou non exclu', "elif not e['J_ecart_type'] < 0.2:", "elif False:"),
    ('K27 etiquette double non exclue', "elif labels.count((e['n1'], e['n2'])) != 1:", "elif False:"),
    ('K28 chaine du moteur instable non exclue', "elif not c['stable1']:", "elif False:"),
    ("K29 chaine d'ordre 2 instable non exclue", "elif not c['stable2']:", "elif False:"),
    ('K30 stabilite : rapport 2 -> 2.5', "max(v) / min(v) <= 2.0", "max(v) / min(v) <= 2.5"),
    ('K31 q3 calcule avec G2', "q3 = c['G3'] / gp if c['G3'] > 0 else None", "q3 = c['G2'] / gp if c['G3'] > 0 else None"),
    ('K32 plateau sous l absorbeur B au lieu de A', "gp = ev['plateaux']['A']['Gamma_pl']", "gp = ev['plateaux']['B']['Gamma_pl']"),
    ('K33 facteur d eta 1/32 au lieu de 1/16 (ordre 2)', "'G2': G2[2],", "'G2': G2[3],"),
    ('K34 non qualifie non exclu', "if ev['statut'] != 'QUALIFIE':", "if False:"),
    ('K35 domaine sans la condition G3 > 0', "dom = bool(c['G3'] > 0 and c['e_bord'] < 0.7", "dom = bool(c['e_bord'] < 0.7"),
]
tues, surv, det = [], [], []
for nom, a, b in MUT:
    assert SRC.count(a) == 1, '%s : texte trouve %d fois : %r' % (nom, SRC.count(a), a)
    m = charger_module(SRC.replace(a, b), nom[:3].lower(), env=ENV)
    try:
        obt = jouer(m)
        diff = [k for k, (x, y) in enumerate(zip(obt, REF)) if x != y]
    except BaseException as x:
        diff = ['plante : %s' % type(x).__name__]
    (tues if diff else surv).append(nom)
    det.append({'mutation': nom, 'essais_ou_elle_differe': diff[:12], 'n': len(diff)})
    print('%-62s %s%s' % (nom, 'TUEE' if diff else 'SURVIT', (' (%d essais)' % len(diff)) if diff else ''), flush=True)
print('BILAN : %d mutations, %d tuees, %d survivantes : %s' % (len(MUT), len(tues), len(surv), surv))
json.dump({'mutations': det, 'survivantes': surv}, open(SORTIE, 'w'), indent=1)
for f in os.listdir(os.path.dirname(os.path.abspath(SRC_PATH))):
    if f.startswith('_mut_') and f.endswith('.py'):
        os.remove(os.path.join(os.path.dirname(os.path.abspath(SRC_PATH)), f))
