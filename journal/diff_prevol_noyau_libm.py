# -*- coding: ascii -*-
# Comparaison feuille par feuille des deux pre-vols du banc v8 (noyau SIMD actif / desactive), sur le meme poste.
import json, sys
A = json.load(open(sys.argv[1])); B = json.load(open(sys.argv[2]))
feuilles_A = {}; feuilles_B = {}
def aplatir(o, chemin, out):
    if isinstance(o, dict):
        for k in sorted(o): aplatir(o[k], chemin + "/" + str(k), out)
    elif isinstance(o, list):
        for i, v in enumerate(o): aplatir(v, chemin + "[%d]" % i, out)
    else:
        out[chemin] = o
aplatir(A, "", feuilles_A); aplatir(B, "", feuilles_B)
cles = sorted(set(feuilles_A) | set(feuilles_B))
diff = [c for c in cles if feuilles_A.get(c, "<absent>") != feuilles_B.get(c, "<absent>")]
print("feuilles : %d (noyau) / %d (libm) ; identiques : %d ; DIFFERENTES : %d" % (len(feuilles_A), len(feuilles_B), len(cles) - len(diff), len(diff)))
exempt = [c for c in diff if any(m in c.lower() for m in ("duree", "date", "utc", "chemin", "sortie", "temps", "secondes", "horodat", "version_python", "plateforme"))]
print("  dont exemptables par nature (duree/date/chemin) : %d" % len(exempt))
for c in diff:
    a, b = feuilles_A.get(c, "<absent>"), feuilles_B.get(c, "<absent>")
    print("  %-90s %r  |  %r" % (c[:90], a, b))
