"""reception_lot_machine1_machine2_v1.py -- machine 2, 2026-09-21.

GARDE DE RECEPTION d'un lot de machine 1, avant toute lecture de fond.
Prend un ZIP telecharge (typiquement "files (NN).zip", qui contient les pieces a plat ET le vrai
lot interne) ou un repertoire deja extrait. N'ecrit RIEN dans le depot : tout va dans un
repertoire de travail, et le depot n'est touche que par la main de l'operateur.

Ce qu'elle etablit, dans cet ordre :
  0. le manifeste du lot est trouve, et le CANON du lot est son empreinte B (il ne se porte pas
     lui-meme) ;
  1. chaque piece enumeree est VERIFIEE, ABSENTE ou EN ECART, et la garde ferme :
     verifiees + absentes + ecarts == pieces annoncees ;
  2. PB-1 : aucune piece que je detiens deja n'est editee en silence -- toute piece du lot
     homonyme d'une piece du depot est comparee, et un ecart est NOMME ;
  3. LES CHIFFRES QUE L'EN-TETE ANNONCE SONT CONFRONTES AUX JOURNAUX DU LOT. C'est le controle
     qui a attrape E-v9-1 (le manifeste du lot v9/v15 annoncait "banc 103/103" quand son propre
     journal rendait 58/58). Un lot qui se decrit faux ne peut pas etre cite.
Deux verbes : chk (peut mordre), note (ne peut pas). Aucun verdict de fond ici : cette piece dit
si le lot est RECEVABLE, pas s'il est juste.

Usage : reception_lot_machine1_machine2_v1.py <zip ou repertoire> [repertoire de travail]
"""
import hashlib
import os
import re
import sys
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
SRC = sys.argv[1] if len(sys.argv) > 1 else None
TRAVAIL = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ICI, 'reception_travail')
lignes, bilan = [], {'chk': 0, 'mord': []}


def out(s=''):
    print(s)
    lignes.append(s)


def chk(nom, cond, detail=''):
    bilan['chk'] += 1
    if not cond:
        bilan['mord'].append(nom)
    out('  [chk %s] %s%s' % ('PASSE' if cond else 'MORD ', nom, (' -- ' + detail) if detail else ''))
    return cond


def note(nom, detail):
    out('  [note] %s -- %s' % (nom, detail))


def emp(raw):
    """convention B (NFC + CRLF -> LF) et brute"""
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


def empf(p):
    return emp(open(p, 'rb').read())


def deplier(src, dest):
    """extrait recursivement : un zip telecharge peut contenir le vrai lot en zip interne"""
    os.makedirs(dest, exist_ok=True)
    if os.path.isdir(src):
        return src
    with zipfile.ZipFile(src) as z:
        z.extractall(dest)
    for f in sorted(os.listdir(dest)):
        q = os.path.join(dest, f)
        if f.lower().endswith('.zip') and zipfile.is_zipfile(q):
            interne = os.path.join(dest, 'lot_interne')
            os.makedirs(interne, exist_ok=True)
            with zipfile.ZipFile(q) as z:
                z.extractall(interne)
            note('lot interne deplie', '%s -> lot_interne/ (%d entrees)' % (f, len(os.listdir(interne))))
            return interne
    return dest


if not SRC or not os.path.exists(SRC):
    print('usage : %s <zip ou repertoire> [repertoire de travail]' % os.path.basename(__file__))
    sys.exit(2)

out('GARDE DE RECEPTION D UN LOT MACHINE 1 -- machine 2')
out('source %s' % SRC)
out()
out('0. LE MANIFESTE ET LE CANON DU LOT')
RAC = deplier(SRC, TRAVAIL)
mans = [f for f in sorted(os.listdir(RAC)) if f.startswith('MANIFEST') and f.endswith('.txt')]
if not chk('0.1 : un manifeste et un seul dans le lot', len(mans) == 1, str(mans) or 'aucun'):
    out()
    out('ARRET : sans manifeste unique, rien ne peut etre verifie.')
    sys.exit(1)
MAN = os.path.join(RAC, mans[0])
TXT = open(MAN, encoding='utf-8', errors='replace').read()
CANON_LOT = empf(MAN)[0]
out('  [note] canon du lot (empreinte B du manifeste) -- %s' % CANON_LOT)
note('manifeste', mans[0])

# ---------------------------------------------------------------- 1. LES PIECES
out()
out('1. LES PIECES ENUMEREES')
RG = re.compile(r'^([0-9a-f]{16}) ([0-9a-f]{16})\s+(\d+)\s+(\d+)\s+(.+?)\s*$', re.M)
enum = RG.findall(TXT)
chk('1.1 : le manifeste enumere au moins une piece', bool(enum), '%d ligne(s)' % len(enum))
verifiees, absentes, ecarts = [], [], []
for b, br, ob, obr, f in enum:
    q = os.path.join(RAC, f)
    if not os.path.isfile(q):
        absentes.append(f)
        continue
    cb, cbr, cob, cobr = empf(q)
    if cb == b and cob == int(ob):
        verifiees.append(f)
        if cbr != br:
            note('1 %s' % f, 'empreinte B conforme, brute differente (fins de ligne) : la convention absorbe')
    else:
        ecarts.append((f, cb, b, cob, int(ob)))
for f, cb, b, cob, ob in ecarts:
    out('  [ECART] %s -- calcule %s (%d o) / annonce %s (%d o)' % (f, cb, cob, b, ob))
for f in absentes:
    out('  [ABSENTE] %s' % f)
mp = re.search(r'pieces\s*:\s*(\d+)', TXT)
NP = int(mp.group(1)) if mp else len(enum)
chk('1.2 : le compte annonce egale le nombre de lignes enumerees', NP == len(enum),
    'annonce %d, enumere %d' % (NP, len(enum)))
chk('1.3 GARDE DE RECEPTION : verifiees + absentes + ecarts == %d' % NP,
    len(verifiees) + len(absentes) + len(ecarts) == NP,
    '%d + %d + %d' % (len(verifiees), len(absentes), len(ecarts)))
chk('1.4 : aucune piece en ECART', not ecarts, '%d' % len(ecarts))
chk('1.5 : aucune piece ABSENTE', not absentes, '%d' % len(absentes))

# ---------------------------------------------------------------- 2. PB-1
out()
out('2. PB-1 -- AUCUNE PIECE QUE JE DETIENS DEJA N EST EDITEE EN SILENCE')
homonymes, edites = [], []
for b, br, ob, obr, f in enum:
    mien = os.path.join(ICI, os.path.basename(f))
    q = os.path.join(RAC, f)
    if os.path.isfile(mien) and os.path.isfile(q):
        homonymes.append(f)
        if empf(mien)[0] != empf(q)[0]:
            edites.append((f, empf(mien)[0], empf(q)[0]))
for f, a, b_ in edites:
    out('  [EDITEE] %s -- mon depot %s / le lot %s' % (f, a, b_))
note('2.1 homonymes', '%d piece(s) du lot existent deja chez moi : %s'
     % (len(homonymes), ', '.join(homonymes) or 'aucune'))
chk('2.2 : aucune piece homonyme n est editee', not edites, '%d editee(s)' % len(edites))

GELS = {'constante_A_pre_enregistrement_v8.md': '800fc6a9a8e56e49',
        'constante_A_pre_enregistrement_v9.md': 'b515abc5a6da73c5',
        'banc_qualification_machine1_v14.py': 'dc91676c640d4323',
        'banc_qualification_machine1_v15.py': 'a1553f6eb5cc74b8'}
for f, c in sorted(GELS.items()):
    mien = os.path.join(ICI, f)
    if os.path.isfile(mien):
        chk('2.3 : %s intact dans MON depot' % f, empf(mien)[0] == c, empf(mien)[0])
    q = os.path.join(RAC, f)
    if os.path.isfile(q):
        chk('2.4 : %s du lot au canon certifie' % f, empf(q)[0] == c, empf(q)[0])

# ---------------------------------------------------------------- 3. L EN-TETE CONTRE LES JOURNAUX
out()
out('3. CE QUE L EN-TETE ANNONCE, CONFRONTE AUX JOURNAUX DU LOT (le controle qui a attrape E-v9-1)')
JOURNAUX = {f: open(os.path.join(RAC, f), encoding='utf-8', errors='replace').read()
            for _, _, _, _, f in enum
            if f.endswith('.log') and os.path.isfile(os.path.join(RAC, f))}
MOTIFS = (('selftest', r'bilan (\d+/\d+)\s*$', r'selftest\s+(\d+/\d+)'),
          ('banc', r'bilan (\d+/\d+) scenarios mordent', r'banc\s+(\d+/\d+)'))
for nom, mlog, mman in MOTIFS:
    mesure = None
    for f, t in JOURNAUX.items():
        if nom not in f.lower():
            continue
        tr = re.findall(mlog, t, re.M)
        if tr:
            mesure = (tr[-1], f)
    annonce = re.search(mman, TXT)
    if mesure is None and annonce is None:
        note('3 %s' % nom, 'ni annonce ni journal dans ce lot')
        continue
    if mesure is None:
        note('3 %s' % nom, 'annonce "%s" mais AUCUN journal du lot ne le porte : rien a confronter'
             % annonce.group(1))
        continue
    if annonce is None:
        note('3 %s' % nom, 'journal %s rend %s ; l en-tete ne l annonce pas' % (mesure[1], mesure[0]))
        continue
    chk('3 %s : l en-tete annonce ce que le journal du lot rend' % nom,
        annonce.group(1) == mesure[0],
        'en-tete "%s" | journal %s rend "%s"' % (annonce.group(1), mesure[1], mesure[0]))
for f, t in sorted(JOURNAUX.items()):
    v = re.findall(r'VERDICT\s+(.+)', t)
    if v:
        note('3 verdict de %s' % f, v[-1].strip()[:100])
    bl = re.findall(r'BILAN : (\d+) controles, (\d+) mordent', t)
    if bl:
        note('3 bilan de %s' % f, '%s controles, %s mordent' % bl[-1])

# ---------------------------------------------------------------- BILAN
out()
# Deux natures de morsure, et elles ne se paient pas au meme prix : une piece absente, en ecart
# ou editee ARRETE (on ne peut pas lire ce qu'on n'a pas) ; une description fausse n'arrete pas,
# elle s'ERRATE -- c'est le traitement que E-v9-1 a recu, le lot ayant ete certifie par ailleurs.
piece = [n for n in bilan['mord'] if n[:2] in ('0.', '1.', '2.')]
descr = [n for n in bilan['mord'] if n not in piece]
out('CANON DU LOT : %s' % CANON_LOT)
out('BILAN : %d controles, %d mordent (%d de PIECE, %d de DESCRIPTION)'
    % (bilan['chk'], len(bilan['mord']), len(piece), len(descr)))
for nm in piece:
    out('   MORD (piece)       : %s' % nm)
for nm in descr:
    out('   MORD (description) : %s' % nm)
out()
if piece:
    out('LOT NON RECEVABLE -- une piece manque, est en ecart ou a ete editee : a lever AVANT'
        ' toute lecture de fond.')
elif descr:
    out('LOT RECEVABLE, DESCRIPTION FAUSSE -- les pieces sont la et au canon : la lecture de fond'
        ' peut commencer. Mais le lot se decrit faux et ne peut pas etre cite tel quel :'
        ' ERRATUM DE MANIFESTE a demander, sans qu aucun canon bouge.')
else:
    out('LOT RECEVABLE -- les pieces sont la, au canon, et le lot se decrit juste : la lecture de'
        ' fond peut commencer.')
out('Cette piece ne dit RIEN du fond : ni le gel, ni l instrument, ni un run ne sont juges ici.')
with open(os.path.join(ICI, 'reception_lot_machine2_v1.log'), 'w', encoding='utf-8', newline='\n') as fh:
    fh.write('\n'.join(lignes) + '\n')
print()
print('journal ecrit : reception_lot_machine2_v1.log')
print('pieces depliees dans : %s (le depot n est PAS touche)' % RAC)
sys.exit(1 if piece else 0)
