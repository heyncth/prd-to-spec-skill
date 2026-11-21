#!/usr/bin/env python3
"""Cross-document ID validation for prd-to-spec-skill.

Usage:
  python assets/scripts/validate_ids.py [project_root]
  python assets/scripts/validate_ids.py --impact REQ-001 [project_root]

Checks (default mode):
  1. No duplicate ID definitions (REQ/US/FLOW/API/TBL).
  2. Every US-xxx defines at least one REQ reference.
  3. Every API-xxx defines at least one REQ or US reference.
  4. Every referenced ID exists (no orphan references).
  5. If both API_SPEC.md and DATABASE.md exist but APIs never
     reference a TBL: warning only.

--impact mode: reverse-graph from one ID -> affected US/API/TBL
(id propagation over the docs) plus plan-task lines referencing them.
Exit 0 = clean / report printed, 1 = errors or bad usage.
"""
import re
import sys
from pathlib import Path

# Definition forms: table rows "| REQ-001 |" and headings "### US-001"
ROW_DEF = re.compile(r"^\|?\s*(REQ|US|FLOW|API|TBL)-(\d{3})\s*\|", re.M)
HEAD_DEF = re.compile(r"^#{1,6}\s*(REQ|US|FLOW|API|TBL)-(\d{3})\b", re.M)
ANY_ID = re.compile(r"\b(REQ|US|FLOW|API|TBL|D)-(\d{3})\b")
ID_FULL = re.compile(r"^(REQ|US|FLOW|API|TBL)-\d{3}$")

DOCS = {
    "PRD": "PRD.md",
    "USER_STORIES": "USER_STORIES.md",
    "USER_FLOWS": "USER_FLOWS.md",
    "UI_UX_SPEC": "UI_UX_SPEC.md",
    "TECH_STACK": "TECH_STACK.md",
    "TDD": "TDD.md",
    "DATABASE": "DATABASE.md",
    "API_SPEC": "API_SPEC.md",
    "IMPLEMENTATION_PLAN": "IMPLEMENTATION_PLAN.md",
    "TESTING": "TESTING.md",
    "DECISIONS": "DECISIONS_LOG.md",
}


def strip_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)


def load(root: Path) -> dict:
    docs = {}
    for key, name in DOCS.items():
        p = root / "docs" / name
        if p.exists():
            docs[key] = strip_comments(p.read_text(encoding="utf-8"))
    return docs


def impact(root: Path, target: str) -> int:
    if not ID_FULL.match(target):
        print(f"ERROR: bad id '{target}' (want REQ-001 / US-001 / API-001 / TBL-001)")
        return 1
    docs = load(root)
    if not docs:
        print(f"ERROR: no docs/ files found under {root}")
        return 1

    def blocks(text: str, prefix: str) -> dict:
        out = {}
        # cut at next id heading OR any level-2 section (e.g. an index table
        # after the entries must not join the last block)
        for m in re.finditer(
            rf"^#{{1,6}}\s*({prefix}-\d{{3}})\b.*?(?=^#{{1,6}}\s*{prefix}-\d{{3}}\b|^##\s|\Z)",
            text, re.M | re.S,
        ):
            out[m.group(1)] = m.group(0)
        return out

    affected = {target}
    us_blocks = blocks(docs.get("USER_STORIES", ""), "US")
    api_blocks = blocks(docs.get("API_SPEC", ""), "API")
    changed = True
    while changed:
        changed = False
        req_seeds = [a for a in affected if a.startswith("REQ-")]
        us_seeds = [a for a in affected if a.startswith("US-")]
        # forward edges only: REQ -> US, REQ/US -> API, API -> TBL
        if req_seeds:
            req_pat = re.compile(r"\b(?:" + "|".join(map(re.escape, req_seeds)) + r")\b")
            for uid, blk in us_blocks.items():
                if uid not in affected and req_pat.search(blk):
                    affected.add(uid)
                    changed = True
        seeds = req_seeds + us_seeds
        if seeds:
            seed_pat = re.compile(r"\b(?:" + "|".join(map(re.escape, seeds)) + r")\b")
            for aid, blk in api_blocks.items():
                if aid not in affected and seed_pat.search(blk):
                    affected.add(aid)
                    changed = True
        for aid in [a for a in affected if a.startswith("API-")]:
            if aid in api_blocks:
                for t in re.findall(r"\bTBL-\d{3}\b", api_blocks[aid]):
                    if t not in affected:
                        affected.add(t)
                        changed = True
    # schema change: a TBL target also hits the endpoints touching it
    if target.startswith("TBL-"):
        for aid, blk in api_blocks.items():
            if re.search(rf"\b{re.escape(target)}\b", blk):
                affected.add(aid)

    print(f"Impact of {target}:")
    for aid in sorted(affected):
        found = None
        for fname, text in docs.items():
            if re.search(rf"^#{{1,6}}\s*{re.escape(aid)}\b|^\|?\s*{re.escape(aid)}\s*\|",
                         text, re.M):
                found = fname
                break
        print(f"  {aid:<9} {DOCS.get(found, '?') if found else '(reference only)'}")

    plan = docs.get("IMPLEMENTATION_PLAN", "")
    hits = [i + 1 for i, line in enumerate(plan.splitlines())
            if re.search(r"\b(?:" + "|".join(map(re.escape, affected)) + r")\b", line)]
    if hits:
        print(f"  plan tasks at lines: {', '.join(map(str, hits))}")
    if len(affected) == 1:
        print("  (no downstream references)")
    return 0


def main() -> int:
    argv = sys.argv[1:]
    if argv and argv[0] == "--impact":
        if len(argv) < 2:
            print("ERROR: --impact needs an id, e.g. --impact REQ-001")
            return 1
        root = Path(argv[2]) if len(argv) > 2 else Path.cwd()
        return impact(root, argv[1])
    root = Path(argv[0]) if argv else Path.cwd()
    docs = load(root)
    if not docs:
        print(f"ERROR: no docs/ files found under {root}")
        return 1

    errors, warnings = [], []

    # 1. Collect definitions, detect duplicates (row + heading forms)
    defined = {}
    row_counts = {}
    for fname, text in docs.items():
        for m in ROW_DEF.finditer(text):
            full = f"{m.group(1)}-{m.group(2)}"
            row_counts[(full, fname)] = row_counts.get((full, fname), 0) + 1
            if row_counts[(full, fname)] == 2:
                errors.append(f"duplicate ID {full}: defined twice in {fname}")
        for pat in (ROW_DEF, HEAD_DEF):
            for m in pat.finditer(text):
                full = f"{m.group(1)}-{m.group(2)}"
                if full in defined and defined[full] != fname:
                    errors.append(
                        f"duplicate ID {full}: defined in {defined[full]} and {fname}"
                    )
                elif full not in defined:
                    defined[full] = fname

    # 2. US must reference >= 1 REQ
    us_text = docs.get("USER_STORIES", "")
    for us in [i for i in defined if i.startswith("US-")]:
        # scope to the US block: next US heading, any h2 section, or EOF
        m = re.search(rf"^#{{1,6}}\s*{us}\b.*?(?=^#{{1,6}}\s*US-\d{{3}}\b|^##\s|\Z)",
                      us_text, re.M | re.S)
        block = m.group(0) if m else us_text
        if not re.search(r"\bREQ-\d{3}\b", block):
            errors.append(f"{us}: no REQ reference")

    # 3. API must reference >= 1 REQ or US
    api_text = docs.get("API_SPEC", "")
    for api in [i for i in defined if i.startswith("API-")]:
        m = re.search(rf"^#{{1,6}}\s*{api}\b.*?(?=^#{{1,6}}\s*API-\d{{3}}\b|^##\s|\Z)",
                      api_text, re.M | re.S)
        block = m.group(0) if m else api_text
        if not re.search(r"\b(REQ|US)-\d{3}\b", block):
            errors.append(f"{api}: no REQ/US reference")

    # 4. Every referenced ID must be defined somewhere
    for fname, text in docs.items():
        for m in ANY_ID.finditer(text):
            full = m.group(0)
            if full.startswith("D-"):
                if "DECISIONS" not in docs or not re.search(
                        rf"\b{re.escape(full)}\b", docs["DECISIONS"]):
                    warnings.append(f"{fname}: references {full} not in DECISIONS_LOG")
                continue
            if full not in defined:
                errors.append(f"{fname}: orphan reference {full} (not defined)")

    # 5. API x DB coverage warning
    if "API_SPEC" in docs and "DATABASE" in docs:
        if not re.search(r"\bTBL-\d{3}\b", docs["API_SPEC"]):
            warnings.append("API_SPEC.md references no TBL despite DATABASE.md existing")

    for w in warnings:
        print(f"WARN : {w}")
    for e in errors:
        print(f"ERROR: {e}")
    if not errors and not warnings:
        print("OK   : all IDs valid")
    elif not errors:
        print(f"OK   : {len(warnings)} warning(s), 0 errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
