# -*- coding: ascii -*-
"""AUTHENTIFICATION DU LOT DE CERTIFICATION DE MACHINE 2 (gel "largeur du vide", premiere partie) -- machine 1, v1, 2026-11-16.
Lit le manifeste du lot, recalcule l'empreinte B de chaque piece presente et la compare ; dit le canon du lot (empreinte B
du manifeste) ; compte les pieces du dossier que le manifeste ne porte pas. Ne lance aucune piece recue.
Usage : python3 -I -B authentifie_lot_m2_certification_vide_machine1_v1.py <dossier du lot extrait> <nom du manifeste> <canon annonce>"""
import sys, os, re, hashlib, unicodedata
D, MAN, ANNONCE = sys.argv[1:4]
def B(p):
    b = open(p, "rb").read()
    try:
        t = unicodedata.normalize("NFC", b.decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
    except UnicodeDecodeError:
        return hashlib.sha256(b).hexdigest()[:16]
    return hashlib.sha256(t).hexdigest()[:16]
canon = B(os.path.join(D, MAN))
print("manifeste %s : canon du lot %s ; annonce %s : %s" % (MAN, canon, ANNONCE, "IDENTIQUE" if canon == ANNONCE else "DIFFERENT"))
lignes = open(os.path.join(D, MAN), encoding="utf-8").read().split("\n")
portes = {}
for l in lignes:
    m = re.match(r"^\s*([0-9a-f]{16})\s+(?:[0-9a-f]{16}\s+)?(?:\d+\s+)?(?:\d+\s+)?(\S.*\S)\s*$", l)
    if m and os.path.exists(os.path.join(D, m.group(2))):
        portes[m.group(2)] = m.group(1)
presents = []
for d, _, fs in os.walk(D):
    for f in fs:
        presents.append(os.path.relpath(os.path.join(d, f), D).replace(os.sep, "/"))
bons = [p for p in portes if B(os.path.join(D, p)) == portes[p]]; mauvais = [p for p in portes if p not in bons]
hors = sorted(p for p in presents if p not in portes and p != MAN)
print("pieces portees par le manifeste et presentes : %d ; au bon canon : %d ; a un autre canon : %d" % (len(portes), len(bons), len(mauvais)))
for p in mauvais:
    print("  MORSURE %s : manifeste %s, recalcule %s" % (p, portes[p], B(os.path.join(D, p))))
print("fichiers du dossier que le manifeste ne porte pas (lui-meme excepte) : %d %s" % (len(hors), hors))
ok = canon == ANNONCE and not mauvais and not hors
print("AUTHENTIFICATION : %s" % ("TIENT" if ok else "NE TIENT PAS"))
sys.exit(0 if ok else 1)
