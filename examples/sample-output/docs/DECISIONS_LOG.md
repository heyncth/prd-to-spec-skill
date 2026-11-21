# Decisions Log

## D-001 — Ship without rate limiting
- **Date:** 2026-11-21
- **Decision:** no rate limiting on API endpoints for MVP
- **Status:** active
- **Alternatives:** per-key fixed window; IP-based throttle
- **Reason:** single trusted team, MVP speed, revisit if exposed publicly
- **Trade-offs:** a leaked key can be hammered until noticed
- **Constraints:** one-day build window
- **Approved by:** user (round 2 of pushback)
