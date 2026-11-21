# PRD — Shrinkr (link shortener)

## Problem
Sharing long URLs is ugly and untrackable. Small teams need a self-hosted shortener with basic click counts.

## Goals
- Create a short link in one request
- Redirect reliably with low latency
- Show click count per link

## Non-Goals
- Custom domains, QR codes, full analytics
- User accounts beyond a single API key

## Users & Context
Internal team members who paste links into docs and chats.

## Requirements

| ID | Requirement | Priority (P0/P1/P2) | Risk (high/med/low) |
|----|--------------|----------------------|----------------------|
| REQ-001 | User can shorten a URL via API with an API key | P0 | high |
| REQ-002 | Short code redirects to the original URL (302) | P0 | high |
| REQ-003 | System counts clicks per short code | P1 | med |
| REQ-004 | Invalid/expired links return 404 with JSON error | P1 | low |
| REQ-005 | User can list their links with click counts | P2 | low |

## Core Flows
Shorten: client sends `POST /links` with URL + API key → server validates → returns short code.
Redirect: browser hits `/:code` → lookup → 302 + increment counter. Lookup miss → 404 JSON (REQ-004).

## Constraints
Single SQLite file, deploy as one container.

## Out of Scope
Browser UI (API only), analytics dashboard.
