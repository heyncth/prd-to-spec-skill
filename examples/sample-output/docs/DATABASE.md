# Database Schema

## Entity relationships
```
TBL-001 links ── (1:N clicks is a column, no join table)
```

## Tables

### TBL-001 — links
**Purpose:** stored short links
**Maps to:** REQ-001, REQ-002, REQ-003, REQ-005

| Column | Type | Constraints | Notes |
|--------|------|-------------|-------|
| code | TEXT | PK | 7-char base62 |
| original_url | TEXT | NOT NULL | |
| clicks | INTEGER | NOT NULL DEFAULT 0 | REQ-003 |
| created_at | TEXT | NOT NULL | ISO-8601 |

**Relations:** none.
**Indexes:** none beyond PK (lookup is by PK).
**Sensitivity:** none (no PII).
