"""Fetch the original project for a Git clone or an extracted companion ZIP.

Downloads only the named public source; does not install or execute its code.
Existing working trees are preserved and their revision must match.
"""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "upstream" / "cold-chain"
URL = "https://github.com/nimowhyca/cold-chain-logistics-FDE-Project.git"
SHA = "ef6633928950ef9c13115fb77439ccab40397790"

if __name__ == "__main__":
    if (ROOT / ".git").exists():
        subprocess.run(["git", "-C", str(ROOT), "submodule", "update", "--init", "--recursive"], check=True)
    elif not DEST.exists() or not any(DEST.iterdir()):
        DEST.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "clone", "--no-checkout", URL, str(DEST)], check=True)
        subprocess.run(["git", "-C", str(DEST), "checkout", "--detach", SHA], check=True)
    current = subprocess.check_output(["git", "-C", str(DEST), "rev-parse", "HEAD"], text=True).strip()
    if current != SHA:
        raise SystemExit("Existing source has a different revision. Preserve your work and review it before continuing.")
    print(f"Original source ready at {SHA}. No dependencies installed or application started.")
