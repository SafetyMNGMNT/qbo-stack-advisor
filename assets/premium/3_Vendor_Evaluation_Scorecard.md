# Vendor Evaluation Scorecard
*Premium Migration Audit Kit*

## Objective
A structured scoring matrix to evaluate potential replacement tools (or validate existing ones) against the QuickBooks Automation Stack Evaluation Model (QASEM).

## Scoring Matrix (Rate 1-5 for each criteria)
*1 = Critical Risk/High Friction | 5 = Highly Secure/Low Friction*

### Tool Name: _______________________

**1. Failure Mode & Risk (FMR)**
*   Does it fail safely? (e.g., pauses and alerts vs. drops data silently)
*   Does it respect the designated Source of Truth?
*   *Score:* [   ]

**2. Audit Trail Strength (ATS)**
*   Are changes logged?
*   Are failed API payloads accessible for troubleshooting?
*   *Score:* [   ]

**3. Integration Friction (IFS)**
*   Does it use official, stable APIs?
*   Does it handle QBO API rate limits gracefully?
*   *Score:* [   ]

**4. Cost Per Client Scaling (CPCS)**
*   Is the pricing model viable as client volume doubles?
*   Does it charge punitively per transaction/task?
*   *Score:* [   ]

**5. Automation Depth (ADS)**
*   Does it eliminate manual categorization, or just move the data?
*   Does it handle exceptions (e.g., multi-currency, complex tax) natively?
*   *Score:* [   ]

---
**Total Score: [   ] / 25**

### Action Thresholds
*   **20 - 25:** Approved for integration.
*   **15 - 19:** Acceptable, but requires documented workarounds for identified failure modes.
*   **< 15:** High Risk. Seek alternative vendor. Do not integrate into core financial workflows.