# PowerView Enumeration Cheatsheet
A practical, clean, and field-tested cheat sheet for enumerating Active Directory using **PowerView** (PowerSploit).  
All commands are organized by objective and include expected output + usage notes.

---

## 1. Import PowerView
```powershell
Import-Module .\PowerView.ps1
```
## Domain information :
```
Get-NetDomain
Get-NetDomainController
Get-NetForest
Get-NetForestDomain
Get-NetForestTrust
```
## User information :
```
Get-NetUser
Get-NetUser -UserName <user>
Get-NetUser | Select cn, samaccountname, description
Get-NetUser | ?{$_.description -ne $null}
```
### Find users with SPNs (useful for Kerberoasting):
```
Get-NetUser -SPN
```
## Group Enumeration
```
Get-NetGroup
Get-NetGroup -GroupName "Domain Admins"
Get-NetGroupMember -GroupName "Domain Admins"
Get-NetGroup -AdminCount 1
```
## Computer enumeration 
```
Get-NetComputer
Get-NetComputer -OperatingSystem *Server*
Get-NetComputer -FullData
```
## OU enumeration 
```
Get-NetOU
Get-NetOU | Select name, distinguishedname
```
## GPO enumeration 
```
Get-NetGPO
Get-NetGPO -Computer <computer>
Get-NetGPOGroup
Get-NetGPO | ?{$_.DisplayName -like "*WSUS*"}
```
## ACL / ACE Enumeration
### Enumerate ACLs on objects
```
Get-ObjectACL -SamAccountName <user/group/computer>
Get-ObjectACL -ADObject "OU=Servers,DC=lab,DC=local"
```
### Find objects you can modify
```
Invoke-ACLScanner
Invoke-ACLScanner -ResolveGUIDs
```
## Shares enumeration (SMB)
```
Invoke-ShareFinder
Invoke-ShareFinder -CheckAccess
Invoke-FileFinder -Extensions txt,doc,pdf,xlsx
```
## Trust enumeration
```
Get-NetDomainTrust
Get-NetForestTrust
```
## Local administrator access (Across Domain)
```
Find-LocalAdminAccess
```
## Session enumeration
```
Get-NetSession -Computer <target>
Get-NetLoggedOn -Computer <target>
```
## Interesting attributes (Hunting)
### Users with passwords in description
```
Get-NetUser | ? {$_.description -match "pass"}
```
### Old passwords / expired accounts
```
Get-NetUser | Select samaccountname,pwdlastset
Get-NetUser -AllowDelegation $False
```
## GPP password extraction (SYSVOL)
```
Get-GPPPassword
```
## Domain policy & kerberos settings
```
Get-DomainPolicy
(Get-DomainPolicy)."Kerberos Policy"
```
## Saved credentials discovery
```
Invoke-PowerDump
```
## Complete AD enumeration (All-in-One)
```
Invoke-EnumerateLocalAdmin
Invoke-UserHunter
Invoke-UserHunter -CheckAccess
Invoke-UserHunter -Stealth
```
## Useful filters 
```
Get-NetUser | ?{$_.pwdlastset -lt (Get-Date).AddDays(-90)}
Get-NetComputer | ?{$_.operatingsystem -match "Windows 7"}
```
## quick recon bundle 
```
Get-NetDomain
Get-NetUser
Get-NetGroup
Find-LocalAdminAccess
Invoke-ShareFinder
Get-NetDomainTrust
```
## Notes
Requires PowerShell v2-v5 depending on environment.
Ideal for pre-BloodHound light enumeration.
Avoid noisy commands on monitored environments.

