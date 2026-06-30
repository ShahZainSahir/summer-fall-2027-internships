"""Company prestige ranking, used to curate capped sections.

When a section has more roles than its cap, we keep roles from the most
recognizable / sought-after companies first. Lower rank = higher priority.
Edit this list to taste — it only affects which roles make the cut when a
section is over its limit, not what gets collected.
"""

from __future__ import annotations

# Roughly ordered by how sought-after they are for SWE/ML interns.
TOP_COMPANIES = [
    "amazon", "google", "microsoft", "apple", "meta", "nvidia", "salesforce",
    "jpmorgan", "goldman", "morgan stanley", "capital one",
    "openai", "anthropic", "stripe", "databricks", "palantir", "scale ai",
    "ramp", "plaid", "coinbase", "robinhood", "airbnb", "dropbox", "notion",
    "figma", "snowflake", "datadog", "mongodb", "cloudflare", "pinterest",
    "reddit", "discord", "instacart", "doordash", "roblox", "unity", "duolingo",
    "brex", "mercury", "vercel", "replit", "perplexity", "cohere", "mistral ai",
    "hugging face", "together ai", "groq", "cerebras", "anduril",
    "applied intuition", "skydio", "neuralink", "two sigma", "jane street",
    "citadel", "optiver", "jump trading", "hudson river trading", "drw", "imc",
    "akuna", "samsara", "affirm", "sofi", "gusto", "asana", "gitlab",
    "hashicorp", "confluent", "elastic", "retool", "airtable", "benchling",
    "faire", "flexport", "lyft", "chime", "gemini", "kraken", "circle",
    "wealthsimple", "niantic", "twitch", "sentry", "postman", "linear",
    "sourcegraph", "amplitude", "segment", "twilio", "okta", "1password",
    "crowdstrike", "sentinelone", "wiz", "snyk", "rippling", "deel", "toast",
    "nubank", "whatnot", "ironclad", "vanta", "cockroach labs", "temporal",
    "fivetran", "airbyte", "dbt labs", "weights & biases", "pinecone",
    "runway", "character.ai", "glean", "harvey", "grammarly", "canva", "miro",
    "loom", "coursera", "webflow", "checkr", "lattice", "gong", "zapier",
]

_RANK = {name: i for i, name in enumerate(TOP_COMPANIES)}
UNRANKED = 10_000


def rank(company: str) -> int:
    """Lower = more sought-after. Unknown companies sort last."""
    c = (company or "").strip().lower()
    if c in _RANK:
        return _RANK[c]
    for name, i in _RANK.items():
        if name in c:  # e.g. "Stripe, Inc." contains "stripe"
            return i
    return UNRANKED
