# -*- coding: ascii -*-
"""Authentifie une ENVELOPPE de machine 1 (ENVOI + manifeste + zip du lot SANS manifeste) comme le ferait machine 2. Extraction fraiche dans un dossier neuf ; lecture de l'ENVOI ;
canon du manifeste (empreinte B) compare a celui que l'ENVOI annonce ; chaque piece du zip aux deux canons et deux tailles ; rien en trop, rien en moins ; fichiers a plat (gel, notes)
compares aux pieces du lot quand elles y figurent. Usage : py -3.11 -I authentifie_envoi_m1_machine2_v1.py <enveloppe.zip> <dossier neuf> [fichier a plat ...]"""
import hashlib
import os
import re
import sys
import unicodedata
import zipfile

ENV, DST = sys.argv[1], sys.argv[2]; PLATS = sys.argv[3:]
assert not os.path.exists(DST), 'le dossier doit etre neuf'
os.makedirs(DST)


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


morsures = []
with zipfile.ZipFile(ENV) as z:
    noms = z.namelist(); print('enveloppe :', noms); z.extractall(DST)
envoi = [n for n in noms if n.startswith('ENVOI_')][0]; man = [n for n in noms if n.startswith('MANIFEST')][0]; lotzip = [n for n in noms if n.endswith('.zip')][0]
t_envoi = open(os.path.join(DST, envoi), 'rb').read().decode('utf-8')
raw_man = open(os.path.join(DST, man), 'rb').read(); canon = emp(raw_man)[0]
annonces = re.findall(r'CANON\s+([0-9a-f]{16})', t_envoi)
print('CANON du manifeste : %s | canon(s) annonce(s) par l ENVOI : %s' % (canon, annonces))
if canon not in annonces:
    morsures.append('canon du manifeste non annonce par l ENVOI')
att = {}
for l in raw_man.decode('utf-8').split('\n'):
    p = l.split()
    if len(p) == 5 and re.fullmatch(r'[0-9a-f]{16}', p[0]):
        att[p[4]] = (p[0], p[1], int(p[2]), int(p[3]))
m = re.search(r'pieces : (\d+)', raw_man.decode('utf-8')); print('pieces annoncees : %s | lignes de piece : %d' % (m.group(1) if m else '?', len(att)))
if m and int(m.group(1)) != len(att):
    morsures.append('nombre de pieces')
with zipfile.ZipFile(os.path.join(DST, lotzip)) as z:
    contenu = {n: z.read(n) for n in z.namelist() if not n.endswith('/')}
mz = [n for n in contenu if os.path.basename(n).startswith('MANIFEST')]
pieces = {n: b for n, b in contenu.items() if n not in mz}
if mz:
    print('le zip du lot porte aussi un manifeste :', mz, '| identique a celui pose a cote :', all(contenu[n] == raw_man for n in mz))
if sorted(pieces) != sorted(att):
    morsures.append('pieces du zip et du manifeste differentes : %s' % (sorted(set(pieces) ^ set(att)),))
for n in att:
    if n in pieces and emp(pieces[n]) != att[n]:
        morsures.append('piece hors canon : %s' % n)
for p in PLATS:
    raw = open(p, 'rb').read(); b = os.path.basename(p); cand = [n for n in pieces if os.path.basename(n) == b]
    print('fichier a plat %s : %s' % (b, ('= piece du lot %s (octets identiques : %s)' % (cand[0], pieces[cand[0]] == raw)) if cand else 'ABSENT du lot'))
    if cand and pieces[cand[0]] != raw:
        morsures.append('le fichier a plat %s differe de la piece du lot' % b)
cites = set(re.findall(r'(?<![0-9a-f])[0-9a-f]{16}(?![0-9a-f])', t_envoi))
print('canons de 16 hex cites par l ENVOI : %d ; dont presents au manifeste : %d ; autres : %s' % (len(cites), len(cites & {v[0] for v in att.values()} | cites & {canon}), sorted(cites - {v[0] for v in att.values()} - {canon})))
print('MORSURES : %d' % len(morsures))
for x in morsures:
    print('  -', x)
