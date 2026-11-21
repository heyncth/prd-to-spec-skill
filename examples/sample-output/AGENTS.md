# AGENTS.md — Working Agreement for Coding Agents

## 1. Context: read order
On session start, read in this order:
1. `docs/PRD.md` — what the product must do
2. `docs/TDD.md` — architecture and data flow
3. `docs/IMPLEMENTATION_PLAN.md` — what to build next
4. Other `docs/` files only when the task touches them (API, DB, flows)

Never implement from memory of a doc — re-read the relevant section.

## 2. Living-docs law
If code changes behavior, data shape, API contract, or tech stack:
1. Identify affected files in `docs/` — run `python assets/scripts/validate_ids.py --impact <ID>`.
2. Report them and get user approval BEFORE editing docs.
3. Re-run `python assets/scripts/validate_ids.py` after edits.
Never let docs drift silently from code.

## 3. Task progress
- Mark `[x]` in `docs/IMPLEMENTATION_PLAN.md` only after the task's `verify:` passes.
- `[~]` (reframed) and `[-]` (skipped) require a written reason and a user report.
- Never mark `[x]` on a red build or skipped verify.

## 4. When stuck (debug & search protocol)
1. Reproduce the error; read the full error + stack trace.
2. Check `docs/` (TDD, API_SPEC) for the intended behavior.
3. Fix from first principles; run the failing verify.
4. Still stuck → search: official docs → GitHub issues → Stack Overflow → Reddit.
5. Still stuck → stop and report to the user: exact error, what you tried, what you found.
Never guess a fix and commit it without a passing verify.
