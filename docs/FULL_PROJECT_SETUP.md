# Run the original AI stack locally

This route prepares the actual upstream SQL Server, Pinecone, LangGraph and Streamlit project. The offline lab is a prerequisite teaching exercise, not evidence that these external integrations work.

**Status:** preparation and Python syntax are checked; Docker, ODBC, SQL, Pinecone and paid model integration must be verified on your own machine/accounts. No cloud server is required. No service is started by the preparation helper.

## 1. Check prerequisites

- Git and Python 3.12.
- Docker with Linux containers and adequate memory. The original SQL Server Linux image is supported on Intel/AMD x86-64 hosts. Apple Silicon users can do the offline lab natively, but should use a supported x86-64 Linux/Windows Docker host for the full SQL route; do not assume emulation is supported.
- Microsoft ODBC Driver 18 for SQL Server installed on the host running Python. `pyodbc` alone does not install the driver.
- VS Code's Microsoft **SQL Server (mssql)** extension, or another SQL client that understands `GO` batches.
- A Pinecone Starter account and your own API access if you choose the documented OpenAI mode.
- A few GB for the source and Python dependencies; the source's requirements include large ML packages. Begin with the offline mode if the machine is small.

Official references: [Microsoft container quickstart](https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-docker?view=sql-server-ver17) and [ODBC driver downloads](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver17).

## 2. Get the pinned original and prepare a learning copy

From the companion root:

```bash
git submodule update --init --recursive
python scripts/prepare_full_project.py
```

For an extracted ZIP without parent Git metadata, run `python scripts/fetch_upstream.py` instead of the `git submodule` command, then run the preparation command.

This copies the pinned source to ignored `work/full-project`. It preserves the original submodule and generates private local SQL passwords. It refuses to overwrite an existing working directory. For another isolated copy, use `--output work/full-project-2`; adapt subsequent paths accordingly.

The helper supplies a shared system prompt, makes the paid model configurable, explicitly selects an embedding model, drops the inherited cache, scopes a new cache to the index/dimension, rejects index deletion for dimension repair, labels the weather heuristic, limits the UI graph to 12 steps and creates the missing audit-table setup. Review `LOCAL_CHANGES.json` inside the copy. Remaining issues are in [Review findings](REVIEW_FINDINGS.md).

## 3. Create an isolated Python environment

Windows PowerShell:

```powershell
cd work/full-project
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

macOS/Linux:

```bash
cd work/full-project
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

The explicit interpreter paths avoid changing your shell execution policy. In subsequent commands, `python` means this venv's Python. Windows can use `.\.venv\Scripts\python.exe`; macOS/Linux can use `.venv/bin/python` without activating the environment.

If a pinned package is unavailable or conflicts, record the exact resolver error. Do not silently upgrade the entire environment. The source pins direct dependencies but is not a tested transitive lock for every OS. Once your integration works, record `python -m pip freeze` in a local file and review it before committing a dependency lock to the companion.

## 4. Configure provider access privately

Open the generated `.env` in `work/full-project`. Keep the generated SQL values. Add your own `OPENAI_API_KEY` and `PINECONE_API_KEY` in that file, never in chat, source files or a commit.

Defaults in the learning copy:

| Variable | Default and meaning |
|---|---|
| `Agent_llm` | `OPENAI`, the documented provider path |
| `OPENAI_MODEL` | `gpt-4.1-mini`, a lower-cost teaching choice |
| `Embeddings_model` | `OPENAI` |
| `OPENAI_EMBEDDING_MODEL` | `text-embedding-3-small`, 1,536 dimensions by default |
| `SQL_SERVER_HOST` | `127.0.0.1` |
| `SQL_SERVER_PORT` | `1433` |
| `LANGSMITH_TRACING` | `false` |

The original hard-codes `gpt-4o` for its OpenAI path; the source is preserved, and the learning copy makes that choice configurable. Set `OPENAI_MODEL=gpt-4o` to compare it, using the same evaluation cases and budget controls. Model availability depends on your account.

The original also includes local embedding and Ollama branches. They still use Pinecone, may download large models, and the legacy Ollama class needs verification for tool calling. They are not an already-verified free equivalent of this guide. The companion's offline lab is the zero-API route that has been exercised here.

## 5. Start an isolated teaching database

From `work/full-project`:

```bash
docker compose up -d sql
docker compose logs sql
```

Wait for SQL Server to report that it is ready for client connections. The Compose file uses Developer edition for learning and binds the SQL port to your local loopback interface. Running it accepts the SQL Server image's EULA as configured by `ACCEPT_EULA=Y`; review Microsoft's terms before you run it.

The mutable `2022-latest` image tag follows the upstream tutorial. For a repeatable cloud release, record and pin the tested image digest. Do not call this tag immutable.

## 6. Ingest the source data

```bash
python scripts/ingest_legacy_data.py
```

This script **replaces** its target raw table in the isolated teaching database. Run it once on initial setup; do not point it at an existing business database. The source uses `master`, which is acceptable only as a tutorial convenience here; choose a dedicated database for a real application.

In the SQL extension, connect to `127.0.0.1,1433` as `sa`, using your local `.env` password, database `master`. The original connection settings trust the local certificate and do not encrypt. These settings are confined to this local exercise and must be redesigned for a remote connection.

Check:

```sql
SELECT COUNT(*) AS total_rows FROM dbo.TBL_SC_FLEET_HIST_RAW;
```

The pinned CSV contains **32,065** data rows. A different count means you need to investigate before continuing.

## 7. Create and verify agent permissions

Run `scripts/setup_security_and_view.sql` from the **prepared copy** in the SQL editor as the admin. It contains the generated password and the audit table addition. It is an initial setup script, not an idempotent migration; do not rerun it blindly after objects already exist.

Connect again as the configured `SQL_AGENT_USER` with `SQL_AGENT_PASSWORD`. Verify:

```sql
-- Expected to succeed:
SELECT TOP 5 * FROM FDE_VIEWS.VW_ACTIVE_FLEET;

-- Expected to fail under the agent identity:
SELECT TOP 5 * FROM dbo.TBL_SC_FLEET_HIST_RAW;
```

The role can SELECT the view and INSERT audit events. Do not grant it administrator permissions to resolve an error.

## 8. Index the policy

```bash
python scripts/ingest_sop_pinecone.py
```

This is the first command in this guide that can make paid embedding calls. It creates/uses the named teaching index in `aws/us-east-1`. Keep within Pinecone Starter's applicable limits and region; changing plan can introduce a monthly minimum.

Confirm that the index becomes ready and has vectors. The original code does not explicitly poll index readiness before continuing; a newly created index may require a short wait and retry. If the tool says everything is unchanged but the index is empty, inspect the target/index identity and the local cache. Do not delete a live/shared index to recover a lab.

A fresh copy excludes the upstream committed cache. Later changing model, splitter, target project or manually recreating the index requires explicit reindexing, not a simple rerun with an old cache.

## 9. Check the tools, then the UI

```bash
python src/agent_tools.py
python -m streamlit run src/ui.py --server.address 127.0.0.1 --server.port 8501
```

Tool checks make external requests, including an embedding request for retrieval. Inspect their individual outputs. Open `http://127.0.0.1:8501` on the same machine.

Start with: **"Using recorded data only, show the observation timestamps and temperature values for rows near Los Angeles. State which facts are missing before recommending an action."**

Then ask a policy-only question. Compare the sources and tool calls with the answer. The source still has historical data and several documented demo limitations. Do not treat its recommendations as instructions for real cargo.

## 10. Stop and resume

Stop Streamlit with Ctrl+C. Stop SQL from the working copy with:

```bash
docker compose stop sql
```

Resume SQL with `docker compose start sql`, then rerun Streamlit. The volume keeps your database. Do not use a volume-delete command unless you deliberately want to discard it.

Before ending a learning session, record which steps passed in your tracker. Keep secrets and raw session logs out of GitHub. The repository's ignored `work/`, `.env` and `runtime/` paths support this; they do not protect a secret pasted into another tracked file.

## Cloud stage

The original EC2 instructions are available in the submodule for comparison. First complete the local integration and review the [Azure mapping](ARCHITECTURE.md) and [cost plan](COSTS.md). A public deployment additionally needs authentication, HTTPS, network restrictions, monitoring and a tested release/rollback process. None is provisioned by this companion.
