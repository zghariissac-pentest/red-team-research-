# Windows Privilege Escalation

Privilege escalation on Windows focuses on moving from a low-privileged account to higher privileges by abusing system weaknesses, misconfigurations, or accessible components. This phase is critical because most initial access points do not offer administrative privileges. A good approach combines enumeration, understanding of system behavior, and safe exploitation.

## Principles of windows privilege escalation

Privilege escalation on Windows follows clear principles that guide every technique.

### Enumeration before exploitation

You identify what exists, what is misconfigured, and what can be abused before attempting anything. Enumeration decides the correct path instead of running random exploits.

### Abuse misconfigurations first

Misconfigurations are more stable and reliable than memory corruption or binary exploits. They are also common in real environments.

### Think like a system owner

Many weaknesses come from convenience choices made by administrators. Your job is to observe and treat the system as something designed by a human with shortcuts.

### Avoid noisy or destructive actions

Your goal is controlled escalation, not damage. Avoid crashes, avoid forcing restarts, and prefer low-noise paths.

### Core Enumeration Steps

A solid escalation path always begins with structured enumeration.

#### System information

Check OS version, build number, patch level, and architecture. Some privilege escalation techniques depend on specific builds or missing patches.

### User and group information

Review groups, privileges, and local administrators. Sometimes a low-privileged user is part of a powerful group without knowing it.

### Services and scheduled tasks

Misconfigured services and tasks often allow file replacement, writable paths, or unquoted paths.

#### Installed software

Look for old, outdated, or auto-update agents running with high privilege.

### Permissions on the filesystem

Writable directories in system paths or service directories are strong escalation candidates.

### Registry permissions

Weak registry key permissions can allow DLL or executable hijacking.

### Token information

Check available tokens, impersonation privileges, and potential for token abuse or privilege duplication.

### Common Privilege Escalation Techniques

This section covers the techniques seen most often during red team operations.

### Exploiting service misconfigurations

Many Windows services run with high privileges. If you can modify the service configuration or its executable path, you can replace it with your own payload. Look for unquoted paths, weak permissions, and writable binaries.

### DLL hijacking

Applications that load DLLs from predictable locations can be abused if you can write to those paths. A crafted DLL executes with the permissions of the calling process.

### Registry-based escalation

Some services load configuration or DLL paths from registry keys. If those keys are writable, you can redirect execution to your payload.

### Scheduled tasks

Weak permissions on scheduled tasks allow replacing the action or executable tied to the task.

### Token impersonation

Windows often creates tokens for privileged accounts. If a process has access to such tokens, it can duplicate or impersonate them to elevate privileges without changing the filesystem.

### Vulnerable drivers

Many environments install drivers that allow direct memory access or raw operations, which can be abused to disable protections or escalate privileges.

### User credential leaks

Stored credentials from administrators, saved Wi-Fi keys, password managers, RDP credentials, or startup scripts may grant direct privileged access.

### Named pipe impersonation

Applications that create privileged named pipes can be abused by connecting first and forcing the application to authenticate against your controlled instance.

### Directory permission abuse

If a privileged application loads from a directory you can write to, you can replace or add files to gain control.

### High-Value Enumeration Targets

These are places where misconfigurations appear more frequently.

### Program Files

Look for writable subfolders, unusual permissions, or leftover installers.

### Service executables

Any binary running as SYSTEM is a powerful target if you can replace it.

### Startup folders

Executables placed here run automatically under certain accounts.

### Tasks under system management suites

Update agents, antivirus scripts, and automation tools often run as SYSTEM.

### LSA and SAM storage

Credentials or sensitive hashes may leak if the system is misconfigured.

Living-off-the-Land for Privilege Escalation

Windows has many built-in tools that can support escalation.

### PowerShell

Allows enumeration, code execution, and interacting with services and registry.

WMI

Useful for exploring services, scheduled tasks, and system information.

Certutil

Can assist with binary handling and execution paths.

Task Scheduler

Lists and manipulates tasks.

Built-in system utilities

Many utilities can be repurposed for execution or file replacement if permissions allow it.

Defensive Friction and EDR Considerations

During escalation, you often encounter defensive controls. Awareness helps avoid detection.

Avoid known attack signatures

Many tools have recognizable artifacts that detection tools look for.

### Focus on manual enumeration

Manual commands generate less noise and avoid common detection triggers.

### Avoid memory injection early

Save in-memory execution methods until after gaining higher privileges, when you have more control.

### Use staged enumeration

Break down your enumeration into small steps instead of large automatic sweeps.

Blend with normal administrative activity

Use commands and utilities that administrators commonly use.

### Building an Escalation Path

A proper privilege escalation path should follow a predictable flow.

### Collect information

Gather data about users, groups, services, tasks, binaries, and permissions.

### Identify misconfigurations

Look for writable paths, weak services, or unprotected registry keys.

### Evaluate impact

Determine the privilege you will gain and whether the technique is reliable.

## Execute minimally

Perform the minimum actions required to escalate.

## Verify escalation

Confirm your privilege level before proceeding.

## Clean up

Remove binaries, logs, or artifacts left behind.

Summary

Privilege escalation on Windows relies on structured enumeration, understanding system configuration, and exploiting weaknesses that emerge from daily administrative decisions. By combining controlled steps with a clear understanding of the Windows architecture, you can build reliable escalation paths that match real red team operations.
