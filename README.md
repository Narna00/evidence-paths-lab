# Evidence Paths Lab

Research prototype for **evidence-aware validation planning in penetration testing**. It represents uncertain candidate transitions, computes confirmed/possible reachability, and prioritizes the next edge to validate. Includes a reproducible synthetic benchmark, five baselines/methods, raw results, paired bootstrap analysis, and a doctoral research protocol.

This is a working research starting point, not a completed PhD, a peer-reviewed result, or an established novel method. The core graph bounds use familiar ideas. The proposed research contribution concerns dependable assessment evidence, realistic validation cost/error models, and reproducible evaluation under correlated and stale tool observations.

## Run

Python 3.12+, standard library only:

```sh
python evidence_paths.py graph.example.json --trust-policy trust.example.json --as-of 2026-10-21T12:00:00Z --recommend
python benchmark.py --seeds 30 --output my-pilot
python -m unittest discover -v
```

The example exits 1 because the cross-owner transition is unvalidated. Two re-exported scanner claims share one origin and do not create proof. The benchmark refuses to overwrite an output directory. Inference exits 0 for a resolved in-model decision, 1 for unknown, and 2 for invalid input. Exit 0 does not mean a system is secure.

For optional figure/report regeneration, extract `pilot-results.zip` into `pilot-results/`, install the optional pinned `requirements-figures.txt`, and run `python report.py`. This regenerates PILOT.md, the SVG, the environment ledger and raw-results archive; it overwrites those generated artifacts. To regenerate the PNG, install the pinned development dependency in `package.json` and run `node render_plot.cjs`. The core benchmark and tests require neither dependency. Keep the original artifact bundle before regenerating, because runtime/environment metadata and resulting archive hashes can change.

## Research package

- [PROPOSAL.md](PROPOSAL.md): research questions, candidate contributions, thesis structure, and milestone gates.
- [RELATED_WORK.md](RELATED_WORK.md): verified seed bibliography, overlap matrix, and literature-review limits.
- [PROTOCOL.md](PROTOCOL.md): hypotheses, baselines, metrics, costs, splits, and reproducibility controls.
- [MODEL.md](MODEL.md): semantics, proof sketch, assumptions, and failure boundaries.
- [LAB_PROTOCOL.md](LAB_PROTOCOL.md): local virtual lab acquisition and transition-validation plan.
- [PILOT.md](PILOT.md): measured synthetic pilot results and limitations, generated from raw outputs.
- `pilot-results.zip`: complete pilot graph fixtures, raw rows, summaries, and hashes.

## Operational interpretation

`reachable` means a path exists using only currently trusted, verified-true transitions. `unreachable_in_model` means no path exists even if all unknown *declared* transitions are possible. `unknown` means current evidence cannot resolve the query. Unknown transitions are never promoted to confirmed by duplicate scanner claims. Time-to-live is explicit and expired/future claims are excluded.

These are graph-model statements. The current directed graph has no conjunction of exploit prerequisites, credential state, temporal action ordering, probability of exploit success, or automatic network discovery. A closed candidate universe and correct trusted validations are essential assumptions. A hostile or incomplete candidate graph can invalidate a real-world safety interpretation. The separate trust policy is an administrator-controlled record, not a signature or proof that validation occurred.

The recommender compares hypothetical perfect true/false resolutions of each relevant unknown edge. Its branch score is a heuristic, not a calibrated probability. Conflicting trusted validators remain unknown and require adjudication. No network operations, exploit execution, or LLM calls occur in the research prototype.

## Local experiments and scope

The user-selected environment is a local virtual lab. The first pilot is fully synthetic and does not claim results for AD, Wi-Fi, or real engagements. See the lab protocol for staged collection with controlled ground truth. A VM-only environment cannot establish RF-layer wireless claims. No human participants, customer evidence, or third-party targets were used.
