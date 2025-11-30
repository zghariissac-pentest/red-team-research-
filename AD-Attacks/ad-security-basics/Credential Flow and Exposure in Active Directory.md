# Credential Flow and Exposure in Active Directory

Understanding how credentials move through a domain is crucial for assessing exposure and strengthening security.

---

## 1. Where Credentials Live
Credentials appear in multiple places:

- Authentication tickets (Kerberos)
- NTLM challenge/response values
- Password hashes stored on DCs
- Cached credentials on clients
- Service account passwords
- Session tokens on servers

Each location is a potential exposure point.

---

## 2. How Credentials Move
During normal use:

1. User logs in  
2. Machine contacts a Domain Controller  
3. A Kerberos or NTLM token is issued  
4. User accesses multiple resources  
5. Credentials or tokens may be cached  

This creates predictable credential paths.

---

## 3. High-Risk Scenarios
Credentials become more exposed when:

- Privileged users log into low-trust machines  
- RDP sessions remain active  
- Service accounts run on many servers  
- Passwords are stored in scripts or scheduled tasks  
- Multiple applications share the same service account  

---

## 4. Credential Types
### Passwords  
For interactive logins, services, or applications.

### Hashes  
Stored on DCs and cached on machines.

### Kerberos tickets  
Stored in memory for Single Sign-On.

### Tokens  
Access tokens for running processes.

---

## 5. Minimizing Exposure
- Limit usage of privileged accounts  
- Enforce strong password policies  
- Use separate accounts for daily admin tasks  
- Segment service accounts  
- Reduce credential caching  

---

## Summary
Credential flow is predictable — and so is credential exposure.  
Understanding this helps secure identity across the domain.
