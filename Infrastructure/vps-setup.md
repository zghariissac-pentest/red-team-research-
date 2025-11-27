# Vps setup

A Virtual Private Server is the core of most red team infrastructure. It hosts redirectors, command servers, payload hosting points, and operational services. A clean and well configured VPS reduces noise, lowers detection, and helps maintain operational security.

## Choosing a provider

Selecting the right provider affects the entire operation. You want a provider that offers fast deployment, supports multiple locations, and accepts flexible payment options. Avoid providers that require strong identity verification when possible. Prefer platforms that support instant VPS wipes and recreate functions.

## Operating system selection

Choose a minimal Linux distribution such as Debian or Ubuntu Server. A minimal OS reduces services, attack surface, and telemetry. Avoid prebuilt images that contain unnecessary monitoring agents or cloud integrations.

## Initial provisioning

Once the server is deployed, update the operating system and install only the required packages. Disable unused services and remove default users or configurations provided by the hosting platform.

## Network hardening

Firewall configuration is essential. Allow only the ports required for redirectors or C2 infrastructure. Deny all inbound traffic by default. Enable outbound filtering if possible to prevent accidental data leakage.

## SSH security

Use key based authentication and disable password login. Change the default SSH port only if it does not interfere with operational profiles. Install fail2ban or equivalent tools only if they do not conflict with stealth requirements.

## Logging control

Reduce logs to the minimum required by the operation. Disable unnecessary audit logs. Configure log rotation to ensure older logs are deleted automatically. Avoid installing monitoring agents from the provider.

## VPS isolation

Do not reuse the same VPS for multiple campaigns. Each operation should have its own server, keys, and domain associations. Keeping infrastructure isolated prevents cross contamination and lowers attribution risk.

## Snapshot and rebuild strategy

Before deploying payloads or redirectors, create a clean snapshot. After the operation is finished, destroy the server entirely. Never reuse a compromised or exposed VPS
