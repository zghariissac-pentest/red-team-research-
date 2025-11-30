# BloodHound data collection (SharpHound)  
A complete and clean guide for collecting AD data for BloodHound using PowerShell (SharpHound), Python, or compiled binaries.

---

## 1. Introduction
BloodHound maps relationships in Active Directory using data collected by **SharpHound**.  
This file provides a full set of safe and practical commands for recon, with OPSEC notes included.

---

## 2. Import SharpHound (PowerShell)
```powershell
Import-Module .\SharpHound.ps1
```
### verify :
```
Get-Help Invoke-BloodHound
```
# Collect all data 
```
Invoke-BloodHound -CollectionMethod All -OutputDirectory .\loot\
```
this a complete collection method

# Recommended (stealthy) collection
```
Invoke-BloodHound -CollectionMethod Session,SessionLoop,ACL,Trusts,RDP -OutputDirectory .\loot\
```
Minimal noise, still useful for privilege escalation.

# Common targeted collection 
## ACL only : 
```
Invoke-BloodHound -CollectionMethod ACL -OutputDirectory .\loot\
```
## sessions only :
```
Invoke-BloodHound -CollectionMethod Session -OutputDirectory .\loot\
```
## local admin collection 
```
Invoke-BloodHound -CollectionMethod LocalAdmin -OutputDirectory .\loot\
```

## Group admin collection 
```
Invoke-BloodHound -CollectionMethod LocalAdmin -OutputDirectory .\loot\
```
## group membership 
```
Invoke-BloodHound -CollectionMethod Group -OutputDirectory .\loot\
```
# Collection using EXE binary 
if you cannot load powershell modules :
```
.\SharpHound.exe --collectionmethod All --outputdirectory loot
```
## stealth mode :
```
.\SharpHound.exe --collectionmethod ACL,Session --ldapport 389
```
# Python bloodhound (linux)
```
bloodhound-python -d <domain> -u <user> -p <pass> -dc <DC> -ns <nameserver> -c All
```
## examples :
```
bloodhound-python -d lab.local -u bob -p Pass123 -dc dc01.lab.local -c All
```
### stealthy :
```
bloodhound-python -d lab.local -u bob -p Pass123 -dc dc01.lab.local -c acl,trusts
```
# Trust enumeration :
```
Invoke-BloodHound -CollectionMethod Trusts -OutputDirectory .\loot\
```
# output files 
Bloodhound generates :
groups.json
users.json
computers.json
domains.json
acls.json
sessions.json
gpos.json

#### zip them :
```
Compress-Archive -Path .\loot\* -DestinationPath bloodhound.zip
```
# opsec notes :
SharpHound can trigger Sysmon Event ID 3, 11, 5145, 4662 depending on collection method.
Avoid running All on monitored domains.
SessionLoop causes continuous LDAP queries (noisy).
Use ACL or Trusts only for stealth operations.

# here's a quick cheatsheet: 
```
# Stealth
Invoke-BloodHound -CollectionMethod ACL,Session -OutputDirectory loot

# Full
Invoke-BloodHound -CollectionMethod All -OutputDirectory loot

# Linux
bloodhound-python -d corp.local -u admin -p Pass123 -c All
```
































