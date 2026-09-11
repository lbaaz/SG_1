#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LES HUIT HUNKS DE LA v2 CONTRE LA v1 -- machine 2, v1, 11/09/2026.

Machine 1 demande (section 3 de sa note) : « la verification des quatre hunks (et des
quatre administratifs) contre la v1, comme au delta 87 ».

Le diff n'est PAS relu : il est REFAIT depuis les deux fichiers. Son diff joint est
ensuite confronte au mien, et surtout APPLIQUE a la v1 -- une piece qui atteste
« rien d'autre ne change » doit reconstruire la v2, sinon elle n'atteste rien.
"""
import difflib, hashlib, itertools, os, re, shutil, subprocess, sys, tempfile, unicodedata

RAC = r"D:\devs\bocal\BOCAL4"
LOT = os.path.join(RAC, "entrant_machine1_2026-09-11_acte_R4R5_v2", "lot")
V1 = os.path.join(LOT, "journal_delta_nn_R4R5_v1.md")
V2 = os.path.join(LOT, "journal_delta_nn_R4R5_v2.md")
SIEN = os.path.join(LOT, "diff_v1_v2_R4R5_machine1_v1.txt")
OK, MORD = [], []


def chk(q, c, d=''):
    OK.append((q, bool(c)))
    if not c:
        MORD.append((q, d))
    print('  [%s] %-56s %s' % ('OK  ' if c else 'MORD', q[:56], d))


def B(p):
    raw = open(p, 'rb').read()
    can = unicodedata.normalize('NFC', raw.decode('utf-8')) \
        .replace('\r\n', '\n').replace('\r', '\n').encode('utf-8')
    return hashlib.sha256(can).hexdigest()[:16]


print("=" * 80)
print("LES HUIT HUNKS DE LA v2 CONTRE LA v1 -- diff REFAIT, non relu")
print("=" * 80)

print("\n[1] LA BASE DU DIFF EST-ELLE LA v1 QUE J'AI CERTIFIEE ?")
chk("v1 jointe au lot v2 == v1 certifiee (86d6ee29d27938ff)",
    B(V1) == "86d6ee29d27938ff", B(V1))
chk("v2 au bit de son manifeste (ce07e533176441a5)",
    B(V2) == "ce07e533176441a5", B(V2))

print("\n[2] LE DIFF, REFAIT PAR MOI")
a = open(V1, encoding='utf-8').read().splitlines(True)
b = open(V2, encoding='utf-8').read().splitlines(True)
mien = [l.rstrip('\n') for l in difflib.unified_diff(a, b, 'v1', 'v2', n=0, lineterm='\n')]
hunks = [l for l in mien if l.startswith('@@')]
plus = [l for l in mien if l.startswith('+') and not l.startswith('+++')]
moins = [l for l in mien if l.startswith('-') and not l.startswith('---')]
chk("8 hunks, comme annonce", len(hunks) == 8, "%d" % len(hunks))
chk("le compte annonce (+27 / -10) est celui du diff reel",
    (len(plus), len(moins)) == (27, 10),
    "diff reel : +%d / -%d" % (len(plus), len(moins)))

print("\n[3] CHAQUE HUNK EST-IL UN DES QUATRE CORRECTIFS, OU ADMINISTRATIF ?")
blocs = []
for k, l in enumerate(mien):
    if l.startswith('@@'):
        bl = []
        for m in mien[k + 1:]:
            if m.startswith('@@'):
                break
            bl.append(m)
        blocs.append((l, bl))
ATT = [("en-tete VERSION 2", lambda s: "PROJET, VERSION 2" in s, "administratif"),
       ("bloc v2 = v1 + correctifs", lambda s: "REMPLACEE, non editee" in s, "administratif"),
       ("H3 borne 1e-5", lambda s: "[H3]" in s and "1e-5 pres" in s, "fond"),
       ("H2 fourchette 4.7", lambda s: "[H2]" in s and "4.7 a 5.7" in s, "fond"),
       ("H1 serie non homogene", lambda s: "[H1]" in s and "PAS homogene" in s, "fond"),
       ("H4 outil de la regle", lambda s: "[H4]" in s and "meme resolution" in s, "fond"),
       ("nn.10 nom de piece", lambda s: "journal_delta_nn_R4R5_v2.md" in s
        and "conservee" in s, "administratif"),
       ("FIN v2", lambda s: "FIN journal_delta_nn_R4R5_v2" in s, "administratif")]
nf = na = 0
for (ent, bl), (nom, test, genre) in zip(blocs, ATT):
    s = "\n".join(bl)
    ok = test(s)
    if ok:
        nf += (genre == "fond"); na += (genre == "administratif")
    chk("hunk %-28s (%s)" % (nom, genre), ok, ent.strip())
chk("4 de fond + 4 administratifs == 8 hunks", nf + na == 8 and nf == 4 and na == 4,
    "%d + %d == %d" % (nf, na, nf + na))
chk("AUCUN hunk hors des huit attendus", len(blocs) == 8)

print("\n[4] SON DIFF JOINT RECONSTRUIT-IL LA v2 ?")
sien = open(SIEN, encoding='utf-8').read().splitlines()
ecarts = [(i, x, y) for i, (x, y) in
          enumerate(itertools.zip_longest(mien, sien, fillvalue=None)) if x != y]
chk("son diff est identique au mien", len(ecarts) == 0,
    "%d ligne(s) different" % len(ecarts))
for i, x, y in ecarts[:6]:
    print("        [%3d] mien %r" % (i, x))
    print("              sien %r" % (y,))
d = tempfile.mkdtemp()
shutil.copy(V1, os.path.join(d, 'v1'))
shutil.copy(SIEN, os.path.join(d, 'p.diff'))
r = subprocess.run(['patch', '-s', '-o', os.path.join(d, 'out'),
                    os.path.join(d, 'v1'), os.path.join(d, 'p.diff')],
                   capture_output=True, text=True)
rec = (r.returncode == 0 and os.path.exists(os.path.join(d, 'out'))
       and B(os.path.join(d, 'out')) == B(V2))
chk("son diff applique a v1 rend la v2 AU BIT", rec,
    "patch rc=%d ; %s" % (r.returncode, (r.stdout or r.stderr).strip()[:90]))
# mon diff, lui, doit reconstruire
shutil.copy(V1, os.path.join(d, 'v1b'))
open(os.path.join(d, 'm.diff'), 'w', encoding='utf-8', newline='\n').write("\n".join(mien) + "\n")
r2 = subprocess.run(['patch', '-s', '-o', os.path.join(d, 'out2'),
                     os.path.join(d, 'v1b'), os.path.join(d, 'm.diff')],
                    capture_output=True, text=True)
chk("MON diff applique a v1 rend la v2 AU BIT",
    r2.returncode == 0 and os.path.exists(os.path.join(d, 'out2'))
    and B(os.path.join(d, 'out2')) == B(V2),
    "patch rc=%d" % r2.returncode)

print("\n[5] LES AFFIRMATIONS DE FORME DE SA NOTE")
raw2 = open(V2, 'rb').read()
chk("v2 : 30523 octets", len(raw2) == 30523, "%d" % len(raw2))
chk("v2 : ASCII pur", all(c < 128 for c in raw2))
chk("v2 : LF seul, aucun CRLF", raw2.count(b'\r') == 0)
chk("v2 : zero signe pour cent", raw2.count(b'%') == 0, "%d" % raw2.count(b'%'))
chk("v2 ne porte plus les trois formulations corrigees",
    all(s not in raw2.decode('utf-8') for s in
        ("a 1e-6 pres", "BAS de 5.4 a 5.7", "-1.071 sur\n       quatre points")))

n = len(MORD)
print("\n" + "=" * 80)
print("controles : %d ; MORDENT : %d" % (len(OK), n))
if n:
    print("\nCE QUI MORD :")
    for q, dd in MORD:
        print("  %s\n      %s" % (q, dd))
print("=" * 80)
