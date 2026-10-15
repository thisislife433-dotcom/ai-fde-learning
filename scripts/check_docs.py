"""Check relative Markdown document/code links; upstream links use its submodule."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []
paths = [*ROOT.glob("*.md"), *(ROOT / "docs").rglob("*.md"),
         *(ROOT / "progress").glob("*.md"), *(ROOT / ".github").rglob("*.md")]
for path in sorted(paths):
    for raw in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
        target = raw.split("#", 1)[0]
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        full = (path.parent / target).resolve()
        if "upstream" in full.parts:
            continue
        if not full.exists():
            errors.append(f"{path.relative_to(ROOT)} -> {raw}")
if errors:
    raise SystemExit("Broken links:\n" + "\n".join(errors))
print("All companion relative document links resolve.")
