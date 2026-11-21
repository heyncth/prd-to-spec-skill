<!--
API_SPEC.md — Conditional: DELETE THIS FILE if the project exposes no API.
Purpose: endpoints consumed by clients (frontend, mobile, third parties).
ID scheme: API-xxx (required when this file exists).
Rules: each endpoint maps to >= 1 REQ-xxx or US-xxx and matches TBL-xxx when a DB exists
       (validated by validate_ids.py). Error shapes defined once, referenced everywhere.
Delete this comment block after filling.
-->

# API Spec

## Conventions
<!-- Base URL, versioning, auth mechanism, content type, pagination — one short section. -->

## Error format
<!-- Define the single error envelope once: status, code, message. -->

## Endpoints

### API-001 — <Name>
**Maps to:** REQ-xxx / US-xxx
`METHOD /path`

**Auth:** <!-- none / token / role -->
**Request:**
<!-- params/body fields: name, type, required, validation -->
**Success (2xx):** <!-- response shape -->
**Errors:** <!-- status → condition -->

## Endpoint index

| ID | Method + Path | Maps to |
|----|---------------|---------|
| API-001 | <!-- GET /users --> | REQ-001 |
