"""Inspectable data -> rules -> recommendation workflow, using only Python's stdlib.

This is intentionally deterministic. The companion lessons compare this flow
with the upstream model-controlled LangGraph agent. No weather is fabricated,
no live data is implied, and no operational action is executed.
"""
from __future__ import annotations

import json
import math
import re
import sqlite3
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = Path(__file__).resolve().parent / "data"


def load_policies(path: Path = DATA / "policies.json") -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_fixture(path: Path = DATA / "shipments.json") -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def seed_database(db_path: Path, fixture: dict | None = None) -> int:
    """Insert or update only our named fixture rows; preserve unrelated data."""
    fixture = fixture or load_fixture()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as connection:
        connection.execute("""CREATE TABLE IF NOT EXISTS shipments (
            id TEXT PRIMARY KEY, location TEXT NOT NULL, temperature_c REAL,
            observed_at TEXT NOT NULL, eta_delay_hours REAL,
            risk TEXT NOT NULL, delay_probability REAL)""")
        connection.executemany("""INSERT INTO shipments VALUES
            (:id, :location, :temperature_c, :observed_at, :eta_delay_hours, :risk, :delay_probability)
            ON CONFLICT(id) DO UPDATE SET
            location=excluded.location, temperature_c=excluded.temperature_c,
            observed_at=excluded.observed_at, eta_delay_hours=excluded.eta_delay_hours,
            risk=excluded.risk, delay_probability=excluded.delay_probability""", fixture["shipments"])
    return len(fixture["shipments"])


def query_shipments(db_path: Path, location: str | None = None) -> list[dict]:
    """A fixed, parameterised query through a read-only SQLite connection.

    This models a narrow tool contract, not a multi-user security boundary.
    The process and OS user still own the local database file.
    """
    uri = db_path.resolve().as_uri() + "?mode=ro"
    with sqlite3.connect(uri, uri=True) as connection:
        connection.row_factory = sqlite3.Row
        sql = "SELECT * FROM shipments"
        params = ()
        if location:
            sql += " WHERE lower(location) = lower(?)"
            params = (location,)
        sql += " ORDER BY id LIMIT 100"
        return [dict(row) for row in connection.execute(sql, params)]


def search_policies(query: str, policies: dict | None = None) -> list[dict]:
    """Transparent keyword retrieval for learning, NOT embedding/vector search."""
    policies = policies or load_policies()
    words = set(re.findall(r"[a-z]+", query.lower()))
    ranked = []
    for rule in policies["rules"]:
        terms = set(re.findall(r"[a-z]+", (rule["topic"] + " " + rule["text"]).lower()))
        score = len(words & terms)
        if score:
            ranked.append((score, rule))
    return [rule for _, rule in sorted(ranked, key=lambda item: (-item[0], item[1]["id"]))]


def assess(row: dict, as_of: datetime, policies: dict | None = None) -> dict:
    policies = policies or load_policies()
    rules = {rule["id"]: rule for rule in policies["rules"]}
    result = {"shipment": row["id"], "location": row["location"],
              "temperature_c": row["temperature_c"], "observed_at": row["observed_at"],
              "status": "WITHIN_LAB_LIMITS", "citations": [], "actions": [],
              "policy_version": policies["version"]}
    temperature = None
    try:
        observed = datetime.fromisoformat(row["observed_at"])
        age = (as_of - observed).total_seconds() / 60
        temperature = float(row["temperature_c"])
        valid = math.isfinite(temperature) and 0 <= age <= rules["DATA-01"]["max_age_minutes"]
    except (ValueError, TypeError, OverflowError):
        valid = False
    result["temperature_c"] = temperature if temperature is not None and math.isfinite(temperature) else None
    if not valid:
        result.update(status="UNKNOWN_CURRENT_STATUS", citations=["DATA-01"],
                      actions=[rules["DATA-01"]["action"]])
        return result
    result["citations"].append("TEMP-01")
    breached = not rules["TEMP-01"]["minimum_c"] <= temperature <= rules["TEMP-01"]["maximum_c"]
    if breached:
        result["status"] = "TEMPERATURE_BREACH"
        result["actions"].append(rules["TEMP-01"]["action"])
        if (row.get("eta_delay_hours") or 0) > rules["ETA-01"]["delay_hours"]:
            result["citations"].append("ETA-01")
            result["actions"].append(rules["ETA-01"]["action"])
    if row["risk"] == "High Risk" and (row.get("delay_probability") or 0) > rules["RISK-01"]["delay_probability"]:
        if not breached:
            result["status"] = "RISK_REVIEW"
        result["citations"].append("RISK-01")
        result["actions"].append(rules["RISK-01"]["action"])
    return result


def answer(question: str, db_path: Path, as_of: datetime) -> dict:
    """Limited classroom router. It is not a general natural-language AI."""
    if not question.strip() or len(question) > 1000:
        raise ValueError("Use a non-empty question of at most 1,000 characters.")
    words = set(re.findall(r"[a-z]+", question.lower()))
    if words & {"delete", "drop", "update", "insert", "ignore", "password", "secret"}:
        return {"mode": "offline deterministic lab", "status": "REFUSED", "trace": [],
                "message": "This lab only reads shipment facts and policy. It cannot execute changes or reveal secrets."}
    if not words & {"shipment", "shipments", "fleet", "truck", "trucks", "temperature", "risk", "policy", "rules", "sop", "delay"}:
        return {"mode": "offline deterministic lab", "status": "NEEDS_CLARIFICATION", "trace": [],
                "message": "Try: Which shipments in Melbourne need review? Or: What are the temperature rules?"}
    policies = load_policies()
    location = "Melbourne" if "melbourne" in words else "Sydney" if "sydney" in words else None
    policy_only = bool(words & {"policy", "rules", "sop"}) and not bool(words & {"shipment", "shipments", "fleet", "trucks"})
    if policy_only:
        found = search_policies(question, policies)
        return {"mode": "offline deterministic lab", "status": "POLICY_ONLY", "policy_version": policies["version"],
                "trace": [{"tool": "search_policies", "matched": [r["id"] for r in found]}], "rules": found}
    rows = query_shipments(db_path, location)
    return {"mode": "offline deterministic lab", "as_of": as_of.isoformat(),
            "data_source": "synthetic fixture, not live fleet data", "weather": "not connected",
            "status": "OK" if rows else "NO_DATA", "actions_executed": False,
            "trace": [{"tool": "query_shipments", "location": location, "rows": len(rows)},
                      {"tool": "apply_lab_policy", "version": policies["version"]}],
            "shipments": [assess(row, as_of, policies) for row in rows]}


def append_audit(path: Path, event: dict) -> None:
    """Append a teaching trace. Local JSONL is editable, not an immutable log."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(event, ensure_ascii=False, allow_nan=False) + "\n")
