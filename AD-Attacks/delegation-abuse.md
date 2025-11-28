# delegation-abuse
## What delegation is

Delegation allows one system or service to act on behalf of a user. AD supports different delegation types to make authentication easier.

## Why delegation is dangerous

If delegation is misconfigured, attackers can impersonate any user, including highly privileged accounts.

## Types of Delegation
### Unconstrained Delegation

A service can act as any user. If this server is compromised, the attacker can impersonate anyone.

Constrained Delegation

Limits which services can be impersonated. Still dangerous if targeted service is high-privileged.

Resource-Based Constrained Delegation

Controlled by the target service. Often easier for attackers to abuse.

## Common Delegation Attacks
### Steal a ticket from an unconstrained server

When attackers compromise a server, they can capture tickets from any user who connects to it.

Abuse RBCD to impersonate users

Attackers can modify delegation permissions if they control a machine account.

Combine delegation with Kerberos attacks

Delegation issues become even more powerful with forged tickets.
