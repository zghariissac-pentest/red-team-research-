
# Privilege Model in Active Directory

Active Directory uses a hierarchical privilege model.  
Understanding it is essential to avoid accidental privilege escalation.

---

## 1. Types of Privileges
### Administrative privileges:
- Domain Admins
- Enterprise Admins
- Schema Admins
- Built-in Administrators

### Delegated privileges:
- OU-specific permissions
- Helpdesk or support permissions
- Application-specific rights

### Local privileges:
- Local Administrators on member servers
- Local rights on workstations

---

## 2. The Role of Groups
Groups determine privilege scope:

- **Global groups**: Assign rights within a domain  
- **Universal groups**: Used across forests  
- **Local groups**: Only on one machine  

Incorrect membership is a common root cause of privilege misalignment.

---

## 3. Privilege Boundaries
Important boundaries include:

- Domain boundary  
- Forest boundary  
- Privileged vs non-privileged accounts  
- Admin vs service accounts  

Blurring boundaries leads to escalation paths.

---

## 4. Delegation Models
Delegation gives limited access without full admin rights.

Examples of delegation:
- Password reset rights  
- Join computer to domain  
- Manage OU objects  

Poor delegation often enables lateral privilege movement.

---

## 5. Tiered Administration
A well-designed privilege model uses tiers:

- **Tier 0**: Domain Controllers, AD admins  
- **Tier 1**: Servers and infrastructure  
- **Tier 2**: Workstations and standard users  

Admins must not cross tiers.

---

## Summary
AD privilege modeling ensures controlled access and prevents escalation. Good privilege design is the foundation of a secure directory environment.
