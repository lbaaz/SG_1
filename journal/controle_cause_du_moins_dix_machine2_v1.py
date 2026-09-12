#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LA CAUSE DU '-10' : MA NOTE D'HIER L'IMPUTAIT A L'OUTIL. C'EST FAUX.
machine 2, v1, 12/09/2026.

Ma note bdd00189e68b61dc ecrit : « difflib.unified_diff(n=0) perd la derniere suppression
du fichier ». Machine 1 repond que la cause est un FILTRE DE PREFIXE ('---' ecarte),
qui avale la suppression d'une ligne commencant elle-meme par '--'. Cette feuille tranche
par la mesure, sans croire ni l'une ni l'autre.

Si l'outil perdait la ligne, elle serait absente de sa SORTIE. Si c'est le filtre, elle y
est et c'est le COMPTAGE qui la rate. Les deux hypotheses sont donc separables.
"""
import difflib, os

RAC = r"D:\devs\bocal\BOCAL4"
V2 = os.path.join(RAC, "entrant_machine1_2026-09-11_acte_R4R5_v2", "lot",
                  "journal_delta_nn_R4R5_v2.md")
V3 = os.path.join(RAC, "entrant_machine1_2026-09-11_acte_v3", "lot",
                  "journal_delta_nn_R4R5_v3.md")
A = open(V2, encoding="utf-8").read().splitlines()
B = open(V3, encoding="utf-8").read().splitlines()

print("=" * 84)
print("LA CAUSE DU '-10' -- ERRATUM DE MACHINE 2, MESURE")
print("=" * 84)

u = list(difflib.unified_diff(A, B, n=0, lineterm=''))
entete = u[:2]
corps = u[2:]
print("\nen-tete de la sortie unified : %s" % entete)

par_prefixe = sum(1 for l in u if l.startswith('-') and not l.startswith('---'))
par_position = sum(1 for l in corps if l.startswith('-'))
opcodes = difflib.SequenceMatcher(None, A, B, autojunk=False).get_opcodes()
brut = sum(i2 - i1 for t, i1, i2, j1, j2 in opcodes if t != 'equal')

print("\nsuppressions, opcodes bruts (la reference) : %d" % brut)
print("suppressions, unified compte par POSITION   : %d" % par_position)
print("suppressions, unified compte par PREFIXE    : %d   <-- le compte rendu hier" %
      par_prefixe)

avalees = [l for l in corps if l.startswith('---')]
print("\nligne(s) presente(s) dans la sortie ET ecartee(s) par le filtre de prefixe :")
for l in avalees:
    print("    %r" % l)

print("\nVERDICT :")
h1 = (par_position == brut)
print("  [%s] la sortie de unified_diff CONTIENT toutes les suppressions (%d == %d)"
      % ("OK  " if h1 else "MORD", par_position, brut))
print("  [%s] l'ecart vient donc du COMPTAGE, pas de l'outil (%d != %d)"
      % ("OK  " if par_prefixe != par_position else "MORD", par_prefixe, par_position))
print("  [%s] et il vaut exactement le nombre de lignes avalees (%d)"
      % ("OK  " if par_position - par_prefixe == len(avalees) else "MORD", len(avalees)))
print("\n  => MA NOTE D'HIER EST FAUSSE SUR LA CAUSE. Le compte rendu (-11) etait juste.")
print("  => Le correctif de machine 1 est le bon : exclure l'en-tete PAR POSITION.")
print("  => Et mon propre script de comptage portait le meme filtre : c'est pourquoi")
print("     j'ai reproduit son -10 et conclu que l'outil fautait.")
print("=" * 84)
