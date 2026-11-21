# Technical Design — Shrinkr

## Architecture
```
client ── HTTP ──> Fastify routes ──> links service ──> SQLite
                      │
                      └── api-key guard (X-API-Key → 401)
```
One process. No queue, no cache — click increments are synchronous SQLite writes.

## Data flow
**Shorten:** validate key → validate URL → generate code (7-char base62, collision retry) → insert row → respond 201.
**Redirect:** lookup by code → miss = 404 JSON → hit = `UPDATE clicks = clicks + 1` → 302.

## Component boundaries
- `routes/` — HTTP shapes only, no SQL.
- `service/` — business rules: code generation, validation. Owns all queries via `db/`.
- `db/` — schema + prepared statements. No Fastify imports.

## Auth & security design
API key compared with timing-safe equality; single key from env `API_KEY`. Request body size capped (1 KB). No user data stored — only URL + counter.

## Risks & open questions
- Write contention on hot links (SQLite single writer): acceptable for MVP, revisit at ~100 rps.
