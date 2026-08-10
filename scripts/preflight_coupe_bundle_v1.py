#!/usr/bin/env python3
# preflight_coupe_bundle_v1.py -- machine 1, 2026-08-10 (PB-3b)
# Pre-vol de la coupe : PROUVE l'assemblage de la serie des deltas
# AVANT git init. Balaye recursivement le repertoire de coupe
# (archive/ comprise), extrait les numeros journal_delta_NN*, et
# ASSERT : chaque numero de 1 a MAX present, zero trou. Les deltas
# multi-versions sont listes (PB-3a : ils entrent TOUS au bundle) --
# le script les rapporte, il n'en exclut aucun.
# Sortie ASCII pur (N-16 : pas d'unicode sous cp1252). Codes retour :
# 0 = serie complete ; 1 = trous ; 2 = usage.
# Usage : python preflight_coupe_bundle_v1.py REPERTOIRE [--max 54]
#         python preflight_coupe_bundle_v1.py --selftest
import re, sys, tempfile
from pathlib import Path

MOTIF = re.compile(r'journal_delta_(\d+)')

def scan(racine):
    trouve = {}
    for p in Path(racine).rglob('*'):
        if p.is_file():
            m = MOTIF.search(p.name)
            if m:
                trouve.setdefault(int(m.group(1)), []).append(p.name)
    return trouve

def verifie(racine, nmax):
    trouve = scan(racine)
    trous = [n for n in range(1, nmax + 1) if n not in trouve]
    multi = {n: sorted(v) for n, v in trouve.items() if len(v) > 1}
    hors = sorted(n for n in trouve if n > nmax)
    print(f"repertoire : {racine}")
    print(f"numeros attendus : 1..{nmax} | presents : {len(trouve)} "
          f"| fichiers delta : {sum(len(v) for v in trouve.values())}")
    for n in sorted(multi):
        print(f"INFO  delta {n} multi-versions ({len(multi[n])}) : "
              + ", ".join(multi[n]) + "  -> TOUS au bundle (PB-3a)")
    if hors:
        print(f"INFO  numeros au-dela de {nmax} (ignores par l'assert) : {hors}")
    if trous:
        print(f"ECHEC serie incomplete -- {len(trous)} trou(s) : {trous}")
        return 1
    print(f"OK    serie complete 1..{nmax}, zero trou")
    return 0

def selftest():
    # Un banc doit TUER : le scenario a trou doit ECHOUER.
    ok = True
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        # scenario A : serie complete 1..6, avec archive/ et multi-versions
        (d / 'archive').mkdir()
        for n in (1, 2, 3):
            (d / 'archive' / f'journal_delta_{n}_x.md').write_text('.')
        for nom in ('journal_delta_4.md', 'journal_delta_5.md',
                    'journal_delta_5_v2.md', 'journal_delta_5_v3.md',
                    'journal_delta_6_run.md'):
            (d / nom).write_text('.')
        rA = verifie(d, 6)
        print(f"selftest A (complete, multi-versions, archive/) : "
              f"retour {rA} attendu 0 -> {'OK' if rA == 0 else 'ECHEC'}")
        ok &= (rA == 0)
        # scenario B : trous (le meme repertoire, exigence 1..9)
        rB = verifie(d, 9)
        print(f"selftest B (trous 7,8,9) : retour {rB} attendu 1 -> "
              f"{'OK' if rB == 1 else 'ECHEC'}")
        ok &= (rB == 1)
    print("SELFTEST : " + ("0 echec" if ok else "ECHEC"))
    return 0 if ok else 1

if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == '--selftest':
        sys.exit(selftest())
    if not a:
        print("usage: preflight_coupe_bundle_v1.py REPERTOIRE [--max N] | --selftest")
        sys.exit(2)
    nmax = 54
    if '--max' in a:
        i = a.index('--max'); nmax = int(a[i + 1]); del a[i:i + 2]
    sys.exit(verifie(a[0], nmax))
