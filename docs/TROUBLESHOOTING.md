# Troubleshooting by layer

Start with the first failing layer. A working interface does not prove the database, retrieval or model is correct.

| Symptom | Check | Next step |
|---|---|---|
| `python` not found | OS launcher/path | Windows: `py -3`; macOS/Linux: `python3` |
| `No module named lab` | Current folder | Run from the companion root containing `lab/` |
| Database missing | Whether seeding ran | `python -m lab seed`, then repeat the query |
| Results look dated | Fixture's `as_of` | The offline lab intentionally uses a fixed synthetic clock; it is not live telemetry |
| All records become unknown with a new `--as-of` | Observation ages | This is expected once they exceed the fictional freshness window |
| Empty upstream directory | Submodule checkout | `git submodule update --init --recursive` |
| Preparation refuses to overwrite | Existing `work/full-project` | Keep the existing work; choose a new `--output work/full-project-2` if necessary |
| Preparation reports changed upstream | Pinned commit or local edits | Preserve your edits, review the difference, and restore the documented clean revision before generating a new copy |
| Package pin cannot be installed | Python version, OS and exact resolver error | Use a separate Python 3.12 venv; resolve the specific incompatibility and record the tested lock |
| ODBC driver not found | Installed native Microsoft driver | Install ODBC Driver 18 for the actual host architecture; pip `pyodbc` is not the driver |
| SQL connection refused | Container health and port | Read `docker compose logs sql`; confirm the loopback port and ready message |
| SQL authentication failure | Correct identity/configuration | Use the matching generated local credentials, without printing them into logs or chat |
| Raw table SELECT denied | Using the agent identity | Expected after the permission setup; query the allowed view |
| Audit table missing | Prepared SQL setup | Ensure you ran the prepared copy's script including the audit table section |
| Pinecone dimension mismatch | Model and index dimensions | Use a separate correctly configured teaching index; do not delete shared data |
| Ingestion says unchanged but retrieval is empty | Cache versus target index | Verify target project/index and vectors; explicitly reindex with a fresh matching cache when appropriate |
| New index initially unavailable | Readiness | Check index status, then retry after it becomes ready |
| Model authentication/quota failure | Provider account/API access | Check provider billing, model access and credentials privately; no API entitlement is assumed |
| Local Ollama tool call failure | Legacy integration and chosen model | This branch is not verified. Use a documented tool-capable integration and test independently before relying on it |
| UI and CLI behave differently | Shared system prompt | Use the prepared teaching copy and compare the shared reasoner code |
| Repeated calls/graph limit reached | Prompt, tool errors and state | Inspect the visible trace, fix the failing tool/route and keep a bounded retry policy |
| Plausible answer, wrong facts | Source rows, timestamps and citations | Treat as a failed evaluation, not a successful run |
| Cloud costs continue after stopping | Disks, IPs, other services | Inspect retained resources and provider billing; do not assume zero usage |

## An effective help request

Share the command, the exact non-secret error, Python/OS version, which step you reached and what you expected. Remove API keys, passwords, connection strings, private records and session tokens. Do not upload `.env`.

## When returning months later

Start with the offline lab. Read the pinned source revision and verification record before updating dependencies. Upgrade one boundary at a time and rerun meaningful cases. Keep a known-good revision; a newer model or library is not automatically an improvement for this task.
