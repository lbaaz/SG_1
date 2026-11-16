# -*- coding: ascii -*-
"""CONTRE-EPREUVE du releve du gel ter : chaque copie alteree du gel doit faire mordre le releve, au controle vise.
Usage : python3 -I contre_epreuve_releve_gel_ter_machine1_v1.py <gel.md> <releve.py> <dossier du gel> <dossier de la note>
        <clone> <manifeste du lot de la note> <dossier de travail>"""
import sys, os, re, subprocess
GEL, RELEVE, D, DN, CLONE, MAN, TRAVAIL = sys.argv[1:8]
T = open(GEL).read(); os.makedirs(TRAVAIL, exist_ok=True)

def sub(motif, remplacement, n=1):
    def f(t):
        u, k = re.subn(motif, remplacement, t, count=n)
        assert k == n, (motif, k)
        return u
    return f

def chiffre(motif):
    """Augmente d'une unite le dernier chiffre du groupe 1 du motif (9 devient 8)."""
    def f(t):
        m = re.search(motif, t); assert m, motif
        s = m.group(1); c = s[-1]; s2 = s[:-1] + ("8" if c == "9" else str(int(c) + 1))
        return t[:m.start(1)] + s2 + t[m.end(1):]
    return f

def hexa(motif):
    def f(t):
        m = re.search(motif, t); assert m, motif
        s = m.group(1); s2 = ("0" if s[0] != "0" else "1") + s[1:]
        return t[:m.start(1)] + s2 + t[m.end(1):]
    return f

MUT = [
 ("C01 tolerance", sub(r"tau = 0\.05 :", "tau = 0.06 :"), "R07"),
 ("C02 longueur de la reference", sub(r"L = 80   -- REFERENCE", "L = 60   -- REFERENCE"), "R07"),
 ("C03 nombre d'etats juges", chiffre(r"decomposition dense \(1\.33e-12\) : (\d+) etats\. Rien d'autre"), "R05"),
 ("C04 r_c d'un point", chiffre(r"(?m)^  C1\s+\S+\s+\S+\s+(\d+)\s+\d+\s"), "R05"),
 ("C05 etats juges d'un point", chiffre(r"(?m)^  L3\s+\S+\s+\S+\s+\d+\s+(\d+)\s"), "R05"),
 ("C06 boite d'un point", chiffre(r"(?m)^  M2\s+\S+\s+\S+\s+\d+\s+\d+\s+(\d+),"), "R05"),
 ("C07 seuil des neuf dixiemes", chiffre(r"\(au moins\s+(\d+)\)"), "R06"),
 ("C08 compte des ancres", sub(r"ancres, 192 ;", "ancres, 193 ;"), "R06"),
 ("C09 compte de l'etage 2", chiffre(r"etage 2, (\d+) lectures"), "R06"),
 ("C10 canon de la sonde", hexa(r"la sonde \(([0-9a-f]{16})\)"), "R03"),
 ("C11 canon du depot", hexa(r"du depot \(([0-9a-f]{16})\)"), "R03"),
 ("C12 canon du bloc", hexa(r"le bloc du lecteur \(([0-9a-f]{16})\)"), "R03"),
 ("C13 canon de la reference des ancres", hexa(r"reference des ancres \(([0-9a-f]{16})\)"), "R03"),
 ("C14 canon de la note", hexa(r"chaine ([0-9a-f]{16}) \(lot"), "R02"),
 ("C15 citation amputee du garde-fou", sub(r"ni troisieme gel, ni\s+autre echelle, ni autre temoin", "ni troisieme gel, ni autre temoin"), "R04"),
 ("C16 citation amputee de la question", sub(r"que la manche M17 a lue est-elle", "est-elle"), "R04"),
 ("C17 citation alteree du reclassement", sub(r"portant un Gamma depuis juillet", "portant un Gamma depuis aout"), "R04"),
 ("C18 selftest", chiffre(r"(\d+) cas tenus sur"), "R09"),
 ("C19 banc", chiffre(r"(\d+) alterations du code"), "R09"),
 ("C20 pire etalement de la note", chiffre(r"PLATEAU aux six points, pire etalement (\d\.\d+)"), "R10"),
 ("C21 accord de la note", chiffre(r"valeurs de plateau s'accordent a (\d\.\d+)"), "R10"),
 ("C22 reglage : etats QUALIFIES", chiffre(r"(\d+) QUALIFIES, \d+ NON QUALIFIES"), "R11"),
 ("C23 reglage : etalement sous A", chiffre(r"fenetre sous A : mediane (\d\.\d+)"), "R11"),
 ("C24 reglage : etalement sous C", chiffre(r"fenetre sous C : mediane \d\.\d+, plus grand (\d\.\d+)"), "R11"),
 ("C25 reglage : accord D / A", chiffre(r"accord D / A, \|ln\| : mediane \d\.\d+, plus grand (\d\.\d+)"), "R11"),
 ("C26 reglage : consigne (e)", chiffre(r"tau a (\d+) etats sur"), "R11"),
 ("C27 temoin positif", chiffre(r"pire \|ln\(Gamma_pl / Gamma_ref\)\| = (\d\.\d+)"), "R12"),
 ("C28 etage 0 : ecart absolu", chiffre(r"pire ecart absolu (\d\.\d)e"), "R12"),
 ("C29 etalement des largeurs deposees", chiffre(r"s'ecartent de\s+(\d\.\d+) en mediane"), "R13"),
 ("C30 probabilite de A-1", chiffre(r"ESTIMATEUR QUALIFIE : (0\.\d+)"), "R14"),
 ("C31 heure d'ouverture", sub(r"08 h 38", "08 h 39"), "R15"),
 ("C32 pour cent", sub(r"tau ne se desserre pas", "tau (5 %) ne se desserre pas"), "R01"),
 ("C33 caractere non ASCII", sub(r"## 0\. Statut", "## 0. Statut " + chr(233)), "R01"),
 ("C34 ligne trop longue", sub(r"## 1\. Question et perimetre", "## 1. Question et perimetre" + " x" * 45), "R01"),
 ("C35 echelle", sub(r"douze valeurs, un facteur 2048", "treize valeurs, un facteur 2048"), "R07"),
 ("C36 poids au site", sub(r"vaut au moins 0\.5\.", "vaut au moins 0.6."), "R07"),
 ("C37 facteur de norme", sub(r"\(d'un facteur 16/25\)", "(d'un facteur 9/16)"), "R07"),
 ("C38 tolerance de l'etage 0", sub(r"<= 1e-3 G_dep \+ 1e-12", "<= 1e-3 G_dep + 1e-11"), "R07"),
 ("C39 fenetres", sub(r"huit fenetres, de k0 = -3 a k0 = 4", "neuf fenetres, de k0 = -3 a k0 = 5"), "R07"),
 ("C40 piece retiree de la liste", sub(r"  banc_feuille_ter_machine1_v1\.py   ", "  banc_feuille_ter_machine1_v9.py   "), "R15"),
]
r = subprocess.run([sys.executable, "-I", RELEVE, GEL, D, DN, CLONE, MAN], capture_output=True, text=True)
print("gel intact : code %d (attendu 0)" % r.returncode)
ok = r.returncode == 0; mordues = 0
for nom, f, vise in MUT:
    chemin = os.path.join(TRAVAIL, nom.split()[0] + ".md")
    open(chemin, "w", newline="\n", encoding="utf-8").write(f(T))
    r = subprocess.run([sys.executable, "-I", RELEVE, chemin, D, DN, CLONE, MAN], capture_output=True, text=True)
    m = re.search(r"mordent (\[.*\])", r.stdout)
    touche = r.returncode == 1 and m is not None and ("'%s'" % vise) in m.group(1)
    mordues += touche
    print("  %-42s %s  (vise %s ; mordent %s)" % (nom, "MORDUE" if touche else "MANQUEE", vise, m.group(1) if m else r.stdout[-200:] + r.stderr[-300:]))
print("CONTRE-EPREUVE : %d copies alterees, %d mordues au controle vise ; gel intact sans morsure : %s" % (len(MUT), mordues, ok))
sys.exit(0 if (ok and mordues == len(MUT)) else 1)
