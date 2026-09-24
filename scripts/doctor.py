"""Read-only environment checks; no network, installation or API calls."""
import importlib.util
import platform
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
print(f"Python: {platform.python_version()} ({sys.executable})")
print("Offline lab:", "ready" if sys.version_info >= (3, 10) else "requires Python 3.10+")
print("Machine architecture:", platform.machine())
for command in ["git", "docker"]:
    print(f"{command}: {'found' if shutil.which(command) else 'not found (not needed for offline lab)'}")
print("Upstream available:", (ROOT / "upstream/cold-chain/src/orchestrator.py").is_file())
print("Full-project config present:", (ROOT / "work/full-project/.env").is_file())
print("Live credentials and provider connectivity are not checked.")
print("For the original stack, use a separate Python 3.12 venv and install its dependencies and ODBC Driver 18.")
