---
name: prd-to-spec-skill
description: Fast MVP project foundation from a PRD or raw idea — docs/ specs, root AGENTS.md, implementation plan with cross-referenced IDs, ready for Claude Code / Codex / Cursor in one session. Built for small projects and vibe coding, not heavyweight delivery methods. Use when the user wants to set up project docs from a PRD, prepare a project foundation for AI coding agents, add missing docs, update living docs after a feature/tech/schema change, or audit drift between docs and code.
---

# PRD to Spec — Fast MVP Project Foundation

Prepare the project foundation (docs + AGENTS.md + implementation plan) before coding starts: approval gates, two-round pushback, mechanical ID validation. Target: **MVP-ready foundation in one session** for small projects — not a full-product delivery method. Docs in English; talk to the user in their language.

## Non-negotiable rules

1. **No fabrication.** Missing critical information → ask the user. Never invent decisions on their behalf.
2. **No silent overrides.** Never overwrite or change a locked decision without approval.
3. **Two-round pushback.** When you find a gap, contradiction, or risky choice: state the problem + propose options (round 1). If the user rejects your recommendation on something that significantly affects the app, push back one more time with concrete risks and trade-offs (round 2). If the user still keeps their choice: respect it, log it to `DECISIONS_LOG.md` (decision, alternatives, reason, trade-offs, constraints, date), and move on. Never a third round.
4. **Research boundary.** During discovery and tech-stack selection, only search official docs / known solutions after asking the user for scope and constraints first. No broad searching when the current plan is already sound. The chain "self-debug → search GitHub issues, Stack Overflow, Reddit" belongs in `AGENTS.md` for the coding phase — not here.
5. **No empty files.** Conditional docs that do not apply are skipped or merged — never created empty.
6. **No mid-flight stops.** If you must pause (gate, question, error), say so explicitly. Track progress in a todo list; mark each file done as you finish it.
7. **Tag assumptions.** Anything you generated that the user did not explicitly confirm gets an inline `[ASSUMPTION: ...]` tag. Confirmed content carries no tag. Assumptions surface at every gate for one-click confirm-or-fix.

## Speed rules (this is an MVP skill)

1. **Default tier S.** Decide a document tier at Gate 0, announce it, let the user override:
   - **S (default, small/MVP project):** `PRD`, `USER_STORIES`, `USER_FLOWS`, `TECH_STACK`, `TDD`, `IMPLEMENTATION_PLAN`, `AGENTS.md` + conditional DB/API. Short files, no filler sections.
   - **M (added risk:** auth, payments, real user data): + fuller acceptance criteria, `UI_UX_SPEC` detail, error paths.
   - **L (rare):** only if the user asks or the project is genuinely multi-module. Never L by default.
2. **One question round, not a drip.** Discovery asks numbered questions in as few rounds as possible (target: 1–2). Every question carries a recommended answer so the user can accept it in one keystroke. Never ask a question whose prerequisite is unanswered.
3. **No research when the plan is sound** (rule 4). No re-interviewing what the PRD already answers.
4. **Gates are one line for tier S:** "Group G1 done, 3 files, validation clean — approve?" Not a wall of text.

## Modes

Detect the project state first, announce the mode, and get confirmation before doing work (Gate 0).

| Mode | Condition | Behavior |
|---|---|---|
| **New** | No `docs/` yet | Full generation flow below |
| **Patch** | `docs/` exists | Only add missing parts or edit sections the user names. Never silently change locked decisions |
| **Drift audit** | `docs/` + code exist | Compare docs vs code, produce a diff report with severity. Do not edit anything before approval |

## Execution flow

### Phase 0 — Intake & mode detect

1. Input:
   - **Existing PRD, complete** → read all of it before saying anything.
   - **Raw idea or thin PRD** → stop. Ask numbered clarifying questions in one round (speed rule 2): scope, users, constraints, risks, success criteria — each with a recommended answer. No output before answers.
2. Detect mode (New / Patch / Drift audit) from the repo state.
3. Announce mode + document tier (S/M/L) + planned outputs → get confirmation. **Gate 0.**

### Phase 1 — Discovery & findings report

1. Read everything: PRD, existing `docs/`, and current code (if any).
2. Produce a findings report covering: gaps, contradictions between sections, missing decisions, and risk areas (auth, data, core flows).
3. Ask scope/constraints before comparing options. Search official docs only after scope is clear (rule 4).
4. Apply two-round pushback (rule 3) for every significant finding.
5. **Readiness check before Gate 1** — answer all five; any NO = say so and fix before generating:
   - [ ] Requirements clear enough to write without inventing?
   - [ ] Tech stack decided (or proposed and confirmed)?
   - [ ] Data entities knowable from PRD/code?
   - [ ] Auth/safety boundary known?
   - [ ] Every open item tagged `[ASSUMPTION]` or answered?
6. **Gate 1:** user approves findings + recommendations + readiness verdict before any generation starts.

### Phase 2 — Generate (3 groups, 3 sub-gates)

Copy the needed templates from `assets/templates/`, fill them, and place them in `docs/` (flat — no subfolders unless the project is genuinely large). `AGENTS.md` goes to the repo root.

| Group | Files | Gate |
|---|---|---|
| G1 Foundation | `docs/PRD.md` → `docs/USER_STORIES.md` → `docs/USER_FLOWS.md` | Gate 1a |
| G2 Spec | `docs/UI_UX_SPEC.md` → `docs/TECH_STACK.md` → `docs/TDD.md` → `docs/DATABASE.md` → `docs/API_SPEC.md` | Gate 1b |
| G3 Plan & rules | `docs/IMPLEMENTATION_PLAN.md` → `AGENTS.md` | Gate 1c |

Conditional files: `docs/DATABASE.md` (skip if no database), `docs/API_SPEC.md` (skip if no API), `docs/TESTING.md` (only if complex logic needs a test plan), `docs/DECISIONS_LOG.md` (only if significant decisions/trade-offs occurred).

**Depth by risk:** write deep detail for auth, data models, and core flows; keep CRUD and simple UI brief. Merge trivial sections instead of creating files.

After G3: run `python assets/scripts/validate_ids.py` from the project root. Fix violations, re-run until clean. **Gate 2 (final):** summary of outputs + validation result for user approval.

### Phase 3 — Living-docs update (user changes feature / tech / schema)

1. Determine impact mechanically first: `python assets/scripts/validate_ids.py --impact REQ-xxx` (or `US/API/TBL` id) → reverse graph lists the stories, endpoints, tables, and plan tasks that reference it. Add manual judgment on top.
2. Present the impact list → get approval → edit only those files.
3. Re-run `validate_ids.py`.
4. Append to `DECISIONS_LOG.md` if the change involved a trade-off. A superseded decision is marked `superseded by D-xxx` — never rewritten or deleted.

### Phase 4 — Drift audit report

Report only, no edits before approval. Each finding: file + line evidence (quote the actual line), docs side vs code side, severity:

- **P0** — drift can cause data loss, security exposure, or a broken deploy
- **P1** — blocks setup, a core flow, or API integration
- **P2** — misleading docs an agent would act on wrongly
- **P3** — naming, examples, polish

Approved fixes go through Phase 3.

## ID scheme & validation

| Prefix | Where | Rule |
|---|---|---|
| `REQ-xxx` | `PRD.md` | Core requirements |
| `US-xxx` | `USER_STORIES.md` | Each story maps to ≥ 1 `REQ` |
| `FLOW-xxx` | `USER_FLOWS.md` | Light — only main flows, no full coverage mandate |
| `API-xxx` | `API_SPEC.md` | Each endpoint maps to ≥ 1 `REQ` or `US`, and matches `TBL` if a DB exists |
| `TBL-xxx` | `DATABASE.md` | Tables |

Mandatory checks (run by `validate_ids.py`): no duplicate IDs; no orphan `US`/`API`; `US` → `REQ`; `API` → `REQ`/`US`; `API` → `TBL` when both files exist. Do not invent ID systems beyond these. Implementation tasks use plain checkboxes `[ ]` / `[x]` referencing `REQ-xxx` — no task ID prefix.

## Output discipline

- One job per doc file; no repetition across files.
- Templates carry `<!-- REQUIRED -->` and `<!-- IF: condition -->` markers — drop markers and inapplicable sections before delivering.
- Strip `[ASSUMPTION]` tags as the user confirms them; anything unconfirmed ships with the tag visible.
- Never pad to look thorough; never cut critical detail to look short. Tier S files stay short by design.
- Todo list tracks every file; report status at each gate.
