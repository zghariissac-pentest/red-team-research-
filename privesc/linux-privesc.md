# Linux Privilege Escalation

Linux privilege escalation focuses on moving from a normal user to root by abusing weak configurations, inherited permissions, environment variables, or vulnerable services. Linux environments vary widely, so enumeration and understanding how each component interacts is the most important part of escalation.

## Core Principles
### Enumeration first

Linux systems differ from each other. Enumeration gives you a complete map of users, permissions, services, and version details before attempting any escalation.

### Prefer misconfigurations over exploits

Most real privilege escalations come from weak permissions, writable paths, or predictable behaviors rather than kernel exploits.

 ### Minimize noise

Avoid brute-force scanning or continuous probing. Subtle and manual commands blend with normal admin routines.

### Chain small weaknesses

Linux privilege escalation usually happens by combining multiple steps: writable binaries + sudo permissions + environment variable abuse.

## Essential Enumeration Areas
### System information

Check OS version, kernel version, distribution, installed updates, and architecture. Kernel-based exploits depend heavily on version data.

### Users and groups

User membership determines what commands or paths you can interact with. Weak or unnecessary group assignments often lead to escalation.

### Sudo privileges

Misconfigured sudoers files are one of the most common escalation paths. Focus on commands that can be abused to spawn shells or modify files.

### Services

Running services, especially custom ones, often expose writable files or dangerous environment configurations.

### Installed software

Outdated tools, scripting languages, or misconfigured applications might allow arbitrary execution.

### File and directory permissions

Writable root-owned directories, scripts executed by cron, or binaries executed by services can be replaced or manipulated.

### Cron jobs

Unprotected cron jobs are classic escalation points. Look for scripts or tasks with weak permissions.

### Capabilities

Linux capabilities allow binaries to perform privileged actions without being fully privileged. Misconfigured capabilities are often exploitable.

## Common Privilege Escalation Techniques
### Exploiting sudo misconfigurations

If a user can run commands without a password, check whether the command can be escaped into a shell or can manipulate important files.

### Writable service or script paths

Services that run as root but use scripts or binaries located in writable directories allow replacing the executable.

### Cron job abuse

If root-owned cron tasks execute files that are writable by the current user, you can insert commands to gain root access.

### SUID binaries

SUID binaries run with elevated privileges. Misconfigured or custom SUID binaries can be exploited to execute arbitrary commands as root.

### PATH variable manipulation

Scripts that call commands without absolute paths can be tricked by placing malicious binaries earlier in the PATH variable.

### Capabilities misuse

Binaries given capabilities such as reading sensitive files or performing network actions might be abused to escalate privileges.

### Kernel exploits

If the system is missing patches and runs an exploitable kernel version, known proof-of-concept exploits may provide direct escalation. This should be a last resort due to stability concerns.

### SSH keys and credential leaks

Readable private keys, backups, or configuration files can give access to privileged accounts.

### Docker or container escape

Membership in the docker group allows root-level access. Running privileged containers may result in host breakout.

## High-Value Enumeration Targets
### Home directories

Look for credentials, SSH keys, history files, or common scripts used by admins.

### /etc/passwd and /etc/shadow

Misconfigurations here can expose hashes or weak password settings.

### /etc/sudoers and included sudoers files

Small misconfigurations can provide full access.

### /tmp and /var/tmp

Common drop locations. Writable by everyone, but useful when chaining exploits.

### System services

Configuration files stored in writable locations are dangerous.

### Logs

Log files sometimes reveal credentials or command histories used by admins.

## Living-off-the-Land Techniques
### Using built-in commands

Linux offers many preinstalled tools that can be abused for enumeration or execution.

## Examples include:
 whoami
id
find
awk
sed
tar
bash
python

### Using system logs

Logs from cron, syslog, or authentication can reveal how privileged accounts behave.

### System environment variables

Environment variables influence service behavior and script execution.

## Defensive Awareness
### Avoid running automated scanners early

They generate noise and create detectable patterns.

### Work manually and precisely

Use small commands that mimic real administration behavior.

### Avoid destructive actions

Never modify system-critical files unless necessary.

### Stay aware of auditing

Commands like sudo are logged. Plan your movements with that in mind.

### Building a Reliable Escalation Path
#### Step 1: Enumerate

Collect system, user, group, permission, and service information.

#### Step 2: Identify weak points

Look for writable paths, misconfigured sudo rules, cron tasks, services, or capabilities.

#### Step 3: Choose the safest path

Favor misconfigurations over kernel exploits.

#### Step 4: Execute with minimal impact

Add only what you need to escalate.

#### Step 5: Confirm privileges

Check whether you gained root or higher permissions.

#### Step 6: Clean up

Remove artifacts, restore file contents, and delete temporary payloads.

## Summary

Linux privilege escalation relies on careful enumeration and exploiting misconfigurations in permissions, services, or filesystem structure. By understanding how different components of the system interact, and using small chained actions, you can build a reliable and clean escalation path that fits real red team operations.
