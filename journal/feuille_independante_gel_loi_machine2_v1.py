# -*- coding: ascii -*-
"""MA FEUILLE D'ORDRE 3 (seconde implementation) -- machine 2, 2026-11-16. Ecrite a partir des sections 5 et 6 du gel (543d8b33e5c9afb8) SEULES ;
la feuille de machine 1 (facd3ceeec07d3bf) n'a servi qu'a lire le FORMAT des fichiers d'entree. Aucun calcul 2D : des chaines a une dimension.
Les chaines sont MES chaines : moteur (gamma_chaine du moteur), ordre 2 (bloc depose 7cd5977bc27bebc1), ordre 3 (ma classe Chaine, reprise de
controle_ordre3_machine2/ordre3_machine2_v1.py, que j'ai rederivee et validee), e_bord = energie du dernier site de la barriere (ma definition de la carte).
Ne controle PAS les canons ni la provenance (ce sont les gardes de machine 1, mordues par son banc) : elle juge. Les ancres de la sonde dense sont comparees (4.4).
Usage en bibliotheque : charger(moteur, bloc2, script3) puis juger(table, dense, verdict, depot_dense) ; en script :
  py -3.11 -P feuille_independante_gel_loi_machine2_v1.py <moteur> <bloc2> <ordre3_machine2_v1.py> <table.json> <dense.json> <verdict.json> <depot.json> <sortie.json>"""
import importlib.machinery
import importlib.util
import json
import math
import os
import sys
import tempfile
from fractions import Fraction as F

import numpy as np

EF = 0.0625
ETAS = (0.25, 0.125, 0.0625, 0.03125)
LIGNES = ('N', 'P')
BORDS = ('BN', 'BP')
_ENV = {}


def charger(moteur, bloc2, script3):
    spec = importlib.util.spec_from_file_location('moteur', moteur)
    M = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(M)
    ld = importlib.machinery.SourceFileLoader('bloc2', bloc2)
    B2 = importlib.util.module_from_spec(importlib.util.spec_from_loader('bloc2', ld))
    B2.M, B2.np, B2.math = M, np, math
    ld.exec_module(B2)
    src = open(script3, encoding='ascii').read()
    a_, b_ = src.index('# les sauts hors echelle'), src.index('def epreuve_boite')
    ent = "import math\nimport numpy as np\nfrom fractions import Fraction as F\nP = M.P\nW1 = float(M.W1)\nC0, C1 = M.CANAL\n"
    chem = os.path.join(tempfile.mkdtemp(), 'chaine_reprise.py')
    open(chem, 'w', encoding='ascii').write(ent + src[a_:b_])
    ld3 = importlib.machinery.SourceFileLoader('chaine_reprise', chem)
    C = importlib.util.module_from_spec(importlib.util.spec_from_loader('chaine_reprise', ld3))
    C.M = M
    ld3.exec_module(C)
    _ENV.update(M=M, B2=B2, C=C, cache={})


def _stable(v):
    return all(x > 0 for x in v) and max(v) / min(v) <= 2.0


def chaines(w2, g, a, b):
    """MES chaines a l'etiquette (a, b) : barriere, e_bord, stabilites moteur / ordre 2, G2 et G3 au facteur 1/16, stabilite de l'ordre 3."""
    cle = (str(w2), repr(g), a, b)
    c = _ENV['cache']
    if cle in c:
        return c[cle]
    M, B2, C = _ENV['M'], _ENV['B2'], _ENV['C']
    sites = M.barriere(float(a), float(b), w2, g, True)
    if not sites:
        r = {'vide': True}
    else:
        G1 = [float(M.gamma_chaine(float(a), float(b), w2, g, sites, eta_facteur=x, M_facteur=4)['Gamma_c']) for x in ETAS]
        tb = B2.tables_ordre2(float(a), float(b), w2, g, sites, M_facteur=4)
        G2 = [B2.gamma_chaine_ordre2(tb, x)['Gamma_flux'] for x in ETAS]
        ch = C.Chaine(float(a), float(b), w2, g)
        G3 = C.chaine3(tb, ch, EF)['Gamma_flux']
        var = [C.chaine3(tb, ch, 2 * EF)['Gamma_flux'], C.chaine3(tb, ch, EF / 2)['Gamma_flux'], C.chaine3(tb, ch, EF, recul=4)['Gamma_flux']]
        stab3 = max(abs(math.log(v / G3)) for v in var) if G3 > 0 and all(v > 0 for v in var) else None
        r = {'vide': False, 'e_bord': sites[-1][1], 'stable1': _stable(G1), 'stable2': _stable(G2), 'G2': G2[2], 'G3': G3, 'stab3': stab3}
    c[cle] = r
    return r


def bande(w2):
    d = abs(F(str(w2)) - 2)
    if d <= F(6, 100):
        return 1.25
    if d <= F(10, 100):
        return 1.6
    if d <= F(12, 100):
        return 2.0          # delta 98 seulement ; hors du gel (les cellules sont a |delta| <= 0.076)
    return None


def ancres_tiennent(table, dense, depot):
    """Gel 4.4 : les deux ancres rejouees portent les memes etiquettes que le depot, Gamma_2D(3) a 1e-3 relatif + 1e-12, energie a 1e-9."""
    anc = [p['id'] for p in table['points'] if p['role'] == 'ancre']
    if len(anc) != 2:
        return False, ['il faut exactement deux ancres']
    D = {p['id']: p for p in dense['points']}
    R = {p['id']: p for p in depot['points']}
    motifs = []
    for i in anc:
        if i not in D or i not in R or len(D[i]['etats']) != 14:
            motifs.append('ancre %s absente ou incomplete' % i)
            continue
        for u, v in zip(sorted(D[i]['etats'], key=lambda e: e['rang']), sorted(R[i]['etats'], key=lambda e: e['rang'])):
            if (u['n1'], u['n2']) != (v['n1'], v['n2']):
                motifs.append('ancre %s rang %d : etiquette' % (i, u['rang']))
            elif abs(u['Gamma_2D']['3'] - v['Gamma_2D']['3']) > 1e-12 + 1e-3 * abs(v['Gamma_2D']['3']) or abs(u['E_re'] - v['E_re']) > 1e-9:
                motifs.append('ancre %s rang %d : largeur ou energie' % (i, u['rang']))
    return (not motifs), motifs


def juger(table, dense, verdict, depot):
    ok_anc, motifs = ancres_tiennent(table, dense, depot)
    if verdict.get('instrument') != 'TIENT' or not ok_anc:
        return {'instrument': 'NE TIENT PAS', 'motifs_ancres': motifs}
    D = {p['id']: p for p in dense['points']}
    cells = []
    for pt in [p for p in table['points'] if p['role'] == 'juge']:
        pid, cr = pt['id'], pt['creneau']
        w2, fac = F(str(pt['w2'])), F(str(pt['facteur']))
        dp = D[pid]
        g = dp['g']
        B = bande(w2)
        labels = [(e['n1'], e['n2']) for e in dp['etats']]
        dens = {e['rang']: e for e in dp['etats']}
        etats = []
        for ev in sorted(verdict['points'][pid]['etats'], key=lambda x: x['rang']):
            e = dens[ev['rang']]
            r = {'rang': ev['rang'], 'exclu': None}
            if ev['statut'] != 'QUALIFIE':                       # 1. qualifie par le lecteur
                r['exclu'] = 'non qualifie'
            elif not e['J_ecart_type'] < 0.2:                    # 2. etiquette nette
                r['exclu'] = 'J flou'
            elif labels.count((e['n1'], e['n2'])) != 1:          # 3. etiquette unique parmi les 14
                r['exclu'] = 'etiquette double'
            else:
                c = chaines(w2, g, e['n1'], e['n2'])
                if c['vide']:                                    # 4. barriere non vide
                    r['exclu'] = 'barriere vide'
                elif not c['stable1']:                           # 5. moteur stable
                    r['exclu'] = 'chaine du moteur instable'
                elif not c['stable2']:                           # 5. ordre 2 stable
                    r['exclu'] = "chaine d'ordre 2 instable"
                else:
                    gp = ev['plateaux']['A']['Gamma_pl']
                    dom = bool(c['G3'] > 0 and c['e_bord'] < 0.7 and c['stab3'] is not None and c['stab3'] <= 0.05)
                    q2 = c['G2'] / gp
                    q3 = c['G3'] / gp if c['G3'] > 0 else None
                    T = 0.05 if c['e_bord'] < 0.3 else 0.10
                    l2 = abs(math.log(q2))
                    l3 = abs(math.log(q3)) if q3 else None
                    r.update({'domaine': dom, 'e_bord': c['e_bord'], 'stab3': c['stab3'], 'G2': c['G2'], 'G3': c['G3'], 'Gamma_pl': gp, 'ln_q2': math.log(q2),
                              'ln_q3': math.log(q3) if q3 else None, 'T': T, 'tient_E1': bool(dom and l3 <= T), 'pres': bool(dom and l3 < l2), 'bande_ok': bool(1.0 / B <= q2 <= B)})
            etats.append(r)
        jug = [r for r in etats if r['exclu'] is None]
        dom = [r for r in jug if r['domaine']]
        hors = [r for r in jug if not r['domaine']]
        assez = len(etats) > 0 and 3 * len(jug) >= 2 * len(etats)
        if cr in LIGNES:
            expl = assez and len(dom) >= 5
        else:
            expl = assez and len(dom) >= 2 and len(hors) >= 2
        e1 = 'INEXPLOITABLE' if not expl else ('TIENT' if all(r['tient_E1'] for r in dom) else 'TOMBE')
        n_pres = sum(r['pres'] for r in dom)
        seuil = -(-3 * len(dom) // 4)
        e2 = None if cr != 'N' else ('INEXPLOITABLE' if not expl else ('TIENT' if n_pres >= seuil else 'TOMBE'))
        e3 = 'VIDE' if not jug else ('TIENT' if all(r['bande_ok'] for r in jug) else 'TOMBE')
        cells.append({'id': pid, 'creneau': cr, 'n_lus': len(etats), 'n_juges': len(jug), 'n_domaine': len(dom), 'n_hors': len(hors), 'exploitable': bool(expl),
                      'E1': e1, 'E2': e2, 'E3': e3, 'n_pres': n_pres, 'seuil_E2': seuil, 'etats': etats})
    out = {'instrument': 'TIENT', 'cellules': cells}

    def issue(cs, cle, max_inexpl, chutes):
        if not cs:
            return 'SANS OBJET', []
        tomb = [c['id'] for c in cs if c[cle] == 'TOMBE']
        n_inexpl = sum(1 for c in cs if c[cle] == 'INEXPLOITABLE')
        if len(tomb) > chutes:
            return 'TOMBE', tomb
        if n_inexpl > max_inexpl:
            return 'NON CONCLUANT', tomb
        return ('TENU' if not tomb else 'TENU SAUF UNE CELLULE'), tomb
    lig = [c for c in cells if c['creneau'] in LIGNES]
    lN = [c for c in cells if c['creneau'] == 'N']
    brd = [c for c in cells if c['creneau'] in BORDS]
    out['E1'] = issue(lig, 'E1', 2, 1)
    out['E2'] = issue(lN, 'E2', 1, 1)
    out['E1B'] = issue(brd, 'E1', 0, 0)
    t3 = [c['id'] for c in cells if c['E3'] == 'TOMBE']
    out['E3'] = ('TENU' if not t3 else 'TOMBE', t3)
    return out


def main():
    moteur, bloc2, script3, ftable, fdense, fverdict, fdepot, fsortie = sys.argv[1:9]
    charger(moteur, bloc2, script3)
    out = juger(json.load(open(ftable)), json.load(open(fdense)), json.load(open(fverdict)), json.load(open(fdepot)))
    json.dump(out, open(fsortie, 'w'), indent=1, sort_keys=True)
    if out['instrument'] != 'TIENT':
        print('INSTRUMENT NE TIENT PAS', out['motifs_ancres'][:5])
        return
    for c in out['cellules']:
        print('  %-3s lus %2d juges %2d domaine %2d hors %2d %-13s E1 %-13s E2 %-13s E3 %s' % (
            c['id'], c['n_lus'], c['n_juges'], c['n_domaine'], c['n_hors'], 'exploitable' if c['exploitable'] else 'INEXPLOITABLE', c['E1'], c['E2'] or '-', c['E3']))
    for k in ('E1', 'E2', 'E1B', 'E3'):
        print('%-3s : %s %s' % (k, out[k][0], out[k][1]))


if __name__ == '__main__':
    main()
