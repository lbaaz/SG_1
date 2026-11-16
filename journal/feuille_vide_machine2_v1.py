# -*- coding: ascii -*-
"""MA FEUILLE du gel 'largeur du vide' (partie 2, eebd979f18d8db48) : seconde implementation de la section 5 (cellule lue, etalement du lecteur s, bande, jugement), de la section 6 (issues V1 et VP)
et de la garde G-3 (forme de chaque fichier de cellule), ecrite du TEXTE du gel. Meme ligne de commande que celle de machine 1, pour le test differentiel :
  py -3.11 -I feuille_vide_machine2_v1.py <lecture_lecteur_gel_loi (deposee)> <table des cellules.json> <dossier du run> <sortie verdict.json> [--prevol]
Elle appelle juger_etat de la feuille DEPOSEE du lecteur (canon controle), comme le dit la section 5 ; elle ne mesure rien et ne calcule aucune chaine."""
import hashlib
import importlib.util
import json
import math
import os
import sys
import unicodedata

F_LECT, TABLE, RUN, SORTIE = sys.argv[1:5]
PREVOL = '--prevol' in sys.argv[5:]
CANON_F_LECT, CANON_TABLE = '83701094e6a2b965', 'b71206e5daf6c741'
CANON_SONDE_VIDE, CANON_MOTEUR, CANON_SONDE_LECT = '0f82986cca133330', '82a0be882568fe0c', 'd5cc48f48e37af99'
ABS = [['A', 'F2', 0, 80], ['B', 'F2', 0, 100], ['C', 'F1', 0, 100], ['D', 'F2', 10, 80]]
KS = list(range(-3, 9))
CRENEAUX = ('MG', 'MP', 'PP', 'PG')


def canon(p):
    t = unicodedata.normalize('NFC', open(p, 'rb').read().decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n')
    return hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]


if canon(F_LECT) != CANON_F_LECT:
    print('FEUILLE REFUSEE : feuille du lecteur')
    sys.exit(2)
if (canon(TABLE) == CANON_TABLE) == PREVOL:
    print('FEUILLE REFUSEE : table et mode')
    sys.exit(2)
spec = importlib.util.spec_from_file_location('feuille_lecteur', F_LECT)
L = importlib.util.module_from_spec(spec)
spec.loader.exec_module(L)
TAB = json.load(open(TABLE))
CEL = TAB['cellules']
if TAB['regle']['absorbeurs_du_lecteur'] != ABS or TAB['regle']['barreaux'] != KS:
    print('FEUILLE REFUSEE : regle de la table')
    sys.exit(2)
TOL = {c['id']: c['tolerance'] for c in CEL}


def forme_ok(S, c):
    """G-3 : renvoie None si le fichier est conforme, sinon le motif."""
    if S.get('sonde_canon') != CANON_SONDE_VIDE or S.get('moteur_canon') != CANON_MOTEUR or S.get('source_bloc_canon') != CANON_SONDE_LECT:
        return 'canons'
    if S.get('prevol') is not PREVOL or S.get('table_canon') != canon(TABLE):
        return 'mode ou table'
    x = S.get('cellule') or {}
    for k in ('id', 'w2', 'm', 'g', 'r_c'):
        if x.get(k) != c[k]:
            return 'cellule : ' + k
    if x.get('eta0') != c['eta0']:
        return 'cellule : eta0'
    r = S.get('reglage') or {}
    if r.get('ks') != KS or r.get('absorbeurs') != ABS:
        return 'reglage'
    for nom, signe in (('jumeau', +1),) if PREVOL else (('jumeau', +1), ('fantome', -1)):
        rec = S.get(nom)
        if not rec or rec.get('signe') != signe or rec.get('site') != [0, 0] or rec.get('E_depart') != 0.0:
            return nom + ' : signe, site, energie'
        tr = rec.get('traj') or {}
        if sorted(tr) != ['A', 'B', 'C', 'D']:
            return nom + ' : absorbeurs'
        for a in tr:
            if sorted(int(k) for k in tr[a]) != KS:
                return nom + ' : barreaux'
        for a, forme, dr, couches in ABS:
            g = (rec.get('absorbeurs') or {}).get(a) or {}
            if (g.get('forme'), g.get('bord'), g.get('couches'), g.get('N')) != (forme, c['r_c'] + dr, couches, c['r_c'] + dr + couches):
                return nom + ' : geometrie ' + a
    if PREVOL and S.get('fantome') is not None:
        return 'pre-vol : fantome present'
    return None


def issue(cs, jugees_min, par_creneau_min, non_lue_possible):
    ten = [c for c in cs if c['jugement'] == 'TIENT']
    tom = [c for c in cs if c['jugement'] == 'TOMBE']
    if len(tom) >= 2:
        return 'TOMBE'
    if non_lue_possible and len(ten) + len(tom) == 0:
        return 'NON LUE'
    if len(ten) + len(tom) < jugees_min:
        return 'NON CONCLUANT'
    if par_creneau_min and any(len([c for c in ten if c['creneau'] == s]) < par_creneau_min for s in CRENEAUX):
        return 'NON CONCLUANT'
    return 'TENU SAUF UNE CELLULE' if len(tom) == 1 else 'TENU'


out = {'prevol': PREVOL, 'cellules': [], 'incomplet': []}
f_inst = os.path.join(RUN, 'verdict_ter_instrument.json')
instrument = json.load(open(f_inst)).get('instrument') if os.path.exists(f_inst) else 'ABSENT'
out['instrument'] = instrument
fichiers = {}
for c in CEL:
    p = os.path.join(RUN, 'sonde_vide_%s.json' % c['id'])
    if not os.path.exists(p):
        out['incomplet'].append('%s : fichier absent' % c['id'])
        continue
    S = json.load(open(p))
    motif = forme_ok(S, c)
    if motif:
        out['incomplet'].append('%s : %s' % (c['id'], motif))
        continue
    fichiers[c['id']] = S
for c in CEL:
    r = {'id': c['id'], 'creneau': c['creneau'], 'ligne': c['ligne'], 'jugement': 'NON LUE', 'motif': None}
    S = fichiers.get(c['id'])
    if S is not None:
        tr = S['jumeau']['traj']
        lect = [tr[a][str(k)] for a in 'ABCD' for k in KS]
        suivies = sum(1 for x in lect if x.get('suivi'))
        gam = [x['gamma'] for x in lect if x.get('suivi') and x.get('gamma') is not None and math.isfinite(x['gamma'])]
        r['temoin'] = {'lectures': len(lect), 'suivies': suivies, 'plus_grande_largeur': max(gam) if gam else None}
        if not PREVOL:
            j = L.juger_etat(S['fantome']['traj'], None)
            r['lecteur'] = {'statut': j['statut']}
            if j['statut'] == 'QUALIFIE':
                P = j['plateaux']
                gpl = P['A']['Gamma_pl']
                s = max([math.log(1.0 + P['A']['etalement'])] + [P[x]['ecart_ln_A'] for x in 'BCD'])
                r['ln_Gamma_pl'] = math.log(gpl)
                r['etalement_du_lecteur'] = s
                rap = (r['temoin']['plus_grande_largeur'] / gpl) if r['temoin']['plus_grande_largeur'] is not None else None
                r['temoin']['tient'] = bool(suivies == len(lect) and rap is not None and rap <= 1e-6)
                if r['temoin']['tient']:
                    ln_q = c['ln_G3'] - r['ln_Gamma_pl']
                    b = c['etendue'] + s
                    T = c['tolerance']
                    r['ln_q'], r['bande'] = ln_q, b
                    r['jugement'] = 'TIENT' if abs(ln_q) <= T - b else ('TOMBE' if abs(ln_q) > T + b else 'NON JUGEABLE')
                else:
                    r['motif'] = 'temoin'
            else:
                r['motif'] = 'lecteur : ' + j['statut']
    out['cellules'].append(r)
if PREVOL:
    out['verdict'] = "PRE-VOL, RIEN N'EST JUGE"
elif instrument != 'TIENT':
    out['verdict'] = "L'INSTRUMENT NE TIENT PAS : RIEN N'EST JUGE"
elif out['incomplet']:
    out['verdict'] = 'RUN INCOMPLET : RIEN N\'EST JUGE'
else:
    lis = [r for r in out['cellules'] if r['ligne'] == 'lisible']
    pro = [r for r in out['cellules'] if r['ligne'] == 'profonde']
    comptes = lambda cs: {k: sum(1 for r in cs if r['jugement'] == k) for k in ('TIENT', 'TOMBE', 'NON JUGEABLE', 'NON LUE')}
    out['V1'] = {'issue': issue(lis, 12, 2, False), 'comptes': comptes(lis), 'tombees': [r['id'] for r in lis if r['jugement'] == 'TOMBE']}
    out['VP'] = {'issue': issue(pro, 6, 0, True), 'comptes': comptes(pro), 'tombees': [r['id'] for r in pro if r['jugement'] == 'TOMBE']}
    out['verdict'] = 'V1 %s ; VP %s' % (out['V1']['issue'], out['VP']['issue'])
json.dump(out, open(SORTIE, 'w', newline='\n'), indent=1, sort_keys=True)
