# Testing authorization after policy changes

Research proposal · 23 October 2026

## Problem

Authorization is often tested as a static matrix: a principal requests a resource and the response is checked against the expected permission. In practice, permissions change while sessions, tokens, application caches and background work remain active. A request denied to a fresh session may still succeed through an older session. Conversely, a temporary failure or an expired session can be mistaken for successful enforcement.

This study will investigate how to test authorization across such changes. The first scope is multi-user web applications and REST APIs deployed in a local virtual lab. Active Directory, endpoint exploitation and wireless assessment are outside the initial empirical claim.

An illustrative case has four steps: establish that an authorized user can read a synthetic private record; revoke that permission through the supported administrative operation; repeat the request with the existing session; repeat it with a fresh session and an unaffected control user. The expected result depends on the application’s documented revocation contract. An eventual-consistency delay is not automatically a vulnerability.

## Research questions

1. Which permission-transition failures are missed by testing each identity against a single static snapshot?
2. Can dependency-aware invalidation of earlier observations reduce retesting cost without missing failures after a policy change?
3. Can a replayable test distinguish authorization failure from session expiry, missing data, infrastructure failure and allowed propagation delay?

The second question is conditional. A dependency model must first be shown to capture the relevant effects of a policy change. Retesting only a guessed subset may miss exactly the failures the study seeks to find.

## Proposed method

Represent a test as a sequence over principal, session, resource, policy version and observed application state. Each security conclusion records the conditions under which it was obtained. A permission change invalidates affected conclusions; a scheduler selects the next control or probe needed to re-establish them. The method produces the sequence, expected policy, observed effect and replay instructions for review.

The result categories are confirmed violation, behavior consistent with the tested policy, and inconclusive. A successful response alone is insufficient to prove disclosure: a synthetic resource marker must demonstrate access to the protected object. A denied response alone is insufficient to prove enforcement: authentication validity and an authorized positive control must succeed. For writes, verify the actual state change through an independent permitted read or database fixture check.

The proposed contribution is the treatment of policy transitions and invalidated evidence in test generation and retest selection. Stateful requests, role switching, authorization matrices, provenance hashes and generated regression tests are established techniques. Novelty is unresolved until the closest systems have been examined and reproduced.

## Relation to existing work

RESTler supplies a strong reference for dependency-aware request sequences. EvoMaster’s 2026 access-policy work is a direct baseline for security oracles and generated tests. BolaZ is relevant to resource-ID flow and authorization boundaries. Enemy of the State and Black Widow establish substantial prior work on state-aware web exploration. The proposed study must identify a failure class these methods miss under a fair configuration, rather than compare only with a weak status-code checker. Sources and limits appear in [RELATED_WORK.md](RELATED_WORK.md).

## Experimental scope

Begin with explicit revocation, role downgrade, tenant removal and resource ownership transfer. Compare existing and fresh sessions, immediate and delayed checks, and direct and cached access paths. Begin with fixed, deterministic application contracts before adding distributed components or timing uncertainty.

Use deliberately seeded cases to test the apparatus and historical open-source defects to assess realism. Keep the two groups separate. Each historical case requires pinned source, its patch, a working pre-patch demonstration and a post-patch control. A training application is useful for development but does not establish generality.

All execution occurs in isolated local VMs with synthetic records. Application families, not individual requests, define the evaluation split. Measure whether the workstation can support each deployment before specifying corpus size. No customer environment, external scanning or human-subject experiment is needed for the first study.

## Expected outputs and decision gates

| Stage | Output | Decision |
|---|---|---|
| Prior-work reproduction | Versioned comparison matrix and executable baseline run | Continue only if a specific unsupported task or measurement gap remains |
| Corpus feasibility | A small set of reproducible policy-transition cases with independently specified expectations | Continue only if failures and controls replay reliably |
| Method development | State/evidence model and prototype scheduler | Test on development families; record all changes |
| Evaluation | Held-out comparisons, costs, errors, inconclusive outcomes and ablations | Retain negative results and explain exclusions |
| External review | Research report and reproducibility package | Choose a submission venue only after the contribution is supported |

A credible negative outcome is that full retesting is sufficiently cheap, dependency inference is unreliable, or an existing fuzzer already detects the same failures. In that case, report the measurement result and stop presenting the scheduler as an advance.

## Current status

This is a proposal. No policy-transition corpus, application adapter or new scheduler has been implemented. Existing graph code remains available as an earlier exploratory experiment. Its synthetic results do not answer the research questions above.
