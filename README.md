# prd-to-spec-skill

> **MVP-ready project foundation in one session.**
> PRD or raw idea → approved docs, `AGENTS.md`, implementation plan — ready for your coding agent.
> Not a delivery method. Not a full-product framework. Preparation for small projects that need to start building today.

[Agent Skills](https://agentskills.io) standard (`SKILL.md`) — works with Claude Code, Codex, Cursor, GitHub Copilot, and any skills-compatible agent.

## Why this exists

Spec-kit, BMAD, and friends solve *"how to build a full product correctly"* — constitutions, per-feature loops, subagent reviews. Right for a 6-month build. Wrong for "I have an idea, give me docs today".

`prd-to-spec-skill` occupies the other end:

| You want | This skill |
|---|---|
| MVP / weekend project / small tool | ✅ default |
| Docs in one session, then code | ✅ |
| Nobody has time for 12 planning commands | ✅ |
| Multi-quarter product with a team of agents | ❌ use [spec-kit](https://github.com/github/spec-kit) |

## Three pillars

1. **Understand** — read the PRD, find gaps, ask in *one numbered round with recommended answers*, challenge risky choices. Two-round pushback protocol: disagree once, disagree harder with trade-offs, then log your call and move on.
2. **Establish** — generate approved docs (tier **S by default** for MVP, M/L only when risk justifies it), cross-referenced with `REQ / US / API / TBL` IDs, validated by a script — not by vibes.
3. **Maintain** — re-run modes for living docs: impact analysis through the ID graph (`--impact REQ-001` → affected stories, endpoints, tables, tasks), Patch, and a P0–P3 drift audit. Docs never silently rot.

**Human-approved decisions. AI-generated documentation. Continuously maintained context.**

## What makes it different

- **Approval-first**: nothing is written as settled before you confirm it.
- **Two-round pushback**: the agent must disagree with you — twice, with numbers — before obeying a risky choice.
- **Mechanical cross-doc validation**: `validate_ids.py` fails on orphan/duplicate/broken `REQ→US→API→TBL` links. No other foundation skill ships a validator.
- **`[ASSUMPTION]` tags**: anything the agent inferred but you never confirmed is visibly tagged until you confirm it. No silent fabrication.
- **Graph-driven impact**: docs are a connected graph; changes propagate through it deterministically.

## What it generates

| File | Scope |
|------|-------|
| `docs/PRD.md` | requirements `REQ-xxx` |
| `docs/USER_STORIES.md` | stories `US-xxx` → `REQ` |
| `docs/USER_FLOWS.md` | flows `FLOW-xxx` (light) |
| `docs/UI_UX_SPEC.md` | screens, states |
| `docs/TECH_STACK.md` | choices + rationale |
| `docs/TDD.md` | technical design (architecture, data flow) |
| `docs/DATABASE.md` | conditional — `TBL-xxx` |
| `docs/API_SPEC.md` | conditional — `API-xxx` |
| `docs/IMPLEMENTATION_PLAN.md` | checkboxes + `REQ` refs |
| `AGENTS.md` (root) | 4 working rules for coding agents |
| `docs/TESTING.md` | conditional — complex logic only |
| `docs/DECISIONS_LOG.md` | conditional — significant decisions only |

Conditional files are skipped when they don't apply — never created empty.

## Install

**Claude Code**

```bash
npx skills add <owner>/prd-to-spec-skill -a claude-code
# or manually
cp -r prd-to-spec-skill .claude/skills/   # project
cp -r prd-to-spec-skill ~/.claude/skills/ # global
```

**Codex**

```bash
cp -r prd-to-spec-skill .agents/skills/   # project
cp -r prd-to-spec-skill ~/.agents/skills/ # global
```

**Cursor / Copilot** — copy into `.agents/skills/` (Cursor also reads `.claude/skills/`; Copilot reads `.github/skills/`).

**Any agent via skills CLI**

```bash
npx skills add <owner>/prd-to-spec-skill -a claude-code -a codex -a cursor
```

## Use

```
/prd-to-spec-skill
```

Paste your PRD or raw idea. The skill detects the mode (`New` / `Patch` / `Drift audit`), announces the document tier, asks one numbered round of questions with recommended answers, reports findings, and asks for approval before writing anything.

Validation anytime:

```bash
python assets/scripts/validate_ids.py <project-root>          # full check
python assets/scripts/validate_ids.py --impact REQ-001 .      # what does this change affect?
```

## Positioning (for the curious)

Direct small skills (`code-idea`, `docs-ai-prd`, `ai-project-starter`) aim at general documentation; heavyweight kits (Spec Kit ~140k★, BMAD ~55k★, OpenSpec ~71k★) own the full-product lifecycle. This skill owns **fast preparation for small projects**: tier-S docs, one question round, gated approval, a validator, and lightweight living-docs maintenance.

## License

Apache-2.0
