"""Make a local teaching copy of the pinned upstream; never launch services.

The submodule remains unchanged. The generated working directory contains local
passwords and must not be committed. Run this from the companion repository.
"""
import argparse
import ast
import json
import secrets
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "upstream" / "cold-chain"
REVISION = "ef6633928950ef9c13115fb77439ccab40397790"


def replace_once(path, old, new):
    text = path.read_text(encoding="utf-8")
    if text.count(old) != 1:
        raise RuntimeError(f"Patch expected one match in {path.name}; found {text.count(old)}. Stop and review upstream.")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def prepare(target):
    target = target.resolve()
    work = (ROOT / "work").resolve()
    if not target.is_relative_to(work) or target == work:
        raise ValueError("Output must be a new subdirectory inside ignored work/.")
    if target.exists():
        raise ValueError("Output already exists. Preserve it and choose a new --output under work/.")
    revision = subprocess.check_output(["git", "-C", str(SOURCE), "rev-parse", "HEAD"], text=True).strip()
    status = subprocess.check_output(["git", "-C", str(SOURCE), "status", "--porcelain"], text=True)
    if revision != REVISION or status.strip():
        raise ValueError("Upstream must be clean at the documented revision. Run git submodule update --init --recursive.")
    shutil.copytree(SOURCE, target, ignore=shutil.ignore_patterns(".git", ".env", ".env.*", "__pycache__", "*.pyc", "ingestion_hash_cache.json"))
    source_mode = target / "src" / "orchestrator.py"
    replace_once(source_mode,
        'llm = ChatOpenAI(model="gpt-4o", temperature=0)',
        'llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"), temperature=0)')
    replace_once(source_mode,
        'response = llm_with_tools.invoke(state["messages"])',
        'messages = state["messages"]\n'
        '    if not messages or not isinstance(messages[0], SystemMessage):\n'
        '        prompt_path = project_root / "src" / "prompts" / "system_prompt.txt"\n'
        '        messages = [SystemMessage(content=prompt_path.read_text(encoding="utf-8")), *messages]\n'
        '    response = llm_with_tools.invoke(messages)')
    for relative in ["scripts/ingest_sop_pinecone.py", "src/agent_tools.py"]:
        replace_once(target / relative, "embeddings = OpenAIEmbeddings()",
            'embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"))')
    # Never delete an existing vector index to repair a model/index mismatch.
    ingestion = target / "scripts" / "ingest_sop_pinecone.py"
    replace_once(ingestion,
        'pc.delete_index(INDEX_NAME)',
        'raise ValueError("Index dimension mismatch: create a separate teaching index; existing data was preserved.")')
    # Avoid shared ingestion state across embedding models and newly-created indexes.
    replace_once(ingestion,
        'index_client = pc.Index(INDEX_NAME)',
        'HASH_CACHE_FILE = cache_dir / f"ingestion_{INDEX_NAME}_{TARGET_DIMENSION}.json"\n'
        'hash_cache = json.loads(HASH_CACHE_FILE.read_text()) if HASH_CACHE_FILE.exists() else {}\n'
        'index_client = pc.Index(INDEX_NAME)')
    # A synthetic wind heuristic must not be presented as measured traffic data.
    tools_file = target / "src" / "agent_tools.py"
    replace_once(tools_file, 'f"Corridor Risk: {status_note} (Congestion Index: {congestion_index}/10)\\n"',
        'f"Demo weather heuristic: {status_note} (synthetic score: {congestion_index}/10; NOT measured traffic)\\n"')
    # Bound the learning UI's agent loop. Framework retries/costs remain documented.
    replace_once(target / "src" / "ui.py",
        'thread_config = {"configurable": {"thread_id": st.session_state.thread_id}}',
        'thread_config = {"configurable": {"thread_id": st.session_state.thread_id}, "recursion_limit": 12}')
    admin_password = secrets.token_hex(18) + "Aa9!"
    agent_password = secrets.token_hex(18) + "Bb8!"
    env = (
        "# LOCAL TEACHING CREDENTIALS. Do not commit or share this file.\n"
        "SQL_SERVER_HOST=127.0.0.1\nSQL_SERVER_PORT=1433\nSQL_ADMIN_USER=sa\n"
        f"SQL_ADMIN_PASSWORD={admin_password}\nSQL_AGENT_USER=USR_FDE_RO\nSQL_AGENT_PASSWORD={agent_password}\n"
        "Agent_llm=OPENAI\nOPENAI_MODEL=gpt-4.1-mini\nOPENAI_API_KEY=\n"
        "Embeddings_model=OPENAI\nOPENAI_EMBEDDING_MODEL=text-embedding-3-small\nPINECONE_API_KEY=\n"
        "Local_Embedding_Model=BAAI/bge-m3\nLANGSMITH_TRACING=false\n"
    )
    (target / ".env").write_text(env, encoding="utf-8")
    (target / ".env").chmod(0o600)
    security = target / "scripts" / "setup_security_and_view.sql"
    replace_once(security, "AgentPassword2026!", agent_password)
    with security.open("a", encoding="utf-8") as stream:
        stream.write("""\nGO
CREATE TABLE FDE_VIEWS.AgentAuditLog (
    LogID INT IDENTITY(1,1) PRIMARY KEY,
    Timestamp DATETIME DEFAULT GETDATE(),
    SessionID VARCHAR(50), NodeExecuted VARCHAR(50),
    ToolName VARCHAR(100), Content NVARCHAR(MAX)
);
GRANT INSERT ON FDE_VIEWS.AgentAuditLog TO USR_FDE_RO;
GO
""")
    security.chmod(0o600)
    shutil.copy(ROOT / "config" / "compose.yaml", target / "compose.yaml")
    (target / "LOCAL_CHANGES.json").write_text(json.dumps({
        "upstream_revision": REVISION,
        "purpose": "local teaching copy; not production hardened",
        "changes": ["shared system-prompt initialisation", "configurable model and explicit embedding model",
            "fresh index-scoped ingestion cache", "reject destructive index repair",
            "label synthetic weather heuristic", "12-step UI graph limit",
            "random local SQL passwords and audit table grant", "SQL bound to localhost"]
    }, indent=2), encoding="utf-8")
    for path in target.rglob("*.py"):
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    return target


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "work" / "full-project")
    args = parser.parse_args()
    try:
        path = prepare(args.output)
        print(f"Prepared local teaching copy: {path}")
        print("No services launched and no API requests made. Read docs/FULL_PROJECT_SETUP.md next.")
    except (ValueError, RuntimeError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Preparation stopped: {error}\n")
