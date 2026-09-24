# Verification record

**Prepared and checked: 24 September 2026.** Update this file when a new environment or live integration is actually exercised. Do not infer a pass from another layer's test.

| Item | Evidence | Status |
|---|---|---|
| Upstream identity | Git checkout at `ef6633928950ef9c13115fb77439ccab40397790` | Confirmed |
| Offline Python lab | Executed with Python 3.12.14 on Linux x86-64 | Passed |
| Behavioural tests | 12 unittest cases: thresholds, stale/future/missing data, repeat seeding, query parameter handling, mutation refusal, routing and trace preservation | Passed |
| Demo scenario | Three Melbourne results: breach, within fictional limits, unknown current status | Passed |
| Preparation helper | Created isolated working copy; source left clean; parsed all copied Python files without executing them | Passed |
| Preparation controls | Refuses overwrite; confines outputs to `work/`; generated credentials are in ignored local files | Checked |
| Recall-card format and content | 28 unique cards; list/review commands exercised | Checked |
| Cost calculator | Default scenario US$1.62 / AU$2.51 with documented assumptions | Checked |
| Relative companion links | `python scripts/check_docs.py` | Checked before delivery |
| Source supporting material | Code, dataset schema/count, original notes and extracted design/business text reviewed | See source scope |
| Full stack dependency installation | Large upstream requirements not installed in this runtime | Not verified |
| SQL Docker/ODBC integration | Docker unavailable in this runtime | Not verified |
| Pinecone ingestion/retrieval | Requires user's provider account and configured index | Not verified |
| Paid model calls/tool selection | Requires user's API access and evaluation cases | Not verified |
| Streamlit full-stack UI | Depends on the unverified services above | Not verified |
| Cloud or Azure deployment | No resources provisioned | Not performed |
| GitHub workflow run | [Run #1](https://github.com/thisislife433-dotcom/ai-fde-learning/actions/runs/36014466608) on commit `0d06034`: Ubuntu runner with Python 3.12; tests, demo and relative-link check all succeeded | Passed |

## Reproduce local checks

```bash
python -m unittest discover -s tests -v
python -m lab demo
python scripts/review.py --list
python scripts/cost_estimator.py
python scripts/check_docs.py
python scripts/doctor.py
```

Run `python scripts/prepare_full_project.py` only to create a new local teaching copy. It does not execute the original app. A prepared copy is not the same as a fully running integration.

## What the tests establish

The tests check the companion's deterministic behaviour with synthetic records. They do not measure an LLM's accuracy, an embedding model's retrieval quality or production security. The original project's identified limitations remain documented even after convenience patches are applied.

## Evidence to add after your first live run

Record operating system, Python version, dependency lock, SQL container digest, ODBC version, model/deployment, index dimension, date, test cases and outcomes. Never record API keys or passwords. Link a reviewed commit or sanitised test report when useful.
