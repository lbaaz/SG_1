# BOCAL campaign -- bundle v3 (Held)

Frozen, versioned, self-contained snapshot of an ongoing two-machine
falsification campaign, cut on 2026-08-10 for external review. This is
a snapshot, not a publication: the campaign continues behind it.
Tag `bundle-v2` incorporated the pre-send review fixes (the review
itself ships in `journal/revue_pre_envoi_2026-08-10b_machine2_v1.md`);
tag `bundle-v3` merges the two independently produced "version c"
states of the note into version d (the collision and the merge are
consigned in journal delta 64 and the campaign journal); the original
cut remains frozen under tag `bundle-v1-held` and is never amended.

## Where to start

Read `notes/note_outreach_EN_unified_2026-08-10d.md` (the single
outreach note, version d; version b is the state frozen at
`bundle-v1-held`, and the machine-1 "version c" state consigned by
journal delta 64 is kept under `journal/`). The prior-art review is in
`notes/novelty_review.md`: it qualifies novelty, not correctness --
its presence frames the claims. Everything else is evidence:
pre-registered gates, primary run outputs, and the two-signatory
campaign journal, mistakes included (they are part of the argument,
see the note).

## What this is / is not

- IS: a frozen evidentiary snapshot -- pre-registrations (gels/),
  primary run artifacts (runs/), scripts (scripts/), the campaign
  journal and cross-certifications (journal/), and the original
  quartic bundle as re-executed (quartic-bundle/).
- IS NOT: a publication, a campaign closure, or a commitment.
  Corrections ship as new tags (v1 -> v2 -> ...); no tag is ever
  amended.

## Verify

    sha256sum -c MANIFEST.sha256

All files are stored with their original bytes; `.gitattributes`
(`* -text`) disables any end-of-line conversion. A small number of
files are intentionally CRLF (documented Windows-side artifacts kept
as-is, with their LF-canonical hashes recorded in the journal).

The quartic bundle has its own recursive manifest,
`quartic-bundle-MANIFEST-2026-08-10.sha256.txt` (paths relative to
`quartic-bundle/`): verify it from inside that directory --

    cd quartic-bundle && sha256sum -c ../quartic-bundle-MANIFEST-2026-08-10.sha256.txt

## Supersession and known caveats

- `quartic-bundle/README.md` (English; the original French is kept as `README_FR.md`) predates the unified note; where the
  two differ, the note supersedes it -- in particular the note
  withdraws "truncation-converged rates" below mid-island (note
  §5(b)(i)) and its "PDF to be generated" line is stale. The quartic
  bundle is shipped unchanged on purpose (it is the re-executed
  artifact of provenance contract A).
- The quartic-bundle build scripts (`build64.py`,
  `bocal_g_build72.py`, `k3_build.py`) hard-code D = 1.0, exact at
  the main system (1, sqrt2) only; re-users at other frequency
  ratios must generalize D = omega2^2 - omega1^2.
- `journal/CAMPAGNE_etat_complet_2026-08-02.md` is included as of
  its date and is superseded by journal deltas 47-60.
- `journal/` and `gels/` are written in French (the campaign's
  working language); the notes and this README are in English.

## Layout

    notes/           entry point: unified outreach note (e) + novelty review
    gels/            certified pre-registrations (the credibility core)
    scripts/         engine, pilots, per-round measurement scripts, cut preflights
    runs/            primary JSON outputs, run logs, archived sweep logs, certifications
    journal/         campaign deltas 1..60, 64-65 as held by machine 2
                     (61-63 in transfer), errata, cross-certifications,
                     pre-send review (earlier master-journal states
                     through §17: on request)
    quartic-bundle/  original quartic bundle, unchanged, as re-executed
                     (recursive manifest: quartic-bundle-MANIFEST-*.txt)

Replays on Windows require PYTHONUTF8=1 for scripts with unicode
output.

## Licensing and contact

Text: CC BY 4.0 (LICENSE). Code: MIT (LICENSE-CODE).
Contact: via GitHub (@lbaaz). Full journals beyond this bundle,
the reimplementation codebase, and any registry lookups: on request.
