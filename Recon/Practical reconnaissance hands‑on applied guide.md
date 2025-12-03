 # Practical Commands, Tools & Techniques 
 
 expanded, hands-on, but RoE-aware. Use these templates only under a signed engagement or in lab environments.

# How I structured this section

Tool categories (purpose + top picks)

Command templates (clear, annotated) , called templates because you’ll tweak them per RoE and target.

Parsing & enrichment tips (how to turn raw output into intelligence)

Automation patterns & orchestration examples (safe pipelines)

OPSEC and tuning guidance (rate limits, stealth)

Quick reference checklist

 ## 1. Tools by purpose (short lists, why to use them)

Passive OSINT

crt.sh / Certstream / Censys , certificate transparency for subdomains/SANs.

PassiveDNS (pDNS) providers , historical DNS resolution.

GitHub/GitLab search / GitHub Advanced Search / Sourcegraph , repo secrets, CI config.

Shodan / BinaryEdge (use carefully, some require subscriptions) , indexed public-facing services.

HaveIBeenPwned / Pastebin monitors / Dehashed — credential leaks (scale as allowed).

Active discovery / scanning

nmap , multi-protocol scanning, service detection, scripting (NSE).

masscan , at-scale port discovery (very noisy; use only when permitted).

httprobe / httpx / tls-scan / wafw00f , fast HTTP/TLS enumeration and WAF detection.

ffuf / gobuster / dirsearch , content discovery / directory brute forcing.

whatweb / wappalyzer / builtwith — tech fingerprinting.

Web & API analysis

Burp Suite (Professional or Community) . intercept, map, fuzz, analyze.

OWASP ZAP , alternative proxy/fuzzer.

mitmproxy / selenium  automated browser interactions or non-interactive JS rendering (use with care).

Protocol specific

enum4linux / rpcclient / smbclient — SMB/Windows enumerations.

ldapsearch , LDAP queries (if permitted).

kerberoast tooling / krb5 tools Kerberos reconnaissance (conceptual only).

smtp-user-enum / dig / host mail and DNS checks.

Automation, parsing & graphs

massdns / amass / subfinder / assetfinder , subdomain discovery.

jq / yq / awk / sed / python — parsing JSON/text outputs.

neo4j / networkx / Maltego / Gephi , relationship graphs and entity resolution.

gitleaks / truffleHog , secrets scanning in repos (good for passive hunting).

## 2. Command templates (annotated & RoE-aware)

Below are templates , replace <target>, adjust rate limits and time windows per RoE. I annotate what each flag is for. Always save output to structured files.

## 2.1 DNS & subdomain discovery (passive to active)

Certificate transparency (passive):

``` # query crt.sh for subdomains (example using curl + html parsing)
curl -s "https://crt.sh/?q=%25.example.com&output=json" -o crt_example.json
# parse names with jq:
jq -r '.[].name_value' crt_example.json | sed 's/\*\.//g' | sort -u > subdomains.txt
```
finds SANs and newly issued certs that reveal subdomains.

Passive DNS lookups (API-based; example conceptual):
``` # use your pDNS provider API to fetch historical A/AAAA records for example.com
# store as json, then extract unique IPs
```

## Active subdomain brute / discovery (massdns + amass)
```
# gather candidates using subfinder/amass then resolve with massdns (fast, parallel)
subfinder -d example.com -silent > candidates.txt
massdns -r resolvers.txt -t A -o S -w massdns_out.txt candidates.txt
cat massdns_out.txt | cut -f1 -d' ' | sort -u > alive_subs.txt
```
massdns is much faster and more reliable than simple dig loops.

## 2.2 TLS & certificate introspection

```
# httpx probes TLS, extracts SANs, status, titles, and more
cat alive_subs.txt | httpx -silent -status-code -title -tls-proto -tls-cipher -o httpx_out.txt
```
Why: fast HTTP/TLS surface mapping; helps identify admin pages, unusual TLS configs, or edge vs origin.

## 2.3 Port discovery & service fingerprinting
low noise targeted nmap : 
```
# targeted ports, service/version detection, script scan for safe NSE scripts, 1 thread and rate-limit to reduce noise
nmap -Pn -sV --version-intensity 2 --top-ports 100 -T3 --max-retries 1 --open -oA nmap_top100_example example.com
```
Flags explained:
-Pn (no host discovery if resolved IP known), -sV service detection,
--top-ports 100 common ports, -T3 sane timing, --open show only open ports, -oA output formats.

### When you need full sweep (use very carefully):
```
masscan 0.0.0.0/0 -p1-65535 --rate=1000 -oL masscan_example.txt
# then hand-picked IPs to nmap for verification
```
masscan is extremely fast but noisy; always limit scope and rate.

## 2.4 HTTP surface & directory discovery
here's a quick vhost/virtual host checks :
```
cat alive_subs.txt | while read sub; do curl -sI -L -m 10 -H "Host: $sub" "http://$ip_or_origin" | head -n 20; done
```

### Directory fuzzing (ffuf):
```
ffuf -w /path/wordlists/common.txt -u https://example.com/FUZZ -recursion -ac -o ffuf_out.json -t 40
```
-recursion and -t thread count are powerful , tune for RoE.

## 2.5 Web API enumeration (safe templates):

Collecting API endpoints via replay (log and diff):
```
# capture logged API calls with Burp or mitmproxy; then use HTTP request diffs to map unauthenticated vs authenticated behavior.
```
reveals API routes that may exist but are not exposed in UI.

## 2.6 GitHub & code artifact scanning (passive):

GH advanced search template (manual)
Search: org:company filename:.env OR filename:config site:github.com

gitleaks scan local/archived repos

```
gitleaks detect -s ./repos-archive -r gitleaks_report.json
```
find accidentally committed secrets, tokens, or config files.

## 2.7 SMB / Windows reconnaissance (conceptual):

numerate SMB shares (read-only checks):
```
# enum4linux for read-only info (domain, shares, users)
enum4linux -a target-ip > enum4linux_target.txt
```
identify shares and misconfigs; avoid brute-forcing credentials unless allowed.

## 2.8 Email & SPF/DKIM/DMARC checks:
```
dig +short TXT example.com | grep -i spf
# or use online SPF/DMARC analyzers for deeper evaluation
```
misconfigured email records can allow phishing or spoofing risks.

## Parsing, enrichment & intelligence turning:
Normalize outputs to JSON where possible (httpx, ffuf, nmap -oX then xsltproc or xml2json), store in a single assets/ DB.

Use jq to filter useful fields:
```
jq -r '.[] | select(.status==200) | .url' httpx_out.json > ok_urls.txt
```
Graph building: convert CSV/JSON into node-edge format and import to Neo4j or networkx:
Nodes: domain, ip, cert, employee, repo
Edges: resolves-to, owned-by, referenced-in
Scoring & prioritization: implement simple scores:
exposure_score = public_asset? * 3 + admin_ui? * 5 + leaked_credentials? * 10
Tune to your client’s risk appetite.

## Automation & pipelines (safe orchestration):
Design modular jobs:

passive-job , runs once: CT + GitHub scrapes + pDNS / normalizes to passive.json.

enrich-job , resolves passive findings with httpx/tls-scan / updates assets.json.

targeted-scan-job , picks top N assets from assets.json and runs nmap/ffuf with conservative timing.

alert-job , if enrich-job finds leaked credentials or exposed storage / generate immediate ticket/alert.

EXAMPLE : 
```
./job_passive.sh && ./job_enrich.sh && ./job_targeted_scan.sh && ./job_alerts.sh
```
Use a scheduler (cron, Airflow, or simple queue) and maintain separate logs for passive vs active.

## 5. OPSEC, tuning, and defensive empathy:
Rate-limits & timing: use -T2/-T3 in nmap, or --rate in masscan with conservative settings. Sleep between tasks: sleep $((RANDOM%10+5)).

Source IP management: if allowed, use client-approved jump hosts (and document them). Don’t route active scans through your daily-driver IP.

Distinct identities: separate accounts for passive OSINT (so GitHub queries do not tie to your personal account).

Detectability checks: simulate a single low-frequency probe then check if target webserver returns CAPTCHA, 403s, or triggers blocking; if so , back off and use passive methods.

Logging & proofs: keep timestamped logs and hashes of retrieved files; include sha256sum where evidence is needed.

## 6. Interpreting common noisy outputs (quick heuristics):
Multiple domains, same cert SANs: look for shared infra / shared panel or CDN origin.

404 vs 403: 403 on many endpoints with a valid auth cookie suggests a protected management app. 404 sometimes indicates security through obscurity.

Short-lived certs (1–7 days): often developer/test environments. Good hunting grounds for weak controls.

Unexpected open port 3389/5985/5986: escalate—these are often high-impact (RDP/WinRM) and should be treated carefully.

## 7. Example practical mini-playbook (safe & complete):
Goal: map HTTP/TLS surface for example.com (low-noise, RoE-compliant).

Passive collection (no target interaction):

Fetch CT entries / crt_example.json to extract subdomains.

Search public repos for example.com references.

Enrichment (safe network queries):

Resolve subdomains to IPs (using passive DNS or one-time DNS queries).

Run httpx against resolved names with -status-code -title -tls-proto.

Targeted active check (single thread, low intensity):

For hosts with admin-like titles or paths, run nmap -Pn -sV --top-ports 50 -T2 --max-retries 1 (single-host at a time).

Directory mapping (careful):

Use ffuf with a small, tailored wordlist against the admin host; cap threads to 10 and use --recursion-depth 1.

Synthesize: import all outputs into assets.json, generate a simple heatmap of exposure_score.

## 8. Advanced techniques & considerations :
JA3/JA3S TLS fingerprinting: useful to identify client/server stacks and detect custom services. Use for correlation rather than attack.

Timing analysis: small timing differences sometimes reveal protected endpoints; use with restraint.

Cloud origin discovery: detect origin behind CDN by comparing DNS history and cert SANs only for mapping, do not try bypassing CDN protections.

Insider/public repo crosswalk: parse company-specific repo references to identify internal hosts mentioned in README/CI —a high-signal low-noise path.

# Final OPSEC checklist:

Store and version your tools in a disposable environment (VM snapshot).

Keep passive and active logs separated and labeled with RoE and timestamp.

Pre-flight: verify scope, verify allowed methods in writing.

Always provide an emergency contact for critical findings discovered out-of-scope.

Keep a “kill switch” note: if you see system instability, stop and notify client.
