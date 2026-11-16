# -*- coding: ascii -*-
"""REJEU PARTIEL, par machine 1, de lectures du run juge du gel E-B ter -- APRES reception et authentification du lot
de resultat (gel, section 12 : "elle peut ensuite rejouer"). Non opposable.
Le code execute est celui de la sonde certifiee, pris tel quel jusqu'a "def main():" (arguments, canons, bloc du
lecteur, mesurer_point) ; seule la liste des etats du point est restreinte aux rangs demandes. Chaque etat etant lu
independamment des autres (trajectoire repart du depot), les lectures sont celles que la sonde rend en mode point.
Usage : python3 -I rejeu_partiel_machine1_v1.py <sonde.py> <moteur.py> <sonde_ordre2.json> <tp_retenus.json>
        <dossier de sortie> <id:rang,rang> [<id:rang,...> ...]
Ecrit un fichier rejeu_partiel_<id>.json par point, au fur et a mesure."""
import sys, os, json, time
SONDE, MOTEUR, DEPOT, RETENUS, DOSSIER = sys.argv[1:6]
SEL = [(a.split(":")[0], [int(x) for x in a.split(":")[1].split(",")]) for a in sys.argv[6:]]
src = open(SONDE, encoding="ascii").read()
tete = src[:src.index("\ndef main():")]
sys.argv = [SONDE, MOTEUR, DEPOT, RETENUS, DOSSIER, "point", SEL[0][0]]
ns = {"__name__": "sonde_tete", "__file__": SONDE}
exec(compile(tete, SONDE, "exec"), ns)
D = json.load(open(DEPOT)); P = {p["id"]: p for p in D["points"]}
os.makedirs(DOSSIER, exist_ok=True)
for pid, rangs in SEL:
    assert pid in ns["JUGES"]
    p = dict(P[pid]); juges = [e["rang"] for e in ns["etats_du_point"](P[pid], "juges")]
    assert all(r in juges for r in rangs), (pid, rangs, juges)
    p["etats"] = [e for e in P[pid]["etats"] if e["rang"] in rangs]
    t0 = time.time()
    pt = ns["mesurer_point"](p, "juges", ns["ABSORBEURS"], ns["KS"])
    out = {"rejeu_partiel": True, "sonde_canon": ns["canon_B"](SONDE), "id": pid, "rangs": rangs, "point": pt,
           "plateforme": {"python": ns["platform"].python_version(), "numpy": ns["np"].__version__, "scipy": ns["scipy"].__version__,
                          "systeme": ns["platform"].system(), "levier": os.environ.get("NPY_DISABLE_CPU_FEATURES")}}
    json.dump(out, open(os.path.join(DOSSIER, "rejeu_partiel_%s.json" % pid), "w"), indent=1, sort_keys=True)
    print("ecrit rejeu_partiel_%s.json (%d etats, %.0f s)" % (pid, len(rangs), time.time() - t0), flush=True)
print("FIN DU REJEU PARTIEL", flush=True)
