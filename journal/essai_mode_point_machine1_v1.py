# -*- coding: ascii -*-
"""Essai du chemin "point" de la sonde SANS toucher a un point juge : une COPIE ALTEREE de la sonde, ou la liste des
points juges est remplacee par l'ancre A1 et le seuil de choix des etats par 1e-6 (trois etats), est jouee en mode
point ; on controle la forme de la sortie. Non opposable ; la sonde du gel n'est pas modifiee.
Usage : python3 -I essai_mode_point_machine1_v1.py <sonde.py> <moteur.py> <sonde_ordre2.json> <tp_retenus.json> <travail>"""
import sys, os, json, subprocess
SONDE, MOTEUR, DEPOT, RETENUS, TRAVAIL = sys.argv[1:6]
s = open(SONDE).read()
a = 'JUGES = ["C1", "C2", "C3", "C4", "M1", "M2", "M3", "M4", "L1", "L2", "L3", "L4"]'; assert s.count(a) == 1
b = "PLANCHER10 = 1.33e-12 "; assert s.count(b) == 1
s2 = s.replace(a, 'JUGES = ["A1"]').replace(b, "PLANCHER10 = 1e-6 ")
os.makedirs(TRAVAIL, exist_ok=True); f = os.path.join(TRAVAIL, "sonde_alteree_pour_essai.py"); open(f, "w", newline="\n").write(s2)
r = subprocess.run([sys.executable, "-I", f, MOTEUR, DEPOT, RETENUS, TRAVAIL, "point", "A1"], capture_output=True, text=True)
print(r.stdout[-600:]); assert r.returncode == 0, r.stderr[-800:]
o = json.load(open(os.path.join(TRAVAIL, "sonde_ter_point_A1.json")))
p = o["points"][0]; ks = [str(k) for k in range(-3, 9)]
ok = (o["mode"] == "point" and o["ids"] == ["A1"] and len(o["points"]) == 1 and p["id"] == "A1"
      and sorted(e["rang"] for e in p["etats"]) == [6, 12, 13]
      and all(sorted(e["traj"]) == ["A", "B", "C", "D"] and all(sorted(e["traj"][x], key=int) == ks for x in "ABCD") for e in p["etats"])
      and all(e["traj"][x][k]["suivi"] for e in p["etats"] for x in "ABCD" for k in ks)
      and set(p["etats"][0]) >= {"rang", "n1", "n2", "E_depart", "G_dep", "traj"}
      and p["absorbeurs"]["A"] == {"forme": "F2", "bord": 40, "couches": 80, "N": 120} and p["absorbeurs"]["D"] == {"forme": "F2", "bord": 50, "couches": 80, "N": 130})
for e in p["etats"]:
    for x in "ABCD":
        v = [e["traj"][x][k]["gamma"] for k in ks]
        print("  rang %2d %s : meilleur etalement %.4f" % (e["rang"], x, min(max(v[i:i + 5]) / min(v[i:i + 5]) - 1.0 for i in range(8))))
print("ESSAI DU MODE POINT (copie alteree, ancre A1, trois etats) : forme de la sortie %s ; duree %.0f s" % ("TENUE" if ok else "FAUSSE", o["duree_s"]))
sys.exit(0 if ok else 1)
