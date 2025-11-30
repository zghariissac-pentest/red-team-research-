# Full windows privilege escalation cheat-sheet for beginners 
## System enumeration (always first):
Just to know who you are and where you are and what are you going to exploit :
#### basic system info :
```
systeminfo
hostname
whoami /all
ipconfig /all
```
#### check users , groups and privileges :
```
net user
net user <username>
net localgroup
net localgroup administrators
whoami /groups
```
#### check running processes : 
```
tasklist /svc
wmic process list full
```
#### check installed programs and hotfixes :
```
wmic product get name,version
wmic qfe
```
#### check services :
```
sc query
sc qc <service>
```
## Commen privilege escalation vectors :
#### Run : 
```
systeminfo
```
Copy the output into:
Windows-Exploit-Suggester
wesng
Search for known escalation exploits (MS10-015, MS16-032, etc.)

## Weak services :
If a service runs as SYSTEM but you can modify it , this means an easy escalation.

#### 1. Check service details:
```
sc qc <servicename>
```
Look for:
BINARY_PATH_NAME . can you modify it?
SERVICE_START_NAME : LocalSystem
Weak permissions (F, C) on folders or .exe



























