# Opsec C2 tips
## 1) Don’t look like a C2

Use domain fronting when available.

Add random jitter instead of fixed intervals.

Match normal app traffic patterns (ports 443 / 80 / 8080).

Rotate User-Agent strings and keep them realistic.

## 2) Network behavior opsec

Keep packet sizes small and varied.

Avoid direct IP callbacks—use aged domains.

Never use new or suspicious-looking domains.

Use DNS over HTTPS when appropriate.

## 3) Infrastructure opsec

Separate components into layers:

Redirectors

Core C2 server

Logging server

Avoid hosting everything on the same IP.

Do not store logs on the same machine as the C2.

## 4) Server hardening

Disable SSH password authentication (use keys only).

Avoid default service ports when possible.

Remove banners (nginx / apache / ssh version info).

Use rate limiting and basic firewall rules.

## 5) Avoid blue team indicators

Avoid large payload transfers.

Prevent obvious process chains (e.g., powershell → curl → exe).

Minimize suspicious child processes; rely on LOLBAS carefully.

Split output into smaller chunks or compress it.

## 6) Beacon opsec

Jitter: 20–60%.

Realistic sleep intervals:

Corporate networks: 2–8 minutes

Internet-facing: 10–20 minutes

Avoid identical callback patterns for all agents.

Use unique configs per operator/machine.

## 7) Payload opsec

Use signed binaries when possible.

Strong obfuscation but not noisy or suspicious.

Reduce direct system calls.

Test behavior thoroughly before deployment.

## 8) Cloud opsec

Use reputable providers (Azure, GCP, AWS).

Match region/geolocation to the target.

Rotate IPs intelligently, not aggressively.

Avoid free-tier cloud hosts.

## 9) Logging opsec

Log only on redirectors, not the core C2.

Avoid storing sensitive command output.

Use encrypted logs with rotation.

Separate operational logs from infrastructure logs.

## 10) Human opsec

Never operate from your personal device.

Shutdown and clean infrastructure after operations.

Use separate operator accounts.

Avoid exposing your real IP address anywhere.

## 11) Detection evasion

Match real TLS fingerprints (JA3/JARM).

Avoid unique or weird packet patterns.

Vary packet sizes and timing.

Deliver payloads via legitimate services (OneDrive, Google APIs).

## 12) Emergency procedures

Maintain a kill switch for agents.

Be able to rotate infrastructure quickly.

Use automated cleanup scripts.

Decommission all infrastructure after the engagement.
