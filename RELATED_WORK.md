# Related work and university research comparison

Targeted review, 23 October 2026. This is a source-based scoping review, not a systematic literature review. Reading depth is stated below. No external system has yet been reproduced in this project. Publication dates refer to the work, not search-engine crawl dates.

## University and doctoral work

| Source | Evidence examined | Relevance |
|---|---|---|
| [Adam Doupé, ASU faculty research page](https://adamdoupe.com/) and [publication list](https://adamdoupe.com/publications/) | Current research description and publication metadata | Automated vulnerability analysis and web security; identifies the papers below |
| [Doupé, Advanced Automated Web Application Vulnerability Analysis, UCSB dissertation, 2014](https://escholarship.org/uc/item/63d660tp) | University repository abstract | A doctoral programme of related advances in web security; a model for connected contributions rather than a broad toolkit |
| [Meng Xu, University of Waterloo research](https://cs.uwaterloo.ca/~m285xu/research/) and [publications](https://cs.uwaterloo.ca/~m285xu/publications/) | University-hosted project descriptions and publication metadata | Program analysis, fuzzing and verification; emphasizes specific technical mechanisms and practical systems |
| [Concordia: Mourad Debbabi](https://www.concordia.ca/faculty/mourad-debbabi.html) and [Computer Security Laboratory](https://www.concordia.ca/ginacody/cybersecurity-intelligent-systems-eng/research/labs/computer-security-laboratory.html) | Official research-area and project descriptions | Canadian context in vulnerability research, software security and quantitative vulnerability models; not an evaluated paper |
| [Ghanem, Towards an efficient automation of network penetration testing using model-based reinforcement learning, City doctoral thesis, 2022](https://openaccess.city.ac.uk/id/eprint/29885/) | Repository abstract and thesis metadata | Sequential planning, partial observation and hierarchical decomposition already belong to doctoral penetration-testing research; thesis results were not independently verified here |

The institutional sources were used to establish research context. No contact, endorsement, acceptance or availability of supervision is implied.

## Systems, methods and evaluation standards

| Work and primary source | Established contribution | Consequence for this study | Reading depth |
|---|---|---|---|
| [Doupé et al., Enemy of the State, USENIX Security 2012](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/doupe) | Infers application state to guide black-box testing | State-aware web scanning cannot be claimed as new | Primary abstract |
| [Black Widow, IEEE S&P 2021](https://publications.cispa.saarland/3224/1/blackwidow_sp2021.pdf) | Navigation modeling and inter-state dependencies for web scanning | Compare state and dependency coverage, not merely endpoint counts | Accessible paper introduction and contribution summary |
| [Trickel et al., Witcher, IEEE S&P 2023](https://sites.cs.ucsb.edu/~vigna/publications/2023_SP_Witcher.pdf) and [artifact](https://github.com/sefcom/Witcher) | Coverage-guided web fuzzing and fault escalation for injection discovery | A catalogue of injection strings is not a comparable research contribution | Artifact description and selected paper sections |
| [Atlidakis et al., RESTler, ICSE 2019](https://www.microsoft.com/en-us/research/wp-content/uploads/2021/03/RESTler.pdf) and [artifact](https://github.com/microsoft/restler-fuzzer) | Generates dependent request sequences using API specifications and feedback | Required baseline for stateful API exploration; compare the applicable security checkers | Paper examples/limitations and project documentation |
| [Deng et al., PentestGPT, USENIX Security 2024](https://www.usenix.org/conference/usenixsecurity24/presentation/deng) | Pentesting benchmark and a framework addressing context loss | General agent orchestration is already established; not the proposed novelty | Primary abstract and artifact-appendix excerpts |
| [Mei et al., ARVO, EuroS&P 2026](https://adamdoupe.com/publications/arvo-eurosp2026.pdf) | Reproducible historical vulnerability environments and patch checking | Adopt rebuild/trigger/fix controls; its memory-safety task differs from authorization testing | Abstract, introduction and capability description |
| [Dong et al., Ta’veren, NDSS 2026](https://adamdoupe.com/publications/taveren-ndss2026.pdf) | Extracts PLC state machines and checks safety policies | Illustrates the difference between supplying a graph and recovering security-relevant behavior | Abstract, introduction and evaluation overview |
| [Liu et al., DRIFT, ASE 2025](https://cs.uwaterloo.ca/~m285xu/assets/publication/drift-paper.pdf) | On-device firmware tracing and testing through the Debug Monitor | Observability and overhead must be measured; physical firmware requirements exceed a VM-only lab | Abstract and introduction |
| [Wang et al., CyberGym, Berkeley RDI report, October 2025](https://rdi.berkeley.edu/blog/cybergym/) | Execution-checked vulnerability reproduction on production open-source software | Evaluate demonstrated effects and patch controls; a university report is not itself a peer-review claim | University report, task construction and quality controls |

## Closest overlap requiring reproduction

[Sahin, Zhang and Arcuri, Enhancing REST API Fuzzing with Access Policy Violation Checks and Injection Attacks](https://arxiv.org/abs/2604.00702), submitted April 2026, links to [Journal of Systems and Software DOI 10.1016/j.jss.2026.113060](https://doi.org/10.1016/j.jss.2026.113060). The accessible abstract and publisher-indexed sections describe access-policy oracles integrated into EvoMaster and executable generated tests. This directly overlaps with a generic proposal for multi-user API security tests. Full oracle behavior, supported state changes and evaluation must be checked before a distinction is claimed. The publisher page could not be fetched directly in this session; indexed sections and the primary arXiv record were available.

[Wu et al., Rethinking Broken Object Level Authorization Attacks Under Zero Trust Principle](https://doi.org/10.1145/3833417), ACM TOSEM, accepted July 2026, presents BolaZ. The publisher-indexed abstract describes resource-ID dataflow and authorization boundaries. This overlaps with ownership and resource dependency reasoning. Only the indexed primary abstract and metadata were examined; the full publisher page was inaccessible. A claim that policy-transition testing lies outside its scope would be premature.

## Remaining review

Search ACM, IEEE, USENIX, NDSS and author repositories for combinations of authorization testing, revocation, role change, session invalidation, cache consistency, stateful API fuzzing and regression test selection. Follow citations from the two closest works and distinguish versions of the same paper. Record inclusion/exclusion reasons, artifacts, supported contracts, experimental unit and reproduction outcome.

The next decision depends on reproducing these methods, not accumulating more citations. If permission-transition failures are already detected adequately, study the cost and reliability of their use or select a different problem. The present search does not establish absence of prior work.
