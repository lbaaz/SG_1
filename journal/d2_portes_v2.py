# Portes de l'etage 2 SANS calcul : etage2 est remplace par une sentinelle. Sept cas.
import sys, os, json, shutil, hashlib, unicodedata, importlib.util
sys.dont_write_bytecode = True
SONDE, MOTEUR, RUN, MANIF, SRC, BASE = sys.argv[1:7]
def canon(raw):
    return hashlib.sha256(unicodedata.normalize("NFC", raw.decode()).replace("\r\n", "\n").encode()).hexdigest()[:16]
# (nom, commande pre-vol, verdict pre-vol, sonde_etage1 pre-vol, mutation etage 1, factice, sonde_etage1 absent, attendu)
CAS = [("1 reel / verdict pre-vol / etage1 pre-vol (D-2 d'origine)", False, True, True, None, False, False, "FERMEE"),
       ("2 reel / verdict reel / etage1 pre-vol (croise)", False, False, True, None, False, False, "FERMEE"),
       ("3 pre-vol / verdict reel / etage1 reel (inverse)", True, False, False, None, False, False, "FERMEE"),
       ("4 TOUT REEL (le chemin legitime de la nuit)", False, False, False, None, False, False, "OUVERTE"),
       ("5 TOUT PRE-VOL, verdict factice (le chemin legitime du pre-vol)", True, True, True, None, True, False, "OUVERTE"),
       ("6 etage 1 MUTE (M-4) sous verdict pre-vol", True, True, True, "M-4", True, False, "FERMEE"),
       ("7 sonde_etage1.json ABSENT", True, True, True, None, True, True, "FERMEE")]
for i, (nom, cmd_pv, v_pv, s_pv, mut, fact, absent, attendu) in enumerate(CAS):
    d = os.path.join(BASE, "porte_%d" % (i + 1)); shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    spec = importlib.util.spec_from_file_location("sonde_qeb_%d" % i, SONDE)
    S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
    def sentinelle(*a, **k): raise RuntimeError("OUVERTE")
    S.etage2 = sentinelle
    j = json.load(open(SRC)); j["prevol"] = s_pv; j["mutation"] = mut
    if not absent:
        json.dump(j, open(os.path.join(d, "sonde_etage1.json"), "w"), indent=1, sort_keys=True)
    c = canon(open(os.path.join(d, "sonde_etage1.json"), "rb").read()) if not absent else "0" * 16
    v = {"canon_sonde_etage1": c, "etage1": "TIENT", "prevol": v_pv}
    if fact: v["factice"] = True
    json.dump(v, open(os.path.join(d, "v.json"), "w"))
    argv = ["sonde", "--moteur", MOTEUR, "--run", RUN, "--manifeste", MANIF, "--sortie", d, "--etage", "2",
            "--verdict1", os.path.join(d, "v.json")] + (["--prevol"] if cmd_pv else [])
    sys.argv = argv
    out = None
    try:
        S.main()
        out = "TERMINEE SANS SENTINELLE"
    except RuntimeError as e:
        out = str(e)
    except SystemExit as e:
        out = "FERMEE"
    except Exception as e:
        out = "EXCEPTION %s" % type(e).__name__
    print("PORTE %s : %s (attendu %s) : %s" % (nom, out, attendu, "OK" if out == attendu else "MORD"), flush=True)
