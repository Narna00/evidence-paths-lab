# Testing authorization after policy changes

## Abstract

Permission changes can invalidate security observations while sessions, caches and background operations remain active. This research investigates how to generate and select authorization tests across these transitions. The proposed method associates observations with their policy and application-state dependencies, identifies evidence affected by a change and selects controls and probes for revalidation. Evaluation will compare static permission matrices, complete replay, stateful API testing and selective revalidation in isolated application deployments.

## Research questions

1. Which permission-transition failures are missed by testing identities against a single static snapshot?
2. How accurately can dependencies between policy changes and test observations be identified?
3. Can selective revalidation reduce assessment cost while maintaining detection relative to complete replay?
4. How reliably can replayable controls distinguish authorization failures from session expiry, unavailable resources, service failure and permitted propagation delay?

## Proposed method

A test sequence records the principal, session generation, resource, action, policy version and relevant application state. Each conclusion is associated with the conditions under which it was observed. A permission change invalidates affected evidence; a scheduler selects the next control or probe needed to establish the resulting behavior.

The output will include the request sequence, expected policy, observed effect, control results and replay instructions. Outcomes are confirmed violation, behavior consistent with the tested policy, or inconclusive. Reads require evidence of the protected object; writes require independent confirmation of the resulting state. Authentication validity and service availability are checked separately.

The technical focus is the relationship between policy transitions, evidence validity and retest selection. Existing stateful testing and access-policy techniques provide the starting point and experimental comparisons; their relationship to this formulation is described in [RELATED_WORK.md](RELATED_WORK.md).

## Scope

The application study will cover explicit revocation, role downgrade, tenant removal and resource ownership transfer in multi-user web applications and REST APIs. Test conditions will distinguish existing and fresh sessions, immediate and delayed enforcement, and direct and cached access paths.

Seeded faults will support harness verification and controlled sensitivity analysis. Historical open-source defects will support evaluation against application behavior. Each historical case will pair a pinned vulnerable version with its documented patch and a reproducible post-patch control. The two corpus groups will be analyzed separately.

Execution will use isolated local virtual machines and synthetic identities and records. Application families and policy implementations will define the development/evaluation split. Corpus size will be determined by reproduction feasibility and the precision required for the primary comparisons.

## Experimental comparisons

| Method | Role in the evaluation |
|---|---|
| Static role/resource matrix | Snapshot-based authorization coverage |
| Complete replay after a change | Reference coverage within the declared inventory |
| Stateful API test generation | Coverage from dependent request sequences |
| Access-policy security checks | Detection through established authorization oracles |
| Selective revalidation | Cost and detection under evidence dependency tracking |
| Random selection at equal cost | Selection baseline without dependency information |

Exact versions, supported operations, adapters, authentication setup and configuration effort will be recorded. Comparisons will use equivalent deployment states and reset conditions.

## Research outputs

The study will produce a model of policy transitions and evidence validity, a test-selection implementation, a reproducible application corpus and a comparative evaluation. The evaluation will include cases where dependency tracking misses relevant effects or where complete replay is equally economical. Protocol changes and exclusions will accompany the released results.

Detailed outcome definitions and analysis appear in [PROTOCOL.md](PROTOCOL.md). Deployment and acquisition procedures appear in [LAB_PROTOCOL.md](LAB_PROTOCOL.md).
