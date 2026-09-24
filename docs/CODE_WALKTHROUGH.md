# Read the code in this order

All original paths below are under `upstream/cold-chain`. The reviewed revision is recorded in [Sources](SOURCES.md). Run `git submodule update --init --recursive` if the folder is empty.

## 1. `scripts/ingest_legacy_data.py`

This is a preparation job, not the chat application's request handler. It reads a CSV with pandas, selects nine columns, renames them into a simulated legacy schema, adds an ingestion flag and writes a SQL table through SQLAlchemy/pyodbc.

The source has 32,065 data rows and 26 CSV columns. Several useful fields are left out of the nine-column selection, including `eta_variation_hours`. There is no actual shipment/truck identifier or cargo type in that source column list. A cargo-condition numeric value does not establish a cargo category.

`to_sql(..., if_exists='replace')` replaces the target table. Use an isolated learning database. It is not an incremental production ingestion design. Consider schema ownership, keys, duplicates, replays, late-arriving records and transactional updates before reusing the pattern.

**Read and explain:** Which columns survive? Which business questions become impossible after the projection?

## 2. `scripts/setup_security_and_view.sql`

The script creates `FDE_VIEWS`, exposes readable aliases through `VW_ACTIVE_FLEET`, creates an agent login/user and grants SELECT on that view. It denies direct raw-table SELECT and several mutations in `dbo`.

This is the right place to teach least privilege: database permissions enforce access even if the model asks for something else. A view by itself does not establish read-only access. The grants and denials matter. `GO` is a client-side batch separator for SQL tooling, not a normal T-SQL statement you pass unmodified through every driver.

Despite the name **ACTIVE_FLEET**, the view has no latest-row or active-status filter. It projects all historical rows. The separate audit instructions grant INSERT on a log table, so the agent identity is read-only for telemetry, not universally read-only.

**Read and explain:** Test the view and raw table with the agent account, not the administrator account.

## 3. `scripts/ingest_sop_pinecone.py`

Follow six stages: resolve paths and environment; choose embeddings; create/attach the index; parse documents; process changes; write the local hash cache.

Markdown is split by headings and then size. Text and PDF pages use recursive splitting (600 characters, 60 overlap in the inspected source). CSV/Excel rows become individual text records. Metadata tracks source filename, format and sometimes page/row. Chunk IDs combine filename and chunk position.

The hash cache tries to skip unchanged files. In the original, a single cache file is shared between embedding modes. A cached source can be skipped even if a fresh index has no vectors. Existing vectors are deleted before replacements are uploaded, so a failure can leave a retrieval gap. There is no transaction spanning local cache and remote vector store.

The local embedding branch assumes 1,024 dimensions; the OpenAI branch assumes 1,536. Changing only the model name is not enough. The index dimension and embedding model must agree for ingestion and queries.

**Read and explain:** What if upload fails halfway? What if the embedding model changes but the document bytes do not?

## 4. `src/agent_tools.py`

The `@tool` decorator exposes a function's name, description and arguments to the agent framework. A tool is ordinary code with a contract; a model does not acquire an independent database identity.

| Function | Input | Work | Output |
|---|---|---|---|
| `query_telemetry_db` | A SQL string | Connect using the configured agent identity; run query; fetch up to ten rows | Text containing column names and records, or an error |
| `fetch_corridor_conditions` | Latitude, longitude | Call Open-Meteo with a six-second HTTP timeout | Weather values and a synthetic wind-based risk score |
| `search_compliance_sop` | Search text | Retrieve two matching chunks from Pinecone | Source-labelled policy passages |

`fetchmany(10)` restricts returned rows, not necessarily database work. It can silently omit matching records from an answer. The SELECT-prefix check is not a SQL parser or a security boundary. Narrow tools, database permissions, timeouts, row limits and tested query restrictions serve different purposes.

The wind-to-congestion score is coded as a two-value heuristic. It is not a traffic service result. In the learning copy the label is changed so this remains visible.

## 5. `src/orchestrator.py`

`AgentState` holds messages. `add_messages` merges message updates. The chosen model is bound to three tools. A reasoner node calls the model; a conditional edge routes to tools if tool calls were returned; results loop back to the reasoner. Otherwise the graph ends.

`MemorySaver` keeps state in memory by thread ID. A restart loses it; multiple app processes do not automatically share it. `temperature=0` is not a guarantee of identical answers or correct facts.

The original system prompt is loaded only in the `if __name__ == '__main__'` block. Importing this module from Streamlit does not run that block. The preparation helper repairs this for the local teaching copy by supplying the prompt at the reasoner boundary.

The source supports OpenAI, DeepSeek and a legacy Ollama class. These are configured alternatives, not an automatic runtime failover system. We have not verified all three provider paths. The companion's documented paid path uses configurable OpenAI calls; the local branch needs its own tool-calling compatibility check.

## 6. `src/prompts/system_prompt.txt`

The prompt asks for SQL, weather and SOP use, followed by a summary, table and action plan. Prompt instructions influence output but cannot enforce database permissions, source freshness or operational approvals. There is also a conflict between always using all tools and the setup notes' example of a simple policy-only query.

**Exercise:** Specify which intents need which tools. Enforce required evidence and allowed actions in code when the consequence matters.

## 7. `src/ui.py`

Streamlit owns session state and assigns a UUID thread ID. It streams graph updates, displays tool traces and records tool arguments, outputs and model text in an audit table. A second panel compares supplied credentials with environment values before opening an admin database connection.

The chat itself does not have enterprise authentication. The audit panel is not equivalent to SSO/RBAC. Administrator database credentials should not be a normal user-facing login mechanism in a real deployment.

Audit-write exceptions are printed and processing continues. The table is writable by administrators and is not independently tamper-proof. The UI does not explicitly log every original user question as a separate audit entry. Its stored traces are application events, not hidden model reasoning.

## 8. `.github/workflows/deploy.yml`

Manual dispatch invokes an SSH action, pulls main into an existing VM folder and restarts a systemd service. It assumes the VM, network, Python environment, secrets and service already exist. It does not create infrastructure or install updated requirements. No automated tests, release artifact, health verification or rollback appear in that workflow.

This companion's workflow runs only offline tests and documentation-link checks. It never provisions or deploys cloud services.

## Original author material

The handwritten notes show the reasoning from business problem through data and tools to the agent loop. The TDD describes intended architecture and security. The business deck explains the operational pitch. Compare these with actual code; design intent is not proof that a feature has been implemented or verified.
