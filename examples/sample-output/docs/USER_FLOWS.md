# User Flows

## FLOW-001 — Shorten a link
**Trigger:** client has a long URL
**Scope:** main flow

**Steps:**
1. Client sends `POST /links` with `url` + `X-API-Key`
2. Server validates key and URL format
3. Server generates unique code, stores row
4. Server returns 201 with `{code, short_url}`

**Error / edge paths:**
- Bad key → 401 JSON; bad URL → 400 JSON
- Code collision → regenerate (retry once, then 500)

## FLOW-002 — Redirect (CRUD-generic read path)
**Trigger:** anyone opens `/:code`

**Steps:**
1. Look up code
2. Hit → increment `clicks`, 302 to original URL
3. Miss → 404 JSON (REQ-004)
