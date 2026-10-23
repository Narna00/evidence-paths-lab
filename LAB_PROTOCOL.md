# Local lab: first authorization-transition experiment

This plan is independent of the public pentesting reference site. It requires local VMs and synthetic accounts only. No lab deployment or experiment described here has yet been completed.

## First milestone

Establish one reproducible permission-revocation sequence on a small local application. Run it against a secure implementation and a deliberately flawed implementation that retains an authorization decision after revocation. This validates the apparatus; it is not evidence of a new vulnerability or a publishable contribution.

Use an isolated application VM with a host-only or internal network. Record the OS image, application commit, dependency versions, network configuration and reset procedure. Check available memory/storage before adding a database, identity service or separate cache VM. Use an application-specific loopback binding when a single VM is sufficient.

## Sequence

1. Reset to the declared initial state. Create two synthetic users, two tenants and one private record containing a unique canary marker.
2. Grant user A access. Confirm the record through A’s existing session and an independent administrator control. Confirm user B is denied while B’s own authorized operation still succeeds.
3. Revoke A’s permission using the supported administrative operation. Record when the change is accepted and when the policy contract requires enforcement.
4. Read the record with A’s old session and then with a fresh session at declared time intervals. Verify the protected marker, not only the status code.
5. Repeat an unaffected authorized request to distinguish enforcement from an unavailable service. Where permitted by the lab fixture, inspect the authoritative permission record independently.
6. Reset and repeat against the paired implementation. Confirm that the reset removed prior sessions, cache state and test records.

Each record should include `application_commit`, `scenario_id`, `policy_contract`, `policy_version`, `principal_id`, `session_generation`, `resource_id`, `change_operation`, `change_accepted_at`, `enforcement_deadline`, `request_started_at`, `response_status`, `observed_effect`, `control_outcome`, `artifact_hashes` and `reset_id`. Use monotonic elapsed time for windows and UTC for the event ledger. Store only synthetic credentials.

## Acceptance

The sequence must detect the planted stale-authorization fault, accept the secure control and return inconclusive when the service or positive control is unavailable. A fresh session that fails authentication must never count as proof that resource authorization works. An allowed consistency delay must not be labeled a defect.

After this milestone, reproduce the applicable EvoMaster and RESTler baselines on the same fixture. Record manual configuration and unsupported features. Then identify historical open-source authorization fixes that can be rebuilt and checked locally. Reject cases without a clear policy expectation or reliable pre/post reproduction; retain exclusion reasons.

The existing `lab_web.py` in the separate workbench is a static object-authorization teaching fixture. It does not implement policy revocation, session generations or cache consistency and cannot validate this study without new implementation.
