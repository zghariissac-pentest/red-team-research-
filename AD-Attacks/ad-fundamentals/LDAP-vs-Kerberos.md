# LDAP vs Kerberos

Active Directory authentication and directory queries rely mainly on **LDAP** and **Kerberos**.  
They solve different problems.

---

## 1. What Is LDAP?
LDAP = Lightweight Directory Access Protocol  
Used for:
- Querying directory objects (users, groups, OUs…)  
- Reading attributes  
- Writing changes (if authorized)  

### LDAP Modes
| Mode | Port | Encryption |
|------|------|-----------|
| LDAP | 389 | None |
| LDAPS | 636 | TLS/SSL |

---

## 2. What Is Kerberos?
Kerberos is the **default authentication protocol** in AD.  
Provides:
- Mutual authentication  
- Ticket-based access  
- Time-sensitive security (5-minute skew rule)

### Kerberos Components
- **KDC** (Key Distribution Center)  
- **AS** (Authentication Service)  
- **TGS** (Ticket Granting Service)  
- **TGT** (Ticket Granting Ticket)  

---

## 3. When AD Uses LDAP vs Kerberos

| Action | Protocol |
|--------|----------|
| Logging in | Kerberos |
| Querying AD | LDAP |
| Checking group membership | LDAP |
| Getting access to a service | Kerberos |
| Updating user attributes | LDAP |

---

## 4. Weaknesses & Security Notes

### LDAP Weaknesses
- Clear-text if not using LDAPS  
- Susceptible to relaying if poorly configured  

### Kerberos Weaknesses
- Time drift breaks auth  
- Kerberoasting (service tickets with weak keys)  
- AS-REP roasting (if pre-auth disabled)

---

## 5. Summary
- **LDAP = directory queries & modifications**  
- **Kerberos = secure authentication**  
- Both are deeply integrated within AD operations  
