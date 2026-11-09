# Security reporting

Report vulnerabilities through GitHub private vulnerability reporting when enabled. Otherwise, use the maintainer’s GitHub profile contact information to arrange a private report before transmitting sensitive details.

A report should identify the affected commit, a minimal synthetic reproducer, expected and observed behavior, and security impact. The development branch is the maintained version. Response times depend on maintainer availability.

The tools process local evidence files. Their trust boundary includes the validation-source policy, candidate graph and retained artifacts. File hashes support integrity checking; they do not authenticate an observation’s origin or establish its truth. Use copied, sanitized data and the minimum operating-system privileges required for processing. Application testing requires explicit authorization for the deployment and operations involved.
