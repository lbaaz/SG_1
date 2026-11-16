# -*- coding: ascii -*-
"""VERIFICATION DES NOMBRES DE L'ACTE DE m1 (journal_delta_nn_largeur_vide_v1.md, canon 464ba00a6905e3a5) CONTRE MES DONNEES -- machine 2, v1, 2026-11-16. Rien n'est juge ni ecrit dans le run.
Sources, toutes miennes ou du run : run_gel_vide_machine2/run_1 (verdict de la feuille jouee, 28 fichiers bruts, console), MES predictions (predictions_machine2_vide_v1.json : ln G1, G2, G3, Phi*, forme fermee, r3),
la table gelee (pour les attentes de signe), le verdict que m1 a rejoue (pour recompter les champs). Chaque tableau de l'acte (nn.3 deux tableaux, nn.6) est REFAIT ligne a ligne et compare au texte ;
chaque nombre de la prose que je peux recalculer l'est. Les controles que je ne peux pas faire sont nommes a la fin.
Usage : py -3.11 -I verifie_acte_machine2_v1.py"""
import json
import math
import os
import re
import statistics as st

B = r'd:\devs\bocal\BOCAL4'
RUN = os.path.join(B, r'run_gel_vide_machine2\run_1')
ACTE = open(os.path.join(B, r'livraison_16j_acte_gel_vide\journal_delta_nn_largeur_vide_v1.md'), encoding='utf-8').read().replace('\r\n', '\n')
V = json.load(open(os.path.join(RUN, 'verdict_vide.json')))
VR = json.load(open(os.path.join(B, r'livraison_16j_acte_gel_vide\ext\lot_m1\lot_machine1_2026-11-16_acte_gel_vide_v1\verdict_vide_rejoue_machine1.json')))
P = {c['id']: c for c in json.load(open(os.path.join(B, r'certif_gel_vide_partie2_machine2\predictions_machine2_vide_v1.json')))['cellules']}
TB = {c['id']: c for c in json.load(open(os.path.join(B, r'livraison_16h_gel_vide_partie2\ext\x_gel_vide_partie2\lot_machine1_2026-11-16_gel_vide_partie2_instrument_enonces_v1\table_cellules_gel_vide_v1.json')))['cellules']}
ordre = lambda i: (['MG', 'MP', 'PP', 'PG'].index(i[:2]), int(i[2:]))
C = sorted(V['cellules'], key=lambda c: ordre(c['id']))
IDS = [c['id'] for c in C]
D = {c['id']: c for c in C}
mauv = []
notes = []


def faux(s):
    mauv.append(s)
    print('  ** DIFFERENCE :', s)


def sec(a, b):
    i = ACTE.index(a)
    return ACTE[i:ACTE.index(b, i + 1)]


def lignes_tableau(texte, ntok):
    out = {}
    for l in texte.split('\n'):
        t = l.split()
        if len(t) == ntok and re.fullmatch(r'(MG|MP|PP|PG)\d+', t[0]):
            out[t[0]] = t
    return out


print('=== 1. TABLEAUX REFAITS LIGNE A LIGNE')
# nn.3, tableau 1
S3 = sec('nn.3 LE VERDICT', 'nn.4 LE REJEU')
A1 = lignes_tableau(S3, 11)
A2 = lignes_tableau(S3, 10)
print('nn.3 tableau 1 : %d lignes dans l acte (attendues 28) ; tableau 2 : %d lignes (attendues 28)' % (len(A1), len(A2)))
n_ok = 0
for i in IDS:
    c = D[i]
    marge = c['tolerance'] - c['bande'] - abs(c['ln_q'])
    ref = [i, c['w2'], str(c['m']), '%.4f' % c['ln_Gamma_pl'], '%.4f' % c['etalement_du_lecteur'], '%.4f' % c['etendue'], '%.4f' % c['bande'], '%+.5f' % c['ln_q'], '%.2f' % c['tolerance'], '%.4f' % marge, c['jugement']]
    if A1.get(i) == ref:
        n_ok += 1
    else:
        faux('nn.3 tableau 1, %s : acte %s ; refait %s' % (i, A1.get(i), ref))
print('  tableau 1 : %d lignes sur 28 identiques a ce que je refais depuis verdict_vide.json' % n_ok)
n_ok = 0
for i in IDS:
    c = D[i]
    pl = c['lecteur']['plateaux']
    ref = [i] + [str(pl[x]['k0']) for x in 'ABCD'] + ['%.1e' % pl['A']['etalement']] + ['%.1e' % pl[x]['ecart_ln_A'] for x in 'BCD'] + ['%.1e' % c['temoin']['rapport_au_plateau']]
    if A2.get(i) == ref:
        n_ok += 1
    else:
        faux('nn.3 tableau 2, %s : acte %s ; refait %s' % (i, A2.get(i), ref))
print('  tableau 2 : %d lignes sur 28 identiques' % n_ok)
# nn.6, tableau des ordres : refait avec MES predictions
S6 = sec('nn.6 CE QUI ETAIT CONSIGNE', 'nn.7 LES ANNONCES')
A3 = lignes_tableau(S6, 7)
print('nn.6 tableau : %d lignes dans l acte (attendues 28)' % len(A3))
# quelle definition de la loi d echelle ? on teste les deux candidates sur MG3 contre l acte (+0.0106)
c0 = D['MG3']
cand = {'ln|delta| + ln_Phi_etoile - lnGamma': math.log(abs(P['MG3']['delta'])) + P['MG3']['ln_Phi_etoile'] - c0['ln_Gamma_pl'], 'ln_Phi_etoile - lnGamma': P['MG3']['ln_Phi_etoile'] - c0['ln_Gamma_pl']}
print('  loi d echelle a MG3 (acte : +0.0106) : %s' % {k: round(v, 4) for k, v in cand.items()})
LOI = 'ln|delta| + ln_Phi_etoile - lnGamma' if abs(cand['ln|delta| + ln_Phi_etoile - lnGamma'] - 0.0106) < 6e-5 else 'ln_Phi_etoile - lnGamma'
print('  definition retenue pour la loi d echelle : %s' % LOI)
lq = {}
for i in IDS:
    c, p = D[i], P[i]
    lg = c['ln_Gamma_pl']
    loi = (math.log(abs(p['delta'])) if LOI.startswith('ln|delta|') else 0.0) + p['ln_Phi_etoile'] - lg
    lq[i] = {'o3': p['ln_G3'] - lg, 'o2': p['ln_G2'] - lg, 'o1': p['ln_G1'] - lg, 'loi': loi, 'ff': p['ln_forme_fermee'] - lg, 'lgd': lg - math.log(abs(p['delta']))}
n_ok = 0
for i in IDS:
    q = lq[i]
    ref = [i, '%+.5f' % D[i]['ln_q'], '%+.4f' % q['o2'], '%+.4f' % q['o1'], '%+.4f' % q['loi'], '%+.4f' % q['ff'], '%+.4f' % q['lgd']]
    ref[6] = '%.4f' % q['lgd']
    if A3.get(i) == ref:
        n_ok += 1
    else:
        # tolerance d'arrondi : tous les champs numeriques a une unite de la derniere decimale ?
        a = A3.get(i)
        marginal = a is not None and all(abs(float(x) - float(y)) <= (1.1e-4 if k > 1 else 1.1e-5) for k, (x, y) in enumerate(zip(a[1:], ref[1:])))
        if marginal:
            notes.append('nn.6 %s : differe d une unite de la derniere decimale (mes predictions et la table gelee different de 8.6e-9) : acte %s ; refait %s' % (i, a, ref))
            n_ok += 1
        else:
            faux('nn.6 tableau, %s : acte %s ; refait %s' % (i, a, ref))
print('  tableau des ordres : %d lignes sur 28 identiques (ou a une unite de la derniere decimale)' % n_ok)
print()

print('=== 2. PROSE : nn.0, nn.2, nn.5')
lis = [c for c in C if c['ligne'] == 'lisible']
pro = [c for c in C if c['ligne'] == 'profonde']
gam = [math.exp(c['ln_Gamma_pl']) for c in C]
dec = math.log10(max(gam) / min(gam))
print('nn.0 largeurs : de %.1e a %.1e ; %.1f decades (acte : de 2.9e-09 a 9.5e-33 ; 23.5)' % (max(gam), min(gam), dec))
if not (abs(dec - 23.5) < 0.05 and '%.1e' % max(gam) == '2.9e-09' and '%.1e' % min(gam) == '9.5e-33'):
    faux('nn.0 largeurs / decades')
for nom, L, tm, ta in (('lisibles', lis, '0.00068', '0.02'), ('profondes', pro, '0.00134', '0.05')):
    m = max(abs(c['ln_q']) for c in L)
    print('nn.0/nn.5 %s : plus grand |ln q| %.5f (acte %s) ; mediane %.5f' % (nom, m, tm, st.median(abs(c['ln_q']) for c in L)))
    if '%.5f' % m != tm:
        faux('plus grand |ln q| %s' % nom)
mL, mP = st.median(abs(c['ln_q']) for c in lis), st.median(abs(c['ln_q']) for c in pro)
if '%.5f' % mL != '0.00028' or '%.5f' % mP != '0.00048':
    faux('medianes de |ln q| : lisibles %.5f (acte 0.00028), profondes %.5f (acte 0.00048)' % (mL, mP))
for nom, L, att in (('lisibles', lis, ('4.4e-15', '2.9e-09', '0.0101', 'PG6', '0.0024', '0.0093', '0.0013', '0.0070', '0.0002', '0.0023')),
                    ('profondes', pro, ('9.5e-33', '8.3e-18', '0.0398', 'PP8', None, None, None, None, None, None))):
    g = [math.exp(c['ln_Gamma_pl']) for c in L]
    mg = min(L, key=lambda c: c['tolerance'] - c['bande'] - abs(c['ln_q']))
    marg = mg['tolerance'] - mg['bande'] - abs(mg['ln_q'])
    print('nn.5 %s : plateaux de %.1e a %.1e ; plus petite marge %.4f (%s) ; bande de %.4f a %.4f ; etendue de %.4f a %.4f ; s de %.4f a %.4f' % (
        nom, min(g), max(g), marg, mg['id'], min(c['bande'] for c in L), max(c['bande'] for c in L), min(c['etendue'] for c in L), max(c['etendue'] for c in L), min(c['etalement_du_lecteur'] for c in L), max(c['etalement_du_lecteur'] for c in L)))
    print('     acte : plateaux de %s a %s ; marge %s (%s)%s' % (att[0], att[1], att[2], att[3], '' if att[4] is None else ' ; bande %s-%s ; etendue %s-%s ; s %s-%s' % att[4:]))
    ex = ('%.1e' % min(g), '%.1e' % max(g), '%.4f' % marg, mg['id'])
    if ex != att[:4]:
        faux('nn.5 %s : %s contre %s' % (nom, ex, att[:4]))
    if att[4]:
        ex2 = ('%.4f' % min(c['bande'] for c in L), '%.4f' % max(c['bande'] for c in L), '%.4f' % min(c['etendue'] for c in L), '%.4f' % max(c['etendue'] for c in L), '%.4f' % min(c['etalement_du_lecteur'] for c in L), '%.4f' % max(c['etalement_du_lecteur'] for c in L))
        if ex2 != att[4:]:
            faux('nn.5 %s : bandes %s contre %s' % (nom, ex2, att[4:]))
sous_e = sum(1 for c in C if abs(c['ln_q']) < c['etendue'])
sous_b = sum(1 for c in C if abs(c['ln_q']) < c['bande'])
sous_s = sum(1 for c in C if abs(c['ln_q']) < c['etalement_du_lecteur'])
print('nn.5 |ln q| sous l etendue : %d ; sous la bande : %d ; sous s : %d (acte 28, 28, 21)' % (sous_e, sous_b, sous_s))
if (sous_e, sous_b, sous_s) != (28, 28, 21):
    faux('comptes sous etendue / bande / s')
# nn.2 : donnees brutes
n_f = n_fs = n_j = n_js = 0
res = 0.0
itmax = 0
dec_rep = 0
pmin = 1.0
for i in IDS:
    d = json.load(open(os.path.join(RUN, 'sonde_vide_%s.json' % i)))
    for ab in 'ABCD':
        for k, e in d['fantome']['traj'][ab].items():
            n_f += 1
            n_fs += 1 if e['suivi'] else 0
            res = max(res, e['residu'])
            itmax = max(itmax, e['iterations'])
            dec_rep += 1 if e['decalage_repris'] else 0
            pmin = min(pmin, e['poids_site'])
    for ab in 'ABCD':
        for k, e in d['jumeau']['traj'][ab].items():
            n_j += 1
            n_js += 1 if e['suivi'] else 0
npl = sum(1 for c in C for x in 'ABCD' if c['lecteur']['plateaux'][x]['statut'] == 'PLATEAU')
print('nn.2 brut : fantome %d lectures, %d suivies ; jumeau %d, %d suivies ; residu au plus %.1e ; iterations au plus %d ; decalages repris %d ; poids au moins %.6f ; plateaux %d sur 112' % (n_f, n_fs, n_j, n_js, res, itmax, dec_rep, pmin, npl))
if (n_f, n_fs, n_j, n_js, npl, dec_rep, itmax) != (1344, 1344, 1344, 1344, 112, 0, 3) or '%.1e' % res != '6.9e-12' or pmin < 0.999:
    faux('nn.2 comptes bruts')
eA = max(c['lecteur']['plateaux']['A']['etalement'] for c in C)
pe = max(((c['lecteur']['plateaux'][x]['ecart_ln_A'], c['id']) for c in C for x in 'BCD'))
print('nn.2 etalement du plateau sous A au plus %.4f (acte 0.0002) ; plus grand ecart entre absorbeurs %.4f a %s (acte 0.0031, PP8)' % (eA, pe[0], pe[1]))
if '%.4f' % eA != '0.0002' or '%.4f' % pe[0] != '0.0031' or pe[1] != 'PP8':
    faux('nn.2 etalement A / ecart entre absorbeurs')
sp = sorted(c['etalement_du_lecteur'] for c in C)
print('nn.2 s : de %.4f a %.4f, mediane %.4f (acte : 0.0001 a 0.0031, 0.0011)' % (sp[0], sp[-1], st.median(sp)))
plancher = [c['id'] for c in C if math.exp(c['ln_Gamma_pl']) < 1.33e-12]
print('nn.2 plateaux sous 1.33e-12 : %d cellules : %s' % (len(plancher), ' '.join(plancher)))
if len(plancher) != 19 or [i for i in plancher if D[i]['ligne'] == 'lisible'] != ['MG6', 'MP5', 'MP6', 'PP5', 'PP6', 'PG5', 'PG6']:
    faux('nn.2 cellules sous le plancher')
print()

print('=== 3. nn.1 : DUREES ET HEURES (console du pilote)')
con = open(os.path.join(B, r'run_gel_vide_machine2\console_run_1.log'), encoding='utf-8').read()
durs = [int(x) for x in re.findall(r'sonde_vide (?:MG|MP|PP|PG)\d+\s+code=0 duree=(\d+) s', con)]
print('28 cellules : %d durees lues ; de %d a %d s ; appels code=0 : %d ; debut/fin : %s' % (len(durs), min(durs), max(durs), con.count('code=0'), re.findall(r'(\d\d:\d\d:\d\d) PILOTE', con)[:1] + re.findall(r'(\d\d:\d\d:\d\d) FIN DU PILOTE', con)))
if (len(durs), min(durs), max(durs), con.count('code=0')) != (28, 309, 866, 33):
    faux('nn.1 durees')
print()

print('=== 4. nn.4 : LE REJEU DE m1, RECOMPTE PAR MOI (verdict rejoue contre verdict du run)')
def feuilles(x, p=''):
    if isinstance(x, dict):
        for k in sorted(x):
            yield from feuilles(x[k], p + '/' + str(k))
    elif isinstance(x, list):
        for i, e in enumerate(x):
            yield from feuilles(e, p + '[%d]' % i)
    else:
        yield p, x
fa, fb = dict(feuilles(V)), dict(feuilles(VR))
cles = sorted(set(fa) | set(fb))
isnum = lambda v: isinstance(v, (int, float)) and not isinstance(v, bool)
nombres = [k for k in cles if k in fa and k in fb and isnum(fa[k]) and isnum(fb[k])]
discrets = [k for k in cles if k in fa and k in fb and not (isnum(fa[k]) and isnum(fb[k])) and fa[k] != fb[k]]
absents = [k for k in cles if (k in fa) != (k in fb)]
ec = max((abs(fa[k] - fb[k]) / max(abs(fa[k]), 1e-300), k) for k in nombres)
print('champs (feuilles de l arbre JSON) : %d ; dont nombres : %d ; absents d un cote : %d ; champs non numeriques differents : %d ; plus grand ecart relatif d un nombre : %.1e (%s)' % (len(cles), len(nombres), len(absents), len(discrets), ec[0], ec[1]))
print('    acte : 1576 champs dont 816 nombres ; aucun champ discret ; plus grand ecart 1.4e-14 (/cellules/PG16/lecteur/plateaux/D/ecart_ln_A)')
if absents or discrets:
    faux('rejeu : champs absents ou discrets differents : %s %s' % (absents[:3], discrets[:3]))
print()

print('=== 5. nn.6 : ORDRES, SUPERPOSITION, SIGNES')
for nom, L, att in (('lisibles', [i for i in IDS if D[i]['ligne'] == 'lisible'], ('0.0024 PG4', '0.0213 MG6', '0.0297 MG6', '0.0602 MG3', 15, 14, 15)),
                    ('profondes', [i for i in IDS if D[i]['ligne'] == 'profonde'], ('0.0045 PG16', '0.0783 MG16', '0.1015 MG16', '0.1136 MG16', 9, 12, 12))):
    out = []
    for k in ('o2', 'o1', 'loi', 'ff'):
        j = max(L, key=lambda i: abs(lq[i][k]))
        out.append('%.4f %s' % (abs(lq[j][k]), j))
    pl = tuple(sum(1 for i in L if abs(D[i]['ln_q']) < abs(lq[i][k])) for k in ('o2', 'o1', 'loi'))
    print('%s : plus grands ecarts (ordre 2, ordre 1, loi, forme fermee) : %s ; ordre 3 plus pres que ordre 2 / ordre 1 / loi a %s cellules' % (nom, out, pl))
    print('     acte : %s ; plus pres a %s' % (list(att[:4]), att[4:]))
    if out != list(att[:4]) or pl != att[4:]:
        faux('nn.6 ordres %s' % nom)
sup = {}
for m in (3, 4, 5, 6, 8, 12, 16):
    L = [i for i in IDS if D[i]['m'] == m]
    sup[m] = (max(lq[i]['lgd'] for i in L) - min(lq[i]['lgd'] for i in L), max(P[i]['ln_G3'] - math.log(abs(P[i]['delta'])) for i in L) - min(P[i]['ln_G3'] - math.log(abs(P[i]['delta'])) for i in L),
              max(D[i]['ln_q'] for i in L) - min(D[i]['ln_q'] for i in L), max(P[i]['kappa'] for i in L) - min(P[i]['kappa'] for i in L))
print('superposition (etendue sur les 4 creneaux de ln(Gamma/|delta|) ; de ln(G3/|delta|) de ma chaine ; de ln q ; ecart de kappa) :')
for m, v in sup.items():
    print('    m = %-2d : %.4f ; %.4f ; %.4f ; kappa a %.1e' % ((m,) + v))
att_sup = {3: ('0.0098', '0.0097', '0.0003'), 6: ('0.0321', '0.0316', '0.0013'), 8: ('0.0481', '0.0473', '0.0008'), 12: ('0.0855', '0.0858', '0.0003'), 16: ('0.1262', '0.1263', '0.0016')}
for m, a in att_sup.items():
    got = tuple('%.4f' % x for x in sup[m][:3])
    if got != a:
        faux('superposition m = %d : %s contre acte %s' % (m, got, a))
if max(v[3] for v in sup.values()) > 3.5e-6:
    faux('kappa egal a 3e-06 pres : %.1e' % max(v[3] for v in sup.values()))
pos = sum(1 for c in C if c['ln_q'] > 0)
par = {cr: sum(1 for c in C if c['creneau'] == cr and c['ln_q'] > 0) for cr in ('MG', 'MP', 'PP', 'PG')}
dneg = sum(1 for c in C if c['delta'] < 0 and c['ln_q'] > 0)
dpos = sum(1 for c in C if c['delta'] > 0 and c['ln_q'] > 0)
a_sd = sum(1 for c in C if c['ln_q'] * c['delta'] > 0)
a_b = sum(1 for c in C if c['ln_q'] * TB[c['id']]['attente']['sous_correction_mediane'] > 0)
print('signes : ln q > 0 a %d, < 0 a %d ; mediane %+.5f ; par creneau %s ; delta < 0 : %d sur 14 ; delta > 0 : %d sur 14 ; signe de delta a %d ; signe de (b) a %d' % (pos, 28 - pos, st.median(c['ln_q'] for c in C), par, dneg, dpos, a_sd, a_b))
print('     acte : 22, 6 ; +0.00032 ; MG 7, MP 5, PP 5, PG 5 ; 12 ; 10 ; 12 ; 19')
if (pos, par, dneg, dpos, a_sd, a_b) != (22, {'MG': 7, 'MP': 5, 'PP': 5, 'PG': 5}, 12, 10, 12, 19):
    faux('signes')
lis_ids = [i for i in IDS if D[i]['ligne'] == 'lisible']
diff = [i for i in lis_ids if TB[i]['attente']['sous_correction_mediane'] * TB[i]['attente']['signe_de_delta'] < 0]
coin = [i for i in lis_ids if i not in diff]
sb = [i for i in diff if D[i]['ln_q'] * TB[i]['attente']['sous_correction_mediane'] > 0]
sa = [i for i in diff if D[i]['ln_q'] * TB[i]['attente']['signe_de_delta'] > 0]
sc = [i for i in coin if D[i]['ln_q'] * TB[i]['attente']['signe_de_delta'] > 0]
print('lectures qui different : %s ; signe de (b) a %d : %s ; signe de (a) a %d : %s ; coincident : %s ; signe commun a %d : %s' % (len(diff), len(sb), ' '.join(sb), len(sa), ' '.join(sa), ' '.join(coin), len(sc), ' '.join(sc)))
print('     acte : 11 ; (b) a 7 (MG3 MG4 MG5 MG6 MP4 MP5 MP6) ; (a) a 4 (MP3 PP4 PP5 PP6) ; coincident : 5 (PP3 PG3 PG4 PG5 PG6) ; commun a 4')
if (len(diff), sb, sa, len(sc)) != (11, ['MG3', 'MG4', 'MG5', 'MG6', 'MP4', 'MP5', 'MP6'], ['MP3', 'PP4', 'PP5', 'PP6'], 4):
    faux('signes (a) / (b)')
mg = [i for i in lis_ids if i[:2] == 'MG']
print('attente sous (b) a MG (part manquee mediane) : %s ; ln q : %s ; etendue : %s' % (['%.4f' % TB[i]['attente']['sous_correction_mediane'] for i in mg], ['%+.5f' % D[i]['ln_q'] for i in mg], ['%.4f' % D[i]['etendue'] for i in mg]))
print('     acte : de 0.0008 a 0.0022 ; +0.00024 +0.00042 +0.00055 +0.00068 ; 0.0013 0.0014 0.0026 0.0022')
if ['%.4f' % TB[i]['attente']['sous_correction_mediane'] for i in mg][0] != '0.0008' or max(TB[i]['attente']['sous_correction_mediane'] for i in mg) < 0.00215:
    faux('attente sous (b) a MG')
print()

print('=== 6. POUR_MACHINE2 (c) : LA PART DE r3 QUE ln q REPRESENTE (lecture apres coup de m1, hors acte)')
for cr in ('MG', 'MP', 'PP', 'PG'):
    print('    %s : %s' % (cr, '  '.join('%s %+.5f/%+.4f = %.3f' % (i, D[i]['ln_q'], P[i]['r3'], D[i]['ln_q'] / P[i]['r3']) for i in lis_ids if i[:2] == cr)))
print()
print('=== 7. nn.7 : bande lisible et part du lecteur')
mb = max(lis, key=lambda c: c['bande'])
ms = max(lis, key=lambda c: c['etalement_du_lecteur'])
print('plus grande bande lisible %.4f (%s) ; plus grand s lisible %.4f (%s) (acte 0.0093 ; 0.0023)' % (mb['bande'], mb['id'], ms['etalement_du_lecteur'], ms['id']))
if '%.4f' % mb['bande'] != '0.0093' or '%.4f' % ms['etalement_du_lecteur'] != '0.0023':
    faux('nn.7 bande / s lisibles')
print()
print('MORSURES NUMERIQUES :', len(mauv))
for m in mauv:
    print('  -', m)
print('NOTES (a une unite de la derniere decimale) :', len(notes))
for n in notes[:12]:
    print('  -', n)
print()
print('NON VERIFIE PAR CE SCRIPT : les durees de vie, la phrase "la plume etait pessimiste, pour la seconde fois de suite" (jugement de m1 sur lui-meme), les declarations de m1 (ouverture, graine, anteriorite de sa piece de reception, message de 19 h 18),')
print('le contenu de ses scripts de reception et de lecture (je ne les ai pas relus ligne a ligne), les 20 cas de son essai (je n en ai rejoue aucun).')
