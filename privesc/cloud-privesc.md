Cloud Privilege Escalation

Cloud privilege escalation focuses on gaining higher privileges within cloud environments such as AWS, Azure, or GCP. Unlike traditional systems, cloud platforms rely on identity, roles, and API permissions, so misconfigurations or overly permissive policies become the main paths for escalation. Understanding identity-based security models is key.

Core Principles
Identity is everything

Cloud platforms manage resources through users, roles, and service accounts. Gaining elevated privileges often means compromising these identities or their associated permissions.

Enumeration first

Identify users, groups, roles, policies, and accessible resources. Without thorough enumeration, escalation attempts are likely to fail or trigger alerts.

Abuse least privilege violations

Excessive permissions or over-permissive roles are the most reliable paths for escalation.

Minimize API calls and logging

Cloud providers log almost all actions. Minimize noisy operations to avoid detection.

Chain misconfigurations

Escalation usually involves chaining multiple permission gaps or misconfigured services.

Key Enumeration Targets
IAM / Identity and Access Management

Check roles, policies, attached permissions, groups, and delegated identities. Look for privilege overlaps and overly broad permissions.

Service accounts and keys

Service accounts with API keys or tokens can allow programmatic access. Key discovery is critical.

Storage buckets and file permissions

Misconfigured S3, Blob, or GCS buckets often expose sensitive data or credentials.

Compute instances and metadata services

Cloud VMs often have metadata services that expose temporary credentials or tokens.

Function-as-a-Service / Serverless

Serverless functions may have elevated roles. Triggering functions or reading environment variables can expose credentials.

Cross-account or cross-project roles

Misconfigured trust relationships allow escalation from one account/project to another.

Common Privilege Escalation Techniques
IAM misconfigurations

Excessive privileges, missing resource restrictions, or misconfigured assume-role policies allow privilege escalation.

Compromised service accounts

Access to service account credentials enables API calls as the service, often with higher privileges.

Metadata service exploitation

Cloud VMs often expose identity tokens in metadata endpoints. Reading these tokens can allow role escalation.

Over-permissive storage access

Readable or writable cloud storage can leak secrets, scripts, or configuration files.

Lambda / Function role abuse

Serverless functions often run with roles that have elevated permissions. Exploiting function code or environment variables may grant higher privileges.

Cross-project / cross-account trust

Abusing trust relationships allows moving from a lower privilege environment to a higher one.

Temporary credential abuse

Tokens issued by cloud providers often expire but can be leveraged to perform actions during their validity.

High-Value Enumeration Commands and APIs
AWS CLI / SDK

aws iam list-users
aws iam list-roles
aws s3 ls
aws sts get-caller-identity
aws ec2 describe-instances

Azure CLI / SDK

az ad user list
az role assignment list
az storage account list
az vm list

GCP CLI / SDK

gcloud iam roles list
gcloud projects get-iam-policy [PROJECT]
gcloud storage buckets list

Metadata endpoints

Check instance metadata for temporary credentials or service account tokens.

Living-off-the-Land Techniques
API calls

Use built-in cloud APIs to enumerate resources, roles, and permissions without additional tooling.

Cloud-native tools

Cloud shells, web consoles, and cloud CLIs allow interactive exploration while respecting logging.

Automated enumeration frameworks

Frameworks like Prowler (AWS), ScoutSuite, or CloudSploit can provide structured assessments safely if used carefully.

Defensive Awareness
Minimize destructive actions

Avoid deleting or modifying cloud resources unless approved.

Respect logging

Every API call is logged. Prefer read-only enumeration before testing exploit paths.

Monitor for alerts

Cloud platforms often have real-time detection. Avoid repeated or high-volume queries.

Protect harvested credentials

If temporary tokens or service account keys are exposed during testing, secure them immediately.

Building a Clean Escalation Path
Step 1: Enumerate identities and permissions

Map users, roles, policies, and attached permissions.

Step 2: Identify misconfigurations

Look for overly permissive roles, missing resource restrictions, exposed keys, or service account weaknesses.

Step 3: Evaluate impact

Determine what actions each identity can perform and potential escalation paths.

Step 4: Execute minimal action

Perform only the required operations to gain higher privileges.

Step 5: Verify access

Confirm elevated permissions or access to new resources.

Step 6: Cleanup and reporting

Revoke temporary keys if created and document findings securely.

Summary

Cloud privilege escalation relies on understanding identity-based security, misconfigurations, and chained permissions. Structured enumeration, careful exploitation of roles or service accounts, and minimal API activity are the foundations of a reliable escalation path in cloud environments. Awareness of logging and detection mechanisms ensures clean and controlled operations.
