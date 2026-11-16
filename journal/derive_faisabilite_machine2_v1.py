# -*- coding: ascii -*-
"""Derive (regle 17 : on n'edite pas la piece de m1) faisabilite_profondeur_jumeau_machine2_v1.py de faisabilite_profondeur_jumeau_machine1_v1.py :
SEULE difference, la mesure de la memoire maximale, qui passe par resource (Linux seulement) ; sous Windows on lit le pic de l'ensemble de travail
du processus (GetProcessMemoryInfo, PeakWorkingSetSize : l'equivalent de ru_maxrss). Chaque remplacement : exactement une fois. Diff ecrit a cote.
Usage : py -3.11 -I derive_faisabilite_machine2_v1.py"""
import difflib
import hashlib
import os
import unicodedata

SRC = r'd:\devs\bocal\BOCAL4\livraison_16f_gel_vide_partie1\ext\x_gel_vide_partie1_regle_tirage\lot_machine1_2026-11-16_gel_vide_partie1_regle_tirage_v1\faisabilite_profondeur_jumeau_machine1_v1.py'
DST = r'd:\devs\bocal\BOCAL4\certif_gel_vide_partie1_machine2\faisabilite_profondeur_jumeau_machine2_v1.py'
raw = open(SRC, 'rb').read()
t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n')
print('canon de la piece de m1 :', hashlib.sha256(t.encode('utf-8')).hexdigest()[:16], '(a0bac3e110a34785 attendu : section 13 du gel)')
if hashlib.sha256(t.encode('utf-8')).hexdigest()[:16] != 'a0bac3e110a34785':
    raise SystemExit('REFUS : canon de la piece de m1')

REMPL = [
    ('import resource\n',
     'import ctypes\nfrom ctypes import wintypes\n\n\ndef pic_memoire_Mo():\n'
     '    """pic de l\'ensemble de travail du processus, en Mo (Windows)."""\n'
     '    class PMC(ctypes.Structure):\n'
     '        _fields_ = [("cb", wintypes.DWORD), ("PageFaultCount", wintypes.DWORD), ("PeakWorkingSetSize", ctypes.c_size_t),\n'
     '                    ("WorkingSetSize", ctypes.c_size_t), ("QuotaPeakPagedPoolUsage", ctypes.c_size_t), ("QuotaPagedPoolUsage", ctypes.c_size_t),\n'
     '                    ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t), ("QuotaNonPagedPoolUsage", ctypes.c_size_t),\n'
     '                    ("PagefileUsage", ctypes.c_size_t), ("PeakPagefileUsage", ctypes.c_size_t)]\n'
     '    c = PMC(); c.cb = ctypes.sizeof(PMC)\n'
     '    k32 = ctypes.WinDLL("kernel32"); k32.GetCurrentProcess.restype = wintypes.HANDLE\n'
     '    ps = ctypes.WinDLL("psapi"); ps.GetProcessMemoryInfo.argtypes = [wintypes.HANDLE, ctypes.POINTER(PMC), wintypes.DWORD]\n'
     '    ps.GetProcessMemoryInfo.restype = wintypes.BOOL\n'
     '    if not ps.GetProcessMemoryInfo(k32.GetCurrentProcess(), ctypes.byref(c), c.cb):\n'
     '        raise RuntimeError("GetProcessMemoryInfo a echoue")\n'
     '    return c.PeakWorkingSetSize / 1048576.0\n'),
    ('round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0, 0)', 'round(pic_memoire_Mo(), 0)'),
]
for ancien, nouveau in REMPL:
    if t.count(ancien) != 1:
        raise SystemExit('REFUS : "%s..." apparait %d fois' % (ancien[:40], t.count(ancien)))
    t = t.replace(ancien, nouveau)
if not all(ord(ch) < 128 for ch in t):
    raise SystemExit('REFUS : octet non ASCII')
orig = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n')
diff = ''.join(difflib.unified_diff(orig.splitlines(True), t.splitlines(True), 'machine1_v1', 'machine2_v1'))
if not all(ord(ch) < 128 for ch in diff):
    raise SystemExit('REFUS : diff non ASCII')
open(DST, 'w', newline='\n').write(t)
open(DST[:-3] + '.diff', 'w', newline='\n').write(diff)
print('ecrit :', DST, ';', len(t), 'octets ;', diff.count('\n'), 'lignes de diff')
