# Trusts and Their Security Impact in Active Directory

Trust relationships define how domains and forests communicate.  
They also extend the attack surface across the entire environment.

---

## 1. What a Trust Is
A trust relationship allows authentication and authorization to flow between two domains or forests.

Types:
- Parent-child trust  
- Tree-root trust  
- External trust  
- Forest trust  
- Shortcut trust  

---

## 2. Trust Direction
Trusts can be:

### One-way  
Domain A trusts Domain B → Users in B can access A.

### Two-way  
Both domains trust each other → Identity flows both ways.

Trust direction defines how far privilege can extend.

---

## 3. Security Considerations
### a. Shared Authentication Surface  
If Domain B is weak, Domain A becomes indirectly exposed.

### b. Extended Privilege Paths  
Group membership or ACLs across domains may create unexpected privilege escalation paths.

### c. Forest-Level Trusts  
A weak forest can impact an entire enterprise.

### d. SID Filtering  
If not properly enforced, SID history may be abused through trusts.

---

## 4. Cross-Forest Identity
Universal groups, global catalogs, and federation services all introduce trust-based risks.

---

## 5. Design Principles
- Avoid unnecessary external trusts  
- Treat forests as security boundaries  
- Keep privilege identities scoped within their domain  
- Audit trust relationships regularly  

---

## Summary
Trusts connect identity systems — and therefore connect their risks as well. Good trust design isolates problems instead of spreading them.
