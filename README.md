# Evidence Paths Lab

This repository contains an exploratory graph experiment and a revised research plan for testing authorization after permissions change.

The research problem is specific: a user loses a role, leaves a tenant, or has access revoked, but an existing session or application component may continue to authorize requests. The proposed study asks how to detect these failures, distinguish a security defect from permitted propagation delay, and preserve a test that reproduces the result.

The new study has not been implemented or evaluated. The existing code computes reachability bounds on synthetic graphs. It is retained as an earlier experiment, with its results and limitations intact. It is not an authorization scanner.

## Research documents

- [Research assessment](RESEARCH_ASSESSMENT.md): comparison with university research, published systems and doctoral work; reasons for changing direction.
- [Study proposal](PROPOSAL.md): problem, research questions, candidate contribution and scope.
- [Related work](RELATED_WORK.md): primary sources and the closest overlap, including work published in 2026.
- [Evaluation plan](PROTOCOL.md): baselines, controls, measurements and rules for interpreting results.
- [Local lab plan](LAB_PROTOCOL.md): the first reproducibility experiment and its acceptance criteria.

## Earlier graph experiment

Python 3.12 or later; standard library only:

```sh
python -m unittest discover -v
python evidence_paths.py graph.example.json --trust-policy trust.example.json --as-of 2026-10-21T12:00:00Z --recommend
python benchmark.py --seeds 30 --output new-pilot
```

The example returns exit code 1 because the modeled transition remains unresolved. The benchmark refuses to overwrite an existing output directory. [MODEL.md](MODEL.md) defines the graph semantics. [PILOT.md](PILOT.md) reports the synthetic results; `pilot-results.zip` contains the underlying artifacts. The original proposal and protocol are preserved under [archive-2026-10-21.zip](archive-2026-10-21.zip).

At a validation budget of five, the gain heuristic resolved 75% of synthetic queries; path-first resolved 80%. These pooled descriptive results do not establish superiority of the proposed heuristic. Correct, perfect-cost validation and a complete candidate graph were simulation assumptions. No production system or independent application corpus was tested.

Optional figures can be regenerated with `report.py` after installing `requirements-figures.txt`. That script overwrites generated reports and archives. `render_plot.cjs` uses the optional dependency in `package.json` to render the PNG. Preserve the original results before regeneration.

## Scope

Experiments are restricted to locally hosted software and isolated virtual machines using synthetic identities and records. The research is independent of the public Assessment Workbench. No human-participant study, new vulnerability discovery or publication acceptance is reported.
