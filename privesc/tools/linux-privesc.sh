#!/bin/bash

# Basic system info
echo "[+] System info"
uname -a
cat /etc/os-release

# Current user
echo ""
echo "[+] Current user"
whoami

# Sudo permissions
echo ""
echo "[+] Sudo permissions"
sudo -l 2>/dev/null

# Users and groups
echo ""
echo "[+] Users and groups"
id
cat /etc/passwd

# Running processes
echo ""
echo "[+] Running processes"
ps aux

# Services and timers
echo ""
echo "[+] Services and timers"
systemctl list-units --type=service
systemctl list-timers

# Cron jobs
echo ""
echo "[+] Cron jobs"
ls -la /etc/cron*
cat /etc/crontab 2>/dev/null

# Writable files and folders
echo ""
echo "[+] Writable folders"
find / -writable -type d 2>/dev/null

echo ""
echo "[+] Writable files"
find / -writable -type f 2>/dev/null

# Suid binaries
echo ""
echo "[+] Suid binaries"
find / -perm -4000 -type f 2>/dev/null

# Capabilities
echo ""
echo "[+] Capabilities"
getcap -r / 2>/dev/null

# Network information
echo ""
echo "[+] Network info"
ip a
ip r
ss -tulpn

# Installed packages
echo ""
echo "[+] Installed packages"
dpkg -l 2>/dev/null || rpm -qa 2>/dev/null

# Search for credentials in config files
echo ""
echo "[+] Searching for config files with credentials"
grep -Ri "password=" /etc 2>/dev/null
grep -Ri "pass" /home 2>/dev/null

# Docker or container detection
echo ""
echo "[+] Checking for container environment"
grep -i docker /proc/1/cgroup 2>/dev/null
grep -i container /proc/1/environ 2>/dev/null

