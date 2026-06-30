"""Company-level quality gate: keep the list free of junk/no-name companies.

Two independent controls:
  - blocklist (data/blocklist.json): exact company names + name substrings to drop
    (e.g. staffing agencies). Always applied.
  - allowlist_only (config): when true, ONLY show recognizable companies (those in
    the priority list). Stricter, lower coverage; off by default.
"""

from __future__ import annotations

import json

from . import paths, priority

_DEFAULT_BLOCKLIST = {"companies": [], "name_contains": []}


def load_blocklist() -> dict:
    try:
        with open(paths.BLOCKLIST_PATH, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError):
        return dict(_DEFAULT_BLOCKLIST)
    return {
        "companies": {c.lower().strip() for c in data.get("companies", [])},
        "name_contains": [s.lower() for s in data.get("name_contains", [])],
    }


def is_blocked(company: str, blocklist: dict) -> bool:
    name = (company or "").lower().strip()
    if not name:
        return True
    if name in blocklist.get("companies", set()):
        return True
    return any(token in name for token in blocklist.get("name_contains", []))


def is_recognized(company: str) -> bool:
    """True if the company is in the curated priority list (used by allowlist mode)."""
    return priority.rank(company) < priority.UNRANKED
