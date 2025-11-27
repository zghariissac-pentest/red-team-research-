#!/usr/bin/env python3

import os
import subprocess

def run(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL)
        return output.decode()
    except:
        return ""

print("[+] Container escape surface scanner\n")

print("[+] Checking cgroup info")
print(run("cat /proc/1/cgroup"))

print("\n[+] Checking if running as root inside container")
print(run("id"))

print("\n[+] Checking mounted file systems")
print(run("mount"))

print("\n[+] Checking if /proc and /sys are restricted")
print(run("ls -l /proc"))
print(run("ls -l /sys"))

print("\n[+] Checking docker socket")
if os.path.exists("/var/run/docker.sock"):
    print("[!] Docker socket exposed: /var/run/docker.sock")
else:
    print("[+] Docker socket not found")

print("\n[+] Checking privileged mode indicators")
priv_indicators = [
    "/sys/kernel/security/apparmor",
    "/sys/fs/selinux",
]

for path in priv_indicators:
    print(f"{path}: {'exists' if os.path.exists(path) else 'missing'}")

print("\n[+] Checking capabilities")
print(run("capsh --print"))

print("\n[+] Checking for writable host mounts")
print(run("find / -maxdepth 3 -type d -writable 2>/dev/null"))

print("\n[+] Checking for available host devices")
print(run("ls -l /dev"))

print("\n[+] Scan complete")
print("[+] Review findings to assess breakout risk without performing exploitation")

