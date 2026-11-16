# Second niveau du perimetre : pour chaque gel du registre, les empreintes de 16 hex qu'il cite et qui ne repondent
# a aucun fichier du registre (convention B). Lecture seule. Argument : <clone> [motif de nom ...]
import sys, os, re, hashlib, unicodedata
clone = sys.argv[1]; motifs = sys.argv[2:]
def cB(b):
    try: t = unicodedata.normalize("NFC", b.decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    except UnicodeDecodeError: return None
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
idx = set()
for d, ds, fs in os.walk(clone):
    if ".git" in ds: ds.remove(".git")
    for f in fs:
        e = cB(open(os.path.join(d, f), "rb").read())
        if e: idx.add(e)
for f in sorted(os.listdir(os.path.join(clone, "gels"))):
    if motifs and not any(m in f for m in motifs): continue
    t = open(os.path.join(clone, "gels", f), "rb").read().decode("utf-8", "replace")
    cit = sorted(set(re.findall(r"(?<![0-9a-f])[0-9a-f]{16}(?![0-9a-f])", t)))
    non = [c for c in cit if c not in idx]
    print("%-70s citees %3d  non resolues %2d  %s" % (f[:70], len(cit), len(non), non))
