# enumeration
## Why enumeration matters

Enumeration is the first and most important phase in AD attacks. Everything else depends on what you find here.

## Key Enumeration Targets
### Users

Check for old accounts, weak policies, and privilege roles.

### Groups

Identify high-value groups like domain admins, enterprise admins, and backup operators.

### Computers

Find servers with high privileges or misconfigurations.

### ACLs

Look for permissions that allow user takeover or privilege escalation.

### Shares

Locate sensitive files and exposed credentials.

### Trusts

Find ways to move to other domains or forests.

## Enumeration Techniques
### LDAP enumeration

Pulling data directly from AD.

PowerShell enumeration

Using powerview or builtin cmdlets.

BloodHound collection

Mapping privilege paths.

Manual checks

Reviewing policies, GPOs, and permissions with built-in tools.
