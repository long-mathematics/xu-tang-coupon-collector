# Repository instructions

The canonical manuscript is
`paper/extremes_and_moments_in_greedy_coupon_collection.tex`.
Its PDF has the same basename and is intentionally tracked.
The companion audit is `notes/xu_tang_proof_audit.tex` and its matching PDF.
Use stable descriptive filenames without draft, journal, date or version
suffixes.

- Keep author attribution. Do not reintroduce submission-only affiliations,
  postal or email addresses, correspondence or personal identifier metadata.
- Preserve the fixed target multiplicity, fixed bounded batch law,
  positive-mean and uniform-type assumptions. The separate holding extension
  allows its activation probability to depend on the population size.
- Distinguish the greedy keep-one model from keep-all group drawings and
  ordinary single-draw collection. Preserve the explicit prior-art comparison.
- Follow every mathematical change through downstream assertions. Do not
  infer moment convergence from convergence in probability or weak convergence
  without the necessary integrability estimates.
- The paper's proof uses fixed-time concentration and a simultaneous gamma
  clock comparison. The old moving-tail fluctuation program is not a proved
  input and must not be described as a central limit theorem established here.
- Numerical verification supplements the proof and is not a substitute for it.
- Bibliographies are inline; preserve stable labels and cite all entries.
- After changes, run `make verify`, `make pdf` and `make check`, and visually
  inspect changed PDF pages. Commit updated PDFs with the sources.
- Keep verification tools in `scripts/` and review records in `audit/`.
  Exclude LaTeX auxiliaries, caches, backups, private chat transcripts and
  submission archives.
- Use feature branches and pull requests for substantive work after
  initialization; do not rewrite published history.
