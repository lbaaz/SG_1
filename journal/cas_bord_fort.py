import sys, importlib.util
spec = importlib.util.spec_from_file_location('f', sys.argv[1]); F = importlib.util.module_from_spec(spec); spec.loader.exec_module(F)
eta = {k: 0.05 * 2.0 ** (-k) for k in range(-5, 13)}
f = {k: (2e-10 if k <= -1 else 2e-10 * eta[k] / eta[-1]) for k in eta}
p = F.plateau(f)
print('STATUT', p['statut'], p.get('k0'))
