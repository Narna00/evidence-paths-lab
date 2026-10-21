# Doctoral research proposal: evidence-aware validation planning for penetration testing

## Working research question

How should a penetration tester choose the next validation action and state a reachability conclusion when assessment evidence is incomplete, stale, correlated, contradictory, or wrong?

The motivating failure is operational: a missing export is treated as absent access, several dashboards repeat one scanner result as independent support, or a historical configuration is mistaken for current enforcement. The intended unit of analysis is a scoped transition and the evidence required to validate it. The first prototype deliberately separates a reported condition from a verified capability.

This is a candidate research direction that fits a local virtual lab, not a claim of thesis acceptance or publication readiness. ResearchGate presence and search indexing are distribution outcomes; the scientific milestones are a defensible contribution, rigorous evaluation, reproducible artifacts, and review by the relevant research community.

## Candidate thesis contributions

1. **Evidence semantics for assessment claims.** A transition evidence model that tracks lineage, validity conditions, contradictions, and proof obligations. Extend the initial directed-graph prototype to AND/OR prerequisites, identity states, and explicit snapshot transitions. Identify the conditions under which conclusions are sound, and when the system must abstain.
2. **Validation planning under practical constraints.** Choose the next permitted action given cost, disruption budget, validator error, and uncertain outcomes. Compare simple heuristics, risk-sensitive planning, and formal/optimization approaches. Do not presuppose that the supplied heuristic wins.
3. **A controlled assessment benchmark.** Create locally reproducible scenarios with independent ground truth, known observation corruption, and tool-source lineage. Evaluate over different topologies and configurations with held-out scenario families. Release acquisition/provenance records, not just a final CSV.
4. **Analyst-facing evaluation.** Test whether evidence-aware explanations improve conclusion quality and test selection compared with conventional reports. A human study is a later phase requiring institutional ethics review, consent, a power analysis, and a study design agreed before recruitment. It is not part of the current pilot.

None of these contributions is established merely by implementing a tool. The nearest prior work must be reproduced and the differentiating claim narrowed after a systematic search. A negative result about a planning heuristic can still be useful if it establishes a reproducible limitation and a well-supported alternative.

## Questions and falsifiable outcomes

| Question | Measurable outcome | Falsification |
|---|---|---|
| RQ1: Do evidence bounds prevent unsafe conclusions under specified observation errors? | False-safe and false-confirmed rates with coverage, condition violations, and exact guarantees | A claim of soundness outside its assumptions, or errors when trusted evidence is correct |
| RQ2: Does targeted validation resolve queries with fewer actions than strong simple baselines? | Paired loss/coverage curves at fixed cost and time budgets | No improvement over path-first or random validation across held-out families |
| RQ3: How do source dependence, staleness, and validator error affect decisions? | Factorial corruption experiments and failure boundaries | Benefits vanish under plausible dependence/error assumptions |
| RQ4: Does the explanation help a professional reviewer? | Blinded conclusion accuracy, validation choices, time, and uncertainty reporting | No improvement, worse calibration, or gains explained by extra information rather than the method |

## Scope of the current artifact

Implemented now: finite directed-graph inference, explicit trusted validation, time validity, contradiction-preserving uncertainty, shortest path witnesses, three validation policies, two observation-only baselines, four synthetic topology families, reproducible seeds, paired bootstrap summaries, raw datasets, a local web fixture in the companion workbench, and regression tests.

Not implemented: general attack-graph generation, AD exploit execution, RF experiments, cryptographic source authentication, Bayesian inference, a real-world cost model, noisy validator simulation, temporal attacker state, an AND/OR solver, a human study, or a systematic literature review. These are research tasks, not hidden capabilities.

## Local-lab resource model

Begin with the included loopback fixture and small graph experiments on the current workstation. Add a Windows evaluation DC/member environment only if legitimate images and sufficient memory/storage are available. Use snapshots and an isolated virtual network; do not bridge the lab to production. Establish the feasible VM count by measurement before buying hardware. Wireless conclusions remain outside the empirical claim until owned radio hardware and appropriate RF isolation exist.

Ground truth should come from a configuration ledger plus an independent controlled validation, not from the same scanner used as input. Archive image identifiers, software versions, configuration changes, acquisition scripts, and timestamps. The budget model must distinguish an offline configuration query, an authenticated check, and a disruptive exploit; a unit-cost oracle cannot justify field claims.

## Milestones and decision gates

| Phase | Work | Exit gate |
|---|---|---|
| Weeks 1–2 | Seed literature matrix, reproduce simple bounds and baselines, document threat model | A supervisor can identify the precise difference from the closest work |
| Weeks 3–6 | Expand controlled web scenarios and evidence acquisition; independent ground truth | Every edge label is reproducible with raw artifacts and declared conditions |
| Weeks 7–10 | Add cost/error models and preregister confirmatory comparisons | Protocol frozen before held-out evaluation |
| Weeks 11–14 | Execute held-out experiments, investigate failures, run ablations | Results reproduce from a clean environment and include negative outcomes |
| Weeks 15–18 | Draft an artifact/benchmark paper or workshop submission if contribution is supported | External technical review finds the claim defensible |
| Months 6–18 | Extend model to identity prerequisites and temporal/AND-OR semantics | New theorem/algorithm/measurement contribution and strong comparisons |
| Months 18–30 | Validate across lab domains and realistic error/cost regimes | Generalization beyond the initial synthetic setting |
| Months 24–42 | Approved analyst study if useful; consolidate publications and dissertation | Institution-specific milestones and supervisory review |

These are planning estimates, not a schedule of unattended agent work or an institutional degree timeline. A PhD normally depends on admission, supervision, coursework/exams where applicable, research progress, and a defended dissertation; confirm the exact requirements with the intended program.

## Publication and integrity strategy

Prepare an initial research statement, a reproducible artifact, a related-work comparison, and a clearly limited pilot. Seek feedback on the research problem before choosing a venue. Preserve raw results and failed hypotheses, record all protocol changes, and distinguish exploratory analysis from confirmatory tests. Do not add fictitious publications, affiliations, datasets, reviews, or acceptance claims. Authorship, assistance disclosure, and data policies must follow the eventual institution and venue requirements.

Potential paper sequence, contingent on actual results: evidence-quality benchmark; cost/error-aware validation planning; multi-domain validation and analyst study. The intended audience is security measurement, systems security, and security assessment research. Venue fit and current submission rules must be checked when a real manuscript exists.
