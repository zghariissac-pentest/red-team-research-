# Attack Scenarios

This folder contains a curated collection of realistic, real-world inspired adversary simulation scenarios designed to model how modern attackers think, plan, and execute operations inside monitored environments.

Each scenario is built as a full attack narrative rather than a collection of isolated techniques. The focus is on decision making, operational tradeoffs, stealth considerations, and defensive visibility , not just tool usage or command execution.

These simulations aim to reflect practical offensive security workflows including:
- Initial access development
- Internal reconnaissance and enumeration
- Credential abuse and privilege escalation
- Lateral movement strategies
- Persistence mechanisms
- Objective-driven operations
- OPSEC decision making
- Detection and blue team perspective analysis

All scenarios are executed within controlled lab environments and documented with an emphasis on reasoning, alternative paths, and real operational constraints such as endpoint detection, logging, and monitoring systems.

The goal of this section is to demonstrate structured adversary thinking, technical depth, and the ability to simulate realistic red team and threat actor behavior across different environments and threat models.

## Structure
Each scenario follows a consistent documentation model:

- `README.md` — Scenario overview and threat model
- `lab-setup.md` — Environment and infrastructure description
- `attack-flow.md` — Stage-by-stage attack narrative
- `commands.md` — Execution details and operational context
- `opsec.md` — Stealth decisions and risk tradeoffs
- `detection.md` — Defensive visibility and detection opportunities
- `lessons-learned.md` — Reflections and improvement points

⚠️ A `_template` directory is included as an internal blueprint used to create new scenarios and should not be treated as an actual attack simulation.

## Philosophy
These are not CTF walkthroughs or simple exploit notes.

They are structured adversary simulations intended to show:
- how attacks evolve over time
- how decisions change based on defensive posture
- how tradeoffs are made between speed, stealth, and reliability
- how offensive actions appear from a defensive perspective

The emphasis is on realistic thinking, not just technical execution.
