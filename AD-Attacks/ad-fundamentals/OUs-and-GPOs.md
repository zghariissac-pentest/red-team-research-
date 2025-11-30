# Organizational Units (OUs) & Group Policy Objects (GPOs)

OUs and GPOs define structure, management, and policy enforcement across an Active Directory domain.

---

## 1. What Are OUs?
Organizational Units allow administrators to:
- Organize users & computers  
- Delegate permissions  
- Apply group policies selectively  
- Segment administrative boundaries  

OUs can be nested and reflect:
- Departments  
- Locations  
- Security boundaries  
- Function-based structures  

---

## 2. Group Policy Objects (GPOs)
GPOs provide centralized configuration management.

### GPOs Manage:
- Security policies  
- Password policies  
- Software restrictions  
- Mapping drives/printers  
- Firewall rules  
- Login scripts  
- Hardening configurations  

---

## 3. GPO Processing Order
Order of application (last wins):
1. **Local Policy**  
2. **Site Policy**  
3. **Domain Policy**  
4. **OU Policy**  
5. **Nested OUs**

---

## 4. Linking OUs and GPOs
GPOs **do not apply** unless linked to:
- Site  
- Domain  
- OU  

Users inherit GPOs based on their **OU location**.

---

## 5. Security Considerations
- Misconfigured OUs allow privilege escalation  
- GPO delegation can expose admin privileges  
- Unsecured SYSVOL exposes policy data  

---

## 6. Why It Matters for Red/Blue Teams
- Attackers abuse GPO rights to push malware/payloads  
- Defenders use GPOs for hardening and baselining  
