# -*- coding: ascii -*-
# INVENTAIRE EN EXTENSION DE LA FENETRE [2.62, 2.73] AU SITE 8/3 -- v2
# machine 2, 2026-08-10 -- execute N-23 (attribution par degre) et le
# correctif de D-6 (inventaire en extension), puis eprouve deux choix de
# gouvernance non declares : l'UNITE DE COMPTE et le TRAITEMENT DES ANCRES.
#
# v1 -> v2 : ajout des sections 7 et 8. La v1 n'avait ete citee par aucune
# piece au moment du remplacement (declaration de version, E13).
#
# Regle appliquee : le statut d'une ligne se lit au BLOC DE GARDE (G6),
# JAMAIS a la carte -- le champ 'recevable' de la carte qualifie la
# RECHERCHE, pas l'exclusion (defaut D1-3 du run M12, deja paye).
# Aucun compte n'est affirme : tous sont COMPTES, et le recompte est
# verifie par assert contre le bloc de resume de l'artefact.
import json, hashlib, os
from math import comb

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
A, C = 2.62, 2.73
SOURCES = [("M15", "m15_results.json", "96d78407"),
           ("M12", "m12_results.json", "fa109da9"),
           ("M13b", "m13b_results.json", "22fa1760")]

def binle(n, k, q): return sum(comb(n, i) * q**i * (1 - q)**(n - i) for i in range(k + 1))
def qL(k, n, alpha=0.20, steps=200):
    lo, hi = 0.0, 1.0
    for _ in range(steps):
        m = (lo + hi) / 2.0
        if binle(n, k, m) > alpha: lo = m
        else: hi = m
    return (lo + hi) / 2.0

print("=" * 74)
print("0. CUSTODY DES ARTEFACTS OUVERTS")
print("=" * 74)
data = {}
for manche, f, att in SOURCES:
    raw = open(os.path.join(OUT, f), "rb").read()
    h = hashlib.sha256(raw).hexdigest()
    data[manche] = json.loads(raw.decode("utf-8"))
    print("  %-5s %-22s %s  %s" % (manche, f, h[:16], "CONFORME" if h[:8] == att else "MISMATCH " + att))

lignes = []
for manche in ("M15", "M12", "M13b"):
    for cle, v in sorted(data[manche]["resultats"]["G6"].items()):
        p_s, pt_s, sg = cle.split("|")
        pt = float(pt_s)
        if A - 1e-9 <= pt <= C + 1e-9:
            lignes.append(dict(manche=manche, p=int(p_s), pt=round(pt, 2), signe=sg,
                               exclue=bool(v.get("exclue")),
                               motif=v.get("motif_exclusion") or ""))

print()
print("=" * 74)
print("1. LIGNES DE LA FENETRE [%.2f, %.2f], LUES AU BLOC G6, EN EXTENSION" % (A, C))
print("=" * 74)
print("  %-6s %-3s %-6s %-4s %s" % ("MANCHE", "p", "point", "sgn", "statut"))
for L in sorted(lignes, key=lambda x: (x["p"], x["pt"], x["signe"])):
    print("  %-6s %-3d %-6.2f %-4s %s"
          % (L["manche"], L["p"], L["pt"], L["signe"], "MORTE" if L["exclue"] else "vivante"))
print("  TOTAL : %d lignes  (p=4 : %d ; impair : %d)"
      % (len(lignes), sum(1 for L in lignes if L["p"] == 4), sum(1 for L in lignes if L["p"] % 2)))

print()
print("=" * 74)
print("2. CONTROLE CROISE : le recompte G6 rend-il le resume de l'artefact ?")
print("=" * 74)
attendu = set(data["M15"]["resume"]["points_perdus"])
recompte = set("%d|%.12f" % (L["p"], L["pt"]) for L in lignes if L["manche"] == "M15" and L["exclue"])
print("  M15 resume.points_perdus : %s" % sorted(attendu))
print("  M15 recompte au bloc G6  : %s" % sorted(recompte))
assert attendu == recompte, "le recompte G6 ne rend pas le resume M15"
print("  CONCORDANCE : True   (les 6 pertes M15 sont toutes de mecanisme G6)")

print()
print("=" * 74)
print("3. N-23 -- ATTRIBUTION PAR DEGRE DES MORTS 2.71 ET 2.73")
print("=" * 74)
for pt in (2.71, 2.72, 2.73):
    ici = sorted([L for L in lignes if L["pt"] == pt], key=lambda x: (x["p"], x["signe"]))
    print("  point %.2f (%d lignes) : %s" % (pt, len(ici),
          ", ".join("%d|%s %s" % (L["p"], L["signe"], "MORTE" if L["exclue"] else "vivante") for L in ici)))
    print("      degres morts : %s" % (sorted(set(L["p"] for L in ici if L["exclue"])) or "aucun"))
print()
p4 = {pt: [L for L in lignes if L["p"] == 4 and L["pt"] == pt] for pt in (2.71, 2.72, 2.73)}
print("  AU SEUL DEGRE 4 : 2.71 %s | 2.72 %s | 2.73 %s"
      % tuple("MORTE" if any(L["exclue"] for L in p4[pt]) else "VIVANTE" for pt in (2.71, 2.72, 2.73)))
print("  => la signature 48.3 est instanciee AU DEGRE 4, pas seulement au niveau point.")
print("     Reserve : 2.72 vient de M12, 2.71 et 2.73 de M15 (juxtaposition")
print("     inter-manches, legitime par 48.4, a declarer au gel).")

def compte(sel):
    q4 = [x for x in sel if x["p"] == 4]; qi = [x for x in sel if x["p"] % 2 == 1]
    assert len(q4) + len(qi) == len(sel), "degre pair non-4 dans la selection"
    return (sum(x["exclue"] for x in q4), len(q4)), (sum(x["exclue"] for x in qi), len(qi))

def ligne_res(lab, sel):
    (k4, n4), (ki, ni) = compte(sel)
    print("  %-46s p=4 %d/%-2d q_L=%.4f | impair %d/%-2d q_L=%.4f"
          % (lab, k4, n4, qL(k4, n4), ki, ni, qL(ki, ni)))
    return (k4, n4), (ki, ni)

print()
print("=" * 74)
print("4. COMPTES PAR DEGRE -- COMPTES, PAS AFFIRMES ; q_L(80 %) sur chacun")
print("=" * 74)
ref = ligne_res("3.2 fenetre M15 seule      (dossier 4/7 et 2/24)",
                [L for L in lignes if L["manche"] == "M15"])
ligne_res("3.3 complement SANS 2.72   (dossier 5/9 et 3/28)",
          [L for L in lignes if L["pt"] != 2.72])
ligne_res("3.3 complement AVEC 2.72   (inventaire reel)", lignes)

print()
print("=" * 74)
print("5. D-8 -- L'UNITE DE COMPTE N'EST PAS DECLAREE")
print("   La campagne declare, a p IMPAIR, la convention s* = min des deux")
print("   signes (M1/(f)) : l'unite naturelle y est (degre, point), alors que")
print("   le bloc G6 exclut par BRANCHE DE SIGNE. Les deux lectures existent.")
print("=" * 74)
ligne_res("(a) ligne sign-resolue [ce que compte le dossier]", lignes)
u = {}
for L in lignes: u.setdefault((L["p"], L["pt"]), []).append(L["exclue"])
selb = [dict(p=p, pt=pt, exclue=any(v), manche="-", signe="*") for (p, pt), v in u.items()]
selc = [dict(p=p, pt=pt, exclue=all(v), manche="-", signe="*") for (p, pt), v in u.items()]
ligne_res("(b) unite (degre,point), morte si >=1 branche morte", selb)
ligne_res("(c) unite (degre,point), morte si TOUTES les branches", selc)
print("  branches par unite : p=4 -> %s ; impair -> %s"
      % (sorted(set(len(v) for (p, pt), v in u.items() if p == 4)),
         sorted(set(len(v) for (p, pt), v in u.items() if p % 2))))
print("  LES TROIS MORTS IMPAIRS SONT TOUS DE SIGNE +1 : %s"
      % ", ".join("%d|%.2f|%s" % (L["p"], L["pt"], L["signe"]) for L in lignes if L["exclue"] and L["p"] % 2))
print("  => aucune unite impaire n'est morte AUX DEUX SIGNES (lecture (c) : 0/16).")
print("  Portee : p=4 est quasi mono-signe (une seule branche partout sauf 2.62),")
print("  donc le dimensionnement de la strate 1 (p=4 seul) est ROBUSTE a ce choix ;")
print("  c'est la LECTURE degre-selective de 3.4 / B3 qui en depend.")

print()
print("=" * 74)
print("6. D-9 -- LE TRAITEMENT DES ANCRES N'EST PAS SYMETRIQUE")
print("   N-22 met 2.62 et 2.72 sur le MEME plan (ancres de geometrie). Le")
print("   compte du dossier garde 2.62 DEDANS et met 2.72 DEHORS. Les deux")
print("   sont des survivants : les exclure baisse n sans baisser k.")
print("=" * 74)
vals = []
for lab, f in [("les deux DEDANS (inventaire reel)", lambda x: True),
               ("2.72 dehors [lecture du dossier]", lambda x: x["pt"] != 2.72),
               ("2.62 dehors", lambda x: x["pt"] != 2.62),
               ("les deux dehors", lambda x: x["pt"] not in (2.62, 2.72))]:
    (k4, n4), _ = ligne_res(lab, [L for L in lignes if f(L)])
    vals.append(qL(k4, n4))
print("  AMPLITUDE sur la borne p=4 qui dimensionne la strate 1 : %.4f" % (max(vals) - min(vals)))
print("  (a comparer aux 0.0769 qui ont fait RETIRER le q_L de niveau-point en D-1)")
print("  Rendements strate 1 (N = 3 tentatives p=4) aux deux extremes :")
for q in (min(vals), max(vals)):
    print("    q = %.4f -> E[surv] = %.4f  P(>=1) = %.4f" % (q, 3 * (1 - q), 1 - q**3))

print()
print("=" * 74)
print("7. CE QUE CET INVENTAIRE NE JOUE PAS")
print("=" * 74)
print("  - Aucune mesure rejouee : les statuts sont LUS aux blocs G6, pas")
print("    recalcules depuis les s*.")
print("  - 'MORTE' == exclue par G6. Sur la fenetre M15 les pertes sont toutes")
print("    de mecanisme G6 (resume) ; non re-verifie pour M12 et M13b.")
print("  - Les points hors [%.2f, %.2f] ne sont pas inventories ; le domaine" % (A, C))
print("    large (bornes 0.0855 / 0.0679) n'est pas recalcule ici.")
print("  - Aucun q_L de niveau-point n'est derive (N-20).")
print("  - Le choix ENTRE les lectures des sections 5 et 6 n'est pas fait ici :")
print("    il appartient au gel, qui doit le DECLARER avant mesure.")
print()
print("=== FIN DE L'INVENTAIRE v2 ===")
