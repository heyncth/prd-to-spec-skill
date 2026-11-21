# Tech Stack

## Overview
Single Node.js service, SQLite storage, deployed as one container. No frontend.

## Choices

| Area | Choice | Rationale | Rejected alternatives |
|------|--------|-----------|-----------------------|
| Language / runtime | TypeScript, Node 22 | team knows it, tiny deploy | Go (overkill for MVP) |
| Framework | Fastify | fast, schema validation built in | Express (no validation) |
| Database | SQLite (better-sqlite3) | zero ops, single file fits constraint | Postgres (ops cost) |
| Auth | Static API key header | single-team MVP | OAuth (out of scope) |
| Hosting | Docker + any VPS | constraint: one container | Serverless (cold start hurts redirect) |

## Version constraints
Pin Fastify major; SQLite file lives on a volume.
