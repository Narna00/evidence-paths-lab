# Local virtual lab protocol

## Stage A: deterministic software fixture

Use the companion [Assessment Workbench](https://github.com/Narna00/assessment-workbench) `lab_web.py`. Its pure `handle` function and loopback HTTP mode provide paired flawed/fixed behavior for object authorization, SQL boolean interpretation, and reflected markup. These are deliberately simplified fixtures, not a representative web-app population.

For each snapshot, record source commit/hash, secure-mode flag, route, test principal, fixture object ownership, baseline response, probe response, expected result, and independent owner/reviewer label. A scanner claim and a reviewer looking at the same scanner output are not independent ground truth. Establish ownership and implementation state separately.

Example transition: `app-session -> foreign-order-readable`. Preconditions: a valid low-privilege lab-b session, object 1001 owned by lab-a, a known route/method, and a fixed snapshot. Control: lab-a can read its own object. Probe: lab-b requests that object. In the flawed fixture the foreign read succeeds; in the fixed fixture it is denied. A denial caused by an invalid token is not evidence of correct object authorization.

Record both positive and negative controls, plus a sensor-failure scenario in which the observation is deliberately omitted. Map omission to UNKNOWN. If you duplicate the same response into three reports, retain one origin lineage. If a snapshot changes, expire the prior transition validation and collect again.

## Stage B: isolated web scenario families

Build multiple application implementations or use legally available, locally hosted training targets with version-pinned images. Separate application family, authorization design, database adapter, and reverse-proxy configuration across splits. Random object IDs within one implementation are not independent scenario families.

Use synthetic users, tenants, records, and canary services only. Keep network adapters host-only/internal and block unapproved egress. No internet callback or production metadata service is needed. Capture tool runtime and operator validation time separately. Store redacted summaries with restricted originals and integrity manifests.

## Stage C: identity/endpoint scenarios

If workstation resources permit, add a legitimately licensed evaluation directory controller and member VM. Start with membership, delegation configuration, service ACLs, and explicit negative controls. Snapshot both machines together, track domain/host identity and clock state, and document any action requiring state changes. A lab configuration ledger determines ground truth, while approved authenticated queries provide fallible observations.

Do not assume a directory attribute makes an exploit feasible. Introduce each additional prerequisite explicitly before moving to an AND/OR or stateful model. Keep the current simple reachability results separate from richer model experiments.

## Wireless boundary

With local VMs only, evaluate offline capture parsing, BSSID inventory, source lineage, and incomplete observation handling. EAP/PMF negotiation, roaming, management-frame behavior, and RF interference require owned hardware and appropriate isolation. No RF-layer result is claimed by this project or its synthetic pilot.

## Evidence ledger fields

`scenario_id`, `family_id`, `snapshot_id`, `source_commit`, `image_digest`, `configuration_change`, `test_case_id`, `transition_id`, `principal`, `target_fixture`, `vantage_point`, `start_utc`, `end_utc`, `tool_version`, `input_artifact_hash`, `output_artifact_hash`, `origin_id`, `ground_truth_method`, `reviewer`, `validation_cost`, `collection_error`, `rollback_verified`.

An adapter must not convert `secure_observed` into a universally false edge. It can validate only the exact transition under the recorded preconditions and snapshot. Out-of-scope implications remain unknown. Hashing supports integrity but does not authenticate a claimed reviewer or observation time.

## Acquisition acceptance criteria

Every released scenario must recreate from pinned sources; every Boolean transition must have independent ground-truth justification; every corruption operation must be logged; every parser/import transformation must be versioned; every excluded scenario must retain its exclusion reason. A second person should reproduce a sample before any field-generalization claim.
