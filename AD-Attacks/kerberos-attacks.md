# kerberos-attacks
### Why Kerberos is targeted

Kerberos is the main authentication protocol in AD. If attackers break it, they break identity.

## Key Kerberos Attack Types
### Kerberoasting

Stealing service account hashes by requesting service tickets.

### ASREProasting

Requesting encrypted ASREP messages from accounts without preauthentication.

### Pass the Ticket

Using captured Kerberos tickets to authenticate.

### Golden Ticket

Forging TGTs with the KRBTGT key.

### Silver Ticket

Forging service tickets for targeted services.

### Overpass the Hash

Using NTLM hashes to obtain Kerberos tickets.

### Ticket renewal abuse

Renewing or extending lifetime of stolen tickets.
