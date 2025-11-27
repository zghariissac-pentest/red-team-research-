# Windows privilege escalation helper script
# Purpose:
#   Automate basic Windows privilege escalation enumeration.
#   Outputs clear results for manual analysis.

# System information
Write-Host "[+] System Info"
systeminfo

# User and group enumeration
Write-Host "`n[+] Current User"
whoami

Write-Host "`n[+] User Groups"
whoami /groups

# Checking privileged tokens
Write-Host "`n[+] Privilege Tokens"
whoami /priv

# Installed programs
Write-Host "`n[+] Installed Programs"
Get-WmiObject -Class Win32_Product | Select-Object Name, Version

# Running services (Check for unquoted Paths / Weak permissions)
Write-Host "`n[+] Services"
Get-WmiObject win32_service | Select Name, PathName, StartMode

# Startup applications
Write-Host "`n[+] Startup Apps"
Get-CimInstance Win32_StartupCommand | Select Name, Command

# Search for writable folders
Write-Host "`n[+] Writable Folders"
Get-ChildItem -Path C:\ -Recurse -ErrorAction SilentlyContinue | Where-Object {
    $_.PsIsContainer -and (Get-Acl $_.FullName).AccessToString -match "Everyone"
} | Select FullName

# Search for web config files with credentials
Write-Host "`n[+] Config Files"
Get-ChildItem -Path C:\ -Recurse -Include web.config,*.config -ErrorAction SilentlyContinue

# Scheduled tasks (privilege misconfigs)
Write-Host "`n[+] Scheduled Tasks"
schtasks /query /fo LIST /v

