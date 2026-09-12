#!/usr/bin/env python3
# -*- coding: ascii -*-
"""R-G2-5 -- ENUMERATION DES ELEVATIONS A UNE PUISSANCE DANS LES .py D'UN REPERTOIRE. machine 1, v2, 12/09/2026.

CE QUE LA v2 CHANGE PAR RAPPORT A LA v1 (507911a496a47fd3, lot 25b6f78bdf2ddcff ; PB-1 : la v1
n'est pas editee) -- remarque de forme de machine 2, prise : la regle "le chemin est un
argument, jamais une constante" valait pour le chemin et pas pour le compte. ATTENDU_PY = 91
etait une constante, et le controle de la ligne du moteur jouait toujours ; rejouee sur un
repertoire qui n'est pas le registre, la feuille mordait deux fois pour une raison qui n'est
pas un defaut. Ici le compte attendu (--attendu N) et la presence du moteur (--moteur) sont
des ARGUMENTS : sans --attendu le compte de fichiers est imprime sans controle ; sans --moteur
le controle du moteur est declare NON JOUE. Le log dit ce qu'il ne joue pas.

Objet (geste (2), R-G2-5) : sur machine 1, toute puissance `**` dont la base est un TABLEAU
numpy de flottants passe par le noyau SIMD de la roue Linux de numpy (non correctement
arrondi, ~5 pour cent des appels, biais -1 ulp). Le perimetre ne s'ecrit pas a la main : il
s'ENUMERE. La feuille parcourt les .py du repertoire donne (git ls-files si c'est un clone,
parcours du disque sinon), les analyse par l'arbre syntaxique (ast) -- donc ni les `**kwargs`,
ni les `**` des chaines et des commentaires -- et range chaque `**` par une heuristique
STATIQUE declaree :

  CONST      base constante numerique (2**k, 10**-6) : scalaire, non expose
  SANS-NUMPY module qui n'importe pas numpy : pow scalaire Python (libm), non expose au noyau
  CARRE      exposant constant 2 (numpy : chemin rapide x*x, correctement arrondi)
  EXPOSABLE  base non constante dans un module numpy, exposant autre que 2 : PEUT etre un
             tableau -- le type n'est pas decidable statiquement, la ligne est A TYPER

Aucun compte attendu de `**` n'existe : l'enumeration EST la mesure. Sont comptes a part les
appels pow()/np.power()/math.pow() et les ufuncs exp/expm1/exp2/arctan2 (noyaux SIMD eux
aussi sur machine 1). Rien n'est edite (PB-1).
"""
import argparse, ast, os, subprocess

ap = argparse.ArgumentParser()
ap.add_argument('repertoire', help='clone du registre, ou tout repertoire (un lot)')
ap.add_argument('--attendu', type=int, default=None, help='compte de .py attendu, declare AVANT de compter')
ap.add_argument('--moteur', action='store_true', help='joue le controle : le coeur du moteur est dans l enumeration')
A = ap.parse_args()
RAC = os.path.abspath(A.repertoire)
OK, NON_JOUES = [], []


def chk(n, c, d=''):
    OK.append((n, bool(c)))
    print('  [%s] %-58s %s' % ('PASSE' if c else 'MORD ', n[:58], d))


def non_joue(n, d):
    NON_JOUES.append(n)
    print('  [NON JOUE] %-54s %s' % (n[:54], d))


try:
    head = subprocess.check_output(['git', '-C', RAC, 'rev-parse', '--short', 'HEAD'],
                                   stderr=subprocess.DEVNULL).decode().strip()
    fichiers = sorted(f for f in subprocess.check_output(['git', '-C', RAC, 'ls-files']).decode().split('\n')
                      if f.endswith('.py'))
except (subprocess.CalledProcessError, FileNotFoundError):
    head = 'sans git'
    fichiers = sorted(os.path.relpath(os.path.join(d, f), RAC) for d, _, fs in os.walk(RAC)
                      for f in fs if f.endswith('.py'))
print('repertoire %s, HEAD %s, %d fichiers .py' % (RAC, head, len(fichiers)))
if A.attendu is None:
    non_joue('compte de fichiers attendu', 'aucun --attendu declare ; %d mesures' % len(fichiers))
else:
    chk('%d fichiers .py, compte attendu %d' % (len(fichiers), A.attendu), len(fichiers) == A.attendu)


def par(s, n):
    return s if isinstance(n, (ast.Name, ast.Constant, ast.Attribute, ast.Subscript, ast.Call)) else '(%s)' % s


def genre(n):
    return 'CONST' if isinstance(n, ast.Constant) else type(n).__name__.upper()


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
if A.moteur:
    chk('la ligne du coeur du moteur est dans l enumeration', bool(coeur),
        ' ; '.join('%s:%d %s ** %s' % (l[1], l[2], l[3], l[4]) for l in coeur) or 'ABSENTE')
else:
    non_joue('ligne du coeur du moteur', 'aucun --moteur declare ; %d ligne(s) m9_replication vue(s)' % len(coeur))

par_cl = {}
for l in lignes:
    par_cl.setdefault(l[0], []).append(l)
print('\n1. COMPTE PAR CLASSE (heuristique statique declaree en tete)')
for cl in ('EXPOSABLE', 'CARRE', 'CONST', 'SANS-NUMPY'):
    print('   %-11s %4d' % (cl, len(par_cl.get(cl, []))))
print('   %-11s %4d   (sur %d fichiers, dont %d importent numpy)' % ('TOTAL', len(lignes), len(fichiers), len(avec_numpy)))
chk('compte : somme des classes == total', sum(len(v) for v in par_cl.values()) == len(lignes), '%d' % len(lignes))

print('\n2. LES EXPOSABLES, UNE PAR LIGNE (fichier:ligne  base ** exposant  [genre de la base])')
fichiers_exp = {}
for cl, f, no, b, e, g, _ in sorted(par_cl.get('EXPOSABLE', []), key=lambda x: (x[1], x[2])):
    fichiers_exp[f] = fichiers_exp.get(f, 0) + 1
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
print('BILAN : %d/%d controles PASSENT ; %d non joue(s) : %s' % (k, n, len(NON_JOUES), ', '.join(NON_JOUES) or 'aucun'))
print('R-G2-5 : %d `**` enumeres sur %d .py (HEAD %s) ; EXPOSABLES %d dans %d fichiers ; ce que la'
      % (len(lignes), len(fichiers), head, len(par_cl.get('EXPOSABLE', [])), len(fichiers_exp)))
print('feuille ne decide pas : le TYPE de la base a l execution -- une EXPOSABLE est une ligne A TYPER.')
print('=====================================================================')
