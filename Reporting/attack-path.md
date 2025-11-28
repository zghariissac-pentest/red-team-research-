# attack-path
## What this file is

This file gives a clear example of how an attacker moves inside an environment. It shows the logic behind attack chains, not the technical exploit details.

## Example attack path
### 1. initial access

Attacker gets a low-priv user through phishing or a weak password.

### 2. internal recon

Attacker checks the network, users, and systems to understand the environment.

### 3. credential access

Attacker captures local credentials or session tokens on a workstation.

### 4. lateral movement

Attacker uses the stolen credentials to move to a more important system like a file server or an admin workstation.

### 5. privilege escalation

Attacker finds a misconfiguration or a weak ACL that gives higher permissions.

### 6. domain impact

Attacker reaches domain admin or full domain control.

### 7. persistence

Attacker creates long-term access points such as scheduled tasks, rogue users, or modified ACLs.

### 8. objectives

Data theft, internal simulation, or anything defined by the engagement.
