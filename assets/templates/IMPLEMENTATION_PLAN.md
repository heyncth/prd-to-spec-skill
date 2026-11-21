<!--
IMPLEMENTATION_PLAN.md — Implementation Plan
Purpose: ordered, verifiable tasks for the coding agent.
Rules:
  - Checkboxes only: [ ] = todo, [x] = done. No task ID prefixes.
  - Reference REQ-xxx / US-xxx per task so progress traces back to requirements.
  - SIMPLE work → grouped tasks (one task, several steps).
  - COMPLEX / error-prone work → atomic tasks, each with dependencies + a verify step.
  - Verify must be a concrete command or check, not "make sure it works".
Delete this comment block after filling.
-->

# Implementation Plan

## Legend
- `[ ]` todo · `[x]` done · `depends on:` blocking tasks · `verify:` command or concrete check

## Group A — Setup & foundations (grouped)
- [ ] **Bootstrap project** (scaffolding, lint, CI) — REQ-xxx
  - steps: 1) ... 2) ...
  - verify: `npm run build` passes

## Group B — Core features (split atomic where risky)
- [ ] **Auth: email+password login** — REQ-xxx
  - depends on: Bootstrap project
  - verify: `npm test -- auth` + manual login on localhost
- [ ] **Auth: session expiry handling** — REQ-xxx
  - depends on: Auth: email+password login
  - verify: expired token rejected with 401

## Group C — CRUD & misc (group aggressively)
- [ ] **List + create + edit for <entity>** — REQ-xxx
  - steps: shared list/detail pattern per UI_UX_SPEC
  - verify: `npm test -- <entity>`

## Rules for the coding agent
1. Never mark [x] without a passing verify.
2. A task change that alters behavior → update affected docs first (see AGENTS.md living-docs law).
