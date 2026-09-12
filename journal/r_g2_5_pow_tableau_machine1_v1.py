#!/usr/bin/env python3
# -*- coding: ascii -*-
"""R-G2-5 -- ENUMERATION DES ELEVATIONS A UNE PUISSANCE DANS LES .py DU REGISTRE. machine 1, v1, 12/09/2026.

Objet (geste (2), R-G2-5) : sur machine 1, toute puissance `**` dont la base est un TABLEAU
numpy de flottants passe par le noyau SIMD de la roue Linux de numpy (non correctement
arrondi, ~5 pour cent des appels, biais -1 ulp). Le perimetre ne s'ecrit pas a la main : il
s'ENUMERE. Cette feuille parcourt les .py du registre (clone frais, chemin en argument),
les analyse par l'arbre syntaxique (ast) -- donc ni les `**kwargs`, ni les `**` des chaines
et des commentaires -- et range chaque `**` par une heuristique STATIQUE declaree :

  CONST      base constante numerique (2**k, 10**-6) : scalaire, non expose
  SANS-NUMPY module qui n'importe pas numpy : pow scalaire Python (libm), non expose au noyau
  CARRE      exposant constant 2 (numpy : chemin rapide x*x, correctement arrondi)
  EXPOSABLE  base non constante dans un module numpy, exposant autre que 2 : PEUT etre un
             tableau -- le type n'est pas decidable statiquement, la ligne est A TYPER

Compte attendu declare AVANT de compter : 91 fichiers .py (mesure de machine 2, 12/09) ;
la ligne du coeur du moteur (base g (x1+x2) ** (P-1)) doit apparaitre dans l'enumeration.
Aucun compte attendu de `**` n'existe : l'enumeration EST la mesure. Sont comptes a part les
appels pow()/np.power()/math.pow() et les ufuncs exp/arctan2 (noyaux SIMD eux aussi sur
machine 1). Rien n'est edite (PB-1). Le chemin du registre est un argument, jamais une
constante.
"""
import ast, os, subprocess, sys

if len(sys.argv) != 2:
    sys.exit("usage : r_g2_5_pow_tableau_machine1_v1.py <chemin du clone du registre>")
RAC = os.path.abspath(sys.argv[1])
ATTENDU_PY = 91
OK = []


def chk(n, c, d=''):
    OK.append((n, bool(c)))
    print('  [%s] %-58s %s' % ('PASSE' if c else 'MORD ', n[:58], d))


try:   # clone git : la liste vient de git ls-files ; sinon (lot, repertoire) : parcours du disque
    head = subprocess.check_output(['git', '-C', RAC, 'rev-parse', '--short', 'HEAD'],
                                   stderr=subprocess.DEVNULL).decode().strip()
    fichiers = sorted(f for f in subprocess.check_output(['git', '-C', RAC, 'ls-files']).decode().split('\n')
                      if f.endswith('.py'))
except (subprocess.CalledProcessError, FileNotFoundError):
    head = 'sans git'
    fichiers = sorted(os.path.relpath(os.path.join(d, f), RAC) for d, _, fs in os.walk(RAC)
                      for f in fs if f.endswith('.py'))
print('registre %s, HEAD %s' % (RAC, head))
chk('%d fichiers .py, compte attendu %d' % (len(fichiers), ATTENDU_PY), len(fichiers) == ATTENDU_PY)


def par(s, n):
    """Parenthese une base ou un exposant compose, pour que la ligne se lise sans ambiguite."""
    return s if isinstance(n, (ast.Name, ast.Constant, ast.Attribute, ast.Subscript, ast.Call)) else '(%s)' % s


def genre(n):
    if isinstance(n, ast.Constant):
        return 'CONST'
    return type(n).__name__.upper()


lignes, appels, ufuncs, non_analyses, avec_numpy = [], [], [], [], set()
for f in fichiers:
    src = open(os.path.join(RAC, f), 'rb').read()
    try:
        arbre = ast.parse(src.decode('utf-8', errors='replace'))
    except SyntaxError as e:
        non_analyses.append((f, str(e).split('(')[0].strip()))
        continue
    numpy = any((isinstance(n, ast.Import) and any(a.name.split('.')[0] == 'numpy' for a in n.names))
                or (isinstance(n, ast.ImportFrom) and (n.module or '').split('.')[0] == 'numpy')
                for n in ast.walk(arbre))
    if numpy:
        avec_numpy.add(f)
    for n in ast.walk(arbre):
        if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Pow):
            b, e = n.left, n.right
            if isinstance(b, ast.Constant):
                cl = 'CONST'
            elif not numpy:
                cl = 'SANS-NUMPY'
            elif isinstance(e, ast.Constant) and e.value == 2:
                cl = 'CARRE'
            else:
                cl = 'EXPOSABLE'
            lignes.append((cl, f, n.lineno, par(ast.unparse(b), b), par(ast.unparse(e), e), genre(b), numpy))
        if isinstance(n, ast.Call):
            fn = n.func
            nom = fn.id if isinstance(fn, ast.Name) else (fn.attr if isinstance(fn, ast.Attribute) else '')
            if nom in ('pow', 'power'):
                appels.append((f, n.lineno, ast.unparse(n)[:90], numpy))
            if nom in ('exp', 'arctan2', 'exp2', 'expm1') and isinstance(fn, ast.Attribute):
                ufuncs.append((f, n.lineno, nom, ast.unparse(n)[:90], numpy))

chk('tous les fichiers analyses (0 erreur de syntaxe)', not non_analyses,
    '; '.join('%s : %s' % x for x in non_analyses) or '0 non analyse')
coeur = [l for l in lignes if 'm9_replication' in l[1] and 'x1' in l[3] and 'x2' in l[3]]
chk('la ligne du coeur du moteur est dans l enumeration', bool(coeur),
    ' ; '.join('%s:%d %s ** %s' % (l[1], l[2], l[3], l[4]) for l in coeur) or 'ABSENTE')

par_cl = {}
for l in lignes:
    par_cl.setdefault(l[0], []).append(l)
print('\n1. COMPTE PAR CLASSE (heuristique statique declaree en tete)')
for cl in ('EXPOSABLE', 'CARRE', 'CONST', 'SANS-NUMPY'):
    print('   %-11s %4d' % (cl, len(par_cl.get(cl, []))))
print('   %-11s %4d   (sur %d fichiers, dont %d importent numpy)' % ('TOTAL', len(lignes), len(fichiers),
      len(avec_numpy)))
chk('compte : somme des classes == total', sum(len(v) for v in par_cl.values()) == len(lignes),
    '%d' % len(lignes))

print('\n2. LES EXPOSABLES, UNE PAR LIGNE (fichier:ligne  base ** exposant  [genre de la base])')
fichiers_exp = {}
for cl, f, no, b, e, g, _ in sorted(par_cl.get('EXPOSABLE', []), key=lambda x: (x[1], x[2])):
    fichiers_exp.setdefault(f, 0)
    fichiers_exp[f] += 1
    print('   %s:%d  %s ** %s  [%s]' % (f, no, b[:60], e[:40], g))
print('\n   fichiers portant au moins une EXPOSABLE : %d' % len(fichiers_exp))
for f, k in sorted(fichiers_exp.items(), key=lambda x: (-x[1], x[0])):
    print('   %4d  %s' % (k, f))

print('\n3. APPELS pow() / power() / math.pow()')
for f, no, s, nu in sorted(appels):
    print('   %s:%d  %s  [numpy %s]' % (f, no, s, 'oui' if nu else 'non'))
print('   total : %d' % len(appels))

print('\n4. UFUNCS exp / expm1 / exp2 / arctan2 (noyaux SIMD sur machine 1 eux aussi), modules numpy seulement')
uf = [u for u in ufuncs if u[4]]
for f, no, nom, s, _ in sorted(uf):
    print('   %s:%d  %s  %s' % (f, no, nom, s))
print('   total : %d (et %d dans des modules sans numpy, non listes)' % (len(uf), len(ufuncs) - len(uf)))

print('\n5. LES CARRES ET LES CONSTANTES, PAR FICHIER (comptes seulement)')
for cl in ('CARRE', 'CONST', 'SANS-NUMPY'):
    d = {}
    for l in par_cl.get(cl, []):
        d[l[1]] = d.get(l[1], 0) + 1
    print('   %-11s %s' % (cl, ', '.join('%s:%d' % (os.path.basename(f), k) for f, k in sorted(d.items()))))

n, k = len(OK), sum(1 for _, o in OK if o)
print('\n=====================================================================')
print('BILAN : %d/%d controles PASSENT' % (k, n))
print('R-G2-5 : %d `**` enumeres sur %d .py (HEAD %s) ; EXPOSABLES %d dans %d fichiers ; ce que la'
      % (len(lignes), len(fichiers), head, len(par_cl.get('EXPOSABLE', [])), len(fichiers_exp)))
print('feuille ne decide pas : le TYPE de la base a l execution -- une EXPOSABLE est une ligne A TYPER.')
print('=====================================================================')
