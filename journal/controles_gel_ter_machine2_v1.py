# -*- coding: ascii -*-
"""CONTROLES DE LECTURE du gel E-B ter (432319b9feb34b82) par machine 2 : chaque nombre qui peut etre relu dans une source l'est. AUCUN calcul 2D.
Sources : le lot de machine 1 (4103... non : 42110a3d1eabdaa0, dossier du lot extrait), le registre a 8d54bf9 (clone neuf), la note de machine 1 (42c822811167b826),
mon rejeu (lot 29073aa2ac4decac) pour ce que la note de machine 1 dit des six points de M17, et MA feuille (feuille_independante_ter_machine2_v1.py) pour juger
les sorties de machine 1 (reglage, etage 0, etage 1). Chaque controle imprime TIENT ou MORD ; un controle qui mord n'est pas retouche, il est dit.
Usage : py -3.11 -I controles_gel_ter_machine2_v1.py <dossier lot m1> <clone registre> <racine BOCAL4> <rejeu.json> <sortie.json>"""
import hashlib
import json
import math
import os
import re
import statistics
import sys
import unicodedata
from fractions import Fraction as F

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import feuille_independante_ter_machine2_v1 as MA

LOT, CLONE, RACINE, REJEU, SORTIE = [os.path.abspath(a) for a in sys.argv[1:6]]
res = []


def canon(octets):
    t = unicodedata.normalize('NFC', octets.decode('utf-8')).replace('\r\n', '\n').encode()
    return hashlib.sha256(t).hexdigest()[:16]


def lire(p, mode='rb'):
    return open(p, mode).read()


def C(nom, ok, detail):
    res.append((nom, bool(ok), detail))
    print('%-5s %-6s %s' % (nom, 'TIENT' if ok else 'MORD', detail), flush=True)


gel = lire(os.path.join(LOT, 'qualification_EB_ter_pre_enregistrement_v1.md')).decode('utf-8')
nn = re.sub(r'\s+', ' ', gel)
man = lire(os.path.join(RACINE, 'MANIFEST_lot_machine1_gel_EB_ter_v1.txt'))
att = {}
for l in man.decode('utf-8').split('\n'):
    p = l.split()
    if len(p) == 5 and re.fullmatch(r'[0-9a-f]{16}', p[0]):
        att[p[4]] = p[0]
dep = json.load(open(os.path.join(CLONE, 'journal', 'sonde_ordre2.json')))
P = {p['id']: p for p in dep['points']}
JUGES = list(MA.JUGES)

# ---- K01 : le lot et le gel
pieces_ok = all(canon(lire(os.path.join(LOT, n))) == c for n, c in att.items())
C('K01', canon(man) == '42110a3d1eabdaa0' and len(att) == 55 and pieces_ok and att['qualification_EB_ter_pre_enregistrement_v1.md'] == '432319b9feb34b82',
  'lot %s, %d pieces au manifeste, toutes au canon dans le dossier extrait : %s ; gel %s' % (canon(man), len(att), pieces_ok, att['qualification_EB_ter_pre_enregistrement_v1.md']))

# ---- K02 : les cinq canons que le gel nomme dans ses sections 10 et 16
noms5 = {'sonde': ('sonde_qualification_EB_ter_machine1_v1.py', 'b5616dcf858e8801'), 'bloc': ('lecteur_plateau_bloc_machine1_v1.py', '9b0f95f3e10e9b0d'),
         'feuille': ('lecture_qualification_EB_ter_machine1_v1.py', 'b2d6d7cfaf30f1cf'), 'banc': ('banc_feuille_ter_machine1_v1.py', '6b63a9de25107ae4'),
         'ancres': ('reference_ancres_ter_machine1_v1.json', '6600fb8418c79930')}
ok5 = all(att[f] == c and c in gel and canon(lire(os.path.join(LOT, f))) == c for f, c in noms5.values())
C('K02', ok5, 'sonde, bloc, feuille, banc, reference des ancres : canon au manifeste == canon recalcule == canon ecrit dans le gel (5 sur 5)')

# ---- K03 : la section 2, chaque canon relu a son chemin
sec2 = gel.split('## 2. Sources')[1].split('## 3.')[0]
lignes = re.findall(r'^ {4}([0-9a-f]{16}) {2}(\S+)', sec2, re.M)
bad, vus = [], 0
for c, chemin in lignes:
    if '/' in chemin:
        f = os.path.join(CLONE, chemin)
    else:
        f = os.path.join(RACINE, chemin)
    if not os.path.isfile(f):
        bad.append((c, chemin, 'absent'))
        continue
    vus += 1
    if canon(lire(f)) != c:
        bad.append((c, chemin, canon(lire(f))))
C('K03', len(lignes) == 11 and not bad, '%d canons de la section 2 relus a leur chemin (registre 8d54bf9 ou racine) : %d resolus, hors canon %s' % (len(lignes), vus, bad))
man_m1 = lire(os.path.join(RACINE, 'MANIFEST_lot_machine1_note_piste0_reprise_v1.txt'))
C('K03b', canon(man_m1) == '4103eae43f989877' and '4103eae43f989877' in gel, 'le lot de la note, 4103eae43f989877, recalcule de son manifeste : %s' % canon(man_m1))

# ---- K04 : le tableau des douze points, recalcule du depot
tab = re.findall(r'^ {2}([CML][1-4]) +(\d+/\d+) +(\d+/\d+) +(\d+) +(\d+) +(\d+), (\d+), (\d+), (\d+)$', gel, re.M)
ecarts = []
for i, w2, fac, r_c, n, nA, nB, nC, nD in tab:
    p = P[i]
    ju = [e for e in p['etats'] if (e.get('Gamma_2D') or {}).get('3') is not None and e['Gamma_2D']['3'] > MA.__dict__.get('PLANCHER10', 1.33e-12)]
    attendu = (p['w2'], p['facteur'], str(p['r_c']), str(len(ju)), str(p['r_c'] + 80), str(p['r_c'] + 100), str(p['r_c'] + 100), str(p['r_c'] + 90))
    if (w2, fac, r_c, n, nA, nB, nC, nD) != attendu:
        ecarts.append((i, (w2, fac, r_c, n, nA, nB, nC, nD), attendu))
    if abs(p['eta0'] - abs(float(F(int(w2.split('/')[0]), int(w2.split('/')[1])) - 2))) > 1e-15:
        ecarts.append((i, 'eta0', p['eta0']))
C('K04', len(tab) == 12 and not ecarts and sum(int(t[4]) for t in tab) == 137, 'tableau du gel (12 lignes) == depot recalcule : w2, facteur, r_c, etats juges, N sous A, B, C, D, et eta0 = |w2 - 2| ; somme des etats %d ; ecarts %s'
  % (sum(int(t[4]) for t in tab), ecarts))

# ---- K05 : les comptes de G-T5
n_e0 = sum(len(P[a]['etats']) * 3 for a in ('A1', 'A2'))
n_anc = sum(2 for a in ('A1', 'A2')) * 4 * 12
n_tp = 2 * 4 * 12
n_tn = 2 * 4 * 12
n_juges = sum(len([e for e in P[i]['etats'] if (e.get('Gamma_2D') or {}).get('3') is not None and e['Gamma_2D']['3'] > 1.33e-12]) for i in JUGES)
C('K05', (n_e0, n_anc, n_tp, n_tn, n_juges * 4 * 12) == (84, 192, 96, 96, 6576), 'comptes G-T5 recalcules : etage 0 %d, ancres %d, TP %d, TN %d, etage 2 %d lectures (%d etats x 4 x 12)' % (n_e0, n_anc, n_tp, n_tn, n_juges * 48, n_juges))

# ---- K06 : les etats juges ont un rang 0, des etiquettes uniques (la feuille refuserait sinon) ; les ancres ont 14 etats lus a k = 2, 3, 4
ok6 = True
for i in JUGES:
    ju = [e for e in P[i]['etats'] if (e.get('Gamma_2D') or {}).get('3') is not None and e['Gamma_2D']['3'] > 1.33e-12]
    ok6 = ok6 and len([e for e in ju if e['rang'] == 0]) == 1 and len(set((e['n1'], e['n2']) for e in ju)) == len(ju)
ok6 = ok6 and all(len(P[a]['etats']) == 14 and all((e.get('Gamma_2D') or {}).get(k) is not None for e in P[a]['etats'] for k in '234') for a in ('A1', 'A2'))
C('K06', ok6, 'aux douze points : un etat de rang 0 juge et des etiquettes (n1, n2) deux a deux distinctes ; aux ancres A1 et A2 : 14 etats, largeurs deposees a k = 2, 3, 4')

# ---- K07 : section 4 (v), les ecarts de la largeur deposee entre k = 2, 3, 4
sp = []
for i in JUGES:
    for e in P[i]['etats']:
        G = e.get('Gamma_2D') or {}
        if G.get('3') is not None and G['3'] > 1.33e-12:
            v = [G[k] for k in '234']
            sp.append(max(v) / min(v) - 1.0)
C('K07', abs(statistics.median(sp) - 0.074) < 5e-4 and abs(max(sp) - 0.221) < 5e-4 and '0.074 en mediane et de 0.221 au pire' in nn,
  'section 4 (v) : ecart entre k = 2, 3 et 4 : mediane %.4f, pire %.4f sur %d etats (le gel : 0.074, 0.221, 137)' % (statistics.median(sp), max(sp), len(sp)))

# ---- K08 : les annonces
a1 = [float(x) for x in re.findall(r'(?:ESTIMATEUR QUALIFIE|QUALIFIE A L\'ETAT LU|QUALIFIE PAR POINT|NON QUALIFIE|NON LISIBLE|NON CONCLUANT D\'INSTRUMENT) : (0\.\d+)', nn.split(' A-1 le verdict.')[1].split(' A-2 ')[0])]
a2 = [float(x) for x in re.findall(r'(?:PLATEAU a tous les etats|DIX AU MOINS|PAS PARTOUT) : (0\.\d+)', nn.split(' A-2 l')[1].split(' A-3 ')[0])]
C('K08', len(a1) == 6 and abs(sum(a1) - 1.0) < 1e-12 and len(a2) == 3 and abs(sum(a2) - 1.0) < 1e-12, 'annonces : A-1 six probabilites, somme %.2f ; A-2 trois, somme %.2f' % (sum(a1), sum(a2)))

# ---- K09 : constantes du gel contre le texte de la sonde, de la feuille et du bloc
sonde = lire(os.path.join(LOT, 'sonde_qualification_EB_ter_machine1_v1.py')).decode()
feuille = lire(os.path.join(LOT, 'lecture_qualification_EB_ter_machine1_v1.py')).decode()
motifs = [('ITER_MIN, ITER_MAX, TOL_RESIDU, POIDS_MIN = 2, 12, 1e-11, 0.5', sonde), ('KS = list(range(-3, 9))', sonde),
          ('[("A", "F2", 0, 80), ("B", "F2", 0, 100), ("C", "F1", 0, 100), ("D", "F2", 10, 80)]', sonde), ('PLANCHER10 = 1.33e-12', sonde),
          ('TP_W2, TP_RC, TP_ETA0 = F(39, 20), 40, 0.05', sonde), ('TAU = Fraction(1, 20)', feuille), ('TAU_F = 0.05', feuille),
          ('TOL_E0_REL, TOL_E0_ABS = 1e-3, 1e-12', feuille), ('TOL_ANCRE = 1e-6', feuille), ('PART_ETATS = Fraction(9, 10)', feuille),
          ('K_MIN, K_MAX = -3, 8', feuille)]
manque = [m for m, t in motifs if m not in t]
textes = ['k = -3, -2, ..., 8', 'tau = 0.05', 'Au moins 2 iterations, au plus 12', '1e-11', '0.5 : poids au site', 'F2 : W = (r - B)^4 / L^2', 'B = r_c + 10, L = 80',
          'L = 100  -- longueur', 'F1, B = r_c,      L = 100  -- forme']
manque_g = [t for t in textes if re.sub(r'\s+', ' ', t) not in nn]
C('K09', not manque and not manque_g, 'constantes de la sonde et de la feuille == texte du gel (11 + 9 controles) ; manque dans le code %s, dans le gel %s' % (manque, manque_g))

# ---- K10 : la note de machine 1 relue dans MON rejeu (section 4 (i) du gel : pire etalement 0.0152, accord a 0.0070)
rj = json.load(open(REJEU))
et, sp5 = [], []
for pt in ('39_20', '197_100', '99_50', '101_50', '203_100', '41_20'):
    r = [x for x in rj['resultats'] if x['nature'] == 'pt' and x['nom'] == pt]
    g = []
    for c in ('F2_60', 'F2_80', 'F1_80', 'F3_60', 'F1T_60'):
        for x in r:
            if c in x['configs']:
                pl = x['configs'][c]['resume']['plateau_A']
                et.append(pl['etalement'])
                g.append(pl['Gamma_pl'])
    sp5.append(max(g) / min(g) - 1.0)
C('K10', abs(max(et) - 0.0152) < 5e-5 and abs(max(sp5) - 0.0070) < 5e-5, 'section 4 (i) : sous les cinq absorbeurs longs de la note, pire etalement %.4f (gel 0.0152), plus grand ecart entre les cinq valeurs de plateau %.4f (gel 0.0070) ; relu dans MON rejeu, qui n a pas ete fait pour cela'
  % (max(et), max(sp5)))

# ---- K11 : (iii) le temoin positif et negatif de machine 1 juges par MA feuille
e1 = json.load(open(os.path.join(LOT, 'essai_m1_sonde_ter_etage1.json')))
ref = json.load(open(os.path.join(CLONE, 'journal', 'tp_reference_machine2_v1.json')))
tab_ref = {r['j']: r for r in ref['balayage']}
pire_tp, ok_tp = 0.0, 0
for v in e1['temoin']:
    r = tab_ref[v['j']]
    for x in 'ABCD':
        pl = MA.plateau(v['traj'][x])
        if pl['statut'] == 'PLATEAU':
            pire_tp = max(pire_tp, abs(math.log(pl['Gamma_pl'] / r['Gamma_ref'])))
        ok_tp += MA.tient_temoin_positif(v['traj'][x], r['Gamma_ref'], r['u_ref'])
rap, g3 = [], []
n_tn_pl = 0
for t in e1['temoin_negatif']:
    for x in 'ABCD':
        tr = t['traj'][x]
        n_tn_pl += not MA.tient_temoin_negatif(tr)
        for k in range(-3, 8):
            rap.append(tr[str(k)]['gamma'] / tr[str(k + 1)]['gamma'])
        g3.append(tr['3']['gamma'])
C('K11', ok_tp == 8 and abs(pire_tp - 0.0007) < 5e-5 and n_tn_pl == 0 and max(abs(r - 2.0) for r in rap) < 0.0021 and min(g3) > 5e-53 and max(g3) < 2.5e-39,
  '(iii) : TP tient %d sur 8, pire |ln(Gamma_pl / ref)| %.4f (gel 0.0007) ; TN : plateau %d sur 8, rapport entre barreaux voisins a %.4f de 2 au plus (gel 0.002), largeur a k = 3 de %.1e a %.1e (gel 1e-52 a 2e-39)'
  % (ok_tp, pire_tp, n_tn_pl, max(abs(r - 2.0) for r in rap), min(g3), max(g3)))

# ---- K12 : (iv) l'etage 0 de machine 1 juge par MA feuille, et l'ecart des deux lectures sur les 1824 lectures du reglage
e0 = json.load(open(os.path.join(LOT, 'essai_m1_sonde_ter_etage0.json')))
n, hors, pa, pr = 0, 0, 0.0, 0.0
for pt in e0['points']:
    d = {e['rang']: e for e in P[pt['id']]['etats']}
    for e in pt['etats']:
        for k in (2, 3, 4):
            r = e['traj']['depot'][str(k)]
            gd = d[e['rang']]['Gamma_2D'][str(k)]
            n += 1
            hors += not MA.tient_etage0(r['gamma'], r['suivi'], gd)
            pa = max(pa, abs(r['gamma'] - gd))
            if gd > 1.33e-10:
                pr = max(pr, abs(r['gamma'] - gd) / gd)
reg = {}
for f in ('reglage_p1.json', 'reglage_p2.json'):
    reg.update(json.load(open(os.path.join(LOT, f)))['points'])
nl, pe = 0, 0.0
for p in reg.values():
    for e in p['etats'].values():
        for x in 'ABCD':
            for k, r in e['cfg'][x].items():
                nl += 1
                if r['gamma'] > 0:
                    pe = max(pe, abs(r['gamma_im'] - r['gamma']) / r['gamma'])
C('K12', n == 84 and hors == 0 and abs(pa - 5.8e-13) < 5e-14 and abs(pr - 2.9e-4) < 5e-5 and nl == 1824 and abs(pe - 6e-4) < 1e-4,
  '(iv) : etage 0 de machine 1 : %d lectures, %d hors tolerance, pire ecart absolu %.1e (gel 5.8e-13), relatif au-dessus de mille planchers %.1e (gel 2.9e-4) ; reglage : %d lectures, -2 Im(lambda) s ecarte de 2 eta <W> de %.1e au pire (gel 6e-04)'
  % (n, hors, pa, pr, nl, pe))

print('')
print('CONTROLES : %d, dont %d tiennent, %d mordent' % (len(res), sum(1 for r in res if r[1]), sum(1 for r in res if not r[1])))
json.dump([{'nom': a, 'tient': b, 'detail': c} for a, b, c in res], open(SORTIE, 'w'), indent=1)
sys.exit(0 if all(r[1] for r in res) else 1)
