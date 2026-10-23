# Assessment of the research direction

23 October 2026

## Conclusion

The existing graph prototype does not establish a doctoral contribution in penetration testing. It implements useful distinctions between confirmed, possible and unresolved reachability, but the central reasoning ideas are established, the input graphs are synthetic, and the validation oracle is perfect. Its experimental result also fails to support the proposed planner over the stronger path-first baseline.

The recommended replacement is a focused study of authorization testing after permission changes. The research would examine executable request sequences, application state and actual enforcement. Its value must be established by reproducing existing methods and measuring a gap they do not already address.

## Comparison with research groups and published work

| Research setting | Work examined | What it demonstrates | Gap in the existing project |
|---|---|---|---|
| Arizona State University and collaborators | ARVO, EuroS&P 2026 | A method and dataset for rebuilding, triggering and checking historical software vulnerabilities across versions | No independently reproduced software vulnerabilities or comparable acquisition pipeline |
| ASU and New Mexico State University | Ta’veren, NDSS 2026 | Recovery and policy checking of state machines from PLC binaries | The prototype accepts a supplied graph; it does not recover application semantics or identify implementation defects |
| UC Santa Barbara | Doupé’s 2014 dissertation and Enemy of the State, USENIX Security 2012 | Research on web vulnerability analysis, including state inference and testing | No executable web exploration, state inference or comparison with a working scanner |
| University of Waterloo and Northeastern University | DRIFT, ASE 2025 | A concrete firmware testing technique addressing observability and execution overhead | The current cost model counts idealized validations rather than measuring acquisition and execution |
| UC Berkeley | CyberGym, university research report, October 2025 | Execution-based evaluation on real open-source vulnerabilities | Synthetic graph outcomes cannot establish vulnerability discovery or reproduction capability |
| City, University of London | Ghanem’s 2022 doctoral thesis on model-based reinforcement learning for network penetration testing | A sustained investigation of sequential planning and scalability in a defined testing model | A small graph heuristic and brief proposal do not supply equivalent depth or establish a new planning method |
| Concordia University | Official faculty and laboratory research descriptions | Ongoing interests in vulnerability research, software security and quantitative network vulnerability models | Relevant departmental context, but a lab description alone is not evidence of an algorithm, result or available supervision |

Primary links, reading limits and publication status are recorded in [RELATED_WORK.md](RELATED_WORK.md). These comparisons concern contribution and evaluation, not prestige or repository size. The university pages do not imply endorsement or a supervisory relationship.

## What should be retained

Retain the graph implementation, tests, raw pilot and negative result as an exploratory record. Evidence lineage, explicit preconditions and a refusal to convert missing observations into proof are sound engineering choices. They can inform the new study’s evidence format without becoming its novelty claim.

The old pilot’s zero decision errors under trusted perfect validation are consequences of its assumptions. They are not evidence that the method will avoid mistakes in a practical assessment. Likewise, adding an LLM, a dashboard or more graph families would not resolve the missing contribution.

## Choice of research problem

Three directions were considered. General autonomous penetration testing is crowded and expensive to evaluate well. A new network attack planner would require a substantially richer state model and direct comparison with existing planning research. Stateful authorization testing offers a narrower problem that can be investigated with local VMs and independently observable outcomes.

The selected question concerns permission changes across existing sessions and application components. It is close to daily penetration-testing practice and permits controlled before-and-after experiments. It also has substantial prior art: RESTler already explores dependent request sequences; EvoMaster now has access-policy oracles and executable security tests; BolaZ examines object-level authorization boundaries. None of these capabilities can be claimed as new here.

The candidate contribution is a method for testing and explaining authorization failures across changes in policy, identity and cached state. Whether that distinction survives a full review remains open. If the nearest systems already cover it, the study should become a comparative measurement project or move to a different question before further implementation.

## Work required before a thesis claim

First, reproduce a relevant access-policy baseline and document its limits on a small controlled experiment. Next, obtain locally reproducible application cases with independent policy specifications and vulnerable/fixed controls. Only then implement the proposed method and freeze a comparison protocol. Evidence of a useful difference must precede claims of novelty, generality or publication readiness.

The immediate output is a research statement for technical review, not a completed dissertation. A thesis would require connected contributions over time: a defensible model of policy transitions, a testing method, and a rigorous empirical evaluation. The present repository establishes none of those results yet.
