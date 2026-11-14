# Fabrique generique d'un lot machine 1 : manifeste a cinq colonnes + ZIP. usage : <nom_lot> <titre> <fichier>...
import sys, re, hashlib, unicodedata, io, zipfile, os
nom, titre, fichiers = sys.argv[1], sys.argv[2], sys.argv[3:]
def B(octets):
    t = unicodedata.normalize("NFC", octets.decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
    return hashlib.sha256(t).hexdigest()[:16], len(t)
lignes = ["MANIFESTE %s -- %s" % (nom, titre),
          "colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier",
          "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.", ""]
for f in fichiers:
    o = open(f, "rb").read(); b, nb = B(o)
    lignes.append("%s  %s  %d  %d  %s" % (b, hashlib.sha256(o).hexdigest()[:16], nb, len(o), os.path.basename(f)))
man = "MANIFEST_" + re.sub(r"_2026-[0-9][0-9]-[0-9][0-9]", "", nom) + ".txt"
io.open(man, "w", encoding="utf-8", newline="\n").write("\n".join(lignes) + "\n")
with zipfile.ZipFile(nom + ".zip", "w", zipfile.ZIP_DEFLATED) as z:
    for f in fichiers:
        z.write(f, os.path.basename(f))
print("CANON", B(open(man, "rb").read())[0], man, len(fichiers), "pieces")
