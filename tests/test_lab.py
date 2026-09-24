import json
import math
import sqlite3
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from lab.core import answer, append_audit, assess, load_fixture, query_shipments, seed_database


class DecisionTests(unittest.TestCase):
    def setUp(self):
        self.fixture = load_fixture()
        self.clock = datetime.fromisoformat(self.fixture["as_of"])
        self.row = dict(self.fixture["shipments"][0])

    def test_breach_has_traceable_policy_and_escalation(self):
        result = assess(self.row, self.clock)
        self.assertEqual(result["status"], "TEMPERATURE_BREACH")
        self.assertEqual(set(result["citations"]), {"TEMP-01", "ETA-01", "RISK-01"})

    def test_boundary_not_breached(self):
        self.row.update(temperature_c=4, risk="Low Risk")
        self.assertEqual(assess(self.row, self.clock)["status"], "WITHIN_LAB_LIMITS")

    def test_missing_and_nonfinite_temperature_are_unknown(self):
        for temperature in [None, math.nan, math.inf, "invalid"]:
            with self.subTest(temperature=temperature):
                self.row["temperature_c"] = temperature
                self.assertEqual(assess(self.row, self.clock)["status"], "UNKNOWN_CURRENT_STATUS")

    def test_stale_and_future_dates_are_unknown(self):
        for stamp in ["2026-09-23T09:00:00+00:00", "2026-09-25T09:00:00+00:00", "bad", "2026-09-24T09:00:00"]:
            with self.subTest(stamp=stamp):
                self.row["observed_at"] = stamp
                self.assertEqual(assess(self.row, self.clock)["status"], "UNKNOWN_CURRENT_STATUS")

    def test_lower_temperature_limit_is_checked(self):
        self.row["temperature_c"] = -0.1
        self.assertEqual(assess(self.row, self.clock)["status"], "TEMPERATURE_BREACH")


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "test.db"
        seed_database(self.path)
        self.clock = datetime.fromisoformat(load_fixture()["as_of"])

    def tearDown(self):
        self.tmp.cleanup()

    def test_seed_can_repeat_without_duplicates(self):
        seed_database(self.path)
        self.assertEqual(len(query_shipments(self.path)), 5)

    def test_sql_injection_is_a_value(self):
        self.assertEqual(query_shipments(self.path, "Melbourne' OR 1=1 --"), [])
        self.assertEqual(len(query_shipments(self.path)), 5)

    def test_melbourne_result_includes_unknown_status(self):
        result = answer("Which shipments in Melbourne need review?", self.path, self.clock)
        self.assertEqual(len(result["shipments"]), 3)
        self.assertEqual(result["shipments"][2]["status"], "UNKNOWN_CURRENT_STATUS")
        self.assertFalse(result["actions_executed"])

    def test_change_request_never_mutates_database(self):
        result = answer("Delete all shipments", self.path, self.clock)
        self.assertEqual(result["status"], "REFUSED")
        self.assertEqual(len(query_shipments(self.path)), 5)

    def test_policy_query_has_no_database_lookup(self):
        result = answer("What are the temperature rules?", Path("missing.db"), self.clock)
        self.assertEqual(result["status"], "POLICY_ONLY")
        self.assertTrue(any(r["id"] == "TEMP-01" for r in result["rules"]))

    def test_out_of_scope_is_clarified(self):
        self.assertEqual(answer("Tell me a joke", self.path, self.clock)["status"], "NEEDS_CLARIFICATION")

    def test_audit_append_preserves_previous_event(self):
        path = Path(self.tmp.name) / "audit.jsonl"
        append_audit(path, {"id": 1})
        append_audit(path, {"id": 2})
        self.assertEqual([json.loads(line)["id"] for line in path.read_text().splitlines()], [1, 2])


if __name__ == "__main__":
    unittest.main()
