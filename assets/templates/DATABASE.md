<!--
DATABASE.md — Conditional: DELETE THIS FILE if the project has no database/storage schema.
Purpose: tables/entities, relations, migration notes.
ID scheme: TBL-xxx (required when this file exists).
Depth rule: deep for core/risk tables (auth, money, ownership); brief for simple CRUD tables.
Delete this comment block after filling.
-->

# Database Schema

## Entity relationships
<!-- Mermaid erDiagram or ASCII. One diagram covering all tables. -->

## Tables

### TBL-xxx — <table_name>
**Purpose:** <!-- one line -->
**Maps to:** REQ-xxx / API-xxx where relevant

| Column | Type | Constraints | Notes |
|--------|------|-------------|-------|
| id | | PK | |

**Relations:** <!-- foreign keys → other TBL-xxx -->
**Indexes:** <!-- only for known query patterns -->
**Sensitivity:** <!-- PII/secret columns if any -->

## Migration notes
<!-- Order, seed data, breaking changes. Delete if greenfield with no constraints. -->
