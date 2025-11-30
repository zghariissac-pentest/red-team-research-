# Overview:
LDAP (Lightweight Directory Access Protocol) is the core query protocol used to read Active Directory data (users, groups, computers, SPNs, attributes). LDAP enumeration is the process of discovering AD structure and assets using LDAP-capable tools and techniques. This file focuses on defensive-minded, professional enumeration that you can present in a repo for learners and practitioners.
## Ethical reminder: 
run these techniques only in labs or environments where you have explicit authorization.

# Goals and scope :
## Primary goals

Identify domain users, groups, computers, trusts, GPOs, SPNs, ACLs, shared folders and other LDAP-exposed objects.
Map relationships that matter for later steps (credential access, lateral movement, escalation).
Produce outputs useful to both offensive and defensive workflows (CSV, JSON, BloodHound ingests).

## Out of scope
Credential theft techniques (except read-only queries).
Active exploitation instructions. (Focus is enumeration & detection.)

# Prerequisites & safety notes
## Prerequisites
Network access to an AD Domain Controller or LDAP-reachable server (TCP 389/636 or LDAPS).
Tools installed (see Tools section).
For PowerShell: AD module or PowerView availability (lab/authorized environment).

## Safety
Use read-only queries unless explicitly indicated otherwise.

# 4 Quick LDAP primer (concepts)
DN (Distinguished Name): unique path (CN=alice,OU=Users,DC=corp,DC=local).
DNSSRV / SRV records: locate domain controllers.
Base DN / search base: starting point for searches.
Attributes: e.g., sAMAccountName, userPrincipalName, servicePrincipalName (SPN), memberOf.
Filter syntax: RFC 4515 style; e.g., (objectClass=user) or (&(objectClass=user)(!(objectClass=computer))).
LDAP over SSL (LDAPS): TCP 636; recommended for confidentiality.
Anonymous bind vs authenticated bind: many domains allow read access to non-sensitive attributes by default (pre-Windows Server 2008R2 ACLs).

# Tools you need :
PowerShell
Get-ADUser / Get-ADComputer (AD module)
PowerView (PowerSploit/PowerView in Empire / standalone)
BloodHound / SharpHound (collection)
ldapsearch (OpenLDAP client) — Linux/macOS
ldapdomaindump
ADRecon
Impacket (e.g., GetADUsers.py, GetNPUsers.py tools)
samba-tool (if Samba / AD DC)
Python ldap libraries (for scripts)
jq / csvkit (for parsing outputs)

# Recon workflow 
Discover domain controllers and LDAP endpoints (DNS SRV).
Basic enumeration: domain, schema, users, groups, computers.
identify high-value targets: SPNs, domain admins, service accounts, privileged groups.
Map relationships: group membership, admin-to, ACLs that allow write/replication.
Collect artifacts for BloodHound and offline analysis.
Document findings: CSV/JSON outputs, screenshots, checklists.

# Common commands and examples
## Discovering domain controllers (DNS)
```
# Linux (dig)
dig _ldap._tcp.dc._msdcs.corp.local SRV +short

# PowerShell
Resolve-DnsName -Type SRV _ldap._tcp.dc._msdcs.corp.local
```
## Simple ldapsearch (anonymous / unauthenticated)
```
# Find domain naming context (rootDSE)
ldapsearch -x -H ldap://dc.corp.local -s base -b "" "(objectClass=*)" namingContexts

# Search users (shallow)
ldapsearch -x -H ldap://dc.corp.local -b "DC=corp,DC=local" "(&(objectCategory=person)(objectClass=user))" sAMAccountName displayName mail
```
## ldapsearch with bind (user/pass)
```
ldapsearch -x -H ldaps://dc.corp.local -D "corp\\alice" -W -b "DC=corp,DC=local" "(objectClass=user)" sAMAccountName userPrincipalName
```
## Enumerate users and common attributes (PowerShell)
```
# With ActiveDirectory module (run on a system that has RSAT or on DC)
Get-ADUser -Filter * -Properties samAccountName,mail,userPrincipalName,memberOf,whenCreated | Select-Object Name,sAMAccountName,UserPrincipalName,mail,whenCreated

# PowerView (PowerShell)
Import-Module .\PowerView.ps1
Get-NetUser -Domain corp.local | ft Name,SamAccountName,Description
```
## Enumerate computers (PowerShell)
```
Get-ADComputer -Filter * -Properties OperatingSystem,LastLogonDate | Select Name,OperatingSystem,LastLogonDate
```
## Find SPNs (Kerberos service principals)
```
# PowerView
Get-NetSPN | ft Identity,SPN

# ldapsearch example
ldapsearch -x -H ldap://dc.corp.local -b "DC=corp,DC=local" "(servicePrincipalName=*)" sAMAccountName servicePrincipalName
```
## Find accounts allowed to replicate or DCSync (ACLs)
```
# PowerView example: find accounts with WriteDacl or Replication privileges
Get-ObjectAcl -SamAccountName 'DC=corg DC=local' -ResolveGUIDs | ? {$_.ObjectDN -like "*CN=Configuration*"} # high-level idea
```
actually you must know this , (ACL enumeration is detailed and requires careful parsing; see Advanced & BloodHound collection sections.)
## LDAP subtree enumeration — common useful filters
```
# All users
(&(objectCategory=person)(objectClass=user))

# Non-disabled users
(&(objectCategory=person)(objectClass=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))

# Users that can’t do Kerberos pre-auth (AS-REP roastable)
(&(objectCategory=person)(objectClass=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2))(msDS-UserAccountControl:1.2.840.113556.1.4.803:=PASSWORD_NOT_REQUIRED_OR_SIMILAR))
# Note: use specific attribute checks like DoesNotReqPreAuth in environment (use Impacket/PowerView helpers)
```

# BloodHound / SharpHound collection notes
Why BloodHound? BloodHound ingests graph data (users, groups, sessions, ACLs) to compute attack paths.
Collection methods
SharpHound.exe (C#) — runs on Windows, collects via LDAP, WMI, SMB, RPC and writes zip files for upload to BloodHound GUI.
Invoke-BloodHound (PowerShell) — PowerShell collector.

## Basic SharpHound invocation
```
# PowerShell collector
Invoke-BloodHound -CollectionMethod All -Domain corp.local -ZipFileName collection.zip

# C# SharpHound (Windows)
SharpHound.exe -c All
```
Tips
Use -c ACL to specifically collect ACLs (heavy but high value).
Use --ExcludeDCs in large environments to reduce noise.
Always run collectors on hosts inside the domain to get session data.
Post-collection
Import .zip to BloodHound GUI.
Run standard queries (Shortest Path to Domain Admins, Find Principals with Unconstrained Delegation, etc.).

# Advanced LDAP queries & tips
## 9.1 Paging control & large results
Large directories require paged LDAP results to avoid truncation:
ldapsearch supports -E pr=1000/noprompt or use tools that handle paging automatically.
## 9.2 Reading adminCount and protected accounts
adminCount=1 often indicates protected privileged accounts (members of privileged groups).
Filter: (adminCount=1)
## 9.3  Enumerating GPOs and SYSVOL

GPOs are stored in CN=Policies,CN=System,DC=... and scripts/prefs in SYSVOL share. Enumerate via LDAP and \\domain\SYSVOL.

## 9.4 Querying lastLogon / lastLogonTimestamp

lastLogon is per-DC; lastLogonTimestamp is replicated (approximate). Combine for accuracy.

## 9.5 Query for unconstrained delegation
Look for userAccountControl flags or msDS-AllowedToActOnBehalfOfOtherIdentity and trust attributes.

## 9.6 LDAPS and Channel Binding
If LDAPS is available, prefer it. Many modern environments require LDAP signing & channel binding to mitigate relay and MITM.

# 10 Detection, logging & SIEM rules

Events to monitor

LDAP simple bind (Event ID 2889 / 1644 depending on platform) — note weak binds.

Kerberos TGS, AS requests for unusual SPNs (Event IDs 4769, 4768).
Unusual number of LDAP queries from a single account or host (possible reconnaissance).
SharpHound or PowerView command indicators (script execution logs, Process Creation events).
Suspicious WinRM/WMI usage for remote enumeration (Event IDs related to remote management).
Example SIEM detection ideas
Alert on accounts that perform > X LDAP searches/minute from a single source.
Alert on requests for many servicePrincipalName attributes across many accounts.
Alert on use of built-in enumeration tools on endpoints (powershell.exe invoking Invoke-Object modules or unusual encoded commands).
Track Get-ADUser and Get-ADComputer via PowerShell logging (Module Logging / Script Block Logging).
Event sources
Domain Controller Security logs (LDAP/AD events)
PowerShell Logging (Module Logging, ScriptBlockLogging)
Sysmon (process command lines)
Windows Event Forwarding to SIEM
ful of impact on domain controllers (avoid aggressive scans during business hours).

# 11  Remediation & hardening guidance

Access & ACLs

Harden ACLs on sensitive objects (limit who can read msDS-AllowedToActOnBehalfOfOtherIdentity, servicePrincipalName, and msDS-KeyVersionNumber).

Reduce Read access to attribute sets for non-privileged accounts where feasible.

Kerberos & SPN hardening

Remove SPNs from non-service accounts when possible.

Avoid service accounts running as domain admin.

LDAP configuration

Enforce LDAP signing & require channel binding (Microsoft guidance).

Disable anonymous LDAP binds.

Require LDAPS for remote management where possible.

Monitoring

Enable detailed PowerShell logging, Sysmon, and forward to SIEM.

Monitor for mass enumeration patterns.

Least privilege

Apply tiered access model; service accounts should be constrained and monitored.
Keep logs of actions for auditability.

# Quick-check enumeration checklist
```
[ ] Discover domain controllers (DNS SRV)
[ ] Enumerate basic domain info (domain functional level, naming contexts)
[ ] Dump all users (sAMAccountName, UPN, mail, whenCreated)
[ ] Dump all computers (OS, lastLogon)
[ ] Enumerate groups, privileged groups (Domain Admins, Enterprise Admins)
[ ] Find SPNs and service accounts
[ ] Search for accounts with no pre-auth (AS-REP roastable)
[ ] Collect ACLs for sensitive containers (Domain, Configuration, Protected Groups)
[ ] Collect data for BloodHound (SharpHound / Invoke-BloodHound)
[ ] Export outputs to CSV/JSON and document findings
[ ] Configure detection rules for excessive LDAP queries & PowerShell usage
```
don't ask me why i made it as a code , it's just look good.

# 13 Additional resources & references

BloodHound / SharpHound official docs
PowerView / PowerSploit docs
Microsoft docs: LDAP signing & channel binding guidance
Impacket repository (GetNPUsers, GetUserSPNs tools)
LDAP RFCs (RFC 4510/4511/4512/4515)

# Appendix: example scripts
## 14.1 Simple ldapsearch wrapper (bash)
```
#!/usr/bin/env bash
# simple-ldap-enum.sh: basic queries and CSV output
DC="$1"    # e.g. dc.corp.local
BASE="$2"  # e.g. DC=corp,DC=local

ldapsearch -x -H ldap://$DC -b "$BASE" "(&(objectCategory=person)(objectClass=user))" sAMAccountName userPrincipalName mail displayName | \
  awk 'BEGIN {FS=": "; OFS=","; print "sAMAccountName,userPrincipalName,mail,displayName"} \
       /^sAMAccountName:/ {u=$2} /^userPrincipalName:/ {p=$2} /^mail:/ {m=$2} /^displayName:/ {d=$2; print u,p,m,d}' > users.csv
echo "done -> users.csv"
```
## 14.2 PowerShell: export all users to CSV
```
# Export-ADUsers.ps1
Import-Module ActiveDirectory
Get-ADUser -Filter * -Properties sAMAccountName,UserPrincipalName,mail,MemberOf,whenCreated |
  Select-Object Name,sAMAccountName,UserPrincipalName,mail,whenCreated |
  Export-Csv -Path .\ADUsers.csv -NoTypeInformation
```






