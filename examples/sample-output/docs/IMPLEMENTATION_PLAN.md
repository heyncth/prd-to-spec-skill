# Implementation Plan

## Legend
- `[ ]` todo · `[x]` done + verify passed · `[~]` reframed (reason below task) · `[-]` skipped (reason below task)
- `depends on:` blocking tasks · `verify:` command or concrete check

## Group A — Setup (grouped)
- [ ] **Bootstrap project** (Fastify + TypeScript + lint) — REQ-001
  - steps: 1) init package + tsconfig 2) health route 3) lint config
  - verify: `npm run build && npm test` passes

## Group B — Core (atomic, risky)
- [ ] **API key guard** — REQ-001
  - depends on: Bootstrap project
  - verify: request without key → 401 (test in `auth.test.ts`)
- [ ] **Shorten endpoint** — REQ-001
  - depends on: API key guard
  - verify: `npm test -- links` — 201 / 400 / 401 cases
- [ ] **Redirect + click counter** — REQ-002, REQ-003
  - depends on: Shorten endpoint
  - verify: `npm test -- redirect` — 302, 404 JSON, counter increments
- [x] **Code generation with collision retry** — REQ-001
  - verify: unit test forces collision, second code accepted
- [~] **Rate limiting per key**
  - reframed: MVP ships without it; single trusted team (decision: D-001 in DECISIONS_LOG)
  - verify: —

## Group C — Read APIs (grouped)
- [ ] **List links endpoint** — REQ-005
  - depends on: Shorten endpoint
  - verify: `npm test -- list` — newest first, counts present
- [-] **Click count as separate endpoint**
  - skipped: covered inside list response (REQ-003), no `GET /links/:code/stats` needed
  - verify: —

## Rules for the coding agent
1. Never mark `[x]` without a passing verify.
2. `[~]` / `[-]` changes get reported to the user, never applied silently.
3. A task change that alters behavior → update affected docs first (see AGENTS.md living-docs law).
