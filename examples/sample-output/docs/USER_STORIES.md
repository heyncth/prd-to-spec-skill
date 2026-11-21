# User Stories

## Story index

| ID | Title | Maps to |
|----|-------|---------|
| US-001 | Shorten a URL | REQ-001 |
| US-002 | Follow a short link | REQ-002, REQ-004 |
| US-003 | See click count | REQ-003 |
| US-004 | List my links | REQ-005 |

## Stories

### US-001 — Shorten a URL
**Maps to:** REQ-001
**As a** team member **I want** to shorten a URL with one API call **so that** I can share a compact link.

**Acceptance criteria:**
- [ ] `POST /links` with valid URL + API key returns 201 and `{code, short_url}`
- [ ] Missing/invalid API key returns 401
- [ ] Malformed URL returns 400 with error body

### US-002 — Follow a short link
**Maps to:** REQ-002, REQ-004
**As a** link recipient **I want** to be redirected **so that** I reach the original page.

**Acceptance criteria:**
- [ ] `GET /:code` returns 302 to the stored URL
- [ ] Unknown code returns 404 JSON error
- [ ] Click counter increments on each successful redirect

### US-003 — See click count
**Maps to:** REQ-003
**As a** team member **I want** the click count per link **so that** I know a link is being used.

**Acceptance criteria:**
- [ ] Count is returned in list response, monotonically increasing

### US-004 — List my links
**Maps to:** REQ-005
**As a** team member **I want** to list my links **so that** I can reuse old codes.

**Acceptance criteria:**
- [ ] `GET /links` returns my links newest-first with counts
