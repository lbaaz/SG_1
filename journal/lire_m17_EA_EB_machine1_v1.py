# Lecture hors chaine : Gamma_c (E-A, chaine) contre Gamma_LS (E-B, 2D) aux points M17 deja joues.
import sys, json, os, math
d = sys.argv[1]
def cles(o, pref="", prof=0, out=None):
    out = [] if out is None else out
    if isinstance(o, dict) and prof < 3:
        for k, v in o.items():
            cles(v, pref + "/" + str(k), prof + 1, out)
    else:
        s = json.dumps(o)
        out.append((pref, s[:70]))
    return out
if sys.argv[2] == "cles":
    j = json.load(open(os.path.join(d, sys.argv[3]), encoding="utf-8"))
    for k, v in cles(j):
        print(k, "=", v)
if sys.argv[2] == "table":
    noms = sorted(f for f in os.listdir(d) if f.startswith("pt_") and "_f" in f and f.endswith(".json"))
    lignes = []
    for f in noms:
        j = json.load(open(os.path.join(d, f), encoding="utf-8"))
        num, den, fr = f[3:-5].split("_")
        w2 = int(num) / int(den)
        ea, eb = j.get("EA", {}), j.get("EB", {})
        gc = (ea.get("Gamma_c") or {}).get("val")
        lam = ea.get("Lambda_c")
        gls = ((eb.get("Gamma_LS") or {}).get("H") or {}).get("Gamma_LS")
        gp = ((eb.get("Gamma_LS") or {}).get("Hplus") or {}).get("Gamma_LS")
        lignes.append((w2, fr, gc, lam, gls, gp, ea.get("card_Bc"), ea.get("barriere_vide"),
                       (j.get("domaine") or {}).get("statut")))
    print("w2    frac  Gamma_c      Lambda_c  Gamma_LS     Gc/GLS    log10   card  vide  domaine")
    for (w2, fr, gc, lam, gls, gp, card, vide, dom) in sorted(lignes):
        r = (gc / gls) if (gc and gls and gls > 0) else None
        print("%.2f  %s  %s  %s  %s  %s  %s  %s  %s  %s" % (
            w2, fr, ("%.3e" % gc) if gc is not None else "   --    ",
            ("%7.3f" % lam) if lam is not None else "   --  ",
            ("%.3e" % gls) if gls is not None else "   --    ",
            ("%8.2f" % r) if r else "    --  ", ("%+.2f" % math.log10(r)) if r else "  -- ",
            card, vide, dom))
