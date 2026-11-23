# note_pole_court_machine1_v1.py -- machine 1, 2026-11-22
# NOTATION, par mon propre code, des attendus S-1, S-2, S-3 et de la clause de tort (ma 22f, section 6,
# note 6eae3f6860a46eef) sur les huit sorties JSON de machine 2 (lot 2d69195af996cc0f), lues comme des
# donnees. Rien du lot n'est execute ni importe : les JSON sont lus par json.load, le script d'analyse
# de machine 2 n'est lu que comme un TEXTE, pour comparer sa recopie de ma table a la mienne.
# Aucune fenetre n'est desserree : les bornes sont celles ecrites avant.
# Usage : python3 -I note_pole_court_machine1_v1.py <dossier des JSON> <script d'analyse de machine 2>
import sys, json, os, re

DOS, ANALYSE_M2 = sys.argv[1], sys.argv[2]

# Ma table de la section 5, recopiee de ma note au projet, dans sa mise en page.
TABLE_TEXTE = """
    g = 5e-04          a = 2                      a = 4
    m_c = 10    0.05435 0.05435 0.05422    0.05436 0.05453 0.05440
    m_c = 11    0.05443 0.05450 0.05454    0.05439 0.05447 0.05435
    m_c = 12    0.05439 0.05442 0.05436    0.05439 0.05445 0.05441
    m_c = 13    0.05442 0.05446 0.05446    0.05440 0.05445 0.05443
    g = 1e-03          a = 2                      a = 4
    m_c = 10    0.05435 0.05435 0.05422    0.05436 0.05453 0.05440
    m_c = 11    0.05443 0.05450 0.05454    0.05439 0.05447 0.05435
    m_c = 12    0.05439 0.05442 0.05437    0.05439 0.05445 0.05441
    m_c = 13    0.05442 0.05446 0.05445    0.05440 0.05445 0.05443
    g = 5e-04          a = 0.5                    a = 1
    m_c = 10    0.04161 0.03937 0.03687    0.05253 0.05171 0.05054
    m_c = 11    0.06964 0.07371 0.07901    0.05584 0.05654 0.05749
    m_c = 12    0.04482 0.04306 0.04106    0.05342 0.05299 0.05235
    m_c = 13    0.06472 0.06725 0.07042    0.05515 0.05551 0.05599
    g = 1e-03          a = 0.5                    a = 1
    m_c = 10    0.04171 0.03947 0.03697    0.05255 0.05174 0.05058
    m_c = 11    0.06916 0.07301 0.07793    0.05581 0.05650 0.05743
    m_c = 12    0.04500 0.04326 0.04128    0.05345 0.05303 0.05240
    m_c = 13    0.06413 0.06644 0.06930    0.05513 0.05547 0.05592
"""

def lire_ma_table(texte):
    table, g, a_gauche, a_droite = {}, None, None, None
    for l in texte.strip("\n").split("\n"):
        m = re.match(r"\s*g = (\S+)\s+a = (\S+)\s+a = (\S+)\s*$", l)
        if m:
            g, a_gauche, a_droite = float(m.group(1)), float(m.group(2)), float(m.group(3))
            continue
        m = re.match(r"\s*m_c = (\d+)\s+(\S+) (\S+) (\S+)\s+(\S+) (\S+) (\S+)\s*$", l)
        assert m, l
        mc = int(m.group(1))
        v = [float(m.group(k)) for k in range(2, 8)]
        for i, m0 in enumerate((2, 3, 4)):
            table[(g, mc, a_gauche, m0)] = v[i]
            table[(g, mc, a_droite, m0)] = v[3 + i]
    return table

def lire_table_m2(chemin):
    # lecture TEXTUELLE de sa recopie : lignes "(g, a): {mc: (x, y, z), ...}"
    table = {}
    for l in open(chemin, encoding="ascii").read().split("\n"):
        m = re.match(r"\s*\((\S+), (\S+)\): \{(.*)\},\s*$", l)
        if not m:
            continue
        g, a = float(m.group(1)), float(m.group(2))
        for mc, x, y, z in re.findall(r"(\d+): \((\S+), (\S+), (\S+)\)", m.group(3)):
            for m0, val in zip((2, 3, 4), (x, y, z)):
                table[(g, int(mc), a, m0)] = float(val)
    return table

T1 = lire_ma_table(TABLE_TEXTE)
T2 = lire_table_m2(ANALYSE_M2)
print("=== 0. ma table et sa recopie")
print("nombres dans ma recopie de ma note : %d (attendu 96)" % len(T1))
print("nombres dans la recopie de machine 2 (lue comme un texte) : %d (attendu 96)" % len(T2))
diff = [k for k in T1 if k not in T2 or T1[k] != T2[k]]
print("cles differentes entre les deux recopies : %d" % len(diff))
assert len(T1) == 96 and len(T2) == 96 and not diff

fichiers = sorted(f for f in os.listdir(DOS) if f.startswith("pole_court_b") and f.endswith(".json"))
print()
print("=== 1. sorties lues : %d (attendu 8)" % len(fichiers))
assert len(fichiers) == 8
cas = []
TAILLES = {10: 868, 11: 869, 12: 1181, 13: 1182}
pire_somme, pire_residu = 0.0, 0.0
for f in fichiers:
    s = json.load(open(os.path.join(DOS, f)))
    assert s["taille"] == TAILLES[s["m_coupe"]], (f, s["taille"])
    assert len(s["cas"]) == 12, f
    for c in s["cas"]:
        ec = abs(c["somme_poids"][0] - 1.0) + abs(c["somme_poids"][1])
        pire_somme, pire_residu = max(pire_somme, ec), max(pire_residu, c["residu"])
        cas.append((s["g"], s["m_coupe"], c["a"], c["m0"], c["gamma_sur_g"], c["re_sur_g"], c["poids_abs"]))
print("cas lus : %d (attendu 96) ; cles distinctes : %d" % (len(cas), len(set(t[:4] for t in cas))))
assert len(cas) == 96 and len(set(t[:4] for t in cas)) == 96
assert set(t[:4] for t in cas) == set(T1.keys())
print("tailles : 868, 869, 1181, 1182 : oui ; pire |somme des poids - 1| : %.1e ; pire residu : %.1e" % (pire_somme, pire_residu))

fort = [t for t in cas if t[2] in (2.0, 4.0)]
print()
print("=== 2. S-1 : aux 48 cas a = 2 et 4, Gamma / g dans [0.0539, 0.0549]")
hors = [t for t in fort if not (0.0539 <= t[4] <= 0.0549)]
print("cas : %d ; plus petit %.6f ; plus grand %.6f ; hors fenetre : %d" % (len(fort), min(t[4] for t in fort), max(t[4] for t in fort), len(hors)))
print("marge a la borne basse %.2e ; a la borne haute %.2e" % (min(t[4] for t in fort) - 0.0539, 0.0549 - max(t[4] for t in fort)))
S1 = len(fort) == 48 and not hors
print("S-1 : %s" % ("TENU aux 48 cas" if S1 else "TOMBE"))

print()
print("=== 3. S-2 : aux memes 48 cas, ecart a ma table d'au plus 2.5e-04")
ec = sorted(((abs(t[4] - T1[t[:4]]), t) for t in fort), reverse=True)
print("plus grand ecart : %.2e (g = %.0e, m_c = %d, a = %.0f, m0 = %d : %.6f contre %.5f)" % (ec[0][0], ec[0][1][0], ec[0][1][1], ec[0][1][2], ec[0][1][3], ec[0][1][4], T1[ec[0][1][:4]]))
print("ecart median : %.2e ; cas au-dessus de 2.5e-04 : %d ; cas au-dessus de 5e-06 (demi-unite de ma table) : %d" % (ec[24][0], sum(1 for e, t in ec if e > 2.5e-4), sum(1 for e, t in ec if e > 5e-6)))
for g in (5e-4, 1e-3):
    e = [abs(t[4] - T1[t[:4]]) for t in fort if t[0] == g]
    print("   g = %.0e : plus grand %.2e ; moyenne %.2e" % (g, max(e), sum(e) / len(e)))
S2 = all(e <= 2.5e-4 for e, t in ec)
print("S-2 : %s" % ("TENU aux 48 cas" if S2 else "TOMBE"))

print()
print("=== 4. S-3 : aux 24 cas a = 0.5, sous 0.050 aux coupes paires, au-dessus de 0.060 aux coupes impaires")
faible = [t for t in cas if t[2] == 0.5]
pair = [t[4] for t in faible if t[1] % 2 == 0]
impair = [t[4] for t in faible if t[1] % 2 == 1]
print("cas : %d ; coupes paires (%d) : de %.6f a %.6f ; coupes impaires (%d) : de %.6f a %.6f" % (len(faible), len(pair), min(pair), max(pair), len(impair), min(impair), max(impair)))
S3 = len(faible) == 24 and all(v < 0.050 for v in pair) and all(v > 0.060 for v in impair)
print("S-3 : %s" % ("TENU aux 24 cas" if S3 else "TOMBE"))

print()
print("=== 5. clause de tort : un cas fort hors de [0.053, 0.056], ou six valeurs fortes d'une boite etalees")
print("       sur plus de 0.02 fois leur moyenne")
hors2 = [t for t in fort if not (0.053 <= t[4] <= 0.056)]
print("cas forts hors de [0.053, 0.056] : %d" % len(hors2))
pire = 0.0
for g in (5e-4, 1e-3):
    for mc in (10, 11, 12, 13):
        v = [t[4] for t in fort if t[0] == g and t[1] == mc]
        assert len(v) == 6
        et = (max(v) - min(v)) / (sum(v) / 6.0)
        pire = max(pire, et)
        print("   g = %.0e m_c = %d : de %.5f a %.5f ; etalement relatif %.4f" % (g, mc, min(v), max(v), et))
TORT = bool(hors2) or pire > 0.02
print("plus grand etalement : %.4f (limite 0.02) ; TORT REALISE : %s" % (pire, "OUI" if TORT else "NON"))

print()
print("=== 6. hors attendu, sans jugement : ecart a ma table a absorbeur faible, et sa croissance avec g")
for a in (0.5, 1.0, 2.0, 4.0):
    lig = []
    for g in (5e-4, 1e-3):
        e = [t[4] - T1[t[:4]] for t in cas if t[2] == a and t[0] == g]
        lig.append((max(abs(x) for x in e), sum(abs(x) for x in e) / len(e)))
    print("a = %.1f : g = 5e-04 : plus grand %.2e, moyenne %.2e ; g = 1e-03 : plus grand %.2e, moyenne %.2e ; rapport des moyennes %.2f" % (a, lig[0][0], lig[0][1], lig[1][0], lig[1][1], lig[1][1] / lig[0][1]))
print("signe de (2D - chaine) a a = 0.5, par parite de coupe :")
for par, nom in ((0, "paires"), (1, "impaires")):
    e = [t[4] - T1[t[:4]] for t in cas if t[2] == 0.5 and t[1] % 2 == par]
    print("   coupes %s : %d cas ; negatifs %d ; positifs %d ; de %+.2e a %+.2e" % (nom, len(e), sum(1 for x in e if x < 0), sum(1 for x in e if x > 0), min(e), max(e)))
print("partie reelle du pole, Re E / g :")
for a in (0.5, 1.0, 2.0, 4.0):
    r = [abs(t[5]) for t in cas if t[2] == a]
    print("   a = %.1f : plus grand |Re E / g| = %.2e" % (a, max(r)))
print("rapport Re E / g (g = 1e-03) / (g = 5e-04), cas par cas, a = 0.5 :")
rap = []
for t in cas:
    if t[2] == 0.5 and t[0] == 1e-3:
        u = [x for x in cas if x[2] == 0.5 and x[0] == 5e-4 and x[1] == t[1] and x[3] == t[3]][0]
        rap.append(t[5] / u[5])
print("   de %.3f a %.3f (2 = une energie d'ordre g^2)" % (min(rap), max(rap)))
print("poids biorthogonal, 96 cas : de %.4f a %.4f" % (min(t[6] for t in cas), max(t[6] for t in cas)))

print()
print("=== BILAN : S-1 %s ; S-2 %s ; S-3 %s ; tort %s" % ("TENU" if S1 else "TOMBE", "TENU" if S2 else "TOMBE", "TENU" if S3 else "TOMBE", "REALISE" if TORT else "NON REALISE"))
