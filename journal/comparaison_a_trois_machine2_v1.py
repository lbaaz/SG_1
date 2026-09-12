#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LA COMPARAISON A TROIS : SES DEUX PRE-VOLS CONTRE LE MIEN -- machine 2, v1, 12/09/2026.

Ce qu'elle demande en 4 : confronter ses deux resultats_temoin.json (noyau / libm) au
MIEN -- la source de R_MOI -- feuille par feuille.

SON ATTENDU, ECRIT AVANT (sa section 4) : mon JSON egal a son run LIBM sur toutes les
feuilles des classes (a) et (b), aux cas durs UCRT pres (mes sept).

L'ISSUE QUI MORD est donc ecrite des deux cotes : si mon JSON s'ecartait de son run libm
sur une feuille de (a), ce ne serait plus le noyau qui separe les postes, et toute la
lecture des sections 3.3 et 5 tomberait. Si au contraire il s'ecartait de son run NOYAU
la ou il egale le libm, c'est la confirmation directe.

Les trois chemins sont des ARGUMENTS.
"""
import json, os, sys

if len(sys.argv) < 4:
    sys.exit("usage : comparaison_a_trois_machine2_v1.py <json noyau m1> <json libm m1> "
             "<json m2>")
NOY = json.load(open(sys.argv[1], encoding="utf-8"))
LIB = json.load(open(sys.argv[2], encoding="utf-8"))
MOI = json.load(open(sys.argv[3], encoding="utf-8"))
OK, MORD = [], []


def sr(v):
    """Rendu ASCII-sur d'une valeur. Les feuilles /meta portent des noms de machine qui
    ne sont pas de l'UTF-8 (le mien en contient un octet Latin-1) : imprimes tels quels,
    ils sortent la PIECE de la convention ASCII/LF, ce qui est arrive au premier passage.
    On ne touche pas a la DONNEE -- on rend l'IMPRESSION sure, et on le dit."""
    return ascii(v)


def chk(q, c, d=''):
    OK.append(bool(c))
    if not c:
        MORD.append((q, d))
    print("  [%s] %-56s %s" % ("OK  " if c else "MORD", q[:56], d))


def feuilles(o, prefixe=""):
    """Enumere toutes les FEUILLES (scalaires) de l'arbre, par leur chemin. Le perimetre
    s'extrait de la STRUCTURE, jamais d'une liste ecrite a la main."""
    if isinstance(o, dict):
        for k in o:
            yield from feuilles(o[k], prefixe + "/" + str(k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from feuilles(v, prefixe + "[%d]" % i)
    else:
        yield prefixe, o


print("=" * 92)
print("LES DEUX PRE-VOLS DE MACHINE 1 (NOYAU / LIBM) CONTRE LE MIEN")
print("=" * 92)

fn, fl, fm = dict(feuilles(NOY)), dict(feuilles(LIB)), dict(feuilles(MOI))
print("      feuilles : son noyau %d | son libm %d | le mien %d" % (len(fn), len(fl), len(fm)))
communes = sorted(set(fn) & set(fl) & set(fm))
print("      communes aux trois : %d" % len(communes))
chk("les trois arbres ont la meme forme sur les feuilles communes",
    len(communes) > 700, "%d" % len(communes))

# --- les feuilles ou SES DEUX runs different : ce sont les feuilles EXPOSEES
exposees = [k for k in communes if fn[k] != fl[k]]
print("\n[1] LES FEUILLES EXPOSEES (ou SES deux runs different)")
print("      %d feuilles" % len(exposees))
par_fam = {}
for k in exposees:
    fam = k.split("/")[1] if k.count("/") > 1 else k
    par_fam[fam] = par_fam.get(fam, 0) + 1
for f, n in sorted(par_fam.items(), key=lambda x: -x[1]):
    print("        %-28s %d" % (f, n))

print("\n[2] SON ATTENDU : MON JSON == SON RUN LIBM SUR LES EXPOSEES")
eg_libm = [k for k in exposees if fm[k] == fl[k]]
eg_noy = [k for k in exposees if fm[k] == fn[k]]
ni = [k for k in exposees if fm[k] != fl[k] and fm[k] != fn[k]]
print("      mon JSON == son LIBM   : %d / %d" % (len(eg_libm), len(exposees)))
print("      mon JSON == son NOYAU  : %d / %d" % (len(eg_noy), len(exposees)))
print("      ni l'un ni l'autre     : %d / %d" % (len(ni), len(exposees)))
chk("SON ATTENDU EST TENU : mon poste est du cote LIBM, pas du cote NOYAU",
    len(eg_libm) > len(eg_noy) and len(eg_libm) > 0,
    "%d contre %d" % (len(eg_libm), len(eg_noy)))
if ni:
    print("      les feuilles ou je ne suis NI l'un NI l'autre (ses cas durs UCRT ?) :")
    for k in ni[:12]:
        print("        %-58s noyau=%s libm=%s moi=%s"
              % (k[:58], sr(fn[k]), sr(fl[k]), sr(fm[k])))
    print("      (%d au total)" % len(ni))

print("\n[3] HORS DES EXPOSEES : LES TROIS COINCIDENT-ILS ?")
non_exp = [k for k in communes if fn[k] == fl[k]]
diverg = [k for k in non_exp if fm[k] != fl[k]]
print("      feuilles non exposees : %d ; ou mon JSON differe quand meme : %d"
      % (len(non_exp), len(diverg)))
for k in diverg[:14]:
    print("        %-58s eux=%s moi=%s" % (k[:58], sr(fl[k]), sr(fm[k])))
chk("hors des exposees, les divergences restent rares et nommables",
    len(diverg) < 0.1 * len(non_exp),
    "%d / %d (%.2f pour cent)" % (len(diverg), len(non_exp),
                                  100 * len(diverg) / max(1, len(non_exp))))

print("\n[4] LES NEUF CELLULES T-2 : e/seuil DES TROIS COTES")
def ratio(o, cel):
    try:
        return o["T2"]["points"][cel]["ratio_seuil"]
    except Exception:
        return None
cels = sorted((NOY.get("T2", {}).get("points", {}) or {}),
              key=lambda c: (int(c.split("|")[0]), float(c.split("|")[1])))
print("      %-9s %14s %14s %14s   %s" % ("cellule", "son noyau", "son libm", "moi",
                                          "moi == ?"))
for c in cels:
    a, b, m = ratio(NOY, c), ratio(LIB, c), ratio(MOI, c)
    if a is None:
        continue
    qui = "LIBM" if m == b else ("NOYAU" if m == a else "ni l'un ni l'autre")
    print("      %-9s %14.8f %14.8f %14.8f   %s" % (c, a, b, m, qui))

print("\n" + "=" * 92)
print("BILAN : %d controles, %d mordent" % (len(OK), len(MORD)))
for q, d in MORD:
    print("   MORD  %s  %s" % (q, d))
print("=" * 92)
