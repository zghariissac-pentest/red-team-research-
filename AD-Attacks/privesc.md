# privesc
## What privilege escalation is

Privilege escalation is gaining higher permissions inside the domain. Attackers look for any weakness that lets them jump from a low-priv user to a privileged one.

## Common AD Privilege Escalation Paths
### Weak ACLs

Permissions that allow attackers to modify objects, reset passwords, or grant rights.

### GPO misconfigurations

Attackers can push malicious scripts or elevate privileges.

### Local admin rights

Local privilege escalation helps attackers move laterally.

### Vulnerable service accounts

High-privileged service accounts with weak or reused passwords.

### Delegation misuse

Allows impersonation of privileged users.

### Token abuse

Stealing or injecting tokens from privileged sessions.

### Kerberos escalation

Using forged tickets to elevate rights.

## Persistence Techniques
### AdminSDHolder

Ensures attacker rights remain even after cleanup.

Rogue GPO

Deploys malicious configuration repeatedly.

Backdoored service accounts

Adds hidden rights through ACL manipulation.
