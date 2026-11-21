<!--
TESTING.md — Conditional: create ONLY when complex logic needs a test plan
(auth flows, money, data transforms). Simple CRUD projects skip this file.
Purpose: what to test, how, and at which layer. Never pad with generic advice.
Delete this comment block after filling.
-->

# Testing Plan

## Strategy
<!-- Layers used (unit/integration/e2e) and why — 3–6 lines. -->

## Critical coverage
<!-- Only high-risk logic. One block per area. -->

### <Area — e.g. payment calculation>
**Linked:** REQ-xxx
**Cases:**
- <!-- happy path -->
- <!-- boundary / failure case -->
**Layer:** unit / integration
**Command:** <!-- how to run, e.g. npm test -- payment -->

## Out of scope for tests
<!-- What deliberately isn't tested and why (e.g. third-party UI). -->
