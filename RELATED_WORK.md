# Related work

This targeted review covers stateful security testing, authorization analysis and reproducible evaluation. It draws on primary publication records, accessible abstracts, artifact documentation and selected paper sections. It is a scoping review; full-system reproduction and systematic screening are separate parts of the research method.

## Stateful web and API testing

[Doupé et al., Enemy of the State, USENIX Security 2012](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/doupe) infers web-application state to guide black-box vulnerability testing. [Doupé’s 2014 dissertation](https://escholarship.org/uc/item/63d660tp) develops related research on automated web vulnerability analysis. These works establish application state as a central concern in security testing.

[Black Widow, IEEE S&P 2021](https://publications.cispa.saarland/3224/1/blackwidow_sp2021.pdf) combines navigation modeling with inter-state dependencies. [Witcher, IEEE S&P 2023](https://sites.cs.ucsb.edu/~vigna/publications/2023_SP_Witcher.pdf) applies coverage-guided fuzzing and fault escalation to injection discovery; its [artifact](https://github.com/sefcom/Witcher) documents the implementation. These approaches concern exploration and vulnerability detection across application behavior.

[Atlidakis et al., RESTler, ICSE 2019](https://www.microsoft.com/en-us/research/wp-content/uploads/2021/03/RESTler.pdf) generates request sequences from API dependencies and execution feedback. Its [implementation](https://github.com/microsoft/restler-fuzzer) provides a practical comparison for stateful API exploration. The authorization-transition evaluation will examine the relevant checkers, supported operations and authentication configuration.

## Authorization analysis

[Sahin, Zhang and Arcuri, Enhancing REST API Fuzzing with Access Policy Violation Checks and Injection Attacks](https://arxiv.org/abs/2604.00702), submitted April 2026, describes access-policy oracles integrated into EvoMaster and executable generated tests. The primary record links to [Journal of Systems and Software DOI 10.1016/j.jss.2026.113060](https://doi.org/10.1016/j.jss.2026.113060). This is a direct comparison for multi-user API checks and regression-test generation. The present review covers the accessible abstract and publisher-indexed sections; full oracle and artifact analysis will establish the supported transition conditions.

[Wu et al., Rethinking Broken Object Level Authorization Attacks Under Zero Trust Principle](https://doi.org/10.1145/3833417), ACM TOSEM, accepted July 2026, presents BolaZ. The accessible publisher abstract describes resource-ID dataflow and authorization boundaries. This is relevant to ownership transitions and resource dependencies. Assessment of its treatment of policy changes requires the complete method and artifact.

The study’s comparison concerns how changes in policy, session generation and cached state affect evidence validity and retest selection. Stateful requests, role switching, authorization checks and generated regression tests are established components of this area.

## Planning under partial observation

[Ghanem’s 2022 doctoral thesis](https://openaccess.city.ac.uk/id/eprint/29885/) studies model-based reinforcement learning and hierarchical planning for network penetration testing. The repository abstract identifies sequential decision-making and partial observation as central problems. These problems also motivate validation selection, although network planning and application-policy transitions have different state and action models.

[Deng et al., PentestGPT, USENIX Security 2024](https://www.usenix.org/conference/usenixsecurity24/presentation/deng) evaluates a penetration-testing framework designed to address context loss. Its benchmark and artifact provide related examples of task definition and evaluation for testing assistance.

## Reproducible security evaluation

[Mei et al., ARVO, EuroS&P 2026](https://adamdoupe.com/publications/arvo-eurosp2026.pdf) provides reproducible historical vulnerability environments and patch checking. [CyberGym, Berkeley RDI report, October 2025](https://rdi.berkeley.edu/blog/cybergym/) describes execution-based vulnerability reproduction on open-source software. Both inform the use of pinned environments, triggering inputs and post-patch controls. Their vulnerability tasks differ from authorization-policy transitions.

[Dong et al., Ta’veren, NDSS 2026](https://adamdoupe.com/publications/taveren-ndss2026.pdf) recovers PLC state machines for policy checking. [Liu et al., DRIFT, ASE 2025](https://cs.uwaterloo.ca/~m285xu/assets/publication/drift-paper.pdf) studies on-device firmware tracing and testing overhead. These systems provide methodological context for state recovery and observability; neither is an application-authorization baseline.

## Review method

The extended review will search ACM, IEEE, USENIX, NDSS and author repositories for authorization testing, revocation, role changes, session invalidation, cache consistency, stateful API fuzzing and regression-test selection. Screening records will distinguish publication versions and record inclusion decisions, supported contracts, datasets, metrics and artifact availability. Citation tracing and baseline reproduction will support the final comparison.
