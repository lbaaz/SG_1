#!/usr/bin/env python3
# preflight_coupe_bundle_v2.py -- machine 1, 2026-08-10 (P-2')
# Pre-vol de la coupe, version 2 : serie des deltas 1..MAX sans trou,
# avec CORRESPONDANCE DECLAREE pour les numeros portes par des
# fichiers combines (pas de fichier journal_delta_NN propre).
# La table CORRESPONDANCE ci-dessous est AUTOREE machine 1 depuis le
# resume de la note de reception P-1' ; elle doit etre CERTIFIEE par
# machine 2 contre la contre-signature delta 55 v2 (8e4bb337),
# sect. 3.2, AVANT tout usage en coupe. Un numero est repute present
# si (a) un fichier journal_delta_NN* existe, ou (b) sa ligne de
# correspondance trouve au moins un fichier porteur. Sinon : TROU.
# D-1' (arbitrage machine 1) : borne par defaut 55 ; la borne
# effective de la coupe = dernier delta consigne au moment du
# pre-vol, passee en --max et CONSIGNEE au delta de coupe.
# D-2' (arbitrage machine 1) : TOUTES les versions datees des
# fichiers porteurs entrent au bundle (coherence PB-3a) -- le script
# les liste toutes, il n'en exclut aucune.
# Sortie ASCII pur (N-16). Codes retour : 0 serie couverte ;
# 1 trous ; 2 usage.
# Usage : python preflight_coupe_bundle_v2.py REPERTOIRE [--max 55]
#         python preflight_coupe_bundle_v2.py --selftest
import re, sys, tempfile
from pathlib import Path

MOTIF = re.compile(r'journal_delta_(\d+)')

# --- CORRESPONDANCE DECLAREE (a certifier contre 8e4bb337 sect. 3.2)
CORRESPONDANCE = [
    (list(range(1, 18)), r'journal_bundle5',
     "journal maitre bundle 5 (deltas 1..17)"),
    ([18], r'section_?18',
     "fichier section 18"),
    ([19, 20], r'journal_delta_19-20',
     "fichier combine deltas 19-20"),
]

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
    print("CORRESPONDANCE DECLAREE (a certifier contre 8e4bb337 sect. 3.2) :")
    couverts = {}
    for nums, motif, desc in CORRESPONDANCE:
        porteurs = sorted(f for f in fichiers if re.search(motif, f))
        etat = ", ".join(porteurs) if porteurs else "AUCUN PORTEUR"
        print(f"  {min(nums)}..{max(nums)} <- /{motif}/ ({desc}) : {etat}")
        if porteurs:
            for n in nums:
                couverts.setdefault(n, []).extend(porteurs)
    multi = {n: sorted(set(v)) for n, v in directs.items() if len(v) > 1}
    for n in sorted(multi):
        print(f"INFO  delta {n} multi-versions ({len(multi[n])}) : "
              + ", ".join(multi[n]) + "  -> TOUS au bundle (PB-3a)")
    for nums, motif, desc in CORRESPONDANCE:
        porteurs = sorted(f for f in fichiers if re.search(motif, f))
        if len(porteurs) > 1:
            print(f"INFO  porteur multi-versions ({desc}) : "
                  + ", ".join(porteurs) + "  -> TOUTES au bundle (D-2')")
    trous = [n for n in range(1, nmax + 1)
             if n not in directs and n not in couverts]
    presents = len(set(list(directs) + [n for n in couverts if n <= nmax]))
    print(f"numeros couverts : {presents}/{nmax} | fichiers delta directs : "
          f"{sum(len(v) for v in directs.values())}")
    if trous:
        print(f"ECHEC serie non couverte -- {len(trous)} trou(s) : {trous}")
        return 1
    print(f"OK    serie couverte 1..{nmax}, zero trou "
          f"(directs + correspondance declaree)")
    return 0

def selftest():
    ok = True
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        (d / 'journal_bundle5_seance.md').write_text('.')
        (d / 'journal_bundle5_v2.md').write_text('.')
        (d / 'fichier_section18.md').write_text('.')
        (d / 'journal_delta_19-20_E16.md').write_text('.')
        for n in range(21, 26):
            (d / f'journal_delta_{n}_x.md').write_text('.')
        rA = verifie(d, 25)
        print(f"selftest A (couverture complete, porteurs multi-versions) : "
              f"retour {rA} attendu 0 -> {'OK' if rA == 0 else 'ECHEC'}")
        ok &= (rA == 0)
        (d / 'fichier_section18.md').unlink()
        rB = verifie(d, 25)
        print(f"selftest B (porteur du 18 supprime -> trou non couvert) : "
              f"retour {rB} attendu 1 -> {'OK' if rB == 1 else 'ECHEC'}")
        ok &= (rB == 1)
        rC = verifie(d, 27)
        print(f"selftest C (borne au-dela des directs -> trous 26,27) : "
              f"retour {rC} attendu 1 -> {'OK' if rC == 1 else 'ECHEC'}")
        ok &= (rC == 1)
    print("SELFTEST : " + ("0 echec" if ok else "ECHEC"))
    return 0 if ok else 1

if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == '--selftest':
        sys.exit(selftest())
    if not a:
        print("usage: preflight_coupe_bundle_v2.py REPERTOIRE [--max N] | --selftest")
        sys.exit(2)
    nmax = 55
    if '--max' in a:
        i = a.index('--max'); nmax = int(a[i + 1]); del a[i:i + 2]
    sys.exit(verifie(a[0], nmax))
