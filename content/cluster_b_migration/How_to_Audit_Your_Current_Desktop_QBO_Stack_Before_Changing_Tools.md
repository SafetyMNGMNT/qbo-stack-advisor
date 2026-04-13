---
title: "How to Audit Your Current Desktop/QBO Stack Before Changing Tools"
status: draft
---

*Disclosure: This site uses a layered monetization model. Some recommended tools (e.g., Make, Dext, Rewind) may provide affiliate compensation. This does not influence our QASEM-based risk evaluations.*

## Layer 1: The Decision Surface

**What this page answers:** How to structurally map and evaluate an existing accounting tech stack before migrating to a new general ledger or replacing core tools.

**Who this is for:** Small accounting firms preparing for a platform migration (e.g., leaving Desktop, restructuring QBO) or experiencing high failure rates in their current automation workflows.

**Decision Summary:** Never migrate a mess. A stack audit identifies undocumented integrations, quantifies true software costs, and maps data dependencies. Changing tools without an audit guarantees inherited failure modes.

## Layer 2: Authority & Trade-Offs

Firms often assume they know how their data flows. An audit usually reveals "shadow IT"—legacy tools, direct bank feeds set up by clients, or redundant Zapier connections that the firm forgot existed.

**Who this is not for:**
Micro-practices with fewer than 5 clients, utilizing a single general ledger and zero third-party integrations. For these firms, a formal architecture audit is operational overkill.

**Cost-Per-Client Scaling (CPCS) Implications:**
An un-audited stack frequently contains redundant subscriptions (e.g., paying for Dext while also paying for a QBO tier that includes receipt capture). Auditing allows firms to terminate overlapping tools, immediately lowering the baseline CPCS before a migration.

**When this stops working (Switch Signal):**
If you cannot confidently diagram how a receipt moves from a client's email into a reconciled bank transaction without manual intervention, your current ad-hoc stack has stopped working. This is the signal to audit.

## Layer 3: Deep Base & Architecture Implication

Using the **QASEM framework**, the audit must prioritize mapping connections over listing features.

**Integration Friction (IFS) & Architectural Mapping:**
Evaluate every tool based on its Integration Friction. Does it connect via native API, third-party orchestrator (like Make), or manual CSV export? Native integrations with low friction on Desktop may exhibit high friction on QBO.

**Failure Mode & Risk (FMR): The "Blind Sync Overwrite" Failure Mode**
A critical failure mode discovered during audits is the blind bidirectional sync. For example, a legacy CRM and a billing tool both push data to the ledger without defined precedence. When migrating to a new platform, if these connections are blindly re-established, the new system will immediately suffer from data overwrites and corruption. The audit must establish a definitive **Source of Truth** for each data domain.

**Next Step:** If your audit is prompted by the impending Intuit service termination, refer to the [QuickBooks Desktop 2023 Sunset: What Small Firms Need to Do Before May 31, 2026](./QuickBooks_Desktop_2023_Sunset.md) for critical deadlines.
