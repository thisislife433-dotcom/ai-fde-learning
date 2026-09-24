"""Local recall practice with private spaced-review progress. No network."""
import argparse
import json
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CARDS = ROOT / "study" / "cards.json"
PROGRESS = ROOT / "progress" / "private" / "recall.json"
INTERVALS = [1, 3, 7, 14, 30]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--list", action="store_true", help="List cards without changing progress")
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be positive")
    cards = json.loads(CARDS.read_text(encoding="utf-8"))
    if args.list:
        for card in cards:
            print(f"{card['id']}: {card['question']}")
        raise SystemExit(0)
    state = json.loads(PROGRESS.read_text()) if PROGRESS.exists() else {}
    today = date.today()
    due = [c for c in cards if state.get(c["id"], {}).get("due", "0001-01-01") <= today.isoformat()]
    print(f"{len(due)} cards due. Progress is private in {PROGRESS}.")
    for card in due[:args.limit]:
        print(f"\n{card['id']}: {card['question']}")
        input("Answer aloud, then press Enter to reveal: ")
        print(card["answer"])
        rating = input("Recall without help? [y/N]: ").strip().lower()
        stage = min(state.get(card["id"], {}).get("stage", -1) + 1, len(INTERVALS)-1) if rating == "y" else 0
        state[card["id"]] = {"stage": stage, "due": (today + timedelta(days=INTERVALS[stage])).isoformat()}
        PROGRESS.parent.mkdir(parents=True, exist_ok=True)
        PROGRESS.write_text(json.dumps(state, indent=2), encoding="utf-8")
    print("Review complete. Commit study notes separately if you want them in GitHub.")
