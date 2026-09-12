#!/usr/bin/env python3
# -*- coding: ascii -*-
"""GARDE STRUCTURELLE -- LES CONTROLES A CONDITION CONSTANTE. machine 1, v1, 12/09/2026.

Objet : D-ACA-1 (12/09) -- un chk(...) dont la condition est le litteral True ne peut pas
mordre et compte pourtant au bilan. La garde ne cherche pas la chaine ", True," (une aiguille
ecrite dans un texte se trouve elle-meme) : elle parcourt l'ARBRE SYNTAXIQUE de chaque
feuille et compte les appels a chk(...) dont le deuxieme argument est une CONSTANTE (True,
False, nombre, chaine). Elle compte aussi les appels statiques a chk, pour que le compte se
nomme : un appel dans une boucle est UN appel statique et plusieurs lignes au log.
Issue qui mord : au moins un appel a condition constante -> la feuille porte de la prose
comptee comme controle ; son bilan "N/N" se lit "N lignes dont N - k controles".
Usage : garde_chk_constante_machine1_v1.py <feuille.py> [...]. Rien n'est edite (PB-1).
"""
import ast, os, sys

if len(sys.argv) < 2:
    sys.exit('usage : garde_chk_constante_machine1_v1.py <feuille.py> [...]')
total_const = 0
for f in sys.argv[1:]:
    arbre = ast.parse(open(f, 'rb').read().decode('utf-8', errors='replace'))
    appels, consts = 0, []
    for n in ast.walk(arbre):
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'chk'
                and len(n.args) >= 2):
            appels += 1
            if isinstance(n.args[1], ast.Constant):
                consts.append((n.lineno, repr(n.args[1].value), ast.unparse(n.args[0])[:64]))
    total_const += len(consts)
    print('%-48s appels chk %3d   a condition constante %d' % (os.path.basename(f), appels, len(consts)))
    for l, v, t in consts:
        print('      l.%-5d %-6s %s' % (l, v, t))
print('\n[%s] %d appel(s) chk a condition constante sur %d feuille(s)'
      % ('PASSE' if total_const == 0 else 'MORD ', total_const, len(sys.argv) - 1))
