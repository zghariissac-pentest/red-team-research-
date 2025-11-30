# Active Directory Attack Surface Overview

## 1. Introduction
Active Directory creates one of the largest attack surfaces inside enterprise networks.  
Not because AD is weak, but because it is complex, deeply integrated, and full of moving parts.

Understanding the attack surface is the first step toward securing it.

---

## 2. Identity & Authentication Surface
AD is the central identity layer, which means:

- Accounts (users, computers, service accounts)
- Authentication protocols (Kerberos, NTLM)
- Password policies
- Tickets and tokens
- Credential caching

Any weakness in these elements increases exposure.

---

## 3. Authorization Surface
Authorization defines *what* an authenticated user can access:

- Groups (local, global, universal)
- Privileged groups (Domain Admins, Enterprise Admins)
- ACLs on AD objects
- GPO permissions
- File share permissions

Misconfigurations here often lead to unintended privilege.

---

## 4. Infrastructure & Replication Surface
The AD engine itself becomes part of the attack surface:

- Domain Controllers
- SYSVOL content
- Replication traffic
- Time synchronization
- DNS records for services

If any component is weak, the entire identity infrastructure is at risk.

---

## 5. Application & Service Layer
AD integrates with:

- Servers
- Databases
- Web apps
- VPNs
- File services
- Cloud connectors

Each integration increases exposure.

---

## 6. Trust Relationships
Trusts extend the attack surface beyond a single domain or forest.  
A weakness in one domain can become a weakness everywhere.

---

## 7. Human & Operational Surface
Even strong technical configurations can be undermined by:

- Admin mistakes
- Over-privileged accounts
- Poor delegation
- Lack of auditing
- Mismanaged service accounts

---

## Summary
The AD attack surface is the combination of identity, permissions, infrastructure, integrations, and human operations. Securing AD starts by understanding how these layers interact — and how a single weak area can compromise the entire domain.
