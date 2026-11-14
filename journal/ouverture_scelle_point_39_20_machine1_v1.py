# -*- coding: ascii -*-
# OUVERTURE DU SCELLE : rejeu declare de machine 1 (point 39_20, F1G20, 18 barreaux, dix etats)
# compare a la sortie de la sonde de machine 2 (BOCAL4), tolerance du gel bis (section 12) : 1e-3.
# Arguments : <rejeu scelle de m1> <sonde_etage2.json de m2> <journal>
import sys, json, hashlib, unicodedata
a, b, journal = sys.argv[1:4]
F = open(journal, "w", encoding="ascii", newline="\n")
def dire(s):
    print(s); F.write(s + "\n")
def cB(f):
    t = unicodedata.normalize("NFC", open(f, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
dire("entrants : rejeu scelle m1 %s (attendu 7fb9026014ad0c93) ; sonde_etage2.json m2 %s (attendu c110c6286157b025)" % (cB(a), cB(b)))
assert cB(a) == "7fb9026014ad0c93" and cB(b) == "c110c6286157b025"
A = json.load(open(a))["traj"]
B = json.load(open(b))["points"]["39_20"]["cfg"]["F1G20"]["traj"]
ks = sorted(int(k) for k in A)
assert ks == sorted(int(k) for k in B) == list(range(-5, 13))
pire0 = pire = 0.0
lieu0 = lieu = None
nsuivis = 0
dire("etat 0 (celui que la feuille juge) : k, Gamma m1, Gamma m2, m1/m2 - 1")
for k in ks:
    ea, eb = A[str(k)]["etats"], B[str(k)]["etats"]
    assert len(ea) == len(eb) == 10
    assert A[str(k)]["eta"] == B[str(k)]["eta"]
    for t in range(10):
        assert ea[t]["suivi"] == eb[t]["suivi"], (k, t)
        if not ea[t]["suivi"]:
            continue
        nsuivis += 1
        e = ea[t]["gamma"] / eb[t]["gamma"] - 1.0
        if t == 0:
            dire("  k = %3d  %.10e  %.10e  %+.3e" % (k, ea[t]["gamma"], eb[t]["gamma"], e))
            if abs(e) > pire0:
                pire0, lieu0 = abs(e), k
        if abs(e) > pire:
            pire, lieu = abs(e), (k, t)
dire("etats suivis compares : %d sur %d (memes statuts de suivi des deux cotes)" % (nsuivis, 18 * 10))
dire("pire ecart relatif, etat 0 : %.3e (k = %d) ; tolerance 1e-3 : %s" % (pire0, lieu0, "TIENT" if pire0 <= 1e-3 else "MORD"))
dire("pire ecart relatif, dix etats : %.3e (k = %d, etat %d) ; tolerance 1e-3 : %s" % (pire, lieu[0], lieu[1], "TIENT" if pire <= 1e-3 else "MORD"))
dire("-- FIN ouverture_scelle_point_39_20_machine1_v1 --")
