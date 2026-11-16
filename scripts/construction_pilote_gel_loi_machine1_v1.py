# -*- coding: ascii -*-
"""Remplit les canons du pilote depuis les pieces de l'instrument. Usage : python3 -I construction_pilote_gel_loi_machine1_v1.py
<gabarit du pilote> <dossier de l'instrument> <feuille d'ordre 3> <pilote a ecrire>"""
import sys, os, hashlib, unicodedata
GAB, INST, F_O3, SORTIE = sys.argv[1:5]
def canon(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
V = {"table": canon(os.path.join(INST, "table_points_gel_loi_ordre3_v1.json")), "sonde_dense": canon(os.path.join(INST, "sonde_dense_gel_loi_machine1_v1.py")),
     "sonde_lecteur": canon(os.path.join(INST, "sonde_lecteur_gel_loi_machine1_v1.py")), "feuille_lecteur": canon(os.path.join(INST, "lecture_lecteur_gel_loi_machine1_v1.py")),
     "feuille_ordre3": canon(F_O3)}
s = open(GAB, encoding="ascii").read()
for k, v in V.items():
    assert s.count("@@%s@@" % k) == 1, k
    s = s.replace("@@%s@@" % k, v)
assert "@@" not in s
open(SORTIE, "w", encoding="ascii", newline="\n").write(s)
print("pilote ecrit : %s canon %s ; canons portes : %s" % (SORTIE, canon(SORTIE), V))
