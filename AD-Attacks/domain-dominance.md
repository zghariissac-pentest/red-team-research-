# domain dominance
## What domain dominance means

Domain dominance is when an attacker reaches a level where they control the entire domain permanently, not just a temporary privileged account.

### Why attackers aim for it

With domain dominance, an attacker has long-term persistence and unrestricted control.

## Paths to Domain Dominance
### Domain Admin compromise

Full control of AD objects, GPOs, and credentials.

### KRBTGT compromise

Allows forging tickets (Golden Ticket).

### GPO control

Attackers can push payloads, create accounts, or modify security settings.

### AdminSDHolder abuse

Used to maintain persistence by overwriting permissions on protected accounts.

### ACL abuse

Misconfigurations on AD objects allow privilege escalation without passwords.
