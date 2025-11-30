# Password Policies and Risks in Active Directory

Password policies control how users authenticate.  
Weak policies open the door to mass credential compromise.

---

## 1. Components of Password Policy
A password policy defines:

- Minimum password length  
- Complexity requirements  
- Maximum password age  
- Lockout thresholds  
- History and reuse rules  

---

## 2. Common Weaknesses
- Minimum length below 10–12 characters  
- Long password lifetimes (90–180 days)  
- No lockout or very high thresholds  
- Reuse allowed  
- Shared service account passwords  
- Plaintext passwords in scripts  

---

## 3. Fine-Grained Password Policies (FGPP)
FGPP allows different password policies for different groups.

Issues arise when:
- Critical accounts use weaker policies  
- No structure in FGPP assignment  
- Admin accounts share policies with normal users  

---

## 4. Service Account Password Problems
Service accounts often have:

- Weak passwords  
- Never-expiring passwords  
- High privileges  
- Widespread usage on many machines  

This creates long-term risk.

---

## 5. Modern Recommendations
- Longer passphrases over complex short passwords  
- MFA for admin accounts  
- Password rotation for service accounts  
- Monitoring of password changes and resets  

---

## Summary
Password policies define the strength of your identity layer.  
Weak settings directly increase exposure inside the domain.
