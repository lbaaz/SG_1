# -*- coding: ascii -*-
# AUDIT MACHINE 2 -- controle du dossier_trilemme_site_v2.md et du
# journal_delta_65_fusion_d_v3.md (2026-08-10).
# Toute valeur du dossier est RE-DERIVEE ; aucune n'est reutilisee comme entree.
# Aucune donnee de manche n'est ouverte (ni JSON, ni npz) : voir section
# "CE QUE CE LOG NE JOUE PAS" de la note.
import hashlib, os, unicodedata
from fractions import Fraction
from math import comb

B = r"D:\devs\bocal\BOCAL4"
D = os.path.dirname(os.path.abspath(__file__))

def emp(path):
    raw = open(path, "rb").read()
    txt = raw.decode("utf-8")
    canon = unicodedata.normalize("NFC", txt.replace("\r\n", "\n").replace("\r", "\n"))
    return (len(raw), hashlib.sha256(raw).hexdigest(),
            hashlib.sha256(canon.encode("utf-8")).hexdigest(),
            raw.count(b"\r"), sum(1 for c in txt if ord(c) > 127))

def ligne(nom, attendu=None):
    p = os.path.join(B, nom)
    if not os.path.exists(p):
        print("  ABSENT                                                     %s" % nom); return
    o, br, ca, cr, na = emp(p)
    v = ""
    if attendu:
        n = len(attendu)
        v = ("CONFORME" if br[:n] == attendu == ca[:n]
             else ("brut SEUL" if br[:n] == attendu
                   else ("canon SEUL" if ca[:n] == attendu else "MISMATCH")))
    print("  %7d o  brut %s  cano %s  CR=%d nonASCII=%-5d %-9s %s"
          % (o, br[:16], ca[:16], cr, na, v, nom))

print("=" * 72)
print("1. CUSTODY -- empreintes re-derivees localement (brut / canonique NFC+LF)")
print("=" * 72)
ligne("dossier_trilemme_site_v2.md")
ligne("dossier_trilemme_site_v1.md", "f8e1f257ea9541cb")
ligne("note_machine2_arbitrage_trilemme_v1.md", "1c490f90fafcf8ff")
ligne("journal_delta_65_fusion_d_v3.md", "e5931c94518916ce")
ligne("journal_delta_64_revue_note_c (1).md", "f4552c5f")
ligne("note_derivation_P1_signes_E_v5.md", "5704987e7d6ff7a6")
ligne("note_outreach_EN_unified_2026-08-10d.md", "74950a6b6912699c")
ligne("revue_pre_envoi_2026-08-10b_machine2_v1.md", "310e21716c502ef3")
ligne("depot_journal_delta_65_pseudonymisation_baaz_COPIE.md")
absents = [f for f in ("61", "62", "63")
           if not [x for x in os.listdir(B) if "delta_" + f in x]]
print("  deltas machine 1 annonces RE-PRESENTES en 65.5, absents de BOCAL4 : %s"
      % (", ".join(absents) if absents else "aucun"))

print()
print("=" * 72)
print("2. ESTIMATEUR q_L(80%) : borne q telle que P(Bin(n,q) <= k) = 0.20")
print("   (bisection 200 pas ; identification ACQUISE au tour precedent, 14/14)")
print("=" * 72)
def binle(n, k, q): return sum(comb(n, i) * q**i * (1 - q)**(n - i) for i in range(k + 1))
def qL(k, n, alpha=0.20, steps=200):
    lo, hi = 0.0, 1.0
    for _ in range(steps):
        m = (lo + hi) / 2.0
        if binle(n, k, m) > alpha: lo = m
        else: hi = m
    return (lo + hi) / 2.0
for (k, n), ref, lab in [((1, 12), 0.22961693269696845, "pilote M12"),
                         ((1, 34), 0.0855, "ITEM 3 p=4 domaine"),
                         ((3, 80), 0.0679, "ITEM 3 impair domaine")]:
    v = qL(k, n)
    print("  %-22s k=%2d n=%2d -> %.17f  registre %-21s ecart %.2e"
          % (lab, k, n, v, ref, abs(v - ref)))

print()
print("=" * 72)
print("3. ITEM 3 SUR LA FENETRE (v2 sections 3.2 et 3.3) -- regle 16")
print("=" * 72)
for (k, n), ref, lab in [((4, 7), 0.7717, "3.2 p=4 fenetre"),
                         ((2, 24), 0.1700, "3.2 impair fenetre"),
                         ((5, 9), 0.7325, "3.3 p=4 complement"),
                         ((3, 28), 0.1882, "3.3 impair complement")]:
    v = qL(k, n)
    print("  %-22s k=%d n=%2d -> %.4f  dossier %.4f  %s"
          % (lab, k, n, v, ref, "OK" if abs(v - ref) < 5e-5 else "ECART"))

print()
print("=" * 72)
print("4. D-1 -- instabilite du q_L de NIVEAU-POINT, quatre lectures non gouvernees")
print("=" * 72)
q4 = []
for (k, n), ref, lab in [((7, 8), 0.9725, "dossier v1 (retire)"),
                         ((7, 9), 0.9074, "2.72 compte vivant"),
                         ((6, 7), 0.9686, "2.67 grossiere retiree"),
                         ((6, 8), 0.8956, "les deux corrections")]:
    v = qL(k, n); q4.append(v)
    print("  %-24s k=%d n=%d -> %.4f  note %.4f  %s"
          % (lab, k, n, v, ref, "OK" if abs(v - ref) < 5e-5 else "ECART"))
print("  amplitude re-derivee = %.4f   (note d'arbitrage : 0.0769)" % (max(q4) - min(q4)))

print()
print("=" * 72)
print("5. RENDEMENTS -- E[surv] = N(1-q) ; P(>=1) = 1 - q^N")
print("=" * 72)
for k, n, lab in [(4, 7, "colonne fenetre    q_L=0.7717"),
                  (5, 9, "colonne complement q_L=0.7325")]:
    q = qL(k, n)
    print("  %s" % lab)
    for N in (3, 5, 7, 9):
        print("    N=%d : E[surv] = %.4f   P(>=1) = %.4f" % (N, N * (1 - q), 1 - q**N))

print()
print("=" * 72)
print("6. GEOMETRIE -- g(a,b,c) = (b-a)(c-b), b = 8/3, arithmetique EXACTE (Fraction)")
print("=" * 72)
b = Fraction(8, 3)
def g(a, c): return (b - Fraction(a)) * (Fraction(c) - b)
gM15, gREC, gINT = g("2.62", "2.73"), g("2.60", "2.80"), g("2.62", "2.72")
print("  corde M15   2.62-2.73 : g = %-10s (%.8f)" % (gM15, float(gM15)))
print("  recul       2.60-2.80 : g = %-10s (%.8f)" % (gREC, float(gREC)))
print("  corde int.  2.62-2.72 : g = %-10s (%.8f)" % (gINT, float(gINT)))
print("  ratio recul/M15    = %s = %.4f   (dossier 400/133 = 3.0075)" % (gREC / gM15, float(gREC / gM15)))
print("  ratio interne/M15  = %s  = %.4f   (dossier 16/19  = 0.842)" % (gINT / gM15, float(gINT / gM15)))

print()
print("=" * 72)
print("7. D-6 -- SENSIBILITE de l'inventaire complementaire 3.3 (non ecrit en extension)")
print("   La phrase de 3.3 cite TROIS apports (2.70, 2.67, 2.72) et rend n=9 :")
print("   7 (fenetre) + 1 (2.70) + 1 (2.67) = 9 exige que la ligne p=4 de 2.72")
print("   ne soit PAS comptee, alors que la meme phrase la nomme VIVANTE.")
print("=" * 72)
for k, n, lab in [(5, 9, "3.3 tel qu ecrit (2.72 hors compte)"),
                  (5, 10, "2.72 p=4 comptee vivante")]:
    q = qL(k, n)
    print("  %-38s k=%d n=%2d -> q_L = %.4f   P(>=1|N=3) = %.4f"
          % (lab, k, n, q, 1 - q**3))
print("  amplitude sur la colonne de dimensionnement = %.4f" % abs(qL(5, 9) - qL(5, 10)))
print("  (a comparer aux 0.0769 qui ont fait RETIRER le q_L niveau-point en D-1)")
print("  impair : 24 -> 28 lignes, +4, dont 1 seule attribuee (7|2.67|+1) ;")
for k, n in [(3, 28), (3, 29), (3, 30)]:
    print("    k=%d n=%d -> q_L = %.4f" % (k, n, qL(k, n)))

print()
print("=" * 72)
print("8. D-7 / N-20 -- ce que la v2 porte encore en clair")
print("=" * 72)
t2 = open(os.path.join(B, "dossier_trilemme_site_v2.md"), encoding="utf-8").read()
for s in ("0.9725", "0.9074", "0.9686", "0.8956", "niveau-point", "N = 9"):
    print("  occurrences de %-14s : %d" % ("'" + s + "'", t2.count(s)))
print("  N-20..N-26 presents : %s"
      % ", ".join("N-%d(%d)" % (i, t2.count("N-%d" % i)) for i in range(20, 27)))

print()
print("=" * 72)
print("9. COLLISION DE NUMERO DE DELTA 65 -- deux pieces distinctes")
print("=" * 72)
print("  machine 1 : journal_delta_65_fusion_d_v3.md            e5931c94518916ce  4380 o")
print("  depot     : journal/journal_delta_65_pseudonymisation_baaz.md")
print("              5ad0561e14ec563e  3003 o  (releve : gh api repos/lbaaz/SG_1)")
print("  les deux declarent s'inserer APRES le delta 64.")
print("  journal/ du depot public, deltas releves : 50..60, 64, 65 -- 61/62/63 ABSENTS")
print("  des DEUX registres (BOCAL4 et depot).")
print()
print("=== FIN DE L'AUDIT ===")
