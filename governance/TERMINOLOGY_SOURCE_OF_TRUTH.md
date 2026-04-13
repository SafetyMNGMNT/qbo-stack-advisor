# TERMINOLOGY SOURCE OF TRUTH

This document governs key terms to prevent factual and conceptual drift across the project. All content must adhere to these definitions.

## Core Framework
* **QASEM (QuickBooks Automation Stack Evaluation Model):** The internal evaluation framework used to judge tools based on Failure Mode & Risk (FMR), Audit Trail Strength (ATS), Integration Friction (IFS), Cost Per Client Scaling (CPCS), and Automation Depth (ADS).

## Evaluation Criteria
* **Failure Mode:** A specific, predictable way a tool, integration, or workflow can break, corrupt data, or create unmanageable manual rework.
* **Cost-Per-Client Scaling:** The financial trajectory of a tool or stack as firm client volume increases. Used to identify when a setup becomes commercially unsustainable.
* **Audit Trail Strength:** The ability of a system to maintain an immutable, easily traceable record of who/what altered data, and when.
* **Integration Friction:** The technical or operational resistance encountered when connecting a tool to QuickBooks Online or other stack components.

## Technical & Architectural Terms
* **Workflow Constraint:** A bottleneck or limitation within a specific operational process that prevents scaling or introduces unacceptable risk.
* **Source of Truth:** The single, authoritative system where a specific data domain (e.g., core financials, client contact details) is mastered and trusted above all other connected systems.
* **Idempotency:** The property of an operation that allows it to be applied multiple times without changing the result beyond the initial application. Critical for safe automation.
* **Rollback / Reversal:** The documented capability and process for undoing a failed automation, data import, or workflow error to restore a safe previous state.
* **Orchestration:** The management and coordination of multiple automated workflows and integrations across the firm's stack.
* **Migration Trigger:** A specific operational, financial, or risk-based threshold that indicates a firm should abandon their current system (e.g., QBO or Desktop) for a new platform.
