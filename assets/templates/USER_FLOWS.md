<!--
USER_FLOWS.md — User Flows
Purpose: step-by-step paths through the product (happy path + error path).
ID scheme: FLOW-xxx — LIGHT. Only main flows; CRUD variations can share one flow.
Rule: deep detail for auth and data-changing flows; one combined flow for generic CRUD.
Delete this comment block after filling.
-->

# User Flows

## FLOW-001 — <name>
**Trigger:** <!-- what the user does to start -->
**Scope:** main flow (or CRUD-generic)

**Steps:**
1. <!-- actor action -->
2. <!-- system response -->
3. <!-- ... -->

**Error / edge paths:**
- <!-- failure case → what the user sees / system does -->

**States:** <!-- list only if the flow has meaningful states (draft/submitted/etc.) -->
