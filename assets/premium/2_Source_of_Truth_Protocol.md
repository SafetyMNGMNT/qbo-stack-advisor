# The "Source of Truth" Pre-Migration Protocol
*Premium Migration Audit Kit*

## Objective
To safely isolate legacy data and prevent data corruption (e.g., Historical Data Truncation or Blind Sync Overwrites) during the platform transition.

## Execution Steps

### Phase 1: Disconnection
**Rule:** Never migrate a live system.
1.  **Suspend Automations:** Pause all active Make scenarios, Zapier zaps, and native integration syncs connected to the legacy ledger.
2.  **Revoke API Tokens:** Manually revoke access for all third-party apps in the legacy system settings.
3.  **Halt Bank Feeds:** Disconnect live bank feeds to prevent duplicate transaction ingestion during the cutover window.

### Phase 2: Data Extraction & Archival
**Rule:** The migration tool will not carry over the audit trail.
1.  **Extract Journal:** Export the complete, granular general ledger detail report for all historical periods to a static CSV/Excel file.
2.  **Extract Audit Log:** If available, export the system audit trail (who changed what, when).
3.  **Secure Storage:** Store these archives in an immutable, read-only location (e.g., a restricted cloud drive folder). This is your forensic fallback.

### Phase 3: Domain Isolation
**Rule:** Define precedence before reconnecting.
1.  Identify the **Source of Truth** for each data type (as defined in the Architecture Map).
2.  Configure the new ledger (e.g., QBO) to accept data *only* from the designated Source of Truth.
3.  Ensure idempotency: Verify that if a transaction is imported twice during testing, the system rejects the duplicate rather than creating a double entry.