#!/usr/bin/env python3
"""Four-class comparison of reproduced .npz archives against embedded references.

Usage:
    python compare_worst.py REF_DIR NEW_DIR [--floor 1e-12]

For every *.npz present in REF_DIR:
  - entries with |ref| >= floor are compared RELATIVELY: |new - ref| / |ref|
  - entries with |ref| <  floor are compared ABSOLUTELY (machine-floor
    quantities: norm residuals, rates at the representation floor, ...)
Each file is classified: bit-exact / floor-only / <=1e-9 / <=1e-6 / >1e-6.
The script ends with the single worst relative deviation over all files:
file, key, index, reference value, new value.

Non-finite entries (inf in the t_blow grids, NaN for undetected rates) are
compared as PATTERNS (positions and values must match, NaN==NaN); only finite
entries enter the deviation. Dict-valued archives are flattened to
numeric/string leaves before comparison; loading them requires numpy's object
deserialization, which is safe here because every archive compared is produced
locally by this bundle's own scripts (no external input).

Note: if an archive stores raw eigenvectors, BLAS/LAPACK version changes can
flip signs/phases and produce O(1) "deviations" that are pure gauge. Compare
gauge-invariant quantities (spectra, |psi|^2, weights) instead.
"""
import argparse
from pathlib import Path

import numpy as np


def _flatten(prefix, v, out):
    if isinstance(v, np.ndarray) and v.dtype == object and v.ndim == 0:
        v = v.item()
    if isinstance(v, dict):
        for kk, vv in v.items():
            _flatten(f"{prefix}.{kk}", vv, out)
        return
    if isinstance(v, (tuple, list)) and any(isinstance(x, (dict, str, type(None))) for x in v):
        for i, vv in enumerate(v):
            _flatten(f"{prefix}[{i}]", vv, out)
        return
    if v is None:
        out[prefix] = np.array(np.nan)
        return
    if isinstance(v, str):
        out[prefix] = v
        return
    arr = np.asarray(v)
    if arr.dtype.kind in "US":
        out[prefix] = arr
        return
    try:
        out[prefix] = np.asarray(arr, dtype=float)
    except (TypeError, ValueError):
        out[prefix] = np.asarray(arr, dtype=str)


def _leaves(npz):
    out = {}
    for k in npz.files:
        _flatten(k, npz[k], out)
    return out


def compare_file(p_ref: Path, p_new: Path, floor: float) -> dict:
    ref = _leaves(np.load(p_ref, allow_pickle=True))
    new = _leaves(np.load(p_new, allow_pickle=True))
    if set(ref) != set(new):
        return {"status": "KEY MISMATCH",
                "only_ref": sorted(set(ref) - set(new)),
                "only_new": sorted(set(new) - set(ref))}
    worst_rel = (0.0, None)   # (value, (key, index, ref, new))
    worst_abs = (0.0, None)
    nonnum_diff = []
    exact = True
    for k in sorted(ref):
        a, b = ref[k], new[k]
        a_str = isinstance(a, str) or (hasattr(a, "dtype") and a.dtype.kind in "US")
        b_str = isinstance(b, str) or (hasattr(b, "dtype") and b.dtype.kind in "US")
        if a_str or b_str:
            if not np.array_equal(np.asarray(a, dtype=str), np.asarray(b, dtype=str)):
                exact = False
                nonnum_diff.append(k)
            continue
        a = np.atleast_1d(a)
        b = np.atleast_1d(b)
        if a.shape != b.shape:
            return {"status": f"SHAPE MISMATCH ({k}: {a.shape} vs {b.shape})"}
        fa, fb = np.isfinite(a), np.isfinite(b)
        # non-finite entries: positions and values must match (NaN==NaN counts as equal)
        if not (np.array_equal(fa, fb) and np.array_equal(a[~fa], b[~fb], equal_nan=True)):
            exact = False
            nonnum_diff.append(f"{k} (inf/nan pattern)")
            continue
        av, bv = a[fa], b[fb]
        if av.size == 0:
            continue
        d = np.abs(bv - av)
        if d.max() > 0:
            exact = False
        absa = np.abs(av)
        big = absa >= floor
        if big.any():
            rel = np.where(big, d / np.where(big, absa, 1.0), 0.0)
            i = int(np.argmax(rel))
            if rel[i] > worst_rel[0]:
                worst_rel = (float(rel[i]), (k, i, av[i].item(), bv[i].item()))
        if (~big).any():
            ab = np.where(big, 0.0, d)
            j = int(np.argmax(ab))
            if ab[j] > worst_abs[0]:
                worst_abs = (float(ab[j]), (k, j, av[j].item(), bv[j].item()))
    if nonnum_diff:
        cls = "NON-NUMERIC DIFF: " + ", ".join(nonnum_diff)
    elif exact:
        cls = "bit-exact"
    elif worst_rel[0] == 0.0:
        cls = "floor-only"
    elif worst_rel[0] <= 1e-9:
        cls = "<= 1e-9"
    elif worst_rel[0] <= 1e-6:
        cls = "<= 1e-6"
    else:
        cls = "> 1e-6  (!)"
    return {"status": "ok", "class": cls,
            "worst_rel": worst_rel, "worst_abs": worst_abs}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("ref_dir")
    ap.add_argument("new_dir")
    ap.add_argument("--floor", type=float, default=1e-12,
                    help="below |ref| < FLOOR, compare absolutely (default 1e-12)")
    args = ap.parse_args()
    ref_dir, new_dir = Path(args.ref_dir), Path(args.new_dir)

    names = sorted(p.name for p in ref_dir.glob("*.npz"))
    if not names:
        raise SystemExit(f"no .npz found in {ref_dir}")

    g_worst = (0.0, None, None)  # (rel, file, detail)
    print(f"{'file':<40} {'class':<18} {'worst rel':>12} {'worst abs (floor)':>18}")
    for name in names:
        p_new = new_dir / name
        if not p_new.exists():
            print(f"{name:<40} MISSING on new side")
            continue
        r = compare_file(ref_dir / name, p_new, args.floor)
        if r["status"] != "ok":
            print(f"{name:<40} {r['status']}")
            continue
        wr, wa = r["worst_rel"], r["worst_abs"]
        print(f"{name:<40} {r['class']:<18} {wr[0]:>12.2e} {wa[0]:>18.2e}")
        if wr[0] > g_worst[0]:
            g_worst = (wr[0], name, wr[1])

    print()
    if g_worst[1] is None:
        print("Global: everything bit-exact (floor quantities excepted).")
    else:
        rel, name, (k, idx, va, vb) = g_worst
        print(f"Worst relative deviation overall: {rel:.3e}")
        print(f"  file  : {name}")
        print(f"  key   : {k}   flat index {idx}")
        print(f"  ref   : {va!r}")
        print(f"  new   : {vb!r}")


if __name__ == "__main__":
    main()
