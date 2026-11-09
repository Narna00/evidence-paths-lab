# Problem formulation

## Authorization across state changes

A permission check concerns a principal, an action and a resource under a particular policy and application state. When any of these conditions changes, a previously observed result may no longer describe the application’s behavior.

Consider a user who can read a private record through an existing session. An administrator removes the user’s tenant membership. The application may consult an updated database for a fresh session while an older session continues to use cached membership. A static matrix collected before the change cannot determine whether revocation is enforced afterward.

The expected outcome depends on the policy contract. Some systems require immediate revocation; others specify a bounded propagation interval. The relevant failure is a protected effect outside that contract. Authentication failure, a missing resource and service unavailability are separate outcomes.

## Test state

Represent an observation by the tuple `(principal, session, resource, action, policy_version, application_state, time)`. Its evidence record includes the request, observed effect, control outcomes and deployment identity. A policy transition can affect several observations through shared dependencies such as group membership, resource ownership or an authorization cache.

Two questions follow. Which observations lose validity after a transition? Which checks provide enough information to establish the new behavior at the lowest practical cost? A dependency model connects the first question to selective revalidation. Missing dependencies create a risk of omitted tests; overly broad dependencies approach the cost of complete replay.

## Observation and conclusion

The study distinguishes three outcomes:

- **Confirmed violation:** the request produces a protected effect that the policy forbids under the recorded conditions.
- **Behavior consistent with policy:** the expected effect or denial is observed and the relevant controls succeed.
- **Inconclusive:** authentication, service state, policy meaning or available evidence prevents classification.

For a read, a synthetic private marker establishes which object was disclosed. For a write, an independent state read establishes whether the action occurred. Positive controls distinguish denial by policy from failure of the test apparatus. These conclusions apply to the recorded conditions and tested paths.

## Relation to graph reasoning

The repository’s graph model treats candidate transitions as available, unavailable or unresolved. Lower and upper graphs bound reachability using trusted validation records. This abstraction permits controlled study of how a validation policy resolves a query under incomplete evidence.

Authorization transitions introduce additional state: session generation, policy version, object ownership and enforcement delay. A single Boolean edge does not encode all these conditions. The application study will therefore use explicit state and evidence dependencies rather than interpret synthetic graph reachability as a measurement of application authorization.

## Evaluation criteria

The primary comparison is between complete replay and selective revalidation after the same permission change. The evaluation will measure missed violations, false findings, inconclusive outcomes and total validation cost. Stateful API generation and access-policy testing provide additional comparisons, as discussed in [RELATED_WORK.md](RELATED_WORK.md).

A useful selection policy must reduce measured cost while maintaining detection on the declared test inventory. Evaluation by application family and policy implementation will distinguish repeated requests from independent evidence of generalization.
