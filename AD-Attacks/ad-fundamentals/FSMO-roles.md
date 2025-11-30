# FSMO Roles (Flexible Single Master Operations)

Although AD uses multi-master replication, certain operations require a **single authoritative DC**.  
These are the **FSMO roles**.

---

## 1. Forest-Wide FSMO Roles (2)

### ✔ Schema Master
- Maintains and updates the AD schema  
- Required for adding new object classes/attributes  
- Only one per forest

### ✔ Domain Naming Master
- Manages domain creation/deletion in the forest  
- Controls cross-domain namespace integrity  

---

## 2. Domain-Wide FSMO Roles (3)

### ✔ RID Master
- Allocates **Relative Identifiers** for SIDs  
- Ensures unique security identifiers  
- Required for creating new users/computers

### ✔ PDC Emulator
- Time synchronization authority  
- Processes password changes  
- Fallback authentication role  
- Legacy NT4 compatibility  
- Most critical day-to-day role

### ✔ Infrastructure Master
- Updates cross-domain object references  
- Ensures correct membership visibility  

---

## 3. Why FSMO Roles Matter
- Misplacing FSMO roles can break:
  - Replication  
  - Time sync  
  - Domain operations  
  - User creation  
- Attackers often target the **PDC Emulator** for:
  - Password harvesting  
  - Time manipulation  
  - GPO injection relevance  

---

## 4. Best Practice Placement
- Keep **PDC Emulator** on a strong, stable DC  
- Keep **RID Master** isolated and monitored  
- Ensure **Schema Master** is protected (rarely used)

---

*These roles ensure consistent, stable domain operations even in large, distributed AD environments.*
