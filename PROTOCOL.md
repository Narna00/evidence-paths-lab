# Evaluation plan: authorization after policy changes

Draft protocol, 23 October 2026. No experiments under this protocol have been run. Freeze versions, corpus, hypotheses and analysis before held-out evaluation. The earlier graph pilot is documented in `archive-2026-10-21.zip`.

## Unit and ground truth

The experimental unit is an application deployment with a defined permission transition. Requests, repeated exports and multiple observations of one defect are not independent samples. Cluster analysis by application family and report the number of distinct root causes.

Ground truth requires an explicit policy contract, a known configuration and independently checked effects. Historical defects additionally require a documented patch and reproducible pre/post behavior. For seeded defects, keep the mutation record separate from the tool input. Mark ambiguous contracts unresolved rather than assigning the expected outcome from the scanner response.

## Comparisons

| Baseline | Purpose |
|---|---|
| Static role/resource matrix | Measures what a conventional snapshot check misses |
| Full replay after each change | Strong completeness reference within the declared test inventory |
| Dependency-aware sequence generator, initially RESTler where compatible | Controls for benefits already supplied by stateful request generation |
| EvoMaster access-policy checks | Direct comparator for security oracles and generated regression tests |
| Random selection at an equal measured budget | Measures benefit beyond a selection policy without domain information |

Record exact versions, authentication setup, adapters, configuration effort and supported tasks. Report incompatible cases separately; unsupported input is not a detected vulnerability or an algorithm failure. No baseline is considered reproduced until a known positive and negative control succeed.

## Outcomes

Primary outcomes are missed violations after a permission transition, false findings on secure controls, and total cost to reach a correct result. Report inconclusive cases and denominators. Measure HTTP requests, reset time, wall time, CPU/memory where relevant, and operator setup/triage time separately. Coverage is a secondary measure, not proof of security.

For revocation, define the allowed enforcement delay before testing. Sample at declared intervals and report the last successful forbidden effect and the first confirmed denial. The interval bounds the observed window; it is not an exact timestamp. Repeat with old and fresh sessions and verify an unaffected authorized control. Distinguish session revocation from resource permission revocation and token expiry.

## Development and held-out evaluation

Use small seeded applications to debug the harness. Hold out complete application families and policy implementations. Reusing a framework with different object IDs does not create an independent family. Deduplicate historical issues by root cause and patch lineage. Choose sample size after measuring feasibility and expected precision, before confirmatory evaluation.

Use paired comparisons on identical deployments and reset conditions. Report distributions and per-family effects, including negative results. Cluster bootstrap intervals by application family if the corpus supports that analysis. Do not treat every request as an independent trial or choose statistical tests after seeing favorable outcomes. Correct for the declared family of confirmatory comparisons.

## Ablations and failure tests

Remove change tracking, session tracking and dependency-based invalidation separately. Vary delayed enforcement, missed policy-change events, stale observations, cache reset and unavailable positive controls. Test whether conclusions survive application restart and a clean VM restore. Charge replay/reset overhead to the tested method. If invalidation misses a relevant dependency, record the resulting missed violation rather than repairing the graph silently.

Release pinned manifests, reset steps, policy contracts, redacted request/response artifacts, exact invocations, expected effects, exclusions and analysis scripts. Preserve original results. A second operator should reproduce a sample before a claim of portability.
