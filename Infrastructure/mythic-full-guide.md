# Mythic full guide
## Introduction

Mythic is an extensible, modern command-and-control framework designed for red team operations. It focuses on modularity, operational security, and cross-platform agent support. This guide provides a clear and practical workflow for setting up, configuring, and operating Mythic from start to finish.

## Requirements

Linux host (Ubuntu recommended)

Docker and Docker Compose

Stable internet connection

Basic knowledge of C2 operational security

A domain and HTTPS certificate (optional but recommended)

## Setup

Install Docker and Docker Compose

Clone the Mythic repository

Start the Mythic environment using:
```
./mythic-cli start
```
Access the web interface through the default port

Create your first user and log in

Configuration
Operator roles

Define operator roles early. Use separate accounts for developers, operators, and analysts. Avoid shared credentials.

Profiles

Set global preferences:

Timezone

Callback interval

Logging behavior

Resource limits

Operational folders

Organize payloads, scripts, and artifacts into clear directories.

Payload types

Mythic supports multiple agents. Choose based on OS, stealth requirements, and capabilities.

Common payload types:

Apollo (Windows)

Poseidon (Linux)

Hermes (macOS)

Medusa (Cross-platform)

Each payload has:

Build configuration

Encryption settings

Transport profile

C2 options

C2 profiles

C2 profiles define communication style and network behavior.

Popular profiles:

HTTP

HTTPS

WebSocket

DNS

Custom profiles

Key parameters:

Callback interval

Jitter

Host/header spoofing

AES keys

User-agent

URI patterns

Avoid defaults to reduce detection.

Building payloads

Select payload type

Configure communication (profile + key)

Set build-specific options

Generate executable or script

Export and prepare for delivery

Keep builds unique per target and per operator.

Agents management

After deployment, callbacks will appear in the dashboard.

## From each agent, you can:

Execute commands

Browse file systems

Upload or download files

Inject into processes

Spawn new agents

Adjust sleep and jitter

Use long sleep intervals for stealth.

Tasks and responses

Each command is treated as a task:

Pending

Executing

Completed

Error

Store only essential output. Avoid large data collection unless necessary.

## Interactions

Mythic allows controlled interactions:

Remote shells

File browsing

Process management

Keylogging or screenshot modules (depending on payload)

Always validate commands in a safe environment before issuing them on live targets.

Plugins

Mythic includes community and official plugins.

## Common plugins:

Reporting

Screenshots viewer

Credential tracker

WebRTC profile

Operation security monitors

Install only what you need. Remove unused plugins to reduce attack surface.

Operational security

## Core opsec considerations:

Use redirectors between operators and the Mythic server

Never expose Mythic directly to the internet

Use strong authentication

Segregate infrastructure into layers

Rotate C2 profiles and payload configurations

Avoid predictable callback patterns

Monitor logs for anomalies

Mythic is powerful, but careless configuration reveals the entire operation.

## Infrastructure tips

Use separate servers for redirectors and the Mythic core

Apply firewall rules to restrict access

Enable TLS with valid certificates

Avoid logging sensitive task output on the main server

Keep infrastructure isolated from your personal workstation

Maintenance

Frequently update payload types

Keep Docker images clean

Remove old or unused builds

Review operational logs

Archive reports and delete outdated data

Troubleshooting

## Common issues:

Payload build failures: verify dependencies

Missing callbacks: check redirector, DNS, and firewall

Slow interface: prune Docker containers

Broken profiles: inspect config files for syntax errors

## Kill chain integration

Mythic supports continuous operations across:

Initial access

Persistence

Privilege escalation

Lateral movement

Collection

Exfiltration

Each stage can be automated or manually controlled.

## cleanup

After finishing the operation:

Kill all active agents

Purge logs

Stop and remove containers

Wipe infrastructure safely

Archive only what is necessary for reporting

Never leave Mythic servers running after an engagement.

# Conclusion

Mythic is a professional-grade C2 framework powerful enough for advanced red team operations. Its modular design requires proper configuration, strong opsec discipline, and organized workflow. With a clean setup and careful usage, it becomes a reliable center of control for complex engagements
