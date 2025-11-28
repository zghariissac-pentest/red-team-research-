# ad-overview
## What this file is

This file gives you a clean and simple understanding of Active Directory. No complex theory. Just what AD is, why it matters in attacks, and how attackers think about it.

## What Active Directory is

Active Directory is the identity and access system used in most companies. It stores information about users, computers, groups, permissions, policies, and how everything connects together.

## Why AD is important in attacks

If an attacker controls Active Directory, they control the entire network. AD decides who can log in, what rights they have, and what resources they can reach. So attacking AD means attacking the brain of the organization.

## Key AD building blocks
### Domain

A collection of users and computers under one security boundary.

Domain Controller

The server that stores AD data and handles authentication.

Users and Groups

Users represent people or services. Groups organize permissions.

Organizational Units

Folders inside AD used to organize and apply policies.

Group Policy

Rules that control user and computer behavior. Can enforce security or cause misconfigurations.

Service Accounts

Accounts used by applications. Many have high privileges and weak protection.

Trusts

Connections between domains or forests. If abused, attackers can move from one environment to another.

## How attackers think about AD

Attackers focus on relationships, not single systems. They look for weak rights, misconfigured privileges, and trust chains that allow movement across the network.

They target three things:

#### identity

Who you are. Attackers steal credentials, tickets, tokens, or passwords.

access

What you are allowed to do. Attackers abuse privileges and misconfigurations.

control

Who controls the domain. Attackers aim for domain admin or domain dominance.

## Why AD attacks are still common

Because most environments are old, large, and full of legacy settings. Companies change, but AD stays the same for years. Misconfigurations pile up, and attackers take advantage of them.
