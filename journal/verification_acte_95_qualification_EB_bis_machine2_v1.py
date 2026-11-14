# -*- coding: ascii -*-
"""VERIFICATION par machine 2 de l'ACTE 'nn' de la qualification E-B BIS (journal_delta_nn_qualification_EB_bis_v1.md,
canon c396a00095a0b9e3, projet version 1, lot ff93d708547f8ec0), 2026-11-13. Chaque affirmation CHIFFREE de l'acte est
RECALCULEE ici depuis MES sources (sorties de la sonde v3 de la nuit, table de reference, verdicts de la feuille v2,
journal du pilote, mon diagnostic), jamais lue dans le script d'ecriture ni dans le releve de machine 1. Les phrases
attendues sont CONSTRUITES depuis les donnees puis cherchees dans l'acte (blancs normalises) : un nombre tape a la main
et faux est une morsure. Ma regle de plateau est reecrite ici (pas importee de la feuille).
Usage (depuis BOCAL4, jamais -I : numpy en user-site) : python -P verification_acte_nn_qualification_EB_bis_machine2_v1.py
Sorties : verification_acte_nn_qualification_EB_bis_machine2_v1.log et .json. Ce script ne modifie rien."""
import hashlib
import io
import json
import math
import os
import re
import subprocess
import sys
import unicodedata
import zipfile
from fractions import Fraction

sys.dont_write_bytecode = True
ICI = os.path.dirname(os.path.abspath(__file__))
DL = os.path.join(os.path.expanduser('~'), 'Downloads')
REG = os.environ.get('REGISTRE_CLONE', '')
ACTE_NOM = 'journal_delta_nn_qualification_EB_bis_v1.md'
LOT = os.environ.get('LOT_ALT', 'lot_machine1_2026-11-13_acte_qualification_EB_bis_v1_recu.zip')   # LOT_ALT : contre-epreuve sur un acte mute
SUFFIXE = os.environ.get('SUFFIXE_SORTIE', '')
MANIF = 'MANIFEST_lot_machine1_acte_qualification_EB_bis_v1.txt'
LOG = os.path.join(ICI, 'verification_acte_nn_qualification_EB_bis_machine2_v1%s.log' % SUFFIXE)
JSN = os.path.join(ICI, 'verification_acte_nn_qualification_EB_bis_machine2_v1%s.json' % SUFFIXE)
SORTIE = os.path.join(ICI, 'nuit_EB_bis', 'sortie')
FH = open(LOG, 'w', encoding='ascii', newline='\n')
CHK, INFO = [], []


def dire(s=''):
    s = s.encode('ascii', 'replace').decode('ascii')
    print(s, flush=True)
    FH.write(s + '\n')
    FH.flush()


def chk(nom, ok, msg):
    CHK.append({'id': nom, 'ok': bool(ok), 'msg': msg})
    dire('%s %-6s %s' % (nom, 'TIENT' if ok else 'MORD', msg))


def info(msg):
    INFO.append(msg)
    dire('     info   ' + msg)


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


def norm(s):
    return re.sub(r'\s+', ' ', s)


def lit(p):
    return open(os.path.join(ICI, p), 'rb').read()


def nonvide(x):
    return x is not None


# ------------------------------------------------------------------ pieces et lot
zl = zipfile.ZipFile(os.path.join(ICI, LOT))
ACTE = zl.read(ACTE_NOM).decode('utf-8')
ACTE_N = norm(ACTE)
dire('VERIFICATION de l acte %s par machine 2' % ACTE_NOM)
c_act = emp(lit(ACTE_NOM))[0] if os.path.isfile(os.path.join(ICI, ACTE_NOM)) else None
chk('C01', c_act == 'c396a00095a0b9e3' == emp(zl.read(ACTE_NOM))[0] and lit(ACTE_NOM) == zl.read(ACTE_NOM),
    'acte hors zip == membre du zip, canon %s (annonce c396a00095a0b9e3)' % c_act)
man = zl.read(MANIF).decode('utf-8')
bad, n_lignes = [], 0
for ln in man.splitlines():
    m = re.match(r'^([0-9a-f]{16}) ([0-9a-f]{16}) +(\d+) +(\d+)  (\S+)$', ln)
    if not m:
        continue
    n_lignes += 1
    if emp(zl.read(m.group(5))) != (m.group(1), m.group(2), int(m.group(3)), int(m.group(4))):
        bad.append(m.group(5))
canon_lot = emp(man.encode())[0]
dl_man = os.path.join(DL, MANIF)
egal_dl = os.path.isfile(dl_man) and open(dl_man, 'rb').read() == man.encode()
chk('C02', n_lignes == 16 and not bad and len(zl.namelist()) == 17 and canon_lot == 'ff93d708547f8ec0' and egal_dl,
    '%d pieces sur 16 au canon, a l empreinte brute et a la taille ; membres du zip %d (attendu 17) ; ecarts %s ; '
    'CANON DU LOT %s (annonce ff93d708547f8ec0) ; manifeste de Downloads identique : %s' % (
        n_lignes, len(zl.namelist()), bad, canon_lot, egal_dl))

# ------------------------------------------------------------------ index de TOUT ce que je detiens
IDX = {}


def ajoute(h, chemin):
    IDX.setdefault(h, []).append(chemin)


def zip_membres(octets, label, prof):
    try:
        z = zipfile.ZipFile(io.BytesIO(octets))
    except zipfile.BadZipFile:
        return
    for i in z.infolist():
        if i.is_dir() or i.file_size > 30 * 1024 * 1024:
            continue
        try:
            d = z.read(i.filename)
        except (RuntimeError, zipfile.BadZipFile, NotImplementedError):
            continue
        ajoute(emp(d)[0], '%s::%s' % (label, i.filename))
        if i.filename.lower().endswith('.zip') and prof < 3:
            zip_membres(d, '%s::%s' % (label, i.filename), prof + 1)


def parcourt(racine, etiquette, filtre_dl=False):
    for rep, dirs, fics in os.walk(racine):
        dirs[:] = [d for d in dirs if d not in ('__pycache__', 'reprise', '.git')
                   and not d.startswith('T' + chr(233) + 'l' + chr(233) + 'ch')]
        for f in fics:
            if filtre_dl and not re.match(r'^(lot_machine|MANIFEST_lot_machine|POUR_MACHINE|qualification_EB|journal_delta|'
                                          r'note_machine|ERRATUM|files \(\d+\)\.zip)', f):
                continue
            p = os.path.join(rep, f)
            try:
                if os.path.getsize(p) > 30 * 1024 * 1024:
                    continue
                d = open(p, 'rb').read()
            except OSError:
                continue
            rel = etiquette + os.path.relpath(p, racine).replace('\\', '/')
            ajoute(emp(d)[0], rel)
            if f.lower().endswith('.zip'):
                zip_membres(d, rel, 1)
        if filtre_dl:
            break


parcourt(ICI, '')
parcourt(DL, 'Downloads/', True)
if REG and os.path.isdir(REG):
    parcourt(REG, 'registre/')
dire('index : %d fichiers ou membres, %d empreintes distinctes (BOCAL4 recursif, Downloads filtre, registre %s)' % (
    sum(len(v) for v in IDX.values()), len(IDX), 'LU' if REG else 'ABSENT'))
TOK = sorted(set(re.findall(r'(?<![0-9a-f])[0-9a-f]{16}(?![0-9a-f])', ACTE)))
non = [t for t in TOK if t not in IDX]
chk('C03', not non and len(TOK) > 0,
    '%d empreintes distinctes citees dans l acte, resolues chez moi : %d, NON resolues : %s (machine 1 annonce 39 dans '
    'son releve C03 : le nombre est a lire, voir C04)' % (len(TOK), len(TOK) - len(non), non))
for t in TOK:
    ou = IDX.get(t)
    dire('     %s %-9s %s' % (t, 'RESOLUE' if ou else 'ABSENTE', (ou[0] if ou else '-')[:100]))

# noms lies : "nom  canon" de nn.1 (le nom doit etre celui d'un fichier que je detiens sous ce canon)
nn1 = ACTE.split('nn.1 PIECES CITEES')[1].split('nn.2 ')[0]
paires = re.findall(r'(?m)^\s{4}(\S+)\s+([0-9a-f]{16})\s*$', nn1)
mal = []
for nom, c in paires:
    ou = IDX.get(c, [])
    if not any(o.replace('\\', '/').split('::')[-1].split('/')[-1] == nom.split('/')[-1] for o in ou):
        mal.append((nom, c, [o[:60] for o in ou][:2]))
chk('C04', len(paires) == len(set(c for _, c in paires)) == len(TOK) and not mal,
    'nn.1 : %d couples (nom, canon) ; chaque canon resout chez moi vers un fichier de MEME NOM ; couples sans fichier du '
    'meme nom : %s ; empreintes distinctes citees dans tout l acte : %d (releve de machine 1 : 39 : a regarder)' % (
        len(paires), mal, len(TOK)))
chk('C05', all(norm(x) in ACTE_N for x in ('(redaction machine 1, contreseing machine 2, depot operateur, 2026-11-13) '
                                           '-- PROJET, VERSION 1',)) and 'DERNIER ESSAI' in ACTE.split('nn.0')[0],
    'tete : projet version 1, redaction m1 / contreseing m2 / depot operateur, dernier essai dit dans le titre')

# ------------------------------------------------------------------ mes sources de la nuit
S1 = json.load(open(os.path.join(SORTIE, 'sonde_etage1.json'), encoding='ascii'))
S2 = json.load(open(os.path.join(SORTIE, 'sonde_etage2.json'), encoding='ascii'))
V1 = json.load(open(os.path.join(SORTIE, 'verdict_etage1.json'), encoding='ascii'))
VQ = json.load(open(os.path.join(SORTIE, 'verdict_qualification_EB.json'), encoding='ascii'))
REF = json.load(open(os.path.join(ICI, 'tp_reference_machine2_v1.json'), encoding='utf-8'))
TAB = {r['j']: r for r in REF['balayage']}
JOURNAL = open(os.path.join(ICI, 'nuit_EB_bis', 'console_nuit.log'), encoding='ascii').read()
L1 = open(os.path.join(SORTIE, 'lecture_etage1.log'), encoding='ascii', errors='replace').read()
PL = 1e-12
KS = list(range(-5, 13))


def serie_de(traj, t=0):
    out = {}
    for k in KS:
        e = traj[str(k)]['etats'][t]
        g = e.get('gamma') if e.get('suivi') else None
        out[k] = g if (g is not None and g > PL) else None
    return out


def fenetres(ser):
    """toutes les fenetres de cinq valeurs lisibles : (k0, rapport max/min exact, ok)"""
    res = []
    for k0 in range(-5, 9):
        v = [ser.get(k) for k in range(k0, k0 + 5)]
        if any(x is None for x in v):
            continue
        rap = Fraction(max(v)) / Fraction(min(v))
        res.append((k0, rap, rap <= Fraction(21, 20), v))
    return res


def meilleure(ser):
    w = fenetres(ser)
    if not w:
        return None
    k0, rap, ok, v = min(w, key=lambda x: (not x[2], x[1], x[0]))
    return {'ok': ok, 'k0': k0, 'etalement': float(rap) - 1.0, 'Gamma_pl': math.exp(sum(math.log(x) for x in v) / 5.0),
            'ok_k0': [x[0] for x in w if x[2]]}


# ------------------------------------------------------------------ nn.4 : ce qui a ete joue
dire()
dire('--- nn.4 : le run ---')
d1 = int(re.search(r'FIN etage1 code=0 duree=(\d+) s', JOURNAL).group(1))
d2 = int(re.search(r'FIN etage2 code=0 duree=(\d+) s', JOURNAL).group(1))
h = re.findall(r'^2026-11-13 (\d\d:\d\d):\d\d (DEBUT etage1|FIN etage1|FIN etage2)', JOURNAL, re.M)
hh = {b: a for a, b in h}
chk('C06', (hh['DEBUT etage1'], hh['FIN etage1'], hh['FIN etage2']) == ('00:52', '02:08', '08:35') and
    (d1 // 3600, round((d1 % 3600) / 60), d2 // 3600, round((d2 % 3600) / 60)) == (1, 17, 6, 27) and
    all(norm(x) in ACTE_N for x in ('lance a 00h52', 'etage 1 fini a 02h08 (duree 1 h 17), code 0',
                                    'etage 2 fini a 08h35 (duree 6 h 27), code 0',
                                    '7dc2197de3401886 sur BOCAL4 (Windows AMD64, python 3.11.9, numpy 2.2.6)')) and
    'ARRET' not in JOURNAL,
    'journal du pilote relu : %s ; durees %d s et %d s ; les phrases de nn.4 les retrouvent ; aucun ARRET' % (hh, d1, d2))
pf = S2['plateforme']
chk('C07', '%s %s, python %s, numpy %s' % (pf['systeme'], pf['machine'], pf['python'], pf['numpy']) ==
    'Windows AMD64, python 3.11.9, numpy 2.2.6' and 'Machine 2 declare n\'avoir lance aucun calcul pendant le run' in ACTE_N,
    'plateforme de mon JSON == celle de nn.4 ; la declaration que l acte me prete est celle de ma note (section 1)')

# ------------------------------------------------------------------ nn.5 : etage 1
dire()
dire('--- nn.5 : etage 1 au chiffre ---')
GREF = {c: TAB[S1['TP'][c]['j']]['Gamma_ref'] for c in ('j06', 'j08')}
UREF = {c: TAB[S1['TP'][c]['j']]['u_ref'] for c in ('j06', 'j08')}
attendu, pires, tient_tous, fen_ok = [], [], True, True
mini_k4 = []
for cle in ('j06', 'j08'):
    attendu.append('j = %d, g = %.5f, Gamma_ref %.4e, u_ref %.1e' % (S1['TP'][cle]['j'], S1['TP'][cle]['g'], GREF[cle], UREF[cle]))
    for cg in ('G20', 'G30'):
        ser = serie_de(S1['TP'][cle]['traj']['F1' + cg])
        p = meilleure(ser)
        tau_tp = 0.05 + UREF[cle]
        e = abs(math.log(p['Gamma_pl'] / GREF[cle]))
        pires.append(e)
        tient = p['ok'] and e <= tau_tp
        v = V1['detail']['TP'][cle]['F1' + cg]
        tient_tous = tient_tous and tient and v['tient'] and abs(v['etalement'] - p['etalement']) < 1e-12
        attendu.append('%s : PLATEAU, k0 = %d, etalement %.4f, Gamma_pl %.4e, |ln| %.4f contre %.4f : TIENT' % (
            cg, p['k0'], p['etalement'], p['Gamma_pl'], e, tau_tp))
        attendu.append('fenetres a PLATEAU : k0 = %s' % ', '.join(str(x) for x in p['ok_k0']))
        mini_k4 += [float(x[1]) - 1.0 for x in fenetres(ser) if x[0] >= 4]
        fen_ok = fen_ok and not any(x[2] for x in fenetres(ser) if x[0] >= 4)
absents = [a for a in attendu if norm(a) not in ACTE_N]
chk('C08', not absents and tient_tous,
    'table du temoin positif recalculee de MA sortie (plateau exact en rationnels, ma table de reference) : %d phrases '
    'attendues, absentes de l acte : %s ; accord avec mon verdict_etage1.json : %s' % (len(attendu), absents, tient_tous))
chk('C09', fen_ok and '%.1f' % min(mini_k4) in ACTE and norm('Les quatre tiennent ; pire ecart a la reference : |ln| = %.4f' % max(pires)) in ACTE_N,
    'consigne 5.2 : aucune fenetre k0 >= 4 a PLATEAU (%s) ; plus petit etalement d une telle fenetre %.3f (acte : 2.8) ; '
    'pire |ln| %.4f' % (fen_ok, min(mini_k4), max(pires)))
gq5 = [abs(v) for d in S1['GQ5'].values() for v in d.values()]
cp = S1['comptes']
chk('C10', len(gq5) == 30 and '%.3e' % max(gq5) == '1.330e-13' and cp['TP']['joues'] == 72 and cp['plancher']['joues'] == 30 and
    cp['TN'] == {'joues': 3, 'repris': 0, 'sautes': 15} and 'G-Q7 selftest 14 tenus sur 14' in ACTE_N and
    'selftest : 14 tenus sur 14' in L1 and 'temoin positif 72 joues, plancher 30, temoin negatif 3 joues et 15 sautes, soit 120'
    in ACTE_N and 'max |Gamma(H+)| = 1.330e-13 contre 1e-12' in ACTE_N and S1['TN']['candidats'] == [[50, 25], [55, 27], [45, 22]]
    and 'AUCUNE FENETRE ; NON JOUE' in ACTE_N and V1['etage1'] == 'TIENT' and not V1['motifs'],
    'gardes de l etage 1 relus dans mon JSON : G-Q5 %d valeurs max %.3e ; comptes %s ; verdict de l etage 1 %s motifs %s' % (
        len(gq5), max(gq5), cp, V1['etage1'], V1['motifs']))

# ------------------------------------------------------------------ nn.6 : etage 2
dire()
dire('--- nn.6 : etage 2 au chiffre ---')
ORDRE = [('1.95', '39_20'), ('1.97', '197_100'), ('1.98', '99_50'), ('2.02', '101_50'), ('2.03', '203_100'), ('2.05', '41_20')]
CFG = ['F1G20', 'F1G30', 'F2G20', 'F3G20', 'F1GT']
MES = {}
lignes_att, gpl_att, nplat = [], [], {c: 0 for c in CFG}
ecarts_feuille = []
for w, n in ORDRE:
    p = S2['points'][n]
    cells, nech = [], 0
    for c in CFG:
        b = meilleure(serie_de(p['cfg'][c]['traj']))
        MES[(n, c)] = b
        cells.append('%s %.4f %d' % ('PL' if b['ok'] else '--', b['etalement'], b['k0']))
        if b['ok']:
            nplat[c] += 1
        else:
            nech += 1
        vq = VQ['detail']['points'][n]['plateaux'][c]
        ecarts_feuille.append(abs(vq['etalement'] - b['etalement']) + abs(vq['k0'] - b['k0']) +
                              (0 if (vq['statut'] == 'PLATEAU') == b['ok'] else 1))
    lignes_att.append('%s %.3e %s %d' % (w, p['G_run'], ' '.join(cells), nech))
    gp = ['%s %.3e' % (c, MES[(n, c)]['Gamma_pl']) for c in CFG if MES[(n, c)]['ok']]
    if gp:
        gpl_att.append('%s %s' % (w, ' ; '.join(gp)))
    # mon compte d echecs == celui de la feuille
    ecarts_feuille.append(abs(len(VQ['detail']['points'][n]['echecs']) - nech))
absents = [a for a in lignes_att + gpl_att if norm(a) not in ACTE_N]
chk('C11', not absents and max(ecarts_feuille) < 1e-12,
    'les six lignes du tableau de nn.6 (statut, etalement, k0, echecs) et les Gamma_pl recalcules de MES sorties par ma '
    'regle de plateau : %d phrases attendues, absentes : %s ; ecart a ma feuille : %.2e' % (
        len(lignes_att + gpl_att), absents, max(ecarts_feuille)))
phrase_cnt = 'Nombre de PLATEAU sur six points : F1G20 %d, F1G30 %d, F2G20 %d, F3G20 %d, F1GT %d.' % tuple(nplat[c] for c in CFG)
b0 = MES[('39_20', 'F1G20')]
acc30 = abs(math.log(MES[('39_20', 'F1G30')]['Gamma_pl'] / b0['Gamma_pl']))
accgt = abs(math.log(MES[('39_20', 'F1GT')]['Gamma_pl'] / b0['Gamma_pl']))
e6e = abs(math.log(S2['points']['39_20']['G_run'] / b0['Gamma_pl']))
att195 = ['accord G30 / G20 : |ln| = %.4f' % acc30, 'accord GT / G20 : |ln| = %.4f' % accgt,
          'pas de plateau sous F2 (meilleur etalement %.4f) ni sous F3 (%.4f)' % (MES[('39_20', 'F2G20')]['etalement'], MES[('39_20', 'F3G20')]['etalement']),
          '|ln(G_run / Gamma_pl)| = %.4f contre 0.05' % e6e, 'la fenetre retenue part de k0 = %d et contient k = 3' % b0['k0']]
absents = [a for a in [phrase_cnt] + att195 if norm(a) not in ACTE_N]
chk('C12', not absents and 3 in range(b0['k0'], b0['k0'] + 5),
    'denombrement des plateaux et epreuves du point 1.95 recalcules : %d phrases, absentes %s (G30/G20 %.4f, GT/G20 %.4f, '
    '(e) %.4f)' % (1 + len(att195), absents, acc30, accgt, e6e))
cp2 = S2['comptes']
suivis = sum(1 for p in S2['points'].values() for c in p['cfg'].values() for r in c['traj'].values() if r['etats'][0].get('suivi'))
ovmin = min(r['etats'][0]['ov'] for p in S2['points'].values() for c in p['cfg'].values() for r in c['traj'].values()
            if r['etats'][0].get('ov') is not None)
idn = [c['identite'] for p in S2['points'].values() for c in p['cfg'].values()]
gq4 = all(v['au_bit'] for v in S2['GQ4'].values()) and len(S2['GQ4']) == 6
chk('C13', cp2['F1'] == {'joues': 210, 'repris': 6, 'sautes': 0} and cp2['formes']['joues'] == 216 and cp2['translation']['joues'] == 108
    and suivis == 540 and '%.9f' % ovmin == '0.999999539' and len(idn) == 30 and all('%.4f' % x == '1.0000' for x in idn) and gq4 and
    all(norm(x) in ACTE_N for x in ('F1 210 joues et 6 repris', 'formes 216, translation 108, soit 540', 'identite 1.0000 aux trente couples',
                                    '0.999999539', 'Gamma == G_run AU BIT aux six points')),
    'G-Q4 au bit %s ; comptes %s ; etat 0 suivi %d/540 ; plus petit recouvrement %.9f ; identite %d couples, min %.4f' % (
        gq4, cp2, suivis, ovmin, len(idn), min(idn)))
T = VQ['detail']['T_etats']
kap = [x for n in T for x in T[n]['kappa']]
nplt = {n: T[n]['n_plateaux'] for _, n in ORDRE}
chk('C14', abs(VQ['detail']['E_run'] - 3.7027) < 5e-5 and max(abs(T[n]['somme_c_ecart']) for n in T) < 3.5e-13 and
    len(kap) == 60 and '%.7f' % min(kap) == '1.0000000' and '%.5f' % max(kap) == '1.00057' and
    all(T[n]['S_w'] is None for n in T) and
    norm('nombre d\'etats a plateau parmi les dix, par point : 1.95 %d, 1.97 %d, 1.98 %d, 2.02 %d, 2.03 %d, 2.05 %d' % tuple(
        nplt[n] for _, n in ORDRE)) in ACTE_N.replace('1.95 1, 1.97 1', '1.95 1, 1.97 1') and
    'S_w lu a zero point sur six' in ACTE_N and 'a 3e-13 pres de 1 aux six points' in ACTE_N,
    'T-etats recalcules : E_run %.4f, somme des c_nu a %.1e pres, %d kappa de %.7f a %.5f, etats a plateau %s, S_w lus %d sur 6' % (
        VQ['detail']['E_run'], max(abs(T[n]['somme_c_ecart']) for n in T), len(kap), min(kap), max(kap), nplt,
        sum(1 for n in T if T[n]['S_w'] is not None)))
cascade_ok = (VQ['verdict'] == 'NON QUALIFIE' and all(VQ['detail']['points'][n]['statut'] == 'NON QUALIFIE' for _, n in ORDRE) and
              not any(VQ['detail']['points'][n]['non_lisibles'] for _, n in ORDRE))
chk('C15', cascade_ok and 'VERDICT, par la cascade de la section 9 : NON QUALIFIE' in ACTE_N and
    'zero point QUALIFIE sur six, zero NON LISIBLE' in ACTE_N, 'verdict de ma feuille : %s ; six points NON QUALIFIES, aucun NON LISIBLE : %s'
    % (VQ['verdict'], cascade_ok))

# ------------------------------------------------------------------ nn.7 : description des trajectoires (recalculee)
dire()
dire('--- nn.7 : trajectoires, recalculees de ma sonde_etage2.json ---')
R = {}
for w, n in ORDRE:
    for c in CFG:
        s = serie_de(S2['points'][n]['cfg'][c]['traj'])
        for k in KS:
            R[(w, c, k)] = None if s[k] is None else s[k] / S2['points'][n]['G_run']


def extr(cfgs, ks, pts=None):
    vals = [(R[(w, c, k)], w, c, k) for (w, _) in ORDRE if (pts is None or w in pts) for c in cfgs for k in ks if R[(w, c, k)] is not None]
    return min(vals), max(vals)


lo13, hi13 = extr(CFG, range(1, 4))
lo03, hi03 = extr(CFG, range(0, 4))
dire('     (a) k = 1..3 : %.4f (%s %s k=%d) a %.4f (%s %s k=%d) ; k = 0..3 : %.4f a %.4f (%s %s k=%d)' % (
    lo13[0], lo13[1], lo13[2], lo13[3], hi13[0], hi13[1], hi13[2], hi13[3], lo03[0], hi03[0], hi03[1], hi03[2], hi03[3]))
loF, hiF = extr(['F2G20', 'F1GT'], range(-5, 0))[0], extr(['F1G20', 'F3G20'], range(-5, 0))[1]
lo_b, hi_b = extr(CFG, range(-5, 0))
dire('     (b) k = -5..-1 : min %.4f (%s %s k=%d), max %.4f (%s %s k=%d) ; F2/GT min %.4f ; F1/F3 max %.4f' % (
    lo_b[0], lo_b[1], lo_b[2], lo_b[3], hi_b[0], hi_b[1], hi_b[2], hi_b[3], loF[0], hiF[0]))
hi_c = extr(CFG, range(5, 13))[1]
dire('     (c) k >= 5 : plus haut %.4f (%s %s k=%d)' % (hi_c[0], hi_c[1], hi_c[2], hi_c[3]))
dd, dd4 = [], []
for w, n in ORDRE:
    s20 = serie_de(S2['points'][n]['cfg']['F1G20']['traj'])
    s30 = serie_de(S2['points'][n]['cfg']['F1G30']['traj'])
    dd += [(abs(s20[k] / s30[k] - 1.0), abs(s30[k] / s20[k] - 1.0), w, k) for k in range(-5, 3)]
    dd4.append((abs(s20[4] / s30[4] - 1.0), abs(s30[4] / s20[4] - 1.0), w))
mx = max(dd)
dire('     (d) k = -5 a 2 : plus grand |G20/G30 - 1| = %.5f (point %s, k=%d), plus grand |G30/G20 - 1| = %.5f ; k = 4 : |G20/G30 - 1| de %.4f a '
     '%.4f, |G30/G20 - 1| de %.4f a %.4f (le sens du rapport n est pas dit dans l acte)' % (
         mx[0], mx[2], mx[3], max(x[1] for x in dd), min(x[0] for x in dd4), max(x[0] for x in dd4), min(x[1] for x in dd4), max(x[1] for x in dd4)))
k0s = [MES[(n, c)]['k0'] for _, n in ORDRE for c in CFG]
proches = sorted([(MES[(n, c)]['etalement'], w, c) for w, n in ORDRE for c in CFG if not MES[(n, c)]['ok'] and MES[(n, c)]['etalement'] < 0.06])
dire('     (e) k0 de %d a %d ; etalements hors plateau sous 0.06 : %s' % (min(k0s), max(k0s), [(round(a, 4), b, c) for a, b, c in proches]))
nn7 = ACTE.split('nn.7 CE QUE LES TRAJECTOIRES')[1].split('nn.8 ')[0]
nn7n = norm(nn7)
cl = []
cl.append(('(a) k=1..3 bas', '%.2f' % lo13[0], 'entre %.2f et %.2f fois G_run' % (lo13[0], hi13[0]) in nn7n))
cl.append(('(a) k=0..3 haut', '%.2f' % hi03[0], 'entre %.2f et %.2f (le plus haut : %s en %s, k = %d)' % (lo03[0], hi03[0], hi03[1], hi03[2], hi03[3]) in nn7n))
cl.append(('(b) bas', '%.2f' % lo_b[0], 'de %.2f (%s en %s, k = %d) a %.2f (%s en %s, k = %d)' % (
    lo_b[0], lo_b[1], lo_b[2], lo_b[3], hi_b[0], hi_b[1], hi_b[2], hi_b[3]) in nn7n))
cl.append(('(b) F1/F3 monte, F2/GT descend', '%.2f %.2f' % (hiF[0], loF[0]), 'jusqu\'a %.2f fois G_run, F2 et la translation descendent jusqu\'a %.2f' % (hiF[0], loF[0]) in nn7n))
cl.append(('(c) haut', '%.2f' % hi_c[0], 'jusqu\'a %.2f fois G_run (%s en %s, k = %d)' % (hi_c[0], hi_c[1], hi_c[2], hi_c[3]) in nn7n))
cl.append(('(d) 0.0028', '%.4f' % mx[0], 'a %.4f pres de k = -5 a k = 2 aux six points (pire : %s)' % (mx[0], mx[2]) in nn7n))
cl.append(('(d) k=4', '%.3f %.3f' % (min(x[0] for x in dd4), max(x[0] for x in dd4)), 'a k = 4, de %.3f a %.3f' % (min(x[0] for x in dd4), max(x[0] for x in dd4)) in nn7n))
cl.append(('(e) k0', '%d a %d' % (min(k0s), max(k0s)), 'partent de k0 = %d a %d' % (min(k0s), max(k0s)) in nn7n))
cl.append(('(e) proches', str(len(proches)), len(proches) == 4 and all(('%.4f a %s en %s' % (a, b, c)) in nn7n for a, b, c in proches)))
cl.append(('(d) G30 5 plateaux, G20 1', '%d %d' % (nplat['F1G30'], nplat['F1G20']), 'G30 a un plateau a cinq points, G20 a un seul' in nn7n))
mord = [x for x in cl if not x[2]]
chk('C16', not mord, 'nn.7 : %d chiffres recalcules ; ceux que l acte ne porte pas tels que je les recalcule (arrondi de ma valeur entre '
    'parentheses) : %s' % (len(cl), [(a, b) for a, b, _ in mord]))
chk('C17', (hi_c[0] > 4.5) and 'l\'etat reste suivi a ces barreaux, ce n\'est pas un saut de suivi' in nn7n and suivis == 540,
    'nn.7 (c) : etat 0 suivi 540/540, plus petit recouvrement %.9f' % ovmin)

# ------------------------------------------------------------------ nn.8 : annonces
dire()
dire('--- nn.8 : annonces ---')
gel = open(os.path.join(ICI, 'qualification_EB_bis_pre_enregistrement_v1.md'), 'rb').read()
gelt = norm(gel.decode('utf-8'))
attendu_gel = ["A-1 verdict : QUALIFIE PAR POINT 0.50 ; NON QUALIFIE 0.27 ; ESTIMATEUR QUALIFIE 0.13 ; NON CONCLUANT D'INSTRUMENT 0.07 ; NON LISIBLE 0.03",
               "A-2 2.02 n'est pas QUALIFIE : 0.6", "que celle de gauche : 0.5", "FLUCTUATION D'ETAT DOMINANTE : 0.7. NON AVEUGLE",
               "tous les trois de droite : 0.6. NON AVEUGLE" if False else "grand des trois de droite : 0.6. NON AVEUGLE",
               "A-6 le TP tient : 0.93. NON AVEUGLE", "(k0 >= -1) : 0.7.", "a (F1, G20) : 0.55."]
att_act = ["QUALIFIE PAR POINT 0.50, NON QUALIFIE 0.27, ESTIMATEUR QUALIFIE 0.13, NON CONCLUANT D'INSTRUMENT 0.07, NON LISIBLE 0.03",
           'A-2 (0.6)', 'A-3 (0.5)', 'A-4 (0.7, non aveugle)', 'A-5 (0.6, non aveugle)', 'A-6 (0.93, non aveugle, temoin regle)', 'A-7 (0.7)', 'A-8 (0.55)']
gel_ok = emp(gel)[0] == 'dcda1611adf5f8fd' and all(norm(x) in gelt for x in attendu_gel) and all(norm(x) in ACTE_N for x in att_act)
a2 = VQ['detail']['points']['101_50']['statut'] != 'QUALIFIE'
f1 = [n for _, n in ORDRE if MES[(n, 'F1G20')]['ok']]
a7 = all(MES[(n, 'F1G20')]['k0'] >= -1 for n in f1)
a8 = all(VQ['detail']['points'][n]['M17_sur_plateau'] is True for n in f1)
a6 = V1['etage1'] == 'TIENT' and all(V1['detail']['TP'][c][g]['tient'] for c in ('j06', 'j08') for g in ('F1G20', 'F1G30'))
a3_gauche = sum(1 for n in ('39_20', '197_100', '99_50') if VQ['detail']['points'][n]['statut'] == 'QUALIFIE')
a3_droite = sum(1 for n in ('101_50', '203_100', '41_20') if VQ['detail']['points'][n]['statut'] == 'QUALIFIE')
ann = VQ['detail']['annonces']
phr = ['A-3 (0.5), la famille de droite compte au moins autant de QUALIFIES que celle de gauche : vrai, SANS CONTENU -- zero contre zero',
       'A-4 (0.7, non aveugle), fluctuation d\'etat dominante : NON JUGEE', 'A-5 (0.6, non aveugle), kappa de gauche plus grand que kappa de droite : faux',
       'A-6 (0.93, non aveugle, temoin regle), le temoin tient : vrai, aux quatre configurations',
       'A-7 (0.7), a (F1, G20), tout point qui a un PLATEAU a une fenetre qui ne commence pas avant k = -1 : vrai sur UN point (1.95, k0 = %d)' % MES[('39_20', 'F1G20')]['k0'],
       'A-2 (0.6), 2.02 n\'est pas QUALIFIE : vrai']
chk('C18', gel_ok and a2 and a6 and f1 == ['39_20'] and a7 and a8 and a3_gauche == a3_droite == 0 and ann['A-4 (fluctuation d\'etat dominante)'] is None
    and ann['A-5 (kappa gauche > droite)'] is False and all(norm(x) in ACTE_N for x in phr),
    'gel bis %s : probabilites des annonces egales dans le gel et dans l acte ; comptes recalcules : A-2 %s, A-3 %d contre %d, A-4 %s, '
    'A-5 %s, A-6 %s, A-7 %s sur %s, A-8 %s' % (emp(gel)[0], a2, a3_gauche, a3_droite, ann['A-4 (fluctuation d\'etat dominante)'],
                                              ann['A-5 (kappa gauche > droite)'], a6, a7, f1, a8))
chk('C19', 'trois vraies dont deux sur un seul point, et l\'annonce principale manquee' in ACTE_N and a2 and a7 and a8 and
    VQ['verdict'] != 'QUALIFIE PAR POINT',
    'bilan de nn.8 : A-2, A-7, A-8 vraies (A-7 et A-8 sur le seul point 1.95), A-1 : l issue donnee pour la plus probable (QUALIFIE PAR '
    'POINT 0.50) ne s est pas produite, celle qui s est produite etait a 0.27 ; la lecture "annonce principale manquee" est de m1')

# ------------------------------------------------------------------ nn.9 : le rejeu de machine 1 (scelle) contre mes valeurs
dire()
dire('--- nn.9 : rejeu de machine 1 contre mes valeurs ---')
SC = json.loads(zl.read('rejeu_point_39_20_F1G20_machine1.json').decode('utf-8'))
c_sc = emp(zl.read('rejeu_point_39_20_F1G20_machine1.json'))[0]
t2 = S2['points']['39_20']['cfg']['F1G20']['traj']
pire0, pire_abs0, pire_abs, hors = 0.0, 0.0, 0.0, {}
gam_k3 = []
e_re_max = 0.0
n_couples = 0
mem_statut = True
fail_gam = []
for k in KS:
    for t in range(10):
        a, b = SC['traj'][str(k)]['etats'][t], t2[str(k)]['etats'][t]
        n_couples += 1
        mem_statut = mem_statut and (bool(a.get('suivi')) == bool(b.get('suivi')))
        e_re_max = max(e_re_max, abs(a['E_re'] - b['E_re']))
        da = abs(a['gamma'] - b['gamma'])
        pire_abs = max(pire_abs, da)
        rel = a['gamma'] / b['gamma'] - 1.0
        if t == 0:
            pire_abs0 = max(pire_abs0, da)
            if abs(rel) > abs(pire0):
                pire0, k_pire0 = rel, k
        if abs(rel) > 1e-3:
            hors.setdefault(t, []).append((k, b['gamma']))
            fail_gam.append(b['gamma'])
        if k == 3:
            gam_k3.append(b['gamma'])
bar = {t: len(v) for t, v in hors.items()}
rg = {t: (min(g for _, g in v), max(g for _, g in v)) for t, v in hors.items()}
gall = {t: (min(t2[str(k)]['etats'][t]['gamma'] for k in KS), max(t2[str(k)]['etats'][t]['gamma'] for k in KS)) for t in range(1, 10)}
ancr = SC['traj']['3']['etats'][0]['gamma'] / S2['points']['39_20']['G_run'] - 1.0
dire('     scelle %s ; etat 0 : pire ecart relatif %.3e (k=%d), plus grand ecart absolu %.2e ; tous etats : plus grand absolu %.2e ; E_re %.2e ;'
     ' ancrage %.3e' % (c_sc, pire0, k_pire0, pire_abs0, pire_abs, e_re_max, ancr))
dire('     barreaux hors 1e-3 par etat : %s ; Gamma (m2) des barreaux hors : %s ; Gamma (m2) sur les 18 : %s ; k=3 : %.1e a %.1e ; plus grand '
     'Gamma hors tolerance %.2e' % (bar, {t: ('%.0e' % a, '%.0e' % b) for t, (a, b) in rg.items()}, {t: ('%.0e' % a, '%.0e' % b) for t, (a, b) in gall.items() if t in bar},
                                    min(gam_k3), max(gam_k3), max(fail_gam)))
ok_etats = (bar.get(2) == 18 and bar.get(7) == 3 and bar.get(8) == 14 and bar.get(9) == 18 and sorted(bar) == [2, 7, 8, 9])
phr9 = ['ecart relatif 2.239e-04' if False else 'ecart relatif %.3e' % abs(ancr), 'pire ecart relatif a BOCAL4 %.3e (k = %d)' % (abs(pire0), k_pire0),
        'plus grand ecart absolu 1.6e-13' if abs(pire_abs0 - 1.6e-13) < 0.05e-13 else 'plus grand ecart absolu %.1e' % pire_abs0,
        'etat 2, 18 barreaux sur 18', 'etat 7, 3 barreaux sur 18', 'etat 8, 14 barreaux sur 18', 'etat 9, 18 barreaux sur 18',
        'Les energies reelles concordent a 1e-11 pres aux 180 couples', 'vaut 5.2e-13', 'Aucune largeur au-dessus de 1.2e-11 ne sort de la tolerance']
absents = [x for x in phr9 if norm(x) not in ACTE_N]
chk('C20', c_sc == '7fb9026014ad0c93' and n_couples == 180 and mem_statut and ok_etats and e_re_max < 1e-11 and abs(pire0 + 4.948e-4) < 1e-7
    and abs(pire_abs - 5.2e-13) < 0.05e-13 and max(fail_gam) <= 1.2e-11 and not absents,
    'scelle %s lu dans le lot ; 180 couples (etat, barreau) memes statuts de suivi : %s ; etat 0 pire ecart %.3e a k=%d ; barreaux hors 1e-3 : %s ; '
    'plus grand ecart absolu %.2e ; E_re <= %.1e ; plus grand Gamma hors tolerance %.2e ; phrases de nn.9 absentes de l acte : %s' % (
        c_sc, mem_statut, pire0, k_pire0, bar, pire_abs, e_re_max, max(fail_gam), absents))
etats5 = [t for t in range(1, 10) if t not in bar]
chk('C21', len(etats5) == 5 and '5 tiennent a 1e-3 a tous les barreaux et 4 non' in ACTE_N,
    'neuf autres etats : %d tiennent a tous les barreaux (%s), %d non (%s)' % (len(etats5), etats5, len(bar), sorted(bar)))
# plages "ou Gamma va de x a y" (lecture a un chiffre : sur les barreaux hors tolerance, ou sur les 18)
claims = {2: ('1e-13', '1e-11'), 7: ('3e-12', '1e-11'), 8: ('3e-13', '8e-12'), 9: ('2e-15', '3e-13')}
res = []
for t, (a, b) in claims.items():
    for nom, rr in (('hors', rg.get(t)), ('18', gall.get(t))):
        if rr and ('%.0e' % rr[0]).replace('e-0', 'e-') == a and ('%.0e' % rr[1]).replace('e-0', 'e-') == b:
            res.append((t, nom))
            break
    else:
        res.append((t, None))
chk('C22', all(x[1] for x in res), 'plages de Gamma citees pour les etats 2, 7, 8, 9 : retrouvees a un chiffre sur %s' % res)
# la feuille de machine 1 rejouee sur mes sorties
dif, relmax = [], 0.0


def compare(a, b, chemin, acc):
    global relmax
    if isinstance(a, dict) and isinstance(b, dict):
        if sorted(a) != sorted(b):
            acc.append((chemin, 'cles'))
            return
        for k in a:
            compare(a[k], b[k], chemin + '/' + str(k), acc)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            acc.append((chemin, 'longueur'))
            return
        for i, (x, y) in enumerate(zip(a, b)):
            compare(x, y, chemin + '[%d]' % i, acc)
    elif isinstance(a, float) and isinstance(b, float):
        if a != b:
            acc.append((chemin, 'flottant'))
            if a != 0:
                relmax = max(relmax, abs(a - b) / abs(a))
    elif a != b:
        acc.append((chemin, 'valeur'))


d1_, d2_ = [], []
compare(json.loads(zl.read('lecture_m1/verdict_etage1.json').decode()), V1, 'e1', d1_)
compare(json.loads(zl.read('lecture_m1/verdict_qualification_EB.json').decode()), VQ, 'e2', d2_)
flot = [x for x in d1_ + d2_ if x[1] == 'flottant']
autres = [x for x in d1_ + d2_ if x[1] != 'flottant']
log_ok = (emp(zl.read('lecture_m1/lecture_etage1.log'))[0] == emp(open(os.path.join(SORTIE, 'lecture_etage1.log'), 'rb').read())[0] == '85e7939fc556b0e8'
          and emp(zl.read('lecture_m1/lecture_etage2.log'))[0] == emp(open(os.path.join(SORTIE, 'lecture_etage2.log'), 'rb').read())[0] == 'e316a1e8caffd058')
chk('C23', log_ok and not autres and len([x for x in d1_ if x[1] == 'flottant']) == 4 and len([x for x in d2_ if x[1] == 'flottant']) == 23 and
    relmax <= 7.5e-12 and 'sauf 27 flottants (4 a l\'etage 1, 23 a l\'etage 2) qui different d\'au plus 7.5e-12 en relatif' in ACTE_N,
    'feuille rejouee par machine 1 comparee a MES verdicts : journaux au canon %s ; differences hors flottants %s ; flottants differents %d '
    '(etage 1 : %d, etage 2 : %d), ecart relatif max %.2e' % (log_ok, autres, len(flot), len([x for x in d1_ if x[1] == 'flottant']),
                                                                len([x for x in d2_ if x[1] == 'flottant']), relmax))

# ------------------------------------------------------------------ nn.10 : O-BIS-2, mon diagnostic contre ma sonde
dire()
dire('--- nn.10 : O-BIS-2 (mon diagnostic contre ma sonde) ---')
pire_d = (0.0, None)
for geom in ('G20', 'G30'):
    for r in json.load(open(os.path.join(ICI, 'diagnostic_TP_echelle_forte', 'diag_%s.json' % geom), encoding='ascii')):
        cle = 'j06' if r['j'] == 6 else 'j08'
        t = S1['TP'][cle]['traj']['F1' + geom].get(str(r['k']))
        if t is None:
            continue
        rel = r['gamma'] / t['etats'][0]['gamma'] - 1.0
        if abs(rel) > abs(pire_d[0]):
            pire_d = (rel, (cle, geom, r['k']))
chk('C24', abs(abs(pire_d[0]) - 3.6e-3) < 0.05e-3 and pire_d[1] == ('j06', 'G30', -2) and '3.6e-03 au plus (j = 6, G30, k = -2)' in ACTE_N and
    'le run donne 0.0015' in ACTE_N and abs(max(pires) - 0.0015) < 5e-5,
    'diagnostic contre sonde aux barreaux communs : pire ecart %.3e en %s ; le run donne |ln| %.4f' % (pire_d[0], pire_d[1], max(pires)))
chk('C25', S2['hors_manifeste'] == ['pt_39_20_f100.zip'] and 'pt_39_20_f100.zip' in ACTE and 'O-BIS-3 (m2, declare)' in ACTE_N,
    'O-BIS-3 : hors manifeste dans mon JSON : %s' % S2['hors_manifeste'])

# ------------------------------------------------------------------ nn.11 : regles candidates sous (X)
dire()
dire('--- nn.11 : regles candidates sous (X) ---')


def regles_acte(texte):
    m0 = re.search(r'(?m)^nn\.\d+ REGLES CANDIDATES[^\n]*\n', texte)
    corps = texte[m0.end():]
    m1 = re.search(r'(?m)^nn\.\d+ ', corps)
    return sorted(set(int(x) for x in re.findall(r'(?m)^  (\d{1,2})(?:[. ] | \(m[12])', corps[:m1.start()])))


SRC_X = ['DEPOT_delta90/journal_delta_nn_constante_A_v2.md', 'DEPOT_delta91/journal_delta_nn_constante_A_run_v2.md',
         'DEPOT_delta92/journal_delta_nn_constante_A_second_ordre_v1.md', 'm2_rec_acte93_v2/journal_delta_nn_constante_A_mesure_v2.md']
par_piece = [regles_acte(open(os.path.join(ICI, c), encoding='utf-8').read()) for c in SRC_X]
zm = zipfile.ZipFile(os.path.join(ICI, 'lot_machine2_2026-09-29_contreseing_acte_delta93_v1.zip'))
n93 = zm.read('POUR_MACHINE1_contreseing_acte_delta93_machine2_v1.md').decode('utf-8')
sec6 = n93.split('## 6. VERSE SOUS (X)')[1].split('## 7.')[0]
par_piece.append(sorted(int(x) for x in re.findall(r'^  (\d{2})  ', sec6, re.M)))
act94 = None
for rel in IDX.get('569ccbd0d1adb927', []):
    if rel.startswith('registre/') or os.path.basename(rel) == 'journal_delta_nn_qualification_EB_v2.md':
        p = os.path.join(REG, rel[len('registre/'):]) if rel.startswith('registre/') else os.path.join(ICI, rel)
        if os.path.isfile(p):
            act94 = open(p, encoding='utf-8').read()
            break
if act94 is None:
    act94 = open(os.path.join(ICI, 'journal_delta_nn_qualification_EB_v2.md'), encoding='utf-8').read()
par_piece.append(regles_acte(act94))
deja = [x for l in par_piece for x in l]
nn11 = ACTE.split('nn.11 REGLES CANDIDATES')[1].split('nn.12 ')[0]
neufs = sorted(int(x) for x in re.findall(r'(?m)^  (\d{2}) \(m1', nn11))
MOTS = {'une': 1, 'deux': 2, 'trois': 3, 'quatre': 4, 'six': 6, 'huit': 8, 'vingt-cinq': 25, 'vingt-huit': 28}
par = re.search(r'Les ([a-z -]+?) precedentes \(([^)]*)\)', norm(nn11))
vals = [MOTS[t] for t in re.findall(r'\b(huit|quatre|trois|deux|six|une)\b', par.group(2))] if par else []
dit = re.search(r'la revue \(X\), echue : ([a-z -]+?) candidates', ACTE_N)
chk('C26', deja == list(range(1, len(deja) + 1)) and len(deja) == 25 and neufs == [26, 27, 28] and
    [len(l) for l in par_piece] == [8, 4, 3, 3, 3, 4] and par and MOTS.get(par.group(1)) == 25 == sum(vals) and vals == [len(l) for l in par_piece]
    and dit and MOTS.get(dit.group(1)) == 28 and 'trois du contreseing du 93 par machine 2' in ACTE_N,
    'regles relues dans MES copies des actes 90 a 94 et de mon contreseing du 93 : %d regles, par piece %s, de 1 a %d sans trou ; les nouvelles '
    'de l acte portent %s ; la parenthese somme a %d ; "%s candidates" dans nn.12' % (
        len(deja), [len(l) for l in par_piece], max(deja), neufs, sum(vals), dit.group(1) if dit else None))
mes_notes = ['POUR_MACHINE1_certification_gel_EB_bis_machine2_v1.md', 'POUR_MACHINE1_resultat_nuit_EB_bis_machine2_v1.md',
             'POUR_MACHINE1_diagnostic_TP_echelle_forte_machine2_v1.md', 'POUR_MACHINE1_contreseing_acte_qualification_EB_machine2_v2.md']
versent = {}
for f in mes_notes:
    t = open(os.path.join(ICI, f), encoding='utf-8').read()
    versent[f] = len(re.findall(r'(?m)^#+ .*VERSE SOUS \(X\)|^#+ .*R[E\u00c9]GLES? CANDIDATES?', t))
chk('C27', all(v == 0 for v in versent.values()) and 'Ni ton contreseing' not in ACTE,
    'mes quatre notes (certification, resultat, diagnostic, contreseing du 94) : motifs "regle candidate / verse sous (X)" trouves : %s' % versent)
chk('C28', 'quatre du 94' in ACTE_N and len(par_piece[5]) == 4 and sorted(par_piece[5]) == [22, 23, 24, 25],
    'acte 94 (copie du registre, canon 569ccbd0d1adb927) : regles %s' % par_piece[5])

# ------------------------------------------------------------------ nn.12 a nn.14 : citations du gel, canaux, registre
dire()
dire('--- nn.12 a nn.14 : citations du gel, chiffres de nn.13, canal ---')
citations = ['et c\'est le DERNIER ESSAI de la piste (0) sous cette forme', 'ni troisieme gel, ni autre echelle, ni autre temoin',
             'L\'operateur peut lever ce garde-fou ; les machines, non',
             'toute phrase portant un Gamma depuis juillet est reclassee ; reste le fait d\'ordre de grandeur "le fantome fuit, le jumeau non", et seulement si le TP a tenu']
manq = [c for c in citations if norm(c) not in gelt]
dans_acte = [c for c in citations if c.split(';')[0] not in ACTE_N and norm(c) not in ACTE_N]
act94n = norm(act94)
cond94 = all(x in act94n for x in ('cet acte d\'abord', 'une seule difference au gel', 'dernier essai'))
chk('C29', not manq and not dans_acte and cond94 and 'nn.10 (iv)' in ACTE,
    'citations du gel bis (sections 12 et 13) retrouvees dans le gel : manquantes %s ; dans l acte : manquantes %s ; les trois conditions de '
    'm1 au 94, nn.10 (iv), retrouvees dans mon exemplaire de l acte 94 : %s' % (manq, dans_acte, cond94))
g = [S2['points'][n]['G_run'] for _, n in ORDRE]
rap = min(g) / max(gq5)
chk('C30', abs(rap - 493) < 1 and 'au moins 493 fois le plancher du jumeau' in ACTE_N and '%.3e' % min(g) == '6.562e-11' and '%.3e' % max(g) == '2.661e-09'
    and 'de 6.562e-11 a 2.661e-09' in ACTE_N and '%.3e' % max(gq5) == '1.330e-13',
    'rapport du plus petit G_run (%.3e) au plus grand |Gamma(H+)| de G-Q5 (%.3e) : %.1f ; G_run de %.3e a %.3e' % (min(g), max(gq5), rap, min(g), max(g)))


def canon_zip_manif(nom):
    z = zipfile.ZipFile(os.path.join(ICI, nom))
    m = [n for n in z.namelist() if n.startswith('MANIFEST_')][0]
    return emp(z.read(m))[0]


mes_lots = {'762a89e8ad7d498a': 'lot_machine2_2026-11-13_diagnostic_TP_echelle_forte_v1.zip',
            '4de461538a1b694d': 'lot_machine2_2026-11-13_certification_gel_EB_bis_v1.zip',
            'a01598ec24237921': 'lot_machine2_2026-11-13_resultat_nuit_EB_bis_v1.zip',
            '25276846153bacff': 'lot_machine1_2026-11-13_gel_EB_bis_v1_recu.zip'}
bons = {c: canon_zip_manif(z) == c for c, z in mes_lots.items()}
chk('C31', all(bons.values()) and all(c in ACTE for c in bons) and 'fe10bfe' in ACTE, 'canons des quatre lots du canal nn.14 recalcules depuis les '
    'manifestes de mes zips : %s' % bons)
try:
    head = subprocess.run(['git', 'ls-remote', 'https://github.com/lbaaz/SG_1', 'HEAD'], capture_output=True, text=True, timeout=60).stdout.split()[0][:7]
except Exception as e:                      # le reseau peut manquer : on le dit, ce controle est alors declare non joue
    head = 'indisponible (%s)' % type(e).__name__
info('tete du registre public lue par git ls-remote : %s (l acte dit fe10bfe)' % head)
chk('C32', head == 'fe10bfe', 'registre : tete publique %s, l acte dit fe10bfe (nn.14)' % head)
# nn.2 / nn.3 : rappels
chk('C33', all(norm(x) in ACTE_N for x in ('Decomptes geles : 120 decompositions a l\'etage 1, 540 a l\'etage 2', 'k = -5 a 12',
                                              'M17 lit a k = 3', 'lot 762a89e8ad7d498a, non opposable', 'k = -6 a -2')) and
    all(x in gelt for x in ('660, dont 120 a l\'etage 1 et 540 a l\'etage 2', 'eta0 2^(-k)' if False else 'k = -5')),
    'rappels de nn.2 et nn.3 (decomptes 120 et 540, echelle, lecture de M17 a k = 3, diagnostic k = -6 a -2) retrouves ; decomptes dans le gel bis')
chk('C34', all(ord(c) < 128 for c in ACTE) and max(len(x) for x in ACTE.splitlines()) <= 100 and ACTE.rstrip().endswith('-- FIN journal_delta_nn_qualification_EB_bis_v1 --'),
    'acte ASCII, plus longue ligne %d, ligne de FIN' % max(len(x) for x in ACTE.splitlines()))

n_mord = sum(1 for c in CHK if not c['ok'])
dire()
dire('BILAN : %d controles, %d mordent : %s' % (len(CHK), n_mord, [c['id'] for c in CHK if not c['ok']]))
json.dump({'acte': ACTE_NOM, 'canon': c_act, 'bilan': {'chk': len(CHK), 'mord': n_mord, 'noms': [c['id'] for c in CHK if not c['ok']]},
           'controles': CHK, 'info': INFO}, open(JSN, 'w', encoding='ascii'), indent=1, sort_keys=True)
dire('CE QUE CE SCRIPT NE JOUE PAS : aucune decomposition, aucune mesure ; il relit mes JSON et recalcule.')
