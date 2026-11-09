# Authorization-transition laboratory protocol

## Environment

The planned laboratory uses isolated local virtual machines, synthetic accounts and synthetic records. Each deployment record will identify the operating-system image, application commit, dependencies, network configuration and reset procedure. Network adapters will use host-only or internal connectivity; single-VM fixtures may use loopback.

## Paired fixture

The initial fixture will implement a private resource and a revocable permission. A secure configuration will enforce the declared revocation contract. A paired fault configuration will retain an authorization decision after that contract requires enforcement. This pair provides positive and negative controls for the acquisition process.

## Acquisition sequence

1. Restore the initial state and create two synthetic users, two tenants and a private record with a unique marker.
2. Grant user A access. Confirm the record through A’s existing session and an independent administrator control. Confirm user B is denied while B’s authorized operation succeeds.
3. Revoke A through the supported administrative operation. Record the accepted change and its enforcement deadline.
4. Request the record with A’s existing session and a fresh session at declared intervals. Record the protected effect and marker as well as response status.
5. Repeat an unaffected authorized operation to establish service availability. Inspect the authoritative permission record independently where the fixture permits it.
6. Reset and repeat against the paired configuration. Verify removal of prior sessions, cached decisions and synthetic records.

## Evidence record

Each observation will contain:

`application_commit`, `scenario_id`, `policy_contract`, `policy_version`, `principal_id`, `session_generation`, `resource_id`, `change_operation`, `change_accepted_at`, `enforcement_deadline`, `request_started_at`, `response_status`, `observed_effect`, `control_outcome`, `artifact_hashes`, `reset_id`.

UTC timestamps identify events; monotonic elapsed time measures enforcement windows. Credentials and records will be synthetic. Raw artifacts will be retained with hashes and a versioned transformation record for derived data.

## Acceptance criteria

The acquisition sequence must detect the planted stale-authorization fault, accept the secure control and classify unavailable service or failed positive controls as inconclusive. Authentication failure is recorded separately from resource denial. A response within a permitted propagation interval is evaluated against that interval.

The applicable RESTler and EvoMaster configurations will be exercised against the same fixture before application-corpus evaluation. Baseline setup records will include manual configuration and unsupported operations. Historical cases will require clear policy expectations and reproducible vulnerable/fixed behavior; exclusions will retain their reasons.
