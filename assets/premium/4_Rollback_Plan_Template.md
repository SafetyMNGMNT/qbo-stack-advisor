# The Rollback Plan Template
*Premium Migration Audit Kit*

## Objective
A documented disaster recovery protocol to restore a safe previous state in the event of a botched batch import or catastrophic automation failure during the migration window.

## Protocol Definition

### 1. Incident Identification
*   **Trigger:** How will a failure be detected? (e.g., Reconciliation discrepancy > $X, Error alert from orchestrator, manual spot-check failure).
*   **Responsible Party:** Who is authorized to declare a rollback? [Name/Role]

### 2. Containment
*   **Immediate Action:** Suspend the failing integration or batch import script immediately.
*   **Communication:** Notify stakeholders that the ledger is currently in an unstable state.

### 3. Reversal Execution
*Select the applicable reversal method based on the failure scope.*

**Method A: Automated Rollback (Preferred)**
*   **Tool:** (e.g., Rewind)
*   **Procedure:** Access the vault, identify the timestamp immediately preceding the failed import/automation run, and initiate a targeted ledger restoration.

**Method B: Scripted Deletion (Orchestrator)**
*   **Tool:** (e.g., Make)
*   **Procedure:** Execute a pre-built "undo" scenario that takes the array of failed transaction IDs (logged during the error) and sends sequential DELETE requests to the QBO API.

**Method C: Manual Journal Reversal (Fallback)**
*   **Procedure:** If APIs fail, create a single, consolidated reversing journal entry to neutralize the financial impact of the corrupted batch, pending a clean re-import.

### 4. Post-Incident Review
*   **Root Cause:** Why did the failure mode execute?
*   **Idempotency Check:** Did the system fail to recognize duplicate data?
*   **Resolution:** What architectural change is required before the integration is re-enabled?