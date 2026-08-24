# -*- coding: ascii -*-
"""SONDE E-A -- l'instrument qui manquait sous E34 (Q2). Machine 2.

RAISON D'ETRE. Le delta 80 (90f7e33cc10a4b12) fonde l'erratum E34 sur
l'echelle en eta_c de Gamma_c : 7.24 -> 26.50 -> 33.99 % en montante, la
descente qui converge, l'independance en M a neuf ou dix chiffres. Ces
nombres sont justes -- ils sont dans note_machine2_relecture_script_m17_v1
-- mais **aucun instrument depose ne les produit** : ils ont ete obtenus
par des blocs en ligne, comme ceux que la rectification du 24/08 vient de
nommer D-M17-26 et D-M17-27. La rectification avait couvert le banc et les
deux pre-vols ; elle n'avait pas couvert les cinq notes de RELECTURE, qui
portent elles aussi des tableaux mesures. Ceci repare la part qui fonde un
erratum.

CE QUE CE LOG JOUE :
  1. l'identite de la cible et du gel
  2. l'echelle en eta_c : reference, MONTANTE x2 x4 x8, DESCENDANTE
     /2 /4 /8 /16 /32 -- les deux directions, cote a cote
  3. la regle d'arret du gel (premier pas sous tau_M) et ce qu'elle borne :
     le PAS ; plus le RESIDU estime par le ratio mesure, et Richardson
  4. l'independance en M : M x1, x2, x4 a la meme geometrie
  5. le constat S-E du banc leger, releve de la sortie du script lui-meme
     (et non filtre comme il l'avait ete au pre-vol v2)

CE QUE CE LOG NE JOUE PAS :
  - aucun Gamma_LS : E-B est au banc lourd v2, ce log ne le touche pas
  - aucun verdict, aucun point de grille opposable
  - il ne tranche pas E34 : il rend l'instrument sous ses chiffres

Sortie : sonde_EA_m17_machine2_v1.log
"""
import hashlib
import importlib.util
import os
import subprocess
import sys
import unicodedata
from fractions import Fraction

BASE = os.path.dirname(os.path.abspath(__file__))
CIBLE = os.path.join(BASE, "m17_chaine_v8.py")
LOG = os.path.join(BASE, "sonde_EA_m17_machine2_v1.log")
GEL = "a5e86ca3191fb204"
OUT = []


def p(s=""):
    OUT.append(s)
    print(s, flush=True)


def convB(chemin):
    b = open(chemin, "rb").read()
    return (hashlib.sha256(unicodedata.normalize(
        "NFC", b.decode("utf-8")).encode("utf-8")).hexdigest()[:16], len(b))


e, o = convB(CIBLE)
p("=" * 74)
p("SONDE E-A (fondement de E34 / Q2) -- m17_chaine_v8.py %s  %d o" % (e, o))
p("=" * 74)

sp = importlib.util.spec_from_file_location("m17ea", CIBLE)
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
m.GEL_EMPREINTE = GEL
for k in m.ERRATUMS_CONSIGNES:
    m.ERRATUMS_CONSIGNES[k] = "E9x"
m.LECTURE_OCCUPATIONS = "reelle"

W2 = Fraction(195, 100)
G = m.g_du_point(W2)
S_NOM = 0.70 * m.s_ff(W2, G)
n1_0, n2_0 = m.occupations_graine(S_NOM, W2, "reelle")
p("")
p("1. GEOMETRIE")
p("   w2 = %s ; g = %.12g ; fraction s = 0.70 (Q1) ; s = %.12g"
  % (float(W2), G, S_NOM))
p("   occupations reelles de la graine : n1_0 = %.6f, n2_0 = %.6f"
  % (n1_0, n2_0))
p("   tau_M = %.4g   (regle d'arret du gel : premier pas sous tau_M)"
  % m.TAU_M)
SITES = m.barriere(n1_0, n2_0, W2, G, avec_Sigma2=True)
p("   barriere : %d sites, m2_bord = %d   (5e argument REEL de gamma_chaine :"
  % (len(SITES), SITES[-1][0] if SITES else -1))
p("    c'est la BARRIERE, pas s -- releve du site d'appel l.1128/1159, non"
  " suppose du factice, dont le parametre portait un autre nom)")


def gc(fac_eta, fac_M=4):
    r = m.gamma_chaine(n1_0, n2_0, W2, G, SITES,
                       eta_facteur=fac_eta, M_facteur=fac_M)
    return r["Gamma_c"], r


ref, rref = gc(1.0)
p("")
p("2. ECHELLE EN eta_c -- LES DEUX DIRECTIONS, A M x4")
p("   reference eta = |delta_des|          Gamma_c = %.6e" % ref)
p("   (eta_c rendu par le moteur : %.12g ; M = %d ; recouvrement %.4f)"
  % (rref.get("eta_c"), rref.get("M"), rref.get("recouvrement")))
p("")
p("   MONTANTE (la lettre du gel)          DESCENDANTE (l'erratum)")
mont, desc = [], []
prev = ref
for f_ in (2.0, 4.0, 8.0):
    v, _ = gc(f_)
    mont.append((f_, v, abs(v - prev) / abs(prev)))
    prev = v
prev = ref
for f_ in (0.5, 0.25, 0.125, 0.0625, 0.03125):
    v, _ = gc(f_)
    desc.append((f_, v, abs(v - prev) / abs(prev)))
    prev = v
for i in range(max(len(mont), len(desc))):
    a = ("     x%-3.0f %.6e %6.2f %%" % (mont[i][0], mont[i][1],
                                         100 * mont[i][2])
         if i < len(mont) else " " * 32)
    bb = ""
    if i < len(desc):
        marq = " < tau_M" if desc[i][2] <= m.TAU_M else ""
        bb = ("     /%-3.0f %.6e %6.2f %%%s"
              % (1 / desc[i][0], desc[i][1], 100 * desc[i][2], marq))
    p("%-38s%s" % (a, bb))
p("")
p("   MONTANTE : %s -- %s"
  % (" -> ".join("%.2f %%" % (100 * x[2]) for x in mont),
     "DIVERGE" if all(mont[i + 1][2] > mont[i][2]
                      for i in range(len(mont) - 1)) else "ne diverge pas"))
p("   DESCENDANTE : %s"
  % (" -> ".join("%.2f %%" % (100 * x[2]) for x in desc)))
sous = [i for i, x in enumerate(desc) if x[2] <= m.TAU_M]
if sous:
    i0 = sous[0]
    p("   premier pas sous tau_M : /%d, pas %.2f %%, Gamma_c = %.6e"
      % (1 / desc[i0][0], 100 * desc[i0][2], desc[i0][1]))

p("")
p("3. CE QUE LA REGLE D'ARRET BORNE -- LE PAS, PAS LE RESIDU")
r1 = desc[3][2] / desc[2][2]
r2 = desc[4][2] / desc[3][2]
p("   rapports mesures : %.2f -> %.2f (r = %.2f), %.2f -> %.2f (r = %.2f)"
  % (100 * desc[2][2], 100 * desc[3][2], r1,
     100 * desc[3][2], 100 * desc[4][2], r2))
res = desc[3][2] * r2 / (1 - r2)
p("   residu estime a eta/16 = pas x r/(1-r) = %.2f %% (%s tau_M)"
  % (100 * res, "sous" if res <= m.TAU_M else "au-dessus de"))
rich = 2 * desc[4][1] - desc[3][1]
p("   Richardson (deux derniers pas) : %.6e" % rich)
p("   LES TROIS A CONSIGNER : eta final = |delta_des|/%d ; Gamma_c la"
  % (1 / desc[4][0]))
p("   = %.6e ; Richardson = %.6e ; residu declare = %.2f %%"
  % (desc[4][1], rich, 100 * res))

p("")
p("4. INDEPENDANCE EN M -- LE BORD N'Y EST POUR RIEN")
p("   M facteur   Gamma_c              ecart doublement")
for fM in (1, 2, 4):
    v0, r0 = gc(1.0, fM)
    v2, _ = gc(2.0, fM)
    p("   x%-10d %.9e   %.4f %%   (M = %d)"
      % (fM, v0, 100 * abs(v2 - v0) / abs(v0), r0.get("M")))
vals = [gc(1.0, fM)[0] for fM in (1, 2, 4)]
comm = 0
s0 = "%.12e" % vals[0]
for i, ch in enumerate(s0):
    if all(("%.12e" % v)[i] == ch for v in vals):
        comm += 1
    else:
        break
p("   les trois valeurs partagent %d caracteres de tete : %s"
  % (comm, s0[:comm]))

p("")
p("5. LE CONSTAT S-E DU BANC LEGER, RELEVE DE LA SORTIE DU SCRIPT")
p("   (au pre-vol v2 je n'avais garde que les lignes de COMPTE : la ligne")
p("    qui porte les nombres de E-A n'y figurait pas. Elle figure ici.)")
r = subprocess.run([sys.executable, CIBLE, "--banc-leger"],
                   capture_output=True, text=True, cwd=BASE)
p("   commande : python m17_chaine_v8.py --banc-leger  (code retour %d)"
  % r.returncode)
sortie = (r.stdout or "") + (r.stderr or "")
for l in sortie.split("\n"):
    t = l.rstrip()
    if "S-E constat" in t or "BANC LEGER" in t or "comptes banc" in t:
        for k in range(0, len(t.strip()), 100):
            p("   | %s" % t.strip()[k:k + 100])

with open(LOG, "w", encoding="ascii", newline="\n") as fh:
    fh.write("\n".join(OUT) + "\n")
eL, oL = convB(LOG)
print("")
print("LOG RELU DU DISQUE : %s  %s  %d o" % (os.path.basename(LOG), eL, oL))
