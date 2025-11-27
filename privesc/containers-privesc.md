# Containers Privilege Escalation

Container privilege escalation focuses on breaking out of isolated environments such as Docker, LXC, or containerized applications to gain higher privileges on the host. Containers are designed to isolate processes, but misconfigurations and permissive settings create paths that allow attackers to escape or control the underlying system.

## Core Principles
### Containers are not VMs

Containers share the host kernel. Any misconfiguration that gives too much access to kernel features can lead to full host compromise. Understanding this kernel-sharing model is essential.

## Enumeration inside the container

Each container’s configuration determines how isolated it is. Enumeration identifies mounted directories, environment variables, capabilities, and host exposures.

### Least-privilege assumption

Most escalations happen because the container violates the principle of least privilege. Extra privileges or volumes give more control.

### Abuse misconfigurations first

The most common breakout methods come from misconfigured Docker settings, mounted directories, capabilities, and root privileges inside the container.

### Key Enumeration Targets
User and privilege level

Check if the current container user is root. Running as root inside a container is dangerous for the host if other misconfigurations exist.

### Mounted volumes

Look for host directories mounted inside the container. Write access to the host filesystem is a direct path to full compromise.

Capabilities

Containers can be given Linux capabilities. If dangerous ones are present, they may allow interacting with the host at a privileged level.

Host devices

Device mounts such as host disks or kernel interfaces allow powerful interactions.

Docker socket exposure

If the Docker socket is exposed inside the container, you can fully control the host Docker daemon.

Sysfs and procfs

Inspect these to understand namespace isolation, cgroups, and host-visible paths.

Common Privilege Escalation Techniques
Privileged containers

If a container is launched with the privileged flag, it has almost unrestricted host access. You can load kernel modules, access devices, or modify the host filesystem.

Mounted Docker socket

Access to the Docker socket means full access to the host. You can spin up a container with host-level privileges.

Writable host directories

If a host directory such as /etc or /root is mounted, you can modify host files and add backdoors.

Capabilities misuse

Capabilities like CAP_SYS_ADMIN, CAP_SYS_MODULE, or CAP_SYS_PTRACE can lead to host escape. CAP_SYS_ADMIN is especially equivalent to root in many situations.

Host namespace access

If the container is given host namespaces, such as host PID or host network namespaces, the isolation breaks and you can interact with host processes.

Device mounts

If devices such as /dev/sda or /dev/kmsg are exposed, they can be abused to write to disks or kernel logs.

Kernel exploit inside the container

Since containers share the host kernel, exploiting vulnerable kernel versions inside the container compromises the host.

Misconfigured LXC containers

LXC containers with weak AppArmor or unconfined settings can allow escaping to the host system.

High-Value Enumeration Commands

Check user and privileges
whoami
id

Check mounts
mount
cat /proc/mounts

Check capabilities
capsh --print
getcap -r /

Check Docker socket
ls -l /var/run/docker.sock

Check namespaces
ls -la /proc/self/ns

Check environment
env

Check host interaction potential
ls /host
ls /mnt
ls /dev

Living-off-the-Land Techniques
Using host-exposed binaries

If the host binary paths are mounted, you can use standard host tools to move or modify files.

Using built-in interpreters

Shells, Python, and other interpreters can manipulate the mounted host filesystem without adding extra tools.

Using Docker from inside the container

If the socket is exposed, docker commands allow you to spawn new containers with full privileges.

Defensive Awareness
Avoid noisy checks

Mass scanning or enumeration creates logs and anomalies.

Examine only what is necessary

Accessing unknown device files or kernel interfaces may trigger alerts.

Avoid container restarts

Restarts sometimes trigger logging or security events.

Cleanup

Remove any files created inside host-mounted paths or logs touched during testing.

Building a Clean Escalation Path
Step 1: Enumerate container setup

Check user, mounts, capabilities, namespaces, and devices.

Step 2: Identify breakout vectors

Focus on privileged flags, Docker socket access, and writable host directories.

Step 3: Confirm isolation level

Decide whether the container is heavily isolated or already close to the host.

Step 4: Execute minimal breakout action

Use the smallest possible step to gain host-level access.

Step 5: Validate privilege

Confirm that you transitioned from container space to host control.

Step 6: Clean traces

Remove modifications or files in mounted directories.

Summary

Container privilege escalation depends on how much the container exposes of the host environment. Misconfigured mounts, overprivileged capabilities, Docker socket exposure, and privileged flags are the main breakout points. With structured enumeration and careful interaction, you can reliably identify and exploit weaknesses for host-level escalation.
