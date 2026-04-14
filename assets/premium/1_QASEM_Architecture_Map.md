# The QASEM Architecture Map
*Premium Migration Audit Kit*

## Overview
Before migrating from QuickBooks Desktop to QBO (or QBO to Xero), you must map the current state. This framework exposes silent failure modes and identifies which integrations will break during the transition.

## Mapping Protocol

### 1. Identify All Ingress Points
List every system that pushes data *into* the general ledger.
*   **System Name:** (e.g., Dext, Custom CRM, Zapier webhook)
*   **Data Type:** (e.g., Invoices, Receipts, Time entries)
*   **Connection Method:** (e.g., Native API, CSV import, Middleware orchestrator)

### 2. Identify All Egress Points
List every system that pulls data *out of* the general ledger.
*   **System Name:** (e.g., Fathom, Float, Custom Dashboard)
*   **Data Type:** (e.g., P&L, Trial Balance, Classes/Locations)

### 3. Define the Source of Truth
For every data domain, identify the single authoritative system.
*   **Client Contact Info:** [System Name]
*   **Billable Time:** [System Name]
*   **Final Financial State:** [General Ledger]

### 4. Locate Bidirectional Syncs (High Risk)
Identify any connection that pushes *and* pulls. 
*   **Warning:** Bidirectional syncs are the primary cause of infinite loops and data overwrites during a migration. They must be downgraded to unidirectional syncs before the data transfer begins.

### 5. Document Workflow Constraints
Identify existing bottlenecks. Does the current setup require manual intervention to categorize an entry after an automation fires? If yes, the migration must address this constraint, or you will carry technical debt into the new platform.