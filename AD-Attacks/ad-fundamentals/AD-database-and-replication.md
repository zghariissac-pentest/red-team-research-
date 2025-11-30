# Active Directory Database & Replication

## 1. What Is the AD Database?
Active Directory stores all directory information in a central database called **NTDS.dit**.  
It contains:
- User accounts  
- Computer accounts  
- Groups  
- Password hashes (protected)  
- GPO links  
- Domain and forest configuration metadata  

### Key Files
| File | Purpose |
|------|---------|
| **NTDS.dit** | Main AD database |
| **edb.log** | Transaction log file |
| **edb.chk** | Checkpoint file |
| **SYSVOL**  | Stores GPOs & logon scripts |

---

## 2. How Replication Works
Replication ensures all Domain Controllers have the same updated directory data.

### Two Types of Replication
1. **Intra-site replication (within same site)**
   - Fast  
   - Uses change notifications  
   - Optimized for LAN

2. **Inter-site replication (between sites)**
   - Scheduled  
   - Compressed  
   - Designed for WAN

---

## 3. Replication Topology
Active Directory uses:
- **KCC (Knowledge Consistency Checker)** to build connection objects  
- **ISTG (Intersite Topology Generator)** for inter-site links  

### Replication Models
- **Multi-master replication**:  
  Any DC can update the database.
- **Last Writer Wins**:  
  Timestamp decides conflicts.

---

## 4. SYSVOL Replication
SYSVOL is replicated using:
- **DFSR (modern)**  
- **FRS (legacy / deprecated)**

SYSVOL contains:
- Group Policy Templates  
- Logon scripts  

---

## 5. Common AD Replication Issues
- USN rollback  
- Lingering objects  
- Time drift between DCs  
- DFSR backlog  
- Broken site links

---

## 6. Why Replication Matters for Pentesting
- Understanding replication helps identify:
  - Attack propagation speed  
  - Where credentials & policies live  
  - Persistence opportunities  
  - Impact of misconfigured sites

---

*This file summarizes how AD stores and synchronizes directory data, giving you the foundations needed for more advanced AD security research. check the other subjects*
