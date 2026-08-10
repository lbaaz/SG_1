#!/usr/bin/env python3
# preflight_coupe_bundle_v2c.py -- machine 1, 2026-08-10 (P-2', version c)
# Revision c du pre-vol v2 (50bfabf7), sur prescriptions C-1..C-3 de la
# certification machine 2 (2c7b42b631059f9f), contre 8e4bb337 sect. 3.2 :
#   C-1  la COUVERTURE 1..17 exige le porteur canonique
#        journal_bundle5_v2026-07-25h (version finale h) ; le motif
#        large /journal_bundle5/ ne sert plus qu'au listing D-2'.
#   C-2  motif 18 ancre sur le nom declare : /journal_delta_section18/.
#   C-3  test negatif neuf : un repertoire portant la SEULE version
#        seance du maitre (sans la h) rend retour 1 -- preuve que C-1
#        mord (un correctif sans test negatif execute n'est pas adopte).
# n-1 et n-2 (notes non bloquantes, "sans changement demande") :
# laisses TELS QUELS -- surface de re-certification minimale.
# D-1' : borne par defaut 55 ; borne effective = dernier delta consigne
# au moment du pre-vol, passee en --max, consignee au delta de coupe.
# D-2' : toutes les versions datees des porteurs au bundle (listees,
# jamais exclues) ; porteur de COUVERTURE = la seule version canonique.
# Sortie ASCII pur (N-16). Codes retour : 0 couvert ; 1 trous ; 2 usage.
# Usage : python preflight_coupe_bundle_v2c.py REPERTOIRE [--max 55]
#         python preflight_coupe_bundle_v2c.py --selftest
import re, sys, tempfile
from pathlib import Path

MOTIF = re.compile(r'journal_delta_(\d+)')

# --- COUVERTURE (certifiee au fond contre 8e4bb337 sect. 3.2 ;
#     motifs C-1/C-2 de la certification 2c7b42b6)
CORRESPONDANCE = [
    (list(range(1, 18)), r'journal_bundle5_v2026-07-25h',
     "journal maitre bundle 5, version finale h -- porteur canonique 1..17"),
    ([18], r'journal_delta_section18',
     "fichier section 18 (nom declare 3.2)"),
    ([19, 20], r'journal_delta_19-20',
     "fichier combine deltas 19-20"),
]
# --- LISTING D-2' seulement (aucune couverture par ce motif)
LISTING_D2 = (r'journal_bundle5',
              "versions du journal maitre -- toutes au bundle (D-2'), "
              "porteuse de couverture : la h seule (C-1)")

def scan(racine):
    directs, fichiers = {}, []
    for p in Path(racine).rglob('*'):
        if p.is_file():
            fichiers.append(p.name)
            m = MOTIF.search(p.name)
            if m:
                directs.setdefault(int(m.group(1)), []).append(p.name)
    return directs, fichiers

def verifie(racine, nmax):
    directs, fichiers = scan(racine)
    print(f"repertoire : {racine} | borne : 1..{nmax} (D-1')")
    print("COUVERTURE (motifs C-1/C-2, certifies contre 8e4bb337 sect. 3.2) :")
    couverts = {}
    for nums, motif, desc in CORRESPONDANCE:
        porteurs = sorted(f for f in fichiers if re.search(motif, f))
        etat = ", ".join(porteurs) if porteurs else "AUCUN PORTEUR"
        print(f"  {min(nums)}..{max(nums)} <- /{motif}/ ({desc}) : {etat}")
        if porteurs:
            for n in nums:
                couverts.setdefault(n, []).extend(porteurs)
    versions = sorted(f for f in fichiers if re.search(LISTING_D2[0], f))
    if len(versions) > 1:
        print(f"INFO  {LISTING_D2[1]} : " + ", ".join(versions))
    multi = {n: sorted(set(v)) for n, v in directs.items() if len(v) > 1}
    for n in sorted(multi):
        print(f"INFO  delta {n} multi-versions ({len(multi[n])}) : "
              + ", ".join(multi[n]) + "  -> TOUS au bundle (PB-3a)")
    trous = [n for n in range(1, nmax + 1)
             if n not in directs and n not in couverts]
    presents = len(set(list(directs) + [n for n in couverts if n <= nmax]))
    print(f"numeros couverts : {presents}/{nmax} | fichiers delta directs : "
          f"{sum(len(v) for v in directs.values())}")
    if trous:
        print(f"ECHEC serie non couverte -- {len(trous)} trou(s) : {trous}")
        return 1
    print(f"OK    serie couverte 1..{nmax}, zero trou "
          f"(directs + couverture C-1/C-2)")
    return 0

def peuple(d, avec_h=True, avec_seance=True):
    if avec_h:
        (d / 'journal_bundle5_v2026-07-25h.md').write_text('.')
    if avec_seance:
        (d / 'journal_bundle5_seance.md').write_text('.')
    (d / 'journal_delta_section18.md').write_text('.')
    (d / 'journal_delta_19-20_E16.md').write_text('.')
    for n in range(21, 26):
        (d / f'journal_delta_{n}_x.md').write_text('.')

def selftest():
    ok = True
    with tempfile.TemporaryDirectory() as td:
        d = Path(td); peuple(d)
        rA = verifie(d, 25)
        print(f"selftest A (h + seance + porteurs ancres) : retour {rA} "
              f"attendu 0 -> {'OK' if rA == 0 else 'ECHEC'}")
        ok &= (rA == 0)
        (d / 'journal_delta_section18.md').unlink()
        rB = verifie(d, 25)
        print(f"selftest B (porteur 18 supprime) : retour {rB} attendu 1 -> "
              f"{'OK' if rB == 1 else 'ECHEC'}")
        ok &= (rB == 1)
    with tempfile.TemporaryDirectory() as td:
        d = Path(td); peuple(d, avec_h=False, avec_seance=True)
        rC = verifie(d, 25)
        print(f"selftest C (C-3 : SEULE version seance, sans la h) : retour "
              f"{rC} attendu 1 -> {'OK' if rC == 1 else 'ECHEC'}")
        ok &= (rC == 1)
    with tempfile.TemporaryDirectory() as td:
        d = Path(td); peuple(d)
        rD = verifie(d, 27)
        print(f"selftest D (borne au-dela des directs) : retour {rD} "
              f"attendu 1 -> {'OK' if rD == 1 else 'ECHEC'}")
        ok &= (rD == 1)
    print("SELFTEST : " + ("0 echec" if ok else "ECHEC"))
    return 0 if ok else 1

if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == '--selftest':
        sys.exit(selftest())
    if not a:
        print("usage: preflight_coupe_bundle_v2c.py REPERTOIRE [--max N] | --selftest")
        sys.exit(2)
    nmax = 55
    if '--max' in a:
        i = a.index('--max'); nmax = int(a[i + 1]); del a[i:i + 2]
    sys.exit(verifie(a[0], nmax))
