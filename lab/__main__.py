import argparse
import json
from datetime import datetime
from pathlib import Path

from .core import ROOT, answer, append_audit, load_fixture, load_policies, query_shipments, seed_database


def main():
    parser = argparse.ArgumentParser(description="Offline FDE teaching lab. No network calls or API fees.")
    parser.add_argument("command", choices=["demo", "seed", "ask", "sql", "policy"])
    parser.add_argument("question", nargs="?", default="Which shipments in Melbourne need review?")
    parser.add_argument("--db", type=Path, default=ROOT / "runtime" / "shipments.db")
    parser.add_argument("--as-of", help="ISO datetime with timezone; default is the synthetic fixture clock")
    args = parser.parse_args()
    try:
        if args.command in {"demo", "seed"}:
            count = seed_database(args.db)
            if args.command == "seed":
                print(f"Seeded {count} synthetic shipments in {args.db}.")
                return
        if args.command == "policy":
            result = load_policies()
        elif args.command == "sql":
            result = query_shipments(args.db)
        else:
            clock = datetime.fromisoformat(args.as_of or load_fixture()["as_of"])
            if clock.utcoffset() is None:
                raise ValueError("--as-of must include a timezone, for example +00:00.")
            result = answer(args.question, args.db, clock)
            append_audit(ROOT / "runtime" / "audit.jsonl", {"question": args.question, "response": result})
        print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))
    except (ValueError, OSError, __import__("sqlite3").Error) as error:
        parser.exit(1, f"Lab error: {error}\nRun 'python -m lab seed' first if the database is missing.\n")


if __name__ == "__main__":
    main()
