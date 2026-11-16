# Canon (convention B) de chaque fichier MANIFEST* sous les dossiers donnes ; n'affiche que les canons demandes.
# Arguments : <canons separes par des virgules> <dossier> ...
import sys, os, hashlib, unicodedata
voulus = set(sys.argv[1].split(","))
def cB(b):
    t = unicodedata.normalize("NFC", b.decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
vus = {}
for base in sys.argv[2:]:
    for d, ds, fs in os.walk(base):
        for f in fs:
            if f.startswith("MANIFEST") and f.endswith(".txt"):
                p = os.path.join(d, f)
                try: c = cB(open(p, "rb").read())
                except Exception: continue
                if c in voulus and c not in vus:
                    vus[c] = p
for c in sorted(voulus): print(c, vus.get(c))
