# -*- coding: ascii -*-
"""MA CHAINE du gel "pont" (seconde partie), mise en module : la chaine a une dimension du texte du gel (sections 4.3 a 4.5 de la premiere partie, section 4 de la seconde),
ecrite DE MON COTE (c'est le code de eligibilite_pont_machine2_v1.py, de la premiere partie, refactorise pour evaluer le lisse a un ecart x QUELCONQUE, ce que la boite fermee demande).
Machine 2, 2026-11-17. Je n'ai PAS lu chaine_pont_bloc_machine1_v1.py ni chaine_cellules_pont_machine1_v1.py avant d'avoir ecrit ce module. Aucune 2D.
Usage CLI : py -3.11 -P chaine_pont_machine2_v1.py <registre clone> <sortie.json> NOM=w2:m:g ...        (w2 en fraction, g tel qu'ecrit, ex. MG3=397/200:3:3.63872e-03)
Module : Chaine(registre).cellule(w2, m, g_texte) -> objet avec .lisse(x, ordre) (mediane des ln rho des 18 variantes a l'ecart x), .table() (les nombres de la section 4)."""
import importlib.util
import json
import math
import sys
from fractions import Fraction as F
import numpy as np

executer = exec
P = 5
VARIANTES = [(a, c, L) for a in (1.0, 2.0, 4.0) for c in (6, 8, 10) for L in (16, 24)]
ECARTS = [0.05, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]


def mediane(v):
    s = sorted(v)
    n = len(s)
    return 0.5 * (s[n // 2 - 1] + s[n // 2]) if n % 2 == 0 else s[n // 2]


class Chaine:
    def __init__(self, registre):
        reg = registre.rstrip('/\\')
        spec = importlib.util.spec_from_file_location("moteur", reg + "/scripts/m17_chaine_v17.py")
        self.M = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.M)
        ns = {"M": self.M}
        for bloc in ("chaine_ordre2_bloc_machine1_v1.py", "ordre3_bloc_machine1_v1.py", "chaine_adaptee_bloc_machine1_v1.py"):
            p = reg + "/scripts/" + bloc
            executer(compile(open(p, encoding="ascii").read(), p, "exec"), ns)
        self.ns = ns

    def cellule(self, w2, m, g_texte):
        return Cellule(self, F(w2), m, g_texte)


def etat_vide(H, i0):
    """valeur propre dont le vecteur propre norme porte le plus grand poids sur le site 0 ; a poids egal, la plus petite partie reelle."""
    val, vec = np.linalg.eig(H)
    poids = np.abs(vec[i0, :]) ** 2 / np.sum(np.abs(vec) ** 2, axis=0)
    k = int(np.lexsort((val.real, -poids))[0])
    return val[k], vec[:, k]


def matrice(tb, t3, a, c, L, ordre):
    d, m_min, m_bord = tb["d"], tb["m_min"], tb["m2_bord"]
    debut = m_bord + c
    Mh = debut + L
    n = Mh - m_min + 1
    H = np.zeros((n, n), dtype=complex)
    for m in range(m_min, Mh + 1):
        i = m - m_min
        H[i, i] = m * d + (tb["S"][m] - tb["S"][0])
        if m > debut:
            H[i, i] += -1j * (a * abs(tb["t"][m]) * ((m - debut) / float(L)) ** 2)
        if m + 1 <= Mh:
            x = tb["t"][m] + (t3["T3"][m] if ordre == 3 else 0.0)
            H[i, i + 1] = x
            H[i + 1, i] = x
        if m + 2 <= Mh:
            H[i, i + 2] = tb["U"][m]
            H[i + 2, i] = tb["U"][m]
        if ordre == 3 and m + 3 <= Mh:
            H[i, i + 3] = t3["W3"][m]
            H[i + 3, i] = t3["W3"][m]
        if ordre == 3 and m + 5 <= Mh:
            H[i, i + 5] = t3["W5"][m]
            H[i + 5, i] = t3["W5"][m]
    return H, -m_min


class Cellule:
    def __init__(self, ch, w2, m, g_texte):
        M, ns = ch.M, ch.ns
        self.w2, self.m, self.g_texte = w2, m, g_texte
        g = float(g_texte)
        self.delta = float(w2) - 2.0
        sites = M.barriere(0, 0, w2, g, True)
        self.m_bord = sites[-1][0] if sites else None
        self.ok = bool(sites) and self.m_bord == m
        if not sites:
            return
        S2 = lambda mm: M.Sigma2_site(M.CANAL[0] * mm, M.CANAL[1] * mm, w2, g)[0]
        self.e_bord = abs(self.m_bord * self.delta + S2(self.m_bord) - S2(0))
        tb = ns["tables_ordre2"](0, 0, w2, g, sites)
        t3 = ns["tables_ordre3"](0, 0, w2, g, tb)
        self.mats = {}
        for (a, c, L) in VARIANTES:
            for o in (2, 3):
                H, i0 = matrice(tb, t3, a, c, L, o)
                E, vec = etat_vide(H, i0)
                self.mats[(a, c, L, o)] = (H, i0, E)

    def ln_rho_variantes(self, x, ordre):
        out = []
        for (a, c, L) in VARIANTES:
            H, i0, E0 = self.mats[(a, c, L, ordre)]
            E = E0.real - x * self.delta
            y = np.linalg.solve(E * np.eye(len(H)) - H, np.eye(len(H))[:, i0])
            rho = -(1.0 / math.pi) * y[i0].imag
            out.append(math.log(rho) if rho > 0 else float('nan'))
        return out

    def lisse(self, x, ordre=3):
        """ln du lisse (mediane des ln rho des 18 variantes) a l'ecart x, SANS |delta| : rho est la densite du site 0 par unite d'energie."""
        v = self.ln_rho_variantes(x, ordre)
        return float('nan') if any(math.isnan(t) for t in v) else mediane(v)

    def table(self):
        """les nombres de la section 4 : ln(rho |delta|) a l'ordre 3 et pas ln rho_2 - ln rho_3 aux 12 ecarts ; etendues du lisse. (G3*, lu en precision etendue, est dans mes details de la premiere partie.)"""
        ld = math.log(abs(self.delta))
        ln3 = [self.lisse(x, 3) + ld for x in ECARTS]
        pas = [self.lisse(x, 2) - self.lisse(x, 3) for x in ECARTS]
        etendue = [max(v) - min(v) for v in (self.ln_rho_variantes(x, 3) for x in ECARTS)]
        return dict(m_bord=self.m_bord, e_bord=self.e_bord, ln_rho3_delta=ln3, pas=pas, etendue_lisse=etendue, etendue_lisse_max=max(etendue), pas_max=max(abs(p) for p in pas))


if __name__ == '__main__':
    reg, sortie = sys.argv[1], sys.argv[2]
    ch = Chaine(reg)
    out = {}
    for spec in sys.argv[3:]:
        nom, rest = spec.split('=')
        w2, m, g = rest.split(':')
        c = ch.cellule(w2, int(m), g)
        t = c.table()
        t.update(w2=w2, m=int(m), g=g, delta=c.delta)
        out[nom] = t
        print('%s : w2 %s m %s g %s  m_bord %s e_bord %.4f  etendue_lisse_max %.4f  pas_max %.4f' % (nom, w2, m, g, t['m_bord'], t['e_bord'], t['etendue_lisse_max'], t['pas_max']), flush=True)
    json.dump(out, open(sortie, 'w', encoding='ascii'), indent=1, sort_keys=True)
