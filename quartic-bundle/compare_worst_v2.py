#!/usr/bin/env python3
"""Four-class comparison of reproduced .npz archives against embedded references.

Usage:
    python compare_worst.py REF_DIR NEW_DIR [--floor 1e-12] [--exclude F.npz ...]
    python compare_worst.py --selftest

Semantics
---------
Numeric leaves (float/complex arrays or scalars, including inside pickled
dicts/lists/object arrays, reached recursively):
  * both values finite            -> relative |new-ref|/|ref| if |ref| >= floor,
                                     else absolute |new-ref| (machine-floor bucket)
  * both non-finite, same kind    -> equal: nan/nan, +inf/+inf, -inf/-inf
                                     (a reproduced non-finite is a faithful
                                     reproduction, e.g. benign cells of t_blow
                                     grids)
  * anything else                 -> NON-FINITE MISMATCH: finite<->non-finite
                                     (a boundary cell changing verdict, not just
                                     timing), +inf<->-inf, inf<->nan. Counted and
                                     sampled loudly; never folded into a relative
                                     number.
Exact-dtype leaves (int/bool/str/bytes/...) must match exactly.

Per-file classes:
  bit-exact / floor-only / <= 1e-9 / <= 1e-6 / > 1e-6 (!) /
  NON-FINITE MISMATCH (n) / EXACT-DTYPE DIFF / STRUCTURE MISMATCH

History note, kept on purpose: v1 computed d = |new - ref| over whole arrays;
on grids containing inf, inf - inf = nan poisoned d.max(), and `nan > 0` being
False silently preserved exact=True -- a false "bit-exact" on an archive KNOWN
to differ in 5 cells, i.e. the one failure mode a verification tool must not
have. v1 also crashed on dict-bearing archives (kill_k*), so it never reached
file 6 of 15. Both failures are encoded as permanent regressions in --selftest.
A related trap (np.array_equal without equal_nan=True treats nan != nan) is
retired structurally: array_equal is no longer used on inexact dtypes at all.
"""

import argparse
import sys
import tempfile
from pathlib import Path

import numpy as np

FLOOR_DEFAULT = 1e-12
MAX_SAMPLES = 3   # sampled locations printed per file for non-finite mismatches
MAX_PATHS = 3     # exact-dtype / structure paths printed per file


class Report:
    def __init__(self):
        self.exact = True
        self.worst_rel = (0.0, None)   # (value, (path, index, ref, new))
        self.worst_abs = (0.0, None)   # same, for |ref| < floor entries
        self.nf_count = 0
        self.nf_samples = []           # (path, index, ref, new)
        self.exact_dtype_diff = []     # leaf paths
        self.structure = []            # (path, reason)

    def classify(self):
        if self.structure:
            return "STRUCTURE MISMATCH"
        if self.nf_count:
            return f"NON-FINITE MISMATCH ({self.nf_count})"
        if self.exact_dtype_diff:
            return "EXACT-DTYPE DIFF"
        if self.exact:
            return "bit-exact"
        if self.worst_rel[0] == 0.0:
            return "floor-only"
        if self.worst_rel[0] <= 1e-9:
            return "<= 1e-9"
        if self.worst_rel[0] <= 1e-6:
            return "<= 1e-6"
        return "> 1e-6  (!)"


def _fmt_idx(flat, shape):
    if not shape:
        return "(scalar)"
    return str(tuple(int(i) for i in np.unravel_index(flat, shape)))


def _numeric(a, b, path, rep, floor):
    """Finite-aware comparison of two numeric arrays/scalars of equal shape."""
    a0 = np.asarray(a)
    shape = a0.shape
    ctype = np.complex128 if (np.iscomplexobj(a) or np.iscomplexobj(b)) else np.float64
    ar = np.atleast_1d(a0).astype(ctype, copy=False).ravel()
    br = np.atleast_1d(np.asarray(b)).astype(ctype, copy=False).ravel()

    fa, fb = np.isfinite(ar), np.isfinite(br)
    both_fin = fa & fb
    # same-kind non-finites are equal; everything else non-finite is a hard mismatch
    nf_ok = (np.isnan(ar) & np.isnan(br)) | (ar == br)
    hard = ~both_fin & ~nf_ok
    if hard.any():
        rep.exact = False
        rep.nf_count += int(np.count_nonzero(hard))
        room = max(0, MAX_SAMPLES - len(rep.nf_samples))
        for i in np.flatnonzero(hard)[:room]:
            rep.nf_samples.append(
                (path, _fmt_idx(int(i), shape), ar[i].item(), br[i].item()))

    if both_fin.any():
        pos = np.flatnonzero(both_fin)
        af, bf = ar[pos], br[pos]
        d = np.abs(bf - af)
        if d.size and d.max() > 0:
            rep.exact = False
        absa = np.abs(af)
        big = absa >= floor
        if big.any():
            rel = d[big] / absa[big]
            k = int(np.argmax(rel))
            if rel[k] > rep.worst_rel[0]:
                flat = int(pos[np.flatnonzero(big)[k]])
                rep.worst_rel = (float(rel[k]),
                                 (path, _fmt_idx(flat, shape),
                                  af[big][k].item(), bf[big][k].item()))
        small = ~big
        if small.any():
            dd = d[small]
            k = int(np.argmax(dd))
            if dd[k] > rep.worst_abs[0]:
                flat = int(pos[np.flatnonzero(small)[k]])
                rep.worst_abs = (float(dd[k]),
                                 (path, _fmt_idx(flat, shape),
                                  af[small][k].item(), bf[small][k].item()))


def _exact(a, b, path, rep):
    """Exact comparison for non-inexact dtypes (int/bool/str/bytes/...)."""
    if not np.array_equal(np.asarray(a), np.asarray(b)):
        rep.exact = False
        rep.exact_dtype_diff.append(path)


def _walk(a, b, path, rep, floor):
    # unwrap 0-d object arrays produced by np.savez on pickled objects
    if isinstance(a, np.ndarray) and a.dtype == object and a.ndim == 0:
        a = a.item()
    if isinstance(b, np.ndarray) and b.dtype == object and b.ndim == 0:
        b = b.item()

    if isinstance(a, dict) and isinstance(b, dict):
        ka, kb = set(a), set(b)
        if ka != kb:
            rep.exact = False
            rep.structure.append(
                (path, f"dict keys differ (only ref: {sorted(ka - kb, key=repr)}, "
                       f"only new: {sorted(kb - ka, key=repr)})"))
            return
        for k in sorted(a, key=repr):
            _walk(a[k], b[k], f"{path}[{k!r}]", rep, floor)
        return

    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        try:  # homogeneous numeric sequences: compare as arrays
            aa, bb = np.asarray(a), np.asarray(b)
            if aa.dtype != object and bb.dtype != object:
                _walk(aa, bb, path, rep, floor)
                return
        except Exception:
            pass
        if len(a) != len(b):
            rep.exact = False
            rep.structure.append((path, f"length {len(a)} vs {len(b)}"))
            return
        for i, (xa, xb) in enumerate(zip(a, b)):
            _walk(xa, xb, f"{path}[{i}]", rep, floor)
        return

    if isinstance(a, np.ndarray) and isinstance(b, np.ndarray):
        if a.shape != b.shape:
            rep.exact = False
            rep.structure.append((path, f"shape {a.shape} vs {b.shape}"))
            return
        if a.dtype == object or b.dtype == object:
            ar, br = a.ravel(), b.ravel()
            for i in range(ar.size):
                _walk(ar[i], br[i], f"{path}[{_fmt_idx(i, a.shape)}]", rep, floor)
            return
        if np.issubdtype(a.dtype, np.inexact) or np.issubdtype(b.dtype, np.inexact):
            _numeric(a, b, path, rep, floor)
        else:
            _exact(a, b, path, rep)
        return

    # scalar leaves
    if isinstance(a, (bool, np.bool_)) and isinstance(b, (bool, np.bool_)):
        if bool(a) != bool(b):
            rep.exact = False
            rep.exact_dtype_diff.append(path)
        return
    isnum = lambda x: isinstance(x, (int, float, complex, np.number)) \
        and not isinstance(x, (bool, np.bool_))
    if isnum(a) and isnum(b):
        if isinstance(a, (float, complex, np.inexact)) or \
           isinstance(b, (float, complex, np.inexact)):
            _numeric(a, b, path, rep, floor)
        elif int(a) != int(b):
            rep.exact = False
            rep.exact_dtype_diff.append(path)
        return
    if isinstance(a, (str, bytes)) and isinstance(b, (str, bytes)):
        if a != b:
            rep.exact = False
            rep.exact_dtype_diff.append(path)
        return
    if a is None and b is None:
        return
    if type(a) is not type(b):
        rep.exact = False
        rep.structure.append(
            (path, f"type {type(a).__name__} vs {type(b).__name__}"))
        return
    try:
        eq = bool(a == b)
    except Exception:
        eq = False
    if not eq:
        rep.exact = False
        rep.structure.append((path, f"unequal/uncomparable {type(a).__name__}"))


def compare_file(p_ref, p_new, floor):
    rep = Report()
    ref = np.load(p_ref, allow_pickle=True)
    new = np.load(p_new, allow_pickle=True)
    ka, kb = set(ref.files), set(new.files)
    if ka != kb:
        rep.exact = False
        rep.structure.append(
            ("<archive>", f"keys only in ref: {sorted(ka - kb)}, "
                          f"only in new: {sorted(kb - ka)}"))
    for k in sorted(ka & kb):
        _walk(ref[k], new[k], k, rep, floor)
    return rep


def _print_worst(label, worst):
    val, name, det = worst
    print()
    if name is None:
        print(f"{label}: none (no relative deviations above zero)")
        return
    path, idx, va, vb = det
    print(f"{label}: {val:.3e}")
    print(f"  file {name}   key {path}   index {idx}")
    print(f"  ref = {va!r}")
    print(f"  new = {vb!r}")


def run(ref_dir, new_dir, floor, exclude):
    ref_dir, new_dir = Path(ref_dir), Path(new_dir)
    names = sorted(p.name for p in ref_dir.glob("*.npz"))
    if not names:
        sys.exit(f"no .npz found in {ref_dir}")
    rows = []
    print(f"{'file':<34} {'class':<26} {'worst rel':>12} {'worst abs(floor)':>17}")
    for name in names:
        p_new = new_dir / name
        if not p_new.exists():
            print(f"{name:<34} MISSING on new side")
            continue
        rep = compare_file(ref_dir / name, p_new, floor)
        rows.append((name, rep))
        print(f"{name:<34} {rep.classify():<26} "
              f"{rep.worst_rel[0]:>12.2e} {rep.worst_abs[0]:>17.2e}")
    for name, rep in rows:
        for path, idx, va, vb in rep.nf_samples:
            print(f"  [nonfinite] {name}:{path} {idx}: ref={va!r} new={vb!r}")
        for path, why in rep.structure[:MAX_PATHS]:
            print(f"  [structure] {name}:{path}: {why}")
        for path in rep.exact_dtype_diff[:MAX_PATHS]:
            print(f"  [exact-dtype] {name}:{path}")

    def gworst(keep):
        best = (0.0, None, None)
        for name, rep in rows:
            if keep(name) and rep.worst_rel[0] > best[0]:
                best = (rep.worst_rel[0], name, rep.worst_rel[1])
        return best

    _print_worst("Worst relative deviation overall", gworst(lambda n: True))
    if exclude:
        excl = set(exclude)
        _print_worst(f"Worst relative deviation excluding {sorted(excl)}",
                     gworst(lambda n: n not in excl))
    return 0


def selftest():
    """Permanent regressions for the two v1 failures + semantics checks."""
    ok = True
    with tempfile.TemporaryDirectory() as tds:
        td = Path(tds)
        (td / "ref").mkdir()
        (td / "new").mkdir()

        # A) v1 regression 1: inf-laden t_blow-like grid, 5 finite cells
        #    shifted at 3.489e-4 relative. v1 reported bit-exact (NaN poison).
        rng = np.random.default_rng(0)
        base = rng.uniform(100, 400, size=(20, 20))
        grid_ref = base.copy()
        grid_ref[base > 250] = np.inf
        grid_new = grid_ref.copy()
        fin = np.argwhere(np.isfinite(grid_ref))[:5]
        for i, j in fin:
            grid_new[i, j] *= (1 + 3.489e-4)
        np.savez(td / "ref" / "A.npz", tb=grid_ref)
        np.savez(td / "new" / "A.npz", tb=grid_new)

        # B) finite<->non-finite flips must scream, not average
        np.savez(td / "ref" / "B.npz", x=np.array([1.0, np.inf, np.nan, -np.inf]))
        np.savez(td / "new" / "B.npz", x=np.array([1.0, 123.0, 0.0, -np.inf]))

        # C) reproduced non-finites are faithful reproductions
        c = np.array([np.nan, np.inf, -np.inf, 2.0])
        np.savez(td / "ref" / "C.npz", x=c)
        np.savez(td / "new" / "C.npz", x=c.copy())

        # D) v1 regression 2: dict-bearing archive (kill_k*-like); numeric
        #    leaves must get the four-class treatment, not a crash
        import copy
        d_ref = {"gamma": np.array([1.0e-5, 2.0e-4]),
                 "resid": np.array([1e-15, 3e-16]),
                 "meta": {"n": 72, "tag": "k1"}}
        d_new = copy.deepcopy(d_ref)
        d_new["gamma"] = d_ref["gamma"] * (1 + 5e-10)
        d_new["resid"] = d_ref["resid"] + 1e-16
        np.savez(td / "ref" / "D.npz", payload=np.array(d_ref, dtype=object))
        np.savez(td / "new" / "D.npz", payload=np.array(d_new, dtype=object))

        # E) sub-floor-only differences
        np.savez(td / "ref" / "E.npz", x=np.array([0.0, 5e-13]))
        np.savez(td / "new" / "E.npz", x=np.array([1e-15, 6e-13]))

        expected = {
            "A.npz": "> 1e-6  (!)",
            "B.npz": "NON-FINITE MISMATCH (2)",
            "C.npz": "bit-exact",
            "D.npz": "<= 1e-9",
            "E.npz": "floor-only",
        }
        for name, want in expected.items():
            rep = compare_file(td / "ref" / name, td / "new" / name, FLOOR_DEFAULT)
            got = rep.classify()
            status = "PASS" if got == want else "FAIL"
            if got != want:
                ok = False
            extra = f"   worst rel {rep.worst_rel[0]:.3e}" if rep.worst_rel[0] else ""
            print(f"[{status}] {name}: expected {want!r}, got {got!r}{extra}")

        repA = compare_file(td / "ref" / "A.npz", td / "new" / "A.npz", FLOOR_DEFAULT)
        if repA.classify() == "bit-exact":
            ok = False
            print("[FAIL] v1 regression: NaN-poisoned grid reported bit-exact")
        if abs(repA.worst_rel[0] - 3.489e-4) > 1e-7:
            ok = False
            print(f"[FAIL] A worst rel {repA.worst_rel[0]:.6e}, expected 3.489e-4")

    print("selftest:", "OK" if ok else "FAILED")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(
        description="Four-class .npz comparison with finite-aware semantics.")
    ap.add_argument("ref_dir", nargs="?")
    ap.add_argument("new_dir", nargs="?")
    ap.add_argument("--floor", type=float, default=FLOOR_DEFAULT,
                    help="below |ref| < FLOOR, compare absolutely (default 1e-12)")
    ap.add_argument("--exclude", nargs="*", default=[],
                    help="file names excluded from the second worst-deviation "
                         "line (e.g. known boundary-cell archives)")
    ap.add_argument("--selftest", action="store_true",
                    help="run built-in regressions (includes both v1 failures)")
    args = ap.parse_args()
    if args.selftest:
        sys.exit(selftest())
    if not args.ref_dir or not args.new_dir:
        ap.error("REF_DIR and NEW_DIR are required unless --selftest")
    sys.exit(run(args.ref_dir, args.new_dir, args.floor, args.exclude))


if __name__ == "__main__":
    main()
