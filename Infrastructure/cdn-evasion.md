# Cdn evasion

Content delivery networks offer strong cover for red team operations. They provide high reputation endpoints, global distribution, and traffic blending with legitimate services. Using a CDN correctly helps reduce detection and makes infrastructure appear normal.

## Why use a CDN

A CDN hides the origin server and places your redirector or content behind a large provider. Defenders often trust traffic from well known CDN networks. This reduces reputation based blocking and makes fingerprinting more difficult.

## CDN as a shield

When traffic passes through a CDN, the origin IP is never exposed to the target. The CDN becomes the only visible endpoint. This improves anonymity and allows infrastructure rotation without changing the public facing domain.

## Traffic normalization

CDNs modify or normalize some headers and request patterns. This blending helps your traffic look similar to regular web browsing. Payload staging and callback traffic can take advantage of this to appear less suspicious.

## Configuration choices

Using a CDN requires selecting the right mode. Some modes forward requests directly to the origin. Others cache static content. For red team operations, disable caching for dynamic content to avoid exposing payloads unintentionally. Ensure HTTPS is enabled to prevent inspection between the target and the CDN.

## Host header control

Many CDNs allow rewriting or controlling the host header. Use this feature to hide the real backend domain name. Proper host header routing prevents the backend server from leaking its hostname or internal configuration.

## Path and pattern filtering

CDNs allow request rules that block specific patterns, restrict methods, or enforce rate limits. Use these rules to filter out scanners, bots, and abnormal traffic. Only allow the required paths used by payloads or C2 channels.

## Using CDN for redirectors

A redirector behind a CDN becomes much harder to fingerprint. The CDN absorbs bulk scans and drops abnormal traffic. The redirector only sees traffic that has already passed through CDN validation. This lowers exposure and enhances stealth.

## Operational risks

Some CDNs log traffic, including headers and IP addresses. Review the provider’s policies before use. Avoid using the same CDN account for multiple operations. Disable features that may rewrite content in unexpected ways. Test configuration carefully before deployment to avoid breaking payload communication.

## Cleanup strategy

After the operation, remove the CDN configuration and delete the associated domain entries. Do not keep stale DNS records pointing to old infrastructure. This prevents correlation across different engagements
