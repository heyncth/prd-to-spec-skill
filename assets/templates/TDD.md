<!--
TDD.md — Technical Design Document  (NOT a test plan)
Purpose: system architecture, data flow, and component boundaries for developers/agents.
Depth rule: deep for auth, data pipelines, cross-service boundaries; brief for CRUD.
Test plans go to TESTING.md (conditional) — do not put them here.
Delete this comment block after filling.
-->

# Technical Design — <Project Name>

## Architecture
<!-- High-level components and how they talk. Mermaid/ASCII diagram welcome. -->

## Data flow
<!-- How a request moves through the system: entry → validation → business logic → storage → response.
     Cover the core flows from PRD. One subsection per critical flow. -->

## Component boundaries
<!-- What each module/service owns. What it must NOT do (to prevent coupling). -->

## Auth & security design
<!-- REQUIRED if REQ has auth/high-risk items: session/token model, permission checks,
     sensitive data handling. Merge into "Key technical decisions" only if trivial. -->

## Key technical decisions
<!-- Non-stack technical choices: caching, queues, pagination, error strategy, etc. -->

## Risks & open questions
<!-- Technical unknowns and their mitigation. Link D-xxx if already decided. -->
