# Secure communications

Secure communication is one of the most important elements of red team operational security. Any message, login session, or file transfer done without proper protection can reveal identity, location, or operational details. Secure communication ensures that all interactions remain confidential, authenticated, and isolated from personal activity.

The goal is to prevent interception, correlation, and metadata leaks during planning, coordination, and execution of operations.

## Communication principles

### Confidentiality
All communication must be encrypted end to end. Unencrypted channels expose content and metadata that can compromise operators and infrastructure.

### Compartmentalization
Use separate communication channels for each engagement. Do not mix personal and operational messages. Each project should have its own accounts, devices, and communication paths.

## Minimal exposure
Share only what is necessary. Avoid long messages, excessive attachments, or sensitive details unless absolutely required.

### Metadata reduction
Even encrypted messages leak metadata such as time, sender, and connection details. Choose platforms that minimize stored metadata and avoid linking accounts to real phone numbers or emails.

### Communication platforms

Select platforms that provide strong encryption, privacy controls, and no mandatory identity verification. Messaging services with anonymous account creation provide better OpSec than those tied to phone numbers or centralized identities.

Self hosted communication tools can offer more control but require careful configuration and isolation. They should not run on personal servers or domains that can reveal identities.

Avoid mainstream corporate tools for sensitive communication as they often log data, perform scanning, or require real identity verification.

## Account hygiene

Create separate accounts for each operation. Do not reuse usernames, avatars, or details across different personas. All accounts should be created from clean devices and routed through VPN and proxy layers.

Do not sync operational communication apps to personal devices. Disable all cloud backups, logging, and message retention features. Avoid linking recovery options to personal email addresses or phone numbers.

## File transfer security

Files shared between operators must be encrypted before upload. Use strong local encryption tools and avoid storing sensitive content on cloud services.

When possible, transfer files through indirect channels such as temporary encrypted storage or layered transfer paths. Remove metadata from files before sending them as embedded information can reveal device details or timestamps.

## Voice and video communication

Voice and video calls produce more metadata and potential leaks than text. Use them only when necessary. Ensure calls are routed through the same layered network paths as other communication. Avoid revealing surroundings, background noise, or device characteristics that break persona consistency.

## Communication discipline

Do not discuss unnecessary operational details through any channel. Limit conversations to the minimum required to execute the mission. Avoid sending real names, personal experiences, or irrelevant content.

Communication logs should be cleared regularly and devices should not retain historical messages. When an operation ends, accounts and communication platforms used for it must be retired
