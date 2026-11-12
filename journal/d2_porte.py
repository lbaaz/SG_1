# Porte de l'etage 2 SANS calcul : etage2 est remplace par une sentinelle.
import sys, os, json, shutil, hashlib, unicodedata, importlib.util
sys.dont_write_bytecode = True
SONDE, MOTEUR, RUN, MANIF, SRC, D = sys.argv[1:7]
spec = importlib.util.spec_from_file_location("sonde_qeb", SONDE)
S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
def sentinelle(*a, **k): raise RuntimeError("PORTE FRANCHIE")
S.etage2 = sentinelle
shutil.rmtree(D, ignore_errors=True); os.makedirs(D)
shutil.copy(SRC, os.path.join(D, "sonde_etage1.json"))
raw = open(os.path.join(D, "sonde_etage1.json"), "rb").read()
c = hashlib.sha256(unicodedata.normalize("NFC", raw.decode()).replace("\r\n", "\n").encode()).hexdigest()[:16]
print("sonde_etage1.json : prevol = %s" % json.loads(raw)["prevol"])
json.dump({"canon_sonde_etage1": c, "etage1": "TIENT", "prevol": True}, open(os.path.join(D, "v.json"), "w"))
sys.argv = ["sonde", "--moteur", MOTEUR, "--run", RUN, "--manifeste", MANIF, "--sortie", D, "--etage", "2",
            "--verdict1", os.path.join(D, "v.json")]
try:
    S.main()
except RuntimeError as e:
    print(e)
except SystemExit as e:
    print("PORTE FERMEE (SystemExit %s)" % e.code)
