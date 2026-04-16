# UK Legal & Commercial Requirements Matrix

This document outlines the mandatory legal and commercial guardrails for scaling and monetizing this project as an entity operating within the United Kingdom.

## 1. Regulatory Compliance (Marketing & Content)
*   **ASA/CAP Code (Advertising Standards Authority):** 
    *   *Requirement:* Affiliate links must be explicitly and prominently disclosed. The current sitewide disclaimer meets the baseline, but inline disclosures (e.g., "[Affiliate Link]") may be required if the primary intent of a page shifts to direct sales.
    *   *Status:* Compliant (Baseline). Addressed in `Affiliate_Disclosure.md`.
*   **CMA (Competition and Markets Authority):** 
    *   *Requirement:* "Fake reviews" and undisclosed incentivized endorsements are strictly prohibited. The QASEM evaluation model serves as the defense against CMA breach by ensuring objective, risk-based analysis supersedes payout potential.
    *   *Status:* Compliant. Driven by the `SYSTEM_GUARDRAILS.md` evidence-first rules.

## 2. Data Protection (GDPR / UK-GDPR)
*   **PECR (Privacy and Electronic Communications Regulations):**
    *   *Risk Area:* The automated cold outreach (B2B prospecting).
    *   *UK Law:* B2B cold email is generally permitted in the UK to corporate subscribers (e.g., `ltd`, `plc`, `LLP` domains) *provided* the email is relevant to their business and offers a clear opt-out. Sole traders and ordinary partnerships require prior consent.
    *   *Operational Rule:* The outreach script (`send_outreach.py`) must include a clear, frictionless opt-out mechanism (e.g., "Reply 'unsubscribe' to stop receiving these architecture notes").
*   **UK-GDPR (Lead Capture):**
    *   *Risk Area:* The Formspree email capture loop.
    *   *Requirement:* We must state exactly what the data will be used for at the point of collection, and we must maintain a compliant Privacy Policy detailing data retention (especially if later shifting to ConvertKit/Mailchimp).
    *   *Operational Rule:* A formal `Privacy_Policy.md` must be drafted and linked from the Formspree capture page before active lead scaling begins.

## 3. Commercial Structure (Entity Setup)
*   **Current State:** Operating as a sole trader/individual project.
*   **Future Requirement (Pre-Layer 3 Launch):** Before unfreezing and launching the "Premium Migration Audit Kit" via Stripe or Gumroad, the project should be routed through a formalized legal entity (e.g., a UK Limited Company or registered Sole Trader account).
    *   *Why:* To shield personal liability regarding the financial advice/decision-support nature of the content. A "Terms of Service" limiting liability for botched data migrations using our templates is commercially critical.

## Action Plan
1.  **Draft Privacy Policy:** Create `content/trust/Privacy_Policy.md` addressing UK-GDPR requirements for the Formspree data collection.
2.  **Update Outreach Templates:** Inject PECR-compliant opt-out language into `outreach_outbox/template_1.txt`.
3.  **Draft Terms of Service (Pre-Monetization):** Create a liability-limiting ToS document before the Layer 3 product is sold.