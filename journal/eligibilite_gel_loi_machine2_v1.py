# -*- coding: ascii -*-
"""MA TABLE D'ELIGIBILITE DES 152 CELLULES CANDIDATES du gel 'loi de la largeur, ordre 3', premiere partie (b56ca5cb2dd25da1, sections 4 et 5) -- machine 2, 2026-11-15. Hors chaine, 1D seulement : AUCUN calcul 2D.
Derive de cellule_machine2_v1.py (non edite ; lot 658e3a89bcfa9368) : meme evaluateur de cellule (evalue, ecrit des regles et sans lire le code de machine 1), memes definitions que la section 4.1 a 4.4 du gel ;
la fin du script est remplacee : les cellules sont celles des quatre creneaux de MON script de tirage (tirage_gel_loi_machine2_v1.py), la regle est 4.5 (commune : N <= 74, au moins 8 jugeables, dont au
moins 5 dans le domaine) ou 4.6 (de bord : N <= 74, au moins 8 jugeables, au moins 2 dans le domaine ET au moins 2 hors du domaine ; hors = jugeable et pas dans le domaine). Le script ecrit ma table
(format de la section 5 du gel, avec le detail par cellule), la confronte a celle de machine 1 cellule par cellule et etiquette par etiquette, et ecrit la TABLE COMMUNE (le ET).
Usage : py -3.11 -P eligibilite_gel_loi_machine2_v1.py <moteur_v17.py> <bloc ordre 2> <ordre3_machine2_v1.py> <tirage_gel_loi_machine2_v1.py> <eligibilite_candidates_v1.json de machine 1>
        <ma table.json> <table commune.json>"""
import concurrent.futures as cf
import importlib.machinery
import importlib.util
import json
import math
import os
import re
import sys
import tempfile
from fractions import Fraction as F
import numpy as np

MOTEUR, BLOC2, SCRIPT3 = sys.argv[1:4]
spec = importlib.util.spec_from_file_location('moteur', MOTEUR)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
ld = importlib.machinery.SourceFileLoader('bloc2', BLOC2)
B2 = importlib.util.module_from_spec(importlib.util.spec_from_loader('bloc2', ld))
B2.M, B2.np, B2.math = M, np, math
ld.exec_module(B2)
src = open(SCRIPT3, encoding='ascii').read()
a_, b_ = src.index('# les sauts hors echelle'), src.index('def epreuve_boite')
ent = "import math\nimport numpy as np\nfrom fractions import Fraction as F\nP = M.P\nW1 = float(M.W1)\nC0, C1 = M.CANAL\n"
_td = tempfile.mkdtemp()
_chem = os.path.join(_td, 'chaine_reprise.py')
open(_chem, 'w', encoding='ascii').write(ent + src[a_:b_])
_ld3 = importlib.machinery.SourceFileLoader('chaine_reprise', _chem)
C = importlib.util.module_from_spec(importlib.util.spec_from_loader('chaine_reprise', _ld3))
C.M = M
_ld3.exec_module(C)

FRACTION, L_BOITE, K_PREDITS, N_JUGES = 0.70, 20, 16, 14
EFS = (0.25, 0.125, 0.0625, 0.03125)
EF = 0.0625
PLANCHER10 = 1.33e-12


def poisson_log(n, m):
    return n * math.log(m) - m - math.lgamma(n + 1) if m > 0 else (0.0 if n == 0 else -1e300)


def stable(v):
    return all(x > 0 for x in v) and max(v) / min(v) <= 2.0


def evalue(w2, fac):
    w2, fac = F(w2), F(fac)
    g_regle = float(M.g_du_point(w2))
    g = g_regle * float(fac)
    s = FRACTION * M.s_ff(w2, g)
    n1_0, n2_0 = M.appariement(s, w2)
    sites0 = M.barriere(n1_0, n2_0, w2, g, True)
    m2b = sites0[-1][0] if sites0 else 0
    b_M = max(8, m2b)
    r_c = int(math.ceil(n1_0)) + 2 * (m2b + b_M) + 2
    N = r_c + L_BOITE
    cel = {'w2': str(w2), 'facteur': str(fac), 'delta': float(w2) - 2.0, 'g': g, 's': s, 'graine': [n1_0, n2_0], 'r_c': r_c, 'N': N, 'faisable': bool(N <= M.N_MAX_EB), 'etats': []}
    if not cel['faisable']:
        return cel
    poids = [(poisson_log(a, n1_0) + poisson_log(b, n2_0), a, b) for a in range(N) for b in range(N)]
    poids.sort(key=lambda x: (-x[0], x[1], x[2]))
    d = float(w2) - 2.0
    for rang, (lw, a, b) in enumerate(poids[:K_PREDITS]):
        e = {'rang_predit': rang, 'n1': a, 'n2': b, 'poids_graine': math.exp(lw), 'vide': None, 'erreur': None}
        try:
            sites = M.barriere(float(a), float(b), w2, g, True)
            e['vide'] = len(sites) == 0
            if not sites:
                cel['etats'].append(e)
                continue
            e['card'] = len(sites)
            e['e_bord'] = sites[-1][1]
            G1 = [float(M.gamma_chaine(float(a), float(b), w2, g, sites, eta_facteur=ef, M_facteur=4)['Gamma_c']) for ef in EFS]
            tb = B2.tables_ordre2(float(a), float(b), w2, g, sites, M_facteur=4)
            G2 = [B2.gamma_chaine_ordre2(tb, ef)['Gamma_flux'] for ef in EFS]
            ch = C.Chaine(float(a), float(b), w2, g)
            G3 = C.chaine3(tb, ch, EF)['Gamma_flux']
            var = [C.chaine3(tb, ch, 2 * EF)['Gamma_flux'], C.chaine3(tb, ch, EF / 2)['Gamma_flux'], C.chaine3(tb, ch, EF, recul=4)['Gamma_flux']]
            e.update({'G1': G1, 'G2': G2, 'G3': G3, 'm_bord': tb['m2_bord'], 'stable1': stable(G1), 'stable2': stable(G2),
                      'stab3': max(abs(math.log(v / G3)) for v in var) if G3 > 0 and all(v > 0 for v in var) else float('inf')})
            garde = e['e_bord'] < 0.7 and e['stab3'] <= 0.05
            larg = G3 if garde else G2[2]
            e['jugeable'] = bool(e['stable1'] and e['stable2'] and larg > PLANCHER10)
            e['domaine'] = bool(e['jugeable'] and garde)
            e['discriminant'] = bool(e['domaine'] and abs(math.log(G2[2] / G3)) >= 0.05)
        except BaseException as x:
            e['erreur'] = '%s: %s' % (type(x).__name__, str(x)[:120])
        cel['etats'].append(e)
    ju = cel['etats'][:N_JUGES]
    cel['compte'] = [sum(1 for e in ju if e.get('jugeable')), sum(1 for e in ju if e.get('domaine')), sum(1 for e in ju if e.get('discriminant'))]
    return cel


def travail(arg):
    return arg[0], evalue(arg[1], arg[2])


ORDRE = ('N', 'P', 'BN', 'BP')
N_COUT, JUG_MIN, DOM_MIN, BORD_MIN = 74, 8, 5, 2


def eligible_cellule(cel, bord):
    """Gel 'loi, ordre 3', partie 1, 4.5 (commune) et 4.6 (de bord). hors = jugeables - dans le domaine (un etat HORS DU DOMAINE y est un etat jugeable qui n'est pas dans le domaine : lecture de machine 2)."""
    c = cel.get('compte')
    if not cel['faisable'] or c is None or cel['N'] > N_COUT:
        return False
    nj, nd = c[0], c[1]
    hors = nj - nd
    if bord:
        return nj >= JUG_MIN and nd >= BORD_MIN and hors >= BORD_MIN
    return nj >= JUG_MIN and nd >= DOM_MIN


if __name__ == '__main__':
    TIRAGE, SIEN, SORTIE_MIENNE, SORTIE_COMMUNE = sys.argv[4:8]
    spt = importlib.util.spec_from_file_location('tirage', TIRAGE)
    T = importlib.util.module_from_spec(spt)
    spt.loader.exec_module(T)
    cellules, cles = [], []
    for s in ORDRE:
        for w in T.liste(s):
            for f in T.CRENEAUX[s][2]:
                cellules.append((s, w, F(f)))
                cles.append((w, F(f)))
    cles = sorted(set(cles))
    print('creneaux N, P, BN, BP : %d w2 candidats, %d cellules (%d distinctes)' % (sum(len(T.liste(s)) for s in ORDRE), len(cellules), len(cles)), flush=True)
    with cf.ProcessPoolExecutor(max_workers=8) as ex:
        res = dict(ex.map(travail, [(k, k[0], k[1]) for k in cles]))
    mine = {'creneaux': {}, 'cellules': [], 'reglage': {'N_cout': N_COUT, 'jug_min': JUG_MIN, 'dom_min': DOM_MIN, 'bord_min': BORD_MIN, 'e_max': 0.7, 'stab_max': 0.05, 'plancher10': PLANCHER10, 'n_etats': N_JUGES}}
    elig_w = {}
    for s in ORDRE:
        bord = s in ('BN', 'BP')
        cands = []
        for w in T.liste(s):
            oks = []
            for f in T.CRENEAUX[s][2]:
                cel = res[(w, F(f))]
                ok = eligible_cellule(cel, bord)
                oks.append(ok)
                c = cel.get('compte') or [None, None, None]
                mine['cellules'].append({'creneau': s, 'w2': str(w), 'facteur': f, 'N': cel['N'], 'n_jug': c[0], 'n_dom': c[1], 'n_hors': (c[0] - c[1]) if c[0] is not None else None, 'eligible': ok,
                                         'etiquettes': [[e['n1'], e['n2'], int(bool(e.get('jugeable'))), int(bool(e.get('domaine')))] for e in cel['etats'][:N_JUGES]]})
            elig_w[(s, w)] = all(oks)
            cands.append({'w2': str(w), 'eligible': all(oks)})
        mine['creneaux'][s] = {'candidats': cands, 'n': len(cands), 'n_eligibles': sum(1 for c in cands if c['eligible'])}
        print('creneau %-2s : %2d w2 eligibles sur %2d%s' % (s, mine['creneaux'][s]['n_eligibles'], len(cands), '' if mine['creneaux'][s]['n_eligibles'] == len(cands) else '   INELIGIBLES : ' + ' '.join(
            '%.3f' % float(F(c['w2'])) for c in cands if not c['eligible'])))
    json.dump(mine, open(SORTIE_MIENNE, 'w'), indent=1, sort_keys=True)
    # la table de machine 1
    his = json.load(open(SIEN))
    hcel = {(c['creneau'], F(c['w2']), F(c['facteur'])): c for c in his['cellules']}
    n_cel_diff, n_flag_diff, n_N_diff, n_count_diff = 0, 0, 0, 0
    diffs = []
    for c in mine['cellules']:
        h = hcel[(c['creneau'], F(c['w2']), F(c['facteur']))]
        dN = c['N'] != h['N']
        n_N_diff += dN
        flags = [(a, b, j, d) for (a, b, j, d) in c['etiquettes']]
        hfl = [tuple(x) for x in h['etiquettes']]
        lab_diff = [x for x in zip(flags, hfl) if x[0] != x[1]]
        cnt = (c['n_jug'], c['n_dom']) != (h['n_jug'], h['n_dom'])
        n_count_diff += cnt
        n_flag_diff += len(lab_diff)
        if dN or lab_diff or cnt or c['eligible'] != h['eligible']:
            n_cel_diff += 1
            diffs.append((c['creneau'], c['w2'], c['facteur'], c['N'], h['N'], (c['n_jug'], c['n_dom']), (h['n_jug'], h['n_dom']), c['eligible'], h['eligible'], lab_diff[:3]))
    print('cellules de la table de machine 1 : %d ; cellules ou nos tables different (boite, comptes, un drapeau, ou l eligibilite) : %d' % (len(his['cellules']), n_cel_diff))
    print('boites differentes : %d ; comptes jugeables / domaine differents : %d ; drapeaux d etiquette (jugeable, domaine) differents : %d sur %d' % (n_N_diff, n_count_diff, n_flag_diff, 14 * len(mine['cellules'])))
    for d in diffs[:30]:
        print('   %s w2 %s x%s : N %s / %s ; (jug, dom) %s / %s ; eligible %s / %s ; etiquettes : %s' % d)
    # la table commune = le ET
    commune = {'creneaux': {}}
    desacc = []
    for s in ORDRE:
        hc = {F(c['w2']): c['eligible'] for c in his['creneaux'][s]['candidats']}
        lst = []
        for c in mine['creneaux'][s]['candidats']:
            w = F(c['w2'])
            lst.append({'w2': str(w), 'eligible': bool(c['eligible'] and hc[w])})
            if c['eligible'] != hc[w]:
                desacc.append((s, str(w), c['eligible'], hc[w]))
        commune['creneaux'][s] = {'candidats': lst, 'n': len(lst), 'n_eligibles': sum(1 for x in lst if x['eligible'])}
    print('desaccords sur l eligibilite d un w2 candidat (moi, machine 1) : %d' % len(desacc))
    for d in desacc:
        print('   %s %s : moi %s, machine 1 %s' % d)
    print('TABLE COMMUNE : ' + ' ; '.join('%s %d / %d' % (s, commune['creneaux'][s]['n_eligibles'], commune['creneaux'][s]['n']) for s in ORDRE))
    json.dump(commune, open(SORTIE_COMMUNE, 'w'), indent=1, sort_keys=True)
    # marges : cellules eligibles de peu
    de_peu = [c for c in mine['cellules'] if c['eligible'] and ((c['creneau'] in ('N', 'P') and (c['n_jug'] == JUG_MIN or c['n_dom'] == DOM_MIN)) or (c['creneau'] in ('BN', 'BP') and (c['n_jug'] == JUG_MIN or c['n_dom'] == BORD_MIN or c['n_hors'] == BORD_MIN)) or c['N'] == N_COUT)]
    print('cellules eligibles DE PEU (un compte au seuil) : %d' % len(de_peu))
    for c in de_peu[:20]:
        print('   %s w2 %s x%s : N %d, jugeables %d, domaine %d, hors %d' % (c['creneau'], c['w2'], c['facteur'], c['N'], c['n_jug'], c['n_dom'], c['n_hors']))
