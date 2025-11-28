# ad-enum.ps1
# Basic Active Directory enumeration script template
# This script focuses on safe, read‑only operations.
# Author: (you)
# Purpose: Collect general domain info for analysis.

Write-Host "[*] Starting AD enumeration..." -ForegroundColor Cyan

# Check if AD module exists
if (-not (Get-Module -ListAvailable -Name ActiveDirectory)) {
    Write-Host "[!] ActiveDirectory module not found." -ForegroundColor Red
    return
}

Import-Module ActiveDirectory

# Retrieve domain information
Write-Host "[*] Domain Information:" -ForegroundColor Yellow
Get-ADDomain | Format-List

# List all domain controllers
Write-Host "`n[*] Domain Controllers:" -ForegroundColor Yellow
Get-ADDomainController -Filter * | Select-Object HostName, IPv4Address

# List users
Write-Host "`n[*] Users:" -ForegroundColor Yellow
Get-ADUser -Filter * -Properties * |
    Select-Object SamAccountName, Enabled, LastLogonDate

# List groups
Write-Host "`n[*] Groups:" -ForegroundColor Yellow
Get-ADGroup -Filter * | Select-Object Name, GroupScope, GroupCategory

# List computers
Write-Host "`n[*] Computers:" -ForegroundColor Yellow
Get-ADComputer -Filter * | Select-Object Name, OperatingSystem

Write-Host "`n[*] Enumeration finished." -ForegroundColor Green

