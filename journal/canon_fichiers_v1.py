# Convention B : sha256(UTF-8 NFC, fins de ligne LF), 16 premiers hex. Usage : canon_fichiers_v1.py <racine> <canon>...
import sys, os, hashlib, unicodedata
def canon(path):
    b = open(path, 'rb').read()
    try:
        t = b.decode('utf-8')
    except UnicodeDecodeError:
        return None
    t = unicodedata.normalize('NFC', t).replace('\r\n', '\n').replace('\r', '\n')
    return hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]
racine = sys.argv[1]; cibles = set(sys.argv[2:])
trouve = {}
for d, _, fs in os.walk(racine):
    if '/.git' in d: continue
    for f in fs:
        p = os.path.join(d, f)
        c = canon(p)
        if c in cibles:
            trouve.setdefault(c, []).append(os.path.relpath(p, racine))
for c in sys.argv[2:]:
    print(c, trouve.get(c, ['ABSENT']))
