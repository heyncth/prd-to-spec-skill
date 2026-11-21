# API Spec

## Conventions
Base URL `/`, JSON in/out, auth = `X-API-Key` header. No pagination (MVP: ≤ 100 links).

## Error format
```json
{ "error": { "code": "not_found", "message": "unknown short code" } }
```

## Endpoints

### API-001 — Shorten a URL
**Maps to:** REQ-001, TBL-001
`POST /links`
**Auth:** API key
**Request:** `{ "url": "https://..." }` (must be http/https, ≤ 2048 chars)
**Success:** `201 { "code": "aB3xY9z", "short_url": "/aB3xY9z" }`
**Errors:** 400 invalid_url · 401 unauthorized

### API-002 — Redirect
**Maps to:** REQ-002, REQ-004, TBL-001
`GET /:code`
**Auth:** none (public redirect)
**Success:** `302` + `Location` header; increments TBL-001.clicks
**Errors:** 404 not_found

### API-003 — List links
**Maps to:** REQ-005, REQ-003, TBL-001
`GET /links`
**Auth:** API key
**Success:** `200 [ { "code", "original_url", "clicks", "created_at" } ]` newest first
**Errors:** 401 unauthorized

## Endpoint index

| ID | Method + Path | Maps to |
|----|---------------|---------|
| API-001 | POST /links | REQ-001 |
| API-002 | GET /:code | REQ-002, REQ-004 |
| API-003 | GET /links | REQ-005 |
