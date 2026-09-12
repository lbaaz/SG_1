# -*- coding: ascii -*-
# Le moteur depose (m9_replication_v1.py, c8ed357b) joue chercher_seuil et integrer sur quelques cellules ;
# a lancer une fois avec, une fois sans le niveau X86_V4 ; les sorties se comparent au bit.
import importlib.util, hashlib, os, sys, json, numpy as np
chemin = sys.argv[1]; sortie = sys.argv[2]
assert hashlib.sha256(open(chemin, "rb").read()).hexdigest().startswith("c8ed357b120352c4")
spec = importlib.util.spec_from_file_location("m9", chemin); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
_o = sys.stdout; sys.stdout = open(os.devnull, "w")
try: mod.certifier_gel()
finally: sys.stdout.close(); sys.stdout = _o
res = {"variable": os.environ.get("NPY_DISABLE_CPU_FEATURES", ""), "P": int(mod.P), "cellules": {}}
for w2 in (2.00, 1.73):
    for sgn in (1, -1):
        s, msg = mod.chercher_seuil(w2, sgn=sgn)
        grille = np.linspace(0.8 * s, 1.2 * s, 96)
        expl = mod.integrer(w2, grille, sgn=sgn)
        cle = "%d|%.2f|%+d" % (mod.P, w2, sgn)
        res["cellules"][cle] = {"s_etoile": s, "s_hex": float(s).hex(), "message": msg, "masque_96": "".join("1" if b else "0" for b in expl)}
        print(cle, repr(s), msg, res["cellules"][cle]["masque_96"], flush=True)
json.dump(res, open(sortie, "w"), indent=1, sort_keys=True)
