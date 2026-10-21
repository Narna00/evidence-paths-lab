# Model and guarantees

## Candidate universe

Let G=(V,E) be a finite directed graph of candidate capability transitions, with start s and goal t. An edge represents one declared transition under fixed lab conditions, not a generic assertion that a CVE exists. Its ground-truth availability is a Boolean for that snapshot. The current implementation supports alternate paths (OR), but not conjunctive prerequisites (AND hyperedges). Restrict claims accordingly.

Each observation carries source identity, origin lineage, observed time, lifetime, a claimed Boolean, and a verified label. The trusted-validator allowlist is separate from graph data. A label alone is insufficient: source identity must also be on that allowlist. Identity authenticity and artifact validity must be established outside this prototype.

At query time, only observations with `observed_at <= as_of < observed_at + ttl` are current. No timestamp-based conflict resolution is used. An edge is TRUE if its current trusted validations all agree TRUE, FALSE if they all agree FALSE, and UNKNOWN if no trusted validation is available or trusted validations conflict. Unverified reports remain leads regardless of their number or source names. Origin lineage is recorded to expose re-export dependence; the bounds do not require independence assumptions.

## Bounds

The lower graph includes only TRUE edges. The upper graph includes TRUE and UNKNOWN edges. If lower reachability holds, report `reachable` and a shortest witness path. If upper reachability fails, report `unreachable_in_model`. Otherwise report `unknown` and one possible path. BFS handles directed cycles through a visited set.

**Conditional soundness statement.** Assume the declared candidate universe includes every transition relevant to s-to-t reachability at the snapshot, TRUE edges really exist, and FALSE edges really do not exist. The true graph contains the lower graph and is contained in the upper graph. Reachability is monotone under edge inclusion. Therefore lower reachability implies true reachability, and lack of upper reachability implies lack of true reachability. This is a standard containment argument, not a novel theorem claimed by the project.

This statement does not survive omitted true edges, incorrect trusted validations, stale state changes within the declared lifetime, mis-modeled prerequisites, or mismatched snapshot conditions. Future work must either detect such violations or report the claim as conditional. TTL is a chosen validity model; it does not make an observation true until expiry.

## Validation recommendation

For an unresolved query, compute the upper-graph s-to-t corridor using forward reachability from s and backward reachability from t. Consider unknown edges on that corridor. Simulate replacing one edge's evidence with a perfect TRUE validation, then with a perfect FALSE validation. Rank candidates by:

1. How many of the two hypothetical branches resolve the reachability query.
2. Sum of reductions in the size of the possible-path corridor.
3. Lexicographic edge ID as a deterministic tie-break.

No probability of either branch is estimated. This is a simple equal-branch resolution heuristic, not Bayes-optimal experimental design or an optimal test sequence. Its straightforward implementation repeatedly runs graph search for each candidate and is intended for small pilot graphs. Expected complexity per recommendation is roughly O(|E| (|V|+|E|)) excluding Python copy/validation overhead.

The simulation's perfect oracle answers an edge's ground truth at unit cost. Real assessments have noisy, inaccessible, costly, and state-changing validations. The prototype's optimistic oracle is an explicit limit; use it to debug semantics and establish an upper-bound setting, not to claim field efficiency. Contradictory trusted validators must be adjudicated, and the current simulator does not model adjudication cost.

## Attack and failure surfaces

| Surface | Current handling | Remaining limitation |
|---|---|---|
| Duplicate tool exports | Origin IDs and duplicate-invariant bounds | Upstream lineage can be false |
| Stale/future reports | Explicit time validity checks | TTL selection is not learned or validated |
| Conflicting verified claims | UNKNOWN | No automated conflict adjudication |
| Forged verified label | Requires separate trusted source allowlist | No source signatures or key management |
| Missing transitions | Candidate-universe assumption disclosed | Cannot certify real-world nonreachability |
| Cyclic paths | BFS visited set | No credential/action-state transitions |
| Independent weak claims | Never promoted to proof | May abstain excessively; measured coverage is essential |
| Misleading node/edge semantics | Lab ground-truth protocol | Human modeling error remains possible |

## What the code tests

Tests enumerate all three-state assignments and consistent Boolean worlds for a small graph, check confirmed-path/cut behavior, handle cycles, reject malformed identifiers/TTL, preserve uncertainty under duplicated reports, reject untrusted verified labels, and check budget compliance. Exhaustive small-graph testing supports implementation correctness; it is not a formal proof of all code behavior or evidence that the method improves real pentests.
