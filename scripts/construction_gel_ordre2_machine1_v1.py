# -*- coding: ascii -*-
# Hors chaine, classe 3, plume machine 1, 2026-11-14. Construit le gel "chaine d'ordre 2" depuis son gabarit : pose les
# canons (convention B) des pieces du lot et les comptes du selftest et du banc, lus dans leurs journaux.
# usage : python3 -I construction_gel_ordre2_machine1_v1.py <gabarit.txt> <dossier du lot> <note.md> <note.json> <gel.md>
import sys, os, re, hashlib, unicodedata
gab, dos, note, note_json, dst = sys.argv[1:6]
def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
t = open(gab, encoding="ascii").read()
def canon(m):
    k = m.group(1)
    if k == "note": return B(note)
    if k == "note_json": return B(note_json)
    return B(os.path.join(dos, k))
t, n = re.subn(r"@@C:([^@]+)@@", canon, t)
st = open(os.path.join(dos, "lecture_selftest_machine1.log"), encoding="ascii").read().strip().split("\n")[-1]
m = re.match(r"SELFTEST : (\d+) cas, (\d+) tenus$", st); assert m and m.group(1) == m.group(2), st
bl = open(os.path.join(dos, "banc_feuille_ordre2_machine1_v1.log"), encoding="ascii").read()
mt = re.search(r"famille T \(la table\) : (\d+) alterations, (\d+) mordues", bl)
mc = re.search(r"famille C \(le code\)  : (\d+) alterations, (\d+) mordues", bl)
for k, v in (("N_SELFTEST", m.group(1)), ("BANC_T", mt.group(1)), ("BANC_T_M", mt.group(2)), ("BANC_C", mc.group(1)), ("BANC_C_M", mc.group(2))):
    t = t.replace("@@" + k + "@@", v)
assert "@@" not in t, t[t.index("@@"):t.index("@@") + 60]
assert all(ord(c) < 128 for c in t) and "%" not in t
longues = [(i + 1, len(l)) for i, l in enumerate(t.split("\n")) if len(l) > 100]
assert not longues, longues
open(dst, "w", encoding="ascii", newline="\n").write(t)
print("gel ecrit : %s  canon %s  %d lignes  %d canons poses" % (dst, B(dst), len(t.split("\n")) - 1, n))
