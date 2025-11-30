# GPO Security Basics

Group Policy Objects (GPOs) define configuration across the domain.  
Misconfigurations here affect both security and stability.

---

## 1. GPO Structure
A GPO consists of:

- GPC (Group Policy Container) — stored in AD  
- GPT (Group Policy Template) — stored in SYSVOL  

Both must be secured.

---

## 2. GPO Linking
GPOs can apply to:

- Sites  
- Domains  
- OUs  

Incorrect linking often applies settings to unintended targets.

---

## 3. GPO Inheritance & Precedence
Order of processing:  
**Local → Site → Domain → OU**

This can override security settings if not carefully designed.

---

## 4. GPO Permissions
A secure GPO requires:

- Restricted “Edit” permissions  
- No write access for standard users  
- Read permissions only where needed  
- GPO version control  

Weak ACLs allow unauthorized policy modifications.

---

## 5. Security-Related GPO Settings
Common areas impacting security:

- Password policies  
- Account lockout  
- Audit configuration  
- Firewall & network restrictions  
- User rights assignments  
- UAC and device controls  

---

## 6. SYSVOL Security
GPOs rely on SYSVOL replication.

Risks include:

- Unauthorized modifications  
- Accidental overwrites  
- Poor file permissions  

---

## Summary
Securing GPOs requires strict permissions, structured linking, and consistent auditing.  
A single misconfigured GPO can compromise the entire domain.
