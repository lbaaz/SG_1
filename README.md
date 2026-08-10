# BOCAL campaign -- bundle v1 (Held)

Frozen, versioned, self-contained snapshot of an ongoing two-machine
falsification campaign, cut on 2026-08-10 for external review. This is
a snapshot, not a publication: the campaign continues behind it.

## Where to start

Read `notes/note_outreach_EN_unified_2026-08-10b.md` (the single
outreach note). The prior-art review is in `notes/novelty_review.md`:
it qualifies novelty, not correctness -- its presence frames the
claims. Everything else is evidence: pre-registered gates, primary
run outputs, and the integral two-signatory journal, mistakes
included (they are part of the argument, see the note).

## What this is / is not

- IS: a frozen evidentiary snapshot -- pre-registrations (gels/),
  primary run artifacts (runs/), scripts (scripts/), the integral
  campaign journal and cross-certifications (journal/), and the
  original quartic bundle as re-executed (quartic-bundle/).
- IS NOT: a publication, a campaign closure, or a commitment.
  Any later correction ships as bundle v2 under a new tag; the tag
  `bundle-v1-held` is never amended.

## Verify

    sha256sum -c MANIFEST.sha256

All files are stored with their original bytes; `.gitattributes`
(`* -text`) disables any end-of-line conversion. A small number of
files are intentionally CRLF (documented Windows-side artifacts kept
as-is, with their LF-canonical hashes recorded in the journal).
`journal/CAMPAGNE_etat_complet_2026-08-02.md` is included as of its
date and is superseded by journal deltas 47-60.

## Layout

    notes/           entry point: unified outreach note + novelty review
    gels/            certified pre-registrations (the credibility core)
    scripts/         engine, pilots, per-round scripts, cut preflights
    runs/            primary JSON outputs, run logs, certifications
    journal/         integral deltas 1..60, errata, cross-certifications
    quartic-bundle/  original quartic bundle, unchanged, as re-executed
                     (recursive manifest: quartic-bundle-MANIFEST-*.txt)

Replays on Windows require PYTHONUTF8=1 for scripts with unicode
output.

## Licensing and contact

Text: CC BY 4.0 (LICENSE). Code: MIT (LICENSE-CODE).
Contact: see the outreach note. Full journals beyond this bundle and
any registry lookups: on request.
