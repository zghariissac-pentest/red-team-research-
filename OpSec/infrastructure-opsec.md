# Infrastructure OPSEC

Infrastructure opsec focuses on minimizing the technical fingerprints that link your operational assets back to you or your team. Every server, domain, and communication channel you use becomes part of your attack surface. Red team operations rely on clean, compartmentalized, and deniable infrastructure. The goal is to remove exploitable patterns and avoid detectable behavior that creates attribution.

Good infrastructure OpSec isn't about hiding forever. It is about reducing correlation during the operation window and eliminating anything that ties separate phases together. Mistakes in this stage are usually irreversible because infrastructure artifacts are long‑lived and easily logged by external systems.

## Infrastructure lifecycle

Operational infrastructure follows a predictable lifecycle. Managing this cycle properly ensures nothing survives longer than it should and no asset remains linked to multiple operations.

Provisioning
Configuration
Use
Rotation
Decommissioning

Provisioning must be clean, anonymous, and isolated from your personal identity. Configuration must follow strict minimalism to avoid noisy services. Use must follow the operational purpose only with no out‑of‑scope actions. Rotation must happen before exposure accumulates. Decommissioning must include wiping logs and never reusing assets.

## Isolation principles

Infrastructure isolation is the core of OpSec. Never mix identities, tools, or objectives on the same asset. Isolation prevents correlation attacks where defenders connect multiple actions back to a single origin.

Identity isolation means using separate payment methods, separate accounts, and separate access credentials for each project. Infrastructure isolation means separate VPS providers, separate domains, and separate C2 servers. Knowledge isolation means limiting who knows which assets belong to the operation. Failure in one layer should not expose the others.

Operational infrastructure should be treated as consumable resources. Expect every component to be burned and design the environment so losing a single asset does not compromise the full operation.

## VPS selection criteria

A VPS provider becomes part of your attribution chain. Picking the wrong provider or using the wrong payment method can expose the entire project. Providers differ in logging behavior, verification requirements, and traffic scrutiny.

A good operational VPS has minimal identity verification, accepts anonymous or low‑attribution payment, and does not aggressively inspect traffic. Avoid providers that require government ID or phone verification. Avoid providers with strict abuse handling or automated blocking. Prefer regions with strong privacy laws, neutral jurisdictions, or historically low cooperation with external investigations.

Never use a single provider across all phases. Rotate providers for redirectors, staging servers, and C2 nodes. Using the same company for everything creates recognizable behavioral patterns.

## Clean networking

Network traffic is what defenders see first. Clean networking reduces noise and limits artifacts that may correlate actions. Infrastructure should never reveal default configurations or unnecessary services.

Remove default banners, disable unused ports, and minimize exposed services. Do not host unrelated files, do not test tools on operational servers, and do not browse the web from C2 infrastructure. Every packet should match a believable purpose. Keep metadata clean by setting proper time zones, removing default hostnames, and avoiding unique configurations.

Outbound traffic must also stay clean. Avoid updating packages during operations because update mirrors leak information about the server’s region and behavior. Avoid external API calls that create logs on third‑party services. Avoid using infrastructure for scanning unless it is designed for that role.

## Domain opsec

Domains are often the most visible part of your infrastructure. Bad domain choices create instant suspicion. Good domain OpSec focuses on blending in.

Pick domains that match the theme of the target or look like normal business domains. Avoid rare TLDs, cheap-looking domains, or names that reveal a technical purpose. Use privacy-protecting WHOIS services. Never register all domains with the same email or provider.

Do not reuse domains across operations. Never reuse subdomains. Keep DNS records minimal and consistent. Avoid fast-changing DNS values that look suspicious. Make redirection chains clean and simple, without unnecessary layers.

## Access hygiene

How you access infrastructure is part of your fingerprint. Most attribution happens because operators interact with servers in predictable or sloppy ways.

Never connect directly from a home IP. Never reuse SSH keys or agent configurations across machines. Do not upload your personal dotfiles or tools. Do not use your local environment to pivot into infrastructure. Every access point must go through a designated operational tunnel or VPN.

Log in with unique users per infrastructure tier. Disable password logins. Restrict SSH to known operational entry points. Never run commands that reveal your local time zone or language settings.

## Tooling separation

Tools leak metadata. Their execution patterns, filenames, and behaviors can reveal the operator. Infrastructure OpSec requires separating tools across roles.

Recon servers should only run scanning tools. Staging servers should only serve payloads. C2 servers should only handle communication. Avoid running multiple tool categories on a single asset. This reduces correlation and limits forensic evidence in case of a compromise.

Use containerized environments when possible to avoid contaminating the host system with artifacts. Build tools in isolated environments, not on operational servers. Keep versions consistent and remove compilation traces.

## Logging and artifacts

Logs accumulate silently. Many operators forget they exist until it is too late. Infrastructure OpSec requires minimizing logs at every layer.

Disable unneeded logging services. Rotate logs aggressively. Store no long-term data on operational servers. Never write payloads to disk unless necessary. Avoid generating temporary files with identifiable names.

Third-party logs are harder to control. DNS logs, CDN logs, and provider logs can persist long after you delete the server. Reduce exposure by minimizing the external services involved in the operation.

## Burn strategy

Every operation should include a clean burn strategy. Infrastructure must be disposable. Once exposed, it should be immediately shut down and wiped.

Burning infrastructure means deleting VPS instances, removing domains, wiping storage, and destroying keys. Do not reuse anything from a burned asset. Do not recycle IP addresses or rely on provider reclamation. Treat every asset as permanently toxic once exposed.

A good burn strategy ensures the operation leaves no long-term footprint that can be tied back to the team or previous engagements
