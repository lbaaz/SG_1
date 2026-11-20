# -*- coding: ascii -*-
"""RELEVE de mon CONTRESEING de l'acte du run du gel "pont" (journal_delta_nn_pont_v1.md, canon e7fb283dd2ee517c) -- machine 2, 2026-11-18. Aucune 2D, aucun appel rejoue.
Methode : chaque nombre de l'acte est LU dans l'acte (expression reguliere) puis REFAIT depuis MES fichiers : mes trois feuilles (ecrites du texte du gel) et les sorties brutes des sondes ; rien n'est repris des feuilles ni du releve de machine 1,
sauf deux lectures dites : le plateau du vide (Q4) et la table de sa chaine, que MES feuilles ne produisent pas (R12, R13).
Usage : py -3.11 -P releve_contreseing_acte_pont_machine2_v1.py <acte.md> <dossier du run> <dossier lot_m1 de l'acte> <racine BOCAL4>
Code de sortie 0 si aucun controle ne mord."""
import hashlib
import json
import math
import os
import re
import statistics
import sys
import unicodedata

ACTE, RUN, LOTA, RAC = [a.rstrip('/\\') for a in sys.argv[1:5]]
MA = RUN + '/feuilles_machine2'
CE = RAC + '/certif_gel_pont_partie2_machine2'
L17A, L17B, L17C = RAC + '/livraison_17a_gel_pont_partie1', RAC + '/livraison_17b_gel_pont_partie2', RAC + '/livraison_17c_rectificatif_gel_pont_partie2'


def canon(ch):
    t = unicodedata.normalize('NFC', open(ch, 'rb').read().decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n')
    return hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]


brut = open(ACTE, 'rb').read()
T = brut.decode('utf-8')
LG = T.split('\n')
TN = ' '.join(T.split())
mord = []
resume = {}


def controle(nom, fautes):
    print('%s : %s' % (nom, 'TIENT' if not fautes else 'MORD -- ' + ' | '.join(str(f)[:110] for f in fautes[:4])))
    resume[nom] = not fautes
    if fautes:
        mord.append(nom.split()[0])


def section(n):
    i = [k for k, l in enumerate(LG) if l.startswith('nn.%d ' % n)][0]
    j = [k for k, l in enumerate(LG) if k > i and (re.match(r'^nn\.\d+ ', l) or l.startswith('-- FIN'))][0]
    return '\n'.join(LG[i:j])


def absents(att, texte=None):
    t = TN if texte is None else ' '.join(texte.split())
    return ['absent de l\'acte : ' + a for a in att if ' '.join(a.split()) not in t]


NOMS = ('MG3', 'MG4', 'MG5', 'PG3', 'PG4', 'PG5')
W2 = {'MG': '397/200', 'PG': '2019/1000'}
V = json.load(open(MA + '/verdict.json'))
VC, VF = V['cellules'], V['familles']
LD = {n: json.load(open('%s/lecture_densite_%s.json' % (MA, n))) for n in NOMS}
X = LD['MG3']['X']
BX = json.load(open(MA + '/lecture_boites.json'))['boites']
par_cell = {n: [b for b in BX if b['cellule_cle'][0] == W2[n[:2]] and b['cellule_cle'][1] == int(n[2])] for n in NOMS}
verd = lambda ok: 'TIENT' if ok else 'TOMBE'
vf = lambda ok: 'TENUE' if ok else 'TOMBEE'
pire = {}
for n in NOMS:
    par = LD[n]['par_x']
    i = max(range(len(par)), key=lambda k: abs(par[k]['ln_R3']))
    pire[n] = (par[i]['ln_R3'], par[i]['x'], par[i]['etendue'])

# R01 forme
f = []
try:
    brut.decode('ascii')
except UnicodeDecodeError:
    f.append('non ASCII')
f += ['ligne trop longue'] * any(len(l) > 100 for l in LG) + ['espace en fin de ligne'] * any(l != l.rstrip() for l in LG) + ['CRLF'] * (b'\r' in brut)
f += ['fin absente'] * (not T.endswith('-- FIN journal_delta_nn_pont_v1 --\n'))
f += ['298 lignes attendues, %d' % (len(LG) - 1)] * (len(LG) - 1 != 298)
controle('R01 forme (ASCII, 298 lignes, sans CRLF, pied)', f)

# R02 la ligne de verdict (depuis MES feuilles)
controle('R02 la ligne de verdict', absents(['VERDICT : (S) %s, (C) %s, (L) %s, (L2) %s.' % (vf(VF['S']['etat'] == 'TENUE'), vf(VF['C']['etat'] == 'TENUE'), vf(VF['L']['etat'] == 'TENUE'), vf(VF['L2']['etat'] == 'TENUE'))]))

# R03 nn.3 : les tables, depuis mes feuilles
s3 = section(3)
f = []
rows1 = re.findall(r'^\s{4}(MG[345]|PG[345])\s+(TIENT|TOMBE)\s+([+-]\d\.\d{4}) a x = (\S+)\s+(\d\.\d\d)\s+(TIENT|TOMBE)$', s3, re.M)
rows2 = re.findall(r'^\s{4}(MG[345]|PG[345])\s+(TIENT|TOMBE)\s+(\d\.\d{4}) \+- (\d\.\d{4})\s+(TIENT|TOMBE)\s+(\d\.\d{3})\s+(\d\.\d{3})\s+(\d\.\d{3})$', s3, re.M)
if len(rows1) != 6 or len(rows2) != 6:
    f.append('lignes de table : %d et %d, 6 et 6 attendues' % (len(rows1), len(rows2)))
for n in NOMS:
    c = VC[n]
    pr, px, _ = pire[n]
    att1 = (n, verd(c['L']['tient']), '%+.4f' % pr, '%g' % px, '%.2f' % (abs(pr) / 0.05), verd(c['L2']['tient']))
    att2 = (n, verd(c['S']['tient']), '%.4f' % c['S']['moyenne'], '%.4f' % c['S']['erreur'], verd(c['C']['tient']), '%.3f' % c['C']['compte_reduit']['UN'], '%.3f' % c['C']['compte_reduit']['DEUX'], '%.3f' % c['C']['rapport'])
    if att1 not in rows1:
        f.append('table (L) %s : attendu %s' % (n, att1))
    if att2 not in rows2:
        f.append('table (S)(C) %s : attendu %s' % (n, att2))
for fam in ('L', 'L2', 'S', 'C'):
    tomb = [n for n in NOMS if not VC[n][fam]['tient']]
    lignes_fam = [l.strip() for l in s3.split('\n') if l.strip().startswith('FAMILLE (%s),' % fam)]
    suffixe = ': %s ; cellules lisibles 6 sur 6%s' % (vf(not tomb), '' if not tomb else ' ; tombees : ' + ' '.join(tomb))
    if len(lignes_fam) != 1 or not lignes_fam[0].endswith(suffixe):
        f.append('ligne de la famille (%s) : lu %s, refait %s' % (fam, lignes_fam, suffixe))
mg_t = {fam: [VC[n][fam]['tient'] for n in NOMS[:3]] for fam in ('L', 'L2', 'S', 'C')}
pg_t = {fam: [VC[n][fam]['tient'] for n in NOMS[3:]] for fam in ('L', 'L2', 'S', 'C')}
if not (not any(mg_t['L']) and not any(mg_t['L2']) and all(mg_t['S']) and all(mg_t['C']) and all(all(v) for v in pg_t.values())):
    f.append('lecture par creneau de mes feuilles differente de celle que l\'acte ecrit')
f += absents(['MG (delta < 0), (L) et (L2) tombent aux trois cellules, (S) et (C) tiennent aux trois ; PG (delta > 0), les quatre familles tiennent aux trois cellules'], s3)
controle('R03 nn.3 : tables de verdict, familles, creneaux (de mes feuilles)', f)

# R04 nn.3 fin : comptes
nn_niv = sum(b['n'] for b in BX)
fia = all(b['fiables'] == b['n'] for b in BX)
etend = max(LD[n]['etendue_absorbeurs_max'] for n in NOMS)
f = []
if not (len(BX) == 120 and all(b['lisible'] for b in BX)):
    f.append('boites lisibles')
if not (fia and nn_niv == 1743):
    f.append('niveaux %d, tous fiables %s' % (nn_niv, fia))
if not all(LD[n]['ecarts_lisibles'] == 12 for n in NOMS):
    f.append('ecarts lisibles')
f += absents(['Tout est lisible : douze ecarts sur douze aux six cellules, plus grande etendue entre absorbeurs %.4f ; 120 boites lisibles sur 120 ; %d niveaux, tous fiables.' % (etend, nn_niv)], s3)
controle('R04 nn.3 : douze ecarts lisibles, 120 boites, %d niveaux fiables, etendue %.4f' % (nn_niv, etend), f)

# R05 nn.5 : ln R3, ln R2 (douze x, six cellules)
s5 = section(5)
rows = re.findall(r'^\s{4}(\d+(?:\.\d+)?)\s+((?:[+-]\d\.\d{4}\s*){6})$', s5, re.M)
f = []
if len(rows) != 24:
    f.append('%d lignes de 6 valeurs, 24 attendues' % len(rows))
for blocs, cle in ((rows[:12], 'ln_R3'), (rows[12:24], 'ln_R2')):
    for i, x in enumerate(X):
        att = ['%+.4f' % LD[n]['par_x'][i][cle] for n in NOMS]
        if i < len(blocs) and (blocs[i][0] != '%g' % x or blocs[i][1].split() != att):
            f.append('%s a x = %g : lu %s, refait %s' % (cle, x, blocs[i][1].split(), att))
controle('R05 nn.5 : les tables ln R3 et ln R2 (24 x 6 nombres, de mes feuilles)', f)

# R06 nn.5 : enonces tires des tables
f = []
hors = {n: [p['x'] for p in LD[n]['par_x'] if abs(p['ln_R3']) > 0.05] for n in NOMS}
txt = []
for n in NOMS[:3]:
    h = hors[n]
    txt.append('%s a x = %s' % (n, ' et '.join('%g' % x for x in h)))
f += absents(['Hors tolerance : ' + ' ; '.join(txt) + '. Partout ailleurs, et a tous les ecarts des trois cellules PG, la tolerance est tenue.'], s5)
if any(hors[n] for n in NOMS[3:]):
    f.append('une cellule PG hors tolerance')
mx4 = max(abs(p['ln_R3']) for n in NOMS[:3] for p in LD[n]['par_x'] if p['x'] <= 4)
if not (0.0135 - 5e-5 <= mx4 < 0.0136):
    f.append('plus grand |ln R3| a x <= 4 aux MG : %.5f' % mx4)
neg = all(LD[n]['par_x'][i]['ln_R3'] < 0 for n in NOMS[:3] for i, x in enumerate(X) if x >= 1)
crois = all(LD[n]['par_x'][i + 1]['ln_R3'] < LD[n]['par_x'][i]['ln_R3'] for n in NOMS[:3] for i, x in enumerate(X[:-1]) if x >= 1)
prof = all(LD['MG3']['par_x'][i]['ln_R3'] > LD['MG4']['par_x'][i]['ln_R3'] > LD['MG5']['par_x'][i]['ln_R3'] for i, x in enumerate(X) if x >= 3)
if not (neg and crois and prof):
    f.append('residu negatif %s, croissant avec l\'ecart %s, avec la profondeur %s' % (neg, crois, prof))
f += absents(['jusqu\'a 4 |delta| il reste sous 0.0136'], s5)
ec8 = LD['MG3']['par_x'][-1]['etendue']
mg3 = abs(pire['MG3'][0])
if not (pire['MG3'][1] == 8 and hors['MG3'] == [8.0] and '%.5f' % mg3 == '0.05024' and '%.4f' % ec8 == '0.0008' and round(ec8 / (mg3 - 0.05)) == 3):
    f.append('MG3 : %.5f, etendue %.5f, rapport %.2f' % (mg3, ec8, ec8 / (mg3 - 0.05)))
f += absents(['MG3 tombe de tres peu : 0.05024 pour 0.05, a un seul ecart', 'l\'etendue entre absorbeurs y vaut 0.0008, soit 3 fois l\'ecart a la tolerance'], s5)
l2mg = all(abs(LD[n]['par_x'][i]['ln_R2']) < abs(LD[n]['par_x'][i]['ln_R3']) for n in NOMS[:3] for i, x in enumerate(X) if x >= 5)
l2pg = all(abs(LD[n]['par_x'][i]['ln_R3']) < abs(LD[n]['par_x'][i]['ln_R2']) for n in NOMS[3:] for i, x in enumerate(X) if x >= 5)
if not (l2mg and l2pg):
    f.append('(L2) : MG %s, PG %s' % (l2mg, l2pg))
controle('R06 nn.5 : les enonces sur les tables (hors tolerance, residu, MG3, (L2))', f)

# R07 nn.5 : (S) et (C) par cellule et par groupe, depuis mes boites et mes feuilles
rows = re.findall(r'^\s{4}(MG[345]|PG[345])\s+(\d\.\d{4}) \+- (\d\.\d{4})\s+(\d\.\d{4})\s+(\d\.\d{4})\s+(\d\.\d{3}) / (\d\.\d{3})\s+(\d+\.\d\d)\s+(\d+\.\d\d)$', s5, re.M)
f = []
if len(rows) != 6:
    f.append('%d lignes, 6 attendues' % len(rows))
gm = []
for n in NOMS:
    c = VC[n]
    sb = [b['S'] for b in par_cell[n] if b['lisible']]
    err = statistics.stdev(sb) / math.sqrt(len(sb))
    if abs(err - c['S']['erreur']) > 1e-12:
        f.append('mon erreur de %s : %.6f contre %.6f de ma feuille' % (n, err, c['S']['erreur']))
    sd = {g: statistics.stdev([b['S'] for b in par_cell[n] if b['lisible'] and b['groupe'] == g]) for g in ('UN', 'DEUX')}
    att = (n, '%.4f' % c['S']['moyenne'], '%.4f' % c['S']['erreur'], '%.4f' % c['S']['par_groupe']['UN'], '%.4f' % c['S']['par_groupe']['DEUX'], '%.3f' % sd['UN'], '%.3f' % sd['DEUX'], '%.2f' % c['C']['n_moyen']['UN'], '%.2f' % c['C']['n_moyen']['DEUX'])
    if att not in rows:
        f.append('ligne %s : attendu %s' % (n, att))
    gm += [c['S']['par_groupe']['UN'], c['S']['par_groupe']['DEUX']]
if not (all(0.85 <= VC[n]['S']['moyenne'] <= 1.15 for n in NOMS) and all(0.80 <= g <= 1.20 for g in gm)):
    f.append('somme hors [0.85, 1.15] ou groupes hors [0.80, 1.20]')
loin = max(gm, key=lambda g: abs(g - 1))
cr = [VC[n]['C']['compte_reduit'][g] for n in NOMS for g in ('UN', 'DEUX')]
rp = [VC[n]['C']['rapport'] for n in NOMS]
f += absents(['la moyenne de groupe la plus loin de 1 vaut %.4f' % loin, 'Le compte reduit vaut de %.3f a %.3f, pour [0.33, 0.55]' % (min(cr), max(cr)), 'le rapport des comptes de %.3f a %.3f, pour [1.25, 1.85]' % (min(rp), max(rp))], s5)
controle('R07 nn.5 : (S) et (C) par cellule et par groupe, ecarts-types refaits de mes boites', f)

# R08 nn.6 : Q1, Q2, Q3, regard apres lecture
s6 = section(6)
sb = [b['S'] for b in BX if b['lisible']]
q1, q1e = statistics.mean(sb), statistics.stdev(sb) / math.sqrt(len(sb))
f = absents(['S = %.4f +- %.4f sur %d boites, soit %+.2f erreur par rapport a 1' % (q1, q1e, len(sb), (q1 - 1) / q1e), '%.3f au groupe UN, %.3f au groupe DEUX (60 boites chacun)' % (V['questions']['Q2_groupe_UN']['rapport'], V['questions']['Q2_groupe_DEUX']['rapport'])], s6)
rows = re.findall(r'^\s{4}(MG[345]|PG[345])\s+(\d\.\d{4})\s+(\d\.\d{4})\s+([+-]\d\.\d{5}) a ([+-]\d\.\d{5})\s+([+-]\d\.\d{5})$', s6, re.M)
if len(rows) != 6:
    f.append('%d lignes (Q3)(Q4), 6 attendues' % len(rows))
q3 = {}
for n in NOMS:
    q3[n] = VC[n]['questions']['Q3_somme_densite_2D']
    att = (n, '%.4f' % q3[n], '%.4f' % VC[n]['S']['moyenne'])
    if not any(r[:3] == att for r in rows):
        f.append('(Q3) %s : attendu %s' % (n, att))
pos = {n: LD[n]['par_x'][-1]['ln_R2'] / (LD[n]['par_x'][-1]['ln_R2'] - LD[n]['par_x'][-1]['ln_R3']) for n in NOMS}
att = ' ; '.join('%s %.2f' % (n, pos[n]) for n in NOMS)
f += absents(['MG3 %.2f ; MG4 %.2f ; MG5 %.2f ; PG3 %.2f ; PG4 %.2f ; PG5 %.2f' % tuple(pos[n] for n in NOMS), 'il va de %.1f a %.1f fois trop loin' % (min(1 / pos[n] for n in NOMS[:3]), max(1 / pos[n] for n in NOMS[:3]))], s6)
mgq3 = [q3[n] for n in NOMS[:3]]
f += absents(['vaut de %.4f a %.4f' % (min(mgq3), max(mgq3))], s6)
controle('R08 nn.6 : (Q1), (Q2), (Q3), le regard apres lecture (refaits de mes boites et de mes feuilles)', f)

# R09 nn.7 : les annonces contre le gel, les issues contre mes feuilles
s7 = section(7)
gel = open(L17B + '/gel_pont_partie2_instrument_enonces_pre_enregistrement_v1.md', encoding='ascii').read()
gp = {m[0]: m[1:] for m in re.findall(r'^\s{4}\((L2?|S|C)\)\s+(\d\.\d\d)\s+(\d\.\d\d)\s+(\d\.\d\d)\s+(\d\.\d\d)\s+(\d\.\d\d)\s+(\d\.\d\d)\s+(\d\.\d\d)$', gel[gel.index('11. LES ANNONCES'):], re.M)}
ap = {m[0]: m[1:] for m in re.findall(r'^\s{4}\((L2?|S|C)\)\s+(\d\.\d\d) (?:TOMBE|tient)\s+(\d\.\d\d) (?:TOMBE|tient)\s+(\d\.\d\d) (?:TOMBE|tient)\s+(\d\.\d\d) (?:TOMBE|tient)\s+(\d\.\d\d) (?:TOMBE|tient)\s+(\d\.\d\d) (?:TOMBE|tient)\s+(\d\.\d\d) (?:TOMBEE|TENUE)$', s7, re.M)}
f = []
if sorted(gp) != ['C', 'L', 'L2', 'S'] or gp != ap:
    f.append('annonces du gel et de l\'acte differentes : gel %s, acte %s' % (gp, ap))
contre = []
for fam in ('L', 'L2', 'S', 'C'):
    for k, n in enumerate(NOMS):
        p = float(gp[fam][k])
        mot = 'tient' if VC[n][fam]['tient'] else 'TOMBE'
        if not re.search(r'^\s{4}\(%s\)\s+(?:\S+\s+){%d}%s %s\b' % (re.escape(fam), 2 * k, gp[fam][k], mot), s7, re.M):
            f.append('mot de %s %s : attendu %s' % (fam, n, mot))
        if (p > 0.5 and not VC[n][fam]['tient']) or (p < 0.5 and VC[n][fam]['tient']):
            contre.append('(%s) %s annoncee a %s' % (fam, n, gp[fam][k]))
    mot = vf(VF[fam]['etat'] == 'TENUE')
    if not re.search(r'^\s{4}\(%s\)\s+.*%s %s$' % (re.escape(fam), gp[fam][6], mot), s7, re.M):
        f.append('mot de la famille %s' % fam)
f += absents(['Sur 24 annonces, %d vont contre le run : %s' % (len(contre), ', '.join(contre))], s7) if len(contre) == 5 else ['nombre d\'annonces contre le run : %d, 5 attendues (%s)' % (len(contre), contre)]
q1ok = 0.99 <= q1 <= 1.05
q2ok = all(0.8 <= V['questions']['Q2_groupe_%s' % g]['rapport'] <= 1.1 for g in ('UN', 'DEUX'))
if not (q1ok and not q2ok):
    f.append('(Q1) tenu %s, (Q2) tenu %s' % (q1ok, q2ok))
f += absents(['(Q1) moyenne dans [0.99, 1.05] : tenu, de peu (%.4f)' % q1, '(Q2) rapport entre 0.8 et 1.1 dans chaque groupe : perdu, de peu (%.3f et %.3f)' % (V['questions']['Q2_groupe_UN']['rapport'], V['questions']['Q2_groupe_DEUX']['rapport'])], s7)
f += absents(['a 8 |delta| il vaut %.4f, %.4f et %.4f en valeur absolue aux trois cellules MG, contre %.4f, %.4f et %.4f aux trois cellules PG' % tuple([abs(LD[n]['par_x'][-1]['ln_R3']) for n in NOMS])], s7)
controle('R09 nn.7 : annonces (contre le gel), issues et paris (contre mes feuilles)', f)

# R10 nn.1 : canons des sept lots, des trois gels, faits du run
s1 = section(1)
MAN = {'7bf7982cceade968': L17B + '/ext/MANIFEST_lot_machine1_gel_pont_partie2_instrument_enonces_v1.txt', '55612644fc4ca279': L17A + '/ext/MANIFEST_lot_machine1_gel_pont_partie1_regle_tirage_v1.txt',
       '5d75dd59784d3811': L17C + '/ext/MANIFEST_lot_machine1_rectificatif_gel_pont_partie2_v1.txt', 'acfecb6da73f20ae': RAC + '/MANIFEST_lot_machine2_certification_gel_pont_partie1_v1.txt',
       '6a83793a2586f4dd': RAC + '/MANIFEST_lot_machine2_tirage_graine_456823_gel_pont_v1.txt', 'a77b27f763fb69cd': RAC + '/MANIFEST_lot_machine2_certification_gel_pont_partie2_v1.txt',
       '9b980dffc71552d5': RAC + '/MANIFEST_lot_machine2_resultats_run_gel_pont_v1.txt'}
f = ['canon du manifeste %s : %s' % (k, canon(p)) for k, p in MAN.items() if canon(p) != k or k not in s1]
GELS = {'735ce41be200c5cd': L17A + '/gel_pont_partie1_regle_tirage_pre_enregistrement_v1_recu.md', '428ac47649de31f3': L17B + '/gel_pont_partie2_instrument_enonces_pre_enregistrement_v1.md',
        '9e25019f3b9bdf04': L17C + '/ext/lot_m1/rectificatif_gel_pont_partie2_avant_run_machine1_v1.md'}
f += ['canon du gel %s : %s' % (k, canon(p)) for k, p in GELS.items() if canon(p) != k or k not in ' '.join(LG[:4])]
ET = json.load(open(RUN + '/etat_run.json'))
jr = open(RUN + '/run_pont_machine2.log', encoding='utf-8').read()
dens = len(re.findall(r'complete \(12 barreaux\)', jr))
bo = len(re.findall(r'toutes les boites sont la', jr))
if not (len(ET) == 48 and all(v['etat'] == 'fait' and v['relances'] == 0 for v in ET.values()) and dens == 24 and bo == 24 and len(BX) == 120):
    f.append('faits du run : %d jobs, %d densites, %d lots de boites' % (len(ET), dens, bo))
m = re.findall(r'\[\s*(\d+) s\] RUN TERMINE', jr)
if m != ['11185'] or '00:11' not in jr.split('\n')[0]:
    f.append('duree ou heure de reception du journal : %s' % m)
f += absents(['11185 s', '48 calculs', 'huit de front', 'Aucun calcul relance ; 24 sorties de densite completes sur 24 ; 120 boites sur 120', 'Machine 2 l\'a recu a 00 h 11 a son horloge'], s1)
controle('R10 nn.1 : canons des sept lots et des trois gels, faits du run (journal, etat)', f)

# R11 nn.12 : les canons des pieces, recalcules depuis mes fichiers
s12 = section(12)
grp, dos, f = None, 0, []
DOSS = {'premiere partie du gel': lambda nom: L17A + '/gel_pont_partie1_regle_tirage_pre_enregistrement_v1_recu.md', 'seconde partie du gel': lambda nom: L17B + '/' + nom,
        'rectificatif d\'avant run': lambda nom: L17C + '/ext/lot_m1/' + nom, 'instrument': lambda nom: L17B + '/ext/lot_m1/' + nom, 'note de machine 2': lambda nom: RAC + '/' + nom,
        'pilote de machine 2': lambda nom: CE + '/' + nom, 'lot de machine 2, run': lambda nom: RUN + '/' + nom, 'lot de machine 2, sa propre feuille': lambda nom: MA + '/' + nom,
        'ce lot, rejeu de machine 1': lambda nom: LOTA + '/' + nom}
for l in LG[LG.index([x for x in LG if x.startswith('nn.12 ')][0]) + 1:]:
    m = re.match(r'^  (\S.*) :$', l)
    if m:
        grp = m.group(1)
        continue
    m = re.match(r'^    ([0-9a-f]{16})  (\S+)$', l)
    if m:
        dos += 1
        if grp not in DOSS:
            f.append('groupe inconnu %r' % grp)
            continue
        p = DOSS[grp](m.group(2))
        if not os.path.isfile(p):
            f.append('fichier absent : %s / %s' % (grp, m.group(2)))
        elif canon(p) != m.group(1):
            f.append('%s : lu %s, recalcule %s' % (m.group(2), m.group(1), canon(p)))
if dos != 29:
    f.append('%d pieces dans nn.12, 29 attendues' % dos)
controle('R11 nn.12 : les %d canons des pieces, recalcules depuis mes fichiers' % dos, f)

# R12 nn.2 et nn.4 : table de la chaine, rejeu contre le run
def feuilles(a, b, p=''):
    if isinstance(a, dict):
        assert sorted(a) == sorted(b), p
        for k in a:
            yield from feuilles(a[k], b[k], p + '/' + k)
    elif isinstance(a, list):
        assert len(a) == len(b), p
        for i, (u, v) in enumerate(zip(a, b)):
            yield from feuilles(u, v, p + '[%d]' % i)
    elif isinstance(a, (bool, str)) or a is None:
        yield (p, 0.0 if a == b else float('inf'), False)
    else:
        yield (p, abs(a - b), True)


f = []
ta, tb = json.load(open(RUN + '/chaine_cellules_pont_v1.json'))['cellules'], json.load(open(L17B + '/ext/lot_m1/chaine_cellules_pont_v1.json'))['cellules']
ct = []
for n in NOMS:        # ses six cellules (sa table porte aussi les points sacrifies) : les memes grandeurs que celles qu'il annonce comparer
    a, b = ta[n], tb[n]
    if (a['w2'], a['m'], a['g'], a['m_bord'], a['r_c']) != (b['w2'], b['m'], b['g'], b['m_bord'], b['r_c']):
        f.append('cellule %s : w2, m, g, m_bord ou r_c different' % n)
    ct += [abs(a['ln_G3'] - b['ln_G3']), abs(a['e_bord'] - b['e_bord'])] + [abs(u - v) for k in ('ln_rho3', 'ln_rho2', 'pas_2_3', 'etendue_rho3') for u, v in zip(a[k], b[k])]
if not ('%.1e' % max(ct) == '1.3e-09' and '%.2e' % max(ct) == '1.26e-09'):
    f.append('table de la chaine, ecart max %.3e' % max(ct))
tot, mx, ou = 0, 0.0, ''
for nom in ['verdict.json', 'lecture_boites.json'] + ['lecture_densite_2d_%s.json' % n for n in NOMS]:
    for p, d, nb in feuilles(json.load(open(RUN + '/' + nom)), json.load(open(LOTA + '/' + nom))):
        if d == float('inf'):
            f.append('champ non numerique different : %s %s' % (nom, p))
        if nb:
            tot += 1
            if d > mx:
                mx, ou = d, nom + p
if tot != 6211 or '%.1e' % mx != '1.4e-11':
    f.append('rejeu contre run : %d nombres, ecart max %.3e (%s)' % (tot, mx, ou))
f += absents(['6211 nombres compares, plus grand ecart 1.4e-11', 'a 1.3e-09 pres'], section(4) + '\n' + section(2))
controle('R12 nn.2 et nn.4 : table de la chaine (%.2e) ; rejeu de m1 contre le run (%d nombres, %.2e a %s)' % (max(ct), tot, mx, ou.split('/')[-1] if ou else ''), f)

# R13 nn.6 (Q4) : arithmetique depuis la table de sa chaine et le plateau du vide de SA feuille (mes feuilles ne le produisent pas)
ch = json.load(open(RUN + '/chaine_cellules_pont_v1.json'))['cellules']
ldm1 = {n: json.load(open('%s/lecture_densite_2d_%s.json' % (RUN, n))) for n in NOMS}
f = []
for n in NOMS:
    q4 = {a: ch[n]['ln_G3'] - math.log(ldm1[n]['vide'][a]['plateau']['val']) for a in 'ABCD'}
    abd = [q4[a] for a in 'ABD']
    if not re.search(r'^\s{4}%s\s+\S+\s+\S+\s+%s a %s\s+%s$' % (n, re.escape('%+.5f' % min(abd)), re.escape('%+.5f' % max(abd)), re.escape('%+.5f' % q4['C'])), s6, re.M):
        f.append('(Q4) %s : refait %+.5f a %+.5f, %+.5f' % (n, min(abd), max(abd), q4['C']))
f += absents(['la chaine d\'ordre 3 rend la largeur 2D a mieux que 0.0004 aux six cellules (hors absorbeur C)'], s6)
controle('R13 nn.6 : (Q4) -- arithmetique seule : ln(G3*) de la table de sa chaine moins ln du plateau du vide de SA feuille', f)

# R14 nn.9 : la tolerance desserree, rejouee depuis ma chaine et mes ln R3
f = []
tombe = []
for n in NOMS:
    ps = ch[n]['pas_2_3']
    for i, p in enumerate(LD[n]['par_x']):
        if abs(p['ln_R3']) > max(0.02, 0.5 * abs(ps[i])):
            tombe.append(n)
            break
if tombe != ['MG3', 'MG4', 'MG5']:
    f.append('avec la tolerance max(0.02, la moitie du pas) : tombent %s' % tombe)
f += absents(['les cellules MG3 MG4 MG5 tombent, les memes. Le desserrement n\'a sauve aucune cellule tombee'], section(9))
controle('R14 nn.9 : l\'ancienne tolerance max(0.02, moitie du pas 2 -> 3), rejouee : tombent %s' % tombe, f)

# R15 nn.10 : les nombres des limites
s10 = section(10)
dq = [q3[n] - VC[n]['S']['moyenne'] for n in NOMS[:3]]
f = absents(['MG3 tombe pour %.5f de trop sur 0.05' % (mg3 - 0.05), 'de 0.0502 a 0.0745 en logarithme a 8 |delta|', 'la somme n\'en bouge que de %.4f a %.4f' % (min(dq), max(dq))], s10)
controle('R15 nn.10 : les nombres des limites', f)

# R16 nn.8 : les deux citations du gel, mot pour mot
s8 = section(8)
gn = ' '.join(gel.split())
cit = re.findall(r'"([^"]+)"', s8)
f = ['pas deux citations : %d' % len(cit)] * (len(cit) != 2)
f += ['citation absente du gel : %s' % c[:60] for c in cit if ' '.join(c.split()) not in gn]
controle('R16 nn.8 : les citations du gel (%d)' % len(cit), f)

print('RELEVE DE MON CONTRESEING : %d controles ; %d morsure(s)%s' % (len(resume), len(mord), (' : ' + ' '.join(mord)) if mord else ''))
json.dump({'controles': resume, 'morsures': mord}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'releve_contreseing_acte_pont_machine2_v1.json'), 'w', encoding='ascii'), indent=1, sort_keys=True)
sys.exit(1 if mord else 0)
