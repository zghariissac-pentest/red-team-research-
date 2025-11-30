
# Authentication in Active Directory: Kerberos & NTLM

Active Directory supports two main authentication protocols:
- **Kerberos** (default)
- **NTLM** (legacy)

---

## 1. Kerberos Authentication Flow (Simplified)
1. Client asks for TGT from the KDC  
2. Client receives encrypted TGT  
3. Client requests a service ticket  
4. Access granted to the service  

### Benefits:
- Mutual authentication  
- Fast, ticket-based  
- More secure  
- Supports delegation  

---

## 2. NTLM Authentication (Legacy)
Based on:
- Challenge/response  
- No mutual authentication  
- Weak against relaying  
- Still widely supported for compatibility

---

## 3. When AD Uses NTLM Automatically
- Cannot contact a DC  
- Kerberos fails (time drift / SPN issues)  
- Legacy applications  
- Workgroup environments  

---

## 4. Security Concerns

### NTLM
- Relaying attacks  
- Pass-the-Hash  
- No server validation  

### Kerberos
- Kerberoasting  
- AS-REP roasting  
- Golden/diamond ticket abuse  

---

## 5. Reducing NTLM Usage
- Enable NTLM auditing  
- Disable NTLM where possible  
- Enforce Kerberos-only services  
- Fix SPN misconfigurations  

---

*Understanding both is crucial for analyzing authentication weaknesses in enterprise AD environments.*
