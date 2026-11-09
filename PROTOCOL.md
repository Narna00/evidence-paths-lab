# Authorization-transition evaluation protocol

## Study design

The planned evaluation uses paired comparisons on application deployments with defined permission transitions. Versions, corpus membership, hypotheses, primary outcomes and analysis will be fixed before held-out evaluation. Development runs will be recorded separately.

The experimental unit is an application deployment and permission transition. Repeated requests, exports and observations of one defect are nested measurements. Analysis will account for clustering by application family and identify distinct root causes.

## Ground truth

Each scenario requires an explicit policy contract, a known configuration and independently checked effects. Historical defects additionally require a documented patch and reproducible pre/post behavior. Seeded faults require a mutation record held separately from tool inputs. Ambiguous policy contracts receive an unresolved label.

## Baselines

| Baseline | Purpose |
|---|---|
| Static role/resource matrix | Snapshot-based detection |
| Complete replay after each change | Reference coverage within the test inventory |
| RESTler, for compatible APIs | Dependency-aware request generation |
| EvoMaster access-policy checks | Established security oracles and generated tests |
| Random selection at equal measured cost | Selection without dependency information |

Baseline configuration records will include software version, authentication, adapters, supported tasks and setup effort. Positive and negative controls will establish that each configuration operates as intended. Incompatible cases will be reported separately.

## Outcome measures

Primary outcomes are missed policy violations, false findings on secure controls and cost to reach a correct result. Inconclusive outcomes will be reported with their reasons and denominators. HTTP request counts, reset overhead, wall time, computational resources and operator setup/triage time will be measured separately.

For revocation, the enforcement deadline follows the application contract. Requests will be sampled at declared intervals. The last successful forbidden effect and first confirmed denial bound the observed enforcement window. Existing-session, fresh-session and unaffected-user controls distinguish resource revocation from session revocation, token expiry and service failure.

## Data partition and analysis

Development scenarios will use seeded applications. Held-out evaluation will separate complete application families and policy implementations. Historical cases will be deduplicated by root cause and patch lineage. Sample size will be set from reproduction feasibility and a precision analysis before confirmatory evaluation.

Paired comparisons will use identical deployment and reset conditions. Results will include per-family distributions and clustered uncertainty estimates where the corpus supports them. The analysis plan will specify the primary comparisons and multiplicity correction. Coverage will be reported alongside decision errors and cost.

## Ablations

Change tracking, session tracking and dependency-based invalidation will be removed separately. Further conditions will vary enforcement delay, missed change events, stale observations, cache reset and unavailable positive controls. Application restart and VM restoration will test replay stability. Each method’s measured cost will include its reset and replay overhead.

Dependency omissions will be recorded as detection failures where they cause a missed violation. Exclusion records will identify deployment failures, unsupported operations, ambiguous contracts and unstable reproductions.

## Reproducibility package

The release will include pinned manifests, reset procedures, policy contracts, sanitized request/response artifacts, exact invocations, expected effects, exclusions and analysis scripts. Independent replay will assess reproducibility on a sample of deployments.
