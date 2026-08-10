# Quantum metastability of island-protected ghosts — the interacting Pais–Uhlenbeck oscillator

Reproducibility bundle for the note *"Quantum metastability of classically protected islands in the interacting Pais–Uhlenbeck oscillator: measured rates, a spectral census, and classical threshold laws"* (`note_outreach_EN_2026-07.md`, included in this bundle; PDF to be generated at repo creation).

**What this is.** Classical threshold maps and quantum escape-rate measurements for the quartically self-interacting PU oscillator, x⁗ + (ω₁²+ω₂²)ẍ + ω₁²ω₂²x = g x³, in the Hermitian indefinite realization H = −ω₁n₁ + ω₂n₂ + (g/4)x⁴. Headline results: classically protected islands leak at all amplitudes with truncation-converged rates; no bound island eigenstates exist (spectral census); the ħ-dependence at fixed classical point is a steep power law (~ħ⁴⁻⁵), not e^(−S/ħ), in the deep-quantum window; classical thresholds obey g·s*² ≈ C·(ω₂−ω₁)²(ω₁+ω₂) with C = 0.272 ± 0.035 (C = 1/4 within errors), with an exact cancellation valley at 1:1 and a finite threshold at exact degeneracy. Follow-up runs (tir1/tir2, pre-registered protocol) settle the form of Gamma: no single law — a floor Γ₀ ≈ 1.4×10⁻⁶ (the ground-cluster resonance width) plus a resonant excess; the floor is non-perturbative in g (g² and g⁴ excluded by 2–6 orders; consistent with e^(−c/g), c ≈ 0.37, across nine orders of magnitude). The threshold law is equivalently a detuning-blind amplitude condition g·A₂*²·(ω₁+ω₂) = 4C; the right edge alone gives C = 0.269 ± 0.011 (see spotcheck_reformulation.py).

*Disclosure: this exploration was carried out by an independent researcher in extended collaboration with an AI assistant (Anthropic's Claude); everything below has been re-run in full, twice, by the human author on independent hardware (~14 min per pipeline; agreement ≤5e-10 except five float-sensitive cells at the fractal blow-up boundary of the control systems).*

## Environment

Python ≥ 3.10 with `numpy`, `scipy`, `sympy`, `matplotlib` (see `requirements.txt`). No other dependencies. Deterministic (fixed-step RK4, exact diagonalization); no random seeds.

```
pip install -r requirements.txt
```

**Cache builds** (once, before the quantum steps): `python3 build64.py` (bq_64.npz, ~15 s); `python3 k3_build.py 0.05`, then `0.025`, then `0.0125` (bq72_g*.npz, ~30 s each).

## Reproduction order (indicative runtimes, single node)

| # | script | produces | time |
|---|---|---|---|
| 1 | `pu_test.py` | baseline benign/malicious scan, (1,√2) | ~2 min |
| 2 | `bocal_dictionnaire.py` | linear PU↔PT-dimer dictionary + RWA theorem (sympy) | ~1 min |
| 3 | `bocal_phases.py` | phase maps (note: the (1,3) scan here is stiffness-confounded; superseded by 4) | ~5 min |
| 4 | `bocal_ab.py` | stiffness-matched A/B thresholds → `bocal_ab_data.npz` | ~8 min |
| 5 | `bocal_critere.py` | frequency-shift (repulsion) check vs FFT; K = g·s*² invariant; out-of-sample tests | ~10 min |
| 6 | `bocal_paysage.py` | threshold landscape s*(ω₂) → `bocal_paysage.npz` | ~4 min |
| 7 | `bocal_normale.py` | 1:1 normal form, invisibility-valley verification, K₀ plateau | ~6 min |
| 8 | `bocal_q_build.py`, `bocal_q_run.py`, `bocal_q_salvage.py` | quantum build/diag + truncation control | ~5 min |
| 9 | `bocal_g_build72.py`, `bocal_g_run.py` | leak rates Γ(s), truncation levers N = 44/64/72 → `bocal_gamma.npz` | ~3 min |
| 10 | `kill_k1.py` | leak vs sloshing: long-time plateaus, shell-independence of Γ(n_c) | ~5 min |
| 11 | `k2_run.py` | regularization robustness (hard wall vs soft taper) | ~3 min |
| 12 | `k3_build.py 0.025` / `0.0125`, then `k3_run.py` | ħ-cascade at fixed classical point g·s² = 0.0245 | ~4 min |
| 13 | `kill_k4.py` | state families (shore-cut, squeezed, Fock) + bound-state census | ~4 min |
| 14 | `kill_k6.py` | front-proof uniform rates (adaptive edge + island survival); C refit | ~6 min |
| 15 | `tir1_gammas.py` | exploratory low-s run — kept as the guard trail that caught the box-saturation artifact (its long-window estimator is superseded by 16) → `tir1_partA.npz` | ~3 min |
| 16 | `tir1_partB2.py` | guarded low-s rates (anchors first, two observables, N = 64/72 box invariance) → `tir1_final.npz`, verdict vs pre-registered forms | ~5 min |
| 17 | `tir1_plancher.py` | floor probes: s = 0.15–0.20, Fock ground state, ground-level shore cuts → `tir1_plancher.npz` | ~4 min |
| 18 | `tir2_gcut.py` | coupling cut at fixed states across g = 0.05 / 0.025 / 0.0125 → `tir2_gcut.npz` (figure deferred to 19) | ~3 min |
| 19 | `tir2_fin.py` | g = 0.0125 completion with honest bounds; final synthesis figure `bocal_tirs12.png` → `tir2_final.npz` | ~2 min |
| 20 | `spotcheck_reformulation.py` | per-point test of the detuning-blind threshold form on the landscape → `spotcheck_reformulation.npz` | ~1 s |

Heavy eigensystem caches (`bq_*.npz`, ~215 MB each) are **not** shipped; each regenerates in ~30 s from the build scripts. Small result files (`bocal_*.npz`, `kill_*.npz`, `tir*_*.npz`, `spotcheck_reformulation.npz`) and the seven figures (`figures/`) are included.

## Known pitfalls

- `bocal_phases.py` step 3 confounds stiffness at (1,3); the stiffness-matched protocol (step 4) is authoritative.
- Edge-flux fit windows are invalid for s ≥ 1.3 (front-arrival transient); use the island-survival estimator (`kill_k6.py`).
- The census in `kill_k4.py` is at fixed truncation N = 72; backed by the convergence tests of steps 9–10.

## Caveats (in full in the note)

One main system (ω₁, ω₂) = (1, √2), one main g = 0.05; occupations 1–15 (deep quantum); "escape" operationalized as flux across n = 34 in a truncated basis — only the *outgoing* rate is claimed; C is empirical; the mechanism behind the ħ⁴⁻⁵ law is undecided; the semiclassical regime is out of reach at these sizes (N ≈ 96 would be required).

## License & contact

MIT (see `LICENSE`). Contact: [NAME] — [email]. Questions, objections and kill-tests are exactly what we are asking for.
