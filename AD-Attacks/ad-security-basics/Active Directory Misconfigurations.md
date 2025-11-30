# Common Active Directory Misconfigurations

Misconfigurations — not vulnerabilities — are the root of most AD compromises.  
Below are the most common weaknesses found in real environments.

---

## 1. Over-Privileged Accounts
Giving users more permissions than necessary results in:

- Excessive group membership
- Unrestricted local admins
- Service accounts with domain-level privileges

Least privilege is rarely implemented correctly.

---

## 2. Weak Password Policies
Common issues include:

- Long password lifetimes
- Short complexity requirements
- Password reuse across service accounts
- Shared admin passwords

Weak policies often allow credential guessing at scale.

---

## 3. Stale, Inactive, and Orphaned Accounts
Older AD environments accumulate:

- Disabled accounts not fully removed
- Users who left the company
- Computers not used for months

Attackers love dormant accounts.

---

## 4. Misconfigured SPNs and Service Accounts
Service accounts often have:

- High privileges
- Weak passwords
- SPNs attached to privileged objects

This expands the credential exposure surface.

---

## 5. Unsecured GPOs
GPOs sometimes allow:

- Modification by non-admins
- Linking in wrong OUs
- Poor ACL inheritance

This affects both security settings and machine behavior.

---

## 6. Poor OU and Delegation Design
Examples:

- All users/computers in one OU
- No structured delegation
- Admins performing daily tasks using privileged accounts

Bad design leads to privilege escalation risks.

---

## 7. Weak Administrative Tiering
Admins logging into low-trust machines or using personal devices for privileged tasks drastically increases exposure.

---

## Summary
Almost all AD security issues come from mismanagement, forgotten accounts, or overly permissive configurations — not from technical exploits.
