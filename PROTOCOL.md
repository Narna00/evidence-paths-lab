# Experimental protocol v0.1: exploratory synthetic pilot

This protocol documents the implemented pilot. It was written during development and is **not preregistered**. The results must not be presented as confirmatory. Before a larger study, freeze a dated protocol in an independent registry or immutable repository release and document every deviation.

## Factors and units

- Four graph families: layered, cyclic, bottleneck, and held-out random.
- Thirty deterministic seeds per family; twelve nodes per graph with family-dependent candidate transitions.
- Per-edge synthetic truth probability 0.68. Observation inclusion, corruption, expiry, re-export, and contradictory reports follow the explicit probabilities in `generate`.
- Initial trusted observations are sparse and correct. The simulation validation oracle is perfect and costs one unit per edge.
- Budgets 0, 2, 5, and 10; five methods per graph/budget. Raw output has 120 graphs and 2,400 method rows.
- The graph/seed is the paired experimental unit. Method rows and repeated budgets from the same graph are not independent samples.

The random-family generator is designated held-out for reporting topology sensitivity, but no blind preregistration or independent custodian exists. The developer can inspect all generators. It is not an untouched confirmatory test set, and shared seeds do not make the families statistically independent replications of a real environment.

## Methods

| Method | Evidence use | Validation |
|---|---|---|
| optimistic | Any current positive report makes an edge present; missing is absent | None |
| two_origins | Two distinct positive origin IDs make an edge present | None |
| bounds_random | Trusted evidence bounds | Random unknown edge |
| bounds_path_first | Trusted evidence bounds | First unknown edge on a shortest possible path |
| bounds_gain | Trusted evidence bounds | Hypothetical branch-resolution/corridor heuristic |

The first two are deliberately simple reporting baselines. They use no validation budget and must not be treated as equivalent-cost planning systems. Primary planning comparisons are bounds_gain against bounds_path_first and bounds_random at equal maximum budget. All methods can stop early; report validations actually used and compute time separately.

## Metrics

For each query, record ground-truth reachability, decision, validation trace, actions used, and wall-clock compute time. Report:

- False-safe: `unreachable_in_model` when the true candidate graph is reachable.
- False-confirmed: `reachable` when the true candidate graph is unreachable.
- Abstention: unresolved/unknown query.
- Coverage: fraction of queries receiving a resolved conclusion.
- Declared loss: 10 × false-safe + 3 × false-confirmed + 1 × abstention.
- Validation cost and runtime, separately from loss.

Loss weights are arbitrary declared choices for the pilot, not calibrated business costs. A future sensitivity analysis must vary these weights and include Pareto plots of errors, coverage, and cost. Avoid rewarding an always-unknown method as a perfect detector or equating high coverage with correct conclusions.

## Statistical analysis

For each family and budget, calculate per-seed paired loss differences: bounds_gain minus each planning baseline. Negative differences favor the gain heuristic. Use 1,000 deterministic paired bootstrap resamples of seeds and percentile 95% intervals. The implementation produces **pointwise**, unadjusted intervals; there are multiple comparisons and no confirmatory significance claim. Preserve per-family results rather than pooling everything into one favorable number.

Do not infer practical superiority from a zero error rate under an oracle that guarantees correct validations. That rate tests the containment assumptions and implementation. The substantive question is resolution/cost under realistic conditions. The current pilot does not measure realistic validator error, external tool collection time, disruption, or analyst workload.

## Required next ablations

1. Remove lineage deduplication in an observation baseline and quantify correlation-induced overconfidence; bounds should remain invariant to duplicate reports.
2. Expire 0%, 10%, 30%, and 60% of evidence; measure coverage and required revalidation.
3. Introduce independently controlled false-positive/false-negative validator outcomes; test how guarantees fail and whether repeat/adjudication policies recover them.
4. Assign heterogeneous measured validation costs and prohibited actions; compare cost-sensitive scheduling with strong baselines and an exact solver on small instances.
5. Add and remove candidate edges to quantify the cost of an incomplete universe; never use in-model nonreachability as a real-world guarantee.
6. Add AND prerequisites, identity transitions, and graph-state changes; compare to existing attack-graph reasoning systems before claiming a new contribution.
7. Repeat on actual isolated lab snapshots with independent ground truth. Split by scenario/configuration family, not individual rows or repeated exports.

## Reproducibility and artifacts

Run `python benchmark.py --seeds 30 --output new-results`. Outputs include raw JSONL, full graph/truth fixtures, summary JSON, and hashes. Semantic rows should reproduce from the same source and seed; measured runtime and whole-file hashes containing runtime will vary by machine/run. Preserve source commit, Python/OS version, CPU/memory, invocation, and source-file hashes in the experiment ledger. A hash manifest provides integrity checking only if the manifest itself is trusted.

The summarizer uses population graphs as bootstrap units. If a future design reuses organizational templates or repeated lab images, use clustered resampling at that higher level. Set sample size through a pilot-based power/precision analysis before confirmatory work. Do not use the initial 30-seed choice as a justified sample size for a human or field study.

## Stop and review conditions

Stop a lab scenario if it reaches an unapproved host/network, changes a real identity, captures real secrets, or violates snapshot/rollback assumptions. Mark affected observations invalid and retain the deviation record. A negative or inconclusive result remains in the dataset with its reason. Human participants require the institution's ethics process before recruitment or data collection; no such study has started.
