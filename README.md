# Red teaming research (work in progress)

This repository is my personal offensive security research project. I am an 18‑year‑old learner who is passionate about red teaming, cyber operations, and understanding how real attacks work behind the scenes. Everything you see here comes from my own studies, experiments, and practice.


## What this repo is

This project is a full documentation hub covering every phase of a red team operation. You will find theory, practical workflows, operational mindset, and custom tools I wrote for learning. Each section is written in simple, clear English without noise or unnecessary complexity.

If you’re new, you can go through the folders in order.
If you’re experienced, you can jump to the section you want and use it as a reference.

## What this repo is not

This repo is not meant to break laws or encourage illegal actions. Everything here is for learning offensive security in ethical, legal, controlled environments. I do not provide real-world attack data or anything harmful.
Everything is educational.

## Structure

## The repository is divided into logical stages:

| File              | Description             |
| ----------------- | ----------------------- |
| `README.md`       | Main introduction       |
| `CONTRIBUTING.md` | Contribution guidelines |
| `LICENSE`         | License information     |
| `ROADMAP.md`      | 15-day roadmap          |

| File                        | Description                  |
| --------------------------- | ---------------------------- |
| `introduction.md`           | Project intro                |
| `methodology.md`            | Red team methodology         |
| `red-vs-blue-vs-purple.md`  | Team model differences       |
| `legal-ethics.md`           | Legal & ethical guidelines   |
| `kill-chain.md`             | Cyber Kill Chain explanation |
| `mitre-attck-overview.md`   | MITRE ATT&CK overview        |
| `operational-philosophy.md` | Red team mindset             |

| File                           | Description                   |
| ------------------------------ | ----------------------------- |
| `opsec-overview.md`            | OpSec fundamentals            |
| `infrastructure-opsec.md`      | Infrastructure OpSec          |
| `persona-development.md`       | Creating operational personas |
| `domains-buying.md`            | Anonymous domain purchase     |
| `vpn-proxy-setup.md`           | VPN & proxy OpSec             |
| `secure-comms.md`              | Secure communication methods  |
| `clean-operational-machine.md` | Clean workstation setup       |

| File                         | Description              |
| ---------------------------- | ------------------------ |
| `overview.md`                | Infrastructure basics    |
| `vps-setup.md`               | VPS setup                |
| `redirectors-types.md`       | Redirector models        |
| `cdn-evasion.md`             | CDN abuse & evasion      |
| `c2-overview.md`             | C2 fundamentals          |
| `cobaltstrike-full-guide.md` | Full Cobalt Strike guide |
| `sliver-full-guide.md`       | Sliver C2 guide          |
| `mythic-full-guide.md`       | Mythic framework         |
| `opsec-c2-tips.md`           | C2 OpSec tips            |

| File                  | Description           |
| --------------------- | --------------------- |
| `passive-recon.md`    | Passive intelligence  |
| `active-recon.md`     | Active scanning       |
| `subdomain-enum.md`   | Subdomain enumeration |
| `cloud-enum.md`       | Cloud service recon   |
| `org-mapping.md`      | Mapping org structure |
| `employee-recon.md`   | Employee recon        |
| `recon-automation.md` | Automation tips       |

| Tool                 | Description           |
| -------------------- | --------------------- |
| `subdomain_enum.py`  | Subdomain enum script |
| `recon_harvester.py` | Recon harvester       |
| `org_mapper.py`      | Organization mapper   |

| File                         | Description             |
| ---------------------------- | ----------------------- |
| `initial-access-overview.md` | Overview                |
| `phishing-advanced.md`       | Advanced phishing       |
| `payload-delivery.md`        | Payload delivery        |
| `malware-opsec.md`           | Malware OpSec           |
| `documents-macro-attacks.md` | Macro-document attacks  |
| `web-vulns-access.md`        | Web attack entry        |
| `vpn-abuse.md`               | VPN exploitation        |
| `initial-access-cloud.md`    | Cloud access techniques |

| Tool                      | Description         |
| ------------------------- | ------------------- |
| `phishing-mailer.py`      | Email phishing tool |
| `macro-generator.vba`     | Macro generator     |
| `exploit-poc-template.py` | Exploit PoC         |
| `payload-stager.cs`       | C# payload stager   |

| File                   | Description             |
| ---------------------- | ----------------------- |
| `host-discovery.md`    | Host discovery          |
| `persistence.md`       | Persistence techniques  |
| `lateral-movement.md`  | Lateral movement        |
| `credential-access.md` | Credential harvesting   |
| `evading-edr.md`       | EDR evasion             |
| `in-memory-exec.md`    | In-memory execution     |
| `cloud-postex.md`      | Cloud post-exploitation |

| Tool                   | Description      |
| ---------------------- | ---------------- |
| `token-stealer.ps1`    | Token stealer    |
| `lateral-movement.py`  | LM tool          |
| `log-bypass.ps1`       | Log bypass       |
| `shellcode-runner.cpp` | Shellcode runner |

| File                  | Description             |
| --------------------- | ----------------------- |
| `ad-overview.md`      | AD basics               |
| `enumeration.md`      | AD enumeration          |
| `kerberos-attacks.md` | Kerberos attacks        |
| `delegation-abuse.md` | Delegation abuse        |
| `privesc.md`          | AD privilege escalation |
| `domain-dominance.md` | Domain domination       |
| `forest-attacks.md`   | Forest-level attacks    |

| Tool                        | Description     |
| --------------------------- | --------------- |
| `bloodhound-queries.cypher` | BH queries      |
| `ad-enum.ps1`               | AD enumeration  |
| `kerberoast.py`             | Kerberoasting   |
| `asreproast.py`             | AS-REP roasting |

| File                    | Description |
| ----------------------- | ----------- |
| `windows-privesc.md`    | Windows PE  |
| `linux-privesc.md`      | Linux PE    |
| `containers-privesc.md` | Containers  |
| `cloud-privesc.md`      | Cloud PE    |

| Tool                    | Description        |
| ----------------------- | ------------------ |
| `win-privesc.ps1`       | Win PE script      |
| `linux-privesc.sh`      | Linux PE script    |
| `container-breakout.py` | Container breakout |

| File                 | Description            |
| -------------------- | ---------------------- |
| `av-bypass.md`       | Antivirus bypass       |
| `edr-evasion.md`     | EDR evasion            |
| `firewall-bypass.md` | Firewall bypass        |
| `sandbox-evasion.md` | Sandbox evasion        |
| `obfuscation.md`     | Obfuscation strategies |
| `dll-injection.md`   | DLL injection          |

| Tool                  | Description     |
| --------------------- | --------------- |
| `xor-obfuscator.py`   | XOR obfuscation |
| `loader.cs`           | Loader          |
| `bypass-signature.py` | Sig bypass      |

| File                   | Description       |
| ---------------------- | ----------------- |
| `executive-summary.md` | Executive summary |
| `attack-path.md`       | Attack path       |
| `technical-report.md`  | Technical report  |
| `remediation.md`       | Recommendations   |
| `template.md`          | Report template   |

| File                | Description   |
| ------------------- | ------------- |
| `sample-report1.md` | Sample report |
| `sample-report2.md` | Sample report |
| `sample-graphs/`    | Graph assets  |

| File                   | Description      |
| ---------------------- | ---------------- |
| `book-list.md`         | Book references  |
| `cheatsheets.md`       | Cheat sheets     |
| `scripts-reference.md` | Script index     |
| `glossary.md`          | Glossary         |
| `apt29.md`             | APT29 case study |
| `apt41.md`             | APT41 case study |
| `lapsus.md`            | LAPSUS$ case     |


Each folder contains Markdown files plus custom scripts where needed.

### Tools

Some sections include small tools I wrote for learning purposes. They are not “real world ready”, but they show concepts, automation ideas, and basic offensive coding skills. You can use them as templates to build your own tools later.

## Why I built this

I wanted one place where I can:

document everything I learn

stay consistent with my growth

build a real portfolio

improve my offensive research writing

collect all concepts in one clean structure

help others who learn the same topics

This repo will continue to evolve as I learn more and expand the content.

#### Contributing

This is mainly a personal research project, but if you want to suggest improvements, corrections, or ideas, feel free to open an issue or a pull request.
Just keep the style clean and the explanations simple.

# License

MIT License.
You are free to use, copy, and modify the content as long as you respect




