# Asset & Infrastructure Optimization Plan

This document aligns the project's operational architecture with the currently available subscription stack to achieve maximum leverage and long-term sustainable monetization while containing overhead.

## Current Available Subscriptions
1.  **ChatGPT / Gemini (LLMs):** Advanced reasoning, content generation, and strategy validation.
2.  **Retool:** Rapid internal UI development, database interaction, and custom application building.
3.  **Supabase:** Open-source Firebase alternative (Postgres database, Authentication, Edge Functions, Storage).
4.  **Google One:** High-capacity cloud storage and workspace integration.
5.  **OpenClaw Agent:** Autonomous execution, file management, cron scheduling, and orchestration.

## Phase 1 (Validation) Optimization: The $0 Incremental Cost Stack
The current static site (GitHub Pages) + Formspree + local SMTP script model costs $0 in new subscriptions. This is the correct strategy for validation. However, as we scale, we will hit limits (e.g., Formspree's 50/month limit).

## Phase 2 (Scaling): Leveraging the Paid Stack

To reach long-term sustainable monetization, we must transition from static assets to a dynamic, scalable infrastructure using the tools already paid for.

### 1. Replacing Formspree with Supabase + Retool (Lead Capture & CRM)
*   **The Problem:** Formspree is a temporary fix. It doesn't scale without a paid tier, and it lacks CRM capabilities.
*   **The Solution:** 
    *   Use **Supabase** as the primary Postgres database for lead capture. Replace the Formspree endpoint on the site with a Supabase edge function or direct API call.
    *   Use **Retool** to build a custom, internal CRM dashboard. This dashboard will connect directly to Supabase, allowing the operator to view leads, track checklist downloads, and manage outreach targets visually, eliminating the need for paid tools like HubSpot or Mailchimp in the early scaling phase.

### 2. Evolving the Layer 3 Offer (The "Software-as-a-Service" Pivot)
*   **The Problem:** The Premium Migration Audit Kit is currently a static digital download ($99 PDF/Spreadsheet). Digital downloads suffer from high piracy and low recurring revenue.
*   **The Solution:** We have Retool and Supabase. We can build the QASEM Architecture Map and Vendor Evaluation Scorecard as an interactive, authenticated web application.
    *   **Architecture:** Supabase handles user auth and saves their audit data. Retool (via Retool Portals/External Apps if available on the tier, or a custom frontend interacting with Supabase) provides the interactive evaluation interface.
    *   **Monetization Shift:** Instead of a one-time $99 PDF, it becomes a dynamic "Stack Audit & Migration Planner" tool. This commands a higher price point or enables a low-cost subscription model for continuous stack monitoring.

### 3. Optimizing OpenClaw Execution Costs
*   **The Problem:** OpenClaw autonomous loops (cron jobs) consume API credits. Polling or inefficient scripting drains capital.
*   **The Solution:**
    *   **Strict Heartbeat Management:** Ensure `HEARTBEAT.md` remains empty unless actionable context is required.
    *   **Batch Processing:** The Python SMTP script and the factual audits are already batched via cron. We must maintain this discipline. Avoid rapid-polling loops.
    *   **Delegation to Supabase Edge Functions:** For repetitive, data-heavy tasks (e.g., parsing incoming lead webhooks), shift the computation from OpenClaw's local context to Supabase Edge Functions, utilizing the existing subscription tier.

## Immediate Action Items for the Operator
1.  **Supabase Initialization:** Create a new Supabase project named `qbo-stack-advisor`. Retrieve the Project URL and Anon Key.
2.  **Database Schema:** Define a simple `leads` table in Supabase (columns: `id`, `name`, `email`, `firm`, `created_at`).
3.  **Form Transition:** Once the Supabase endpoint is ready, OpenClaw will rewrite `download-risk-checklist.md` to post directly to Supabase, bypassing Formspree entirely.