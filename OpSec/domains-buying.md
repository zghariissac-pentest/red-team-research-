# Domains buying

Buying domains for red team operations requires strict OpSec discipline. A domain becomes one of the most visible components of your infrastructure and is often the first element defenders investigate. The goal is to acquire and configure domains in a way that avoids attribution, blends with normal internet behavior, and supports the operational mission.

## Domain purpose

A domain must match the intended role in the operation. It can be used for phishing, payload delivery, redirectors, or command and control. Each purpose demands a different level of realism and different naming patterns. Choosing the wrong domain for the wrong task increases suspicion and may compromise the entire operation.

Phishing domains require maximum legitimacy and high-quality appearance. Payload delivery domains need stability and neutrality. Redirector and C2 domains should be minimalistic and not attract attention.

## Opsec principles for domain acquisition

When buying domains, the priority is to avoid linking the purchase to your real identity. You must use separate accounts, isolated payment methods, and a clean environment.

Use unique registrars for different operations. Do not buy all domains from the same vendor. Avoid registrars that require identity verification or additional documentation. Use WHOIS privacy for every domain to hide personal information. Never reuse contact emails across domains or projects.

Payment should not expose personal financial accounts. Use low-attribution payment methods that match the level of needed anonymity for the engagement. Avoid mixing personal browsing or login sessions with operational domain purchases.

## Choosing the right domain name

A domain name must blend in and appear natural. It should not look auto-generated, suspicious, or related to hacking tools. The domain should match the theme of the target or a legitimate service category.

Avoid rare TLDs, cheaply priced domains, or TLDs that are heavily associated with malicious activity. Avoid numbers, random characters, or overly technical names. Prefer neutral industry themes or names that resemble real organizations.

The domain length should be moderate. Very short or very long domains stand out. Subdomains should be realistic and connected to the purpose of the operation.

## DNS and provider opsec

DNS records reveal a lot about your infrastructure. Keep them minimal and consistent with normal organizations.

Use A, AAAA, and MX records only when needed. Avoid exposing unnecessary TXT or SRV records. Ensure DNS does not change too frequently as rapid changes create suspicion. Use providers with stable DNS propagation and avoid free DNS services that log aggressively.

Do not host DNS and VPS on the same provider. This avoids correlation.

## Lifetime and rotation

Domains should not live longer than the operation requires. Long-lived domains accumulate logs, passive DNS data, and associations to multiple servers over time.

Set an expiration timeline that aligns with the engagement. Once a domain is burned or no longer needed, remove all records and let it expire. Do not reuse domains across different operations or targets.

Tracking domain usage and exposure helps know when to rotate. If a domain appears in public threat feeds, it is considered compromised and should be burned immediately.

## Hosting and additional artifacts

Avoid hosting unrelated content on operational domains. Every file or service you expose becomes part of your footprint. Do not upload personal development files or leftover test data.

Use neutral hosting environments and avoid mixing operational domains with personal or business infrastructure. Keep TLS certificates clean and consistent. Never use personal certificate providers and avoid leaking real organizational names through certificate metadata
