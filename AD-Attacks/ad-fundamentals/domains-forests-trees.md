
# Domains, Forests, and Trees in Active Directory

Active Directory uses a hierarchical structure to organize identity and authentication boundaries.

---

## 1. What Is a Domain?
A domain is the basic administrative/security boundary.  
It contains:
- Users  
- Computers  
- GPOs  
- Policies  
- Authentication services  

Each domain has:
- Its own **Domain Controller(s)**  
- Its own **SID namespace**  

---

## 2. What Is a Tree?
A tree is a group of domains in a contiguous namespace.

Example:
- corp.local  
- eu.corp.local  
- hr.eu.corp.local  

Domains in a tree have **two-way trust** automatically.

---

## 3. What Is a Forest?
A forest is the **top-level security boundary** in AD.
It includes:
- Multiple trees  
- Multiple domains  
- A shared schema  
- A shared global catalog  

### Forest = **highest trust boundary**  
Different forests do *not* trust each other unless manually connected.

---

## 4. Trusts
Trusts define how authentication flows between domains/forests.

Types:
- Parent-child (automatic)  
- Tree-root trust (automatic)  
- External trust  
- Forest trust  
- Shortcut trust  

---

## 5. Security Boundaries
| Level | Security Boundary | Notes |
|-------|-------------------|-------|
| **Forest** | Yes | True isolation boundary |
| **Domain** | Partial | Administrative, not full isolation |
| **OU** | No | Delegation only |

---

## 6. Why Understanding This Matters
- Helps map attack paths  
- Identifies trust-based weaknesses  
- Shows where credentials propagate  
- Determines where privilege escalation is restricted or allowed  
