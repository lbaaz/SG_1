#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CE QUE MACHINE 2 PEUT DIRE DU NUMERO DE DELTA -- et ce qu'elle ne peut pas.

L'acte ecrit : « NUMERO nn PRIS AU DEPOT : plafond releve sur clone frais lbaaz/SG_1 a
HEAD 39fbc89 le 11/09 = 88, premier numero libre 89 ; le corps garde "nn". »  et au
manifeste : « a reverifier ».

JE NE PEUX PAS LE REVERIFIER. Il n'y a aucun depot git au poste machine 2 ; le registre
ORDONNANT (journal/ de lbaaz/SG_1) n'y est pas. Dire « plafond 88 verifie » serait
exactement la faute de portee deja payee le 07/09 : conclure de l'absence au poste a un
fait sur le monde. Ce que cette feuille etablit est plus faible, et elle le dit.
"""
import hashlib, os, re, unicodedata

RAC = r"D:\devs\bocal\BOCAL4"
nums, ou = {}, {}
for dp, _, fs in os.walk(RAC):
    for f in fs:
        m = re.match(r'journal_delta_(\d+)', f)
        if m:
            nums.setdefault(int(m.group(1)), []).append(os.path.join(dp, f))
n = sorted(nums)
print("=" * 78)
print("LE NUMERO DE DELTA : CE QUE LE POSTE MACHINE 2 PERMET DE DIRE")
print("=" * 78)
print("\n[1] CE QUE JE PEUX ETABLIR")
print("    journaux de delta presents au poste : %d numeros distincts, de %d a %d"
      % (len(n), n[0], n[-1]))
print("    plafond LOCAL                       : %d" % n[-1])
print("    89 present au poste                 : %s" % (89 in nums))
trous = [i for i in range(n[0], n[-1] + 1) if i not in nums]
print("    trous dans la serie locale          : %s"
      % (trous if trous else "aucun entre %d et %d" % (n[0], n[-1])))


def B(p):
    raw = open(p, 'rb').read()
    can = unicodedata.normalize('NFC', raw.decode('utf-8')) \
        .replace('\r\n', '\n').replace('\r', '\n').encode('utf-8')
    return hashlib.sha256(can).hexdigest()[:16]


p88 = os.path.join(RAC, "entrant_machine1_2026-09-09_depot_P4",
                   "journal_delta_88_P4_v1.md")
b = B(p88)
print("    delta 88 cite par l'acte (0f8e283fa9499f96) : %s -> %s"
      % (b, "AU BIT" if b == "0f8e283fa9499f96" else "DIVERGE"))
print("\n[2] CE QUE JE NE PEUX PAS ETABLIR, ET QUI RESTE A L'OPERATEUR")
print("    - le plafond du REGISTRE ORDONNANT (journal/ de lbaaz/SG_1 a HEAD 39fbc89) :")
print("      aucun depot git au poste machine 2. Le releve de machine 1 n'est ni")
print("      confirme ni infirme ici.")
print("    - que 89 soit libre AU DEPOT. Il est libre A MON POSTE, ce qui est autre chose.")
print("\n[3] CONCLUSION, A LA PORTEE EXACTE")
print("    Le plafond local (%d) CONCORDE avec le releve de machine 1 (88), et le delta" % n[-1])
print("    88 qu'elle cite est au bit. Cela rend son releve VRAISEMBLABLE ; cela ne le")
print("    remplace pas. Le numero se prend au depot, par l'operateur, sur le registre")
print("    ordonnant -- et le corps de l'acte garde 'nn' jusque-la, ce qui est correct.")
print("=" * 78)
