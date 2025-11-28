# forest-attacks
## What a forest is

A forest is a collection of domains that trust each other. It is the highest level of AD structure.

### Why forests matter

If an attacker compromises one domain, they can sometimes move to other domains or even control the entire forest.

## Forest Trust Types
### Parent-child trust

Automatic trust between related domains.

### Tree trust

Trusts between domain trees in the same forest.

### External trust

Connects domains from different forests.

### Forest trust

Full trust between two forests.

## Common Forest Attack Paths
### Exploiting trust misconfigurations

Weak permissions allow movement across domains.

Abusing Enterprise Admin privileges

Enterprise Admins have control across the forest.

Kerberos trust key attacks

If trust keys are leaked, attackers can forge inter-domain tickets.

#### SIDHistory abuse

Attackers inject old SIDs to gain privileges across domains.
