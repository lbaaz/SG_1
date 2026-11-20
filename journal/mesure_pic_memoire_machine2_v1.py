# -*- coding: ascii -*-
"""Lance une commande et rend le PIC de memoire de travail (PeakWorkingSetSize) de son processus, sous Windows (la sonde de machine 1 ne le mesure que sous Unix). Machine 2, 2026-11-17.
Usage : py -3.11 -P mesure_pic_memoire_machine2_v1.py <commande> [arguments ...]"""
import ctypes
import ctypes.wintypes as wt
import subprocess
import sys
import time


class PMC(ctypes.Structure):
    _fields_ = [('cb', wt.DWORD), ('PageFaultCount', wt.DWORD), ('PeakWorkingSetSize', ctypes.c_size_t), ('WorkingSetSize', ctypes.c_size_t), ('QuotaPeakPagedPoolUsage', ctypes.c_size_t),
                ('QuotaPagedPoolUsage', ctypes.c_size_t), ('QuotaPeakNonPagedPoolUsage', ctypes.c_size_t), ('QuotaNonPagedPoolUsage', ctypes.c_size_t), ('PagefileUsage', ctypes.c_size_t), ('PeakPagefileUsage', ctypes.c_size_t)]


t0 = time.time()
p = subprocess.Popen(sys.argv[1:])
k32 = ctypes.WinDLL('kernel32', use_last_error=True)
k32.OpenProcess.restype = wt.HANDLE
h = k32.OpenProcess(0x1000 | 0x0400, False, p.pid)       # QUERY_LIMITED_INFORMATION | QUERY_INFORMATION
psapi = ctypes.WinDLL('psapi', use_last_error=True)
pic = 0
while p.poll() is None:
    m = PMC(); m.cb = ctypes.sizeof(m)
    if psapi.GetProcessMemoryInfo(h, ctypes.byref(m), m.cb):
        pic = max(pic, m.PeakWorkingSetSize)
    time.sleep(1.0)
m = PMC(); m.cb = ctypes.sizeof(m)
if psapi.GetProcessMemoryInfo(h, ctypes.byref(m), m.cb):
    pic = max(pic, m.PeakWorkingSetSize)
print('code de sortie %d ; duree %.0f s ; pic de memoire de travail du processus %.2f Go' % (p.returncode, time.time() - t0, pic / 2.0 ** 30))
