# QBO Automation Risk Checklist

**Asset Type:** Diagnostic Framework / Self-Audit Tool
**Objective:** Identify architectural vulnerabilities, undocumented data overwrites, and commercial scaling risks within a QuickBooks Online tech stack before they cause systemic failure.

---

## 1. Failure Mode & Risk (FMR)
*Assess the blast radius of a broken workflow.*

- [ ] **Source of Truth Definition:** Is there a single, documented "Source of Truth" for every data domain (e.g., CRM for client contacts, QBO for final ledger)?
- [ ] **Bidirectional Sync Rules:** Are bidirectional syncs strictly governed by precedence rules to prevent endless data loops or blind overwrites?
- [ ] **Idempotency Check:** If an automation fires twice by accident, does it create duplicate entries in QBO, or does it recognize the existing transaction and halt?
- [ ] **Rollback Protocol:** If a batch data import or automation corrupts 500 ledger entries, is there a documented, tested procedure to reverse the damage (e.g., using Rewind or manual reversal scripts)?

## 2. Audit Trail Strength (ATS)
*Assess traceability and forensic recovery.*

- [ ] **Payload Logging:** Do third-party orchestrators (like Make or Zapier) store the raw payload of failed API calls for troubleshooting?
- [ ] **Transaction Attribution:** When looking at a QBO journal entry, can you immediately identify *which* specific automation or tool generated it?
- [ ] **Error Notification Routing:** Are integration failure alerts routed to a centralized, monitored channel rather than a single employee's personal inbox?

## 3. Integration Friction (IFS)
*Assess the brittleness of the connection.*

- [ ] **API vs. Workarounds:** Does the integration use official Intuit APIs, or does it rely on fragile methods like CSV email parsing or UI scraping?
- [ ] **Rate Limit Handling:** If client transaction volume spikes, will the integration hit QBO API rate limits? If so, does it queue the data gracefully or drop it entirely?
- [ ] **Authentication Stability:** How often do API tokens or OAuth connections spontaneously disconnect, requiring manual re-authentication?

## 4. Cost-Per-Client Scaling (CPCS)
*Assess the commercial sustainability of the stack.*

- [ ] **Volume Penalties:** Does the automation software charge per task/operation in a way that punishes firm growth (e.g., per-receipt pricing scaling exponentially)?
- [ ] **Feature Redundancy:** Are you paying for third-party tools (e.g., standalone receipt capture) that are now natively covered by your current QBO subscription tier?
- [ ] **SaaS Margin Drain:** Have you calculated the exact monthly software overhead per client, and is it factored into your fixed-fee pricing model?

## 5. Automation Depth (ADS)
*Assess if the tool solves the root problem.*

- [ ] **Manual Rework Creation:** Does the automation require human intervention to categorize data *after* it reaches QBO, negating the efficiency gain?
- [ ] **Exception Handling:** Does the workflow automatically flag anomalies for human review, or does it blindly force bad data into the ledger?

---
*For a complete methodology on evaluating your stack, refer to our [Methodology](../content/trust/Methodology.md) and the [How to Audit Your Current Desktop/QBO Stack Before Changing Tools](../content/cluster_b_migration/How_to_Audit_Your_Current_Desktop_QBO_Stack_Before_Changing_Tools.md) guide.*