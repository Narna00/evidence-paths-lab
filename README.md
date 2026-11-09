# Evidence Paths Lab

Research on evidence validity and test selection in penetration testing, with a focus on authorization after permission changes.

Revocation, role changes and tenant membership updates can leave existing sessions and cached decisions out of step with application policy. Testing these transitions requires more than comparing response codes: the assessment must establish the expected permission, confirm the protected effect and distinguish enforcement from session expiry or service failure.

## Research design

The authorization study examines how policy changes affect the validity of test evidence and the selection of subsequent checks. It will compare static permission matrices, complete replay and selective revalidation across controlled application deployments.

| Document | Contents |
|---|---|
| [Problem formulation](RESEARCH_ASSESSMENT.md) | Policy transitions, evidence dependencies and the test-selection problem |
| [Research proposal](PROPOSAL.md) | Questions, proposed method and experimental scope |
| [Related work](RELATED_WORK.md) | Stateful testing, authorization analysis and reproducible security evaluation |
| [Evaluation protocol](PROTOCOL.md) | Baselines, outcome measures, controls and statistical analysis |
| [Laboratory protocol](LAB_PROTOCOL.md) | Deployment conditions, revocation sequence and evidence schema |

## Graph model and synthetic benchmark

The Python implementation represents candidate capability transitions as a directed graph. It distinguishes confirmed, possible and unresolved reachability using time-bounded validation records. The benchmark compares observation-only rules and three validation policies on synthetic graph families.

Python 3.12 or later; standard library only:

```sh
python -m unittest discover -v
python evidence_paths.py graph.example.json --trust-policy trust.example.json --as-of 2026-10-21T12:00:00Z --recommend
python benchmark.py --seeds 30 --output benchmark-results
```

The example returns exit code 1 for an unresolved query. Exit code 0 indicates a resolved in-model decision; invalid input returns 2. Benchmark output directories are created exclusively.

[MODEL.md](MODEL.md) defines the graph semantics and assumptions. [PILOT.md](PILOT.md) reports the synthetic evaluation. At a maximum validation budget of five, the branch/corridor heuristic resolved 75% of queries and path-first resolved 80%. The experiment uses a complete candidate graph and a perfect unit-cost validation oracle. These results describe graph-query resolution under those conditions.

`pilot-results.zip` contains graph fixtures, truth labels, raw results, summaries and integrity hashes. [Graph experiment documentation](archive-2026-10-21.zip) specifies the associated research design and simulation protocol.

## Reproducibility

`report.py` regenerates the pilot report and SVG after the results archive is extracted into `pilot-results/` and `requirements-figures.txt` is installed. It also rewrites the environment ledger and results archive. Use a separate checkout to preserve the distributed artifacts. `render_plot.cjs` renders the PNG with the optional dependency in `package.json`.

Semantic outcomes reproduce from the same code, fixtures and seeds. Runtime measurements and environment-dependent hashes can vary across machines. Application experiments will use isolated local virtual machines, synthetic identities and independently specified policy contracts.
