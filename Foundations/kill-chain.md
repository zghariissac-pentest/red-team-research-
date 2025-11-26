## kill-chain

The kill chain describes the sequence of steps an adversary follows during an attack. It helps red teamers structure operations, identify opportunities for stealth, and understand how real threats progress through a target environment. A clear kill chain provides context for planning, execution, and reporting.

The goal of the kill chain is not to force a rigid structure but to give operators a mental model for how attacks naturally evolve. Each stage has its own risks, its own visibility, and its own operational decisions.

## Reconnaissance

The attacker gathers information about the target. This includes domains, network ranges, employees, technologies, cloud services, and external exposure. Recon shapes every later stage. Good intelligence enables realistic tradecraft while poor intelligence leads to noisy or ineffective actions.

This stage is usually passive to reduce detection. Active probing is used only when necessary and within the engagement scope.

## Weaponization

The attacker prepares tools, payloads, infrastructure, and delivery mechanisms. This may include phishing templates, macro documents, exploits, redirectors, C2 servers, and operational personas.

Weaponization is about aligning all tools with the intelligence gathered earlier. Payloads must match the environment, avoid detection, and support post exploitation objectives.

## Delivery

The attacker delivers the payload to the target. Common delivery paths include phishing emails, malicious documents, web exploitation, cloud abuse, supply chain mechanisms, or physical access.

Delivery must balance effectiveness and stealth. A high success rate means nothing if the method triggers alarms that compromise the entire operation.

## Exploitation

The delivered payload is executed. This stage may involve user interaction, exploit triggers, misconfigurations, or authentication weaknesses.

The goal is to gain initial code execution or authenticated access. Timing, payload design, and user behavior all play a role in this stage.

## Installation

The attacker establishes a foothold on the target system. This commonly includes installing an agent, setting up persistence, or creating initial credentials. Installation must be as quiet as possible to avoid immediate detection.

A stable foothold enables deeper movement inside the environment.

## Command and Control

The attacker connects back to controlled infrastructure. The communication channel must be reliable, encrypted, and disguised to blend with normal traffic. C2 operations must consider endpoint visibility, network monitoring, and behavioral detection.

This stage defines how operators interact with the target and maintain long term access.

## Lateral Movement

The attacker expands control through the environment. This includes credential theft, token abuse, remote execution, and pivoting through trust relationships. The goal is to reach higher value systems with minimal noise.

Lateral movement is where detection risk increases the most. Every action must follow strict OPSEC rules.

## Actions on Objectives

The attacker executes actions that demonstrate real world impact. Examples include data access, account takeover, domain dominance, cloud compromise, or exfiltration. This final stage shows what a motivated adversary could achieve.

Actions must align with engagement objectives and avoid unnecessary risk.

Operational Use for Red Teams

The kill chain is a guide, not a rulebook. Red teams use it to structure operations, assess progress, and understand defensive detection points. Each stage provides opportunities for stealth, alternative paths, and controlled escalation.

A disciplined approach to the kill chain enables realistic threat simulation and reduces operational mistakes
