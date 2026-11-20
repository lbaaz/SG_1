# -*- coding: ascii -*-
"""MES TROIS FEUILLES du gel "pont" (seconde partie), ECRITES DEPUIS LE TEXTE SEUL (sections 5.2, 5.4, 5.5, 7, 8, 9 de gel_pont_partie2_instrument_enonces_pre_enregistrement_v1.md, canon 428ac47649de31f3).
Machine 2, 2026-11-17. Je n'ai PAS lu lecture_densite_2d_pont_machine1_v1.py, lecture_boites_pont_machine1_v1.py ni verdict_pont_machine1_v1.py avant d'avoir rendu mes sorties sur les pieces de qualification.
Les feuilles ne calculent AUCUNE 2D : elles lisent les sorties des sondes. Choix de lecture quand le texte ne tranche pas : ecrits en tete de chaque fonction, "CHOIX".
Usage : py -3.11 -P feuilles_pont_machine2_v1.py densite <chaine.json> <cellule> <sortie.json> <A.json> <B.json> <C.json> <D.json>
        py -3.11 -P feuilles_pont_machine2_v1.py boites <registre clone> <sortie.json> <fichier.jsonl> ...
        py -3.11 -P feuilles_pont_machine2_v1.py verdict <boites.json> <sortie.json> [--min-boites N] <lecture_densite.json> ..."""
import json
import math
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))


def mediane(v):
    s = sorted(v)
    n = len(s)
    return 0.5 * (s[n // 2 - 1] + s[n // 2]) if n % 2 == 0 else s[n // 2]


# ------------------------------------------------------------------ 5.2 feuille de densite
def plateau(valeurs, seuil=1.05):
    """5.2 : parmi les fenetres de cinq barreaux consecutifs, celle de plus petit rapport max/min ; PLATEAU si ce rapport est <= 1.05 ; valeur = moyenne geometrique des cinq.
    CHOIX : un barreau absent (vide non suivi) ou non positif invalide toutes les fenetres qui le contiennent ; a rapport egal, la fenetre de plus petit indice (plus petit k)."""
    meilleur = None
    for i in range(len(valeurs) - 4):
        w = valeurs[i:i + 5]
        if any(v is None or not v > 0 for v in w):
            continue
        r = max(w) / min(w)
        if meilleur is None or r < meilleur[0]:
            meilleur = (r, i)
    if meilleur is None or meilleur[0] > seuil:
        return None
    w = valeurs[meilleur[1]:meilleur[1] + 5]
    return math.exp(sum(math.log(v) for v in w) / 5.0)


def densite(chaine_json, cellule, sortie, fichiers, tol_etendue=0.02):
    """CHOIX : rho = rho_flux (celle qui s'ecrit (eta/pi) somme W |y|^2 ; rho_direct est l'autre lecture, comparee a part) ; ln rho_3(x) = ln(rho_3 |delta|) de la table - ln|delta| ;
    ln rho_2(x) = ln rho_3 + pas ; w0 = mediane sur les absorbeurs de la mediane sur les barreaux SUIVIS."""
    ch = json.load(open(chaine_json))[cellule]
    delta = ch['delta']
    ld = math.log(abs(delta))
    X = [0.05, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    sorties = [json.load(open(f)) for f in fichiers]
    nom_abs = [s['absorbeur'] for s in sorties]
    assert sorted(nom_abs) == ['A', 'B', 'C', 'D'], nom_abs
    for s in sorties:
        assert s['X'] == X and s['w2'] == '%d/%d' % (F(ch['w2']).numerator, F(ch['w2']).denominator) and s['m'] == ch['m'] and s['g'] == ch['g'], 'la sortie ne porte pas la cellule'
    for s in sorties:
        assert sorted(int(k) for k in s['k']) == list(range(-3, 9)), 'sortie de sonde INCOMPLETE : les douze barreaux -3 a 8 doivent tous y etre (la sonde reecrit son fichier a chaque barreau)'
    w0_abs = []
    for s in sorties:
        ws = [s['k'][k]['w0'] for k in sorted(s['k'], key=int) if s['k'][k].get('suivi')]
        w0_abs.append(mediane(ws))
    w0 = mediane(w0_abs)
    par_x = []
    for i, x in enumerate(X):
        pl = []
        for s in sorties:
            ks = sorted(s['k'], key=int)
            vals = [s['k'][k]['rho_flux'][i] if s['k'][k].get('suivi') else None for k in ks]
            pl.append(plateau(vals))
        lisible = all(p is not None for p in pl)
        e = dict(x=x, plateaux=[(None if p is None else math.log(p)) for p in pl], lisible=bool(lisible))
        if lisible:
            lns = [math.log(p) for p in pl]
            e['etendue'] = max(lns) - min(lns)
            e['lisible'] = e['etendue'] <= tol_etendue
            ln2d = mediane(lns)
            ln3 = ch['ln_rho3_delta'][i] - ld
            ln2 = ln3 + ch['pas'][i]
            e.update(ln_rho_2D=ln2d, ln_R3=ln2d - math.log(w0) - ln3, ln_R2=ln2d - math.log(w0) - ln2)
        par_x.append(e)
    lis = [e for e in par_x if e['lisible']]
    out = dict(cellule=cellule, w2=ch['w2'], m=ch['m'], g=ch['g'], delta=delta, X=X, w0=w0, par_x=par_x, ecarts_lisibles=len(lis),
               ln_R3_max_abs=max((abs(e['ln_R3']) for e in lis), default=None), etendue_absorbeurs_max=max((e['etendue'] for e in par_x if 'etendue' in e), default=None))
    json.dump(out, open(sortie, 'w', encoding='ascii'), indent=1, sort_keys=True)
    print('%s : %d ecarts lisibles sur 12 ; w0 %.8f ; plus grand |ln R3| %s' % (cellule, len(lis), w0, '%.4f' % out['ln_R3_max_abs'] if lis else '-'))


# ------------------------------------------------------------------ 5.4 feuille des boites
def groupe_de(cote):
    return 'UN' if 180 <= cote <= 189 else ('DEUX' if 291 <= cote <= 300 else None)


def boites(registre, sortie, fichiers, fiable_tol=0.02):
    """CHOIX : fenetre 0.05 < x < 8 (stricte) ; c2 d'un niveau = moyenne de ses deux lectures par partition (c2_a, c2_b) ; FIABLE si |c2_a - c2_b| <= 2 pour cent de leur moyenne ;
    compte VALIDE si w0 >= 0.5, residu_vide <= 1e-9, les deux lectures couvrent la fenetre (couverte_a, couverte_b), memes niveaux (listes_identiques) ; rho_3(x) vient de MA chaine
    (chaine_pont_machine2_v1.py), evaluee a l'ecart x du niveau ; un cote en double dans une cellule est refuse."""
    sys.path.insert(0, HERE)
    import chaine_pont_machine2_v1 as C
    ch = C.Chaine(registre)
    cache = {}
    res = []
    vus = set()
    for f in fichiers:
        for ligne in open(f):
            if not ligne.strip():
                continue
            b = json.loads(ligne)
            cle = (b['w2'], b['m'], b['g'])
            if cle not in cache:
                cache[cle] = ch.cellule(b['w2'], b['m'], b['g'])
            cel = cache[cle]
            assert (cle, b['cote']) not in vus, 'cote en double : %s %s' % (cle, b['cote'])
            vus.add((cle, b['cote']))
            D = abs(float(F(b['w2'])) - 2.0)
            niv = [n for n in b['niveaux'] if 0.05 < n['x'] < 8.0]
            ys, fiabs, xs = [], [], []
            for n in niv:
                c2 = n['c2_a'] if os.environ.get('PONT_C2') == 'a' else 0.5 * (n['c2_a'] + n['c2_b'])      # le texte ne dit pas quelle lecture : voir la certification
                rho3 = math.exp(cel.lisse(n['x'], 3))
                ys.append(c2 / (b['w0'] * rho3 * D))
                fiabs.append(abs(n['c2_a'] - n['c2_b']) <= fiable_tol * c2)
                xs.append(n['x'])
            somme = sum(ys)
            valide = bool(b['w0'] >= 0.5 and b['residu_vide'] <= 1e-9 and b['couverte_a'] and b['couverte_b'] and b['listes_identiques'] and b['n'] == b['n_b'])
            non_fiable = sum(y for y, fb in zip(ys, fiabs) if not fb)
            lisible = bool(valide and non_fiable <= 0.05 * somme)
            w = [y / somme for y in ys] if somme > 0 else []
            part = 1.0 / sum(t * t for t in w) if w else float('nan')
            res.append(dict(cellule_cle=list(cle), cote=b['cote'], groupe=groupe_de(b['cote']), n=len(niv), n_fichier=b['n'], valide=valide, lisible=lisible, S=somme / 7.95,
                            fiables=int(sum(fiabs)), non_fiable_part=(non_fiable / somme if somme > 0 else None), participation=part, x=xs, y=ys, fiable=fiabs))
    json.dump(dict(boites=res), open(sortie, 'w', encoding='ascii'), indent=1, sort_keys=True)
    print('%d boites ; valides %d ; lisibles %d' % (len(res), sum(r['valide'] for r in res), sum(r['lisible'] for r in res)))


# ------------------------------------------------------------------ 5.5 feuille de verdict (sections 7, 8, 9)
def verdict(boites_json, sortie, lectures, min_boites=8):
    """Applique la section 7 aux sorties des deux feuilles. CHOIX : la cellule d'une boite est (w2, m) ; son creneau MG si w2 < 2, PG sinon ; le compte reduit d'un groupe utilise la moyenne des
    cotes des boites de compte VALIDE du groupe ; la moyenne de S utilise les boites LISIBLES ; une famille sans cellule lisible est NON JUGEE."""
    B = json.load(open(boites_json))['boites']
    L = {}
    for f in lectures:
        d = json.load(open(f))
        L[d['cellule']] = d
    cellules = {}
    for nom, d in L.items():
        cle = (d['w2'], d['m'], d['g'])
        cellules[nom] = dict(densite=d, boites=[b for b in B if tuple(b['cellule_cle']) == cle])
        for b in cellules[nom]['boites']:
            pass
    out = {'cellules': {}, 'familles': {}, 'questions': {}}
    for nom, c in cellules.items():
        d, bs = c['densite'], c['boites']
        delta = abs(d['delta'])
        r = {}
        # (L) et (L2)
        lis = [e for e in d['par_x'] if e['lisible']]
        L_lisible = len(lis) >= 10
        L_tient = L_lisible and all(abs(e['ln_R3']) <= 0.05 for e in lis)
        grands = [e for e in lis if e['x'] >= 5]
        L2_tient = L_lisible and all(abs(e['ln_R3']) < abs(e['ln_R2']) for e in grands)
        r['L'] = dict(lisible=L_lisible, tient=(L_tient if L_lisible else None), ecarts_lisibles=len(lis), pire=max((abs(e['ln_R3']) for e in lis), default=None))
        r['L2'] = dict(lisible=L_lisible, tient=(L2_tient if L_lisible else None))
        # (S)
        gr = {g: [b for b in bs if b['groupe'] == g] for g in ('UN', 'DEUX')}
        S_lis = {g: [b for b in gr[g] if b['lisible']] for g in gr}
        S_lisible = all(len(S_lis[g]) >= min_boites for g in gr)
        toutes = S_lis['UN'] + S_lis['DEUX']
        mS = sum(b['S'] for b in toutes) / len(toutes) if toutes else float('nan')
        mSg = {g: (sum(b['S'] for b in S_lis[g]) / len(S_lis[g]) if S_lis[g] else float('nan')) for g in gr}
        S_tient = S_lisible and 0.85 <= mS <= 1.15 and all(0.80 <= mSg[g] <= 1.20 for g in gr)
        sd = (sum((b['S'] - mS) ** 2 for b in toutes) / (len(toutes) - 1)) ** 0.5 if len(toutes) > 1 else float('nan')
        r['S'] = dict(lisible=S_lisible, tient=(S_tient if S_lisible else None), moyenne=mS, erreur=sd / math.sqrt(len(toutes)) if len(toutes) > 1 else None, par_groupe=mSg, boites_lisibles={g: len(S_lis[g]) for g in gr})
        # (C)
        C_val = {g: [b for b in gr[g] if b['valide']] for g in gr}
        C_lisible = all(len(C_val[g]) >= min_boites for g in gr)
        mn = {g: (sum(b['n'] for b in C_val[g]) / len(C_val[g]) if C_val[g] else float('nan')) for g in gr}
        mc = {g: (sum(b['cote'] for b in C_val[g]) / len(C_val[g]) if C_val[g] else float('nan')) for g in gr}
        red = {g: mn[g] / (mc[g] * 7.95 * delta) for g in gr}
        rap = mn['DEUX'] / mn['UN'] if C_val['UN'] and C_val['DEUX'] else float('nan')
        C_tient = C_lisible and all(0.33 <= red[g] <= 0.55 for g in gr) and 1.25 <= rap <= 1.85
        r['C'] = dict(lisible=C_lisible, tient=(C_tient if C_lisible else None), compte_reduit=red, rapport=rap, n_moyen=mn)
        # questions
        q = {}
        if toutes:
            q['Q1_moyenne_S'] = mS
        for g in gr:
            if S_lis[g]:
                q['Q2_%s' % g] = (sum(1.0 / b['participation'] for b in S_lis[g]) / len(S_lis[g])) / (sum(3.0 / (b['n'] + 2) for b in S_lis[g]) / len(S_lis[g]))
        # (Q3) la somme relue avec la densite 2D : y / R3(x), ln R3 interpole lineairement en x entre les ecarts lisibles (plat au-dela). CHOIX : boites lisibles des deux groupes
        xs_l = [e['x'] for e in lis]
        if len(lis) >= 2 and toutes:
            def lnR3(x):
                if x <= xs_l[0]:
                    return lis[0]['ln_R3']
                if x >= xs_l[-1]:
                    return lis[-1]['ln_R3']
                for a, b in zip(lis, lis[1:]):
                    if a['x'] <= x <= b['x']:
                        return a['ln_R3'] + (b['ln_R3'] - a['ln_R3']) * (x - a['x']) / (b['x'] - a['x'])
            q['Q3_somme_densite_2D'] = sum(sum(y / math.exp(lnR3(x)) for y, x in zip(b['y'], b['x'])) / 7.95 for b in toutes) / len(toutes)
        r['questions'] = q
        out['cellules'][nom] = r
    for fam in ('L', 'L2', 'S', 'C'):
        lisibles = {n: out['cellules'][n][fam] for n in out['cellules'] if out['cellules'][n][fam]['lisible']}
        tombees = sorted(n for n, v in lisibles.items() if v['tient'] is False)
        creneaux = {n: ('MG' if L[n]['delta'] < 0 else 'PG') for n in L}
        def etat(noms):
            lis = [n for n in noms if n in lisibles]
            if any(lisibles[n]['tient'] is False for n in lis):
                return 'TOMBEE'
            if len(lis) >= 4 and {creneaux[n] for n in lis} >= {'MG', 'PG'}:
                return 'TENUE'
            return 'NON JUGEE'
        out['familles'][fam] = dict(etat=etat(list(L)), cellules_lisibles=sorted(lisibles), tombees=tombees,
                                    par_creneau={s: etat([n for n in L if creneaux[n] == s]) for s in ('MG', 'PG')})
    # (Q2), lue PAR GROUPE en confondant les cellules (le texte dit "par groupe" sans dire si la cellule est l'unite) : toutes les boites lisibles de chaque groupe
    for g in ('UN', 'DEUX'):
        bl = [b for nom in cellules for b in cellules[nom]['boites'] if b['groupe'] == g and b['lisible']]
        if bl:
            out['questions']['Q2_groupe_%s' % g] = dict(boites=len(bl), rapport=(sum(1.0 / b['participation'] for b in bl) / len(bl)) / (sum(3.0 / (b['n'] + 2) for b in bl) / len(bl)))
    json.dump(out, open(sortie, 'w', encoding='ascii'), indent=1, sort_keys=True)
    for fam, v in out['familles'].items():
        print('(%s) %s ; lisibles %s ; tombees %s ; par creneau %s' % (fam, v['etat'], v['cellules_lisibles'], v['tombees'], v['par_creneau']))


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'densite':
        densite(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5:])
    elif cmd == 'boites':
        boites(sys.argv[2], sys.argv[3], sys.argv[4:])
    else:
        args = sys.argv[4:]
        mb = 8
        if args and args[0] == '--min-boites':
            mb = int(args[1])
            args = args[2:]
        verdict(sys.argv[2], sys.argv[3], args, mb)
