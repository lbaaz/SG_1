# -*- coding: ascii -*-
# Construit lecture_piste0_etape0_machine1_v2.py depuis le v1 par hunks a ancre unique.
import sys
src = open(sys.argv[1], encoding="ascii").read()
H = []
# H1 (D-P0-1) : la regle HORS PLAGE ne se prononce pas sur une valeur non finie
H.append(('''                x = pts[j][cle]
                if wd == 0:''', '''                x = pts[j][cle]
                if x != x:
                    non_lisibles.append(("%.2f" % j, cle))
                    print("  [%s] %-6s O=[%.4e, %.4e]  %.2f : NON LISIBLE"
                          " (valeur non finie), ni dans ni hors la plage"
                          % (g_, cle, lo, hi, j))
                    continue
                if wd == 0:'''))
H.append(('''    hors = {("%.2f" % j): {"A": [], "I": []} for j in T}
''', '''    hors = {("%.2f" % j): {"A": [], "I": []} for j in T}
    non_lisibles = []
'''))
H.append(('''    res["L2_L3"] = {"hors": hors, "L2": l2, "L3": l3}''',
          '''    print("  non lisibles (D-P0-1) : %s" % non_lisibles)
    res["L2_L3"] = {"hors": hors, "L2": l2, "L3": l3,
                    "non_lisibles": non_lisibles}'''))
# H2 (D-P0-2) : rho(G, R) seulement la ou R existe, compte declare
H.append(('''    r_gr, _, _ = spearman(G, R)
''', '''    wR = [w for w in ws if pts[w]["R"] == pts[w]["R"]]
    r_gr, _, _ = spearman([pts[w]["G"] for w in wR],
                          [pts[w]["R"] for w in wR])
'''))
H.append(('''    print("    rho(G, R)  = %s" % r_gr)''',
          '''    print("    rho(G, R)  = %s sur %d points ou R existe + %d sans R"
          " == %d (D-P0-2)" % (r_gr, len(wR), len(ws) - len(wR), len(ws)))'''))
# H3 (D-P0-3) : le signe du dernier pas n'existe que si 0 < r < 1
H.append(('''    sg = {w: (1 if pts[w]["R"] > pts[w]["G"] else -1) for w in ws}
    l5 = len(set(sg.values())) == 1''',
          '''    sg = {w: ((1 if pts[w]["R"] > pts[w]["G"] else -1)
              if 0.0 < pts[w]["r"] < 1.0 else 0) for w in ws}
    l5 = (0 not in sg.values()) and len(set(sg.values())) == 1
    print("    (0 = NON DEFINI : r hors de ]0, 1[, Richardson absent --"
          " D-P0-3) ; definis %d + non definis %d == %d" % (
              sum(1 for v in sg.values() if v), sum(1 for v in sg.values()
              if not v), len(ws)))'''))
# H4 : le budget B nomme ses termes ; residu non fini = terme absent, declare
H.append(('''    B = {w: max(pts[w]["t"], pts[w]["n"], pts[w]["p3"], abs(pts[w]["res"]))
         for w in ws}''',
          '''    B = {w: max([pts[w]["t"], pts[w]["n"], pts[w]["p3"]]
                + ([abs(pts[w]["res"])] if pts[w]["res"] == pts[w]["res"]
                   else [])) for w in ws}
    print("\\n    points SANS residu (r hors de ]0, 1[), B sur trois termes :"
          " %s" % ["%.2f" % w for w in ws if pts[w]["res"] != pts[w]["res"]])'''))
for old, new in H:
    if src.count(old) != 1:
        sys.exit("ancre non unique : %r (%d)" % (old[:50], src.count(old)))
    src = src.replace(old, new)
src = src.replace("etape 0 -- machine 1\n", "etape 0 -- machine 1 -- v2 = v1 + 7 remplacements (D-P0-1..3, B)\n", 1)
open(sys.argv[2], "w", encoding="ascii").write(src)
print("remplacements appliques : %d + 1 ligne d'en-tete" % len(H))
